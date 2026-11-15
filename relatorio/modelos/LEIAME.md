# Modelos do relatório Meta Ads

Cada versão do visual tem sua pasta. As antigas ficam só como imagem (PNG) para consulta; o código delas está no git.

| Pasta | Data | O que é |
|---|---|---|
| `1-antigo/` | antes do projeto | Dashboard que o gestor montava à mão. Referência da posição dos cards. |
| `2-quatro-paginas/` | 13/11/2026 | Primeiro modelo do Midas (4 páginas, uma por seção). Código no commit `e361ef7`. |
| `3-atual-dashboard/` | 14/11/2026 | **Modelo atual**, aprovado. 3 páginas, mais a página 4 de evolução mensal quando há histórico. É o que o `gerar.py` usa. |

Estrutura de um modelo executável (`3-atual-dashboard/`):

```
html/relatorio.html.j2      documento inteiro: head, body e as páginas A4 em ordem
html/componentes.html.j2    peças que se repetem nas páginas (cabeçalho, investimento, kpi_card, rodapé...)
css/relatorio.css           todo o estilo
referencia/              PNG de cada página (gerado de relatorio/exemplos/cliente-exemplo.json)
```

Modelo novo: copiar `3-atual-dashboard/` para `4-<nome>/`, mexer em `html/` e `css/`, gerar com `--modelo 4-<nome>`.
