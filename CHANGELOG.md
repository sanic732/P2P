# CHANGELOG

Полная история версий — [`docs/CHANGELOG_v8C3.md`](docs/CHANGELOG_v8C3.md).
Этот файл — release-level changelog публикации в GitHub.

---

## [v8C.3-ALPHA] — 2026-06

### Added
- **PILOT** — единая ось управления уровнем помощи (Co-Pilot / Auto-Pilot / Manual + GLASS COCKPIT). Оборачивает DEEP_THINK_VALUE_GATE, IDEALIST/PRAGMATIST, 9-step contract, SIR Scanner. Выбор буквой `C/A/M`. `USER_LEVEL ↔ PILOT_MODE`; сессионный override через sandbox `PERSONA_HINT`.
- **SHERPA** — проводник по штатным фичам среды (апгрейд teacher → inline-коучинг). Флаг `SHERPA: auto|on|off` + `/sherpa`.
- **6 ON-DEMAND модулей** (меню [35-40]): `!rag` (RAPTOR, LongRAG, adRAP) · `!reasoning` (Self-Consistency, rStar-Math/MCTS, s1) · `!routing` (Semantic/Cascade/Cost-Aware, RouteLLM) · `!compression` (LLMLingua, Gist Tokens) · `!security` (SelfCheckGPT, injection defense) · `!optimization` (OPRO, APE, EvoPrompt). Источники — `docs/TECHNIQUES_v8C3.md`.
- **VERSION_COMPAT** — `v8C2/v8C3 on/off` + 6 MODULE-флагов (`false|true|auto|or`); **CONFLICT_RESOLVER v1.0** при конфликте техник.
- **Арт-меню** — опциональный `!art.md`: ASCII-баннеры режимов на старте (вертикально), выбор буквой.
- **Claude Fable 5** — добавлена как T4-модель (Arena #1 Agent, `claude-fable-5`).
- `docs/`: MODES_GUIDE, TECHNIQUES_v8C3, MODULE_REFERENCE, MINDMAP, ARCHITECTURE_MAP (карта архитектуры + Route Changelog).
- `NOTICE` — атрибуции интегрированных техник + дисклеймер про авторские имена P2P.

### Changed
- Live specs → `live_specs_20260617.md` (v8.5, 10 вендоров, Fable 5, Opus 4.8).
- Манифесты: `p2p-v8c2` → `p2p-v8c3`, версия `8.2.0` → `8.3.0`.
- TARGET CONTEXT CHECK в Contract Builder (host ≠ target: подписка/лимиты/разбивка задачи).
- intent §2.5 MODULE HANDOFF — маршрутизация в новые модули.
- `docs/` — заменена на EN-документацию (INSTALL_GUIDE, TECHNIQUES_v8C3, MODULE_REFERENCE, MINDMAP, MODES_GUIDE, ARCHITECTURE_MAP); добавлен `tools/` с python-чекерами.

### Fixed
- Унифицирована схема активации модулей (`trigger`/`trigger_keywords` → `triggers`).
- FABRICATION_SCAN (VECTOR/ANON) больше не блокирует собственные техники: SC ≠ USC, MCTS ≠ ToT, RAPTOR ≠ GoT.
- Висячая якорная ссылка `#DB_TASK_TYPE` исправлена; 0 битых якорей.
- Версионный дрейф `v8C.1`/`v8C.2` в теле модулей вычищен.

### Verified
- Consistency: 0 битых якорей, паритет дистрибуций, 0 терминологического рассинхрона.
- Симуляции 6 сценариев (генерация, QUORUM, feedback-loop, cross-model, conflict-resolver) — механики отрабатывают как заявлено.

### Notes
- Интегрированные техники — паттерны промптинга, вдохновлённые открытыми работами (код не включён). P2P остаётся под **MIT**.
- Drop-in замена для v8C.2. v8C.3 модули по умолчанию активны в alpha-сборке; для прода `v8C3=off` экономит токены.

---

## [v8C.2] — 2026-05-15 — публичная публикация на GitHub

Первая публикация P2P v8C.2 как открытого GitHub-проекта в репозитории
`sanic732/P2P-4PDA-edition` (зеркало для 4PDA-сообщества).

### Что вошло в релиз

- `cowork + code/` — плагин для Claude Code и Cowork (skills, agents, commands,
  pack scripts, `.claude-plugin/` манифесты)
- `for chat (project)/` — модули для Claude.ai Projects/Chat и API
  (BASE, ON-DEMAND, _live/, vendors/)
- `docs/` — 10 markdown-гайдов (install, teacher, FAQ, changelog, agents…)
- Корневые: `README.md`, `LICENSE` (MIT), `NOTICE`, `.gitignore`,
  `.claude-plugin/marketplace.json` (для `/plugin marketplace add`)

### Ассеты релиза

- `p2p-v8c2.plugin` — собранный one-click пакет (Cowork/Claude Code import)
- `p2p-v8C.2-cowork-code.zip` — исходники плагина для самостоятельной сборки
- `p2p-v8C.2-for-chat.zip` — модули для Chat/Projects/API

### Pre-release fixes 2026-05-15

При подготовке к публикации проведена сквозная валидация v8C.2:

- ✅ `plugin.json` — валиден, name=p2p-v8c2, version=8.2.0
- ✅ `marketplace.json` (внутри плагина) — валиден
- ✅ `.claude/commands/` — 11 файлов (`/p2p` + 10 субкоманд, включая `/p2p-teacher`)
- ✅ `.claude/agents/` — 8 sub-agent файлов (QUORUM)
- ✅ `.claude/skills/` — 2 skill (`p2p`, `p2p-teacher`)
- ✅ `pack.ps1` собирает чистый `.plugin` (210 KB, без pack-скриптов и `.zip`/`.plugin` мусора внутри)
- ✅ `for chat (project)/` — 25 верхне-уровневых файлов (3 BASE + 19 ON-DEMAND + 3 индекс/мастер), `_live/` × 4, `vendors/` × 4
- ✅ `docs/` — 10 гайдов, все на месте
- 🔧 `cowork + code/.claude-plugin/plugin.json` — поле `homepage` обновлено
  с placeholder-URL `p2p-project/p2p-v8c2` на актуальный
  `sanic732/P2P-4PDA-edition`; добавлен блок `repository`.
- 🔧 Создан корневой `.claude-plugin/marketplace.json` с `source: "./cowork + code"`,
  чтобы `/plugin marketplace add <git-url>` работал из корня репо
  (внутренний `cowork + code/.claude-plugin/marketplace.json` сохранён для
  локальной сборки).
- 🔧 `cowork + code/INSTALL.md` — раздел "Метод 2 — Marketplace" обновлён
  реальной командой импорта с этого репо (`sanic732/P2P-4PDA-edition`)
  вместо плейсхолдера `<user>/p2p`.
- 🔧 `docs/INSTALL_GUIDE.md` — добавлен **Метод 0 — GitHub marketplace** в начало
  как рекомендованный one-liner.

Никаких ломающих изменений в логике системы, агентах, базе знаний или
вендорских модулях не вносилось. CAPSULE и state-файлы из v8C.1 совместимы.

---

## [v8C.1] и ранее

См. [`docs/CHANGELOG.md`](docs/CHANGELOG.md) для полной истории
(v8C.0 → v8C.1 → v8C.2 и v7C.x).
