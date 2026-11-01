<!-- Doc-Kind: hand | Brief for a short gallery Claude Code session: the website's night of Nov 1 went red on the Display figures check because the inner Van Allen belt's pinned sentence still says 9,600 km after the orrery's rounding fix; the pin moves to 10,000 km and the hover fixture is re-recorded. Written by the coordinating session; zero code. -->
# Brief: the gallery session (the Display figures pin after the rounding fix)

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | November 1, 2026, 09:05

Written at orrery 0c0bac8aa3dc9e76ba4c6b4533bc37cf5028c440 at
https://github.com/tonylquintanilla/palomas_orrery (branch main; the
night's record commit on top of Tony's push 0edcd788 of the orrery
session's work) and gallery c1c578f57f812aa0dcc0f1fec45bab43e7826bd0
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(branch main). Both read live on Nov 1, 14:50 UTC. YOUR BASE IS HEAD
WHEN YOU OPEN THE SESSION; read it yourself.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a SHORT build session in the GALLERY repository. The
ledger items: L-484 (the two agree: the rounding) and L-485 (a nightly
run). The session reads this file first; the orrery session's brief
`COORD_L485_orrery_rounding_hold_pins_brief_20261031.md`, section 1,
says what changed in the export and why.

## 1. What happened

- The orrery session of Oct 31 fixed the export's rounding (L-484).
  Five served conversions changed; one of them is printed in a room:
  `EARTH_VAN_ALLEN_INNER_RADII` in km, 9,600 before, 10,000 now (1.5
  Earth radii at two figures is 9,567 km; a unit in the source's last
  place is 638 km, nearest the thousands, so the kilometres round at
  the thousands place: 10,000).
- The website's night of Nov 1 (run 2, by hand, 14:24 UTC) pulled that
  export, built the cache, and went RED in the maintenance run's night
  pass: "1 of 36 gating checkers FAILED: Display figures", two
  findings, both the same hover: "Earth: Inner Radiation Belt: the
  hover does not carry the approved line = 9,600 km (0.00006 AU)" and
  "earth/Earth: Inner Radiation Belt carries no declared count and its
  hover changed" against the fixture recorded at gallery 7a4a03a8.
  Nothing was committed; the site still serves the old cache and the
  old sentence. The gate did its job on a number that changed on
  purpose.
- Neither the orrery session nor the coordinating session grepped the
  website's CHECKS for the old number before the push; both read only
  the renderers. That is the lesson, recorded in section 4.

## 2. The fix, two parts, in this order

1. **The pin.** `documentation/smoke_display_figures.js`, the
   ACCEPTANCE_LINES entry "Earth: Inner Radiation Belt" (about line
   617): "= 9,600 km (0.00006 AU)" becomes the line the room now
   builds. Expected: "= 10,000 km (0.00006 AU)" (the AU conversion
   did not change: one figure, 0.00006). READ THE BUILT HOVER FIRST
   and pin what it prints, with a comment naming L-484 and the date;
   if the built line is not that string, say so and stop. Its `absent`
   list gains "9,600" so a return of the old rounding fails by name.
2. **The fixture.** The check holds every count-less hover byte for
   byte against `fixture_hovers_L497_on_7a4a03a8.json`. Re-record it
   by the file's own convention (its header, lines 60 to 287): a NEW
   file named for the item and the gallery commit it is recorded on
   (`fixture_hovers_L484_on_<gallery sha>.json`), `FIXTURE_AT` and
   `FIXTURE` pointed at it, the header gaining the paragraph that says
   exactly which hovers differ from the L-497 one ("earth/Earth: Inner
   Radiation Belt" alone, expected) and that the others are byte for
   byte; the L-497 one left in place, unreferenced. The recording
   (`node documentation/smoke_display_figures.js --record`, gallery
   root) must be made from a cache built from the NEW export, so the
   Daily Run (the pulls, then the builder) runs before it; read the
   mirrored config and the served index to confirm the belt's row
   carries the new km before recording. Then the check, green, and
   its self-test still going red its 21 ways.

Nothing else. The belt's 90th height ("about 100 million km") is
graded by arithmetic in the Solar System figures check, which passed
on the same run; no pin there.

## 3. The run, then the night

- `python daily_run.py` from the gallery root (the Run button): the
  guest book, the pulls (the new export lands; the Objects export pull
  accepts schema 4, `SCHEMA_WANTED = 1`), the builder, the run records,
  the offline maintenance run, which is red on Display figures until
  part 1 is done and the fixture re-recorded; then the maintenance run
  again, green, read from its output: 36 of 36.
- Tony commits and pushes the gallery (the check, the new fixture, the
  served cache and the pulled files the Daily Run wrote).
- Then "Run workflow" on the website's Actions tab, by hand, and its
  log read to "NIGHT RUN: CLEAN" (or the next night's schedule, which
  fired seven hours late on the orrery today; the brief's author
  prefers the run by hand so the site changes today).
- Tony's phone, after closing the saved tab: the belt's text box
  reads "about 100 million km" for the 90th height; Earth's inner
  radiation belt reads "= 10,000 km (0.00006 AU)".

## 4. Records

- L-484 (the two agree): the website's pin moved and why; the fixture
  re-recorded, named; THE LESSON: a served number that changes on
  purpose is grepped in the OTHER repository's checks (the acceptance
  lines and the hover fixture are consumers of the export, as much as
  the renderers are) before the push, and the brief for such a change
  names the pins that move. For the next version of
  gallery-cache-builder or provenance-discipline, whichever the next
  orrery session judges: write the sentence on L-484, do not edit a
  skill from the gallery.
- L-485 (a nightly run): the website's run 2 of Nov 1, red by name,
  and what it proved: the gate refused a cache whose words did not
  match a pin, as designed. Also, read from GitHub by the coordinating
  session: the orrery's schedule fired at 14:17 UTC on Nov 1, seven
  hours late (its run 4), and Tony's hand-fired run 5 queued behind it
  under the concurrency group; each clean run commits its own record,
  so two record commits landed (b0acdea, 0c0bac8). The website's
  schedule has not fired by itself yet (its runs 1 and 2 were both by
  hand). GitHub's page, read Nov 1: "The schedule event can be delayed
  during periods of high loads of GitHub Actions workflow runs" and
  "If the load is sufficiently high enough, some queued jobs may be
  dropped." A backstop (a second scheduled time) is for the next
  design talk, not this session.
- Where We Are: the box's "Changed" line for the belt sentence stands;
  "Do next" becomes the gallery push and the run by hand; the marker
  and the zone untouched. Records in the ORRERY's documentation folder
  per the ledger skill; the gallery folder gets nothing but the code.
- The final report per the gallery's CLAUDE.md: files changed with edit
  counts, Tony's run order, the rollup. ASCII, LF.

## 5. Tony-action rollup

- (do) Open a Claude Code session on the gallery repository (the
  python_work door: the prompt names the gallery) and paste the prompt
  the coordinating session gives you.
- (do) Afterwards: commit and push the gallery; "Run workflow" on the
  website's Actions tab; the phone look.
- (decide) Nothing.

Written November 1, 2026 with Anthropic's Claude Fable 5.1.
