# P2P v8H.3 — CHANGELOG (Hybrid Edition)

**Build:** v8H.3 / edition 8.4.3-H (Hybrid = merge 8A.1 Gemini ⊕ 8G.1 Grok) · **Date:** 2026-07-13
**Base:** универсальный каркас 8N-style + 8C.3 parity · **Donors:** 8A.1, 8G.1 (read-only).

---

## [8.4.6-H] — 2026-07-26

Изменения с версии 8.4.5-H.

### Added
- **`claude-opus-5` — основная модель** (1M/128K, $5/$25, thinking включён по умолчанию).
  Добавлены `gemini-3.6-flash` (1M/65K, $1.50/$7.50, ~304 tok/s), `gemini-3.5-flash-lite`
  ($0.30/$2.50) и `kimi-k3` (WebDev #1, $3/$15) — последний с меткой **ACCESS-RISK,
  не назначается основным**: hosted-only, подписки закрыты, весов нет.
- **Automatic Fallbacks** в профиле Claude: параметр, beta-header, наблюдаемый блок ответа,
  `usage.iterations`, расщепление биллинга, как отключить.
- **Две новые записи в базе ошибок:** G21 (несовпадение заявленной и фактической модели —
  сверять `resolved_model_slug`, у Anthropic смотреть блок `{"type":"fallback"}`) и
  G22 (агентная опасность GPT-5.6 Sol).
- Сроки снятия моделей: 05.08 (Opus 4.1), 26.08 (Assistants API, включая Azure), 31.08, 10.10.

### Changed
- **Версия отображается одна во всех местах** — `8.4.6-H`, включая восемь строк
  `HOST_IDENTITY`, заголовки файлов-модулей и вопрос о выборе хоста при старте.
- **Fable 5 выведен из весов маршрутизации** для задач кода и рассуждений (с 20.07
  тарифицируется по usage credits); его долю (35%) занял `claude-opus-5`.
- `claude-opus-4-8` остаётся доступным: пропал из селектора интерфейса, но не из API.
- Токенизатор: канон **~+30%** (одна официальная цифра вместо вилки) + Token Counting API.
- **Сборка стала легче на ~7 300 символов (≈2 400 токенов при полной загрузке).** Из рабочих
  файлов убраны служебные хвосты: кто донор секции, в каком поколении она появилась, даты
  правок, построчные changelog-заметки. Всё это — история, её место здесь, а не в контексте
  модели при каждом запуске. Накопленный список возможностей перенесён в раздел внизу файла.
- **Номер версии теперь стоит в одном месте каждого файла — YAML-шапке.** Раньше он
  дублировался в заголовке, в поле `scope` и в хвостовом блоке; копии расходились.
- **Логотип при старте** заменён на простой ASCII — он одинаково отображается на всех
  хостах, в отличие от блочного, который разъезжался при переносе.
- **В самоопределении системы указывается поколение, а не выпуск** — «Ты — P2P v8H,
  работающий на Claude» вместо номера выпуска. Номер выпуска остаётся там, где он нужен:
  логотип, шапка меню, строка статуса.
- **Добавлен флаг `MODULE_SKILLS`.** Модулей семь, флагов было шесть — пункт генератора
  Agent Skills гейтился правилом, для которого у него не было переключателя.
- Заголовок раздела меню обещал «30 базовых + 6 динамических» при фактических
  **37 базовых и 8 динамических** — счётчик сверен с реестром.

### Fixed
- **Правило миграции DeepSeek было перевёрнуто:** бывший `deepseek-reasoner` идёт на
  **v4-pro**, а не на v4-flash — иначе reasoning тихо деградирует.
- **Цена Grok на кэшированный ввод:** `$0.30` short / `$0.60` long вместо `$0.50`;
  добавлен порог 200K, после которого тариф удваивается **вместе с кэшем**, и пометка
  о том, что `reasoning_effort` отключить нельзя.
- **Grok в EU:** доступ открыт 21.07; ограничение переформулировано с недоступности
  на персональные данные (размещение данных не гарантируется).
- Правило удорожания на длинном контексте уточнено: ×2 на некэшированный ввод, ×1.5 на вывод,
  **кэшированный ввод не дорожает**; у xAI порог свой — 200K, и кэш там дорожает тоже.
- Цена GLM-5.2 помечена как неподтверждённая (единственный источник противоречив сам себе),
  а не подана как факт.
- Проверено и подтверждено: моделей `grok-4.5-heavy` / `-expert` / `-fast` не существует —
  ссылок на них в редакции нет.
- Заголовок модуля `!x_realtime.md` отставал от версии ядра — приведён в соответствие.
- **Логотип при старте показывал `P2P v8H.4- HIGH EDITION`** — старый номер, да ещё и
  со слипшимся разделителем. Теперь `P2P 8.4.6-H — HIGH EDITION`.
- В шапке `_preloader.md` было сказано, что механика автодетекта хоста портирована
  из `8.4.6-H`, то есть из самой себя. Восстановлен источник — `8L.3` (редакция Lite).

---

## [8.4.5 · 2026-07-19 · Code] Комплаенс-формулировки + возврат принципа A/B

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

## [8.4.4-H · 2026-07-19 · Code] HOTFIX — data-drift по внешнему аудиту
- **Powод:** внешний аудит (GPT) указал на data-drift; подтверждено скриптом `_SERVICE/audit_model_data.py` на 8.4.4. Итог: **39 файлов, 108 строк** (C: 15 ф., H: 14, N: 10; **L чист**). Только данные — логика/структура/якоря не тронуты.
- **🔴 DeepSeek-миграция противоречила сама себе (H+N):** `!!core`/`live_vendors` говорили `deepseek-chat → deepseek-v4-pro`, а `!!db`/`MANIFEST` — `→ deepseek-v4-flash`. Приведено к канону: **оба алиаса → v4-flash (non-thinking/thinking), НЕ V4-Pro**; убраны неверные `[ex:]`-теги в db; tier2 G16-note уточнён.
- **🔴 Retired `claude-sonnet-4-6` в живых маршрутах → `claude-sonnet-5`:** fallback/cascade-цепочки `!routing` (C обе формы/H/N), `FALLBACK_CHAIN`+Tier2 в `!llm_router` (H), `!routing_matrix`/`!scope`/`_master`-шаблоны, `fallback_model` в `live_core` (C обе формы), sandbox-примеры, API_STRINGS-списки (`_preloader`/`!domain`/`!!core` SCAN_FOR). Historical-пометки ([PASSED]/[COMPLETED]/tier2-legacy-справка) сохранены.
- **🔴 Цены к канону 07-13:** Opus `$15/$75`→`$5/$25` (COST_ESTIMATE `!!core` H/N — пропуск фикса 07-14); GPT-5.5 `$7/$28`→`$5/$30` (+GPT-5.6 линейка); Sonnet→Sonnet 5 `$2/$10`; Gemini 3.1 Pro `$2/$12 ≤200K`; Grok 4.5 `$2/$6`/4.3 `$1.25/$2.50`; DeepSeek Pro `$0.435/$0.87`/Flash `$0.14/$0.28`.
- **🔴 H `!llm_router.md` CAPABILITY_MATRIX был целиком стар (2026-05-02, пропущен интеграцией 07-14):** Opus 200K/$15/$75, sonnet-4-6, GPT-5.5 128K/$7/$28, DeepSeek 32K, `moonshot-v2-128k`, `glm-5.1-flash`. → канон: 1M-линейка Claude, **grok-4.20 (Heavy-16)**, **grok-4.5**, **gpt-5.6-sol**, **kimi-k2.6**, **glm-5.2**, qwen3.6-plus; Long-ctx правило → gemini 2M / grok-4.20 2M.
- **🟡 Синхронизация двух форм C:** plugin `core.md` identity (был «Opus 4.7 / Sonnet 4.6 primary») → как for-chat: «Fable 5 / Opus 4.8 (primary) / Sonnet 5 (default)»; plugin `preloader.md` примеры target_model; plugin `CLAUDE.md` список API-строк (+sonnet-5, sonnet-4-6 → API-legacy).
- **🟡 Agentic-роутинг C:** `gpt-5.5 → manus/manus-1.6-max` → `gpt-5.6-sol → gpt-5.5-pro (Codex)` — Manus track-only и по канону не маршрутизируется; db «Coding | Opus 4.7» → Opus 4.8 (соответствие routing-модулю); индексы/README: GPT-5.5 → GPT-5.6.
- **⚙ `_SERVICE/audit_model_data.py` → pre-release gate:** EDITIONS → 8.4.4; +6 паттернов (deepseek→pro-миграция, sonnet-4-6 как routing source/target/шаблон, `$15/$75`, `$7/$28`). Прогон после правок: 0 хитов по новым паттернам во всех 4 сборках.

## [8.4.4-H · 2026-07-18 · Code] v8H.4 — +8 техник промпт-инжиниринга
- **8 техник** (add-only, компактный for-chat): POSITIVE_FRAMING / VERBALIZED_SAMPLING / BRUTAL_EDITOR (в `!!db_v8H §2`, host-adaptive — VS без хардкода XML для мультихоста, G2); GEPA / MASPO / SePO-backlog (`!optimization`); Context-Grounding CoT (`!reasoning` + ссылка `!rag`); Context Engineering (`!compression` + `!memory`).
- COMBINATOR + FABRICATION_SCAN расширены (VS≠USC, GEPA≠GoT, MASPO≠ToT); MASPO note у WEIGHT_TABLE (I7=8 неизменно); POSITIVE_FRAMING правило в `!!core` P5.
- **Внутренняя версия** v8H.3 → **v8H.4** (тронутые модули + системные `_preloader`/`_index`/`_master`).
- **Внешний релиз** 8.4.3 → **8.4.4** (координированно со всеми сборками C/N/L).
- **Источники техник:** `docs/CREDITS_TECHNIQUES.md` (arXiv, авторы, лицензии).

## [8.4.3-H · 2026-07-13 · Cowork pass] Live Specs v8.6.3 · host-detect fix · GROK_HOST_GUIDE · Agent Skills
- **E2 Live Specs → v8.6.3:** `files/_live/live_specs.md` обновлён (Grok 4.5 GA 2026-07-08, GPT-5.6 GA, Fable 5 #1); MANIFEST version-пины → v8.6.3.
- **E5 Host-detect fix (`_preloader` БЛОК 0):** `NORMALIZE` HOST_MODEL → lowercase + синонимы (`GROK`/`Grok`/`xai` → grok); `ENV_SIGNALS` (X-инструменты / grok.com / Grok Build → grok HIGH даже при неуверенном self-name); LOW → обязательный `HOST_PICK_LIST` перед меню; `PERSIST`; хинт `/host grok`. Тестовый хардкод `HOST_MODEL: "GROK"` сброшен на `""`.
- **E4 `docs/GROK_HOST_GUIDE.md`** (NEW): Grok Build CLI (install/device-auth/headless `--prompt-file`), grok.com (нативные агенты, Agent Skills), offload-подводный камень >~50K; перекрёстная ссылка из `HOST_GUIDE.md`.
- **E1 Agent Skills:** новый ON-DEMAND `!skills.md` (генератор `SKILL.md`, agentskills.io); пункт меню **[42]** + `/p2p-skill`; регистрация в `_preloader`/`_index_v8H`.
- **E7:** bump 8.4.2 → 8.4.3 (README, каталог `editions/8.4.3-H`).

### Code 2026-07-14 — live_specs→дельта, docs, grok.md, токен-карта
- **✂️ `_live/live_specs.md` → ДЕЛЬТА:** 91849→31061 б, **31 351→10 614 токенов**. Стабильные спеки моделей теперь только в BASE (`vendors/tier*`, `live_vendors`); live_specs несёт волатильное (deltas/deadlines/ERROR_REGISTRY/ARENA/media/changelog).
- **🔴 `vendors/grok.md` — исправлена атрибуция:** Heavy-16 и 2M приписывались `grok-4.3`; по канону это `grok-4.20`. Разделено: `grok-4.5` (500K, $2/$6, ⚠ не EU) · `grok-4.3` (1M, $1.25/$2.50) · `grok-4.20` (2M, Heavy-16) · `grok-build-0.1`. Файл остаётся в H легитимно — от него зависит `!grok_heavy.md`; `_index_v8H` строка 14 обновлена.
- **🔴 docs:** неверный маппинг DeepSeek `chat→v4-pro` → `chat`/`reasoner`→**`v4-flash`** (дедлайн `24.07 15:59 UTC, no grace`); `qwen3-plus`→`qwen3.6-plus`; `glm-5.1-flash`→`glm-5.2`(1M)/`glm-5.1`(~120K).
- **📊 `docs/ЧТО_ЗАГРУЖАТЬ.txt` пересчитан** реальным токенайзером (o200k): минимум 32 000→**34 400**, на Grok 35 000→**38 600**; `_preloader` 4400→5000, `live_vendors` 4600→5300, live_specs 27 800→10 600; добавлен `!skills.md`.

### Code-ревизия 2026-07-14 (интеграция Live Specs в BASE)
- **Live Specs v8.6.3 интегрирована в BASE:** `vendors/tier1-4`, `vendors/CLAUDE.md`, `_live/{live_vendors,live_core,MANIFEST}`, `!!db_v8H` §API STRINGS → канон 2026-07-13. +Sonnet 5/GPT-5.6 Sol/Terra/Luna/Grok 4.5/GLM-5.2/Kimi K2.7; retire Sonnet 4.6.
- **⚠ Пред-баг H исправлен** (не от Cowork): Claude `context: 200K` → **1M**, Opus 4.x `$15/$75` → **$5/$25** (в tier1/CLAUDE.md/live_core/host_engine).
- `vendors/grok.md` **сохранён** (легитимный host-профиль Grok, дата бампнута).
- Метод: правил только канон-метрики; G1-G20 каталог, translation-rules, prompting-паттерны не тронуты.

## [8.4.3-H · 2026-07-13] Grok Heavy-16 native pack + strict JSON
- **NEW `!grok_heavy.md`** (host-module H6) — восстанавливает нативную мощь донора 8G.1 в High edition:
  - **GROK_HANDSHAKE (§A)** — offer-on-detect: при `HOST_MODEL=grok` (запуск P2P НА Grok) ИЛИ
    `TARGET_MODEL=grok` (генерация промпта ПОД Grok) → однократно предлагает собрать нативный пак.
    Никогда молча; через INTERACTIVE_CHOICE; отказ помнится (P5).
  - **GROK_JSON_CONTRACT (§B)** — «самый строгий на рынке JSON»: canonical envelope, `json_schema strict:true`
    (constrained decoding), JSON-only discipline (Type H guard), G14 SAFE-PARAMS (иначе HTTP 400), re-inject @8.
  - **GROK_PACK (§C) + GENERATOR (§D)** — 8 канонических агентов + HEAVY_ORCHESTRATOR как pasteable
    plain-text+JSON скелеты (нативно для Grok, как sub-agents на Claude). ANON=tool-exec на grok.
- **Wiring (без дублирования):** `_preloader` GROK_FLAGS.GROK_PACK_OFFER + ON_DEMAND-триггер ·
  `!host_profiles` GROK_ADVANTAGE_RULE (оба триггера) · `!agents` РЕЖИМ A ссылается на скелеты ·
  `!!core` P1 Grok-ветка + `/p2p-grok` · `_index` H6 + dependency map. Источники чисел/специй не тронуты
  (!tool_budget, !x_realtime, vendors/grok — единственные владельцы). Модуль тратит 0 токенов вне grok.
- **Инварианты:** XML только в code-fences (I6); YAML frontmatter; offer-gated.
- **✅ LIVE-ТЕСТ на Grok-4.5 (Grok Build CLI, 2026-07-13):** headless-прогон бандла High → Grok сам определил host=grok (HIGH), воспроизвёл GROK_HANDSHAKE дословно, сгенерировал нативный Heavy-16 пак (5 агентов T3 + HELIOS + строгий JSON envelope/json_schema strict). TRIGGER_2 (target=grok с чужого хоста) и Type H-стресс (JSON-only под давлением) — оба прошли. ANON=tool-exec понят верно; XML вне fences — нет. Само-проверка Grok: логика взята из !grok_heavy, не выдумана.
- **[LIVE] Specs grok-4.5** (source: docs.x.ai/developers/grok-4-5 + live `grok models`): добавлен `grok-4.5` в vendors/grok, live_specs, live_vendors, live_core — coding/agentic flagship, $2/$6, ~500K ctx, ~2x token eff., strict json_schema, GA (не EU), cutoff 2026-02-01. Grok 4.4 — SKIPPED (вышла 4.5). Grok Build CLI теперь на grok-4.5.

## [NEW] Гибридная редакция (merge 8A.1 + 8G.1)
- Универсальный preloader: `HOST_MODEL` (8 хостов) + `HOST_CAPS` авто-гейты + `GROK_FLAGS` + VERSION_COMPAT.
- **`!host_profiles.md`** — host-choice brain: при `HOST_MODEL=grok` → нативный Heavy-16; иначе → simulated QUORUM.
- **`!agents.md`** — host-gated merge: Heavy-16 (8G) ⊕ simulated QUORUM раунды 1-8 (8A).
  - **ANON host-gated**: grok→tool-exec (≤18 calls); иначе→neutral reviewer (FABRICATION_SCAN).
  - **Безопасность вынесена в `!security.md`**, НЕ на ANON (в отличие от 8C.3). Матрица — docs/MERGE_NOTES.md.
  - VECTOR=data (default; creative→IRIS/!writing); DATOS=data+realtime (X только на grok); AXIOM-before-write (union).

## [NEW] Grok host-engine (порт из 8G.1)
- `!llm_router.md` — multi-provider router; default primary=HOST_MODEL (не хардкод Grok); +Fable 5/Opus 4.8;
  contract-translation на 8 хостов (Gemini zero-XML); unified output schema сохранён; fallback chain host-agnostic.
- `!routing_matrix.md` — аудируемая routing matrix v2.0 (task taxonomy + примеры).
- `!tool_budget.md` — Type B prevention (budget 25, ANON ≤18, re-inject @8); grok-gated.
- `!x_realtime.md` — X Firehose ($0.50 value gate, 7-day cache); только grok host.
- `!!db_v8H`: добавлены Grok Heavy failure modes Type B/H/T/X/V + G14.

## [PARITY] 8C.3 техники (унаследованы из 8N.3)
- 6 ON-DEMAND модулей [35-40]: RAG/Reasoning/Routing/Compression/Security/Optimization (host-gated, ≤5K).
  `!routing` ссылается на `!llm_router` (без дублирования cascade/cost).
- VERSION_COMPAT (legacy/v3 + 6 MODULE_* default false) + CONFLICT_RESOLVER v1.0 + динамическое меню [35-40].
- Расширения memory/agents/metrics/toolkit (append-блоки).

## [LIVE] Нативный live-specs 2026-06-12 (v8.4)
- Claude Fable 5 (#1 Agent/WebDev) + Opus 4.8 в tier1/live_core/live_vendors/llm_router.
- Старые спеки доноров (8A=05-19, 8G=05-19) не переносились; единый источник — live_specs_20260617.

## [FORM] Две формы поставки
- flat (Chat/Projects/API) + native plugin (`.claude/agents/p2p-*.md` ×8 + `.claude-plugin/{plugin,marketplace}.json`).

## [META]
- Версии v8H.3 во всех операционных файлах; G1-G20 union обоих доноров сохранён.
- Дедлайны: Claude dated legacy / gpt-5.x legacy — PASSED, литералы отсутствуют (унаследовано из 8N.3);
  deepseek-chat/reasoner (07-24) — активные ретайр-нотисы. budget_tokens не используется (G7).

---

## Тесты (3 кейса/модуль вкл. grok-host и gemini-host)
| Кейс | Ожидание |
|------|----------|
| grok host, agentic T4 | Heavy-16 native (реальный параллелизм), Tool Budget, ANON=tool-exec ≤18 |
| gemini host, тот же запрос | simulated QUORUM раунды 1-8, ZERO-XML (G2), ANON=neutral reviewer |
| !routing на любом хосте | ссылка на !llm_router; не дублирует cascade |
| !security активен | GUARDIAN форс ON; ANON остаётся в родной роли (security отдельно) |
| X Firehose на non-grok | недоступен → web_search fallback |
| budget_tokens / temp+thinking | отсутствуют (G7); retired строки только в нотисах |

---

## Накопленные возможности поколения 8H

> Перенесено 2026-07-26 из служебных блоков внутри файлов сборки (`!!core_v8H.md`,
> `_preloader.md`, `!pipeline.md`). Раньше этот список грузился в контекст при каждом запуске.

**Ядро и хосты**
- `HOST_PROFILE_LOADER` — 8 моделей с актуальными API-строками; всего 10 хостов
  (+ MiniMax, Manus), данные — в `live_specs`.
- Реестр ошибок G1-G20 встроен в каждый профиль хоста.
- `DEADLINE`-флаги на устаревших API-строках + DEADLINE Scanner (пункт [44]).
- Translation Layer v2 — 7 конвертаций между синтаксисами хостов.
- `DEEP_THINK_VALUE_GATE` v2 — синтаксис под конкретный хост.
- `CONSTRAINT_REINJECTION_PROTOCOL` v2.
- `HOST_MODEL` по умолчанию пуст — нативный автодетект хоста (порт механики Lite).

**Агенты и конвейер**
- HELIOS — восьмой агент, финальный синтезатор.
- Template M (Karpathy Mode) в `!pipeline.md`, обновлённый Step 8 под все 8 моделей.

**Память и метрики**
- Session Metrics v0.2 · Routing Memory v2 с затуханием.
- Каталог `_live/` — `MANIFEST`, `live_core`, `live_vendors`.

**Модули по требованию**
- 6 ON-DEMAND триггеров: rag, reasoning, routing, compression, security, optimization.
- `VERSION_COMPAT` (legacy/v3 + 6 флагов `MODULE_*`) и `CONFLICT_RESOLVER` v1.0.
- `live_specs` в последовательности загрузки.
