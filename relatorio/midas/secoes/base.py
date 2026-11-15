"""Classe base das seções do relatório (Instagram, vídeo, landing page, WhatsApp)."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable, List, Optional

from ..formatacao import Formatador
from ..metricas import Calculo, Kpi, Variacao


@dataclass
class PassoFluxo:
    """Uma etapa do fluxo. `taxa` é a conversão vinda da etapa anterior (o primeiro passo não tem)."""
    rotulo: str
    valor: str
    taxa: Optional[str] = None
    taxa_txt: Optional[str] = None


@dataclass
class Fluxo:
    titulo: str
    passos: List[PassoFluxo]


@dataclass
class LinhaComparacao:
    """Uma linha da tabela "este período x período anterior"."""
    rotulo: str
    etapa: Optional[str]
    atual: str
    anterior: str
    variacao: Optional[Variacao]


class Secao(ABC):
    """Uma seção do relatório. Cada subclasse diz de qual etapa do funil é e como monta seus cards.

    As subclasses definem os atributos de classe (chave, etapa, títulos) e implementam
    `montar_kpis`, `montar_fluxo` e `linhas_comparacao`.

    Uma seção pode aparecer mais de uma vez (ex.: WhatsApp de São Paulo e de Campinas): no JSON, a chave
    recebe uma lista, e cada item traz `bloco` ("São Paulo"), que vai no título e na tabela de comparação.
    """

    chave: str            # nome da seção no JSON de dados
    etapa: str            # topo, meio ou fundo (define a cor)
    nome_etapa: str       # "Topo", "Meio", "Fundo"
    rotulo_etapa: str     # "Pessoas novas", "Vídeo", "Foco em consulta"
    titulo: str
    titulo_curto: Optional[str] = None      # usado quando a seção se repete (cabe junto com o nome do bloco)
    icone: str
    cor_icone: Optional[str] = None         # fundo do ícone redondo (cor ou gradiente CSS); sem valor, usa a cor da etapa
    campo_evolucao: Optional[str] = None    # campo do JSON que vira gráfico de evolução mensal
    rotulo_evolucao: str = ""
    dado_evolucao: Optional[str] = None     # campo dos dados da seção que vai para o gráfico (padrão: campo_evolucao)
    campos_obrigatorios: tuple = ()         # sem esses campos o relatório não sai (ver conferencia.py)
    campos_desejaveis: tuple = ()           # sem esses campos sai, com aviso (pendência)
    tipo_pagina: str = "bloco"              # "bloco" (cards, várias seções por página) ou "video" (página própria)
    sem_investimento: bool = False          # seção só com números orgânicos: fica fora do total e da barra

    def __init__(self, dados: dict):
        self.dados = dados
        self.anterior = dados.get("anterior", {})
        self.investido = 0.0 if self.sem_investimento else dados["investido"]
        self.investido_anterior = None if self.sem_investimento else self.anterior.get("investido")
        self.comentario = dados.get("comentario")
        self.participacao = 0.0                 # fatia do investimento total (0 a 1)
        self.bloco: Optional[str] = dados.get("bloco")   # nome do bloco quando a seção se repete (cidade, tema)
        self.tema: Optional[str] = dados.get("tema") or self.bloco   # vai no título: "WhatsApp · São Paulo"
        self.extras: tuple = tuple(dados.get("extras") or ())        # cards a mais pedidos pelo gestor
        self.painel = None                      # só o vídeo usa
        self.kpis: Optional[List[Kpi]] = self.montar_kpis()
        self.fluxo: Optional[Fluxo] = self.montar_fluxo()

    # ---- o que cada seção implementa ----

    @abstractmethod
    def montar_kpis(self) -> Optional[List[Kpi]]:
        """Os cards da seção."""

    def montar_fluxo(self) -> Optional[Fluxo]:
        """Fluxo com taxas entre etapas. Seções sem fluxo devolvem None."""
        return None

    @abstractmethod
    def linhas_comparacao(self) -> List[LinhaComparacao]:
        """Linhas desta seção na tabela de comparação com o período anterior."""

    # ---- apoio compartilhado ----

    @property
    def titulo_exibido(self) -> str:
        """Título do cabeçalho da seção: "Captação de leads no WhatsApp" ou "Leads no WhatsApp · São Paulo"."""
        titulo = self.titulo_curto if (self.bloco and self.titulo_curto) else self.titulo
        return f"{titulo} · {self.tema}" if self.tema else titulo

    @property
    def id(self) -> str:
        """Nome único da seção no relatório: "whatsapp" ou, se ela se repete, "whatsapp:São Paulo"."""
        return f"{self.chave}:{self.bloco}" if self.bloco else self.chave

    def definir_participacao(self, total: float) -> None:
        self.participacao = Calculo.dividir(self.investido, total) or 0

    @property
    def investido_fmt(self) -> str:
        return Formatador.moeda(self.investido)

    @property
    def participacao_fmt(self) -> str:
        return Formatador.percentual(self.participacao, 0)

    def valor(self, campo: str):
        return self.dados[campo]

    def valor_anterior(self, campo: str):
        return self.anterior.get(campo)

    def custo(self, campo: str):
        """Investido ÷ campo (ex.: custo por seguidor). Nunca digitado, sempre calculado."""
        return Calculo.dividir(self.investido, self.valor(campo))

    def custo_anterior(self, campo: str):
        return Calculo.dividir(self.investido_anterior, self.valor_anterior(campo))

    def _linha(self, rotulo: str, formatar: Callable, atual, anterior, menor_melhor: bool = False) -> LinhaComparacao:
        if self.bloco:
            rotulo = f"{rotulo} · {self.bloco}"
        return LinhaComparacao(rotulo, self.etapa, formatar(atual), formatar(anterior),
                               Variacao.calcular(atual, anterior, menor_melhor=menor_melhor))
