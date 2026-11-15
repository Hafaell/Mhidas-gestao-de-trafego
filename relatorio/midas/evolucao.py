"""Gráfico de evolução: uma linha pequena por indicador, com os últimos meses."""
from __future__ import annotations

import calendar
from dataclasses import dataclass
from datetime import date
from typing import Callable, Dict, List, NamedTuple, Optional, Tuple

from .formatacao import MESES, Formatador as F
from .historico import Historico
from .metricas import Variacao

MAX_MESES = 6


class Indicador(NamedTuple):
    campo: str
    rotulo: str
    cor: str
    formatar: Callable
    neutra: bool       # investimento: o selo de variação fica sempre cinza
    atual: Optional[float]
    anterior: Optional[float]


@dataclass
class Ponto:
    x: float
    y: float
    rotulo: str       # "out", ou "nov*" quando o mês é parcial
    valor: str
    ultimo: bool
    y_valor: float = 0.0  # onde escrever o valor: acima do ponto, ou abaixo se ele for um vale da linha


@dataclass
class CardEvolucao:
    rotulo: str
    cor: str                      # variável CSS: --topo, --meio, --fundo ou --navy-2
    valor: str                    # valor do mês do relatório
    variacao: Optional[Variacao]  # contra o mês anterior da série
    pontos: List[Ponto]
    linha: str                    # atributo `points` do polyline SVG


class Evolucao:
    """Monta os cards de evolução a partir do histórico do cliente e dos dados do próprio relatório.

    O mês do relatório e o período anterior vêm do próprio JSON (então o gráfico já nasce com 2 pontos
    no primeiro relatório); os meses mais antigos vêm do histórico gravado em clientes/historico/.
    """

    # Medidas do desenho (viewBox 0 0 120 ALTURA no relatorio.html.j2). Acima da linha fica o valor
    # de cada mês; abaixo, o nome do mês (Y_MES).
    LARGURA, MARGEM = 120, 10
    ALTURA, TOPO_LINHA, BASE_LINHA, Y_MES = 80, 15, 54, 76
    ACIMA, ABAIXO = -5, 9  # distância do valor até o ponto

    def __init__(self, relatorio, historico: Optional[Historico]):
        self.r = relatorio
        self.hist = historico
        self.cards: List[CardEvolucao] = self._montar()
        self.tem_parcial = any(p.rotulo.endswith("*") for c in self.cards for p in c.pontos)

    # ---- origem dos números ----

    def indicadores(self) -> List[Indicador]:
        r = self.r
        itens = [Indicador("investido", "Investimento total", "var(--navy-2)", F.moeda, True,
                           r.total, r.total_anterior)]
        # Seção repetida (ex.: WhatsApp por cidade) vira um indicador só, com a soma dos blocos.
        vistos: Dict[str, int] = {}
        for s in r.secoes:
            if not s.campo_evolucao:
                continue
            dado = s.dado_evolucao or s.campo_evolucao
            atual, anterior = s.dados.get(dado), s.anterior.get(dado)
            if s.campo_evolucao in vistos:
                i = vistos[s.campo_evolucao]
                ant = itens[i]
                itens[i] = ant._replace(atual=self._somar(ant.atual, atual), anterior=self._somar(ant.anterior, anterior))
                continue
            vistos[s.campo_evolucao] = len(itens)
            itens.append(Indicador(s.campo_evolucao, s.rotulo_evolucao, f"var(--{s.etapa})", F.inteiro, False,
                                   atual, anterior))
        return itens

    @staticmethod
    def _somar(a, b):
        return None if a is None or b is None else a + b

    @staticmethod
    def _parcial(inicio: str, fim: str) -> bool:
        d = date.fromisoformat(fim)
        return inicio[:7] != fim[:7] or d.day != calendar.monthrange(d.year, d.month)[1] or inicio[8:] != "01"

    def _serie(self, campo: str, atual, anterior) -> List[Tuple[str, float, bool]]:
        r = self.r
        meses: Dict[str, Tuple[Optional[float], bool]] = {}
        if self.hist:
            for mes, v in self.hist.meses_antes_de(r.periodo.mes):
                meses[mes] = (v.get(campo), self._parcial(v["inicio"], v["fim"]))
        if r.periodo_anterior and r.periodo_anterior.mes not in meses:
            pa = r.periodo_anterior
            meses[pa.mes] = (anterior, self._parcial(pa.inicio, pa.fim))
        meses[r.periodo.mes] = (atual, self._parcial(r.periodo.inicio, r.periodo.fim))
        serie = [(m, v, parcial) for m, (v, parcial) in sorted(meses.items()) if v is not None]
        return serie[-MAX_MESES:]

    # ---- desenho ----

    def _montar(self) -> List[CardEvolucao]:
        cards = []
        for i in self.indicadores():
            serie = self._serie(i.campo, i.atual, i.anterior)
            if len(serie) < 2 or serie[-1][0] != self.r.periodo.mes:
                continue
            cards.append(self._card(i.rotulo, i.cor, i.formatar, i.neutra, serie))
        return cards

    def _card(self, rotulo, cor, formatar: Callable, neutra: bool, serie) -> CardEvolucao:
        valores = [v for _, v, _ in serie]
        menor, maior = min(valores), max(valores)
        n = len(serie)
        pontos = []
        for i, (mes, v, parcial) in enumerate(serie):
            x = self.MARGEM + i * (self.LARGURA - 2 * self.MARGEM) / (n - 1)
            falta = (v - menor) / (maior - menor) if maior != menor else 0.5
            y = self.BASE_LINHA - falta * (self.BASE_LINHA - self.TOPO_LINHA)
            nome_mes = MESES[int(mes[5:7]) - 1] + ("*" if parcial else "")
            pontos.append(Ponto(round(x, 1), round(y, 1), nome_mes, formatar(v), i == n - 1))
        # Valor abaixo do ponto quando ele é um vale (mais baixo que os vizinhos), para não cruzar a linha.
        for i, p in enumerate(pontos):
            vizinhos = [q.y for q in pontos[max(i - 1, 0):i + 2] if q is not p]
            vale = all(p.y > y for y in vizinhos)
            p.y_valor = round(p.y + (self.ABAIXO if vale else self.ACIMA), 1)
        linha = " ".join(f"{p.x},{p.y}" for p in pontos)
        variacao = Variacao.calcular(valores[-1], valores[-2], neutra=neutra, menor_melhor=False)
        return CardEvolucao(rotulo, cor, formatar(valores[-1]), variacao, pontos, linha)
