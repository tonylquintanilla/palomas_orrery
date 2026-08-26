"""
patch_L252_2_ledger_rows.py -- L-251, L-252, and L-247's outcome.

Run:  save into the repo root (the folder holding LEDGER_CONSOLIDATED.md),
      open in VS Code, click Run.
      Or:  python patch_L252_2_ledger_rows.py

Built on c00e40068a8d95c7087147788bee3dce402b9207
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES
  1. Rewrites L-247's Gap. The dispatch it was waiting on happened:
     three returns, two rulings, a repair, and three defects in that
     repair. The row said "the dispatch" and that is now history.
  2. Opens L-251 -- the galactic centre launcher serving a cached HTML.
  3. Opens L-252 -- L2b's fourth outcome, COMPLETED.

  Both new rows go at the end of section A, immediately after L-249.

AFTER THIS RUN, in order:
  1. python ledger_index.py
  2. python maintenance_run.py

Success: one "ok" line per edit, then "patch applied".
Failure: a single "ERROR:" or "ANCHOR FAIL" line; nothing is written.
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'
BASE_FP = '86f135440784e651c664f34608231fba'


# ----------------------------------------------------------------------
# Edit 1 -- L-247's Gap becomes its outcome.
# ----------------------------------------------------------------------

L247_OLD = b"""**Gap:** the dispatch. Seven values, six with no source and one with a
lead. This is the verification loop applied to a family that was
previously invisible to it, because the values sat in a module the
worksheet builder does not reach.
"""

L247_NEW = b"""- **The dispatch ran, 2026-08-25.** Five values went out as
  `REQUEST_L247_sgr_a_constants.md` and three returns came back --
  Claude Opus 5, GPT-5.6-sol, Gemini 2.5 Pro. Compared in
  `documentation/CONVERGENCE_L247_sgr_a_constants.md`.
- **The builder could not build the request, and the reason is
  structural.** `worksheet_checker.collect_claims()` skips any unit
  whose attached text carries no `# Cross-checked:` record, so the
  corpus is the ALREADY-annotated set and the builder re-checks rather
  than first-checks. Measured at `cf865ffc`: 98 corpus rows, 21 of them
  in `constants_new.py`, none of these five among them. The request was
  hand-written with no Key column, because minting keys outside
  `worksheet_keys.py` produces a key born stale.
- **Rows 1-3 came back unanimous.** G confirmed digit for digit
  (CODATA 2022). `SOLAR_MASS_KG` APPROX in all three, all three giving
  1.98841e30 from the IAU-exact `(GM)_sun` over the current G.
  `PARSEC_TO_AU` a DEFINITION, 648000/pi, in all three.
- **Rows 4-5 split two against one, on a convention gap rather than a
  fact.** Every leg agreed that GRAVITY 2019 publishes 4.154e6 and
  8178 pc and that GRAVITY 2022 publishes 4.297e6 and 8277 pc. GPT
  judged `Value correct?` against the later measurement and declared
  that at the top of its return; the other two judged it against the
  cited one. The v2 vocabulary does not say which, so this was a
  FINDING for conversation.
- **Tony's ruling, 2026-08-25 (epoch policy).** The most recent
  publication is authoritative and the value it replaces is recorded
  rather than overwritten. Refined in the same breath, because the
  literal reading does not land anywhere: "most recent publication"
  means the most recent paper that reports the value AS A RESULT. There
  are at least two later GRAVITY papers (A&A 692 A242 in 2024, A&A 701
  89 in 2025) that carry mass and distance as fit parameters while
  studying something else, and an August 2026 Nature paper on S301 that
  quotes the figures in passing. None supersedes the 2022 determination.
  Written into the section header of `constants_new.py`.
- **Tony's ruling, 2026-08-25 (the solar mass).** Introduce
  `GM_SUN_SI = 1.3271244e20` as the sourced primary and DERIVE the
  kilogram value, rather than correcting the literal. The reason is the
  product: this file holds both factors of a quantity the IAU declares
  exact, and carried as two literals their product was 1.32751827e20
  against a defined 1.3271244e20 -- 0.030% off, implicitly, where
  nothing watched it. Derived, it is exact by construction.
- **What landed** (`patch_L247_4_repair.py`): G sourced, value
  unchanged; `GM_SUN_SI` and `SGR_A_DISTANCE_PC` added as sourced
  primaries; `SOLAR_MASS_KG` and `SGR_A_DISTANCE_LY` derived from them;
  `PARSEC_TO_AU` to its exact definitional value; `SGR_A_MASS_SOLAR`
  4.154e6 -> 4.297e6. Tier-1 fell 294 -> 292. Mode 5 confirms the hover
  reads 4.297 million solar masses and 26,996 light-years.
- **Three defects in that repair, caught by two checkers, not by
  reading.** 32 unmarked continuation lines; four missing `# Resolved:`
  legs; and a `# Cross-checked:` line on `SGR_A_DISTANCE_PC` naming a
  worksheet whose row is about `SGR_A_DISTANCE_LY` -- an annotation
  asserting a check never performed on that name, written by the patch
  closing exactly that failure class. A fourth found while fixing them:
  `# Superseded:` is not a label; the registry knows twelve and that
  was an invented thirteenth. All four repaired in
  `patch_L247_5_annotation_repair.py`, which moves no value and asserts
  that by fingerprinting all seven assignments.
**Gap:** a SECOND cross-check leg on `SGR_A_MASS_SOLAR` and on
`SGR_A_DISTANCE_PC`. Both carry one. Only GPT reached the 2022 value;
the Claude return noted a successor exists without giving its numbers,
and the Gemini return gave the 2022 distance in prose but not the mass.
`SGR_A_DISTANCE_PC` carries NO leg at all, because the name did not
exist when the request went out. Both are stated in the code as
`# Review-note:` rather than smoothed over.
- **Note:** the value verdict on rows 4 and 5 is the ONE place where
  three complete returns disagreed. Recorded here because the next
  dispatch on this family will meet it again.
"""


# ----------------------------------------------------------------------
# Edit 2 -- L-251 and L-252, at the end of section A.
# ----------------------------------------------------------------------

ANCHOR_OLD = b"""`HANDOFF_20260825_evening_singularity_thread.md` step 2.

## PENDING ACTION (Tony-side)
"""

ANCHOR_NEW = b"""`HANDOFF_20260825_evening_singularity_thread.md` step 2.

#### [L-251] The galactic centre button served a cached HTML for seven months
<!-- L:251 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/95/1 -->
- **Found by Mode 5, and only because the number it showed was wrong in
  a way that could be dated.** On 2026-08-25 the Sgr A* hover read
  4.154 million solar masses after the L-247 repair had moved it to
  4.297. Two regenerations did not change it.
- **The mechanism.** `launch_galactic_center()` in `palomas_orrery.py`
  opened a permanent `sgr_a_grand_tour.html` from the repo root IF ONE
  EXISTED, and generated only when it did not. So the first click ever
  wrote that file and every click after served it back, unchanged,
  forever. Nothing in that path looks at the code again.
- **A parallel pipeline, in the exact shape the protocol names.**
  `sgr_a_grand_tour.py`'s own `__main__` already called
  `show_and_save`, which writes a temp copy, opens THAT, and offers a
  save dialog. One figure, two entry points, different behaviour, only
  one of them current.
- **The rendered value carried its own date stamp.** The hover's
  Schwarzschild radius read 12,271,267 km. The constants in force the
  day before give 12,271,442 -- a 175 km gap, relative 1.4e-05. That
  figure is reproduced to the kilometre by `AU_TO_METERS = 1.496e11`, a
  rounded astronomical unit the code no longer holds. The file was
  written in January 2026 and had survived every constant change since.
  A wrong number turned out to be a timestamp.
- **The verification instruction was itself a check that could not
  fail.** "Regenerate and hover the marker" cannot show a change in a
  file the regeneration does not write. Two Mode 5 passes returned the
  same stale numbers and neither was wrong to.
- **The fix** (`patch_L251_1_galactic_center_launcher.py`, Tony's
  ruling 2026-08-25): the launcher generates every time and hands the
  figure to `show_and_save`. The stale-file branch is DELETED rather
  than corrected, so there is nothing left to go stale.
**Gap:** confirm by clicking Galactic Center in the orrery -- it should
pause to generate, open a `tmp*.htm` tab, then offer the save dialog.
The old `sgr_a_grand_tour.html` may still be in the repo root; nothing
reads it now, and deleting it is Tony's call.
- **Note:** worth a sweep for the same shape elsewhere. A grep of
  `palomas_orrery.py` at `8847d6be` found no other launcher with an
  `os.path.exists(...) -> open` branch, but that grep was one file.
- **Note:** RICE 4/4/95/1 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-247 (the constants whose change it hid); Check All Parallel
Pipelines [CRITICAL]; Verify Execution, Not Appearance [CRITICAL];
Observation Override (Tony's eyes won twice here).

#### [L-252] L2b's fourth outcome: an INCOMPLETE verdict is not a confirmation
<!-- L:252 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/95/1 -->
- **Found by the pin that exists to be read.** After the L-247 repair,
  `test_worksheet_checker.py` failed with `no live claim is called
  DRIFTED without a value verdict -- got: ['PARSEC_TO_AU']`. That
  check's own comment says a DRIFTED here means a real defect is being
  reported: read it, do not relax it.
- **Reading it.** `worksheet_checker.py` maps APPROX and PARTIAL to
  `V_INCOMPLETE`, then fires DRIFTED for `V_CONFIRMED` and
  `V_INCOMPLETE` alike -- while its own comment defines DRIFTED as "the
  worksheet confirmed that value; the code left it anyway." An APPROX
  worksheet did not confirm anything. It said the number was
  approximate and supplied the exact one. Three returns verdicted
  206265.0 APPROX and gave 648000/pi; L-247 took that value; the tool
  called it drift. A `# Resolved:` leg does not clear it -- that is a
  separate mechanism.
- **The same mistake the block already fixed one case over.** Its
  comment records that all eight L-192 findings were corrections
  reported as drift, and that "the information needed to tell them
  apart was already in the matched row." It is here too, in the
  supplied-value column, read at L2a sixteen lines up.
- **The fix** (`patch_L252_1_incomplete_outcome.py`, Tony's ruling
  2026-08-25): a fourth outcome, COMPLETED -- the worksheet called it
  APPROX or PARTIAL and supplied a value, and the code now reads
  exactly that. Recorded, not routed.
- **Narrow on purpose, and pinned in both directions.** INCOMPLETE
  alone does not earn COMPLETED; the code must equal the value THAT
  worksheet supplied, by the same `compare()` L2a uses. An APPROX
  verdict where the code moved somewhere the worksheet never named
  still reports DRIFTED. Two synthetic checks, one per direction, take
  the suite 134 -> 136. Widening it to "INCOMPLETE and the code moved"
  would have made it unfailable, which is not a verdict.
**Gap:** none in the tool. Whether the four outcomes want a matching
line in provenance-discipline's verdict vocabulary is unruled --
COMPLETED is a checker outcome, not a worksheet token, and the two
vocabularies have stayed separate so far.
- **Note:** RICE 3/4/95/1 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-192 (the three outcomes this extends); L-247 (the founding
case); A Check That Cannot Fail Is Not Passing [CRITICAL].

## PENDING ACTION (Tony-side)
"""

EDITS = [
    (ANCHOR_OLD, ANCHOR_NEW, 'insert [L-251] and [L-252] at the end of section A'),
    (L247_OLD, L247_NEW, 'L-247: the Gap becomes the outcome'),
]


def fail(msg):
    print('ERROR: ' + msg)
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail('%s not found. Run this from the folder that holds it.' % TARGET)

    with open(TARGET, 'rb') as handle:
        data = handle.read()

    is_crlf = data.count(b'\r\n') > 0
    norm = data.replace(b'\r\n', b'\n')
    fp = hashlib.md5(norm).hexdigest()
    if fp != BASE_FP:
        print('ERROR: BASE MOVED.')
        print('  expected content fingerprint %s' % BASE_FP)
        print('  found                        %s' % fp)
        sys.exit(1)
    print('base ok  %-24s (%s)  %d bytes'
          % (TARGET, 'CRLF' if is_crlf else 'LF', len(data)))

    for token in (b'[L-251]', b'[L-252]', b'L:251', b'L:252'):
        if token in norm:
            fail('%r already present -- this patch has already run.'
                 % token.decode())

    inserted = ANCHOR_NEW + L247_NEW
    bad = sorted({b for b in inserted if b > 127})
    if bad:
        fail('non-ASCII byte(s) in inserted text: %r' % bad)
    print('ok  encoding gate: inserted text is ASCII-only')

    start = norm.find(b'<!-- INDEX:START')
    end = norm.find(b'<!-- INDEX:END -->')
    if start < 0 or end < 0:
        fail('INDEX marker zone not found')
    index_before = norm[start:end]

    out = data
    for old, new, label in EDITS:
        o, n = old, new
        if is_crlf:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = out.count(o)
        if count != 1:
            print('ANCHOR FAIL (%d matches, expected 1): %s' % (count, label))
            print('  nothing written.')
            sys.exit(1)
        out = out.replace(o, n)
        print('ok  %s' % label)

    out_norm = out.replace(b'\r\n', b'\n')
    for token, want in ((b'#### [L-251]', 1), (b'#### [L-252]', 1),
                        (b'<!-- L:251 ', 1), (b'<!-- L:252 ', 1),
                        (b'\n## PENDING ACTION (Tony-side)\n', 1)):
        got = out_norm.count(token)
        if got != want:
            fail('post-check: %r appears %d time(s), expected %d'
                 % (token, got, want))
    # L-247 must still have exactly one Gap line, and it must be the new
    # one. A row with two Gaps, or with the old wording surviving, is
    # this patch half-applied.
    l247 = out_norm.split(b'#### [L-247]', 1)[1].split(b'#### [L-248]', 1)[0]
    if l247.count(b'**Gap:**') != 1:
        fail('post-check: L-247 carries %d Gap lines, expected 1'
             % l247.count(b'**Gap:**'))
    if b'**Gap:** the dispatch.' in l247:
        fail('post-check: L-247 still carries the old Gap wording')
    print('ok  post-check: two new rows, and L-247 has exactly one Gap')

    s2 = out_norm.find(b'<!-- INDEX:START')
    e2 = out_norm.find(b'<!-- INDEX:END -->')
    if out_norm[s2:e2] != index_before:
        fail('post-check: the generated INDEX zone changed -- it must not')
    print('ok  post-check: generated INDEX zone byte-identical')

    if is_crlf and out.count(b'\n') != out.count(b'\r\n'):
        fail('post-check: mixed line endings introduced')
    print('ok  post-check: line endings preserved (%s)'
          % ('CRLF' if is_crlf else 'LF'))

    with open(TARGET, 'wb') as handle:
        handle.write(out)
    print('patch applied to %s  %+d bytes  (%s)'
          % (TARGET, len(out) - len(data), 'CRLF' if is_crlf else 'LF'))
    print('')
    print('NEXT, in order:')
    print('  1. python ledger_index.py')
    print('  2. python maintenance_run.py')


if __name__ == '__main__':
    main()
