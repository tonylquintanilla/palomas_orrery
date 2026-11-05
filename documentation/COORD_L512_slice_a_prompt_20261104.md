Please see this prompt.

Built on 79018c0c at https://github.com/tonylquintanilla/palomas_orrery
(branch main).

Tony's rulings for L-512 part 2 are in the last section of
documentation/MAP_L512_jpl_fallbacks_20261104.md, "Tony's rulings,
November 4, 2026". Read that section first and build from it; where it
differs from the map's own recommendations, the rulings win. The order
(a), (b), (c) stands. One change to the rulings, made here: the fresh
switch's check covers the whole repository, which replaces
"palomas_orrery_helpers.py added to TestUtcClock".

Start as CLAUDE.md says: if local HEAD differs from GitHub's main, or
the working tree has edits waiting, report and stop. Do not reset,
discard or overwrite any work. Confirm every code fact the rulings
section states at HEAD before building on it.

Before any other work, save this prompt verbatim as
documentation/COORD_L512_slice_a_prompt_20261104.md.

Slice (a) is built in two parts, with my look between them.

PART A1: THE SAVED FILE GOES, AND EVERY JPL QUESTION IS ASKED FRESH

1. Inventory first. List every reader, writer, restorer and repairer of
   data/orbit_paths.json and its two backups at HEAD, by file and
   function, marking each as live (called), uncalled, test, or comment
   only. A review at 79018c0c found at least:
   - palomas_orrery.py: startup's orbit_data_manager.initialize (line
     4007) and the health summary that opens the file (4016) with the
     restore-point display after it; update_orbit_paths (save, 4164);
     get_orbit_data_for_plotting (4187); the static plot's writer call
     and its "Update Orbit Data?" dialog (5141); the animation worker's
     writer call, which has no dialog (6755).
   - orbit_data_manager.py: initialize, load_orbit_paths (which can
     restore a backup over the main file), repair_cache_on_load,
     save_orbit_paths, update_orbit_paths_incrementally, and its own
     on_center_change (not the app's, which is
     palomas_orrery.on_center_change).
   - palomas_orrery_helpers.cleanup_old_orbits (imported, call
     commented out); data_inventory.py's entry for the file; the
     dashboard's "Verify Orbit Cache" and "Export Orbit Cache" entries
     and their scripts.
   Report anything the inventory adds to this list.

2. Then:
   - Removed: every live app connection that exists only for this file,
     at startup, in the static plot and in the animation, along with
     the dialog, the writer, and helpers used only by them.
   - Kept, because the osculating-elements cache uses them:
     orbit_data_manager.utc_to_tdb and query_horizons_elements
     (imported by osculating_cache_manager.py and test_period_fetch.py).
   - Marked obsolete, in the DEPRECATED-banner form palomas_orrery.py
     already uses (L-509 has not ruled yet): verify_orbit_cache.py,
     export_orbit_cache.py, cleanup_old_orbits, and any retained
     uncalled function in the list. Say plainly which of them still
     read the file if someone runs them on purpose.
   - data_inventory.py stops listing the file.
   - Stop and ask me if a removal would reach anything that serves
     another store.

3. Prove nothing live touches the file. Test startup, a static plot
   and an animation twice: with the file present and with it absent.
   Use throwaway copies or watch file access; a launch with the file
   missing proves nothing by itself, because the old readers skip a
   missing file silently. Restore every original file even if a check
   fails, and never overwrite an original with a new one. You never
   delete data/orbit_paths.json or its backups: that is my step, last
   in the run order.

4. The fresh switch, cache=HORIZONS_CACHE, at the nine JPL calls that
   lack it: palomas_orrery_helpers.fetch_trajectory and
   fetch_orbit_path; spacecraft_encounters.py, three;
   comet_visualization_shells.py, one; earth_pole_of_date.py, two;
   earth_pole_live_check.py, one. Locate them by function.

5. Rebuild the freshness check on Python's parser, not line text, and
   run it over every .py file except the tests and documentation/ (its
   old patch scripts carry code in strings). It finds every call of a
   method named vectors, elements or ephemerides (or the _async forms),
   across line breaks, and requires the keyword cache=HORIZONS_CACHE.
   cache=True, a comment or a string does not satisfy it. A call is
   exempt only when get_query_payload=True is written in it. Any
   reference to those methods that is not a direct call (saved under
   another name) is flagged. A file that will not parse fails the
   check. Calls that are not JPL go on an exceptions list inside the
   check (file, function, reason, printed every run); today that is
   provenance_history.py's two Counter.elements() calls. The passing
   output names how many files and calls it examined. Keep the
   local-clock and utc_clock checks on DATA_PATH_MODULES as now.
   Report the full list the scan finds before switching; if it
   differs from the nine, say so.

6. Make it run where it counts. Register every new test class in
   test_orbit_cache.py's main suite, which today loads only
   TestOrbitCache and TestUtcClock by name. Plant one unfresh call,
   show the maintenance run's "Orbit cache" step failing on it, remove
   the plant, run again, and show the passing output naming the
   repository-wide check.

STOP: report A1 with the file list and my look, wifi off and on. With
the wifi off I expect Juno around Jupiter no longer to draw, since it
was coming from astroquery's saved answer, while Mars and Halley keep
their orbits. Say whether that is what I should see, and what else
changes. Do not start A2 until I have looked.

PART A2: "NO SUCH BODY" IS NOT "JPL UNREACHABLE" (RULING 1)

7. Record the installed astroquery version and read how it actually
   reports each case. fetch_trajectory and fetch_position must tell
   apart: an unknown target, an ambiguous target (more than one
   match), and a failure to reach JPL (connection error, timeout, HTTP
   failure). Unavailable dates, empty results, malformed answers and
   local errors are none of these, and are never called an outage.
   Do not label every leftover exception "unreachable".

8. Cover both routes fetch_position takes: the direct small-body
   request (position_accuracy.fetch_small_body_state) and then
   astroquery. A definite "unknown" or "ambiguous" from the first
   route must not be overwritten by an outage when the second route
   fails to connect.

9. Each fetch hands its outcome to its callers, not only to the
   console. Make only the caller changes needed so that an unknown or
   ambiguous target never enters the existing fallback branches
   (plot_actual_orbits, the static worker, the animation worker).
   Successful results and date padding are unchanged. Build no new
   fallback: propagation and the positions record are slices (b) and
   (c).

10. Tests, all without the network: each outcome, on both routes, for
    both functions, with faked answers, plus a success case and a
    non-outage failure; registered in the main suite as in step 6.

Records at the end of each part: L-512, Where We Are by section, and
skill sentences by the records skill's rule. In A1, record on L-512, in
this prompt's words, the change to the rulings made above (the fresh
switch's check covers the whole repository). One skill sentence is
known now: horizons-orbital-mechanics's L-470 paragraph sends a session
to compare saved paths in data/orbit_paths.json after a body's record
changes; once the file is gone that would send a session to a store
that no longer exists, so it is corrected in A1 and the skill bumped,
with its manifest row and the protocol's version entry.

Commit and push are mine. Each part's report ends with the file list
(edits per file), the run order, the token count (or sizes read and
written), and the Tony-action list.
