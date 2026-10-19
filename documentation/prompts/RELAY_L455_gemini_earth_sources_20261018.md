<!-- Doc-Kind: hand | Relay prompt for Gemini 4: check the sources behind Earth's new rows (L-455) and search for the ones still missing. Copy everything below the line into Gemini. -->
# Relay prompt for Gemini 4 -- Earth's sources (L-455)

Written 2026-10-18 by Anthropic's Claude Opus 5.5 for Tony to carry to
Gemini 4. Copy everything below the line. Ask for the highest effort
tier Gemini offers: half the rows are DISCOVERY rows, which are only as
good as how long the checker keeps looking.

---

Built on palomas_orrery 05cb185ada593eda178b79c57d2a3cbfcce97a24 at
https://github.com/tonylquintanilla/palomas_orrery and
tonyquintanilla.github.io 10508dfc2ef1afd657e6630d18b7cf00ef50eca6 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, plus
this session's unpushed working copies. The rows below are NOT in
either repository yet, so every value you need is written out here.
Vocabulary: v2 (2026-08-13)

## Who you are working for

Tony Quintanilla, PE, a retired civil and environmental engineer, builds
Paloma's Orrery, a 3D astronomy visualization (a desktop program and the
website palomasorrery.com), through conversation with AI partners. He is
not a professional programmer or astronomer. Every number a visitor
reads must come from a source anyone can open. Please write plainly.

## The rules this job follows

If you have imported the palomas_orrery repository, read these two
files and name them at the top of your answer:

- skills/provenance-discipline/SKILL.md -- sections The Access Standard,
  The Unit Field and What a Visitor Reads
- skills/provenance-cross-check/references/worksheets.md -- section
  Worksheet Types

If you have not imported it, say so; the rules you need are restated
here:

1. **Open sources only.** A source counts only if its text can be read
   without a paywall: open full text, a free abstract that states the
   claim, an agency page or document. A source behind a paywall does not
   count, whatever its authority.
2. **Name what you opened.** Give the title and authors as printed in
   the document you actually opened, not a paper it cites.
3. **Quote it.** Every row needs a short verbatim quote from the source
   containing the figure, and a locator (section, table, page, or the
   exact URL). A row without both is recorded as UNVERIFIED whatever its
   verdict says. If you are recalling rather than reading, say so and
   leave the row UNVERIFIED. Silence is better than a guess.
4. **Temperatures are stored in kelvin.** If a source gives degrees
   Celsius, report the figure exactly as the source prints it; the
   conversion is ours.
5. **Prefer an agency or a peer-reviewed paper** (NASA, NOAA, USGS, ESA,
   WMO, NIST, IERS, an open journal article or arXiv preprint) over an
   educational or news page. Say which kind each source is.

## Before any row: a pre-flight

Open this page and quote one sentence from it, so we know your fetching
works:

```
https://www.noaa.gov/jetstream/atmosphere/layers-of-atmosphere
```

## Your answer's header

Start with one line naming your MODEL and your EFFORT TIER, then the
list of rule files you read (or "not imported").

## The two kinds of row

[CITATION] -- the row names a source. Open it and confirm it states the
figure, at the figure's precision. Then, separately, check the value
against one other open source of your own choosing, preferably an
agency or a paper.

[DISCOVERY] -- the figure may have no source at all. Do not assume one
exists, and do not reconcile it with any other row. Find whether an open
source states it. UNSOURCED is a valid and useful answer, but a negative
must show its search: list the queries you actually ran and the places
you looked, in a SEARCH LOG under the table. A negative with no search
log is recorded as UNVERIFIED.

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
  found states the figure.

- Put every URL as a bare address inside a code block, after the table,
  numbered by row. Links pasted as chips lose their address.
- Please deliver the whole answer as a downloadable Markdown file named
  worksheet_gemini4_<effort tier>_L455_earth_20261018.md, as well as
  in the chat.

## The rows

### Citation rows (a source is named)

C1. Earth's inner core reaches up to 5,600 K. Source named: NASA
Scientific Visualization Studio 14374, "A Guide to Cosmic Temperatures"
(2023), https://svs.gsfc.nasa.gov/14374/

C2. Oceanic crust is about 5 km thick. Source named: NASA Science,
"Facts About Earth", https://science.nasa.gov/earth/facts/

C3. Continental crust is about 30 km deep on average on land. Source
named: NASA Science, "Facts About Earth" (as C2).

C4. The lowest temperature recorded at Earth's surface is -89.2 degrees
Celsius, Vostok, Antarctica, 21 July 1983. Source named: World
Meteorological Organization, "Records of Weather and Climate Extremes"
(table as of 31 July 2025),
https://wmo.int/sites/default/files/2025-07/Table_Records_25Jul2025.pdf

C5. The highest is 56.7 degrees Celsius, Furnace Creek (Greenland
Ranch), California, 10 July 1913. Source named: as C4.

C6. The troposphere reaches on average about 12 km. Source named: NASA
Science, "Earth's Atmosphere: A Multi-layered Cake",
https://science.nasa.gov/earth/earth-atmosphere/earths-atmosphere-a-multi-layered-cake/

C7. The average temperature at the bottom of the troposphere is about
17 degrees Celsius. Source named: NOAA JetStream, "Layers of the
Atmosphere" (the pre-flight page).

C8. The temperature at the tropopause is about -51 degrees Celsius.
Source named: as C7.

C9. Temperatures near the top of the thermosphere can reach about 2,000
degrees Celsius. Source named: as C7.

C10. On April 13, 2029 the asteroid Apophis passes about 32,000 km from
Earth's surface. Source named: NASA Science, "Apophis Facts",
https://science.nasa.gov/solar-system/asteroids/apophis-facts -- please
note that the page's own sentence in "What Will Happen in 2029" gives
36,000 km beside the same 20,000 miles; say which figure the page
supports.

C11. The outer core is between 4,500 and 5,500 degrees Celsius. Source
named: National Geographic Society, "Core",
https://education.nationalgeographic.org/resource/core/

C12. The mantle runs from about 1000 degrees Celsius near the crust to
about 3700 near the core. Source named: National Geographic Society,
"Mantle", https://education.nationalgeographic.org/resource/mantle/

C13. The bottom 30 km of the atmosphere holds about 98 percent of its
mass. Source named: National Geographic Society, "Parts of the
Atmosphere",
https://education.nationalgeographic.org/resource/parts-atmosphere/

C14. The thermopause, the top of the thermosphere, lies between about
500 and 1,000 km, varying with the Sun's activity. Source named: UCAR
Center for Science Education, "Layers of Earth's Atmosphere",
https://scied.ucar.edu/learning-zone/atmosphere/layers-earths-atmosphere

C15. In the 21 January 2005 storm the subsolar magnetopause was pushed
inside geosynchronous orbit, at its closest about 3 Earth radii from
Earth's centre. Source named: Dmitriev et al. (2014), "Anomalous
dynamics of the extremely compressed magnetosphere during 21 January
2005 magnetic storm", J. Geophys. Res. Space Physics 119,
doi:10.1002/2013JA019534, open at https://arxiv.org/abs/1402.0927

C16. The Moon's semimajor axis is 384,400 km. Source named: NASA NSSDCA
Moon Fact Sheet,
https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html

C17. The International Space Station orbits at 370 to 460 km, inclined
51.6 degrees. Source named: ESA, "ISS: International Space Station",
https://www.esa.int/Our_Activities/Human_Spaceflight/International_Space_Station/ISS_International_Space_Station

C18. Hubble is about 340 miles above Earth's surface. Source named:
NASA, "Hubble Space Telescope -- An Overview" (fact sheet),
https://science.nasa.gov/wp-content/uploads/2023/04/hst_overview_fact_sheet.pdf

C19. About 15,900 satellites are still functioning in Earth orbit, and
about 47,140 space objects are regularly tracked and catalogued (as of
14 October 2026). Source named: ESA Space Debris Office, Space
Environment Statistics, https://sdup.esoc.esa.int/discosweb/statistics/
-- give the figures and the "last updated" date the page shows when you
open it.

C20. 11,140 Starlink satellites were working in orbit on 15 October
2026. Source named: Jonathan McDowell, Jonathan's Space Report,
https://planet4589.org/space/con/star/stats.html -- give the figure and
date the page shows when you open it, and say what kind of source this
is.

### Discovery rows (no source yet, or a better one wanted)

D1. The outer core's temperature range, from an agency or a
peer-reviewed open paper. C11's figures come from an educational page;
the project's old text said 4,500 to 5,400 degrees Celsius. Report every
figure you find with its source; do not average them.

D2. The upper mantle's and the lower mantle's temperatures, separately,
from an agency or open paper. The old text said about 500 to 2,200
degrees Celsius for the upper mantle and 2,200 to 4,500 for the lower.

D3. The share of the atmosphere's mass held by the troposphere and the
stratosphere together. The old text said 99 percent. Also report any
open agency figure for the troposphere alone.

D4. How long a satellite in low Earth orbit, such as the International
Space Station, is visible crossing the sky. The old text said about
6 minutes.

D5. The altitude of Starlink's main orbital shells, from SpaceX, a
regulator's filing (for example the FCC), or an agency. The old text
said about 550 km.

D6. The number of active satellites in low Earth orbit specifically,
and the number of tracked objects in low Earth orbit, from an agency.
The old text said about 11,000 active and more than 35,000 tracked
objects. C19's figures are for all orbits.

D7. The temperature at Earth's center, or at the inner core boundary.
Four open figures are already known to us and differ: up to 5,600 K
(NASA SVS), as high as 5,400 degrees Celsius (NASA "Facts About Earth"),
about 6,000 +/- 500 degrees Celsius at the inner core boundary (ESRF,
2013, reporting Anzellini et al., Science), and about 5,200 degrees
Celsius (National Geographic). Find the most authoritative open
statement and say which kind of source it is; if you find a recent
review or agency page, report its figure and uncertainty.

## What not to do

- Do not propose wording for the website.
- Do not combine rows, or reconcile one row's figure with another's.
- Do not fill a cell from memory. If you could not open a source, the
  cell is UNVERIFIED and Notes says what stopped you.
