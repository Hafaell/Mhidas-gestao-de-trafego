# Dr. Rodrigo Villalva

Este arquivo é a fonte do relatório deste cliente: como ele é montado e o JSON que o gerador usa. Instagram, Drive e demais dados do Notion: `memoria/CLIENTES-ATIVOS.md`.

Fonte: `[Dr_Rodrigo_Villalva]_Relatórios_FB_3.0.pdf` (out/2026) e conector Meta Ads em 15/11/2026.

## Identificação
- Notion: "drrodrigovillalva". Tags: Planilha Div, Seguidores, Caixinhas de Pergunta.
- Instagram: @drrodrigovillalva
- Conta de anúncio do Notion: 2328762197650912 ("CA - Dr Rodrigo Villalva"). **Conector desligado para essa conta** (`is_ads_mcp_enabled: false` em 15/11/2026). A outra conta da BM, "drrodrigovillalva" (444228829894416), tem conector ligado, mas **não gastou em out/2026**: não é a do relatório.
- Negócio: especialidade não identificada (sem Google Ads).

## Tipo de campanha
Vídeo de topo + vídeo de meio (remarketing) + WhatsApp. **Sem campanha de seguidores: não tem seção de Instagram.** Nomes das campanhas não conferidos (conector desligado).

## Estrutura do relatório antigo
- Rótulos do cabeçalho: **"Topo (Pessoas novas)", "Meio (Remarketing)", "Fundo (Foco em consulta)"**.
1. Investimento + Captação de Leads **com Alcance** (Valor Investido, Impressões, Alcance, Cliques, Conversas iniciadas, Investido/Conversa).
2. Investimento + Topo de Funil Video View + Meio de Funil Video View (cards padrão).

Sem página de Google Ads.

## Em aberto
- Com o conector desligado, o agente não lê essa conta. Avisar o gestor. Status geral: `memoria/STATUS-RELATORIOS.md`.
- Em 15/11/2026 o suporte da Meta sinalizou **restrição por "atividades incomuns"** nesta conta (2328762197650912), embora o conector a mostre como ativa. O pedido de análise ("Aja agora") não foi feito: depende do gestor.

## JSON do relatório

É o cadastro e a configuração do relatório. O `coletor-dados` lê este bloco direto daqui e grava nele a classificação nova e a foto; mudança de campanha, layout ou tema também se faz aqui. Significado dos campos: `.claude/agents/coletor-dados.md`, Passo 1b.

```json
{
  "nome": "Dr. Rodrigo Villalva",
  "apelidos": [],
  "descricao": "",
  "ad_account_id": "2328762197650912",
  "instagram": "@drrodrigovillalva",
  "foto": null,
  "tema_video": null,
  "classificacao": {},
  "layout": {
    "rotulos_etapa": {
      "meio": "Remarketing"
    }
  }
}
```

`classificacao` vazia: o `coletor-dados` classifica as campanhas na primeira geração (Passo 1b) e o resultado volta para este bloco.

Vídeo de topo e de meio com página própria cada; WhatsApp com Alcance. IDs das campanhas: preencher quando o conector liberar a conta.
