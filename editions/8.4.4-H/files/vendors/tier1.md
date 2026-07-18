---
id: vendors_tier1_v8H
version: v8H.3
type: VENDOR_PROFILE
tier: 1
priority: REFERENCE
compatible_with: "!!db_v8H.md | _live/live_vendors.md"
last_verified: 2026-07-13
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — VENDORS TIER 1
// Flagship models: Claude Fable 5, Claude Opus 4.8, Claude Opus 4.7 (legacy),
//                  GPT-5.5, Gemini 3.1 Pro
// ═══════════════════════════════════════════════════════
// OVERRIDE: live_specs > live_vendors.md > этот файл при конфликтах.

// ─────────────────────────────────────────────────────
// §0. CLAUDE FABLE 5  (NEW — v8.4, debut 2026-06-10)
// ─────────────────────────────────────────────────────

CLAUDE_FABLE_5:
  api_string:     claude-fable-5
  arena_elo:      Overall/Text/Vision #1; Agent Net Improvement #1 (14.10%)
  context:        1M | output: 128K
  pricing:        $10/$50 per M in/out (cache 90% off input); 50%-weekly include до 19.07 → usage credits
  strengths:      Frontier: Overall/Text/Vision #1, agentic workflows, high-quality text
  arch:           XML_NATIVE (на Claude-хосте); host-gated для генерации под другие модели
  thinking:       {"type":"adaptive"} | effort low|medium|high|xhigh|max (НЕ temperature при thinking — G7)

  KNOWN_ISSUES:
    CLASSIFIER_FP: safety-classifier даёт FP на security/coding → ~5% сессий молча на Opus 4.8 (UNRESOLVED BY DESIGN).
                  → для гарантии модели пинить claude-opus-4-8; security/pentest → сразу Opus 4.8.
    G7: temperature + thinking → HTTP 400 (как у всей линейки Claude).

  WHEN_TO_USE:
    T3-T4 agentic, frontier, высококачественный текст/vision; первый выбор для QUORUM-оркестрации.
    Fallback chain: claude-fable-5 → claude-opus-4-8 → claude-sonnet-5

// ─────────────────────────────────────────────────────
// §0b. CLAUDE OPUS 4.8  (NEW — v8.4)
// ─────────────────────────────────────────────────────

CLAUDE_OPUS_48:
  api_string:     claude-opus-4-8
  arena_elo:      Code top-tier; SWE-bench Pro 69.2%
  context:        1M | output: 128K
  pricing:        $5/$25 per M in/out
  strengths:      Coding (primary), reasoning; GraphWalks F1 1M: 68.1% (+27.8pp vs 4.7)
  arch:           XML_NATIVE
  thinking:       {"type":"adaptive"} | effort low|medium|high|xhigh|max

  KNOWN_ISSUES:
    G7: temperature + thinking → HTTP 400. Delete temperature from payload.
    G8: MRCR v2 1M = 32.2% (vs 78.3% Opus 4.6). Pin claude-opus-4-6 for >500K recall.

  WHEN_TO_USE:
    Coding/reasoning primary; стабильный выбор когда Fable 5 classifier-FP нежелателен.
    НЕ для: >500K recall (→ Opus 4.6).

// ─────────────────────────────────────────────────────
// §0c. CLAUDE SONNET 5  (NEW — default Free/Pro, GA 2026-06-30)
// ─────────────────────────────────────────────────────

CLAUDE_SONNET_5:
  api_string:     claude-sonnet-5
  context:        1M | output: 128K (300K batch)
  pricing:        $2/$10 (intro до 2026-08-31) → $3/$15 (c 01.09)
  strengths:      near-Opus-4.8 качество, дёшево; Tier 3 default для cost-efficient agentic
  arch:           XML_NATIVE
  thinking:       {"type":"adaptive"} | effort low|medium|high|xhigh|max

  KNOWN_ISSUES:
    G6: общий токенизатор (+30-42% на англ. прозе). G7: temperature + thinking → HTTP 400.

  WHEN_TO_USE:
    Баланс цена/качество T2-T3, cost-efficient agentic; заменил RETIRED Sonnet 4.6 как default.

// ─────────────────────────────────────────────────────
// §1. CLAUDE OPUS 4.7  (legacy flagship)
// ─────────────────────────────────────────────────────

CLAUDE_OPUS_47:
  api_string:     claude-opus-4-7
  arena_elo:      Vision #2-thinking; Code strong
  context:        1M | output: 128K
  pricing:        $5/$25 per M in/out
  strengths:      Coding (SWE-bench 72.5%), reasoning, complex tasks
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

GPT_56:  // GPT-5.6 Sol/Terra/Luna — PUBLIC GA 2026-07-09 (superseded GPT-5.5 как флагман)
  api_string:     gpt-5.6-sol (alias gpt-5.6) | gpt-5.6-terra | gpt-5.6-luna
  arena_elo:      Sol WebDev #1 (codex-harness); Overall #8
  context:        1.05M | output: 128K | cutoff: 2026-02-16
  pricing:        Sol $5/$30 (cache $0.50) | Terra $2.50/$15 | Luna $1/$6
  strengths:      Sol flagship code/agentic (Terminal-Bench 88.8%); Terra balanced; Luna cheap/fast
  legacy:         gpt-5.5 / gpt-5.5-pro ($30/$180) остаются для Codex computer_use

  KNOWN_ISSUES:
    G9: >7 MUST/MUST NOT pairs → silent quality downgrade.
    G10: >272K input → 2x input / 1.5x output на всю сессию (BY DESIGN; 5.4/5.5/5.6).
    SOL_REWARD_HACKING: METR flag — не доверять headline-бенчам Sol без верификации (MONITORING).
    LUNA_MRCR: collapse >512K — не для deep long-doc.

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
  api_string:     gemini-3.1-pro-preview
  arena_elo:      Search #6 (grounding); Text strong
  context:        2M (reliable up to 500K)
  pricing:        $2/$12 per M (≤200K)
  strengths:      Long context (2M), Google Search native, multimodal
  NOTE:           Gemini 3.5 Pro (gemini-3.5-pro-preview, 2M) — всё ещё PREVIEW (не GA); НЕ трактовать как GA.

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
  SYSTEM:      P2P v8H.3 · Vendors Tier 1
  MODELS:      Claude Fable 5, Sonnet 5, Opus 4.8, Opus 4.7, GPT-5.6 Sol/Terra/Luna, Gemini 3.1 Pro
  SOURCE:      _live/live_specs.md (v8.6.3)
  COMPATIBLE:  !!db_v8H.md | _live/live_vendors.md
