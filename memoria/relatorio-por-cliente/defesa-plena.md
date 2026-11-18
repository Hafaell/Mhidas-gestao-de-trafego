# Defesa Plena (Denis)

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: Notion e conector Meta Ads em 15/11/2026. **Não há relatório antigo (PDF) desse cliente.**

## Identificação
- Notion: "Defesa Plena (Denis)". Tags: Seguidores Campanha, Seguidores. Prioridade 3.
- Instagram: @defesaplena
- Conta de anúncio: 392732128512252 ("Tribunal do Júri ads"). **Conector desligado para essa conta** (`is_ads_mcp_enabled: false` em 15/11/2026). O agente não consegue ler as campanhas.
- Negócio: pelo nome da conta, advocacia criminal (tribunal do júri) [Adivinhando]. É o único cliente fora da área da saúde.

## Tipo de campanha
Desconhecido. As tags do Notion sugerem campanha de seguidores [Provável].

## Em aberto
- Sem PDF e sem acesso pelo conector: perguntar ao gestor quais seções o relatório desse cliente tem.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Defesa Plena (Denis)",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "392732128512252",
  "instagram": "@defesaplena",
  "foto": null,
  "tema_video": null,
  "classificacao": {},
  "layout": {}
}
```

`classificacao` vazia: o `coletor-dados` classifica as campanhas na primeira geração (Passo 1b) e o resultado volta para este bloco.
