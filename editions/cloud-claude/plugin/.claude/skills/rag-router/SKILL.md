---
name: rag-router
description: >-
  Recommend the right RAG approach and environment for a task: direct file attach
  vs NotebookLM vs Cowork vs plain chat, and naive / RAPTOR / LongRAG strategy,
  plus a suitable model. Use when the user asks "что выбрать под задачу", "куда
  грузить документы", "NotebookLM или Cowork / напрямую", "какую RAG-стратегию",
  "какую модель под этот корпус", "which RAG approach", or is unsure where to put
  their data. Decides by corpus size, task type (strict-grounding vs creative vs
  code), data location (cloud vs local) and reproducibility needs. NOT for prepping
  files (use rag-prep) or writing the query prompt (use rag-grounding).
version: 1.0
tags: [rag, routing, decision, notebooklm, cowork, strategy, model-choice]
---

# rag-router — выбор среды и стратегии под задачу

Советует, КУДА класть данные и КАК их извлекать, по размеру корпуса, типу задачи
и месту данных. Стержень — «задача → инструмент», без гадания.

## Когда применять / НЕ применять
**Применять:** не ясно, брать «+»/NotebookLM/Cowork/чат и какую стратегию/модель.
**НЕ применять:** готовить файлы (→ `rag-prep`); писать сам запрос (→ `rag-grounding`).

## Ось 1 — среда (куда грузить)
```
Строгая опора на документы + цитаты              → NotebookLM (облако)
Креатив / микс файлов с вебом                      → Gemini-чат, файлы через «+»
Многошаговая офисная работа с локальными файлами   → Claude Cowork (ПК)
Разработка / правки кода                            → Claude Code / Antigravity IDE
Просто обсудить, пара файлов                        → Chat / Project
```
Развилка «+» vs NotebookLM: напрямую — модель мешает «от себя» (надёжно до ~50K
токенов); через NotebookLM — выжимка с цитатами, но риск туннельного зрения.

## Ось 2 — стратегия (как извлекать), по размеру корпуса
```
< 20 док / < 50K токенов          → Naive RAG / прямое прикрепление
20–500 документов                 → RAPTOR (иерархическое дерево сводок)
> 500 док / высокая связность      → векторная база + LongRAG (единица — документ)
Глобальные вопросы «темы корпуса»  → GraphRAG (community-сводки)
Многошаговые цепочки по докам       → multi-hop / итеративный (агентная среда)
```

## Ось 3 — место данных и регуляторика
- Облако Google, нужен grounded-ресёрч → **NotebookLM** (данные не идут в обучение).
- Локальные файлы/офис на ПК → **Cowork**.
- Регулируемое (HIPAA/PCI/SOX) → ни Cowork, ни «как есть» — нужен отдельный контур.

## Модель под кейс (ориентир)
Строгий grounding/большой контекст → Opus 4.8 / Gemini 3.1 Pro; быстро/массово →
Sonnet 4.6 / Gemini 3.5 Flash. Дешёвые (Haiku, Flash-Lite) — не для строгого RAG.

## Вывод
Дай 1 рекомендацию (среда + стратегия + модель) + 1–2 строки «почему» и явное
«когда это менее уместно». Правильный вопрос — не «что лучше вообще», а «что меньше
всего мешает этой задаче».
