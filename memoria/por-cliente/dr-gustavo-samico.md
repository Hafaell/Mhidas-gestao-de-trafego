# Dr. Gustavo Samico

Fonte: `[Dr_Gustavo_Samico]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "gustavosamico.oftalmo". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta.
- Instagram: @gustavosamico.oftalmo
- Conta de anúncio: 4249069415413930 ("CA - Dr Gustavo Samico"), conector ok.
- Negócio: oftalmologia em São Paulo (Moema).

## Tipo de campanha
Só WhatsApp. **Sem campanha de seguidores e sem vídeo.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120238532655900189 | [FUNDO][MSG] Agendamento oftamologia | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
1. Investimento (Total = Fundo) + **Crescimento do Instagram sem valor investido** (Alcance, Visitas ao perfil, Novos Seguidores, Cliques na Bio, com números do perfil, já que não há campanha de topo) + Captação de Leads (Valor Investido, Impressões, Cliques, Conversas Iniciadas, Investido/Conversa).
2. Google Ads (Search de leads + Performance Max; termos: clínica oftalmologia São Paulo, oftalmologista Moema).

## Decisão do gestor (15/11/2026)
- O bloco do Instagram **continua sendo esperado** mesmo sem campanha de seguidores (números orgânicos do perfil).

## Números de referência (out/2026)
Total R$ 910,41. Instagram (perfil): alcance 72.267, visitas 4.027, 273 novos seguidores, 69 cliques na bio. WhatsApp: 41.258 impressões, 129 cliques, 56 conversas, R$ 16,26/conversa.

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/dr-gustavo-samico.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "classificacao": {
    "120238532655900189": "whatsapp"
  },
  "layout": {
    "instagram_organico": true
  }
}
```

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Crescimento do Instagram sem valor investido (Alcance, Visitas, Novos Seguidores, Cliques na Bio) | igual: seção `instagram_organico`, números do perfil, fora do total |
| Captação de Leads (WhatsApp) | igual, com o card Alcance a mais |
| Página de Google Ads | **fica de fora**: Google Ads é fase futura do Midas |

- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.
