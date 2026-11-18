# COG, Centro Ortopédico Grajaú

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[COG_Centro_Ortopédico]_Relatórios_FB_3.0.pdf` (out/2026) e conector Meta Ads em 15/11/2026.

## Identificação
- Notion: "COG - Centro Ortopédico Grajaú". Tags: Seguidores, Checar verba. Prioridade 3.
- Instagram: @grajaucentroortopedico
- Conta de anúncio do Notion: 430427302706806 ("COG Life"). **Conector desligado para essa conta** (`is_ads_mcp_enabled: false` em 15/11/2026). Existe outra conta, 2468228613414433 ("COG - Centro Ortopédico"), com conector ligado, mas **sem gasto em out/2026**: não é a do relatório.
- Negócio: clínica ortopédica no Grajaú, Rio de Janeiro.

## Tipo de campanha
Topo (Instagram) + Meio (vídeo). **Sem WhatsApp e sem landing page.** Nomes das campanhas não conferidos (conector desligado).

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Meio) + Crescimento do Instagram (cards padrão) + Meio de Funil Video View (cards padrão), tudo na mesma página.
2. Google Ads (Search "[COG - Leads]", R$ 2.431,07; termos: ortopedista, clínica ortopédica Grajaú).

## Em aberto
- Com o conector desligado, o agente não lê essa conta. Avisar o gestor.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "COG Centro Ortopédico Grajaú",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "430427302706806",
  "instagram": "@grajaucentroortopedico",
  "foto": null,
  "tema_video": null,
  "classificacao": {},
  "layout": {}
}
```

`classificacao` vazia: o `coletor-dados` classifica as campanhas na primeira geração (Passo 1b) e o resultado volta para este bloco.
