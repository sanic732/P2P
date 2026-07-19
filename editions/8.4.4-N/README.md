# 🟩 P2P 8N.4 — Normal / Universal Edition

> 🇷🇺 Русский · 🇬🇧 [English](README.en.md) · ⬆️ [Назад к выбору редакции](../../README.md) · 📖 [Расшифровка имени](../../NAMING.md)

**Версия:** 8N.4 · **Токен-бюджет:** MINIMAL ~60K · STANDARD ~120K (реком.) · FULL ~200K

> 📖 **Полная инструкция (Google Docs):** https://docs.google.com/document/d/e/2PACX-1vS2Xo8p7cEFYfrW7Lfxr2YxrbxSojmMp6-ueRgq3_9-Q-MGKeSiRUDuQmHSj1QUHXaHA3LFvYyPNI2e/pub

## Для кого
Тех, чьей модели нет среди «нативных» (GPT, DeepSeek, Qwen, Kimi, GLM, Gemini…). Самая простая в запуске.

## Чем отличается
Универсальный прелоадер без привязки к вендору. Диспетчер `!!core_v8N.md` «на лету» перестраивает синтаксис под хост: для GPT — JSON, для DeepSeek — отключает управление рассуждением, для GLM — строгий Markdown.

## Плюсы и минусы
- ✅ Работает на любом хосте; сбалансирована токены/возможности; защиты от багов G15/G18/G19/G20 под китайские флагманы.
- ⚠️ Не использует нативные фишки конкретного вендора (для этого — C для Claude, H для Grok).

## Требования к хосту
Любой из 8: GPT-5.6, DeepSeek V4, Qwen 3.6, Kimi K2.x, GLM-5.1, Gemini 3.x, MiniMax, Manus. Хост — в `_preloader.md`.

## Что нового
Поколение .3: те же 6 ON-DEMAND модулей и VERSION_COMPAT; live specs 17.06.26 (Fable 5 + Opus 4.8 в тирах и роутинге).

## Установка
Плоский набор `.md` → Projects/NotebookLM; `HOST_MODEL` в `_preloader.md`. ZIP-ассет: `p2p-normal-8N.3.zip`.

> ⚠️ Не смешивайте файлы разных редакций — архитектуры синтаксически несовместимы.
> 📊 Сравнение всех 4 редакций — [`COMPARISON.md`](../COMPARISON.md).
