---
source_id: EXPLORATION_V8C
version: v8C.3-ALPHA
module_type: on-demand
depends_on: core.md
last_updated: 2026-06-12
scope: Exploration Mode (Cortex Patch A built-in) — divergent thinking, hypothesis generation, experimental approaches. Safe for brainstorming, not for production decisions without verification.
tags: exploration, cortex-patch-a, brainstorm, hypotheses, divergent-thinking, on-demand
triggers: "исследуй", "exploration", "EXPLORATION MODE", "brainstorm", "гипотезы", "[22]", "/p2p-explore"
---

# P2P v8C.3-ALPHA — EXPLORATION MODE (exploration_mode.md)

> Cortex Patch A встроен в v8C.3. Активируется командой [22] или `/p2p-explore`.

---

## ЧТО ТАКОЕ EXPLORATION MODE

Стандартный режим P2P оптимизирован для **выполнения** — чёткие инструкции, предсказуемый вывод.

Exploration Mode оптимизирован для **открытий** — генерация гипотез, нестандартные углы, дивергентное мышление.

**Когда использовать:**
- Застрял на проблеме, стандартные подходы не работают
- Нужны нестандартные решения
- Brainstorm фаза перед реализацией
- Исследование незнакомой области
- "А что если...?" вопросы

**Когда НЕ использовать:**
- Production-критические решения (без последующей верификации)
- Когда задача уже чётко определена
- Когда нужна скорость, а не глубина

---

## ПРАВИЛА EXPLORATION MODE

```xml
<exploration_rules>
MUST:
- Помечать каждую гипотезу: [EXP: ...]
- После каждой гипотезы → краткое обоснование (1-2 предложения)
- В конце → ранжировать гипотезы по вероятности успеха
- Помечать нестандартные предположения: [UNCONVENTIONAL]
- Явно отмечать противоречия между гипотезами

MUST NOT:
- Представлять гипотезы как факты
- Отфильтровывать "странные" идеи (дивергентная фаза)
- Смешивать Exploration и Standard режим без явного перехода
- Использовать для необратимых действий без верификации
</exploration_rules>
```

---

## ФОРМАТ ВЫВОДА EXPLORATION MODE

```
═══ EXPLORATION MODE ACTIVE ═══

Исследую: [ТЕМА/ПРОБЛЕМА]

[EXP: Гипотеза 1]
→ Обоснование: [почему это может работать]
→ Риск: [где может провалиться]

[EXP: Гипотеза 2] [UNCONVENTIONAL]
→ Обоснование: [почему нестандартная идея имеет смысл]
→ Риск: [что нужно проверить]

[EXP: Гипотеза 3]
...

═══ РАНЖИРОВАНИЕ ═══
1. Гипотеза N — вероятность успеха: HIGH | Причина: [...]
2. Гипотеза M — вероятность успеха: MEDIUM | Причина: [...]
3. Гипотеза K — вероятность успеха: LOW (но стоит рассмотреть) | Причина: [...]

═══ СЛЕДУЮЩИЙ ШАГ ═══
Рекомендую верифицировать: [Гипотезу N]
Метод верификации: [как проверить быстро]

[Введи EXIT EXPLORATION или /p2p-scope чтобы перейти к реализации]
```

---

## CORTEX PATCH A — ВСТРОЕННОЕ РАСШИРЕНИЕ

В v8C.3 Cortex Patch A встроен в ядро (в отличие от v7C.2 где был отдельным модулем).

Это означает:
- Exploration Mode всегда доступен без дополнительной загрузки
- Переключение между Standard и Exploration занимает одну команду
- ATLAS и METRICS отслеживают exploration runs отдельно

**Флаг в p2p.config.md:**
```yaml
flags:
  CORTEX_BUILTIN: true   # Exploration Mode встроен (v8C.3 default)
```

---

## ПРИМЕРЫ ЗАПРОСОВ

```
/p2p-explore как решить проблему N+1 запросов в GraphQL?

/p2p-explore почему наши пользователи уходят после онбординга?

[22] → P2P покажет меню Exploration Mode

вызови IRIS в Exploration Mode для [задача]
```

---

## ВЫХОД ИЗ EXPLORATION MODE

```
Команды для выхода:
  EXIT EXPLORATION  → Стандартный режим
  /p2p-scope       → Переход к SCOPE.HELM (реализация)
  /p2p-quorum      → Запустить QUORUM для верификации гипотез
```

---

## ДЕТАЛЬНЫЕ ТРИГГЕРЫ (port from v7C.2 exploration_mode.md)

> Anchor: #EXPLORATION_TRIGGERS

Активируется при любом из:
- **T1.** SIR Scanner вернул confidence < 0.55 (default fallback при неясной маршрутизации)
- **T2.** Задача не маппится ни на один task_type из db.md (см. #DB_DYNAMIC_WEIGHTING)
- **T3.** Пользователь явно: "explore", "исследуй", "не уверен как подойти", "/p2p-explore"
- **T4.** QUORUM: разброс весов агентов > 30% (нет доминирующего лидера)
- **T5.** Меню п.22 выбран явно

---

## АЛГОРИТМ ПОВЕДЕНИЯ (4 шага)

> Anchor: #EXPLORATION_BEHAVIOR

**STEP 1 — Не выбирать один маршрут.**
Сгенерировать 2-3 варианта подхода:
- Для каждого варианта: агент-лидер, шаблон, оценка Tier, краткая суть.
- Используй AXIOM для оценки каждого варианта.

**STEP 2 — Спросить пользователя:**
- В Code/Cowork: структурированные options (AskUserQuestion)
- В Projects/Chat: статичный markdown список

```
EXPLORATION MODE
Задача не вписывается в стандартные маршруты. Вот как к ней можно подойти:

Подход A — [название]
Агент: [TECTON|IRIS|...] | Шаблон: [из templates_library.md] | Сложность: [Tier 0-4]
Суть: [1-2 предложения]

Подход B — [название]
Агент: [...] | Шаблон: [...] | Сложность: [Tier]
Суть: [...]

Подход C — [опционально, если есть третий явный вариант]
...

Какой подход выбираешь? Или опиши точнее — перемаршрутизирую.
```

**STEP 3 — После выбора:**
- Зафиксировать выбор как routing decision (для session_metrics.md)
- Выполнить через выбранный маршрут
- В конце спросить: "Этот подход сработал? [да/нет/частично]"

**STEP 4 — Если "нет" / "частично":**
- Активировать Feedback Loop (db.md Раздел 11)
- Зафиксировать в session_metrics.md: corrections_requested++

---

## ENV-AWARE ВЗАИМОДЕЙСТВИЕ

```
IF env == "code" OR env == "cowork":
  → AskUserQuestion tool для выбора подхода (нативный UI)
  → Не выводить markdown-список, использовать структурированные options

IF env == "projects" OR env == "chat":
  → Статичный markdown (как §3)
  → Ждать текстового ответа пользователя
```

---

## ANTI-PATTERNS EXPLORATION MODE

- EXPLORATION MODE — это НЕ "я не знаю". Это "есть несколько путей, выбери".
- Никогда не отвечать "не могу" — всегда предлагать варианты.
- Не предлагать >3 подходов — это парализует выбор (Decision Paralysis).
- Не предлагать варианты из одного и того же агента — должны быть разные.
- Не входить в Exploration Mode на простых задачах (Tier 0-1) — это overhead.

---

## ИНТЕГРАЦИЯ

```
ROUTING:   core.md → SIR Scanner → fallback hook при confidence < 0.55
METRICS:   session_metrics.md → exploration_triggers++
FEEDBACK:  db.md Раздел 11 → автозапуск при "нет"/"частично"
AGENTS:    agents.md → AXIOM оценивает варианты
COMMAND:   /p2p-explore
MENU:      item 22 в core.md
```

---

<!-- SOURCE_META: type=on-demand | priority=4 | exploration=true | cortex-patch-a=true | brainstorm=true | triggers=true | behavior=true | env-aware=true -->


========================================
VERSION_METADATA
========================================
id: EXPLORATION_V8C
version: v8C.3-ALPHA
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
