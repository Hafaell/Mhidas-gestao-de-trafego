# Clínica Sotre

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Clínica_Sotre]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "clinicasotre". Sem tags.
- Instagram: @clinicasotre
- Conta de anúncio: 1299560581140296 ("Clinica Sotre", BM "bmmercante", a mesma do Dr. Bernardo Mercante), conector ok.
- Negócio: clínica ortopédica em Bangu, Rio de Janeiro (termos do Google).

## Tipo de campanha
Só WhatsApp, em duas campanhas (coluna e joelho). **Sem Instagram e sem vídeo.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120239367294690711 | [FUNDO][VENDA][MSG] CP3 Div Agendamento Coluna | Captação de Leads (somada) |
| 120239366439420711 | [FUNDO][VENDA][MSG] CP3 Div Agendamento Joelho | Captação de Leads (somada) |

## Estrutura do relatório antigo
1. Investimento (Total = Fundo) + Captação de Leads, com coluna e joelho somados num bloco só (Valor Investido, Impressões, Cliques, Conversas Iniciadas, Investido/Conversa).
2. Google Ads (Search de leads; termos: ortopedista no Rio de Janeiro, ortopedista Bangu).

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Clínica Sotre",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "1299560581140296",
  "instagram": "@clinicasotre",
  "foto": null,
  "tema_video": null,
  "classificacao": {},
  "layout": {}
}
```

`classificacao` vazia: o `coletor-dados` classifica as campanhas na primeira geração (Passo 1b) e o resultado volta para este bloco.
