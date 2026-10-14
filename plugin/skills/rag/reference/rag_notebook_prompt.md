---
file_id: RAG_NOTEBOOK_PROMPT
version: 2.0
updated: 2026-06-21
role: universal_system_prompt
scope: rag_notebook_metaprompt_operation
rag_priority: maximum
description: >
  Ready-to-use universal system prompt + working instruction for
  operating large metaprompts via RAG notebooks (NotebookLM,
  Notebooks in the Gemini app, Claude Projects/Cowork). Distillate
  of proven practices and lifehacks, stripped of ties to specific
  projects. Paste as a system prompt into a notebook or use
  as a checklist when building a metaprompt system.
key_concepts:
  - grounded_backend
  - persona_task_context_output_guard
  - internal_anchoring
  - anti_hallucination
  - notebook_versioning
  - quotas_and_limits
applies_to: [NotebookLM, Gemini_Notebooks, Claude_Projects, Claude_Cowork]
---

# 🧩 RAG NOTEBOOK PROMPT v2.0
# Universal system prompt for working with metaprompts via a RAG notebook

> Two-part document.
> **Part I** — ready-to-use system prompt (copy to notebook / custom instructions).
> **Part II** — working instruction: mechanics, anchoring, lifehacks, limits, patterns.
> All facts are current as of June 2026. Examples are neutral, suitable for any project.

═══════════════════════════════════════════════════════════════════
PART I. READY-TO-USE SYSTEM PROMPT (COPY AS IS)
═══════════════════════════════════════════════════════════════════

<!-- rag_anchor: ready_system_prompt -->

Below is a self-contained system prompt. Paste into the notebook's system
instruction field (in NotebookLM — custom prompt; in Gemini —
notebook instructions; in Claude Project — Project instructions).
Replace values in [square brackets] for your project.

```text
# PERSONA
You are [role: for example, lead engineer/analyst/documentation author]
for the system [SYSTEM_NAME vX.X]. You work ONLY with the sources
of this notebook. You do not go beyond the loaded materials without
explicit user permission.

# TASK_ANCHOR: [unique_task_ID]
[Specific goal in 1–2 sentences. What exactly needs to be produced
as output and why.]

# CONTEXT_SCOPE
Sources: rely on files/tags [list key .md files
or tags relevant to the task].
Allowed: synthesis, comparison of sources, citation with specification
of file and section, identification of contradictions between sources.
Restrictions: do not speculate or interpolate beyond the sources;
do not replace facts from the sources with your own general knowledge;
if web search is used — explicitly separate web data from notebook data.

# OUTPUT_CONTRACT
Format: [table / bulleted list / paragraphs — select].
Volume: [limit, for example "up to 400 words" or "table with 7–10 rows"].
Citation: accompany each substantive thesis with a reference of the form
[file, §section].
Response language: [Russian / Ukrainian / other].

# ANTI_HALLUCINATION_GUARD
Answer based on the notebook sources.
If there is no exact grounding in the sources — state directly:
"There is no direct answer in the sources regarding [topic]; below is an interpretation based
on [file]" — and label such fragment.
Any statement without source backing is considered an error.
If a question goes beyond the scope of the notebook — suggest clarifying the query or
adding missing sources.
```

COMPACT ONE-LINE VERSION (for one-off chat queries):

```text
Role: [role] | Task: [task] | Context: notebook sources only,
no speculating | Format: [output] + citation [file, §] for each thesis |
If there is no data — state directly, do not invent.
```

WHY THIS SPECIFIC STRUCTURE:
A structured prompt (Persona / Task / Context / Output / Guard)
produces a noticeably more accurate and verifiable result than a one-sentence
"search" phrasing. This is the main difference between working
with a grounded backend and free-form chat with a regular LLM.

═══════════════════════════════════════════════════════════════════
PART II. WORKING INSTRUCTION
═══════════════════════════════════════════════════════════════════

───────────────────────────────────────────────────────────────────
§1. MECHANICS: WHAT IS A "GROUNDED BACKEND" AND HOW IT WORKS
───────────────────────────────────────────────────────────────────

<!-- rag_anchor: grounded_backend_mechanics -->

The core idea of the "notebook + chat" bundle: the notebook (NotebookLM) acts
as a grounded backend with verifiable sources and
precise citation, while the chat model (Gemini / Claude) provides reasoning,
synthesis, and — if necessary — web search.

TWO MODES TO DISTINGUISH:

1. INSIDE NotebookLM ITSELF — the answer is STRICTLY tied to sources
   (source-grounded), the web does not intervene in the response by default, each
   thesis is accompanied by an inline citation to a specific spot in the source.

2. NOTEBOOK ATTACHED TO Gemini CHAT — the answer is tied to notebook
   sources, BUT the model CAN additionally invoke web search and other
   tools. This is "the best of both worlds": notebook grounding + freedom
   and recency of chat. The downside — without an explicit guard, the model may mix in
   hallucinations/unverified claims.

IMPORTANT ABOUT CONTEXT (dispelling the myth):
Even with a 1M token window, the backend DOES NOT "load the entire notebook at once"
into every response. A retrieval sample of relevant
fragments is assembled for a specific query, plus the history of the current chat session. The 1M context applies
to a SINGLE session, not to "the entire notebook simultaneously". Therefore,
the structure of sources for retrieval is critical at any volume.

BIDIRECTIONAL INTEGRATION (Notebooks in the Gemini app):
Sources added in one application appear in both.
A chat conducted in the context of a notebook can be indexed back
into the notebook as a separate source — this creates a self-learning
memory layer: drafts and conclusions from chat become material for subsequent
queries. (Google does not document the exact depth of accounting for history across all chats —
see §6 "Open Questions".)

───────────────────────────────────────────────────────────────────
§2. HOW TO BUILD METAPROMPTS FOR A LARGE NUMBER OF SOURCES
───────────────────────────────────────────────────────────────────

<!-- rag_anchor: metaprompt_structure -->

Main principle: STRUCTURE IS MORE IMPORTANT THAN LENGTH. A metaprompt that lives as
a source (.md file) can be verbose; but keep the chat queries
themselves concise, relying on this master prompt.

METAPROMPT FRAMEWORK (same as in Part I):
PERSONA → TASK → CONTEXT/SCOPE → OUTPUT_CONTRACT → ANTI_HALLUCINATION_GUARD.

RECOMMENDATIONS FOR FILE ORGANIZATION:
- Move the framework into a separate file _MASTER_PROMPT.md and use it as
  the notebook system prompt.
- Split the corpus into semantic components (one file = one zone), rather than
  keeping one giant file — even if word count limits allow it.
- Maintain _GLOSSARY.md with definitions of ecosystem terms: the model
  uses it as a terminological anchor during synthesis across modules.

BALANCING STRICTNESS OF GUARD RULES:
Excessively strict prohibitions ("never do X") sometimes reduce
the utility and creativity of responses. For strict domains (law, finance,
security) — a strict guard is justified; for research and
creative tasks — make it softer. Formulate rules POSITIVELY (see §5).

───────────────────────────────────────────────────────────────────
§3. INTERNAL ANCHORING AND INTER-FILE LINKS
───────────────────────────────────────────────────────────────────

<!-- rag_anchor: internal_anchoring -->

When there are many sources (dozens of files), the model loses coherence.
The most common mistake is the absence of anchor identifiers between files.
Robust patterns:

1. ID TAG AT THE BEGINNING OF EACH FILE (HTML comment, not rendered in UI):
   <!-- SOURCE_ID: [ID] | VERSION: [vX.X] | DEPENDS_ON: [other_ID] -->
   The model reads such comments in Markdown and uses them during synthesis.

2. INDEX FILE _INDEX.md WITH A DEPENDENCY MAP:
   table "Source ID → purpose → linked files".
   Helps build coherent responses when approaching source limits.

3. CROSS-REFERENCES IN THE TEXT:
   explicit references of the form [see CHANGELOG vX.X §3] increase the likelihood that
   both linked documents end up in the context of a single response.

4. SEMANTIC TAGS AT THE END OF A SOURCE:
   ## TAGS: [topic1], [topic2], [topic3]
   provide the model with anchors for thematic filtering and quick "topic prompts"
   ("show all steps tagged with [topic]").

(The detailed markup standard — frontmatter, rag_zone, rag_anchor,
rag_ref, deduplication — is moved to a separate document:
RAG_METAPROMPT_STANDARD v2.0.)

OPEN QUESTION: Google does not disclose the exact prioritization algorithm
for sources/chunks (by size, recency, file type). There is no official
confirmation that YAML/HTML metadata is processed differently from
plain text, — but empirically it helps structure the retrieval sample.

───────────────────────────────────────────────────────────────────
§4. WORKFLOWS AND LIFEHACKS (proven community practices)
───────────────────────────────────────────────────────────────────

<!-- rag_anchor: workflows_lifehacks -->

"RESEARCH POD" / SECOND BRAIN WORKFLOW:
1. Ingest — collect all materials (PDF, .md, transcripts, notes)
   into one notebook.
2. Orchestrate — in a chat with the attached notebook, request to build
   a "knowledge map" (Research Map): topics, questions, gaps.
3. Synthesize — the chat model supplements the picture with fresh web data
   (what came out after your sources' date); use the notebook as a
   "hallucination corrector" — a verifier against sources.
A cheap alternative to custom enterprise RAG: you get web access
and reasoning of the chat model plus guaranteed citations and isolation of the notebook.

ITERATIVE PROMPT UPGRADE (self-improvement loop):
notebook retrieves material on a topic → another LLM (e.g. Claude)
rewrites it into a universal metaprompt template following RAG standards →
template returns to the notebook as a master prompt. Convenient for migration
and comparing versions against each other.

PRE-PROCESSING SOURCES BEFORE INGESTION:
run "dirty" text through an LLM with the instruction "structure into Markdown
with headers, remove noise, add metadata". The response quality of the RAG backend
grows multifold on clean, structured sources.

NOTEBOOK VERSIONING — two strategies:
- Version = separate notebook (recommended for major versions):
  lower risk of polluting context with stale chunks; clean retrieval.
- Version = MIGRATION + CHANGELOG tags/files in a single notebook:
  convenient for end-to-end search across the entire stack, but requires strict tracking
  of tags and version marks.
Common choice: a separate notebook per major version + one "meta-notebook"
with a shared glossary and architecture.

"CHATS FROM GEMINI" AS A MEMORY LAYER:
since a chat with an attached notebook can be indexed back
as a source, use this as a self-learning layer: drafts and
analysis from chat automatically become material that the notebook
subsequently checks for errors and contradictions.

───────────────────────────────────────────────────────────────────
§5. PROMPT PATTERNS (ready-made, neutral templates)
───────────────────────────────────────────────────────────────────

<!-- rag_anchor: prompt_patterns -->

POSITIVE FORMULATIONS (core principle):
Describing a problem in a prompt forces the model to "imagine" the problem.
Formulate what is desired, not prohibitions.
  ❌ "do not hallucinate", "avoid errors", "do not make things up"
  ✅ "answer only based on sources"
  ✅ "accompany each thesis with a citation"
  ✅ "if data is missing — state so explicitly"

─── 5.1. GAP ANALYSIS (finding gaps in documentation) ───

"Using only the sources of this notebook, identify 3–5 categories
of gaps along the axes: (a) conceptual, (b) procedural, (c) example-based.
For each gap:
1) problem description in one sentence;
2) files/sections where the gap is particularly noticeable;
3) 1–2 clarifying questions for the authors.
Format as a table. Each thesis — with a citation [file, §]."

─── 5.2. RECURRING TOPICS / GLOSSARY ───

"Analyze sources associated with [version/tag].
Identify 10–15 recurring concepts (modules, protocols, modes).
For each:
1) short definition in your own words;
2) files where it occurs, with a brief citation;
3) whether there are contradictions between sources.
Present as a table — this will form the foundation of _GLOSSARY.md."

─── 5.3. CONFLICT DETECTION (finding contradictions) ───

"Find contradictions between notebook sources.
Format: [file_A §N] claims X, [file_B §M] claims Y.
Suggest a resolution or flag as an “open question”."

─── 5.4. RESEARCH MAP (topic map for a new team member) ───

"Role: analyst of system [NAME] with access to the notebook.
Task: construct a map of topics, questions, and risks for [domain].
Context: use notebook sources; if necessary — web search,
but clearly separate web data from notebook data; do not provide final
security recommendations, only designate risk areas.
Format: first, a list of 7–10 main topics; then for each —
(a) description, (b) related sources, (c) open questions.
Language: [language]."

─── 5.5. CITATION-FORCING GUARD (for mixed notebook+web mode) ───

"Answer based on notebook sources. For each thesis, provide
at least one citation [file, §]. If there is no exact citation — state:
“There is no direct answer in the sources — reasoning based on interpretation”.
Claims without source backing are considered an error."

CONSENSUS ON PATTERNS:
- The best prompts for a grounded backend FORCE citation,
  structure output, and explicitly delineate source boundaries — this is how they
  differ from a "reason freely" style.
- For large projects, a STACK of several linked prompts
  (extract → analyze → synthesize) is more effective than a single "mega-prompt for everything".

───────────────────────────────────────────────────────────────────
§6. QUOTAS, LIMITS, AND HIDDEN CONSTRAINTS (NotebookLM, June 2026)
───────────────────────────────────────────────────────────────────

<!-- rag_anchor: quotas_limits -->

FORMAL NotebookLM LIMITS BY PLAN:

| Parameter               | Free      | Plus / AI Pro | Ultra      |
|-------------------------|-----------|---------------|------------|
| Sources per notebook    | 50        | 300           | 600        |
| Total notebooks         | 100       | 500           | 500+       |
| Words per source        | 500 000   | 500 000       | 500 000    |
| File size (max)         | 200 MB    | 200 MB        | 200 MB     |
| Chat queries per day    | ~50       | up to ~500    | up to ~5000|
| Audio/Video Overviews/d | ~3        | more          | ~200       |
| Deep Research           | ~10/mo    | ~20/day       | ~200/day   |

NOTES:
- The limit of 500 000 words per source is IDENTICAL across all plans (≈650–700
  PDF pages). Technically, one file can hold an enormous corpus, but
  semantic chunking + anchors yield more accurate retrieval than a "wall of text".
- Google periodically changes exact daily counts and does not always publish
  a single unified list — check support.google.com/notebooklm before
  planning heavy workloads.
- Plan pricing is tied to Google AI bundles (Pro / Ultra) and fluctuates —
  verify the current price at the time of use; do not hardcode into the guide.

HIDDEN / EMPIRICAL CONSTRAINTS (based on observations, not official docs):
- Internal "weighted" query consumption: one heavy query with large
  files or context >100K tokens can "cost" multiple regular ones.
- High thinking level consumes a notable share of the output budget on
  "reflections", reducing the usable response length; UI does not display this.
- During peak hours, silent downgrades from senior to junior models and spikes
  in 429/503 errors are possible, while the interface may continue showing the senior model.
  Empirical workarounds: run heavy jobs off-peak, split queries,
  reset chat or move to a new notebook upon "topic drift".
  (All consumption figures are estimated/observational, not guaranteed.)

CONTEXT AT CHAT LEVEL vs NOTEBOOK LEVEL:
1M context applies to a single chat session (retrieval sample of fragments + dialogue
history), not "the entire notebook into every generation". This is typical for
long-context: a large buffer is available, but a retrieval sample is placed into it.

CONSENSUS ON LIMITS:
- The 50 sources ceiling (Free) quickly becomes a bottleneck
  for serious projects — power users upgrade to Plus/Pro for 300 sources.
- Deep Research is a narrower bottleneck than chat queries; save it
  for genuinely heavy tasks.

───────────────────────────────────────────────────────────────────
§7. OPEN QUESTIONS (what is not officially documented)
───────────────────────────────────────────────────────────────────

<!-- rag_anchor: known_unknowns -->

- The exact algorithm for prioritizing sources/chunks (by size, recency,
  file type) is not disclosed.
- Whether YAML/HTML metadata is processed differently from plain text —
  not officially confirmed (empirically it helps).
- How deeply chat accounts for the history of ALL chats associated with the notebook,
  rather than just the current one, — is undocumented.
- The effect of master prompt length in the system field on latency and quality
  with a large number of sources — no public benchmarks exist.
- Whether there are hidden limits on total text volume when connecting a single
  notebook to a chat — officially only per-notebook source caps exist.

───────────────────────────────────────────────────────────────────
§8. CHECKLIST BEFORE LAUNCHING A NOTEBOOK
───────────────────────────────────────────────────────────────────

<!-- rag_anchor: launch_checklist -->

□ System prompt (Part I) is pasted and values are populated for the project.
□ _INDEX.md exists with a map of files and dependencies.
□ ID tag/frontmatter at the beginning of each file; ## TAGS at the end.
□ Corpus is chunked semantically (one file = one zone), no "walls of text".
□ Duplicates are replaced with references (rag_ref), a unified _GLOSSARY.md exists.
□ Guard rules are phrased positively, strictness matches task type.
□ Version = separate notebook (for major versions).
□ Ran 10 test queries of various types: citations accurate? correct
  file? no topic blending?

// ═══════════════════════════════════════════════════════════════
// END OF RAG_NOTEBOOK_PROMPT v2.0
// ═══════════════════════════════════════════════════════════════
