---
id: vendors_grok_v8H
version: v8H.3
type: VENDOR_PROFILE
priority: REFERENCE
compatible_with: "!!db_v8H.md | _live/live_vendors.md | !llm_router.md"
last_verified: 2026-07-14
tags: grok, heavy-16, x-firehose, vendor, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — VENDOR: GROK (primary для grok host)
// OVERRIDE: live_specs > live_vendors > этот файл.
// ═══════════════════════════════════════════════════════

GROK_4_5:  // GA 2026-07-08 (source: docs.x.ai/developers/grok-4-5) — current agentic/coding flagship; default в Grok Build/CLI
  api_string:   grok-4.5
  context:      500K
  pricing:      $2/$6 per M (cached input $0.50)
  strengths:    coding + agentic + knowledge work; ~80 tps; ~4.2x меньше output-токенов vs Opus 4.8 на SWE-bench Pro; reasoning low/medium/high (default high)
  arch:         PLAIN_TEXT; XML только в code-fences; native strict JSON (json_schema)
  extras:       function calling, web search, X search, code execution; Responses API + Chat Completions
  cutoff:       2026-02-01
  avail:        GA (Grok Build, Cursor, xAI console); ⚠ НЕ в EU (на 2026-07-13; ожидается сер. июля)
  benchmarks:   SWE-Bench Pro 64.7% | Terminal-Bench 2.1 83.3% | Arena WebDev #6
  WHEN_TO_USE:  agentic/coding (default для Grok Build CLI); для 2M-контекста и Heavy-16 → grok-4.20.

GROK_4_3:
  api_string:   grok-4.3
  context:      1M
  pricing:      $1.25/$2.50 per M (cached $0.20)
  strengths:    X Firehose realtime, длинный контекст, нативное видео
  arch:         PLAIN_TEXT; XML только в code-fences
  thinking:     reasoning: none|low|medium|high (safe params only)
  WHEN_TO_USE:  real-time X data, длинный контекст 1M без agentic-дефолта 4.5.

GROK_4_20:  // Heavy-16 multi-agent — реальный параллелизм (эксклюзив grok host)
  api_string:   grok-4.20
  context:      2M
  pricing:      $2/$6 per M (SuperGrok Heavy $300/mo)
  strengths:    нативный Heavy-16 (до 16 параллельных tool calls), 2M контекст, X Firehose
  HEAVY_16:     HELIOS=HEAVY_ORCHESTRATOR; Tool Budget 25 (ANON ≤18); re-inject @8; JSON tool calls.
  WHEN_TO_USE:  agentic T3-4 (реальный параллелизм), ultra-long контекст 2M.

GROK_BUILD_01:
  api_string:   grok-build-0.1
  context:      256K | pricing: $1/$2 per M
  WHEN_TO_USE:  coding engine (НЕ default — с 08.07 CLI по умолчанию на grok-4.5).

KNOWN_ISSUES:  // общие для линейки
  G14: unsupported param → HTTP 400 (hard fail). Safe-list: temperature, max_tokens, stream, top_p, stop.
  G3:  topic drift → topic anchor каждые 3 хода.
  GROK45_EU_GUARD: не маршрутизировать grok-4.5 на EU-трафик до подтверждения доступности.
  GROK45_HIGH_TOKEN_CONSUMPTION: MONITORING — повышенный расход квоты на agentic-циклах.
  HEAVY16_SHADOW_DOWNGRADE: DISPUTED — сообщения о тихом даунгрейде SuperGrok Heavy → 4.3 (без подтверждения xAI).
  Type B/H/T/X/V (Heavy failure modes — см. !!db_v8H GROK_HEAVY_FAILURE_MODES).

X_FIREHOSE:   нативный x_stream; $0.50 value gate; 7-day cache (см. !x_realtime.md).
TEMP:         0.3 analytical / 0.85 creative.

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 · Vendor Grok
  SOURCE:      donor 8G.1 vendors/grok.md + live_specs v8.6.3 (Grok 4.5 GA)
  COMPATIBLE:  !llm_router.md | !host_profiles.md | !grok_heavy.md | _live/live_vendors.md
