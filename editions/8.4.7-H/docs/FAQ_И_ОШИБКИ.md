# P2P 8.4.7-H — FAQ и Ошибки

---

## Частые вопросы

**Q: Какую модель выбрать для задачи?**
A: T0-1 → Sonnet 4.6 или DeepSeek V4-Flash. T2-3 → Sonnet 4.6 или Opus 4.7.
T4 / максимальное качество → Opus 4.7. Бюджет → DeepSeek V4-Flash ($0.07/M).

**Q: HTTP 400 при Extended Thinking на Claude**
A: Удали `temperature` из payload — G7. Также убедись что нет `budget_tokens` (удалён из API). Используй `effort: "medium"`.

**Q: Промпт работает на Claude, но ломается на Gemini**
A: G2 (XML CoH interference). Убери все XML теги: `/p2p-translate gemini`.
Проверка: `grep -c '<[a-z_]*>' prompt.txt` должно быть 0.

**Q: Gemini перестал следовать правилам после 50+ сообщений**
A: G13 (memory nuke). Активируй CONSTRAINT_REINJECTION: `[21]` или подожди — P2P делает это автоматически каждые 25 сообщений.

**Q: DeepSeek возвращает мусор в multi-turn диалоге**
A: G15 (reasoning carryover). Re-inject `reasoning_content` в multi-turn с tools (НЕ обнулять — G15 RESOLVED BY DESIGN).

**Q: Grok отвечает не на мой вопрос**
A: G3 (topic drift). Добавь topic anchor каждые 3 хода:
`[TOPIC ANCHOR: Задача = {1 предложение}. Держись темы.]`

**Q: GPT-5.5 стал хуже отвечать без ошибок**
A: G9 (silent downgrade). Более 7 пар MUST/MUST NOT. Сократи до 7 максимум.

**Q: GLM деградирует на длинных документах**
A: G19. HARD LIMIT 100K для GLM-5.1 — выше этого качество рушится.

**Q: Kimi завис на большом swarm задании**
A: G20 (swarm >1h via REST → timeout). Используй PARL async + webhooks.

**Q: QUORUM слишком долго и дорого**
A: Используй FAST_TRIO (`/p2p-quorum fast`) — только IRIS→TECTON→AXIOM.
Или снизь reasoning до LOW в BUDGET DECLARATION.

**Q: Как сохранить состояние между сессиями?**
A: `/p2p-capsule save` → скопируй CAPSULE блок → вставь в новую сессию как первое сообщение.

**Q: Когда включать Extended Thinking?**
A: Используй DEEP_THINK_VALUE_GATE: 2 из 3 условий — (1) сложное многошаговое рассуждение, (2) >50K токенов контекста, (3) высокие ставки (production/необратимые действия).

**Q: Устаревшие API строки — что делать?**
A: `/p2p-deadline` или пункт [44] меню. Проверит все legacy strings и выдаст замены.
Главные: `claude-* dated legacy aliases (RETIRED 2026-06-15)` → актуальные (дедлайн 2026-06-15),
`deepseek-chat`/`deepseek-reasoner` → `deepseek-v4-flash` (дедлайн **2026-07-24 15:59 UTC**, без grace-периода;
chat→flash non-thinking, reasoner→flash thinking — это НЕ апгрейд на V4-Pro).

**Q: Что такое CROSS_MODEL_GENERATION_AWARENESS?**
A: Ключевой принцип Normal Edition. HOST_MODEL ≠ TARGET_MODEL.
Claude хост может генерировать промпт для Gemini → должен использовать синтаксис Gemini (ZERO XML), не свой XML.

**Q: P2P v8H.1 vs v8C.1 — что выбрать?**
A: v8C.1 (Claude Edition) — если используешь только Claude и хочешь максимум нативных возможностей (56 файлов, .claude/agents, полный HELIOS).
Редакция H (Hybrid Edition) — гибрид Gemini+Grok на любом из 8 хостов; Heavy-16 на grok, simulated QUORUM иначе.

---

## Quick Reference: G-Errors

| G# | Модель | Симптом | Критичность | Fix |
|----|--------|---------|-------------|-----|
| G1 | Gemini Pro | отказ / иное поведение | CRITICAL | не передавать temperature на линии 3.x; Deep Think — 1.0 или опустить |
| G2 | Gemini | Quality fail | CRITICAL (BLOCKER) | ZERO XML |
| G3 | Grok | Topic drift | HIGH | Anchor каждые 3 turn |
| G4 | Gemini Pro | Ignored thinking | MEDIUM | thinkingLevel вместо thinking_budget |
| G6 | Opus 4.7 | Context overflow | MEDIUM | Plan 160K effective max |
| G7 | Claude | HTTP 400 | CRITICAL | Удали temperature при thinking |
| G8 | Opus 4.7 | Bad recall | MEDIUM | Pin Opus 4.6 для >500K |
| G9 | GPT-5.5 | Silent downgrade | HIGH | Max 7 rule pairs |
| G10 | GPT-5.5 | Cost spike | HIGH | Stay <272K tokens |
| G11 | Gemini | Billing shock | HIGH | Value Gate перед HIGH |
| G12 | Gemini Pro | HTTP 429 | MEDIUM | Switch to Flash |
| G13 | Gemini | Memory nuke | HIGH | Reinject каждые 25 |
| G14 | Grok | HTTP 400 | CRITICAL | Safe params только |
| G15 | DeepSeek | Context pollution | MEDIUM | re-inject reasoning_content (НЕ null) |
| G16 | DeepSeek | RETIRE | CRITICAL | v4-pro/v4-flash |
| G17 | Qwen | HTTP 404 | MEDIUM | Правильный prefix |
| G18 | Qwen | Lost thinking | MEDIUM | preserve_thinking: true |
| G19 | GLM | Context collapse | CRITICAL | Hard limit 100K |
| G20 | Kimi | Swarm timeout | HIGH | PARL async >40 |

---

## Quick Reference: Error Types A-P

| Тип | Симптом | Fix |
|-----|---------|-----|
| A | Нет ответа, кредиты сняты | Уменьши thinking, разбей |
| B | Останов на 50-90% | Chunking, continuation |
| C | Обрезан молча | Проверь max_tokens |
| D | Деградация в середине | ANCHOR_CONTEXT |
| E | Забывает инструкции | Restate constraints |
| F | Gemini дрейфует | CONSTRAINT_REINJECTION |
| G | Kimi откатывает | Checkpoint before writes |
| H | Неправильный tool формат | Один формат на сессию |
| I | Overthinking (Kimi T0-1) | thinking:off |
| J | Плейсхолдеры в выводе | ZERO-STATE_IMMUNITY |
| K | Grok отвечает мимо | Topic anchor |
| L | Claude звучит скучно | /clear + острый промпт |
| M1 | Бесконечные правки | /clear + переписать |
| M2 | Слишком много файлов | Аудит контекста |
| M3 | Исследование съело контекст | Scope limit |
| N | Выдуманные tools | Defs в primacy zone |
| O | Отказ от легитимного | EXCELLENT technique |
| P | Переключение формата | Format lock в 2 зонах |
