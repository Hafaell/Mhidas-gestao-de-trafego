#!/usr/bin/env python3
"""Abre o relatório no navegador, em localhost, com botão para baixar o PDF.

Uso:
    python3 relatorio/servir.py                      # usa o relatório mais recente de saida/
    python3 relatorio/servir.py nome-do-relatorio    # sem extensão
    python3 relatorio/servir.py --porta 8080 --sem-abrir

Abre em http://localhost:8000 (só acessível neste computador).
"""
import argparse

from midas.config import PDF_JS
from midas.exportador_pdf import ExportadorPdf
from midas.servidor import ServidorLocal


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("nome", nargs="?", help="nome do relatório em saida/, sem extensão (padrão: o mais recente)")
    ap.add_argument("--porta", type=int, default=8000)
    ap.add_argument("--sem-abrir", action="store_true", help="não abre o navegador")
    args = ap.parse_args()

    nome = args.nome or ServidorLocal.relatorio_mais_recente()
    ServidorLocal(nome, ExportadorPdf(PDF_JS), args.porta).iniciar(abrir_navegador=not args.sem_abrir)


if __name__ == "__main__":
    main()
