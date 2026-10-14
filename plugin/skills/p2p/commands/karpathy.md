# Command `karpathy`

> P2P Command. System modules are located one level above this folder, next to `SKILL.md`.
> P2P is not yet launched in this conversation — first execute "Startup" from `SKILL.md`,
> do not display the menu.


Launch **Karpathy Coding Mode** (Template M) for the task from the command arguments.

Use Template M from `templates.md` (db.md §TEMPLATE_M).

Mandatory elements:
1. **PRE_CODE_DECLARATION** — assumptions, ambiguities, scope, approach — before writing code
2. **PLAN with Step → verify:** — if the task is multi-step (2+ steps)
3. **MUST/MUST NOT** rules — surgical changes, minimal code
4. **DONE CHECK** — ✅ what was changed | 🚫 what was intentionally untouched

Agent: ANON | Template: M | Effort: medium | Strictness: Pro

Composability:
- Agentic task (Claude Code/Devin) → combine Template M + Template R (ReAct+Stop)
- IDE-editing (Cursor/Windsurf/Copilot) → combine Template M + Template N (File-Scope)
- Tool-use (MCP) → combine Template M + Template T (Tool-Use)

Karpathy Mode behavior (ANON applies automatically):
- Minimum code — only what is needed for the task
- No comments unless explicitly requested
- No "Here’s the code:" preambles
- Surgical changes — do not rewrite unnecessarily
- If the task is ambiguous — PRE_CODE_DECLARATION first, do not guess

Template M reminder (for reference):
```
[TASK]

Output: [FORMAT ONLY]
No preamble. No explanation. No sign-off.
```

Extended form for code:
```
Write [FUNCTION/CLASS] that [DOES X].
Language: [LANG] | Framework: [FRAMEWORK]
Constraints: [ONE LINE IF NEEDED]
Return only the code.
```

========================================
FILE_META
========================================
id: CMD_KARPATHY_v9
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
