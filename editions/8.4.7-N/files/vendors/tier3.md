---
id: vendors_tier3_v8N
version: 8.4.7-N
type: VENDOR_PROFILE
tier: 3
priority: REFERENCE
compatible_with: "!!db_v8N.md | _live/live_vendors.md"
---

// ═══════════════════════════════════════════════════════
// P2P — VENDORS TIER 3
// Budget/Fast: Gemini 3.6 Flash / 3.5 Flash-Lite, DeepSeek V4-Flash, Qwen 3.6-Plus, Claude Haiku 4.5
// ═══════════════════════════════════════════════════════

GEMINI_36_FLASH:  // GA 2026-07-21 — новый workhorse вместо 3.5 Flash
  api_string:   gemini-3.6-flash
  context:      1,048,576 | output: 65,536
  pricing:      $1.50/$7.50 per M | cache-read $0.15 | ~304 tok/s
  strengths:    дешёвый bulk, нативный Computer Use, на 17% меньше выходных токенов

  NOTE: G2 (ZERO XML) применяется так же как Pro.
  ⚠ G13 на 3.6 Flash НЕ ВОСПРОИЗВЕДЁН И НЕ ПРИЗНАН — модель **не проверена** на этот баг,
    а не **очищена** от него. Обходы применять и здесь: Context Caching API, история ≤80K,
    без пачек 30+ изображений; особенно на длинных не-английских контекстах.
  ⚠ Индекс интеллекта AA = 50, как у 3.5 Flash: экономия токенов, а не рост способностей.
  NOTE: Нет G12 (hard 429) — soft limit + retry queue.
  IDEAL: High-frequency API calls, bulk multimodal, budget tasks с большим контекстом.

GEMINI_35_FLASH_LITE:  // GA 2026-07-21 — самый дешёвый уровень
  api_string:   gemini-3.5-flash-lite
  context:      1M | output: 64K | ~350 tok/s
  pricing:      $0.30/$2.50 per M
  strengths:    самая дешёвая hosted-опция с 1M контекстом
  NOTE: те же G2 / G13-обходы.

GEMINI_35_FLASH:  // предыдущий workhorse, вытеснен 3.6 Flash
  api_string:   gemini-3.5-flash
  arena_elo:    Vision #10
  context:      1M | output: 64K
  pricing:      $1.50/$9 per M

  NOTE: G2, G13 (Error 13 @100-128K; non-English триггерит) — cap 80K. Нет G12.

DEEPSEEK_V4_FLASH:
  api_string:   deepseek-v4-flash
  arena_elo:    1441
  context:      1M | output: 384K
  pricing:      $0.14/$0.28 per M  (CHEAPEST REASONING)
  status:       ⚠ линейка V4 официально PREVIEW (запись changelog 2026-04-24; более поздних,
                снимающих метку, нет). Заявления о GA — вторичные. Оставлена в маршрутизации
                с пометкой: после ретайра алиасов других путей нет.
  strengths:    Fastest, cheapest, light reasoning
  ⚠ thinking у v4-flash включён по умолчанию и НЕ отключается.

  NOTE: G15 (reasoning carryover) — тот же fix что и V4-Pro.
  NOTE: G16 — deepseek-chat/reasoner ИСПОЛНЕНО 2026-07-24 15:59 UTC, без grace-периода.
        Точный HTTP-код первичными логами не подтверждён: 404 либо 400 invalid_request_error —
        принимать оба. ⚠ Бывший deepseek-reasoner → **deepseek-v4-pro**, НЕ v4-flash-thinking.
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

FILE_META:
  MODELS:      Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, Gemini 3.5 Flash, DeepSeek V4-Flash,
               Qwen 3.6-Plus, Claude Haiku 4.5
  COMPATIBLE:  !!db_v8N.md | _live/live_vendors.md
