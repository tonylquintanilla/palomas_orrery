#!/usr/bin/env python3
"""
patch_L445_3_close_20261016.py -- closes L-445 (Earth's period from the
Earth-Moon barycentre) and L-448 (the test file in the tracked tree) on
Tony's run and look, and carries one note to safe-file-editing's next
version on L-351.

Tony, 2026-10-16: "yes, the hover is correct and we can close."

Built on orrery a66fd679d3844064b240f40097fbe057011bb8df at
https://github.com/tonylquintanilla/palomas_orrery ("L446 close"). The
gallery is not touched (0f8efb17 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 16, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L445_3_close_20261016.py

    Save this file in the ORRERY folder above, open it in VS Code and
    click Run. It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing, in two files, each edited only at the
lines it changes, so your notes elsewhere are kept:

    LEDGER_CONSOLIDATED.md   L-445 and L-448 to DONE, quoting your run
                             record of 2026-10-15 (the copy you uploaded
                             on 2026-10-16); L-351 carries the folder-
                             removal note; header stamp
    documentation/WHERE_WE_ARE.md
                             above the run-record marker only: the date,
                             the box, road stages 5 and 8-8b, a signal,
                             the details

    It does not touch your run-record copy, which goes up with your push.

WHAT IT PRINTS

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = 'a66fd67'
ZONES = {}
MARKERS = {'documentation/WHERE_WE_ARE.md': '--- Your run record below this line'}
FINGERPRINTS = {}
RESULTS = {}
DELETES = {}
NEW_FILES = {}
EDITS = [('LEDGER_CONSOLIDATED.md', 'line 466: Module updated: October 16, 2026 with Anthropi', 'done), built on 3cedfb7 and gallery 0f8efb1.\nReview and RICE update Tony 6-21-2026\n', "done), built on 3cedfb7 and gallery 0f8efb1.\nModule updated: October 16, 2026 with Anthropic's Claude Opus 5.5\n(L-445 and L-448 closed on Tony's run and look; a note carried to\nsafe-file-editing's next version on L-351), built on a66fd67 and\ngallery 0f8efb1.\nReview and RICE update Tony 6-21-2026\n"), ('LEDGER_CONSOLIDATED.md', 'line 1255: <!-- L:448 status:DONE upd:2026-10-16 section:', '#### [L-448] The maintenance run writes a test file into the tracked tree (orrery, maintenance)\n<!-- L:448 status:OPEN upd:2026-10-15 section:A flag: rice: -->\n- **Seen by Tony, 2026-10-15,** pushing L-447\'s records: "test_orbit_paths.json\n', '#### [L-448] The maintenance run writes a test file into the tracked tree (orrery, maintenance)\n<!-- L:448 status:DONE upd:2026-10-16 section:C flag: rice: -->\n- **Seen by Tony, 2026-10-15,** pushing L-447\'s records: "test_orbit_paths.json\n'), ('LEDGER_CONSOLIDATED.md', "line 1276: - **Closed 2026-10-16 on Tony's run,** read fr", "  FILES WRITTEN no longer names it.\n**Gap:** Tony's commit of the deletion (patch_L445_1); then DONE.\n**Ref:** `test_orbit_cache.py`; `.gitignore`; L-447.\n\n", '  FILES WRITTEN no longer names it.\n- **Closed 2026-10-16 on Tony\'s run,** read from his record\n  `documentation/WHERE_WE_ARE_10-15-26_2236_run_record.md` (the copy he uploaded on 2026-10-16). His\n  first maintenance run after patch_L445_1 printed "Orbit cache ... All 6\n  orbit cache tests passed: cache loads, old formats convert, corrupted\n  entries are dropped; nothing left behind."; the deletion went up in\n  his push at 54c27d7. Every run since says the same.\n- **The patch crashed on its last step, and nothing was lost.**\n  patch_L445_1 deleted the file, then tried to remove the emptied\n  `test_output` folder; Windows refused (`PermissionError: [WinError 5]\n  Access is denied`), most likely OneDrive holding the folder it had\n  just seen emptied. Every write had landed before the refusal:\n  compared byte for byte with the build the same night. The traceback\n  hid the patch\'s "ok" lines. The empty folder is ignored by git and by\n  `.gitignore`; Tony deletes it by hand when he likes.\n- **Loose ends, re-homed or struck:**\n  - A patch that removes a folder treats a refused removal as a note:\n    carried to safe-file-editing\'s next version on L-351 (rules owed to\n    the next bumps of their stores).\n**Gap:** none. Closed 2026-10-16.\n**Ref:** `test_orbit_cache.py`; `.gitignore`; L-447; L-351.\n\n'), ('LEDGER_CONSOLIDATED.md', 'line 1280: <!-- L:445 status:DONE upd:2026-10-16 section:', "#### [L-445] Earth's orbital period from the Earth-Moon barycentre, not Earth's centre (orrery + website, periods)\n<!-- L:445 status:OPEN upd:2026-10-15 section:A flag: rice: -->\n- **Found 2026-10-15, on L-444's first live run.** JPL's period for\n", "#### [L-445] Earth's orbital period from the Earth-Moon barycentre, not Earth's centre (orrery + website, periods)\n<!-- L:445 status:DONE upd:2026-10-16 section:C flag: rice: -->\n- **Found 2026-10-15, on L-444's first live run.** JPL's period for\n"), ('LEDGER_CONSOLIDATED.md', "line 1338: - **Closed 2026-10-16 on Tony's run and look,*", "  horizons-orbital-mechanics 1.8, protocol v3.99.\n**Gap:** Tony's live run (the Period fetch row names Earth; the\nHorizons check compares the new record with JPL the same run); his\nlook at Earth's hover in the orrery and the words; the gallery patch,\nits run and the website look after the next Daily Run. L-448 rides.\n**Ref:** L-444; L-431; `orbital_period.py`; `period_fetch.py`;\n", '  horizons-orbital-mechanics 1.8, protocol v3.99.\n- **Closed 2026-10-16 on Tony\'s run and look,** read from his record\n  `documentation/WHERE_WE_ARE_10-15-26_2236_run_record.md` (the copy he uploaded on 2026-10-16). Each\n  proof the brief asked for, as his run printed it:\n  - patch_L445_1 wrote every file and then stopped on the empty\n    folder\'s removal (L-448); every file was compared byte for byte\n    with the build the same night.\n  - `orrery_maintenance_run.py`: "Period fetch ... rewrote\n    data/osculating_cache.json -- PASS -- fetched 1: Earth; elements\n    refreshed for: Earth"; "Horizons check ... rewrote\n    data/horizons_confirmations.json -- PASS -- 1 checked today, 1\n    queries"; "Period fetch suite ... pass -- 36 checks, every planted\n    fault caught (20 planted, 8 of them for Earth\'s period, L-445)".\n    The one red row, Dashboard parity, named L-446\'s two new website\n    steps with no button yet; L-446\'s orrery patch added them (31 of 31\n    at 3cedfb7). Pushed at 54c27d7.\n  - The words in the orrery, "For the Earth-Moon center of mass, around\n    the Sun, from JPL Horizons, fetched <date>.": Tony, "-- correct".\n  - patch_L445_2 applied (9 edits in 2 files); the gallery\'s offline\n    run, "28 of 28 gating checkers passed"; pushed at 0f8efb1; the live\n    run, "Export freshness -- the served export is the orrery\'s at\n    54c27d7f, byte for byte".\n  - The website look, Earth\'s hover in the Solar System and Earth rooms\n    (asked 2026-10-16): Tony, "-- correct", and "yes, the hover is\n    correct and we can close."\n- **Loose ends, re-homed or struck:**\n  - The look at the website, received from L-444: done above.\n  - The skill obligation: horizons-orbital-mechanics 1.8 travels. Tony\n    reinstalled it on 2026-10-15; the session that built and closed\n    this item loaded 1.7 and cannot read the new copy. The next session\n    whose work fires the skill confirms its loaded copy reads 1.8.\n  - Struck, unreachable today: if Earth\'s period were ever taken around\n    the solar system\'s barycentre, the website\'s cache builder would\n    fetch the drawn orbit for Earth\'s own id (399) around it. The\n    two-centre test keeps the Sun (0.0039 days of change in a year\n    against 2.52, `documentation/worksheets/period_answers_L445.json`),\n    and the orrery\'s drawing already refuses the barycentre\'s elements\n    for Earth (tested).\n  - L-448 (the test file): closed with this item.\n**Gap:** none. Closed 2026-10-16.\n**Ref:** L-444; L-431; `orbital_period.py`; `period_fetch.py`;\n'), ('LEDGER_CONSOLIDATED.md', 'line 3751: <!-- L:351 status:OPEN upd:2026-10-16 section:', '#### [L-351] Rules learned at C2, owed to the next bumps of their stores (skills, protocol)\n<!-- L:351 status:OPEN upd:2026-10-11 section:A flag: rice: -->\n- **Recorded, not built.** A class found while building L-322 Stage C2\n', '#### [L-351] Rules learned at C2, owed to the next bumps of their stores (skills, protocol)\n<!-- L:351 status:OPEN upd:2026-10-16 section:A flag: rice: -->\n- **Recorded, not built.** A class found while building L-322 Stage C2\n'), ('LEDGER_CONSOLIDATED.md', 'line 3864: - **2026-10-16, safe-file-editing, next bump (', "      way.\n**Gap:** Each lands with its store's next bump.\n", '      way.\n  - **2026-10-16, safe-file-editing, next bump (L-448):** a patch that\n    removes a folder it has just emptied treats a refusal as a note,\n    never a crash. On Windows under OneDrive, patch_L445_1\'s\n    `os.rmdir` raised WinError 5 after every write had landed, so the\n    run showed a traceback instead of its "ok" lines and read as a\n    failure. The skill says nothing wrong today; it does not cover\n    this, so it is carried here, not bumped.\n**Gap:** Each lands with its store\'s next bump.\n'), ('documentation/WHERE_WE_ARE.md', 'line 4: Last updated: October 16, 2026, morning: L-445', "\nLast updated: October 16, 2026, morning: L-446 (the Daily Run's order) closed.\n- Written at orrery 3cedfb7 and gallery 0f8efb1.\n\n", "\nLast updated: October 16, 2026, morning: L-445 (Earth's period) closed.\n- Written at orrery a66fd67 and gallery 0f8efb1.\n\n"), ('documentation/WHERE_WE_ARE.md', "line 10: > - L-445 (Earth's period) closed: the Earth-M", "> **Changed since you last read this:**\n> - L-445 (Earth's period) built: the Earth-Moon barycentre's period,\n>   1.00000 years (365.25 days); L-448 (the test file) rode it.\n> - L-446 (the Daily Run's order) closed: the pulls ran before the build,\n>   28 of 28 checks passed, the live site serves the orrery's export.\n>\n> **Do next:** *The L-445 (Earth's period) close, in its own session.*\n>\n", '> **Changed since you last read this:**\n> - L-445 (Earth\'s period) closed: the Earth-Moon barycentre\'s period,\n>   in the orrery and on the website, your "correct" on both.\n> - L-448 (the test file) closed: the tests leave nothing in the repo.\n>\n> **Do next:** *Earth\'s list goes on: the rest of L-421\'s checks (the\n> typed facts, stage 6).*\n>\n'), ('documentation/WHERE_WE_ARE.md', 'line 18: > - *Run patch_L445_3, then the orrery mainten', '> **Needs you now:**\n> - *Run patch_L446_4, then the orrery maintenance run; push.*\n\n', '> **Needs you now:**\n> - *Run patch_L445_3, then the orrery maintenance run; push.*\n\n'), ('documentation/WHERE_WE_ARE.md', "line 26: 5.   [NOW]   *Earth's list (L-413): the rest o", "               feeds the website and nothing is typed twice.\n  5.   [NOW]   *Earth's list (L-413): L-445 (Earth's period, stage 8b),\n               then the rest of L-421's checks (stage 6), then Earth's\n               design talks.*\n  5b.  [NOW]   The scaffolding checks clear beside the slices: the\n", "               feeds the website and nothing is typed twice.\n  5.   [NOW]   *Earth's list (L-413): the rest of L-421's checks (stage\n               6), then Earth's design talks.* << moved this session\n  5b.  [NOW]   The scaffolding checks clear beside the slices: the\n"), ('documentation/WHERE_WE_ARE.md', 'line 36: 8-8b.[done]  The served objects are checked ag', "               System room's features close with these rooms.\n  8-8a.[done]  The served objects are checked against JPL from the\n               orrery's run, missing periods fetched first (Oct 14, 15).\n  8b.  [NOW]   *L-445 (Earth's period): built; your look at the hover next.*\n  8c.  [done]  L-446 (the Daily Run's order): pulls before the build (Oct 16).\n", "               System room's features close with these rooms.\n  8-8b.[done]  The served objects are checked against JPL from the\n               orrery's run, missing periods fetched first; Earth's from\n               the Earth-Moon barycentre (Oct 14-16). << moved this session\n  8c.  [done]  L-446 (the Daily Run's order): pulls before the build (Oct 16).\n"), ('documentation/WHERE_WE_ARE.md', 'line 95: - Tier-1 on the gate path: 0, by name (PROVENA', '- Last cache build: 20261016T043242Z, ok, one retry absorbed (gallery 0f8efb1).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 3cedfb7).\n  Whole tree: 280: orrery 116, Earth System 149, stars 13, utilities 2.\n', '- Last cache build: 20261016T043242Z, ok, one retry absorbed (gallery 0f8efb1).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, a66fd67).\n  Whole tree: 280: orrery 116, Earth System 149, stars 13, utilities 2.\n'), ('documentation/WHERE_WE_ARE.md', 'line 120: - *Next: L-421 (the typed facts) in the ledger', '- Every item: `LEDGER_CONSOLIDATED.md`.\n- *Now: `HANDOFF_L445_earth_period_build_20261015.md`, its close next*\n- L-446, closed: `HANDOFF_L446_daily_run_order_build_20261015.md`\n- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;\n', '- Every item: `LEDGER_CONSOLIDATED.md`.\n- *Next: L-421 (the typed facts) in the ledger, its remaining checks*\n- Closed: L-445 `HANDOFF_L445_earth_period_build_20261015.md`; L-446\n  `HANDOFF_L446_daily_run_order_build_20261015.md`\n- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;\n')]


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
    print("patch applied (%d new files, %d edits in %d files, %d deleted)"
          % (len(NEW_FILES), len(EDITS), len(texts), len(DELETES)))
    print("")
    print("NEXT:")
    print('  1. Run orrery_maintenance_run.py: its ledger index moves L-445 and')
    print('     L-448 into the closed section.')
    print('  2. Move this script into documentation/; commit; push.')
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
