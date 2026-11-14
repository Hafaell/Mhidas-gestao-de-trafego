#!/usr/bin/env python3
"""Gera o relatório Meta Ads de um cliente (HTML) a partir de um JSON de dados.

Uso:
    python3 relatorio/gerar.py relatorio/exemplos/cliente-exemplo.json
    python3 relatorio/gerar.py dados.json --saida saida/ --com-pdf
    python3 relatorio/gerar.py dados.json --modelo 3-atual-dashboard

O JSON segue o formato de relatorio/exemplos/cliente-exemplo.json.
Seções ausentes no JSON simplesmente não aparecem no relatório.
Entrega: só o HTML (+ relatorio.css ao lado). O PDF sai pelo botão do servir.py.
"""
import argparse
import json
import sys
from pathlib import Path

from midas.config import MODELO_ATUAL, PASTA_MODELOS, PDF_JS, SAIDA
from midas.exportador_pdf import ExportadorPdf
from midas.relatorio import Relatorio
from midas.renderizador import RenderizadorHtml


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dados", help="arquivo JSON com os dados do cliente")
    ap.add_argument("--saida", default=str(SAIDA), help="pasta de saída (padrão: saida/)")
    ap.add_argument("--com-pdf", action="store_true",
                    help="grava também o PDF em saida/ (padrão: só o HTML)")
    ap.add_argument("--modelo", default=MODELO_ATUAL,
                    help=f"pasta de relatorio/modelos/ com o visual (padrão: {MODELO_ATUAL})")
    args = ap.parse_args()

    arquivo = Path(args.dados).resolve()
    relatorio = Relatorio(json.loads(arquivo.read_text(encoding="utf-8")), pasta_fotos=arquivo.parent)

    html = RenderizadorHtml(PASTA_MODELOS / args.modelo).gravar(relatorio, Path(args.saida))
    print(f"HTML: {html}")

    exportador = ExportadorPdf(PDF_JS)
    if args.com_pdf:
        pdf = html.with_suffix(".pdf")
        exportador.exportar(html, pdf)
        print(f"PDF:  {pdf}")
    else:
        exportador.conferir_paginas(html)   # avisa se alguma página estourou; não grava PDF


if __name__ == "__main__":
    sys.exit(main())
