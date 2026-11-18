# Doc Circle

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Doc_Circle]_Relatórios_FB_3.0.pdf` (out/2026). Cliente ativo, mas **fora do Notion** (o gestor esqueceu de cadastrar, informado em 15/11/2026).

## Identificação
- Notion: não cadastrado.
- Instagram: desconhecido.
- Conta de anúncio: **não achada** na lista do conector Meta Ads (15/11/2026). Perguntar ao gestor qual é.
- Negócio: desconhecido.

## Tipo de campanha
Só **landing page** (fundo de funil). Sem Instagram, sem vídeo e sem WhatsApp.

## Estrutura do relatório antigo
1. Página única: Investimento (Total = Fundo) + "Campanhas de Landing Page": Valor Investido, Cliques, Landing Page Views, Conversão na Página, Custo/Conversão.

Sem página de Google Ads.

## Em aberto
- Conta de anúncio, Instagram e nome das campanhas.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Doc Circle",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": null,
  "instagram": null,
  "foto": null,
  "tema_video": null,
  "classificacao": {},
  "layout": {
    "nome_resultado_lp": "Conversões"
  }
}
```

`classificacao` vazia: o `coletor-dados` classifica as campanhas na primeira geração (Passo 1b) e o resultado volta para este bloco.

Só a seção `landing_page`, com o resultado chamado "Conversões" (como no PDF). Falta a conta de anúncio.
