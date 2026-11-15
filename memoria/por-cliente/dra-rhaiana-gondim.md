# Dra. Rhaiana Gondim

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

## Números de referência (out/2026)
Total R$ 2.460,49 (Topo 776,51 = seguidores 466,93 + vídeo 309,58 · Meio 242,43 · Fundo 1.441,55). Instagram: alcance 392.398, visitas 6.218, cliques na bio 112, 3,1 mil seguidores, R$ 0,15/seguidor. WhatsApp: 72.522 impressões, 39.519 alcance, 265 cliques, 60 conversas, R$ 24,03. Vídeo topo: 15 seg 10.608 (R$ 0,03). Vídeo meio: 15 seg 2.031 (R$ 0,12).

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/dra-rhaiana-gondim.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "classificacao": {
    "120241092304190037": "instagram",
    "120241091977500037": "video_topo",
    "120241092419170037": "video",
    "120241234128330037": "whatsapp"
  },
  "layout": {}
}
```

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Crescimento do Instagram (6 cards) | igual; o custo se chama "Custo por seguidor" e os cliques na bio são a estimativa via anúncio (regra de 15/11/2026) |
| Captação de Leads com Alcance | igual |
| Topo de Funil Video View | igual: página "Vídeo de topo de funil" (azul), mesmos cards e funil |
| Meio de Funil Video View | igual: página "Vídeo de meio de funil" (laranja) |
| Página de Google Ads | **fica de fora**: Google Ads é fase futura do Midas |

- Rótulos do PDF ("Topo (Pessoas novas)", "Meio", "Fundo"): o Midas usa os rótulos padrão, que são parecidos.
- No PDF, vídeo de topo e de meio dividiam a mesma página; no Midas cada um tem a sua (cabe o funil de cada).
- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.
