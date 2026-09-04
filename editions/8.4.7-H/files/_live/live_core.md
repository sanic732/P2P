---
id: live_core_v8H
version: 8.4.7-H
type: LIVE_CORE
priority: HIGH
load_order: 5
update_frequency: weekly
last_verified: 2026-07-26
---

// ═══════════════════════════════════════════════════════
// P2P — LIVE CORE
// Прайсинг, Arena benchmarks, маршрутизация с весами.
// Источник истины: _live/live_specs.md (v8.6.3 OVERRIDE).
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. PRICING TABLE (2026-06-27 — v8.5)
// ─────────────────────────────────────────────────────

PRICING:
  // Format: model | $/1M in | $/1M out | context | notes

  // TIER 1 — Flagship (Claude → 1M context; Opus 4.x = $5/$25)
  claude-opus-5:             $5     / $25   / 1M    / PRIMARY (GA 24.07); thinking ON BY DEFAULT; out 128K; general reasoning/agentic/long-horizon
  claude-fable-5:            $10    / $50   / 1M    / Arena Text/Vision #1; batch 5/25, cache-hit in 1; classifier FP → fallback Opus 4.8; USAGE CREDITS с 20.07 — COST-GATED, не в автоциклы
  claude-sonnet-5:           $2     / $10   / 1M    / NEW default Free/Pro (GA 30.06); near-Opus; $3/$15 c 01.09; out 128K/300K batch
  claude-opus-4-8:           $5     / $25   / 1M    / coding; effort default=high; out 128K/300K batch; ACTIVE, НЕ депрекирован (floor «не ранее 2027-05-28»); API-only surface — UI-видимость ≠ доступность
  claude-opus-4-7:           $5     / $25   / 1M    / legacy; G6 общий токенизатор
  claude-opus-4-6:           $5     / $25   / 1M    / пин для >500K recall (MRCR 78.3%); токенизатор эффективнее 4.7/4.8
  gpt-5.6-sol:               $5     / $30   / 1.05M / GA 09.07; cached 0.50; >272K → 10/45 при cached тоже ×2; ⚠ G22 агентная опасность — вне judge-ролей и harness с записью в ФС/секреты
  gemini-3.6-flash:          $1.50  / $7.50 / 1,048,576 / GA 21.07 workhorse; cache-read 0.15; ~304 tok/s; нативный Computer Use; ⚠ G13 НЕ тестирован — не очищен, обходы применять
  gemini-3.5-flash:          $1.50  / $9.00 / 1M    / вытеснен 3.6 Flash; thinkingLevel MEDIUM default
  gemini-3.1-pro-preview:    $2     / $12   / 2M    / Deep Think; grounding (<=200K цена)
  // RECALL >500K: пинить claude-opus-4-6 (MRCR v2 1M: 4.7/4.8 = 32.2% vs 4.6 = 78.3% — G8/G6)
  // gemini-3.5-pro-preview (2M, PREVIEW — ТРЕТИЙ пропуск GA); grok-4.20 (2M, Heavy-16); minimax-m3 (0.30/1.20 track-only)
  // ⚠ claude-opus-4-1-20250805 RETIRES 2026-08-05 (замена по офиц. таблице — opus-4-8)

  // TIER 2 — Balanced
  gpt-5.6-terra:             $2.50  / $15   / 1.05M / GA 09.07; balanced (замена 5.5); long-context ставки НЕ документированы
  grok-4.5:                  $2     / $6    / 500K  / GA 08.07: coding/agentic flagship, ~80 tps; cached $0.30; от 200K → $4 / $0.60 cached / $12 (удваивается и кэш); EU открыт 21.07 БЕЗ data-residency; strict JSON
  grok-4.3:                  $1.25  / $2.50 / 1M    / X Firehose; для 2M → grok-4.20 Heavy
  deepseek-v4-pro:           $0.435 / $0.87 / 1M    / Budget powerhouse; out 384K
  qwen3.7-max:               $2.50  / $7.50 / 1M    / Agent Era; out 131K
  // ✅ claude-sonnet-4-6 активен; с 30.06 дефолт — Sonnet 5 выше

  // TIER 3 — Budget/Fast
  gpt-5.6-luna:              $1     / $6    / ⚠ офиц. строки нет / cheap/fast; MRCR collapse >512K; long-context ставки НЕ документированы; голый алиас gpt-5.6 → Sol
  gemini-3.5-flash-lite:     $0.30  / $2.50 / 1M    / GA 21.07; самый дешёвый уровень; ~350 tok/s
  gemini-3.5-flash:          $1.50  / $9    / 1M    / High-freq safe (no G12)
  deepseek-v4-flash:         $0.22  / $0.66 / 1M    / Cheapest reasoning; v4-pro GA 13.08, flash-0731 public beta; алиасы мертвы 24.07; thinking неотключаем
  qwen3.7-plus:              $0.32  / $1.28 / 1M    / multimodal (расхождение по цене: и 0.40/1.60)
  qwen3.6-35b-a3b:           $0.14  / $1.00 / 262,144 / open-weight Apache-2.0
  qwen3.6-plus:              budget /       / 1M    /
  claude-haiku-4-5-20251001: $1     / $5    / 200K  / Fastest Claude

  // TIER 4 — Specialist/Budget
  glm-5.2:                   ⚠ UNCONFIRMED  / 1M    / MIT; WebDev #4; цена ~1.40/4.40 из единственного источника, в canon НЕ принята
  glm-5.1:                   budget /       / 120K  / MIT, G19 limit ~120K
  kimi-k3:                   $3     / $15   / 1,048,576 / GA 16.07, WebDev #1; thinking always-on; ⚠ ACCESS-RISK: hosted-only, подписки закрыты, весов нет → НЕ primary
  kimi-k2.6:                 TBD    /       / 256K-1M / Swarm 300; kimi-k2.7-code open-weight 0.95/4

// ─────────────────────────────────────────────────────
// §2. ARENA BENCHMARKS (snapshot; volatile — авторитетно в live_specs v8.6.3 §BENCHMARK_TABLE)
// ─────────────────────────────────────────────────────
// ⚠ Arena Elo меняется еженедельно → актуальный leaderboard держится в live_specs (OVERRIDE),
//   НЕ здесь. Ниже — исторический snapshot для грубой ориентировки.
// 2026-07-26 highlights: kimi-k3 дебютирует WebDev #1 (первый раз позицию держит не Anthropic и не OpenAI);
//   Fable 5 держит Text/Vision #1, но теряет Document #1 (→ claude-opus-4-6) и WebDev #1;
//   claude-sonnet-5-high входит в Agent #5, Document #10; gpt-5.6-sol-xhigh поднимается до Agent #2.
//   Пять медиа-категорий НЕ обновлялись в окне — отсутствие движения там артефакт свежести данных.

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
  Agentic/Text/Vision: Claude Fable 5 #1 — но classifier FP → Opus 4.8 (точная доля НЕ опубликована;
                       ходившие «<5% сессий» и «на 85% реже у Opus 5» — вторичные, без методики)
  WebDev: kimi-k3 #1 (доступ ограничен) → claude-fable-5 → glm-5.2 как всегда-доступный путь
  Documents: claude-opus-4-6 #1 — старое поколение сильнее нового, «новее = лучше» здесь не работает
  Coding: Claude Opus 5 (PRIMARY) → Opus 4.8; Fable 5 силён в WebDev, но cost-gated
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
    claude-opus-5:      35%   // PRIMARY с 24.07; thinking on by default
    claude-opus-4-8:    25%   // ACTIVE, API-only surface
    claude-sonnet-5:    20%   // (было sonnet-4-6; дефолт сменился на Sonnet 5)
    qwen3.6-plus:       12%
    deepseek-v4-pro:    8%
    // claude-fable-5 выведен из автоматических весов: COST-GATED с 20.07 (usage credits),
    // допускается только по явному вызову оператора и с бюджетом

  REASONING:
    claude-opus-5:        35%  // PRIMARY
    gpt-5.6-terra:        28%  // (было gpt-5.5 → GPT-5.6); Sol не ставить в автопути
    gemini-3.1-pro:       22%
    claude-opus-4-8:      10%  // (было fable-5 — выведен, cost-gated)
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
    claude-sonnet-5:      10%  // (было sonnet-4-6; дефолт сменился на Sonnet 5)

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
  100K-500K: Claude Opus 5 / Opus 4.8 (1M native; G6 tokenizer ~+30% офиц. → считать Token Counting API)
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

FILE_META:
  ROLE:        Прайсинг, Arena ELO, routing matrix, context strategy, thinking budget, caching
  COMPATIBLE:  !!core_v8H.md | !!db_v8H.md | _live/live_vendors.md
