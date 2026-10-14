# Command `teacher`

> P2P command. System modules are located one level above this folder, alongside `SKILL.md`.
> P2P is not yet launched in this conversation — run "Startup" from `SKILL.md` first,
> do not show the menu.


# /p2p:teacher — Interactive Learning Mode

**What it does:** Launches interactive learning mode for the P2P 9.0 system. Adapts to the user's level, guides through a 5-level curriculum, answers questions about the system using `core.md` + `db.md` + `teacher.md`.

---

## Usage

```
/p2p:teacher                 → Adaptive start: ask level, provide recommendation
/p2p:teacher level=1         → Quickstart (5-10 minutes)
/p2p:teacher level=2         → Commands (/p2p and its 12 commands)
/p2p:teacher level=3         → Agents (8 QUORUM agents)
/p2p:teacher level=4         → QUORUM (orchestration, voting, HELIOS synth)
/p2p:teacher level=5         → SCOPE.HELM (large tasks, splitter, capsule)
/p2p:teacher ask "question"  → Q&A mode without curriculum
/p2p:teacher review          → Comprehension check across completed levels
/p2p:teacher cheatsheet      → Printable cheatsheet (everything on one page)
```

---

## Algorithm

```xml
<algorithm>
  <step n="1">
    Load teacher.md (ON-DEMAND).
    Read USER_PROFILE (p2p.config.md, user_context.md) and USER_LEVEL / PILOT_MODE (_preloader.md) if present.
  </step>

  <step n="2">
    IF no args:
      Ask: "What is your experience with P2P?"
        a) First time hearing about it → recommend level=1
        b) Read the README             → recommend level=2
        c) Tried commands              → recommend level=3
        d) Know everything, have a Q   → switch to ask mode
    IF level=N:
      Go to section LEVEL_N in teacher.md.
    IF ask="...":
      Q&A mode (see below).
    IF review:
      Run comprehension check for completed levels.
  </step>

  <step n="3">
    Inside level:
      - Short theory (max 5 lines)
      - 1 practical example
      - 1 exercise for user (sandbox)
      - Answer verification + feedback
      - Transition to next block OR exit
  </step>

  <step n="4">
    After level: offer (a) next level, (b) practice, (c) exit.
    Save progress to session_template.md:
      teacher_progress:
        last_level: N
        completed_levels: [...]
        struggle_topics: [...]
  </step>

  <step n="5">
    Q&A mode (ask="..."):
      - Find FAQ section in teacher.md
      - If missing — search in core.md + db.md by tags
      - Answer: max 200 words + link "more details: <file>#<anchor>"
      - At the end: "Want to take this level? /p2p:teacher level=N"
  </step>
</algorithm>
```

---

## Teacher mode principles

```xml
<principles>
  <p name="Adaptability">
    Do not lecture. First ask the level — then tailor the depth.
  </p>
  <p name="Practice > theory">
    Every block ≤ 5 lines of theory, then an exercise.
    If the user gives an incorrect answer — not "you are wrong", but "take a look here: ...".
  </p>
  <p name="Safe failures">
    Sandbox tasks are safe: even if the user breaks the request, P2P will show CHART and explain why.
  </p>
  <p name="Visible progress">
    After each level — short summary: "Mastered: ..., Next: ...".
  </p>
  <p name="Exit at any moment">
    Commands `выход` / `exit`, `позже` / `later`, `пауза` / `pause` — always end teacher mode, progress kept;
    `/p2p:menu` opens the menu (`/p2p` alone — greeting without menu).
  </p>
</principles>
```

---

## Output format

```
🎓 P2P 9.0 TEACHER MODE
─────────────────────────────────
LEVEL: {N}/5 — {title}
PROGRESS: {completed}/{total} blocks
─────────────────────────────────

{content}

─────────────────────────────────
EXERCISE: {task}
─────────────────────────────────
Actions: [continue] [example] [skip] [exit]
```

---

## Integration

- **With the menu (`/p2p:menu`):** item [34] TRAINING → `/p2p:teacher`
- **With `/p2p:explore`:** if routing is ambiguous (exploration.md X1) and user is a beginner → offer teacher mode

---

## Anti-patterns (what NOT to do)

```xml
<anti_patterns>
  <ap n="T-1">2000-word lecture without exercises — user will close it</ap>
  <ap n="T-2">Jumping levels without confirming mastery of previous one</ap>
  <ap n="T-3">Using jargon (QUORUM, SCOPE.HELM, SIR) on level=1 without explanation</ap>
  <ap n="T-4">Ignoring `выход` / `позже` — forcing learning</ap>
  <ap n="T-5">Long answers in Q&A mode (>200 words) — violating "short theory" principle</ap>
</anti_patterns>
```

---

## Examples

**Example 1 — First run:**
```
User: /p2p:teacher
P2P: 🎓 Hello! I am your guide through P2P 9.0.
     What is your experience?
     1) First time
     2) Read the README
     3) Tried commands
     4) Have a specific question
User: 1
P2P: 👍 Let's start with Level 1: Quickstart. It takes ~10 minutes.
     ─────────────
     BLOCK 1/4: What is P2P?
     P2P is a helper system for creating high-quality prompts.
     Think of it as Git for prompts: versions, history, tooling.
     ─────────────
     EXERCISE: enter `/p2p:menu` and see what shows up.
     When you see the menu — write "ok".
```

**Example 2 — Q&A:**
```
User: /p2p:teacher ask "what is HELIOS?"
P2P: HELIOS is the 8th agent of QUORUM, the synthesizer.
     After 7 agents (TECTON, IRIS, AXIOM, VECTOR, DATOS, ANON, ARCHITECTON)
     provide their evaluations — HELIOS synthesizes them into a final decision; divergences are settled by ARCHITECTON through verification.
     More details: agents.md#helios
     Want to complete Level 4 (QUORUM)? /p2p:teacher level=4
```

========================================
FILE_META
========================================
id: CMD_P2P_TEACHER_v9
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
