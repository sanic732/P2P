# P2P v8H.3 — CHANGELOG (Hybrid Edition)

**Build:** v8H.3 (Hybrid = merge 8A.1 Gemini ⊕ 8G.1 Grok) · **Date:** 2026-06-17
**Base:** универсальный каркас 8N-style + 8C.3 parity · **Donors:** 8A.1, 8G.1 (read-only).

---

## [NEW] Гибридная редакция (merge 8A.1 + 8G.1)
- Универсальный preloader: `HOST_MODEL` (8 хостов) + `HOST_CAPS` авто-гейты + `GROK_FLAGS` + VERSION_COMPAT.
- **`!host_profiles.md`** — host-choice brain: при `HOST_MODEL=grok` → нативный Heavy-16; иначе → simulated QUORUM.
- **`!agents.md`** — host-gated merge: Heavy-16 (8G) ⊕ simulated QUORUM раунды 1-8 (8A).
  - **ANON host-gated**: grok→tool-exec (≤18 calls); иначе→neutral reviewer (FABRICATION_SCAN).
  - **Безопасность вынесена в `!security.md`**, НЕ на ANON (в отличие от 8C.3). Матрица — docs/MERGE_NOTES.md.
  - VECTOR=data (default; creative→IRIS/!writing); DATOS=data+realtime (X только на grok); AXIOM-before-write (union).

## [NEW] Grok host-engine (порт из 8G.1)
- `!llm_router.md` — multi-provider router; default primary=HOST_MODEL (не хардкод Grok); +Fable 5/Opus 4.8;
  contract-translation на 8 хостов (Gemini zero-XML); unified output schema сохранён; fallback chain host-agnostic.
- `!routing_matrix.md` — аудируемая routing matrix v2.0 (task taxonomy + примеры).
- `!tool_budget.md` — Type B prevention (budget 25, ANON ≤18, re-inject @8); grok-gated.
- `!x_realtime.md` — X Firehose ($0.50 value gate, 7-day cache); только grok host.
- `!!db_v8H`: добавлены Grok Heavy failure modes Type B/H/T/X/V + G14.

## [PARITY] 8C.3 техники (унаследованы из 8N.3)
- 6 ON-DEMAND модулей [35-40]: RAG/Reasoning/Routing/Compression/Security/Optimization (host-gated, ≤5K).
  `!routing` ссылается на `!llm_router` (без дублирования cascade/cost).
- VERSION_COMPAT (legacy/v3 + 6 MODULE_* default false) + CONFLICT_RESOLVER v1.0 + динамическое меню [35-40].
- Расширения memory/agents/metrics/toolkit (append-блоки).

## [LIVE] Нативный live-specs 2026-06-12 (v8.4)
- Claude Fable 5 (#1 Agent/WebDev) + Opus 4.8 в tier1/live_core/live_vendors/llm_router.
- Старые спеки доноров (8A=05-19, 8G=05-19) не переносились; единый источник — live_specs_20260617.

## [FORM] Две формы поставки
- flat (Chat/Projects/API) + native plugin (`.claude/agents/p2p-*.md` ×8 + `.claude-plugin/{plugin,marketplace}.json`).

## [META]
- Версии v8H.3 во всех операционных файлах; G1-G20 union обоих доноров сохранён.
- Дедлайны: Claude dated legacy / gpt-5.x legacy — PASSED, литералы отсутствуют (унаследовано из 8N.3);
  deepseek-chat/reasoner (07-24) — активные ретайр-нотисы. budget_tokens не используется (G7).

---

## Тесты (3 кейса/модуль вкл. grok-host и gemini-host)
| Кейс | Ожидание |
|------|----------|
| grok host, agentic T4 | Heavy-16 native (реальный параллелизм), Tool Budget, ANON=tool-exec ≤18 |
| gemini host, тот же запрос | simulated QUORUM раунды 1-8, ZERO-XML (G2), ANON=neutral reviewer |
| !routing на любом хосте | ссылка на !llm_router; не дублирует cascade |
| !security активен | GUARDIAN форс ON; ANON остаётся в родной роли (security отдельно) |
| X Firehose на non-grok | недоступен → web_search fallback |
| budget_tokens / temp+thinking | отсутствуют (G7); retired строки только в нотисах |
