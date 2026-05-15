# P2P v8C.2 — Руководство по сборке

---

## Три уровня сборки

| Сборка | Токены | Файлов | Когда |
|--------|--------|--------|-------|
| MINIMAL | ~80K | 4 | Тест системы, T0-T2, строгий лимит |
| STANDARD | ~150K | 9 | Большинство задач, T2-T3 |
| FULL | ~300K | 20+ | T3-T4, QUORUM, длинные задачи |

---

## MINIMAL (~80K токенов)

```bash
cat _preloader.md \
    !!core_v8C.md \
    _live/MANIFEST.md \
    _live/live_core.md \
    > p2p_minimal.md
```

**Включает:** ENV detection, меню, базовые правила, дедлайны.  
**Не включает:** G-errors, Templates, QUORUM профили, Translation Layer.

---

## STANDARD (~150K токенов) — Рекомендуется

```bash
cat _preloader.md \
    !!core_v8C.md \
    !!db_v8C.md \
    _live/MANIFEST.md \
    _live/live_core.md \
    _live/live_claude.md \
    _live/live_vendors.md \
    !agents.md \
    !contract.md \
    > p2p_standard.md
```

**Включает:** Всё для T2-T3, G-errors, Templates A-M, QUORUM, Translation Layer.

---

## FULL (~300K токенов)

```bash
cat _preloader.md \
    !!core_v8C.md \
    !!db_v8C.md \
    _live/MANIFEST.md \
    _live/live_core.md \
    _live/live_claude.md \
    _live/live_vendors.md \
    !agents.md \
    !contract.md \
    !debug.md \
    !exploration.md \
    !memory.md \
    !metrics.md \
    !scope.md \
    !templates.md \
    !mentor.md \
    !tool_budget.md \
    !user_context.md \
    !domain.md \
    vendors/tier3.md \
    vendors/tier4.md \
    > p2p_full.md
```

---

## ПРАВИЛО PRIMACY/RECENCY

Claude лучше следует инструкциям в начале и конце промпта (LitM эффект).

**Обязательно:**
1. `_preloader.md` — ВСЕГДА первый
2. `!!core_v8C.md` — сразу после preloader
3. Критичные constraints из MANIFEST — в первых 20% промпта
4. `<task>` секция — в последних 10% промпта (primacy/recency boost)

---

## CONTEXT CACHING API

```python
import anthropic

client = anthropic.Anthropic()

with open("p2p_standard.md") as f:
    system_prompt = f.read()

# Первый запрос — создаёт кэш
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    system=[{
        "type": "text",
        "text": system_prompt,
        "cache_control": {"type": "ephemeral"}  # TTL: 5 минут
    }],
    messages=[{"role": "user", "content": "СТАРТ"}]
)

print(f"Cache write tokens: {response.usage.cache_creation_input_tokens}")

# Второй запрос — читает кэш (90% экономии)
response2 = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    system=[{
        "type": "text",
        "text": system_prompt,
        "cache_control": {"type": "ephemeral"}
    }],
    messages=[{"role": "user", "content": "Создай промпт для X"}]
)

print(f"Cache read tokens: {response2.usage.cache_read_input_tokens}")
```

**Экономия:** ~90% стоимости system prompt при повторных запросах.

---

## YAML FRONTMATTER — убирать или оставлять?

**Оставить если:**
- Используешь NotebookLM для RAG
- Нужна programmatic navigation
- Хочешь source_id трекинг

**Убрать если:**
- API с жёстким token лимитом
- System prompt только для Claude (не для RAG)

**Скрипт убирания YAML:**
```python
import re

def strip_yaml_frontmatter(text):
    return re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)

with open("p2p_standard.md") as f:
    content = strip_yaml_frontmatter(f.read())
    
# ~5-10% экономия токенов
```

---

## ZERO XML AUDIT (для Gemini)

Если адаптируешь v8C.1 под Gemini — обязательно убери XML:

```bash
# Проверить наличие XML тегов:
grep -n '<[a-z_]*>' p2p_standard.md | head -20

# Список тегов которые нужно убрать для Gemini:
# <role> <context> <rules> <task> <output_format>
# <exploration_rules> <tri_mode_detection> <sir_scanner>
# и другие XML теги
```

**Альтернатива:** Используй Translation Layer в !contract.md — он убирает XML автоматически при target=Gemini.

---

## ЧЕКЛИСТ ПЕРЕД ДЕПЛОЕМ

```
☐ API strings актуальные (не claude-*-4-20250514)
☐ budget_tokens удалён (заменён на effort)
☐ temperature отсутствует при thinking=enabled
☐ YAML frontmatter убран если нужно
☐ XML теги убраны если цель Gemini
☐ Тест на 3 кейсах: T1 / T2 / adversarial
☐ CHANGELOG обновлён
```
