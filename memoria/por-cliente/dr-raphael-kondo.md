# Dr. Raphael Kondo

Fonte: `[Raphael_Kondo]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Dr Raphael Kondo". Tags: Planilha Div, Caixinhas de Pergunta, Seguidores.
- Instagram: @drraphaelkondo
- Conta de anúncio: 319841613840597 ("Dr Raphael Kondo [CRM]"), conector ok. A outra conta da BM, "CA - Dr. Raphael Oficial" (659325279540449), não teve gasto em out/2026.
- Negócio: menopausa e climatério, em Curitiba.

## Tipo de campanha
O cliente mais completo: Instagram + vídeo de topo + vídeo de meio + **landing page** + WhatsApp.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120222387056700435 | CP1 [TOPO] [TRF] Novos Seguidores - 22/04 | Crescimento do Instagram |
| 120230865006030435 | CP1 [TOPO] [VV] Novo Funil Menopausa - 30/07 | Topo de Funil Video View |
| 120213727032670435 | [MEIO] [CP2] [VV] Exercicios na menopausa - 19/11 | Meio de Funil Video View |
| 120246631646060435 | [FUNDO][LP] Agendamento LP - 21/05 | Campanhas de Landing Page |
| 120248101650860435 | [FUNDO] [MSG] Menopausa - 10/06 | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Meio, Fundo) + Crescimento do Instagram (custo chamado "Custo/Novos Seguidores") + **Campanhas de Landing Page** (Valor Investido, Cliques, Landing Page Views, Leads, Investido/Leads) + Captação de Leads (Valor Investido, Impressões, Cliques, Conversas Iniciadas, Custo/Lead).
2. Investimento + Topo de Funil Video View + Meio de Funil Video View (cards padrão).
3. Google Ads (Search; termos: especialista em menopausa em Curitiba, climatério).

O Fundo do cabeçalho soma landing page + WhatsApp.

## Números de referência (out/2026)
Total R$ 4.034,96 (Topo 1.087,30 = seguidores 621,02 + vídeo 466,28 · Meio 309,34 · Fundo 2.638,32 = LP 917,84 + WhatsApp 1.720,48).
- Instagram: alcance 1.109.430, visitas 39.248, cliques na bio 2.007, 12,8 mil seguidores.
- Landing page: 871 cliques, 338 landing page views, 137 leads, R$ 6,70/lead.
- WhatsApp: 58.015 impressões, 303 cliques, 106 conversas, R$ 16,23/conversa.
- Vídeo topo: 15 seg 11.626. Vídeo meio: 15 seg 3.865 (R$ 0,08).
- No PDF, o card "Valor Gasto" do vídeo de topo mostrava R$ 1.087,30 (o Topo inteiro); o vídeo de topo sozinho gastou R$ 466,28 [Certa].

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/dr-raphael-kondo.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "classificacao": {
    "120222387056700435": "instagram",
    "120230865006030435": "video_topo",
    "120213727032670435": "video",
    "120246631646060435": "landing_page",
    "120248101650860435": "whatsapp"
  },
  "layout": {}
}
```

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Crescimento do Instagram (6 cards) | igual; o custo se chama "Custo por seguidor" e os cliques na bio são a estimativa via anúncio (regra de 15/11/2026) |
| Campanhas de Landing Page (Valor Investido, Cliques, Landing Page Views, Leads, Investido/Leads) | igual: seção "Campanhas de landing page", com Impressões a mais; Leads = `results` da campanha (`conversions:contact_website`). Conferido na API: out/2026 deu 871 cliques, 338 visualizações e 137 leads, igual ao PDF |
| Captação de Leads (WhatsApp) | igual, com o card Alcance a mais |
| Topo de Funil Video View | igual: página "Vídeo de topo de funil" (azul), mesmos cards e funil |
| Meio de Funil Video View | igual: página "Vídeo de meio de funil" (laranja) |
| Página de Google Ads | **fica de fora**: Google Ads é fase futura do Midas |

- Instagram + landing page + WhatsApp = 3 blocos: a página 1 sai com cards compactos (testado, cabe).
- No PDF, o "Valor Gasto" do vídeo de topo era o Topo inteiro (R$ 1.087,30); no Midas é só o vídeo (R$ 466,28), então o custo por 15 seg sai menor que o do PDF.
- No PDF, vídeo de topo e de meio dividiam a mesma página; no Midas cada um tem a sua (cabe o funil de cada).
- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.

## Conferência com dados reais: out/2026 gerado no Midas x PDF (15/11/2026)

| Número | PDF feito à mão | Midas | Situação |
|---|---|---|---|
| Total investido | R$ 4.034,96 | R$ 4.034,96 | igual |
| Instagram: investido | R$ 621,02 | R$ 621,02 | igual |
| Instagram: novos seguidores | 12,8 mil | 250 | **diferente de propósito**: regra do gestor de 15/11/2026, seguidores vindos de todas as campanhas (o PDF usava o perfil inteiro, 12.772) |
| Instagram: alcance | 1.109.430 | 1.139.568 | 2,7% acima (corrigido: soma diária do perfil; antes era o alcance da campanha, 34.757) |
| Instagram: custo por seguidor | R$ 0,04 | R$ 2,48 | 621,02 ÷ 250 (regra nova). Com o perfil inteiro daria R$ 0,05; origem do R$ 0,04 do PDF não identificada |
| Instagram: visitas ao perfil | 39.248 | 1.355 (anúncio) | **não identificado**: o perfil inteiro teve 24.310 visitas no mês, menos que o PDF |
| Instagram: cliques na bio | 2.007 | ~185 (estimativa via anúncio) | **não identificado**: o perfil inteiro teve 3.311; o Midas mostra a estimativa via anúncio (regra de 15/11) |
| Landing page | 871 cliques, 338 visualizações, 137 leads | igual | igual |
| WhatsApp | 58.015 impr., 303 cliques, 106 conversas | igual | igual |
| Vídeo de meio | 3.865 / 1.306 / 914 / 705 | igual | igual |
| Vídeo de topo: views 15s / 50% / 75% / 95% | 11.626 / 7.673 / 4.810 / 3.880 | 9.287 / 5.151 / 3.842 / 3.159 | o PDF **somava as views de vídeo da campanha de seguidores** (2.339 / 2.522 / 968 / 721) com a [TOPO][VV]: a soma bate exata. O "Valor Gasto" do PDF (R$ 1.087,30) também era o Topo inteiro. Decisão pendente do gestor |
