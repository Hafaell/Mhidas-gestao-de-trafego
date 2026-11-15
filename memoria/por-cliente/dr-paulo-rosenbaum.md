# Dr. Paulo Cesar Rosenbaum

Fonte: `[Dr._Paulo_Rosenbaum]_Relatórios_FB_3.0.pdf` (**período 01 a 22/10/2026**, não o mês inteiro) e campanhas lidas no Meta Ads em 15/11/2026 (out/2026 completo).

## Identificação
- Notion: "Paulo Cesar Rosenbaum". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta.
- Instagram: @drpaulocesar.rosenbaum
- Conta de anúncio: 725094333687912 ("CA - Dr Paulo Rosenbaum", BM "Dra Flavia e Paulo"), conector ok. Existe outra conta "DR PAULO ROSENBAUM" (1043855171176781), não conferida; os números do PDF batem com a 725094333687912 [Provável].
- Negócio: tratamento da dor, em Mato Grosso do Sul: Campo Grande (Google), **Nova Andradina** e **Ivinhema** (Meta).

## Tipo de campanha
Instagram (duas campanhas de seguidores) + vídeo de topo + WhatsApp **dividido em três** (tema e cidades). **Sem vídeo de meio.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120230805172670041 | [TOPO][TRF] CP1 Div \| Novos Seguidores | Crescimento do Instagram (somada) |
| 120241749296960041 | [TOPO][TRF] CP1 Div \| Novos Seguidores Nova Andradina | Crescimento do Instagram (somada) |
| 120230805904160041 | [TOPO][VV] CP1 Div | Topo de Funil Video View |
| 120230806021980041 | [FUNDO][MSG] CP3 Div \| Dor | Captação de Leads **Dor** |
| 120241749382950041 | [FUNDO][MSG] Agendamento Nova Andradina | Captação de Leads **Nova Andradina** |
| 120249017766140041 | [FUNDO][MSG] Agendamento Ivinhema | Captação de Leads **Ivinhema** |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Fundo) + Crescimento do Instagram (custo chamado "Custo/seguidores") + **três blocos de Captação de Leads**: "Dor", "Nova Andradina" e "Ivinhema", cada um com Valor Investido, Impressões, Cliques, Conversas Iniciadas e Investido/Conversa.
2. Investimento + Topo de Funil Video View (cards padrão).
3. Google Ads (Search; termos: clínica especializada em dor, médico especialista em dor, clínica da dor em Campo Grande).

## Números de referência (01 a 22/10/2026, do PDF)
Total R$ 2.233,89 (Topo 797,52 = seguidores 588,39 + vídeo 209,13 · Fundo 1.436,37).
- Instagram: alcance 142.925, visitas 1,7 mil, cliques na bio 1,4 mil, 372 seguidores, R$ 1,82/seguidor.
- Dor: R$ 581,78, 44 conversas, R$ 13,22. Nova Andradina: R$ 585,93, 28 conversas, R$ 20,93. Ivinhema: R$ 268,66, 30 conversas, R$ 8,96.
- Vídeo topo: 15 seg 3.186 (R$ 0,07).

Gasto no mês inteiro de out/2026 (conector): seguidores 464,79 + 401,53; vídeo 309,30; Dor 853,88; Nova Andradina 849,33; Ivinhema 392,64.

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/dr-paulo-rosenbaum.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "classificacao": {
    "120230805172670041": "instagram",
    "120241749296960041": "instagram",
    "120230805904160041": "video_topo",
    "120230806021980041": "whatsapp:Dor",
    "120241749382950041": "whatsapp:Nova Andradina",
    "120249017766140041": "whatsapp:Ivinhema"
  },
  "layout": {
    "blocos_whatsapp": {
      "| Dor": "Dor",
      "Nova Andradina": "Nova Andradina",
      "Ivinhema": "Ivinhema"
    }
  }
}
```

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Crescimento do Instagram (2 campanhas somadas) | igual (somadas; alcance somado de 2 campanhas vira pendência) |
| 3 blocos de Captação de Leads: Dor, Nova Andradina, Ivinhema | igual: três blocos "Leads no WhatsApp · <bloco>" |
| Topo de Funil Video View | igual: página "Vídeo de topo de funil" (azul), mesmos cards e funil |
| Página de Google Ads | **fica de fora**: Google Ads é fase futura do Midas |

- Instagram + 3 blocos de WhatsApp = 4 blocos: viram 2 páginas de 2 blocos (testado, cabe).
- Sem vídeo de meio: o investimento mostra só Topo e Fundo, como no PDF.
- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.
