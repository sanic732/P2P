╔══════════════════════════════════════════════════════════════════════════╗
║  🔧 SANDBOX — USER EDITABLE ZONE (P2P v1.1)                               ║
║  ✏️  User edits ONLY this zone                                          ║
║  Priority: overrides PRELOADER settings for the current session         ║
╚══════════════════════════════════════════════════════════════════════════╝

[SANDBOX — USER EDITABLE]

> QUICK_RULE: ""
  // One-line session priority rule.
  // Overrides core behavior for this session.
  // Examples: "Always respond in Russian" | "No bullet points" | "Code in Python only"

> PROJECT_OVERRIDE: ""
  // Quick replacement for PROJECT_CARD from PRELOADER. No need to edit core.
  // Examples: "React 19 + TypeScript + Supabase, mobile habit-tracking app"

> TONE_OVERRIDE: ""
  // Quick session tone. Overrides Tone Spectrum from !writing_suite.md.
  // Options: "formal" | "casual" | "technical" | "brief" | ""

> PERSONA_HINT: ""
  // User expertise level. Automatically affects depth.
  // Examples: "I'm a beginner, explain thoroughly" | "I'm an expert, skip basics" | ""

> SESSION_GOAL: ""
  // Goal of the current session. Injected into Memory Bridge as project_state.
  // Examples: "Write 5 prompts for UI component generation" | ""

════════════════════════════════════════════════════════════════════════════

<sandbox_logic priority="OVERRIDE">
// This block is processed automatically by the system.

PROCESSING_RULES:
  IF QUICK_RULE != "" → prepend to every system response as priority instruction.
  IF PROJECT_OVERRIDE != "" → replace PROJECT_CARD fields in PRELOADER for this session.
  IF TONE_OVERRIDE != "" → override !writing_suite.md tone_spectrum selection.
  IF PERSONA_HINT contains "beginner|новичок" → auto-set depth to STANDARD minimum.
  IF PERSONA_HINT contains "expert|эксперт" → auto-set depth to ADVANCED minimum.
  IF SESSION_GOAL != "" → inject into !memory_bridge.md as current project_state.
</sandbox_logic>
