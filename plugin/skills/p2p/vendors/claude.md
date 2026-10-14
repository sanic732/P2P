---
source_id: vendor_claude_v9
version: "9.0"
type: VENDOR_PROFILE
vendor: claude
priority: REFERENCE
compatible_with: "db.md | live_specs.md (optional, attached by the user)"
---

// P2P 9.0 — VENDOR: CLAUDE (Anthropic) — prompting profile. Specs, prices, statuses: live_specs.md
// MODEL_REGISTRY. PRIORITY: an attached live_specs.md > this file.

// Source: docs.anthropic.com / anthropic.com/news.

KNOWN_ISSUES:
  G6: new tokenizer on current Claude models (versions: live_specs.md): increased tokens vs earlier models, by design;
      count with the official Token Counting API (all active models); cost-sensitive → earlier Claude generation (versions: live_specs.md).
  G7: 400 on non-default temperature / top_p / top_k on current Claude models (versions: live_specs.md) (with or without thinking); prefill → 400 on current Claude models (versions: live_specs.md);
      forced tool_choice → 400 on the flagship / balanced / agentic Claude models (exact id: live_specs.md). Full list: live_specs.md G7.
  G8: recall differences across generations → earlier Claude models (versions: live_specs.md) for large recall.
  PINNED EARLIER MODEL (G6 / G8): the current-lineup payload does not carry over. The oldest generations do not accept
      thinking {"type":"adaptive"}, some of them not output_config.effort either — omit what the pinned model does not
      accept (thinking is off by default there); per model: live_specs.md. Never send the current payload unchecked.
  budget_tokens: removed (400 on current Claude models (versions: live_specs.md)) → thinking {"type":"adaptive"}, effort low | medium | high | xhigh | max.
  cache TTL (Claude Code too) → ephemeral block on the stable prefix.
  Classifiers: false positives on security / coding / biology (FABLE5_CLASSIFIER_FALSE_POSITIVES) — legitimacy frame; refusals before output are billed.

CLAUDE_5X:  // contracts — what each model accepts
  FLAGSHIP (the flagship Claude model (exact id: live_specs.md), PRIMARY): thinking always on (disabled / enabled → 400; no thinking-off path); default effort
    MEDIUM — set it; tool_choice any / tool → 400; computer use only computer_toolset (legacy toolset → 400 on the
    Claude API and Google Cloud); edited or dropped thinking blocks → 400. Fallback only to the agentic Claude model (exact id: live_specs.md) (keeps thinking).
    Role: T3-T4 general / complex agentic, code, webdev (max).
  BALANCED (the balanced Claude model (exact id: live_specs.md), balanced): default effort high; thinking off = {"type":"between_tools"} at effort ≤ high, NOT
    "disabled" — then effort is fixed for the conversation (a per-message change → 400; vary effort → adaptive); tool_choice any / tool → 400; legacy computer toolset refused; thinking blocks of another account dropped silently. Role: T2-T3, budget path.
  AGENTIC (the agentic Claude model (exact id: live_specs.md)): tool_choice any / tool → 400 (strict tool use or structured outputs); thinking blocks bound to
    the exact history → append-only history.
    Role: explicit call for long-horizon agentic.
  FAST (the fast Claude model (exact id: live_specs.md), fast default): Adaptive thinking on by default — effort is the lever (low may skip thinking); thinking off =
    {"type":"disabled"} at effort ≤ high (xhigh / max → 400; effort then fixed for the conversation); budget_tokens → 400;
    forced tool_choice accepted, the reply starts with the tool call and has no thinking block; temperature / top_p / top_k
    and prefill → 400; computer use only computer_toolset; thinking blocks account-bound, append-only history;
    handle stop_reason "refusal" (no server-side fallback); Priority Tier not supported. Role: T0-T1, forced tool.

CLAUDE_5X_PROMPTING:  // prompt-writing levers and effort calibration per role
  ALL:
    - State desired output, constraints, sequential steps, and "above and beyond" depth explicitly → models follow instructions literally and do not infer unstated scope from vague prompts → [src: Anthropic prompting guide, all models: § Be clear and direct]
    - Explain the motivation or downstream constraint behind a rule → model generalizes better from why a behavior matters than from bare prohibitions → [src: Anthropic prompting guide, all models: § Add context to improve performance]
    - Wrap relevant, diverse multishot examples in `<examples><example>` tags → steers format, tone, and structure while distinguishing examples from instructions → [src: Anthropic prompting guide, all models: § Use examples effectively]
    - Separate instructions, context, and inputs with consistent hierarchical XML tags (`<instructions>`, `<context>`, `<documents><document>`) → reduces misinterpretation in complex prompts → [src: Anthropic prompting guide, all models: § Structure prompts with XML tags]
    - Set an explicit domain role in `system` → focuses behavior and tone for the use case → [src: Anthropic prompting guide, all models: § Give Claude a role]
    - Place long documents at the top of the prompt above instructions/query and require extracting `<quotes>` first → improves multi-document reasoning and grounds answers in source text → [src: Anthropic prompting guide, all models: § Long context prompting]
    - Request post-tool-use recaps explicitly when visibility is needed → current models are concise by default and often jump straight to the next action without verbal summaries → [src: Anthropic prompting guide, all models: § Communication style and verbosity]
    - State target format positively, wrap prose targets in descriptive XML tags, match prompt formatting style to desired output, or add `<avoid_excessive_markdown_and_bullet_points>` → positive framing and prompt style steer formatting more reliably than negative rules → [src: Anthropic prompting guide, all models: § Control the format of responses]
    - Instruct plain-text math with standard operators and forbid LaTeX/MathJax when plain text is needed → models default to LaTeX for mathematical and technical expressions → [src: Anthropic prompting guide, all models: § LaTeX output]
    - Use explicit action verbs or `<default_to_action>` vs `<do_not_act_before_instructions>`, and dial back `CRITICAL / MUST` tool-triggering language to normal phrasing → literal adherence means "suggest" only suggests, while aggressive language causes overtriggering → [src: Anthropic prompting guide, all models: § Tool usage]
    - Add `<use_parallel_tool_calls>` (or instruct sequential steps with pauses) → steers independent reads, searches, and commands to maximum concurrency or sequential stability → [src: Anthropic prompting guide, all models: § Optimize parallel tool calling]
    - Replace "If in doubt, use [tool]" with targeted conditions and instruct committing to one approach unless contradicted (or lower effort) → curbs excessive upfront exploration and repeated decision revisiting → [src: Anthropic prompting guide, all models: § Overthinking and excessive thoroughness]
    - Guide post-tool reflection and adaptive-thinking frequency with high-level goals rather than prescriptive step-by-step plans, and never ask to output reasoning in `<thinking>` or response text → models reason better natively, while requesting visible reasoning risks `reasoning_extraction` refusals → [src: Anthropic prompting guide, all models: § Leverage thinking & interleaved thinking capabilities]
    - Tell the model if context auto-compacts so it saves state instead of wrapping up early; track tests in structured JSON, notes in freeform text, and checkpoints in git, forbidding test removal → prevents premature wrap-up near context limits and maintains state across sessions → [src: Anthropic prompting guide, all models: § Long-horizon reasoning and state tracking]
    - Instruct taking local reversible actions freely but confirming before destructive, hard-to-reverse, or externally visible actions (without bypassing safety checks) → balances autonomy with safety on shared systems → [src: Anthropic prompting guide, all models: § Balancing autonomy and safety]
    - Define clear research success criteria and require tracking competing hypotheses, confidence levels, and cross-source verification in notes → drives methodical synthesis across large corpora → [src: Anthropic prompting guide, all models: § Research and information gathering]
    - Specify when to spawn subagents (parallel, isolated context) vs work directly (simple, sequential, single-file) → prevents wasteful subagent delegation where direct tool calls suffice → [src: Anthropic prompting guide, all models: § Subagent orchestration]
    - Instruct removing temporary iteration scripts at task end, add `<investigate_before_answering>` to require reading referenced files first, and forbid over-engineering or test-case hardcoding → keeps workspaces clean, prevents ungrounded code claims, and enforces general-purpose minimal solutions → [src: Anthropic prompting guide, all models: § Minimizing hallucinations in agentic coding]
    - Add `<frontend_aesthetics>` demanding distinctive typography, cohesive CSS variables, high-impact motion, and layered backgrounds while forbidding generic fonts and layouts → prevents convergence on generic "AI slop" frontend defaults → [src: Anthropic prompting guide, all models: § Frontend design]
  FLAGSHIP:
    - Calibrate effort starting at `medium`, test `low` for cost-sensitive coding, reserve `xhigh`/`max` for measured gains, and lower effort rather than prompting to think less → FLAGSHIP thinks more per turn at a given level than prior generations and matches prior high-effort work at `medium` → [src: Anthropic prompting guide, flagship: § Calibrate effort]
    - For latency-sensitive paths, use `low` effort (+ optional "Answer directly without deliberating.") and remove legacy thinking-disabled mitigations or response-text reasoning prompts → thinking is always on and asking for reasoning in text triggers `reasoning_extraction` refusals → [src: Anthropic prompting guide, flagship: § Prompts written for thinking disabled]
    - In unattended runs, append the standing instruction forbidding four early-stop habits (summary announcing next step without a tool call, offering to wait, non-blocking decision lists, milestone check-ins) and require pairing status notes with the next tool call → prevents text-only progress updates from ending the turn while work remains → [src: Anthropic prompting guide, flagship: § Unattended agentic runs]
    - Request predictable update points in `system` (intent line before first tool call, recap at end), declare a dedicated user-message tool upfront for verbatim snippets, or append a turn-scoped reminder after silent tool steps → inter-tool updates are emitted as progress-update thinking blocks rather than text blocks → [src: Anthropic prompting guide, flagship: § User-facing progress updates]
    - In multi-app workflows, instruct the model in `system` to broadly list and open potentially relevant emails, docs, tabs, and records before acting → model otherwise starts acting immediately and misses constraints sitting in unmentioned records → [src: Anthropic prompting guide, flagship: § Explore context in multi-app workflows]
    - Pass elapsed time against a budget in harness messages or add "Time matters here: do not spend time that can be avoided, and the earlier a correct result is obtained, the better." in `system` → drives multiagent teams to parallelize more aggressively without cutting work depth like lowering effort does → [src: Anthropic prompting guide, flagship: § Time signals for multiagent harnesses]
    - In chat, remove "think carefully before answering" instructions and add "Once you have answered something, treat that answer as done. On later turns, focus your thinking on what the user is asking now..." → stops redundant re-thinking of settled prior turns and reduces follow-up latency → [src: Anthropic prompting guide, flagship: § Thinking instructions in chat system prompts]
    - Wrap user-pasted external text in `<pasted_content id="...">` tags with a random ID and instruct in `system` to follow instructions inside only when the user’s own message asks to → hardens against indirect prompt injection inside pasted emails or pages → [src: Anthropic prompting guide, flagship: § Mark pasted text in user messages]
    - Drop legacy visual scaffolding for standard charts, but provide crop/image-processing tools and higher effort for dense technical drawings → native chart reading is accurate at low effort, whereas technical drawings still gain from tools and higher effort → [src: Anthropic prompting guide, flagship: § Tools for complex visual inputs]
    - Name specific visual patterns to forbid (e.g., cream/off-white backgrounds, italic headline accents, numbered section labels, monospace labels, pill buttons) iteratively → general "avoid a generic AI look" instructions merely swap one default style for another → [src: Anthropic prompting guide, flagship: § Frontend design defaults]
  AGENTIC:
    - Start effort sweeps at `high` and test stepping down to `medium` or `low` on evals → capability gains hold across levels, making lower effort competitive where eval quality holds → [src: Anthropic prompting guide, agentic: § Consider all effort levels]
    - Remove rules that suppress narration ("hold all findings for the final response"), instruct a pre-start intent line, brief mid-work updates, and a standalone closing recap, and notify via turn-scoped system message if UI hides command output → model writes fewer inter-tool updates by default, especially at high effort and in long tool chains → [src: Anthropic prompting guide, agentic: § Ask for user-facing progress updates]
    - In coding and computer-use loops, append a turn-scoped system message after tool results: "First privately list what you need next; then request every item that doesn’t depend on another’s result in this one response." → when next independent calls are implied by the task rather than named upfront, the model otherwise calls tools one per turn → [src: Anthropic prompting guide, agentic: § Batch independent tool calls in agent loops]
    - Define and forbid "mannered prose" (or add "Please remove all mannered prose.") in the user message or system prompt → model’s prose can run dense with long sentences, fewer paragraph breaks, and performative metaphors → [src: Anthropic prompting guide, agentic: § Writing density]
    - Remove legacy anti-markdown blocks or replace them with a rule allowing lists/bullets when content is multifaceted and plain prose in conversational exchanges → model naturally formats less, so anti-formatting prompts over-suppress needed structure → [src: Anthropic prompting guide, agentic: § Formatting in chat]
    - For source summarization, add a complete `<example>` (`<user>`, `<response>` with your tool name, `<rationale>`) demonstrating indirect speech with short marked quotes → model is otherwise prone to reproducing source wording without quotation marks → [src: Anthropic prompting guide, agentic: § Quoting retrieved sources]
    - Add the autonomous-operation prompt ("You are operating autonomously. The user is not watching in real time...") and scope-deliverable rules in `system` → stops the model from ending turns by announcing next steps ("I’ll...") or asking permission for reversible work already requested → [src: Anthropic prompting guide, agentic: § Finish the whole task]
    - For client-side compaction, instruct summarizing inside `<summary>` tags preserving six exact categories while keeping user words close to verbatim and condensing assistant reasoning to conclusions → prevents compaction from dropping constraints, ruled-out options, or hard-to-reconstruct details → [src: Anthropic prompting guide, agentic: § Tell the model what to preserve in compaction summaries]
    - Instruct reporting pre-existing bugs/optimizations as follow-ups rather than fixing them, implementing the most direct reading on ambiguity, and committing only requested or repo-standard focused tests → curbs unrequested nearby fixes and excess committed test files on open-ended tasks → [src: Anthropic prompting guide, agentic: § Keep changes and tests to what the task asks for]
    - At `low` effort, instruct in `system` that recognizing a name in a fast-moving domain is not knowing its current state and require searching the exact user-written name (or raise effort for that turn) → at `low` effort the model calls search/retrieval tools less often and answers from memory → [src: Anthropic prompting guide, agentic: § Search triggering at low effort]
    - Phrase compile checks as bug checks ("Are there any bugs in this program?"), supply docs for lesser-known languages, and keep base64 data out of tool outputs → reduces false-positive safeguard refusals on benign coding work → [src: Anthropic prompting guide, agentic: § Reduce safeguard false positives]
    - Append "The number of tokens used to edit files is best minimized, all else being equal. Therefore, when it will not affect the end result, try to surgically edit a file rather than rewrite the entire thing." → prevents whole-file rewrites on small or medium changes → [src: Anthropic prompting guide, agentic: § Prefer targeted edits over whole-file rewrites]
    - Run long-deliverable requests at `high` effort, or at `xhigh`/`max` append the user-message note explaining the shared token limit and instructing to use reasoning for structure/decisions rather than drafting the full deliverable twice → prevents full-draft duplication in thinking that hits `max_tokens` → [src: Anthropic prompting guide, agentic: § Leave room for long outputs at xhigh and max effort]
    - Provide a crop tool or image-processing container (PIL/OpenCV) for dense charts and visual inputs → enables iterative crop-and-zoom visual verification → [src: Anthropic prompting guide, agentic: § Give vision work tools to crop and zoom]
  BALANCED:
    - Start effort at `high` (default), use `medium` for well-specified agentic coding (`high` for harder/longer), and `low`/`medium` for latency-sensitive chat; lower effort rather than prompting to think less → from `medium` up the model thinks briefly before almost every reply (even greetings), whereas `low` skips thinking on simple requests → [src: Anthropic prompting guide, balanced: § Calibrate effort]
    - Add the carry-through + no-unrequested-additions prompt ("Keep working until everything the user asked for is done... Don’t add features, tests, files, docs or refactors..."), at `xhigh`/`max` forbid unrequested review rounds/reviewer subagents, and on open-ended idea requests forbid building until asked → at `low`/`medium` the model stops early to check in, while at higher effort it adds unrequested tests/files or launches reviewer subagents → [src: Anthropic prompting guide, balanced: § Steer initiative and scope]
    - Under `between_tools`, remove any instruction telling the model not to think, and switch to adaptive thinking for tool-free multi-step reasoning → "do not think" instructions under `between_tools` leak internal XML tags into visible output, and `between_tools` skips up-front thinking when no tools are called → [src: Anthropic prompting guide, balanced: § Running without up-front thinking]
    - For multi-step reasoning with JSON output, use adaptive thinking and append "Think the problem through before you answer." in `system` (or run at `xhigh` effort) → at `low`/`medium` effort the model often answers without thinking first, lowering accuracy when response text is constrained to JSON → [src: Anthropic prompting guide, balanced: § Reasoning tasks with JSON output]
    - Remove legacy "hold all findings for the final response" rules, specify update points in `system`, and cap turn-scoped silence reminders at two or three per turn → multi-sentence inter-tool notes become progress-update thinking blocks, and frequent post-tool harness text triggers prompt-injection suspicion → [src: Anthropic prompting guide, balanced: § User-facing progress updates]
    - Remove tool-discouraging phrases ("only use tools when strictly necessary", "minimize tool calls") and instruct in `system` to search for changeable specifics (allowed, required, charged) and gather current sources for reports → model otherwise answers from training knowledge on facts that have changed → [src: Anthropic prompting guide, balanced: § Tool use in chat and knowledge work]
    - Never place user text inside `tool_result` or in a system message right after `tool_result`; append mid-turn user words as a `user` text block after the last `tool_result`, put harness notices in a separate system message after user words, and omit custom per-step token countdowns → prevents indirect prompt-injection defenses from misreading genuine user input as spoofed tool output → [src: Anthropic prompting guide, balanced: § Mid-turn user messages]
    - At `low` effort on coding tasks, add the system paragraph requiring a real check (tests, type-checker, build, or command run, installing lockfile dependencies via project package manager without sudo) before reporting done → at `low` effort the model keeps thinking short and sometimes skips verification when dependencies are missing → [src: Anthropic prompting guide, balanced: § Verification on coding tasks]
    - Provide image crop/zoom or code-execution tools for dense charts (all effort levels) and technical drawings (`high` effort and up) → for charts, tools at `high` effort beat raising effort to `max` without tools at lower cost → [src: Anthropic prompting guide, balanced: § Tools for complex visual inputs]
  FAST:
    - Start effort at `medium` (default, including agentic coding), use `low` for chat and short tool tasks, `high` for longer agent tasks and strict instruction following, and check for empty visible replies at `xhigh` in multi-turn chat → prompt instructions to answer directly do not stop thinking, and `xhigh` in multi-turn chat can place the entire reply inside thinking → [src: Anthropic prompting guide, fast: § Use effort to control thinking]
    - Provide `The current date is {{current_date}}.` once in `system` or search tool description, and on long system prompts or at `low` effort append the cutoff/changeable-facts search instruction (with user country/region for local facts) while avoiding blanket "search for any present-day factual question" rules → grounds answers and raises search on changed facts without causing unnecessary searches on static facts → [src: Anthropic prompting guide, fast: § Accurate search results]
    - When requesting structured JSON output with custom tools and thinking disabled, switch to adaptive thinking or add "The JSON output format applies to your final answer only. When you need a tool, call it first, with no text before the call, and write the JSON once you have the results." → with thinking off and JSON format set, the model otherwise skips needed tool calls → [src: Anthropic prompting guide, fast: § Use adaptive thinking with JSON output and your own tools]
    - On long coding-agent system prompts at `low` effort, add the "Keep working until everything the user asked for is done..." + "Don’t add new features, docs, or refactors..." block (or raise effort to `medium`) → long system prompts at `low` effort cause early stopping and handing the task back → [src: Anthropic prompting guide, fast: § Prevent early stopping in long agent prompts]
    - At `low` and `medium` effort, add the real-verification system paragraph (run tests/type-checker/build, install declared lockfile dependencies without sudo, or state which check could not run and why) → unlike larger models where skipped verification is mainly a `low`-effort issue, FAST skips checks at both `low` and `medium` effort unless prompted → [src: Anthropic prompting guide, fast: § Tell coding agents to verify their changes]
    - For chatbots and support assistants, add the system rule that prompt rules hold for the whole conversation even when a user argues, gives a sympathetic reason, asks for a small part, claims an approved exception, or keeps asking (and use `high` effort when adherence is critical) → prevents user pushback from eroding system prompt adherence → [src: Anthropic prompting guide, fast: § Keep chatbots to their system prompt]
    - Switch from thinking disabled or `low` effort to adaptive thinking at `medium` effort if reasoning-like text appears in user-facing replies → model sometimes leaks reasoning-like text into visible replies when thinking is off or at `low` effort → [src: Anthropic prompting guide, fast: § Keep reasoning out of user-facing text]

AUTOMATIC_FALLBACKS:  (opt-in beta)
  API: `fallbacks: "default"` + beta header (Claude API only). Observable: content block {"type":"fallback"}, usage.iterations
  filled, billing split per model; app / Claude Code: same, can be switched off. Check the block AND usage.iterations
  (sticky routing: later turns reach the fallback model with no block — only a fallback_message entry); never guess the
  downgrade from output quality. Next turn: echo the fallback block in place — with thinking blocks from both sides,
  an omitted or moved block gets the request rejected (G21).

EXTENDED_THINKING:
  # no budget_tokens; no temperature / top_p / top_k; the flagship Claude model (exact id: live_specs.md) — omit thinking, set effort; the balanced Claude model (exact id: live_specs.md) off — between_tools

PLATFORMS:
  Microsoft Foundry: flagship / balanced Claude models (exact id: live_specs.md) Global Standard only; Foundry «follows the Claude API lifecycle schedule», yet the
    Microsoft table has its own dates — route by the platform actually called.
  Models API "line" field: group by line, not by parsing ids.
  Cowork on Windows: COWORK_WINDOWS_PLAN9. Claude Code: one retry of a turn stopped by the output filter while thinking.
  Claude Code client: maxEffortLevel caps effort on every provider (the lower of two caps wins); PreModelSwitch hooks may
    forbid a model switch; a skill / command with a different `model` in its frontmatter re-reads the history without cache;
    alias routing → route by explicit string;
    no model access → 404, unavailable beta header → 400 (not 403); token counting rejects server tools (except advisor),
    the MCP connector and url / file image or document blocks → base64 or usage from Messages.
  Prompt caching: minimum cacheable prompt on current Claude models (versions: live_specs.md).

CLAUDE_CONTEXT_STRATEGY:
  general / agentic → the flagship Claude model (exact id: live_specs.md) · cost-efficient agentic → the balanced Claude model (exact id: live_specs.md)
  complex code → the flagship Claude model (exact id: live_specs.md) · forced tool / least thinking → the fast Claude model (exact id: live_specs.md)
  documents → the agentic Claude model (exact id: live_specs.md)
  Worth checking live: the flagship Claude model (exact id: live_specs.md) as primary on a code audit and a long-horizon agentic run — response time, token spend,
  templates with forced tool_choice.

ARCH:        XML_NATIVE on the Claude host; host-gated when generating for other models.
WHEN_TO_USE: general reasoning / agentic / long-horizon (flagship Claude model PRIMARY (exact id: live_specs.md)), coding (flagship Claude model (exact id: live_specs.md)), balance (balanced Claude model (exact id: live_specs.md)),
             fast, forced tool, least thinking (fast Claude model (exact id: live_specs.md)).

// §Claude — flagship (PRIMARY), balanced, agentic (exact ids: live_specs.md):
//   one profile per model in vendors/claude.md (CLAUDE_5X). Prompts: XML structure (<role>, <rules>, <task>,
//   <output_format>), every MUST paired with a MUST NOT, no prefill, no sampling parameters.

FILE_META:
  COMPATIBLE:  live_specs.md | db.md
  SOURCES:     CLAUDE_5X_PROMPTING — Anthropic prompting guides (best practices; flagship, agentic,
               balanced and fast models)
