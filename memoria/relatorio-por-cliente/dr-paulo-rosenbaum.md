# Dr. Paulo Cesar Rosenbaum

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Dr._Paulo_Rosenbaum]_Relatórios_FB_3.0.pdf` (**período 01 a 22/10/2026**, não o mês inteiro) e campanhas lidas no Meta Ads em 15/11/2026 (out/2026 completo).

## Identificação
- Notion: "Paulo Cesar Rosenbaum". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta.
- Instagram: @drpaulocesar.rosenbaum
- Conta de anúncio: 725094333687912 ("CA - Dr Paulo Rosenbaum", BM "Dra Flavia e Paulo"), conector ok. Existe outra conta "DR PAULO ROSENBAUM" (1043855171176781), não conferida; os números do PDF batem com a 725094333687912 [Provável].
- Negócio: tratamento da dor, em Mato Grosso do Sul: Campo Grande (Google), **Nova Andradina** e **Ivinhema** (Meta).

## Tipo de campanha
Instagram (duas campanhas de seguidores) + vídeo de topo + WhatsApp **dividido em três** (tema e cidades). **Sem vídeo de meio.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120230805172670041 | [TOPO][TRF] CP1 Div \| Novos Seguidores | Crescimento do Instagram (somada) |
| 120241749296960041 | [TOPO][TRF] CP1 Div \| Novos Seguidores Nova Andradina | Crescimento do Instagram (somada) |
| 120230805904160041 | [TOPO][VV] CP1 Div | Topo de Funil Video View |
| 120230806021980041 | [FUNDO][MSG] CP3 Div \| Dor | Captação de Leads **Dor** |
| 120241749382950041 | [FUNDO][MSG] Agendamento Nova Andradina | Captação de Leads **Nova Andradina** |
| 120249017766140041 | [FUNDO][MSG] Agendamento Ivinhema | Captação de Leads **Ivinhema** |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Fundo) + Crescimento do Instagram (custo chamado "Custo/seguidores") + **três blocos de Captação de Leads**: "Dor", "Nova Andradina" e "Ivinhema", cada um com Valor Investido, Impressões, Cliques, Conversas Iniciadas e Investido/Conversa.
2. Investimento + Topo de Funil Video View (cards padrão).
3. Google Ads (Search; termos: clínica especializada em dor, médico especialista em dor, clínica da dor em Campo Grande).

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dr. Paulo Cesar Rosenbaum",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "725094333687912",
  "instagram": "@drpaulocesar.rosenbaum",
  "foto": null,
  "tema_video": null,
  "classificacao": {
    "120230805172670041": "instagram",
    "120241749296960041": "instagram",
    "120230805904160041": "video_topo",
    "120230806021980041": "whatsapp:Dor",
    "120241749382950041": "whatsapp:Nova Andradina",
    "120249017766140041": "whatsapp:Ivinhema"
  },
  "layout": {
    "blocos_whatsapp": {
      "| Dor": "Dor",
      "Nova Andradina": "Nova Andradina",
      "Ivinhema": "Ivinhema"
    }
  }
}
```
