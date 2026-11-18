# Dr. Gustavo Mesquita

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: campanhas lidas no Meta Ads em 15/11/2026 e Notion. **Não há relatório antigo (PDF) desse cliente.**

## Identificação
- Notion: "drgustavomesquita". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta.
- Instagram: @drgustavomesquita
- Conta de anúncio: 2012998965793310 ("CA - Dr Gustavo Mesquita"), conector ok. A "CA2 - Dr Gustavo Mesquita" (2256549558461026) não tem forma de pagamento e não é a usada.
- Negócio: especialidade não identificada.

## Tipo de campanha
Estrutura padrão completa: Instagram + vídeo de topo + vídeo de meio + WhatsApp. Igual à da Dra. Cleanir e da Dra. Rhaiana [Provável].

| ID | Campanha (out/2026) | Seção provável |
|---|---|---|
| 120246829138020711 | [TOPO][TRF] Novos Seguidores | Crescimento do Instagram |
| 120246829208720711 | [TOPO][VV] CP1 Div | Topo de Funil Video View |
| 120246829291620711 | [MEIO][VV] CP2 Div | Meio de Funil Video View |
| 120246828272020711 | [FUNDO][MSG] Agendamento | Captação de Leads (WhatsApp) |

## Em aberto
- Sem PDF: não se sabe se o relatório dele tinha rótulos próprios, Alcance no WhatsApp ou página de Google Ads.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dr. Gustavo Mesquita",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "2012998965793310",
  "instagram": "@drgustavomesquita",
  "foto": null,
  "tema_video": null,
  "classificacao": {
    "120246829138020711": "instagram",
    "120246829208720711": "video_topo",
    "120246829291620711": "video",
    "120246828272020711": "whatsapp"
  },
  "layout": {}
}
```
