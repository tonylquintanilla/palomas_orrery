# Ruling -- L-345: a computed conversion takes its count from its source row alone

**Built on orrery `714293a901159be25074a95662526e4703cc92fc` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
read live with `git ls-remote` on 2026-09-28 in the session that
wrote this. Gallery `2df02f3baead894ff40922bcadef9cb84c49fa07` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, as
`DESIGN_L345_conversions_computed_20260928.md` states it; this
session did not re-read the gallery.**

**Type: RULING, carried from the Claude Fable 5.1 session to the
Claude Opus 5.5 session that builds `DESIGN_L345_conversions_computed
_20260928.md`.** It changes one part of that design, section 4, and
the parts that depend on it. It does not change the architecture.

**Rules this ran under:** protocol v3.71; provenance-discipline 2.21
(this session's loaded copy reads 2.21, and the repo copy at 714293a9
was diffed against it); ledger-and-session-records 1.11. The
receiving session has the same Project, so no second anchor line is
needed, but section 6 asks for a read-back all the same.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds it.

---

## 1. Tony's rulings, 2026-09-28, in order

1. On L-345: "follow the single source of truth principle. use the
   single best source for the store with provenance. compute all
   conversions instead of duplicating. we should build this
   architecture now. add to the skill if clarification is needed."
2. On the design's section 4, after Fable's review: the conversion
   count rule in section 2 below goes into provenance-discipline 2.22
   as the method, replacing 2.21's "for now" sentence, and the export
   is built to it. Tony's words: "confirmed as recommended." Tony
   asked that this be the skill's method, not his judgment or his eye.

## 2. The rule, for provenance-discipline 2.22

This is the text to place in Rule 3, in the paragraph 2.21 added,
replacing its last two sentences ("Here a place-governed value means a
sum or a difference. A single measured value scaled by an exact row,
which is what the reference page's 8-inch example is, is deliberately
left under the fewest-figures rule for now."). Opus folds it into the
2.22 bump D19 already carries, so one session ships one version of the
skill.

> **A value in another unit is computed, never stored, and its count
> comes from its source row alone** (v2.22). A conversion is not a row
> and has no chain. Its uncertainty is its source row's, scaled by the
> exact factor: the stated uncertainty, where the source's figures
> field has one; otherwise half a unit of the source's last declared
> place; for an exact source, a unit of the last place of its print
> count. The place printed is the power of ten nearest that scaled
> uncertainty on a log scale, a tie going to the coarser, which is the
> Report test under The ceiling. The count is the figures of the
> full-digit value down to that place, and the value is computed from
> the source's full digits and rounded once. The sum rule above is one
> instance of this: a sum's declared place is the place its count
> names. This reads a row's declared precision; it never sets a row's
> ceiling from its chain, so the implied-uncertainty bullet under The
> ceiling stands and Jelinek's bow shock stays 13.5 Earth radii. The
> exception cuts both ways. The chromosphere gains a figure (698,000 km
> at three, 1.003 solar radii at four); the bow shock loses one (13.5
> Earth radii at three, 86,000 km at two, because the source's last
> figure is worth 638 km and "86,200" would claim fifty). A conversion
> whose source row is wrong is fixed at the source row, once. (Tony's
> ruling, 2026-09-28, on Claude Fable 5.1's recommendation; L-345.)

For Rule 8, the checker paragraph 2.21 added is widened in the same
way: the place is found for any derived row that is a source row
scaled only by exact rows, not only for a sum, and the checker prints
the place it found beside the count. The export gives each entry in
`"in"` its count by this rule and no other; the "smaller of counting
and propagation" in the design's section 4 is withdrawn. An exact
source's conversions are exact and carry a `"prints"` count found by
the same place rule (the 200 km LEO floor prints 3, so its value in
Earth radii prints 0.0314).

The design's section 4 heading, "no rule changes", is therefore wrong,
and its section 4 text is replaced by the paragraph above.

## 3. What the rule gives on the 13 rows

Computed in the Fable session against `constants_new.py` at
714293a9, with `EARTH_EQUATORIAL_RADIUS_KM`, `KM_PER_AU` and
`SUN_RADIUS_KM` as the exact factors. "Inherit" is the count the rule
gives; "declared" is the count the conversion row states today.

| Conversion | Source figures | Source uncertainty | Declared | Inherit | Prints as |
|---|---|---|---|---|---|
| EARTH_INNER_CORE_RADII | 5 | -- | 5 | 5 | 0.19151 |
| EARTH_OUTER_CORE_RADII | 5 | -- | 5 | 5 | 0.54561 |
| EARTH_LOWER_MANTLE_RADII | 3 | -- | 3 | 3 | 0.895 |
| EARTH_UPPER_MANTLE_RADII | 5 | -- | 5 | 5 | 0.99506 |
| EARTH_GEOSTATIONARY_RADII | 7 | -- | 7 | 7 | 6.610735 |
| EARTH_LEO_INNER_RADII | 8 (stale, see 4) | -- | 8 | 9 | see 4 |
| EARTH_LEO_OUTER_RADII | 8 (stale, see 4) | -- | 8 | 9 | see 4 |
| EARTH_HILL_SPHERE_RADII | 3 | -- | 3 | 3 | 235 |
| EARTH_MAGNETOPAUSE_STANDOFF_KM | 3 | 0.13 R_E | 2 | 2 | 65,000 |
| EARTH_MAGNETOPAUSE_STANDOFF_AU | 3 | 0.13 R_E | 2 | 2 | 0.00044 |
| EARTH_BOW_SHOCK_STANDOFF_KM | 3 | -- | 3 | 2 | 86,000 |
| EARTH_BOW_SHOCK_STANDOFF_AU | 3 | -- | 3 | 2 | 0.00058 |
| CHROMOSPHERE_PHYSICAL_RADII | 3 | -- | 4 | 4 | 1.003 |

Ten of thirteen match the declared count, and the chromosphere needs
no special case. The three that differ are section 4.

## 4. What changes in the design because of the rule

- **Section 5, the list of hovers that change, is recomputed.** Any
  hover that prints the bow shock's kilometre or AU line moves: the
  kilometre line to 86,000 km at two figures, the AU line to 0.00058.
  The design's promise that nothing else on screen moves held only
  because its count rule reproduced the counting artifact. Opus lists
  every such hover, today and after, before building, as manifest
  section 6 step 5 already requires; Tony checks them on his phone.
- **Section 7, third bullet, is withdrawn.** The magnetopause's 10.3
  Earth radii does not "take 2 figures and print 10". The row's own
  figures line says its 3 comes from the uncertainty 0.13, not from
  counting, and by the Report test 0.13 rounds to tenths: 10.3 implies
  +/- 0.05, 10 implies +/- 0.5, and 0.13 is nearer the first. 10.3
  beside 65,000 km is not an asymmetry; +/- 0.13 Earth radii lands in
  tenths in one unit and in thousands in the other. Both are correct.
- **A new source-row finding, for the ledger.** `EARTH_LEO_INNER_KM`
  and `EARTH_LEO_OUTER_KM` say "Figures: 8 -- set by
  EARTH_EQUATORIAL_RADIUS_KM". Tony ruled on 2026-09-27 that the
  equatorial radius is a definition and exact, and the LEO edges are
  exact rows with print counts (D15). An exact plus an exact is exact,
  so both figures lines are stale and both rows should be exact with a
  print count. Their radii conversions then follow the exact-source
  clause of section 2. Whether this lands in D20 (the rows patch) or
  is recorded is the build's call; it is one class, two instances.
- **Section 8's first choice stands.** The 13 names stay as computed
  aliases with no precision of their own.

## 5. Recorded, not built -- one class

- **The orrery's own hovers that print the 13 names** are a fifth
  consumer of the same numbers (Check All Parallel Pipelines). D20
  checks them byte for byte, which keeps them where they are; they do
  not read the computed count until the orrery prints conversions
  through `constants_rows.py` as the export does. A class for the
  ledger, not this build.

## 6. Read-back

The build session states, in its handoff, which paragraph of 2.22
carries the rule of section 2, and lists the hovers of section 4 that
it found print a bow shock kilometre or AU line. A handoff that names
neither is telling the next session the rule was not placed.

---

Written September 28, 2026 with Anthropic's Claude Fable 5.1, from
the review Tony confirmed.
