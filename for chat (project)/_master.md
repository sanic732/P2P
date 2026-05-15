---
source_id: MASTER_V8C
version: v8C.2
module_type: meta
last_updated: 2026-05-14
scope: _master.md — assembly instructions for single-file API deployment (v8C.2). Not for direct use — follow assembly guide.
tags: master, assembly, api, single-file, deployment
---

# P2P v8C.2 — МАСТЕР СБОРКИ (_master.md)

> Этот файл описывает как собрать v8C.2 в единый промпт для API.
> Для детальных инструкций → docs/ASSEMBLY_GUIDE.md

---

## ЗАЧЕМ _master.md

При работе через API нельзя загружать файлы по одному.
_master.md описывает порядок конкатенации файлов в единый system prompt.

---

## СБОРКИ ПО РАЗМЕРУ

### MINIMAL (~80K токенов)
Файлы в порядке:
```
1. _preloader.md
2. !!core_v8C.md
3. _live/MANIFEST.md
4. _live/live_core.md
```

**Когда:** API со строгими context limits, T0-T2 задачи, тест системы.

### STANDARD (~150K токенов)
Файлы в порядке:
```
1. _preloader.md
2. !!core_v8C.md
3. !!db_v8C.md
4. _live/MANIFEST.md
5. _live/live_core.md
6. _live/live_claude.md
7. _live/live_vendors.md
8. !agents.md
9. !contract.md
```

**Когда:** Большинство production задач, T2-T3.

### FULL (~300K токенов)
Все выше + в порядке:
```
10. !debug.md
11. !exploration.md
12. !memory.md
13. !metrics.md
14. !scope.md
15. !templates.md
16. !mentor.md
17. !tool_budget.md
18. !user_context.md
19. !domain.md
20. vendors/tier3.md
21. vendors/tier4.md
```

**Когда:** T3-T4, QUORUM, длинные multi-step задачи.

---

## ПРАВИЛА СБОРКИ

**PRIMACY/RECENCY RULE:**
- _preloader.md → ВСЕГДА первый (устанавливает контекст)
- !!core_v8C.md → сразу после (активирует систему)
- Критичные инструкции из _live/ → в первых 20% и последних 20%

**XML INTEGRITY:**
- Не разбивать XML теги между файлами
- Проверь что `<role>` тег всегда закрыт в том же файле

**YAML FRONTMATTER:**
- В API промпте можно убрать YAML frontmatter для экономии токенов
- Оставь только если используешь NotebookLM / RAG indexing

---

## BASH СКРИПТ СБОРКИ

```bash
#!/bin/bash
# Сборка STANDARD build
OUTPUT="p2p_v8c1_standard.md"

cat _preloader.md \
    !!core_v8C.md \
    !!db_v8C.md \
    _live/MANIFEST.md \
    _live/live_core.md \
    _live/live_claude.md \
    _live/live_vendors.md \
    !agents.md \
    !contract.md \
    > "$OUTPUT"

echo "Built: $OUTPUT ($(wc -c < $OUTPUT) bytes)"
```

---

## CONTEXT CACHING (Anthropic)

При повторных запросах используй prompt caching:

```python
import anthropic

client = anthropic.Anthropic()

# Кэшируемая часть (BASE + LIVE — меняется редко)
with open("p2p_v8c1_standard.md") as f:
    system_prompt = f.read()

response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    system=[{
        "type": "text",
        "text": system_prompt,
        "cache_control": {"type": "ephemeral"}  # Кэш на 5 минут
    }],
    messages=[{"role": "user", "content": user_message}]
)
```

**Экономия:** 70-90% стоимости при повторных запросах с тем же system prompt.
**Минимум для кэша:** 1024 tokens (Opus/Sonnet).

<!-- SOURCE_META: type=meta | priority=2 | assembly=true | api-deployment=true | context-caching=true -->


========================================
VERSION_METADATA
========================================
id: MASTER_V8C
version: v8C.2
type: meta
edition: CLAUDE_NATIVE
last_verified: 2026-05-14
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
