<!-- Doc-Kind: hand | Record of L-431 build 3 (the website prints each body's orbital period from JPL, and draws an orbit around its period's centre) built with L-395's move (the Horizons check now runs in the orrery's maintenance run and checks the period too). Built and tested in the sandbox; the run order for Tony, with what each step prints; the one decision; where the loose ends went. -->
# L-431 build 3, the website, with the Horizons check's move (L-395)

Built on orrery 5cd63ccea16e5242014f8aeb12cfb4beeb36ea31 at
https://github.com/tonylquintanilla/palomas_orrery ("L431") and
gallery 77988635526d1dd68f8c082cae39f4b7ad3f56b8 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (your Daily
Run of October 14, then the gallery patch's first copy added in the
root, unrun). First built on orrery db63721d and gallery 924977a3; both
moved during the session (the dashboard labels, L-440; your Daily Run
of October 14; then patch_L269_6), the orrery patch refused twice on
your machine, writing nothing each time, and the build was rebuilt on
the new HEADs each time.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.

- Type: BUILD. Three patches, run in this order:
  `patch_L431_11_website_orrery_20261014.py` (orrery),
  `patch_L431_12_website_gallery_20261014.py` (gallery) and
  `patch_L431_13_dashboard_buttons_20261014.py` (orrery again). This
  record is created by the first.
- Why three: L-440's Dashboard Parity check, in the orrery's maintenance
  run, reads the gallery folder beside the orrery and holds every run
  step to a dashboard button. The dashboard is in the orrery; the
  website's Horizons scripts leave in the gallery patch. So the
  website's buttons can only move after it, in a small third patch.
- Companion: the brief, `documentation/HANDOFF_L431_build3_website_brief_20261013.md`,
  read with `documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md`.
- Skills loaded at session start, each confirmed against the manifest at
  db63721d: horizons-orbital-mechanics 1.5 and provenance-discipline 2.29
  (both bumped on October 13; this was the first session able to check
  them, and both matched), orrery-coding-conventions 1.10,
  safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.20, gallery-assembler 1.3,
  gallery-cache-builder 1.8, interactive-exhibit 1.14.

## 1. What you get

- Every body in the Solar System room, and Earth in the Earth room's Sun
  Direction, has a line in its hover giving its orbital period. One of
  three forms:
  - "Orbital period: 0.240846 years (87.969 days), around the Sun, from
    JPL Horizons, fetched 2026-10-13." (Mercury, Jupiter, Encke today)
  - "Orbital period: 1.8808 years (686.98 days). Typed value, not
    fetched from JPL." (the eight bodies the orrery has not yet fetched)
  - "Orbital period: not yet fetched from JPL." (the Pluto-Charon
    barycentre; see section 2)
  The digits are the orrery's, counted by the orrery's rule and carried
  in its export. The website never recounts them.
- An orbit whose period is taken around the solar system's barycentre
  is drawn around the barycentre, moved to where it sits seen from the
  Sun, with no perturbation lines, as the orrery draws Sedna. No body the
  website serves today has such a period, so nothing changes on screen
  for this yet; it is built and tested on Sedna's real numbers.
- The Horizons check runs in the orrery's maintenance run now, just
  before the objects export. It still asks JPL only what is due. It now
  also checks each fetched period against JPL's own, and re-reads the 26
  spacecraft data sheets every 30 days. The website's Daily Run is three
  steps: guest book, cache builder, maintenance run.
- The website keeps one offline check, "Horizons confirmations". It
  reads the dates from the orrery's export and goes red, naming the
  objects, on the day one turns 30 days old.

## 2. The one decision

The Pluto-Charon barycentre has no period from JPL to show. The orrery
fetches elements for Pluto, and for Pluto around the barycentre, but
never for the barycentre itself around the Sun. So its row on the
website says "Orbital period: not yet fetched from JPL."

- Recommended: ship it that way now. Teaching the orrery to fetch the
  barycentre's own elements is orrery plotting work, outside this
  build; it is recorded on L-433 (the road) for the objects work.
- The other way: hold build 3 until the orrery fetches it.

Your answer changes nothing in the patches; it decides whether the look
accepts that row.

## 3. Run order, and what each step prints

Before you start (do): if you want the website to show JPL's periods
for Venus, Earth, Mars, Saturn, Uranus, Neptune, Apophis and Halley
instead of the typed values, plot each once in the orrery and answer
yes to Update Orbital Elements. This is optional; the build is correct
either way, and you can do it any later day. If you do it, the next
maintenance run asks JPL about each new period.

Orrery folder:

1. Save the new `patch_L431_11_website_orrery_20261014.py` in the
   orrery folder, replacing the copy that refused (and the new
   `patch_L431_13_dashboard_buttons_20261014.py` beside it, for step 7),
   and press Run. It
   prints 79 "ok" lines for the edits and 7 for the new files, then:
   `patch applied (79 edits in 14 files, 7 files created)`
   A second run prints "ERROR: horizons_check.py already exists; this
   patch has run. NOTHING was written."
2. Run `orrery_maintenance_run.py`. It needs the internet today: the
   Horizons check asks JPL about three periods never confirmed. Expect:
   - "Horizons check ... PASS -- 3 checked today, 3 queries"
   - "Objects export ... rewrote data/objects_export.json"
   - "Skill manifest" rewrites PROJECT_INSTRUCTIONS.md (the three new
     skill versions) and "Ledger index" rewrites the ledger's index
   - "Dashboard parity ... PASS"
   - "30 of 30 gating checkers passed", and the provenance scanner's
     "0 TIER-1 -- the push gate holds"
   If "Horizons check" says UNREACHABLE, JPL could not be reached:
   "Horizons confirmations" is then red too. Run it again later; do
   not push until it passes. If it says FAIL, it names the body and
   JPL's figure: stop, and bring it to a session.
3. Move the patch script into `documentation/`, and
   `patch_L431_10_brief_both_sets_20261013.py` too if it is still in
   the root folder. Commit and push.

Gallery folder:

4. Run `tools/pull_objects_export.py`. It prints "Pulled objects from
   orrery <your new SHA>: 13 (...)".
5. Save `patch_L431_12_website_gallery_20261014.py` in the gallery
   folder and press Run. It prints 81 "ok" lines for edits, one
   "created", four "removed (now in the orrery)", then:
   `patch applied (81 edits in 18 files, 1 file created, 4 removed)`
   If you run it before step 4 it says the export "is schema 1, from
   before the orrery patch" and writes nothing.
6. Run `gallery_maintenance_run.py` (offline). Its Objects mirror
   rewrites `data/objects_config.json` with each object's period.
   Expect "27 of 27 gating checkers passed", with "Drawn orbit" and
   "Horizons confirmations" among them. Don't commit the gallery yet.

Orrery folder again:

7. Save `patch_L431_13_dashboard_buttons_20261014.py` in the orrery
   folder and press Run. It prints 10 "ok" lines, then
   `patch applied (10 edits in 1 file)`. Run before the gallery patch,
   it says "the gallery patch has not run yet" and writes nothing.
8. Run `orrery_maintenance_run.py`. Expect "Dashboard parity ... PASS"
   and "30 of 30 gating checkers passed". (Between steps 5 and 7,
   Dashboard parity is red, naming the two Horizons buttons and Drawn
   Orbit. That is expected; step 7 is the cure.) Move the script into
   `documentation/`. Commit and push the orrery.

Gallery folder again:

9. Run the Daily Run: the guest book, the cache builder, the
   maintenance run again.
10. Move the gallery patch into `documentation/`. Commit the config and
   the cache together, and push. Then run
   `python gallery_maintenance_run.py --live`.
11. The look (decide), on the phone and the desktop: in the Solar
   System room, hover Mercury and Jupiter (JPL's period, around the
   Sun), Mars (typed, marked) and Pluto (not yet fetched). In the Earth
   room, hover the Sun Direction: Earth's period. Encke and Halley are
   not rows in that room's list, so their periods show only once they
   are; the Moon has no key in the orrery's list, so it gets no period
   (section 6). The Sun room prints no period: the Sun has none.
    The dashboard (step 7's patch): the website group no longer shows
    Horizons Check or Horizons Check Suite; the Maintenance Run group
    shows Horizons Check, Horizons Check Suite and Horizons
    Confirmations; Drawn Orbit sits under the served cache.

## 4. What reaches a visitor, and when

- The period lines reach a visitor on the push alone. The rooms read
  the period from `data/objects_config.json`, as they read a body's
  description and link. (The brief said the cache rebuild was needed;
  that holds only for the drawn orbit below.)
- An orbit drawn around the barycentre is cache data ("drawn_orbit"),
  so it needs the builder. "Cache in step" fails until the builder has
  run, and the room's warnings say so.
- A body whose period changes kind (typed to fetched, after you plot it
  in the orrery) reaches the website after the orrery's maintenance
  run, its push, and the gallery's maintenance run and push.

## 5. What was tested here, and what was not

Tested in the sandbox, each patch on a throwaway copy of its repo at
its pinned SHA:

- Each patch applied cleanly, wrote every file exactly as built, and
  refused on a second run. The gallery patch refused before the orrery
  export was schema 2.
- The orrery maintenance run, offline: every checker passed except
  "Horizons confirmations", which needs JPL that day and read
  UNREACHABLE, as it should. The Horizons check then ran on recorded
  answers as if online: "HORIZONS CHECK: PASS -- 3 checked today, 3
  queries". Then the maintenance run again: "30 of 30 gating checkers
  passed". Be clear what that proves: the identity answers are JPL's
  own, but the three elements answers (the periods) and the data-sheet
  answers were written by this session in JPL's format, from the
  orrery's own fetched numbers, because the sandbox cannot reach JPL.
  So the check's reading of a real JPL period answer is first tested by
  your step 2.
- The gallery maintenance run on that export: 27 of 27, and the config
  the mirror wrote matched the build's byte for byte.
- With both folders side by side, as on your machine: Dashboard parity
  passed after the orrery patch, went red after the gallery patch,
  naming exactly the two Horizons buttons and Drawn Orbit, and passed
  again after the third patch ("79 steps matched to their buttons by
  name and script; 109 cards carry a short line"); then 30 of 30.
- The three rooms' drivers ran in plain Python on the served cache, and
  the page booted headless on each with no errors; the hovers above are
  what it printed.
- The five planted faults the brief asked for, each caught: an export
  period with no centre; a mirror that drops the centre; a hover
  printing more figures than the export's count; a barycentre orbit
  drawn around the Sun; a Horizons check passing a period JPL
  disagrees with.

A cold review by a separate agent, after the build, found two faults,
both fixed and retested before delivery: Encke's period query sent its
';' bare where JPL's own examples send %3B; and the website's check,
red at day 30, would have gone red every cycle, because the orrery
asked JPL again only at day 30 and the website sees the new date only
after the push and the pull. The orrery now asks again from day 25.

Not tested here: anything that reaches JPL live (the sandbox cannot),
the cache builder's live fetch of a "drawn_orbit" (no served body
needs one yet), and what the rooms look like. Your step 2 is the live
test of the check; your look is the test of the words.

## 6. Found while building, and where it went

- Loose ends of L-431 and L-395, re-homed to L-433 (the road), in its
  note of 2026-10-14, for the work that brings the rest of the
  orrery's objects to the website: the served objects with no key in
  the orrery's list (moon, io, titan, pluto, charon, voyager_1) get no
  period and no Horizons check; the Pluto-Charon barycentre's own
  period; the fields the list lacks; the display-name rename; MAPS and
  3I/ATLAS checked live once served; and whether the identity check
  widens past the keyed entries (default no).
- The objects-to-website brief names its item L-438. The dashboard
  session took L-440 and the ledger now lists L-438 and L-439 as
  retired, so the objects work opens under the next free handle (on
  L-433's note).
- The "Tier-1 rise: NOT READ" line your run printed was L-269's; its
  session fixed it in patch_L269_6 (Windows line endings), which this
  build now sits on.
- The orrery's export now serves typed periods, from
  `KNOWN_ORBITAL_PERIODS`. The website marks every one as typed, and the
  provenance scanner already names the table. Its 132 unsourced entries
  stay one class, as L-431 recorded; struck as a loose end of L-431.
- The skill horizons-orbital-mechanics grew past one read with this
  version, so it now opens with its read plan (L-418's rule).

## 7. The ledger and the skills

- L-431 and L-395 are PENDING-GATE: built, each waiting only on your
  run and look. When you accept, a session sets each to DONE; nothing
  else changes.
- Skills: horizons-orbital-mechanics 1.6, gallery-cache-builder 1.9,
  interactive-exhibit 1.15; protocol v3.96. A reinstall made during a
  session is not visible to that session, so the NEXT session confirms
  its loaded copies read those three versions before work that fires
  them.

## 8. Your actions, all of them

- (do) Optional, any day: plot the eight typed bodies in the orrery
  and answer yes to Update Orbital Elements (section 3).
- (do) Steps 1 to 10 of section 3, in order.
- (do) Reinstall the three skills from `skills/` (Settings > Skills):
  horizons-orbital-mechanics, gallery-cache-builder,
  interactive-exhibit.
- (decide) The Pluto-Charon barycentre's row (section 2).
- (decide) The look (step 11).

Session written October 2026 with Anthropic's Claude Opus 5.5.
