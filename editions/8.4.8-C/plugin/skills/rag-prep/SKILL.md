---
name: rag-prep
description: >-
  Prepare and clean a document so it works well in a RAG source (NotebookLM,
  Claude Projects/Cowork, any retrieval backend). Use when the user wants to
  "подготовить документ под RAG / NotebookLM", "почистить исходник для базы
  знаний", "разбить на чанки / структурировать под retrieval", "prep doc for
  RAG", "make this RAG-ready", or hands a messy/long file to upload to a notebook.
  Restructures into clean Markdown: one file = one semantic zone, header-based
  sections (chunk-friendly), frontmatter + ## TAGS + anchors, fixes IF/THEN
  splits, dedups, suggests splitting big files. NOT for querying a RAG (use
  rag-grounding) and NOT for choosing a tool (use rag-router).
version: 1.0
tags: [rag, preprocessing, chunking, notebooklm, cowork, markdown, ingestion]
---

# rag-prep — подготовка источника под RAG

Превращает сырой/длинный документ в источник, который RAG-движок хорошо режет на
чанки и точно извлекает. Это «предварительное редактирование» перед загрузкой в
NotebookLM / Claude Project / Cowork.

## Когда применять / НЕ применять
**Применять:** перед загрузкой материала в RAG-источник; чистка «простыни»;
структурирование под retrieval. **НЕ применять:** нужно задать запрос к уже
готовой базе (→ `rag-grounding`); выбрать инструмент/стратегию (→ `rag-router`).

## Принцип
Качество ответа RAG = качество попавших в контекст чанков. Значит каждый чанк
должен быть самодостаточным и точно именованным. Правило: **один файл = одна
семантическая зона, один параграф = одна концепция, один тег = один сигнал.**

## Что делает (по шагам)
1. **Структура.** Режет текст на разделы по Markdown-заголовкам (`#`, `##`) —
   это естественные границы чанков. Никакого «полотна» без заголовков.
2. **Чанк-безопасность.** Логические блоки (`IF … THEN`, определение+пояснение)
   держит целиком в одном разделе. Где нужно — закладывает overlap-формулировки
   на границах.
3. **Frontmatter** в шапку файла: `source_id`, `tags`, при необходимости
   `depends_on` (граф связей).
4. **Якоря и теги.** Стабильные `#ID` на ключевых блоках (для точного lookup) +
   `## TAGS: …` в конце (тематическая выборка).
5. **Чистка и дедуп.** Убирает шум/повторы; дубли заменяет ссылкой, а не копией.
6. **Дробление.** Если файл несёт несколько зон — предлагает разбить на отдельные
   файлы (одна зона = один файл) и даёт строку для `_INDEX.md`.

Полный стандарт разметки (frontmatter, rag_zone, rag_anchor, дедуп, граф
зависимостей) — в `reference/rag_metaprompt_standard.md`; открывать при сложной
многофайловой структуре.

## Важно (анти-мифы)
- Большое окно (1M) **не отменяет** структуру: retrieval-качество ≠ размер окна.
- Символьный тег `[A-P_RULES]` в dense-поиске «растворяется» — для надёжного
  lookup дублируй ID в frontmatter/метаданных и рассчитывай на гибридный поиск.

## Self-check перед выдачей
- [ ] Есть заголовки-границы; нет «полотна» без структуры.
- [ ] Ни один `IF…THEN` / определение не разорваны между разделами.
- [ ] В шапке frontmatter, в конце `## TAGS`, на ключевых блоках — якоря.
- [ ] Дубли убраны/заменены ссылкой.
- [ ] Если зон несколько — предложено дробление + строки для `_INDEX`.
- [ ] Вывод — чистый Markdown в UTF-8.
