# L-322 (d): how a calculated value is rounded to significant figures

Built on orrery `ebdc55cc4668c297d78ff1d46d2880b3cd78635f`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `72a49552aa6ba4b21c2f58e3c5fe53f7d198590c`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | Claude Fable 5.1 | 2026-09-16
Type: DESIGN. Zero code.
RULED 2026-09-16, same evening: "confirmed as recommended. and i withdraw
my september 12 ruling as it may be counter productive given the new
procedure." Rules 6 and 8 below are in their REVISED form, as the skill
carries them (provenance-discipline 2.13, L-335); the originals were
written on the September 12 ruling and went with it.
Skill loaded: provenance-discipline 2.12, matching the manifest.
Reference Tony named: https://en.wikipedia.org/wiki/Significant_figures
(read this session). The engineering standard behind it is ASTM E29,
"Standard Practice for Using Significant Digits in Test Data".

---

## 1. What is being decided

L-322 item (d) asks how many figures a DERIVED constant may carry, and
who decides. The ledger already says the answer has to be DECLARED per
row, the way the unit is, because Python can round a number to N
figures but cannot count them through arithmetic. This document says
what the declaration is, what the standard counting rules are, and what
the checker does with them.

## 2. What the store does today, measured at ebdc55cc

`constants_new.py` has 110 top-level assignments. 27 of them carry a
`# Derived:` line. They are in three different states.

**21 are stored as expressions**, so Python holds them at full float
precision and the figure count lives only in prose on the row:

  Earth interior and near-space (10): EARTH_INNER_CORE_RADII,
  EARTH_OUTER_CORE_RADII, EARTH_LOWER_MANTLE_KM, EARTH_LOWER_MANTLE_RADII,
  EARTH_UPPER_MANTLE_RADII, EARTH_GEOSTATIONARY_RADIUS_KM,
  EARTH_GEOSTATIONARY_RADII, EARTH_LEO_OUTER_KM, EARTH_LEO_OUTER_RADII,
  EARTH_THERMOPAUSE_RADII.

  Earth Hill sphere (2): EARTH_HILL_SPHERE_KM, EARTH_HILL_SPHERE_RADII.

  Sun (3): SOLAR_RADIUS_AU, RADIATIVE_ZONE_AU, CHROMOSPHERE_PHYSICAL_RADII.

  Exact conversions and definitions (5): LIGHT_MINUTES_PER_AU,
  AU_PER_LIGHT_YEAR, SPEED_OF_LIGHT_M_S, M_PER_AU, SOLAR_MASS_KG.

  Galactic (1): SGR_A_DISTANCE_LY.

**4 are stored as literals with no Status line**: ROCHE_LIMIT_RADII,
HAUMEA_RADIUS_KM, PARSEC_TO_AU, EARTH_BOW_SHOCK_CUT_ANGLE_DEG (this last
one is a measured value that happens to carry a `# Derived:` note; it is
not a derived row).

**2 are stored the way L-325 rules**, as literals at their declared
figures, with `# Status: derived` and a `REPORT` figure in prose:
EARTH_MAGNETOPAUSE_STANDOFF_RADII and EARTH_BOW_SHOCK_STANDOFF_RADII.

`test_derived_figures.py` finds derived rows by the words `derived` on a
`# Status:` line. Only the two magnetosphere rows have one. So the
checker sees 2 of 27 derived rows, and its own promise -- "an uncovered
derived row FAILS here rather than being quietly ignored" -- cannot fire
for the other 25, because it cannot see them. This is the shape the
protocol calls A Check That Cannot Fail. It ran green this session
(2 of 2 OK) and that result says nothing about 25 rows.

**The skill contradicts itself on this class.** The section Report to
the Figures You Have [QUALITY] says a derived row "stays symbolic" and
shows EARTH_INNER_CORE_RADII as an expression as its worked example. The
section A Derived Row Stores the Figure Its Sources Support [CRITICAL]
(Tony's ruling, 2026-09-12) says a derived row with declared-constant
inputs stores the rounded literal. Both are in provenance-discipline
2.12. The 21 expression rows follow the first; the 2 literal rows follow
the second. A next session reading the skill could justify either.

## 3. The standard method, as the reference states it

These are the rules any engineering or science course teaches. Nothing
here is invented for this project.

**Counting the figures in a written number.** Non-zero digits count.
Zeros between non-zero digits count. Leading zeros never count (0.056
has two figures). Zeros after the decimal point at the end count (1.200
has four). Trailing zeros in an integer with no decimal point are
AMBIGUOUS: 3480 could be three or four figures, and only the source can
say. An exact number (a count, a defined constant, an integer in a
formula like the 2 in 2r) has unlimited figures and never limits a
result.

**Multiplication and division.** The result keeps as many figures as
the input with the FEWEST figures. 1221.5 (five) / 6378.1366 (eight)
supports five: 0.19151.

**Addition and subtraction.** The result is good to the coarsest
DECIMAL PLACE among the inputs, regardless of how many figures each
has. 6371.0 (good to tenths) - 660 (good to units) is good to units:
5711. The skill already states this case correctly.

**Chains of calculation.** Do not round intermediate results. Carry
full precision through every step and round ONCE at the end. Rounding
an intermediate and then using it compounds error.

**Powers, exponentials and other functions.** The counting rules above
are guidelines, not laws, and they were written for products and sums.
For a power like Dp ** (-1/eps), the relative uncertainty of the result
is roughly |exponent| times the relative uncertainty of the base. The
reference's general statement is that the figures in f(x) follow from
the figures in x through the function's condition number. In practice:
apply the fewest-figures rule as the default, and when the function
MAGNIFIES the input's uncertainty (an exponent above one in magnitude,
an exponential of a large argument), drop a figure and say why on the
row.

**When the source states an uncertainty, use it instead.** Significant
figures are a stand-in for an uncertainty nobody wrote down. Where a
paper prints 0.713 +/- 0.003, the uncertainty decides the figures, not
the count. The skill already says this (How many figures is set by the
source's uncertainty, not by taste). It stays the top rule; counting is
the fallback.

**Rounding the last digit.** When the dropped part is exactly half,
round to the even digit (1.25 to 1.2, 1.35 to 1.4). This is the
scientific default because it does not bias a long list of values
upward, and it is what Python's `round()` and `%g` formatting already do.
Half-away-from-zero is the schoolroom rule and is NOT what Python does,
so naming the rule once avoids a later argument with the interpreter.

## 4. The procedure proposed for the skill

Eight rules. Each is method: it resolves the same way next month for a
different constant in a different file, so under Method Belongs to the
Skill none of them is a question for Tony once the set is adopted.

**Rule 1. The figure count is a declared field, `# Figures:`, the
sixteenth comment key.** Like `# Unit:`, it sits beside the value and is
never inferred from the literal. Three forms:

    # Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)
    # Figures: 4 -- source states 4; trailing zero in 3480 is significant
    # Figures: exact -- IAU 2012 definition

A derived row names the input that set its count. A measured row states
what the source supports, and resolves the trailing-zero ambiguity in
words when the literal has one. A defined constant says `exact`.

Why a field and not the literal: a Python float cannot hold a
significant trailing zero (13.50 is stored as 13.5), and an integer
literal cannot say whether its trailing zeros count. The count has to
travel beside the number or the export loses it, and the gallery's hover
then has no way to format the value honestly. This is the same reason
ruling 1 made the unit a field.

**Rule 2. Counting follows the standard rules in section 3**, with one
project-specific consequence: a DECLARED drawing condition (a chosen
solar wind pressure, a chosen cut angle) is an exact number for counting
purposes. It is a choice, not a measurement, so all of its digits are
"known". The magnetosphere rows already treat Dp = 2.0 nPa this way; the
rule writes down why.

**Rule 3. A derived row's count is set by its least-precise MEASURED
input under the operation rules** -- fewest figures for products and
quotients, coarsest decimal place for sums and differences, the
magnification caveat for powers and functions. Exact inputs and declared
conditions are skipped when finding the minimum. Where any input carries
a stated uncertainty, propagate that instead and let it decide.

**Rule 4. Compute from the PRIMARY inputs at full precision; round once.**
A derived row that feeds a second derived row (EARTH_GEOSTATIONARY_RADII
divides EARTH_GEOSTATIONARY_RADIUS_KM, itself derived) does not chain
through the stored, rounded literal. The second row's `# Derived:` line
and the checker's formula both go back to the measured primaries.
Rounding the intermediate would put a rounding error inside the store,
which is the error the reference's chain rule exists to prevent.

**Rule 5. Round half to even, implemented as `float("%.*g" % (n, x))`.**
This is the call test_derived_figures.py already makes. On binary floats
an exact decimal tie almost never occurs, but the rule is named so that
when one does, the interpreter and the skill agree.

**Rule 6 (revised at the ruling). The store holds the derivation, never
a rounded copy.** A derived row stays an expression at full float
precision and follows its inputs automatically. Rounding happens at the
reporting step, and the EXPORT is a reporting step: it rounds each value
to its declared count and carries the count beside the value and the
unit. That answers the September 12 objection (sixteen digits copied
into a gallery config) at the boundary instead of at rest, and it
removes the contradiction in the skill the other way: Report to the
Figures You Have's "stays symbolic" stands, and the September 12
section becomes a WITHDRAWN stub. The two magnetosphere literals stay
literals until the export lands and the gallery stops parsing the
store, then revert to expressions at their slice visit.

**Rule 7. The declared count governs REPORTING; a display may show
fewer, never more.** A hover or export formats to `%.{N}g` using the
served count. A row may carry a supported count of seven and a hover may
show five for readability; the shorter display is not a precision claim.
What is never allowed is a display showing more figures than the row
declares. (EARTH_GEOSTATIONARY_RADII is the live example: its inputs
support seven figures; its row says "report no more than five". Under
this rule the field says 7 and the hover's 5 is a display choice.) The
export carries `figures` beside `value` and `unit`, so the gallery
formats without guessing -- this joins the export design under (c) and
(e).

**Rule 8 (revised at the ruling). The checker judges the DECLARATION,
and a derived row it cannot see FAILS by name.** With the expression
live in Python, the arithmetic follows its inputs on its own, so the
checker no longer recomputes a literal and needs no formula table. It
reads `# Figures:` and checks that a derived row's count does not exceed
the least count among the non-exact inputs it names, that each named
input appears in the expression, and it enumerates derived rows by the
presence of a `# Derived:` line rather than by a `# Status:` word. A
`# Derived:` row with no `# Figures:` line prints NOT YET MIGRATED with
its name -- inside a closed slice that is a FAIL, outside one it is a
named gap, which is the per-slice gate Tony ruled on 2026-09-14. That
turns 25 invisible rows into 25 named rows on the first run.

## 5. What this costs, and where it lands in the walk

Nothing new is walked. The 2026-09-14 ruling already says each row is
visited once, Earth first, and that `# Unit:`, `# Status:` and the
figure count settle at that single visit. Rule 1 names the field that
visit writes. The Earth slice has 12 derived rows (the 10 interior and
near-space rows plus the 2 Hill sphere rows); each visit converts the
expression to a literal, writes the three fields, and adds a formula to
the checker. The 3 Sun rows, the Sgr A* row and the 4 literals-without-
Status follow in their bodies' slices. The 5 exact rows get
`# Figures: exact` and stay expressions.

The skill edit is one bump, provenance-discipline 2.12 to 2.13: the
`# Figures:` key added to the Status Line's key list, the eight rules
under a new heading, the older section's example and scope amended. Per
v3.55's ordering the bump is taken BEFORE the Earth-slice build, and the
next session confirms its loaded copy reads 2.13 before touching the
store.

## 6. What is NOT decided here

(a), (b), (c) and (e) of L-322 stay open. Rule 7's `figures` field in
the export is a dependency on (c) and (e), not a ruling on them. Whether
the field name is `# Figures:` or something else is method and can be
changed in the skill edit without coming back here.

## 7. The one thing asked

Adopt the eight rules as the procedure, so the skill edit can be drafted.
(Adopted; see the RULED line in the header.)
