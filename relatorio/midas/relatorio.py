"""O relatório de um cliente: junta o JSON de dados em objetos prontos para o modelo de HTML."""
from __future__ import annotations

import base64
import mimetypes
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import List, Optional

from .config import PASTA_FOTOS
from .formatacao import Formatador
from .metricas import Calculo, Variacao
from .secoes import SECOES_NA_ORDEM, LinhaComparacao, Secao


@dataclass
class Periodo:
    inicio: str   # AAAA-MM-DD
    fim: str

    def texto(self) -> str:
        return f"{Formatador.data(self.inicio)} a {Formatador.data(self.fim)}"

    def texto_curto(self) -> str:
        return f"{Formatador.data_curta(self.inicio)} a {Formatador.data_curta(self.fim)}"

    @property
    def mes(self) -> str:
        """AAAA-MM, usado no nome do arquivo."""
        return self.inicio[:7]


class Cliente:
    """Quem recebe o relatório. A foto vira data URI para o HTML ficar autossuficiente."""

    TITULOS_IGNORADOS = {"dr", "dra"}

    def __init__(self, dados: dict, pasta_fotos: Path):
        self.nome: str = dados["nome"]
        self.descricao: str = dados.get("descricao") or ""
        self.instagram: str = dados.get("instagram") or ""
        self.iniciais: str = self._iniciais(self.nome)
        self.foto: Optional[str] = self._foto_como_data_uri(dados.get("foto"), pasta_fotos)

    @classmethod
    def _iniciais(cls, nome: str) -> str:
        partes = [p for p in re.split(r"\s+", nome) if p and p.lower().rstrip(".") not in cls.TITULOS_IGNORADOS]
        return "".join(p[0] for p in partes[:2]).upper() or "?"

    @staticmethod
    def _foto_como_data_uri(caminho: Optional[str], pasta: Path) -> Optional[str]:
        if not caminho:
            return None
        if caminho.startswith(("http://", "https://", "data:")):
            return caminho
        # Procura ao lado do JSON e, se não achar, em clientes/fotos/ (onde a foto fica guardada).
        arquivo = next((c.resolve() for c in (pasta / caminho, PASTA_FOTOS / caminho) if c.exists()), None)
        if arquivo is None:
            return None
        mime = mimetypes.guess_type(arquivo.name)[0] or "image/jpeg"
        return f"data:{mime};base64,{base64.b64encode(arquivo.read_bytes()).decode()}"


class Relatorio:
    """Tudo que o modelo de HTML precisa: cliente, períodos, seções, totais e comparação."""

    def __init__(self, dados: dict, pasta_fotos: Path):
        self.agencia: str = dados.get("agencia", "Agência Lupa")
        self.cliente = Cliente(dados["cliente"], pasta_fotos)
        self.periodo = Periodo(**dados["periodo"])
        anterior = dados.get("periodo_anterior")
        self.periodo_anterior: Optional[Periodo] = Periodo(**anterior) if anterior else None
        self.observacoes: Optional[str] = dados.get("observacoes")
        self.gerado_em: str = date.today().strftime("%d/%m/%Y")

        self.secoes: List[Secao] = self._montar_secoes(dados.get("secoes", {}))
        self.total: float = sum(s.investido for s in self.secoes)
        self.total_anterior: Optional[float] = self._somar_anterior()
        for s in self.secoes:
            s.definir_participacao(self.total)
        self.comparacao: List[LinhaComparacao] = self._montar_comparacao() if self.periodo_anterior else []

    # ---- montagem ----

    @staticmethod
    def _montar_secoes(dados_secoes: dict) -> List[Secao]:
        """Só entram as seções que existem no JSON, sempre na ordem topo, meio, fundo."""
        return [classe(dados_secoes[classe.chave])
                for classe in SECOES_NA_ORDEM if dados_secoes.get(classe.chave)]

    def _somar_anterior(self) -> Optional[float]:
        partes = [s.investido_anterior for s in self.secoes]
        return sum(partes) if all(p is not None for p in partes) else None

    def _montar_comparacao(self) -> List[LinhaComparacao]:
        total = LinhaComparacao(
            "Investimento total", None, Formatador.moeda(self.total), Formatador.moeda(self.total_anterior),
            Variacao.calcular(self.total, self.total_anterior, neutra=True))
        return [total] + [linha for s in self.secoes for linha in s.linhas_comparacao()]

    # ---- o que o HTML mostra ----

    @property
    def total_fmt(self) -> str:
        return Formatador.moeda(self.total)

    @property
    def total_variacao(self) -> Optional[Variacao]:
        return Variacao.calcular(self.total, self.total_anterior, neutra=True)

    @property
    def periodo_txt(self) -> str:
        return self.periodo.texto()

    @property
    def anterior_txt(self) -> Optional[str]:
        return self.periodo_anterior.texto_curto() if self.periodo_anterior else None

    @property
    def nome_arquivo(self) -> str:
        """Ex.: relatorio-dra-ana-exemplo-2026-10 (sem extensão)."""
        return f"relatorio-{Formatador.slug(self.cliente.nome)}-{self.periodo.mes}"
