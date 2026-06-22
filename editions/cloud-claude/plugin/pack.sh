#!/usr/bin/env bash
# pack.sh — Упаковка P2P v8C.3 в .plugin файл для one-click импорта
# Usage: bash pack.sh [output_name]
# Default output: p2p-v8c3.plugin

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_NAME="${1:-p2p-v8c3.plugin}"
OUTPUT_PATH="${SCRIPT_DIR}/../${OUTPUT_NAME}"

echo "═══════════════════════════════════════════════════════════"
echo "  P2P v8C.3 PACKAGING SCRIPT"
echo "═══════════════════════════════════════════════════════════"
echo "  Source:  ${SCRIPT_DIR}"
echo "  Output:  ${OUTPUT_PATH}"
echo "═══════════════════════════════════════════════════════════"

# Validate plugin.json exists
if [[ ! -f "${SCRIPT_DIR}/.claude-plugin/plugin.json" ]]; then
  echo "ERROR: .claude-plugin/plugin.json not found"
  exit 1
fi

# Validate JSON parses
if command -v python3 &> /dev/null; then
  python3 -c "import json; json.load(open('${SCRIPT_DIR}/.claude-plugin/plugin.json'))" \
    || { echo "ERROR: plugin.json is not valid JSON"; exit 1; }
fi

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
echo "   Size:  $(du -h "${OUTPUT_PATH}" | cut -f1)"
echo "   Files: $(unzip -l "${OUTPUT_PATH}" 2>/dev/null | tail -1 | awk '{print $2}')"
echo ""
echo "Install:"
echo "  • Cowork:      Settings → Skills → Upload a skill → ${OUTPUT_NAME}"
echo "  • Claude Code: /plugin install ${OUTPUT_PATH}"
echo "═══════════════════════════════════════════════════════════"
