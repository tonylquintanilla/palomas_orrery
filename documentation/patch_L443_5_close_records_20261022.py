r"""patch_L443_5_close_records_20261022.py -- L-443's last records of the
evening: slice 1 live, the phone checklist, and L-471 (a delivered patch
is final).

RUN COMMAND
    python patch_L443_5_close_records_20261022.py

Save it in the ORRERY repository's root folder
(C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\),
open it in VS Code and click Run. Then move it to documentation/,
commit and push. No maintenance run is needed tonight; the next one
adds L-471 to the ledger's index.

Built on orrery f10e859f at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Final as delivered: nothing will replace it.

WHAT IT CHANGES (records only; no code)
    LEDGER_CONSOLIDATED.md      L-443: live at b93072eb, the Gap now
                                your phone look; L-471, new: three rules
                                for safe-file-editing's next version
    documentation/WHERE_WE_ARE.md  by section: header, box, Deferred,
                                Signals. The run-record zone is not
                                touched
    documentation/HANDOFF_L443_slice1_build_20261022.md  the pushes;
                                section 10, the phone checklist

Each file is checked only at the lines this patch edits, so notes you
have added elsewhere do not stop it.

SUCCESS prints one "ok" line per file, then "patch applied".
FAILURE prints one FAILURE line, and NOTHING is written; undo is
Discard Changes in GitHub Desktop.

Role: devtool
Domain: dev_tools
"""

import hashlib
import os
import sys

TITLE = 'L-443 close records'
FILES = [
    {"path": 'LEDGER_CONSOLIDATED.md', "kind": "edit", "guard": 'anchors', "md5": 'a247efe3f1272182316cceae59dadccd', "edits": [
        (b'\n#### [L-470] Orrery entries the website cannot serve as they stand (orrery, objects)\n',
         b'\n#### [L-471] A delivered patch is final (safe-file-editing, next version)\n<!-- L:471 status:OPEN upd:2026-10-22 section:A flag: rice: -->\n- **Found 2026-10-22, closing L-443\'s slice 1** (Tony\'s run records,\n  `documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`). One class:\n  how a patch reaches Tony and what happens when it meets his folder.\n  Three rules for safe-file-editing\'s next version, method rather than\n  rulings (the protocol\'s Method Belongs to the Skill):\n  - **A delivered patch is final.** Claude never replaces a patch once\n    it is in Tony\'s folder; an addition goes in the next numbered\n    patch. Patch 3 was replaced twice after Tony had run its first\n    copy, leaving an unrun copy in the orrery\'s root that patch 4 had\n    to remove. Tony: "part of the problem is that I ran these patches\n    while you were still amending them. That\'s a lesson learned for\n    me." The fix is Claude\'s: a patch is delivered only when it is\n    ready to run, and Claude says so.\n  - **One route per document.** A document a patch writes is not also\n    handed to Tony to download, or he is told the patch will place it.\n    His downloaded copy of the design brief made patch 3 refuse; he\n    deleted it and ran it again. Tony: "why does a patch refuse when it\n    sees a document you gave to me as an artifact?"\n  - **A refusal says what to do, and a match is not a conflict.** When\n    a file the patch would write new already exists, the refusal names\n    the likely cause and the fix ("a copy of the same document you\n    downloaded: delete it and run again"); a file already holding\n    exactly what the patch would write is accepted.\n**Gap:** safe-file-editing\'s next version carries the three.\n**Ref:** L-443; `documentation/patch_L443_4_period_count_20261022.py`.\n\n#### [L-470] Orrery entries the website cannot serve as they stand (orrery, objects)\n'),
        (b'**Gap (replaces the one below, 2026-10-22, late evening):** patch 4 and\n',
         b"- **2026-10-22, 22:50: live.** Orrery pushed at f10e859f (patch 4,\n  maintenance run 31 of 31); the second Daily Run passed 35 of 35,\n  Solar System figures among them; the website pushed at b93072eb; the\n  live run found all 25 files served as committed. Tony reinstalled\n  interactive-exhibit 1.21 and horizons-orbital-mechanics 1.9.\n**Gap (replaces the one below, 2026-10-22, 22:50):** Tony's phone look\n(the handoff, sec. 10); then slice 2, the spacecraft and the\nopen-path comets.\n**Gap (superseded above):** patch 4 and\n"),
    ]},
    {"path": 'documentation/WHERE_WE_ARE.md', "kind": "edit", "guard": 'anchors', "md5": 'ec5bf7f95b0b276c216334cd3b5a00fc', "edits": [
        (b'Last updated: October 22, 2026, late evening: slice 1 in the orrery;\none fix before the website goes.\n- Written at orrery d91dc1d and gallery 0bb3434, with patch 4.\n',
         b'Last updated: October 22, 2026, late evening: slice 1 is live, 50\nbodies in folding groups.\n- Written at orrery f10e859 and gallery b93072e, with patch 5.\n'),
        (b'> - Slice 1 of L-443 (the objects to the website) is in the orrery,\n>   pushed: 50 bodies, in six groups that fold open in the drawer.\n',
         b'> - Slice 1 of L-443 (the objects to the website) is live: 50 bodies,\n>   in six groups that fold open in the drawer.\n'),
        (b"> **Do next:** *patch 4, the orrery run and push, then the Daily Run\n> and the website's push (the handoff, sec. 9).*\n",
         b'> **Do next:** *your phone look (the handoff, sec. 10); then slice 2,\n> the spacecraft and the comets on open paths.*\n'),
        (b'> - *(do) Patch 4 and the runs, in order (the handoff, sec. 9).*\n> - *Reinstall interactive-exhibit 1.21, horizons-orbital-mechanics 1.9.*\n',
         b'> - *(do) Your phone look (the handoff, sec. 10).*\n'),
        (b'- A drawn main-belt cloud (L-443 (the objects)), behind slice 2.\n\n',
         b"- A drawn main-belt cloud (L-443 (the objects)), behind slice 2.\n- L-471 (a delivered patch is final): safe-file-editing's next version.\n\n"),
        (b'- Last cache build: 20261023T021052Z, ok, first try (on gallery\n  0bb3434, not yet pushed).\n',
         b'- Last cache build: 20261023T032713Z, ok, first try (gallery\n  b93072e).\n'),
    ]},
    {"path": 'documentation/HANDOFF_L443_slice1_build_20261022.md', "kind": "edit", "guard": 'anchors', "md5": '26ee3b3bd6d0acd74858d34b12b708fd', "edits": [
        (b"(branch main of each). Pushed at: orrery d91dc1d0 (section 2's steps\n1 to 3); the website, after section 9.\n\n",
         b"(branch main of each). Pushed at: orrery d91dc1d0 (section 2's steps\n1 to 3) and f10e859f (section 9); the website b93072eb.\n\n"),
        (b"\nSession written October 2026 with Anthropic's Claude Opus 5.5.\n",
         b'\n## 10. Your look on the phone (Mode 5)\n\nThe website went live at b93072eb; the live run found all 25 files\nserved as committed. Each line is a yes or a no; note anything that\nlooks wrong beside it.\n\n1. A bare palomasorrery.com/interactive.html link opens the Solar\n   System room.\n2. The i panel\'s two new sentences read as you approved them.\n3. See more shows the six groups in their places along the list.\n4. Tap Comets: it folds open with 13 comets. Tap it again: it closes.\n5. Open the trans-Neptunian objects: 15 bodies, by their average\n   distance from the Sun.\n6. Tick a group\'s box: its bodies draw and the view widens to hold\n   them. All / none clears them, and the Sun stays.\n7. Hover Orcus: the shared-centre sentence. Hover Eris: none.\n8. Hover 2025 PN7: "Orbital period: 1.00 years (364 days)".\n9. Hover a comet, then find Halley: where it is now, far out.\n10. The Explorer opens from its gallery card.\n\nSession written October 2026 with Anthropic\'s Claude Opus 5.5.\n'),
    ]},
]


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    root = os.getcwd()
    plan = []
    for f in FILES:
        path = os.path.join(root, f["path"])
        if f["kind"] == "delete":
            if not os.path.exists(path):
                plan.append((f, path, None, "gone"))
                continue
            raw = open(path, "rb").read().replace(b"\r\n", b"\n")
            if hashlib.md5(raw).hexdigest() != f["md5"]:
                fail("%s is not the copy this patch removes (content "
                     "fingerprint differs); nothing was removed" % f["path"])
            plan.append((f, path, None, False))
            continue
        if f["kind"] == "new":
            if os.path.exists(path):
                fail("%s already exists; this patch writes it new" % f["path"])
            plan.append((f, path, None, False))
            continue
        if not os.path.exists(path):
            fail("%s not found. Run this from the repository's root folder" % f["path"])
        raw = open(path, "rb").read()
        crlf = b"\r\n" in raw
        lf = raw.replace(b"\r\n", b"\n")
        if f["guard"] == "md5" and hashlib.md5(lf).hexdigest() != f["md5"]:
            fail("%s is not the file this patch was built against "
                 "(content fingerprint differs)" % f["path"])
        spots = []
        for k, (old, new) in enumerate(f["edits"]):
            n = lf.count(old)
            if n != 1:
                fail("ANCHOR FAIL in %s, edit %d: expected 1 match, found %d: %r"
                     % (f["path"], k + 1, n, old[:70]))
            spots.append((lf.index(old), old, new))
        spots.sort()
        out, last = b"", 0
        for i, old, new in spots:
            if i < last:
                fail("%s: two edits overlap" % f["path"])
            out += lf[last:i] + new
            last = i + len(old)
        out += lf[last:]
        plan.append((f, path, out, crlf))
    for f, path, out, crlf in plan:
        if f["kind"] == "delete":
            if crlf == "gone":
                print("ok  %s (already gone)" % f["path"])
            else:
                os.remove(path)
                print("ok  %s (removed)" % f["path"])
            continue
        if f["kind"] == "new":
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            open(path, "wb").write(f["content"])
            print("ok  %s (new, %d bytes)" % (f["path"], len(f["content"])))
        else:
            open(path, "wb").write(out)
            print("ok  %s (%d edits%s)" % (f["path"], len(f["edits"]),
                                        "; it was CRLF in the working copy, written LF" if crlf else ""))
    print("patch applied: %s (%d files)" % (TITLE, len(plan)))


if __name__ == "__main__":
    main()
