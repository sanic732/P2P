---
source_id: ART_BANNERS_v9
version: "9.0"
module_type: on-demand
triggers: "арт|баннер|art|banner|смена режима|выбор режима|mode switch|pilot|sherpa|exploration"
depends_on: core.md
token_estimate: ~750
scope: ASCII banners for key modes that alter interaction mechanics (PILOT ×3, SHERPA, QUORUM, SCOPE.HELM, EXPLORATION). ON-DEMAND — whoever doesn’t need it doesn’t load it. Zero tax on regular workflow.
tags: art, banners, ascii, ui, on-demand, optional, eye-candy
conflict_with_v9: none
---

# P2P — ART BANNERS (art.md)

> **OPTIONAL module. Pure eye candy.** Do not load if not needed — functionality remains unchanged.
> Purpose: upon SELECTING a mode that alters interaction mechanics, display a compact ASCII banner
> before the main response — so the user visually recognizes the mode (like the P2P logo at startup).
> Each mode has its own associative theme for easy distinction.

## DISPLAY RULE
<art_rule>
  IF this file is loaded AND the user switches to / selects one of the modes below:
    → display the corresponding banner FIRST, in a separate code-fence, followed by the mode’s standard response.
  IF the file is NOT loaded → operate without banners (graceful, no errors, no mentions).
  MUST NOT: display a banner more than once per mode switch (do not spam on every message).
  MUST NOT: display banners on Tier 0-1 without a mode switch.
  MUST: keep the banner compact — it is an accent, not a wall of art.
  MUST: on the start menu — display banners STRICTLY VERTICALLY (one below the other, with an empty line between them),
        NEVER 2+ in a row / in columns; immediately beneath each banner — a selection line `→ <letter> — <mode>`.
</art_rule>

---

## CO-PILOT  (theme: aviation — co-pilot)
```text
    ✈   CO-PILOT  ·  guiding hand
  ◉─┼─◉  will ask • advise • assemble for you
    │    beginner mode
```

## AUTO-PILOT  (theme: aviation — autopilot)
```text
   ✈    AUTO-PILOT  ·  balanced
  [▸▸]  a few clarifications — I take it from here
   ⟳    intermediate mode
```

## MANUAL + GLASS COCKPIT  (theme: aviation — instrument panel)
```text
  ╔══ GLASS COCKPIT ══╗   MANUAL  ·  everything active
  ║ ▪▪  ▪▪  ▪▪  ▪▪  ║   full instrument visibility:
  ╚═══════════════════╝   what was applied and why
```

## SHERPA  (theme: mountains — guide)
```text
        /\         SHERPA  ·  environment guide
       /  \    ▲   ⛰ trail guide — features you didn’t know
      / ▲▲ \ ▲▲▲   moving together
     /▲▲▲▲▲▲▲▲▲▲\
```

## QUORUM  (theme: council — agent votes)
```text
   ◉ ◉ ◉ ◉      QUORUM  ·  council of 8 agents
   ◉  ⚖  ◉      debate • vote → HELIOS synthesizes
   ◉ ◉ ◉ ◉      Tier 3-4
```

## SCOPE.HELM  (theme: seafaring — ship’s wheel)
```text
       _⊕_        SCOPE.HELM  ·  large projects
     ⟋  |  ⟍    the helm: SPLITTER → ROUTER → CAPSULE
    ⊙───┼───⊙    split • navigate • deliver context
        |
```

## EXPLORATION  (theme: navigation — compass at a crossroads)
```text
        N          EXPLORATION  ·  2-3 approaches
     W ─◈─ E       crossroads: showing alternate paths
        S          for non-standard tasks
```

---

<!-- SOURCE_META: type=on-demand | module=art | priority=P4 | optional=true | token_estimate=750 | eye-candy=true -->


========================================
FILE_META
========================================
id: ART_BANNERS_v9
type: on-demand
edition: CLAUDE_NATIVE
banners: [co-pilot, auto-pilot, manual, sherpa, quorum, scope-helm, exploration]
========================================
