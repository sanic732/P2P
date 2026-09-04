---
source_id: GLOSSARY_V8C
version: 8.4.7-C
module_type: meta
scope: P2P glossary — all terms, acronyms, G-errors quick reference, agent names.
tags: glossary, terms, definitions, g-errors-reference, v8c
---

# P2P — ГЛОССАРИЙ (_glossary.md)

---

## ТЕРМИНЫ P2P

**ATLAS** — карта задач сессии (GOAL/PROGRESS/NEXT_STEP/BLOCKERS). Обновляется автоматически.

**BUDGET DECLARATION** — обязательное объявление бюджета перед запуском QUORUM: количество агентов, reasoning level, stop conditions.

**CAPSULE** — снимок состояния сессии для восстановления в новой сессии.

**Constraint Drift** — постепенное игнорирование ранних инструкций при длинных сессиях. Решение: CONSTRAINT_REINJECTION_PROTOCOL.

**Contract** — промпт, построенный по 9-step алгоритму с MUST/MUST NOT парами.

**Cortex Patch A** — расширение для дивергентного мышления (Exploration Mode). В v8C.3 встроен.

**DEEP_THINK_VALUE_GATE** — 3 вопроса перед активацией Extended Thinking. 2/3 да → включить.

**G-Error** — известная ошибка конкретной LLM модели. G1-G20 задокументированы.

**GUARDIAN** — протокол защиты от scope creep. ON в Code/Projects режиме.

**HELIOS** — 8-й агент QUORUM, финальный синтезатор.

**LoadScore** — числовая оценка сложности задачи (0.0-1.0). Определяет Tier.

**LitM** — Lost in the Middle — феномен когда LLM хуже вспоминает информацию из середины контекста. Type K anti-pattern.

**P2P** — Prompt-to-Prompt, мета-промпт система для генерации промптов под другие LLM.

**QUORUM** — консилиум из 8 специализированных агентов для сложных задач.

**ROUTER** — компонент SCOPE.HELM управляющий переходами между шагами.

**SIR Scanner** — Signal → Intent → Route, алгоритм классификации запросов.

**SCOPE.HELM** — система управления большими задачами (SPLITTER + CAPSULE + ROUTER).

**SPLITTER** — компонент SCOPE.HELM для декомпозиции больших задач.

**TRI_MODE_BRIDGE** — автоматическое определение среды (Code/API/Projects/Chat).

---

## АГЕНТЫ

| Имя | Специализация | Позиция в QUORUM |
|-----|---------------|-----------------|
| IRIS | Исследование, картография | Раунд 1 |
| TECTON | Архитектура, структура | Раунд 2 |
| AXIOM | Критика, верификация | Раунд 3 |
| VECTOR | Оптимизация, алгоритмы | Раунд 4 |
| DATOS | Данные, аналитика | Раунд 5 |
| ANON | Безопасность, приватность | Раунд 6 |
| ARCHITECTON | Интеграция, холизм | Раунд 7 |
| HELIOS | Финальный синтез | Раунд 8 |

---

## G-ERRORS QUICK REFERENCE

| Код | Модель | Описание | Критичность |
|-----|--------|----------|------------|
| G1 | Gemini Pro | Deep Think + temp≠1.0 → HTTP 400 | 🔴 |
| G2 | Gemini | XML в system context → CoH fail | 🔴 |
| G4 | Gemini Pro | thinking_budget игнорируется | 🟡 |
| G6 | Opus 4.7+ / Fable 5 / Sonnet 5 / Opus 5 | ~+30% tokenizer inflation (офиц.; счётчик — Token Counting API) | 🟡 |
| G7 | Claude 4.x | temperature + thinking → HTTP 400 | 🔴 |
| G8 | Opus 4.7 | MRCR 32.2% at 1M (vs 78.3% у 4.6) | 🟡 |
| G9 | GPT-5.5 | >7 rule pairs → silent downgrade | 🟡 |
| G10 | GPT-5.5 | >272K input → pricing trap | 🟡 |
| G11 | Gemini | thinkingLevel=HIGH billing shock | 🟡 |
| G12 | Gemini Pro | Hard 429 (нет queue) | 🟡 |
| G13 | Gemini | Memory nuke после ~80 сообщений | 🟡 |
| G14 | Grok | Unsupported param → HTTP 400 | 🔴 |
| G15 | DeepSeek | reasoning_content carryover | 🟡 |
| G16 | DeepSeek | deepseek-chat/reasoner RETIRE 2026-07-24 | 🔴 |
| G17 | Qwen | Provider prefix mismatch | 🟡 |
| G18 | Qwen | preserve_thinking=false by default | 🟡 |
| G19 | GLM | Context collapse >100K | 🟡 |
| G20 | Kimi | Swarm timeout >40 sync agents | 🟡 |

---

## TIER СИСТЕМА

| Tier | Сложность | Время | Агентов | QUORUM |
|------|-----------|-------|---------|--------|
| T0 | Тривиально | <5 мин | 1 | Нет |
| T1 | Просто | 5-15 мин | 1 | Нет |
| T2 | Средне | 15-60 мин | 1-3 | Опционально |
| T3 | Сложно | 1-4 ч | 3-5 | Рекомендован |
| T4 | Критично | >4 ч | 5-8 | Обязателен |

---

## API STRINGS (актуальные, May 2026)

| Модель | API String |
|--------|-----------|
| Claude Opus 4.7 | `claude-opus-4-7` |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` |
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` |
| GPT-5.5 | `gpt-5.5` |
| Grok 4.3 | `grok-4.3` |
| DeepSeek V4-Flash | `deepseek-v4-flash` |
| Qwen 3.6-Plus | `qwen3-plus` |
| Kimi K2.x | `kimi-k2-6` |

<!-- SOURCE_META: type=meta | priority=2 | glossary=true | reference=true -->


========================================
FILE_META
========================================
id: GLOSSARY_V8C
type: meta
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
