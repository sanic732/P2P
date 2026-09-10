# P2P v8.4.8 — Данные выправлены по эталону, Lite грузит свежие модули, меню High без тихих отказов

---

Выпуск целиком про достоверность. Разбор 09–10.09 сверил четыре редакции между собой
и с эталонными live specs и нашёл тридцать четыре расхождения. Двенадцать из них устроены
одинаково: факт исправлен в файле-объявлении и не исправлен там, где его читают.

Самое заметное — **цена Sonnet 5**. Подорожание до $3/$15 с 01.09 отменили ещё 10.08,
манифест каждой сборки прямо писал «любая строка с $3/$15 неверна» — а сами строки остались
в десяти местах. Дата наступила, и сборка называла вдвое завышенную цену на модель
по умолчанию Free/Pro.

## Lite грузил модули полуторамесячной давности

Индекс `_index_v8L.md` в `main` и в опубликованном `8.4.7-L.zip` указывал на ревизию гиста
от 26.07 — то есть на модули **8.4.6**. Проверка целостности при этом молчала: sha256
в индексе сходились с теми самыми старыми файлами, потому что ревизия и хеши записываются
туда одновременно. Обе стороны сверки брались из одного файла.

Причина — порядок выпуска 8.4.7: релиз опубликовали в 02:59, модули залили на гист в 03:22,
а коммит с новыми хешами лёг в ветку, которая была слита за полчаса до него.

В 8.4.8 индекс указывает на модули этого выпуска. Появился `tools/verify_gist_live.py`:
он качает каждый файл по адресу **без вшитой ревизии** и сверяет с индексом — так подмена
источника перестаёт быть незаметной.

## Цены и сроки

- **Sonnet 5** — $2/$10. Строки «$3/$15 с 01.09» убраны из всех редакций.
- **GPT-5.6 Sol** — $4 / $0.40 cached / $20, промо «не раньше» 21.11. Выше порога 272K — $8 / $30.
  Прежние $5/$30 и $10/$45 остались от старого прайса.
- **`deepseek-v4-flash`** — $0.22/$0.66 off-peak, $0.44/$1.32 peak. Сборка называла шесть
  разных значений в разных файлах.
- **G10 (порог 272K)**: cached input дорожает **вдвое вместе с обычным**. Прежняя пометка
  «cached EXEMPT» и вывод «стабильный префикс от перехода спасает» были неверны и сняты.
- **Дедлайны 05.08, 26.08 и 31.08 исполнены** — числились предстоящими в четырнадцати местах,
  включая счётчик `[T-10 DAYS]`, отсчитывавший от даты месячной давности. Счётчики остальных
  сроков пересчитаны от 10.09.

## Маршрутизация

- **Код** ведёт на `claude-opus-5` (был Opus 4.8). Прежде в каждой сборке лежали две таблицы
  «задача → модель» с разными ответами, а одна из них была датирована 02.05.
- **`grok-4.3` — 1M контекста**, 2M только у `grok-4.20` (Heavy-16).
- **`gemini-3.8-flash`** внесён в реестры: он был объявлен основным для bulk-нагрузки,
  но маршрутизатор до него не доходил ни в одной редакции.
- **Убраны цели, которых не существует**: `moonshot-v2-128k` и `moonshot-v2-8k` не значились
  ни в одном реестре — swarm ведёт на `kimi-k2.6`.
- **Убран legacy `gpt-5.5`** как цель agentic и как рекомендуемая модель в Contract Builder
  и таблицах совместимости шаблонов.
- **MiniMax-M3 больше не цель маршрута** в редакции Claude: модель track-only — P2P на ней
  работает, но не маршрутизирует на неё.
- **Computer use на `gpt-5.6-sol`** помечен G22: нужен явный allowlist и журнал аудита.
- **35 запрещённых алиасов `-latest`** убраны из High и Normal.

## Плагин догнал чат-форму

Дерево плагина было не копией, а более старой сборкой. Живой слой отставал до 26.07 и 27.06
и нёс три факта, отменённых эталоном явным «BASE 26.07 IS WRONG»: «cached input EXEMPT»,
запрет strict-JSON у Qwen3.8-Max, «Fable 5 SUSPENDED globally». Внутри одного дерева один
файл объявлял основной моделью Opus 4.8, другой — Opus 5.

Заодно: головной `core.md` объявлял зависимости по именам чат-формы — ни один из четырёх
путей в дереве плагина не существовал; всего таких ссылок было 59. Пункт `[42] Создать
Agent Skill` требовал модуля, которого в плагине не было.

## Меню High: пять пунктов выводились без модулей

`[24] CONTRACT BUILDER`, `[25] EXPLORATION MODE` и `[19] MENTOR METHOD` вели на имена файлов,
которых в поставке нет, — при том что сами модули есть под другими именами. `[15] VISUAL CODING`
и арт-баннеры требовали модулей, которых не было вовсе: они перенесены из редакции Claude.
`[18] KB BROWSER` ссылался на индекс донорской редакции 8A.

Подписи агентов `[7]` и `[9]` были взяты из схемы Normal и противоречили `!agents.md` самой
High: ANON там — исполнение инструментов и neutral reviewer, VECTOR — данные и аналитика,
а безопасность живёт в `!security.md [39]`.

## Каталог ошибок

Заголовки во всех четырёх редакциях объявляли каталог как G1–G20, хотя коды G21 и G22 в нём
давно есть — 45 мест. Семь кодов назывались по-разному в разных редакциях и сведены к одной
форме. `G3` (Grok topic drift) в редакции Claude стоял «(RESERVED)», хотя Grok там
поддерживается как цель.

## Что было сломано и как исправлено

Этот раздел — про наши собственные промахи, а не про чужие данные. Мы решили описать их
прямо: пользователю важнее знать, где сборка врала, чем читать ровный список улучшений.

1. **Lite полтора месяца грузил модули 8.4.6** — разобрано выше, в разделе про индекс `_index_v8L.md`.
2. **10.09 при попытке починить 8.4.7-L ассет был перезалит с концами строк CRLF.** У части хостов
   после этого перестали грузиться модули: символ `\r` попадал в хвост адреса, взятого из индекса,
   и запрос уходил в никуда. Ассет возвращён к опубликованному в тот же день; тег `v8.4.7`
   и история не трогались. В 8.4.8 сборка идёт из тега, а концы строк проверяет карантин
   отдельной проверкой — по байтам, а не по тексту.
3. **Прежний чек-лист выпуска не имел ни одного проверяемого пункта** — это была процедура на бумаге,
   и 8.4.7 вышел мимо неё. Теперь публикацию запрещает `tools/release_gate.py`: пятнадцать проверок,
   у каждой печатается число осмотренных объектов рядом с числом провалов, ноль осмотренных —
   это провал. К заслону написана пара-слепота, которая ломает выпуск нарочно и проверяет,
   что заслон это заметил.
4. **Из сборок убран вшитый `live_specs.md`** — четыре копии по 62 КБ в каждой поставке. Факты
   переехали в BASE редакций, свежее приходит по LIVE-каналу. Сборка стала меньше, а расхождение
   «в файле одно, в канале другое» — невозможным.
5. **Модули Lite теперь публикуются отдельным гистом на каждый выпуск.** Прежде один гист
   переписывался поверх, и установка молча получала не те модули, на которые рассчитана.
   В 8.4.7 это выглядело так: индекс указывал на ревизию гиста от 26.07 — то есть на модули
   **8.4.6**, — а sha256 рядом были записаны от них же, поэтому проверка целостности сходилась
   и о подмене не сообщала.
6. **Маршруты не доедут до уже установленного 8.4.7 через LIVE-канал.** Это ограничение, а не
   недоделка: по каналу идёт форма DELTA, в ней есть цены, статусы, дедлайны и реестр ошибок,
   но нет таблицы маршрутов. Новый маршрут webdev на `gpt-6-astra` появится только у тех,
   кто поставит 8.4.8.

## Факты 8.7.4

- **GPT-6 Astra** (`gpt-6-astra`, GA 09.09): контекст 1 050 000, выход 128 000, cutoff 2026-04-30,
  $10 / $1 cached / $12.50 cache-write / $50. Порог 272K действует вместе с кэшем — за ним ×2
  на вход и на кэш и ×1.5 на выход, поэтому контекст держать ниже порога. Инструменты — только
  через `/v1/responses`, на `/v1/chat/completions` вместе с `reasoning_effort` они дают 400.
  Primary для webdev в High и Normal; в Claude — по явному указанию оператора.
- **Вендор Grok теперь SpaceXAI** (бывш. xAI): сделка объявлена 02.02.2026, документация вендора
  и борды Arena уже переименованы. Имя продукта Grok и api-строки не менялись; распознавание
  хоста понимает оба написания.
- **GLM-5.3-Flash**: промо истекло 09.09 в срок, действуют прайсовые $0.15 / $0.03 / $0.50.
- **Qwen3.8-Max**: максимальный выход — 131 072 токена (прежние 128K были неточностью);
  тариф плоский, 12/36 CNY за 1M, долларовые $2/$6 — приближение.
- **MiniMax Token Plan**: Plus $22 / Max $55 / Ultra $132 в месяц (числа $20/$50/$120 мертвы).
  Модель по-прежнему track-only: P2P на ней работает, но не маршрутизирует на неё.
- **Claude Code 2.1.267**: `maxEffortLevel` ограничивает усилие на всех провайдерах, и при
  корпоративном потолке побеждает нижний; хуки `PreModelSwitch` могут запретить смену модели,
  а при неопределимом наборе хуков плагина смена отклоняется; появился
  `--system-prompt-snapshot off`; пол версии для Fable 5.1 — v2.1.257; коды ошибок — 404
  на недоступную модель и 400 на недоступный бета-заголовок, не 403.

## Обновление

```
/plugin marketplace update p2p
/plugin update p2p-v8c3
```

Файловые сборки — архивы в этом релизе. Редакции High, Normal и Lite обновляются заменой
каталога; Lite дополнительно подтянет модули с гиста при первом запросе.

---

# [EN] P2P v8.4.8 — Data reconciled with the reference, Lite fetches current modules, High menu without silent failures

A correctness release. A 09–10.09 review cross-checked all four editions against each other
and against the reference live specs, and found thirty-four discrepancies. Twelve share
one shape: the fact was fixed in the file that declares it and left stale everywhere it is read.

**Sonnet 5 pricing** is the clearest case. The rise to $3/$15 from 01.09 was cancelled on 10.08
and every build's own manifest said "any line carrying $3/$15 is wrong" — yet ten such lines
remained. The date passed, so the build was quoting double the real price of the Free/Pro
default model.

**Lite was loading modules from six weeks earlier.** The `_index_v8L.md` index in `main` and in
the published `8.4.7-L.zip` pinned a gist revision from 26.07 — the **8.4.6** modules. Integrity
checks stayed silent: the index's sha256 matched those old files because revision and hashes are
written together. Both sides of the check came from the same file. The new
`tools/verify_gist_live.py` fetches each file by its **unpinned** URL, so a substituted source
can no longer pass unnoticed.

Also in this release: Sol at $4/$0.40/$20 (was $5/$30), `deepseek-v4-flash` at $0.22/$0.66
off-peak (six different values across files before), the G10 rule corrected — cached input
doubles along with uncached; three executed August deadlines moved to past tense; code routing
to `claude-opus-5`; `grok-4.3` back to 1M context; `gemini-3.8-flash` added to the registries;
non-existent route targets (`moonshot-v2-128k`, `moonshot-v2-8k`) and legacy `gpt-5.5` removed;
35 forbidden `-latest` aliases dropped from High and Normal; MiniMax-M3 no longer a route target
(it is track-only); computer use on `gpt-5.6-sol` flagged with G22.

The **plugin tree** was an older build rather than a copy of the chat form: its live layer lagged
to 26.07 and carried three facts the reference had explicitly revoked, and 59 links pointed at
chat-form filenames that do not exist there. The **High menu** listed five items whose modules
were missing — three were wrong filenames for modules that do exist, two were genuinely absent
and have been ported from the Claude edition. The **error catalogue** is now declared as G1–G22
(45 headings said G1–G20), seven code names were unified, and `G3` is documented in the Claude
edition instead of sitting reserved.

## What was broken and how it was fixed

This section is about our own mistakes, not someone else's data. We chose to state them plainly:
knowing where a build lied matters more than a tidy list of improvements.

1. **Lite loaded 8.4.6 modules for six weeks** — described above, in the `_index_v8L.md` section.
2. **On 10.09, while fixing 8.4.7-L, the asset was re-uploaded with CRLF line endings.** On some
   hosts module loading then broke: a `\r` ended up at the tail of the URL read from the index,
   so the request went nowhere. The asset was restored to the published one the same day; the
   `v8.4.7` tag and the history were not touched. In 8.4.8 assets are built from the tag, and
   line endings are checked by the release gate — on bytes, not on text.
3. **The previous release checklist had no verifiable item in it** — a procedure on paper, and
   8.4.7 shipped past it. Publication is now blocked by `tools/release_gate.py`: fifteen checks,
   each printing the number of objects inspected next to the number of failures, with zero
   inspected counting as a failure. A blind-test companion breaks a release on purpose and
   verifies that the gate noticed.
4. **The embedded `live_specs.md` is gone from the builds** — four copies of 62 KB each. The facts
   moved into each edition's BASE, and fresh data arrives over the LIVE channel. Builds are
   smaller, and "one thing in the file, another in the channel" is no longer possible.
5. **Lite modules are now published as a separate gist per release.** Previously a single gist was
   overwritten in place, so an install silently received modules it was not built for. In 8.4.7 the
   index pinned a gist revision from 26.07 — the **8.4.6** modules — and the sha256 values beside it
   had been written from those same files, so the integrity check matched and reported nothing.
6. **Routing will not reach an installed 8.4.7 over the LIVE channel.** This is a limitation, not
   an omission: the channel carries the DELTA form, which has prices, statuses, deadlines and the
   error registry, but not the routing table. The new webdev route to `gpt-6-astra` reaches only
   those who install 8.4.8.

## Facts from 8.7.4

- **GPT-6 Astra** (`gpt-6-astra`, GA 09.09): context 1,050,000, output 128,000, cutoff 2026-04-30,
  $10 / $1 cached / $12.50 cache-write / $50. The 272K cliff applies to the cache as well — 2x on
  input and cache, 1.5x on output beyond it — so keep context below the threshold. Tools go through
  `/v1/responses` only; on `/v1/chat/completions` together with `reasoning_effort` they return 400.
  Primary for webdev in High and Normal; in Claude, on explicit operator request only.
- **The Grok vendor is now SpaceXAI** (formerly xAI): the deal was announced 2026-02-02, and the
  vendor's docs and the Arena boards already carry the new name. The Grok product name and the
  api strings are unchanged; host detection understands both spellings.
- **GLM-5.3-Flash**: the promo expired on schedule on 09.09; list prices $0.15 / $0.03 / $0.50 apply.
- **Qwen3.8-Max**: max output is 131,072 tokens (the earlier 128K was imprecise); the tariff is
  flat at 12/36 CNY per 1M, and $2/$6 is an approximation.
- **MiniMax Token Plan**: Plus $22 / Max $55 / Ultra $132 per month ($20/$50/$120 are dead).
  The model stays track-only: P2P runs on it but does not route to it.
- **Claude Code 2.1.267**: `maxEffortLevel` caps effort on every provider, and where an enterprise
  cap also applies the lower one wins; `PreModelSwitch` hooks can block a model switch, and when
  the hook set of a managed plugin cannot be determined the switch is refused; new
  `--system-prompt-snapshot off`; the version floor for Fable 5.1 is v2.1.257; error codes are 404
  for an unavailable model and 400 for an unavailable beta header, not 403.

## Update

```
/plugin marketplace update p2p
/plugin update p2p-v8c3
```
