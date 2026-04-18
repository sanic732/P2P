<vendors_tier2 id="P2P_v1.1_TIER2">
[PRIORITY_WEIGHT: VENDOR_REFERENCE]
[LAST_VERIFIED: 2026-04-18]
[OVERRIDE: live_specs_YYYYMMDD.md wins if VERSION is newer]
[ROLE: Target model syntax and constraints for Gemini + Grok — REFERENCE_DATA_ONLY]

// ═══════════════════════════════════════════════════════
// §GEMINI — Google Gemini 3.x Series
// Deep Think · NO XML · temperature=1.0 · Late Chunking
// ═══════════════════════════════════════════════════════

<vendor id="Gemini" family="Gemini_3_Series">

<models>
  Gemini 3.1 Pro Preview: 1M ctx | 65K output | Deep Think native
  Gemini 3 Flash Preview: 1M ctx | 65K output | fast, thinking_budget configurable
  Gemini 3.1 Flash-Lite:  1M ctx | 65K output | cheapest, edge deployment
</models>

<syntax_rules>
  FORMAT: NO XML — conflicts with native Chain of Hindsight (CoT).
  Use plain text structure with clear section headers.
  Structure: ROLE: → CONTEXT: → TASK: → CONSTRAINTS: → OUTPUT:
  Deep Think: Chain of Hindsight mechanism. Temperature MUST = 1.0 (strict requirement).
  thinking_budget: Configurable for Flash/Flash-Lite.
  CRITICAL: NEVER enforce structural tags (XML/JSON/Lists) for internal CoT.
    Formatting only in OUTPUT section.
  STEP-BY-STEP: Forbidden in reasoning. Allowed only in OUTPUT FORMAT.
</syntax_rules>

<critical_warnings>
  TEMPERATURE: Must be 1.0 for Deep Think. Other values break reasoning quality.
  NO XML: XML tags interfere with native CoT. Use plain text delimiters.
  CONTEXT DRIFT: ~9% in sessions >50 messages (Error Type F). Apply CLAUDE_MD technique.
  LATE CHUNKING: 100K blocks. Do not segment smaller.
</critical_warnings>

<routing_guide>
  Flash-Lite   → Edge, real-time, cheapest, Tier 0-1
  Flash        → Balanced speed/quality, Tier 1-2
  3.1 Pro      → Deep analysis, GPQA 94.3%, research, Tier 2-4
  3.1 Pro Deep Think → Frontier tasks, scientific modeling
</routing_guide>

<prompt_patterns>
  NO_XML: Plain text structure only.
  DEEP_THINK: temp=1.0, no CoT scaffolding, let model reason natively.
  LATE_CHUNKING: 100K blocks for documents.
  ANCHOR_CONTEXT: For sessions >50 messages.
</prompt_patterns>

<benchmarks>
  GPQA Diamond: 3.1 Pro 94.3%
  ARC-AGI-2: 3.1 Pro 77.1%
  BrowseComp: 85-86%
  APEX-Agents: 33-34%
</benchmarks>
</vendor>

// ═══════════════════════════════════════════════════════
// §GROK — xAI Grok 4.x Series
// Drift guard · low censorship · x_stream
// ═══════════════════════════════════════════════════════

<vendor id="Grok" family="Grok_4_Series">

<models>
  Grok 4.1:          128K ctx | ~90K output (truncation risk >70%) | standard
  Grok 4.2 Fast:     128K ctx | ~90K output | faster, less reasoning
  Grok 4.2 Thinking: 128K ctx | ~90K output | extended reasoning
</models>

<syntax_rules>
  FORMAT: Flexible — Markdown or plain text both work.
  TEMPERATURE: 0.3 analytical | 0.7 creative.
  DRIFT GUARD: Explicit topic anchoring required. Re-state task every 3rd turn.
  CHUNKING: Standard 128K. Mandatory for outputs approaching 90K.
  OUTPUT RISK: ~90% truncation risk on very long outputs. Always use chunking.
</syntax_rules>

<critical_warnings>
  TOPIC DRIFT: Error Type K — Grok loses focus in long context. Severity increases >10K output.
    Inject: "[TOPIC ANCHOR: Original task = {task}. Stay on target.]" every 3rd turn.
  TRUNCATION: Output approaching model limit often truncates silently.
    Mandatory chunking for any output >50K tokens.
  CENSORSHIP: Lowest refusal rate (~0.3% in Fun Mode). Best for uncensored creative.
</critical_warnings>

<routing_guide>
  Grok 4.2 Fast → Quick tasks, low latency, Tier 0-1
  Grok 4.1      → Creative writing (lowest censorship), Tier 1-2
  Grok 4.2 Thinking → Analytical tasks, Tier 2-3
</routing_guide>

<prompt_patterns>
  DRIFT_GUARD: Re-state task every 3rd turn. Use [TOPIC ANCHOR] markers.
  LOW_CENSORSHIP: Best for creative tasks that trigger over-refusals on other models.
  CHUNKING: Standard 128K. Plan outputs in segments.
</prompt_patterns>

<capabilities>
  x_stream: true | vision: true | real_time: true
</capabilities>
</vendor>

</vendors_tier2>
