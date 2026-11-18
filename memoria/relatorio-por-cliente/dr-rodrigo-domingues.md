# Dr. Rodrigo Domingues

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Dr_Rodrigo_Domingues]_Relatórios_FB_3.0.pdf` (out/2026), campanhas lidas no Meta Ads em 15/11/2026 e o JSON abaixo.

## Identificação
- Notion: "Rodrigo Domingues". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta. **Prioridade 5** (a mais alta do Notion).
- Instagram: @dr.rodrigodomingues
- Conta de anúncio: 4949141168532200 ("CA - Dr. Rodrigo Domingues"), conector ok. A conta "CA - Dr Rodrigo Domingues Médicos" (1978845849442334) não é a do relatório.
- Negócio: ortopedista especialista em coluna, Brasília.
- É um cliente diferente do Instituto Domingues (estética, `instituto-domingues.md`).
- Foi o cliente usado para montar o modelo atual do relatório. Cadastro, classificação e tema do vídeo ("Coluna") estão no JSON abaixo.

## Tipo de campanha
Instagram + vídeo de meio + WhatsApp. **Sem vídeo de topo.**

| ID | Campanha (out/2026) | Seção |
|---|---|---|
| 23862269286960250 | [TOPO] [TRF] Novos Seguidores - 04/10 | Crescimento do Instagram |
| 120250760906110251 | [MEIO] CP2 - [VV][DIV]Meio de Funil | Meio de Funil Video View Coluna |
| 120229418324530251 | [FUNDO][MSG] Agendamento - 10/07 | Captação de Leads (WhatsApp) |

## Estrutura do relatório antigo
- Rótulos do cabeçalho: **"Topo (Pessoas novas)", "Fundo (Foco em consulta)"**. O Meio gastou, mas não aparecia no cabeçalho do PDF.
1. Investimento + Crescimento do Instagram (custo chamado "Investido/Seguidores") + Captação de Leads **com Alcance** (Valor Investido, Impressões, Alcance, Cliques, Conversas iniciadas, Investido/Conversa).
2. Investimento + "Meio de Funil Video View Coluna" (cards padrão).
3. Google Ads (Search de agendamento; termos: ortopedista especialista em coluna).

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dr. Rodrigo Domingues",
  "apelidos": [
    "rodrigo",
    "dr rodrigo",
    "rodrigo domingues",
    "dr rodrigo domingues"
  ],
  "descricao": "Ortopedista, especialista em coluna · Brasília",
  "ad_account_id": "4949141168532200",
  "instagram": "@dr.rodrigodomingues",
  "foto": "dr-rodrigo-domingues.jpg",
  "tema_video": "Coluna",
  "classificacao": {
    "23862269286960250": "instagram",
    "120250760906110251": "video",
    "120229418324530251": "whatsapp"
  },
  "layout": {}
}
```
