# Memória por cliente (como o relatório de cada um é montado)

Um arquivo por cliente com **só o que o relatório dele precisa**: tipos de campanha, seções, títulos, divisões, decisões do gestor e o bloco **"JSON do relatório"** (cadastro e configuração que o gerador lê; a skill `relatorio-cliente` grava esse bloco em `clientes/<slug>.json`). Não muda o jeito geral de montar (isso está em `memoria/relatorio-meta-ads.md` e no agente `coletor-dados`).

Dados gerais do cliente (Instagram, Drive, Planilha Div, tags do Notion, quem está ativo): `memoria/CLIENTES-ATIVOS.md`. Números de referência e conferências com os PDFs antigos de out/2026 foram tirados em 17/11/2026 (continuam no histórico do git). Decisão nova do gestor sobre um cliente vai para o arquivo dele, com data.

**Quem dá e quem não dá para gerar hoje: `memoria/STATUS-RELATORIOS.md`.**

## Onde está cada cliente

| Cliente (Notion) | Arquivo | Conta de anúncio | Instagram | Topo vídeo | Meio vídeo | WhatsApp | Landing page | Google Ads (antigo) |
|---|---|---|---|---|---|---|---|---|
| Sanos Life | `sanos-life.md` | 377748377317593 | sim (post impulsionado) | – | sim | – | – | sim |
| CEIOF | `clinica-ceiof.md` | 1231637101726635 (conector desligado) | ? | ? | ? | ? | ? | só Google |
| COG Centro Ortopédico Grajaú | `cog-centro-ortopedico.md` | 430427302706806 (conector desligado) | sim | – | sim | – | – | sim |
| Carlos Alexandre | `dr-carlos-alexandre.md` | 684865741344979 | – | sim | sim | sim | – | sim |
| Clínica Lis | `clinica-lis.md` | 542875426658220 | omitido | – | omitido | sim (3 somadas) | – | – |
| Defesa Plena (Denis) | `defesa-plena.md` | 392732128512252 (conector desligado) | ? | ? | ? | ? | ? | ? |
| Dr. Raphael Kondo | `dr-raphael-kondo.md` | 319841613840597 | sim | sim | sim | sim | sim | sim |
| Dr. Bernardo Mercante | `dr-bernardo-mercante.md` | 637111717776472 | sim (post impulsionado) | – | omitido | sim (2 somadas) | – | sim |
| Dr. Gustavo Langen | `dr-gustavo-langen.md` | 507254411405150 | sim | sim | sim (2 somadas) | sim, por cidade | – | – |
| Dra. Patrícia Cabrejos | `dra-patricia-cabrejos.md` | 662414357579318 | orgânico | – | – | sim | – | sim |
| Instituto Domingues | `instituto-domingues.md` | 880566547457944 | sim | sim | sim | sim | – | – |
| Patrícia Canelas | `dra-patricia-canelas.md` | 352376624307091 | sim | sim | sim | sim | – | sim |
| Paulo Cesar Rosenbaum | `dr-paulo-rosenbaum.md` | 725094333687912 | sim (2 somadas) | sim | – | sim, por tema/cidade | – | sim |
| Rodrigo Domingues | `dr-rodrigo-domingues.md` | 4949141168532200 | sim | – | sim | sim | – | sim |
| Clínica Sotre | `clinica-sotre.md` | 1299560581140296 | – | – | – | sim (2 somadas) | – | sim |
| Dra. Cleanir Sandi | `dra-cleanir-sandi.md` | 2107073943226911 | sim | sim | sim | sim | – | – |
| Dra. Rhaiana Gondim | `dra-rhaiana-gondim.md` | 1384213717075897 | sim | sim | sim | sim | – | sim |
| Dr. Gustavo Mesquita | `dr-gustavo-mesquita.md` | 2012998965793310 | sim | sim | sim | sim | – | sem PDF |
| Dr. Rodrigo Villalva | `dr-rodrigo-villalva.md` | 2328762197650912 (conector desligado) | – | sim | sim | sim | – | – |
| Dr. Gustavo Samico | `dr-gustavo-samico.md` | 4249069415413930 | orgânico | – | – | sim | – | sim |
| Instituto Reluz (reluz.maternoinfantil) | `instituto-reluz.md` | 1003900615567848 | – | sim | – | sim | – | sim |
| Renovare | `renovare.md` | 1754718338672052 | – | – | – | sim (2 somadas) | – | sim |
| Doc Circle (fora do Notion) | `doc-circle.md` | não achada no conector | – | – | – | – | sim | – |

"Omitido" = a campanha gastou, mas o gestor tira a seção de propósito (o gasto só entra no investimento). "Orgânico" = bloco do Instagram com números do perfil, sem campanha de seguidores.

## Nome das campanhas (padrão da agência)

| Marca no nome | O que é | Seção no relatório antigo |
|---|---|---|
| `[TOPO][TRF] Novos Seguidores` | campanha de seguidores, otimiza visita ao perfil | Crescimento do Instagram |
| `[TOPO] Post do Instagram: ...` | post impulsionado, também otimiza visita ao perfil (conferido no Sanos e no Bernardo) | Crescimento do Instagram |
| `[TOPO][VV]` / `CP1 ... [VV]` | vídeo de **topo** de funil (ThruPlay) | Topo de Funil Video View |
| `[MEIO][VV]` / `CP2 ... [VV]` | vídeo de meio de funil (ThruPlay) | Meio de Funil Video View |
| `[FUNDO][MSG]` / `CP3` | conversa no WhatsApp | Campanhas de Captação de Leads |
| `[FUNDO][LP]` | landing page | Campanhas de Landing Page |
| `[MEIO][RMKT]`, `[TOPO] Institucional` | remarketing / institucional | só na Clínica Lis, omitidas |

CP1, CP2 e CP3 = topo, meio e fundo.

## Cards de cada seção no relatório antigo

- **Crescimento do Instagram:** Valor Investido, Alcance, Visitas ao perfil, Cliques na Bio, Novos Seguidores, Investido/Seguidor.
- **Video View (topo ou meio, mesmo layout):** Valor Gasto, Visualização 15 seg, Custo 15 seg; Vídeo 50%, 75% e 95% com o custo de cada; funil 15 seg → 50% → 95%.
- **Captação de Leads (WhatsApp):** Valor Investido, Impressões, Cliques, Conversas Iniciadas, Investido/Conversa. Alguns clientes têm também **Alcance** (está anotado no arquivo de cada um).
- **Landing Page:** Valor Investido, Cliques, Landing Page Views, Conversões/Leads, Custo por conversão.
- **Cabeçalho de investimento:** Total + Topo/Meio/Fundo. Alguns clientes usam rótulos próprios ("Topo (Pessoas novas)", "Fundo (Foco em consulta)").
- **Google Ads:** página própria no fim (fase futura do Midas; aqui só fica registrado quem tinha).

## O que os relatórios antigos tinham e como o Midas faz hoje (15/11/2026)

Cada arquivo de cliente tem o bloco **"JSON do relatório"** (cadastro, `classificacao` e `layout`), que o `coletor-dados` lê direto.

| Do relatório feito à mão | No Midas |
|---|---|
| **Topo de Funil Video View** separado do de meio (11 clientes) | seção `video_topo`, página própria em azul |
| **WhatsApp dividido** por cidade ou tema (Langen, Paulo Rosenbaum) | lista `whatsapp` com `bloco`; `layout.blocos_whatsapp` diz a marca no nome da campanha |
| **Landing Page** (Raphael Kondo, Doc Circle) | seção `landing_page` |
| **Instagram orgânico** sem campanha de seguidores (Samico, Cabrejos) | seção `instagram_organico` (`layout.instagram_organico: true`) |
| Card **Custo/Visitas ao perfil** (Canelas) | `layout.instagram_extras: ["custo_visita_perfil"]` |
| Rótulos próprios de etapa (Villalva, Instituto Domingues) | `layout.rotulos_etapa` |
| Tema no título (Mela, Tricologia) | `layout.temas` |
| Card **Alcance** no WhatsApp | já existia (todos têm) |
| **Seções omitidas de propósito** (Clínica Lis, Bernardo) | continua: a campanha fica fora do relatório (`fora_do_modelo`). **Não resolvido:** no PDF o gasto dela entrava no investimento total; no Midas, não |
| Página de **Google Ads** | fora: fase futura |
