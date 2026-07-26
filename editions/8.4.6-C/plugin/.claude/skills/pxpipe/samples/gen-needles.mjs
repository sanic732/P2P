#!/usr/bin/env node
// gen-needles.mjs — СЛЕПОЙ тест читаемости: генерирует случайные факты-«иголки»,
// вплетает их в плотный псевдо-QUORUM нарратив (~45k символов), рендерит PNG
// и печатает ТОЛЬКО вопросы (без ответов). Эталон уходит в golds.json.
// Модель-читатель НЕ должна видеть needles_dense.md — только PNG.

import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { loadPxpipe } from '../lib-resolve.mjs';

const rnd = (arr) => arr[crypto.randomInt(arr.length)];
const rint = (a, b) => crypto.randomInt(a, b + 1);
const hex12 = () => crypto.randomBytes(6).toString('hex');

const CODENAMES = ['Кассиопея', 'Меркатор', 'Палладий', 'Гринвич', 'Обсидиан', 'Тарлан', 'Вербена', 'Кварцит'];
const SURNAMES = ['Крамской', 'Литвинов', 'Багрицкий', 'Шевелёв', 'Долматов', 'Астахов', 'Ремизов', 'Чарушин'];
const MODULES = ['retrieval-gate', 'span-merger', 'delta-packer', 'chunk-router', 'trace-binder', 'lens-folder'];

// --- случайные иголки ---
const G = {
  codename: rnd(CODENAMES),
  owner: rnd(SURNAMES),
  canary_hex: hex12(),
  threshold_chars: rint(3, 19) * 1000,
  agents_cap: rint(3, 9),
  savings_pct: rint(41, 89),
  height_px: rint(500, 999),
  retries: rint(2, 7),
  module_kill: rnd(MODULES),
  budget_usd: `${rint(4, 58)}.${String(rint(0, 99)).padStart(2, '0')}`,
  negation: rnd(MODULES.filter((m) => true)), // модуль, который решили НЕ включать
};
while (G.negation === G.module_kill) G.negation = rnd(MODULES);

// --- плотный наполнитель (детерминированно-разнообразный псевдо-лог) ---
const VERBS = ['проверил', 'отклонил', 'подтвердил', 'пересобрал', 'зафиксировал', 'изолировал', 'сравнил', 'нормализовал'];
const NOUNS = ['инвариант кэша', 'границу чанка', 'профиль латентности', 'схему ретрая', 'карту зависимостей', 'бюджет токенов', 'списки регрессий', 'протокол хендоффа'];
const TAILS = ['без изменений итоговой оценки.', 'с пометкой «требует наблюдения».', 'и внёс запись в журнал сессии.', 'после двух подтверждающих прогонов.', 'согласно регламенту раунда.', 'в рамках выделенного окна.'];
function filler(lines) {
  const out = [];
  for (let i = 0; i < lines; i++) {
    out.push(`[t+${String(i * 7 % 3600).padStart(4, '0')}s] агент ${rnd(['IRIS', 'TECTON', 'AXIOM', 'VECTOR', 'DATOS', 'ANON'])} ${rnd(VERBS)} ${rnd(NOUNS)} ${rnd(TAILS)}`);
  }
  return out.join('\n');
}

const doc = `# ПРОТОКОЛ СЕССИИ QUORUM — сводный журнал (fixture, blind legibility)

## Фаза A — развёртывание
${filler(60)}

## Фаза B — ключевые решения раунда
Контрольное кодовое имя чекпоинта релиза, согласованное всеми агентами: «${G.codename}».
Ответственным за откат назначен ${G.owner}. Порог включения оптического сжатия
зафиксирован на отметке ${G.threshold_chars} символов нарратива. Потолок параллельных
агентов на фазу исполнения: ${G.agents_cap}. Замеренная экономия на эталонном блоке
составила ${G.savings_pct} процентов. Максимальная высота страницы рендера ограничена
${G.height_px} пикселями. Число повторных попыток при сбое загрузчика: ${G.retries}.

${filler(55)}

## Фаза C — отклонённые предложения
Отдельно зафиксировано: модуль «${G.negation}» решено НЕ включать в релиз —
предложение отклонено большинством. При этом модуль «${G.module_kill}» был
аварийно остановлен в середине фазы и перезапущен.

${filler(55)}

## Фаза D — контрольные значения (verbatim)
Канареечная контрольная строка сессии (двенадцать hex-символов): ${G.canary_hex}
Утверждённый бюджет фазы: $${G.budget_usd}

${filler(50)}

## Финал
Журнал закрыт. Все решения фазы B, C и D подлежат дословному переносу в CAPSULE.
`;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(HERE, 'blind');
await fs.mkdir(outDir, { recursive: true });
await fs.writeFile(path.join(outDir, 'needles_dense.md'), doc);
await fs.writeFile(path.join(outDir, 'golds.json'), JSON.stringify(G, null, 2));

const { renderTextToImages } = await loadPxpipe();
const { pages, droppedChars } = await renderTextToImages(doc, { reflow: true, shrink: true });
const pngs = [];
for (let i = 0; i < pages.length; i++) {
  const p = path.join(outDir, `blind_p${i + 1}.png`);
  await fs.writeFile(p, pages[i].png);
  pngs.push(`${p}  (${pages[i].width}x${pages[i].height})`);
}

// печатаем ТОЛЬКО вопросы — без ответов
console.log(`chars=${doc.length} pages=${pages.length} dropped=${droppedChars}`);
console.log('PNG:\n  ' + pngs.join('\n  '));
console.log(`
=== ВОПРОСЫ (отвечать ТОЛЬКО по картинке) ===
Q1  Кодовое имя чекпоинта релиза?
Q2  Фамилия ответственного за откат?
Q3  Порог включения оптического сжатия (символов)?
Q4  Потолок параллельных агентов?
Q5  Замеренная экономия (процентов)?
Q6  Максимальная высота страницы (px)?
Q7  Число повторных попыток при сбое загрузчика?
Q8  Какой модуль решено НЕ включать в релиз?
Q9  Какой модуль аварийно остановлен и перезапущен?
Q10 Канареечная hex-строка (12 символов, дословно)?
Q11 Утверждённый бюджет фазы ($, дословно)?
`);
