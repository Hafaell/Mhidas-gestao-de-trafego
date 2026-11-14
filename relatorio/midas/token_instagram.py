"""Verifica o ACCESS_TOKEN do Instagram (Graph API) sem nunca imprimir o token."""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Callable, Optional

from .config import RAIZ

VERSAO_API = "v25.0"
DIAS_DE_AVISO = 7

OK, VENCENDO, INVALIDO, NAO_VERIFICADO = 0, 1, 2, 3   # códigos de saída do verificar_token.py


@dataclass
class ResultadoToken:
    codigo: int
    mensagem: str


class TokenInstagram:
    def __init__(self, buscar: Optional[Callable[[str], dict]] = None, agora: Optional[datetime] = None):
        self.buscar = buscar or self._buscar_na_internet
        self.agora = agora or datetime.now(timezone.utc)

    # ---- token ----

    @staticmethod
    def ler_token() -> Optional[str]:
        """Variável de ambiente ACCESS_TOKEN ou linha ACCESS_TOKEN= do .env na raiz do projeto."""
        if os.environ.get("ACCESS_TOKEN"):
            return os.environ["ACCESS_TOKEN"].strip()
        env = RAIZ / ".env"
        if env.exists():
            for linha in env.read_text(encoding="utf-8").splitlines():
                chave, _, valor = linha.partition("=")
                if chave.strip() == "ACCESS_TOKEN":
                    return valor.strip().strip("'\"") or None
        return None

    # ---- consulta ----

    @staticmethod
    def _buscar_na_internet(token: str) -> dict:
        """debug_token com o próprio token do usuário. Devolve o JSON; erro HTTP também vira JSON."""
        query = urllib.parse.urlencode({"input_token": token, "access_token": token})
        url = f"https://graph.facebook.com/{VERSAO_API}/debug_token?{query}"
        try:
            with urllib.request.urlopen(url, timeout=20) as resposta:
                return json.loads(resposta.read())
        except urllib.error.HTTPError as erro:
            try:
                return json.loads(erro.read())
            except (json.JSONDecodeError, ValueError):
                return {"error": {"message": f"HTTP {erro.code}"}}

    def verificar(self, token: Optional[str] = None) -> ResultadoToken:
        token = token or self.ler_token()
        if not token:
            return ResultadoToken(NAO_VERIFICADO, "Não achei ACCESS_TOKEN no .env nem no ambiente. "
                                                  "Veja a renovação em memoria/relatorio-meta-ads.md.")
        try:
            resposta = self.buscar(token)
        except (urllib.error.URLError, TimeoutError, OSError) as erro:
            return ResultadoToken(NAO_VERIFICADO, f"Não consegui falar com a Meta ({erro.__class__.__name__}). "
                                                  "Tente de novo antes de gerar relatórios.")
        return self._interpretar(resposta)

    def _interpretar(self, resposta: dict) -> ResultadoToken:
        if "error" in resposta:
            erro = resposta["error"]
            if erro.get("code") == 190:
                return ResultadoToken(INVALIDO, "Token vencido ou inválido (erro 190). Renove antes de gerar "
                                                "relatórios: memoria/relatorio-meta-ads.md, seção do token.")
            return ResultadoToken(NAO_VERIFICADO, f"A Meta recusou a consulta: {erro.get('message', 'sem detalhe')}")
        dados = resposta.get("data", {})
        if not dados.get("is_valid", False):
            return ResultadoToken(INVALIDO, "Token inválido. Renove antes de gerar relatórios.")
        expira = dados.get("expires_at", 0)
        if not expira:
            return ResultadoToken(OK, "Token válido, sem data de vencimento informada.")
        vence = datetime.fromtimestamp(expira, tz=timezone.utc)
        dias = (vence - self.agora).days
        data = vence.astimezone().strftime("%d/%m/%Y")
        if vence <= self.agora:
            return ResultadoToken(INVALIDO, f"Token venceu em {data}. Renove antes de gerar relatórios.")
        if vence - self.agora < timedelta(days=DIAS_DE_AVISO):
            return ResultadoToken(VENCENDO, f"Token vence em {data} (faltam {dias} dias). Renove já, para o "
                                            "clique na bio não falhar no meio de um lote.")
        return ResultadoToken(OK, f"Token válido até {data} (faltam {dias} dias).")
