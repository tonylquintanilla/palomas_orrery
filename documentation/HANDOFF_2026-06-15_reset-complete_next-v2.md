# Handoff -- 2026-06-15 -- Reset button COMPLETE; trace-storm guard delivered

## Round trip (do this first next session)

Session BUILD base: `77dce3ead907b49af70eac05223e0dc7ee007520` (branch main).
This session reconciled the prior handoff's close SHA (`aa1a4cd`) to HEAD and
found four DOC-ONLY commits since (`25adda6`, `c461b37`, `728ceba`, `77dce3e`)
-- no .py changed, so the Reset touchpoint-map line numbers held byte-exact.

The Reset + trace-storm work was delivered as Mode-1 snippets + one new test
file; Tony applies, commits, and pushes. So at the time this handoff is written
the new bytes are NOT yet on the remote.

Next session: read remote HEAD live (`git ls-remote --symref <repo> HEAD`).
Expected: the SHA Tony pushed after applying the Reset + guard snippets (record
it here when you push: built on `77dce3e`; pushed at `__________`). If HEAD is
still `77dce3e`, the snippets were not pushed -- reconcile before building.

Repos: `tonylquintanilla/palomas_orrery` (app), `tonyquintanilla.github.io`
(website / Gallery Studio).

SHA chain into this session:
`aa1a4cd` (19.3 Phase 2 close) -> `25adda6` -> `c461b37` -> `728ceba`
-> `77dce3e` (doc-only; reset design docs committed) == this session's build base.

## Done this session -- Reset button (render-confirmed) + trace-storm guard (sandbox-proven)

### Reset button -- COMPLETE, render-confirmed Mode 5 (Tony, doc-1/doc-3)
Top-bar Reset (date_frame row 0, col 11, next to Vernal Eq), behind the confirm
dialog, returns the GUI to STARTUP state. Delivered as two Mode-1 snippets into
`palomas_orrery.py` (handler `reset_all_selections` ~L8211; button ~L8504) plus
the new full file `test_reset_completeness.py`.

Mechanism (Option A, shell-clear resolved as a complement-set sweep): objects
loop clears the 182 body/spacecraft/comet vars; the 10 named display/option
toggles are restored to DECLARED defaults (the two marker vars default ON = 1,
restored to 1, not 0); a complement-set sweep zeroes EVERY remaining module
tk.IntVar (the 113 shells + 4 dead stragglers); 3 StringVars -> Auto/Sun/None;
10 scalar entries -> startup strings; date -> now via existing fill_now().

Runtime-proven: 310 global IntVar names -> 309 distinct objects (frag_var aliases
comet_2025k1d_var). The sweep targets exactly 117 vars, ALL declared-default 0,
so zeroing is correct; the only default-1 vars (the two markers) are handled in
the named set, never swept. `test_reset_completeness.py` dirties every var and
asserts the LIVE handler restores all 309 IntVars + 3 StringVars + 10 entries
-> PASS. Tony's Mode-5 gate confirmed: dropdown counts down to ['Sun'], next
plot rebuilds clean, days_to_plot = 28, center = Sun.

DESIGN DEVIATION (recorded): the touchpoint map prescribed iterating
SHELL_CONFIGS/CUSTOM_SHELLS for the shells; that registry reaches only 78 of the
113 (Sun 19, Earth 12, asteroid belts 4 = 35 are hand-coded). The complement
sweep is provably total and drift-proof; the guarantee lives in the completeness
TEST, per the map's "build the test, not the architecture."

MAP CORRECTION (recorded): the map's 4 "stragglers to confirm"
(arrokoth_new_horizons_var, dw_var, kbo_var, voyager1h_var) are DEAD -- declared,
never wired. The live "2024 DW" var is asteroid_dw_var, already in the 182
objects. The sweep re-zeros the dead 4 harmlessly (D-sweep candidates).

### Trace-storm guard -- DELIVERED, sandbox-proven, RENDER-GATE PENDING
Observed in the Reset gate (doc-1): clearing 182 objects fired the per-object
`update_center_dropdown` 'write' trace ~182 times (the `[CENTER MENU] Dynamic
centers: Sun + ['Sun']` flood). Three Mode-1 edits suppress it: a module flag
`_reset_in_progress` + early-return guard in `update_center_dropdown`; the
objects loop wrapped in try/finally with the flag set; one explicit rebuild at
the END of the handler (after center -> Sun). Sandbox proof: rebuilds during a
Reset 182 -> 1; with a planet pre-set as center the menu ends Sun-only (the
end-placement also clears a previously-selected center that the old per-object
path would have left lingering); completeness test still PASSES; compile/ASCII/LF
clean. NOT yet render-gated by Tony.

FIRST ACTION next session: apply the guard snippets (if not already), run the
Reset, confirm the `[CENTER MENU] ...` flood is gone (one line, not ~180) and the
dropdown still lands Sun-only. Then close the guard item in the ledger.

### Mercury epoch anomaly -- investigated, NOT resolved (deferred to recurrence)
doc-1 rendered Mercury's Keplerian with `epoch 2019-01-01 osc.` / a 2018
perihelion while Venus/Earth were current. Claude's first read ("7-year stale
cache") was WRONG and retracted -- the project is 18 months old and the manual
fallback (planetary_params['Mercury']) carries epoch 2025-11-19, not 2019.
Grounded fact: doc-1's params had MA/TA keys, which only the OSCULATING path
produces (the static dict has neither), so the 2019 value was a runtime
osculating element set, now overwritten by Tony's update (current = 2026-06-15
17:50, marker 0.433395 == hover 0.4333945989). Origin not determinable from disk;
Tony's recollection insufficient. Per Tony: test it if it recurs. See D.Priority.

## Backlog (cold-startable; pick at next session start -- Tony converges)

PROPOSED next primary (Claude's suggestion, Tony's call):
A. GO-BUTTON PRESET-VISIBILITY (the other half of the Reset pairing). Reset is
   the one-tap way BACK to startup; the open half is making an ACTIVE preset's
   auto-set bundle VISIBLE ("preset active -- center: Arrokoth, scale: 3e-5 AU").
   Design TBD, design-first session. Sticky center/scale/selection itself is
   CORRECT and universal -- do NOT "fix" the stickiness.

Equally valid alternatives:
B. 19.3 FAST-FOLLOW: user-settable range/dtick GUI fields (orrery generation-time
   + Gallery Studio refinement = the full round trip); S3 exoplanet (~5996) opt-in
   to build_scene/auto_dtick with its own render gate. Machinery is warm
   (build_scene, auto_dtick, _calculate_grid_dtick).
C. plot_objects / animate_objects DIVERGENCE AUDIT (dedicated, map-first). Map
   both pipelines, three-bucket catalog (shared / intentionally divergent /
   accidental drift), optional parity smoke. The Reset + animation work keeps
   surfacing divergence (center-body marker render gap is the live example).
   Full function-merge stays OFF the list (high blast radius).
D. Camera-tracking S4 per-frame autorange residual (the June-13 dedicated item;
   `_track_axis` ~7627 emits the full spec; residual is large-window / no-JS).

RESERVE: IPC food-insecurity build (API key not yet arrived; Tony waiting) and
the Gallery/Studio track (ledger section H) if IPC keeps waiting.

Cosmetic cleanups (bundle when convenient): the `WARNING: Unknown object type
'satellite'` spurious warning; Psyche encounter hardcoded-fallback `# Source:`
gap; strip trailing whitespace palomas_orrery.py 5711/7927; regenerate
MODULE_ATLAS.md (build_scene signature stale).

## Protocol reminders

- `palomas_orrery.py` = Mode 1 snippets only, never full file. Other modules can
  take full-function / full-file.
- Map ALL touchpoints before building; partial reset / partial sweep is the
  failure to avoid. Smoke against the LIVE dispatch/handler, not the builder in
  isolation; Mode-5 visual gate is authoritative.
- Bottom-up edits; ASCII/LF; credit line on touched modules; ledger update +
  handoff before close.
- The render wins over the handoff. The trace-storm guard is a CLAIM until Tony
  gates it; the Mercury origin is UNKNOWN, not explained.

## Ledger

Paste blocks provided in `LEDGER_additions_2026-06-15_reset.md`: a C.DONE entry
(Reset, render-confirmed), a near-term OPEN entry (trace-storm guard, render-gate
pending), two D.Priority entries (osculating pre-fetch false-provenance messages;
Mercury 2019-epoch anomaly), and two D.Cosmetic entries (satellite warning;
Psyche fallback Source gap). Update the running ledger IN PLACE; do not re-embed.
