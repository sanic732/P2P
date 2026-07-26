---
description: "/p2p-pxpipe — оптическая экономия токенов: прокси-режим (весь трафик) или разовое сжатие хендоффа."
argument-hint: "[on|off|status|measure <file>]"
source_id: CMD_PXPIPE_V8C
version: 8.4.6-C
module_type: command
scope: /p2p-pxpipe — включить/выключить прокси оптического сжатия (pxpipe) или измерить выгоду по файлу.
---
# /p2p-pxpipe — Оптическая экономия токенов (pxpipe)

**Что делает:** управляет двумя слоями оптического сжатия. Токен-выгода — математика
пикселей (не зависит от модели); *читаемость* требует reader-модели (**Fable 5**).

**Использование:**
```
/p2p-pxpipe on              → инструкция запуска ПРОКСИ (Tier A, максимальный ROI 65–70%)
/p2p-pxpipe off             → как выключить прокси / снять PXPIPE_PROXY_ACTIVE
/p2p-pxpipe status          → активен ли прокси, поддерживается ли текущая модель
/p2p-pxpipe measure <file>  → замер токенайзером (text vs image, ratio, savings %) БЕЗ отправки
```

**Алгоритм (`on` — прокси):**
1. GATE: ENV=Code и target_model == claude-fable-5. Иначе → предупредить,
   что имиджинг на этой модели читается плохо (Opus 0/15 verbatim hex) → предложить только `measure`.
2. Установить один раз: `cd .claude/skills/pxpipe && npm install` — ставит готовый
   пакет `pxpipe-proxy` (+ gpt-tokenizer); сборка из исходников не нужна.
3. Запустить: `PXPIPE_MIN_COMPRESS_CHARS=24000 npx pxpipe-proxy` → слушает
   `127.0.0.1:47821`, дашборд там же. Порог 24000 обязателен: одиночные PNG на мелких
   слэбах (~16k, headless `claude -p`) систематически ловят safety-refusal Fable 5.
   ⚠ pxpipe-proxy v0.8.0 env не читает — нужен патч transform-фабрики в `dist/node.js`
   (перезатирается `npm install`); см. docs/PXPIPE_GUIDE.md.
4. Указать клиенту: `ANTHROPIC_BASE_URL=http://127.0.0.1:47821`.
   ⚠ Если Claude Code CLI не установлен (только desktop-приложение) — env
   ANTHROPIC_BASE_URL приложением не подхватывается; тогда прокси-режим недоступен,
   используй разовое сжатие L-OPTICAL (compress.mjs) и `measure`.
5. Выставить флаг `PXPIPE_PROXY_ACTIVE=1` → это ГЛУШИТ L-OPTICAL/PXPIPE_GATE
   (прокси уже жмёт весь трафик; двойной имиджинг не нужен).

**Что жмёт прокси:** статический system-prompt + tool docs (кэшируется, амортизация с 2-го хода),
старые tool_result и `<system-reminder>`. Свежие ходы и вывод модели — не трогает.
Всё вне allowlist моделей проходит байт-в-байт.

**`measure <file>`:** `node .claude/skills/pxpipe/measure.mjs <file> --reflow` — печатает
text-tokens, image-tokens, ratio, savings %, режим точности (<10× ≈ 97%, DeepSeek-OCR).

Связано: `compression.md` → L-OPTICAL (разовое сжатие) · `agents.md` → PXPIPE_GATE (хендофф).

========================================
FILE_META
========================================
id: CMD_PXPIPE_V8C
type: command
edition: CLAUDE_NATIVE
========================================
