# Dr. Gustavo Samico

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

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

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dr. Gustavo Samico",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "4249069415413930",
  "instagram": "@gustavosamico.oftalmo",
  "foto": null,
  "tema_video": null,
  "classificacao": {
    "120238532655900189": "whatsapp"
  },
  "layout": {
    "instagram_organico": true
  }
}
```
