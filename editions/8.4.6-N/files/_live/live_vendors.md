---
id: live_vendors_v8N
version: 8.4.6-N
type: LIVE_VENDORS
priority: HIGH
load_order: 6
update_frequency: weekly
last_verified: 2026-07-26
---

// ═══════════════════════════════════════════════════════
// P2P — LIVE VENDORS
// G-ошибки G1-G20 детально, правила маршрутизации.
// OVERRIDE приоритет: live_specs > live_vendors > vendors/*.md > !!db_v8N.md
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. CAPABILITY MATRIX (все хосты)
// ─────────────────────────────────────────────────────

CAPABILITY_MATRIX:
  // Format: model | XML | Thinking | Long ctx | Agents | Vision

  claude-opus-5:       XML=NATIVE | Thinking=ON BY DEF | 1M      | Computer Use  | Yes  // PRIMARY, GA 24.07; general reasoning/agentic/long-horizon
  claude-fable-5:      XML=NATIVE | Thinking=adaptive  | 1M      | Computer Use  | Yes  // Text/Vision #1; classifier FP→Opus 4.8; USAGE CREDITS с 20.07 (cost-gated)
  claude-sonnet-5:     XML=NATIVE | Thinking=adaptive  | 1M      | Computer Use  | Yes  // NEW default Free/Pro (30.06); near-Opus, $2/$10
  claude-opus-4-8:     XML=NATIVE | Thinking=adaptive  | 1M      | Computer Use  | Yes  // complex code, SWE-bench Pro 69.2%; ACTIVE, НЕ депрекирован; API-only surface (UI-видимость ≠ доступность)
  claude-opus-4-7:     XML=NATIVE | Thinking=adaptive  | 1M      | Computer Use  | Yes
  claude-opus-4-6:     XML=NATIVE | Thinking=adaptive  | 1M      | Computer Use  | Yes  // pin >500K recall (MRCR 78.3%)
  claude-haiku-4-5:    XML=NATIVE | Thinking=limited   | 200K    | Tool Calling  | Yes
  claude-sonnet-4-6:   XML=NATIVE | Thinking=effort    | 200K    | Tool Calling  | Yes  // RETIRED 30.06 (API-only legacy)
  gemini-3.5-pro:      XML=BLOCK  | Deep Think=level   | 2M      | Code Exec     | Yes  // ⚠ PREVIEW (не GA)
  gemini-3.1-pro:      XML=BLOCK  | Deep Think=level   | 2M      | Code Exec     | Yes (native)
  gemini-3.6-flash:    XML=BLOCK  | Flash thinking     | 1,048,576 | Code Exec + Computer Use | Yes  // GA 21.07 workhorse; 1.50/7.50; cache-read 0.15; G13 НЕ тестирован — не очищен
  gemini-3.5-flash-lite: XML=BLOCK | Flash thinking     | 1M      | Code Exec     | Yes  // GA 21.07; дешевейший 0.30/2.50
  gemini-3.5-flash:    XML=BLOCK  | Flash thinking     | 1M      | Code Exec     | Yes  // вытеснен 3.6 Flash
  gpt-5.6-sol:         XML=JSON   | reasoning_effort   | 1.05M   | Function Call | Yes  // GA 09.07; ⚠ G22 агентная опасность: вне judge-ролей и вне harness с записью в ФС/секреты
  gpt-5.6-terra:       XML=JSON   | reasoning_effort   | 1.05M   | Function Call | Yes  // NEW balanced (замена 5.5)
  gpt-5.6-luna:        XML=JSON   | reasoning_effort   | ⚠ офиц. строки нет | Function Call | Yes  // cheap; ⚠ MRCR >512K; long-context ставки не документированы
  grok-4.5:            XML=NO     | reasoning(def high, НЕ отключается)| 500K    | Tool+strict JSON | Yes  // GA 08.07; coding flagship; EU открыт 21.07 БЕЗ data-residency; $2 / $0.30 cached / $6, от 200K ×2 включая кэш
  grok-4.3:            XML=NO     | reasoning          | 1M      | Tool Use      | Yes  // $1.25/$2.50
  grok-4.20:           XML=NO     | reasoning(Heavy-16)| 2M      | Tool Use      | Yes  // multi-agent 16 parallel
  deepseek-v4-pro:     XML=NO     | native (temp=0.3)  | 1M      | Function Call | No
  deepseek-v4-flash:   XML=NO     | native (light, thinking неотключаем) | 1M | Function Call | No   // ⚠ линейка V4 официально PREVIEW; алиасы мертвы 24.07
  qwen3.7-max:         XML=NO     | thinking_budget    | 1M      | Tool Use      | Qwen-VL
  qwen3.7-plus:        XML=NO     | thinking_budget    | 1M / out 65K | Tool Use  | Yes  // multimodal, GA
  qwen3.6-35b-a3b:     XML=NO     | thinking_budget    | 262,144 | Tool Use      | No   // open-weight Apache-2.0
  qwen3.6-plus:        XML=NO     | thinking_budget    | 1M      | Tool Use      | Partial
  kimi-k3:             XML=NO     | thinking=ALWAYS-ON | 1,048,576 | Tool Use    | No   // WebDev #1; ⚠ ACCESS-RISK: hosted-only, подписки закрыты, весов нет → НЕ primary
  kimi-k2.6:           XML=NO     | thinking=on|off    | 256K-1M | Swarm 300     | No
  glm-5.2:             XML=NO     | thinking=on|off    | 1M      | Tool Use      | No   // MIT; WebDev #4; цена UNCONFIRMED
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

G6: OPUS4X_TOKENIZER_INFLATION
  Model:    Opus 4.7 и новее, Fable 5, Mythos 5, Sonnet 5, Opus 5 (весь новый токенизатор)
  Error:    Контекст расходуется быстрее ожидаемого (~+30%, официальная цифра)
  Cause:    Тот же входной текст даёт ~+30% токенов против моделей старше 4.7. Официальная
            цифра, одна, не вилка; не дефект — заявленное свойство токенизатора.
  Fix:      Считать официальным Token Counting API (поддерживает ВСЕ активные модели);
            cost-sensitive → пин claude-opus-4-6 / claude-sonnet-4-6
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

G10: GPT_PRICING_TRAP_272K
  Model:    GPT-5.5, GPT-5.6 (Sol/Terra/Luna)
  Error:    Неожиданный скачок стоимости
  Cause:    Выше 272K весь запрос → x2 UNCACHED input и x1.5 output. Sol: 5/30 → 10/45.
            КЛЮЧЕВОЕ: cached input EXEMPT — остаётся 0.50, скидка на кэш 90% переживает обрыв.
  Fix:      Перехват 250K, жёсткий обрыв 260K, явные cache breakpoints. Решать по доле
            попаданий в кэш, а не по сырому числу токенов.
  Warn:     Terra/Luna long-context ставки НЕ документированы; окно контекста Luna
            официальной строки не имеет. У xAI порог ИНОЙ (200K) и там удваивается также кэш.

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
  DEADLINE: 2026-07-24 15:59 UTC ★ КРИТИЧНО
  Fix:
    deepseek-chat      → deepseek-v4-flash (non-thinking)
    deepseek-reasoner  → deepseek-v4-pro  ⚠ НЕ v4-flash-thinking (иначе reasoning тихо деградирует)
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

FILE_META:
  SCOPE:       G-errors G1-G20, v8.5 issues, Translation Rules, Capability Matrix
  OVERRIDE:    Этот файл имеет приоритет над vendors/*.md при конфликтах
  COMPATIBLE:  !!core_v8N.md | !!db_v8N.md | all v8N files
// ═══════════════════════════════════════════════════════
// §DELTA (обновлено 2026-07-26 под live_specs v8.7.2 — OVERRIDE governs on conflict)
// Актуальные модели — в CAPABILITY_MATRIX выше; ниже per-vendor нюансы.
// ═══════════════════════════════════════════════════════
DELTA_v872:
  Claude_legacy_retire: COMPLETED — *-4-20250514 → HTTP 404; sonnet-4-6 RETIRED 30.06 (Sonnet 5 default).
  Claude_5_line: Opus 5 PRIMARY (GA 24.07, $5/$25, 1M/128K, thinking ON BY DEFAULT) — заменил Opus 4.8 как дефолтную тяжёлую модель. Sonnet 5 (default Free/Pro, $2/$10→$3/$15 c 01.09), Fable 5 (USAGE CREDITS с 20.07 — cost-gated, не в автоциклы; $10/$50, batch $5/$25, cache-hit in $1), Mythos 5 (Glasswing, not routed).
  Claude_specs: Opus 4.x/5 pricing $5/$25; context 1,000,000; output 128K sync/300K batch; effort default=high (low|medium|high|xhigh|max). Opus 4.8 ACTIVE, НЕ депрекирован — retirement floor «не ранее 2027-05-28»; убран из селектора приложения 24.07: это поверхность, НЕ депрекация, видимость в UI ≠ сигнал доступности. Opus 4.1 RETIRES 2026-08-05 (замена по офиц. таблице — opus-4-8). Fast mode у Opus 4.7 удалён.
  Claude_G6_tokenizer: UNRESOLVED BY DESIGN. КАНОН ~+30% (официальная цифра, одна, не вилка) для Opus 4.7+/Fable 5/Mythos 5/Sonnet 5/Opus 5 против моделей старше 4.7. Счётчик — официальный Token Counting API, ВСЕ активные модели. Прежние +30-42% и 10-35% — сторонние измерения, вторичные → pin claude-opus-4-6 для cost-sensitive.
  Claude_thinking: для 4.x ТОЛЬКО thinking:{"type":"adaptive"}; на Opus 5 включён по умолчанию; budget_tokens removed; G7 — никогда temperature/top_p/top_k.
  Claude_automatic_fallbacks: opt-in beta — параметр `fallbacks` + beta-header server-side-fallback-2026-06-01; цель Opus 4.8; НАБЛЮДАЕМО через content block {"type":"fallback"} + usage.iterations; биллинг расщепляется по моделям; в app/Claude Code отключаемо. Проверять блок, а не угадывать деградацию по качеству вывода.
  MODEL_IDENTITY_ASSERT (cross-vendor): OpenAI — сверять resolved_model_slug, НЕ model_slug; Anthropic — проверять блок {"type":"fallback"}. Расхождение личности модели = громкий отказ harness, а не то, что поглощают молча.
  DeepSeek_G15_REVERSED: reasoning_content НАДО re-inject после tool calls (НЕ обнулять) — RESOLVED BY DESIGN. Алиасы deepseek-chat/reasoner мертвы 24.07 15:59 UTC без grace; точный код не подтверждён (404 либо 400 invalid_request_error) — принимать оба. Бывший deepseek-reasoner → v4-pro, НЕ v4-flash-thinking. Линейка V4 официально PREVIEW (запись 24.04, метку никто не снимал); заявления о GA вторичны.
  Gemini: 3.6 Flash GA 21.07 — новый workhorse (1,048,576/65,536; $1.50/$7.50; cache-read $0.15; ~304 tok/s; на 17% меньше выходных токенов; нативный Computer Use). Индекс AA = 50, как у 3.5 Flash: экономия, не рост способностей. 3.5 Flash-Lite GA ($0.30/$2.50, ~350 tok/s). 3.5 Pro — ТРЕТИЙ пропуск GA, остаётся preview, цены нет. Error 13 на 3.6 Flash НЕ воспроизведён и НЕ признан — модель не проверена, а не очищена: обходы (Context Caching, cap 80K, без пачек 30+ изображений) применять и к ней. Safety Erasure → BLOCK_SOME/NONE (API не UI). Внутренний маршрут gemini-3.6-flash-tiered НЕ публичный.
  Grok: единственный id grok-4.5 — heavy/expert/fast НЕ существуют (Heavy = план 300/мес плюс режим оркестрации поверх той же модели). Цена: 2 in / 0.30 cached / 6 out; от 200K — 4 / 0.60 / 12, удваивается И КЭШ, кэширование обрыв не смягчает (перехват 190K, обрыв 195K). Унаследованная cached 0.50 НЕВЕРНА. EU открыт 21.07 БЕЗ data-residency. reasoning_effort high неотключаем, reasoning биллится как output. 4.20 multi-agent (2M, Heavy-16); 4.3 → 1M. HEAVY16_SHADOW_DOWNGRADE — CLOSED AS OBSOLETE (не resolved: ничего не чинили, конфигурация перестала существовать; реоткрыть при появлении отдельных Heavy-эндпоинтов). G14 safe-list.
  GPT: 5.6 Sol/Terra/Luna GA 09.07 (Sol 5 in / 0.50 cached / 30 out; Terra 2.50/15; Luna 1/6). G10: выше 272K весь запрос ×2 UNCACHED input и ×1.5 output, cached input EXEMPT — скидка на кэш 90% переживает обрыв, решать по доле попаданий в кэш. Long-context ставки Terra и Luna НЕ документированы (ходившие цифры — экстраполяция); окно контекста Luna официальной строки не имеет. Голый алиас gpt-5.6 резолвится в Sol. Sol: system card вендора документирует удаление файлов без запроса и использование неавторизованных учётных данных → вне judge-ролей И вне любого harness с записью в ФС/секреты без allowlist и аудита. Тихий даунгрейд детектируется через resolved_model_slug. Ghost-users: падение одного списания деактивирует ВЕСЬ workspace вместе с оплаченными местами → не брать годовую предоплату на Business. Assistants API (/v1/assistants, /v1/threads, вкл. Azure) — отключение 2026-08-26 без автомиграции. 5.5 Pro для Codex; G9 (≤7 пар).
  Qwen: 3.7-Max TEXT-ONLY (2.50/7.50) + 3.7-Plus multimodal 1M/65K + 3.6-35B-A3B (open-weight Apache-2.0, 262K, 0.14/1.00) + 3.6-Plus. Deep-thinking режим НЕ поддерживает structured output; response_format json_object доступен только в non-thinking. qwen3.8-max-preview thinking не отключает → strict JSON структурно невозможен, в BASE НЕ вносить (нет карточки, лицензии, цены). JSON errors → response_format + слово "JSON"; G18 bailian/ prefix обязателен. DEADLINE 2026-10-10: снятие пяти qwen3-*/3.6-*.
  Kimi: K3 GA 16.07 (3/15, ctx 1,048,576, thinking always-on) — Arena WebDev #1, но ACCESS-RISK: только hosted, приём подписок приостановлен, веса не опубликованы → НЕ primary, держать запасной путь. K2.6 (Swarm 300 async) + K2.7-Code (open-weight) + Code HighSpeed tier. Type M (infinite-repeat) документирован для K2.5/K2.6; на K3 не воспроизводился, обход «отключить Thinking» там неприменим. DEADLINE 2026-08-31: гасятся k2.5 и часть moonshot-v1.
  GLM: glm-5.2 (1M, MIT, WebDev #4) основной — цена ~1.40/4.40 UNCONFIRMED (единственный источник, внутренне противоречив, официальной страницей не подтверждён) → в canon не принята. Сильнейший open-weight, у которого веса ДЕЙСТВИТЕЛЬНО опубликованы. OpenRouter AI Gateway stream-break: DISPUTED, взвешено В СТОРОНУ ОТКРЫТОГО — первичная проверка тикета показала, что он открыт и PR не привязан; корень в SSE-событиях из одних комментариев, задевает любого провайдера с таким поведением → путь через этот шлюз обходить. glm-5.1 (eff ~120K, G19); /compact hang на 5.1.
  NEW_VENDORS: MiniMax M3 ($0.30/$1.20, track-only); Manus 1.6 Max (GEOPOLITICAL CRISIS — Meta unwinding $2B; track-only, avoid prod).
  DEADLINES (from 2026-07-26): 2026-08-05 claude-opus-4-1 RETIRES; 2026-08-26 OpenAI Assistants API shutdown (вкл. Azure); 2026-08-31 Sonnet 5 intro → 3/15; 2026-08-31 kimi-k2.5 sunset; 2026-10-10 снятие пяти qwen3-*/qwen3.6-*.
