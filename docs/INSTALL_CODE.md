# P2P v1.1 — Installation: Claude Code

## Requirements
- Claude Code CLI (any current version)
- Access to `Bash`, `Read`, `Write`, `Edit`, `Grep`, `Glob`, `Agent` tools (standard Code set)

## Installation (3 Steps)

### Step 1 — Copy `.claude/`

```bash
cp -r "P2P v1.1/.claude" /path/to/your/project/
```

Structure that appears in your project:
```
your-project/
└── .claude/
    ├── settings.json
    ├── skills/p2p/         (24 modules)
    ├── agents/             (8 sub-agents)
    └── commands/           (9 slash commands)
```

### Step 2 — Configure `p2p.config.md`

Open `.claude/skills/p2p/p2p.config.md` and fill in:

```
> PROJECT_NAME: "MyApp"
> AUTHOR_NAME: "Your name"
> PROJECT_STACK: "React 19 + TypeScript + Tailwind"
> OUTPUT_LANG: "en"
> CORTEX_BUILTIN: "true"
```

This is the **only** file you edit. Everything else is read-only.

### Step 3 — Run

```bash
cd /path/to/your/project
claude
```

In the chat:
```
/p2p
```

You'll get a 32-item menu. Alternatively use any of the 9 slash commands (`/p2p-quorum`, `/p2p-scope`, ...) or just type: `generate a prompt for Gemini for a landing page`.

## What's Enabled by Default

- ✅ Skill `p2p` — auto-triggers on key phrases
- ✅ 8 sub-agents (Agent tool, parallel spawn via QUORUM)
- ✅ 9 slash commands
- ✅ Cortex built-in (Exploration / Metrics / RM)
- ✅ SCOPE.HELM env-aware (GUARDIAN OFF in Code, SPLITTER → TodoWrite)
- ✅ Live specs override

## What's Disabled (opt-in)

- ❌ Hooks in `settings.json` — all `_disabled: true`. Enable manually if needed.
- ❌ Auto anti-pattern scan on every Write — scaffold is ready, activation is optional.

## Permissions (`.claude/settings.json`)

**allow** (no confirmation):
- Read, Grep, Glob, Edit
- Write only to `.claude/state/` and `docs/`
- Safe Bash: mkdir, ls, cp

**ask** (with confirmation):
- git commit/push
- Write to `.claude/skills/p2p/` (protects skill internals)

**deny** (blocked):
- rm -rf, git push --force
- curl
- Write to /etc/, ~/.ssh/

Adjust as needed — these are just starting defaults for the release.

## Slash Commands Cheatsheet

```
/p2p                                    # main menu (32 items)
/p2p-quorum write a prompt for X        # multi-agent council
/p2p-chain decompose pipeline X         # Chain Mode
/p2p-feedback my prompt ... doesn't work because ...
/p2p-explore I want to do X but don't know how
/p2p-metrics                            # session report
/p2p-scope large project X              # SPLITTER + TodoWrite
/p2p-capsule                            # handoff Capsule to .claude/state/
/p2p-atlas                              # audit modules
```

## Sub-agents

Available via Agent tool. QUORUM (`p2p-quorum`) automatically spawns others in parallel by task type. You can call them directly:

```
Use p2p-tecton to develop an XML scaffold for a system prompt
```

or

```
Run p2p-axiom on my prompt: ...
```

## State Persistence

In Code, P2P state persists in `.claude/state/`:
- `p2p_metrics.json` — session_metrics counter between sessions
- `p2p_memory.json` — routing_memory data
- `capsule_<timestamp>.md` — Context Capsules from SCOPE.HELM
- `brief_<N>.md` — briefs from SPLITTER

On next launch the skill reads from there automatically.

## Troubleshooting

**Skill not triggering?**
→ Verify `.claude/skills/p2p/SKILL.md` is present, restart `claude`.

**Slash commands not visible?**
→ `.claude/commands/` must be in the project root. `ls .claude/commands` → should show 9 .md files.

**Sub-agents not found?**
→ `.claude/agents/` also in the root. `ls .claude/agents` → 8 p2p-*.md files.

**Does `start` / `СТАРТ` work instead of slash?**
→ Yes, `start` / `СТАРТ` / `/start` / `p2p` all show the menu — for compatibility with v1.0 users.

**ENV detected incorrectly?**
→ Force it in `p2p.config.md`: `> ENV: "code"`.

## Updating (when v1.2 releases)

```bash
# Backup your config
cp .claude/skills/p2p/p2p.config.md /tmp/

# Replace .claude/
rm -rf .claude/skills/p2p .claude/agents .claude/commands
cp -r "P2P v1.2/.claude/"* .claude/

# Restore config
cp /tmp/p2p.config.md .claude/skills/p2p/
```

From v1.1 onwards, updates do not break the config — it lives in a separate file.
