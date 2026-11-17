<!-- Doc-Kind: hand | Relay prompt for GPT: an independent review of the El Nino page's revised words (L-060), after Gemini's review. Copy everything below the line into GPT. -->
# Relay prompt for GPT -- El Nino's page, the revised words (L-060)

Written 2026-11-16 by Anthropic's Claude Opus 5.5 for Tony to carry to
GPT at the highest reasoning effort it offers. This is the second,
independent leg: GPT must not see Gemini's worksheet or the review of
it. Two of the rows are DISCOVERY rows.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
and gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\
The return is saved as
documentation/worksheets/worksheet_gpt_<effort>_L060_el_nino_words_20261116.md
in the orrery, the file exactly as GPT exports it.

---

Built on palomas_orrery 16f9bac230eb720204f1910cce3ed8ccb635c8e2 at
https://github.com/tonylquintanilla/palomas_orrery and
tonyquintanilla.github.io 1c5fe516cebaa7b239d34c7573f66a0f6099cc90 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. The
words below are NOT in either repository yet, so every sentence is
written out here.
Vocabulary: v2 (2026-08-13)

## Who you are working for

Tony Quintanilla, PE, a retired civil and environmental engineer,
builds Paloma's Orrery, a science gallery (palomasorrery.com), through
conversation with AI partners. He is not a climatologist, an
oceanographer or a programmer, and has asked for this review because
he cannot judge the best way to present this science himself. His goal
is accuracy in sourcing: every sentence a visitor reads must rest on a
source anyone can open. Please write plainly.

## What is being made

A page on the website about the 2026-27 El Nino, read mostly on a
phone, scrolled one step at a time. Its single source of record is
NOAA's Climate Prediction Center (CPC): its Relative Oceanic Nino Index
(RONI), its ENSO Alert System status, and its monthly ENSO discussion
and probabilities. Other agencies' indices are deliberately left off
the page, and so is NOAA's older index (ONI), because NOAA made RONI
its official index on February 1, 2026.

Above the steps, a status line: "El Nino Advisory. NOAA's latest
update: 12 November 2026. Next expected: 10 December 2026."

## The rules this job follows

You can fetch GitHub. Fetch these at the commit above, read them, and
name them at the top of your answer:

- PROJECT_INSTRUCTIONS.md (section Fetched vs Recalled Convention)
- skills/provenance-discipline/SKILL.md (sections The Access Standard
  and What a Visitor Reads)
- skills/provenance-cross-check/references/worksheets.md (section
  Worksheet Types)
- skills/earth-system-pipeline/SKILL.md (section A Layer's Page and
  Its Walk)

The rules you need are also restated here:

1. **Open sources only.** A source counts only if its text can be read
   without a paywall: open full text, a free abstract that states the
   claim, an agency page or document, an arXiv preprint.
2. **Name what you opened.** Give the title and authors as printed in
   the document you actually opened.
3. **Quote it.** Every row needs a short verbatim quote from the source
   and a locator (section, figure, table, page, or the exact URL). A
   row without both is recorded as UNVERIFIED whatever its verdict
   says. A quotation must be copied from the text you opened; never
   reconstruct one from memory. If you are recalling rather than
   reading, say so and leave the row UNVERIFIED. Silence is better
   than a guess.
4. **Prefer NOAA**, then another agency or a peer-reviewed paper, over
   educational, news or blog pages. NOAA's ENSO blog on climate.gov
   counts as NOAA. A copy of NOAA's data on another site is not NOAA.
5. **Dates matter.** Give the date of every source.

## Before any row: a pre-flight

Open this page and quote one sentence from it, so we know your
fetching works:

```
https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/
```

## Your answer's header

Start with one line naming your MODEL and your REASONING EFFORT, then
the list of rule files you read.

## Two kinds of row

[REVIEW] -- a step's drafted words. Say whether each sentence is
scientifically accurate and whether a non-expert would likely misread
it. If one is wrong or misleading, say what is wrong and what it must
convey instead, with a source that shows it. Do NOT write replacement
wording: the project writes the page's words from the sources.

[DISCOVERY] -- a question with no good source yet. Do not assume one
exists. UNSOURCED is a valid answer, but a negative must show its
search: list the queries you ran and the places you looked, in a
SEARCH LOG under the table. A negative with no search log is recorded
as UNVERIFIED.

## The table

One row per numbered item below (and for a REVIEW row with several
sentences, one row per sentence you find a problem with, numbered
R2a, R2b ...), in this exact layout:

| # | Job | Claim | Your finding | Source (URL opened, access word, date) | Value correct? | Citation correct? | Read by | Quote | Locator | Notes |

- **Access word**: open full text, abstract, agency page, open
  document, educational page, news page, blog.
- Each verdict cell holds EXACTLY ONE token:

```
Value correct?     YES  NO  APPROX  UNVERIFIED
Citation correct?  YES  NO  PARTIAL  DERIVED  UNSOURCED  UNVERIFIED
```

  For a REVIEW row, "Value correct?" answers whether the sentence is
  accurate (APPROX: accurate but likely to be misread; say why in
  Notes), and "Citation correct?" whether your source supports your
  finding.
- Put every URL as a bare address inside a code block, after the
  table, numbered by row. Links pasted as chips lose their address.
- Please deliver the whole answer as a downloadable Markdown file named
  worksheet_gpt_<reasoning effort>_L060_el_nino_words_20261116.md, as
  well as in the chat.

## The rows

### Review rows: the page's words, step by step

R1. Step 1, "What El Nino is", under a sketch of the Pacific in usual
years and in El Nino:
"In a usual year the trade winds pile up warm water in the western
Pacific, off Asia. In an El Nino the trade winds relax, and the warm
water spreads east along the equator."
"Its opposite, when the eastern Pacific runs cooler than usual, is La
Nina. Between them, NOAA calls the Pacific neutral."

R2. Step 2, "Since 1950, in one line", under NOAA's RONI from 1950 to
now drawn as a seesaw, red above zero and blue below:
"Each sliver is one season: a three-month average, overlapping the
next, so twelve to a year."
"Red above the line: compared with its 1991-2020 average, the
equatorial Pacific is warmer by more than the tropical oceans as a
whole. Blue below: by less, or cooler."
"The scientists who proposed this index found that, measured the old
way, global warming makes El Nino events 'seem bigger than they are,'
and La Nina events smaller." (cited to van Oldenborgh and others,
"Defining El Nino indices in a warming climate", Environmental
Research Letters, 2021)
"So NOAA's index compares the central Pacific with the tropical oceans
as a whole, in the same season."
"The three strongest El Nino events: 1982-83, 1997-98 and 2015-16."

R3. Step 3, "This year so far", under the last twelve seasons of RONI
as bars, with the record as a dashed line:
"La Nina ended early in 2026. By July-September the index stood at
+1.69, and NOAA's table now gives August-October at 2.0."
"The record on RONI, NOAA's official index, is +2.40, from the winter
of 1982-83. It has not been passed yet. NOAA's chance of passing it is
in the next step."

R4. Step 4, "What NOAA expects", under bars of NOAA's chance of El Nino
by season (OND 100%, NDJ 100%, DJF 100%, JFM 100%, FMA 98%, MAM 80%,
AMJ 38%, issued November 2026):
"NOAA's chances, from its forecast of November 2026. These are NOAA's
numbers, not a forecast of ours."
"NOAA counts an event as historic at +2.5 or more for a three-month
RONI value. It gives that about a 60 percent chance for
October-December and for November-January."
"They change every month. This step is redrawn when NOAA's next
discussion comes out."
Also: is it sound to show these chances as bars, one per overlapping
season?

R5. Step 5, "Why the whole planet feels it", under a sketch with no
time axis of the ocean taking heat in and giving it back:
"In La Nina years the ocean takes heat in. In El Nino years it gives
heat back to the air, and the world's warmest years tend to follow."
"El Nino's heat now lands on a warmer world. Whether global warming is
also making El Nino events stronger is still being studied."

R6. The page as a whole: a visitor who has just read a news story
calling this "the strongest El Nino on record" arrives at step 3,
which says the RONI record has not been passed. What would they
likely conclude, and is anything on the page missing or misleading
for that visitor? Answer from sources, not opinion.

### Discovery rows

D1. In November 2026, news coverage calls this El Nino the strongest
on record. Find which measure those claims rest on: weekly or monthly
Nino-3.4 values, the traditional ONI, RONI, another agency's index, or
something else. Give at least two dated news or agency sources, each
with the exact sentence that makes the claim and the figure it
cites.

D2. NOAA's two-decimal RONI values. NOAA's file
https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt ended at
JAS 2026 (+1.69) when read on November 16, 2026, while NOAA's RONI web
table (the pre-flight page) showed ASO 2026 at 2.0. Find which NOAA
file carries RONI at two decimals on the dataset the web table names
(ERSST.v6), through the newest season, and give its exact URL from a
NOAA page that links to it. Do not use a copy on another site.

## What not to do

- Do not write wording for the website.
- Do not combine rows, or reconcile one row's figure with another's.
- Do not fill a cell from memory, and never reconstruct a quotation.
  If you could not open a source, the cell is UNVERIFIED and Notes
  says what stopped you.
