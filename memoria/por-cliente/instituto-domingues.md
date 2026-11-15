# Instituto Domingues (estética do Dr. Rodrigo Domingues)

Fonte: `[Estetica_Rodrigo_Domingues]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Instituto domingues". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta. Prioridade 2.
- Instagram: @instituto.domingues
- Conta de anúncio: 880566547457944 ("CA2- DR RODRIGO DOMINGUES ESTÉTICA", BM "BM Douglas - Anunciante"), conector ok. A conta antiga "CA - Dr Rodrigo Domingues - Estetica" (224025513067237) está desativada pela Meta.
- No PDF antigo o cliente aparece como **"Estética Rodrigo Domingues"**. É um cliente diferente do Dr. Rodrigo Domingues (ortopedia, `dr-rodrigo-domingues.md`).
- Negócio: estética. As campanhas giram em torno do tema **"M.E.L.A"** (escrito "Mela" nos títulos do relatório).

## Tipo de campanha
Instagram + vídeo de topo + vídeo de meio + WhatsApp, todos do tema M.E.L.A.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120217786722210553 | [TOPO][TRF] Novos Seguidores | Crescimento do Instagram |
| 120217792613920553 | [TOPO][VV] CP1 Div - M.E.L.A | Topo de Funil Video View (Mela) |
| 120217797112750553 | [MEIO][VV] CP2 Div - M.E.L.A | Meio de Funil Video View (Mela) |
| 120221899200830553 | [FUNDO] [MSG] CP3 Div - Agendamento M.E.L.A | Captação de Leads MELA |

Em 15/11/2026 as quatro estavam **pausadas**, mas gastaram em out/2026.

## Estrutura do relatório antigo
- Rótulos do cabeçalho: **"Topo (Pessoas novas)", "Meio (Pessoas engajadas)", "Fundo (Foco em consulta)"**.
1. Investimento + Crescimento do Instagram (custo chamado "Valor investido/Seguidores") + "Campanhas de Captação de Leads MELA" **com Alcance** (Valor Investido, Impressões, Alcance, Cliques, Conversas Iniciadas, Investido/Conversa).
2. Investimento + "Topo de Funil Video View (Mela)" + "Meio de Funil Video View (Mela)" (cards padrão).

Sem página de Google Ads.

## Números de referência (out/2026)
Total R$ 1.013,57 (Topo 559,98 = seguidores 377,44 + vídeo 182,54 · Meio 151,23 · Fundo 302,36), cerca de 51% a menos que o mês anterior. Instagram: alcance 67.692, visitas 1.789, cliques na bio 50, 174 seguidores, R$ 2,16/seguidor. WhatsApp: 6.980 impressões, 3.668 alcance, 41 cliques, 10 conversas, R$ 30,24. Vídeo topo: 15 seg 2.568. Vídeo meio: 15 seg 1.601.

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/instituto-domingues.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "classificacao": {
    "120217786722210553": "instagram",
    "120217792613920553": "video_topo",
    "120217797112750553": "video",
    "120221899200830553": "whatsapp"
  },
  "layout": {
    "rotulos_etapa": {
      "meio": "Pessoas engajadas"
    },
    "temas": {
      "video_topo": "Mela",
      "video": "Mela",
      "whatsapp": "MELA"
    }
  }
}
```

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Rótulos "Topo (Pessoas novas)", "Meio (Pessoas engajadas)", "Fundo (Foco em consulta)" | igual (`rotulos_etapa`) |
| Crescimento do Instagram (6 cards) | igual; o custo se chama "Custo por seguidor" e os cliques na bio são a estimativa via anúncio (regra de 15/11/2026) |
| Campanhas de Captação de Leads MELA (com Alcance) | igual: "Captação de leads no WhatsApp · MELA" |
| Topo e Meio de Funil Video View (Mela) | igual: "Vídeo de topo de funil · Mela" e "Vídeo de meio de funil · Mela" |

- As campanhas estavam pausadas em 15/11/2026: mês sem gasto não gera seção.
- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.
