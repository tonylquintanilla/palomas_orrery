#!/usr/bin/env python3
"""
patch_L371_2_roche_drawn_orrery_20261003.py -- ORRERY repo. The second
patch for L-371's distance cards: the row that says where the Roche limit
is drawn.

Built on orrery a841ab6ee36fbbcef936408bc87774bc32a7598d
at https://github.com/tonylquintanilla/palomas_orrery
(gallery d4b408e60b1d9a45252174ca4a2c861ca17b49a5 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; not touched
here -- patch_L371_3 is the gallery's half and runs after this push).

WHY. The Roche limit is known to one figure, about 3 solar radii, which is
also where the inner corona is drawn. The website draws each shell at the
number it is served, so it would draw the two on top of each other. Tony's
ruling of 2026-10-03, option B: draw it at the formula's full answer,
3.45, on both sites, as a stated drawing choice, and say "about 3" in the
words. An interim until edges known only as ranges are drawn as fuzzy
bands, a design item of its own.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L371_2_roche_drawn_orrery_20261003.py
    Then run orrery_maintenance_run.py the same way.

WHAT THE MAINTENANCE RUN SHOULD SAY
    Every gating checker passes, Constants change included: this time the
    only change is one formula row, which it reads. Constants relations
    reads "25 of 25". The provenance scanner should report no file whose
    serious findings rose, except perhaps this script while it is in the
    root folder.
    Then move this script into documentation/, commit and push.

WHAT CHANGES
    constants_new.py   ROCHE_LIMIT_DRAWN_RADII = ROCHE_LIMIT_RADII: where
                       the shell is drawn, declared, exact, printing 3.45.
                       The export serves it unrounded, so the website can
                       draw at 3.45 while its card says 3.
    shell_configs.py   the orrery's Roche shell draws from that row. Same
                       radius as before.
    test_constants_provenance.py   a relation test: the drawn row equals
                       the Roche row at full digits and stays outside the
                       inner corona.

PERMANENT, though this script is thrown away: the row, the shell's
pointer to it, the test.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 3, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py",)
BUILT_ON = "a841ab6e"
NEXT = ["1. Run orrery_maintenance_run.py (VS Code, Run). Every gating",
        "   checker should pass.",
        "2. Move this script into documentation/; commit and push.",
        "3. Then the gallery patch, patch_L371_3."]

BASE = {'constants_new.py': '9ebd85477298e0c473190cfd3506b93d',
 'shell_configs.py': '1bee2c13bcd6c7c009cc0c88c5e68656',
 'test_constants_provenance.py': '2432927fa6783d2f14b9f11a740332c3'}

EDITS = {'constants_new.py': [('ROCHE_LIMIT_RADII: its note points at the drawn row',
                       '# Note+: sourcing the comet density is recorded on L-371. Drawn at the\n'
                       '# Note+: full 3.45, printed at one figure.\n',
                       '# Note+: sourcing the comet density is recorded on L-371. Printed at one\n'
                       '# Note+: figure; drawn through ROCHE_LIMIT_DRAWN_RADII below, at its full\n'
                       '# Note+: digits.\n',
                       1),
                      ("ROCHE_LIMIT_DRAWN_RADII: where the shell is drawn, Tony's option B",
                       '# Note+: inside it. Ikeya-Seki survived at 1.66 R_sun.\n'
                       '\n'
                       'ALFVEN_SURFACE_RADII = 19.7\n',
                       '# Note+: inside it. Ikeya-Seki survived at 1.66 R_sun.\n'
                       '\n'
                       'ROCHE_LIMIT_DRAWN_RADII = ROCHE_LIMIT_RADII\n'
                       '# Derived: where the Roche limit is drawn, its row at full digits = 3.45\n'
                       '# Unit: r_sun\n'
                       '# Status: declared 2026-10-03 -- where the shell is drawn, L-371\n'
                       '# Figures: exact -- prints 3, the digits of the value its rule gives\n'
                       '# Figures+: (3.45); declared construction: equal to ROCHE_LIMIT_RADII at\n'
                       '# Figures+: its full digits\n'
                       '# Declared: the Roche limit is known to one figure, about 3 solar radii,\n'
                       '# Declared+: the same as the line the inner corona is drawn at, so drawn\n'
                       '# Declared+: at that value the two shells would sit on top of each other.\n'
                       "# Declared+: It is drawn at the formula's full answer instead, so the two\n"
                       '# Declared+: stay apart and the orrery and the gallery draw the same '
                       'place.\n'
                       "# Declared+: Which is really further out is not known. Tony's ruling of\n"
                       '# Declared+: 2026-10-03, option B: an interim, until edges known only as\n'
                       '# Declared+: ranges are drawn as fuzzy bands (a design item of its own).\n'
                       '\n'
                       'ALFVEN_SURFACE_RADII = 19.7\n',
                       1)],
 'shell_configs.py': [('docstring: credit line',
                       "Module updated: September 7, 2026 with Anthropic's Claude Fable 5.1 "
                       '(L-295:\n',
                       "Module updated: October 3, 2026 with Anthropic's Claude Opus 5.5 (L-371:\n"
                       '    the Roche limit shell draws from ROCHE_LIMIT_DRAWN_RADII, the row\n'
                       '    that says where it is drawn, rather than from the one-figure row it\n'
                       '    equals. Same radius; the drawing choice now has its own home.)\n'
                       "Module updated: September 7, 2026 with Anthropic's Claude Fable 5.1 "
                       '(L-295:\n',
                       1),
                      ('import the drawn row',
                       'from constants_new import (\n'
                       '    EARTH_INNER_CORE_RADII, EARTH_OUTER_CORE_RADII,\n',
                       '# L-371: the Roche limit draws from the row that says where it is drawn.\n'
                       'from constants_new import ROCHE_LIMIT_DRAWN_RADII\n'
                       'from constants_new import (\n'
                       '    EARTH_INNER_CORE_RADII, EARTH_OUTER_CORE_RADII,\n',
                       1),
                      ('the Roche shell draws from the drawn row',
                       "            'radius_au': ROCHE_LIMIT_RADII * SOLAR_RADIUS_AU,\n",
                       "            'radius_au': ROCHE_LIMIT_DRAWN_RADII * SOLAR_RADIUS_AU,\n",
                       1)],
 'test_constants_provenance.py': [('import the drawn row',
                                   '    HELMET_CUSP_HIGH_RADII,\n    HELIOPAUSE_AU,\n',
                                   '    HELMET_CUSP_HIGH_RADII,\n'
                                   '    ROCHE_LIMIT_DRAWN_RADII,\n'
                                   '    HELIOPAUSE_AU,\n',
                                   1),
                                  ('the Roche limit is drawn at its own full digits',
                                   'def test_unsourced_gravitational_range_stays_gone():\n',
                                   'def test_roche_limit_drawn_at_its_full_digits():\n'
                                   '    """L-371, Tony\'s option B (2026-10-03): the drawn row '
                                   'equals the\n'
                                   '    one-figure row at full digits, and stays outside the inner '
                                   "corona's\n"
                                   '    drawn line, which is why it exists."""\n'
                                   '    assert ROCHE_LIMIT_DRAWN_RADII == ROCHE_LIMIT_RADII, \\\n'
                                   '        "the Roche limit is not drawn at its own row\'s full '
                                   'digits"\n'
                                   '    assert ROCHE_LIMIT_DRAWN_RADII > INNER_CORONA_RADII, \\\n'
                                   '        "the drawn Roche limit sits on or inside the inner '
                                   'corona"\n'
                                   '\n'
                                   '\n'
                                   'def test_unsourced_gravitational_range_stays_gone():\n',
                                   1),
                                  ('docstring: credit line',
                                   'than typed twice, and the unsourced range row stays gone. '
                                   'Still no\n'
                                   'pinned values.)\n',
                                   'than typed twice, and the unsourced range row stays gone. '
                                   'Still no\n'
                                   'pinned values. A fourth the same day: the Roche limit is drawn '
                                   'at its\n'
                                   'own full digits, outside the inner corona.)\n',
                                   1)]}

NEW_FILES = {}


def fingerprint(raw):
    return hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    for path in NEW_FILES:
        if os.path.exists(path):
            raise SystemExit("ERROR: %s already exists. If this patch already "
                             "ran, it has nothing left to do. NOTHING was "
                             "written." % path)
    results = []
    for path in sorted(EDITS):
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. It has changed since\n"
                "       %s, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got, BUILT_ON))
        nl = "\r\n" if b"\r\n" in raw else "\n"
        text = raw.decode("utf-8").replace("\r\n", "\n")
        done = []
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d. NOTHING was written."
                                 % (label, want, path, found))
            text = text.replace(old, new)
            done.append(label)
        results.append((path, text.replace("\n", nl), done))
    for path, text, done in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-36s %s" % (path, label))
    for path in sorted(NEW_FILES):
        with open(path, "wb") as handle:
            handle.write(NEW_FILES[path].encode("utf-8"))
        print("ok  %-36s created" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
