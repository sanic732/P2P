---
id: vendors_claude_v8H
version: v8H.3
type: VENDOR_PROFILE
priority: REFERENCE
compatible_with: "!!db_v8H.md | _live/live_vendors.md | !llm_router.md"
last_verified: 2026-07-13
tags: claude, fable-5, sonnet-5, opus-4-8, vendor, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — VENDOR: CLAUDE (для claude host; полные специи — vendors/tier1.md)
// OVERRIDE: live_specs > live_vendors > этот файл.
// ═══════════════════════════════════════════════════════

CLAUDE_MODELS:
  claude-fable-5:    $10/$50  | 1M | #1 Overall/Text/Vision; classifier FP ~5%→Opus 4.8; 50%-weekly до 19.07 → credits
  claude-sonnet-5:   $2/$10   | 1M | default Free/Pro (GA 30.06); near-Opus; $3/$15 c 01.09; out 128K/300K batch
  claude-opus-4-8:   $5/$25   | 1M | coding primary; SWE-bench Pro 69.2%
  claude-opus-4-7:   $5/$25   | 1M | legacy флагман; G6 общий токенизатор
  claude-opus-4-6:   $5/$25   | 1M | пин для >500K recall (G8; MRCR 78.3%)
  claude-haiku-4-5:  $1/$5    | 200K | fast fallback (T0-1)
  claude-sonnet-4-6: legacy   | 200K | ⚠ RETIRED 30.06 (API-only)
  claude-mythos-5:   $10/$50  | 1M | 🔒 Limited (Glasswing) — НЕ маршрутизируется

KNOWN_ISSUES:
  G6: общий токенизатор Opus 4.7/4.8/Fable 5/Sonnet 5 → +30-42% на англ. прозе (by design) → пин 4.6 для cost-sensitive.
  G7: temperature/top_p/top_k + thinking=enabled → HTTP 400 (удалить).
  G8: MRCR v2 1M = 32.2% (4.7/4.8) vs 78.3% (4.6) → пин 4.6 для >500K recall.
  budget_tokens: удалён из API — thinking:{"type":"adaptive"} | effort low|medium|high|xhigh|max.
  cache TTL: Claude Code 1h→5min → ephemeral на стабильный префикс.
  Fable5_classifier: FP на security/coding → fallback Opus 4.8; security/pentest → сразу Opus 4.8.

ARCH:     XML_NATIVE (на claude host); host-gated при генерации под другие модели.
WHEN_TO_USE: coding/reasoning (Opus 4.8), agentic/frontier/vision (Fable 5), баланс (Sonnet 5), >500K recall (Opus 4.6).

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 · Vendor Claude
  SOURCE:      donor 8G.1 vendors/claude.md + live_specs v8.6.3 (Sonnet 5/Fable 5/Opus 4.8)
  COMPATIBLE:  !llm_router.md | vendors/tier1.md | _live/live_vendors.md
