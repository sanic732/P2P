# CHANGELOG — P2P (Prompt-to-Prompt)

Формат — [Keep a Changelog](https://keepachangelog.com/ru/1.1.0/), версионирование — по поколениям архитектуры P2P (v1 → v8).

> **Историзация:** записи v1–v7 и v8 .1/.2 помечены `(backfilled)` — это **историческая реконструкция** по форумным постам 4PDA и архивным файлам (`old_version/`). Даты приведены как в первоисточниках; **git-коммиты задним числом не создаются** (решение 2026-06-19). Подробные описания — `legacy/v*/DESCRIPTION.md`, нарратив — `legacy/HISTORY.md`.

---

## [v8.4.3] — 2026-07-13 · UNRELEASED (Cowork) — Live Specs v8.6.3 + host-detect fix + Grok knowledge + Agent Skills + канон ошибок

### Added
- **Agent Skills генератор (`!skills.md`, E1):** новый ON-DEMAND модуль в **C(for-chat)/H/N** — генерирует `SKILL.md` по стандарту agentskills.io (frontmatter-правила name/description, progressive disclosure, description-валидатор, анти-паттерны, таргеты Grok/Claude/Cursor/Codex). Пункт меню **[42]** (H/C) / **[32]** (N, EXTENSIONS_SCAN-гейт) + команда `/p2p-skill`. **Lite — намеренно без skills** (решение Master).
- **Grok target-слой (E3):** `vendors/grok.md` (grok-4.5/4.3, G14 safe-params) в **C/N**; секция `GROK_JSON_TARGET` (строгий JSON envelope + `json_schema strict:true` + Type H guard) в contract-модулях. Полный Heavy-16 пак остаётся High/Light-эксклюзивом.
- **`docs/GROK_HOST_GUIDE.md` (E4, High):** Grok Build CLI (install/device-auth/headless), grok.com (нативные агенты, Agent Skills), offload-подводный камень.
- **`editions/G_ERRORS_CANON_AUDIT_8.4.3.md` (E6):** отчёт-diff аудита реестров ошибок.

### Changed
- **Live Specs → v8.6.3 (E2):** во всех 4 сборках (H/C/N + L через Gist; L-заливка отложена до `gh auth login`). Grok 4.5 GA 2026-07-08, GPT-5.6 GA, Fable 5 #1 Overall.
- **⭐ Интеграция Live Specs в BASE (Code-ревизия 2026-07-14):** Cowork только ПОДМЕНИЛ live_specs, но НЕ перенёс данные в BASE-файлы (застряли на 06-12). Приведены к канону 2026-07-13 во всех 4 сборках: `tier1-4`, `live_vendors`/`_live_specs`, `live_claude`/`_live_claude`, `MANIFEST`/`_live_manifest`, db-реестры (`!!db_v8x` §API_STRINGS), L-монолит `!!db_v8L`/`!!core_v8L`. Добавлены: Sonnet 5, GPT-5.6 Sol/Terra/Luna, Grok 4.5, GLM-5.2, Kimi K2.7 Code, Mythos 5; ретайр Sonnet 4.6; снят ложный «Fable 5 SUSPENDED». **⚠ Пред-баг H исправлен:** Claude context 200K→1M, Opus 4.x $15/$75→$5/$25. Логика/паттерны/G-errors-каталог не тронуты. Карта размещения данных + audit-скрипт → `_SERVICE/`.
- **Дубль `vendors/grok.md` удалён (Code-ревизия):** в **C** (обе формы) и **N** — Grok уже в tier2/tier3; ссылки (`!!core`/`_index`/`_master`/`!contract`/`contract_builder`/`!pipeline`) → tier2/tier3. В **H** `grok.md` сохранён (легитимный host-профиль).
- **✂️ live_specs → ДЕЛЬТА (2026-07-14): 91849 → 31061 б (−66%), токены 31351 → 10614.** Реализован 2-слойный контракт из `_SERVICE/LIVE_SPECS_DATA_MAP.md`: стабильные спеки моделей живут в BASE (`vendors/tier*`, `live_vendors`, `db`), а live_specs несёт только волатильное — CRITICAL_DELTA, UPCOMING_DEADLINES, USER_SANDBOX, per-vendor `CHANGES`, активный `ERROR_REGISTRY`, weekly `ARENA`, `MEDIA_MODELS`, `CHANGES_LOG`. Раскатано на канон + 4 embedded (все идентичны, sha `3190449145d6`) и залито в оба gist (LIVE `a64245c3` + арсенальный); новый revision арсенала `cfc670a8…`, канарейка/CORE_PLUS в `_index_v8L` перепиннуты, `size_kb: 90→30`. **Эффект:** в наборах H/N live_specs 27 800 → 10 600 токенов.
- **📊 `ЧТО_ЗАГРУЖАТЬ.txt` (C/H/N) пересчитан реальным токенайзером** (o200k / gpt-tokenizer) по фактическим файлам: H минимум 32 000→**34 400** (на Grok 35 000→**38 600**), N 27 000→**29 200**, C **28 400** (+ исправлен заголовок «8.4.2-C»→8.4.3-C); добавлен `!skills.md`.
- **🔴 Фиксы фактических ошибок в docs (C/H/N):** неверный маппинг DeepSeek `chat→v4-pro` → **`chat`/`reasoner`→`v4-flash`** (live_specs: «NOT to V4-Pro»), дедлайн уточнён `24.07 15:59 UTC, no grace`; `qwen3-plus`→`qwen3.6-plus`; `glm-5.1-flash`→`glm-5.2`/`glm-5.1`.
- **🔴 `vendors/grok.md` (H) — исправлена атрибуция:** Heavy-16 и 2M приписывались `grok-4.3` → разделено на `grok-4.5` (500K, ⚠ не EU) · `grok-4.3` (1M) · `grok-4.20` (2M, Heavy-16) · `grok-build-0.1`. В H файл остаётся легитимно (от него зависит `!grok_heavy.md`); в C/N удалён как дубль tier-данных.
- **🗑 BREAKING — плагинная форма 8L.3 УДАЛЕНА (2026-07-14):** `editions/8.4.3-L/plugin/` (27 файлов) + бандл `p2p-v8l3.plugin` удалены навсегда. Причина: команды/скиллы Lite-плагина пересекались с 8C.3 → при установке обоих плагинов в Claude Code происходило взаимное «заражение» одноимёнными файлами. **8L.3 теперь только файловая сборка:** `boot/` (4 файла) + `docs/`. Для Claude Code/Cowork → **8C.3 (`p2p-v8c3`)**; плагин в репо теперь ровно один. Ссылки починены в README(.en)/INSTALL/docs/RELEASE_CHECKLIST; `marketplace.json` не трогали (`p2p-v8l3` убран оттуда ещё в 8.3.9).
- **⭐ 8L.3 BOOT: форсирование fetch + компрессия −52% (Antigravity-пасс 2026-07-14, лог реконструирован):** прежние правки L дали побочку — Gemini сразу отказывался («нет fetch»). Фикс: **режим `LITE_ONLY` удалён** (вместе с `FETCH_HONESTY`/P8 и `DECLINE`-fallback), `FETCH_CAPABILITY_GATE.JUDGE` сделан безусловным, все 8 хостов → `GIST_LAZY_FETCH ✓`; добавлены `NO_OFFLINE_ILLUSION` (ЗАПРЕЩЕНО «OFFLINE/SKIPPED/ограничения сессии»), форс-инструкция в `/p2p-verify`, класс ошибки `R. Refusal/Laziness`. Автодетект хоста (E5) → явный вопрос [1..8]. BOOT сжат ~87→~42 KB (−52%). **Итог: fetch работает на claude/gemini/gpt/grok/deepseek/qwen.** ⚠ Побочно утрачена честная деградация (риск фабрикации чанков на хосте без реального fetch) — см. `_SERVICE/CHANGELOG.md`.
- **L Gist-слой → v8.6.3 (E2-L ЗАКРЫТ, 2026-07-14):** LIVE gist `a64245c3` → v8.6.3; арсенальный gist `7727406` (`gist_vendors`/`gist_host_engine`/`gist_live_specs`) → канон; новый revision `85411b2f`; `_index_v8L` канарейка + CORE_PLUS перепиннуты (gist_route не менялся, sha256 валиден). Заливка через `gh gist edit` (git push блокируется sandbox).
- **Host-detect fix (E5, H/N/L `_preloader` БЛОК 0):** `NORMALIZE` HOST_MODEL (lowercase + синонимы grok), `ENV_SIGNALS` (HIGH при неуверенном self-name), заметный `HOST_PICK_LIST` fallback, `PERSIST`, хинт `/host grok`. **C — Claude-only, не трогали.**
- **Канон ошибок (E6):** `Type Q — L-OPTICAL` синхронизирован в обе C-формы (было только в plugin-эталоне); заголовки «Type A–P» → «Type A–Q».
- **Bump 8.4.2 → 8.4.3:** каталоги `editions/8.4.3-*`, `plugin.json` (C/L), `marketplace.json` source/description, README редакций.

### Deferred (требует `gh auth login`, делает Master/Claude Code)
- ~~Заливка live_specs v8.6.3 в Gist `a64245c3f824f45708519d57e0d62408` (E2-L).~~ ✅ ВЫПОЛНЕНО 2026-07-14 (+ арсенальный gist + re-pin канарейки).
- Пере-упаковка архивов, ветка + PR, push (BASE-правки в `new_version` ещё не запушены). См. `HANDOFF_8.4.3_для_Claude_Code.md`.
- (опц.) live_specs trim 91KB→дельта — файл регенерируется апстримом, durable-фикс = политика в `_SERVICE/LIVE_SPECS_DATA_MAP.md §4`.

## [v8.4.2] — 2026-07-07 · UNRELEASED — pxpipe refusal-фикс + docs 8C.3 + YAML-шапки light + rename папок

### Added
- **8C.3: полный набор документации в `editions/8.4.2-C/docs/`** (раньше — только PXPIPE_GUIDE): `README.md` (навигатор + выбор формы поставки), `INSTALL_GUIDE.md` (обе формы: Code/Cowork плагин И Chat/Projects for-chat), `FAQ_И_ОШИБКИ.md` (FAQ + ошибки E1–E8: префикс `/p2p-v8c3:`, Code≠Cowork, YAML strict, pxpipe…), `AGENTS_GUIDE.md` (QUORUM: ростер, запуск, паттерны, веса, VETO).
- **`ЧТО_ЗАГРУЖАТЬ.txt` в трёх сборках** (`8.4.2-C/for-chat/docs/`, `8.4.2-H/docs/`, `8.4.2-N/docs/`) — простой текст без markdown: обязательный минимум (C: 6 файлов ~28K т.; N: 6 файлов ~27K; H: 8 файлов ~32K, +1 на Grok) и пронумерованный список всех остальных файлов с токен-оценками (gpt-tokenizer по реальным файлам) и описаниями. Закрывает постоянный вопрос пользователей «какие файлы обязательны и сколько это токенов». Ссылки добавлены в docs/README (H/N) и INSTALL_GUIDE/README docs (C).

### Fixed
- **🚨 8C.3 pxpipe: safety-refusal у Fable 5 на одиночных PNG** (live-трафик, `events.jsonl`): профиль «1 PNG со static-слэбом ~16k симв + почти без текста» (headless `claude -p`) флагается ~70% (5/7) — `stop_reason: refusal`; multi-PNG чист (15/15). Фикс: **`PXPIPE_MIN_COMPRESS_CHARS=24000`**; upstream pxpipe-proxy v0.8.0 ручки не имеет → задокументирован патч transform-фабрики в `dist/node.js` (перезатирается `npm install`). Обновлены `PXPIPE_GUIDE.md`, `commands/p2p-pxpipe.md` (алгоритм `on`: npm/npx вместо устаревшего pnpm build), `skills/pxpipe/VERIFICATION.md`.
- **🔴 8L.3: YAML-шапки плагина** (хвост, отмеченный в 8.4.1): 14 команд без `description` (добавлен из `scope`) + `p2p-karpathy.md` с незакавыченным `: ` (ронял парсер Claude Code). 15 файлов проверены pyyaml.

### Changed
- **Bump плагинов `8.4.1 → 8.4.2`** (`p2p-v8c3`, `p2p-v8l3`) — триггер кнопки Update.
- **Каталоги редакций** `editions/8.4.1-{C,H,N,L}` → **`editions/8.4.2-{C,H,N,L}`** (папка = номер релиза); обновлены `marketplace.json → source`, корневые README (ru/en), COMPARISON.md, README редакций, skill p2p-release.

---

## [v8.4.1] — 2026-07-07 · pxpipe optical compression (8C.3) + rename редакций (запись восстановлена)

> Запись добавлена задним числом 2026-07-07 (релиз ушёл без строки в корневом CHANGELOG).

### Added
- **⭐ 8C.3: pxpipe** — оптическое сжатие токенов (текст → плотный PNG; vision-биллинг по площади пикселей; **только Fable 5**): слой L-OPTICAL (compression), PXPIPE_GATE (хендофф QUORUM/CAPSULE), команда `/p2p-pxpipe` + skill `pxpipe` (compress/measure/byte-guard). Замеры: ~82% экономии на блок; прокси — 53% холодный / 93.5% тёплый ход. Гейты: READER (Fable 5/GPT-5.6), PROFIT (≥8k симв), BYTE-GUARD + DECISION LEDGER. Атрибуция: [teamchong/pxpipe](https://github.com/teamchong/pxpipe) (MIT), DeepSeek-OCR (arXiv 2510.18234).
- Релиз [v8.4.1](https://github.com/sanic732/P2P-4PDA-edition/releases/tag/v8.4.1): 4 zip-ассета + `p2p-v8c3.plugin` (бандл дозалит 2026-07-07).

### Changed
- **Каталоги редакций** `editions/{claude-native,high,normal,light}` → `editions/8.4.1-{C,H,N,L}`; Fable 5 / Opus 4.8 в `compatibility.models`; displayName «8.4.1-C».

### Known issues
- ⚠️ git-тег `v8.4.1` указывает на коммит `ff34c27` (06.07, БЕЗ pxpipe) — merge pxpipe (`b733548`, PR #38) произошёл после создания тега → авто-ассеты «Source code» релиза не содержат pxpipe. Zip-ассеты собраны из правильного состояния.

---

## [v8.3.9] — 2026-06-28 · SESSION split (8L.3) + light → local-only + bump доставки

### Changed
- **Маркетплейс `P2P-4PDA-edition` теперь содержит только `p2p-v8c3`** (8C.3 Claude Native). Плагин **`p2p-v8l3` (8L.3) убран из `marketplace.json`** — отныне доступен **только локальной установкой** через `.plugin`-бандл (релиз-ассет `p2p-v8l3.plugin`). Существующие маркетплейс-инсталляции 8L.3 при синке станут orphaned — это намеренно.
- **Bump обоих плагинов `8.3.8` → `8.3.9`** (`p2p-v8c3`, `p2p-v8l3`) — строгий SemVer, триггер кнопки **Update** в Claude (доставка SESSION-сплита и for-chat фикса).

### Fixed
- **🔴 SESSION-чанк превышал token-ceiling (8L.3, FIX D5).** Монолит `gist_session.md` (45.9 KB, ~11.5K т.) разрезан на **`gist_session_core.md`** (40.0 KB — toolkit+scope+memory+sandbox) и **`gist_session_metrics.md`** (7.1 KB, ~1.8K т. — metrics+quality eval). `OPTIMIZATION` теперь тянет только `SESSION_METRICS + CORE_PLUS` вместо всего SESSION → экономия при optimize ~36 KB (~9K токенов). Обновлены контракты в `_index_v8L.md` (routing table, DEPENDENCY_MAP, MUTEX_MATRIX, SIZE_NOTES, VALIDATION_CHECK), меню и `COMMAND_CHUNK_MAP` в `!!core_v8L.md`, ссылка в `!!db_v8L.md`.
- **for-chat 8C.3:** исправлен YAML-frontmatter `!!core_v8C.md` — добавлен открывающий `---`, убран таб перед `source_id`.

---

## [v8.3.8] — 2026-06-27 · фикс live_specs OVERRIDE + bump доставки

### Fixed
- **🔴 Битая ссылка live_specs OVERRIDE (все редакции).** Загрузчики/манифесты (`_preloader`, `_index`, `_live/MANIFEST`, `_master`, `_live_specs`) ссылались на переименованный (коммит `b491bf8`) файл `live_specs_20260617.md`, которого больше нет → актуальный `live_specs.md` (v8.6.1) грузился по правилу «при наличии» и **молча пропускался**. Перенаправлено на `live_specs.md` (31 файл; исторические CHANGELOG не трогались). Версия-метки рядом со ссылками: v8.4/v8.5 → v8.6.1.
- **Light `_index_v8L`:** актуализирован пин модульного gist в шапке (`rev fdfe1e1` → `6d80f15f`); фактический fetch уже шёл на `6d80f15f`. sha256 anti-tamper сверен с живым gist — совпадает (`984c8c53…`).

### Changed
- **Bump обоих плагинов `8.3.7` → `8.3.8`** (`p2p-v8c3`, `p2p-v8l3`) — триггер кнопки **Update** в Claude (доставка фикса live_specs пользователям).

---

## [v8.3.2-ALPHA] — 2026-06-22 · скиллы Cowork + новые скиллы + fallback live_specs

### Added
- **5 готовых скиллов** в `editions/claude-native/plugin/.claude/skills/`: `bb4pda` (BB-разметка 4PDA), `rag-prep`, `rag-grounding`, `rag-router`, `notebook-pack` — формат `name`/`description` (Cowork-совместимы, авто-дискавери через `"skills": "./.claude/skills"`).
- **Скилл-обёртка `p2p-quorum`** (`skills/p2p-quorum/SKILL.md`) — тонкий триггер с делегированием в `skills/p2p/core.md` + `agents.md`, чтобы `/p2p-quorum` регистрировался как скилл в **Cowork** (команды ≠ скиллы). Логика не дублируется.
- **Fallback `live_specs_20260617.md`** возвращён в `skills/p2p/vendors/` — на случай недоступности fetch-загрузки live-спеков (основной путь — онлайн-fetch).
- Сопутствующий BB text-prompt → `docs/`.

### Changed
- **Бамп версии плагина `8.3.1` → `8.3.2-C`** (cloud `p2p-v8c3`, в корневом и вложенном `marketplace.json` + `plugin.json`) — чтобы у уже установивших Claude показал «update available». Буква редакции `C` — semver-валидным суффиксом (как `-L` у light), major остаётся числовым. Light `p2p-v8l3` без изменений (`8.3.1-L`) — лёгкая редакция, локальные скиллы ей не нужны.

---

## [v8.3.1-ALPHA] — 2026-06-19 · публикация монорепо + фикс обновления

### Added
- Опубликованы **все 4 редакции** в монорепо `editions/*` и в релизе `v8.3-alpha` (Latest): 8C.3, 8H.3, 8N.3, 8L.3.
- Релиз-ассеты разнесены по форме поставки: `p2p-8C.3-for-chat.zip` + `p2p-8C.3-cowork-code.zip` (вместо одного combined), `p2p-high-8H.3.zip`, `p2p-normal-8N.3.zip`, `p2p-light-8L.3.zip`, `p2p-v8c3.plugin`, **`p2p-v8l3.plugin`** (новый — плагин-форма light).

### Changed
- **Бамп версии плагинов `8.3.0` → `8.3.1`** (cloud `p2p-v8c3`) и `8.3.0-L` → `8.3.1-L` (light `p2p-v8l3`) — чтобы Claude Code корректно показал «update available» после реструктуризации (имя `p2p-v8c3@p2p` стабильно, обновление прозрачно).
- `marketplace.json`: `source` плагина `p2p-v8c3` переведён с `./cowork + code` на `./editions/claude-native/plugin` (без пробелов); добавлен второй плагин `p2p-v8l3` (`./editions/light/plugin`).

### Fixed
- Ссылка на архивный репозиторий в истории: `P2P-main` → `P2P` (реальное имя репо).

---

## [v8.3-ALPHA] — 2026-06 · «NEXUS» (.3)

### Added
- 4 редакции одной архитектуры: **8C.3** (Claude Native), **8H.3** (High \ Hybrid = слияние Gemini-A ⊕ Grok-G), **8N.3** (Normal/Universal), **8L.3** (Lite/Live).
- **PILOT** — ось уровня помощи (Co-Pilot / Auto-Pilot / Manual + GLASS COCKPIT); **SHERPA** — проводник по фичам среды.
- 6 ON-DEMAND модулей: `!rag` · `!reasoning` · `!routing` · `!compression` · `!security` · `!optimization` (RAPTOR/LongRAG, Self-Consistency/MCTS/s1, Cost-Aware routing, LLMLingua/Gist, SelfCheckGPT, OPRO/APE/EvoPrompt).
- **VERSION_COMPAT** + CONFLICT_RESOLVER v1.0; арт-меню (ASCII-баннеры); **Claude Fable 5** как T4-модель.
- Live specs от 17.06.26 интегрированы во все редакции; переход на **base-model идентификаторы**.

### Changed
- Манифесты `p2p-v8c2` → `p2p-v8c3` (`8.2.0` → `8.3.0`).
- 8L.3: 4 BOOT-файла (~18-22K токенов) + ленивая online-подгрузка арсенала по триггеру.

> Все 4 редакции опубликованы в монорепо `P2P-4PDA-edition` — см. запись `v8.3.1-ALPHA` выше.

---

## [v8C.2] — 2026-05-14 (backfilled) · «NEXUS» (.2)
🔗 [Обновление P2P для Claude → 8C.2](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143383283)

- Claude Native Edition: XML-ядро, cowork-code + for-chat, 8 агентов QUORUM, SCOPE.HELM.
- Параллельные ветки поколения .1/.2: **8A.1** (Gemini AI Studio, ZERO XML — обход G2; Memory Bridge против G13), **8G.1** (Grok Native — Heavy-16, X Firehose, Tool Budget), **8N.1** (Universal — HOST_PROFILE_LOADER, защиты G15/G18/G19/G20). См. `legacy/v8-pre/`.

---

## [v1.1-EN] — 2026-04 (backfilled, archived) · публичный EN-релиз
🔗 Архивный репозиторий (read-only): https://github.com/sanic732/P2P

- Первый публичный релиз на GitHub. **Внутренняя версия v7C.2** (поколение CORTEX), English-only.
- Переименование агентов: `ANON → FORGE`, `KSENIA → LYRA`; команда `/lang` (EN/RU).
- Без слома совместимости с v1.0 (=внутр. v7C.1). → судьба: **архив + ссылка** (см. `03a_NAMING_DECISION.md`).

---

## [v7] — 2026-03 → 2026-04 (backfilled) · «CORTEX»
🔗 [SCOPE.HELM v1.0](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142654977) · [CORTEX Patch 001](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142550801)

- Редакции FULL / NORMAL / LITE; ветки 7A.1 (AI Studio), 7C.1/7C.2 (Claude), 7N.1, 7L.
- **SCOPE.HELM v1.0** — pre-work движок больших сессий (SPLITTER → ROUTER → CAPSULE).
- **CORTEX Patch 001** — три недостающих контура ядра. 8 агентов, 38 техник, 16 типов ошибок (A-P), 11 шаблонов.

---

## [v6] — 2026-02 → 2026-03 (backfilled) · «LEGION»

- **Domain Knowledge Layer** (React 19, Kotlin); **NotebookLM Bridge v1.0 STABLE**; **Cross-Pollination Directive**.
- **Tier 4 (Frontier)** с обязательным QUORUM; 4 техники DeepSearch (GO_SLOW, CLAUDE_MD, LLM_COUNCIL, SAFE_THINKING); **ROUTING_FORMULA_PROTOCOL v1.0**.
- Сборки 6.0 / 6.1_fix / 6.3_fix2 (Ядро+БД).

---

## [v5.5–5.9] — 2026-02-15 (backfilled) · «CHIMERA»
🔗 [P2P CORE v5.5 «CHIMERA» — релиз](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=141969850) · 📜 [DevLog ч.2](https://4pda.to/forum/index.php?showtopic=1077922&view=findpost&p=142005543)

- Переход от монолита к модульной «Химере». Трёхслойная база знаний; ссылки-якоря `#DB_LINK_XXX`; правило свежести 90 дней.
- Линия 5.3 → 5.5 → 5.7 → 5.9 STABLE. Начало «ОС внутри промпта».

---

## [v4.0–4.1] — 2026-01 → 2026-02-16 (backfilled) · «Constraint Prompting»

- Парадигма **Constraint Prompting** (границы+цели вместо CoT для reasoning-моделей, +30-40% качества).
- Трёхслойная архитектура (Static/Dynamic/Empirical); **DoD Security**; **Chain of Prompts** (Research→Draft→Review→Polish); **Library Anchor Protocol**.

---

## [v3.2] — 2025-12 (backfilled) · «Dynamic Lab»
📜 [DevLog ч.1](https://4pda.to/forum/index.php?showtopic=1077922&view=findpost&p=140958693)

- Архитектура **Dynamic Lab**: разделение логики (Core) и данных (Knowledge Base).
- Динамическая инъекция знаний; валидация авто-адаптируется под модель (XML/Markdown/CoT); модуль анти-галлюцинаций.

---

## [v2] — 2025-11 (backfilled)

- Коллекция системных промптов под каждую LLM (GPT/Gemini/Claude/DeepSeek/Grok/Qwen/Kimi).
- Уровни строгости Simple / Pro / System; встроенные чек-листы валидации.

---

## [v1] — 2025-10 (backfilled) · «Prompt to create prompts»

- Первый мета-промпт: один англоязычный текстовый промпт (intake GOAL/CONTEXT/FORMAT → дизайн → чек-лист оптимизации). Исток проекта.
