# Contexto da conversa: projeto Midas

Resumo para retomar o trabalho em uma sessão nova. Atualizado em 14/11/2026.

## Objetivo
O gestor tem mais de 30 clientes no Meta Ads (Agência Lupa) e gasta cerca de 2 horas por cliente montando o dashboard do relatório. O Midas (assistente de gestão de tráfego) deve automatizar isso e entregar um **PDF** por cliente, que o gestor baixa e coloca no Drive do cliente.

## Decisões do gestor
- Tudo gratuito (sem Looker Studio com conector pago, Supermetrics etc.).
- Entrega em PDF, completo, para baixar.
- As Business Managers são dos clientes. O gestor acessa pelo **usuário pessoal** do Facebook.
- Forma de acesso escolhida: **conector oficial da Meta no claude.ai** (`https://mcp.facebook.com/ads`, login pessoal, somente leitura).
- Foto do cliente: puxar a foto de perfil do Instagram dele (sem foto, usa iniciais).
- Por enquanto só Meta Ads. Google Ads fica para depois.
- Estrutura flexível: seções aparecem ou somem conforme as campanhas de cada cliente.
- Visual livre, mas os dados do modelo antigo continuam todos (seguidores, cliques na bio, retenção do vídeo, conversas etc.).
- Ignorar a skill "gestor-de-trafego" do claude.ai.
- Modelo do PDF **aprovado** em 13/11/2026.

## O que foi pesquisado
- **Find Skills** instalado a partir do repositório oficial `vercel-labs/skills` (pacote npm `skills`, mantido pela Vercel).
- Skills de Meta Ads avaliadas: nenhuma gera o dashboard completo sozinha. A mais útil é `tristanmanchester/agent-skills@meta-ads-cli`, que lê dados pela ferramenta oficial da Meta. Foi instalada e testada (16 de 16 testes passaram).
- A Meta lançou em abril/2026 uma CLI oficial (pacote PyPI `meta-ads`, comando `meta`, exige token de usuário do sistema) e um conector MCP oficial (`mcp.facebook.com/ads`, beta, gratuito, login com Facebook).
- Atenção ao nome: `meta-ads-cli` no PyPI é um projeto independente, não da Meta.
- Dois erros encontrados no relatório antigo: custo por seguidor R$ 1,83 (o correto era R$ 1,64) e Fundo com R$ 1.737,07 no resumo contra R$ 1.737,03 na seção.

## O que existe no projeto
| Caminho | Para que serve |
|---|---|
| `CLAUDE.md` | Papel do Midas, tom de resposta, segurança. Lido automaticamente |
| `memoria/relatorio-meta-ads.md` | Estrutura, regras e visual do relatório. **Ler antes de gerar qualquer relatório** |
| `relatorio/gerar.py` | Gera HTML e PDF a partir de um JSON |
| `relatorio/modelo/relatorio.html.j2` | Template do relatório |
| `relatorio/pdf.js` | Converte HTML em PDF e avisa se o conteúdo estourar a página |
| `relatorio/exemplos/cliente-exemplo.json` | Dados fictícios no formato que o Midas preenche |
| `relatorio/modelo-aprovado/` | PDF aprovado, imagens das 4 páginas e dados do modelo |
| `.claude/skills/find-skills`, `.claude/skills/meta-ads-cli` | Skills instaladas |
| `saida/` | Relatórios gerados (fora do git, de propósito) |

Como gerar: `python3 relatorio/gerar.py relatorio/exemplos/cliente-exemplo.json` (precisa de Python com jinja2 e do Playwright com Chromium).

## Estrutura do relatório aprovado (4 páginas A4)
1. **Resumo:** investimento total com barra por etapa (Topo, Meio, Fundo), resultados principais, tabela contra o período anterior, texto "Leitura do mês".
2. **Instagram (topo, azul):** investido, alcance, visitas ao perfil, cliques na bio, novos seguidores, custo por seguidor, gráfico do alcance ao seguidor.
3. **Vídeo (meio, laranja):** gasto, views de 15s, 50%, 75%, 95% com custo de cada, barras de retenção.
4. **WhatsApp (fundo, verde):** investido, impressões, alcance, cliques, conversas iniciadas, custo por conversa, gráfico do anúncio à conversa.

Custos são sempre calculados pelo script, nunca digitados.

## Git
- Repositório: `Hafaell/Mhidas-gestao-de-trafego`.
- `main`: raiz nova, sem ligação com a branch da sessão, com o projeto inteiro (commit `e10020f`).
- `develop`: aponta para o mesmo commit da `main`.
- `claude/affectionate-gates-j4rctl`: branch original da sessão, ainda é o branch padrão no GitHub. Para apagá-la é preciso antes trocar o padrão para `main` em Settings → Branches.
- Este arquivo de contexto foi criado depois e ainda **não foi commitado**.

## Situação em 14/11/2026 (fim da sessão)
- Nenhum dado real de cliente conectado ainda. O conector da Meta não estava carregado nesta sessão (só Gmail, Notion, Windsor.ai e n8n, pendentes de autorização).
- O gestor colou `https://mcp.facebook.com/ads` na **busca** do diretório de conectores e apareceram só produtos de terceiros (Adspirer, Windsor.ai, circle-skills, Ory, Ryze AI). **Nenhum é o conector oficial da Meta; não usar** [Certa].
- Caminho certo: botão **"Adicionar conector personalizado"** em https://claude.ai/customize/connectors, com nome "Meta Ads" e a URL no campo de servidor, depois Conectar e login pessoal do Facebook. Se o botão não existir no plano do gestor, partir para o plano B (token + CLI `meta`).
- O gestor vai abrir uma sessão nova para continuar.

## Pendências e próximos passos
1. Adicionar o conector **personalizado** em https://claude.ai/customize/connectors (`https://mcp.facebook.com/ads`), somente leitura, marcando as contas dos clientes. Não pela barra de busca.
2. Abrir uma **sessão nova** no projeto (o conector só carrega no início da sessão; nesta sessão ele não estava disponível).
3. Testar com uma conta real e confirmar de onde vêm visitas ao perfil, cliques na bio e seguidores (talvez exijam a API do Instagram, e não a de anúncios) [Provável].
4. Plano B se o conector não funcionar na nuvem: CLI `meta` com token (`ACCESS_TOKEN` no `.env`, nunca no git).
5. Definir como classificar cada campanha em topo, meio e fundo e guardar isso por cliente.
6. ~~Fluxo de relatórios em lote~~ feito em 14/11/2026: skill `relatorio-cliente` + agente `montador-relatorio` (ver `memoria/relatorio-meta-ads.md`). Os cadastros em `clientes/` são criados conforme os clientes forem pedidos. O conector Meta Ads já aparece carregado na sessão de 14/11/2026.
7. Trocar o branch padrão para `main` no GitHub e decidir se apaga a `claude/...`.
8. Fase seguinte: relatório de Google Ads (estrutura já descrita na memória).

## Regras de resposta do gestor
Português do Brasil, direto ao ponto, sem bajulação, sem travessão longo, sem jargão corporativo, marcar alegações não óbvias com [Certa], [Provável] ou [Adivinhando], e pedir confirmação antes de apagar, mover ou criar arquivos em massa e mexer em integrações. O projeto é só leitura: nunca alterar campanhas dos clientes.
