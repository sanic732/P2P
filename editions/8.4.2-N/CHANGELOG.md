# P2P v8N.3 — CHANGELOG

**Build:** v8N.3 (Universal / Normal Edition) · **Date:** 2026-06-27 · **Base:** v8N.1
**Тип:** ADDITIVE (append-only) — импорт техник из v8C.3 + нативный live-specs 2026-06-12.
**Обратная совместимость:** полная. Новые модули по умолчанию OFF (`VERSION_COMPAT.v3=off`).

---

## [FIXED · 2026-07-06] Меню не отражало загрузку модулей + нативный автодетект хоста
**Решение:** отказались от эксперимента base/extended-сплита (8.4.1-N) — экономию токенов даёт само
приложение подмножества файлов, а не физический сплит. Логика гейта вшита СТАТИЧНО в ядро (всегда в памяти).

- **Меню-гейт (static, `!!core_v8N.md §4`):** добавлены `EXTENSIONS_SCAN` + `AVAILABILITY` +
  `MENU_RENDER_ALGORITHM`. Пункты [26-31] печатаются как рабочие ТОЛЬКО если тело их файла-модуля
  реально в контексте (детект по заголовку «… MODULE (!x.md)» + frontmatter `id`/`menu_item`; упоминания
  в base-файлах не считаются). Не загружен → 🔒-футер. Флаг `MODULE_*=true` без файла → остаётся LOCKED.
- **Фикс бага нумерации:** дублировавшийся пункт «26» (`/p2p-download` и RAG) устранён; `/p2p-download`
  вынесен в слэш-команды, модули заняли чистые [26-31] c тегами `[MODULE: !x.md]`.
- **Хост (`_preloader.md`):** нативный `HOST_MODEL_AUTODETECT` (SELF_IDENTIFY + CONFIDENCE_GATE,
  `HOST_MODEL=""` по умолчанию, порт из 8N/8H) + `HOST_PICK_LIST [1..8]` (ручной выбор, когда автодетект
  не сработал — частый случай Qwen; порт из 8L). `ON_LOAD`: хост определяется/выбирается ПЕРЕД меню.
- **Якоря (`_index.md` EXTENSIONS_ANCHOR):** триггеры-меню ⇄ core §4 EXTENSIONS_SCAN ⇄ модули (единый источник).

## [ADDED] 6 ON-DEMAND модулей (импорт техник из v8C.3, универсализированы под 8 хостов)

| Файл | Меню | Техники | Источник-донор |
|------|------|---------|----------------|
| `!rag.md` | [26] | RAPTOR, LongRAG, adRAP/Dynamic RAPTOR | v8C.3 `!rag.md` |
| `!reasoning.md` | [27] | s1 Budget Forcing, Self-Consistency, MCTS/rStar-Math, CCP | v8C.3 `!reasoning.md` |
| `!routing.md` | [28] | Semantic Router, Cascade, Cost-Aware, LLM-Router | v8C.3 `!routing.md` |
| `!compression.md` | [29] | LLMLingua, Gist Tokens, Verbatim Deletion, Constrained Gen | v8C.3 `!compression.md` |
| `!security.md` | [30] | Injection Scanner, Jailbreak Classifier, Hardening, SelfCheck | v8C.3 `!security.md` |
| `!optimization.md` | [31] | APO, OPRO, EvoPrompt, QUORUM-refinement | v8C.3 `!optimization.md` |

**Универсализация 8C→8N (применена к каждому модулю):**
- Frontmatter: `version: v8N.3`, убран `edition: CLAUDE_NATIVE`, `depends_on` → файлы v8N.
- XML host-gated через существующие `P7 HOST_SYNTAX_ISOLATION` + `§11 CROSS_MODEL_SYNTAX_FILTER`
  (Gemini → ZERO-XML, G2).
- Model strings приведены к набору 8N (8 хостов) + добавлены Fable 5 / Opus 4.8.
- `budget_tokens` удалён (CLAUDE.md rule 4) — только effort/thinkingLevel/thinking_budget по хосту.
- Logit-access caveat для constrained decoding (`!compression`): prompt-side + валидация-петля.

## [ADDED] VERSION_COMPAT в `_preloader.md`
- Нейтральные флаги `legacy/v3` (не `v8C2/v8C3` — ARCHITECTURE_DIFF §7) + 6 `MODULE_*` (по умолчанию `false`).
- `CONFLICT_RESOLVER v1.0` + MUTEX-таблица; load-step для `MODULE_*=true|or` с учётом mutex.
- 6 ON-DEMAND-триггеров добавлены в `ON_DEMAND_TRIGGERS`.

## [ADDED] Динамическое меню [26-31] в `!!core_v8N.md`
- Пункты видны только если соответствующий модуль загружен (`MENU_DISPLAY_RULE`).
- Quick-commands `/p2p-rag … /p2p-optimize`.
- ⚠ Отступление от буквы ТЗ: ТЗ указывал [35-40] (как в 8C.3, где меню до [34]); меню 8N — 25 пунктов,
  поэтому выбраны [26-31] (естественное продолжение, без дыр). Решение согласовано.

## [ADDED] Расширения консолидированных модулей (append-only, блоки `## [v8N.3] …`)
- `!memory.md` — Advanced Memory (Mem0, Letta/MemGPT, MemoryOS, NextMem, SuperLocalMemory) [КАРТА §3.1]
- `!agents.md` — Advanced Agents (Branch-Solve-Merge, LangGraph, Graphiti, Magentic-One ledgers) [§3.2]
- `!metrics.md` — Hallucination/Quality eval (LLM-as-Judge, FG-PRM, SelfCheck-Eval) [§3.3]
- `!toolkit.md` — Activation/Inference debug (GeoSteer, I2CL, CogniLoad), prompt-side only [§3.4; в 8N → toolkit, не debug]

## [ADDED] Нативный live-specs 2026-06-12 (v8.4)
- `_live/live_specs_20260617.md` импортирован как OVERRIDE; `live_specs_20260519.md` удалён.
- **Claude Fable 5** (GA 2026-06-10, `claude-fable-5`, $10/$50, Arena #1 Agent/Text/WebDev) →
  tier1, live_core (pricing/ELO/routing), live_vendors, !!db_v8N.
- **Opus 4.8** (`claude-opus-4-8`, GraphWalks F1 68.1%) → tier1, routing.
- Известные баги v8.4 → `live_vendors §2b`: Fable 5 Safety Nanny (~5%→Opus 4.8), Claude cache TTL 1h→5min,
  Gemini Error 13, GLM-5.1 Compact Hang, OpenAI Billing/Memory bugs. MRCR-регрессия: пин Opus 4.6 для >500K.

## [META] Версии и дедлайны
- Бамп `v8N.1 → v8N.3` во всех операционных файлах (frontmatter + VERSION_METADATA + MANIFEST).
- Дедлайны: Claude dated legacy aliases (06-15) и gpt-5.x legacy (06-05) — PASSED, литералы удалены
  из операционных файлов (CLAUDE.md rule 5). `deepseek-chat/reasoner` (07-24) — активны, оставлены как ретайр-нотисы.
- Исключения grep-чистки (документированы): `_live/live_specs_20260617.md` (verbatim дата-снапшот) и
  `docs/MIGRATION_С_v7N1.md` (исторический документ).

---

## Тесты (3 кейса на модуль: simple / medium / adversarial)

Для промпт-системы «тест» = задокументированный сценарий запуска + ожидаемое поведение.

| Модуль | simple | medium | adversarial |
|--------|--------|--------|-------------|
| !rag | «найди в документах X» → триггер [26], Naive RAG (<20 docs) | «база 100 doc, общий вопрос» → RAPTOR L2 | XML-промпт на Gemini → ZERO-XML вариант (G2) |
| !reasoning | «посчитай 2+2» → Direct (нет overhead) | «спорная задача T3» → Self-Consistency N=5 | THINKING:ON + reasoning → MUTEX: один контроллер бюджета |
| !routing | «какую модель для кода?» → claude-opus-4-8 | «бюджет $0.01, текст» → deepseek-v4-flash | проектная задача → передать в !scope (не дублировать Cascade) |
| !compression | «сожми этот текст» → LLMLingua 0.5 | «контекст 85%» → Verbatim+LLMLingua | JSON-schema на хосте без logits → prompt-side + валидация |
| !security | «проверь промпт» → Security Audit | «инъекция в user input» → INJECTION_SCANNER alert | GUARDIAN:OFF при активном !security → MUTEX форс GUARDIAN:ON |
| !optimization | «улучши промпт» → APO baseline | «оптимизируй до score 0.9» → OPRO 5 iter | нет !metrics → refuse (не оптимизировать вслепую) |

Ожидание для каждого: корректный триггер, host-адаптация (Gemini=ZERO-XML), срабатывание mutex.
