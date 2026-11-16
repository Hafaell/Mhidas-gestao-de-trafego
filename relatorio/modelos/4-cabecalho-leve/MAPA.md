# Mapa do modelo `4-cabecalho-leve`

Leitura obrigatória do agente `editor-layout` antes de mexer no visual. Diz **como o modelo é montado**, **onde fica cada peça** e **o que pode ser mudado sem tocar nos dados**. Se o modelo mudar, este mapa muda junto (é parte do modelo: copiar a pasta para um modelo novo leva o mapa).

Prints de cada página: `referencia/` (exemplo básico) e `referencia/secoes-novas/` (completo e orgânico).

## 1. Como o HTML nasce

```
JSON de dados  ──►  midas/relatorio.py + midas/secoes/*.py  ──►  objeto `relatorio`  ──►  html/*.j2 + css  ──►  HTML
(agente coletor-dados)   (transforma números em cards prontos)        (já formatado)        (este modelo)
```

- O modelo **nunca faz conta nem formata número**. Ele recebe texto pronto (`k.valor` = "R$ 1.234,56") do Python.
- Quem decide **quais cards** existem, em que ordem, com que rótulo, é o Python das seções (`montar_kpis`). Quem decide **como eles aparecem** (tamanho, cor, grade, espaçamento) é o modelo.
- Quem decide **quais páginas** existem é `Relatorio._montar_paginas` (Python). O modelo só desenha cada tipo de página.

## 2. Arquivos do modelo

| Arquivo | O que tem | Muda quando |
|---|---|---|
| `html/relatorio.html.j2` | documento inteiro; um bloco `{% if pag.tipo == ... %}` por tipo de página | muda a disposição dentro de uma página (funil, fluxo, tabela, evolução) |
| `html/componentes.html.j2` | macros que se repetem: `cabecalho`, `investimento`, `rodape`, `banda`, `icone`, `kpi_card`, `grade_kpis`, `selo_variacao` | muda algo que aparece em toda página ou em toda seção |
| `css/relatorio.css` | todo o estilo, em 12 partes numeradas (índice no topo do arquivo) | muda cor, fonte, tamanho, espaçamento |
| `referencia/*.png` | print aprovado de cada página | regerar depois de o gestor aprovar uma mudança |

## 3. Tipos de página (blocos do `relatorio.html.j2`)

| Tipo (`pag.tipo`) | Quando existe | Peças, de cima para baixo |
|---|---|---|
| `blocos` | Instagram, Instagram orgânico, landing page, WhatsApp. Até 3 seções por página; com 3, classe `compacta` (cards menores) | `cabecalho` · `investimento` · para cada seção: `banda` + `grade_kpis` · `rodape` |
| `video` | uma página por vídeo (`video_topo` azul, `video` laranja) | `cabecalho` · `investimento` · `banda` · linha de 3 ou 4 cards (`s.painel.topo`) · à esquerda 3 pares quantidade/custo (`s.painel.pares`), à direita o funil SVG (`s.painel.funil`) · `rodape` |
| `resumo` | se há fluxo ou período anterior. Fluxos e comparação juntos se ≤ 2 fluxos e ≤ 9 linhas; senão em páginas separadas | `cabecalho` · `investimento` · "Do anúncio ao resultado" (um card por `s.fluxo`, passos com seta e taxa) · "Comparação com o período anterior" (tabela, único lugar com selo de variação) · `rodape` |
| `evolucao` | com 2 meses ou mais de histórico | `cabecalho` · `investimento` · grade de `evol-card` (mini gráfico de linha SVG por indicador) · nota de mês parcial · `rodape` |

## 4. Componentes (`componentes.html.j2`)

| Macro | Desenha | Usa do `relatorio` / da seção | Classes CSS (parte do CSS) |
|---|---|---|---|
| `cabecalho()` | faixa azul-marinho: foto ou iniciais, logo Meta, nome, "Relatório de leads · Meta Ads", descrição · @, caixas Período / Comparado a | `cliente.nome/descricao/instagram/foto/iniciais`, `periodo_txt`, `anterior_txt` | `.cab .avatar .logo-meta .cab-centro .l1 .l2 .l3 .filtros .filtro` (2) |
| `investimento()` | "Investimento do período": total, barra por etapa, legenda Topo/Meio/Fundo com valor e % | `total_fmt`, `etapas[]` (`chave nome rotulo investido_fmt participacao participacao_fmt`) | `.invest .invest-valor .barra .legenda .leg .leg-nome .leg-valor .leg-share` (4) |
| `rodape(n, total)` | agência, data de geração, "Página n de total" | `agencia`, `gerado_em` | `.rod .ag` (10) |
| `banda(s)` | cabeçalho leve da seção: ícone redondo + título à esquerda; etapa e % à direita; linha fina com trecho na cor da etapa | `s.titulo_exibido s.icone s.cor_icone s.etapa s.nome_etapa s.rotulo_etapa s.participacao_fmt s.sem_investimento` | `.banda .banda-t .banda-s .ic` (5) |
| `icone(nome)` | SVG branco: `instagram`, `video`, `globo`, `whatsapp` | nome vem de `Secao.icone` | `.ic svg` (5) |
| `kpi_card(k)` | card de métrica: rótulo, valor grande, nota pequena opcional; `destaque` muda o fundo | `k.rotulo k.valor k.nota k.destaque` | `.card .kpi .kpi-rot .kpi-valor .kpi-nota .destaque` (3, 6) |
| `grade_kpis(kpis)` | grade de cards: 4 cards = 2 colunas; 7 ou mais = 4 colunas; resto = 3 | lista de `Kpi` | `.kpis .kpis-4 .kpis-7` (6) |
| `selo_variacao(v)` | selo verde/vermelho/cinza com a variação | `v.texto v.estado` (`bom ruim neutro`) | `.var` (6) |

## 5. Cores e medidas (variáveis no `:root`, parte 1 do CSS)

| Variável | Valor | Uso |
|---|---|---|
| `--topo` / `--topo-tint` | `#2a78d6` / `#eaf2fc` | etapa Topo (Instagram, vídeo de topo) |
| `--meio` / `--meio-tint` | `#eb6834` / `#fdefe8` | etapa Meio (vídeo de meio) |
| `--fundo` / `--fundo-tint` | `#1baf7a` / `#e5f6ef` | etapa Fundo (landing page, WhatsApp) |
| `--bom` `--ruim` `--neutro` (+ `-tint`) | verde, vermelho, cinza | selos da tabela de comparação |
| `--bg` `--card` `--line` `--ink` `--ink-2` `--muted` `--navy` `--navy-2` | fundo, cards, bordas, textos, cabeçalho | geral |

- Cada página/bloco recebe `--cor` e `--tint` da etapa no `style` (`var(--{{ s.etapa }})`). Mudar a cor de uma etapa = mudar só a variável.
- Página A4 fixa: `.pagina { width: 210mm; height: 297mm; overflow: hidden }`. Conteúdo que passa disso **some** (o `gerar.py` avisa "página X estourou").
- Página cheia até o rodapé: classe `.estica` (o bloco cresce e os cards, tabela e gráficos esticam). Folga de ~6 mm antes do rodapé.

## 6. O que fica no Python, mas é decisão de layout

Mexer aqui muda **todos** os relatórios, inclusive os antigos se forem regerados. Fazer só com pedido do gestor.

| Quero mudar | Onde |
|---|---|
| rótulo, ordem ou quantidade de cards de uma seção | `montar_kpis` em `midas/secoes/<seção>.py` (`Kpi.criar(rótulo, valor, formato, anterior, destaque=..., nota=...)`) |
| título da seção, ícone, cor do ícone | atributos `titulo`, `titulo_curto`, `icone`, `cor_icone` da classe da seção |
| passos do fluxo "Do anúncio ao resultado" | `montar_fluxo` da seção |
| linhas da tabela de comparação | `linhas_comparacao` da seção |
| desenho do funil do vídeo (etapas, larguras, cores) | `FUNIL`, `CORES_FUNIL`, `PARES` em `midas/secoes/video.py` |
| quantos blocos por página, quando fluxo e comparação se separam | constantes no topo de `midas/relatorio.py` (`MAX_BLOCOS_POR_PAGINA` etc.) e `_montar_paginas` |
| nomes e rótulos das etapas ("Topo · Pessoas novas") | `NOMES_ETAPA`, `ROTULOS_ETAPA` em `midas/relatorio.py` |
| gráfico de evolução (medidas, meses) | `midas/evolucao.py` |

Card novo que precisa de **número novo** (ex.: "Custo por clique") não é só layout: se o número sai de campos que já vêm no JSON, o editor faz a conta no Python da seção; se precisa de campo que o JSON não tem, registra o pedido em `relatorio/CONTRATO-DADOS.md` (seção "Pedidos do layout") para o `coletor-dados` passar a buscar.

## 7. Cards de cada seção (o que o gestor aprovou)

| Seção | Cards |
|---|---|
| Instagram (Topo) | Valor investido, Alcance no Instagram (só anúncio de seguidores), Visitas ao perfil, Cliques na bio (est. anúncio), Novos seguidores ("vindos de todas as campanhas"), Custo por seguidor. Extra por cliente: Custo por visita ao perfil |
| Instagram orgânico (Topo) | Alcance do perfil, Visitas ao perfil, Cliques na bio, Novos seguidores; sem valor investido (fora do total) |
| Vídeo de topo (azul) e de meio (laranja) | Linha de cima: Valor gasto, Visualização 15 seg, Custo 15 seg, Tempo médio assistido (some sem dado). Abaixo à esquerda: 50%, 75%, 95% com o custo de cada. À direita: funil em trapézios (15 seg, 50%, 95%), largura fixa decrescente (forma, não escala) |
| Landing page (Fundo) | Valor investido, Impressões, Cliques no link, Visualizações da página, Leads (ou "Conversões"), Custo por lead |
| WhatsApp (Fundo), pode vir em blocos por cidade/tema | Valor investido, Impressões, Alcance, Cliques, Conversas iniciadas, Custo por conversa. Título "Leads no WhatsApp · <bloco>" |

- Bloco "Investimento do período" soma por **etapa**, não por seção (no Kondo, Fundo = landing page + WhatsApp, como no relatório feito à mão). Rótulo da etapa pode ser trocado por cliente (`rotulos_etapa`: Villalva "Meio · Remarketing").
- `tema` de uma seção vai no título ("Vídeo de meio de funil · Mela").
- Evolução mensal: investimento total + um indicador por seção (seção repetida soma os blocos); mês parcial com `*`.

## 8. Regras visuais que o gestor já fechou (não desfazer sem ele pedir)

Regra nova de visual entra aqui, com a data.

- **Cabeçalho de seção leve** (15/11/2026): ícone redondo + título à esquerda, etapa e % do investimento à direita (cinza pequeno), linha fina com trecho na cor da etapa. **Nunca** a faixa azul-marinho de ponta a ponta (o gestor achou agressiva). O cabeçalho da página (azul-marinho, com foto) continua.
- **Cor dos ícones de seção** (15/11/2026): Instagram com gradiente laranja do Instagram; landing page azul com globo; WhatsApp verde (cor do Fundo). Só o círculo muda; a linha fina continua na cor da etapa. Atributo `cor_icone` da classe.
- **Cabeçalho da página** (todas): azul-marinho, foto (a do perfil do Instagram; sem foto, iniciais), logo Meta, nome / "Relatório de leads · Meta Ads", caixas "Período" e "Comparado a".
- **Bloco "Investimento do período"** em todas as páginas: total, barra por etapa e legenda com valor e %. Não trocar por cards pequenos.
- **Cores por etapa:** Topo `#2a78d6` azul, Meio `#eb6834` laranja, Fundo `#1baf7a` verde.
- **Selo de variação só na tabela de comparação** (15/11/2026). Cards, investimento e evolução sem seta nem %. Verde melhorou, vermelho piorou, cinza investimento; em custo, cair é bom.
- **Página cheia, com respiro** (15/11/2026): conteúdo até o rodapé (classe `estica`), sem meia página vazia nem aperto, folga de ~6 mm antes do rodapé. Ao mudar o layout, conferir todas as páginas em PNG.
- **Sem notas de interpretação** (15/11/2026): nada de "O que esse resultado mostra" (`comentario`) nem "Leitura do mês" (`observacoes`). Só dados.
- **Visual livre, dados fixos:** pode melhorar o visual, mas todos os dados do dashboard antigo continuam (seguidores, cliques na bio, retenção do vídeo, conversas).
- Visual novo se testa numa cópia na pasta temporária (`--modelo <caminho absoluto>`) e só vira modelo depois de o gestor aprovar.

## 9. Como testar uma mudança

```bash
# cópia de trabalho fora do projeto (regra: visual novo é testado numa cópia)
TMP=$(python3 relatorio/gerar.py --pasta-saida)/layout-teste
cp -r relatorio/modelos/4-cabecalho-leve "$TMP"
# ... editar $TMP/html e $TMP/css ...
for ex in cliente-exemplo cliente-exemplo-completo cliente-exemplo-organico; do
  python3 relatorio/gerar.py relatorio/exemplos/$ex.json --modelo "$TMP" --saida "$TMP/saida/$ex"
done
mkdir -p "$TMP/png/cliente-exemplo"
node relatorio/pdf.js "$TMP/saida/cliente-exemplo/relatorio-dra-ana-exemplo-2026-10.html" "$TMP/x.pdf" --png "$TMP/png/cliente-exemplo"
# ver no navegador:
python3 relatorio/servir.py relatorio-dra-ana-exemplo-2026-10 --pasta "$TMP/saida/cliente-exemplo" --porta 8000
```

Os três exemplos juntos passam por todos os tipos de página e todas as seções. Eles têm o mesmo nome de cliente e mês, por isso cada um sai numa subpasta própria.
