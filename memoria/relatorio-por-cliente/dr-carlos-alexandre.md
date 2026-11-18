# Dr. Carlos Alexandre

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Dr_Carlos_Alexandre]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Carlos Alexandre". Sem tags.
- Instagram: @carlosazevedo.mao
- Conta de anúncio: 684865741344979 ("CA - Dr Carlos Alexandre"), conector ok.
- Negócio: cirurgião da mão / ortopedista especialista em mão (termos do Google).

## Tipo de campanha
Vídeo de topo + vídeo de meio + WhatsApp. **Sem campanha de seguidores: não tem seção de Instagram.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120240312004210183 | [TOPO][VV] CP1 Div | Topo de Funil Video View |
| 120240312322170183 | [MEIO][VV] CP2 Div | Meio de Funil Video View |
| 120236279940120183 | [FUNDO][MSG] Agendamento | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Fundo) + Captação de Leads **com Alcance**: Valor Investido, Impressões, Alcance, Cliques, Conversas Iniciadas, Investido/Conversa.
2. Investimento (Total, Topo, Meio, Fundo) + "Topo de Funil Video" + "Meio de Funil Video" (cards padrão de vídeo).
3. Google Ads (Search de leads; termos: cirurgião da mão, ortopedista especialista em mãos).

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dr. Carlos Alexandre",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "684865741344979",
  "instagram": "@carlosazevedo.mao",
  "foto": null,
  "tema_video": null,
  "classificacao": {
    "120240312004210183": "video_topo",
    "120240312322170183": "video",
    "120236279940120183": "whatsapp"
  },
  "layout": {}
}
```
