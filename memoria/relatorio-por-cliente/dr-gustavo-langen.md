# Dr. Gustavo Langen

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Dr_Gustavo_Langen]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Dr. Gustavo Langen". Tags: Planilha Div, Caixinhas de Pergunta, Seguidores.
- Instagram: @drgustavolangen
- Conta de anúncio: 507254411405150 ("CA - Dr Gustavo Langen"), conector ok. O conector mostra outras contas com o nome dele (355693226314239, 4574248379318426 e "CA - CURSO MÉDICOS" 2028634627690820), mas elas não são as do relatório.
- Negócio: ortopedia regenerativa e ombro, atendendo em **São Paulo e Campinas**.

## Tipo de campanha
Instagram + vídeo de topo + vídeo de meio + WhatsApp **dividido por cidade**.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120240476892160202 | [TOPO][TRF] Novos Seguidores | Crescimento do Instagram |
| 120232722534820202 | [TOPO][VV] CP1 Div \| Regenerativa | Topo de Funil Video View |
| 120232722815360202 | [MEIO][VV] CP2 Div \| Regenerativa | Meio de Funil Video View (somada) |
| 120243742951030202 | [MEIO][VV] CP2 Div \| Caixinhas | Meio de Funil Video View (somada) |
| 120236939086340202 | [FUNDO][MSG][SP] Post do Instagram: Dores nos ombros... | WhatsApp **São Paulo** |
| 120233085498560202 | [FUNDO][MSG][SP] CP3 Div \| Agendamento Regenerativa | WhatsApp **São Paulo** |
| 120236939041520202 | [FUNDO][MSG][CAMPINAS] Post do Instagram: Dores nos ombros... | WhatsApp **Campinas** |

A cidade está no nome da campanha (`[SP]`, `[CAMPINAS]`).

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Meio, Fundo) + Crescimento do Instagram (custo chamado "Custo/Seguidores") + Captação de Leads em **dois blocos**: "Valor Investido São Paulo" e "Valor Investido Campinas", cada um com Impressões, Cliques, Conversas Iniciadas e Investido/Conversa.
2. Investimento + Topo de Funil Video View + Meio de Funil Video View (cards padrão).

Sem página de Google Ads.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dr. Gustavo Langen",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "507254411405150",
  "instagram": "@drgustavolangen",
  "foto": null,
  "tema_video": null,
  "classificacao": {
    "120240476892160202": "instagram",
    "120232722534820202": "video_topo",
    "120232722815360202": "video",
    "120243742951030202": "video",
    "120236939086340202": "whatsapp:São Paulo",
    "120233085498560202": "whatsapp:São Paulo",
    "120236939041520202": "whatsapp:Campinas"
  },
  "layout": {
    "blocos_whatsapp": {
      "[SP]": "São Paulo",
      "[CAMPINAS]": "Campinas"
    }
  }
}
```
