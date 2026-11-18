# Fila de downloads: so um agente baixa por vez (varios agentes dividem a mesma pasta Downloads).
# Uso:
#   powershell -NoProfile -ExecutionPolicy Bypass -File trava-download.ps1 -Acao pegar
#   powershell -NoProfile -ExecutionPolicy Bypass -File trava-download.ps1 -Acao soltar
# pegar: espera a vez (ate -EsperaSeg) e imprime TRAVA_OK; se estourar o tempo, imprime TRAVA_TIMEOUT e sai com 1.
# soltar: libera a trava e imprime TRAVA_LIBERADA.
# Trava esquecida por mais de 5 minutos e considerada abandonada e e tomada.
# Arquivo ASCII de proposito (PowerShell 5.1 le .ps1 sem BOM como ANSI).
param(
  [Parameter(Mandatory = $true)][ValidateSet('pegar', 'soltar')][string]$Acao,
  [int]$EsperaSeg = 300,
  [int]$AbandonoSeg = 300
)
$trava = Join-Path ([IO.Path]::GetTempPath()) 'midas-caixinhas-download.lock'

if ($Acao -eq 'soltar') {
  Remove-Item -LiteralPath $trava -Force -ErrorAction SilentlyContinue
  'TRAVA_LIBERADA'
  exit 0
}

$limite = (Get-Date).AddSeconds($EsperaSeg)
while ((Get-Date) -lt $limite) {
  if (Test-Path -LiteralPath $trava) {
    $idade = ((Get-Date) - (Get-Item -LiteralPath $trava).LastWriteTime).TotalSeconds
    if ($idade -gt $AbandonoSeg) { Remove-Item -LiteralPath $trava -Force -ErrorAction SilentlyContinue }
  }
  try {
    # CreateNew falha se o arquivo ja existe: so um processo consegue.
    $fs = [IO.File]::Open($trava, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
    $fs.Close()
    'TRAVA_OK'
    exit 0
  } catch {
    Start-Sleep -Milliseconds 1500
  }
}
'TRAVA_TIMEOUT'
exit 1
