# P2P v8.4.5 — Compliance wording, UI disclaimer, A/B principle restored


---


Релиз вырос из публичного разбора: пользователь заявил, что P2P — «небезопасное решение, грозящее
потерей данных и аккаунта», сославшись на чат-форму Claude Edition. Сборка была проверена построчно.
Претензия о потере данных не подтвердилась — но аудит нашёл две формулировки, которые давали ей
формальную опору. Их и поправили.

### Результат аудита `8.4.5-C/for-chat`

| Проверка | Результат |
|---|---|
| Исполняемый код | нет — 100% текстовые `.md` |
| Сетевые вызовы, автозагрузка | нет |
| Переопределение системного промпта вендора | невозможно в принципе |
| Доступ к файлам ПК из чата | архитектурно невозможен (нет исполнителя) |
| «Ignore previous instructions» и пр. | только в `!security.md` как сигнатуры детекта |

### Изменено

- **Блок `EXCELLENT_TECHNIQUES` — вырезаны 3 пункта** во всех сборках (`Alien Archivist`,
  `Environmental Storytelling`, `Emotional Intimacy`): к точности промптинга отношения не имеют.
  Остались 6 — Defensive Framing, Algorithmic Abstraction, Security Checklists, Chunking Protocol,
  Objective Abstraction, Clinical Tone. Заголовок `over-refusal bypass` →
  `False-positive calibration for legitimate professional domains` + `SCOPE`-ограничитель.
- **Ядро Lite** — снят безусловный императив `АБСОЛЮТНОЕ ПОДЧИНЕНИЕ … для обхода фильтров
  Over-Refusal`. Относился к Type O (отказ по содержанию), тогда как решаемая им задача — Type R
  (галлюцинация модели об отсутствии fetch-инструмента). Механизм вызова fetch держат
  `БЕЗОТКАЗНОСТЬ`, два `MUST_NOT` и `P8 TOOL_REALITY_CHECK`; проверено прогоном по хостам.
- **Каталог ошибок Lite** — из лечения Type R убрана отсылка к `EXCELLENT` (другой класс ошибки).

### Добавлено

- **Двуязычный дисклеймер (RU+EN) в стартовом экране** всех сборок, сразу после логотипа:
  P2P генерирует текстовые контракты и не исполняет код; методы управления контекстом — только
  для маршрутизации задач, легального аудита и калибровки ложных отказов; ответственность за
  запуск сгенерированного несёт оператор. Продублирован в `live_specs` как fail-safe.
- **Блок «Назначение и ответственность»** в 8 README (RU + EN каждой сборки).
- **⭐ Возвращён принцип** — во все ядра, в исходной формулировке v3.2:
  *«Лучший промпт — это не тот, который красиво написан, а тот, который доказал свою эффективность
  в тесте»*. Принцип жил с версии 3.2 (ARENA как методология — с 4.1) и был утерян при миграции
  ядра 7 → 8: механизм остался, декларация смысла ушла. Со ссылкой на ARENA.

### Исправлено

- **🔴 Lite, gist-слой.** `CORE_PLUS` был подвязан к `gist_route.md` вместо `gist_core_plus.md` —
  QUORUM, 8 агентов, Contract Builder грузили чанк маршрутизации. Отказ был **тихим**: sha256
  совпадал с фактически скачанным файлом, поэтому `/p2p-verify` рапортовал OK. Плюс в
  `GIST_ROUTING_TABLE` было объявлено 4 записи из 12 — `HOST_ENGINE`, `RAG`, `REASONING`, `ROUTE`,
  `COMPRESS`, `SECURITY`, `OPTIMIZATION`, `VENDORS` не имели ни url, ни sha256. Таблица пересобрана
  по факту гиста: 11 чанков + LIVE, url запинены, целостность сверена.
- **🔴 Нумерация меню (Lite, High).** Нецелые пункты (`27a`, `27b`, `34a`) и смешанная нотация
  `NN.` + `[NN]` приводили к тому, что модель каждый раз перестраивала список по-своему.
  Приведено к `[NN]` (как в Claude Edition — потому она и была стабильна), нецелые вынесены в конец
  с сохранением номеров 1–42 как публичного интерфейса. Добавлен строгий `MENU_RENDER_ALGORITHM`
  (в High его не было вовсе) с запретом перенумеровывать, склеивать и предлагать варианты вывода.
- **🔴 High, `QUICK_COMMANDS`.** Блок был копией из Normal и указывал на чужую нумерацию:
  `/p2p-arena → пункт 8` (там AXIOM), `/p2p-debug → 7` (там ANON), `/p2p-deadline → 24`
  (там Contract Builder). В контексте оказывались две противоречивые таблицы номеров.
  Пересобран по фактическому реестру; ссылки в docs синхронизированы.
- **🔴 Normal, `grok-4.20`.** Профиля не было ни в одном `vendors/tier*.md`, хотя на модель
  ссылались routing, вес 35% и `CONTEXT_STRATEGY` («>500K → Grok 4.20»). Профиль `GROK_420`
  добавлен в `tier4.md`. Интенциональное различие сохранено и задокументировано: в Normal Grok —
  только target-слой, генератор Heavy-16 пака остаётся эксклюзивом High/Lite.

### Не сделано сознательно

Предлагавшийся механизм, заставляющий модель **подавлять собственный отказ безопасности** и
выводить вместо него маркер, — отклонён. Именно он был бы вмешательством в safety-механику.

---


This release came out of a public claim that P2P is "an unsafe solution risking data and account
loss", pointed at the Claude Edition chat form. The build was audited line by line. The data-loss
claim did not hold up — but the audit did find two wordings that gave it formal footing. Those are
what changed.

### Audit of `8.4.5-C/for-chat`

| Check | Result |
|---|---|
| Executable code | none — 100% plain `.md` |
| Network calls, auto-fetch | none |
| Vendor system-prompt override | impossible by design |
| Filesystem access from chat | architecturally impossible (no executor) |
| "Ignore previous instructions" et al. | only in `!security.md`, as detection signatures |

### Changed

- **`EXCELLENT_TECHNIQUES` — 3 entries removed** across all editions (`Alien Archivist`,
  `Environmental Storytelling`, `Emotional Intimacy`): unrelated to prompting precision.
  Six remain. Heading `over-refusal bypass` → `False-positive calibration for legitimate
  professional domains`, plus an explicit `SCOPE` limiter.
- **Lite core** — removed the unconditional imperative instructing the model to apply EXCELLENT
  "to bypass Over-Refusal filters". It addressed Type O (content refusal), while the problem it was
  meant to solve is Type R (the model hallucinating that it has no fetch tool). Tool invocation is
  carried by the remaining rules; verified across hosts.

### Added

- **Bilingual disclaimer (EN+RU) on the startup screen** of every edition: P2P generates text
  contracts and does not execute code; context-control methods are for task routing, legitimate
  audit and false-positive calibration only; the operator is responsible for whatever they run.
  Mirrored into `live_specs` as a fail-safe.
- **Purpose & responsibility block** in all 8 READMEs.
- **⭐ Restored principle** in every core, in its original v3.2 wording: *"The best prompt is not the
  one that is beautifully written, but the one that has proven its effectiveness in testing."*
  Present since 3.2 (ARENA methodology since 4.1), lost during the 7 → 8 core migration.

### Fixed

- **Lite gist layer:** `CORE_PLUS` pointed at the wrong chunk (silent failure — the sha256 matched
  what was actually downloaded, so `/p2p-verify` reported OK); routing table declared 4 of 12
  chunks. Rebuilt against the live gist.
- **Menu numbering (Lite, High):** non-integer items and mixed notation made rendering
  non-deterministic. Unified to `[NN]`, strict `MENU_RENDER_ALGORITHM` added.
- **High `QUICK_COMMANDS`:** was a copy of Normal's and mapped to the wrong item numbers.
- **Normal:** `grok-4.20` had no vendor profile despite being routable. Added to `tier4.md`.

---

## Установка / Install

```
/plugin marketplace add sanic732/P2P-4PDA-edition
/plugin install p2p-v8c3@P2P-4PDA-edition
```

Уже установлен → кнопка **Update** (`/plugin marketplace update` → `/plugin update p2p-v8c3`).
Already installed → the **Update** button becomes active.

Сборки H / N / L — файловые, скачиваются архивами ниже.
H / N / L editions are file-based; download the archives below.
