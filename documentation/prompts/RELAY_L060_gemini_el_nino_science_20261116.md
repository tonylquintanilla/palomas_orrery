<!-- Doc-Kind: hand | Relay prompt for Gemini: review how the El Nino page presents the science, check its sources, and search for the ones still missing (L-060). Copy everything below the line into Gemini. -->
# Relay prompt for Gemini -- El Nino's page, the science (L-060)

Written 2026-11-16 by Anthropic's Claude Opus 5.5 for Tony to carry to
Gemini, in the desktop app as a Task, at the highest effort tier it
offers: eight of the rows are DISCOVERY rows, which are only as good as
how long the checker keeps looking. The same prompt can go to GPT
unchanged, as a second, independent leg; it must not see Gemini's
answer.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
and gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\
The return is saved as
documentation/worksheets/worksheet_gemini_<tier>_L060_el_nino_science_20261116.md
in the orrery, the file exactly as Gemini exports it.

---

Built on palomas_orrery 16f9bac230eb720204f1910cce3ed8ccb635c8e2 at
https://github.com/tonylquintanilla/palomas_orrery and
tonyquintanilla.github.io 1c5fe516cebaa7b239d34c7573f66a0f6099cc90 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Nothing
below is in either repository yet, so every sentence and value you
need is written out here.
Vocabulary: v2 (2026-08-13)

## Who you are working for

Tony Quintanilla, PE, a retired civil and environmental engineer,
builds Paloma's Orrery, a science gallery (palomasorrery.com), through
conversation with AI partners. He is not a climatologist, an
oceanographer or a programmer, and he has asked for this review
because he cannot judge the best way to present this science himself.
His goal is accuracy in sourcing: every sentence a visitor reads must
rest on a source anyone can open. Please write plainly.

## What is being made

A page on the website about the 2026-27 El Nino, read mostly on a
phone, scrolled one step at a time. Its single source of record is
NOAA's Climate Prediction Center (CPC): its Relative Oceanic Nino Index
(RONI), its ENSO Alert System status, and the season-by-season chances
in its monthly ENSO discussion. Other agencies' indices (Australia's
Bureau of Meteorology, WMO) are deliberately left off the page, so that
two definitions of El Nino are never mixed.

The page has five steps, each a picture above a few sentences:

1. What El Nino is: a sketch of the equatorial Pacific in usual years
   and in El Nino.
2. 76 years in one line: RONI from 1950 to now, drawn as a seesaw, red
   above zero and blue below, the three highest peaks labelled. Under
   discussion: the older index, ONI, drawn as a thin line over it.
3. This year so far: the last twelve seasons of RONI, with the record
   drawn as a dashed line.
4. What NOAA expects: NOAA's chances, season by season, of El Nino and
   of a record-strength El Nino.
5. Why the whole planet feels it: a sketch with no time axis, the ocean
   taking heat in during La Nina and giving it back during El Nino.

Above the steps, a status line: the ENSO Alert System status, the date
of NOAA's latest discussion, and when the next is expected.

## The rules this job follows

If you have imported the palomas_orrery repository, name the date of
your import, read these files and name them at the top of your answer:

- skills/provenance-discipline/SKILL.md -- sections The Access Standard
  and What a Visitor Reads
- skills/provenance-cross-check/references/worksheets.md -- section
  Worksheet Types
- skills/earth-system-pipeline/SKILL.md -- section A Layer's Page and
  Its Walk

If you have not imported it, say so; the rules you need are restated
here:

1. **Open sources only.** A source counts only if its text can be read
   without a paywall: open full text, a free abstract that states the
   claim, an agency page or document, an arXiv preprint. A source
   behind a paywall does not count, whatever its authority.
2. **Name what you opened.** Give the title and authors as printed in
   the document you actually opened, not a paper it cites.
3. **Quote it.** Every row needs a short verbatim quote from the source
   containing the figure or statement, and a locator (section, figure,
   table, page, or the exact URL). A row without both is recorded as
   UNVERIFIED whatever its verdict says. If you are recalling rather
   than reading, say so and leave the row UNVERIFIED. Silence is better
   than a guess.
4. **Prefer NOAA, then another agency or a peer-reviewed paper** (the
   IPCC, WMO, an open journal article, an arXiv preprint) over an
   educational, news or blog page. NOAA's own ENSO blog on climate.gov
   counts as NOAA. Say which kind each source is.
5. **Dates matter here.** This is about an event under way in November
   2026. Give the date of every source, and say when a source is older
   than a newer one that says something different.

## Before any row: a pre-flight

Open this page and quote one sentence from it, so we know your
fetching works:

```
https://doi.org/10.1088/1748-9326/abe9ed
```

## Your answer's header

Start with one line naming your MODEL and your EFFORT TIER, then the
list of rule files you read (or "not imported").

## Three kinds of row

[REVIEW] -- a sentence drafted for the page, or a way of drawing
something. Say whether it is scientifically accurate and whether a
non-expert would likely misread it. If it is wrong or misleading, say
what is wrong and what the sentence must convey instead, with a source
that shows it. Do NOT write the replacement wording: the page's words
are written by the project, from the sources.

[CITATION] -- the row names a source the project already opened. Open
it and confirm it states the claim, at the claim's precision. Then,
separately, check the claim against one other open source of your own
choosing, preferably NOAA's.

[DISCOVERY] -- the claim has no good source yet. Do not assume one
exists, and do not reconcile it with any other row. Find whether an
open source states it. UNSOURCED is a valid and useful answer, but a
negative must show its search: list the queries you actually ran and
the places you looked, in a SEARCH LOG under the table. A negative with
no search log is recorded as UNVERIFIED.

## The table

One row per numbered item below, in this exact layout:

| # | Job | Claim | Your finding | Source (URL opened, access word, date) | Value correct? | Citation correct? | Read by | Quote | Locator | Notes |

- **Read by**: who opened the source -- your model name.
- **Access word**: one of open full text, abstract, agency page, open
  document, educational page, news page, blog.
- Each verdict cell holds EXACTLY ONE token, and the tokens belong to
  their column:

```
Value correct?     YES  NO  APPROX  UNVERIFIED
Citation correct?  YES  NO  PARTIAL  DERIVED  UNSOURCED  UNVERIFIED
```

  For a REVIEW row, "Value correct?" answers whether the sentence or
  drawing is accurate (YES, NO, or APPROX for accurate but likely to
  be misread; say why in Notes), and "Citation correct?" answers
  whether the source you give supports your finding. APPROX qualifies
  a value or sentence (say the tolerance or the problem in Notes).
  PARTIAL qualifies a citation (the source supports part of the claim).
  UNSOURCED means the named source does not state the claim at all; NO
  means it states something different. For a DISCOVERY row, "Citation
  correct?" answers whether the source you found states the claim.

- Put every URL as a bare address inside a code block, after the table,
  numbered by row. Links pasted as chips lose their address.
- Please deliver the whole answer as a downloadable Markdown file named
  worksheet_gemini_<effort tier>_L060_el_nino_science_20261116.md, as
  well as in the chat.

## The rows

### Review rows (the page's drafted words and drawing choices)

R1. Step 2's drafted words, in full:
"Each sliver is one three-month season. Red above the line: the
central Pacific warmer than usual. Blue below: cooler."
"The scientists who proposed this index found that, measured the old
way, global warming makes El Nino events 'seem bigger than they are,'
and La Nina events smaller."
"So NOAA's index compares the central Pacific with the tropical oceans
as a whole, in the same season."
Is this an accurate and fair account of why NOAA uses RONI? Does
"warmer than usual" mislead, given RONI is a relative measure?

R2. A drawing choice for step 2: the older index (ONI) as a thin line
over RONI's seesaw, with a sentence saying that the red and blue show
El Nino itself, the thin line shows the central Pacific's raw warmth
against its own past, warming included, and the gap between them is
the warming. Is "the gap between them is the warming" accurate, given
that RONI is rescaled after the tropical mean is subtracted? Is
showing both lines on one chart sound practice, or does it confuse?

R3. Step 5's drafted words:
"In La Nina years the ocean takes heat in. In El Nino years it gives
heat back to the air, and the world's warmest years tend to follow."
Is this accurate? Is "the world's warmest years tend to follow" still
true and fairly stated as of 2026?

R4. A sentence proposed for step 5: El Nino's heat now lands on a
warmer world; and whether global warming is also making El Nino events
stronger is still being studied. Is that a fair statement of where the
science stands in November 2026? A common belief is that global
warming adds heat to the ocean and the heat comes out as stronger El
Ninos. Say what the science supports and does not support in that
belief, with sources, including any assessment newer than the IPCC's
Sixth Assessment Report (2021).

R5. Records. News coverage in November 2026 calls this the strongest
El Nino on record. On RONI, the highest season in the file is +2.40
(DJF 1983) and the latest is +1.69 (JAS 2026). On which index, and by
what measure, are such "record" claims made? Should the page say which
index a record is on, and is it misleading to say "not passed yet" on
RONI while the news says "record"?

R6. Anything else in the five steps, as described above, that a
non-expert visitor would likely misread, or that a climate scientist
would object to.

### Citation rows (the project opened these, or read them in search)

C1. The relative Nino-3.4 index is the difference between the original
SST anomaly and the anomaly over all tropical oceans (20 S to 20 N); it
describes the onset of convection better and is not contaminated by
global warming. Also: global warming has caused warm El Nino events to
seem bigger than they are, and cold La Nina events smaller, in the
commonly used Nino3.4 index. Source named: van Oldenborgh, Hendon,
Stockdale, L'Heureux, Coughlan de Perez, Singh and van Aalst, "Defining
El Nino indices in a warming climate", Environmental Research Letters
16, 044003 (2021), abstract. Read so far only in abstract listings;
please open the paper itself.
https://doi.org/10.1088/1748-9326/abe9ed

C2. The relative index subtracts the tropical mean SST anomaly from the
Nino-3.4 index and multiplies by a scaling factor, and gives a more
consistent classification of historical El Nino and La Nina conditions,
more robust across climatological periods. Source named: L'Heureux,
Tippett, Wheeler and others, "A Relative Sea Surface Temperature Index
for Classifying ENSO Events in a Changing Climate", Journal of Climate
(2024), abstract, NOAA repository copy.
https://repository.library.noaa.gov/view/noaa/67067

C3. Where waters are warmer relative to the tropical average, there is
more rising motion, cloud formation and rainfall than where waters are
relatively cooler. Source named: NOAA ENSO blog, climate.gov, "Is ENSO
running a fever, or is it global warming?" (read in search excerpts
only; please open the post and give its date and author).
https://www.climate.gov/news-features/blogs/enso/enso-running-fever-or-it-global-warming

C4. NOAA's RONI file: the latest season is JAS 2026 at +1.69; the
highest in the file is DJF 1983 at +2.40, then NDJ 1982 at +2.36, NDJ
1997 at +2.28 and NDJ 2015 at +2.25; the last twelve seasons run from
ASO 2025 at -0.78 through NDJ 2025 at -1.04 to JAS 2026 at +1.69. Please
also report the file's newest row on the day you open it, in case a
new season has been added.
https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt

C5. NOAA's ENSO diagnostic discussion issued 12 November 2026: the ENSO
Alert System status, and the next discussion scheduled for 10 December
2026. Please also transcribe its season-by-season probability table
exactly as printed (each season's chance of La Nina, neutral and El
Nino), and every figure it gives for the chance of a record-strength or
very strong event, with the threshold and index each figure is stated
on.
https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml

C6. The IPCC's Sixth Assessment Report found no clear evidence yet of a
climate change effect on tropical Pacific SST anomalies; found no model
consensus for a systematic change in the intensity of ENSO SST
variability over the 21st century (medium confidence); and found it
very likely that ENSO rainfall variability will increase significantly
by the second half of the century. Sources named: NOAA ENSO blog,
climate.gov, "ENSO and Climate Change: What does the new IPCC report
say?" (2021), and "Has climate change already affected ENSO?" (guest
post by Mike McPhaden). Please confirm against the IPCC AR6 Working
Group I report itself (Summary for Policymakers or Chapter 4), with
the exact wording and its locator.
https://www.climate.gov/news-features/blogs/enso/enso-and-climate-change-what-does-new-ipcc-report-say

C7. ENSO SST variability increased after 1960, with more frequent
strong El Nino and La Nina events; climate models attribute an increase
of approximately 10 percent in post-1960 ENSO amplitude to greenhouse
warming. Source named: Cai and others, "Anthropogenic impacts on
twentieth-century ENSO variability changes", Nature Reviews Earth and
Environment 4, 407 (2023), doi 10.1038/s43017-023-00427-8; an open copy
appears to be at the address below. Please say whether later work
(2024 to 2026) supports, qualifies or disputes it.
https://par.nsf.gov/servlets/purl/10432496

C8. No internationally agreed El Nino threshold exists: NOAA's CPC uses
+0.5 C on its relative index, Australia's Bureau of Meteorology +0.8 C.
Source named: WMO, "Understanding ENSO Indices" (April 2026), read in a
search excerpt only (the address below; a news page gave the same).
https://wmo.int/sites/default/files/2026-05/Understanding%20ENSO%20Indices_April2026.pdf.pdf

### Discovery rows (no good source yet)

D1. NOAA's own definition of RONI and of an El Nino episode on it:
which SST dataset, which region, which tropical band, the rescaling,
and the rule (threshold and how many consecutive overlapping seasons).
The project has this only from a non-agency page. Find it on a NOAA
page or document.

D2. The date NOAA made RONI its official index for monitoring and
forecasting, and whether NOAA still publishes ONI. Find a NOAA source.

D3. Step 1's picture and words: in usual years warm water piles up in
the western equatorial Pacific under the trade winds; in El Nino the
trade winds weaken and the warm water spreads east. Find a NOAA page
(or another agency's) stating this in words.

D4. Step 5's picture: the ocean takes up heat during La Nina and
releases it to the atmosphere during El Nino (the recharge and
discharge of the Pacific's heat). Find an agency page or open paper
stating this in words, in a form a lay reader could follow.

D5. El Nino raises the global mean surface temperature, with the
largest effect a few months after its peak, so the year after an El
Nino peak tends to be warmer. Find a NOAA, NASA, WMO or Copernicus
source, with the lag if it gives one. Note: one NOAA blog post says
2016 was the warmest year on record; later years have been warmer, so
please give the current statement.

D6. Whether this 2026-27 event is, or is forecast to be, the strongest
on record on RONI, as of the newest NOAA statement you can find, and
whether NOAA has said so in its own words.

D7. What NOAA says the ONI shows that RONI does not, in its own words:
whether NOAA describes the difference between the two indices as the
tropical oceans' warming, or in some other way.

D8. Any open, peer-reviewed criticism of the relative index (RONI or
relative Nino-3.4): its limits, what it hides, or where the original
index is still the better measure, for example for marine heat or
impacts that depend on absolute temperature.

## What not to do

- Do not write wording for the website. Say what is wrong and what a
  sentence must convey; the project writes the words.
- Do not combine rows, or reconcile one row's figure with another's.
- Do not fill a cell from memory. If you could not open a source, the
  cell is UNVERIFIED and Notes says what stopped you.
