# pack.ps1 — Build a .plugin bundle of the Claude-Native edition (version-agnostic).
#
# WHAT THIS IS (and is NOT):
#   • The .plugin file is a ZIP of THIS single plugin folder, for MANUAL import only
#     (Cowork → "Upload a skill", or a one-off local install). It bundles ONE plugin.
#   • It is NOT how the marketplace works. "Add marketplace → Sync" clones the whole
#     repo and reads .claude-plugin/marketplace.json (at the REPO ROOT); each plugin is
#     fetched from its `source`. This script does not touch that flow.
#
# VERSIONING: the bundle name and version are read LIVE from .claude-plugin/plugin.json,
#   so the script is never tied to a hardcoded version — it always packs the latest manifest.
#   Output name defaults to "<plugin name>.plugin" (e.g. p2p-v8c3.plugin).
#
# Usage: powershell -ExecutionPolicy Bypass -File pack.ps1 [output_name]

param(
    [string]$OutputName
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# --- Read & validate plugin.json (single source of truth for name + version) ---
$PluginManifest = Join-Path $ScriptDir ".claude-plugin\plugin.json"
if (-not (Test-Path $PluginManifest)) {
    Write-Error "plugin.json not found at $PluginManifest"
    exit 1
}
try {
    $Manifest = Get-Content $PluginManifest -Raw | ConvertFrom-Json
} catch {
    Write-Error "plugin.json is not valid JSON: $_"
    exit 1
}
if (-not $Manifest.name) {
    Write-Error "plugin.json has no 'name' field"
    exit 1
}

$PluginName = $Manifest.name
$PluginVer  = if ($Manifest.version) { $Manifest.version } else { "(unset → commit-SHA versioning)" }
if (-not $OutputName) { $OutputName = "$PluginName.plugin" }
$OutputPath = Join-Path (Split-Path -Parent $ScriptDir) $OutputName

# --- Guard: a plugin folder must NOT contain its own marketplace.json (nested-marketplace bug) ---
$NestedMarketplace = Join-Path $ScriptDir ".claude-plugin\marketplace.json"
if (Test-Path $NestedMarketplace) {
    Write-Error "Nested marketplace.json found inside the plugin ($NestedMarketplace). marketplace.json must live ONLY at the repo root, not inside a plugin."
    exit 1
}

Write-Host "═══════════════════════════════════════════════════════════"
Write-Host "  P2P PLUGIN PACKAGING (version-agnostic)"
Write-Host "═══════════════════════════════════════════════════════════"
Write-Host "  Plugin:   $PluginName"
Write-Host "  Version:  $PluginVer"
Write-Host "  Source:   $ScriptDir"
Write-Host "  Output:   $OutputPath"
Write-Host "═══════════════════════════════════════════════════════════"

# Remove old output
if (Test-Path $OutputPath) { Remove-Item $OutputPath -Force }

# --- Stage everything except packaging artifacts ---
$Excludes = @('.git', '.DS_Store', 'node_modules', '*.plugin', 'pack.sh', 'pack.ps1')
$TempDir = Join-Path $env:TEMP "p2p-pack-$(Get-Random)"
New-Item -ItemType Directory -Path $TempDir | Out-Null

try {
    Get-ChildItem -Path $ScriptDir -Recurse -Force | ForEach-Object {
        $RelPath = $_.FullName.Substring($ScriptDir.Length + 1)
        $skip = $false
        foreach ($pattern in $Excludes) {
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

    # Sanity: staged plugin.json must still be the manifest we read
    $StagedManifest = Join-Path $TempDir ".claude-plugin\plugin.json"
    if (-not (Test-Path $StagedManifest)) {
        Write-Error "Staging failed: plugin.json missing from staged tree"
        exit 1
    }

    # Create archive with FORWARD-SLASH entry paths (.plugin = zip).
    # NOTE: Compress-Archive on Windows writes BACKSLASH separators in entry names,
    # which is non-standard and breaks some unzippers — so we build the zip via
    # System.IO.Compression and force '/' in every entry name (per tools/RELEASE_CHECKLIST.md).
    Add-Type -AssemblyName System.IO.Compression | Out-Null
    Add-Type -AssemblyName System.IO.Compression.FileSystem | Out-Null
    $fs = [System.IO.File]::Open($OutputPath, [System.IO.FileMode]::Create)
    try {
        $zip = New-Object System.IO.Compression.ZipArchive($fs, [System.IO.Compression.ZipArchiveMode]::Create)
        try {
            Get-ChildItem -Path $TempDir -Recurse -File | ForEach-Object {
                $rel = $_.FullName.Substring($TempDir.Length + 1).Replace('\', '/')
                $entry = $zip.CreateEntry($rel, [System.IO.Compression.CompressionLevel]::Optimal)
                $es = $entry.Open()
                try {
                    $bytes = [System.IO.File]::ReadAllBytes($_.FullName)
                    $es.Write($bytes, 0, $bytes.Length)
                } finally { $es.Dispose() }
            }
        } finally { $zip.Dispose() }
    } finally { $fs.Dispose() }

    $FileCount = (Get-ChildItem -Path $TempDir -Recurse -File).Count
    $SizeKB = [Math]::Round((Get-Item $OutputPath).Length / 1KB, 1)

    Write-Host ""
    Write-Host "✅ DONE" -ForegroundColor Green
    Write-Host "   Bundle: $OutputName"
    Write-Host "   Files:  $FileCount"
    Write-Host "   Size:   $SizeKB KB"
    Write-Host ""
    Write-Host "This bundle is for MANUAL import only:"
    Write-Host "  • Cowork:      Settings → Skills → Upload a skill → $OutputName"
    Write-Host "  • Claude Code: /plugin install `"$OutputPath`""
    Write-Host ""
    Write-Host "For normal distribution use the MARKETPLACE (no bundle needed):"
    Write-Host "  • /plugin marketplace add sanic732/P2P-4PDA-edition"
    Write-Host "  • /plugin install $PluginName@P2P-4PDA-edition"
    Write-Host "  • Update later: /plugin marketplace update P2P-4PDA-edition"
    Write-Host "═══════════════════════════════════════════════════════════"

} finally {
    if (Test-Path $TempDir) { Remove-Item $TempDir -Recurse -Force }
}
