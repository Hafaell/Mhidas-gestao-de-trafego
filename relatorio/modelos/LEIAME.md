# Modelos do relatório Meta Ads

Só o **modelo atual** tem código (HTML e CSS) e imagens de referência, direto em `relatorio/modelos/`. Todo modelo antigo vai para `legado/` e fica **só como imagem (print das páginas)**, sem HTML nem CSS. O código antigo, se precisar, está no histórico do git.

## Modelo atual

| Pasta | Data | O que é |
|---|---|---|
| `4-cabecalho-leve/` | 15/11/2026 | **Aprovado.** Cada seção abre com cabeçalho leve (ícone + título, etapa do funil à direita, linha fina com trecho colorido). Sem caixas de texto de interpretação, página cheia até o rodapé. 3 páginas, mais a página 4 de evolução mensal quando há histórico. É o que o `gerar.py` usa (`MODELO_ATUAL` em `midas/config.py`). |

Estrutura:

```
html/relatorio.html.j2      documento inteiro: head, body e as páginas A4 em ordem
html/componentes.html.j2    peças que se repetem nas páginas (cabeçalho, investimento, kpi_card, rodapé...)
css/relatorio.css           todo o estilo
referencia/                 PNG de cada página (gerado de relatorio/exemplos/cliente-exemplo.json)
referencia/secoes-novas/    PNG das seções que vieram dos relatórios feitos à mão (15/11/2026): completo-* (vídeo de
                            topo, landing page, WhatsApp em 2 blocos, card extra, rótulo "Remarketing") e organico-*
                            (Instagram sem campanha). Gerados de cliente-exemplo-completo.json e cliente-exemplo-organico.json
```

As páginas não estão fixas no HTML: o `relatorio.html.j2` percorre `relatorio.paginas`, montado em `Relatorio._montar_paginas` (blocos de cards até 3 por página, uma página por vídeo, resumo, evolução).

## Legado (só prints)

| Pasta | Data | Como era |
|---|---|---|
| `legado/1-antigo/` | antes do projeto | Dashboard que o gestor montava à mão. Referência da posição dos cards. |
| `legado/2-quatro-paginas/` | 13/11/2026 | Primeiro modelo do Midas (4 páginas, uma por seção). Código no commit `e361ef7`. |
| `legado/3-atual-dashboard/` | 14/11/2026 | Dashboard com faixa azul-marinho de ponta a ponta em cada seção e caixas "O que esse resultado mostra". Versão aprovada em 14/11: código no commit `540dcfe`. |

## Modelo novo

1. Copiar `4-cabecalho-leve/` para `5-<nome>/`, mexer em `html/` e `css/`, gerar com `--modelo 5-<nome>`. Para só testar um visual sem criar pasta no projeto, `--modelo` aceita o caminho absoluto de uma cópia na pasta temporária.
2. Depois de o gestor aprovar: trocar `MODELO_ATUAL` em `midas/config.py`, gerar as imagens em `5-<nome>/referencia/`.
3. Mover o modelo antigo para `legado/<pasta>/`, deixando **só as imagens** (tirar `html/` e `css/`).
