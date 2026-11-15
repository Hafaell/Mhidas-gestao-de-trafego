# Dr. Carlos Alexandre

Fonte: `[Dr_Carlos_Alexandre]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Carlos Alexandre". Sem tags.
- Instagram: @carlosazevedo.mao
- Conta de anúncio: 684865741344979 ("CA - Dr Carlos Alexandre"), conector ok.
- Negócio: cirurgião da mão / ortopedista especialista em mão (termos do Google).

## Tipo de campanha
Vídeo de topo + vídeo de meio + WhatsApp. **Sem campanha de seguidores: não tem seção de Instagram.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120240312004210183 | [TOPO][VV] CP1 Div | Topo de Funil Video View |
| 120240312322170183 | [MEIO][VV] CP2 Div | Meio de Funil Video View |
| 120236279940120183 | [FUNDO][MSG] Agendamento | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Fundo) + Captação de Leads **com Alcance**: Valor Investido, Impressões, Alcance, Cliques, Conversas Iniciadas, Investido/Conversa.
2. Investimento (Total, Topo, Meio, Fundo) + "Topo de Funil Video" + "Meio de Funil Video" (cards padrão de vídeo).
3. Google Ads (Search de leads; termos: cirurgião da mão, ortopedista especialista em mãos).

## Números de referência (out/2026)
Meta R$ 1.233,67 (Topo vídeo 436,61 · Meio vídeo 187,06 · WhatsApp 610,00). WhatsApp: 47.906 impressões, 19.299 alcance, 249 cliques, 46 conversas, R$ 13,26/conversa. Topo vídeo: 15 seg 8.999 (R$ 0,05). Meio vídeo: 15 seg 5.939 (R$ 0,03).

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/dr-carlos-alexandre.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "classificacao": {
    "120240312004210183": "video_topo",
    "120240312322170183": "video",
    "120236279940120183": "whatsapp"
  },
  "layout": {}
}
```

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Captação de Leads com Alcance | igual |
| Topo de Funil Video View | igual: página "Vídeo de topo de funil" (azul), mesmos cards e funil |
| Meio de Funil Video View | igual: página "Vídeo de meio de funil" (laranja) |
| Página de Google Ads | **fica de fora**: Google Ads é fase futura do Midas |

- Sem Instagram: a página 1 tem só o WhatsApp (o bloco estica até o rodapé).
- No PDF, vídeo de topo e de meio dividiam a mesma página; no Midas cada um tem a sua (cabe o funil de cada).
- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.
