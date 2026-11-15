"""Seção Campanhas de landing page (fundo de funil): anúncio que leva ao site e gera lead (formulário,
agendamento). Clientes: Dr. Raphael Kondo e Doc Circle (relatórios feitos à mão de out/2026)."""
from ..formatacao import Formatador as F
from ..metricas import Calculo, Kpi
from .base import Fluxo, PassoFluxo, Secao


class SecaoLandingPage(Secao):
    chave = "landing_page"
    etapa = "fundo"
    nome_etapa = "Fundo"
    rotulo_etapa = "Foco em consulta"
    titulo = "Campanhas de landing page"
    titulo_curto = "Landing page"
    icone = "globo"
    cor_icone = "var(--topo)"   # ícone azul (pedido do gestor, 15/11/2026); a linha do título segue verde, do Fundo
    campo_evolucao, rotulo_evolucao = "leads", "Leads da landing page"
    campos_desejaveis = ("impressoes", "cliques", "visualizacoes_pagina", "leads")

    def __init__(self, dados: dict):
        # Nome do resultado: "Leads" (padrão) ou o que o gestor usava no relatório, ex.: "Conversões" (Doc Circle).
        self.nome_resultado = dados.get("nome_resultado") or "Leads"
        self.singular = self.SINGULAR.get(self.nome_resultado, self.nome_resultado.lower())
        super().__init__(dados)

    SINGULAR = {"Leads": "lead", "Conversões": "conversão", "Agendamentos": "agendamento"}

    def montar_kpis(self):
        v, a, r = self.valor, self.valor_anterior, self.nome_resultado
        return [
            Kpi.criar("Valor investido", self.investido, F.moeda, self.investido_anterior, investimento=True),
            Kpi.criar("Impressões", v("impressoes"), F.inteiro, a("impressoes")),
            Kpi.criar("Cliques no link", v("cliques"), F.inteiro, a("cliques")),
            Kpi.criar("Visualizações da página", v("visualizacoes_pagina"), F.inteiro, a("visualizacoes_pagina")),
            Kpi.criar(r, v("leads"), F.inteiro, a("leads"), destaque=True),
            Kpi.criar(f"Custo por {self.singular}", self.custo("leads"), F.moeda, self.custo_anterior("leads"),
                      menor_melhor=True, destaque=True),
        ]

    def montar_fluxo(self):
        v = self.valor
        return Fluxo("Do clique ao lead", [
            PassoFluxo("Cliques no link", F.inteiro(v("cliques"))),
            PassoFluxo("Visualizações da página", F.inteiro(v("visualizacoes_pagina")),
                       F.percentual(Calculo.dividir(v("visualizacoes_pagina"), v("cliques"))), "carregaram a página"),
            PassoFluxo(self.nome_resultado, F.inteiro(v("leads")),
                       F.percentual(Calculo.dividir(v("leads"), v("visualizacoes_pagina"))), "das visitas viraram lead"),
        ])

    def linhas_comparacao(self):
        r = self.nome_resultado
        return [
            self._linha(f"{r} da landing page", F.inteiro, self.valor("leads"), self.valor_anterior("leads")),
            self._linha(f"Custo por {self.singular} (landing page)", F.moeda,
                        self.custo("leads"), self.custo_anterior("leads"), menor_melhor=True),
        ]
