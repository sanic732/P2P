---
id: compression_module_v8N
version: 8.4.6-N
type: on-demand
module_type: on-demand
triggers: "compress|сжат|llmlingua|gist token|токен бюджет|context window full|контекст переполнен|длинный контекст|constrained output|JSON schema|grammar"
depends_on: "!!core_v8N.md, !!db_v8N.md, !pipeline.md"
token_estimate: ~2400
scope: Сжатие контекста — LLMLingua, Gist Tokens, Verbatim Deletion, Selective Summarization + constrained generation. Загружается по триггеру или MODULE_COMPRESSION=true.
compatible_with: "all v8N files"
tags: compression, llmlingua, gist-tokens, context, constrained-decoding, on-demand, v8n3
conflict_with: CAPSULE (or mode, minor)
menu_item: 29
---

// ═══════════════════════════════════════════════════════
// P2P — COMPRESSION MODULE (!compression.md)
// Загружен: добавлен пункт [29] в меню.
// ═══════════════════════════════════════════════════════

// ─── HOST-ADAPTIVE NOTE ───
// Gist использует CAPSULE (!memory.md) как gist-аналог — работает на всех хостах.
// CONSTRAINED DECODING caveat (КАРТА §): техники грамматик/JSON-schema требуют доступа к logits.
//   Для API-хостов БЕЗ доступа к logits → применять prompt-side: строгая инструкция формата
//   + цикл валидации (сгенерировать → проверить схему → переспросить при невалидности).
// MUTEX: выбрать ОДИН constrained-decoding подход за раз (не комбинировать грамматики).
//        При одновременном RAG/CAPSULE — один компрессор состояния.

# ТЕХНИКИ СЖАТИЯ (интегрированные)

## LLMLingua — сжатие промптов через perplexity
Источник: Microsoft Research 2023/2024. Удаление высокоперплекситных (избыточных) токенов; до 5-20x при потере <5%.
```
[LLMLINGUA]  target_ratio: 0.5   method: perplexity
  1. Определить опорные предложения (факты, числа, имена)
  2. Удалить избыточные союзы/вводные/повторы
  3. Примеры → ссылки ("как выше")   4. Шаблонные фразы → краткие
Когда: контекст > 80% лимита модели (лимит зависит от HOST_MODEL — см. live_core CONTEXT_STRATEGY).
```

## Gist Tokens — семантическое сжатие (без fine-tuning)
Источник: arXiv 2304.08467 (Mu et al., Stanford 2024).
```
[GIST_COMPRESSION]  заменить повторяющийся блок инструкций → ссылку на CAPSULE
  Формат: [REF:CAPSULE_ID] вместо полного блока (100+ токенов → ~5)
Когда: одинаковые блоки инструкций повторяются в нескольких запросах.
```

## Context Compaction — Verbatim Deletion
```
[CONTEXT_COMPACT]
  Удалять: полные повторы ответов, служебные ("Понял, приступаю"), обработанные примеры, черновики.
  Сохранять: PROJECT_CARD, ATLAS, последний exchange, критические constraints.
  trigger: контекст > 70% лимита → предложить compaction.
```

## Selective Summarization (иерархическая)
```
[SELECTIVE_SUMMARY]
  L1 verbatim:  последние 2 exchange + PROJECT_CARD + ATLAS
  L2 condensed: решения сессии (1-2 предложения)
  L3 reference: "ранее определили X, Y, Z"
  L4 deleted:   промежуточные шаги/черновики
  При нехватке: L4 → L3 → L2.
```

## Constrained Generation (grammar / JSON schema) — host-gated
```
[CONSTRAINED_GEN]  (один подход за раз — MUTEX)
  Хосты с нативной schema: gpt (response_format json_object) | gemini (output_schema) | glm (temp=0 JSON)
  Хосты БЕЗ logit-доступа: prompt-side — "MUST: вывод строго по схеме {schema}" + валидация-петля.
```

# COMPRESSION ROUTER
```
ctx < 60%   → нет action
ctx 60-80%  → Selective Summary (L4)
ctx 80-90%  → Verbatim Deletion + LLMLingua на старых exchanges
ctx > 90%   → CAPSULE сохранить + новая сессия (см. !memory CAPSULE_TARGET)
```

# CONFLICT_RESOLVER DECLARATIONS
- vs CAPSULE (!memory.md): сжать сейчас (compression) vs сохранить-и-загрузить (CAPSULE).
  При `or`: P2P спросит — сжать контекст или сохранить CAPSULE.
- MUTEX: один компрессор за раз (LLMLingua ИЛИ CAPSULE-gist), один constrained-decoding подход.

# CONTEXT ENGINEERING (Anthropic framing)
Сдвиг: не «формулировка промпта», а «курирование набора токенов» (system prompt, tools, примеры, история, память).
Приёмы (сшивка с модулями v8N):
  • compaction    → LLMLingua / Selective Summary (выше)
  • note-taking   → !memory / CAPSULE
  • JIT retrieval → !rag adaptive retrieval
  • labeled sections <background>/<instructions> → CONTEXT_CACHE_ANCHOR (!!db_v8N)
Экономика: prompt caching — до 90% cost / 85% latency (Anthropic); OpenAI 50% на cached input.
Предостережение: агрессивный compaction выбрасывает критичный нюанс — держать якорь ключевых фактов.

FILE_META:
  TECHNIQUES:  LLMLingua, Gist_Tokens, Verbatim_Deletion, Selective_Summarization, Constrained_Gen, Context_Engineering
  MENU_ITEM:   29
  COMPATIBLE:  !!core_v8N.md | !!db_v8N.md | !pipeline.md | !memory.md
