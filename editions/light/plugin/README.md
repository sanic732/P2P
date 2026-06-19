# P2P v8L.3 — Native Plugin (Claude Code / Cowork)

Эта папка — нативный плагин P2P v8L.3 для **Claude Code** и **Cowork**.
Даёт команды `/p2p-*` и 8 sub-агентов QUORUM «из коробки», без ручной вставки файлов.

## Содержимое

```
claude/
├── .claude/
│   ├── agents/        8 sub-агентов QUORUM (IRIS, TECTON, AXIOM, VECTOR,
│   │                  DATOS, ANON, ARCHITECTON, HELIOS)
│   ├── commands/      15 команд: /p2p, /p2p-quorum, /p2p-scope, /p2p-chain,
│   │                  /p2p-capsule, /p2p-metrics, /p2p-explore, /p2p-atlas,
│   │                  /p2p-feedback, /p2p-karpathy, /p2p-teacher,
│   │                  /p2p-verify, /p2p-download, /p2p-host, /p2p-fetch-test
│   └── settings.json  безопасные дефолты (хуки OPT-IN, выключены)
└── .claude-plugin/
    ├── plugin.json        манифест плагина (v8.3.0-L)
    └── marketplace.json   манифест маркетплейса
```

## Установка

1. **Claude Code:** укажи эту папку (`claude/`) как plugin source — она содержит
   `.claude/` и `.claude-plugin/` в корне, как ожидает Claude Code.
2. **Cowork:** drag-drop собранный `.plugin` (или папку `claude/`).
3. После подключения: набери `/p2p` — появится меню.

## Как плагин связан с движком

- Команды (`commands/`) — тонкие обёртки: показывают меню, запускают QUORUM, чек целостности.
- Агенты (`agents/`) — нативные sub-agents. На Claude/Grok QUORUM идёт через них (AGENT_PATH=LOCAL);
  на других хостах — поднимается из чанка `CORE_PLUS` (см. `../P2P/`).
- Полная логика (resolver, host-профили, техники) — в BOOT-файлах `../P2P/`. Плагин их дополняет,
  а не заменяет: для работы движка BOOT-файлы должны быть в контексте (или загружены скиллом).

## Совместимость
claude-fable-5 · claude-opus-4-8 · claude-opus-4-7 · claude-sonnet-4-6 (+ haiku-4-5, opus-4-6).
Универсально работает на 8 хостах — XML-вывод только при HOST_MODEL=claude.
