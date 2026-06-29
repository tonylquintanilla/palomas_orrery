# Adding New Objects to Paloma's Orrery
*Guide v1.2 - June 2026 | Tony + Claude*

---

## Overview: The Touchpoints

Every new object touches 2-4 files depending on its type.
The minimal path is always:

| File | What you add | Always? |
|------|-------------|---------|
| `celestial_objects.py` | Object dict in `OBJECT_DEFINITIONS` | YES |
| `constants_new.py` | Color entry in `color_map()` | YES |
| `palomas_orrery.py` | GUI checkbox | YES |
| `info_dictionary.py` | `INFO[name]` hover text | Recommended (enables Object Encyclopedia) |
| `orbital_elements.py` | `planetary_params` entry | Only if idealized orbit wanted |
| `orbital_elements.py` | `parent_planets` entry | Only for satellites/moons |

> **Adding an Earth System KMZ layer instead** (a Google Earth "blockbuster" +
> its web-gallery card) — that's a separate subsystem with its own pipeline and
> does not touch any of the files above. See **Section F**.

---

## Step 0: Look Up the Horizons ID

Before writing any code, go to [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) and confirm:

- **The ID that works** — try designation first (e.g. `2023 KQ14`), then record number (e.g. `90000355`) if designation is ambiguous
- **id_type** — `'smallbody'` for comets/asteroids, `None` or `'majorbody'` for planets/major moons, `'id'` for numeric-only IDs (Lagrange points, some special records)
- **Data arc** — start and end dates Horizons actually has data for
- **Object type** — periodic comet? Hyperbolic? TNO? Satellite?

**Ambiguity check:** If a comet designation like `10P` returns multiple records, you need the numeric record number (e.g. `90000214`). The comment above the entry should document this.

---

## Object Type Quick Reference

| What you're adding | `object_type` | `symbol` | GUI section | Section below |
|-------------------|--------------|----------|-------------|---------------|
| Asteroid, TNO, dwarf planet | `'orbital'` | `'circle-open'` | celestial_frame | A |
| Periodic comet | `'orbital'` | `'diamond'` | comet_frame | B |
| Hyperbolic / interstellar comet | `'orbital'` | `'diamond'` | interstellar_frame | B |
| Moon / satellite | `'satellite'` | `'circle'` | celestial_frame | C |
| Binary barycenter | `'barycenter'` | `'square-open'` | celestial_frame | D |

---

## Section A: Minor Planet / Asteroid / TNO / Dwarf Planet

### Step A1 — `celestial_objects.py`: Add to `OBJECT_DEFINITIONS`

**Simple smallbody** (no centered views needed):
```python
{'name': 'MyObject', 'id': '2023 XX1', 'var_name': 'myobject_var',
 'color_key': 'MyObject', 'symbol': 'circle-open', 'object_type': 'orbital',
 'id_type': 'smallbody',
 'mission_info': 'Horizons: 2023 XX1. One sentence description.',
 'mission_url': 'https://en.wikipedia.org/wiki/...'},
```

**If it has a moon or you want centered views** (add `center_id`):
```python
{'name': 'MyObject', 'id': '920XXXXXX', 'var_name': 'myobject_var',
 'color_key': 'MyObject', 'symbol': 'circle', 'object_type': 'orbital',
 'id_type': 'majorbody',
 'helio_id': '2023 XX1',        # smallbody designation for Sun-centered plots
 'helio_id_type': 'smallbody',
 'center_id': '920XXXXXX',      # primary body ID for centered views
 'mission_info': 'Horizons: XXXXXX MyObject. Description.',
 'mission_url': 'https://...'},
```

**JPL numeric ID scheme for binaries:**
- `20XXXXXX` = barycenter
- `920XXXXXX` = primary body  
- `120XXXXXX` = secondary (moon) — use this as query target, it's more reliable

**Symbol convention:** `'circle'` for named dwarf planets; `'circle-open'` for smaller/unnamed objects.

### Step A2 — `constants_new.py`: Add color

In the `color_map()` function, add one line in the appropriate section:
```python
'MyObject': 'rgb(218, 165, 32)',   # goldenrod - or any named color
```

Choose a color that:
- Distinguishes it visually from neighbors
- Fits the object's character (icy = blue-white, rocky = brown-grey, etc.)

### Step A3 — `palomas_orrery.py`: Add GUI checkbox

Find the appropriate section in `celestial_frame` (search for nearby objects by type).
Add using the standard `Checkbutton` pattern already in use for that section:
```python
# Near the other TNO/asteroid checkboxes
myobject_var = tk.BooleanVar()
myobject_cb = tk.Checkbutton(celestial_frame, text="MyObject", variable=myobject_var)
myobject_cb.grid(...)
```

**The `var_name` in `celestial_objects.py` must exactly match the Python variable name here.**
The `build_objects_list()` function in `celestial_objects.py` uses `var_name` to look up the
`tk.BooleanVar()` via `globals()`. If they don't match, the checkbox won't connect.

### Step A4 (optional) — `info_dictionary.py`: Add hover text

In the `INFO` dictionary:
```python
'MyObject': 'Horizons: 2023 XX1. Full description for hover panel and gallery. '
            'Orbital period: X years. Perihelion: Y AU. Discovered YYYY.',
```

**Object Encyclopedia:** Any object with an INFO entry automatically gets an interactive encyclopedia card in every HTML visualization. Hover or click the object, and an "i" button appears in the top-left corner. Click it to read the full reference text. This works in both the live orrery preview and saved HTML files -- no Studio curation needed. Objects without INFO entries simply don't show the button. This makes INFO entries more than hover text -- they're the object's encyclopedia page.

### Step A5 (optional) — `orbital_elements.py`: Add idealized orbit

Only needed if you want the dotted "ideal orbit" ellipse in addition to the Horizons trajectory.
In `planetary_params`:
```python
'MyObject': {
    'a': 0.922583,    # semi-major axis in AU  (Horizons: A)
    'e': 0.191481,    # eccentricity           (Horizons: EC)
    'i': 3.331,       # inclination, degrees   (Horizons: IN)
    'omega': 126.394, # arg. of perihelion, deg (Horizons: W)
    'Omega': 204.061, # long. ascending node   (Horizons: OM)
    'epoch': 'YYYY-MM-DD',
    'TP': 2460719.35  # time of perihelion, JD (Horizons: Tp)
},
```

Get all values from Horizons → Ephemeris → Orbital Elements output.

---

## Section B: Comets

Comets come in two flavors with different GUI sections.

| Type | e | GUI section | Function |
|------|---|-------------|----------|
| Periodic (returns) | < 1 | `comet_frame` | `create_comet_checkbutton()` |
| Hyperbolic / interstellar / sungrazer | >= 1 or extreme | `interstellar_frame` | `create_interstellar_checkbutton()` |

### Step B1 — `celestial_objects.py`: Add to `OBJECT_DEFINITIONS`

**Periodic comet:**
```python
{'name': 'MyComet', 'id': '90000355', 'var_name': 'comet_mycomet_var',
 'color_key': 'MyComet', 'symbol': 'diamond', 'object_type': 'orbital',
 'id_type': 'smallbody',
 # Optional date range if Horizons data arc is limited:
 # 'start_date': datetime(2010, 1, 1), 'end_date': datetime(2030, 12, 31),
 'mission_info': 'Horizons: 24P/MyComet. Jupiter-family comet, X-year period. Perihelion Y AU.',
 'mission_url': 'https://en.wikipedia.org/wiki/...'},
```

**Hyperbolic / interstellar / long-period:**
```python
{'name': 'MyComet', 'id': 'C/2025 X1', 'var_name': 'comet_mycomet_var',
 'color_key': 'MyComet', 'symbol': 'diamond', 'object_type': 'orbital',
 'id_type': 'smallbody',
 'start_date': datetime(2025, 1, 1), 'end_date': datetime(2026, 12, 31),
 'mission_info': 'Horizons: C/2025 X1. Description.',
 'mission_url': 'https://...'},
```

**Comet with fragments** — add `show_tails: False` to fragment entries:
```python
{'name': 'MyComet-B', 'id': '...', 'var_name': 'comet_mycomet_b_var',
 'color_key': 'MyComet-B', 'symbol': 'diamond', 'object_type': 'orbital',
 'id_type': 'smallbody', 'show_tails': False,   # suppresses tail visualization for fragment
 'mission_info': 'Fragment B of MyComet.'},
```

**Ambiguous designation:** If the short name (e.g. `67P`) returns multiple records in Horizons,
use the numeric record number (e.g. `90000699`) as the `id`. Document this in a comment above the entry.

### Step B2 — `constants_new.py`: Add color

```python
'MyComet': 'white',   # or rgb()
```

For fragments, add separate entries:
```python
'MyComet-B': 'rgb(0, 200, 220)',
'MyComet-C': 'rgb(255, 215, 0)',
```

### Step B3 — `palomas_orrery.py`: Add GUI checkbox

**Periodic comet** — add inside the `comet_frame` section:
```python
create_comet_checkbutton("MyComet", comet_mycomet_var, "(YYYY-present, periodic)",
                         "Perihelion: 1.XX AU, Month YYYY")
```

**Hyperbolic / interstellar** — add inside the `interstellar_frame` section:
```python
create_interstellar_checkbutton("MyComet", comet_mycomet_var, "(YYYY-MM-DD to YYYY-MM-DD)",
                                "Perihelion: X.XX AU, Month YYYY")
```

The variable `comet_mycomet_var` must be declared as `tk.BooleanVar()` before this call.
In practice, scan the existing comet_frame section for the declaration pattern and follow it.

### Step B4 (optional) — `info_dictionary.py`: Add hover text

```python
'MyComet': 'Horizons: C/2025 X1. Full description. Perihelion: X.XX AU (YYYY-MM-DD). '
           'Discovery: telescope/observer, date. Any notable features.',
```

---

## Section C: Satellite / Moon

### Step C1 — `celestial_objects.py`: Add to `OBJECT_DEFINITIONS`

```python
{'name': 'Vanth', 'id': '120090482', 'var_name': 'vanth_var',
 'color_key': 'Vanth', 'symbol': 'circle', 'object_type': 'satellite',
 'id_type': 'majorbody',
 'mission_info': 'Horizons: Vanth. Moon of Orcus. Binary period: 9.54 days.',
 'mission_url': 'https://...'},
```

**ID for satellites:** Use the JPL `120XXXXXX` scheme for secondaries of numbered bodies.
For planet moons (e.g. Triton = `803`), use the simple numeric ID with `id_type=None` or `'majorbody'`.

### Step C2 — `constants_new.py`: Add color

```python
'Vanth': 'rgb(169, 169, 169)',
```

### Step C3 — `orbital_elements.py`: Register in `parent_planets`

This tells the orrery to use satellite resolution when the parent is the center object:
```python
'Orcus': ['Vanth'],   # or append to existing list
```

For a new parent body:
```python
'MyDwarfPlanet': ['MoonA', 'MoonB'],
```

### Step C4 — `palomas_orrery.py`: Add GUI checkbox

Satellites usually go in `celestial_frame` near their parent.
Follow the existing pattern for nearby satellites.

### Step C5 (optional) — `orbital_elements.py`: Add idealized orbit

Same format as Section A5. Use elements from the satellite's orbit around its parent,
not around the Sun.

---

## Section D: Binary Barycenter

Only add if the mass ratio puts the barycenter **outside** the primary body.
(Rule of thumb: mass ratio > ~5% is worth showing.)

### Step D1 — `celestial_objects.py`:

```python
{'name': 'Orcus-Vanth Barycenter', 'id': '20090482', 'var_name': 'orcus_barycenter_var',
 'color_key': 'Orcus', 'symbol': 'square-open', 'object_type': 'barycenter',
 'mission_info': 'Center of mass for Orcus-Vanth system. Binary period: 9.54 days. Mass ratio: 16%.'},
```

No `mission_url` needed for barycenters.
`color_key` typically matches the primary body.

### Step D2 — `orbital_elements.py`: Register in `parent_planets`

```python
'Orcus-Vanth Barycenter': ['Orcus', 'Vanth'],
```

This enables binary system centering mode.

No `color_map` entry needed (barycenter inherits primary's color via `color_key`).

---

## Section E: Spacecraft / Mission

Missions differ from other objects in three ways: they use negative Horizons IDs, their
trajectories are fetched at fine time steps (not orbital point counts), and they get
encounter "Go" buttons automatically from `spacecraft_encounters.py`.

### Step E1 — Horizons: Find the spacecraft ID

Spacecraft use **negative integer IDs** in Horizons (e.g. `-98` = New Horizons, `-61` = Juno).
Search `https://ssd.jpl.nasa.gov/horizons/` for the spacecraft name.
Check the ephemeris header for:
- The ID (always negative)
- `Prior to` / `after` date limits — these become your `start_date` / `end_date`

### Step E2 — `celestial_objects.py`: Add to `OBJECT_DEFINITIONS`

```python
{'name': 'MyMission', 'id': '-999', 'var_name': 'mymission_var',
 'color_key': 'MyMission', 'symbol': 'diamond-open',
 'object_type': 'trajectory', 'id_type': 'id', 'is_mission': True,
 'start_date': datetime(2024, 10, 1), 'end_date': datetime(2031, 12, 31),
 'mission_url': 'https://...',
 'mission_info': 'Horizons: -999. One sentence description.'},
```

**Required fields that differ from other objects:**

| Field | Value | Why |
|-------|-------|-----|
| `id` | `'-999'` (string, negative) | All spacecraft use negative IDs |
| `id_type` | `'id'` | Forces Horizons to use numeric ID lookup |
| `object_type` | `'trajectory'` | Selects fine time-step fetch (not orbital points) |
| `symbol` | `'diamond-open'` | Convention: open diamond = spacecraft |
| `is_mission` | `True` | Routes to mission_frame GUI; gates encounter display |
| `start_date` / `end_date` | `datetime(...)` | Required; from Horizons ephemeris header |

**Do not** set `is_mission` on asteroid targets (Bennu, Ryugu) — those are separate
orbital objects. The spacecraft and its target are always separate entries.

### Step E3 — `constants_new.py`: Add color

```python
'MyMission': 'white',   # or any color / rgb()
```

Mission colors are often arbitrary — pick something visible on dark background.

### Step E4 — `palomas_orrery.py`: Add GUI checkbox

Declare the variable and call `create_mission_checkbutton()`. Find the right
chronological position in the `mission_frame` section (ordered by launch date):

```python
mymission_var = tk.BooleanVar()
# ... (declared near other variable declarations at top of GUI section)

create_mission_checkbutton("MyMission", mymission_var, "(2024-10-01 to 2031-12-31)")
```

The `create_mission_checkbutton()` function automatically:
- Creates the labeled checkbox
- Generates "Go" buttons for any encounters found in `spacecraft_encounters.py`
- Adds the hover tooltip from `INFO.get(name)`

No extra GUI code is needed for encounter buttons — they appear automatically
as soon as you add entries to `SPACECRAFT_ENCOUNTERS` in the next step.

### Step E5 (recommended) — `spacecraft_encounters.py`: Add encounters

This is what makes the mission educational. Each flyby, gravity assist, or
orbit insertion becomes a "Go" button under the checkbox. The encounter data
also feeds cross-reference markers under target body checkboxes (e.g., "Go:
New Horizons Gravity Assist" appearing under Jupiter).

**Add to `SPACECRAFT_ENCOUNTERS`:**

```python
'MyMission': [
    {
        'target': 'Earth',             # Must match name in celestial_objects.py
        'date': '2025-03-15 14:22:00', # UTC, authoritative from NASA/JPL docs
        'type': 'gravity_assist',      # flyby | gravity_assist | orbit_insertion |
                                       # orbit | landing | sample | sample_return |
                                       # end_of_mission | planned
        'dist_km': 500000,             # Center-to-center closest approach (km)
        'dist_au': 500000 / AU_KM,     # Same in AU (always compute, never hardcode)
        'v_kms': 8.5,                  # Relative velocity at encounter (km/s)
        'label': 'Earth Gravity Assist',
        'note': ('Educational note for hover text. What happened, why it matters, '
                 'one or two interesting numbers.'),
        'date_source': 'authoritative', # See date source convention below
        'status': 'completed',          # completed | planned | canceled
        'source': 'NASA/JPL',
        'center': 'Sun',               # Heliocentric view center
        'select_also': ['Earth'],      # Objects to auto-select with encounter preset
        'plot_days': 60,
        'plot_scale_au': 2.0,
        'center_closeup': 'Earth',     # Center for close-up "Go" view
        'plot_days_closeup': 7,
        'plot_scale_au_closeup': 0.05,
    },
    # Add more encounters as a list...
],
```

**Date source convention** — pick one per encounter:

| `date_source` | When to use |
|--------------|-------------|
| `'authoritative'` | Fixed event timestamp (burn, impact, orbit insertion). Never re-derive. |
| `'horizons'` | Proximity minimum with OEM data in Horizons. Derived via two-pass search. |
| `'planning'` | Future prediction not yet in Horizons; falls back gracefully. |

**Adaptive resolution is automatic:** The encounter system derives fetch step and
plot scale from `dist_km` and `v_kms` using two geometric formulas:
- Cube scale = `dist_km × 4` → frames the close-up view
- Arc time = `π × dist_km / v_kms` → drives fetch step (targets ~30 points through the closest-approach arc)

You only need to supply `dist_km` and `v_kms` — the system handles the rest.
If `v_kms` is unknown or unavailable, leave it `None` and the fallback uses the
`plot_scale_au_closeup` and `plot_days_closeup` values you supply.

### Step E6 (optional) — `spacecraft_encounters.py`: Add full-mission preset

This creates a "Go: Full Mission" button showing the entire trajectory at once.
Add to `SPACECRAFT_FULL_MISSION`:

```python
'MyMission': {
    'center': 'Sun',
    'select_also': ['Earth', 'Jupiter'],  # Targets to auto-select
    'start_date': '2024-10-01',
    'end_date': '2031-12-31',
    'plot_scale_au': None,               # None = auto-scale to data
    'fetch_step': '6h',                  # Coarser step for full-mission overview
    'label': 'Full Mission',
},
```

### Step E7 (optional) — `info_dictionary.py`: Add hover text

```python
'MyMission': 'Horizons: -999. Agency and mission description. '
             'Launch date, target, mission objectives. Key achievements.',
```

---

## Section E Summary: Files Touched for a Mission

| Step | File | What | Required? |
|------|------|------|-----------|
| E2 | `celestial_objects.py` | Object dict | YES |
| E3 | `constants_new.py` | Color | YES |
| E4 | `palomas_orrery.py` | Checkbox | YES |
| E5 | `spacecraft_encounters.py` | Encounter data | Recommended |
| E6 | `spacecraft_encounters.py` | Full-mission preset | Optional |
| E7 | `info_dictionary.py` | Hover text | Recommended |

---

## Section F: Earth System KMZ Layers (Google Earth blockbusters)

Earth System layers are a **separate subsystem** from the solar-system objects in
Sections A-E. They do not touch `celestial_objects.py`, `constants_new.py`, or
`palomas_orrery.py`. Instead a generator reads a climate/impact dataset and emits a
**pair** of artifacts in one run:

| Artifact | File | Where it's used |
|----------|------|-----------------|
| Teaser | `data/{scenario_id}_teaser.html` | Web gallery (fast 2D Plotly map) |
| KMZ | `data/{scenario_id}_blockbuster.kmz` | Google Earth Pro (the 3D "blockbuster") |

The teaser carries a `_kmz_handoff` string (the KMZ filename); the gallery viewer
reads it at view time and draws the green "Click 3D Earth" button. The button is
**viewer chrome**, not baked into the teaser — the teaser only holds the filename.

### Two generator families

| Family | Engine | Config lives in | Examples |
|--------|--------|-----------------|----------|
| **Grid scenarios** | `earth_system_generator.run_scenario(scenario)` | a `SCENARIOS` list | `scenarios_heatwaves.py` (28), `scenarios_coral_bleaching.py` (2), `scenarios_western_heatwave_march_2026.py` (dated series, ~10 KMZs) |
| **Bespoke generators** | a self-contained module with its own `run()` | the module itself | `food_insecurity_generator.py` (IPC GeoJSON -> Sudan) |

Grid scenarios share one engine, so an engine-level change (e.g. the KMZ "3+5"
info-card redesign, L-075) reaches **every grid scenario** on its next
regeneration. Bespoke generators have their **own** card/balloon code and do **not**
inherit engine changes — port the change in separately if you want it there.

### Step F1 — Define the scenario (grid family)

Add a dict to the `SCENARIOS` list (e.g. in `scenarios_heatwaves.py`):

| Key | Meaning |
|-----|---------|
| `scenario_id` | stable slug; drives every output filename (`{id}_blockbuster.kmz`, `{id}_teaser.html`) |
| `name` | human title shown on the teaser + KMZ balloon |
| `date` | `YYYY-MM-DD`; the dated snapshot (also the fetch cache key) |
| `lat_range`, `lon_range` | the map window |
| `description` | one-line tagline |
| `briefing` | the full narrative; `[TO-FETCH]` is auto-filled with the regional peak. **Every numeric claim needs an inline `# Source:` within scanner lookback (goal: Tier-1 = 0).** |
| `populations` | list of `{name, lat, lon, pop}` -> proportional impact circles + the balloon's Population Exposure key |
| `thresholds` | colour bands + height multiplier (e.g. `HEATWAVE_THRESHOLDS`) |
| `fetch` | the data fetcher (e.g. `fetch_era5_heatwave`), cache-aware via `data/weather_cache.json` keyed `lat_lon_date` |

For a **bespoke** layer, write a module whose `run()` ends by calling its own
`package_kmz(...)` and (optionally) `generate_plotly_teaser(...)`, emitting the same
`{scenario_id}_blockbuster.kmz` + `{scenario_id}_teaser.html` pair.

### Step F2 — Generate

Run the scenario module (grid) or the generator's `run()` (bespoke). One run writes
**both** the teaser HTML and the KMZ into `data/`. Cached date -> offline/instant;
uncached -> a network fetch (historical reanalysis is stable, so re-fetching a past
date reproduces the same bytes).

### Step F3 — View in Google Earth (orrery side)

Earth System Visualization GUI -> **Google Earth Layer Launcher** -> add
`data/{scenario_id}_blockbuster.kmz` -> launch. Requires Google Earth Pro. The
launcher (`earth_system_controller.py`) is a generic `.kml`/`.kmz` opener.

### Step F4 — Publish to the web gallery

1. Run `json_converter` on `data/{scenario_id}_teaser.html`. It is **interactive**:
   pick **Mode** (L landscape / P portrait / B both) and pass the **category**. It
   writes the JSON card(s) and stamps the `gallery_metadata.json` entry the proven
   way. **Never hand-edit `gallery_metadata.json`** — the converter is the producer
   that made every working card.
2. (Optional) set subcategory / labels / featured in the Gallery Editor.
3. Push to the gallery repo: the JSON card(s) **and** the KMZ into `gallery/assets/`.
   The card's `layout._kmz_handoff` = the KMZ basename, which the viewer turns into
   the green 3D-Earth button. Two card variants (`_teaser_gallery` desktop,
   `_teaser_mobile` portrait) can share one KMZ.

### Update discipline — what to re-push when you change something

The expensive mistakes are re-running the whole pipeline when you didn't need to,
and skipping a step when you did. Match the change to the artifact:

| What you changed | Teaser changes? | KMZ changes? | Re-push |
|------------------|:---:|:---:|---------|
| KMZ-side code only (intel card, balloon, overlays, KML builders) | no | yes | **KMZ only** -> `gallery/assets/`. Cards already point to the stable `{id}_blockbuster.kmz`. |
| Teaser-side code (`generate_plotly_teaser`, CTA, annotation) | yes | no | re-run `json_converter` -> push new card JSON (+ metadata only if structure changed) |
| Scenario **data** (date, region, briefing text, peak) | yes | yes | full pipeline: regenerate -> converter -> push card + KMZ |
| New scenario | new | new | full pipeline + new card + new metadata entry + KMZ |

Because the KMZ filename is stable per `scenario_id`, a pure-KMZ change is a drop-in
replacement: regenerate, copy the `_blockbuster.kmz` into `gallery/assets/`, push.
No teaser, converter, card, or metadata work. (This is why the L-075 3+5 rollout is
KMZ-only.)

### Files touched for an Earth System layer

| Step | File | What | Required? |
|------|------|------|-----------|
| F1 | `scenarios_*.py` (or a new generator module) | scenario dict / `run()` | YES |
| F2 | (none — run it) | produces teaser + KMZ in `data/` | YES |
| F3 | (none — launch it) | verify the KMZ in Google Earth Pro | to verify |
| F4 | gallery repo `gallery/` + `gallery/assets/` | card JSON + KMZ | to publish |

### Common mistakes (Earth System)

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Hand-editing `gallery_metadata.json` | broken nav / invalid JSON | always go through `json_converter` |
| Pushing the card but not the KMZ | green 3D button 404s | push `{id}_blockbuster.kmz` to `gallery/assets/` |
| Regenerating teasers for a KMZ-only change | wasted converter runs, churned cards | KMZ-only -> push only the KMZ |
| Expecting a bespoke generator to inherit engine changes | the food-insecurity card still looks old after an engine fix | port the change into that generator |
| Balloon HTML shows as raw `<div>` tags in GE | `simplekml` entity-escaped the description | wrap the balloon HTML in `<![CDATA[ ... ]]>` — `simplekml` leaves CDATA untouched |
| Population Exposure key on a non-population layer (e.g. coral) | a "Megacity / Major / Region" key appears where it makes no sense | the 3+5 balloon currently always includes it; gate on `populations` if it doesn't fit |
| Unsourced number in `briefing` | provenance scanner Tier-1 > 0 | inline `# Source:` within lookback, or remove + note the gap |
| Non-ASCII in a scenario string | Windows console / encoding mangling | ASCII only |

---

## Checklist: Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| `var_name` doesn't match Python variable | Object never appears, no error | Match exactly |
| Wrong `id_type` for Horizons | Fetch fails silently | Test in Horizons web UI first |
| Ambiguous designation → multiple records | Wrong orbit returned | Use numeric record ID |
| Missing `color_map` entry | `KeyError` or grey dot | Add to `constants_new.py` |
| Fragment without `show_tails: False` | Tail code runs on a fragment with bad data | Add the flag |
| Satellite not in `parent_planets` | Satellite plots in solar frame, not centered | Add to `orbital_elements.py` |
| `start_date`/`end_date` outside data arc | No data fetched, silent | Match to Horizons arc |
| Comet in wrong GUI section | Wrong display label / date format | Periodic → comet_frame; hyperbolic → interstellar_frame |
| Spacecraft `id_type` not `'id'` | Horizons can't find spacecraft by name | Always use `'id'` for negative IDs |
| Missing `is_mission: True` | Spacecraft lands in wrong GUI section; no encounter Go buttons | Add the flag |
| Encounter `dist_au` hardcoded | Drifts if `dist_km` is corrected | Always compute `dist_km / AU_KM` |
| Encounter `date_source` wrong | `'horizons'` triggers unnecessary two-pass search on historical burns | Use `'authoritative'` for fixed event timestamps |
| `v_kms` missing from encounter | Adaptive resolution falls back to coarse whole-day logic | Supply from mission docs; estimate beats nothing |

---

## Quick Lookup: ID Types

| Situation | `id_type` value |
|-----------|----------------|
| Planet, major moon (numbered) | `None` |
| Asteroid by designation (e.g. `2023 KQ14`) | `'smallbody'` |
| Comet by designation (e.g. `C/1995 O1`) | `'smallbody'` |
| Comet by record number (e.g. `90000355`) | `'smallbody'` |
| Major body by numeric ID (e.g. `920090482`) | `'majorbody'` |
| Lagrange point / special numeric ID | `'id'` |
| K1 parent using SPK-ID `90004912` | `'id'` |

---

## Delivery Format Options

This guide exists as a Markdown file you can keep in the repo.
Two other options are available on request:

**Option 1 (this file):** Reference markdown — upload to any Claude session as context.

**Option 2: Interactive snippet generator** — a Claude-powered artifact where you fill in
name, Horizons ID, type, and it generates all four code blocks ready to paste.

**Option 3: Session-based** — paste a Horizons web output to Claude in a session,
and Claude generates all the additions from scratch.

Options 2 and 3 are good for high-frequency additions. Option 1 is the right foundation.

---

*Guide v1.0 - April 2026*
*Module updated: April 2026 with Anthropic's Claude Sonnet 4.6*
*Section F (Earth System KMZ Layers) added June 2026 with Anthropic's Claude Opus 4.8*
