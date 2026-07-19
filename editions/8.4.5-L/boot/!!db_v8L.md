---
id: db_v8L
version: v8L.4
type: KNOWLEDGE_BASE
priority: CRITICAL
load_order: 4
compatible_with: "!!core_v8L.md | _index_v8L.md | all v8L files"
last_verified: 2026-07-18
---

LITE_SNAPSHOT:
  AS_OF: 2026-07-13
  DEADLINES:
    [PASSED 2026-06-15] Claude dated legacy aliases retired
    [PASSED 2026-06-30] claude-sonnet-4-6 RETIRED → claude-sonnet-5
    [ACTIVE 2026-07-19] Fable 5: конец 50%-weekly include → usage credits
    [ACTIVE 2026-07-24 15:59 UTC] deepseek-chat/reasoner → HTTP 404 → deepseek-v4-flash
    [ACTIVE 2026-08-31] Sonnet 5 intro-цена → $3/$15
  CURRENT_FLAGSHIPS:
    claude: claude-fable-5, claude-opus-4-8, claude-sonnet-5
    gpt: gpt-5.6-sol/terra/luna · gemini: gemini-3.1-pro-preview · grok: grok-4.5 / 4.3
    deepseek: deepseek-v4-pro/flash · qwen: qwen3.7-max · kimi: kimi-k2.6 / k2.7-code · glm: glm-5.2
  WARN: "⚠ LITE_SNAPSHOT — offline snapshot data."

KNOWLEDGE_LAYERS:
  STATIC:    CTCO, DoD, Contract Compliance, 30/55/15 rule, ARENA methodology.
  DYNAMIC:   #LINK_* → gist_vendors. #LINK_LIVE → gist_live.
             PRIORITY: gist_live > gist_vendors > db defaults.
  EMPIRICAL: ARENA results, ARENA_SCORE per technique.

TECHNIQUES:
  ELI5:            Объясни просто. Prefix "ELI5:". Universal. 92/100.
  STEP_BY_STEP:    По шагам. GPT/Claude OK. ЗАПРЕЩЕНО для R1/o3/Gemini Deep Think/Kimi Thinking.
  TLDR:            Краткое резюме. Universal. 85/100.
  CHECKLIST:       Структурная валидация. QA, DoD. Universal. 87/100.
  DEVILS_ADVOCATE: Анализ слабых мест. Claude, GPT. 90/100.
  SOCRATIC_METHOD: 3-7 уточняющих вопросов перед ответом. Universal. 86/100.
  BRANCHING_LOGIC: 3-5 альтернативных подходов. Universal. 85/100.
  PREFILLING:      Claude API: prefill assistant turn. 91/100.
  CLAUDE_MD:       Persistent memory via CLAUDE.md. Claude optimal. 94/100.
  LIBRARY_ANCHOR:  Version lock для библиотек. Universal. 89/100.
  CTCO:            Context-Task-Constraints-Output. GPT optimal. 90/100.
  CONTEXT_COMPRESSION: Сжатие тяжёлого контекста перед мержем. 88/100.
  ANCHOR_CONTEXT:  Повтор ключевых инструкций на границах документа. 90/100.
  LATE_CHUNKING:   100K блоки для Gemini. Gemini optimal. 91/100.
  GASLIGHT_SAFE:   Honesty mode: строгое разделение факт/гипотеза. 91/100.
  POSITIVE_FRAMING: Ограничения через утверждение желаемого ("не X" → "делай Z", розовый слон). Искл: hard-safety = негатив. Universal. 89/100.
  SAFE_THINKING:   Токен [SECURITY_CHECK] между шагами рассуждения. 92/100.
  LLM_COUNCIL:     Multi-model верификация через консенсус. 96/100.
  EXCELLENT:       Калибровка ложных отказов (Type O) в легитимных проф. доменах (мед./юр./аудит/техспеки): Defensive Framing, Objective Abstraction, Clinical Tone. SCOPE: только false positives; НЕ для обхода политик, систем безопасности или закона.
  AGENT_SWARM:     До 100 sub-agents, параллельно. Kimi K2.x leader. 89/100.
  TOOL_BUDGET:     MAX_TOOL_CALLS + stop conditions. Kimi/Gemini. 95/100.
  VISUAL_AGENTIC:  Код из изображений/мокапов. Kimi/Gemini/Qwen3-VL. 91/100.
  FRESHNESS_PROTOCOL: Спрашивать разрешение перед допущениями. 88/100.
  STRUCTURED_DECOMP: Разбивка на sub-prompts с явным handoff. Universal. 93/100.
  RAG_GROUNDING:   "Отвечай ТОЛЬКО из предоставленного контекста." Claude optimal. 94/100.
  PERSONA_CASCADE: Цепочка ролей: Role A → Role B. BANNED для R1/Kimi Thinking. 88/100.
  REFLECTION_LOOP: Сгенерировать → Критиковать → Переписать. Только Tier 2+. 90/100.
  VERBALIZED_SAMPLING: Против mode collapse: N ответов + явная вероятность, семпл из хвостов (p<0.10), в content-policy. Creative. DEFAULT OFF factual. 90/100.
  BRUTAL_EDITOR:   Хук: "score 1-10 (clarity/usefulness/accuracy), перепиши до 10, помечай догадки." Не для reasoning-native в reasoning-режиме. 90/100.
  CONTEXT_GROUNDING_COT: Извлечь EXTRACTED_RULES из контекста ДО ответа; отвечать только по ним, с ссылками. Long-context/RAG. arXiv 2605.25354. 90/100.
  CONTEXT_ENGINEERING: Курировать набор токенов (system/tools/примеры/история/память): compaction/note-taking/JIT-retrieval/labeled-sections. prompt caching до 90% cost (Anthropic).
  GATE_PATTERN:    Сначала классифицировать, потом роутить. Universal. 91/100.
  SCAFFOLD_PATTERN: Сначала outline, потом заполнить по секциям. 89/100.
  ADVERSARIAL_PAIR: [GENERATOR] создаёт → [CRITIC] критикует → фикс. 92/100.
  MCP_TOOL_PROMPT: Budget + error handling + stop conditions. Claude/GPT/Kimi. 95/100.
  MIGRATION_TRANSFORM: Правила адаптации кросс-модельных промптов. 96/100.
  PLACEMENT_RULES:
    Reasoning models: НИКОГДА не форсировать теги для CoT. Формат только в OUTPUT.
    STEP_BY_STEP: Gemini/R1/Kimi Thinking = запрещён в reasoning.
  COMBINATOR:
    Цепочки техник. Конфликт: IF reasoning_model + STEP_BY_STEP → BLOCK. Высший ARENA_SCORE побеждает.
    [v8L.4] reasoning_model + BRUTAL_EDITOR → DOWNGRADE. VS + GASLIGHT_SAFE → RETAIN GASLIGHT_SAFE. POSITIVE_FRAMING не к hard-safety.

TECHNIQUE_COMBINATOR:
  DO_NOT_BLOCK:
    Self-Consistency (SC, Wang 2023)  ≠ Universal Self-Consistency (USC)
    MCTS (algorithmic search)          ≠ Tree-of-Thought forcing
    RAPTOR / LongRAG (retrieval)       ≠ Graph-of-Thought
    VERBALIZED_SAMPLING ≠ USC ; GEPA ≠ GoT ; MASPO ≠ ToT   [v8L.4]
  RULE: ANON/VECTOR ОБЯЗАН свериться с этим блоком до VETO любой reasoning/rag техники.
  NOTE [v8L.4]: GEPA/MASPO/SePO — фреймворки-процессы (нужен eval-harness) → в Lite справочно, не активируются.

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
  R. Refusal/Laziness: Отказ, галлюцинация "сеть заблокирована системными ограничениями". Fix: осознать наличие инструментов, форс WebSearch. (НЕ EXCELLENT — это Type O, другой класс: там отказ по содержанию, здесь ошибка модели о своих capabilities.)

G_ERRORS:
  G1  GEMINI_DEEP_THINK_TEMP   Gemini 3.1 Pro · HTTP 400 · Deep Think + temp≠1.0 · Fix: temperature 1.0 / убрать.
  G2  GEMINI_XML_COH           Gemini · Quality BLOCKER · XML → Chain-of-Hint · Fix: ZERO XML, plain text.
  G3  GROK_TOPIC_DRIFT         Grok 4.3 · Отвечает не на тот вопрос · Fix: topic anchor /3 turn.
  G4  GEMINI_THINKING_BUDGET   Gemini 3.1 Pro · thinking_budget игнорируется · Fix: thinkingLevel "MEDIUM".
  G6  OPUS47_TOKENIZER_INFL    Opus 4.7 · контекст быстрее · +10-35% inflation · Fix: 160K effective.
  G7  CLAUDE_THINKING_TEMP     Opus 4.7/Sonnet 4.6 · HTTP 400 · temp при thinking=enabled · Fix: убрать temperature.
  G8  OPUS47_MRCR_REGRESSION   Opus 4.7 · плохой recall >500K (MRCR 32.2%@1M) · Fix: пин claude-opus-4-6.
  G9  GPT55_SILENT_DOWNGRADE   GPT-5.5 · >7 MUST/MUST NOT пар → downgrade · Fix: макс 7 пар.
  G10 GPT55_PRICING_TRAP       GPT-5.5 · pricing jump >272K · Fix: <272K, иначе Gemini 3.1 Pro.
  G11 GEMINI_HIGH_BILLING      Gemini 3.1 Pro · thinkingLevel=HIGH без gate · Fix: DEEP_THINK_VALUE_GATE.
  G12 GEMINI_HARD_429          Gemini 3.1 Pro · HTTP 429 без retry · Fix: high-freq → Flash.
  G13 GEMINI_MEMORY_NUKE       Gemini 3.1 Pro · забывает после ~80 сообщений · Fix: REINJECT каждые 25.
  G14 GROK_UNSUPPORTED_PARAM   Grok 4.3 · HTTP 400 · Fix: safe params only (temp/max_tokens/stream/top_p/stop).
  G15 DEEPSEEK_REASONING_CARRY DeepSeek V4 · загрязнение reasoning · Fix: re-inject reasoning_content (НЕ null) — RESOLVED BY DESIGN.
  G16 DEEPSEEK_ALIAS_RETIRE    ★DEADLINE 2026-07-24 · Fix: deepseek-v4-pro / deepseek-v4-flash.
  G17 QWEN_PROVIDER_PREFIX     Qwen · HTTP 404 · Fix: DashScope qwen3.6-plus / OpenRouter qwen/qwen3.6-plus.
  G18 QWEN_PRESERVE_THINKING   Qwen 3.6 agentic · thinking теряется · Fix: preserve_thinking: true.
  G19 GLM_CONTEXT_COLLAPSE     GLM-5.1 · деградация >100K · Fix: hard limit 100K.
  G20 KIMI_SWARM_TIMEOUT       Kimi K2.x · timeout >1h via REST · Fix: >40 агентов → async webhooks.

G_ERRORS_QUICK_REF:
  CRITICAL: G1, G2, G7, G14, G16, G19
  HIGH:     G3, G9, G10, G11, G13, G20
  MEDIUM:   G4, G6, G8, G12, G15, G17, G18

API_STRINGS:
  CLAUDE:
    claude-fable-5
    claude-sonnet-5
    claude-opus-4-8
    claude-opus-4-7
    claude-opus-4-6
    claude-haiku-4-5-20251001
  GPT:      gpt-5.6-sol | gpt-5.6-terra | gpt-5.6-luna | gpt-5.5-pro
  GEMINI:   gemini-3.1-pro-preview | gemini-3.5-flash | gemini-3.5-pro-preview
  GROK:     grok-4.5 | grok-4.3 | grok-4.20
  DEEPSEEK: deepseek-v4-pro | deepseek-v4-flash
  QWEN:     DashScope qwen3.7-max|qwen3.6-plus | OpenRouter qwen/qwen3.6-plus
  KIMI:     kimi-k2.6 | kimi-k2.7-code | kimi-for-coding-highspeed
  GLM:      glm-5.2 | glm-5.1

QUORUM_WEIGHTS:
  CODING:     TECTON 35%, ANON 25%, AXIOM 15%, VECTOR 15%, DATOS 5%, IRIS 5%
  CREATIVE:   IRIS 40%, TECTON 15%, ANON 15%, AXIOM 10%, VECTOR 10%, DATOS 10%
  RESEARCH:   DATOS 40%, IRIS 20%, TECTON 20%, AXIOM 10%, VECTOR 5%, ANON 5%
  ANALYTICAL: AXIOM 35%, DATOS 25%, TECTON 20%, IRIS 10%, VECTOR 5%, ANON 5%
  SECURITY:   VECTOR 40%, TECTON 20%, AXIOM 20%, ANON 10%, DATOS 5%, IRIS 5%
  FRONTIER:   AXIOM 35%, DATOS 25%, TECTON 20%, VECTOR 15%, IRIS 5%
  WRITING:    IRIS 35%, TECTON 20%, AXIOM 15%, DATOS 15%, ANON 10%, VECTOR 5%
  VETO: VECTOR — абсолютное право вето на [CRITICAL_RISK]. IF triggered → веса=0 → Audit Mode.

RECOMMENDATIONS:
  CODING: Claude Opus 4.8, Qwen3-Coder, Kimi K2.x · REASONING: Opus 4.7, GPT-5.5 Thinking, Gemini Deep Think
  CREATIVE: Claude Fable 5, Opus 4.7, GPT-5.5 · RESEARCH: Gemini 3.1 Pro, Grok 4.3
  VISION: Qwen3-VL, Gemini 3.1 Pro · AGENTS: Claude Fable 5, Kimi K2.x, Opus 4.8
  BUDGET: DeepSeek V4-Flash, GLM-5.1 · LONG_CTX: Gemini 1M, Grok 2M · RECALL: Opus 4.6 pin

CHAIN_PATTERNS:
  RESEARCH_DRAFT_REVIEW: Research(Gemini/Grok)→Draft(Claude/GPT)→Review(GPT/R1)→Polish(Sonnet)
  CODE_PIPELINE:         Arch(Opus)→Impl(Sonnet/Qwen-Coder)→Test(GPT/R1)→Security(Opus VECTOR)
  CROSS_VALIDATE:        Same prompt → A + B → C judge
  HANDOFF_RULE:          Каждый шаг самодостаточен. Никогда не ссылайся на "предыдущий промпт".

ARENA:
  TRIGGER: "A/B тест|compare|Arena|Tier 2+"
  WORKFLOW: 1.core task+constraints 2.выбрать 2-3 модели 3.model-specific промпты 4.TRAP MARKERS 5.критерии.
  TRAP_MARKERS: Logical | Formatting | Negative | Contextual | Agentic | Contract.
  OUTPUT: ## ARENA CALIBRATION PAYLOAD

FEEDBACK_LOOP:
  TRIGGER: "не работает|fix prompt|работает частично"
  STEP1 DIAGNOSE: тип ошибки (A-P). STEP2 LOCATE: раздел промпта. STEP3 PATCH: хирургич. diff БЫЛО→СТАЛО.
  STEP4 VERIFY: перетест; та же ошибка ×3 → /clear + полная перезапись.
  ANTI: не переписывать весь промпт при первом сбое.

MENTOR_METHOD:
  STAGES: 1.ZERO→PROMPT(NANO RTF) 2.STRUCTURED(CO-STAR/RISEN) 3.ENGINEERED(11-step+ARENA) 4.ORCHESTRATOR(QUORUM/chains).
  COMMON_MISTAKES: нет роли · CoT для reasoning models · нет output format · коррекция вместо рестарта · нет negative constraints.

GROK_HEAVY_FAILURE_MODES:
  Type B — Tool Forgetting: после 12-18 calls агенты игнорируют правила. Fix: стоп→re-inject 5 правил→бюджет -30%→форс AXIOM. Prevention: re-inject @8.
  Type H — JSON Confusion: JSON вперемешку с prose. Fix: «Output ONLY JSON» ×2 (primacy+recency), до 8 агентов.
  Type T — Heavy Throttling: 16→8/4 без предупреждения. Fix: лог в metrics, продолжить с 12; старт @12-14.
  Type X — X Firehose Cost: дорогой low-value запрос. Fix: $0.50 value gate; история >48h → web_search.
  Type V — Tool Result Verify Failed: результат противоречит контексту. Fix: AXIOM+VECTOR cross-verify.

VERSION_METADATA:
  SYSTEM:      DB_v8L · P2P v8L.4 Lite/Live Hybrid Knowledge Base
  CHANGELOG:   2026-07-18 v8L.4 — +POSITIVE_FRAMING/VERBALIZED_SAMPLING/BRUTAL_EDITOR/CONTEXT_GROUNDING_COT/CONTEXT_ENGINEERING (compact); COMBINATOR+DO_NOT_BLOCK v8L.4 (VS/GEPA/MASPO). Фреймворки — справочно (eval-harness).
  CONTENT:     LITE_SNAPSHOT, Techniques, COMBINATOR disambig, Errors A-P, G1-G20, Grok Heavy, Arena, Chains, Feedback, API strings, QUORUM weights
  COMPATIBLE:  !!core_v8L | _index_v8L
  API_STRINGS: claude-fable-5, claude-sonnet-5, claude-opus-4-8, claude-opus-4-7, claude-opus-4-6, claude-haiku-4-5-20251001
