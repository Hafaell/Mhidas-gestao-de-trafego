# Dra. Cleanir Sandi

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Dra_Cleanir_Sandi]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "dracleanirsandi". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta. Único cliente ativo com "Relatório Feito" **desmarcado** no Notion (15/11/2026).
- Instagram: @dracleanirsandi
- Conta de anúncio: 2107073943226911 ("CA - DrA Cleanir Sandi"), conector ok.
- Negócio: especialidade não identificada nos relatórios (sem Google Ads).
- Cliente novo: o PDF de out/2026 não tem nenhuma comparação com o mês anterior, e as campanhas são recentes [Provável]. Pode não haver período anterior para comparar.

## Tipo de campanha
Estrutura padrão completa: Instagram + vídeo de topo + vídeo de meio + WhatsApp.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120254008528190332 | [TOPO][TRF] Novos Seguidores | Crescimento do Instagram |
| 120254008255330332 | [TOPO][VV] CP1 Div | Topo de Funil Video View |
| 120254008444980332 | [MEIO][VV] CP2 Div | Meio de Funil Video View |
| 120253771222360332 | [FUNDO][MSG] Agendamento | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Meio, Fundo) + Crescimento do Instagram (cards padrão) + Captação de Leads (Valor Investido, Impressões, Cliques, Conversas, Investido/Conversa).
2. Investimento + Topo de Funil Video View + Meio de Funil Video View (cards padrão).

Sem página de Google Ads. No PDF, o cabeçalho da página 2 tinha números de outro cliente (erro de cópia), e a página 1 está certa.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dra. Cleanir Sandi",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "2107073943226911",
  "instagram": "@dracleanirsandi",
  "foto": null,
  "tema_video": null,
  "classificacao": {
    "120254008528190332": "instagram",
    "120254008255330332": "video_topo",
    "120254008444980332": "video",
    "120253771222360332": "whatsapp"
  },
  "layout": {}
}
```
