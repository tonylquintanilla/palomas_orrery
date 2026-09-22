# Addendum, revision 2 -- the dipole-tilt display rule, after Opus's review

**Built on orrery `a318b3ecfed1ffaa290e8b34ed1ef63caa59295d`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `b17fd92704054e83424651585aa68a393ecb3d92`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs re-read live on 2026-09-21; neither has moved. Both
repositories cloned there for the enumeration in finding 5.**

**Type: ADDENDUM rev2, Mode 7.** Written September 21, 2026 by Claude
Fable 5.1, replacing
`ADDENDUM_L322_C2_dipole_tilt_display_rule_fable_20260921.md` whole,
after `REVIEW_L322_C2_tilt_addendum_opus_20260921.md`. All six of Opus's
findings are accepted; each is taken up below under its number.

**Rule files and sections read.** provenance-discipline 2.16 from the
orrery repo at `a318b3ec` (the mounted copy is 2.15, as recorded in the
reply): Rules 2, 3, 6, 7 and The ceiling; Measured Is the Goal,
"When the source gives a range". PROJECT_INSTRUCTIONS.md v3.66: The
Braid; Check All Parallel Pipelines. `constants_tokens.py` (sixteen
tokens, none year-based -- confirmed). `constants_new.py` rows
`EARTH_VAN_ALLEN_OUTER_RADII` and the IGRF-13 file as before.
`earth_visualization_shells.py` and `gallery/feature_renderers.js`,
grepped for every fixed-width format on a store row.

---

## What is withdrawn, now stated in full (finding 3)

From the reply of 2026-09-21, sub-questions 4 and 5:

- "The belt hover should print 9.4." No rule; withdrawn.
- "Remove the drift sentence in C2." Withdrawn; show-or-cap says show.
- **"Show-or-cap does not apply. A snapshot correctly labelled with its
  epoch has no mismatch."** Withdrawn. That sentence treated the epoch
  label as the claim. The claim is the drawn cone on a page with no
  date, and the label is part of SHOWING the mismatch, not a reason the
  rule does not apply. The addendum's position stands: the relation is
  one drawn tilt for a quantity that moves, the source publishes the
  size of the movement, so the rule says show.

The epoch 2020.0, form A, the count of five by counting for the tilt,
and the source and read lines all stand.

## The rate row (findings 1, 2 and 6)

**Which form the skill requires: the derivative, and here is the
basis.** Rule 3 says a derived row's count is set by its least precise
MEASURED input, and counts a difference by decimal places. Written as
a one-year difference of two tilts, the row's places come from the two
tilts, and theirs from the main-field coefficients (-29404.8 and so
on); the three secular-variation coefficients are absorbed into sums
and set nothing. The count would then describe an arithmetic artifact
and not the numbers the rate rests on. Rule 3's purpose is that the
count comes from the inputs that carry the quantity, so the form that
satisfies it is the one in which those inputs appear as factors: the
derivative. This is method and it will recur (Earth's pole, the
Moon's recession), so it goes in the skill, proposed below.

Both forms measured from the NOAA file as printed, degrees per year:
one-year difference -0.049293; derivative at 2020.0 -0.049277. Opus's
figures, confirmed.

**The row.** With H = sqrt(g11^2 + h11^2) and the six coefficient rows
(three main-field, three secular-variation):

```
rate = ( |g10| * (g11*g11' + h11*h11') / H  -  H * (-g10') )
       / (H^2 + g10^2)        in radians per year, then to degrees
```

(g10 is negative; its magnitude falls as g10 rises, so d|g10|/dt is
-g10'.) Written as an expression over the six rows with `np.hypot`,
`np.degrees` and `abs`. Count by Rule 3: products and quotients over
the secular-variation rows 5.7 (two figures), 7.4 (two) and -25.9
(THREE -- finding 6, my error) and the main-field rows (five, five,
six): **two figures, -0.049**. `# Figures: 2 -- set by the two-figure
secular-variation rows (5.7, 7.4)`. `# Derived:` states -0.049, at
that count.

**Tokens** (finding 2): `nt_per_year`, dimension nanotesla per year,
for the three secular-variation rows; `deg_per_year` for the rate. No
defining constant for either. `test_dimensions.py` then checks the
rate as a quotient of nT-per-year by nT, dimensionless, times degrees
-- the builder confirms the power rule reaches it or lists it NOT
CHECKABLE with the reason, which is a finding, not a pass.

**The hover** (finding 1) prints the rate at the row's count, not at
one figure: "tilted 9.4105 degrees from it (IGRF-13, epoch 2020.0),
decreasing about 0.049 degrees a year". Words Tony's; both numbers
served.

## The outer belt, reapplied against its actual row (finding 4)

Opus is right and the correction goes further than the review asks.
The mismatch is the L = 4 to 5 band in which three sources place the
peak, not the 3-to-7 extent. And the skill already says how a pick
from a band is stored: "Store the range as data, derive the drawn value
from it by a stated rule, and let display text interpolate the range
rather than restate the drawn value as a measurement" (Measured Is the
Goal, When the source gives a range). The row today types 4.5 with the
band in `# Declared:` prose, and the orrery's own belt hover types
"the L = 4 to 5 band" as literal text (`earth_visualization_shells.py`
line 1011): a number with no home, drawn on a public page. That is a
C1 row that passed while not meeting the range section. Not a
scope creep: the row is in the slice that closes.

So, in C2: two measured rows for the band, unit `l_shell` (L = 4 and
L = 5, one figure each, source Li et al. 2025 sec. 1 with the two
corroborating works as `# Source+:`, the arXiv text as what was
opened, reads from the builder); `EARTH_VAN_ALLEN_OUTER_RADII` becomes
the midpoint expression over them, status declared with the rule on
the row, count exact as a declared pick (Rule 2). The gallery hover
then shows the band from served rows -- "the peak is placed in the
L = 4 to 5 band; drawn at its midpoint" -- and with the mismatch shown,
show-or-cap says show, the count is not capped, and the km line prints
what the row declares. If Tony judges those eight figures wrong even
so, the fix is a cap on the row with the reason, never a shorter
display. The same section reaches other bodies (the Sun's helmet cusp
is "top of measured 2-4 range"); one ledger row for the class.

## The reach of the proposed Rule 7, enumerated (finding 5)

The Braid: bound to what the current artifact renders, assign each to
C2 or to a class. Grepped on both clones for a store row inside a
fixed-width format.

**Gallery, Earth room.** After C2 every Earth hover goes through
`fmtServed` at the served count except one site: line 372, the AU
figure at min(3, count), which is the named format exception. Two
other fixed-width sites exist and do not reach Earth: line 1047
(`radius_fraction.toFixed(2)`, a shape no served object uses, as its
own comment says) and line 1301 (`fmtAu`, the far shells). **Gallery
reach: zero new failures.**

**Orrery, Earth hovers.** `earth_visualization_shells.py` carries 47
format sites on 35 lines, in four kinds:

- `:.4g` on the two standoffs, four sites (791, 801, 882, 950). These
  print MORE than the rows will declare -- 10.25 where the row says 10.3
  -- so they fail the CURRENT Rule 7 the moment C2 changes the rows,
  and they print a number the store no longer holds. **These four are
  C2.**
- `:g`, twelve sites (796, 805 x2, 809 x2, 812 x2, 888, 891, 954, 997,
  999 x2, 1005, 1007 x2, 1011): prints the float's own digits, fewer
  where a declared trailing zero exists (2.0 prints "2"), more where a
  float holds digits the row does not declare.
- Fixed decimal places, `:,.0f` `:,.1f` `:.0f` `:.2f` `:.6f`,
  twenty-eight sites (169, 242 x2, 315, 316, 390, 391, 1191 x2,
  1192 x2, 1193 x2, 1200, 1305, 1306, 1307 x2, 1308, 1346 x2,
  1375 x2 and the LEO line Opus found): fewer or more depending on the
  row. Three of these also do arithmetic inside the display (316, 390,
  1305-1307), which is Rule 4's rounded-intermediate class one layer
  down.
- The typed band at 1011 and the typed "~9.6 deg" in
  `planet_visualization_utilities.py`: already C2 (correction does not
  travel; the band rows above).

**Assignment.** The orrery's hovers are the orrery's display pipeline,
one of the five parallel consumers; the artifact C2 delivers is the
store and the gallery's Earth room. The orrery's forty-odd sites go to
ONE ledger class, named with the line numbers and the four kinds
above, for a follow-on slice whose mechanism is not designed yet: the
orrery reads Python floats from the store and has no count at hand, so
it needs a helper that formats a row by the count the export declares.
Designing that helper here would be building the follow-on inside C2.
The four `.4g` sites are the exception pulled into C2, because after
C2 they print a wrong number.

So the proposed Rule 7 opens no sweep on adoption: its reach is
measured, bounded, and assigned, and this section is the record.

## The proposed skill wording, revised

**Rule 7, replaced whole** (2.16 lines 1943-1946):

> **Rule 7. A display prints the declared count, never more, and never
> chooses fewer.** A hover formats to the served count. A display with
> more figures than the row declares is the failure. A display that
> reads as too many figures is a finding about the ROW, not the page:
> the row's count comes down under Rule 3 -- by the ceiling where an
> uncertainty is stated, or by a cap with the reason on the row where
> the relation is approximate and its mismatch cannot be shown -- and
> the page then prints the shorter count because the row declares it.
> The page never shortens on its own, because a shortening the row
> does not record is a judgment nobody can find later, and the served
> count is what every checker reads. One format exception, named where
> it occurs: a display of fixed width truncates a longer served count
> and says so in its comment; the gallery's AU line at min(3, count) is
> that case. A display that FORMATS by a fixed number of places or
> figures rather than by the served count is not that exception; it is
> a site to be listed and assigned when the rule reaches it, as the
> orrery's Earth hovers were at L-322 C2.

**Show or cap, one sentence added** after "This decides which of the
two answers applies.":

> It also decides a snapshot of a quantity that moves: where the source
> publishes the rate, the store holds the rate's inputs and the page
> shows the epoch and the rate beside the value; where it does not, the
> count is capped to the place the movement over the model's validity
> span supports. Earth's dipole tilt is the case: IGRF-13 prints the
> secular variation, so the tilt prints at its full count with its
> epoch and its rate.

**Rule 3, one paragraph added** after the "relation itself is
approximate" paragraph:

> **A rate or other derivative row is written as the derivative
> expression over the rows, never as a difference of two evaluations.**
> The difference form is counted by decimal places from the two
> evaluated values, whose places come from the largest inputs, so the
> quantities the rate actually rests on set no count and the row claims
> a precision it borrowed. Earth's dipole tilt rate is the case: as a
> one-year difference it would carry the main field's places; as the
> derivative it carries two figures from the secular-variation
> coefficients, -0.049 degrees per year. Time-rate rows need time-rate
> tokens (`nt_per_year`, `deg_per_year`).

**Rule 6, one sentence added** as in the first addendum (a whole the
source defines from parts it prints is a derived row over rows for the
parts).

**When the source gives a range, one sentence added:**

> A pick typed as a literal with its range in prose does not meet this
> section, however well the prose cites; the range is rows, the pick is
> an expression over them, and the display shows the range from those
> rows. Earth's outer-belt peak at L-322 C2 is the corrected case.

## What this changes in the manifest

- 4.2, 4.3a: the tilt brings six measured coefficient rows, the tilt
  and its rate (two derived); the outer belt brings two band rows and
  its pick becomes an expression. Two new tokens in 4.1.
- Section 6: the belt tilt line prints the full count, the epoch and
  the rate; the outer belt gains a band line. Exact words to Tony.
- Section 13, item 9: removed; each case now resolves on its row.
- A new stage in 4: the four `.4g` sites in `earth_visualization_shells.py`
  print by the export's declared count.
- Section 11 gains three classes: the orrery's Earth format sites (47,
  four kinds, lines named above); declared picks with their range in
  prose on other bodies; rate rows on other bodies.

## Ordering

As Opus says, and one line more than the first addendum: this build
session loaded 2.16 and cannot verify a reinstall from inside itself,
so the C2 build moves to a fresh session that confirms 2.17 at load,
and the manifest revision belongs with the 2.17 cut from the designing
session.

---

Written September 21, 2026 with Anthropic's Claude Fable 5.1.
