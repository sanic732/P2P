---
name: rag-grounding
description: >-
  Generate a ready grounding/system prompt that forces a model to answer strictly
  from attached sources (RAG), in that model's native syntax. Use when the user
  wants to "промпт для работы с источниками / NotebookLM", "как считывать базу",
  "grounding prompt", "промпт чтобы не выдумывал, только по файлам", "собери
  системный промпт под Gemini/Claude/GPT для RAG", or needs a citation-forcing
  query prompt for a notebook/attached docs. Outputs PERSONA/TASK/CONTEXT/OUTPUT/
  GUARD framework adapted per model (Claude XML, Gemini Zero-XML, GPT ≤7 rules,
  Grok topic-anchor, DeepSeek minimal, Qwen/GLM markdown-JSON). NOT for preparing
  source files (use rag-prep) and NOT for choosing a tool (use rag-router).
version: 1.0
tags: [rag, grounding, prompt, citations, anti-hallucination, per-model]
---

# rag-grounding — промпт-запрос к источникам («как считывать»)

Собирает готовый системный промпт, который заставляет модель отвечать СТРОГО по
прикреплённым источникам, с цитатами и маркером UNKNOWN — в нативном синтаксисе
выбранной модели.

## Когда применять / НЕ применять
**Применять:** нужно надёжно «прочитать» базу/блокнот без отсебятины; собрать
grounding-промпт под конкретную модель. **НЕ применять:** подготовка самих файлов
(→ `rag-prep`); выбор инструмента/стратегии (→ `rag-router`).

## Каркас (неизменный костяк)
`PERSONA` → `TASK` → `CONTEXT_SCOPE` → `OUTPUT_CONTRACT` → `ANTI_HALLUCINATION_GUARD`.
Меняются только Task/Output под задачу; grounding и guard остаются.

Правило формулировок — **позитивно**: «отвечай только на основе источников» и
«каждый тезис — с цитатой [файл, §]», а не «не галлюцинируй».

## Адаптация под модель (обязательно)
Один контракт — разный синтаксис и обход бага модели:
- **Claude (Opus 4.8 / Sonnet 4.6):** XML-теги (`<role><rules><task>`), нативно.
- **Gemini (3.1 Pro / 3.5 Flash):** Zero-XML, только markdown-заголовки (XML
  триггерит деградацию — баг G2). Идеально под NotebookLM.
- **GPT-5.5:** markdown, ≤7 пар MUST/MUST NOT (иначе тихая деградация — G9).
- **Grok 4.3:** обрамить Topic Anchor сверху и снизу (дрейф темы — G3).
- **DeepSeek:** минимализм, не навязывать структуру и не писать «думай пошагово»
  (ломает нативный reasoning); fetch у него нет — RAG только через прикреплённые файлы.
- **Qwen / GLM:** markdown + строгий JSON-режим.

Готовые блоки под каждую модель (копировать) — в `reference/model_templates.md`
(полированные; сырые исходные заготовки — в `reference/model_templates_source.txt`).
Самые дешёвые модели (Haiku, Gemini 3.5 Flash-Lite) исключать: на них строгий
grounding нестабилен.

## Процесс
1. Спроси/определи целевую модель и задачу.
2. Возьми каркас, подставь Task/Output, переупакуй под синтаксис модели и её баг.
3. Выдай готовый промпт одним блоком для копирования.

## Self-check
- [ ] Есть все 5 секций каркаса; guard сформулирован позитивно.
- [ ] Синтаксис строго под целевую модель (XML только для Claude; Gemini — Zero-XML).
- [ ] Соблюдён лимит правил для GPT; Topic Anchor для Grok.
- [ ] Требование цитат [файл, §] и маркер UNKNOWN присутствуют.
