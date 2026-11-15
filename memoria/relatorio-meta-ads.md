# Memória: relatório Meta Ads (Midas)

Ler antes de gerar ou alterar qualquer relatório. Decisões do gestor de 13 e 14/11/2026, salvo outra data.

**Quem dá e quem não dá para gerar hoje: `memoria/STATUS-RELATORIOS.md`** (4 clientes estão bloqueados pela Meta no conector). Conferir lá antes de despachar o agente.

## Contexto e regras fixas

- **Agência Lupa** (nome no rodapé). Mais de 30 clientes no Meta Ads; montar à mão levava ~2 h por cliente.
- **Só Meta Ads.** Google Ads é fase futura (ver fim do arquivo).
- **Tudo gratuito**: nada de Looker Studio pago, Supermetrics, Windsor, Porter etc.
- **Acesso:** as BMs são dos clientes; o gestor entra pelo usuário pessoal do Facebook, via **conector oficial da Meta no claude.ai** (`mcp.facebook.com/ads`). Só leitura.
- **Não usar o Composio** (o Instagram dele é o pessoal do gestor). Ignorar a skill "gestor-de-trafego" do claude.ai.
- **Entrega:** só o HTML, aberto em localhost com `servir.py`, link `http://localhost:<porta>` no chat (uma porta por cliente, a partir de 8000). **Sempre abrir a página no navegador do gestor (regra de 15/11/2026):** rodar `servir.py` SEM `--sem-abrir`, porque só o link no chat não mostra nada a ele. Vale também ao mostrar o template ou uma alteração de visual.
- **Servidores locais (regra do gestor, 15/11/2026):** deixar o servidor no ar por pelo menos 1 hora depois de mandar o link; depois disso pode fechar. Ao subir um servidor novo, antes verificar se o antigo daquela porta ainda está no ar (`netstat -ano | grep ":<porta> .*LISTENING"`); se estiver, fechar (`Stop-Process -Id <pid>`, autorizado pelo gestor) e servir o HTML novo nessa porta. Nunca deixar dois servidores na mesma porta (já aconteceu: 4 presos na 8000 mostrando o HTML velho). Não gerar nem listar arquivo PDF: o gestor baixa pelo botão "Baixar PDF" (sai completo, todas as páginas) e sobe no Drive do cliente.
- **Estrutura flexível:** a seção só aparece se houver campanha daquele tipo **com gasto no período**. Campanha pausada hoje mas que gastou entra; ativa sem gasto fica fora. Citar no resumo as descartadas.
- **Visual livre, dados fixos:** pode melhorar o visual, mas todos os dados do dashboard antigo continuam (seguidores, cliques na bio, retenção do vídeo, conversas).
- **Foto:** a de perfil do Instagram do cliente. Sem foto, iniciais.
- Custos (por seguidor, por conversa, por view) são sempre calculados pelo gerador, nunca digitados.

## Fluxo

1. Gestor pede o relatório de um ou mais clientes (padrão: mês anterior completo).
   - **Período anterior (regra do gestor, 14/11/2026):** os **mesmos dias do mês anterior**, com a mesma quantidade de dias. Pediu 09 a 20/11, compara com 09 a 20/10; pediu 01 a 15, compara com 01 a 15 do mês anterior. Nunca "os dias imediatamente antes" (não vale 25/10 a 08/11). Se o intervalo cair nos dias 30 e 31 e o mês anterior for mais curto, mantém a quantidade de dias e deixa terminar no dia 1 (20 a 31/10 compara com 20/09 a 01/10). Exceção minha, ainda não confirmada pelo gestor: mês inteiro (dia 1 ao último) compara com o mês anterior inteiro. Para calcular: `python3 relatorio/gerar.py --periodo-anterior <início> <fim>`.
2. Skill `relatorio-cliente` localiza os clientes e despacha um agente `montador-relatorio` por cliente, em paralelo.
3. O agente busca os dados, classifica as campanhas, monta o JSON e roda `gerar.py`.
4. A sessão principal sobe o localhost e manda os links.

O mapa completo de métricas (campo da API para cada card) está em `.claude/agents/montador-relatorio.md`.

## Onde fica cada coisa

| O quê | Onde | Dura |
|---|---|---|
| Cadastro do cliente (conta, @, tema do vídeo, classificação das campanhas) | `clientes/<slug>.json` (fora do git) | sempre |
| Memória do cliente (tipos de campanha, seções e particularidades do relatório dele, tirados dos relatórios feitos à mão de out/2026) | `memoria/por-cliente/<slug>.md`, índice em `LEIAME.md` (no git, por decisão do gestor de 15/11/2026) | sempre |
| Foto do cliente | `clientes/fotos/<slug>.jpg` (fora do git) | sempre |
| JSON de dados do mês, HTML e CSS gerados | pasta temporária: `<temp>/midas/` (ver `python3 relatorio/gerar.py --pasta-saida`) | uso único |
| Histórico mensal (números do mês, para o gráfico de evolução) | `clientes/historico/<slug>.json` (fora do git, gravado por `gerar.py --registrar-historico`) | sempre |
| Token do Instagram | `.env` (`ACCESS_TOKEN`, fora do git) | ~60 dias |

## Modelo atual (`relatorio/modelos/4-cabecalho-leve/`, aprovado em 15/11/2026; veio do 3, de 14/11, hoje só em `legado/`)

A4 em pé, fundo cinza-claro, cards brancos. Imagens de referência em `referencia/`.

- **Cabeçalho de seção leve (regra do gestor, 15/11/2026):** cada seção (Instagram, vídeo, WhatsApp) abre com ícone redondo + título à esquerda, etapa do funil e % do investimento à direita (cinza pequeno) e uma linha fina com um trecho na cor da etapa. **Nunca** a faixa azul-marinho de ponta a ponta: o gestor achou agressiva. O cabeçalho da página (azul-marinho, com foto) continua. Ao testar visual novo, fazer numa cópia na pasta temporária (`gerar.py --modelo <caminho absoluto>`) e só virar modelo depois de o gestor aprovar.

- **Cor dos ícones de seção (regra do gestor, 15/11/2026):** Instagram em laranja com gradiente do Instagram; landing page em azul, com ícone de globo; WhatsApp na cor do Fundo (verde), como estava. Só o círculo do ícone muda: a linha fina do título continua na cor da etapa. Atributo `cor_icone` na classe da seção.
- **Cabeçalho (todas as páginas):** azul-marinho, foto, logo Meta, nome do cliente / "Relatório de leads · Meta Ads", caixas "Período" e "Comparado a".
- **Bloco "Investimento do período" (todas as páginas):** total, barra por etapa e legenda Topo/Meio/Fundo com valor e %. Manter assim, não trocar por cards pequenos.
- **Cores por etapa:** Topo `#2a78d6` azul, Meio `#eb6834` laranja, Fundo `#1baf7a` verde.
- **Selos de variação (regra do gestor, 15/11/2026): só na tabela "Comparação com o período anterior".** Nos cards (Instagram, vídeo, landing page, WhatsApp), no bloco de investimento e na evolução mensal não aparece seta nem %. Lá: verde melhorou, vermelho piorou, cinza investimento (neutro); em custo, cair é bom.
- **Página cheia, com respiro (regra do gestor, 15/11/2026):** o conteúdo ocupa a página até o rodapé (classe `estica` no CSS: os blocos principais crescem e os cards, a tabela e os gráficos esticam junto), sem meia página vazia e sem ficar apertado. Folga de ~6 mm antes do rodapé. Ao mudar o layout, conferir as 4 páginas em PNG.
- **Sem notas de interpretação (regra do gestor, 15/11/2026):** o relatório não tem a caixa "O que esse resultado mostra" (`comentario`) nem a "Leitura do mês" (`observacoes`). Só os dados. Não reintroduzir sem o gestor pedir.

**Páginas** (o plano sai de `Relatorio._montar_paginas`, conforme as seções que o cliente tem):
1. **Blocos de cards**: Investimento + Instagram (Topo) + landing page e WhatsApp (Fundo). Até 3 blocos por página (com 3, cards compactos); 4 blocos viram 2 páginas de 2.
2. **Uma página por vídeo**: Vídeo de topo de funil (azul) e Vídeo de meio de funil (laranja), cada um com cards + funil.
3. **"Do anúncio ao resultado"** (fluxos com taxas) + comparação com o período anterior. Com mais de 2 fluxos ou mais de 9 linhas, fluxos e comparação ficam em páginas separadas.
4. **Evolução nos últimos meses**: investimento total e um indicador por seção (seção repetida soma os blocos). Só existe com 2 meses ou mais de dados. Mês parcial aparece com `*`.
- O bloco "Investimento do período" soma por **etapa** (Topo, Meio, Fundo), não por seção: no Kondo, Fundo = landing page + WhatsApp, como no relatório feito à mão.

### Seções que vieram dos relatórios feitos à mão (15/11/2026)

Pedido do gestor: cada cliente sai igual ao relatório que ele fazia à mão. O que cada cliente usa fica na memória dele (`memoria/por-cliente/<slug>.md`, bloco "Configuração do relatório") e em `layout` no `clientes/<slug>.json`. Exemplos fictícios: `relatorio/exemplos/cliente-exemplo-completo.json` e `cliente-exemplo-organico.json`; prints em `relatorio/modelos/4-cabecalho-leve/referencia/secoes-novas/`.

| Seção (chave no JSON) | Para quem | O que mostra |
|---|---|---|
| `video_topo` | quem tem `[TOPO][VV]`/CP1 (11 clientes) | mesmos cards e funil do vídeo de meio, em azul, página própria |
| `landing_page` | Kondo, Doc Circle | Valor investido, Impressões, Cliques no link, Visualizações da página, Leads (ou "Conversões"), Custo por lead; fluxo clique → página → lead |
| `whatsapp` em lista (`bloco`) | Langen (São Paulo, Campinas), Paulo Rosenbaum (Dor, Nova Andradina, Ivinhema) | um bloco de WhatsApp por cidade/tema, título "Leads no WhatsApp · <bloco>" |
| `instagram_organico` | Samico, Cabrejos | Alcance do perfil, Visitas, Cliques na bio, Novos seguidores, sem valor investido (fora do total) |
| `extras: ["custo_visita_perfil"]` no Instagram | Patrícia Canelas | 7º card "Custo por visita ao perfil" |
| `rotulos_etapa` | Villalva ("Meio · Remarketing"), Instituto Domingues ("Meio · Pessoas engajadas") | troca o rótulo da etapa no investimento e no cabeçalho da seção |
| `tema` em qualquer seção | Instituto Domingues (Mela), Cabrejos (Tricologia) | vai no título da seção |

- **Instagram tem limite de 30 dias por consulta** (testado em 15/11/2026). O `relatorio/instagram_perfil.py` divide o período e soma. O alcance do perfil somado de 2 janelas é aproximado.
### Cards por seção

| Seção | Campanha de origem (padrão de nome) | Cards |
|---|---|---|
| Instagram (Topo) | `[TOPO] [TRF] Novos Seguidores - <data>`; várias = somar | Valor Investido, Alcance, Visitas ao perfil, Clique na Bio (estimativa via anúncio), Novos Seguidores, Investido/Seguidor |
| Vídeo de topo e de meio | `[TOPO][VV]`/CP1 vira vídeo de topo; `[MEIO][VV]`/CP2 vira vídeo de meio; só as que gastaram, somadas | Linha de cima: Valor Gasto, Visualização 15 seg, Custo 15 seg, Tempo médio assistido (some sem dado). Abaixo à esquerda: 50%, 75%, 95% com custo de cada. À direita: funil em trapézios laranja (15 seg, 50%, 95%), largura fixa decrescente (forma, não escala) |
| WhatsApp (Fundo) | `[FUNDO][MSG] ...` | Valor Investido, Impressões, Alcance, Cliques, Conversas iniciadas, Investido/Conversa |

### Decisões sobre os dados

- **Clique na Bio = estimativa via anúncio (regra do gestor, 15/11/2026).** Nenhuma API separa o clique na bio por origem [Provável], então o card mostra `cliques na bio × visitas ao perfil via anúncio ÷ visitas totais ao perfil`, com o rótulo "Cliques na bio (est. anúncio)". O JSON traz os números crus (`cliques_bio_total` = `website_clicks` e `visitas_perfil_total` = `profile_views`, ambos da API do Instagram; `visitas_perfil` do Meta Ads) e o gerador calcula `cliques_bio` (`SecaoInstagram.estimar_cliques_bio`). Supõe que quem vem do anúncio clica na bio na mesma taxa do orgânico. Fração limitada a 100% (com aviso). **Obrigatório em todo relatório**: sem algum dos três números, ERRO. Se a API do Instagram falhar (erro 190 = token vencido), parar e avisar o gestor.
- **Novos seguidores = seguidores vindos de TODAS as campanhas (regra do gestor, 15/11/2026).** É o `instagram_profile_follow_v2` no nível da conta (soma de todas as campanhas): Kondo 01 a 15/11/2026 = 72 (seguidores 7 + vídeo topo 6 + vídeo meio 1 + landing page 41 + WhatsApp 17). Não é só a campanha de seguidores (7) nem o perfil inteiro do Instagram (2.858, que inclui orgânico). Custo por seguidor = investido na campanha de Instagram ÷ esse total. Consequência que o gestor aceitou: não bate com o relatório feito à mão, que usava o perfil inteiro (out/2026: 250 no Midas contra 12,8 mil no PDF).
- **Alcance do Instagram = soma do alcance diário do PERFIL (15/11/2026).** É o que o relatório feito à mão mostrava (Kondo out/2026: 1.139.568 contra 1.109.430 no PDF); o `reach` da campanha (34.757) não é usado. Fonte: `relatorio/instagram_perfil.py`.
- **Visitas ao perfil:** `results` com indicador `profile_visit_view` na campanha de topo (só existe se o conjunto otimiza `VISIT_INSTAGRAM_PROFILE`). É o número só do anúncio; nunca trocar pelo `profile_views` do Instagram (isso viraria 100% na estimativa).
- **Cliques do WhatsApp:** `link_click` (cliques no link). Nunca `clicks`.
- **15 seg = ThruPlay** (15 s ou vídeo completo). Em vídeo curto, o 50% pode passar do ThruPlay; é normal.
- **Vídeo:** das métricas extras da API, só o tempo médio entra. Não incluir reproduções totais, 2 s, 3 s, 25% nem 100%. Para trocar o funil para azul: `CORES_FUNIL` em `relatorio/midas/secoes/video.py`.
- Não existe na API de anúncios métrica de "cliques na bio" nem campo dedicado de "visitas ao perfil" (testado com `ads_get_field_context`) [Certa].

## Token do Instagram (`ACCESS_TOKEN` no `.env`)

Estendido em 14/11/2026, vence por volta de **13/01/2027**. O `python3 relatorio/verificar_token.py` confere a validade no início de cada pedido de relatório (a skill `relatorio-cliente` roda sozinha): avisa se faltam menos de 7 dias e para tudo se vencer (erro 190). Ele nunca mostra o token.

Renovar:
1. developers.facebook.com/tools/explorer, app `App Cursosobredireito`, "Obter token de acesso do usuário".
2. Permissões: `pages_show_list`, `pages_read_engagement`, `business_management`, `ads_read`, `read_insights` e as do Instagram. Generate Access Token, marcando todas as páginas e Instagrams dos clientes (inclusive novos).
3. developers.facebook.com/tools/debug/accesstoken, colar o token, "Estender token de acesso".
4. Trocar a linha `ACCESS_TOKEN=` do `.env` (sem aspas). Nunca colar no chat nem no git.
5. Pedir ao Midas uma leitura de teste e atualizar aqui a nova data de vencimento.

## Código (regra do gestor: orientado a objetos, HTML, CSS e Python separados)

- **Conferência antes de gerar** (`midas/conferencia.py`): ERRO impede o relatório (estimativa de cliques na bio impossível, valor negativo, investido diferente do `conferencia.investido_api` lido da API), AVISO vira pendência (campo sem dado, funil estranho como mais conversas que cliques, sem período anterior, foto não achada). Campo obrigatório ou desejável de cada seção: atributos `campos_obrigatorios` e `campos_desejaveis` na classe dela.
- **Python** em `relatorio/midas/` (mapa em `midas/__init__.py`). Seção nova = classe nova em `midas/secoes/` + uma linha em `secoes/__init__.py`. `gerar.py` e `servir.py` são só a porta de entrada. Caminhos todos em `midas/config.py`.
- **HTML (regra do gestor, 15/11/2026):** um arquivo com o documento inteiro (`html/relatorio.html.j2`: head, body e as páginas escritas por extenso). Só vai para outro arquivo o que se repete em várias páginas (`html/componentes.html.j2`) ou o que for muito grande. Não quebrar em um arquivo por componente ou por página. **CSS** em um arquivo só.
- Modelo novo = pasta nova em `relatorio/modelos/` (ver o `LEIAME.md` de lá). **Só o modelo atual guarda HTML, CSS e referências (regra do gestor, 15/11/2026).** Modelo antigo vai para `relatorio/modelos/legado/<pasta>/` com apenas os prints das páginas (PNG), sem HTML nem CSS; o código fica no git.
- Antes de dar uma refatoração por boa, comparar o exemplo antes e depois, página a página (`node relatorio/pdf.js <html> <pdf> --png <pasta>`).
- Ambiente: `python3` com `jinja2`; Playwright + Chromium em `node_modules/` (`npm install`). No Windows, usar `python3` (o `python` do Git Bash não tem jinja2).

```bash
python3 relatorio/gerar.py relatorio/exemplos/cliente-exemplo.json   # HTML na pasta temporária
python3 relatorio/servir.py <nome-do-html-sem-extensão> --porta 8000   # abre o navegador; --sem-abrir só se o gestor pedir
```

## Google Ads (fase futura)

Página própria, fundo cinza-chumbo, logo Google Ads, título "Relatório de Vendas · Google Ads". Faixa com Valor Investido, Impressões, Cliques, Conversões, Custo/conv.; funil Impressões → Cliques → Conversões → Custo/conv.; tabela de termos de pesquisa (termo, impressões, cliques, custo); tabela por campanha (impressões, CPM, CPV, cliques, CPC, conversões, custo/conv., custo).
