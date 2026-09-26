"""patch_L322_D_12_exact_rows_report_20260925.py -- L-322 Stage D, patch D12.

RUN COMMAND

    Save this file in the ROOT of the palomas_orrery repository, open it in
    VS Code and click Run (the same as typing: python
    patch_L322_D_12_exact_rows_report_20260925.py). It refuses to run from
    documentation/. After it has run, MOVE it into documentation/.

    Success prints one "ok" line per file and "patch applied". Failure
    prints FAILURE and writes nothing; undo after a success is Discard
    Changes in GitHub Desktop.

WHAT IT CHANGES

    A new report, EXACT_ROWS_PRINTED.md in the orrery root: every place
    the orrery or the gallery prints an exact row of constants_new.py,
    with the code on each line. Rebuilt on every maintenance run and
    available on the dashboard. Report-only; it never gates a push.

    exact_rows_report.py            new, the generator
    orrery_maintenance_run.py       a seventh generator, before Document
                                    index; its summary shows in the run
    palomas_orrery_dashboard.py     Exact Rows Report beside the other
                                    generators
    documentation/RUN_RECORD_L322_D12_20260925.md   new

    Independent of patch D11: different files, either order.
    Nothing in constants_new.py or in the gallery repository is touched.

    Permanent, once run: the new tool, its row in the maintenance run
    and its dashboard entry. This script itself is disposable.

Built on orrery de4eadc58e3de746183515dff422aaab3943fe6a
at https://github.com/tonylquintanilla/palomas_orrery.

Written September 25, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

EDITS = [
    ('orrery_maintenance_run.py', '996771288c061ef84814a6d9d5a2f706', '92f273b18f199aaa435a194c890db890', [
        ('Runs the six GENERATORS, then the CHECKERS, and prints one summary at',
         'Runs the seven GENERATORS, then the CHECKERS, and prints one summary at'),
        ('Stage D, patch D3: CHECKERS gains Earth pole of date,\ntest_earth_pole_of_date.py, which checks the pole-of-date geometry against\nERFA and the fallback without contacting Horizons.)\n"""\n',
         'Stage D, patch D3: CHECKERS gains Earth pole of date,\ntest_earth_pole_of_date.py, which checks the pole-of-date geometry against\nERFA and the fallback without contacting Horizons.)\nModule updated: September 25, 2026 with Anthropic\'s Claude Opus 5.5 (L-322\nStage D, patch D12: GENERATORS gains Exact rows report,\nexact_rows_report.py, which writes EXACT_ROWS_PRINTED.md: every place the\norrery or the gallery prints an exact row of constants_new.py. It runs\nbefore Document index, so README.md lists the report on the same run. A\ngenerator row may now carry a fourth field, a verdict hint, as a checker\nrow does; its line is added to the row\'s note, so this report\'s summary\nshows in the run instead of only in a file nobody opens.)\n"""\n'),
        ("    ('Data inventory',  ['data_inventory.py'],\n     ['DATA_INVENTORY.md']),\n",
         "    ('Data inventory',  ['data_inventory.py'],\n     ['DATA_INVENTORY.md']),\n    # L-322 Stage D: every place the orrery or the gallery prints an exact\n    # row, which provenance-discipline Rule 7 says prints by a print count\n    # the row states. Reads the gallery folder beside this one, as Data\n    # inventory does. Before Document index, so README.md lists the report\n    # on the same run. The fourth field is a verdict hint: its line joins\n    # the note, so the count shows here and not only in the file.\n    ('Exact rows report', ['exact_rows_report.py'],\n     ['EXACT_ROWS_PRINTED.md'], 'EXACT ROWS PRINTED:'),\n"),
        ('    for label, argv_tail, outputs in GENERATORS:\n        before = dict((path, snapshot(path)) for path in outputs)',
         '    for entry in GENERATORS:\n        # An optional fourth field is a verdict hint, as on a checker row\n        # (L-322 Stage D, patch D12). Read with a length guard.\n        label, argv_tail, outputs = entry[0], entry[1], entry[2]\n        gen_hint = entry[3] if len(entry) > 3 else None\n        before = dict((path, snapshot(path)) for path in outputs)'),
        ("        else:\n            note = ('unchanged (%d checked, not written)'\n                    % len(outputs))\n        print_row(label, seconds, note)",
         "        else:\n            note = ('unchanged (%d checked, not written)'\n                    % len(outputs))\n        if gen_hint and rc == 0:\n            verdict = line_containing(output, gen_hint)\n            if verdict.startswith(gen_hint):\n                verdict = verdict[len(gen_hint):].strip()\n            note += ' -- ' + (verdict or 'no summary line printed')\n        print_row(label, seconds, note)"),
    ]),
    ('palomas_orrery_dashboard.py', '5cf8f142befa083f19a89d3763f1871e', '76a3bc1a426e78c757a937751d806fa0', [
        ('here. Both in alphabetical place.\n"""\n',
         'here. Both in alphabetical place.\nSeptember 25, 2026 with Anthropic\'s Claude Opus 5.5 (L-322 Stage D, patch\nD12), on Tony\'s request: added Exact Rows Report beside the other\ngenerators, in alphabetical place. It writes EXACT_ROWS_PRINTED.md in the\norrery root. No other entry touched.\n"""\n'),
        ('        ("Data Inventory",\n         "data_inventory.py",\n         "Inventory the large, gitignored data stores (data/, star_data/). "\n         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n',
         '        ("Data Inventory",\n         "data_inventory.py",\n         "Inventory the large, gitignored data stores (data/, star_data/). "\n         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Exact Rows Report",\n         "exact_rows_report.py",\n         "List every place the orrery or the gallery prints an exact row of "\n         "constants_new.py -- a definition or a stated rule, such as a cut "\n         "angle -- with the code on each line, so the width it prints at "\n         "can be read. Rule 7 of provenance-discipline says such a row "\n         "prints by a print count it states, not a width chosen where it "\n         "is printed; this is the list that work moves from. Reads the "\n         "gallery folder beside the orrery and says so at the top if it is "\n         "missing. Report-only: writes EXACT_ROWS_PRINTED.md and never "\n         "gates a push. The maintenance run runs it every time.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n'),
    ]),
]

NEW_FILES = [
    ('exact_rows_report.py', 'ae137de2d32ae5769719a7803adf39e1',
     '"""exact_rows_report.py -- which exact rows a display prints, and where.\n\nRUN COMMAND\n-----------\nOpen this file in VS Code and click Run. It takes no arguments.\n\n    python exact_rows_report.py\n\nThe orrery maintenance run runs it every time, as a generator. It\nwrites EXACT_ROWS_PRINTED.md in the orrery root and prints one summary\nline beginning "EXACT ROWS PRINTED:".\n\nWHAT IT DOES\n------------\nAn exact row is a row in constants_new.py whose "# Figures:" line\nbegins "exact": a definition or a stated rule, such as a cut angle,\nrather than a measurement. Rule 7 of provenance-discipline says a\ndisplay prints an exact row by a print count the row states, never by\na width chosen where it is printed. This tool lists every place a\ndisplay prints an exact row, in the orrery AND in the gallery, so the\nwork that moves those places onto a print count has a list to work\nfrom and a way to tell when it is finished.\n\nIt changes nothing and chooses no width. It is a report.\n\nTHE ORRERY HALF. Every tracked .py file outside documentation/, except\nconstants_new.py, is searched for each exact row\'s name in a printing\nform: inside {...} in a formatted string, as the argument of\n_declared, _whole_figures or _with_uncertainty, after %, or inside\nstr(...) or format(...).\n\nTHE GALLERY HALF. The gallery sits beside the orrery on Tony\'s\ncomputer, at ../tonyquintanilla.github.io, as data_inventory.py and the\ndashboard already assume. Its pages get constants_new.py values only\nthrough pointer entries in data/objects_config.json, each a node with\nan "orrery_constant", and through the two frame rows, which are used\nonly in arithmetic. A pointer\'s value usually reaches its print line\nunder another name, so the PRINTS table below says, for each pointer to\nan exact row, which page script, which function and which piece of code\nprints it. The table is small and hand-kept, so the tool checks it\nevery run: a pointer to an exact row with no entry is reported as NOT\nFOLLOWED, and an entry that matches no print line is reported as\nBROKEN. Neither is ever dropped quietly. A new exact row printed by the\ngallery therefore shows up first as NOT FOLLOWED, which is the prompt\nto add its entry.\n\nCONSOLE LINES. A tool that prints an exact row to the terminal, such\nas export_orbit_cache.py logging KM_PER_AU, is not a display a visitor\nsees. Lines that begin with print( are listed under their own heading\nand not counted as printing lines.\n\nIf the gallery folder is not there, the report says so at the top and\nthe summary line says the gallery half was not read; it never presents\nthe orrery half as the whole.\n\nThe output carries no date and no commit, so a run where nothing moved\nwrites identical bytes and the maintenance run reports it unchanged.\n\nBuilt for L-322 Stage D, after a one-time inventory on 2026-09-25\n(documentation/INVENTORY_L322_exact_rows_printed_20260925.md) found 7\nexact rows printed at 17 lines. Tony, the same day: make it a generator\nin the maintenance run and the dashboard, with the report in the root.\n\nRole: devtool\nDomain: dev_tools\n\nModule updated: September 25, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D12: new.)\n"""\n\nimport os\nimport re\nimport subprocess\nimport sys\n\nimport constants_rows\n\nHERE = os.path.dirname(os.path.abspath(__file__))\nOUT = os.path.join(HERE, \'EXACT_ROWS_PRINTED.md\')\nGALLERY_DIR = os.path.normpath(os.path.join(HERE, \'..\',\n                                            \'tonyquintanilla.github.io\'))\nGALLERY_CONFIG = os.path.join(\'data\', \'objects_config.json\')\n\n# The gallery\'s page scripts: every .js file in gallery/ and the one\n# page that hosts the rooms.\nGALLERY_SCRIPT_DIR = \'gallery\'\nGALLERY_PAGES = [\'interactive.html\']\n\n# A line in a gallery script that formats a number for display.\nGALLERY_PRINT_RE = re.compile(\n    r\'fmtServed\\(|_fmtServed\\(|sigFigures\\(|kmAndAu\\(|fmtKm\\(|\'\n    r\'\\.toFixed\\(|\\.toPrecision\\(|toLocaleString\\(\')\n\n# Where each gallery pointer to an exact row is printed. Key: the end\n# of the pointer node\'s path in data/objects_config.json. Value: the\n# page script, the top-level function the print line sits in, and a\n# piece of code that is on the print line. A pointer\'s value usually\n# reaches its print line under another name (the magnetopause\'s\n# pressure is printed through mpS.pressure, a shell\'s altitude through\n# km.altitudeKm), and one piece of code can sit in two functions (the\n# ring and the shell renderers print altitudes the same way), so all\n# three are needed. The table is hand-kept and checked every run: a\n# pointer to an exact row with no entry is reported as NOT FOLLOWED,\n# and an entry that matches no pointer or no print line is reported as\n# BROKEN.\nPRINTS = {\n    \'earth_magnetosphere/magnetopause/surface/pressure\':\n        (\'gallery/feature_renderers.js\', \'renderMagnetosphere\', \'mpS.pressure\'),\n    \'earth_magnetosphere/bow_shock/surface/pressure\':\n        (\'gallery/feature_renderers.js\', \'renderMagnetosphere\', \'bsS.pressure\'),\n    \'earth_magnetosphere/magnetopause/surface/bz\':\n        (\'gallery/feature_renderers.js\', \'renderMagnetosphere\', \'mpS.bz\'),\n    \'earth_magnetosphere/magnetopause/surface/cut_angle\':\n        (\'gallery/feature_renderers.js\', \'renderMagnetosphere\', \'mpS.cut_angle\'),\n    \'earth_magnetosphere/bow_shock/surface/cut_angle\':\n        (\'gallery/feature_renderers.js\', \'renderMagnetosphere\', \'bsS.cut_angle\'),\n    \'van_allen_belts/outer_belt_distance\':\n        (\'gallery/feature_renderers.js\', \'renderBelts\', \'distances[i]\'),\n    \'earth_orbital_zones/leo_inner/altitude\':\n        (\'gallery/feature_renderers.js\', \'renderShellSet\', \'km.altitudeKm\'),\n    \'earth_orbital_zones/leo_outer/altitude\':\n        (\'gallery/feature_renderers.js\', \'renderShellSet\', \'km.altitudeKm\'),\n}\n\n# A top-level function in a gallery script: two spaces of indent, which\n# is the gallery\'s module pattern. Nested helpers do not count as owners.\nTOP_FUNCTION_RE = re.compile(r\'  function\\s+(\\w+)\\s*\\(\')\n\n\ndef exact_rows():\n    """[(name, value text)] of every exact row, in store order."""\n    _text, rows, by_name = constants_rows.read_store(HERE)\n    out = []\n    for name in by_name:\n        figures = (by_name[name].field(\'Figures\') or \'\').strip().lower()\n        if figures.startswith(\'exact\'):\n            out.append(name)\n    return out\n\n\ndef tracked_py_files():\n    """Tracked .py files the orrery half searches, relative to HERE."""\n    try:\n        listed = subprocess.check_output(\n            [\'git\', \'ls-files\', \'*.py\'], cwd=HERE,\n            stderr=subprocess.DEVNULL).decode(\'utf-8\', \'replace\').split()\n    except (OSError, subprocess.CalledProcessError):\n        listed = []\n        for root, dirs, files in os.walk(HERE):\n            dirs[:] = [d for d in dirs if not d.startswith(\'.\')]\n            for name in files:\n                if name.endswith(\'.py\'):\n                    listed.append(os.path.relpath(os.path.join(root, name),\n                                                  HERE).replace(os.sep, \'/\'))\n    return sorted(f for f in listed\n                  if not f.startswith(\'documentation/\')\n                  and f != \'constants_new.py\'\n                  and f != os.path.basename(__file__))\n\n\ndef orrery_print_pattern(name):\n    n = re.escape(name)\n    return re.compile(\n        r\'\\{\\s*%s\\b[^}]*\\}\' % n\n        + r\'|(?:_declared|_whole_figures|_with_uncertainty)\\(\\s*[\\\'"]%s[\\\'"]\' % n\n        + r\'|%%\\s*\\(?\\s*%s\\b\' % n\n        + r\'|(?:str|format)\\(\\s*%s\\b\' % n)\n\n\ndef read_lines(path):\n    with open(path, \'r\', encoding=\'utf-8\', errors=\'replace\') as handle:\n        return handle.read().splitlines()\n\n\ndef orrery_sites(names):\n    """Display sites, console sites, and other-use counts, by row name."""\n    sites = dict((n, []) for n in names)\n    console = dict((n, []) for n in names)\n    uses = dict((n, 0) for n in names)\n    patterns = dict((n, orrery_print_pattern(n)) for n in names)\n    for rel in tracked_py_files():\n        path = os.path.join(HERE, rel)\n        if not os.path.exists(path):\n            continue\n        for number, line in enumerate(read_lines(path), 1):\n            stripped = line.strip()\n            if stripped.startswith(\'#\'):\n                continue\n            for n in names:\n                if n not in line:\n                    continue\n                if patterns[n].search(line):\n                    if stripped.startswith(\'print(\'):\n                        console[n].append((rel, number, stripped))\n                    else:\n                        sites[n].append((rel, number, stripped))\n                else:\n                    uses[n] += 1\n    return sites, console, uses\n\n\ndef config_pointers(config, names):\n    """[(row, config path, key)] for every pointer to an exact row."""\n    found = []\n    wanted = set(names)\n\n    def walk(node, path):\n        if isinstance(node, dict):\n            pointer = node.get(\'orrery_constant\')\n            if isinstance(pointer, str):\n                row = pointer.split(\'::\')[-1]\n                if row in wanted:\n                    found.append((row, path, path.rsplit(\'/\', 1)[-1]))\n            for key, value in node.items():\n                walk(value, path + \'/\' + key)\n        elif isinstance(node, list):\n            for index, value in enumerate(node):\n                walk(value, \'%s/%d\' % (path, index))\n\n    walk(config, \'\')\n    return found\n\n\ndef gallery_scripts():\n    """Relative paths of the gallery\'s page scripts that exist."""\n    out = []\n    script_dir = os.path.join(GALLERY_DIR, GALLERY_SCRIPT_DIR)\n    if os.path.isdir(script_dir):\n        for name in sorted(os.listdir(script_dir)):\n            if name.endswith(\'.js\'):\n                out.append(GALLERY_SCRIPT_DIR + \'/\' + name)\n    for name in GALLERY_PAGES:\n        if os.path.exists(os.path.join(GALLERY_DIR, name)):\n            out.append(name)\n    return out\n\n\ndef map_entry(path):\n    """The PRINTS entry for a pointer path, or None."""\n    for suffix, entry in PRINTS.items():\n        if path.endswith(\'/\' + suffix):\n            return suffix, entry\n    return None\n\n\ndef gallery_sites(pointers):\n    """({row: [(file, line, code, path)]}, not_followed, broken)."""\n    print_lines = []\n    for rel in gallery_scripts():\n        owner = None\n        for number, line in enumerate(\n                read_lines(os.path.join(GALLERY_DIR, rel)), 1):\n            match = TOP_FUNCTION_RE.match(line)\n            if match:\n                owner = match.group(1)\n            stripped = line.strip()\n            if stripped.startswith(\'//\') or stripped.startswith(\'*\'):\n                continue\n            if GALLERY_PRINT_RE.search(line):\n                print_lines.append((rel, owner, number, stripped))\n\n    sites = {}\n    not_followed = []\n    used = set()\n    for row, path, _key in pointers:\n        found = map_entry(path)\n        if found is None:\n            not_followed.append((row, path))\n            continue\n        suffix, (script, function, marker) = found\n        hits = [(f, n, code) for f, owner, n, code in print_lines\n                if f == script and owner == function and marker in code]\n        if hits:\n            used.add(suffix)\n        for f, n, code in hits:\n            sites.setdefault(row, []).append((f, n, code, path))\n    # An entry whose pointer matches no print line is BROKEN; an entry\n    # that no pointer reaches at all (the config entry was renamed or\n    # removed) is broken too, since it can no longer vouch for anything.\n    broken = [(suffix, PRINTS[suffix][2]) for suffix in PRINTS\n              if suffix not in used]\n    return sites, not_followed, broken\n\n\ndef short(code, width=96):\n    code = \' \'.join(code.split())\n    return code if len(code) <= width else code[:width - 3] + \'...\'\n\n\ndef main():\n    names = exact_rows()\n    o_sites, o_console, o_uses = orrery_sites(names)\n\n    gallery_read = os.path.exists(os.path.join(GALLERY_DIR, GALLERY_CONFIG))\n    g_sites, not_followed, broken, pointers = {}, [], [], []\n    if gallery_read:\n        import json\n        with open(os.path.join(GALLERY_DIR, GALLERY_CONFIG), \'r\',\n                  encoding=\'utf-8\') as handle:\n            config = json.load(handle)\n        pointers = config_pointers(config, names)\n        g_sites, not_followed, broken = gallery_sites(pointers)\n\n    printed = [n for n in names if o_sites[n] or g_sites.get(n)]\n    unprinted = [n for n in names if n not in printed]\n    o_lines = set((f, l) for n in names for f, l, _c in o_sites[n])\n    g_lines = set((f, l) for n in names for f, l, _c, _p in g_sites.get(n, []))\n\n    lines = []\n    add = lines.append\n    add(\'<!-- Doc-Kind: generated | Which exact rows of constants_new.py \'\n        \'a display prints, and where, in the orrery and the gallery; \'\n        \'rebuilt by exact_rows_report.py. Do not hand-edit. -->\')\n    add(\'# Exact Rows Printed\')\n    add(\'\')\n    add(\'Rebuilt by `exact_rows_report.py` on every orrery maintenance \'\n        \'run. An exact row is one whose `# Figures:` line begins `exact`: \'\n        \'a definition or a stated rule, not a measurement. \'\n        \'provenance-discipline Rule 7 says a display prints such a row by \'\n        \'a print count the row states, never by a width chosen where it \'\n        \'is printed. This report lists every place a display prints one, \'\n        \'with the code on that line, so the width it uses can be read.\')\n    add(\'\')\n    if not gallery_read:\n        add(\'**THE GALLERY HALF WAS NOT READ.** No `%s` was found at `%s`. \'\n            \'Everything below is the orrery only.\'\n            % (GALLERY_CONFIG.replace(os.sep, \'/\'),\n               GALLERY_DIR.replace(os.sep, \'/\')))\n        add(\'\')\n    add(\'## Summary\')\n    add(\'\')\n    add(\'- %d exact rows in `constants_new.py`.\' % len(names))\n    add(\'- %d printed by at least one display: %s.\'\n        % (len(printed), \', \'.join(\'`%s`\' % n for n in printed) or \'none\'))\n    add(\'- %d printing lines: %d in the orrery, %s in the gallery.\'\n        % (len(o_lines) + len(g_lines), len(o_lines),\n           len(g_lines) if gallery_read else \'not read\'))\n    if gallery_read:\n        add(\'- Gallery pointers to exact rows with no PRINTS entry (NOT \'\n            \'FOLLOWED): %d%s.\' % (len(not_followed), (\': \' + \', \'.join(\n                \'`%s` at `%s`\' % (r, p) for r, p in not_followed))\n                if not_followed else \'\'))\n        add(\'- PRINTS entries that no longer match a pointer or a print line \'\n            \'(BROKEN): %d%s.\'\n            % (len(broken), (\': \' + \', \'.join(\n                \'`%s` -> `%s`\' % (k, m) for k, m in broken))\n                if broken else \'\'))\n    add(\'\')\n    add(\'## Printed\')\n    add(\'\')\n    for n in printed:\n        add(\'### `%s`\' % n)\n        add(\'\')\n        for f, l, code in o_sites[n]:\n            add(\'- orrery `%s` line %d: `%s`\' % (f, l, short(code)))\n        for f, l, code, path in g_sites.get(n, []):\n            add(\'- gallery `%s` line %d (config `%s`): `%s`\'\n                % (f, l, path, short(code)))\n        add(\'\')\n    console_rows = [n for n in names if o_console[n]]\n    if console_rows:\n        add(\'## Printed to a terminal only\')\n        add(\'\')\n        add(\'A tool logging a value is not a display a visitor sees, so \'\n            \'these are not counted above.\')\n        add(\'\')\n        for n in console_rows:\n            for f, l, code in o_console[n]:\n                add(\'- `%s`: orrery `%s` line %d: `%s`\'\n                    % (n, f, l, short(code)))\n        add(\'\')\n    add(\'## Not printed\')\n    add(\'\')\n    add(\'No display prints these exact rows. Under Rule 7 they \'\n        \'carry no print count. The number is how many other orrery lines \'\n        \'name the row, so a use that prints it through another name can \'\n        \'still be found by reading those lines.\')\n    add(\'\')\n    for n in unprinted:\n        add(\'- `%s`: named on %d other orrery line(s).\' % (n, o_uses[n]))\n    add(\'\')\n    add(\'## How the search works\')\n    add(\'\')\n    add(\'Orrery: every tracked `.py` file outside `documentation/`, except \'\n        \'`constants_new.py` and this tool, searched for each exact row\\\'s \'\n        \'name inside `{...}` in a formatted string, as the argument of \'\n        \'`_declared`, `_whole_figures` or `_with_uncertainty`, after `%`, \'\n        \'or inside `str(...)` or `format(...)`. Comment lines are skipped.\')\n    add(\'\')\n    add(\'Gallery: each pointer in `data/objects_config.json` to an exact \'\n        \'row, followed to its print lines by the PRINTS table in the tool: \'\n        \'the page script, the function and a piece of the print line. \'\n        \'A pointer with no entry, or an entry that matches nothing, is \'\n        \'reported above rather than dropped. \'\n        \'Page scripts read: %s.\'\n        % (\', \'.join(\'`%s`\' % s for s in gallery_scripts())\n           if gallery_read else \'none (not read)\'))\n    add(\'\')\n    add(\'Not searched: an exact row\\\'s value typed into text as words or \'\n        \'digits instead of read from the row.\')\n    add(\'\')\n\n    text = \'\\n\'.join(lines)\n    old = None\n    if os.path.exists(OUT):\n        with open(OUT, \'r\', encoding=\'utf-8\', newline=\'\') as handle:\n            old = handle.read()\n    if old is None or old.replace(\'\\r\\n\', \'\\n\') != text:\n        with open(OUT, \'w\', encoding=\'utf-8\', newline=\'\\n\') as handle:\n            handle.write(text)\n\n    summary = (\'EXACT ROWS PRINTED: %d of %d exact rows printed at %d lines \'\n               \'(%d orrery, %s gallery)\'\n               % (len(printed), len(names), len(o_lines) + len(g_lines),\n                  len(o_lines), len(g_lines) if gallery_read else \'NOT READ\'))\n    if gallery_read:\n        summary += \'; %d not followed, %d map entries broken\' % (\n            len(not_followed), len(broken))\n    else:\n        summary += \'; the gallery folder was not found\'\n    print(summary)\n    return 0\n\n\nif __name__ == \'__main__\':\n    sys.exit(main())\n'),
    ('documentation/RUN_RECORD_L322_D12_20260925.md', '8eb99c40652ca901515ba6038e52fb95',
     '# Run record -- L-322 Stage D, patch D12: the exact-rows report\n\n**Built on orrery `de4eadc58e3de746183515dff422aaab3943fe6a` at\nhttps://github.com/tonylquintanilla/palomas_orrery.** It reads the\ngallery at whatever state the folder beside the orrery is in; tested\nagainst gallery `42a17abe16eebe5f03c790ad2a8f39f918c1ba7b` at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io.\n\nIndependent of patch D11 (provenance-discipline 2.19): the two patches\ntouch different files and can run in either order.\n\nWritten for Tony and for the sessions that act on the report.\n\n---\n\n## 1. Why\n\nOn 2026-09-25 a one-time inventory\n(`documentation/INVENTORY_L322_exact_rows_printed_20260925.md`) listed\nevery place the orrery or the gallery prints an exact row of\n`constants_new.py`. Tony: promote it to a generator in the maintenance\nrun and the dashboard, with the report in the orrery root beside the\nother reports.\n\n## 2. What the patch changes\n\n- **New `exact_rows_report.py`.** Writes `EXACT_ROWS_PRINTED.md` in the\n  orrery root and prints one line beginning "EXACT ROWS PRINTED:". The\n  report names every exact row, every line that prints one with the code\n  on that line, the rows printed only to a terminal, and the rows no\n  display prints. It reads the gallery folder beside the orrery, as\n  `data_inventory.py` does; if that folder is missing it says so at the\n  top and in the summary line, and never presents the orrery half as the\n  whole.\n- **The gallery half is checked, not trusted.** A served value usually\n  reaches its print line under another name, so a table in the tool,\n  PRINTS, names the script, the function and a piece of the print line\n  for each gallery pointer to an exact row. A pointer with no entry is\n  reported as NOT FOLLOWED; an entry that matches no pointer or no print\n  line is reported as BROKEN. A new exact row printed by the gallery\n  therefore shows up first as NOT FOLLOWED.\n- **`orrery_maintenance_run.py`.** A seventh generator, "Exact rows\n  report", before "Document index", so `README.md` lists the report on\n  the same run. A generator row may now carry a verdict hint, as a\n  checker row does, so the report\'s summary line shows in the run itself\n  and not only in the file.\n- **`palomas_orrery_dashboard.py`.** "Exact Rows Report" beside the other\n  generators, in alphabetical place.\n\n## 3. How it was verified, in the sandbox\n\n- The report against both repos: 7 of 20 exact rows printed at 18\n  lines, 8 in the orrery and 10 in the gallery, none not followed, no\n  entry broken. The hand inventory said 17 lines; the tool found one it\n  had missed, the belt hover\'s kilometre line in the gallery\n  (`kmAndAu(distances[i] * radiusKm, ...)`), which prints a conversion of\n  the outer belt\'s peak.\n- It fails when it should, each on a throwaway copy: with no gallery\n  folder, the summary says "NOT READ gallery; the gallery folder was not\n  found" and the report opens with it; with one pointer\'s entry renamed,\n  it reports 1 not followed and 1 broken; with one entry\'s code changed,\n  1 broken.\n- A second run with nothing changed writes identical bytes, so the\n  maintenance run reports it unchanged.\n- The full maintenance run on the changed copy: the new row printed\n  "unchanged -- 7 of 20 exact rows printed at 18 lines ...", and\n  Document index added the report to `README.md`. 18 of 19 checkers\n  passed; Reset completeness fails in the sandbox on the untouched base\n  as well, because the Windows colour name `SystemButtonFace` does not\n  exist on Linux. On your machine all should pass.\n- The provenance scanner, as counted lists: 1083 findings before and\n  after. One dict-size entry moved from 134 to 135 entries because the\n  tree has one more module; nothing gained or lost otherwise.\n\n## 4. What your first run will change\n\nThe maintenance run will create `EXACT_ROWS_PRINTED.md` and rewrite\n`README.md` (one new row in its documents table). Commit both with the\npatch.\n\n## 5. Tony\'s run\n\n(Append the patch output, the maintenance run\'s result, and a look at\nEXACT_ROWS_PRINTED.md.)\n\n---\n\nSession written September 2026 with Anthropic\'s Claude Opus 5.5.\n'),
]


def content(raw):
    """LF-normalised bytes: line endings are not content."""
    return raw.replace(b"\r\n", b"\n")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(here) == "documentation":
        print("ERROR: run this from the repository ROOT, not from "
              "documentation/. Move it up one level, run it, then move it "
              "back. NOTHING was written.")
        return 1
    store = os.path.join(here, "constants_new.py")
    if not os.path.exists(store):
        print("ERROR: constants_new.py is not beside this script, so this "
              "is not the orrery root. NOTHING was written.")
        return 1

    planned = []
    problems = []
    notes = []
    already = 0
    for name, base_fp, want_fp, hunks in EDITS:
        path = os.path.join(here, name)
        if not os.path.exists(path):
            problems.append("%s: not found" % name)
            continue
        with open(path, "rb") as handle:
            raw = handle.read()
        is_crlf = b"\r\n" in raw
        body = content(raw)
        actual = hashlib.md5(body).hexdigest()
        if actual == want_fp:
            problems.append("%s: already carries this patch's result -- a "
                            "second run" % name)
            already += 1
            continue
        if actual != base_fp:
            problems.append("%s: BASE MOVED. Expected %s, found %s"
                            % (name, base_fp[:12], actual[:12]))
            continue
        if is_crlf:
            notes.append("%s: the working copy is CRLF; written back CRLF"
                         % name)
        text = body.decode("utf-8")
        for index, (old, new) in enumerate(hunks, 1):
            found = text.count(old)
            if found != 1:
                problems.append("%s: ANCHOR FAIL, edit %d of %d matched %d "
                                "times" % (name, index, len(hunks), found))
                break
            if any(ord(ch) > 127 for ch in new):
                problems.append("%s: edit %d inserts a non-ASCII character"
                                % (name, index))
                break
            text = text.replace(old, new)
        else:
            out = text.encode("utf-8")
            if hashlib.md5(out).hexdigest() != want_fp:
                problems.append("%s: the result is not the file this patch "
                                "was built to produce" % name)
                continue
            planned.append((path, out.replace(b"\n", b"\r\n") if is_crlf
                            else out, name, "%d edit(s)" % len(hunks)))
    for name, want_fp, text in NEW_FILES:
        path = os.path.join(here, name)
        data = text.encode("utf-8")
        if hashlib.md5(data).hexdigest() != want_fp:
            problems.append("%s: the text in this patch is damaged" % name)
            continue
        if os.path.exists(path):
            with open(path, "rb") as handle:
                if hashlib.md5(content(handle.read())).hexdigest() == want_fp:
                    problems.append("%s: already exists with this patch's "
                                    "content -- a second run" % name)
                else:
                    problems.append("%s: already exists with OTHER content; "
                                    "this patch will not overwrite it" % name)
            continue
        planned.append((path, data, name, "new file"))

    if problems:
        print("FAILURE -- NOTHING was written:")
        for line in problems:
            print("  " + line)
        print("")
        print("Undo is Discard Changes in GitHub Desktop.")
        return 1

    for path, data, name, what in planned:
        with open(path, "wb") as handle:
            handle.write(data)
        print("ok  %-48s %s" % (name, what))
    for line in notes:
        print("note: " + line)
    print("")
    print("patch applied (%d file(s))" % len(planned))
    print("")
    print("DO THESE, IN THIS ORDER:")
    print("  1. Run the orrery maintenance run. Its GENERATORS section "
          "gains an \"Exact rows report\" row, which should read "
          "\"7 of 20 exact rows printed at 18 lines (8 orrery, 10 gallery); "
          "0 not followed, 0 map entries broken\". If it says the gallery "
          "was NOT READ, the gallery folder is not beside the orrery folder.")
    print("  2. Open EXACT_ROWS_PRINTED.md in the orrery root and look it "
          "over. README.md also gains one row in its documents table.")
    print("  3. Commit the patch's files, EXACT_ROWS_PRINTED.md and "
          "README.md together, push, and move this script into "
          "documentation/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
