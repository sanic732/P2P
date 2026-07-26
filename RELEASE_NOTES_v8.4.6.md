# P2P v8.4.6 — Одна версия на сборку, история из рабочих файлов вынесена, арсенал Lite пересобран


---


Номер версии жил в проекте в двух несовместимых системах: внешней (`8.4.5-N`, каталоги и релизы)
и внутренней, унаследованной с форума (`v8N.4`). Они поднимались раздельно и расходились при каждом
выпуске. Это не косметика — класс дважды ломал функциональность: пункты меню Normal `[26-32]`
не открывались никогда, а одна редакция C представлялась пользователю двумя разными версиями.

Причина у обоих случаев одна: номер стоял в стольких местах, что синхронизировать его вручную
невозможно. В этом релизе мест не осталось.

### Версия

- Номер выпуска живёт **только в YAML-шапке файла** и в трёх местах на редакцию, где его видит
  пользователь: логотип при старте, шапка меню, строка статуса. Раньше в файлах C он стоял
  до четырёх раз — шапка, заголовок документа, поле `scope`, хвостовой блок метаданных.
- В самоопределении системы (`HOST_IDENTITY`), напоминании об ограничениях и рамке ATLAS теперь
  стоит **серия** — `v8C` / `v8H` / `v8N` / `v8L`. Серия не меняется от выпуска к выпуску,
  и эти 40 строк больше не требуют правки при релизе.
- `tools/bump_version.py` — следующий выпуск делается одной командой: 207 замен, переименование
  каталогов, `marketplace.json`, README редакций. Текущую версию скрипт берёт из имён каталогов,
  а не с аргумента, поэтому рассинхрон невозможен по построению.

### История вынесена из рабочих файлов

Из сборок убраны блоки «что нового в поколении», поля `SYSTEM` / `CHANGELOG` / `SOURCE` /
`PREDECESSOR` / `SECTIONS`, даты правок и метки поколения вида `[v8C.3]` — **суммарно 612 строк**.
Всё это описывало прошлое и грузилось в контекст модели при каждом запуске. Содержательная часть
перенесена в CHANGELOG редакций: проверено, что половины списка возможностей `NEW_IN_v8N`
в чейнджлогах не было — блок был единственным носителем.

Блок метаданных в конце файла переименован в `FILE_META`: версии в нём больше нет, осталась
связность (`COMPATIBLE`, `MENU_ITEM`) и справочные поля.

Сборки стали легче на 1,5–2,6 % — примерно 2000–2500 токенов при полной загрузке.

### Normal: меню

Показ модулей `[26-32]` переведён на гейт по флагу. Прежний детект искал тело файла-модуля
в контексте по frontmatter — на живом прогоне он отдавал **25 пунктов из 32** при всех включённых
модулях и приложенных файлах. Правило, требующее от модели найти строку в другом документе,
оказалось ненадёжным; условие должно лежать в её собственном состоянии.

Страховка от выдумывания сохранена: если пункт выбран, а файла модуля в контексте нет, система
просит приложить файл и не сочиняет его содержимое. Добавлен флаг `MODULE_SKILLS` — модулей семь,
а флагов было шесть.

Описание меню в ядре сокращено с 65 строк до 34 без изменения правил.

### Lite: арсенал пересобран и разрезан

Lite не хранит модули у себя — тянет их чанками из gist. Чанки были собраны 27.06–13.07
и с тех пор не обновлялись: внутри стояла версия `v8H.3`, не было `claude-opus-5`, не было записей
G21/G22, а про снятые алиасы DeepSeek говорилось в будущем времени, хотя срок прошёл 24.07.

- Чанки пересобраны из текущих файлов High. Ссылки на `!!core_v8H §7` переведены на **имена блоков**
  Lite: нумерованных секций в ядре L нет, и прямая замена дала бы ссылку в никуда.
- Чанк `VENDORS` (55 KB после обновления модель-данных) разрезан на четыре **вендорных** чанка:
  Claude, Frontier (GPT + Gemini), Grok, Budget. Максимум одной загрузки — **18,3 KB вместо 55**.
  Резали по вендору, а не по тиру: иначе по слову «sonnet» пользователь получил бы чанк,
  в котором Sonnet 4.6 нет — он лежал в другом файле.
- Доставка проверена скачиванием обратно: 14 из 14 по контрольной сумме и маркеру конца файла.

### Исправлено

- **High:** логотип при старте показывал `P2P v8H.4- HIGH EDITION` — старый номер и слипшийся
  разделитель. Из-за разделителя строку не видел и сам инструмент проверки.
- **Claude:** строка статуса расходилась между двумя формами поставки (`v8C.4` в плагине против
  `v8C.3` в chat-форме) — то же расхождение, что уже чинили в PR #42, только в другом месте.
  Рамки `SESSION METRICS` и `SANDBOX` тоже несли старый номер.
- **High / Normal / Lite:** в базе знаний строка `VERSION_METADATA → SYSTEM` осталась со старым
  номером: инструмент проверки видел рядом имя сущности (`DB_v8H`) и относил строку к защищённым.
- **High:** в шапке `_preloader.md` было сказано, что механика автодетекта хоста портирована
  из `8.4.6-H`, то есть из самой себя. Восстановлен источник — `8L.3`.
- **Все редакции:** восемь агентов QUORUM больше не представляются с номером версии.
- **README редакций** H/N/L несли внутреннюю нумерацию, причём русская и английская версии
  расходились между собой.
- Заголовок раздела меню в High обещал «30 базовых + 6 динамических» при фактических 37 и 8.

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
Lite обновляется вместе с boot-файлами; арсенал подтянется из gist автоматически.


---


# P2P v8.4.6 — One version per build, history moved out of working files, Lite arsenal rebuilt


The release number used to live in two incompatible systems: external (`8.4.5-N`, directories and
releases) and internal, inherited from the forum (`v8N.4`). They were bumped separately and drifted
apart every release. That drift twice broke functionality: Normal menu items `[26-32]` never opened,
and one edition of C presented itself under two different versions.

### Version

- The release number now lives **only in the YAML front matter** of each file, plus three
  user-visible places per edition: startup logo, menu header, status line. In C files it used to
  appear up to four times per file.
- Self-identification (`HOST_IDENTITY`), the constraint reminder and the ATLAS frame now carry
  the **series** — `v8C` / `v8H` / `v8N` / `v8L` — which does not change between releases.
- `tools/bump_version.py` performs the next release in one command: 207 replacements, directory
  renames, `marketplace.json`, edition READMEs. It reads the current version from directory names.

### History moved out of working files

Generation blocks, `SYSTEM` / `CHANGELOG` / `SOURCE` / `PREDECESSOR` / `SECTIONS` fields, edit dates
and `[v8C.3]`-style markers are gone — **612 lines total**. The substantive part was moved into the
edition CHANGELOGs. The trailing metadata block is now `FILE_META`: it no longer carries a version.

Builds are 1.5–2.6 % lighter — roughly 2000–2500 tokens at full load.

### Normal: menu

Module items `[26-32]` are now gated by flag. The previous detector looked for the module file body
in context and returned **25 items out of 32** in a live run with every module attached. The
anti-hallucination guard remains: if an item is selected and its file is absent, the system asks for
the file instead of inventing content. Added the missing `MODULE_SKILLS` flag.

### Lite: arsenal rebuilt and split

Lite fetches its modules from a gist. Those chunks were assembled on 27.06–13.07 and still carried
`v8H.3`, lacked `claude-opus-5` and the G21/G22 entries, and described the retired DeepSeek aliases
in the future tense.

Chunks were rebuilt from current High files, with references remapped to Lite block names. The
`VENDORS` chunk (55 KB) was split into four **per-vendor** chunks — Claude, Frontier, Grok, Budget —
bringing the largest single fetch down to **18.3 KB from 55**. Delivery verified by downloading all
14 chunks back and checking hashes and end-of-file markers.

### Fixed

High startup logo showed `P2P v8H.4- HIGH EDITION` · C status line disagreed between the two
delivery forms · `VERSION_METADATA → SYSTEM` in H/N/L knowledge bases kept the old number ·
H preloader claimed its host-detection was ported from itself · QUORUM agents no longer introduce
themselves with a version · edition READMEs carried internal numbering and disagreed between RU
and EN.

### Update

Plugin: `/plugin marketplace update` → **Update**. File builds for H/N/L are attached below.
