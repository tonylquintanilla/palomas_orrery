"""exact_rows_report.py -- which exact rows a display prints, and where.

RUN COMMAND
-----------
Open this file in VS Code and click Run. It takes no arguments.

    python exact_rows_report.py

The orrery maintenance run runs it every time, as a generator. It
writes EXACT_ROWS_PRINTED.md in the orrery root and prints one summary
line beginning "EXACT ROWS PRINTED:".

WHAT IT DOES
------------
An exact row is a row in constants_new.py whose "# Figures:" line
begins "exact": a definition or a stated rule, such as a cut angle,
rather than a measurement. Rule 7 of provenance-discipline says a
display prints an exact row by a print count the row states, never by
a width chosen where it is printed. This tool lists every place a
display prints an exact row, in the orrery AND in the gallery, so the
work that moves those places onto a print count has a list to work
from and a way to tell when it is finished.

It changes nothing and chooses no width. It is a report.

THE ORRERY HALF. Every tracked .py file outside documentation/, except
constants_new.py, is searched for each exact row's name in a printing
form: inside {...} in a formatted string, as the argument of
_declared, _whole_figures or _with_uncertainty, after %, or inside
str(...) or format(...).

THE GALLERY HALF. The gallery sits beside the orrery on Tony's
computer, at ../tonyquintanilla.github.io, as data_inventory.py and the
dashboard already assume. Its pages get constants_new.py values only
through pointer entries in data/objects_config.json, each a node with
an "orrery_constant", and through the two frame rows, which are used
only in arithmetic. A pointer's value usually reaches its print line
under another name, so the PRINTS table below says, for each pointer to
an exact row, which page script, which function and which piece of code
prints it. The table is small and hand-kept, so the tool checks it
every run: a pointer to an exact row with no entry is reported as NOT
FOLLOWED, and an entry that matches no print line is reported as
BROKEN. Neither is ever dropped quietly. A new exact row printed by the
gallery therefore shows up first as NOT FOLLOWED, which is the prompt
to add its entry.

CONSOLE LINES. A tool that prints an exact row to the terminal, such
as export_orbit_cache.py logging KM_PER_AU, is not a display a visitor
sees. Lines that begin with print( are listed under their own heading
and not counted as printing lines.

If the gallery folder is not there, the report says so at the top and
the summary line says the gallery half was not read; it never presents
the orrery half as the whole.

The output carries no date and no commit, so a run where nothing moved
writes identical bytes and the maintenance run reports it unchanged.

Built for L-322 Stage D, after a one-time inventory on 2026-09-25
(documentation/INVENTORY_L322_exact_rows_printed_20260925.md) found 7
exact rows printed at 17 lines. Tony, the same day: make it a generator
in the maintenance run and the dashboard, with the report in the root.

Role: devtool
Domain: dev_tools

Module updated: September 25, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D12: new.)
"""

import os
import re
import subprocess
import sys

import constants_rows

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'EXACT_ROWS_PRINTED.md')
GALLERY_DIR = os.path.normpath(os.path.join(HERE, '..',
                                            'tonyquintanilla.github.io'))
GALLERY_CONFIG = os.path.join('data', 'objects_config.json')

# The gallery's page scripts: every .js file in gallery/ and the one
# page that hosts the rooms.
GALLERY_SCRIPT_DIR = 'gallery'
GALLERY_PAGES = ['interactive.html']

# A line in a gallery script that formats a number for display.
GALLERY_PRINT_RE = re.compile(
    r'fmtServed\(|_fmtServed\(|sigFigures\(|kmAndAu\(|fmtKm\(|'
    r'\.toFixed\(|\.toPrecision\(|toLocaleString\(')

# Where each gallery pointer to an exact row is printed. Key: the end
# of the pointer node's path in data/objects_config.json. Value: the
# page script, the top-level function the print line sits in, and a
# piece of code that is on the print line. A pointer's value usually
# reaches its print line under another name (the magnetopause's
# pressure is printed through mpS.pressure, a shell's altitude through
# km.altitudeKm), and one piece of code can sit in two functions (the
# ring and the shell renderers print altitudes the same way), so all
# three are needed. The table is hand-kept and checked every run: a
# pointer to an exact row with no entry is reported as NOT FOLLOWED,
# and an entry that matches no pointer or no print line is reported as
# BROKEN.
PRINTS = {
    'earth_magnetosphere/magnetopause/surface/pressure':
        ('gallery/feature_renderers.js', 'renderMagnetosphere', 'mpS.pressure'),
    'earth_magnetosphere/bow_shock/surface/pressure':
        ('gallery/feature_renderers.js', 'renderMagnetosphere', 'bsS.pressure'),
    'earth_magnetosphere/magnetopause/surface/bz':
        ('gallery/feature_renderers.js', 'renderMagnetosphere', 'mpS.bz'),
    'earth_magnetosphere/magnetopause/surface/cut_angle':
        ('gallery/feature_renderers.js', 'renderMagnetosphere', 'mpS.cut_angle'),
    'earth_magnetosphere/bow_shock/surface/cut_angle':
        ('gallery/feature_renderers.js', 'renderMagnetosphere', 'bsS.cut_angle'),
    'van_allen_belts/outer_belt_distance':
        ('gallery/feature_renderers.js', 'renderBelts', 'distances[i]'),
    'earth_orbital_zones/leo_inner/altitude':
        ('gallery/feature_renderers.js', 'renderShellSet', 'km.altitudeKm'),
    'earth_orbital_zones/leo_outer/altitude':
        ('gallery/feature_renderers.js', 'renderShellSet', 'km.altitudeKm'),
}

# A top-level function in a gallery script: two spaces of indent, which
# is the gallery's module pattern. Nested helpers do not count as owners.
TOP_FUNCTION_RE = re.compile(r'  function\s+(\w+)\s*\(')


def exact_rows():
    """[(name, value text)] of every exact row, in store order."""
    _text, rows, by_name = constants_rows.read_store(HERE)
    out = []
    for name in by_name:
        figures = (by_name[name].field('Figures') or '').strip().lower()
        if figures.startswith('exact'):
            out.append(name)
    return out


def tracked_py_files():
    """Tracked .py files the orrery half searches, relative to HERE."""
    try:
        listed = subprocess.check_output(
            ['git', 'ls-files', '*.py'], cwd=HERE,
            stderr=subprocess.DEVNULL).decode('utf-8', 'replace').split()
    except (OSError, subprocess.CalledProcessError):
        listed = []
        for root, dirs, files in os.walk(HERE):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for name in files:
                if name.endswith('.py'):
                    listed.append(os.path.relpath(os.path.join(root, name),
                                                  HERE).replace(os.sep, '/'))
    return sorted(f for f in listed
                  if not f.startswith('documentation/')
                  and f != 'constants_new.py'
                  and f != os.path.basename(__file__))


def orrery_print_pattern(name):
    n = re.escape(name)
    return re.compile(
        r'\{\s*%s\b[^}]*\}' % n
        + r'|(?:_declared|_whole_figures|_with_uncertainty)\(\s*[\'"]%s[\'"]' % n
        + r'|%%\s*\(?\s*%s\b' % n
        + r'|(?:str|format)\(\s*%s\b' % n)


def read_lines(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as handle:
        return handle.read().splitlines()


def orrery_sites(names):
    """Display sites, console sites, and other-use counts, by row name."""
    sites = dict((n, []) for n in names)
    console = dict((n, []) for n in names)
    uses = dict((n, 0) for n in names)
    patterns = dict((n, orrery_print_pattern(n)) for n in names)
    for rel in tracked_py_files():
        path = os.path.join(HERE, rel)
        if not os.path.exists(path):
            continue
        for number, line in enumerate(read_lines(path), 1):
            stripped = line.strip()
            if stripped.startswith('#'):
                continue
            for n in names:
                if n not in line:
                    continue
                if patterns[n].search(line):
                    if stripped.startswith('print('):
                        console[n].append((rel, number, stripped))
                    else:
                        sites[n].append((rel, number, stripped))
                else:
                    uses[n] += 1
    return sites, console, uses


def config_pointers(config, names):
    """[(row, config path, key)] for every pointer to an exact row."""
    found = []
    wanted = set(names)

    def walk(node, path):
        if isinstance(node, dict):
            pointer = node.get('orrery_constant')
            if isinstance(pointer, str):
                row = pointer.split('::')[-1]
                if row in wanted:
                    found.append((row, path, path.rsplit('/', 1)[-1]))
            for key, value in node.items():
                walk(value, path + '/' + key)
        elif isinstance(node, list):
            for index, value in enumerate(node):
                walk(value, '%s/%d' % (path, index))

    walk(config, '')
    return found


def gallery_scripts():
    """Relative paths of the gallery's page scripts that exist."""
    out = []
    script_dir = os.path.join(GALLERY_DIR, GALLERY_SCRIPT_DIR)
    if os.path.isdir(script_dir):
        for name in sorted(os.listdir(script_dir)):
            if name.endswith('.js'):
                out.append(GALLERY_SCRIPT_DIR + '/' + name)
    for name in GALLERY_PAGES:
        if os.path.exists(os.path.join(GALLERY_DIR, name)):
            out.append(name)
    return out


def map_entry(path):
    """The PRINTS entry for a pointer path, or None."""
    for suffix, entry in PRINTS.items():
        if path.endswith('/' + suffix):
            return suffix, entry
    return None


def gallery_sites(pointers):
    """({row: [(file, line, code, path)]}, not_followed, broken)."""
    print_lines = []
    for rel in gallery_scripts():
        owner = None
        for number, line in enumerate(
                read_lines(os.path.join(GALLERY_DIR, rel)), 1):
            match = TOP_FUNCTION_RE.match(line)
            if match:
                owner = match.group(1)
            stripped = line.strip()
            if stripped.startswith('//') or stripped.startswith('*'):
                continue
            if GALLERY_PRINT_RE.search(line):
                print_lines.append((rel, owner, number, stripped))

    sites = {}
    not_followed = []
    used = set()
    for row, path, _key in pointers:
        found = map_entry(path)
        if found is None:
            not_followed.append((row, path))
            continue
        suffix, (script, function, marker) = found
        hits = [(f, n, code) for f, owner, n, code in print_lines
                if f == script and owner == function and marker in code]
        if hits:
            used.add(suffix)
        for f, n, code in hits:
            sites.setdefault(row, []).append((f, n, code, path))
    # An entry whose pointer matches no print line is BROKEN; an entry
    # that no pointer reaches at all (the config entry was renamed or
    # removed) is broken too, since it can no longer vouch for anything.
    broken = [(suffix, PRINTS[suffix][2]) for suffix in PRINTS
              if suffix not in used]
    return sites, not_followed, broken


def short(code, width=96):
    code = ' '.join(code.split())
    return code if len(code) <= width else code[:width - 3] + '...'


def main():
    names = exact_rows()
    o_sites, o_console, o_uses = orrery_sites(names)

    gallery_read = os.path.exists(os.path.join(GALLERY_DIR, GALLERY_CONFIG))
    g_sites, not_followed, broken, pointers = {}, [], [], []
    if gallery_read:
        import json
        with open(os.path.join(GALLERY_DIR, GALLERY_CONFIG), 'r',
                  encoding='utf-8') as handle:
            config = json.load(handle)
        pointers = config_pointers(config, names)
        g_sites, not_followed, broken = gallery_sites(pointers)

    printed = [n for n in names if o_sites[n] or g_sites.get(n)]
    unprinted = [n for n in names if n not in printed]
    o_lines = set((f, l) for n in names for f, l, _c in o_sites[n])
    g_lines = set((f, l) for n in names for f, l, _c, _p in g_sites.get(n, []))

    lines = []
    add = lines.append
    add('<!-- Doc-Kind: generated | Which exact rows of constants_new.py '
        'a display prints, and where, in the orrery and the gallery; '
        'rebuilt by exact_rows_report.py. Do not hand-edit. -->')
    add('# Exact Rows Printed')
    add('')
    add('Rebuilt by `exact_rows_report.py` on every orrery maintenance '
        'run. An exact row is one whose `# Figures:` line begins `exact`: '
        'a definition or a stated rule, not a measurement. '
        'provenance-discipline Rule 7 says a display prints such a row by '
        'a print count the row states, never by a width chosen where it '
        'is printed. This report lists every place a display prints one, '
        'with the code on that line, so the width it uses can be read.')
    add('')
    if not gallery_read:
        add('**THE GALLERY HALF WAS NOT READ.** No `%s` was found at `%s`. '
            'Everything below is the orrery only.'
            % (GALLERY_CONFIG.replace(os.sep, '/'),
               GALLERY_DIR.replace(os.sep, '/')))
        add('')
    add('## Summary')
    add('')
    add('- %d exact rows in `constants_new.py`.' % len(names))
    add('- %d printed by at least one display: %s.'
        % (len(printed), ', '.join('`%s`' % n for n in printed) or 'none'))
    add('- %d printing lines: %d in the orrery, %s in the gallery.'
        % (len(o_lines) + len(g_lines), len(o_lines),
           len(g_lines) if gallery_read else 'not read'))
    if gallery_read:
        add('- Gallery pointers to exact rows with no PRINTS entry (NOT '
            'FOLLOWED): %d%s.' % (len(not_followed), (': ' + ', '.join(
                '`%s` at `%s`' % (r, p) for r, p in not_followed))
                if not_followed else ''))
        add('- PRINTS entries that no longer match a pointer or a print line '
            '(BROKEN): %d%s.'
            % (len(broken), (': ' + ', '.join(
                '`%s` -> `%s`' % (k, m) for k, m in broken))
                if broken else ''))
    add('')
    add('## Printed')
    add('')
    for n in printed:
        add('### `%s`' % n)
        add('')
        for f, l, code in o_sites[n]:
            add('- orrery `%s` line %d: `%s`' % (f, l, short(code)))
        for f, l, code, path in g_sites.get(n, []):
            add('- gallery `%s` line %d (config `%s`): `%s`'
                % (f, l, path, short(code)))
        add('')
    console_rows = [n for n in names if o_console[n]]
    if console_rows:
        add('## Printed to a terminal only')
        add('')
        add('A tool logging a value is not a display a visitor sees, so '
            'these are not counted above.')
        add('')
        for n in console_rows:
            for f, l, code in o_console[n]:
                add('- `%s`: orrery `%s` line %d: `%s`'
                    % (n, f, l, short(code)))
        add('')
    add('## Not printed')
    add('')
    add('No display prints these exact rows. Under Rule 7 they '
        'carry no print count. The number is how many other orrery lines '
        'name the row, so a use that prints it through another name can '
        'still be found by reading those lines.')
    add('')
    for n in unprinted:
        add('- `%s`: named on %d other orrery line(s).' % (n, o_uses[n]))
    add('')
    add('## How the search works')
    add('')
    add('Orrery: every tracked `.py` file outside `documentation/`, except '
        '`constants_new.py` and this tool, searched for each exact row\'s '
        'name inside `{...}` in a formatted string, as the argument of '
        '`_declared`, `_whole_figures` or `_with_uncertainty`, after `%`, '
        'or inside `str(...)` or `format(...)`. Comment lines are skipped.')
    add('')
    add('Gallery: each pointer in `data/objects_config.json` to an exact '
        'row, followed to its print lines by the PRINTS table in the tool: '
        'the page script, the function and a piece of the print line. '
        'A pointer with no entry, or an entry that matches nothing, is '
        'reported above rather than dropped. '
        'Page scripts read: %s.'
        % (', '.join('`%s`' % s for s in gallery_scripts())
           if gallery_read else 'none (not read)'))
    add('')
    add('Not searched: an exact row\'s value typed into text as words or '
        'digits instead of read from the row.')
    add('')

    text = '\n'.join(lines)
    old = None
    if os.path.exists(OUT):
        with open(OUT, 'r', encoding='utf-8', newline='') as handle:
            old = handle.read()
    if old is None or old.replace('\r\n', '\n') != text:
        with open(OUT, 'w', encoding='utf-8', newline='\n') as handle:
            handle.write(text)

    summary = ('EXACT ROWS PRINTED: %d of %d exact rows printed at %d lines '
               '(%d orrery, %s gallery)'
               % (len(printed), len(names), len(o_lines) + len(g_lines),
                  len(o_lines), len(g_lines) if gallery_read else 'NOT READ'))
    if gallery_read:
        summary += '; %d not followed, %d map entries broken' % (
            len(not_followed), len(broken))
    else:
        summary += '; the gallery folder was not found'
    print(summary)
    return 0


if __name__ == '__main__':
    sys.exit(main())
