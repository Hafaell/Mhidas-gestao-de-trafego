---
name: relatorio-cliente
description: Use quando o gestor pedir o relatório de um ou mais clientes da Agência Lupa, em qualquer forma ("faz o relatório do Dr. Fulano", "relatório de outubro da Clínica X", "gera os relatórios da Ana e do Rodrigo", "relatório de todos os clientes"). Cobre relatório mensal de Meta Ads no modelo aprovado, entregue em HTML aberto em localhost (sem arquivo PDF).
---

# Relatório de cliente (Meta Ads)

Esta skill organiza o pedido e usa **três agentes**, cada um com um papel só:

| Agente | Faz | Não faz |
|---|---|---|
| `coletor-dados` | busca os números de um cliente, classifica campanhas, grava e confere o JSON de dados | HTML, visual |
| `montador-relatorio` | junta o JSON com o modelo aprovado (`gerar.py`), confere as páginas | buscar dado, mudar visual |
| `editor-layout` | muda o visual do modelo (pedido do gestor), testa com os exemplos | buscar dado de cliente |

Os três combinam pelo `relatorio/CONTRATO-DADOS.md` (campos do JSON e pedidos de campo novo do layout). O modelo está descrito em `relatorio/modelos/<atual>/MAPA.md`. A sessão principal só prepara, despacha e junta os resultados.

Antes de tudo, leia `memoria/relatorio-meta-ads.md` (regras gerais) e `memoria/STATUS-RELATORIOS.md` (quem dá para gerar). As regras de dados e de visual ficam com os agentes: não precisa ler o contrato nem o mapa.

## Passo 1: entender o pedido

Extraia da mensagem do gestor:

| Item | Regra |
|---|---|
| Clientes | Um ou vários nomes. "Todos" = todos os clientes de `memoria/CLIENTES-ATIVOS.md`. |
| Período | Mês citado ("relatório de outubro"). Sem mês: **mês anterior completo** (dia 1 ao último dia). |
| Período anterior | **Os mesmos dias do mês anterior**, com a mesma quantidade de dias (pediu 09 a 20/11, compara com 09 a 20/10; nunca os dias imediatamente antes). Calcule com `python3 relatorio/gerar.py --periodo-anterior <início> <fim>`, sem fazer a conta de cabeça. Regra completa em `memoria/relatorio-meta-ads.md`. |

## Passo 2: localizar cada cliente

Para cada nome:

1. Confirme que é cliente ativo em `memoria/CLIENTES-ATIVOS.md` (lista geral, sem diferenciar maiúscula nem acento). Não está lá: avise o gestor e pare (pode ser desativado ou cliente novo).
2. **Leia a memória do cliente: `memoria/relatorio-por-cliente/<slug>.md`** (o slug está na coluna "Arquivo" do `CLIENTES-ATIVOS.md`). Ela diz como o relatório dele é montado (seções, títulos, divisões, particularidades) e traz o bloco **"JSON do relatório"**, que é a fonte do cadastro e da configuração. Siga o que ela diz ao despachar os agentes.
3. Não existe outro arquivo de cadastro: o coletor lê o bloco "JSON do relatório" direto da memória do cliente e grava nele a classificação nova e a foto.
4. Sem `ad_account_id` no bloco ou conta nova: chame `ads_get_ad_accounts` (conector Meta Ads, todas as páginas), mostre as contas com nome parecido e pergunte qual é a do cliente. Com a resposta, grave no bloco do `.md`. Cliente sem memória em `memoria/relatorio-por-cliente/`: crie o arquivo a partir de outro cliente, com o formato de `relatorio/exemplos/cliente-config-exemplo.json` (só `nome`, `apelidos`, `ad_account_id`, `descricao` se souber; o coletor completa o resto).
- Conta com `is_queryable: false` ou `is_ads_mcp_enabled: false`: avise o gestor com o motivo e não despache esse cliente.

Mais de 5 clientes de uma vez: confirme a lista com o gestor antes de despachar (regra do CLAUDE.md sobre criar arquivos em massa).

## Passo 3: checagem rápida do ambiente e do token (uma vez por sessão)

```bash
python3 -c "import jinja2" && node -e "require('playwright')"
python3 relatorio/verificar_token.py
```

Se a primeira falhar, pare e avise o gestor do que falta (`pip install jinja2`, `npm install playwright` e `npx playwright install chromium`). Não instale nada sem ele pedir.

O `verificar_token.py` confere o `ACCESS_TOKEN` do Instagram (os cliques na bio dependem dele) e nunca mostra o token. Saída 0: siga. Saída 1 (vence em menos de 7 dias): avise o gestor, mas pode seguir se ele mandar. Saída 2 (vencido ou inválido): **pare e avise**, sem despachar agentes. Saída 3 (não deu para verificar, sem token ou sem rede): avise e pergunte se segue.

## Passo 4: despachar coletores e montadores

**Onda 1, coletores:** faça **todas** as chamadas `Agent` na **mesma mensagem**, uma por cliente, com `subagent_type: "coletor-dados"`. Prompt (só isto):

```
Cliente: <memoria/relatorio-por-cliente/<slug>.md>
Período: <AAAA-MM-DD> a <AAAA-MM-DD>
Período anterior: <AAAA-MM-DD> a <AAAA-MM-DD>
```

**Onda 2, montadores:** quando os coletores voltarem, para cada cliente com Status OK ou OK com pendências, uma chamada `Agent` com `subagent_type: "montador-relatorio"`, todas na **mesma mensagem**. Prompt:

```
Dados: <caminho do JSON que o coletor devolveu>
Real: sim
```

Cliente cujo coletor voltou FALHOU não vai para o montador: entra na tabela final com o motivo.

## Passo 5: juntar e entregar

Quando todos voltarem, responda ao gestor com uma tabela curta:

| Cliente | Status | Ver relatório | Pendências |
|---|---|---|---|

- **Entrega só em HTML, sem PDF** (regra do gestor, 14/11/2026). Não liste nem mande arquivo PDF: o gestor baixa pelo botão "Baixar PDF" da própria página.
- **Ver relatório** é obrigatório: para cada cliente, suba o servidor local em segundo plano e mande o link `http://localhost:<porta>`:
  `python3 relatorio/servir.py <nome-sem-extensão> --porta <porta>` (rode com `run_in_background`; sem `--sem-abrir`, para abrir a página no navegador do gestor, regra de 15/11/2026). Uma porta por cliente, começando em 8000. Antes de subir, veja se a porta já tem servidor (`netstat -ano | grep ":<porta> .*LISTENING"`); se tiver, feche o processo (`Stop-Process -Id <pid>`, autorizado pelo gestor em 15/11/2026) e sirva o HTML novo nela. Deixe o servidor no ar por pelo menos 1 hora. Antes de mandar o link, confirme que respondeu 200 com `curl -s -o /dev/null -w "%{http_code}" http://localhost:<porta>` (não use `curl -I`: o servidor não aceita HEAD e responde 501).
- Conferência do gerador: se o agente devolveu ERRO da conferência (exit 2 do `gerar.py`), o relatório daquele cliente não saiu. Diga qual foi o erro.
- Pendências que os agentes devolveram (dado que faltou, campanha fora do modelo, página estourada), dizendo de qual agente veio cada uma.
- Se algum agente falhou, diga qual e por quê. Não esconda falha atrás de "concluído".

Pedido de ajuste depois:
- **De dado do cliente** ("o tema é Joelho", "essa campanha é de WhatsApp"): edite o JSON que o coletor devolveu (pasta temporária, `python3 relatorio/gerar.py --pasta-saida`) e rode o `montador-relatorio` de novo com ele. Não precisa buscar os dados outra vez. Se o JSON sumiu, rode o coletor de novo.
- **De visual** ("muda a cor do card", "tira esse gráfico", "coloca o custo por clique"): despache o `editor-layout` com o pedido do gestor nas palavras dele. Ele devolve uma prévia: sirva cada exemplo da prévia com `python3 relatorio/servir.py <nome> --pasta <pasta que o editor devolveu> --porta <porta>` (uma porta por exemplo; sem `--sem-abrir`, para abrir no navegador do gestor, e com as mesmas regras de porta do Passo 5) e mande o link. Com o "aprovado" do gestor, continue o mesmo editor (`SendMessage`) com "aprovado" para ele aplicar no modelo. Depois, se havia relatórios de clientes abertos, rode o montador de novo para cada um (os dados não mudam).
- Se o editor devolver PRECISA DE DADO NOVO, avise o gestor: o campo entra no próximo relatório, quando o coletor atender o pedido no contrato.
- Pendência de layout que o montador devolver (página estourou, card vazio por falta de espaço) também vai para o `editor-layout`.

## Regras que não mudam

- Só leitura. Nenhuma ferramenta do Meta Ads que crie, altere, ative ou apague algo.
- Regra nova do gestor vai para o arquivo do assunto: dados em `relatorio/CONTRATO-DADOS.md`, visual no `MAPA.md` do modelo, entrega aqui, regra geral em `memoria/relatorio-meta-ads.md`.
- Decisão nova sobre um cliente (classificação de campanha, tema do vídeo, foto) vai para a memória dele (`memoria/relatorio-por-cliente/<slug>.md`: o bloco JSON se for configuração, o texto se for regra de montagem). O coletor grava a classificação nova e a foto no bloco JSON do `.md`.
