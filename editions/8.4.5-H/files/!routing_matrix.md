---
id: routing_matrix_v8H
version: v8H.3
type: HOST_ENGINE
priority: MEDIUM
load_order: 6.7
triggers: "routing matrix|матрица маршрутизации|tier routing|какой tier|stakes"
depends_on: "!llm_router.md, !!db_v8H.md"
last_verified: 2026-06-27
compatible_with: "all v8H files"
tags: routing-matrix, tiers, auditable, v8h3
---

// ═══════════════════════════════════════════════════════
// P2P v8H.3 — ROUTING MATRIX v2.0 (auditable source of routing truth)
// Порт из 8G.1 !routing_matrix.md. vendors/*.md = reference-only.
// ═══════════════════════════════════════════════════════

// §1. TASK TAXONOMY (Tier → calls / context / stakes)
TASK_TAXONOMY:
  Tier 0 | 1-3 calls   | <8K     | Low      | "Fix typo"
  Tier 1 | 3-8 calls   | 8K-32K  | Low      | "React button"
  Tier 2 | 8-15 calls  | 32K-100K| Medium   | "Dashboard + auth"
  Tier 3 | 15-30 calls | 100K-400K| High    | "Refactor auth system"
  Tier 4 | 30+ calls   | 400K+   | Critical | "New microservices arch"

// §2. ROUTING EXAMPLES (primary → fallback)
ROUTING_EXAMPLES:
  Code Generation:    claude-opus-4-8 / claude-fable-5 (T2-4) → grok-4.3 → deepseek-v4-pro
  Complex Agentic:    grok Heavy-16 (grok host) / claude-fable-5 → kimi swarm → claude-opus-4-8
  Research/Fact-check: gemini-3.1-pro-latest (grounding) / grok-4.3 (X realtime) → deepseek-v4-flash
  UI/Design:          claude-fable-5 (#1 WebDev) / glm-5v → gemini-3.1-pro-latest
  High-Stakes Reason: claude-opus-4-8 (max quality) → grok Heavy-16 → gemini-3.1-pro-latest
  Long Context:       gemini-3.1-pro-latest (2M) / grok-4.20 (2M) → claude-sonnet-5 (1M)
  Budget:             deepseek-v4-flash → glm-5.1-flash → qwen3-plus

// §3. HOST-GATING
// Heavy-16 строки активны ТОЛЬКО при HOST_MODEL=grok (см. !host_profiles GROK_ADVANTAGE_RULE).
// На прочих хостах "grok Heavy-16" → simulated QUORUM на текущем хосте.
// Реальный выбор/исполнение делегируется !llm_router.md (этот файл — аудируемая карта решений).

VERSION_METADATA:
  SYSTEM:      P2P v8H.3 Hybrid · Routing Matrix v2.0
  SOURCE:      donor 8G.1 !routing_matrix.md + Fable5/Opus4.8
  COMPATIBLE:  !llm_router.md | !host_profiles.md | vendors/*
