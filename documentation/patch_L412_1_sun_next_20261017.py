#!/usr/bin/env python3
"""
patch_L412_1_sun_next_20261017.py -- records Tony's ruling of October 17,
2026 (late): Earth's remaining design talks wait; the Sun's slice goes
next, its numbers first, then the drawings he picks; then the objects.
Ledger only, and Where We Are. No code.

Built on orrery 88fedb3fce3b25910d7f5e5ff32a24789a268918 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
da442bf21c7d90bffc775e8f5e58d751265a1aa2 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 17, 2026 with Anthropic's Claude Fable 5.1.

RUN COMMAND

    python patch_L412_1_sun_next_20261017.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing; each file is edited only at the lines it
changes, so your notes elsewhere are kept:

    LEDGER_CONSOLIDATED.md          the header stamp; L-412, L-413,
                                    L-443, L-410, L-385, L-128, L-454,
                                    L-356
    documentation/WHERE_WE_ARE.md   above the run-record marker only

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = '88fedb3f'
ZONES = {}
MARKERS = {'documentation/WHERE_WE_ARE.md': '--- Your run record below this line'}
FINGERPRINTS = {}
RESULTS = {}
DELETES = {}
NEW_FILES = {}

TONY_1 = ('"i am thinking that maybe we should leave this aside for now and '
          'work on the sun slice. these ideas are recorded in the handoff. '
          'i would like to finish the sun slice and then work on adding the '
          'symbols to the interactive."')
TONY_2 = ('"yes the numbers and we then decide which of the drawings we do '
          'as well. i would be inclined to do the fades, the dust cloud, the '
          'opening view and maybe wait on the ice lines."')

EDITS = [
    # ---- the ledger's header stamp ----
    ('LEDGER_CONSOLIDATED.md', 'header stamp',
     "(Earth's fade done on Tony's runs and looks: L-410 and L-413), built on\n"
     "adcc1851 and gallery da442bf2.\n",
     "(Earth's fade done on Tony's runs and looks: L-410 and L-413), built on\n"
     "adcc1851 and gallery da442bf2.\n"
     "Module updated: October 17, 2026 with Anthropic's Claude Fable 5.1\n"
     "(the order after Earth's fade, Tony's ruling: Earth's talks 2 to 6\n"
     "wait, the Sun's slice next, its numbers first, then the drawings he\n"
     "picks, then the objects: L-412, L-413, L-443, L-410, L-385, L-128;\n"
     "notes on L-454 and L-356), built on 88fedb3f and gallery da442bf2.\n"),

    # ---- L-412, the Sun's list ----
    ('LEDGER_CONSOLIDATED.md', 'L-412 meta',
     "<!-- L:412 status:OPEN upd:2026-10-11 section:A flag: rice: -->",
     "<!-- L:412 status:OPEN upd:2026-10-17 section:A flag: rice: -->"),
    ('LEDGER_CONSOLIDATED.md', 'L-412 ruled: numbers first',
     "**Gap:** after L-413, work down the list from item 3.\n",
     "- **2026-10-17, Tony's ruling** in the coordination session, after\n"
     "  Earth's round 1 and Earth's fade closed: Earth's remaining design\n"
     "  talks (L-413, talks 2 to 6) wait, and this list goes next. His\n"
     "  words: " + TONY_1 + "\n"
     "  Asked whether \"finish the Sun\" means the whole list or its numbers\n"
     "  first: " + TONY_2 + "\n"
     "  So the list is worked in two halves, and the second is chosen when\n"
     "  the first is done:\n"
     "  - THE NUMBERS FIRST (road stage 7, the Sun's numbers getting the\n"
     "    checking Earth's got): item 4 (L-228, the Alfven latitudes), item\n"
     "    5 (L-411, the typed numbers in the Sun's hovers), item 7 (L-386,\n"
     "    the Sun's unexported rows), and L-371's own Gap (the Sun room's\n"
     "    unlinked numbers and the fifteen eyeballed shape numbers).\n"
     "  - THEN THE DRAWINGS TONY PICKS, decided when the numbers are done.\n"
     "    He leans to item 9 (L-410, the fades, with L-131, the dust cloud;\n"
     "    L-241, the Hills hover, rides inside L-410's design as before)\n"
     "    and item 3 (L-385, the opening view), with item 10 (L-128, the\n"
     "    comet ice lines) likely waiting.\n"
     "  - THEN L-443 (the objects to the website), its design session\n"
     "    first; Earth's talks are no longer in front of it.\n"
     "  Items 1, 2 and 8 were already done.\n"
     "**Gap:** the numbers first: L-228, L-411, L-386 and L-371's Gap; then\n"
     "Tony's choice of drawings; then L-443.\n"),

    # ---- L-413, Earth's list ----
    ('LEDGER_CONSOLIDATED.md', 'L-413 talks wait',
     "**Gap:** talk 2 (L-356 with L-375, and L-454), next session, its agenda in section 5 of\n"
     "`documentation/HANDOFF_earth_fade_build_20261017.md`; then talks 3 to 6. Talk 4 (L-314)\n"
     "keeps the solar-wind fetch; its aberration is built.\n",
     "- **2026-10-17, later, Tony's ruling** (the coordination session):\n"
     "  the design talks 2 to 6 wait; the Sun's slice (L-412) goes first,\n"
     "  its numbers before its drawings. " + TONY_1 + "\n"
     "  Talk 2's agenda stays where it is, section 5 of\n"
     "  `documentation/HANDOFF_earth_fade_build_20261017.md`, with its\n"
     "  starting prompt. This list's own text already allowed it: the\n"
     "  talks are \"interleaved with the Sun's list rather than blocking\n"
     "  it\" (2026-10-04).\n"
     "**Note (Claude, 2026-10-17):** the one dated thing a visitor meets\n"
     "meanwhile is the field's epoch (L-356), which the hover states.\n"
     "**Gap:** talks 2 to 6, after the Sun's numbers and the drawings Tony\n"
     "picks there (L-412): talk 2 (L-356 with L-375, and L-454), its agenda in section 5 of\n"
     "`documentation/HANDOFF_earth_fade_build_20261017.md`; then talks 3 to 6. Talk 4 (L-314)\n"
     "keeps the solar-wind fetch; its aberration is built.\n"),

    # ---- L-443, the objects to the website ----
    ('LEDGER_CONSOLIDATED.md', 'L-443 meta',
     "<!-- L:443 status:OPEN upd:2026-10-14 section:A flag: rice: -->",
     "<!-- L:443 status:OPEN upd:2026-10-17 section:A flag: rice: -->"),
    ('LEDGER_CONSOLIDATED.md', 'L-443 after the Sun',
     "**Gap:** after the Earth and Sun slices close: the design session, from\n"
     "the brief:",
     "- **Tony, 2026-10-17:** \"i would like to finish the sun slice and\n"
     "  then work on adding the symbols to the interactive.\" The order\n"
     "  holds, with Earth's remaining talks (L-413) moved out of its way:\n"
     "  this item follows the Sun's numbers and the drawings he picks\n"
     "  (L-412).\n"
     "**Gap:** after the Sun's numbers and its chosen drawings (L-412): the design session, from\n"
     "the brief:"),

    # ---- L-410, the fades ----
    ('LEDGER_CONSOLIDATED.md', 'L-410 gap',
     "**Gap:** the Sun's fades, the outer corona first with the\n"
     "dust cloud (L-131), in the Sun's slice (L-412).",
     "**Gap:** the Sun's fades, the outer corona first with the\n"
     "dust cloud (L-131), in the Sun's slice (L-412), after its numbers;\n"
     "Tony leans to doing them (2026-10-17), decided when the numbers are\n"
     "done."),

    # ---- L-385, the opening view ----
    ('LEDGER_CONSOLIDATED.md', 'L-385 meta',
     "<!-- L:385 status:OPEN upd:2026-10-04 section:A flag: rice: -->",
     "<!-- L:385 status:OPEN upd:2026-10-17 section:A flag: rice: -->"),
    ('LEDGER_CONSOLIDATED.md', 'L-385 gap',
     "**Gap:** read the Sun's autoscale with its default shells; propose how\n"
     "the view opens at photosphere + 10% and what the axis does; Tony's eye.\n",
     "**Gap:** read the Sun's autoscale with its default shells; propose how\n"
     "the view opens at photosphere + 10% and what the axis does; Tony's eye.\n"
     "After the Sun's numbers (L-412); Tony leans to doing it (2026-10-17).\n"),

    # ---- L-128, the comet ice lines ----
    ('LEDGER_CONSOLIDATED.md', 'L-128 meta',
     "<!-- L:128 status:OPEN upd:2026-10-08 section:A flag: rice: -->",
     "<!-- L:128 status:OPEN upd:2026-10-17 section:A flag: rice: -->"),
    ('LEDGER_CONSOLIDATED.md', 'L-128 likely waits',
     "- **2026-10-04 (Tony):** in the Sun's slice, its tenth item (L-412):\n"
     "  a design talk after the dust cloud, since both are about what fills\n"
     "  the space around the Sun.\n",
     "- **2026-10-04 (Tony):** in the Sun's slice, its tenth item (L-412):\n"
     "  a design talk after the dust cloud, since both are about what fills\n"
     "  the space around the Sun.\n"
     "- **2026-10-17 (Tony):** \"maybe wait on the ice lines\": likely the\n"
     "  one Sun drawing that waits behind the objects (L-443); decided when\n"
     "  the Sun's numbers are done (L-412).\n"),

    # ---- L-454, edges that move ----
    ('LEDGER_CONSOLIDATED.md', 'L-454 note and gap',
     "**Gap:** a design talk, on Earth's list (L-413) with talk 2.\n",
     "**Note (Claude, 2026-10-17):** the Sun's slice now goes before Earth's\n"
     "talk 2 (L-412). Its Alfven surface (L-228) and its fades (L-410) are\n"
     "edges of this kind, so the device's questions may be met there first;\n"
     "Earth's talk 2 then takes what the Sun decided, or asks them fresh.\n"
     "**Gap:** a design talk, on Earth's list (L-413) with talk 2, after the\n"
     "Sun's numbers (L-412).\n"),

    # ---- L-356, IGRF-14 ----
    ('LEDGER_CONSOLIDATED.md', 'L-356 meta',
     "<!-- L:356 status:OPEN upd:2026-09-22 section:A flag: rice: -->",
     "<!-- L:356 status:OPEN upd:2026-10-17 section:A flag: rice: -->"),
    ('LEDGER_CONSOLIDATED.md', 'L-356 note',
     "**Gap:** Re-source the six rows to IGRF-14 and move the epoch; the hover words move with it.\n",
     "**Note (Claude, 2026-10-17):** with Earth's talk 2 now behind the\n"
     "Sun's slice (L-412, L-413), this re-sourcing need not wait for the\n"
     "talk: the talk-2 brief (section 5 of\n"
     "`documentation/HANDOFF_earth_fade_build_20261017.md`) says method\n"
     "already answers it once the model is read. A small build on an evening\n"
     "of its own, at Tony's word; the hover states its epoch meanwhile.\n"
     "**Gap:** Re-source the six rows to IGRF-14 and move the epoch; the hover words move with it.\n"),

    # ---- Where We Are ----
    ('documentation/WHERE_WE_ARE.md', 'date and box',
     "Last updated: October 17, 2026, night: Earth's fade done.\n"
     "- Written at orrery adcc185 and gallery da442bf.\n"
     "\n"
     "> **READ THIS FIRST**\n"
     ">\n"
     "> **Changed since you last read this:**\n"
     "> - Earth's hydrogen fades out from 3 to 100 Earth radii in both\n"
     ">   instruments, live and looked at: \"looks right\", \"Looks good\"\n"
     ">   (L-410, the fades).\n"
     "> - The low-orbit look is done: \"contrast and shape are good\".\n"
     ">\n"
     "> **Do next:** *Earth's design talk 2, next session: section 5 of\n"
     "> HANDOFF_earth_fade_build_20261017.md.*\n"
     ">\n"
     "> **Needs you now:**\n"
     "> - *Run this small close patch, commit and push.*\n"
     "> - Talk 2 covers the field's newer model, its off-centre dipole, and\n"
     ">   a way to draw edges that move.",
     "Last updated: October 17, 2026, late: the Sun's slice is next.\n"
     "- Written at orrery 88fedb3 and gallery da442bf.\n"
     "\n"
     "> **READ THIS FIRST**\n"
     ">\n"
     "> **Changed since you last read this:**\n"
     "> - The order: Earth's remaining design talks wait. The Sun's slice\n"
     ">   (L-412, the Sun's list) goes next, its numbers before its drawings.\n"
     ">\n"
     "> **Do next:** *The Sun's numbers: L-228 (the Alfven latitudes), L-411\n"
     "> (typed numbers in the Sun's hovers), L-386 (the Sun's unexported\n"
     "> rows), L-371 (the Sun room's unlinked numbers).*\n"
     ">\n"
     "> **Needs you now:**\n"
     "> - *Run this small patch, commit and push.*\n"
     "> - After the numbers: which drawings? You lean to the fades with the\n"
     ">   dust cloud and the opening view; the ice lines wait."),
    ('documentation/WHERE_WE_ARE.md', 'road stage 5',
     "  5.   [NOW]   *Earth's list (L-413): the fade done; talk 2 next\n"
     "               session, then talks 3 to 6.* << moved this session",
     "  5.   [next]  Earth's list (L-413): talks 2 to 6 wait behind the\n"
     "               Sun's numbers. << moved this session"),
    ('documentation/WHERE_WE_ARE.md', 'road stage 7',
     "  7.   [next]  The Sun's numbers get the checking Earth's got; the Solar\n"
     "               System room's features close with these rooms.",
     "  7.   [NOW]   *The Sun's slice (L-412): numbers first, then the drawings\n"
     "               you pick; the Solar System room's features close too.* << moved this session"),
    ('documentation/WHERE_WE_ARE.md', 'settled',
     "- Belts: random dots, both curved. Low orbit starts at ESA's 180 km.\n"
     "  A lost run record stops the Daily Run. Lines past a hover's 17 go to\n"
     "  its i panel. What a visitor reads: in provenance-discipline. (Oct 17)\n",
     "- Belts: random dots, both curved. Low orbit starts at ESA's 180 km.\n"
     "  A lost run record stops the Daily Run. Lines past a hover's 17 go to\n"
     "  its i panel. What a visitor reads: in provenance-discipline. (Oct 17)\n"
     "- Earth's talks wait; the Sun's numbers, then its drawings, then the objects. (Oct 17)\n"),
    ('documentation/WHERE_WE_ARE.md', 'signals',
     "- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, adcc185).",
     "- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 88fedb3)."),
    ('documentation/WHERE_WE_ARE.md', 'details next',
     "- *Next: `HANDOFF_earth_fade_build_20261017.md`, section 5 (talk 2)*\n",
     "- *Next: L-412 (the Sun's list); Earth's talk 2 later: `HANDOFF_earth_fade_build_20261017.md` sec. 5*\n"),
]


class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError("missing file: %s (is this the right folder?)" % rel)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), (b"\r\n" in raw)


def fingerprint(rel, text):
    zone = ZONES.get(rel)
    if zone:
        a = text.index(zone[0])
        b = text.index(zone[1]) + len(zone[1])
        text = text[:a] + text[b:]
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def main():
    log, notes, texts, crlf = [], [], {}, {}
    try:
        for rel in sorted(set(e[0] for e in EDITS)):
            texts[rel], crlf[rel] = read(rel)
        for rel, want in FINGERPRINTS.items():
            if fingerprint(rel, texts[rel]) != want:
                raise PatchError("BASE MOVED: %s is not the file this patch "
                                 "was built against (%s)" % (rel, SHA))
            log.append("ok  base    %s matches %s" % (rel, SHA))
        for rel, label, old, new in EDITS:
            text = texts[rel]
            n = text.count(old)
            if n != 1:
                raise PatchError("ANCHOR FAIL [%s %s]: %d matches"
                                 % (rel, label, n))
            mark = MARKERS.get(rel)
            if mark and (text.count(mark) != 1
                         or text.index(old) + len(old) > text.index(mark)):
                raise PatchError("ANCHOR FAIL [%s %s]: not above the "
                                 "run-record marker" % (rel, label))
            texts[rel] = text.replace(old, new)
            log.append("ok  edit    %-44s %s" % (rel, label))
        page = 'documentation/WHERE_WE_ARE.md'
        above = texts[page].index(MARKERS[page])
        lines_above = texts[page][:above].count("\n")
        if lines_above > 130:
            raise PatchError("Where We Are would be %d lines above the "
                             "run-record marker; the cap is 130" % lines_above)
        log.append("ok  check   %-44s %d lines above the marker (cap 130)"
                   % (page, lines_above))
        for rel, text in texts.items():
            bad = sum(1 for ch in text if ord(ch) > 127)
            if bad:
                raise PatchError("%s: %d non-ASCII character(s) after the "
                                 "edits" % (rel, bad))
    except PatchError as exc:
        print("ERROR: %s" % exc)
        print("NOTHING was written.")
        print("Undo is not needed. Discard Changes in GitHub Desktop restores "
              "any file you changed by hand.")
        sys.exit(1)

    for rel, text in texts.items():
        with open(os.path.join(ROOT, rel), "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf[rel]:
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % rel)
    for line in log:
        print(line)
    for line in notes:
        print(line)
    print("stamps updated: the ledger's header; Where We Are's date")
    print("")
    print("patch applied (%d edits in %d files)" % (len(EDITS), len(texts)))
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py (dashboard): its ledger index")
    print("     picks up the dates.")
    print("  2. Move this script into documentation/; commit; push.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
