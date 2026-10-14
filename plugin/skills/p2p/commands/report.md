# /p2p:report — anonymized report to the P2P author

**What it does:** gathers a short report from this session on how P2P performed — without any content of your work.
Menu item [19].

**What is included (only facts about P2P):**
- environment (Code / API / Projects / Chat — TRI_MODE_BRIDGE), help mode;
- which features and commands were triggered;
- routes: INTENT → Tier → where the request went;
- target models (id);
- where P2P made a mistake or you corrected it — in one line: flaws of the prompt by the anti-pattern letters A–P
  (core.md), errors of execution by E-A…E-P (debug.md);
- your rating 1–5 and a few words, if you wish.

**What is NOT in the report and never can be:** text of requests, prompts, and files; names of people, projects, and companies;
paths, addresses, keys, and passwords.

**Procedure:**
1. Assemble the report now, from this conversation only: look back at what worked well, what did not and where P2P
   erred (features, route, target model, error type). Nothing was recorded in advance.
2. Ask for a rating 1–5 and a comment; an answer of "skip" means a report without them.
3. Show the report IN FULL in a single code block — the user sees everything that will go to the author.
   The report itself is ALWAYS in English, whatever OUTPUT_LANG is (the user’s comment translated into English);
   the questions and explanations around it stay in OUTPUT_LANG.
4. State where to send it: an issue in the P2P repository on GitHub (the repository link is in the plugin’s
   README). Only the user sends it; P2P itself never sends anything anywhere.

**Format:**
```
P2P_REPORT v1 · P2P 9.0 · <date> · env: <environment> · mode: <mode>
features: <comma-separated features>
routes: <INTENT/Tier → route; …>
targets: <model ids>
issues: <A–P or E-A…E-P: one line; …> | none
rating: <1–5 | —> · comment: <user’s words | —>
```

========================================
FILE_META
========================================
id: CMD_REPORT_v9
type: command
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
