"""
patch_ledger_L192_rulings.py -- record the L-192 fork rulings in the ledger

Two anchored edits to LEDGER_CONSOLIDATED.md, all-or-nothing. Nothing is
written unless every anchor matches exactly once.

  1. the L-192 "Still open for Tony (decide)" list closes -- all three
     were ruled 2026-08-13
  2. new subsection: Forks ruled, 2026-08-13 -- DERIVED, no propose
     mode, the mismatch route. Includes the disposition for the two
     false attributions and one new (do) item for Pluto's shell text.

TARGET: LEDGER_CONSOLIDATED.md (path resolved relative to this script,
so save this file at the REPO ROOT).

Built on 2a7ead883652ff90f0280c8a82fb0c9e40a5d596 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

RUN: save at the repo root, open in VS Code, click Run.
     Equivalent command line: python patch_ledger_L192_rulings.py

SUCCESS: one "ok" line per edit, then "patch applied (N bytes)".
FAILURE: a single "ERROR:" or "ANCHOR FAIL" line. Nothing is written
         either way, so it is always safe to re-check and retry.

AFTER RUNNING: python ledger_index.py
     (regenerates the INDEX zone; L-192 stays OPEN)

Role: patch
Domain: dev_tools

Script created: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'

# md5 of the LF-normalized base content this patch was written against
BASE_FP = '0bfcddaa81e2f0f8d92c8ac65305373a'


EDITS = []

# ---------------------------------------------------------------- 1
EDITS.append((
    b"**Still open for Tony (decide):**\n"
    b"1. Does a QUALIFIED verdict (PARTIAL, APPROX) earn a leg? Fable's\n"
    b"   middle: never by token class, only by explicit per-row ruling\n"
    b"   recorded in `provenance_exceptions.json` and visible in the audit.\n"
    b"   Deliberately deferred to a fresh session -- a day spent inside the\n"
    b"   Oort case biases this toward the strict answer.\n"
    b"2. Fork 3, the propose mode.\n"
    b"3. `BENNU_RADIUS_KM` and `ARROKOTH_RADIUS_KM` -- see below.\n",

    b"**Still open for Tony (decide): none.** All three were ruled\n"
    b"2026-08-13; see the forks-ruled section below. Fable's middle answer\n"
    b"on QUALIFIED -- per-row rulings recorded in\n"
    b"`provenance_exceptions.json` -- was NOT taken. The ruling is simpler\n"
    b"and needs no store.\n",
))

# ---------------------------------------------------------------- 2
EDITS.append((
    b"will surface both mechanically on its first run. Tony (decide): remove,\n"
    b"reattribute, or annotate. Rule added to provenance-discipline v2.1.\n"
    b"\n"
    b"#### [L-190] Scanner reach: anything rendered must be reachable\n",

    b"will surface both mechanically on its first run. Rule added to\n"
    b"provenance-discipline v2.1.\n"
    b"\n"
    b"**RULED 2026-08-13: send both back.** The rule that governs a PARTIAL\n"
    b"row governs a false attribution -- we do not accept and interpret an\n"
    b"answer the evidence does not support. Reopen the session that produced\n"
    b"`worksheet_claude_constants_new.md` and ask it either to perform the\n"
    b"two checks or to state plainly that it did not. Leaving the\n"
    b"annotations standing as a live test fixture for the checker's first\n"
    b"run was considered and declined: a known-false provenance claim held\n"
    b"in the tree to prove a tool works is the thing the tool exists to\n"
    b"prevent.\n"
    b"\n"
    b"##### Forks ruled, 2026-08-13: DERIVED, no propose mode, the mismatch route\n"
    b"\n"
    b"Skill consequence: provenance-discipline 2.1 -> 2.2, five edits,\n"
    b"pushed with this entry. The rulings are Tony's; the reasoning is the\n"
    b"session record.\n"
    b"\n"
    b"**Fork 2 -- what counts as a completed check. PARTIAL and APPROX\n"
    b"return to the originator for completion**, unconditionally and\n"
    b"without first asking why the row is qualified. Neither earns a leg\n"
    b"toward the cross-checked rung and neither is interpreted into one.\n"
    b"This is the August 13 rule -- we do not have to accept and interpret\n"
    b"incomplete or malformed answers -- applied to the verdict vocabulary\n"
    b"rather than only to unreadable worksheets. Fable's middle answer,\n"
    b"per-row exceptions in `provenance_exceptions.json`, is declined: it\n"
    b"stores a judgement where the simpler move is to get a better\n"
    b"worksheet.\n"
    b"\n"
    b"**DERIVED is not a third member of that family.** It answers the\n"
    b"CITATION question, not the value question -- no source publishes the\n"
    b"number because the number is computed, so there is nothing for that\n"
    b"column to be right about. It can pair with any value verdict,\n"
    b"including NO. The pre-design's classification table put DERIVED\n"
    b"beside PARTIAL and APPROX as though all three qualified a value.\n"
    b"Measured against the corpus that is wrong, and wrong in a way that\n"
    b"would have returned complete derivations while letting incomplete\n"
    b"ones through.\n"
    b"\n"
    b"**A DERIVED row is COMPLETE when it names its inputs, shows the\n"
    b"arithmetic, and the arithmetic closes.** Then L-158 governs: the\n"
    b"derivation logic has cleared its own check and the value inherits the\n"
    b"rung of its weakest input. Not a completed check on its own -- it\n"
    b"hands the question to the premise. Worked case, the Moon's Hill\n"
    b"sphere in lunar radii: 60,000 / 1737.4 = 34.53 closes exactly over a\n"
    b"60,000 km premise that reads APPROX and UNSOURCED, so the derived\n"
    b"figure is worth that and no more. A DERIVED row showing no work is\n"
    b"incomplete and goes back like any other.\n"
    b"\n"
    b"**Fork 3 -- the checker does not write.** No `--propose` argument.\n"
    b"Proposed annotations are discussed in conversation before anything is\n"
    b"written. Fable recommended a propose mode emitting a patch script for\n"
    b"review; the mode itself is declined, not merely its safeguards. The\n"
    b"backfill of the 27 happens in conversation, which is also where the\n"
    b"adjudications get made.\n"
    b"\n"
    b"**A complete row that disagrees is a FINDING, not a defective\n"
    b"worksheet.** This is the correction that changed the design.\n"
    b"Send-back fires on INCOMPLETENESS; it does not fire on DISAGREEMENT.\n"
    b"A row that names its inputs and shows its arithmetic has already\n"
    b"given everything needed to settle the question, so returning it asks\n"
    b"for what we already hold. A mismatch is therefore reported loudly and\n"
    b"routed to conversation, with no cause assigned by any tool. Three\n"
    b"outcomes, none of them the default:\n"
    b"\n"
    b"- CONVENTION MISMATCH -- both derivations correct, answering\n"
    b"  different questions; the code must say which question it answers.\n"
    b"- THE CODE'S NUMBER IS WRONG -- the worksheet wins, the value moves.\n"
    b"- THE WORKSHEET'S DERIVATION IS WRONG -- the code wins.\n"
    b"\n"
    b"Every outcome is confirmed in conversation UNLESS THE RULE IS ALREADY\n"
    b"STATED. That clause is what makes writing an adjudication down worth\n"
    b"the effort: a stated rule settles the next occurrence without a\n"
    b"second conversation.\n"
    b"\n"
    b"**The Hill sphere is the worked example, and it is a convention\n"
    b"mismatch.** The standard Hill radius carries an eccentricity factor,\n"
    b"a(1-e)(m/3M)^(1/3), so what it returns is the PERIHELION Hill radius.\n"
    b"Checkers computing at semimajor axis dropped the (1-e): for Eris at\n"
    b"e~0.44 that gives 14.2 Mkm against 8.0 Mkm, which reads as a gross\n"
    b"error and is not one. Nobody did bad arithmetic. This is Tony's\n"
    b"reading and it corrected this session's first pass, which had filed\n"
    b"both Eris and Pluto as live value errors.\n"
    b"\n"
    b"Eris is already resolved in the tree and shows the recording shape:\n"
    b"the shell text names both figures and says the shell draws\n"
    b"perihelion, so the next checker who computes 14.3 Mkm reads the\n"
    b"answer before raising it. **Pluto is the same case half-finished.**\n"
    b"Its `# Source:` comments name perihelion 29.66 AU and the\n"
    b"Pluto-Charon system GM, and `radius_fraction` 5041 is consistent with\n"
    b"them -- but the hover text and tooltip a reader actually sees say\n"
    b"only \"approximately 5.99 million kilometers\" with no basis at all.\n"
    b"**(do)** Apply the Eris fix to Pluto's reader-facing text, in both\n"
    b"`pluto_visualization_shells.py` and `shell_configs.py`.\n"
    b"\n"
    b"**An adjudication is recorded with its reason, in the place the next\n"
    b"reader will hit it.** Two shapes already work here: the reader-facing\n"
    b"text for a convention, and a `# Corrected:` line in the comment block\n"
    b"for a changed value -- Pluto's block carries one recording that\n"
    b"`radius_fraction` 4685 drew a 5.57 Mkm shell under text claiming 5.99\n"
    b"Mkm. A verdict with no reason is not an adjudication; it is the same\n"
    b"run repeated later by somebody who does not know it already happened.\n"
    b"\n"
    b"**Method note.** The DERIVED reading came from reading the rows, not\n"
    b"from the token list. They split three ways: arithmetic on the\n"
    b"project's own premise, a formula applied to external inputs, and\n"
    b"inference from a measurement -- \"high density implies a largely rocky\n"
    b"composition\" -- which is not derivation at all. Two worksheets also\n"
    b"write a compound token, `DERIVED -- verified`, which the vocabulary\n"
    b"does not contain. The token was carrying more than one job because\n"
    b"nothing had ever defined it.\n"
    b"\n"
    b"#### [L-190] Scanner reach: anything rendered must be reachable\n",
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
    print('NEXT: python ledger_index.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
