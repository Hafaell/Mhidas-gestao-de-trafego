# Instituto Reluz (Reluz Materno Infantil)

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Instituto_Reluz]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "reluz.maternoinfantil". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta.
- Instagram: @reluz.maternoinfantil
- Conta de anúncio: 1003900615567848 ("CA2 Instituto Reluz"), conector ok. A "CA Instituto Reluz" (834248182578817) está desativada pela Meta, e a "CA - Reluz" (761249612788224) não é a do relatório.
- Negócio: fonoaudiologia infantil, Brasília (termos do Google).

## Tipo de campanha
Vídeo de topo + WhatsApp. **Sem campanha de seguidores (não tem seção de Instagram) e sem vídeo de meio.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120249925448730275 | [TOPO][VV] CP1 Div | Topo de Funil Video View |
| 120249924944830275 | [FUNDO][MSG] Agendamento | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Fundo) + Captação de Leads (Valor Investido, Impressões, Cliques, Conversas Iniciadas, Investido/Conversa).
2. Investimento + Topo de Funil Video View (cards padrão).
3. Google Ads (Search; termos: fono infantil, fono infantil Brasília, fonoaudiólogo infantil).

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Instituto Reluz",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "1003900615567848",
  "instagram": "@reluz.maternoinfantil",
  "foto": null,
  "tema_video": null,
  "classificacao": {
    "120249925448730275": "video_topo",
    "120249924944830275": "whatsapp"
  },
  "layout": {}
}
```
