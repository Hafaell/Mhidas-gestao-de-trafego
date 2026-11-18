# Renovare Clínica

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Renovare]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "renovareclinica". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta.
- Instagram: @renovareclinica
- Conta de anúncio: 1754718338672052 ("C.A - Renovare Urologia"), conector ok. As outras contas da BM ("Renovare (Read-Only)" e uma "unknown") estão em USD e não são as do relatório.
- Negócio: urologia em Brasília (termos do Google: urologista em Brasília, andrologista).

## Tipo de campanha
Só WhatsApp, em duas campanhas. **Sem Instagram e sem vídeo.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120250264406670451 | [FUNDO][ENG][MSG] Agendamento Novo N | Captação de Leads (somada) |
| 120249484966930451 | [FUNDO][ENG][MSG] Agendamento | Captação de Leads (somada) |

Em 15/11/2026 as duas estavam **pausadas**, mas gastaram em out/2026.

## Estrutura do relatório antigo
1. Investimento (Total = Fundo) + Captação de Leads (Valor Investido, Impressões, Cliques, Conversas Iniciadas, Custo/Lead).
2. Google Ads (Search de leads; termos: urologista em Brasília, consulta urologista).

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Renovare Clínica",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "1754718338672052",
  "instagram": "@renovareclinica",
  "foto": null,
  "tema_video": null,
  "classificacao": {},
  "layout": {}
}
```

`classificacao` vazia: o `coletor-dados` classifica as campanhas na primeira geração (Passo 1b) e o resultado volta para este bloco.
