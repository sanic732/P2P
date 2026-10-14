---
source_id: REASONING_MODULE_v9
version: "9.0"
module_type: on-demand
triggers: "reasoning|цепочка рассуждений|chain of thought|cot|self-consistency|mcts|tts|test-time|scaling|подумай|think step"
depends_on: core.md
token_estimate: ~3200
scope: Extended reasoning techniques for P2P — TTS, Self-Consistency, MCTS, rStar-Math, critical chains, Context-Grounding CoT. Loaded on trigger or MODULE_REASONING=true.
tags: reasoning, cot, tts, self-consistency, mcts, on-demand
conflict_with_v9: DEEP_THINK_VALUE_GATE (or mode)
---

# P2P — REASONING MODULE (reasoning.md)

> Item [36] is always in the menu; this module is read when the item is chosen.
> ⚠ Conflict with core DEEP_THINK_VALUE_GATE possible — see CONFLICT_RESOLVER.

---

## REASONING TECHNIQUES (integrated)

### s1: Simple Test-Time Scaling (Budget Forcing)
**Source:** s1 (Stanford 2025) — already partially in core as Budget Forcing  
**NOTE:** The technique is present in both catalogs (STOP-4). Integrated in core via DEEP_THINK_VALUE_GATE. This module extends it — adds explicit thinking budget control and multi-step forcing.

**Extension (NOT replacement):**
```
[BUDGET_FORCING_EXTENDED]
# core: DEEP_THINK_VALUE_GATE — effort; adaptive thinking (no thinking=enabled on current Claude models, G7)
# module adds:
effort_levels:
  auto:   flagship Claude model — no thinking block, effort only; other Claude models — thinking {type: "adaptive"}
  medium: effort: "medium"   # flagship Claude model: omit thinking; other Claude models: thinking {type: "adaptive"}
  high:   effort: "high"     # never {type: "enabled"} on the flagship Claude model (HTTP 400, G7); never budget_tokens — removed (G7)
  forced: append "Wait, let me reconsider" → forced thinking step
```
**G7 WARNING:** NEVER non-default temperature/top_p/top_k on current Claude models (versions: live_specs.md) (with or without thinking); on older models — not with thinking=enabled.

---

### Self-Consistency (SC) — Multi-generation + voting
**Source:** Wang et al. 2023 (classic CoT)  
**Essence:** Generate N independent solutions → take majority vote as final answer.

**Application in P2P:**
```
[SELF_CONSISTENCY]
N: 3-5 (for T2-3) / 7-9 (for T4 critical)
Voting: majority vote (for closed-ended)
        or best reasoning chain (for open-ended)

Example for QUORUM:
  IRIS   → solution A
  TECTON → solution B  
  AXIOM  → solution C
  Final: majority_vote([A, B, C]) or synthesis
```

---

### MCTS for Reasoning (rStar-Math pattern)
**Source:** arXiv 2501.04519 (rStar-Math, Microsoft 2025)  
**Essence:** Monte Carlo Tree Search for exploring the reasoning space. Intermediate step evaluation (Process Reward Model).

**When to use:** T4 tasks, mathematics, logic, multi-step planning.

**Application in P2P:**
```
[MCTS_REASONING]
Step 1: Decompose task into state-steps
Step 2: For each step — generate 3-5 continuation variants
Step 3: Score each variant (0-1) — how well it leads to the solution
Step 4: Select best branch, continue
Step 5: Backpropagation — if branch failed, backtrack and try another
Step 6: Final answer = best full path

Adaptation for P2P (without real MCTS):
  IRIS  → draft 3 approaches to the step
  AXIOM → score each (score 0-1)
  TECTON → select best, continue
```

---

### Critical Chain Prompting (CCP)
**Essence:** Explicit identification of the critical path in reasoning before starting generation.

**Application in P2P:**
```
[CCP]
Before answering:
1. CRITICAL_PATH: [list of key steps]
2. DEPENDENCIES: [what depends on what]
3. RISKS: [where it could go wrong]
Then — execution along the critical path.
```

---

### Context-Grounding CoT (rule extraction before answering)
**Source/Metrics:** arXiv 2605.25354 (May 2026, in-window). +3.79pp on CL-Bench.
**Difference from CCP:** CCP is about the critical path of the solution; Context-Grounding is about extracting rules/definitions from data BEFORE generation. Complements rag-grounding (rag.md).
```
[CONTEXT_GROUNDING]
1. EXTRACTED_RULES: [rules/definitions/constraints from context relevant to the task]
2. Answer is built ONLY on EXTRACTED_RULES, with explicit citations.
Application: long-context, RAG, documents/specifications. Complements rag-grounding.
```

---

## REASONING ROUTER

```
Task type → reasoning strategy:

Math/Logic T4    → MCTS_REASONING (QUORUM: IRIS+AXIOM+TECTON, as above)
Ambiguous T3-4   → Self-Consistency (N=5, majority vote)
Creative T2-3    → Budget Forcing EXTENDED (effort=high)
Structured T2    → CCP → CoT
Simple T0-1      → Direct (no overhead)
```

---

## CONFLICT_RESOLVER DECLARATIONS

**Conflict 1:** `MODULE_REASONING` + `DEEP_THINK_VALUE_GATE`

| | core | module |
|--|-------|-------|
| Approach | DEEP_THINK gate (ValueScore threshold) | MCTS / SC / Budget Forcing Extended |
| When | T3-4 per SIR Scanner | By task type (math→MCTS, ambiguous→SC) |
| Outcome | Reliable, proven | Potentially more accurate for specific tasks |

On such a conflict CONFLICT_RESOLVER asks for the strategy choice for this request.

**Conflict 2:** `Budget Forcing Extended` vs `budget_tokens` (G7)

The module NEVER uses `budget_tokens` (removed from API). `thinking: {type: "adaptive"}` with effort is used (flagship Claude model: effort only, no thinking block).

---

<!-- SOURCE_META: type=on-demand | module=reasoning | priority=P1 | menu_item=36 | token_estimate=3200 -->


========================================
FILE_META
========================================
id: REASONING_MODULE_v9
type: on-demand
edition: CLAUDE_NATIVE
techniques: [s1_extended, Self_Consistency, MCTS_reasoning, rStar_Math, CCP, Context_Grounding_CoT]
menu_item: 36
conflict_with_v9: DEEP_THINK_VALUE_GATE
========================================
