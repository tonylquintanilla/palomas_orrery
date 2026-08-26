"""
patch_L252_3_handoff.py -- file the 2026-08-25 session handoff.

Run:  save into the repo root (the folder holding constants_new.py),
      open in VS Code, click Run.
      Or:  python patch_L252_3_handoff.py

Built on c00e40068a8d95c7087147788bee3dce402b9207
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery c8c1518b74411338b4debe6611a3d61721c6625b, untouched.

WHAT IT DOES
  Creates ONE new file and edits nothing:

      documentation/HANDOFF_20260825_night_L247_dispatch_and_repair.md

  It refuses rather than overwriting.

WHAT IS PERMANENT
  The handoff. The script is one-shot.

NOTE ON THE ANCHOR
  c00e4006 is where the remote stood when this was written, with three
  patches still queued locally. The handoff says so rather than
  claiming a state it cannot see. The next session's SHA round trip
  settles it against the only thing it can read.

Success: one "ok" line, then "file written".
Failure: a single "ERROR:" line; nothing is written.
"""

import os
import sys

OUT_PATH = os.path.join(
    'documentation', 'HANDOFF_20260825_night_L247_dispatch_and_repair.md')

HANDOFF = """# HANDOFF -- 2026-08-25 (night) -- the L-247 dispatch, and three defects in its repair

**Orrery: `cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd` ->
`c00e40068a8d95c7087147788bee3dce402b9207`**
(https://github.com/tonylquintanilla/palomas_orrery, branch main).
**Gallery: `c8c1518b74411338b4debe6611a3d61721c6625b`, untouched.**
Every SHA read from the live remote. Confirmed HEAD moves, in order:
`cf865ffc`, `9b6f2029`, `cf588f1f`, `8847d6be`, `c00e4006`. One more,
`d4eb552`, appeared only as a tool's own comparison line and was never
read directly -- recorded as partial rather than written out in full.

**Type: DISPATCH, then REPAIR, then REPAIR OF THE REPAIR.** Nine
patches, all orrery-side. No gallery work. **The Earth build did not
start.** Step 1 of the path closed; step 2 is where it stops.

**Three patches were still queued locally when this was written**:
`patch_L251_1`, `patch_L252_1`, `patch_L252_2`. At `c00e4006` the
annotation repair is present and those three are not. Do not assume
they landed -- read the files.

---

## What this session was actually about

It opened as "write L-248 and L-249 into the ledger" and became the
first full turn of the verification loop on a family of constants that
had never been through it. Five values went out, three returns came
back, two rulings settled them, the repair landed -- and then two
checkers reported that the repair's ANNOTATIONS were wrong in three
ways, one of them the exact failure the apparatus exists to catch.

The through-line is narrower than provenance:

**A CHECK THAT REPORTS SUCCESS IS NOT THE SAME AS A CHECK THAT COULD
HAVE REPORTED FAILURE.** Four separate instances in one session, in
four unrelated layers. They are listed in their own section below
because four is not a coincidence, it is a pattern in how this project
verifies things.

---

## What landed

| Patch | Result |
|---|---|
| `patch_L249_1_ledger_rows_248_249.py` | L-248 and L-249 written; blank line before section D restored (a defect `patch_L250_1` left the night before) |
| `patch_L248_1_constants_gate_and_au_yr.py` | `constants_change_report.py` gains a third case, DERIVED; `4.74` in `exoplanet_coordinates.py` derived from `KM_PER_AU` |
| `patch_L247_2_worksheet_request.py` | `REQUEST_L247_sgr_a_constants.md` written, hand-built |
| `patch_L247_3_convergence_report.py` | `CONVERGENCE_L247_sgr_a_constants.md` -- three returns compared |
| `patch_L247_4_repair.py` | Five values sourced and repaired; two new sourced primaries; two new derivations |
| `patch_L247_5_annotation_repair.py` | The three annotation defects, plus an invented label retired. No value moves |
| `patch_L251_1_galactic_center_launcher.py` | The orrery's Galactic Center button stops serving a cached HTML |
| `patch_L252_1_incomplete_outcome.py` | L2b gains a fourth outcome, COMPLETED; suite 134 -> 136 |
| `patch_L252_2_ledger_rows.py` | L-251 and L-252 opened; L-247's Gap becomes its outcome |

Tier-1 findings moved 293 -> 294 -> 292. The rise was three patch
scripts sitting in the repo root, one of which carries a dict of md5
fingerprints; the fall was the L-247 repair.

---

## The four checks that could not fail

Recorded together because the pattern is the finding.

1. **`Constants change` reported "No changes since HEAD" while the gate
   it was meant to run was still broken.** The derived lines it cannot
   parse had moved behind HEAD, so the diff was empty. Green because
   there was nothing to read, not because it could read it.

2. **"Regenerate the Sgr A* views and hover the marker" could not show
   a change.** `show_and_save` writes a TEMP file; the named HTML in
   the repo root is only rewritten through the save dialog. Two Mode 5
   passes returned identical stale numbers and neither was wrong to.
   This was Claude's instruction, and it was the wrong instruction.

3. **The Galactic Center button never regenerated at all** (L-251). It
   opened a permanent HTML if one existed. The first click ever wrote
   that file; every click since served it back. Seven months.

4. **`DRIFTED` fired on a value that had been corrected** (L-252),
   because APPROX was grouped with CONFIRMED. The pin that caught it
   says in its own comment: read this, do not relax it. Reading it was
   the right move and the tool was wrong.

Two more of the same shape, smaller, inside patch scripts:
a post-check searching for `# Cross-checked:` matched Claude's own
prose describing its removal, and a fixture count counted a
pre-existing `**APPROX**` row as this patch's work. Both fired. Both
were the guard working.

---

## Tony's rulings

**Epoch policy, and its refinement.** The most recent publication is
authoritative; the value it replaces is recorded rather than
overwritten. Refined the same evening because the literal reading does
not land: "most recent publication" means the most recent paper that
reports the value AS A RESULT. Two later GRAVITY papers carry mass and
distance as fit parameters while studying something else, and an August
2026 Nature paper on S301 quotes them in passing. Neither supersedes
the 2022 determination. Written into `constants_new.py`'s section
header.

**The solar mass is derived, not corrected.** `GM_SUN_SI` enters as the
sourced primary and `SOLAR_MASS_KG` derives from it. The reason is the
product: the file holds both factors of a quantity the IAU declares
exact, and as two literals their product was 0.030% off it, implicitly,
where nothing watched.

**The fourth L2b outcome exists.** COMPLETED, narrow: INCOMPLETE alone
does not earn it, the code must equal the value that worksheet
supplied.

**The Galactic Center button uses the standard save path.** Temp file
plus an optional dialog, never a permanent file read from the root.

---

## The dispatch, in one place

Five values, three model families, one request that the builder could
not build.

**Why hand-written.** `worksheet_checker.collect_claims()` skips any
unit whose attached text carries no `# Cross-checked:` record. The
corpus is therefore the ALREADY-annotated set: the builder re-checks,
it does not first-check. Measured at `cf865ffc` -- 98 corpus rows, 21
in `constants_new.py`, none of these five among them. There is no tool
path today for a first-time dispatch of an uncited value.

**Unanimous:** G (CODATA 2022, value unchanged), `SOLAR_MASS_KG`
(APPROX, all three giving 1.98841e30), `PARSEC_TO_AU` (a DEFINITION,
648000/pi).

**Split two against one:** the mass and the distance, and not on a
fact. Every leg agreed on what 2019 and 2022 each publish. GPT judged
`Value correct?` against the later measurement and said so at the top
of its return; the other two judged it against the cited one. The v2
vocabulary does not define which. That is a convention gap, and it will
be met again.

**Still owed:** a SECOND cross-check leg on `SGR_A_MASS_SOLAR` and on
`SGR_A_DISTANCE_PC`. Only GPT reached the 2022 value.
`SGR_A_DISTANCE_PC` carries no leg at all -- the name did not exist
when the request went out. Both say so in `# Review-note:` lines.

---

## The path -- unchanged in shape, one step closed

### 1. `patch_L248_1` -- DONE

The gate reads `NAME = EXPR` over tracked names as DERIVED and passes
it. A changed formula still fails. `4.74` derives; the returned
velocity rose 0.0099%.

### 2. L-249 -- the Earth slice of L-181 -- NOT STARTED, and held

Five interior boundary radii move into `constants_new.py` in km with
sources; `shell_configs.py` derives `radius_fraction` from them.

**One question is parked at Tony's instruction and must be settled
before the migration runs.** The two mantle shells disagree with their
own hover prose by far more than the cores do, and whether that is
drift or a declared drawing choice under L-240 is not established.
`lower_mantle` stores 0.85, drawing 5,421 km, against a stated 660 km
depth which is 5,718 km or 0.8965. `upper_mantle` stores 0.98, drawing
6,251 km, against 30 km depth which is 6,348 km or 0.9953. Deriving
would move both spheres. Claude offered to investigate the file history
and the neighbouring bodies and bring evidence rather than the question
cold; Tony said hold. **That offer is still open and is the natural
first move on step 2.**

### 3. L-235's T5 fix with L-237's golden re-cut (gallery-side)

### 4. L-238 -- the `radius_fraction > 1.0` validator (gallery-side)

### 5. Earth's config entries and the interior shell rendering

### 6. The magnetosphere -- a design pass, not a port

### 7. Mode 5, then re-lock

**Steps 3 and 4 are gallery-side and independent.** No gallery work
happened this session; that repo did not move.

---

## Ledger

**Opened:** L-248 (36 sites of `3.26156`), L-249 (Earth boundaries),
L-251 (the cached HTML), L-252 (the fourth outcome).
**Rewritten:** L-247's Gap became its outcome; the row now carries the
dispatch, both rulings, the repair, and the three defects.

L-251 and L-252 score 15.2 and 11.4 in the generated index, above
anything else currently open. Both are already built, which is why.

---

## Corrections to this session's own claims

Left visible rather than restated.

- **"Seven patches."** Nine. Counted in a summary sentence rather than
  from the list.
- **"38 sites of `3.26156`."** Thirty-six, measured at `cf865ffc` by
  counting the literal in tracked `.py` outside `documentation/`. The
  extra two are spent patch scripts that quote it in their own text.
  The eleven modules were right.
- **"The exact quotient is 3.2615675."** 3.2615668 from the store's own
  constants at the time, and 3.2615637772 once `PARSEC_TO_AU` became
  exact. The swept literal 3.26156 is closer to the second.
- **"Regenerating settles it in one step."** It cannot; see the four
  checks above.
- **"Both checkers return to green" (patch_L247_5).** One did. The
  other needed L-252, which did not exist yet. Caught by running it
  before delivery rather than by predicting it.
- **RICE for L-248 stated as 2.6.** The index renders 2.5. The prose
  score is a third copy of a number the metadata holds and the index
  computes; L-247 has already drifted the same way (row says 4.1, index
  says 4.0). Unruled.

---

## Skills

Loaded and matched at session start: `ledger-and-session-records` 1.9,
`safe-file-editing` 1.8, `provenance-discipline` 2.6. No bumps, so no
obligation carried forward.

---

## (do) and (decide) -- Tony-side

- **(do)** Run the three queued patches -- `patch_L251_1`,
  `patch_L252_1`, `patch_L252_2` -- then `ledger_index.py`, then
  `maintenance_run.py`. Any order; they touch different files.
- **(do)** Archive the session's patch scripts to `documentation/`.
  Tier-1 should read 292 with them moved, and each one left in the root
  that carries a fingerprint dict adds one.
- **(do)** Delete `documentation/worksheets/PREVIEW_REQUEST_L247_sgr_a_constants.md`.
  It is a byte-for-byte duplicate of the request, committed by
  accident, and it counts as an uncited worksheet.
- **(do)** Confirm the Galactic Center button regenerates: it should
  pause, open a `tmp*.htm` tab, then offer the save dialog. The old
  `sgr_a_grand_tour.html` in the root is now read by nothing.
- **(decide)** RICE for L-251 (4/4/95/1) and L-252 (3/4/95/1).
- **(decide)** The mantle question in L-249, or accept the offer to
  investigate it first.
- **(decide)** Whether `REQUEST_<batch>.md` should classify as a prompt.
  `worksheet_checker.py` keys on the substring "prompt", so six
  requests the builder itself emitted sit in the uncited count and will
  never leave, because a request is not evidence.
- **(decide)** Whether a row's prose RICE score should exist at all,
  given the index computes it.
- **(open)** The nightly still reports `[RECOVER] could not remove
  retained data\\solar-system.prev (WinError 5)` and quarantines
  instead. Carried from the previous handoff, untouched.

---

## Next session -- first three cheap things

1. SHA round trip: orrery `c00e4006` or later, gallery `c8c1518b`, read
   live. Three patches were queued when this was written, so expect
   HEAD to be ahead.
2. Confirm loaded skill versions against the manifest.
3. Read L-247, L-251 and L-252 in the ledger before touching either
   subject.

Then step 2 of the path, starting with the mantle question.

---

*Session written August 25, 2026 with Anthropic's Claude Opus 5. Orrery
`cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd` to
`c00e40068a8d95c7087147788bee3dce402b9207`; gallery
`c8c1518b74411338b4debe6611a3d61721c6625b`, untouched. All confirmed
against the live remote.*
"""


def fail(msg):
    print('ERROR: ' + msg)
    sys.exit(1)


def main():
    if not os.path.exists('constants_new.py'):
        fail('constants_new.py not found. Run this from the repo root.')
    if not os.path.isdir('documentation'):
        fail('documentation/ does not exist.')
    if os.path.exists(OUT_PATH):
        fail('%s already exists. Refusing to overwrite.' % OUT_PATH)

    payload = HANDOFF.encode('ascii', 'strict')
    bad = sorted({b for b in payload if b > 127})
    if bad:
        fail('non-ASCII byte(s) in the handoff: %r' % bad)
    print('ok  handoff is ASCII-only, %d bytes' % len(payload))

    with open(OUT_PATH, 'wb') as handle:
        handle.write(payload)

    print('file written  %s  (LF)' % OUT_PATH)
    print('')
    print('NEXT: python maintenance_run.py, then commit and push.')


if __name__ == '__main__':
    main()
