---
id: vendors_grok_v8H
version: v8H.3
type: VENDOR_PROFILE
priority: REFERENCE
compatible_with: "!!db_v8H.md | _live/live_vendors.md | !llm_router.md"
last_verified: 2026-06-17
tags: grok, heavy-16, x-firehose, vendor, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — VENDOR: GROK (primary для grok host)
// OVERRIDE: live_specs_20260617 > live_vendors > этот файл.
// ═══════════════════════════════════════════════════════

GROK_4_3:
  api_string:   grok-4.3
  context:      2M
  pricing:      $5/$15 per M (Standard); Heavy-16 ~$15-20/M
  strengths:    нативный Heavy-16 (до 16 параллельных tool calls), X Firehose realtime, 2M контекст
  arch:         PLAIN_TEXT; XML только в code-fences
  thinking:     reasoning: on (safe params only)
  KNOWN_ISSUES:
    G14: unsupported param → HTTP 400. Safe-list: temperature, max_tokens, stream, top_p, stop.
    G3:  topic drift → topic anchor каждые 3 хода.
    Type B/H/T/X/V (Heavy failure modes — см. !!db_v8H GROK_HEAVY_FAILURE_MODES).
  HEAVY_16:     HELIOS=HEAVY_ORCHESTRATOR; Tool Budget 25 (ANON ≤18); re-inject @8; JSON tool calls.
  X_FIREHOSE:   нативный x_stream; $0.50 value gate; 7-day cache (см. !x_realtime.md).
  TEMP:         0.3 analytical / 0.85 creative.
  WHEN_TO_USE:  agentic T3-4 (реальный параллелизм), real-time X data, длинный контекст 2M.

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 · Vendor Grok
  SOURCE:      donor 8G.1 vendors/grok.md
  COMPATIBLE:  !llm_router.md | !host_profiles.md | _live/live_vendors.md
