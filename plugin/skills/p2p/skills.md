---
source_id: skills_generator_v9
version: "9.0"
type: ON_DEMAND
priority: 3
edition: CLAUDE_NATIVE
depends_on: "core.md, _preloader.md"
trigger: "skill|скилл|agent skill|create skill|создай скилл|SKILL.md|навык агента"
tags: agent-skills, skill-md, generator, agentskills-io, progressive-disclosure
---

// ═══════════════════════════════════════════════════════
// P2P — skills.md — AGENT SKILLS GENERATOR (agentskills.io standard)
// P2P generates an Agent Skill as an ARTIFACT (folder <name>/SKILL.md + optional resources)
//     that the user puts into Grok (~/.grok/skills/), Claude, Cursor or Codex.
// EN: Generates a portable Agent Skill artifact per the agentskills.io open standard.
// NOTE: this is artifact GENERATION, NOT plugin installation. Following the !grok_heavy pattern (offer + generator).
// ═══════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────
// §A. SKILL_OFFER — when to offer skill generation
// ─────────────────────────────────────────────────────
SKILL_OFFER:
  TRIGGER: query contains "создай скилл | create skill | agent skill | SKILL.md | навык агента |
           оформи это как скилл | сделай переиспользуемый навык".
  ACTION (once, not silently):
    EMIT: "🧩 Build an Agent Skill (agentskills.io standard)? Choose:
      [1] Minimal SKILL.md (frontmatter + body only)
      [2] SKILL.md + resources (scripts/ references/ assets/)
      [3] Show template and description validator rules"
  DISCOVERY_RULE: a skill makes sense ONLY for things the model does NOT know (domain processes,
                  runbooks, specific workflows). Well-known common knowledge → do not package into a skill.

// ─────────────────────────────────────────────────────
// §B. SKILL_MD_CONTRACT — SKILL.md file rules
// ─────────────────────────────────────────────────────
SKILL_MD_CONTRACT:

  // ── B.1 FRONTMATTER (YAML) ──
  FRONTMATTER:
    name:         2–64 chars; only [a-z0-9-]; do NOT start/end with a hyphen; no "--".
                  FOLDER == name (exact match).
    description:  ≤1024 chars per agentskills.io; for upload to claude.ai — ≤200 chars (a rule for the skills P2P
                  generates; the skills of this plugin follow the Claude Code plugin limits);
                  NO quotes and no ": " inside; imperative mood;
                  "WHAT it does + WHEN to use" + trigger words/contexts.
    // Only these two fields are required (metadata ~100 tokens — always in context).
    // Outside Claude Code (upload to claude.ai, Skills API) ONLY the following are allowed: name, description,
    // license, compatibility, metadata, allowed-tools. Any other field crashes the upload
    // with the error "Unexpected key(s) in SKILL.md frontmatter". Put custom data in metadata.

  // ── B.2 BODY (Markdown, ≤500 lines) ──
  BODY:
    STYLE:    imperative mood; checklists; examples; error handling (Gotchas); output templates.
    PATTERN:  Plan → Validation → Execution; validation loops.
    LINKS:    link to resources via relative paths: scripts/extract.py, references/api.md.
    LIMIT:    keep ≤500 lines; move extensive material to references/.

  // ── B.3 PROGRESSIVE DISCLOSURE (3 levels) ──
  DISCLOSURE:
    1. metadata (name+description) — always in context (~100 tokens).
    2. full SKILL.md — loaded upon skill activation.
    3. resources (scripts/ references/ assets/) — loaded on demand.

  // ── B.4 STRUCTURE (folder) ──
  STRUCTURE:
```
<name>/
├── SKILL.md          # required: frontmatter + instructions
├── scripts/          # optional: recurring executable code
├── references/       # optional: detailed docs/schemas/API errors (loaded on demand)
└── assets/           # optional: templates, images, boilerplate
```

// ─────────────────────────────────────────────────────
// §C. DESCRIPTION_VALIDATOR — triggering reliability (sole trigger during discovery)
// ─────────────────────────────────────────────────────
DESCRIPTION_VALIDATOR:
  FORMULA: "[What it does]. Use when [contexts/intentions]. Include even if the user
            did not mention [key terms]."
  PRINCIPLES: imperative mood; focus on user INTENT (not on mechanics); "pushy" (explicit contexts);
              keywords + variations; concise 1–4 sentences.
  EVAL (checklist before output):
    - compile eval_queries: 8–10 positive + 8–10 negative near-miss.
    - run each ≥3 times → trigger_rate.
    - THRESHOLD: positive ≥0.5–0.7 ; negative <0.3. If failing → rewrite description.
  NEAR_MISS_EXAMPLE (PDF skill): positive "извлеки таблицы из PDF" · negative "отредактируй текст внутри PDF".

// ─────────────────────────────────────────────────────
// §D. ANTI_PATTERNS (from the agentskills.io guide)
// ─────────────────────────────────────────────────────
ANTI_PATTERNS:
  - Do NOT duplicate knowledge the model already has.
  - Triggers belong ONLY in description, NOT in the SKILL.md body.
  - Do NOT create README.md / CHANGELOG.md etc. inside the skill.
  - Do NOT make deeply nested references.
  - Do NOT exceed 500 lines in SKILL.md.
  - Do NOT use quotes and ": " in description.
  - Do NOT make descriptions too broad or too narrow.
  - One skill = one coherent task (scoping based on real-world experience: runbooks/errors/patches).

// ─────────────────────────────────────────────────────
// §E. TARGETS — where the artifact goes (unified standard)
// ─────────────────────────────────────────────────────
TARGETS:
  Grok:   ~/.grok/skills/<name>/  (persistent, preserved across sessions).
          init:     bash ~/.grok/skills/skill-creator/scripts/init-skill.sh <name> <dir> --resources scripts,references,assets
          validate: bash ~/.grok/skills/skill-creator/scripts/validate-skill.sh <dir>/<name>
  Claude: Claude Code — .claude/skills/<name>/ (project) or ~/.claude/skills/<name>/ (personal);
          plugin — skills/<name>/; claude.ai — ZIP with <name>/ folder at the root:
          Customize → Skills → Upload a skill (requires Code execution).
  Cursor: project rules/skills — same SKILL.md standard.
  Codex:  same SKILL.md standard.
  // SKILL.md format is identical across all targets (agentskills.io) — portable without changes.

// ─────────────────────────────────────────────────────
// §F. GENERATOR — step-by-step output
// ─────────────────────────────────────────────────────
GENERATOR:
  STEP_1: clarify the skill's task + intended target (Grok/Claude/Cursor/Codex).
  STEP_2: generate name (a-z0-9-, ==folder) + description (via §C formula and validator).
  STEP_3: assemble the SKILL.md body (§B: imperative mood, checklists, Gotchas, output templates, ≤500 lines).
  STEP_4: if [2] — propose scripts/ references/ assets/ (only what is necessary; §D anti-patterns).
  STEP_5: run DESCRIPTION_VALIDATOR (§C) → show trigger_rate assessment.
  STEP_6: output artifact as a file tree (SKILL.md + resources), ready to be placed in TARGET.
  OUTPUT: clean SKILL.md (frontmatter + body); do NOT add README/CHANGELOG.

FILE_META:
  STANDARD:    agentskills.io (specification + best-practices + optimizing-descriptions)
  COMPATIBLE:  core.md | _preloader.md | _index.md
  MENU:        [42] — no separate command
// EOF_MARKER_SKILLS_V9_VALIDATED
