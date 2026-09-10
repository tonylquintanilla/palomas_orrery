# L-310 camera steps built; L-313 (recenter) opened

Built on orrery `5fea17955d5f2d57f8426da8446d7d1b76f7274f`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `57fd93c62606cb91ed56050885dd7ce6f3852859`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
Pushed at: orrery -- the commit carrying `patch_L310_ledger.py`;
gallery -- the commit carrying `patch_L310_camera_step.py` (the next
session reads both from `git log`).

Tony Quintanilla, PE | Claude Fable 5.1 | 2026-09-10
Type: DESIGN + BUILD (one design round from the phone; one gallery
patch; ledger). Protocol v3.56. Handles: L-310, L-313.

**Supersedes** item 1 of the OPEN list in `HANDOFF_earth_close_20260910.md`.

## STEP 0 -- Gates for the next session

- The skill obligation from the Earth close handoff was discharged this
  session: interactive-exhibit loaded 1.1, ledger-and-session-records
  1.11, both matching the manifest. Nothing travels from this session;
  no skill was bumped.
- `git ls-remote` both repos. Orrery one commit past `5fea1795`;
  gallery one commit past `57fd93c6`, or two if the spent patch was
  moved separately.

## WHAT HAPPENED

- **The design round reframed the item.** Tony: coarse sweep is not
  the need; fine control at full magnification is, like a telescope
  by hand at high power. So the step scales with the eye distance
  instead of sitting at a fixed angle, and there is no hold-to-repeat.
- **Recentering surfaced and was split off** as L-313. Rotation
  orbits the scene centre, so a fine step still swings an off-centre
  feature away. The orrery has a recenter for comet detail views;
  that is the prior art.
- **Built** `navCameraStep` in interactive.html and optional arrow
  buttons in `gallery/nav_cluster.js` (a cross with Home at the
  centre, drawn only when a page passes step handlers). Sandbox:
  patch applied on a throwaway copy, re-run aborted on the
  fingerprint, `node --check` on both files, stub-DOM mount gave 7
  buttons with steps and 3 without, rotation math checked by hand.
  Not rendered: Mode 5 is the gate.

## FOUND IN PASSING, NOT FIXED

- interactive.html's header stamp stopped at September 6. The Earth
  step 3 edits of 2026-09-09 (the `EXHIBITS` table, L-291) carry no
  Updated line. This patch adds its own line; the missing one needs
  the wording from the session that made the change.

## OPEN, IN ORDER

1. **L-310 Mode 5** on the Earth room at full zoom, phone and desktop.
   Three knobs in interactive.html if it is off: `NAV_STEP_BASE_DEG`
   (5), `NAV_STEP_SIGN` (+1), `NAV_STEP_POLE_MARGIN_DEG` (2). If the
   cross collides with the drawer handle on a portrait phone, that is
   a layout change in `nav_cluster.js`, not a knob.
2. **L-311**, **L-305**, then the plan's order, as in the Earth close
   handoff.
3. **L-313** design round after L-310 closes; read the orrery's
   recenter first.

## TONY-ACTION ROLLUP

1. **(do)** Gallery repo root: run `patch_L310_camera_step.py` (Run).
2. **(do)** Orrery repo root: run `patch_L310_ledger.py` (Run), then
   `ledger_index.py` (Run).
3. **(do)** Move both spent patches into each repo's `documentation/`.
4. **(do)** GitHub Desktop: commit and push both repos; report both
   SHAs.
5. **(decide)** Mode 5 on the phone and desktop; say what the arrows
   feel like at full zoom. L-310 closes on your word.

Written September 2026 with Anthropic's Claude Fable 5.1.
