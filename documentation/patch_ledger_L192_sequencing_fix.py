"""
patch_ledger_L192_sequencing_fix.py -- correct the Bennu/Arrokoth
disposition already written into LEDGER_CONSOLIDATED.md

FOLLOW-UP to patch_ledger_L192_rulings.py, which has already been run.
That patch recorded the Bennu/Arrokoth ruling as "send both back" and
said the leave-in-place option was declined. That was wrong. Tony's
ruling is the sequencing: they STAY until the checker's first run
catches them, and the catch is what routes them back.

Two anchored edits, all-or-nothing. Nothing is written unless every
anchor matches exactly once.

  1. replace the "send both back" paragraph with the sequencing ruling
  2. add the two-dispositions paragraph -- L2 MISMATCH routes to
     conversation, L3 routes to send-back

TARGET: LEDGER_CONSOLIDATED.md (path resolved relative to this script,
so save this file at the REPO ROOT).

Built on 2a7ead883652ff90f0280c8a82fb0c9e40a5d596 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), PLUS
patch_ledger_L192_rulings.py applied. The base fingerprint below is that
combined state; running ledger_index.py in between does not change it,
because the regenerated INDEX zone comes out byte-identical.

RUN: save at the repo root, open in VS Code, click Run.
     Equivalent command line: python patch_ledger_L192_sequencing_fix.py

SUCCESS: one "ok" line per edit, then "patch applied (N bytes)".
FAILURE: a single "ERROR:" or "ANCHOR FAIL" line. Nothing is written
         either way, so it is always safe to re-check and retry.

AFTER RUNNING: python ledger_index.py

Role: patch
Domain: dev_tools

Script created: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'

# md5 of the LF-normalized ledger AFTER patch_ledger_L192_rulings.py
BASE_FP = '93471882add9f11f1148a0c047dd70f3'


EDITS = []

# ---------------------------------------------------------------- 1
EDITS.append((
    b"**RULED 2026-08-13: send both back.** The rule that governs a PARTIAL\n"
    b"row governs a false attribution -- we do not accept and interpret an\n"
    b"answer the evidence does not support. Reopen the session that produced\n"
    b"`worksheet_claude_constants_new.md` and ask it either to perform the\n"
    b"two checks or to state plainly that it did not. Leaving the\n"
    b"annotations standing as a live test fixture for the checker's first\n"
    b"run was considered and declined: a known-false provenance claim held\n"
    b"in the tree to prove a tool works is the thing the tool exists to\n"
    b"prevent.\n",

    b"**RULED 2026-08-13: they stay until the checker's first run, then go\n"
    b"back. Not fixed now.** The rule that governs a PARTIAL row governs a\n"
    b"false attribution -- we do not accept and interpret an answer the\n"
    b"evidence does not support -- so the disposition is return to the\n"
    b"originator: reopen the session that produced\n"
    b"`worksheet_claude_constants_new.md` and ask it either to perform the\n"
    b"two checks or to state plainly that it did not.\n"
    b"\n"
    b"The SEQUENCING is the ruling. The first run should catch both as\n"
    b"examples of an incomplete response, and the catch is what routes\n"
    b"them. Fixing them beforehand would remove the only two known-true\n"
    b"failures in the corpus, and a first run that cannot fail is not a\n"
    b"passing run.\n"
    b"\n"
    b"(Correction of record: this entry first read \"send both back\" and\n"
    b"said the leave-in-place option was declined. That inverted the\n"
    b"ruling. Fixed 2026-08-13 in a follow-up patch.)\n",
))

# ---------------------------------------------------------------- 2
EDITS.append((
    b"Every outcome is confirmed in conversation UNLESS THE RULE IS ALREADY\n"
    b"STATED. That clause is what makes writing an adjudication down worth\n"
    b"the effort: a stated rule settles the next occurrence without a\n"
    b"second conversation.\n"
    b"\n"
    b"**The Hill sphere is the worked example, and it is a convention\n",

    b"Every outcome is confirmed in conversation UNLESS THE RULE IS ALREADY\n"
    b"STATED. That clause is what makes writing an adjudication down worth\n"
    b"the effort: a stated rule settles the next occurrence without a\n"
    b"second conversation.\n"
    b"\n"
    b"**Two dispositions, and the checker names which one.** An L2 MISMATCH\n"
    b"-- a value and its own evidence disagreeing about a number -- routes\n"
    b"to CONVERSATION, because the cause is open. An L3 failure -- an\n"
    b"annotation asserting a completed check over a row that records an\n"
    b"incomplete one -- routes to SEND BACK, because the cause is already\n"
    b"known. `BENNU_RADIUS_KM` and `ARROKOTH_RADIUS_KM` are the worked L3\n"
    b"cases, and demonstrating that route is part of what the first run is\n"
    b"for.\n"
    b"\n"
    b"**The Hill sphere is the worked example, and it is a convention\n",
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
        print('       this patch expects patch_ledger_L192_rulings.py to')
        print('       have run already, and nothing else since')
        print('       nothing written')
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
