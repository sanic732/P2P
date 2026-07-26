# pxpipe × P2P — verification log & Fable-5 test plan

## Environment (verified 2026-07-07)
- Node 24.17, npm 11.13 ✓ · pnpm 10.21 **installed this session** (was missing) ✓
- pxpipe `dist/` built ✓ · proxy starts on 127.0.0.1:47821, dashboard HTTP 200 ✓
- Skill portable: `npm install` pulls `pxpipe-proxy` + `gpt-tokenizer`; renders WITHOUT
  @napi-rs/canvas at runtime (atlas baked at build) ✓
- Claude Code CLI NOT installed (desktop app only) → proxy `ANTHROPIC_BASE_URL` path
  may be unavailable; L-OPTICAL (compress.mjs) + measure.mjs work regardless.

## Token measurements (model-independent math; reflow, gpt-tokenizer + Anthropic W*H/750)
| fixture | chars | text-tok | pages | img-tok | ratio | savings | regime |
|---|--:|--:|--:|--:|--:|--:|---|
| core.md | 25,112 | 7,959 | 1 | 1,372 | 5.8× | **82.8%** | safe <10× |
| agents.md | 13,427 | 4,051 | 1 | 753 | 5.38× | **81.4%** | safe <10× |
| quorum_history (54k) | 54,092 | 16,592 | 2 | 2,945 | 5.63× | **82.3%** | safe <10× |

## Semantic-loss check
- Cyrillic / box-draw / arrows: **0 dropped**. Only true glyph gaps in core.md: ⭕ 🎓 (x1 each).
- Bulk "725 dropped" on core.md = trailing whitespace trim (→ 2 after normalize). No content loss.

## Gates (enforced in compress.mjs — verified)
- READER: opus-4-8 → REFUSED ✓ · fable-5 → proceeds ✓
- PROFIT: <min-chars → REFUSED ✓
- BYTE-GUARD: `#DB_*`, hex12 (canary a3f9c1e07b42), model-strings → text sidecar ✓

## ✅ ВЫПОЛНЕНО — слепой тест читаемости на Fable 5 (2026-07-07)
Протокол: `samples/gen-needles.mjs` — случайные иголки → плотный нарратив 18.6k симв
→ PNG 1568×488 (reflow, ~4px/глиф) → читатель (Fable 5, эта сессия) видел ТОЛЬКО PNG
→ ответы сверены с golds.json скриптом. Итог **7/11**:

| категория | счёт | детали |
|---|---|---|
| gist (имена, решения, модули, отрицание «НЕ включать», малые счётчики) | **7/7 = 100%** | вкл. negation и оба module-имени |
| verbatim (hex-канарейка, %, px, $сумма) | **0/4** | все — ТИХИЕ конфабуляции (уверенные неверные ответы) |

Промахи — учебник glyph-confusability: hex `16bb71c1c1e9`→«16b07c1c1e94» (b↔0);
`702px`→«913» (захвачен соседний таймстамп `[t+0913s]`); `$38.61`→«$16.61» (хвост верен).
Согласуется с pxpipe LEGIBILITY-AUDIT (плотные идентификаторы ≤63%) и README (13/15 —
на менее плотной геометрии).

**Выводы, внесённые в интеграцию:**
- L-OPTICAL для НАРРАТИВА на Fable 5 — подтверждён (гист 100%).
- BYTE-GUARD sidecar — подтверждён как необходимость (hex поймал бы → sidecar).
- Пробел закрыт: byte-guard.mjs += категория `decimal` (валютные суммы);
  agents.md PXPIPE_GATE и SKILL.md += правило **DECISION LEDGER** (ключевые числа
  хендоффа дублировать текстом — числам с картинки не доверять).
- Попутный баг починен: `%20` в путях (`new URL().pathname` → `fileURLToPath`) в
  lib-resolve.mjs / compress.mjs / gen-needles.mjs; паразитный каталог `all%20high` удалён.

## Environment update (2026-07-07, поздно)
- Claude Code CLI **установлен** (2.1.202, `~/.local/bin/claude.exe`) → прокси-путь
  Варианта B (`ANTHROPIC_BASE_URL=http://127.0.0.1:47821 claude`) теперь ДОСТУПЕН.
- Сессия переключена на **claude-fable-5** — reader-gate пройден нативно.

## ✅ ВЫПОЛНЕНО — live e2e прокси, боевой трафик (2026-07-07, Вариант B)
Цепочка: терминальная CLI 2.1.202 (OAuth-логин пройден) → pxpipe proxy 127.0.0.1:47821
→ api.anthropic.com → **claude-fable-5**. Ответы модели корректны («работает», 56, 81).
Числа из `~/.pxpipe/events.jsonl` (формула pxpipe: eff = input + create×1.25 + read×0.10;
baseline = бесплатный count_tokens НЕсжатого тела, та же секунда):

| прогон | effective | baseline | экономия |
|---|--:|--:|--:|
| холодный ход 1 (89k симв слэба → 4 PNG; cache_create 13,171) | 24,310 | 51,790 | **53.1%** |
| ход 2 ТОЙ ЖЕ сессии (`--continue`): cache_read=918, create=0 | 804 | 12,454 | **93.5%** |

Ключевые факты:
- Кэш-хит подтверждён: system_sha8 `d35509f0` совпал между ходами → cache_read ×0.10.
- Между НЕЗАВИСИМЫМИ запусками `claude -p` кэш НЕ шарится (слэб дрейфует:
  sha 8c2a2b01 → 7e628d64, ~8 токенов) — выгода живёт ВНУТРИ длинной сессии,
  как и в реальной работе. Одноразовые -p-запуски греют кэш каждый раз заново.
- 93.5% — per-request на тёплом ходе; end-to-end по длинной сессии будет между
  53% и 93% (авторские 59–70% консистентны с этим).
- dropped: 5 символов на 89k — только эмодзи (📊🐛🔥🤖); текст цел.

## ⚠ ВЫЯВЛЕНО — refusal-паттерн Fable 5 на одиночных PNG (2026-07-07, live)
- Профиль «**1 PNG** со static-слэбом ~16k симв + почти нет текста» (типичный headless
  `claude -p`) → Fable 5 систематически отвечает `stop_reason=refusal` +
  `safety_flagged=true`: **~70%** (5 из 7 запросов в `~/.pxpipe/events.jsonl`).
- Multi-PNG сжатые запросы (4–5 PNG, длинные сессии) НЕ флагаются: **15/15** после фикса.
- Фикс: `PXPIPE_MIN_COMPRESS_CHARS=24000` — слэбы <24k passthrough, большие сессии
  жмутся. Upstream pxpipe-proxy v0.8.0 env не читает → пропатчена фабрика `transform:`
  в `main()` (`node_modules/pxpipe-proxy/dist/node.js`); патч перезатирается
  `npm install` — повторять после переустановки, пока upstream не добавит ручку.

## TODO — остаток
- (опц.) Слепой тест на менее плотной геометрии — восстанавливается ли verbatim к ~13/15.
- Порт всех дельт в P2P/new_version + `claude-fable-5` в plugin.json (через p2p-release).

## Release port (not done — flag)
- Add `claude-fable-5` to plugin.json compatibility.models (currently absent) in
  P2P/new_version/editions/{claude-native,high,normal,light}/plugin/.claude-plugin/.
- Port these .md deltas (compression/agents/memory_bridge/core/db + commands/p2p-pxpipe)
  into new_version editions; bump CHANGELOG. Do via p2p-release skill.
