# Memória: Relatório de Clientes Meta Ads (Midas)

Este arquivo guarda como o relatório dos clientes deve funcionar. Ler antes de gerar ou alterar qualquer relatório.

## Contexto do negócio

- Agência: **Agência Lupa** (nome que aparece no rodapé dos relatórios).
- Mais de 30 clientes com campanhas no Meta Ads. Alguns também têm Google Ads.
- Hoje cada relatório leva cerca de 2 horas para montar à mão. O objetivo do projeto é automatizar isso.
- Exemplo de cliente usado como referência: médico ortopedista especialista em coluna (Brasília), com campanhas de seguidores, vídeo e WhatsApp.

## Regras fixas

1. **Tudo gratuito.** Nada de Looker Studio com conector pago, Supermetrics, Windsor, Porter etc.
2. **Entrega em PDF.** O gestor baixa o PDF e coloca na pasta do cliente no Google Drive. O PDF tem que sair completo, com todas as páginas, sem cortar nada.
3. **Acesso às contas:** as Business Managers são dos clientes, não estão ligadas à BM do gestor. O gestor tem acesso pelo **usuário pessoal dele** do Facebook. Opção escolhida pelo gestor: **conector oficial da Meta no claude.ai** (`https://mcp.facebook.com/ads`, login pessoal, escolhe as contas). Não usar usuário do sistema de BM própria.
4. **Estrutura flexível.** O modelo abaixo é o padrão, mas cada cliente pode ter seções a mais ou a menos. Exemplo: cliente sem campanha de vídeo não tem a página de vídeo; cliente sem WhatsApp pode ter formulário ou site. A seção só aparece se houver campanha daquele tipo no período.
5. Não confundir com a skill "gestor-de-trafego" do claude.ai: ela não faz parte deste projeto.
6. **Só Meta Ads por enquanto.** Google Ads fica para depois.
7. **Foto do cliente:** puxar a foto de perfil do Instagram do cliente. Sem foto, o relatório usa as iniciais.
8. **Visual livre, dados fixos.** O gestor liberou mudar o visual para ficar melhor de ler, mas todos os dados do modelo antigo têm que continuar aparecendo (ex.: seguidores/follows, cliques na bio, retenção do vídeo, conversas).

## Identidade visual do modelo ANTIGO (só referência histórica)

- Fundo escuro (preto e azul-marinho muito escuro).
- Cabeçalho preto com: foto do cliente à esquerda (moldura arredondada), logo da plataforma (Meta ou Google Ads), título em duas linhas em caixa alta e negrito:
  - Linha 1: nome do cliente (ex.: `DR NOME SOBRENOME`)
  - Linha 2: `RELATÓRIO DE LEADS - FACEBOOK` (Meta) ou `RELATÓRIO DE Vendas - Google ADS` (Google)
- No dashboard original existem filtros "Selecionar período" e "Selecione a Campanha". No PDF eles viram texto fixo com o **período do relatório** (ex.: `01/10/2026 a 31/10/2026`).
- Cards de resumo do topo: fundo preto, texto branco.
- Faixas de seção: barra preta de largura total, ícone redondo + título em branco negrito, centralizado.
- Cards de métricas das seções: cartões brancos com cantos arredondados, rótulo pequeno cinza em cima e número grande preto embaixo.
- Rodapé: faixa preta com `AGÊNCIA LUPA` centralizado.
- Formato brasileiro: `R$ 1.737,03`, milhar com ponto (`151.043`), decimal com vírgula.

## Modelo NOVO (APROVADO em 13/11/2026)

Referência visual salva em `relatorio/modelo-aprovado/` (PDF, imagens das páginas e dados). Consultar antes de gerar qualquer relatório.

Gerado por `relatorio/gerar.py` (ver seção "Como gerar" no fim). Visual:
- PDF A4 em pé, fundo cinza-claro, cards brancos, cabeçalho azul-marinho com foto redonda, nome, período e "Relatório de leads · Meta Ads".
- Cores fixas por etapa (validadas para daltonismo): Topo `#2a78d6` azul, Meio `#eb6834` laranja, Fundo `#1baf7a` verde.
- Variação contra o período anterior em selo: verde = melhorou, vermelho = piorou, cinza = investimento (neutro). Para custos, cair é bom.
- Página 1: investimento total + barra dividida por etapa, resultados principais (seguidores, views 15s, conversas), tabela "período anterior x este período", "Leitura do mês" (texto do gestor).
- Uma página por seção: faixa com título e etapa, 6 cards de métricas, gráfico (fluxo com taxas entre etapas ou barras de retenção do vídeo) e caixa opcional "O que esse resultado mostra".
- O card "Meio" foi adicionado no resumo (o modelo antigo só tinha Topo e Fundo).

## Estrutura do relatório Meta Ads (dados que sempre aparecem)

Cada página repete o cabeçalho e o bloco de resumo, e depois traz uma seção.

### Bloco de resumo (topo de todas as páginas)
| Card | Origem |
|---|---|
| Valor Total Investido | soma do gasto de todas as campanhas no período |
| Topo (Pessoas novas) | gasto das campanhas de topo (crescimento de Instagram / seguidores) |
| Fundo (Foco em consulta) | gasto das campanhas de fundo (mensagens / WhatsApp / leads) |

Observação: no exemplo, Total = Topo + Fundo + Meio (vídeo): 831,37 + 1.737,07 + 834,31 = 3.402,75. O meio de funil entra no total mas não tem card próprio no resumo. [Certa, conferido na conta]

### Seção 1: Crescimento do Instagram (topo de funil)
Ícone do Instagram. Seis cards em 2 linhas de 3:
- Valor Investido
- Alcance
- Visitas ao perfil
- Clique na Bio
- Novos Seguidores
- Investido/Seguidores (custo por seguidor = investido ÷ novos seguidores)

Atenção: no exemplo o card mostrava R$ 1,83, mas 831,37 ÷ 507 = R$ 1,64. Calcular sempre pela fórmula e checar.
Visitas ao perfil, cliques na bio e seguidores podem precisar da API do Instagram (conta profissional) e não só da API de anúncios. [Provável, confirmar na implementação]

### Seção 2: Meio de Funil (Video View)
Ícone de câmera. Título no formato `Meio de Funil Video View <tema>` (ex.: "Coluna").
- Valor Gasto
- Visualização 15 seg | Custo 15 seg
- Vídeo 50% | Valor Gasto / Vídeo 50%
- Vídeo 75% | Valor Gasto / Vídeo 75%
- Vídeo 95% | Valor Gasto / Vídeo 95%
- Gráfico de funil à direita (azul claro para azul escuro): Vídeo 15 seg → Vídeo 50% → Vídeo 95%

### Seção 3: Campanhas de Captação de Leads (fundo de funil)
Ícone do WhatsApp. Seis cards em 2 linhas de 3:
- Valor Investido
- Impressões
- Alcance
- Cliques
- Conversas iniciadas
- Valor Investido / Conversas Iniciadas (custo por conversa)

### Ordem das páginas no PDF
1. Resumo + Crescimento do Instagram + Captação de Leads (WhatsApp)
2. Resumo + Meio de Funil (vídeo)
3. Google Ads, quando o cliente tiver (ver abaixo)

## Estrutura do relatório Google Ads (quando houver)

- Cabeçalho igual, com logo do Google Ads e título `RELATÓRIO DE Vendas - Google ADS`. Filtros: período e grupo de anúncios.
- Faixa "Taxa de Investimento e Faturamento" com 5 números: Valor Investido, Impressões, Cliques, Conversões, Custo/conv.
- Funil de compras colorido (vermelho, verde, verde-azulado, laranja): Impressões → Cliques → Conversões → Custo/conv.
- Tabela de termos de pesquisa: Termo, Impressões, Cliques, Custo.
- Tabela "Visão Geral de Campanha": Campanha, Impressões, CPM, CPV méd., Cliques, CPC médio, Conversões, Custo/conv., Custo.
- Fundo cinza-chumbo nesta página.
- Prioridade do projeto é Meta Ads. Google Ads fica para uma fase seguinte.

## Como identificar o tipo de cada campanha

- Usar primeiro o objetivo e o destino da campanha na API (ex.: mensagens/WhatsApp = fundo; visitas ao perfil do Instagram = topo; ThruPlay/visualização de vídeo = meio).
- Se ficar ambíguo, usar o nome da campanha (a agência usa prefixos como `[Lupa]`, `[Leads]`, `[Search]`).
- Guardar a classificação de cada cliente na configuração dele para não errar no mês seguinte.

## Fluxo desejado

1. Gestor pede: "gera o relatório de <mês> do <cliente>" ou "de todos os clientes".
2. Midas puxa os dados de cada conta de anúncio pelo acesso pessoal do gestor.
3. Classifica as campanhas em topo, meio e fundo.
4. Monta só as seções que existem para aquele cliente.
5. Gera o PDF com o visual acima e entrega para download.
6. Gestor sobe o PDF no Drive do cliente.

## Ferramentas instaladas no projeto

- `.claude/skills/find-skills` (vercel-labs/skills): busca de skills.
- `.claude/skills/meta-ads-cli` (tristanmanchester/agent-skills): guia para ler dados pela ferramenta oficial da Meta (`pip install meta-ads`, comando `meta`). Só leitura neste projeto. A ferramenta precisa de `ACCESS_TOKEN` no `.env`; o conector do claude.ai (opção escolhida) não precisa de token. Testado em 13/11/2026: instala e responde, testes da skill passam (16/16). Ainda sem teste com conta real.

## Como gerar o PDF

```bash
python3 relatorio/gerar.py relatorio/exemplos/cliente-exemplo.json
# saída em saida/ (fora do git): .html e .pdf
```

- O JSON de entrada segue `relatorio/exemplos/cliente-exemplo.json`. Seção ausente = página não aparece. Sem `periodo_anterior` = sem variações e sem tabela de comparação.
- Custos (por seguidor, por conversa, por visualização) são calculados pelo script, nunca digitados.
- `relatorio/pdf.js` avisa "ATENÇÃO: página X estourou" se algum conteúdo passar do tamanho da página. Se aparecer, encurtar textos.
