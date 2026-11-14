# Futuras atualizações (para quando entrar o Google Ads)

Ideias aprovadas pelo gestor em 14/11/2026 para uma fase posterior. Nada daqui está instalado nem implementado. Mexem em integração, então cada uma exige confirmação do gestor antes de executar.

## 1. Envio automático do PDF para o Drive do cliente

- **O que faz:** depois que o gestor aprova o relatório, o PDF é gerado na pasta temporária e enviado para a pasta do cliente no Google Drive. Hoje o gestor baixa e sobe à mão, cliente por cliente.
- **Caminhos possíveis:** a skill `googleworkspace/cli@gws-drive-upload` (ferramenta oficial de linha de comando do Google Workspace, 51 mil instalações no skills.sh em 14/11/2026) ou o conector do Google Drive do claude.ai.
- **A decidir antes:** onde fica a pasta de cada cliente (guardar o ID da pasta em `clientes/<slug>.json`), se o envio é sempre manual ("manda para o Drive") ou automático, e o nome padrão do arquivo.
- **Combina com:** geração agendada no início do mês. O link em localhost só funciona no computador onde o relatório foi gerado, então rodando na nuvem o PDF teria de ir para o Drive.

## 2. Google Ads

- **O que faz:** relatório de Google Ads, no mesmo fluxo do Meta. A estrutura da página está no fim de `memoria/relatorio-meta-ads.md` (seção "Google Ads").
- **Caminho possível:** `google/skills@google-ads-api-mcp-setup` (do próprio Google, 8,8 mil instalações em 14/11/2026). Orienta a instalar o servidor oficial do Google Ads no Claude, o equivalente ao conector da Meta. Exige Python 3.12+ e pipx.
- **Atenção:** na página dessa skill no skills.sh, uma das verificações de segurança (Snyk) aparece como reprovada em 14/11/2026. Olhar o conteúdo antes de instalar.
- **A decidir antes:** como o gestor acessa as contas do Google Ads dos clientes (conta de gerente/MCC ou acesso individual), e se o Google Ads entra na mesma página ou em uma página própria com fundo cinza-chumbo, como no dashboard antigo.
- **Regras que continuam valendo:** só leitura, nada de ferramenta paga, entrega em HTML no localhost.
