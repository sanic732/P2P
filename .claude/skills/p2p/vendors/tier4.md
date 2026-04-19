<vendors_tier4 id="P2P_v1.1_TIER4">
[PRIORITY_WEIGHT: VENDOR_REFERENCE]
[LAST_VERIFIED: 2026-04-18]
[OVERRIDE: live_specs_YYYYMMDD.md wins if VERSION is newer]
[ROLE: Target model syntax and constraints for Kimi + GLM — REFERENCE_DATA_ONLY]

// ═══════════════════════════════════════════════════════
// §KIMI — Moonshot Kimi K2.5 Series
// MLA+YaRN 256K · Agent Swarm · Mental Sandbox · thinking toggle
// ═══════════════════════════════════════════════════════

<vendor id="Kimi" family="Kimi_K2_Series">

<models>
  Kimi K2.5:          256K ctx (MLA+YaRN) | thinking: on/off per request
  Kimi K2.5 Thinking: 256K ctx | extended reasoning mode
  Kimi K2 Turbo:      128K ctx | faster, less reasoning
</models>

<syntax_rules>
  FORMAT: Plain text or Markdown. XML partially supported.
  TEMPERATURE: 0.6 default.
  THINKING: Toggle per request — on for complex, off for simple.
  CRITICAL: In Thinking mode, no STEP-BY-STEP (same rule as o3/R1).
    STEP-BY-STEP allowed only in OUTPUT FORMAT section.
  AGENT_SWARM: Up to 100 sub-agents. Up to 1500 tool calls per session.
  MENTAL_SANDBOX: Simulates answer before outputting. Use for legal/fact verification.
  CHUNKING: MLA + YaRN interpolation, 256K blocks.
  COST: $0.60/M — 76% cheaper than Claude for similar coding performance.
</syntax_rules>

<critical_warnings>
  AGENT SELF-REVERT: Error Type G — model rolls back fixes in agentic sessions.
    MANDATORY: Add checkpoint instructions before every write operation.
    "Output list of planned changes. Await confirmation before execution."
  OVERTHINKING: Error Type I — Thinking mode on simple tasks wastes 1.2-1.6x tokens.
    Disable Thinking for Tier 0-1 tasks. Use [CONCISE MODE].
  TOOL CALL CONFUSION: Error Type H — mixed JSON/XML formats cause wrong tool calls.
    Enforce single format per session: [OUTPUT FORMAT: JSON ONLY].
</critical_warnings>

<routing_guide>
  K2 Turbo      → Fast tasks, low cost, Tier 0-1
  K2.5          → Agents (leader), visual coding, Tier 1-3
  K2.5 Thinking → Deep reasoning, Tier 2-4
</routing_guide>

<prompt_patterns>
  THINKING_TOGGLE: thinking:on for complex, thinking:off for simple.
  AGENT_SWARM: Set [TOOL BUDGET] Max tool calls: [N]. Max sub-agents: [M].
  CHECKPOINT: Mandatory before writes in agentic mode.
  MENTAL_SANDBOX: "Simulate your answer internally before outputting."
  MLA_YARN: 256K native context. Best long-context performance per dollar.
</prompt_patterns>

<benchmarks>
  SWE-Bench: K2.5 Thinking 76.8%
  HLE: K2.5 50.2% (with tools)
  BrowseComp: 78.4% (Agent Swarm)
  OCRBench: 92.3% (MoonViT-3D)
  Needle-in-Haystack: 94.7%
</benchmarks>
</vendor>

// ═══════════════════════════════════════════════════════
// §GLM — Zhipu GLM-5 / GLM-4.x Series
// Turn-level thinking · Claude-compatible API · real ctx ~200K
// ═══════════════════════════════════════════════════════

<vendor id="GLM" family="GLM_5_Series">

<models>
  GLM-5:        ~200K real ctx | 128K output | turn-level thinking on/off
  GLM-4.7:      ~200K real ctx | 128K output | fallback, Claude-compatible API
  GLM-4.6V:     128K ctx | 24K output | vision, image→code, UI reverse engineering
  GLM-4.6V-Flash: 128K ctx | faster vision
</models>

<syntax_rules>
  FORMAT: Markdown or XML (Claude-compatible API on GLM-4.7).
  TEMPERATURE: 1.0 default | 0.7 coding/SWE | 0 strict agents.
  THINKING: Turn-level toggle — on/off per message, not per session.
  CHUNKING: Structured Segmentation, 128K blocks (GLM-4.6V) or 200K (GLM-5).
  CRITICAL: IDE may show 1M context — this is a display bug.
    Real context limit is ~200K. Do not rely on displayed 1M.
</syntax_rules>

<critical_warnings>
  CONTEXT LIMIT BUG: IDEs and some interfaces display 1M context. Real limit ~200K.
    Exceeding real limit causes silent degradation, not error messages.
  GLM-5 FALLBACK: If GLM-5 shows instability, fall back to GLM-4.7.
  VISION SPECIALTY: GLM-4.6V excels at image→code, PDF parsing, UI reverse engineering.
    For browser/OS agent tasks, GLM-4.6V is competitive with much larger models.
</critical_warnings>

<routing_guide>
  GLM-4.6V-Flash → Fast vision tasks, Tier 0-1
  GLM-4.6V       → Image→code, UI reverse engineering, PDF, Tier 1-2
  GLM-4.7        → Budget alternative to Claude ($0.60/M), Claude-compatible API, Tier 1-2
  GLM-5          → Complex agent chains, backend/infra, Tier 2-3
</routing_guide>

<prompt_patterns>
  TURN_THINKING: Toggle thinking per turn, not per session.
  STRUCTURED_SEGMENTATION: System/Context/Task sections for >100K context.
  CLAUDE_COMPAT: GLM-4.7 accepts Claude-format prompts with minimal adaptation.
  VISION: GLM-4.6V prefers structured sections: Project Map / Open Files / Diff.
</prompt_patterns>

<benchmarks>
  SWE-bench: GLM-4.7 ~73.8%
  Cost: GLM-4.7 $0.60/M (via aggregators)
  Vision: GLM-4.6V competitive with frontier on UI reverse engineering
</benchmarks>
</vendor>

</vendors_tier4>
