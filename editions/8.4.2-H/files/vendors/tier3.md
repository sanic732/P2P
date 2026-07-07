---
id: vendors_tier3_v8H
version: v8H.3
type: VENDOR_PROFILE
tier: 3
priority: REFERENCE
compatible_with: "!!db_v8H.md | _live/live_vendors.md"
last_verified: 2026-06-27
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — VENDORS TIER 3
// Budget/Fast: Gemini Flash, DeepSeek V4-Flash, Qwen 3.6-Plus, Claude Haiku 4.5
// ═══════════════════════════════════════════════════════

GEMINI_31_FLASH:
  api_string:   gemini-3.1-flash-latest
  arena_elo:    1481
  context:      1M
  pricing:      $0.15/$0.60 per M
  strengths:    High-frequency, budget, 1M context

  NOTE: G2 (ZERO XML) применяется так же как Pro.
  NOTE: thinking_budget поддерживается (в отличие от Pro — G4).
  NOTE: Нет G12 (hard 429) — soft limit + retry queue.
  IDEAL: High-frequency API calls, budget tasks с >200K context.

DEEPSEEK_V4_FLASH:
  api_string:   deepseek-v4-flash
  arena_elo:    1441
  context:      32K
  pricing:      $0.07/$0.28 per M  (CHEAPEST REASONING)
  strengths:    Fastest, cheapest, light reasoning

  NOTE: G15 (reasoning carryover) — тот же fix что и V4-Pro.
  NOTE: G16 (retire deepseek-reasoner alias 2026-07-24).
  IDEAL: T0-T2 tasks, batch processing, high-volume pipelines.

QWEN_36_PLUS:
  api_string_dashscope:  qwen3-plus
  api_string_openrouter: qwen/qwen3-plus
  arena_elo:   1480 (approx)
  context:     128K
  pricing:     $0.40/$1.20 per M
  strengths:   Good quality/cost T1-2

  NOTE: G17 (provider prefix) — то же что Max.
  NOTE: G18 (preserve_thinking) — то же что Max.
  IDEAL: T1-T2 balanced budget tasks.

CLAUDE_HAIKU_45:
  api_string:   claude-haiku-4-5-20251001
  arena_elo:    1455
  context:      200K
  pricing:      $0.80/$4.00 per M
  strengths:    Fastest Claude, tool calling, T0-T1

  NOTE: G7 (no temperature + thinking) — то же что Opus/Sonnet.
  NOTE: Минимум 2048 токенов для context caching (vs 1024 у Opus/Sonnet).
  IDEAL: T0-T1 tasks, latency-sensitive apps, high volume с качеством Claude.

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 · Vendors Tier 3
  MODELS:      Gemini Flash, DeepSeek V4-Flash, Qwen 3.6-Plus, Claude Haiku 4.5
  COMPATIBLE:  !!db_v8H.md | _live/live_vendors.md
