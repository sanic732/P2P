---
description: P2P Karpathy Coding Mode — precision behavioral constraints for surgical code edits. Minimalist approach: Template M + PRE_CODE_DECLARATION. Composable with agentic (M+R) and IDE (M+I) templates.
argument-hint: [task description | file:path function:name]
---

Активируй skill `p2p`. Запусти **Karpathy Coding Mode** (Template M) для задачи: $ARGUMENTS

Используй Template M из `!templates.md` (!!db_v8C.md §TEMPLATE_M).

Обязательные элементы:
1. **PRE_CODE_DECLARATION** — допущения, неясности, скоуп, подход — до написания кода
2. **PLAN со Step → verify:** — если задача многошаговая (2+ шагов)
3. **MUST/MUST NOT** правила — хирургические изменения, минимальный код
4. **DONE CHECK** — ✅ что изменено | 🚫 что намеренно не тронуто

Агент: ANON | Template: M | Effort: medium | Strictness: Pro

Composability:
- Задача агентная (Claude Code/Devin) → комбинировать Template M + Template R (ReAct+Stop)
- IDE-редактирование (Cursor/Windsurf/Copilot) → комбинировать Template M + Template I (File-Scope)
- Tool-use (MCP) → комбинировать Template M + Template T (Tool-Use)

Karpathy Mode поведение (ANON применяет автоматически):
- Минимум кода — только то, что нужно для задачи
- Никаких комментариев если не просили явно
- Никаких "Here's the code:" преамбул
- Хирургические изменения — не переписывать без нужды
- Если задача неоднозначна — PRE_CODE_DECLARATION сначала, не угадывать

Template M напоминание (для справки):
```
[TASK]

Output: [FORMAT ONLY]
No preamble. No explanation. No sign-off.
```

Расширенная форма для кода:
```
Write [FUNCTION/CLASS] that [DOES X].
Language: [LANG] | Framework: [FRAMEWORK]
Constraints: [ONE LINE IF NEEDED]
Return only the code.
```
