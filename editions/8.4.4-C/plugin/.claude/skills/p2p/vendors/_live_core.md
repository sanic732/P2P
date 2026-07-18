---
source_id: LIVE_CORE_V8C
version: v8C.3
module_type: live
depends_on: _live/MANIFEST.md
last_updated: 2026-06-12
scope: P2P v8C.3 live session state — current session tracking, active project, ATLAS state placeholder, routing memory state.
tags: live, session-state, atlas, routing-memory, core
---

# P2P v8C.3 — LIVE CORE (_live/live_core.md)

> Сбрасывается при каждой новой сессии. Заполняется автоматически по мере работы.

---

## ТЕКУЩАЯ СЕССИЯ

```yaml
session_id: ""           # Заполняется при старте
started_at: ""           # ISO timestamp
environment: ""          # Code / API / Projects / Chat
project_card_loaded: false
live_specs_version: "v8C.3-20260502"

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
fallback_model: "claude-sonnet-4-6"
current_thinking_level: null   # null / low / medium / high
temperature: null              # null при thinking=enabled
```

<!-- SOURCE_META: type=live | priority=2 | session-state=true | atlas=true | routing-memory=true -->


========================================
VERSION_METADATA
========================================
id: LIVE_CORE_V8C
version: v8C.3
type: live
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
// ═══════════════════════════════════════════════════════
// [V8.5 OVERRIDE — 2026-06-27] источник истины: vendors/live_specs.md (перебивает при конфликте)
// ═══════════════════════════════════════════════════════
V85_OVERRIDE:
  Claude: PRIMARY=opus-4-8 ($5/$25, 1M ctx, out 128K/300K batch, effort high default low|med|high|xhigh|max).
  Fable5: $10/$50 1M, Arena #1 Agent/Text/WebDev — SUSPENDED globally 12.06 (export controls) → fallback opus-4-8.
  opus-4-6: пин >500K recall (MRCR 78.3%); токенизатор эффективнее 4.7/4.8.
  legacy_retire: COMPLETED — claude-*-4-20250514 → HTTP 404.
  G6 tokenizer inflation: UNRESOLVED (+10-35%) → pin 4.6 cost-sensitive.
  thinking: ТОЛЬКО {"type":"adaptive"}; budget_tokens removed; G7 нет temperature/top_p/top_k.
  cache_ttl: Claude Code 1h→5min → ephemeral на префикс.
  deadlines: 2026-06-25 Gemini Nano Banana preview shutdown; 2026-07-24 deepseek-chat/reasoner → 404.
