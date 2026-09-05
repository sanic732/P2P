# P2P 8.4.7-N — Руководство по хостам

---

## 🌐 Определение хоста (v8.4.1 — авто + ручной выбор)

С 8.4.1 `HOST_MODEL` по умолчанию **пустой** (`""`) — вписывать вручную больше не обязательно:

1. **Автодетект** (`_preloader.md` БЛОК 0, `HOST_MODEL_AUTODETECT`): прелоадер через `SELF_IDENTIFY`
   определяет, на какой из **10 хостов** он запущен (claude · gemini · gpt · grok · deepseek · qwen ·
   kimi · glm · minimax · manus). Уверенно узнал → баннер «🌐 Хост определён: <model> (авто)».
2. **Ручной выбор, если не определилось** (`HOST_PICK_LIST`, БЛОК 4): при низкой уверенности
   показывается нумерованный список `[1..10]` — выбери число. _(Частый случай: **Qwen** почти
   никогда не самоопределяется — это нормально, просто выбери `[6] qwen`.)_ **Меню появляется
   только ПОСЛЕ выбора хоста.**
3. **Форс / смена:** вписать `HOST_MODEL: "grok"` в `_preloader.md` (автодетект пропускается) или
   команда `/host <модель>` в сессии.

> MiniMax/Manus: отдельного профиля в `!!core §1` пока нет → дефолт PLAIN_TEXT + adaptive XML +
> simulated QUORUM; лимиты/цены — из `_live/live_specs.md`.

Ниже — как вручную задать любой конкретный хост (необязательно, для форса).

---

## Быстрая таблица

| HOST_MODEL | Синтаксис | Thinking API | Ключевые ограничения |
|------------|-----------|--------------|---------------------|
| claude | XML теги | effort: medium | G6, G7, G8 |
| gemini | Plain text | thinkingLevel: MEDIUM | G1, G2, G4, G11-G13 |
| gpt | JSON/Plain | reasoning_effort: medium | G9, G10 |
| grok | Plain text | reasoning: on | G3, G14 |
| deepseek | Plain text | native (temp=0.3) | G15, G16 |
| qwen | Plain text | thinking_budget: 10000 | G17, G18 |
| kimi | Plain text | thinking: on | G20, Type G, Type I |
| glm | ## sections | thinking: on | G19 |

---

## Claude — HOST

Установи в _preloader.md: `HOST_MODEL: "claude"`

P2P в родном режиме. XML структура работает полностью.

```xml
<role>Ты — P2P 8.4.7-N на Claude.</role>
<rules>
MUST: [правило]
MUST NOT: [ограничение]
</rules>
<task>[задача]</task>
```

**Thinking API:**
```python
thinking={"type": "enabled", "effort": "medium"}
# НЕТ temperature (G7)
# НЕТ budget_tokens (удалён из API)
```

**Ловушки:** G6 (Opus 4.7 tokenizer inflation), G7 (temp+thinking), G8 (MRCR >500K).

---

## Gemini — HOST

Установи: `HOST_MODEL: "gemini"`

P2P адаптируется автоматически. Все XML теги заменяются на ## разделы.

```markdown
## Role
Ты — P2P 8.4.7-N на Gemini.

## Rules
MUST: [правило]
MUST NOT: [ограничение]

## Task
[задача]
```

**Thinking API:**
```python
thinkingConfig={"thinkingLevel": "MEDIUM"}  # НЕ thinking_budget (G4)
# temperature: 1.0 при Deep Think (G1)
```

**Критично:** ZERO XML в любых промптах (G2 — CoH interference).
**Память:** CONSTRAINT_REINJECTION каждые 25 сообщений (G13).

---

## GPT — HOST

Установи: `HOST_MODEL: "gpt"`

JSON предпочтителен. Минимум XML. Строгий лимит правил.

```python
reasoning_effort="medium"
response_format={"type": "json_object"}  # для JSON output
# MAX 7 MUST + 7 MUST NOT пар (G9)
```

**Ловушки:** G9 (>7 rule pairs → silent downgrade), G10 (>272K → pricing jump).

---

## Grok — HOST

Установи: `HOST_MODEL: "grok"`

Plain Markdown. Только safe параметры.

```python
# SAFE params только:
temperature=0.7
max_tokens=8096
stream=False
top_p=0.9
stop=None
# ЗАПРЕЩЕНО: top_k, repetition_penalty, presence_penalty (G14 → HTTP 400)
```

**Topic anchor каждые 3 хода (G3):**
```
[TOPIC ANCHOR: Исходная задача = {1 предложение}. Держись темы.]
```

---

## DeepSeek — HOST

Установи: `HOST_MODEL: "deepseek"`

Нативный reasoning. Не управляется извне.

```python
model="deepseek-v4-pro"      # или deepseek-v4-flash; контекст 1M, out 384K
temperature=0.3               # для reasoning
# Multi-turn: re-inject reasoning_content, НЕ null (G15 RESOLVED BY DESIGN)
# ⚠ G16: deepseek-chat/reasoner → HTTP 404 c 2026-07-24 15:59 UTC (no grace).
#    Алиасы уходят на V4-FLASH: chat→flash (non-thinking), reasoner→flash (thinking).
#    Это НЕ апгрейд на V4-Pro — на Pro переходить осознанно.
```

---

## Qwen — HOST

Установи: `HOST_MODEL: "qwen"`

thinking_budget вместо effort levels.

```python
thinking_budget=10000         # medium (0=off, 81920=max)
preserve_thinking=True        # для agentic задач (G18)
# DashScope: "qwen3.7-max" | "qwen3.6-plus" | OpenRouter: "qwen/qwen3.6-plus" (G17)
```

---

## Kimi — HOST

Установи: `HOST_MODEL: "kimi"`

Swarm specialist. Осторожно с thinking на простых задачах.

```python
thinking="on"      # T2+ задачи
thinking="off"     # T0-T1 (Type I prevention)
# >40 агентов → PARL async (G20)
```

**Checkpoint before writes (Type G prevention):**
```
Before making changes: list all planned changes. Await confirmation.
```

---

## GLM — HOST

Установи: `HOST_MODEL: "glm"`

MIT лицензия. ## секции.

```python
model="glm-5.2"             # основной: 1M контекст, WebDev #3
# model="glm-5.1"           # legacy: HARD LIMIT ~120K (G19 collapse); /compact hang → мигрировать на 5.2
temperature=0               # для JSON output
```

---

## CROSS_MODEL_GENERATION_AWARENESS

Важнейший принцип Normal Edition:

> Синтаксис промпта для ХОСТА ≠ синтаксис промпта для ЦЕЛИ.

| Host | Target | Что делать |
|------|--------|-----------|
| claude | gemini | Translation Layer: убрать XML, добавить ## |
| gemini | claude | Добавить XML теги в output |
| gpt | grok | Убрать нестандартные params в output |
| claude | glm | Translation Layer: ZERO XML, ## sections |

Команда: `/p2p-translate [target_model]`
