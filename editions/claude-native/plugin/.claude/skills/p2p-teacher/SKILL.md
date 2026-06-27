---
name: p2p-teacher
description: Interactive teaching mode for P2P v8C.3 meta-prompt system. Use when the user wants to learn P2P, asks "how do I use P2P", "explain P2P to me", "научи меня P2P", "как пользоваться P2P", "не понимаю как работает", "как использовать систему", "что умеет P2P", "научи использовать", or any natural-language request to onboard, train, or get guided through the P2P system. Triggers a 5-level curriculum (Quickstart → Commands → Agents → QUORUM → SCOPE.HELM) with exercises, sandbox tasks, and Q&A mode. Not for generating prompts (use /p2p) or for QUORUM analysis (use /p2p-quorum).
source_id: SKILL_P2P_TEACHER
version: v8C.3-ALPHA
module_type: skill
last_updated: 2026-06-12
tags: skill, teacher, onboarding, curriculum, interactive, learning
---

# P2P TEACHER SKILL

**Skill:** P2P v8C.3 Interactive Teacher
**Version:** v8C.3-ALPHA
**Platform:** Claude (Opus 4.7 / Sonnet 4.6)
**Entry point:** `/p2p-teacher` command
**Knowledge base:** `teacher.md` (ON-DEMAND module)

---

## When to invoke

Trigger this skill when the user says (in any language):
- "научи меня P2P" / "teach me P2P"
- "как пользоваться" / "how do I use"
- "не понимаю как работает" / "I don't get how this works"
- "что такое QUORUM?" / "what is QUORUM?"
- "объясни систему" / "explain the system"
- "помоги разобраться" / "help me figure out"
- "с чего начать" / "where to start"

## What happens

1. Load `teacher.md` ON-DEMAND module
2. Detect user level (ask 1 question if unknown)
3. Route to appropriate Level (1-5) OR Q&A mode
4. Run interactive blocks with exercises
5. Track progress in `_live/live_core.md` (`teacher_progress`)

## Curriculum levels

| Level | Title | Time | Prereq |
|-------|-------|------|--------|
| 1 | Quickstart | 10 min | none |
| 2 | Commands (11 /p2p-*) | 20 min | Level 1 |
| 3 | Agents (8 QUORUM) | 30 min | Level 2 |
| 4 | QUORUM Orchestration | 30 min | Level 3 |
| 5 | SCOPE.HELM (Big Tasks) | 45 min | Level 4 |

## Commands

- `/p2p-teacher` — adaptive start
- `/p2p-teacher level=N` — jump to level
- `/p2p-teacher ask "..."` — Q&A
- `/p2p-teacher review` — comprehension check
- `/p2p-teacher cheatsheet` — printable summary

## Not for

- Generating prompts → use `/p2p`
- Running QUORUM → use `/p2p-quorum`
- Large task decomposition → use `/p2p-scope`
- Discovering brand voice → use `brand-voice:discover-brand`


========================================
VERSION_METADATA
========================================
id: SKILL_P2P_TEACHER
version: v8C.3-ALPHA
type: skill
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
