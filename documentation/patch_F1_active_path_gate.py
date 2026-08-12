"""
patch_F1_active_path_gate.py -- narrow the stated push gate to the ACTIVE
BUILD PATH in the provenance-discipline skill and the protocol pointer.

WHY
    On 2026-08-05 (ledger L-184) Tony ratified a narrower push gate:
    Tier-1 = 0 on the interactive build path, not globally, because at
    206 Tier-1 findings the global gate blocks every push forever.

    The skill and the protocol kept teaching the global gate. A fresh
    session reads the protocol and the skill, not L-184, so it would
    have enforced a rule retired a week earlier -- and told Tony a push
    was not allowed when it was. Caught by Fable's document-layer claim
    audit, finding F1, 2026-08-11.

    Tony's ruling, 2026-08-11: keep BOTH, and say which is live. Global
    Tier-1 = 0 remains the destination; the firing rule is the active
    build path. And the scope MOVES -- the interactive gallery path is
    what is active now; when Earth-science visualization work resumes,
    those files become the gated path in turn.

WHAT THIS DOES
    Six anchored edits across TWO files, applied all-or-nothing. Both
    fingerprints are checked before anything is written, so a mismatch
    on either file leaves both untouched.

    skills/provenance-discipline/SKILL.md
      1. frontmatter `description` -- gate restated
      2. frontmatter `fires_when` -- gate restated (this is the text
         skills_index.py copies into the protocol's manifest row)
      3. version line 1.8 -> 1.9
      4. version-history paragraph gains the v1.9 entry
      5. "The Goal State" section rewritten

    PROJECT_INSTRUCTIONS.md
      6. the Fetched-vs-Recalled pointer names the active-path gate

    The manifest ROW in the protocol is NOT patched here. It is a
    generated zone; skills_index.py rebuilds it from `fires_when`.
    Editing it by hand would be overwritten on the next run.

HOW TO RUN IT
    Save this file into the palomas_orrery repo root (the folder holding
    PROJECT_INSTRUCTIONS.md), open it in VS Code, and click Run.

    Or from a terminal in that folder:
        python patch_F1_active_path_gate.py

    THEN, and this matters -- a skill lives in THREE stores and all
    three have to agree or the next session stops on the Stale Skill
    gate:
      1. run skills_index.py           (rebuilds the manifest row)
      2. reinstall the skill to your account: Settings > Skills
      3. commit SKILL.md and PROJECT_INSTRUCTIONS.md TOGETHER, in one
         commit, per the binding rule in ledger-and-session-records

WHAT SUCCESS LOOKS LIKE
    One "ok" line per edit, then "patch applied" with both byte counts.

WHAT FAILURE LOOKS LIKE
    A single "ERROR:" line (a base file has moved) or an "ANCHOR FAIL"
    line naming the edit whose text was not found. Either way NOTHING is
    written to EITHER file.

Built on cdcdb4bba7d1f86ed4f7dacadcfcc4393266be35
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Role: patch
Domain: dev_tools

Written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

SKILL = os.path.join('skills', 'provenance-discipline', 'SKILL.md')
PROTOCOL = 'PROJECT_INSTRUCTIONS.md'

# Content fingerprints, line endings normalized to LF.
BASE_MD5 = {
    SKILL: '8313af8320b19d2468caccea2a4190cb',
    PROTOCOL: '1823338a8e85d130cbc0bc4cc1a8c096',
}

EDITS = [
    (
        SKILL, 'frontmatter description',
        b"or preparing a GitHub push (Tier-1 = 0 is the push gate).",

        b"or preparing a GitHub push (the gate is Tier-1 = 0 on the active "
        b"build path).",
    ),
    (
        SKILL, 'frontmatter fires_when',
        b"fires_when: Scanner runs, audits, citations, constants, pre-push "
        b"(Tier-1 = 0)\n",

        b"fires_when: Scanner runs, audits, citations, constants, pre-push "
        b"(Tier-1 = 0 on the active build path)\n",
    ),
    (
        SKILL, 'version line 1.8 -> 1.9',
        b"Skill version: 1.8 | Cut from palomas_orrery @ 8e4b5ca (v1.8), "
        b"earlier\n@ 3398970 (v1.7) | August 11, 2026\n",

        b"Skill version: 1.9 | Cut from palomas_orrery @ cdcdb4b (v1.9), "
        b"earlier\n@ 8e4b5ca (v1.8), @ 3398970 (v1.7) | August 11, 2026\n",
    ),
    (
        SKILL, 'version-history entry for 1.9',
        b"already talked itself into calling fabricated.\n",

        b"already talked itself into calling fabricated.\n"
        b"v1.9 narrows The Goal State to the ACTIVE BUILD PATH gate Tony\n"
        b"ratified 2026-08-05 (L-184), keeping global Tier-1 = 0 as the\n"
        b"stated destination rather than the firing rule. The skill had\n"
        b"carried the retired global gate for a week; caught by Fable's\n"
        b"document-layer claim audit, finding F1, August 11, 2026.\n",
    ),
    (
        SKILL, 'The Goal State rewritten',
        b"## The Goal State\n"
        b"\n"
        b"Tier-1 = 0 before any GitHub push. A clean audit can rest on "
        b"honest\n",

        b"## The Goal State\n"
        b"\n"
        b"**The push gate is Tier-1 = 0 ON THE ACTIVE BUILD PATH** -- the\n"
        b"files the project is currently building. As of August 2026 that is\n"
        b"the interactive gallery build path (Tony ratified 2026-08-05;\n"
        b"recorded in L-184). The scope MOVES with the work: when\n"
        b"Earth-science visualization work resumes, those files become the\n"
        b"gated path in turn.\n"
        b"\n"
        b"**Global Tier-1 = 0 is the destination, not the current gate.** It\n"
        b"was suspended, not retired. At 206 Tier-1 findings a global gate\n"
        b"blocks every push forever, and a rule nobody can obey stops being\n"
        b"read as a rule at all. The global number is approached by clearing\n"
        b"paths as they go active -- which is why the gate is written\n"
        b"active-path rather than pinned to one named path.\n"
        b"\n"
        b"Do not enforce the global form on a push outside the active path,\n"
        b"and do not read a bare \"Tier-1 = 0\" anywhere in this project as\n"
        b"the global form unless it says so. (Tony's ruling 2026-08-11, on\n"
        b"Fable audit finding F1: this skill and the protocol's manifest row\n"
        b"carried the global gate for a week after the ratification narrowed\n"
        b"it, while Tony pushed five times in one evening against it. A gate\n"
        b"that is routinely and correctly ignored is worse than a wrong\n"
        b"number -- it teaches the reader to ignore gates.)\n"
        b"\n"
        b"A clean audit can rest on honest\n",
    ),
    (
        PROTOCOL, 'gate pointer names the active path',
        b"Tier-1 = 0 push gate: provenance-discipline skill.)\n",

        b"active-build-path Tier-1 push gate: provenance-discipline skill.)\n",
    ),
]


def fail(msg):
    print("ERROR: %s" % msg)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    blobs = {}
    crlf = {}
    for rel in BASE_MD5:
        path = os.path.join(here, rel)
        if not os.path.isfile(path):
            fail("%s not found. Save this script into the repo root (the "
                 "folder holding %s)." % (rel, PROTOCOL))
        with open(path, 'rb') as f:
            data = f.read()
        got = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
        if got != BASE_MD5[rel]:
            fail("base file has moved: %s\n"
                 "       expected md5 (LF-normalized) %s\n"
                 "       found                        %s\n"
                 "       NOTHING was written to either file."
                 % (rel, BASE_MD5[rel], got))
        blobs[rel] = data
        crlf[rel] = data.count(b'\r\n') > 0
        if crlf[rel]:
            print("note: %s uses CRLF; anchors translated to match." % rel)

    for rel, label, old, new in EDITS:
        if crlf[rel]:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = blobs[rel].count(old)
        if count != 1:
            print("ANCHOR FAIL (%s): expected 1 match, found %d. "
                  "Nothing written to either file." % (label, count))
            sys.exit(1)
        blobs[rel] = blobs[rel].replace(old, new)
        print("  ok  %s" % label)

    for rel, data in blobs.items():
        with open(os.path.join(here, rel), 'wb') as f:
            f.write(data)

    print()
    print("patch applied")
    for rel, data in sorted(blobs.items()):
        print("  %-44s %d bytes" % (rel, len(data)))
    print()
    print("NEXT -- three stores must agree or the next session stops:")
    print("  1. run skills_index.py (rebuilds the protocol manifest row)")
    print("  2. reinstall provenance-discipline: Settings > Skills")
    print("  3. commit SKILL.md and PROJECT_INSTRUCTIONS.md in ONE commit")


if __name__ == '__main__':
    main()
