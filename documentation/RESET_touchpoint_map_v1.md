# Reset Button -- Touchpoint Map (selection-var families)

Mapped against HEAD `aa1a4cd`. Purpose: enumerate EVERY state Reset must clear or
restore so the clear is provably total. The failure to avoid is a partial reset
(clears bodies, silently leaves shells/toggles) -- same class as the encounter
stickiness and parallel-pipeline drift.

## The load-bearing finding

`objects` (built at palomas_orrery.py:3422 via build_objects_list, from
`get_all_var_names()` = OBJECT_DEFINITIONS var_names) covers only **182 of 309
IntVars**. The `for obj in objects: obj['var'].set(0)` loop does NOT touch the
other 127 -- which are dominated by the SHELLS. An objects-only Reset would leave
every shell and every display toggle checked.

Also: two toggles default ON. Reset must restore each var to its DECLARED
default, NOT blindly to 0.

Counts: 309 IntVars (182 objects + 113 shells/belts + 5 display + 5 option +
4 stragglers) + 3 StringVars + N scalar entry widgets.

---

## Family 1 -- Objects (182 vars)  [one loop]

Bodies, moons, dwarf planets, asteroids, comets, interstellar objects,
spacecraft, Lagrange points, barycenters, exoplanet/star systems. All default 0.

Clear: `for obj in objects: obj['var'].set(0)`

## Family 2 -- Shells / structure sub-toggles (113 vars)  [NOT in objects -- the risk]

All default 0. By body:
- Sun (19): core, radiative, photosphere, chromosphere, inner/outer_corona,
  streamer_belt, roche_limit, alfven_surface, termination_shock, heliopause,
  inner/outer_oort, inner_oort_limit, outer_oort_clumpy, hills_cloud_torus,
  galactic_tide, gravitational, shells
- Mercury (8), Venus (7), Earth (12, incl. leo / geostationary_belt /
  system_viz), Moon (6), Mars (8), Jupiter (10, incl. io_plasma_torus /
  radiation_belts), Saturn (10, incl. enceladus_plasma_torus), Uranus (8),
  Neptune (8), Pluto (6, incl. haze_layer), Eris (5), Planet 9 (2: surface,
  hill_sphere)
- Asteroid belts (4): main, hildas, trojans_greeks, trojans_trojans

IMPLEMENTATION: prefer iterating the SHELL registry over hardcoding 113 names --
SHELL_CONFIGS (shell_configs.py:85) + CUSTOM_SHELLS (2053). Confirm that iterating
their keys reaches every shell var; if a few aren't keyed there, clear those
explicitly. (This registry-vs-hardcode choice is LOCAL to the shell family --
still Option A, not a global refactor.)

## Family 3 -- Celestial / star display toggles (5 vars)  [all default 0]

star_background_var (2723), star_names_var (2724), celestial_grid_var (2725),
celestial_grid_labels_var (2726), constellation_names_var (2727).

## Family 4 -- Marker / animation / fetch toggles (5 vars)  [MIXED defaults]

- show_apsidal_markers_var (10288)   default = **1**  (restore to 1, not 0)
- show_closest_approach_var (10290)  default = **1**  (restore to 1, not 0)
- animate_comet_tails_var (10435)    default = 0
- animate_magnetospheres_var (10452) default = 0
- special_fetch_var (10553)          default = 0  ("always disabled")

## Family 5 -- Scalar selectors (3 StringVars)

- scale_var (10133)        -> 'Auto'
- center_object_var (10162) -> 'Sun'
- track_camera_var (10473)  -> 'None (free camera)'

## Family 6 -- Scalar entry widgets  [delete+insert, not var.set()]

- Date fields entry_year/month/day/hour/minute -> NOW. Reuse the existing
  set-to-now fill (safe_int(entry_*, now.*) at ~564-568; the delete/insert
  pattern at ~8173+). hour/minute default to 0.
- days_to_plot_entry -> startup default (confirm value at implementation).
- Animation step, trajectory interval, encounter date-override -> startup values.
CONFIRM at implementation: exact widgets + their startup defaults; reuse the
date-fill-now helper rather than reimplementing.

## Stragglers to confirm (4 IntVars, not in objects)

arrokoth_new_horizons_var (3228), dw_var (3220), kbo_var (3190),
voyager1h_var (3056). Look body-like (the first is the New Horizons/Arrokoth
flyby trajectory -- the one that stayed checked in the bug that started this).
Confirm whether each is a user checkbutton (clear to 0) or an internal flag
(leave). Did not match a one-line Checkbutton pattern -- created elsewhere.

## Explicitly OUT (Reset leaves alone)

Window geometry, last_save_directory, the orbit cache, remember_var (436/4681 --
dialog-local "remember my choice"), and any app-preference vars. Boundary: a GUI
Reset cannot close already-open Plotly browser tabs or wipe console scrollback --
clean slate for the NEXT plot, not erase past output.

---

## The completeness guard (this is what makes Option A safe)

Do NOT build a registry refactor to prevent drift. Instead, build the TEST that
catches it (bar-for-modification): a smoke test that snapshots every IntVar's and
StringVar's DECLARED default, calls the Reset handler, and asserts each var ==
its default afterward. If a future shell/toggle family is added and Reset misses
it, the assert fails loudly. That converts "did we enumerate every family" from a
silent partial-reset risk into a caught test failure -- the structural guard
lives in the test, not in an over-built architecture.

Run it against the LIVE Reset handler (the button's command), not a reimplemented
clear -- a test of the wrong path passes falsely.

## Build order next session (after confirming this map with Tony)

1. Confirm the family list + the 4 stragglers + the Family-6 widget defaults.
2. Reset handler: objects loop + SHELL_CONFIGS/CUSTOM_SHELLS loop + Families 3-6
   restored to DECLARED defaults + the `# add new checkbox families here` comment.
3. Button next to vernal_equinox_button (8500); confirm dialog before clearing.
4. Completeness smoke (assert-all-vars-at-default) against the live handler.
5. Mode-5 gate: build a complex plot (many shells/bodies), Reset, confirm it
   really goes blank + now-dated + Sun/Auto. Then ledger + handoff.

Delivery: Mode 1 snippets for palomas_orrery.py (never full file).
