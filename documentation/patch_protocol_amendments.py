# -*- coding: utf-8 -*-
"""patch_protocol_amendments.py -- git-GUI preference ruling + Stale Skill = Stop [CRITICAL] gate

Built on 339897000b63fa768ccb9b556dd432bac4f9d4eb
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file in the REPO ROOT, open it in VS Code, click Run.
    All anchors are verified before anything is written; on failure
    nothing is touched.

AFTER RUNNING: only the LIVE protocol (PROJECT_INSTRUCTIONS.md) is
    amended. The documentation/project_instructions_v3_33.md snapshot is
    deliberately left alone -- skills_index.py treats versioned copies as
    historical record. The generated SKILL-MANIFEST zone is NOT touched.
    Two amendments now sit in a file still labelled v3.33; whether that
    becomes v3.34 with a fresh snapshot is your call.
"""

import os
import sys

EDITS = [
    ('PROJECT_INSTRUCTIONS.md', 'GIT-1', 'WHO TONY IS: git GUI is a preference, not a ban',
     b"Tony is a git novice, learning through experience rather than formal\nstudy, and works exclusively through GitHub Desktop's GUI -- never the\ngit command line. His known operations are commit and push. He doesn't\nuse or recognize pull; in his single-author, always-push-after-commit\nworkflow, it has nothing to reconcile. Frame any git guidance in GitHub\nDesktop's own terms (buttons, panels) rather than CLI syntax, or explain clearly.",
     b'Tony is a git novice, learning through experience rather than formal\nstudy, and works through GitHub Desktop\'s GUI. His known operations are\ncommit and push. He doesn\'t use or recognize pull; in his single-author,\nalways-push-after-commit workflow, it has nothing to reconcile. Frame git\nguidance in GitHub Desktop\'s own terms (buttons, panels) rather than CLI\nsyntax, or explain clearly.\n\nAmended August 5, 2026: the GUI is a PREFERENCE where practical, not a\nprohibition. An earlier wording ("never the git command line") read as a\nban and put this section in conflict with the safe-file-editing skill\'s\n`git apply` delivery format -- surfaced by the Fable skills-layer review\n(Job 2 #16). Tony\'s ruling: prefer the GUI and the Run button where they\ndo the job; a terminal step is a fallback, not forbidden. The obligation\nthat survives is the one below -- don\'t hand over an operation outside\nTony\'s known working set without plainly explaining what it does and what\ncould go wrong first.'),
    ('PROJECT_INSTRUCTIONS.md', 'GATE-1', 'add Stale Skill = Stop [CRITICAL] gate',
     b"Skill Manifest\nThe skills below are authored in the repo (skills/<name>/SKILL.md),\nversioned, SHA-stamped in their bodies, and installed to Tony's account.\nIf session behavior suggests a skill differs from the expected version,\nreconcile before trusting it -- same rule as a SHA mismatch. If a listed\nskill is relevant and has not fired, load it by name.",
     b'Skill Manifest\nThe skills below are authored in the repo (skills/<n>/SKILL.md),\nversioned, SHA-stamped in their bodies, and installed to Tony\'s account.\nIf a listed skill is relevant and has not fired, load it by name.\n\nStale Skill = Stop [CRITICAL]\nA skill lives in THREE stores: the repo (skills/<n>/SKILL.md), Tony\'s\naccount install (Settings > Skills -- the copy Claude actually loads), and\nthe manifest table below (a generated mirror, rebuilt by skills_index.py).\nWhen Claude loads a skill it needs, it compares that skill\'s own version\nline against the manifest row. The comparison is free: both are already in\ncontext.\n\nIf they disagree, STOP before proceeding with the task. Do NOT work from\nthe skill and mention the mismatch afterwards. Do NOT reason about which\ncopy looks newer and carry on. State plainly which version loaded, which\nversion the manifest expects, and ask Tony to:\n  - (do) push the current SKILL.md to skills/ in the repo, and\n  - (do) reinstall it to the account profile (Settings > Skills),\nthen reload the skill and continue the task.\n\nThe STOP is the whole point. A mismatch noticed mid-task and mentioned in\npassing is the failure this gate exists to prevent -- it is easy to miss,\nand meanwhile the work proceeds on a skill nobody has confirmed is the\nright one. (Tony\'s ruling, August 5, 2026. The prior wording asked only to\n"reconcile before trusting it," and the manifest still advertised 1.1/1.4\nagainst an actual 1.2/1.6 for about three weeks with nothing surfacing it.)\n\nThe repo is live-readable at any point, so where the loaded and expected\nversions agree but there is reason to doubt the repo copy, a raw fetch\nsettles it -- the same live read that confirms a push.'),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    files = {}
    for rel, eid, label, old, new in EDITS:
        path = os.path.join(root, rel.replace('/', os.sep))
        if rel not in files:
            if not os.path.exists(path):
                print("ERROR: %s not found. Save this in the repo root." % rel)
                return 1
            with open(path, 'rb') as f:
                files[rel] = f.read()
            if b'\r\n' in files[rel]:
                print("ERROR: %s has CRLF line endings." % rel)
                return 1

    for rel, eid, label, old, new in EDITS:
        n = files[rel].count(old)
        if n != 1:
            print("ANCHOR FAIL: %s (%s) in %s matched %d, expected 1." % (eid, label, rel, n))
            print("             Nothing written.")
            return 1

    for rel, eid, label, old, new in EDITS:
        files[rel] = files[rel].replace(old, new, 1)
        print("ok  %-10s %s" % (eid, label))

    for rel, data in files.items():
        try:
            data.decode('utf-8')
        except UnicodeDecodeError as exc:
            print("ERROR: %s would not be valid UTF-8 (%s). Nothing written." % (rel, exc))
            return 1

    for rel, data in files.items():
        with open(os.path.join(root, rel.replace('/', os.sep)), 'wb') as f:
            f.write(data)
    print("")
    print("patch applied to %d file(s)" % len(files))
    return 0


if __name__ == '__main__':
    sys.exit(main())
