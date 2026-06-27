---
id: vendors_tier4_v8H
version: v8H.3
type: VENDOR_PROFILE
tier: 4
priority: REFERENCE
compatible_with: "!!db_v8H.md | _live/live_vendors.md"
last_verified: 2026-06-27
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — VENDORS TIER 4
// Specialist: GLM-5.1 (MIT), Kimi K2.x (Swarm)
// ═══════════════════════════════════════════════════════

GLM_51_FLASH:
  api_string:     glm-5.1-flash
  arena_elo:      1398
  context:        202K nominal / 100K HARD LIMIT (G19)
  pricing:        $0.60/$1.80 per M
  license:        MIT (может использоваться коммерчески, включая fine-tuning)
  strengths:      MIT license, local deployment, vision (GLM-5V), cheap

  KNOWN_ISSUES:
    G19: Context collapse above 100K. Reliable ceiling = 100K.
         Hard block: НИКОГДА не отправлять >100K в GLM-5.1.

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

KIMI_K2X:
  api_string:       moonshot-v2-128k
  context:          128K
  pricing:          $0.50/$2.50 per M
  strengths:        Agent swarm (up to 300 agents; async webhooks >1h), 1500+ tool calls, Moon Vision

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
  SYSTEM:      P2P v8H.3 · Vendors Tier 4
  MODELS:      GLM-5.1 (MIT license), Kimi K2.x (Swarm specialist)
  COMPATIBLE:  !!db_v8H.md | _live/live_vendors.md
