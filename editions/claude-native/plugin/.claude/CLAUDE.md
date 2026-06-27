# CLAUDE.md — P2P v8C.3 Claude Edition

> Local rules for the v8C.3 repo. Applies within this folder.

## Context
P2P v8C.3 — Claude Edition meta-prompt system.
Optimized for Claude Fable 5 / Claude Opus 4.8 / Sonnet 4.6.
XML-native, TRI_MODE_BRIDGE v3, QUORUM 8 agents, interactive teacher mode, VERSION_COMPAT.

## Mandatory rules

1. **Before any change** — read the target file in full
2. **API strings** — only current: `claude-fable-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-sonnet-4-6`
3. **NEVER** pass temperature when thinking=enabled (G7 → HTTP 400)
4. **NEVER** use budget_tokens (removed from API)
5. **DEADLINE 2026-06-15** — remove all mentions of `claude-*-4-20250514` (HTTP 400/404)
6. **DEADLINE 2026-07-24** — remove `deepseek-chat` / `deepseek-reasoner` aliases
7. **Versioning** — every change = bump + entry in CHANGELOG

## Architectural invariants

1. XML-native for Claude — do not remove tags for "simplicity"
2. Modular loading (BASE/LIVE/ON-DEMAND) — never monolith
3. YAML frontmatter on all files
4. File language: English for instructions; comments bilingual (RU+EN)
5. Tests: 3 cases (simple/medium/adversarial) before commit
6. Plugin manifest `.claude-plugin/plugin.json` synced with system version

## Structure

```
v8C.3-cowork-code/
├── .claude-plugin/             ← plugin manifest only (marketplace.json lives at REPO ROOT)
│   └── plugin.json
├── .claude/
│   ├── agents/                 ← 8 sub-agent files
│   ├── commands/               ← 11 /p2p-* commands (+ p2p-teacher)
│   ├── skills/
│   │   ├── p2p/                ← main skill manifest + all core files
│   │   └── p2p-teacher/        ← teacher skill
│   ├── settings.json
│   └── CLAUDE.md               ← this file
├── INSTALL.md                  ← Quick start TL;DR
├── pack.sh / pack.ps1          ← packaging scripts
└── README.md
```

## v8C.3 new vs v8C.2

- Claude Fable 5 added as T4 FULL+ model (Arena #1 Agent; `claude-fable-5`)
- VERSION_COMPAT system: v8C2/v8C3 on/off + 6 MODULE flags
- CONFLICT_RESOLVER v1.0: activates when both v8C2 and v8C3 are on
- Dynamic menu [35-40]: items shown only when corresponding module is loaded
- 6 new ON-DEMAND modules: !rag, !reasoning, !routing, !compression, !security, !optimization
- STARTUP_LOGO: ASCII P2P art on /start
- Language: all .md files in English; output defaults to Russian (changeable via /lang)
- Live specs: live_specs_20260617.md (v8.4, 10 vendors, Fable 5 added)
