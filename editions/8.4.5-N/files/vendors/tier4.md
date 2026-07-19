---
id: vendors_tier4_v8N
version: v8N.3
type: VENDOR_PROFILE
tier: 4
priority: REFERENCE
compatible_with: "!!db_v8N.md | _live/live_vendors.md"
last_verified: 2026-07-13
---

// ═══════════════════════════════════════════════════════
// P2P v8N.3 — VENDORS TIER 4
// Specialist: GLM-5.2/5.1 (MIT), Kimi K2.x (Swarm), Grok 4.20 (Heavy-16, 2M)
// ═══════════════════════════════════════════════════════

GLM_52:  // NEW основной GLM — MIT, 1M context (снимает G19-лимит 5.1); WebDev Arena #3
  api_string:     glm-5.2
  context:        1M (~1,048,576) | output: 32K-131K
  pricing:        ~$1.40/$4.40 per M (spread $0.77-1.40 / $2.42-4.40)
  license:        MIT
  strengths:      WebDev #3, near-Sonnet-5 бенчи, on-prem, long-horizon agent
  NOTE:           для >120K → GLM-5.2 (не 5.1); OpenRouter AI Gateway stream-break DISPUTED (direct Zhipu API безопаснее).

GLM_51_FLASH:  // legacy — 100K hard limit; мигрировать на GLM-5.2 для длинного контекста
  api_string:     glm-5.1
  arena_elo:      1398
  context:        200K nominal / ~120K effective (G19)
  pricing:        budget
  license:        MIT (может использоваться коммерчески, включая fine-tuning)
  strengths:      MIT license, local deployment, vision (GLM-5V), cheap

  KNOWN_ISSUES:
    G19: Context collapse above ~120K. Reliable ceiling ~100-120K.
         Для длинного контекста → GLM-5.2 (1M). /compact hang на 5.1 → avoid.

  SYNTAX:
    ## Structured Segmentation (NO XML)
    temperature: 0 для строгого JSON
    thinking: on|off per turn
    ZERO XML теги в любых промптах для GLM

  LOCAL_DEPLOYMENT:
    Поддерживает локальный запуск (MIT лицензия)
    Quantized варианты доступны для потребительского железа

  IDEAL: MIT-licensed use cases, local deployment, vision tasks <100K, budget tasks.

  BENCHMARKS_LEGACY:
    GLM family: SWE-bench ~73.8% | LMSYS Elo ~1452 (GLM-4.7 historical baseline)

  GLM_VISION_PATTERN (для GLM-5V / GLM-4.6V наследие):
    Структурированные секции для UI reverse engineering:
      ## Project Map
      [структура проекта]
      ## Open Files
      [список открытых файлов]
      ## Diff
      [изменения]

GROK_420:  // Heavy-16 multi-agent — реальный параллелизм (не симуляция); 2M context
  api_string:     grok-4.20
  context:        2M
  pricing:        $2/$6 per M (доступ: SuperGrok Heavy $300/mo)
  strengths:      Heavy-16 — 16 параллельных нативных агентов; 2M контекст; X Firehose realtime
  arch:           PLAIN_TEXT; XML только внутри code-fences; нативный strict JSON

  KNOWN_ISSUES:
    G14: Unsupported params → HTTP 400 (hard fail, не silent).
         SAFE_PARAMS: temperature, max_tokens, stream, top_p, stop.
    G3:  Topic drift — anchor каждые 3 turn.
    Heavy-16 downgrade — статус DISPUTED (см. _live/live_vendors.md).

  WHEN_TO_USE: >500K контекст (альтернатива Gemini 3.1 Pro 2M) · задачи с реальным
               мультиагентным параллелизмом · realtime X-данные на большом объёме.

  NOTE:  В Normal Grok — ТОЛЬКО target-слой: строгий JSON-контракт через
         !pipeline.md GROK_JSON_TARGET + G14 safe-params. Полный генератор
         Heavy-16 пака (8 нативных агентов) — эксклюзив High/Light (!grok_heavy.md).
         Это интенциональное различие редакций, не баг.

KIMI_K2X:
  api_string:       kimi-k2.6 (Swarm 300) | kimi-k2.7-code (open-weight, $0.95/$4) | kimi-for-coding-highspeed (~5-6x)
  context:          256K-1M
  pricing:          K2.6 TBD | K2.7 Code $0.95/$4
  strengths:        Agent swarm (up to 300 agents; async webhooks >1h), open-weight coding (K2.7), Moon Vision

  KNOWN_ISSUES:
    G20: Swarm >1h via REST → timeout (async webhooks MANDATORY).
         Fix: >40 агентов → PARL async + webhooks.
    Type G: Self-revert. Checkpoint before writes обязателен.
    Type I: Overthinking на T0-T1. thinking: off для простых задач.

  THINKING_API:
    thinking: on    // для T2+ задач
    thinking: off   // T0-T1 (Type I prevention)

  SWARM_PATTERNS:
    // Синхронно (≤40 агентов):
    result = kimi.swarm(agents=list[:40], mode="sync")

    // Асинхронно (>40 агентов) — G20 prevention:
    job_id = kimi.swarm(agents=list, mode="async", webhook_url="...")
    // Получить результат через webhook callback или polling

  CHECKPOINT_PATTERN:  // Type G prevention
    "Before making any changes: output list of planned changes. Await confirmation."

  MENTAL_SANDBOX_FORMAT:  // strict format compliance
    "Simulate the entire response mentally first.
     Then output ONLY the final verified result."

  IDEAL: Multi-agent tasks, tool-heavy pipelines, agentic coding.

VERSION_METADATA:
  SYSTEM:      P2P v8N.3 · Vendors Tier 4
  MODELS:      GLM-5.2 (MIT, 1M) / GLM-5.1 (legacy), Kimi K2.6/K2.7 Code (Swarm/open-weight)
  COMPATIBLE:  !!db_v8N.md | _live/live_vendors.md
