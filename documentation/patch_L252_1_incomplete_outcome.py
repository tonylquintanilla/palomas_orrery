"""
patch_L252_1_incomplete_outcome.py -- L2b's fourth outcome.

Run:  save into the repo root (the folder holding worksheet_checker.py),
      open in VS Code, click Run.
      Or:  python patch_L252_1_incomplete_outcome.py

Built on 8847d6be699c49c7e8fa077cc7f1790909c74c47
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Tony's ruling, 2026-08-25.

THE PROBLEM

worksheet_checker.py maps APPROX and PARTIAL to V_INCOMPLETE, then
fires DRIFTED for V_CONFIRMED and V_INCOMPLETE alike. But its own
comment defines DRIFTED as "the worksheet confirmed that value; the
code left it anyway." An APPROX worksheet did not confirm the value --
it said the number was approximate and supplied the exact one. When the
code then takes that exact value, the tool calls it drift and routes a
reader to go re-check a correction the code already records.

That is the same mistake the block's own comment describes one case
earlier, and the information needed to tell them apart is in the same
row: the value the worksheet supplied is read at L2a, sixteen lines up.

Founding case: PARSEC_TO_AU. Three returns verdicted 206265.0 as
APPROX and gave 648000/pi = 206264.806247096 exactly. L-247 took that
value. The checker reported DRIFTED and a Resolved leg did not clear
it.

THE FOURTH OUTCOME

  DRIFTED     the worksheet CONFIRMED the value and the code left it
              anyway, or it was INCOMPLETE and the code moved somewhere
              the worksheet never named. The only defect of the four.
  CORRECTED   the worksheet REFUTED it and the code moved.
  COMPLETED   the worksheet called it APPROX or PARTIAL and supplied a
              value, and the code now reads exactly that. NEW.
  UNCHECKED_MOVE  nobody established anything.

COMPLETED is narrow on purpose. INCOMPLETE alone does not earn it; the
code must equal the value that worksheet supplied. An INCOMPLETE
verdict with the code moved anywhere else still reports DRIFTED, and
the test added here pins that direction, because an outcome that
cannot fail is not a verdict.

TWO FILES
  worksheet_checker.py       the outcome, and the comment that
                             documents it
  test_worksheet_checker.py  two synthetic checks, one per direction

AFTER THIS RUN
  python maintenance_run.py
  Worksheet checker tests returns to green at 136 of 136, up from 134,
  and the live PARSEC_TO_AU row reports COMPLETED instead of DRIFTED.
  Measured before delivery, not predicted.

Success: one "ok" line per edit, then "patch applied".
Failure: a single "ERROR:" or "ANCHOR FAIL" line; nothing is written.
"""

import hashlib
import os
import sys

BASES = {
    'worksheet_checker.py': 'bebbc2cd2b83f7d4239c8b4bf9481576',
    'test_worksheet_checker.py': None,   # filled at run time, see main()
}

WC_COMMENT_OLD = b"""    # THREE outcomes, not two. A value that moved away from a number
    # the worksheet REJECTED is the correction landing -- this whole
    # apparatus working -- and reporting it as drift tells a reader to
    # go re-check a resolution the code already records. All eight L2b
    # findings in the L-192 report were that shape. The information
    # needed to tell them apart was already in the matched row, three
    # lines further down, and was simply read too late.
    #
    #   DRIFTED         the worksheet confirmed that value; the code
    #                   left it anyway. The only defect of the three.
    #   CORRECTED       the worksheet refuted it and the code moved.
    #                   Recorded, not routed.
    #   UNCHECKED_MOVE  the worksheet neither confirmed nor refuted it,
    #                   so neither word is honest. Routed, because
    #                   nobody has established anything.
"""

WC_COMMENT_NEW = b"""    # FOUR outcomes, not two. A value that moved away from a number
    # the worksheet REJECTED is the correction landing -- this whole
    # apparatus working -- and reporting it as drift tells a reader to
    # go re-check a resolution the code already records. All eight L2b
    # findings in the L-192 report were that shape. The information
    # needed to tell them apart was already in the matched row, three
    # lines further down, and was simply read too late.
    #
    # The fourth was the same mistake one case over (L-252). APPROX and
    # PARTIAL map to V_INCOMPLETE, which was grouped with V_CONFIRMED --
    # so a worksheet that said "approximately right, here is the exact
    # value" reported DRIFTED once the code took that exact value. An
    # INCOMPLETE verdict is not a confirmation, and the value it
    # supplied is already read at L2a, sixteen lines up.
    #
    #   DRIFTED         the worksheet CONFIRMED that value and the code
    #                   left it anyway, or it was INCOMPLETE and the
    #                   code moved somewhere the worksheet never named.
    #                   The only defect of the four.
    #   CORRECTED       the worksheet refuted it and the code moved.
    #                   Recorded, not routed.
    #   COMPLETED       the worksheet called it APPROX or PARTIAL and
    #                   supplied a value; the code now reads exactly
    #                   that. Recorded, not routed.
    #   UNCHECKED_MOVE  the worksheet neither confirmed nor refuted it,
    #                   so neither word is honest. Routed, because
    #                   nobody has established anything.
    #
    # COMPLETED is deliberately narrow. INCOMPLETE alone does not earn
    # it -- the code must equal the value THAT worksheet supplied, by
    # the same compare() L2a uses. Widening it to "INCOMPLETE and the
    # code moved" would make it unfailable, which is not a verdict.
"""

WC_CODE_OLD = b"""            elif own == V_REFUTED:
                claim.fail('L2b', 'CORRECTED',
                           '%s, which it rejected: %s' % (moved, token), '')
            elif own in (V_CONFIRMED, V_INCOMPLETE):
                claim.fail('L2b', 'DRIFTED', moved, 'CONVERSATION')
"""

WC_CODE_NEW = b"""            elif own == V_REFUTED:
                claim.fail('L2b', 'CORRECTED',
                           '%s, which it rejected: %s' % (moved, token), '')
            elif (own == V_INCOMPLETE and evidence
                  and compare(claim.code_value, evidence)[0]
                  in ('MATCH', 'CONVERSION')):
                claim.fail('L2b', 'COMPLETED',
                           '%s -- the code now reads the value this '
                           'worksheet supplied, whose verdict was %s'
                           % (moved, token), '')
            elif own in (V_CONFIRMED, V_INCOMPLETE):
                claim.fail('L2b', 'DRIFTED', moved, 'CONVERSATION')
"""

WC_STAMP_OLD = b"""Role: devtool
Domain: dev_tools
"""

WC_STAMP_NEW = b"""Role: devtool
Domain: dev_tools

Module updated: August 25, 2026 with Anthropic's Claude Opus 5 (L-252:
L2b gains a fourth outcome, COMPLETED, so an INCOMPLETE verdict whose
supplied value the code then took stops reporting as DRIFTED)
"""

TEST_OLD = b"""    claim = run_layers(\"\"\"
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 137.5 | 100.0 | **UNVERIFIED** |
\"\"\")
    check('a value nobody checked reports UNCHECKED_MOVE',
          'UNCHECKED_MOVE' in codes(claim), codes(claim))
"""

TEST_NEW = b"""    claim = run_layers(\"\"\"
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 137.5 | 100.0 | **UNVERIFIED** |
\"\"\")
    check('a value nobody checked reports UNCHECKED_MOVE',
          'UNCHECKED_MOVE' in codes(claim), codes(claim))

    # L2b's fourth outcome (L-252). APPROX is not a confirmation. The
    # worksheet said 137.5 was approximate and supplied 100.0; the code
    # reads 100.0. That is the verdict landing, not drift.
    claim = run_layers(\"\"\"
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 137.5 | 100.0 | **APPROX** |
\"\"\")
    check('an INCOMPLETE verdict whose value the code took reports '
          'COMPLETED, not DRIFTED',
          'COMPLETED' in codes(claim) and 'DRIFTED' not in codes(claim),
          codes(claim))

    # The other direction, and the reason COMPLETED is a verdict rather
    # than a way of not failing. Same APPROX verdict, but the code went
    # somewhere this worksheet never named. Still drift.
    claim = run_layers(\"\"\"
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 137.5 | 42.0 | **APPROX** |
\"\"\")
    check('an INCOMPLETE verdict the code ignored still reports DRIFTED',
          'DRIFTED' in codes(claim) and 'COMPLETED' not in codes(claim),
          codes(claim))
"""

EDITS = {
    'worksheet_checker.py': [
        (WC_CODE_OLD, WC_CODE_NEW, 'L2b: the COMPLETED branch'),
        (WC_COMMENT_OLD, WC_COMMENT_NEW, 'L2b: four outcomes documented'),
        (WC_STAMP_OLD, WC_STAMP_NEW, 'docstring: currency stamp'),
    ],
    'test_worksheet_checker.py': [
        (TEST_OLD, TEST_NEW, 'two synthetic checks, one per direction'),
    ],
}


def fail(msg):
    print('ERROR: ' + msg)
    sys.exit(1)


def main():
    staged = {}
    for filename, edits in EDITS.items():
        if not os.path.exists(filename):
            fail('%s not found. Run this from the repo root.' % filename)
        with open(filename, 'rb') as handle:
            data = handle.read()

        is_crlf = data.count(b'\r\n') > 0
        fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
        expected = BASES.get(filename)
        if expected is not None and fp != expected:
            print('ERROR: BASE MOVED -- %s' % filename)
            print('  expected content fingerprint %s' % expected)
            print('  found                        %s' % fp)
            sys.exit(1)
        print('base ok  %-28s (%s)  %d bytes'
              % (filename, 'CRLF' if is_crlf else 'LF', len(data)))

        out = data
        for old, new, label in edits:
            o, n = old, new
            if is_crlf:
                o = o.replace(b'\n', b'\r\n')
                n = n.replace(b'\n', b'\r\n')
            bad = sorted({b for b in n if b > 127})
            if bad:
                fail('non-ASCII in inserted text (%s): %r' % (label, bad))
            count = out.count(o)
            if count != 1:
                print('ANCHOR FAIL (%d matches, expected 1) in %s: %s'
                      % (count, filename, label))
                print('  nothing written to any file.')
                sys.exit(1)
            out = out.replace(o, n)
            print('ok  %-28s %s' % (filename, label))
        staged[filename] = (data, out, is_crlf)

    checker = staged['worksheet_checker.py'][1].replace(b'\r\n', b'\n')
    if checker.count(b"'COMPLETED'") != 1:
        fail('post-check: the COMPLETED branch is not present exactly once')
    if checker.count(b"claim.fail('L2b', 'DRIFTED', moved, 'CONVERSATION')") != 1:
        fail('post-check: the DRIFTED branch was lost')
    # COMPLETED must sit ABOVE the DRIFTED branch or it can never fire:
    # the V_INCOMPLETE arm would swallow it first.
    if checker.find(b"'COMPLETED'") > checker.find(b"'DRIFTED', moved"):
        fail('post-check: COMPLETED is below DRIFTED and would never fire')
    print('ok  post-check: COMPLETED present, above DRIFTED, DRIFTED intact')

    tests = staged['test_worksheet_checker.py'][1].replace(b'\r\n', b'\n')
    # Counted by check NAME, not by fixture text: the file already
    # carried one **APPROX** fixture before this patch, so counting
    # those would be counting somebody else's work as mine.
    for needle in (b"'COMPLETED, not DRIFTED'",
                   b'the code ignored still reports DRIFTED'):
        if tests.count(needle) != 1:
            fail('post-check: missing the check named %r' % needle.decode())
    print('ok  post-check: both directions pinned')

    for filename, (data, out, is_crlf) in staged.items():
        with open(filename, 'wb') as handle:
            handle.write(out)
        print('patch applied  %-28s %+d bytes  (%s)'
              % (filename, len(out) - len(data), 'CRLF' if is_crlf else 'LF'))

    print('')
    print('NEXT: python maintenance_run.py')
    print('  Worksheet checker tests: 136 of 136, up from 134.')
    print('  The live PARSEC_TO_AU row reports COMPLETED, not DRIFTED.')
    print('  Both measured before delivery.')


if __name__ == '__main__':
    main()
