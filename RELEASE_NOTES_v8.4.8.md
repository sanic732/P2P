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

## Update

```
/plugin marketplace update p2p
/plugin update p2p-v8c3
```
