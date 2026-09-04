# CLAUDE.md — P2P Claude Edition

> Local rules for this edition. Applies within this folder.
> Release number lives in the YAML frontmatter of each file — nowhere else.

## Context
P2P — Claude Edition meta-prompt system.
Optimized for Claude Fable 5 / Claude Opus 4.8 / Sonnet 4.6.
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
├── .claude-plugin/             ← plugin manifest only (marketplace.json lives at REPO ROOT)
│   └── plugin.json
├── .claude/
│   ├── agents/                 ← 8 sub-agent files
│   ├── commands/               ← /p2p-* commands
│   ├── skills/
│   │   ├── p2p/                ← main skill manifest + all core files
│   │   └── p2p-teacher/        ← teacher skill
│   ├── settings.json
│   └── CLAUDE.md               ← this file
├── INSTALL.md                  ← Quick start TL;DR
├── pack.sh / pack.ps1          ← packaging scripts
└── README.md
```
