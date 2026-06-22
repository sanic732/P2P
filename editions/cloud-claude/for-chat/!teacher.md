---
source_id: TEACHER_V8C
version: v8C.3-BETA
module_type: on-demand
depends_on: !!core_v8C.md, !!db_v8C.md
last_updated: 2026-06-12
scope: Interactive teaching curriculum for P2P v8C.3. 5 levels + Q&A FAQ. Loaded on /p2p-teacher trigger.
tags: teacher, curriculum, onboarding, levels, exercises, faq
---

# !teacher.md — Curriculum P2P v8C.3

> ON-DEMAND модуль. Загружается командой `/p2p-teacher` или скиллом `p2p-teacher`.
> Источник истины для всех учебных сценариев. Не использовать как замену `!!core_v8C.md`.

---

## ОГЛАВЛЕНИЕ

- [LEVEL 1 — Quickstart](#level-1)
- [LEVEL 2 — Commands](#level-2)
- [LEVEL 3 — Agents](#level-3)
- [LEVEL 4 — QUORUM](#level-4)
- [LEVEL 5 — SCOPE.HELM](#level-5)
- [Q&A FAQ](#qa-faq)
- [CHEATSHEET](#cheatsheet)
- [COMPREHENSION CHECKS](#comprehension)
- [META: как teacher mode работает изнутри](#meta)

---

## КАК ИСПОЛЬЗОВАТЬ ЭТОТ ФАЙЛ

Этот файл — **внутренний справочник** для команды `/p2p-teacher`. Пользователь его напрямую обычно не читает. Структура:

- Каждый уровень = независимый блок, можно проходить в любом порядке (но рекомендуется по порядку)
- Каждый блок (БЛОК N) = атомарная учебная единица: теория ≤ 5 строк + 1 пример + 1 упражнение + критерий освоения
- FAQ покрывает 80% типичных вопросов; для остального — fallback в `!!core_v8C.md` + `!!db_v8C.md`

---

<a name="level-1"></a>
# LEVEL 1 — Quickstart (10 минут)

**Цель:** За 10 минут пользователь понимает что такое P2P, зачем оно, как запустить первую команду.

**Pre-check:** "Ты раньше работал с промпт-инжинирингом? (да/нет/немного)" — для адаптации тона.

---

## БЛОК 1.1 — Что такое P2P?

**Теория (5 строк):**
P2P — мета-промпт система для Claude. Помогает создавать качественные промпты под любую задачу: код, текст, дизайн, исследование.
Думай о ней как о Git для промптов: версии, история, тулинг.
Работает на 3 принципах: **модульность** (грузим только нужное), **многоагентность** (8 экспертов голосуют), **XML-native** (формат Claude).

**Пример:**
Без P2P: "Напиши код для авторизации"
С P2P: использует Template L (Production Code), вызывает агента TECTON, добавляет MUST/MUST NOT, проверяет на 16 anti-patterns → результат в 3-5 раз качественнее.

**Упражнение:**
Открой главный файл `!!core_v8C.md` и пролистай меню (34 пункта). Напиши какой пункт привлёк внимание.

**Критерий освоения:** пользователь называет ≥1 пункт меню.

---

## БЛОК 1.2 — Как запустить P2P

**Теория:**
3 способа запуска в зависимости от среды:
- **Claude Code / Cowork:** `/p2p` (slash-команда)
- **Claude Chat / Projects:** скопировать `_master.md` целиком в system prompt
- **API:** загрузить `_preloader.md → !!core_v8C.md → !!db_v8C.md → _live/*`

**Пример:**
```
User: /p2p
P2P: [P2P v8C.3 | Среда: COWORK | Guardian: ON]
     1) QUICK GEN ...
     2) DEEP DIVE ...
     ...
     33) ОБУЧЕНИЕ → /p2p-teacher
```

**Упражнение:**
Запусти `/p2p` (если в Code/Cowork) ИЛИ открой `!!core_v8C.md` и найди где описано меню. Какая среда у тебя сейчас?

**Критерий:** пользователь определил свою среду (Code / Cowork / Chat / API).

---

## БЛОК 1.3 — Первая команда

**Теория:**
Самая частая команда — просто запрос задачи. P2P сам решит какой Template + какие агенты + какой Tier модели.
Можешь форсировать: `задача [TIER=3]` или `задача [AGENT=TECTON]`.

**Пример:**
```
User: Напиши Python функцию проверки email
P2P: [Selected: Template L | Agent: TECTON | Tier: 2 (Sonnet)]
     [Generated prompt with MUST/MUST NOT...]
     [ATLAS: complexity=2, est_tokens=800, est_quality=9/10]
```

**Упражнение:**
Подумай о задаче которая тебе нужна сейчас. Какой Tier ты бы выбрал (1=быстро/дёшево, 4=максимальное качество)?

**Критерий:** пользователь формулирует задачу + выбирает Tier.

---

## БЛОК 1.4 — ATLAS и что он показывает

**Теория:**
ATLAS — карта задачи. После каждой генерации P2P показывает:
- complexity (1-5)
- est_tokens
- est_quality (1-10)
- agents_used
- efficiency (quality/cost)

**Пример:**
```
ATLAS:
  task: email validator
  complexity: 2/5
  est_tokens: 800
  est_quality: 9/10
  agents_used: [TECTON]
  tier: 2 (Sonnet)
  efficiency: 0.92
```

**Упражнение:**
Если ATLAS показал complexity=4 и agents_used=[TECTON], что бы ты сделал? (подсказка: complex задаче нужен QUORUM)

**Критерий:** пользователь говорит "запустить QUORUM" или "/p2p-quorum".

---

## ПРОВЕРКА LEVEL 1

3 вопроса:
1. Что такое P2P в одном предложении?
2. Назови команду для запуска главного меню.
3. Что такое ATLAS?

**Pass:** 3/3 → переход на Level 2. 2/3 → повторение слабого блока. <2/3 → повторение всего Level 1.

---

<a name="level-2"></a>
# LEVEL 2 — Commands (20 минут)

**Цель:** Пользователь знает все 11 команд `/p2p-*` и когда их использовать.

**Pre-check:** "Какие команды P2P ты уже пробовал?"

---

## БЛОК 2.1 — Карта команд

**Теория:**
Все команды в `.claude/commands/`. 11 штук:

| Команда | Когда |
|---------|-------|
| `/p2p` | Главное меню, старт сессии |
| `/p2p-quorum` | Сложная задача (нужно мнение 8 экспертов) |
| `/p2p-chain` | Цепочка зависимых шагов |
| `/p2p-scope` | Большая задача (>10 файлов / >1000 LoC) |
| `/p2p-explore` | Неясные требования, нужен brainstorm |
| `/p2p-atlas` | Показать карту задач в сессии |
| `/p2p-capsule` | Сохранить/восстановить контекст |
| `/p2p-metrics` | Метрики качества сессии |
| `/p2p-feedback` | Дать обратную связь системе |
| `/p2p-karpathy` | Karpathy Coding Mode (Template M) |
| `/p2p-teacher` | Этот режим обучения |

**Упражнение:**
Назови команду для случая: "У меня сложная архитектурная задача, не понимаю как разбить".

**Критерий:** ответ — `/p2p-scope` или `/p2p-explore`.

---

## БЛОК 2.2 — /p2p-quorum (самая мощная)

**Теория:**
Запускает 8 агентов (TECTON, IRIS, AXIOM, VECTOR, DATOS, ANON, ARCHITECTON, HELIOS). Каждый оценивает задачу со своей стороны. HELIOS синтезирует финальное решение.
Порог запуска: complexity ≥ 3 или явный запрос.

**Пример:**
```
User: /p2p-quorum design API rate limiting for SaaS
P2P: [QUORUM Tier-3 activated]
     TECTON: architecture suggestion ...
     IRIS: UX implications ...
     AXIOM: edge cases ...
     ...
     HELIOS synth: [final recommendation with weights]
```

**Упражнение:**
Какой агент отвечает за edge cases и G-errors? (подсказка: смотри `.claude/agents/`)

**Критерий:** ответ — AXIOM.

---

## БЛОК 2.3 — /p2p-scope и /p2p-capsule

**Теория:**
`/p2p-scope` — SCOPE.HELM v1.2. Разбивает большую задачу на куски, оценивает план, маршрутизирует по моделям, делит проект на части.
`/p2p-capsule` — сохраняет состояние сессии в YAML (для возврата позже).

**Пример:**
```
User: /p2p-scope refactor monolith to microservices
P2P: [SCOPE.HELM activated]
     SPLITTER: 7 phases identified
     ESTIMATOR: ~14 hours, plan: PRO (4 sessions)
     ROUTER: phases 1-3 → Sonnet, 4-7 → Opus
     CAPSULE: saved as scope_2026-05-14_microservices.yaml
```

**Упражнение:**
У тебя 30 файлов кода для рефакторинга. Какие 2 команды используешь?

**Критерий:** `/p2p-scope` + `/p2p-capsule`.

---

## БЛОК 2.4 — Modifiers и flags

**Теория:**
Команды поддерживают модификаторы:
- `[TIER=N]` — форсировать tier модели (1-4)
- `[AGENT=X]` — конкретный агент
- `[LANG=ru/en]` — язык output
- `[FORMAT=xml/md/code]` — формат
- `[VERBOSE]` — показать reasoning

**Пример:**
`/p2p-quorum design API [TIER=4][LANG=en]`

**Упражнение:**
Напиши команду: "запусти QUORUM на максимальном качестве, output на английском".

**Критерий:** `/p2p-quorum [TIER=4][LANG=en]` или эквивалент.

---

## ПРОВЕРКА LEVEL 2

5 вопросов:
1. Когда использовать `/p2p-quorum` vs `/p2p`?
2. Что делает `/p2p-capsule`?
3. Как форсировать tier=4?
4. Какой агент за edge cases?
5. Что такое `/p2p-karpathy`?

**Pass:** 4/5 → Level 3.

---

<a name="level-3"></a>
# LEVEL 3 — Agents (30 минут)

**Цель:** Понять роль каждого из 8 агентов, когда какой "голос" доминирует.

---

## БЛОК 3.1 — Зачем 8 агентов

**Теория:**
Один LLM ≠ один эксперт. Разделяем мышление на роли — каждая со своим bias.
Это даёт честный multi-perspective review без слепых пятен.
Все 8 — это симулированные через single-call multi-agent prompting (не 8 реальных вызовов).

**Пример:**
Без QUORUM: "Напиши API" → один взгляд, забыли про rate limiting + i18n + GDPR.
С QUORUM: 8 голосов покроют security (AXIOM), UX (IRIS), data (DATOS), edge cases, scalability (ARCHITECTON), etc.

**Упражнение:**
Перечисли 3 риска "single perspective" мышления.

**Критерий:** ≥3 ответа из {bias, blind spots, missed edge cases, no UX, no security, etc}.

---

## БЛОК 3.2 — Профили агентов

**Теория:**
| Агент | Роль | Когда доминирует |
|-------|------|------------------|
| **TECTON** | Architect / Code structure | Сложные системы, design patterns |
| **IRIS** | UX / Communication | UI, copy, onboarding |
| **AXIOM** | Edge cases / G-errors | Security, validation, failure modes |
| **VECTOR** | Performance / Optimization | Speed, memory, scalability |
| **DATOS** | Data / Schema | DB, API contracts, types |
| **ANON** | Anti-patterns / Critique | Code review, refactoring |
| **ARCHITECTON** | Macro architecture | System design, microservices |
| **HELIOS** | Synth / Final decision | Всегда финальный голос QUORUM |

**Пример:**
Задача "redesign onboarding flow":
- IRIS dominant (UX)
- TECTON support (information arch)
- HELIOS synth

**Упражнение:**
Задача "найти memory leak в Python service". Кто dominant?

**Критерий:** VECTOR.

---

## БЛОК 3.3 — Weights и voting

**Теория:**
В QUORUM веса не равны. По умолчанию все = 1.0. Но Dynamic Weighting v0.2 меняет веса по типу задачи:
- security task → AXIOM × 1.5
- UX task → IRIS × 1.5
- HELIOS всегда tiebreaker (VETO power для критичных рисков)

**Пример:**
Задача "JWT auth implementation":
- AXIOM weight 1.5 (security-heavy)
- TECTON 1.2 (architecture)
- остальные 1.0
- HELIOS synth с учётом весов

**Упражнение:**
Если 5 агентов сказали "approve", но AXIOM сказал "critical security risk" — что произойдёт?

**Критерий:** HELIOS использует VETO (AXIOM критичный риск перевешивает).

---

## БЛОК 3.4 — Sub-QUORUM patterns

**Теория:**
Иногда нужны только 2-3 агента (Sub-QUORUM):
- **Code review pair:** TECTON + ANON
- **Security audit:** AXIOM + ANON
- **UX critique:** IRIS + ANON
- **Performance review:** VECTOR + ARCHITECTON

**Пример:**
`/p2p-quorum [PRESET=code-review]` → запускает только TECTON+ANON.

**Упражнение:**
Какой Sub-QUORUM для "security audit смарт-контракта"?

**Критерий:** AXIOM + ANON (опц. + DATOS для data flow).

---

## ПРОВЕРКА LEVEL 3

5 вопросов:
1. Кто отвечает за edge cases?
2. Что такое HELIOS VETO?
3. Какие Sub-QUORUM знаешь? (≥2)
4. Зачем weighted voting?
5. Назови всех 8 агентов.

**Pass:** 4/5 → Level 4.

---

<a name="level-4"></a>
# LEVEL 4 — QUORUM (30 минут)

**Цель:** Освоить полный orchestration: triggers, voting, weights, HELIOS synth, ATLAS отчёт.

---

## БЛОК 4.1 — Когда QUORUM срабатывает

**Теория:**
3 триггера автозапуска:
1. complexity ≥ 3 (из SIR Scanner)
2. SIR confidence < 0.55
3. Явный `/p2p-quorum`

Также T-routes (T1-T5 из !exploration.md) могут эскалировать.

**Пример:**
```
User: "архитектура для real-time trading platform"
SIR: complexity=5, confidence=0.4 → AUTO QUORUM
[Тurning QUORUM_SIMULATED_PROTOCOL]
```

**Упражнение:**
Простая задача "напиши hello world". Запустится ли QUORUM? Почему?

**Критерий:** нет, complexity=1.

---

## БЛОК 4.2 — QUORUM_SIMULATED_PROTOCOL

**Теория:**
Симулированный multi-agent в single call:
1. Каждый агент даёт ≤ 5 строк своей позиции
2. Format: `<agent name="X">...position...</agent>`
3. HELIOS читает все, синтезирует
4. Output: финальное решение + per-agent breakdown

**Пример output:**
```xml
<quorum>
  <agent name="TECTON">Use CQRS + event sourcing</agent>
  <agent name="IRIS">Status indicators for sync state</agent>
  <agent name="AXIOM">Idempotency keys mandatory</agent>
  ...
  <helios_synth>
    Final: CQRS+ES with idempotency, UI sync indicators.
    Risks: AXIOM flagged race conditions.
    Confidence: 0.82
  </helios_synth>
</quorum>
```

**Упражнение:**
Прочитай пример output. Какие 3 ключевых рекомендации?

**Критерий:** CQRS, idempotency, UI sync.

---

## БЛОК 4.3 — Cognitive Load Formula

**Теория:**
P2P считает cognitive load чтобы не перегрузить LLM:
```
CL = base_complexity × agent_count_factor × context_size_factor
```
Если CL > 0.8 → QUORUM активирует CAPSULE protocol (сжатие).

**Пример:**
8 агентов × complexity=5 × 80K context = CL=0.9 → trigger CAPSULE.

**Упражнение:**
Какое значение CL означает "нужно сжатие контекста"?

**Критерий:** > 0.8.

---

## БЛОК 4.4 — Chain orchestration

**Теория:**
3 паттерна цепочки:
1. **RESEARCH_DRAFT_REVIEW** — исследовать → черновик → ревью
2. **CODE_PIPELINE** — spec → code → tests → review
3. **CROSS_VALIDATE** — 2 параллельных подхода → сравнить

**Пример:**
`/p2p-chain [pattern=CODE_PIPELINE] task="REST API for users"`

**Упражнение:**
Какой pattern для "написать статью + проверить факты + отредактировать"?

**Критерий:** RESEARCH_DRAFT_REVIEW.

---

## ПРОВЕРКА LEVEL 4

5 вопросов:
1. 3 триггера QUORUM?
2. Что делает HELIOS в synth?
3. Что такое CL > 0.8 означает?
4. Назови chain pattern для код-пайплайна.
5. Может ли AXIOM "перевесить" 5 других агентов? Как?

**Pass:** 4/5 → Level 5.

---

<a name="level-5"></a>
# LEVEL 5 — SCOPE.HELM (45 минут)

**Цель:** Управлять большими задачами через SPLITTER/CAPSULE/ROUTER/GUARDIAN.

---

## БЛОК 5.1 — Зачем SCOPE.HELM

**Теория:**
Если задача >10 файлов, >1000 LoC, или предполагает несколько сессий — обычный prompt сломается.
SCOPE.HELM = планировщик + маршрутизатор для multi-session work.

**Пример:**
Задача "мигрировать монолит на микросервисы (50 сервисов)":
- BAD: один огромный prompt, контекст сломается
- GOOD: `/p2p-scope` → SPLITTER создаёт 12 phases → ROUTER распределяет → CAPSULE сохраняет state между сессиями

**Упражнение:**
Когда НЕ нужен SCOPE.HELM? (1 пример)

**Критерий:** маленькая задача (<10 файлов / <1000 LoC).

---

## БЛОК 5.2 — SPLITTER

**Теория:**
SPLITTER разбивает задачу на phases с критериями:
- Каждая phase делается за 1 сессию
- Phases independent OR explicit dependency
- Output phase N = input phase N+1 (formal contract)

**Пример:**
```
SPLITTER output for "rewrite auth":
  phase 1: audit current code [Sonnet, 30min]
  phase 2: design new schema [Opus, 1h]
  phase 3: implement core [Sonnet, 2h]
  phase 4: tests [Sonnet, 1h]
  phase 5: migration script [Opus, 1h]
```

**Упражнение:**
Задача "построить блог с нуля". Сколько phases предложишь? (примерно)

**Критерий:** 4-8 phases (acceptable range).

---

## БЛОК 5.3 — CAPSULE protocol

**Теория:**
CAPSULE — формат сохранения context между сессиями. YAML:
```yaml
capsule:
  task: "..."
  current_phase: 3
  completed: [phase1, phase2]
  pending: [phase4, phase5]
  context:
    decisions: [...]
    files_touched: [...]
    open_questions: [...]
```

**Пример:**
После 1 сессии: `/p2p-capsule save` → YAML на диск.
Через неделю: `/p2p-capsule load auth_2026-05.yaml` → P2P восстановит state.

**Упражнение:**
Какие 3 поля обязательны в CAPSULE?

**Критерий:** task, current_phase, completed (или эквивалент).

---

## БЛОК 5.4 — ROUTER (Model Routing)

**Теория:**
ROUTER решает какая модель для каждой phase:
- Simple/repetitive → Haiku/Sonnet (cheap)
- Architecture decisions → Opus
- Code generation bulk → Sonnet
- Final review → Opus

**Пример:**
12-phase migration: phases 1,2,5,10 → Opus (decisions). Остальные → Sonnet.
Экономия: ~60% vs all-Opus.

**Упражнение:**
8h задачи: 1h architecture + 5h impl + 2h tests. Распредели по моделям.

**Критерий:** Opus 1h, Sonnet 7h (или эквивалент).

---

## БЛОК 5.5 — GUARDIAN

**Теория:**
GUARDIAN — мониторинг плана. Считает:
- Estimated cost vs budget
- Estimated time vs deadline
- Plan limits (FREE/PRO/MAX5X/MAX20X)
- Inline report после каждой phase

**Пример:**
```
GUARDIAN report (phase 3 of 7):
  spent: $4.20 / $20 budget
  time: 2.5h / 8h estimate
  plan: PRO (within limits)
  status: ✅ on track
```

**Упражнение:**
GUARDIAN говорит "70% budget на 30% задачи". Что делать?

**Критерий:** упростить, разбить, route на cheaper model, спросить пользователя.

---

## ПРОВЕРКА LEVEL 5

5 вопросов:
1. Когда НУЖЕН SCOPE.HELM?
2. Что делает SPLITTER?
3. 3 обязательных поля CAPSULE?
4. Какая модель для "финального review"?
5. Что мониторит GUARDIAN?

**Pass:** 4/5 → FINAL CERTIFICATION.

---

# FINAL CERTIFICATION

10 вопросов покрывая все уровни. Pass: 8/10.

После сертификации:
- Бейдж в `_live/live_core.md`: `teacher_certified: true`
- Доступ к `advanced examples` (sandbox с реальными production задачами)
- Рекомендация: попробовать v8C.2 на реальной задаче

---

<a name="qa-faq"></a>
# Q&A FAQ — Топ-30 вопросов

### Q1. Зачем мне P2P если можно просто писать промпты?
A: На простых задачах разницы нет. На сложных (complexity ≥ 3) — разница в качестве 2-5×. P2P — это инструмент когда стоимость ошибки высока.

### Q2. P2P работает с GPT/Gemini?
A: Да через Translation Layer (`!contract.md`). Native — Claude. Для других моделей есть adaptation (`vendors/tier1-4.md`).

### Q3. Сколько токенов жрёт P2P?
A: Минимальная сборка ~80K, стандартная ~150K, полная ~300K. Modular loading позволяет грузить только нужное.

### Q4. Что такое XML-native?
A: Claude 4.x лучше понимает XML теги чем markdown. P2P использует `<role>`, `<step>`, `<must>` etc. — даёт +15-20% качества.

### Q5. Можно ли отключить QUORUM?
A: Да: `/p2p [QUORUM=off]` или через `p2p.config.md`. Но для complex задач — не рекомендуется.

### Q6. Что такое G-errors?
A: 20 типов системных ошибок Claude (G1-G20). G6=stop-token confusion, G7=temperature+thinking conflict, G8=budget_tokens deprecated. См. `!!db_v8C.md` раздел 4.

### Q7. Чем v8C.2 отличается от v8C.3?
A: + plugin manifest для one-click import, + interactive teacher mode (`/p2p-teacher` + `!teacher.md`), + packaging scripts, + INSTALL docs.

### Q8. Можно ли использовать P2P в Claude Code и в Cowork одновременно?
A: Да. v8C.2 — это plugin, ставится в обе среды одинаково.

### Q9. Что делать если QUORUM "не согласен сам с собой"?
A: HELIOS использует tiebreaker logic. Если spread > 30% — auto-trigger Exploration Mode для прояснения.

### Q10. Где хранится state между сессиями?
A: В `_live/live_core.md` (working memory) + CAPSULE YAML файлы для долгосрочного.

### Q11. Можно ли создать своего агента?
A: Технически да — добавить файл в `.claude/agents/`. Но рекомендуется переиспользовать 8 существующих с разными prompts.

### Q12. P2P open source?
A: Да, MIT license. См. `plugin.json`.

### Q13. Как обновить P2P?
A: Скачать новую версию папки vXC.Y, заменить старую. CAPSULE файлы совместимы.

### Q14. Что такое SIR Scanner?
A: Stage 1 routing — анализирует запрос за <100 токенов, выбирает route без загрузки больших файлов. См. `!intent.md`.

### Q15. Когда использовать /p2p-explore?
A: Когда требования неясны, или SIR confidence < 0.55, или явный brainstorm.

### Q16. Что такое Template M?
A: Karpathy Coding Mode template. PRE_CODE_DECLARATION + composability M+R / M+I / M+T. См. `!templates.md`.

### Q17. Можно ли передать P2P свою память (long-term)?
A: Да через `!memory.md` Bridge protocol. Поддерживает CAPSULE injection + selective recall.

### Q18. Что такое CONSTRAINT_REINJECTION_PROTOCOL?
A: Через каждые 25/50/75 сообщений перевпрыскивает constraints (light/full/capsule) — Claude "забывает" instructions при длинном чате.

### Q19. Что такое DEEP_THINK_VALUE_GATE?
A: 3-вопросный gate перед включением Extended Thinking — экономит токены если задача не требует deep reasoning.

### Q20. Чем p2p-teacher отличается от README?
A: README статичный. Teacher — интерактивный: спрашивает уровень, даёт упражнения, проверяет понимание, сохраняет прогресс.

### Q21. Что делать если /p2p-teacher не запускается?
A: 1) Проверь что plugin установлен 2) `ls .claude/commands/p2p-teacher.md` 3) Перезапусти Claude Code/Cowork.

### Q22. Можно ли пройти teacher на английском?
A: Да: `/p2p-teacher [LANG=en]`. Curriculum переключится. Принципы те же.

### Q23. Сколько времени на весь curriculum?
A: ~2 часа суммарно (Level 1: 10min, L2: 20, L3: 30, L4: 30, L5: 45). Можно по 1 уровню в день.

### Q24. Что если я застрял на упражнении?
A: Команды teacher mode: `подсказка`, `пример`, `пропустить`. Каждый блок имеет fallback path.

### Q25. Зачем p2p.config.md?
A: Персонализация: твой стек, опыт, предпочтения. P2P подстраивает output. Не обязательно но рекомендуется.

### Q26. Можно ли использовать P2P в команде?
A: Да. Каждый член команды ставит plugin локально. CAPSULE файлы можно шарить через git.

### Q27. Что такое Tier 1/2/3/4?
A: Tier модели: 1=cheap/fast (Haiku/DeepSeek), 2=balanced (Sonnet), 3=quality (Opus), 4=max (Opus + Extended Thinking).

### Q28. Когда использовать Tier 4?
A: Сложные decisions, security, architecture, ambiguous requirements. НЕ для bulk code generation.

### Q29. Что такое Routing Memory?
A: P2P запоминает какие агенты успешны на каких задачах, биасит будущие routing decisions. См. `!metrics.md`.

### Q30. Где FAQ по ошибкам?
A: `docs/FAQ_И_ОШИБКИ.md` — все G-errors + типичные user errors + fixes.

---

<a name="cheatsheet"></a>
# CHEATSHEET (одна страница)

```
═══════════════════════════════════════════════════════════
P2P v8C.3 CHEATSHEET
═══════════════════════════════════════════════════════════

КОМАНДЫ (11):
  /p2p              главное меню
  /p2p-quorum       8 агентов голосуют
  /p2p-chain        цепочка шагов
  /p2p-scope        большая задача
  /p2p-explore      brainstorm
  /p2p-atlas        карта задач
  /p2p-capsule      save/load state
  /p2p-metrics      качество сессии
  /p2p-feedback     обратная связь
  /p2p-karpathy     Karpathy coding mode
  /p2p-teacher      обучение (ты сейчас здесь)

АГЕНТЫ (8):
  TECTON      architecture
  IRIS        UX / communication
  AXIOM       edge cases / security
  VECTOR      performance
  DATOS       data / schema
  ANON        critique / antipatterns
  ARCHITECTON system design
  HELIOS      synth / final

MODIFIERS:
  [TIER=1-4]      cheap → max
  [AGENT=NAME]    конкретный агент
  [LANG=ru/en]    язык
  [FORMAT=...]    xml/md/code
  [VERBOSE]       reasoning visible

ТРИГГЕРЫ AUTO-QUORUM:
  complexity ≥ 3
  SIR confidence < 0.55
  явный /p2p-quorum

КОГДА SCOPE.HELM:
  >10 файлов
  >1000 LoC
  >1 session

CL > 0.8 → CAPSULE
DEADLINE 2026-06-15 — удалить legacy API strings
═══════════════════════════════════════════════════════════
```

---

<a name="comprehension"></a>
# COMPREHENSION CHECKS

Все checks — в формате multiple choice. Pass thresholds:
- Level 1-2: 3/4 правильных
- Level 3-4: 4/5
- Level 5: 4/5
- Final cert: 8/10

Полные банки вопросов хранятся inline в каждом Level выше (секции ПРОВЕРКА). Teacher mode сам выбирает рандом из банка.

---

<a name="meta"></a>
# META — как teacher mode работает изнутри

Для разработчиков системы / advanced users:

1. **Storage:** `_live/live_core.md` секция `teacher_progress` — current_level, completed_levels, struggle_topics, last_session
2. **Adaptive routing:** struggle_topics → следующая сессия начнётся с повторения слабого блока
3. **Q&A fallback:** если вопрос не в FAQ — full-text search по `!!core_v8C.md` + `!!db_v8C.md` + ON-DEMAND modules с тегами
4. **Exit handling:** команды `выход`, `позже`, `пауза` → save state → return to `/p2p`
5. **Integration with /p2p-metrics:** teacher_session добавляет `learning_hours` field

**Anti-pattern T-6:** `/p2p-teacher` НИКОГДА не должен запускаться автоматически без явного триггера skill description match или command. Это сломает flow для опытных пользователей.


========================================
VERSION_METADATA
========================================
id: TEACHER_V8C
version: v8C.3-BETA
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
