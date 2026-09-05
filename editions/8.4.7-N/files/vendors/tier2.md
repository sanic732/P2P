---
id: vendors_tier2_v8N
version: 8.4.7-N
type: VENDOR_PROFILE
tier: 2
priority: REFERENCE
compatible_with: "!!db_v8N.md | _live/live_vendors.md"
---

// ═══════════════════════════════════════════════════════
// P2P — VENDORS TIER 2
// Balanced: Claude Sonnet 4.6, Grok 4.3, DeepSeek V4-Pro, Qwen 3.6-Max
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. CLAUDE SONNET 4.6
// ─────────────────────────────────────────────────────

// ⚠ Sonnet 4.6 RETIRED 2026-06-30 как default → заменён CLAUDE SONNET 5 (см. tier1 §0c).
//   Для новых интеграций использовать claude-sonnet-5 ($2/$10, 1M). Ниже — legacy-справка.
CLAUDE_SONNET_46:
  api_string:     claude-sonnet-4-6
  status:         RETIRED 2026-06-30 (API-only legacy; не для новых интеграций)
  arena_elo:      1518
  context:        200K (нет G6 — нет tokenizer inflation)
  pricing:        legacy
  strengths:      Balanced performance; legacy fallback без G6 tokenizer-inflation
  arch:           XML_NATIVE

  KNOWN_ISSUES:
    G7: temperature + thinking → HTTP 400. (Общая Claude проблема)

  IDEAL_FOR:
    T1-T3 задачи. Лучший выбор при 160K-200K контексте (нет G6).
    Production workloads с умеренным бюджетом.
    Бесплатный доступ (май 2026) → идеальный для тестирования.

  THINKING_API:
    thinking: {type: "enabled", effort: "medium"}
    // НЕТ temperature при thinking (G7)

  DEADLINE:
    [PASSED 2026-06-15] Claude Sonnet dated legacy alias → claude-sonnet-4-6

// ─────────────────────────────────────────────────────
// §2. GROK 4.3
// ─────────────────────────────────────────────────────

GROK_45:  // NEW coding/agentic flagship — GA 2026-07-08 (см. также live_vendors CAPABILITY_MATRIX)
  api_string:     grok-4.5
  context:        500K | ~80 tps
  pricing:        short $2 in / $0.30 cached / $6 out per M — проверено у вендора
                  long (ОТ 200K): $4 in / $0.60 cached / $12 out per M — удваивается И КЭШ ТОЖЕ,
                  кэширование не смягчает; рычаг один — резать контекст (перехват 190K, обрыв 195K)
                  ⚠ унаследованная cache $0.50 НЕВЕРНА (лежит между $0.30 и $0.60 — грепать явно)
  reasoning:      ⚠ reasoning_effort HIGH по умолчанию, НЕ отключается; reasoning биллится как output
  ⚠ ФАНТОМЫ:      grok-4.5-heavy / -expert / -fast НЕ СУЩЕСТВУЮТ (единственный id — grok-4.5)
  strengths:      coding/agentic flagship, token-efficient, X Firehose
  guard:          EU-доступ открыт 21.07, но БЕЗ data-residency → персональные данные EU не пускать; grok-build default

GROK_43:
  api_string:     grok-4.3
  arena_elo:      1541
  context:        1M (для 2M-контекста → grok-4.20 Heavy, профиль в vendors/tier4.md)
  pricing:        $1.25/$2.50 per M
  strengths:      X.com real-time search, long context, reasoning

  KNOWN_ISSUES:
    G3: Topic drift. Anchor каждые 3 turn.
    G14: Unsupported params → HTTP 400 (hard fail, не silent).

  SAFE_PARAMS_ONLY: temperature, max_tokens, stream, top_p, stop
  BANNED_PARAMS: top_k, repetition_penalty, presence_penalty, logit_bias

  IDEAL_FOR:
    Real-time research (X/Twitter data), >200K context tasks.
    Topic anchoring required в длинных сессиях.

  TOPIC_ANCHOR_TEMPLATE:
    "[TOPIC ANCHOR: Исходная задача = {task_1_sentence}. Держись темы.]"
    Вставлять каждые 3 хода.

  SPECIAL_TAGS:
    [Tone: Expert]                  → факты, точные данные
    [Tone: Fun]                     → сатира, мемы, креатив
    [Require: Real-Time Verification] → принудительный X.com lookup
    [Perspective: Devil's Advocate] → оппозиционный анализ

// ─────────────────────────────────────────────────────
// §3. DEEPSEEK V4-PRO
// ─────────────────────────────────────────────────────

DEEPSEEK_V4_PRO:
  api_string:     deepseek-v4-pro
  arena_elo:      SWE-bench Verified 80.6%
  context:        1M | output: 384K
  pricing:        $0.435/$0.87 per M  (BUDGET POWERHOUSE)
  status:         ✅ GA 13.08.2026 для deepseek-v4-pro (чекпойнт 0813, веса MIT, нативный
                  OpenAI Responses API). deepseek-v4-flash-0731 — public beta, не GA.
                  Прежняя пометка «вся линейка V4 — Preview» опиралась на changelog
                  2026-04-24 и устарела (исправлено 8.4.7).
  strengths:      Native reasoning, очень дёшево, code quality

  KNOWN_ISSUES:
    G15: Reasoning carryover в multi-turn.
         Fix: re-inject reasoning_content (store+re-inject, НЕ обнулять) — RESOLVED BY DESIGN.
    G16: deepseek-chat/reasoner — ИСПОЛНЕНО 2026-07-24 15:59 UTC, без grace-периода.
         Точный HTTP-код первичными логами не подтверждён: 404 либо 400 invalid_request_error —
         обработчик должен принимать оба.
         ⚠ ЛОВУШКА: официальный маппинг вёл ОБА алиаса на deepseek-v4-flash. Нагрузку бывшего
         deepseek-reasoner вести на **deepseek-v4-pro**, НЕ на v4-flash-thinking — иначе reasoning
         тихо деградирует. У v4-flash thinking включён по умолчанию и не отключается.

  THINKING_API:
    Native reasoning (R1). Не управляется извне.
    temperature: 0.3 для reasoning режима.
    temperature: 0.7 для creative режима.

  MULTI_TURN_FIX:  # G15 prevention
    messages.append({
      "role": "assistant",
      "content": prev_response.content,
      "reasoning_content": prev_reasoning  # re-inject, НЕ null (v8.5)
    })

  IDEAL_FOR:
    Budget-conscious tasks, code generation, <64K context.
    Лучший ROI для T1-T2 coding задач.

// ─────────────────────────────────────────────────────
// §4. QWEN 3.6-MAX
// ─────────────────────────────────────────────────────

QWEN_36_MAX:
  api_string_dashscope:   qwen3-max
  api_string_openrouter:  qwen/qwen3-max
  arena_elo:              1498
  context:                128K (reliable), 32K (optimal)
  pricing:                $1.20/$3.60 per M
  strengths:              thinking_budget fine control, coding, vision (Qwen3-VL)

  KNOWN_ISSUES:
    G17: Provider prefix mismatch. DashScope ≠ OpenRouter format.
    G18: preserve_thinking needed for agentic tasks.

  THINKING_API:
    thinking_budget: 0        # отключён
    thinking_budget: 10000    # medium
    thinking_budget: 81920    # maximum

  PROVIDER_SYNTAX:  # G17
    DashScope:    "qwen3-max"           (без префикса)
    OpenRouter:   "qwen/qwen3-max"      (с qwen/)
    HuggingFace:  "Qwen/Qwen3-Max"      (с заглавной Q)

  AGENTIC_PARAMS:  # G18
    preserve_thinking: true   # для multi-step agentic задач

  IDEAL_FOR:
    Balanced quality/cost T2-3, OCR tasks (Qwen3-VL), coder variant available.

  ARCHITECTURE_NOTE:
    MoE 397B total / 17B active per token.
    Производительность ≠ количество параметров — задавай ожидания соответственно.
    Qwen3-VL OCR: 99.2% (best для text-in-image задач).
    LIBRARY_ANCHOR обязателен — иначе hallucinated методы в коде.

FILE_META:
  MODELS:      Claude Sonnet 4.6, Grok 4.3, DeepSeek V4-Pro, Qwen 3.6-Max
  COMPATIBLE:  !!db_v8N.md | _live/live_vendors.md
