# HANDOFF v24 -- Bow Shocks + Magnetosphere Nest (Movement 1 complete) + Go-Forward

**Date:** June 2, 2026 (continued)
**Session model:** Claude Opus 4.8
**Supersedes:** v23 -- single running ledger; v23's shell-consolidation ledger
carried forward by reference (see "Carried forward from v23", below). Nothing
renumbered.
**Type:** MANIFEST EXECUTED + magnetosphere-nest correction. CODE CHANGED.
Nine files edited; all compile, ASCII-clean, LF; live-dispatch smoke ALL PASS.
Tony Mode-5 render + push PENDING (the remaining gate).
**Built on:** GitHub repo HEAD `a57aeb9` (branch main). Build = HEAD + this
delta. All 9 pre-edit bases confirmed byte-identical to repo HEAD this session
(Earth via fresh upload; the other 8 via /mnt/project, verified == repo).
**Integrator:** Tony Quintanilla

> **One document to follow for the bow-shock / magnetosphere / dipole-cone
> track.** v23 remains the running ledger for the shell-consolidation D-track
> (Phases A-D, Uranus U-items, provenance, on-the-horizon); those items are
> UNCHANGED this session and are carried forward intact. This session executed
> the MANIFEST (Movement 1) and, via Tony's Mode-5, discovered and fixed a
> separate magnetosphere-sizing defect the manifest did not cover. Ledger rule
> holds: nothing renumbered; new items appended with the next free numbers.

---

## 1. WHAT THIS SESSION DID

**Movement 1 (the manifest) -- bow shocks, IMPLEMENTED + verified.**
- Extracted ONE shared `create_bow_shock_shape(standoff, width, n_phi, n_theta,
  eccentricity)` into `planet_visualization_utilities.py` (between
  `create_magnetosphere_shape` and `create_sphere_points`). Conic-section model
  r = L/(1+e*cos a), L = standoff*(1+e); legacy paraboloid path retained ONLY as
  the one-time extraction regression test (eccentricity=None), not rendered.
- Four inner bodies (Mercury/Venus/Earth/Mars): inline paraboloid blocks replaced
  by the shared conic call inside the live `create_<body>_magnetosphere_shell`
  functions. Earth now renders the conic too (was going to stay paraboloid as a
  "regression anchor" -- Tony caught the conflation; the anchor's job is the
  extraction test, not the render).
- Four giants (Jupiter/Saturn/Uranus/Neptune): NEW conic bow shocks added inside
  their live magnetosphere builders. Uranus required care -- its builder returns
  `[geom_trace, info_trace]` (not `return traces`), so the first insertion landed
  in the wrong function (dead path); corrected to the real builder.
- Each shock: one `X: Bow Shock` legend entry, geometry `hoverinfo='skip'`, ONE
  cross info-marker at the nose carrying km AND AU (giants); single legendgroup
  toggles both. Eccentricity 1.05 illustrative (confirmed imperceptible by 3
  independent reviews; Winslow's Mercury 1.02 not separately rendered).

**Magnetosphere-nest correction -- NOT in the manifest; surfaced by Tony's
Mode-5.** Tony's render of Mercury showed the bow shock BEHIND the magnetosphere.
Root cause was not the shock (physically correct at 1.96 R_M) but the
magnetosphere: Mercury's ENTIRE param dict was Earth-scaled (sunward_distance 10,
equatorial 12, tail 100 -- a copy-paste from Earth, latent for ages). The
corrected, smaller shock simply stopped hiding the oversized magnetosphere. The
manifest's nest-check had covered only the giants; the original smoke test
inherited that gap (it checked the inner bodies' trace presence but not the
nest). Fixed:
- Smoke test UPGRADED with an all-eight nose-nest assertion (near-axis, so a
  tilted magnetosphere's off-axis flank is reported as a note, not a false fail).
- Magnetopause `sunward_distance` corrected on the broken bodies (sourced):
  Mercury full proportional rescale, Venus, Mars, Jupiter, Uranus.

**Verification:** all 9 compile, ASCII, LF; live-dispatch smoke (resolves each
builder via its CUSTOM_SHELLS string, inspects real traces) = ALL PASS, nest
holds for all eight. Neptune still prints its tilt-flank note (Movement-2 item,
not a regression). Container artifacts are ephemeral; the smoke test is
re-runnable from the repo (Layer 1 of the test protocol).

---

## 2. SOURCED NEST TABLE (values now in code; subsolar standoff in R_planet)

    Body      Magnetopause   Bow shock   Source(s)
    Mercury   1.45           1.96        Winslow et al. 2013 (both, MESSENGER)
    Venus     1.05           1.40        Zhang 2007 (IMB) / Shan 2015 (shock), VEX
    Earth     10             15          Shue 1997 (MP) / textbook (shock)
    Mars      1.29           1.64        Vignes et al. 2000 (both, MGS)
    Jupiter   65             82          Joy et al. 2002
    Saturn    22             27          Pilkington 2015 / Went 2011, Cassini
    Uranus    18             23.7        Slavin 1987 (MP) / Ness 1986 (shock), V2
    Neptune   26.5           34.9        Ness et al. 1989, Voyager 2

Mercury magnetosphere dimensions (rescaled, in R_M): nose 1.45; terminator/
equatorial 2.05 (= 1.45*sqrt(2), alpha=0.5 Shue fit); polar 2.0; tail base 2.7
(Winslow: ~2.7 R_M at 3 R_M downstream); tail far-end 3.4; drawn tail length 15.

---

## 3. REASONING TRAIL, TONY-CATCHES, LESSONS (process layer)

From the v23 design-session ADDENDUM (fold these into the archive):
- SHAPE self-correction: Claude's first instinct was an unsourced HEURISTIC conic
  (invented flank-gain factor); it flipped to the real cited conic-section model
  only because Tony twice declined the lean and said "what is the evidence."
  Sourcing it made it simpler AND citable. Fetched-vs-Recalled applied to
  GEOMETRY, not just numbers.
- ITEM 24 REFRAMED: the v23 premise (bow shock is the first consumer of the
  pole-vector producer) was physically off. The shocks are SUN-framed
  (rotate_to_sunward(sun_position)), self-contained, consume no pole work. The
  genuine first pole-frame consumer is the Uranus tilt cone (Movement 2).
- GEMINI BLIND CHECK: Claude's first cross-check prompt included Claude's own
  numbers; Tony caught that this anchors the reviewer and collapses two opinions
  into one. Rewritten to ask de novo -> the blind pass agreed 7/8 independently
  and surfaced real corrections. A cross-check is only a cross-check if the
  second opinion is independent.
- INNER-PLANET INVENTORY: Claude's first scope pass covered only the giants.
  Tony's "what about Mercury, Venus, Mars?" forced the sweep that found the
  Earth-copied 15*radius standoffs. The 8-copy duplication is what made the
  shared-shape extraction clearly correct, not optional.
- EARTH SHAPE / EARTH VALUE: Tony's catches (render uses the cited model;
  paraboloid is test-only) and judgment call (15 with a range tooltip).

New this session (append to archive):
- MAGNETOSPHERE SIZING FOUND VIA MODE-5, NOT TESTS. The bow-shock fix exposed a
  pre-existing Earth-scaled-magnetosphere bug. Tests were green; Tony's eyes
  caught it. Same shape as the v23 obliquity false-pass: the container test
  cannot see what the render shows.
- PROVENANCE DOES NOT CATCH RELATIONAL INVARIANTS. Asked why the provenance
  scanner missed Mercury's `10`: it checks per-claim SOURCING within a lookback
  window, not correctness, and structurally cannot check the NEST -- a relation
  between two numbers in two different files (magnetopause in one, shock in
  another). Provenance-clean != physically-consistent. The nest needed its own
  runtime assertion (now in the smoke test). Same family as compile-clean !=
  runs and cited != true.
- TRIPLE-AI CROSS-CHECK + TWO CLAUDE DIVERGENCES. Gemini (blind) caught real
  scale errors: Jupiter MP 50 too compressed, Uranus MP 21 too close to its
  shock, Mars shock 1.5 too low, Mercury tail over-flared. Claude diverged on two
  Gemini overreaches and held the convention: (a) Mercury's 0.2 R_M dipole offset
  is along the SPIN AXIS, perpendicular to the Sun line at ~0 obliquity, so the
  subsolar standoff stays ~1.45 from center (sqrt(1.45^2+0.2^2)=1.46), NOT
  Gemini's 1.65 (a linear-add slip); (b) the tilt-enclosure fix is "enclose the
  obstacle while the shock NOSE stays sunward," not "rotate the shock nose
  off-sun." Two later independent ChatGPT answers corroborated both Claude
  divergences and added: Jupiter is genuinely BIMODAL (Joy 2002 MP peaks ~63 and
  ~92), so a single Jupiter number is slightly false to the physics. Lesson:
  use the reviewer for parameter correction; keep geometry discipline; "good
  reviewer / better editor" only worked because disagreements were visible in
  language where Tony could adjudicate.
- REPO IS GROUND TRUTH; THE TWO PROJECT STORES CANNOT BE TRUSTED FOR "CURRENT."
  The recurring stale-Earth file was a duplicate upload shadowing the current one
  (the /mnt/project snapshot served the older twin); project_knowledge_search
  also served a persistent GHOST (palomas_orrery_before_none.py, Oct 2025, gone
  from filesystem and repo, surviving a full project-knowledge replacement).
  Resolution validated end-to-end: pull build-target files from GitHub at HEAD,
  SHA-pin the base, demote /mnt/project + project knowledge to orientation/search
  only. Encoded in protocol v3.26 (Session-Start Repo Pull and Snapshot
  Integrity [CRITICAL]; Context Priority re-ranked: repo at tier 2). Project
  knowledge to be expunged and re-synced from the repo via the GitHub connector
  (push-then-sync; one-time delete of old manual uploads to avoid in-store twins).

One-liner for the archive: "The manifest records what was decided; the deciding
was a double-helix, not a monologue -- and the two biggest catches (the
magnetosphere sizing, and two reviewer overreaches) came from eyes and
skepticism, not from any test passing."

---

## 4. MOVEMENT 2 QUEUE (next session -- the dipole cone + spin axis)

The manifest's deferred half, now with this session's additions folded in. This
is where the pole-frame work (orient_to_planet_pole) gets its FIRST real
consumer.
- **Uranus / Neptune dipole tilt cone + spin axis** (the original Movement 2):
  visualize the ~59 deg / ~47 deg dipole tilt; first consumer of the pole-vector
  producer revived in v23 (U3).
- **Uranus/Neptune bow-shock tilt enclosure.** The tilted magnetosphere envelope
  pokes sunward of the shock on the flank (Neptune confirmed by smoke + Gemini as
  a real artifact, not to preserve). FIX: enclose the tilted/offset obstacle --
  widen the shock flaring and/or apply the obstacle's offset -- while keeping the
  shock NOSE sunward (it faces the solar wind; do NOT rotate the nose off-sun).
  Design conversation, not a parameter tweak.
- **Mercury +0.2 R_M northward dipole offset.** Translate the magnetosphere (and
  shock) shell north by 0.2 R_M to represent Mercury's defining N-S asymmetry
  (large exposed southern cusp; Anderson 2011). Subsolar standoff stays 1.45.
- Inputs ready: magnetic_tilt values (Uranus 60 per v23 U1; Jupiter ~10; Earth
  ~11), sun_position threading, the pole-frame producer.

---

## 5. DEFERRED PRECISION / LEDGER ITEMS (low-risk; not blocking)

- **Jupiter compressed/expanded toggle.** Joy 2002 MP is bimodal (~63 / ~92 R_J).
  Current single value 65 is a defensible compact representative; the honest
  representation is a toggle (feature, not a number). Bow shock left at 82; if
  pinning Jupiter to one Joy fit, verify Joy's bow-shock mean directly (the
  independent reviews said ~84) before changing -- do not flip on AI assertion.
- **Earth citation upgrade.** Two reviews prefer MP ~10 / BS ~14.6 (Fairfield/
  Shue) over flat "15 textbook." Accuracy refinement; nest unaffected.
- **Per-body bow-shock eccentricity** (e.g. Mercury 1.02). Optional; 1.05
  illustrative is confirmed visually fine.
- **Inner-four bow-shock hover text** still says "radii" only (no km/AU), unlike
  the giants. Add km/AU for consistency with the AU convention if desired.
- **Dead-code annotation** (standing Tony instruction): annotate, do not remove,
  dead inline code met while editing (e.g. dead `rotate_points` import in
  uranus_visualization_shells.py). Removal is the deferred D3 sweep.

---

## 6. LIVE FLAGS / ASSUMPTIONS

- `orrery_rendering.py` (home of `create_info_marker`, `rotate_to_sunward`) was
  read from the /mnt/project snapshot; only CALLED, not edited. Signatures used:
  `create_info_marker(x, y, z, color, text, legendgroup, customdata=None,
  fill_color=None, border_color='red')`; `rotate_to_sunward(px, py, pz,
  center_position, sun_position)`. Re-confirm against a fresh pull if either is
  edited.
- Conic flare at e=1.05 is wider than the legacy paraboloid (physically correct).
  The `0.92` asymptote-cap in `create_bow_shock_shape` is the knob if Mode-5 finds
  it too broad.
- Plotly Scatter3d ignores marker.line.width (#4118) -- border WIDTH is
  non-functional; contrast is via fill color (standing fact).

---

## 7. FILES + INTEGRATION

Changed this session (build on repo HEAD a57aeb9):
- `planet_visualization_utilities.py` -- shared `create_bow_shock_shape` + credit.
- `mercury_visualization_shells.py` -- conic shock; magnetosphere rescaled.
- `venus_visualization_shells.py` -- conic shock; magnetopause 1.05.
- `earth_visualization_shells.py` -- conic shock + range note (built on the
  AUTHORITATIVE upload; the snapshot was the stale twin).
- `mars_visualization_shells.py` -- conic shock; shock 1.64, MPB 1.29 (Vignes).
- `jupiter_visualization_shells.py` -- new conic shock; magnetopause 65.
- `saturn_visualization_shells.py` -- new conic shock (magnetopause unchanged).
- `uranus_visualization_shells.py` -- new conic shock (live builder); MP 18.
- `neptune_visualization_shells.py` -- new conic shock; magnetopause 34 -> 26.5.
- `smoke_bow_shock.py` -- live-dispatch test with all-eight nest assertion +
  loaded-file audit (run from a CLEAN dir, never the archive sandbox).

Test protocol: `TEST_PROTOCOL_bow_shock.md` (Layer 0 file integrity, Layer 1
smoke, Layer 2 full-app launch on Windows, Layer 3 Mode-5).

Sequence to close: Tony Mode-5 (shock outside magnetosphere for all 8; Neptune
flank the one known exception) -> push -> record new HEAD SHA -> expunge +
GitHub-sync project knowledge.

---

## 8. CARRIED FORWARD FROM v23 (by reference; unchanged this session)

The v23 running ledger remains authoritative for the shell-consolidation D-track:
U-items (U1 magnetic tilt=60, U2 convention, U3 belt/ring orient_to_planet_pole
CLOSED, U4 copy-paste fixes), N14 (Miranda real 4.2 deg tilt, tooltip note),
provenance Phase 1 (Tier-1 = 0), dead-code tags, and the broader on-the-horizon
backlog (Phase D sun_position threading + magnetic_tilt wiring, comet perihelion
presets, Spacecraft Mission Explorer, Food Insecurity module, ERA5/Western
Heatwave, gallery pipeline, provenance audit). None touched this session.
(If a single merged file is wanted, fold the v23 ledger body in -- ask and it
will be done.)

---

## 9. NEXT-SESSION PRIORITIES

1. Confirm Tony's Mode-5 verdict on Movement 1; apply any flank-flare (0.92) or
   value tweaks it surfaces; record the post-push HEAD SHA as the new base.
2. Movement 2: the dipole tilt cone + spin axis (first pole-frame consumer),
   folding in the Uranus/Neptune tilt enclosure and Mercury north offset.
3. Optionally clear the deferred precision items (Section 5) as a batched pass.

Session-start: pull build targets from repo HEAD, SHA-pin, build on repo/upload
only (v3.26). Run the smoke from a clean dir and read its loaded-file audit.
