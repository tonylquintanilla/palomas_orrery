<!-- Doc-Kind: hand | Brief for the next session: slice 2's website half (build B), with the evening's rulings of Oct 24 it builds by and the questions it asks first. -->
# Brief: slice 2's website half (build B)

Tony Quintanilla, PE | Claude Opus 5.5 | October 24, 2026, close of the night

Built on orrery 0b93a25830be3723f9279aaa7b60e6f9e7b21bfa at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b1a4ce6c7fc72b17571a13e18ab11df98b86485b at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main), both read with git ls-remote at this close. The close patch
(patch_L443_11_session_close_20261024.py) adds this brief.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a BUILD session. Companion to:
`DESIGN_L443_slice2_rulings_20261023.md` (slice 2's design),
`HANDOFF_L443_slice2_buildA_20261024.md` (build A, the path plan),
`COORD_L443_comet_span_ruling_20261024.md` and
`COORD_L443_words_decisions_20261024.md` (the evening's rulings),
`WORDS_L443_slice2_draft_20261024.md` and
`CHECK_L443_slice2_sources_20261024.md` (the words and their reads), and
Tony's run record `WHERE_WE_ARE_10-24-26_1927_run_record.md`. Supersedes
nothing.

## 0. Before anything

- git ls-remote both repos: the orrery at or past 0b93a25 with this
  close patch pushed, the gallery at or past b1a4ce6. If the orrery
  still sits at 0b93a25, the close patch has not run; stop and say so.
- Confirm the loaded interactive-exhibit reads 1.23 and
  horizons-orbital-mechanics reads 1.10 before work that fires them
  (protocol v3.111's obligation). The session that bumped them loaded
  1.22 and 1.9.
- Read, in order: `documentation/WHERE_WE_ARE.md`, this brief, the run
  record above (its last third holds the preview's report), then the
  design record.

## 1. Where slice 2 stands

- **Build A is done and checked on JPL's real data.** `path_plan.py`
  planned the twelve spacecraft by name (the dashboard's preview, Tony's
  run of 20:44 to about 21:12): 12 paths, 498 events, written to
  `data/path_plans_preview.json`, which the export never reads. The
  flybys spot-checked land on the dates of the missions' known flybys
  (Voyager 1 at Jupiter and Saturn, Voyager 2 at Saturn, Uranus and
  Neptune, New Horizons at Pluto, Juno's, Lucy's, JUICE's, Psyche's,
  Clipper's and BepiColombo's Earth, Moon, Venus and Mars passes). That
  check was against the missions' dates as Claude knows them; the
  numbers are JPL's. Since patch_L443_10 it prints as it goes, saves
  each plan as it is made, and keeps to a 10-minute limit unless
  --no-limit.
- **Owed before anything is served:** OSIRIS-APEX's Earth pass at
  7,526 km on 2029-04-13, the day Apophis passes Earth, is not one
  Claude recognised. Check it against JPL's data sheet for -64.
- **C/2025 K1 is fixed in the orrery** (asked as DES=1004075;) and
  Tony's look confirmed it (L-470).

## 2. What build B does

By the design record, with these rulings since:

1. **Key the twelve spacecraft with their website entries,** in the
   same round (the website's objects mirror refuses a key with no
   entry), with the words of `WORDS_L443_slice2_draft_20261024.md` as
   ruled: BepiColombo's description carries no date; Juno is drawn to
   where JPL's data ends, 2028-09-02, solid to today and dashed after,
   and its description says nothing about the mission's end. The
   preview list, its flag and its dashboard button come out.
2. **The orbiter rule** (ruled this evening; L-443): in each body's
   daily series, a stretch of days inside the body's Hill sphere with
   one nearest approach is a flyby, as now. A stretch with more than
   one is a capture: its first nearest approach (the arrival) is an
   event, and its last before the spacecraft leaves is an event; the
   approaches between are not events, and in the Solar System room the
   spacecraft rides with the body there. A stretch that runs to the end
   of JPL's data is an arrival with no departure (a landing, or a
   mission's end). The loops wait for that body's room. Passes of the
   Sun are not captures (it has no Hill-sphere gate) and stay events,
   Parker's 42 among them. Built into `path_plan.py` with its suite,
   then the preview run again so Tony sees the counts fall.
3. **The builder fetches each path by its plan;** the Solar System room
   draws each path solid to today, dashed after; the hover words go to
   Tony first.
4. **L-461 with it:** when the Daily Run's pull and Tony's push
   differ, does it stop, or wait and try again? Ask Tony.
5. **Then the open-path comets,** by the span ruling: a year before
   perihelion to a year past today, both ends clipped to what JPL
   serves; "hyperbolic" with plain words for what it means.

## 3. Asked first, one at a time

1. **Their own room, or the Solar System room?** Tony, 2026-10-24,
   22:26: "build 3 would implement the spacecraft and hyperbolic comets
   and interstellar objects? Perhaps those should go in their own room?"
   The design so far puts them in the Solar System room (Settled, Oct
   22: "Open-path comets go with the spacecraft"), where the planets
   already give their paths a frame. A room of their own would have to
   draw the planets again. Put it to Tony with that trade-off before
   building.
2. **The drawer's order.** Tony, the same message: "i would suggest
   putting the spacecraft drawer after earth's as the comets are after
   the sun's." Read as: a Spacecraft group row right after Earth's row
   (before Near-Earth asteroids), as the Comets group follows the Sun.
   Confirm the reading, then build it.
3. L-461, stop or wait (section 2).

## 4. Method to write into the skills at their next versions

- horizons-orbital-mechanics: a comet whose designation also matches
  its own pieces is asked by JPL's permanent number for it; the
  orrery's path cache, keyed by name, does not notice a new record;
  the orbiter rule (section 2); a long JPL run prints as it goes, saves
  as it goes, and keeps under the maintenance run's 15 minutes.
- interactive-exhibit: L-484's rule, the website and the orrery agree
  on every object both draw, or the difference is documented.
- safe-file-editing: L-471's three rules.

## 5. Deferred, recorded tonight

- L-485 (a nightly run): the maintenance routines run unattended at
  night; committing and pushing stay Tony's.
- L-486 (a view carried into a room).
- L-483 (a comet room for C/2025 K1 and its pieces), after slice 2.

Written October 24, 2026 with Anthropic's Claude Opus 5.5.
