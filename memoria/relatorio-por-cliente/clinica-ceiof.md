# Clínica CEIOF

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Clinica_CEIOF]_Relatórios_FB_3.0.pdf` (out/2026) e conector Meta Ads em 15/11/2026.

## Identificação
- Notion: "CEIOF (@ceiof)". Sem tags.
- Instagram: @ceiof
- Conta de anúncio: 1231637101726635 ("Clinica Ceiof"). **Conector desligado para essa conta** (`is_ads_mcp_enabled: false` em 15/11/2026: "Ads MCP is gradually being rolled out"). O agente não consegue ler as campanhas.
- Negócio: clínica de oftalmologia no Rio de Janeiro (Tijuca), pelos termos do Google [Provável].

## Tipo de campanha
O relatório antigo de out/2026 tem **só a página de Google Ads** (Search de leads, R$ 2.582,54, 348 conversões, R$ 7,42/conv.). **Não há nenhuma seção de Meta Ads.**

## Estrutura do relatório antigo
1. Google Ads (única página): termos "consulta oftalmologista", "clínica de olhos no Rio de Janeiro", "oftalmologista na Tijuca".

## Em aberto
- Não se sabe se o cliente tem campanha no Meta. Com o conector desligado, não dá para conferir. Perguntar ao gestor antes de montar.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Clínica CEIOF",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "1231637101726635",
  "instagram": "@ceiof",
  "foto": null,
  "tema_video": null,
  "classificacao": {},
  "layout": {}
}
```

`classificacao` vazia: o `coletor-dados` classifica as campanhas na primeira geração (Passo 1b) e o resultado volta para este bloco.
