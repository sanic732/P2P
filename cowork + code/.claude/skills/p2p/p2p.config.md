---
source_id: CONFIG_V8C
version: v8C.1
module_type: config
last_updated: 2026-05-02
scope: User configuration file for P2P v8C.1. Copy to project root and fill in.
tags: config, user-settings, project-card, flags, personalization
---

# P2P v8C.1 — КОНФИГУРАЦИЯ ПОЛЬЗОВАТЕЛЯ

> Скопируй этот файл в корень проекта и заполни под себя.
> P2P автоматически загружает p2p.config.md если он существует.

## PROJECT_CARD

```yaml
PROJECT_CARD:
  name: ""
  type: ""              # web-app / script / research / content / api / other
  stack: ""             # Python 3.12 + FastAPI / React 18 / etc.
  target_model: "claude-opus-4-7"
  description: ""       # 1-3 предложения
  constraints: []
  team_size: ""         # solo / small / medium / large
  deadline: ""
  phase: ""             # planning / development / testing / production
```

## USER PROFILE

```yaml
USER_PROFILE:
  role: "developer"     # developer / designer / pm / researcher / other
  expertise:
    programming: 2      # 0=нет, 1=beginner, 2=intermediate, 3=expert
    system_design: 2
    domain: ""
  communication:
    language: "ru"      # ru / en / auto
    verbosity: "balanced"
    show_reasoning: true
    prefer_examples: true
```

## FLAGS

```yaml
flags:
  CORTEX_BUILTIN: true
  SCOPE_HELM: true
  LIVE_SPECS_OVERRIDE: false
  DEEP_THINK: "auto"
  GUARDIAN: "auto"
  VERBOSE_MODE: false
  SHOW_ATLAS: true
  METRICS_TRACKING: true
```

## SESSION_OVERRIDE

```yaml
SESSION_OVERRIDE:
  tier_override: null
  agent_override: null
  thinking_level: null
  output_format: null
  quorum_threshold: "T3"
```

## ROUTING MEMORY SEED

```yaml
routing_memory_seed:
  TECTON: 0
  IRIS: 0
  AXIOM: 0
  VECTOR: 0
  DATOS: 0
  ANON: 0
  ARCHITECTON: 0
  HELIOS: 0
```

> ⚠ Этот файл только для пользователя. P2P читает но не изменяет.
