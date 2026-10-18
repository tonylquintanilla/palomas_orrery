#!/usr/bin/env python3
"""
patch_L410_3_earth_fade_close_20261017.py -- the close of Earth's fade
build: records the build on L-410 (waiting on Tony's runs and looks),
the low-orbit look and the fade on L-413, the stored_fade method owed on
L-435, the third stored drawing on L-434; updates Where We Are; and adds
the session's handoff, which carries the brief for Earth's design
talk 2.

Built on orrery 785536e5b700518d17c86d8381f0994a15d20bb7 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
44a6225c0049a36e72c770ad4557be31dde72250 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 17, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L410_3_earth_fade_close_20261017.py

    Saved in the ORRERY folder above. Run it after
    patch_L410_1_earth_fade_orrery_20261017.py and before the orrery
    maintenance run. Open it in VS Code and click Run. It takes no
    arguments and asks no questions.

WHAT IT DOES, all or nothing; each file is edited only at the lines it
changes, so your notes elsewhere are kept:

    LEDGER_CONSOLIDATED.md   L-410, L-413, L-435, L-434; the header stamp
    documentation/WHERE_WE_ARE.md
                             above the run-record marker only: the date,
                             the box, road stage 5, the signals, the
                             details
    documentation/HANDOFF_earth_fade_build_20261017.md     NEW

WHAT IT PRINTS

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = '785536e5'
ZONES = {}
MARKERS = {'documentation/WHERE_WE_ARE.md': '--- Your run record below this line'}
FINGERPRINTS = {}
RESULTS = {}
DELETES = {}
NEW_FILES = {'documentation/HANDOFF_earth_fade_build_20261017.md': '<!-- Doc-Kind: hand | Session record of Earth\'s fade build (L-410): the hydrogen exosphere drawn as stored dots that thin out from 3 to 100 Earth radii in both instruments, three patches with Tony\'s run order; and the brief for the next session, Earth\'s design talk 2 (L-356 with L-375, and L-454). -->\n# Handoff: Earth\'s fade, the build; and the brief for design talk 2\n\nBuilt on orrery 785536e5b700518d17c86d8381f0994a15d20bb7 at\nhttps://github.com/tonylquintanilla/palomas_orrery ("L330 leo contrast\nclose") and gallery 44a6225c0049a36e72c770ad4557be31dde72250 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io ("L330\nwebsite belt words L449 run records"). Nothing pushed by this session;\nTony pushes.\nTony\'s local folders: orrery\nC:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\ngallery\nC:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n\nType: BUILD (L-410, Earth\'s fade), and a brief for the next session\'s\nDESIGN talk (section 5).\nCompanions: the design, `documentation/DESIGN_fades_rulings_20261017.md`;\nthe sources and rows, `documentation/SOURCES_earth_fade_20261017.md`;\nthe round-1 records earlier the same day,\n`documentation/HANDOFF_earth_round1_build_20261017.md` and\n`documentation/HANDOFF_earth_round1_close_20261017.md`.\n\n## 1. Your run order (every Tony-action, in one list)\n\nEach patch checks the files it edits and refuses rather than guess.\n\n1. **(decide)** The look and the words, sent in the session with a\n   render of both zooms. Run nothing below until they read right to you.\n2. **(do)** Orrery folder: run `patch_L410_1_earth_fade_orrery_20261017.py`.\n3. **(do)** Orrery folder: run `patch_L410_3_earth_fade_close_20261017.py`\n   (the ledger, Where We Are, and this handoff).\n4. **(do)** Orrery maintenance run (dashboard). Expect 31 of 31 gating,\n   "Drawings export check" with 8 of 8 planted faults caught, and the\n   gate line at 0 TIER-1. Your Earth plot this afternoon refreshed\n   Earth\'s orbital elements (committed in 785536e5), so this run\n   re-exports Earth\'s period and its Horizons check confirms it with\n   JPL; that needs the internet, and would happen without these patches.\n5. **(look)** Mode 5 in the orrery: plot Earth with the Exosphere\n   (Geocorona) box on, and the belts. The dots thin out from Earth past\n   the Moon\'s orbit; zoom in to see them among the belts. Hover the\n   marker over the north pole, out at 100 Earth radii.\n6. **(do)** Move the two orrery scripts into `documentation/`; commit;\n   push. The website\'s Daily Run pulls the dots and rows from this push.\n7. **(do)** Website folder: run `patch_L410_2_earth_fade_website_20261017.py`.\n8. **(do)** The Daily Run. Expect its pulls to bring\n   `data/drawings/earth_exosphere.json`, 29 of 29 gating, "Drawings"\n   with 12 of 12 planted faults caught, and "Typed facts" with OPEN\n   empty.\n9. **(do)** Move the website script into `documentation/`; commit; push;\n   then `python gallery_maintenance_run.py --live`.\n10. **(look)** Mode 5 on the phone, in the Earth room: tick the\n    exosphere; the dots, its hover, its i panel (the words and three\n    Sources: where the dots start, the density, where they stop).\n\nNo skill changed, so nothing to reinstall.\n\n## 2. What was built, and how it was checked\n\n**Orrery patch (L-410).**\n- `earth_exosphere_sampler.py`, new: 1,500 dots from 3 to 100 Earth\n  radii. Each dot\'s distance is drawn from n(r) r^2, where n(r) is\n  Zoennchen et al. (2022)\'s eq. 7 to 15 Earth radii and then eq. 9\'s\n  fall carried on from eq. 7\'s value there; its direction is even on\n  the sphere; seed 410. Each dot\'s weight is the log of the density at\n  its distance, 0 at 100 and 1 at 3 Earth radii, so both instruments\n  shade it the same way. Its checks: every dot between the rows; in\n  five shells, each holds the profile\'s share (four standard deviations\n  or 15 percent); each weight is the one its distance gives.\n- `constants_new.py`: the seven approved rows, and an eighth,\n  `EARTH_EXOSPHERE_H_AT_RADII` (10 Earth radii), where the 35 atoms per\n  cubic centimetre was measured, from the same abstract, so the hover\n  does not type it. Three unit tokens in `constants_tokens.py`.\n  `EARTH_GEOCORONA_RADII`\'s note says it is now where the dots stop.\n- `earth_visualization_shells.py`: `create_earth_exosphere_shell()` and\n  the new hover words; `shell_configs.py` moves the exosphere from the\n  sphere shells to the custom builders.\n- `export_drawings.py` writes `data/drawings/earth_exosphere.json`;\n  `test_drawings_export.py` checks it, with three planted faults (an\n  inside dot, no fall-off, a wrong weight); 8 of 8 in all.\n- `orrery_maintenance_run.py` watches the new file; the dashboard\'s\n  Drawings Export card names all three drawings.\n\n**Website patch (L-410).**\n- `data/objects_config.json`: the geocorona is a `stored_fade` shape\n  naming the drawing `earth_exosphere`; pointers to the four rows its\n  words print (the mirror fills them at the Daily Run); each edge\'s\n  sentence as its `hover_line`; the `about` and `note` in the approved\n  words; the name drops "detected extent"; the sphere\'s opacity, point\n  count and marker size are gone with the sphere.\n- `gallery/feature_renderers.js`: `renderStoredFade()` draws the dots\n  as given, scaled by Earth\'s served radius, turned to the pole, shaded\n  by weight; one info marker over the pole at 100 Earth radii.\n- `tools/check_drawings.py`: the exosphere is round, so it has no plane\n  to check; it is judged by its mechanism instead -- between the served\n  edges, centred on Earth, thinning out -- with three planted faults;\n  12 of 12 in all.\n- `documentation/smoke_display_figures.js` grades the two edge\n  sentences by its own arithmetic, pinned: "3 Earth radii, about 20,000\n  km (0.0001 AU)" and "100 Earth radii, about 600,000 km (0.004 AU)".\n- `documentation/payload_earth_scene.json` re-recorded.\n- `gallery_maintenance_run.py`: the live check also fetches the belts\'\n  and the exosphere\'s served dots (section 4).\n\n**Tested.** Orrery: the maintenance run on a clean copy with the patch\napplied; 32 of 33 checkers passed here, 30 of 31 gating, the one\nred being "Horizons confirmations", which cannot reach JPL from the\nsandbox to confirm Earth\'s re-exported period (step 4); "Drawings export\ncheck" 8 of 8 planted faults caught; "Dashboard parity" green; the gate\nline 0 TIER-1, whole tree 280 as before. Website: a stand-in for your Daily Run\n(the patched copy, the orrery\'s new export and drawing laid in,\nmirrored, the served features and drawings rebuilt): 29 of 29 gating.\nBoth patches applied clean, and on a copy with Windows line endings,\nand refuse a second run. The website\'s own renderer was drawn headless\nand matches the orrery\'s picture.\n\n## 3. Choices made in the build, for your look\n\n- The eighth row (above): One Value, One Home, not a design change.\n- The shading: opacity 25 to 90 percent and size 1.5 to 3 by weight, as\n  for the belts; the colour the old shell had, pale lavender.\n- The info marker over the north pole at 100 Earth radii, where the old\n  shell\'s sat.\n- The 2024 paper\'s day-night sentence is cited on the row where the\n  dots start, so a visitor sees the source of "denser near the line\n  from the Sun to Earth" (What a Visitor Reads, principle 4).\n- From 3 to 7 Earth radii the hydrogen\'s pale lavender dots sit among\n  the outer belt\'s light blue ones; the two colours are close. Your eye\n  decides.\n\n## 4. Found, and where it went\n\n- The live check\'s list of files the browser fetches named the Hills\n  cloud\'s drawing but not the belts\' (missed by L-330\'s patch 3). Fixed\n  in the website patch, with the exosphere\'s.\n- The orrery dashboard\'s Drawings Export card still described only the\n  Hills cloud. Fixed in the orrery patch.\n- Placing the new builder beside the old upper-atmosphere function\n  pushed that dead function\'s text out of the scanner\'s reach of its\n  citation (Tier-1 280 to 281). The builder was moved beside the\n  low-orbit builder instead; 280 again. The dead function is L-254\'s.\n- Owed to interactive-exhibit\'s next version: the `stored_fade` shape\n  (L-435).\n\n## 5. Next session: Earth\'s design talk 2 (the brief)\n\nTony, 2026-10-17: "we can hold the design talk 2 for the handoff." Zero\ncode. Three items, all about Earth\'s magnetic field and how it moves.\nRead each in the ledger first; the questions below are where to start,\none at a time.\n\n1. **L-356 (IGRF-14).** The belts\' plane and the dipole cone use\n   IGRF-13\'s 2020 coefficients, whose drift was a forecast for 2020 to\n   2025; IGRF-14 replaces them. Question: re-source the six rows to\n   IGRF-14 and move the epoch, so the hovers\' "for 2020 (IGRF-13 model)"\n   becomes the new model\'s date? Method says yes once read; the talk\n   only needs to confirm the slice.\n2. **L-375 (the dipole\'s offset).** Earth\'s magnetic dipole sits off\n   the planet\'s centre, by an amount that turns with Earth once a day;\n   neither instrument models Earth\'s rotation phase. Questions: is the\n   offset shown at all; if so, as an envelope (the dipole cone\'s\n   pattern) rather than one position; and whether the website draws the\n   dipole cone, which only the orrery does today. The starting source,\n   Koochak and Fraser-Smith (2017), has not been read: the publisher\n   refused the session. Read it first.\n3. **L-454 (edges that move).** The magnetopause and bow shock stay\n   sharp at their models; their motion gets a second drawn device, like\n   the dipole cone. The store already holds how far real crossings sit\n   from each model (1.23 and 0.69 Earth radii). Questions: what the\n   device looks like (a translucent band either side of the surface? a\n   second surface at each end?), and what the spread means -- the\n   crossings\' scatter about the model, not the range the edge moves\n   through with the solar wind. The Alfven surface and the\n   heliosphere\'s edges are the same kind, in the Sun\'s slice later.\n\nAfter talk 2, Earth\'s list (L-413) has talks 3 to 6; talk 4 (L-314)\nkeeps the solar-wind fetch.\n\n## 6. Skill obligations\n\nThis session confirmed its loaded copies read provenance-discipline\n2.30 and interactive-exhibit 1.17 (discharging v3.102\'s obligation for\nboth), and orrery-coding-conventions 1.10, agentic-pre-test 1.3 and\nledger-and-session-records 1.21, as the manifest expects. Still\ntravelling: gallery-cache-builder 1.11 (v3.102) and\nhorizons-orbital-mechanics 1.8 (v3.99); no work this session fired\neither.\n\nSession written October 17, 2026 with Anthropic\'s Claude Opus 5.5.\n'}
EDITS = [
    ('LEDGER_CONSOLIDATED.md', 'header stamp', 'updated), built on fc2bb6f9 and gallery 44a6225c.\n', "updated), built on fc2bb6f9 and gallery 44a6225c.\nModule updated: October 17, 2026 with Anthropic's Claude Opus 5.5\n(Earth's fade built in two patches, waiting on Tony's runs and looks:\nL-410; the low-orbit look recorded on L-413; L-434 and L-435 updated),\nbuilt on 785536e5 and gallery 44a6225c.\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-410 built', "**Gap:** Earth's fade built from those rows; then the Sun's fades,", '- **Built 2026-10-17** (orrery `patch_L410_1_earth_fade_orrery_20261017.py`,\n  gallery `patch_L410_2_earth_fade_website_20261017.py`), on Tony\'s word\n  "yes, let\'s complete earth\'s fade":\n  - `earth_exosphere_sampler.py` places 1,500 dots from 3 to 100 Earth\n    radii, distances drawn from n(r) r^2 (eq. 7 to 15 Earth radii, then\n    eq. 9\'s fall from eq. 7\'s value there), directions even on the\n    sphere, seed 410; each dot\'s weight is the log of its density between\n    100 (0) and 3 (1). Its checks: every dot between the rows, five\n    shells each holding the profile\'s share, each weight the one its\n    distance gives. Stored as `data/drawings/earth_exosphere.json`, the\n    third stored drawing; three planted faults (8 of 8 in all).\n  - The rows: the seven approved, and an eighth, `EARTH_EXOSPHERE_H_AT_RADII`\n    (10), the distance the 35 per cubic centimetre was measured at, so the\n    hover does not type it (One Value, One Home). Three unit tokens:\n    `per_cm3`, `falloff_exponent`, `density_fit_coefficient`. The 2024\n    paper\'s day-night sentence joins `EARTH_EXOSPHERE_H_FIT_INNER_RADII`\'s\n    Source, read at its abstract and sec. 3.2, 2.2.1 and 2.3 (What a\n    Visitor Reads, principle 4).\n  - The orrery draws the dots (`create_earth_exosphere_shell`, now a\n    custom builder; the sphere shell is gone), shaded like the belts,\n    one info marker over the pole at 100 Earth radii. The website draws\n    the same dots as a `stored_fade` shape, its hover from each edge\'s\n    served `hover_line`, its i panel from the served `about` and `note`\n    with their numbers filled from served rows. The served name drops\n    "detected extent". The website\'s drawings check judges the dots by\n    their mechanism: between the served edges, centred on Earth,\n    thinning out; three planted faults (12 of 12 in all).\n  - Words sent to Tony with a render of both zooms before the patches\n    were saved; his answer is the gate for running them.\n  - Found and fixed: the live check\'s list of files the browser fetches\n    lacked the belts\' drawing (patch 3 of L-330); it now names both\n    Earth drawings. The orrery dashboard\'s Drawings Export card named\n    only the Hills cloud; it names all three.\n  - Tested: the orrery run on the patched copy, gating checkers green\n    but Horizons confirmations, which the sandbox cannot reach JPL for:\n    Tony\'s Earth plot of 2026-10-17 refreshed Earth\'s elements\n    (785536e5), so any run now re-exports Earth\'s period and confirms it\n    with JPL, patch or not. Whole tree 280 Tier-1 as before, gate path 0. A sandbox stand-in for\n    the Daily Run: 29 of 29 gating. Both patches applied clean, on\n    Windows line endings, and refuse a second run.\n  Record: `documentation/HANDOFF_earth_fade_build_20261017.md`.\n**Gap:** Tony\'s runs, and his looks in both instruments, close Earth\'s\nfade; then the Sun\'s fades,'),
    ('LEDGER_CONSOLIDATED.md', 'L-413 low orbit and fade', "**Gap:** Tony's look at the low-orbit dots in his next orrery plot\n(Mode 5); then Earth's fade built (L-410) or talk 2 (L-356 with L-375,\nand L-454), Tony's choice which first;", '- **2026-10-17, the low-orbit look:** "contrast and shape are good"\n  (Tony\'s run record, `documentation/WHERE_WE_ARE_10-16-26_2116_run_record.md`,\n  saved again that evening; pushed 785536e5). Then, Tony: "yes, let\'s\n  complete earth\'s fade. we can hold the design talk 2 for the handoff."\n  Earth\'s fade built the same evening (L-410), waiting on his runs and\n  looks.\n**Gap:** Tony\'s runs and looks at Earth\'s fade (L-410); then talk 2 (L-356\nwith L-375, and L-454), next session, its agenda in section 5 of\n`documentation/HANDOFF_earth_fade_build_20261017.md`;'),
    ('LEDGER_CONSOLIDATED.md', 'L-435 stored fade', '  edited, and removed, by the store writer. Also owed: the fades rule\n  (L-410) as method for any room.', "  edited, and removed, by the store writer. Also owed: the fades rule\n  (L-410) as method for any room; and, from Earth's fade (2026-10-17), a\n  `stored_fade` shape: a shell drawn as the orrery's stored dots between\n  its served `inner_radius` and `radius`, each edge's sentence its\n  `hover_line`."),
    ('LEDGER_CONSOLIDATED.md', 'L-434 third drawing', '**Gap:** a design talk on which shapes, in what order; L-239 for the\nclumps and the tide;', "- **2026-10-17:** Earth's hydrogen exosphere became the third stored\n  drawing (L-410), after the Hills cloud and the belts.\n**Gap:** a design talk on which shapes, in what order; L-239 for the\nclumps and the tide;"),
    ('documentation/WHERE_WE_ARE.md', 'date and box', "Last updated: October 17, 2026, evening: Earth's round 1 closed.\n- Written at orrery fc2bb6f and gallery 44a6225.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - Round 1 is live and closed: the belts, your words, the citations,\n>   the run-records check. Four items closed on your runs and looks.\n> - The low-orbit dots are brighter and larger, so the inner belt no\n>   longer hides them (your option A). The tooltip says 180 km.\n> - The seven fade rows are approved (L-410, the fades).\n>\n> **Do next:** *Run patch_L330_4_leo_contrast_close_20261017.py, then\n> the orrery run; plot Earth and look at the low-orbit dots; push.*\n>\n> **Needs you now:**\n> - *After that look: Earth's fade built first, or talk 2?*", 'Last updated: October 17, 2026, night: Earth\'s fade built.\n- Written at orrery 785536e and gallery 44a6225.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - Earth\'s hydrogen now fades out from 3 to 100 Earth radii in both\n>   instruments, where it was a sharp shell (L-410, the fades). Built,\n>   waiting on your runs and looks.\n> - The low-orbit look is done: "contrast and shape are good".\n>\n> **Do next:** *Your run order, section 1 of\n> HANDOFF_earth_fade_build_20261017.md.*\n>\n> **Needs you now:**\n> - *Two orrery patches, the run, push; the website patch, the Daily\n>   Run, push; then the two looks.*\n> - Next session: Earth\'s design talk 2 (that handoff, section 5).'),
    ('documentation/WHERE_WE_ARE.md', 'road stage 5', "  5.   [NOW]   *Earth's list (L-413): round 1 closed; the low-orbit\n               look; then Earth's fade or talk 2.* << moved this session", "  5.   [NOW]   *Earth's list (L-413): the fade built, your runs and\n               looks; then talk 2, next session.* << moved this session"),
    ('documentation/WHERE_WE_ARE.md', 'signals', '- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, fc2bb6f).', '- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 785536e).'),
    ('documentation/WHERE_WE_ARE.md', 'details next', "- *Next: `HANDOFF_earth_round1_close_20261017.md` (your run order)*\n- Round 1's build: `HANDOFF_earth_round1_build_20261017.md`; the fade's\n  sources and rows: `SOURCES_earth_fade_20261017.md`", "- *Next: `HANDOFF_earth_fade_build_20261017.md` (your run order; talk 2)*\n- The fade's sources and rows: `SOURCES_earth_fade_20261017.md`"),
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
        for rel, content in NEW_FILES.items():
            if os.path.exists(os.path.join(ROOT, rel)):
                have, _c = read(rel)
                if have != content:
                    raise PatchError("%s already exists with other content; "
                                     "nothing was overwritten" % rel)
                notes.append("note: %s already present, identical" % rel)
            else:
                log.append("ok  new     %s" % rel)
        for rel, want in DELETES.items():
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                notes.append("note: %s is already gone" % rel)
                continue
            have, _c = read(rel)
            if hashlib.md5(have.encode("utf-8")).hexdigest() != want:
                raise PatchError("%s is not the file this patch removes "
                                 "(its content changed); nothing was written"
                                 % rel)
            log.append("ok  delete  %s" % rel)
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
        for rel, want in RESULTS.items():
            if fingerprint(rel, texts[rel]) != want:
                raise PatchError("%s did not come out as built" % rel)
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
    for rel in DELETES:
        path = os.path.join(ROOT, rel)
        if os.path.exists(path):
            os.remove(path)
            folder = os.path.dirname(path)
            if folder != ROOT and not os.listdir(folder):
                rel_folder = os.path.relpath(folder, ROOT).replace(os.sep, "/")
                try:
                    os.rmdir(folder)
                    log.append("ok  delete  %s/ (now empty)" % rel_folder)
                except OSError as exc:
                    # L-448: Windows (OneDrive) can refuse to remove a
                    # folder it has just seen emptied. Every write has
                    # already landed, so this is a note, never a crash.
                    notes.append("note: %s/ is empty but Windows refused to "
                                 "remove it (%s); delete it by hand, git "
                                 "ignores an empty folder" % (rel_folder, exc))
    for line in log:
        print(line)
    for line in notes:
        print(line)
    print("stamps updated: the ledger's header; Where We Are's date")
    print("")
    print("patch applied (%d new file, %d edits in %d files)"
          % (len(NEW_FILES), len(EDITS), len(texts)))
    print("")
    print("NEXT (section 1 of documentation/HANDOFF_earth_fade_build_20261017.md):")
    print("  1. Run orrery_maintenance_run.py (dashboard).")
    print("  2. Plot Earth with the exosphere on (Mode 5).")
    print("  3. Move both orrery scripts into documentation/; commit; push.")
    print("  4. Then the website patch, in the WEBSITE folder, and the Daily Run.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
