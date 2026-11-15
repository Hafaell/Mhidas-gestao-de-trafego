"""Seções de vídeo: meio de funil (SecaoVideo) e topo de funil (SecaoVideoTopo).
Cada uma tem página própria: cards à esquerda e funil de verdade à direita."""
from dataclasses import dataclass
from typing import List

from ..formatacao import Formatador as F
from ..metricas import Calculo, Kpi
from .base import Secao


@dataclass
class EtapaFunil:
    """Um trapézio do funil. `pontos` é o atributo `points` do polígono SVG."""
    rotulo: str
    valor: str
    pontos: str
    cor: str
    y_rotulo: float
    y_valor: float


@dataclass
class FunilVideo:
    titulo: str
    etapas: List[EtapaFunil]
    altura_total: int
    retencao_final: str


@dataclass
class ParVideo:
    """Dois cards lado a lado: quantidade em um ponto do vídeo e valor gasto ÷ essa quantidade."""
    quantidade: Kpi
    custo: Kpi


@dataclass
class PainelVideo:
    topo: List[Kpi]
    pares: List[ParVideo]
    funil: FunilVideo


class SecaoVideo(Secao):
    chave = "video"
    etapa = "meio"
    nome_etapa = "Meio"
    rotulo_etapa = "Vídeo"
    titulo = "Vídeo de meio de funil"
    icone = "video"
    campo_evolucao, rotulo_evolucao = "views_15s", "Visualizações 15 seg (meio)"
    campos_desejaveis = ("views_15s", "video_50", "video_75", "video_95")
    tipo_pagina = "video"

    # Desenho do funil: (rótulo, campo, largura do topo, largura da base) em um quadro de 200 de largura.
    # A largura sempre diminui: é forma de funil, não escala (50% pode ser maior que 15 seg).
    FUNIL = [("Vídeo 15 seg", "views_15s", 200, 158),
             ("Vídeo 50%", "video_50", 150, 108),
             ("Vídeo 95%", "video_95", 100, 50)]
    CORES_FUNIL = ["#de6a35", "#c0521f", "#96401a"]   # tons de laranja (cor do Meio), claro para escuro
    ROTULO_COMPARACAO = "vídeo de meio"
    ALTURA_ETAPA, FOLGA = 64, 6
    PARES = [("video_50", "Vídeo 50%"), ("video_75", "Vídeo 75%"), ("video_95", "Vídeo 95%")]

    def __init__(self, dados: dict):
        super().__init__(dados)
        self.tema = dados.get("tema")
        self.painel = self._montar_painel()

    def montar_kpis(self):
        return None   # o vídeo tem painel próprio (ver _montar_painel)

    def _montar_painel(self) -> PainelVideo:
        v, a = self.valor, self.valor_anterior
        topo = [
            Kpi.criar("Valor gasto", self.investido, F.moeda, self.investido_anterior, investimento=True),
            Kpi.criar("Visualização 15 seg", v("views_15s"), F.inteiro, a("views_15s"), destaque=True),
            Kpi.criar("Custo 15 seg", self.custo("views_15s"), F.moeda, self.custo_anterior("views_15s"),
                      menor_melhor=True, destaque=True),
        ]
        if self.dados.get("tempo_medio_s") is not None:   # opcional: 4º card da linha de cima
            topo.append(Kpi.criar("Tempo médio assistido", v("tempo_medio_s"), lambda s: f"{round(s)} s",
                                  a("tempo_medio_s")))
        pares = [ParVideo(
            Kpi.criar(rotulo, v(campo), F.inteiro, a(campo)),
            Kpi.criar(f"Valor gasto / {rotulo}", self.custo(campo), F.moeda, self.custo_anterior(campo),
                      menor_melhor=True),
        ) for campo, rotulo in self.PARES]
        return PainelVideo(topo, pares, self._montar_funil())

    def _montar_funil(self) -> FunilVideo:
        etapas = []
        for i, (rotulo, campo, larg_topo, larg_base) in enumerate(self.FUNIL):
            y0 = i * (self.ALTURA_ETAPA + self.FOLGA)
            y1 = y0 + self.ALTURA_ETAPA
            pontos = (f"{100 - larg_topo / 2:g},{y0} {100 + larg_topo / 2:g},{y0} "
                      f"{100 + larg_base / 2:g},{y1} {100 - larg_base / 2:g},{y1}")
            meio = y0 + self.ALTURA_ETAPA / 2
            etapas.append(EtapaFunil(rotulo, F.inteiro(self.valor(campo)), pontos,
                                     self.CORES_FUNIL[i], meio - 9, meio + 14))
        n = len(self.FUNIL)
        return FunilVideo(
            titulo="Funil de visualização",
            etapas=etapas,
            altura_total=n * self.ALTURA_ETAPA + (n - 1) * self.FOLGA,
            retencao_final=F.percentual(Calculo.dividir(self.valor("video_95"), self.valor("views_15s"))),
        )

    def linhas_comparacao(self):
        return [
            self._linha(f"Visualizações de 15 seg ({self.ROTULO_COMPARACAO})", F.inteiro,
                        self.valor("views_15s"), self.valor_anterior("views_15s")),
            self._linha(f"Custo por 15 seg ({self.ROTULO_COMPARACAO})", F.moeda,
                        self.custo("views_15s"), self.custo_anterior("views_15s"), menor_melhor=True),
        ]


class SecaoVideoTopo(SecaoVideo):
    """Vídeo de topo de funil (campanhas [TOPO][VV] / CP1 ... [VV]), para pessoas que ainda não conhecem o
    cliente. Mesmos cards do vídeo de meio, em azul. Os relatórios feitos à mão de out/2026 tinham as duas
    seções separadas (Topo de Funil Video View e Meio de Funil Video View)."""
    chave = "video_topo"
    etapa = "topo"
    nome_etapa = "Topo"
    rotulo_etapa = "Pessoas novas"
    titulo = "Vídeo de topo de funil"
    campo_evolucao, rotulo_evolucao = "views_15s_topo", "Visualizações 15 seg (topo)"
    dado_evolucao = "views_15s"
    CORES_FUNIL = ["#3d8be0", "#2266b8", "#18498a"]   # tons de azul (cor do Topo), claro para escuro
    ROTULO_COMPARACAO = "vídeo de topo"
