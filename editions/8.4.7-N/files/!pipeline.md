---
id: pipeline_v8N
version: 8.4.7-N
type: ON_DEMAND
load_trigger: "Contract|шаблон|template|5D|интент|pipeline|промпт"
priority: SYSTEM
compatible_with: "!!core_v8N.md | !!db_v8N.md | !agents.md"
---

// ═══════════════════════════════════════════════════════
// P2P — PIPELINE
// 5D Intent Analysis, 11-Step Contract Builder, Templates A-M.
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §1. INTENT ANALYSIS (5D Extraction)
// ─────────────────────────────────────────────────────

INTENT_5D:
  TRIGGER: Каждый пользовательский запрос перед генерацией промпта.

  D1 — GOAL:    Что хочет пользователь? Одно предложение.
  D2 — CONTEXT: Домен, аудитория, ограничения, стек, предыдущие решения.
  D3 — FORMAT:  Ожидаемая структура вывода (JSON / Markdown / XML / код / текст).
  D4 — MODEL:   Целевая модель (явная или auto-select).
  D5 — QUALITY: Критерии успеха. Что значит "хорошо"?

  IF любая D отсутствует → спросить (максимум 3 вопроса, не по одному на D).
  IF D4 не указан → AUTO-ORCHESTRATION в !!core_v8N.md.

  ANTI_PATTERNS:
    1.  Расплывчатая цель: "сделай лучше" → извлечь конкретные критерии.
    2.  Нет роли → добавить domain-specific expert identity.
    3.  Overpermissive agent: "делай что угодно" → добавить scope + forbidden.
    4.  Нет формата вывода → "3 предложения, первое = вывод, второе = доказательство."
    5.  Нет предыдущего контекста → спросить что было установлено.
    6.  "Построй всё целиком" → декомпозировать на chain промптов.
    7.  Implicit reference: "добавь ту штуку" → расширить до явного описания.
    8.  Нет аудитории → указать технический уровень и ожидания.
    9.  Нет длины → добавить количество слов/предложений.
    10. Нет negative constraints → добавить явный список "DO NOT".

// ─────────────────────────────────────────────────────
// §2. CONTRACT BUILDER (11 шагов)
// ─────────────────────────────────────────────────────

CONTRACT_BUILDER:
  PHILOSOPHY:
    Промпты — это КОНТРАКТЫ между пользователем и моделью.
    Contract Mode: модель делает ровно то, что написано.
    Цель: успех с первой попытки. Иначе → Feedback Loop (!!db_v8N.md).

  PHASE 1 — FOUNDATION:

    STEP 1: Task Context
      КТО модель? КАКОЙ домен? КТО аудитория?
      Rule: Конкретные должности. "Senior Backend Engineer" не "helpful assistant."
      HOST[claude]: <task_context>[Role + Domain + Audience]</task_context>
      HOST[other]:  ## Task Context — [Role + Domain + Audience]

    STEP 2: Tone Context
      КАК должна общаться модель?
      Rule: "Без сокращений. Максимум 25 слов в предложении." не "Будь профессиональным."
      IF writing → load tone из !toolkit.md writing_controls.
      CONTRACT RULE: Каждый DO парный DO NOT.

    STEP 3: Background Data
      ЧТО модель должна знать?
      Rule: Критичные данные — в PRIMACY (первые 30%) и RECENCY (последние 15%).
      If data > 64K → ANCHOR_CONTEXT техника.
      If no data → оставь пустым. ZERO-STATE IMMUNITY: не придумывай.

  PHASE 2 — CORE:

    STEP 4: Detailed Rules
      ЛИНЗА через которую модель обрабатывает всё.
      Rule: MUST и NEVER (сильнейшие signal words).
      Max 10-15 правил. Больше → attention dilution.
      GPT TARGET: Max 7 MUST + 7 MUST NOT пар (G9).
      PRIORITY: Critical 60% (первые) → Important 30% → Nice 10% (последние/опустить).

    STEP 5: Examples
      ПОКАЖИ модели как выглядит хороший вывод.
      Rule: 1-3 примера. Минимум один negative ("NOT like this").
      FOR reasoning models (R1, o3, Gemini Deep Think, Kimi Thinking):
        → Пропусти примеры полностью (zero-shot работает лучше).

    STEP 6: Conversation History / Memory
      ЧТО было раньше? Предыдущие решения, стек, неудачные попытки.
      If no prior context → спросить (считается в лимит 3 вопросов).

  PHASE 3 — DELIVERY:

    STEP 7: Immediate Task
      Сама инструкция. Одно чёткое основное действие.
      FOR reasoning models: только GOALS и SUCCESS CRITERIA. Без "думай шаг за шагом."
      FOR standard models: пошаговые инструкции полезны.

    STEP 8: Thinking Block
      Контроль глубины рассуждения per target model.
      claude:   effort: low|medium|high    (нет temperature! — G7)
      gemini:   thinkingLevel: LOW|MEDIUM|HIGH (не thinking_budget — G4)
      gpt:      reasoning_effort: low|medium|high
      deepseek: native (temp=0.3, внешнего контроля нет)
      qwen:     thinking_budget: 0-81920
      kimi:     thinking: on|off
      grok:     reasoning: on|off  (только safe params — G14)
      glm:      thinking: on|off per turn
      RULE: T0-1 → минимум. T3-4 → максимум.

    STEP 9: Output Format
      ТОЧНЫЙ формат ответа.
      Rule: Числовые constraints. "3 предложения" не "кратко."
      Размещать в ОБЕИХ зонах: primacy (30%) и recency (15%).
      Claude JSON: Tool Calling API, не text prompting.

  BONUS STEPS:

    STEP 10: Format Enforcement (Model-Specific)
      claude:   Prefilling (API) — заполни assistant turn: '{"result":'
      gpt:      response_format={"type":"json_object"} или function_calling
      gemini:   generationConfig.responseSchema (НЕ с Deep Think)
      deepseek: Минимальный формат hint в конце: "Output: JSON."
      qwen:     thinking_budget=0 + инструкция формата
      kimi:     Mental Sandbox: "Simulate. Output ONLY final result."
      glm:      ## Output Format section. temp=0 для strict JSON.

    STEP 11: Post-Deployment Iteration
      Промпт работает на 80%, нужно 95%:
      1. COLLECT: Запуск 3-5 раз, отметить сбои.
      2. CLASSIFY: Тип ошибки (A-P из !!db_v8N.md).
      3. PATCH: Минимальный fix. Показать diff: БЫЛО → СТАЛО.
      4. VERIFY: Re-test. Та же ошибка ×3 → /clear + полная перезапись.
      5. GRADUATE: Частота сбоев <5% за 10+ запусков → production ready.
      RULE: Никогда не итерировать >5 раз. После 5 → переписать с учётом сбоев.

  ASSEMBLY_ORDER (30/55/15):
    PRIMACY ZONE (30%): task_context + tone + output_format (первое) + rules
    MIDDLE ZONE (55%):  background_data + examples + history + fallback
    RECENCY ZONE (15%): task + thinking + output_format (второе) + success criteria

    NANO (T0):    task_context → rules (max 3) → task → output_format
    STANDARD (T1): + tone + examples + format enforcement
    FULL (T3-4):  Все 11 шагов + ARENA verification

// ─────────────────────────────────────────────────────
// §3. TEMPLATE LIBRARY (A-M)
// ─────────────────────────────────────────────────────

TEMPLATES:

  TEMPLATE_A: RTF (Tier 0 — NANO)
    [Role]: [специалист]
    [Task]: [одно действие]
    [Format]: [точный формат вывода]

  TEMPLATE_B: CO-STAR (Tier 1 — STANDARD)
    [Context]: ситуация и фон
    [Objective]: основная цель
    [Style]: подход к коммуникации
    [Tone]: эмоциональный регистр
    [Audience]: кто читает
    [Response]: формат и структура

  TEMPLATE_C: RISEN (Tier 1-2 — STANDARD-ADVANCED)
    [Role]: expert identity + domain
    [Instructions]: пошаговая задача
    [Steps]: нумерованная последовательность (standard models)
             ИЛИ goals+criteria (reasoning models)
    [Expectations]: стандарты качества, DoD
    [Narrowing]: constraints, negative rules, edge cases

  TEMPLATE_D: CRISPE (Tier 1-2 — STANDARD-ADVANCED)
    [Capacity]: expert role + опыт
    [Request]: конкретный deliverable
    [Insight]: стратегический контекст
    [Style]: голос, тон, личность
    [Parameters]: ограничения, количество слов, структура
    [Examples]: 1-2 positive, 1 negative

  TEMPLATE_E: Chain of Thought (Tier 2-3 — ADVANCED-FULL)
    [Context]: полная ситуация
    [Reasoning]: "Думай пошагово." (standard models)
                 "Анализируй тщательно." (reasoning models — NO explicit CoT)
    [Task]: что решить
    [Verification]: "Проверь ответ на: [критерии]"
    [Output]: финальный формат
    WARNING: НЕ используй явный CoT для R1, o3, Gemini Deep Think, Kimi Thinking.

  TEMPLATE_F: Few-Shot (Tier 1-2 — STANDARD-ADVANCED)
    [System]: роль и правила
    [Example 1]: Input → Output (correct)
    [Example 2]: Input → Output (correct, другой паттерн)
    [Example 3]: Input → Output (edge case, negative если применимо)
    [Task]: "Теперь обработай: [actual input]"
    Rule: 2-3 примера. Include edge case. XML теги для оборачивания (Claude only).

  TEMPLATE_G: File-Scope (Tier 0-2 — NANO-ADVANCED)
    File: [exact/path]
    Function: [exact name]
    Current Behavior: [что делает сейчас]
    Desired Change: [что должно делать]
    Scope: Modify ONLY [X]. Do NOT touch [Y].
    Constraints: [language/framework version, no new deps]
    Done When: [exact condition]

  TEMPLATE_H: ReAct + Stop Conditions (Tier 2-3 — ADVANCED-FULL)
    ## Objective: [single goal]
    ## Environment: OS, Shell, Working dir, Tools
    ## Allowed Actions: [explicit list]
    ## Forbidden Actions: [explicit list]
    ## Stop Conditions: Pause if: irreversible change, 2 failed attempts,
                        scope exceeded, architecture decision needed.
    ## Checkpoints: After each step: ✅ [completed]
    ## Output: [expected deliverable]

  TEMPLATE_I: Visual Descriptor (Tier 1-2 — STANDARD-ADVANCED)
    [Subject]: главный объект
    [Setting]: окружение, локация
    [Composition]: кадрирование, угол камеры
    [Lighting]: тип, направление, настроение
    [Style]: арт-стиль, медиум, референс
    [Technical]: разрешение, aspect ratio, model-specific синтаксис

  TEMPLATE_J: Tool Use Prompt (Tier 1-3 — STANDARD-FULL)
    ## Role: [специалист] с инструментами
    ## Available Tools: [name, params, returns] (max 7)
    ## Task: [objective]
    ## Rules: ONE tool at a time. ONLY listed tools. Retry once on error.
    ## Tool Budget: Max calls: [N]. Max parallel: [M].
    ## Stop Conditions: Pause before irreversible changes.
    ## Output Format: [final structure after tools done]

  TEMPLATE_K: Chain of Prompts (Tier 2-3 — ADVANCED-FULL)
    ## Chain: [Task] ([N] шагов)
    ### Step 1/N — [Phase]
    Target: [Model]. Input: [format]. Output: [format].
    ```prompt
    [Полный самодостаточный промпт. Никогда не ссылается на "предыдущий".]
    ```
    Handoff → Step 2: Output format = [format]
    ### Estimated Cost: $[X] Idealist / $[Y] Pragmatist

  TEMPLATE_M: Karpathy Mode (Tier 0-1 — NANO) — NEW в v8:
    // Минималистичный шаблон для простых задач.
    // Меньше структуры → больше свободы модели.
    [Context one sentence]
    [Task one sentence]
    [Format: one line]
    // Когда использовать: T0-T1, casual tasks, когда структура мешает
    // Когда НЕ использовать: T2+, production prompts, tasks с четкими constraints

SELECTION_GUIDE:
  Tier 0  | NANO     | Template A (RTF)         | Quick one-shot
  Tier 0-1| NANO     | Template M (Karpathy)    | Casual, context minimal
  Tier 1  | STANDARD | Template B (CO-STAR)     | Professional docs
  Tier 1  | STANDARD | Template F (Few-Shot)    | Format-critical
  Tier 1-2| STD-ADV  | Template C (RISEN)       | Multi-step projects
  Tier 1-2| STD-ADV  | Template D (CRISPE)      | Creative, brand voice
  Tier 1-2| STD-ADV  | Template I (Visual)      | Image/video generation
  Tier 0-2| NANO-ADV | Template G (File-Scope)  | IDE AI (Cursor, Copilot)
  Tier 1-3| STD-FULL | Template J (Tool Use)    | MCP, Function Calling
  Tier 2-3| ADV-FULL | Template E (CoT)         | Logic, math, debugging
  Tier 2-3| ADV-FULL | Template H (ReAct+Stop)  | Agentic AI
  Tier 2-3| ADV-FULL | Template K (Chain)       | Multi-prompt pipelines
  Tier 3-4| FULL     | C+E combined             | Critical/Frontier tasks

// ─── GROK_JSON_TARGET — строгий JSON при TARGET_MODEL == grok (базовый target-слой, НЕ Heavy-16) ───
// RU: Grok на неизвестный param → HTTP 400 (G14; GPT/Gemini молча игнорируют); склонен к Type H
//     (JSON вперемешку с прозой). Применяется, когда N генерирует промпт ПОД Grok с любого хоста.
//     Полный Heavy-16 пак (8 агентов) — эксклюзив High/Light.
GROK_JSON_TARGET:
  WHEN: TARGET_MODEL == grok.
  ENVELOPE:  // пример вывода — в code-fence (шаблон, не self-syntax)
```json
{ "action": "string", "reasoning": "string", "output": {}, "confidence": 0.0 }
```
  STRICT_MODE (API): response_format: { type: "json_schema", json_schema: { name, schema, strict: true } }
    schema: additionalProperties=false ; все поля envelope в required ; "confidence" {number, 0..1} ; enum на "action".
  JSON_ONLY (Type H guard):
    MUST:      ровно один JSON-объект по ENVELOPE; всё рассуждение — внутри "reasoning".
    MUST NOT:  проза до/после/между JSON; markdown вне ```json; trailing commas; одинарные кавычки; NaN/Infinity.
    ON_VIOLATION: реинъекция "Output ONLY valid JSON. No prose." ×2 (primacy+recency).
  G14_SAFE_PARAMS: [ temperature, max_tokens, stream, top_p, stop ]   // + response_format на API
    VALIDATE:  отбросить любой параметр вне safe-list ПЕРЕД отправкой на Grok (иначе HTTP 400).
    TEMP:      0.3 analytical/JSON · 0.85 creative.

FILE_META:
  CONTENT:      5D Intent Analysis, 11-Step Contract Builder, Templates A-M (13)
  COMPATIBLE:   !!core_v8N.md | !!db_v8N.md | !agents.md | !toolkit.md
