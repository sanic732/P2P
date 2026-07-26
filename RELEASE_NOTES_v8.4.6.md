# P2P v8.4.6 — Обновление модель-данных, техники 8.4.4 в chat-форме, одна версия на сборку


---


Три больших блока: **актуализация данных о моделях** (Opus 5 как основная, две новые записи
в каталоге ошибок, пересмотр цен и миграций), **выравнивание Claude Edition** (техники релиза
8.4.4 наконец доступны и в чат-форме, `/p2p` с задачей больше не открывает меню) и **приведение
версий в порядок** — из-за их расхождения пункты меню Normal `[26-32]` не открывались никогда.

### Модели и данные — во всех сборках

- **`claude-opus-5` — основная модель** (1M/128K, $5/$25, thinking включён по умолчанию).
  Добавлены `gemini-3.6-flash` (1M/65K, $1.50/$7.50, ~304 tok/s), `gemini-3.5-flash-lite`
  ($0.30/$2.50), `kimi-k3` (Arena WebDev #1) — последний с меткой **ACCESS-RISK и не назначается
  основным**: hosted-only, подписки закрыты, весов нет. В Normal также `qwen3.7-plus`,
  `qwen3.6-35b-a3b`, в Claude — `kimi-k2.7-code-highspeed`.
- **Fable 5 выведен из автоматической маршрутизации** — с 20.07 тарифицируется по usage credits,
  вызывается только явно. Его долю (35 % в задачах кода и рассуждений) занял `claude-opus-5`.
  `claude-opus-4-8` остаётся доступным: пропал из селектора интерфейса, но не из API.
- **Две новые записи в каталоге ошибок:** **G21** — несовпадение заявленной и фактической модели
  (сверять `resolved_model_slug`, у Anthropic смотреть блок `{"type":"fallback"}`); **G22** —
  агентная опасность GPT-5.6 Sol. В Lite обе внесены в быстрый справочник.
- **Automatic Fallbacks** в профиле Claude: параметр, beta-header, наблюдаемый блок ответа,
  `usage.iterations`, расщепление биллинга и как отключить.
- **Токенизатор Claude:** канон **~+30 %** — одна официальная цифра вместо вилки «+10-35 %»,
  плюс Token Counting API как способ считать точно.
- **Сроки снятия:** 05.08 (Opus 4.1), 26.08 (Assistants API, включая Azure), 31.08, 10.10.

### Исправления в данных

- **Правило миграции DeepSeek было перевёрнуто:** бывший `deepseek-reasoner` идёт на **v4-pro**,
  а не на v4-flash — официальный маппинг вёл на flash, и reasoning на нём тихо деградировал.
  Алиасы мертвы с 24.07 (404 либо 400 — считать оба), линейка V4 официально в статусе PREVIEW,
  но оставлена в маршрутизации: после снятия алиасов других путей нет.
- **Grok:** цена кэшированного ввода `$0.30` short / `$0.60` long вместо унаследованной `$0.50`;
  добавлен порог 200K, после которого тариф удваивается **вместе с кэшем**; `reasoning_effort`
  отключить нельзя. Доступ в EU открыт 21.07 — ограничение переформулировано с недоступности
  на персональные данные. Моделей `grok-4.5-heavy` / `-expert` / `-fast` не существует.
- **Длинный контекст:** ×2 на некэшированный ввод, ×1.5 на вывод, **кэшированный ввод
  не дорожает**; у xAI порог свой (200K) и кэш там дорожает тоже. Пороги вендоров общей формулой
  не описываются: xAI 200K против OpenAI 272K.
- **Цена GLM-5.2** помечена как неподтверждённая — единственный источник противоречит сам себе.
- **Qwen:** режим deep-thinking не поддерживает structured output; `qwen3.8-max-preview`
  не маршрутизировать — строгий JSON на нём структурно невозможен.
- **G13 на `gemini-3.6-flash`:** баг не тестировался, то есть модель не проверена, а не исправлена —
  обходные приёмы применять и к ней.

### Claude Edition

- **Техники релиза 8.4.4 теперь доступны и в chat-форме** — раньше они были только в плагине:
  VERBALIZED_SAMPLING и BRUTAL_EDITOR (`!writing.md`), GEPA и MASPO (`!optimization.md`),
  CONTEXT ENGINEERING (`!compression.md`), Context-Grounding CoT (`!reasoning.md`),
  POSITIVE_FRAMING (`!!db_v8C.md`). SePO внесена как backlog, без активации.
  Атрибуция (`docs/CREDITS_TECHNIQUES.md`, 6 arXiv-источников) тоже добавлена в chat-форму.
- **`/p2p <задача>` больше не открывает меню, а запускает разбор задачи:** SIR Scanner →
  определение сложности → Contract Builder. Меню вызывается голым `/p2p`, а также
  `start` / `старт` / `menu` / `меню`.
- **Правило кросс-модельной генерации:** если целевая модель не указана, TARGET = HOST;
  при HOST = TARGET = Claude контракт выдаётся в XML, а не markdown.
- **pxpipe: оптическое сжатие разрешено только для Fable 5.** GPT-5.6 убран из гейта вслед
  за автором pxpipe — на проверке точности модель не воспроизвела ни одного из четырёх
  идентификаторов и выдала четыре вымышленных. Обойти осознанно — флаг `--force`.
- **Меню плагина обрывалось на `[40]`** — пункты `[41]` и `[42]` были только в chat-форме.
  Теперь обе формы дают одинаковый ряд `[0]`–`[42]`. `[41] /p2p-download` показывается только
  там, где доступен web-fetch.
- Ссылка «SHERPA `[21]`» вела не туда (`[21]` — это CONSTRAINT REINJECTION) · в предписании
  оставалась снятая `claude-sonnet-4-6` · ссылки на отсутствующие в chat-форме файлы
  (`!exploration.md`, `!scope.md`, `!metrics.md`) вели в пустоту · `SKILL.md` объявлял 11 команд
  при 13 файлах · `VERSION_METADATA` в ядре плагина был обрезан на середине строки.

### Normal: меню `[26-32]` не открывалось никогда

Модули `!rag`, `!reasoning`, `!routing`, `!compression`, `!security`, `!optimization`, `!skills`
оставались заблокированными **при любых значениях флагов и при любом числе приложенных файлов**.
Детектор сверял номер версии в заголовке файла-модуля с версией ядра, а они разошлись.

Теперь показ пунктов гейтится флагом `MODULE_*` или сработавшим триггером. Промежуточный вариант —
детект по телу файла — проверен вживую и отбракован: он отдавал **25 пунктов из 32** при всех
включённых модулях. Правило, требующее от модели найти строку в другом документе контекста,
оказалось ненадёжным.

Страховка от выдумывания сохранена: если пункт выбран, а файла модуля в контексте нет, система
просит приложить файл и не сочиняет содержимое. Добавлен флаг `MODULE_SKILLS` — модулей семь,
а флагов было шесть. Подсказка в футере требовала приложить файл `!<module>.md` **буквально**,
с угловыми скобками; теперь подставляются настоящие имена. В трёх местах значилось «все 6»
и `[26-31]` при семи модулях.

### Версия: одна на сборку

Номер жил в двух несовместимых системах — внешней (`8.4.5-N`, каталоги и релизы) и внутренней,
унаследованной с форума (`v8N.4`). Они поднимались раздельно и расходились каждый выпуск. Именно
это и сломало меню Normal, а до того — заставило редакцию C представляться двумя версиями сразу.

- Номер выпуска живёт **только в YAML-шапке файла** и в трёх местах на редакцию, где его видит
  пользователь: логотип, шапка меню, строка статуса. В файлах C он раньше стоял до четырёх раз
  в одном файле.
- В самоопределении системы, напоминании об ограничениях и рамке ATLAS теперь стоит **серия** —
  `v8C` / `v8H` / `v8N` / `v8L`, она не меняется от выпуска к выпуску.
- `tools/bump_version.py` — следующий выпуск одной командой: 207 замен, переименование каталогов,
  `marketplace.json`, README редакций. Версию скрипт берёт из имён каталогов, а не с аргумента.

### История вынесена из рабочих файлов

Блоки «что нового в поколении», поля `SYSTEM` / `CHANGELOG` / `SOURCE` / `PREDECESSOR` /
`SECTIONS`, даты правок и метки вида `[v8C.3]` — **612 строк**. Всё это описывало прошлое
и грузилось в контекст модели при каждом запуске; содержательная часть перенесена в CHANGELOG
редакций. Блок метаданных в конце файла переименован в `FILE_META` — версии в нём больше нет.

Сборки легче на 1,5–2,6 % (≈2000–2500 токенов при полной загрузке), BOOT Lite — на ~250 токенов.

### Lite: арсенал пересобран и разрезан

Lite тянет модули чанками из gist. Прежние чанки собирались 27.06–13.07: внутри стояла версия
`v8H.3`, не было `claude-opus-5` и записей G21/G22, а про снятые алиасы DeepSeek говорилось
в будущем времени.

- Чанки пересобраны из текущих файлов High. Ссылки `!!core_v8H §7` переведены на **имена блоков**
  Lite — нумерованных секций в ядре L нет, прямая замена дала бы ссылку в никуда.
- Справочник моделей (55 KB после обновления данных) разрезан на четыре **вендорных** чанка:
  Claude · GPT+Gemini · Grok · бюджетные. Максимум одной загрузки — **18,3 KB вместо 55**.
  Резали по вендору, а не по уровню модели: иначе на запрос про Sonnet пользователь получил бы
  чанк, в котором Sonnet 4.6 нет.
- Доставка проверена скачиванием обратно: 14 из 14 по контрольной сумме и маркеру конца файла.

### Прочие исправления

- **High:** логотип при старте показывал `P2P v8H.4- HIGH EDITION` — старый номер и слипшийся
  разделитель, из-за которого строку не видел и инструмент проверки. Заголовок раздела меню
  обещал «30 базовых + 6 динамических» при фактических 37 и 8. В шапке `_preloader.md`
  говорилось, что автодетект хоста портирован из `8.4.6-H`, то есть из самого себя.
- **Claude:** строка статуса расходилась между формами (`v8C.4` против `v8C.3`), рамки
  `SESSION METRICS` и `SANDBOX` несли старый номер, строка идентификации в chat-форме
  тянула устаревшую дату сборки.
- **High / Normal / Lite:** в базе знаний строка `VERSION_METADATA → SYSTEM` осталась со старым
  номером — инструмент проверки видел рядом имя сущности (`DB_v8H`) и считал строку защищённой.
- **Все сборки:** логотипы H и N переведены на простой ASCII (блочный разъезжался при переносе) ·
  восемь агентов QUORUM больше не представляются с номером версии · README редакций H/N/L несли
  внутреннюю нумерацию, причём русская и английская версии расходились между собой.

### Проверки

| | результат |
|---|---|
| `verify_c_dispatch.py` | 21 проверка · 11 821 объект · 0 провалов |
| `--selftest` | 11 из 11 |
| `verify_lite.py` | 15 проверок · 0 ошибок |
| гейт дрейфа модель-данных | 94 хита, не вырос |
| учёт внутренней нумерации | 1416 → 664 вхождения, механических классов ноль |

Проверка «версия только в YAML-шапке» переписана и получила собственный тест на срабатывание:
в прежнем виде она искала блок `VERSION_METADATA` и после его переименования осматривала бы
2 файла вместо 99, оставаясь зелёной.

### Обновление

Плагин: `/plugin marketplace update` → кнопка **Update**. Файловые сборки H/N/L — архивами ниже.
Lite: обновите boot-файлы, арсенал подтянется из gist автоматически.


---


# P2P v8.4.6 — Model data refresh, 8.4.4 techniques in chat form, one version per build


Three blocks: **model data refresh** (Opus 5 as primary, two new error catalogue entries, revised
prices and migrations), **Claude Edition alignment** (8.4.4 techniques finally available in the chat
form, `/p2p <task>` no longer opens the menu) and **version cleanup** — their drift is why Normal
menu items `[26-32]` never opened.

### Models and data

`claude-opus-5` is now the primary model (1M/128K, $5/$25, thinking on by default); added
`gemini-3.6-flash`, `gemini-3.5-flash-lite`, `kimi-k3` (**ACCESS-RISK**, never routed as primary),
plus `qwen3.7-plus` and `qwen3.6-35b-a3b` in Normal. Fable 5 removed from automatic routing
(usage-credit billing since 20.07); its 35 % share went to `claude-opus-5`. Two new error entries:
**G21** (declared vs actual model — check `resolved_model_slug`) and **G22** (GPT-5.6 Sol agentic
hazard). Claude tokenizer inflation canonised at **~+30 %** with the Token Counting API.

Fixed: the DeepSeek migration rule was inverted (`deepseek-reasoner` → **v4-pro**, not v4-flash) ·
Grok cached input priced `$0.30`/`$0.60` with a 200K threshold that doubles the cache too · Grok EU
access opened 21.07 · long-context surcharge clarified (cached input does not get more expensive) ·
GLM-5.2 price marked unconfirmed · Qwen deep-thinking does not support structured output.

### Claude Edition

The 8.4.4 techniques (VERBALIZED_SAMPLING, BRUTAL_EDITOR, GEPA, MASPO, CONTEXT ENGINEERING,
Context-Grounding CoT, POSITIVE_FRAMING) and the attribution file are now in the chat form as well.
`/p2p <task>` runs the dispatcher instead of printing the menu. pxpipe optical compression is
restricted to Fable 5. The plugin menu used to stop at `[40]`; both forms now expose `[0]`–`[42]`.

### Normal

Menu items `[26-32]` never opened — the detector compared the version in the module header with the
core version, and the two had drifted. Gating now uses the `MODULE_*` flag or a matched trigger; the
intermediate approach (detect by file body) was tested live and rejected, returning **25 items out
of 32**. The anti-hallucination guard remains. Added the missing `MODULE_SKILLS` flag.

### Version and history

The release number now lives **only in YAML front matter** plus three user-visible places per
edition; self-identification carries the **series** (`v8C` / `v8H` / `v8N` / `v8L`).
`tools/bump_version.py` performs the next release in one command. History was moved out of working
files — **612 lines**; builds are 1.5–2.6 % lighter.

### Lite

Arsenal chunks were rebuilt from current High files (the previous ones dated 27.06–13.07 and still
carried `v8H.3`). The vendor reference (55 KB) was split into four per-vendor chunks, bringing the
largest single fetch down to **18.3 KB from 55**. Delivery verified by downloading all 14 chunks
back and checking hashes and end-of-file markers.

### Update

Plugin: `/plugin marketplace update` → **Update**. File builds for H/N/L are attached below.
