---
name: relatorio-cliente
description: Use quando o gestor pedir o relatório de um ou mais clientes da Agência Lupa, em qualquer forma ("faz o relatório do Dr. Fulano", "relatório de outubro da Clínica X", "gera os relatórios da Ana e do Rodrigo", "relatório de todos os clientes"). Cobre relatório mensal de Meta Ads no modelo aprovado, entregue em HTML aberto em localhost (sem arquivo PDF).
---

# Relatório de cliente (Meta Ads)

Esta skill organiza o pedido e despacha **um agente `montador-relatorio` por cliente, em paralelo**. Quem busca os dados e gera o HTML é o agente. A sessão principal só prepara, despacha e junta os resultados.

Antes de tudo, leia `memoria/relatorio-meta-ads.md` (regras do relatório).

## Passo 1: entender o pedido

Extraia da mensagem do gestor:

| Item | Regra |
|---|---|
| Clientes | Um ou vários nomes. "Todos" = todos os arquivos em `clientes/`. |
| Período | Mês citado ("relatório de outubro"). Sem mês: **mês anterior completo** (dia 1 ao último dia). |
| Período anterior | **Os mesmos dias do mês anterior**, com a mesma quantidade de dias (pediu 09 a 20/11, compara com 09 a 20/10; nunca os dias imediatamente antes). Calcule com `python3 relatorio/gerar.py --periodo-anterior <início> <fim>`, sem fazer a conta de cabeça. Regra completa em `memoria/relatorio-meta-ads.md`. |

## Passo 2: localizar cada cliente

Para cada nome, procure em `clientes/*.json` (campos `nome` e `apelidos`, sem diferenciar maiúscula nem acento).

- **Achou um:** use o arquivo.
- **Achou mais de um:** pergunte qual.
- **Não achou:** é cliente novo. Chame `ads_get_ad_accounts` (conector Meta Ads, todas as páginas), mostre as contas com nome parecido e pergunte qual é a do cliente. Com a resposta, crie `clientes/<slug>.json` no formato de `relatorio/exemplos/cliente-config-exemplo.json` (só `nome`, `apelidos`, `ad_account_id`, `descricao` se souber; o agente completa o resto).
- Conta com `is_queryable: false` ou `is_ads_mcp_enabled: false`: avise o gestor com o motivo e não despache esse cliente.

Mais de 5 clientes de uma vez: confirme a lista com o gestor antes de despachar (regra do CLAUDE.md sobre criar arquivos em massa).

## Passo 3: checagem rápida do ambiente e do token (uma vez por sessão)

```bash
python3 -c "import jinja2" && node -e "require('playwright')"
python3 relatorio/verificar_token.py
```

Se a primeira falhar, pare e avise o gestor do que falta (`pip install jinja2`, `npm install playwright` e `npx playwright install chromium`). Não instale nada sem ele pedir.

O `verificar_token.py` confere o `ACCESS_TOKEN` do Instagram (os cliques na bio dependem dele) e nunca mostra o token. Saída 0: siga. Saída 1 (vence em menos de 7 dias): avise o gestor, mas pode seguir se ele mandar. Saída 2 (vencido ou inválido): **pare e avise**, sem despachar agentes. Saída 3 (não deu para verificar, sem token ou sem rede): avise e pergunte se segue.

## Passo 4: despachar os agentes em paralelo

Faça **todas** as chamadas `Agent` na **mesma mensagem**, uma por cliente, com `subagent_type: "montador-relatorio"`. Nunca um cliente de cada vez.

Prompt de cada agente (preencha os campos, nada além disso):

```
Cliente: <arquivo clientes/<slug>.json>
Período: <AAAA-MM-DD> a <AAAA-MM-DD>
Período anterior: <AAAA-MM-DD> a <AAAA-MM-DD>
```

## Passo 5: juntar e entregar

Quando todos voltarem, responda ao gestor com uma tabela curta:

| Cliente | Status | Ver relatório | Pendências |
|---|---|---|---|

- **Entrega só em HTML, sem PDF** (regra do gestor, 14/11/2026). Não liste nem mande arquivo PDF: o gestor baixa pelo botão "Baixar PDF" da própria página.
- **Ver relatório** é obrigatório: para cada cliente, suba o servidor local em segundo plano e mande o link `http://localhost:<porta>`:
  `python3 relatorio/servir.py <nome-sem-extensão> --porta <porta>` (rode com `run_in_background`; sem `--sem-abrir`, para abrir a página no navegador do gestor, regra de 15/11/2026). Uma porta por cliente, começando em 8000. Antes de subir, veja se a porta já tem servidor (`netstat -ano | grep ":<porta> .*LISTENING"`); se tiver, feche o processo (`Stop-Process -Id <pid>`, autorizado pelo gestor em 15/11/2026) e sirva o HTML novo nela. Deixe o servidor no ar por pelo menos 1 hora. Antes de mandar o link, confirme que respondeu 200 com `curl -s -o /dev/null -w "%{http_code}" http://localhost:<porta>` (não use `curl -I`: o servidor não aceita HEAD e responde 501).
- Conferência do gerador: se o agente devolveu ERRO da conferência (exit 2 do `gerar.py`), o relatório daquele cliente não saiu. Diga qual foi o erro.
- Pendências que o agente devolveu (dado que faltou, campanha fora do modelo, texto em rascunho, página estourada).
- Se algum agente falhou, diga qual e por quê. Não esconda falha atrás de "concluído".

Pedido de ajuste depois ("muda o texto do vídeo", "o tema é Joelho"): edite o JSON que o agente devolveu (na pasta temporária, `python3 relatorio/gerar.py --pasta-saida`) e rode `python3 relatorio/gerar.py <json>` de novo. Não precisa buscar os dados outra vez. Se o JSON já sumiu da pasta temporária, rode o agente de novo.

## Regras que não mudam

- Só leitura. Nenhuma ferramenta do Meta Ads que crie, altere, ative ou apague algo.
- Regra nova do gestor sobre relatórios vai para `memoria/relatorio-meta-ads.md`.
- Decisão nova sobre um cliente (classificação de campanha, tema do vídeo, foto) vai para o `clientes/<slug>.json` dele.
