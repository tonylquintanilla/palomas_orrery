# PHASE 1B BUILD MANIFEST — export_orbit_cache.py (v3)

**Type:** BUILD MANIFEST (Mode 2 — agentic, new module)
**Design source:** PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.6 (+ v3 handoff
deltas listed in §10 — apply to handoff before or with the build)
**Base:** orrery — resolve live HEAD at build session start (do NOT hardcode)
**Pre-build gates:**
(1) diff `f1ede52..<live HEAD>` for the 10 source files —
    **RUN AND PASSED at `3e21970`** (July 7, 2026, Fable 5 session, via
    `git clone --filter=blob:none` + `git diff --name-status`): 4 commits,
    documentation + ledger only, zero source files touched. If HEAD has
    moved past `3e21970` at build start, re-run for `3e21970..<live HEAD>`
    only.
(2) pre-flight verification (Step 0 below) — includes the moon-cadence
    decision gate (Step 0-STOP), which Tony rules on BEFORE the export
    code is written.
**Post-build gate:** provenance scan Tier-1 = 0 on new module before push

**v3 changes from v2:** Fable 5 manifest verification incorporated (all
checks run against code at orrery HEAD `3e21970`, not handoff prose).
Pre-build diff gate executed and recorded as PASSED. AU constant resolved:
`KM_PER_AU` (the name `AU_TO_KM` does not exist — v2's pre-flight snippet
would fail). `shell_configs` import-cleanliness claim corrected: it
transitively imports plotly (no tkinter) — acceptable for a desktop
devtool; §2/§7 reworded. `NEEDS_POSITIONS` comprehension bug fixed
(selected category, not availability — moons were silently excluded;
named unpacking now). Pluto added to `PARENT_OBJECTS` and `pluto.json`
produced (resolves Charon's failure of invariant #4; honors handoff
v0.3 option (b) — parents of moons serve position files). Invariant #4
strengthened: parent coverage must CONTAIN (not overlap) the moon's
window — `np.interp` silently clamps out-of-range and corrupts end
segments. Invariant #7 rewritten for the interpolation design (nesting
rationale was stale); composition contract recorded for Phase 2.
Moon-cadence risk upgraded from "verify at build" to code-confirmed:
every cache write path keys points date-only (`%Y-%m-%d`) — sub-daily
samples collide; the stop/go WILL fire for inner moons; decision branch
moved ahead of the build. Pre-flight 0e gains unit sanity print; new 0f
dumps an osculating entry and asserts the `Charon@9` key. Step 4 handles
`MA = None` (stored via `.get()`). Voyager frame comment aligned to
`arc-natural`. Post-build checks extended (Earth–Moon interpolation
scallop, Mode 5).

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
| `data/osculating_cache.json` | Osculating elements per object | Direct JSON load (no tkinter dep) — path verified at HEAD: `CACHE_DIR = Path(__file__).parent / 'data'` |
| `celestial_objects.py` | `OBJECT_DEFINITIONS` — Horizons IDs, categories, parents | Import — **verified clean at HEAD** (imports only `datetime`) |
| `constants_new.py` | `KM_PER_AU` = 149597870.7 — **verified at HEAD; the name `AU_TO_KM` does not exist** | Import |
| `shell_configs.py` | `SHELL_CONFIGS` — feature rendering parameters | Import — **NOT plotly-clean at HEAD**: transitively imports `plotly.graph_objs` via the `*_visualization_shells` modules and `planet_visualization_utilities`. **No tkinter anywhere in the chain** (verified by grep at `3e21970`). Acceptable: this is a desktop devtool and plotly is installed. Do NOT attempt to strip the dependency in Phase 1b |
| `close_approach_data.py` | Preset definitions for close approaches, perihelia | Import — **verified clean at HEAD** (stdlib + `constants_new`) |

**Import verification (bare interpreter, informational — plotly loading via
shell_configs is EXPECTED, not a failure):**
```
python -c "from celestial_objects import OBJECT_DEFINITIONS; print('OK')"
python -c "from constants_new import KM_PER_AU; print(KM_PER_AU)"
python -c "from shell_configs import SHELL_CONFIGS; print('OK')"  # pulls plotly; fine
python -c "import close_approach_data; print('OK')"
```

---

## 3. Outputs (to target directory)

```
<output_dir>/
├── coverage_index.json          # The schema v0.6 manifest (+ v3 deltas, §10)
├── feature_configs.json         # Renderer + params from SHELL_CONFIGS
├── positions/
│   ├── earth.json               # Heliocentric, km (parent of Moon)
│   ├── jupiter.json             # Heliocentric, km (parent of Io)
│   ├── saturn.json              # Heliocentric, km (parent of Titan)
│   ├── pluto.json               # Heliocentric, km — the BARYCENTER trajectory
│   │                            #   (trajectory_of: pluto_barycenter); parent
│   │                            #   of Charon. Contingent on Step 0b (target 9)
│   ├── moon.json                # Parent-relative to Earth, km
│   ├── io.json                  # Parent-relative to Jupiter, km
│   ├── titan.json               # Parent-relative to Saturn, km
│   ├── charon.json              # Parent-relative to Pluto barycenter, km
│   └── voyager_1.json           # frame: arc-natural (heliocentric-stored
│                                #   vectors, km, write-once)
└── presets/
    └── (apophis_2029_close_approach.json — only if 2029 data exists)
```

**Not produced:** Apophis position file (analytic, preset only — and the
preset is likely null for the test tranche since the desktop cache probably
covers 2025–2026, not 2029).

**Pluto note (v3):** `pluto.json` IS produced. Handoff v0.3 settled option
(b): parents of moons serve position files, cache-exact composition, no
hidden analytic fallback. v2 excluded Pluto, which made Charon fail
invariant #4 by the manifest's own assertion. The file is the Pluto–Charon
barycenter heliocentric trajectory (what the `Pluto_Sun` cache pair holds
if Step 0b confirms target 9), consistent with `trajectory_of`. Marginal
cost ~100 KB.

**Apophis note:** Without 2029 data, Apophis exercises only the plain
analytic path. The "self-contained preset" schema pattern goes untested
in Phase 1b. This is explicitly acceptable — the pattern is validated
when preset data is available.

---

## 4. Processing Steps (in dependency order)

### Step 0: Pre-flight verification

**This step runs before any export code is written.** It answers the
questions the manifest cannot answer from documentation alone.
`--preflight-only` runs 0a–0f and stops. **Capture the full output and
paste it into the build session** — it is the ground truth the build
proceeds on.

**What is already answered from code at HEAD (`3e21970`), no longer
pre-flight unknowns:**
- AU constant name: `KM_PER_AU` (149597870.7).
- Pair key construction: `f"{name}_{center_object_name}"` — so
  `"Voyager 1_Sun"` (with space) is correct.
- Osculating cache keys: `get_cache_key('Charon','@9')` → `'Charon@9'`;
  heliocentric entries are bare names (`'Pluto'`).
- Osculating element fields: `a, e, i, omega, Omega, epoch, TP, MA, TA` —
  `epoch` is a string like `"2026-01-01 osc."`; `MA` and `TA` are stored
  via `.get()` and **may be None**.
- Osculating metadata fields: `fetched` (isoformat), `source`,
  `solution_date`, `horizons_id`, `display_name`, `center_body`
  (default `'@sun'`).
- **Cache write paths key `data_points` by `strftime("%Y-%m-%d")` —
  date-only.** Sub-daily samples collide into one key and silently
  overwrite. See Step 0-STOP below.

**What pre-flight still verifies (the on-disk file can predate the
current writer):**

```python
# 0a. Cache key resolution + actual on-disk cadence
import json
with open('data/orbit_paths.json', 'r') as f:
    cache = json.load(f)

io_entry = cache.get('Io_Sun', {})
keys = sorted(io_entry.get('data_points', {}).keys())
print(f"Io_Sun: {len(keys)} data points")
print(f"First 10 keys: {keys[:10]}")
print(f"Last 5 keys: {keys[-5:]}")
# Code at HEAD writes date-only keys. If these keys carry time
# ("YYYY-MM-DD HH:MM"), the data predates or postdates the current
# writer -- report it either way.

# 0b. Pluto pair key -- what Horizons target is stored?
pluto_entry = cache.get('Pluto_Sun', {})
pluto_meta = pluto_entry.get('metadata', {})
print(f"Pluto_Sun center_body: {pluto_meta.get('center_body')}")
print(f"Pluto_Sun data points: {len(pluto_entry.get('data_points', {}))}")
# Target 9 (barycenter): Charon subtraction is consistent; pluto.json
#   is the barycenter trajectory as designed.
# Target 999 (body): Charon subtraction will mismatch osculating.
#   Options: re-fetch as target 9, or adjust Charon's osculating.center.
#   Tony decides.

# 0c. Saturn presence -- required for Titan
saturn_entry = cache.get('Saturn_Sun', {})
print(f"Saturn_Sun present: {bool(saturn_entry)}")
print(f"Saturn_Sun data points: {len(saturn_entry.get('data_points', {}))}")

# 0d. Import checks (informational; shell_configs pulling plotly is expected)
from celestial_objects import OBJECT_DEFINITIONS
print(f"OBJECT_DEFINITIONS: {len(OBJECT_DEFINITIONS)} objects")
from constants_new import KM_PER_AU
print(f"KM_PER_AU: {KM_PER_AU}")

# 0e. Date coverage + unit sanity
for key in ['Earth_Sun', 'Jupiter_Sun', 'Saturn_Sun', 'Pluto_Sun',
            'Moon_Sun', 'Io_Sun', 'Titan_Sun', 'Charon_Sun',
            'Voyager 1_Sun', 'Apophis_Sun']:
    entry = cache.get(key, {})
    dp = entry.get('data_points', {})
    meta = entry.get('metadata', {})
    dates = sorted(dp.keys()) if dp else []
    print(f"{key}: {len(dates)} pts, "
          f"{dates[0] if dates else 'N/A'} to {dates[-1] if dates else 'N/A'}, "
          f"center={meta.get('center_body', 'N/A')}")
    if dates:
        p = dp[dates[0]]
        print(f"  sample xyz: ({p['x']:.6f}, {p['y']:.6f}, {p['z']:.6f})")
# Unit sanity: Earth sample magnitude ~1.0 confirms AU (schema converts
# to km via KM_PER_AU). Magnitudes in the hundreds of millions would
# mean km already -- stop and reconcile before writing conversion code.

# 0f. Osculating cache structure (new in v3)
with open('data/osculating_cache.json', 'r') as f:
    osc = json.load(f)
print(f"osculating entries: {len(osc)}")
assert 'Charon@9' in osc, "Charon@9 barycentric elements missing"
sample = osc.get('Jupiter', {})
print(f"Jupiter elements keys: {sorted(sample.get('elements', {}).keys())}")
print(f"Jupiter metadata keys: {sorted(sample.get('metadata', {}).keys())}")
print(f"Jupiter MA: {sample.get('elements', {}).get('MA')}")  # may be None
```

### Step 0-STOP: the moon-cadence decision gate *(v3 — decide BEFORE build)*

**Code-confirmed at HEAD:** every `data_points` write path in
`orbit_data_manager.py` keys points date-only, and points are placed at
computed uniform dates, not Horizons' returned timestamps. The cache as
written by current code **cannot hold sub-daily moon trajectories** —
four 6h samples per day collapse into one key. Therefore, at daily
cadence: Io ≈ 0.57 points per orbit (unusable), Titan ≈ 64 (fine),
Moon ≈ 27 (renderable but chunky — Mode 5 call).

The v2 stop/go treated this as a maybe; it is now the expected outcome,
and its option (a) "re-fetch moons at 6h" is **not just a re-fetch — it
requires a desktop code change** (time-bearing keys), which this manifest
declares out of scope. So the branch is decided by Tony ahead of the
build, informed by 0a/0e output:

- **(i) Ship the daily tranche.** Planets, spacecraft, Titan, and (Mode 5
  permitting) the Moon at daily cadence. Io drops to analytic-only
  (osculating conic still renders its orbit shape). Fine-cadence moons
  become a scoped follow-on: desktop time-keyed cache upgrade with L-079
  "assembler-must-inherit" delta-log discipline, then a re-export.
- **(ii) Pull the desktop change into Phase 1b.** Time-bearing keys in
  `orbit_data_manager.py` (backward-compatible read of both key formats),
  moon re-fetch at 6h, then export. Larger scope, one fewer phase.

Either way the schema is untouched — `step_hours` already expresses both
worlds. If 0a reveals time-bearing keys on disk (data predating/
postdating the current writer), report and reassess.

- If Pluto is body-999 → see 0b options. Tony decides.
- If Saturn is missing → drop Titan from tranche. Log it.

### Step 1: Load and validate inputs

```
load orbit_paths.json -> raw_cache
load osculating_cache.json -> osc_cache
import OBJECT_DEFINITIONS, KM_PER_AU, SHELL_CONFIGS
```

### Step 2: Define test tranche

```python
# Center body -> slug map (explicit, not string-strip)
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

from collections import namedtuple
TestObject = namedtuple('TestObject',
    'slug cache_pair_key osc_key horizons_id category availability '
    'parent stored_center canonical_frame trajectory_of features')

TEST_OBJECTS = [
    TestObject("earth",     "Earth_Sun",     "Earth",     "399",   "planet",       "analytic",       "sun",     "sun",              "heliocentric",    None,               ["van_allen_belts", "atmosphere_shell"]),
    TestObject("jupiter",   "Jupiter_Sun",   "Jupiter",   "599",   "planet",       "analytic",       "sun",     "sun",              "heliocentric",    None,               ["magnetosphere", "ring_system"]),
    TestObject("saturn",    "Saturn_Sun",    "Saturn",    "699",   "planet",       "analytic",       "sun",     "sun",              "heliocentric",    None,               ["ring_system"]),
    TestObject("moon",      "Moon_Sun",      "Moon",      "301",   "moon",         "cache-required", "earth",   "earth",            "parent-relative", None,               None),
    TestObject("io",        "Io_Sun",        "Io",        "501",   "moon",         "cache-required", "jupiter", "jupiter",          "parent-relative", None,               None),
    TestObject("titan",     "Titan_Sun",     "Titan",     "606",   "moon",         "cache-required", "saturn",  "saturn",           "parent-relative", None,               None),
    TestObject("pluto",     "Pluto_Sun",     "Pluto",     "999",   "dwarf_planet", "analytic",       "sun",     "sun",              "heliocentric",    "pluto_barycenter", None),
    TestObject("charon",    "Charon_Sun",    "Charon@9",  "901",   "moon",         "cache-required", "pluto",   "pluto_barycenter", "parent-relative", None,               None),
    TestObject("apophis",   "Apophis_Sun",   "Apophis",   "99942", "asteroid",     "analytic",       "sun",     "sun",              "heliocentric",    None,               None),
    TestObject("voyager_1", "Voyager 1_Sun", None,        "-31",   "spacecraft",   "spacecraft",     "sun",     "sun",              "arc-natural",     None,               None),
]

# Parents whose position files are required for moon composition.
# v3: pluto added (Charon's parent; the served trajectory is the
# barycenter's, per trajectory_of). Resolves invariant #4 for Charon.
PARENT_OBJECTS = {"earth", "jupiter", "saturn", "pluto"}

# Objects that need position files written.
# v3 FIX: v2's comprehension read _[3] (category), not availability --
# moons were silently excluded and only failed three steps later at the
# invariant gate. Named fields make the bug untranscribable.
NEEDS_POSITIONS = {o.slug for o in TEST_OBJECTS
                   if o.availability in ("cache-required", "spacecraft")} \
                  | PARENT_OBJECTS
```

**Note:** Voyager's `osc_key` is `None` — spacecraft have no osculating
elements (invariant #2).

**Note:** Charon's `osc_key` is `"Charon@9"` (barycentric elements,
key convention verified against `get_cache_key()` at HEAD). The export
script asserts that its resolved center equals `pluto_barycenter`.

### Step 3: Extract position data for each object

For each object in `NEEDS_POSITIONS`:

```
1. Look up pair_key in raw_cache (e.g. "Io_Sun")
2. If not found -> log warning, skip
3. Extract data_points dict
4. Sort by date key, parse to JD timestamps
5. Extract x, y, z coordinate arrays
6. Convert AU to km (multiply by KM_PER_AU)
7. For parent-relative moons:
   a. Look up parent's pair key (e.g. "Jupiter_Sun")
   b. Parse parent's dates to JD, extract parent x, y, z in km
   c. ASSERT COVERAGE CONTAINMENT (v3, invariant #4): parent's time
      range must CONTAIN the moon's -- parent_t[0] <= moon_t[0] and
      parent_t[-1] >= moon_t[-1]. numpy.interp silently clamps
      out-of-range values (flat-lines the parent), corrupting the end
      segments with no error. Fail loud here, not silently there.
   d. INTERPOLATE parent onto moon's timestamps using numpy.interp
      on each coordinate independently (NOT grid intersection --
      intersection decimates moon resolution) *(4.8 catch 2)*
   e. Subtract interpolated parent from moon at each timestamp
   f. The result is parent-relative in km at the moon's full cadence
   g. ASSERT: Charon's resolved center == pluto_barycenter *(4.8 catch 4)*
8. Write column-oriented JSON position file with provenance header
```

**Why interpolation, not intersection *(4.8 catch 2)*:** Intersecting a
fine moon grid with a coarser parent grid keeps only the coarse-aligned
points — throwing away most moon samples. Interpolating the parent
(smooth planetary motion) preserves the moon's full cadence.

**Interpolation error budget *(v3, replaces the stale nesting rationale)*:**
Linear-interp chord error for a parent sampled at step θ (radians of its
orbit) is ≈ r·θ²/8 at chord midpoints (arithmetic estimate, not fetched).
At DAILY parent cadence: Jupiter ≈ 205 km ≈ 0.05% of Io's orbit radius
(invisible); Saturn ≈ 61 km ≈ 0.005% of Titan's (invisible); Pluto
negligible; **Earth ≈ 5,500 km ≈ 1.4% of the Moon's 384,400 km** — a
daily-period scallop in the Earth–Moon parent-relative view that may be
Mode 5 visible. If the Moon ships (Step 0-STOP branch (i)), the render
adjudicates; if it scallops, Earth needs finer cadence in the follow-on
fetch. Invariant #7 encodes the budget.

**Composition contract *(v3 — record for Phase 2)*:** Wide-view runtime
composition is `heliocentric = interp(parent columns, at moon t, linear,
per-coordinate) + moon_relative` — the SAME operation the export used
for the subtraction, on the SAME served parent points. Matching method +
matching points ⇒ recomposition is exact (float rounding aside). Write
this contract into the coverage index as a top-level field, e.g.
`"composition": {"method": "linear_interp_per_coordinate"}`, so the
Phase 2 assembler cannot innocently diverge.

### Step 4: Build osculating entries for coverage index

For each object with `osc_key is not None`:

```
1. Look up osc_key in osc_cache (e.g. "Jupiter", "Charon@9")
2. If not found -> log warning (invariant #3 catches at assembly)
3. Extract elements dict
4. Map fields (verified against osculating_cache_manager.py at HEAD):
   a -> a_au (direct)
   e -> e (direct)
   i -> i_deg (direct)
   omega -> peri_deg (direct)
   Omega -> node_deg (direct)
   MA -> M0_deg -- MA is stored via .get() and MAY BE None (v3).
     If None: try TA -> M0 conversion via e (standard anomaly relation),
     else emit osculating with M0_deg absent + loud warning. Never
     invent a value; never let None serialize as 0.0.
   epoch (string, "YYYY-MM-DD osc.") -> epoch_jd (parse date portion,
     convert to JD via astropy.time)
5. Resolve center: metadata.center_body -> resolve_center_slug()
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
3. Add serving_base, feature_configs path, scene_features, composition
   contract (Step 3)
4. Assert all 8 validation invariants:
   #1: cache-required -> positions != null
   #2: spacecraft -> osculating == null && positions != null
   #3: analytic -> osculating != null (warn at scale, assert for tranche)
   #4: parent-relative -> parent in catalog with positions, and parent
       coverage CONTAINS this object's window (v3: containment, not
       overlap -- the np.interp clamp hazard)
   #5: osculating != null -> osculating.center populated AND valid slug
   #6: every presets[].positions.file exists on disk
   #7: (v3 rewrite) parent step_hours <= 24 for any parent of a served
       moon -- the interpolation error budget (Step 3). The v2/handoff
       "grid nesting" form is retired: the algorithm interpolates by
       design; nesting is neither required nor checked.
   #8: every positions.file exists on disk
5. Write coverage_index.json
```

### Step 6: Write feature configs (Phase 2 prep)

Read `SHELL_CONFIGS` from `shell_configs.py` (plotly loads transitively —
expected, see §2). For each config entry in the test objects' feature
lists, extract renderer type and params. Write `feature_configs.json` per
the schema. Best-effort first pass — JS renderers don't exist yet (Phase 2).

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
    "t": [2460676.5, 2460677.5, ...],
    "x": [-123456.7, -118234.5, ...],
    "y": [345678.9, 348901.2, ...],
    "z": [1234.5, 1456.7, ...]
  }
}
```

Voyager's file carries `"frame": "arc-natural"` (v3 — v2's §3 comment said
"Heliocentric"; the vectors are heliocentric-stored but the schema frame
value is `arc-natural`, and the file says what the schema says).

---

## 6. Script Interface

```
python export_orbit_cache.py [--output-dir <path>] [--full-catalog] [--preflight-only]
```

- `--output-dir`: where to write (default: `../tonyquintanilla.github.io/data/solar-system/`)
- `--full-catalog`: export all objects in cache, not just test tranche
- `--preflight-only`: run Step 0 diagnostics and stop (no export).
  Capture and paste the output into the build session.
- Prints summary: objects exported, files written, invariants checked,
  warnings.

---

## 7. Dependencies (desktop only, no new pip installs expected)

- `json`, `os`, `pathlib`, `datetime`, `argparse`, `collections` (stdlib)
- `numpy` (array operations, interpolation)
- `astropy.time` (JD conversion — already installed for Horizons)
- Imports from orrery codebase: `celestial_objects.OBJECT_DEFINITIONS`,
  `constants_new.KM_PER_AU`, `shell_configs.SHELL_CONFIGS`,
  `close_approach_data` (Apophis preset metadata)
- Does NOT import: `orbit_data_manager`, `osculating_cache_manager`,
  `tkinter`
- plotly loads transitively via `shell_configs` (v3 — verified at HEAD;
  acceptable on the desktop, not a defect)

---

## 8. What to Verify After Build

1. **Provenance scan** on `export_orbit_cache.py` — Tier-1 = 0 before push.
2. **Manual spot-check**: open `positions/io.json` (or the finest moon that
   shipped) and verify:
   - Coordinates are in km (hundreds of thousands, not ~0.003 AU)
   - Timestamps are JD (not date strings)
   - `center` says the parent slug (parent-relative, not Sun)
   - Point count matches the cache's cadence (NOT decimated to the
     parent's grid)
3. **Charon check**: `positions/charon.json` has `center: "pluto_barycenter"`
   and `osculating.center` in the coverage index also says
   `pluto_barycenter`; `positions/pluto.json` exists (parent file).
4. **Invariant assertions**: the script prints all 8 checks and pass/fail.
5. **Earth–Moon scallop (Mode 5, if the Moon shipped)**: render the Moon
   parent-relative and look for a daily-period ripple in the orbit —
   the interpolation-residual signature from daily Earth cadence
   (Step 3 error budget). Tony's eyes adjudicate.
6. **Round trip**: Tony copies output to gallery repo, pushes. A test page
   fetches `coverage_index.json` and one position file. Confirm the
   `composition` contract field is present for Phase 2.

---

## 9. Lineage

- Design handoff: PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.6
  (v3 handoff deltas in §10)
- Master plan: v10
- Source code reviewed: orbit_data_manager.py, osculating_cache_manager.py
  (orrery repo HEAD)
- 4.8 manifest review (July 7, 2026): cache key resolution, parent
  interpolation, Saturn/Titan, Pluto/Charon center slug map
- Fable 5 manifest verification (July 7, 2026): both repo HEADs confirmed
  by `git ls-remote` (orrery `3e21970`, gallery `4b086a6`); pre-build
  diff gate RUN AND PASSED (`f1ede52..3e21970`, docs + ledger only);
  manifest assumptions checked against code at HEAD (`KM_PER_AU`,
  import chains, cache paths, key conventions, element/metadata fields,
  date-only write keys); four catches (NEEDS_POSITIONS field bug,
  Pluto parent file, interp containment/clamp hazard, invariant #7
  rewrite) + moon-cadence decision gate
- Ledger: L-098 (data serving pipeline)

## 10. Handoff v0.6 Deltas Required (apply as handoff v0.7, or fold into build session)

So the design document and this manifest do not silently diverge:

1. Invariant #4: "time coverage overlapping" → "time coverage
   **containing** this object's window" (np.interp clamp hazard).
2. Invariant #7: retire the grid-nesting form; replace with the parent
   cadence bound (parent step ≤ 24h for parents of served moons) and
   reference the interpolation error budget.
3. Cross-Object Parent Dependency section: note the runtime composition
   contract (linear per-coordinate interpolation, same served parent
   points) and the new index-level `composition` field.
4. Source structures section: AU constant is `KM_PER_AU`; cache write
   keys are date-only at HEAD (moon-cadence consequence, Step 0-STOP);
   `MA` may be None; `shell_configs` carries transitive plotly.
5. Test-object/schema examples: `pluto.json` is served (parent of Charon).

Also: L-098's Gap line should record the diff gate as passed at
`3e21970` and bump refs to handoff v0.6 + manifest v3.

---

Build manifest v2 written July 2026 with Anthropic's Claude Opus 4.6.
Build manifest v3 written July 2026 with Anthropic's Claude Fable 5.
