# Modelos do relatório Meta Ads

Cada versão do visual tem sua pasta. As antigas ficam só como imagem (PNG) para consulta; o código delas está no git.

| Pasta | Data | O que é |
|---|---|---|
| `1-antigo/` | antes do projeto | Dashboard que o gestor montava à mão. Referência da posição dos cards. |
| `2-quatro-paginas/` | 13/11/2026 | Primeiro modelo do Midas (4 páginas, uma por seção). Código no commit `e361ef7`. |
| `3-atual-dashboard/` | 14/11/2026 | Dashboard com faixa azul-marinho de ponta a ponta em cada seção. Substituído pelo 4. O código segue na pasta por enquanto. |
| `4-cabecalho-leve/` | 15/11/2026 | **Modelo atual**, aprovado. Igual ao 3, mas cada seção abre com cabeçalho leve (ícone + título, etapa do funil à direita, linha fina com trecho colorido) em vez da faixa escura. Sem caixas de texto de interpretação, página cheia até o rodapé. 3 páginas, mais a página 4 de evolução mensal quando há histórico. É o que o `gerar.py` usa (`MODELO_ATUAL` em `midas/config.py`). |

Estrutura de um modelo executável (`4-cabecalho-leve/`):

```
html/relatorio.html.j2      documento inteiro: head, body e as páginas A4 em ordem
html/componentes.html.j2    peças que se repetem nas páginas (cabeçalho, investimento, kpi_card, rodapé...)
css/relatorio.css           todo o estilo
referencia/              PNG de cada página (gerado de relatorio/exemplos/cliente-exemplo.json)
```

Modelo novo: copiar `4-cabecalho-leve/` para `5-<nome>/`, mexer em `html/` e `css/`, gerar com `--modelo 5-<nome>` e, depois de aprovado, trocar `MODELO_ATUAL` em `midas/config.py`. Para só testar um visual sem criar pasta no projeto, `--modelo` aceita um caminho absoluto de uma cópia na pasta temporária.
