#!/usr/bin/env bash
# pack.sh — Build a .plugin bundle of the Claude-Native edition (version-agnostic).
#
# WHAT THIS IS (and is NOT):
#   • The .plugin file is a ZIP of THIS single plugin folder, for MANUAL import only
#     (Cowork → "Upload a skill", or a one-off local install). It bundles ONE plugin.
#   • It is NOT how the marketplace works. "Add marketplace → Sync" clones the whole
#     repo and reads .claude-plugin/marketplace.json (at the REPO ROOT); each plugin is
#     fetched from its `source`. This script does not touch that flow.
#
# VERSIONING: name + version are read LIVE from .claude-plugin/plugin.json, so the
#   script is never tied to a hardcoded version. Output defaults to "<name>.plugin".
#
# Usage: bash pack.sh [output_name]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANIFEST="${SCRIPT_DIR}/.claude-plugin/plugin.json"

# --- Read & validate plugin.json (single source of truth for name + version) ---
if [[ ! -f "${MANIFEST}" ]]; then
  echo "ERROR: .claude-plugin/plugin.json not found"; exit 1
fi
if ! command -v python3 &> /dev/null; then
  echo "ERROR: python3 required to read plugin.json"; exit 1
fi
python3 -c "import json; json.load(open('${MANIFEST}'))" \
  || { echo "ERROR: plugin.json is not valid JSON"; exit 1; }

PLUGIN_NAME="$(python3 -c "import json; print(json.load(open('${MANIFEST}'))['name'])")"
PLUGIN_VER="$(python3 -c "import json; print(json.load(open('${MANIFEST}')).get('version','(unset → commit-SHA versioning)'))")"
OUTPUT_NAME="${1:-${PLUGIN_NAME}.plugin}"
OUTPUT_PATH="${SCRIPT_DIR}/../${OUTPUT_NAME}"

# --- Guard: a plugin folder must NOT contain its own marketplace.json ---
if [[ -f "${SCRIPT_DIR}/.claude-plugin/marketplace.json" ]]; then
  echo "ERROR: nested marketplace.json inside the plugin. It must live ONLY at the repo root."; exit 1
fi

echo "═══════════════════════════════════════════════════════════"
echo "  P2P PLUGIN PACKAGING (version-agnostic)"
echo "═══════════════════════════════════════════════════════════"
echo "  Plugin:   ${PLUGIN_NAME}"
echo "  Version:  ${PLUGIN_VER}"
echo "  Source:   ${SCRIPT_DIR}"
echo "  Output:   ${OUTPUT_PATH}"
echo "═══════════════════════════════════════════════════════════"

# Remove old output
[[ -f "${OUTPUT_PATH}" ]] && rm -f "${OUTPUT_PATH}"

# Create ZIP (renamed to .plugin)
cd "${SCRIPT_DIR}"
zip -r "${OUTPUT_PATH}" . \
  -x "*.git*" \
  -x "*.DS_Store" \
  -x "node_modules/*" \
  -x "*.plugin" \
  -x "pack.sh" \
  -x "pack.ps1" \
  > /dev/null

echo ""
echo "✅ DONE"
echo "   Bundle: ${OUTPUT_NAME}"
echo "   Size:   $(du -h "${OUTPUT_PATH}" | cut -f1)"
echo "   Files:  $(unzip -l "${OUTPUT_PATH}" 2>/dev/null | tail -1 | awk '{print $2}')"
echo ""
echo "This bundle is for MANUAL import only:"
echo "  • Cowork:      Settings → Skills → Upload a skill → ${OUTPUT_NAME}"
echo "  • Claude Code: /plugin install ${OUTPUT_PATH}"
echo ""
echo "For normal distribution use the MARKETPLACE (no bundle needed):"
echo "  • /plugin marketplace add sanic732/P2P-4PDA-edition"
echo "  • /plugin install ${PLUGIN_NAME}@P2P-4PDA-edition"
echo "═══════════════════════════════════════════════════════════"
