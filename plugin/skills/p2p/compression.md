---
source_id: COMPRESSION_MODULE_v9
version: "9.0"
module_type: on-demand
triggers: "compress|сжат|llmlingua|gist token|токен бюджет|context window full|контекст переполнен|длинный контекст|KV-cache"
depends_on: core.md
token_estimate: ~2400
scope: Context compression for P2P — LLMLingua, Gist Tokens, Verbatim Deletion, Selective Summarization, Context Engineering. Loaded via trigger or MODULE_COMPRESSION=true.
tags: compression, llmlingua, gist-tokens, context, kv-cache, on-demand
conflict_with_v9: CAPSULE (or mode, minor)
---

# P2P — COMPRESSION MODULE (compression.md)

> Item [38] is always in the menu; this module is read when the item is chosen.
---

## COMPRESSION TECHNIQUES (integrated)

### LLMLingua — Prompt Compression via Perplexity
**Source:** Microsoft Research 2023/2024  
**Essence:** Removing high-perplexity (redundant) tokens while preserving meaning. Compression ratio up to 5-20x with <5% quality loss.

**Application in P2P:**
```
[LLMLINGUA]
target_ratio: 0.5    # keep 50% of tokens
method: perplexity   # remove high-perplexity tokens

Algorithm (in-prompt emulation):
1. Identify "anchor" sentences (key facts, numbers, names)
2. Remove redundant conjunctions, introductory phrases, repetitions
3. Replace examples → references ("for example, as above")
4. Compress boilerplate phrases ("please make sure that" → "mandatory")

Apply when: context > 80% of model limit
```

---

### Gist Tokens — Semantic Compression
**Source:** arXiv 2304.08467 (Mu et al., Stanford NLP 2024)  
**Essence:** Train a model to represent long instructions using a single "gist token" — a special marker. Adaptation for P2P (without fine-tuning): use CAPSULE as a gist-analog.

**Application in P2P (without fine-tuning):**
```
[GIST_COMPRESSION]
Principle: replace repeating instruction block → reference to CAPSULE
Format: [REF:CAPSULE_ID] instead of full block (100+ tokens → 5 tokens)

When to use: identical instruction blocks repeat across multiple requests
```

---

### Context Compaction — Verbatim Deletion
**Source:** Anthropic best practices + arXiv (Context Compaction)  
**Essence:** Remove verbatim repetitions → replace with summarization or reference.

**Application in P2P:**
```
[CONTEXT_COMPACT]
What to delete:
  - Full repetitions of previous responses
  - Service messages ("Understood, proceeding...")
  - Examples that have already been processed
  - Intermediate drafts (keep only the final version)

What to preserve:
  - PROJECT_CARD
  - CHART (current task state)
  - Last exchange (user + assistant)
  - Critical constraints

triggers: context > 70% of limit → suggest compaction
```

---

### Selective Summarization (hierarchical)
```
[SELECTIVE_SUMMARY]
Preservation levels:
  L1 (verbatim):  last 2 exchanges + PROJECT_CARD + CHART
  L2 (condensed): decisions from session (1-2 sentences each)
  L3 (reference): "earlier we defined X, Y, Z"
  L4 (deleted):   all intermediate steps and drafts

When context is low: L4 → L3 → L2 (in this order)
```

---

## COMPRESSION ROUTER

```
IF ctx_usage < 60%:   → no action
IF ctx_usage 60-80%:  → suggest Selective Summary (L4)
IF ctx_usage 80-90%:  → Verbatim Deletion + LLMLingua on older exchanges
IF ctx_usage > 90%:   → save CAPSULE + new session (CAPSULE_TARGET)
```

---

## CONFLICT_RESOLVER DECLARATIONS

**Conflict:** `COMPRESSION` + `CAPSULE` (memory.md)

| | CAPSULE (memory.md) | Compression (this module) |
|--|---------------|-------------------|
| Approach | Save everything to CAPSULE → load later | Compress context right now |
| When | Context is full, pause needed | Context is full, continuing work |
| Result | Full history recoverable | Continuation without interruption |

On such a conflict P2P asks — compress context or save CAPSULE?

**Disambiguation (DO NOT mix — two different compression axes):**

| Technique | Axis | Reversibility | When |
|---------|-----|-------------|-------|
| LLMLingua | token-space (removes tokens) | lossy, irreversible | text remains text |
| Gist | learned marker → reference | referential | repetition of identical blocks |

See `db.md` #DB_TECHNIQUE_COMBINATOR.

---

## CONTEXT ENGINEERING (Anthropic framing)
Shift: not "prompt formulation", but "curating the token set" (system prompt, tools, examples, history, memory).
Techniques (interlocking with P2P modules):
  • compaction   → LLMLingua / selective summarization
  • note-taking  → memory_bridge / CAPSULE
  • JIT retrieval→ rag.md adaptive retrieval
  • labeled sections <background>/<instructions>/## Tool guidance → CONTEXT_CACHE_ANCHOR
Economics: prompt caching — up to 90% cost / 85% latency (Anthropic); OpenAI 50% on cached input.
Caveat: aggressive compaction discards critical nuance — maintain an anchor of key facts.

---

<!-- SOURCE_META: type=on-demand | module=compression | priority=P2 | menu_item=38 | token_estimate=2400 -->


========================================
FILE_META
========================================
id: COMPRESSION_MODULE_v9
type: on-demand
edition: CLAUDE_NATIVE
techniques: [LLMLingua, Gist_Tokens, Verbatim_Deletion, Selective_Summarization]
menu_item: 38
conflict_with_v9: CAPSULE_minor
========================================
