# P2P v8L.3 — Установка (TL;DR)

## Способ 1 — Native plugin (Claude Code / Cowork)
1. Распакуй `p2p-v8l3.zip`.
2. Укажи папку **`claude/`** как plugin source (см. `claude/README.md`).
3. Готово: команды `/p2p`, `/p2p-quorum`, `/host`, `/p2p-verify` + 8 агентов.

## Способ 2 — Manual (любой хост: chat / API / Studio)
1. Склей 4 BOOT-файла из папки `P2P/`:
   ```bash
   cat P2P/_preloader_v8L.md P2P/_index_v8L.md "P2P/!!core_v8L.md" "P2P/!!db_v8L.md" > boot_v8L.md
   ```
2. Вставь `boot_v8L.md` в контекст.
3. Система спросит хост → выбери (claude/gemini/gpt/grok/deepseek/qwen/kimi/glm).
4. Напиши `СТАРТ`. Арсенал подтянется по триггеру (если хост умеет web-fetch).

## Требования
- Для полного арсенала — хост с web-fetch (claude/gemini/grok/gpt/kimi).
- Без fetch → режим `LITE_ONLY` (базовые техники работают).

## Проверка целостности
```bash
cd P2P && bash verify_v8L.sh        # 11/11 PASS
```

Подробно: `docs/README.md`, `docs/ASSEMBLY_GUIDE.md`, `docs/HOST_GUIDE.md`.
