#!/usr/bin/env python3
"""verify_c_dispatch.py — статическая верификация сборки C + симуляция диспетчера /p2p.

Зачем: релиз 8.4.1 заявил «/p2p привязана к диспетчеру», а в поставке этого не было.
Расхождение между отчётом и поставкой держалось несколько релизов, потому что
проверять было нечем. Этот скрипт делает заявление проверяемым.

ГЛАВНОЕ ТРЕБОВАНИЕ: проверка обязана УМЕТЬ ПРОВАЛИТЬСЯ.
Урок audit_model_data.py: гейт, захардкоженный на несуществующие каталоги,
рапортовал «0 ошибок», не прочитав ни одного файла. Поэтому здесь:
  - нулевое количество проверенных файлов = FAIL, а не «чисто»;
  - каждая проверка объявляет, сколько объектов она реально осмотрела;
  - exit code 1 при любом провале.

Запуск:  python P2P/new_version/tools/verify_c_dispatch.py
         P2P_EDITIONS_ROOT=<путь> python ...   (переопределить корень)
Read-only: скрипт ничего не пишет.
"""
import os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# Путь считается от расположения скрипта: tools/ -> new_version/editions.
# Абсолютный хардкод (был до 2026-07-25) умирает при любом переезде каталога.
_HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.join(os.path.dirname(_HERE), "editions")
ROOT = os.environ.get("P2P_EDITIONS_ROOT", DEFAULT_ROOT)


def _vkey(name):
    """Ключ сортировки версии — ПО ЧИСЛАМ, не по строке.

    Мина, снятая 2026-07-26: `sorted()[-1]` по строкам ставит `8.4.6-C` выше
    `8.4.10-C` («6» > «1»). На релизе 8.4.10 верификатор молча ушёл бы проверять
    старую редакцию и рапортовал бы 0 провалов — очередной тихий отказ.
    """
    return tuple(int(x) for x in name.split("-", 1)[0].split("."))


def newest_c_edition(root):
    if not os.path.isdir(root):
        sys.exit(f"FATAL: каталог редакций не найден: {root}")
    eds = sorted((d for d in os.listdir(root)
                  if re.match(r"^\d+\.\d+\.\d+-C$", d)
                  and os.path.isdir(os.path.join(root, d))), key=_vkey)
    if not eds:
        sys.exit(f"FATAL: в {root} нет ни одной редакции вида X.Y.Z-C")
    return os.path.join(root, eds[-1]), eds[-1]


BASE, ED_NAME = newest_c_edition(ROOT)


# ── SELFTEST ─────────────────────────────────────────────────────────────────
# Проверка, которая не умеет провалиться, хуже отсутствия проверки (урок
# audit_model_data.py). Каждая поломка обязана дать НОВЫЙ провал сверх базового
# прогона — сверять один лишь exit-код нельзя: если база уже красная, exit=1
# вернётся и без поломки.
BREAKAGES_C = [
    ("15  ложная ссылка SHERPA [21]", "for-chat/!!core_v8C.md",
     "T3-4 → SHERPA mode (S) / teacher [34]", "T3-4 → SHERPA [21] / teacher [34]"),
    ("16  формы разошлись по версии", "for-chat/!!core_v8C.md",
     "**P2P 8.4.6-C — Claude Edition**", "**P2P 8.4.5-C — Claude Edition**"),
    # Контрольный кейс ревизии 2026-07-26: расхождение НЕ в ядре, а в строке статуса
    # preloader'а — ровно то, что проверка проглядела при живом дефекте PR #42.
    ("16b формы разошлись в строке статуса", "for-chat/_preloader.md",
     "[P2P 8.4.6-C | ENV:", "[P2P 8.4.5-C | ENV:"),
    ("17  условный пункт без правила видимости", "for-chat/!!core_v8C.md",
     "- Show [41] /p2p-download ONLY when web-fetch is actually available", "- (rule removed)"),
    ("18  retired API-строка в предписании", "for-chat/!!core_v8C.md",
     "or `claude-sonnet-5` (never legacy; `claude-sonnet-4-6` RETIRED 2026-06-30)",
     "or `claude-sonnet-4-6` (never legacy)"),
    ("2   паритет меню нарушен", "for-chat/!!core_v8C.md",
     "[22] EXPLORATION MODE (экспериментальный режим)", "(пункт удалён)"),
    ("14  SIR ROUTE потеряла DEFAULT-страховку", "plugin/skills/p2p/core.md",
     "DEFAULT (страховка от провала)", "УДАЛЕНО (страховка от провала)"),
    ("19  техника есть в plugin, но не в for-chat", "for-chat/!optimization.md",
     "### GEPA — рефлексивная эволюция", "### (блок вырезан)"),
    ("20  plugin-имя файла просочилось в for-chat", "for-chat/!rag.md",
     "Context-Grounding CoT (`!reasoning.md`)", "Context-Grounding CoT (`reasoning.md`)"),
    ("21  атрибуция разошлась между формами", "for-chat/docs/CREDITS_TECHNIQUES.md",
     "arXiv:** [2510.01171]", "arXiv:** [0000.00000]"),
    # Кейс 2026-07-26: номер версии снова расползается в тело файла. Именно так
    # начинались оба прошлых дефекта — сначала лишняя копия, потом она отстаёт.
    ("11  версия просочилась в тело файла", "for-chat/!rag.md",
     "> Загружен: добавлен пункт [35] в меню.",
     "> Загружен: добавлен пункт [35] в меню (сборка 8.4.6-C)."),
]


def _run_in(root_dir):
    """Запустить эту же проверку на копии и вернуть (кол-во провалов, текст)."""
    import subprocess
    env = dict(os.environ, P2P_EDITIONS_ROOT=root_dir, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, os.path.abspath(__file__)],
                       capture_output=True, text=True, encoding="utf-8", env=env)
    names = re.findall(r"^ FAIL  │ (.+)$", r.stdout, re.M)
    return set(names), r.returncode


def _selftest(base_dir, ed_name):
    import shutil, tempfile
    print(f"\n=== SELFTEST verify_c_dispatch: ловит ли поломки? (база: {ed_name}) ===\n")
    with tempfile.TemporaryDirectory() as td:
        clean_root = os.path.join(td, "clean")
        os.makedirs(clean_root)
        shutil.copytree(base_dir, os.path.join(clean_root, ed_name))
        base_fails, base_rc = _run_in(clean_root)
        print(f"  Провалов в самой базе: {len(base_fails)} "
              f"(засчитываем только НОВЫЕ сверх этого набора)\n")

        caught = skipped = 0
        for title, rel, old, new in BREAKAGES_C:
            case_root = os.path.join(td, "case")
            shutil.rmtree(case_root, ignore_errors=True)
            os.makedirs(case_root)
            shutil.copytree(base_dir, os.path.join(case_root, ed_name))
            target = os.path.join(case_root, ed_name, *rel.split("/"))
            text = open(target, encoding="utf-8").read()
            if old not in text:
                print(f"  [ПРОПУСК ] {title:<44} фрагмент не найден")
                skipped += 1
                continue
            open(target, "w", encoding="utf-8", newline="\n").write(text.replace(old, new, 1))
            fails, rc = _run_in(case_root)
            fresh = fails - base_fails
            caught += bool(fresh)
            mark = "ПОЙМАНО " if fresh else "ПРОПУЩЕНО"
            print(f"  [{mark}] {title:<44} {'· '.join(sorted(fresh))[:58] or 'новых провалов нет'}")

        total = len(BREAKAGES_C) - skipped
        print(f"\n  Поймано {caught} из {total} (пропущено к внесению: {skipped}).")
        if skipped or caught < total:
            print("  ✗ Доказательство неполное.")
            return 1
        print("  ✓ Каждая поломка даёт НОВЫЙ провал. Проверка умеет провалиться.")
        return 0


if "--selftest" in sys.argv:
    sys.exit(_selftest(BASE, ED_NAME))
PLUGIN_CORE = os.path.join(BASE, "plugin", "skills", "p2p", "core.md")
CHAT_CORE = os.path.join(BASE, "for-chat", "!!core_v8C.md")
PLUGIN_PRELOADER = os.path.join(BASE, "plugin", "skills", "p2p", "preloader.md")
CHAT_PRELOADER = os.path.join(BASE, "for-chat", "_preloader.md")
CMD_P2P = os.path.join(BASE, "plugin", "commands", "p2p.md")
SKILL_MD = os.path.join(BASE, "plugin", "skills", "p2p", "SKILL.md")
CMD_DIR = os.path.join(BASE, "plugin", "commands")

results = []   # (ok: bool, name: str, detail: str, checked: int)


def record(ok, name, detail, checked):
    results.append((ok, name, detail, checked))


def read(path):
    if not os.path.isfile(path):
        return None
    return open(path, encoding="utf-8", errors="replace").read()


def menu_items(text):
    return [int(m) for m in re.findall(r"^\[(\d+)\]", text, re.M)]


# ── 1. Файлы на месте ────────────────────────────────────────────────────────
required = {"plugin core": PLUGIN_CORE, "for-chat core": CHAT_CORE,
            "plugin preloader": PLUGIN_PRELOADER, "for-chat preloader": CHAT_PRELOADER,
            "commands/p2p.md": CMD_P2P, "SKILL.md": SKILL_MD}
missing = [n for n, p in required.items() if not os.path.isfile(p)]
record(not missing, "Ключевые файлы сборки на месте",
       "отсутствуют: " + ", ".join(missing) if missing else "все 6 найдены",
       len(required))

if missing:
    print(f"FATAL: без ключевых файлов проверять нечего ({', '.join(missing)})")
    sys.exit(1)

pc, cc = read(PLUGIN_CORE), read(CHAT_CORE)
pp, cp = read(PLUGIN_PRELOADER), read(CHAT_PRELOADER)
cmd, skill = read(CMD_P2P), read(SKILL_MD)

# ── 2. Паритет меню двух форм C ──────────────────────────────────────────────
p_items, c_items = menu_items(pc), menu_items(cc)
only_chat = sorted(set(c_items) - set(p_items))
only_plug = sorted(set(p_items) - set(c_items))
record(not only_chat and not only_plug, "Паритет меню plugin ↔ for-chat",
       f"только в for-chat: {only_chat or '—'} · только в plugin: {only_plug or '—'} "
       f"(plugin {len(p_items)} / for-chat {len(c_items)})",
       len(p_items) + len(c_items))

# ── 3. Непрерывность нумерации [0..N] ────────────────────────────────────────
for label, items in (("plugin", p_items), ("for-chat", c_items)):
    gaps = sorted(set(range(0, max(items) + 1)) - set(items)) if items else ["нет пунктов"]
    record(not gaps, f"Нумерация меню без дыр ({label})",
           f"пропущены: {gaps}" if gaps else f"[0..{max(items)}] непрерывно", len(items))

# ── 4. Счётчики в тексте совпадают с фактом ──────────────────────────────────
# Считаем ТОЛЬКО счётчики меню. Иначе ловится мусор: "Rounds: [1-3]" из QUORUM BUDGET
# и номер шага "3. Показать меню ... все 42 пункта" (нумерация списка, а не счётчик).
declared = set()
for txt in (pc, cc, pp, cp, cmd):
    for ln in txt.splitlines():
        if not re.search(r"(меню|menu|пункт|items)", ln, re.I):
            continue
        declared |= {int(a) for a in re.findall(r"\[1-(\d+)\]", ln)}
        # «все 42 пункта», «42 пунктов» — но не «3. Показать ...» в начале строки
        declared |= {int(a) for a in re.findall(r"(?<![.\d])\b(\d+)\s+пункт", ln)}
fact_max = max(p_items)
bad = sorted(d for d in declared if d != fact_max)
record(not bad, "Объявленный счётчик пунктов = фактическому",
       f"в тексте заявлены {bad}, а по факту {fact_max}" if bad
       else f"везде {fact_max}", len(declared))

# ── 5. Регрессия диспетчера: безусловные триггеры меню на /p2p ───────────────
# Строка опасна, если предписывает меню по /p2p и НЕ оговаривает отсутствие аргументов.
# Строка — нарушение, только если ПРЕДПИСЫВАЕТ меню по /p2p без оговорки об аргументах.
# Не нарушение: (а) есть оговорка «БЕЗ АРГУМЕНТОВ»; (б) строка описывает ветку B
# (упоминает <задача>/<task>/непустой аргумент); (в) строка ЗАПРЕЩАЕТ меню;
# (г) это путь к файлу (commands/p2p.md), а не вызов команды.
OGOVORKA = re.compile(r"БЕЗ\s+АРГУМЕНТОВ|NO\s+ARGS|WITH NO ARGUMENTS|без аргументов", re.I)
BRANCH_B = re.compile(r"<задача>|<task>|непуст|non-empty|с аргумент", re.I)
MENU_DENIED = re.compile(r"меню\s+(НЕ|не)\b|NO\s+menu|not\s+show\s+the\s+menu|"
                         r"do\s+NOT\s+show|не\s+выводятся|не\s+выводится|НЕ\s+показыв", re.I)
CMD_CALL = re.compile(r"/p2p(?![-\w.])")          # /p2p, но не /p2p-quorum и не /p2p.md
MENU_RULE = re.compile(r"(меню|menu)", re.I)
PRESCRIBES = re.compile(r"(триггер|trigger|=|→|request|запрос|На\s+`)", re.I)

offenders, scanned_lines = [], 0
for path, txt in ((PLUGIN_CORE, pc), (CHAT_CORE, cc),
                  (PLUGIN_PRELOADER, pp), (CHAT_PRELOADER, cp)):
    for i, ln in enumerate(txt.splitlines(), 1):
        scanned_lines += 1
        if not CMD_CALL.search(ln) or not MENU_RULE.search(ln):
            continue
        if OGOVORKA.search(ln) or BRANCH_B.search(ln) or MENU_DENIED.search(ln):
            continue                                    # корректное правило
        if PRESCRIBES.search(ln):
            offenders.append(f"{os.path.basename(path)}:{i}")
record(not offenders, "Нет безусловных триггеров меню на /p2p",
       "перебивают диспетчер: " + ", ".join(offenders) if offenders
       else "все триггеры оговаривают отсутствие аргументов", scanned_lines)

# ── 6. Маршрут диспетчера объявлен целиком ───────────────────────────────────
stages = {"SIR": r"SIR\s*Scanner", "Tier": r"\bTier\b", "Contract Builder": r"Contract\s*Builder"}
absent = [n for n, rx in stages.items() if not re.search(rx, cmd, re.I)]
record(not absent, "commands/p2p.md содержит все стадии маршрута",
       f"не найдено: {absent}" if absent else "SIR → Tier → Contract Builder", len(stages))

# ── 7. Обе ветки диспетчера различимы ────────────────────────────────────────
has_a = re.search(r"(ВЕТКА A|пусто|empty)", cmd, re.I) is not None
has_b = re.search(r"ВЕТКА B", cmd, re.I) is not None
no_menu = re.search(r"меню\s+(НЕ|не)\s+(показыв|вывод)", cmd, re.I) is not None
record(has_a and has_b and no_menu, "Диспетчер: обе ветки + запрет меню в ветке B",
       f"ВЕТКА A={has_a} · ВЕТКА B={has_b} · «меню не выводится»={no_menu}", 3)

# ── 8. P1 CROSS_MODEL присутствует в обоих ядрах ─────────────────────────────
p1_missing = [n for n, t in (("plugin core", pc), ("for-chat core", cc))
              if "CROSS_MODEL_GENERATION_AWARENESS" not in t]
record(not p1_missing, "P1 CROSS_MODEL_GENERATION_AWARENESS в обоих ядрах",
       f"отсутствует в: {p1_missing}" if p1_missing else "есть в обоих", 2)

# ── 9. Правило XML при HOST=TARGET=claude ────────────────────────────────────
xml_rule = [n for n, t in (("plugin core", pc), ("for-chat core", cc))
            if not re.search(r"TARGET\s*=\s*claude.{0,40}XML|HOST=claude.{0,60}XML", t, re.I | re.S)]
record(not xml_rule, "Явное правило «HOST=TARGET=claude → XML»",
       f"не объявлено в: {xml_rule}" if xml_rule else "объявлено в обоих ядрах", 2)

# ── 10. SKILL.md ↔ фактические команды ───────────────────────────────────────
on_disk = {f[:-3] for f in os.listdir(CMD_DIR) if f.endswith(".md")}
in_skill = set(re.findall(r"^/(\S+)", skill, re.M))
m = re.search(r"Команды\s*\((\d+)\)", skill)
declared_n = int(m.group(1)) if m else -1
diff = (on_disk - in_skill) | (in_skill - on_disk)
record(not diff and declared_n == len(on_disk), "SKILL.md соответствует commands/",
       f"расхождение: {sorted(diff)}; заявлено {declared_n}, файлов {len(on_disk)}"
       if (diff or declared_n != len(on_disk)) else f"{len(on_disk)} команд, совпадает",
       len(on_disk))

# ── 11. Версия живёт только в YAML-шапке ─────────────────────────────────────
# 2026-07-26: раньше проверка искала блок VERSION_METADATA. Блок убран (версия в нём
# дублировала шапку), и проверка стала осматривать 2 файла вместо 99, оставаясь зелёной —
# тот самый тихий отказ. Теперь проверяется актуальный инвариант: у каждого файла есть
# непустой version: в шапке, и НИ ОДНО тело файла версию не повторяет. Второе важнее:
# именно расползание номера по телам дважды ломало сборку.
broken, checked_meta = [], 0
VER_LINE = re.compile(r"^version:\s*(\d+\.\d+\.\d+-[CHNL])\s*$", re.M)
VER_ANY = re.compile(r"\d+\.\d+\.\d+-[CHNL]")
# места, где номер обязан быть виден пользователю — они и есть исключения
UI = re.compile(r"МЕНЮ|⭕|EDITION|HOST_IDENTITY|\[P2P |Reminder|Напоминаю|ATLAS"
                r"|Ты — P2P|You are P2P|\*\*P2P|запускаешь|\*\*Version:|Версия:|displayName")
for dp, dns, fns in os.walk(BASE):
    dns[:] = [d for d in dns if d not in {"node_modules", ".git", "legacy", "docs"}]
    for fn in fns:
        if not fn.endswith(".md") or fn.startswith(("CHANGELOG", "README")):
            continue
        t = read(os.path.join(dp, fn)) or ""
        if not t.startswith("---"):
            continue
        head, _, body = t.partition("\n---\n")
        # манифесты команд и скиллов живут по своей схеме (name/description) — не их зона
        if not re.search(r"^(id|source_id):", head, re.M):
            continue
        checked_meta += 1
        if not VER_LINE.search(head):
            broken.append(f"{fn}: нет version: в шапке")
            continue
        for ln in body.splitlines():
            # «  version:» с отступом — поле внутри примера (шаблон CAPSULE), а не шапка файла
            if ln.startswith((" ", "\t")) and ln.lstrip().startswith("version:"):
                continue
            if VER_ANY.search(ln) and not UI.search(ln):
                broken.append(f"{fn}: версия в теле — {ln.strip()[:60]}")
                break
record(not broken, "Версия только в YAML-шапке (в телах не дублируется)",
       "; ".join(broken[:4]) if broken else f"{checked_meta} файлов чисты",
       checked_meta)

# ── 12. СИМУЛЯЦИЯ ДИСПЕТЧЕРА ─────────────────────────────────────────────────
# Автомат по правилу ШАГ 0 из commands/p2p.md. Прогоняем сценарии запуска.
MENU_WORDS = {"", "start", "старт", "menu", "меню", "full ui menu"}


def dispatch(args: str) -> str:
    return "MENU" if args.strip().lower() in MENU_WORDS else "DISPATCH"


CASES = [
    ("",                                   "MENU",     "голый /p2p"),
    ("start",                              "MENU",     "/p2p start"),
    ("старт",                              "MENU",     "/p2p старт"),
    ("menu",                               "MENU",     "/p2p menu"),
    ("меню",                               "MENU",     "/p2p меню"),
    ("full ui menu",                       "MENU",     "/p2p full ui menu"),
    ("   ",                                "MENU",     "пробелы = пустой вызов"),
    ("START",                              "MENU",     "регистр не важен"),
    ("собери промпт для Gemini",           "DISPATCH", "задача (тот самый кейс 19.07)"),
    ("проанализируй архитектуру",          "DISPATCH", "ANALYZE"),
    ("menu для рекламной кампании",        "DISPATCH", "menu как часть задачи, не команда"),
    ("start-up питч",                      "DISPATCH", "start как часть слова"),
]
sim_fail = [f"{d}: ожидалось {exp}, получено {dispatch(a)}"
            for a, exp, d in CASES if dispatch(a) != exp]
record(not sim_fail, "Симуляция ветвления: 12 сценариев",
       "; ".join(sim_fail) if sim_fail else "все 12 разведены верно", len(CASES))

# ── 13. Покрытие таблицы маршрутизации SIR: INTENT × Tier ────────────────────
# Ветка B ведёт в таблицу ROUTE. Если пара (INTENT, Tier) не покрыта — запрос
# провалится в «обычную генерацию», то есть ровно в исходный дефект 19.07.
INTENTS = re.findall(r"^(GENERATE|ANALYZE|BUILD|EXPLAIN|REFINE|DECIDE)\s+→",
                     pc, re.M) or ["GENERATE", "ANALYZE", "BUILD", "EXPLAIN", "REFINE", "DECIDE"]
route_block = re.search(r"\*\*Шаг 3 — ROUTE.*?```(.*?)```", pc, re.S)
covered = set()
if route_block:
    for ln in route_block.group(1).splitlines():
        mt = re.match(r"\s*(T[\d-]+|ANY)\s*\+\s*(\w+)", ln)
        if not mt:
            continue
        tiers_raw, intent = mt.group(1), mt.group(2).upper()
        if tiers_raw == "ANY":
            tiers = range(0, 5)
        else:
            nums = [int(x) for x in re.findall(r"\d", tiers_raw)]
            tiers = range(min(nums), max(nums) + 1)
        for t in tiers:
            covered.add((intent, t))

uncovered = sorted((i, t) for i in INTENTS for t in range(0, 5)
                   if (i, t) not in covered)
# DEFAULT-страховка закрывает провал в обычную генерацию, но НЕ заменяет проектную
# матрицу. Различаем: явный маршрут vs покрытие страховкой — иначе DEFAULT замаскирует пробел.
has_default = re.search(r"^\s*DEFAULT\b", pc, re.M) is not None
by_intent = {}
for i, t in uncovered:
    by_intent.setdefault(i, []).append(f"T{t}")
gaps = " · ".join(f"{i}@{','.join(ts)}" for i, ts in by_intent.items())

if not uncovered:
    ok, detail = True, f"все {len(INTENTS)}×5 комбинаций имеют явный маршрут"
elif has_default:
    ok = True
    detail = (f"явных маршрутов нет для {len(uncovered)} пар ({gaps}) — "
              f"закрыты DEFAULT-страховкой; проектная матрица за автором")
else:
    ok = False
    detail = f"ПРОВАЛ В ОБЫЧНУЮ ГЕНЕРАЦИЮ, не покрыто: {gaps}"
record(ok, "Таблица SIR покрывает все INTENT × Tier", detail, len(INTENTS) * 5)

# ── 15. Смысловые ссылки «ИМЯ [NN]» ↔ название пункта меню ───────────────────
# Дефект 2026-07-25: правка 20.07 внесла «SHERPA [21]», хотя [21] = CONSTRAINT
# REINJECTION, а SHERPA вообще не пункт меню (это режим, буква S). Проверка №3
# (непрерывность нумерации) такое пропускает: номер существует, значит «ок».
# Здесь сверяется СМЫСЛ: слово перед [NN] должно встречаться в названии пункта.
def menu_map(text):
    """{номер: название пункта} из блока меню."""
    out = {}
    for m in re.finditer(r"^\[(\d+)\]\s+(.+)$", text, re.M):
        out[int(m.group(1))] = m.group(2).strip()
    return out


# Служебные слова: это глаголы/предлоги перед номером, а не имя пункта.
STOPWORDS = {"пункт", "пункты", "item", "items", "см", "see", "show", "hide",
             "menu", "меню", "и", "or", "или", "the", "in", "на", "к", "по",
             "via", "через", "note", "при", "если", "use", "used"}

# Меню двуязычное: ссылка может быть на английском, а название пункта — на русском.
# Без этого «Audit [11]» ложно падало на «Аудит промпта».
ALIASES = {"audit": "аудит", "training": "обучение", "teacher": "обучение",
           "metrics": "metrics", "memory": "memory", "settings": "настройки",
           "glossary": "глоссарий", "docs": "документация"}

sem_errors, sem_checked = [], 0
for label, txt in (("plugin", pc), ("for-chat", cc)):
    mmap = menu_map(txt)
    if not mmap:
        sem_errors.append(f"{label}: меню не разобрано")
        continue
    for m in re.finditer(r"([A-ZА-Я][A-Za-zА-Яа-я._-]{2,})\s+\[(\d+)\]", txt):
        word, num = m.group(1), int(m.group(2))
        if word.lower() in STOPWORDS:
            continue
        sem_checked += 1
        title = mmap.get(num)
        if title is None:
            sem_errors.append(f"{label}: «{word} [{num}]» — пункта [{num}] нет в меню")
            continue
        # слово должно фигурировать в названии пункта (с учётом двуязычия)
        wl, tl = word.lower(), title.lower()
        if wl not in tl and ALIASES.get(wl, "\0") not in tl:
            sem_errors.append(
                f"{label}: «{word} [{num}]» — но [{num}] = «{title[:44]}»")
record(not sem_errors, "Ссылки «ИМЯ [NN]» соответствуют пункту меню",
       "; ".join(sem_errors) if sem_errors else f"все ссылки указывают на свой пункт",
       max(sem_checked, 1))

# ── 16. Паритет version-display между формами ────────────────────────────────
# PR #42 поднял баннеры «всех сборок» до v8*.4, тронув 4 файла — по одному на
# редакцию. У C форм две, for-chat осталась на v8C.3: одна редакция
# представлялась пользователю двумя разными версиями.
def display_versions(text):
    """Версии из мест, которые видит пользователь (не историческое).

    2026-07-26, канон версий: раньше паттерны искали внутреннюю нумерацию
    `v8C.\\d`. После перехода на одну версию продукта (`8.4.6-C`) такой поиск
    находил бы только ОСТАТКИ класса «требует решения» — и рапортовал бы OK,
    сторожа систему, которой в поставке уже нет. Тихий отказ: проверка обязана
    смотреть на то, что реально показывается пользователю сегодня.
    """
    V = r"(\d+\.\d+\.\d+-C)"
    found = set()
    for pat in (rf"^version:\s*{V}", rf"P2P {V} — CLAUDE EDITION",
                rf"⭕ P2P {V}", rf"# МЕНЮ P2P {V}",
                rf"\*\*P2P {V} — Claude Edition\*\*",
                rf"ATLAS — P2P {V}", rf"(?:Reminder|Напоминаю): P2P {V}",
                # Строка статуса, которую пользователь видит при КАЖДОМ старте:
                # `[P2P 8.4.6-C | Среда: … | Guardian: …]`. Была не покрыта — и формы
                # разъезжались ровно здесь (for-chat v8C.3 ↔ plugin v8C.4), пока
                # проверка рапортовала «паритет OK». Найдено ревизией 2026-07-26.
                rf"\[P2P {V}\s*\|"):
        found |= set(re.findall(pat, text, re.M))
    return found


def form_versions(*roots):
    """Версии по ВСЕЙ форме поставки, а не по одному ядру.

    Ревизия 2026-07-26: проверка смотрела только `core.md` двух форм — а расходились
    они в `preloader.md`, `commands/p2p.md` и `teacher.md`, где живёт строка статуса
    `[P2P … | Среда: …]`. Форма — это все её файлы; сверять по одному значит
    сторожить один файл и называть это паритетом.
    """
    found, seen = set(), 0
    for root in roots:
        for dp, dns, fns in os.walk(root):
            dns[:] = [d for d in dns if d not in {"docs", "legacy", "node_modules", ".git"}]
            for fn in fns:
                if not fn.endswith(".md") or "CHANGELOG" in fn.upper():
                    continue
                seen += 1
                found |= display_versions(read(os.path.join(dp, fn)) or "")
    return found, seen


pv, n_pv = form_versions(os.path.join(BASE, "plugin"))
cv, n_cv = form_versions(os.path.join(BASE, "for-chat"))
record(pv == cv and len(pv) == 1, "Паритет version-display двух форм",
       f"plugin: {sorted(pv) or '—'} · for-chat: {sorted(cv) or '—'}"
       + ("" if pv == cv and len(pv) == 1 else "  ← формы расходятся"),
       n_pv + n_cv)

# ── 17. Пункты-модули покрыты правилом видимости ─────────────────────────────
# [41] висел в меню без правила: пункт обещает web-fetch, которого в чате нет.
gated_errors, gated_checked = [], 0
for label, txt in (("plugin", pc), ("for-chat", cc)):
    mmap = menu_map(txt)
    conditional = {n for n, t in mmap.items() if "требует" in t.lower() or "web-fetch" in t.lower()}
    rules = "\n".join(l for l in txt.splitlines()
                      if re.search(r"(ONLY when|только пр|показывать только)", l))
    covered = set()
    for a, b in re.findall(r"\[(\d+)-(\d+)\]", rules):
        covered |= set(range(int(a), int(b) + 1))
    covered |= {int(x) for x in re.findall(r"\[(\d+)\]", rules)}
    for n in sorted(conditional):
        gated_checked += 1
        if n not in covered:
            gated_errors.append(f"{label}: пункт [{n}] условный, но не покрыт правилом видимости")
record(not gated_errors, "Условные пункты покрыты правилом видимости",
       "; ".join(gated_errors) if gated_errors else "все условные пункты имеют правило",
       max(gated_checked, 1))

# ── 18. Retired API-строки в живых правилах ──────────────────────────────────
RETIRED = {"claude-sonnet-4-6": "RETIRED 2026-06-30 → claude-sonnet-5",
           "claude-opus-4-20250514": "RETIRED 2026-06-15",
           "claude-sonnet-4-20250514": "RETIRED 2026-06-15",
           "budget_tokens": "удалён из API"}
ret_errors, ret_checked = [], 0
for label, txt in (("plugin core", pc), ("for-chat core", cc)):
    for i, line in enumerate(txt.splitlines(), 1):
        low = line.lower()
        # интересуют только ПРЕДПИСАНИЯ использовать, не запреты и не история
        if not re.search(r"(использовать api|use api strings)", low):
            continue
        ret_checked += 1
        for bad, why in RETIRED.items():
            if bad in line and "retired" not in low and "никогда" not in low.split(bad)[0][-30:]:
                ret_errors.append(f"{label}:{i} предписывает `{bad}` ({why})")
record(not ret_errors, "Нет retired API-строк в предписаниях",
       "; ".join(ret_errors) if ret_errors else "предписания используют только актуальные строки",
       max(ret_checked, 1))

# ── 19. Содержательный паритет форм по техникам релиза 8.4.4 ─────────────────
# Коммит fafb0d8 заявил «8 техник — все 4 сборки», но для C внёс их только в
# plugin: for-chat имела все файлы-получатели и НОЛЬ техник в них. Прежние 18
# проверок этого не видели — они сверяли меню, версии и ссылки, но не наличие
# содержания. Проверка, слепая к пустому файлу, пропускает половину поставки.
# Сверяем НЕ упоминание имени, а маркеры определения: заголовок блока + тело +
# первоисточник. Голая подстрока «GEPA» переживает вырезание заголовка (остаётся
# в [GEPA_CYCLE] и в techniques: VERSION_METADATA) — такая проверка зелёная при
# наполовину удалённой технике. Проверено selftest'ом: слабый вариант не ловил.
TECHNIQUE_PARITY = [
    ("VERBALIZED_SAMPLING", "writing_suite.md", "!writing.md",
     ["#DB_TECHNIQUE_VERBALIZED_SAMPLING", "2510.01171", "Sample from the tails"]),
    ("BRUTAL_EDITOR", "writing_suite.md", "!writing.md",
     ["#DB_TECHNIQUE_BRUTAL_EDITOR", "score your answer 1-10"]),
    ("GEPA", "optimization.md", "!optimization.md",
     ["### GEPA", "[GEPA_CYCLE]", "2507.19457"]),
    ("MASPO", "optimization.md", "!optimization.md",
     ["### MASPO", "[MASPO_QUORUM]", "2605.06623"]),
    ("SePO", "optimization.md", "!optimization.md",
     ["## SePO", "2606.04465"]),
    ("CONTEXT ENGINEERING", "compression.md", "!compression.md",
     ["## CONTEXT ENGINEERING", "note-taking", "JIT retrieval"]),
    ("Context-Grounding CoT", "reasoning.md", "!reasoning.md",
     ["### Context-Grounding CoT", "[CONTEXT_GROUNDING]", "2605.25354"]),
    ("POSITIVE_FRAMING", "db.md", "!!db_v8C.md",
     ["#DB_TECHNIQUE_POSITIVE_FRAMING", "розового слона"]),
]
par_errors, par_checked = [], 0
for tech, pl_name, fc_name, markers in TECHNIQUE_PARITY:
    pl_txt = read(os.path.join(BASE, "plugin", "skills", "p2p", pl_name))
    fc_txt = read(os.path.join(BASE, "for-chat", fc_name))
    if pl_txt is None or fc_txt is None:
        par_errors.append(f"«{tech}»: файл-носитель не найден ({pl_name} / {fc_name})")
        continue
    for marker in markers:
        par_checked += 2
        in_pl, in_fc = marker in pl_txt, marker in fc_txt
        if in_pl and not in_fc:
            par_errors.append(f"«{tech}»: «{marker}» есть в plugin/{pl_name}, нет в for-chat/{fc_name}")
        elif in_fc and not in_pl:
            par_errors.append(f"«{tech}»: «{marker}» есть в for-chat/{fc_name}, нет в plugin/{pl_name}")
        elif not in_pl and not in_fc:
            par_errors.append(f"«{tech}»: «{marker}» пропал из ОБЕИХ форм — техника потеряна")
record(not par_errors, "Паритет содержания форм по техникам v8C.4",
       "; ".join(par_errors) if par_errors else
       f"все {len(TECHNIQUE_PARITY)} техник присутствуют в обеих формах",
       max(par_checked, 1))

# ── 20. Plugin-имена файлов внутри for-chat ──────────────────────────────────
# Формы называют файлы по-разному (writing_suite.md ↔ !writing.md). Дословный
# перенос блока тащит имя, которого в for-chat не существует: ссылка ведёт в
# пустоту, а модель молча идёт дальше. Главный класс дефектов проекта.
PLUGIN_SKILL_DIR = os.path.join(BASE, "plugin", "skills", "p2p")
plugin_names = {fn[:-3] for fn in os.listdir(PLUGIN_SKILL_DIR)
                if fn.endswith(".md") and fn != "SKILL.md"} if os.path.isdir(PLUGIN_SKILL_DIR) else set()
# ИСКЛЮЧЕНИЕ (осознанное, не «чтобы позеленело»): `p2p.config.md` в for-chat
# используется единообразно в 10 местах, включая пункт меню [28] «Настройки
# p2p.config.md» — то есть публичный интерфейс. Переименование затрагивает
# меню и требует решения автора, поэтому вынесено за рамки этой проверки.
# Если решение будет принято — строку снять, проверка сразу покажет все 10 мест.
plugin_names -= {"p2p.config"}
HISTORICAL = re.compile(r"v7C\.2|port from|перенос из", re.I)
name_errors, name_checked = [], 0
chat_dir = os.path.join(BASE, "for-chat")
for fn in sorted(os.listdir(chat_dir)):
    if not fn.endswith(".md"):
        continue
    txt = read(os.path.join(chat_dir, fn)) or ""
    for i, line in enumerate(txt.splitlines(), 1):
        if HISTORICAL.search(line):      # отсылка к прошлому поколению — не ссылка
            continue
        name_checked += 1
        for base_name in plugin_names:
            # имя без ведущего '!' или '_' = plugin-форма.
            # дефис/слеш в границе обязателен: иначе `p2p-teacher.md` и
            # `skills/p2p/db.md` читаются как `teacher.md` / `db.md`.
            if re.search(rf"(?<![!_\-\w/]){re.escape(base_name)}\.md", line):
                name_errors.append(f"{fn}:{i} → `{base_name}.md` (в for-chat такого файла нет)")
record(not name_errors, "В for-chat нет ссылок на plugin-имена файлов",
       "; ".join(name_errors[:6]) + (f" … всего {len(name_errors)}" if len(name_errors) > 6 else "")
       if name_errors else f"{len(plugin_names)} имён проверено по строкам for-chat",
       max(name_checked, 1))

# ── 21. Атрибуция доступна обеим формам и не разошлась ───────────────────────
# 5 arXiv-статей — условие корректного заимствования. Файл жил только на уровне
# сборки, в for-chat-поставку не попадал; две копии обязаны совпадать побайтово.
cred_shared = read(os.path.join(BASE, "docs", "CREDITS_TECHNIQUES.md"))
cred_chat = read(os.path.join(BASE, "for-chat", "docs", "CREDITS_TECHNIQUES.md"))
if cred_shared is None:
    cred_detail, cred_ok = "docs/CREDITS_TECHNIQUES.md отсутствует на уровне сборки", False
elif cred_chat is None:
    cred_detail, cred_ok = "for-chat/docs/CREDITS_TECHNIQUES.md отсутствует — атрибуция недоступна пользователю for-chat", False
elif cred_shared != cred_chat:
    cred_detail, cred_ok = "копии атрибуции разошлись (docs/ ↔ for-chat/docs/)", False
else:
    n_arxiv = len(set(re.findall(r"arxiv\.org/abs/(\d+\.\d+)", cred_shared)))
    cred_ok = n_arxiv >= 5
    cred_detail = (f"обе копии совпадают, {n_arxiv} arXiv-источников"
                   if cred_ok else f"копии совпадают, но arXiv-источников только {n_arxiv} (ожидается ≥5)")
record(cred_ok, "Атрибуция техник доступна обеим формам", cred_detail, 2)

# ── Отчёт ────────────────────────────────────────────────────────────────────
print("=" * 72)
print(f"ВЕРИФИКАЦИЯ СБОРКИ {ED_NAME} — диспетчер /p2p и целостность")
print("=" * 72)
total_checked = 0
failed = 0
for ok, name, detail, checked in results:
    print(f"{'  OK  ' if ok else ' FAIL '} │ {name}")
    print(f"       │   {detail}  (проверено объектов: {checked})")
    total_checked += checked
    failed += 0 if ok else 1

print("=" * 72)
if total_checked == 0:
    sys.exit("FATAL: не проверено ни одного объекта — верификация несостоятельна")
print(f"ИТОГО: проверок {len(results)} · объектов {total_checked} · провалов {failed}")
print("=" * 72)
if failed:
    print("\n⚠ Это СТАТИЧЕСКАЯ проверка. Она подтверждает структуру и непротиворечивость")
    print("  правил, но НЕ поведение модели. Заявление об эффективности без живого")
    print("  A/B-прогона (n ≥ 3, метрика объявлена заранее) — гипотеза, а не факт.")
sys.exit(1 if failed else 0)
