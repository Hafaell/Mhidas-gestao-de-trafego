"""Conferência dos dados antes de gerar o relatório.

Dois níveis:
    ERRO   o relatório NÃO sai (dado obrigatório faltando, total que não bate com a API, valor negativo).
    AVISO  o relatório sai, mas o problema vira pendência para o gestor.
"""
from __future__ import annotations

import sys
from typing import List, Optional

from .formatacao import Formatador as F

TOLERANCIA_REAIS = 0.01

# (campo maior, campo menor, texto). Se o "menor" passar do "maior", algo está estranho.
# Vídeo fica de fora de propósito: 50% pode passar do ThruPlay (ver memória do relatório).
FUNIS = {
    "instagram": [("alcance", "visitas_perfil", "visitas ao perfil maiores que o alcance"),
                  ("visitas_perfil", "novos_seguidores", "mais seguidores novos do que visitas ao perfil")],
    "whatsapp": [("impressoes", "alcance", "alcance maior que as impressões"),
                 ("impressoes", "cliques", "cliques maiores que as impressões"),
                 ("cliques", "conversas", "mais conversas do que cliques no link")],
}


class Conferencia:
    def __init__(self, dados: dict, relatorio):
        self.dados = dados
        self.relatorio = relatorio
        self.erros: List[str] = []
        self.avisos: List[str] = []
        self._conferir()

    @property
    def passou(self) -> bool:
        return not self.erros

    def imprimir(self) -> None:
        for e in self.erros:
            sys.stderr.write(f"ERRO: {e}\n")
        for a in self.avisos:
            sys.stderr.write(f"AVISO: {a}\n")

    # ---- verificações ----

    def _conferir(self) -> None:
        self._periodos()
        self._investimento_contra_api()
        for secao in self.relatorio.secoes:
            self._secao(secao)
        self._textos_e_foto()

    def _periodos(self) -> None:
        r = self.relatorio
        if r.periodo.inicio > r.periodo.fim:
            self.erros.append("o período começa depois de terminar")
        if r.periodo_anterior and r.periodo_anterior.fim >= r.periodo.inicio:
            self.avisos.append("o período anterior se sobrepõe ao período do relatório")
        elif r.periodo_anterior:
            esperado = r.periodo.anterior_equivalente()
            if (esperado.inicio, esperado.fim) != (r.periodo_anterior.inicio, r.periodo_anterior.fim):
                self.avisos.append(f"período anterior fora da regra (mesmos dias do mês anterior): esperado "
                                   f"{esperado.texto_curto()}, veio {r.periodo_anterior.texto_curto()}")

    def _investimento_contra_api(self) -> None:
        """Totais que o agente leu direto da API (campo opcional conferencia.investido_api)."""
        esperado = (self.dados.get("conferencia") or {}).get("investido_api") or {}
        valores = {"total": self.relatorio.total, **{s.chave: s.investido for s in self.relatorio.secoes}}
        for chave, da_api in esperado.items():
            if chave not in valores:
                self.avisos.append(f"investido_api traz '{chave}', que não existe neste relatório")
            elif abs(valores[chave] - da_api) > TOLERANCIA_REAIS + 1e-9:
                self.erros.append(f"investido ({chave}) não bate com a API: relatório {F.moeda(valores[chave])}, "
                                  f"API {F.moeda(da_api)}")

    def _secao(self, secao) -> None:
        nome = secao.titulo
        if secao.investido <= 0:
            self.avisos.append(f"{nome}: investimento zerado; seção sem gasto não deveria entrar")
        for campo, valor in secao.dados.items():
            if isinstance(valor, (int, float)) and not isinstance(valor, bool) and valor < 0:
                self.erros.append(f"{nome}: '{campo}' está negativo ({valor})")
        for campo in secao.campos_obrigatorios:
            if secao.dados.get(campo) is None:
                self.erros.append(f"{nome}: '{campo}' é obrigatório e veio vazio")
        faltando = [c for c in secao.campos_desejaveis if secao.dados.get(c) is None]
        if faltando:
            self.avisos.append(f"{nome}: sem dado em {', '.join(faltando)} (aparece como – no relatório)")
        for maior, menor, texto in FUNIS.get(secao.chave, []):
            a, b = secao.dados.get(maior), secao.dados.get(menor)
            if a is not None and b is not None and b > a:
                self.avisos.append(f"{nome}: {texto} ({F.inteiro(b)} contra {F.inteiro(a)})")
        if self.relatorio.periodo_anterior and not secao.anterior:
            self.avisos.append(f"{nome}: sem dados do período anterior (sem variação nesta seção)")

    def _textos_e_foto(self) -> None:
        if not self.relatorio.observacoes:
            self.avisos.append("sem texto em 'Leitura do mês'")
        for secao in self.relatorio.secoes:
            if not secao.comentario:
                self.avisos.append(f"{secao.titulo}: sem comentário")
        foto: Optional[str] = (self.dados.get("cliente") or {}).get("foto")
        if foto and not self.relatorio.cliente.foto:
            self.avisos.append(f"foto '{foto}' não encontrada; o relatório vai usar as iniciais")
