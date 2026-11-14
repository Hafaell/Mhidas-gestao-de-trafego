"""HTML em PDF A4, usando o Chromium do Playwright (pdf.js)."""
import subprocess
import tempfile
from pathlib import Path
from typing import Optional


class ExportadorPdf:
    def __init__(self, script_pdf: Path):
        self.script_pdf = script_pdf

    def exportar(self, html: Path, destino: Path, pasta_png: Optional[Path] = None) -> None:
        """Grava o PDF em `destino`. Com `pasta_png`, grava também cada página como imagem."""
        comando = ["node", str(self.script_pdf), str(html), str(destino)]
        if pasta_png:
            comando += ["--png", str(pasta_png)]
        subprocess.run(comando, check=True)

    def conferir_paginas(self, html: Path) -> None:
        """Gera o PDF num arquivo temporário (apagado em seguida) só para o pdf.js avisar
        "ATENÇÃO: página X estourou" quando algum conteúdo passa do tamanho da página."""
        with tempfile.TemporaryDirectory() as tmp:
            self.exportar(html, Path(tmp) / "conferencia.pdf")
