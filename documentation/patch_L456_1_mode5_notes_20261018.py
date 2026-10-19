#!/usr/bin/env python3
"""
patch_L456_1_mode5_notes_20261018.py -- records only: Tony's Mode 5
notes after L-455, written where the next sessions read them. No code
changes.

Built on orrery e4d4a9e318e25f66fe023d625879143af6a5ae2f at
https://github.com/tonylquintanilla/palomas_orrery ("L455 earth numbers
Gemini cross check"), with gallery c5c05b52 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 18, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L456_1_mode5_notes_20261018.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing. Each file is edited only at the lines it
changes, so your notes elsewhere in them are kept:

    LEDGER_CONSOLIDATED.md         L-456 new (what a visitor reads, in
                                   every room); L-385 widened to every
                                   view's opening; L-412's gap; L-351
                                   carries a test-order lesson; stamp
    documentation/WHERE_WE_ARE.md  by section, above the marker only
    documentation/HANDOFF_L455_earth_numbers_20261018.md
                                   section 7: your notes and the next
                                   session's starting prompt

WHAT IT PRINTS

    Success: one "ok" line per edit, then "patch applied".
    Failure: one ERROR or ANCHOR FAIL line and "NOTHING was written."
    A second run refuses: its anchors are gone once it has run.

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = 'e4d4a9e3'
MARKERS = {'documentation/WHERE_WE_ARE.md': '--- Your run record below this line'}
FINGERPRINTS = {}
RESULTS = {}
NEXT = ['  1. Commit the run record copy with your Mode 5 notes', '     (documentation/WHERE_WE_ARE_10-18-26_1326_run_record.md), this', '     script moved into documentation/, and the three files; push.', '     No maintenance run is needed: no code changed. The next one', '     rebuilds the ledger index with L-456 in it.', "  2. Next session: the handoff's section 7 starting prompt."]
NEW_FILES = {}
EDITS = [
    ('LEDGER_CONSOLIDATED.md', 'line 524: Module updated: October 18, 2026, late, ', 'a skill line carried on L-351), built on 05cb185a and gallery 10508dfc.\nReview and RICE update Tony 6-21-2026\n', "a skill line carried on L-351), built on 05cb185a and gallery 10508dfc.\nModule updated: October 18, 2026, late, with Anthropic's Claude Opus 5.5\n(Tony's Mode 5 notes after L-455: the opening-view rule for every view\non L-385; L-456 new, what a visitor reads, mostly for every room; a\ntest-order lesson carried on L-351), built on e4d4a9e3 and gallery\nc5c05b52.\nReview and RICE update Tony 6-21-2026\n", 1),
    ('LEDGER_CONSOLIDATED.md', 'line 1284: #### [L-456] What a visitor reads, from ', '## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n', '## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n#### [L-456] What a visitor reads, from Earth\'s Mode 5 look: body radii, sources as a list with live links, Celsius for Earth\'s surface and air (gallery + orrery)\n<!-- L:456 status:OPEN upd:2026-10-18 section:A flag: rice: -->\n- **Recorded 2026-10-18** from Tony\'s Mode 5 look at the Earth room\n  after L-455 was pushed (orrery e4d4a9e3, gallery c5c05b52), in his\n  run record `documentation/WHERE_WE_ARE_10-18-26_1326_run_record.md`.\n  Tony: "these should become the pattern for all rooms and maybe add\n  to the skill as needed."\n- **(1) A shell inside a body gives its radius in that body\'s radii\n  first.** On the inner core\'s hover: "it does not mention the radius\n  fraction." Then: "Yes, Re gives an intuitive sense of proportion.\n  Please add." The four lines, approved the same evening ("approved"),\n  each in the crust\'s form, Earth radii first:\n  inner core "Radius: 0.19151 Earth radii" / "= 1,221.5 km\n  (0.000008165 AU)"; outer core "Radius: 0.54561 Earth radii" /\n  "= 3,480.0 km (0.0000233 AU)"; lower mantle "Radius: 0.895 Earth\n  radii" / "= 5,710 km (0.0000382 AU)"; upper mantle "Radius: 0.99506\n  Earth radii" / "= 6,346.6 km (0.0000424 AU)". Each is already served\n  (the row\'s "in"), at its served count; the Earth radius is the\n  equatorial one, the unit the crust and the outer shells use.\n- **(2) Earth\'s surface and air temperatures add degrees Celsius in\n  brackets after the kelvin, for these Earth shells only.** The crust\'s\n  records: "for these surface temperatures, let\'s also add back degrees\n  Celsius parenthetically, in addition to degrees Kelvin." The lower\n  atmosphere: "add back degrees Celsius parenthetically." Then, on\n  being told this amended the kelvin rule: "this is not an amended\n  rule. It was a parenthetical addition for these earth shells only\n  because Celsius is familiar in terrestrial environments. The general\n  kelvin rule is unchanged." So provenance-discipline 2.31 stands as it\n  is, and no other room or shell gains Celsius from this. The Celsius\n  figures still come from their rows (kelvin minus 273.15, an exact\n  offset), not typed, as every served number does; the served\n  conversions today are factors only, so the build finds how. The\n  words come to Tony as a list.\n- **(3) The i panel\'s sources as a list:** "since the info panel\n  scrolls, can we organize the citations better so they are more\n  easily read? maybe instead of semicolons, separate with bullets."\n  Today a shell\'s citations are joined into one line with "; "\n  (`withShellWords`, `withGatheredSource` in\n  `gallery/feature_renderers.js`), and one citation can hold "; "\n  itself, so the list is carried as a list, not split from the line.\n- **(4) Live links:** "can we make source hyperlinks clickable? those\n  single lines are very difficult to select if copying to a browser."\n  The focus panel in `interactive.html` prints the Source line as plain\n  text.\n- (1), (3) and (4) are the pattern for every room ("these should\n  become the pattern for all rooms"): (3) and (4) are the panel\'s own\n  and reach every room at once; (1) is each room\'s words.\n  interactive-exhibit records them at the build. (2) is Earth\'s alone\n  and changes no skill.\n**Gap:** after the opening views (L-385): the four Earth-radii lines\n(approved); the Celsius words for Earth\'s surface and air as a list for\nTony; the panel\'s list and live links; interactive-exhibit\'s bump.\n**Ref:** gallery `gallery/feature_renderers.js`, `interactive.html`;\nprovenance-discipline (The Unit Field); interactive-exhibit; L-455,\nL-421, L-385.\n\n', 1),
    ('LEDGER_CONSOLIDATED.md', "line 2346: **Gap:** the drawings in Tony's order: L", "  behind L-443.\n**Gap:** the drawings in Tony's order: L-385, then L-410 with L-131\nand L-241; the streamer belt's and the clumps' eyeballed numbers with\n", "  behind L-443.\n**Gap:** the drawings in Tony's order: L-385 (now every view's\nopening, the Sun first, then Earth; 2026-10-18), then L-410 with L-131\nand L-241; the streamer belt's and the clumps' eyeballed numbers with\n", 1),
    ('LEDGER_CONSOLIDATED.md', 'line 2933: - **2026-10-18, later, the rule for ever', '(L-412).\n**Ref:** `documentation/HANDOFF_L322_D_orrery_pole_built_20260924.md` sec. 3; L-322.\n', '(L-412).\n- **2026-10-18, later, the rule for every view** (Tony\'s run record\n  `documentation/WHERE_WE_ARE_10-18-26_1326_run_record.md`). On the\n  orrery\'s low-orbit look: "the initial view of Earth has the same\n  issue as the Sun. the auto scale should be set to the farthest shell\n  drawn plus say 20%. the sun pointer should be ignored unless it is\n  the only feature drawn." Then: "start with the initial view of the\n  sun. it should follow the earth pattern: fartherst shell plus 20%.\n  this should be the rule for all rooms or system views." So this item\n  widens from the Sun to every orrery view, and the gap above is\n  replaced by the one below.\n**Gap (replaces the one above, 2026-10-18):** every orrery view opens\non the farthest shell drawn plus 20 percent; the line drawn toward the\nSun sets the view only when nothing else is drawn. Read the\nautoscale; build it for the Sun first, then Earth, then check the other\nviews; whether the Sun\'s long rotation axis is shortened or runs past\nthe view\'s edge is shown to Tony. The rule goes into\norrery-coding-conventions at the build. Tony\'s eye.\n**Ref:** `documentation/HANDOFF_L322_D_orrery_pole_built_20260924.md` sec. 3; L-322.\n', 1),
    ('LEDGER_CONSOLIDATED.md', 'line 3977: - **2026-10-18, agentic-pre-test, next b', "    does not name the check, so it is carried here.\n**Gap:** Each lands with its store's next bump.\n", '    does not name the check, so it is carried here.\n  - **2026-10-18, agentic-pre-test, next bump:** a patch pair is tested\n    in the order Tony runs it. L-455\'s order applied the website patch\n    before the orrery maintenance run. The sandbox ran that orrery run\n    beside a website copy whose config was already mirrored; on Tony\'s\n    machine it was not yet, since the Daily Run mirrors it later. So\n    "Exact rows by the count" failed there for\n    EARTH_LEO_UPPER_ALTITUDE_KM, "served prints None, the row states\n    4", where the handoff had promised 31 of 31. It passes at the pushed\n    pair (orrery e4d4a9e3, gallery c5c05b52), and nothing wrong was\n    pushed. The skill says nothing wrong; it does not cover a patch\n    pair, so it is carried here.\n**Gap:** Each lands with its store\'s next bump.\n', 1),
    ('documentation/WHERE_WE_ARE.md', 'line 4: Last updated: October 18, 2026, late: Ea', "\nLast updated: October 18, 2026, evening: Earth's numbers built; the numbers half done.\n- Written at orrery 05cb185 and gallery 10508df.\n\n", "\nLast updated: October 18, 2026, late: Earth's numbers pushed; your Mode 5 notes recorded.\n- Written at orrery e4d4a9e and gallery c5c05b5.\n\n", 1),
    ('documentation/WHERE_WE_ARE.md', "line 10: > - Earth's numbers are pushed and check", "> **Changed since you last read this:**\n> - Earth's numbers are built (L-455, typed numbers): every number in\n>   Earth's words comes from a row with a source you can open.\n> - A new website check, Typed numbers, fails on any digit with no row.\n", "> **Changed since you last read this:**\n> - Earth's numbers are pushed and checked on your phone (L-455).\n> - A new website check, Typed numbers, fails on any digit with no row.\n", 1),
    ('documentation/WHERE_WE_ARE.md', 'line 12: > - Your Mode 5 notes are recorded: ever', "> - A new website check, Typed numbers, fails on any digit with no row.\n> - The deep Earth's temperatures come from two open papers, which\n>   Gemini 4 found; National Geographic's figures are gone.\n>\n", "> - A new website check, Typed numbers, fails on any digit with no row.\n> - Your Mode 5 notes are recorded: every view opens on its farthest\n>   shell plus 20% (L-385); body radii and sources listed with live\n>   links in every room, Celsius for Earth's surface and air (L-456).\n>\n", 1),
    ('documentation/WHERE_WE_ARE.md', 'line 16: > **Do next:** *the opening views, the S', '>\n> **Do next:** *run the two L-455 patches in order: the handoff,\n> section 1.*\n>\n', ">\n> **Do next:** *the opening views, the Sun first, then Earth: the\n> handoff's section 7.*\n>\n", 1),
    ('documentation/WHERE_WE_ARE.md', 'line 66: - A spacecraft: by its own JPL data shee', '  check, with the orrery\'s own code: orbit and period together. (Oct 14, 15)\n- A spacecraft: by its own JPL data sheet; the Voyagers\' sky angle,\n  turned into km at their distance and said to be ours. (Oct 12)\n- "Surface": the solid surface, or one radius where there is none (a\n', '  check, with the orrery\'s own code: orbit and period together. (Oct 14, 15)\n- "Surface": the solid surface, or one radius where there is none (a\n', 1),
    ('documentation/WHERE_WE_ARE.md', 'line 87: - Every view opens on its farthest shell', "- The Sun's drawings: opening view, then corona fade with dust; ice lines wait. (Oct 18)\n\n", "- The Sun's drawings: opening view, then corona fade with dust; ice lines wait. (Oct 18)\n- Every view opens on its farthest shell plus 20%. Every room: body radii,\n  sources listed with live links. Kelvin stays; Celsius only for Earth's surface and air. (Oct 18)\n\n", 1),
    ('documentation/WHERE_WE_ARE.md', 'line 93: - Last cache build: 20261019T030849Z, ok', 'Read from files when this page was written, not typed from memory.\n- Last cache build: 20261018T181330Z, ok; one rename needed a second try (gallery 10508df).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 05cb185).\n  Whole tree: 280: orrery 116, Earth System 149, stars 13, utilities 2.\n', 'Read from files when this page was written, not typed from memory.\n- Last cache build: 20261019T030849Z, ok, every rename on the first try (gallery c5c05b5).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, e4d4a9e).\n  Whole tree: 280: orrery 116, Earth System 149, stars 13, utilities 2.\n', 1),
    ('documentation/WHERE_WE_ARE.md', 'line 119: - *Next: the opening views (L-385): `HAN', "- Every item: `LEDGER_CONSOLIDATED.md`.\n- *Next: the Sun's opening view (L-385): `HANDOFF_L455_earth_numbers_20261018.md` sec. 6*\n- Earth's words and Gemini 4: `WORDS_L455_*`, `REVIEW_L455_gemini4_*`\n", "- Every item: `LEDGER_CONSOLIDATED.md`.\n- *Next: the opening views (L-385): `HANDOFF_L455_earth_numbers_20261018.md` sec. 7*\n- Earth's words and Gemini 4: `WORDS_L455_*`, `REVIEW_L455_gemini4_*`\n", 1),
    ('documentation/HANDOFF_L455_earth_numbers_20261018.md', 'line 190: The starting prompt that stood here is r', '\nStarting prompt for the next session:\n', '\nThe starting prompt that stood here is replaced by section 7\'s.\n\n## 7. After the push: Tony\'s Mode 5 notes (added October 18, late)\n\nPushed at orrery e4d4a9e318e25f66fe023d625879143af6a5ae2f and gallery\nc5c05b52cdc3ea2800813fd3c73ae36599188408. Tony\'s run record,\n`documentation/WHERE_WE_ARE_10-18-26_1326_run_record.md`, carries the\nruns and his verdicts; every number on the Earth room checked "correct".\n\n**One step did not go as this handoff said.** The orrery maintenance\nrun (section 1, step 3) failed one check, "Exact rows by the count",\non EARTH_LEO_UPPER_ALTITUDE_KM: "served prints None, the row states 4".\nThe run order had the website patch in before that run, and the\nwebsite\'s config is only filled in by the Daily Run, later. The sandbox\ntest had run beside an already filled-in config, so it passed there. At\nthe pushed pair the check passes; nothing wrong was pushed. The lesson\nis carried on L-351 for agentic-pre-test.\n\n**His notes, now rules:**\n- **Every view opens on its farthest shell drawn, plus 20 percent; the\n  line toward the Sun counts only when nothing else is drawn** (L-385,\n  widened from the Sun to every orrery view). "start with the initial\n  view of the sun. it should follow the earth pattern: fartherst shell\n  plus 20%. this should be the rule for all rooms or system views."\n  This replaces the 10 to 20 percent of section 6.\n- **What a visitor reads** (L-456, new). For every room: a shell inside\n  a body gives its radius in body radii first (the four Earth lines are\n  approved); the i panel lists its sources one per line, and their\n  links can be clicked. For Earth\'s surface and air only: degrees\n  Celsius in brackets after the kelvin, worked out from the row. Tony:\n  "It was a parenthetical addition for these earth shells only because\n  Celsius is familiar in terrestrial environments. The general kelvin\n  rule is unchanged."\n\nStarting prompt for the next session:\n', 1),
    ('documentation/HANDOFF_L455_earth_numbers_20261018.md', 'line 227: Build session: the opening views in the ', "```\nBuild session: the Sun's opening view in the orrery (L-385), the first\nof the Sun's drawings (L-412). The view opens at about the Sun's\nradius plus 10 to 20 percent, like the website's Sun room.\nPull both repositories and say the SHAs; the handoff is\ndocumentation/HANDOFF_L455_earth_numbers_20261018.md, section 6.\nConfirm your loaded skills against the manifest before work that fires\n", "```\nBuild session: the opening views in the orrery (L-385), the first of\nthe Sun's drawings (L-412). Every view opens on its farthest shell\ndrawn plus 20 percent; the line toward the Sun counts only when\nnothing else is drawn. The Sun first, then Earth, then check the other\nviews. Pull both repositories and say the SHAs; the handoff is\ndocumentation/HANDOFF_L455_earth_numbers_20261018.md, section 7.\nConfirm your loaded skills against the manifest before work that fires\n", 1),
]

class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError("missing file: %s (is this the right folder?)" % rel)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), (b"\r\n" in raw)


def fingerprint(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def main():
    log, notes, texts, crlf = [], [], {}, {}
    try:
        for rel, content in NEW_FILES.items():
            if os.path.exists(os.path.join(ROOT, rel)):
                have, _c = read(rel)
                if have != content:
                    raise PatchError("%s already exists with other content; "
                                     "nothing was overwritten" % rel)
                notes.append("note: %s already present, identical" % rel)
            else:
                log.append("ok  new     %s" % rel)
        for rel in sorted(set(e[0] for e in EDITS)):
            texts[rel], crlf[rel] = read(rel)
        for rel, want in FINGERPRINTS.items():
            if fingerprint(texts[rel]) != want:
                raise PatchError("BASE MOVED: %s is not the file this patch "
                                 "was built against (%s)" % (rel, SHA))
            log.append("ok  base    %s matches %s" % (rel, SHA))
        for rel, label, old, new, count in EDITS:
            text = texts[rel]
            n = text.count(old)
            if n != count:
                raise PatchError("ANCHOR FAIL [%s %s]: %d matches, expected %d"
                                 % (rel, label, n, count))
            mark = MARKERS.get(rel)
            if mark and (text.count(mark) != 1
                         or text.rindex(old) + len(old) > text.index(mark)):
                raise PatchError("ANCHOR FAIL [%s %s]: not above the "
                                 "run-record marker" % (rel, label))
            texts[rel] = text.replace(old, new)
            log.append("ok  edit    %-44s %s" % (rel, label))
        for rel, want in RESULTS.items():
            if fingerprint(texts[rel]) != want:
                raise PatchError("%s did not come out as built" % rel)
        for page, mark in MARKERS.items():
            above = texts[page][:texts[page].index(mark)].count("\n")
            if above > 130:
                raise PatchError("%s would be %d lines above the run-record "
                                 "marker; the cap is 130" % (page, above))
            log.append("ok  check   %-44s %d lines above the marker (cap 130)"
                       % (page, above))
        for rel, text in list(texts.items()) + list(NEW_FILES.items()):
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

    for rel, content in NEW_FILES.items():
        path = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
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
    print("")
    print("patch applied (%d new files, %d edits in %d files)"
          % (len(NEW_FILES), len(EDITS), len(texts)))
    print("")
    print("NEXT:")
    for line in NEXT:
        print(line)
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
