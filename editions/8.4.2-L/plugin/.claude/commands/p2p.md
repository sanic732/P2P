---
description: "/p2p — main entry point. Show menu, detect environment, initialize session."
source_id: CMD_P2P_V8L
version: v8L.3
module_type: command
last_updated: 2026-06-27
scope: /p2p — main entry point. Show menu, detect environment, initialize session.
---
# /p2p — Главная Команда

**Что делает:** Показывает главное меню P2P v8L.3 и инициализирует сессию.

**Алгоритм:**
1. Выполнить FETCH_CAPABILITY_GATE (_preloader_v8L БЛОК 0) → зафиксировать LOAD_MODE
2. Определить среду (TRI_MODE_BRIDGE v3); загрузить p2p.config.md если есть
3. Показать меню (chunk-aware, !!core_v8L §4): пункты [36-41] видны только если чанк загружен;
   в LITE_ONLY недоступные lazy-пункты помечены "(требует fetch)"
4. Вывести баннер: `[P2P v8L.3 | LOAD_MODE: {GIST_LAZY_FETCH|LITE_ONLY} | Среда: {СРЕДА} | Guardian: {ON/OFF}]`

**Использование:** `/p2p` или команда `СТАРТ`

**Связано:** `/p2p-verify` — сверка целостности Gist-чанков (пункт [35] меню).


========================================
VERSION_METADATA
========================================
id: CMD_P2P_V8L
version: v8L.3
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-06-27
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
