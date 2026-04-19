<vendors_tier3 id="P2P_v1.1_TIER3">
[PRIORITY_WEIGHT: VENDOR_REFERENCE]
[LAST_VERIFIED: 2026-04-18]
[OVERRIDE: live_specs_YYYYMMDD.md wins if VERSION is newer]
[ROLE: Target model syntax and constraints for DeepSeek + Qwen — REFERENCE_DATA_ONLY]

// ═══════════════════════════════════════════════════════
// §DEEPSEEK — DeepSeek R1 / V3.2
// No CoT (R1 reasons natively) · on-prem · temp 0.3
// ═══════════════════════════════════════════════════════

<vendor id="DeepSeek" family="DeepSeek_R_V_Series">

<models>
  DeepSeek R1:   128K ctx | 16K std / 32K Pro output | reasoning: native internal
  DeepSeek V3.2: 128K ctx | 16K output | reasoning: standard
</models>

<syntax_rules>
  FORMAT: Plain text or Markdown. No deep XML nesting.
  TEMPERATURE: 0.3 analytical ONLY. Higher values break structure.
  CRITICAL: R1 = NO CoT instructions. It reasons natively like o3.
    "Think step by step" degrades R1 output. Short clean instructions only.
  CHUNKING: Structured Segmentation, 128K blocks.
  ON-PREM: Supported. Air-gapped deployment available.
</syntax_rules>

<critical_warnings>
  R1 REASONING: Never add external CoT. State goals and constraints. Model decides how to reason.
  TEMPERATURE: >0.3 analytical breaks structured output. Keep strict.
  COST: $0.27/M tokens — significant budget advantage. Best PRAGMATIST pick for reasoning.
</critical_warnings>

<routing_guide>
  V3.2     → General tasks, budget-friendly, Tier 0-2
  R1       → Deep reasoning, math, proofs, Tier 2-4
  R1 Pro   → Extended reasoning, 32K output, Tier 3-4
</routing_guide>

<prompt_patterns>
  NO_COT: Short clean instructions for R1. No scaffolding.
  LOW_TEMP: Always 0.3 for analytical. Never higher for structured tasks.
  STRUCTURED_SEGMENTATION: 128K blocks for long context.
</prompt_patterns>

<benchmarks>
  Cost: $0.27/M (cheapest frontier reasoning)
  On-prem: Full support, air-gapped
</benchmarks>
</vendor>

// ═══════════════════════════════════════════════════════
// §QWEN — Alibaba Qwen 3.5 Series
// thinking_budget configurable · MoE · on-prem
// ═══════════════════════════════════════════════════════

<vendor id="Qwen" family="Qwen_3_Series">

<models>
  Qwen3.5-Max:       128K ctx | thinking_budget: 0-81920 | flagship
  Qwen3-Coder:       64K ctx  | code specialized
  Qwen3.5-397B-A17B: 128K ctx | MoE flagship (only 17B active of 397B)
  Qwen3-Omni-Flash:  64K ctx  | $0.14/M | cheapest multimodal
  Qwen3-VL:          64K ctx  | vision leader, OCR 99.2%
</models>

<syntax_rules>
  FORMAT: Markdown or plain text. XML partially supported but not native.
  TEMPERATURE: 0.7 default. Adjustable.
  thinking_budget: 0-81920 tokens. Explicit control over reasoning depth.
    0 = no thinking (fastest). 81920 = maximum reasoning.
  MoE FLAG: Architecture is Mixture-of-Experts. Must note in prompt context
    that model activates only 17B parameters per token of 397B total.
  CHUNKING: Hierarchical Context Management, 64K blocks.
  ON-PREM: Supported.
</syntax_rules>

<critical_warnings>
  MoE ARCHITECTURE: The 397B model only activates 17B per token. Performance
    does not scale linearly with parameter count. Set expectations accordingly.
  THINKING_BUDGET: Unlike effort levels, this is an exact token count.
    Too low = shallow reasoning. Too high = wasted tokens on simple tasks.
  VISION: Qwen3-VL is OCR leader (99.2%). Prefer for text-in-image tasks.
</critical_warnings>

<routing_guide>
  Qwen3-Omni-Flash → Cheapest multimodal ($0.14/M), Tier 0-1
  Qwen3-Coder      → Code tasks, Tier 1-2
  Qwen3-VL         → Vision/OCR tasks, Tier 1-2
  Qwen3.5-Max      → General flagship, Tier 2-3
</routing_guide>

<prompt_patterns>
  THINKING_BUDGET: Explicit token allocation. Low for simple, high for complex.
  MoE_FLAG: Note architecture in prompt context for accurate capability expectations.
  HIERARCHICAL_CHUNKING: 64K blocks.
</prompt_patterns>
</vendor>

</vendors_tier3>
