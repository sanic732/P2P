---
id: db_v8L
version: v8L.3-BETA
type: KNOWLEDGE_BASE
priority: CRITICAL
load_order: 4
compatible_with: "!!core_v8L.md | _index_v8L.md | all v8L files"
last_verified: 2026-06-17
---

// ═══════════════════════════════════════════════════════════════
// P2P v8L.3 — KNOWLEDGE BASE (Lite/Live Hybrid)
// RU: Техники, G-ошибки, A-P, QUORUM-веса, API strings + LITE_SNAPSHOT (offline).
// EN: Techniques, G-errors, A-P, QUORUM weights, API strings + LITE_SNAPSHOT (offline).
// Порт из db_v8H. Добавлено: §0 LITE_SNAPSHOT (DEGRADE fallback), §2b COMBINATOR disambig.
// ═══════════════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §0. LITE_SNAPSHOT (NEW v8L — DEGRADE fallback при LOAD_MODE=LITE_ONLY)
// RU: Минимальный срез критичных live-данных, чтобы офлайн система не слепла.
// EN: Minimal slice of critical live data so an offline system isn't blind.
// На него ссылается core §12 (DEADLINE_SCANNER) и §10 (RESOURCE_STRATEGY) когда gist_live недоступен.
// FRESHNESS: snapshot от 2026-06-17. Если онлайн — gist_live ПЕРЕЗАПИСЫВАЕТ эти значения.
// ─────────────────────────────────────────────────────

LITE_SNAPSHOT:
  AS_OF: 2026-06-17
  DEADLINES:
    [PASSED 2026-06-15] Claude dated legacy aliases retired (HTTP 400/404)
    [PASSED 2026-06-05] gpt-5.x legacy → gpt-5.5
    [ACTIVE 2026-07-24] deepseek-chat → deepseek-v4-pro ; deepseek-reasoner → deepseek-v4-flash
  CURRENT_FLAGSHIPS:
    claude: claude-fable-5 (Arena #1 Agent), claude-opus-4-8 (coding #1), claude-sonnet-4-6
    gpt: gpt-5.5  · gemini: gemini-3.1-pro-latest · grok: grok-4.3
    deepseek: deepseek-v4-pro · qwen: qwen3-max · kimi: moonshot-v2-128k · glm: glm-5.1-flash
  WARN: "⚠ LITE_SNAPSHOT — данные на 2026-06-17, могут устареть. Для свежих ELO/цен нужен fetch (gist_live)."

// ─────────────────────────────────────────────────────
// §1. KNOWLEDGE ARCHITECTURE
// ─────────────────────────────────────────────────────

KNOWLEDGE_LAYERS:
  STATIC:    CTCO, DoD, Contract Compliance, 30/55/15 rule, ARENA methodology (immutable).
  DYNAMIC:   #LINK_* → gist_vendors (tier1-4, claude, grok). #LINK_LIVE → gist_live (OVERRIDE).
             PRIORITY: gist_live > gist_vendors > db defaults. FRESHNESS >60d → DATOS Deep Search.
  EMPIRICAL: ARENA результаты, ARENA_SCORE per technique.

// ─────────────────────────────────────────────────────
// §2. PROMPT ENGINEERING TECHNIQUES (38 техник)
// ─────────────────────────────────────────────────────

TECHNIQUES:
  // ── BASIC ──
  ELI5:            Объясни просто. Prefix "ELI5:". Universal. 92/100.
  STEP_BY_STEP:    По шагам. GPT/Claude OK. ЗАПРЕЩЕНО для R1/o3/Gemini Deep Think/Kimi Thinking
                   (деградирует нативный reasoning). 93/100 train, 45/100 reasoning.
  TLDR:            Краткое резюме. Universal. 85/100.
  CHECKLIST:       Структурная валидация. QA, DoD. Universal. 87/100.
  DEVILS_ADVOCATE: Анализ слабых мест. Claude, GPT. 90/100.
  SOCRATIC_METHOD: 3-7 уточняющих вопросов перед ответом. Universal. 86/100.
  BRANCHING_LOGIC: 3-5 альтернативных подходов. Universal. 85/100.
  // ── STRUCTURAL ──
  PREFILLING:      Claude API: prefill assistant turn. 91/100.
  CLAUDE_MD:       Persistent memory via CLAUDE.md. Claude optimal. 94/100.
  LIBRARY_ANCHOR:  Version lock для библиотек. Universal. 89/100.
  CTCO:            Context-Task-Constraints-Output. GPT optimal. 90/100.
  CONTEXT_COMPRESSION: Сжатие тяжёлого контекста перед мержем. 88/100.
  ANCHOR_CONTEXT:  Повтор ключевых инструкций на границах документа. 90/100.
  LATE_CHUNKING:   100K блоки для Gemini. Gemini optimal. 91/100.
  // ── SAFETY & QUALITY ──
  GASLIGHT_SAFE:   Honesty mode: строгое разделение факт/гипотеза. 91/100.
  SAFE_THINKING:   Токен [SECURITY_CHECK] между шагами рассуждения. 92/100.
  LLM_COUNCIL:     Multi-model верификация через консенсус. 96/100.
  EXCELLENT:       Обход over-refusal: Defensive Framing, Objective Abstraction, Clinical Tone.
                   Обязателен для Claude 4.x и Gemini 3.1 Pro.
  // ── AGENTIC ──
  AGENT_SWARM:     До 100 sub-agents, параллельно. Kimi K2.x leader. 89/100.
  TOOL_BUDGET:     MAX_TOOL_CALLS + stop conditions. Kimi/Gemini. 95/100.
  VISUAL_AGENTIC:  Код из изображений/мокапов. Kimi/Gemini/Qwen3-VL. 91/100.
  FRESHNESS_PROTOCOL: Спрашивать разрешение перед допущениями. 88/100.
  // ── ADVANCED ──
  STRUCTURED_DECOMP: Разбивка на sub-prompts с явным handoff. Universal. 93/100.
  RAG_GROUNDING:   "Отвечай ТОЛЬКО из предоставленного контекста." Claude optimal. 94/100.
  PERSONA_CASCADE: Цепочка ролей: Role A → Role B. BANNED для R1/Kimi Thinking. 88/100.
  REFLECTION_LOOP: Сгенерировать → Критиковать → Переписать. Только Tier 2+. 90/100.
  GATE_PATTERN:    Сначала классифицировать, потом роутить. Universal. 91/100.
  SCAFFOLD_PATTERN: Сначала outline, потом заполнить по секциям. 89/100.
  ADVERSARIAL_PAIR: [GENERATOR] создаёт → [CRITIC] критикует → фикс. 92/100.
  MCP_TOOL_PROMPT: Budget + error handling + stop conditions. Claude/GPT/Kimi. 95/100.
  MIGRATION_TRANSFORM: Правила адаптации кросс-модельных промптов. 96/100.
  // ── META ──
  PLACEMENT_RULES:
    Reasoning models: НИКОГДА не форсировать теги для CoT. Формат только в OUTPUT.
    STEP_BY_STEP: Gemini/R1/Kimi Thinking = запрещён в reasoning.
  COMBINATOR:
    Цепочки техник. Конфликт: IF reasoning_model + STEP_BY_STEP → BLOCK. Высший ARENA_SCORE побеждает.

// ─────────────────────────────────────────────────────
// §2b. TECHNIQUE_COMBINATOR — disambiguation (на него ссылается core §11 / agents FABRICATION_SCAN)
// RU: P2P-техники, которые НЕЛЬЗЯ блокировать как фабрикации.
// ─────────────────────────────────────────────────────

TECHNIQUE_COMBINATOR:
  DO_NOT_BLOCK (это легитимные техники, не фабрикации):
    Self-Consistency (SC, Wang 2023)  ≠ Universal Self-Consistency (USC) — SC разрешён.
    MCTS (algorithmic search)          ≠ Tree-of-Thought forcing — MCTS разрешён (gist_reasoning).
    RAPTOR / LongRAG (retrieval)       ≠ Graph-of-Thought — разрешены (gist_rag).
  RULE: ANON/VECTOR ОБЯЗАН свериться с этим блоком до VETO любой reasoning/rag техники.

// ─────────────────────────────────────────────────────
// §3. ERROR CLASSIFICATION (A-P, 16 типов)
// ─────────────────────────────────────────────────────

ERRORS_AP:
  A. Silent timeout:  Кредиты сняты, нет ответа. Fix: уменьши thinking, чанки.
  B. Mid-stop:        Останавливается 50-90%. Fix: chunking, continuation points.
  C. Truncation:      Обрезан молча ~90%. Fix: max_tokens, ручной chunking.
  D. Long drift:      Качество падает в середине. Fix: ANCHOR_CONTEXT, semantic chunking.
  E. Context Drift:   Забывает инструкции. Fix: повтор constraints, Document Map.
  F. Gemini drift:    ~9% после 50+ сообщений. Fix: CLAUDE_MD, CONSTRAINT_REINJECTION.
  G. Agent Self-revert: Kimi откатывает изменения. Fix: checkpoint перед записью.
  H. Tool Confusion:  Смешивает JSON/XML. Fix: один формат на сессию.
  I. Overthinking:    Kimi Thinking на простых. Fix: thinking:off для T0-1.
  J. Zero-State:      Placeholder в выводе. Fix: ZERO_STATE_IMMUNITY.
  K. Topic drift (Grok): Не тот вопрос. Fix: topic anchor каждые 3 turn.
  L. Silent Degradation: Claude звучит обобщённо. Fix: /clear + острее промпт.
  M1. Correction Loop: 3+ одинаковых коррекции. Fix: /clear + переписать.
  M2. Kitchen Sink:   Слишком много файлов. Fix: аудит, убрать лишнее.
  M3. Infinite Explore: Исследование заполняет контекст. Fix: ограничение scope.
  N. Hallucinated Tool: Изобретает tools/params. Fix: дефиниции в primacy, max 7 tools.
  O. Safety Over-Refusal: Отказ от легитимного. Fix: EXCELLENT, professional context.
  P. Format Oscillation: Переключает формат. Fix: format lock в primacy AND recency.

// ─────────────────────────────────────────────────────
// §4. G-ERRORS CATALOG (G1-G20) — model-specific. Full spec → gist_live.
// ─────────────────────────────────────────────────────

G_ERRORS:
  G1  GEMINI_DEEP_THINK_TEMP   Gemini 3.1 Pro · HTTP 400 · Deep Think + temp≠1.0 · Fix: temperature 1.0 / убрать.
  G2  GEMINI_XML_COH           Gemini · Quality BLOCKER · XML → Chain-of-Hint · Fix: ZERO XML, plain text.
  G3  GROK_TOPIC_DRIFT         Grok 4.3 · Отвечает не на тот вопрос · Fix: topic anchor /3 turn.
  G4  GEMINI_THINKING_BUDGET   Gemini 3.1 Pro · thinking_budget игнорируется · Fix: thinkingLevel "MEDIUM".
  G6  OPUS47_TOKENIZER_INFL    Opus 4.7 · контекст быстрее · +10-35% inflation · Fix: 160K effective.
  G7  CLAUDE_THINKING_TEMP     Opus 4.7/Sonnet 4.6 · HTTP 400 · temp при thinking=enabled · Fix: убрать temperature.
                               // OK: {"model":"claude-opus-4-7","thinking":{"type":"enabled","effort":"medium"}}
                               // BAD (400): {"thinking":{"type":"enabled"},"temperature":0.7}
  G8  OPUS47_MRCR_REGRESSION   Opus 4.7 · плохой recall >500K (MRCR 32.2%@1M) · Fix: пин claude-opus-4-6.
  G9  GPT55_SILENT_DOWNGRADE   GPT-5.5 · >7 MUST/MUST NOT пар → downgrade · Fix: макс 7 пар.
  G10 GPT55_PRICING_TRAP       GPT-5.5 · pricing jump >272K · Fix: <272K, иначе Gemini 3.1 Pro.
  G11 GEMINI_HIGH_BILLING      Gemini 3.1 Pro · thinkingLevel=HIGH без gate · Fix: DEEP_THINK_VALUE_GATE.
  G12 GEMINI_HARD_429          Gemini 3.1 Pro · HTTP 429 без retry · Fix: high-freq → Flash.
  G13 GEMINI_MEMORY_NUKE       Gemini 3.1 Pro · забывает после ~80 сообщений · Fix: REINJECT каждые 25.
  G14 GROK_UNSUPPORTED_PARAM   Grok 4.3 · HTTP 400 · Fix: safe params only (temp/max_tokens/stream/top_p/stop).
  G15 DEEPSEEK_REASONING_CARRY DeepSeek V4 · загрязнение reasoning · Fix: re-inject reasoning_content (НЕ null) — RESOLVED BY DESIGN.
  G16 DEEPSEEK_ALIAS_RETIRE    ★DEADLINE 2026-07-24 · Fix: deepseek-v4-pro / deepseek-v4-flash.
  G17 QWEN_PROVIDER_PREFIX     Qwen 3.6 · HTTP 404 · Fix: DashScope qwen3-plus / OpenRouter qwen/qwen3-plus.
  G18 QWEN_PRESERVE_THINKING   Qwen 3.6 agentic · thinking теряется · Fix: preserve_thinking: true.
  G19 GLM_CONTEXT_COLLAPSE     GLM-5.1 · деградация >100K · Fix: hard limit 100K.
  G20 KIMI_SWARM_TIMEOUT       Kimi K2.x · timeout >1h via REST · Fix: >40 агентов → async webhooks.

G_ERRORS_QUICK_REF:
  CRITICAL: G1, G2(BLOCKER), G7, G14, G16, G19
  HIGH:     G3, G9, G10, G11, G13, G20
  MEDIUM:   G4, G6, G8, G12, G15, G17, G18

// ─────────────────────────────────────────────────────
// §5. API STRINGS (актуальные; OVERRIDE из gist_live при онлайне)
// ─────────────────────────────────────────────────────

API_STRINGS:
  CLAUDE:
    claude-fable-5            ← рекомендован (Tier 3-4, #1 Agent/WebDev)
    claude-opus-4-8           ← рекомендован (Tier 3-4, coding #1)
    claude-opus-4-7           ← legacy флагман (Tier 3-4)
    claude-sonnet-4-6         ← рекомендован (Tier 1-3)
    claude-haiku-4-5-20251001 ← Tier 0-1, бюджет
    claude-opus-4-6           ← пин для >500K recall (G8)
    [PASSED 2026-06-15]: Claude dated legacy aliases retired (в реестре отсутствуют).
  GPT:      gpt-5.5 | gpt-5.5-mini | gpt-5.5-turbo  [PASSED 2026-06-05: legacy → gpt-5.5]
  GEMINI:   gemini-3.1-pro-latest | gemini-3.1-flash-latest
  GROK:     grok-4.3 | grok-4.3-mini
  DEEPSEEK: deepseek-v4-pro | deepseek-v4-flash
            [RETIRE 2026-07-24]: deepseek-chat → deepseek-v4-pro ; deepseek-reasoner → deepseek-v4-flash
  QWEN:     DashScope qwen3-max|qwen3-plus|qwen3-coder-plus | OpenRouter qwen/qwen3-plus (G17)
  KIMI:     moonshot-v2-128k | moonshot-v2-8k
  GLM:      glm-5.1-flash (MIT, ≤100K)

// ─────────────────────────────────────────────────────
// §6. DYNAMIC WEIGHTING (QUORUM) — используется gist_core_plus (agents)
// ─────────────────────────────────────────────────────

QUORUM_WEIGHTS:
  CODING:     TECTON 35%, ANON 25%, AXIOM 15%, VECTOR 15%, DATOS 5%, IRIS 5%
  CREATIVE:   IRIS 40%, TECTON 15%, ANON 15%, AXIOM 10%, VECTOR 10%, DATOS 10%
  RESEARCH:   DATOS 40%, IRIS 20%, TECTON 20%, AXIOM 10%, VECTOR 5%, ANON 5%
  ANALYTICAL: AXIOM 35%, DATOS 25%, TECTON 20%, IRIS 10%, VECTOR 5%, ANON 5%
  SECURITY:   VECTOR 40%, TECTON 20%, AXIOM 20%, ANON 10%, DATOS 5%, IRIS 5%
  FRONTIER:   AXIOM 35%, DATOS 25%, TECTON 20%, VECTOR 15%, IRIS 5%
  WRITING:    IRIS 35%, TECTON 20%, AXIOM 15%, DATOS 15%, ANON 10%, VECTOR 5%
  VETO: VECTOR — абсолютное право вето на [CRITICAL_RISK]. IF triggered → веса=0 → Audit Mode.

// ─────────────────────────────────────────────────────
// §7. MODEL RECOMMENDATIONS (стратегия; цифры — gist_live)
// ─────────────────────────────────────────────────────

RECOMMENDATIONS:
  CODING: Claude Opus 4.8, Qwen3-Coder, Kimi K2.x · REASONING: Opus 4.7, GPT-5.5 Thinking, Gemini Deep Think
  CREATIVE: Claude Fable 5, Opus 4.7, GPT-5.5 · RESEARCH: Gemini 3.1 Pro, Grok 4.3
  VISION: Qwen3-VL, Gemini 3.1 Pro · AGENTS: Claude Fable 5, Kimi K2.x, Opus 4.8 (Computer Use)
  BUDGET: DeepSeek V4-Flash, GLM-5.1 · LONG_CTX: Gemini 1M, Grok 2M · RECALL: Opus 4.6 pin (>500K, G8)

// ─────────────────────────────────────────────────────
// §8. CHAIN PATTERNS
// ─────────────────────────────────────────────────────

CHAIN_PATTERNS:
  RESEARCH_DRAFT_REVIEW: Research(Gemini/Grok)→Draft(Claude/GPT)→Review(GPT/R1)→Polish(Sonnet)
  CODE_PIPELINE:         Arch(Opus)→Impl(Sonnet/Qwen-Coder)→Test(GPT/R1)→Security(Opus VECTOR)
  CROSS_VALIDATE:        Same prompt → A + B → C judge (Gemini 3.1 Pro / Opus 4.7)
  HANDOFF_RULE:          Каждый шаг самодостаточен. Никогда не ссылайся на "предыдущий промпт".

// ─────────────────────────────────────────────────────
// §9. ARENA VERIFICATION (логика расширена в gist_session)
// ─────────────────────────────────────────────────────

ARENA:
  TRIGGER: "A/B тест|compare|Arena|Tier 2+"
  WORKFLOW: 1.core task+constraints 2.выбрать 2-3 модели 3.model-specific промпты 4.TRAP MARKERS 5.критерии.
  TRAP_MARKERS: Logical | Formatting(XML греческий) | Negative(без чисел) | Contextual(фраза в середине) | Agentic(50 calls) | Contract(MUST без пары).
  OUTPUT: ## ARENA CALIBRATION PAYLOAD (Task, Target A/B prompts, Evaluation Matrix, Red Flags).

// ─────────────────────────────────────────────────────
// §10. FEEDBACK LOOP
// ─────────────────────────────────────────────────────

FEEDBACK_LOOP:
  TRIGGER: "не работает|fix prompt|работает частично"
  STEP1 DIAGNOSE: тип ошибки (A-P). STEP2 LOCATE: раздел промпта. STEP3 PATCH: хирургич. diff БЫЛО→СТАЛО.
  STEP4 VERIFY: перетест; та же ошибка ×3 → /clear + полная перезапись.
  ANTI: не переписывать весь промпт при первом сбое; 80% сбоев — промпт, не модель.

// ─────────────────────────────────────────────────────
// §11. MENTOR METHOD (basics)
// ─────────────────────────────────────────────────────

MENTOR_METHOD:
  STAGES: 1.ZERO→PROMPT(NANO RTF) 2.STRUCTURED(CO-STAR/RISEN) 3.ENGINEERED(11-step+ARENA) 4.ORCHESTRATOR(QUORUM/chains).
  COMMON_MISTAKES: нет роли · CoT для reasoning models · нет output format · коррекция вместо рестарта (M1) · нет negative constraints.

// ─────────────────────────────────────────────────────
// §12. GROK HEAVY FAILURE MODES (Type B/H/T/X/V) — при HOST_MODEL=grok
// ─────────────────────────────────────────────────────

GROK_HEAVY_FAILURE_MODES:
  Type B — Tool Forgetting (most common): после 12-18 calls агенты игнорируют правила. Fix: стоп→re-inject 5 правил→бюджет -30%→форс AXIOM. Prevention: re-inject @8.
  Type H — JSON Confusion: JSON вперемешку с prose. Fix: «Output ONLY JSON» ×2 (primacy+recency), до 8 агентов.
  Type T — Heavy Throttling: 16→8/4 без предупреждения. Fix: лог в metrics, продолжить с 12; старт @12-14.
  Type X — X Firehose Cost: дорогой low-value запрос. Fix: $0.50 value gate; история >48h → web_search.
  Type V — Tool Result Verify Failed: результат противоречит контексту. Fix: AXIOM+VECTOR cross-verify.

// ─────────────────────────────────────────────────────
VERSION_METADATA:
  SYSTEM:      DB_v8L · P2P v8L.3 Lite/Live Hybrid Knowledge Base
  CONTENT:     LITE_SNAPSHOT (offline fallback), Techniques(38), COMBINATOR disambig,
               Errors A-P(16), G1-G20, Grok Heavy(B/H/T/X/V), Arena, Chains, Feedback, API strings, QUORUM weights
  COMPATIBLE:  !!core_v8L | _index_v8L | gist_core_plus | gist_live
  NEW_IN_v8L3: §0 LITE_SNAPSHOT для DEGRADE-fallback (LITE_ONLY mode)
  API_STRINGS: claude-fable-5, claude-opus-4-8, claude-opus-4-7, claude-sonnet-4-6
// EOF_MARKER_DB_V8L_VALIDATED
