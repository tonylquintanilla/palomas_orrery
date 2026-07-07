# PHASE 1B DATA SERVING PIPELINE — Preliminary Design Handoff

**Type:** DESIGN SESSION (zero code)
**Base:** orrery @ `f1ede52` / gallery @ `4b086a6`
**Date:** July 7, 2026
**Participants:** Tony Quintanilla, Claude Opus 4.6
**Purpose:** Preliminary design for 4.8 convergence review. Not a spec —
a reasoning trail and schema draft for verification and challenge.
**Source:** Master plan v9 §3a, §5 Phase 1b; Fable 5 broad analysis
(`DATA_SERVING_BROAD_ANALYSIS.md`, July 5 2026); Opus 4.6 + Tony
convergence (July 6, 2026).

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

**For 4.8:** The schema examples below contain illustrative values marked
`(illustrative)` in comments. When reviewing the schema, evaluate the
field structure and types, not the specific numbers.

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
| Jupiter   | analytic          | Outer scale, moon host                               |
| Moon      | cache-required    | Earth's moon, familiar geometry for visual validation |
| Io        | cache-required    | Fast period (~42h), step-size stress (6h = ~7 pts)   |
| Titan     | cache-required    | Different parent (Saturn), slow period               |
| Pluto     | barycenter edge   | `stored_center` = Pluto-Charon barycenter            |
| Charon    | cache-req + bary  | Moon of a barycenter object                          |
| Apophis   | analytic + preset | Close-approach Tier-2 override for specific window   |
| Voyager 1 | spacecraft        | Arc-natural frame, write-once, no elements           |

**Design question surfaced by the test set:** Apophis is analytic-available
(asteroid, Keplerian fallback works at solar system scale) but has a Tier-2
curated close-approach data set for a specific date window. The schema must
express "this object has both an analytical fallback AND a cached preset
for a specific date range." This is the `presets` field in the schema (§3).

**Not in the test set (by design):** inner Galilean moons other than Io
(Miranda, Europa, Ganymede, Callisto — same class, different step-size
dial), comets other than Apophis, additional spacecraft. The nine cover
every schema pattern; scaling is a catalog question (OQ-A), not a schema
question.

---

## 3. Coverage Index Schema — Draft v0.1

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
- **Solar system only.** Star, Earth system, and orbital parameter
  domains declare their bounds in their own simpler manifests (master
  plan §1). The serving home accommodates all domains; the coverage
  index schema is solar system.
- **Object keys are slugs**, not Horizons IDs. Human-readable, stable,
  used in file paths. Horizons ID is a field for provenance and re-fetch.
- **Schema-versioned.** The `schema_version` field lets the assembler
  detect and handle index format changes.

### Schema

**All values below are illustrative (see Provenance Discipline Notice).
At build time:** Horizons IDs and object metadata from
`celestial_objects.py` (`OBJECT_DEFINITIONS`). Osculating elements from
`osculating_cache_manager.py`. Position coverage from `orbit_paths.json`
via `orbit_data_manager.py`. Close approach presets from
`close_approach_data.py`. Feature slugs from `shell_configs.py`. The
`source` field in each object's `osculating` block will carry the actual
Horizons query provenance string recorded by the cache manager.

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

    "io": {
      "name": "Io",
      "horizons_id": "501",
      "category": "moon",
      "availability": "cache-required",
      "parent": "jupiter",
      "stored_center": "jupiter",
      "canonical_frame": "parent-relative",

      "osculating": {
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

      "presets": null
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
      "presets": null
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
      ]
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

      "presets": null
    }
  }
}
```

### Field Glossary

| Field | Type | Purpose |
|-------|------|---------|
| `schema_version` | string | Lets consumers detect format changes |
| `generated` | ISO datetime | When this index was produced |
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
| `.osculating.epoch_jd` | float | Julian date of the osculating epoch |
| `.osculating.a_au` | float | Semi-major axis in AU |
| `.osculating.e` | float | Eccentricity |
| `.osculating.i_deg` | float | Inclination in degrees |
| `.osculating.node_deg` | float | Longitude of ascending node in degrees |
| `.osculating.peri_deg` | float | Argument of perihelion in degrees |
| `.osculating.M0_deg` | float | Mean anomaly at epoch in degrees |
| `.osculating.source` | string | Provenance string (fetched, not recalled) |
| `.positions` | object\|null | Rolling cache position data. Null if analytic-only |
| `.positions.file` | string | Path relative to `serving_base` |
| `.positions.start` | ISO date | Coverage start |
| `.positions.end` | ISO date | Coverage end |
| `.positions.step_hours` | int | Time step in hours |
| `.positions.n_points` | int | Number of data points (derived, for validation) |
| `.positions.size_kb` | int | File size in KB (for loading indicators) |
| `.presets` | array\|null | Tier-2 curated data sets (close approaches, perihelia, encounters) |
| `.presets[].name` | string | Display name for the preset |
| `.presets[].slug` | string | URL-safe identifier |
| `.presets[].description` | string | One-line description for the UI |
| `.presets[].tier` | int | Cache tier (always 2 for curated presets) |
| `.presets[].positions` | object | Same schema as top-level `.positions` |
| `.presets[].positions.center` | string | Override center for this preset (e.g. `earth` for geocentric close approach) |
| `.presets[].positions.canonical_frame` | string | Override frame for this preset |
| `.features` | array\|null | Slugs of available visual features for this object (§6). UI enables toggles based on this list. Rendering params live in `feature_configs.json` |
| `scene_features` | array | Top-level. Scene-wide visual features (asteroid belt, heliosphere, etc.) |
| `feature_configs` | string | Top-level. Path to the feature config file relative to `serving_base` |

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
  "source": "JPL Horizons vectors via astroquery — export records query params",
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

**Unit:** `km` for positions (preserves float64 significance for moons;
AU would lose digits for Io's ~422,000 km orbit around Jupiter). The
assembler converts to AU for plotting. The index's osculating elements
use AU because they're solar-system-scale quantities.

**4.8 verification ask:** Is there a consistency concern with km in
position files vs AU in osculating elements? The rationale is precision
(parent-relative moons at AU scale lose significance), but the assembler
must handle the unit mismatch. Is this a footgun?

---

## 4. Open Questions — Preliminary Positions

### OQ-A: Web Catalog Scope

**Position:** Curated first tranche (the 9 test objects above), not all
157. Prove the pipeline end-to-end before scaling. The schema accommodates
the full catalog — scaling is an export run, not a schema change.

**4.8 ask:** Is there a risk that designing against 9 objects misses a
pattern that only surfaces at scale? What patterns might 157 objects
introduce that 9 don't?

### OQ-B: Window Policy

**Position:** Split policy.
- Heliocentric objects (planets, asteroids, comets): accumulate. Small
  data, analytical fallback exists. No reason to discard history.
- Moons: slide. They're the bulk of the data and parent-relative orbits
  don't need deep history. Window = current date minus some lookback +
  forward padding.
- Spacecraft: write-once. Completed missions never change.

**4.8 ask:** Does the accumulate/slide split introduce complexity in the
export script, or is it a simple per-class conditional?

### OQ-C: Update Cadence

**Position:** Monthly manual batch, 90-day forward padding. Tony runs the
export script on the desktop when convenient. No automation pressure.

### OQ-D: Moon Step Size

**Position:** 6h default. Per-object `step_hours` in the index from day
one. Inner moons (Io: ~42h period) may want 2h for smooth visual
rendering; outer moons (Titan: ~16 days) are fine at 6h or even 12h.
The dial exists in the schema; the value is tuned per object.

**4.8 ask:** Is 6h a reasonable default? At 6h, Io gets ~7 points per
orbit. Is that enough for a visually smooth Keplerian arc, or does the
assembler need to interpolate?

### OQ-E: Serving Home

**Position:** H1 — dedicated `palomas-orrery-data` repo, orphan-branch
publish, zero history growth. Keeps data weight off the gallery's 1 GB
ceiling. Separate Pages project site under the custom domain.

**Gate:** CORS check. Does `palomasorrery.com/data-repo-name/` share
origin with `palomasorrery.com/`? Probable yes (same custom domain over
GitHub Pages user site), but empirical confirmation needed before locking.
This is the literal first thing to build.

**The serving home accommodates all domains** — solar system data now,
star cache (Phase 3), Earth system data (Phase 5). The coverage index
schema is solar system; the repo layout has domain directories.

Proposed repo layout:
```
palomas-orrery-data/
├── solar-system/
│   ├── coverage_index.json
│   ├── positions/
│   │   ├── io.json
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

### OQ-F: Canonical Frame

**Position:** Settled in principle. Heliocentric for planets/asteroids/
comets, parent-relative for moons, arc-natural for spacecraft. The export
script transforms from whatever frame the desktop cache stores to the
canonical frame. Presets may override (Apophis close approach is
geocentric).

**Implementation detail:** The desktop's `orbit_paths.json` stores
moon positions in heliocentric coordinates (as fetched from Horizons
with `@sun` center). The export script must subtract the parent's
heliocentric position to get parent-relative. This requires the parent's
positions to be available for the same time steps — either fetched in
the same batch or interpolated.

**4.8 ask:** Is the heliocentric-to-parent-relative subtraction a
precision concern? At float64, subtracting two large heliocentric
vectors to get a small parent-relative vector loses significant digits.
Should the export script re-query Horizons with the parent as center
body (e.g., `@599` for Jupiter's moons) instead of subtracting?

### OQ-G: Wire Format

**Position:** JSON for v1. Debuggability during assembler development.
Column-oriented within JSON (see §3). Binary optimization (MessagePack,
CBOR, .npz) is a dial for later — the schema and file structure are
format-independent.

---

## 5. Design Tensions and Judgment Calls

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

### Position data unit (km vs AU)

Positions stored in km (see §3). Osculating elements in AU. The assembler
handles the conversion. Rationale: moons' parent-relative positions at AU
scale lose significant digits in float64 (e.g. Io's orbit radius is on the
order of ~0.003 AU — illustrative, exact value from cache at build time).

**4.8 ask:** Reiterated from §3. Is the mixed-unit approach a footgun
that will bite during assembler development? The alternative is all-AU
with a note that moon precision is degraded, or all-km with an AU
conversion constant in the index.

### Presets override frame and center

The Apophis close-approach preset uses `geocentric` frame and `earth`
center, overriding the object's default `heliocentric` / `sun`. This
means the assembler must handle per-preset coordinate transforms. The
schema expresses this (preset positions have their own `center` and
`canonical_frame` fields), but the implementation has implications for
Phase 2 assembler complexity.

**4.8 ask:** Is the preset frame override a Phase 1b schema concern or a
Phase 2 assembler concern? Should the schema just document the override
cleanly (as drafted), or should it constrain presets to the object's
default frame?

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

### Merge Point (Phase 2 Design Decision)

In B′ exhibits, the Python assembler returns orbit traces as a Plotly figure.
JS adds feature traces separately. Two options:

- (a) Python returns figure JSON → JS adds feature traces via
  `Plotly.addTraces()` after initial render.
- (b) JS extracts orbit trace data from Python's figure, combines with
  JS-generated feature traces, calls `Plotly.newPlot()` once.

Option (b) is likely cleaner (single render, no flash). Deferred to Phase 2.

### 4.8 Verification Asks (Features)

1. **Is the orbit/feature split clean?** Are there visual elements that
   straddle the line — things that need both orbital data AND parametric
   rendering? (Example: a comet tail needs the comet's position from the
   orbit solver AND the sun-comet vector for anti-sunward orientation.
   Does that break the "features are JS-only" rule, or does JS just read
   the comet's current position from the orbit data?)
2. **Does the feature config schema accommodate the desktop's SHELL_CONFIGS
   patterns?** The desktop has a rich shell configuration system. Can the
   web configs express the same visual vocabulary, or are there patterns
   that don't reduce to renderer + params?
3. **Is a separate `feature_configs.json` the right home, or should feature
   params ride in the coverage index?** The argument for separate: keeps
   the coverage index focused on data availability. The argument for
   inline: one fewer file to fetch. The configs are small (a few KB).

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

---

## 8. Specific Asks for 4.8 Review

1. **Schema completeness.** Are there fields the assembler will need that
   the schema doesn't carry? Walk the Phase 2 consumer path: "I want to
   show Jupiter and its moons for March 2026" — does the index have
   everything the assembler needs to know whether it can fulfill that
   request and where to find the data?
2. **Precision and units.** The km/AU mixed-unit question (§3, §5).
   Float64 significance for parent-relative moons.
3. **Preset frame overrides.** Schema concern or assembler concern? (§5).
4. **OQ-B split window.** Does accumulate/slide add implementation
   complexity worth worrying about now, or is it a simple conditional
   in the export script? (§4).
5. **OQ-D interpolation.** At 6h step and ~42h period, does Io need
   assembler-side interpolation for a smooth visual arc? (§4).
6. **OQ-E CORS.** Confirm the reasoning that a project site under a
   custom domain shares origin with the user site. If 4.8 has empirical
   knowledge, save us the test.
7. **Provenance.** Are the `source` fields in the schema and position
   files sufficient for the provenance discipline, or does the scanner
   need something more structured?
8. **Three-context feature split (§6).** Verify the delineation: static
   gallery = pre-baked traces in JSON (unchanged); interactive A and B′ =
   JS renderers from config params. Specifically: is the orbit/feature
   split clean, or are there visual elements that straddle the line
   (needing both orbital data AND parametric rendering — e.g. comet tails
   needing sun-object vector)?
9. **Feature config schema (§6).** Does `renderer` + `params` accommodate
   the desktop's SHELL_CONFIGS patterns? Are there shell types that don't
   reduce to this shape?
10. **Feature config home.** Separate `feature_configs.json` vs inline in
    coverage index. The configs are small (a few KB). What's cleaner?
11. **What did we miss?** The most valuable 4.8 output is often the thing
    we didn't think to ask about.

---

## 9. Lineage

- Master plan v9 §3a, §5 Phase 1b (July 6, 2026)
- Fable 5 broad analysis: `DATA_SERVING_BROAD_ANALYSIS.md` (July 5, 2026,
  built on `993dfd5` / `a6420bc`)
- Opus 4.6 + Tony convergence (July 6, 2026): F2 adopted, three trace
  types, two-class model
- Opus 4.6 + Tony design session (July 7, 2026): schema draft, test
  objects, OQ preliminary positions
- Ledger: L-098 (data serving pipeline), L-079 (shared assembler,
  keystone)

Base: orrery @ `f1ede52` / gallery @ `4b086a6`.

Session/entry written July 2026 with Anthropic's Claude Opus 4.6.
