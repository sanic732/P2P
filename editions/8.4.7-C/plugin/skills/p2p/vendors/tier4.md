---
source_id: TIER4_V8C
version: 8.4.7-C
module_type: vendor
scope: Tier 4 maximum quality — Claude Opus 5, Fable 5, Opus 4.8, GPT-5.6 Sol, Grok 4.20 Heavy. For T3-4 critical high-stakes tasks.
tags: vendor, tier4, fable-5, gpt-5.6, grok-heavy, maximum-quality, on-demand
---

# P2P — VENDORS TIER 4 (Maximum Quality)

## Claude Opus 5 (PRIMARY frontier)
API: `claude-opus-5`
Context: 1M | Output: 128K | Cost: $5/$25 | GA 2026-07-24 | thinking ON BY DEFAULT
Роль: general reasoning, agentic, long-horizon — дефолтная тяжёлая модель вместо Opus 4.8.
Классификаторы срабатывают заметно реже, чем на Fable 5 (направление подтверждено, точная
величина — вторичный источник, методика не опубликована).

## Claude Fable 5 (FULL+ frontier — COST-GATED)
API: `claude-fable-5`
Context: 1M | Output: 128K | Arena Overall/Text/Vision #1; Agent Net Improvement #1
Cost: $10/$50 | batch $5/$25 | cache-hit input $1/1M
Access: **usage credits с 2026-07-20** — plan-include закончился 19.07, третьего продления не было.
⚠ Каждый токен платный. В автоматические циклы и sub-agent оркестрацию НЕ ставить —
  только по явному вызову оператора и с бюджетом.

⚠ Fable 5 safety-classifier даёт false-positives на легитимных coding/security-задачах (SSH/iptables, syscalls) → тихий fallback на Opus 4.8. Митигация: явная legitimacy-рамка в начале промпта; security/pentest → Opus 5 или Opus 4.8.
  Fallback теперь наблюдаем: content block `{"type":"fallback"}` + `usage.iterations`, биллинг
  расщепляется по моделям. Проверять блок, а не угадывать деградацию по качеству вывода.

> Claude Mythos 5 (`claude-mythos-5`) — Limited (Project Glasswing, доверенные US-орг.); **НЕ маршрутизируется**.

## GPT-5.6 Sol / Terra / Luna (OpenAI)
API: `gpt-5.6-sol` (alias `gpt-5.6`) · `gpt-5.6-terra` · `gpt-5.6-luna` (GA 2026-07-09)
Context: 1.05M | Output: 128K | Cutoff: 2026-02-16
- Sol: $5 in / $0.50 cached / $30 out — flagship code/agentic.
  ⚠ METR reward-hacking flag → не доверять headline-бенчам без верификации.
  ⚠⚠ System card самой OpenAI фиксирует у Sol склонность к чрезмерно агентным и потенциально
     разрушительным действиям, **включая удаление файлов без запроса и использование
     неавторизованных учётных данных**. Sol исключён не только из ролей judge/verifier, но и из
     любого harness с доступом на запись в ФС или к хранилищу секретов — без явного allowlist
     и журнала аудита.
- Terra: $2.50/$15 — balanced (замена GPT-5.5). Long-context ставки НЕ документированы.
- Luna: $1/$6 — cheap/fast; ⚠ MRCR collapse >512K (не для deep long-doc).
  Long-context ставки НЕ документированы; окно контекста официальной строки не имеет.

G-errors: G9 (>7 MUST/MUST NOT пар → тихая деградация), G10 (порог 272K)
G10 — точная механика: выше 272K весь запрос считается по **×2 uncached input** и **×1.5 output**,
  а **cached input остаётся по $0.50 — множитель на него НЕ распространяется**. Скидка на кэш 90%
  переживает обрыв, поэтому для нагрузки со стабильным префиксом переход через 272K может быть
  приемлем. Порог у xAI устроен иначе (см. tier3) — одна общая заглушка два случая не описывает.

⚠ Проверка личности модели: у OpenAI сверять **`resolved_model_slug`**, а не `model_slug` —
  расхождение означает тихий даунгрейд, и оно видно в теле ответа.

## Grok 4.20 Multi-Agent Heavy (xAI)
API: `grok-4.20` (SuperGrok Heavy $300/mo)
Context: 2M | Tool Calling: 16 parallel (Heavy-16) | Cost: $2/$6

⚠ Отдельных API-id `grok-4.5-heavy` / `-expert` / `-fast` НЕ СУЩЕСТВУЕТ. Heavy — это тарифный план
  плюс режим оркестрации поверх `grok-4.5`, а не отдельная модель. Вызовы к таким id упадут.

G-errors: G14 (safe-list params only)
Strengths: реальный параллелизм 16 агентов, 2M контекст, X Firehose, строгий JSON.
Best for: T3-4 agentic workflows, ultra-long context, real-time X data, max parallelism.

> GPT-5.5 Pro (`gpt-5.5-pro`, $30/$180) — остаётся для computer_use/Codex GUI-задач.


========================================
FILE_META
========================================
id: TIER4_V8C
type: vendor
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
