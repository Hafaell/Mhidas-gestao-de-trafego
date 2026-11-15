# Memória: relatório Meta Ads (Midas)

Regras gerais do relatório. Decisões do gestor de 13 a 15/11/2026, salvo outra data. Cada regra mora num lugar só:

| Assunto | Onde está | Quem lê |
|---|---|---|
| Regras gerais, fluxo, período anterior, token, código | **este arquivo** | sessão principal e todos os agentes |
| Campos do JSON, fonte de cada número na API, decisões sobre os dados | `relatorio/CONTRATO-DADOS.md` | `coletor-dados` (e o `editor-layout`, para saber o que existe) |
| Como o visual é montado, cards de cada seção, regras de visual fechadas | `relatorio/modelos/<atual>/MAPA.md` | `editor-layout` |
| Despacho dos agentes, entrega em localhost, servidores e portas | `.claude/skills/relatorio-cliente/SKILL.md` | sessão principal |
| Quem dá e quem não dá para gerar hoje (4 bloqueados pela Meta) | `memoria/STATUS-RELATORIOS.md` | sessão principal, antes de despachar |
| O que o relatório de cada cliente tem (seções, campanhas, configuração) | `memoria/por-cliente/<slug>.md`, índice em `LEIAME.md` | `coletor-dados` |
| Google Ads e envio para o Drive | `memoria/futuras-atualizacoes.md` | só quando entrar |

Regra nova do gestor vai para o arquivo do assunto dela (dados, visual, entrega), não para cá, a menos que seja geral.

## Contexto e regras fixas

- **Agência Lupa** (nome no rodapé). Mais de 30 clientes no Meta Ads; montar à mão levava ~2 h por cliente.
- **Só Meta Ads.** Google Ads é fase futura.
- **Tudo gratuito**: nada de Looker Studio pago, Supermetrics, Windsor, Porter etc.
- **Acesso:** as BMs são dos clientes; o gestor entra pelo usuário pessoal do Facebook, via **conector oficial da Meta no claude.ai** (`mcp.facebook.com/ads`). Só leitura.
- **Não usar o Composio** para o relatório (o Instagram dele é o pessoal do gestor). Ignorar a skill "gestor-de-trafego" do claude.ai.
- **Entrega:** só o HTML, aberto em localhost e no navegador do gestor; nunca arquivo PDF (o gestor baixa pelo botão "Baixar PDF" e sobe no Drive do cliente). Passo a passo e regras de porta: skill `relatorio-cliente`, Passo 5.
- **Pedido de relatório padrão:** mês anterior completo.

## Fluxo: três agentes, um papel cada (pedido do gestor, 15/11/2026)

1. Skill `relatorio-cliente` localiza os clientes e despacha, em paralelo, um **`coletor-dados`** por cliente: busca, classifica, grava e confere o JSON.
2. Com os JSONs prontos, um **`montador-relatorio`** por cliente junta o JSON com o modelo aprovado (`gerar.py`) e confere as páginas.
3. A sessão principal sobe o localhost e manda os links.
4. Pedido de mudança de aparência vai para o **`editor-layout`**, que parte do modelo aprovado (nunca do zero), testa numa cópia e só aplica depois de o gestor aprovar.

Coletor e editor combinam pelo `relatorio/CONTRATO-DADOS.md`: o editor pede campo novo na tabela "Pedidos do layout" e o coletor responde.

**Período anterior (regra do gestor, 14/11/2026):** os **mesmos dias do mês anterior**, com a mesma quantidade de dias. Pediu 09 a 20/11, compara com 09 a 20/10; nunca os dias imediatamente antes (não vale 25/10 a 08/11). Se cair nos dias 30 e 31 e o mês anterior for mais curto, mantém a quantidade de dias e termina no dia 1 (20 a 31/10 compara com 20/09 a 01/10). Exceção minha, ainda não confirmada pelo gestor: mês inteiro compara com o mês anterior inteiro. Calcular sempre com `python3 relatorio/gerar.py --periodo-anterior <início> <fim>`.

## Onde fica cada arquivo

| O quê | Onde | Dura |
|---|---|---|
| Cadastro do cliente (conta, @, classificação das campanhas, `layout`) | `clientes/<slug>.json` (fora do git) | sempre |
| Foto do cliente | `clientes/fotos/<slug>.jpg` (fora do git) | sempre |
| Histórico mensal (gráfico de evolução) | `clientes/historico/<slug>.json` (fora do git, gravado por `gerar.py --registrar-historico`) | sempre |
| Relatórios feitos à mão de out/2026 (PDFs, fonte da memória por cliente) | `memoria/relatorios-feitos-a-mão-dos-clientes/` (só no computador do gestor, fora do git) | sempre |
| JSON de dados do mês, HTML e CSS gerados | pasta temporária `<temp>/midas/` (`python3 relatorio/gerar.py --pasta-saida`) | uso único |
| Token do Instagram | `.env` (`ACCESS_TOKEN`, fora do git) | ~60 dias |

## Token do Instagram (`ACCESS_TOKEN` no `.env`)

Estendido em 14/11/2026, vence por volta de **13/01/2027**. O `python3 relatorio/verificar_token.py` confere a validade no início de cada pedido de relatório: avisa se faltam menos de 7 dias e para tudo se vencer (erro 190). Nunca mostra o token.

Renovar:
1. developers.facebook.com/tools/explorer, app `App Cursosobredireito`, "Obter token de acesso do usuário".
2. Permissões: `pages_show_list`, `pages_read_engagement`, `business_management`, `ads_read`, `read_insights` e as do Instagram. Generate Access Token, marcando todas as páginas e Instagrams dos clientes (inclusive novos).
3. developers.facebook.com/tools/debug/accesstoken, colar o token, "Estender token de acesso".
4. Trocar a linha `ACCESS_TOKEN=` do `.env` (sem aspas). Nunca colar no chat nem no git.
5. Pedir ao Midas uma leitura de teste e atualizar aqui a nova data de vencimento.

## Código (regra do gestor: orientado a objetos, HTML, CSS e Python separados)

- **Python** em `relatorio/midas/` (mapa de cada arquivo em `midas/__init__.py`). Seção nova = classe nova em `midas/secoes/` + uma linha em `secoes/__init__.py`. `gerar.py`, `servir.py`, `instagram_perfil.py` e `verificar_token.py` são só portas de entrada. Caminhos todos em `midas/config.py`.
- **Conferência antes de gerar** (`midas/conferencia.py`): ERRO impede o relatório (estimativa de cliques na bio impossível, valor negativo, investido diferente do `conferencia.investido_api`); AVISO vira pendência. Campos obrigatórios e desejáveis: atributos `campos_obrigatorios` e `campos_desejaveis` da classe da seção.
- **HTML (15/11/2026):** um arquivo com o documento inteiro (`html/relatorio.html.j2`); só o que se repete vai para `html/componentes.html.j2`. Não quebrar em um arquivo por componente ou página. **CSS** num arquivo só.
- **Modelos:** só o atual guarda HTML, CSS e prints; modelo antigo vai para `relatorio/modelos/legado/<pasta>/` só com os PNG (regra de 15/11/2026). Passo a passo em `relatorio/modelos/LEIAME.md`.
- Antes de dar uma refatoração por boa, comparar os exemplos antes e depois, página a página (`node relatorio/pdf.js <html> <pdf> --png <pasta>`).
- Ambiente: `python3` com `jinja2`; Playwright + Chromium em `node_modules/` (`npm install`). No Windows, usar `python3` (o `python` do Git Bash não tem jinja2).

```bash
python3 relatorio/gerar.py relatorio/exemplos/cliente-exemplo.json   # HTML na pasta temporária
python3 relatorio/gerar.py <dados.json> --so-conferir                 # só a conferência (coletor-dados)
python3 relatorio/servir.py <nome-do-html-sem-extensão> --porta 8000   # abre no navegador
python3 relatorio/servir.py <nome> --pasta <pasta> --porta 8001        # HTML de outra pasta (prévia do editor)
```
