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
    # Regra do gestor (15/11/2026): o card "Cliques na bio" mostra a ESTIMATIVA dos cliques vindos de anúncio.
    # O JSON traz os números crus (cliques_bio_total e visitas_perfil_total da API do Instagram, visitas_perfil
    # do Meta Ads) e o gerador calcula cliques_bio. Sem um deles a estimativa não sai e o relatório para.
    campos_obrigatorios = ("cliques_bio_total", "visitas_perfil_total", "cliques_bio")
    campos_desejaveis = ("alcance", "novos_seguidores")

    def __init__(self, dados: dict):
        for bloco in (dados, dados.get("anterior") or {}):
            if "cliques_bio_total" in bloco:
                bloco["cliques_bio"] = self.estimar_cliques_bio(
                    bloco.get("cliques_bio_total"), bloco.get("visitas_perfil"), bloco.get("visitas_perfil_total"))
        super().__init__(dados)

    @staticmethod
    def estimar_cliques_bio(cliques_total, visitas_anuncio, visitas_total):
        """Cliques na bio via anúncio ≈ cliques na bio × visitas ao perfil via anúncio ÷ visitas totais ao perfil.

        Supõe que quem chega pelo anúncio clica na bio na mesma taxa de quem chega pelo orgânico.
        A fração fica limitada a 100% (a conferência avisa quando as visitas via anúncio passam do total).
        """
        fracao = Calculo.dividir(visitas_anuncio, visitas_total)
        if cliques_total is None or fracao is None:
            return None
        return round(cliques_total * min(fracao, 1.0))

    def montar_kpis(self):
        v, a = self.valor, self.valor_anterior
        return [
            Kpi.criar("Valor investido", self.investido, F.moeda, self.investido_anterior, investimento=True),
            Kpi.criar("Alcance", v("alcance"), F.inteiro, a("alcance")),
            Kpi.criar("Visitas ao perfil", v("visitas_perfil"), F.inteiro, a("visitas_perfil")),
            Kpi.criar("Cliques na bio (est. anúncio)", v("cliques_bio"), F.inteiro, a("cliques_bio")),
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
