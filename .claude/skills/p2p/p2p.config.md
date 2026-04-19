# P2P v1.1 — User Configuration

> This is the **only** file you edit by hand.
> Fill in the fields for your project. Save. Done.
> Do not touch the core modules.

```
[HOST CONFIG]
> HOST_MODEL: "Claude"
  // Host is always Claude in v1.1. Do not change.

[ENVIRONMENT]
> ENV: "auto"
  // auto | code | cowork | projects | chat
  // auto = detected from runtime signals (see core.md TRI_MODE_BRIDGE_v2.0)

[PROJECT CARD]
> PROJECT_NAME: "Untitled Project"
> AUTHOR_NAME: "User"
> CLIENT_AUDIENCE: "General Public"
> PROJECT_STACK: ""
  // "React 19 + TypeScript + Tailwind" | "Python 3.12 + FastAPI" | ""
> PROJECT_CONSTRAINTS: ""
  // "no external deps" | "mobile-first" | "air-gapped" | ""
> PROJECT_GLOSSARY: ""
  // "PR=Pull Request, SLA=Service Level Agreement"

[USER PREFERENCE]
> OUTPUT_LANG: "en"
  // en | ru | uk
> DEFAULT_TIER: "auto"
  // auto | T0 | T1 | T2 | T3 | T4

[FLAGS]
> ATLAS_BETA: "false"
> CORTEX_BUILTIN: "true"
  // true = exploration_mode + session_metrics + routing_memory active as core
  // false = disabled (legacy v1.0 behavior)
> SCOPE_HELM: "auto"
  // auto = activates on long tasks | on | off
> LIVE_SPECS_OVERRIDE: "true"
  // true = vendors/_live_specs.md overrides tierN.md on LAST_VERIFIED conflict

[SESSION OVERRIDE]
> QUICK_RULE: ""
  // Quick rule for current session. Highest priority (Recency).
> TONE_OVERRIDE: ""
  // Forced tone: corporate_formal | startup_casual | academic | marketing | tech_doc
> SESSION_GOAL: ""
  // One phrase: what you want to achieve this session.
```

## How the System Reads This

`core.md` reads this file on initialization. If the file is absent — defaults apply.
This allows updating P2P (replacing `core.md`/`db.md`/etc) without losing your configuration.

## Migration Tip from v1.0

If you had a filled PRELOADER in the old `!!core_claude.md` — move those PROJECT_CARD values here once.
After that, `core.md` can be updated freely.
