# P2P 9.0 — Installation

A single plugin works everywhere: in web chat, in Claude Desktop, in Cowork, and in Claude Code.
The more capable the environment, the more P2P takes advantage of it automatically:

| Environment | Commands | QUORUM | Menu Selection |
|---|---|---|---|
| Web chat and Claude Desktop | `/p2p`, `/p2p:quorum` … | roles take turns in a single response | selection dialog if supported, otherwise by number |
| Cowork | same | subagents `p2p:iris`, `p2p:axiom` … | selection dialog |
| Claude Code | same, plus short `/quorum`, `/teacher` … | subagents | selection dialog |
| Skill without plugin, any plan | `/p2p`, then `quorum …` | roles take turns in a single response | dialog or number |

P2P is launched only by explicit trigger — `/p2p`, `старт`, or a command like `/p2p:quorum`. It does not activate itself based on request context.

---

## 1. Plugin — Web Chat, Claude Desktop, Cowork (Paid Plans)

**From file:** **Customize** → **Plugins** → **Add** → **Upload plugin** → `p2p.plugin`.
The plugin will not update automatically this way: each new version must be re-uploaded.

**From repository:** **Customize** → **Plugins** → **Add** → **Add marketplace** →
`sanic732/P2P` → install **p2p**.

The plugin is saved to your account and syncs to Claude Code when using the same account.

**Previously `p2p-v8c3`.** The plugin is now named `p2p`, enabling shorter commands. If installed from the repository, the migration happens automatically: the marketplace recognizes the old name. If uploaded from file — remove the old `p2p-v8c3` and upload `p2p.plugin`.

---

## 2. Claude Code

```
/plugin marketplace add sanic732/P2P
/plugin install p2p@P2P
```

Launch — `/p2p`. Commands — `/p2p:quorum`, `/p2p:teacher`, etc.; if the name is not taken by another command, the short form `/quorum`, `/teacher` is sufficient.
Inspect plugin without installing: `claude --plugin-dir <unpacked folder>`.

---

## 3. Skill — Any Plan, Requires Code Execution

1. **Settings** → **Capabilities** — enable Code execution.
2. **Customize** → **Skills** → **+** → **Create skill** → **Upload a skill** →
   `P2P_9_skill_claude.zip`.
3. Launch — `/p2p` or `старт` in chat.

The Skill does not have separate slash-commands or subagents: invoke commands by name — `quorum <task>`, `teacher` — or following `/p2p`.

---

## 4. Project or Chat Without Skill

File-based version of P2P 9.0 (`P2P_9_files.zip` archive): all modules as files, attach to chat; see quick start in its `README.md`.

---

## 5. API

One system prompt from all modules — the file version of P2P carries the assembly order.

---

## Verification

```
/p2p          → short greeting without menu, status line [P2P 9.0 | Environment: … | Guardian: …]
/p2p:menu     → menu [0]–[42] and selection dialog if supported by the environment
/p2p:teacher  → interactive course
```
