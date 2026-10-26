built on 5398439 at https://github.com/tonylquintanilla/palomas_orrery (branch main)

# L-491: the comet nucleus sizes, looked for at their sources

Tony Quintanilla, PE, with Anthropic's Claude Opus 5.5 | October 26, 2026

## What this is

The orrery's comet hover prints the size of each comet's nucleus, the
solid body at the centre of the comet. Until today those sizes came from
a table typed from memory in `comet_visualization_shells.py`,
`COMET_NUCLEUS_SIZES`: fifteen comets plus a default, with no source for
any of them. Tony's ruling, October 26: "bring the sourcing into the
ledger and into this slice."

Each size was looked for in JPL's Small-Body Database and in papers that
can be opened free of charge. The search was done by a helper session of
this build, which quoted every figure it read; two of its reads were
repeated in this session and agreed (JPL's page for 88P/Howell, and
Table 1A of Knight et al. 2023).

## The result, in one paragraph

Nine sizes were found in a source that can be opened, and they are now
rows in `constants_new.py`, section COMET NUCLEUS SIZES, each with its
source, what was read and how. Six had no size anywhere that could be
opened, and came out of the hover: NEOWISE, ISON, West, Lemmon,
Wierzchos and PANSTARRS. Their hovers now print no size, which is the
honest blank. Four of the old typed values were wrong against every
source found: Halley, Tempel 2, Howell and 3I/ATLAS.

## The nine kept

| Comet | Kept | Old typed value | Source |
|---|---|---|---|
| 1P/Halley | radius 5.5 km | 15x8x8 km | Knight et al. 2023, Table 1A |
| C/1995 O1 Hale-Bopp | radius 37 km | 60 | Szabo et al. 2012 |
| C/1965 S1 Ikeya-Seki | radius 4.3 km, an estimate from its brightness before perihelion | 5 | Knight et al. 2010, Table 1 |
| C/1996 B2 Hyakutake | radius 2.4 km | 4 | Knight et al. 2023, Table 1A |
| 3I/ATLAS (C/2025 N1) | radius 1.3 km, measured by Hubble after perihelion, assuming a dark surface | 8 | Hui et al. 2026 |
| C/2026 A1 MAPS | diameter 0.4 km, estimated from James Webb Space Telescope images | 0.4 ("JWST, March 2026") | Sekanina and Krolikowska 2026, quoting Zhang et al. 2026 |
| 24P/Schaumasse | diameter 2.6 km | 3 ("~2.6 km") | JPL Small-Body Database |
| 88P/Howell | diameter 4.4 km | 3 | JPL Small-Body Database |
| 10P/Tempel 2 | radius 5.98 km | 16x9 km | Knight et al. 2023, Table 1A |

Each is kept in the form its source gives it, a radius or a diameter,
and the hover says which. The old table called every value a diameter.

## The six removed, and why

- **NEOWISE (C/2020 F3).** JPL holds no size. The one table that gives
  one (Knight et al. 2023, a 2.5 km radius) cites unpublished data. An
  IPAC news page quotes "about 5 kilometers across" and names no work.
- **ISON (C/2012 S1).** Every figure published is an upper limit or a
  model value, from a 0.3 km radius to a 4 km diameter. The comet broke
  up at perihelion.
- **West (C/1975 V1).** JPL holds no size. No paper with a figure was
  found. Wikipedia gives a radius with no citation.
- **Lemmon (C/2025 A6).** No size anywhere.
- **Wierzchos (C/2024 E1).** The only published figure is an upper
  limit, a 13.7 km radius (Snodgrass et al., JWST). The old note,
  "2-10 km (JWST estimates)", traces to a paper whose 2 and 10 km are
  generic model sizes, not this comet's.
- **PANSTARRS (C/2025 R3).** JPL holds no size. NASA's picture of the
  day says "likely a few kilometers across" and names no work.

## Where the sources disagree

These are written into each row's Also line in `constants_new.py`; the
short form is here so the disagreement is visible without opening the
file.

- **Halley.** JPL gives an effective diameter of 11.0 km, which is the
  same 5.5 km radius kept. JPL also gives axes of 14.9 x 8.2 km after
  Keller et al. 1987, not opened. NASA's NSSDC page says 16 x 8 x 8 km
  and names no work. The old 15x8x8 matches none of these.
- **Hale-Bopp.** JPL gives a 60 +/- 20 km effective diameter after
  Fernandez 2002, not opened: a 30 km radius. Szabo et al. 2012 give
  37 +/- 3 km, which that 30 does not reach. Older work gives upper
  limits of 30 and 48 km. The 37 km radius is kept because it is the
  figure that could be read in full.
- **Hyakutake.** JPL's 4.2 km diameter is marked by JPL itself "value
  unverified".
- **3I/ATLAS.** Before perihelion only upper limits were published.
  Cloete, Loeb and Veres 2025 give a lower limit on the diameter of
  5 km, from a model, which the Hubble measurement does not meet.
- **MAPS.** The size's own paper (Zhang et al. 2026, Research Notes of
  the AAS) could not be opened; the figure is read where another paper
  quotes it. The old note said the imaging was in March; it was
  February 6-7.
- **Schaumasse and Howell.** JPL's figures are after Scotti 1994, a
  conference abstract that could not be opened. Wikipedia quotes
  smaller figures after Tancredi et al. 2006, which is paywalled.
- **Tempel 2.** Lamy et al. 2004 give semi-axes of 8 to 8.15 km and 4
  to 4.3 km, about 16 x 8.6 km in full. JPL gives a 10.6 km effective
  diameter after the same chapter. The old 16x9 is close to the full
  axes but matches no source as written.

## What could not be opened

Three hosts refused the fetch: NASA ADS, the PDS Small Bodies node and
the IOP journals. Every "not opened" above is one of those, unless it
says otherwise.

## What is left

The ten gallery cards that carry a comet hover were exported with the
old sizes. They change only when re-exported through Gallery Studio,
which is Tony's step; the ledger item L-491 carries it.
