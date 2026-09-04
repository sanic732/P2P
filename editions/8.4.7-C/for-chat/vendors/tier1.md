---
source_id: TIER1_V8C
version: 8.4.7-C
module_type: vendor
scope: Tier 1 budget models — Gemini 3.5 Flash-Lite, DeepSeek V4-Flash, Qwen 3.6-Plus, Kimi K2.6/K2.7, GLM-5.1, GPT-5.6 Luna. For T0-2 high-volume or cost-sensitive tasks.
tags: vendor, tier1, deepseek, qwen, kimi, glm, budget, on-demand
---

# P2P — VENDORS TIER 1 (Budget)

## Gemini 3.5 Flash-Lite (самый дешёвый уровень)
API: `gemini-3.5-flash-lite`
Context: 1M | Output: 64K | Cost: $0.30/$2.50 | ~350 tok/s | GA 2026-07-21
Best for: самая дешёвая hosted-опция с 1M контекстом

G-errors: G1, G2, G13 (обходы G13 применять и здесь — на 3.5/3.6 Flash баг не закрыт)

## DeepSeek V4-Flash
API: `deepseek-v4-flash` (⚠ НЕ `deepseek-chat`/`deepseek-reasoner` — alias мёртв с 2026-07-24 15:59 UTC,
     без grace-периода; точный HTTP-код первичными логами не подтверждён: 404 либо 400 invalid_request_error)
Context: 1M | Output: 384K | Cost: $0.14/$0.28 | Best for: Bulk batch, T0-2

⚠ СТАТУС ЛИНЕЙКИ V4: официально **PREVIEW**. Свежайшая запись V4 в changelog вендора датирована
  2026-04-24; с 13.08.2026 v4-pro официально GA, v4-flash-0731 остаётся public beta. Заявления
  о GA — вторичные. При этом после ретайра алиасов V4 остался единственным рабочим путём, поэтому
  модели сохранены в маршрутизации с этой пометкой, а не удалены.
⚠ Thinking у V4-Flash включён по умолчанию и не отключается.

G-errors: G15 (reasoning_content store + re-inject после tool calls — BY DESIGN), G16 (alias RETIRE 24.07)
> Соседний: DeepSeek V4-Pro (`deepseek-v4-pro`, $0.435/$0.87, 1M) — T2-3, SWE-bench Verified 80.6%.
> ⚠ Нагрузку бывшего `deepseek-reasoner` вести на **v4-pro**, а НЕ на v4-flash-thinking —
>   иначе reasoning тихо деградирует (официальный маппинг алиасов указывал на flash).

## Qwen 3.6-Plus
API DashScope: `qwen3.6-plus` | Context: 1M | Cost: Budget | Best for: Multilingual, Chinese content

G-errors: G17 (preserve_thinking=true для agentic), G18 (обязательный `bailian/` prefix — иначе silent fail)

## Kimi K2.6 / K2.7 Code
API: `kimi-k2.6` (Swarm 300 agents) · `kimi-k2.7-code` (open-weight coding, $0.95/$4)
Context: 256K-1M | Best for: Large swarm orchestration, long-horizon agentic

G-errors: G20 (>N sync agents → timeout; для больших swarm → async PARL/webhooks), Type M (infinite-repetition в Thinking-mode → temp=1.0/min_p=0.01)
> ⚠ Type M задокументирован для **K2.5/K2.6**. На K3 «!»-цикл не воспроизводился, отчётов в
>   трекерах vLLM и llama.cpp нет — тег скорее K2.x-специфичен. Обход «отключить Thinking»
>   на K3 неприменим: там thinking не отключается.
> Kimi Code HighSpeed (`kimi-for-coding-highspeed`) — access-tier ~5-6x Standard speed.

## GLM-5.1 (MIT)
API: `glm-5.1` | Context: 200K (effective ~120K) | Cost: budget

G-errors: G19 (context collapse >120K → cap 100-120K, или мигрировать на GLM-5.2 1M)

## GPT-5.6 Luna
API: `gpt-5.6-luna` | Cost: $1/$6 | Best for: cheap high-volume, classification, streaming
> ⚠ MRCR collapse >512K — не для deep long-doc анализа (см. tier4 GPT-5.6 семейство).
> ⚠ Окно контекста официальной строки НЕ имеет — в разделе Models вендора есть строки для 5.5 и 5.4,
>   строки для Luna нет. Ни 1.05M/128K, ни 400K/64K не подтверждены. Не закладываться на цифру.
> ⚠ Long-context ставки для Luna и Terra НЕ документированы: порог 272K и множители расписаны
>   только для Sol. Ходившие $2/$9 и $5/$22.5 — экстраполяция сторонних калькуляторов, не данные
>   вендора. В canon не вносить.
> ⚠ Голый алиас `gpt-5.6` резолвится в Sol — самый дорогой уровень. Всегда пинить terra/luna явно.


========================================
FILE_META
========================================
id: TIER1_V8C
type: vendor
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
