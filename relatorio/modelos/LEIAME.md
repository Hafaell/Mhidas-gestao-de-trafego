# Modelos do relatório Meta Ads

Cada versão do visual do relatório fica em sua pasta. Nenhuma é apagada.

| Pasta | Quando | O que é |
|---|---|---|
| `1-antigo/` | antes do projeto | Dashboard que o gestor montava à mão (fundo escuro, cards pretos e brancos). PDF e imagens das páginas. Serviu de referência para o layout. |
| `2-quatro-paginas/` | 13/11/2026 | Primeiro modelo do Midas: 4 páginas, uma por seção. PDF, imagens, dados e o template da época (`relatorio.html.j2`, tudo em um arquivo). Só consulta: o código que gerava está no commit `e361ef7` do git. |
| `3-atual-dashboard/` | 14/11/2026 | **Modelo atual**, aprovado pelo gestor. 3 páginas, cards nas posições do dashboard antigo. É o que o `gerar.py` usa. |

## Estrutura de um modelo que o gerador executa (como o `3-atual-dashboard/`)

```
3-atual-dashboard/
  html/
    relatorio.html.j2      esqueleto: escolhe e monta as páginas
    componentes/           peças reaproveitáveis (cabeçalho, kpi_card, funil_video, rodapé...)
    paginas/               uma página A4 completa cada
  css/
    relatorio.css          todo o estilo, ligado ao HTML por <link>
  referencia/              PDF, imagens e dados que mostram como o modelo deve ficar
```

Para criar um modelo novo: copiar a pasta do atual para `4-<nome>/`, mexer em `html/` e `css/` e gerar com `python3 relatorio/gerar.py <dados.json> --modelo 4-<nome>`.
