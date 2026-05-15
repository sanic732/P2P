# P2P v8C.2 · Claude Native Edition
### Distributed Cognitive Orchestrator — Meta-Prompt System

> Мета-промпт, который пишет другие промпты.
> Хост: Claude. Цели: Claude / GPT / Gemini / Grok / DeepSeek / Qwen / Kimi / GLM.

**Версия:** 8C.2 (8.2.0) · Claude Native Edition
**Лицензия:** MIT
**Статус:** Release · 14.05.2026
**Платформа:** Claude Opus 4.7 / Sonnet 4.6
**Зеркало для:** [4PDA-сообщества «Prompt to Prompt 8 NEXUS»](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143218594)

---

## Что такое P2P

P2P (Prompt-to-Prompt) — модульная оркестрирующая система, загружаемая в Claude и превращающая его в эксперта по prompt engineering. Вместо ручного написания промптов вы описываете задачу — система сама применяет нужную архитектуру, защитные механизмы и model-specific форматирование.

**Архитектура:** Foundation → Safeguards → Execution
**Философия:** ограничения, а не давление. Эмпирично, а не эстетично.
**Суть:** убить классический prompt engineering для обычного пользователя — вы кидаете в чат поток сознания, а P2P за вас раскладывает на 9D-intent, выбирает агентов, ставит Stop Conditions и защищается от галлюцинаций.

---

## Что в этом релизе

```
P2P-4PDA-edition/
├── README.md                    ← вы здесь
├── LICENSE                      ← MIT
├── NOTICE                       ← атрибуции (Karpathy и др.)
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
│   ├── !*.md                                       (ON-DEMAND, 19 модулей)
│   ├── _live/                                      (4 файла)
│   └── vendors/                                    (tier1-4)
└── docs/                        ← гайды, FAQ, changelog
```

**Зачем две папки:** в версиях v7C.x — v8C.1 всё лежало в одной `skills/p2p/` — Chat-пользователь грузил `.claude/` тоже, теряя ~50% контекста. В v8C.2 каждый use-case получает только нужное.

| Где работаешь | Папка | Что делать |
|---------------|-------|------------|
| Claude.ai **Projects** | `for chat (project)/` | Загрузить в Project Knowledge |
| Claude.ai **Chat** | `for chat (project)/` | Скопировать `_master.md` в system prompt |
| **API** (anthropic-sdk) | `for chat (project)/` | Собрать `system_prompt` из BASE-файлов |
| **Cowork** (desktop) | `cowork + code/` | `pack.ps1` → drag-drop `.plugin` |
| **Claude Code** (CLI) | `cowork + code/` | `/plugin marketplace add` или `pack.sh` |

---

## Установка — 4 рекомендованных пути

### 1. ⭐ GitHub-marketplace (Claude Code, рекомендуется)

```
/plugin marketplace add https://github.com/sanic732/P2P-4PDA-edition
/plugin install p2p-v8c2@p2p
```

Один раз — навсегда. Обновления подтягиваются автоматически по `git pull` под капотом.

### 2. Скачать `.plugin` из релиза (Cowork desktop / Claude Code)

1. [Открыть последний релиз](https://github.com/sanic732/P2P-4PDA-edition/releases/tag/v8C.2)
2. Скачать `p2p-v8c2.plugin`
3. **Cowork:** Settings → Skills → "+" → Upload a skill → выбрать файл
3. **Claude Code:** `/plugin install /путь/к/p2p-v8c2.plugin`

### 3. Скачать ZIP-архив `cowork + code` (Cowork desktop)

1. Скачать [`p2p-v8C.2-cowork-code.zip`](https://github.com/sanic732/P2P-4PDA-edition/releases/tag/v8C.2)
2. Распаковать
3. Запустить `pack.ps1` (Windows) или `pack.sh` (Linux/macOS)
4. Получившийся `.plugin` импортировать как в п.2

### 4. Скачать ZIP-архив `for chat` (Claude.ai Projects / Chat / API)

1. Скачать [`p2p-v8C.2-for-chat.zip`](https://github.com/sanic732/P2P-4PDA-edition/releases/tag/v8C.2)
2. Распаковать
3. **Projects:** загрузить файлы в Project Knowledge (минимально — `_preloader.md`, `!!core_v8C.md`, `_live/MANIFEST.md`, `_live/live_core.md`, `_live/live_claude.md`)
4. **Chat:** скопировать `_master.md` в system prompt
5. **API:** собрать `system_prompt` по инструкции из [`docs/ASSEMBLY_GUIDE.md`](docs/ASSEMBLY_GUIDE.md)
6. В чате: `СТАРТ`

Полный гайд со всеми 6 методами и troubleshooting — [`docs/INSTALL_GUIDE.md`](docs/INSTALL_GUIDE.md).

---

## Live Specs — почему данные о моделях не лежат в репо

Цены, квоты, баги моделей, retire-даты, AAII-метрики, новые ошибки роутинга — всё это меняется каждые 1-2 недели. Хардкодить такие данные в релиз — значит выпускать устаревший релиз сразу.

P2P-система читает **Live Specs** из `_live/` (Chat-ветка) и `vendors/` (Code-ветка). Эти файлы поставляются в момент релиза по состоянию на дату сборки, но **актуальные дельты публикуются вне релизного цикла** на форуме:

→ **[Актуальные Live Specs от 12.05.2026](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143350511)** (Grok migration 15.05, Gemini G13 worsened, Claude thinking API breaking, DeepSeek promo cutoff)

Подпишитесь на ветку — получите уведомление о следующем обновлении.

---

## Что нового в v8C.2 vs v8C.1

- **One-click импорт** — собирается в `.plugin` файл, drag-drop в Cowork или `/plugin install` в Claude Code
- **`/p2p-teacher`** — интерактивный курс из 5 уровней (Quickstart → Commands → Agents → QUORUM → SCOPE.HELM), ~2 часа, по 1 уровню в день, с упражнениями и финальной сертификацией
- **Marketplace-импорт** — теперь работает через GitHub: `/plugin marketplace add` подтягивает `.claude-plugin/marketplace.json` из корня репо
- **Разделение архива** — две папки под Chat и Code/Cowork, без дубликации файлов
- **`docs/INSTALL_GUIDE.md`** (416 строк) — 5 методов установки с troubleshooting, offline-сценариями, обновлением, удалением

**Без поломок совместимости:** ON-DEMAND модули, базы знаний, агенты, vendors, CAPSULE — всё унаследовано из v8C.1. Drop-in replacement.

Детальный список — [`docs/ЧТО_НОВОГО.md`](docs/ЧТО_НОВОГО.md).

---

## 8 агентов QUORUM (без изменений с v8C.1)

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

## Дедлайны API (актуально на 05.2026)

| Дата | Действие |
|------|----------|
| 2026-05-15 12:00 PT | Grok: 5 моделей retire (`grok-4`, `grok-4-fast`, `grok-4-1-fast`, `grok-code-fast-1`, `grok-imagine-image-pro`) → миграция на `grok-4.3` |
| 2026-05-25 | Gemini: `gemini-3.1-flash-lite` preview shutdown (перешёл в GA) |
| 2026-05-31 | DeepSeek: окончание 75% promo на V4-Pro (цены × 4 после) |
| 2026-06-15 | Claude: удалить `claude-opus-4-20250514` → `claude-opus-4-7`, `claude-sonnet-4-20250514` → `claude-sonnet-4-6` |
| 2026-07-24 | DeepSeek: `deepseek-chat` → `deepseek-v4-pro` |

P2P v8C.2 уже использует актуальные API strings. Live Specs покрывают дельты между релизами.

---

## Документация

| Файл | Когда читать |
|------|--------------|
| **[docs/INSTALL_GUIDE.md](docs/INSTALL_GUIDE.md)** | 6 методов установки + troubleshooting |
| **[docs/TEACHER_GUIDE.md](docs/TEACHER_GUIDE.md)** | Гайд по `/p2p-teacher` |
| [docs/ИНДЕКС.md](docs/%D0%98%D0%9D%D0%94%D0%95%D0%9A%D0%A1.md) | Навигация по всей документации |
| [docs/НАЧАЛО_РАБОТЫ.md](docs/%D0%9D%D0%90%D0%A7%D0%90%D0%9B%D0%9E_%D0%A0%D0%90%D0%91%D0%9E%D0%A2%D0%AB.md) | Быстрый старт за 5 минут |
| [docs/ЧТО_НОВОГО.md](docs/%D0%A7%D0%A2%D0%9E_%D0%9D%D0%9E%D0%92%D0%9E%D0%93%D0%9E.md) | Изменения vs v8C.1 |
| [docs/AGENTS_GUIDE.md](docs/AGENTS_GUIDE.md) | 8 агентов QUORUM подробно |
| [docs/FAQ_И_ОШИБКИ.md](docs/FAQ_%D0%98_%D0%9E%D0%A8%D0%98%D0%91%D0%9A%D0%98.md) | G-errors + типичные вопросы |
| [CHANGELOG.md](CHANGELOG.md) | История версий |

---

## Атрибуции

`/p2p-karpathy` и Template M (Karpathy Mode) вдохновлены философией Andrej Karpathy ("constraints, not pressure"; "best prompt — no prompt, just clean context") и сообществом проекта [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills). Имплементация P2P — независимая. Полный список атрибуций — [NOTICE](NOTICE).

---

## Помощь и обратная связь

- Не запускается → [`docs/INSTALL_GUIDE.md`](docs/INSTALL_GUIDE.md) §Troubleshooting
- Не понятно как пользоваться → `/p2p-teacher` после установки
- Ошибка от Claude API → [`docs/FAQ_И_ОШИБКИ.md`](docs/FAQ_%D0%98_%D0%9E%D0%A8%D0%98%D0%91%D0%9A%D0%98.md) §G-errors
- Багрепорт / предложение → [Issues](https://github.com/sanic732/P2P-4PDA-edition/issues) или 4PDA-ветка

**4PDA родительский пост:** [Prompt to Prompt 8 NEXUS](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=143218594)
**Автор:** sanic732 · **License:** MIT
