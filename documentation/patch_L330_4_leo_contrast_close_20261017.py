#!/usr/bin/env python3
"""
patch_L330_4_leo_contrast_close_20261017.py -- the close of Earth's
round 1, on Tony's runs and looks. Makes the orrery's low-orbit dots
visible against the inner radiation belt (Tony's option A: full
opacity, size 2.5), corrects the low-orbit checkbox tooltip's "roughly
200 km" by reading both edges from the store's rows, and records the
close: L-330, L-451, L-452 and L-450 closed; L-449's check seen
working; L-410's fade rows approved; L-231, L-413 and L-455 updated;
Where We Are; and the session's close handoff.

Built on orrery fc2bb6f9211935bec87ce92ed7f7c6268bb4d050 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
44a6225c0049a36e72c770ad4557be31dde72250 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 17, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L330_4_leo_contrast_close_20261017.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing:

    earth_visualization_shells.py   the low-orbit dots, tooltip and
                                    docstring
    shell_configs.py                the unused copy of that tooltip, to
                                    agree with it ("roughly" dropped)
                                    -- both checked whole, before and
                                    after, so a changed copy is refused
    LEDGER_CONSOLIDATED.md          L-330, L-451, L-452, L-450 closed;
                                    L-449, L-410, L-231, L-413, L-455;
                                    the header stamp -- edited only at
                                    those lines, so your notes are kept
    documentation/WHERE_WE_ARE.md   above the run-record marker only: the
                                    date, the box, road stage 5, the
                                    signals, the details
    documentation/HANDOFF_earth_round1_close_20261017.md     NEW

WHAT IT PRINTS

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = 'fc2bb6f9'
ZONES = {}
MARKERS = {'documentation/WHERE_WE_ARE.md': '--- Your run record below this line'}
FINGERPRINTS = {'earth_visualization_shells.py': '6c3ce2be6453e8597019eaf1cb57e7c4', 'shell_configs.py': '81944530e4bd0c34d22c770fc14955d2'}
RESULTS = {'earth_visualization_shells.py': '61d3e2a8a3a5889705bd488a0c91a1c5', 'shell_configs.py': '461617d1c678761bc976b775ea2997d4'}
DELETES = {}
NEW_FILES = {'documentation/HANDOFF_earth_round1_close_20261017.md': '<!-- Doc-Kind: hand | Session record of Earth\'s round-1 close: Tony\'s runs and looks close L-330, L-451, L-452 and L-450; L-449\'s check seen working; the fade rows approved; the low-orbit dots made visible against the inner belt and the low-orbit tooltip\'s 200 km corrected, in one orrery patch. -->\n# Handoff: Earth round 1, the close\n\nBuilt on orrery fc2bb6f9211935bec87ce92ed7f7c6268bb4d050 at\nhttps://github.com/tonylquintanilla/palomas_orrery ("L330 belts words\ncitations and earth round 1 build close") and gallery\n44a6225c0049a36e72c770ad4557be31dde72250 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io ("L330\nwebsite belt words L449 run records"). Nothing pushed by this session;\nTony pushes.\nTony\'s local folders: orrery\nC:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\ngallery\nC:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n\nType: BUILD (one small orrery patch) and DOCUMENTATION (the close).\nCompanion: the build\'s record,\n`documentation/HANDOFF_earth_round1_build_20261017.md`. This is the\nsame session, after Tony\'s runs.\n\n## 1. Your run order (every Tony-action, in one list)\n\n1. **(do)** Orrery folder: run\n   `patch_L330_4_leo_contrast_close_20261017.py`.\n2. **(do)** Orrery maintenance run (dashboard). Expect 31 of 31 gating\n   and the gate line at 0 TIER-1.\n3. **(look)** Plot Earth with the magnetosphere and low Earth orbit on.\n   The low-orbit dots should now show as warm white points among the\n   inner belt\'s red ones. Hover the low-orbit checkbox: its tooltip\n   should say 180 km.\n4. **(do)** Move the patch into `documentation/`; commit, with your run\n   record; push.\n5. **(decide)** Then: Earth\'s fade built first (L-410, its rows\n   approved), or design talk 2 (L-356 with L-375, the field\'s model and\n   offset, and L-454, the device for edges that move)?\n\nNo skill changed, so nothing to reinstall.\n\n## 2. Your runs and looks, as recorded\n\nRead from your run record,\n`documentation/WHERE_WE_ARE_10-16-26_2116_run_record.md` (saved again\non Oct 17 with the round-1 runs):\n- Orrery maintenance run: 31 of 31 gating; push fc2bb6f9.\n- Skills reinstalled; v3.102 uploaded to the project.\n- Daily Run: pulls 5 of 5; run records 86 before and 86 after the\n  copy; 29 of 29 gating, Drawings 7 of 7, Typed facts 0 held open;\n  push 44a6225c; live check 2 of 2.\n- Orrery look: "looks good except that the color contrast between the\n  lower belt and the LEO is not enough to see LEO dots."\n- Phone look: "correct". The seven fade rows: "approved". The three\n  wordings: "Approved." (in this session).\n\n## 3. What the patch does\n\n`earth_visualization_shells.py`, three edits, all in low Earth orbit:\n- The dots: full opacity and size 2.5, was 35% and size 1.5. Your\n  option A of three; a throwaway render compared 2.5 and 3 against the\n  inner belt, and 3 crowded it.\n- The checkbox tooltip reads 180 km and 2,000 km from the same rows the\n  hover reads; it said "roughly 200 km", a copy patch 2 missed.\n- The builder\'s docstring names the two rows instead of "~200 km".\n\n`shell_configs.py`, one edit: its unused copy of that tooltip (the\n`tooltip` field nothing reads, kept agreeing with the live one by the\ncoding conventions) drops "roughly".\n\nThe ledger: L-330, L-451, L-452 and L-450 closed (the ledger index moves\nthem to section C on the next orrery run); L-449\'s check recorded as\nseen working, the item open for its cause; L-410\'s rows approved;\nL-231 receives L-330\'s loose end (the website\'s `evenBeltRings()`, for\nJupiter); L-455 records the orrery\'s own typed low-orbit numbers; L-413\nrecords the close. Where We Are: the date, the box, road stage 5, the\nsignals and the details.\n\nTested on a copy of orrery fc2bb6f9 with the patch applied: the\nmaintenance run, results in section 4; the GUI starts headless; the\nlow-orbit traces built at size 2.5 and opacity 1.0; the tooltip prints\n"180 km to 2,000 km".\n\n## 4. Test results\n\n- Orrery maintenance run on the patched copy: 31 of 31 gating\n  checkers passed; the scanner\'s gate line "0 TIER-1 -- the push gate\n  holds", whole tree 280 as before. The ledger index moved L-330,\n  L-450, L-451 and L-452 into section C.\n- The orrery GUI starts headless on a throwaway copy, no errors.\n- Applied clean to fc2bb6f9\'s files, and to a copy with Windows line\n  endings (written back LF, as the patch says). A changed\n  `shell_configs.py` is refused with "BASE MOVED" and nothing written.\n\n## 5. Skill obligations travel\n\nNo skill changed this session after v3.102. The next session confirms\nits loaded copies read provenance-discipline 2.30, interactive-exhibit\n1.17 and gallery-cache-builder 1.11 before work that fires them;\nhorizons-orbital-mechanics 1.8 (v3.99) still travels. This part of the\nsession confirmed orrery-coding-conventions 1.10, agentic-pre-test 1.3\nand ledger-and-session-records 1.21 at load, as the manifest expects.\n\nSession written October 17, 2026 with Anthropic\'s Claude Opus 5.5.\n'}
EDITS = [
    ('earth_visualization_shells.py', 'tooltip from the rows', 'earth_leo_shell_info = (\n            "SET MANUAL SCALE TO 0.003 AU TO VISUALIZE.\\n\\n"\n            "Low Earth Orbit (LEO) is the region from roughly 200 km to 2,000 km altitude\\n"\n            "(1.03 to 1.31 Earth radii), where satellites orbit at all inclinations.\\n\\n"', '# L-452 (2026-10-17): the altitudes read from the same rows as the hover\n# below, so the checkbox tooltip cannot keep an edge the store has moved\n# (it said "roughly 200 km" after the lower edge became ESA\'s row).\nearth_leo_shell_info = (\n            "SET MANUAL SCALE TO 0.003 AU TO VISUALIZE.\\n\\n"\n            f"Low Earth Orbit (LEO) is the region from {row_text(\'EARTH_LEO_LOWER_ALTITUDE_KM\')} km to {exact_text(\'EARTH_LEO_UPPER_ALTITUDE_KM\', grouping=True)} km altitude\\n"\n            f"({EARTH_LEO_INNER_RADII:.2f} to {EARTH_LEO_OUTER_RADII:.2f} Earth radii), where satellites orbit at all inclinations.\\n\\n"'),
    ('earth_visualization_shells.py', 'docstring names the rows', '    LEO spans ~200 km to ~2,000 km altitude (1.03 to 1.31 Earth radii).\n', '    LEO spans the rows EARTH_LEO_LOWER_ALTITUDE_KM (ESA, the lowest height\n    satellites fly) to EARTH_LEO_UPPER_ALTITUDE_KM (IADC) above the surface.\n'),
    ('earth_visualization_shells.py', 'low-orbit dots stronger', "            marker=dict(\n                size=1.5,\n                color='rgb(255, 248, 220)',   # Warm white -- visible satellites\n                opacity=0.35,\n                symbol='circle',\n            ),\n            name='Earth: Low Earth Orbit (LEO)',", "            # L-330 round 1 (Tony's look, 2026-10-17, option A): full\n            # opacity and size 2.5, so the dots show against the inner\n            # belt's, which reach size 3 and full opacity at its peak and\n            # fill the same heights. Was size 1.5 at 35%. A rendering\n            # setting; the warm white keeps its meaning.\n            marker=dict(\n                size=2.5,\n                color='rgb(255, 248, 220)',   # Warm white -- visible satellites\n                opacity=1.0,\n                symbol='circle',\n            ),\n            name='Earth: Low Earth Orbit (LEO)',"),
    ('shell_configs.py', 'unused tooltip twin agrees', '                f"Low Earth Orbit (LEO) is the region from roughly {row_text(\'EARTH_LEO_LOWER_ALTITUDE_KM\', grouping=True)} km to', '                f"Low Earth Orbit (LEO) is the region from {row_text(\'EARTH_LEO_LOWER_ALTITUDE_KM\', grouping=True)} km to'),
    ('LEDGER_CONSOLIDATED.md', 'header stamp', 'L-413 and L-435 updated), built on da78b80 and gallery f49b3e6.\n', "L-413 and L-435 updated), built on da78b80 and gallery f49b3e6.\nModule updated: October 17, 2026 with Anthropic's Claude Opus 5.5\n(Earth's round 1 closed on Tony's runs and looks: L-330, L-451, L-452\nand L-450 closed; L-449's check seen working; L-410's fade rows\napproved; the low-orbit dots made visible against the inner belt and\nthe low-orbit tooltip's 200 km corrected; L-231, L-413 and L-455\nupdated), built on fc2bb6f9 and gallery 44a6225c.\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-455 orrery instance', '  are the ones met, not a sweep.\n**Gap:** a sweep of the served words for typed numbers, then each\nsourced into a row or removed, when the Earth or Sun slice next opens\nthese shells.', '  are the ones met, not a sweep.\n- **Met 2026-10-17 in the orrery\'s own low-orbit hover and tooltip**\n  (`earth_visualization_shells.py`; not served to the website, so the\n  orrery\'s form of this class): the satellite counts (about 11,000\n  active, about 7,000 Starlink, 35,000 tracked debris), the heights of\n  the ISS, Starlink and Hubble, the 90 to 120 minute orbit, and the\n  typed `STARLINK_KM = 6921.0` that places the dots. Their `# Source:`\n  comment names databases, not a read ("Verified: April 2026 via Gemini\n  fact-check"). Same method when the low-orbit shell is next opened.\n**Gap:** a sweep of the served words for typed numbers, then each\nsourced into a row or removed, when the Earth or Sun slice next opens\nthese shells; the orrery\'s low-orbit numbers above with them.'),
    ('LEDGER_CONSOLIDATED.md', 'L-452 meta', '<!-- L:452 status:OPEN upd:2026-10-17 section:A flag: rice: -->', '<!-- L:452 status:DONE upd:2026-10-17 section:C flag: rice: -->'),
    ('LEDGER_CONSOLIDATED.md', 'L-452 close', "**Gap:** Tony's run of patches 2 and 3, a green run, and his look at the\ni panels and the two wordings. Typed numbers met in served words are\nL-455.", '- **Closed 2026-10-17 on Tony\'s runs and look** (his run record,\n  `documentation/WHERE_WE_ARE_10-16-26_2116_run_record.md`, saved again that\n  afternoon): patches 2 and 3 run; the orrery 31 of 31 gating, pushed\n  fc2bb6f9; the Daily Run 29 of 29 gating, pushed 44a6225c; the live\n  check green. The phone look, i panels included: "correct". The three\n  wordings Claude chose: "Approved."\n- **One copy the build missed, found at the close:** the orrery\'s\n  low-orbit checkbox tooltip (`earth_visualization_shells.py`,\n  `earth_leo_shell_info`) and its builder\'s docstring still said\n  "roughly 200 km". The tooltip now reads both edges from the rows the\n  hover reads; the docstring names the rows\n  (`patch_L330_4_leo_contrast_close_20261017.py`).\n- **Loose ends:** the typed numbers met in served words are L-455\n  (open), which now also holds the orrery\'s low-orbit numbers.\n**Gap:** none. Closed.'),
    ('LEDGER_CONSOLIDATED.md', 'L-451 meta', '<!-- L:451 status:OPEN upd:2026-10-17 section:A flag: rice: -->', '<!-- L:451 status:DONE upd:2026-10-17 section:C flag: rice: -->'),
    ('LEDGER_CONSOLIDATED.md', 'L-451 close', "**Gap:** Tony's run of patch 3 and the Daily Run: closes when OPEN is\nempty on his run.", '- **Closed 2026-10-17 on Tony\'s Daily Run** (his run record,\n  `documentation/WHERE_WE_ARE_10-16-26_2116_run_record.md`): "TYPED FACTS: PASS\n  -- 0 typed facts in the Sun and Earth rooms; 17 number line(s), 27 of\n  27 allowed". Pushed 44a6225c. No loose ends.\n**Gap:** none. Closed.'),
    ('LEDGER_CONSOLIDATED.md', 'L-450 meta', '<!-- L:450 status:OPEN upd:2026-10-17 section:A flag: rice: -->', '<!-- L:450 status:DONE upd:2026-10-17 section:C flag: rice: -->'),
    ('LEDGER_CONSOLIDATED.md', 'L-450 close', "**Gap:** Tony's run of patch 2 with a green orrery run, and the export\ncarrying the new citations to the website at the next Daily Run.", '- **Closed 2026-10-17 on Tony\'s runs** (his run record,\n  `documentation/WHERE_WE_ARE_10-16-26_2116_run_record.md`): patch 2 with the orrery\n  31 of 31 gating and 0 Tier-1 on the gate path, pushed fc2bb6f9; the\n  Daily Run\'s pulls carried the export ("PULLS: all 5 passed", the\n  Config mirror among them) and its run was 29 of 29 gating, pushed\n  44a6225c; the live check\'s store drift read orrery fc2bb6f9, 0 DRIFT.\n  No loose ends.\n**Gap:** none. Closed.'),
    ('LEDGER_CONSOLIDATED.md', 'L-449 seen', "**Gap:** Tony's run of patch 1. The check part is then done; the item\nstays open for the CAUSE, read from the `[RUNS]` lines at the next\nloss; then the deliberate limit, its number set then, each removal\nnamed.", '- **The check seen working, 2026-10-17** (Tony\'s Daily Run of 15:59,\n  his run record `documentation/WHERE_WE_ARE_10-16-26_2116_run_record.md`):\n  "[RUNS] before the copy: 86 run records in data\\solar-system\\raw\\runs"\n  and "[RUNS] after the copy:  86 run records in\n  data\\.staging_solar-system_20261017T205940Z\\raw\\runs"; nothing lost,\n  so nothing stopped. Its stop branch is tested by the builder suite\'s\n  planted loss. Pushed 44a6225c.\n**Gap:** the CAUSE, read from the `[RUNS]` lines at the next loss; then\nthe deliberate limit, its number set then, each removal named.'),
    ('LEDGER_CONSOLIDATED.md', 'L-410 rows approved', "**Gap:** Earth's fade built (the sources read in full first, each\nnumber a row); then the Sun's fades,", '- **The fade\'s rows, approved 2026-10-17** (Tony: "read and approved"),\n  after the sources were read in full: seven rows from Zoennchen et al.\n  (2022), Ann. Geophys. 40:271, eqs. 7 to 9 --\n  EARTH_EXOSPHERE_H_FIT_INNER_RADII, _FIT_OUTER_RADII, _FIT_COEFF_CM3,\n  _FIT_OFFSET_RADII, _FIT_EXPONENT, _OUTER_EXPONENT and\n  _AT_10_RADII_CM3. Each row\'s value, quote and locator:\n  `documentation/SOURCES_earth_fade_20261017.md`. Not yet in\n  `constants_new.py`; the fade\'s build writes them.\n**Gap:** Earth\'s fade built from those rows; then the Sun\'s fades,'),
    ('LEDGER_CONSOLIDATED.md', 'L-231 meta', '<!-- L:231 status:OPEN upd:2026-09-16 section:A flag: rice:2/2/90/2 -->', '<!-- L:231 status:OPEN upd:2026-10-17 section:A flag: rice:2/2/90/2 -->'),
    ('LEDGER_CONSOLIDATED.md', 'L-231 from L-330', 'reworded, both code comments corrected, one pass, then Mode 5 -- done for\nEarth.)\n', "reworded, both code comments corrected, one pass, then Mode 5 -- done for\nEarth.) From L-330's close (2026-10-17): the website keeps\n`evenBeltRings()` for a body with served belt edges and no stored\ndrawing, and the orrery removed its copy; re-read it when Jupiter's\nbelts get edge rows.\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-330 meta', '<!-- L:330 status:OPEN upd:2026-10-17 section:A flag: rice:3/3/60/3 -->', '<!-- L:330 status:DONE upd:2026-10-17 section:C flag: rice:3/3/60/3 -->'),
    ('LEDGER_CONSOLIDATED.md', 'L-330 close', "**Gap:** Tony's look in both instruments, after his runs: the orrery\nplot (Mode 5) and the Earth room on the phone. Closes then.", '- **Closed 2026-10-17 on Tony\'s looks** (his run record,\n  `documentation/WHERE_WE_ARE_10-16-26_2116_run_record.md`, saved again that\n  afternoon): the orrery plot, "looks good except that the color\n  contrast between the lower belt and the LEO is not enough to see LEO\n  dots"; the Earth room on the phone, "correct". Runs green: the orrery\n  31 of 31 gating, pushed fc2bb6f9; the Daily Run 29 of 29 gating with\n  Drawings 7 of 7, pushed 44a6225c; the live check green.\n- **The low-orbit dots, found at that look.** The inner belt\'s dots now\n  reach size 3 and full opacity and fill the same heights, so the\n  low-orbit dots (size 1.5 at 35%) were lost among them; the website\n  draws low orbit as two edge shells and was not affected. Tony chose\n  option A of three ("A. As recommended"): full opacity and size 2.5,\n  the warm white kept. A throwaway render set size 2.5 and size 3\n  against the belt; 3 crowded it. Built in\n  `patch_L330_4_leo_contrast_close_20261017.py`; Tony\'s next orrery\n  plot is the look, carried on L-413.\n- **Loose ends:** the website\'s `evenBeltRings()` note went to L-231\'s\n  Gap (Jupiter\'s half), which opens those rows.\n**Gap:** none. Closed.'),
    ('LEDGER_CONSOLIDATED.md', 'L-413 round 1 closed', "**Gap:** Tony's runs and looks close L-330, L-451, L-452 and L-450;\nthen Earth's fade built (L-410) or talk 2 (L-356 with L-375, and\nL-454), Tony's choice which first;", "- **2026-10-17, round 1 closed** on Tony's runs and looks: L-330,\n  L-451, L-452 and L-450 closed; L-449's check seen working, open for\n  its cause; Earth's fade rows approved (L-410). His orrery look found\n  the low-orbit dots lost against the inner belt: option A built in\n  `patch_L330_4_leo_contrast_close_20261017.py`.\n**Gap:** Tony's look at the low-orbit dots in his next orrery plot\n(Mode 5); then Earth's fade built (L-410) or talk 2 (L-356 with L-375,\nand L-454), Tony's choice which first;"),
    ('documentation/WHERE_WE_ARE.md', 'date and box', "Last updated: October 17, 2026, afternoon: Earth's round-1 build done.\n- Written at orrery da78b80 and gallery f49b3e6.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - Belts as random dots along the field lines; your approved words;\n>   a lost run record stops the Daily Run. Three patches, waiting.\n> - Fades only where nature thins out; Earth's hydrogen fade designed\n>   (L-410, the fades).\n>\n> **Do next:** *Your run order, section 1 of\n> HANDOFF_earth_round1_build_20261017.md.*\n>\n> **Needs you now:**\n> - *Patches 1, 2, the close, the orrery run, push; reinstall three\n>   skills; patch 3, the Daily Run, push; then the two looks.*\n> - At the phone look, three wordings Claude chose (handoff, sec. 4);\n>   then: Earth's fade built first, or talk 2?", "Last updated: October 17, 2026, evening: Earth's round 1 closed.\n- Written at orrery fc2bb6f and gallery 44a6225.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - Round 1 is live and closed: the belts, your words, the citations,\n>   the run-records check. Four items closed on your runs and looks.\n> - The low-orbit dots are brighter and larger, so the inner belt no\n>   longer hides them (your option A). The tooltip says 180 km.\n> - The seven fade rows are approved (L-410, the fades).\n>\n> **Do next:** *Run patch_L330_4_leo_contrast_close_20261017.py, then\n> the orrery run; plot Earth and look at the low-orbit dots; push.*\n>\n> **Needs you now:**\n> - *After that look: Earth's fade built first, or talk 2?*"),
    ('documentation/WHERE_WE_ARE.md', 'road stage 5', "  5.   [NOW]   *Earth's list (L-413): round 1 built, waiting on your\n               runs and looks; then Earth's fade or talk 2.* << moved this session", "  5.   [NOW]   *Earth's list (L-413): round 1 closed; the low-orbit\n               look; then Earth's fade or talk 2.* << moved this session"),
    ('documentation/WHERE_WE_ARE.md', 'signals', '- Last cache build: 20261017T131445Z, ok, every rename on the first try (gallery f49b3e6).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, da78b80).', '- Last cache build: 20261017T205940Z, ok, every rename on the first try (gallery 44a6225).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, fc2bb6f).'),
    ('documentation/WHERE_WE_ARE.md', 'details next', '- *Next: `HANDOFF_earth_round1_build_20261017.md` (your run order)*', "- *Next: `HANDOFF_earth_round1_close_20261017.md` (your run order)*\n- Round 1's build: `HANDOFF_earth_round1_build_20261017.md`; the fade's\n  sources and rows: `SOURCES_earth_fade_20261017.md`"),
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
    print("NEXT (section 1 of documentation/HANDOFF_earth_round1_close_20261017.md):")
    print("  1. Run orrery_maintenance_run.py (dashboard). Its ledger index")
    print("     moves L-330, L-450, L-451 and L-452 to the closed section.")
    print("  2. Plot Earth with the magnetosphere and low Earth orbit on;")
    print("     look at the low-orbit dots against the inner belt.")
    print("  3. Move this script into documentation/; commit; push.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
