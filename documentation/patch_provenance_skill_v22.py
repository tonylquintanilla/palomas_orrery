"""
patch_provenance_skill_v22.py -- provenance-discipline SKILL.md 2.1 -> 2.2

Five anchored edits, all-or-nothing. Nothing is written unless every
anchor matches exactly once.

  1. version line 2.1 -> 2.2, SHA lineage rolled forward
  2. v2.2 changelog paragraph
  3. DERIVED defined in the verdict vocabulary; "ran out of session"
     replaced with plain wording
  4. send-back clause split: incompleteness returns, PARTIAL/APPROX
     return unconditionally
  5. new subsection -- A Complete Row That Disagrees Is a Finding

TARGET: skills/provenance-discipline/SKILL.md (path resolved relative to
this script, so save this file at the REPO ROOT).

Built on 6b99acec3d980c9de7e1770ef752d82a54c01db8 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

RUN: save at the repo root, open in VS Code, click Run.
     Equivalent command line: python patch_provenance_skill_v22.py

SUCCESS: one "ok" line per edit, then "patch applied (N bytes)".
FAILURE: a single "ERROR:" or "ANCHOR FAIL" line. Nothing is written
         either way, so it is always safe to re-check and retry.

AFTER RUNNING, two steps this script does NOT do:
  1. python skills_index.py PROJECT_INSTRUCTIONS.md
     (regenerates the manifest table; the version bump is not done
     until the manifest agrees, and both files commit together)
  2. reinstall the skill to your account: Settings > Skills
     (the account copy is the one a session actually loads)

Role: patch
Domain: dev_tools

Script created: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = os.path.join('skills', 'provenance-discipline', 'SKILL.md')

# md5 of the LF-normalized base content this patch was written against
BASE_FP = 'c8636a2fe692d9f7bed75ea9a388867d'


EDITS = []

# ---------------------------------------------------------------- 1
EDITS.append((
    b"Skill version: 2.1 | Cut from palomas_orrery @ 00219d9 (v2.1), earlier\n"
    b"@ eb77c83 (v2.0), @ cdcdb4b (v1.9), @ 8e4b5ca (v1.8) | August 13, 2026\n",

    b"Skill version: 2.2 | Cut from palomas_orrery @ 6b99ace (v2.2), earlier\n"
    b"@ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9) | August 13, 2026\n",
))

# ---------------------------------------------------------------- 2
EDITS.append((
    b"produced the evidence can be reopened to finish the job.\n"
    b"\n"
    b"The resident protocol carries the two governing principles as CRITICAL\n",

    b"produced the evidence can be reopened to finish the job.\n"
    b"\n"
    b"v2.2 (August 13, 2026) defines DERIVED, which v2.1 listed in the\n"
    b"verdict vocabulary without ever saying what it meant, and separates\n"
    b"two things the send-back rule had run together. A row that is\n"
    b"INCOMPLETE goes back to its originator. A row that is COMPLETE and\n"
    b"disagrees with the code is a FINDING and comes to conversation,\n"
    b"because the disagreement may be a convention mismatch rather than an\n"
    b"error in either place. Earned August 13 on the Eris and Pluto Hill\n"
    b"sphere rows, where checkers computing at semimajor axis disagreed\n"
    b"with code computing at perihelion and nobody had done bad\n"
    b"arithmetic. Tony's rulings: PARTIAL and APPROX return\n"
    b"unconditionally, and an adjudication is recorded with its reason so\n"
    b"the next run does not re-raise it.\n"
    b"\n"
    b"The resident protocol carries the two governing principles as CRITICAL\n",
))

# ---------------------------------------------------------------- 3
EDITS.append((
    b"PARTIAL means the claim is genuinely half-right -- a source that\n"
    b"publishes the value at lower precision than the code carries.\n"
    b"\"I ran out of session\" is UNVERIFIED, and the Notes say what blocked\n"
    b"it. An honest UNVERIFIED is a usable answer; a PARTIAL standing in for\n"
    b"one is not.\n",

    b"PARTIAL means the claim is genuinely half-right -- a source that\n"
    b"publishes the value at lower precision than the code carries.\n"
    b"A checker that STOPPED BEFORE FINISHING writes UNVERIFIED, and the\n"
    b"Notes say what blocked it: a context limit, a paywalled paper, a\n"
    b"conversation that ended. An honest UNVERIFIED is a usable answer; a\n"
    b"PARTIAL standing in for one is not.\n"
    b"\n"
    b"DERIVED answers the CITATION question, not the value question. It\n"
    b"means no source publishes this number because the number is computed,\n"
    b"so there is no citation for that column to be right about. It can\n"
    b"pair with any value verdict, including NO. Reading it as a third\n"
    b"member of the PARTIAL/APPROX family is the error to avoid: those two\n"
    b"qualify a value, DERIVED describes where one came from.\n"
    b"\n"
    b"A DERIVED row is COMPLETE when it names its inputs, shows the\n"
    b"arithmetic, and the arithmetic closes. Then L-158 governs: the\n"
    b"derivation logic has cleared its own check, and the value inherits\n"
    b"the rung of its WEAKEST INPUT. That is not a completed check on its\n"
    b"own -- it hands the question to the premise. Worked example, the\n"
    b"Moon's Hill sphere in lunar radii: 60,000 / 1737.4 = 34.53 closes\n"
    b"exactly, and the 60,000 km premise under it reads APPROX and\n"
    b"UNSOURCED, so the derived figure is worth precisely that and no\n"
    b"more. A DERIVED row showing no work is incomplete and goes back.\n",
))

# ---------------------------------------------------------------- 4
EDITS.append((
    b"**Incomplete or malformed evidence is sent back, not interpreted.**\n"
    b"[Tony's ruling, August 13, 2026.] If a worksheet is prose a tool cannot\n"
    b"read, or its verdict is PARTIAL because the checker ran out of session\n"
    b"rather than because the claim is half-right, the answer is a better\n"
    b"worksheet -- not a cleverer parser and not a charitable reading.\n",

    b"**Incomplete or malformed evidence is sent back, not interpreted.**\n"
    b"[Tony's ruling, August 13, 2026.] If a worksheet is prose a tool\n"
    b"cannot read, or a row shows no work, the answer is a better worksheet\n"
    b"-- not a cleverer parser and not a charitable reading.\n"
    b"\n"
    b"**PARTIAL and APPROX return to the originator for completion.**\n"
    b"[Tony's ruling, August 13, 2026.] Unconditionally, and without first\n"
    b"asking why the row is qualified. Neither token earns a leg toward the\n"
    b"cross-checked rung, and neither is interpreted into one.\n",
))

# ---------------------------------------------------------------- 5
EDITS.append((
    b"Ask for a NEW file rather than an edit. The original worksheet is the\n"
    b"record of what was known on its date, and rewriting it makes it assert\n"
    b"something it did not say at the time.\n"
    b"For derived values where the source is a computation, not a lookup:\n",

    b"Ask for a NEW file rather than an edit. The original worksheet is the\n"
    b"record of what was known on its date, and rewriting it makes it assert\n"
    b"something it did not say at the time.\n"
    b"\n"
    b"#### A Complete Row That Disagrees Is a Finding [CRITICAL]\n"
    b"\n"
    b"Send-back fires on incompleteness. It does NOT fire on disagreement.\n"
    b"A row that names its inputs and shows its arithmetic has already\n"
    b"given everything needed to settle the question; returning it asks for\n"
    b"what we already hold and discards a usable finding.\n"
    b"\n"
    b"So a mismatch between a value and its own evidence is reported LOUDLY\n"
    b"and routed to conversation. No tool assigns the cause. Three outcomes\n"
    b"are live and none of them is the default:\n"
    b"\n"
    b"- CONVENTION MISMATCH. Both derivations are arithmetically correct\n"
    b"  and answer different questions. Nobody is wrong; the code has to\n"
    b"  say which question it answers.\n"
    b"- THE CODE'S NUMBER IS WRONG. The worksheet wins; the value changes.\n"
    b"- THE WORKSHEET'S DERIVATION IS WRONG. The code wins.\n"
    b"\n"
    b"**Every outcome is confirmed in conversation unless the rule is\n"
    b"already stated** [Tony's ruling, August 13, 2026]. A stated rule\n"
    b"settles the next occurrence without a second conversation, which is\n"
    b"the whole reason for writing it down.\n"
    b"\n"
    b"The Hill sphere is the worked example, and it is a convention\n"
    b"mismatch. The standard Hill radius carries an eccentricity factor,\n"
    b"a(1-e)(m/3M)^(1/3), so what it returns is the PERIHELION Hill radius.\n"
    b"Checkers computing at semimajor axis dropped the (1-e) and got a\n"
    b"larger number: for Eris at e~0.44 that is 14.2 Mkm against 8.0 Mkm,\n"
    b"which reads as a gross error and is not one.\n"
    b"\n"
    b"**The adjudication is recorded with its reason, in the place the next\n"
    b"reader will hit it.** Two shapes already work in this codebase:\n"
    b"\n"
    b"- For a convention, the reader-facing text. Eris's shell text now\n"
    b"  states both figures and says the shell draws perihelion, so the\n"
    b"  next checker who computes 14.3 Mkm reads the answer before raising\n"
    b"  it.\n"
    b"- For a changed value, a `# Corrected:` line in the comment block\n"
    b"  saying what moved and why. Pluto's block carries one recording that\n"
    b"  radius_fraction 4685 drew a 5.57 Mkm shell under text claiming\n"
    b"  5.99 Mkm.\n"
    b"\n"
    b"A verdict with no reason is not an adjudication. It is the same run\n"
    b"repeated later by somebody who does not know it already happened.\n"
    b"\n"
    b"For derived values where the source is a computation, not a lookup:\n",
))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print('ERROR: target not found: %s' % path)
        print('       save this script at the repo root and run it there')
        return 1

    with open(path, 'rb') as handle:
        data = handle.read()

    normalized = data.replace(b'\r\n', b'\n')
    fingerprint = hashlib.md5(normalized).hexdigest()
    if fingerprint != BASE_FP:
        print('ERROR: base moved -- expected %s, found %s'
              % (BASE_FP, fingerprint))
        print('       nothing written; re-anchor the patch before retrying')
        return 1

    is_crlf = data.count(b'\r\n') > 0

    # dry pass -- every anchor must match exactly once before anything writes
    for index, (old, _new) in enumerate(EDITS, start=1):
        probe = old.replace(b'\n', b'\r\n') if is_crlf else old
        count = data.count(probe)
        if count != 1:
            print('ANCHOR FAIL: edit %d expected 1 match, got %d' % (index, count))
            print('             first line: %s' % old.split(b'\n')[0][:64])
            print('             nothing written')
            return 1

    for index, (old, new) in enumerate(EDITS, start=1):
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        data = data.replace(old, new, 1)
        print('ok   edit %d' % index)

    with open(path, 'wb') as handle:
        handle.write(data)

    print('patch applied (%d bytes)' % len(data))
    print('')
    print('NEXT: python skills_index.py PROJECT_INSTRUCTIONS.md')
    print('      then reinstall the skill under Settings > Skills')
    return 0


if __name__ == '__main__':
    sys.exit(main())
