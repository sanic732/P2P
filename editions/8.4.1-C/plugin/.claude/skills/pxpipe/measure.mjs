#!/usr/bin/env node
// measure.mjs — real tokenizer measurement for optical compression in P2P.
// Renders an input file to PNG page(s) via the pxpipe library, then reports:
//   text chars · text tokens (gpt-tokenizer) · page count · pixels ·
//   image tokens (Anthropic ceil(W*H/750)) · compression ratio · token savings %.
// Token math is MODEL-INDEPENDENT (pixels vs tokens); legibility is a separate live test.
//
// Usage: node measure.mjs <input.(md|txt)> [--reflow] [--no-shrink] [--json]

import fs from 'node:fs/promises';
import path from 'node:path';
import { loadPxpipe } from './lib-resolve.mjs';
import { scanByteExact } from './byte-guard.mjs';

const ANTHROPIC_TOKENS_PER_IMAGE = (w, h) => Math.ceil((w * h) / 750); // Anthropic vision pricing

async function textTokens(text) {
  try {
    const mod = await import('gpt-tokenizer');
    const enc = mod.encode || (mod.default && mod.default.encode);
    if (enc) return enc(text).length;
  } catch {}
  return Math.ceil(text.length / 4); // fallback ~4 chars/token
}

async function main() {
  const args = process.argv.slice(2);
  const file = args.find((a) => !a.startsWith('--'));
  if (!file) {
    console.error('Usage: node measure.mjs <input.md> [--reflow] [--no-shrink] [--json]');
    process.exit(1);
  }
  const reflow = args.includes('--reflow');
  const shrink = !args.includes('--no-shrink');
  const asJson = args.includes('--json');

  const text = await fs.readFile(file, 'utf-8');
  const { renderTextToImages } = await loadPxpipe();

  const guard = scanByteExact(text);
  const { pages, droppedChars, pixels } = await renderTextToImages(text, { reflow, shrink });

  const tText = await textTokens(text);
  let tImage = 0;
  const pageDims = pages.map((p) => {
    const t = ANTHROPIC_TOKENS_PER_IMAGE(p.width, p.height);
    tImage += t;
    return { w: p.width, h: p.height, tokens: t };
  });

  const ratio = tImage > 0 ? tText / tImage : 0;
  const savedPct = tText > 0 ? Math.round(((tText - tImage) / tText) * 1000) / 10 : 0;

  const report = {
    file: path.basename(file),
    opts: { reflow, shrink },
    text_chars: text.length,
    text_tokens: tText,
    pages: pages.length,
    page_dims: pageDims,
    total_pixels: pixels,
    image_tokens: tImage,
    dropped_chars: droppedChars,
    compression_ratio: Math.round(ratio * 100) / 100,
    token_savings_pct: savedPct,
    profitable: tImage < tText,
    fidelity_regime: ratio <= 10 ? 'safe (<10x ~97% per DeepSeek-OCR)' : 'AGGRESSIVE (>10x — fidelity drops)',
    byte_exact_hits: guard.hits.length,
    byte_exact_counts: guard.counts,
  };

  if (asJson) {
    console.log(JSON.stringify(report, null, 2));
    return;
  }

  const bar = '─'.repeat(58);
  console.log(bar);
  console.log(`  OPTICAL COMPRESSION MEASUREMENT — ${report.file}`);
  console.log(bar);
  console.log(`  reflow=${reflow}  shrink=${shrink}`);
  console.log(`  text:   ${report.text_chars.toLocaleString()} chars  →  ${tText.toLocaleString()} text-tokens`);
  console.log(`  image:  ${pages.length} page(s)  ${pageDims.map((d) => `${d.w}x${d.h}`).join(', ')}`);
  console.log(`          ${report.total_pixels.toLocaleString()} px  →  ${tImage.toLocaleString()} image-tokens`);
  console.log(bar);
  console.log(`  COMPRESSION RATIO : ${report.compression_ratio}x   (${report.fidelity_regime})`);
  console.log(`  TOKEN SAVINGS     : ${savedPct}%   ${report.profitable ? '✅ profitable' : '❌ NOT profitable'}`);
  console.log(`  dropped chars     : ${droppedChars}`);
  console.log(`  byte-exact hits   : ${guard.hits.length}  ${JSON.stringify(guard.counts)}`);
  if (guard.hits.length) {
    console.log(`  ⚠ byte-exact content present → guard would emit a text sidecar (verbatim-safe).`);
  }
  console.log(bar);
}

main().catch((e) => {
  console.error('measure error:', e.message);
  process.exit(1);
});
