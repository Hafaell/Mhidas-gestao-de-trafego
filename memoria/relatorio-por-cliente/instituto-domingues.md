# Instituto Domingues (estética do Dr. Rodrigo Domingues)

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Estetica_Rodrigo_Domingues]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Instituto domingues". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta. Prioridade 2.
- Instagram: @instituto.domingues
- Conta de anúncio: 880566547457944 ("CA2- DR RODRIGO DOMINGUES ESTÉTICA", BM "BM Douglas - Anunciante"), conector ok. A conta antiga "CA - Dr Rodrigo Domingues - Estetica" (224025513067237) está desativada pela Meta.
- No PDF antigo o cliente aparece como **"Estética Rodrigo Domingues"**. É um cliente diferente do Dr. Rodrigo Domingues (ortopedia, `dr-rodrigo-domingues.md`).
- Negócio: estética. As campanhas giram em torno do tema **"M.E.L.A"** (escrito "Mela" nos títulos do relatório).

## Tipo de campanha
Instagram + vídeo de topo + vídeo de meio + WhatsApp, todos do tema M.E.L.A.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120217786722210553 | [TOPO][TRF] Novos Seguidores | Crescimento do Instagram |
| 120217792613920553 | [TOPO][VV] CP1 Div - M.E.L.A | Topo de Funil Video View (Mela) |
| 120217797112750553 | [MEIO][VV] CP2 Div - M.E.L.A | Meio de Funil Video View (Mela) |
| 120221899200830553 | [FUNDO] [MSG] CP3 Div - Agendamento M.E.L.A | Captação de Leads MELA |

Em 15/11/2026 as quatro estavam **pausadas**, mas gastaram em out/2026.

## Estrutura do relatório antigo
- Rótulos do cabeçalho: **"Topo (Pessoas novas)", "Meio (Pessoas engajadas)", "Fundo (Foco em consulta)"**.
1. Investimento + Crescimento do Instagram (custo chamado "Valor investido/Seguidores") + "Campanhas de Captação de Leads MELA" **com Alcance** (Valor Investido, Impressões, Alcance, Cliques, Conversas Iniciadas, Investido/Conversa).
2. Investimento + "Topo de Funil Video View (Mela)" + "Meio de Funil Video View (Mela)" (cards padrão).

Sem página de Google Ads.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Instituto Domingues",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "880566547457944",
  "instagram": "@instituto.domingues",
  "foto": null,
  "tema_video": null,
  "classificacao": {
    "120217786722210553": "instagram",
    "120217792613920553": "video_topo",
    "120217797112750553": "video",
    "120221899200830553": "whatsapp"
  },
  "layout": {
    "rotulos_etapa": {
      "meio": "Pessoas engajadas"
    },
    "temas": {
      "video_topo": "Mela",
      "video": "Mela",
      "whatsapp": "MELA"
    }
  }
}
```
