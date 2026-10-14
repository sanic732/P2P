---
source_id: DEBUG_v9
version: "9.0"
module_type: on-demand
depends_on: core.md, db.md
scope: Debug Engine — structured failure analysis, G-error diagnosis, prompt autopsy, iterative fix workflow.
tags: debug, failure-analysis, g-errors, autopsy, on-demand
triggers: ["debug", "провал", "не работает", "ошибка", "почему", "исправь", "[12]", "Debug Engine"]
---

# P2P — DEBUG ENGINE (debug.md)

---

## FAILURE ANALYSIS ALGORITHM

### Step 1 — SYMPTOM CLASSIFICATION

If the input is a SCREENSHOT (frequent case: prompt was run in another LLM, result was unsatisfactory →
screenshot → return to P2P): extract the error/output text from the image, then classify below.
Vision is native to the host model (Claude / Gemini).

Determine the symptom type:

```
A. HTTP Error    → G-error immediate diagnostics
B. Wrong format  → Type C/E/H anti-pattern
C. Hallucination → No data, no DATOS verification
D. Ignored rules → Type A/B — constraint drift
E. Low quality   → Tier mismatch, incorrect agent
F. Slow/expensive → G6/G10/G11, billing trap
G. Crash/timeout  → G12/G19/G20, resource limit
```

### Step 2 — G-ERROR QUICK CHECK

```
HTTP 400 + temperature/top_p/top_k + current Claude flagship (versions: live_specs.md) → G7 (remove parameter — with thinking and without)
HTTP 400 + Grok + non-standard param → G14 (safe params only)
current Gemini models (versions: live_specs.md) + passed temperature/top_p/top_k → G1 (deprecated; remove parameter)
HTTP 429 + Gemini Pro → G12 (switch to Flash for batching)
Poor recall at large context + flagship Claude → G8 (pin to prior generation: live_specs.md)
Expensive + flagship Claude → G6 (effective max: live_specs.md)
DeepSeek multi-turn freeze → G15 (re-inject reasoning_content, never null)
```

### Step 3 — PROMPT AUTOPSY

For the failed prompt:

```
☐ ROLE defined? → If no → Type A
☐ MUST/MUST NOT pairs present? → If no → Type A
☐ Output format explicit? → If no → Type E
☐ Critical instructions at start/end? → If no → Type K (LitM risk)
☐ No conflicting rules? → If yes → Type D
☐ temperature/top_p/top_k on current Claude models (versions: live_specs.md) or when thinking=enabled? → Type L (G7)
☐ Legacy API string? → Type M
☐ Tier matches complexity? → If no → Type F
```

### Step 4 — HYPOTHESIS RANKING

```
Propose a maximum of 5 hypotheses, rank by probability:

1. [Hypothesis — 60%] Evidence: [why I think so]
2. [Hypothesis — 25%] Evidence: [why I think so]
3. [Hypothesis — 10%] Evidence: [why I think so]
...

DO NOT propose a fix until the root cause is determined.
```

### Step 5 — FIX + VERIFY

```
Root cause: [identified cause]

Minimal fix:
[Specific change — one or multiple]

Verification:
[How to verify that the fix worked]

Prevention:
[What to change in the process to prevent recurrence]
```

---

## COMMON FAILURES AND READY-MADE FIXES

### "Claude ignores my rules after 20 messages"
**Root cause:** Constraint drift (Type B)  
**Fix:** Activate CONSTRAINT_REINJECTION_PROTOCOL (every 25 messages)  
**Prevention:** Add explicit rule "Re-read <rules> before every response"

### "Claude adds long preambles and explanations"
**Root cause:** Missing MUST NOT counterpart to "Be concise"  
**Fix:**
```xml
<rules>
MUST: Be concise
MUST NOT: Add preamble ("Here is...", "Sure!", "Of course!")
MUST NOT: Add explanation after result unless asked
MUST NOT: Repeat the user's question
</rules>
```

### "JSON contains markdown fences and prose"
**Root cause:** Type H (JSON/Prose Mix)  
**Fix:**
```xml
<rules>
MUST: Output ONLY valid JSON
MUST NOT: Add markdown code fences (```)
MUST NOT: Add any text before or after JSON
MUST NOT: Add explanations inside JSON as string values
</rules>
```

### "HTTP 400 during Extended Thinking"
**Root cause:** G7 — temperature passed (current Claude models: live_specs.md — 400 always; earlier models — when thinking=enabled)  
**Fix:** Remove `"temperature"` from payload entirely  
```python
# Correct:
{"model": "balanced Claude model (exact id: live_specs.md)", "thinking": {"type": "adaptive"}, "output_config": {"effort": "medium"}}
```

### "Result is too superficial for a complex task"
**Root cause:** Tier Mismatch (Type F) or wrong agent  
**Fix:** Upgrade Tier + run QUORUM or Extended Thinking  
**Check:** LoadScore > 0.6 → T3, > 0.8 → T4 + QUORUM mandatory

### "Gemini ignores prompt structure"
**Root cause:** G2 — XML in system context  
**Fix:** Remove all XML tags, switch to plain text hierarchy  
```
## Role  (not <role>)
## Rules (not <rules>)
```

---

## ITERATIVE FIX PROTOCOL

```
Iteration 1: Apply minimal fix
Iteration 2: If it didn't help — add MUST NOT targeting the problematic behavior
Iteration 3: If it didn't help — change template (e.g., Template C for JSON)
Iteration 4: If it didn't help — switch agent or Tier
Iteration 5: If it didn't help — QUORUM for diagnostics

After 5 iterations without improvement → Rethink the task (formulation may be flawed)
```

---

## LLM ERROR TAXONOMY E-A…E-P

> Cross-model behavioral failures (separate from G1-G22 API errors and from the prompt anti-patterns Type A–P of core.md). Activate during diagnosis.

**Core metaphor:** LLM = CPU, context window = RAM. Lost-in-the-Middle: rules in middle 55% of context decay; primacy + recency survive.

> Injection scripts: db.md SECTION 7 (#DB_ERROR_INJECT_[TYPE]) — the one source.

| Type | Name | Symptom | Diagnosis | Fix |
|------|------|---------|-----------|-----|
| **E-A** | Silent timeout | Credits gone, no response | Thinking set too high for the target | One step lower in the family's own parameter (Claude `effort`, GPT `reasoning_effort`, Gemini `thinkingLevel`, Gemini Flash / Qwen `thinking_budget` — vendors/<family>.md), split the task |
| **E-B** | Mid-stop without Continue | Stops at 50-90%, no continuation | Token cap hit | Chunking, raise max_tokens |
| **E-C** | Unwarned truncation | Looks complete, ~90% cut silently | max_tokens below required | Check max_tokens, request "indicate if truncated" |
| **E-D** | Long response drift | Quality degrades mid-output | Attention decay during generation | Anchor Context, Semantic Chunking |
| **E-E** | Context Drift (gradual) | Early instructions forgotten over many turns | Window filling up | Periodic constraint re-statement, Document Map |
| **E-F** | Context Drift (Gemini long) | Gemini drifts >50 messages (~9% rate) | No persistent state file | A project state file re-read each turn (CLAUDE.md in Claude Code, GEMINI.md in Gemini CLI) |
| **E-G** | Agent self-revert (Kimi model family) | Model rolls back its own fixes | Parallel agents conflict, no checkpoint | Explicit checkpoints |
| **E-H** | Tool Call Confusion | Mixes JSON/XML in same session | Multiple format expectations | Single format per session |
| **E-I** | Overthinking (Kimi Thinking) | Elaborate reasoning for trivial T0-1 (1.2-1.6× tokens) | Thinking activated for simple task | Concise-mode instruction; disable Thinking only where the model allows it (not on current Kimi models — db.md G20) |
| **E-J** | Zero-State Hallucination | Outputs literal `[Insert text]` or fake IDs | Empty template + autoregressive instinct | ZERO-STATE IMMUNITY |
| **E-K** | Topic Drift (Grok) | Grok diverges from task >10K out tokens | Grok-specific drift | Topic anchor every 3rd turn |
| **E-L** | Silent Degradation (Claude) | Quality drops, no error signal | Context pollution from accumulated corrections | `/clear` → new session; do NOT re-correct in same session |
| **E-M1** | Correction Loop | Same correction 3+ times, oscillation | Each correction adds contradictory context | `/clear` → rewrite incorporating failure |
| **E-M2** | Kitchen Sink | Context overloaded with irrelevant files | User keeps adding without removing | Audit: "what error without this file?" no answer → remove |
| **E-M3** | Infinite Explore | Unbounded research fills context | "Figure out X" without scope limits | Scope: "Find only X. Read nothing else." or use subagent |
| **E-N** | Hallucinated Tool Call | Calls non-existent tool / invalid params | Tool definitions buried | Tool defs to primacy zone, max 7 tools |
| **E-O** | Safety Over-Refusal | Refuses legitimate request | False-positive safety trigger | EXCELLENT (excellent_techniques.md): Defensive Framing + Objective Abstraction |
| **E-P** | Format Oscillation | Switches format mid-response (>2K tokens) | Format lock only in primacy | Lock in BOTH primacy AND recency; mid-point reminder |

### E-L — Silent Degradation: 5 diagnostic indicators
- **E-L1**: Output could be from any model; no Claude-specific depth.
- **E-L2**: Hedging language increases ("perhaps", "generally").
- **E-L3**: Format becomes uniform regardless of task.
- **E-L4**: Creativity drops — no unexpected angles, no pushback.
- **E-L5**: Same correction requested twice without improvement.

**Root cause:** context pollution. **Prevention:** keep context clean; one task per prompt; don't stack corrections — restart with better prompt.

### Symptom-based quick lookup

| Symptom you see | Suspect |
|-----------------|---------|
| No response, credits gone | E-A |
| Response stopped mid-sentence | E-B |
| Looks complete but missing | E-C |
| Quality drops mid-output | E-D |
| Forgot earlier instructions | E-E |
| Gemini drifting >50 msgs | E-F |
| Agent undid its own changes | E-G |
| Wrong format in tool calls | E-H |
| Overlong reasoning for simple | E-I |
| `[Insert text]` in output | E-J |
| Grok answering wrong question | E-K |
| Claude generic/safe/bland | E-L |
| Worse the more I correct | E-M1 |
| Can't handle all my files | E-M2 |
| Research ate all the context | E-M3 |
| Calls non-existent tool | E-N |
| Refuses legitimate request | E-O |
| Format switches mid-response | E-P |

### Context Integrity Diagnostics
1. COUNT files in context; turns in conversation. >15 files or >30 turns → suspect E-M2 or E-E.
2. MEASURE system vs user content. >60% system → P2P files crowding user content.
3. TEST: ask model to repeat a specific rule from early in session. Fails → confirm E-E.
4. COMPARE: same question in fresh clean session. Dramatically better → confirm E-L or E-M1…E-M3.
5. NEEDLE TEST: plant a unique phrase, ask model to find it. Fails → Lost-in-the-Middle confirmed.

---

<!-- SOURCE_META: type=on-demand | priority=3 | debug=true | failure-analysis=true | g-errors=true | error-taxonomy=E-A..E-P -->


========================================
FILE_META
========================================
id: DEBUG_v9
type: on-demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
