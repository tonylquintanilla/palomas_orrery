<!-- Doc-Kind: hand | Session record of Earth's typed numbers (L-455), the last item of the Sun's numbers half (L-412): the Typed numbers check, thirty Earth rows from open sources, Gemini 4's source worksheet, the approved words; two patches, with Tony's run order. -->
# Handoff: Earth's typed numbers (L-455, the end of the numbers half)

Built on orrery 05cb185ada593eda178b79c57d2a3cbfcce97a24 at
https://github.com/tonylquintanilla/palomas_orrery ("cleanup") and
gallery 10508dfc2ef1afd657e6630d18b7cf00ef50eca6 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Nothing
pushed by this session; Tony pushes.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD. Written October 18, 2026 by Anthropic's Claude Opus 5.5.
Supersedes nothing; follows `HANDOFF_L412_sun_numbers_20261017.md`.
Companions, all shipped by the orrery patch:
- `DISCOVERY_L455_earth_typed_numbers_20261018.md`: every number typed
  into Earth's visitor text, as the new check printed it.
- `WORDS_L455_earth_numbers_20261018.md`: the wording list, revision 3,
  which Tony approved.
- `prompts/RELAY_L455_gemini_earth_sources_20261018.md`: the prompt
  carried to Gemini 4.
- `REVIEW_L455_gemini4_worksheet_20261018.md`: what Gemini 4 confirmed
  and found, and how it did.
Gemini 4's worksheet itself,
`documentation/worksheets/worksheet_gemini4_high_l455_earth_20261018.md`,
is in Tony's orrery folder already, saved by him; it is not in the
patch. Thirty rows' Read lines name it, so it goes in the same commit.

## 1. Your run order (every Tony-action of this session, in one list)

Each patch checks the lines it edits and refuses rather than guess.

1. **(do)** Orrery folder: run `patch_L455_1_earth_numbers_20261018.py`.
2. **(do)** Website folder: run `patch_L455_2_earth_words_20261018.py`
   now, before step 3, but not the Daily Run. The orrery run's
   Dashboard parity reads the website's new Typed numbers check, and
   fails if the website patch is not in yet.
3. **(do)** Orrery maintenance run (dashboard). Expect 31 of 31 gating
   checkers passed, the gate line "0 TIER-1", the whole tree still 280,
   and "Exact rows" with 0 not followed. The Constants change report
   lists the new rows. It rewrites the constants export.
4. **(look)** Mode 5 in the orrery: tick Earth's Low Earth Orbit shell
   and read its checkbox tooltip and its hover. The orbit takes about
   88 to 127 minutes; the counts are 15,900 and 28,015; the dots now
   fill the shell evenly instead of clustering at one height.
5. **(do)** Move the orrery script into `documentation/`; commit it
   with Gemini 4's worksheet and the rest; push. Push before step 6:
   the website's Daily Run pulls the new rows from GitHub.
6. **(do)** The Daily Run. Its pull writes the new rows' values and
   citations into the config, then it builds. Until it has, "Config
   mirror check", "Cache in step", "Typed numbers" and "Display
   figures" are red; that is expected. After it, expect every gating
   check to pass, with the new row "Typed numbers": 0 typed numbers,
   8 held (the Sun's, on L-411).
7. **(do)** Move the website script into `documentation/`; commit the
   config, the cache, the renderer and the checks together; push; then
   `python gallery_maintenance_run.py --live`.
8. **(look)** Mode 5 on the phone, the Earth room: the text boxes and i
   panels of the inner and outer core, the two mantles, the crust, the
   lower and upper atmosphere, low orbit, the geostationary belt, the
   magnetopause, the magnetotail and the Hill sphere.
9. **(decided)** Which of the Sun's drawings follow: answered the same
   evening, "Yes in that order" (section 3).

## 2. What was built

**The check, first.** Tony's starting prompt asked for the discovery
as a check, so the sweep is its output and it runs on every website
maintenance run. `documentation/smoke_typed_numbers.js` builds the Sun
and Earth rooms with no browser, masks every served citation, then
every served number (by scaling the served values and seeing which
printed numbers move), and fails on any digit left standing. A digit
passes only as part of a name (Voyager 1, ISEE-3, IGRF-13), a
citation's locator (a year in brackets, a section or equation number),
or a listed date with the work that states it named. The Sun's eight
known sentences are held, each printed every run with L-411 beside it.
A self-test plants a typed number in each room and breaks a date's
work, and the check must fail on each. It is the gallery run's
"Typed numbers" row, gating, and an orrery dashboard card.

**The orrery, `constants_new.py`.** Thirty Earth rows and one unit
row (seconds per minute), each from an open source read today. The
deep Earth's temperatures come from two open papers, Andrault and
others (2016) for the core's boundaries and Katsura (2022) for the
mantle; the surface records from the WMO; the atmosphere from NOAA,
NASA and UCAR; low orbit's residents and counts from ESA, NASA and
Jonathan McDowell's catalogue. Low orbit's two periods are worked out
by Kepler's third law from the edges' rows and Earth's gravitational
constant (about 88 and 127 minutes), not typed.

**The orrery, the low-orbit tooltip and hover**
(`earth_visualization_shells.py`). Every number prints from its row,
with its citation. `shell_configs.py` held a second copy of the
tooltip; it now uses the module's. The dots are spread evenly between
the shell's two edges; they were clustered at a typed Starlink height.

**The orrery's checks.** The constants change report understands a
row worked out with `math` (it called the periods unreadable). The
exact-rows report follows low orbit's two printed edges.

**The website.** In `data/objects_config.json` Earth's shells link
their new rows and their words are revision 3. `withShellWords` now
reaches the rings, the magnetopause and the magnetotail, and reads
only the numbers a sentence names. The display-figures check grades a
number in braces inside a description.

## 3. Tony's rulings this session

- The starting prompt: "Same method as the Sun's numbers ... Every
  wording change comes to me as a list before it ships ... Build the
  discovery as a check: mask every served number that has a row behind
  it and fail on any digit left standing."
- On revision 1: "There are a lot of unsourced dropped numbers
  especially in sections 2 and 5. Please search for appropriate
  sources so the numbers can come back accordingly."
- He asked for a prompt for Gemini 4, then brought back its worksheet:
  "this is also a good test of the new Gemini model and usefulness for
  mode 3." Its finds replaced every National Geographic figure.
- Revision 3: "Approved with one question: should we split the mantle
  into upper and lower?" Answered yes, as built: both sites draw two
  layers, and Katsura gives figures either side of the 660 km boundary
  between them. The lower mantle's top (1,960 K) reads 30 K cooler
  than the upper mantle's base (1,990 K); that is the paper's, inside
  its 40 K uncertainty, and is left unexplained.
- The Sun's drawings. Tony sent the website's Sun room as it opens:
  "This is the opening view in the interactive. The orrery could be
  similar." Asked whether the opening view, then the corona fade with
  the dust cloud, come next with the ice lines waiting: "Yes in that
  order". On what the target is: "The view is basically Rsun + 10% or
  20%".

## 4. How it was checked

- The orrery maintenance run on the working copy: 31 of 31 gating
  passed; gate path 0 Tier-1; whole tree 280, unchanged; Exact rows
  PASSING, 0 not followed.
- The website maintenance run on a copy whose cache was given the
  config's Earth features: every gating check passed, Typed numbers
  with 287 numbers masked and 8 held. The pull generators fail in the
  sandbox only because it cannot reach GitHub.
- The pre-test: the orrery compiles, opens its window under a headless
  display, and the live dispatch of the low-orbit shell prints the new
  tooltip and hover; its dots lie between 6,558 and 8,378 km.
- The website config in the patch carries pointers and words only.
  Mirrored on a copy from the patched orrery's own export, it comes
  out identical to the tested working copy. Before that mirror, four
  website checks are red, as expected (section 1, step 6).
- The orrery run on the patched copy found one order problem, now in
  the run order: its Dashboard parity needs the website patch applied
  first (section 1, step 2).
- Every source a row adopts from Gemini 4 was re-opened here; each Read
  line names both readers.
- Both patches were run on throwaway copies at the SHAs above, and
  their output compared byte for byte with the working copies.

## 5. Skill versions and what travels

This session's loaded copies read provenance-discipline 2.31
(discharging v3.103's obligation), interactive-exhibit 1.17,
agentic-pre-test 1.3, provenance-cross-check 1.0 and
ledger-and-session-records 1.21, as the manifest expected. No skill was
bumped. One addition is carried on L-351 for interactive-exhibit's next
version: the Typed numbers check, and that a new room's served words
join it.

## 6. What is left, and the next session

- L-455 is DONE. Its loose ends: the orrery's other Earth tooltips and
  hovers still type the old figures, and the geostationary ring's
  height prints 35,786.03 km where a row would give 35,786.04; both
  went to L-413 (Earth's list). The Sun's eight held sentences stay on
  L-411.
- The Sun's numbers half (L-412) is complete with this. The drawings
  follow in Tony's order:
  1. The opening view (L-385), first. Tony's target: "The view is
     basically Rsun + 10% or 20%", as the website's Sun room opens.
     Today the orrery opens about 31 times wider than the Sun,
     because its Sun rotation axis is drawn 52 solar radii long and
     the automatic view widens to fit it. Read the autoscale with the
     Sun's default shells and make it open at the Sun's radius plus
     10 to 20 percent. Whether the long axis is shortened or simply
     runs past the edge of the view is shown to Tony, not assumed;
     his eye decides against his screenshot.
  2. The outer corona's fade with the dust cloud (L-410 with L-131),
     the Hills hover (L-241) inside it, and the streamer belt's seven
     eyeballed numbers with it.
  3. The comet ice lines (L-128) wait behind the objects (L-443).

Starting prompt for the next session:

```
Build session: the Sun's opening view in the orrery (L-385), the first
of the Sun's drawings (L-412). The view opens at about the Sun's
radius plus 10 to 20 percent, like the website's Sun room.
Pull both repositories and say the SHAs; the handoff is
documentation/HANDOFF_L455_earth_numbers_20261018.md, section 6.
Confirm your loaded skills against the manifest before work that fires
them. My eye is the gate. One question per message, plain speech.
```

Session written October 2026 with Anthropic's Claude Opus 5.5.
