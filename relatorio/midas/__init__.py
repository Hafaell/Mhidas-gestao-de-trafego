"""Midas: gerador dos relatórios Meta Ads da Agência Lupa.

Mapa do pacote (cada arquivo tem uma responsabilidade):
    config.py           caminhos e constantes do projeto
    formatacao.py       Formatador: números, moeda e datas no padrão brasileiro
    metricas.py         Calculo, Variacao e Kpi: contas e selos de variação
    secoes/             Secao (base) e uma classe por seção do relatório
    relatorio.py        Cliente, Periodo e Relatorio: juntam os dados do JSON
    renderizador.py     RenderizadorHtml: Relatorio + modelo de HTML = arquivo .html
    exportador_pdf.py   ExportadorPdf: HTML em PDF (via Chromium)
    servidor.py         ServidorLocal: abre o relatório em localhost
"""
