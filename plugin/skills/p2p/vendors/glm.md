---
source_id: vendor_glm_v9
version: "9.0"
type: VENDOR_PROFILE
vendor: glm
priority: REFERENCE
compatible_with: "db.md | live_specs.md (optional, attached by the user)"
---

// P2P 9.0 — VENDOR: GLM (Z.ai) — prompting profile. Specs, prices, statuses: live_specs.md
// MODEL_REGISTRY. PRIORITY: an attached live_specs.md > this file.

// §GLM — Z.ai
                 The flagship GLM model (exact id: live_specs.md) — top of the line, weights on HF: the strongest open-weight option with weights really
                 published → air-gapped and reproducible runs. Fallback balanced GLM model (exact id: live_specs.md). High token counts → fallback balanced GLM model (exact id: live_specs.md).
                 The fast GLM model (exact id: live_specs.md): multimodal.
                 OpenRouter AI Gateway works for GLM — no workaround needed.
  SYNTAX:        ## Structured Segmentation, ZERO XML; temperature 0 for strict JSON; thinking on|off per turn.
  VISION_PATTERN: ## Project Map / ## Open Files / ## Diff — UI reverse engineering.
  BASELINE:      GLM family (historical: live_specs.md).

FILE_META:
  COMPATIBLE:  live_specs.md | db.md
