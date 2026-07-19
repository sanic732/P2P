#!/usr/bin/env node
// compress.mjs — P2P optical-compression EXECUTOR (mechanism only; policy lives in
// compression.md L-OPTICAL / agents.md PXPIPE_GATE). Renders a narrative artifact to
// dense PNG page(s) for a reader-gated, byte-safe agent handoff.
//
// Gates enforced here (not just advised):
//   1) READER GATE  — only image for models proven to read renders (Fable 5, GPT-5.6).
//   2) BYTE GUARD   — extract byte-exact tokens (SHAs/keys/ids/paths/model-strings) to a
//                     text sidecar that rides ALONGSIDE the image (verbatim-safe).
//   3) PROFIT GATE  — refuse below --min-chars (tiny inputs lose to image overhead).
//
// Usage:
//   node compress.mjs <input.md> [--reader claude-fable-5] [--out DIR]
//                     [--min-chars 8000] [--no-reflow] [--force]
//
// Prints: markdown image links (+ sidecar) to paste for the next agent, and a measurement line.

import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { loadPxpipe } from './lib-resolve.mjs';
import { scanByteExact } from './byte-guard.mjs';

const SUPPORTED_READERS = new Set(['claude-fable-5', 'gpt-5.6', 'fable-5', 'fable']);
const ANTHROPIC_IMG_TOKENS = (w, h) => Math.ceil((w * h) / 750);

function arg(name, def) {
  const i = process.argv.indexOf(name);
  return i >= 0 && process.argv[i + 1] && !process.argv[i + 1].startsWith('--')
    ? process.argv[i + 1]
    : def;
}
const has = (name) => process.argv.includes(name);

async function textTokens(text) {
  try {
    const m = await import('gpt-tokenizer');
    const enc = m.encode || (m.default && m.default.encode);
    if (enc) return enc(text).length;
  } catch {}
  return Math.ceil(text.length / 4);
}

async function main() {
  const input = process.argv.slice(2).find((a) => !a.startsWith('--'));
  if (!input) {
    console.error('Usage: node compress.mjs <input.md> [--reader claude-fable-5] [--out DIR] [--min-chars N] [--no-reflow] [--force]');
    process.exit(1);
  }
  const reader = (arg('--reader', 'claude-fable-5') || '').toLowerCase();
  const minChars = parseInt(arg('--min-chars', '8000'), 10);
  const reflow = !has('--no-reflow');
  const force = has('--force');
  const outDir = arg('--out', path.join(path.dirname(fileURLToPath(import.meta.url)), '../../state/pxpipe_cache'));

  const text = await fs.readFile(input, 'utf-8');

  // GATE 1 — reader
  if (!SUPPORTED_READERS.has(reader) && !force) {
    console.error(`[pxpipe] REFUSED: reader "${reader}" is not a proven render-reader.`);
    console.error(`[pxpipe] Supported: ${[...SUPPORTED_READERS].join(', ')}. Passthrough as TEXT, or re-run with --force.`);
    process.exit(2);
  }
  // GATE 3 — profitability floor
  if (text.length < minChars && !force) {
    console.error(`[pxpipe] REFUSED: ${text.length} chars < --min-chars ${minChars}. Too small to win; keep as text (or --force).`);
    process.exit(3);
  }

  // GATE 2 — byte-exact guard
  const guard = scanByteExact(text);

  const { renderTextToImages } = await loadPxpipe();
  const { pages, droppedChars, pixels } = await renderTextToImages(text, { reflow, shrink: true });

  await fs.mkdir(outDir, { recursive: true });
  const base = crypto.randomBytes(4).toString('hex');
  const links = [];
  for (let i = 0; i < pages.length; i++) {
    const p = path.join(outDir, `px_${base}_p${i + 1}.png`);
    await fs.writeFile(p, pages[i].png);
    links.push(`![px_${base}_p${i + 1}](file:///${p.replace(/\\/g, '/')})`);
  }
  let sidecarPath = '';
  if (!guard.clean) {
    sidecarPath = path.join(outDir, `px_${base}_sidecar.txt`);
    await fs.writeFile(sidecarPath, guard.sidecar);
  }

  // Measurement
  const tText = await textTokens(text);
  const tImage = pages.reduce((s, p) => s + ANTHROPIC_IMG_TOKENS(p.width, p.height), 0);
  const savedPct = tText > 0 ? Math.round(((tText - tImage) / tText) * 1000) / 10 : 0;
  const ratio = tImage > 0 ? Math.round((tText / tImage) * 100) / 100 : 0;

  console.log(`[pxpipe] reader=${reader} pages=${pages.length} pixels=${pixels} dropped=${droppedChars}`);
  console.log(`[pxpipe] tokens: ${tText} text → ${tImage} image  |  ratio ${ratio}x  |  savings ${savedPct}%  ${tImage < tText ? '✅' : '❌'}`);
  if (!guard.clean) {
    console.log(`[pxpipe] ⚠ byte-exact: ${guard.hits.length} hit(s) ${JSON.stringify(guard.counts)} → sidecar written`);
  }
  console.log('\n--- paste for next agent (images + sidecar as TEXT) ---');
  console.log(links.join('\n'));
  if (sidecarPath) console.log(`\n[verbatim sidecar — paste as text, NOT image]\n${guard.sidecar}`);
}

main().catch((e) => {
  console.error('[pxpipe] error:', e.message);
  process.exit(1);
});
