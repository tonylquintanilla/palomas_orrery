# Gap capture -- FLAG-2 propagate_marker (documentation only) -- L-167

Built on orrery e796693a920ec643775a2b5eae3392d96407a0e5
and gallery d49fd0b353f49930e199be1cf8c67639bab9b3cf
(https://github.com/tonylquintanilla/palomas_orrery,
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Type: DOCUMENTATION. No code touched. Session did NOT push.

SUPERSEDES the earlier L-166-numbered draft of this capture. In the
interim the orrery moved (637dd77b -> e796693a, two commits: "Update
LEDGER_CONSOLIDATED.md" + "gallery and master plan update") and handle
L-166 was assigned to a DIFFERENT item -- F1b, the trust-system
consumption side (resolver reads per-object windows + soft-edge
date-picker UX; coupled to L-149/L-150/L-126/L-080). Pasting the FLAG-2
block as L-166 would collide with that item -- the exact renumbering-leak
failure the ledger conventions guard against. This item therefore takes
the next free handle, L-167 (max in use is now L-166).

Re-verified at the new HEAD:
- FLAG-2 is STILL uncaptured in the ledger (grep for k_gauss /
  propagate_marker / mean-motion is empty) -- the finding stands.
- Gallery HEAD is UNCHANGED (d49fd0b3), so every code-side fact below
  holds byte-for-byte: render_orbits.py line 90, assemble.py:62,
  test_artifact1_earth.py:81, builder FLAG-2 comments.
- Cited handles are stable: L-118 DONE, L-149 DONE (F1a closed), L-150
  OPEN, L-154 BLOCKED (JS feature-rendering layer), L-119 OPEN.
- The master plan still names FLAG-2 (line ~20) only in the past tense as
  "caught"; the clarification below is still needed.

Only two things changed from the prior draft: the handle (L-166 -> L-167)
and the orrery anchor (637dd77b -> e796693a). The FLAG-2 substance is
unchanged.

--------------------------------------------------------------------------
1) PASTE INTO: LEDGER_CONSOLIDATED.md  (orrery repo)
   Location: section "## W. WEB PUBLICATION TRACK" -> "### W.Active --
   current phase", among the W.Active DETAIL blocks (natural spot: near
   L-154 and the new L-166, all same phase / same trigger).
   Then run ledger_index.py to regenerate the INDEX zone. Do NOT hand-edit
   the index rows -- the indexer builds them from this block's metadata
   comment.
--------------------------------------------------------------------------

#### [L-167] propagate_marker uses solar K_GAUSS mean-motion -- wrong for planetocentric moon markers (FLAG-2; caught in F1 design, avoided in serving, source fix still open)
<!-- L:167 status:OPEN upd:2026-07-28 section:W.Active flag: rice:3/3/80/2 -->
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
  MASTER_PLAN_INTERACTIVE_GALLERY.md, "New in v14").
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

**Tony:** documentation-only capture (repo moved twice since the F1 build;
no code touched this session). Gives the caught-but-unfixed bug a handle so
it cannot fall through when L-154 / Artifact 2 resumes. Renumbered from an
earlier L-166 draft after L-166 was taken by F1b in the interim.

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
MASTER_PLAN_INTERACTIVE_GALLERY.md ("New in v14"). Coupled to L-154 (same
trigger; DISTINCT bug -- L-154's resolver `tuple(dict)` drops feature
PARAMETERS; this drops marker POSITION accuracy). Sibling to L-166 (F1b
trust consumption -- distinct concern, same assembler / pre-Artifact-2
phase). Anchored: built on orrery e796693a / gallery d49fd0b3.

--------------------------------------------------------------------------
2) PASTE INTO: documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md (orrery repo)
   Text-anchored (robust to line shifts): find the sentence ending
     "...(planetocentric mean-motion in `propagate_marker`) GPT's
      manifest missed entirely."
   Insert the following sentence immediately AFTER "missed entirely." and
   BEFORE 'See "New in v14" below.'. Purpose: the existing text reads as
   "handled"; this makes the caught-vs-fixed distinction explicit and
   points to the handle. (Distinct from L-166, which is the trust-
   consumption item referenced later in this section.)
--------------------------------------------------------------------------

That bug is AVOIDED in the F1 serving path (moons carry Horizons' own `n`),
but `propagate_marker` itself still derives mean motion from solar GM at
HEAD and remains on the assembler's live marker path (assemble.py); the
source fix is tracked as L-167, to land with L-154 before any moon artifact
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
