# Memória: relatório Meta Ads (Midas)

Ler antes de gerar ou alterar qualquer relatório. Decisões do gestor de 13 e 14/11/2026, salvo outra data.

## Contexto e regras fixas

- **Agência Lupa** (nome no rodapé). Mais de 30 clientes no Meta Ads; montar à mão levava ~2 h por cliente.
- **Só Meta Ads.** Google Ads é fase futura (ver fim do arquivo).
- **Tudo gratuito**: nada de Looker Studio pago, Supermetrics, Windsor, Porter etc.
- **Acesso:** as BMs são dos clientes; o gestor entra pelo usuário pessoal do Facebook, via **conector oficial da Meta no claude.ai** (`mcp.facebook.com/ads`). Só leitura.
- **Não usar o Composio** (o Instagram dele é o pessoal do gestor). Ignorar a skill "gestor-de-trafego" do claude.ai.
- **Entrega:** só o HTML, aberto em localhost com `servir.py`, link `http://localhost:<porta>` no chat (uma porta por cliente, a partir de 8000). Não gerar nem listar arquivo PDF: o gestor baixa pelo botão "Baixar PDF" (sai completo, todas as páginas) e sobe no Drive do cliente.
- **Estrutura flexível:** a seção só aparece se houver campanha daquele tipo **com gasto no período**. Campanha pausada hoje mas que gastou entra; ativa sem gasto fica fora. Citar no resumo as descartadas.
- **Visual livre, dados fixos:** pode melhorar o visual, mas todos os dados do dashboard antigo continuam (seguidores, cliques na bio, retenção do vídeo, conversas).
- **Foto:** a de perfil do Instagram do cliente. Sem foto, iniciais.
- Custos (por seguidor, por conversa, por view) são sempre calculados pelo gerador, nunca digitados.

## Fluxo

1. Gestor pede o relatório de um ou mais clientes (padrão: mês anterior completo).
2. Skill `relatorio-cliente` localiza os clientes e despacha um agente `montador-relatorio` por cliente, em paralelo.
3. O agente busca os dados, classifica as campanhas, monta o JSON e roda `gerar.py`.
4. A sessão principal sobe o localhost e manda os links.

O mapa completo de métricas (campo da API para cada card) está em `.claude/agents/montador-relatorio.md`.

## Onde fica cada coisa

| O quê | Onde | Dura |
|---|---|---|
| Cadastro do cliente (conta, @, tema do vídeo, classificação das campanhas) | `clientes/<slug>.json` (fora do git) | sempre |
| Foto do cliente | `clientes/fotos/<slug>.jpg` (fora do git) | sempre |
| JSON de dados do mês, HTML e CSS gerados | pasta temporária: `<temp>/midas/` (ver `python3 relatorio/gerar.py --pasta-saida`) | uso único |
| Token do Instagram | `.env` (`ACCESS_TOKEN`, fora do git) | ~60 dias |

## Modelo atual (`relatorio/modelos/3-atual-dashboard/`, aprovado em 14/11/2026)

A4 em pé, fundo cinza-claro, cards brancos. Imagens de referência em `referencia/`.

- **Cabeçalho (todas as páginas):** azul-marinho, foto, logo Meta, nome do cliente / "Relatório de leads · Meta Ads", caixas "Período" e "Comparado a".
- **Bloco "Investimento do período" (todas as páginas):** total, barra por etapa e legenda Topo/Meio/Fundo com valor e %. Manter assim, não trocar por cards pequenos.
- **Cores por etapa:** Topo `#2a78d6` azul, Meio `#eb6834` laranja, Fundo `#1baf7a` verde.
- **Selos de variação:** verde melhorou, vermelho piorou, cinza investimento (neutro). Em custo, cair é bom.
- Cada seção tem a caixa "O que esse resultado mostra" (comentário curto).

**Páginas:**
1. Investimento + **Crescimento do Instagram** (Topo) + **Captação de Leads no WhatsApp** (Fundo). Página apertada: se aparecer "página 1 estourou", encurtar os comentários.
2. Investimento + **Meio de Funil Video View <tema>**.
3. Investimento + "Do anúncio ao resultado" (fluxos com taxas) + comparação com o período anterior + "Leitura do mês" (texto do gestor).

### Cards por seção

| Seção | Campanha de origem (padrão de nome) | Cards |
|---|---|---|
| Instagram (Topo) | `[TOPO] [TRF] Novos Seguidores - <data>`; várias = somar | Valor Investido, Alcance, Visitas ao perfil, Clique na Bio, Novos Seguidores, Investido/Seguidor |
| Vídeo (Meio) | `[MEIO]` e `[VV]` no nome; só as que gastaram, somadas | Linha de cima: Valor Gasto, Visualização 15 seg, Custo 15 seg, Tempo médio assistido (some sem dado). Abaixo à esquerda: 50%, 75%, 95% com custo de cada. À direita: funil em trapézios laranja (15 seg, 50%, 95%), largura fixa decrescente (forma, não escala) |
| WhatsApp (Fundo) | `[FUNDO][MSG] ...` | Valor Investido, Impressões, Alcance, Cliques, Conversas iniciadas, Investido/Conversa |

### Decisões sobre os dados

- **Clique na Bio:** vem da API do Instagram (`website_clicks`, total do perfil, orgânico + anúncio), não da de anúncios. **Obrigatório em todo relatório**; nunca "–" nem pendência. Se falhar (erro 190 = token vencido), parar e avisar o gestor.
- **Visitas ao perfil:** `results` com indicador `profile_visit_view` na campanha de topo (só existe se o conjunto otimiza `VISIT_INSTAGRAM_PROFILE`). Sem isso, buscar nos insights do Instagram (`profile_views`).
- **Cliques do WhatsApp:** `link_click` (cliques no link). Nunca `clicks`.
- **15 seg = ThruPlay** (15 s ou vídeo completo). Em vídeo curto, o 50% pode passar do ThruPlay; é normal.
- **Vídeo:** das métricas extras da API, só o tempo médio entra. Não incluir reproduções totais, 2 s, 3 s, 25% nem 100%. Para trocar o funil para azul: `CORES_FUNIL` em `relatorio/midas/secoes/video.py`.
- Não existe na API de anúncios métrica de "cliques na bio" nem campo dedicado de "visitas ao perfil" (testado com `ads_get_field_context`) [Certa].

## Token do Instagram (`ACCESS_TOKEN` no `.env`)

Estendido em 14/11/2026, vence por volta de **13/01/2027**. A partir de **06/01/2027**, avisar o gestor no início de qualquer sessão de relatório. Erro 190 = vencido.

Renovar:
1. developers.facebook.com/tools/explorer, app `App Cursosobredireito`, "Obter token de acesso do usuário".
2. Permissões: `pages_show_list`, `pages_read_engagement`, `business_management`, `ads_read`, `read_insights` e as do Instagram. Generate Access Token, marcando todas as páginas e Instagrams dos clientes (inclusive novos).
3. developers.facebook.com/tools/debug/accesstoken, colar o token, "Estender token de acesso".
4. Trocar a linha `ACCESS_TOKEN=` do `.env` (sem aspas). Nunca colar no chat nem no git.
5. Pedir ao Midas uma leitura de teste e atualizar aqui a nova data de vencimento.

## Código (regra do gestor: orientado a objetos, HTML, CSS e Python separados)

- **Python** em `relatorio/midas/` (mapa em `midas/__init__.py`). Seção nova = classe nova em `midas/secoes/` + uma linha em `secoes/__init__.py`. `gerar.py` e `servir.py` são só a porta de entrada. Caminhos todos em `midas/config.py`.
- **HTML** em peças (`html/componentes/`, `html/paginas/`); **CSS** em um arquivo só.
- Modelo novo = pasta nova em `relatorio/modelos/` (ver o `LEIAME.md` de lá).
- Antes de dar uma refatoração por boa, comparar o exemplo antes e depois, página a página (`node relatorio/pdf.js <html> <pdf> --png <pasta>`).
- Ambiente: `python3` com `jinja2`; Playwright + Chromium em `node_modules/` (`npm install`). No Windows, usar `python3` (o `python` do Git Bash não tem jinja2).

```bash
python3 relatorio/gerar.py relatorio/exemplos/cliente-exemplo.json   # HTML na pasta temporária
python3 relatorio/servir.py <nome-do-html-sem-extensão> --porta 8000 --sem-abrir
```

## Google Ads (fase futura)

Página própria, fundo cinza-chumbo, logo Google Ads, título "Relatório de Vendas · Google Ads". Faixa com Valor Investido, Impressões, Cliques, Conversões, Custo/conv.; funil Impressões → Cliques → Conversões → Custo/conv.; tabela de termos de pesquisa (termo, impressões, cliques, custo); tabela por campanha (impressões, CPM, CPV, cliques, CPC, conversões, custo/conv., custo).
