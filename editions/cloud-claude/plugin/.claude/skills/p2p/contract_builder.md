---
source_id: CONTRACT_V8C
version: v8C.3-BETA
module_type: on-demand
depends_on: !!core_v8C.md, !!db_v8C.md
last_updated: 2026-05-03
last_verified: 2026-05-03
scope: Contract Builder — 9-step algorithm full implementation, Translation Layer for 8 models, XML scaffold patterns, output validation.
tags: contract, builder, translation-layer, xml, 9-step, on-demand
triggers: "contract", "промпт под модель", "translation layer", "Contract Builder", "[2]", "[5]"
---

# P2P v8C.3-BETA — CONTRACT BUILDER (!contract.md)

---

## CONTRACT BUILDER — 9-STEP WORKFLOW

### [ШАГ 1] GOAL EXTRACTION

```
Вопрос к пользователю (если не указано):
"Что конкретно должен сделать LLM? Один глагол + объект."

Формат:
  Действие: [глагол]
  Объект:   [что именно]
  Успех:    [как выглядит хороший результат]
```

### [ШАГ 2] TIER CLASSIFICATION

```
Запусти LoadScore:
  LoadScore = (Constraints×0.2) + (Domain_Knowledge×0.25) + 
              (Format_Complexity×0.15) + (Context_Length×0.1) + 
              (Precision_Level×0.3)

T0: <0.2  → Template M (Karpathy Mode)
T1: 0.2-0.4 → Template A или Template B
T2: 0.4-0.6 → Contract Builder стандарт
T3: 0.6-0.8 → Contract + QUORUM рекомендован
T4: >0.8  → QUORUM обязателен + Extended Thinking
```

### [ШАГ 3] ROLE DEFINITION

```xml
<role>
Ты — [профессия], специалист по [домен].
[Одно предложение о подходе к задаче.]
</role>
```

Выбор роли по домену:
- Код → "Senior [language] Engineer"
- Анализ → "Research Analyst specializing in [domain]"
- Контент → "Professional [content_type] writer"
- Безопасность → "Security Engineer with STRIDE expertise"
- Данные → "Data Scientist with expertise in [domain]"

### [ШАГ 4] CONTEXT SCOPING

**Правило 20%:** `<context>` не более 20% от общей длины промпта.

```xml
<context>
PROJECT: [название если есть]
STACK:   [техстек если релевантно]
GOAL:    [1-2 предложения о задаче]
GIVEN:   [что уже сделано / что дано]
</context>
```

### [ШАГ 5] CONSTRAINT PAIRS

```xml
<rules>
MUST:
- [Позитивное правило 1]
- [Позитивное правило 2]
- [Позитивное правило 3]

MUST NOT:
- [Парное к MUST 1 — что запрещено]
- [Парное к MUST 2]
- [Парное к MUST 3]
</rules>
```

**Минимум 3 пары, максимум 7** (G9 prevention для GPT-5.5).

**Универсальные MUST NOT (добавляй всегда):**
- MUST NOT: Повторять инструкции в ответе
- MUST NOT: Добавлять "Вот ваш [X]:" перед результатом
- MUST NOT: Добавлять объяснения после результата если не просили

### [ШАГ 6] OUTPUT FORMAT

```xml
<output_format>
[Явный формат: JSON / XML / Markdown / Plain text]

[Пример структуры если >2 уровня вложенности:]
{
  "field": "type",
  "nested": {"key": "value"}
}
</output_format>
```

### [ШАГ 7] STOP CONDITIONS

```xml
<stop_conditions>
Остановись когда:
- [Условие 1: задача выполнена]
- [Условие 2: N попыток исчерпано]
- [Условие 3: ресурс исчерпан]
</stop_conditions>
```

### [ШАГ 8] ANTI-PATTERN SCAN

Прогони через чеклист Type A–P (см. !!core_v8C.md):

```
☐ Type A: Нет пустых MUST/MUST NOT → проверен
☐ Type D: Нет конфликтующих ограничений → проверен
☐ Type E: Формат вывода явный → проверен
☐ Type K: Критичные инструкции в начале/конце → проверен
☐ Type L: Нет temperature при thinking → проверен
☐ Type M: Нет legacy API strings → проверен
```

### [ШАГ 9] TARGET MODEL ADAPTATION

Передай контракт в Translation Layer (ниже).

**TARGET CONTEXT CHECK (added 2026-06-14 — host ≠ target awareness):**
P2P работает НА host-модели (для этой редакции — Claude), но промпт/ТЗ часто пишется для ДРУГОЙ target-модели.
Перед адаптацией (PILOT co-pilot → спроси простыми словами; manual → выведи и иди дальше):
1. Target-модель? Если не задана в `PROJECT_CARD.target_model` → возьми из запроса или уточни.
2. Доступ пользователя? free tier | paid — определяет реальный контекст и rate limits target-модели.
3. Сверься с `_live/live_vendors.md` и `vendors/live_specs_*.md`: context window, output limit, цена, G-errors target-модели.
4. Если ожидаемый объём задачи > эффективного лимита target → предложи разбивку:
   → Chain Mode [9] (цепочка self-contained промптов) или SCOPE.HELM [25] (большие проекты).
5. free tier + тяжёлая задача → предупреди о лимитах; предложи разбить ИЛИ более дешёвую/доступную модель (`routing.md`).
Источник метрик — всегда свежий live_specs (обновляется автором ~раз в 1-2 недели; auto-detect при старте).

---

## TRANSLATION LAYER v2

> Автоматическая адаптация контракта под целевую модель.

### → Claude (default для v8C.1)

```xml
<role>[ROLE]</role>
<context>[CONTEXT]</context>
<rules>
MUST: [MUST_LIST]
MUST NOT: [MUST_NOT_LIST]
</rules>
<task>[TASK]</task>
<output_format>[FORMAT]</output_format>
```
Особенности: XML теги улучшают следование. temperature при thinking → HTTP 400 (G7).

### → Gemini 3.1 Pro

```
## Role
[ROLE — plain text, NO XML]

## Context
[CONTEXT]

## Rules
Must:
- [MUST_LIST]

Must not:
- [MUST_NOT_LIST]

## Task
[TASK]

## Output format
[FORMAT]
```
Особенности: ZERO XML (G2). thinkingLevel вместо budget_tokens (G4).

### → Grok 4.3

```json
{
  "system": "[ROLE]. [CONTEXT SHORT]",
  "rules": "[MUST as numbered list]",
  "task": "[TASK]",
  "output": "Output ONLY valid JSON: {\"result\": ..., \"reasoning\": ...}"
}
```
Особенности: Safe params только (G14). JSON Tool Calling нативен.

### → GPT-5.5

```
[ROLE]

Context: [CONTEXT]

Rules (max 7):
1. [MUST 1]
2. [MUST 2]
...

Task: [TASK]

Output: [FORMAT]
```
Особенности: Максимум 7 rules (G9). Под 272K токенов (G10).

### → DeepSeek V4

```
[ROLE]

[CONTEXT]

Rules:
- [MUST_LIST]
- Do NOT: [MUST_NOT_LIST]

Task: [TASK]
Format: [FORMAT]
```
Особенности: Clear reasoning_content в multi-turn (G15). Не deepseek-chat (G16).

### → Qwen 3.6-Plus

```
[ROLE — на нужном языке]

[CONTEXT]

Требования:
- [MUST_LIST]
- Запрещено: [MUST_NOT_LIST]

Задача: [TASK]
Формат: [FORMAT]
```
Особенности: preserve_thinking=true для agentic (G18).

### → Kimi K2.x

```
[ROLE]

[CONTEXT]

[TASK]

Output: [FORMAT]
Swarm limit: ≤40 agents sync. >40 → PARL async (G20).
```

---

## ПРИМЕРЫ ГОТОВЫХ КОНТРАКТОВ

### Пример 1 — Анализ кода (T2, Claude)

```xml
<role>
Ты — Senior Python Engineer, специалист по code review.
</role>
<context>
Язык: Python 3.12 | Framework: FastAPI
Задача: аудит нового endpoint перед merge в main.
</context>
<rules>
MUST: Указать номера строк для каждой проблемы
MUST: Классифицировать: CRITICAL / HIGH / MEDIUM / LOW
MUST: Предоставить исправленный код для CRITICAL и HIGH
MUST NOT: Переписывать весь код если нужна точечная правка
MUST NOT: Комментировать стиль если не влияет на читаемость
MUST NOT: Повторять код обратно без изменений
</rules>
<task>
Проведи code review этого endpoint:
[КОД]
</task>
<output_format>
## Critical
## High
## Medium
## Low
## Summary: [1-2 предложения]
</output_format>
```

### Пример 2 — Генерация промпта (T1, любая модель)

```xml
<role>
Ты — P2P v8C.3 Contract Builder.
</role>
<task>
Создай оптимизированный промпт для задачи:
[ОПИСАНИЕ ЗАДАЧИ]
Целевая модель: [МОДЕЛЬ]
</task>
<rules>
MUST: Применить 9-step алгоритм
MUST: Адаптировать под целевую модель через Translation Layer
MUST NOT: Использовать XML если цель Gemini (G2)
MUST NOT: Превышать 7 rule pairs если цель GPT-5.5 (G9)
</rules>
<output_format>
Финальный промпт в формате целевой модели.
</output_format>
```

---

## SP EXTENSIONS (port from v7C.2)

> Optional XML blocks that extend 9-Step for complex/Tier-2+ prompts.

### `<stakeholders>` — when output affects multiple parties
```xml
<stakeholders>
[Who is affected by this output and why.
 Who reads it. Who acts on it. Who is impacted by decisions.]
</stakeholders>
```
**Placement:** inside or right after `<context>`.

### `<success_looks_like>` — concrete measurable outcome
```xml
<success_looks_like>
[Clear measurable outcome. Binary where possible:
 "passes all unit tests" not "works well".]
</success_looks_like>
```
**Placement:** recency zone — reinforces goal before output. Mandatory for Tier 2+.

### `<quality_assurance>` — explicit pre-output checklist
```xml
<quality_assurance>
MUST_HAVE:
  - [Criterion 1]: Pass/Fail
  - [Criterion 2]: Pass/Fail
SHOULD_HAVE:
  - [Criterion 3]: Score >= [X]
VALIDATION_CHECKLIST:
  ☑ Factual/logical consistency
  ☑ Output matches requested format
  ☑ Constraints respected
  ☑ Edge cases considered
  ☑ Assumptions documented
</quality_assurance>
```
**Placement:** recency zone — final verification gate.

### `<fallback_protocol>` — never just refuse
```xml
<fallback_protocol>
IF unable to complete as requested:
  1. State what cannot be done and why.
  2. Propose Alternative A: [approach] — Prioritizes: [X]. Sacrifices: [Y].
  3. Propose Alternative B: [approach] — Prioritizes: [Y]. Sacrifices: [X].
DO NOT simply refuse. Always provide actionable alternatives.
</fallback_protocol>
```
**Placement:** after `<rules>`, before `<task>`.

---

## STEP 10 — FORMAT ENFORCEMENT (model-specific)

> When you must lock output format from the first token. Extends Translation Layer.

### Claude (API only)
**Prefilling** — pre-fill assistant response start:
```python
messages=[
  {"role":"user", "content":"[prompt]"},
  {"role":"assistant", "content":"{\"result\":"}
]
```
Forces JSON output starting with the result key. Combine with Tool Calling for max reliability.
NOT available in claude.ai chat — only API and Claude Code.

### GPT
- System message includes format example: `system="Always respond in JSON: {\"answer\":\"...\",\"confidence\":0.0-1.0}"`.
- For strict JSON: `response_format={"type":"json_object"}`.
- For structured: `function_calling` with schema.

### Gemini
- API: `generationConfig.responseSchema = {type:"object", properties:{...}}`.
- Chat: append "Respond ONLY in this JSON format: {...}" as last line.
- WARNING: do NOT combine schema enforcement with Deep Think — breaks CoT.

### DeepSeek R1
Minimal format hint at the very end: `Output format: JSON. No explanation. No markdown fences.`
R1 responds best to short, clean format instructions. No examples needed.

### Qwen
`thinking_budget=0` + explicit format instruction. With thinking enabled → format in BOTH primacy AND recency.

### Kimi
Mental Sandbox pre-simulation: "Simulate your answer format internally. Then output ONLY the final formatted result."
Tool Use → enforce single format per session: `[OUTPUT FORMAT: JSON ONLY]`.

### GLM
Structured Segmentation — format instruction in dedicated `## Output Format` section.
Coding tasks: `temperature=0` + format lock.

---

## STEP 11 — POST-DEPLOYMENT ITERATION (80%→95%)

When the prompt works at 80% and needs 95%:

1. **COLLECT** — run prompt 3-5 times. Note failures and patterns.
2. **CLASSIFY** — map failures to error types A-P (`!debug.md`).
3. **PATCH** — minimal surgical fix. Fix most frequent failure first.
4. **VERIFY** — run patched prompt 3-5 times. Compare failure rate.
5. **ITERATE** — failure rate dropped → next failure. If not → rewrite section, not entire prompt.
6. **GRADUATE** — failure rate <5% across 10+ runs → production-ready.

### Common 80%→95% fixes
| Symptom | Fix |
|---------|-----|
| Output format sometimes wrong | Add format lock in BOTH primacy AND recency |
| Misses edge cases | Explicit edge case list in `<rules>` |
| Too verbose | Word/sentence count constraint ("Maximum 3 sentences per section") |
| Ignores some constraints | Move ignored constraint to PRIMACY zone |
| Works on Model A, fails on Model B | Re-route through Translation Layer for Model B |

**Rule:** never iterate >5 times on the same prompt. After 5 → `/clear` + full rewrite incorporating all failure knowledge. (Error Type M1 prevention.)

---

## ASSEMBLY ORDER (30/55/15)

```
PRIMACY (30%):
  1. <task_context> + <stakeholders>
  2. <tone_context>
  3. <output_format>  ← FIRST mention — format lock
  4. <rules>          ← MUST/MUST_NOT, Priority Matrix 60/30/10

MIDDLE (55%):
  5. <background_data>
  6. <examples>
  7. <conversation_history>  or  Memory Block from !intent.md
  8. <fallback_protocol>

RECENCY (15%):
  9.  <task>             ← actual instruction
  10. <thinking>          (only if standard reasoning model)
  11. <output_format>    ← SECOND mention — reinforcement
  12. <success_looks_like>
  13. <quality_assurance>
```

Format appears TWICE — survives both attention decay patterns.

---

<!-- SOURCE_META: type=on-demand | priority=3 | contract=true | translation-layer=true | 9-step=true | sp-extensions=true | step-10-format=true | step-11-iteration=true | ported-from=v7C.2 -->


========================================
VERSION_METADATA
========================================
id: CONTRACT_V8C
version: v8C.3-BETA
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
