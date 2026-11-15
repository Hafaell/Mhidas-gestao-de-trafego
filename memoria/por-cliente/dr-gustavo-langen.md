# Dr. Gustavo Langen

Fonte: `[Dr_Gustavo_Langen]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Dr. Gustavo Langen". Tags: Planilha Div, Caixinhas de Pergunta, Seguidores.
- Instagram: @drgustavolangen
- Conta de anúncio: 507254411405150 ("CA - Dr Gustavo Langen"), conector ok. O conector mostra outras contas com o nome dele (355693226314239, 4574248379318426 e "CA - CURSO MÉDICOS" 2028634627690820), mas elas não são as do relatório.
- Negócio: ortopedia regenerativa e ombro, atendendo em **São Paulo e Campinas**.

## Tipo de campanha
Instagram + vídeo de topo + vídeo de meio + WhatsApp **dividido por cidade**.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120240476892160202 | [TOPO][TRF] Novos Seguidores | Crescimento do Instagram |
| 120232722534820202 | [TOPO][VV] CP1 Div \| Regenerativa | Topo de Funil Video View |
| 120232722815360202 | [MEIO][VV] CP2 Div \| Regenerativa | Meio de Funil Video View (somada) |
| 120243742951030202 | [MEIO][VV] CP2 Div \| Caixinhas | Meio de Funil Video View (somada) |
| 120236939086340202 | [FUNDO][MSG][SP] Post do Instagram: Dores nos ombros... | WhatsApp **São Paulo** |
| 120233085498560202 | [FUNDO][MSG][SP] CP3 Div \| Agendamento Regenerativa | WhatsApp **São Paulo** |
| 120236939041520202 | [FUNDO][MSG][CAMPINAS] Post do Instagram: Dores nos ombros... | WhatsApp **Campinas** |

A cidade está no nome da campanha (`[SP]`, `[CAMPINAS]`).

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Meio, Fundo) + Crescimento do Instagram (custo chamado "Custo/Seguidores") + Captação de Leads em **dois blocos**: "Valor Investido São Paulo" e "Valor Investido Campinas", cada um com Impressões, Cliques, Conversas Iniciadas e Investido/Conversa.
2. Investimento + Topo de Funil Video View + Meio de Funil Video View (cards padrão).

Sem página de Google Ads.

## Números de referência (out/2026)
Total R$ 5.567,41 (Topo 2.640,69 = seguidores 1.397,83 + vídeo 1.242,86 · Meio 930,34 · Fundo 1.996,38).
- Instagram: alcance 211.882, visitas 3.532, cliques na bio 122, 1 mil seguidores, R$ 1,39/seguidor.
- WhatsApp São Paulo: R$ 1.391,32, 60.657 impressões, 417 cliques, 176 conversas, R$ 7,91.
- WhatsApp Campinas: R$ 605,06, 38.030 impressões, 152 cliques, 50 conversas, R$ 12,10.
- Vídeo topo: 15 seg 19.784 (R$ 0,06). Vídeo meio: 15 seg 11.870 (R$ 0,17 no PDF).

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/dr-gustavo-langen.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "classificacao": {
    "120240476892160202": "instagram",
    "120232722534820202": "video_topo",
    "120232722815360202": "video",
    "120243742951030202": "video",
    "120236939086340202": "whatsapp:São Paulo",
    "120233085498560202": "whatsapp:São Paulo",
    "120236939041520202": "whatsapp:Campinas"
  },
  "layout": {
    "blocos_whatsapp": {
      "[SP]": "São Paulo",
      "[CAMPINAS]": "Campinas"
    }
  }
}
```

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Crescimento do Instagram (6 cards) | igual; o custo se chama "Custo por seguidor" e os cliques na bio são a estimativa via anúncio (regra de 15/11/2026) |
| Captação de Leads em 2 blocos (São Paulo e Campinas) | igual: dois blocos "Leads no WhatsApp · São Paulo" e "· Campinas" (lista `whatsapp` com `bloco`) |
| Topo de Funil Video View | igual: página "Vídeo de topo de funil" (azul), mesmos cards e funil |
| Meio de Funil Video View (2 campanhas somadas) | igual (somadas) |

- Instagram + 2 blocos de WhatsApp = 3 blocos: página 1 com cards compactos.
- No PDF, vídeo de topo e de meio dividiam a mesma página; no Midas cada um tem a sua (cabe o funil de cada).
- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.
