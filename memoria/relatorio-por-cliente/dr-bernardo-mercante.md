# Dr. Bernardo Mercante

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Dr_Bernardo_Mercante]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Dr. Bernardo Mercante". Tags: Caixinhas de Pergunta, Seguidores. Prioridade 2.
- Instagram: @drbernardomercante
- Conta de anúncio: 637111717776472 ("CA - DR. BERNARDO", BM "bmmercante", a mesma da Clínica Sotre), conector ok.
- Negócio: ortopedista de coluna e joelho no Rio de Janeiro (termos do Google).

## Tipo de campanha
Instagram (post impulsionado) + WhatsApp em duas campanhas (coluna e joelho). O vídeo de meio existe, mas não vira seção.

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120231869446080673 | [TOPO] Post do Instagram: O joelho é a articulação do... | Crescimento do Instagram (post impulsionado, otimiza `VISIT_INSTAGRAM_PROFILE`) |
| 120243111223960673 | [FUNDO][MSG] - Agendamento Coluna | Captação de Leads (somada) |
| 120243110649610673 | [FUNDO][MSG] - Agendamento joelho | Captação de Leads (somada) |
| 120200624099140673 | [MEIO] [VV] - Institucional - 13/10 | **omitida** (só no investimento) |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Meio, Fundo) + Crescimento do Instagram (cards padrão) + Captação de Leads, com coluna e joelho somados num bloco só (Valor Investido, Impressões, Cliques, Conversas Iniciadas, Custo/Lead).
2. Google Ads (Search de leads; termos: ortopedista especialista em coluna Rio de Janeiro, ácido hialurônico no joelho).

## Decisão do gestor (15/11/2026)
- O Meio Video View Institucional fica fora do relatório **de propósito**. O gasto aparece só no bloco de investimento.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dr. Bernardo Mercante",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "637111717776472",
  "instagram": "@drbernardomercante",
  "foto": null,
  "tema_video": null,
  "classificacao": {},
  "layout": {}
}
```

`classificacao` vazia: o `coletor-dados` classifica as campanhas na primeira geração (Passo 1b) e o resultado volta para este bloco.
