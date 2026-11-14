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
- Uma página por seção: faixa com título e etapa, 6 cards de métricas, gráfico (fluxo com taxas entre etapas; no vídeo, funil ao lado dos cards, ver Seção 2) e caixa opcional "O que esse resultado mostra".
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

**Origem (regra do gestor, 14/11/2026):** campanha de meio com `[MEIO]` e `[VV]` no nome no Gerenciador (ex.: `🔥[MEIO] CP2 - [VV][DIV]Meio de Funil`). Pode haver mais de uma com o mesmo padrão; só entra a que gastou no período e os valores se somam.

**Layout (aprovado em 14/11/2026, igual ao dashboard de exemplo do gestor):**
- Linha de cima, 4 cards: Valor Gasto | Visualização 15 seg | Custo 15 seg | Tempo médio assistido (este último some se não houver dado)
- Abaixo, à esquerda, 3 linhas de 2 cards: Vídeo 50% | Valor Gasto / Vídeo 50%, depois 75%, depois 95%
- Abaixo, à direita, **gráfico de funil de verdade** (trapézios empilhados que afunilam): Vídeo 15 seg → Vídeo 50% → Vídeo 95%, com o número real dentro de cada faixa. A largura do desenho é fixa e sempre diminui (é forma, não escala), porque 50% pode ser maior que 15 seg (ver nota abaixo). Cores em tons de laranja (cor do Meio), claro para escuro. O exemplo do gestor usava azul; se ele preferir azul, é só trocar `cores` em `montar_video`.
- Código: `montar_video` em `relatorio/gerar.py` e bloco `s.vv` em `relatorio/modelo/relatorio.html.j2`. Mesmos nomes de dados do JSON de antes (`views_15s`, `video_50`, `video_75`, `video_95`).

Nota: 15 seg aqui é ThruPlay (15 s ou vídeo completo). Em vídeo de ~30 s, 50% cai perto dos 15 s, então `video_p50` pode ficar um pouco acima ou abaixo do ThruPlay (aconteceu no exemplo do gestor: 7.886 contra 7.802, e na campanha do Dr. Rodrigo em 01/11 a 13/11: 3.533 contra 3.495). [Certa, visto nos dados]

**Todas as métricas de vídeo que a API de anúncios entrega (conferido em 14/11/2026 com `ads_get_field_context`), nível campanha:**
| Métrica | Campo | No relatório hoje |
|---|---|---|
| Reproduções de vídeo | `video_play_actions` | não |
| Reproduções de 2 s contínuos | `video_continuous_2_sec_watched_actions` (custo: `cost_per_2_sec_continuous_video_view`) | não |
| Reproduções de 3 s | `3_second_video_plays` (custo: `cost_per_video_view`) | não |
| ThruPlay (15 s ou completo) | `video_thruplay_watched_actions` (custo: `cost_per_thruplay`) | **sim**, "Visualização 15 seg" |
| 25% do vídeo | `video_p25_watched_actions` | não |
| 50% do vídeo | `video_p50_watched_actions` | **sim** |
| 75% do vídeo | `video_p75_watched_actions` | **sim** |
| 95% do vídeo | `video_p95_watched_actions` | **sim** |
| 100% do vídeo | `video_p100_watched_actions` | não |
| Tempo médio assistido (segundos) | `video_avg_time_watched_actions` | **sim** (decisão do gestor, 14/11/2026), 4º card da linha de cima, campo `tempo_medio_s` no JSON. Só aparece se o dado existir. Leitura de teste do Dr. Rodrigo: 6 s |

**Decisão do gestor (14/11/2026): das métricas extras, só o tempo médio entra. Não incluir reproduções totais, 2 s, 3 s, 25% nem 100%.**

Apoio (não são de vídeo): `amount_spent`, `impressions`, `reach`, `frequency`, `cpm`. Os custos "Valor Gasto / Vídeo X" são calculados (gasto ÷ views), nunca digitados. `video_p25/p50/p75/p95` não são filtráveis na API, então não dá para filtrar campanha por elas; filtrar pelo nome (`MEIO`).

Leitura de teste (Dr. Rodrigo, 01/11 a 13/11/2026, só leitura): `🔥[MEIO] CP2 - [VV][DIV]Meio de Funil` gastou R$ 388,57, 24.454 impressões, 10.664 alcance, 3.495 ThruPlay, p50 3.533, p75 1.162, p95 917. A campanha `... - 07/12` do mesmo padrão gastou R$ 0 e fica de fora.

### Seção 3: Campanhas de Captação de Leads (fundo de funil)
Ícone do WhatsApp. Todos os valores vêm do Gerenciador de Anúncios (campanha de WhatsApp do período, só as que gastaram), nunca dos números de exemplo. Teste real em 14/11/2026 (Dr. Rodrigo, 01/11 a 13/11, campanha `[FUNDO][MSG] Agendamento - 10/07`): R$ 822,84, 16.862 impressões, 9.491 alcance, 111 cliques no link, 46 conversas, R$ 17,89 por conversa. Seis cards em 2 linhas de 3:
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

## Skill e agente (criados em 14/11/2026)

- **Skill `relatorio-cliente`** (`.claude/skills/relatorio-cliente/SKILL.md`): dispara quando o gestor pede relatório de alguém. Identifica clientes e período (padrão: mês anterior completo), checa o ambiente e despacha um agente por cliente, todos na mesma mensagem (paralelo).
- **Agente `montador-relatorio`** (`.claude/agents/montador-relatorio.md`): um por cliente. Busca dados no conector Meta Ads, classifica campanhas, monta `saida/dados/<slug>-<AAAA-MM>.json`, roda `gerar.py` e devolve resumo com pendências. Ferramentas de escrita do Meta Ads bloqueadas no próprio agente.
- **Entrega no chat (regra do gestor, 14/11/2026):** ao terminar cada relatório, sempre mostrar no chat o link do HTML (`file:///...`) para o gestor abrir no navegador, além do caminho do PDF.
- **Cadastro de clientes:** `clientes/<slug>.json` (fora do git, são dados de cliente). Formato em `relatorio/exemplos/cliente-config-exemplo.json`: nome, apelidos, ID da conta, Instagram, foto, tema do vídeo e classificação de cada campanha.

## Mapa de métricas (conector Meta Ads, conferido em 14/11/2026)

| Dado do relatório | Campo da API |
|---|---|
| Investido | `amount_spent` |
| Alcance / Impressões | `reach` / `impressions` |
| Visitas ao perfil | `results` dos conjuntos com meta `VISIT_INSTAGRAM_PROFILE` [Provável] |
| Novos seguidores | `instagram_profile_follow_v2` [Certa, campo existe] |
| Cliques na bio | não apareceu na API de anúncios [Certa]. Vem da API do Instagram (`website_clicks`, ver "Mapa de campos por seção"). Obrigatório buscar, nunca "–" |
| Visualização 15 s | `video_thruplay_watched_actions` (ThruPlay = 15 s ou vídeo completo) |
| Vídeo 50/75/95% | `video_p50/p75/p95_watched_actions` |
| Cliques (WhatsApp) | `link_click` (cliques no link). **Confirmado pelo gestor em 14/11/2026.** Não usar `clicks` (cliques todos): no teste do Dr. Rodrigo (01/11 a 13/11) deu 313 contra 111 do `link_click` |
| Conversas iniciadas | `actions:onsite_conversion.messaging_conversation_started_7d` |

Classificação automática pela meta do conjunto: `VISIT_INSTAGRAM_PROFILE` = Topo, `THRUPLAY` = Meio, `CONVERSATIONS` = Fundo. Campanha de formulário ou site ainda não tem página no gerador: o agente avisa como pendência.

## Mapa de campos por seção (de onde cada card puxa o dado)

Só a referência da origem, sem valores. Regra do gestor (14/11/2026): cada seção diz de qual lugar do Gerenciador de Anúncios do Meta Ads o dado vem.

### Regra para toda campanha lida (gestor, 14/11/2026)

Antes de pegar valores de qualquer campanha, **verificar se ela estava ativa ou se gastou verba dentro do período do relatório**. Campanha sem gasto no período não entra nos cards (e não conta como seção). Se a campanha estiver pausada hoje mas gastou no período, ela entra. Se estiver ativa mas sem gasto, fica de fora. Citar no resumo quais campanhas entraram e quais foram descartadas por não ter gasto.

### Crescimento do Instagram (topo de funil)

**Regra geral:** apesar de ser a seção do Instagram, **todos os dados vêm do Gerenciador de Anúncios do Meta Ads**, não do Instagram em si. O gestor tem uma campanha paga que leva tráfego para o perfil. Os números dela já estão no gerenciador.

**Onde buscar:** Gerenciador de Anúncios, aba **Campanhas**, nível campanha, no período do relatório. A campanha de origem é a de topo com nome no padrão `[TOPO] [TRF] Novos Seguidores - <data>` (exemplo: `[TOPO] [TRF] Novos Seguidores - 04/10`). A linha "Resultados de 1 campanha" no rodapé da tabela mostra o total das campanhas selecionadas.

| Card | Origem no gerenciador (coluna da campanha) |
|---|---|
| Valor Investido | coluna de gasto da campanha (`amount_spent`, "Valor usado") |
| Alcance | coluna **Alcance** da campanha (`reach`). Não é o alcance do Instagram, é o da campanha de novos seguidores |
| Visitas ao perfil | **Confirmado em 14/11/2026 (Dr. Rodrigo, 01/11 a 13/11):** campanha `⭐[TOPO] [TRF] Novos Seguidores - 04/10` (OUTCOME_TRAFFIC), `results` com indicador `profile_visit_view` = 689, gasto R$ 388,95. O relatório salvo de 13/11 mostrava 678 (diferença provavelmente por dados que chegaram depois) [Provável]. Campanha de meio (`[MEIO] CP2`) e de fundo (`[FUNDO][MSG]`) não têm esse indicador. 1º: tentar da campanha. Só existe como `results` se a meta de otimização do conjunto for `VISIT_INSTAGRAM_PROFILE`; se a campanha otimiza seguidores, o `results` não é visita. 2º (fallback): insights do Instagram (visitas ao perfil no período) |
| Clique na Bio | **Decisão do gestor (14/11/2026): pegar das métricas do próprio Instagram**, via API do Instagram com `ACCESS_TOKEN` do `.env` (ver "Teste do token"). Métrica: `website_clicks` (cliques no link da bio), `metric_type=total_value`, `period=day`, com `since`/`until` do relatório. Testado em 14/11/2026 no Dr. Rodrigo, outubro: `website_clicks` = 73, `profile_links_taps` = 0 (conta só botões de contato, não o link). Atenção: é o total do perfil (orgânico + anúncio), não só da campanha. |
| Novos Seguidores | gerenciador, mesma campanha (`instagram_profile_follow_v2`, seguidores/follows do Instagram) |
| Investido/Seguidores | calculado: Valor Investido ÷ Novos Seguidores (nunca digitado) |

Teste de campos em 14/11/2026 (`ads_get_field_context`): **não existe métrica dedicada de "visitas ao perfil" nem de "cliques na bio" na API de anúncios**. Existem `instagram_profile_follow_v2` (seguidores), `link_click`, `outbound_clicks` e `results`. [Certa] Por isso a regra do gestor é: tentar da campanha, e se não houver métrica, buscar direto do Instagram. Marcar no relatório/resumo de onde cada um veio.

Pesquisa na web (14/11/2026, fontes de terceiros, não da Meta): no Gerenciador, em **Personalizar colunas > Interações > Cliques**, existe a coluna **"Visitas ao perfil do Instagram"** (em inglês "Instagram Profile Visits"), e não precisa otimizar para visita ao perfil para ela aparecer [Provável]. **Não achei coluna de "cliques na bio" em anúncios**: esse dado só existe nos insights orgânicos do Instagram (atividade do perfil, toques no link da bio) [Provável]. O nome do campo na API de anúncios ainda não foi encontrado; os testes com `instagram_profile_visits` e variações falharam no conector.

Instagram do cliente pelo conector (testado em 14/11/2026 com a conta `CA - Dr. Rodrigo Domingues`, ID 4949141168532200): `ads_get_ig_accounts` lista os perfis ligados e o perfil `dr.rodrigodomingues` aparece (ID 17841400645393151). `ads_get_ig_media` devolve só os posts (legenda, curtidas, comentários, data). **Não devolve insights do perfil** (visitas ao perfil, toques no link da bio, seguidores totais). [Certa] Obs.: `ads_get_ig_accounts` lista os perfis de vários clientes juntos; escolher sempre o do cliente pelo `@` salvo na config dele.

**REGRA DO GESTOR (14/11/2026): NÃO usar o Composio neste projeto.** O Instagram que está nele é o pessoal do gestor, não os dos clientes. Para dados do Instagram (visitas ao perfil, cliques na bio), a fonte a usar é a skill `meta-ads-cli` (comando `meta`, conta do gestor ligada ao Meta). Estado em 14/11/2026: o `meta` não está instalado nesta máquina e não há `ACCESS_TOKEN` no `.env`, então ainda não foi possível testar se ele entrega esses insights.

Pesquisa de skills (14/11/2026, `find-skills`): as skills de Instagram do ecossistema (hyperfx, clawlink, insta-audit/Treg, Composio) usam "Instagram Login", que conecta **um perfil por login**, e dependem de serviço de terceiros. Não servem para "um login do gestor, vários clientes". O caminho multi-cliente é a **API do Instagram com login do Facebook**: um token de usuário do gestor com as permissões `instagram_basic`, `instagram_manage_insights`, `pages_read_engagement` (e `business_management`) lê `/{ig-user-id}/insights` (`profile_views`, `profile_links_taps`, `website_clicks`) de qualquer perfil ligado a uma página que o gestor administra [Provável]. A skill já instalada `meta-ads-cli` faz isso pelo `scripts/meta_graph.py` (requisição GET crua ao Graph, token no `.env`). Os IDs dos perfis já vêm de `ads_get_ig_accounts`. Falta: criar app de desenvolvedor da Meta (grátis), gerar o token e testar.

**Teste do token do gestor (14/11/2026, Graph API Explorer v25.0): FUNCIONOU.** App `App Cursosobredireito` em modo Desenvolvimento, token de usuário com `pages_show_list`, `pages_read_engagement`, `business_management`, `ads_read`, `read_insights` (+ permissões do Instagram do caso de uso). Consulta `/{ig-user-id}/insights?metric=profile_views&metric_type=total_value&period=day&since=2026-10-01&until=2026-10-31` devolveu `total_value.value` (um perfil de cliente, 1.729 visitas em outubro). Primeiro deu erro `(#10) Application does not have permission` até a permissão certa entrar no app. Falta: testar `website_clicks` / `profile_links_taps` (Clique na Bio), conferir o número com o app do Instagram do cliente, estender o token (~60 dias) e guardar no `.env` como `ACCESS_TOKEN`. Token comum dura ~1 h; o estendido ~60 dias, depois renovar.

Registro histórico, não usar: busca no Composio (só consulta, nada executado): tem a ação `INSTAGRAM_GET_USER_INSIGHTS` com as métricas `profile_views`, `profile_links_taps` e `website_clicks`, por período e por `ig_user_id`. A conexão ativa lá é de **uma conta só** (`aiinoaps`, criada em 11/11/2026), não dos clientes. Só funciona para o perfil de um cliente se esse login tiver acesso ao perfil dele. [Provável, não testado] Usar o Composio é mexer em integração: pedir confirmação ao gestor antes de executar.

**Cliques na bio, funcionando (14/11/2026):** `website_clicks` pela Graph API v25.0 com o `ACCESS_TOKEN` do `.env`, perfil do Dr. Rodrigo (ID 17841400645393151): 28 em 01/11 a 13/11 e 36 em 19/10 a 31/10 (`profile_links_taps` = 0). O agente `montador-relatorio` não fazia essa consulta (instrução dele dizia `null`); corrigido na mesma data.

**REGRA DO GESTOR (14/11/2026): o Midas TEM que buscar os cliques na bio, em todo relatório. Nunca deixar "–" nem avisar como pendência.** Se a consulta falhar (token vencido, erro 190), é falha do processo: parar e avisar o gestor para renovar o token (ver "Token do Instagram: renovação"), em vez de entregar o relatório sem o dado.

Se houver mais de uma campanha de novos seguidores no período, somar todas as de topo do cliente.

(As demais seções ainda serão detalhadas, uma por vez, do mesmo jeito.)

## Token do Instagram: renovação

O `ACCESS_TOKEN` do `.env` foi estendido em 14/11/2026 e vence por volta de **13/01/2027** (~60 dias). Renovar a partir de **06/01/2027**. A data exata está em developers.facebook.com/tools/debug/accesstoken (campo "Expira em"). Se a API devolver erro code 190, o token expirou. Midas: no início de uma sessão de relatório, se a data for 06/01/2027 ou depois, avisar o gestor antes de gerar.

Passo a passo para renovar:
1. Abrir developers.facebook.com/tools/explorer (Ferramentas, depois Explorador da Graph API).
2. Em **Meta App**, escolher `App Cursosobredireito`. Em **Usuário ou Página**, escolher "Obter token de acesso do usuário".
3. Conferir as permissões: `pages_show_list`, `pages_read_engagement`, `business_management`, `ads_read`, `read_insights` e as do Instagram. Clicar em **Generate Access Token** e, na janela do Facebook, marcar todas as páginas e Instagrams dos clientes (inclusive clientes novos).
4. Abrir developers.facebook.com/tools/debug/accesstoken, colar o token e clicar em **Estender token de acesso**. Copiar o token novo (o estendido, de 60 dias).
5. Abrir o `.env` na raiz do projeto e trocar o valor da linha `ACCESS_TOKEN=` pelo novo (sem aspas, sem espaços). Salvar. Nunca colar o token no chat nem no git.
6. Pedir ao Midas para fazer uma leitura de teste (visitas ao perfil de um cliente) e confirmar que voltou número, não erro.
7. Atualizar nesta seção a nova data de vencimento (hoje + 60 dias) e a lembrança.

## Ferramentas instaladas no projeto

- `.claude/skills/find-skills` (vercel-labs/skills): busca de skills.
- `.claude/skills/meta-ads-cli` (tristanmanchester/agent-skills): guia para ler dados pela ferramenta oficial da Meta (`pip install meta-ads`, comando `meta`). Só leitura neste projeto. A ferramenta precisa de `ACCESS_TOKEN` no `.env`; o conector do claude.ai (opção escolhida) não precisa de token. Testado em 13/11/2026: instala e responde, testes da skill passam (16/16). Ainda sem teste com conta real.

## Como gerar o PDF

Ambiente: `jinja2` está no `python3`; Playwright + Chromium foram instalados em 14/11/2026 na pasta do projeto (`node_modules/`, `package.json`, fora do git). Usar `python3` (o `python` do Git Bash não tem o jinja2). Testado: PDF gerado sem aviso de página estourada.

```bash
python3 relatorio/gerar.py relatorio/exemplos/cliente-exemplo.json
# saída em saida/ (fora do git): .html e .pdf
```

- O JSON de entrada segue `relatorio/exemplos/cliente-exemplo.json`. Seção ausente = página não aparece. Sem `periodo_anterior` = sem variações e sem tabela de comparação.
- Custos (por seguidor, por conversa, por visualização) são calculados pelo script, nunca digitados.
- `relatorio/pdf.js` avisa "ATENÇÃO: página X estourou" se algum conteúdo passar do tamanho da página. Se aparecer, encurtar textos.
