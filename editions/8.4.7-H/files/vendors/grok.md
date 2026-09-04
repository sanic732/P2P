---
id: vendors_grok_v8H
version: 8.4.7-H
type: VENDOR_PROFILE
priority: REFERENCE
compatible_with: "!!db_v8H.md | _live/live_vendors.md | !llm_router.md"
tags: grok, heavy-16, x-firehose, vendor, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P — VENDOR: GROK (primary для grok host)
// OVERRIDE: live_specs > live_vendors > этот файл.
// ═══════════════════════════════════════════════════════

GROK_4_5:  // GA 2026-07-08 (source: docs.x.ai/developers/grok-4-5) — current agentic/coding flagship; default в Grok Build/CLI
  api_string:   grok-4.5
  context:      500K
  pricing:      short-context $2 in / $0.30 cached / $6 out per M — проверено у вендора
                long-context (промпты ОТ 200K): $4 in / $0.60 cached / $12 out per M
                ⚠ на обрыве удваивается И КЭШ ТОЖЕ — кэширование не смягчает, рычаг один:
                  резать контекст. Перехват 190K, жёсткий обрыв 195K.
                ⚠ унаследованная цифра cached $0.50 НЕВЕРНА (лежит между $0.30 и $0.60,
                  на глаз ошибкой не выглядит — грепать явно)
  strengths:    coding + agentic + knowledge work; ~80 tps; ~4.2x меньше output-токенов vs Opus 4.8 на SWE-bench Pro
  reasoning:    ⚠ reasoning_effort HIGH по умолчанию и НЕ ОТКЛЮЧАЕТСЯ; reasoning-токены биллятся
                как output ($6/1M) — структурная причина дрейфа стоимости на агентных циклах
  arch:         PLAIN_TEXT; XML только в code-fences; native strict JSON (json_schema)
  extras:       function calling, web search, X search, code execution; Responses API + Chat Completions
  cutoff:       2026-02-01
  avail:        GA (Grok Build, Cursor, xAI console); EU-доступ ОТКРЫТ 2026-07-21 через API-консоль,
                но БЕЗ гарантий data-residency → персональные данные EU не пускать (отдельный риск GDPR).
                50% launch-скидка закончилась 21.07.
  benchmarks:   SWE-Bench Pro 64.7% | Terminal-Bench 2.1 83.3% | Arena WebDev #8
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
  ⚠ ФАНТОМНЫЕ ID: grok-4.5-heavy / -expert / -fast НЕ СУЩЕСТВУЮТ. У вендора опубликован
    единственный id grok-4.5; Heavy — это тарифный план ($300/мес) плюс режим оркестрации
    поверх той же модели, глубина управляется reasoning_effort. Вызовы к этим id упадут.
  ⚠ Тарифы плана: X Premium $8 · Premium+ $40 · SuperGrok Lite $10 · SuperGrok $30 · Heavy $300.
    Введены жёсткие недельные лимиты даже для SuperGrok.
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
  GROK45_EU_GUARD: доступность в EU подтверждена (21.07), НО data-residency не гарантирована —
    гейт остаётся для персональных данных EU, а не для доступа как такового.
  GROK45_HIGH_TOKEN_CONSUMPTION: MONITORING — механизм установлен: reasoning_effort high
    неотключаем + reasoning биллится как output + удвоение тарифа от 200K. Контрмера:
    жёсткий cap контекста ниже 200K, API вместо подписочных поверхностей.
  HEAVY16_SHADOW_DOWNGRADE: **CLOSED AS OBSOLETE** (2026-07-26) — НЕ resolved. Разница
    принципиальна: ничего не чинили. Конфигурация, которую описывал тег — отдельный путь
    Heavy-модели, способный тихо деградировать — перестала существовать. Два прогона подряд
    не нашли воспроизведения. Закрытие как OBSOLETE фиксирует, что вопрос стал неотвечаемым,
    а не что ответ отрицательный.
    УСЛОВИЕ РЕОТКРЫТИЯ: если xAI опубликует отдельные Heavy-эндпоинты или документацию
    маршрутизации — тег оживляется, а не заводится заново.
  Type B/H/T/X/V (Heavy failure modes — см. !!db_v8H GROK_HEAVY_FAILURE_MODES).

X_FIREHOSE:   нативный x_stream; $0.50 value gate; 7-day cache (см. !x_realtime.md).
TEMP:         0.3 analytical / 0.85 creative.

FILE_META:
  COMPATIBLE:  !llm_router.md | !host_profiles.md | !grok_heavy.md | _live/live_vendors.md
