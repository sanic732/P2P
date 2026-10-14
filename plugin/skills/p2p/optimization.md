---
source_id: OPTIMIZATION_MODULE_v9
version: "9.0"
module_type: on-demand
triggers: "optim|оптимиз|APO|OPRO|автоматическ|улучши промпт|improve prompt|auto-tune|prompt evolution"
depends_on: core.md
token_estimate: ~3000
scope: Automatic prompt optimization for P2P — APO, OPRO, EvoPrompt, GEPA, MASPO, iterative improvement. Loaded via trigger or MODULE_OPTIMIZATION=true.
tags: optimization, apo, opro, evoprompt, auto-tune, on-demand
conflict_with_v9: Contract_Builder (or mode, minor)
---

# P2P — OPTIMIZATION MODULE (optimization.md)

> Item [40] is always in the menu; this module is read when the item is chosen.
---

## OPTIMIZATION TECHNIQUES (integrated)

### APO — Automatic Prompt Optimizer
**Core concept:** Iterative prompt optimization via gradient-free meta-learning. The LLM analyzes errors → generates an improved version.

**Application in P2P:**
```
[APO_CYCLE]
Step 1: Run prompt v0 → get output_0
Step 2: Evaluate output_0 (quality 0-1, what went wrong)
Step 3: Query the LLM: "What needs to be changed in the prompt so that the output is better?"
        → get delta (list of changes)
Step 4: Apply delta → prompt v1
Step 5: Repeat 3-5 cycles
Step 6: Final prompt = the best one by metric

Evaluation metrics:
  □ Task alignment (0-1)
  □ Length and completeness
  □ Constraint following (MUST/MUST NOT)
  □ Absence of anti-patterns (Type A-P)
```

---

### OPRO — Optimization by PROmpting
**Source:** Google DeepMind 2023  
**Core concept:** Meta-prompt with a history of previous attempts and their scores → LLM generates an improved prompt.

**Application in P2P:**
```
[OPRO]
META_PROMPT:
"You are a prompt engineering expert.
Optimization history:
  v0: [prompt] → score: 0.6
  v1: [prompt] → score: 0.73
  v2: [prompt] → score: 0.81
Task: {task description}
Success criterion: {metric}

Propose v3 that will improve the score > 0.85.
MUST: Explain what was changed and why."

P2P constraints:
  max_iterations: 5
  stop_if: score ≥ 0.9 or no improvement for 2 consecutive iterations
```

---

### EvoPrompt — Evolutionary Optimization
**Core concept:** Population-based approach: multiple prompt variants → selection of the best → crossover → mutation.

**Application in P2P (simplified):**
```
[EVOPROMPT]
Generation 0:
  A: original prompt
  B: rephrased version
  C: contractual version (MUST/MUST NOT)

Fitness evaluation of each: run on 2-3 test inputs

Selection: 2 best → "offspring" (take the best from each)

Apply when: radical prompt overhaul is needed
Cost: high (many requests) → T3-4 tasks only
```

---

### GEPA — Reflective Evolution (EvoPrompt upgrade)
**Source/Metrics:** arXiv 2507.19457 (July 2025, ICLR'26 Oral — "surging", not new-in-window). +6..19pp over GRPO with 35× fewer rollouts; +12pp AIME-2025 vs MIPROv2.
**Difference from EvoPrompt:** NL-reflection (LLM diagnoses WHY failure occurred, accumulates lessons) + Pareto-selection across {accuracy, tokens, cost}, rather than a single fitness function.
```
[GEPA_CYCLE]  (framework, T3-4, requires eval-harness)
  1. Run prompt → 2-5 traces (success/failure)
  2. REFLECTION: "Why the failure? Formulate 1-3 lessons."
  3. Mutation ACCOUNTING FOR lessons (not random)
  4. Pareto front: non-dominated across {accuracy, tokens, cost}
  5. stop: no front improvement for 2 iterations / budget exhausted
```

---

### Iterative Refinement via QUORUM
**Core concept:** Using QUORUM to evaluate and improve a prompt across multiple agents.

```
[QUORUM_OPTIMIZATION]
Round 1 — IRIS: Analyze weak points in the current prompt
Round 2 — TECTON: Propose structural improvements
Round 3 — AXIOM: Check for anti-patterns (Type A-P)
Round 4 — VECTOR: Adversarial test — attempt to break the prompt
Round 5 — HELIOS: Synthesize the best suggestions → final version

Output: prompt v_final + changelog of improvements
```

---

### MASPO — Joint QUORUM Optimization (meta-tuning mode)
**Source/Metrics:** arXiv 2605.06623 (May 2026, ICML'26 — genuinely in-window). +2.9pp over SOTA; without ground-truth for intermediate agents.
**⚠ Invariant interaction:** MASPO optimizes WEIGHT DISTRIBUTION and prompts of the 8 agents (agents.md). DOES NOT violate `I7_agents_8` — the number of agents = 8 remains unchanged, only their weights/prompts change. Recorded in changelog.
```
[MASPO_QUORUM]  (QUORUM meta-tuning mode, T4)
  Evaluation of candidate prompt for agent X across 3 axes:
    • local validity  — quality of its own output
    • lookahead        — assistance to subsequent agents
    • global alignment — contribution to HELIOS result
  Joint reward = f(local, lookahead, global); hard-negative mining on disagreements;
  trace-guided beam search over prompt configurations of ALL agents.
```

---

## OPTIMIZATION PIPELINE [40]

When selecting [40] Optimization:
```
P2P requests:
  1. Prompt to optimize
  2. Task / expected output
  3. Quality criterion (what defines "good"?)
  4. Method: [A] APO / [B] OPRO / [C] EvoPrompt / [D] QUORUM

Executes:
  □ Baseline evaluation of current prompt
  □ N optimization iterations (per method)
  □ Anti-pattern scan of each version (Type A-P)
  □ Comparative table of versions

Outputs:
  OPTIMIZATION_REPORT:
    Initial score: X
    Final score: Y
    Iterations: N
    Key changes: [list]
    Final prompt: [text]
```

---

## SePO — BACKLOG (not included in delivery)
**Source/Metrics:** arXiv 2606.04465 (June 2026). +4.49pp vs Manual-CoT.
**Status:** requires training budget → cannot be activated in an inference-only environment. Formatted as a direction in backlog (self-tuning core roadmap), NOT an implementation item for the current release.

---

## CONFLICT_RESOLVER DECLARATIONS

**Conflict:** `optimization.md` vs `Contract Builder [2]`

| | Contract Builder | Optimization (this module) |
|--|------------------------|-------------------|
| Approach | 9-step construction algorithm | Iterative improvement of existing |
| When | Create a prompt from scratch | Improve an existing prompt |
| Compatibility | Complementary: CB creates → Opt improves | — |

Recommendation in case of or: use Contract Builder for creation → Optimization for tuning.

---

<!-- SOURCE_META: type=on-demand | module=optimization | priority=P3 | menu_item=40 | token_estimate=3000 -->


========================================
FILE_META
========================================
id: OPTIMIZATION_MODULE_v9
type: on-demand
edition: CLAUDE_NATIVE
techniques: [APO, OPRO, EvoPrompt, GEPA, QUORUM_Optimization, MASPO, SePO_backlog]
menu_item: 40
conflict_with_v9: Contract_Builder_complementary
========================================
