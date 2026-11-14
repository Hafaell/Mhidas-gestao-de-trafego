# Modelo aprovado do relatório Meta Ads (layout dashboard)

Aprovado pelo gestor em 14/11/2026 (substitui o modelo de 13/11/2026, de 4 páginas). Todo relatório novo deve seguir este visual e esta estrutura. A disposição dos cards segue o dashboard antigo (ver `relatorio/modelos/1-antigo/`).

Arquivos:
- `modelo-atual.pdf`: PDF completo de 3 páginas (dados fictícios).
- `pagina-1.png` a `pagina-3.png`: cada página como imagem, para consulta rápida.
- `dados-do-modelo.json`: os dados que geraram o modelo (mesmo formato que o Midas preenche com dados reais).

Páginas: 1 investimento do período + Instagram (topo) + WhatsApp (fundo), 2 vídeo (meio), 3 fluxos, comparação com o período anterior e leitura do mês.
Para regenerar: `python3 relatorio/gerar.py relatorio/modelos/3-atual-dashboard/referencia/dados-do-modelo.json`
