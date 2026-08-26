"""
patch_L247_3_convergence_report.py -- file the L-247 convergence report.

Run:  save into the repo root (the folder holding constants_new.py),
      open in VS Code, click Run.
      Or:  python patch_L247_3_convergence_report.py

Built on cf588f1f6e0847653f6493985e5857a908fb0943
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES
    Creates ONE new file and edits nothing:

        documentation/CONVERGENCE_L247_sgr_a_constants.md

    Step 3 of the Batch Worksheet Workflow -- the comparison across the
    three returns that came back on the L-247 request. It refuses
    rather than overwriting.

    It guards on the content fingerprint of all three returns, so the
    report cannot describe worksheets that were edited after it was
    written.

WHAT IT DOES NOT DO
    It does not touch the three returns. Two of them carry non-ASCII
    characters (GPT 42 bytes, Gemini 144). An evidence artifact is
    filed as received; the encoding gate's Fix In Passing conditions
    require a file this patch is already editing, and these are
    evidence, not source.

    It writes no annotation into constants_new.py. Nothing here is a
    repair -- the repairs wait on one ruling, which the report states.

WHAT IS PERMANENT
    The report. The script is one-shot.

Success: three "ok" lines, then "file written".
Failure: a single "ERROR:" line; nothing is written.
"""

import hashlib
import os
import sys

WORKSHEETS = os.path.join('documentation', 'worksheets')
OUT_PATH = os.path.join('documentation',
                        'CONVERGENCE_L247_sgr_a_constants.md')

# Content fingerprints (CRLF normalized to LF) of the three returns
# this report describes.
RETURNS = {
    'worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md':
        'd5471f485630d1408461dcbcf3817efd',
    'worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md':
        '23a403e34cba10d2ccbe8f34ecf2a119',
    'worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md':
        '3cd016d5d2dd78e361a38a37da4cbd77',
}

REPORT = """# Convergence report -- L-247 Sagittarius A* and galactic-scale constants

**Built on `cf588f1f6e0847653f6493985e5857a908fb0943` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Request: `documentation/worksheets/REQUEST_L247_sgr_a_constants.md`,
issued against `cf865ffc`.

Three returns, three model families:

| Leg | File | Bytes |
|---|---|---:|
| Claude Opus 5 | `worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md` | 12029 |
| GPT-5.6-sol | `worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md` | 8058 |
| Gemini 2.5 Pro | `worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md` | 7189 |

Step 3 of the Batch Worksheet Workflow. Nothing here is a repair.

---

## The verdict grid

| # | Constant | Claude | GPT | Gemini |
|---|---|---|---|---|
| 1 | `GRAVITATIONAL_CONSTANT_SI` | YES / UNSOURCED | YES / UNSOURCED | YES / UNSOURCED |
| 2 | `SOLAR_MASS_KG` | APPROX / UNSOURCED | APPROX / UNSOURCED | APPROX / UNSOURCED |
| 3 | `PARSEC_TO_AU` | APPROX / UNSOURCED | APPROX / UNSOURCED | APPROX / UNSOURCED |
| 4 | `SGR_A_MASS_SOLAR` | YES / PARTIAL | **NO / YES** | YES / PARTIAL |
| 5 | `SGR_A_DISTANCE_LY` | APPROX / UNSOURCED | **NO** / UNSOURCED | APPROX / UNSOURCED |

Rows 1, 2 and 3 are unanimous on both verdicts. Rows 4 and 5 split two
against one, and the split is not about the facts.

---

## Arithmetic, recomputed independently

Every number the three legs asserted was recomputed here rather than
carried. All of it closes:

    (GM)_sun^N / G = 1.3271244e20 / 6.67430e-11 = 1.988409870698e30 kg
    at four significant figures                 = 1.988e30, not 1.989e30
    648000 / pi                                 = 206264.80624709636 AU
    206265.0 relative error                     = 9.393e-07
    1 pc in light-years                         = 3.2615637771674
    8178 pc                                     = 26673.07 ly
    8277 pc                                     = 26995.96 ly
    26670.0 ly inverted                         = 8177.06 pc
    G x 1.989e30   = 1.32751827e20, +0.02968% off the IAU-exact GM
    G x 1.98841e30 = 1.32712449e20, +0.000007% off

One small discrepancy inside a leg: Gemini's Findings section writes the
quotient as 1.9884095e30 where the correct value is 1.9884099e30. Its
table cell reads 1.98841e30, which is right. It changes nothing, and it
is recorded because a DERIVED row is complete only when the arithmetic
closes, so an arithmetic slip inside one is worth naming.

---

## Rows 1 to 3 -- converged, repairs ready, blocked only by sequencing

### Row 1, `GRAVITATIONAL_CONSTANT_SI = 6.67430e-11`

No numeric repair. All three legs confirm the code value digit for
digit. The only divergence is which CODATA adjustment to name: Claude
and GPT both cite CODATA 2022 (Mohr, Newell, Taylor & Tiesinga, Rev.
Mod. Phys. 97, 025002, 2025, DOI 10.1103/RevModPhys.97.025002), and
Gemini cites CODATA 2018 (Tiesinga et al., Rev. Mod. Phys. 93, 025010,
2021) while naming both adjustments in the same cell.

That is not a conflict about the number. Claude states that the 2022
adjustment took in no new competitive datum for G, so both adjustments
publish the same central value. Cite 2022 as the current authority.

Relative standard uncertainty 2.2e-05. Two legs note that the bare
literal reads as exact when it is a recommended measured value.

### Row 2, `SOLAR_MASS_KG = 1.989e30`

Unanimous APPROX, unanimous diagnosis, unanimous replacement value.
The solar mass in kilograms is not measured; what is fixed is the
product, (GM)_sun^N = 1.3271244e20 m^3 s^-2 exactly, IAU 2015
Resolution B3, published as Prsa et al. 2016, AJ 152, 41. Divide by the
current G and the answer is 1.98841e30 kg. The code's value is 0.0297%
high.

Claude adds a structural finding neither other leg states outright, and
it is the reason this row matters more than 0.03% usually would.
`constants_new.py` now holds BOTH factors of a product that is known far
better than either factor. Multiplying the file's own two constants
gives 1.32751827e20 against a defined 1.3271244e20 -- so the file
contains a solar gravitational parameter 0.030% off a quantity the IAU
declares exact, implicitly, where nothing watches it.

Two repairs, and they are not equivalent:

  (a) `SOLAR_MASS_KG = 1.98841e30`, which makes the product right to
      five figures and keeps the file's present shape.
  (b) Introduce `GM_SUN_SI = 1.3271244e20` as the primary and derive
      the kilogram value from it, which makes the product exact by
      construction and cannot drift when CODATA next moves G.

Claude and Gemini both name (b) as the better shape; GPT says the
repair should say DERIVED and name both inputs, which is (b) in
substance. **(b) adds a constant to the store, so it is a scope call.**
Under the new DERIVED case in `constants_change_report.py`,
`SOLAR_MASS_KG = GM_SUN_SI / GRAVITATIONAL_CONSTANT_SI` reports its
parents and passes.

### Row 3, `PARSEC_TO_AU = 206265.0`

Unanimous, and unanimous that this is a DEFINITION rather than a
measurement: 1 pc = (648000/pi) au exactly, IAU 2015 Resolution B2,
restated in Prsa et al. 2016. The exact value is 206264.80624709636.
The code is 0.194 au high, relative error 9.39e-07. Two legs note that
the trailing `.0` asserts a tenth-of-an-au precision the number does
not have: the true fourth decimal is 8, not 0.

**This row reaches past L-247 and into L-248, which is the reason to do
it first.** L-248 replaces 36 copies of the literal `3.26156` with
`PARSEC_TO_AU / AU_PER_LIGHT_YEAR`. With the store as it stands that
quotient is 3.2615668. With the exact parsec it is 3.2615638. The
literal being swept, 3.26156, is closer to the second -- relative
1.2e-06 against 2.1e-06. So repairing row 3 makes L-248's derivation
agree BETTER with the 36 values it replaces. Sweeping first would
migrate 36 sites onto a rounding.

Claude also flags a conflict inside the request form itself: the
question list says a defined or derived quantity should be marked as
such, while the paragraph above the table tells rows 1, 2, 3 and 5 to
write `UNSOURCED`. For row 3 those give different answers, and they
describe different objects -- `UNSOURCED` is true of the CODE, `DERIVED`
is true of the QUANTITY. All three legs wrote `UNSOURCED` and two put
"DEFINED" or "derived" in Notes, so the information survived. It is a
vocabulary question, not a defect in any return.

---

## Rows 4 and 5 -- the divergence, and what it actually is

**All three legs agree on every fact.** GRAVITY Collaboration 2019
(A&A 625, L10, DOI 10.1051/0004-6361/201935656) publishes a mass of
4.154 +/- 0.014 e6 M_sun and R_0 = 8178 +/- 13 (stat) +/- 22 (sys) pc.
GRAVITY Collaboration 2022 (A&A 657, L12, DOI
10.1051/0004-6361/202142465) publishes 4.297 e6 M_sun and R_0 = 8277 pc.
Nobody disputes either pair.

The split is that GPT judged `Value correct?` against the later
measurement and the other two judged it against the cited one. GPT
declared this at the top of its return rather than leaving it to be
inferred:

> For measured quantities, `Value correct?` is judged against the best
> later primary measurement I could establish at the review date, not
> merely against whether an older paper once published the code
> literal.

That is a coherent reading, and so is the other one. The request did
not say which, and the v2 vocabulary does not define it. So this is a
FINDING for conversation under the skill's own rule -- three complete
returns that disagree because of a convention gap, not an error in any
of them.

**The ruling that resolves both rows: does the orrery track the most
recent publication, or pin a stated epoch?** Claude and GPT each raised
it independently as a policy question. It is one decision, not two, and
it is worth making once rather than per constant.

Two things travel with whichever way it goes.

**They move together or not at all.** Mass and distance came out of the
same orbit fit of the same star and are strongly correlated -- Claude
cites the paper's own degeneracy along M proportional to R_0 cubed and
its sensitivity of 1.4e3 M_sun per pc; GPT states the same conclusion
independently. Taking a newer distance while keeping an older mass
produces a pair no publication supports, and no single-value check would
catch it, because each number remains individually citable.

**Which column, if 2019 is pinned.** Claude reports that Table 1 has
three columns, that 4.154 belongs to the "Down-sampled data" column
whose R_0 is 8179, and that the headline R_0 = 8178 belongs to the
"Noise model fit" column whose mass is 4.152 -- so the code may have
taken the mass from one column and the distance from another. Gemini
describes 4.154 as the combined orbit and spectroscopic fit, which is a
different account of the same cell. GPT does not address the columns.
This is unresolved between the legs and is the one item that may need a
fourth look.

Two supporting measurements, recomputed here: 26670.0 ly inverts to
8177.06 pc, which matches no column of Table 1 (8175, 8178, 8179); and
8178 pc converts to 26673.07 ly, which rounds to 26670 at four
significant figures. So the code's distance is a rounding of the 2019
headline, not a fourth column.

---

## Findings only one leg raised

- **The implicit GM error (Claude).** Row 2 above. The strongest finding
  in the batch and the only one that changes a rendered quantity beyond
  its own row: every Schwarzschild radius, escape velocity and orbital
  period computed as G x (solar masses x `SOLAR_MASS_KG`) inherits
  0.030%.
- **The closure check that does not discriminate (Claude).** The paper
  publishes an angular Schwarzschild radius of 10.022 microarcsec.
  Recomputing from the code's constants gives 10.0305; recomputing with
  the corrected solar mass gives 10.0275. Both sit inside the paper's
  uncertainty, so the check passes either way and cannot be used to
  argue the code's value is fine. Reported by its own author as a green
  result that answers nothing -- which is the resident gate, applied by
  a leg to its own work.
- **Uncertainty semantics (GPT).** Rows 1, 3, 4 and 5 all carry trailing
  precision the underlying quantity does not support. Row 5 is the worst:
  `.0` asserts 0.1 ly against a real uncertainty near 83 ly, overstated
  by about three orders of magnitude.
- **Independence (Claude, procedural).** The Claude leg notes that the
  request's footer records it was written with Claude Opus 5, and that
  it is Claude Opus 5. No proposal travelled with the request, so the
  answer is independent mechanically, but not across model families.
  With GPT and Gemini also answering, three families are represented and
  the concern does not bind here. It would bind if a future dispatch went
  to two Claudes.

---

## What is due

- **(decide)** Epoch policy: track the latest publication, or pin a
  stated epoch? This resolves rows 4 and 5 together and is the only
  thing blocking the repair patch.
- **(decide)** Row 2's repair shape: (a) correct the literal to
  1.98841e30, or (b) introduce `GM_SUN_SI` and derive. (b) adds a
  constant to the store.
- **(do)** `documentation/worksheets/PREVIEW_REQUEST_L247_sgr_a_
  constants.md` is a duplicate of `REQUEST_L247_sgr_a_constants.md`,
  byte for byte. It was a preview copy and should not have been
  committed. Deleting it removes one entry from the worksheet checker's
  uncited count.

Rows 1 to 3 need no ruling except row 2's shape and can be repaired in
the same patch as 4 and 5. All five sit in one block of one file, so one
patch is the right unit.

---

*Report written August 25, 2026 with Anthropic's Claude Opus 5, against
`cf588f1f6e0847653f6493985e5857a908fb0943`. Ledger: L-247.*
"""


def fail(msg):
    print('ERROR: ' + msg)
    sys.exit(1)


def main():
    if not os.path.exists('constants_new.py'):
        fail('constants_new.py not found. Run this from the repo root.')
    if not os.path.isdir(WORKSHEETS):
        fail('%s does not exist.' % WORKSHEETS)
    if os.path.exists(OUT_PATH):
        fail('%s already exists. Refusing to overwrite.' % OUT_PATH)

    for name in sorted(RETURNS):
        path = os.path.join(WORKSHEETS, name)
        if not os.path.exists(path):
            fail('%s not found. The report describes it.' % path)
        with open(path, 'rb') as handle:
            data = handle.read()
        got = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
        if got != RETURNS[name]:
            print('ERROR: %s has changed since the report was written.' % name)
            print('  expected content fingerprint %s' % RETURNS[name])
            print('  found                        %s' % got)
            print('  The report would describe a worksheet that moved.')
            sys.exit(1)
        print('ok  return unchanged  %s' % name)

    payload = REPORT.encode('ascii', 'strict')
    bad = sorted({b for b in payload if b > 127})
    if bad:
        fail('non-ASCII byte(s) in the report: %r' % bad)

    with open(OUT_PATH, 'wb') as handle:
        handle.write(payload)

    print('file written  %s  %d bytes  (LF)' % (OUT_PATH, len(payload)))
    print('')
    print('The three returns were NOT touched. Two carry non-ASCII')
    print('characters (GPT 42 bytes, Gemini 144) and are left as')
    print('received: an evidence artifact is filed as it arrived.')
    print('')
    print('No annotation was written into constants_new.py. The repair')
    print('waits on the epoch ruling the report states.')


if __name__ == '__main__':
    main()
