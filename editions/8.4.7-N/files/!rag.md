---
id: rag_module_v8N
version: 8.4.7-N
type: on-demand
module_type: on-demand
triggers: "rag|raptor|retrieval|ретривал|вектор|поиск по базе|векторная БД|document search|база знаний|документы"
depends_on: "!!core_v8N.md, !!db_v8N.md, !memory.md, !agents.md"
token_estimate: ~2800
scope: RAG техники — RAPTOR, векторный поиск, адаптивный ретривал. Загружается по триггеру или MODULE_RAG=true.
compatible_with: "all v8N files"
tags: rag, raptor, retrieval, vectors, on-demand, v8n3
conflict_with: "!memory CAPSULE + LLMLingua (один компрессор)"
menu_item: 26
---

// ═══════════════════════════════════════════════════════
// P2P — RAG MODULE (!rag.md)
// Загружен: добавлен пункт [26] в меню.
// ═══════════════════════════════════════════════════════

// ─── HOST-ADAPTIVE NOTE ───
// Этот модуль аддитивный — не конфликтует с базовой логикой v8N.
// Целевые модели для RAG выбираются по контексту (см. !routing.md / live_core).
// MUTEX: при одновременном !memory CAPSULE + сжатии — один компрессор (см. !compression.md).

# ТЕХНИКИ RAG (интегрированные)

## RAPTOR — Recursive Abstractive Processing for Tree-Organized Retrieval
Источник: arXiv 2401.18059 (Sarthi et al., Stanford NLP 2024).
Иерархическое дерево документов: рекурсивная кластеризация и суммаризация чанков на нескольких уровнях.
Когда: большие корпусы (>50 документов), нужны и детальные, и общие ответы.
```
[RAPTOR-RAG]
  1. Разбить документы на чанки (512-1024 токенов)
  2. Кластеризовать похожие чанки (UMAP + GMM)
  3. Суммаризовать кластер → узел дерева L1
  4. Повторить L1→L2, L2→L3
  5. При запросе — извлечь с нужного уровня (collapsed tree или traversal)
  6. Подать в контекст с метаданными уровня
```

## LongRAG — Long-Context RAG
Источник: arXiv 2410.18050. Большие retrieval units (документ/секция) вместо мелких чанков — меньше шума.
Когда: модели с >200K контекстом, документы с высокой взаимосвязанностью.
```
[LONGRAG]
  target_model: claude-opus-4-8 (200K) / gemini-3.1-pro-latest (1M) / grok-4.3 (2M)
  retrieval_unit: "full document" или "major section" (не чанки)
  top_k: 3-5
```

## adRAP / Dynamic RAPTOR
Источник: arXiv 2410.01736. Адаптивный выбор уровня по типу запроса.
```
[DYNAMIC-RAPTOR]
  factual/specific → level 0 (raw chunks)
  thematic/summary → level 1-2
  abstract/overview → level 2-3
```

> Для контекст-зависимых ответов — Context-Grounding CoT (!reasoning.md): извлекать правила из чанков ДО генерации.

# RAG ROUTING (интеграция с !routing.md)
```
IF corpus < 20 docs AND < 50K tokens → Naive RAG (прямая загрузка)  → модель с большим ctx
IF corpus 20-500 docs               → RAPTOR (дерево)               → claude-opus-4-8 / gemini-3.1-pro-latest
IF corpus > 500 docs OR semantic    → Vector DB + RAPTOR
IF high interconnectedness          → LongRAG (большие units)
```

# CONFLICT_RESOLVER DECLARATIONS
Аддитивный модуль. При пересечении с [16] DATOS Deep Search / поиском в !!db_v8N:
- база v8N: keyword/semantic search
- RAG: RAPTOR-дерево с иерархическим ретривалом
- режим `or`: P2P предложит выбор стратегии.
MUTEX: RAG + !memory CAPSULE + LLMLingua → один компрессор (не сжимать дважды).

# ШАБЛОНЫ ПРОМПТОВ RAG
```
[RAPTOR-суммаризация кластера]
  MUST: связная суммаризация, сохранить ключевые факты/термины; длина ≈ 1/5 суммы чанков.
  MUST NOT: добавлять выводы которых нет в документах; bullet points (только prose).

[Финальный RAG-ответ]
  Контекст (RAPTOR уровень {LEVEL}): {RETRIEVED_CONTEXT}   Запрос: {QUERY}
  MUST: использовать только контекст; указать уровень абстракции (detail/summary/overview).
  MUST NOT: hallucinate факты вне контекста.
```

FILE_META:
  TECHNIQUES:  RAPTOR, LongRAG, adRAP, Dynamic_RAPTOR
  MENU_ITEM:   26
  COMPATIBLE:  !!core_v8N.md | !!db_v8N.md | !memory.md | !routing.md
