# Phase 2 Solar System Assembler - Artifact 1 (Earth alone): As-Built

**Type:** BUILD (as-built record, one artifact of seven)
**Session:** Mode 7 collegial relay (Opus implements; Tony integrates + Mode 5 gate)
**Author:** Claude Opus 4.8, July 2026
**Base SHAs at build time:** orrery `e95116f7` (port sources; verified identical
to the manifest's `c10a424` base), gallery `e864fd42` (served cache schema).
**Repo HEADs at write time:** orrery `6fc52b9a`, gallery `f89d83c4`. The
final-state modules listed below must be current at gallery HEAD after this
session's push -- pin the post-push SHA here on commit.
**Contract:** `documentation/PHASE2_SYNTHESIS_MANIFEST_v2.md` (executable),
`PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.3.md`, `MASTER_PLAN_INTERACTIVE_GALLERY.md`.

---

## 1. Status

**Artifact 1 (Earth alone) is CLOSED.** All three parts of its acceptance gate
(manifest S6) are green:

- L-080 structural checks pass in CPython -- confirmed on Tony's Windows machine
  and in Linux, identical fingerprint.
- Renders via Pyodide, no console errors.
- Mode 5 (Tony's eyes) -- confirmed ("perfect"), after the aspect/camera fixes.

The first golden L-080 fingerprint, `abbd01094852b57f`, is locked as the
baseline every later artifact regresses against.

This is the floor case and the visual template: artifacts 2-7 inherit its hover
format, marker taxonomy, colors, layer order, axis/scene convention, and legend
behavior.

---

## 2. What was built (file inventory)

All under `gallery/assembler/` in the gallery repo (`tonyquintanilla.github.io`),
inside the existing served `gallery/` folder. Pure stdlib (math, json, hashlib,
dataclasses, typing) -- imports nothing Pyodide cannot supply; touches no files
or network. ASCII-only, LF, credit-lined.

| File | Responsibility |
|------|----------------|
| `errors.py` | Stable exception classes (FrameRejectionError, UnsupportedInPhase2Error, MissingCachePayloadError, OutOfServedWindowError, UnknownObjectError). |
| `models.py` | Frozen dataclasses: SceneSpec, ResolvedObject, FeatureRequest, AssemblyContext (frozen truth); AssemblyResult; closed ROLE_* trace vocabulary. |
| `catalog.py` | Indexes objects_config.json by slug (operates on a parsed dict; no I/O). |
| `cache_reader.py` | Reads the served coverage_index.json: snapshot id, served_window, scene_features, per-object record, require_orbit_payload. |
| `render_orbits.py` | **Position engine.** solve_kepler, propagate_marker (M0->E->nu), sweep_conic (geometric 360-pt ellipse), build_orbit_traces (polyline + single info-marker). Mean-elements path present, first used at artifact 4. |
| `render_objects.py` | build_object_marker (circle), build_label (white text), build_center_marker (square-open if barycenter). km+AU hover. |
| `render_spacecraft.py` | Stub (NotImplementedError) -- wired at artifact 5 (Voyager 1 arc). |
| `render_events.py` | Stub -- wired at artifacts 4/7 (comet perihelion / event_link). |
| `resolver.py` | SceneSpec -> frozen AssemblyContext: ISO->JD, frame rejection, served_window bound (warns while null), feature dispatch, unsupported/unknown-field policy. |
| `presentation.py` | Colors, layer ordering, and the layout: dark theme + cube + equal ranges + uniform dtick + 3/4 camera, ported from the orrery's build_scene. |
| `assemble.py` | `assemble_scene()` orchestration -> AssemblyResult (Pyodide-safe figure dict + feature-dispatch report). |
| `harness/fingerprint.py` | L-080 semantic fingerprint + compare(). |
| `harness/golden/artifact_1_earth_alone.json` | The locked golden fingerprint. |
| `tests/test_artifact1_earth.py` | End-to-end CPython test against the real served cache. |
| `__init__.py` x3 | Package markers (assembler, harness, tests). |

Dev render page: `gallery/solar_system_earth_test.html` (sibling to assembler/,
in the served gallery/ folder).

---

## 3. Architecture decisions (load-bearing)

- **Output is a Pyodide-safe Plotly figure dict** `{data, layout}`, not a
  go.Figure. The assembler needs no plotly-Python and no numpy; plotly.js
  renders the dict directly. This is the S2 boundary rule taken literally and
  is what keeps the package importable in Pyodide with zero extra wheels.
- **Features render in JavaScript, always.** The Python assembler RESOLVES and
  REPORTS which features apply (van_allen_belts, atmosphere_shell for Earth) as
  data in `result.report["features"]`; it never builds a shell/ring trace. (This
  reverses a v1 synthesis merge error -- manifest S0.) Shells appear on screen
  at artifact 2 once the JS feature layer exists (gated on F1).
- **AssemblyContext is frozen** after the resolver. Date, center, frame, and
  object selection are decided once; nothing downstream reinterprets them.
- **Frame rejection before any trace.** An object whose stored_center != the
  scene center raises FrameRejectionError (e.g. Moon in a heliocentric scene).
  Phase 2 renders each object in its own stored frame only; no silent transforms.
- **Position marker is PROPAGATED, never as_of_today.** as_of_today is the
  engine cross-check only, so marker and orbit cannot disagree.

---

## 4. Position engine and ground-truth validation

Handoff S9: the orrery draws orbit SHAPE by geometric true-anomaly sweep (static
ellipse) and gets the position MARKER from live Horizons. The web has no
Horizons, so the marker is Kepler-propagated from the served osculating snapshot
(M0_deg at epoch_jd -> M(t) -> solve E -> true anomaly -> conic xyz). Elements
are ecliptic J2000 heliocentric; positions computed in AU; hover shows km via
km = AU * 149597870.7.

**Validation:** propagating Earth's osculating snapshot to its stored
`as_of_today.t` reproduced the stored (x, y, z) to **0.0 km (2.6e-11 AU) =
machine precision.** This verifies the conic + Kepler math, the ecliptic-J2000
frame, and the AU<->km units against ground truth. Constants: AU_KM =
149597870.7, K_GAUSS = 0.01720209895 (sqrt(GM_sun), AU^1.5/day).

---

## 5. Scene / visual convention (final values)

Ported from the orrery's `visualization_utils.build_scene` + the `plot_objects`
layout envelope, so the web view matches the desktop:

- `aspectmode: "cube"`, the SAME symmetric range `[-R, R]` on all three axes.
- **R = largest orbital radius x 1.25** (25% buffer; `data_half_range` buffer
  param). Earth alone -> R ~ 1.27 AU.
- **Uniform grid dtick** from `calculate_grid_dtick` (ported
  `_calculate_grid_dtick`; ~6 clean gridlines; 0.5 AU for Earth). Same on all axes.
- **Dark theme:** black paper/plot/backplanes, gray grid, white fonts, light-gray
  data annotation ("Data: JPL/NASA Horizons"). Label text is white (was defaulting
  to black -> invisible on black).
- **Default camera: 3/4 perspective** (eye 1.25,1.25,1.25, up z) so all three
  dimensions read at the start. (The orrery's own default is top-down orthographic
  via get_default_camera; the web assembler opens on the angled view by Tony's
  choice. Rotatable to top-down with the mouse. One-line change to revert.)
- `domain: x=[0.2, 1.0], y=[0.0, 1.0]` -- clears the left legend.
- Marker taxonomy: circle = celestial object; cross = info-only; square-open =
  barycenter. Single-info-marker pattern on the conic (geometry hoverinfo=skip;
  one cross carries the AU+km hover).

None of Section 5's styling touches the fingerprint (see S6).

---

## 6. L-080 harness and the golden fingerprint

The fingerprint is **semantic, not full Plotly JSON**. It is built from the
frozen AssemblyContext AND the rendered traces, so both logical and visual
regressions are catchable. Fields: artifact_id, scene_spec_hash,
cache_snapshot_id, resolved_epoch_jd, resolved_center, resolved_frame,
object_slugs, trace_role_counts, feature_keys, legend_groups, coordinate_bounds,
position_samples, position_tolerance, warnings.

**Locked golden:** `artifact_1_earth_alone.json`, scene_spec_hash
`abbd01094852b57f`, at epoch 2026-07-13. Reproduces byte-identically in CPython
and in-browser Pyodide -- it characterizes the scene, not the machine.

**Position tolerance** defaults to 0.001 (0.1%); it is a parameter, not a
constant -- Tony to tune (manifest S9.1).

**What does NOT move the fingerprint** (free restyles): colors, line width,
marker size, camera, aspectmode, dtick, axis buffer/range, theme, title text.
**What DOES move it:** changes to which traces exist, legend grouping, or
positions/bounds. Those need a deliberate golden regen with the reason recorded
in the ledger and commit message (manifest S8).

---

## 7. Dev render page

`gallery/solar_system_earth_test.html` -- THROWAWAY dev harness, not the shipped
exhibit. Loads Pyodide (v314.0.2, lazily on the button = the S5/S7 consent gate),
writes the assembler package into the Pyodide FS, fetches the real served cache,
calls assemble_scene, and renders the figure dict with Plotly.js (2.35.2). Shows
the in-browser fingerprint for cross-check. Header reads "Paloma's Orrery".
Includes a **date picker** that feeds the epoch and re-propagates (moving the
date visibly walks Earth around its orbit -- the Kepler engine, live).

**Run (must be over HTTP, not file://):**
```
cd <gallery repo root>
python -m http.server 8000
```
then open `http://localhost:8000/gallery/solar_system_earth_test.html`.

**Run the CPython test:**
```
cd gallery
python -m assembler.tests.test_artifact1_earth
```
(from the gallery/ directory so `assembler` imports; the test self-locates the
repo root and reads the real data/ files).

**Serving locality (important):** artifact 1 is served from Tony's own machine,
NOT from GitHub Pages. `python -m http.server 8000` starts a local server;
`localhost:8000` resolves to 127.0.0.1, so the page, the assembler package, and
the data/ files are all read from local disk -- no internet round-trip for
project files. Two edges to that:
- The page still fetches two assets from public CDNs: Pyodide
  (cdn.jsdelivr.net, v314.0.2) and Plotly.js (cdn.plot.ly, 2.35.2). Only project
  files are local; the runtime and plotting library come from CDNs. (F4, the
  ship gate, deploys the slim self-hosted plotly wheel to remove that dependency
  for the public page.)
- Committed/pushed to the repo is separate from served. The files are pushed
  (that is how the SHA round-trips work), but GitHub Pages is NOT rendering this
  page to the public. It stays a local-only render until deployed as a real page
  -- deliberately downstream of the local Mode 5 render, at the F4 ship gate.

---

## 8. Manifest deviations (2, both intentional)

1. **Output contract:** figure dict + report rather than a go.Figure (keeps the
   package Pyodide-clean). One-module change at the assemble boundary if a
   go.Figure is ever wanted.
2. **served_window null:** the resolver warns rather than rejects when the bound
   is absent (it cannot enforce a bound it does not have). The warning is carried
   in the fingerprint. Populating served_window is a small builder change to ride
   with F1.

---

## 9. Open items / next session

- **Artifact 2 (Jupiter + Saturn)** is next, gated on **F1**. F1 is builder work
  in the gallery repo (feature params move into objects_config.json; the builder
  derives feature_configs.json instead of writing it empty), so it runs under the
  gallery-cache-builder layered gate (offline suite from a clean checkout,
  --dry-run, then a real build), NOT the assembler pre-test.
  - **Tony decision (manifest S9.4), not yet made:** the exact config shape for
    feature params -- per-object inside objects_config.json (recommended; matches
    the existing source-of-truth pattern) vs a sibling file.
  - Once F1 lands, the JS feature layer draws shells/rings and artifact 2's
    features (and Earth's, retroactively) appear on screen.
- **Info card (#4 from this session)** deliberately held to F1. Integration path:
  serve info_dictionary.py text as JSON (same serve-data/render-JS pattern), then
  a Plotly click handler on the object marker opens the gallery's "i" encyclopedia
  card. Log as its own ledger item when F1 opens.
- **served_window population** rides with F1 (see deviation 2).
- **Section 9 still open:** harness tolerance (0.1% placeholder), comet
  perihelion-marker default-on (Mode 5 call at artifact 4), page naming.
- **Page identity / shipped design:** the dev page is throwaway; the real page
  name and design are Tony's (F4 is the ship gate: plotly wheel + attribution).
- **Later artifacts:** 3 (Mars+Jupiter+Saturn / mean elements begin), 4 (Halley --
  needs F3 real --first-build + mean-elements conic + perihelion), 5 (Voyager 1
  full arc), 6 (Pluto/Charon barycenter, view_id), 7 (comet + event_link, F2).

---

## 10. Field notes (recommend into skills / ledger)

- **aspectmode "data" collapses a near-planar orbit edge-on.** Solar-system
  scenes need "cube" with equal axis ranges (orrery build_scene already does
  this). The Earth orbit rendered as an invisible sliver + axis X until this was
  fixed. -> orrery-coding-conventions.
- **scatter3d line has no `dash` attribute** (2D-only). Distinguish mean vs
  osculating orbits by width, not dash, to keep the console clean. -> conventions.
- **Text/label traces default to black** -- invisible on the dark theme. Set
  textfont color explicitly. -> conventions.
- The manifest pinned orrery `c10a424` but HEAD had moved to `e95116f`; all seven
  port-source files were byte-identical, so the claims held. Gate 0 discipline
  caught and cleared it.

---

## 11. Verification performed

- Both repo HEADs re-pinned via git ls-remote at session start.
- Gate 0: 7 orrery port-source files byte-identical c10a424 vs HEAD.
- Served schema confirmed at gallery e864fd42 (served_window null, 11 objects no
  halley key, osculating fields, as_of_today km, features dispatch keys).
- Position engine validated against Earth as_of_today: 0.0 km.
- Test `test_artifact1_earth`: T1-T5 all pass (CPython + Windows).
- Figure dict is strict-JSON (allow_nan=False) clean, 5 traces.
- py_compile + ASCII/LF + credit-line gates: clean on all modules.
- Fingerprint stable at `abbd01094852b57f` across every layout change this session.

---

## 12. Ledger recommendations

- L-080 detail block updated (harness now live; golden locked; status OPEN;
  co-evolves through artifacts 2-7). Block drafted this session -- run
  ledger_index.py after pasting.
- New L-item for the deferred info card (open when F1 opens).
- Field notes (S10) into orrery-coding-conventions (bump its version, SHA-stamp).
- Consider rescoring L-080 RICE (effort down, confidence up now that the harness
  is built and proven) -- Tony's call.

---

*As-built written July 2026 with Anthropic's Claude Opus 4.8. Artifact 1 of the
seven golden artifacts; Mode 5 closed by Tony Quintanilla.*
