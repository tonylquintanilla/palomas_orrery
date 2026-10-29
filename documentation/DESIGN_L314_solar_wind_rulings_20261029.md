<!-- Doc-Kind: design | Rulings from the design talk of October 29, 2026 on L-314 (live solar wind for the magnetosphere shells): where the fetch lives, its cadence, the storm level in the hover, and the change in the order of work that puts the nightly run (L-485) next. Zero code. -->
# Design talk: L-314, live solar wind for the magnetosphere shells

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 29, 2026, 13:35 to 14:10

Built on orrery b3bfab02 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 963500ca at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both read live with git ls-remote on Oct 29, 14:10. The gallery
Code session of Oct 29 (L-399, L-502, L-503) was running during the
talk and did not touch any file this record names.

Type: DESIGN RECORD (zero code). Earth's list (L-413), design talk 4.
The talk ran from Tony's phone. It closes the design of L-314; the
build waits on L-485 (a nightly run), by the order ruled in section 5.

## 1. What was already ruled, and stands (Sept 12 and Oct 16, 2026)

Read from L-314 before the talk; one sentence each, so this record is
complete on its own:
- The visitor's browser never fetches NOAA; a build step does, on a
  schedule.
- A nightly spot value is the wrong sampler. The step takes the last
  24 hours of NOAA's series and stores the low, high and mean of the
  dynamic pressure, Bz and speed, and of the two derived standoffs
  (the magnetopause nose by Shue 1998, the bow shock nose by Jelinek
  2012). The shells draw at the mean; the hover carries the band and
  the time span it was measured over.
- A compression is never attributed to a coronal mass ejection; only
  what is measured and published is said.
- A value outside a model's stated range (Jelinek 0.6 to 11 nPa;
  Shue's Bz range, from L-305's read) draws at the range edge and says
  so.
- A failed fetch keeps the last good day, dated, and never falls back
  silently to the declared 2 nPa, 0 nT, 400 km/s.
- The aberration (the nose turned toward Earth's orbital motion by
  atan(v_orbit / v_sw), about 4 degrees) is applied from the measured
  speed once the fetch exists; until then both instruments draw along
  the Sun-Earth line and say so (built Oct 17).

Confirmed in the talk, read live Oct 29: NOAA's directory
https://services.swpc.noaa.gov/products/solar-wind lists plasma and
magnetic-field files at five cadences (5-minute, 2-hour, 6-hour,
1-day, 3-day, 7-day). The files' field names were not read (the
reader was refused) and stay "recalled, to confirm when the step first
reads them", as L-314 already says.

## 2. The rulings of Oct 29, in order, Tony's words quoted

1. **Fetch once, serve twice: the orrery fetches, the website pulls
   (option C).** Offered A (the website's builder fetches; the orrery
   keeps the declared conditions and says so) and B (both instruments
   fetch, website first). Tony, 13:50: "Shouldn't we fetch once and
   serve twice? Or would the orrery fetch be 'now'. Cadence matters
   too." Then, 13:56: "Option C."
   The fetch is one step in the orrery's maintenance run. It reads
   NOAA's last 24 hours, writes one file with the low, high and mean
   of pressure, Bz and speed, the two derived standoffs, the storm
   level (ruling 3), and the time span measured, all UTC. The
   website's Daily Run pulls that file the way it pulls the drawings.
   Both instruments draw from the same stored day and print the same
   numbers with the same stamp.
   This revises the Sept 12 line that put the fetch in the website's
   builder "because it already fetches nightly": since Oct 25 (L-485)
   the orrery's checks will run nightly too, so the reason is gone,
   and the one-way flow (the orrery the source, the website pulling)
   is kept for this number as for every other.

2. **Cadence: nightly, stamped; the orrery reads the stored day too.**
   Every hover says "the solar wind as measured over the 24 hours
   ending <time> UTC". At most a day old on the website, which is the
   honest cost of a site with no live connection. The orrery reads the
   same stored day; a re-fetch at plot time when the stored day is
   older than 24 hours was offered and set aside: "start with the
   stored day for both and add the re-fetch only if you find yourself
   wanting it." Tony: "Option C" covered both.

3. **The storm level rides in the hover.** NOAA publishes the Kp index
   and its G-scale (G1 minor to G5 extreme), measured and published,
   so the hover may carry it. Tony, 14:03: "Yes G3 measured." The
   magnetosphere hovers show the day's storm level beside the
   pressure, Bz and speed; the words are "measured", never a cause.

4. **The order of work changes: the nightly run (L-485) goes next.**
   Tony, 14:03: "When are we planning L[4]85? The reason I'm asking is
   that would standardize the cache build time for visitors and also
   keep the website live when I can't." And 14:10: "Confirmed." The
   order is in section 5.

## 3. Settled as method (proposed; the skill absorbs it unless Tony objects)

- **The figures printed for a fed value (L-325 re-examined, as L-314
  asked).** The declared pressure's derived standoffs were stored with
  a reported figure count and a test that fails when the input moves.
  A fed value moves every day, so that test cannot stand. The rule:
  each standoff prints to the place the day's own band earns (the low
  to high range is its error), by the same report_exponent rule the
  periods use. The band is the uncertainty; no typed figure count.
- **The aberration from the measured speed.** Applied from the day's
  mean speed; the hover's sentence of Oct 17 changes from "is turned a
  few degrees" to the measured angle, printed to the place the day's
  speed band earns.
- **Derived pressure.** p = rho v^2 with the proton mass; the helium
  fraction is a declared assumption stated on the row, as L-314 says.
- **The i panel.** One sentence: the two shells are drawn for the
  solar wind as measured over the day named in the hover, from NOAA's
  real-time solar wind (the DSCOVR spacecraft at L1), with the link.
- **Checks.** The step's own suite with planted faults (a band
  outside a model's range not clamped; a stamp missing; a fetch
  failure falling back silently); the orrery's maintenance run reads
  it; the website's Cache in step covers the pulled file; the drift
  checker reads the fed rows' non-length units (L-305 noted this).

## 4. The build, when it comes (after L-485, by section 5)

Two Code sessions, orrery then gallery, each judged on Tony's screen
or phone:
- **Orrery:** the fetch step (a new module beside period_fetch.py and
  path_plan.py, in the maintenance run and on the dashboard); the
  stored file under data/; the three declared rows become fed rows
  with the file as their source and the Sept 12 declared values as the
  stated fallback; the Earth shells' hovers in the orrery read the
  file; the export carries it. horizons-orbital-mechanics does not
  fire (no JPL); provenance-discipline and orrery-coding-conventions
  do; earth-system-pipeline is consulted for the one NOAA source it
  already names (SWPC, L-313).
- **Gallery:** the Daily Run pulls the file; feature_renderers.js
  draws the two shells at the day's mean with the aberration; the
  hovers and the i panel sentence; the Earth room's checks.
- **Mode 5:** Tony opens the Earth room on a quiet day and on a stormy
  one (NOAA's G-scale tells which) and sees the shells move and the
  hover say by how much and when.

## 5. The order of work, ruled Oct 29, 14:10

1. The gallery session running now finishes: L-399, L-502, L-503,
   pushes, Tony's looks.
2. One orrery Code session for L-504 (the orrery's clock), ruled Oct
   28 to go before L-485; sharper now, because on GitHub's computers
   the clock is UTC.
3. L-485 (a nightly run): its two Code sessions, orrery then gallery,
   beginning with the Oct 25 design record's section 4 verifications,
   as the Oct 27 brief says.
4. L-314 (this item), option C, as a step in the now-nightly
   maintenance run.
5. Earth's remaining talks (L-321, the Lagrange points L-297 and
   L-294, precession L-374 and L-061) continue from Tony's phone in
   between; their builds follow.
On Where We Are's road, Earth's list and the nightly run swap places:
the nightly run becomes "now", Earth's list "beside". Compositions
(L-489) stay after both.

## 6. Tony-action rollup

- (do) Nothing now. Commit this file with the next orrery push.
- (decide) Nothing pending; the three decisions of the talk are ruled
  above, and the method points stand unless you object.

Written October 29, 2026 with Anthropic's Claude Fable 5.1.
