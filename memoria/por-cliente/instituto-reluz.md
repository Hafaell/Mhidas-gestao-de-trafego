# Instituto Reluz (Reluz Materno Infantil)

Fonte: `[Instituto_Reluz]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "reluz.maternoinfantil". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta.
- Instagram: @reluz.maternoinfantil
- Conta de anúncio: 1003900615567848 ("CA2 Instituto Reluz"), conector ok. A "CA Instituto Reluz" (834248182578817) está desativada pela Meta, e a "CA - Reluz" (761249612788224) não é a do relatório.
- Negócio: fonoaudiologia infantil, Brasília (termos do Google).

## Tipo de campanha
Vídeo de topo + WhatsApp. **Sem campanha de seguidores (não tem seção de Instagram) e sem vídeo de meio.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120249925448730275 | [TOPO][VV] CP1 Div | Topo de Funil Video View |
| 120249924944830275 | [FUNDO][MSG] Agendamento | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Fundo) + Captação de Leads (Valor Investido, Impressões, Cliques, Conversas Iniciadas, Investido/Conversa).
2. Investimento + Topo de Funil Video View (cards padrão).
3. Google Ads (Search; termos: fono infantil, fono infantil Brasília, fonoaudiólogo infantil).

## Números de referência (out/2026)
Total R$ 908,94 (Topo vídeo 305,11 · Fundo 603,83). WhatsApp: 80.947 impressões, 231 cliques, 25 conversas, R$ 24,15. Vídeo topo: 15 seg 6.341, 50% 17.056, 75% 9.990, 95% 6.578. Nesse vídeo curto o 50% passa do 15 seg, o que é normal.

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/instituto-reluz.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/montador-relatorio.md`, Passo 1b.

```json
{
  "classificacao": {
    "120249925448730275": "video_topo",
    "120249924944830275": "whatsapp"
  },
  "layout": {}
}
```

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Captação de Leads (WhatsApp) | igual, com o card Alcance a mais |
| Topo de Funil Video View | igual: página "Vídeo de topo de funil" (azul), mesmos cards e funil |
| Página de Google Ads | **fica de fora**: Google Ads é fase futura do Midas |

- Sem Instagram e sem vídeo de meio: página 1 só com WhatsApp, página 2 com o vídeo de topo.
- Vídeo curto: o 50% passa do 15 seg; o funil mantém a forma (é normal).
- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.
