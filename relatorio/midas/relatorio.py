"""O relatório de um cliente: junta o JSON de dados em objetos prontos para o modelo de HTML."""
from __future__ import annotations

import base64
import calendar
import math
import mimetypes
import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List, Optional

from .config import PASTA_FOTOS
from .evolucao import Evolucao
from .formatacao import Formatador
from .historico import Historico
from .metricas import Calculo, Variacao
from .secoes import SECOES_NA_ORDEM, LinhaComparacao, Secao


# Etapas do funil, na ordem. O rótulo aparece ao lado do nome ("Topo · Pessoas novas") e pode ser trocado
# por cliente com "rotulos_etapa" no JSON (ex.: Villalva usa "Meio · Remarketing").
ETAPAS = ("topo", "meio", "fundo")
NOMES_ETAPA = {"topo": "Topo", "meio": "Meio", "fundo": "Fundo"}
ROTULOS_ETAPA = {"topo": "Pessoas novas", "meio": "Vídeo", "fundo": "Foco em consulta"}

# Páginas de blocos (Instagram, landing page, WhatsApp): até 3 por página. Com 3, os cards ficam compactos.
MAX_BLOCOS_POR_PAGINA = 3
# Página de resumo: fluxos e comparação juntos só se couberem; senão, cada um na sua página.
MAX_FLUXOS_COM_COMPARACAO, MAX_LINHAS_COM_FLUXOS, MAX_FLUXOS_POR_PAGINA = 2, 9, 3


@dataclass
class Etapa:
    """Uma etapa do funil no bloco "Investimento do período" (soma das seções daquela etapa)."""
    chave: str
    nome: str
    rotulo: str
    investido: float
    participacao: float

    @property
    def investido_fmt(self) -> str:
        return Formatador.moeda(self.investido)

    @property
    def participacao_fmt(self) -> str:
        return Formatador.percentual(self.participacao, 0)


@dataclass
class Pagina:
    """Uma página A4 do relatório. `tipo`: blocos, video, resumo, evolucao."""
    tipo: str
    secoes: list = field(default_factory=list)
    fluxos: list = field(default_factory=list)      # seções cujo fluxo aparece (página de resumo)
    comparacao: bool = False                        # a tabela de comparação aparece (página de resumo)
    compacta: bool = False                          # 3 blocos na página: cards menores


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

    def anterior_equivalente(self) -> "Periodo":
        """Período anterior para comparação (regra do gestor, 14/11/2026): os mesmos dias do mês anterior
        e a mesma quantidade de dias. 09 a 20/11 compara com 09 a 20/10. Se o intervalo atravessar o fim do
        mês (20 a 31/10 contra 20/09 a 31/09), mantém os dias e termina em 01/10.
        Exceção: mês inteiro (dia 1 ao último dia) compara com o mês anterior inteiro."""
        ini, fim = date.fromisoformat(self.inicio), date.fromisoformat(self.fim)
        ano, mes = (ini.year, ini.month - 1) if ini.month > 1 else (ini.year - 1, 12)
        dias_do_mes_anterior = calendar.monthrange(ano, mes)[1]
        mes_inteiro = (ini.day == 1 and ini.month == fim.month and ini.year == fim.year
                       and fim.day == calendar.monthrange(fim.year, fim.month)[1])
        if mes_inteiro:
            novo_ini, novo_fim = date(ano, mes, 1), date(ano, mes, dias_do_mes_anterior)
        else:
            novo_ini = date(ano, mes, min(ini.day, dias_do_mes_anterior))
            novo_fim = novo_ini + (fim - ini)
        return Periodo(novo_ini.isoformat(), novo_fim.isoformat())


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

    def __init__(self, dados: dict, pasta_fotos: Path, historico: Optional[Historico] = None):
        self.agencia: str = dados.get("agencia", "Agência Lupa")
        self.cliente = Cliente(dados["cliente"], pasta_fotos)
        self.periodo = Periodo(**dados["periodo"])
        anterior = dados.get("periodo_anterior")
        self.periodo_anterior: Optional[Periodo] = Periodo(**anterior) if anterior else None
        self.gerado_em: str = date.today().strftime("%d/%m/%Y")

        self.rotulos_etapa: Dict[str, str] = {**ROTULOS_ETAPA, **(dados.get("rotulos_etapa") or {})}
        self.secoes: List[Secao] = self._montar_secoes(dados.get("secoes", {}))
        for s in self.secoes:
            if not s.sem_investimento:
                s.rotulo_etapa = self.rotulos_etapa[s.etapa]
        self.pagas: List[Secao] = [s for s in self.secoes if not s.sem_investimento]   # entram no total
        self.total: float = sum(s.investido for s in self.pagas)
        self.total_anterior: Optional[float] = self._somar_anterior()
        for s in self.pagas:
            s.definir_participacao(self.total)
        self.etapas: List[Etapa] = self._montar_etapas()
        self.comparacao: List[LinhaComparacao] = self._montar_comparacao() if self.periodo_anterior else []
        self.evolucao = Evolucao(self, historico)
        self.paginas: List[Pagina] = self._montar_paginas()

    # ---- montagem ----

    @staticmethod
    def _montar_secoes(dados_secoes: dict) -> List[Secao]:
        """Só entram as seções que existem no JSON, sempre na ordem topo, meio, fundo.
        Uma chave pode trazer uma lista (seção repetida, ex.: WhatsApp por cidade): um bloco por item."""
        secoes = []
        for classe in SECOES_NA_ORDEM:
            valor = dados_secoes.get(classe.chave)
            if not valor:
                continue
            for item in (valor if isinstance(valor, list) else [valor]):
                secoes.append(classe(item))
        return secoes

    def _somar_anterior(self) -> Optional[float]:
        partes = [s.investido_anterior for s in self.pagas]
        return sum(partes) if partes and all(p is not None for p in partes) else None

    def _montar_etapas(self) -> List[Etapa]:
        etapas = []
        for chave in ETAPAS:
            valor = sum(s.investido for s in self.pagas if s.etapa == chave)
            if any(s.etapa == chave for s in self.pagas):
                etapas.append(Etapa(chave, NOMES_ETAPA[chave], self.rotulos_etapa[chave], valor,
                                    Calculo.dividir(valor, self.total) or 0))
        return etapas

    @staticmethod
    def _dividir(itens: list, maximo: int) -> List[list]:
        """Divide em grupos de até `maximo`, do tamanho mais parecido possível (4 itens com máximo 3 = 2 + 2)."""
        if not itens:
            return []
        tamanho = math.ceil(len(itens) / math.ceil(len(itens) / maximo))
        return [itens[i:i + tamanho] for i in range(0, len(itens), tamanho)]

    def _montar_paginas(self) -> List[Pagina]:
        """Plano das páginas, na ordem: blocos (Instagram, landing page, WhatsApp), um vídeo por página,
        resumo (fluxos + comparação) e evolução mensal."""
        paginas: List[Pagina] = []
        blocos = [s for s in self.secoes if s.tipo_pagina == "bloco"]
        for grupo in self._dividir(blocos, MAX_BLOCOS_POR_PAGINA):
            paginas.append(Pagina("blocos", grupo, compacta=len(grupo) >= 3))
        paginas += [Pagina("video", [s]) for s in self.secoes if s.tipo_pagina == "video"]

        fluxos = [s for s in blocos if s.fluxo]
        if fluxos or self.comparacao:
            juntos = (len(fluxos) <= MAX_FLUXOS_COM_COMPARACAO and len(self.comparacao) <= MAX_LINHAS_COM_FLUXOS)
            if juntos:
                paginas.append(Pagina("resumo", fluxos=fluxos, comparacao=bool(self.comparacao)))
            else:
                for grupo in self._dividir(fluxos, MAX_FLUXOS_POR_PAGINA):
                    paginas.append(Pagina("resumo", fluxos=grupo))
                if self.comparacao:
                    paginas.append(Pagina("resumo", comparacao=True))
        if self.evolucao.cards:
            paginas.append(Pagina("evolucao"))
        return paginas

    def _montar_comparacao(self) -> List[LinhaComparacao]:
        total = LinhaComparacao(
            "Investimento total", None, Formatador.moeda(self.total), Formatador.moeda(self.total_anterior),
            Variacao.calcular(self.total, self.total_anterior, neutra=True))
        return [total] + [linha for s in self.secoes for linha in s.linhas_comparacao()]

    def registrar_em(self, historico: Historico) -> None:
        """Grava no histórico o mês deste relatório (sobrescreve) e o anterior (só se ainda não existir)."""
        indicadores = self.evolucao.indicadores()
        historico.registrar(self.periodo.mes, self.periodo.inicio, self.periodo.fim,
                            {i.campo: i.atual for i in indicadores})
        if self.periodo_anterior:
            historico.registrar(self.periodo_anterior.mes, self.periodo_anterior.inicio, self.periodo_anterior.fim,
                                {i.campo: i.anterior for i in indicadores}, sobrescrever=False)

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
