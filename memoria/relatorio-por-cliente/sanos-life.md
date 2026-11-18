# Sanos Life

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Sanos_Life]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "(Sanos Life) Tratamento da Dor Crônica". Tags: Seguidores, Checar verba. Prioridade 3.
- Instagram: @sanoslife
- Conta de anúncio: 377748377317593 ("Sanos Life"), conector ok.
- Negócio: clínica de ortopedia e tratamento da dor no Rio de Janeiro (Jacarepaguá, Freguesia, Taquara, pelos termos do Google) [Provável].

## Tipo de campanha
Topo (Instagram) + Meio (vídeo). **Sem WhatsApp e sem landing page.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120240256715280659 | [TOPO] Post do Instagram: Aqui na Sanos Life, entendemos... | Crescimento do Instagram (post impulsionado, otimiza `VISIT_INSTAGRAM_PROFILE`) |
| 120212202899730659 | [MEIO] [VV] CP2 \| Div \| Tratamento joelho/coluna | Meio de Funil Video View |

## Estrutura do relatório antigo
1. Investimento (Total, Topo, Meio) + Crescimento do Instagram (cards padrão; o card de seguidores se chamava "Seguidores" e o custo "Custo/seguidores").
2. Investimento + Meio de Funil Video View (cards padrão).
3. Google Ads (Search de leads + Display). É o maior investimento do cliente (R$ 6.219,88 em out/2026, contra R$ 425,20 no Meta).

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Sanos Life",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "377748377317593",
  "instagram": "@sanoslife",
  "foto": null,
  "tema_video": null,
  "classificacao": {},
  "layout": {}
}
```

`classificacao` vazia: o `coletor-dados` classifica as campanhas na primeira geração (Passo 1b) e o resultado volta para este bloco.
