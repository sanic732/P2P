<vendors_tier1 id="P2P_v1.1_TIER1">
[PRIORITY_WEIGHT: VENDOR_REFERENCE]
[LAST_VERIFIED: 2026-04-18]
[OVERRIDE: live_specs_YYYYMMDD.md wins if VERSION is newer]
[ROLE: Target model syntax and constraints for Claude + GPT — REFERENCE_DATA_ONLY]

// ═══════════════════════════════════════════════════════
// §CLAUDE — Anthropic Claude 4.6 Series
// XML-native · Extended Thinking · Contract mode
// ═══════════════════════════════════════════════════════

<vendor id="Claude" family="Claude_4_Series">

<models>
  Opus 4.6:   200K ctx (1M beta) | 128K output | $15/$75 per 1M | effort: low-max
  Sonnet 4.6: 200K ctx (1M beta) | 16K output  | $3/$15 per 1M  | effort: low-max
  Haiku 4.5:  200K ctx           | 8K output   | $0.80/$4 per 1M | effort: low-max
</models>

<syntax_rules>
  FORMAT: XML-native. Wrap all logical blocks in XML tags.
  Structure: <role> → <tone> → <background_data> → <rules> → <examples> → <task> → <thinking> → <output_format>
  Prefilling: API-only — pre-fill assistant response to force format.
  Extended Thinking: Native adaptive. Set effort level, not thinking_budget.
  Structured output: ALWAYS use Tool Calling or Structured Outputs API for JSON.
    Text prompting for JSON is unreliable — model adds preamble or quotes.
</syntax_rules>

<critical_warnings>
  CONTRACT MODE: Claude 4.x follows instructions literally. No "above and beyond."
    Every instruction must be explicit. Pair MUST with MUST NOT.
  REFUSAL: 33% refusal rate on CP3 security tasks. Use Defensive Framing for legitimate code analysis.
  COST: Pro = 5 hours "effort" per day. Effort:max can exhaust daily limit in one session.
  THINKING COST: Simple 200-token request can generate 5000+ hidden CoT tokens. Set effort:low for Tier 0-1.
</critical_warnings>

<routing_guide>
  Haiku 4.5   → Tier 0-1, chatbots, automation, quick transforms
  Sonnet 4.6  → Tier 1-2, daily dev, cost/quality balance
  Opus 4.6    → Tier 2-4, agents, audit, planning
  Opus Thinking → Coding Deep Think (Elo 1556), NOT for dialogue
</routing_guide>

<prompt_patterns>
  XML_FIRST: All blocks in strict XML tags.
  EFFORT_CONTROL: effort:low (T0-1) → medium (T1-2) → high (T2) → max (T3-4).
  CONTEXT_COMPACTION: [ANCHOR: critical_data] for blocks that must not be summarized.
  AGENT_CHECKPOINT: "Output list of changes before applying" for long agentic sessions.
  CHUNKING: Semantic Chunking, 64K blocks.
</prompt_patterns>

<benchmarks>
  LMSYS Overall: Opus 1504, Sonnet ~1497
  LMSYS Coding: Opus Thinking 1556 (leader)
  SWE-Bench: Opus 80.8%, Sonnet 79.6%
  HLE: Opus 53.0%
  BrowseComp: Opus 84-86.8% (leader)
  AIME 2025: Opus 100%
</benchmarks>
</vendor>

// ═══════════════════════════════════════════════════════
// §GPT — OpenAI GPT-5.x / o3 / o4-mini Series
// Markdown headers · reasoning_effort · CTCO Framework
// ═══════════════════════════════════════════════════════

<vendor id="GPT" family="GPT_5_Series">

<models>
  GPT-5.4:       128K ctx | 16K output | reasoning: standard
  GPT-5.4-Pro:   128K ctx | 16K output | reasoning: enhanced
  o3:            200K ctx | 100K output | reasoning: native internal
  o4-mini:       200K ctx | 100K output | reasoning: native internal, faster
  GPT-5.3-Codex: 192K ctx | long-horizon agents, mid-task steering
</models>

<syntax_rules>
  FORMAT: Markdown headers + numbered lists + **bold** emphasis.
  Structure: ## Role → ## Context → ## Task → ## Rules → ## Output Format (CTCO Framework)
  CRITICAL: o3/o4 = NO CoT instructions. They reason internally.
    "Think step by step" DEGRADES o3 output. State what you want, not how to think.
  reasoning_effort: low | medium | high (o3/o4 only — controls compute spend).
  Structured output: JSON mode reliable. Specify schema explicitly.
</syntax_rules>

<critical_warnings>
  o3 REASONING: Never add external reasoning scaffolding. Short clean instructions ONLY.
  DOCUMENT MAP: >272K tokens → auto-compact via model_auto_compact_token_limit.
  GPT-5.3 Garlic: Perfect Recall to 400K (99.9%) — chunking not needed.
  COMPUTER USE: GPT-5.4 native computer use, OSWorld 75%.
</critical_warnings>

<routing_guide>
  o4-mini     → Fast reasoning, cost-efficient, Tier 0-2
  GPT-5.4     → General purpose, strong writing, Tier 1-3
  o3          → Deep reasoning, math, proofs, Tier 2-4
  GPT-5.3-Codex → Long-horizon agent tasks, multi-tool orchestration
</routing_guide>

<prompt_patterns>
  CTCO: Context-Task-Constraints-Output framework.
  REASONING_GUARD: No CoT for o3/o4. Clean instructions only.
  DOCUMENT_MAP: 272K auto-compact. Use [SECTION: TITLE] delimiters.
  CHUNKING: Document Map 272K blocks. Garlic: no chunking needed.
</prompt_patterns>

<benchmarks>
  MMMU-Pro: GPT-5.4 81.2%
  Computer Use: GPT-5.4 OSWorld 75%
  Garlic Perfect Recall: 400K, 99.9%
</benchmarks>
</vendor>

</vendors_tier1>
