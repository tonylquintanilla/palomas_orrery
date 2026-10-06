#!/usr/bin/env python3
"""
patch_L420_3_session_close_20261006.py -- ORRERY repo. L-420's session record: the
ledger's L-420 block and header stamp, a line in the website session's
handoff, and this session's handoff,
documentation/HANDOFF_L420_galactic_plane_20261006.md.

Built on orrery 51436054330aefd6be2a7efd93ebd58f06c4a2d2
at https://github.com/tonylquintanilla/palomas_orrery
(gallery not touched).

Run it after patch_L420_2_galactic_plane_and_centre_20261006.py.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L420_3_session_close_20261006.py

YOUR NOTES ARE SAFE. The ledger and the handoff are checked only at the
lines this patch changes, never as whole files (L-419), so notes you
have written anywhere else in them do not stop it. Where We Are is NOT
touched: the website session owns it this round.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 6, 2026 with Anthropic's Claude Opus 5.5.
"""

import os

REPO = "orrery"
ROOT_MARKERS = ["palomas_orrery.py", "constants_new.py", "LEDGER_CONSOLIDATED.md"]

HANDOFF_PATH = 'documentation/HANDOFF_L420_galactic_plane_20261006.md'

HANDOFF = '<!-- Doc-Kind: hand | Session record for L-420, the galactic plane and the galactic centre in the orrery. -->\n# Handoff: L-420, the galactic plane and the galactic centre\n\nBuilt on orrery 51436054330aefd6be2a7efd93ebd58f06c4a2d2\nat https://github.com/tonylquintanilla/palomas_orrery\n(gallery ed48d078ceb639f5f98f13f4c6abc129f722c566\nat https://github.com/tonylquintanilla/tonyquintanilla.github.io;\nnot touched). Pushed at: (Tony writes the SHA here.)\n\n- Type: BUILD.\n- Supersedes: nothing. Runs beside the two sessions of 2026-10-05,\n  Earth\'s website patch and the Horizons design round, and touches\n  neither\'s files.\n- Patches, in order: `patch_L420_2_galactic_plane_and_centre_20261006.py`\n  (the code), `patch_L420_3_session_close_20261006.py` (this record, the\n  ledger, a line in the website session\'s handoff).\n\n## What was asked\n\n- Tony, 2026-10-06: "Build L-420". The design was ruled on 2026-10-05:\n  the galactic plane and its poles in the Celestial Grid, the galactic\n  centre in the Star Background.\n- Tony confirmed the plan and the words: "Yes, confirmed as\n  recommended".\n\n## What was done\n\n- The galactic centre\'s row was sourced first.\n  - Source: Liu, Zhu and Hu, arXiv:1110.6268, sec. 3.2, eq. (8), read\n    as the ar5iv HTML rendering on 2026-10-06 by Claude Opus 5.5. It\n    prints Sgr A*\'s position from Reid and Brunthaler (2004), measured\n    with the Very Long Baseline Array: 17h 45m 40.0400s,\n    -29 deg 00\' 28.138".\n  - It is the same paper the galactic pole rows already cite.\n  - New rows in `constants_new.py`: `SGR_A_STAR_RA_ICRS_ARCSEC`,\n    `SGR_A_STAR_DEC_ICRS_ARCSEC` (exact as printed), and the derived\n    `SGR_A_STAR_RA_ICRS_DEG`, `SGR_A_STAR_DEC_ICRS_DEG`.\n- A check on the existing pole row came free.\n  - The paper\'s eq. (7) gives the point the frame defines as galactic\n    longitude zero.\n  - It lies on the plane drawn from the store\'s pole to a\n    hundred-millionth of a degree.\n  - Sgr A* sits 0.05 degrees from the plane. Nothing drawn can show it.\n- `star_sphere_builder.py`\n  - `build_galactic_grid()` computes the galactic plane and both poles\n    from the store\'s rows when the plot is drawn. The saved star file,\n    `star_data/star_sphere_vmag35.json`, is not rebuilt.\n  - Celestial Grid: a violet circle, and violet crosses labelled NGP and\n    SGP, drawn the way NCP/SCP and NEP/SEP are.\n  - Star Background: a violet dot labelled "Sgr A*", always hoverable.\n  - Fixed in passing: with Labels on, the celestial and ecliptic pole\n    hovers showed the short label ("NCP") where the full name was meant.\n    The hover pointed at the label field instead of the name field.\n- `palomas_orrery.py`\n  - Both "Ecliptic Coordinates (J2000)" boxes, the static plot\'s and\n    the animation\'s, gain the violet-circle line.\n  - The Celestial Sphere, Star Background, Celestial Grid and Labels\n    tooltips name the plane, its poles and Sgr A*.\n\n## The words, as approved\n\n- Sgr A* hover:\n      Sagittarius A*\n      The black hole at the centre of our galaxy\n      Its direction from the Sun, among the stars\n- Galactic pole hovers, with Labels on:\n      North Galactic Pole (NGP)\n      Perpendicular to the disk of our galaxy\n  and the same for the South Galactic Pole (SGP).\n- Box line:\n      Violet circle: Galactic plane, the disk of the Milky Way\n      (NGP, SGP its poles)\n- No number is printed, so the tilt of the plane (about 60 degrees to\n  the ecliptic) needed no derived row.\n\n## Verified, and how\n\n- Both patches ran on a copy of 51436054 and a second run refused.\n  patch_L420_2 also ran on a CRLF copy and wrote the same bytes.\n- py_compile on the three code files; the GUI started headless.\n- The live call path: the GUI\'s `add_celestial_sphere_traces` is the\n  edited function. It was called with each switch on and off:\n  - Labels off: the new markers show their labels and no hover, as the\n    other poles do. Labels on: the full names.\n  - Star Background off: no Sgr A*. Celestial Grid off: no plane.\n- The maintenance run, against the same run at 51436054:\n  - Every checker gives the same verdict. Constants export rows go from\n    101 to 105; derived rows read go from 34 to 36.\n  - The scanner\'s Tier-1 findings are the same 296, compared file by\n    file, not by the total. A first build added one, a docstring saying\n    "90 degrees"; it was reworded before delivery.\n  - The two new measured rows score 15, cited and not yet cross-checked,\n    the same as the galactic pole rows.\n  - Reset completeness fails in the sandbox at 51436054 too: it needs\n    a Tk colour only Windows has. Not this patch.\n- NOT verified: how it looks. That is Tony\'s look.\n\n## Running beside the other sessions\n\n- Where We Are was not rewritten: the website session owns it this\n  round. The lines below are for the next rewrite, and patch_L420_3 adds\n  a pointer to them in the website session\'s handoff.\n- In the ledger this session edited only L-420 and the header stamp.\n  Its edits match only the lines they change, so the sessions\' patches\n  apply in either order.\n\n## For the next Where We Are\n\n- Changed: the orrery\'s Celestial Grid draws the galactic plane, a\n  violet circle, with its poles NGP and SGP; the Star Background marks\n  Sagittarius A*, the direction of the galaxy\'s centre.\n- Changed: the pole hovers show their full names with Labels on.\n- Needs Tony: a look at the violet circle, the Sgr A* dot and the new\n  line in the coordinate box.\n- Road: not a stage of its own; an orrery item done between stages.\n- Details: L-420.\n\n## Tony-actions\n\n(do)\n1. Run `patch_L420_2_galactic_plane_and_centre_20261006.py` in the\n   orrery root.\n2. Run `patch_L420_3_session_close_20261006.py` the same way.\n3. Run `orrery_maintenance_run.py`. Its Constants export step rewrites\n   `data/constants_export.json` with the four new rows.\n4. Move both patch scripts into `documentation/`, commit and push.\n5. Plot with Star Background, Celestial Grid and Labels on, and look:\n   the violet colour, the marker sizes, where the labels sit.\n\n## Next session\n\n- Close L-420 on Tony\'s look, or adjust what he names.\n- Nothing else is opened by this session.\n\nSession written October 2026 with Anthropic\'s Claude Opus 5.5.\n'

EDITS = {'LEDGER_CONSOLIDATED.md': [('header stamp',
                             'centre in the star background, as Tony ruled), '
                             'built on 0493fad0.\n',
                             'centre in the star background, as Tony ruled), '
                             'built on 0493fad0.\n'
                             'Module updated: October 6, 2026 with '
                             "Anthropic's Claude Opus 5.5\n"
                             '(L-420 built: the galactic plane, its poles '
                             'and Sgr A* in the orrery;\n'
                             "Sgr A*'s position sourced), built on "
                             '51436054.\n'),
                            ('L-420 date',
                             '<!-- L:420 status:OPEN upd:2026-10-05 '
                             'section:A flag: rice: -->\n',
                             '<!-- L:420 status:OPEN upd:2026-10-06 '
                             'section:A flag: rice: -->\n'),
                            ('L-420 built, Gap and Ref',
                             "**Gap:** a build session after Earth's website "
                             'patch and the Horizons\n'
                             "round: source the galactic centre's row, build "
                             "both, Tony's look (Mode 5).\n"
                             '**Ref:** `star_sphere_builder.py`; '
                             '`constants_new.py` (the galactic pole\n'
                             'rows); '
                             '`solar_visualization_shells.create_sun_galactic_tide`; '
                             'L-406.\n',
                             '- **Built 2026-10-06** at orrery 51436054, in '
                             'a session of its own,\n'
                             '  after Tony confirmed the plan and the words '
                             '("Yes, confirmed as\n'
                             '  recommended"): '
                             '`patch_L420_2_galactic_plane_and_centre_20261006.py`.\n'
                             "  - The galactic centre's row, sourced: Sgr "
                             "A*'s position from Liu,\n"
                             '    Zhu and Hu, arXiv:1110.6268, eq. (8), the '
                             'VLBA position of Reid and\n'
                             '    Brunthaler (2004), read 2026-10-06 by '
                             'Claude Opus 5.5.\n'
                             '    `SGR_A_STAR_RA_ICRS_ARCSEC` and '
                             '`SGR_A_STAR_DEC_ICRS_ARCSEC` hold it\n'
                             '    in arcseconds, exact as printed; their '
                             'degree rows are derived.\n'
                             "  - A check on the pole row: the same paper's "
                             'eq. (7), the point the\n'
                             '    frame defines as galactic longitude zero, '
                             'lies on the plane drawn\n'
                             "    from the store's pole to a "
                             'hundred-millionth of a degree. Sgr A*\n'
                             '    sits 0.05 degrees from that plane, far '
                             'below what the drawing shows.\n'
                             '  - The plane, NGP and SGP are computed when '
                             'the plot is drawn\n'
                             '    '
                             '(`star_sphere_builder.build_galactic_grid`), '
                             'so the saved star file\n'
                             '    is not rebuilt.\n'
                             '  - Words shown to Tony and approved: the Sgr '
                             'A* hover ("Sagittarius\n'
                             '    A*" / "The black hole at the centre of our '
                             'galaxy" / "Its\n'
                             '    direction from the Sun, among the stars"); '
                             'the galactic pole\n'
                             '    hovers ("North Galactic Pole (NGP)" / '
                             '"Perpendicular to the disk\n'
                             '    of our galaxy"); the box line ("Violet '
                             'circle: Galactic plane, the\n'
                             '    disk of the Milky Way (NGP, SGP its '
                             'poles)"). The four tooltips\n'
                             '    name the plane, its poles and Sgr A*.\n'
                             '  - Fixed in passing and reported: with Labels '
                             'on, the celestial and\n'
                             '    ecliptic pole hovers showed "NCP" where '
                             'the full name was meant.\n'
                             '  - No angle is printed, so the tilts (about '
                             '60 degrees to the\n'
                             '    ecliptic) needed no derived row.\n'
                             '  - Checked in the sandbox: the maintenance '
                             'run gives the same verdicts\n'
                             "    as at 51436054, and the scanner's Tier-1 "
                             'findings are the same 296,\n'
                             '    file by file. The two new measured rows '
                             'score 15, cited and not yet\n'
                             '    cross-checked, as the pole rows do. Reset '
                             'completeness fails in the\n'
                             '    sandbox at 51436054 too: a Tk colour only '
                             'Windows has.\n'
                             '  - Where We Are was left alone: the website '
                             'session owns it this\n'
                             '    round. Its lines are in\n'
                             '    '
                             '`documentation/HANDOFF_L420_galactic_plane_20261006.md`.\n'
                             '**Gap:** Tony runs patch_L420_2, patch_L420_3 '
                             'and the maintenance run,\n'
                             'pushes, and looks (Mode 5): the violet colour, '
                             'the marker sizes, where\n'
                             'the labels sit. Then close.\n'
                             '**Ref:** `star_sphere_builder.py` '
                             '(`build_galactic_grid`);\n'
                             '`constants_new.py` (the galactic pole and Sgr '
                             'A* rows);\n'
                             '`palomas_orrery.py` (the two coordinate boxes, '
                             'the four tooltips);\n'
                             '`solar_visualization_shells.create_sun_galactic_tide`; '
                             'L-406;\n'
                             '`documentation/HANDOFF_L420_galactic_plane_20261006.md`.\n')],
 'documentation/HANDOFF_L413_earth_orrery_patch_20261005.md': [('L-420 '
                                                                'built: '
                                                                'where its '
                                                                'page lines '
                                                                'are',
                                                                '  and the '
                                                                'galactic '
                                                                'centre in '
                                                                'the star '
                                                                'background, '
                                                                'for a build '
                                                                'session\n'
                                                                '  after '
                                                                'this one '
                                                                'and the '
                                                                'Horizons '
                                                                'round.\n',
                                                                '  and the '
                                                                'galactic '
                                                                'centre in '
                                                                'the star '
                                                                'background, '
                                                                'for a build '
                                                                'session\n'
                                                                '  after '
                                                                'this one '
                                                                'and the '
                                                                'Horizons '
                                                                'round.\n'
                                                                '  It was '
                                                                'built on '
                                                                '2026-10-06 '
                                                                'in a '
                                                                'session of '
                                                                'its own, '
                                                                'which left\n'
                                                                '  Where We '
                                                                'Are alone; '
                                                                'take its '
                                                                'lines for '
                                                                'the page '
                                                                'from\n'
                                                                '  '
                                                                '`documentation/HANDOFF_L420_galactic_plane_20261006.md`, '
                                                                'under\n'
                                                                '  "For the '
                                                                'next Where '
                                                                'We '
                                                                'Are".\n')]}


NEXT = [
    "1. Run orrery_maintenance_run.py. Its Ledger index step updates",
    "   L-420's row; its Constants export step writes the four new rows.",
    "2. Move both L420 patch scripts into documentation/, commit and push.",
    "3. Your look: plot with Star Background, Celestial Grid and Labels on.",
    "   The violet colour, the marker sizes, where the labels sit.",
]


def read_lf(path):
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), b"\r\n" in raw


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    if os.path.exists(HANDOFF_PATH):
        raise SystemExit("ERROR: %s already exists. If this patch already "
                         "ran, it has nothing left to do. NOTHING was "
                         "written." % HANDOFF_PATH)
    consts, _ = read_lf("constants_new.py")
    if "SGR_A_STAR_RA_ICRS_ARCSEC" not in consts:
        raise SystemExit("ERROR: constants_new.py has no Sgr A* rows, so "
                         "patch_L420_2 has not run. Run it first. NOTHING "
                         "was written.")
    writes = []
    for path in sorted(EDITS):
        text, was_crlf = read_lf(path)
        done = []
        for label, old, new in EDITS[path]:
            found = text.count(old)
            if found != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, found))
            text = text.replace(old, new)
            done.append(label)
        writes.append((path, text, done, was_crlf))
    writes.append((HANDOFF_PATH, HANDOFF, ["created"], False))
    for path, text, done, was_crlf in writes:
        new_lines = [n for (l, o, n) in EDITS.get(path, [])] or [text]
        if any(ord(ch) > 127 for chunk in new_lines for ch in chunk):
            raise SystemExit("ERROR: the text for %s holds non-ASCII. "
                             "NOTHING was written." % path)
    for path, text, done, was_crlf in writes:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-58s %s" % (path, label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    print("")
    print("stamps updated: the ledger's header stamp; the new handoff opens "
          "with its anchor")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
