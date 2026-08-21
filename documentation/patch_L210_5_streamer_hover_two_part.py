"""patch_L210_5_streamer_hover_two_part.py

Built on 9b9743d300070a69aac11229b9392845edb3488a at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
AFTER patch_L210_3 and patch_L210_4 have run, in that order.

Written August 20, 2026 with Anthropic's Claude Opus 5.

WHAT IS WRONG

We withdrew "helmet streamers extend 4-6 R_sun" from
constants_new.py this afternoon as unsourced. It kept rendering. The
claim lives at TEN sites of user-facing hover text across
solar_visualization_shells.py and spacecraft_encounters.py, plus a
source comment crediting "NASA Solar Wind / SOHO LASCO observations"
for it.

That is the parallel-pipeline failure in its plainest form: the
constant was fixed and the text that reaches the screen was not. A
user hovering the streamer belt shell right now reads a claim the code
no longer stands behind.

And it is not merely unsourced -- it is contradicted. Suess & Nerney
(2004), Adv. Space Res. 33:668, verified at source on 2026-08-20,
states that streamers extend to many solar radii while the closed
field regions -- the helmets -- reach no higher than 2-4 solar radii.
So "helmet streamers extending to 4-6" is wrong at both ends of the
range it names.

TONY'S RULING, 2026-08-20

Keep 6.0 as a visualization assumption. Let the hover text explain the
two-part reality and its ranges, with references. The shell is a rough
equivalent of the structure in any case, and saying so is more honest
than adopting one regime's number and presenting it as the boundary.

THE TWO-PART STRUCTURE, as the text now conveys it

  HELMET (closed magnetic loops)   below 2-4 R_sun   [Suess & Nerney 2004]
  STALK  (open field, current sheet)  many R_sun; studied 2-10 R_sun
                                      [Suess & Nerney 2004, 2005]
  The shell at 6.0                 inside the stalk band, above the
                                   helmet ceiling, a drawing choice

Suess & Nerney also make a point the old text never conveyed: the
brightness boundary seen in a coronagraph separates two FLOW REGIMES,
not plasma from vacuum. That is why a single sphere is an
approximation rather than a wrong number -- there is no surface there
to get right.

WHAT IT DOES -- 11 edits, no value changes
  solar_visualization_shells.py   9 hover sites + 1 source comment
  spacecraft_encounters.py        1 hover site

VERIFICATION. After the edits the patch re-scans BOTH files for any
surviving "4-6 R_sun" or "4-6 solar radii" and refuses to write if one
remains. The failure this repairs was a claim surviving in text nobody
re-read, so the check is a re-read that cannot be skipped.

AFTER RUNNING
  python -m py_compile solar_visualization_shells.py spacecraft_encounters.py
  Load the Sun's Streamer Belt shell and hover it -- Mode 5, your eyes
  are the gate.
  Re-run the maintenance runner.
  Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = '9b9743d300070a69aac11229b9392845edb3488a'

SHELLS = 'solar_visualization_shells.py'
ENCOUNTERS = 'spacecraft_encounters.py'

# State AFTER patch_L210_3 and patch_L210_4.
FINGERPRINTS = {
    SHELLS: '6b4fd9216ef90b165c3366516f76b7b5',
    ENCOUNTERS: '3411c454d05a3d25eddc02aa0da7b7ba',
}

REF = 'Suess & Nerney 2004, Adv. Space Res. 33:668'

EDITS = [
    (SHELLS, 'corona overview line',
     "    \"* The visible structured corona (helmet streamers) extends to ~4-6 R_sun.<br>\"\n",
     "    \"* Helmet streamers have two parts: closed loops below 2-4 R_sun, then<br>\"\n"
     "    \"  an open-field stalk reaching many R_sun (Suess & Nerney 2004).<br>\"\n"),

    (SHELLS, 'shell-list cross-reference',
     "    \"* Visible streamer belt: 4-6 R_sun (see Streamer Belt shell)<br>\"\n",
     "    \"* Visible streamer belt: drawn at 6.0 R_sun, an approximation<br>\"\n"
     "    \"  (see Streamer Belt shell)<br>\"\n"),

    (SHELLS, 'source comment on the info block',
     "# Source: constants_new.py STREAMER_BELT_RADII=6.0; NASA Solar Wind / SOHO LASCO observations\n",
     "# Source: constants_new.py STREAMER_BELT_RADII=6.0 -- a VISUALIZATION\n"
     "#   ASSUMPTION with no verified source (L-210). Ranges quoted below:\n"
     "#   Suess & Nerney 2004, Adv. Space Res. 33:668 (helmets below 2-4\n"
     "#   R_sun; streamers to many R_sun); Suess & Nerney 2005, Solar Wind\n"
     "#   11 / SOHO 16 (boundaries and stalks studied 2-10 R_sun);\n"
     "#   Decraemer et al. 2019, ApJ 883:152 (stalk as a plasma slab around\n"
     "#   a current sheet). See documentation/worksheets/\n"
     "#   worksheet_gemini-3-1-pro_streamer_extent_20260820.md\n"),

    (SHELLS, 'info block opening paragraph',
     "streamer_belt_info = (\n"
     "    \"Sun: Streamer Belt / Visible Corona:<br><br>\"\n"
     "\n"
     "    \"The streamer belt is the brightest, most structured region of the visible solar corona,<br>\"\n"
     "    \"extending from the inner corona out to about 4-6 solar radii. This is the corona that<br>\"\n"
     "    \"observers see during total solar eclipses as a pearly white halo around the Sun.<br><br>\"\n"
     "\n"
     "    \"Three components of white-light corona:<br>\"\n",
     "streamer_belt_info = (\n"
     "    \"Sun: Streamer Belt / Visible Corona:<br><br>\"\n"
     "\n"
     "    \"The streamer belt is the brightest, most structured region of the visible<br>\"\n"
     "    \"solar corona, seen at total eclipse as a pearly white halo.<br><br>\"\n"
     "\n"
     "    \"IT HAS NO SINGLE OUTER RADIUS, and this shell is drawn at one anyway.<br>\"\n"
     "    \"A streamer is two structures stacked. The HELMET, a dome of closed<br>\"\n"
     "    \"magnetic loops, reaches no higher than 2-4 R_sun. Above its cusp the<br>\"\n"
     "    \"field opens and the solar wind draws it out into a STALK -- a thin<br>\"\n"
     "    \"current sheet reaching many solar radii, studied between 2 and 10.<br>\"\n"
     "    \"This shell sits at 6.0 R_sun: above the helmet, inside the stalk, and<br>\"\n"
     "    \"not a boundary anybody has measured. It is a drawing choice.<br>\"\n"
     "    \"(Suess & Nerney 2004, Adv. Space Res. 33:668; 2005, Solar Wind 11.)<br><br>\"\n"
     "\n"
     "    \"What you see at eclipse is a BRIGHTNESS boundary, and it divides two<br>\"\n"
     "    \"flow regimes rather than separating plasma from empty space. There is<br>\"\n"
     "    \"no surface there to get right.<br><br>\"\n"
     "\n"
     "    \"Three components of white-light corona:<br>\"\n"),

    (SHELLS, 'info block helmet bullet',
     "    \"* Helmet streamers: Bottle-shaped, dense magnetic structures extending to 4-6 R_sun.<br>\"\n"
     "    \"  Source of slow solar wind. Visible in coronagraphs and at eclipse.<br>\"\n",
     "    \"* Helmet streamers: Bottle-shaped, dense magnetic structures. The closed<br>\"\n"
     "    \"  helmet stays below 2-4 R_sun; its stalk continues far beyond.<br>\"\n"
     "    \"  Source of slow solar wind. Visible in coronagraphs and at eclipse.<br>\"\n"),

    (SHELLS, 'hover block opening paragraph',
     "streamer_belt_info_hover = (\n"
     "    \"Sun: Streamer Belt / Visible Corona:<br><br>\"\n"
     "\n"
     "    \"The streamer belt is the brightest, most structured region of the visible solar corona,<br>\"\n"
     "    \"extending from the inner corona out to about 4-6 solar radii. This is the corona that<br>\"\n",
     "streamer_belt_info_hover = (\n"
     "    \"Sun: Streamer Belt / Visible Corona:<br><br>\"\n"
     "\n"
     "    \"The brightest, most structured region of the visible solar corona. It has<br>\"\n"
     "    \"NO single outer radius: the closed helmet stays below 2-4 R_sun and its<br>\"\n"
     "    \"open stalk reaches many R_sun (Suess & Nerney 2004). This shell is drawn<br>\"\n"
     "    \"at 6.0 R_sun -- above the first, inside the second, and a drawing choice<br>\"\n"
     "    \"rather than a measured boundary. The eclipse edge divides two flow<br>\"\n"
     "    \"regimes, not plasma from vacuum. This is the corona that<br>\"\n"),

    (SHELLS, 'hover block helmet bullet',
     "    \"* Helmet streamers: Dense magnetic structures extending 4-6 R_sun. Source of slow solar wind.<br>\"\n",
     "    \"* Helmet streamers: closed loops below 2-4 R_sun, then a stalk reaching<br>\"\n"
     "    \"  many R_sun. Source of slow solar wind.<br>\"\n"),

    (SHELLS, 'shell menu line A',
     "    '* Streamer Belt (Visible Corona): 4-6 R_sun -- eclipse white-light corona<br>'\n",
     "    '* Streamer Belt (Visible Corona): drawn at 6.0 R_sun, approximate<br>'\n"),

    (SHELLS, 'shell menu line B',
     "    '* Streamer Belt (Visible Corona): 4-6 R_sun -- eclipse white-light corona<br>'\n",
     "    '* Streamer Belt (Visible Corona): drawn at 6.0 R_sun, approximate<br>'\n"),

    (SHELLS, 'create_sun_streamer_belt_shell docstring',
     "    Visible white-light corona / helmet streamer belt: ~4-6 solar radii.\n"
     "    This is the corona seen during total solar eclipses. Distinct from the\n"
     "    Alfven surface (plasma boundary) and the extended F-corona (dust-scattered).\n",
     "    Visible white-light corona / helmet streamer belt, drawn at 6.0 R_sun.\n"
     "    That radius is a VISUALIZATION ASSUMPTION, not a measured boundary\n"
     "    (L-210). The structure has two parts and no single outer radius: the\n"
     "    closed helmet stays below 2-4 R_sun and its open stalk reaches many\n"
     "    R_sun (Suess & Nerney 2004, Adv. Space Res. 33:668). 6.0 sits above\n"
     "    the first and inside the second.\n"
     "    This is the corona seen during total solar eclipses. Distinct from the\n"
     "    Alfven surface (plasma boundary) and the extended F-corona (dust-scattered).\n"),

    (ENCOUNTERS, 'Parker boundary note',
     "            Streamer Belt (~4-6 R_sun). Perihelion tp 14:22 UTC April 4 confirmed.\n",
     "            Streamer Belt (drawn at 6.0 R_sun, an approximation -- the closed\n"
     "            helmet stays below 2-4 R_sun and its stalk reaches many R_sun;\n"
     "            Suess & Nerney 2004). Perihelion tp 14:22 UTC April 4 confirmed.\n"),
]


def fail(message):
    print('ABORT: %s' % message)
    print('Nothing was written.')
    sys.exit(1)


def main():
    for path in (SHELLS, ENCOUNTERS):
        if not os.path.isfile(path):
            fail('%s not found. Run this from the repo root.' % path)

    originals, endings = {}, {}
    for path, expected in FINGERPRINTS.items():
        with open(path, 'rb') as handle:
            data = handle.read()
        endings[path] = b'\r\n' if b'\r\n' in data else b'\n'
        data = data.replace(b'\r\n', b'\n')
        actual = hashlib.md5(data).hexdigest()
        if actual != expected:
            fail('%s is not in the state patches _3 and _4 leave it in.\n'
                 '  expected md5 %s\n  actual   md5 %s\n'
                 '  Run patch_L210_3 then patch_L210_4 FIRST.'
                 % (path, expected, actual))
        originals[path] = data
        print('[base ok] %-32s md5 %s  (%s on disk)'
              % (path, actual, 'CRLF' if endings[path] == b'\r\n' else 'LF'))

    for path, data in originals.items():
        try:
            data.decode('ascii')
        except UnicodeDecodeError as exc:
            fail('%s carries non-ASCII at offset %d.' % (path, exc.start))
        print('[ascii ok] %s' % path)

    working = dict((p, d.decode('ascii')) for p, d in originals.items())

    # The two menu lines are byte-identical, so each replace must take the
    # FIRST remaining occurrence and the count must fall by one each time.
    for path, label, old, new in EDITS:
        count = working[path].count(old)
        if count < 1:
            fail('anchor for "%s" in %s not found.' % (label, path))
        if count > 1 and 'shell menu line' not in label:
            fail('anchor for "%s" in %s matched %d times; expected 1.'
                 % (label, path, count))
        working[path] = working[path].replace(old, new, 1)
        print('[anchor ok] %-38s %s' % (label, path))

    # THE CHECK. The failure being repaired is a withdrawn claim that
    # survived in text nobody re-read. So re-read, over the WHOLE file,
    # for both spellings, and refuse to write if one is left.
    for path in (SHELLS, ENCOUNTERS):
        survivors = []
        for number, line in enumerate(working[path].split('\n'), 1):
            if '4-6 R_sun' in line or '4-6 solar radii' in line:
                survivors.append((number, line.strip()))
        if survivors:
            print('')
            print('%d site(s) still carry the withdrawn range in %s:'
                  % (len(survivors), path))
            for number, line in survivors:
                print('  %5d  %s' % (number, line[:66]))
            fail('the repair is incomplete.')
        print('[verified] %-32s 0 surviving "4-6" claims' % path)

    for path in (SHELLS, ENCOUNTERS):
        try:
            compile(working[path], path, 'exec')
        except SyntaxError as exc:
            fail('patched %s does not parse: line %s, %s'
                 % (path, exc.lineno, exc.msg))
        print('[syntax ok] %s parses' % path)

    for path in (SHELLS, ENCOUNTERS):
        out = working[path].encode('ascii')
        if endings[path] == b'\r\n':
            out = out.replace(b'\n', b'\r\n')
        with open(path, 'wb') as handle:
            handle.write(out)
        print('[written] %-32s (%s preserved)'
              % (path, 'CRLF' if endings[path] == b'\r\n' else 'LF'))

    print('')
    print('NO VALUE CHANGED. STREAMER_BELT_RADII is still 6.0 and the shell')
    print('renders at the same radius. Only what the text CLAIMS has moved.')
    print('')
    print('MODE 5 -- this one needs your eyes, not a passing test. Load the')
    print("Sun's Streamer Belt shell and hover it. The text is longer than it")
    print('was; if it reads as a wall, say so and it gets cut rather than')
    print('kept because it is correct.')
    print('')
    print('NEXT:')
    print('  1. python -m py_compile %s %s' % (SHELLS, ENCOUNTERS))
    print('  2. Render and hover the Streamer Belt shell')
    print('  3. Re-run the maintenance runner')
    print('  4. Move this script to documentation/')


if __name__ == '__main__':
    main()
