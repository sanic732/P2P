# DEVELOPING — правила правки редакции C

> Правила для того, кто правит эту редакцию. Файл жил внутри поставки как CLAUDE.md
> и никогда не читался: `claude plugin validate` прямо говорит, что CLAUDE.md в корне
> плагина не загружается как контекст. Перенесён сюда 8.4.7 — он про разработку, а не
> про работу продукта.
> Release number lives in the YAML frontmatter of each file — nowhere else.

## Context
P2P — Claude Edition meta-prompt system.
Optimized for Claude Opus 5 / Fable 5.1 / Sonnet 5; поколение 4.6-4.8 поддерживается.
XML-native, TRI_MODE_BRIDGE v3, QUORUM 8 agents, interactive teacher mode, VERSION_COMPAT.

## Mandatory rules

1. **Before any change** — read the target file in full
2. **API strings** — only current: `claude-opus-5`, `claude-sonnet-5`, `claude-fable-5-1`, `claude-fable-5`,
   `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6`, `claude-sonnet-4-6` (generation 4.6+ is ACTIVE —
   retirement not sooner than Feb 2027, a legitimate cost choice)
3. **NEVER** pass temperature when thinking=enabled (G7 → HTTP 400)
4. **NEVER** use budget_tokens (removed from API)
5. **Versioning** — bump `version:` in the YAML frontmatter; describe the change in the
   edition CHANGELOG. Do not repeat the release number in file bodies.

## Architectural invariants

1. XML-native for Claude — do not remove tags for "simplicity"
2. Modular loading (BASE/LIVE/ON-DEMAND) — never monolith
3. YAML frontmatter on all files
4. File language: English for instructions; comments bilingual (RU+EN)
5. Tests: 3 cases (simple/medium/adversarial) before commit
6. Plugin manifest `.claude-plugin/plugin.json` synced with system version

## Structure

```
plugin/
├── .claude-plugin/             ← манифест плагина (marketplace.json лежит в КОРНЕ РЕПОЗИТОРИЯ)
│   └── plugin.json
├── agents/                     ← 8 sub-agent файлов
├── commands/                   ← /p2p-* команды
├── skills/
│   ├── p2p/                    ← главный скилл: манифест + все файлы ядра
│   └── p2p-teacher/            ← скилл обучения
├── settings.example.json       ← образец permissions + hooks (opt-in, не часть плагина)
├── INSTALL.md                  ← быстрый старт
└── pack.sh / pack.ps1          ← сборка .plugin
```

> Раскладка выправлена в 8.4.7: компоненты лежат в КОРНЕ плагина, а не в `.claude/`.
> Прежняя раскладка работала в Claude Code, потому что манифест перечислял пути явно,
> но загрузка `.plugin` на claude.ai падала: «No agent files found in specified
> directories: 'agents', '.claude/agents/p2p-anon.md' …».
