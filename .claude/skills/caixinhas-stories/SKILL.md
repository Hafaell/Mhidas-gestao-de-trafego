---
name: caixinhas-stories
description: Use quando o gestor pedir para ver, checar ou baixar as caixinhas de pergunta dos stories de um ou mais clientes ou de qualquer perfil do Instagram ("baixa as caixinhas do @fulano", "o Dr. X tem caixinha de pergunta hoje?", "puxa os stories da Clínica Y", "caixinhas do Gustavo Samico", "tem caixinha hoje?", "caixinhas de todos os clientes"). Recebe o nome do cliente ou o @ do Instagram; despacha um agente coletor-caixinhas por cliente, em paralelo.
---

# Caixinhas de pergunta dos stories

Esta skill é a **despachante**. Ela descobre o @ de cada cliente, chama um agente **`coletor-caixinhas` por cliente, todos ao mesmo tempo**, e junta as respostas numa tabela. Quem olha o Instagram e baixa é o agente (`.claude/agents/coletor-caixinhas.md`): ele vê os stories no Chrome logado do gestor, identifica a caixinha por print e **só se houver caixinha** baixa o story pelo Spector para `Downloads\<usuario>\`.

O gestor chamar a skill com um nome já autoriza baixar as caixinhas desse perfil. Story sem caixinha nunca é baixado.

**Aviso (diga na primeira vez da sessão):** para ver o story, o agente clica em "Ver story" e a conta do gestor aparece na lista de quem viu o story do cliente. Em vários clientes, isso se repete em todos.

## Passo 1: descobrir o @ de cada cliente

| O gestor passou | @ do Instagram |
|---|---|
| @, link ou usuário (`@gustavosamico.oftalmo`, `instagram.com/gustavosamico.oftalmo`) | Limpe: tire `@`, `https://`, `www.instagram.com/`, `/stories/`, barras e `?...` |
| Só o nome ("Gustavo Samico") | Coluna Instagram da linha de `memoria/CLIENTES-ATIVOS.md` cujo nome bate (sem diferenciar maiúscula nem acento) |
| Só o nome, e não está em `memoria/CLIENTES-ATIVOS.md` | **Pergunte o @ ao gestor.** Não adivinhe o perfil. |

Lista de clientes:
- Nomes ou @ citados: só esses.
- "Todos os clientes ativos": os 22 de `memoria/CLIENTES-ATIVOS.md`.
- Sem nome nenhum ("tem caixinha hoje?"): pergunte se são os 22 ou só os 15 com a tag Cx.
- Mais de 5 clientes: confirme a lista com o gestor antes (regra do CLAUDE.md sobre ações em massa).

**Pré-checagem (uma vez por sessão, antes de despachar):** `tabs_context_mcp` com `createIfEmpty: true` para ver se a extensão Claude in Chrome está conectada. Se falhar, pare e avise o gestor (extensão desconectada ou Chrome fechado). Não despache agentes assim.

## Passo 2: despachar os agentes em paralelo

Faça **todas** as chamadas `Agent` na **mesma mensagem**, uma por cliente, com `subagent_type: "coletor-caixinhas"`. Prompt (só isto):

```
Usuário: <@ sem o @>
Cliente: <nome>
```

**Lotes de até 5 clientes ao mesmo tempo.** Cada agente abre uma aba própria no Chrome e todos dividem a mesma conta do Instagram; muitas abas juntas podem travar o Chrome ou fazer o Instagram limitar a conta [Adivinhando: o limite de 5 é prudência, ainda não foi testado]. Com mais de 5 clientes, despache um lote, espere as respostas e despache o próximo. O gestor pode pedir outro tamanho de lote.

Os agentes se organizam sozinhos para não baixar um arquivo do outro (fila de download em `trava-download.ps1`); você não precisa fazer nada.

## Passo 3: juntar as respostas

Cada agente devolve: cliente, status, stories ativos, caixinhas (posição, foto/vídeo, aberta/resposta, texto), caminho dos arquivos, dúvidas e pendências. Entregue ao gestor:

- Uma tabela com **cliente, stories ativos, caixinhas e onde ficaram os arquivos**. Cliente sem caixinha: "nenhuma caixinha nos N stories".
- Abaixo, os clientes com erro, "não conferido" ou "dúvida", e o motivo (por exemplo, Instagram deslogado).
- Para cada caixinha: o texto da pergunta e o caminho completo (`C:\Users\Rafael\Downloads\<usuario>\...`).
- Se **algum agente falhou**, ofereça refazer só aquele cliente.

Não repita o relatório de cada agente na íntegra: a tabela e as exceções bastam.

## Se o Instagram estiver deslogado

O agente para e devolve `FALHOU (Instagram deslogado)`. Avise o gestor para entrar no Instagram no Chrome (a skill nunca digita senha) e refaça só os clientes que falharam.

## Arquivos desta skill

| Arquivo | Para quê |
|---|---|
| `.claude/agents/coletor-caixinhas.md` | O agente de um cliente: ver stories, identificar a caixinha, baixar pelo Spector |
| `mover-stories.ps1` | Move o que baixou de `Downloads` para `Downloads\<usuario>\` |
| `trava-download.ps1` | Fila de download entre agentes paralelos (`pegar` / `soltar`) |

## Histórico do método

O SnapInsta (usado antes) passou a responder "Esse vídeo é privado" mesmo para perfis públicos em 17/11/2026, por isso o método atual usa o Instagram logado do gestor para ver os stories e o Spector para baixar. O Fast Save deixou de ser usado (ele só abria o Spector).

Teste de 17/11/2026 com @drraphaelkondo (2 stories, nenhuma caixinha): o Instagram logado abriu os stories, o print identificou que não havia caixinha, e o link direto do Spector abriu com o campo preenchido e listou os 2 cartões (em ordem diferente da do Instagram). Download de foto pelo Spector funcionou no teste anterior (via Fast Save, mesma página).

Em 17/11/2026 a skill foi dividida em skill (despachante) + agente `coletor-caixinhas`, para rodar vários clientes ao mesmo tempo.

**Ainda não testado:**
- Vários agentes ao mesmo tempo (abas em paralelo no mesmo Chrome; abas em segundo plano podem dar print em branco: o agente trata isso como "não conferido", não como "sem caixinha").
- Clicar em Baixar depois de abrir o link direto do Spector, e baixar **vídeo** pelo Spector.
- A fila de download com dois agentes de verdade (o script foi testado sozinho: pegar, esperar e soltar funcionam).
- O agente novo só aparece depois de reiniciar a sessão do Claude Code (ou recarregar os agentes).
