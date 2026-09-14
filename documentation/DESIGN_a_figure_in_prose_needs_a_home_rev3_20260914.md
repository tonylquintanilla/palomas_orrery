# Design record -- a figure in prose needs a home (revision 3)

Built on orrery `2f1a0c2f03a15927a6667bf4297f2a07991bfdfe`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `eab070a94e53296c05b384eb342085884ef56341`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-14
Type: DESIGN (zero code). Handle: L-323. Serves L-305 item 7.
**Supersedes** `DESIGN_a_figure_in_prose_needs_a_home_rev2_20260912.md`,
which remains filed as the record of the design as it stood BEFORE the
checkers returned.

Revision 2 was written while the L-321 worksheets were still out. Four
checker legs returned on 2026-09-13, and a source-recovery pass opened
what one of them had named. They sourced the figures revision 2 expected
to be unsourced, removed the stated reason for one ruling, reversed one
verdict and moved the magnetotail figure. Tony ruled the frame question
and the kilometre presentation on 2026-09-14.

This revision states the design as it now stands, because the session
that builds L-305 item 7 reads this document rather than a handoff.

## What changed from revision 2

**1. The extents are SOURCED. Item 7 is a citation job, not a removal
job.** Revision 2 predicted UNSOURCED across the four extent rows and
planned around losing them. Three open full-text sources state them:

- Meredith, Horne, Kersten, Fraser and Grew (2014), "Global morphology
  and spectral properties of EMIC waves derived from CRRES
  observations", J. Geophys. Res. Space Physics 119, 5328-5342,
  doi:10.1002/2014JA020064. Introduction, first paragraph: the inner
  belt extends from about 1.1 to 2 Earth radii in the geomagnetic
  equatorial plane; the outer belt from 3 to 7 R_E. OPEN, NERC
  repository.
- Li, Tu, Selesnick and Huang (2024), "Modeling the contribution of
  precipitation loss to a radiation belt electron dropout observed by
  Van Allen Probes", J. Geophys. Res. Space Physics 129, e2023JA032171,
  doi:10.1029/2023JA032171. Introduction, first paragraph: the outer
  belt extends from about 3 to 7 Earth radii. OPEN, NSF PAR.
- Koskinen and Kilpua (2022), chapter 1, open access at Springer.
  Equatorial geocentric R_E, stated outright in the chapter's own
  footnote 2.

**2. Ruling B's stated reason is gone.** Revision 2 held that the store
carries L because L is the frame the sources state. They state geocentric
Earth radii. The RULE was right and the FACT under it was wrong, which is
why ruling B changes rather than the reasoning behind it.

**3. The literature is mixed, so the frame has to live on the row.**
Y. X. Li et al. (2023) states 3 to 7 as L shells. Baker et al. (2018)
states the outer extent both ways: r ~ 3 to >= 6.5 R_E from SAMPEX, and
L ~ 3.0 to 6.5. Li et al. (2025) states the outer peak in L. So "the
frame the source states" yields one answer only once the row names WHICH
source its figure follows. A row reading `r_earth` with no paper pinned
can be contradicted by a paper somebody opens next year. A row reading
`r_earth`, geocentric equatorial, per Meredith 2014, cannot.

**4. The inner span changes its source, on SCOPE rather than on
figure.** Koskinen and Kilpua state 1.1 to 2 R_E for the inner ELECTRON
belt, and put the energetic protons over about 1.1 to 3 R_E in the same
section. Our hover calls the inner belt "mainly protons". Citing
Koskinen and Kilpua would put an electron extent under a proton label --
the figure matching while the scope does not. Meredith 2014 states 1.1
to 2 for the inner belt with no species qualifier, so it is the cleaner
source and Koskinen and Kilpua become corroboration.

**5. Row 9's NO reverses, and the outcome does not.** A checker called
60,000 km physically impossible because 10.4 R_E sits outside our own
10.25 R_E magnetopause. Koskinen and Kilpua put the outer belt's reach
at 7 to 10 R_E, and the belt's outer edge approaching the magnetopause
is why magnetopause shadowing is a standard loss mechanism. So the
figure is not impossible. It still goes, for the reason in "The altitude
pairs" below: nothing peer-reviewed states it, and our own stored span
does not support it.

**6. The magnetotail figure is 220 R_E, not the near edge of Ness's
band.** Tony's ruling, 2026-09-13. Revision 2 had the row holding the
900 of Ness's 900 to 1,050. Three figures with three meanings were on
the table:

| Figure | Source | What was measured |
|---|---|---|
| 220 R_E | Slavin et al. (1983), Geophys. Res. Lett. 10 | a tail keeping much of its near-Earth structure, ISEE-3 |
| 900-1,050 R_E | Ness, Scearce and Cantarano (1967) | connected field lines, intermittent over a week, no coherent tail |
| 3,100 R_E | Intriligator et al. (1979), Geophys. Res. Lett. 6:585 | tail-ASSOCIATED phenomena, later read as field lines disconnected from Earth |

220 is the only one where the thing measured is the thing the hover
names. Ness and Intriligator go on the row's Source line as the more
distant signatures, so a later session does not read the choice as
ignorance of them.

Two corrections to revision 2's reading of Ness, both from the GSFC
preprint rather than the abstract. It is NOT a single crossing: Pioneer
7 was in the expected tail region from 26 September to 3 October 1966
and tail-like fields appeared intermittently as the solar wind swept the
tail across it. And the paper is reachable in full -- NASA NTRS serves
preprint X-612-67-183, same authors and title, where the JGR pages are
walled. The same preprint records Explorer 33 seeing a well-defined tail
and neutral sheet out to 80 R_E.

## The diagnosis, unchanged

A visitor opening Earth's magnetosphere can meet three figures for the
outer belt in one sitting: the drawn torus at 4.5, the hover's "spans
roughly 3 to 7 Earth radii", and the info text's "13,000 km to 60,000 km
above Earth's surface".

The peak INTERPOLATES from `EARTH_VAN_ALLEN_OUTER_RADII`, so it cannot
disagree with the drawn torus -- it is the same object. The extents are
TYPED, and they are typed because no VALUE holds them. Both belt rows
carry their span in a `# Note:` line instead, and the gallery's
`objects_config.json` repeats that prose word for word. A Note became a
store. Nothing could have caught a disagreement, because nothing existed
for a checker to compare against.

The mechanism is unchanged: fetch the constant into the TEXT as well as
into the render, so the two are associated by construction.
`solar_visualization_shells.py` already does it for both ends of
`GRAVITATIONAL_INFLUENCE_RANGE_AU` (L-179).

## The rulings, as they now stand

**A. The first slice is the two belts and the magnetotail extent.**
Stands. Out of the slice: Shue's and Jelinek's validity ranges, and
Lugaz's corroborating 11 to 14 R_E, which stays in the bow shock row's
Note.

**B. AMENDED AGAIN, Tony's ruling of 2026-09-14. The store holds
geocentric equatorial Earth radii, and every belt row names the frame
and the paper its figure follows.**

Unit token: `r_earth`, the vocabulary's existing one. No new token is
needed for the extent rows.

The frame is stated on every belt row. WHERE it is stated is L-322's to
settle, not this design's: a new `# Frame:` comment key is inert until
the exporter reads it, and the export shape is L-322's work. Until then
the frame goes in the row's own `# Source:` line, in the source's words
-- "in the geomagnetic equatorial plane" is Meredith's phrase, not ours
-- and a later `# Frame:` key can lift it out mechanically.

`l_shell` is still needed, for exactly one row. Revision 2 introduced
the token for the extent rows, which no longer need it. The outer peak
row does: its value is a midpoint of an L band and stays in L.

**C. Values at item 7.** Discharged. The verdicts are back and the
values are below.

## What each row holds

Four new scalars, one new row, two existing rows corrected.

| Row | Value | Unit | Source opened | Access |
|---|---|---|---|---|
| `EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE` | 1.1 | r_earth | Meredith et al. (2014), intro para. 1 | OPEN |
| `EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE` | 2 | r_earth | Meredith et al. (2014), intro para. 1 | OPEN |
| `EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE` | 3 | r_earth | Meredith et al. (2014); Li, Tu et al. (2024) | OPEN |
| `EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE` | 7 | r_earth | Meredith et al. (2014); Li, Tu et al. (2024) | OPEN |
| `EARTH_MAGNETOTAIL_OBSERVED_RADII` | 220 | r_earth | Slavin et al. (1983), NTRS 19830066648 | ABSTRACT |
| `EARTH_VAN_ALLEN_INNER_RADII` (peak) | 1.5 | r_earth | Baker et al. (2018), sec. 2 | OPEN |
| `EARTH_VAN_ALLEN_OUTER_RADII` (peak) | 4.5 | l_shell | Li et al. (2025), sec. 1 | OPEN |

The names follow revision 2's `_INNER_EDGE` / `_OUTER_EDGE` per belt,
written out as `_INNER_BELT_` / `_OUTER_BELT_` because the existing rows
already spend the word "inner" on the belt.

**The earlier work is recorded as the next layer down, not as the
source.** Meredith and Li state these extents in their introductions,
passing on earlier work: Baker et al. (2007) for the inner span,
Paulikas and Blake (1979) with Baker et al. (1986) for the outer,
Ganushkina et al. (2011) and Van Allen et al. (1958) for Li's. The
Access Standard already rules this -- the Source records the document
opened -- and the row carries the rest one layer down so a later session
can climb it.

**Baker's tighter figure is recorded on the outer edge row.** Baker et
al. (2018) gives r ~ 3 to >= 6.5 R_E from SAMPEX, which is a measuring
review rather than an introduction, and it disagrees with the stored 7
on the outside. It goes in the row's Note with its frame, so the
disagreement is visible instead of resolved by silence.

**The inner peak row keeps `r_earth`.** Baker et al. (2018) sec. 2
places the inner-zone proton flux peak near geocentric r ~ 1.5 R_E, and
that is the frame our row is in. The CIRBE/REPTile-2 paper's L = 1.5
stays on the row as the second reading of the same number, recorded as
a different frame rather than as agreement.

**The outer peak row's unit moves to `l_shell`, and its status is
`declared`.** The value is the midpoint of L = 4 to 5. The word
"derived" describes it in English, but the store's status grammar
reserves `derived` for a row computed from named top-level constants in
the same file -- `test_status_lines.py` rule 7 fails a derived row whose
inputs are not there, and L = 4 and L = 5 are not rows. A pick from a
range is a declared choice, which is what the provenance skill already
says. The range carries the citation and the pick carries its reason.

**Baker drops off the outer PEAK citation.** The string currently names
both Li (2025) and Baker (2018) for the 4.5. A checker found that
Baker's figure 30 uses L* = 4.5 as a selected analysis location rather
than identifying a universal peak, and that his figure 12 concerns
variable peak positions. Baker supports the outer belt's SPAN, not its
peak, and the two figures move to the rows where they belong.

**The hover says "at the equator" wherever it prints the outer peak**,
because L equals geocentric distance in Earth radii only where a field
line crosses the magnetic equator.

## The kilometres stay, and they are a conversion

Tony's ruling, 2026-09-14. The typed pairs go; a kilometre presentation
stays and is DERIVED from the Earth-radii rows at render time. No second
pair is stored.

Why keep kilometres at all: a visitor has no feel for 1.1 Earth radii,
and six hundred kilometres up is a number a person can place against the
ISS. Dropping them would make the panel more honest and less legible,
and the gallery's point is that both hold.

Why derive rather than cite: the unit was never the problem, the pairs
were. `earth_magnetosphere_info` states 1,000 to 6,000 km for the inner
belt (line 745) and 13,000 to 60,000 km for the outer (line 747). No
peer-reviewed source states either as written. What the checkers found
was a modelling preprint's introductory background, whose own conversion
to Earth radii is internally inconsistent; a magazine article; a news
article; and a university mission-announcement page. Baker's own 2018
review disagrees with the outer pair. Storing a kilometre pair as its
own sourced row would also be two rows for one quantity, one of them
arithmetic on the other, which is what L-325 ruled against.

The panel changes visibly, and that is the correction landing rather
than a cost to manage.

**Round to the precision the source carries.** The extents are schematic
and carry one or two figures, so a four-digit altitude claims precision
the input does not have. Roughly 600 to 6,400 km for the inner belt and
roughly 13,000 to 38,000 km for the outer, or tighter rounding if it
reads better.

The rounding happens in the FORMAT, not in the text. Every printed
kilometre figure stays arithmetic on its row, because a rounded number
typed into a string is the failure this design removes, one digit
smaller. The four strings share one small rounding helper and item 7
picks its exact form; what it must not do is type 600.

**Subtract `EARTH_EQUATORIAL_RADIUS_KM`, and this corrects revision 3's
own first draft.** That draft said to use `EARTH_MEAN_RADIUS_KM` (6371.0)
because Koskinen and Kilpua define R_E as 6370 km. Reading the render
settles it the other way. Belt positions are scaled by `EARTH_RADIUS_AU`,
which `earth_visualization_shells.py` line 1015 records as
equatorial-based at 6,378.137 km, and L-178 retired a local
`EARTH_RADIUS_KM = 6371.0` as a shadow constant for exactly this reason:
mixing the mean radius into equatorial-based geometry put a +0.112
percent error in every altitude band. Every `_RADII` row in
`constants_new.py` already divides by the equatorial constant -- core,
mantle, geostationary, LEO. A hover subtracting a different Earth from
the one the torus is drawn against would be two Earths in one exhibit.

At the rounding above the two constants print the same figures, so this
is about which pointer the drift check follows, not about the number.
The same goes for the sources' own R_E definitions, which differ by a
few kilometres and disappear at one or two significant figures.

**Label it in the hover as a conversion.** Something in the shape of
"roughly 600 to 6,400 km above the surface at the equator (converted
from Earth radii)". This is Show the Envelope's approximate-and-say-so
branch: the kilometres are not a second measurement and must not read as
one. The "at the equator" is load-bearing twice over -- for the outer
peak because L equals geocentric distance only where a field line
crosses the magnetic equator, and for every belt figure because the
sources state them in the geomagnetic equatorial plane.

**The peaks get the same treatment**, Tony's ruling of 2026-09-14 in
answer to a review question. 1.5 R_E is about 3,200 km above the
surface, 4.5 is about 22,000 km, both by the same derivation, the same
rounding and the same conversion label.

## What lands at item 7, and where

- Four belt edge scalars in `constants_new.py`, unit `r_earth`, each
  with its own `# Unit:`, `# Status:` and `# Source:`.
- One magnetotail row at 220, form unchanged from revision 2: a single
  scalar read "observed to at least", with the three distances and their
  three meanings on the Source and Note lines.
- `EARTH_VAN_ALLEN_OUTER_RADII` unit to `l_shell`, status `declared`,
  Baker removed from its citation.
- `EARTH_VAN_ALLEN_INNER_RADII` unit stays `r_earth`.
- Both belt rows' `# Note:` lines stop carrying a span, because the new
  rows hold it.
- The four typed extents in `earth_visualization_shells.py` become
  interpolations: `belt_texts` lines 892 and 896, and
  `earth_magnetosphere_info` lines 745 and 747.
- The kilometre figures in those same strings become arithmetic on the
  rows, subtracting `EARTH_EQUATORIAL_RADIUS_KM`, rounded in the format,
  labelled as a conversion, with the peaks treated the same way.
- One small rounding helper, shared by those strings, so no printed
  kilometre figure is ever typed.
- The belt `note` fields in the gallery's `data/objects_config.json`,
  which repeat the span prose. Item 6 was fenced off these on purpose
  so they are edited once, here.
- A live store-drift run reading MATCH by name for every new pointer,
  then Mode 5 on the render.

## What is still open

- Standoff precision: whether the hover prints 10.25, 10.3 or "about
  10", and the same question for 13.51. Carried from the 2026-09-13
  handoff.
- Where the frame is stated once the export shape is settled. L-322.
- The scanner's citation window, which is what made this class
  invisible: a citation should clear the figures it NAMES, not the block
  it sits in. L-322.
- The range rule stated in two skills, one in its superseded form.
  L-323's Note.
- `GRAVITATIONAL_INFLUENCE_RANGE_AU` stays a tuple. One ledger row by
  class: range rows held as tuples, 1.

Written September 2026 with Anthropic's Claude Opus 5.
