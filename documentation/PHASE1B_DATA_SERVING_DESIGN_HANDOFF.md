# PHASE 1B DATA SERVING PIPELINE — Design Handoff v0.2

**Type:** DESIGN SESSION (zero code)
**Base:** orrery @ `f1ede52` / gallery @ `4b086a6`
**Date:** July 7, 2026
**Participants:** Tony Quintanilla, Claude Opus 4.6, Claude Opus 4.8 (review)
**Purpose:** Converged design for Phase 1b. Schema draft, test objects, open
questions, feature architecture, and validation rules — reviewed and refined
through 4.8 convergence.
**Source:** Master plan v9 §3a, §5 Phase 1b; Fable 5 broad analysis
(`DATA_SERVING_BROAD_ANALYSIS.md`, July 5 2026); Opus 4.6 + Tony convergence
(July 6, 2026); Opus 4.8 review (July 7, 2026).

**v0.2 changes from v0.1:** Incorporated 4.8 convergence review. Added
osculating `center` field (catch 1), validation invariants (catch 2),
cross-object parent dependency rules (catch 3). Settled km/AU, OQ-F
subtraction, OQ-E orphan-branch anchoring, presets-are-self-contained,
comet tail contract, SHELL_CONFIGS hover gap (flagged, deferred). Hybrid
provenance source field. Charon added to schema examples.

---

## Provenance Discipline Notice

**All numeric values in this handoff are illustrative — recalled from
Claude's training, not fetched from authoritative sources.** This includes
osculating element values, position vector examples, feature config
parameters (radii, ring dimensions, belt boundaries), Horizons IDs, step
counts, and file sizes. The schema SHAPE is the design deliverable; the
specific numbers are placeholders that demonstrate field types and ranges.

**At build time, the export script reads from these desktop source files:**

| Data Type | Source File(s) | Notes |
|-----------|---------------|-------|
| Osculating elements | `osculating_cache_manager.py` | Cached from JPL Horizons via `astroquery.jplhorizons`. Desktop-local |
| Position vectors | `orbit_paths.json` (~92 MB, gitignored) | Pair-based cache; export script extracts per-object canonical trajectories |
| Position vector management | `orbit_data_manager.py` | Manages cache reads/writes; has 5% size-reduction guard |
| Mean orbital elements | `orbital_elements.py` | Embedded in codebase, ships with assembler (no export needed) |
| Object definitions | `celestial_objects.py` (`OBJECT_DEFINITIONS`) | Horizons IDs, object categories, parent bodies |
| Physical constants | `constants_new.py` | AU conversion, gravitational parameters |
| Shell / feature configs | `shell_configs.py` (`SHELL_CONFIGS`) | Shell radii, colors, opacities — the desktop's rendering parameters |
| Shell rendering | `*_visualization_shells.py` modules | Per-planet shell geometry (Jupiter, Earth, Saturn, etc.) |
| Close approach data | `close_approach_data.py` | Preset definitions for encounters, perihelia, close approaches |
| Spacecraft encounters | `spacecraft_encounters.py` | Encounter timing, adaptive resolution |

**Provenance scan compliance:** All built code (the export script, the
coverage index generator) must pass provenance scan at Tier-1 = 0 before
push. Every numeric value in the export script's output must carry a
`source` field traceable to a fetched authority (JPL Horizons query, or
the desktop cache which itself carries Horizons provenance). No recalled
values survive into shipped data. The `# Source:` comment convention
applies to the export script's code, within scanner lookback distance.

---

## 1. What Phase 1b Is

Phase 1b builds the bridge from Tony's desktop caches to the browser. The
desktop has accumulated months of osculating elements and position vectors
from JPL Horizons. This pipeline makes that data available to the
interactive gallery as web-servable static files.

**Four deliverables:**

1. **Export script** — reads desktop caches (`osculating_cache_manager.py`
   + `orbit_paths.json`), writes per-object canonical files (F2 storage)
   in web-servable format.
2. **Coverage index** — JSON manifest of available objects. The assembler
   (Phase 2, B′ architecture) reads this to know what it can offer and
   what controls to enable. The GUI declares the envelope — this is the
   envelope.
3. **Serving home** — the location where web cache files live. Resolve
   OQ-E (CORS check first). Deploy first web cache as proof of pipeline.
   The slim plotly wheel (~3.9 MB, B′) also lives here.
4. **OQ resolutions** — settle OQ-A through OQ-G (see §4 below).

**What Phase 1b is NOT:** It does not build the assembler (Phase 2). It
does not touch the desktop code. It does not serve star data (Phase 3).
It produces the data files and the index that Phase 2 will consume.

---

## 2. Test Objects

Nine objects, selected to represent every class and edge case the schema
must express. The export script and coverage index are validated against
these before scaling to the full catalog.

| Object    | Class             | What It Tests                                        |
|-----------|-------------------|------------------------------------------------------|
| Earth     | analytic          | Baseline planet, easy visual check                   |
| Jupiter   | analytic          | Outer scale, moon host, parent dependency anchor     |
| Moon      | cache-required    | Earth's moon, familiar geometry for visual validation |
| Io        | cache-required    | Fast period (~42h), step-size stress, parent grid    |
| Titan     | cache-required    | Different parent (Saturn), slow period               |
| Pluto     | barycenter edge   | `stored_center` = Pluto-Charon barycenter            |
| Charon    | cache-req + bary  | Moon of a barycenter object, osculating center test  |
| Apophis   | analytic + preset | Close-approach Tier-2 override for specific window   |
| Voyager 1 | spacecraft        | Arc-natural frame, write-once, no elements           |

**Schema patterns confirmed by the test set (per 4.8 review):** Charon
tests the osculating-center mismatch (catch 1 — elements referenced to
barycenter, not Pluto's surface). Io tests parent-grid co-sampling
(catch 3 — Jupiter must be sampled on Io's time grid for the
heliocentric→parent-relative transform). Apophis tests self-contained
presets (the geocentric close-approach data carries no dependency on
Earth's rolling cache).

**Not in the test set (by design):** inner Galilean moons other than Io
(Europa, Ganymede, Callisto — same class, different step-size dial),
comets other than Apophis, additional spacecraft. The nine cover every
schema pattern; scaling is a catalog question (OQ-A), not a schema
question.

---

## 3. Coverage Index Schema — Draft v0.2

The coverage index is a single JSON file that tells the assembler (or
any consumer) what data is available, where it lives, and what trace
types are valid for each object. It is the contract between the export
script (producer) and the interactive page (consumer).

### Design Principles

- **The index is the envelope.** The GUI enables only what the index
  declares. A cache miss is something the UI won't let you request —
  not a runtime error.
- **Osculating elements ride inline.** They're ~8 numbers per object.
  The assembler can draw a full Keplerian conic from the index alone,
  no file fetch needed. Only position vectors go in separate files.
- **Osculating elements declare their own center.** The osculating
  `center` field is explicit even when it duplicates `stored_center`.
  Redundant-but-explicit prevents the Charon@9 failure: elements taken
  about the barycenter but drawn from the wrong center render visibly
  wrong, and nothing in the compiler catches it. *(4.8 catch 1)*
- **Solar system only.** Star, Earth system, and orbital parameter
  domains declare their bounds in their own simpler manifests (master
  plan §1). The serving home accommodates all domains; the coverage
  index schema is solar system.
- **Object keys are slugs**, not Horizons IDs. Human-readable, stable,
  used in file paths. Horizons ID is a field for provenance and re-fetch.
- **Schema-versioned.** The `schema_version` field lets the assembler
  detect and handle index format changes.
- **Unit is data.** The assembler reads the `unit` field and never
  assumes. Position files use km (float64 significance for moons).
  Osculating elements use AU (self-declared by field name `a_au`).
  The split matches each quantity's natural scale. *(4.8 settled)*
- **Presets are self-contained.** Rolling cache participates in frame
  composition (heliocentric→parent-relative subtraction); presets never
  do. A preset stores positions directly in its declared frame and
  center, with no dependency on any other object's coverage. This
  keeps Tier-2 curated data write-once and dependency-free.
  *(4.8 settled)*

### Schema

**All values below are illustrative (see Provenance Discipline Notice).
At build time:** Horizons IDs and object metadata from
`celestial_objects.py` (`OBJECT_DEFINITIONS`). Osculating elements from
`osculating_cache_manager.py`. Position coverage from `orbit_paths.json`
via `orbit_data_manager.py`. Close approach presets from
`close_approach_data.py`. Feature slugs from `shell_configs.py`. The
`source` field in each object's `osculating` block will carry the actual
Horizons query provenance recorded by the cache manager.

```json
{
  "schema_version": "1.0",
  "generated": "2026-07-07T12:00:00Z",
  "generator": "export_orbit_cache.py v1.0",
  "serving_base": "data/solar-system/",
  "feature_configs": "feature_configs.json",
  "scene_features": ["asteroid_belt", "kuiper_belt", "heliosphere"],

  "objects": {

    "earth": {
      "name": "Earth",
      "horizons_id": "399",
      "category": "planet",
      "availability": "analytic",
      "parent": "sun",
      "stored_center": "sun",
      "canonical_frame": "heliocentric",

      "osculating": {
        "center": "sun",
        "epoch_jd": 2460676.5,
        "a_au": 1.00000261,
        "e": 0.01671123,
        "i_deg": 0.00005,
        "node_deg": 174.9,
        "peri_deg": 288.1,
        "M0_deg": 357.5,
        "source": "PLACEHOLDER — build reads osculating_cache_manager.py"
      },

      "positions": null,
      "presets": null,
      "features": ["van_allen_belts", "atmosphere_shell"]
    },

    "jupiter": {
      "name": "Jupiter",
      "horizons_id": "599",
      "category": "planet",
      "availability": "analytic",
      "parent": "sun",
      "stored_center": "sun",
      "canonical_frame": "heliocentric",

      "osculating": {
        "center": "sun",
        "epoch_jd": 2460676.5,
        "a_au": 5.2026,
        "e": 0.0489,
        "i_deg": 1.303,
        "node_deg": 100.5,
        "peri_deg": 14.7,
        "M0_deg": 0.0,
        "source": "PLACEHOLDER — build reads osculating_cache_manager.py"
      },

      "positions": null,
      "presets": null,
      "features": ["magnetosphere", "ring_system"]
    },

    "io": {
      "name": "Io",
      "horizons_id": "501",
      "category": "moon",
      "availability": "cache-required",
      "parent": "jupiter",
      "stored_center": "jupiter",
      "canonical_frame": "parent-relative",

      "osculating": {
        "center": "jupiter",
        "epoch_jd": 2460676.5,
        "a_au": 0.00282,
        "e": 0.0041,
        "i_deg": 0.04,
        "node_deg": 0.0,
        "peri_deg": 0.0,
        "M0_deg": 0.0,
        "source": "PLACEHOLDER — build reads osculating_cache_manager.py"
      },

      "positions": {
        "file": "positions/io.json",
        "start": "2025-01-01",
        "end": "2026-04-01",
        "step_hours": 6,
        "n_points": "COMPUTED — (end-start)/step",
        "size_kb": "COMPUTED — measured at export"
      },

      "presets": null,
      "features": null
    },

    "pluto": {
      "name": "Pluto",
      "horizons_id": "999",
      "category": "dwarf_planet",
      "availability": "analytic",
      "parent": "sun",
      "stored_center": "pluto_barycenter",
      "canonical_frame": "heliocentric",

      "osculating": {
        "center": "pluto_barycenter",
        "epoch_jd": 2460676.5,
        "a_au": 39.482,
        "e": 0.2488,
        "i_deg": 17.16,
        "node_deg": 110.3,
        "peri_deg": 113.8,
        "M0_deg": 0.0,
        "source": "PLACEHOLDER — build reads osculating_cache_manager.py"
      },

      "positions": null,
      "presets": null,
      "features": null
    },

    "charon": {
      "name": "Charon",
      "horizons_id": "901",
      "category": "moon",
      "availability": "cache-required",
      "parent": "pluto",
      "stored_center": "pluto_barycenter",
      "canonical_frame": "parent-relative",

      "osculating": {
        "center": "pluto_barycenter",
        "epoch_jd": 2460676.5,
        "a_au": 0.000117,
        "e": 0.0002,
        "i_deg": 0.0,
        "node_deg": 0.0,
        "peri_deg": 0.0,
        "M0_deg": 0.0,
        "source": "PLACEHOLDER — build reads osculating_cache_manager.py"
      },

      "positions": {
        "file": "positions/charon.json",
        "start": "2025-01-01",
        "end": "2026-04-01",
        "step_hours": 6,
        "n_points": "COMPUTED",
        "size_kb": "COMPUTED"
      },

      "presets": null,
      "features": null
    },

    "apophis": {
      "name": "Apophis",
      "horizons_id": "99942",
      "category": "asteroid",
      "availability": "analytic",
      "parent": "sun",
      "stored_center": "sun",
      "canonical_frame": "heliocentric",

      "osculating": {
        "center": "sun",
        "epoch_jd": 2460676.5,
        "a_au": 0.9224,
        "e": 0.1914,
        "i_deg": 3.34,
        "node_deg": 204.4,
        "peri_deg": 126.4,
        "M0_deg": 0.0,
        "source": "PLACEHOLDER — build reads osculating_cache_manager.py"
      },

      "positions": null,

      "presets": [
        {
          "name": "2029 Close Approach",
          "slug": "apophis-2029-close-approach",
          "description": "Apophis close approach — build reads close_approach_data.py for details",
          "tier": 2,
          "positions": {
            "file": "presets/apophis_2029_close_approach.json",
            "start": "2029-04-01",
            "end": "2029-04-30",
            "step_hours": 1,
            "n_points": "COMPUTED",
            "size_kb": "COMPUTED",
            "center": "earth",
            "canonical_frame": "geocentric"
          }
        }
      ],

      "features": null
    },

    "voyager_1": {
      "name": "Voyager 1",
      "horizons_id": "-31",
      "category": "spacecraft",
      "availability": "spacecraft",
      "parent": "sun",
      "stored_center": "sun",
      "canonical_frame": "arc-natural",

      "osculating": null,

      "positions": {
        "file": "positions/voyager_1.json",
        "start": "1977-09-05",
        "end": "2025-12-31",
        "step_hours": 720,
        "n_points": "COMPUTED",
        "size_kb": "COMPUTED"
      },

      "presets": null,
      "features": null
    }
  }
}
```

### Field Glossary

| Field | Type | Purpose |
|-------|------|---------|
| `schema_version` | string | Lets consumers detect format changes |
| `generated` | ISO datetime | When this index was produced. **This is the provenance anchor for the data repo** — not the repo SHA, which is ephemeral on an orphan branch *(4.8)* |
| `generator` | string | Which script + version produced it |
| `serving_base` | string | Base URL/path prefix for all file references |
| `objects.{slug}` | object | Keyed by human-readable slug, not Horizons ID |
| `.name` | string | Display name |
| `.horizons_id` | string | JPL Horizons ID for provenance and re-fetch |
| `.category` | enum | `planet`, `dwarf_planet`, `moon`, `asteroid`, `comet`, `spacecraft` |
| `.availability` | enum | `analytic`, `cache-required`, `spacecraft` |
| `.parent` | string | Slug of gravitational parent (`sun`, `jupiter`, etc.) |
| `.stored_center` | string | What the position data is relative to (provenance) |
| `.canonical_frame` | enum | `heliocentric`, `parent-relative`, `geocentric`, `arc-natural` |
| `.osculating` | object\|null | Keplerian elements for one epoch. Null for spacecraft |
| `.osculating.center` | string | **Explicit center for these elements.** Usually matches `stored_center` but may differ (Charon: elements about barycenter, not Pluto surface). Redundant-but-explicit prevents silent render errors *(4.8 catch 1)* |
| `.osculating.epoch_jd` | float | Julian date of the osculating epoch |
| `.osculating.a_au` | float | Semi-major axis in AU |
| `.osculating.e` | float | Eccentricity |
| `.osculating.i_deg` | float | Inclination in degrees |
| `.osculating.node_deg` | float | Longitude of ascending node in degrees |
| `.osculating.peri_deg` | float | Argument of perihelion in degrees |
| `.osculating.M0_deg` | float | Mean anomaly at epoch in degrees |
| `.osculating.source` | string\|object | Provenance. String for non-Horizons sources. Structured `{query_target, center, epoch, retrieved}` for Horizons-derived data (enables re-verification) |
| `.positions` | object\|null | Rolling cache position data. Null if analytic-only |
| `.positions.file` | string | Path relative to `serving_base` |
| `.positions.start` | ISO date | Coverage start |
| `.positions.end` | ISO date | Coverage end |
| `.positions.step_hours` | int | Time step in hours |
| `.positions.n_points` | int | Number of data points (derived, for validation) |
| `.positions.size_kb` | int | File size in KB (for loading indicators) |
| `.presets` | array\|null | Tier-2 curated data sets (close approaches, perihelia, encounters). **Self-contained:** presets carry their own frame/center with no dependency on other objects' coverage *(4.8)* |
| `.presets[].name` | string | Display name for the preset |
| `.presets[].slug` | string | URL-safe identifier |
| `.presets[].description` | string | One-line description for the UI |
| `.presets[].tier` | int | Cache tier (always 2 for curated presets) |
| `.presets[].positions` | object | Same schema as top-level `.positions` plus `center` and `canonical_frame` |
| `.presets[].positions.center` | string | Override center for this preset (e.g. `earth` for geocentric close approach) |
| `.presets[].positions.canonical_frame` | string | Override frame for this preset |
| `.features` | array\|null | Slugs of available visual features for this object (§6). UI enables toggles based on this list. Rendering params live in `feature_configs.json` |
| `scene_features` | array | Top-level. Scene-wide visual features (asteroid belt, heliosphere, etc.) |
| `feature_configs` | string | Top-level. Path to the feature config file relative to `serving_base` |

### Validation Invariants *(4.8 catch 2)*

The export script asserts these before emitting the index. A violation is
a loud export failure, not a silent envelope lie.

1. `availability == "cache-required"` ⟹ `positions != null`
2. `availability == "spacecraft"` ⟹ `osculating == null && positions != null`
3. `availability == "analytic"` ⟹ `osculating != null`
4. `canonical_frame == "parent-relative"` ⟹ `parent` exists in the catalog
   with position coverage overlapping this object's window *(4.8 catch 3)*
5. `osculating != null` ⟹ `osculating.center` is populated
6. Every `presets[].positions.file` exists on disk at export time

### Cross-Object Parent Dependency *(4.8 catch 3)*

Storing moons parent-relative (correct for float64 precision) means the
assembler composes `heliocentric = parent_helio + moon_relative` whenever
a wide view is needed. This creates a hard dependency: a parent-relative
moon requires its parent's positions on the moon's time grid.

**Export-side rule:** Co-sample parent and moon on one time grid at export.
The export script subtracts the parent's heliocentric position from the
moon's to produce parent-relative vectors. The subtraction is performed
at float64 (~12 significant digits of headroom, confirmed by Fable's F2
rule). Re-querying Horizons with the parent as center body is NOT done —
it would violate the settled principle that the pipeline never fetches
Horizons; the desktop cache is the sole data source.

**Index-side rule:** Validation invariant #4 — every parent-relative
object's `parent` must exist in the catalog with overlapping time
coverage. Otherwise the assembler could offer a wide view it can't
compose.

### Position File Format (v1 — JSON)

Column-oriented for typed-array friendliness, but JSON for v1
debuggability. Each position file:

```json
{
  "object": "io",
  "center": "jupiter",
  "frame": "parent-relative",
  "unit": "km",
  "epoch_type": "JD",
  "source": {
    "query_target": "501",
    "center": "@599",
    "epoch": "2025-01-01 to 2026-04-01",
    "retrieved": "2026-06-15T10:30:00Z"
  },
  "data": {
    "t": ["(illustrative JD values — from orbit_paths.json via export script)"],
    "x": ["(illustrative — from orbit_paths.json, transformed to parent-relative)"],
    "y": ["(illustrative)"],
    "z": ["(illustrative)"]
  }
}
```

Column-oriented chosen over row-oriented: columns map directly to typed
arrays (the assembler does `np.array(data['x'])`), and a JSON viewer still
shows the structure clearly. The header fields (`object`, `center`,
`frame`, `unit`, `source`) make each file self-documenting — the same
provenance-first principle as `# Source:` comments in the codebase.

**Unit rule:** Unit is data; the assembler reads the `unit` field and
never assumes. `km` for positions (preserves float64 significance for
moons). `a_au` self-declares AU by field name for osculating elements.
The split matches each quantity's natural scale. *(4.8 settled)*

**Source field:** Structured object for Horizons-derived data (enables
re-verification — a future audit can re-run the query). For data derived
from codebase constants (mean elements, feature configs), a plain string
suffices. The hybrid approach avoids assuming all data is Horizons-shaped
while giving machine-verifiable provenance where it's available.

---

## 4. Open Questions — Preliminary Positions

### OQ-A: Web Catalog Scope

**Position:** Curated first tranche (the 9 test objects), not all 157.
Prove the pipeline end-to-end before scaling. The schema accommodates
the full catalog — scaling is an export run, not a schema change. The
nine were chosen to exercise every schema pattern, including the three
structural gaps 4.8 found (osculating center, parent dependency,
self-contained presets).

### OQ-B: Window Policy

**Position:** Split policy.
- Heliocentric objects (planets, asteroids, comets): accumulate. Small
  data, analytical fallback exists. No reason to discard history.
- Moons: slide. They're the bulk of the data and parent-relative orbits
  don't need deep history. Window = current date minus some lookback +
  forward padding.
- Spacecraft: write-once. Completed missions never change.

4.8 confirmed this is a simple per-class conditional in the export
script, not a complexity concern.

### OQ-C: Update Cadence

**Position:** Monthly manual batch, 90-day forward padding. Tony runs the
export script on the desktop when convenient. No automation pressure.

### OQ-D: Moon Step Size

**Position:** 6h default. Per-object `step_hours` in the index from day
one. Inner moons (Io: ~42h period) may want 2h for smooth visual
rendering; outer moons (Titan: ~16 days) are fine at 6h or even 12h.
The dial exists in the schema; the value is tuned per object. 4.8
confirmed this is a Mode 5 question — Tony's render decides.

### OQ-E: Serving Home — SETTLED + ANCHORING RULE

**Position:** H1 — dedicated `palomas-orrery-data` repo, orphan-branch
publish, zero history growth. Keeps data weight off the gallery's 1 GB
ceiling. Separate Pages project site under the custom domain.

**Gate:** CORS check. Does `palomasorrery.com/data-repo-name/` share
origin with `palomasorrery.com/`? Probable yes (same custom domain over
GitHub Pages user site), but empirical confirmation needed before locking.
This is the literal first thing to build.

**Anchoring rule *(4.8)*:** A force-pushed orphan branch makes the data
repo's commit SHA useless as a round-trip anchor — it's not history,
it's a projection that gets rewritten every export. The coverage index's
`generated` timestamp + `generator` version is the provenance anchor for
the data store. The data repo does NOT participate in the SHA round-trip
protocol; the orrery and gallery repos do.

**The serving home accommodates all domains** — solar system data now,
star cache (Phase 3), Earth system data (Phase 5). The coverage index
schema is solar system; the repo layout has domain directories.

Proposed repo layout:
```
palomas-orrery-data/
├── solar-system/
│   ├── coverage_index.json
│   ├── feature_configs.json
│   ├── positions/
│   │   ├── io.json
│   │   ├── charon.json
│   │   ├── titan.json
│   │   └── ...
│   ├── presets/
│   │   ├── apophis_2029_close_approach.json
│   │   └── ...
│   └── wheels/
│       └── plotly-slim-5.x.x-py3-none-any.whl
├── stars/
│   └── (Phase 3)
└── earth-system/
    └── (Phase 5)
```

### OQ-F: Canonical Frame — SETTLED

**Position:** Heliocentric for planets/asteroids/comets, parent-relative
for moons, arc-natural for spacecraft. Presets may override (Apophis close
approach is geocentric).

**Transform method — settled *(4.8)*:** Subtract, don't re-query. The
export script subtracts the parent's heliocentric position from the moon's
to produce parent-relative vectors. Float64 has ~12 significant digits of
headroom — sufficient for the subtraction. Re-querying Horizons with the
parent as center body violates the settled principle that the pipeline
never fetches Horizons; the desktop cache is the sole data source.

**Co-sampling requirement:** Export the parent and moon on the same time
grid before subtracting. If Jupiter is stepped 1d and Io 6h,
interpolating Jupiter introduces smooth-arc artifacts. Co-sample
parent+moon on one grid at export time.

### OQ-G: Wire Format

**Position:** JSON for v1. Debuggability during assembler development.
Column-oriented within JSON (see §3). Binary optimization (MessagePack,
CBOR, .npz) is a dial for later — the schema and file structure are
format-independent.

---

## 5. Design Decisions — Settled

### Osculating element staleness — SETTLED

**Decision:** No `valid_until` field. The osculating conic represents ONE
orbit shape at the stated epoch — a snapshot of the orbit geometry, not a
time-evolving position. The three trace types already distinguish between
"actual positions" (cached, dated), "osculating at epoch" (shape, epoch-
specific), and "mean elements" (long-term average). The UI labels the
osculating trace clearly as epoch-specific.

**Rationale (Tony):** except for comets at perihelion (where the osculating
orbit IS the interesting thing — the hyperbolic or highly eccentric conic
at that moment), one orbit shape is about right. The assembler draws one
Keplerian ellipse from the six elements. No staleness tracking needed.

This is a science museum, not mission planning. Adding `valid_until` would
imply a precision promise the visualization doesn't need to make.

### Position data unit (km vs AU) — SETTLED *(4.8)*

**Rule:** Unit is data; the assembler reads the `unit` field and never
assumes. Position files use km (preserves float64 significance for parent-
relative moons). Osculating elements use AU (self-declared by field name
`a_au`). The split matches each quantity's natural scale — more honest
than degrading moon precision to satisfy uniformity.

### Presets are self-contained — SETTLED *(4.8)*

Rolling cache participates in frame composition (heliocentric→parent-
relative subtraction); presets never do. A preset stores positions
directly in its declared frame and center. No assembler-side composition,
no dependency on other objects' coverage. This keeps Tier-2 curated data
write-once and dependency-free, and sidesteps a second Charon@9 (an
overriding center that doesn't match its data).

### Subtract, don't re-query — SETTLED *(4.8)*

See OQ-F above. The desktop cache is the sole data source. The export
script performs the heliocentric→parent-relative subtraction at float64.
Re-querying Horizons violates the settled "site never fetches Horizons"
principle.

---

## 6. Feature Rendering Architecture — Three Contexts

Visual features (shells, magnetospheres, ring systems, comet tails, asteroid
belts, etc.) are procedural, not positional. They're computed from parameters
(radii, angles, geometry), not from Horizons data. But WHERE they render
differs across the gallery's three rendering contexts, and the architecture
must respect that.

### The Three Contexts

| Context | Orbits | Features | Implication |
|---------|--------|----------|-------------|
| **Static gallery** (index.html, curated cards) | Desktop Python → baked into JSON | Desktop Python → baked into JSON | No change to existing pipeline. Heavy Mesh3d vertex arrays are fine — computed once, shipped as data. |
| **Interactive A** (frozen pedagogical demos) | NumPy arrays → JS trace builder | JS renderers from config params | No Pyodide plotly. JS builds everything. Lightweight. |
| **Interactive B′** (data-backed exhibits) | Python assembler → plotly figure JSON | JS renderers from config params — **not** through Pyodide | Python handles physics (orbits). JS handles parametric geometry (features). Avoids serializing heavy meshes through Python→JSON→JS. |

### Key Insight: Features Are Always JS in the Interactive Layer

The B′ Python assembler handles orbit computation only. Feature traces are
JS-rendered from parameter configs, shared across both A and B′ exhibits.
This is NOT the parallel-pipeline anti-pattern — the split is by kind of
computation (orbital mechanics vs parametric geometry), not by duplication
of the same computation.

The static gallery doesn't need feature configs — its features are pre-baked
by the desktop Python into the JSON files, same as today. The feature config
schema is an interactive-side concern only.

**Feature renderer contract *(4.8 settled)*:** Feature renderers may read
an object's current position from the rendered orbit output; they never
invoke orbital mechanics. A comet tail needs the comet's position (from
the orbit trace already rendered) and the anti-sunward vector (the sun is
at the origin in heliocentric, so the vector is `-normalize(position)`).
The tail is JS-rendered from data JS already holds. This resolves comet
tails, Mercury's sodium tail, and any future anti-sunward feature without
breaking the orbit/feature split.

### Feature Config Schema

A separate `feature_configs.json` in the serving home. The coverage index
references feature availability (slugs); the config file carries the
rendering parameters. Kept separate to avoid bloating the coverage index
with rendering details.

```json
{
  "schema_version": "1.0",

  "renderers": {
    "ellipsoid_shell": { "description": "3D ellipsoid mesh (magnetospheres, atmospheres)" },
    "annulus": { "description": "Flat ring (planetary rings)" },
    "torus_belt": { "description": "Toroidal belt region (asteroid belt, Kuiper belt)" },
    "cone_sweep": { "description": "Conical sweep (magnetic dipole tilt, bow shock)" },
    "tail_vector": { "description": "Anti-sunward tail (comet tail, sodium tail)" }
  },

  "object_features": {
    "jupiter": {
      "magnetosphere": {
        "renderer": "ellipsoid_shell",
        "params": {
          "radius_km": "(illustrative — build reads shell_configs.py SHELL_CONFIGS)",
          "color": "(illustrative — build reads shell_configs.py)",
          "name": "Jupiter Magnetosphere"
        }
      },
      "ring_system": {
        "renderer": "annulus",
        "params": {
          "inner_km": "(illustrative — build reads shell_configs.py)",
          "outer_km": "(illustrative — build reads shell_configs.py)",
          "color": "(illustrative)",
          "name": "Jupiter Ring System"
        }
      }
    },
    "earth": {
      "van_allen_belts": {
        "renderer": "ellipsoid_shell",
        "params": {
          "radius_km": "(illustrative — build reads shell_configs.py)",
          "color": "(illustrative)",
          "name": "Van Allen Belts"
        }
      }
    }
  },

  "scene_features": {
    "asteroid_belt": {
      "renderer": "torus_belt",
      "params": {
        "inner_au": "(illustrative — build reads constants_new.py or shell_configs.py)",
        "outer_au": "(illustrative)",
        "color": "(illustrative)",
        "name": "Asteroid Belt"
      }
    }
  }
}
```

### Coverage Index Integration

The coverage index carries feature slugs only — enough for the UI to know
what toggles to offer. It does NOT carry rendering parameters.

```json
"jupiter": {
  ...
  "features": ["magnetosphere", "ring_system"]
}
```

Scene-level features at the index root:

```json
{
  "schema_version": "1.0",
  "scene_features": ["asteroid_belt", "kuiper_belt", "heliosphere"],
  "objects": { ... }
}
```

### Renderer Vocabulary (Illustrative — Phase 2 Builds This)

**Per-object features:**
- `ellipsoid_shell` — magnetospheres, atmosphere boundaries, Van Allen belts
- `annulus` — ring systems (Saturn, Jupiter, Uranus, Neptune)
- `cone_sweep` — magnetic dipole tilt visualization
- `tail_vector` — comet ion/dust tails, Mercury sodium tail (anti-sunward)
- `bow_shock` — planetary bow shock surfaces

**Scene-level features:**
- `torus_belt` — asteroid belt, Kuiper belt
- `sphere_shell` — heliosphere, heliopause
- `solar_wind` — radial field lines (if implemented)

### Hover Behavior Gap *(4.8 flagged, deferred to Phase 2)*

The `renderer + params` schema captures **geometry** (radii, colors,
opacities) but does NOT capture the desktop's **interaction layer** —
specifically the single-info-marker pattern (one cross marker carries the
hover for an entire shell; `hoverinfo='skip'` on all geometry points).
That's hover routing, not geometry, and it doesn't live in radii/colors.

This is a Phase 2 JS renderer concern, not a Phase 1b schema concern.
The feature config schema defines *what* to draw and *where*. How to
handle hover routing in JS/Plotly.js is an implementation decision for
the JS renderers — the desktop's single-info-marker convention may or
may not be the right pattern in a browser context.

### Merge Point (Phase 2 Design Decision)

In B′ exhibits, the Python assembler returns orbit traces as a Plotly figure.
JS adds feature traces separately. Two options:

- (a) Python returns figure JSON → JS adds feature traces via
  `Plotly.addTraces()` after initial render.
- (b) JS extracts orbit trace data from Python's figure, combines with
  JS-generated feature traces, calls `Plotly.newPlot()` once.

Option (b) is likely cleaner (single render, no flash). Deferred to Phase 2.

---

## 7. What This Handoff Does NOT Cover

- **The export script implementation.** This handoff settles the schema.
  The script is a Phase 1b build deliverable.
- **The assembler's consumption of the index.** That's Phase 2, after
  the data pipeline validates.
- **Star data format.** Phase 3 (master plan §7 #8).
- **Earth system data.** Phase 5.
- **The slim plotly wheel build.** Fable's strip spec
  (`AB_FORK_ANALYSIS.md`) covers this. It rides in the serving home
  but isn't a schema question.
- **Desktop code changes.** Phase 1b reads the desktop caches; it does
  not modify them.
- **JS feature renderer implementation.** The config schema defines
  the interface; the renderers are Phase 2.

---

## 8. Convergence Status After 4.8 Review

### Settled (no further review needed)

1. **Osculating center field** — added. Redundant-but-explicit. *(catch 1)*
2. **Validation invariants** — six rules the export script asserts. *(catch 2)*
3. **Parent dependency** — co-sample + index validation. *(catch 3)*
4. **km/AU** — unit is data, assembler reads the field, never assumes.
5. **OQ-F subtraction** — subtract, don't re-query. Float64 sufficient.
6. **Presets self-contained** — no frame composition, no dependency.
7. **Comet tail contract** — feature renderers read position from orbit
   output, never invoke orbital mechanics.
8. **Osculating staleness** — no `valid_until`. One orbit shape.
9. **OQ-E anchoring** — index `generated` timestamp, not repo SHA.
10. **Provenance source field** — hybrid string/structured object.

### Open (Mode 5 or future phase)

1. **OQ-A catalog scope** — nine test objects now; full catalog is a
   later export run. No schema change needed.
2. **OQ-D step size tuning** — 6h default; per-object dial exists.
   Tony's render decides. Mode 5.
3. **OQ-E CORS check** — empirical gate. First thing to build.
4. **Hover behavior in JS renderers** — flagged, deferred to Phase 2.
5. **Feature config home** — separate `feature_configs.json` is current
   position. Could go inline later if one-fewer-fetch matters.

---

## 9. Lineage

- Master plan v9 §3a, §5 Phase 1b (July 6, 2026)
- Fable 5 broad analysis: `DATA_SERVING_BROAD_ANALYSIS.md` (July 5, 2026,
  built on `993dfd5` / `a6420bc`)
- Opus 4.6 + Tony convergence (July 6, 2026): F2 adopted, three trace
  types, two-class model
- Opus 4.6 + Tony design session (July 7, 2026): schema v0.1, test
  objects, OQ preliminary positions, feature architecture, provenance
  annotations
- Opus 4.8 convergence review (July 7, 2026): three load-bearing catches
  (osculating center, validation invariants, parent dependency), five
  settled items (km/AU, subtraction, presets, comet tail, OQ-E anchoring),
  hover gap flagged
- Opus 4.6 + Tony convergence to v0.2 (July 7, 2026): all 4.8 catches
  accepted, Charon added to schema, SHELL_CONFIGS hover gap accepted as
  flag (deferred), provenance source hybrid adopted
- Ledger: L-098 (data serving pipeline), L-079 (shared assembler,
  keystone)

Base: orrery @ `f1ede52` / gallery @ `4b086a6`.

Session/entry written July 2026 with Anthropic's Claude Opus 4.6.
