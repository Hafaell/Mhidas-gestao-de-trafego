# Dra. Cleanir Sandi

Fonte: `[Dra_Cleanir_Sandi]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "dracleanirsandi". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta. Único cliente ativo com "Relatório Feito" **desmarcado** no Notion (15/11/2026).
- Instagram: @dracleanirsandi
- Conta de anúncio: 2107073943226911 ("CA - DrA Cleanir Sandi"), conector ok.
- Negócio: especialidade não identificada nos relatórios (sem Google Ads).
- Cliente novo: o PDF de out/2026 não tem nenhuma comparação com o mês anterior, e as campanhas são recentes [Provável]. Pode não haver período anterior para comparar.

## Tipo de campanha
Estrutura padrão completa: Instagram + vídeo de topo + vídeo de meio + WhatsApp.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120254008528190332 | [TOPO][TRF] Novos Seguidores | Crescimento do Instagram |
| 120254008255330332 | [TOPO][VV] CP1 Div | Topo de Funil Video View |
| 120254008444980332 | [MEIO][VV] CP2 Div | Meio de Funil Video View |
| 120253771222360332 | [FUNDO][MSG] Agendamento | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Meio, Fundo) + Crescimento do Instagram (cards padrão) + Captação de Leads (Valor Investido, Impressões, Cliques, Conversas, Investido/Conversa).
2. Investimento + Topo de Funil Video View + Meio de Funil Video View (cards padrão).

Sem página de Google Ads. No PDF, o cabeçalho da página 2 tinha números de outro cliente (erro de cópia), e a página 1 está certa.

## Números de referência (out/2026)
Total R$ 783,66 (Topo 369,62 = seguidores 231,00 + vídeo 138,62 · Meio 87,27 · Fundo 326,77). Instagram: alcance 20.239, visitas 856, cliques na bio 7, 101 seguidores, R$ 2,28/seguidor. WhatsApp: 19.520 impressões, 75 cliques, 13 conversas, R$ 25,14. Vídeo topo: 15 seg 2.752 (R$ 0,05). Vídeo meio: 15 seg 303.

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/dra-cleanir-sandi.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "classificacao": {
    "120254008528190332": "instagram",
    "120254008255330332": "video_topo",
    "120254008444980332": "video",
    "120253771222360332": "whatsapp"
  },
  "layout": {}
}
```

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Crescimento do Instagram (6 cards) | igual; o custo se chama "Custo por seguidor" e os cliques na bio são a estimativa via anúncio (regra de 15/11/2026) |
| Captação de Leads (WhatsApp) | igual, com o card Alcance a mais |
| Topo de Funil Video View | igual: página "Vídeo de topo de funil" (azul), mesmos cards e funil |
| Meio de Funil Video View | igual: página "Vídeo de meio de funil" (laranja) |

- Estrutura padrão completa; nada de especial no layout.
- No PDF, vídeo de topo e de meio dividiam a mesma página; no Midas cada um tem a sua (cabe o funil de cada).
- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.
