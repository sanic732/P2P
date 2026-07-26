---
source_id: LIVE_CORE_V8C
version: 8.4.6-C
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-06-12
scope: P2P live session state — current session tracking, active project, ATLAS state placeholder, routing memory state.
tags: live, session-state, atlas, routing-memory, core
---

# P2P — LIVE CORE (_live/live_core.md)

> Сбрасывается при каждой новой сессии. Заполняется автоматически по мере работы.

---

## ТЕКУЩАЯ СЕССИЯ

```yaml
session_id: ""           # Заполняется при старте
started_at: ""           # ISO timestamp
environment: ""          # Code / API / Projects / Chat
project_card_loaded: false
live_specs_version: "v8C.3-20260612"

# Метрики
prompts_total: 0
corrections: 0
agent_calls: 0
quorum_runs: 0
tasks_completed: 0
quality_scores: []
session_efficiency: 0.0
```

---

## ATLAS STATE (текущий)

```
╔══════════════════════════════╗
║  ATLAS — пусто               ║
╚══════════════════════════════╝
Заполняется после первого /p2p-atlas или при создании задачи Tier ≥ 2
```

---

## ROUTING MEMORY (текущая сессия)

```yaml
# Формат: agent → bias_delta
routing_biases:
  IRIS: 0%
  TECTON: 0%
  AXIOM: 0%
  VECTOR: 0%
  DATOS: 0%
  ANON: 0%
  ARCHITECTON: 0%
  HELIOS: 0%

# История последних решений
recent_decisions: []
```

---

## CONSTRAINT STATE

```yaml
last_reinjection: 0        # Сообщение последней реинъекции
next_light_reinjection: 25
next_full_reinjection: 50
next_capsule_suggestion: 75
active_constraints: []     # Ключевые активные ограничения
```

---

## ACTIVE MODELS

```yaml
primary_model: "claude-opus-4-7"
fallback_model: "claude-sonnet-5"
current_thinking_level: null   # null / low / medium / high
temperature: null              # null при thinking=enabled
```

<!-- SOURCE_META: type=live | priority=2 | session-state=true | atlas=true | routing-memory=true -->


========================================
FILE_META
========================================
id: LIVE_CORE_V8C
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
