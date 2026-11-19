"""
patch_L432_1_colors_to_drawing_code.py - moves the orrery's colour table
out of constants_new.py into its own drawing module, orrery_colors.py.

RUN COMMAND
    Save this file in the orrery folder (palomas_orrery_for_github),
    open it in VS Code and click Run:

        python patch_L432_1_colors_to_drawing_code.py

    Success: one "ok" line per step, then "patch applied".
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop (and delete
    orrery_colors.py, which is new).

WHY (L-432)
    Tony's ruling of 2026-09-22 (provenance-discipline, Three Kinds of
    Drawing Number): a colour is a rendering setting, "defined in the code
    not in constants new". The colour table, color_map(), still sat in
    constants_new.py, the store of measured values, where the Constants
    change check reads every changed line holding a digit as a value that
    moved. A colour line holds digits ("rgb(188, 39, 50)", "EM-L1"), so
    every colour change turned the run red, and new bodies were left in
    the default goldenrod (2026 ED138, Oct 28; the eight Lagrange points,
    Nov 18, which Session 1 of L-297 routed around with a name map).

WHAT IT DOES, in four files
    1. orrery_colors.py (NEW): color_map() moved here whole, byte for
       byte, then three changes inside it: the eight Lagrange points'
       lines carry the names shown (Earth-Moon L1 ... Earth-Sun L5) in
       the colours they had; the two L3 lines go (JPL has no L3, L-297);
       and the name map's lookup goes.
    2. constants_new.py: the function's block is replaced by one import,
       so the six modules that import color_map from it still work
       (palomas_orrery.py, palomas_orrery_helpers.py, idealized_orbits.py,
       apsidal_markers.py, orbital_param_viz.py, test_orbit_markers.py).
       Its docstring gains a stamp.
    3. celestial_objects.py: COLOR_KEY_BY_NAME (Session 1's name map) and
       the comment pointing at it go; a stamp.
    4. constants_change_report.py: it learns the shape of a colour line.
       A REMOVED colour line is named and passes: a rendering setting
       leaving the store, as ruled. An ADDED one fails, with the reason:
       a colour belongs in orrery_colors.py. It runs a self-test of that
       rule every time it runs, with a planted loose pattern that must be
       caught, so the new rule can fail where it is used.

    Before writing, the patch checks that the moved color_map gives the
    same colour as the old one for every name the old table held, but the
    ten Lagrange keys it renames or drops, and names those ten.

PERMANENT PARTS (this script itself is one-shot; archive it to
the documentation folder once it has run): orrery_colors.py; the import in
constants_new.py; the colour-line rule and its self-test in
constants_change_report.py.

AFTER IT RUNS
    1. The orrery's maintenance run. Constants change should pass,
       naming the colour lines removed; Tier-1 0 on the gate path.
    2. Open the orrery, tick a few Lagrange points and two planets, and
       see their colours.
    3. Commit and push in GitHub Desktop (not while a night is running).

Built on palomas_orrery @ a70d98c58d9227432fe11831339d60d7bf55fe24 (the push of L-297), Nov 19, 2026,
with Anthropic's Claude Opus 5.5 (coordinating session).
"""

import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# LF-normalised md5 of each target as pushed at the base above.
FINGERPRINTS = {
    'constants_new.py': '378600f7ae1fee525ad088d9872d0088',
    'celestial_objects.py': '7df6d89a44bf762dec2bf7bdf2c1d476',
    'constants_change_report.py': '51163716be15580795bc097cb0da099b',
}
NEW_FILE = 'orrery_colors.py'

STAMP_DATE = 'November 19, 2026'
MODEL = "Anthropic's Claude Opus 5.5"

BLOCK_START = "def color_map(planet):\n"
BLOCK_END = "    return colors.get(planet, 'goldenrod')\n"

# The eight Lagrange lines renamed, the two L3 lines dropped (L-297).
RENAMES = [
    ("        'EM-L1': 'cyan',        \n", "        'Earth-Moon L1': 'cyan',\n"),
    ("        'EM-L2': 'white',\n", "        'Earth-Moon L2': 'white',\n"),
    ("        'EM-L3': 'green',\n", ""),
    ("        'EM-L4': 'magenta',\n", "        'Earth-Moon L4': 'magenta',\n"),
    ("        'EM-L5': 'red',\n", "        'Earth-Moon L5': 'red',\n"),
    ("        'L1': 'cyan',        \n", "        'Earth-Sun L1': 'cyan',\n"),
    ("        'L2': 'white',\n", "        'Earth-Sun L2': 'white',\n"),
    ("        'L3': 'green',\n", ""),
    ("        'L4': 'magenta',\n", "        'Earth-Sun L4': 'magenta',\n"),
    ("        'L5': 'red',\n", "        'Earth-Sun L5': 'red',\n"),
]
OLD_KEYS = ['EM-L1', 'EM-L2', 'EM-L3', 'EM-L4', 'EM-L5',
            'L1', 'L2', 'L3', 'L4', 'L5']
NEW_NAMES = {'Earth-Moon L1': 'EM-L1', 'Earth-Moon L2': 'EM-L2',
             'Earth-Moon L4': 'EM-L4', 'Earth-Moon L5': 'EM-L5',
             'Earth-Sun L1': 'L1', 'Earth-Sun L2': 'L2',
             'Earth-Sun L4': 'L4', 'Earth-Sun L5': 'L5'}

ALIAS_LOOKUP = (
    "    # A name shown that is not one of the table's keys is first turned\n"
    "    # into its key: the Lagrange points (L-297) show Tony's names and keep\n"
    "    # their colour lines under JPL's. The map is in celestial_objects.py.\n"
    "    from celestial_objects import COLOR_KEY_BY_NAME\n"
    "    planet = COLOR_KEY_BY_NAME.get(planet, planet)\n")

NEW_MODULE_HEAD = '''"""
orrery_colors.py - The orrery's colour for each body it draws, by the name
it shows.

A colour is a rendering setting: it says how a body is drawn, not what the
body is, so it lives in the drawing code and needs no source (Tony's ruling
of 2026-09-22, provenance-discipline's Three Kinds of Drawing Number:
"defined in the code not in constants new"). Until 2026-11-19 this table
sat in constants_new.py, the store of measured values, where the Constants
change check read each changed colour line as a value that moved (L-432).
The table is keyed by the name a body shows (its 'name' in
celestial_objects.py, or its 'color_key' where one is set); a name the
table does not hold is drawn in 'goldenrod'.

Key functions:
    color_map(name) - the colour for a body's name, or 'goldenrod'

Consumed by: constants_new.py re-exports it, so the six modules that
import it from there still work: palomas_orrery.py,
palomas_orrery_helpers.py, idealized_orbits.py, apsidal_markers.py,
orbital_param_viz.py and test_orbit_markers.py. celestial_objects.py's
build_objects_list() is handed it as color_map_func.
Picking a colour is Mode 5: Tony's eye on the bodies it is drawn beside.

Domain: orrery

Module updated: %s with %s (L-432: moved here
from constants_new.py whole; the eight Lagrange points keyed by the names
they show, the two L3 lines gone, as JPL has no L3, L-297.)
"""


''' % (STAMP_DATE, MODEL)

CONSTANTS_POINTER = (
    "# color_map() moved to orrery_colors.py on 2026-11-19 (L-432): a colour\n"
    "# is a rendering setting and lives in the drawing code (provenance-\n"
    "# discipline, Three Kinds of Drawing Number; Tony, 2026-09-22). This\n"
    "# import keeps every \"from constants_new import color_map\" working.\n"
    "from orrery_colors import color_map\n")

CONSTANTS_STAMP_ANCHOR = (
    "read, so the eight points keep their colours under their new names.)\n"
    '"""\n')
CONSTANTS_STAMP_NEW = (
    "read, so the eight points keep their colours under their new names.)\n"
    "Module updated: %s with %s\n"
    "(L-432: color_map() moved to orrery_colors.py, a drawing module, and\n"
    "re-exported here by one import; the name map of the line above went\n"
    "with it, as the table now holds the eight points' names shown.)\n"
    '"""\n') % (STAMP_DATE, MODEL)

CELESTIAL_COMMENT_OLD = (
    "    # the colour table (constants_new.py, color_map) keeps its lines\n"
    "    # under JPL's names; COLOR_KEY_BY_NAME, after this list, turns each\n"
    "    # name shown into its key, so no colour line changed (L-432).\n")
CELESTIAL_COMMENT_NEW = (
    "    # the colour table (orrery_colors.py, color_map) holds a line for\n"
    "    # each point under the name shown (L-432, 2026-11-19).\n")

CELESTIAL_MAP_START = "# A name shown -> the key of its line in the colour table\n"
CELESTIAL_MAP_END = "    'Earth-Sun L5': 'L5',\n}\n\n\n"

CELESTIAL_DOCARG_OLD = "color_map_func: The color_map function from constants_new"
CELESTIAL_DOCARG_NEW = ("color_map_func: The color_map function (orrery_colors.py,"
                        " re-exported by constants_new)")

CELESTIAL_STAMP_ANCHOR = (
    'the NASA: "..." form, with that page as its link, by Tony\'s choices.)\n'
    '"""\n')
CELESTIAL_STAMP_NEW = (
    'the NASA: "..." form, with that page as its link, by Tony\'s choices.)\n'
    "Module updated: %s with %s (L-432: COLOR_KEY_BY_NAME,\n"
    "the name map L-297 added, removed; the colour table, now\n"
    "orrery_colors.py, holds the Lagrange points under the names shown.)\n"
    '"""\n') % (STAMP_DATE, MODEL)

# ---- constants_change_report.py -----------------------------------------

REPORT_STAMP_ANCHOR = (
    "    equator tilt, an angle worked out with acos, is understood).\n"
    '"""\n')
REPORT_STAMP_NEW = (
    "    equator tilt, an angle worked out with acos, is understood).\n"
    "Module updated: %s with %s\n"
    "    (L-432: a colour line, 'Name': 'colour', is read as a rendering\n"
    "    setting. Removed, it is named and passes, as the colour table left\n"
    "    for orrery_colors.py; added, it fails, since a colour belongs in\n"
    "    the drawing code. A self-test of the shape runs first, every run,\n"
    "    with a planted loose pattern it must catch.)\n"
    '"""\n') % (STAMP_DATE, MODEL)

REPORT_RE_ANCHOR = "COMMENT_RE = re.compile(r'^\\s*#')\n"
REPORT_RE_NEW = REPORT_RE_ANCHOR + r'''
# A colour line, 'Name': '<colour>', with either kind of quote, where the
# colour is a CSS name, a hex code, or rgb() / rgba() of plain numbers.
# It holds no value this check judges: a colour is a rendering setting
# (provenance-discipline, Three Kinds of Drawing Number; Tony,
# 2026-09-22). Since L-432 (2026-11-19) the table is orrery_colors.py, so
# a REMOVED colour line is named and passes, and an ADDED one fails: a
# colour belongs in the drawing code. Only a line holding a digit is
# taken (a colour line without one was never read as a value).
_COLOUR_NUM = r'\d+(?:\.\d+)?%?'
COLOUR_RE = re.compile(
    r"""^\s*(?:'(?P<k1>[^']+)'|"(?P<k2>[^"]+)")\s*:\s*"""
    r"""(?P<q>['"])(?:[A-Za-z]+|#[0-9A-Fa-f]{3,8}"""
    r'|rgba?\(\s*' + _COLOUR_NUM + r'(?:\s*,\s*' + _COLOUR_NUM
    + r'){2,3}\s*\))'
    r"""(?P=q)\s*,?\s*(?:#.*)?$""")


def take_colour_lines(diff_text, pattern=None):
    """Take the colour lines out of a diff, before its values are read.

    Returns (removed, added, rest): the names of the colour lines the diff
    removes and adds, in diff order, and the diff without those lines, for
    read_changes(). A colour line is a changed line holding a digit that
    matches COLOUR_RE (or `pattern`, which the self-test plants).
    """
    pattern = pattern or COLOUR_RE
    removed, added, kept = [], [], []
    for line in diff_text.split('\n'):
        body = line[1:]
        if (line[:1] in '+-' and not line.startswith(('+++', '---'))
                and any(ch.isdigit() for ch in body)):
            m = pattern.match(body)
            if m:
                name = m.groupdict().get('k1') or m.groupdict().get('k2')
                (removed if line[0] == '-' else added).append(
                    name or body.strip())
                continue
        kept.append(line)
    return removed, added, '\n'.join(kept)


# Each case: a diff line, and what it must be read as.
_COLOUR_CASES = [
    ("-        'Mars': 'rgb(188, 39, 50)',", 'removed'),
    ("-        'EM-L1': 'cyan',        ", 'removed'),
    ('-        "Hi\'iaka": \'rgb(200, 180, 220)\',    # Light purple',
     'removed'),
    ("+        'Ceres': 'rgb(1, 2, 3)',", 'added'),
    ("-        'Mass': '5.97e24 kg',", 'value'),
    ("-        'Odd': 'rgb(1, 2)',", 'value'),
    ("-    KM_PER_AU = 149597870.7", 'value'),
]
_LOOSE = re.compile(
    r"""^\s*(?:'(?P<k1>[^']+)'|"(?P<k2>[^"]+)")\s*:\s*['"].*""")


def _judge(pattern):
    """How many of the cases `pattern` reads as each case says."""
    right = 0
    for line, want in _COLOUR_CASES:
        removed, added, _rest = take_colour_lines(line, pattern)
        got = 'removed' if removed else 'added' if added else 'value'
        right += (got == want)
    return right


def colour_self_test():
    """True when the rule reads every case right and a loose one does not."""
    n = len(_COLOUR_CASES)
    right = _judge(COLOUR_RE)
    loose_right = _judge(_LOOSE)
    print('  colour lines: self-test %d of %d cases read right; a planted'
          ' loose pattern misread %d' % (right, n, n - loose_right))
    return right == n and loose_right < n


def report_colours(removed, added):
    """Print the colour lines; True when one was ADDED (a failure)."""
    if removed:
        print('  %d colour line(s) removed -- a rendering setting leaving'
              ' this file (L-432):' % len(removed))
        print('      ' + ', '.join(removed))
    if added:
        print('  %d colour line(s) ADDED -- a colour belongs in'
              ' orrery_colors.py, not here (L-432):' % len(added))
        print('      ' + ', '.join(added))
    if removed or added:
        print()
    return bool(added)
'''

REPORT_MAIN_TEST_ANCHOR = (
    "    print('  comparing against %s' % resolved.strip())\n"
    "    print()\n")
REPORT_MAIN_TEST_NEW = (
    "    print('  comparing against %s' % resolved.strip())\n"
    "    if not colour_self_test():\n"
    "        print('  The colour-line rule failed its own self-test.')\n"
    "        print('  Nothing was checked. This is not a pass.')\n"
    "        return 2\n"
    "    print()\n")

REPORT_MAIN_SPLIT_ANCHOR = (
    "    docstrings, doc_note = docstring_lines(here, base)\n")
REPORT_MAIN_SPLIT_NEW = (
    "    colour_removed, colour_added, out = take_colour_lines(out)\n"
    "    colour_failed = report_colours(colour_removed, colour_added)\n"
    "    docstrings, doc_note = docstring_lines(here, base)\n")

REPORT_EARLY_ANCHOR = (
    "                  ' (%s).' % (len(doc_lines), doc_note))\n"
    "        return 0\n")
REPORT_EARLY_NEW = (
    "                  ' (%s).' % (len(doc_lines), doc_note))\n"
    "        return 1 if colour_failed else 0\n")

REPORT_FINAL_ANCHOR = (
    "    return 1 if (bare or unclear or unparsed or derived_bare\n"
    "                 or unreadable) else 0\n")
REPORT_FINAL_NEW = (
    "    return 1 if (bare or unclear or unparsed or derived_bare\n"
    "                 or unreadable or colour_failed) else 0\n")


# ---- the harness ---------------------------------------------------------

def fail(msg):
    print('ERROR: ' + msg)
    print('NOTHING was written. Undo is not needed.')
    sys.exit(1)


def read_lf(name):
    path = os.path.join(HERE, name)
    if not os.path.exists(path):
        fail('%s not found beside this script. Save the patch in the'
             ' orrery folder (palomas_orrery_for_github).' % name)
    raw = open(path, 'rb').read()
    return raw.replace(b'\r\n', b'\n').decode('utf-8'), b'\r\n' in raw


def replace_once(text, old, new, label, count=1):
    n = text.count(old)
    if n != count:
        print('ANCHOR FAIL: %s (expected %d match, found %d)'
              % (label, count, n))
        print('NOTHING was written.')
        sys.exit(1)
    print('ok ' + label)
    return text.replace(old, new)


def colours_of(block_source, names, extra=None):
    """Run a color_map block in its own namespace; colour for each name."""
    ns = dict(extra or {})
    exec(compile(block_source, '<color_map>', 'exec'), ns)
    return {n: ns['color_map'](n) for n in names}


def main():
    print('patch_L432_1: the colour table to the drawing code')
    texts, crlf = {}, {}
    for name, want in FINGERPRINTS.items():
        text, was_crlf = read_lf(name)
        got = hashlib.md5(text.encode('utf-8')).hexdigest()
        if got != want:
            fail('%s is not the file this patch was built on (md5 %s,'
                 ' expected %s). Pull origin first; if the push of L-297'
                 ' is in and this still refuses, tell Claude.'
                 % (name, got, want))
        texts[name], crlf[name] = text, was_crlf
        print('ok base: %s%s' % (name, ' [CRLF]' if was_crlf else ''))

    new_path = os.path.join(HERE, NEW_FILE)

    # 1. the block, and its moved form
    cn = texts['constants_new.py']
    if cn.count(BLOCK_START) != 1 or cn.count(BLOCK_END) != 1:
        fail('color_map() is not where it was in constants_new.py.')
    a = cn.index(BLOCK_START)
    b = cn.index(BLOCK_END) + len(BLOCK_END)
    old_block = cn[a:b]
    moved = replace_once(old_block, ALIAS_LOOKUP, '', 'moved: the name map lookup out')
    for old, new in RENAMES:
        moved = replace_once(moved, old, new,
                             'moved: %s' % (old.strip() + ' -> ' + (new.strip() or 'gone')))
    module_text = NEW_MODULE_HEAD + moved

    # 2. the same colour for every name, but the ten Lagrange keys
    keys = re.findall(r"""^\s*(?:'([^']+)'|"([^"]+)")\s*:""", old_block, re.M)
    names = sorted(set(k1 or k2 for k1, k2 in keys))
    stub = {'__builtins__': __builtins__}

    class _Stub:  # the old block imports the name map at call time
        COLOR_KEY_BY_NAME = NEW_NAMES
    sys.modules['celestial_objects'] = _Stub
    before = colours_of(old_block, names + list(NEW_NAMES), stub)
    del sys.modules['celestial_objects']
    after = colours_of(moved, names + list(NEW_NAMES), stub)
    differ = sorted(n for n in before if before[n] != after[n])
    if differ != sorted(OLD_KEYS):
        fail('the moved table does not give the same colours: these names'
             ' differ, %s; only the ten Lagrange keys may.' % differ)
    if any(after[n] != before[n] for n in NEW_NAMES):
        fail('a Lagrange point lost its colour in the move.')
    print('ok same colour for all %d names but the ten Lagrange keys (%s);'
          ' the eight names shown keep theirs' % (len(names) + len(NEW_NAMES)
                                                  - len(OLD_KEYS),
                                                  ', '.join(OLD_KEYS)))
    for text_, label in ((module_text, NEW_FILE),):
        compile(text_, label, 'exec')

    # 3. constants_new.py
    cn = cn[:a] + CONSTANTS_POINTER + cn[b:]
    print('ok constants_new.py: color_map() replaced by its import')
    cn = replace_once(cn, CONSTANTS_STAMP_ANCHOR, CONSTANTS_STAMP_NEW,
                      'constants_new.py: stamp')
    compile(cn, 'constants_new.py', 'exec')

    # 4. celestial_objects.py
    co = texts['celestial_objects.py']
    if co.count(CELESTIAL_MAP_START) != 1 or co.count(CELESTIAL_MAP_END) != 1:
        fail('COLOR_KEY_BY_NAME is not where it was in celestial_objects.py.')
    ma = co.index(CELESTIAL_MAP_START)
    mb = co.index(CELESTIAL_MAP_END) + len(CELESTIAL_MAP_END)
    co = co[:ma] + co[mb:]
    print('ok celestial_objects.py: COLOR_KEY_BY_NAME removed')
    co = replace_once(co, CELESTIAL_COMMENT_OLD, CELESTIAL_COMMENT_NEW,
                      'celestial_objects.py: the colours comment')
    co = replace_once(co, CELESTIAL_DOCARG_OLD, CELESTIAL_DOCARG_NEW,
                      'celestial_objects.py: build_objects_list docstring')
    co = replace_once(co, CELESTIAL_STAMP_ANCHOR, CELESTIAL_STAMP_NEW,
                      'celestial_objects.py: stamp')
    if 'COLOR_KEY_BY_NAME = {' in co:
        fail('celestial_objects.py still defines COLOR_KEY_BY_NAME.')
    users = []
    for root, dirs, files in os.walk(HERE):
        dirs[:] = [d for d in dirs if not d.startswith('.')
                   and d not in ('documentation', '__pycache__')]
        for fn in files:
            rel = os.path.relpath(os.path.join(root, fn), HERE)
            if (fn.endswith('.py') and rel not in FINGERPRINTS
                    and fn != os.path.basename(__file__)):
                with open(os.path.join(root, fn), 'rb') as f:
                    if b'COLOR_KEY_BY_NAME' in f.read():
                        users.append(rel)
    if users:
        fail('these files still use COLOR_KEY_BY_NAME: %s. Tell Claude.'
             % ', '.join(sorted(users)))
    print('ok no other .py file uses COLOR_KEY_BY_NAME')
    compile(co, 'celestial_objects.py', 'exec')

    # 5. constants_change_report.py
    rp = texts['constants_change_report.py']
    rp = replace_once(rp, REPORT_FINAL_ANCHOR, REPORT_FINAL_NEW,
                      'report: the colour failure in the final verdict')
    rp = replace_once(rp, REPORT_EARLY_ANCHOR, REPORT_EARLY_NEW,
                      'report: the colour failure in the no-value verdict')
    rp = replace_once(rp, REPORT_MAIN_SPLIT_ANCHOR, REPORT_MAIN_SPLIT_NEW,
                      'report: colour lines taken out before values are read')
    rp = replace_once(rp, REPORT_MAIN_TEST_ANCHOR, REPORT_MAIN_TEST_NEW,
                      'report: the self-test at every run')
    rp = replace_once(rp, REPORT_RE_ANCHOR, REPORT_RE_NEW,
                      'report: the colour-line rule')
    rp = replace_once(rp, REPORT_STAMP_ANCHOR, REPORT_STAMP_NEW,
                      'report: stamp')
    compile(rp, 'constants_change_report.py', 'exec')
    ns = {'__name__': 'patch_check'}
    exec(compile(rp, 'constants_change_report.py', 'exec'), ns)
    if not ns['colour_self_test']():
        fail('the colour-line rule fails its own self-test.')

    # 6. the bytes leaving are ASCII
    for label, text_ in ((NEW_FILE, module_text), ('constants_new.py', cn),
                         ('celestial_objects.py', co),
                         ('constants_change_report.py', rp)):
        bad = sum(1 for ch in text_ if ord(ch) > 127)
        if bad and label == NEW_FILE:
            fail('%s would hold %d non-ASCII character(s).' % (label, bad))
        if bad:
            print('note: %s holds %d non-ASCII character(s) this patch did'
                  ' not reach' % (label, bad))

    if os.path.exists(new_path):
        existing = open(new_path, 'rb').read().replace(b'\r\n', b'\n')
        if existing != module_text.encode('utf-8'):
            fail('%s already exists and differs from what this patch'
                 ' writes. If it is a copy saved by hand, delete it and run'
                 ' again.' % NEW_FILE)
        print('ok %s already there, identical' % NEW_FILE)

    # write: everything checked above
    for name, text_ in ((NEW_FILE, module_text), ('constants_new.py', cn),
                        ('celestial_objects.py', co),
                        ('constants_change_report.py', rp)):
        with open(os.path.join(HERE, name), 'wb') as f:
            f.write(text_.encode('utf-8'))
        note = ' (was CRLF; written LF)' if crlf.get(name) else ''
        print('ok written: %s%s' % (name, note))

    # the import still works, from a fresh interpreter
    probe = ("from constants_new import color_map as c; "
             "import orrery_colors as o; "
             "assert c is o.color_map; "
             "print(c('Mars'), c('Earth-Moon L1'), c('Earth-Sun L2'), "
             "c('no such body'))")
    run = subprocess.run([sys.executable, '-c', probe], cwd=HERE,
                         capture_output=True, text=True)
    if run.returncode != 0:
        print('FAILURE: the files are written, but constants_new.py does not'
              ' import cleanly:')
        print(run.stderr.strip()[-800:])
        print('Undo is Discard Changes in GitHub Desktop, and delete'
              ' orrery_colors.py. Then tell Claude.')
        sys.exit(1)
    print('ok import from a fresh interpreter: Mars, Earth-Moon L1,'
          ' Earth-Sun L2, an unknown name -> %s' % run.stdout.strip())

    print('patch applied')
    print()
    print('Still quoting the old place (not edited here): L-432 on the'
          ' ledger,')
    print("and provenance-discipline's note on rendering settings still in")
    print('constants_new.py. The close records both.')
    print()
    print('Do next:')
    print('  1. (do) Move this file into documentation\\.')
    print("  2. (do) The orrery's maintenance run: Constants change names")
    print('     the colour lines removed and passes; Tier-1 0.')
    print('  3. (look) Open the orrery: a few Lagrange points and two')
    print('     planets, in their colours.')
    print('  4. (do) Commit and push, not while a night is running.')


if __name__ == '__main__':
    main()
