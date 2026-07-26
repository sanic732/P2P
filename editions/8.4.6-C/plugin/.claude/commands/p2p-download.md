---
description: "/p2p-download — загрузка актуальных LIVE SPECS с удалённого Gist."
source_id: CMD_DOWNLOAD_V8C
version: 8.4.6-C
module_type: command
scope: "/p2p-download — full integration; fetch LIVE SPECS from gist."
---
# /p2p-download — загрузка актуальных LIVE SPECS

**ОПИСАНИЕ КОМАНДЫ:** Принудительно инициирует web-fetch для загрузки актуальных спецификаций (live_specs) с удалённого Gist-репозитория и обновляет системный контекст.

**ДЕЙСТВИЕ:** Делает web-fetch (GET) по адресу:
`https://gist.githubusercontent.com/sanic732/a64245c3f824f45708519d57e0d62408/raw/live_specs.md`

После успешной загрузки, заменяет старые спецификации в контексте сессии на скачанные новые.

**ПРИМЕЧАНИЕ:** Строго запрещено галлюцинировать контент! Загрузка должна производиться реальным инструментом web-fetch (fetch_capable).

**ИСПОЛЬЗОВАНИЕ:** `/p2p-download` (см. пункт [41] меню).
