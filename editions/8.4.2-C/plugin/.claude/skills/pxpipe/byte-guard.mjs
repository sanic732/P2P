// BYTE-GUARD — scans text for byte-exact tokens that optical compression must NOT
// silently image (pxpipe/DeepSeek-OCR: exact identifiers confabulate at density).
// Policy: extract hits to a text sidecar that rides ALONGSIDE the image (pxpipe's
// documented mitigation), so the model gets the exact strings as text + the bulk as pixels.
//
// Categories (SPLIT-BRAIN forbidden list, made enforceable):
//   - hex >=12 (SHAs, hashes, hex ids)
//   - API keys (sk-..., sk-ant-...)
//   - model/API strings (claude-*, gpt-*, us.anthropic.*)
//   - P2P anchor ids (#DB_*)
//   - long digit runs >=9 (numeric ids)
//   - Windows/POSIX absolute paths

const PATTERNS = [
  ['api_key', /\bsk-(?:ant-)?[A-Za-z0-9_-]{16,}\b/g],
  ['hex12', /\b[0-9a-fA-F]{12,}\b/g],
  ['model_string', /\b(?:claude|gpt|gemini|us\.anthropic)[A-Za-z0-9._-]*\b/g],
  ['db_anchor', /#DB_[A-Z0-9_]+/g],
  ['digit_id', /\b\d{9,}\b/g],
  // десятичные суммы/валюты ($38.61, 12,50) — короткие, но verbatim-критичные:
  // слепой тест 2026-07-07 (Fable 5, плотный рендер) показал конфабуляцию $38.61→$16.61
  ['decimal', /[$€₽]\s?\d+[.,]\d{2}\b|\b\d+[.,]\d{2}\s?(?:USD|EUR|RUB|\$|€|₽)/g],
  ['path_win', /\b[A-Za-z]:\\[^\s"'`]+/g],
  ['path_posix', /(?:^|\s)(\/[A-Za-z0-9._-]+){3,}\b/g],
];

/**
 * @param {string} text
 * @returns {{clean:boolean, hits:{cat:string,value:string,line:number}[], sidecar:string, counts:Record<string,number>}}
 */
export function scanByteExact(text) {
  const lines = text.split(/\r?\n/);
  const hits = [];
  const counts = {};
  const seen = new Set();
  lines.forEach((line, i) => {
    for (const [cat, re] of PATTERNS) {
      re.lastIndex = 0;
      let m;
      while ((m = re.exec(line)) !== null) {
        const value = (m[0] || '').trim();
        if (value.length < 4) continue;
        const key = cat + '::' + value + '::' + i;
        if (seen.has(key)) continue;
        seen.add(key);
        hits.push({ cat, value, line: i + 1 });
        counts[cat] = (counts[cat] || 0) + 1;
      }
    }
  });
  const sidecar = hits.length
    ? '# BYTE-EXACT SIDECAR (verbatim — do NOT read these off the image)\n' +
      hits.map((h) => `L${h.line} [${h.cat}] ${h.value}`).join('\n') + '\n'
    : '';
  return { clean: hits.length === 0, hits, sidecar, counts };
}
