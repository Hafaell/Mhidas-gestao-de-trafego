# STATUS DOS RELATÓRIOS: quem dá para gerar hoje

**Conferido em 15/11/2026** (atualizado no mesmo dia: o modelo ganhou as seções que faltavam). Leia o resumo e a tabela. Detalhes de cada cliente: `memoria/por-cliente/<cliente>.md`.

## Resumo

| | Clientes | Quantos |
|---|---|---|
| ✅ Dá para gerar, o modelo atual cobre tudo | Sanos Life, Dr. Bernardo Mercante, Dr. Rodrigo Domingues, Clínica Sotre, Renovare, Clínica Lis | 6 |
| ✅ Dá para gerar, **layout novo pronto** (seções criadas em 15/11/2026 a partir do relatório feito à mão) | Carlos Alexandre, Dr. Raphael Kondo, Dr. Gustavo Langen, Dra. Patrícia Cabrejos, Instituto Domingues, Dra. Patrícia Canelas, Dr. Paulo Rosenbaum, Dra. Cleanir Sandi, Dra. Rhaiana Gondim, Dr. Gustavo Mesquita, Dr. Gustavo Samico, Instituto Reluz | 12 |
| ⛔ **Não dá para gerar**: a Meta não liberou a conta no conector | COG, CEIOF, Dr. Rodrigo Villalva, Defesa Plena | 4 |
| ❓ Faltam dados | Doc Circle (conta de anúncio não achada) | 1 |

**Relatório já gerado de verdade:** só o **Dr. Rodrigo Domingues** (tem cadastro e histórico em `clientes/`). Os outros ainda não foram rodados; "dá para gerar" quer dizer que a conta está acessível e a estrutura foi mapeada, não que o relatório saiu [Certa].

## ⛔ Os 4 que NÃO dá para gerar (fazer à mão por enquanto)

Motivo: a Meta mantém desligado o conector de IA (Ads MCP) nessas contas. Mensagem do conector: *"This ad account is not enabled for the Ads MCP. Ads MCP is being gradually rolled out"*. Em Configurações da empresa > Servidor MCP de anúncios, a conta aparece com "Actions allowed: -". A trava é da conta, não do usuário nem do app: na BM do Villalva, duas contas do mesmo login têm resultado diferente (uma liberada, a do relatório bloqueada). **Não há opção do lado do gestor para ligar.**

| Cliente | Conta de anúncio (a do relatório) | Obs. |
|---|---|---|
| COG, Centro Ortopédico Grajaú | 430427302706806 ("COG Life") | existe a conta 2468228613414433, liberada, mas sem gasto em out/2026: não é a do relatório |
| CEIOF | 1231637101726635 | o relatório antigo era só Google Ads |
| Dr. Rodrigo Villalva | 2328762197650912 | existe a 444228829894416, liberada, sem gasto em out/2026. A Meta também sinalizou **restrição por "atividades incomuns"** nesta conta (ver abaixo) |
| Defesa Plena (Denis) | 392732128512252 ("Tribunal do Júri ads") | sem relatório antigo |

### Pedido ao suporte da Meta (15/11/2026)
- Enviado pelo suporte para empresas, no perfil do Filipe Rabello, pedindo a liberação das 4 contas. **Não há número de caso nem confirmação** de que virou chamado [Certa].
- A análise automática respondeu só sobre a conta do Villalva: "Restringimos sua conta de anúncios" e ofereceu o botão "Aja agora" (pedir análise da restrição). **Não foi clicado**, por depender de decisão do gestor.
- Pendente: decidir se pede a análise da restrição do Villalva; ver se a restrição tem relação com o conector (não se sabe).

### Quando reconferir
Antes de pedir o relatório de um desses quatro, rodar `ads_get_ad_accounts` e olhar `is_ads_mcp_enabled` da conta. Se virar `true`, o agente passa a funcionar sem mudar mais nada: atualizar esta tabela e o arquivo do cliente.

## ✅ Os 12 que ganharam layout próprio (15/11/2026)

Antes saíam com partes faltando. Agora o modelo tem vídeo de **topo** separado, **landing page**, WhatsApp **em blocos** (cidade/tema), **Instagram sem campanha** (números do perfil), card extra e rótulos/temas por cliente. A configuração de cada um está na memória dele (bloco "Configuração do relatório"), com a conferência PDF x layout novo. Testado com os números de out/2026 dos PDFs: todas as páginas cabem.

| Cliente | O que o layout dele usa | Relatório real já gerado no layout novo? |
|---|---|---|
| Carlos Alexandre | vídeo de topo + vídeo de meio + WhatsApp (sem Instagram) | não |
| Dr. Raphael Kondo | Instagram + vídeo de topo + vídeo de meio + **landing page** + WhatsApp | **sim**, 01 a 15/11/2026 (R$ 1.871,02, conferência sem erro) |
| Dr. Gustavo Langen | vídeo de topo; WhatsApp **São Paulo** e **Campinas** | não |
| Dra. Patrícia Cabrejos | **Instagram orgânico**; WhatsApp "Tricologia" | não |
| Instituto Domingues | vídeo de topo; tema "Mela"; rótulo "Meio · Pessoas engajadas" | não (campanhas pausadas) |
| Dra. Patrícia Canelas | vídeo de topo; card "Custo por visita ao perfil" | não |
| Dr. Paulo Rosenbaum | vídeo de topo; WhatsApp **Dor**, **Nova Andradina**, **Ivinhema** | não |
| Dra. Cleanir Sandi | vídeo de topo (estrutura padrão completa) | não |
| Dra. Rhaiana Gondim | vídeo de topo | não |
| Dr. Gustavo Mesquita | vídeo de topo (sem PDF para comparar) | não |
| Dr. Gustavo Samico | **Instagram orgânico** + WhatsApp | não |
| Instituto Reluz | vídeo de topo + WhatsApp (sem Instagram) | não |

O que continua de fora para todos: página de **Google Ads** (fase futura). Obs.: no Instituto Domingues e na Renovare as campanhas estavam **pausadas** em 15/11/2026; mês sem gasto não gera seção.

## ✅ Os 6 que o modelo atual cobre

| Cliente | Seções |
|---|---|
| Sanos Life | Instagram (post impulsionado) + vídeo de meio |
| Dr. Bernardo Mercante | Instagram (post impulsionado) + WhatsApp (coluna + joelho somados); vídeo de meio **fora de propósito** |
| Dr. Rodrigo Domingues | Instagram + vídeo de meio + WhatsApp (**já gerado**) |
| Clínica Sotre | só WhatsApp (coluna + joelho somados) |
| Renovare | só WhatsApp (2 campanhas somadas) |
| Clínica Lis | só WhatsApp (3 somadas); topo institucional e meio remarketing **fora de propósito** |

## ❓ Doc Circle
Cliente ativo, mas não está no Notion e a conta de anúncio não aparece no conector. Relatório antigo: só landing page (o modelo atual também não cobre). Falta: conta de anúncio e Instagram.

## Como manter este arquivo
Atualizar sempre que: o conector liberar uma conta, o modelo ganhar uma seção nova, um relatório for gerado pela primeira vez (marcar na tabela dos 12), ou entrar cliente novo. Colocar a data no topo.
