# P2P v8C.2 — Claude-Specific Возможности

---

## Почему Claude Edition лучше generic промптов

Claude 4.x имеет уникальные характеристики которые P2P v8C.2 использует на 100%:

1. **XML понимание** — `<role>`, `<rules>`, `<task>` улучшают следование инструкциям
2. **Extended Thinking** — нативная поддержка через effort levels
3. **200K контекст** — достаточно для большинства задач без chunking
4. **Литеральное исполнение** — каждое MUST исполняется буквально (сила + ответственность)
5. **Отличный tool calling** — надёжный structured output через XML/JSON

---

## XML-Native Структура

P2P v8C.2 использует нативный XML формат Claude:

```xml
<role>
[Роль агента]
</role>

<context>
[Контекст задачи]
</context>

<rules>
MUST:
- [правило 1]
MUST NOT:
- [ограничение 1]
</rules>

<task>
[Задача]
</task>

<output_format>
[Формат]
</output_format>
```

**Почему XML а не plain text:**
- Claude 4.x обученн на XML структурах — лучше следует hierarchical instructions
- XML теги = явные boundaries между секциями
- Меньше ambiguity = меньше Type A anti-pattern

**Важно:** XML работает ТОЛЬКО для Claude. Для Gemini — G2 (CoH interference). Translation Layer убирает XML при адаптации под Gemini.

---

## Extended Thinking — Полное руководство

### API (v8C.1 актуальный)

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-7",       # или claude-sonnet-4-6
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "effort": "medium"          # "low" | "medium" | "high"
    },
    # НЕТ temperature — G7 → HTTP 400
    # НЕТ budget_tokens — удалён из API
    messages=[{"role": "user", "content": your_prompt}]
)

# Получить thinking:
for block in response.content:
    if block.type == "thinking":
        print("Thinking:", block.thinking)
    elif block.type == "text":
        print("Answer:", block.text)
```

### Когда включать Extended Thinking

Используй DEEP_THINK_VALUE_GATE (2 из 3 условий):

```
Q1: Задача требует многошагового рассуждения / научного анализа?
Q2: Контекст > 50K токенов или очень плотная информация?
Q3: Высокие ставки (production, публичный релиз, необратимые действия)?

0-1 из 3 → disabled (default)
2 из 3   → effort: "medium"
3 из 3   → effort: "high"
```

### Effort levels

| Effort | Когда | Стоимость | Время |
|--------|-------|-----------|-------|
| `"low"` | Факт-чек, классификация, T1-2 | Минимум | Быстро |
| `"medium"` | Стандарт, T2-3 analysis | Умеренная | Средне |
| `"high"` | T4, critical architecture, complex math | Высокая | Медленно |

---

## Claude Контекстная Стратегия

```
< 100K токенов  → Claude Opus 4.7 (без рисков)
100K-160K       → Claude Opus 4.7 (G6 inflation, планируй ~160K effective)
160K-200K       → Claude Sonnet 4.6 (нет G6, те же 200K контекст)
> 200K          → Gemini 3.1 Pro (1M) или Grok 4.3 (2M)
> 500K с recall → Claude Opus 4.6 pinned (G8 protection — 78.3% recall vs 32.2%)
```

---

## Claude Opus 4.6 — Когда Пинить

**НЕ обновляй Opus 4.6 → 4.7 для:**

```python
# Long-context recall задачи (>500K):
model = "claude-opus-4-6"    # MRCR 78.3% at 1M
# vs claude-opus-4-7:        # MRCR 32.2% at 1M (G8 regression)

# Cost-sensitive pipelines:
model = "claude-opus-4-6"    # Нет G6 tokenizer inflation
# vs claude-opus-4-7:        # +10-35% token inflation (G6)

# Bedrock/Vertex deployments:
model = "claude-opus-4-6"    # Alias там ещё не переключён на 4.7
```

---

## Context Caching (экономия 70-90%)

```python
# System prompt кэшируется если > 1024 токенов
system=[{
    "type": "text",
    "text": p2p_system_prompt,
    "cache_control": {"type": "ephemeral"}  # TTL: 5 минут
}]

# Повторные запросы с тем же system → читают из кэша
# Экономия: ~90% стоимости system prompt
```

**Минимум для кэша:**
- Opus/Sonnet: 1024 токенов
- Haiku: 2048 токенов

---

## DEADLINE Alert

```
2026-06-15: ОБЯЗАТЕЛЬНО обновить:
  claude-opus-4-20250514   → claude-opus-4-7
  claude-sonnet-4-20250514 → claude-sonnet-4-6

Проверь:
  grep -r "4-20250514" .
```
