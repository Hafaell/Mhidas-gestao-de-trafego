# Contrato de dados do relatório

É o combinado entre os três agentes do relatório:

| Agente | Papel | Relação com este arquivo |
|---|---|---|
| `coletor-dados` | busca os números de um cliente e grava o JSON de dados | **entrega** exatamente os campos daqui, da fonte indicada |
| `editor-layout` | mexe só no visual (pasta do modelo e partes de apresentação do Python) | **consome** os campos daqui; precisa de campo novo → escreve em "Pedidos do layout" |
| `montador-relatorio` | junta o JSON com o modelo (`gerar.py`) e confere as páginas | não muda nada aqui; reclama se o JSON não seguir o contrato |

Os agentes não conversam em tempo real: a conversa entre o coletor e o editor é **este arquivo**. O editor pede, o coletor atende e move o pedido para a tabela da seção.

Formato completo de exemplo: `relatorio/exemplos/cliente-exemplo.json`, `cliente-exemplo-completo.json`, `cliente-exemplo-organico.json` (dados fictícios).

## 1. Raiz do JSON

| Campo | Obrigatório | O que é |
|---|---|---|
| `agencia` | não | padrão "Agência Lupa" |
| `cliente.nome` `cliente.descricao` `cliente.instagram` `cliente.foto` | nome sim | `foto` = nome do arquivo em `clientes/fotos/` ou `null` (usa iniciais) |
| `periodo.inicio` `periodo.fim` | sim | `AAAA-MM-DD` |
| `periodo_anterior.inicio` `.fim` | sim, se houver comparação | mesmos dias do mês anterior (`gerar.py --periodo-anterior`), nunca recalcular |
| `rotulos_etapa` | não | `{"meio": "Remarketing"}`, vem de `layout.rotulos_etapa` do cliente |
| `conferencia.investido_api` | sim | investido como a API devolveu: `total` e por seção (`"whatsapp"` soma os blocos, `"whatsapp:São Paulo"` um bloco). Diferença > R$ 0,01 = ERRO |
| `secoes` | sim | uma chave por seção com gasto no período (ver 2). Seção sem gasto: não entra |

Nunca entram: custos (o gerador calcula), `comentario`, `observacoes`, `cliques_bio` do Instagram pago (o gerador estima).

## 2. Seções

Em toda seção paga: `investido` (soma de `amount_spent` das campanhas da seção, 2 casas) e `anterior` com os mesmos campos do período anterior (omitir `anterior` se a seção não gastou lá). Campo sem dado = `null` + pendência; nunca inventar.

Seção repetida (WhatsApp por cidade/tema): a chave recebe uma **lista**, cada item com `bloco` (`"whatsapp": [{"bloco": "São Paulo", ...}, ...]`).

Campos opcionais em qualquer seção: `tema` (vai no título); em `landing_page`: `nome_resultado` ("Leads" ou "Conversões").

### `instagram` (Topo, campanha de seguidores)

| Campo | Nível | Fonte |
|---|---|---|
| `alcance` | desejável | `reach` da campanha de seguidores com `breakdowns: ["publisher_platform"]`, só a linha `instagram` (várias campanhas: soma + pendência "alcance somado de N campanhas") |
| `visitas_perfil` | obrigatório | `results` dos conjuntos com `VISIT_INSTAGRAM_PROFILE` (só anúncio; nunca o total do Instagram) |
| `visitas_perfil_total` | obrigatório | `visitas_perfil_total` do `instagram_perfil.py` |
| `cliques_bio_total` | obrigatório | `cliques_bio_total` do `instagram_perfil.py` |
| `novos_seguidores` | desejável | `instagram_profile_follow_v2` no nível `ad_account` (soma de todas as campanhas) |

### `instagram_organico` (Topo, sem campanha; sem `investido`)

`alcance`, `visitas_perfil` (= `visitas_perfil_total` do script), `cliques_bio` (= `cliques_bio_total`), `novos_seguidores` (do script). Todos do `instagram_perfil.py`.

### `video_topo` e `video` (Topo `[TOPO][VV]`/CP1 e Meio `[MEIO][VV]`/CP2)

| Campo | Nível | Fonte |
|---|---|---|
| `views_15s` | desejável | `video_thruplay_watched_actions` |
| `video_50` `video_75` `video_95` | desejável | `video_p50/p75/p95_watched_actions` |
| `tempo_medio_s` | opcional (card some sem ele) | `video_avg_time_watched_actions`, segundos |

### `landing_page` (Fundo)

| Campo | Fonte |
|---|---|
| `impressoes` | `impressions` |
| `cliques` | `link_click` |
| `visualizacoes_pagina` | `landing_page_view` |
| `leads` | `results` da campanha (anotar o `indicator` nas pendências) |

### `whatsapp` (Fundo)

| Campo | Fonte |
|---|---|
| `impressoes` | `impressions` |
| `alcance` | `reach` (várias campanhas: soma + pendência "alcance somado de N campanhas") |
| `cliques` | `link_click` (nunca `clicks`) |
| `conversas` | `actions:onsite_conversion.messaging_conversation_started_7d` |

## 3. Decisões do gestor sobre os dados (o porquê de cada fonte)

- **Seção só entra se gastou no período.** Campanha pausada hoje que gastou entra; ativa sem gasto fica fora. Citar as descartadas nas pendências.
- **Custos nunca vão no JSON** (por seguidor, por conversa, por view): o gerador calcula.
- **Cliques na bio = estimativa via anúncio (15/11/2026).** Nenhuma API separa o clique na bio por origem [Provável], e a API de anúncios não tem métrica de cliques na bio nem campo dedicado de visitas ao perfil (testado com `ads_get_field_context`) [Certa]. O gerador calcula `cliques_bio_total × visitas_perfil ÷ visitas_perfil_total` (`SecaoInstagram.estimar_cliques_bio`), supondo que quem vem do anúncio clica na bio na mesma taxa do orgânico; fração limitada a 100% com aviso. Sem um dos três números: ERRO. API do Instagram falhou (erro 190 = token vencido): parar e avisar o gestor.
- **Novos seguidores = vindos de TODAS as campanhas (15/11/2026).** Kondo 01 a 15/11/2026 = 72 na conta (seguidores 7 + vídeo topo 6 + vídeo meio 1 + landing page 41 + WhatsApp 17). Não é só a campanha de seguidores nem o perfil inteiro (2.858, com orgânico). Custo por seguidor = investido na campanha de Instagram ÷ esse total. O gestor aceitou que não bate com o relatório feito à mão, que usava o perfil inteiro (out/2026: 250 no Midas contra 12,8 mil no PDF).
- **Instagram pago: alcance do anúncio no Instagram, não do perfil (15/11/2026, substitui a regra anterior do mesmo dia).** O gestor quer só as pessoas alcançadas pelo anúncio de seguidores, entregue no Instagram (alcance único, não impressões). Kondo out/2026: 28.546 no Instagram (Facebook 7.750, fora; impressões no Instagram 57.245, não usadas). A soma do alcance diário do perfil (1.139.568) foi abandonada: juntava orgânico e contava a mesma pessoa uma vez por dia. O `instagram_perfil.py` continua dando `alcance` só para o `instagram_organico`.
- **Visitas ao perfil (`visitas_perfil`)** = `results` com indicador `profile_visit_view`, que só existe se o conjunto otimiza `VISIT_INSTAGRAM_PROFILE`. Nunca trocar pelo `profile_views` do Instagram (a estimativa viraria 100%).
- **Instagram aceita no máximo 30 dias por consulta** (15/11/2026): o `instagram_perfil.py` divide e soma; alcance somado de 2 janelas é aproximado.
- **15 seg = ThruPlay** (15 s ou vídeo completo). Em vídeo curto o 50% pode passar do ThruPlay: é normal (a conferência não reclama). Das métricas extras de vídeo só entra o tempo médio; nada de reproduções totais, 2 s, 3 s, 25% ou 100%.
- **WhatsApp:** cliques = `link_click`, nunca `clicks`.
- **Leads da landing page:** `results` da campanha. Conferido em 15/11/2026: Kondo out/2026 deu 871 cliques, 338 visualizações e 137 leads, igual ao PDF.

## 4. Pedidos do layout

O `editor-layout` escreve aqui quando um card novo precisa de um número que o JSON ainda não traz. O `coletor-dados` lê esta lista toda vez: se conseguir buscar, passa a entregar o campo, move a linha para a tabela da seção (seção 2) e apaga daqui. Se não houver fonte na API, responde na coluna "Resposta do coletor" e o pedido volta para o gestor decidir.

| Data | Seção | Campo pedido | Para quê (card) | Resposta do coletor |
|---|---|---|---|---|
| | | | | |
