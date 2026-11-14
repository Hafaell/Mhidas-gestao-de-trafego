"""Contas e peças de métrica: divisão segura, variação contra o período anterior e card (Kpi)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from .formatacao import Formatador


class Calculo:
    @staticmethod
    def dividir(a, b):
        """a ÷ b, ou None quando falta dado ou o divisor é zero."""
        if a is None or b in (None, 0):
            return None
        return a / b


@dataclass
class Variacao:
    """Selo "▲ 12,3%". `estado` pinta o selo: bom (verde), ruim (vermelho) ou neutro (cinza)."""
    texto: str
    estado: str

    @classmethod
    def calcular(cls, atual, anterior, menor_melhor: bool = False, neutra: bool = False) -> Optional["Variacao"]:
        """None se não houver base de comparação.

        menor_melhor: para custos, cair é bom.
        neutra: para investimento, que não é nem bom nem ruim (selo sempre cinza).
        """
        if atual is None or anterior in (None, 0):
            return None
        pct = (atual - anterior) / anterior
        if neutra or abs(pct) < 0.005:
            estado = "neutro"
        else:
            melhorou = pct < 0 if menor_melhor else pct > 0
            estado = "bom" if melhorou else "ruim"
        seta = "▲" if pct > 0 else ("▼" if pct < 0 else "•")
        return cls(f"{seta} {Formatador.percentual(abs(pct))}", estado)


@dataclass
class Kpi:
    """Um card do relatório: rótulo, valor já formatado e variação."""
    rotulo: str
    valor: str
    variacao: Optional[Variacao] = None
    nota: Optional[str] = None
    destaque: bool = False

    @classmethod
    def criar(cls, rotulo: str, valor, formatar: Callable, anterior=None, *,
              menor_melhor: bool = False, investimento: bool = False,
              nota: Optional[str] = None, destaque: bool = False) -> "Kpi":
        """Monta o card a partir do número cru (formata o valor e calcula a variação)."""
        variacao = Variacao.calcular(valor, anterior, menor_melhor=menor_melhor, neutra=investimento)
        return cls(rotulo, formatar(valor), variacao, nota, destaque)
