"""Caminhos e constantes do projeto. Tudo que muda de lugar fica só aqui."""
import tempfile
from pathlib import Path

PASTA_RELATORIO = Path(__file__).resolve().parent.parent   # relatorio/
RAIZ = PASTA_RELATORIO.parent                              # raiz do projeto
# Relatórios gerados (HTML, CSS e JSON de dados) são de uso único: ficam na pasta
# temporária do sistema (Windows: %TEMP%\midas, Linux/Mac: /tmp/midas), fora do projeto.
SAIDA = Path(tempfile.gettempdir()) / "midas"
# O que precisa durar de um mês para o outro fica em clientes/ (fora do git).
PASTA_CLIENTES = RAIZ / "clientes"
PASTA_FOTOS = PASTA_CLIENTES / "fotos"                     # foto de perfil de cada cliente
PASTA_HISTORICO = PASTA_CLIENTES / "historico"             # números de cada mês, por cliente (gráfico de evolução)

# Cada versão do visual do relatório mora em uma pasta de relatorio/modelos/.
PASTA_MODELOS = PASTA_RELATORIO / "modelos"
MODELO_ATUAL = "4-cabecalho-leve"

PDF_JS = PASTA_RELATORIO / "pdf.js"
PASTA_VISUALIZADOR = PASTA_RELATORIO / "visualizador"      # página do localhost (botão Baixar PDF)
