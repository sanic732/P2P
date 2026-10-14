---
source_id: SANDBOX_v9
version: "9.0"
module_type: on_demand
depends_on: [_preloader.md, user_context.md]
tags: [sandbox, user-overrides, session-config, quick-rules]
triggers: [sandbox, песочница, override, session config, quick rule]
---

# sandbox.md — User Editable Sandbox

> User overrides zone for the session.
> Priority: overrides PRELOADER for the current session. Does NOT modify core.

---

## SANDBOX BLOCK (edit this, leave the rest alone)

```
╔══════════════════════════════════════════════════════════════╗
║  SANDBOX — USER EDITABLE ZONE (P2P)                          ║
║  ✏ Edit ONLY this zone                                       ║
║  Priority: overrides PRELOADER for the current session       ║
╚══════════════════════════════════════════════════════════════╝

[SANDBOX — USER EDITABLE]

> QUICK_RULE: ""
  // Single-line priority rule for the session.
  // Examples: "Always respond in Russian" | "No bullet points" | "Code in Python only"

> PROJECT_OVERRIDE: ""
  // Quick replacement of PROJECT_CARD from PRELOADER.
  // Example: "React 19 + TypeScript + Supabase, mobile habit-tracker"

> TONE_OVERRIDE: ""
  // Session tone. Overrides Tone Spectrum from writing.md.
  // Options: "formal" | "professional" | "casual" | "technical" | "brief" | "narrative"

> PERSONA_HINT: ""
  // User expertise level — affects the depth of explanations.
  // Examples: "I’m a beginner, explain thoroughly" | "I’m an expert, skip basics"

> SESSION_GOAL: ""
  // Goal of the current session. Injected into Memory Bridge as project_state.
  // Example: "Write 5 prompts for UI component generation"

> MODEL_OVERRIDE: ""
  // Forced model/Extended Thinking mode.
  // Examples: "[flagship Claude id: live_specs.md] effort=high" | "[balanced Claude id: live_specs.md] effort=low"

> AGENT_PREFERENCE: ""
  // Preferred agents for the session.
  // Example: "IRIS, TECTON, HELIOS only" | "skip ANON"

> LANG: ""
  // Forced output language: any language by name or code ("es", "Deutsch", "uk", "日本語")

══════════════════════════════════════════════════════════════
```

---

## §1. ORDER OF APPLICATION

```
PRELOADER (defaults)
  ↓
p2p.config.md in the project root (user persistent profile)
  ↓
sandbox.md (this file — session overrides)
  ↓
user message (highest priority)
```

In case of conflict, the lower layer wins.

---

## §2. WHEN TO USE

| Scenario | SANDBOX Field |
|----------|---------------|
| Change language for the session | `LANG` |
| Change project stack | `PROJECT_OVERRIDE` |
| Reduce pedagogical tone | `PERSONA_HINT: "expert"` |
| Enable Karpathy Mode | `QUICK_RULE: "Karpathy mode, no fluff"` |
| Force the balanced Claude model instead of the flagship | `MODEL_OVERRIDE: "[balanced Claude id: live_specs.md]"` |
| Disable agents | `AGENT_PREFERENCE: "no agents, single pass"` |

---

## §3. VALIDATION

Upon loading sandbox.md, the system:
1. Reads each field.
2. If non-empty — writes to the session state (session_template.md); live_specs.md is attached by the user, read-only.
3. Logs the override source in CHART.
4. At each step, checks whether SANDBOX contradicts safety rules
   (G-errors, model deadlines). Safety always overrides SANDBOX.

---

## §4. ANTI-PATTERNS

- **SP-1:** Filling QUICK_RULE with long text — it is a single-line entry.
- **SP-2:** Placing sensitive data in PROJECT_OVERRIDE — it will enter the cache.
- **SP-3:** Conflicting fields (LANG=ru + QUICK_RULE="answer in English").
- **SP-4:** Using SANDBOX instead of the persistent profile (p2p.config.md) for permanent settings.

---

<!-- SOURCE_META: type=on-demand | priority=4 | sandbox=true | session-overrides=true -->


========================================
FILE_META
========================================
id: SANDBOX_v9
type: on_demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
