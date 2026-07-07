---
description: "/p2p-verify — Manifest Reconciliation. Re-hash Gist chunks, compare to _index_v8L contracts, report drift."
source_id: CMD_VERIFY_V8L
version: v8L.3
module_type: command
last_updated: 2026-06-27
scope: /p2p-verify — Manifest Reconciliation. Re-hash Gist chunks, compare to _index_v8L contracts, report drift.
---
# /p2p-verify — Сверка целостности Gist-чанков (Manifest Reconciliation)

**Что делает:** Проверяет, что удалённые Gist-чанки совпадают с контрактами в `_index_v8L.md`
(sha256 + EOF-маркер + размер). Отвечает на вопрос «кто следит за хешами» — не человек вручную,
а эта команда перед релизом/при подозрении на drift.

**Алгоритм:**
1. Прочитать `GIST_ROUTING_TABLE` из `_index_v8L.md` (url + sha256 + eof_hash + size_kb по каждому чанку)
2. Для каждого чанка:
   - FETCH(url) — если хост умеет (иначе пометить SKIP: LITE_ONLY)
   - проверить: последняя непустая строка == eof_hash (анти-усечение)
   - проверить: sha256(тело) == контрактный sha256 (анти-подмена, D4)
   - проверить: размер в пределах ±15% от size_kb
3. Вывести таблицу `chunk · sha · eof · size` со статусами OK/DRIFT/MISSING
4. Итог: ✅ ALL VALIDATED либо ❌ DRIFT (с указанием чанков)

**Использование:** `/p2p-verify` (или пункт [35] меню)

**Локальный аналог (CI/релиз):** `bash verify_v8L.sh` — сверяет локальные `gist/*.md` против
`chunk_manifest.json`. При пересборке: `pack_v8L.sh` → `gh gist edit` → перепроставить revision в URL `_index`.

**Текущий Gist:** secret `7727406fc1047387c4e49bbef489bc46` @ rev `fdfe1e1` (10 активных чанков, pinned URLs).


========================================
VERSION_METADATA
========================================
id: CMD_VERIFY_V8L
version: v8L.3
type: command
edition: CLAUDE_NATIVE
last_verified: 2026-06-27
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
