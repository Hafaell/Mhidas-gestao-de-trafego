# Move os stories baixados (pelo Spector, via Fast Save) da pasta Downloads para Downloads\<usuario>\.
# Uso:
#   powershell -NoProfile -ExecutionPolicy Bypass -File mover-stories.ps1 -Cliente "drraphaelkondo" -Desde "2026-11-17 01:16:00" -Esperados 1
# -Cliente: nome da pasta (o @ do Instagram sem o @).
# -Desde: horario anotado ANTES do primeiro clique em "Baixar" (so arquivos depois dele sao movidos).
# -Esperados: quantos cliques em "Baixar" foram feitos (espera ate esse numero de arquivos chegar).
# Saida: uma linha por arquivo: SALVO <caminho> | JA_EXISTIA <caminho> | NENHUM_ARQUIVO
# Arquivo ASCII de proposito (PowerShell 5.1 le .ps1 sem BOM como ANSI).
param(
  [Parameter(Mandatory = $true)][string]$Cliente,
  [Parameter(Mandatory = $true)][datetime]$Desde,
  [int]$Esperados = 1,
  [int]$TimeoutSeg = 90,
  [string]$Origem = (Join-Path $env:USERPROFILE 'Downloads'),
  [string]$Raiz = (Join-Path $env:USERPROFILE 'Downloads')
)
$ErrorActionPreference = 'Stop'

$invalidos = [IO.Path]::GetInvalidFileNameChars()
$nomePasta = (-join ($Cliente.ToCharArray() | Where-Object { $invalidos -notcontains $_ })).Trim().TrimEnd('.')
if (-not $nomePasta) { throw 'Nome da pasta ficou vazio depois de limpar caracteres invalidos.' }
$destino = Join-Path $Raiz $nomePasta
$extensoes = @('.jpg', '.jpeg', '.png', '.webp', '.mp4', '.mov')

function Get-Novos {
  @(Get-ChildItem -LiteralPath $Origem -File -ErrorAction SilentlyContinue |
    Where-Object { $_.LastWriteTime -ge $Desde -or $_.CreationTime -ge $Desde })
}

# Espera os downloads terminarem (Chrome usa .crdownload enquanto baixa).
$limite = (Get-Date).AddSeconds($TimeoutSeg)
do {
  $novos = Get-Novos
  $parciais = @($novos | Where-Object { $_.Extension -eq '.crdownload' })
  $prontos = @($novos | Where-Object { $extensoes -contains $_.Extension.ToLower() })
  if ($prontos.Count -ge $Esperados -and $parciais.Count -eq 0) { break }
  Start-Sleep -Seconds 2
} while ((Get-Date) -lt $limite)

if ($prontos.Count -eq 0) { 'NENHUM_ARQUIVO'; exit 1 }
if ($prontos.Count -lt $Esperados) { "AVISO: esperava $Esperados, chegaram $($prontos.Count)" }

New-Item -ItemType Directory -Force -Path $destino | Out-Null
$hoje = Get-Date -Format 'yyyy-MM-dd'
foreach ($f in $prontos) {
  $existente = @(Get-ChildItem -LiteralPath $destino -File | Where-Object { $_.Name -eq $f.Name -or $_.Name.EndsWith("_$($f.Name)") })
  if ($existente.Count -gt 0) {
    Remove-Item -LiteralPath $f.FullName
    "JA_EXISTIA $($existente[0].FullName)"
    continue
  }
  $alvo = Join-Path $destino "${hoje}_$($f.Name)"
  Move-Item -LiteralPath $f.FullName -Destination $alvo
  "SALVO $alvo"
}
