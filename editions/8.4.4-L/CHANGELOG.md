---
id: changelog_v8L3
version: v8L.3
type: DOC
last_verified: 2026-07-07
---

# CHANGELOG — P2P v8L.3 (Lite/Live Hybrid)

> Ветка миграции из **v8H.3** (30-файловый монолит) в **Resolver-Gated Lazy Hybrid**:
> 4 локальных BOOT-файла + 11 lazy Gist-чанков, загружаемых по триггеру через
> dependency-resolver с проверкой целостности sha256.

## [8.4.4-L] — 2026-07-18 (Code: v8L.4 — +техники промпт-инжиниринга, Light-scope)
- **Техники** (add-only, компактно в `!!db_v8L`): POSITIVE_FRAMING, VERBALIZED_SAMPLING, BRUTAL_EDITOR, CONTEXT_GROUNDING_COT, CONTEXT_ENGINEERING (одностроч.); COMBINATOR + TECHNIQUE_COMBINATOR DO_NOT_BLOCK (VS≠USC, GEPA≠GoT, MASPO≠ToT); POSITIVE_FRAMING правило в `!!core_v8L` P5.
- **Фреймворки GEPA/MASPO/SePO** — только справочно (нужен eval-harness → в Lite не активируются, чтобы держать токен-экономию).
- **Внутренняя версия** v8L.3 → **v8L.4**; **внешний релиз** 8.4.3 → **8.4.4** (координированно).
- **Источники техник:** `docs/CREDITS_TECHNIQUES.md` (arXiv, авторы, лицензии).

## [8.4.3-L] — 2026-07-13 (Cowork: Live Specs v8.6.3 + host-normalize)

- **E2 Live Specs → v8.6.3 (Gist):** L тянет live_specs из отдельного unpinned gist `a64245c3f824f45708519d57e0d62408` (raw/live_specs.md). Canon v8.6.3 готов к заливке (`VERSION:` + `// END OF FILE` → integrity-gate проходит). ⚠ Сама заливка `gh gist edit` — ОТДЕЛЬНЫМ шагом после `gh auth login` (см. HANDOFF).
- **E5 Host-normalize (`_preloader_v8L` БЛОК 0/HOST_CONFIG):** `HOST_MODEL_NORMALIZE` → lowercase + синонимы grok (`GROK`/`Grok`/`xai` → grok) ДО любого сравнения; ENV_HINT (X-инструменты / grok.com / Grok Build → grok); `PERSIST`; хинт `/host grok`.
- **НЕ добавлялось (решение Master):** Grok target-слой и Agent Skills генератор — в Lite намеренно НЕ портируются (экономия токенов).
- **E7:** bump 8.4.2 → 8.4.3 (`plugin.json`, README, каталог `editions/8.4.3-L`).

### 🗑 BREAKING 2026-07-14 — плагинная форма Lite УДАЛЕНА НАВСЕГДА
**Причина (решение Master):** команды/скиллы 8L.3-плагина пересекались с 8C.3 — при установке обоих
плагинов в Claude Code они «заражали» друг друга одноимёнными файлами. Lite и так задуман как лёгкая
файловая сборка; держать вторую форму поставки = мусорить в системе Claude Code.
- **Удалено:** `editions/8.4.3-L/plugin/` (27 файлов: `.claude/agents` ×8, `.claude/commands` ×15, `settings.json`,
  `.claude-plugin/plugin.json`, `pack.ps1`, `README.md`) + бандл `p2p-v8l3.plugin`. **Восстановлению не подлежит** (при нужде — из `current_version/editions/8.4.2-L/`).
- **Состав 8L.3 теперь:** `boot/` (4 файла загрузки: `_preloader` · `_index` · `!!core` · `!!db`) + `docs/` + `README(.en)` + `INSTALL` + `CHANGELOG`.
- **Ссылки починены:** `README.md`/`README.en.md` (убрано «плагин — ручная установка», добавлено «файловая сборка; для Claude Code → 8C.3»),
  `INSTALL.md` (переписан: убран «Способ 1 — Native plugin», остался файловый путь + `/p2p-verify` + блок «Почему у Lite нет плагина»),
  `docs/README.md` (структура релиза без `claude/`), `docs/AGENTS_GUIDE.md` (агенты только из `CORE_PLUS`),
  `tools/RELEASE_CHECKLIST.md` (убран `p2p-v8l3.plugin` из ассетов; помечено, что плагин в репо ровно один — `p2p-v8c3`).
- `marketplace.json` не трогали — `p2p-v8l3` там уже отсутствовал (убран в 8.3.9).

### Code 2026-07-14 — docs/ актуализированы под новую механику
- `docs/README.md` · `HOST_GUIDE.md` · `FAQ_И_ОШИБКИ.md` · `AGENTS_GUIDE.md` — убраны все упоминания `LITE_ONLY`/`LITE_DECLINE`
  (режима больше нет), описан единый `GIST_LAZY_FETCH`; таблица хостов → «инструмент веб-доступа» вместо «Fetch → LOAD_MODE».
- **Добавлена ключевая рекомендация пользователю** (во всех 4 документах): после выбора хоста **сначала `/p2p-verify`**,
  работа — только после успешного отчёта; не прошло → включить веб-доступ в настройках хоста (Gemini — grounding/поиск,
  GPT — browsing, Qwen/GLM/DeepSeek — провайдерский web-tool). Ошибка E1 переписана под «ленивый отказ» (`R. Refusal/Laziness`).
- Метрики хостов в `HOST_GUIDE` → канон (claude 1M + adaptive; deepseek 1M; qwen `qwen3.6-plus`; kimi 256K-1M; glm 5.2 1M / 5.1 ~120K).
- `docs/CHANGELOG_v8L3.md` — новая запись `[8.4.3-L] 2026-07-14` (единый режим + компрессия −52% + Live Specs v8.6.3 + канон host-профилей);
  исторические записи 8.3.0-L оставлены как есть (снимки во времени). idle-вес в docs: ~18K → ~10K.

### Code 2026-07-14 — добивка канона после Antigravity-пасса
- **API_STRINGS-футеры** (`_preloader`/`_index`/`!!db`) — были stale (`…claude-sonnet-4-6`, без Sonnet 5) → канон: `claude-fable-5, claude-sonnet-5, claude-opus-4-8/4-7/4-6, claude-haiku-4-5-20251001`.
- **`!!db §API_STRINGS`**: `claude-sonnet-4-6` убран из списка АКТИВНЫХ (компрессия срезала пометку RETIRED → модель могла счесть его валидной целью; retire задокументирован в LITE_SNAPSHOT-дедлайнах).
- **host-PROFILE в `!!core` — устаревшие метрики → канон:** claude `200K→1M` + adaptive thinking (budget_tokens удалён); gemini `1M→2M` (3.5 Pro = PREVIEW); gpt `128K→1.05M` + GPT-5.6 API-строки; grok `2M→500K/1M/2M` (4.5/4.3/4.20) + safe-list reasoning + EU-guard; deepseek `64K→1M` (out 384K); qwen `32K/128K→1M` + `qwen3-plus→qwen3.6-plus`; kimi `128K→256K-1M` + K2.7/HighSpeed; glm `100K→1M` (5.2) / `~120K` (5.1).
- `_preloader last_verified` → 2026-07-14.

### ⭐ Antigravity-пасс 2026-07-14 — BOOT: форсирование fetch + компрессия −52%
> Лог реконструирован Claude Code постфактум (правки делались без фиксации). Повод: прежние правки L дали побочку —
> Gemini сразу отказывался («нет инструмента fetch»). **Итог (эмпирика): fetch работает на claude/gemini/gpt/grok/deepseek/qwen.**

- **Режим `LITE_ONLY` УДАЛЁН** (21→0); вместе с ним `FETCH_HONESTY`/P8 (2→0) и `DECLINE`-fallback (3→0) — убран «лёгкий выход» в отказ.
- `_preloader FETCH_CAPABILITY_GATE.JUDGE` → безусловный (`fetch_capable=true`, `LOAD_MODE=GIST_LAZY_FETCH`); `SELECT_HOST_FETCH_MATRIX` — все 8 хостов `→ GIST_LAZY_FETCH ✓` (даже `deepseek: FETCH=usually NO → ✓`); `_index LOAD_MODES` только `GIST_LAZY_FETCH`, `FETCH_CANARY.rule` безусловное.
- **NEW** `!!core §NO_OFFLINE_ILLUSION` («ЗАПРЕЩЕНО: OFFLINE/SKIPPED/ограничения сессии; всегда WebFetch/Google»); **NEW** `/p2p-verify` — «ОБЯЗАТЕЛЬНО использовать инструменты поиска; ссылаться на ограничения ЗАПРЕЩЕНО»; **NEW** класс ошибки `!!db §R. Refusal/Laziness`.
- `_preloader`: автодетект хоста (Cowork E5) убран → явный вопрос «выбери хост [1..8]»; `HOST_MODEL_NORMALIZE` сохранён.
- **Компрессия BOOT ~87→~42 KB (−52%):** `_preloader` −62%, `_index` −75%, `!!core` −43%, `!!db` −39%. Вырезаны комментарии, CONTRACT SCHEMA, RESOLVER-псевдокод, SIZE_NOTES, VALIDATION_CHECK, MIGRATION-заметки.
- **Выжило:** канон LITE_SNAPSHOT/§API_STRINGS (Sonnet 5, GPT-5.6, Grok 4.5, GLM-5.2), re-pin канарейки `85411b2f`, `size_kb: 90`, пины SESSION_*.
- ⚠ **Риск:** утрачена честная деградация — на хосте без реального fetch возможна фабрикация чанков вместо отказа (`SKIP`/`DEGRADE` в `_index` сохранились, но без уведомления). ⚠ 3 stale-футера `API_STRINGS …sonnet-4-6`; `_preloader last_verified` не бампнут.

### Code-ревизия 2026-07-14 (Live Specs в монолит + Gist-слой, E2-L ЗАКРЫТ)
- **Монолит → канон 2026-07-13:** `!!db_v8L` (LITE_SNAPSHOT CURRENT_FLAGSHIPS + §5 API_STRINGS) + `!!core_v8L` (реестр + deadline-scanner) — +Sonnet 5/GPT-5.6/Grok 4.5/GLM-5.2/Kimi K2.7; retire Sonnet 4.6; дедлайны 19/24.07/31.08. Числа L берёт из Gist.
- **🌐 Gist-слой обновлён (E2-L закрыт):** LIVE gist `a64245c3` → v8.6.3; арсенальный gist `7727406` (`gist_vendors`/`gist_host_engine`/`gist_live_specs`) → канон; **новый revision `85411b2f`**; `_index_v8L` канарейка + CORE_PLUS перепиннуты на `85411b2f` (gist_route не менялся, sha256 `984c8c53…` валиден); SESSION_* оставлены на прежних ревизиях. Заливка через `gh gist edit` (git push блокируется sandbox).
- ⚠ Арсенальные gist-чанки без локального source-mirror в репо — кандидат на version-control.
- **🔴 Фикс size-drift LIVE (после тест-загрузки в Gemini 3.1 Pro):** LIVE gist вырос v8.6.2→v8.6.3 (48→~90 KB, 91849 b), но `_index_v8L` LIVE `size_kb` остался `~48` → anti-truncation `within(90,48,±15%)` провалил бы даже успешный fetch (→ ложный DEGRADE). Исправлено: `size_kb ~48→~90` + сделан **ADVISORY** для LIVE (целостность = freshness `VERSION:` + `end_marker`, размер не жёсткий — live_specs растёт); псевдокод резолвера получил ветку freshness-gated; size-заметки (BOOT/full arsenal/packaging) синхронизированы.

## [8.4.2-L] — 2026-07-07 (maintenance: YAML-шапки команд)

- **🔴 Починены YAML-шапки плагина** (унаследованный хвост, отмечен в 8.4.1): **14 команд
  без `description`** — добавлен из `scope` (Claude Code без description не показывает
  подсказку команды); **p2p-karpathy.md** — незакавыченное значение с `: ` внутри ломало
  YAML-парсер Claude Code (строгий) и могло ронять загрузку всего плагина (Cowork парсит
  мягко и маскировал). Все 15 файлов проверены pyyaml.
- Bump `8.4.1 → 8.4.2` (plugin.json) — запиненная версия бампается при изменении содержимого.

## [8.3.5-L] — 2026-06-26 (maintenance)
- **🔴 Удалён вложенный `.claude-plugin/marketplace.json`** (footgun: `source: "."` + устаревшая `version: 8.3.2-C`; создавал самоссылающийся `local-desktop-app-uploads`). Теперь `.claude-plugin/` = только `plugin.json`; маркетплейс один — в корне репо.
- **8/8 sub-агентов** получили обязательные `name` + `description` (была заглушка «Agent from plugin»; авто-делегация теперь работает).
- Bump версии `8.3.4-L → 8.3.5-L` (запиненная версия должна бампаться при изменении содержимого).

## [8.3.0-L] — 2026-06-27

### DEV/USER варианты + чистка (2026-06-27)
- Команда `/p2p-load` → **`/p2p-download`** (везде: меню [36], command-map, файл команды, доки).
- Удалён устаревший локальный `gist_live_specs.md` (нёс неверную «источник истины: _live/live_specs_20260617.md»;
  LIVE теперь тянет из gist `a64245`). Манифест регенерирован → **10 модульных чанков** + LIVE. verify 10/10.
- Две сборки на релиз: **DEV** (всё + инструменты/исходники/спека парсинга) и **USER**
  (загружаемые файлы + плагин + INSTALL/usage/mindmap/changelog; БЕЗ update-инструментов и detailed-механик).
- Клоны 8C/8H/8N: `*_DEV.zip` (auto-update live + static live_specs) и `*_USER.zip`
  (static snapshot, БЕЗ remote-механики, без dev-доков). Дата-имя `live_specs_20260617.md` → **`live_specs.md`** (static).
- Gist live specs: статичное имя файла `live_specs.md` — при апдейте меняется только содержимое (VERSION 8.5→8.6…).

### LIVE_SPECS — единый авто-обновляемый источник (2026-06-27)
- `LIVE` чанк переподключён на выделенный **unpinned** gist (`a64245c3…/raw/live_specs.md`) —
  всегда latest. Источник: `Live_UPDATE/` (юзер правит файл → `update_live.cmd` → один клик, без браузера/2FA).
- Свежесть проверяется маркером `VERSION:` + `// END OF FILE` (не sha256 — для live контент меняется).
- `_preloader_v8L` ON_LOAD шаг 5: при fetch_capable → fetch live → **override** LITE_SNAPSHOT;
  иначе вшитый snapshot + warn о дате. ~48 KB (~12K токенов) на старте при fetch.
- Тот же механизм переносим в 8C/8H/8N — см. `Live_UPDATE/INTEGRATION_SNIPPET.md`.
- (старый `gist_live_specs.md` в чанк-гисте больше не источник LIVE — deprecated.)

### Команда /p2p-download — полная интеграция (2026-06-27)
- Новая команда **`/p2p-download`** + пункт меню **[36]** (сразу после `/p2p-verify` [35]).
- Грузит ВСЕ 11 чанков разом (fetch + verify) → все пункты [1-42] работают без дозагрузок.
- Динамические модули сдвинуты [36-41] → **[37-42]**.
- COMMAND_CHUNK_MAP: `/p2p-download → ALL`. MUTEX-классы разные (по 1 чанку) → check_mutex не падает;
  загрузка ≠ активация (ограничения техник enforced при вызове, не при наличии в контексте).
- Требует web-fetch (~57K токенов); на LITE_ONLY → подсказка про ручную FULL-вставку.

### Архитектура (новое)
- **4-слойная модель** вместо плоского реестра v8H: L0 BOOT → L1 RESOLVER → L2 TRANSPORT → L3 GIST CLOUD.
- **FETCH_CAPABILITY gate** (`_preloader_v8L` БЛОК 0): детект web-fetch на старте →
  `LOAD_MODE = GIST_LAZY_FETCH | LITE_ONLY`. Честная деградация вместо галлюцинации чанков.
- **DEPENDENCY_RESOLVER** (`!!core_v8L §6` + `LAZY_FETCH_PROTOCOL_v8L`): транзитивное замыкание
  `requires` + dedup + MUTEX-чек ДО fetch.
- **Integrity verify**: каждый fetch проверяется тремя ступенями — EOF-маркер, **sha256**, размер ±15%.
- **`_index_v8L`** расширен от «URL-таблицы» до полного **контракта чанка**
  (`trigger·url·sha256·size·requires·mutex·fallback`).

### Нарезка чанков (по co-load-частоте + MUTEX, не по теме)
- `gist_core_plus` ← agents + pipeline (склейка — всегда co-load).
- `gist_session` ← toolkit+scope+memory+metrics+sandbox.
- `gist_security` / `gist_compress` / `gist_route` ← **расклеен бывший монолит gist_10**
  (разные MUTEX: GUARDIAN_ON / single_compressor / scope_cascade).
- Остальные: vendors, host_engine, reasoning, optimization, rag, live.

### Исправления (по ревизии QUORUM + реальный packaging)
- **D1** — gist_10 нельзя было держать одним чанком (3 конфликтующих MUTEX) → расклеен.
- **D2** — `OPTIMIZATION`/`RAG` тянут транзитивно `SESSION`+`CORE_PLUS` (а не «один чанк 3.5K»).
- **D4** — добавлен реальный **sha256** на каждый чанк (EOF-маркер ловит лишь усечение, не подмену).
- **packaging-фикс** — `gist_live_specs` оказался **80.5 KB** (~20K токенов). Eager-load убил бы
  lite-вес → переведён в **lazy**; дедлайны/флагманы обслуживает `!!db_v8L §0 LITE_SNAPSHOT` (0 fetch).
- **DATOS** — `gist_host_engine` реально 16.7 KB (занижение ×3 в исходном миндмапе подтвердилось).
- **verify-bug** — `verify_v8L.sh` ловил хеш соседнего чанка (`grep -A1`) → исправлен.

### Инструменты
- `pack_v8L.sh` — детерминированная сборка чанков из исходников v8H.3 + sha256 + `chunk_manifest.json`.
- `verify_v8L.sh` (`/p2p-verify`) — Manifest Reconciliation: сверка sha256 + EOF-маркеров. **11/11 PASS**.

### Реальные размеры (chunk_manifest.json, 2026-06-27)
- idle (BOOT, 4 файла): **73 KB ≈ 18K токенов** (лучше прежней оценки ~33K).
- active QUORUM: +21.6 KB · optimize (транзитивно): +72.9 KB · full arsenal (11): ~227 KB ≈ 57K т.
- Честная вилка: **~18K idle / ~25-40K active**. Никаких «-86% всегда».

### FIX D5 — SESSION split (2026-06-28)
- `gist_session.md` (45.9 KB, ~11.5K т.) разделён на:
  - **`gist_session_core.md`** (40.0 KB, ~10K т.) — toolkit+scope+memory+sandbox
  - **`gist_session_metrics.md`** (7.1 KB, ~1.8K т.) — metrics+quality eval ✅ под ceiling
- `OPTIMIZATION` теперь требует `SESSION_METRICS + CORE_PLUS` вместо `SESSION + CORE_PLUS`.
- Экономия при optimize: ~36 KB (~9K токенов) — с ~72.9 KB до ~35 KB.
- Обновлены: `_index_v8L.md` (контракты, DEPENDENCY_MAP, MUTEX, SIZE_NOTES), `!!core_v8L.md` (меню, COMMAND_CHUNK_MAP).

### Открытые вопросы
- Хостинг Gist: public (открытая IP) vs private+token vs обфускация — **решение за пользователем**.

### FETCH_CAPABILITY_GATE → активная канарейка — 2026-06-27 (эмпирика)
- **Находка:** Gemini Pro chat РЕАЛЬНО умеет web-fetch (вернул точные EOF-маркеры gist_route/gist_compress).
  Ранее ложно определялся как LITE_ONLY.
- **Корень бага:** пассивная проверка «есть ли инструмент» + фраза-выход «если не можешь, скажи
  CANNOT_FETCH» → модель шла по пути наименьшего сопротивления (false negative).
- **Фикс:** гейт стал АКТИВНЫМ — дёргает `FETCH_CANARY` (`_index_v8L`) и сверяет ответ с эталоном
  БЕЗ фразы-выхода. Несовпадение ловит и лень, и галлюцинацию. Затронуто: `_preloader` БЛОК 0,
  `LAZY_FETCH_PROTOCOL` STAGE 0, новый `FETCH_CANARY` в `_index`, команда `/p2p-fetch-test`.
- **Следствие:** на Gemini v8L.3 работает в полном GIST_LAZY_FETCH (меню легитимно полное).

### Универсальность хоста (как 8N.3) — 2026-06-27
- v8L.3 объявлен **UNIVERSAL** edition: не привязан к Claude, как и Normal-редакция 8N.3.
- `_preloader_v8L`: `HOST_MODEL` теперь **нейтральный** (пусто → система спрашивает хост на старте,
  8 вариантов), а не дефолт `claude`. Добавлена `SELECT_HOST_FETCH_MATRIX` (fetch-способность по хостам).
- `HOST_DETECT_BRIDGE`: восстановлен `ENV_GEMINI_STUDIO` (не только claude/api/chat).
- `!!core_v8L`: добавлен `/host` handler; стартовый баннер показывает `HOST · XML · Agents · MODE`.
- Новая команда `/host <model>` — смена хоста на лету (8 моделей).
- `AGENT_PATH`: claude/grok+plugin → нативные sub-agents; любой другой хост → QUORUM из CORE_PLUS chunk.
- `plugin.json` description: universal any-host; XML только при host=claude.

### Совместимость
- `claude-fable-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-sonnet-4-6` (+ haiku-4-5, opus-4-6 pin).
- ACTIVE дедлайн 2026-07-24: `deepseek-chat`→`deepseek-v4-pro`, `deepseek-reasoner`→`deepseek-v4-flash`.

// EOF_MARKER_CHANGELOG_V8L3_VALIDATED

