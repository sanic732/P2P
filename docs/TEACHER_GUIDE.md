# P2P v8C.2 — Teacher Mode Guide

> Гайд по интерактивному обучающему режиму `/p2p-teacher`.
> Curriculum + Q&A режим. Источник: `!teacher.md` (ON-DEMAND модуль).

---

## ОГЛАВЛЕНИЕ

1. [Что это и зачем](#about)
2. [Запуск](#launch)
3. [5 уровней curriculum](#levels)
4. [Q&A режим](#qa)
5. [Прогресс и сохранение](#progress)
6. [Команды](#commands)
7. [Когда НЕ использовать teacher](#not-for)
8. [FAQ](#faq)

---

<a name="about"></a>
## 1. Что это и зачем

P2P — мощная но сложная система. 42 файла, 11 команд, 8 агентов, 5 режимов. Без проводника новый пользователь тонет.

**Teacher Mode** — это интерактивный курс который:
- Подстраивается под уровень пользователя (новичок / уверенный / эксперт)
- Идёт через 5 уровней с упражнениями, а не лекциями
- Сохраняет прогресс между сессиями
- Имеет Q&A режим для точечных вопросов

Принцип: **практика > теория, ≤5 строк теории на блок**.

---

<a name="launch"></a>
## 2. Запуск

### Через slash-команду
```
/p2p-teacher
```
Адаптивный старт — задаст 1 вопрос про опыт, порекомендует уровень.

### Через natural language (в Cowork)
```
"научи меня P2P"
"как пользоваться этой системой"
"объясни что такое QUORUM"
"с чего начать?"
```
Cowork сам подхватит skill `p2p-teacher` через description triggers.

### Через главное меню
```
/p2p
→ выбрать пункт [34] 🎓 ОБУЧЕНИЕ
```

---

<a name="levels"></a>
## 3. 5 уровней curriculum

| # | Название | Время | Содержание |
|---|----------|-------|------------|
| 1 | **Quickstart** | 10 мин | Что такое P2P, как запустить, ATLAS |
| 2 | **Commands** | 20 мин | 11 команд /p2p-*, modifiers, flags |
| 3 | **Agents** | 30 мин | 8 агентов QUORUM, профили, weights |
| 4 | **QUORUM** | 30 мин | Orchestration, voting, HELIOS synth, chains |
| 5 | **SCOPE.HELM** | 45 мин | SPLITTER, CAPSULE, ROUTER, GUARDIAN |

**Итого:** ~2 часа на полный курс. Рекомендуется по 1 уровню в день.

### Структура каждого уровня

```
LEVEL N: <title>
├── Pre-check (1 вопрос про опыт)
├── БЛОК N.1 (теория ≤5 строк + пример + упражнение)
├── БЛОК N.2 (...)
├── БЛОК N.3 (...)
├── БЛОК N.4 (...)
└── ПРОВЕРКА (3-5 вопросов, pass threshold)
```

### Прыгать через уровни

```
/p2p-teacher level=3
```
Принудительно начать с Level 3. Полезно если ты опытный, но забыл детали QUORUM.

⚠ **Anti-pattern T-2:** teacher mode НЕ даст пропустить уровень без прохождения предыдущего — система покажет рекомендацию пройти базу.

---

<a name="qa"></a>
## 4. Q&A режим

Если у тебя конкретный вопрос (не нужен полный курс) — используй ask:

```
/p2p-teacher ask "что такое HELIOS?"
/p2p-teacher ask "когда использовать /p2p-scope?"
/p2p-teacher ask "что такое G7 error?"
```

### Что произойдёт

1. Teacher ищет ответ в `!teacher.md` секция Q&A FAQ (30 вопросов)
2. Если не найдено — full-text search по `!!core_v8C.md` + `!!db_v8C.md` по тегам
3. Ответ: max 200 слов + ссылка `подробнее: <file>#<anchor>`
4. В конце: предложение пройти relevant level

### Топ-30 FAQ покрыты

Включая:
- "Зачем мне P2P если можно просто писать промпты?"
- "Сколько токенов жрёт P2P?"
- "Что такое XML-native?"
- "Можно ли отключить QUORUM?"
- "Что такое G-errors?"
- "Чем v8C.2 отличается от v8C.1?"
- ...и ещё 24 вопроса

Полный список — `!teacher.md#qa-faq`.

---

<a name="progress"></a>
## 5. Прогресс и сохранение

Teacher сохраняет state в `_live/live_core.md`:

```yaml
teacher_progress:
  last_level: 3
  completed_levels: [1, 2]
  struggle_topics: [HELIOS_voting, CL_formula]
  certified: false
  last_session: 2026-05-14T15:30:00
```

### Проверка прогресса

```
/p2p-teacher review
```
Покажет:
- Какие уровни пройдены
- Какие блоки давались тяжело (struggle_topics)
- Что повторить

### Финальная сертификация

После Level 5 → 10-вопросный test покрывающий все уровни.
**Pass:** 8/10 → бейдж `teacher_certified: true` в live_core.

После сертификации:
- Доступ к "advanced examples" (sandbox с production задачами)
- В `/p2p-metrics` появляется поле `learning_hours`

---

<a name="commands"></a>
## 6. Команды teacher mode

| Команда | Что делает |
|---------|------------|
| `/p2p-teacher` | Адаптивный старт |
| `/p2p-teacher level=N` | Прыжок на уровень N (1-5) |
| `/p2p-teacher ask "..."` | Q&A на конкретный вопрос |
| `/p2p-teacher review` | Проверка прогресса + comprehension check |
| `/p2p-teacher cheatsheet` | Печатная шпаргалка (одна страница) |
| `/p2p-teacher [LANG=en]` | Curriculum на английском |
| `выход` / `позже` / `пауза` | Сохранить state и вернуться в /p2p |

### Modifiers (можно комбинировать)
```
/p2p-teacher level=4 [LANG=en]
/p2p-teacher ask "что такое CAPSULE?" [VERBOSE]
```

---

<a name="not-for"></a>
## 7. Когда НЕ использовать teacher

- **Генерация промптов** → используй `/p2p`
- **QUORUM анализ задачи** → используй `/p2p-quorum`
- **Большая задача (>10 файлов)** → используй `/p2p-scope`
- **Brainstorm** → используй `/p2p-explore`
- **Discovery brand voice** → используй skill `brand-voice:discover-brand`

Teacher — для **обучения системе**, не для применения её к рабочим задачам.

---

<a name="faq"></a>
## 8. FAQ

### Q: Сколько времени нужно?
~2 часа на весь курс. Можно по 10-45 минут за раз. Прогресс сохраняется.

### Q: Можно ли проходить нелинейно?
Да: `level=N`. Но teacher предупредит если есть зависимость (Level 4 предполагает знание Level 3).

### Q: Что если я застрял на упражнении?
Команды: `подсказка`, `пример`, `пропустить`. Каждый блок имеет fallback.

### Q: Можно ли пройти на английском?
Да: `/p2p-teacher [LANG=en]`. Курс переключится. Принципы те же.

### Q: Где сохраняется прогресс?
`_live/live_core.md` секция `teacher_progress`. Если используешь plugin — внутри plugin storage. Если project-level — внутри проекта.

### Q: Что делать после сертификации?
1. Применять P2P на реальных задачах
2. Делиться обратной связью через `/p2p-feedback`
3. Если есть продвинутые сценарии — `docs/CLAUDE_ВОЗМОЖНОСТИ.md`, `docs/AGENTS_GUIDE.md`

### Q: Можно ли использовать teacher параллельно с работой над задачей?
Да. Teacher и /p2p — независимые режимы. Capsule сохраняет state обоих отдельно.

### Q: Что если я хочу учить кого-то другого?
Дай ему ссылку на `INSTALL.md` + скажи запустить `/p2p-teacher`. Курс самодостаточен.

### Q: Можно ли добавить свои уроки?
Технически — да, редактируя `!teacher.md`. Рекомендуется делать это в форке/PR, не in-place — обновления P2P перетрут изменения.

### Q: Teacher работает в Claude.ai Chat?
Только если загружен `!teacher.md` в knowledge base (Метод 4 установки). Команда `/p2p-teacher` сама по себе там не работает — slash-команды только в Code/Cowork.

### Q: Это серьёзный курс или "просто README с questions"?
5 уровней, 20 блоков с упражнениями, 30 FAQ, comprehension checks, final cert, ~820 строк curriculum. Сделано с учётом anti-patterns образования (не лекция, не overwhelm, exit always available).

---

## См. также

- `../!teacher.md` — сам curriculum (source of truth)
- `../.claude/commands/p2p-teacher.md` — техническая спека команды
- `../.claude/skills/p2p-teacher/SKILL.md` — skill metadata для Cowork
- `НАЧАЛО_РАБОТЫ.md` — alternative quickstart без teacher mode


========================================
VERSION_METADATA
========================================
id: TEACHER_GUIDE_V8C
version: v8C.2
type: docs
edition: CLAUDE_NATIVE
last_verified: 2026-05-14
invariants_passed: [I1_yaml_n/a, I2_api_strings, I5_version_metadata]
========================================
