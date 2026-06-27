---
id: vendors_tier1_v8N
version: v8N.3
type: VENDOR_PROFILE
tier: 1
priority: REFERENCE
compatible_with: "!!db_v8N.md | _live/live_vendors.md"
last_verified: 2026-06-27
---

// ═══════════════════════════════════════════════════════
// P2P v8N.3 — VENDORS TIER 1
// Flagship models: Claude Fable 5, Claude Opus 4.8, Claude Opus 4.7 (legacy),
//                  GPT-5.5, Gemini 3.1 Pro
// ═══════════════════════════════════════════════════════
// OVERRIDE: live_specs > live_vendors.md > этот файл при конфликтах.

// ─────────────────────────────────────────────────────
// §0. CLAUDE FABLE 5  (NEW — v8.4, debut 2026-06-10)
// ─────────────────────────────────────────────────────

CLAUDE_FABLE_5:
  api_string:     claude-fable-5
  arena_elo:      1665 (WebDev #1); Text #1 = 1510; Agent #1 = 12.94%
  context:        200K
  pricing:        $10/$50 per M in/out
  strengths:      Agentic workflows (#1), WebDev (#1), text quality (#1)
  arch:           XML_NATIVE (на Claude-хосте); host-gated для генерации под другие модели
  thinking:       effort: low|medium|high (НЕ temperature при thinking — G7)

  KNOWN_ISSUES:
    SAFETY_NANNY: ~5% сессий молча перенаправляются на Opus 4.8 (UNRESOLVED BY DESIGN).
                  → для гарантии модели пинить claude-opus-4-8; держать Opus 4.8 в fallback.
    G7: temperature + thinking → HTTP 400 (как у всей линейки Claude).

  WHEN_TO_USE:
    T3-T4 agentic, WebDev, высококачественный текст; первый выбор для QUORUM-оркестрации.
    Fallback chain: claude-fable-5 → claude-opus-4-8 → claude-sonnet-4-6

// ─────────────────────────────────────────────────────
// §0b. CLAUDE OPUS 4.8  (NEW — v8.4)
// ─────────────────────────────────────────────────────

CLAUDE_OPUS_48:
  api_string:     claude-opus-4-8
  arena_elo:      1583 (Code #1)
  context:        200K
  pricing:        $15/$75 per M in/out
  strengths:      Coding (#1), reasoning; GraphWalks F1 1M: 68.1% (+27.8pp vs 4.7)
  arch:           XML_NATIVE
  thinking:       effort: low|medium|high

  KNOWN_ISSUES:
    G7: temperature + thinking → HTTP 400. Delete temperature from payload.
    G8: MRCR v2 1M = 32.2% (vs 78.3% Opus 4.6). Pin claude-opus-4-6 for >500K recall.

  WHEN_TO_USE:
    Coding/reasoning флагман; стабильный выбор когда Fable 5 Safety Nanny нежелателен.
    НЕ для: >500K recall (→ Opus 4.6).

// ─────────────────────────────────────────────────────
// §1. CLAUDE OPUS 4.7  (legacy flagship)
// ─────────────────────────────────────────────────────

CLAUDE_OPUS_47:
  api_string:     claude-opus-4-7
  arena_elo:      1571 (Code #1)
  context:        200K (effective 160K — G6 inflation)
  pricing:        $15/$75 per M in/out
  strengths:      Coding (#1 SWE-bench 72.5%), reasoning, complex tasks
  arch:           XML_NATIVE
  thinking:       effort: low|medium|high
  swe_bench:      72.5%

  KNOWN_ISSUES:
    G6: Tokenizer inflation +10-35% vs Opus 4.6. Plan for 160K effective max.
    G7: temperature + thinking → HTTP 400. Delete temperature from payload.
    G8: MRCR 32.2% at 1M (vs 78.3% Opus 4.6). Pin 4.6 for >500K recall tasks.

  IDEAL_PROMPTS:
    XML структура: <role>, <rules>, <task>, <output_format>
    Contract pairs: кажый MUST парный MUST NOT
    Prefilling доступен (API): установи assistant turn
    Максимум 200K system + user + context combined

  THINKING_API:
    // ПРАВИЛЬНО:
    thinking={type: "enabled", effort: "medium"}
    // НЕТ temperature при thinking
    // НЕТ budget_tokens (удалён из API)

  CONTEXT_CACHE:
    Условие: system prompt > 1024 токенов
    Method: cache_control: {type: "ephemeral"} (TTL 5 мин)
    Savings: ~90% повторных system prompt costs

  WHEN_TO_USE:
    T3-T4 задачи, кодинг, complex reasoning, production prompts
    НЕ для: >500K recall (→ Opus 4.6), >160K context тяжёлые задачи (→ Sonnet 4.6)

  DEADLINE:
    [PASSED 2026-06-15] Claude dated legacy alias → claude-opus-4-8 / claude-opus-4-7

// ─────────────────────────────────────────────────────
// §2. GPT-5.5
// ─────────────────────────────────────────────────────

GPT_55:
  api_string:     gpt-5.5
  arena_elo:      1563
  context:        128K (pricing jump >272K — G10)
  pricing:        $7/$28 per M (<272K), $14/$56 per M (>272K)
  strengths:      Reasoning, function calling, JSON schema

  KNOWN_ISSUES:
    G9: >7 MUST/MUST NOT pairs → silent quality downgrade.
    G10: Pricing jump above 272K input tokens.

  IDEAL_PROMPTS:
    JSON preferred over XML
    reasoning_effort: medium (вместо effort)
    response_format: {type: "json_object"} для JSON
    Max 7 MUST + 7 MUST NOT

  THINKING_API:
    reasoning_effort: low|medium|high

  RULE_LIMIT: 7 пар максимум (G9)
  TOKEN_LIMIT: <272K для нормального ценообразования (G10)

  DEADLINE:
    [PASSED 2026-06-05] gpt-5.x legacy aliases → gpt-5.5

// ─────────────────────────────────────────────────────
// §3. GEMINI 3.1 PRO
// ─────────────────────────────────────────────────────

GEMINI_31_PRO:
  api_string:     gemini-3.1-pro-latest
  arena_elo:      1549
  context:        1M (reliable up to 500K)
  pricing:        $3.50/$10.50 per M (base)
  strengths:      Long context, Google Search native, multimodal

  KNOWN_ISSUES:
    G1: Deep Think + temperature ≠ 1.0 → HTTP 400.
    G2: XML tags → Chain-of-Hint interference. ZERO XML required.
    G4: thinking_budget ignored. Use thinkingLevel instead.
    G11: thinkingLevel=HIGH без Value Gate → billing shock ($50/M).
    G12: Hard rate limit (429). Use Flash for high-frequency.
    G13: Memory nuke after ~80 messages. Reinject every 25.

  IDEAL_PROMPTS:
    ## Markdown headers вместо XML тегов
    **Bold** для важного
    Plain text sections
    ZERO XML — никаких <role>, <rules>, <task> тегов

  THINKING_API:
    thinkingConfig: {thinkingLevel: "MEDIUM"}  // не thinking_budget!
    temperature: 1.0 при Deep Think (или удали temperature — G1)

  SYNTAX_EXAMPLE:
    ## Role
    Ты — эксперт по [domain].

    ## Task
    [задача]

    ## Rules
    MUST: [правило 1]
    MUST NOT: [ограничение 1]

    ## Output Format
    [формат]

  REINJECTION: каждые 25 сообщений (G13 prevention)

  WHEN_TO_USE:
    >200K context, research с Google Search, multimodal tasks
    НИКОГДА: XML промпты (G2 — качество падает ниже baseline)

  BENCHMARKS:
    GPQA: 94.3% | ARC-AGI-2: 77.1% | BrowseComp: 85-86% | LMSYS Elo: ~1505

  CINE_PROMPTING (Veo / video generation):
    Использовать киношные термины: Dolly Zoom, Volumetric lighting,
    Anamorphic flare, Rack focus, Crane shot, Dutch angle.
    Pattern: [Subject] + [Camera move] + [Lighting] + [Lens/Style]

VERSION_METADATA:
  SYSTEM:      P2P v8N.3 · Vendors Tier 1
  MODELS:      Claude Fable 5, Claude Opus 4.8, Claude Opus 4.7 (legacy), GPT-5.5, Gemini 3.1 Pro
  SOURCE:      _live/live_specs.md (v8.6.1)
  COMPATIBLE:  !!db_v8N.md | _live/live_vendors.md
