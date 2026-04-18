# P2P v1.1 — Installation: claude.ai (Projects / Chat)

## Option A — Claude Projects (recommended)

### Step 1 — Create a Project
1. Open claude.ai → Projects → Create new project
2. Name it (e.g. "P2P v1.1 Workspace")

### Step 2 — Upload Files to Project Knowledge

Upload **all files** from the archive root:
- `!!core_claude.md`, `!!db_claude.md`, `!routing_claude.md`, `!agents_claude.md`, `!intent_engine.md`
- `!contract_builder.md`, `!templates_library.md`, `!writing_suite.md`, `!visual_suite.md`
- `!memory_bridge.md`, `!debug_engine.md`, `!mentor_method.md`, `!domain_knowledge.md`
- `!global_index.md`, `!sandbox_user.md`, `user_context.md`

Total: **22 files** in Project Knowledge.

> **Note:** P2P v1.1 (Claude Edition) uses the `!!`/`!` prefix naming convention to control load priority in Claude Projects. Do not rename the files.

### Step 3 — Configure user_context.md

Open `user_context.md` in Project Knowledge (edit inline) and fill in the PROJECT_CARD fields for your project.

### Step 4 — Run

In a chat inside the Project:
```
start
```
or
```
/start
```
or
```
p2p
```

You'll get the full 29-item menu.

## Option B — Chat (no Project)

### Limit: 20 attachments per chat

Hard limit. P2P v1.1 has 22 files — it does not fit entirely in Chat. Use selective loading.

### Minimum set (always):
```
!!core_claude.md       ← FIRST
!!db_claude.md
!routing_claude.md
!agents_claude.md
!global_index.md
user_context.md
```

### Add by task:
```
!intent_engine.md        → complex tasks
!contract_builder.md     → precise prompt construction
!templates_library.md    → template selection
!writing_suite.md        → writing tasks
!visual_suite.md         → visual tasks
!memory_bridge.md        → cross-session state
!debug_engine.md         → debugging errors
!mentor_method.md        → learning / education
```

### Vendor files for target model:
```
!vendors_tier1.md        → Claude / GPT prompts
!vendors_tier2.md        → Gemini / Grok
!vendors_tier3.md        → DeepSeek / Qwen
!vendors_tier4.md        → Kimi / GLM
```

## claude.ai vs Code/Cowork Feature Comparison

| Feature | Projects | Chat | Code/Cowork |
|---|---|---|---|
| Start menu (29 items) | ✅ | ✅ | ✅ (via `/p2p`) |
| Slash commands | ❌ | ❌ | ✅ |
| Sub-agents (native) | ❌ logical only | ❌ logical only | ✅ Agent tool |
| SCOPE.HELM GUARDIAN | ✅ inline | ✅ inline | ❌ off |
| SPLITTER → TodoWrite | ❌ text map | ❌ text map | ✅ real todos |
| CAPSULE persistence | memory_bridge | copy-paste | file in `.claude/state/` |
| /lang toggle | ✅ | ✅ | ✅ |

## Updating an Existing v1.0 Project

If you already have a Project with v1.0 (7C.1) files:

1. **Do not delete** old files.
2. Replace all 20 system modules with v1.1 versions.
3. Replace `user_context.md` with the new template if needed.
4. The menu will automatically update on the next `start`.

## Troubleshooting

**Menu not showing on `start`?**
→ Verify `!!core_claude.md` is uploaded to Project Knowledge.

**`/lang` command not working?**
→ Confirm `!!core_claude.md` is the v1.1 version (contains `OUTPUT_LANG` flag in PRELOADER).

**Sub-agents not working?**
→ In claude.ai, sub-agents exist as logical roles inside `!agents_claude.md`. Native Agent tool is unavailable. QUORUM works via text orchestration, not parallel spawn.

**Live specs override not working?**
→ There is no `_live_specs.md` in the v1.1 Claude Edition release — vendor data lives in `!vendors_tier1-4.md`. Upload the appropriate tier file for your target model.
