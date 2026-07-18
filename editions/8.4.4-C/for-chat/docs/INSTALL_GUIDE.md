---
source_id: INSTALL_GUIDE_V8C3
version: v8C.3
module_type: docs
last_updated: 2026-06-12
scope: Установка P2P v8C.3 и переход с v8C.2. Не содержит информации о переходе с более ранних версий.
tags: docs, install, upgrade, v8c3
---

# P2P v8C.3 — РУКОВОДСТВО ПО УСТАНОВКЕ

> Для пользователей v8C.2 — здесь только то что изменилось.  
> Полная карта файлов → `docs/MODULE_REFERENCE.md`  
> Визуальная архитектура → `docs/MINDMAP_v8C3.md`

---

## ЧТО НОВОГО В v8C.3 (если ты с v8C.2)

| Изменение | v8C.2 | v8C.3 |
|-----------|-------|-------|
| Основная модель | Opus 4.7 | **Opus 4.8** (coding FIXED) |
| Новые модули | 0 | **6 новых** (!rag, !reasoning, !routing, !compression, !security, !optimization) |
| Меню | 34 пункта | **40 пунктов** (35-40 динамические) |
| VERSION_COMPAT | нет | **есть** — управление v8C.2/v8C.3 логикой |
| Логотип | нет | **ASCII логотип** при старте |
| Live specs | live_specs.md | **live_specs.md** (14 вендоров) |
| Документация | 1 файл | **5 файлов** в docs/ |

---

## БЫСТРЫЙ СТАРТ (Claude Projects / Chat)

### 1. Загрузи базовые файлы (BASE — обязательно)
```
_preloader.md
!!core_v8C.md
!!db_v8C.md
_live/MANIFEST.md
_live/live_core.md
_live/live_claude.md
```

### 2. Добавь live данные
```
_live/live_vendors.md   ← API strings, цены, routing
```

### 3. Активируй нужные v8C.3 модули (опционально)

Открой `_preloader.md`, найди секцию `VERSION_COMPAT`, измени:
```yaml
VERSION_COMPAT:
  v8C2: on    # оставь on — не трогай базовую логику
  v8C3: off   # измени на on если хочешь все v8C.3 модули
              # или оставь off и настрой гранулярно ниже

  MODULE_RAG: false        # → true если работаешь с документами
  MODULE_REASONING: false  # → true если нужны расширенные цепочки
  MODULE_ROUTING: false    # → true для умного выбора модели
  MODULE_COMPRESSION: false # → true если проблемы с контекстом
  MODULE_SECURITY: false   # → true для аудита промптов
  MODULE_OPTIMIZATION: false # → true для авто-улучшения промптов
```

Затем загрузи соответствующие `!*.md` файлы в Project Knowledge.

### 4. Напиши "старт" или "/start"

Увидишь:
```text
██████╗ ██████╗ ██████╗
...
P2P v8C.3 | LiveSpecs: 2026-06-09
```
И меню с пунктами [1-34] + активными v8C.3 пунктами.

---

## УСТАНОВКА ДЛЯ CLAUDE CODE (cowork-code)

Если используешь Claude Code (desktop/VS Code extension):

1. Скопируй папку `.claude/` в корень своего проекта
2. Файлы подхватятся автоматически через SKILL механизм
3. VERSION_COMPAT настраивается в `skills/p2p/preloader.md`

---

## РЕЖИМЫ VERSION_COMPAT — ОБЪЯСНЕНИЕ ПРОСТЫМИ СЛОВАМИ

**Вариант 1: Только v8C.2 логика (рекомендуется для начала)**
```yaml
v8C2: on
v8C3: off
```
Работает как раньше. Никаких изменений в поведении.

**Вариант 2: Добавить один модуль**
```yaml
v8C2: on
v8C3: off
MODULE_RAG: true   # только RAG включён, остальное — v8C.2
```
Загружается только !rag.md, пункт [35] появляется в меню.

**Вариант 3: Оба режима + умный выбор**
```yaml
v8C2: on
v8C3: on
```
Все v8C.3 модули доступны. При конфликте техник — P2P спрашивает что делать:
```
[CONFLICT] Обнаружен конфликт
  [A] v8C.2 логика  [B] v8C.3 логика  [C] Запомнить выбор
```

**Вариант 4: Авто-определение**
```yaml
MODULE_RAG: auto
MODULE_ROUTING: auto
```
P2P сам определяет по контексту задачи нужен ли модуль. Удобно если не хочешь думать о настройке.

---

## ТОКЕН-БЮДЖЕТ (что загружать для какой задачи)

| Задача | Загружай | Токенов |
|--------|---------|---------|
| Быстрый вопрос | BASE (6 файлов) | ~14K |
| Генерация промптов | BASE + !contract.md | ~17K |
| Работа с агентами | BASE + !agents.md + !scope.md | ~19K |
| RAG / документы | BASE + !rag.md + !routing.md | ~19K |
| Всё сразу | BASE + все !*.md | ~59K |

> Совет: начни с LIGHT пресета (BASE + live_vendors), добавляй модули по мере необходимости.

---

## ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ

**Q: Можно ли оставить v8C.2 файлы нетронутыми?**  
A: Да. v8C.3_release — отдельная папка. v8C.2 не изменён.

**Q: Новые [35-40] пункты в меню мешают?**  
A: Нет — они появляются только при загруженных !*.md файлах. По умолчанию скрыты.

**Q: Opus 4.8 обязателен?**  
A: Нет. Opus 4.7 и Sonnet 4.6 работают полностью. 4.8 рекомендован для coding задач T4.

**Q: Как обновить live specs когда выйдут новые?**  
A: Скачать новый `live_specs_YYYYMMDD.md`, обновить ссылки `live_specs_ref` в MANIFEST.md и live_vendors.md. База v8C.3 не меняется.

---

## CHANGELOG v8C.2 → v8C.3

| Дата | Изменение |
|------|----------|
| 2026-06-12 | ALPHA релиз v8C.3 |
| 2026-06-12 | +6 новых ON-DEMAND модулей (v8C.3 tier) |
| 2026-06-12 | +VERSION_COMPAT + CONFLICT_RESOLVER в _preloader.md |
| 2026-06-12 | +ASCII логотип P2P в !!core_v8C.md |
| 2026-06-12 | +Динамическое меню [35-40] в !!core_v8C.md |
| 2026-06-12 | +Claude Opus 4.8 как T4 PRIMARY в routing |
| 2026-06-12 | +10 вендоров в live_vendors.md (Manus, MiniMax и др.) |
| 2026-06-12 | +live_specs.md (PRIORITY:OVERRIDE, 14K токенов) |
| 2026-06-12 | +docs/ папка: MODULE_REFERENCE, MINDMAP, TECHNIQUES, INSTALL, CHANGELOG |
