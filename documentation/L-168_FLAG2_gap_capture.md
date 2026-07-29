# Gap capture -- FLAG-2 propagate_marker (documentation only) -- L-168

Built on orrery 0d13fbb9cf0d177055572b2b1d4e6f976e2ab9d0
and gallery f4ce24cb68d2aa5834c6abcf98a1d7e0d5a68e8a
(https://github.com/tonylquintanilla/palomas_orrery,
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Type: DOCUMENTATION. No code touched. Session did NOT push.

SUPERSEDES the L-167-numbered draft of this capture (which itself
superseded an earlier L-166-numbered draft). Both repos moved again in
the interim:
- orrery: e796693a -> 0d13fbb9 (advanced)
- gallery: d49fd0b3 -> f4ce24cb (advanced)

The consequential change: handle L-167 was assigned to a DIFFERENT item
in the interim -- "[L-167] Artifact-1 field notes -- orrery-coding-
conventions still missing three entries" (section H, three Plotly
rendering gotchas from the Artifact-1 as-built: aspectmode cube,
scatter3d has no dash attribute, textfont.color must be set explicitly).
Pasting the FLAG-2 block as L-167 would collide with that item -- the
same renumbering-leak failure the ledger conventions guard against, and
the same mechanism that forced the L-166 -> L-167 renumbering one round
ago. This item therefore takes the next free handle, **L-168** (max in
use is now L-167; L-168 confirmed free repo-wide).

Re-verified at the new HEAD:
- FLAG-2 is STILL uncaptured in the ledger (grep for k_gauss /
  propagate_marker / mean-motion is empty) -- the finding stands.
- Gallery-side code is BYTE-IDENTICAL between d49fd0b3 and f4ce24cb for
  every file this capture cites (render_orbits.py, assemble.py,
  test_artifact1_earth.py, tools/gallery_cache_builder.py -- diffed
  directly, zero output). Every line-number claim below holds without
  re-derivation: render_orbits.py line 90, assemble.py:62,
  test_artifact1_earth.py:81, builder FLAG-2 comments.
- L-166 (F1b) is unchanged.
- The master plan's anchor sentence ("...(planetocentric mean-motion in
  `propagate_marker`) GPT's manifest missed entirely. See \"New in v14\"
  below.") is unchanged, byte-identical across both orrery commits --
  the insertion point below is still valid as written.
- Ledger INDEX/DETAIL reconciliation (asked for separately, reported in
  chat, not repeated here): currently consistent at this HEAD (162 real
  DETAIL blocks = 100 live + 62 closed per the INDEX header). Re-run
  ledger_index.py after pasting this block to fold L-168 in (163 total).

Only three things changed from the L-167 draft: the handle (L-167 ->
L-168), both repo anchors (advanced to current HEAD), and one added
disambiguation line (new L-167 is an unrelated item, noted in Ref below).
The FLAG-2 substance is byte-for-byte unchanged from the original
capture.

--------------------------------------------------------------------------
1) PASTE INTO: LEDGER_CONSOLIDATED.md  (orrery repo)
   Location: section "## W. WEB PUBLICATION TRACK" -> "### W.Active --
   current phase", among the W.Active DETAIL blocks (natural spot: near
   L-154 and L-166, all same phase / same trigger).
   Then run ledger_index.py to regenerate the INDEX zone. Do NOT hand-edit
   the index rows -- the indexer builds them from this block's metadata
   comment.
--------------------------------------------------------------------------

#### [L-168] propagate_marker uses solar K_GAUSS mean-motion -- wrong for planetocentric moon markers (FLAG-2; caught in F1 design, avoided in serving, source fix still open)
<!-- L:168 status:OPEN upd:2026-07-28 section:W.Active flag: rice:3/3/80/2 -->
- **What.** `gallery/assembler/render_orbits.py` `propagate_marker()`
  computes mean motion as `n = K_GAUSS / (a ** 1.5)` (line 90 @ gallery
  f4ce24cb), where `K_GAUSS = sqrt(GM_sun)`. Correct ONLY for heliocentric
  bodies. For a planetocentric moon -- served from its OWN osculating conic
  in the parent-relative frame, so `a` is the tiny moon-parent semi-major
  axis in AU -- solar GM is the wrong gravitational parameter, and the
  propagated as-of-today marker lands wrong by ~3 orders of magnitude.
  [verified @f4ce24cb]
- **Worked number.** Moon a ~ 0.00257 AU -> n = 0.01720209895 / 0.00257^1.5
  ~ 132 rad/day -> implied period ~ 68 minutes, versus the real 27.32-day
  sidereal month. Independently re-derived. This is the same catch GPT's F1
  manifest missed and the Fable/GPT competitive cross-check surfaced (see
  MASTER_PLAN_INTERACTIVE_GALLERY.md, "New in v14").
- **Caught != fixed.** F1/M2 (L-118 / L-149) was DESIGNED to avoid this: the
  serving pipeline captures Horizons' own `n` and emits `n_deg_per_day`, and
  the builder never calls `propagate_marker` (FLAG-2 comments at
  gallery_cache_builder.py lines 67, 341, and the derivation note ~372-380).
  But avoiding it in the serving path did not change `propagate_marker`
  itself -- render_orbits.py was correctly out of M2's edit scope, so the
  wrong formula is still at HEAD and `propagate_marker` is on a LIVE
  dispatch path: `gallery/assembler/assemble.py:62` calls it to place the
  position marker for every object that has osculating elements.
  [verified @f4ce24cb]
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

**Tony:** documentation-only capture (repo moved twice since the original
F1 build; no code touched this session). Gives the caught-but-unfixed bug
a handle so it cannot fall through when L-154 / Artifact 2 resumes.
Renumbered twice on the way in -- L-166 draft -> L-167 draft -> this L-168
-- purely from handle collisions as other sessions landed unrelated items
in the same window; the underlying finding never changed.

**Gap:** land the `propagate_marker` fix (use served `n`, drop solar-GM
derivation, guard no-`n`) BEFORE or WITH the L-154 JS feature-rendering
layer, so the first Jupiter/Saturn/moon render carries correct marker
positions; re-run Earth Mode-5 as the no-regression gate.

**Ref:** `gallery/assembler/render_orbits.py` (propagate_marker, line 90 @
f4ce24cb); `gallery/assembler/assemble.py:62` (live call site);
`gallery/assembler/tests/test_artifact1_earth.py:81` (test call site);
`tools/gallery_cache_builder.py` FLAG-2 comments (67, 341, ~372-380);
`documentation/M2_IMPLEMENTATION_REPORT.md`;
`documentation/PHASE2_F1_BUILD_MANIFEST_v2_2.md` (FLAG-2 origin);
MASTER_PLAN_INTERACTIVE_GALLERY.md ("New in v14"). Coupled to L-154 (same
trigger; DISTINCT bug -- L-154's resolver `tuple(dict)` drops feature
PARAMETERS; this drops marker POSITION accuracy). Sibling to L-166 (F1b
trust consumption -- distinct concern, same assembler / pre-Artifact-2
phase). NOT to be confused with L-167 ("Artifact-1 field notes --
orrery-coding-conventions still missing three entries" -- unrelated
Plotly-rendering topic, assigned in the same window; pure numbering
coincidence). Anchored: built on orrery 0d13fbb9 / gallery f4ce24cb.

--------------------------------------------------------------------------
2) PASTE INTO: documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md (orrery repo)
   Text-anchored (robust to line shifts): find the sentence ending
     "...(planetocentric mean-motion in `propagate_marker`) GPT's
      manifest missed entirely."
   Insert the following sentence immediately AFTER "missed entirely." and
   BEFORE 'See "New in v14" below.'. Purpose: the existing text reads as
   "handled"; this makes the caught-vs-fixed distinction explicit and
   points to the handle. (Distinct from L-166, the trust-consumption item
   referenced later in this section, and from L-167, an unrelated
   rendering-conventions item.)
--------------------------------------------------------------------------

That bug is AVOIDED in the F1 serving path (moons carry Horizons' own `n`),
but `propagate_marker` itself still derives mean motion from solar GM at
HEAD and remains on the assembler's live marker path (assemble.py); the
source fix is tracked as L-168, to land with L-154 before any moon artifact
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

Module updated: July 2026 with Anthropic's Claude Sonnet 5.
