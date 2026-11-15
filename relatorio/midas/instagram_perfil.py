"""Números do perfil do Instagram num período (API do Instagram, Graph v25.0), sem nunca imprimir o token.

A API aceita no máximo 30 dias por consulta (testado em 15/11/2026: "There cannot be more than 30 days
between since and until"). Um mês de 31 dias vira duas consultas, e os números são somados.
Visitas, cliques na bio e novos seguidores podem ser somados.

Alcance: o relatório feito à mão usava a SOMA DO ALCANCE DE CADA DIA (conferido em 15/11/2026 no Kondo,
out/2026: soma diária 1.139.568 contra 1.109.430 no PDF; o alcance único do mês dá ~793 mil). O campo `alcance`
é essa soma diária. `alcance_unico` é o alcance sem repetir pessoa (aproximado se houver mais de uma janela).
"""
from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from typing import Callable, List, Optional, Tuple

from .token_instagram import VERSAO_API, TokenInstagram

MAX_DIAS = 30


class ErroInstagram(Exception):
    def __init__(self, mensagem: str, codigo: Optional[int] = None):
        super().__init__(mensagem)
        self.codigo = codigo   # 190 = token vencido ou inválido


@dataclass
class NumerosPerfil:
    visitas_perfil_total: int     # profile_views
    cliques_bio_total: int        # website_clicks
    alcance: int                  # soma do reach de cada dia (como no relatório feito à mão)
    novos_seguidores: int         # follows_and_unfollows, follow_type = FOLLOWER (seguidores novos do perfil)
    alcance_unico: int            # reach total_value (aproximado se janelas > 1)
    janelas: int
    alcance_unico_aproximado: bool


class PerfilInstagram:
    def __init__(self, ig_user_id: str, token: Optional[str] = None,
                 buscar: Optional[Callable[[str], dict]] = None):
        self.ig = ig_user_id
        self.token = token or TokenInstagram.ler_token()
        if not self.token:
            raise ErroInstagram("ACCESS_TOKEN não encontrado no .env")
        self.buscar = buscar or self._buscar_na_internet

    @staticmethod
    def janelas(inicio: str, fim: str) -> List[Tuple[str, str]]:
        """Divide o período (fim incluído) em janelas de até 30 dias. Cada janela volta como (since, until),
        com o until EXCLUSIVO (dia seguinte ao último), como a API pede."""
        ini, ult = date.fromisoformat(inicio), date.fromisoformat(fim)
        saida = []
        while ini <= ult:
            ate = min(ini + timedelta(days=MAX_DIAS - 1), ult)
            saida.append((ini.isoformat(), (ate + timedelta(days=1)).isoformat()))
            ini = ate + timedelta(days=1)
        return saida

    def numeros(self, inicio: str, fim: str) -> NumerosPerfil:
        soma = {"profile_views": 0, "website_clicks": 0, "reach": 0, "seguidores": 0, "reach_diario": 0}
        janelas = self.janelas(inicio, fim)
        for since, until in janelas:
            base = {"period": "day", "metric_type": "total_value", "since": since, "until": until}
            dados = self._consultar({**base, "metric": "profile_views,website_clicks,reach"})
            for item in dados:
                soma[item["name"]] += item["total_value"]["value"]
            diario = self._consultar({"metric": "reach", "period": "day", "since": since, "until": until})
            soma["reach_diario"] += sum(v["value"] for v in diario[0].get("values", []))
            seg = self._consultar({**base, "metric": "follows_and_unfollows", "breakdown": "follow_type"})
            for r in seg[0]["total_value"]["breakdowns"][0]["results"]:
                if r["dimension_values"] == ["FOLLOWER"]:
                    soma["seguidores"] += r["value"]
        return NumerosPerfil(soma["profile_views"], soma["website_clicks"], soma["reach_diario"], soma["seguidores"],
                             soma["reach"], len(janelas), len(janelas) > 1)

    def _consultar(self, params: dict) -> list:
        query = urllib.parse.urlencode({**params, "access_token": self.token})
        resposta = self.buscar(f"https://graph.facebook.com/{VERSAO_API}/{self.ig}/insights?{query}")
        if "error" in resposta:
            erro = resposta["error"]
            raise ErroInstagram(erro.get("message", "erro desconhecido"), erro.get("code"))
        return resposta["data"]

    @staticmethod
    def _buscar_na_internet(url: str) -> dict:
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            try:
                return json.loads(e.read())
            except (json.JSONDecodeError, ValueError):
                return {"error": {"message": f"HTTP {e.code}"}}


def como_dict(n: NumerosPerfil) -> dict:
    return asdict(n)
