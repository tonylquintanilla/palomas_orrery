#!/usr/bin/env python3
"""
patch_L420_1_galactic_plane_item_20261005.py -- ORRERY repo. Records
Tony's design for the galactic plane in the Celestial Grid and the
galactic centre in the star background as L-420. No code changes.

Built on orrery 0493fad007456fe68a7690a2400af2c2d185a410 at
https://github.com/tonylquintanilla/palomas_orrery (gallery
ed48d078ceb639f5f98f13f4c6abc129f722c566 not read or changed).

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT, open it in VS Code and click
    Run. Then follow the NEXT steps.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md   L-420 opened, and the header stamp.
    documentation/HANDOFF_L413_earth_orrery_patch_20261005.md   one line
        asking the website session to put L-420 on Where We Are, which
        that session owns this round.
    Both matched only at the lines changed (L-419).

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ANCHOR FAIL: line, and NOTHING is written.

Written October 5, 2026 with Anthropic's Claude Opus 5.5.
"""

import os

ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
NEXT = ["1. Move this script into documentation/.",
        "2. Run orrery_maintenance_run.py: its Ledger index step adds",
        "   L-420 to the index.",
        "3. Commit and push. Run it before the website session's patch if",
        "   you can; either order works."]

EDITS = {
  'LEDGER_CONSOLIDATED.md': [
    ('header stamp',
      "1.16, protocol v3.82), built on patch_L413_4's tree over d9f47a87.\n",
      ("1.16, protocol v3.82), built on patch_L413_4's tree over d9f47a87.\n"
      "Module updated: October 5, 2026 with Anthropic's Claude Opus 5.5\n"
      '(L-420 opened: the galactic plane in the Celestial Grid, the galactic\n'
      'centre in the star background, as Tony ruled), built on 0493fad0.\n'),
      1),
    ('L-420 opened',
      '#### [L-419] A patch checks a file Tony annotates only at the lines it edits (patches, skills)\n',
      ('#### [L-420] The galactic plane in the Celestial Grid, the galactic centre in the star background (orrery, sky)\n'
      '<!-- L:420 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n'
      '- **Tony, 2026-10-05:** "in the celestial grid, could we add the galactic\n'
      '  plane? this is relevant to the galactic tide in particular." Then, on\n'
      '  where the galactic centre goes: "we could put the plane and poles in\n'
      '  the Celestial Grid and the galactic centre in the star background."\n'
      '- **The design, as ruled:**\n'
      '  - Celestial Grid (`star_sphere_builder.py`): a third great circle, the\n'
      '    galactic plane, in its own colour beside the amber ecliptic and the\n'
      '    teal celestial equator; the north and south galactic poles marked\n'
      '    and labelled NGP and SGP, as the grid marks NCP/SCP and NEP/SEP; a\n'
      '    line in the "Ecliptic Coordinates (J2000)" box naming the circle.\n'
      '  - Star Background: the direction of the galactic centre, Sagittarius\n'
      '    A*, as a sky object among the stars, not a grid line.\n'
      '- **What the store already holds:** the north galactic pole,\n'
      '  `GALACTIC_NORTH_POLE_RA_J2000_DEG` and `GALACTIC_NORTH_POLE_DEC_J2000_DEG`,\n'
      '  sourced to Liu, Zhu and Hu, arXiv:1110.6268, eq. (2), added for the\n'
      '  galactic tide (L-406). The plane is the great circle 90 degrees from\n'
      '  it, so the plane and both poles need no new number. Worked from those\n'
      '  rows on 2026-10-05: the plane is tilted about 60 degrees to the\n'
      '  ecliptic and about 63 to the celestial equator; any hover that prints\n'
      '  either needs a derived row first.\n'
      "- **What it does not hold:** the galactic centre's position.\n"
      "  `sgr_a_star_data.py` carries the S-star orbits, not Sgr A*'s place on\n"
      '  the sky. The build sources a row first (a published position of Sgr\n'
      "  A*, or the frame's own definition of galactic longitude zero from the\n"
      '  same family of sources as the pole), never a recalled number.\n'
      '- **Scope:** the orrery only; the website has no celestial grid yet. It\n'
      '  touches neither of the two sessions running on 2026-10-05.\n'
      "**Gap:** a build session after Earth's website patch and the Horizons\n"
      "round: source the galactic centre's row, build both, Tony's look (Mode 5).\n"
      '**Ref:** `star_sphere_builder.py`; `constants_new.py` (the galactic pole\n'
      'rows); `solar_visualization_shells.create_sun_galactic_tide`; L-406.\n'
      '\n'
      '#### [L-419] A patch checks a file Tony annotates only at the lines it edits (patches, skills)\n'),
      1),
  ],
  'documentation/HANDOFF_L413_earth_orrery_patch_20261005.md': [
    ('L-420 for Where We Are',
      ('- One cost Tony carries: two threads to bring results between. A\n'
      '  session that finds itself asking Tony for more than one thing at a\n'
      '  time waits for the other to finish.\n'),
      ('- One cost Tony carries: two threads to bring results between. A\n'
      '  session that finds itself asking Tony for more than one thing at a\n'
      '  time waits for the other to finish.\n'
      '- When this session rewrites Where We Are, it adds L-420, opened after\n'
      '  this record: the galactic plane and its poles in the Celestial Grid,\n'
      '  and the galactic centre in the star background, for a build session\n'
      '  after this one and the Horizons round.\n'),
      1),
  ],
}

ALREADY = {'LEDGER_CONSOLIDATED.md': '#### [L-420]', 'documentation/HANDOFF_L413_earth_orrery_patch_20261005.md': 'it adds L-420, opened after'}


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the "
                             "orrery root. NOTHING was written." % marker)
    for path, marker in ALREADY.items():
        with open(path, "rb") as handle:
            if marker.encode("utf-8") in handle.read():
                raise SystemExit("ERROR: %s already holds %r, so this patch "
                                 "has already run. NOTHING was written."
                                 % (path, marker))
    results = []
    for path in sorted(EDITS):
        with open(path, "rb") as handle:
            raw = handle.read()
        text = raw.decode("utf-8").replace("\r\n", "\n")
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d. Has this patch already run? "
                                 "NOTHING was written."
                                 % (label, want, path, found))
            text = text.replace(old, new)
            results.append((path, label))
        EDITS[path] = text
    for path in sorted(EDITS):
        with open(path, "wb") as handle:
            handle.write(EDITS[path].encode("utf-8"))
    for path, label in results:
        print("ok  %-60s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
