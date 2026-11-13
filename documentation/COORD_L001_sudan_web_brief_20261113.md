<!-- Doc-Kind: hand | The brief for one Claude Code session through the python_work door: L-001 (food insecurity), Sudan's three IPC periods in one Google Earth file built for Google Earth on the web, and the website card that opens it. Communication; written once, read by its session. -->
# Brief: Sudan's three periods, on Google Earth web (L-001)

Built on orrery 11662222b00babb5b1551b0d7b603eebdf65036a at
https://github.com/tonylquintanilla/palomas_orrery
and gallery d377726992ca73f0976fb3809c3f1f6eee330373 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-13, 14:40 Chicago). Nightly bot commits
since are expected. This brief and the three new files in data/ (named
under "The data" below) are in Tony's next orrery push; the session
reads them in the folder in front of it.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session in the ORRERY, through the
python_work door, with one small change in the GALLERY in Part 3.
Written November 13, 2026 with Anthropic's Claude Opus 5.5, the
coordinating session. It supersedes the build plan in
`documentation/HANDOFF_food_insecurity_sdn_projections_20261112.md`
(its findings still hold; its steps 1 to 3 do not: the projection
GeoJSON files it asked for do not exist, see "The data"). It goes
before Mars (L-514), by Tony's word of Nov 12, 22:42.

## What this is, in one paragraph

The Sudan food-insecurity layer draws one period, February-May 2026,
as a Google Earth Pro file. IPC's same analysis also projects June-
September 2026 (the lean season) and October 2026-January 2027 (the
harvest season, which is now), for 56 of Sudan's 195 areas. Google
Earth Pro on the desktop stops being offered on 25 June 2027, and the
web version needs no download, so Tony ruled to move to the web. This
session builds ONE file holding all three periods, written so Google
Earth on the web keeps it, fixes an error the June data file carried,
and makes the website's Sudan card open Tony's shared Google Earth
project instead of downloading a file.

## The rulings (Tony's words and times, Chicago)

1. Nov 12, 23:10: South Sudan waits for IPC's next analysis (its
   newest, April-July 2026, has ended). "Yes. Thanks."
2. Nov 12, 23:11: June-September is a third layer. "Yes"
3. Nov 13, 11:10: rebuild February-May from the corrected file. "yes."
4. Nov 13, 11:50: the seven displacement camps are drawn as small
   circles coloured by phase, with the full pop-up, in all three
   periods. "yes, thanks."
5. Nov 13, 12:25: one file holding all three periods, opening on
   October-January. "one file as recommended."
6. Nov 13, 12:32: "i think we should migrate to the web. it is also
   more accessible to people that do not download the app."
7. Nov 13, 13:59: "the question is whether we will update the app
   link. i would lean to, no. so we can focus on the web version."
   The coordinator's reading, said to Tony and not corrected: the card
   links only to the web project; the file link comes off.
8. Nov 13, 14:31: "Yes, please proceed" (this brief).

## What the coordinator found (checked Nov 13; re-check, do not trust)

- IPC's GeoJSON download gives the February-May features whatever
  period is selected; only its header's "active" flag changes. Both
  the June file and `data/IPC_SD_A_87143417_2026-11-13.geojson` hold
  February-May features only.
- THE JUNE FILE WAS WRONG. In 152 of 228 features of
  `IPC_SD_A_87143417_2026-06-22.geojson`, the five phase counts add up
  to more than the area's population (phase 3 too high). In the Nov 13
  file all of them add up. The report's February-May table (PDF page
  46) matches the Nov 13 file: Al Malha 69,143 in Phase 3+ (60%),
  where the June file says 97,953. The live layer's pop-ups show the
  June counts. Phase colours did not change, except Abyei PCA: no
  phase in June, 0 (population 0) in Nov 13.
- The Excel export holds all three periods, area by area:
  `data/IPC_SD_Acute_Food_Insecurity_Analysis___SD_February_2026_2026-11-13.xlsx`,
  sheet "Population Table". Its 196 area names (rows indented by two
  spaces; unindented rows are state totals and "ANALYSIS TOTALS")
  match the GeoJSON's 196 distinct names one for one. Each period has
  Est Pop, Phase 1-5 with %, Phase 3+ with %, From/Thru dates and a
  Phase code "P0"-"P5"; "P0" is not analysed. Some Est Pop cells are
  text. Projected 1 (June-September) and Projected 2 (October-January)
  each analyse 56 areas. Al Malha's rows match the report's tables on
  PDF pages 52 and 54, except one person: Phase 3+ June-September is
  74,905 in the report and 74,904 in the Excel.
- 189 GeoJSON features are polygons (names unique), 39 are points.
  Seven of the 56 projected areas are camps that exist only as points:
  Ad Du'ayn IDPs, Um Baru IDPs, At Tina IDPs, Tawila IDPs, Al Buram
  IDPs, Kadugli IDPs, "Um Durein  IDPs" (two spaces, as IPC spells it).
  The generator skips all points today.
- `risk_of_famine` is False in every feature of both files, and the
  generator reads it (line 263) but draws nothing from it.
- Google Earth web, tested with Tony's import of the live file and a
  test file (`ge_web_test.kml`, coordinator's; Tony's look on his phone
  Nov 13, 14:30):
  - Colours referenced from styles inside a Folder are LOST (every
    area plain yellow; 228 "referencing a style that does not exist"
    errors). Shared styles at Document level, and styles written
    inside a placemark, both WORK.
  - ScreenOverlay is "Unsupported". The title and legend cards vanish.
  - In pop-ups: `<br>` and plain newlines are stripped (lines run
    together); `<table>` becomes the words "TABLE SECTION". `<p>`,
    `<div>` and `<ul><li>` each keep one item per line; `<b>` and
    `<a href>` work. ExtendedData shows as labelled fields, but below
    Google's own Area and Perimeter boxes.
  - A Folder with `<visibility>0</visibility>` arrives switched off.
    radioFolder (one at a time) could not be confirmed; assume not.
  - A Point with a coloured IconStyle circle shows (T10, phone look).
  - A project shared "Anyone with the link" opens for a viewer who is
    not signed in, as View only.

## The design

THE DATA. Per-area figures for all three periods come from the Excel,
read at run time, never typed in. Outlines come from the Nov 13
GeoJSON. Join by area name after stripping the Excel's leading spaces.
The Excel's "Current" columns must equal the Nov 13 GeoJSON's figures
for every area; any difference stops the run with the area named. The
June GeoJSON stays in data/ and is no longer read. A phase code "P0",
0 or missing is drawn and worded as not analysed (white, "Not
analysed"), never "Phase 0".

ONE FILE. `data/food_insecurity_sdn_blockbuster.kmz`, name unchanged.
Three period folders named with IPC's own names and dates: "Current:
February - May 2026", "Projected 1: June - September 2026", "Projected
2: October 2026 - January 2027". Projected 2 is visible when opened;
the other two carry visibility 0. Each folder holds that period's
areas, its camps and its Phase 5 dots (L-069). Areas IPC did not
analyse in a projection are drawn white and say so.

WRITTEN FOR THE WEB.
- Every style is a shared style at Document level, referenced by id:
  one per phase, one for not analysed, one per circle kind. None
  inside a Folder.
- No ScreenOverlay. The title card's and the legend's content moves
  into the "i" pin's pop-up, as lines: what the map shows, the period,
  each phase with its colour named in words, and the 20-percent rule
  sentence (earth-system-pipeline: the legend must state it).
- Pop-ups use one `<div>` per line, `<b>` for labels; no `<table>`, no
  `<br>`. Every area's pop-up keeps the FULL phase 1-5 breakdown,
  people and percent, then Phase 3+, the period, IPC's evidence and
  assistance levels as now, and the source lines. "Data retrieved" reads
  the export's date, 2026-11-13. The framing folder's text follows the
  same rule.
- The camps: Point placemarks at IPC's own point, a circle in the
  phase colour, the same full pop-up as an area.

EACH PERIOD'S NATIONAL LINES, transcribed (earth-system-pipeline,
"Transcribe, don't sum"; re-read each at its PDF page before it
becomes a constant with a # Source line; pages are the PDF's own count,
the report's printed footers run one higher). They go in each period
folder's description and in the "i" pop-up.
- Current, February-May 2026: the generator's existing constants,
  unchanged (NATL_* at lines 122-125).
- Projected 1, June-September 2026, PDF page 22: "Around 2.2 million
  people are expected to experience Emergency (IPC Phase 4)", "a
  further 3.1 million will likely be in Crisis (IPC Phase 3)", "5.6
  million people during the lean season, corresponding to 67 percent
  of the analysed population", and Catastrophe "nearly 200,000".
- Projected 2, October 2026-January 2027, PDF page 28: "an estimated
  4.9 million people (59 percent of the analysed population)", "over
  71,000 people in Catastrophe (IPC Phase 5), 1.7 million in Emergency
  (IPC Phase 4), and 3 million in Crisis (IPC Phase 3)."
- Both projections carry a coverage line, PDF pages 22 and 28: "56
  areas out of 195 units of analysis", "equivalent to nearly 8.3
  million people out of the total population of Sudan (47.5
  million)." Their numbers describe those 56 areas, never all Sudan.
- The Excel's own analysis totals are not shown (Projected 1's total
  row divides by all 47.5 million and prints 12 percent).

RISK OF FAMINE, PDF page 26, transcribed as two named lists (the files
carry no flag). Projected 1, 14: At Tina locality, At Tina IDP
settlement, El Fasher locality, Kernoi locality, Tawila IDP settlement,
Um Baru locality, Um Baru IDP settlement, Dilling locality, Kadugli
locality, Kadugli IDP settlement, Al Buram locality, Al Buram IDP
settlement, Um Durein IDP settlement, Beliel locality. Projected 2, 13:
the same without Beliel. Map the report's names to the data's in one
dict with a # Source line ("El Fasher" is "Al Fasher" in the data;
"... IDP settlement" is "... IDPs"); each must resolve to exactly one
area or the run stops. Current: none drawn (no list for it here; record
the gap). On the layer: one pop-up line in each listed area, in IPC's
words, "Risk of Famine (reasonable worst-case scenario)". A visible
mark on the map is NOT settled: propose one in the Part 2 report and
Tony rules at his look.

## Start

1. Record both bases; say whether either moved past the anchor above.
2. Load the skills the job fires and compare each version line with
   the manifest: earth-system-pipeline 1.2, provenance-discipline 2.36,
   safe-file-editing 1.14, agentic-pre-test 1.3, gallery-pipeline 1.2
   (Part 3), ledger-and-session-records 1.23 (close). Stale = stop.
3. Read food_insecurity_generator.py and scenarios_food_insecurity.py
   whole; map where the KML is built and where the "i" pin, framing
   folder and Phase 5 dots come from (earth_system_common.py).

## The job, in three parts, with a stop and a report after each

PART 1, THE DATA (no KML change). A reader for the Excel and the join.
Report, by name not count where short: the 196-name match; the Current
columns against the Nov 13 GeoJSON (every area, any difference
named); the 56 analysed areas in each projection; the seven camps; the
famine lists resolved to areas. Stop.

PART 2, THE FILE. Build the one file as designed: period folders,
shared styles at Document level, web pop-ups, camps, famine lines,
national and coverage lines, Abyei. Then agentic-pre-test, and the KMZ
byte checks: no Style inside a Folder, no ScreenOverlay, no `<table>`
or `<br>` in any description, every styleUrl resolves at Document
level, 3 period folders with visibility 1/0/0 as designed, phase counts
per period printed by name of phase. Then write Tony's steps, in Google
Earth web's own buttons, to replace the contents of his shared Sudan
project (https://earth.google.com/earth/d/1X6rIf_0j_qfo-OdS-tQU7Kp4R-exuvJG)
with the new file so its link does not change, and to look on his
computer and phone. Report, with the map-mark proposal. Stop. Tony's
look closes it.

PART 3, THE CARD AND THE RECORDS. In the gallery, the Sudan card's
Google Earth button (index.html, `kmz-handoff-btn`, set from the
layout's `_kmz_handoff`, around line 4173) downloads
`gallery/assets/food_insecurity_sdn_blockbuster.kmz`. The button is
shared by every Earth System card. Propose the smallest change that
makes the Sudan card open Tony's shared project in a new tab and
leaves the other cards as they are, and whether the stale asset goes;
Tony rules; then build it and run the gallery's checks. Then the
close.

## Out of scope

South Sudan (ruling 1). The website teaser map (its phases and Phase 5
counts are unchanged). The Earth System controller and GUI launchers.
The other Earth System layers on the web: open one ledger item for
them at the close (the heat layers use ScreenOverlays and folder
styles the same way).

## Checks

py_compile and the pre-test on a throwaway copy; the provenance
scanner, Tier-1 = 0 on the active build path; the KMZ byte checks
above; the gallery run's checks in Part 3. Tony's look on Google Earth
web, computer and phone, is the gate.

## Close

L-001: the eight rulings, what was built, the June file's error and
its fix, the web findings, the gaps (Current's famine-risk list; the
map mark if not ruled). L-070 (other countries): ruling 1. A new item
for the other Earth System layers on the web. earth-system-pipeline:
propose a version with the web rules (styles at Document level, no
ScreenOverlay, pop-up lines in `<div>`, no `<table>` or `<br>`, the
GeoJSON download holds Current only) and bump it only on Tony's
go-ahead. Where We Are, at its anchors. The session's token count, as
the protocol's Token Economy asks.

## Amendment, Nov 13, 16:05 (Tony's rulings of 15:51 and 15:59)

This replaces Part 3's card step; everything else in Part 3 stands.

9. Nov 13, 15:51, on three ideas the coordinator offered for the Earth
   System's move to the web: "I think they work well together." The
   three: (a) each layer's short page is its one home, written by the
   generator from the text the scenario files already carry; (b) a
   network link inside each Google Earth project fetches the file from
   the website, so an update needs no re-import (unverified: one test,
   later); (c) not every layer needs Google Earth, a still picture on
   its page may be enough.
10. Nov 13, 15:59: "The Sudan map is a priority so should be shown
   regardless as a featured item. Then the new room migration, after
   Mars and the rest of the moons. We may interrupt again for
   something else like el nino."

PART 3, REVISED.
- SUDAN'S SHORT PAGE. The generator writes it, beside the KMZ, so its
  words and their sources live in one place (idea a). One page, built
  upright and phone-first: the title; the three periods by IPC's names
  and dates; each phase with its colour named in words and the
  20-percent rule; the two projections' coverage line; IPC's credit
  and citation; and one button, "Open the map in Google Earth", that
  opens Tony's shared project in a new tab. Every number on it is
  transcribed or composed by the provenance rules, as on the layer.
  A still picture of the October-January map, drawn by the generator
  from the same data at every build, never a screenshot. Propose
  where the page and picture live in the gallery, and Tony rules.
- FEATURED. The lobby's Featured board gets an item that opens the
  short page (ruling 10). The board's rules are L-519's; propose the
  smallest way to give it an item that opens a page, and Tony rules.
- THE OLD SUDAN CARD. Its Google Earth button opens the short page
  instead of downloading the file. Whether the stale KMZ asset goes:
  propose; Tony rules.
- Google Earth web will not show its projects inside another site's
  page: every earth.google.com address answers X-Frame-Options
  SAMEORIGIN, ?embedded=true included (checked Nov 13). So the page
  links out; it does not frame the map.

RECORDED, NOT BUILT (put in the ledger at the close).
- The Earth Science room in the interactive site, laid out like the
  Solar System room (drawers and rows, by theme), after Mars and the
  rest of the moons (ruling 10). Meanwhile plan, for its design talk:
  the room's rows first link to the old cards (index.html opens a
  card from #<card id>); the old lobby hides its Earth System rooms
  (74 cards, about 37 layers with their phone versions); each row
  moves to its new page as its layer is made web-ready, and that old
  card goes. Check first where closing an old card lands a visitor
  who came from the new room. About a dozen rows are charts, not
  Google Earth layers.
- Ideas (a), (b), (c) of ruling 9, with (b)'s test.
- An interruption such as El Nino may come before the room (ruling 10).

Session written November 2026 with Anthropic's Claude Opus 5.5.
