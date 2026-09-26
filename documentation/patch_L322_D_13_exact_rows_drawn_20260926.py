#!/usr/bin/env python3
"""
patch_L322_D_13_exact_rows_drawn_20260926.py -- L-322 Stage D, patch D13:
the exact-rows report learns that a gallery pointer can be read only to
place a drawing.

Built on orrery 43ba290b20ed17aee22a9bb7c121ff0b1a8fca3e at
https://github.com/tonylquintanilla/palomas_orrery, tested against gallery
c6000f03324fc6cdf1d192d0c1c77b91c10dd25f at
https://github.com/tonylquintanilla/tonyquintanilla.github.io with gallery
patch 3 applied. Run it AFTER gallery patch 3.

WHAT IT DOES

    exact_rows_report.py gains a DRAWN table beside PRINTS: gallery
    pointers to exact rows that are read to shape a drawing and never
    printed -- the magnetotail's drawn radius and drawn end, and Earth's
    two fallback pole rows. Each entry names the line that reads the
    value, and is reported BROKEN if that line is gone, if it is a print
    line, or if no pointer reaches it. Without this, those four pointers
    would be reported NOT FOLLOWED on every run.

    It also writes the two run records for this session into
    documentation/: this patch's and gallery patch 3's.

FILES

    changed  exact_rows_report.py
    new      documentation/RUN_RECORD_L322_D13_20260926.md
    new      documentation/RUN_RECORD_L322_D_p3_gallery_20260926.md

    Permanent: all three. This script is one-shot; archive it to
    documentation/ once it has run.

RUN COMMAND

    Save this file in the orrery repo root (the folder holding
    constants_new.py), open it in VS Code, and click Run.

        python patch_L322_D_13_exact_rows_drawn_20260926.py

    Success: one "ok" line per file, then "PATCH APPLIED" and the next
    steps. Failure: "FAILURE: ..." and NOTHING is written. Undo after a
    success is Discard Changes in GitHub Desktop.

Written September 26, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

TARGETS = [
    ('exact_rows_report.py', 'ae137de2d32ae5769719a7803adf39e1', [
        (b'\nCONSOLE LINES. A tool that prints an exact row to the terminal, such\n',
         b'\nDRAWN, NOT PRINTED. Some gallery pointers to exact rows are read only to\nplace a drawing and never printed: the magnetotail\'s drawn radius and\ndrawn end, which shape the tail while the hover prints the measured rows\nbeside them, and Earth\'s fallback pole, which places the axis when no\npole of date is served. A second hand-kept table, DRAWN, names for each\nthe page script, the function and a piece of the line that reads the\nvalue. The tool checks it the same way: an entry whose line is gone is\nBROKEN, and so is one whose line turns out to be a print line, because\nthen the value is printed after all and belongs in PRINTS. A drawn-only\nrow is listed under "Not printed", with the line that reads it.\n\nCONSOLE LINES. A tool that prints an exact row to the terminal, such\n'),
        (b'(L-322 Stage D, patch D12: new.)\n"""\n',
         b'(L-322 Stage D, patch D12: new.)\nModule updated: September 26, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D13: the DRAWN table, for gallery pointers to exact\nrows that are read only to place a drawing -- gallery patch 3 added four\n-- checked like PRINTS, so they are reported as drawn and not as NOT\nFOLLOWED.)\n"""\n'),
        (b"        ('gallery/feature_renderers.js', 'renderShellSet', 'km.altitudeKm'),\n}\n",
         b"        ('gallery/feature_renderers.js', 'renderShellSet', 'km.altitudeKm'),\n}\n\n# Gallery pointers to exact rows that are read only to place a drawing\n# and never printed. Same key and value as PRINTS, but the piece of code\n# is on the line that READS the value. Checked every run: an entry whose\n# line is gone, or whose line is a print line, is BROKEN. (L-322 Stage D,\n# patch D13, for the four pointers gallery patch 3 added.)\nDRAWN = {\n    'earth_magnetosphere/magnetotail/drawn_radius':\n        ('gallery/feature_renderers.js', 'renderMagnetosphere',\n         'tl.drawn_radius'),\n    'earth_magnetosphere/magnetotail/drawn_end':\n        ('gallery/feature_renderers.js', 'renderMagnetosphere',\n         'tl.drawn_end'),\n    'orientation/pole/ra':\n        ('gallery/feature_renderers.js', 'basisFor', 'pole.ra'),\n    'orientation/pole/dec':\n        ('gallery/feature_renderers.js', 'basisFor', 'pole.dec'),\n}\n"),
        (b'\ndef map_entry(path):\n    """The PRINTS entry for a pointer path, or None."""\n    for suffix, entry in PRINTS.items():\n        if path.endswith(\'/\' + suffix):\n',
         b'\ndef map_entry(path, table=None):\n    """The PRINTS (or given table\'s) entry for a pointer path, or None."""\n    for suffix, entry in (PRINTS if table is None else table).items():\n        if path.endswith(\'/\' + suffix):\n'),
        (b'def gallery_sites(pointers):\n    """({row: [(file, line, code, path)]}, not_followed, broken)."""\n    print_lines = []\n    for rel in gallery_scripts():\n',
         b'def gallery_sites(pointers):\n    """({row: [(file, line, code, path)]}, not_followed, broken, drawn).\n\n    drawn is {row: [(file, line, code, path)]} for pointers the DRAWN\n    table names, each the line that reads the value."""\n    print_lines = []\n    code_lines = []\n    for rel in gallery_scripts():\n'),
        (b'                continue\n            if GALLERY_PRINT_RE.search(line):\n                print_lines.append((rel, owner, number, stripped))\n',
         b'                continue\n            is_print = bool(GALLERY_PRINT_RE.search(line))\n            code_lines.append((rel, owner, number, stripped, is_print))\n            if is_print:\n                print_lines.append((rel, owner, number, stripped))\n'),
        (b'    sites = {}\n    not_followed = []\n    used = set()\n    for row, path, _key in pointers:\n',
         b'    sites = {}\n    drawn = {}\n    not_followed = []\n    used = set()\n    drawn_broken = []\n    for row, path, _key in pointers:\n'),
        (b'        if found is None:\n            not_followed.append((row, path))\n            continue\n',
         b"        if found is None:\n            as_drawn = map_entry(path, DRAWN)\n            if as_drawn is None:\n                not_followed.append((row, path))\n                continue\n            suffix, (script, function, marker) = as_drawn\n            hits = [(f, n, code, is_print)\n                    for f, owner, n, code, is_print in code_lines\n                    if f == script and owner == function and marker in code]\n            if not hits:\n                drawn_broken.append((suffix, marker + ' (no line reads it)'))\n                continue\n            if any(is_print for _f, _n, _c, is_print in hits):\n                drawn_broken.append((suffix, marker + ' (on a print line: '\n                                     'it is printed, so it belongs in '\n                                     'PRINTS)'))\n                continue\n            for f, n, code, _p in hits:\n                drawn.setdefault(row, []).append((f, n, code, path))\n            continue\n"),
        (b'              if suffix not in used]\n    return sites, not_followed, broken\n\n',
         b"              if suffix not in used]\n    # A DRAWN entry that no pointer reaches can no longer vouch for\n    # anything either.\n    reached = set()\n    for _row, path, _key in pointers:\n        found = map_entry(path, DRAWN)\n        if found is not None:\n            reached.add(found[0])\n    broken += drawn_broken\n    broken += [(suffix, DRAWN[suffix][2] + ' (no pointer reaches it)')\n               for suffix in DRAWN if suffix not in reached]\n    return sites, not_followed, broken, drawn\n\n"),
        (b'    gallery_read = os.path.exists(os.path.join(GALLERY_DIR, GALLERY_CONFIG))\n    g_sites, not_followed, broken, pointers = {}, [], [], []\n    if gallery_read:\n',
         b'    gallery_read = os.path.exists(os.path.join(GALLERY_DIR, GALLERY_CONFIG))\n    g_sites, not_followed, broken, pointers, g_drawn = {}, [], [], [], {}\n    if gallery_read:\n'),
        (b'        pointers = config_pointers(config, names)\n        g_sites, not_followed, broken = gallery_sites(pointers)\n\n',
         b'        pointers = config_pointers(config, names)\n        g_sites, not_followed, broken, g_drawn = gallery_sites(pointers)\n\n'),
        (b"                if not_followed else ''))\n        add('- PRINTS entries that no longer match a pointer or a print line '\n            '(BROKEN): %d%s.'\n            % (len(broken), (': ' + ', '.join(\n",
         b"                if not_followed else ''))\n        add('- Gallery pointers to exact rows read only to place a drawing '\n            '(DRAWN, not printed): %d%s.'\n            % (len(g_drawn), (': ' + ', '.join('`%s`' % r for r in g_drawn))\n               if g_drawn else ''))\n        add('- PRINTS or DRAWN entries that no longer match a pointer or '\n            'their line (BROKEN): %d%s.'\n            % (len(broken), (': ' + ', '.join(\n"),
        (b"        add('- `%s`: named on %d other orrery line(s).' % (n, o_uses[n]))\n    add('')\n",
         b"        add('- `%s`: named on %d other orrery line(s).' % (n, o_uses[n]))\n        for f, l, code, path in g_drawn.get(n, []):\n            add('  - gallery: read to draw, not printed, at `%s` line %d '\n                '(config `%s`): `%s`' % (f, l, path, short(code)))\n    add('')\n"),
        (b"        'the page script, the function and a piece of the print line. '\n        'A pointer with no entry, or an entry that matches nothing, is '\n",
         b"        'the page script, the function and a piece of the print line. '\n        'A pointer read only to place a drawing is named instead in the '\n        'DRAWN table, by the line that reads it, and that line must not '\n        'be a print line. '\n        'A pointer with no entry, or an entry that matches nothing, is '\n"),
        (b"    if gallery_read:\n        summary += '; %d not followed, %d map entries broken' % (\n            len(not_followed), len(broken))\n    else:\n",
         b"    if gallery_read:\n        summary += ('; %d drawn only, %d not followed, %d map entries broken'\n                    % (len(g_drawn), len(not_followed), len(broken)))\n    else:\n"),
    ]),
]

NEW_FILES = {
    'documentation/RUN_RECORD_L322_D13_20260926.md': b'# Run record -- L-322 Stage D, patch D13: drawn-only rows in the exact-rows report\n\n**Built on orrery `43ba290b20ed17aee22a9bb7c121ff0b1a8fca3e` at\nhttps://github.com/tonylquintanilla/palomas_orrery.** It reads the gallery\nfolder beside the orrery; tested against gallery\n`c6000f03324fc6cdf1d192d0c1c77b91c10dd25f` at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io with gallery\npatch 3 applied.\n\nRun it after gallery patch 3 (`RUN_RECORD_L322_D_p3_gallery_20260926.md`).\nIn that order, the one orrery maintenance run that reads both reports\nnothing not followed and nothing broken.\n\nWritten for Tony and for the sessions that act on the report.\n\n---\n\n## 1. Why\n\n`exact_rows_report.py` (patch D12) follows each gallery pointer to an\nexact row of `constants_new.py` to the line that prints it, through its\nPRINTS table, and reports a pointer with no entry as NOT FOLLOWED. It had\nno way to say a pointer is read only to place a drawing. Gallery patch 3\nadds four such pointers: the magnetotail\'s drawn radius and drawn end,\nwhich shape the tail while its hover prints the measured rows, and\nEarth\'s two fallback pole rows, which place the axis when no pole of date\nis served. Without this patch the report would call all four NOT\nFOLLOWED on every run: a permanent warning that is always wrong.\n\nThe orrery half already had the category ("Not printed"). This gives the\ngallery half the same one. Proposed at session start and confirmed by\nTony, 2026-09-26.\n\n## 2. What the patch changes\n\n- **`exact_rows_report.py`**: a second hand-kept table, DRAWN, keyed like\n  PRINTS: the page script, the function, and a piece of the line that\n  READS the value. An entry is BROKEN if no line in that function reads\n  it, if that line is a print line (then the value is printed and belongs\n  in PRINTS), or if no pointer reaches the entry. A drawn-only row is\n  listed under "Not printed" with the line that reads it. The summary line\n  gains "N drawn only". The four entries:\n  `earth_magnetosphere/magnetotail/drawn_radius` and `.../drawn_end` in\n  `renderMagnetosphere`, `orientation/pole/ra` and `.../dec` in `basisFor`.\n- **Two run records**, this one and gallery patch 3\'s, into\n  `documentation/`.\n\n## 3. How it was verified, in the sandbox\n\n- Against the patched gallery: "7 of 20 exact rows printed at 18 lines\n  (8 orrery, 10 gallery); 4 drawn only, 0 not followed, 0 map entries\n  broken". Without this patch, the same gallery gives "4 not followed".\n- It goes red when it should, each on a throwaway copy: the tail\'s\n  `tl.drawn_radius` read renamed, 1 broken; the pole\'s read line made a\n  print line, 1 broken; one DRAWN entry removed, 1 not followed; no\n  gallery folder, "NOT READ gallery".\n- Two runs with nothing changed write identical bytes.\n- The orrery maintenance run in the sandbox: the same four checkers fail\n  before and after the patch (Dimensions, Reset completeness, Orbit cache,\n  Earth pole of date), each because the sandbox lacks astropy, astroquery,\n  plotly or Tk; the other fifteen pass. On your machine all should pass.\n\n## 4. What your first run will change\n\nThe orrery maintenance run rewrites `EXACT_ROWS_PRINTED.md`: the DRAWN\nline in the summary and the four "read to draw" lines under Not printed.\nCommit it with the patch.\n\n## 5. Tony\'s run\n\n(Append the patch output and the maintenance run\'s "Exact rows report"\nline.)\n\n---\n\nSession written September 2026 with Anthropic\'s Claude Opus 5.5.\n',
    'documentation/RUN_RECORD_L322_D_p3_gallery_20260926.md': b'# Run record -- L-322 Stage D, gallery patch 3: the magnetotail and the belts\n\n**Built on gallery `c6000f03324fc6cdf1d192d0c1c77b91c10dd25f` at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io and orrery\n`43ba290b20ed17aee22a9bb7c121ff0b1a8fca3e` at\nhttps://github.com/tonylquintanilla/palomas_orrery.** Both HEADs read live\nwith `git ls-remote` on 2026-09-26, at the start of the session and again\nbefore the patch was written.\n\nThe patch is `patch_L322_D_p3_gallery_tail_belts_20260926.py`, run from the\ngallery root and archived to the gallery\'s `documentation/`. It runs\nbefore the orrery\'s patch D13 (see `RUN_RECORD_L322_D13_20260926.md`).\n\nRules this work ran under: protocol v3.69; provenance-discipline 2.19\n(the loaded copy read 2.19, discharging v3.69\'s obligation),\ninteractive-exhibit 1.4, gallery-cache-builder 1.6, gallery-assembler 1.3,\nsafe-file-editing 1.11, agentic-pre-test 1.2, ledger-and-session-records\n1.11. Every loaded copy was byte-identical to `skills/` at orrery\n`43ba290b`.\n\nWritten for Tony, a retired professional engineer who is not a\nprogrammer, and for the session that follows.\n\n---\n\n## 1. Rulings this session\n\n- **The magnetotail is its own entry in the drawer** (Tony, 2026-09-26,\n  option A of two). Option B, part of the Magnetopause row, would have left\n  the tail\'s sources with nowhere to show in the i panel, which shows one\n  row\'s sources, and GO on Magnetopause would have framed out to 220 Earth\n  radii. Tony added: the two views, with the tail and without it, each get\n  their own framing, which is what a separate row gives.\n- **The words a visitor reads were shown to Tony before the build finished,\n  and he said continue.** Two were shortened after that to fit the hover\n  budget; section 4 names both.\n- **The plan, with the orrery patch D13 added to it**, confirmed as\n  recommended.\n\n## 2. What the patch changes\n\n- **`data/objects_config.json`.**\n  - The `magnetotail` entry becomes a served shell: a name, a one-line\n    description, an i-panel paragraph, a note, a source, a link, and\n    pointer entries for the four tail rows (`flare_end`, `diameter`,\n    `drawn_radius`, `drawn_end`) beside the existing `observed_extent`.\n    Its colour and opacity are the magnetopause\'s, so the two read as one\n    surface. `length_radii`, `base_radii`, `end_radii` and the old colour\n    and opacity are gone; the `_declared` sentence is rewritten.\n  - `observed_extent`\'s source keeps only the reach; the 1983 abstract\'s\n    figures for the end of widening and the diameter now sit with the 1985\n    rows.\n  - Earth\'s belts lose `belt_thickness` and `n_rings`; `_declared` says the\n    ring count follows from the edge and peak rows.\n  - The magnetic tilt\'s source sentence is corrected: the paper prints no\n    tilt, the store computes it at five figures, and it shrinks by about\n    0.049 degrees a year, not 0.05 per decade.\n  - Earth\'s `orientation`: the pole\'s two numbers point at\n    `EARTH_POLE_RA_J2000_DEG` and `EARTH_POLE_DEC_J2000_DEG` instead of\n    `idealized_orbits.py`; the source names Horizons for the pole drawn\n    and the IERS for the fallback, and says the IAU report was cited\n    until today; a `rotation_period` pointer entry is added for\n    `EARTH_SIDEREAL_ROTATION_PERIOD_H`.\n  - The 14 `uncertainty` fields the mirror writes (section 3).\n- **`gallery/feature_renderers.js`.**\n  - The magnetotail, in `renderMagnetosphere`, drawn only if the\n    magnetopause was. Its start is worked out from the served Shue rows at\n    the served cut; rings run from there to the drawn end, with a ring\n    added exactly at the flare end so the bend sits where the row puts it.\n    It is stamped with its own shell key, `magnetotail`, so the arrival\n    rule hides it on arrival like every other shell but the crust.\n  - The belts: `evenBeltRings()`, the page\'s copy of the orrery\'s\n    `_even_belt_rings()`, reading decimals to a thousandth as the orrery\'s\n    `limit_denominator(1000)` does, capped at 25 rings. The peak ring is a\n    second trace in the same drawer row, opacity 1.0 and twice the size;\n    the info marker sits on it. A belt with no edges keeps a served\n    thickness (Jupiter) or, with neither, is drawn as one ring with a\n    warning. The 0.5 fallback is gone.\n  - The magnetopause hover\'s sentence about where the drawing stops now\n    says the boundary is drawn on as the magnetotail.\n- **`gallery/earth_geometry.js`.** The axis hover states the period from\n  the served row at its served count. Its panel source credits the sense\n  of rotation to the IAU report\'s general definition (section 2, page 6)\n  and its statement that Earth\'s rotation is direct (section 7, page 27),\n  both read in the report this session, and adds the period\'s source. The\n  module description no longer calls the frame angle the renderer\'s own\n  IAU 2006 obliquity.\n- **`tools/mirror_constants.py`.** `uncertainty` joins `value`, `unit` and\n  `figures`. A null is never inserted, and an export before schema 4,\n  which has no such key, leaves entries as they were.\n- **`tools/test_mirror_constants.py`.** Case 17, the uncertainty field;\n  case 18, Earth\'s pole served; case 9\'s link outside the store is\n  Jupiter\'s pole now.\n- **The three smoke checks.**\n  - `smoke_earth_geometry.js` takes the magnetosphere and the period from\n    the served cache, as it already took the pole of date, because the\n    recorded payload predates them. It checks the tail as a shape (where it\n    starts, where it bends, where it ends, round, the marker on it), the\n    belts\' rings against the orrery\'s answers, and the axis hover\'s period.\n    Its `normal()` helper now picks three points that span a trace: with\n    several rings in one trace, its old choice put three points on one\n    radial line and read as a false 23-degree tilt.\n  - `smoke_hover_budget.js` measures the room with the served\n    magnetosphere, so the tail\'s hover is measured at all.\n  - `smoke_display_figures.js` grades the tail line by line and the axis\n    period against the served row, drops the retired sentences, and holds\n    the rest to a re-recorded fixture,\n    `documentation/fixture_hovers_L322d_p3_on_c6000f03.json`. The D7\n    fixture is left in place, unreferenced.\n\n## 3. How it was verified, in the sandbox\n\n- **The whole gallery maintenance run: 16 of 16 gating checkers passed**,\n  after the served cache\'s feature copies were refreshed from the config\n  the way `derive_served()` copies them (the sandbox cannot reach\n  Horizons; your real cache build replaces this step). The same result on\n  a fresh clone of `c6000f03` with only the patch applied.\n- **The patch reproduces the sandbox byte for byte** on a fresh clone,\n  refuses a second run, and keeps CRLF on a working copy that has it.\n- **Each new check was shown failing.** Tail radius off by one percent:\n  four tail checks fail. Peak ring as faint as the others: both belts\'\n  peak checks fail. The axis sentence reworded: the period check fails.\n  `uncertainty` removed from the mirror\'s fields: two mirror checks fail.\n- **The mirror writes 14 fields and a second run writes none**: eight on\n  Earth\'s radius (`"0.0001"`), the magnetopause\'s three coefficients, its\n  standoff in Earth radii, kilometres and AU.\n- **The exact-row print lines are unchanged.** `EXACT_ROWS_PRINTED.md` at\n  orrery `43ba290b` lists ten gallery lines; after this patch the report\n  still finds all ten with nothing broken. What it found new is section 5.\n- **Hover sizes.** The tail\'s hover is 17 lines, at the ceiling; the outer\n  belt\'s is 17; the axis hover\'s 17.\n- **D5\'s cone cleanup** does not apply: the gallery draws no dipole cone,\n  only the two spin-arrow heads on the axis.\n\n## 4. The visitor-facing text\n\nThe magnetotail\'s hover, under its name:\n\n    Earth\'s magnetic field, drawn out by the solar wind into a long tail on\n    the night side.\n\n    Spacecraft found the tail stops widening about 120 Earth radii behind\n    Earth, plus or minus 10, and is about 60 Earth radii wide beyond there,\n    plus or minus 5.\n    That is about 770,000 km (0.0051 AU) and 380,000 km (0.0026 AU).\n    The straight widening up to that point is our choice; the measurements\n    give only its two ends.\n    The drawing stops at 220 Earth radii, which is how far the spacecraft\n    went, not where the tail ends.\n    Drawn round, its average shape; at any moment it is often flattened.\n\nThe kilometre line was "... 770,000 km (0.0051 AU) behind Earth and\n380,000 km (0.0026 AU) wide." when Tony saw it; "behind Earth" and "wide"\nwere dropped to bring the hover from 18 lines to the 17 allowed. The\nsentence before it gives the order.\n\nIts i-panel paragraph:\n\n    The solar wind drags Earth\'s magnetic field out behind the planet into\n    a long tail. Spacecraft crossing it far downstream found that it stops\n    widening about 120 Earth radii behind Earth and is about 60 Earth radii\n    across beyond there. ISEE-3 followed it out to 220 Earth radii, which\n    is how far the spacecraft went rather than where the tail ends. The\n    tail is drawn round, which is close to its shape on average; at any\n    moment it is often flattened, in a direction set by the solar wind\'s\n    own magnetic field, which keeps changing.\n\nThe belts\' new sentence, both belts:\n\n    The belt is one continuous region; its evenly spaced rings only mark its\n    extent, and the brighter ring marks where it is most intense.\n\nTony saw a three-line version ("The belt is one continuous region. The\nrings only mark its extent: they are evenly spaced from its inner edge to\nits outer edge, and the brighter ring marks where the belt is most\nintense."); it was shortened to two lines because the outer belt\'s hover\nwas 18. The edges it dropped are on the next lines of the same hover\n("Measured extent: 3 to 7 Earth radii"). "Drawn 0.5 radii wide, a width\nchosen for the picture." is gone.\n\nThe magnetopause\'s sentence: "That is where the drawing stops, not where\nthe surface ends: it widens down the tail without limit." became "Beyond\nthat angle the boundary is drawn as the magnetotail."\n\nThe axis hover: "This scene is one epoch: the axis is the line Earth turns\nabout; the turning itself is not shown, and no rotation period is stated\nbecause none is served." became "Earth turns once every 23.93447 hours\nmeasured against the stars. The turning is not animated, because nothing\non the crust marks a longitude to watch it by."\n\n## 5. For the ledger, one row per class\n\n- **Jupiter\'s belt thickness is a typed 0.5 with no source.** Served in\n  `radiation_belts`, drawn by no room, and it has no edge rows to draw\n  across. Waits for the braid; this build kept it rather than draw\n  Jupiter\'s belts some new way unasked. The manifest and the previous\n  handoff said "both `belt_thickness` entries"; this is the second one.\n- **The recorded Earth scene is overlaid piece by piece.** Three checks now\n  take the pole of date, the magnetosphere and the rotation period from\n  the served cache because `documentation/payload_earth_scene.json` (a\n  recording of 2026-09-08/09) predates them. It still carries the 9.6\n  tilt and the old belt thickness. Extends the existing aging-payload row;\n  a recapture would retire the overlays.\n- **The tail\'s hover is at the line ceiling (17).** Anything added to it\n  needs a line taken away.\n- **There is no Wikipedia article for the magnetotail;** the link is the\n  Magnetosphere article.\n\nCarried, now done by this patch: L-311\'s gallery half; the axis period and\nre-homed sources; the orientation source; the tilt sentence; the test at\nline 373 (now case 9 and case 18); the mirror\'s docstring (three\n`planet_poles` links).\n\n## 6. Tony\'s run\n\n(Append the patch output, the cache builder\'s last swap-log line, the\ngallery maintenance run\'s summary, the live run, and what the phone\nshowed: the tail with and without framing, both belts, the axis hover, and\nthe Sun room.)\n\n---\n\nSession written September 2026 with Anthropic\'s Claude Opus 5.5.\n',
}


def fail(msg):
    print("FAILURE: %s" % msg)
    print("NOTHING was written.")
    sys.exit(1)


def main():
    planned = []
    for rel, fp, edits in TARGETS:
        path = os.path.join(HERE, *rel.split('/'))
        if not os.path.exists(path):
            fail("%s not found -- is this script in the orrery repo root?" % rel)
        raw = open(path, 'rb').read()
        crlf = b'\r\n' in raw
        lf = raw.replace(b'\r\n', b'\n')
        got = hashlib.md5(lf).hexdigest()
        if got != fp:
            fail("%s is not the file this patch was built on (fingerprint %s, "
                 "expected %s). Has it changed since orrery 43ba290b?"
                 % (rel, got, fp))
        spans = []
        for old, new in edits:
            n = lf.count(old)
            if n != 1:
                fail("ANCHOR FAIL in %s: expected 1 match, found %d: %r"
                     % (rel, n, old[:60]))
            spans.append((lf.index(old), len(old), old, new))
        spans.sort()
        for a, b in zip(spans, spans[1:]):
            if a[0] + a[1] > b[0]:
                fail("two edits overlap in %s" % rel)
        out = lf
        for i, ln, old, new in reversed(spans):
            out = out[:i] + new + out[i + ln:]
        try:
            out.decode('ascii')
        except UnicodeDecodeError:
            fail("%s would not be ASCII after the patch" % rel)
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        planned.append((rel, path, out, len(edits), crlf))
    for rel in NEW_FILES:
        if os.path.exists(os.path.join(HERE, *rel.split('/'))):
            fail("%s already exists -- this patch may have run already" % rel)
    for rel, path, out, n, crlf in planned:
        with open(path, 'wb') as handle:
            handle.write(out)
        print("  ok  %s: %d edit(s)%s" % (rel, n, " [CRLF kept]" if crlf else ""))
    for rel, text in NEW_FILES.items():
        with open(os.path.join(HERE, *rel.split('/')), 'wb') as handle:
            handle.write(text)
        print("  ok  %s: new file (%d bytes)" % (rel, len(text)))
    print("  ok  stamps: the module history line added to exact_rows_report.py")
    print("")
    print("PATCH APPLIED")
    print("")
    print("NEXT STEPS")
    print("  1. Run orrery_maintenance_run.py with the Run button. Its 'Exact")
    print("     rows report' line should say '4 drawn only, 0 not followed,")
    print("     0 map entries broken'. If it says 4 not followed, gallery")
    print("     patch 3 has not run in the gallery folder beside the orrery.")
    print("  2. Move this script into documentation/. Commit the orrery,")
    print("     with the rewritten EXACT_ROWS_PRINTED.md, and push.")
    print("  3. Append your run to the two new run records in documentation/.")

if __name__ == '__main__':
    main()
