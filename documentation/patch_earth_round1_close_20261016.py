#!/usr/bin/env python3
"""
patch_earth_round1_close_20261016.py -- the close of Earth's design
talk, round 1 (zero code). Records Tony's rulings on L-330 (the belts'
shape), L-451 (the eight held sentences), L-452 with L-450 (the notes
beside a citation), L-449 (the run records) and L-314 (the aberration),
and L-413's progress; updates Where We Are.

Built on orrery 48c84c34910df9ce128c85a35a4c0f015172903b at
https://github.com/tonylquintanilla/palomas_orrery ("Update
WHERE_WE_ARE_10-16-26_1708_run_record.md"). The gallery is not touched
(2090a8b at https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 16, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_earth_round1_close_20261016.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing, in two files, each edited only at the
lines it changes, so your notes elsewhere are kept:

    LEDGER_CONSOLIDATED.md   the rulings onto L-330 (retitled), L-451,
                             L-452, L-450, L-449, L-314 and L-413;
                             header stamp
    documentation/WHERE_WE_ARE.md
                             above the run-record marker only: the date,
                             the box, road stage 5, Settled, a signal,
                             Waiting on you, the details

    The two new records are already in documentation/ beside it:
    DESIGN_earth_round1_rulings_20261016.md and
    HANDOFF_earth_round1_build_brief_20261016.md. Your run-record copy
    WHERE_WE_ARE_10-16-26_2116_run_record.md goes up with your push too.

WHAT IT PRINTS

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = '48c84c3'
ZONES = {}
MARKERS = {'documentation/WHERE_WE_ARE.md': '--- Your run record below this line'}
FINGERPRINTS = {}
RESULTS = {}
DELETES = {}
NEW_FILES = {}
EDITS = [('LEDGER_CONSOLIDATED.md', 'line 473: header stamp', 'interactive-exhibit 1.16, protocol v3.101), built on 6b97515 and\ngallery 2090a8b.\nReview and RICE update Tony 6-21-2026\n', "interactive-exhibit 1.16, protocol v3.101), built on 6b97515 and\ngallery 2090a8b.\nModule updated: October 16, 2026 with Anthropic's Claude Opus 5.5\n(Earth's design talk, round 1, zero code: rulings onto L-330, L-451,\nL-452, L-450, L-449, L-314 and L-413; the build brief written), built\non 48c84c3 and gallery 2090a8b.\nReview and RICE update Tony 6-21-2026\n"), ('LEDGER_CONSOLIDATED.md', 'line 1229: L-452 ruled', "#### [L-452] The website's notes beside a citation: read them again now that the citation prints above them (gallery, words)\n<!-- L:452 status:OPEN upd:2026-10-16 section:A flag: rice: -->", '#### [L-452] The website\'s notes beside a citation: read them again now that the citation prints above them (gallery, words)\n<!-- L:452 status:OPEN upd:2026-10-16 section:A flag: rice: -->\n- **Ruled 2026-10-16 at Earth\'s design talk, round 1** (a rule, not 35\n  rulings). Tony: "Wording that is relevant to the citation should be\n  moved to the store.  Notes should be dropped unless they are drawing\n  choices." So: wording that bears on a citation moves to its row in\n  `constants_new.py` (`# Source:` when it is part of the citation,\n  other comment lines otherwise); a `source_note` stays only when it\n  describes a drawing choice; every other note is dropped. Stricter\n  than the option put to him, which kept a note saying what the number\n  is for. Claude\'s reading, said in the talk and not contradicted: the\n  Crust\'s served `note` is a drawing choice and stays, without "(Tony,\n  2026-09-28)". The edited words go to Tony before they ship. Method,\n  so interactive-exhibit\'s next version carries it. Record:\n  `documentation/DESIGN_earth_round1_rulings_20261016.md`.'), ('LEDGER_CONSOLIDATED.md', 'line 1245: L-452 gap', "**Gap:** read the 35 notes against their citations; strike a repeat,\nkeep a locator, word each for the visitor; take the attribution out of\nthe Crust's note. Words go to Tony before they ship. Through the store\nwriter, in a session that opens the rooms' words.\n", "**Gap:** the build, `documentation/HANDOFF_earth_round1_build_brief_20261016.md`:\nthe moved wording in the orrery's rows (patch 2, with L-450), the notes\nremoved and the Crust's attribution taken out through the store writer\n(patch 3); the list to Tony before either ships.\n"), ('LEDGER_CONSOLIDATED.md', 'line 1252: L-451 ruled', '#### [L-451] The sentences the Typed facts check holds open (gallery, words)\n<!-- L:451 status:OPEN upd:2026-10-16 section:A flag: rice: -->', '#### [L-451] The sentences the Typed facts check holds open (gallery, words)\n<!-- L:451 status:OPEN upd:2026-10-16 section:A flag: rice: -->\n- **Ruled 2026-10-16 at Earth\'s design talk, round 1.** Tony,\n  "Confirmed as recommended": SERVE 1 to 5, each with its rows\'\n  source; ALLOW 6 (about the picture); REWORD 7 to "Where that is so,\n  the text beside it says so." and ALLOW it (how to use the page; "Nobody\n  has measured those" was a claim about the world with no source); CUT\n  8 (curved belts no longer "sit in" the plane, L-330; the belts\'\n  served `hovers_plane` already says the plane and its daily average,\n  read at gallery 2090a8b). Record:\n  `documentation/DESIGN_earth_round1_rulings_20261016.md`.'), ('LEDGER_CONSOLIDATED.md', 'line 1281: L-451 gap', "**Gap:** (decide) Tony's ruling on each, at a design talk; then the\nbuild moves each off the OPEN list, which the check prints until it is\nempty.\n", "**Gap:** the build moves each as ruled (patch 3 of\n`documentation/HANDOFF_earth_round1_build_brief_20261016.md`); closes\nwhen the check's OPEN list is empty on Tony's run.\n"), ('LEDGER_CONSOLIDATED.md', 'line 1308: L-450 rides', "**Gap:** each row's `# Source:` names the work and its locator, with\nstore notes moved to the row's other comment lines; the IADC edition\nchecked against the document read. One class; the rows are named\nabove. When `constants_new.py`'s Earth and Sun rows are next opened\n(road stage 7, the Sun's numbers get Earth's checking).\n", "- **2026-10-16, rides Earth's round-1 build** (the brief said so; L-452's\n  ruling of the same day moves the website notes' citation wording into\n  these same rows, so both are done in one pass through\n  `constants_new.py`, patch 2 of\n  `documentation/HANDOFF_earth_round1_build_brief_20261016.md`).\n**Gap:** each row's `# Source:` names the work and its locator, with\nstore notes moved to the row's other comment lines; the IADC edition\nchecked against the document read. One class; the rows are named\nabove. In Earth's round-1 build, with L-452; the list to Tony first.\n"), ('LEDGER_CONSOLIDATED.md', 'line 1359: L-449 ruled', "**Gap:** (decide) keep the run records, or a rule for how many the\nbuilder keeps. Then: the cause, which has now recurred, with the swap's\nfirst-try rename ruling out the retry; the check above, a shrink check\nfor the run records beside the point-count one.\n", '- **Ruled 2026-10-16 at Earth\'s design talk, round 1.** Tony: "For the\n  purpose of explanation, confirmed. Otherwise what is gained by\n  storing?" Answered: very little; nothing reads them and git keeps each\n  one, since every Daily Run\'s push commits that night\'s record. Then,\n  to keeping every record until the cause is found and then a\n  deliberate limit, its number set then, each removal named: "Yes".\n**Gap:** the build, patch 1 of\n`documentation/HANDOFF_earth_round1_build_brief_20261016.md`: the\nbuilder prints what its copy step carried; the Daily Run compares\n`raw/runs/` with `data/solar-system.prev/` after the builder and stops,\nnaming each lost record, before the maintenance run. (decide) at the\nbuild\'s start: stop and name, or put back from `.prev` and say so.\nThen the cause, from those prints on the next loss; then the limit.\n'), ('LEDGER_CONSOLIDATED.md', 'line 9313: L-314 aberration ruled', "  **Tony-action (decide):** apply it, or draw un-aberrated and say so\n  in the hover. Here because the angle follows the solar wind's speed.\n", '  **Tony-action (decide):** apply it, or draw un-aberrated and say so\n  in the hover. Here because the angle follows the solar wind\'s speed.\n- **Aberration ruled 2026-10-16 at Earth\'s design talk, round 1.**\n  Tony: "Unturned until we can design the solar wind fetch". Both\n  instruments keep the magnetopause and bow shock along the Sun-Earth\n  line; each hover gains one served sentence saying so (the real nose\n  turns a few degrees toward Earth\'s motion, depending on the solar\n  wind\'s speed), sourced to the Shue and Jelinek rows, no typed number.\n  Declined: applying it from `EARTH_SOLAR_WIND_SPEED_KM_S` (400 km/s,\n  whose row says its reason is NOT YET WRITTEN; Tony asked "What\'s the\n  source of 400, the mean?" and there is none); sourcing a typical\n  speed first. Asked in the talk and answered from the code: no\n  instrument turns any planet\'s magnetosphere for the aberration;\n  Neptune\'s turn is its field\'s 47 degree tilt and offset. Record:\n  `documentation/DESIGN_earth_round1_rulings_20261016.md`; the\n  sentence rides `documentation/HANDOFF_earth_round1_build_brief_20261016.md`.\n'), ('LEDGER_CONSOLIDATED.md', 'line 9315: L-314 gap', "**Gap:** the whole item, now that L-305 has closed (2026-10-04); and\nthe aberration decision above. On Earth's list (L-413), design talks.\n", "**Gap:** the whole item, now that L-305 has closed (2026-10-04); the\naberration is applied when the fetch is designed (ruled 2026-10-16).\nOn Earth's list (L-413), design talks.\n"), ('LEDGER_CONSOLIDATED.md', 'line 9232: L-314 date', '<!-- L:314 status:OPEN upd:2026-10-04 section:A flag: rice:3/3/60/4 -->', '<!-- L:314 status:OPEN upd:2026-10-16 section:A flag: rice:3/3/60/4 -->'), ('LEDGER_CONSOLIDATED.md', 'line 1899: L-413 talk 1 held', "- **2026-10-16:** L-445 (Earth's period) closed; L-421's checks built\n  and closed on Tony's runs and look. Left on this list: the design\n  talks, in the order above.\n**Gap:** the design talks in the order above, L-330 (the belts' shape)\nfirst; L-451 (the sentences the Typed facts check holds open) joins\nthe first talk that opens those rooms' words.\n", "- **2026-10-16:** L-445 (Earth's period) closed; L-421's checks built\n  and closed on Tony's runs and look. Left on this list: the design\n  talks, in the order above.\n- **2026-10-16, design talk 1 held** (zero code): L-330 ruled to a\n  throwaway render, both belts curved as a density field, regular\n  against random dots; L-451, L-452 with L-450, and L-449 ruled; and\n  talk 4's aberration taken early (L-314: unturned, said in the hover).\n  `documentation/DESIGN_earth_round1_rulings_20261016.md`; the build:\n  `documentation/HANDOFF_earth_round1_build_brief_20261016.md`.\n**Gap:** the round-1 build; then talks 2 to 6 in the order above, next\nL-356 with L-375 (which also carries the South Atlantic Anomaly: the\ncurved belts, drawn centred, cannot show it). Talk 4 (L-314) keeps the\nsolar-wind fetch; its aberration is ruled.\n"), ('LEDGER_CONSOLIDATED.md', 'line 4096: L-330 header', '#### [L-330] Belt shape: rings at the peaks, not the served region (Earth exhibit)\n<!-- L:330 status:OPEN upd:2026-10-04 section:A flag: rice:3/3/60/3 -->', '#### [L-330] Belt shape: the belts curved along the field lines, a density field (Earth exhibit)\n<!-- L:330 status:OPEN upd:2026-10-16 section:A flag: rice:3/3/60/3 -->'), ('LEDGER_CONSOLIDATED.md', 'line 4136: L-330 ruled', "- **2026-10-04:** L-231 is built for Earth (its Gap now holds only\n  Jupiter's belts), so this item's prerequisite is met. First of\n  Earth's design talks (L-413).\n**Gap:** a design round, then a decision, then both instruments in one\npass.\n", '- **2026-10-04:** L-231 is built for Earth (its Gap now holds only\n  Jupiter\'s belts), so this item\'s prerequisite is met. First of\n  Earth\'s design talks (L-413).\n- **2026-10-16, read at HEAD before the design talk:** the "gap" bullet\n  above is out of date. Since L-322 Stage D (orrery D8 and D9,\n  2026-09-25; gallery patch 3, 2026-09-26) both instruments draw each\n  belt as evenly spaced flat rings from its served inner edge to its\n  served outer edge, peak ring brighter; the typed 0.5 and the "Band\n  thickness" line are gone from both [verified @48c84c3 and gallery\n  2090a8b]. The question left was the belts\' curve. Also corrected in\n  the talk: drawn centred on the spin axis, the dipole shape does not\n  show the South Atlantic Anomaly; that needs the field\'s offset\n  (L-375).\n- **Ruled 2026-10-16 at Earth\'s design talk, round 1.** Tony: "Let\'s\n  start with A and see where we take it." Then, on the peak: "Thought:\n  what about a density field similar to the sun\'s streamer belt?"; and\n  on the comparison: "Wait I thought the comparison was a formula and\n  the random scatter." So a THROWAWAY RENDER in the orrery draws both\n  belts curved along dipole field lines (option A) as a density field,\n  two ways side by side: dots on a regular pattern thinning by a\n  formula, and dots scattered at random (which brings L-434\'s stored\n  drawing if chosen). Thickest at the peak in the equator; the fade is\n  a drawing choice the hover states. Tony\'s look decides regular or\n  random, and whether the inner belt reads or falls back to C (inner\n  flat, outer curved). Declined: the flat bands, B (an unmeasured tube\n  height), and rings along the field lines. Record:\n  `documentation/DESIGN_earth_round1_rulings_20261016.md`.\n**Gap:** the build,\n`documentation/HANDOFF_earth_round1_build_brief_20261016.md`: the\nrender and Tony\'s look, then both instruments (orrery patch 2, gallery\npatch 3), the dipole relation\'s source read before it is drawn; closes\non Tony\'s look in both.\n'), ('documentation/WHERE_WE_ARE.md', 'line 4: date', 'Last updated: October 16, 2026, evening: L-421 (the typed facts) closed.\n- Written at orrery 6b97515 and gallery 2090a8b.\n', "Last updated: October 16, 2026, night: Earth's design talk 1 held.\n- Written at orrery 48c84c3 and gallery 2090a8b.\n"), ('documentation/WHERE_WE_ARE.md', 'line 9: box', '> **Changed since you last read this:**\n> - L-421 (the typed facts) closed: the website\'s citations are the\n>   orrery\'s, word for word; a new check catches a fact typed in code.\n> - L-262 (the framing test) closed; the website\'s checks go to item 3.\n> - Grey type is blue; Earth\'s inner shells say "Radius:" (L-453).\n>\n> **Do next:** *Earth\'s design talks, the belts\' shape first (L-330).*\n>\n> **Needs you now:**\n> - *Run patch_L421_11, the orrery run, push; reinstall interactive-exhibit 1.16.*\n', "> **Changed since you last read this:**\n> - Earth's first design talk: the belts go curved, as a density field;\n>   a render first, regular against random dots (L-330).\n> - Also ruled: five held sentences served (L-451); notes only for\n>   drawing choices (L-452); every run record kept for now (L-449); the\n>   magnetosphere unturned, and its hover says so (L-314).\n>\n> **Do next:** *The round-1 build: the run-records check, the belts' render.*\n>\n> **Needs you now:**\n> - *Run patch_earth_round1_close, the orrery run, push.*\n"), ('documentation/WHERE_WE_ARE.md', 'line 26: road 5', "  5.   [NOW]   *Earth's list (L-413): the design talks, the belts'\n               shape first (L-330).* << moved this session\n", "  5.   [NOW]   *Earth's list (L-413): talk 1 held; its build next,\n               then talks 2 to 6.* << moved this session\n"), ('documentation/WHERE_WE_ARE.md', 'line 30: road 6 mark', '  6-6a.[done]  The typed facts, served and checked (Oct 16) << moved this session;\n', '  6-6a.[done]  The typed facts, served and checked (Oct 16);\n'), ('documentation/WHERE_WE_ARE.md', 'line 38: road 9 mark', '               next, item 3, L-357 (stale leftovers). << moved this session\n', '               next, item 3, L-357 (stale leftovers).\n'), ('documentation/WHERE_WE_ARE.md', 'line 87: settled', "- A served number's citation is the orrery's, word for word; the\n  website's words about it are its note (option A). Grey type is blue. (Oct 16)\n", "- A served number's citation is the orrery's, word for word, its wording\n  in the store; the website's note only for a drawing choice. Grey type\n  is blue. All run records kept for now; magnetosphere unturned. (Oct 16)\n"), ('documentation/WHERE_WE_ARE.md', 'line 94: signals', '- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 6b97515).\n', '- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 48c84c3).\n'), ('documentation/WHERE_WE_ARE.md', 'line 108: waiting: talk', '- Stored drawings for the other dot clouds: L-434 (stored drawings).\n- *L-451 (eight sentences held open); L-452 (notes repeating a citation).*\n', "- Stored drawings for the other dot clouds: L-434 (stored drawings).\n- Earth's talk 2: L-356 with L-375 (the field's model and offset).\n"), ('documentation/WHERE_WE_ARE.md', 'line 113: waiting: not urgent', '2. Choosing a date, and animation.\n3. L-449 (the run records): lost again Oct 16, put back; how many to\n   keep, and a check that stops the Daily Run on a loss.\n', '2. Choosing a date, and animation.\n'), ('documentation/WHERE_WE_ARE.md', 'line 120: details', "- *Next: L-413 (Earth's list) in the ledger: the design talks*\n", '- *Next: `HANDOFF_earth_round1_build_brief_20261016.md`*\n- Your rulings tonight: `DESIGN_earth_round1_rulings_20261016.md`\n')]


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
    print("  1. Run orrery_maintenance_run.py: its ledger index picks up")
    print("     L-330's new title and the dates.")
    print("  2. Move this script into documentation/; commit (with the two")
    print("     new records and your run-record copy); push.")
    print("  3. Start the build session from")
    print("     documentation/HANDOFF_earth_round1_build_brief_20261016.md.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
