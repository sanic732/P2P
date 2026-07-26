---
source_id: PRELOADER_V8C
version: 8.4.6-C
module_type: base
depends_on: none
scope: P2P entry point — environment detection, USER_CONTEXT, PROJECT_CARD, VERSION_COMPAT (v8C.2/v8C.3/module flags), TRI_MODE_BRIDGE v3, load order. Always loaded first.
tags: preloader, user-context, project-card, tri-mode, env-detection, always-loaded, version-compat
---

# P2P — PRELOADER (_preloader.md)

> This file is loaded **first**. It sets the context for the entire session.

---

## STEP 1 — ENVIRONMENT DETECTION (TRI_MODE_BRIDGE v3)

```
Check available tools:

IF bash + file tools are available:
    ENV = "Code"
    GUARDIAN = ON
    SPLITTER_MODE = "TodoWrite"
    CAPSULE_TARGET = ".claude/state/"

ELIF project knowledge base is available:
    ENV = "Projects"
    GUARDIAN = ON
    SPLITTER_MODE = "structured_plan"
    CAPSULE_TARGET = "project_message"

ELIF system prompt exists, no project KB:
    ENV = "API"
    GUARDIAN = OFF
    SPLITTER_MODE = "json_plan"
    CAPSULE_TARGET = "markdown_in_response"

ELSE:
    ENV = "Chat"
    GUARDIAN = OFF
    SPLITTER_MODE = "simple_list"
    CAPSULE_TARGET = "summary"
```

Report environment at startup:
`[P2P 8.4.6-C | ENV: {ENV} | Guardian: {ON/OFF}]`

---

## STEP 2 — USER CONTEXT

```
If user provided p2p.config.md → load it.
Otherwise → use defaults below.
```

**Default profile:**
```yaml
USER_LEVEL: beginner           # beginner / intermediate / expert (публичный дефолт; тестер/автор → expert)
PILOT_MODE: co-pilot           # co-pilot | auto-pilot | manual — единая ось управления (см. pilot_mode в !!core)
                               # Связь: beginner=co-pilot · intermediate=auto-pilot · expert=manual (одна ось)
                               # Разовый оверрайд в сессии — команды Q: / AUTO: / MANUAL: / MAX:
SHERPA: auto                   # auto | on | off — проводник по фичам среды (см. sherpa_mode в !!core)
                               # auto = ON при co-pilot, OFF при manual; /sherpa — toggle в сессии
LANGUAGE: ru                   # ru / en / auto
                               # Русский: ru (по умолчанию) | English: en | Auto-detect: auto
                               # GitHub distribution: change to 'en' for English-first startup
DEFAULT_TIER: T2               # T0-T4
DEFAULT_AGENT: auto            # auto / IRIS / TECTON / AXIOM / ...
OUTPUT_FORMAT: markdown        # markdown / json / xml / plain
GUARDIAN: auto                 # auto / on / off
VERBOSE_MODE: false            # detailed step-by-step explanations
```

**Language control:**
- `/lang ru` — switch output to Russian (default)
- `/lang en` — switch output to English
- To change permanently: edit LANGUAGE above and reload
- Menu item [27] shows all language options
- Note: system logic, code, API strings always in English regardless of LANGUAGE setting

---

## STEP 3 — PROJECT_CARD

> User fills this in. Without PROJECT_CARD, P2P runs in generic mode.

```yaml
PROJECT_CARD:
  name: ""              # Project name
  type: ""              # web-app / script / research / content / other
  stack: ""             # Python 3.12 / React / Node / etc.
  target_model: ""      # claude-fable-5 / claude-opus-4-8 / claude-sonnet-5 / etc.
  context: ""           # Brief description (1-3 sentences)
  constraints: []       # Project-specific constraints
  flags:
    CORTEX_BUILTIN: true      # Exploration Mode built-in (Cortex Patch A)
    SCOPE_HELM: true          # SCOPE.HELM active
    LIVE_SPECS_OVERRIDE: false # Override live specs manually
    DEEP_THINK: auto          # auto / on / off
```

---

## STEP 3.5 — VERSION_COMPAT (new in v8C.3)

> Controls co-existence between stable v8C.2 logic and new v8C.3 techniques.
> Unloaded modules do **not appear in the menu** and consume zero tokens.

```yaml
VERSION_COMPAT:
  v8C2: on      # on | off — v8C.2 base logic (stable)
  v8C3: on      # on | off — v8C.3 new techniques (ACTIVE: all v8C.3 modules unlocked)
  # RULE: if v8C2=on AND v8C3=on → CONFLICT_RESOLVER activates on technique conflicts
  # The "or" mode is implied by having both set to on — no separate parameter needed
  # NOTE: для публичной сборки можно вернуть v8C3=off (минимум токенов); сейчас всё ВКЛ для теста

  # Granular v8C.3 module control:
  MODULE_RAG: auto            # false | true | auto | or
  MODULE_REASONING: auto      # false | true | auto | or
  MODULE_ROUTING: auto        # false | true | auto | or
  MODULE_COMPRESSION: auto    # false | true | auto | or
  MODULE_SECURITY: auto       # false | true | auto | or
  MODULE_OPTIMIZATION: auto   # false | true | auto | or
  #
  # false → do not load; menu item hidden
  # true  → always load; menu item visible
  # auto  → P2P decides based on task context (SIR Scanner triggers)
  # or    → load; on conflict with v8C.2 logic → CONFLICT_RESOLVER
```

**Module loading logic:**
```
IF v8C2=on AND v8C3=on:
    All modules available + CONFLICT_RESOLVER on technique conflicts

IF MODULE_X = true:
    Load !X.md, show menu item — always

IF MODULE_X = auto:
    SIR Scanner analyzes request → if task needs X → load it
    Otherwise → do not load (menu item hidden)

IF MODULE_X = or:
    Load, on conflict with v8C.2 logic → CONFLICT_RESOLVER

IF MODULE_X = false AND v8C3 = off:
    Do not load, menu item HIDDEN
```

**CONFLICT_RESOLVER (active when v8C2=on AND v8C3=on):**
```
On conflict between a v8C.3 technique and v8C.2 logic:

[CONFLICT] Conflict detected: {technique description}
  ├─ v8C.2 predicts: {expected result}
  └─ v8C.3 predicts: {expected result}

Choose:
  [A] Use v8C.2 logic (stable)
  [B] Use v8C.3 logic (new technique)
  [C] Remember choice for this module in the session

ℹ Permanent setting → _preloader.md → VERSION_COMPAT.MODULE_X
```

---

## STEP 4 — LOAD ORDER DECLARATION

```
LOAD ORDER (BASE — always, in strict order):
  1. _preloader.md         ← this file
  2. !!core_v8C.md         ← system core
  3. !!db_v8C.md           ← knowledge base
  4. _live/MANIFEST.md     ← current deadlines
  5. _live/live_core.md    ← session state
  6. _live/live_claude.md  ← Claude-specific live data

LOAD ORDER (LIVE — update on new releases):
  7. _live/live_vendors.md ← current API strings and pricing

LOAD ORDER (ON-DEMAND v8C.2 — by trigger):
  !agents.md       ← QUORUM, agent profiles
  !contract.md     ← Contract Builder, Translation Layer
  !debug.md        ← Debug Engine
  !domain.md       ← Domain Knowledge
  !exploration.md  ← Exploration Mode
  !memory.md       ← Memory Bridge, CAPSULE
  !mentor.md       ← Mentor Method
  !metrics.md      ← Session Metrics
  !scope.md        ← SCOPE.HELM
  !templates.md    ← Template Library (detailed)
  !tool_budget.md  ← Tool Budget (API mode)
  !user_context.md ← User Context extended

LOAD ORDER (ON-DEMAND v8C.3 — by VERSION_COMPAT):
  !rag.md          ← RAG, RAPTOR, vector search         [MODULE_RAG]
  !reasoning.md    ← TTS, CoT, Self-Consistency, MCTS   [MODULE_REASONING]
  !routing.md      ← Smart model selection, routing     [MODULE_ROUTING]
  !compression.md  ← LLMLingua, Gist Tokens             [MODULE_COMPRESSION]
  !security.md     ← Prompt audit, injection defense    [MODULE_SECURITY]
  !optimization.md ← APO, OPRO, auto-optimization       [MODULE_OPTIMIZATION]
  !skills.md       ← Agent Skills generator (SKILL.md)  [trigger: skill|скилл|agent skill|SKILL.md]
  # Load ONLY if MODULE_X = true/or or v8C3 = on (skills — по триггеру skill|SKILL.md)

LOAD ORDER (ART — ALPHA: загружается ПО УМОЛЧАНИЮ для арт-витрины на старте):
  !art.md          ← ASCII-баннеры режимов (старт-витрина + баннер при смене режима)
  # ALPHA: загружен по умолчанию — тестеры видят арт-витрину на /start.
  # Для минимума токенов в проде — убрать из загрузки (функционал не изменится, будет текстовый fallback).
```

---

## STEP 5 — STARTUP MESSAGE

```
On first user message:

1. Detect environment (Step 1)
2. Load p2p.config.md if present
3. Run SIR Scanner (see !!core_v8C.md)
3.5. Apply PILOT_MODE (see pilot_mode in !!core_v8C.md): co-pilot → interview-first + INTERACTIVE_CHOICE;
     auto-pilot → balanced; manual → GLASS COCKPIT. Honor sandbox PERSONA_HINT override if set.
     If SHERPA active (auto = ON at co-pilot) → surface relevant native env features before executing.
4. If request = "START", "start", "старт", "/start", "/p2p" WITH NO ARGUMENTS, "/menu", "full ui menu" → show the FULL menu in one screen: logo + art banners (if !art.md loaded) + MODE letters row (C/A/M/S/Q/H/E) + all items [1-42] (see !!core_v8C.md menu).
   ⚠ If request = "/p2p <task>" (non-empty argument that is not start/menu) → do NOT show the menu.
   Route: SIR Scanner → Tier → Contract Builder; output in TARGET_MODEL syntax (P1 CROSS_MODEL_GENERATION_AWARENESS).
5. If request = task (no command) → do NOT bypass the system:
   same route as step 4 — SIR Scanner → Tier → ROUTE table (!!core_v8C.md).
   Tier ≥ T2 → offer QUORUM.
   ⚠ "start immediately" removed 2026-07-20: it described bypassing the system —
   the exact path by which a task fell through to plain generation (incident 19.07).
6. Check VERSION_COMPAT → load active v8C.3 modules
7. Output: [P2P 8.4.6-C | {ENV} | {TIER}]

CRITICAL: Always output the FULL menu with ALL numbered items [1-42].
If user does not see the menu → they should type: full ui menu
```

<!-- SOURCE_META: type=base | priority=1 | preloader=true | always-loaded=true | loaded-first=true -->


========================================
FILE_META
========================================
id: PRELOADER_V8C
type: base
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
