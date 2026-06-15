# Ledger entry -- Reset button (paste into LEDGER_orrery_consolidated.md)

## [RESET BUTTON] -- GUI reset-to-startup-state -- DELIVERED (pending Mode-5)

Base HEAD: 77dce3e. Mechanism: Option A, with the shell-clear resolved as a
complement-set IntVar sweep (see decision below). Two Mode-1 snippets into
palomas_orrery.py (handler ~L8211, button row0/col11 ~L8504) + new full-file
test_reset_completeness.py.

What Reset restores (provably total -- runtime-proven, not asserted):
- 182 object vars  -> 0   (per-object loop)
- 5 display toggles -> 0
- 5 option toggles  -> declared defaults (2 markers -> 1, rest -> 0)
- 113 shell/belt vars + 4 dead stragglers -> 0  (complement-set sweep)
- 3 StringVars -> Auto / Sun / None (free camera)
- 10 scalar entries -> startup strings (28/10/50x4/29/1d/6h/1h)
- date -> now via existing fill_now()  (days_to_plot reset to 28 first)

Runtime proof (xvfb probe + test): 310 global IntVar names -> 309 distinct
objects (frag_var aliases comet_2025k1d_var). The sweep targets exactly 117
vars (113 shells + 4 stragglers); ALL 117 have declared default 0, so zeroing
them is correct. The only default-1 vars (show_apsidal_markers_var,
show_closest_approach_var) are handled in the named group, never swept.
test_reset_completeness.py dirties every var and asserts the LIVE handler
restores all 309 IntVars + 3 StringVars + 10 entries -> PASS, exit 0.

DESIGN DECISION (deviation from touchpoint-map detail, surfaced to Tony):
The map prescribed iterating SHELL_CONFIGS/CUSTOM_SHELLS to clear shells.
Demonstrated gap: SHELL_DEFINITIONS reaches only 78 of the 113 shell vars
(Sun 19 / Earth 12 / asteroid belts 4 = 35 are hand-coded, not keyed there);
no single registry cleanly covers all 113. Chose the complement-set sweep
(zero every module IntVar not in objects/named-set) -- provably total,
drift-proof (a future checkbox family is cleared automatically), one block,
no hardcoded 113 names. The map itself flagged registry-vs-hardcode as a
LOCAL choice still inside Option A. The completeness guard is the test, per
the map's "build the test, not the architecture" instruction.

CORRECTION to RESET_touchpoint_map_v1.md "Stragglers to confirm":
The 4 vars (arrokoth_new_horizons_var L3228, dw_var L3221, kbo_var L3191,
voyager1h_var L3056) are DEAD -- declared but never wired to a checkbutton or
read anywhere. They are NOT the Arrokoth flyby checkbox the original bug was
about; the live user-facing var for "2024 DW" is asteroid_dw_var, which is in
the 182 objects and cleared by the objects loop. The sweep re-zeros the 4 dead
vars harmlessly. (Candidates for a future D-sweep with # DEAD: tags.)

Also corrected: map note "date hour/minute default to 0" -- reusing fill_now()
sets hour/minute to CURRENT time, which matches true startup by construction
(startup calls the same fill_now()), so dates are correct without special-casing.

## Mode-5 gate (Tony -- before close)

1. Build a heavy plot: check many bodies + several shells (Sun corona/heliopause,
   Earth shells, a couple of planet magnetospheres), set center to a planet,
   set scale to Manual with a small value, change days-to-plot and a couple of
   interval fields, add an animation frame count.
2. Click Reset, confirm Yes.
3. Verify the GUI returns to startup: every checkbox cleared (bodies AND shells),
   center back to Sun, scale Auto, date = now, days-to-plot = 28, all scalar
   entries back to defaults, the two marker toggles back ON.
4. Run the next plot -- it should build the default Sun-centered view, confirming
   no stale selection leaked through.
Note: Reset does not close already-open Plotly browser tabs (out of scope, by
design) -- clean slate for the NEXT plot only.
