"""Caminhos e constantes do projeto. Tudo que muda de lugar fica só aqui."""
from pathlib import Path

PASTA_RELATORIO = Path(__file__).resolve().parent.parent   # relatorio/
RAIZ = PASTA_RELATORIO.parent                              # raiz do projeto
SAIDA = RAIZ / "saida"                                     # relatórios gerados (fora do git)

# Cada versão do visual do relatório mora em uma pasta de relatorio/modelos/.
PASTA_MODELOS = PASTA_RELATORIO / "modelos"
MODELO_ATUAL = "3-atual-dashboard"

PDF_JS = PASTA_RELATORIO / "pdf.js"
PASTA_VISUALIZADOR = PASTA_RELATORIO / "visualizador"      # página do localhost (botão Baixar PDF)
