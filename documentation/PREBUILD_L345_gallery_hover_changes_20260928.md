# Pre-build note -- L-345 gallery patch: what a visitor will see change

**Built on orrery `807e9dd535211b2bdb91263b49988e1494c308a8` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`2df02f3baead894ff40922bcadef9cb84c49fa07` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
HEADs read live with `git ls-remote` on 2026-09-28. Loaded skills:
provenance-discipline 2.22, interactive-exhibit 1.5 (the handoff's
obligation, discharged). Nothing has been built.

**Type: PRE-BUILD NOTE.** The handoff asked for every changed hover,
today and after, before building. This is that list, measured, and it
is longer than the handoff expected.

## 1. How it was measured

- Today's hovers: built headless from gallery `2df02f3b`'s served cache
  with the page's own renderer.
- After: each printed kilometre, AU or radii number read from the `"in"`
  entry the orrery's export at `807e9dd5` serves for that row, as
  interactive-exhibit 1.5 requires ("a hover prints a unit it is
  served"). Kilometres at the served count; AU at the served count or
  three figures, whichever is fewer (Rule 7's named AU exception).
- Rows D20 has not built yet (the stratopause and thermopause kilometre
  rows) are worked out by provenance-discipline 2.22 Rule 3 and marked
  "expected". They are confirmed when those rows exist.

## 2. The list

| Room | Hover | Today | After | Why |
|---|---|---|---|---|
| Earth | Crust | Radius: 1.0000 Earth radii | Radius: 1 Earth radius | patch 4 |
| Earth | Magnetopause | Bz 0.0 nT, dynamic pressure 2.0 nPa | Bz 0 nT, dynamic pressure 2 nPa | patch 4 |
| Earth | Bow shock | at dynamic pressure 2.0 nPa | at dynamic pressure 2 nPa | patch 4 |
| Earth | Bow shock | 86,200 km (0.000576 AU) | 86,000 km (0.00058 AU) | L-345 ruling |
| Sun | Chromosphere | Radius: 1.002874802357338 solar radii | Radius: 1.003 solar radii | L-345 |
| Sun | Chromosphere | = 697,700 km (0.00466 AU) | = 698,000 km (0.00466 AU) | L-345 |
| Sun | Photosphere | Radius: 1 solar radii | Radius: 1 solar radius | singular at 1 |
| Earth | Magnetotail | 770,000 km (0.0051 AU) | 800,000 km (0.005 AU) | NEW, see 3 |
| Earth | Magnetotail | 380,000 km (0.0026 AU) | 400,000 km (0.003 AU) | NEW, see 3 |
| Earth | Inner radiation belt | = 9,600 km (0.000064 AU) | = 9,600 km (0.00006 AU) | NEW, see 3 |
| Earth | LEO inner edge | Radius: 1.0313571 Earth radii | Radius: 1.03135712 Earth radii | NEW, see 3 |
| Earth | LEO outer edge | Radius: 1.3135712 Earth radii | Radius: 1.31357121 Earth radii | NEW, see 3 |
| Earth | Lower atmosphere | Radius: 1.008 Earth radii | Radius: 1.0078 Earth radii (expected) | NEW, see 3 |
| Earth | Upper atmosphere | Radius: 1.09 Earth radii | Radius: 1.094 Earth radii (expected) | NEW, see 3 |

Every other Earth and Sun hover line holds byte for byte: the interior,
the geocorona, geostationary, the Hill sphere, the outer belt, the
magnetopause's 65,000 km (0.00044 AU), every altitude line, and every
Sun shell outside the chromosphere and photosphere.

## 3. Why the six new rows move

All six are the 2.22 rule doing what the ruling says it does ("the
exception cuts both ways"), in places the design did not examine.

- **Magnetotail and inner belt.** Their hovers multiply a served
  Earth-radii number by Earth's radius to print kilometres
  (`feature_renderers.js` lines 1143 and 2407). That is the conversion
  interactive-exhibit 1.5 forbids. Read from `"in"` instead, they take
  the count their source rows support. The tail's 120 Earth radii
  carries a stated plus or minus 10, which is about 64,000 km, so its
  kilometre figure keeps one figure.
- **LEO edges.** The pointer moves from the Earth-radii conversion row
  (8 figures) to the kilometre row, and the kilometre row's value in
  Earth radii carries 9. The ruling's table already said 9 ("Inherit").
- **Stratopause and thermopause.** Their radii become conversions of
  kilometre sums at D20. 50 km is good to the kilometre and 600 km to
  ten kilometres, so the radii keep ten-thousandths and thousandths,
  as the chromosphere's did.

## 4. The ordering question, with a recommendation

The stratopause and thermopause have no kilometre row until D20, so
their two gallery pointers cannot move yet. Two ways:

- **A.** Gallery patch now with 9 pointers; D20; a second small gallery
  patch for the last 2. Two phone checks, and between D20's push and
  the second gallery patch the two links point at rows the export no
  longer serves.
- **B (recommended).** A small orrery patch first that only ADDS the
  two kilometre rows; then the gallery patch with all 11 pointers; then
  D20 retires the old rows. One phone check covers every change above,
  and no check sits failing between pushes. Cost: one extra orrery
  commit and push before the gallery work.

## 5. A second question, after the first: the three-figure AU line

Rule 7 lets the AU line print three figures when the served count is
longer. With `"in"`, the page would do that by rounding a served value
that is already rounded, which is the rounded intermediate Rule 4
forbids. It can round a tie the wrong way. It already meets one: the
inner core's AU is served as 0.000008165 (four figures); the true value
0.0000081652 rounds to 0.00000817, and the page also prints 0.00000817,
but only because of how the computer stores 8.165 in binary. Today
nothing would catch it going the other way.

This does not change any line in section 2 today. It needs settling
before the build writes the AU code, and it comes after the ordering
question.

---

Written September 28, 2026 with Anthropic's Claude Opus 5.5.
