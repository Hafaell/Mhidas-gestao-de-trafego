#!/usr/bin/env python3
"""Gera o relatório Meta Ads de um cliente (HTML) a partir de um JSON de dados.

Uso:
    python3 relatorio/gerar.py relatorio/exemplos/cliente-exemplo.json
    python3 relatorio/gerar.py dados.json --com-pdf
    python3 relatorio/gerar.py dados.json --modelo 4-cabecalho-leve
    python3 relatorio/gerar.py dados.json --registrar-historico   # relatório real: guarda os números do mês
    python3 relatorio/gerar.py dados.json --so-conferir   # só a conferência, sem gerar HTML (coletor-dados)
    python3 relatorio/gerar.py --periodo-anterior 2026-11-09 2026-11-20   # mostra o período de comparação
    python3 relatorio/gerar.py --pasta-saida     # mostra onde ficam os relatórios gerados

O JSON segue o formato de relatorio/exemplos/cliente-exemplo.json.
Seções ausentes no JSON simplesmente não aparecem no relatório.
Antes de gravar, confere os dados (midas/conferencia.py): ERRO impede o relatório (exit 2), AVISO vira pendência.
Entrega: só o HTML (+ relatorio.css ao lado), na pasta temporária do sistema
(<temp>/midas/). O PDF sai pelo botão do servir.py.
"""
import argparse
import json
import sys
from pathlib import Path

from midas.conferencia import Conferencia
from midas.config import MODELO_ATUAL, PASTA_HISTORICO, PASTA_MODELOS, PDF_JS, SAIDA
from midas.exportador_pdf import ExportadorPdf
from midas.formatacao import Formatador
from midas.historico import Historico
from midas.relatorio import Periodo, Relatorio
from midas.renderizador import RenderizadorHtml


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--periodo-anterior", nargs=2, metavar=("INICIO", "FIM"),
                    help="só mostra o período de comparação (mesmos dias do mês anterior) e sai")
    ap.add_argument("dados", nargs="?", help="arquivo JSON com os dados do cliente")
    ap.add_argument("--saida", default=str(SAIDA), help=f"pasta de saída (padrão: {SAIDA})")
    ap.add_argument("--pasta-saida", action="store_true", help="só mostra a pasta de saída e sai")
    ap.add_argument("--com-pdf", action="store_true",
                    help="grava também o PDF na pasta de saída (padrão: só o HTML)")
    ap.add_argument("--modelo", default=MODELO_ATUAL,
                    help=f"pasta de relatorio/modelos/ com o visual (padrão: {MODELO_ATUAL})")
    ap.add_argument("--registrar-historico", action="store_true",
                    help="guarda os números do mês em clientes/historico/ (use só em relatório real, não no exemplo)")
    ap.add_argument("--pasta-historico", default=str(PASTA_HISTORICO), help=argparse.SUPPRESS)
    ap.add_argument("--so-conferir", action="store_true",
                    help="só confere os dados (ERRO = exit 2) e sai, sem gerar HTML")
    ap.add_argument("--forcar", action="store_true",
                    help="gera mesmo com ERRO na conferência (só com autorização do gestor)")
    args = ap.parse_args()
    if args.periodo_anterior:
        anterior = Periodo(*args.periodo_anterior).anterior_equivalente()
        print(f"{anterior.inicio} {anterior.fim}")
        return
    if args.pasta_saida:
        print(SAIDA)
        return
    if not args.dados:
        ap.error("informe o arquivo JSON com os dados do cliente")

    arquivo = Path(args.dados).resolve()
    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    historico = Historico(Formatador.slug(dados["cliente"]["nome"]), Path(args.pasta_historico))
    relatorio = Relatorio(dados, pasta_fotos=arquivo.parent, historico=historico)

    conferencia = Conferencia(dados, relatorio)
    conferencia.imprimir()
    if not conferencia.passou and not args.forcar:
        sys.exit(2)
    if args.so_conferir:
        print("Conferência OK" + (" (com avisos)" if conferencia.avisos else ""))
        return

    html = RenderizadorHtml(PASTA_MODELOS / args.modelo).gravar(relatorio, Path(args.saida))
    print(f"HTML: {html}")
    if args.registrar_historico:
        relatorio.registrar_em(historico)
        print(f"Histórico: {historico.salvar()}")

    exportador = ExportadorPdf(PDF_JS)
    if args.com_pdf:
        pdf = html.with_suffix(".pdf")
        exportador.exportar(html, pdf)
        print(f"PDF:  {pdf}")
    else:
        exportador.conferir_paginas(html)   # avisa se alguma página estourou; não grava PDF


if __name__ == "__main__":
    sys.exit(main())
