# /p2p:lang — the language P2P talks to you in

**What it does:** sets OUTPUT_LANG — the language of menus, statuses, questions and explanations. Any language of the
world works: Claude reads and writes them all.

**How to type:**
- `/p2p:lang <language>` — a name in any language or a code: `/p2p:lang español`, `/p2p:lang Deutsch`,
  `/p2p:lang uk`, `/p2p:lang 日本語`, `/p2p:lang pt-BR`.
- `/p2p:lang auto` — back to the default: the language of your own words in this conversation.
- `/p2p:lang` without an argument — show the current language.
- Without the plugin (Skill, file version): `lang <language>` or `/lang <language>`.

**Steps:**
1. Read the argument. A name or code that names a real language → OUTPUT_LANG = that language, in its usual form
   (a code becomes the language name: `uk` → Ukrainian). `auto` → OUTPUT_LANG = auto.
2. Unclear argument (two languages fit, or not a language) → ask once, offering the likely choices; do not guess.
3. Confirm in ONE line in the new language: `[P2P 9.0] Language: <language>` — no menu, no extra text.
4. From here on, everything user-facing is in OUTPUT_LANG. The setting lasts for this conversation and wins over the
   plugin setting `language` and over `p2p.config.md`.

**What does not change:**
- System logic, anchors `#DB_*`, code, API strings — English, as always.
- Generated prompts follow the language of the request (core.md, /lang HANDLER); ask for another language explicitly
  if the target model should get the prompt in a different one.
- `/p2p:report` is always written in English, whatever OUTPUT_LANG is.

MUST: accept any real language, by name or code. MUST NOT: refuse a language that is not Russian or English.
MUST: confirm in the chosen language. MUST NOT: show the menu after switching.

========================================
FILE_META
========================================
id: CMD_LANG_v9
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
