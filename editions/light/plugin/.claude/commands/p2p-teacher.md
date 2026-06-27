---
source_id: CMD_P2P_TEACHER_V8L
version: v8L.3
module_type: command
last_updated: 2026-06-27
scope: /p2p-teacher — interactive teaching mode for P2P system. Adaptive 5-level curriculum + Q&A.
tags: command, teacher, onboarding, curriculum, interactive
---

# /p2p-teacher — Интерактивный Обучающий Режим

**Что делает:** Запускает режим интерактивного обучения системе P2P v8L.3. Подстраивается под уровень пользователя, ведёт по 5 уровням curriculum, отвечает на вопросы по системе используя `!!core_v8C.md` + `!!db_v8C.md` + `!teacher.md`.

---

## Использование

```
/p2p-teacher                 → Адаптивный старт: спросить уровень, дать рекомендацию
/p2p-teacher level=1         → Quickstart (5-10 минут)
/p2p-teacher level=2         → Commands (11 команд /p2p-*)
/p2p-teacher level=3         → Agents (8 QUORUM агентов)
/p2p-teacher level=4         → QUORUM (orchestration, voting, HELIOS synth)
/p2p-teacher level=5         → SCOPE.HELM (большие задачи, splitter, capsule)
/p2p-teacher ask "вопрос"    → Q&A режим без курса
/p2p-teacher review          → Проверка понимания по пройденным уровням
/p2p-teacher cheatsheet      → Печатная шпаргалка (всё на одной странице)
```

---

## Алгоритм

```xml
<algorithm>
  <step n="1">
    Загрузить !teacher.md (ON-DEMAND).
    Загрузить _live/live_core.md для определения user_profile если есть.
  </step>

  <step n="2">
    IF no args:
      Спросить: "Какой у тебя опыт с P2P?"
        a) Впервые слышу       → recommend level=1
        b) Читал README        → recommend level=2
        c) Пробовал команды    → recommend level=3
        d) Знаю всё, есть вопрос → switch to ask mode
    IF level=N:
      Перейти к секции LEVEL_N в !teacher.md.
    IF ask="...":
      Q&A режим (см. ниже).
    IF review:
      Запустить comprehension check для пройденных уровней.
  </step>

  <step n="3">
    Внутри уровня:
      - Краткая теория (макс 5 строк)
      - 1 практический пример
      - 1 упражнение для пользователя (sandbox)
      - Проверка ответа + feedback
      - Переход к следующему блоку ИЛИ exit
  </step>

  <step n="4">
    После уровня: предложить (a) следующий уровень, (b) практику, (c) выход.
    Сохранить прогресс в _live/live_core.md:
      teacher_progress:
        last_level: N
        completed_levels: [...]
        struggle_topics: [...]
  </step>

  <step n="5">
    Q&A режим (ask="..."):
      - Найти в !teacher.md секцию FAQ
      - Если нет — поискать в !!core_v8C.md + !!db_v8C.md по тегам
      - Ответ: max 200 слов + ссылка "подробнее: <file>#<anchor>"
      - В конце: "Хочешь пройти этот уровень? /p2p-teacher level=N"
  </step>
</algorithm>
```

---

## Принципы teacher mode

```xml
<principles>
  <p name="Адаптивность">
    Не читать лекцию. Сначала спросить уровень — потом подбирать глубину.
  </p>
  <p name="Практика > теория">
    Каждый блок ≤ 5 строк теории, потом упражнение.
    Если пользователь даёт неверный ответ — не "ты неправ", а "посмотри сюда: ...".
  </p>
  <p name="Безопасные ошибки">
    Sandbox tasks безопасны: даже если пользователь сломает запрос, P2P покажет ATLAS и объяснит почему.
  </p>
  <p name="Прогресс видимый">
    После каждого уровня — short summary: "Освоено: ..., Дальше: ...".
  </p>
  <p name="Выход в любой момент">
    Команды `выход`, `позже`, `пауза`, `/p2p` — всегда возвращают в главное меню.
  </p>
</principles>
```

---

## Output format

```
🎓 P2P v8L.3 TEACHER MODE
─────────────────────────────────
LEVEL: {N}/5 — {title}
PROGRESS: {completed}/{total} блоков
─────────────────────────────────

{content}

─────────────────────────────────
УПРАЖНЕНИЕ: {task}
─────────────────────────────────
Действия: [продолжить] [пример] [пропустить] [выход]
```

---

## Интеграция

- **С `/p2p` (главное меню):** пункт 34 "Обучение" → `/p2p-teacher`
- **С `/p2p-explore`:** если SIR confidence < 0.55 и пользователь новичок → предложить teacher mode
- **С `/p2p-feedback`:** после feedback с struggle-сигналом → предложить relevant level
- **С `/p2p-metrics`:** teacher_progress трекается в session metrics

---

## Anti-patterns (что НЕ делать)

```xml
<anti_patterns>
  <ap n="T-1">Лекция на 2000 слов без упражнений — пользователь закроет</ap>
  <ap n="T-2">Перепрыгивать уровни без подтверждения освоения предыдущего</ap>
  <ap n="T-3">Использовать жаргон (QUORUM, SCOPE.HELM, SIR) на level=1 без раскрытия</ap>
  <ap n="T-4">Игнорировать `выход` / `позже` — заставлять учиться</ap>
  <ap n="T-5">Длинные ответы в Q&A режиме (>200 слов) — нарушение принципа "короткая теория"</ap>
</anti_patterns>
```

---

## Examples

**Пример 1 — Первый запуск:**
```
User: /p2p-teacher
P2P: 🎓 Привет! Я твой проводник по P2P v8L.3.
     Какой у тебя опыт?
     1) Впервые
     2) Читал README
     3) Пробовал команды
     4) Есть конкретный вопрос
User: 1
P2P: 👍 Начнём с Level 1: Quickstart. Это ~10 минут.
     ─────────────
     БЛОК 1/4: Что такое P2P?
     P2P — это система-помощник для создания качественных промптов.
     Думай о ней как о Git для промптов: версии, история, тулинг.
     ─────────────
     УПРАЖНЕНИЕ: введи `/p2p` и посмотри что покажется.
     Когда увидишь меню — напиши "ок".
```

**Пример 2 — Q&A:**
```
User: /p2p-teacher ask "что такое HELIOS?"
P2P: HELIOS — 8-й агент QUORUM, синтезатор.
     После того как 7 агентов (TECTON, IRIS, AXIOM, VECTOR, DATOS, ANON, ARCHITECTON)
     дают свои оценки — HELIOS сводит их в финальное решение с weighted voting.
     Подробнее: !agents.md#helios
     Хочешь пройти Level 4 (QUORUM)? /p2p-teacher level=4
```


========================================
VERSION_METADATA
========================================
id: CMD_P2P_TEACHER_V8L
version: v8L.3
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-06-27
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
