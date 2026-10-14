---
source_id: vendor_gemini_v9
version: "9.0"
type: VENDOR_PROFILE
vendor: gemini
priority: REFERENCE
compatible_with: "db.md | live_specs.md (optional, attached by the user)"
---

// P2P — VENDOR: GEMINI (Google) — prompting profile. Specs, prices, statuses: live_specs.md
// MODEL_REGISTRY. PRIORITY: an attached live_specs.md > this file.

// §Gemini — Google (Flash line below)
The flagship Gemini model (exact id: live_specs.md): google_frontier and long_docs primary; long context, Google Search native, multimodal.
  KNOWN_ISSUES:  G1 (no temperature on current Gemini models (versions: live_specs.md)), G2 (ZERO XML), G4 (thinkingLevel, not thinking_budget), G11 (HIGH only after
                 the Value Gate), G12 (hard 429 → Flash for high frequency), G13 (reinject every 25 messages);
                 MODEL_CAPACITY_EXHAUSTED in Antigravity IDE (single report) [S].
  IDEAL_PROMPTS: ## Markdown headers, **bold**, plain sections, ZERO XML:
                 ## Role / ## Task / ## Rules (MUST: … / MUST NOT: …) / ## Output Format
  THINKING_API:  thinkingConfig {thinkingLevel:"MEDIUM"}; depth only through thinkingLevel.
  CINE_PROMPTING (video): Dolly Zoom, Volumetric lighting, Anamorphic flare, Rack focus, Crane shot, Dutch angle;
                 pattern [Subject] + [Camera move] + [Lighting] + [Lens/Style]; video target the fast Gemini model (exact id: live_specs.md).

// §Flash — Gemini Flash line
The balanced / fast Gemini model (exact id: live_specs.md): bulk primary; native Computer Use in the API; concision, not capability. G2 (ZERO XML) as Pro;
                 thinking_level "minimal" → error; no G12 (soft limit + queue). G13 on current Gemini models (versions: live_specs.md) — not
                 cleared: Context Caching API, history limits, no large batches of images (long non-English contexts most).
                 GEMINI38_FLASH_OVERLOAD: backoff. Ideal: high-frequency calls, bulk multimodal.
The fast Gemini model (exact id: live_specs.md): fast fallback; same G2 / G13 guards.

FILE_META:
  COMPATIBLE:  live_specs.md | db.md
