# The Figure Count (provenance-discipline reference)

Read this file in 3 parts: lines 1-261, 262-514, 515-569.

Opened from provenance-discipline's Report to the Figures You Have,
before writing or checking a `# Figures:` line, deriving a value, or
printing a number in a display. Moved here from provenance-discipline
2.26 on 2026-10-08 (L-418), word for word apart from the edits
provenance-discipline 2.27 lists. The core rule -- compute at full
precision, report to what the least precise input supports -- and The
Store Carries the Verified Figure stay in SKILL.md, and so do the rules
this one leans on: When the Source Gives a Range, The Status Line and
The Read Field.

### The Figure Count Is a Declared Field [QUALITY]

Python can round a number to N figures but cannot count them through
arithmetic, so the count is declared per row, the way the unit is.
These are the textbook rules, written down once so they resolve the
same way for every row. The reference is **Wikipedia, Significant
figures**, which Tony named and which is open: every rule below can be
checked against it by anybody, which is the point. The same rules
appear in ASTM E29, but that is an aside and NOT the reference we work
from -- it costs $86, so a rule the project depends on could not be
opened by any of us, which fails our own Access Standard; and its scope
is conformance with specification limits, which this store has none of.
(Tony's ruling, 2026-09-19, L-342.)

**Where a rule below states a condition, the condition is load-bearing
and is not to be trimmed.** v2.14's Rule 2 said trailing zeros after a
decimal point count, full stop. The page says they count WHEN THEY ARE
WITHIN THE REPORTING RESOLUTION. Dropping four words made the rule
wrong, and nobody could see it without opening the source -- which is
the argument for citing something openable rather than for copying a
standard verbatim.

**Rule 1. `# Figures:` is a comment key beside the value.** Seven forms:

```
# Figures: 7 -- set by EARTH_ROTATION_RATE_RAD_S (7.292115e-5, 7)
# Figures: 5 -- PREM reports to 0.1 km, so 3480.0's trailing zero counts
# Figures: exact -- IAU 2012 definition
# Figures: exact -- prints 8, the definition's own digits (84381.448)
# Figures: 4 -- Table 1 prints 10.22, uncertainty 0.10
# Figures: 3 -- uncertainty 0.13, root-sum-square of Shue's a1 to a5
# Figures: 4 -- thousandths: thousands place of the sum, set by CHROMOSPHERE_PHYSICAL_KM (2000, 1), carried through the exact SUN_RADIUS_KM
```

A derived row names the input that set its count. A place-governed
row scaled by an exact row names the place it keeps, the input that
set the place, and the exact row it was scaled by (Rule 3, scaling). A measured row
states what the source supports, and says in words whether a trailing
zero counts, because an integer literal cannot. A defined constant says
`exact`, and when a display prints it, also how many figures it prints
(`prints N`, Rule 7's exact row). A measured row whose source STATES an uncertainty writes it
as a FIELD: the word `uncertainty` followed directly by the number, in
the row's own unit, on its `# Figures:` line. A checker reads that
field and never the prose around it, so "an uncertainty of 0.1 m" in
words is not read. A derived row writes the uncertainty form only when
it declares more figures than counting alone allows, and then the
number is the one recomputed from full digits (Rule 3, The ceiling). The field is needed because a float cannot hold a significant
trailing zero (13.50 is stored as 13.5) and the export would otherwise
lose the count.

**A conversion carries none of these lines** (v2.27, L-390). A name the
orrery keeps for a value in another unit (Rule 3) is marked with one
comment key instead, naming the row it converts:

```
# Conversion: of <ROW> -- computed from that row, which carries the source and the count
```

It carries no `# Figures:`, `# Status:`, `# Derived:`, `# Source:`,
`# Read:` or `# Cross-checked:` line, because its count and its source
are its row's. Its expression is that one row scaled only by rows that
define units. `constants_rows.conversion_problem()` checks it (Rule 8).

**Rule 2. Counting a literal follows the standard rules.** Non-zero
digits count; zeros between them count; leading zeros never count;
trailing zeros in an integer count only if the source says so. An exact
number has unlimited figures.

**Trailing zeros after a decimal point count WHEN THEY FALL WITHIN THE
SOURCE'S MEASUREMENT OR REPORTING RESOLUTION**, and that condition is
the rule, not a refinement of it. 1500 m measured to a resolution of
100 m has TWO figures, not four, and the page lists exactly that case
among the digits which are not significant: trailing zeros serving as
placeholders. So the question to ask of a row is never "where does the
last digit fall" but "to what resolution does this source report". PREM
Table I reports every boundary radius to 0.1 km, so `3480.0` carries
five. The NASA fact sheet prints `6371.000` in a block that also prints
3485, 5513, 20.4 and 11.186, so it is not padding and the value carries
seven. A DECLARED drawing condition (a chosen solar wind pressure, a
chosen cut angle) is exact for counting: it is a choice, not a
measurement, so all of its digits are known.

**A trailing `.0` in this store is Python's, not a figure** (v2.20).
The digits of a choice are the digits it was chosen with, and a decimal
point Python needs is not one of them. A trailing `.0` reaches this
store and its displays by three routes, and none of them says anything
about significant figures:

- **Typing.** Python treats a number written with a decimal point as a
  float and one without as a whole number, so rows are typed `200.0`
  to make them floats. `200`, `200.0` and `200.00` are the same stored
  number; the float keeps no record of how it was typed. That is also
  why `13.50` is stored as `13.5` (Rule 1).
- **Arithmetic.** Division in Python always returns a float, even
  between whole numbers: `4 / 2` is `2.0`. A derived row can gain a
  `.0` from its expression without anyone typing one.
- **Printing.** A float printed with no format always shows at least
  one decimal place, so a whole-number float prints as `2.0`. That
  covers `str()`, a bare f-string `{x}`, and `json.dumps`, which
  writes `constants_export.json`. A format can remove it (`:g` prints
  `2`) and a page can put it back: the gallery printed the declared
  solar wind pressure as "2.0 nPa" by its own `toFixed(1)`, from a
  value JavaScript had read out of the export as plain 2.

So the literal, the printed value, the exported value and the page's
output cannot say which trailing zeros are meant. For a measured row
the source's reporting resolution says (above). For an exact row the
digits it was defined or chosen with say: the declared pressure is
2 nPa because Shue et al. (1998) use Dp = 2 nPa, and the `.0` in
`2.0` is Python's. That is why the count is a field on the
`# Figures:` line and an exact row's print count is a field too
(Rule 7), never read from the value. A choice that really was made to
a trailing zero says so on its `# Declared:` line, and its print count
states it. (Checked by running Python 3 and Node on 2026-09-27, at
Tony's request, when the Stage D print counts were settled. Handle
L-322.)

**A DECLARED CONSTRUCTION is exact in the same way** (v2.17). A drawing
value that is a stated rule over measured rows -- the midpoint of a
sourced band, the top of a sourced range -- is a choice, not a
measurement, and its `# Figures:` line names the rule and the rows:
`exact -- declared construction: midpoint of <row>, <row>`. The
checker accepts `exact` only on a row whose `# Status:` begins
`declared` (not `declared pending`), with every named row in the
expression; a `measured` or `derived` row cannot declare exact over a
measured input. The export serves an exact row unrounded, so every
consumer draws the same value. The alternative was measured before
this was written: counted to its rows' one figure, the outer belt's
4.5 exported as 4.0 for the gallery while the orrery drew 4.5 from
the float -- two consumers, two rings. The construction is not a
measurement and the hover does not print it as one: it shows the
range from the rows and states the rule (When the source gives a
range). The checker lists every declared construction by name in its
output, so each use is seen. Earth's outer-belt peak is the case
(L-322 C2).

**Rule 3. A derived row's count is set by its least precise MEASURED
input.** Products and quotients keep the fewest figures among the
inputs. Sums and differences are good to the coarsest decimal place
among the inputs (`6371.0 - 660` is good to tens: 5710, because its
660 km input carries two figures). Exact inputs
and declared conditions are skipped when finding the minimum. For a
power, an exponential or another function, the fewest-figures rule is
the default; where the function magnifies the input's uncertainty (an
exponent above one in magnitude), drop a figure and say why on the
row. Where an input carries a stated uncertainty, the uncertainty
decides instead and counting is the fallback; how is set out under The
ceiling, below.

**A place-governed value scaled by an exact row keeps its place, not
its count** (v2.21). A sum or difference is good to a decimal place
(above). Multiplying or dividing it by an exact row -- a unit
conversion, a nominal radius -- moves that place with the value, and
the row keeps the place the scaling gives: a sum good to thousands of
kilometres, divided by 695,700 km per solar radius, is good to
thousandths of a solar radius, because 1,000 km is 0.0014 solar
radii. Counting the quotient by fewest figures instead keeps three on
either side of the division, and three figures of 698,000 is
+/- 500 km while three figures of 1.003 is +/- 3,500 km: the leading
digit went from 6 to 1 and the count lost a factor of seven. The
reference page names this case. Its arithmetic guidelines do not
ensure the result's implied uncertainty is close to the measured one,
it says the problem shows up in unit conversion, and its example is
8 inches (+/- 0.5 in) converted by the guideline to 20 cm (+/- 5 cm)
when the proper result is 20. cm (+/- 0.5 cm). The place kept is the
power of ten nearest, on a log scale, to the sum's place unit carried
through the scaling, a tie going to the coarser -- the same measure
the Report bullet under The ceiling uses: 1,000 km / 695,700 km is
0.0014, nearer 0.001 than 0.01, so thousandths. The row states the
place it keeps, the input that set the sum's place, and the exact row
it was scaled by (Rule 1, seventh form). The two forms of one
expression now count the same: 1 + 2000 / 695700 and
(695700 + 2000) / 695700 both keep thousandths, so whichever form the
unit check accepts, the count is 4. This is not an implied
uncertainty raising a count; it is the sum's own place, converted,
and it reaches nothing but a sum or difference scaled by exact rows.
A product or quotient of measured quantities keeps fewest figures as
before, and Jelinek's bow shock stays 13.5.

**A value in another unit is computed, never stored, and its count
comes from its source row alone** (v2.22). Each quantity is ONE row,
in the unit its best source gives it, carrying that source. Its value
in any other unit is not a row: `constants_rows.conversions()` works it
out from the source row's full digits times the exact factor, rounds
once, and the export serves it as `"in"` (schema 6). A name the
orrery's drawing code keeps for such a value is computed from the one
row, is marked `# Conversion: of <ROW>` (Rule 1), and states no
precision of its own. A conversion has no chain. Its
uncertainty is its source row's, scaled by the exact factor: the stated
uncertainty, where the source's figures field has one; otherwise half a
unit of the source's last declared place; for an exact source, half a
unit of the last place of its print count. The place printed is the one
whose implied uncertainty, half a unit in that place, is nearest that
scaled uncertainty on a log scale, a tie going to the coarser -- the
Report test under The ceiling. Where the uncertainty is half a unit of
a place, that is the same as carrying the place itself through the
factor to the nearest power of ten, which is the measure the paragraph
above uses. The count is the figures of the full-digit value down to
that place, and never fewer than one: where the place is coarser than
the value's leading digit, the value keeps its one leading figure
(a one-figure 100 Earth radii is 0.004 AU, not 0.00). An exact source's
conversions are exact, unrounded, with a print count found the same
way; the row that defines a unit is 1 in that unit, printing 1. The
sum rule above is one instance of this: a sum's declared place is the
place its count names. This reads a row's declared precision; it never
sets a row's ceiling from its chain, so the implied-uncertainty bullet
under The ceiling stands and Jelinek's bow shock stays 13.5 Earth
radii. The exception cuts both ways. The chromosphere gains a figure
(698,000 km at three, 1.003 solar radii at four); the bow shock loses
one (13.5 Earth radii at three, 86,000 km at two, because the source's
last figure is worth 638 km and "86,200" would claim fifty). A
conversion whose source row is wrong is fixed at the source row, once.
(Tony's ruling, 2026-09-28, on Claude Fable 5.1's recommendation;
L-345. Fable's text said "the power of ten nearest that scaled
uncertainty"; its own worked numbers, and the Report test it names,
compare the uncertainty with half a unit in each place, which is the
wording here. Read the other way, the bow shock's AU would print
0.000576 at three figures, against the ruling's 0.00058.)

The top of the chromosphere is the worked case. `SUN_RADIUS_KM +
CHROMOSPHERE_PHYSICAL_KM` is good to thousands, set by the depth
Carroll & Ostlie give as about 2,000 km (one figure), so 698,000 km at
three figures; divided by the exact `SUN_RADIUS_KM` it keeps
thousandths, 1.003 at four figures -- one more figure than the
kilometre line, and the figure the drawing needs. The export rounds
to the count (Rule 6): at three figures the served value is 1.00,
which draws the chromosphere on the photosphere and erases the
2,000 km hairline promoted on 2026-08-16; at 1.003 it draws 2,087 km
above the photosphere, inside the source's "about". The hover still
says about 2,000 km deep, and the radius line no longer contradicts
it with an implied +/- 3,500 km. Before this paragraph the rule as
written gave 1.00 by the sum-first form and 1.003 by the divide-first
form, and the unit check forced the first. (Tony's ruling,
2026-09-28, confirming Claude Fable 5.1's recommendation, checked
against the reference page the same day. Handle L-322.)

**A row may declare FEWER figures than its inputs support when the
RELATION ITSELF is approximate, with the reason in words on the row.**
Counting governs how precision flows through arithmetic; it says
nothing about a formula that is an idealisation to begin with. Earth's
Hill sphere is the case: every input is exact or carries nine figures,
so counting gives seven, but substituting Earth's perihelion distance
for its mean distance moves the answer by more than one percent. Seven
figures would claim a precision the relation cannot deliver whatever
its inputs carry. This is a floor on honesty, not a licence to round to
taste: the row must say WHICH approximation caps it and by roughly how
much. (L-342, Fable's review of C1, Finding 3.)

**A rate or other derivative row is written as the derivative
expression over the rows, never as a difference of two evaluations**
(v2.17). The difference form is counted by decimal place from the two
evaluated values, whose places come from the largest inputs, so the
quantities the rate rests on set no count and the row claims a
precision it borrowed. Earth's dipole tilt rate is the case: as a
one-year difference of two tilts it would carry the main field's
places; as the derivative over the six IGRF-13 rows it carries three
figures, set by the sum inside it, -0.0493 degrees per year.
Time-rate rows use time-rate tokens (`nt_per_year`, `deg_per_year`).

**An angle computed from a pure number never applies `degrees` to the
result.** An inverse trigonometric function of a ratio, or a rate
derived from one, comes out of the arithmetic as a bare number or an
inverse time. The unit check reduces a ratio whose units cancel to a
plain float before the function, so `degrees` of the result is a bare
number declared in `deg`, a MISMATCH; `degrees` of an inverse time it
refuses outright, CANNOT EVALUATE, which fails inside a closed slice.
The row multiplies by the exact row `DEG_PER_RAD` instead, whose unit
is `deg` and which carries the radian, so the unit check follows the
chain to degrees, or degrees per time, with no equivalency. Both the
tilt and its rate are written this way, and both were run through
both checkers before this was written. `DEG_PER_RAD` has no store
inputs, so neither checker judges it and its unit is asserted; the
row says so in words, as a definition.

**A unit conversion inside an expression is an exact row, never a bare
number** (v2.18). The unit check converts units by itself, so dividing
seconds by a bare 3600 leaves seconds. Earth's sidereal rotation period
was drafted as `2 * math.pi / EARTH_ROTATION_RATE_RAD_S / 3600.0` and
declared in hours; the unit check failed it as a MISMATCH, the
arithmetic giving 0.006648 hours against 23.93447 stored, while the
figures check passed the same row. The conversion is an exact row with
a compound-unit token -- `S_PER_HOUR` in `s_per_h`, `ARCSEC_PER_DEG` in
`arcsec_per_deg` -- and the expression divides by the row. A pure number
that belongs to the physics, like the two pi in a period, stays bare,
because the token it meets already treats the radian as dimensionless;
giving it a unit fails the check the other way ("declares s; the
arithmetic gives rad s"). Both forms were run through both checkers
before this was written. (Claude Fable 5.1's review of the Stage D
manifest, Finding 1, re-run by Claude Opus 5.5 at ac25d4f4. Other rows
that convert by a bare number, such as `LIGHT_MINUTES_PER_AU`, are one
ledger class.)

**The ceiling: where an uncertainty is stated, propagate it** (v2.16).
The procedure these rules were adopted from says it in one line:
"Where any input carries a stated uncertainty, propagate that instead
and let it decide." Five parts make that usable. What the reference
page says is kept apart from what this project adds, and the project's
part is marked as its own.

- **Which uncertainty.** Propagate the stated uncertainties of the
  INPUTS: how well each was measured or fitted. A model's scatter about
  the data it was fitted to is a different quantity. It describes the
  real thing around the model, and it is shown beside the value, not
  propagated into it.
- **Show or cap.** Where the source publishes the size of a relation's
  mismatch as a number the store can hold and the page can show, show
  it beside the value: real magnetopause crossings scatter 1.23 Earth
  radii about Shue's model, and the hover says so. Where it does not,
  cap the count and say why on the row, as the Hill sphere's is in the
  paragraph above. This decides which of the two answers applies. It
  also decides a snapshot of a quantity that moves (v2.17): where the
  source publishes the rate, the store holds the rate's inputs and the
  page shows the epoch and the rate beside the value; where it does
  not, the count is capped to the place the movement over the model's
  validity span supports. Earth's dipole tilt is the case: IGRF-13
  prints the secular variation, so the tilt prints at its full count
  with its epoch and its rate.
- **When propagation sets the ceiling.** A derived row's ceiling -- the
  most figures it may declare -- is set by propagation whenever at
  least one measured primary in its chain STATES an uncertainty, and by
  counting otherwise. A row may always declare its ceiling or fewer. It
  writes the uncertainty form of Rule 1 only when it declares MORE than
  counting alone allows, so the reason for the extra figures is on the
  row; a row that counts and stays within its ceiling keeps its
  counting line. Implied uncertainties alone never set a ceiling:
  Jelinek's bow shock standoff, whose chain states none, is 13.5 by
  counting and would be 13.51 if they did. A place carried through an
  exact scaling is not this: it is the sum's own place, converted
  (Rule 3, scaling).
- **Propagate.** Trace the row to its primaries. Move each up and down
  by its uncertainty and take the half-difference, a central
  difference; a one-sided step gives a different answer wherever the
  relation curves (Shue's standoff gives 0.129 up and 0.136 down).
  Combine by root-sum-square, re-evaluating through the chain from full
  digits: Rule 4 applies to an uncertainty exactly as to a value, and
  an uncertainty converted from a rounded one is the same failure.
  Root-sum-square assumes independent inputs; where the source gives no
  correlations the row says so, and where the reported place would not
  survive the plain sum of the effects, the row gives both numbers. A
  primary that states no uncertainty contributes its implied one, half
  a unit in its last significant place, as the page allows; that is a
  full half-width rather than a standard deviation, so it errs large.
  Declared conditions and exact numbers contribute nothing.
- **Report. What the page says:** to report a single number, choose
  the one whose implied range is close to the measured range, since
  going coarser loses a lot of information; its examples are
  3.78 +/- 0.07 kg and 3.78 +/- 0.09 kg, both best quoted as 3.8 kg.
  Where the uncertainty is printed beside the value, it takes one or
  two figures and the value ends in the same place. **What this project
  adds, and why:** "close" is measured on a log scale, because implied
  uncertainties step by factors of ten, and a tie goes to the coarser
  place; a linear measure would keep the tenths place up to +/- 0.27
  and overstate the precision five-fold. Each unit is reported by its
  own uncertainty, so a value and its conversion can carry different
  counts; the page warns of exactly this for unit conversions, and on
  the counting route the same exception is Rule 3's scaling
  paragraph.

The magnetopause standoff is the worked case. Shue's Table 1 states a
standard deviation on every coefficient; propagated at the declared
solar wind they give 10.2518729724 +/- 0.1326 Earth radii, reported
10.3 -- the tenths place implies +/- 0.05 and the units place +/- 0.5,
and the tenths is closer. The store had carried 10.25, a figure too
many even by the largest single effect, +/- 0.09. In kilometres the
same uncertainty is +/- 846 km, so 65,000 km at two figures; in AU,
0.00044. The plain sum of the effects is 0.25 and the tenths place
holds only to 0.158, which the row states. (Tony's instruction of
2026-09-20, "See the Skill on significant digits"; worked in
`documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md`,
section 2.1, and reviewed twice by Claude Fable 5.1. Handle L-322.)

**Rule 4. Compute from the PRIMARY inputs at full precision; round
once.** A derived row that feeds a second derived row does not chain
through a rounded copy. The second row's `# Derived:` line goes back to
the measured primaries. Rounding an intermediate puts a rounding error
inside the store.

**Rule 5. Round half to even**, implemented as `float("%.*g" % (n, x))`.
This is what Python's `round()` and `%g` already do; the schoolroom
half-away-from-zero is not, so the rule is named to avoid an argument
with the interpreter.

**Rule 6. The store holds the derivation, never a rounded copy.** A
derived row stays an expression at full float precision and follows its
inputs automatically. Rounding happens at the reporting step, and the
EXPORT is a reporting step: it rounds each value to its declared count
and carries the count beside the value and the unit, so the gallery
formats without guessing and no downstream copy holds digits the row
never had. (This is what Tony's 2026-09-12 objection was about --
sixteen digits copied into a gallery config -- and Rule 6 answers it at
the boundary rather than at rest.) The two magnetosphere standoffs
stored as literals under the withdrawn ruling stay literals until the
export lands and the gallery stops parsing the store (L-322 ruling 6);
they revert to expressions at their slice visit.

**Where a source prints the parts and states the relation that makes
the whole, the whole is a derived row over measured rows for the
parts** (v2.17) -- never a typed result with its working in a comment,
which a closed slice does not accept (Rule 8 names that shape).
IGRF-13 prints the three degree-1 coefficients and says the pole is
computed from them, so Earth's dipole tilt is an expression over
three coefficient rows; the stored 9.6 it replaced was in no epoch of
the cited source.

**Rule 7. A display prints the declared count, never more, and never
chooses fewer** (v2.17). A hover formats to the served count. A display
with more figures than the row declares is the failure. A display that
reads as too many figures is a finding about the ROW, not the page:
the row's count comes down under Rule 3 -- by the ceiling where an
uncertainty is stated, or by a cap with the reason on the row where
the relation is approximate and its mismatch cannot be shown -- and
the page then prints the shorter count because the row declares it.
The page never shortens on its own, because a shortening the row does
not record is a judgment nobody can find later, and the served count
is what every checker reads. One format exception, named where it
occurs: a display of fixed width truncates a longer served count and
says so in its comment; the gallery's AU line at min(3, count) is
that case. A display that FORMATS by a fixed number of places or
figures rather than by the served count is not that exception; it is
a site to be listed and assigned when the rule reaches it, as the
orrery's Earth hovers were at L-322 C2: 47 sites, four kinds, one
ledger class with no automated coverage, and the four that print more
than the row declares pulled into the build. (Until v2.17 this rule
let a display show fewer with no method for choosing, and every use
of that permission reached Tony as a readability call. Tony,
2026-09-21: "the basis should be in the skill not arbitrary.")

**An exact row prints the digits its definition states** (v2.18). An
exact quantity has unlimited figures, so a served count of `exact`
cannot tell a page how many to print. Until v2.18 the gallery's
`fmtServed` printed every exact row with `toFixed` and a number of
places chosen at each of its call sites, which is the page choice this
rule forbids; nobody noticed while the exact rows were numbers like
2.0 and 120. The parts:

- **Stored in the form its definition prints.** A quantity defined in
  arcseconds is a row in arcseconds, and its degree form is an
  expression over it and an exact conversion row (Rule 3). Horizons
  defines its ecliptic of J2000 by an obliquity of 84381.448
  arcseconds, so `EARTH_OBLIQUITY_J2000_ARCSEC` holds that and
  `EARTH_OBLIQUITY_J2000_DEG` divides it by `ARCSEC_PER_DEG`. The unit
  check then judges the degree row, instead of trusting a literal that
  has no inputs.
- **The print count is a field.** Every exact row a display prints
  states it on its `# Figures:` line directly after `exact --`, as
  `exact -- prints N`. That is the only place a checker reads it:
  measured rows' lines say "the source prints 1.5" in prose, and
  prose is never read. It has to be a field because the literal cannot
  carry it. A trailing `.0` is Python's, not a figure (Rule 2), and for
  a declared pick there is no source resolution to say whether a zero
  counts, so a count read from the literal would print a floor chosen
  as 200 km as "200.0 km". The count is the digits the definition or
  the choice was stated with: 3 for that floor, 1 for Shue's 2 nPa. An
  exact row defined from another exact row writes its defining input's
  count on its own line; nothing carries a count between rows. A
  DECLARED CONSTRUCTION (Rule 2) prints the digits of the value its
  rule gives, not the counts of the measured rows its rule is over,
  which are figure counts and not print counts: the midpoint of 4 and
  5 prints 4.5, two figures. Its line carries both fields:
  `exact -- prints 2, the digits of the value its rule gives (4.5);
  declared construction: midpoint of <row>, <row>`.
- **The checker refuses three counts** (v2.20). A count with more
  digits than the number has: for a typed number, the digits of the
  literal as written, trailing zeros included, so 200.0 allows up to
  four; for an expression, the digits of the value it computes. A
  count too small to write the number out in full, because an exact
  number printed rounded is a different number: 105 at two figures
  would print 100. And any count but 1 on a zero, which prints as 0.
  `constants_rows.print_count_problem()` makes all three, and the
  export stops on any of them. An exact row no display prints carries
  no print count. A display that reaches an exact row with none
  reports it rather than choosing a width: in the orrery,
  `constants_rows.exact_text()` raises where the display is built.
  `exact_rows_report.py --check` fails, naming each item, when a
  printed exact row states no count, when an orrery line prints one
  any way but `exact_text()`, or when the gallery does not serve the
  count beside it; the maintenance run runs it as "Exact rows by the
  count".
- **The export carries it and the page prints by it.** The export
  serves the print count beside the value, and the page prints an
  exact row to that many significant figures. `toFixed` goes for exact
  rows. The gallery's magnetopause hover is the case: it prints
  `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`, a declared limit typed 120.0, as
  "Drawn to 120 degrees", until Stage D by a width of 0 decimals chosen
  at the call site. Under this rule the row states `exact -- prints 3`
  and the page prints three figures; counted from the literal it would
  print "120.0".
- **Earth's obliquity carries no print count.** It is the row this
  rule was first written on, and it was the example until v2.19. Since
  the Stage D manifest's revision 3 no display prints it: the axis
  hovers print the tilt of date, worked out from Horizons' pole, and
  `EARTH_OBLIQUITY_J2000_DEG` is used only as the angle that defines
  the ecliptic frame. An exact row no display prints carries no print
  count, as the second part above says.

(Claude Fable 5.1's review of the Stage D manifest, 2026-09-23,
Finding 2; the print-count field is Claude Opus 5.5's amendment to it
in the same round, because Fable's form counted from the literal.
Tony accepted both on 2026-09-23. The checker, the export and the page
implement this in the Stage D build.)

**Rule 8. The checker reads the field and names every derived row it
cannot see.** `test_derived_figures.py` checks the DECLARATION rather
than a rounded literal: a derived row's count may not exceed the least
count among the non-exact inputs it names, each named input appears in
the expression, and a `# Derived:` row with no `# Figures:` line prints
NOT YET MIGRATED with its name -- a FAIL inside a closed slice, a named
gap outside one. ENUMERATION NAMES BOTH ROUTES TO A DERIVED ROW, never
a `# Status:` word: a row whose right-hand side is ARITHMETIC over other
store rows, and a row carrying a `# Derived:` line. They are not the
same set. `constants_rows.py` treats a typed number with a `# Derived:`
note as a LITERAL whose arithmetic lives in prose rather than in the
expression, so it is invisible to a walk that looks only at right-hand
sides -- and the two `TRANSITIONAL` standoffs are exactly that shape
until they revert. The checker names rows found by either route, and an
expression with no `# Derived:` line is itself a named gap. (At 2.12
enumeration went by Status and saw 2 of 27.)

**The checker also enforces the ceiling of Rule 3.** It is specified
here at 2.16 and built at L-322 Stage C2; until that build the checker
counts only, and a row relying on the uncertainty route fails it. For
every derived row it works out the ceiling -- by propagation where any
measured primary in the chain states an uncertainty in the field
form, by counting otherwise -- and FAILS a row only for declaring MORE
than its ceiling; where the two ceilings differ it prints both. A row
declaring more than counting allows must carry the uncertainty form,
and its stated number must match the recomputed one to the digits
stated, which is how a one-sided step or a rounded intermediate is
caught. It reads uncertainties only from the field, never from prose,
and names any primary whose figures line mentions an uncertainty in
words without the field, so the blind spot announces.

**The checker also applies Rule 3's scaling paragraph** (v2.21,
specified here and built with the chromosphere row; widened at v2.22).
For a derived row that is a source row, or a sum or difference of
rows, scaled only by exact rows, the ceiling by counting is not the
fewest figures among the inputs but the place: the source's
uncertainty, or the coarsest last place among the sum's measured
inputs, carried through the exact factors and placed by the conversion
rule in Rule 3; the count is the figures of the computed value down to
that place. It prints the place it found beside the count, so a wrong
ceiling is visible and not only a pass. The widening was built with
patch D20 (L-345), which retired the store's conversion rows. Since
then a marked conversion (Rule 1) is checked by
`constants_rows.conversion_problem()` and listed by name with its
source; a wrong one is CONVERSION WRONG, which fails, and a row shaped
like a conversion and not marked is UNMARKED CONVERSION, a named gap
that fails inside a closed slice (v2.27, L-390).
The export's conversions are checked separately, value and count, by
`test_constants_export.py` check 6.

(Tony's rulings, 2026-09-16, adopting the procedure in
`documentation/DESIGN_L322_d_significant_figures_20260916.md` "as
recommended" and withdrawing the ruling of 2026-09-12 in the same
message. Handle L-322 (d).)
