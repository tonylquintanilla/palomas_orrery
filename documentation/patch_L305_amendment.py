"""patch_L305_amendment.py -- L-305 amended with the Jelinek 2012 read and
Tony's Shue/Jelinek ruling; L-314 (live solar wind) and L-315 (a patch
method finding) opened. Replaces patch_L305_brief.py,
patch_L305_2_citation.py and the paste steps in
L-305_amendment_20260910.md. Do not run those.

ORRERY repo (palomas_orrery). Built on orrery 5fea1795 at
https://github.com/tonylquintanilla/palomas_orrery ; gallery claims
checked at 57fd93c6 and 4506fb48 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io

Run: save this file in the orrery repo root (beside LEDGER_CONSOLIDATED.md),
open it in VS Code, click Run.  Or from a terminal in the repo root:
    python patch_L305_amendment.py

WHERE IT CAN START. The ledger may be in any of these states, and each
works:
  - exactly as pushed at 5fea1795 (patch_L310_ledger.py never ran, or it
    refused) -- this patch then applies L-310's three ledger edits too,
    byte for byte, and writes that session's handoff if it is missing;
  - with patch_L310_ledger.py's edits, whether or not ledger_index.py ran
    after it;
  - LF or CRLF line endings. The file is written back the way it was found.
The guard compares the ledger's text OUTSIDE the generated INDEX zone,
with line endings normalised. The index is rebuilt by ledger_index.py
afterwards, so its state before this patch does not matter.

Anything else -- the brief or citation patch applied, the design record
pasted by hand -- is refused with the reason, and nothing is written.

What it does, all-or-nothing:
  LEDGER_CONSOLIDATED.md
    - header stamp;
    - L-310's ledger edits, only if absent (see above); L-310 gains its
      gallery push at 4506fb48;
    - L-305: the 2026-09-10 read and ruling, corrected (new handle L-314
      instead of L-313; the tilt and tail-extent lines the replacement
      Gap had dropped are restored; Shue's alpha tagged as not read; the
      hover strings named by line); new Gap and Ref; upd stamp;
    - L-314 opened (live solar wind through the nightly builder);
    - L-315 opened (why the three earlier patches refused).
  documentation/HANDOFF_L310_camera_step_20260910.md
    - written only if absent, verbatim from the L-310 session.

Permanent: the ledger text and the handoff. Disposable: this script.
Success prints one 'ok' per step and 'patch applied'. Any failure prints
one ERROR / ANCHOR FAIL line and writes nothing.
Undo is Discard Changes in GitHub Desktop.

Tony-action rollup:
  1. (do) Run this script, then ledger_index.py (Run). Expect
     "OK: 310 L-blocks parsed, no consistency problems."
  2. (do) Move this script and patch_L310_ledger.py into documentation/.
     Delete patch_L305_brief.py, patch_L305_2_citation.py and
     L-305_amendment_20260910.md: they never landed and their content is
     now in L-305.
  3. (do) Commit and push the orrery; report the SHA.
  4. (do) Keep the Jelinek 2012 PDF where the next L-305 session can
     read it (L-305 Gap item 1).
  5. (decide) Aberration at the declared 400 km/s, or none -- recorded
     in L-305; no hurry.

Written September 10, 2026 with Anthropic's Claude Opus 5.
"""
import hashlib, os, sys

LEDGER = "LEDGER_CONSOLIDATED.md"
HANDOFF = os.path.join("documentation", "HANDOFF_L310_camera_step_20260910.md")
INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"

# md5 of the LF text with the INDEX zone removed
FP_HEAD = "2d0d4b1ae7cd5cdee3273bd33c9f842a"          # orrery 5fea1795 as pushed
FP_L310 = "50f7988782ccef21d577b1109bbe0ff6"          # 5fea1795 + patch_L310_ledger.py's edits
FP_FINAL = "cb220402f781dd810ca4ae98f002782d"        # the tested result of this patch

# ------------------------------------------------------------------
# A. patch_L310_ledger.py's ledger edits, byte for byte. Applied only
#    when the ledger is still at 5fea1795. (Transcribed from the L-310
#    session; checked by reproducing that patch's output exactly.)
# ------------------------------------------------------------------
L310_EDITS = [
(b"""Module updated: September 10, 2026 with Anthropic's Claude Opus 5""",
b"""Module updated: September 10, 2026 with Anthropic's Claude Fable 5.1
(L-310 design ruled and built; L-313 opened), built on 5fea1795.
Module updated: September 10, 2026 with Anthropic's Claude Opus 5"""),
(b"""**Gap:** design round with Tony; then build. Not blocking L-291.
""",
b"""- **Design round, 2026-09-10, on the phone, and the ruling.** Tony:
  coarse sweep and rotation are not the need; the hand and the mouse
  give those. "In full zoom both sweep and rotate are hard to control
  precisely. It's like moving a telescope on full magnification by
  hand." So: no hold-to-repeat, and no fixed angle. The step SCALES
  WITH MAGNIFICATION. A tap turns the camera by a base angle (5
  degrees, a Mode 5 knob) times the ratio of the live eye distance to
  the arrival eye distance, so a wheel-dollied view gets a
  proportionally smaller step and a tap always moves about the same
  slice of the screen -- the slow-motion knob. Frame zoom (+/-) does
  not change the eye distance, and a fixed angle already sweeps a
  fixed slice there, so the two zooms compose.
- **Settled with it.** Left/right yaw about the up vector; up/down
  pitch about the eye's horizontal, refused within 2 degrees of the
  poles. Arrows draw only where the page passes step handlers, so a
  2D page later gets the three buttons unchanged (the L-285 lesson:
  one button, one meaning). Layout is a cross with Home at the centre,
  under + and -. The step reads the live camera through
  `sunLiveCamera` (L-289), so it is right after a touch rotation. The
  sign convention and the base angle are Mode 5 knobs
  (`NAV_STEP_SIGN`, `NAV_STEP_BASE_DEG`).
- **Recentering was raised and split off.** Rotation orbits the scene
  centre, so an off-centre feature swings out of view however fine
  the step; the orrery already has a recenter for its comet-detail
  views. Tony: capture it as its own item. L-313.
- **Built 2026-09-10** by `patch_L310_camera_step.py` in the gallery
  repo (`gallery/nav_cluster.js`, `interactive.html`) against gallery
  `57fd93c6`; syntax-checked and the cluster's two layouts exercised on
  a stub DOM in the sandbox. [render-gated]
**Gap:** Tony's Mode 5, phone and desktop, on the Earth room at full
zoom: the step feels right at high magnification, the arrow signs feel
right, and the cross clears the drawer handle and the title on a
portrait phone. Then DONE.
"""),
(b"""#### [L-311] Earth's rotation period and obliquity are not served, so the axis hover names neither""",
b"""#### [L-313] Recenter the camera on a chosen feature in the exhibit rooms
<!-- L:313 status:OPEN upd:2026-09-10 section:A flag: rice:3/3/60/3 -->
- **Opened 2026-09-10, split from L-310's design round.** A camera
  step, however fine, orbits the scene centre; a feature off that
  centre (the Moon in the Earth room) swings across the screen and
  out on any rotation. A telescope mount has the same limit, which is
  why the object is centred in the finder before high power. The fix
  is to move `scene.camera.center` onto the feature so the arrows and
  the mouse both turn about it.
- **Prior art, from Tony:** the orrery already recenters for
  high-zoom views such as comet details. Read that mechanism first
  (which module, and how it picks the point) before designing the
  room's version; the module is not yet named here.
- **Questions for the design round:** how the point is chosen (a tap
  on a plotted point through Plotly's click event; what a tap on empty
  space does); where the control lives (a cluster button, or a gesture
  with no button); how the frame HUD shows that the pivot moved
  (L-289's triad follows the camera eye, not the centre); and that
  Home restores the arrival centre as it restores the eye.
- **Note:** RICE 3/3/60/3 -> 1.8 proposed, not confirmed.
**Gap:** design round, zero code, after L-310 passes Mode 5. Then one
patch, shared chrome.
**Ref:** L-310 (the arrows), L-267 (the cluster), L-289 (the HUD),
`gallery/nav_cluster.js`, interactive.html (`navCameraStep`,
`navHome`), the orrery's recenter.

#### [L-311] Earth's rotation period and obliquity are not served, so the axis hover names neither"""),
]

# ------------------------------------------------------------------
# B. This patch's own edits. Applied in every accepted state.
# ------------------------------------------------------------------
L305_OLD_GAP_AND_REF = b"""**Gap:** fetch Jelinek et al. 2012 and read its fitted parameters from
the paper; fetch a magnetotail extent citation; supersede
`EARTH_MAGNETOPAUSE_STANDOFF_RADII` (10.0) and
`EARTH_BOW_SHOCK_STANDOFF_RADII` (12.5) with sources; remove the Farris
& Russell "Model form" claim; port the one formulation to
`planet_visualization_utilities.py` and `gallery/feature_renderers.js`;
serve shape parameters and validity range; drop the tilt; then Mode 5 on
both. Also clear now, in whichever patch opens the file: the bow shock
Note still says "the shell's 15 is a migration item" when line 825
already reads the store.
**Ref:** L-291, L-292, L-298 (the orrery-vs-exhibit gap, made concrete),
L-306, `constants_new.py`, `earth_visualization_shells.py`,
`planet_visualization_utilities.py`, `gallery/feature_renderers.js`,
`data/objects_config.json` (gallery), skills/interactive-exhibit/SKILL.md.
"""

L305_NEW_BODY_GAP_AND_REF = b"""- **2026-09-10, the paper read: gap item 1 closes by reading.** The
  peer-reviewed parameters are IDENTICAL to the WDS'10 numbers above:
  R_MP = 12.82 p^(-1/5.26), R_BS = 15.02 p^(-1/6.55), lambda_MP = 1.54,
  lambda_BS = 1.17, R0 at p = 1 nPa (eqs. 13-16). The surfaces in
  aberrated GSE are x = R0 p^(-1/eps) - tau^2/2,
  R_yz = sqrt(2 R0 p^(-1/eps)) tau / lambda. The paper states its own
  envelope: dayside only, within +/- 7 h of local noon; solar wind
  dynamic pressure 0.6-11 nPa; rotational symmetry assumed; no IMF Bz,
  dipole tilt or Mach dependence (sec. 3, 6, 7). Sec. 7 says parabolic
  coordinates suit the bow shock and that elliptical coordinates would
  describe the magnetopause better. [read from Tony's uploaded PDF by a
  Claude Fable 5.1 session, 2026-09-10; not re-read since]
- **The reference, and how it is reached.** Jelinek, K., Z. Nemecek,
  and J. Safrankova (2012), A new approach to magnetopause and bow
  shock modeling based on automated region identification, J. Geophys.
  Res. 117, A05208, doi:10.1029/2011JA017252. The Wiley DOI page
  refuses sandbox fetches. A web search the same day listed the article
  as free access at
  https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2011JA017252
  -- search-result metadata; nobody opened that page. Whether the
  citation meets the Access Standard is settled when its store row is
  written.
- **Tony's ruling (2026-09-10): use each model for the part it fits
  best, and state the reason.** The magnetopause moves to Shue et al.
  (1998), doi:10.1029/98JA01103 -- the source the served row ALREADY
  cites for its standoff: r = r0 (2 / (1 + cos theta))^alpha,
  r0 = (10.22 + 1.29 tanh(0.184 (Bz + 8.14))) Dp^(-1/6.6),
  alpha = (0.58 - 0.007 Bz)(1 + 0.024 ln Dp). The bow shock stays
  Jelinek 2012. This AMENDS the ruling above that one formulation
  serves both boundaries (under "Why Jelinek and not Lin"). Why it
  holds against that ruling's own reason (portability): Shue is two
  lines and eight published coefficients, checkable by eye against the
  paper's figures, so the bar that deferred Lin is still met. Why it is
  worth a second function: the tail. At p = 2 nPa, Bz = 0, the
  cross-section radius at x = -100 R_E is 28.9 R_E under Shue and 45.9
  under the Jelinek paraboloid (the 46 recorded above), and the paper's
  own sec. 7 concedes the parabola for the magnetopause. Shue's tail
  still flares (alpha = 0.59 > 0.5), slowly; it does not close.
  [computed; reproduced 2026-09-10 by the patch that landed this. The
  r0 line matches the Source already on
  `EARTH_MAGNETOPAUSE_STANDOFF_RADII`; the alpha line appears nowhere
  in the repo and was not read this round -- Gap item 1]
- **The tail therefore needs no geometry citation of its own.** The
  "tail gets its OWN citation for extent and cross-section" bullet
  above narrows to EXTENT only: Shue's surface is drawn to the served
  100 R_E and the hover says the drawn surface stops there against a
  real tail past 1,000 R_E, and that Shue was fitted on near-Earth
  crossings, not the distant tail (Show the Envelope). Two parts of
  that hover are not yet sourced. The 1,000 R_E entered with L-291's
  hover requirement and sits in the served magnetotail row's
  `_declared` text with no citation (Gap item 2); the fitting range
  comes from the Shue read (Gap item 1). The row's `base_radii` (15)
  and `end_radii` (25) retire with the old tail, since Shue's surface
  sets the cross-section. [row verified @57fd93c6, unchanged @4506fb48]
- **The bow shock stops at the fit limit, and says so.** Jelinek's
  surface is drawn from the nose to 105 degrees from the nose (the
  +/- 7 h local-time envelope). At p = 2 nPa that is x = -7.8 R_E,
  R_yz = 29.0 R_E. Beyond it a paraboloid is unsupported (67 R_E at
  x = -100) and the real shock follows a Mach cone the paper does not
  model. The cut angle is SERVED with the shape parameters, per the
  "flaring parameter is SERVED" ruling above; the hover names it.
  [computed; reproduced 2026-09-10]
- **The seam at the nose, stated in the hover.** At p = 2 nPa, Bz = 0:
  Shue magnetopause nose 10.25 R_E; Jelinek bow shock nose 13.51 R_E;
  subsolar sheath 3.3 R_E where Jelinek's own pair gives 2.3 (his
  magnetopause at 2 nPa is 11.24). The two magnetopause noses differ by
  about 1 R_E against a fit scatter of about 0.7-0.8 R_E (Jelinek
  Fig. 7, per the read). The two hovers name both papers and the 1 R_E
  disagreement rather than let the pair read as one measurement.
  [computed; reproduced 2026-09-10]
- **Supersessions now fixed in number**, both called for above:
  `EARTH_MAGNETOPAUSE_STANDOFF_RADII` 10.0 -> 10.25 (Shue at the
  declared conditions; the served row's source string and the
  constant's own Source both say 10.2 while the value says 10.0 -- a
  drift inside one row, cleared by this).
  `EARTH_BOW_SHOCK_STANDOFF_RADII` 12.5 -> 13.51 (Jelinek at 2 nPa);
  the bow shock's Lugaz-midpoint derivation and the Farris & Russell
  "Model form" Note go. New store names, each with value / source /
  orrery_constant: Shue's eight coefficients; Jelinek's R0, eps and
  lambda for the bow shock (3); the bow-shock cut angle (105 deg,
  source: the paper's stated local-time envelope); and the MODEL
  CONDITIONS p = 2 nPa, Bz = 0 nT, v_sw = 400 km/s, status declared
  pending -- L-314, stated in every hover as the condition, not a
  measurement. Each pick's reason goes on its row: 2 nPa is the
  pressure the store's Shue Source already uses; the reason for
  400 km/s is not yet written. L-314 replaces the three with measured
  values. [constant verified @5fea1795; served row @57fd93c6]
- **Aberration is applied, declared.** Both fits are in ABERRATED GSE.
  The Sun direction is already in the Earth driver's payload
  (`payload.sun.dir`, from Earth's served osculating elements)
  [verified @57fd93c6]; the nose is rotated from it by
  atan(v_orbit / v_sw), about 4.3 deg at 400 km/s, in the ecliptic
  plane against Earth's motion. v_sw is one of the declared conditions
  above. **Tony-action (decide):** apply the 4.3 degrees at the
  declared 400 km/s (this record's choice, because both models are
  defined in the aberrated frame), or draw un-aberrated and say so in
  the hover.
- **The dipole tilt stays dropped** (ruling above). Shue is also
  symmetric about the aberrated x axis; nothing in either model draws a
  lean. The desktop drawing still applies it -- `magnetic_tilt_deg=11`
  in the `rotate_to_sunward` call at `earth_visualization_shells.py:785`
  [verified @5fea1795] -- so its removal stays in the Gap.
- **Arrival: both shells are drawer rows.** The Earth room's floor is
  6.155e-5 AU, the LEO outer edge [verified @57fd93c6]; the bow shock
  nose is ten times that. L-291's arrival policy applies without a
  new ruling. When either row is lit the view rescales to hold it,
  which is the existing drawer behaviour. `earth_geometry.js` already
  names the group as an ABSENCE in the drawer until a renderer
  exists; the new renderer replaces that line, and the i-panel's "The
  magnetosphere is not drawn yet" paragraph comes out in the same
  patch (EARTH_INFO_HTML, interactive.html). [both still present
  @4506fb48]
- **Still open, unchanged:** how `check_store_drift` treats a
  DIMENSIONLESS pointer (eps, lambda, alpha, the cut angle, Bz in nT,
  v_sw in km/s -- its unit table is all lengths). Read before the
  config change, per the bullet above.
- **Note:** landed 2026-09-10 by `patch_L305_amendment.py` (Claude
  Opus 5) from the Fable session's design record, which could not be
  pasted as written. Corrections, each named: the new solar-wind item
  is L-314, not L-313 (L-310's patch had already opened L-313 for
  recentering); the record's replacement Gap had dropped two lines of
  the old one, the tilt removal and the tail extent citation, and both
  are restored; Shue's alpha is tagged as not read; the standoff
  quotes are named by line (four quotes in three strings, where the
  record said two strings); the model conditions use
  provenance-discipline's "declared pending" status; a ruling quoted
  in words that do not appear above is paraphrased. The two earlier
  L-305 patches, a brief for the read and the reference, never landed
  and are superseded by the two bullets that open this group. The
  match with the WDS'10 numbers is not an independent check, because
  the reading session had this block open; Gap item 1 confirms the
  values against the PDF before the store takes them. L-315 records
  why the earlier patches refused.
**Gap:** (1) Read Shue et al. (1998) for the alpha line and its three
coefficients, and for the range of the crossings it was fitted on,
before any store name or renderer uses them; confirm Jelinek's six
values and the local-time envelope against the PDF in the same read.
Each row records its equation or table number and its access route.
**Tony-action (do):** keep the Jelinek PDF where that session can read
it. (2) Source the tail extent behind "past 1,000 R_E" (the served
magnetotail row's `_declared` text and L-291's hover requirement), or
remove the figure from both and note the gap. (3) Read
`check_store_drift` for dimensionless and non-length units and extend
its table before any new pointer is served. (4) In `constants_new.py`,
the single value home: supersede the two standoff constants, add the
store names listed above, remove the bow shock's Lugaz-midpoint
derivation and the Farris & Russell "Model form" claim, and clear its
Note's "the shell's 15 is a migration item" (line 825 of the shells
file already reads the store). (5) Port Shue (magnetopause, to
100 R_E) and Jelinek (bow shock, to the 105 deg cut) to
`planet_visualization_utilities.py` AND `gallery/feature_renderers.js`
in one patch, with the aberration from `payload.sun.dir` on the
gallery side and from the orrery's own Sun direction on the desktop
side; drop the tilt (`magnetic_tilt_deg=11`,
`earth_visualization_shells.py:785`). (6) Serve the shape parameters,
the cut angle, the declared conditions and the validity range in
`data/objects_config.json`; retire the magnetotail row's `base_radii`
and `end_radii`. (7) Hover text in `earth_visualization_shells.py`
for the new models, naming both papers and the seam:
`earth_magnetosphere_info` (standoff quotes at lines 729 and 734),
`magnetosphere_text` (792), `bow_shock_text` (847, and the Lugaz
midpoint sentence at 848, which goes) [lines @5fea1795]; the quotes
follow the constants on their own, the surrounding sentences do not.
Delete the drawer's magnetosphere absence and the i-panel paragraph.
(8) Live store-drift run reads MATCH by name for every new pointer;
then Mode 5 on both, phone first.
**Ref:** L-291, L-292, L-298 (the orrery-vs-exhibit gap, made concrete),
L-306, L-314, L-315, `constants_new.py`, `earth_visualization_shells.py`,
`planet_visualization_utilities.py`, `gallery/feature_renderers.js`,
`data/objects_config.json` (gallery), skills/interactive-exhibit/SKILL.md;
Jelinek et al. (2012), JGR 117, A05208, doi:10.1029/2011JA017252 (read
from the PDF, 2026-09-10); Shue et al. (1998), JGR 103:17691,
doi:10.1029/98JA01103; EARTH_DRIVER and EARTH_INFO_HTML in
interactive.html; gallery/earth_geometry.js (composeScene, the absence
list).
"""

L314_L315_BLOCKS = b"""#### [L-314] Live solar wind conditions for the magnetosphere shells (SWPC through the nightly builder)
<!-- L:314 status:OPEN upd:2026-09-10 section:A flag: rice:3/3/60/4 -->
- **Where this came from.** L-305's 2026-09-10 design round fixed the
  magnetosphere shells at DECLARED conditions -- p = 2 nPa, Bz = 0 nT,
  v_sw = 400 km/s -- because that is what the store can source today.
  Tony's ruling the same round: live if we can, later. This item is
  the later. (The round's record called it L-313; L-310 had already
  opened that handle for recentering.)
- **The shape is driven by three numbers the solar wind actually
  reports.** Shue takes Dp and Bz; Jelinek takes p; the aberration
  takes v_sw. NOAA SWPC publishes DSCOVR real-time solar wind (plasma:
  density, speed, temperature; mag: Bz in GSM) as JSON on
  services.swpc.noaa.gov [recalled, not fetched: confirm the endpoints
  and their fields when this opens]. Dynamic pressure is derived from
  density and speed (p = rho v^2, with the proton mass; the helium
  fraction is a declared assumption to state). The builder is the
  right home: it already fetches, stages, guards and swaps served data
  nightly (gallery-cache-builder), and a value that changes hourly
  should not be fetched by the visitor's browser.
- **What it changes for the visitor.** The two shells breathe day to
  day; each hover carries the measured p, Bz, v_sw AND their timestamp,
  replacing the "model condition" line. The i-panel gains one sentence
  saying the shells are drawn for the solar wind as measured at the
  build time named in the hover.
- **What it must not do.** Serve a value without its timestamp; fall
  back silently to the declared conditions when the fetch fails (Guard
  v2 quarantine and a stated fallback in the hover instead); or push
  the shells outside the models' validity ranges without saying so
  (Jelinek 0.6-11 nPa; Shue's Bz range, from L-305's Shue read). Out
  of range -> draw at the range edge and say so, per Show the Envelope.
- **Note:** RICE 3/3/60/4 -> 1.35 proposed, not confirmed. Effort is
  the builder's new data source plus the drift checker's non-length
  units (L-305 reads them first). Confidence 60: a feed the builder
  has never read, in a format not yet confirmed. Not started until
  L-305's renderer is on the phone.
**Gap:** the whole item; sequenced after L-305 closes.
**Ref:** L-305, tools/gallery_cache_builder.py, data/objects_config.json,
gallery/feature_renderers.js, skills/gallery-cache-builder/SKILL.md.

#### [L-315] Chained ledger patches refuse once the indexer runs between them (safe-file-editing field note)
<!-- L:315 status:OPEN upd:2026-09-10 section:A flag: rice:2/2/90/1 -->
- **What happened, 2026-09-10.** `patch_L305_brief.py` was
  fingerprinted against the ledger exactly as `patch_L310_ledger.py`
  left it, BEFORE `ledger_index.py` ran, and `patch_L305_2_citation.py`
  against the brief's output the same way -- while each of the three
  tells the operator to run `ledger_index.py` next. Doing that rewrites
  the index zone, and the next patch refuses. All three also hashed raw
  bytes, and `ledger_index.py` writes in text mode (`open(path, 'w')`),
  so on Windows the working copy goes CRLF and fails a raw-byte guard
  in any order. Reproduced on throwaway copies of `5fea1795`: the
  brief's expected md5 is the post-patch, pre-index ledger; after the
  indexer the same ledger reads `8f4baaa5` (LF). [verified @5fea1795]
- **What `patch_L305_amendment.py` did instead.** It fingerprints the
  LF-normalised text OUTSIDE the INDEX zone. A patch that never edits
  the index, and ends by telling the operator to regenerate it, does
  not depend on that zone; a guard that includes it refuses for a
  reason that is not about content -- Line Endings Are Not Content, one
  layer out. It writes the file back in the line endings it found.
- **Note:** this is method, so it goes into safe-file-editing as a
  field note at that skill's next bump, not to Tony as a ruling.
  `ledger_index.py` writing in binary mode and keeping the file's line
  endings would remove the CRLF half at its source; the gallery's
  text-mode writers had the same shape (L-236). RICE 2/2/90/1 -> 3.6
  proposed, not confirmed.
**Gap:** the field note, under the four-step skill-bump rule;
`ledger_index.py` preserving line endings, in the same session.
**Ref:** L-236, L-305, L-310, `ledger_index.py`, safe-file-editing 1.10
(Line Endings Are Not Content; Compare Content, Not Bytes).

"""

EDITS = [
# 1. header stamp, after L-310's
(b"""Module updated: September 10, 2026 with Anthropic's Claude Fable 5.1
(L-310 design ruled and built; L-313 opened), built on 5fea1795.
""",
b"""Module updated: September 10, 2026 with Anthropic's Claude Fable 5.1
(L-310 design ruled and built; L-313 opened), built on 5fea1795.
Module updated: September 10, 2026 with Anthropic's Claude Opus 5
(L-305 amended with the Jelinek 2012 read and Tony's Shue/Jelinek
ruling, corrected where it could not land as written; L-314 and L-315
opened; L-310's gallery push recorded), built on 5fea1795.
"""),
# 2. L-310: the gallery push
(b"""  a stub DOM in the sandbox. [render-gated]
**Gap:** Tony's Mode 5, phone and desktop, on the Earth room at full
""",
b"""  a stub DOM in the sandbox. [render-gated]
- **Pushed 2026-09-10** in the gallery at `4506fb48`: `navCameraStep`
  and the step handlers are present there and absent at `57fd93c6`.
  [verified @4506fb48]
**Gap:** Tony's Mode 5, phone and desktop, on the Earth room at full
"""),
# 3. L-305 upd stamp
(b"""<!-- L:305 status:OPEN upd:2026-09-08 section:A flag: rice:4/4/60/4 -->""",
b"""<!-- L:305 status:OPEN upd:2026-09-10 section:A flag: rice:4/4/60/4 -->"""),
# 4. L-305 body, Gap and Ref
(L305_OLD_GAP_AND_REF, L305_NEW_BODY_GAP_AND_REF),
# 5. L-314 and L-315, after L-312 (above L-278)
(b"""#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery""",
L314_L315_BLOCKS +
b"""#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery"""),
]

EDIT_NAMES = ["header stamp", "L-310 gallery push", "L-305 upd stamp",
              "L-305 body, Gap and Ref", "L-314 and L-315 opened"]

HANDOFF_TEXT = """# L-310 camera steps built; L-313 (recenter) opened

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
"""


def body_fp(lf):
    """md5 of LF text with the generated INDEX zone cut out, or None."""
    if lf.count(INDEX_START) != 1 or lf.count(INDEX_END) != 1:
        return None
    a = lf.index(INDEX_START)
    b = lf.index(INDEX_END) + len(INDEX_END)
    if b <= a:
        return None
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest()


def explain_unknown(lf):
    if b"- **Brief for the paper-read session (2026-09-10" in lf:
        return "patch_L305_brief.py has already been applied"
    if b"#### [L-313] Live solar wind" in lf:
        return "the design record's new item was pasted in as L-313"
    if b"gap item 1 closes by reading" in lf:
        return "the design record's L-305 text was pasted in by hand"
    return "the ledger differs from 5fea1795 in a way this patch does not recognise"


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(root, LEDGER)
    if not os.path.exists(fn):
        print("ERROR: not found: %s (run from the orrery repo root)" % fn); return 1
    docdir = os.path.join(root, "documentation")
    if not os.path.isdir(docdir):
        print("ERROR: no documentation/ folder beside the ledger -- is this the orrery root?"); return 1

    with open(fn, "rb") as f:
        raw = f.read()
    was_crlf = b"\r\n" in raw
    lf = raw.replace(b"\r\n", b"\n")
    tag = " [CRLF: the working copy uses Windows line endings; kept]" if was_crlf else ""

    fp = body_fp(lf)
    if fp is None:
        print("ERROR: %s has no single INDEX zone; nothing written" % LEDGER); return 1
    if fp == FP_FINAL:
        print("ERROR: this patch has already been applied (ledger matches its result); nothing written")
        return 1
    if fp == FP_HEAD:
        print("base: ledger text matches 5fea1795, without patch_L310_ledger.py's edits%s" % tag)
        for i, (old, new) in enumerate(L310_EDITS, 1):
            n = lf.count(old)
            if n != 1:
                print("ANCHOR FAIL: L-310 edit %d expected 1 match, got %d" % (i, n)); return 1
            lf = lf.replace(old, new)
        if body_fp(lf) != FP_L310:
            print("ERROR: L-310 edits did not reproduce patch_L310_ledger.py's result; nothing written")
            return 1
        print("ok  L-310 ledger edits applied (3), matching patch_L310_ledger.py exactly")
    elif fp == FP_L310:
        print("base: ledger text matches 5fea1795 plus patch_L310_ledger.py's edits%s" % tag)
        print("ok  L-310 ledger edits already present; not repeated")
    else:
        print("ERROR: %s -- %s; nothing written." % (LEDGER, explain_unknown(lf)))
        print("Undo is Discard Changes on %s in GitHub Desktop, which returns it to" % LEDGER)
        print("5fea1795; then Run this again. (If you made other ledger edits since")
        print("5fea1795 that you want to keep, stop and say so first.)")
        return 1

    for i, (old, new) in enumerate(EDITS):
        n = lf.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s expected 1 match, got %d" % (EDIT_NAMES[i], n)); return 1
        lf = lf.replace(old, new)
        print("ok  %s" % EDIT_NAMES[i])

    for h in (b"#### [L-313]", b"#### [L-314]", b"#### [L-315]"):
        if lf.count(h) != 1:
            print("ERROR: %s appears %d times after editing; nothing written" % (h.decode(), lf.count(h)))
            return 1
    bad = sum(1 for c in lf if c > 127)
    if bad:
        print("ERROR: %d non-ASCII byte(s) in the result; nothing written" % bad); return 1
    got = body_fp(lf)
    if got != FP_FINAL:
        print("ERROR: result %s does not match the tested result %s; nothing written" % (got, FP_FINAL))
        return 1
    print("ok  result matches the tested ledger text (md5 %s, outside the index)" % FP_FINAL)

    hf = os.path.join(root, HANDOFF)
    write_handoff = not os.path.exists(hf)
    if write_handoff:
        with open(hf, "wb") as f:
            f.write(HANDOFF_TEXT.encode("ascii"))
        print("ok  wrote %s (absent; the L-310 session's record, verbatim)" % HANDOFF)
    else:
        print("ok  %s present; left as is" % HANDOFF)

    out = lf.replace(b"\n", b"\r\n") if was_crlf else lf
    with open(fn, "wb") as f:
        f.write(out)
    print("stamped header: %s" % LEDGER)
    print("patch applied (%d bytes)" % len(out))
    print('next: run ledger_index.py -- expect "OK: 310 L-blocks parsed, no consistency problems."')
    return 0


if __name__ == "__main__":
    sys.exit(main())
