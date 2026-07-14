# P2P v8L.3 — Руководство по агентам (QUORUM)

8 специализированных агентов. На claude/grok с плагином — нативные sub-agents
(`.claude/agents/`, AGENT_PATH=LOCAL). На остальных хостах — поднимаются из чанка
`gist_core_plus` (simulated QUORUM). Логика и веса идентичны.

## Ростер

| Агент | Роль | Сильная сторона | Профиль |
|-------|------|-----------------|---------|
| **IRIS** | Исследователь/Картограф | широкий обзор, скрытые зависимости | проблемное пространство |
| **TECTON** | Архитект/Структурировщик | декомпозиция, системный дизайн | структура |
| **AXIOM** | Критик/Верификатор | devil's advocate, стресс-тест | логика |
| **VECTOR** | Оптимизатор/Алгоритмист | trade-off, эффективность; **право VETO** | оптимизация |
| **DATOS** | Аналитик/Фактчекер | проверка данными, источники | факты |
| **ANON** | Security/Privacy | STRIDE, threat modeling | безопасность |
| **ARCHITECTON** | Интегратор/Холист | разрешение конфликтов, связи | интеграция |
| **HELIOS** | Финальный синтезатор | executive summary, действия | вывод |

## Запуск

```
/p2p-quorum [задача]        → FULL QUORUM (8 агентов, взвешенные голоса)
/p2p-quorum fast [задача]   → FAST_TRIO (IRIS→TECTON→AXIOM)
вызови IRIS для [задача]     → прямой вызов одного агента
```

QUORUM живёт в чанке `CORE_PLUS` на Gist — нужен включённый веб-доступ хоста.
Убедись через **`/p2p-verify`** до первого запуска.
(В 8L.3 агенты всегда из чанка `CORE_PLUS` — плагинной формы с локальными агентами у Lite нет, см. `README.md`.)

## Sub-QUORUM паттерны

| Паттерн | Состав | Когда |
|---------|--------|-------|
| FAST_TRIO | IRIS→TECTON→AXIOM | средние задачи, быстрый ответ |
| CODE_QUAD | TECTON→AXIOM→ANON→ARCHITECTON | код/архитектура |
| SECURITY_QUAD | AXIOM→ANON→VECTOR→HELIOS | аудиты безопасности |
| ARCH_PENTA | IRIS→TECTON→ARCHITECTON→DATOS→HELIOS | большие арх-решения |

## Веса по типу задачи (из `!!db_v8L §QUORUM_WEIGHTS`)

| task_type | доминирующие агенты |
|-----------|---------------------|
| CODING | TECTON 35%, ANON 25% |
| CREATIVE | IRIS 40% |
| RESEARCH | DATOS 40% |
| SECURITY | VECTOR 40% |
| ANALYTICAL/FRONTIER | AXIOM 35% |

**VETO:** VECTOR имеет абсолютное право вето на `[CRITICAL_RISK]` → все веса = 0 → Audit Mode.

## Параллельный запуск (только Code/Cowork, Tier 2+)
Один tool-message → N вызовов `Task(<АГЕНТ>)` в одном блоке → параллельно, изолированные контексты
→ сводит HELIOS. Потолок 3 экземпляра. Дифференцируй scope каждого (иначе N одинаковых отчётов).

## Failure modes (кратко)
TECTON — over-engineering на T0-1 · IRIS — abstraction spiral · ANON — over-blocking ·
AXIOM — analysis paralysis · DATOS — stale data · ARCHITECTON — technique collision ·
HELIOS — simplification tax. Полный список + митигации — в чанке `gist_core_plus` (!agents).
