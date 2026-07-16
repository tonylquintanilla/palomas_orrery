# Phase 2 F1 — Feature-Config Serving Pipeline Build Manifest v0.1

**Type:** EXECUTABLE BUILD CONTRACT  
**Implementation target:** Claude Opus or equivalent coding agent  
**Prepared for:** Tony Quintanilla  
**Source design:** `PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md`  
**Prompt source:** `FABLE_MANIFEST_PROMPT_F1_v0.2.md`  
**Required repository pins:** gallery `953c650edc8dbd35ab11ec1720f8283987d63901`; orrery `58dfa5205d492711d6163560d8c3fa15f6c60b9c`  
**Status:** READY FOR IMPLEMENTATION, SUBJECT TO THE SOURCE-DRIFT GATE IN §1

---

## 0. Contract purpose

This manifest converts the converged F1 design into two independently buildable and independently reviewable implementation units. It is not permission to revisit the settled physics, schema, feature naming, F1a/F1b phasing, 0.5° tolerance, moon-exclusion rule, or Jupiter feature substitution. It does grant implementation latitude inside those decisions.

The implementation must leave `resolver.py` and `cache_reader.py` untouched, must not add the uncertainty-envelope UI, must not implement Apophis encounter anchoring, must not add `event_link` or the info-card work, and must not introduce sun-oriented features.

Chunk A ports feature configuration and serves it. Chunk B measures two-body trust and emits F1a trust metadata plus the conservative global `served_window`. Each chunk must have its own commit, test evidence, and rollback boundary.

---

## 1. Mandatory repository pin and source-drift gate

The handoff was authored against gallery `953c650edc8dbd35ab11ec1720f8283987d63901` and an earlier orrery revision. Tony has now supplied orrery `58dfa5205d492711d6163560d8c3fa15f6c60b9c`. Therefore, all orrery source citations in the handoff are hypotheses until re-verified at the new pin.

Before editing any file, run:

```powershell
git -C <gallery-repo> fetch origin
git -C <gallery-repo> checkout --detach 953c650edc8dbd35ab11ec1720f8283987d63901
git -C <gallery-repo> status --short
git -C <gallery-repo> rev-parse HEAD

git -C <orrery-repo> fetch origin
git -C <orrery-repo> checkout --detach 58dfa5205d492711d6163560d8c3fa15f6c60b9c
git -C <orrery-repo> status --short
git -C <orrery-repo> rev-parse HEAD
```

Both worktrees must be clean and both resolved SHAs must match exactly. If either SHA is unavailable, stop and report `PIN FAILURE`.

Then re-locate, by symbol rather than line number, every upstream source named below:

| Feature | Required source symbol at orrery pin |
|---|---|
| Earth atmosphere | `SHELL_CONFIGS['Earth']['atmosphere']` and `SHELL_CONFIGS['Earth']['upper_atmosphere']` |
| Earth Van Allen belts | `CUSTOM_SHELLS['Earth']['magnetosphere']` and `create_earth_magnetosphere_shell` belt-only geometry |
| Jupiter ring system | `create_jupiter_ring_system` |
| Jupiter radiation belts | `create_jupiter_radiation_belts` |
| Saturn ring system | `create_saturn_ring_system` |

Record the current file path and line range for every symbol in the implementation report. Compare all numeric values against §3 of the handoff. If a value changed, do not silently choose either version. Stop that feature only, mark it `SOURCE DRIFT`, quote the old and new values, and ask Tony which source controls. Unaffected features may continue.

Also re-verify at the gallery pin that the following architectural claims still hold: `derive_served` writes an empty `feature_configs.json`; top-level `served_window` is currently `None`; `event_link` is still hardcoded `None`; the object catalog contains the expected category field; `solve_kepler` and `propagate_marker` exist in `gallery/assembler/render_orbits.py`; and the current resolver tolerates unknown additive fields. Any contradiction is a manifest-blocking discrepancy for the affected chunk.

---

## 2. Non-negotiable design decisions

The output feature schema is object-keyed configuration assembled from each object's `features` mapping. Earth receives `atmosphere_shell` and `van_allen_belts`. Jupiter receives `ring_system` and `radiation_belts`; the old conceptual `magnetosphere` name is not served. Saturn receives `ring_system`. Halley and Encke receive explicit empty mappings.

The trust method is empirical. It compares two-body propagation against a fetched Horizons check vector at epoch plus Δ, using the worse of two check samples and a safety factor `guard_k = 2.0`. The global angular tolerance is `0.5°`. Per-object trust metadata is additive in F1a. The existing global `served_window` is populated from the minimum measured `window_days` among in-scope objects where `category != "moon"`. Planets, dwarf planets, asteroids, and comets are not excluded merely because they may have short or unusual windows.

The one-orbit quantity is an outer cap for planets, not a minimum guarantee. Satellite handling remains measured and per-object, even though moon-category objects are excluded from the interim global minimum. Comets are bounded to the current apparition. Spacecraft do not participate in Kepler trust measurement.

---

# BUILD UNIT A — Feature-config porting and serving

## A1. Allowed files

The expected edit surface is:

```text
data/objects_config.json
tools/gallery_cache_builder.py
<existing Layer-1 offline test files only>
```

A different file may be edited only when necessary to preserve an existing schema validator or test fixture. Explain every extra file in the implementation report. Do not edit client rendering, resolver, cache reader, event-link, or info-card code.

## A2. Catalog migration

Convert the participating objects' `features` values to mappings with the exact keys below. Preserve unrelated object fields byte-for-byte where practical and preserve established JSON formatting conventions.

### A2.1 Earth

Serve:

```json
"features": {
  "atmosphere_shell": {
    "type": "shell_layers",
    "layers": [
      {
        "name": "lower_atmosphere",
        "radius_fraction": 1.05,
        "color": "rgb(150,200,255)",
        "opacity": 0.5,
        "n_points": 20
      },
      {
        "name": "upper_atmosphere",
        "radius_fraction": 1.25,
        "color": "rgb(100,150,255)",
        "opacity": 0.3,
        "n_points": 20
      }
    ]
  },
  "van_allen_belts": {
    "type": "warped_belt_system",
    "distance_unit": "body_radius",
    "inner_belt_distance": 1.5,
    "outer_belt_distance": 4.5,
    "belt_thickness": 0.5,
    "n_rings": 5,
    "n_points_per_ring": 80,
    "z_warp_fraction": 0.2,
    "colors": {
      "inner": "rgb(255,100,100)",
      "outer": "rgb(100,200,255)"
    }
  }
}
```

The implementer may adjust purely structural field names such as `n_points_per_ring` only if the repository already has a settled feature-config naming convention that clearly controls. Numeric values, feature keys, semantics, and units may not change. Any structural adjustment must be documented and covered by a schema test.

Do not port the complete Earth magnetosphere. This unit is belt-only.

### A2.2 Jupiter

Serve `ring_system` as four named components with kilometer units:

| Component | Inner radius km | Outer radius km | Thickness km |
|---|---:|---:|---:|
| main | 122500 | 129000 | 30 |
| halo | 100000 | 122500 | 12500 |
| amalthea_gossamer | 129000 | 182000 | 2000 |
| thebe_gossamer | 129000 | 226000 | 8600 |

Serve `radiation_belts` with `belt_distances = [1.5, 3.0, 6.0]` body radii, `belt_thickness = 0.5` body radii, `n_rings = 5`, and `n_points_per_ring = 80`.

The Jupiter radiation-belt config must contain no Sun vector, solar longitude, bow-shock parameter, or other sun-dependent datum. It replaces the prior feature name `magnetosphere` for this serving scope.

### A2.3 Saturn

Serve `ring_system` as seven named components with kilometer units:

| Component | Inner radius km | Outer radius km |
|---|---:|---:|
| d_ring | 66900 | 74500 |
| c_ring | 74658 | 92000 |
| b_ring | 92000 | 117500 |
| a_ring | 122340 | 136800 |
| f_ring | 140210 | 140420 |
| g_ring | 166000 | 175000 |
| e_ring | 180000 | 480000 |

Do not invent thickness, opacity, color, or texture values unless the source function at the pinned orrery SHA provides them and the existing gallery schema has a defined place for them. Any optional values ported beyond the table must be separately identified as source-derived additions.

### A2.4 Halley and Encke

Add:

```json
"features": {}
```

Do not port coma, tail, sodium-tail, or sun-oriented configuration.

## A3. `derive_served` rewrite

Replace the unconditional empty feature artifact with deterministic assembly from the object catalog. The implementation must:

1. Read each object's `features` value with an empty-mapping default.
2. Validate that the value is a mapping. A legacy list on any catalog object must fail with an object-specific message rather than being silently coerced.
3. Emit only objects whose feature mapping is non-empty, unless the current artifact contract explicitly requires empty object entries. Pick one behavior, encode it in tests, and state it in the report. The preferred behavior is sparse emission because Halley and Encke's explicit empties are catalog-completeness declarations, not useful served payload.
4. Preserve deterministic ordering using the catalog's existing stable order or a documented lexical order.
5. Preserve the existing `schema_version` mechanism; do not bump it unless the current repository's schema policy demonstrably requires a bump. If a bump appears necessary, stop and flag it rather than making an unreviewed compatibility decision.
6. Write through the builder's existing canonical JSON writer or atomic-write path. Do not create a second serialization path.
7. Leave `event_link` and info-card behavior unchanged.

Expected artifact shape:

```json
{
  "schema_version": "<existing value>",
  "features": {
    "earth": { "atmosphere_shell": {}, "van_allen_belts": {} },
    "jupiter": { "ring_system": {}, "radiation_belts": {} },
    "saturn": { "ring_system": {} }
  }
}
```

The abbreviated inner objects above indicate presence, not empty actual configs.

## A4. Unit A tests

Add or update offline tests that prove the exact served object keys, exact feature keys, exact critical numeric values, absence of Jupiter `magnetosphere`, absence of sun-dependent fields in Jupiter `radiation_belts`, explicit catalog empties for Halley and Encke, deterministic repeated output, and a clear failure on a legacy list-shaped `features` value.

The test must also prove that `event_link`, top-level coverage structure, and unrelated object configuration remain unchanged by Unit A.

## A5. Unit A acceptance command set

Use the repository's canonical environment and commands. At minimum run the complete Layer-1 offline suite and the builder dry run. Then produce a temporary or clean-worktree real build sufficient to inspect `feature_configs.json`.

Acceptance is achieved only when the offline suite passes, dry run passes, the real artifact matches the expected keys and values, a second identical run produces no semantic diff, and no file outside the declared edit surface changes unexpectedly.

Commit Unit A separately with a message equivalent to:

```text
phase2 f1a: serve object feature configs
```

---

# BUILD UNIT B — Empirical trust metadata and F1a global served window

## B1. Allowed files

The expected edit surface is:

```text
tools/gallery_cache_builder.py
<existing builder support module only if extraction is justified>
<existing Layer-1 offline test files>
```

Do not modify `gallery/assembler/render_orbits.py` merely to reuse its math. Import from it if dependency direction and import safety are acceptable. If importing it would pull rendering dependencies or create a cycle, extract only the already-validated pure propagation functions into a neutral module and make both callers import that single implementation. Do not duplicate the equations.

Any extraction must be behavior-preserving and separately tested against the pre-extraction implementation before deletion of the old copy.

## B2. Trust measurement architecture

Implement a pure computation layer separated from Horizons I/O and artifact serialization. The preferred decomposition is:

```text
select_trust_delta(object_config, orbital_data) -> delta_days
fetch_check_vector(object_config, epoch_jd, delta_days) -> state vector
propagate_two_body(elements, delta_days) -> predicted position
measure_angular_error(predicted, fetched, origin) -> error_deg
estimate_error_rate(samples) -> error_deg_per_day
compute_window_days(tolerance_deg, rate, guard_k, caps) -> window_days
build_trust_block(...) -> JSON-safe mapping
```

Names may follow repository conventions. The separation of concerns is mandatory because offline tests must exercise all calculations without network access.

## B3. Sample epochs and Δ selection

For each eligible non-spacecraft object with the data needed for Kepler propagation, choose a nominal Δ near `P/8`, capped at approximately 30 days. Apply any settled shorter-domain rule for satellites and current-apparition rule for comets from the handoff. The exact cap constant must live in one named constant, not as repeated literals.

Use two forward check samples derived from the same source epoch. A valid default is Δ and 2Δ, provided 2Δ remains inside the applicable cap and apparition/domain boundary. If the handoff's prior implementation notes specify a different pair, follow them. Record both sample offsets in the trust block or diagnostic evidence so the result is auditable.

Do not use a single sample except where the valid domain mathematically permits only one. Such a fallback must carry an explicit degraded-confidence marker and must not be silently treated as equivalent.

## B4. Error metric

Compare the predicted and fetched position directions from the same propagation center. Compute angular separation with a numerically stable dot-product formula:

```text
cos(theta) = clamp(dot(u, v), -1, 1)
theta_deg = degrees(acos(cos(theta)))
```

Reject zero-length vectors and mismatched centers with object-specific errors.

For each sample, compute `error_deg / elapsed_days`. The measured rate is the worse of the two sample rates. Do not average them.

The guarded rate is:

```text
guarded_rate_deg_per_day = measured_rate_deg_per_day * 2.0
```

The tolerance-derived window is:

```text
raw_window_days = 0.5 / guarded_rate_deg_per_day
```

When the measured rate is effectively zero within an explicit numeric epsilon, the tolerance-derived window is unbounded and must be reduced only by the applicable outer cap. Do not divide by zero or manufacture a tiny rate without recording the policy.

## B5. Caps and domain bounds

Apply the tolerance-derived window first, then the relevant domain cap.

For planets, cap at one orbital period. This is an outer cap, never a floor.

For moon-category objects, use the applicable short-domain or period-derived cap from the settled design. Their trust blocks are still emitted even though they are excluded from the interim global minimum.

For comets, cap to the current valid apparition interval. The trust block must identify the cap basis so a later builder run can explain why the window changed.

For asteroids, use the ordinary measured result in this pass. Do not implement encounter-epoch anchoring. If Apophis produces a suspiciously broad interval across its 2029 encounter, retain the design's current scope boundary and surface a diagnostic warning; do not silently add the deferred mechanism.

Spacecraft receive no Kepler trust block from this path.

## B6. Per-object trust schema

Use one stable additive mapping per eligible object. The exact repository placement should follow the handoff and existing artifact structure. The block must contain enough information to reproduce the decision without exposing unnecessary raw vectors.

Required semantic fields are:

```json
"trust": {
  "method": "two_body_check_vector",
  "epoch_jd": 0.0,
  "sample_offsets_days": [0.0, 0.0],
  "sample_errors_deg": [0.0, 0.0],
  "measured_rate_deg_per_day": 0.0,
  "guard_k": 2.0,
  "guarded_rate_deg_per_day": 0.0,
  "tolerance_deg": 0.5,
  "window_days": 0.0,
  "start_jd": 0.0,
  "end_jd": 0.0,
  "cap_basis": "tolerance|orbital_period|apparition|satellite_domain",
  "confidence": "measured"
}
```

Field spelling may be aligned to an already-settled schema in the handoff or repository, but no required semantic datum may be dropped. `start_jd` and `end_jd` must be computed from the same reference epoch and `window_days` convention used by the global envelope. State clearly whether `window_days` is one-sided or total span; the preferred convention is one-sided radius around the reference epoch, because the global artifact already exposes separate start and end boundaries.

Do not serialize NaN, Infinity, numpy scalar objects, datetime objects, or non-standard JSON types.

## B7. Global `served_window` F1a rule

After all eligible trust blocks are computed, select the minimum `window_days` across objects satisfying all of the following:

```text
trust block exists
category != "moon"
category != "spacecraft"
measurement succeeded
window_days is finite and positive after caps
```

Do not exclude `dwarf_planet`, `asteroid`, or `comet`.

Compute the top-level global `start_jd` and `end_jd` using the selected conservative one-sided window around the build's controlling reference epoch. Store or log the controlling object key. If the published schema cannot accept a controller field, include it in builder diagnostics and test evidence rather than changing schema casually.

If no qualifying object exists, fail the build. Do not emit `served_window: null` as a quiet fallback.

Moon-category trust failures must be visible but must not independently prevent construction of the F1a global window unless the repository's existing strict-build policy requires all catalog measurements to succeed. Whichever strictness policy is chosen must be explicit and tested.

## B8. Network behavior and reproducibility

All new Horizons requests must use the builder's existing client, retry, throttling, cache, and diagnostic pathways. Do not create direct ad hoc network calls.

A nightly run should not fetch the same check vector repeatedly inside one process. Cache by a key containing object identity, center, epoch, and requested sample epoch.

Offline tests must use fixed fixtures. No Layer-1 test may require network access. Real-build evidence must record the build timestamp, source epoch, sample epochs, controlling object, and final window.

When a transient network failure prevents one measurement, follow the builder's established strictness policy. Do not substitute stale or synthetic vectors without a visible provenance marker.

## B9. Unit B tests

Add deterministic tests for Δ selection, 30-day cap behavior, worse-of-two rate selection, `guard_k = 2.0`, 0.5° conversion, zero-rate handling, angular clamp stability, planet one-orbit outer cap, comet apparition cap, moon trust emission, moon exclusion from global minimum, inclusion of dwarf planet/asteroid/comet in the global minimum, spacecraft exclusion, empty-qualifier failure, JSON-safe serialization, and deterministic output.

Add a regression test proving that changing a moon's tiny `window_days` does not change global `served_window`, while changing the controlling non-moon object's window does.

Add a compatibility test proving that the current resolver and cache reader continue to accept the additive trust data without modification. This is a test-only interaction; production files remain untouched.

## B10. Unit B acceptance command set

Run the full offline suite from a clean checkout. Run builder dry mode. Run one real `--first-build` or canonical equivalent in an isolated output directory, then a canonical nightly run against that output. Both must complete without schema or compatibility errors.

Inspect and preserve evidence for at least Earth, Moon, Jupiter, Pluto, Apophis, Halley, and Voyager 1, representing planet, moon, dwarf planet, asteroid, comet, and spacecraft paths. Confirm that Voyager 1 has no Kepler trust block, Moon has a trust block but cannot control the global window, and the controlling non-moon object is reported.

Repeat the offline suite after the real run to detect fixture contamination.

Commit Unit B separately with a message equivalent to:

```text
phase2 f1a: measure and serve propagation trust
```

---

## 3. Cross-unit integration gate

After both commits exist, create a clean integration worktree containing Unit A followed by Unit B. Run the entire offline suite, dry run, first build, and nightly build again.

The integrated artifacts must satisfy these invariants:

| Invariant | Required result |
|---|---|
| Feature artifact | Non-empty and contains only the intended served feature objects |
| Earth features | `atmosphere_shell`, `van_allen_belts` |
| Jupiter features | `ring_system`, `radiation_belts`; no `magnetosphere` |
| Saturn features | `ring_system` |
| Halley/Encke catalog | Explicit `features: {}` |
| Per-object trust | Present for eligible propagated bodies, including moon-category bodies |
| Spacecraft trust | Absent from Kepler trust path |
| Global served window | Non-null, finite, positive, controlled by minimum qualifying non-moon |
| Existing event link | Unchanged |
| Resolver/cache reader | No source changes |
| Golden fingerprint | Unchanged unless an existing artifact contract explicitly includes one of the newly changed outputs; any unexpected change is a stop condition |

Do not accept an output merely because JSON parses. Compare semantics against the contract.

---

## 4. Required implementation report

Deliver a short implementation report beside the code changes containing:

```text
Pinned SHAs and clean-worktree proof
Re-located source symbols and line ranges at the new orrery SHA
Any source drift found and Tony's disposition
Files changed per unit
Schema choices that were implementation latitude rather than settled design
Commands run and results
Generated artifact excerpts
Per-object trust summary table
Global controlling object and final served window
Network/cache behavior observed
Known warnings
Explicit confirmation of untouched out-of-scope files/features
Commit SHAs for Unit A and Unit B
```

The trust summary table should include object key, category, epoch, sample offsets, sample errors, measured rate, guarded rate, cap basis, final window, and whether the object was eligible to control the global window.

---

## 5. Stop conditions

Stop rather than improvise when any of these occurs: a pinned SHA cannot be checked out; a load-bearing source value differs at the new orrery pin; the existing feature schema contradicts the handoff; reusing the propagation math requires a behavior-changing refactor; the artifact schema cannot carry additive trust without a version decision; the current resolver does not actually tolerate additive fields; the global-window epoch convention is ambiguous in live code; real Horizons data produces a structurally impossible or non-finite result; or the golden fingerprint changes outside an output intentionally modified by F1.

A stop report must identify the smallest blocking question and preserve all completed, independently valid work. Do not broaden the stop into a redesign request.

---

## 6. Explicitly deferred work

F1b consumption of per-object trust by `resolver.py` and `cache_reader.py` remains deferred and will deliberately reopen the Artifact 1 fingerprint when scheduled.

The uncertainty-envelope client UX remains deferred to a visual design pass.

Apophis encounter-epoch anchoring remains deferred. The future shape is an `overrides.asteroid.anchor` mechanism analogous to the existing comet anchor flow.

`event_link`, the info card, magnetosphere envelopes, bow shocks, sodium tails, comet comae and tails, and all other sun-oriented features remain deferred.

---

## 7. Definition of done

F1a is done only when Unit A and Unit B are separately committed and independently passing; the clean integrated run passes; `feature_configs.json` serves the agreed Wave 1 and Wave 2 configuration; eligible bodies expose auditable trust metadata; the global `served_window` is conservatively computed under the exact moon-exclusion rule; all stated scope boundaries remain intact; and the implementation report contains enough evidence for another model or human reviewer to reproduce the result without relying on conversation memory.

