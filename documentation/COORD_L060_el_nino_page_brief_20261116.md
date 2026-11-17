<!-- Doc-Kind: hand | The brief for one Claude Code session through the python_work door: L-060 (El Nino), a page of its own on the website, a walk in five steps from NOAA's data. Communication; written once, read by its session. -->
# Brief: El Nino's page, a walk in five steps (L-060)

Built on orrery 20a9c1559ee36426b69beb731ab61b51e43f87f3 at
https://github.com/tonylquintanilla/palomas_orrery
and gallery 1c5fe516cebaa7b239d34c7573f66a0f6099cc90 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-16, 22:40 Chicago). Nightly bot commits
since are expected. This brief, and its companion file below, are in
documentation/ on Tony's computer, not yet pushed.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session on Tony's computer, through the
python_work door: a generator in the orrery, the page in the gallery.
Written November 16, 2026 with Anthropic's Claude Opus 5.5, the
coordinating session of that day. It interrupts ESCAPADE's path (L-533),
which comes next.

## What this is, in one paragraph

The 2026-27 El Nino is near its peak and in the news. It gets its own
page on the website, like Sudan's: a short scroll of five steps, each a
picture above a few sentences, upright phone first. The page's one
source of record is NOAA's Climate Prediction Center (CPC). Its words
were drafted in a design talk, reviewed by two outside models (Gemini,
then GPT), and every sentence was checked against a source re-opened on
Nov 16. The words are in the appendix below; the build changes none of
them without Tony's word, except figures it computes from NOAA's data.

## Read first

- The ledger, L-060: its three notes of 2026-11-16 (morning, afternoon,
  evening). They are the rulings, in Tony's words and times.
- documentation/REVIEW_L060_gemini_worksheet_20261116.md and
  documentation/REVIEW_L060_gpt_worksheet_20261116.md: what each
  sentence rests on, and what the build must do (below, under The data).
- documentation/ENSO_chart_spec.md (v2, June). Still holds: RONI as the
  lead series; phases and strength computed from RONI (its D4), never a
  recalled label; the 2026-27 event marked provisional; a drawing with
  no time axis for the mechanism. No longer holds: the old gallery card
  and Plotly teaser (sections 3 and 6), the IRI model plume (D6), and
  the ONI thin line (not drawn: Tony's ruling of Nov 16, 16:56).
- documentation/MOCKUP_L060_el_nino_drawings_20261116.py, REFERENCE
  ONLY: the drawing code behind the mockup, for the maps' shapes,
  colours and labels and the charts' layout. Its long RONI chart is a
  made-up sketch.
- The mockup itself is a claude.ai artifact ("El Nino page mockup",
  https://claude.ai/artifact/8dr1qD8XGuKSiEJLR4eFv3), private to Tony;
  this session may not be able to open it. The appendix carries
  everything in it that the build needs.

## The design

THE FORM. A new page, `earth/el_nino.html` (the name is this brief's
choice; Tony may rename it), written by a new generator in the orrery,
`enso_page_generator.py`, a dedicated module like
food_insecurity_generator.py (it imports no scalar engine). It writes
the page and every picture at each build into the orrery's data/earth/,
copied to the gallery's earth/, in the site's look as Sudan's page has
it (dark ground, white figure panels, gold step headings). Pictures are
`earth/el_nino_<step>.png`, each with alt text saying what it shows.

THE STATUS LINE, above the steps: the ENSO Alert System status, "NOAA's
latest update: <date>", linked to the discussion, and "Next expected:
<date>", all read from NOAA's discussion at build time.

THE FIVE STEPS (words in the appendix):
1. What El Nino is. Picture: three simplified maps of the tropical
   Pacific, one above the other: El Nino, neutral, La Nina, each with
   the Nino 3.4 box marked and the trade winds as an arrow (weak,
   normal, stronger). Red is warm water, blue cool; the picture says it
   is simplified. Follow the reference file's shapes.
2. Since 1950, in one line. Picture: NOAA's RONI from 1950 to the
   newest season, a filled seesaw, red above zero and blue below, the
   +0.5 and -0.5 thresholds dashed, the axis labelled "RONI, degrees C",
   and the three strongest El Nino events labelled, COMPUTED from the
   data. Then the boxed note "For the technical reader".
3. This year so far. Picture: the last twelve seasons of RONI as bars,
   the record as a dashed line, COMPUTED from the data.
4. What NOAA expects. Picture: NOAA's chance of El Nino, one bar per
   overlapping three-month season, as NOAA's table gives them, labelled
   with the percentages.
5. Why the whole planet feels it. Picture: a drawing with no time axis:
   the ocean taking heat in (La Nina) and giving it back (El Nino).

Each step ends with a "Sources:" line of live links (appendix). Below
the steps: a button to NOAA's own discussion, then the footer (sources,
the safeguards' line, the credit line).

THE SPELLING. "El Nino", "La Nina" and "Nino 3.4" carry the tilde on
the page, in the pictures, in the alt text and in the title (Tony, Nov
16, 22:20). The code stays ASCII: write `&ntilde;` in HTML and the
escape `\u00f1` in Python strings for the pictures.

## The data

- ONE SOURCE OF RECORD: NOAA CPC. No other agency's figures anywhere on
  the page. Japan's agency and the WMO appear only in step 3's sources
  line, for one sentence (Tony, Nov 16, 19:00, three conditions in
  L-060).
- RONI: `https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt`,
  NOAA's own named file for the index (NWS statement 26-05). READ IT
  FRESH at every build, never through a cache: on Nov 16 a cached copy
  ended at JAS 2026 while the file held ASO 2026 at +1.97.
- Chances: NOAA's table at
  `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/probabilities/`
  (issued November 2026: El Nino 100, 100, 100, 100, 98, 80, 38 percent
  for OND through AMJ; check against the page when built).
- Status, dates and the "historic event" figure: NOAA's current
  discussion,
  `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml`.
  The ~60 percent is stated with NOAA's own threshold (+2.5 or more on
  RONI) and the discussion's date, never as the chance of passing the
  record (+2.40). If the sentence cannot be found in a new discussion,
  the build stops and names it; it does not guess.
- Figures the page states are computed from the file at build time:
  the newest season and its value, the record and its season, whether
  it has been passed, the three strongest events. A sentence whose
  figure changes is rebuilt from the data; one the data contradicts
  stops the build (earth-system-pipeline, A Layer's Page and Its Walk).

THE TWO SAFEGUARDS (L-060, Nov 16 morning; Tony's funding question):
1. The page always shows the date of NOAA's latest update. When the
   next discussion's date has passed and the build cannot find a newer
   one, the page says so in one plain line.
2. Every build saves a dated copy of the NOAA files it read (the RONI
   file, the probabilities page, the discussion) in the orrery, under
   data/earth/, so the record survives if a feed ends.

THE MONTHLY PROMISE. Step 4 says it is redrawn after each NOAA update
(the second Thursday of each month). Say in the report how that will be
kept: Tony running the generator, or a line in the Daily Run. Tony
decides; until then the sentence stays only if the way is in place.

## Start

1. Record both bases; say whether either moved past the anchor.
2. Load earth-system-pipeline 1.3, provenance-discipline 2.36,
   safe-file-editing 1.14, agentic-pre-test 1.3, gallery-pipeline 1.2,
   and, at the close, ledger-and-session-records 1.23. Compare each
   version line with the manifest. Stale = stop.
3. Find how a visitor reaches Sudan's page today, and say whether El
   Nino's page can be reached the same way. Do not build a lobby card or
   room (L-531 is the Earth Science room's).

## The job, with a stop and a report after each part

PART 1, THE DATA. The generator's fetch: the three NOAA sources, read
fresh, saved as dated copies, parsed. Report what it read, by name: the
newest RONI season and value, the record and its season, the three
strongest events it computed, the chances table, the status, the two
dates and the ~60 percent sentence as printed. Stop.

PART 2, THE PAGE. The five pictures and the page, as designed, with the
appendix's words and links. Report EVERY sentence in full, each with
its source, marking which figures were computed; put a phone-size
preview where Tony's phone can open it; check 360 and 375 px widths, no
sideways scroll. Tony reads every word before anything goes live, and
his phone look is the gate. Stop.

PART 3, THE CLOSE. L-060: what was built, the monthly promise as Tony
rules it, anything the build found. Where We Are at its anchors (it
stands at its 130-line cap: make room by moving an old Settled line,
not by adding). No skill change unless the build finds a rule the skill
lacks; if so, propose it for Tony's go-ahead.

## Out of scope

The Amazon's fires (recorded on L-060, a later step if at all); the
Phase 2 pass on energy_imbalance.py (its form waits on L-531); the old
index (ONI) on the chart; any map layer for Google Earth; a lobby card
or room.

## Checks

py_compile and the pre-test on a throwaway copy; the provenance scanner,
Tier-1 = 0 on the active build path, with a `# Source:` at each of the
generator's constants and URLs; the gallery run's checks; every picture
with alt text; every link opening; the page at 360 and 375 px with no
sideways scroll. Tony's reading of the words, and his phone look, are
the gate. Commit and push are Tony's. The work lands on his disk as it
goes.

## Appendix: the page's words, step by step

Typographic quotes and dashes are written here in ASCII; use the
proper characters on the page (as entities). "[computed]" marks a
figure the build computes from NOAA's data at each build; the value
shown is Nov 16's.

Title: El Nino, 2026-27. Subtitle: NOAA's record of El Nino and La Nina
since 1950, and what NOAA expects next, in five steps. Hint: Scroll
down, one step at a time.

### Step 1: What El Nino is

- In a neutral year, the trade winds blow west along the equator, taking
  warm water toward Asia. The sea off Asia is about 8 C warmer than in
  the eastern Pacific, where cold water rises from deeper levels off
  South America.
- In an El Nino the trade winds weaken, and the warm water is pushed
  back east, toward the Americas.
- In a La Nina the trade winds are even stronger than usual, pushing
  more warm water toward Asia, and more cold water rises off the
  Americas.
- Think of the warm water sloshing from one side of the ocean to the
  other. The black box on the maps is the stretch of ocean NOAA watches,
  explained in the next step.
- Sources: NOAA Ocean Service, What are El Nino and La Nina?
  `https://oceanservice.noaa.gov/facts/ninonina.html`; NOAA PMEL, What
  is El Nino? `https://www.pmel.noaa.gov/elnino/what-is-el-nino/`

### Step 2: Since 1950, in one line

Picture caption: none (the chart is NOAA's data).
- The line follows a box of ocean along the equator that NOAA calls Nino
  3.4. The name is not a latitude. Scientists first watched two boxes
  called Nino 3 and Nino 4, and Nino 3.4 is the box between them,
  overlapping both. It runs from 5 degrees north of the equator to 5
  degrees south, and from 120 to 170 degrees west.
- Each sliver of the chart is one season: a three-month average. The
  seasons overlap, December-February, then January-March, and so on, so
  there are twelve to a year.
- For each season NOAA asks two questions. First: how much warmer or
  cooler than usual is the water in the Nino 3.4 box? Second: how much
  warmer or cooler than usual are all the tropical oceans, taken
  together? The index is the first answer minus the second.
- When the box has warmed more than the tropical oceans as a whole, the
  index is above zero, drawn in red. When it has warmed less, or cooled,
  the index is below zero, drawn in blue. So a season can be red even
  when the box is a little cooler than usual, if the tropical oceans are
  cooler still. What counts is the difference.
- Why subtract? The scientists who proposed this index found that,
  measured the old way, global warming makes El Nino events "seem bigger
  than they are," and La Nina events smaller. Taking away the warming of
  the tropical oceans as a whole takes that out of the measure.
- For the technical reader (a boxed note, smaller type): Vertical axis:
  NOAA's Relative Oceanic Nino Index (RONI), in degrees Celsius. Each
  point is a three-month running mean of the sea-surface temperature
  anomaly in the Nino 3.4 box (5 N-5 S, 120 W-170 W), minus the anomaly
  averaged over all tropical oceans (20 N-20 S), then rescaled to match
  the amplitude of the traditional index. Data: NOAA's ERSST version 6.
  NOAA counts El Nino when the index is +0.5 or more for five
  overlapping seasons in a row, and La Nina at -0.5 or less.
- On this index, the three strongest El Nino events are 1982-83,
  1997-98 and 2015-16. [computed]
- Sources: NOAA CPC, RONI
  `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/`;
  NOAA Climate.gov, Why are there so many ENSO indexes? (2015)
  `https://www.climate.gov/news-features/blogs/enso/why-are-there-so-many-enso-indexes-instead-just-one`;
  NOAA CPC, RONI handout (2026)
  `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/pdf/roni-info-may-2026.pdf`;
  NWS statement 26-05 (13 Jan 2026)
  `https://www.weather.gov/media/notification/pdf_2026/pns26-05_Relative_ONI.pdf`;
  van Oldenborgh and others, Environmental Research Letters (2021)
  `https://doi.org/10.1088/1748-9326/abe9ed`; NOAA CPC, RONI data file
  `https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt`

### Step 3: This year so far

Picture caption: NOAA's RONI, twelve overlapping seasons, to
August-October 2026. [computed]
- NOAA issued its final La Nina advisory in April 2026, as neutral
  conditions emerged. By August-October the index stood at +1.97.
  [computed] NOAA's newest values can still be revised.
- The record on RONI, NOAA's official index, is +2.40, from
  December-February 1982-83. It has not been passed yet. [computed]
- This page's record is NOAA's three-month record on RONI. Other
  agencies report on another stretch of the Pacific, a single month, or
  a forecast, so a record reported elsewhere may not be this one.
- Sources: NOAA CPC, RONI data file (above); NOAA ENSO discussion, 9 Apr
  2026
  `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_disc_apr2026/ensodisc.shtml`;
  Japan Meteorological Agency, El Nino Outlook (10 Nov 2026)
  `https://ds.data.jma.go.jp/tcc/tcc/products/elnino/outlook.html`;
  WMO press conference (6 Nov 2026)
  `https://www.unognewsroom.org/teleprompter/en/3318/wmo-press-conference-06-november-2026`

### Step 4: What NOAA expects

Picture caption: NOAA's chance of El Nino, for overlapping three-month
seasons, issued November 2026. [computed]
- NOAA's chances, from its forecast of November 2026. These are NOAA's
  numbers, not a forecast of ours.
- In its discussion of 12 November 2026, NOAA gives about a 60 percent
  chance of a "historic event" of +2.5 or more on RONI, for
  October-December and for November-January. [read from the discussion]
- NOAA updates these on the second Thursday of each month, and this step
  is redrawn after each update. [only if the monthly promise is kept]
- Sources: NOAA CPC, ENSO probabilities (Nov 2026)
  `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/probabilities/`;
  NOAA ENSO discussion, 12 Nov 2026
  `https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml`

### Step 5: Why the whole planet feels it

Picture caption: No time axis: this is how it works, not a record.
- During La Nina, the tropical Pacific stores extra heat at depth.
  During El Nino that heat goes out into the air, warming the Pacific
  and then the world.
- Global average temperature follows the Pacific's warming, with a delay
  of two to three months.
- El Nino's heat now lands on a warmer world. Whether global warming is
  also making El Nino events stronger is still being studied.
- More on the planet's energy budget: the energy imbalance chart (link
  to its current page; say in the report where it points).
- Sources: NOAA Climate.gov, El Nino and La Nina FAQ (2016)
  `https://prod-01-asg-www-climate.woc.noaa.gov/news-features/understanding-climate/el-nino-and-la-nina-frequently-asked-questions`;
  NOAA Climate.gov, Where does global warming go during La Nina?
  `https://www.climate.gov/news-features/blogs/enso/where-does-global-warming-go-during-la-nina`;
  NOAA Climate.gov, Has climate change already affected ENSO? (2023)
  `https://climate.gov/news-features/blogs/enso/has-climate-change-already-affected-enso`;
  ECMWF, How confident should we be in a prediction of El Nino? (Apr
  2026)
  `https://www.ecmwf.int/en/about/media-centre/science-blog/2026/el-nino-2026`

### Below the steps

- Button: Read NOAA's own discussion (to the discussion), with "Opens
  NOAA's page, updated monthly."
- Footer: Source: NOAA Climate Prediction Center. The index is NOAA's
  Relative Oceanic Nino Index (RONI), 1950 to the latest season; the
  status and the chances are from NOAA's monthly ENSO discussion. / Each
  step lists its sources. Japan's agency and the WMO are named only for
  step 3's sentence on other agencies. / Every build keeps a copy of the
  NOAA files it read. If an update is late, this page says so here. /
  Paloma's Orrery. Drawn from NOAA's data, with Anthropic's Claude.

### Still to open before the words go live

Three sentences rest on sources read only in part on Nov 16; open them
in full in Part 2 and say what you found: the history of the boxes
(Climate.gov, 2015); "warming the Pacific and then the world" (the
Climate.gov FAQ); and the open question's two sources (McPhaden 2023,
read in search; ECMWF, read Nov 16).

Session written November 2026 with Anthropic's Claude Opus 5.5.
