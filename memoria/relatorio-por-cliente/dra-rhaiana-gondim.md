# Dra. Rhaiana Gondim

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Dra_Rhaiana_Gondim]_Relatórios_FB_3.0 (2).pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "drarhaianagondim". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta.
- Instagram: @drarhaianagondim
- Conta de anúncio: 1384213717075897 ("CA Dra Rhaiana Gondim"), conector ok.
- Negócio: urologia pediátrica (termos do Google: urologista pediatra, uropediatria, fimose infantil).

## Tipo de campanha
Estrutura padrão completa: Instagram + vídeo de topo + vídeo de meio + WhatsApp.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120241092304190037 | [TOPO][TRF] Novos Seguidores | Crescimento do Instagram |
| 120241091977500037 | [TOPO][VV] CP1 Div | Topo de Funil Video View |
| 120241092419170037 | [MEIO][VV] CP2 Div | Meio de Funil Video View |
| 120241234128330037 | [FUNDO][MSG] Agendamento | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
- Rótulos do cabeçalho: **"Topo (Pessoas novas)", "Meio", "Fundo"**.
1. Investimento + Crescimento do Instagram (custo chamado "Investido/Seguidores") + Captação de Leads **com Alcance** (Valor Investido, Impressões, Alcance, Cliques, Conversas iniciadas, Investido/Conversa).
2. Investimento + Topo de Funil Video View + Meio de Funil Video View (cards padrão).
3. Google Ads (Search de leads; termos: urologista pediatra, uropediatria, urologista infantil, fimose infantil).

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dra. Rhaiana Gondim",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "1384213717075897",
  "instagram": "@drarhaianagondim",
  "foto": null,
  "tema_video": null,
  "classificacao": {
    "120241092304190037": "instagram",
    "120241091977500037": "video_topo",
    "120241092419170037": "video",
    "120241234128330037": "whatsapp"
  },
  "layout": {}
}
```
