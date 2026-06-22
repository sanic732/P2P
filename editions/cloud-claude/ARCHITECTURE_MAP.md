# P2P v8C.3 — ARCHITECTURE MAP (maintainer's graph)

> **DEV ARTIFACT — NOT loaded at runtime.** Purpose: any Claude session / maintainer opens this
> and understands P2P internals before touching anything. Token-dense English on purpose.
> **Update the Route Changelog (§9) on every structural change.**
> Last updated: 2026-06-14

---

## 0. What P2P is (mental model)
Meta-prompt that **writes prompts** OR **executes tasks directly**. Mission: *kill prompt-engineering
for the end user* — user speaks plain intent, P2P picks technique/model/mode under the hood.
It is a **composition engine** (knowledge bricks combined dynamically), NOT a category tree.
Author-original concepts (QUORUM, SCOPE.HELM, ATLAS, VECTOR, SIR…) — NOT taken from papers.

Two distributions (syntactically incompatible — never mix):
- **for-chat** → Projects / Chat / API. Files use `!`-prefix (`!!core_v8C.md`, `!rag.md`).
- **cowork-code** → Claude Code / Cowork. Descriptive names, no `!` (`core.md`, `rag.md`).

Naming map: `!!core_v8C`↔`core`, `!!db_v8C`↔`db`, `!agents`↔`agents`, `!contract`↔`contract_builder`,
`!intent`↔`intent_engine`, `!metrics`↔`session_metrics`, `!scope`↔`scope_helm`, `!memory`↔`memory_bridge`,
`!visual`↔`visual_suite`, `!writing`↔`writing_suite`, `_index`↔`global_index`, `_preloader`↔`preloader`.

---

## 1. Load layers
```
BASE (always):   _preloader → !!core_v8C → !!db_v8C → _live/MANIFEST → _live/live_core → _live/live_claude
LIVE:            _live/live_vendors  (+ vendors/live_specs_YYYYMMDD.md = full spec, PRIORITY override)
ON-DEMAND v8C.2: agents contract debug domain exploration intent memory mentor metrics
                 scope templates tool_budget user_context sandbox visual writing teacher
ON-DEMAND v8C.3: rag reasoning routing compression security optimization   (menu [35-40])
```
Live specs update flow (works in ALL editions): user drops new `live_specs_*.md` → types `старт`/`/p2p`/`full ui menu`
→ menu version+date auto-refresh. This is why a single file update propagates без перевыпуска метапромта.

---

## 2. Vertical dependency (depends_on)
```
_preloader (none)
  └─ !!core_v8C  ──depends── _preloader, _live/{MANIFEST,live_core,live_claude}
       └─ !!db_v8C ──depends── !!core_v8C
            └─ most ON-DEMAND modules ──depends── !!core_v8C (+ !!db_v8C for some)
 special: !sandbox→[_preloader,!user_context]  !visual→[!!db,!templates]  !writing→[!!db,!contract,!agents]
          !routing→[!!core,_live/live_vendors]
```

## 3. Horizontal cross-reference (who calls whom) — from graph scan 2026-06-13
```
INBOUND hubs (most referenced): core 23 · db 20 · contract 12 · memory 12 · debug 11 · metrics 11 · intent 11
                                agents 9 · templates 9 · visual 6 · writing 6
OUTBOUND (calls others most):   _index 51 · _preloader 21 · _master 20 · teacher 16 · exploration 9 · intent 8
v8C.3 modules = ISLANDS:        inbound 2-3, outbound 0-2 (reasoning/security/optimization = 0 outbound)
                                → being woven into work routes (Step 5: contract→routing, intent→reasoning/security…)
```

## 4. Activation (trigger registry)
- Schema unified 2026-06-13: **all functional modules use `triggers:` (plural)**. (Was: 6 v8C.3 modules used `trigger:` singular → invisible to matcher.)
- No-trigger (menu/command-activated only): core, db (BASE), sandbox, teacher, visual, writing.
  ⚠ visual/writing SHOULD get triggers (domain auto-activation) — Step 5 todo.
- **No central matcher exists in core** — activation relies on host model + env skill-engine.
  Strongest in Code/Cowork (skill description-match), weakest in Projects/Chat (plain text).

## 5. Control mechanisms (v8C.3)
- **VERSION_COMPAT** (`_preloader`): `v8C2/v8C3 on|off` + 6 `MODULE_*` flags (`false|true|auto|or`). Safety valve — disable all-new, keep old.
- **PILOT** (`!!core`, added 2026-06-13): `co-pilot|auto-pilot|manual` axis. WRAPS (does not duplicate) DEEP_THINK_VALUE_GATE + IDEALIST/PRAGMATIST + 9-step contract + SIR. `USER_LEVEL↔PILOT_MODE` synonyms. Public default = co-pilot.
- **INTERACTIVE_CHOICE** (in `<pilot_mode>`): env-aware — clickable in Code/Cowork, numbered `[1]/[2]/[3]` in Projects/Chat.
- **GLASS COCKPIT** (manual level): show which techniques/modules applied + why (SIR route, effort/model choice).
- **SHERPA** (`!!core`/`core`, added 2026-06-14): env-feature coach. TRI_MODE-aware — before a task, surfaces native
  environment features the user may not know (plan-mode, effort slider, settings) via INTERACTIVE_CHOICE. Upgrades
  `teacher` from formal course → inline coaching. Flag `SHERPA: auto|on|off` in preloader (auto=ON at co-pilot) + `/sherpa` toggle.
- **PERSONA_HINT** (sandbox): session-scope override of the level axis — beats PILOT_MODE for current session without editing preloader.
- **CONFLICT_RESOLVER v1.0** (`!!core`): fires when v8C2=on AND v8C3=on. + **TECHNIQUE_COMBINATOR** matrix (in db) — technique conflict → predict outcome of each → user picks. ⚠ 6 v8C.3 modules to be added to matrix — Step 4 todo.
- **DEEP_THINK_VALUE_GATE** (db): decides effort low/med/high. **SIR Scanner** (core): Signal→Intent→Route. **5D / 9-step contract**: prompt build with clarifying Q.

## 6. Key runtime routes
```
/p2p|старт|full ui menu → STARTUP_LOGO → FULL menu [1-40] + ✈ PILOT toggle
plain intent (Tier≥2)   → SIR Scanner → (PILOT co-pilot: intake interview) → route to module(s) → output
prompt request          → !contract (9-step) → [Step5: → !routing model/effort advice]
"реши сам" / Q:         → QUORUM (8 agents) → HELIOS synthesis
conflict of techniques  → CONFLICT_RESOLVER → predict A vs B → INTERACTIVE_CHOICE
```

## 7. Known weak spots / techdebt (live)
- [x] visual/writing "untriggered" — RESOLVED 2026-06-14: was 3rd field-name variant `trigger_keywords:` → unified to `triggers:` (visual/writing/sandbox ×2 distros). Schema now fully uniform.
- [x] v8C.3 modules under-linked — RESOLVED 2026-06-14: intent §2.5 MODULE HANDOFF wires all 6 into the router hub.
- [x] 6 modules not in conflict matrix — RESOLVED 2026-06-14: db COMBINATOR extended + Fabrication Banned List disambiguation (USC≠SC, ToT≠MCTS).
- [ ] cowork distro is Russian (for-chat instructions were English-converted; cowork not) — non-breaking
- [x] index trees (_index/global_index) list 6 v8C.3 modules + art — RESOLVED 2026-06-14 (both distros).
- [x] banners → user docs — RESOLVED 2026-06-14: docs/MODES_GUIDE.md (for-chat) with PILOT/SHERPA/QUORUM/SCOPE.HELM/EXPLORATION banners + plain-language descriptions.
- [ ] cowork preloader BASE load-order still uses `!!core_v8C.md` notation vs real `core.md` files (legacy, non-breaking)

## 8. Editions beyond 8C (do NOT touch in 8C work)
8A.1 (Gemini, ZERO-XML) · 8G.1 (Grok, Heavy16 parallel) · 8N.1 (Universal multi-host). Each architecture-specific.

## 10. Evolution v6→v7→v8 (why things are where they are)
- **v6 LEGION** = monolith (core+db+vendors), multi-host via TARGET_MODEL IF/ELSE. Suffered Attention Sink in RAG.
- **v7 CORTEX** = birth of modularity (1 file = 1 semantic zone = precise RAG recall). Split host↔target: 7C=Claude-only.
  NEW modules born here (still in 8C): Intent Engine (9D), Contract Builder (9-step), Memory Bridge, Writing Suite.
  Also: Sandbox 5 fields, Tier Depth Modes (NANO/STANDARD/ADVANCED/FULL), Fabrication Banned List, live_specs override + staleness guard (60d→DATOS warns).
- **v8 NEXUS** = current. 5 editions (8C Claude / 8A Gemini / 8G Grok / 8N universal). 8C = XML-native.

### Cross-version findings that affect current work
- **PERSONA_HINT (sandbox, since v7)** = proto user-level. PILOT must also honor it as the SESSION-scope override
  of the level axis (PILOT_MODE = persistent in preloader · PERSONA_HINT = disposable in sandbox). → enhance Step 2/5.
- **Fabrication Banned List (VECTOR)** bans USC, ToT, GoT, MoE-prompting, chaining-as-layers. v8C.3 !reasoning.md
  adds Self-Consistency (≈USC?) and MCTS (≈ToT?). **Step 4 MUST disambiguate**: USC≠SC / ToT≠MCTS, or VECTOR will
  veto P2P's own new techniques. This is the core "do no harm" check.
- **Chain Orchestrator RESEARCH_DRAFT_REVIEW** (cheap model plans, expensive executes) already encodes the
  "ТЗ на Sonnet, исполнение на Opus" pattern user described — Step 5 advisor should reference it, not reinvent.
- **9D Intent (max 3 clarifying Q) + PROJECT_CARD auto-fill** = the existing intake. CO-PILOT deepens it, not replaces.

## 9. Route Changelog (UPDATE ON EVERY STRUCTURAL CHANGE)
- 2026-06-13 — Step 1: activation schema unified `trigger→triggers` (6 v8C.3 modules, both distros).
- 2026-06-13 — Step 2: PILOT axis added to `!!core`/`core` + `PILOT_MODE` in preloader (both distros). Toggle in menu header. INTERACTIVE_CHOICE + GLASS COCKPIT defined. USER_LEVEL↔PILOT_MODE linked. Public default beginner/co-pilot.
- 2026-06-14 — Step 2b: SHERPA mode (env-feature coach, TRI_MODE-aware, upgrades teacher→inline) in core+preloader both distros. PILOT now honors PERSONA_HINT (sandbox session override). v7 CORTEX read → v6→v8 gap closed (§10 added).
- 2026-06-14 — Added `!art.md`/`art.md` (OPTIONAL eye-candy): compact ASCII banners for mode-changing features (PILOT ×3, SHERPA, QUORUM, SCOPE.HELM, EXPLORATION). ON-DEMAND, zero tax when not loaded. Registered in preloader load-order (optional section). TODO: mirror banners into user docs (visual recognition between interface ↔ guide).
- 2026-06-14 — SIMULATION PASS (load-order + XML + vendor/ANON): (a) XML hygiene — inline tag refs `<pilot_mode>`/`<sherpa_mode>` in text stripped of angle brackets so they don't read as unclosed tags; all real blocks balanced. (b) FABRICATION_SCAN (agents.md, ANON enforcement point) given v8C.3 exception so ANON won't veto SC/MCTS/RAPTOR — closes the do-no-harm loop at enforcement, not just db. (c) Contract Step 9 TARGET CONTEXT CHECK added (host≠target: target model, free/paid tier, live_specs limits, task-splitting via Chain/SCOPE.HELM). (d) `_art.md`→`!art.md` (on-demand convention, resolves dangling ref). (e) v8C.1→v8C.3 version drift cleaned across 34 files. (f) preloader STEP 5 now explicitly applies PILOT_MODE + SHERPA (closes declaration→activation loop; was: declared but never activated in startup flow). Backups: v8C.3_BACKUP_20260614-0215.zip (pre-sim) + re-zipped post-sim.
- 2026-06-14 — Step 3: 9D question-limit made PILOT-aware (co-pilot ≤5 + INTERACTIVE_CHOICE, auto-pilot ≤3, manual ≤1; PERSONA_HINT override) — !intent/intent_engine both distros.
- 2026-06-14 — Step 4: db COMBINATOR conflict matrix extended with 6 v8C.3 modules + Fabrication Banned List disambiguation (SC≠USC, MCTS≠ToT, RAPTOR≠GoT) so VECTOR won't veto own techniques — both distros.
- 2026-06-14 — Step 5a: schema fully unified — `trigger_keywords:` → `triggers:` (visual/writing/sandbox ×2). Only core/db (BASE) + teacher (command) now lack triggers, by design.
- 2026-06-14 — Step 5b: intent §2.5 MODULE HANDOFF table wires all 6 v8C.3 modules into the router hub (advisory under co-pilot, auto under manual) + contract→routing note — both distros.
- 2026-06-14 — SIM PASS 2 (task-solving sims, both envs): 6 scenarios traced (gen→improve, QUORUM, feedback-loop w/ screenshot, cross-model Gemini, FABRICATION false-positive, CONFLICT_RESOLVER). Found 1 real bug (already fixed: FABRICATION false-positive) + 2 gaps now closed: (a) PARALLEL_EXECUTION block added to agents.md (was documented in author's forum post but absent from prompt) — both distros; (b) screenshot→symptom intake added to debug Step 1 — both distros. Report: out\SIMULATION_REPORT.md.
- 2026-06-14 — Python consistency checker (out\p2p_consistency_check.py, stdlib-only, run on PC): cyrillic map + terminology desync + cross-distro. Result: ZERO real term desync (only SCOPE.HELM vs SCOPE_HELM = legit yaml-key), all key mechanics present in both distros. Outputs: consistency_report.md + translation_map.json.
- 2026-06-14 — Step 6 mostly done: index trees + banners→docs (MODES_GUIDE.md) RESOLVED. Only cowork English conversion remains (optional; cyrillic map in translation_map.json).
- 2026-06-14 — ENGLISH consistency / ANCHOR audit (new tool: out\p2p_english_consistency.py, per-distro, prefix-artifact filtered). Findings: anchors **0 broken** (1 real dangling fixed: `#DB_TASK_TYPE`→`task_type`+`#DB_DYNAMIC_WEIGHTING`, both distros), **perfect cross-distro parity** (fc-only=0/cw-only=0), **0 anchor spelling drift**, 69 orphan-defs = normal addressable db-registry anchors. Canonical terms: all present both distros. Synonym clusters (hook/handle/anchor, handoff/hand-off) = FALSE POSITIVES on context analysis (distinct legit concepts: React hooks, CC Hooks, marketing hook, UI handle, verb 'handle'; noun 'handoff' vs verb 'hand off' = correct grammar). → English is terminologically consistent; no "breaks-on-Sonnet" naming drift. Reports: english_consistency_report.md.
- 2026-06-16 — Fixes from user live-test screenshots (Cowork/Code env): (1) TEST-ACTIVATION — VERSION_COMPAT v8C3=on + all 6 MODULE_*=true (both distros) → [35-40] unlocked, "Active v8C.3 modules" populated. Public build may revert to off for token economy. (2) Fixed false "clickable" promise — PILOT toggle said "клик чтобы сменить" but a PROMPT outputs only TEXT; clickable UI is rendered by the host app, not prompt text. Toggle now "сменить → напиши: co-pilot/auto-pilot/manual"; INTERACTIVE_CHOICE rewritten honestly (numbered text, user types; no false env-clickable branch). Both distros.
- 2026-06-16 — TWO-STAGE START (UX, user request): /start now shows COMPACT start screen (logo + PILOT mode choice + "опиши задачу" / "full ui menu") instead of full 40-item wall. Full menu [1-40] shown only on `full ui menu` OR after mode pick (then ART banner if !art.md loaded). CRITICAL INVARIANT reworded: /start→compact, full ui menu→always-full. Updated core (STARTUP rule + menu→"ПОЛНОЕ МЕНЮ") + preloader STEP 5, both distros.
- 2026-06-16 — ALPHA start = ART GALLERY (user: testers should see banners incl. SHERPA first): /start → logo + ASCII banners of all 7 mode-arts from !art.md (CO-PILOT/AUTO-PILOT/MANUAL/SHERPA/QUORUM/SCOPE.HELM/EXPLORATION) + prompt; text fallback if !art.md absent. After mode pick → full menu [1-40] as before. !art.md now loads BY DEFAULT (alpha; prod can drop it → text fallback, zero tax). Both distros. Build: v8C.3_ALPHA_*.zip.
- 2026-06-16 — SIMPLIFIED to SINGLE menu (user: "не заморачивать, арты в full menu + буквы"): reverted two-stage start. Now /start = ONE screen: logo + art banners (if art.md loaded) + MODE row + full [1-40]. Modes pick by LETTER (C/A/M/S/Q/H/E) — separate space from menu action numbers [1-40] (no [1-7]↔[1-40] collision). INVARIANT: /start & full ui menu → full menu always. Both distros. Build: v8C.3_ALPHA_*.zip.
- (pending) ONLY cowork English instruction conversion (big, optional; cyrillic map ready).
