---
source_id: RAG_MODULE_v9
version: "9.0"
module_type: on-demand
triggers: "rag|raptor|retrieval|вектор|поиск по базе|document search|ретривал|векторная"
depends_on: core.md, db.md
token_estimate: ~2800
scope: RAG techniques for P2P — RAPTOR, vector search, adaptive retrieval. Loaded via trigger or MODULE_RAG=true.
tags: rag, raptor, retrieval, vectors, on-demand
conflict_with_v9: none
---

# P2P — RAG MODULE (rag.md)

> Item [35] is always in the menu; this module is read when the item is chosen.
---

## RAG TECHNIQUES (integrated)

### RAPTOR — Recursive Abstractive Processing for Tree-Organized Retrieval
**Source:** arXiv 2401.18059 (Sarthi et al., Stanford NLP 2024)  
**Essence:** Hierarchical document tree — recursive clustering and summarization of chunks across multiple levels. The tree allows retrieving information at any level of abstraction.

**When to use:** Large corpora (>50 documents), answers needed for both detailed and general questions.

**Application in P2P:**
```
[RAPTOR-RAG]
Step 1: Split documents into chunks (512-1024 tokens)
Step 2: Cluster similar chunks (UMAP + GMM)
Step 3: Summarize each cluster → tree node L1
Step 4: Repeat for L1 → L2, L2 → L3
Step 5: On query — retrieve from the required level (collapsed tree or tree traversal)
Step 6: Feed into context with level metadata
```

---

### LongRAG — Long-Context RAG
**Source:** arXiv 2410.18050  
**Essence:** Instead of small chunks — large retrieval units (entire document or major section). Reduces noise, increases recall for long queries.

**When to use:** Models with >200K context, documents with high interconnectedness.

**Application in P2P:**
```
[LONGRAG]
target_model: the flagship Claude model / Gemini Pro model (context windows: live_specs.md)
retrieval_unit: "full document" or "major section" (not chunks)
top_k: 3-5 (fewer units, but larger each)
```

---

### adRAP / Dynamic RAPTOR
**Source:** arXiv 2410.01736  
**Essence:** RAPTOR with adaptive level selection depending on query type. Fact-based queries → lower levels. Summary queries → upper levels.

**Application in P2P:**
```
[DYNAMIC-RAPTOR]
Query Classification:
  factual/specific → level 0 (raw chunks)
  thematic/summary → level 1-2
  abstract/overview → level 2-3
```

> For context-dependent answers — Context-Grounding CoT (reasoning.md): extract rules from chunks BEFORE generation.

---

## RAG ROUTING (Integration with routing.md)

```
RAG task → strategy selection:

IF corpus < 20 docs AND docs < 50K tokens:
    → Naive RAG (direct load into context)
    → Model: the flagship Claude model (context window: live_specs.md)

IF corpus = 20-500 docs:
    → RAPTOR (hierarchical tree)
    → Model: the flagship Claude model / Gemini Pro model (exact ids: live_specs.md)

IF corpus > 500 docs OR needs semantic:
    → Full Vector DB + RAPTOR
    → Model: based on task

IF docs high interconnectedness:
    → LongRAG (large retrieval units)
```

---

## CONFLICT_RESOLVER DECLARATIONS

This module DOES NOT conflict with base logic — additive.

When working with [15] Knowledge base search:
- base logic: keyword/semantic search in db.md
- this module: RAPTOR tree with hierarchical retrieval
- **Mode or:** P2P will prompt for strategy selection

---

## RAG PROMPT TEMPLATES

### Prompt for RAPTOR cluster summarization:
```
You are a RAPTOR node summarizer. A document cluster has been provided.
MUST: Create a coherent summary preserving key facts and terms.
MUST: Summary length — 1/5 of the total chunk length.
MUST NOT: Add conclusions not present in the documents.
MUST NOT: Use bullet points — prose only.
```

### Prompt for final RAG answer:
```
Context (RAPTOR retrieval, level {LEVEL}):
{RETRIEVED_CONTEXT}

Query: {QUERY}
MUST: Use only information from the context.
MUST: State the abstraction level of the source (detail/summary/overview).
MUST NOT: Hallucinate facts outside the context.
```

---

<!-- SOURCE_META: type=on-demand | module=rag | priority=P1 | menu_item=35 | token_estimate=2800 -->


========================================
FILE_META
========================================
id: RAG_MODULE_v9
type: on-demand
edition: CLAUDE_NATIVE
techniques: [RAPTOR, LongRAG, adRAP, Dynamic_RAPTOR]
menu_item: 35
conflict_with_v9: none
========================================
