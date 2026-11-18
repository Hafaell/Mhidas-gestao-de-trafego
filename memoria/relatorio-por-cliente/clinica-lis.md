# Clínica Lis

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Clinia_Lis]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Clínica Lis". Sem tags.
- Instagram: @clinica.lis
- Conta de anúncio: 542875426658220 ("Douglas Marketing", BM "douglas monteiro"), conector ok. A conta "CA - CLÍNICA LIS" (978030259519896) está desativada pela Meta e não é a do relatório.
- Negócio: clínica com várias especialidades (endocrinologia, dermatologia, pós-bariátrica, pelos nomes das campanhas).

## Tipo de campanha
Foco total em **WhatsApp** (92% do investimento). Tem topo e meio, mas eles não viram seção.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120211771691500379 | [FUNDO] [MSG] Agendamento Endocrino 09/10/2024 | Captação de Leads (somada) |
| 120209517053480379 | [FUNDO] [MSG] Agendamento Dermato 22/05/2024 | Captação de Leads (somada) |
| 120209853816700379 | [FUNDO][MSG][Venda wpp] Agendamento Pós Bariatrica - 06/06 | Captação de Leads (somada) |
| 120213072969600379 | [TOPO] Institucional | **omitida** (só no investimento) |
| 120207868334260379 | [MEIO] [RMKT] Convenio Automação - 05/04 | **omitida** (só no investimento) |

## Estrutura do relatório antigo
1. Página única: Investimento (Total, Topo, Meio, Fundo) + uma seção "Campanhas de Captação de Leads" com as 3 de WhatsApp somadas: Valor Investido, Impressões, Cliques, Conversas Iniciadas, Custo/Lead.

## Decisão do gestor (15/11/2026)
- O Topo Institucional e o Meio Remarketing ficam fora do relatório **de propósito**. O gasto deles aparece só no bloco de investimento.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Clínica Lis",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "542875426658220",
  "instagram": "@clinica.lis",
  "foto": null,
  "tema_video": null,
  "classificacao": {},
  "layout": {}
}
```

`classificacao` vazia: o `coletor-dados` classifica as campanhas na primeira geração (Passo 1b) e o resultado volta para este bloco.
