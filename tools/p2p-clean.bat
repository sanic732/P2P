@echo off
chcp 65001 >nul
powershell -NoProfile -ExecutionPolicy Bypass -Command "$f='%~f0'; $l=Get-Content -LiteralPath $f -Encoding UTF8; ($l[5..($l.Count-1)] -join [char]10) | Invoke-Expression"
exit /b
REM ===== PowerShell-нагрузка ниже (строки 6+). Двойной клик по .bat запускает её. =====
$ErrorActionPreference = 'Stop'
try {
  Write-Host ''
  Write-Host '===================================================' -ForegroundColor Cyan
  Write-Host '   P2P — полная очистка остатков плагина/маркетплейса' -ForegroundColor Cyan
  Write-Host '===================================================' -ForegroundColor Cyan
  Write-Host ''
  Write-Host 'ВАЖНО: перед запуском ЗАКРОЙТЕ Claude Code / Claude Desktop / Cowork.' -ForegroundColor Yellow
  Write-Host 'Скрипт удалит все следы P2P и подготовит чистую переустановку.'
  Write-Host ''

  $claude = Join-Path $env:USERPROFILE '.claude'
  if (-not (Test-Path $claude)) {
    Write-Host 'Папка ~/.claude не найдена — чистить нечего.' -ForegroundColor Yellow
    return
  }
  $plugins = Join-Path $claude 'plugins'

  $ans = Read-Host 'Продолжить очистку? (y/n)'
  if ($ans -ne 'y') { Write-Host 'Отменено пользователем.'; return }

  $ts = Get-Date -Format 'yyyyMMdd-HHmmss'
  $bk = Join-Path $claude ('backups\p2p-clean-' + $ts)
  New-Item -ItemType Directory -Force -Path $bk | Out-Null
  foreach ($rel in @('settings.json', 'plugins\installed_plugins.json', 'plugins\known_marketplaces.json')) {
    $src = Join-Path $claude $rel
    if (Test-Path $src) { Copy-Item $src (Join-Path $bk (Split-Path $rel -Leaf)) -Force }
  }
  Write-Host ('Бэкап создан: ' + $bk) -ForegroundColor Green
  Write-Host ''

  function Save-Json($obj, $path) {
    $json = $obj | ConvertTo-Json -Depth 100
    [System.IO.File]::WriteAllText($path, $json, (New-Object System.Text.UTF8Encoding $false))
  }
  function Remove-Props($obj, [scriptblock]$match) {
    if ($null -eq $obj) { return 0 }
    $names = @($obj.PSObject.Properties.Name | Where-Object { & $match $_ })
    foreach ($n in $names) { [void]$obj.PSObject.Properties.Remove($n) }
    return $names.Count
  }
  $isP2P = { param($k) ($k -match '^p2p') -or ($k -match 'local-desktop-app-uploads') }
  $isMkt = { param($k) ($k -eq 'p2p') -or ($k -eq 'local-desktop-app-uploads') }

  $sp = Join-Path $claude 'settings.json'
  if (Test-Path $sp) {
    $j = Get-Content $sp -Raw | ConvertFrom-Json
    $n = 0
    if ($j.PSObject.Properties.Name -contains 'enabledPlugins')        { $n += Remove-Props $j.enabledPlugins $isP2P }
    if ($j.PSObject.Properties.Name -contains 'extraKnownMarketplaces') { $n += Remove-Props $j.extraKnownMarketplaces $isMkt }
    Save-Json $j $sp
    Write-Host ('settings.json — удалено P2P-записей: ' + $n)
  }

  $ip = Join-Path $plugins 'installed_plugins.json'
  if (Test-Path $ip) {
    $j = Get-Content $ip -Raw | ConvertFrom-Json
    $n = 0
    if ($j.PSObject.Properties.Name -contains 'plugins') { $n += Remove-Props $j.plugins $isP2P }
    Save-Json $j $ip
    Write-Host ('installed_plugins.json — удалено P2P-записей: ' + $n)
  }

  $kp = Join-Path $plugins 'known_marketplaces.json'
  if (Test-Path $kp) {
    $j = Get-Content $kp -Raw | ConvertFrom-Json
    $n = Remove-Props $j $isMkt
    Save-Json $j $kp
    Write-Host ('known_marketplaces.json — удалено маркетплейсов: ' + $n)
  }

  foreach ($name in @('local-desktop-app-uploads', 'p2p')) {
    $mp = Join-Path $plugins ('marketplaces\' + $name)
    if (Test-Path $mp) { Remove-Item $mp -Recurse -Force; Write-Host ('Удалена папка marketplace: ' + $name) }
    $ca = Join-Path $plugins ('cache\' + $name)
    if (Test-Path $ca) { Remove-Item $ca -Recurse -Force; Write-Host ('Удалён кэш: ' + $name) }
  }
  $cacheRoot = Join-Path $plugins 'cache'
  if (Test-Path $cacheRoot) {
    Get-ChildItem $cacheRoot -Recurse -Directory -ErrorAction SilentlyContinue |
      Where-Object { $_.Name -match 'p2p' } |
      ForEach-Object { Remove-Item $_.FullName -Recurse -Force -ErrorAction SilentlyContinue }
  }

  Write-Host ''
  Write-Host 'ГОТОВО. Все следы P2P удалены.' -ForegroundColor Green
  Write-Host ''
  Write-Host 'Теперь запустите Claude Code и поставьте начисто:' -ForegroundColor Cyan
  Write-Host '   /plugin marketplace add https://github.com/sanic732/P2P-4PDA-edition'
  Write-Host '   /plugin install p2p-v8c3@p2p'
  Write-Host ''
  Write-Host 'Плагин Light (8L.3) ставится ОТДЕЛЬНО — скачанным файлом p2p-v8l3.plugin из релиза,'
  Write-Host 'через marketplace он больше не подтягивается.'
  Write-Host ''
  Write-Host ('Если что-то пошло не так — восстановите файлы из бэкапа: ' + $bk) -ForegroundColor DarkGray
}
catch {
  Write-Host ''
  Write-Host ('ОШИБКА: ' + $_.Exception.Message) -ForegroundColor Red
  Write-Host 'Ничего не сломано: исходные файлы лежат в папке бэкапа (если он успел создаться).' -ForegroundColor Yellow
}
finally {
  Write-Host ''
  Read-Host 'Нажмите Enter для выхода'
}
