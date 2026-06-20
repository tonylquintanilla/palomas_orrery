# HANDOFF -- Dipole Cones: Mercury, Earth, Jupiter, Saturn
# Tony Quintanilla, PE | Claude Opus 4.8 | June 20, 2026
# Base SHA: 5b294c8 -> Dipole pushed: 08f9831

---

## What was done this session

Built magnetic dipole cones for Mercury, Earth, Jupiter, and Saturn,
extending the existing Uranus/Neptune primitive. Closes L-009 (dipole
cluster) and L-006 (Mercury offset). Design-first per v29 scoping: D1-D7
resolved in conversation before any code, then a four-edit build, all gates
green container-side, Mode-5 confirmed by Tony.

### Sourced data (Gemini de-novo, June 18; cone values rounded to display precision)

| Body    | Cone tilt | Offset            | Source                                              |
|---------|-----------|-------------------|-----------------------------------------------------|
| Mercury | 0.0 (axis)| 0.19 R_M N        | Anderson et al. 2011, MESSENGER (Science 333, 1859) |
| Earth   | 9.6       | 0.085 R_E N       | Alken et al. 2021, IGRF-13 (Earth Planets Space 73, 49) |
| Jupiter | 10.3      | 0.12 R_J          | Connerney et al. 2022, JRM33 (JGR Planets 127(2))   |
| Saturn  | 0.0 (axis)| 0.045 R_S N       | Dougherty et al. 2018, Cassini Grand Finale (Science 362) |

Precision discipline: Jupiter stored as 10.3 (source is 10.31 close-in JRM33;
planet-wide integrated dipole reads ~9.6 -- both disclosed in hover). Saturn
offset 0.045 is the midpoint of the measured 0.04-0.05 R_S (disclosed). A cone
projection cannot honor finer precision, so the rendered value is honest about
what it resolves while the exact source figure rides in the hover note.

### Design decisions resolved (D1-D7)

- **D1** offset_fraction: builder reads `dip.get('offset_fraction', 0.0)`;
  Uranus/Neptune omit it -> 0.0 -> render unchanged. Backward compatible.
- **D2** Mercury/Saturn (tilt 0): option (a). At tilt 0 the cone half-angle ->
  0, so sin_t zeroes the nappe rim and sweep-arc radius alike -- the cone
  PHYSICALLY collapses to a line. Builder emits only the generator line
  (= offset spin axis) + info marker; collapsed nappes and sweep arrows are
  skipped. The honest envelope of a zero-tilt dipole IS the axis; a faked wider
  cone would be the cite-over-recalled failure class.
- **D3** Earth offset: axial 0.085 R_E + hover disclosure that the true center
  is also displaced laterally (~540 km, secular variation, unmodeled).
- **D4** Jupiter offset: axial 0.12 R_J + hover disclosure (true shift toward N
  hemisphere and System III active longitude; rotation phase unmodeled).
- **D5** Saturn narrative: option (a) + Cowling-theorem paradox note
  (helium-rain axisymmetric filter). High educational value.
- **D6** CUSTOM_SHELLS wiring: dipole_cone entry per body, mirroring
  Uranus/Neptune, each with a sourced tooltip.
- **D7** L-006: closes naturally -- Anderson 2011's 0.19 R_M IS the +0.2 item.

PROVENANCE GATE (L-009): all tilts/offsets sourced from peer-reviewed mission
data; recalled values retired. Citations carried in the PLANET_DIPOLE 'source'
key (the form Uranus/Neptune already clear).

### The four edits (3 files; palomas_orrery.py NOT touched)

1. **planet_visualization_utilities.py**
   - PLANET_DIPOLE: +4 entries (offset_fraction, offset_note, note, source).
   - build_dipole_cone_traces: (a) apex shifted northward along +pole by
     offset_fraction * body_radius; (b) tilt < 0.5 deg degenerate branch
     (generator line + marker only); (c) per-body hover (offset disclosure,
     Jupiter dual-reading, Saturn midpoint/Cowling, Mercury/Saturn degeneracy);
     (d) tilt format %.0f -> %.1f (integer format would erase Earth 9.6 vs
     Jupiter 10.3 -- both round to "10").

2. **shell_configs.py** -- dipole_cone CUSTOM_SHELLS entry for the four bodies,
   per-body sourced tooltips.

3. **smoke_dipole_cone.py** -- tilt-aware: BODIES = all six; OMITTED = [Mars];
   trace-count expectation 8 (tilted) vs 2 (degenerate); rim-arc/sweep checks
   guarded for tilt~0; docstring updated. (The harness existed but its
   hardcoded expectations -- 8 traces, Earth/Jupiter/Saturn in OMITTED --
   would have inverted the moment the cones were added. "The harness exists"
   is not "the harness is correct for the new state.")

**palomas_orrery.py: no change.** Dispatch is generic in both pipelines
(static planet_visualization.py and animated collect_perframe_elements);
dipole_cone rides the any-shell-checked trigger with no checkbox. v29 step 5
("add/verify checkbox vars") resolved to a verified no-op.

### Why no checkbox: dispatch map (verified, not assumed)

- pole = M[:,2] from create_planet_transformation_matrix = IAU north pole
  (z_basis built from planet_poles RA/Dec, rotated to ecliptic). All four
  targets in planet_poles, all dec > 0 -> +pole = geographic north -> "northward
  offset" verified, not assumed. (Uranus dec -15.1 is the IAU-convention quirk;
  not touched.)
- Static + animated dispatch both iterate CUSTOM_SHELLS and dispatch by the
  builder string; no body/element names hardcoded.

---

## Verification

| Gate | Result |
|------|--------|
| py_compile (3 files) | PASS |
| ASCII-only / LF | PASS (no CRLF, no non-ASCII) |
| smoke_dipole_cone.py on pushed HEAD 08f9831 | PASS (6 cones; 4 tilted 8-trace, 2 degenerate 2-trace; tilt on-pole within 1e-14; sense correct; Mars omitted) |
| Offset magnitude + northward | PASS (Mercury .19 / Earth .085 / Jupiter .12 / Saturn .045; Uranus/Neptune 0.0) |
| Provenance Tier-1 | 0, no dipole flags (container over-report run; Tony-side run with exceptions file is authoritative) |
| Mode-5 (Tony's eyes) | PASS -- Earth/Jupiter cones rhyme spin+sweep; Mercury/Saturn read as axis shifted north |

---

## Ledger items closed

| L-#   | Status change | Notes                                                  |
|-------|---------------|--------------------------------------------------------|
| L-006 | -> DONE -> C  | Mercury 0.19 R_M offset (Anderson 2011) = the +0.2 item |
| L-009 | -> DONE -> C  | Dipole cluster: Mercury/Earth/Jupiter/Saturn built + Mode-5 confirmed |
| --    | Tooling       | smoke_dipole_cone.py: tilt-aware, six bodies           |

---

## Process lesson (for the protocol)

**Complete the round trip before "go."** Session-Start treats repo-HEAD as
ground truth "by construction" because Tony's loop pushes before a session.
This session was the exception: local work was un-pushed, so the construction
did not hold and the build was cut one base behind the real working tree. The
fix is not more Claude-side checking -- it is the precondition: the pre-session
push completes the round trip (commit + push + SHA match), and THEN we say go.
When local work is in flight, the uploaded working copy is the authoritative
base, not repo-HEAD.

Corollary on the failure signature: `git apply` "patch does not apply" here was
NOT corruption or CRLF -- it was double-application. The full files had already
been dropped into the working tree, so the patch could not find its original
context to splice into. Recovery was the uploads diff: local == pushed ==
gate-passed build, all LF.

---

## SHAs

- Dipole build: built on **5b294c8** -> pushed at **08f9831** ("dipole update").
- Follow-on (LOCAL, not yet pushed at handoff time): dipole_cone_4bodies.patch
  relocated to documents/ -- next push moves HEAD past 08f9831.

---

## Next-session scoping (carried from v29)

### Comet MAPS per-frame tail animation -- L-056

- MAPS is explicitly skipped in the per-frame engine: palomas_orrery.py L2324
  (`if name == 'MAPS': continue`). Exclusion was caution per ADDENDUM_phase4
  decision 1, not technical incompatibility. Builder (build_comet_tail_traces)
  is shared with all comets; static path (plot_objects) already handles MAPS.
- Prerequisite: read documentation/ADDENDUM_phase4_decisions.md decision 1 --
  the "two-site" warning / "partition design" may be the frame-1 tail doubling
  bug (C2a). MAPS may need the same frame-1 guard.
- Scope: remove the L2324 gate, verify MAPS enters per-frame allocation, smoke
  with MAPS + comet-tails checkbox on, verify no frame-1 doubling, check both
  pipelines, update L-056 (other residuals -- O2/O3 wording, apsidal em-dashes
  -- remain).
- Risk: low. Shared builder; exclusion was caution.

### Other open (from v29 ledger)

- L-015: ~78 dead _info imports remain (broader sweep deferred).
- L-025 / L-020: confirming greps (likely-done items, scriptable closure).
- L-014 / L-017: D.Feature-C design decisions (asteroid-belt migration,
  globals() rewiring).
