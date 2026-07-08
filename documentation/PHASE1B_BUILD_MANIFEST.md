# PHASE 1B BUILD MANIFEST — export_orbit_cache.py (v2)

**Type:** BUILD MANIFEST (Mode 2 — agentic, new module)
**Design source:** PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.6
**Base:** orrery — resolve live HEAD at build session start (do NOT hardcode)
**Pre-build gates:** (1) diff `f1ede52..<live HEAD>`, confirm 10 source files
unchanged; (2) pre-flight verification (Step 0 below)
**Post-build gate:** provenance scan Tier-1 = 0 on new module before push

**v2 changes from v1:** 4.8 manifest review incorporated. Pre-flight step
added (cache key resolution, import cleanliness, symbol names, Pluto pair
key). Parent interpolation replaces grid intersection in Step 3. Saturn
added as 10th test object. Explicit center slug map. `close_approach_data.py`
added to inputs. Apophis preset acknowledged as likely null. Voyager osc_key
set to None. SHA drift fixed (use live HEAD, not hardcoded).

---

## 1. What We're Building

One Python script (`export_orbit_cache.py`) that runs on Tony's desktop,
reads the local caches, and writes web-servable files to a target directory
(which Tony then copies to the gallery repo's `data/solar-system/`). Plus
a small `feature_configs.json` authored from `SHELL_CONFIGS`.

The script is a **desktop developer tool** — it lives in the orrery repo
alongside `gallery_studio.py` and the other devtools. It does NOT run in
the browser. It does NOT modify the desktop caches.

---

## 2. Inputs (all desktop-local, read-only)

| File | Provides | Read via |
|------|----------|---------|
| `data/orbit_paths.json` | Position vectors (date-keyed, AU, pair keys) | Direct JSON load (no tkinter dep) |
| `data/osculating_cache.json` | Osculating elements per object | Direct JSON load (no tkinter dep) |
| `celestial_objects.py` | `OBJECT_DEFINITIONS` — Horizons IDs, categories, parents | Import |
| `constants_new.py` | AU-to-km conversion constant (verify actual name) | Import |
| `shell_configs.py` | `SHELL_CONFIGS` — feature rendering parameters | Import |
| `close_approach_data.py` | Preset definitions for close approaches, perihelia | Import (for Apophis preset metadata) |

**Import cleanliness (verify at build start):** `celestial_objects`,
`constants_new`, `shell_configs`, and `close_approach_data` must import
clean — no transitive plotly/tkinter dependencies. Test each in a bare
interpreter before writing the script:
```
python -c "from celestial_objects import OBJECT_DEFINITIONS; print('OK')"
python -c "from constants_new import AU_TO_KM; print('OK')"  # verify actual name
python -c "from shell_configs import SHELL_CONFIGS; print('OK')"
```

---

## 3. Outputs (to target directory)

```
<output_dir>/
├── coverage_index.json          # The schema v0.6 manifest
├── feature_configs.json         # Renderer + params from SHELL_CONFIGS
├── positions/
│   ├── earth.json               # Heliocentric, km (parent of Moon)
│   ├── jupiter.json             # Heliocentric, km (parent of Io)
│   ├── saturn.json              # Heliocentric, km (parent of Titan)
│   ├── moon.json                # Parent-relative to Earth, km
│   ├── io.json                  # Parent-relative to Jupiter, km
│   ├── titan.json               # Parent-relative to Saturn, km
│   ├── charon.json              # Parent-relative to Pluto barycenter, km
│   └── voyager_1.json           # Heliocentric, km (write-once)
└── presets/
    └── (apophis_2029_close_approach.json — only if 2029 data exists)
```

**Not produced:** Pluto position file (analytic, its trajectory IS the
barycenter per `trajectory_of`). Apophis position file (analytic, preset
only — and preset is likely null for the test tranche since the desktop
cache probably covers 2025–2026, not 2029).

**Apophis note:** Without 2029 data, Apophis exercises only the plain
analytic path. The "self-contained preset" schema pattern goes untested
in Phase 1b. This is explicitly acceptable — the pattern is validated
when preset data is available.

---

## 4. Processing Steps (in dependency order)

### Step 0: Pre-flight verification *(4.8 catch 1)*

**This step runs before any export code is written.** It answers the
questions the manifest cannot answer from documentation alone.

```python
# 0a. Cache key resolution — THE critical gate for moons
import json
with open('data/orbit_paths.json', 'r') as f:
    cache = json.load(f)

io_entry = cache.get('Io_Sun', {})
keys = sorted(io_entry.get('data_points', {}).keys())
print(f"Io_Sun: {len(keys)} data points")
print(f"First 10 keys: {keys[:10]}")
print(f"Last 5 keys: {keys[-5:]}")
# If keys are "YYYY-MM-DD" (daily): ~365 points/year, 0.5 per Io orbit
#   → moons need finer desktop re-fetch before export can proceed
# If keys carry time ("YYYY-MM-DD HH:MM"): check spacing
# If old format (bare x/y/z arrays): count array length

# 0b. Pluto pair key — what Horizons target is stored?
pluto_entry = cache.get('Pluto_Sun', {})
pluto_meta = pluto_entry.get('metadata', {})
print(f"Pluto_Sun center_body: {pluto_meta.get('center_body')}")
print(f"Pluto_Sun data points: {len(pluto_entry.get('data_points', {}))}")
# If this is barycenter (target 9): Charon subtraction is consistent
# If this is body (target 999): Charon subtraction will mismatch osculating

# 0c. Saturn presence — required for Titan
saturn_entry = cache.get('Saturn_Sun', {})
print(f"Saturn_Sun present: {bool(saturn_entry)}")
print(f"Saturn_Sun data points: {len(saturn_entry.get('data_points', {}))}")

# 0d. Import cleanliness
from celestial_objects import OBJECT_DEFINITIONS
print(f"OBJECT_DEFINITIONS: {len(OBJECT_DEFINITIONS)} objects")

# Verify the AU conversion constant name
import constants_new
au_attrs = [a for a in dir(constants_new) if 'AU' in a.upper() and 'KM' in a.upper()]
print(f"AU-to-km candidates: {au_attrs}")

# 0e. Date coverage summary
for key in ['Earth_Sun', 'Jupiter_Sun', 'Io_Sun', 'Titan_Sun',
            'Moon_Sun', 'Pluto_Sun', 'Charon_Sun', 'Saturn_Sun',
            'Voyager 1_Sun', 'Apophis_Sun']:
    entry = cache.get(key, {})
    dp = entry.get('data_points', {})
    meta = entry.get('metadata', {})
    dates = sorted(dp.keys()) if dp else []
    print(f"{key}: {len(dates)} pts, "
          f"{dates[0] if dates else 'N/A'} to {dates[-1] if dates else 'N/A'}, "
          f"center={meta.get('center_body', 'N/A')}")
```

**Stop/go decision after Step 0:**
- If Io keys are daily → moons cannot be exported at sub-orbit resolution.
  Options: (a) re-fetch moons at 6h on the desktop first (scope expansion),
  or (b) export planets/spacecraft only, defer moons. Tony decides.
- If Pluto is body-999 → Charon subtraction will produce body-relative,
  not barycenter-relative. Options: re-fetch as target 9, or adjust
  Charon's `osculating.center` to match. Tony decides.
- If Saturn is missing → drop Titan from tranche. Log it.

### Step 1: Load and validate inputs

```
load orbit_paths.json → raw_cache
load osculating_cache.json → osc_cache
import OBJECT_DEFINITIONS, AU_TO_KM (verified name), SHELL_CONFIGS
```

### Step 2: Define test tranche

```python
# Center body → slug map (explicit, not string-strip)
CENTER_SLUG_MAP = {
    '@sun': 'sun', '@0': 'sun', '@10': 'sun', 'Sun': 'sun', '0': 'sun',
    '@399': 'earth', '399': 'earth',
    '@599': 'jupiter', '599': 'jupiter',
    '@699': 'saturn', '699': 'saturn',
    '@9': 'pluto_barycenter', '9': 'pluto_barycenter',
}

def resolve_center_slug(center_body_str):
    """Map Horizons center_body to schema slug. Rejects unmapped values."""
    slug = CENTER_SLUG_MAP.get(center_body_str)
    if slug is None:
        slug = CENTER_SLUG_MAP.get(center_body_str.lstrip('@'))
    if slug is None:
        raise ValueError(f"Unmapped center_body: {center_body_str}")
    return slug

TEST_OBJECTS = [
    # (slug, cache_pair_key, osc_key, horizons_id, category, availability,
    #  parent, stored_center, canonical_frame, trajectory_of, features)
    ("earth",     "Earth_Sun",     "Earth",     "399",   "planet",       "analytic",       "sun", "sun", "heliocentric", None, ["van_allen_belts", "atmosphere_shell"]),
    ("jupiter",   "Jupiter_Sun",   "Jupiter",   "599",   "planet",       "analytic",       "sun", "sun", "heliocentric", None, ["magnetosphere", "ring_system"]),
    ("saturn",    "Saturn_Sun",    "Saturn",    "699",   "planet",       "analytic",       "sun", "sun", "heliocentric", None, ["ring_system"]),
    ("moon",      "Moon_Sun",      "Moon",      "301",   "moon",         "cache-required", "earth", "earth", "parent-relative", None, None),
    ("io",        "Io_Sun",        "Io",        "501",   "moon",         "cache-required", "jupiter", "jupiter", "parent-relative", None, None),
    ("titan",     "Titan_Sun",     "Titan",     "606",   "moon",         "cache-required", "saturn", "saturn", "parent-relative", None, None),
    ("pluto",     "Pluto_Sun",     "Pluto",     "999",   "dwarf_planet", "analytic",       "sun", "sun", "heliocentric", "pluto_barycenter", None),
    ("charon",    "Charon_Sun",    "Charon@9",  "901",   "moon",         "cache-required", "pluto", "pluto_barycenter", "parent-relative", None, None),
    ("apophis",   "Apophis_Sun",   "Apophis",   "99942", "asteroid",     "analytic",       "sun", "sun", "heliocentric", None, None),
    ("voyager_1", "Voyager 1_Sun", None,        "-31",   "spacecraft",   "spacecraft",     "sun", "sun", "arc-natural", None, None),
]

# Parents whose position files are required for moon composition
PARENT_OBJECTS = {"earth", "jupiter", "saturn"}

# Objects that need position files written
NEEDS_POSITIONS = {slug for slug, *_ in TEST_OBJECTS
                   if _[3] in ("cache-required", "spacecraft")} | PARENT_OBJECTS
```

**Note:** Voyager's `osc_key` is `None` — spacecraft have no osculating
elements (invariant #2).

**Note:** Charon's `osc_key` is `"Charon@9"` (barycentric elements). The
export script asserts that its resolved center equals `pluto_barycenter`.

### Step 3: Extract position data for each object

For each object in `NEEDS_POSITIONS`:

```
1. Look up pair_key in raw_cache (e.g. "Io_Sun")
2. If not found → log warning, skip
3. Extract data_points dict
4. Sort by date key, parse to JD timestamps
5. Extract x, y, z coordinate arrays
6. Convert AU to km (multiply by AU_TO_KM)
7. For parent-relative moons:
   a. Look up parent's pair key (e.g. "Jupiter_Sun")
   b. Parse parent's dates to JD, extract parent x, y, z in km
   c. INTERPOLATE parent onto moon's timestamps using numpy.interp
      on each coordinate independently (NOT grid intersection —
      intersection decimates moon resolution) *(4.8 catch 2)*
   d. Subtract interpolated parent from moon at each timestamp
   e. The result is parent-relative in km at the moon's full cadence
   f. ASSERT: Charon's resolved center == pluto_barycenter *(4.8 catch 4)*
8. Write column-oriented JSON position file with provenance header
```

**Why interpolation, not intersection *(4.8 catch 2)*:** Invariant #7
requires the moon step to be finer than the parent's. Intersecting a fine
moon grid with a coarser parent grid keeps only the coarse-aligned points —
throwing away 3 of every 4 Io samples. Interpolating the parent (smooth
planetary motion, safe for linear interp at sub-day scales) preserves the
moon's full resolution while using the parent's data. The invariant checks
grid nesting; the algorithm honors it.

### Step 4: Build osculating entries for coverage index

For each object with `osc_key is not None`:

```
1. Look up osc_key in osc_cache (e.g. "Jupiter", "Charon@9")
2. If not found → log warning (invariant #3 catches at assembly)
3. Extract elements dict
4. Map fields:
   a → a_au (direct)
   e → e (direct)
   i → i_deg (direct)
   omega → peri_deg (direct)
   Omega → node_deg (direct)
   MA → M0_deg (direct)
   epoch (string) → epoch_jd (parse date portion, convert to JD)
5. Resolve center: metadata.center_body → resolve_center_slug()
   ASSERT for Charon: resolved == "pluto_barycenter"
6. Build structured source object from metadata:
   {query_target: metadata.horizons_id,
    center: metadata.center_body,
    epoch: parsed epoch date string,
    retrieved: metadata.fetched}
```

### Step 5: Assemble coverage index

```
1. Assemble each object entry (osculating + positions + features + metadata)
2. Add schema_version, generated timestamp, generator version
3. Add serving_base, feature_configs path, scene_features
4. Assert all 8 validation invariants:
   #1: cache-required → positions != null
   #2: spacecraft → osculating == null && positions != null
   #3: analytic → osculating != null (warn at scale, assert for tranche)
   #4: parent-relative → parent in catalog with positions, overlapping coverage
   #5: osculating != null → osculating.center populated AND valid slug
   #6: every presets[].positions.file exists on disk
   #7: moon step_hours ≤ parent step_hours (grid nesting)
   #8: every positions.file exists on disk
5. Write coverage_index.json
```

### Step 6: Write feature configs (Phase 2 prep)

Read `SHELL_CONFIGS` from `shell_configs.py`. For each config entry in the
test objects' feature lists, extract renderer type and params. Write
`feature_configs.json` per the schema. Best-effort first pass — JS
renderers don't exist yet (Phase 2).

---

## 5. Position File Format (per handoff §3)

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
    "retrieved": "2026-06-15T10:30:00"
  },
  "data": {
    "t": [2460676.5, 2460676.75, ...],
    "x": [-123456.7, -118234.5, ...],
    "y": [345678.9, 348901.2, ...],
    "z": [1234.5, 1456.7, ...]
  }
}
```

---

## 6. Script Interface

```
python export_orbit_cache.py [--output-dir <path>] [--full-catalog] [--preflight-only]
```

- `--output-dir`: where to write (default: `../tonyquintanilla.github.io/data/solar-system/`)
- `--full-catalog`: export all objects in cache, not just test tranche
- `--preflight-only`: run Step 0 diagnostics and stop (no export)
- Prints summary: objects exported, files written, invariants checked,
  warnings.

---

## 7. Dependencies (desktop only, no new pip installs expected)

- `json`, `os`, `pathlib`, `datetime`, `argparse` (stdlib)
- `numpy` (for array operations, interpolation)
- `astropy.time` (for JD conversion — already installed for Horizons)
- Imports from orrery codebase: `celestial_objects.OBJECT_DEFINITIONS`,
  `constants_new` (AU conversion, verify symbol name), `shell_configs.SHELL_CONFIGS`
- Does NOT import: `orbit_data_manager`, `osculating_cache_manager`,
  `plotly`, `tkinter`

---

## 8. What to Verify After Build

1. **Provenance scan** on `export_orbit_cache.py` — Tier-1 = 0 before push.
2. **Manual spot-check**: open `positions/io.json` and verify:
   - Coordinates are in km (hundreds of thousands, not ~0.003 AU)
   - Timestamps are JD (not date strings)
   - `center` says `"jupiter"` (parent-relative, not Sun)
   - Point count matches the cache's resolution (NOT parent's coarser grid)
3. **Charon check**: `positions/charon.json` has `center: "pluto_barycenter"`
   and `osculating.center` in the coverage index also says `pluto_barycenter`.
4. **Invariant assertions**: the script prints all 8 checks and pass/fail.
5. **Round trip**: Tony copies output to gallery repo, pushes. A test page
   fetches `coverage_index.json` and one position file.

---

## 9. Lineage

- Design handoff: PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.6
- Master plan: v10
- Source code reviewed: orbit_data_manager.py, osculating_cache_manager.py
  (orrery repo HEAD)
- 4.8 manifest review (July 7, 2026): cache key resolution, parent
  interpolation, Saturn/Titan, Pluto/Charon center slug map
- Ledger: L-098 (data serving pipeline)

Build manifest v2 written July 2026 with Anthropic's Claude Opus 4.6.
