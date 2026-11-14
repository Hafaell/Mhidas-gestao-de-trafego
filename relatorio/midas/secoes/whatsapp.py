"""Seção Captação de leads no WhatsApp (fundo de funil)."""
from ..formatacao import Formatador as F
from ..metricas import Calculo, Kpi
from .base import Fluxo, PassoFluxo, Secao


class SecaoWhatsapp(Secao):
    chave = "whatsapp"
    etapa = "fundo"
    nome_etapa = "Fundo"
    rotulo_etapa = "Foco em consulta"
    titulo = "Captação de leads no WhatsApp"
    icone = "whatsapp"
    campo_evolucao, rotulo_evolucao = "conversas", "Conversas iniciadas"
    campos_desejaveis = ("impressoes", "alcance", "cliques", "conversas")

    def montar_kpis(self):
        v, a = self.valor, self.valor_anterior
        return [
            Kpi.criar("Valor investido", self.investido, F.moeda, self.investido_anterior, investimento=True),
            Kpi.criar("Impressões", v("impressoes"), F.inteiro, a("impressoes")),
            Kpi.criar("Alcance", v("alcance"), F.inteiro, a("alcance")),
            Kpi.criar("Cliques", v("cliques"), F.inteiro, a("cliques")),
            Kpi.criar("Conversas iniciadas", v("conversas"), F.inteiro, a("conversas"), destaque=True),
            Kpi.criar("Custo por conversa", self.custo("conversas"), F.moeda,
                      self.custo_anterior("conversas"), menor_melhor=True, destaque=True),
        ]

    def montar_fluxo(self):
        v = self.valor
        return Fluxo("Do anúncio à conversa", [
            PassoFluxo("Impressões", F.inteiro(v("impressoes"))),
            PassoFluxo("Cliques", F.inteiro(v("cliques")),
                       F.percentual(Calculo.dividir(v("cliques"), v("impressoes")), 2), "clicaram no anúncio"),
            PassoFluxo("Conversas iniciadas", F.inteiro(v("conversas")),
                       F.percentual(Calculo.dividir(v("conversas"), v("cliques"))), "dos cliques viraram conversa"),
        ])

    def linhas_comparacao(self):
        return [
            self._linha("Conversas iniciadas", F.inteiro,
                        self.valor("conversas"), self.valor_anterior("conversas")),
            self._linha("Custo por conversa", F.moeda,
                        self.custo("conversas"), self.custo_anterior("conversas"), menor_melhor=True),
        ]
