# Dra. Patrícia Canelas

Fonte: `[Patricia_Canela]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Patrícia Canelas". Tags: Planilha Div, Caixinhas de Pergunta.
- Instagram: @patricia.urologista
- Conta de anúncio: 352376624307091 ("CA1 - Dra Patricia Canelas [CRM]"), conector ok.
- Negócio: urologia feminina (infecção urinária, incontinência, dor pélvica, exame urodinâmico, pelos termos do Google).

## Tipo de campanha
Instagram + vídeo de topo + vídeo de meio + WhatsApp.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120233309208820345 | [TOPO] [TRF] Novos Seguidores - 15/09 | Crescimento do Instagram |
| 120210684872620345 | [TOPO] [VV] [CP1] Div urologia - 17/12 | Topo de Funil Video View |
| 120211170049030345 | [MEIO] [VV] Tratamento & Beneficios - 17/12 | Meio de Funil Video View |
| 120222613218500345 | [FUNDO] [MSG] Captação de leads - 15/04/25 | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Meio, Fundo) + Crescimento do Instagram com **um card a mais: "Custo/Visitas ao perfil"** (além de Valor Investido, Alcance, Visitas, Cliques na Bio, Novos Seguidores, Investido/Seguidor) + Captação de Leads (Valor Investido, Impressões, Cliques, Conversas Iniciadas, Investido/Conversa).
2. Investimento + Topo de Funil Video View + Meio de Funil Video View (cards padrão).
3. Google Ads (várias campanhas de Search por tema).

## Números de referência (out/2026)
Total R$ 1.621,36 (Topo 522,20 = seguidores 173,62 + vídeo 348,58 · Meio 243,18 · Fundo 855,98). Instagram: alcance 5.865, visitas 2.003 (R$ 0,08/visita), cliques na bio 623, 336 seguidores, R$ 0,51/seguidor. WhatsApp: 34.230 impressões, 155 cliques, 63 conversas, R$ 13,59. Vídeo topo: 15 seg 5.594 (R$ 0,06). Vídeo meio: 15 seg 2.220 (R$ 0,06).

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/dra-patricia-canelas.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/montador-relatorio.md`, Passo 1b.

```json
{
  "classificacao": {
    "120233309208820345": "instagram",
    "120210684872620345": "video_topo",
    "120211170049030345": "video",
    "120222613218500345": "whatsapp"
  },
  "layout": {
    "instagram_extras": [
      "custo_visita_perfil"
    ]
  }
}
```

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Crescimento do Instagram com 7 cards (inclui "Custo/Visitas ao perfil") | igual: card extra "Custo por visita ao perfil" (`instagram_extras`), grade de 4 colunas |
| Captação de Leads (WhatsApp) | igual, com o card Alcance a mais |
| Topo de Funil Video View | igual: página "Vídeo de topo de funil" (azul), mesmos cards e funil |
| Meio de Funil Video View | igual: página "Vídeo de meio de funil" (laranja) |
| Página de Google Ads | **fica de fora**: Google Ads é fase futura do Midas |

- No PDF, vídeo de topo e de meio dividiam a mesma página; no Midas cada um tem a sua (cabe o funil de cada).
- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.
