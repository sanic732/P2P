---
id: live_core_v8H
version: v8H.3
type: LIVE_CORE
priority: HIGH
load_order: 5
update_frequency: weekly
last_verified: 2026-07-13
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — LIVE CORE
// Прайсинг, Arena benchmarks, маршрутизация с весами.
// Источник истины: _live/live_specs.md (v8.6.3 OVERRIDE).
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. PRICING TABLE (2026-06-27 — v8.5)
// ─────────────────────────────────────────────────────

PRICING:
  // Format: model | $/1M in | $/1M out | context | notes

  // TIER 1 — Flagship (Claude → 1M context; Opus 4.x = $5/$25)
  claude-fable-5:            $10    / $50   / 1M    / Arena Overall/Text/Vision #1; REDEPLOYED (НЕ suspended); classifier FP → fallback Opus 4.8
  claude-sonnet-5:           $2     / $10   / 1M    / NEW default Free/Pro (GA 30.06); near-Opus; $3/$15 c 01.09; out 128K/300K batch
  claude-opus-4-8:           $5     / $25   / 1M    / PRIMARY coding; effort default=high; out 128K/300K batch
  claude-opus-4-7:           $5     / $25   / 1M    / legacy; G6 общий токенизатор
  claude-opus-4-6:           $5     / $25   / 1M    / пин для >500K recall (MRCR 78.3%); токенизатор эффективнее 4.7/4.8
  gpt-5.6-sol:               $5     / $30   / 1.05M / NEW GA 09.07; WebDev #1; ⚠ reward-hacking; G10 >272K → 2x/1.5x
  gemini-3.5-flash:          $1.50  / $9.00 / 1M    / fast draft; thinkingLevel MEDIUM default
  gemini-3.1-pro-preview:    $2     / $12   / 2M    / Deep Think; grounding (<=200K цена)
  // RECALL >500K: пинить claude-opus-4-6 (MRCR v2 1M: 4.7/4.8 = 32.2% vs 4.6 = 78.3% — G8/G6)
  // NEW: gemini-3.5-pro-preview (2M, PREVIEW не GA); grok-4.20 (2M, Heavy-16); minimax-m3 ($0.30/$1.20 track-only)

  // TIER 2 — Balanced
  gpt-5.6-terra:             $2.50  / $15   / 1.05M / NEW GA 09.07; balanced (замена 5.5)
  grok-4.5:                  $2     / $6    / 500K  / NEW GA 08.07: coding/agentic flagship, ~80 tps; ⚠ не EU; strict JSON
  grok-4.3:                  $1.25  / $2.50 / 1M    / X Firehose; для 2M → grok-4.20 Heavy
  deepseek-v4-pro:           $0.435 / $0.87 / 1M    / Budget powerhouse; out 384K
  qwen3.7-max:               $2.50  / $7.50 / 1M    / Agent Era; out 131K
  // ⚠ claude-sonnet-4-6 RETIRED 30.06 (API-only legacy) — заменён Sonnet 5 выше

  // TIER 3 — Budget/Fast
  gpt-5.6-luna:              $1     / $6    / 1.05M / NEW cheap/fast; ⚠ MRCR collapse >512K
  gemini-3.5-flash:          $1.50  / $9    / 1M    / High-freq safe (no G12)
  deepseek-v4-flash:         $0.14  / $0.28 / 1M    / Cheapest reasoning; ⚠ alias 404 24.07
  qwen3.6-plus:              budget /       / 1M    /
  claude-haiku-4-5-20251001: $1     / $5    / 200K  / Fastest Claude

  // TIER 4 — Specialist/Budget
  glm-5.2:                   ~$1.40 / ~$4.40/ 1M    / MIT; WebDev #3 (заменил 5.1 для длинного ctx)
  glm-5.1:                   budget /       / 120K  / MIT, G19 limit ~120K
  kimi-k2.6:                 TBD    /       / 256K-1M / Swarm 300; kimi-k2.7-code open-weight $0.95/$4

// ─────────────────────────────────────────────────────
// §2. ARENA BENCHMARKS (snapshot; volatile — авторитетно в live_specs v8.6.3 §BENCHMARK_TABLE)
// ─────────────────────────────────────────────────────
// ⚠ Arena Elo меняется еженедельно → актуальный leaderboard держится в live_specs (OVERRIDE),
//   НЕ здесь. Ниже — исторический snapshot для грубой ориентировки.
// 2026-07-13 highlights: Fable 5 Overall/Text/Vision #1; gpt-5.6-sol WebDev #1; grok-4.5 WebDev #6.

ARENA_ELO:
  // Chatbot Arena Elo, снимок (см. live_specs для актуального)
  // Source: lmarena.ai / arena.ai

  claude-fable-5:            1665  (WebDev #1; Text #1 = 1510; Agent #1 = 12.94%)
  claude-opus-4-8:           1583  (Code #1)
  claude-opus-4-7:           1571  (legacy)
  gpt-5.5:                   1563
  gemini-3.1-pro-latest:     1549
  claude-sonnet-4-6:         1518
  grok-4.3:                  1541
  deepseek-v4-pro:           1502
  qwen3-max:                 1498
  gemini-3.1-flash-latest:   1481
  claude-haiku-4-5-20251001: 1455
  deepseek-v4-flash:         1441
  glm-5.1-flash:             1398
  moonshot-v2-128k:          1432

BENCHMARK_NOTES:
  Arena Elo — general quality, not domain-specific.
  Agentic/WebDev/Text: Claude Fable 5 #1 (debut 2026-06-10) — но Safety Nanny ~5% сессий → Opus 4.8
  Coding: Claude Opus 4.8 >> others; Fable 5 силён в WebDev
  Long context recall: Claude Opus 4.6 > Opus 4.7/4.8 for >500K (G8: MRCR 32.2% vs 78.3%)
  Math: GPT-5.5 Thinking, Gemini 3.1 Pro Deep Think
  Speed: Gemini Flash, Haiku 4.5, DeepSeek V4-Flash

// ─────────────────────────────────────────────────────
// §3. ROUTING MATRIX (веса маршрутизации)
// ─────────────────────────────────────────────────────

ROUTING_WEIGHTS:
  // Default weights before routing_memory biases applied
  // Format: task_type → {model: weight%}

  CODING:
    claude-opus-4-8:    35%
    claude-fable-5:     25%   // frontier/agentic; fallback Opus 4.8 при classifier-FP
    claude-sonnet-5:    20%   // (было sonnet-4-6, RETIRED → Sonnet 5)
    qwen3.6-plus:       12%
    deepseek-v4-pro:    8%

  REASONING:
    claude-opus-4-8:      35%
    gpt-5.6-terra:        28%  // (было gpt-5.5 → GPT-5.6)
    gemini-3.1-pro:       22%
    claude-fable-5:       10%
    deepseek-v4-pro:      5%

  RESEARCH:
    gemini-3.1-pro:       40%
    grok-4.3:             35%
    claude-opus-4-7:      15%
    deepseek-v4-pro:      10%

  CREATIVE:
    claude-opus-4-7:      40%
    gpt-5.6-terra:        30%  // (было gpt-5.5 → GPT-5.6)
    gemini-3.1-pro:       20%
    claude-sonnet-5:      10%  // (было sonnet-4-6, RETIRED → Sonnet 5)

  BUDGET:
    deepseek-v4-flash:    40%
    glm-5.1:              30%
    qwen3.6-plus:         20%
    gemini-3.5-flash:     10%

  LONG_CONTEXT:
    gemini-3.1-pro:       40%  // 2M context
    grok-4.20:            35%  // 2M context (Heavy-16)
    grok-4.3:             15%  // 1M context
    claude-opus-4-8:      10%  // 1M

// ─────────────────────────────────────────────────────
// §4. CONTEXT WINDOW STRATEGY
// ─────────────────────────────────────────────────────

CONTEXT_STRATEGY:  // v8.5: Claude Opus/Fable → 1M native; Grok 4.20 → 2M
  <100K:     Любая модель. Claude Opus 4.8 предпочтителен.
  100K-500K: Claude Opus 4.8 (1M native; G6 tokenizer +10-35% → следить за бюджетом)
  >500K:     Claude Opus 4.6 pinned (recall MRCR 78.3%) ИЛИ Grok 4.20 (2M) / Gemini 3.1 Pro (2M)
  cost-sensitive большой ctx: claude-opus-4-6 (токенизатор эффективнее) или gemini-3.5-flash
  >120K GLM: HARD BLOCK (G19)
  >100K GLM: HARD BLOCK (G19)

// ─────────────────────────────────────────────────────
// §5. THINKING BUDGET GUIDE
// ─────────────────────────────────────────────────────

THINKING_BY_TIER:
  TIER0-1: OFF (все модели)
  TIER2:   LOW/MEDIUM (проверь DEEP_THINK_VALUE_GATE)
  TIER3:   MEDIUM
  TIER4:   HIGH

THINKING_COST_MULTIPLIER:
  Claude effort=low:     ~1.5x base cost
  Claude effort=medium:  ~3x base cost
  Claude effort=high:    ~8x base cost
  Gemini LOW:            ~2x base cost
  Gemini MEDIUM:         ~5x base cost
  Gemini HIGH:           ~15x base cost (G11: осторожно!)
  GPT reasoning=medium:  ~4x base cost

THINKING_CAUTION:
  Gemini HIGH без Value Gate → G11 billing shock
  Claude + temperature → G7 HTTP 400
  GLM thinking=on при >80K → близко к G19 limit

// ─────────────────────────────────────────────────────
// §6. CACHING GUIDE (экономия токенов)
// ─────────────────────────────────────────────────────

CACHING:
  CLAUDE:
    Условие: system prompt > 1024 токенов (Haiku: 2048)
    Метод: cache_control: {type: ephemeral} (TTL: 5 минут)
    // v8.5 NOTE: Claude Code cache TTL понижен 1h → 5min (2026-06). Для длинных
    //            сессий ставить ephemeral-блок на стабильный префикс перед каждым вызовом.
    Экономия: ~90% стоимости system prompt при повторных запросах
    // Пример:
    // system=[{"type":"text","text":p2p_prompt,
    //          "cache_control":{"type":"ephemeral"}}]

  GEMINI:
    Context Caching API (>32K tokens, TTL до 1 часа)
    Экономия: ~75% при высокой частоте запросов

  OPENAI:
    Prompt Caching (автоматически для >1024 токенов)
    Экономия: ~50% на повторяющихся prefix

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 Normal · Live Core
  ROLE:        Прайсинг, Arena ELO, routing matrix, context strategy, thinking budget, caching
  SOURCE:      _live/live_specs.md (v8.6.1 OVERRIDE)
  COMPATIBLE:  !!core_v8H.md | !!db_v8H.md | _live/live_vendors.md
