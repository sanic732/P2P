---
id: tool_budget_v8H
version: v8H.3
type: HOST_ENGINE
priority: MEDIUM
triggers: "tool budget|лимит вызовов|Type B|re-inject|бюджет инструментов"
depends_on: "!agents.md, !!core_v8H.md, !metrics.md"
last_verified: 2026-06-27
compatible_with: "all v8H files"
tags: tool-budget, type-b, grok, host-gated, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — TOOL BUDGET (порт 8G.1; grok-gated, прочие хосты — мягкий лимит)
// Профилактика Type B (tool forgetting). Активен жёстко при HOST_MODEL=grok.
// ═══════════════════════════════════════════════════════

TOOL_BUDGET:
  GLOBAL: 20-25 calls/session (hard max 30 — выше Type B риск)
  ANON_CAP: 18 calls (hard)
  RE_INJECT: каждые 8 calls → впрыснуть 5 критичных правил (primacy defense)
  ALERTS:
    @12  → warn + re-inject
    @16  → warn + сократить бюджет на 30%
    @18  → стоп ANON
    @20  → форсировать summary
  INTEGRATION: !debug логирует Type B инциденты; !metrics трекает budget-exhaustion; !memory хранит success-паттерны.

HOST_GATING:
  grok      → жёсткие лимиты выше (реальные параллельные tool calls).
  claude    → применять к sub-agents/Computer Use (мягко).
  иначе     → симуляция: «логический» бюджет шагов, re-inject правил каждые ~8 ходов.

RE_INJECT_TEMPLATE:
  "[CONSTRAINT REFRESH — call N] Активные правила: 1.{} 2.{} 3.{} 4.{} 5.{}. Держись их."

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 Hybrid · Tool Budget
  SOURCE:      donor 8G.1 !tool_budget.md (Type B prevention)
  COMPATIBLE:  !agents.md | !x_realtime.md | !metrics.md | !debug→!toolkit
