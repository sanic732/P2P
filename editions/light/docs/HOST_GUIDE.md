# P2P v8L.3 — Руководство по хостам

v8L.3 универсальна (как 8N.3), но добавляет важное измерение: **fetch-способность хоста**,
от которой зависит LOAD_MODE (доступен ли удалённый арсенал).

---

## Быстрая таблица

| HOST_MODEL | Синтаксис | Thinking API | Fetch (LOAD_MODE) | Ограничения |
|------------|-----------|--------------|-------------------|-------------|
| claude | XML теги | effort: medium | ✅ WebFetch → LAZY | G6, G7, G8 |
| gemini | Plain text | thinkingLevel: MEDIUM | ✅ Google Search → LAZY | G1, G2, G4, G11-G13 |
| gpt | JSON/Plain | reasoning_effort: medium | ✅ browsing → LAZY (если вкл.) | G9, G10 |
| grok | Plain text | reasoning: on | ✅ X/web → LAZY | G3, G14 |
| deepseek | Plain text | native (temp=0.3) | ⚠ обычно нет → LITE_ONLY | G15, G16 |
| qwen | Plain text | thinking_budget: 10000 | ⚠ зависит → авто-детект | G17, G18 |
| kimi | Plain text | thinking: on | ✅ Agent/web → LAZY | G20, Type G/I |
| glm | ## sections | thinking: on | ⚠ зависит → авто-детект | G19 |

> Реальный режим всё равно ставит **FETCH_CAPABILITY_GATE** (БЛОК 0 preloader) по факту
> наличия инструмента. Таблица — лишь ожидание.

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
`HOST_MODEL: "claude"` — XML-native, нативные sub-agents (AGENT_PATH=LOCAL), WebFetch.
```python
thinking={"type":"enabled","effort":"medium"}   # НЕТ temperature (G7), НЕТ budget_tokens
```
Ловушки: G6 (Opus 4.7 inflation → ~160K eff.), G7, G8 (MRCR >500K → пин opus-4-6).

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
`HOST_MODEL: "deepseek"` — нативный reasoning; **обычно LITE_ONLY** (нет browsing).
```python
model="deepseek-v4-pro"   # НЕ deepseek-chat (G16, retire 2026-07-24); temp=0.3
# multi-turn: re-inject reasoning_content, НЕ null (G15)
```
> В LITE_ONLY: арсенал недоступен, но базовые техники + дедлайны (LITE_SNAPSHOT) работают.

## Qwen
`HOST_MODEL: "qwen"` — thinking_budget; provider-prefix (G17), preserve_thinking (G18).

## Kimi
`HOST_MODEL: "kimi"` — Agent Swarm; thinking off для T0-1 (Type I); checkpoint (Type G); >40 → async (G20).

## GLM
`HOST_MODEL: "glm"` — ## sections, ≤100K (G19), temperature=0 для JSON.

---

## CROSS_MODEL_GENERATION_AWARENESS

> Синтаксис промпта для ХОСТА ≠ синтаксис промпта для ЦЕЛИ.

Генерируемые промпты адаптируются под `TARGET_MODEL` (P1/P7, Translation Layer §9),
независимо от хоста. Команда: `/p2p-translate [target_model]`.

| Host | Target | Что делает Translation Layer |
|------|--------|------------------------------|
| claude | gemini | убрать XML, добавить ## (G2) |
| gemini | claude | добавить XML теги |
| any | glm | ZERO XML, ## sections, ≤100K |
