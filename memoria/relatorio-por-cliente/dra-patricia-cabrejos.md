# Dra. Patrícia Cabrejos

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Patricia_Cabrejos]_Relatórios_FB_3.0.pdf` (out/2026) e campanhas lidas no Meta Ads em 15/11/2026.

## Identificação
- Notion: "Dra. Patrícia Cabrejos". Tags: Planilha Div, Caixinhas de Pergunta.
- Instagram: @drapatriciacabrejos
- Conta de anúncio: 662414357579318 ("Dra Patrícia Cabrejos [CRM]"), conector ok. A outra conta da BM ("Dra. Patrícia Cabrejos", 499705148489800) não tem forma de pagamento e não é a do relatório.
- Negócio: tricologia (cabelo e couro cabeludo) em Manaus.

## Tipo de campanha
Só WhatsApp. **Sem campanha de seguidores e sem vídeo.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 120244820952350341 | [FUNDO][MSG] Agendamento - Tricologia | Captação de Leads Tricologia |

## Estrutura do relatório antigo
1. Investimento (Total = Fundo) + **Crescimento do Instagram sem valor investido** (Alcance, Visitas ao perfil, Seguidores, Cliques na Bio, com números do perfil, já que não há campanha de topo) + "Campanhas de Captação de Leads Tricologia" (Valor Investido, Impressões, Cliques, Conversas Iniciadas, Investido/Conversa).
2. Google Ads (Search de leads; termos: tricologista, tricologista Manaus).

## Decisão do gestor (15/11/2026)
- O bloco do Instagram **continua sendo esperado** mesmo sem campanha de seguidores (números orgânicos do perfil).

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dra. Patrícia Cabrejos",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "662414357579318",
  "instagram": "@drapatriciacabrejos",
  "foto": null,
  "tema_video": null,
  "classificacao": {
    "120244820952350341": "whatsapp"
  },
  "layout": {
    "instagram_organico": true,
    "temas": {
      "whatsapp": "Tricologia"
    }
  }
}
```
