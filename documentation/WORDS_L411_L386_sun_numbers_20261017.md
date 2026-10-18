<!-- Doc-Kind: hand | Wording list for Tony's approval: every visitor-facing change from L-411 groups W, S, D, N and L-386, before and after. Revision 2. -->
# The Sun's numbers: the wording list (L-411 and L-386), revision 2

Built on orrery 6f4fc9b0e85bf27920cea5bc9e664ee85455bcf1 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
da442bf21c7d90bffc775e8f5e58d751265a1aa2 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Written 2026-10-17 by Anthropic's Claude Opus 5.5. L-228's list,
approved earlier tonight, is not repeated here.

Revision 2, after Tony's two questions at 22:25: temperatures in
kelvin, and the three removals that did have sources. Sedna, the
termination shock's range and the wind's speed are back, each from a
source, and the Celsius wording is gone.

Every "after" below is what the code printed when run on this
session's working copies, not what was intended.

## What changes in fact or in the drawing

These come from the sources, by rule, not by choice. They are listed
first because they change what a visitor learns or sees.

1. **The core is drawn at 0.25 solar radii, not 0.2, on both sites.**
   The 0.2 rested only on a textbook nobody here can open. NASA/Marshall's
   solar interior page (Hathaway) says "the innermost 25%".
2. **The radiative zone's edge prints 0.71, not 0.713.** It is still
   drawn at 0.713. The source's +/- 0.003 supports two figures by the
   figure rule.
3. **Parker Solar Probe's closest approach prints 9.85 solar radii from
   the Sun's center, not "~8.8".** 8.8 was the height above the surface.
   So MAPS's break-up at 8.33 was well inside Parker's distance, not "just
   inside": that sentence changes.
4. **The photosphere is about 100 km thick, not 500, and about 5,700 K,
   not 5,500** (NASA/Marshall). On the website both change. In the
   orrery only the thickness changes tonight: its temperature sits beside
   a wavelength worked out from it, and the two move together later.
5. **Temperatures stay in kelvin.** NASA/Marshall prints the interior's
   in degrees Celsius; the words convert them, which changes no printed
   figure (15 million, 7 and 2 million, 6,000 and 20,000).
6. **Sedna's farthest distance prints 937 AU, from the orbit the orrery
   fetched, not a typed 936.** It is measured from the solar system's
   center of mass, the centre its period is taken around; the 936 was the
   same number, cut off rather than rounded.
7. **The termination shock lies "about 80 to 100 AU" from the Sun, not
   "75 to 100"** (Treumann and Jaroschek). 75 AU is where Voyager 2
   entered the shock's foreshock, not an edge of the range.
8. **The wind's speed across the shock is Voyager 2's measurement: about
   320 km/s before it and about 200 after** (Li, Wang and Richardson
   2008, Table 1). It replaces "~100 to 200 km/s" and "a few hundred
   kilometers a second".
9. **Removed, because no source carries them:** the core's "a third of
   its mass" and "the hottest place in the solar system".
10. **Corrected:** both Voyagers are past the heliopause (2012 and 2018);
   the text said both were still in the heliosheath.

## The website (the Sun room)

A change to these words reaches a visitor after the nightly cache build.

**Core.** Radius line: "0.2 solar radii = 139,140 km (0.000930 AU)" ->
"0.25 solar radii = 170,000 km (0.0012 AU)".
About, first two sentences:
- Before: "The core reaches out to about a quarter of the Sun's radius
  and holds about a third of its mass. It is the hottest place in the
  solar system, near 15 million kelvin, and about 150 times denser than
  water under the weight of the layers above."
- After: "The core reaches out to the radius drawn here; beyond it the
  nuclear burning almost stops. It is about 15 million kelvin at the
  very center, where the gas is about 150 times as dense as water under
  the weight of the layers above."
Source line: the textbook-range wording goes; NASA/Marshall's solar
interior page, with what it says.

**Radiative Zone.** Radius line: "0.713 solar radii = 496,034 km" ->
"0.71 solar radii = 500,000 km (0.00332 AU)".
About:
- Before: "... between the core and the convection zone, from about a
  fifth to about seven tenths of the Sun's radius. ... so its energy can
  take millions of years to cross this layer. Temperatures fall from
  about 7 million kelvin near the core ..."
- After: "... between the core and the convection zone. ... so it takes
  about a million years to cross this layer. Temperatures fall from
  about 7 million kelvin near the core ..."
Source line: Delahaye and Pinsonneault, sec. 2.2 (the 1991 estimate,
0.713 +/- 0.003), then NASA/Marshall for the temperatures and the
million years. It said "so the base of the zone sits at 1 - 0.287 =
0.713", our own arithmetic, which a visitor should not be handed.

**Photosphere.** About: "a layer only about 500 km thick, ... at about
5,500 kelvin" -> "a layer only about 100 km thick, ... at about 5,700
kelvin" (both printed from rows). Source line gains NASA/Marshall's two
pages after the IAU.

**Chromosphere.**
- About: "from a few thousand kelvin at the bottom to about 20,000 at
  the top" -> "from about 6,000 kelvin at the bottom to about 20,000 at
  the top".
- Note: "Derived: 1 + 2000 km / 695700 km. The sourced claim is the
  2000 km thickness, not the ratio. Drawn at true physical scale since
  2026-08-16." -> "Drawn at its true depth, not thickened to be seen: at
  any scale that also shows the corona it sits on the photosphere."
- Description: unchanged on screen ("about 2,000 km deep"), now printed
  from the depth row.
- Source line: Carroll and Ostlie, a book, goes; Montana State's Yohkoh
  page ("approximately 2000 km thick") and NASA/Marshall's chromosphere
  page come in. The depth itself is unchanged.

**Alfven Surface.** About, last sentence:
- Before: "The surface is not a smooth sphere: it is lower over the
  poles and higher over the streamer belt."
- After: "Most of the time it lies between about 10 and 20 solar radii
  from the Sun's center, and it is not a smooth sphere: computer models
  of the corona often put it farthest out above the large polar coronal
  holes and closest in at the tops of the helmet streamers."
Source line gains Cranmer et al. (2023) after Kasper et al. (2021).

**Termination Shock.** About, last sentence:
- Before: "Voyager 1 crossed it at 94.01 AU and Voyager 2 at 84 AU;
  beyond it the wind moves at a few hundred kilometers a second through
  the turbulent region called the heliosheath."
- After: "Voyager 1 crossed it at 94.01 AU and Voyager 2 at 84 AU.
  Voyager 2 measured the wind slowing from about 320 to about 200
  kilometers a second as it crossed; beyond lies the turbulent region
  called the heliosheath." (Every number printed from a row.)
Source line gains NASA's Scientific Visualization Studio page for
Voyager 2's 84 AU and Li, Wang and Richardson (2008) for the speeds.

## The orrery

Where a shell has both a short hover and a long text, the change is the
same in both unless said.

**Sun and Its Atmosphere (hover and tooltip).**
- "Inner Corona (K-corona): 1-3 R_sun" -- unchanged on screen, the 3 now
  from its row.
- "Parker Solar Probe closest approach: ~8.8 R_sun (2024)" -> "Parker
  Solar Probe closest approach: 9.85 R_sun from the Sun's center,
  December 24, 2024 (NASA)".
- "Parker Solar Probe closest approach: 8.8 R_sun (0.041 AU) -- MAPS
  disintegrated at 8.33 R_sun (0.039 AU), just inside Parker's record."
  -> "Parker Solar Probe closest approach: 9.85 R_sun (0.0458 AU) -- MAPS
  disintegrated at 8.33 R_sun (0.039 AU), closer to the Sun than Parker
  has flown."

**Extended Corona.**
- Text: "Parker Solar Probe's closest approach: ~8.8 R_sun as of 2024."
  -> "Parker Solar Probe's closest approach: 9.85 R_sun from the Sun's
  center, on December 24, 2024 (NASA)."
- Hover: "Parker Solar Probe closest approach: ~8.8 R_sun (2024)" ->
  "Parker Solar Probe closest approach: 9.85 R_sun from the Sun's center
  (December 24, 2024; NASA)".
- Text: "closed loops below 2-4 R_sun" -- unchanged on screen, from its
  rows.

**Streamer Belt.**
- Text: "IT HAS NO SINGLE OUTER RADIUS, and since 2026-08-22 it is no
  longer drawn as if it did." -> "IT HAS NO SINGLE OUTER RADIUS, and it is
  not drawn as if it did." (a ruling date out of visitor text).
- Band hover: "wave motion out to 15 R_sun (10,435,500 km, 0.069757 AU)"
  -> "wave motion out to 15 R_sun (10,000,000 km, 0.07 AU)", now from a
  row cited to DeForest, Howard and McComas (2014), and printed at the
  figures 15 supports.

**Radiative Zone.** "extends from about 0.2 to 0.7 solar radii, about
0.00325 AU" -> "extends from about 0.25 to 0.71 solar radii, about
0.00332 AU".

**Photosphere.**
- "only about 500 kilometers thick" -> "only about 100 kilometers thick".
- "the radius is from 0.7 to 1 Solar radii, or about 0.00465 AU" -> "the
  radius is from 0.71 to 1 solar radius, or about 0.004650 AU".
- Unchanged tonight: "~5,500K at the Photosphere" and "527.32 nm"
  (they move together; recorded on L-411).

**Chromosphere** (its radius line, in both). "(~0.00465 - 0.00466 AU)"
-> "(0.004650 to 0.00466 AU)": each end printed by its own row, the
Sun's radius to four figures and the chromosphere's top to three.

**Termination Shock.**
- "The Solar Wind Termination Shock extends from about 75 to 100 AU."
  -> "The Solar Wind Termination Shock lies about 80 to 100 AU from the
  Sun (Treumann and Jaroschek 2008)."
- "Voyager 1 encountered the Termination Shock at 94.01 AU, while
  Voyager 2 at 84 AU." -> "Voyager 1 encountered the Termination Shock at
  94.01 AU, and Voyager 2 at 84 AU (NASA)."
- "After the Termination Shock the speeds slow down to ~100 to 200
  km/s." -> "Voyager 2 measured the wind slowing from about 320 to about
  200 km/s as it crossed (Li et al. 2008)."

**Heliopause.** "Both probes have crossed the termination shock and are
currently exploring the heliosheath, sending back valuable data about
this mysterious region." -> "Both probes crossed the termination shock
and then the heliopause, and both are now in interstellar space: Voyager
1 in 2012 (Gurnett et al. 2013), Voyager 2 in 2018 (NASA)."

**Gravitational Influence.** "including, Sedna's orbit (936 AU), the
Hills Cloud" -> "including Sedna's orbit, which reaches about 937 AU /
from the solar system's center of mass (JPL Horizons, 2026-10-13), the
Hills Cloud". The number is worked out when the orrery starts, from the
barycentric elements its period fetch saved; if that record is ever
missing, the line names Sedna's orbit and gives no number.

## How, in one line each

- New store rows, each with its open source read tonight: the core
  (0.25), the radiative zone's edge (0.713), the photosphere's thickness
  (100 km) and temperature (5,700 K), Parker's closest approach (6.16
  million km above the surface; from the center worked out), Voyager 2's
  crossing (84 AU) and its speeds (321.01 and 184.67 km/s), the
  termination shock's range (80 and 100 AU), the coronagraph floor (15).
  The chromosphere's depth keeps its value under an open citation.
- The AU forms of the solar radius, the core, the radiative zone and
  Parker's distance are computed from those rows, never stored (L-386).
- Sedna's distance is not a row: it is JPL's fetched orbit, printed by
  its error, so it follows the next fetch.
- The website's plain shells can now name a linked row in their words,
  in braces, the way the Hills cloud already does; that row's citation
  joins the Source line, and a citation already there is not printed
  twice.

## Left for later, recorded on L-411

- A number inside a feature NAME ("Chromosphere (2,000 km skin)"): a name
  cannot be filled from a row yet.
- Numbers written as words in the website's words ("one to three million
  kelvin"), which the digit search does not see.
- The non-number sentences in the website's about texts, checked against
  the citation a visitor sees.
- Earth's website words give temperatures in degrees Celsius (the inner
  core's 5,400, the mantle's ranges); the Sun's now say kelvin. One class,
  for Earth's later talks.
- The streamer band's 7.25 degrees, from the Sun's pole, which has no
  per-value rows.
- The bulk: groups T, M and C in the discovery list.
