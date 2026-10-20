<!-- Doc-Kind: hand | Relay prompt for Gemini 4: an outside check of the Sun's numbers rows (L-412) and a search for the sentences the website still holds without a source (L-411). Copy everything below the line into Gemini. -->
# Relay prompt for Gemini 4 -- the Sun's numbers (L-411, L-412)

Written 2026-10-19 by Anthropic's Claude Opus 5.5 for Tony to carry to
Gemini 4. Copy everything below the line. Choose Gemini 4 Argon in the
model menu and, under Thinking level, the highest setting offered: the
discovery rows are only as good as how long the checker keeps looking.
Ask it to name the model and setting your screen shows.

---

Built on palomas_orrery 59e1b656c56ac38660f7943cae066513e9ab7b77 at
https://github.com/tonylquintanilla/palomas_orrery and
tonyquintanilla.github.io 4fc320fa6d2e0e10d9a50b8b69006cbff96a1364 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. The
citation rows below ARE in the orrery's constants_new.py at that
commit, and are served on the website's Sun room; every value you need
is written out here anyway.
Vocabulary: v2 (2026-08-13)

## Who you are working for

Tony Quintanilla, PE, a retired civil and environmental engineer, builds
Paloma's Orrery, a 3D astronomy visualization (a desktop program and the
website palomasorrery.com), through conversation with AI partners. He is
not a professional programmer or astronomer. Every number a visitor
reads must come from a source anyone can open. Please write plainly.

## What this job is

The website's Sun room prints numbers about the Sun's layers. Fourteen
of them were sourced on 2026-10-17 and 18, each read by one model
(Claude) from the open source named below. No second reader has
re-opened them: that is the citation half. Separately, five sentences
the room still shows carry a typed number with no source the project
has stored for it: that is the discovery half.

## The rules this job follows

If you have imported the palomas_orrery repository, read these two
files and name them at the top of your answer:

- skills/provenance-discipline/SKILL.md -- sections The Access Standard
  and What a Visitor Reads
- skills/provenance-cross-check/references/worksheets.md -- section
  Worksheet Types

If you have not imported it, say so; the rules you need are restated
here:

1. **Open sources only.** A source counts only if its text can be read
   without a paywall: open full text, a free abstract that states the
   claim, an agency page or document, an arXiv preprint. A source
   behind a paywall does not count, whatever its authority.
2. **Name what you opened.** Give the title and authors as printed in
   the document you actually opened, not a paper it cites.
3. **Quote it.** Every row needs a short verbatim quote from the source
   containing the figure or statement, and a locator (section,
   equation, table, page, or the exact URL). A row without both is
   recorded as UNVERIFIED whatever its verdict says. If you are
   recalling rather than reading, say so and leave the row UNVERIFIED.
   Silence is better than a guess.
4. **Temperatures are stored in kelvin.** If a source gives degrees
   Celsius, report the figure exactly as the source prints it; the
   conversion is ours.
5. **Prefer an agency or a peer-reviewed paper** (NASA, ESA, an open
   journal article or arXiv preprint) over an educational or news page.
   Say which kind each source is.

## Before any row: a pre-flight

Open this page and quote one sentence from it, so we know your fetching
works:

```
https://arxiv.org/abs/2202.11533
```

## Your answer's header

Start with one line naming your MODEL and your EFFORT TIER, then the
list of rule files you read (or "not imported").

## The two kinds of row

[CITATION] -- the row names a source. Open it and confirm it states the
figure or statement, at the figure's precision. Then, separately, check
the value against one other open source of your own choosing,
preferably an agency or a paper.

[DISCOVERY] -- the claim may have no source at all. Do not assume one
exists, and do not reconcile it with any other row. Find whether an
open source states it. UNSOURCED is a valid and useful answer, but a
negative must show its search: list the queries you actually ran and
the places you looked, in a SEARCH LOG under the table. A negative with
no search log is recorded as UNVERIFIED.

## The table

One row per numbered item below, in this exact layout:

| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Read by | Quote | Locator | Notes |

- **Read by**: who opened the source -- your model name.
- **Access word**: one of open full text, abstract, agency page, open
  document, educational page, news page.
- Each verdict cell holds EXACTLY ONE token, and the tokens belong to
  their column:

```
Value correct?     YES  NO  APPROX  UNVERIFIED
Citation correct?  YES  NO  PARTIAL  DERIVED  UNSOURCED  UNVERIFIED
```

  APPROX qualifies a value (right to a stated tolerance; say the
  tolerance in Notes). PARTIAL qualifies a citation (the source supports
  part of the claim). UNSOURCED means the named source does not publish
  the figure at all; NO means it publishes a different one. For a
  DISCOVERY row, "Citation correct?" answers whether the source you
  found states the claim.

- Put every URL as a bare address inside a code block, after the table,
  numbered by row. Links pasted as chips lose their address.
- Please deliver the whole answer as a downloadable Markdown file named
  worksheet_gemini4_<effort tier>_L411_sun_numbers_20261019.md, as well
  as in the chat.

## The rows

### Citation rows (a source is named)

C1. The Sun's core, where energy is generated, reaches out to about 25
percent of the distance from the centre to the surface (0.25 solar
radii). Source named: D. H. Hathaway, NASA/Marshall Solar Physics, "The
Solar Interior". https://solarscience.msfc.nasa.gov/interior.shtml

C2. The radiative zone's outer edge (the base of the convection zone)
is at 0.713 +/- 0.003 solar radii. Source named: Delahaye and
Pinsonneault, "The Solar Heavy Element Abundances: I. Constraints from
Stellar Interiors", arXiv:astro-ph/0511779, sec. 2.2, which quotes the
1991 estimate (Christensen-Dalsgaard, Gough and Thompson, ApJ 378:413)
beside Basu and Antia's 0.7133 +/- 0.0005.
https://arxiv.org/abs/astro-ph/0511779

C3. The photosphere is a layer about 100 km thick. Source named:
Hathaway, NASA/Marshall, "The Photosphere".
https://solarscience.msfc.nasa.gov/surface.shtml

C4. At the visible surface the temperature has dropped to 5,700 K.
Source named: Hathaway, NASA/Marshall, "The Solar Interior" (as C1).

C5. The chromosphere is a layer of gas approximately 2,000 km thick.
Source named: Yohkoh Public Outreach Project, Montana State University,
"A 'Dancing' Layer of the Sun".
https://solar.physics.montana.edu/YPOP/Spotlight/SunInfo/Chromosph.html
Please also report what NASA's 2017 eclipse page gives (we read about
5,000 km there): https://science.gsfc.nasa.gov/attic/eclipse2017.gsfc.nasa.gov/chromosphere.html

C6. The Alfven surface spends most of its time between about 10 and 20
solar radii from the Sun's centre. Source named: Cranmer et al.
(2023), "The Sun's Alfven Surface: Recent Insights and Prospects for
the Polarimeter to Unify the Corona and Heliosphere (PUNCH)", arXiv
2310.05887, abstract. https://arxiv.org/abs/2310.05887

C7. Voyager 1 crossed the termination shock on 16 December 2004 at
94.01 AU. Source named: Stone et al. (2005), "Voyager 1 explores the
termination shock region and the heliosheath beyond", Science 309,
2017, abstract at NASA ADS.
https://ui.adsabs.harvard.edu/abs/2005Sci...309.2017S/abstract

C8. Voyager 2 reached the termination shock in August 2007 at about
83.6 AU. Source named: Li, Wang and Richardson (2008), "Properties of
the termination shock observed by Voyager 2", GRL 35:L19107, abstract.
https://www.spaceweather.ac.cn/~hli/papers/Li%20et%20al%202008%20GRL%20Properties%20of%20the%20termination%20shock%20observed%20by%20Voyager%202.pdf

C9. At Voyager 2's first crossing the solar wind's radial speed
averaged 321.01 +/- 2.84 km/s upstream and 184.67 +/- 23.38 km/s
downstream. Source named: as C8, Table 1, shock 1.

C10. The termination shock lies between 80 and 100 AU from the Sun.
Source named: Treumann and Jaroschek, "The Heliospheric Termination
Shock", arXiv 0807.4170, secs. V.A and V.D.2.
https://arxiv.org/abs/0807.4170

C11. Parker Solar Probe's closest approach is 6.16 million km above the
Sun's surface (3.83 million miles), reached on 24 December 2024.
Sources named: Johns Hopkins APL, Parker Solar Probe, "The Mission",
https://parkersolarprobe.jhuapl.edu/The-Mission/index.php ; and NASA
Scientific Visualization Studio 14741, https://svs.gsfc.nasa.gov/14741/
Please say whether each source gives the distance above the surface or
from the Sun's centre.

### Discovery rows (sentences the website shows with no stored source)

For each, find an open source, preferably an agency page or a
peer-reviewed paper, that states the figure; quote it; and give the
figure in kelvin if the source does (if it gives degrees Celsius,
report it exactly as printed). Report every figure you find; do not
average them.

D1. The core: "about 15 million kelvin at the very center, where the
gas is about 150 times as dense as water". (Hathaway's interior page,
C1, is known to say about 15,000,000 degrees C and about 150 g/cm3 at
the centre; find a second open source, ideally a standard solar model
paper that tabulates the central temperature and density.)

D2. The radiative zone: temperatures "fall from about 7 million kelvin
near the core to about 2 million at the top of the zone". (Hathaway's
interior page is known to say 7,000,000 to about 2,000,000 degrees C;
find a second open source, ideally a model or a helioseismology paper.)

D3. The chromosphere: its temperature "rises with height, from about
6,000 kelvin at the bottom to about 20,000 at the top". (Hathaway's
chromosphere page, https://solarscience.msfc.nasa.gov/chromos.shtml ,
is known to say 6000 degrees C to about 20,000 degrees C; note that
6,000 degrees C is about 6,270 K, so please look for a source that
states the bottom temperature in kelvin, for example the temperature
minimum at the top of the photosphere.)

D4. "NASA's Parker Solar Probe crossed this boundary [the Alfven
surface] in April 2021, the first spacecraft to fly inside the corona."
Find NASA's announcement or the paper reporting the crossing, with its
date and the distance at which it happened.

D5. "A 2025 computer model finds instead a slightly warped disk tilted
about 30 degrees to the ecliptic, nearly at right angles to the plane
of the Milky Way" (the Hills cloud, the inner Oort cloud). The project
cites Nesvorny et al., arXiv 2502.11252. Confirm the year it was posted
or published, and the tilt it states.
https://arxiv.org/abs/2502.11252

## What not to do

- Do not propose wording for the website.
- Do not combine rows, or reconcile one row's figure with another's.
- Do not fill a cell from memory. If you could not open a source, the
  cell is UNVERIFIED and Notes says what stopped you.
