"""
patch_fable_corrections.py -- apply the corrections from Fable's
document-layer claim audit (documentation/FABLE_FINDINGS_document_layer_
claims.md), plus the Stale Skill gate amendment earned tonight.

WHAT THIS DOES
    Seventeen anchored edits across SIX files, applied all-or-nothing.
    Every fingerprint is checked before anything is written, so a
    mismatch on any one file leaves all six untouched.

    LEDGER_CONSOLIDATED.md
      F3  "7 of 45 top-level assignments" -> 49 with 6 derived (x2 sites)
      F4  "126 dead tooltip fields"       -> 124
      F5  "the 126 dead tooltip fields"   -> 124
      F6  "defined 126 times"             -> 124, and the note that the
          126 was a raw-grep artifact rather than a corrected count
      F12 "the next new item is L-062"    -> no number at all
      F2  version-history appendix gains v3.35, v3.36, v3.37 and v3.38

    documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md
      F7  "Two sites in the ledger carry 126" -> three live sites

    documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md
      F13 "current HEAD orrery X / gallery Y" -> a built-on anchor, which
          stays true instead of going false on the next push

    README.md
      F14 two stale module counts; the schematic loses its number
          entirely rather than acquiring a fresh one to go stale

    DATA_INVENTORY.md
      F10 the tracked file stops claiming it is gitignored

    PROJECT_INSTRUCTIONS.md
      F11 two pointers to documentation/PROJECT_ORIGIN.md, which does
          not exist -- the file is at the repo root (x2 sites)
      +   Stale Skill = Stop gains its two known limits (see below)
      +   version header -> v3.38, version history entry added

THE MEASUREMENTS
    Not carried over from the report. Re-measured against this commit:
      - constants_new.py: 49 top-level assignments; 7 non-literal, of
        which 6 are derived expressions and 1 is a constructor call
        (HORIZONS_MAX_DATE = datetime(...)). That last figure also
        settles the master plan decision 12 open question -- ONE
        constructor call, not two.
      - shell_configs.py: 124 'tooltip' dict keys via ast (83 in
        SHELL_CONFIGS + 41 in CUSTOM_SHELLS). Raw grep returns 133
        text matches, which is why grep-derived counts keep drifting.
      - repo root: 118 .py files, 96,078 non-blank lines.

THE GATE AMENDMENT
    Tony's ruling tonight: a mid-session skill reinstall CANNOT be
    verified from inside the session, and accepting "Tony reinstalled
    it" in place of a read would be cite-to-clear moved into the skill
    layer. So the amendment adds no assertion-based escape. It records
    two limits -- the gate is load-triggered, and the loaded copy is
    bound at conversation start -- and routes the verification into the
    handoff, where the NEXT session discharges it against the only thing
    it can actually read.

HOW TO RUN IT
    Save this file into the palomas_orrery repo root (the folder holding
    PROJECT_INSTRUCTIONS.md), open it in VS Code, and click Run.

    Or from a terminal in that folder:
        python patch_fable_corrections.py

    THEN, in this order:
      1. run ledger_index.py      (regenerates the index zone)
      2. run module_atlas.py      (F8: the atlas still describes the
                                   pre-move tree)
      3. run provenance_scanner.py (F9: the audit still says 119 files)
      4. update the resident project instructions to v3.38 and archive a
         copy as documentation/project_instructions_v3_38.md
      5. commit

WHAT SUCCESS LOOKS LIKE
    One "ok" line per edit, then "patch applied" with six byte counts.

WHAT FAILURE LOOKS LIKE
    A single "ERROR:" line (a base file has moved) or an "ANCHOR FAIL"
    line naming the edit whose text was not found. Either way NOTHING is
    written to ANY of the six files.

Built on bbc5e78cf6bf9043da16862abe9cfebe4cdac3c0
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Role: patch
Domain: dev_tools

Written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

LEDGER = 'LEDGER_CONSOLIDATED.md'
PROTOCOL = 'PROJECT_INSTRUCTIONS.md'
README = 'README.md'
INVENTORY = 'DATA_INVENTORY.md'
PLAN = os.path.join('documentation', 'MASTER_PLAN_INTERACTIVE_GALLERY.md')
SUMMARY = os.path.join('documentation',
                       'MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md')

# Content fingerprints, line endings normalized to LF.
BASE_MD5 = {
    LEDGER:    '83262aa66ea8adaecc87db42a27ff7c8',
    PROTOCOL:  '426783a88a5d7a7f93c5037a4f061bea',
    README:    'ed1da8f779380faf4db25410a75b55b7',
    INVENTORY: 'ef5b0b37aaaa1684e7e876735f79e079',
    PLAN:      '6e7776342fad378370ce97388c51bb52',
    SUMMARY:   '5a91c017864785885cbf28d454946a93',
}

VERSION_HISTORY_ADDITION = (
    b"\n"
    b"v3.35 (August 7, 2026): Updated skill safe-file-editing (v1.3).\n"
    b"\n"
    b"v3.36 (August 8, 2026): Register Rule amended (Part 2). A\n"
    b"message-level Check 0 added ahead of the two paragraph-level checks --\n"
    b"does this message ask Tony for one thing. The prior checks were\n"
    b"paragraph-scoped and could all pass while a message carried four\n"
    b"separate jobs, which is the load that actually fails. Two supporting\n"
    b"defaults added: answer first with evidence only on request, and\n"
    b"capture goes in a file rather than in the conversation. Backstop\n"
    b"corrected -- \"opaque\" is a repair, not the mechanism, because Tony has\n"
    b"stated he cannot sustain flagging density in real time; the check runs\n"
    b"on Claude's side before sending. \"Just the decision\" added as a second\n"
    b"Tony-side lever. Origin: a full mobile session in which the rule did\n"
    b"not fire once.\n"
    b"\n"
    b"v3.37 (August 11, 2026): Two changes. (1) \"The Artifact Bounds the\n"
    b"Audit\" added to Part 3 -- Tony's August 8 ruling, drafted for the first\n"
    b"time. (2) Protocol trimmed from 882 lines to 849: version history\n"
    b"v3.29-v3.33 dropped (the ledger carries it) and twenty-seven Part 5\n"
    b"lessons removed as restatements of rules already stated where they\n"
    b"fire. A first cut moved ALL forty-one lessons to an archive file and\n"
    b"was reversed the same day -- an archive has no trigger, so the fourteen\n"
    b"with no counterpart elsewhere would have left. A lesson duplicated by a\n"
    b"firing rule is redundant; a lesson that is nowhere else IS the archive.\n"
    b"\n"
    b"v3.37.1 (August 11, 2026): provenance-discipline skill v1.8 -> v1.9.\n"
    b"\n"
    b"v3.38 (August 11, 2026): Two changes, both from Fable's document-layer\n"
    b"claim audit. (1) Two dead pointers to documentation/PROJECT_ORIGIN.md\n"
    b"corrected -- the file is at the repo root (finding F11). (2) Stale\n"
    b"Skill = Stop gains its two known limits. The gate is LOAD-TRIGGERED, so\n"
    b"a manifest that changes later in the same session creates a mismatch\n"
    b"with nothing to fire on -- which is exactly what happened when\n"
    b"provenance-discipline went 1.8 to 1.9 mid-session and the mismatch\n"
    b"surfaced only because a later check re-read the file for an unrelated\n"
    b"reason. And a mid-session reinstall CANNOT be verified from inside the\n"
    b"session: the loaded copy appears bound at conversation start, so the\n"
    b"reinstall lands in the account and stays invisible until the next\n"
    b"session. Tony's ruling: do not add an assertion-based clear. \"Tony\n"
    b"reinstalled it\" is a claim, not a check, and accepting it in place of a\n"
    b"read is cite-to-clear moved into the skill layer. The verification is\n"
    b"deferred into the handoff and discharged by the next session's load.\n"
    b"Skill-layer companion: provenance-discipline v1.9 narrows the push gate\n"
    b"to the ACTIVE BUILD PATH (L-184, ratified 2026-08-05), keeping global\n"
    b"Tier-1 = 0 as the destination rather than the firing rule (finding F1).\n"
)

GATE_AMENDMENT = (
    b"The repo is live-readable at any point, so where the loaded and expected\n"
    b"versions agree but there is reason to doubt the repo copy, a raw fetch\n"
    b"settles it -- the same live read that confirms a push.\n"
    b"\n"
    b"Two limits on this gate, both learned August 11, 2026, and neither one\n"
    b"a reason to weaken it.\n"
    b"\n"
    b"IT IS LOAD-TRIGGERED. The comparison happens when Claude loads a skill.\n"
    b"A manifest that changes LATER in the same session produces a mismatch\n"
    b"with nothing left to fire on. That is what happened when\n"
    b"provenance-discipline went 1.8 to 1.9 mid-session: the load had already\n"
    b"happened and had correctly matched, and the mismatch surfaced only\n"
    b"because a later check re-read the file for an unrelated reason. Nothing\n"
    b"in the gate would have caught it.\n"
    b"\n"
    b"A MID-SESSION REINSTALL CANNOT BE VERIFIED FROM INSIDE THE SESSION. The\n"
    b"skill copy a conversation loads appears to be bound when the\n"
    b"conversation starts. A reinstall lands in the account and stays\n"
    b"invisible to the running session -- confirmed by two fresh sandboxes,\n"
    b"one built after a re-upload, both serving the old bytes while Settings\n"
    b"showed the new version. This is architectural, not a mistake anyone\n"
    b"made.\n"
    b"\n"
    b"So do NOT clear the gate on Tony's word that he reinstalled it. That is\n"
    b"an assertion standing in for a check Claude cannot perform -- the\n"
    b"skill-layer form of a `# Source:` over recalled data, and it fails the\n"
    b"same way: the claim suppresses the suspicion that would catch the real\n"
    b"case. (Tony's ruling, August 11, 2026, declining exactly this\n"
    b"amendment when Claude proposed it.)\n"
    b"\n"
    b"A mid-session skill bump is therefore NOT cleared in session. It is\n"
    b"written into the handoff as an obligation the next session discharges:\n"
    b"\n"
    b"    provenance-discipline went to 1.9 at <SHA>; the session that\n"
    b"    bumped it loaded 1.8; the next session confirms its loaded copy\n"
    b"    reads 1.9 before doing provenance work.\n"
    b"\n"
    b"The next session's load performs the check against the only thing it\n"
    b"can actually read. Same structure as the SHA round trip: defer the\n"
    b"verification, carry it in writing, settle it against something\n"
    b"unforgeable. Until then the state stays honestly unverified, which is\n"
    b"what it is.\n"
)

EDITS = [
    # ---------------- LEDGER ----------------
    (
        LEDGER, 'F3 top-level assignment count (49, 6 derived)',
        b"with `ast` without executing it fights the store's design: 7 of 45\n",

        b"with `ast` without executing it fights the store's design: 6 of 49\n",
    ),
    (
        LEDGER, 'F3 derived-constant echo',
        b"  live; it is dormant. (2) The 7 derived constants were written up "
        b"as a\n",

        b"  live; it is dormant. (2) The 6 derived constants were written up "
        b"as a\n",
    ),
    (
        LEDGER, 'F4 tooltip count at the breakdown bullet',
        b"- 126 dead `tooltip` fields (83 sphere + 41 custom) are a\n",

        b"- 124 dead `tooltip` fields (83 sphere + 41 custom) are a\n",
    ),
    (
        LEDGER, 'F5 tooltip count in the build-path decision',
        b"(d) decide on the 126 dead tooltip fields. L-184's build path "
        b"cannot be\n",

        b"(d) decide on the 124 dead tooltip fields. L-184's build path "
        b"cannot be\n",
    ),
    (
        LEDGER, 'F6 tooltip count and the grep-artifact note',
        b"  **126 times and read by nothing**, confirming L-181's \"124 dead\n"
        b"  tooltip fields\" as dead and updating the count.",

        b"  **124 times and read by nothing**, confirming L-181's \"124 dead\n"
        b"  tooltip fields\" as dead. (Corrected 2026-08-11: this bullet had\n"
        b"  read 126 and described itself as \"updating the count\" -- but 126\n"
        b"  is the raw text-match total, and the real figure is 124 dict\n"
        b"  keys, 83 in SHELL_CONFIGS plus 41 in CUSTOM_SHELLS, measured with\n"
        b"  `ast`. It revised a correct number back to a wrong one on the\n"
        b"  strength of a grep.)",
    ),
    (
        LEDGER, 'F12 next-handle claim loses its number',
        b"re-embed a fresh copy. Handles are append-only -- the next new item "
        b"is L-062;\n",

        b"re-embed a fresh copy. Handles are append-only -- a new item takes "
        b"the next\nunused L-### (read the highest in use off the index; do "
        b"not trust a number\nwritten here, which goes stale the moment it is "
        b"written);\n",
    ),
    (
        LEDGER, 'F2 version-history appendix gains v3.35 through v3.38',
        b"\n### Preserved verbatim: v3.29 Technical lessons "
        b"(now field notes in skills)\n",

        VERSION_HISTORY_ADDITION
        + b"\n### Preserved verbatim: v3.29 Technical lessons "
        b"(now field notes in skills)\n",
    ),

    # ---------------- SUMMARY ----------------
    (
        SUMMARY, 'F7 site count for the 126 figure',
        b"sites in the ledger carry 126, one of which contradicts its own\n"
        b"83-plus-41 breakdown in the same bullet.\n",

        b"live sites in the ledger carry 126, one of which contradicts its "
        b"own\n83-plus-41 breakdown in the same bullet. (Corrected "
        b"2026-08-11: this\nnote said two; there were three. A fourth sits "
        b"inside a completed-batch\nhistorical record and is correctly left "
        b"alone -- correcting it would\nfalsify the record.)\n",
    ),

    # ---------------- MASTER PLAN ----------------
    (
        PLAN, 'F13 current-HEAD phrase becomes a built-on anchor',
        b"HEAD orrery `ee0da47c` / gallery `61a78c00` -- F1a (M2) fully "
        b"closed: L-149\n",

        b"state as of that work, orrery `ee0da47c` / gallery `61a78c00` -- "
        b"F1a (M2)\nfully closed: L-149\n",
    ),

    # ---------------- README ----------------
    (
        README, 'F14a schematic drops its module count',
        b"|- *.py                          # ~121 Python modules, all at "
        b"root\n",

        b"|- *.py                          # Python modules, all at root "
        b"(count:\n|                                #   MODULE_ATLAS.md, "
        b"generated)\n",
    ),
    (
        README, 'F14b scale paragraph recounted',
        b"noting: 121 Python modules and roughly 92,000 non-blank lines as "
        b"of July\n2026 ",

        b"noting: 118 Python modules and roughly 96,000 non-blank lines as "
        b"of August\n2026 ",
    ),

    # ---------------- DATA INVENTORY ----------------
    (
        INVENTORY, 'F10 header stops claiming the file is gitignored',
        b"# Data Inventory (local, gitignored -- CURRENT state)\n"
        b"\n"
        b"Repo copies stale/absent; this reflects the live local stores.\n",

        b"# Data Inventory (state of the local data stores)\n"
        b"\n"
        b"This FILE is tracked in git. The data DIRECTORIES it describes are\n"
        b"local and not all of them are in the repo, so the tables below can\n"
        b"only be confirmed by re-running the inventory tool on Tony's\n"
        b"machine. Treat them as current as of the generation date, not as\n"
        b"something the repo can verify. (Corrected 2026-08-11: the header\n"
        b"read \"local, gitignored\" while the file was committed and absent\n"
        b"from .gitignore -- a tracked file asserting it was not in the "
        b"repo.)\n",
    ),

    # ---------------- PROTOCOL ----------------
    (
        PROTOCOL, 'F11a PROJECT_ORIGIN pointer (preamble)',
        b"2024; see documentation/PROJECT_ORIGIN.md.) Each shortcut looks "
        b"harmless\n",

        b"2024; see PROJECT_ORIGIN.md at the repo root.) Each shortcut looks "
        b"harmless\n",
    ),
    (
        PROTOCOL, 'F11b PROJECT_ORIGIN pointer (The Origin)',
        b"Full account in Tony's own words: documentation/PROJECT_ORIGIN.md. "
        b"The\n",

        b"Full account in Tony's own words: PROJECT_ORIGIN.md at the repo "
        b"root. The\n",
    ),
    (
        PROTOCOL, 'Stale Skill = Stop gains its two known limits',
        b"The repo is live-readable at any point, so where the loaded and "
        b"expected\nversions agree but there is reason to doubt the repo "
        b"copy, a raw fetch\nsettles it -- the same live read that confirms "
        b"a push.\n",

        GATE_AMENDMENT,
    ),
    (
        PROTOCOL, 'version header -> v3.38',
        b"Tony Quintanilla, PE | Claude | v3.37.1 | August 11, 2026\n",

        b"Tony Quintanilla, PE | Claude | v3.38 | August 11, 2026\n",
    ),
    (
        PROTOCOL, 'version history entry for v3.38',
        b"v.3.37.1 (August 11, 2026): Provenance Discipline skill moved from "
        b"v1.8 to v1.9\n",

        b"v3.37.1 (August 11, 2026): provenance-discipline skill v1.8 -> "
        b"v1.9.\n"
        b"\n"
        b"v3.38 (August 11, 2026): Two changes, both from Fable's\n"
        b"document-layer claim audit. (1) Two dead pointers to\n"
        b"documentation/PROJECT_ORIGIN.md corrected -- the file is at the "
        b"repo\nroot (finding F11). (2) Stale Skill = Stop gains its two "
        b"known limits.\nThe gate is LOAD-TRIGGERED, so a manifest that "
        b"changes later in the same\nsession creates a mismatch with nothing "
        b"to fire on -- which is what\nhappened when provenance-discipline "
        b"went 1.8 to 1.9 mid-session. And a\nmid-session reinstall cannot be "
        b"verified from inside the session: the\nloaded copy appears bound at "
        b"conversation start. Tony's ruling: do NOT\nadd an assertion-based "
        b"clear, because \"Tony reinstalled it\" is a claim\nrather than a "
        b"check, and accepting it in place of a read is\ncite-to-clear moved "
        b"into the skill layer. The verification defers into\nthe handoff and "
        b"is discharged by the next session's load. Skill-layer\ncompanion: "
        b"provenance-discipline v1.9 narrows the push gate to the\nACTIVE "
        b"BUILD PATH (L-184), keeping global Tier-1 = 0 as the destination\n"
        b"rather than the firing rule (finding F1).\n",
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
                 "       NOTHING was written to any of the six files."
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
                  "Nothing written to any file." % (label, count))
            sys.exit(1)
        blobs[rel] = blobs[rel].replace(old, new)
        print("  ok  %s" % label)

    for rel, data in blobs.items():
        with open(os.path.join(here, rel), 'wb') as f:
            f.write(data)

    print()
    print("patch applied")
    for rel, data in sorted(blobs.items()):
        print("  %-56s %7d bytes" % (rel, len(data)))
    print()
    print("NEXT, in this order:")
    print("  1. ledger_index.py        -- regenerate the index zone")
    print("  2. module_atlas.py        -- F8, the atlas describes the")
    print("                               pre-move tree")
    print("  3. provenance_scanner.py  -- F9, the audit still says 119 files")
    print("  4. update the resident project instructions to v3.38 and")
    print("     archive documentation/project_instructions_v3_38.md")
    print("  5. commit")


if __name__ == '__main__':
    main()
