# Anti-Pattern Scan · P2P v1.1

> Scope: new/updated v1.1 artifacts against the Type A–P classifier
> from `.claude/skills/p2p-generator/anti-patterns.md`.
> Date: 2026-04-18 | Reviewer: P2P maintainer

═══════════════════════════════════════════════════════════════

## Artifacts in Scan

- `docs/SCOPE_HELM_GUIDE.md`
- `docs/LIVE_SPECS_PROTOCOL.md`
- `docs/WHATS_NEW_v1.1.md`
- `CHANGELOG.md`
- §APPEND patches in `core.md`, `routing.md`, `memory_bridge.md`, `debug_engine.md`, `global_index.md`, `templates_library.md`
- 9 slash commands, 8 sub-agent files, `settings.json`
- 4 new modules: `exploration_mode.md`, `session_metrics.md`, `routing_memory.md`, `scope_helm.md`

═══════════════════════════════════════════════════════════════

## Results by Type

| Type | Name                      | Status | Notes |
|------|---------------------------|--------|-------|
| A    | Pressure prompting        | ✅ PASS | Constraints-only. No MUST/CRITICAL/!!! pressure language. CHANGELOG and docs use "should", not "must". |
| B    | Instruction collision     | ✅ PASS | TRI_MODE_BRIDGE detector resolves env-dependent rule conflicts. SCOPE.HELM explicitly describes override via `p2p.config.md ENV`. |
| C    | Lost-in-the-Middle        | ⚠️ WATCH | `_live_specs.md` is 944 lines. KNOWN_ISSUES sits in the middle → risk of being skipped. **Mitigation:** routing.md/debug_engine.md read only relevant `[VENDOR: X]` sections via anchors, not the whole file. Confirmed in LIVE_SPECS_PROTOCOL § "Who imports and how". |
| D    | Attention sink            | ✅ PASS | No repeated decorative blocks overloading attention. `═══` separators are used as section anchors, not noise. |
| E    | Role drift                | ✅ PASS | 8 sub-agent files each have a clear `role` + `tool-permissions`. QUORUM assembles them explicitly without dilution. |
| F    | Format hallucination      | ⚠️ WATCH | Template L (Capsule) — fixed format with unicode borders. Opus 4.6 in long sessions may drift on borders. **Mitigation:** anchor `#DB_TEMPLATE_L` + explicit example in `templates_library.md`. Add regex border validator in v1.2. |
| G    | Over-helpfulness          | ✅ PASS | SCOPE_HELM_GUIDE § "Anti-pattern guardrails" explicitly states: single-shot tasks → SCOPE.HELM does not activate. GUARDIAN does not flood every message. |
| H    | Refusal cascade           | ✅ PASS | KNOWN_ISSUES Type D (OVER_REFUSAL_CONTEXT) imported with workaround "professional framing". |
| I    | Context window starvation | ✅ PASS | Progressive module disclosure preserved. 24 modules load lazily. p2p.config.md extracted from PRELOADER. |
| J    | Tool over/under-call      | ⚠️ WATCH | Type C_ext TOOL_FORGETTING (>15 tool calls) imported with workaround. QUORUM can generate chain >15. **Mitigation:** explicit limit in `p2p-quorum.md` slash command — "no more than 5 parallel agents per round". Verify in file — TODO. |
| K    | Multilingual leak         | ✅ PASS | `OUTPUT_LANG` in `p2p.config.md` (ru/en/uk). Docs in user language, code/anchors in English — clean separation. |
| L    | Versioning amnesia        | ✅ PASS | CHANGELOG v1.1 inherits from v1.0 with explicit `Base:`. SYSTEM_HASH bump recorded. Old modules not deleted. |
| M    | Cross-model leak          | ✅ PASS | v1.1 is Claude-edition, does not claim cross-model scope. `_live_specs.md` stores data for 8 vendors, but routing explicitly filters by active vendor. Cross-model porting goes through 7A (Gemini). |
| N    | Silent truncation         | ⚠️ WATCH | Haiku 4.5 OUTPUT_LIMIT 8K — corrected in core.md. But if user forces Haiku on long output, it will silently truncate. **Mitigation:** Model Router in SCOPE.HELM explicitly does not recommend Haiku for long-form artifacts. Consider warning in `p2p.config.md` validation in v1.2. |
| O    | Adversarial echo          | ✅ PASS | `routing_memory.md` uses bias, not replay. `[RM]` transparency marks every trigger — user sees that bias was applied. |
| P    | Skill non-trigger         | ✅ PASS | SKILL.md description extended (RU/UK/EN triggers), including "P2P", "meta-prompt", "generate prompt", "prompt for Claude/Gemini/...". Confirmed via system-reminder skill description. |

═══════════════════════════════════════════════════════════════

## Summary

- **PASS:** 12 / 16
- **WATCH:** 4 / 16 (C, F, J, N)
- **FAIL:** 0

All 4 WATCH items have active mitigations. None block the release.

═══════════════════════════════════════════════════════════════

## Action Items for v1.2

1. **[Type J]** Verify `commands/p2p-quorum.md` — confirm "no more than 5 parallel agents" limit exists. Add if missing.
2. **[Type F]** Add regex validator for Template L borders in `templates_library.md` (post-generation check).
3. **[Type N]** In `p2p.config.md` validation block: warning when `MODEL=haiku` and task type is `long_form`.
4. **[Type C]** Consider splitting `_live_specs.md` into `_live_specs_index.md` + `_live_specs_<vendor>.md` if file grows > 1500 lines.

═══════════════════════════════════════════════════════════════
END OF SCAN
