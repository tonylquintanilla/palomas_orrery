#!/usr/bin/env python3
"""
patch_round1_notes_20261017.py -- two notes from Earth's round 1 onto
the ledger: a rule owed to ledger-and-session-records's next version
(L-351: a file saved into Tony's folder is read back before it is
reported delivered), and a locator owed on L-314 (Jelinek's frame,
sec. 3). Ledger only; no code, no Where We Are change.

Built on orrery bc25fdc83f85b75cb7389483bebf5508ab4f340e at
https://github.com/tonylquintanilla/palomas_orrery ("Update
WHERE_WE_ARE_10-16-26_2116_run_record.md"). The gallery is not touched
(44a6225c at https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 17, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_round1_notes_20261017.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing, in one file, edited only at the lines it
changes, so your notes elsewhere are kept:

    LEDGER_CONSOLIDATED.md   L-351 gains the read-back rule; L-314
                             gains the Jelinek locator; header stamp

WHAT IT PRINTS

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = 'bc25fdc'
ZONES = {}
MARKERS = {}
FINGERPRINTS = {}
RESULTS = {}
DELETES = {}
NEW_FILES = {}
EDITS = [('LEDGER_CONSOLIDATED.md', 'line 495: header stamp', "(Earth's fade done on Tony's runs and looks: L-410 and L-413), built on\nadcc1851 and gallery da442bf2.\nReview and RICE update Tony 6-21-2026\n", "(Earth's fade done on Tony's runs and looks: L-410 and L-413), built on\nadcc1851 and gallery da442bf2.\nModule updated: October 17, 2026 with Anthropic's Claude Opus 5.5\n(two notes from Earth's round 1: a rule owed on L-351, a locator owed\non L-314), built on bc25fdc8 and gallery 44a6225c.\nReview and RICE update Tony 6-21-2026\n"), ('LEDGER_CONSOLIDATED.md', 'line 3713: L-351 date', '#### [L-351] Rules learned at C2, owed to the next bumps of their stores (skills, protocol)\n<!-- L:351 status:OPEN upd:2026-10-16 section:A flag: rice: -->', '#### [L-351] Rules learned at C2, owed to the next bumps of their stores (skills, protocol)\n<!-- L:351 status:OPEN upd:2026-10-17 section:A flag: rice: -->'), ('LEDGER_CONSOLIDATED.md', 'line 3832: L-351 read-back rule', "    failure. The skill says nothing wrong today; it does not cover\n    this, so it is carried here, not bumped.\n**Gap:** Each lands with its store's next bump.\n", '    failure. The skill says nothing wrong today; it does not cover\n    this, so it is carried here, not bumped.\n  - **2026-10-17, ledger-and-session-records, next bump (Tony\'s Local\n    Folders):** a file saved into Tony\'s folder through the link to his\n    computer is read back from his folder and compared (size or hash)\n    before it is reported delivered. On 2026-10-16 the design session\n    saved the round-1 build brief, then saved an amended copy under the\n    same name with Claude Fable 5.1\'s three review additions; the save\n    reported "written", but his folder held the first version\'s bytes\n    (13,613 against the amended 15,257, read back 2026-10-17), most\n    likely because the tool reused the copy it had already sent under\n    that name. His 23:06 push (e63a207) carries the first version, and\n    the session told him the additions were in it. No harm followed:\n    the build did the records check inside `daily_run.py` anyway, and\n    the other two rested on reads already on file. The skill says\n    nothing wrong; it does not cover this, so it is carried here.\n**Gap:** Each lands with its store\'s next bump.\n'), ('LEDGER_CONSOLIDATED.md', 'line 9319: L-314 date', '<!-- L:314 status:OPEN upd:2026-10-16 section:A flag: rice:3/3/60/4 -->', '<!-- L:314 status:OPEN upd:2026-10-17 section:A flag: rice:3/3/60/4 -->'), ('LEDGER_CONSOLIDATED.md', 'line 9422: L-314 locator owed', "**Gap:** the whole item, now that L-305 has closed (2026-10-04); the\naberration is applied when the fetch is designed (ruled 2026-10-16).\nOn Earth's list (L-413), design talks.\n", '- **2026-10-17, a locator owed when these rows are next opened.** The\n  served aberration sentence (built 2026-10-17) rests on both fits\'\n  turned frames. Shue\'s row names where (theta "measured from the\n  aberrated Sun-Earth line", eq. 11, p. 17,697). Jelinek\'s does not:\n  `EARTH_BOW_SHOCK_JELINEK_R0_RADII`\'s `# Source:` ends "Fitted from\n  Themis crossings, in aberrated GSE." with no locator for that\n  clause, though L-305\'s record of the 2026-09-10 read gives it: "Jelinek\n  is in aberrated GSE (sec. 3)". Add "sec. 3" to that clause when the\n  row is next opened (provenance-discipline 2.30, What a Visitor Reads:\n  a citation names what was read and where).\n**Gap:** the whole item, now that L-305 has closed (2026-10-04); the\naberration is applied when the fetch is designed (ruled 2026-10-16);\nthe Jelinek frame locator above rides the same opening.\nOn Earth\'s list (L-413), design talks.\n')]


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
    print("stamps updated: the ledger's header")
    print("")
    print("patch applied (%d new files, %d edits in %d files, %d deleted)"
          % (len(NEW_FILES), len(EDITS), len(texts), len(DELETES)))
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py: its ledger index picks up")
    print("     the two dates.")
    print("  2. Move this script into documentation/; commit; push.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
