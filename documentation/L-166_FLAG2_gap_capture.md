# Gap capture -- FLAG-2 propagate_marker (documentation only)

Built on orrery 637dd77b625ccf1ca598953c27d8f1f1bfbf12ba
and gallery d49fd0b353f49930e199be1cf8c67639bab9b3cf
(https://github.com/tonylquintanilla/palomas_orrery,
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Type: DOCUMENTATION. No code touched. Session did NOT push.

Reconciliation found ONE undocumented pending item: the FLAG-2 bug in
`gallery/assembler/render_orbits.py` `propagate_marker` is still live at
gallery HEAD, was caught in F1 design and avoided in the serving path, but
was never fixed at the source and has no ledger handle. The master plan
names it (line 20) only in the past tense as a bug that was "caught," which
reads as handled. This capture gives it a handle and corrects that framing.

Everything else I flagged in the prior session is already tracked or
resolved: the fake_vectors sec 5.6 test-consistency issue and the trust/
served_window work are covered by the committed M2_IMPLEMENTATION_REPORT.md
plus L-149 (DONE) and its open follow-on L-150; L-118 (F1) is DONE; the JS
feature-rendering layer is L-154 (BLOCKED); provenance cluster L-155..L-162
is in W.Active.

Next free handle at HEAD is L-166 (highest in use is L-165).

--------------------------------------------------------------------------
1) PASTE INTO: LEDGER_CONSOLIDATED.md  (orrery repo)
   Location: section "## W. WEB PUBLICATION TRACK" -> "### W.Active --
   current phase", among the other W.Active DETAIL blocks (natural spot:
   right after the L-154 block, since they share a trigger).
   Then run ledger_index.py to regenerate the INDEX zone. Do NOT hand-edit
   the index rows -- the indexer builds them from this block's metadata
   comment.
--------------------------------------------------------------------------

#### [L-166] propagate_marker uses solar K_GAUSS mean-motion -- wrong for planetocentric moon markers (FLAG-2; caught in F1 design, avoided in serving, source fix still open)
<!-- L:166 status:OPEN upd:2026-07-28 section:W.Active flag: rice:3/3/80/2 -->
- **What.** `gallery/assembler/render_orbits.py` `propagate_marker()`
  computes mean motion as `n = K_GAUSS / (a ** 1.5)` (line 90 @ gallery
  d49fd0b3), where `K_GAUSS = sqrt(GM_sun)`. Correct ONLY for heliocentric
  bodies. For a planetocentric moon -- served from its OWN osculating conic
  in the parent-relative frame, so `a` is the tiny moon-parent semi-major
  axis in AU -- solar GM is the wrong gravitational parameter, and the
  propagated as-of-today marker lands wrong by ~3 orders of magnitude.
  [verified @d49fd0b3]
- **Worked number.** Moon a ~ 0.00257 AU -> n = 0.01720209895 / 0.00257^1.5
  ~ 132 rad/day -> implied period ~ 68 minutes, versus the real 27.32-day
  sidereal month. Independently re-derived. This is the same catch GPT's F1
  manifest missed and the Fable/GPT competitive cross-check surfaced (see
  MASTER_PLAN_INTERACTIVE_GALLERY.md line 20, "New in v14").
- **Caught != fixed.** F1/M2 (L-118 / L-149) was DESIGNED to avoid this: the
  serving pipeline captures Horizons' own `n` and emits `n_deg_per_day`, and
  the builder never calls `propagate_marker` (FLAG-2 comments at
  gallery_cache_builder.py lines 65, 341, 376, 379). But avoiding it in the
  serving path did not change `propagate_marker` itself -- render_orbits.py
  was correctly out of M2's edit scope, so the wrong formula is still at
  HEAD and `propagate_marker` is on a LIVE dispatch path:
  `gallery/assembler/assemble.py:62` calls it to place the position marker
  for every object that has osculating elements. [verified @d49fd0b3]
- **Dormant, not benign.** Only Artifact 1 (Earth, heliocentric) is built
  and Mode-5 accepted in the interactive assembler today, so the live path
  only ever feeds a heliocentric body, where the formula is correct. It
  becomes a visibly wrong marker the moment a planetocentric moon renders --
  Artifact 2 (Jupiter/Saturn) and Artifact 3 (Moon/Io/Titan), the objects
  L-154's feature-rendering layer unblocks. The trigger for this bug and the
  trigger for L-154 are the same event.
- **Fix approach (not built; design choice for its session).** The correct
  `n` is already in the served data (`n_deg_per_day` on the osculating
  block). Preferred: thread the served `n` into `propagate_marker` and use
  it directly instead of deriving from `a` ("fetched, not recalled" -- use
  Horizons' measured mean motion); alternative: pass the correct
  central-body GM per frame. Either removes the solar-GM assumption. Small,
  targeted change to one function plus the `obj.osculating` payload that
  reaches it; guard the no-`n` case (WARN/skip, never a silent solar-GM
  fallback). Confirm on Earth's existing Mode-5 harness (no heliocentric
  regression) before a moon artifact.

**Tony:** documentation-only capture (repo moved substantially since the F1
build; no code touched this session). This gives the caught-but-unfixed bug
a handle so it cannot fall through when L-154 / Artifact 2 resumes.

**Gap:** land the `propagate_marker` fix (use served `n`, drop solar-GM
derivation, guard no-`n`) BEFORE or WITH the L-154 JS feature-rendering
layer, so the first Jupiter/Saturn/moon render carries correct marker
positions; re-run Earth Mode-5 as the no-regression gate.

**Ref:** `gallery/assembler/render_orbits.py` (propagate_marker, line 90 @
d49fd0b3); `gallery/assembler/assemble.py:62` (live call site);
`gallery/assembler/tests/test_artifact1_earth.py:81` (test call site);
`tools/gallery_cache_builder.py` FLAG-2 comments (65/341/376/379);
`documentation/M2_IMPLEMENTATION_REPORT.md`;
`documentation/PHASE2_F1_BUILD_MANIFEST_v2_2.md` (FLAG-2 origin);
MASTER_PLAN_INTERACTIVE_GALLERY.md line 20. Coupled to L-154 (same trigger;
DISTINCT bug -- L-154's resolver `tuple(dict)` drops feature PARAMETERS;
this drops marker POSITION accuracy). Anchored: built on orrery 637dd77b /
gallery d49fd0b3.

--------------------------------------------------------------------------
2) PASTE INTO: documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md (orrery repo)
   Location: end of the sentence that currently closes at "...missed
   entirely. See "New in v14" below." (around line 20-21). Insert the
   following sentence immediately after "missed entirely." and before
   'See "New in v14" below.' -- or as its own parenthetical sentence in
   that paragraph. Purpose: the existing text reads as "handled"; this
   makes the caught-vs-fixed distinction explicit and points to the handle.
--------------------------------------------------------------------------

That bug is AVOIDED in the F1 serving path (moons carry Horizons' own `n`),
but `propagate_marker` itself still derives mean motion from solar GM at
HEAD and remains on the assembler's live marker path (assemble.py); the
source fix is tracked as L-166, to land with L-154 before any moon artifact
renders.

--------------------------------------------------------------------------
3) NO LEDGER ITEM (disposition note -- for your call, not an action)
--------------------------------------------------------------------------

Earth radiation-belt name prefix: the M1 delivery dropped the "Earth: "
prefix on the two belt names ("Inner Radiation Belt" / "Outer Radiation
Belt") per manifest sec 4.2, and that is what is in the served
objects_config.json now. This was a deliberate de-duplication (the feature
already sits under the `earth` key), following the build contract. My
recommendation is NO ledger item -- it is a resolved intentional deviation,
not a gap. If you would rather restore the source's "Earth: " prefix, it is
a one-line edit to the two `names` strings under `earth.van_allen_belts` in
data/objects_config.json; say the word and I will draft it.
