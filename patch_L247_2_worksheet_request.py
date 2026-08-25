"""
patch_L247_2_worksheet_request.py -- write the L-247 cross-check request.

Run:  save into the repo root (the folder holding constants_new.py),
      open in VS Code, click Run.
      Or:  python patch_L247_2_worksheet_request.py

Built on cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES
    Creates ONE new file and edits nothing:

        documentation/worksheets/REQUEST_L247_sgr_a_constants.md

    It refuses rather than overwriting if that name already exists,
    which is worksheet_request_builder.py's own rule.

WHY THIS IS HAND-WRITTEN AND NOT BUILT BY THE BUILDER
    worksheet_request_builder.py builds over the ANNOTATED corpus.
    worksheet_checker.collect_claims() skips any unit whose attached
    text carries no `# Cross-checked:` record, so a value with no
    annotation is not in the corpus and the builder cannot mint a key
    for it. Measured at cf865ffc: 98 rows in the corpus, 21 of them in
    constants_new.py, and none of these five among them.

    So this request carries NO Key column. Minting keys by hand outside
    worksheet_keys.py is the failure the builder's own docstring names
    -- a key born stale, minted correctly and unresolvable forever.
    These five enter the keyed corpus when they carry annotations,
    which is what this dispatch exists to produce.

WHAT IS PERMANENT
    The request file. The script is one-shot.

AFTER THIS RUN
    Send the file to two models independently (Claude and GPT is the
    default two-leg pattern). It carries no Claude proposal, so it is
    one dispatch per model, not two.

Success: one "ok" line, then "file written".
Failure: a single "ERROR:" line; nothing is written.
"""

import os
import sys

OUT_DIR = os.path.join('documentation', 'worksheets')
OUT_NAME = 'REQUEST_L247_sgr_a_constants.md'

SHA = 'cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd'
REPO = 'https://github.com/tonylquintanilla/palomas_orrery'

# Sanity anchors: the request must describe the code it claims to
# describe. Each of these must appear in constants_new.py exactly once,
# or the request is being written against a file that already moved.
CODE_ANCHORS = (
    b'GRAVITATIONAL_CONSTANT_SI = 6.67430e-11',
    b'SOLAR_MASS_KG = 1.989e30',
    b'PARSEC_TO_AU = 206265.0',
    b'SGR_A_MASS_SOLAR = 4.154e6',
    b'SGR_A_DISTANCE_LY = 26670.0',
)

REQUEST = """# Cross-check request -- L-247 Sagittarius A* and galactic-scale constants

**Built on `cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Vocabulary: v2 (2026-08-13)

Worksheet type: VALUE VERIFICATION, with first-time sourcing. Four of
the five rows carry no citation at all, so the job is to establish one
rather than to confirm one.

Expected return filename, per the L-206 convention:

    worksheet_<model>-<version>_L247_sgr_a_constants_<YYYYMMDD>.md

Underscores separate fields, hyphens live inside a field, the date is
last. Add a trailing letter to the date if a day repeats.

---

## What these values are

Five constants in `constants_new.py`, migrated there on 2026-08-25 from
`sgr_a_star_data.py`. The migration moved them without changing them.
Only one arrived carrying any attribution, and that one names no paper,
DOI or table.

Two related constants in the same block are NOT in this request because
they are derived from values that are already cited: `SPEED_OF_LIGHT_M_S`
and `M_PER_AU`.

## The question, for every row

1. Is the number right? Give your own value and the primary source that
   publishes it, with enough detail to find the exact statement -- paper,
   year, DOI, table or page, or the specific data page for an agency
   source.
2. At what precision does the source publish it, and does the code's
   precision overstate that?
3. **If the quantity is DEFINED or DERIVED rather than measured, say so
   and show the arithmetic.** Some of these may not have a source to
   cite because no source publishes them as numbers -- they follow from
   a definition. That is a legitimate answer and it changes the repair,
   so do not force a citation onto a value that has none to give. A
   derivation is complete when it names its inputs, shows the work, and
   the arithmetic closes.
4. If you cannot establish a value or a source, write UNVERIFIED and say
   in Notes what stopped you. An honest UNVERIFIED is a usable answer.

## Two things deliberately withheld

Each of these constants carries a `# Review-note:` comment written by an
earlier session. Those notes are not reproduced here, because two of them
characterize where the value probably comes from and this request is for
an independent look. Ask if you want them after you have answered.

No Claude proposal travels with this request. Nothing below states what
anyone expects the answer to be.

## Response table

Fill `Your value`, `Your source`, `Value correct?`, `Citation correct?`
and `Notes`. Do not edit `Constant` or `Code value`: they record what the
code said at the SHA above.

Verdict tokens -- exactly one per cell, nothing else, reasoning in Notes:

    Value correct?     YES  NO  APPROX  UNVERIFIED
    Citation correct?  YES  NO  PARTIAL  DERIVED  UNSOURCED  UNVERIFIED

`Value correct?` asks whether the number is right. `Citation correct?`
asks whether the source NAMED IN THE CODE publishes it. They are separate
questions and a right number under a wrong authority is value-YES and
citation-NO.

Rows 1, 2, 3 and 5 name no source in the code, so there is nothing there
for the citation verdict to be right about: write `UNSOURCED`, and put
what you found in `Your source`. Row 4 is the only row where the citation
question is live.

| # | Constant | Code value | Code's source line | Your value | Your source | Value correct? | Citation correct? | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | `GRAVITATIONAL_CONSTANT_SI` -- Newtonian constant of gravitation | 6.67430e-11 m^3 kg^-1 s^-2 | none | | | | | |
| 2 | `SOLAR_MASS_KG` -- mass of the Sun | 1.989e30 kg | none | | | | | |
| 3 | `PARSEC_TO_AU` -- astronomical units per parsec | 206265.0 AU | none | | | | | |
| 4 | `SGR_A_MASS_SOLAR` -- mass of Sagittarius A* | 4.154e6 solar masses | `# Source: GRAVITY Collaboration 2019` | | | | | |
| 5 | `SGR_A_DISTANCE_LY` -- distance to Sagittarius A* | 26670.0 light-years | none | | | | | |

Row 4's source line is quoted verbatim and is the whole of it. It names
no paper, DOI or table, so part of that row is identifying which
publication is meant, if any single one is.

## Findings section

Below the table, in prose: anything that does not fit a verdict cell. A
value that is right for a reason different from the one the code implies,
a source that publishes a range where the code carries a point, a unit or
epoch mismatch, a definition that changed between editions.

## What happens to this

Two models answer this independently, without seeing each other's return.
A human compares them. Disagreement between the two returns is a FINDING,
not an error to reconcile before sending back.

Nothing here becomes a `# Cross-checked:` annotation automatically. A
returned verdict is evidence; what lands in the code is a separate edit,
made in conversation, that cites this worksheet by filename.

---

*Request written August 25, 2026 with Anthropic's Claude Opus 5, against
`cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd`. Ledger: L-247.*
"""


def fail(msg):
    print('ERROR: ' + msg)
    sys.exit(1)


def main():
    if not os.path.exists('constants_new.py'):
        fail('constants_new.py not found. Run this from the repo root.')
    if not os.path.isdir(OUT_DIR):
        fail('%s does not exist.' % OUT_DIR)

    target = os.path.join(OUT_DIR, OUT_NAME)
    if os.path.exists(target):
        fail('%s already exists. Refusing to overwrite -- an existing '
             'request may already be out with a responder.' % target)

    # The request describes five specific lines. If any of them is not
    # where this says it is, the request is wrong before it is sent.
    with open('constants_new.py', 'rb') as handle:
        code = handle.read().replace(b'\r\n', b'\n')
    for anchor in CODE_ANCHORS:
        count = code.count(anchor)
        if count != 1:
            fail('constants_new.py carries %d copies of %r, expected 1. '
                 'The request would describe a file that moved.'
                 % (count, anchor.decode('ascii')))
    print('ok  all 5 constants found exactly once in constants_new.py')

    payload = REQUEST.encode('ascii', 'strict')
    bad = sorted({b for b in payload if b > 127})
    if bad:
        fail('non-ASCII byte(s) in the request: %r' % bad)

    with open(target, 'wb') as handle:
        handle.write(payload)

    print('file written  %s  %d bytes  (LF)' % (target, len(payload)))
    print('')
    print('EXPECT ONE NEW LINE IN THE NEXT WORKSHEET CHECK')
    print('  worksheet_checker.py counts a file in worksheets/ as a')
    print('  prompt only when its NAME contains "prompt", and as an')
    print('  uncited worksheet otherwise. This one is named for the')
    print('  builder convention, REQUEST_<batch>.md, so the next run')
    print('  will read "now uncited: %s"' % OUT_NAME)
    print('  and the pending-wiring count goes 25 -> 26.')
    print('  The six REQUEST_constants_new_pilot_* files the builder')
    print('  itself emitted are already in that same bucket, and a')
    print('  request will never be cited, because a request is not')
    print('  evidence. Reported rather than worked around: the two')
    print('  conventions genuinely disagree and that is a ruling.')
    print('')
    print('NEXT')
    print('  Send it to two models independently. Claude + GPT is the')
    print('  default two-leg pattern; Gemini is the escalation when both')
    print('  come back UNVERIFIED on a book citation.')
    print('  It carries no Claude proposal, so it is ONE dispatch per')
    print('  model. The two-dispatch rule does not apply here.')
    print('')
    print('  Returns are filed in documentation/worksheets/ under the')
    print('  L-206 name the request header states.')


if __name__ == '__main__':
    main()
