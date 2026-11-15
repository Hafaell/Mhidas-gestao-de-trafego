# Dra. Patrícia Cabrejos

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

## Números de referência (out/2026)
Total R$ 1.522,30. Instagram (perfil): alcance 27.222, visitas 2.863, 213 seguidores, 166 cliques na bio. WhatsApp: 73.587 impressões, 532 cliques, 179 conversas, R$ 8,50/conversa.

## Configuração do relatório (layout no Midas, 15/11/2026)

Copiar para `clientes/dra-patricia-cabrejos.json` (`classificacao` e `layout`). Com isso o relatório sai igual ao feito à mão. Significado dos campos: `.claude/agents/montador-relatorio.md`, Passo 1b.

```json
{
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

## Conferência: relatório feito à mão (out/2026) x layout novo

| No PDF | No Midas |
|---|---|
| Investimento (Total, Topo, Meio, Fundo) | igual: bloco "Investimento do período" soma por etapa |
| Crescimento do Instagram sem valor investido (Alcance, Visitas, Seguidores, Cliques na Bio) | igual: seção `instagram_organico`, números do perfil pelo `relatorio/instagram_perfil.py`, fora do total. "Seguidores" do PDF = novos seguidores do mês [Provável] (213 em out/2026) |
| Campanhas de Captação de Leads Tricologia | igual: "Captação de leads no WhatsApp · Tricologia" |
| Página de Google Ads | **fica de fora**: Google Ads é fase futura do Midas |

- O Midas acrescenta páginas que o PDF não tinha: fluxos ("Do anúncio ao resultado"), comparação com o período anterior e evolução mensal.
