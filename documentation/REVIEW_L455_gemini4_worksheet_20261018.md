<!-- Doc-Kind: hand | Review of Gemini 4's L-455 source worksheet for Earth: what it confirmed, what it found, where it held back, and how it did as a checker. -->
# Review of Gemini 4's worksheet, L-455 (Earth's sources)

Built on palomas_orrery 05cb185ada593eda178b79c57d2a3cbfcce97a24 at
https://github.com/tonylquintanilla/palomas_orrery and
tonyquintanilla.github.io 10508dfc2ef1afd657e6630d18b7cf00ef50eca6 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, plus this
session's unpushed working copies.

Written 2026-10-18 by Anthropic's Claude Opus 5.5. The worksheet is
`documentation/worksheets/worksheet_gemini4_high_l455_earth_20261018.md`
(Gemini 4, high effort tier). The prompt it answered is
`documentation/prompts/RELAY_L455_gemini_earth_sources_20261018.md`.

## In one sentence

Gemini 4 was a useful checker: it confirmed the agency sources, held back
honestly where it could not read a page, and its discovery searches found
the papers that replaced every National Geographic figure.

## What it confirmed (citation rows)

With a verbatim quote and a locator for each: C1 to C10 (NASA SVS inner
core, NASA crust thicknesses, WMO records, NASA troposphere height, NOAA
temperatures, Apophis), C14 (UCAR thermopause), C16 (Moon's distance),
C17 (ISS height and tilt), C19 (ESA counts) and C20 (McDowell's Starlink
count).

On C10 it settled the question the prompt raised: NASA's "Apophis Facts"
gives 32,000 km beside 20,000 miles in one place and 36,000 km beside the
same 20,000 miles in another. 20,000 miles is 32,000 km, so the 36,000 is
the page's slip.

## Where it held back, correctly

It marked as UNVERIFIED every row whose page it could not open, rather
than filling the cell from memory:

- C11, C12, C13, the three National Geographic pages (blocked).
- C15, the arXiv copy of Dmitriev and others (blocked). It found another
  open paper confirming the magnetopause was inside the geostationary
  ring, but not the paper's 3 Earth radii. The row here was read from
  arXiv earlier in the session, so it stands.
- C18, NASA's Hubble fact sheet PDF (blocked). It found "about 340
  miles" on two other NASA pages.

That is the behaviour the prompt asked for, and the most important thing
a checker can do.

## What it found (discovery rows)

- D1 and D7, the core: Andrault and others (2016), open full text, 4,100
  +/- 200 K at the core-mantle boundary and 5,580 +/- 600 K at the inner
  core's boundary; also Deschamps and Cobden (2022) and Anzellini and
  others (2013). Adopted: Andrault.
- D2, the mantle: Katsura (2022), open full text, an adiabat from 1,646 K
  at 50 km down to 1,994 K above the 660 km boundary and 1,960 K below it.
  Adopted.
- D3, the atmosphere: UCAR, "over 99 percent" in the troposphere and
  stratosphere together, which restores the old words' figure with a
  source. Adopted.
- D5, Starlink's height: the FCC's authorised shells (540, 550, 560 and
  570 km) and a NASA Orbital Debris Quarterly News issue. Adopted: the
  NASA issue's "most near 550 km".
- D6, low orbit's own count: ESA's table of orbit regimes, 28,015 objects
  tracked in low Earth orbit on 14 October 2026. Adopted; it replaces the
  old typed 35,000, which ESA does not support.
- D4, the sky crossing: an ESA page saying "several minutes" and NASA
  pages giving five and three minutes for particular passes. Not adopted:
  there is no single figure.

Every adopted figure was re-opened here before it went into a row; each
row's Read line names both readers.

## How it did, against the rules

- Header, model and effort tier: given. Rule files: "not imported", said
  plainly. The pre-flight quote was given.
- Verdict tokens: one per cell, from the right column, throughout.
- Search logs: given for every discovery row, with the queries run.
- One weakness: some cells run very long, mixing several sources in one
  "Your value" cell, which makes the table hard to scan. Asking for one
  source per row next time would help.
- One thing to watch: it marked C10 YES on the value even though the page
  prints two different kilometre figures. Its note explained the
  difference correctly, so nothing was lost, but a PARTIAL would have
  described the page better.

## For Mode 7 (the multi-AI relay)

This was the first job for Gemini 4 under the open-source and read-it
rules, and it is a good result. It is most valuable on discovery rows,
where a long search matters: four of its finds changed what a visitor
will read, and two of them (the mantle and the core) correct figures by
hundreds of kelvin. On citation rows it confirmed what was already
confirmed here, which is useful as a second reader but not new.
