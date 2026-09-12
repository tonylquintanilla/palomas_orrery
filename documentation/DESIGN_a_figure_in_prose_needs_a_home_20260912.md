# Design record and review request -- a figure in prose needs a home

Built on orrery `a4ead59ac3f3f390710c99c4e3687d60b444447c`
at https://github.com/tonylquintanilla/palomas_orrery
The gallery is at `1f44673faf2acd32340bfdd4b524b6c8af5dd376` and enters
only at question 3.

Tony Quintanilla, PE | written by Claude Opus 5 | 2026-09-12
Type: DESIGN (zero code). Origin: L-305 and L-321, the outer belt
contradiction. Needs a handle; one is not proposed here.

This document is both the session record and the review request. Read it
as a design to attack, not a decision to ratify. Three of Tony's
rulings are recorded below as ruled; attacking them is welcome and one
of them was made on evidence this document also gives you.

**Note on state.** `patch_L305_magnetosphere_constants.py` sits unrun in
the repo root at this SHA. Nothing below depends on it, and every figure
below is from the unpatched files.

## For a reviewer without the resident layer

Fetch at the orrery SHA above and read before replying:

- `PROJECT_INSTRUCTIONS.md` -- The Braid, The Artifact Bounds the Audit,
  A Check That Cannot Fail Is Not Passing, A Report Names Its Items,
  Fetched vs Recalled Convention, Show the Envelope of the Unknowable.
- `skills/provenance-discipline/SKILL.md` -- When the Source Gives a
  Range, Geometry Constants Are First-Class Claims, One Value One Home,
  A Drawing Approximation Does Not Promote, Report to the Figures You
  Have, The Status Line.
- `skills/orrery-coding-conventions/SKILL.md` -- hover text conventions.

**Name in your reply which of those three you read.** A reply that does
not name them is telling us it did not read them.

Tony Quintanilla is a retired civil and environmental engineer with sole
commit authority, not a professional programmer; the codebase's polish is
two years of AI collaboration. Unpack jargon on first use. Write for him.

## How this started

A visitor opening Earth's magnetosphere can meet three different figures
for the outer radiation belt in one sitting:

- the drawn torus sits at 4.5 Earth radii from centre, which is
  `EARTH_VAN_ALLEN_OUTER_RADII`, the flux peak;
- the plot hover says the belt spans roughly 3 to 7 Earth radii;
- the GUI tooltip, and its twin in `shell_configs.py`, say the belt
  extends 13,000 to 60,000 km above Earth's surface.

Two of the three carry citations.

## The diagnosis, and it is not what it looks like

These strings did not drift away from the store. **They drifted away
from each other, because neither figure was ever in the store.**

The distinction is the whole design. Look at what one string does with
the peak and with the extent, in consecutive lines:

```python
f"Drawn at the flux peak, {EARTH_VAN_ALLEN_OUTER_RADII:g} Earth radii
  from Earth's centre; the belt"
"spans roughly 3 to 7 Earth radii and moves with geomagnetic activity."
```

The peak is INTERPOLATED. It cannot disagree with the drawn torus,
because it is the same object. The extent is TYPED, and it is typed
because there is no constant to interpolate: the store holds a peak and
nothing holds a span. Nothing could have caught the disagreement,
because there was nothing for a checker to compare against.

Tony's framing, which this document adopts: the mechanism is to fetch
the constant into the text as well as into the render, so the two are
associated by construction. That mechanism already exists here. It has
simply never been pointed at an extent.

## The mechanism, already ruled and already worked in this file

`earth_visualization_shells.py`'s own docstring records the 2026-08-26
ruling (L-249): the info strings stop typing their boundary figures and
interpolate `constants_new.py` instead, because the store is the only
home for a numeric value "in prose as much as in code."

`provenance-discipline` carries the range case specifically: where the
source gives a range, store the range as DATA, derive the drawn value
from it by a stated rule, and let display text interpolate the range
rather than restate the drawn value as a measurement.

And the worked pair is in the store, from L-179:

```python
GRAVITATIONAL_INFLUENCE_AU = 150000                    # the drawn value
GRAVITATIONAL_INFLUENCE_RANGE_AU = (100000, 200000)    # the envelope
```

with `solar_visualization_shells.py` interpolating both ends of the
range into its display string.

**Three subjects, one shape.** Each of the three in this slice is a
drawn value that already exists beside a sourced envelope that does not:

| Subject | Drawn value | Sourced envelope |
|---|---|---|
| inner belt | flux peak, in the store | span, typed in two strings |
| outer belt | flux peak, in the store | span, typed in two strings |
| magnetotail | 100 radii, typed twice, in no store | Ness 1967, in no store |

## Measured at the SHA above, by running the real code

**The four typed belt extents.** Two per belt, in two different frames:

| Belt | Plot hover (from centre) | Tooltip and its twin (altitude) |
|---|---|---|
| inner | 1.1 to 2 Earth radii | 1,000 to 6,000 km |
| outer | 3 to 7 Earth radii | 13,000 to 60,000 km |

**Converted, at `EARTH_EQUATORIAL_RADIUS_KM` = 6,378.1 km:**

| Belt | Hover, as altitude | Tooltip, from centre |
|---|---|---|
| inner | 638 to 6,378 km | 1.16 to 1.94 Earth radii |
| outer | 12,756 to 38,269 km | 3.04 to 10.41 Earth radii |

The outer belt's two strings agree at the low end within rounding and
differ by a factor of 1.5 at the high end.

**The inner belt disagrees too, and the L-321 record says it does not.**
That record of 2026-09-11 reads "the inner belt figures are consistent
(1,000-6,000 km altitude against 1.1-2 R_E)." Converted, 1.1 Earth radii
is 638 km, not 1,000; the low ends differ by about 360 km. The record
compared the two figures without converting between them, which is the
same omission the strings themselves make. The worksheet prompts have
been corrected.

**The magnetotail, which is the sharpest case in the slice.** The orrery
draws its tail from `params['tail_length'] = 100` typed at the call site
in `earth_visualization_shells.py`, with a comment and no source. The
gallery serves the same figure a second time as `length_radii: 100.0` in
`data/objects_config.json`. Two hand copies of one drawing choice, in two
repositories, with no store row between them. The sourced extent is in
neither: the gallery's `_declared` prose says the real tail extends "past
1,000 radii", which the 2026-09-11 read record corrected to about 1,000
radii on Ness et al. (1967), whose own title says "probable" and whose
abstract reports a crossing at 900 to 1,050 radii rather than a lower
bound. The orrery's two magnetosphere strings assert "a long magnetotail"
and give no figure at all.

**A range constant does not reach the gallery.** Run against the
gallery's `parse_constants`, `GRAVITATIONAL_INFLUENCE_AU` is in the
parsed set and `GRAVITATIONAL_INFLUENCE_RANGE_AU` is not: the parser
evaluates numeric expressions and a tuple is not one. Ranges are
orrery-only today.

## Tony's rulings

**A. The first slice is the two belts and the magnetotail extent.** That
is what the current artifact renders, and the tail is in because the
orrery draws a tail from a typed figure and states a tail in prose
without one. Out of the slice: Shue's and Jelinek's validity ranges,
which no string carries yet and which item 7 would add; and Lugaz's
corroborating 11 to 14 Earth radii, which the pending L-305 patch
removes from the hover and leaves in the store's own Note.

**B. One frame, and it is the frame the source states -- which means
Earth radii.** The kilometre-altitude presentation leaves the strings
rather than being derived from the radii. Two presentations of one
figure is two chances to be wrong and the conversion is what nobody
performed; the sources state belt extents from centre, Ness states the
tail in Earth radii, and the store already speaks radii. Nothing is
converted anywhere, because there is only one frame to be in.

**C. Design now, values at item 7.** The belt range values are what
L-321's worksheets decide, so storing them before the verdicts return
would mean storing numbers we are about to check. The rows land in the
same patch that rewrites the strings.

## Questions for the reviewer

Attacking rulings A and B is in scope and welcome. B in particular was
ruled on the conversion table above; if keeping a kilometre presentation
is worth more to a visitor than the risk it carries, say so.

1. **Tuple, or two scalars?** `GRAVITATIONAL_INFLUENCE_RANGE_AU` is a
   tuple and the precedent is real. But a tuple takes one `# Unit:` line,
   one `# Status:` line and one `# Source:` block for two numbers that
   may not share a provenance state -- a well-measured inner edge and a
   variable outer edge, say. Two scalars would each carry their own.
   Does the range's coherence justify one row, or is the two-scalar form
   more honest?

2. **Does the checker get a rule, and can it?** The failure this design
   fixes was invisible because nothing related a typed figure to a stored
   one. Is there a check that would have caught it -- and if the only
   honest answer is "a figure that is not interpolated cannot be
   checked," does that make interpolation itself the rule, enforced by
   something that greps display strings for bare numerals?

3. **The tail length, and L-322's export.** The drawn 100 radii is a
   drawing choice, and A Drawing Approximation Does Not Promote says a
   number typed because the result looked right does not earn a store
   row. But this one is typed twice in two repositories, which is the
   failure One Value One Home names. Which rule wins? And separately:
   ranges do not survive the gallery's parser today, so does an envelope
   fit the export's value / unit / source shape, need a second shape, or
   is the honest answer that the gallery serves only what it draws?

4. **Discovery beyond Earth.** Every shell in the orrery has strings with
   typed extents. The Braid says separate discovery from remediation:
   enumerate against a stated pattern over a finite tree, produce a list,
   fix nothing. What is the stated pattern -- is it "a numeral in a
   display string that is not interpolated," and does that terminate, or
   does it collect every date, count and axis label in the codebase?

5. **Naming and reporting.** `EARTH_VAN_ALLEN_OUTER_RANGE_RADII` follows
   the precedent's shape. And Report to the Figures You Have applies to
   an interpolated envelope as much as to a single value: is "3 to 7"
   right, or "3.0 to 7.0", and does the format specifier belong with the
   row or with the string?

## What we do NOT want back

- No patches, no diffs, no code.
- No ledger handles and no ledger blocks.
- Do not re-derive the conversions above. If one is wrong, say which and
  how you would check it.

Prose is fine, and disagreement is the point of asking. Where you think
the framing here is itself wrong, say that first.

Written September 2026 with Anthropic's Claude Opus 5.
