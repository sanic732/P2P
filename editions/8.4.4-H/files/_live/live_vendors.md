---
id: live_vendors_v8H
version: v8H.3
type: LIVE_VENDORS
priority: HIGH
load_order: 6
update_frequency: weekly
last_verified: 2026-07-13
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — LIVE VENDORS
// G-ошибки G1-G20 детально, правила маршрутизации.
// OVERRIDE приоритет: live_specs > live_vendors > vendors/*.md > !!db_v8H.md
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. CAPABILITY MATRIX (все хосты)
// ─────────────────────────────────────────────────────

CAPABILITY_MATRIX:
  // Format: model | XML | Thinking | Long ctx | Agents | Vision

  claude-fable-5:      XML=NATIVE | Thinking=adaptive  | 1M      | Computer Use  | Yes  // #1 Overall/Text/Vision; classifier FP ~5%→Opus 4.8
  claude-sonnet-5:     XML=NATIVE | Thinking=adaptive  | 1M      | Computer Use  | Yes  // NEW default Free/Pro (30.06); near-Opus, $2/$10
  claude-opus-4-8:     XML=NATIVE | Thinking=adaptive  | 1M      | Computer Use  | Yes  // primary complex code; SWE-bench Pro 69.2%
  claude-opus-4-7:     XML=NATIVE | Thinking=adaptive  | 1M      | Computer Use  | Yes
  claude-opus-4-6:     XML=NATIVE | Thinking=adaptive  | 1M      | Computer Use  | Yes  // pin >500K recall (MRCR 78.3%)
  claude-haiku-4-5:    XML=NATIVE | Thinking=limited   | 200K    | Tool Calling  | Yes
  claude-sonnet-4-6:   XML=NATIVE | Thinking=effort    | 200K    | Tool Calling  | Yes  // RETIRED 30.06 (API-only legacy)
  gemini-3.5-pro:      XML=BLOCK  | Deep Think=level   | 2M      | Code Exec     | Yes  // ⚠ PREVIEW (не GA)
  gemini-3.1-pro:      XML=BLOCK  | Deep Think=level   | 2M      | Code Exec     | Yes (native)
  gemini-3.5-flash:    XML=BLOCK  | Flash thinking     | 1M      | Code Exec     | Yes
  gpt-5.6-sol:         XML=JSON   | reasoning_effort   | 1.05M   | Function Call | Yes  // NEW GA 09.07; WebDev #1; ⚠ reward-hacking
  gpt-5.6-terra:       XML=JSON   | reasoning_effort   | 1.05M   | Function Call | Yes  // NEW balanced (замена 5.5)
  gpt-5.6-luna:        XML=JSON   | reasoning_effort   | 1.05M   | Function Call | Yes  // NEW cheap; ⚠ MRCR >512K
  grok-4.5:            XML=NO     | reasoning(def high)| 500K    | Tool+strict JSON | Yes  // NEW GA 08.07; coding flagship; ⚠ не EU; $2/$6
  grok-4.3:            XML=NO     | reasoning          | 1M      | Tool Use      | Yes  // $1.25/$2.50
  grok-4.20:           XML=NO     | reasoning(Heavy-16)| 2M      | Tool Use      | Yes  // multi-agent 16 parallel
  deepseek-v4-pro:     XML=NO     | native (temp=0.3)  | 1M      | Function Call | No
  deepseek-v4-flash:   XML=NO     | native (light)     | 1M      | Function Call | No   // ⚠ alias 404 24.07
  qwen3.7-max:         XML=NO     | thinking_budget    | 1M      | Tool Use      | Qwen-VL
  qwen3.6-plus:        XML=NO     | thinking_budget    | 1M      | Tool Use      | Partial
  kimi-k2.6:           XML=NO     | thinking=on|off    | 256K-1M | Swarm 300     | No
  glm-5.2:             XML=NO     | thinking=on|off    | 1M      | Tool Use      | No   // MIT; WebDev #3
  glm-5.1:             XML=NO     | thinking=on|off    | 100K*   | Tool Use      | GLM-5V
  // * G19: context collapse above 100K (5.1); GLM-5.2 расширен до 1M

// ─────────────────────────────────────────────────────
// §2. G-ERRORS FULL CATALOG (G1-G20)
// ─────────────────────────────────────────────────────

G1: GEMINI_DEEP_THINK_TEMP
  Model:    Gemini 3.1 Pro
  Error:    HTTP 400
  Cause:    Deep Think требует temperature = 1.0 (или отсутствие temperature)
  Fix:      Установи temperature: 1.0 или удали temperature полностью
  Example:
    // WRONG:
    // {"model":"gemini-3.1-pro", "temperature":0.7, "thinkingConfig":{"thinkingBudget":5000}}
    // CORRECT:
    // {"model":"gemini-3.1-pro", "temperature":1.0, "thinkingConfig":{"thinkingLevel":"MEDIUM"}}

G2: GEMINI_XML_COH_INTERFERENCE
  Model:    Gemini 3.1 Pro / Flash
  Error:    Деградация качества, игнорирование инструкций
  Cause:    XML теги вызывают Chain-of-Hint inference в Gemini CoT
  Fix:      ZERO XML в system prompt. Используй ## заголовки, **жирный**
  Critical: BLOCKER — промпты с XML для Gemini работают хуже random baseline
  Detection: grep -c '<[a-z_]*>' your_prompt.txt  (должно быть 0 для Gemini)

G3: GROK_TOPIC_DRIFT
  Model:    Grok 4.3
  Error:    Ответ уходит в сторону от исходной задачи
  Cause:    Grok отвлекается на интересные связанные темы
  Fix:      Topic anchor каждые 3 хода:
            "[TOPIC ANCHOR: Исходная задача = {краткое описание}. Держись темы.]"
  Pattern:  Добавь в шаблон для Grok как часть контракта

G4: GEMINI_THINKING_BUDGET_PRO
  Model:    Gemini 3.1 Pro
  Error:    thinking_budget молча игнорируется
  Cause:    Pro модель использует thinkingLevel enum, не thinking_budget int
  Fix:      {"thinkingConfig": {"thinkingLevel": "MEDIUM"}}  // не thinking_budget: 5000
  Note:     Flash поддерживает оба. Pro — только thinkingLevel.

G5: (зарезервировано для будущих Gemini issues)

G6: OPUS47_TOKENIZER_INFLATION
  Model:    Claude Opus 4.7
  Error:    Контекст расходуется быстрее ожидаемого (~10-35%)
  Cause:    Новый токенизатор Opus 4.7 считает символы иначе
  Fix:      При планировании → используй 160K как effective max (не 200K)
  Impact:   Для длинных системных промптов (P2P FULL ~300K) → использовать Sonnet 4.6

G7: CLAUDE_EXTENDED_THINKING_TEMP
  Model:    Claude Opus 4.7, Claude Sonnet 4.6
  Error:    HTTP 400 немедленно
  Cause:    temperature присутствует в payload при thinking=enabled
  Fix:      Полностью удали temperature из запроса
  Code fix:
    # ПРАВИЛЬНО:
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=16000,
        thinking={"type": "enabled", "effort": "medium"},
        # НЕТ temperature здесь
        messages=[{"role": "user", "content": prompt}]
    )
    # НЕПРАВИЛЬНО (HTTP 400):
    response = client.messages.create(
        model="claude-opus-4-7",
        thinking={"type": "enabled", "effort": "medium"},
        temperature=0.7,  # ← УДАЛИ ЭТО
        messages=[...]
    )

G8: OPUS47_MRCR_REGRESSION
  Model:    Claude Opus 4.7
  Error:    Плохой recall при длинных контекстах
  Cause:    MRCR (Multi-hop Reasoning Chain Recall) 32.2% at 1M (vs 78.3% у Opus 4.6)
  Fix:      Для задач с необходимостью recall >500K → пин claude-opus-4-6
  Note:     claude-opus-4-7 превосходит 4.6 на всём остальном — только recall регрессия

G9: GPT55_SILENT_DOWNGRADE
  Model:    GPT-5.5
  Error:    Тихое снижение качества без ошибок, без предупреждений
  Cause:    Более 7 пар MUST/MUST NOT → silent quality downgrade в inference
  Fix:      Максимум 7 MUST + 7 MUST NOT = 14 правил итого
  Pattern:  Использовать приоритетную матрицу: оставить только Critical правила

G10: GPT55_PRICING_TRAP
  Model:    GPT-5.5
  Error:    Неожиданный скачок стоимости
  Cause:    Pricing tier jump выше 272K input tokens
  Fix:      Держи system + user tokens под 272K совокупно
  Alt:      Для >272K → Gemini 3.1 Pro (лучше соотношение цена/качество)

G11: GEMINI_HIGH_BILLING_SHOCK
  Model:    Gemini 3.1 Pro
  Error:    Очень высокий счёт (15-20x базовая стоимость)
  Cause:    thinkingLevel=HIGH без Value Gate активирован на простых задачах
  Fix:      Всегда применяй DEEP_THINK_VALUE_GATE перед HIGH
  Note:     HIGH = примерно $50/M vs $3.50/M базовая

G12: GEMINI_HARD_429
  Model:    Gemini 3.1 Pro
  Error:    HTTP 429, нет retry queue
  Cause:    Pro имеет hard rate limit (в отличие от Flash с soft limit + queue)
  Fix:      Для высокочастотных вызовов → переключись на Gemini Flash
  Pattern:  Pro для качества, Flash для скорости/частоты

G13: GEMINI_MEMORY_NUKE
  Model:    Gemini 3.1 Pro
  Error:    Модель "забывает" constraints после ~80 сообщений
  Cause:    Heavy tool use вызывает session memory nuke около turn 80
  Fix:      CONSTRAINT_REINJECTION каждые 25 сообщений (не 50 как для Claude)
  Script:   Передавать summary constraints как часть каждого N*25-го turn

G14: GROK_UNSUPPORTED_PARAM
  Model:    Grok 4.3
  Error:    HTTP 400 на нестандартные параметры
  Cause:    Grok строго валидирует параметры, не молчит как другие
  Fix:      Используй только safe params: temperature, max_tokens, stream, top_p, stop
  Banned:   top_k, repetition_penalty, presence_penalty, logit_bias (→ HTTP 400)

G15: DEEPSEEK_REASONING_CARRYOVER
  Model:    DeepSeek V4 (Pro и Flash)
  Error:    Загрязнение reasoning из предыдущего turn
  Cause:    reasoning_content накапливается в history — это BY DESIGN (для рефакторинга), НЕ баг
  Fix:      В multi-turn с tools: store + re-inject reasoning_content (НЕ обнулять) — RESOLVED BY DESIGN
  Code:
    messages.append({
        "role": "assistant",
        "content": response.content,
        "reasoning_content": prev_reasoning  # re-inject, НЕ null (v8.5 RESOLVED)
    })

G16: DEEPSEEK_ALIAS_RETIRE
  Model:    deepseek-chat, deepseek-reasoner
  Error:    API вызовы перестанут работать после дедлайна
  DEADLINE: 2026-07-24 ★ КРИТИЧНО — 83 дня
  Fix:
    deepseek-chat      → deepseek-v4-pro
    deepseek-reasoner  → deepseek-v4-flash
  Scan:     grep -r "deepseek-chat\|deepseek-reasoner" .

G17: QWEN_PROVIDER_PREFIX
  Model:    Qwen 3.6 (все варианты)
  Error:    HTTP 404 или загружается не та модель
  Cause:    Разные провайдеры требуют разные форматы имён
  Fix:
    DashScope (official):  "qwen3-plus" (без префикса)
    OpenRouter:            "qwen/qwen3-plus" (с префиксом qwen/)
    HuggingFace Inference: "Qwen/Qwen3-plus" (с заглавной Q)

G18: QWEN_PRESERVE_THINKING
  Model:    Qwen 3.6 в agentic режиме
  Error:    Thinking блок теряется между tool calls
  Cause:    По умолчанию thinking не сохраняется в контексте
  Fix:      preserve_thinking: true в параметрах запроса

G19: GLM_CONTEXT_COLLAPSE
  Model:    GLM-5.1-flash
  Error:    Резкая деградация качества
  Cause:    Реальный надёжный предел контекста ~100K (номинальный 202K)
  Fix:      HARD LIMIT 100K для всех GLM-5.1 запросов
  Note:     MIT лицензия сохраняется — просто держи контекст под 100K

G20: KIMI_SWARM_TIMEOUT
  Model:    Kimi K2.x
  Error:    Timeout при >40 синхронных агентах
  Cause:    Синхронный лимит агентов = 40
  Fix:      Для >40 агентов → PARL async режим + webhooks для результатов
  Code pattern:
    # Синхронно (до 40):
    result = kimi.swarm(agents=list[:40], mode="sync")
    # Асинхронно (>40):
    job_id = kimi.swarm(agents=list, mode="async")
    # Получить через webhook или polling

// ─────────────────────────────────────────────────────
// §2b. v8.6.1 NEW ISSUES (2026-06-12, import из live_specs)
// ─────────────────────────────────────────────────────

V84_ISSUES:

  FABLE5_SAFETY_NANNY:
    Model:   claude-fable-5
    Issue:   ~5% сессий молча перенаправляются на Opus 4.8 (UNRESOLVED BY DESIGN)
    Impact:  непредсказуемость стиля/латентности в agentic-пайплайнах
    Fix:     для критичных прогонов с гарантией модели → пинить claude-opus-4-8 явно;
             держать Opus 4.8 в fallback chain после Fable 5

  CLAUDE_CACHE_TTL_DROP:
    Scope:   Claude Code
    Issue:   cache TTL понижен 1h → 5min (2026-06)
    Fix:     ставить ephemeral cache_control на стабильный префикс перед каждым вызовом

  GEMINI_ERROR_13:
    Model:   Gemini 3.5 Flash + 3.5 Pro Preview
    Issue:   Error 13 — UNRESOLVED (на момент 2026-06-12)
    Fix:     для продакшена пинить gemini-3.1-pro-latest (стабильная ветка)

  GLM51_COMPACT_HANG:
    Model:   GLM-5.1
    Issue:   бесконечный thinking-loop на команде /compact
    Fix:     не использовать /compact на GLM; ручное сжатие через CAPSULE (!memory)

  OPENAI_v84_BUGS:
    Model:   GPT-5.5 / OpenAI platform
    Issue:   Billing Ghost Users + Memory Routing Bug (2026-06-12)
    Fix:     мониторить биллинг; не полагаться на серверную memory-маршрутизацию для критичного состояния

// ─────────────────────────────────────────────────────
// §3. TRANSLATION RULES (детально)
// ─────────────────────────────────────────────────────

TRANSLATION_RULES:

  ANY → GEMINI:
    STRIP: <role>, <rules>, <task>, <context>, <output_format>
           все кастомные XML теги
    REPLACE_WITH: ## Role, ## Rules, ## Task (plain text)
    STRIP_PARAM: temperature (если Deep Think)
    ADD_PARAM: thinkingLevel: "MEDIUM" (если deep thinking нужен)
    VERIFY: grep -c '<[a-z_]*>' output.txt == 0

  ANY → GPT:
    CONVERT: XML structure → plain sections or JSON schema
    LIMIT_RULES: max 7 MUST + 7 MUST NOT
    ADD_PARAM: reasoning_effort: "medium"
    WATCH: input_tokens < 272K (G10)
    FORMAT: response_format={"type":"json_object"} для JSON output

  ANY → GROK:
    STRIP: XML tags, nonstardard params
    KEEP: temperature, max_tokens, stream, top_p, stop only
    ADD: topic anchor шаблон (G3 prevention)
    FORMAT: Plain Markdown

  ANY → DEEPSEEK:
    STRIP: XML, extended thinking params
    ADD: re-inject reasoning_content в multi-turn с tools (G15 RESOLVED BY DESIGN — НЕ обнулять)
    USE_API: deepseek-v4-pro / deepseek-v4-flash (не старые алиасы — G16)
    TEMP: 0.3 для R1 reasoning

  ANY → QWEN:
    STRIP: XML, effort params
    USE: thinking_budget: 10000 (вместо effort: medium)
    PROVIDER: проверить prefix (G17)
    AGENTIC: preserve_thinking: true (G18)

  ANY → KIMI:
    STRIP: XML, effort levels
    USE: thinking: on|off
    ADD: checkpoint_before_writes (Type G prevention)
    T0-T1: thinking: off (Type I prevention)
    FORMAT: Mental Sandbox для strict format

  ANY → GLM:
    STRIP: XML полностью
    USE: ## Structured Segmentation
    TEMP: 0 для JSON output
    LIMIT: 100K context hard (G19)
    THINKING: per-turn on|off

// ─────────────────────────────────────────────────────
// VERSION
// ─────────────────────────────────────────────────────

VERSION_METADATA:
  SYSTEM:      live_vendors v8H.3
  SCOPE:       G-errors G1-G20, v8.5 issues, Translation Rules, Capability Matrix
  SOURCE:      _live/live_specs.md (v8.6.3 OVERRIDE)
  OVERRIDE:    Этот файл имеет приоритет над vendors/*.md при конфликтах
  COMPATIBLE:  !!core_v8H.md | !!db_v8H.md | all v8H files
// ═══════════════════════════════════════════════════════
// §DELTA (обновлено 2026-07-13 под live_specs v8.6.3 — OVERRIDE governs on conflict)
// Актуальные модели — в CAPABILITY_MATRIX выше; ниже per-vendor нюансы.
// ═══════════════════════════════════════════════════════
DELTA_v863:
  Claude_legacy_retire: COMPLETED — *-4-20250514 → HTTP 404; sonnet-4-6 RETIRED 30.06 (Sonnet 5 default).
  Claude_5_line: Sonnet 5 (default Free/Pro, $2/$10→$3/$15 c 01.09), Fable 5 (REDEPLOYED — НЕ suspended; $10/$50, Arena #1), Mythos 5 (Glasswing, not routed), Opus 4.8 primary complex code.
  Claude_specs: Opus 4.x pricing $5/$25; context 1,000,000; output 128K sync/300K batch; effort default=high (low|medium|high|xhigh|max).
  Claude_G6_tokenizer: UNRESOLVED (+30-42% на англ. прозе) → pin claude-opus-4-6 для cost-sensitive/больших system prompt.
  Claude_thinking: ТОЛЬКО thinking:{"type":"adaptive"}; budget_tokens removed; G7 — никогда temperature/top_p/top_k.
  DeepSeek_G15_REVERSED: reasoning_content НАДО re-inject после tool calls (НЕ обнулять) — RESOLVED BY DESIGN. Alias deepseek-chat/reasoner → 404 24.07 15:59 UTC (no grace).
  Gemini: 3.5 Pro всё ещё PREVIEW (2-й пропуск GA); 3.5 Flash/Omni Flash GA (T2V #1); Error 13 @100-128K (cap 80K); Safety Erasure → BLOCK_SOME/NONE (API не UI).
  Grok: 4.5 GA 08.07 (coding flagship, 500K, $2/$6, ~80 tps, ⚠ не EU, grok-build default) — заменил пропущенный 4.4; 4.20 multi-agent (2M, Heavy-16); 4.3 → 1M @ $1.25/$2.50; Heavy16 downgrade DISPUTED; G14 safe-list.
  GPT: 5.6 Sol/Terra/Luna PUBLIC GA 09.07 (1.05M; $5/$30 · $2.50/$15 · $1/$6; Sol WebDev #1 + reward-hacking flag; Luna MRCR collapse >512K); 5.5 Pro для Codex; G9 (≤7 пар), G10 (>272K → 2x/1.5x).
  Qwen: 3.7-Max (Agent Era) + 3.6-Plus; JSON errors → response_format {"type":"json_object"} + слово "JSON"; G18 bailian/ prefix обязателен.
  Kimi: K2.6 (Swarm 300 async) + K2.7-Code (open-weight, -30% thinking) + Code HighSpeed tier; Thinking-mode infinite-repeat → disable, use Swarm.
  GLM: glm-5.2 (1M, MIT, ~$1.40/$4.40, WebDev #3) основной; glm-5.1 (eff ~120K, G19) + highspeed; /compact hang на 5.1 (avoid → мигрировать на 5.2).
  NEW_VENDORS: MiniMax M3 ($0.30/$1.20, track-only); Manus 1.6 Max (GEOPOLITICAL CRISIS — Meta unwinding $2B; track-only, avoid prod).
  DEADLINES (from 2026-07-13): 2026-07-19 Fable5 → usage credits; 2026-07-24 15:59 UTC deepseek-chat/reasoner → 404; 2026-08-31 Sonnet 5 intro → $3/$15.
