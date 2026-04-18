# P2P v1.1 — Installation: Cowork

## Requirements
- Cowork (current version)
- Plugin host with skills and sub-agents support

## Installation

### Option A — via setup-cowork skill (recommended)

In Cowork, type:
```
setup p2p
```

or follow the guide from the `setup-cowork` skill manually.

### Option B — Manual Installation

1. Open the Cowork plugin directory (platform-dependent — see Cowork documentation).
2. Copy `.claude/skills/p2p/`, `.claude/agents/`, `.claude/commands/` to the plugin directory.
3. Reload Cowork.

## Verification

In Cowork:
```
/p2p
```

A 32-item menu should appear.

## Cowork-Specific Behavior

- ✅ **Skills, sub-agents, slash commands** — all work as in Code.
- ✅ **SCOPE.HELM GUARDIAN: SOFT** — Cowork shows limits natively; GUARDIAN does not duplicate, only reminds at 80%.
- ✅ **CAPSULE** — written to plugin state directory.
- ✅ **Skills from Cowork ecosystem** available in parallel: `pdf`, `docx`, `pptx`, `xlsx` — P2P can generate prompts that those skills then execute.

## Cross-Skill Workflow

P2P v1.1 combines well with other Cowork skills:

```
Use p2p-architecton to generate a prompt for building a pptx presentation,
then use the pptx skill to assemble it
```

Or:

```
/p2p-scope large research project
→ SCOPE.HELM splits into 5 chats
→ for each brief you can call the docx or pdf skill
```

## Troubleshooting

Same as Code — see `INSTALL_CODE.md` Troubleshooting section. All main issues and solutions are identical.
