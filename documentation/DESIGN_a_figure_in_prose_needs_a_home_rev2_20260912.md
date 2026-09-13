# Design record -- a figure in prose needs a home (revision 2)

Built on orrery `62ee5149e611e325455e56bb3b09486daeea0040`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `1f44673faf2acd32340bfdd4b524b6c8af5dd376`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-12
Type: DESIGN (zero code). Handle: L-323.
**Supersedes** `DESIGN_a_figure_in_prose_needs_a_home_20260912.md`, which
was written as a review request and is kept as the record of the round
that produced this one.

Revision 1 asked five questions and recorded three rulings. A Fable
review round answered the questions, corrected the diagnosis and amended
one ruling, and a measurement today corrected a fourth thing. This
revision states the design as it now stands, so that a session opening
L-323 next does not rebuild it from the questions.

A second review round read this revision before it landed. Its
corrections are folded in: the peak rows are disposed of rather than
only noted, the magnetotail row is given a FORM instead of being called
an envelope, and the unit token is named so item 7 does not have to
invent one.

## What changed from revision 1

**1. The diagnosis was wrong, and the correct one is a better rule.**
Revision 1 said the span figures were never in the store. They are in
the store -- as PROSE, in each belt row's `# Note:` line. The inner
row's Note says the belt spans roughly L = 1.1 to 2; the outer row's
says L = 3 to 7. The gallery's `objects_config.json` repeats both word
for word.

So the failure is not an absent figure. It is a figure held where
nothing can interpolate it and nothing can check it, with every
downstream copy typed from that prose by hand. **A Note became a
store.** That is a class, and it recurs wherever a row carries a figure
in its Note that the row's value does not hold. It has already drifted
inside one row: the outer belt's `# Source:` cites Baker et al. (2018)
at r ~ 3 to 6.5 R_E from SAMPEX, and its `# Note:` three lines below
says L = 3 to 7 -- a different upper edge, a different frame, no Source
line on that row stating it.

**2. There are three frames, not two.** Revision 1's conversion table
compared Earth radii from centre against kilometres of altitude and
missed the frame the store itself uses. The store Notes say L. The
hovers say Earth radii from Earth's centre. The info text says
kilometres above the surface.

L is the McIlwain L-shell: the distance, in Earth radii, at which a
magnetic field line crosses the magnetic equator. For a dipole it equals
geocentric radius AT THE EQUATOR and nowhere else -- a belt spanning
L = 3 to 7 reaches much lower altitudes at high latitude. The hover was
written from the Note and dropped the L. That is the same silent frame
change revision 1 caught in the L-321 prompts, one layer earlier. The
peak rows have it too: the sources put the outer peak at L = 4 and 5,
and the store row calls it R_E.

**3. Two skills state the range rule and one is the superseded form.**
`provenance-discipline` (When the Source Gives a Range) says store the
range as data and interpolate it, and says in so many words that this
supersedes the weaker form. `orrery-coding-conventions` 1.8
(Visualization Constant vs Range Convention) still teaches that weaker
form -- best value in code, range in the comment -- with a worked
example. The belt rows are not a violation of anything; they are that
weaker convention executed correctly. A fresh session loading the coding
skill for hover work would rebuild the failure. One ledger row by class,
recorded in L-323's Notes.

**4. The altitude figures are not where revision 1 put them.** Measured
at the SHA above, and re-measured at `a4ead59a`, revision 1's own SHA,
so this is not something a later patch moved.

All four typed extents live in ONE file, `earth_visualization_shells.py`:

| Figure | Where | Line |
|---|---|---|
| inner belt, 1,000 to 6,000 km altitude | `earth_magnetosphere_info` | 745 |
| outer belt, 13,000 to 60,000 km altitude | `earth_magnetosphere_info` | 747 |
| inner belt, spans roughly 1.1 to 2 Earth radii | `belt_texts` | 892 |
| outer belt, spans roughly 3 to 7 Earth radii | `belt_texts` | 896 |

The `shell_configs.py` tooltip carries NO span in either frame. It gives
the two flux peaks, both interpolated from the store, plus the standoff
attributions. Revision 1 said the tooltip and "its twin" state the
13,000 to 60,000 km extent; they do not, and did not at its own SHA.
The twin is a partial one, and on exactly the figures at issue here it
is already doing the right thing.

## The diagnosis, corrected

A visitor opening Earth's magnetosphere can meet three figures for the
outer belt in one sitting: the drawn torus at 4.5 (the flux peak,
interpolated from `EARTH_VAN_ALLEN_OUTER_RADII`), the hover's "spans
roughly 3 to 7 Earth radii", and the info text's "13,000 km to 60,000
km above Earth's surface".

The peak INTERPOLATES. It cannot disagree with the drawn torus, because
it is the same object. The extents are TYPED, and they are typed because
no VALUE holds them -- only a Note does. Nothing could have caught the
disagreement, because nothing existed for a checker to compare against.

The mechanism is the one revision 1 proposed and Tony framed: fetch the
constant into the TEXT as well as into the render, so the two are
associated by construction. It already exists here and has simply never
been pointed at an extent. `solar_visualization_shells.py` interpolates
both ends of `GRAVITATIONAL_INFLUENCE_RANGE_AU` (L-179) and prints two
units from one constant by arithmetic inside the f-string.

## The peak rows are two cases, not one

The frame problem reaches the two peak rows as well as the spans, and
they do not resolve the same way. Both rows are touched by this slice --
their Notes lose the span -- so this is forward-going on rows touched,
not a sweep.

**The outer peak row's unit is wrong, and the fix lands in the same
patch.** `EARTH_VAN_ALLEN_OUTER_RADII = 4.5` is the midpoint of L = 4
to 5, which is what the row's own Source line says: the CIRBE/REPTile-2
paper puts the belt most intense around L = 4 and 5, Kellerman et al.
(2014) gives maximum electron flux at L = 4-5, and the row records
"Midpoint of that band." The value is derived from an L band and the
row calls it R_E. That is a conversion nobody performed, the same shape
as the one this design exists to fix. Its unit moves to L. Baker's
figure on that row is the SPAN (r ~ 3 to 6.5 R_E from SAMPEX), not the
peak, and it belongs with the edge rows.

**The inner peak row is not a relabel and is left to the worksheets.**
`EARTH_VAN_ALLEN_INNER_RADII = 1.5` carries two sources in two frames
for the same number: Baker et al. (2018) states inner-zone proton
fluxes peaking near geocentric r ~ 1.5 R_E, and the CIRBE/REPTile-2
paper states the inner belt centred near L = 1.5. Relabelling the row
to L would drop Baker's frame; leaving it R_E drops the other. The two
agree numerically, which at the equator they would, and that agreement
is not evidence about which frame the row is in. L-321 prompt 3 rows 2
and 5 ask the question; the row's unit is settled at item 7 by what
comes back, not here.

This is why a checker returning PARTIAL on "Citation correct?" for the
frame alone is a correct verdict on those rows and should be expected
rather than treated as a defect.

## The rulings, as they now stand

**A. The first slice is the two belts and the magnetotail extent.**
Stands. That is what the artifact renders. The tail is in because the
gallery already asserts an extent in prose ("past 1,000 radii"), so the
claim is rendered and inside the bound. Out of the slice: Shue's and
Jelinek's validity ranges, which no string carries yet and which L-305
item 7 would add; and Lugaz's corroborating 11 to 14 Earth radii, which
the L-305 item 4 patch removed from the bow shock hover and left in the
store's own Note.

**B. AMENDED. One frame in the STORE, and it is L. Presentations in the
STRING are derived from it.**

Revision 1 ruled "the frame the source states, which means Earth radii".
The conclusion was right and the frame was wrong: the frame the sources
state for both belts is L, not geocentric R_E. Calling it R_E in the
store is a conversion nobody performed -- one level below the conversion
revision 1 caught.

And the binary was false. "One frame" and "a kilometre presentation" are
not opposed. A belt string can print the stored L and derive an
equatorial altitude from it in the same line, and the two cannot
disagree because one is computed from the other. That is the
by-construction association, applied twice. The coding skill's Hover
Text AU Convention -- every distance hover carries two units -- is a
standing rule that B as originally worded would have broken.

So: the store holds L. The string may print as many derived
presentations as help a visitor, each computed from the row. The
altitude figures leave the strings as TYPED numbers and may come back as
ARITHMETIC. Whether a lay visitor is better served by kilometres is
Tony's call at item 7; the design does not need the ruling either way.

**C. Design now, values at item 7.** Stands without reservation. The
belt range values are what L-321's worksheets decide, so storing them
before the verdicts return would mean storing numbers we are about to
check. The rows land in the same patch that rewrites the strings.

## The five questions, answered

**1. Tuple, or two scalars? Two scalars.**

Provenance is per number: the outer belt's outer edge moves with
geomagnetic activity and its inner edge does not, so one `# Status:` on
a tuple would force one state on two things. The checker's derived rule
names INPUTS and resolves top-level scalars; naming a tuple's element is
a form nothing in the file uses. And the gallery's parser evaluates
numeric expressions, which a tuple is not -- two scalars reach the
served side in the existing value / unit / source / pointer shape with
no parser change.

Names: `_INNER_EDGE` and `_OUTER_EDGE` per belt. The precedent's
`_RANGE_` shape does not carry to two rows, and `_LOW` / `_HIGH` would
not survive the inner belt, whose high edge sits below the outer belt's
low one. Unit: L.

`GRAVITATIONAL_INFLUENCE_RANGE_AU` is NOT migrated. Braid: forward-going
on rows touched. It is one line of backlog by class -- range rows held
as tuples: 1.

**2. Does the checker get a rule? Interpolation IS the rule, and it is
already written.** One Value One Home covers prose. What failed was not
the rule but the detection: the provenance scanner flags number-plus-unit
tokens in display strings, and "3 to 7 Earth radii" is one, but the same
string carries "Source (peak): Baker..." and the scanner's window
credits the whole block. A citation for the PEAK cleared the SPAN.

So no new tool. A grep for bare numerals would be a second, worse copy
of the scanner, which already has a unit vocabulary, an exceptions file
and a run history. The fix is the window inference -- a citation should
clear the figures it NAMES, not the block it sits in -- and that is
L-322's.

**3. The magnetotail splits into two numbers.** Neither rule wins,
because they are not about the same number.

- The DRAWN 100 radii (`params['tail_length'] = 100`,
  `earth_visualization_shells.py` 765) is a shape, in the same family as
  the 15-radius base and 25-radius end beside it. A Drawing
  Approximation Does Not Promote says no store row, and One Value One
  Home's own scope boundary agrees: declared drawing parameters stay
  where they are drawn. The gallery's `length_radii: 100.0` is a served
  drawing parameter, the same kind of parallel copy as every opacity in
  `objects_config.json`.
- The OBSERVED extent earns a row, because prose already states it and
  Show the Envelope says the hover must. Its form is ONE SCALAR holding
  a LOWER BOUND, not two edges and not a tuple. Ness, Scearce and
  Cantarano (1967) report a single Pioneer 7 crossing at 900 to 1,050
  radii, with "probable" in the title and no coherent tail -- a
  signature, not a tail. A two-scalar near/far pair would assert two
  EDGES of an extent, and the source reports one crossing whose
  distance is uncertain within a band; that is a different object, and
  stating it as an extent would be the same invented precision this
  design exists to remove. So: value = the near edge of the crossing
  band, read as "observed to at least", with the band, the single
  crossing and the "probable" caveat on the row's own Source line, and
  the string saying "observed to at least" rather than "extends to".
  Provisional: L-321 prompt 1 row 7 asks whether a later open source
  restates or supersedes Ness, and a source reporting a sustained tail
  rather than one crossing would change the form to two scalars.
- Two later deep-tail campaigns are candidates for the checkers to
  verify, not figures to store: ISEE-3's 1983 passes and Geotail's
  early orbits, both a few hundred radii downstream. They are named
  from recall rather than from an opened source, which is exactly why
  they are a question for prompt 1 row 7 and not a value.
- The hover then says both, and cannot drift from either: the 100
  interpolates the drawing parameter from where it is drawn, the
  observed figure interpolates the store. Two numbers, two homes, one
  sentence.

**4. Discovery beyond Earth: read the enumerator that exists.** The
pattern is already stated in code -- the scanner's numeric-claim regex,
a number plus a unit from its vocabulary, in a display string. It
terminates because the tree is finite, and its output is already a list:
`PROVENANCE_AUDIT.md`'s display-string class. Dates carry no unit and
are excluded; axis labels carrying "AU" or "km" will appear and are a
class to name and set aside. Do not write a second enumerator. Split the
existing list by whether the numeral is interpolated, which is a grep
for `{` inside the flagged strings. That split is the only new work.

**5. Reporting: "3 to 7", not "3.0 to 7.0".** The sources give integers,
Report to the Figures You Have says report what the input supports, and
`:g` prints 3.0 as 3. The figure count is stated on the row in prose, as
the file already does. The format specifier lives with the STRING, per
the `:.4g` ruling of 2026-09-12, and waits on L-322(d) for the declared
form -- the same interim as the standoffs, no new entrenchment.

## What lands, and where

At L-305 item 7, after L-321's verdicts return:

- Four belt scalars: inner edge and outer edge per belt, unit L, each
  with its own `# Source:` and `# Status:`.
- One row for the observed magnetotail extent, a lower bound in Earth
  radii, in the form set out under question 3.
- `EARTH_VAN_ALLEN_OUTER_RADII`'s unit moves from R_E to L, because its
  value is the midpoint of an L band.
- `EARTH_VAN_ALLEN_INNER_RADII`'s unit is settled by what the
  worksheets return, for the reason in "The peak rows" above.
- The four typed extents in `earth_visualization_shells.py` become
  interpolations; any kilometre presentation becomes arithmetic on the
  stored L.
- The store's belt Notes stop carrying a span, because the rows will.

**The unit token is `l_shell`, not `l`.** The store's `# Unit:`
vocabulary today runs r_earth, dimensionless, per_nt, nt, npa, km_s,
deg. L is dimensionless with a meaning, and the gallery's value / unit /
source shape carries whatever token the row states, so a reader who has
not met McIlwain meets it here. The vocabulary itself is L-322 ruling
1's, not this design's; naming the intended token now is what keeps item
7 from inventing one under time pressure.

**A boundary on L-305 item 6.** Item 6 serves the magnetosphere shape
parameters to the gallery and retires three claims there. It must NOT
touch the belt `note` fields in `data/objects_config.json` that repeat
the span prose. Those change at item 7 with the edge rows. Editing them
at item 6 and again at item 7 is the same double-store failure this
design is about, performed on the fix.

Not in this slice, and not forgotten: the Shue and Jelinek validity
ranges (item 7 would add them), the Lugaz corroboration (stays a Note),
`GRAVITATIONAL_INFLUENCE_RANGE_AU` (one class row).

## What is still open

- Whether a visitor is better served by a derived kilometre
  presentation alongside L. Tony's call, at item 7.
- The inner peak row's frame, which two sources state two ways for the
  same number. L-321 prompt 3 decides it.
- Whether Ness is restated or superseded, which decides whether the
  magnetotail row stays a lower bound or becomes two scalars.
- The scanner's citation window, which is what made this class
  invisible. L-322.
- The range rule stated in two skills, one superseded. L-323's Note.
- The belt edge VALUES themselves, which the L-321 worksheets decide.
  Revision 3 of those prompts accompanies this document.

Written September 2026 with Anthropic's Claude Opus 5.
