---
name: caixinhas-stories
description: Use quando o gestor pedir para ver, checar ou baixar as caixinhas de pergunta dos stories de um cliente ou de qualquer perfil do Instagram ("baixa as caixinhas do @fulano", "o Dr. X tem caixinha de pergunta hoje?", "puxa os stories da Clínica Y", "caixinhas do Gustavo Samico"). Recebe o nome do cliente ou o @ do Instagram.
---

# Caixinhas de pergunta dos stories

Esta skill olha os stories ativos de um perfil público do Instagram pelo site SnapInsta, no Chrome (extensão Claude in Chrome). Ela baixa **só os stories com caixinha de pergunta** para `Área de Trabalho\Stories\<Nome do cliente>\`.

O gestor chamar a skill com um nome já autoriza baixar as caixinhas desse perfil. Stories sem caixinha não são baixados.

## Passo 1: descobrir o @ e o nome da pasta

| O gestor passou | @ do Instagram | Nome da pasta |
|---|---|---|
| @, link ou usuário (`@gustavosamico.oftalmo`, `instagram.com/gustavosamico.oftalmo`) | Limpe: tire `@`, `https://`, `www.instagram.com/`, `/stories/`, barras e `?...` | Nome que o gestor escreveu junto, se escreveu. Senão, o campo `nome` do `clientes/*.json` com o mesmo `instagram`. Senão, o próprio usuário (`gustavosamico.oftalmo`). |
| Só o nome ("Gustavo Samico") | Campo `instagram` do `clientes/*.json` que bate com `nome` ou `apelidos` (sem diferenciar maiúscula nem acento) | O nome que o gestor escreveu |
| Só o nome, e não existe no `clientes/` | **Pergunte o @ ao gestor.** Não adivinhe o perfil. | O nome que o gestor escreveu |

Mais de um cliente: faça um por vez, na mesma aba. "Todos os clientes": confirme a lista com o gestor antes (regra do CLAUDE.md sobre criar arquivos em massa).

## Passo 2: abrir os stories no SnapInsta

1. Carregue os tools do Chrome numa única chamada ToolSearch: `tabs_context_mcp`, `tabs_create_mcp`, `tabs_close_mcp`, `navigate`, `computer`, `find`, `browser_batch`, `javascript_tool`.
2. `tabs_context_mcp` com `createIfEmpty: true`. Use a aba vazia do grupo ou crie uma.
3. Abra `https://snapinsta.to/pt57/instagram-story-downloader`.
4. `find` "campo Colar URL Instagram", clique nele e digite **`https://www.instagram.com/stories/<usuario>/`**. Depois Enter e espere ~7 s.
   - **Tem que ser o link `/stories/`.** O link do perfil (`instagram.com/<usuario>/`) traz as publicações do feed, não os stories.
5. Um **pop-up em branco** com o botão "Fechar" aparece sempre. Feche com `find` "botão Fechar" e clique pelo `ref`. Se aparecer de novo depois, feche de novo.
6. Role para o topo e tire um screenshot.

**Como ler o resultado:**

| O que aparece | Significa |
|---|---|
| Cartões em pé (resolução tipo `1179x2096`), botões "Baixar foto" ou "Baixar vídeo" | São os stories ativos. Siga. |
| Primeiro cartão "Baixar Avatar" e fotos `1080x1350` | Veio o feed: o link digitado não foi o `/stories/`. Refaça o passo 4. |
| Mensagem de erro, nada listado | Perfil privado, sem story nas últimas 24h, ou o site falhou. Tente mais uma vez. Se repetir, informe ao gestor e pare. |

## Passo 3: achar as caixinhas

**A prévia padrão corta o story em cima e embaixo**, e os botões cobrem a parte de baixo. Uma caixinha nessas áreas passa despercebida. Antes de olhar, mostre o story inteiro com `javascript_tool`:

```js
const s=document.createElement('style'); s.id='midas-preview';
s.textContent='.download-items,.download-items__thumb{height:auto!important;max-height:none!important}.download-items__thumb img{object-fit:contain!important;width:100%!important;height:auto!important;max-height:none!important}.download-items>:not(.download-items__thumb){display:none!important}';
document.head.appendChild(s); window.scrollTo(0,0); document.querySelectorAll('.download-items__thumb img').length
```

O retorno é o número de stories. Tire um screenshot e dê `zoom` em **cada cartão**, rolando se houver mais de uma linha. Antes de clicar em "Baixar" (passo 4), devolva os botões com `document.getElementById('midas-preview').remove()`.

A caixinha de pergunta é o sticker do Instagram com este formato:

| Sticker | Como reconhecer | Baixa? |
|---|---|---|
| **Caixinha de pergunta aberta** | Cartão arredondado. Foto de perfil redonda em cima, saindo da borda. Faixa colorida com a pergunta ("Faça uma pergunta", "Me pergunte...", ou texto do cliente). Campo claro embaixo ("Escreva algo...", "Toque para responder"). | **Sim** |
| **Resposta de caixinha** | O cartão traz a pergunta de um seguidor (texto dentro de uma caixa, às vezes com "@usuário"). Fica por cima de um vídeo ou foto do cliente respondendo. Não tem campo para escrever. | **Sim** (avise no resumo que é resposta) |
| Enquete | 2 opções lado a lado ("SIM / NÃO") ou barras com porcentagem | Não |
| Enquete de várias opções ou quiz | Faixa de título e uma lista de 3-4 opções empilhadas | Não |
| Barra de emoji, link, menção @, música, contagem regressiva | Outros stickers | Não |

Cartão de **vídeo**: a prévia é um quadro do vídeo, e o sticker costuma aparecer nela. Se ficar em dúvida mesmo com zoom, baixe e mova com `-Raiz` apontando para a pasta temporária (passo 4). Se o `ffmpeg` existir, extraia um quadro para olhar. Só mova para a Área de Trabalho o que tiver caixinha confirmada. Se não der para confirmar, liste o story como "dúvida" no resumo.

Anote, para cada caixinha, a posição do cartão (1º, 2º...) e o texto da pergunta.

**Nenhuma caixinha:** não baixe nada e não crie pasta. Vá para o passo 5.

## Passo 4: baixar e mover para a pasta do cliente

1. Anote o horário **antes** de clicar:
   ```powershell
   Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
   ```
2. Use `find` "botões Baixar foto e Baixar vídeo". Eles vêm na mesma ordem dos cartões. Clique pelo `ref` só nos cartões com caixinha, deixando a resolução padrão (a maior). O Chrome salva em `Downloads` como `SnapInsta.to_<id>_n.jpg` ou `.mp4`.
3. Rode o script, com `-Esperados` = número de cliques:
   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .claude/skills/caixinhas-stories/mover-stories.ps1 -Cliente "<Nome da pasta>" -Desde "<horário do item 1>" -Esperados <N>
   ```
   O script espera os downloads terminarem e cria `Desktop\Stories` e `Desktop\Stories\<Nome>` se não existirem. Depois move os arquivos com o nome `AAAA-MM-DD_<id>_n.jpg`. Se o story já foi baixado antes (mesmo id), ele não duplica e apaga a cópia nova de Downloads.
   - Saída `SALVO <caminho>`: ok.
   - Saída `JA_EXISTIA <caminho>`: já estava na pasta, sem problema.
   - Saída `NENHUM_ARQUIVO`: o clique não baixou. Veja no screenshot se o Chrome abriu uma janela "Salvar como" ou um aviso "este site quer baixar vários arquivos". **Não clique nesses avisos.** Peça ao gestor para aceitar ou para desligar "Perguntar onde salvar" no Chrome, e tente de novo.
4. Abra cada arquivo salvo com Read e confirme que a caixinha aparece na imagem.

## Passo 5: fechar e responder

Feche a aba com `tabs_close_mcp`. Responda ao gestor:

- Perfil e quantidade de stories ativos.
- Caixinhas encontradas: posição, tipo (aberta ou resposta) e texto da pergunta.
- Caminho completo de cada arquivo salvo (`C:\Users\Rafael\Desktop\Stories\<Nome>\...`).
- Stories em "dúvida", se houver.
- Se não havia caixinha: "nenhuma caixinha nos N stories ativos de @usuario", sem pasta criada.

## Erros comuns

| Erro | Correção |
|---|---|
| Colar o link do perfil | Sempre `instagram.com/stories/<usuario>/` |
| Julgar pela prévia cortada | Sempre aplique o CSS `midas-preview` do passo 3 antes de olhar |
| Clicar num cartão escondido pelo pop-up | Feche o pop-up e clique pelo `ref` do `find`, não por coordenada |
| Baixar todos os stories "para garantir" | Só caixinhas. O resto fica só na tela. |
| Tentar ler a URL dos botões "Baixar" por JavaScript | A extensão bloqueia (o link tem token). Clique no botão. |
| Criar a pasta do cliente sem caixinha | A pasta só nasce quando o script move um arquivo |
