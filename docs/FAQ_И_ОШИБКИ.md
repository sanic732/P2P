# P2P v8C.2 — FAQ и Ошибки

---

## G-ERRORS — Индивидуальные описания

### G1 — GEMINI_DEEP_THINK_TEMP
**Модель:** Gemini 3.1 Pro  
**Симптом:** HTTP 400  
**Причина:** Deep Think + temperature ≠ 1.0  
**Fix:** `temperature: 1.0` или убери temperature совсем

### G2 — GEMINI_XML_COH_INTERFERENCE
**Модель:** Gemini 3.1 Pro / Flash  
**Симптом:** Игнорирование инструкций, деградация качества  
**Причина:** XML теги в system context вызывают Chain-of-Hint interference  
**Fix:** ZERO XML в system context. Только plain text hierarchy.  
**Критичность:** 🔴 Blocker для любого Gemini использования с v8C.2

### G4 — GEMINI_THINKING_BUDGET_PRO
**Модель:** Gemini 3.1 Pro  
**Симптом:** thinking_budget молча игнорируется  
**Причина:** Pro модель использует thinkingLevel, не thinking_budget  
**Fix:** `thinkingLevel: "MEDIUM"` вместо `thinking_budget: 5000`

### G6 — OPUS47_TOKENIZER_INFLATION
**Модель:** Claude Opus 4.7  
**Симптом:** Контекст расходуется быстрее ожидаемого  
**Причина:** +10-35% inflation vs Opus 4.6  
**Fix:** Планируй 160K effective max, не 200K

### G7 — CLAUDE_EXTENDED_THINKING_TEMP
**Модель:** Claude Opus 4.7, Claude Sonnet 4.6  
**Симптом:** HTTP 400  
**Причина:** temperature передан при thinking=enabled  
**Fix:** Удали temperature из payload полностью

```python
# ПРАВИЛЬНО:
{"model": "claude-opus-4-7", "thinking": {"type": "enabled", "effort": "medium"}}

# НЕПРАВИЛЬНО (HTTP 400):
{"thinking": {"type": "enabled"}, "temperature": 0.7}
```

### G8 — OPUS47_MRCR_REGRESSION
**Модель:** Claude Opus 4.7  
**Симптом:** Плохой recall в длинных контекстах  
**Причина:** MRCR recall 32.2% at 1M (vs 78.3% у Opus 4.6)  
**Fix:** Для задач с recall >500K → пин `claude-opus-4-6`

### G9 — GPT55_SILENT_DOWNGRADE
**Модель:** GPT-5.5  
**Симптом:** Тихое снижение качества без ошибок  
**Причина:** >7 MUST/MUST NOT пар → silent downgrade  
**Fix:** Максимум 7 rule pairs

### G10 — GPT55_PRICING_TRAP
**Модель:** GPT-5.5  
**Симптом:** Неожиданный прыжок стоимости  
**Причина:** Pricing jump >272K input  
**Fix:** Держи под 272K. Для >272K → Gemini 3.1 Pro

### G11 — GEMINI_HIGH_BILLING_SHOCK
**Модель:** Gemini 3.1 Pro  
**Симптом:** Очень высокий счёт  
**Причина:** thinkingLevel=HIGH без Value Gate  
**Fix:** Применяй DEEP_THINK_VALUE_GATE перед HIGH

### G12 — GEMINI_HARD_429
**Модель:** Gemini 3.1 Pro  
**Симптом:** HTTP 429 без retry queue  
**Причина:** Pro — hard rate limit (Flash — soft + queue)  
**Fix:** Для high-frequency → Gemini Flash, не Pro

### G13 — GEMINI_MEMORY_NUKE
**Модель:** Gemini 3.1 Pro  
**Симптом:** Модель забывает constraints после ~80 сообщений  
**Причина:** Session memory nuke при heavy tool use  
**Fix:** CONSTRAINT_REINJECTION каждые 25 сообщений

### G14 — GROK_UNSUPPORTED_PARAM
**Модель:** Grok 4.3  
**Симптом:** HTTP 400 на нестандартные параметры  
**Причина:** Hard 400 (не молчаливое игнорирование)  
**Fix:** Safe params только: `temperature, max_tokens, stream, top_p, stop`

### G15 — DEEPSEEK_REASONING_CARRYOVER
**Модель:** DeepSeek V4  
**Симптом:** Загрязнение reasoning между turns  
**Fix:** Явно `reasoning_content: null` в multi-turn

### G16 — DEEPSEEK_ALIAS_RETIRE
**Модель:** deepseek-chat, deepseek-reasoner  
**★ DEADLINE: 2026-07-24**  
**Fix:** `deepseek-v4-pro` или `deepseek-v4-flash`

### G17 — QWEN_PROVIDER_PREFIX
**Модель:** Qwen 3.6  
**Симптом:** HTTP 404 или неправильная модель  
**Fix:** DashScope → `qwen3-plus`, OpenRouter → `qwen/qwen3-plus`

### G18 — QWEN_PRESERVE_THINKING
**Модель:** Qwen 3.6 agentic  
**Симптом:** Thinking теряется  
**Fix:** `preserve_thinking: true` для agentic задач

### G19 — GLM_CONTEXT_COLLAPSE
**Модель:** GLM-5.1  
**Симптом:** Деградация >100K  
**Fix:** Hard limit 100K для GLM-5.1

### G20 — KIMI_SWARM_TIMEOUT
**Модель:** Kimi K2.x  
**Симптом:** Timeout >40 sync agents  
**Fix:** >40 агентов → PARL async + webhooks

---

## QUICK REFERENCE TABLE

| G# | Модель | Тип | Критичность |
|----|--------|-----|------------|
| G1 | Gemini | HTTP 400 | 🔴 |
| G2 | Gemini | Quality fail | 🔴 |
| G4 | Gemini Pro | Silent ignore | 🟡 |
| G6 | Opus 4.7 | Cost | 🟡 |
| G7 | Claude | HTTP 400 | 🔴 |
| G8 | Opus 4.7 | Recall | 🟡 |
| G9 | GPT-5.5 | Quality | 🟡 |
| G10 | GPT-5.5 | Cost | 🟡 |
| G11 | Gemini | Cost | 🟡 |
| G12 | Gemini Pro | Rate limit | 🟡 |
| G13 | Gemini | Memory | 🟡 |
| G14 | Grok | HTTP 400 | 🔴 |
| G15 | DeepSeek | Context | 🟡 |
| G16 | DeepSeek | RETIRE | 🔴 |
| G17 | Qwen | 404 | 🟡 |
| G18 | Qwen | Context | 🟡 |
| G19 | GLM | Context | 🟡 |
| G20 | Kimi | Timeout | 🟡 |

---

## ЧАСТЫЕ ВОПРОСЫ

**Q: Claude перестал следовать правилам через 20 сообщений**  
A: Активируй CONSTRAINT_REINJECTION: `[21]` или подожди — P2P сделает это автоматически через 25 сообщений.

**Q: HTTP 400 при попытке использовать Extended Thinking**  
A: Удали `temperature` из payload — G7. Также удали `budget_tokens` (устарел).

**Q: Какую модель выбрать для задачи?**  
A: T0-1 → Sonnet 4.6. T2-3 → Sonnet 4.6 или Opus 4.7. T4 / максимальное качество → Opus 4.7.

**Q: QUORUM слишком долго / дорого**  
A: Используй FAST_TRIO (`/p2p-quorum fast`) вместо FULL QUORUM. Или снизь reasoning до LOW.

**Q: Как сохранить состояние между сессиями?**  
A: `/p2p-capsule save` → скопируй CAPSULE → вставь в новой сессии через `/p2p-capsule load`.

**Q: Extended Thinking или обычный режим?**  
A: Используй DEEP_THINK_VALUE_GATE: 2 из 3 условий (сложное рассуждение / >50K контекст / высокие ставки).

**Q: Для Gemini промпт работает хуже чем для Claude**  
A: Проверь G2 — убери XML теги из промпта для Gemini. Используй Translation Layer (`[5]`).

**Q: Можно ли использовать v8C.1 с GPT-5.5?**  
A: Да, через Translation Layer. Ограничения: max 7 rule pairs (G9), <272K tokens (G10), нет XML.

**Q: Что такое "Tier" задачи?**  
A: Уровень сложности T0-T4. Определяется автоматически через LoadScore. Влияет на выбор агентов, thinking level, QUORUM.

**Q: Как работает routing memory?**  
A: Система запоминает какой агент хорошо/плохо справился (+10%/-15%). Применяется при выборе агента. Decay: -5% через 30 дней.

---

## v8C.2-специфичные вопросы

### Q: Чем v8C.2 отличается от v8C.1?
A: Plugin manifest для one-click импорта + интерактивный teacher mode (`/p2p-teacher`).
   Drop-in replacement. Подробно: [ЧТО_НОВОГО.md](ЧТО_НОВОГО.md).

### Q: Как ставить v8C.2?
A: 5 методов на выбор. Рекомендуется метод 1: `bash pack.sh` → `.plugin` → drag-drop.
   Полный гайд: [INSTALL_GUIDE.md](INSTALL_GUIDE.md).

### Q: Что такое /p2p-teacher?
A: Интерактивный 5-уровневый курс по системе. Не лекция — упражнения, проверки понимания,
   Q&A режим. ~2 часа в сумме. Подробно: [TEACHER_GUIDE.md](TEACHER_GUIDE.md).

### Q: Я сидел на v8C.1 и работал через .claude/ в проекте. Как обновиться?
A: Удалить старые файлы, скопировать v8C.2 на их место. CAPSULE и `_live/live_core.md`
   совместимы — старый state читается.

### Q: pack.sh ругается на JSON
A: `python3 -c "import json; json.load(open('.claude-plugin/plugin.json'))"` —
   проверь что вернёт. Если ошибка — открой файл, ищи trailing comma или unclosed bracket.
