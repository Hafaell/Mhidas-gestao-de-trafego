"""Seção Crescimento do Instagram (topo de funil)."""
from ..formatacao import Formatador as F
from ..metricas import Calculo, Kpi
from .base import Fluxo, LinhaComparacao, PassoFluxo, Secao


class SecaoInstagram(Secao):
    chave = "instagram"
    etapa = "topo"
    nome_etapa = "Topo"
    rotulo_etapa = "Pessoas novas"
    titulo = "Crescimento do Instagram"
    icone = "instagram"
    campo_evolucao, rotulo_evolucao = "novos_seguidores", "Novos seguidores"
    campos_obrigatorios = ("cliques_bio",)     # regra do gestor: nunca fica "–"
    campos_desejaveis = ("alcance", "visitas_perfil", "novos_seguidores")

    def montar_kpis(self):
        v, a = self.valor, self.valor_anterior
        return [
            Kpi.criar("Valor investido", self.investido, F.moeda, self.investido_anterior, investimento=True),
            Kpi.criar("Alcance", v("alcance"), F.inteiro, a("alcance")),
            Kpi.criar("Visitas ao perfil", v("visitas_perfil"), F.inteiro, a("visitas_perfil")),
            Kpi.criar("Cliques na bio", v("cliques_bio"), F.inteiro, a("cliques_bio")),
            Kpi.criar("Novos seguidores", v("novos_seguidores"), F.inteiro, a("novos_seguidores"), destaque=True),
            Kpi.criar("Custo por seguidor", self.custo("novos_seguidores"), F.moeda,
                      self.custo_anterior("novos_seguidores"), menor_melhor=True, destaque=True),
        ]

    def montar_fluxo(self):
        v = self.valor
        return Fluxo("Do alcance ao seguidor", [
            PassoFluxo("Alcance", F.inteiro(v("alcance"))),
            PassoFluxo("Visitas ao perfil", F.inteiro(v("visitas_perfil")),
                       F.percentual(Calculo.dividir(v("visitas_perfil"), v("alcance"))), "visitaram o perfil"),
            PassoFluxo("Novos seguidores", F.inteiro(v("novos_seguidores")),
                       F.percentual(Calculo.dividir(v("novos_seguidores"), v("visitas_perfil"))),
                       "das visitas viraram seguidores"),
        ])

    def linhas_comparacao(self):
        return [
            self._linha("Novos seguidores", F.inteiro,
                        self.valor("novos_seguidores"), self.valor_anterior("novos_seguidores")),
            self._linha("Custo por seguidor", F.moeda,
                        self.custo("novos_seguidores"), self.custo_anterior("novos_seguidores"), menor_melhor=True),
        ]
