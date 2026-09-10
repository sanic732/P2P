---
name: notebook-pack
description: >-
  Assemble a complete, RAG-ready source bundle for NotebookLM / Claude Projects /
  Cowork from raw materials — end to end. Use when the user wants to "собрать
  блокнот / базу знаний под NotebookLM", "сделать комплект источников для Cowork",
  "build a notebook pack", "подготовь всё для загрузки в RAG", or has a pile of
  docs to turn into a structured, queryable knowledge base. Produces _MASTER_PROMPT
  (grounding system prompt), _INDEX (file map), _GLOSSARY, and cleaned per-zone
  source files with frontmatter/anchors/tags. Combines rag-prep + rag-grounding +
  rag-router into one deliverable.
version: 1.0
tags: [rag, notebooklm, cowork, bundle, knowledge-base, end-to-end]
---

# notebook-pack — готовый комплект источников под RAG

End-to-end сборка: из набора сырых материалов делает структурированную базу,
которую остаётся загрузить в NotebookLM / Project / Cowork и сразу спрашивать.
Объединяет `rag-prep` (чистка/структура), `rag-grounding` (мастер-промпт) и
`rag-router` (выбор стратегии).

## Когда применять / НЕ применять
**Применять:** есть материалы → нужен цельный комплект под загрузку. **НЕ применять:**
надо обработать один файл (→ `rag-prep`) или только собрать запрос (→ `rag-grounding`).

## Что собирает (структура комплекта)
```
notebook/
├── _MASTER_PROMPT.md   grounding-каркас (PERSONA/TASK/CONTEXT/OUTPUT/GUARD),
│                        в синтаксисе целевой модели — системный промпт блокнота
├── _INDEX.md           карта файлов + граф зависимостей (тег → файлы)
├── _GLOSSARY.md        термины проекта (терминологический якорь)
└── <зоны>.md           источники: одна зона = один файл, frontmatter+TAGS+якоря
```

## Процесс
1. **Маршрут (rag-router):** оцени объём/тип → стратегия (naive/RAPTOR/LongRAG),
   среда (NotebookLM/Cowork), целевая модель.
2. **Подготовка (rag-prep):** каждый источник → чистый Markdown, одна зона = один
   файл, заголовки под чанкинг, frontmatter + `## TAGS` + якоря, без разрыва IF/THEN.
3. **Индекс и глоссарий:** собери `_INDEX.md` (таблица «ID → назначение → связи») и
   `_GLOSSARY.md` (ключевые термины с определениями своими словами).
4. **Мастер-промпт (rag-grounding):** `_MASTER_PROMPT.md` под целевую модель, с
   принуждением к цитатам и маркером UNKNOWN, guard сформулирован позитивно.
5. **Чек запуска:** прогнать чек-лист готовности (ниже).

Полные образцы и стандарт — в `reference/rag_notebook_prompt.md` (готовый системный
промпт + рабочая инструкция) и `reference/rag_metaprompt_standard.md` (стандарт
разметки мультифайловых систем). Открывать при сборке.

## Чек-лист готовности комплекта
- [ ] `_MASTER_PROMPT` вставлен, значения подставлены под проект и модель.
- [ ] Есть `_INDEX.md` с картой и зависимостями; есть `_GLOSSARY.md`.
- [ ] Каждый файл: одна зона, frontmatter + `## TAGS`, якоря; нет «простыней».
- [ ] Дубли заменены ссылками; IF/THEN не разорваны.
- [ ] Версия = отдельный блокнот (для крупных версий).
- [ ] Прогон 10 тестовых запросов: цитаты точные? правильный файл? нет смешения тем?
- [ ] Все файлы — UTF-8.
