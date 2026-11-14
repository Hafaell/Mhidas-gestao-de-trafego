---
name: relatorio-cliente
description: Use quando o gestor pedir o relatório de um ou mais clientes da Agência Lupa, em qualquer forma ("faz o relatório do Dr. Fulano", "relatório de outubro da Clínica X", "gera os relatórios da Ana e do Rodrigo", "relatório de todos os clientes"). Cobre relatório mensal de Meta Ads em PDF no modelo aprovado.
---

# Relatório de cliente (Meta Ads)

Esta skill organiza o pedido e despacha **um agente `montador-relatorio` por cliente, em paralelo**. Quem busca os dados e gera o PDF é o agente. A sessão principal só prepara, despacha e junta os resultados.

Antes de tudo, leia `memoria/relatorio-meta-ads.md` (regras do relatório e mapa de métricas).

## Passo 1: entender o pedido

Extraia da mensagem do gestor:

| Item | Regra |
|---|---|
| Clientes | Um ou vários nomes. "Todos" = todos os arquivos em `clientes/`. |
| Período | Mês citado ("relatório de outubro"). Sem mês: **mês anterior completo** (dia 1 ao último dia). |
| Período anterior | Mês imediatamente antes do período, para as comparações. |
| Leitura do mês | Se o gestor escreveu um texto para o cliente, ele vai literal em `observacoes`. |

## Passo 2: localizar cada cliente

Para cada nome, procure em `clientes/*.json` (campos `nome` e `apelidos`, sem diferenciar maiúscula nem acento).

- **Achou um:** use o arquivo.
- **Achou mais de um:** pergunte qual.
- **Não achou:** é cliente novo. Chame `ads_get_ad_accounts` (conector Meta Ads, todas as páginas), mostre as contas com nome parecido e pergunte qual é a do cliente. Com a resposta, crie `clientes/<slug>.json` no formato de `relatorio/exemplos/cliente-config-exemplo.json` (só `nome`, `apelidos`, `ad_account_id`, `descricao` se souber; o agente completa o resto).
- Conta com `is_queryable: false` ou `is_ads_mcp_enabled: false`: avise o gestor com o motivo e não despache esse cliente.

Mais de 5 clientes de uma vez: confirme a lista com o gestor antes de despachar (regra do CLAUDE.md sobre criar arquivos em massa).

## Passo 3: checagem rápida do ambiente (uma vez por sessão)

```bash
python3 -c "import jinja2" && node -e "require('playwright')"
```

Se falhar, pare e avise o gestor do que falta (`pip install jinja2`, `npm install playwright` e `npx playwright install chromium`). Não instale nada sem ele pedir.

## Passo 4: despachar os agentes em paralelo

Faça **todas** as chamadas `Agent` na **mesma mensagem**, uma por cliente, com `subagent_type: "montador-relatorio"`. Nunca um cliente de cada vez.

Prompt de cada agente (preencha os campos, nada além disso):

```
Cliente: <arquivo clientes/<slug>.json>
Período: <AAAA-MM-DD> a <AAAA-MM-DD>
Período anterior: <AAAA-MM-DD> a <AAAA-MM-DD>
Leitura do mês do gestor: <texto literal, ou "nenhuma, escreva um rascunho">
```

## Passo 5: juntar e entregar

Quando todos voltarem, responda ao gestor com uma tabela curta:

| Cliente | Status | Ver relatório | PDF | Pendências |
|---|---|---|---|---|

- **Ver relatório** é obrigatório: link markdown para o `Link HTML` que o agente devolveu, ex. `[abrir](file:///C:/.../saida/relatorio-x-2026-10.html)`, para o gestor abrir no navegador direto do chat. Se o agente não devolveu, gere você com `pathlib.Path(...).resolve().as_uri()`.
- Caminho de cada PDF como link clicável.
- Pendências que o agente devolveu (dado que faltou, campanha fora do modelo, texto em rascunho, página estourada).
- Se algum agente falhou, diga qual e por quê. Não esconda falha atrás de "concluído".
- Ofereça abrir um deles com `python3 relatorio/servir.py <nome-sem-extensão>`.

Pedido de ajuste depois ("muda o texto do vídeo", "o tema é Joelho"): edite o JSON em `saida/dados/` e rode `python3 relatorio/gerar.py <json>` de novo. Não precisa buscar os dados outra vez.

## Regras que não mudam

- Só leitura. Nenhuma ferramenta do Meta Ads que crie, altere, ative ou apague algo.
- Regra nova do gestor sobre relatórios vai para `memoria/relatorio-meta-ads.md`.
- Decisão nova sobre um cliente (classificação de campanha, tema do vídeo, foto) vai para o `clientes/<slug>.json` dele.
