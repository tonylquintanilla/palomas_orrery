<!-- Doc-Kind: hand | Brief for the orrery Claude Code session of Oct 29-30, 2026: L-504 (the orrery's clock) first slice, the data path; with it the belt's kilometres in the export, Pluto's words, the n.a. sentence, four skill bumps and the protocol entry, and the closures of L-399 and L-502. Written by the coordinating session; zero code. -->
# Brief: the orrery session (L-504's first slice, and the small builds)

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 29, 2026, 20:50

Built on orrery 47edd731b7aeb01b6ffafe2fc00ffcd4b9848b1a at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b55109f228f37b38f248c6359298783889f992af at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both read live with git ls-remote on Oct 29, 20:20, after
Tony's pushes of 19:51 and 19:52. Every line number below was read
from those two commits.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a build session in the ORRERY repository, item 2 of
`HANDOFF_coordination_20261028_29.md`, section 5, with tonight's
findings folded in. The session reads this file and that handoff
before anything else; Where We Are's "Do next" line at HEAD names
Tony's steps of Oct 29 evening, all done, so this brief is the job.

## 0. The base, and what is waiting

- Orrery: 47edd731, clean. Tony's run record for this session,
  `documentation/WHERE_WE_ARE_10-29-26_<hhmm>_run_record.md`, appears
  when he copies the page at your first run order; that one is
  expected, and this brief once he has it in the folder. Anything else
  waiting is not.
- Gallery (the sibling folder): b55109f2, clean. Read, never written,
  from this session.
- Skills this job fires, each read in full before the work, versions
  stated in the first report against the manifest in
  PROJECT_INSTRUCTIONS.md v3.117: horizons-orbital-mechanics 1.12,
  orrery-coding-conventions 1.12, provenance-discipline 2.35,
  safe-file-editing 1.14, agentic-pre-test 1.3,
  ledger-and-session-records 1.22; and, for the bumps in section 5,
  interactive-exhibit 1.28 and gallery-cache-builder 1.13.
- Order of work: section 1 (the clock) is why the session exists and
  goes first; then sections 2 to 4, small; then section 5 (skills and
  the protocol); then the records. If the session runs out of room,
  section 5 is what moves to the next orrery session, and the report
  says so plainly.
- The session asks Tony ONE question in all; this brief leaves none
  open. Two things it should TELL him, because they change what he
  sees (section 1, "What Tony will notice").

## 1. L-504 (the orrery's clock): the first slice, the data path

THE RULING (Tony, Oct 28, 23:50): "we should standardize on utc." The
epochs asked of JPL stay at TDB midnight on purpose (Oct 29 morning);
this item fixes only the local-clock readings taken as UTC.

THE FINDING, on the item: the orrery reads the computer's clock with
no time zone (`datetime.now()`, `date.today()`) and treats the reading
as UTC when `orbit_data_manager.utc_to_tdb` (line 51) converts it for
JPL, so a "now" it asks for is off by Chicago's 5 or 6 hours; and the
orbit cache's "fetched" stamps (`osculating_cache_manager.py` lines
455 and 612) are local time with no zone, while the website's are UTC.

THE SLICE: the 49 readings in the ten data-path modules named on
L-504 (palomas_orrery.py 17, orbit_data_manager.py 12,
idealized_orbits.py 7, osculating_cache_manager.py 5, path_plan.py 2,
orbital_period.py 2, period_fetch.py 1, horizons_check.py 1,
close_approach_data.py 1, palomas_orrery_dashboard.py 1). Re-count at
47edd731 before editing; the count is the item's, not this brief's.

HOW, the shape the coordinating session expects (method; the session
settles the details and says so):

- One reading, one place. A small helper the ten modules import (a
  `utc_now()` and a `utc_today()`, in a module that already sits under
  all ten with no imports of its own, or a new tiny one), returning
  timezone-aware UTC. The later slices (the Earth System fetches, the
  report stamps, the tools) import the same one. Grep each module for
  every reading, map which ones feed the TDB conversion, which ones
  are stamps, and which ones set what the GUI shows, before editing
  any of them (Verify Execution, Not Appearance).
- A stamp says its zone. New "fetched" stamps are UTC and say so
  (ISO text ending in "+00:00" or "Z"). The cache's readers (line 315's
  `fetched_str` and whatever else parses a stamp) must read BOTH the
  old zoneless stamps already in `data/osculating_cache.json` and the
  new ones; a refresh rule counted in days is not harmed by a few hours
  either way, but the reader must not crash on either form, and a
  planted old-form stamp is in the test.
- What the GUI shows. Every date the orrery prints or defaults to is
  UTC and says "UTC" where a date is shown (the date fields' default
  "now", the plot's date line, the hover's "fetched" line). Where a
  label has no room, the tooltip says it.
- Tests: `test_position_digits.py`, `test_orbit_markers.py`, the
  Horizons check (`horizons_check.py`) and the period fetch
  (`period_fetch.py`) run and are read to the end; the dashboard's
  parity check; the agentic pre-test on a throwaway copy for every
  module delivered whole. Tier-1 = 0 on the active build path before
  Tony pushes (provenance-discipline): a new helper's docstring and
  any "UTC" in a display string are scanned.

ASTROQUERY'S SAVED ANSWERS, received on L-504 from L-399 tonight. The
library the orrery uses to ask JPL keeps every answer on disk for a
week and hands it back when the same question is asked again
(`astroquery.cache_conf.cache_timeout`, 604800 s). The website's
builder found this out the hard way on Oct 29 (JPL revised 2026
ED138's orbit between two runs; the second run was answered from the
first run's saved copy) and now asks fresh everywhere through one
switch, `HORIZONS_CACHE = False` (gallery
`tools/gallery_cache_builder.py` line 413). The orrery's own calls
pass no `cache=` at all: `orbit_data_manager.py` lines 695 and 1810,
`close_approach_data.py` 573, `orbital_period.py` 318,
`palomas_orrery.py` 1392, 1950 and 1956, and the 2xr request in
`position_accuracy.py`, which goes to JPL directly and is already
fresh. The recommendation, to confirm or correct in the report: the
orrery's own caches (the osculating cache, the orbit cache) are the
only caches, so a record that says "fetched" today was fetched today;
the same one switch, `cache=False` passed at every call in the slice,
with a comment at the switch saying why. The cost is a JPL round trip
on a repeated plot, which the orrery's own cache already absorbs for
orbits.

WHAT TONY WILL NOTICE, to say in the report before he runs anything:

- In the evening the orrery's default date becomes TOMORROW's date.
  At 8 pm in Chicago it is already 1 am UTC the next day; the website
  showed "30 Oct 2026, 01:10 UTC" in his look tonight, and the orrery
  will now agree with it instead of saying Oct 29.
- A "now" plot shifts by five hours of motion. The Moon moves about
  2,700 km an hour, so its "now" position moves about 13,000 km; Earth
  about 540,000 km; a comet near perihelion more. The hover's
  distances print to JPL's uncertainty, so most will not change in the
  digits shown, but a body's dot can move a little from where the old
  "now" put it. That is the fix working, not a fault.

## 2. The belt's kilometres in the export (L-503, L-484)

`export_constants.py` serves the belt's three distance and latitude
tables (the nine MAIN_BELT_* rows) rounded to their declared figures
and with no "in" kilometres, while a length row carries "in" (line
428, `converted`). The website prints the belt's distances in AU alone
for that reason (L-503's documented difference on L-484). The job:
each table entry carries its "in" kilometres from the store's full
digits, the way a length row does, so the website can print "1.67 AU
(about 250 million km)" as the orrery does. Read the gallery's
`tools/mirror_constants.py` (read only) to confirm a new field on a
table entry is ignored by the mirror until the website asks for it;
the website's half, printing them, is the next gallery session's.
Tony's Daily Run tomorrow pulls the export; the pulls' PASS lines
will name `data/constants_export.json` as changed.

## 3. Pluto's words, and the ninefold jump (L-484)

- The question first (Discovery over Delivery). The orrery's Pluto
  hover prints Pluto's own period around the Sun from the orbit cache,
  "250 years (92,000 days)", rounded by a 589-day yearly change; the
  fetch of Oct 28, 14:57 read 91,491 days with a 66-day change, the
  one at 23:19 read 91,623 days with 589. Find out why the yearly
  change jumped ninefold in nine hours (`osculating_cache_manager.py`
  line 491 prints it; read how `year_change_days` is made). One
  hypothesis to test, not to assume: the record is Pluto's BODY, which
  circles the Pluto-Charon centre of mass every 6.4 days, so its
  osculating elements around the Sun swing with Charon, and a change
  measured between two fetches depends on where in that 6.4-day swing
  each fetch fell; the website's Pluto is the barycentre's (90,578
  days, 247.990 years), which does not swing. If that is it, the
  yearly change is not a yearly change for Pluto's body, and the
  rounding rule needs the swing's size, not the difference of two
  fetches.
- Then the words: the orrery's Pluto hover says, in plain words, why
  its period differs from the website's (the body against the
  barycentre, Charon's pull), from the sourced numbers, nothing typed.
- Pluto's checkbox gains a tooltip (`palomas_orrery.py` line 9677 is
  where its shells are built; find its checkbox), and the barycentre's
  tooltip gains hover words. orrery-coding-conventions fires for both.
- Record what was found on L-484, and the rounding rule's fate on the
  item that owns it.

## 4. The n.a. sentence (L-399, L-484)

In `position_accuracy.py`, `_side` (line 337's small_body branch) a
small body whose 2xr row came back with "n.a." in the uncertainty
column (Bennu, Halley and Ikeya-Seki tonight) and one whose
uncertainty was never fetched both return `_none_side(name,
'not_fetched')`, so the hover says "JPL's uncertainty for this position
is not included here" when the truth is that JPL states none. The
module already has the true sentence, `_gap`'s `unstated` branch, "JPL
states no accuracy for this position". The job: when `sig` is present
and `range_3sigma_km` is None, return `_none_side(name, 'unstated')`;
a case in `test_position_digits.py` for each of the two reasons,
shown able to fail. Record on L-484 that the website's sentence, "JPL's
own uncertainty for this position is not yet included", has the same
slant for the same three bodies, and that the two instruments print a
distance with no uncertainty to different digits (the orrery the whole
kilometre, its stated floor; the website the tens): both for the next
gallery session, the digits as a method question for the skill, not
a ruling.

IF ROOM: ask Horizons once each, with OBJ_DATA on, for 2026 ED138,
Bennu, Halley and Ikeya-Seki, and record on L-399's closing note what
JPL says of each solution (its date, the observations behind it, and
whether it carries a covariance), fetched, not recalled. That answers
Tony's question of tonight, why the three have no figure, with JPL's
own words.

## 5. Four skills, one bump each, and the protocol's entry

One Session, One Bump. Each skill's oldest of four version entries
moves to `documentation/SKILL_HISTORIES.md`; `skills_index.py` rebuilds
the manifest; the protocol gets v3.118 with its header stamp and SHA
anchor, v3.115 moving down to PROJECT_INSTRUCTIONS_HISTORY.md PART 1;
the entry carries the obligation that the next session loading skills
from the account confirms the four new versions. Every sentence
written is read from the code at 47edd731 and b55109f2 first.

- interactive-exhibit 1.28 -> 1.29: the six corrections listed on
  L-503 ("For interactive-exhibit's next version"); and from tonight,
  the anatomy's frame HUD row: the triad at three quarters (78 by 90
  px), the HUD row and the count line at 48 px, the count line's
  width `calc(50% - 59px)` (gallery `interactive.html` lines 683, 699,
  731, 733). No sentence on the shared link's address yet; it is not
  built.
- gallery-cache-builder 1.13 -> 1.14: the builder serves
  `position_uncertainty` on each small body's record; `serve_drawings`
  reads a room's own rows (L-503); every JPL question asks fresh
  through `HORIZONS_CACHE` and why; the match rule (the body's own
  3-sigma, floored at 1e-7 AU, capped at 1e-3 AU, the cap set by the
  closest comet pieces); a refusal names its numbers (L-399, read from
  the builder at b55109f2).
- horizons-orbital-mechanics 1.12 -> 1.13: the website's 2xr is a
  second question held to the served point within the body's own
  uncertainty; astroquery's saved answers and what each instrument
  does about them (section 1); the n.a. case prints "states no
  accuracy" (section 4); the clock helper, if section 1 made one.
- provenance-discipline 2.35 -> 2.36: A Computed Position Prints What
  Its Errors Earn no longer says the asteroids wait for L-399; a
  sentence that says why a figure is missing says the true reason (not
  fetched, or stated as none).
- ledger-and-session-records stays at 1.22: its next version is the
  records session's (handoff section 5, item 6).

## 6. Records

- Close L-399 (each small body's own uncertainty) and L-502 (the
  triad's spot) on Tony's phone look of Oct 29, 20:11 (his run record,
  "Correct", with two screenshots): ED138 printed to the hundred-
  thousand km, 47.225 AU (7,064,700,000 km), by JPL's revised 80,903
  km, with no "not yet included" line; the triad small and low in the
  Solar System and Earth rooms. A Closing Item Re-homes Its Loose
  Ends: L-502's three pre-existing walk failures
  (`tools/headless/walk_solar_system_drawer.js`, 168 of 171) go to the
  item that owns the website's checks, and the closing note says
  which.
- L-503 (the belt on the website): Tony's look passed (run record item
  11, "yes, see upload"); it stays open for the kilometres, this
  session's export half done, the website's printing next.
- L-504: this slice, the helper, the stamps' two forms, the saved
  answers' decision, the later slices' counts unchanged.
- L-484: sections 3 and 4.
- Where We Are: the box rewritten (Do next: Tony's push, the four
  skills reinstalled, the Daily Run tomorrow); the road's 5d line
  marked by what this slice did and what the later slices are; the
  marker and the zone below it untouched; the ledger's index rebuilt.
- The final report, per the orrery's CLAUDE.md: the skills read with
  their version lines; the two things Tony will notice (section 1);
  what the Pluto question found; every file changed with its edit
  count; Tony's run order; the Tony-action rollup. Tony pastes that
  report to the coordinating session before he commits.

## 7. Tony's run order after the session (for Code to print, and for Tony)

1. Paste Code's final report to the coordinating session; wait for its
   word.
2. Run the orrery once from VS Code's Run button: the date fields
   should open on today's UTC date (tomorrow's, in the evening), say
   UTC, and a plot of Earth and the Moon should draw.
3. GitHub Desktop: commit and push the orrery (the commit carries this
   brief and your run record).
4. Settings > Skills: reinstall the four bumped skills
   (interactive-exhibit 1.29, gallery-cache-builder 1.14,
   horizons-orbital-mechanics 1.13, provenance-discipline 2.36).
5. Tomorrow's Daily Run pulls the export with the belt's kilometres;
   its pulls should name `data/constants_export.json` as changed and
   every checker stay green. Commit and push the gallery after it.
6. Send the orrery's SHA to the coordinating session tonight, the
   gallery's tomorrow.

## 8. Tony-action rollup

- (do) Open a Claude Code session on the orrery repository (the
  python_work door: the prompt names the orrery) and paste the short
  prompt the coordinating session gives you; it points here.
- (do) Afterwards, the run order in section 7.
- (decide) Nothing; every question is ruled or is the skill's.

Written October 29, 2026 with Anthropic's Claude Fable 5.1.
