# Dr. Raphael Kondo

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

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

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dr. Raphael Kondo",
  "apelidos": [
    "raphael kondo",
    "rafael kondo",
    "rafael condo",
    "raphael condo",
    "dr raphael",
    "kondo"
  ],
  "descricao": "Menopausa e climatério · Curitiba",
  "ad_account_id": "319841613840597",
  "instagram": "@drraphaelkondo",
  "foto": "dr-raphael-kondo.jpg",
  "tema_video": null,
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
