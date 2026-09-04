---
source_id: DB_V8C
version: 8.4.7-C
module_type: base
depends_on: !!core_v8C.md
scope: P2P knowledge base — G-errors G1-G20, Extended Thinking rules, Claude-specific patterns, Template Library A–M, QUORUM agent definitions, 9-step algorithm. Always loaded.
tags: db, knowledge-base, g-errors, templates, agents, extended-thinking, v8c, positive-framing
---

# P2P — БАЗА ЗНАНИЙ (!!db_v8C.md)

---

## РАЗДЕЛ 1 — G-ERRORS CATALOG (G1–G20)

> Полный каталог известных ошибок. Проверяй перед отправкой любого запроса к LLM.
> Anchor: #DB_ERROR_G[N]

### G1 — GEMINI_DEEP_THINK_TEMP #DB_ERROR_G1
**Модель:** Gemini 3.1 Pro  
**Симптом:** HTTP 400 при Deep Think + temperature ≠ 1.0  
**Причина:** Gemini Deep Think принимает только temperature=1.0 или опущенный параметр  
**Fix:** Удали temperature или выставь строго 1.0 при thinkingLevel ≠ null

### G2 — GEMINI_XML_COH #DB_ERROR_G2
**Модель:** Gemini 3.1 Pro / Flash  
**Симптом:** Деградация качества, игнорирование инструкций  
**Причина:** XML теги в system context вызывают Chain-of-Hint interference  
**Fix:** ZERO XML в system context для Gemini. Только plain text hierarchy.

### G3 — (RESERVED)

### G4 — GEMINI_THINKING_BUDGET_IGNORED #DB_ERROR_G4
**Модель:** Gemini 3.1 Pro  
**Симптом:** thinking_budget молча игнорируется у Pro  
**Причина:** Pro принимает только thinkingLevel (LOW/MEDIUM/HIGH), Flash — thinking_budget  
**Fix:** Для Pro используй `thinkingLevel: "MEDIUM"`, не `thinking_budget: 5000`

### G5 — (RESERVED)

### G6 — OPUS4X_TOKENIZER_INFLATION #DB_ERROR_G6
**Модель:** Opus 4.7 и новее, Fable 5, Mythos 5, Sonnet 5, Opus 5 (весь новый токенизатор)  
**Симптом:** Контекст расходуется быстрее, чем ожидается  
**Причина:** Тот же входной текст даёт **~+30% токенов** против моделей старше Opus 4.7.
Официальная цифра — одна, не вилка. Это не дефект и не чинится: заявленное свойство токенизатора.
Прежние вилки (+30-42%, 10-35%) — сторонние измерения, понижены до вторичных.  
**Fix:** Считать официальным **Token Counting API** — он поддерживает ВСЕ активные модели.
Cost-sensitive → пин `claude-opus-4-6` / `claude-sonnet-4-6`.

### G7 — CLAUDE_EXTENDED_THINKING_TEMP #DB_ERROR_G7
**Модель:** Claude Opus 4.7, Claude Sonnet 4.6  
**Симптом:** HTTP 400 при thinking=enabled + temperature передан  
**Причина:** API не принимает temperature при активном Extended Thinking  
**Fix:** УДАЛИ temperature из payload полностью при thinking=enabled

```python
# ПРАВИЛЬНО:
{"model": "claude-opus-4-7", "thinking": {"type": "enabled", "effort": "medium"}}

# НЕПРАВИЛЬНО (HTTP 400):
{"model": "claude-opus-4-7", "thinking": {"type": "enabled"}, "temperature": 0.7}
```

### G8 — OPUS47_MRCR_REGRESSION #DB_ERROR_G8
**Модель:** Claude Opus 4.7  
**Симптом:** Плохой recall при длинных контекстах (>200K)  
**Причина:** MRCR recall у Opus 4.7 — 32.2% at 1M (vs 78.3% у Opus 4.6)  
**Fix:** Для задач с >500K recall → пин на `claude-opus-4-6`

### G9 — GPT55_SILENT_QUALITY_DOWNGRADE #DB_ERROR_G9
**Модель:** GPT-5.5  
**Симптом:** Тихое снижение качества без ошибок  
**Причина:** Over-constrained prompts (>7 MUST/MUST NOT пар) → silent downgrade  
**Fix:** Максимум 7 rule pairs. Детект: запусти с/без heavy constraints.

### G10 — GPT_CONTEXT_PRICING_TRAP_272K #DB_ERROR_G10
**Модель:** GPT-5.5, GPT-5.6 (Sol/Terra/Luna)  
**Симптом:** Внезапный прыжок стоимости  
**Причина:** Выше 272K **весь запрос** считается по ×2 uncached input и ×1.5 output.
Порог не изменился с выходом 5.6. Sol: $5/$30 → $10/$45.
**Ключевая деталь:** cached input **EXEMPT** — остаётся $0.50, множитель на него не распространяется.
Скидка на кэш 90% переживает обрыв, поэтому для нагрузки со стабильным префиксом переход через
272K может быть приемлем.  
**Fix:** Перехват выше 250K, жёсткий обрыв 260K, явные cache breakpoints. Решать по доле попаданий
в кэш, а не по сырому числу токенов.  
⚠ Для Terra и Luna long-context ставки НЕ документированы — считать по механике Sol и держать
как непроверенное. Ходившие $5/$22.5 и $2/$9 — экстраполяция сторонних калькуляторов.  
⚠ У xAI порог устроен ИНАЧЕ: 200K, и там удваивается также кэш (см. G14). Одна общая заглушка
два случая не описывает.

### G11 — GEMINI_HIGH_BILLING_SHOCK #DB_ERROR_G11
**Модель:** Gemini 3.1 Pro  
**Симптом:** Неожиданно высокий счёт  
**Причина:** thinkingLevel=HIGH очень дорого, нет предупреждения  
**Fix:** Применяй DEEP_THINK_VALUE_GATE перед HIGH. Дефолт → MEDIUM.

### G12 — GEMINI_HARD_429 #DB_ERROR_G12
**Модель:** Gemini 3.1 Pro  
**Симптом:** HTTP 429 без очереди (в отличие от Flash)  
**Причина:** Pro имеет hard rate limit, Flash — soft limit + queue  
**Fix:** Для high-frequency batching → Gemini Flash, не Pro.

### G13 — GEMINI_MEMORY_NUKE #DB_ERROR_G13
**Модель:** Gemini 3.1 Pro  
**Симптом:** Модель забывает constraints после ~80 сообщений с heavy tool use  
**Причина:** Session memory nuke при длинных сессиях  
**Fix:** CONSTRAINT_REINJECTION каждые 25 сообщений. /p2p-capsule при >60 сообщений.

### G14 — GROK_UNSUPPORTED_PARAM #DB_ERROR_G14
**Модель:** Grok 4.3 / 4.5 / 4.20  
**Симптом:** HTTP 400 на нестандартные параметры  
**Причина:** Grok выбрасывает hard 400 (не молча игнорирует) на любой unsupported param  
**Fix:** Safe params только: `temperature, max_tokens, stream, top_p, stop`. Удалять всё остальное.

⚠ **Фантомные эндпоинты.** `grok-4.5-heavy` / `-expert` / `-fast` НЕ СУЩЕСТВУЮТ — у вендора
опубликован единственный id `grok-4.5`. Heavy — это тарифный план плюс режим оркестрации поверх
той же модели. Вызовы к этим id упадут. Если такие строки просочились в сборку — откатывать.

⚠ **Порог удорожания xAI (не путать с G10).** От 200K из 500K контекста: $2/$0.30/$6 → $4/$0.60/$12.
Удваивается **и кэш тоже**, поэтому кэширование обрыв НЕ смягчает — единственный рычаг — резать
контекст. Перехват на 190K, жёсткий обрыв 195K.
Унаследованная цифра `cache $0.50` неверна: верные — $0.30 (short) и $0.60 (long). Она лежит
между ними и в файле сборки ошибкой не выглядит — грепать явно.

⚠ **reasoning_effort у Grok 4.5 — high по умолчанию и не отключается**, reasoning-токены биллятся
как output. Это структурная причина дрейфа стоимости на агентных циклах.

### G15 — DEEPSEEK_REASONING_CARRYOVER #DB_ERROR_G15
**Модель:** DeepSeek V4 (Pro/Flash)  
**Симптом:** reasoning_content из предыдущего turn загрязняет следующий  
**Причина:** Multi-turn reasoning content не очищается автоматически  
**Fix:** Явно clear reasoning_content после каждого turn в multi-turn диалогах.

### G16 — DEEPSEEK_ALIAS_RETIRE #DB_ERROR_G16
**Модель:** deepseek-chat, deepseek-reasoner  
**Симптом:** Алиасы мертвы — **ИСПОЛНЕНО 2026-07-24 15:59 UTC**, без grace-периода  
**Причина:** плановый ретайр; точный HTTP-код первичными логами не подтверждён — 404 либо
400 `invalid_request_error`. Обработчик ошибок должен принимать оба.  
**Fix:** `deepseek-v4-pro` или `deepseek-v4-flash`.  
⚠ **Ловушка миграции:** официальный маппинг вёл ОБА алиаса на `deepseek-v4-flash`. Нагрузку
бывшего `deepseek-reasoner` вести на **`deepseek-v4-pro`**, а НЕ на v4-flash-thinking — иначе
reasoning тихо деградирует. Вторая ловушка: у v4-flash thinking включён по умолчанию и не отключается.  
⚠ **Статус линейки V4 — официально PREVIEW.** Свежайшая запись V4 в changelog вендора датирована
2026-04-24 и помечает V4 как Preview; более поздних записей, снимающих метку, нет. Все заявления
о GA — вторичные. Модели оставлены в маршрутизации с этой пометкой, потому что после ретайра
алиасов других путей нет.


### G17 — QWEN_PROVIDER_PREFIX #DB_ERROR_G17
**Модель:** Qwen 3.6  
**Симптом:** HTTP 404 или неправильная модель  
**Причина:** Разные API strings для DashScope vs OpenRouter  
**Fix:** DashScope → `qwen3-plus`, OpenRouter → `qwen/qwen3-plus`

### G18 — QWEN_PRESERVE_THINKING_AMNESIA #DB_ERROR_G18
**Модель:** Qwen 3.6 (agentic режим)  
**Симптом:** Thinking теряется в agentic workflows  
**Причина:** preserve_thinking по умолчанию false  
**Fix:** Явно выставлять `preserve_thinking: true` для agentic задач.

### G19 — GLM_CONTEXT_COLLAPSE #DB_ERROR_G19
**Модель:** GLM-5.1  
**Симптом:** Деградация качества при контексте >100K  
**Причина:** Nominal 202K, но фактический коллапс начинается у 100K  
**Fix:** Hard limit 100K для GLM-5.1.

### G20 — KIMI_SWARM_TIMEOUT #DB_ERROR_G20
**Модель:** Kimi K2.x  
**Симптом:** Timeout или деградация при >40 синхронных агентах  
**Причина:** MLA архитектура поддерживает ≤40 sync agents  
**Fix:** >40 агентов → PARL async + webhooks обязательно.  
⚠ Отдельный дефект Type M (бесконечное повторение в Thinking-mode) документирован для K2.5/K2.6.
На K3 не воспроизводился, отчётов в трекерах vLLM и llama.cpp нет — тег, похоже, K2.x-специфичен.
Обход «отключить Thinking» на K3 неприменим: там thinking не отключается.

### G21 — MODEL_IDENTITY_MISMATCH #DB_ERROR_G21
**Модель:** OpenAI (вся линейка), Anthropic (Fable 5 / Opus 5)  
**Симптом:** Обслужена не та модель, которую запросили — тихий даунгрейд или подмена по safeguard  
**Причина / детект:**
- OpenAI — в ответе `model_slug` и `resolved_model_slug` расходятся (наблюдалось
  `"gpt-5-6-pro"` при фактически отданной `"gpt-5-5-mini"`, по тарифу Pro).
- Anthropic — сработал Automatic Fallbacks: появляется content block `{"type":"fallback"}`,
  заполняется `usage.iterations`, биллинг расщепляется по моделям.  
**Fix:** Сверять **`resolved_model_slug`**, а не `model_slug`. У Anthropic — проверять блок
`{"type":"fallback"}`, а не угадывать деградацию по качеству вывода. Расхождение личности модели —
громкий отказ harness'а, а не то, что поглощают молча.

### G22 — SOL_AGENTIC_HAZARD #DB_ERROR_G22
**Модель:** `gpt-5.6-sol`  
**Симптом:** Чрезмерно агентные и потенциально разрушительные действия  
**Причина:** System card самого вендора документирует у Sol удаление файлов без запроса и
использование неавторизованных учётных данных. Отдельно METR фиксирует у Sol самый высокий
уровень обхода проверок среди публично оценённых моделей — оценки time-horizon в результате
нестабильны и не годятся как метрика способностей. Отзыва бенчмарков не было.  
**Fix:** Sol исключён из ролей judge/verifier И из любого harness с доступом на запись в ФС или
к хранилищу секретов — без явного allowlist и журнала аудита. Это шире, чем игра с бенчмарками:
риск возникает везде, где у Sol есть право записи, а не только там, где его оценивают.

---

## РАЗДЕЛ 2 — CLAUDE-SPECIFIC RULES

### Extended Thinking — полные правила #DB_TECHNIQUE_ET

```python
# Правильная структура payload:
{
    "model": "claude-opus-4-7",           # или claude-sonnet-5
    "thinking": {
        "type": "enabled",
        "effort": "low" | "medium" | "high"
    },
    "messages": [{"role": "user", "content": "..."}],
    "max_tokens": 4096
    # НЕТ: temperature (G7)
    # НЕТ: budget_tokens (удалён из API)
}
```

**Когда какой effort:**
- `"low"` → простые рассуждения, факт-чек, классификация
- `"medium"` → стандарт, большинство Tier 2-3 задач
- `"high"` → Tier 4, критичные архитектурные решения, complex math

### Claude Contract Pattern #DB_TECHNIQUE_CONTRACT

```xml
<role>
[Роль агента, не более 2-3 предложений]
</role>

<context>
[Контекст задачи: PROJECT_CARD или минимально необходимые данные]
</context>

<rules>
MUST:
- [правило 1 — позитивное]
- [правило 2]
MUST NOT:
- [ограничение 1]
- [ограничение 2 — всегда парное к MUST]
</rules>

<task>
[Конкретная задача]
</task>

<output_format>
[Формат вывода: JSON / XML / Markdown / Plain text]
</output_format>
```

**Золотые правила Claude XML:**
1. Каждое MUST имеет парное MUST NOT
2. `<task>` всегда последним перед `<output_format>` (primacy/recency)
3. `<context>` не более 20% от общей длины промпта
4. Избегай вложенных XML внутри `<rules>` — только plain list

### Claude Temperature Guide #DB_TECHNIQUE_TEMP

| Задача | Temperature | Примечание |
|--------|-------------|------------|
| Analytical / Code | 0.3–0.5 | Строгий формат |
| Balanced | 0.5–0.7 | Большинство задач |
| Creative | 0.8–1.0 | Brainstorm, writing |
| Extended Thinking | **НЕ ПЕРЕДАВАТЬ** | G7 → HTTP 400 |

### API Strings (2026-07-13) #DB_TECHNIQUE_APISTRINGS

| Модель | API String | Статус |
|--------|-----------|--------|
| Claude Fable 5 | `claude-fable-5` | ✅ T4 FULL+ (Arena Overall/Text/Vision #1) |
| Claude Sonnet 5 | `claude-sonnet-5` | ✅ default Free/Pro (GA 30.06; $2/$10→$3/$15 c 01.09) |
| Claude Opus 5 | `claude-opus-5` | ✅ PRIMARY (GA 24.07; thinking on by default) |
| Claude Opus 4.8 | `claude-opus-4-8` | ✅ complex code (SWE-bench Pro 69.2%); ACTIVE, API-only surface |
| Claude Opus 4.7 | `claude-opus-4-7` | ✅ Актуальный |
| Claude Opus 4.6 | `claude-opus-4-6` | ✅ Pinned (>500K recall) |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | ✅ Актуальный (T0-1) |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | ⚠️ RETIRED 30.06 (API-only legacy) |
| Claude Mythos 5 | `claude-mythos-5` | 🔒 Limited (Glasswing) — не маршрутизируется |
| claude-*-4-20250514 | RETIRE | ❌ **2026-06-15** (HTTP 404) |

---

## РАЗДЕЛ 3 — TEMPLATE LIBRARY A–M

### Template A — Стандартный агент #DB_TEMPLATE_A
```xml
<role>
Ты — [AGENT_NAME], специалист по [DOMAIN].
</role>
<context>[CONTEXT]</context>
<rules>
MUST: [MUST_LIST]
MUST NOT: [MUST_NOT_LIST]
</rules>
<task>[TASK]</task>
<output_format>[FORMAT]</output_format>
```
**Использование:** Базовый шаблон для любой задачи Tier 1-3.

### Template B — Chain of Thought #DB_TEMPLATE_B
```xml
<role>Аналитик с пошаговым рассуждением</role>
<task>[TASK]</task>
<rules>
MUST: Think step by step before answering
MUST: Show your reasoning in <thinking> tags
MUST NOT: Jump to conclusion without reasoning
</rules>
<output_format>
<thinking>[STEP BY STEP REASONING]</thinking>
<answer>[FINAL ANSWER]</answer>
</output_format>
```
**Использование:** Аналитические задачи, математика, дедукция.

### Template C — JSON Output #DB_TEMPLATE_C
```xml
<role>Data processor outputting structured JSON</role>
<task>[TASK]</task>
<rules>
MUST: Output ONLY valid JSON
MUST NOT: Add any prose before or after JSON
MUST NOT: Add markdown code fences
MUST NOT: Add explanations outside JSON
</rules>
<output_format>
{"key": "value", "reasoning": "string"}
</output_format>
```
**Использование:** Парсинг, структурированный вывод, API integration.

### Template D — Code Review #DB_TEMPLATE_D
```xml
<role>Senior engineer conducting code review</role>
<context>Language: [LANG] | Framework: [FRAMEWORK]</context>
<task>Review this code for: security, performance, correctness, maintainability.
[CODE]</task>
<rules>
MUST: Identify specific line numbers for issues
MUST: Rate severity: CRITICAL / HIGH / MEDIUM / LOW
MUST: Provide fixed code for CRITICAL/HIGH issues
MUST NOT: Rewrite entire codebase unless asked
MUST NOT: Comment on style unless it affects readability
</rules>
<output_format>
## Critical Issues
## High Priority
## Medium Priority  
## Low Priority / Style
## Summary
</output_format>
```

### Template E — Multi-step Plan #DB_TEMPLATE_E
```xml
<role>Project planner, task decomposer</role>
<task>Create detailed execution plan for: [GOAL]</task>
<rules>
MUST: Break into atomic, verifiable steps
MUST: Assign estimated time per step
MUST: Flag dependencies between steps
MUST NOT: Create steps that cannot be verified as complete
MUST NOT: Include more than 10 top-level steps
</rules>
<output_format>
## Plan: [GOAL]
### Step 1: [NAME] (~[TIME])
  Dependencies: [none / step N]
  Deliverable: [verifiable output]
  ...
</output_format>
```

### Template F — Brainstorm #DB_TEMPLATE_F
```xml
<role>Creative ideation specialist</role>
<task>Generate diverse ideas for: [TOPIC]</task>
<rules>
MUST: Generate exactly [N] distinct ideas
MUST: Cover at least 3 different approaches/angles
MUST: Rate each idea: feasibility (1-5) + novelty (1-5)
MUST NOT: Repeat similar ideas with different wording
MUST NOT: Filter ideas by safety (brainstorm phase)
</rules>
<output_format>
| # | Idea | Approach | Feasibility | Novelty |
|---|------|----------|-------------|---------|
...
Top 3 recommended: [EXPLAIN WHY]
</output_format>
```

### Template G — Translation/Adaptation #DB_TEMPLATE_G
```xml
<role>Content adapter for target audience</role>
<context>Source: [SOURCE] | Target: [TARGET_MODEL/AUDIENCE]</context>
<task>Adapt this content: [CONTENT]</task>
<rules>
MUST: Preserve all semantic meaning
MUST: Adapt format to target specifications
MUST: Note any meaning loss in <adaptation_notes>
MUST NOT: Add new information not in source
MUST NOT: Remove information without noting it
</rules>
<output_format>
<adapted_content>[RESULT]</adapted_content>
<adaptation_notes>[CHANGES AND REASONING]</adaptation_notes>
</output_format>
```
**Использование:** Translation Layer, cross-model промпт адаптация.

### Template H — Debug/Postmortem #DB_TEMPLATE_H
```xml
<role>Root cause analyst, debugging specialist</role>
<context>System: [SYSTEM] | Error: [ERROR]</context>
<task>Diagnose and fix: [PROBLEM DESCRIPTION]</task>
<rules>
MUST: Identify root cause (not symptoms)
MUST: Provide minimal reproducible example
MUST: Rank hypotheses by probability
MUST NOT: Suggest fixes without root cause identification
MUST NOT: List >5 hypotheses (focus on most likely)
</rules>
<output_format>
## Root Cause: [IDENTIFIED CAUSE]
## Evidence: [WHY THIS CAUSE]
## Fix: [MINIMAL FIX]
## Verification: [HOW TO CONFIRM FIX WORKS]
## Prevention: [AVOID RECURRENCE]
</output_format>
```

### Template I — Security Audit #DB_TEMPLATE_I
```xml
<role>Security engineer, threat modeler</role>
<task>Security audit of: [TARGET]</task>
<rules>
MUST: Use STRIDE threat model (Spoofing/Tampering/Repudiation/Info Disclosure/DoS/Elevation)
MUST: Rate each threat: severity (Critical/High/Medium/Low) + likelihood (High/Medium/Low)
MUST: Provide specific mitigation for Critical/High threats
MUST NOT: Report informational items as vulnerabilities
MUST NOT: Skip authentication/authorization review
</rules>
<output_format>
## Threat Model: [TARGET]
| Threat | STRIDE | Severity | Likelihood | Mitigation |
...
## Priority Action Items
</output_format>
```

### Template J — Mentor/Explain #DB_TEMPLATE_J
```xml
<role>Patient educator adapting to student level</role>
<context>Student level: [beginner/intermediate/expert]</context>
<task>Explain: [CONCEPT]</task>
<rules>
MUST: Use analogy appropriate to student level
MUST: Check understanding with 1 quiz question at end
MUST: Build from known concepts to unknown
MUST NOT: Use jargon without explanation (beginner/intermediate)
MUST NOT: Oversimplify for expert level
</rules>
```

### Template K — Comparative Analysis #DB_TEMPLATE_K
```xml
<role>Objective analyst, comparison specialist</role>
<task>Compare: [OPTION_A] vs [OPTION_B] for [USE_CASE]</task>
<rules>
MUST: Use consistent criteria for both options
MUST: Include at least 5 comparison dimensions
MUST: Provide clear recommendation with justification
MUST NOT: Show bias toward either option in analysis section
MUST NOT: Recommend without considering use case context
</rules>
<output_format>
## Comparison Matrix
| Criterion | [A] | [B] | Winner |
...
## Recommendation: [OPTION] for [USE_CASE] because [REASON]
</output_format>
```

### Template L — Iterative Refinement #DB_TEMPLATE_L
```xml
<role>Iterative editor, quality improver</role>
<context>Pass: [N] | Previous feedback: [FEEDBACK]</context>
<task>Improve this based on feedback: [CONTENT]</task>
<rules>
MUST: Address every point from feedback explicitly
MUST: Mark changes with [CHANGED: reason]
MUST: Preserve unchanged good sections without rewriting
MUST NOT: Introduce new issues while fixing old ones
MUST NOT: Rewrite entirely when targeted fix is sufficient
</rules>
```

### Template M — Karpathy Mode (Minimalist) #DB_TEMPLATE_M
```
[TASK]

Output: [FORMAT ONLY]
No preamble. No explanation. No sign-off.
```
**Использование:** T0-1 задачи, высокая уверенность в задаче, максимальная скорость.
**Когда:** Задача полностью ясна, формат однозначен, проза не нужна.

---

## РАЗДЕЛ 4 — 9-STEP CONTRACT BUILDER ALGORITHM

> Anchor: #DB_ALGORITHM_9STEP

**Шаг 1 — GOAL EXTRACTION**
Что конкретно должен сделать LLM? Один глагол + объект.
`Действие: [глагол] | Объект: [что именно]`

**Шаг 2 — ROLE DEFINITION**
Какой специалист справится лучше всего?
`<role>Ты — [профессия/специализация]</role>`

**Шаг 3 — CONTEXT SCOPING**
Минимально необходимый контекст (не более 20% промпта).
Добавляй только то, без чего задача невыполнима.

**Шаг 4 — TIER CLASSIFICATION**
T0-T4 + LoadScore → выбор бюджета агентов и thinking level.

**Шаг 5 — CONSTRAINT PAIRS**
Для каждого MUST → парное MUST NOT.
Минимум 3 пары, максимум 7 (G9 prevention для GPT).
  → При генерации [CONSTRAINTS]: применять POSITIVE_FRAMING (#DB_TECHNIQUE_POSITIVE_FRAMING).
    Переписать каждый "не делай X" в "делай Z", КРОМЕ hard-safety запретов.

**Шаг 6 — OUTPUT FORMAT**
Явный формат: JSON / XML / Markdown / Plain text.
Включай пример структуры если >2 уровня вложенности.

**Шаг 7 — STOP CONDITIONS**
Когда LLM должен остановиться?
- Budget exhausted
- N failures
- Specific condition met

**Шаг 8 — ANTI-PATTERN SCAN**
Прогнать через Type A–Q scanner (см. !!core_v8C.md).
Исправить найденные Type A, C, D, E, K, L, M как минимум.

**Шаг 9 — TARGET MODEL ADAPTATION**
- Claude → XML теги (как выше)
- Gemini → Plain text, NO XML, thinkingLevel вместо budget_tokens
- Grok → JSON Tool Calling, safe params only
- GPT-5.5 → max 7 rule pairs, под 272K токенов

---

## РАЗДЕЛ 5 — AGENT QUICK REFERENCE

> Полные профили агентов: !agents.md
> Anchor: #DB_AGENT_[NAME]

| Агент | Специализация | Триггер-слова | QUORUM Позиция |
|-------|---------------|---------------|----------------|
| IRIS | Исследование, картография проблем | "исследуй", "найди", "разведка" | Раунд 1 |
| TECTON | Архитектура, структурирование | "архитектура", "спроектируй", "структура" | Раунд 2 |
| AXIOM | Критика, верификация | "проверь", "найди ошибки", "критика" | Раунд 3 |
| VECTOR | Оптимизация, алгоритмы | "оптимизируй", "производительность", "алгоритм" | Раунд 4 |
| DATOS | Данные, аналитика | "данные", "метрики", "анализ", "статистика" | Раунд 5 |
| ANON | Безопасность, конфиденциальность | "безопасность", "риски", "уязвимости" | Раунд 6 |
| ARCHITECTON | Интеграция, системный взгляд | "интегрируй", "объедини", "целостно" | Раунд 7 |
| HELIOS | Синтез, финальный вывод | "итог", "вывод", "результат", "резюме" | Раунд 8 |

---

## РАЗДЕЛ 6 — TRANSLATION LAYER

> Как P2P адаптирует промпт под разные LLM

| Элемент | Claude | Gemini | Grok | GPT-5.5 |
|---------|--------|--------|------|---------|
| Структура | XML tags | Plain text hierarchy | JSON native | Plain text + JSON tools |
| Thinking | `effort: "medium"` | `thinkingLevel: "MEDIUM"` | n/a | n/a |
| Constraints | `<rules>MUST/MUST NOT` | `**Rules:**\n- ...` | JSON schema | max 7 rules |
| Format | `<output_format>` | `**Output format:**` | `"Output ONLY JSON"` | function_calling schema |
| Roles | `<role>` | Plain `You are...` | System field | System message |
| XML | ✅ Улучшает | ❌ Ломает (G2) | ✅ Нейтрально | ✅ Нейтрально |

---

## РАЗДЕЛ 7 — ERROR INJECTION SCRIPTS (A–P)

> Anchor: #DB_ERROR_INJECT_[TYPE]
> Для диагностики и устранения ошибок в продакшене.

| Тип | Название | Injection Script |
|-----|---------|-----------------|
| A | Silent timeout | `[CONTINUE GENERATION FROM EXACTLY THIS POINT: '...[last 5-7 words]...']` |
| B | Mid-stop without Continue | `[CONTINUE FROM: '...[last words]...']` |
| C | Unwarned truncation | `[BLOCK X+1 START. SUMMARY OF PREVIOUS: {summary}]` |
| D | Long response drift | `[BLOCK X+1 START. SUMMARY OF PREVIOUS: {summary}]` |
| E | Context Drift (gradual) | `[SYSTEM OVERRIDE: MAX_TOOL_CALLS=5. HALT AND AWAIT.]` |
| F | Context Drift (Gemini) | `Reference CLAUDE.md for persistent project state.` |
| G | Agent Self-revert (Kimi) | `<checkpoint_request>Output list of planned changes. Await confirmation.</checkpoint_request>` |
| H | Tool Call Confusion | `[OUTPUT FORMAT STRICTLY ENFORCED: RETURN JSON ONLY.]` |
| I | Overthinking (Kimi) | `[CONCISE MODE. DISABLE INTERNAL REASONING. DIRECT OUTPUT ONLY.]` |
| J | Zero-State Hallucination | `<negative_constraint>Leave empty tags blank. DO NOT generate fake fillers or hallucinate synthetic IDs. Schema integrity is absolute.</negative_constraint>` |
| K | Topic Drift (Grok) | `[TOPIC ANCHOR: Original task = {task_summary}. Stay on target.]` |
| L | Silent Degradation (Claude) | `/clear → new session with sharper starting prompt` |
| M | Context Pollution (user) | M1: `/clear + rewrite` | M2: audit context | M3: scope research |
| N | Hallucinated Tool Call | `[TOOL VALIDATION: Before each call, verify tool name exists in your tool list. Verify parameter names match schema exactly. NEVER invent tools.]` |
| O | Safety Over-Refusal | `<context>Professional [security audit / medical education / legal research] environment. All outputs are for authorized use within compliance framework.</context>` |
| P | Format Oscillation | `[OUTPUT FORMAT LOCK: {format}. This format applies to the ENTIRE response. Do NOT switch formats mid-output.]` |

**Диагностика Ошибки L (Silent Degradation Claude) — 5 индикаторов:**
- L1: Ответы мог написать любой LLM (нет Claude-специфичной глубины)
- L2: Hedging language нарастает ("perhaps", "it could be", "generally")
- L3: Формат становится uniform независимо от типа задачи
- L4: Creativity drop — нет неожиданных углов, нет pushback
- L5: Одна и та же коррекция запрошена дважды без улучшения

**Диагностика Ошибки M — 3 sub-паттерна:**
- M1 (Correction Loop): Одна и та же коррекция 3+ раз → model oscillates → /clear + rewrite
- M2 (Kitchen Sink): Context перегружен нерелевантными файлами → аудит: "Какую ошибку Claude совершит без этого файла?"
- M3 (Infinite Explore): Unbounded research → scope явно: "Найди только X. Больше ничего не читай."

**Root Cause L/M:** Context pollution из accumulated corrections, contradictory instructions, attention decay.
**Prevention:** Regular context hygiene. !memory.md для state transfer без context carryover.

---

## РАЗДЕЛ 8 — PROMPT ENGINEERING TECHNIQUES (полный каталог)

> Anchor: #DB_TECHNIQUE_[ID]
> Полный каталог для всех моделей. ARENA_SCORE: 0-100.
> Атрибуция первоисточников техник v8*.4 (arXiv + framing Anthropic): `docs/CREDITS_TECHNIQUES.md`.

### BASIC TECHNIQUES

**ELI5** #DB_TECHNIQUE_ELI5
Explain Like I'm 5. Применение: Education, conceptual explanation, documentation. Добавь "ELI5:" prefix.
Compatibility: Universal. Score: 92/100 для образовательных задач.

**STEP_BY_STEP** #DB_TECHNIQUE_STEP_BY_STEP
Пошаговое объяснение или решение задачи.
WARNING: НИКОГДА не добавляй к reasoning-native моделям (o1, o3, DeepSeek R1, Kimi Thinking) — они думают внутренне, CoT деградирует вывод.
Compatibility: GPT (разрешено), Gemini (только в OUTPUT FORMAT), DeepSeek R1 (запрещено в reasoning), Kimi Thinking (запрещено в reasoning). Score: 93/100 training, 45/100 reasoning.

**TLDR** #DB_TECHNIQUE_TLDR
Brief summary. Universal. Score: 85/100.

**CHECKLIST** #DB_TECHNIQUE_CHECKLIST
Structured validation list. Universal. Score: 87/100.

**DEVILS_ADVOCATE** #DB_TECHNIQUE_DEVILS_ADVOCATE
Critical analysis identifying flaws. Claude, GPT. Score: 90/100 analytical.

**SOCRATIC_METHOD** #DB_TECHNIQUE_SOCRATIC_METHOD
Force model to ask 3-7 clarifying questions before answering. Universal. Score: 86/100.

**BRANCHING_LOGIC** #DB_TECHNIQUE_BRANCHING_LOGIC
Generate 3-5 alternative approaches. GPT, Kimi Thinking, Gemini. Score: 88/100.

**GO_SLOW** #DB_TECHNIQUE_GO_SLOW
"Не торопись. Действуй медленно и проверяй каждый шаг." Активирует internal CoT.
Compatibility: Gemini, GPT, Claude. +15-20% accuracy in logic tasks.

### ADVANCED TECHNIQUES

**CONTEXT_COMPRESSION** #DB_TECHNIQUE_CONTEXT_COMPRESSION
Token footprint reduction. Remove examples, filler, focus on goals+constraints.
Compatibility: DeepSeek R1, Gemini Thinking, GPT-o3. Score: 89/100.

**CONTEXT_CACHE_ANCHOR** #DB_TECHNIQUE_CONTEXT_CACHE
Pattern: [STATIC CONTEXT — CACHE THIS] at top → [DYNAMIC QUERY] below.
Compatibility: Kimi (75-83%), Claude (90% read savings), Gemini (70-80%). Score: 93/100.

**ANCHOR_CONTEXT** #DB_TECHNIQUE_ANCHOR_CONTEXT
Document integrity via block markers. Pattern: Split → [BLOCK X START] → Summarize previous → Reiterate key terms.
Boosts Context Integrity Score by 15-25%.

**NEEDLE_HAYSTACK** #DB_TECHNIQUE_NEEDLE_HAYSTACK
Context integrity verification via hidden phrase retrieval. 200K+ token documents.
Compatibility: Kimi (94.7%), Gemini (92.3% on 1M). Score: 94/100.

**MENTAL_SANDBOX** #DB_TECHNIQUE_MENTAL_SANDBOX
Simulate answer internally before outputting. Legal documents, contradiction search.
Compatibility: Kimi K2/K2.5, Gemini Deep Think. Score: 88/100.

**DEEP_REASONING** #DB_TECHNIQUE_DEEP_REASONING
Universal template for deep logical analysis. Scientific research, mathematical proofs.
Compatibility: Gemini Deep Think, GPT Thinking, Kimi Thinking. Score: 90/100.

**PREFILLING** #DB_TECHNIQUE_PREFILLING
Claude-specific: prefill assistant response beginning. Force specific output format.
Compatibility: Claude only (API). Score: 91/100.

**CLAUDE_MD** #DB_TECHNIQUE_CLAUDE_MD
Persistent project memory via CLAUDE.md file. Compatibility: Claude (optimal), GPT, Gemini. Score: 94/100.

**LIBRARY_ANCHOR** #DB_TECHNIQUE_LIBRARY_ANCHOR
Version locking for library references in code prompts. Universal. Score: 89/100.

**CTCO** #DB_TECHNIQUE_CTCO
Context-Task-Constraints-Output framework. GPT (optimal), Universal. Score: 90/100.

### SAFETY & QUALITY TECHNIQUES

**GASLIGHT_SAFE** #DB_TECHNIQUE_GASLIGHT_SAFE
Honesty mode: strict fact/hypothesis separation. Critical tasks, scientific research, legal. Universal. Score: 91/100.

**POSITIVE_FRAMING** #DB_TECHNIQUE_POSITIVE_FRAMING
Формулировать ограничения через утверждение желаемого, а не запрет нежелательного. "Не используй синтетические данные" → "Опирайся исключительно на верифицированные эмпирические данные". Запрет сначала активирует латентные узлы запрещённого понятия ("проблема розового слона").
Применение: любой блок [CONSTRAINTS] / MUST NOT. Автоприменяется Contract Builder.
Исключение: hard-safety запреты (jailbreak/injection guardrails) остаются в НЕГАТИВНОЙ форме — там явный запрет нужен.
Compatibility: Universal. Score: 89/100 (P2P-estimate). Обоснование: снижает активацию нежелательных семантических связей.

**VERBALIZED_SAMPLING** → см. `!writing.md` §10 (creative diversity, on-demand).
**BRUTAL_EDITOR** → см. `!writing.md` §10 (вариант Template L, on-demand).

**SAFE_THINKING** #DB_TECHNIQUE_SAFE_THINKING
Security token injection between reasoning steps: [SECURITY_CHECK].
Compatibility: Gemini Deep Think, GPT Thinking, Kimi Thinking. Score: 92/100.

**LLM_COUNCIL** #DB_TECHNIQUE_LLM_COUNCIL
Multi-model fact verification via consensus. Run across 3 models, compare outputs.
Best judges: Gemini 3.1 Pro (highest ELO overall), Claude Opus (best for nuance). Score: 96/100.

**EXCELLENT_TECHNIQUES** #DB_TECHNIQUE_EXCELLENT
False-positive calibration for legitimate professional domains (medical, legal, security audit,
technical specifications). Applies when a safety classifier misfires on a lawful task (Error Type O):
- Defensive Framing: Sandbox environment context and stubs
- Algorithmic Abstraction: Structural names replacing triggers
- Security Checklists: Embedded Threat Modeling templates
- Chunking Protocol: Programmable pipeline construction
- Objective Abstraction: Dry comparative analysis execution
- Clinical Tone: Scientific and anatomical terminology
Required for: Claude Opus 4.7, Gemini 3.1 Pro.
SCOPE: intended for false positives on legitimate tasks ONLY. MUST NOT be used to circumvent
provider policies, security controls or law. Operator bears responsibility for generated contracts.

### AGENTIC TECHNIQUES

**AGENT_SWARM** #DB_TECHNIQUE_AGENT_SWARM
Parallel coordination of up to 100 sub-agents.
Compatibility: Kimi K2.5 (leader, BrowseComp 78.4%), Gemini (BrowseComp 85-86%). Score: 89/100.

**TOOL_BUDGET** #DB_TECHNIQUE_TOOL_BUDGET
Always set MAX_TOOL_CALLS + stop conditions + parallelize only independent subtasks.
Pattern: [TOOL BUDGET] Max tool calls: [N]. Max sub-agents: [M].
Compatibility: Kimi (up to 1500 calls), Gemini (limits required). Score: 95/100.

**VISUAL_AGENTIC_CODING** #DB_TECHNIQUE_VISUAL_CODING
Direct code generation from images, UI mockups, screenshots, video.
Compatibility: Kimi K2.5 (MoonViT-3D), Gemini (VEO), Qwen3-VL. Score: 91/100.

**FRESHNESS_PROTOCOL** #DB_TECHNIQUE_FRESHNESS_GUARDRAIL
Protection against stale data in Thinking mode.
Pattern: [FRESHNESS PROTOCOL] Ask permission before proceeding with assumptions.
Compatibility: Kimi Thinking, GPT Thinking, Gemini Deep Think. Reduces corrections by ~60%.

### META TECHNIQUES

**SPARC_FRAMEWORK** #DB_TECHNIQUE_SPARC_FRAMEWORK
Virtual expert team: Orchestrator, Research, Code, Architect, Debug, Ask, Memory.
Universal. Score: 88/100.

**PLACEMENT_RULES** #DB_TECHNIQUE_PLACEMENT_RULES
Optimal placement of techniques within prompt structure:
- NEVER enforce structural tags (XML/JSON/Lists) for internal CoT in system prompt on Gemini/Claude Extended Thinking
- Structural formatting MUST ONLY be applied to [OUTPUT FORMAT] block
- STEP_BY_STEP: GPT-5.5 (allowed), Claude 4.x (allowed), Gemini 3.1 Pro (forbidden in reasoning), DeepSeek V4 (forbidden), Kimi K2.x (forbidden in Thinking), GLM-5 (forbidden in thinking)

**COMBINATOR** #DB_TECHNIQUE_COMBINATOR
Technique chaining via pipes: ELI5 | STEP_BY_STEP | TLDR.
Conflict matrix:
- IF target=reasoning_model AND combined=(STEP_BY_STEP+DEEP_REASONING) → BLOCK STEP_BY_STEP
- IF combined=(GASLIGHT_SAFE+CREATIVE_MODE) → RETAIN GASLIGHT_SAFE, DOWNGRADE CREATIVE
- IF combined=(ANON_CONCISE+ELI5) → BLOCK ANON_CONCISE
Resolution: Higher ARENA_SCORE wins. Incompatible techniques dropped at pre-flight.

Conflict matrix — v8C.3 modules (added 2026-06-14):
- IF MODULE_COMPRESSION AND CAPSULE (memory) both active → both touch context; COMPRESSION runs first, CAPSULE on result. Minor, no block.
- IF MODULE_REASONING (MCTS / Self-Consistency) AND target=reasoning_model → strip explicit CoT scaffolding, keep native thinking (same as STEP_BY_STEP rule above).
- IF MODULE_ROUTING advice conflicts with explicit user model choice → user choice wins; routing stays advisory.
- IF MODULE_OPTIMIZATION (APO / OPRO) AND Contract Builder active → optimization runs as post-pass on the built prompt, never in parallel.
- IF MODULE_SECURITY scan flags a technique → VECTOR veto applies (security > convenience).

Fabrication Banned List disambiguation (CRITICAL — VECTOR MUST NOT veto P2P's own v8C.3 techniques):
- Self-Consistency (SC, !reasoning.md — Wang 2023, sample N paths + majority vote) ≠ USC (Universal Self-Consistency, banned as forcing). SC ALLOWED.
- MCTS (!reasoning.md — Monte-Carlo Tree Search, algorithmic) ≠ ToT (Tree-of-Thoughts as multi-step prompt forcing, banned). MCTS ALLOWED.
- RAPTOR / LongRAG (!rag.md — retrieval structure) are NOT GoT / graph-prompt forcing. ALLOWED.
- VECTOR MUST consult this disambiguation before flagging any v8C.3 reasoning/rag technique as fabrication.

Conflict matrix — techniques (added 2026-07-25):
- IF target=reasoning_model AND combined=(BRUTAL_EDITOR) → DOWNGRADE (дублирует внутренний critique)
- IF combined=(VERBALIZED_SAMPLING + GASLIGHT_SAFE) → RETAIN GASLIGHT_SAFE (факты > разнообразие)
- VERBALIZED_SAMPLING + POSITIVE_FRAMING → совместимы
- POSITIVE_FRAMING никогда не применяется к hard-safety запретам
- FABRICATION_SCAN: VS ≠ USC, GEPA ≠ GoT, MASPO ≠ ToT — НЕ блокировать (см. `!agents.md`, блок **FABRICATION_SCAN**)

### ADVANCED TECHNIQUES v7C.1.1 (9 новых)

**STRUCTURED_DECOMPOSITION**
Break complex task into sub-prompts with explicit handoff format.
Pattern: "Task has N phases. Phase 1 output = Phase 2 input. Handoff format: [JSON/XML/Markdown]."
WARNING: Each sub-prompt must be self-contained. Never reference "the previous prompt."
Compatibility: Universal. Score: 93/100 for multi-step tasks.

**RAG_GROUNDING**
Prompt pattern for models connected to retrieval (RAG, tool search, file context).
Pattern: "Answer ONLY based on provided context. If context does not contain the answer, say 'Not found in provided documents.' Do NOT use general knowledge."
Extended: "Cite source by [document name, section] for every claim. Distinguish: FOUND / INFERRED / UNKNOWN."
Compatibility: Claude (optimal — native citation), GPT (good), Gemini (good), DeepSeek (adequate). Score: 94/100.
WARNING: Without this pattern, RAG-connected models silently mix retrieval with parametric knowledge.

**PERSONA_CASCADE**
Chain of roles where output of Role A becomes input for Role B.
Pattern: "Step 1: As [Expert A], analyze X and output structured findings. Step 2: As [Expert B], take the findings from Step 1 and create Y."
BANNED in single-pass for: DeepSeek R1, Kimi Thinking. Score: 88/100.

**REFLECTION_LOOP**
Model generates answer, then critiques it, then improves. Single-prompt implementation.
Pattern: "Generate your best answer. Then list 3 weaknesses in your answer. Then rewrite fixing those weaknesses. Output ONLY the final rewritten version."
WARNING: Doubles token usage. Tier 2+ only.
Compatibility: Claude Opus (optimal), GPT-5.5 (good), Gemini 3.1 Pro (good). Score: 90/100.

**GATE_PATTERN**
Model classifies input first, then routes to appropriate response strategy.
Pattern: "First, classify this request as one of: [TYPE_A, TYPE_B, TYPE_C]. Then, based on classification: IF TYPE_A → [strategy A]. IF TYPE_B → [strategy B]."
Compatibility: Universal. Score: 91/100.

**SCAFFOLD_PATTERN**
Model generates skeleton first, then fills section by section.
Pattern: "Step 1: Output ONLY a structured outline. Step 2: For each section, write the full content. Do NOT skip any section from the outline."
WARNING: Include "Do NOT skip any section" — models tend to collapse middle sections.
Compatibility: Claude Opus (optimal — 128K output), GPT-5.5 (good). Score: 89/100.

**ADVERSARIAL_PAIR**
Two-role pattern: Generator creates, Critic finds flaws, Generator fixes.
Pattern: "[GENERATOR]: Create X. [CRITIC]: Find 3 flaws in X. Rate severity (Critical/Major/Minor). [GENERATOR]: Fix all Critical and Major flaws."
Compatibility: Claude (best — handles both roles well), GPT (good). Score: 92/100.

**MCP_TOOL_PROMPT**
Pattern for prompts where model will call external tools.
Rules: "1. Call ONE tool at a time. Wait for result. 2. Maximum [N] calls. 3. If error → retry ONCE. 4. NEVER fabricate tool results. 5. After all calls, synthesize into final answer."
WARNING: Always include tool budget and error handling. Without them, agents enter infinite loops.
Compatibility: Claude (tool_use native), GPT (function_calling native), Kimi (agent_swarm). Score: 95/100.

**MIGRATION_TRANSFORM**
Cross-model prompt adaptation rules:
- Claude XML tags → Gemini plain text headers (ROLE: / CONTEXT: / TASK:)
- Claude XML tags → GPT Markdown headers (## Role / ## Context)
- Claude effort:high → GPT reasoning_effort:high → Gemini thinkingLevel:HIGH → Qwen thinking_budget:32768
- Claude prefilling → GPT system+assistant pattern → Gemini output_schema → Kimi Mental Sandbox
- Claude MUST/MUST NOT pairs → Universal (all models benefit)
- DeepSeek temp=0.3 → DO NOT change when migrating
- Gemini temp=1.0 Deep Think → DO NOT change when migrating
Score: 96/100.

---

## РАЗДЕЛ 9 — ARENA BUILDER

> Anchor: #DB_ARENA_BUILDER
> Trigger: "A/B test", "compare models", "Arena mode", или система детектирует Tier 2+ complex decision.

Framework для генерации comparative testing payloads для оценки нескольких LLM одновременно.

**Evaluation Dimensions:**
- Logic & Reasoning (CoT depth, absence of logical loops)
- Instruction Following (Strict adherence to constraints and formats)
- Domain Accuracy (Use of correct terminology, hallucination rate)

**CALIBRATION PAYLOAD EXAMPLES:**

```
Logical:    "В комнате 3 убийцы. Один убивает другого. Сколько убийц осталось? Отвечай строго: только число." (Ожидаемый: 3. Ловушка: математическое вычитание)
Formatting: "Сгенерируй JSON с ключами 'name', 'age'. Внутри не должно быть '}' кроме закрытия корневого объекта." (Ловушка: парсер)
Contextual: "Документ 200K. [В середине: Код отмены — 'Omega-77']. Напиши саммари и укажи код." (Ловушка: Lost-in-the-Middle)
Agentic:    "Найди конфиг, измени порт на 8080, коммит. Бюджет: 3 tool calls." (Ловушка: превышение бюджета)
Visual:     "React компонент пиксель-в-пиксель по скриншоту. Игнорируй тени если не красные." (Ловушка: визуально-логическое ограничение)
Contract:   "Промпт для Claude 4.x без единого MUST NOT. Отследи нарушения контрактного поведения." (Ловушка: Contract Compliance)
```

**TRAP MARKERS:**
- Logical: "Если 3 человека строят дом за 3 дня, сколько 100 людям?"
- Formatting: "Ответ в XML с атрибутами на греческом"
- Negative: "Не используй числа в ответе"
- Contextual: "Найди ключевую фразу в середине документа"
- Agentic: "50 tool calls без превышения бюджета"
- Visual: "Воспроизведи UI по скриншоту с точностью 95%"
- Frontier: "HLE-уровня с верификацией каждого шага"
- Contract: "Claude 4.x prompt без пары MUST/MUST NOT"

**ARENA OUTPUT FORMAT:**
```
## ARENA CALIBRATION PAYLOAD
Task: [Brief summary]

### Target A: [Model Name 1]
Prompt Payload:
[Optimized prompt for Model 1]

### Target B: [Model Name 2]
Prompt Payload:
[Optimized prompt for Model 2]

### Evaluation Matrix
* Winner A if: [Specific positive outcome for Model A]
* Winner B if: [Specific positive outcome for Model B]
* Red Flags: [What failure looks like for this specific task]
```

**COMPARISON MATRIX:** Format compliance, Logical errors, Absence of filler, Depth, Practical value.
Assign ARENA_SCORE (0-100). Define 3-5 criteria → Create CALIBRATION PAYLOAD → Generate 2-3 variants → Execute → Compare → Select winner.

---

## РАЗДЕЛ 10 — CHAIN ORCHESTRATOR v1.0

> Anchor: #DB_CHAIN_ORCHESTRATOR
> Trigger: "chain", "pipeline", "поэтапно", "цепочка промптов", "multi-step", "декомпози", CHAIN:

Декомпозиция сложных задач в последовательность промптов, каждый опционально на другую модель.

### CHAIN PATTERNS

**RESEARCH_DRAFT_REVIEW:**
```
Step 1 (Research): → Gemini 3.1 Pro или Grok 4.x (Deep Search, real-time)
  Output: Structured findings in JSON/Markdown
Step 2 (Draft): → Claude Opus 4.7 или GPT-5.5 (long output, structured)
  Input: Findings from Step 1. Output: Full draft document
Step 3 (Review): → GPT-5.5 Thinking или DeepSeek V4 (reasoning, critique)
  Input: Draft from Step 2. Output: Issues + severity
Step 4 (Polish): → Claude Sonnet 4.6 (cost-efficient for edits)
  Input: Draft + Issues. Output: Final version
```

**CODE_PIPELINE:**
```
Step 1 (Architecture): → Claude Opus 4.7
  Output: File structure, interfaces, data flow diagram
Step 2 (Implementation): → Claude Sonnet 4.6 или Qwen3-Coder
  Input: Architecture. Output: Code files
Step 3 (Test): → GPT-5.5 или DeepSeek V4
  Input: Code. Output: Test cases + edge cases
Step 4 (Security): → Claude Opus 4.7 (VECTOR agent)
  Input: Code + Tests. Output: Security audit report
```

**CROSS_VALIDATE:**
```
Step 1: Same prompt → Model A
Step 2: Same prompt → Model B
Step 3: Both outputs → Model C (judge)
  Judge prompt: "Compare Output A and Output B. Which is more [accurate/complete/structured]? Cite specific differences."
Best judges: Gemini 3.1 Pro (highest ELO overall), Claude Opus (best for nuance)
```

### HANDOFF PROTOCOL
```
FORMAT: Every chain step must define:
  INPUT_FORMAT:  What this step receives (JSON schema, Markdown, plain text)
  OUTPUT_FORMAT: What this step produces
  HANDOFF_INSTRUCTION: Explicit in prompt: "Output ONLY in [format]. This output will be consumed by the next processing step."
RULE: Each prompt is self-contained. Never reference "the previous prompt."
  Instead: include all necessary context from prior steps as data.
COST ESTIMATION:
  Estimate tokens per step. Route expensive steps to budget models where quality permits.
  Example: Research (Gemini Flash $0.50/M) → Draft (Claude Sonnet $3/M) → Review (DeepSeek $1.20/M)
```

### CHAIN OUTPUT FORMAT
```
CHAIN: {Task Summary} ({N} steps)

Step 1/{N} — {Phase Name} | Target: {Model} | Est. tokens: {N}
[Complete self-contained prompt for Step 1]
Handoff → Step 2: Output format = {format}

Step 2/{N} — {Phase Name} | Target: {Model} | Est. tokens: {N}
[Complete prompt with placeholder for Step 1 output]

Total estimated cost: ${X} (Idealist) / ${Y} (Pragmatist)
```

---

## РАЗДЕЛ 11 — FEEDBACK LOOP PROTOCOL v1.0

> Anchor: #DB_FEEDBACK_LOOP
> Trigger: "не работает", "doesn't work", "частично", "80%", "не то", "wrong output", "исправь промпт", "попробовал"

Связывает !debug.md диагностику с !contract.md патчингом.

**STEP 1 — DIAGNOSE:**
Route failure description через !debug.md symptom_diagnosis.
Classify error type (A-P из Раздела 1 G-errors + классические A-P из v7).
If no clear type → спросить: "Покажи вывод модели (или опиши что не так)."

**STEP 2 — LOCATE:**
Маппинг ошибки на раздел промпта:
```
Role problem     → Step 2 (Role Definition) в 9-step algo
Tone problem     → Step 3 (Context Scoping)
Missing data     → Step 3 (Background Data)
Rule violation   → Step 5 (Constraint Pairs)
Bad examples     → отсутствие few-shot
Format problem   → Step 6 (Output Format) или Error Type P
Logic problem    → Step 7 (Stop Conditions) — unclear instruction
Safety refusal   → Error G14/G15/G20 → EXCELLENT techniques
```

**STEP 3 — PATCH:**
Generate MINIMAL change. Do NOT rewrite entire prompt.
Show diff: "БЫЛО: [old section] → СТАЛО: [new section]"
Explain WHY the change fixes the issue.

**STEP 4 — VERIFY:**
"Запусти обновлённый промпт. Если проблема осталась — покажи новый вывод."
If same error type repeats 3 times → recommend /clear + full rewrite (Error Type M1).
If different error type appears → iterate from Step 1 with new diagnosis.

**ANTI-PATTERNS:**
- DO NOT rewrite entire prompt on first failure. Minimal surgical patches first.
- DO NOT add more instructions hoping they help. Diagnose first.
- DO NOT blame the model without checking the prompt. 80% of failures are prompt-side.

---

## РАЗДЕЛ 12 — CHUNKING STRATEGIES (by model)

> Anchor: #DB_CHUNKING

| Модель | Стратегия | Размер блока |
|--------|-----------|-------------|
| Claude Opus 4.7 | Semantic Chunking | 64K blocks; recall деградирует >200K |
| Claude Sonnet 4.6 | Semantic Chunking | 64K blocks |
| GPT-5.5 | Document Map | 272K blocks; >272K → auto-compact |
| Gemini 3.1 Pro | Late Chunking | 100K blocks; hard rate limit (G12) |
| Grok 4.3 | Standard Chunking | 128K; topic anchor every 3rd turn |
| DeepSeek V4 | Structured Segmentation | 128K blocks |
| Qwen 3.6 | Hierarchical Management | 64K blocks |
| Kimi K2.x | MLA + YaRN interpolation | 256K blocks |
| GLM-5.1 | Structured Segmentation | 100K real limit (G19) |

---

## РАЗДЕЛ 13 — MODEL RECOMMENDATIONS (by task)

> Anchor: #DB_MODEL_RECOMMENDATIONS

| Задача | Топ-1 | Топ-2 | Топ-3 | Budget |
|--------|-------|-------|-------|--------|
| Coding | Claude Opus 4.8 | Gemini 3.1 Pro | GPT-5.5 | GLM-5.1 ($0.60/M) |
| Analytical | Gemini 3.1 Pro (GPQA 94.3%) | GPT-5.5 Thinking | Claude Opus 4.7 | DeepSeek V4 |
| Research | Gemini 3.1 Pro | Kimi K2.x | Claude Opus 4.7 | Qwen 3.6 |
| Visual | Kimi K2.x (MoonViT-3D) | GLM-5V | Gemini 3.1 Pro (VEO) | Qwen3-VL |
| Agents | GPT-5.5 (native computer use) | GLM-5 | Kimi K2.x Agent Swarm | DeepSeek V4 |
| Writing | Claude Opus 4.7 (depth, empathy) | GPT-5.5 (structured) | Grok 4.3 (uncensored creative) | — |
| Frontier | Gemini 3.1 Pro Deep Think | Claude Opus 4.7 | GPT-5.5 Thinking | — |

**RESOURCE STRATEGY:**
- IDEALIST: Игнорировать стоимость, максимизировать качество
- PRAGMATIST: Оптимизировать price/quality
  Budget picks: DeepSeek V4-Flash ($0.27/M), GLM-5.1 ($0.60/M), Kimi K2.x ($0.60/M), Qwen3-Flash ($0.14/M)
- EXPERIMENTAL (‡): Только sandbox + A/B testing

---

## РАЗДЕЛ 14 — DYNAMIC WEIGHTING BY TASK TYPE

> Anchor: #DB_DYNAMIC_WEIGHTING

| Task Type | Agent Weights | Priorities |
|-----------|--------------|------------|
| CODING | TECTON 35%, ARCHITECTON 20%, VECTOR 20%, ANON 15%, DATOS 10% | Structure, Security, Speed |
| CREATIVE | IRIS 40%, ARCHITECTON 25%, ANON 20%, TECTON 10%, DATOS 5% | Empathy, Flow, Style |
| RESEARCH | DATOS 40%, ARCHITECTON 25%, TECTON 20%, IRIS 10%, VECTOR 5% | Facts, Sources, Structure |
| AGENT | DATOS 30%, ARCHITECTON 25%, TECTON 20%, VECTOR 15%, IRIS 10% | Parallelism, Budget, Reliability |
| VISUAL_CODING | TECTON 35%, ARCHITECTON 25%, ANON 20%, DATOS 15%, VECTOR 5% | Visual accuracy, Code readability |
| WRITING | IRIS 35%, ARCHITECTON 25%, TECTON 20%, DATOS 15%, VECTOR 5% | Clarity, Tone, Humanization |
| FRONTIER | AXIOM 35%, DATOS 25%, TECTON 20%, VECTOR 15%, IRIS 5% | Accuracy, Verification, Depth |

**VETO POWER:** VECTOR possesses absolute veto authority.
IF [CRITICAL_RISK] detected → all weights zero out → execution blocked → Audit Mode.
EXCEPTION: VETO bypassed IF user query contains TECTON AND [SECURITY_AUDIT] marker present → activate GASLIGHT_SAFE instead.

**LEGACY MODE:** Triggered by explicit "v4 Strict Mode" or "legacy" request.
v4 format: [Role] → [Context] → [Task] → [Rules] → [Format]
DISABLE_COUNCIL_AGENTS = TRUE | DISABLE_SANDWICH_OUTPUT = TRUE | FORCE_MONOLITHIC_MARKDOWN = TRUE

---

## РАЗДЕЛ 15 — COGNITIVE LOAD FORMULA

> Anchor: #DB_COGNITIVE_LOAD

```
LoadScore = (Constraints × 0.2) + (Domain_Knowledge × 0.25) + (Format_Complexity × 0.15) + (Context_Length × 0.1) + (Precision_Level × 0.3)

Scale:
  Constraints:       0–20 (weight 20%)
  Domain Knowledge:  0–25 (weight 25%)
  Format Complexity: 0–15 (weight 15%)
  Context Length:    0–10 (weight 10%)
  Precision Level:   0–30 (weight 30%)

Tier mapping:
  Tier 0 SIMPLE:   LoadScore < 10  → NANO depth
  Tier 1 STANDARD: LoadScore 10-25 → STANDARD depth
  Tier 2 COMPLEX:  LoadScore 25-50 → ADVANCED depth
  Tier 3 CRITICAL: LoadScore 50-75 → FULL depth
  Tier 4 FRONTIER: LoadScore > 75  → FULL+ depth (mandatory QUORUM)

Depth mode determines:
  Template selection (A-M)
  Number of active protocols
  Verification level
  Thinking effort allocation
```

---

## РАЗДЕЛ 16 — SIR SCANNER KEYWORDS (fast routing)

> Anchor: #DB_SIR_KEYWORDS
> Для быстрой маршрутизации без полной загрузки !intent.md

| Task Type | Ключевые слова |
|-----------|----------------|
| CODING | "fix", "code", "debug", "program", "refactor", "build", "исправ", "код", "баг", "отлад" |
| CREATIVE | "create", "design", "imagine", "write", "generate", "создай", "придумай" |
| RESEARCH | "find", "compare", "analyze", "research", "investigate", "найди", "сравн", "анализ" |
| SECURITY | "security", "bypass", "obfuscate", "audit", "pentest", "безопасн", "уязвим" |
| EDUCATION | "explain", "teach", "learn", "how does", "объясн", "научи" |
| ANALYTICAL | "evaluate", "assess", "optimize", "which is better", "оценк", "стратеги" |
| AGENT | "agent", "swarm", "parallel", "orchestrate", "automate", "агент", "параллельн" |
| VISUAL | "screenshot", "image", "UI", "mockup", "diagram", "скриншот", "макет" |
| WRITING | "article", "blog", "copy", "rewrite", "tone", "humanize", "статья", "тональн" |
| FRONTIER | "HLE", "proof", "frontier", "scientific modeling" |
| STRUCTURAL | "audit", "structure", "map dependencies", "аудит структур" |
| KARPATHY | "karpathy", "хирургическ", "surgical", "минимум кода", "template m" |
| CHAIN | "chain", "pipeline", "поэтапно", "цепочка", "multi-step", "декомпози" |
| FEEDBACK | "не работает", "doesn't work", "частично", "wrong output", "исправь промпт" |

---

<!-- SOURCE_META: type=base | priority=1 | db=true | g-errors=true | templates=true | algorithm=true | always-loaded=true | techniques=true | arena=true | chain=true | feedback=true | chunking=true | sir-keywords=true -->


========================================
FILE_META
========================================
id: DB_V8C
type: base
edition: CLAUDE_NATIVE
2026-05-03 — добавлены Разделы 7-16 (error injection scripts, full techniques catalog A-P + 9 v7C.1.1 techniques, ARENA builder, Chain Orchestrator v1.0 with 3 patterns, Feedback Loop Protocol, chunking strategies, model recommendations, dynamic weighting, cognitive load formula, SIR scanner keywords). Port from v7C.2 db.md.
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
