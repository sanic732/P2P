# P2P v8N.3 — CHANGELOG

**Build:** v8N.3 (Universal / Normal Edition) · **Date:** 2026-06-27 · **Base:** v8N.1
**Тип:** ADDITIVE (append-only) — импорт техник из v8C.3 + нативный live-specs 2026-06-12.
**Обратная совместимость:** полная. Новые модули по умолчанию OFF (`VERSION_COMPAT.v3=off`).

---

## [8.4.6-N] — 2026-07-26

Изменения с версии 8.4.5-N.

### Fixed
- **🔴 Пункты меню [26-32] не открывались никогда.** Модули (`!rag.md`, `!reasoning.md`,
  `!routing.md`, `!compression.md`, `!security.md`, `!optimization.md`, `!skills.md`)
  оставались заблокированными при любых значениях флагов `MODULE_*` и при любом числе
  приложенных файлов. Детект сверял номер версии в заголовке файла-модуля с версией ядра,
  а они разошлись. Теперь модуль опознаётся по `id` и `menu_item` — **версия не сверяется**.
  Проверено: определяются все 7.
- **Подсказка в футере меню требовала приложить файл `!<module>.md`** — буквально, с угловыми
  скобками. Теперь подставляются настоящие имена файлов.
- В трёх местах значилось «все 6» и «[26-31]» при семи модулях — исправлено на «все 7» / «[26-32]».
- **Логотип при старте показывал `P2P v8N.4 - NORMAL EDITION`** — старый номер версии.
  Теперь `P2P 8.4.6-N — NORMAL EDITION`.
- **Правило миграции DeepSeek было перевёрнуто:** бывший `deepseek-reasoner` идёт на
  **v4-pro**, а не на v4-flash — иначе reasoning тихо деградирует.
- **Цена Grok на кэшированный ввод:** `$0.30` short / `$0.60` long вместо `$0.50`;
  добавлен порог 200K, после которого тариф удваивается **вместе с кэшем**.
- **Grok в EU:** доступ открыт 21.07; ограничение переформулировано с недоступности
  на персональные данные (размещение данных не гарантируется).
- Токенизатор: канон **~+30%** (одна официальная цифра вместо вилки) + Token Counting API.
- Правило удорожания на длинном контексте уточнено: ×2 на некэшированный ввод, ×1.5 на вывод,
  **кэшированный ввод не дорожает**. Длинный контекст Terra/Luna помечен как недокументированный.
- Цена GLM-5.2 помечена как неподтверждённая, а не подана как факт.
- Линейка DeepSeek V4 помечена как официально PREVIEW — но оставлена в маршрутизации:
  после снятия алиасов других путей нет.

### Added
- **`claude-opus-5` — основная модель** (1M/128K, $5/$25, thinking включён по умолчанию).
  Добавлены `gemini-3.6-flash`, `gemini-3.5-flash-lite`, `kimi-k3` (ACCESS-RISK, не основной),
  `qwen3.7-plus`, `qwen3.6-35b-a3b`.
- **Две новые записи в базе ошибок:** G21 (несовпадение заявленной и фактической модели) и
  G22 (агентная опасность GPT-5.6 Sol).
- **Правило structured output для Qwen:** режим deep-thinking его не поддерживает;
  `qwen3.8-max-preview` не маршрутизировать — строгий JSON на нём структурно невозможен.
- Сроки снятия моделей: 05.08 (Opus 4.1), 26.08 (Assistants API, включая Azure), 31.08, 10.10.

### Changed
- **Версия отображается одна во всех местах** — `8.4.6-N`, включая заголовки файлов-модулей
  и вопрос о выборе хоста при старте.
- **Fable 5 выведен из весов маршрутизации** для задач кода и рассуждений (с 20.07
  тарифицируется по usage credits); его долю занял `claude-opus-5`.
- `claude-opus-4-8` остаётся доступным: пропал из селектора интерфейса, но не из API.
- **Сборка стала легче на ~7 500 символов (≈2 500 токенов при полной загрузке).** Из рабочих
  файлов убраны служебные хвосты: в каком поколении появилась секция, откуда портирована,
  даты правок, построчные changelog-заметки. Это история — её место здесь, а не в контексте
  модели при каждом запуске. Накопленный список возможностей перенесён в раздел внизу файла.
- **Номер версии теперь стоит в одном месте каждого файла — YAML-шапке.** Раньше он
  дублировался в заголовке, в поле `scope` и в хвостовом блоке; копии расходились — именно
  так и возник дефект с модулями [26-32].
- **Логика показа модулей в меню упрощена.** Пункты [26-32] показываются по флагу
  `MODULE_*` или по сработавшему триггеру — без отдельного прохода детекта по телам файлов.
  Проверено вживую: со сложным детектом меню отдавало 25 пунктов из 32 при всех включённых
  модулях, с простым правилом — все 32. Страховка сохранена: если пункт выбран, а файла
  модуля в контексте нет, система просит приложить файл и не выдумывает его содержимое.
- **Логотип при старте** заменён на простой ASCII — он одинаково отображается на всех хостах,
  в отличие от блочного, который разъезжался при переносе.
- **Добавлен флаг `MODULE_SKILLS`.** Модулей семь, а флагов было шесть: пункт [32]
  (генератор Agent Skills) гейтился правилом, для которого у него не было переключателя.
- Заголовок раздела обещал «25 базовых + 7 динамических v8N.3» — метка поколения убрана,
  счётчик сверен с реестром.

---

## [8.4.5 · 2026-07-19 · Code] Комплаенс-формулировки + возврат принципа A/B

### Fixed
- `grok-4.20` не имел профиля ни в одном `vendors/tier*.md`, хотя на него ссылались routing в
  `!!db_v8N`, `live_core` (вес 35%, CONTEXT_STRATEGY >500K) и `live_vendors`. Профиль `GROK_420`
  добавлен в `vendors/tier4.md`; указатели `#LINK_GROK` и routing → tier4. В N Grok остаётся
  target-слоем (GROK_JSON_TARGET + G14 safe-params); Heavy-16 пак — эксклюзив High/Light.

### Changed
- `EXCELLENT_TECHNIQUES`: убраны `Alien Archivist`, `Environmental Storytelling`, `Emotional Intimacy`
  (не относятся к точности промптинга). Заголовок → `False-positive calibration for legitimate
  professional domains` (мед./юр./аудит безопасности/техспеки) + `SCOPE`-ограничитель.

### Added
- Двуязычный дисклеймер (EN+RU) в `STARTUP_LOGO` ядра и в `USER SANDBOX` блоке `live_specs.md`:
  «P2P генерирует текстовые контракты, кода не исполняет; ответственность за запуск — на операторе».
- Блок «Назначение и ответственность» в `README.md` / `README.en.md`.
- Возврат `PRINCIPLE` в полной формулировке v3.2: «Лучший промпт — это не тот, который красиво
  написан, а тот, который доказал свою эффективность в тесте» (утерян при миграции ядра 7 → 8).

Контекст: `P2P_SELF_STUDY/_NEXT_RELEASE/03_PLAN_8.4.5_compliance_and_arena.md`

---

## [8.4.4-N · 2026-07-19 · Code] HOTFIX — data-drift по внешнему аудиту
- **Powод:** внешний аудит (GPT) указал на data-drift; подтверждено скриптом `_SERVICE/audit_model_data.py` на 8.4.4. Итог: **39 файлов, 108 строк** (C: 15 ф., H: 14, N: 10; **L чист**). Только данные — логика/структура/якоря не тронуты.
- **🔴 DeepSeek-миграция противоречила сама себе (H+N):** `!!core`/`live_vendors` говорили `deepseek-chat → deepseek-v4-pro`, а `!!db`/`MANIFEST` — `→ deepseek-v4-flash`. Приведено к канону: **оба алиаса → v4-flash (non-thinking/thinking), НЕ V4-Pro**; убраны неверные `[ex:]`-теги в db; tier2 G16-note уточнён.
- **🔴 Retired `claude-sonnet-4-6` в живых маршрутах → `claude-sonnet-5`:** fallback/cascade-цепочки `!routing` (C обе формы/H/N), `FALLBACK_CHAIN`+Tier2 в `!llm_router` (H), `!routing_matrix`/`!scope`/`_master`-шаблоны, `fallback_model` в `live_core` (C обе формы), sandbox-примеры, API_STRINGS-списки (`_preloader`/`!domain`/`!!core` SCAN_FOR). Historical-пометки ([PASSED]/[COMPLETED]/tier2-legacy-справка) сохранены.
- **🔴 Цены к канону 07-13:** Opus `$15/$75`→`$5/$25` (COST_ESTIMATE `!!core` H/N — пропуск фикса 07-14); GPT-5.5 `$7/$28`→`$5/$30` (+GPT-5.6 линейка); Sonnet→Sonnet 5 `$2/$10`; Gemini 3.1 Pro `$2/$12 ≤200K`; Grok 4.5 `$2/$6`/4.3 `$1.25/$2.50`; DeepSeek Pro `$0.435/$0.87`/Flash `$0.14/$0.28`.
- **🔴 H `!llm_router.md` CAPABILITY_MATRIX был целиком стар (2026-05-02, пропущен интеграцией 07-14):** Opus 200K/$15/$75, sonnet-4-6, GPT-5.5 128K/$7/$28, DeepSeek 32K, `moonshot-v2-128k`, `glm-5.1-flash`. → канон: 1M-линейка Claude, **grok-4.20 (Heavy-16)**, **grok-4.5**, **gpt-5.6-sol**, **kimi-k2.6**, **glm-5.2**, qwen3.6-plus; Long-ctx правило → gemini 2M / grok-4.20 2M.
- **🟡 Синхронизация двух форм C:** plugin `core.md` identity (был «Opus 4.7 / Sonnet 4.6 primary») → как for-chat: «Fable 5 / Opus 4.8 (primary) / Sonnet 5 (default)»; plugin `preloader.md` примеры target_model; plugin `CLAUDE.md` список API-строк (+sonnet-5, sonnet-4-6 → API-legacy).
- **🟡 Agentic-роутинг C:** `gpt-5.5 → manus/manus-1.6-max` → `gpt-5.6-sol → gpt-5.5-pro (Codex)` — Manus track-only и по канону не маршрутизируется; db «Coding | Opus 4.7» → Opus 4.8 (соответствие routing-модулю); индексы/README: GPT-5.5 → GPT-5.6.
- **⚙ `_SERVICE/audit_model_data.py` → pre-release gate:** EDITIONS → 8.4.4; +6 паттернов (deepseek→pro-миграция, sonnet-4-6 как routing source/target/шаблон, `$15/$75`, `$7/$28`). Прогон после правок: 0 хитов по новым паттернам во всех 4 сборках.

## [8.4.4-N · 2026-07-18 · Code] v8N.4 — +8 техник промпт-инжиниринга
- **8 техник** (add-only, компактный формат): POSITIVE_FRAMING / VERBALIZED_SAMPLING / BRUTAL_EDITOR (в `!!db_v8N §2`, host-adaptive); GEPA / MASPO / SePO-backlog (`!optimization`); Context-Grounding CoT (`!reasoning` + ссылка `!rag`); Context Engineering (`!compression` + `!memory`).
- COMBINATOR + VECTOR fabrication-list расширены (VS≠USC, GEPA≠GoT, MASPO≠ToT); MASPO note (I7=8 неизменно); POSITIVE_FRAMING правило в `!!core` P5.
- **Внутренняя версия** v8N.3 → **v8N.4**; **внешний релиз** 8.4.3 → **8.4.4** (координированно).
- **Источники техник:** `docs/CREDITS_TECHNIQUES.md` (arXiv, авторы, лицензии).

### [HOTFIX · 2026-07-18] !!core_v8N.md — восстановлены 3 потерянных блока данных
Сравнение с эталоном `!!core_v8H.md` (v8.4.3-H) выявило 3 потери при сборке ядра v8N.4:
- **🔴 QUICK_COMMANDS:** полный блок 24 слэш-команд отсутствовал (осталась 1 строка-комментарий) → восстановлен с адаптацией нумерации под N-edition (25+7 пунктов).
- **🔴 HOST_PROFILES minimax/manus:** 2 TRACK-ONLY host-only профиля полностью исчезли → восстановлены (v8N.4 identity, совпадают с _index.md «10 хостов»).
- **🔴 VERSION_METADATA.NEW_IN_v8N:** файл обрезан на строке 649 (`- G-`) → восстановлен полный список (14 строк из v8H + 5 строк дельты v8N.3/v8N.4).
- Аудит 8.4.4-H и 8.4.4-L потерь не выявил.

## [8.4.3-N · 2026-07-13 · Cowork] Live Specs v8.6.3 · host-detect fix · Grok target-слой · Agent Skills
- **E2 Live Specs → v8.6.3:** `files/_live/live_specs.md` обновлён; MANIFEST version-пины → v8.6.3.
- **E5 Host-detect fix (`_preloader` БЛОК 0):** `NORMALIZE` HOST_MODEL → lowercase + синонимы grok; `ENV_SIGNALS` (HIGH при неуверенном self-name); LOW → обязательный `HOST_PICK_LIST` перед меню; `PERSIST`; хинт `/host grok`.
- **E3 Grok target-слой:** новый `files/vendors/grok.md` (grok-4.5/4.3, G14 safe-params, TARGET); секция **GROK_JSON_TARGET** в `!pipeline.md`; GROK-ветка в P1 CROSS_MODEL (`!!core_v8N`). Полный Heavy-16 — НЕ в N.
- **E1 Agent Skills:** новый ON-DEMAND `!skills.md` (генератор `SKILL.md`, agentskills.io); пункт меню **[32]** (EXTENSIONS_SCAN-гейт) + `/p2p-skill`; регистрация в `_preloader`/`_index`.
- **E6:** ссылка anti-patterns в P6 → «Type A–Q» (синхр. с эталоном).
- **E7:** bump 8.4.2 → 8.4.3 (README, каталог `editions/8.4.3-N`).

### Code 2026-07-14 — live_specs→дельта, docs, токен-карта
- **✂️ `_live/live_specs.md` → ДЕЛЬТА:** 91849→31061 б, **31 351→10 614 токенов** (стабильные спеки — в `vendors/tier*` + `live_vendors`).
- **🔴 docs:** неверный маппинг DeepSeek `chat→v4-pro` → `chat`/`reasoner`→**`v4-flash`** (дедлайн `24.07 15:59 UTC, no grace`); `qwen3-plus`→`qwen3.6-plus`; `glm-5.1-flash`→`glm-5.2`(1M)/`glm-5.1`(~120K).
- **📊 `docs/ЧТО_ЗАГРУЖАТЬ.txt` пересчитан** реальным токенайзером (o200k): минимум 27 000→**29 200**; `_preloader` 3500→4000, `live_vendors` 4600→5300, live_specs 27 800→10 600; добавлен `!skills.md` [32].

### Code-ревизия 2026-07-14 (интеграция Live Specs в BASE)
- **Live Specs v8.6.3 интегрирована в BASE:** `vendors/tier1-4` + `_live/{live_core,live_vendors}` перенесены из готового H (baseline-diff: N==H с точностью до тега v8N/v8H); `MANIFEST` + `!!db_v8N` §API STRINGS → канон 2026-07-13. +Sonnet 5/GPT-5.6/Grok 4.5/GLM-5.2/Kimi K2.7; retire Sonnet 4.6.
- **Дубль `vendors/grok.md` удалён** (Grok — target, уже в tier2); ссылки (`!!core`/`_index`/`_master`/`!pipeline`) → tier2.
- Метод: правил только канон-метрики; логику/паттерны/G-errors не тронул.

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

---

## Накопленные возможности поколения 8N

> Перенесено 2026-07-26 из служебных блоков внутри файлов сборки. Раньше этот список
> лежал в `!!core_v8N.md`, `_preloader.md`, `!agents.md`, `!pipeline.md` и грузился в контекст
> при каждом запуске. Здесь он выполняет ту же функцию, не занимая место в рабочих файлах.

**Ядро и хосты**
- `HOST_PROFILE_LOADER` — 8 моделей с актуальными API-строками.
- Реестр ошибок G1-G20 встроен в каждый профиль хоста.
- `DEADLINE`-флаги на устаревших API-строках + DEADLINE Scanner (пункт меню).
- Translation Layer v2 — 7 конвертаций между синтаксисами хостов.
- `DEEP_THINK_VALUE_GATE` v2 — синтаксис под конкретный хост.
- `CONSTRAINT_REINJECTION_PROTOCOL` v2 — переинъекция ограничений по ходу сессии.
- Автодетект хоста (`SELF_IDENTIFY` + `CONFIDENCE_GATE`), 10 хостов; при неуверенности —
  ручной выбор из списка `[1..10]` до показа меню.

**Агенты и конвейер**
- HELIOS — восьмой агент, финальный синтезатор (выделен из ARCHITECTON).
- Template M (Karpathy Mode) в `!pipeline.md`, обновлённый Step 8 под все 8 моделей.

**Память и метрики**
- Session Metrics v0.2.
- Routing Memory v2 с затуханием.
- Каталог `_live/` — `MANIFEST`, `live_core`, `live_vendors`.

**Модули по требованию**
- 6 ON-DEMAND модулей: RAG, Reasoning, Routing, Compression, Security, Optimization.
- `EXTENSIONS_SCAN` + `MENU_RENDER_ALGORITHM` — динамическое меню [26-32].
- `VERSION_COMPAT` (+ 6 флагов `MODULE_*`) и `CONFLICT_RESOLVER` v1.0 в `_preloader`.
- Генератор Agent Skills — пункт [32] и `/p2p-skill`.

**Техники**
- +8 техник промпт-инжиниринга: POSITIVE_FRAMING, VERBALIZED_SAMPLING, BRUTAL_EDITOR,
  GEPA, MASPO, SePO, Context-Grounding CoT, Context Engineering.
