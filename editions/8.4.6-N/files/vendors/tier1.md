---
id: vendors_tier1_v8N
version: 8.4.6-N
type: VENDOR_PROFILE
tier: 1
priority: REFERENCE
compatible_with: "!!db_v8N.md | _live/live_vendors.md"
---

// ═══════════════════════════════════════════════════════
// P2P — VENDORS TIER 1
// Flagship models: Claude Opus 5 (PRIMARY), Fable 5, Opus 4.8, Opus 4.7 (legacy),
//                  GPT-5.6/5.5, Gemini 3.6 Flash / 3.5 Flash-Lite / 3.1 Pro
// ═══════════════════════════════════════════════════════
// OVERRIDE: live_specs > live_vendors.md > этот файл при конфликтах.

// ─────────────────────────────────────────────────────
// §0-a. CLAUDE OPUS 5  (PRIMARY — GA 2026-07-24)
// ─────────────────────────────────────────────────────

CLAUDE_OPUS_5:
  api_string:     claude-opus-5
  context:        1M | output: 128K
  pricing:        $5/$25 per M in/out
  strengths:      general reasoning, agentic, long-horizon; новый флагман, заменил Opus 4.8
                  как дефолтную тяжёлую модель. Default на Max, топ-модель на Pro.
  arch:           XML_NATIVE
  thinking:       ВКЛЮЧЁН ПО УМОЛЧАНИЮ (отличие от Opus 4.x, где был opt-in) — явно включать не нужно
  classifiers:    срабатывают заметно реже, чем на Fable 5 (направление подтверждено; точная величина —
                  вторичный источник, методика не опубликована → в качестве канона не использовать)

  KNOWN_ISSUES:
    G6: новый токенизатор → ~+30% токенов (официальная цифра, одна, не вилка).
    G7: temperature/top_p/top_k → HTTP 400 (как у всей линейки Claude).
    AUTOMATIC_FALLBACKS: параметр `fallbacks` + beta-header server-side-fallback-2026-06-01;
        цель — Opus 4.8. НАБЛЮДАЕМО: content block {"type":"fallback"} + usage.iterations;
        биллинг расщепляется по моделям; в app/Claude Code отключаемо.

  WHEN_TO_USE:
    T3-T4 primary: general reasoning, agentic, long-horizon, сложный код.
    Fallback chain: claude-opus-5 → claude-opus-4-8 → claude-sonnet-5

ℹ️ Стоит проверить вживую: смена primary с Opus 4.8 на Opus 5 · сценарий: сложный code-audit
   и long-horizon agentic прогон · на что смотреть: thinking включён по умолчанию — не выросли ли
   время ответа и расход токенов там, где раньше хватало Opus 4.8 без thinking.

// ─────────────────────────────────────────────────────
// §0. CLAUDE FABLE 5  (frontier — COST-GATED с 2026-07-20)
// ─────────────────────────────────────────────────────

CLAUDE_FABLE_5:
  api_string:     claude-fable-5
  arena_elo:      Text/Vision/Img2WebDev #1; Agent Net Improvement #1 (12.72%, было 14.10%)
  context:        1M | output: 128K
  pricing:        $10/$50 per M in/out | batch $5/$25 | cache-hit input $1/1M
  access:         ⚠ USAGE CREDITS с 2026-07-20 — plan-include закончился 19.07, третьего продления
                  не было. Каждый токен платный. В автоматические циклы и sub-agent оркестрацию
                  НЕ ставить: только явный вызов оператора и с бюджетом.
  strengths:      Frontier: Text/Vision #1, agentic workflows, high-quality text
  arch:           XML_NATIVE (на Claude-хосте); host-gated для генерации под другие модели
  thinking:       {"type":"adaptive"} | effort low|medium|high|xhigh|max (НЕ temperature при thinking — G7)

  KNOWN_ISSUES:
    CLASSIFIER_FP: safety-classifier даёт FP на security/coding → молчаливый fallback на Opus 4.8
                  (UNRESOLVED BY DESIGN). Точная доля ложных срабатываний НЕ опубликована —
                  ходившие «<5% сессий» и «на 85% реже у Opus 5» найдены только в интервью и медиа,
                  без методики → вторичные, каноном не считать.
                  → security/pentest → Opus 5 или Opus 4.8; fallback теперь наблюдаем через
                    content block {"type":"fallback"}, а не угадывается по качеству вывода.
    G7: temperature + thinking → HTTP 400 (как у всей линейки Claude).

  WHEN_TO_USE:
    T3-T4 frontier/vision — ТОЛЬКО по явному вызову оператора (cost-gated).
    Fallback chain: claude-fable-5 → claude-opus-5 → claude-sonnet-5

// ─────────────────────────────────────────────────────
// §0b. CLAUDE OPUS 4.8  (NEW — v8.4)
// ─────────────────────────────────────────────────────

CLAUDE_OPUS_48:
  api_string:     claude-opus-4-8
  arena_elo:      Code top-tier; SWE-bench Pro 69.2%
  context:        1M | output: 128K
  pricing:        $5/$25 per M in/out
  status:         ACTIVE, НЕ депрекирован. Retirement-даты нет; официальный порог —
                  «не ранее 2027-05-28». ⚠ Убран из селектора приложения 2026-07-24: это решение
                  о поверхности, НЕ депрекация. Сборка, читающая видимость в UI как сигнал
                  доступности, разойдётся с реальностью. API-путь сохранять.
  strengths:      Coding, reasoning; GraphWalks F1 1M: 68.1% (+27.8pp vs 4.7);
                  цель Automatic Fallbacks для Fable 5 / Opus 5
  arch:           XML_NATIVE
  thinking:       {"type":"adaptive"} | effort low|medium|high|xhigh|max

  KNOWN_ISSUES:
    G6: новый токенизатор → ~+30% токенов (официальная цифра).
    G7: temperature + thinking → HTTP 400. Delete temperature from payload.
    G8: MRCR v2 1M = 32.2% (vs 78.3% Opus 4.6). Pin claude-opus-4-6 for >500K recall.

  WHEN_TO_USE:
    Coding/reasoning; стабильный выбор когда Fable 5 classifier-FP нежелателен.
    НЕ для: >500K recall (→ Opus 4.6), документов (→ Opus 4.6, Document #1).

// ─────────────────────────────────────────────────────
// §0b-2. CLAUDE OPUS 4.1  — RETIRES 2026-08-05
// ─────────────────────────────────────────────────────

CLAUDE_OPUS_41:
  api_string:     claude-opus-4-1-20250805
  status:         ⚠ DEPRECATED 2026-06-05 → RETIRES 2026-08-05
  replacement:    claude-opus-4-8 (по официальной таблице депрекаций)
  NOTE:           таблица называет заменой Opus 4.8, а не Opus 5 — похоже, её не обновляли после
                  выхода Opus 5. На маршрутизацию не влияет: обе модели активны.

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
    G6: новый токенизатор → ~+30% токенов против моделей старше Opus 4.7 (официальная цифра,
        одна, не вилка; счётчик — официальный Token Counting API, все активные модели).
    G7: temperature + thinking → HTTP 400.

  WHEN_TO_USE:
    Баланс цена/качество T2-T3, cost-efficient agentic; заменил RETIRED Sonnet 4.6 как default.
    Agent-борд #5 при доле цены Opus — рабочий выбор для агентных задач в N.

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
    G6: новый токенизатор → ~+30% токенов vs модели старше 4.7 (официальная цифра).
        Счётчик — официальный Token Counting API. Fast mode у 4.7 УДАЛЁН (2026-07-24).
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
  pricing:        Sol $5 in / $0.50 cached / $30 out | Terra $2.50/$15 | Luna $1/$6
                  Sol long-context (>272K): $10 in / $45 out — но CACHED INPUT EXEMPT, остаётся $0.50
                  ⚠ Terra и Luna: long-context ставки НЕ ДОКУМЕНТИРОВАНЫ. Порог 272K и множители
                    расписаны только для Sol. Ходившие Terra $5/$22.5 и Luna $2/$9 — экстраполяция
                    сторонних калькуляторов, не данные вендора → в canon не вносить.
                  ⚠ Окно контекста Luna официальной строки НЕ имеет (в разделе Models есть строки
                    для 5.5 и 5.4, для Luna — нет). Ни 1.05M/128K, ни 400K/64K не подтверждены.
  strengths:      Sol flagship code/agentic (Terminal-Bench 88.8%); Terra balanced; Luna cheap/fast
  legacy:         gpt-5.5 / gpt-5.5-pro ($30/$180) остаются для Codex computer_use
  ⚠ ALIAS_TRAP:   голый `gpt-5.6` резолвится в Sol — самый дорогой уровень. Всегда пинить terra/luna.

  KNOWN_ISSUES:
    G9: >7 MUST/MUST NOT pairs → silent quality downgrade.
    G10: >272K input → ×2 UNCACHED input / ×1.5 output на весь запрос (BY DESIGN; 5.4/5.5/5.6).
         КЛЮЧЕВОЕ: cached input EXEMPT — скидка на кэш 90% переживает обрыв, поэтому для нагрузки
         со стабильным префиксом переход через 272K может быть приемлем. Решать по доле попаданий
         в кэш, а не по сырому числу токенов. Перехват 250K, жёсткий обрыв 260K.
         ⚠ У xAI порог устроен ИНАЧЕ: 200K, и там удваивается также кэш — одна общая заглушка
           два случая не описывает.
    SOL_AGENTIC_HAZARD: **шире, чем игра с бенчмарками.** System card самого вендора документирует
         у Sol удаление файлов без запроса и использование неавторизованных учётных данных.
         → Sol исключён из ролей judge/verifier И из любого harness с доступом на запись в ФС
           или к хранилищу секретов — без явного allowlist и журнала аудита.
           Существующие агентные harness'ы с такими правами — пересмотреть, а не просто пометить.
    SOL_REWARD_HACKING: METR — самый высокий уровень обхода проверок среди публично оценённых
         моделей; зафиксированы эксплуатация багов окружения и извлечение скрытых ответов.
         Оценки time-horizon в результате нестабильны и не годятся как метрика способностей.
         Независимых воспроизведений протокола с опубликованными данными НЕТ — остальное
         пересказывает METR. Отзыва бенчмарков не было (MONITORING).
    SILENT_DOWNGRADE: обслужена не та модель, что запрошена. ДЕТЕКТИРУЕТСЯ: сверять
         `resolved_model_slug`, а НЕ `model_slug` — расхождение видно в теле ответа,
         harness должен отвергать такой ответ, а не только подозревать.
    GHOST_USERS: лишний «призрачный» пользователь → падает единичное пропорциональное списание
         за место → деактивируется ВЕСЬ workspace, включая уже оплаченные места и годовую
         предоплату; владелец при этом не может дойти до биллинга, чтобы это исправить.
         → пока открыто, не брать годовую предоплату на Business-workspace.
    LUNA_MRCR: collapse >512K — не для deep long-doc.
    ASSISTANTS_API_SHUTDOWN: /v1/assistants, /v1/threads (вкл. Azure OpenAI) — полное отключение
         2026-08-26, автоматической миграции threads НЕТ. Мигрировать на Responses API.

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

GEMINI_36_FLASH:  // GA 2026-07-21 — новый workhorse, вытеснил 3.5 Flash
  api_string:     gemini-3.6-flash
  context:        1,048,576 | output: 65,536
  pricing:        $1.50/$7.50 per M | cache-read $0.15 | ~304 tok/s
  strengths:      дешёвый bulk, нативный Computer Use (встроен в API, внешняя GUI-обёртка не нужна),
                  на 17% меньше выходных токенов чем 3.5 Flash
  ⚠ SKEPTICISM:   независимый индекс интеллекта у 3.6 Flash = 50, ТОЧНО как у 3.5 Flash.
                  Экономия токенов — это лаконичность ответа, а не рост способностей.
  ⚠ ERROR_13:     G13 на 3.6 Flash НЕ ВОСПРОИЗВЕДЁН И НЕ ПРИЗНАН. Модель **не проверена** на этот
                  баг, а не **очищена** от него. Ни launch-пост, ни страница модели, ни changelog
                  Error 13 не упоминают; сообщения сообщества идут против СТАРОЙ линии 3 Flash.
                  → обходы G13 применять и здесь: Context Caching API, история ≤80K, без пачек
                    30+ изображений — особенно на длинных не-английских контекстах.
  ⚠ NOT_PUBLIC:   внутренний маршрут gemini-3.6-flash-tiered (Antigravity) — НЕ публичный API-id.

GEMINI_35_FLASH_LITE:  // GA 2026-07-21 — самый дешёвый уровень
  api_string:     gemini-3.5-flash-lite
  context:        1M | output: 64K | ~350 tok/s
  pricing:        $0.30/$2.50 per M
  strengths:      самая дешёвая hosted-опция с 1M контекстом
  NOTE:           вместе с ней вышла gemini-3.5-flash-cyber (GA 21.07), характеристики TBD →
                  до появления спецификаций держать вне BASE-маршрутизации.

GEMINI_31_PRO:
  api_string:     gemini-3.1-pro-preview
  arena_elo:      Search #6 (grounding); Text strong
  context:        2M (reliable up to 500K)
  pricing:        $2/$12 per M (≤200K)
  strengths:      Long context (2M), Google Search native, multimodal
  NOTE:           Gemini 3.5 Pro (gemini-3.5-pro-preview, 2M) — ТРЕТИЙ пропуск срока GA (17.07).
                  Суффикс -preview в официальном changelog не снят, цена не финализирована,
                  даты GA нет. НЕ трактовать как GA и не строить на ней планов.

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

FILE_META:
  MODELS:      Claude Opus 5 (PRIMARY), Fable 5, Sonnet 5, Opus 4.8, Opus 4.7, GPT-5.6 Sol/Terra/Luna,
               Gemini 3.6 Flash, Gemini 3.5 Flash-Lite, Gemini 3.1 Pro
  COMPATIBLE:  !!db_v8N.md | _live/live_vendors.md
