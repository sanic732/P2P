---
id: changelog_v8L3
version: v8L.3
type: DOC
last_verified: 2026-07-14
---

# CHANGELOG — P2P v8L.3 (Lite/Live Hybrid)

> Ветка миграции из **v8H.3** (30-файловый монолит) в **Resolver-Gated Lazy Hybrid**:
> 4 локальных BOOT-файла + 11 lazy Gist-чанков, загружаемых по триггеру через
> dependency-resolver с проверкой целостности sha256.

## [8.4.3-L] — 2026-07-14

### ⭐ Единый режим `GIST_LAZY_FETCH` (убран `LITE_ONLY`)
Прежняя двухрежимная схема (`GIST_LAZY_FETCH | LITE_ONLY` с «честной деградацией») давала
**побочный эффект**: модели читали описания LITE_ONLY и **сразу отказывались** от сетевых
вызовов («нет инструмента fetch») — ярче всего на Gemini. Решение: убрать режим и все его
упоминания; система всегда использует веб-доступ хоста.
- `LITE_ONLY` удалён из `_preloader`/`_index`/`!!core`/`!!db`; `FETCH_CAPABILITY_GATE` безусловный.
- `SELECT_HOST_FETCH_MATRIX`: все 8 хостов → `GIST_LAZY_FETCH`.
- Добавлены `NO_OFFLINE_ILLUSION` (`!!core`), форс-инструкция в `/p2p-verify`, класс ошибки
  `R. Refusal/Laziness` (`!!db`) — против «ленивых» отказов.
- **Проверено 2026-07-14:** fetch отрабатывает на claude · gemini · gpt · grok · deepseek · qwen.
- 📌 **Рекомендация пользователю:** после выбора хоста **сначала `/p2p-verify`**, и только после
  успешного отчёта — работа. Не прошло → включить инструмент веб-доступа в настройках хоста.

### Компрессия BOOT ~87 → ~42 KB (−52%)
Вырезаны пояснительные комментарии, CONTRACT SCHEMA, псевдокод резолвера, SIZE_NOTES,
VALIDATION_CHECK, MIGRATION-заметки. Человекочитаемая документация — только здесь, в `docs/`.

### Live Specs v8.6.3 + актуализация канона
- `LITE_SNAPSHOT` (`!!db §0`) и `§API_STRINGS` → канон 2026-07-13: **Sonnet 5** (default Free/Pro),
  **GPT-5.6** Sol/Terra/Luna, **Grok 4.5**, **GLM-5.2**, **Kimi K2.7 Code**, Mythos 5 (не маршрутизируется);
  `claude-sonnet-4-6` — RETIRED 30.06 (убран из активных строк).
- Дедлайны: 19.07 (Fable 5 → usage credits) · 24.07 15:59 UTC (deepseek-chat/reasoner → 404, no grace) · 31.08 (Sonnet 5 → $3/$15).
- host-PROFILE (`!!core §1`) → канон: claude 1M + `{"type":"adaptive"}`; gemini 2M; gpt 1.05M;
  grok 500K/1M/2M (4.5/4.3/4.20, ⚠ 4.5 не в EU); deepseek 1M; qwen 1M; kimi 256K-1M; glm 1M (5.2)/~120K (5.1).
- LIVE gist обновлён до v8.6.3; канарейка + CORE_PLUS перепиннуты на revision `85411b2f`.

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

### Открытые вопросы
- ⚠ `SESSION` 45.9 KB (~11.5K т.) превышает VECTOR-ceiling ≤6K токенов/чанк → кандидат на сплит
  (выделить metrics-only под-чанк). Отложено: +1 fetch round-trip.
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

