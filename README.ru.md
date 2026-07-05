# P2P — Prompt-to-Prompt

> 🇷🇺 **Русский** · 🇬🇧 [English](README.md)

[![Version](https://img.shields.io/badge/version-v8.4.0-blue)]() [![License](https://img.shields.io/badge/license-MIT-green)]() [![Status](https://img.shields.io/badge/status-BETA-yellow)]() [![Editions](https://img.shields.io/badge/editions-C%20%C2%B7%20H%20%C2%B7%20N%20%C2%B7%20L-orange)]()

**Мета-промпт, который пишет промпты — и выполняет задачи.** Поток сознания на входе → выверенный промпт под нужную модель на выходе. Цель проекта: **убрать классический prompt engineering для рядового пользователя.**

Вы не должны знать, что такое Chain-of-Thought или как экранировать XML от prompt-injection. Вы просто описываете задачу — *«хочу приложение для учёта расходов, данные из экселя, тёмная тема»* — а P2P берёт на себя декомпозицию, маршрутизацию, подбор агентов и защиту от галлюцинаций «под капотом».

---

## Что такое P2P

P2P (Prompt-to-Prompt) — модульная оркестрирующая система, загружаемая в LLM и превращающая её в эксперта по prompt engineering. Архитектура **RAG** (BASE / LIVE / ON-DEMAND), консилиум из 8 агентов **QUORUM**, движок больших задач **SCOPE.HELM**, авто-обновляемые **Live Specs**.

**Философия:** ограничения, а не давление. Эмпирично, а не эстетично.

Проект прошёл путь от одного текстового промпта (v1) до мета-промпт-ОS (v8 NEXUS) — см. [историю эволюции](legacy/HISTORY.md).

### ⚡ [Интерактивная карта архитектуры](https://sanic732.github.io/P2P-4PDA-edition/p2p-map.html)

> **Полная карта системы: модули, агенты, команды, перекрёстные связи, потоки данных** — в одной интерактивной D3.js-визуализации с табами, фильтрами, анимацией и переключением RU/EN. Как связаны 8 агентов QUORUM, 11 команд и 6 ON-DEMAND модулей.

---

## 🧭 Выберите редакцию

Одна архитектура — четыре входа под разные хосты и форм-факторы. **Не уверены — берите ту, что заточена под вашу основную модель.**

| Редакция | Для кого | Хост | Старт |
|---|---|---|---|
| 🟦 **[claude-native](editions/claude-native/README.md)** (8C.3) | Работаешь в **Claude** (Code / Cowork / Projects) | только Claude | ~7K |
| 🟥 **[high](editions/high/README.md)** (8H.3) | Хочешь максимум / сидишь на **Grok** | 8 хостов (нативно Grok) | ~60K |
| 🟩 **[normal](editions/normal/README.md)** (8N.3) | Твоей модели нет среди «нативных» | любой из 8 | ~60K |
| 🟦 **[light](editions/light/README.md)** (8L.3) | Экономия токенов / лимит контекста / **новичкам** | универсальный | **~18K** |

📊 Подробное сравнение — [`editions/COMPARISON.md`](editions/COMPARISON.md) · 📖 расшифровка имён — [`NAMING.md`](NAMING.md).

---

## 🚀 Быстрый старт

> 📖 **Полная инструкция (Google Docs):** https://docs.google.com/document/d/e/2PACX-1vS2Xo8p7cEFYfrW7Lfxr2YxrbxSojmMp6-ueRgq3_9-Q-MGKeSiRUDuQmHSj1QUHXaHA3LFvYyPNI2e/pub

### Вариант A — плагин (Claude Code / Cowork)

```
/plugin marketplace add https://github.com/sanic732/P2P-4PDA-edition
/plugin install p2p-v8c3@p2p
```

Проверка: `/p2p` (главное меню) · `/p2p-teacher` (интерактивный курс). Обновление: `/plugin update p2p-v8c3@p2p`.

### Вариант B — чат / Projects / API (любой хост)

Загрузите `.md`-файлы выбранной редакции в Project Knowledge (или system prompt) и напишите `старт` / `/p2p`. Для Gemini — можно через NotebookLM (экономия токенов). Подробно — в INSTALL каждой редакции и [`docs/INSTALL_GUIDE.md`](docs/INSTALL_GUIDE.md).

Триггеры запуска: `/start` · `start` · `старт` · `/p2p` · `/menu`. Не виден интерфейс? Напишите `full ui menu`.

---

## 👥 8 агентов QUORUM

| Агент | Роль | Когда |
|-------|------|-------|
| 🟣 **IRIS** | Strategist & Cartographer | Карта задачи, скрытые зависимости, правильные вопросы |
| 🟢 **TECTON** | System Architect | Структура промпта, архитектура кода, Decision Trees |
| 🟡 **AXIOM** | Logician & Verifier | Red Team, дыры в логике, Confidence Score |
| 🟠 **VECTOR** | Optimization & Security | Защита от prompt-injection, санитизация |
| 🟤 **DATOS** | Data Analyst | Фактчекинг, эмпирическая верификация (на Grok — X Firehose) |
| ⚫ **ANON** | Code Specialist / Security | Production-ready код, Stop Conditions (в 8C.3 — безопасностник) |
| 🔵 **ARCHITECTON** | Integrator | Разрешение конфликтов между агентами, UI/UX |
| ☀️ **HELIOS** | Final Synthesizer | Сборка хора 7 агентов в чистый результат |

На **Grok** (high) агенты запускаются нативно параллельно (**Heavy-16**, в 5-7× быстрее); на остальных хостах — симулированный QUORUM.

---

## 📡 Live Specs

Цены/квоты/баги моделей обновляются отдельно (~раз в 1-2 недели) из выделенного Gist (`live_specs.md`, latest). Система на старте проверяет способность к web-fetch и работает в режиме онлайн-обновления или из вшитого snapshot. Механика — в [`editions/COMPARISON.md`](editions/COMPARISON.md#механика-live-specs-что-нового-в-поколении-3).

---

## 📚 Документация

| Раздел | Что внутри |
|---|---|
| **[NAMING.md](NAMING.md)** | Расшифровка имён C/H/N/L/A/G, версий, статусов |
| **[FAQ.md](FAQ.md)** | Частые вопросы: установка, хосты, токены, траблшутинг |
| **[editions/COMPARISON.md](editions/COMPARISON.md)** | Сравнение 4 редакций + механика Live Specs |
| **[CHANGELOG.md](CHANGELOG.md)** | История версий (v1 → v8) |
| **[legacy/HISTORY.md](legacy/HISTORY.md)** | Нарратив эволюции проекта |
| **[docs/](docs/)** | Архитектура, техники, режимы PILOT, mindmap |

---

## 🔬 Scientific Sources & атрибуции

Интегрированные ON-DEMAND техники (RAPTOR, LongRAG, Self-Consistency, MCTS, LLMLingua, OPRO…) — это **паттерны промптинга, вдохновлённые** открытыми работами; чужой код не включён, проект под **MIT**. `/p2p-karpathy` и Template M вдохновлены философией Andrej Karpathy. Авторские механизмы P2P (QUORUM, SCOPE.HELM, PILOT, ATLAS…) — независимые разработки. Полный список с источниками — [`NOTICE`](NOTICE) и [`docs/TECHNIQUES_v8C3.md`](docs/TECHNIQUES_v8C3.md).

---

## Помощь и обратная связь

- Не запускается → [`docs/INSTALL_GUIDE.md`](docs/INSTALL_GUIDE.md) или [`FAQ.md`](FAQ.md)
- Не понятно как пользоваться → `/p2p-teacher` после установки
- Багрепорт / предложение → [Issues](https://github.com/sanic732/P2P-4PDA-edition/issues) или 4PDA-ветка

**Лицензия:** MIT (форкай, модифицируй; не вырезай `NOTICE`). **Автор:** sanic732 · **4PDA:** [Prompt to Prompt 8 NEXUS](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=137565576)
