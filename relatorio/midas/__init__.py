"""Midas: gerador dos relatórios Meta Ads da Agência Lupa.

Mapa do pacote (cada arquivo tem uma responsabilidade):
    config.py           caminhos e constantes do projeto
    formatacao.py       Formatador: números, moeda e datas no padrão brasileiro
    metricas.py         Calculo, Variacao e Kpi: contas e selos de variação
    secoes/             Secao (base) e uma classe por seção do relatório: Instagram (com campanha ou orgânico),
                        vídeo de topo, vídeo de meio, landing page, WhatsApp (pode vir em blocos)
    relatorio.py        Cliente, Periodo e Relatorio: juntam os dados do JSON
    renderizador.py     RenderizadorHtml: Relatorio + modelo de HTML = arquivo .html
    conferencia.py      Conferencia: erros e avisos sobre os dados, antes de gerar
    historico.py        Historico: números de cada mês por cliente (clientes/historico/)
    evolucao.py         Evolucao: cards do gráfico dos últimos meses
    token_instagram.py  TokenInstagram: confere a validade do ACCESS_TOKEN
    instagram_perfil.py PerfilInstagram: números do perfil (visitas, cliques na bio, alcance, seguidores),
                        em janelas de até 30 dias (limite da API)
    exportador_pdf.py   ExportadorPdf: HTML em PDF (via Chromium)
    servidor.py         ServidorLocal: abre o relatório em localhost
"""
