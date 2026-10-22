<!-- Doc-Kind: hand | Discovery, no fixes: where each feature drawn in the Sun and Earth rooms starts and stops, against the served rows behind each end. -->
# Where the drawings start and stop, against their rows

Built on orrery c0feb22 at https://github.com/tonylquintanilla/palomas_orrery
and gallery b334077 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Written
October 21, 2026 with Anthropic's Claude Opus 5.5.

**Why.** Tony, 2026-10-21, after the corona was found drawn from the
Sun's surface while its own source puts its base 3,000 km higher: "we
should double check our drawings for correct distances." This is the
discovery half. It lists, and fixes nothing.

**How.** Both rooms were built with the website's real renderers from
the served config, and the stored drawings from the served cache. For
every drawn feature, the nearest and farthest drawn point were measured
from the centre, leaving out the info marker. Each end was matched
against every length on the feature's served row, within 1.5 percent.
An end that matches no row is flagged and its cause read from the code
that draws it.

## The result

35 features. 25 have both ends on a served row. The other ten have
twelve ends between them that match no row, in four kinds.

**1. Wrong by its own source (one).**
- **Corona, inner end:** drawn from the Sun's surface, 1 solar radius.
  Mann et al. (2023), Sect. 2, the paper the dots follow: "the bottom
  of the corona is located at a radial distance of 1.0043 R_sun" (R_sun
  for the paper's symbol), about
  3 Mm above the photosphere; the model is only extended down to 1 R_sun.
  The sampler took that as "a definition, not a measurement." Being
  fixed this session: a sourced row for the base, the dots start there.
  The streamer belt, drawn with the corona, also starts at 1 solar
  radius (its declared base_radius), and moves to the same base.

**2. The drawing does not reach where its row says it begins (one).**
- **Outer Oort Cloud (clumps), inner end:** the row says the clumps are
  "drawn beginning here, thin" at 10,000 AU. The nearest drawn dot is
  at 21,360 AU: the drawing places 15 clumps at random between its
  edges, and none falls that close. The far end is on its row.

**3. Ends set by a declared drawing choice, with its reason on the row
(three). Each places dots past a sourced edge.**
- **Hills Cloud, inner end:** dots reach 257 AU, inside the cloud's
  sourced inner edge of 2,000 AU. Every orbit is drawn with the declared
  eccentricity HILLS_CLOUD_ECCENTRICITY = 0.8, and the sampler's note
  says dots near an orbit's near end fall inside the edge "as a real
  body on that orbit would."
- **Inner and Outer Radiation Belts, inner ends:** dots reach 1.016 and
  1.58 Earth radii. Each belt's edges are sourced at the equator; the
  dots follow the dipole field lines from there down to the ground
  ("each belt stops at the ground", a declared choice in
  van_allen_belt_sampler.py). Where along a field line the trapped
  particles actually stop, above the atmosphere, is set by no row.
**4. Ends set by rows that are not lengths, or by sampling (seven).
Consistent with their rows.**
- **Magnetopause and Bow Shock, far ends:** 23.3 and 30.0 Earth radii,
  where each fitted surface is cut at its served cut angle.
- **Magnetotail, inner end:** 30.6 Earth radii, where the page continues
  the magnetopause from its cut; the row says so.
- **Zodiacal Dust Cloud, inner end:** nearest dot 5.36 solar radii; the
  dust-free zone's row is 5 solar radii, and the dust thins to nothing
  there, so few dots fall near it.
- **Galactic Tide, inner end:** nearest dot 10,560 AU against its row's
  10,000 AU, where the drawing begins thin.
- **Hills Cloud, outer end:** farthest dot 19,280 AU against its row's
  20,000 AU, where the disk thins to nothing.
- **Corona, outer end:** 20 solar radii, the streamer belt's last
  points. They are drawn with no opacity past its fade radius, the
  Alfven surface at 19.7, where its row says the band fades to nothing;
  the visible band ends there. (Corrected on a second look: the first
  version of this list counted the belt as reaching past its row.)

## Tony's ruling

"we are in the sun slice now so we should do this now" (2026-10-21):
the Sun's items are settled in this slice, not deferred. The belts are
Earth's, in Earth's slice.

## Not checked here

Whether each SERVED ROW is right against its source. That is the
provenance work already under way slice by slice; this list checks only
that each drawing ends where a row says it does. The orrery's own
drawings were not measured separately: the website draws the orrery's
stored dots as given, and its spheres from the same rows.

## What followed, the same night

Added at the session's close; the list above is as it was found.
- **Corona, inner end:** fixed. A sourced row for the base
  (`CORONA_BASE_HEIGHT_KM`, 3,000 km, Mann et al. 2023); the dots and
  the streamer belt start there (L-460).
- **Hills Cloud, inner end:** fixed, on the rule that a drawing ends
  where its row says. The dots now go only on the part of each orbit
  past the 2,000 AU edge; nearest dot 2,000 AU (L-466).
- **Clumps, inner end:** OPEN, with the clumps' stored drawing (L-434).
- **The two radiation belts, inner ends:** OPEN, in Earth's slice
  (L-413): where the trapped particles stop along a field line needs a
  row, or a declared drawing choice put to Tony.
- **The kind 4 ends:** held as they are, each with its reason.
- **The check:** the website's gallery run gained "Drawn ends"
  (`documentation/smoke_drawn_ends.js`), which measures every end on
  each run, holds eleven by name, and matches within half a percent
  rather than this list's 1.5 percent. The rule is in
  provenance-discipline 2.33, What a Visitor Reads, principle 4.
