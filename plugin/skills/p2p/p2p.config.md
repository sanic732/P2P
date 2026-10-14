---
source_id: CONFIG_v9
version: "9.0"
module_type: config
scope: User configuration file for P2P 9.0. Copy to project root and fill in.
tags: config, user-settings, project-card, flags, personalization
---

# P2P — USER CONFIGURATION

> Copy this file to the project root and fill it out for your needs.
> P2P automatically loads p2p.config.md if it exists.

## PROJECT_CARD

```yaml
PROJECT_CARD:
  name: ""
  type: ""              # web-app / script / research / content / api / other
  stack: ""             # Python 3.12 + FastAPI / React 18 / etc.
  target_model: "the flagship Claude model (exact id: live_specs.md)"
  context: ""           # 1-3 sentences (the key of _preloader.md PROJECT_CARD)
  constraints: []
  team_size: ""         # optional, not read by P2P
  deadline: ""          # optional, not read by P2P
  phase: ""             # optional, not read by P2P
  flags:
    CORTEX_BUILTIN: true
    SCOPE_HELM: true
    LIVE_SPECS_OVERRIDE: false
    DEEP_THINK: "auto"
    SHOW_CHART: true           # optional, not read by P2P
    METRICS_TRACKING: true     # optional, not read by P2P
```

## ASSISTANCE

```yaml
PILOT_MODE: co-pilot   # co-pilot | auto-pilot | manual (core.md pilot_mode; default of _preloader.md)
SHERPA: auto           # auto | on | off (core.md sherpa_mode)
GUARDIAN: auto         # auto = by the environment (_preloader.md STEP 1) / on / off
VERBOSE_MODE: false    # _preloader.md STEP 2 profile
```

## USER PROFILE

```yaml
USER_PROFILE:
  role: "developer"     # developer / designer / pm / researcher / other
  expertise:
    programming: 2      # 0=none, 1=beginner, 2=intermediate, 3=expert
    system_design: 2
    domain: ""
  communication:
    language: "auto"    # auto or any language by name or code
    verbosity: "balanced"
    show_reasoning: true
    prefer_examples: true
```

## SESSION_OVERRIDE

```yaml
SESSION_OVERRIDE:
  tier_override: null        # not read by P2P (reserved)
  agent_override: null       # not read by P2P (reserved)
  thinking_level: null       # not read by P2P (reserved)
  output_format: null        # not read by P2P (reserved)
  quorum_threshold: "T2"
```

> ⚠ This file is for the user only. P2P reads it but MUST NOT modify it.
