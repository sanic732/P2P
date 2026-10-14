---
file_id: RAG_METAPROMPT_STANDARD
version: 2.0
updated: 2026-06-21
role: universal_instruction
scope: rag_optimized_metaprompt_architecture
rag_priority: maximum
description: >
  Universal standard for constructing large metaprompts
  adapted for RAG backends (NotebookLM, Gemini Notebooks,
  Claude Projects/Cowork, any long-context LLM with retrieval).
  Apply when creating any multi-file prompt system
  (10+ files, 50K+ characters).
key_concepts:
  - YAML_frontmatter
  - rag_zone_tags
  - master_index
  - semantic_isolation
  - dependency_graph
  - symptom_indexed_tables
  - deduplication
  - query_anchors
applies_to: [NotebookLM, Gemini_Notebooks, Claude_Projects, Claude_Cowork, any_RAG_LLM]
---

# 📐 RAG METAPROMPT STANDARD v2.0
# Universal Instruction for Building Large Metaprompts for RAG

> Updated 2026-06-21. The principles of version 1.0 are retained completely — they
> are architecture-independent. Added to §0 is an up-to-date model of how
> modern RAG backends actually work (this is essential for understanding
> WHY the techniques below work).

═══════════════════════════════════════════════════════════════════
FOUNDATIONAL PRINCIPLE
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: core_principle -->

A RAG engine splits documents into chunks and returns the most
relevant ones. LLM response quality = the quality of the chunks
retrieved into context. The metaprompt author’s task: make each chunk
self-contained, accurately named, and free from semantic
noise from adjacent concepts.

ANALOGY: one chunk = one paragraph in a textbook. If three topics
are mixed on a single page, a student will understand none of them. If each topic
is on a separate page with a heading, retrieval is accurate.

KEY RULE: one file — one semantic zone.
One paragraph — one concept. One tag — one signal.

═══════════════════════════════════════════════════════════════════
§0. HOW RAG BACKENDS ACTUALLY WORK (current as of 2026)
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: how_rag_backends_work -->

<rag_backend_model>

// This section explains WHY all the techniques below work.
// It is important not to confuse two distinct mechanisms.

─── TWO DISTINCT MECHANISMS ───

  1. CLASSICAL CHUNK RAG (vector retrieval)
     Documents are split into chunks → embedded → stored in a vector DB.
     Upon query, the semantically closest chunks are retrieved → inserted into the prompt.
     This is how enterprise RAG, custom pipelines, and NotebookLM operate on
     a large corpus.

  2. LONG-CONTEXT INGESTION (everything into the window)
     Sources are fed in their entirety into the model’s large context window
     (currently 1M tokens in frontier models). Retrieval is not needed
     as long as the corpus fits within the window.

─── IMPORTANT CLARIFICATION (dispelling a common myth) ───

  Myth: "NotebookLM simply loads the entire notebook into a 1M window wholesale."
  Fact: even with models having a 1M window, the backend conducts SAMPLING from sources
  for a specific query, rather than feeding the entire corpus into every generation.
  The 1M context applies to a SINGLE chat session (dialogue history + selected
  fragments), not to "the entire notebook simultaneously."

  Practical takeaway: even with a gigantic window, retrieval quality and
  window size are DIFFERENT things. A large window DOES NOT guarantee that the model
  will find the required fact in the middle of the corpus (see §0.1 "Lost in the Middle").
  Therefore, structuring sources for retrieval remains critical
  on ANY backend.

─── §0.1 THE "LOST IN THE MIDDLE" EFFECT ───

<!-- rag_anchor: lost_in_the_middle -->

  Established fact (Liu et al., TACL 2024): models use information better
  at the BEGINNING and at the END of the context, and noticeably worse in the MIDDLE.
  Attention is distributed in a U-shaped curve (primacy + recency bias).

  Empirically confirmed on recent models: on long slices
  (closer to 1M tokens), extraction accuracy from the middle drops by several times
  even in models advertised as "long-context."

  IMPLICATION FOR THE METAPROMPT AUTHOR:
  - Critical instructions belong at the beginning AND at the end of a file/section, not in the middle.
  - Feed the model selected relevant fragments rather than "the entire corpus."
  - The more precisely a fact is isolated (frontmatter + anchor + short zone),
    the higher the chance it will be sampled and placed into a "strong" attention zone.

─── §0.2 WHAT MAKES RAG MORE RELIABLE ───

  Modern backends (including NotebookLM on modern Gemini), on top of
  basic retrieval, support: hybrid search (semantic + keyword),
  candidate reranking, grounding with citations to specific locations
  in the source, and agentic passes (multiple retrieval iterations).

  Grounding + citations = the primary mechanism for reducing hallucinations:
  the response is tethered to the source and can be verified with a click.

</rag_backend_model>

═══════════════════════════════════════════════════════════════════
§1. FILE SYSTEM STRUCTURE
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: file_structure -->

<file_architecture>

─── MANDATORY FILES ───

  00_INDEX.md        — Main index of the entire system (read first)
  00_CORE.md         — Configuration, identity, entrypoint
  01_ROUTER.md       — Request routing to modules
  [02..N]_MODULE.md  — Thematic modules (one module = one zone)

─── NUMBERING PRINCIPLE ───

  00_*  — System files (config, index, routing)
  01_*  — Routing and orchestration
  02-0N — Content modules (ordered by access frequency)
  [N-1] — Diagnostics and troubleshooting
  [N]   — Templates, recipes, examples

  Numbering = RAG priority when resolving conflicts between chunks of equal weight.
  Lower number → higher priority.

─── FILE SIZE RULE ───

  Optimal:   5,000 – 25,000 characters per file
  Maximum:   50,000 characters (exceeding this — split into parts A/B)
  Minimum:   1,000 characters (smaller is not recommended — better to merge)

  Why: a RAG chunker usually splits text into 512–2048 tokens.
  Files >50K produce chunks with lost heading context.

</file_architecture>

═══════════════════════════════════════════════════════════════════
§2. YAML FRONTMATTER — MANDATORY HEADER FOR EVERY FILE
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: yaml_frontmatter -->

<frontmatter_standard>

// The first thing RAG reads when indexing a file.
// Equivalent to "the first 20-30 words" carrying maximum weight.
// Without frontmatter, RAG does not know what the file is about until reading it through.

─── MANDATORY TEMPLATE ───

---
file_id: [UNIQUE_FILE_ID]
version: [X.Y]
role: [single-word role of the file in the system]
scope: [domain scope — 3-7 words]
rag_priority: [critical | high | medium | low]
description: >
  [1-2 sentences: WHAT the file contains and WHEN it MUST be read]
key_concepts:
  - [concept_1]
  - [concept_2]
  - [concept_3]
depends_on: [list of file_ids this file depends on]
used_by: [list of file_ids referencing this file]
---

─── FIELD EXPLANATIONS ───

file_id          — Unique key for cross-references.
                   Use everywhere instead of file names.
role             — Single word: config | router | engine | vocab |
                   adapter | troubleshoot | templates | index
scope            — Semantic scope for RAG filtering.
rag_priority     — critical: always loaded first
                   high: loaded on relevant queries
                   medium: loaded upon explicit mention
                   low: loaded only on direct query
description      — The most important text. RAG quotes it first.
key_concepts     — Array: each item = a separate retrieval anchor.
depends_on       — Dependency graph. LLM understands what to read together.
used_by          — Backlinks. Helps RAG build context.

─── FILLING EXAMPLE ───

---
file_id: STYLE_ENGINE
version: 1.0
role: engine
scope: style_prompt_construction
rag_priority: critical
description: >
  Contains the formula for building a Style prompt (GMIV+P), a library
  of genre descriptors, hybridization rules, and a persona builder.
  Read on any request to create or improve a Style prompt.
key_concepts:
  - GMIV_formula
  - Time_and_Place_rule
  - instrument_descriptors
  - persona_workshop
  - hybrid_genre_lab
  - production_environments
depends_on: [CORE, AUDIO_VOCAB]
used_by: [ROUTER, TEMPLATES]
---

</frontmatter_standard>

═══════════════════════════════════════════════════════════════════
§3. INDEX FILE: 00_INDEX.md
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: master_index_spec -->

<master_index>

// 00_INDEX.md is the most important file in the system for RAG.
// It MUST be FIRST in the notebook / source list.
// On any generic query, RAG will find it first
// via the system’s shared keywords.

─── MANDATORY INDEX SECTIONS ───

## SYSTEM MAP (table of all files)

| file_id | Purpose | Key concepts | When to query |
|---------|---------|--------------|---------------|
| CORE    | System configuration and identity | preloader, versions, commands | During setup or identity-related questions |
| ROUTER  | Request routing | intent detection, platform, depth | When intent is undefined |
| ...     | ...     | ...          | ...           |

Why a table rather than prose: RAG indexes tables as
structured data — each row = a distinct retrieval signal.

## DEPENDENCY GRAPH (ASCII dependency graph)

  CORE ──► ROUTER ──► MODULE_A ◄── VOCAB
                  ├──► MODULE_B
                  └──► MODULE_C ◄── MODULE_A

The graph allows the LLM to understand which files to read together
without waiting for explicit user instructions.

## VERSION FLAGS

  List: what is new in the current version + which file to read.
  Example: "v2.0: new algorithm X — see MODULE_A §3"

## QUICK QUERY MAP

  Frequently asked questions → file_id + section.
  Example:
  "How to do Y?" → MODULE_B §2
  "What does tag Z mean?" → VOCAB §4

</master_index>

═══════════════════════════════════════════════════════════════════
§4. INTERNAL FILE MARKUP: RAG ZONES
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: internal_markup -->

<rag_zone_system>

// RAG zones are an instrument for isolating semantic units
// within a single file. Without them, a long paragraph is chunked
// arbitrarily, breaking coherence.

─── XML TAGS AS SEMANTIC BOUNDARIES ───

Wrap each semantic section:

  <rag_zone id="[unique_id]">
  ... content ...
  </rag_zone>

  The id MUST be unique across the entire file system,
  not just within the file.

─── HTML COMMENTS AS ANCHORS ───

Before each paragraph/table:

  <!-- rag_anchor: [semantic_key] -->

  Key = what the LLM looks for during a query.
  Example: <!-- rag_anchor: instrument_descriptors_guitars -->

  Anchors work even when XML tags are unsupported:
  HTML comments are read by the parser, but not rendered in the UI.

─── SEPARATING THEORETICAL AND EXAMPLE CONTENT ───

POOR (mixed block):
  ## Rule X
  Explanation of rule X.
  ✅ Example 1
  ❌ Example 2
  Additional explanation.
  ✅ Example 3

GOOD (isolated blocks):

  ## §N.1 RULE: Theoretical Foundation of X
  <!-- rag_anchor: rule_X_theory -->
  Explanation: why rule X works this way.

  ## §N.2 EXAMPLES: Correct Application of X
  <!-- rag_anchor: rule_X_correct_examples -->
  ✅ Example 1 → result
  ✅ Example 3 → result

  ## §N.3 EXAMPLES: Common Mistakes with X
  <!-- rag_anchor: rule_X_wrong_examples -->
  ❌ Example 2 → why this is incorrect

Why: three requests ("what is X?", "show a correct example of X",
"show an error with X") return three precise chunks instead of one
overloaded chunk.

─── MAXIMUM SEMANTIC BLOCK LENGTH RULE ───

  One <rag_zone> = no more than 50 lines / ~2000 characters.
  If a section is longer → split it into §N.1, §N.2, §N.3...

</rag_zone_system>

═══════════════════════════════════════════════════════════════════
§5. ROUTER: TABLES INSTEAD OF PSEUDOCODE
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: router_optimization -->

<router_spec>

// The router file is the most critical for RAG after the index.
// It determines which modules to activate on each query.
// Pseudocode (IF/ELSE) is a poor format for RAG: the model does not understand
// whether it is logic or descriptive text. Tables are the ideal format.

─── KEYWORD → MODULE MAP (mandatory table) ───

<!-- rag_anchor: keyword_module_map -->

| Trigger words/phrases | INTENT | Primary module | Secondary modules |
|-----------------------|--------|----------------|-------------------|
| [words] | [INTENT_NAME] | [file_id §N] | [file_id §N] |

  Why: upon querying "which module handles X?", RAG returns
  a single table row, rather than an entire IF block with unnecessary conditions.

─── INTENT → OUTPUT MAP ───

<!-- rag_anchor: intent_output_map -->

| INTENT | Output format | Variant count | Mandatory fields |
|--------|---------------|---------------|------------------|
| ...    | ...           | ...           | ...              |

─── DEPTH CALIBRATION TABLE ───

<!-- rag_anchor: depth_calibration -->

| Signal | Level | What to include in response |
|--------|-------|----------------------------|
| [signal description] | beginner / pro | [list of elements] |

─── ERROR HANDLING TABLE ───

<!-- rag_anchor: error_handling -->

| Error type | Symptom | Action |
|------------|---------|--------|
| INSUFFICIENT_INPUT | < 3 words without context | Request clarification |
| CONFLICTING_INPUT | Mutually exclusive parameters | Suggest 2 options |
| VERSION_MISMATCH | Feature requested from unavailable version | Inform + offer upgrade |

</router_spec>

═══════════════════════════════════════════════════════════════════
§6. CONTENT MODULES: CONSTRUCTION PRINCIPLES
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: content_module_principles -->

<module_construction>

─── SECTION STRUCTURE ───

Each section of a module is constructed using the schema:

  ## §N. CONCEPT NAME
  <!-- rag_anchor: [concept_key] -->

  <rag_zone id="[concept_key]">

  [1-2 sentences: what it is and why it exists]

  ─── RULES / DEFINITIONS ───
  [normative content]

  ─── EXAMPLES ───
  [declarative content]

  ─── ANTI-EXAMPLES ─── (if applicable)
  [what NOT to do]

  </rag_zone>

─── TABLES VS. PROSE ───

  TABLES for:
    - Mapping (key → value)
    - Comparison (A vs B)
    - Reference guides (parameter → effect → example)
    - Categorized lists

  PROSE for:
    - Explaining cause-and-effect relationships
    - Describing workflow with context
    - Theoretical rationale

─── SECTION NAMING ───

  Good names for rag_anchor (query-discoverable):
    ✅ instrument_descriptors_guitars
    ✅ error_types_vocal_hallucination
    ✅ rule_brackets_theory
    ✅ template_recipe_edm

  Bad names:
    ❌ section_3 (non-semantic)
    ❌ stuff (not specific)
    ❌ more_details (not discoverable by topic)

─── INFORMATION PRIORITY WITHIN A SECTION ───

  The most important content belongs in the first 2-3 lines of the section.
  RAG truncates chunks, not sections. The tail may be lost.

  PRIORITY STRUCTURE:
  1. Definition / rule essence           ← always lands in the chunk
  2. Primary example                     ← almost always
  3. Additional examples                 ← often
  4. Exceptions and edge cases           ← sometimes
  5. Historical context / notes          ← rarely needed

</module_construction>

═══════════════════════════════════════════════════════════════════
§7. DEDUPLICATION: ELIMINATING SEMANTIC CLONES
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: deduplication -->

<deduplication_rules>

// Duplicating content across files is the primary enemy of RAG accuracy.
// Upon querying "what is X?", RAG will return both chunks containing X, and they
// may contradict or complement each other unpredictably.

─── SINGLE SOURCE OF TRUTH RULE ───

  Each concept lives in EXACTLY ONE file.
  In other files — only a REFERENCE to the primary source.

─── REFERENCE FORMAT (instead of duplication) ───

  <!-- rag_ref: [file_id] §[N] [concept_key] -->
  > Full description: see [file_id] §[N].
  > Quick cheat sheet: [5-10 words of the essence].

  A cheat sheet is permissible. It does not duplicate; it creates
  a retrieval anchor pointing to the primary source.

─── PERMISSIBLE EXCEPTIONS ───

  Duplication is permitted ONLY if:
  1. It is a Quick Reference in an INDEX file (no more than 1-2 lines per item)
  2. It is a standalone template/recipe (MUST work without consulting other files)
  3. Version differences (v1 and v2 of a single concept — separate files)

─── DUPLICATE DIAGNOSTICS ───

  When building the system, perform an audit:
  1. List all key_concepts from all frontmatters
  2. Find recurring concepts → keep in one file
  3. In remaining files, replace with <!-- rag_ref: ... -->

</deduplication_rules>

═══════════════════════════════════════════════════════════════════
§8. TROUBLESHOOT FILE: SYMPTOM-INDEXED STRUCTURE
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: troubleshoot_structure -->

<troubleshoot_spec>

// A diagnostic file requires a dedicated structure.
// The user describes a symptom; RAG MUST find the cause + fix.
// With linear text: the query "vocals in instrumental" might return
// the middle of another error type. A symptom table solves this.

─── MANDATORY STRUCTURE ───

  ## SYMPTOM INDEX
  <!-- rag_anchor: symptom_index -->

  | Symptom (how the user will describe the problem) | Type | Section |
  |--------------------------------------------------|------|---------|
  | [symptom description] | TYPE_[N] | §[N].[M] |

  Key: formulate symptoms using USER words,
  not technical terms. RAG matches against incoming query semantics,
  not internal taxonomy.

  ## §N. TYPE_X: [ERROR TYPE NAME]
  <!-- rag_anchor: error_type_X -->

  <rag_zone id="error_type_X">

  Symptoms:   [what the user sees]
  Cause:      [technical explanation]
  Fix:
    1. [step 1]
    2. [step 2]
  Prevention: [how to avoid in the future]

  </rag_zone>

─── DIAGNOSTIC CHECKLIST (for audit mode) ───

  <!-- rag_anchor: diagnostic_checklist -->

  Numbered checklist ordered by importance.
  Each item: CHECK N — NAME — what to check — how to fix.

</troubleshoot_spec>

═══════════════════════════════════════════════════════════════════
§9. TEMPLATES AND RECIPES: ISOLATED STANDALONE BLOCKS
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: templates_spec -->

<templates_spec>

// A template file is read differently than knowledge modules.
// The user seeks a specific template, not theory.
// Each template MUST be a fully standalone chunk.

─── STRUCTURE OF EACH TEMPLATE/RECIPE ───

  ### TEMPLATE: [TEMPLATE_NAME]
  <!-- rag_anchor: template_[unique_key] -->
  <!-- tags: [tag1], [tag2], [tag3] -->

  <rag_zone id="template_[unique_key]">

  Purpose: [1 line — what this template is for]
  Application Context: [when to use]

  [TEMPLATE STRUCTURE ITSELF]

  Parameters:
    [parameter_1]: [description]
    [parameter_2]: [description]

  </rag_zone>

  ---  ← separator between templates (important for the chunker)

─── WHY <!-- tags: ... --> MATTERS ───

  Comment tags generate additional retrieval signals.
  The query "template for EDM" will match the tag "edm" earlier
  than scanning the entire text of the template.

─── TEMPLATE INDEX TABLE ───

  At the beginning of the file — a table of all templates:

  | Name | Purpose | Tags | Section |
  |------|---------|------|---------|
  | [name] | [purpose] | [tags] | §[N] |

</templates_spec>

═══════════════════════════════════════════════════════════════════
§10. CONFIGURATION FILE (CORE): PRELOADER ARCHITECTURE
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: core_config_spec -->

<core_config>

// 00_CORE.md is the single place of configuration storage.
// All system runtime parameters reside here.

─── PRELOADER STRUCTURE ───

  <preloader>
  [PARAMETER_1]  = "[default_value]"  // type | options
  [PARAMETER_2]  = "[default_value]"  // type | options
  </preloader>

  Why <preloader> tags: RAG finds the configuration block
  via a semantic tag, not by position in the file.

─── RUNTIME COMMANDS (commands for changing configuration) ───

  <!-- rag_anchor: runtime_commands -->

  Table format:

  | Command | What it changes | Effect |
  |---------|-----------------|--------|
  | /set [param] [value] | PARAM in preloader | [description] |

─── QUICK REFERENCE RULES ───

  <!-- rag_anchor: quick_reference_rules -->

  Numbered list of 8-12 core system rules.
  Each rule: 1-2 lines, actionable.
  This serves as instant context for the LLM on any query.

─── FILE INDEX (in CORE, brief version) ───

  <!-- rag_anchor: file_index_brief -->

  Table: file_id | role | when to use.
  Brief — the full version is in 00_INDEX.md.

</core_config>

═══════════════════════════════════════════════════════════════════
§11. SYSTEM VERSIONING
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: versioning -->

<versioning_strategy>

─── STRATEGY: DEDICATED NOTEBOOK PER MAJOR VERSION ───

  Recommended: a separate NotebookLM/notebook for each major version.

  Reason: when updating sources, old chunks remain
  in the index and compete with new ones. A dedicated notebook = clean context.

  EXCEPTION: minor versions (v1.1, v1.2) — updating sources
  with a version tag in the frontmatter is sufficient.

─── VERSION FLAGS IN FRONTMATTER ───

  Each file flags its version:
  version: X.Y

  This enables the LLM to answer “this rule is from v1.0, current
  version v1.1 modified it — see §N.2”

─── CHANGELOG FILE ───

  Optional: 00_CHANGELOG.md with a table:

  | Version | Date | File | What changed |
  |---------|------|------|--------------|

  Particularly useful for 20+ files: LLM understands history
  without hallucinating outdated rules.

</versioning_strategy>

═══════════════════════════════════════════════════════════════════
§12. ANTI-HALLUCINATION GUARDS
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: anti_hallucination -->

<anti_hallucination_guards>

// In source-grounded RAG systems, the LLM MUST explicitly signal
// when an answer exceeds the scope of the sources.

─── MASTER PROMPT GUARD (insert into custom instructions / system prompt) ───

  “Answer only on the basis of the sources in this notebook.
   For each substantive point, provide a citation:
   [file_id, §N, rag_anchor].
   If there is no exact citation, state:
   'The sources do not contain a direct answer. This reasoning is based
   on an interpretation of [file_id]'.
   Any claim lacking source support = an error.”

─── GAP ANALYSIS PROMPT ───

  “Using only the sources in this notebook, identify 3-5 categories
   of documentation gaps along the following axes:
   (a) conceptual, (b) procedural, (c) example-based.
   For each gap: description + files containing the closest content +
   formulation of a question to the authors.
   Format as a table. Every point MUST include a citation.”

─── CONFLICT DETECTION PROMPT ───

  “Find contradictions across notebook sources.
   Format: [file_id_A §N] asserts X,
           [file_id_B §M] asserts Y.
   Suggest a resolution or mark as 'open question'.”

─── POSITIVE FORMULATIONS (Trigger Words principle) ───

  Describing a problem in a prompt forces the model to "visualize"
  the problem and amplifies it. Always formulate positively:

  ❌ "do not hallucinate", "avoid errors", "do not fabricate"
  ✅ "answer solely on the basis of the sources"
  ✅ "support every assertion with a citation"
  ✅ "when data is missing, explicitly state so"

</anti_hallucination_guards>

═══════════════════════════════════════════════════════════════════
§13. WORKFLOW FOR CREATING A NEW METAPROMPT SYSTEM FOR RAG
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: creation_workflow -->

<creation_workflow>

STEP 1 — DEFINE SEMANTIC ZONES (prior to writing)
  Write out all concepts in the system.
  Group them by semantic proximity.
  Each group = a separate file.
  Rule: if two concepts are always needed together → one file.
  If needed independently → separate files.

STEP 2 — BUILD DEPENDENCY GRAPH
  Draw an ASCII graph: which file depends on which.
  This will become depends_on / used_by in the frontmatter
  and the DEPENDENCY GRAPH in 00_INDEX.md.

STEP 3 — WRITE 00_INDEX.md FIRST
  Fill in the file table (SYSTEM MAP) — even if files are currently blank.
  This is your "contract" with the RAG system detailing what is where.

STEP 4 — WRITE 00_CORE.md
  Preloader containing configuration.
  Quick Reference Rules (8-12 items).
  Brief file index.

STEP 5 — WRITE 01_ROUTER.md
  Keyword → Module MAP (table).
  Intent → Output MAP (table).
  Depth calibration (table).
  WITHOUT IF/ELSE pseudocode.

STEP 6 — WRITE CONTENT MODULES
  For each file:
  a) Frontmatter
  b) One semantic zone per file
  c) RAG zones inside (XML tags + HTML anchors)
  d) Separate theory and examples
  e) Verify: are there duplicates across other files?

STEP 7 — WRITE TROUBLESHOOT FILE
  Symptom Index table — first.
  Followed by detailed error types with zones.

STEP 8 — WRITE TEMPLATES FILE
  Template index table — first.
  Each template — an isolated zone with tags.

STEP 9 — DEDUPLICATION AUDIT
  Compare key_concepts across all frontmatters.
  Find recurrences → keep in one file, use rag_ref in others.

STEP 10 — TEST IN RAG SYSTEM
  Load into NotebookLM / Gemini Notebooks.
  Ask 10 test questions of varying types.
  Verify: are citations exact? Correct file? No cross-contamination?
  If a citation "cuts off" — the section is too long; split it.

</creation_workflow>

═══════════════════════════════════════════════════════════════════
§14. AUDIT CHECKLIST FOR COMPLETED SYSTEM
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: audit_checklist -->

<audit_checklist>

─── STRUCTURAL AUDIT ───

CHECK 1 — INDEX FILE:
  Is 00_INDEX.md present? Is the SYSTEM MAP table present?
  Is the DEPENDENCY GRAPH present?
  ❌ FIX: Create or complete.

CHECK 2 — FRONTMATTER:
  Does every file have YAML frontmatter?
  Are file_id, role, scope, rag_priority, description, key_concepts filled in?
  ❌ FIX: Add frontmatter using the §2 template.

CHECK 3 — RAG ZONES:
  Is every semantic section wrapped in <rag_zone>?
  Is <!-- rag_anchor: ... --> present before each zone?
  ❌ FIX: Add markup per §4.

CHECK 4 — ROUTER FORMAT:
  Does the router use tables (not IF pseudocode)?
  Is Keyword → Module MAP present?
  ❌ FIX: Rewrite into tabular format per §5.

CHECK 5 — DEDUPLICATION:
  Is identical content absent across two or more files?
  ❌ FIX: Keep in one, use rag_ref in others per §7.

CHECK 6 — TROUBLESHOOT:
  Is the Symptom Index table present at the beginning of the file?
  Are symptoms described using the user’s vocabulary?
  ❌ FIX: Add table per §8.

CHECK 7 — TEMPLATES:
  Is each template isolated inside a separate rag_zone?
  Is the template index table present?
  ❌ FIX: Add separators and zones per §9.

CHECK 8 — FILE SIZE:
  Are all files within the 5K–50K character range?
  ❌ FIX: Split large ones into A/B, merge small ones.

CHECK 9 — THEORY vs EXAMPLES:
  Are theoretical blocks separated from examples?
  ❌ FIX: Split into §N.1 (theory) / §N.2 (examples) per §4.

CHECK 10 — POSITIVE FORMULATIONS:
  Are prohibitive phrases ("do not do X") absent from prompts?
  ❌ FIX: Reformulate positively per §12.

─── FUNCTIONAL TEST ───

  Load into RAG system and ask:
  □ Generic question about the system → MUST return INDEX
  □ Question about a specific concept → exact file + section
  □ Request for a template → isolated template without surplus text
  □ Problem description → Symptom Index → correct type
  □ Question about configuration → CORE preloader
  □ Question about dependencies → graph from INDEX

</audit_checklist>

═══════════════════════════════════════════════════════════════════
§15. QUICK REFERENCE: CORE RULES
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: quick_reference -->

<quick_rules>

1. ONE FILE = ONE SEMANTIC ZONE.
   DO NOT mix different concepts in one file without isolation.

2. FRONTMATTER IS MANDATORY.
   First lines of a file = maximum RAG weight. Without frontmatter,
   RAG does not know what the file is about.

3. 00_INDEX.md IS THE FIRST FILE IN THE NOTEBOOK.
   It defines all subsequent RAG navigation.

4. TABLES > PSEUDOCODE > PROSE for mapping.
   Keyword → Module MAP is always formatted as a table.

5. ZERO DUPLICATION.
   Each concept lives in one file. Others use rag_ref.

6. SYMPTOM-FIRST in Troubleshoot.
   Symptom table comes first; details follow.

7. THEORY SEPARATED FROM EXAMPLES.
   §N.1 = rule. §N.2 = correct examples. §N.3 = errors.

8. TEMPLATES ARE AUTONOMOUS ZONES.
   Each template functions independently without cross-file references.

9. POSITIVE FORMULATIONS IN PROMPTS.
   Naming the problem = amplifying the problem. Describe the desired state.

10. TEST = 10 VARIED QUERIES.
    The system is ready when each of the 10 query types returns
    an exact, uncontaminated chunk.

</quick_rules>

// ═══════════════════════════════════════════════════════════════
// END OF RAG_METAPROMPT_STANDARD v2.0
// ═══════════════════════════════════════════════════════════════
