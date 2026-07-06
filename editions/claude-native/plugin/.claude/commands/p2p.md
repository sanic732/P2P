---
description: "/p2p — main entry point. Show menu, detect environment, initialize session."
argument-hint: "[start|menu]"
source_id: CMD_P2P_V8C
version: v8C.3
module_type: command
last_updated: 2026-06-12
scope: /p2p — main entry point. Show menu, detect environment, initialize session.
---
# /p2p — Главная Команда

**Что делает:** Показывает главное меню P2P v8C.3 и инициализирует сессию.

**Алгоритм:**
1. Определить среду (TRI_MODE_BRIDGE v3)
2. Загрузить p2p.config.md если есть
3. Показать меню (34 пункта)
4. Вывести: `[P2P v8C.3 | Среда: {СРЕДА} | Guardian: {ON/OFF}]`

**Использование:** `/p2p` или команда `СТАРТ`


========================================
VERSION_METADATA
========================================
id: CMD_P2P_V8C
version: v8C.3
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-06-12
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
