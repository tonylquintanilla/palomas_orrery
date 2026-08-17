# Pilot expected dispositions -- 23 rows, constants_new.py

**Built on `98b29f00dbd7e3be235a6f88d615718ccfc397dd` at
https://github.com/tonylquintanilla/palomas_orrery (branch main), WITH
`patch_L195_1_shape_a_swaps.py` applied.** That patch has not been run
yet. Six rows below describe citations that only exist after it runs;
they are marked **[post-swap]**. If the pilot dispatches before the
patch, those six expectations are void.

Type: **PREDICTION.** Written before dispatch, which is the only time
it is worth anything.

Lands in `documentation/`.

---

## What this file is for

The pilot tests the loop, not the constants. A loop test needs a way to
fail, and the failure mode is that everything comes back looking fine.
Twenty-three filled rows, every token in the vocabulary, the checker
routing without complaint -- that is what a working loop produces and
also what a responder pattern-matching the columns produces.

So the expectations go on paper first. Afterward there are three
outcomes per row, and all three teach something:

- **Return matches the expectation.** The loop carried a row whose
  answer we could predict. Weak evidence alone, strong in aggregate.
- **Return contradicts the expectation and the return is right.** The
  prediction was wrong. Best case -- the pilot found something a reading
  did not.
- **Return contradicts the expectation and the return is wrong.** The
  artifact misled a careful reader. This is the finding the pilot exists
  for, and it is invisible without this file.

These are Claude's predictions, unratified. Overrule any row.

---

## Headline prediction

**13 clear, 10 return.** Only CONFIRMED clears -- PARTIAL and APPROX go
back unconditionally by the 2026-08-13 ruling, so a row answered
"approximately right" is a return, not a pass.

If all 23 clear, do not read it as success. Ten of these rows have a
defensible reason to come back, and a sweep of twenty-three
confirmations means the responder agreed with the code rather than
checked it.

---

## The 13 expected to clear

| Row | Value | Authority on the Source line | Why it should clear |
|---|---|---|---|
| `KM_PER_AU` | 149597870.7 | IAU 2012 Res. B2 | Exact by definition |
| `SUN_RADIUS_KM` | 695700.0 | IAU 2015 Res. B3 | Nominal value, exact by definition |
| `EARTH_POLAR_RADIUS_KM` | 6356.752 | IERS Conventions (Petit & Luzum 2010) | Source names the body that publishes the full precision |
| `JUPITER_EQUATORIAL_RADIUS_KM` | 71492.0 | IAU 2015 Res. B3 | Nominal |
| `JUPITER_POLAR_RADIUS_KM` | 66854.0 | IAU 2015 Res. B3 | Nominal |
| `SPEED_OF_LIGHT_KM_S` | 299792.458 | NIST / SI | Exact by definition |
| `ALFVEN_SURFACE_RADII` **[post-swap]** | 18.8 | Kasper et al. (2021), PRL 127:255101 | Measured crossing, stated in the paper |
| `TERMINATION_SHOCK_AU` **[post-swap]** | 94 | Stone et al. (2005), Science 309:2017 | Measured crossing, stated in the paper |
| `HELIOPAUSE_RADII` **[post-swap]** | 26148 | Gurnett et al. (2013), Science 341:1489 | 121.6 AU converted to solar radii |
| `MOON_RADIUS_KM` | 1737.4 | NASA NSSDCA | Published volumetric mean |
| `MARS_RADIUS_KM` | 3396.2 | Archinal et al. 2018 | Published equatorial |
| `SATURN_RADIUS_KM` | 60268 | Archinal et al. 2018 | Published equatorial |
| `URANUS_RADIUS_KM` | 25559 | Archinal et al. 2018 | Published equatorial |
| `NEPTUNE_RADIUS_KM` | 24764 | Archinal et al. 2018 | Published equatorial |

That is fourteen rows, and the count says thirteen. `SUN_RADIUS_KM` is
listed here but appears again below as a trap row: it should clear, and
there is a specific, predictable way for it not to. Counted as a return
in the headline, deliberately -- predicting the safer number would make
the headline unfalsifiable in the direction that matters.

## The 10 expected to return, and what each one tests

**`EARTH_EQUATORIAL_RADIUS_KM` = 6378.137, cited to IAU B3.**
Expect PARTIAL on the citation. B3 publishes 6378.1; the third decimal
comes from IERS, which the block says in a `# Note:` but not in the
Source line. Tests whether a responder verdicts the Source line alone,
as Break 5 requires, or quietly credits the context legs.

**`CHROMOSPHERE_PHYSICAL_KM` = 2000.0, Carroll & Ostlie Ch. 11.**
Expect APPROX. The source says "extends ~2000 km," and a tilde is not a
measurement. Also carries one joined continuation line, so a clean
return proves the join survived the round trip.

**`INNER_CORONA_RADII` = 3, Golub & Pasachoff (2010).**
Expect CONVERSATION. The published extent is 2-3 R_sun and the code
takes the top of the range as a drawing boundary. The question this row
really asks is whether a visualization boundary is verdictable at all --
which is the artifact-bounds question arriving as a worksheet row rather
than as an argument.

**`STREAMER_BELT_RADII` = 6.0 [post-swap], Golub & Pasachoff; DeForest et al.**
Expect PARTIAL, same shape as above: 4-6 R_sun observed, 6.0 chosen.
Two authorities on one Source line -- watch whether the responder
verdicts both or picks one.

**`ROCHE_LIMIT_RADII` = 3.45 [post-swap], Murray & Dermott (1999) Sec. 4.6.**
Expect DERIVED. The authority supports the formula; the number comes
from substituting an assumed cometary density of 500 kg/m3, which no
source publishes for this constant. The most likely row to force leg 6,
and the one whose existing cross-checks say only "formula verified."

**`PARKER_CLOSEST_RADII` = 9.86 [post-swap], the JHUAPL mission page.**
Expect REFUTED or UNSOURCED on the citation. The page reports about 3.8
million km above the surface; the code states 9.86 solar radii from
center. Same orbit, different reference, and the Source line is now a
bare URL with no author or date. Tests whether a URL functions as an
authority at all.

**`BENNU_RADIUS_KM` = 0.246, Nolan et al. 2013 + OSIRIS-REx.**
Expect CONFIRMED, but flagged: the body is 246 metres and the constant
is in kilometres. A responder reporting 246 and calling it a mismatch
has been tripped by units, not by the source.

**`HAUMEA_RADIUS_KM` = 715, JPL SSD (Lockwood et al. 2014).**
Expect CONVERSATION. Three defensible numbers sit in one block: 715
from JPL, 779.5 as the geometric mean of the axes, 870 equatorial. Two
joined continuation lines. If any row produces disagreement between
readers, this is it -- and disagreement here is a property of the body,
not a defect in the worksheet.

**`ARROKOTH_RADIUS_KM` = 9.1, Keane et al. 2022.**
Expect DERIVED or CONFIRMED. The value is an equivalent-sphere radius
computed from a published volume of 3166 km3. Three joined continuation
lines -- the heaviest join in the corpus, so it is the strongest single
test that continuation text arrives intact.

**`SUN_RADIUS_KM` = 695700.0 -- counted as a return, see the trap rows.**

---

## Trap rows: where a wrong answer is predictable and diagnostic

These three carry an anticipated misreading. The block already
addresses each one in a `# Note:` the responder can see. If the
misreading happens anyway, the finding is about the artifact, not the
constant.

| Row | The predictable wrong answer | What it would prove |
|---|---|---|
| `SUN_RADIUS_KM` | Cites the measured photospheric radius, ~696,340 km, and refutes 695700 | The Note distinguishing nominal from measured was not read |
| `HELIOPAUSE_RADII` | Reads Gurnett's 121.6 AU, compares it to 26148, reports a mismatch | The worksheet does not convey the unit of the code value |
| `BENNU_RADIUS_KM` | Reports 246 against a code value of 0.246 | Same defect, at a different scale |

`HELIOPAUSE_RADII` is also the canary. It is on record as
must-not-send-back -- both August checkers found and corrected a real
error in it, so drift there reflects a successful check. If it comes
back as a defect, the finding is in the loop.

---

## How to read the pilot afterward

1. **Count the clears.** Expect 13. Substantially more means agreement
   rather than checking; substantially fewer means the corpus is in
   worse shape than a reading suggests, which is worth knowing.
2. **Check the three trap rows first.** They test the artifact, and
   they are the only rows whose wrong answer is diagnostic on its own.
3. **Check the four join rows** -- chromosphere, Moon, Haumea, Arrokoth
   -- for whether the continuation text arrived intact. Arrokoth is the
   strongest signal at three joined lines.
4. **Then everything else**, against the table above.

---

*Prepared August 17, 2026 with Anthropic's Claude Opus 5. Built on
`98b29f00dbd7e3be235a6f88d615718ccfc397dd` with
`patch_L195_1_shape_a_swaps.py` applied.*
