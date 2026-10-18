#!/usr/bin/env python3
"""
patch_L410_4_earth_fade_done_20261017.py -- records Earth's fade as done
on Tony's runs and looks: L-410 (open for the Sun's fades), L-413 (talk
2 next), and Where We Are.

Built on orrery adcc1851cf9f8582b906ca51074a61dd09c92799 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
da442bf21c7d90bffc775e8f5e58d751265a1aa2 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 17, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L410_4_earth_fade_done_20261017.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing; each file is edited only at the lines it
changes, so your notes elsewhere are kept:

    LEDGER_CONSOLIDATED.md          L-410, L-413; the header stamp
    documentation/WHERE_WE_ARE.md   above the run-record marker only

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = 'adcc1851'
ZONES = {}
MARKERS = {'documentation/WHERE_WE_ARE.md': '--- Your run record below this line'}
FINGERPRINTS = {}
RESULTS = {}
DELETES = {}
NEW_FILES = {}
EDITS = [
    ('LEDGER_CONSOLIDATED.md', 'header stamp', 'L-410; the low-orbit look recorded on L-413; L-434 and L-435 updated),\nbuilt on 785536e5 and gallery 44a6225c.\n', "L-410; the low-orbit look recorded on L-413; L-434 and L-435 updated),\nbuilt on 785536e5 and gallery 44a6225c.\nModule updated: October 17, 2026 with Anthropic's Claude Opus 5.5\n(Earth's fade done on Tony's runs and looks: L-410 and L-413), built on\nadcc1851 and gallery da442bf2.\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-410 Earth done', "**Gap:** Tony's runs, and his looks in both instruments, close Earth's\nfade; then the Sun's fades,", '- **Earth\'s fade done, 2026-10-17,** on Tony\'s runs and looks (his run\n  record, `documentation/WHERE_WE_ARE_10-16-26_2116_run_record.md`, saved again that night):\n  the orrery run 31 of 31 gating, "Drawings export check" 8 of 8 planted\n  faults, the gate 0 TIER-1, pushed adcc1851; the orrery plot, "looks\n  right"; the Daily Run 29 of 29 gating, "Drawings" 12 of 12, "Typed\n  facts" 0 held open, pushed da442bf2; the live check 2 of 2, store drift\n  against orrery adcc1851 with 0 DRIFT; the Earth room on the phone,\n  "Looks good". The item stays open for the Sun\'s fades.\n**Gap:** the Sun\'s fades,'),
    ('LEDGER_CONSOLIDATED.md', 'L-413 talk 2 next', "**Gap:** Tony's runs and looks at Earth's fade (L-410); then talk 2 (L-356\nwith L-375, and L-454), next session,", "- **2026-10-17, Earth's fade done** (L-410) on Tony's runs and looks.\n**Gap:** talk 2 (L-356 with L-375, and L-454), next session,"),
    ('documentation/WHERE_WE_ARE.md', 'date and box', 'Last updated: October 17, 2026, night: Earth\'s fade built.\n- Written at orrery 785536e and gallery 44a6225.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - Earth\'s hydrogen now fades out from 3 to 100 Earth radii in both\n>   instruments, where it was a sharp shell (L-410, the fades). Built,\n>   waiting on your runs and looks.\n> - The low-orbit look is done: "contrast and shape are good".\n>\n> **Do next:** *Your run order, section 1 of\n> HANDOFF_earth_fade_build_20261017.md.*\n>\n> **Needs you now:**\n> - *Two orrery patches, the run, push; the website patch, the Daily\n>   Run, push; then the two looks.*\n> - Next session: Earth\'s design talk 2 (that handoff, section 5).', 'Last updated: October 17, 2026, night: Earth\'s fade done.\n- Written at orrery adcc185 and gallery da442bf.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - Earth\'s hydrogen fades out from 3 to 100 Earth radii in both\n>   instruments, live and looked at: "looks right", "Looks good"\n>   (L-410, the fades).\n> - The low-orbit look is done: "contrast and shape are good".\n>\n> **Do next:** *Earth\'s design talk 2, next session: section 5 of\n> HANDOFF_earth_fade_build_20261017.md.*\n>\n> **Needs you now:**\n> - *Run this small close patch, commit and push.*\n> - Talk 2 covers the field\'s newer model, its off-centre dipole, and\n>   a way to draw edges that move.'),
    ('documentation/WHERE_WE_ARE.md', 'road stage 5', "  5.   [NOW]   *Earth's list (L-413): the fade built, your runs and\n               looks; then talk 2, next session.* << moved this session", "  5.   [NOW]   *Earth's list (L-413): the fade done; talk 2 next\n               session, then talks 3 to 6.* << moved this session"),
    ('documentation/WHERE_WE_ARE.md', 'signals', '- Last cache build: 20261017T205940Z, ok, every rename on the first try (gallery 44a6225).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 785536e).', '- Last cache build: 20261018T000459Z, ok, every rename on the first try (gallery da442bf).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, adcc185).'),
    ('documentation/WHERE_WE_ARE.md', 'details next', '- *Next: `HANDOFF_earth_fade_build_20261017.md` (your run order; talk 2)*', '- *Next: `HANDOFF_earth_fade_build_20261017.md`, section 5 (talk 2)*'),
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
    print("patch applied (%d edits in %d files)" % (len(EDITS), len(texts)))
    print("")
    print("NEXT: move this script into documentation/; commit; push.")
    print("(The next orrery maintenance run refreshes the ledger's index.)")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
