# pack.ps1 — Упаковка P2P v8C.3-ALPHA в .plugin файл для one-click импорта
# Usage: powershell -ExecutionPolicy Bypass -File pack.ps1 [output_name]
# Default output: p2p-v8c3.plugin

param(
    [string]$OutputName = "p2p-v8c3.plugin"
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$OutputPath = Join-Path (Split-Path -Parent $ScriptDir) $OutputName

Write-Host "═══════════════════════════════════════════════════════════"
Write-Host "  P2P v8C.3-ALPHA PACKAGING SCRIPT (PowerShell)"
Write-Host "═══════════════════════════════════════════════════════════"
Write-Host "  Source:  $ScriptDir"
Write-Host "  Output:  $OutputPath"
Write-Host "═══════════════════════════════════════════════════════════"

# Validate plugin.json
$PluginManifest = Join-Path $ScriptDir ".claude-plugin\plugin.json"
if (-not (Test-Path $PluginManifest)) {
    Write-Error "plugin.json not found at $PluginManifest"
    exit 1
}

# Validate JSON parses
try {
    Get-Content $PluginManifest -Raw | ConvertFrom-Json | Out-Null
} catch {
    Write-Error "plugin.json is not valid JSON: $_"
    exit 1
}

# Remove old output
if (Test-Path $OutputPath) { Remove-Item $OutputPath -Force }

# Build temporary staging directory excluding pack scripts and .plugin files
$TempDir = Join-Path $env:TEMP "p2p-v8c3-pack-$(Get-Random)"
New-Item -ItemType Directory -Path $TempDir | Out-Null

try {
    # Copy everything except excluded patterns
    Get-ChildItem -Path $ScriptDir -Recurse -Force | ForEach-Object {
        $RelPath = $_.FullName.Substring($ScriptDir.Length + 1)
        $skip = $false
        foreach ($pattern in @('.git', '.DS_Store', 'node_modules', '*.plugin', 'pack.sh', 'pack.ps1')) {
            if ($RelPath -like "*$pattern*") { $skip = $true; break }
        }
        if (-not $skip) {
            $Target = Join-Path $TempDir $RelPath
            if ($_.PSIsContainer) {
                New-Item -ItemType Directory -Path $Target -Force | Out-Null
            } else {
                $TargetDir = Split-Path -Parent $Target
                if (-not (Test-Path $TargetDir)) { New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null }
                Copy-Item $_.FullName $Target -Force
            }
        }
    }

    # Create archive (.plugin = renamed .zip; Compress-Archive requires .zip extension)
    $ZipPath = [System.IO.Path]::ChangeExtension($OutputPath, ".zip")
    if (Test-Path $ZipPath) { Remove-Item $ZipPath -Force }
    Compress-Archive -Path "$TempDir\*" -DestinationPath $ZipPath -CompressionLevel Optimal -Force
    Rename-Item -Path $ZipPath -NewName (Split-Path -Leaf $OutputPath)

    Write-Host ""
    Write-Host "✅ DONE" -ForegroundColor Green
    $Size = (Get-Item $OutputPath).Length
    $SizeKB = [Math]::Round($Size / 1KB, 1)
    Write-Host "   Size:  $SizeKB KB"
    Write-Host "   Path:  $OutputPath"
    Write-Host ""
    Write-Host "Install:"
    Write-Host "  • Cowork:      Settings → Skills → Upload a skill → $OutputName"
    Write-Host "  • Claude Code: /plugin install `"$OutputPath`""
    Write-Host "═══════════════════════════════════════════════════════════"

} finally {
    if (Test-Path $TempDir) { Remove-Item $TempDir -Recurse -Force }
}
