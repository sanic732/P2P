---
source_id: CMD_HOST_V8L
version: v8L.3-ALPHA
module_type: command
last_updated: 2026-06-18
scope: /host — show or switch the host LLM model (universal edition, like 8N.3).
---
# /host — Выбор/смена хост-модели LLM

**Что делает:** Показывает или меняет хост-модель, на которой запущен P2P v8L.3.
v8L.3 — УНИВЕРСАЛЬНАЯ редакция (как 8N.3): работает на любой из 8 моделей, не только Claude.

**Использование:**
```
/host              → показать текущий HOST_MODEL + LOAD_MODE + AGENT_PATH + XML_POLICY
/host claude       → переключить на Claude  (XML-native, native sub-agents, WebFetch)
/host gemini       → Gemini   (ZERO XML — G2, Google Search fetch, thinkingLevel)
/host gpt          → GPT      (JSON-pref, reasoning_effort, ≤7 правил — G9)
/host grok         → Grok     (Heavy-16 native, X firehose, safe-params — G14)
/host deepseek     → DeepSeek (native reasoning; обычно LITE_ONLY — нет fetch)
/host qwen         → Qwen     (thinking_budget; provider-prefix — G17)
/host kimi         → Kimi     (Agent Swarm; thinking on|off)
/host glm          → GLM      (≤100K — G19; ## segmentation)
```

**Алгоритм при смене:**
1. Записать новый HOST_MODEL в HOST_CONFIG (_preloader_v8L)
2. Перезагрузить HOST_PROFILE (!!core_v8L §1): XML_POLICY, thinking-синтаксис, G-ошибки, лимиты
3. Пересчитать ожидаемый fetch по SELECT_HOST_FETCH_MATRIX; FETCH_CAPABILITY_GATE подтвердит по факту
4. Выставить AGENT_PATH: claude/grok+plugin → LOCAL(.claude/agents); иначе → QUORUM из CORE_PLUS chunk
5. Вывести баннер: `[P2P v8L.3 | HOST: {model} | MODE: {LOAD_MODE} | Agents: {path}]`

**ПРИМ:** генерируемые промпты адаптируются под TARGET_MODEL (P1/P7, §9 Translation Layer),
а не под хост — кросс-модельная генерация сохраняется при любом хосте.


========================================
VERSION_METADATA
========================================
id: CMD_HOST_V8L
version: v8L.3-ALPHA
type: command
edition: UNIVERSAL
last_verified: 2026-06-18
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
