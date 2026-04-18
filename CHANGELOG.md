# CHANGELOG — P2P Claude Edition

All versions documented. Old versions preserved for pedagogical value.

---

## v1.1 (internal: v7C.2) — 2026-04

### English release · GitHub Edition

**Goal:** Public release of P2P for GitHub. Full English translation, agent renames, `/lang` command.

**Agent renames:**
- `ANON` → `FORGE` (Operational Expert / Code Specialist)
  - Rationale: `FORGE` better reflects the agent's role — forging production-ready code and agentic prompts
- `KSENIA` → `LYRA` (Live Chat — Creative Brainstorm Partner)
  - Rationale: neutral public name for the creative companion persona

**New features:**
- `/lang` command in UI menu (item 29): toggles system output language between English and Russian
- Language state persists for the session; resets on `start`
- All Russian UI text translated to English; Russian keyword routing preserved for backward compatibility with existing users

**Architecture:** No breaking changes vs v1.0. All 20 modules preserved. Menu items 1–28 unchanged.

**Files affected:** !!core_claude.md, !agents_claude.md, !routing_claude.md, !global_index.md, !sandbox_user.md, user_context.md, README.md (new), CHANGELOG.md (new)

---

## v1.0 (internal: v7C.1) — 2026-03

### Feature release

**Summary:** 17 patches across 9 files. ~614 new lines (total: ~4214). 28 menu items (was 26).

**Removed:**
- LIVE_CHAT system (Ksenia / P2P_Orchestrator) — removed from core, stub retained in agents file for reference

**Fixed:**
- OUTPUT_LIMIT values for Sonnet/Haiku: corrected from 8K → 64K
- DUAL_MODE detection: false positive on Chat mode with project_knowledge_search not present
- Routing: Russian trigger words now correctly matched
- Format Oscillation (Error P): added to error taxonomy with diagnostic script

**Added — Techniques (9 new):**
1. Structured Decomposition
2. RAG Grounding
3. Persona Cascade
4. Reflection Loop
5. Gate Pattern
6. Scaffold Pattern
7. Adversarial Pair
8. MCP Tool Prompt
9. Migration Transform

**Added — Error types (3 new, completing A–P taxonomy):**
- Type N: Hallucinated Tool Call
- Type O: Safety Over-Refusal
- Type P: Format Oscillation

**Added — Agents (per-agent enhancements):**
- All 7 active agents: explicit `failure_modes` blocks
- FORGE (prev. ANON): Stop Conditions block, Environment Block (from WARP pattern)
- AXIOM: Self-Critique function (`!crit`), Fallback Generator
- VECTOR: Fabrication Banned List — 5 techniques blocked from generated prompts
- ARCHITECTON: Primacy/Recency 30/55/15 rule, Technique Selector (auto by task type), Priority Matrix 60/30/10
- QUORUM: Full weight distribution table inline (per task_type)
- Cross-Agent Protocols: collision patches unified in one section

**Added — Contract Builder:**
- Step 10: Format Enforcement (model-specific format locking)
- Step 11: Post-Deployment Iteration protocol

**Added — Chain Orchestrator (menu item 27):**
- Decompose task into N-step prompt pipeline
- Each step: TECTON (structure) + IRIS (strategy) + FORGE if code, DATOS if research
- Chain Route in !routing_claude.md

**Added — Feedback Loop Protocol (menu item 28):**
- Iterative prompt improvement from test results
- Feedback Route: AXIOM (diagnose) + TECTON (patch)

**Added — Writing Suite (5 new tone profiles):**
- Corporate Formal
- Startup Casual
- Academic
- Marketing
- Technical Documentation

**Added — Templates (2 new):**
- Template J: Tool Use Prompt (model-specific tool calling syntax)
- Template K: Chain of Prompts (multi-step pipeline template)

**Added — Contract Mode Warning:**
- Claude 4.x literal execution: every MUST paired with MUST NOT
- Cross-Model Generation Awareness: syntax checks before generating for non-Claude targets

**Files affected:** All 20 modules. Breaking changes within v7C.x: none.

---

## v0.9 (internal: v7C.0) — 2025-12

### Initial Claude-native release

**Architecture shift:** Monolithic (2 files) → Modular (20 files)

**What changed from v6.3 (universal multi-model):**
- Host is now always Claude — no more TARGET_MODEL variable in PRELOADER
- Vendor files (tier 1–4) become REFERENCE_DATA_ONLY — target model specs only, not host configs
- Routing extracted to `!routing_claude.md` (was inline in core)
- 8 agents with full persona specs in dedicated `!agents_claude.md` (was in db, menu-only)
- Contract mode implementation: Claude 4.x literal execution awareness throughout
- New tools: Contract Builder (9 steps), Memory Bridge, Writing Suite, ATLAS [BETA]
- User isolation: PRELOADER (was entire config) → Sandbox + user_context separation
- RAG optimization: 20 anchor-tagged files for Claude Projects semantic search
- Dual-mode bridge: auto-detects Projects vs Chat mode

**Files:** 20 modules, all new. 28 menu items.

---

## v6.3 and earlier

> Versions v6.x and below used a 2-file universal architecture (core + db) supporting multiple host models simultaneously.  
> These versions are archived in the `OLD version/` folder alongside v7C releases.
> P2P v1–v6 history (Russian): see `пост 4pda.txt` files in the P2P v1–v6 directories.
