r'''
patch_L254_1_dead_builder_markers.py -- L-254.

Marks the eight dead sphere-shell builders in
earth_visualization_shells.py as dead, in the one place a reader meets
them -- their own docstrings -- and opens the ledger row for the
codebase-wide sweep.

WHY THIS IS NEEDED. Sphere shells render through
SHELL_CONFIGS -> build_sphere_shell() -> create_info_marker(). The
per-body create_*_shell() functions predate that dispatch and were never
removed. They are imported at planet_visualization.py lines 129-139 and
called from nowhere, so an import list is the only evidence they still
exist, and reading one gives every impression of reading live code.
orrery_rendering.py's own docstring has said so since May 2026, in a
paragraph correcting an earlier sweep that edited those very dicts:
"the per-body inline-marker sweep edited the *_visualization_shells.py
inline dicts, which for sphere shells are NOT on the live dispatch path
(dead code)". Nothing in the modules themselves says it.

Patch L-249-2 had to reach into four of these functions to stop them
holding their own copies of Earth's boundary values, which is how the
question came up.

WHAT THIS PATCH DOES. Docstring markers only. No function is deleted, no
behaviour changes, nothing is renamed. Tony's ruling, 2026-08-26:
annotate now, sweep later under its own row.

THE CENSUS, measured at orrery fc25ef23c2ccab023bb905d77217c77187e6e2a1
rather than recalled. 82 create_*_shell functions are defined across 15
*_visualization_shells modules. Six are live, every one of them reached
through a CUSTOM_SHELLS 'builder' string resolved by
planet_visualization.py line 440's rsplit + getattr: the four
magnetospheres (Earth, Mars, Mercury, Venus) and Earth's LEO and
geostationary belt. The other 76 are dead. That is the only dynamic
dispatch path in the codebase -- there is no getattr-by-name or eval
route that could rescue one of the 76 -- which is what makes the count
safe to state.

    earth 8, solar 14, mars 7, jupiter 6, moon 6, pluto 6, saturn 6,
    venus 6, eris 5, neptune 5, uranus 5, planet9 2

Dead by MIGRATION, not by abandonment: each was superseded when its body
moved to shell_configs.py during Phases A-D. planet9_visualization_shells
says so in its own docstring -- "fully archivable once shell_configs.py
migration is complete."

RUN COMMAND (save this file into the repo root -- the same folder as
earth_visualization_shells.py and LEDGER_CONSOLIDATED.md -- open it in
VS Code and click Run, or from a terminal in that folder):

    python patch_L254_1_dead_builder_markers.py

Success prints one `ok` line per edit then `patch applied`. Any failure
prints a single ERROR:/ANCHOR FAIL line and writes nothing to either
file. One-shot: a second run aborts on the fingerprint.

RUN ORDER: after patch_L249_3. Afterwards run ledger_index.py, which
generates L-254's summary row and its RICE score.

PERMANENT: the edits to both files.
DISPOSABLE: this script. Archive it to documentation/ once it has run.
'''

import hashlib
import os
import sys

SHELLS = 'earth_visualization_shells.py'
LEDGER = 'LEDGER_CONSOLIDATED.md'

# md5 of the LF-normalised bases, orrery fc25ef23c2ccab023bb905d77217c77187e6e2a1
BASE_FP = {
    SHELLS: '93e4567213f115e4ec340358dbe82317',
    LEDGER: '6343d8bc945211fdb829a54c33d612ce',
}


def bb(text):
    return text.encode('ascii')


SECTION_OLD = bb('# Earth Shell Creation Functions')

SECTION_NEW = bb(r'''# Earth Shell Creation Functions
#
# DISPATCH, read this before editing anything below (L-254, 2026-08-26).
# Eleven create_earth_*_shell functions live in this file. THREE are on
# the live render path, all of them reached through a CUSTOM_SHELLS
# 'builder' string that planet_visualization.py resolves by rsplit and
# getattr:
#     create_earth_magnetosphere_shell
#     create_earth_leo_shell
#     create_earth_geostationary_belt_shell
# The other EIGHT are dead. They are imported at planet_visualization.py
# lines 129-139 and called nowhere. Sphere shells render through
# SHELL_CONFIGS -> build_sphere_shell() -> create_info_marker() instead,
# and have since the Phase A-D migration; orrery_rendering.py's docstring
# has recorded it since May 2026. Each dead function says so in its own
# docstring below.
#
# The _info strings above are NOT dead. They are the canonical `\n` form,
# read by the Tk checkbox tooltips through celestial_objects.
# get_shell_tooltip_names() and globals(), and imported by
# shell_configs.py, which derives `<br>` from them at the Plotly boundary.
# Editing one changes what the user reads in two places. Editing a dead
# function below changes nothing at all.''')

DEAD_MARKER = (
    '\n\n    DEAD CODE (L-254, 2026-08-26). Not on the render path: imported at\n'
    '    planet_visualization.py and called nowhere. This body renders its\n'
    '    sphere shells through SHELL_CONFIGS -> build_sphere_shell(). Edit\n'
    '    that config, not this function -- a change here renders nothing.\n'
    '    Retained pending the codebase-wide sweep in L-254.\n    ')

DEAD_DOCSTRINGS = [
    ('inner core', '"""Creates Earth\'s inner core shell."""'),
    ('outer core', '"""Creates Earth\'s outer core shell."""'),
    ('lower mantle', '"""Creates Earth\'s lower mantle shell."""'),
    ('upper mantle', '"""Creates Earth\'s upper mantle shell."""'),
    ('crust', '"""Creates Earth\'s crust shell using Mesh3d for better '
              'performance with improved hover."""'),
    ('lower atmosphere', '"""Creates Earth\'s lower atmosphere shell."""'),
    ('upper atmosphere', '"""Creates Earth\'s upper atmosphere shell."""'),
    ('hill sphere', '"""Creates Earth\'s Hill sphere."""'),
]

DOC_OLD = bb(r'''August 26, 2026 (L-249, Opus 5): the four interior info strings stop''')

DOC_NEW = bb(r'''August 26, 2026 (L-254, Opus 5): the eight dead create_earth_*_shell
    functions are marked as dead in their own docstrings, and the
    dispatch note above the section says which three are live. No
    function removed and no behaviour changed -- the sweep is L-254.
August 26, 2026 (L-249, Opus 5): the four interior info strings stop''')

LEDGER_ANCHOR = bb(r'''**Ref:** L-249 (the migration that surfaced it); L-194 (text-only
assertions); L-240 (measured vs declared); Fetched vs Recalled and Show
the Envelope of the Unknowable, resident protocol Part 3;
`constants_new.py::EARTH_D660_DEPTH_KM`.
''')

LEDGER_NEW = bb(r'''**Ref:** L-249 (the migration that surfaced it); L-194 (text-only
assertions); L-240 (measured vs declared); Fetched vs Recalled and Show
the Envelope of the Unknowable, resident protocol Part 3;
`constants_new.py::EARTH_D660_DEPTH_KM`.

#### [L-254] 76 dead sphere-shell builders, unmarked, across 12 modules
<!-- L:254 status:OPEN upd:2026-08-26 section:A flag: rice:3/3/95/3 -->
- **Measured, not recalled, at orrery `fc25ef23`.** 82
  `create_*_shell` functions are defined across 15
  `*_visualization_shells` modules. SIX are live, every one reached
  through a `CUSTOM_SHELLS` `'builder'` string that
  `planet_visualization.py` line 440 resolves by `rsplit('.', 1)` plus
  `getattr`: the Earth, Mars, Mercury and Venus magnetospheres, plus
  Earth's LEO and geostationary belt. The other **76 are dead** --
  defined, imported, called nowhere.
- **The count is safe to state because the dispatch is closed.** That
  builder-string lookup is the ONLY dynamic call route in the codebase:
  a repo-wide search for `getattr` on a shells module, for
  `globals()[...]` and for `eval` of a builder name returns nothing
  else. So a dead builder cannot be rescued by a path the census missed.
- **Dead by migration, not by abandonment.** Sphere shells render
  through `SHELL_CONFIGS` -> `build_sphere_shell()` ->
  `create_info_marker()`, and each per-body builder was superseded when
  its body moved to `shell_configs.py` in Phases A-D.
  `planet9_visualization_shells.py` says so in its own docstring:
  "fully archivable once shell_configs.py migration is complete."
- **Per module:** earth 8, solar 14, mars 7, jupiter 6, moon 6, pluto 6,
  saturn 6, venus 6, eris 5, neptune 5, uranus 5, planet9 2.
- **Why it is not cosmetic.** A dead function is indistinguishable from
  a live one while reading, and this project has already paid for that
  twice. In May 2026 an inline-marker sweep edited these dicts and
  rendered nothing;
  `orrery_rendering.py`'s docstring still carries the correction. On
  2026-08-26 `patch_L249_2` found four of them holding their own copies
  of Earth's interior boundary values -- a second store of a migrated
  constant, in code that cannot run, which would have read as
  authoritative to whoever found it next.
- **Done so far (`patch_L254_1`, 2026-08-26):** Earth's eight are marked
  in their own docstrings, and a dispatch note above the section names
  the three that are live. Annotation only. Tony's ruling the same day:
  annotate now, sweep later.
- **The remaining 68 carry no marker.** Solar's fourteen are the largest
  single block.
- **Note:** RICE 3/3/95/3 is Claude's proposed score. Effort 3 because
  deletion is not the only option -- archiving the modules, or keeping
  them as marked reference, are both live choices and that is a
  judgment call before it is a mechanical one.
  **Tony-action (decide):** confirm or redirect the score, and rule on
  whether the sweep deletes, archives, or annotates the remaining 68.
**Gap:** 68 dead builders across 11 modules are unmarked. Closing this
means one pass that either removes them or marks them, plus a decision
on whether the now-unused imports at `planet_visualization.py` lines
129-139 go with them.
**Ref:** L-249 (`patch_L249_2`, which surfaced it); L-191 (display-text
duplication, the same modules); `orrery_rendering.py` docstring, May 28
2026 correction; Verify Execution, Not Appearance [CRITICAL], resident
protocol Part 3.
''')


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def load(name):
    if not os.path.exists(name):
        print('ERROR: %s not found. Save this script into the repo root, '
              'beside %s and %s.' % (name, SHELLS, LEDGER))
        return (None, None)
    with open(name, 'rb') as handle:
        data = handle.read()
    fp = fingerprint(data)
    if fp != BASE_FP[name]:
        print('ERROR: BASE MOVED. %s fingerprints %s, expected %s.'
              % (name, fp, BASE_FP[name]))
        print('       Nothing written to either file. If this patch already '
              'ran, that is the expected result of a second run.')
        return (None, None)
    is_crlf = data.count(b'\r\n') > 0
    print('ok   base fingerprint %s (%s, %d bytes, %s)'
          % (fp, name, len(data), 'CRLF' if is_crlf else 'LF'))
    return (data, is_crlf)


def apply_edits(data, is_crlf, edits):
    for label, old, new in edits:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = data.count(old)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, got %d: %r'
                  % (label, count, old[:70]))
            print('             Nothing written to either file.')
            return None
        data = data.replace(old, new, 1)
        print('ok   %s' % label)
    return data


def main():
    shells, s_crlf = load(SHELLS)
    if shells is None:
        return 1
    ledger, l_crlf = load(LEDGER)
    if ledger is None:
        return 1

    edits = [
        ('shells docstring stamp', DOC_OLD, DOC_NEW),
        ('dispatch note above the section', SECTION_OLD, SECTION_NEW),
    ]
    for label, doc in DEAD_DOCSTRINGS:
        marked = doc[:-3] + DEAD_MARKER + '"""'
        edits.append(('%s marked dead' % label, bb(doc), bb(marked)))

    shells = apply_edits(shells, s_crlf, edits)
    if shells is None:
        return 1

    ledger = apply_edits(ledger, l_crlf, [
        ('L-254 detail block', LEDGER_ANCHOR, LEDGER_NEW),
    ])
    if ledger is None:
        return 1

    for raw in (SECTION_NEW, LEDGER_NEW, DOC_NEW):
        try:
            raw.decode('ascii')
        except UnicodeDecodeError as exc:
            print('ERROR: non-ASCII byte in inserted text: %s' % exc)
            return 1
    print('ok   encoding gate -- inserted lines are ASCII')

    s_text = shells.decode('ascii').replace('\r\n', '\n')
    l_text = ledger.decode('ascii').replace('\r\n', '\n')

    # Exactly eight functions marked -- not seven, and not the three live
    # ones by accident.
    marked = s_text.count('DEAD CODE (L-254, 2026-08-26)')
    if marked != len(DEAD_DOCSTRINGS):
        print('ERROR: post-condition -- %d functions marked, expected %d.'
              % (marked, len(DEAD_DOCSTRINGS)))
        return 1
    print('ok   post-condition -- %d functions marked dead' % marked)

    # The three LIVE builders must be untouched. This is the check that
    # matters: marking a live function as dead would be worse than
    # marking nothing, because the next reader would believe it.
    for live in ('create_earth_magnetosphere_shell',
                 'create_earth_leo_shell',
                 'create_earth_geostationary_belt_shell'):
        start = s_text.index('def %s(' % live)
        body = s_text[start:start + 900]
        if 'DEAD CODE' in body:
            print('ERROR: post-condition -- %s is LIVE and has been marked '
                  'dead.' % live)
            return 1
    print('ok   post-condition -- the three live builders carry no marker')

    if l_text.count('#### [L-254]') != 1:
        print('ERROR: post-condition -- L-254 appears %d times.'
              % l_text.count('#### [L-254]'))
        return 1
    row_start = l_text.index('#### [L-254]')
    row = l_text[row_start:l_text.index('## PENDING ACTION', row_start)]
    if '<!-- L:254 ' not in row:
        print('ERROR: post-condition -- L-254 has no metadata comment, so '
              'ledger_index.py will not index it.')
        return 1
    for figure in ('82', '76', '68', 'fc25ef23'):
        if figure not in row:
            print('ERROR: post-condition -- the census figure %r did not '
                  'reach the L-254 row.' % figure)
            return 1
    print('ok   post-condition -- L-254 carries its census and its anchor')

    with open(SHELLS, 'wb') as handle:
        handle.write(shells)
    with open(LEDGER, 'wb') as handle:
        handle.write(ledger)
    print('patch applied (%s %d bytes, %s %d bytes)'
          % (SHELLS, len(shells), LEDGER, len(ledger)))
    print('')
    print('Next: python ledger_index.py, then maintenance_run.py. No render')
    print('changes in this patch -- nothing to look at in the orrery.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
