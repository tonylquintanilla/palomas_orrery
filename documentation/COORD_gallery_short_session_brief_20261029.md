<!-- Doc-Kind: hand | Brief for the short gallery Claude Code session of Oct 29-30, 2026: L-399's guard tolerance so 2026 ED138 is served, the triad lower still (L-502), and, if room, the shared link that keeps the view. Written by the coordinating session; zero code. -->
# Brief: the short gallery session (L-399, L-502, the shared link)

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 29, 2026, 18:05

Built on orrery dceb4dc6344e73c3c8a82df684cf54f5bf5e6c25 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b3b4826f4280b795e2efe2e9e30efa3e6be23ae4 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both read live with git ls-remote on Oct 29, 17:55. Every line
number below was read from those two commits.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a build session in the GALLERY repository, item 1 of
`HANDOFF_coordination_20261028_29.md`, section 5. The session reads
this file and that handoff before anything else; Where We Are's "Do
next" line at HEAD names Tony's steps of Oct 29 afternoon, all done,
so this brief is the job.

## 0. The base, and what is waiting

- Gallery: b3b4826f, clean. If `git status` shows anything, stop and
  say so.
- Orrery (the sibling folder): dceb4dc6, with TWO uncommitted files
  Tony knows about and commits with this session's records:
  `documentation/HANDOFF_coordination_20261028_29.md` (the
  coordination handoff, 12,265 bytes) and his run record
  `documentation/WHERE_WE_ARE_10-28-26_2357_run_record.md` (his
  phone looks and SHAs were added after the 17:03 push). Those two are
  expected; anything else waiting is not. This brief will be a third,
  once Tony has it in the folder.
- Skills this job fires, each read in full from the orrery folder
  before the work, versions stated in the first report against the
  manifest in PROJECT_INSTRUCTIONS.md v3.117: gallery-cache-builder
  1.13, interactive-exhibit 1.28, gallery-assembler 1.3,
  ledger-and-session-records 1.22, safe-file-editing 1.14,
  agentic-pre-test 1.3. ONE THING TO KNOW about interactive-exhibit
  1.28: six of its sentences are out of date since the Oct 29 builds
  (listed on L-503 (the belt on the website), "For
  interactive-exhibit's next version"); where the skill and that list
  disagree, the list is right. A gallery session reads the skills and
  does not edit them; 1.29 is the next orrery session's.
- The session asks Tony ONE question in all; this brief leaves none
  open, so the one question is spent only if the work finds one.

## 1. L-399 (each small body's own uncertainty): the guard refused 2026 ED138

WHAT HAPPENED. The builder asks JPL for each small body's position
uncertainty (the 2xr vector table) at the moment of the body's served
"you are here" point, and serves it only if the answer's position
matches that point. The match tolerance is a fixed distance:
`UNCERTAINTY_MATCH_AU = 1e-7` (about 15 km), at
`tools/gallery_cache_builder.py` line 556, used at line 665. Its
comment says the two are "the same JPL solution at the same moment,
so they agree to Horizons' printed digits". The Daily Run of 14:05
UTC served 51 of 54 and ED138 among them (444,725 km, its own
3-sigma). The Daily Run of 21:57 UTC served 50: ED138 refused, "JPL's
2xr answer sits 8.88e-05 AU from the served point, so another record
answered". 8.88e-05 AU is about 13,000 km, a thirtieth of the body's
own uncertainty. The fallback worked as designed: no uncertainty
served, so the room prints ED138 to the tens with the honest sentence.
The live site shows that now, and Tony's look (run record, item 6)
says "reads to the 10's still".

FIRST, THE CAUSE (Discovery over Delivery: investigate, understand,
document, then fix). Today the refusal keeps only the distance; the
answer itself is thrown away, so nobody can tell afterwards WHAT
answered. Two steps:

- Make the refusal name its items. The missing reason, and the run
  record under `position_uncertainty`, carry the answer's X, Y, Z and
  the served point's (AU, as JPL printed them), the R_s the answer
  carried, and the body's JPL id as asked. A refusal read a week later
  must be diagnosable from the record alone.
- Ask JPL once now, in the session, for ED138's 2xr row at the served
  moment, JD 2461342.500694444 TDB, measured from the Sun, and compare
  it with the served point in `data/solar-system/raw/vectors/tno_2026_ed138.json`
  (x 2.523967238837812, y -44.57300836441859, z -15.3947905194702 AU)
  and with the day before's point there. The body moves about 0.0024
  AU a day, so 8.88e-05 AU is about 53 minutes of its motion: a
  difference ALONG the motion says the two queries were not asked at
  the same moment; a difference ACROSS it says JPL's orbit solution
  for ED138 changed between the range fetch and the 2xr question (it is
  a 2026 discovery, and JPL revises such orbits as observations
  arrive). Report which it was. If it cannot be settled, say so; the
  fix below holds either way.

THE FIX (Tony's direction, handoff section 4): the tolerance is
measured against the body's own uncertainty, not a fixed 15 km. The
session chooses the exact rule and states it in the report with its
reason, this being method (the skill's), not a ruling to put to Tony.
The shape the coordinating session expects, to be confirmed or
corrected by what the cause turns out to be:

- Read R_s from the answer first (an answer with no R_s serves nothing
  whatever its position, as now). Then accept the answer when it lies
  within the larger of the present floor (1e-7 AU) and the body's own
  3-sigma range (3 x R_s) of the served point. Ceres (0.01 km) and
  Apophis (0.4 km) keep the floor; ED138 (444,725 km) gets its own.
- Why another record would still be refused: a different body sits
  AU away, far outside any body's 3-sigma. The ONE case where another
  record can sit close is a comet with pieces, C/2025 K1 and its B, C
  and D (`c2025_k1*` in `data/objects_config.json`). Before settling
  the rule, read the live distances between those four and their
  served 3-sigmas; if a piece lies inside its parent's tolerance, the
  rule needs a cap, and the report says what it is.
- The offline suite, `tools/test_gallery_cache_builder_offline.py`:
  the planted "another record" at line 1849 shifts X by 1e-5 AU, which
  the new rule may accept; re-plant it beyond any body's tolerance
  (a different body's distance, AU not km), and ADD the case the fix
  exists for: an answer shifted inside the body's own 3-sigma but
  beyond 1e-7 AU is served. The switched-off test at lines 1872-1879
  must still switch off the whole match. The refusal's new fields are
  checked in the planted case.
- The Solar System figures check needs no change in principle: the
  sentence prints exactly when no uncertainty is served, and the
  check already has the planted fault for a body JPL gives none.
  Re-run it; read the result.

AFTER THE FIX. Tony's Daily Run rebuilds the cache; its
`[UNCERTAINTY]` line should read "served for 51 of 54" with bennu,
halley and ikeya_seki the only three missing, and the live site then
prints ED138's distance to the million km with no "not yet included"
line. L-399 closes on that look, not before.

## 2. L-502 (the triad's spot): lower still

Tony's look (run record, item 8): "yes, but can we move it further
down?"

THE GEOMETRY AT HEAD, `interactive.html`: the frame HUD row
(`.sun-hud`, line 671) sits at `bottom: calc(58px + safe-area)`; the
count line (`.ss-outside`, line 712) shares that height; the drawer
button sits in `.drawer-bar` (line 760) with 12 px padding, so the
button's top is about 46 px up. The triad's bottom edge is therefore
about 12 px above the drawer button, and it is 104 by 120 px
(`.sun-triad`, line 682; its viewBox 0 0 104 120 at line 1478 scales
with the box).

"LOWER STILL" HAS THREE FORMS, and the drawer button is never covered:

- (a) Close the gap: the HUD row and the count line to about 48 px,
  one line each; 10 px gained.
- (b) Draw the triad smaller, say three quarters (78 by 90 px). Its
  TOP edge is what reaches into the thumb's zone over the scene, and
  shrinking lowers that edge by 30 px while the labels stay readable.
  The count line's `max-width: calc(50% - 72px)` (line 716) is sized
  to the triad's half width plus gaps; adjust it with the triad.
- (c) Put the triad beside the drawer button on the bottom row, left
  of the button. More to move (the button is centred by flex and
  variable in width) and only if (a) and (b) do not satisfy the look.

Build (a) and (b) together; offer (c) in the report as the next step
if Tony's thumb still finds it, not as a question. Every room (the
Sun's, Earth's, the Solar System). Check the headless walk
(`tools/headless`) and the maintenance run's Page framing and Hover
budget rows still pass; read the results. L-502 closes on Tony's
phone look, with the three far clouds' crosses he has already judged
(item 9: "i think so").

## 3. If room: the shared link that keeps the view

Ruled Oct 29, 13:07 to 13:27, in
`documentation/DESIGN_shared_view_rulings_20261029.md` (orrery, at
HEAD). Read it whole; sections 3 to 5 are the design, section 7 the
build. In one paragraph: the address carries the ticked rows by key
and the minute the room shows, written by the page itself (the rows
live as they are ticked; the minute once, when the room opens, the
maker's minute); the browser's own Share then sends the scene. Opened
from such an address, the room ticks those rows, shows that minute,
adds "as shared" under the title, and a tap on it returns to now and
clears the minute from the address. A minute outside the served
window opens at now and says so in the text box; a missing body is
named there; the Sun's and Earth's shells are listed the same way, by
their keys. Parameter names `show` and `at` are placeholders for the
build to settle: short, readable, typeable.

HOW IT IS BUILT HERE:

- Open the item first, at the next free handle, L-505 at dceb4dc6, "A
  shared link keeps the view", pointing at the design record; the
  handoff's section 5, item 6 had the records session open it, so say
  on the item that this session did instead. If the build does not
  start, do not open it.
- The address logic needs no browser to reason about, so it lives in
  its own file (Tony's ruling, L-338), say `gallery/shared_view.js`,
  with a headless check in `tools/headless` and a gating row in the
  maintenance run that can fail (a planted address that is not read
  back the same). `history.replaceState`, never a new history entry
  and never a reload.
- The minute from the address must drive the DRAWN scene, the moment
  the assembler propagates to, not only the label under the title.
  gallery-assembler fires there: confirm the room keeps one variable
  for its moment and that the address sets that one.
- interactive-exhibit gains a sentence on the address parameters at
  1.29 (the orrery session's); record the sentence on L-505 so it
  travels.
- Mode 5: Tony ticks a scene on his phone (ED138 and Pluto, his
  example), shares the link to himself, opens it on another device:
  the same bodies at the same minute, "as shared" under the title, a
  tap bringing now.

If there is no room, say so in the report; the shared link waits for
the next gallery session and nothing is opened.

## 4. Records and the report

- After each build: the gallery maintenance run offline from the
  gallery folder, read to the end; a red row is fixed or reported,
  never left for the close.
- Records per ledger-and-session-records 1.22, in the orrery folder:
  notes on L-399 and L-502 (and L-505 if opened); Where We Are's box
  rewritten (Do next: Tony's Daily Run, commit and push both folders,
  the live run, his phone looks), the road's 5c line updated, the
  marker and the zone below it untouched; the ledger's index rebuilt.
- The final report, per the gallery's CLAUDE.md: the skills read with
  their version lines; the cause found for ED138 and the rule chosen;
  every file changed with its edit count, both folders; Tony's run
  order; the Tony-action rollup. Tony pastes that report to the
  coordinating session before he commits; it checks the report against
  the folder and GitHub.
- When Tony pushes before this session closes, the coordinating
  session sends the new SHA into the session for its records (handoff
  section 1).

## 5. Tony's run order after the session (for Code to print, and for Tony)

1. Paste Code's final report to the coordinating session; wait for its
   word.
2. The Daily Run. Read its `[UNCERTAINTY]` line: 51 of 54, ED138
   served.
3. GitHub Desktop: commit and push the gallery; then the orrery (the
   orrery commit carries the Oct 28-29 handoff, this brief, your run
   record, the ledger and Where We Are).
4. The live run.
5. Phone looks: ED138's distance to the million km, no "not yet
   included" line; the triad, thumb test, in all three rooms; if
   built, the shared link: tick ED138 and Pluto, share to yourself,
   open elsewhere.
6. Send both SHAs to the coordinating session.

## 6. Tony-action rollup

- (do) Open a Claude Code session on the gallery repository
  (the python_work door: the prompt names the gallery) and paste the
  short prompt the coordinating session gives you; it points here.
- (do) Afterwards, the run order in section 5.
- (decide) Nothing; every question of the period is ruled.

Written October 29, 2026 with Anthropic's Claude Fable 5.1.
