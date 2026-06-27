---
source_id: RAG_MODULE_V8C3
version: v8C.3
module_type: on-demand
triggers: "rag|raptor|retrieval|вектор|поиск по базе|document search|ретривал|векторная"
depends_on: !!core_v8C.md, !!db_v8C.md
last_updated: 2026-06-12
token_estimate: ~2800
scope: RAG техники для P2P v8C.3 — RAPTOR, векторный поиск, адаптивный ретривал. Загружается по триггеру или MODULE_RAG=true.
tags: rag, raptor, retrieval, vectors, on-demand, v8c3
conflict_with_v8C2: none
---

# P2P v8C.3 — RAG MODULE (!rag.md)

> Загружен: добавлен пункт [35] в меню.

---

## ТЕХНИКИ RAG (интегрированные)

### RAPTOR — Recursive Abstractive Processing for Tree-Organized Retrieval
**Источник:** arXiv 2401.18059 (Sarthi et al., Stanford NLP 2024)  
**Суть:** Иерархическое дерево документов — рекурсивная кластеризация и суммаризация чанков на нескольких уровнях. Дерево позволяет извлекать информацию на любом уровне абстракции.

**Когда использовать:** Большие корпусы (>50 документов), нужны ответы как на детальные так и на общие вопросы.

**Применение в P2P:**
```
[RAPTOR-RAG]
Шаг 1: Разбить документы на чанки (512-1024 токенов)
Шаг 2: Кластеризовать похожие чанки (UMAP + GMM)
Шаг 3: Суммаризовать каждый кластер → узел дерева L1
Шаг 4: Повторить для L1 → L2, L2 → L3
Шаг 5: При запросе — извлечь с нужного уровня (collapsed tree или tree traversal)
Шаг 6: Подать в контекст с метаданными уровня
```

---

### LongRAG — Long-Context RAG
**Источник:** arXiv 2410.18050  
**Суть:** Вместо маленьких чанков — большие retrieval units (весь документ или большая секция). Снижает шум, повышает recall для длинных запросов.

**Когда использовать:** Модели с >200K контекстом, документы с высокой взаимосвязанностью.

**Применение в P2P:**
```
[LONGRAG]
target_model: claude-opus-4-8 (1M ctx) / gemini-3.1-pro (1M ctx)
retrieval_unit: "full document" или "major section" (не чанки)
top_k: 3-5 (меньше units, но больше каждый)
```

---

### adRAP / Dynamic RAPTOR
**Источник:** arXiv 2410.01736  
**Суть:** RAPTOR с адаптивным выбором уровня в зависимости от типа запроса. Fact-based queries → нижние уровни. Summary queries → верхние уровни.

**Применение в P2P:**
```
[DYNAMIC-RAPTOR]
Query Classification:
  factual/specific → level 0 (raw chunks)
  thematic/summary → level 1-2
  abstract/overview → level 2-3
```

---

## RAG ROUTING (Integration с !routing.md)

```
RAG задача → выбор стратегии:

IF corpus < 20 docs AND docs < 50K tokens:
    → Naive RAG (прямая загрузка в контекст)
    → Модель: claude-opus-4-8 (1M ctx)

IF corpus = 20-500 docs:
    → RAPTOR (иерархическое дерево)
    → Модель: claude-opus-4-8 / gemini-3.1-pro

IF corpus > 500 docs OR needs semantic:
    → Full Vector DB + RAPTOR
    → Модель: по задаче

IF docs high interconnectedness:
    → LongRAG (большие retrieval units)
```

---

## CONFLICT_RESOLVER DECLARATIONS

Этот модуль НЕ конфликтует с базовой логикой v8C.2 — аддитивный.

При работе с [15] Поиск в базе знаний (v8C.3):
- v8C.2: keyword/semantic search в !!db_v8C.md
- v8C.3 RAG: RAPTOR-дерево с иерархическим ретривалом
- **Режим or:** P2P предложит выбор стратегии

---

## ШАБЛОНЫ ПРОМПТОВ RAG

### Промпт для RAPTOR-суммаризации кластера:
```
Ты суммаризатор узла RAPTOR. Получен кластер документов.
MUST: Создать связную суммаризацию сохраняя ключевые факты и термины.
MUST: Длина суммаризации — 1/5 от суммарной длины чанков.
MUST NOT: Добавлять выводы которых нет в документах.
MUST NOT: Использовать bullet points — только prose.
```

### Промпт для финального RAG ответа:
```
Контекст (RAPTOR retrieval, уровень {LEVEL}):
{RETRIEVED_CONTEXT}

Запрос: {QUERY}
MUST: Использовать только информацию из контекста.
MUST: Указать уровень абстракции источника (detail/summary/overview).
MUST NOT: Hallucinate факты вне контекста.
```

---

<!-- SOURCE_META: type=on-demand | module=rag | priority=P1 | v8c3=true | menu_item=35 | token_estimate=2800 -->


========================================
VERSION_METADATA
========================================
id: RAG_MODULE_V8C3
version: v8C.3
type: on-demand
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
techniques: [RAPTOR, LongRAG, adRAP, Dynamic_RAPTOR]
menu_item: 35
conflict_with_v8C2: none
========================================
