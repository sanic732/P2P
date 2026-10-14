---
source_id: ROUTING_MODULE_v9
version: "9.0"
module_type: on-demand
triggers: "routing|маршрутизация|выбор модели|какую модель|model selection|smart route|роутинг"
depends_on: core.md, live_specs.md
token_estimate: ~2100
scope: Smart task-based routing — optimal model selection, cost-aware routing, cascade routing. Loaded on trigger or MODULE_ROUTING=true.
tags: routing, model-selection, cost-aware, cascade, on-demand
conflict_with_v9: Translation_Layer (or mode)
---

# P2P — ROUTING MODULE (routing.md)

> Item [37] is always in the menu; this module is read when the item is chosen.
---

## ROUTING TECHNIQUES (integrated)

### Semantic Router — routing by task type
**Essence:** Classification of the incoming request by semantic features → routing to the optimal model.

**Routing matrix (June 2026):**

```
[SEMANTIC_ROUTER]

Task                      → Model               → Fallback
─────────────────────────────────────────────────────────────────
Code / debugging          → the flagship Claude model (exact id: live_specs.md)     → a balanced Claude model (exact id: live_specs.md)
Deep analysis T4          → the flagship Claude model (exact id: live_specs.md)     → a flagship GPT model (exact id: live_specs.md)
General text T2-3         → a balanced Claude model (exact id: live_specs.md)   → the flagship Claude model (exact id: live_specs.md)
Fast T0-1                 → a fast Claude model (exact id: live_specs.md)    → a balanced Claude model (exact id: live_specs.md)
Long context >200K        → a Gemini Pro model (exact id: live_specs.md) → a Grok model (exact id: live_specs.md)
Long context up to 1M, budget → a balanced Claude model (exact id: live_specs.md) (no markup) → —
Real-time X/Twitter data  → a Grok model (exact id: live_specs.md)            → —
Agentic / computer use    → an agentic GPT model (exact id: live_specs.md)       → a flagship GPT model (the flagship Claude model — via computer toolset: live_specs.md)
  (GPT variant: G22 ban is NOT transferred to it and is NOT lifted — verify by result)
Multi-agent swarm         → a Kimi model (exact id: live_specs.md)             → —
Chinese content           → a Qwen model (exact id: live_specs.md)         → —
On-premises / open-weight → a GLM model (weights on HF: live_specs.md) → a GLM model (MIT: live_specs.md)
Super-cheap               → a Gemini Flash model (exact id: live_specs.md)    → a DeepSeek Flash model (exact id: live_specs.md)

⚠ WebDev / frontend: `GPT model` (top WebDev; top Claude — flagship Claude max) — in Claude skill ONLY UPON
  EXPLICIT OPERATOR DIRECTION (operator-explicit), same as `Claude model`. Keep context below threshold (live_specs.md)
  (past the threshold: multiplier input and cache, output markup; price: live_specs.md); tools — only via
  `/v1/responses` (otherwise 400); call using explicit string, not an alias.
⚠ G22: computer use on GPT model (live_specs.md) — only with explicit allowlist and audit log
  (vendor system card: unprompted file deletion, unauthorized credentials).
⚠ minimax / manus — host-only (in live_specs TRACK-ONLY): P2P can RUN on them,
  but does NOT route TO them.
```

---

### Cascade Routing — tiered fallback routing
**Essence:** First try a cheap model; if the result falls below the quality threshold, escalate to an expensive one.

**Application in P2P:**
```
[CASCADE_ROUTING]
Cascade levels:
  L1: a fast Claude model (price: live_specs.md)    → if quality ≥ threshold → stop
  L2: a balanced Claude model (price: live_specs.md)    → if quality ≥ threshold → stop
  L3: the flagship Claude model (price: live_specs.md)    → final answer

Quality threshold:
  T0-1: L1 is sufficient
  T2:   L2 is sufficient
  T3-4: L3 is mandatory

Quality assessment (heuristic):
  - Is the task fully completed? (0/1)
  - No hallucination signals?
  - Length ≥ expected?
```

---

### Cost-Aware Routing — budget-conscious routing
**Essence:** Selecting a model based on budget constraints with minimal quality degradation.

```
[COST_ROUTER]
INPUT: task_tier, token_estimate, budget_limit

IF budget_limit is very low (tiers: live_specs.md):
    → a DeepSeek Flash model (pricing details: live_specs.md)
    → or a GLM Flash model (pricing and context: live_specs.md)

IF budget_limit is moderate (tiers: live_specs.md):
    → a balanced Claude model (exact id: live_specs.md)

IF budget_limit is high OR tier ≥ T3 (tiers: live_specs.md):
    → the flagship Claude model (best quality)

Formula:
  cost_estimate = (input_tokens/1M × price_in) + (output_tokens/1M × price_out)
```

---

### LLM-Router (Automatic Classification)
**Essence:** A lightweight model classifies the request → routes it to a specialized model.

```
[LLM_ROUTER]
Classifier: a fast Claude model (fast, cheap; exact id: live_specs.md)
Classes:
  code        → the flagship Claude model (exact id: live_specs.md)
  analysis    → the flagship Claude model / a balanced Claude model (exact ids: live_specs.md)
  creative    → a balanced Claude model (exact id: live_specs.md)
  factual     → a Gemini Pro model (web grounding if needed; exact id: live_specs.md)
  multimodal  → the flagship Claude model (exact id: live_specs.md)
  math        → the flagship Claude model + reasoning MCTS (exact id: live_specs.md)
  chinese     → a Qwen model (exact id: live_specs.md)
  rt_social   → a Grok model (exact id: live_specs.md)

Cost: classifier minimal per query (savings on expensive models; price: live_specs.md)
```

---

## CONFLICT_RESOLVER DECLARATIONS

**Conflict:** `routing.md` vs `Translation Layer` in `contract.md`

| | Translation Layer | Routing Module (this module) |
|--|------------------------|----------------------|
| Approach | Prompt adaptation for the model (G-errors) | Automatic model selection by task |
| Focus | HOW to address the model | WHICH model to select |
| Compatibility | Mutually complementary | — |

**Conclusion:** Conflict is minimal — both modules complement each other. CONFLICT_RESOLVER is needed only if the user wants to MANUALLY select a model — in that case, routing will suggest, and the translation layer will adapt.

---

## TEMPLATE: Model Selection for a Task

Command `[37] Smart Routing` → P2P asks questions:
```
1. Task type? (code/analysis/text/math/agent/...)
2. Complexity? (T0-T4)
3. Context size? (< 100K / 100K-1M / >1M)
4. Budget? (unlimited / economy / minimum)
5. Specific requirements? (Chinese/real-time/on-premises/...)

→ Recommendation: {MODEL} (${COST} est.)
→ Fallback: {MODEL}
→ Apply Translation Layer? [Y/N]
```

---

<!-- SOURCE_META: type=on-demand | module=routing | priority=P1 | menu_item=37 | token_estimate=2100 -->


========================================
FILE_META
========================================
id: ROUTING_MODULE_v9
type: on-demand
edition: CLAUDE_NATIVE
techniques: [Semantic_Router, Cascade_Routing, Cost_Aware_Routing, LLM_Router]
menu_item: 37
conflict_with_v9: Translation_Layer_minor
========================================
