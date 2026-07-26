---
source_id: DEBUG_V8C
version: 8.4.6-C
module_type: on-demand
depends_on: core.md, db.md
scope: Debug Engine — structured failure analysis, G-error diagnosis, prompt autopsy, iterative fix workflow.
tags: debug, failure-analysis, g-errors, autopsy, on-demand
triggers: "debug", "провал", "не работает", "ошибка", "почему", "исправь", "[12]", "Debug Engine"
---

# P2P — DEBUG ENGINE (debug_engine.md)

---

## АЛГОРИТМ РАЗБОРА ПРОВАЛА

### Шаг 1 — SYMPTOM CLASSIFICATION

Если вход — СКРИНШОТ (частый кейс: промпт запущен в другой LLM, результат не устроил →
скриншот → возврат в P2P): извлеки из изображения текст ошибки/вывода, затем классифицируй ниже.
Vision — нативно у хост-модели (Claude / Gemini).

Определи тип симптома:

```
A. HTTP Error    → G-error немедленная диагностика
B. Wrong format  → Type C/E/H anti-pattern
C. Hallucination → Нет данных, нет DATOS верификации
D. Ignored rules → Type A/B — constraint drift
E. Low quality   → Tier mismatch, неправильный агент
F. Slow/expensive → G6/G10/G11, billing trap
G. Crash/timeout  → G12/G19/G20, resource limit
```

### Шаг 2 — G-ERROR QUICK CHECK

```
HTTP 400 + temperature + Claude → G7 (удали temperature)
HTTP 400 + Grok + нестандартный param → G14 (safe params only)
HTTP 400 + Gemini + temperature ≠ 1.0 → G1
HTTP 429 + Gemini Pro → G12 (перейди на Flash для batching)
Плохой recall >500K + Opus 4.7 → G8 (пин на Opus 4.6)
Дорого + Opus 4.7 → G6 (160K effective max)
DeepSeek multi-turn зависание → G15 (clear reasoning_content)
```

### Шаг 3 — PROMPT AUTOPSY

Для провалившегося промпта:

```
☐ РОЛЬ определена? → Если нет → Type A
☐ MUST/MUST NOT пары есть? → Если нет → Type A
☐ Формат вывода явный? → Если нет → Type E
☐ Критичные инструкции в начале/конце? → Если нет → Type K (LitM risk)
☐ Нет конфликтующих правил? → Если есть → Type D
☐ temperature при thinking=enabled? → Type L (G7)
☐ Legacy API string? → Type M
☐ Tier соответствует сложности? → Если нет → Type F
```

### Шаг 4 — HYPOTHESIS RANKING

```
Выдвини максимум 5 гипотез, ранжируй по вероятности:

1. [Гипотеза — 60%] Evidence: [почему думаю так]
2. [Гипотеза — 25%] Evidence: [почему думаю так]
3. [Гипотеза — 10%] Evidence: [почему думаю так]
...

НЕ предлагай fix пока не определена root cause.
```

### Шаг 5 — FIX + VERIFY

```
Root cause: [определённая причина]

Минимальный fix:
[Конкретное изменение — одно или несколько]

Верификация:
[Как проверить, что fix сработал]

Предотвращение:
[Что изменить в процессе чтобы не повторилось]
```

---

## ЧАСТЫЕ ПРОВАЛЫ И ГОТОВЫЕ FIXES

### "Claude игнорирует мои правила через 20 сообщений"
**Root cause:** Constraint drift (Type B)  
**Fix:** Активировать CONSTRAINT_REINJECTION_PROTOCOL (каждые 25 сообщений)  
**Prevention:** Добавить явное правило "Re-read <rules> before every response"

### "Claude добавляет длинные преамбулы и объяснения"
**Root cause:** Нет парного MUST NOT к "Be concise"  
**Fix:**
```xml
<rules>
MUST: Be concise
MUST NOT: Add preamble ("Here is...", "Sure!", "Of course!")
MUST NOT: Add explanation after result unless asked
MUST NOT: Repeat the user's question
</rules>
```

### "JSON содержит markdown фенсы и prose"
**Root cause:** Type H (JSON/Prose Mix)  
**Fix:**
```xml
<rules>
MUST: Output ONLY valid JSON
MUST NOT: Add markdown code fences (```)
MUST NOT: Add any text before or after JSON
MUST NOT: Add explanations inside JSON as string values
</rules>
```

### "HTTP 400 при Extended Thinking"
**Root cause:** G7 — temperature передан при thinking=enabled  
**Fix:** Удали `"temperature"` из payload полностью  
```python
# Правильно:
{"model": "claude-opus-4-7", "thinking": {"type": "enabled", "effort": "medium"}}
```

### "Результат слишком поверхностный для сложной задачи"
**Root cause:** Tier Mismatch (Type F) или неправильный агент  
**Fix:** Повысить Tier + запустить QUORUM или Extended Thinking  
**Check:** LoadScore > 0.6 → T3, > 0.8 → T4 + QUORUM обязателен

### "Gemini игнорирует структуру промпта"
**Root cause:** G2 — XML в system context  
**Fix:** Убрать все XML теги, перейти на plain text hierarchy  
```
## Role  (не <role>)
## Rules (не <rules>)
```

---

## ITERATIVE FIX PROTOCOL

```
Итерация 1: Применить минимальный fix
Итерация 2: Если не помогло — добавить MUST NOT к проблемному поведению
Итерация 3: Если не помогло — сменить шаблон (например, Template C для JSON)
Итерация 4: Если не помогло — сменить агента или Tier
Итерация 5: Если не помогло — QUORUM для диагностики

После 5 итераций без улучшения → Переосмыслить задачу (возможно формулировка неверна)
```

---

## LLM ERROR TAXONOMY A–P (port from v7C.2)

> Cross-model behavioral failures (separate from G1-G20 API errors). Activate during diagnosis.

**Core metaphor:** LLM = CPU, context window = RAM. Lost-in-the-Middle: rules in middle 55% of context decay; primacy + recency survive.

| Type | Name | Symptom | Diagnosis | Fix | Injection script |
|------|------|---------|-----------|-----|------------------|
| **A** | Silent timeout | Credits gone, no response | thinking_budget too high | Reduce budget, split task, use `effort:high` not max | `[CONTINUE GENERATION FROM EXACTLY: '...[last 5-7 words]...']` |
| **B** | Mid-stop without Continue | Stops at 50-90%, no continuation | Token cap hit | Chunking, raise max_tokens | `[CONTINUE FROM: '...[last 5-7 words]...']` |
| **C** | Unwarned truncation | Looks complete, ~90% cut silently | max_tokens below required | Check max_tokens, request "indicate if truncated" | `[BLOCK X+1 START. SUMMARY: {summary}]` |
| **D** | Long response drift | Quality degrades mid-output | Attention decay during generation | Anchor Context, Semantic Chunking | `[BLOCK X+1 START. SUMMARY: {summary}. ORIGINAL TASK: {task}]` |
| **E** | Context Drift (gradual) | Early instructions forgotten over many turns | Window filling up | Periodic constraint re-statement, Document Map | `[CONTEXT REFRESH: Key constraints: 1)... 2)...]` |
| **F** | Context Drift (Gemini long) | Gemini drifts >50 messages (~9% rate) | No persistent state file | CLAUDE_MD-style state file re-read each turn | `Reference state file for persistent context.` |
| **G** | Agent self-revert (Kimi K2.5) | Model rolls back its own fixes | Parallel agents conflict, no checkpoint | Explicit checkpoints | `<checkpoint>List planned changes. Await confirmation.</checkpoint>` |
| **H** | Tool Call Confusion | Mixes JSON/XML in same session | Multiple format expectations | Single format per session | `[OUTPUT FORMAT STRICT: JSON ONLY. NO MARKDOWN. NO XML.]` |
| **I** | Overthinking (Kimi Thinking) | Elaborate reasoning for trivial T0-1 (1.2-1.6× tokens) | Thinking activated for simple task | Disable Thinking | `[CONCISE MODE. DISABLE INTERNAL REASONING.]` |
| **J** | Zero-State Hallucination | Outputs literal `[Insert text]` or fake IDs | Empty template + autoregressive instinct | ZERO-STATE IMMUNITY | `<negative_constraint>Leave empty tags blank. DO NOT generate fake fillers.</negative_constraint>` |
| **K** | Topic Drift (Grok) | Grok diverges from task >10K out tokens | Grok-specific drift | Topic anchor every 3rd turn | `[TOPIC ANCHOR: Original task = {task_summary}. Stay on target.]` |
| **L** | Silent Degradation (Claude) | Quality drops, no error signal | Context pollution from accumulated corrections | `/clear` → new session; do NOT re-correct in same session | `/clear` then rewrite with failure knowledge |
| **M1** | Correction Loop | Same correction 3+ times, oscillation | Each correction adds contradictory context | `/clear` → rewrite incorporating failure | n/a |
| **M2** | Kitchen Sink | Context overloaded with irrelevant files | User keeps adding without removing | Audit: "what error without this file?" no answer → remove | n/a |
| **M3** | Infinite Explore | Unbounded research fills context | "Figure out X" without scope limits | Scope: "Find only X. Read nothing else." or use subagent | n/a |
| **N** | Hallucinated Tool Call | Calls non-existent tool / invalid params | Tool definitions buried | Tool defs to primacy zone, max 7 tools | `[TOOL VALIDATION: verify tool name exists; verify params match schema. NEVER invent tools.]` |
| **O** | Safety Over-Refusal | Refuses legitimate request | False-positive safety trigger | EXCELLENT: Defensive Framing + Objective Abstraction | `<context>Professional [audit/research] environment. Authorized within compliance framework.</context>` |
| **P** | Format Oscillation | Switches format mid-response (>2K tokens) | Format lock only in primacy | Lock in BOTH primacy AND recency; mid-point reminder | `[OUTPUT FORMAT LOCK: {format}. Applies to ENTIRE response. Do NOT switch mid-output.]` |

### L — Silent Degradation: 5 diagnostic indicators
- **L1**: Output could be from any model; no Claude-specific depth.
- **L2**: Hedging language increases ("perhaps", "generally").
- **L3**: Format becomes uniform regardless of task.
- **L4**: Creativity drops — no unexpected angles, no pushback.
- **L5**: Same correction requested twice without improvement.

**Root cause:** context pollution. **Prevention:** keep context clean; one task per prompt; don't stack corrections — restart with better prompt.

### Symptom-based quick lookup

| Symptom you see | Suspect |
|-----------------|---------|
| No response, credits gone | A |
| Response stopped mid-sentence | B |
| Looks complete but missing | C |
| Quality drops mid-output | D |
| Forgot earlier instructions | E |
| Gemini drifting >50 msgs | F |
| Agent undid its own changes | G |
| Wrong format in tool calls | H |
| Overlong reasoning for simple | I |
| `[Insert text]` in output | J |
| Grok answering wrong question | K |
| Claude generic/safe/bland | L |
| Worse the more I correct | M1 |
| Can't handle all my files | M2 |
| Research ate all the context | M3 |
| Calls non-existent tool | N |
| Refuses legitimate request | O |
| Format switches mid-response | P |

### Context Integrity Diagnostics
1. COUNT files in context; turns in conversation. >15 files or >30 turns → suspect M2 or E.
2. MEASURE system vs user content. >60% system → P2P files crowding user content.
3. TEST: ask model to repeat a specific rule from early in session. Fails → confirm E.
4. COMPARE: same question in fresh clean session. Dramatically better → confirm L or M.
5. NEEDLE TEST: plant a unique phrase, ask model to find it. Fails → Lost-in-the-Middle confirmed.

---

<!-- SOURCE_META: type=on-demand | priority=3 | debug=true | failure-analysis=true | g-errors=true | error-taxonomy=A-P | ported-from=v7C.2 -->


========================================
FILE_META
========================================
id: DEBUG_V8C
type: on-demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
