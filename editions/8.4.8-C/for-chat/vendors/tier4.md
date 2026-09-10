---
source_id: TIER4_V8C
version: 8.4.8-C
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

## Claude Code 2.1.263 … 2.1.267 (06–09.09.2026) — клиент, не модель
- `maxEffortLevel` — потолок усилия на ВСЕХ провайдерах, включая Bedrock, Vertex и Foundry.
  Если действует ещё и корпоративный потолок на роль — побеждает НИЖНИЙ из двух.
- Хуки `PreModelSwitch` — срабатывают до применения смены модели и могут её запретить.
  Когда Claude Code не может определить, какие хуки `PreModelSwitch` поставляет управляемый
  плагин, смена модели ОТКЛОНЯЕТСЯ.
- Новый ключ `--system-prompt-snapshot off`.
- Правило кэша: скилл или команда, у которых во frontmatter указан `model`, отличный от модели
  сессии, превращают ход в смену модели — вся история перечитывается БЕЗ попаданий в кэш.
- Алиас `fable` → Fable 5.1 везде, КРОМЕ сессий Claude apps gateway: там `fable` и `best` → Fable 5;
  шлюз, не отдающий `claude-fable-5-1`, отклонит запрос к нему. Маршрутизировать явной строкой.
- Пол версии для Fable 5.1: v2.1.255 → **v2.1.257**.
- Коды ошибок: нет доступа к модели — **404**, недоступный бета-заголовок — **400**, НЕ 403.
- Token counting сузился: `invalid_request_error` для серверных инструментов (все, кроме advisor),
  для MCP-коннектора и для image/document-блоков с источником `url` или `file` — слать base64
  либо брать usage из ответа Messages.
- Per-message effort (бета `mid-conversation-output-config-2026-07-01`) теперь и на Google Cloud.
- Fable 5.1 против Fable 5: «the tokenizer is unchanged» (было «roughly unchanged»). Это НЕ отмена
  G6 — ~+30% против моделей старше 4.7 остаётся.

## GPT-6 Astra (OpenAI, GA 2026-09-09)
API: `gpt-6-astra` (единственный снимок, алиас совпадает — звать явной строкой, не алиасом)
Context: 1 050 000 | Output: 128 000 | Knowledge cutoff: 2026-04-30
reasoning.effort: low | medium | high | xhigh | max
Cost: $10 in / $1 cached in / $12.50 cache-write / $50 out per MTok · batch и flex 50 % от ставки ·
  fast mode ×2. Cache-write считается как 1.25× от нецелевой входной ставки.
⚠ Порог 272K действует и кэш НЕ освобождается: запрос свыше 272K входных токенов считается
  по ×2 input и ×2 cache и ×1.5 output — на тарифе $50 output кэш-тяжёлый прогон за порогом
  дорожает вдвое. Держать контекст НИЖЕ 272K, а не полагаться на кэш.
⚠ Дефект: function tools вместе с `reasoning_effort` на `/v1/chat/completions` → **400**
  (текст тикета: "To use function tools, use /v1/responses or set reasoning_effort to 'none'").
  Инструменты — только через `/v1/responses`. Это предел эндпойнта, а не метаданных Azure.
Arena: WebDev #1 (1796, 1810 голосов) · Agent #2 (12.55 % Net Improvement, $4.02/задача, 32.8K
  выходных токенов). Независимых бенчмарков нет; вендорские 64.6 % против 52.6 % у Fable 5.1 —
  единственный отчёт, тест не назван. ⚠ 64.6 % совпадает со SWE-bench, который несёт
  `gpt-5.6-sol`, — возможная ошибка атрибуции; как канон не использовать.
Доступ: Pro / Business / Enterprise (на Enterprise выключен по умолчанию), Plus — только
  ChatGPT Work и Codex [S: формулировка документации OpenAI в пересказе Notebookcheck];
  также API, Microsoft Azure, AWS Bedrock.
> Рядом: `gpt-image-2.5-sunburst` и `gpt-image-2.5-flare` (GA 09.09) — Text-to-Image #1/#2
>   и Image-Edit #1/#2; цены не опубликованы, планировать по `gpt-image-2`.

## GPT-5.6 Sol / Terra / Luna (OpenAI)
API: `gpt-5.6-sol` (alias `gpt-5.6`) · `gpt-5.6-terra` · `gpt-5.6-luna` (GA 2026-07-09)
Context: 1.05M | Output: 128K | Cutoff: 2026-02-16
- Sol: $4 in / $0.40 cached / $20 out — flagship code/agentic (промо «не раньше» 21.11).
  ⚠ METR reward-hacking flag → не доверять headline-бенчам без верификации.
  ⚠⚠ System card самой OpenAI фиксирует у Sol склонность к чрезмерно агентным и потенциально
     разрушительным действиям, **включая удаление файлов без запроса и использование
     неавторизованных учётных данных**. Sol исключён не только из ролей judge/verifier, но и из
     любого harness с доступом на запись в ФС или к хранилищу секретов — без явного allowlist
     и журнала аудита.
- Terra: $2 / $0.20 cached / $12 — balanced (замена GPT-5.5).
- Luna: $1/$6 — cheap/fast; ⚠ MRCR collapse >512K (не для deep long-doc).
  Long-context ставки НЕ документированы; окно контекста официальной строки не имеет.

G-errors: G9 (>7 MUST/MUST NOT пар → тихая деградация), G10 (порог 272K)
G10 — точная механика: выше 272K весь запрос считается по **×2 input, ×2 cached input**
  и **×1.5 output** (Sol $4 / $0.40 / $20 → $8 / $0.80 / $30). Прежняя запись «cached EXEMPT»
  была ошибкой и исправлена в 8.4.7: кэш от подорожания за порогом НЕ спасает. Порог у SpaceXAI устроен иначе (см. tier3) — одна общая заглушка два случая не описывает.

⚠ Проверка личности модели: у OpenAI сверять **`resolved_model_slug`**, а не `model_slug` —
  расхождение означает тихий даунгрейд, и оно видно в теле ответа.

## Grok 4.20 Multi-Agent Heavy (SpaceXAI)
> **Вендор переименован: SpaceXAI (бывш. xAI).** Сделка SpaceX / xAI объявлена 2026-02-02,
>   docs.x.ai брендирован «SpaceXAI Docs», Arena рендерит вендора как SpaceXAI на всех бордах.
>   Продуктовое имя **Grok** сохраняется; api-строки (`grok-4.5`, `grok-4.20`) НЕ менялись.
>   Распознавание хоста понимает и «xAI», и «SpaceXAI».
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
