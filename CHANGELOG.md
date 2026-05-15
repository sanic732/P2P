# CHANGELOG

Полная история версий — [`docs/CHANGELOG.md`](docs/CHANGELOG.md).
Этот файл — release-level changelog публикации в GitHub.

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
