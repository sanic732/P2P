// Resolve the pxpipe library in a portable, shippable way.
// Order: installed npm package `pxpipe-proxy` (preferred) → env PXPIPE_HOME → sibling checkout.
// The published package renders WITHOUT @napi-rs/canvas at runtime (atlas baked at build time).
import { existsSync } from 'node:fs';
import { pathToFileURL, fileURLToPath } from 'node:url';
import path from 'node:path';

const HERE = path.dirname(fileURLToPath(import.meta.url));

const FALLBACKS = [
  process.env.PXPIPE_HOME && path.join(process.env.PXPIPE_HOME, 'dist/core/library.js'),
  path.join(HERE, '../../../../pxpipe/dist/core/library.js'),
].filter(Boolean);

export async function loadPxpipe() {
  // Preferred: the installed package (portable / release path).
  try {
    return await import('pxpipe-proxy');
  } catch (_) {
    /* fall through to dev fallbacks */
  }
  for (const c of FALLBACKS) {
    if (existsSync(c)) return import(pathToFileURL(c).href);
  }
  throw new Error(
    '[pxpipe] library not found. Run `npm install pxpipe-proxy` in this skill folder, ' +
      'or set PXPIPE_HOME to a built pxpipe checkout.',
  );
}
