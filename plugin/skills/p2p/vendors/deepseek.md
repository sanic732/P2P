---
source_id: vendor_deepseek_v9
version: "9.0"
type: VENDOR_PROFILE
vendor: deepseek
priority: REFERENCE
compatible_with: "db.md | live_specs.md (optional, attached by the user)"
---

// P2P 9.0 — VENDOR: DEEPSEEK — prompting profile. Specs, prices, statuses: live_specs.md
// MODEL_REGISTRY. PRIORITY: an attached live_specs.md > this file.

// §DeepSeek
DEEPSEEK_V4_PRO: the flagship DeepSeek model (exact id: live_specs.md); native OpenAI Responses API; budget powerhouse, native reasoning, code quality; the reasoning target of G16.
  DATA:          VENDOR_REQUEST_RELAY — sensitive or third-party data never to the hosted API; self-hosted weights not affected.
  KNOWN_ISSUES:  G15 (re-inject reasoning_content, never null); G16 (handler accepts 404 and 400).
  THINKING_API:  native reasoning, not controlled from outside; temperature 0.3 reasoning, 0.7 creative.
  MULTI_TURN_FIX: messages.append({"role":"assistant","content":prev.content,"reasoning_content":prev_reasoning})
  IDEAL_FOR:     budget coding T1-T2, code generation; not for sensitive data.

// §Flash — Gemini Flash line and DeepSeek Flash
DEEPSEEK_FLASH:  the fast DeepSeek model (exact id: live_specs.md) — bulk fallback after the fast Gemini model (exact id: live_specs.md), cheap_agentic primary; thinking on by
                 default — turn off for forced tool calls; Agent-Pareto frontier; G15 as V4-Pro; not for sensitive data.

FILE_META:
  COMPATIBLE:  live_specs.md | db.md
