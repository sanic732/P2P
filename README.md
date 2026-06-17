# P2P — Prompt-to-Prompt · Claude Native Edition · **v8C.3-ALPHA**

> Мета-промпт, который пишет промпты (и выполняет задачи). Поток сознания на входе — выверенный промпт под нужную модель на выходе. Цель: убрать промпт-инжиниринг для рядового пользователя.

**Версия:** v8C.3-ALPHA · **Лицензия:** MIT · **Оптимизировано под:** Claude Fable 5 / Opus 4.8 / Sonnet 4.6  
**Зеркало для:** [4PDA-сообщества «Prompt to Prompt 8 NEXUS»](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143218594)

---

## Что такое P2P

P2P (Prompt-to-Prompt) — модульная оркестрирующая система, загружаемая в Claude и превращающая его в эксперта по prompt engineering. Вместо ручного написания промптов вы описываете задачу — система сама применяет нужную архитектуру, защитные механизмы и model-specific форматирование.

**Архитектура:** Foundation → Safeguards → Execution  
**Философия:** ограничения, а не давление. Эмпирично, а не эстетично.  
**Суть:** убить классический prompt engineering для обычного пользователя.

---

## 🚀 Установка (Claude Code / Cowork)

```
/plugin marketplace add https://github.com/sanic732/P2P-4PDA-edition
/plugin install p2p-v8c3@p2p
```

Проверка: `/p2p` (главное меню) · `/p2p-teacher` (интерактивный курс).  
Обновление: `/plugin update p2p-v8c3@p2p`.

Для Claude.ai **Chat / Projects / API** — дистрибуция `for chat (project)/` (грузить `.md` в Project Knowledge или system prompt). Подробно: `docs/INSTALL_GUIDE.md`.

---

## ✨ Что нового в v8C.3-ALPHA (vs v8C.2)

- **PILOT** — единая ось управления уровнем помощи: **Co-Pilot** (новичок, веду за руку) / **Auto-Pilot** (баланс) / **Manual** (эксперт + GLASS COCKPIT, видно какие техники применены и почему). Выбор буквой `C/A/M`.
- **SHERPA** — проводник по штатным возможностям среды: подсказывает про план-режим, выбор модели и т.п. (апгрейд обучения «по ходу работы»).
- **6 новых ON-DEMAND модулей** (техники из открытых работ — см. `docs/TECHNIQUES_v8C3.md`):  
  `!rag` (RAPTOR/LongRAG) · `!reasoning` (Self-Consistency/MCTS/s1) · `!routing` (Semantic/Cascade/Cost-Aware) · `!compression` (LLMLingua/Gist) · `!security` (SelfCheckGPT/injection defense) · `!optimization` (OPRO/APE/EvoPrompt).
- **VERSION_COMPAT** — сосуществование стабильной логики v8C.2 и новых техник (`v8C2/v8C3 on/off` + флаги модулей); CONFLICT_RESOLVER при конфликте техник.
- **Арт-меню** — на старте ASCII-баннеры режимов (опционально, `!art.md`); выбор режима буквой, действия меню — цифрой `[1-40]`.
- **Claude Fable 5** добавлена как T4-модель (Arena #1 Agent, `claude-fable-5`); live specs обновлены (`vendors/live_specs_20260617.md`).
- Все инструкции — на английском (вывод по умолчанию русский, переключаемо `/lang`).

Детальный список — [`CHANGELOG.md`](CHANGELOG.md) · [`docs/ARCHITECTURE_MAP.md`](docs/ARCHITECTURE_MAP.md).

---

## 🗂 Структура репо

```
P2P-4PDA-edition/
├── README.md                    ← вы здесь
├── LICENSE                      ← MIT
├── NOTICE                       ← атрибуции техник + дисклеймер
├── CHANGELOG.md
├── .claude-plugin/
│   └── marketplace.json         ← для `/plugin marketplace add`
├── cowork + code/               ← ⭐ для Claude Code и Cowork
│   ├── .claude-plugin/          (plugin/marketplace manifests)
│   ├── .claude/                 (agents, commands, skills)
│   ├── pack.sh / pack.ps1       (упаковка в .plugin)
│   └── INSTALL.md               (TL;DR установки)
├── for chat (project)/          ← ⭐ для Claude.ai (Projects/Chat) и API
│   ├── _preloader.md, !!core_v8C.md, !!db_v8C.md   (BASE)
│   ├── !*.md                                       (ON-DEMAND, 26 модулей)
│   ├── docs/                                       (внутренние гайды дистрибуции)
│   ├── _live/                                      (4 файла)
│   └── vendors/                                    (tier1-4 + live_specs)
└── docs/                        ← гайды, карта архитектуры, техники
```

| Где работаешь | Папка | Что делать |
|---------------|-------|------------|
| Claude.ai **Projects** | `for chat (project)/` | Загрузить в Project Knowledge |
| Claude.ai **Chat** | `for chat (project)/` | Скопировать `_master.md` в system prompt |
| **API** (anthropic-sdk) | `for chat (project)/` | Собрать `system_prompt` из BASE-файлов |
| **Cowork** (desktop) | `cowork + code/` | `pack.ps1` → drag-drop `.plugin` |
| **Claude Code** (CLI) | `cowork + code/` | `/plugin install p2p-v8c3@p2p` |

> ⚠️ Не смешивай файлы из разных дистрибуций — архитектуры синтаксически несовместимы.

---

## 8 агентов QUORUM

| Агент | Роль | Когда |
|-------|------|-------|
| 🟣 **IRIS** | Strategist & Cartographer | Карта задачи, скрытые зависимости, правильные вопросы |
| 🟢 **TECTON** | System Architect | Структура промпта, архитектура кода, Decision Trees |
| 🟡 **AXIOM** | Logician & Verifier | Red Team, дыры в логике, Confidence Score |
| 🟠 **VECTOR** | Optimization & Security | Защита от prompt-injection, санитизация |
| 🟤 **DATOS** | Data Analyst | Фактчекинг, эмпирическая верификация |
| ⚫ **ANON** | Code Specialist | Production-ready код, Stop Conditions |
| 🔵 **ARCHITECTON** | Integrator | Разрешение конфликтов между агентами, UI/UX |
| ☀️ **HELIOS** | Final Synthesizer | Сборка хора 7 агентов в чистый результат |

11 команд: `/p2p`, `/p2p-quorum`, `/p2p-chain`, `/p2p-scope`, `/p2p-explore`, `/p2p-feedback`, `/p2p-metrics`, `/p2p-atlas`, `/p2p-capsule`, `/p2p-karpathy`, `/p2p-teacher`.

---

## 📡 Live Specs

Цены/квоты/баги моделей обновляются отдельно (~раз в 1-2 недели). Положи свежий `live_specs_YYYYMMDD.md` в `_live/`/`vendors/` и напиши `full ui menu` — дата и версия обновятся автоматически.

Текущие: `vendors/live_specs_20260617.md` (v8.5, 10 вендоров, Fable 5, Opus 4.8).

---

## 🔬 Scientific Sources

Интегрированные техники — это **паттерны промптинга, вдохновлённые** открытыми работами (код не включён; P2P под MIT). Полный список с arXiv — `docs/TECHNIQUES_v8C3.md` и `NOTICE`.  
Авторские механизмы P2P (QUORUM, SCOPE.HELM, ATLAS, SIR, VECTOR…) — независимые разработки проекта.

---

## Документация

| Файл | Когда читать |
|------|--------------|
| **[docs/INSTALL_GUIDE.md](docs/INSTALL_GUIDE.md)** | Методы установки + troubleshooting |
| **[docs/TECHNIQUES_v8C3.md](docs/TECHNIQUES_v8C3.md)** | Описание 6 ON-DEMAND техник |
| **[docs/MODULE_REFERENCE.md](docs/MODULE_REFERENCE.md)** | Справочник всех модулей |
| **[docs/MODES_GUIDE.md](docs/MODES_GUIDE.md)** | PILOT режимы: Co-Pilot / Auto / Manual |
| **[docs/MINDMAP_v8C3.md](docs/MINDMAP_v8C3.md)** | Карта системы |
| **[docs/ARCHITECTURE_MAP.md](docs/ARCHITECTURE_MAP.md)** | Dev-карта архитектуры (maintainer) |
| **[CHANGELOG.md](CHANGELOG.md)** | История версий |

---

## Атрибуции

`/p2p-karpathy` и Template M вдохновлены философией Andrej Karpathy. Интегрированные техники ON-DEMAND — паттерны промптинга по открытым работам. Полный список — [NOTICE](NOTICE).

---

## Помощь и обратная связь

- Не запускается → [`docs/INSTALL_GUIDE.md`](docs/INSTALL_GUIDE.md)
- Не понятно как пользоваться → `/p2p-teacher` после установки
- Багрепорт / предложение → [Issues](https://github.com/sanic732/P2P-4PDA-edition/issues) или 4PDA-ветка

**Багрепорты:** GitHub Issues. **Лицензия:** MIT (форкай, модифицируй; не вырезай `NOTICE`).  
**Автор:** sanic732 · **4PDA:** [Prompt to Prompt 8 NEXUS](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143218594)
