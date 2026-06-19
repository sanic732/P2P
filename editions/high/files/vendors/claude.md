---
id: vendors_claude_v8H
version: v8H.3
type: VENDOR_PROFILE
priority: REFERENCE
compatible_with: "!!db_v8H.md | _live/live_vendors.md | !llm_router.md"
last_verified: 2026-06-17
tags: claude, fable-5, opus-4-8, vendor, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — VENDOR: CLAUDE (для claude host; полные специи — vendors/tier1.md)
// OVERRIDE: live_specs_20260617 > live_vendors > этот файл.
// ═══════════════════════════════════════════════════════

CLAUDE_MODELS:
  claude-fable-5:    $10/$50  | 200K | #1 Agent/Text/WebDev; Safety Nanny ~5%→Opus 4.8
  claude-opus-4-8:   $15/$75  | 200K | coding #1; GraphWalks F1 1M 68.1%
  claude-opus-4-7:   $15/$75  | 200K | legacy флагман; G6 effective 160K
  claude-sonnet-4-6: $3/$15   | 200K | balanced
  claude-opus-4-6:   —        | —    | пин для >500K recall (G8)

KNOWN_ISSUES:
  G6: Opus 4.7 tokenizer inflation → план на ~160K effective.
  G7: temperature + thinking=enabled → HTTP 400 (удалить temperature).
  G8: MRCR v2 1M = 32.2% (4.7/4.8) vs 78.3% (4.6) → пин 4.6 для >500K recall.
  budget_tokens: удалён из API — использовать effort: low|medium|high.
  cache TTL: Claude Code 1h→5min (2026-06) → ephemeral на стабильный префикс.

ARCH:     XML_NATIVE (на claude host); host-gated при генерации под другие модели.
WHEN_TO_USE: coding/reasoning (Opus 4.8), agentic/WebDev/текст (Fable 5), баланс (Sonnet 4.6).

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 · Vendor Claude
  SOURCE:      donor 8G.1 vendors/claude.md + live_specs_20260617 (Fable 5/Opus 4.8)
  COMPATIBLE:  !llm_router.md | vendors/tier1.md | _live/live_vendors.md
