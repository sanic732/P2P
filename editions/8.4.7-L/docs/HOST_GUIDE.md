# P2P 8.4.7-L — Руководство по хостам

Редакция L универсальна (как N) и рассчитана на **хост с включённым веб-доступом** —
арсенал подтягивается из Gist по триггеру (`GIST_LAZY_FETCH` — единственный режим).

---

## Быстрая таблица

| HOST_MODEL | Синтаксис | Thinking API | Инструмент веб-доступа | Ограничения |
|------------|-----------|--------------|------------------------|-------------|
| claude | XML теги | `{"type":"adaptive"}` | WebFetch / web_search | G6, G7, G8 |
| gemini | Plain text | thinkingLevel: MEDIUM | Google Search / grounding | G1, G2, G4, G11-G13 |
| gpt | JSON/Plain | reasoning_effort: medium | browsing | G9, G10 |
| grok | Plain text | reasoning: none/low/medium/high | X / web | G3, G14 |
| deepseek | Plain text | native (temp=0.3) | провайдерский web-tool | G15, G16 |
| qwen | Plain text | thinking_budget: 10000 | провайдерский web-tool | G17, G18 |
| kimi | Plain text | thinking: on | Agent / web | G20, Type G/I |
| glm | ## sections | thinking: on | провайдерский web-tool | G19 |

> **⚠ Проверка обязательна.** Сразу после выбора хоста выполни **`/p2p-verify`** (пункт 35) —
> система реально дёрнет все Gist-URL и сверит sha256/EOF/размеры. Работать начинай только после
> успешного отчёта. Не прошло → включи в настройках хоста инструмент веб-доступа и повтори.
> Проверено на практике (2026-07-14): claude · gemini · gpt · grok · deepseek · qwen — fetch работает.

---

## Выбор и смена хоста

```
# на старте система спросит сама (HOST_MODEL пуст):
🌐 На какой LLM запускаешь? [1]claude … [8]glm

# сменить на лету:
/host gemini
/host            # показать текущий HOST + LOAD_MODE + AGENT_PATH
```

При смене хоста перезагружается HOST_PROFILE (§1 core): XML_POLICY, thinking-синтаксис,
G-ошибки, лимиты, ожидание fetch.

---

## Claude
`HOST_MODEL: "claude"` — XML-native, нативные sub-agents (AGENT_PATH=LOCAL), WebFetch. Контекст 1M.
```python
thinking={"type":"adaptive"}   # НЕТ temperature/top_p/top_k (G7), НЕТ budget_tokens (удалён)
```
Ловушки: G6 (общий токенизатор 4.7/4.8/Fable 5/Sonnet 5 → +30-42% на англ. прозе),
G7, G8 (MRCR >500K → пин `claude-opus-4-6`).

## Gemini
`HOST_MODEL: "gemini"` — ZERO XML (G2!), Google Search покрывает fetch.
```python
thinkingConfig={"thinkingLevel":"MEDIUM"}  # НЕ thinking_budget (G4); temperature 1.0 при Deep Think (G1)
```
Память: REINJECT каждые 25 (G13). QUORUM — из CORE_PLUS chunk (не нативные агенты).

## GPT
`HOST_MODEL: "gpt"` — JSON-pref, ≤7 пар MUST/MUST NOT (G9), <272K (G10).
```python
reasoning_effort="medium"; response_format={"type":"json_object"}
```

## Grok
`HOST_MODEL: "grok"` — Heavy-16 native, X firehose. Только safe-params (G14).
```python
# safe: temperature, max_tokens, stream, top_p, stop ; topic anchor /3 turn (G3)
```

## DeepSeek
`HOST_MODEL: "deepseek"` — нативный reasoning, контекст 1M (out 384K). Нужен провайдерский web-tool.
```python
model="deepseek-v4-pro"   # ⚠ deepseek-chat/reasoner → HTTP 404 c 2026-07-24 15:59 UTC (G16, no grace)
# multi-turn: re-inject reasoning_content, НЕ null (G15)
```

## Qwen
`HOST_MODEL: "qwen"` — thinking_budget; provider-prefix (G17: DashScope `qwen3.6-plus` / OpenRouter `qwen/qwen3.6-plus`),
preserve_thinking (G18). Контекст 1M.

## Kimi
`HOST_MODEL: "kimi"` — Agent Swarm (300); thinking off для T0-1 (Type I); checkpoint (Type G); >1h → async webhooks (G20).
Контекст 256K-1M.

## GLM
`HOST_MODEL: "glm"` — ## sections, temperature=0 для JSON.
`glm-5.2` — MIT, 1M (основной); `glm-5.1` — ≤~120K (G19 collapse), /compact hang → мигрировать на 5.2.

---

## CROSS_MODEL_GENERATION_AWARENESS

> Синтаксис промпта для ХОСТА ≠ синтаксис промпта для ЦЕЛИ.

Генерируемые промпты адаптируются под `TARGET_MODEL` (P1/P7, Translation Layer §9),
независимо от хоста. Команда: `/p2p-translate [target_model]`.

| Host | Target | Что делает Translation Layer |
|------|--------|------------------------------|
| claude | gemini | убрать XML, добавить ## (G2) |
| gemini | claude | добавить XML теги |
| any | glm | ZERO XML, ## sections (5.2 — 1M; 5.1 — ≤~120K) |
