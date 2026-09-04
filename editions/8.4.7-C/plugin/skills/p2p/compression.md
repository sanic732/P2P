---
source_id: COMPRESSION_MODULE_V8C3
version: 8.4.7-C
module_type: on-demand
triggers: "compress|сжат|llmlingua|gist token|токен бюджет|context window full|контекст переполнен|длинный контекст|KV-cache"
depends_on: core.md
token_estimate: ~2400
scope: Сжатие контекста для P2P — LLMLingua, Gist Tokens, Verbatim Deletion, Selective Summarization, Context Engineering. Загружается по триггеру или MODULE_COMPRESSION=true.
tags: compression, llmlingua, gist-tokens, context, kv-cache, on-demand, v8c3
conflict_with_v8C2: CAPSULE (or mode, minor)
---

# P2P — COMPRESSION MODULE (compression.md)

> Загружен: добавлен пункт [38] в меню.

---

## ТЕХНИКИ СЖАТИЯ (интегрированные)

### LLMLingua — Сжатие промптов через perplexity
**Источник:** Microsoft Research 2023/2024  
**Суть:** Удаление токенов с высокой perplexity (избыточных) при сохранении смысла. Коэффициент сжатия до 5-20x при потере качества <5%.

**Применение в P2P:**
```
[LLMLINGUA]
target_ratio: 0.5    # оставить 50% токенов
method: perplexity   # удалять высокоперплекситные токены

Алгоритм (эмуляция в промпте):
1. Определить "опорные" предложения (ключевые факты, числа, имена)
2. Удалить избыточные союзы, вводные фразы, повторы
3. Заменить примеры → ссылки ("например, как выше")
4. Сжать шаблонные фразы ("пожалуйста, убедитесь что" → "обязательно")

Применять когда: контекст > 80% лимита модели
```

---

### Gist Tokens — Семантическое сжатие
**Источник:** arXiv 2304.08467 (Mu et al., Stanford NLP 2024)  
**Суть:** Обучить модель представлять длинные инструкции одним "gist token" — специальным маркером. Адаптация для P2P (без fine-tuning): использовать CAPSULE как gist-аналог.

**Применение в P2P (без fine-tuning):**
```
[GIST_COMPRESSION]
Принцип: заменить повторяющийся блок инструкций → ссылку на CAPSULE
Формат: [REF:CAPSULE_ID] вместо полного блока (100+ токенов → 5 токенов)

Когда использовать: одинаковые блоки инструкций повторяются в нескольких запросах
```

---

### Context Compaction — Verbatim Deletion
**Источник:** Anthropic best practices + arXiv (Context Compaction)  
**Суть:** Удалить дословные повторы → заменить суммаризацией или ссылкой.

**Применение в P2P:**
```
[CONTEXT_COMPACT]
Что удалять:
  - Полные повторы предыдущих ответов
  - Служебные сообщения ("Понял, приступаю...")
  - Примеры которые уже обработаны
  - Промежуточные черновики (оставить только финал)

Что сохранять:
  - PROJECT_CARD
  - ATLAS (текущее состояние задачи)
  - Последний exchange (user + assistant)
  - Критические constraints

triggers: контекст > 70% лимита → предложить compaction
```

---

### Selective Summarization (иерархическая)
```
[SELECTIVE_SUMMARY]
Уровни сохранения:
  L1 (verbatim):  последние 2 exchange + PROJECT_CARD + ATLAS
  L2 (condensed): решения из session (1-2 предложения каждое)
  L3 (reference): "ранее мы определили X, Y, Z"
  L4 (deleted):   все промежуточные шаги и черновики

При нехватке контекста: L4 → L3 → L2 (в таком порядке)
```

---

## COMPRESSION ROUTER

```
IF ctx_usage < 60%:   → нет action
IF ctx_usage 60-80%:  → предложить Selective Summary (L4)
IF ctx_usage 80-90%:  → Verbatim Deletion + LLMLingua на старых exchanges
        └ ЕСЛИ ENV=Code AND model∈readers AND есть narrative-блок ≥8000 и НЕ byte-exact:
IF ctx_usage > 90%:   → CAPSULE сохранить + новая сессия (CAPSULE_TARGET)
                        └ крупный state → CAPSULE optical-backend (memory_bridge.md)
```

---

## CONFLICT_RESOLVER DECLARATIONS

**Конфликт:** `COMPRESSION` + `CAPSULE` (v8C.2 memory_bridge.md)

| | v8C.2 CAPSULE | v8C.3 Compression |
|--|---------------|-------------------|
| Подход | Сохранить всё в CAPSULE → загрузить потом | Сжать контекст прямо сейчас |
| Когда | Контекст заполнен, нужна пауза | Контекст заполнен, продолжаем работу |
| Результат | Полная история восстановима | Продолжение без разрыва |

При `v8C3=or`: P2P спросит — сжать контекст (v8C.3) или сохранить CAPSULE (v8C.3)?

**Disambiguation (НЕ смешивать — три разные оси сжатия):**

| Техника | Ось | Обратимость | Когда |
|---------|-----|-------------|-------|
| LLMLingua | token-space (удаляет токены) | lossy, необратимо | текст остаётся текстом |
| Gist | learned marker → ссылка | ссылочная | повтор одинаковых блоков |

≠ LLMLingua, ≠ Gist. См. `db.md` #DB_TECHNIQUE_COMBINATOR.

---

## CONTEXT ENGINEERING (Anthropic framing)
Сдвиг: не «формулировка промпта», а «курирование набора токенов» (system prompt, tools, примеры, история, память).
Приёмы (сшивка с модулями P2P):
  • compaction   → LLMLingua / selective summarization
  • note-taking  → memory_bridge / CAPSULE
  • JIT retrieval→ rag.md adaptive retrieval
  • labeled sections <background>/<instructions>/## Tool guidance → CONTEXT_CACHE_ANCHOR
Экономика: prompt caching — до 90% cost / 85% latency (Anthropic); OpenAI 50% на cached input.
Предостережение: агрессивный compaction выбрасывает критичный нюанс — держать якорь ключевых фактов.

---

<!-- SOURCE_META: type=on-demand | module=compression | priority=P2 | v8c3=true | menu_item=38 | token_estimate=2400 -->


========================================
FILE_META
========================================
id: COMPRESSION_MODULE_V8C3
type: on-demand
edition: CLAUDE_NATIVE
techniques: [LLMLingua, Gist_Tokens, Verbatim_Deletion, Selective_Summarization]
menu_item: 38
conflict_with_v8C2: CAPSULE_minor
========================================
