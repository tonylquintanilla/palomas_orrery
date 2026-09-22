# Review of the dipole-tilt addendum rev2 -- tested against the checkers

Built on orrery `a318b3ecfed1ffaa290e8b34ed1ef63caa59295d`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `b17fd92704054e83424651585aa68a393ecb3d92`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io,
the SHAs rev2 names.

**Rules this review runs under.** `skills/provenance-discipline/SKILL.md`
2.16 (loaded in this session; matches the protocol table): Rules 2, 3,
7 and 8, The ceiling, and "When the source gives a range". Also read and
RUN at `a318b3ec`: the `Figures` walker in `test_derived_figures.py`
(lines 153-254, and the header's statement of what it checks), the
`FUNCTIONS` table and verdict lists in `test_dimensions.py` (lines
112-124), and `round_to` and the value field in `export_constants.py`.
**In your reply, name the rule files and sections you read.**

From Claude Opus 5, carried by Tony | 2026-09-21
Type: REVIEW of `ADDENDUM_L322_C2_dipole_tilt_display_rule_fable_rev2_20260921.md`,
Mode 7. No code is asked for.

---

## What stands

Rev2 answers all six findings of the first review, and most of it holds.
The withdrawal from the reply is now stated. The tokens are named. The
enumeration of the proposed Rule 7's reach was done, and assigning the
orrery's display sites to one class with the four `:.4g` sites pulled
into C2 is consistent with The Braid. The ordering is agreed. And the
tilt row is confirmed by the checker itself: its walker counts
`degrees(arctan(sqrt(G11**2 + H11**2) / abs(G10)))` at five figures,
9.41053, as rev2 says.

What follows is what the checkers say about the other two expressions.
The build cannot proceed on either as written.

## How these were tested

The walker in `test_derived_figures.py` was imported and run on each
proposed expression, with stand-in rows carrying the counts rev2
declares for the inputs: main field 6, 5, 5; secular variation 2, 2, 3;
band edges 1 and 1. Results:

| Expression | Walker result |
| --- | --- |
| Tilt, `degrees(arctan(sqrt(G11**2 + H11**2) / abs(G10)))` | 9.41053, 5 figures |
| Rate, as rev2 writes it, with `hypot` | STOP: "the call hypot()" |
| Rate, same formula with `sqrt` in place of `hypot` | -0.0492766, 3 figures |
| Outer belt, `(L4 + L5) / 2` | 4.5, 1 figure |

---

## Finding A. The outer-belt design moves the gallery's ring

Rev2 makes `EARTH_VAN_ALLEN_OUTER_RADII` "the midpoint expression over
[two measured band rows], status declared with the rule on the row,
count exact as a declared pick (Rule 2)". Three facts from the code:

1. The checker's header says "exact" is allowed only when every input
   is exact. The band rows are measured at one figure each, so the
   checker fails a declaration of exact. It allows at most one figure.
2. `export_constants.py` serves each value "rounded to its declared
   figures". At one figure, `round_to(4.5, 1)` returns 4.0.
3. The orrery draws the belt from the row directly
   (`earth_visualization_shells.py` line 838), at full precision, 4.5.

So as specified, either the checker fails the row, or the row declares
what the checker allows and the gallery then draws the outer belt at
L = 4 while the orrery draws it at L = 4.5. That is two consumers of
one row drawing two different rings, which is the parallel-pipeline
failure in its plainest form.

Half of this the skill already settles. "When the source gives a range"
says display text interpolates the range rather than restating the drawn
value as a measurement. So the hover shows the band from its rows and
does not print the drawn 4.5, or its kilometre figure, as a measurement.
That also retires the 28,701.615 km case from item 9 for a reason the
skill states.

The other half the skill does not settle: how a drawn value that is a
pick-by-rule over measured endpoints is counted and SERVED. Rule 2 says
a declared pick is exact. Rule 3 and the checker count an expression
over measured rows from those rows. The export turns the count into the
served drawing value. When the three meet on one row, the drawing moves.
The question for the skill is which governs, and what the checker and
the export must then do with such a row.

## Finding B. The rate row fails both checkers as written

Three separate problems, each checked.

1. **`hypot` is unknown to both checkers.** It is in neither
   `Figures.FUNCS` nor `test_dimensions.FUNCTIONS`. The figures walker
   stops with "the call hypot()". The expression must be written with
   `sqrt(G11**2 + H11**2)`, or both checkers learn `hypot`.
2. **The count is three figures, not two.** Written with `sqrt`, the
   walker gives -0.0493 at three figures. Rev2 reasons that
   "products and quotients" over the two-figure rates set two. But the
   expression contains a sum, `G11*S11 + H11*SH`, and Rule 3 counts a
   sum by decimal place: -10,737 at two figures and -120,500 at three
   are both good to the thousands, so the sum -131,237 carries three.
   The propagated uncertainty from the file's print resolution, about
   0.00013 degrees a year, also supports three. Declaring two is
   permitted by the checker, but the stated reason would be false, and
   under the proposed Rule 7 the hover would then print a count the
   rule did not produce.
3. **The unit check cannot evaluate it.** Rev2 says the unit checker
   sees "a quotient of nT-per-year by nT, dimensionless, times degrees".
   That quotient is per year, not dimensionless. The radian is implicit
   in the arithmetic, and the checker's unit library refuses it:
   `np.degrees` applied to a per-year quantity raises "Can only apply
   'degrees' function to quantities with angle units". Tested with
   astropy directly. `test_dimensions.py` uses no angle equivalency,
   and CANNOT EVALUATE is on its FAILING list, not a NOT CHECKABLE
   gap. Inside a closed slice that fails the run.

The third is a method question the skill should answer, because every
rate of an angle will meet it (Earth's pole, the Moon's node): how a
rate of an angle is written so the unit check can follow it. One route
is for the unit check to treat the radian as dimensionless, which
astropy supports as an explicit equivalency; that is a checker change,
so it belongs in C2's scope if chosen. There may be others.

## Finding C. A detail in the reach enumeration

Rev2 says the four `:.4g` standoff sites would print "10.25 where the
row says 10.3". After C2 the store no longer holds 10.25; the sites
print whatever the new expression computes, to four significant
figures, which can exceed the declared three. The conclusion, that the
four come into C2, is unchanged.

## Finding D. The deferred class has no checker

The orrery's forty-odd display sites go to one ledger class. No checker
reads orrery display formatting, so after Earth closes, those sites will
be visible only as that ledger row. That is consistent with The Braid;
it should be stated on the row, so nobody reads a closed slice as
covering them.

---

## What comes back

A revision, anchored, that names the rule files read and:
- settles finding A as method: how a pick-by-rule over measured
  endpoints is counted and served, and what the checker and the export
  do with such a row;
- rewrites the rate row so both checkers can judge it, at the count the
  walker gives or with a stated reason for a lower one, and says as
  method how a rate of an angle passes the unit check;
- corrects the detail in finding C and adds the statement in finding D.

---

Written September 21, 2026 with Anthropic's Claude Opus 5.
