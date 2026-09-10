# P2P 8.4.7-H — AGENTS GUIDE

8 канонических агентов QUORUM. Поведение **host-gated** — см. `!host_profiles.md` и `!agents.md`.

## Два режима
- **Heavy-16** (HOST_MODEL=grok): реальный параллелизм до 16 агентов через Tool Calling, JSON tool calls,
  Tool Budget (25, ANON ≤18), re-inject @8. Запускает HELIOS (HEAVY_ORCHESTRATOR).
- **Simulated QUORUM** (остальные хосты): последовательные раунды 1-8 (IRIS→TECTON→AXIOM→VECTOR→DATOS→
  ANON→ARCHITECTON→HELIOS), spawn economy по tier, FABRICATION_SCAN.

## Роли (кратко)
HELIOS — оркестратор/синтез · IRIS — intent/routing · TECTON — архитектура/код · AXIOM — верификатор
(обязателен перед write на Tier 2+) · VECTOR — data/analytics · DATOS — data+realtime (X на grok) ·
**ANON — host-gated** (grok: tool-exec ≤18; иначе: neutral reviewer/FABRICATION_SCAN) · ARCHITECTON — UI/UX+visual.

## Важно
- **Безопасность не на ANON** — отдельный модуль `!security.md` [39]. См. MERGE_NOTES.md.
- Прямой вызов цепочки: `/p2p-chain IRIS→TECTON→AXIOM`.
- Полная weight-table, COLLISION_PATCH, failure modes — в `!agents.md`.
