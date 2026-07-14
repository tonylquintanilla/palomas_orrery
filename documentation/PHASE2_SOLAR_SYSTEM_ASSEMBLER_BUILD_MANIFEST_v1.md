# PHASE 2 SOLAR SYSTEM ASSEMBLER BUILD MANIFEST v1

**Type:** BUILD MANIFEST / EXECUTABLE DESIGN CONTRACT  
**Mode:** Mode 2 agentic implementation, with Mode 5 visual gates and Mode 7 relay discipline  
**Parent:** L-079 shared assembler architecture  
**Co-evolving harness:** L-080  
**Design source:** `PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.2.md`  
**Pinned orrery base:** `8bce8354b6c9ae37b1e941f536cfc6f0a0a435c8`  
**Pinned gallery base:** `e864fd426a6bcffc478fe5ed9452a4dfc9159766`  
**Status:** Ready for implementation after Tony ratifies the decision flags in S1

---

## S0. Purpose and governing rule

This manifest defines the implementation contract for the Phase 2 static solar-system assembler in the interactive gallery. It is not a review, a code patch, or a restatement of the handoff. It converts the closed pre-design into an ordered build with explicit module boundaries, data contracts, failure behavior, golden artifacts, visual gates, and characterization requirements.

The governing rule is:

> The assembler may compose only data already present in the served gallery cache. It must never query Horizons, mutate the cache, infer unsupported objects, or silently substitute a different frame.

The gallery repository is the implementation home. The desktop orrery is a computation and visual-convention reference, not a runtime dependency.

All implementation claims in this manifest are tagged either `[verified @<sha>]` or `[carried]`.

---

## S1. Decision flags for Tony

### D1. Introduce an immutable `AssemblyContext`

**Status:** RECOMMENDED FOR RATIFICATION

The assembler should normalize a scene request into one immutable context before rendering. This is an architectural addition beyond the handoff, but it does not expand user-facing scope.

The context should contain at minimum:

```text
scene_spec
resolved_date
resolved_center_slug
resolved_center_record
selected_object_records
cache_snapshot_id
frame_groups
feature_requests
camera_policy
axis_policy
warnings
```

The purpose is to prevent center resolution, date clamping, feature dispatch, and frame interpretation from being recomputed independently by multiple renderers. It also gives L-080 a deterministic object to characterize.

**Decision requested:** Ratify `AssemblyContext` as the single normalized input to all render stages.

### D2. Reject mixed incompatible frames in Phase 2

**Status:** RECOMMENDED FOR RATIFICATION

A single scene may contain multiple objects only when they are already represented in a common served frame, or when a specifically supported composition policy exists. The assembler must not revive general vector transforms as a normal path.

For Phase 2, this means:

```text
heliocentric + heliocentric: allowed
parent-relative siblings with same center_slug: allowed
Pluto + Charon in pluto_barycenter: allowed
arbitrary heliocentric + parent-relative mixture: rejected unless rendered as separate view
```

This is the operational form of the handoff's "transforms retired except as fallback" conclusion.

**Decision requested:** Ratify hard rejection over silent transformation for unsupported mixed-frame scenes.

### D3. Golden files store semantic fingerprints, not full Plotly JSON

**Status:** RECOMMENDED FOR RATIFICATION

L-080 should not initially compare entire Plotly figure JSON. Full JSON is too sensitive to harmless Plotly ordering and version changes. Store a normalized semantic fingerprint plus selected numeric samples and a human-approved screenshot.

**Decision requested:** Ratify semantic characterization as the primary automated baseline, with screenshots as Mode 5 evidence.

---

## S2. Verified base facts

The gallery repository is pinned at `e864fd426a6bcffc478fe5ed9452a4dfc9159766`. The pinned tree contains `data/`, `documentation/`, `gallery/`, and `tools/`; `tools/` contains `gallery_cache_builder.py` and `test_gallery_cache_builder_offline.py`. `[verified @e864fd426a6bcffc478fe5ed9452a4dfc9159766]`

The orrery repository is pinned at `8bce8354b6c9ae37b1e941f536cfc6f0a0a435c8`, and its tree contains the referenced desktop modules including `celestial_objects.py`, `idealized_orbits.py`, `orbit_data_manager.py`, `orbital_elements.py`, `palomas_orrery.py`, and the planetary shell modules. `[verified @8bce8354b6c9ae37b1e941f536cfc6f0a0a435c8]`

`data/objects_config.json` declares itself the single authority for the gallery cache builder and distinguishes `canonical_center` from `center_slug`. `[verified @e864fd426a6bcffc478fe5ed9452a4dfc9159766]`

The configured Phase 2 objects at the pinned gallery SHA include Earth, Jupiter, Saturn, Moon, Io, Titan, Pluto, Charon, Apophis, Voyager 1, Encke, and Halley. `[verified @e864fd426a6bcffc478fe5ed9452a4dfc9159766]`

Earth is heliocentric and carries `van_allen_belts` and `atmosphere_shell`; Jupiter is heliocentric and carries `magnetosphere` and `ring_system`; Saturn is heliocentric and carries `ring_system`. `[verified @e864fd426a6bcffc478fe5ed9452a4dfc9159766]`

Moon, Io, and Titan are served parent-relative with centers Earth, Jupiter, and Saturn respectively. `[verified @e864fd426a6bcffc478fe5ed9452a4dfc9159766]`

Pluto and Charon are both served relative to `@9` with `center_slug: pluto_barycenter`. `[verified @e864fd426a6bcffc478fe5ed9452a4dfc9159766]`

Voyager 1 is configured as `full-arc`, starts at `1977-09-06`, uses a 7-day glide backbone, includes Jupiter and Saturn event windows, and uses Douglas-Peucker thinning tolerance `0.02 AU`. `[verified @e864fd426a6bcffc478fe5ed9452a4dfc9159766]`

Encke and Halley are pinned to Horizons records `90000091` and `90000030`, with Tp-anchored conics. `[verified @e864fd426a6bcffc478fe5ed9452a4dfc9159766]`

Phase 2 is cache-only, static, solar-system-only, and intentionally narrower than the desktop. `[carried]`

L-046 and L-104 remain outside this assembler build except for the generic `event_link` rendering contract proven by artifact 7. `[carried]`

---

## S3. Scope

### In scope

The implementation shall provide a static scene assembler capable of:

1. Loading and validating scene specifications.
2. Resolving selected objects against `objects_config.json` and served cache data.
3. Resolving a legal center and frame policy.
4. Selecting a date from the served window.
5. Building object markers, analytic orbit traces, spacecraft arcs, shells, hover content, event markers, axes, and camera state.
6. Returning a Plotly figure and a deterministic assembly report.
7. Producing the seven golden artifacts.
8. Building L-080 characterization alongside those artifacts.

### Explicitly out of scope

The implementation shall not add live Horizons access, free-form object IDs, animation, Studio preset authoring, NEO close-up composition, spacecraft flyby close-ups, arbitrary frame conversion, per-shell user toggles, orbit-cache management, or Phase 3-5 domains.

The assembler shall not modify the cache builder's fetching logic unless an implementation-blocking defect is discovered. Any such defect must be routed back to Tony as a separate decision.

---

## S4. Proposed module architecture

The filenames below are recommendations. The implementer may adjust names, but not responsibilities, without recording the change.

### `gallery/assembler/models.py`

Owns immutable data models and validation types:

```text
SceneSpec
ResolvedObject
ResolvedCenter
AssemblyContext
AssemblyWarning
AssemblyReport
ArtifactFingerprint
```

No Plotly imports. No file I/O.

### `gallery/assembler/catalog.py`

Loads `data/objects_config.json`, validates schema expectations, indexes records by slug, and exposes read-only lookup functions.

Required behavior:

```text
unknown slug -> explicit error
missing required field -> explicit configuration error
duplicate slug -> startup failure
unsupported category -> explicit configuration error
```

### `gallery/assembler/cache_reader.py`

Reads served cache records only. It must not import `astroquery`, cache-builder fetch functions, or desktop modules.

Required outputs:

```text
object metadata
available date interval
position sample at or around requested date
analytic orbit or conic payload when present
spacecraft arc payload when present
provenance metadata
```

### `gallery/assembler/resolver.py`

Normalizes a `SceneSpec` into `AssemblyContext`.

Responsibilities:

```text
validate object slugs
resolve date policy
resolve center
partition frame groups
reject unsupported compositions
resolve feature availability
record warnings
freeze the normalized context
```

### `gallery/assembler/render_objects.py`

Builds object markers and object labels from resolved records.

### `gallery/assembler/render_orbits.py`

Builds analytic orbit or comet-conic traces. It consumes cache payloads and does not derive new Horizons data.

### `gallery/assembler/render_spacecraft.py`

Builds full spacecraft arcs and current-position markers from served arc data.

### `gallery/assembler/render_features.py`

Dispatches configured features such as atmosphere, belts, magnetosphere, and rings.

The dispatch key is the gallery `features` vocabulary, not desktop module names.

### `gallery/assembler/render_events.py`

Builds perihelion and `event_link` markers. Event links are presentation metadata; they do not trigger alternate live-scene assembly.

### `gallery/assembler/presentation.py`

Owns hover composition, legend grouping, camera, axes, title, annotations, and mobile-safe layout.

### `gallery/assembler/assemble.py`

The sole public assembly entry point:

```text
assemble_scene(scene_spec, repository) -> AssemblyResult
```

`AssemblyResult` contains:

```text
figure
context
report
fingerprint
```

### `gallery/assembler/errors.py`

Owns stable exception classes suitable for tests and UI messages.

### `tests/assembler/`

Contains unit, contract, integration, and golden-artifact characterization tests.

---

## S5. Scene specification contract

Phase 2 should accept a deliberately small scene specification. The canonical form is:

```json
{
  "content_type": "static",
  "domain": "solar_system",
  "date": "2026-07-11",
  "objects": ["earth"],
  "center": "sun",
  "view_id": null,
  "event_links": []
}
```

Required fields are `content_type`, `domain`, `date`, `objects`, and `center`.

`content_type` must equal `static` in Phase 2.

`domain` must equal `solar_system`.

`objects` must be non-empty, unique, and known to the catalog.

`center` is a slug-level presentation center. It must resolve to the same served frame required by all included objects, unless the selected `view_id` invokes one of the explicitly supported multi-view patterns.

`view_id` is not the unresolved general `preset_id` mechanism. It is an internal assembler view selector for a closed set of Phase 2 patterns, initially:

```text
standard
pluto_wide
pluto_barycenter_detail
```

This naming avoids reopening OQ-4.

---

## S6. Assembly pipeline

The implementation shall execute these stages in order.

### Stage A: Parse

Parse the scene request and reject malformed input before loading data.

### Stage B: Catalog resolution

Resolve all slugs through the gallery catalog. No fallback to desktop catalogs.

### Stage C: Cache resolution

Load the served cache metadata and payload for each selected object.

### Stage D: Date resolution

Use exact-date data when present. If the cache contract allows nearest-date selection, select deterministically and emit a warning containing the requested and resolved date. Never extrapolate a planetary position merely to satisfy a missing date.

### Stage E: Frame resolution

Confirm that all selected records can be rendered under one supported frame policy. Reject illegal mixtures before creating Plotly traces.

### Stage F: Context freeze

Construct the immutable `AssemblyContext`. No later renderer may change object selection, center, frame, or date.

### Stage G: Geometry

Build object markers, analytic orbits, conics, arcs, shells, and event markers in deterministic layer order.

### Stage H: Presentation

Apply hover, legend, axes, camera, title, and annotations.

### Stage I: Characterization

Generate `AssemblyReport` and `ArtifactFingerprint` from the completed figure and frozen context.

### Stage J: Validation

Run structural invariants before returning the result.

---

## S7. Global invariants

Every successful assembly must satisfy all applicable invariants.

### Data invariants

Every rendered object maps to exactly one configured slug.

Every rendered geometry item records its source object slug and source cache record.

No rendered point may originate from a network request.

No requested object may be silently dropped.

### Frame invariants

Every trace declares a `frame_slug` in internal metadata.

Every object marker in a single view must use the resolved context frame.

The center marker is at the numerical origin of that view.

Parent-relative moon scenes use the parent as origin without a synthetic post-fetch translation.

Pluto-barycenter detail uses `pluto_barycenter` as origin.

### Determinism invariants

Identical scene spec plus identical cache snapshot produces the same semantic fingerprint.

Trace ordering is stable.

Legend group ordering is stable.

Warnings are stable and sorted.

### Presentation invariants

The selected center is visually identifiable.

Object hover identifies name, date, center/frame, distance from center when available, and provenance.

Decorative shells never obscure the primary object marker.

Event-link markers are distinguishable from astronomical position markers.

### Failure invariants

An unsupported scene fails before partial rendering.

A missing cache payload fails with an object-specific diagnostic.

A missing optional feature emits a warning only when the base astronomical object can still be rendered correctly.

---

## S8. Layer order

The assembler shall use one stable layer order:

```text
1. reference grid / axes helpers
2. analytic orbit or conic traces
3. spacecraft full arcs
4. volumetric or surface shells
5. rings and belts
6. event markers
7. object markers
8. center marker
9. labels and annotations
```

The center marker and selected object markers must remain interactable above shells.

---

## S9. Feature dispatch contract

Feature rendering is data-driven from `objects_config.json`.

Initial required feature keys are:

```text
van_allen_belts
atmosphere_shell
magnetosphere
ring_system
```

Each feature renderer shall accept:

```text
AssemblyContext
ResolvedObject
object position in resolved frame
feature-specific style defaults
```

Each feature renderer shall return zero or more Plotly traces plus feature metadata for the assembly report.

Unsupported feature keys are configuration errors in test and development modes. In production, they must be surfaced as visible assembly warnings and telemetry, not silently ignored.

Feature renderers must not import Tkinter GUI state.

---

## S10. Hover contract

Hover content shall be composed from normalized fields rather than copied wholesale from desktop strings.

Required fields when available:

```text
name
category
date
center
frame
distance from center
velocity or speed
orbit or trace type
source attribution
```

Comet hover should identify that the displayed curve is Tp-anchored analytic geometry.

Voyager hover should distinguish the spacecraft marker from the served historical arc.

Event-link hover must name the linked static exhibit and clearly indicate that selecting it leaves the live interactive scene.

---

## S11. Camera and axes contract

Camera policy is presentation-level and must not change geometry.

The default static scene uses a deterministic orthographic camera unless an artifact-specific view requires perspective.

Axis ranges shall be computed from the actual assembled geometry with a stable padding function. Hard-coded ranges are allowed only for named view policies such as `pluto_barycenter_detail`.

L-040 remains open. Therefore this build must isolate axis policy behind one function so later Studio/web dtick and range controls can be added without rewriting geometry assembly. `[carried]`

---

## S12. Golden artifact 1 - Earth alone

### Objective

Prove the complete minimal path from scene spec to figure for one configured planet.

### Scene

```text
objects: earth
center: sun
view_id: standard
```

### Required output

Earth marker, heliocentric orbit/conic as supported by the served payload, Sun center marker, Earth atmosphere shell, Earth Van Allen belts, hover, axes, and camera.

### Acceptance criteria

The context resolves to `heliocentric` and center `sun`.

Earth appears exactly once as the primary object marker.

The feature report records both configured Earth features.

No network-capable module is imported during assembly.

The figure passes structural validation.

A Mode 5 comparison confirms position, scale, and shell placement are credible relative to the desktop reference.

### L-080 increment

Create the first semantic fingerprint schema and Earth golden baseline.

---

## S13. Golden artifact 2 - Jupiter and Saturn

### Objective

Prove multi-object heliocentric composition and feature dispatch across two planets.

### Scene

```text
objects: jupiter, saturn
center: sun
view_id: standard
```

### Required output

Both object markers, both orbit traces, Sun center marker, Jupiter magnetosphere, Jupiter rings, Saturn rings, shared axes, hover, and legend grouping.

### Acceptance criteria

Both objects share one heliocentric context.

Jupiter and Saturn are not recentered independently.

Jupiter's magnetosphere is attached to Jupiter's resolved position.

Ring-system dispatch produces one logical ring feature per configured body, regardless of internal trace count.

Legend entries do not multiply merely because a feature uses several Plotly traces.

### L-080 increment

Add trace-group counts, feature attachment checks, and duplicate-legend checks.

---

## S14. Golden artifact 3 - Moon, Io, Titan

### Objective

Prove direct parent-relative fetching and center resolution without general transforms.

### Output form

This artifact is a set of three separately assembled scenes, not one mixed-frame scene:

```text
Moon centered on Earth
Io centered on Jupiter
Titan centered on Saturn
```

### Acceptance criteria

Each context resolves to `parent-relative`.

Each scene's parent is at the origin.

No heliocentric translation step is called.

The selected moon position comes from its served canonical center.

Attempting to combine Moon, Io, and Titan into one unsupported common view produces a clear frame-compatibility error rather than three unrelated origin-centered traces.

### L-080 increment

Add frame-policy fingerprints and negative tests for unsupported mixed-parent scenes.

---

## S15. Golden artifact 4 - Halley and Encke

### Objective

Prove grouped comet rendering with two independently pinned Horizons records.

### Scene

```text
objects: halley, encke
center: sun
view_id: standard
```

### Required output

Two object markers at the selected date, two Tp-anchored conics, perihelion markers when supplied by the served payload, clear comet hover, and no trajectory-line substitution.

### Acceptance criteria

Halley resolves to record `90000030`.

Encke resolves to record `90000091`.

Both conics are identified as analytic/Tp-anchored in report metadata.

No bare designation is used at render time.

A pre-build or build-session gate confirms Halley's cache payload was produced by a successful dry-run/first-build path; the assembler itself must not perform that check against Horizons.

### L-080 increment

Add conic type, anchor, pinned-record, and perihelion-marker checks.

---

## S16. Golden artifact 5 - Voyager 1

### Objective

Prove spacecraft full-arc rendering from the served gallery cache.

### Scene

```text
objects: voyager_1
center: sun
view_id: standard
```

### Required output

Voyager 1 current marker, full served historical arc, Sun center marker, hover, and arc provenance.

### Acceptance criteria

The assembler consumes the already-thinned served arc and does not rerun Douglas-Peucker thinning.

The arc begins no earlier than the configured authoritative start.

The report identifies `trace_policy: full-arc`.

Arc ordering is chronological.

The current marker corresponds to the final applicable served sample.

No future predicted segment is invented.

### L-080 increment

Add chronological ordering, endpoint, arc-point-count range, and event-window preservation fingerprints.

---

## S17. Golden artifact 6 - Pluto and Charon

### Objective

Port the verified two-view desktop pattern without inventing dual-fetch composition.

### Required views

#### `pluto_wide`

A wide solar-system presentation in which Pluto is shown in the broad context supported by the gallery's available data and view policy.

#### `pluto_barycenter_detail`

A separate detail scene containing Pluto, Charon, and a barycenter marker at the origin.

### Acceptance criteria

The detail view resolves both bodies in `pluto_barycenter` frame.

The barycenter marker uses the general barycenter presentation convention, not a Pluto-only conditional.

Pluto and Charon positions are not transformed from heliocentric coordinates in the detail view.

The two views are separate assembly results or explicitly separated view panels; they are not forced into a single coordinate scale.

### L-080 increment

Add named-view fingerprints, barycenter-origin checks, and two-body relative-distance checks.

---

## S18. Golden artifact 7 - Halley plus `event_link`

### Objective

Prove the generic bridge from a live interactive scene to a static Gallery Studio exhibit.

### Scene

```text
objects: halley
center: sun
event_link: Halley perihelion exhibit
```

### Required output

Halley marker and conic, perihelion marker, and a coincident or intentionally offset `event_link` marker that resolves to the correct static exhibit.

### Acceptance criteria

The astronomical perihelion marker and link marker remain semantically distinct even if visually coincident.

The event link target is validated as a relative gallery route or approved absolute gallery URL.

The event link does not alter the live scene specification.

No Apophis close-up, OQ-4 precedence logic, or Studio authoring behavior is introduced.

The pattern is data-driven and reusable for another comet without renderer changes.

### L-080 increment

Add event-target, coincidence/offset, marker-role, and route-safety checks.

---

## S19. L-080 characterization harness

L-080 begins as soon as Earth alone renders. It is not a preliminary phase and not postponed until all artifacts exist.

### Harness layers

#### Layer 1: Pure unit tests

Cover schema validation, catalog lookup, date policy, center resolution, frame compatibility, feature dispatch lookup, route validation, and fingerprint normalization.

#### Layer 2: Structural figure tests

Assert trace roles, stable order, legend groups, center origin, object count, feature attachment, hover fields, and absence of `NaN`/infinite coordinates.

#### Layer 3: Semantic golden fingerprints

Each artifact stores a compact JSON fingerprint containing:

```text
artifact_id
scene_spec_hash
cache_snapshot_id
resolved_date
resolved_center
resolved_frame
object_slugs
trace_roles
trace_count_by_role
feature_keys
legend_groups
coordinate_bounds
selected numeric samples
warnings
```

Numeric samples must use documented tolerances.

#### Layer 4: Mode 5 screenshot evidence

Store or reference one human-approved screenshot per golden artifact/view. Screenshot comparison is advisory at first; semantic tests are blocking.

#### Layer 5: Mainloop-suppression and import tests

Prepare the existing proposed fixture so importing assembler modules cannot start Tkinter, open a browser, or write files.

### Fingerprint stability rule

A fingerprint update requires an explicit reason recorded in the commit message or handoff. The test suite must make accidental baseline rewrites difficult.

---

## S20. Test matrix

The minimum blocking matrix is:

```text
catalog schema tests
cache reader contract tests
exact-date and nearest-date tests
unsupported-date tests
center resolution tests
mixed-frame rejection tests
feature dispatch tests
hover contract tests
event route validation tests
Earth integration test
Jupiter/Saturn integration test
three parent-relative integration tests
Halley/Encke integration test
Voyager integration test
Pluto wide and detail integration tests
Halley event-link integration test
all seven fingerprint tests
no-network import test
no-write assembly test
```

The existing cache-builder offline suite must remain green. The assembler tests are additive; they do not replace builder validation.

---

## S21. Failure messages

Failures should be written for a human integrator. Examples:

```text
Object 'moon' is stored relative to 'earth', but this scene resolves center 'sun'.
Phase 2 does not transform parent-relative data into heliocentric coordinates.
Build a separate Earth-centered Moon scene or choose a supported view policy.
```

```text
No served cache payload is available for 'halley' on or near 2026-07-11.
Run the gallery cache builder's required dry-run and first-build procedure.
The assembler will not query Horizons.
```

```text
Scene mixes frame groups: earth=heliocentric, moon=parent-relative(earth).
No Phase 2 composition policy supports this mixture.
```

---

## S22. Build sequence and gates

### Gate 0 - Pin and inspect

Reconfirm both repository HEADs. If either differs from this manifest's base, inspect the diff affecting `data/objects_config.json`, served cache schema, builder outputs, gallery routing, or desktop reference modules. Update verification tags where necessary.

### Gate 1 - Skeleton and contracts

Create package structure, models, errors, catalog loader, cache reader interface, and tests. No Plotly assembly beyond a smoke fixture.

### Gate 2 - Earth vertical slice

Implement the complete pipeline for Earth. Perform Mode 5 confirmation. Freeze the first L-080 fingerprint.

### Gate 3 - Shared feature composition

Add Jupiter and Saturn. Resolve legend grouping and feature attachment before proceeding.

### Gate 4 - Frame discipline

Add Moon, Io, and Titan as separate parent-relative scenes. Add mixed-frame negative tests.

### Gate 5 - Small-body analytic path

Add Halley and Encke. Confirm cache provenance and conic metadata.

### Gate 6 - Spacecraft path

Add Voyager 1 using served arc data only.

### Gate 7 - Named multi-view path

Add Pluto wide and barycenter detail views.

### Gate 8 - Event bridge

Add Halley `event_link` marker and route validation.

### Gate 9 - Full characterization

Run all unit, integration, fingerprint, no-network, no-write, and builder-regression tests. Complete Mode 5 evidence for every artifact.

### Gate 10 - Documentation and ledger handoff

Document public scene-spec fields, supported view IDs, supported feature keys, failure behavior, and deferred scope. Route ledger closure or follow-up recommendations to Tony.

---

## S23. Definition of done

Phase 2 assembler implementation is complete when:

1. All seven golden artifacts render from the served cache at the pinned or updated verified HEAD.
2. Every artifact passes its structural and semantic acceptance criteria.
3. Every artifact has Mode 5 visual confirmation.
4. L-080 contains stable characterization for all artifacts and views.
5. No assembly path can reach Horizons or mutate cache files.
6. Unsupported frame combinations fail clearly.
7. Feature dispatch is data-driven.
8. Pluto wide/detail remains a two-view pattern.
9. `event_link` proves live-to-static navigation without importing deferred Studio design.
10. The cache-builder offline suite remains green.
11. ASCII-only and LF requirements are met.
12. A final implementation handoff records actual filenames, deviations, test commands, visual evidence, and the final SHAs.

---

## S24. Deferred work remains deferred

The following are not blockers for closure:

```text
L-040 Studio/web axis controls
L-046 Studio preset-authoring refactor
L-104 curated NEO/spacecraft links and close-up exhibits
animation
live Horizons
free-form object entry
Phase 3 stars
Phase 4 hybrid scenes
Phase 5 Earth-system scenes
spacecraft flyby close-up composition
Apophis close-encounter live assembly
```

A discovered opportunity may be recorded, but must not be silently included in this build.

---

## S25. Implementer latitude

The implementer has broad latitude over internal code organization, naming, and Plotly construction technique, provided the following are preserved:

```text
cache-only boundary
immutable normalized context or an equivalent single-resolution mechanism
hard frame compatibility checks
seven artifact order
data-driven feature dispatch
semantic characterization
separation of Pluto views
separation of live assembler from Studio authoring
```

Any change to those constraints is a design change and must be routed to Tony.

---

## S26. Final relay format

The implementation handoff should report:

```text
final orrery SHA
final gallery SHA
files added
files modified
commands run
unit test results
integration test results
builder regression result
artifact-by-artifact status
Mode 5 evidence locations
manifest deviations
open risks
ledger recommendations
```

Claims must continue to use `[verified @<sha>]` and `[carried]`.

---

## S27. Manifest conclusion

The handoff's central resolution is sound: Phase 2 does not need a new universal transform engine or a unified close-up composition system. The assembler should be built as a deterministic cache-to-scene compiler with strict frame discipline, data-driven feature dispatch, named view policies for the few legitimate special presentations, and a characterization harness that grows one golden artifact at a time.

The only architectural addition proposed here is the immutable `AssemblyContext` and its semantic fingerprint. Together they turn a collection of render functions into an inspectable, testable assembly system without expanding the user-facing scope.
