# Dra. Patrícia Canelas

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

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

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dra. Patrícia Canelas",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "352376624307091",
  "instagram": "@patricia.urologista",
  "foto": null,
  "tema_video": null,
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
