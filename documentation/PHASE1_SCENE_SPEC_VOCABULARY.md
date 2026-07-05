# Phase 1 Deliverable: Scene-Spec Vocabulary — Solar System Domain

**Type:** Design session output (zero code)
**Author:** Claude Fable 5, July 4, 2026, via collegial relay (Tony Quintanilla)
**Base:** main @ `fdb66ca6e959d2cceb90ecd0408f38783b5f1825` (SHA round trip confirmed
against remote HEAD at session start). `palomas_orrery.py` and
`celestial_objects.py` verified byte-identical (md5) between the prompt's base
`7b25eb9` and this HEAD — the analysis target is exactly what the task prompt
specified.
**Inputs read:** `palomas_orrery.py` (11,110 lines, fetched at SHA),
`celestial_objects.py` (fetched at SHA), `palomas_orrery_helpers.py` (fetched
at SHA, for `get_animation_axis_range` signature only), `shell_configs.py`
(fetched at SHA, for shell key structure), `MASTER_PLAN_WEB_PUBLICATION.md` v6,
`SECTION_W_DRAFT.md`, orrery-coding-conventions skill.
**Scope:** Deliverables 1–5 per the task prompt (vocabulary + coverage-index
slice of Phase 1). Seam gate-check and scene-equivalence criteria are out of
scope per the prompt's scope boundary.

---

## 0. Summary — the vocabulary at a glance

Every spec is a plain JSON-serializable dict. Datetimes are ISO-8601 strings.
No tkinter types, no widget references, no callables.

**Shared skeleton (all domains):**

| Field | Type | Values / default |
|---|---|---|
| `spec_version` | str | `"1.0"` |
| `domain` | str | `solar_system` \| `stars` \| `orbital_params` \| `earth_system` |
| `content_type` | str | `static` \| `animation` |
| `preset_id` | str \| None | tier-2 curated preset ID; None = fully explicit spec |
| `title` | str \| None | None = assembler auto-generates |

**Solar system vocabulary (domain payload):**

| Field | Type | Default | Source widget(s) |
|---|---|---|---|
| `objects` | list[str] | required | `obj['var']` checkboxes |
| `center` | str | `"Sun"` | `center_object_var` |
| `epoch` | ISO datetime | required | `entry_year/month/day/hour/minute` |
| `window.start` | ISO datetime | = epoch | same date entries (via `get_interval_settings`) |
| `window.end` | ISO datetime | required | `end_entry_year/.../minute` |
| `sampling.orbital_points` | float | 50 | `orbital_points_entry` |
| `sampling.trajectory_points` | float | 50 | `trajectory_points_entry` |
| `sampling.satellite_points` | float | 50 | `satellite_points_entry` |
| `sampling.satellite_days` | int | 50 | `satellite_days_entry` |
| `orbits.apsidal_markers` | bool | False | `show_apsidal_markers_var` |
| `orbits.closest_approach_markers` | bool | False | `show_closest_approach_var` |
| `shells` | dict[str, list[str]] | `{}` | `sun_shell_vars`, `planet_shell_vars` (13 bodies) |
| `celestial_sphere.stars` | bool | False | `star_background_var` |
| `celestial_sphere.star_names` | bool | False | `star_names_var` |
| `celestial_sphere.grid` | bool | False | `celestial_grid_var` |
| `celestial_sphere.grid_labels` | bool | False | `celestial_grid_labels_var` |
| `celestial_sphere.constellation_names` | bool | False | `constellation_names_var` |
| `axes.scale_mode` | str | `"auto"` | `scale_var` (`'Auto'`/manual) |
| `axes.manual_half_range_au` | float \| None | None | `custom_scale_entry` |
| `axes.dtick_au` | float \| None | None | `custom_dtick_entry` (blank/0 = auto) |
| `comet_tails` | bool | True | (implicit in static — see DD-3) |
| `animation` | dict \| None | None | present iff `content_type == "animation"` |
| `animation.step` | str | required | `step`/`label` params of `animate_objects` |
| `animation.num_frames` | int | required | `num_frames_entry` |
| `animation.camera_track` | str \| None | None | `track_camera_var` |
| `animation.animate_comet_tails` | bool | False | `animate_comet_tails_var` |

**Excluded from the spec (with rationale in the mapping table):**
`special_fetch_var` + the three fetch-interval entries (data acquisition, not
scene description); the mid-plot orbit-update dialog (`remember_var`,
`user_choice` — data-freshness policy); `days_to_plot_entry` (derived, and the
code itself recalculates it from the date range); all status/progress/save-
dialog widgetry (display stage).

**Verification anchor:** 52 active widget-variable reads in `plot_objects`,
43 in `animate_objects` at this SHA (counting method in §3.0 — reproducible
by script). Every one is accounted for in the mapping table as MAPPED,
DERIVED, or EXCLUDED.

---

## 1. Deliverable 1 — Shared Spec Skeleton

```python
# Plain dict (or dataclass with asdict round-trip). JSON-serializable.
{
    "spec_version": "1.0",          # vocabulary version, for forward migration
    "domain": "solar_system",       # "solar_system" | "stars" |
                                    # "orbital_params" | "earth_system"
    "content_type": "static",      # "static" | "animation"
    "preset_id": None,              # str | None. Tier-2 curated preset ID.
                                    # The assembler expands a preset into the
                                    # explicit domain payload before assembly.
    "title": None,                  # str | None. None => assembler generates
                                    # the house-format title from epoch/window
                                    # ("Paloma's Orrery for {date} UTC" /
                                    #  "... through {end} UTC").
    "solar_system": { ... },        # exactly one domain payload key, matching
                                    # the domain tag (see Deliverable 2)
}
```

Rationale and boundaries:

- **`spec_version`** is not in the master plan's minimum ("domain tag, content
  type, display options") but presets, shareable scenes, and CI all serialize
  specs to disk; a version field is the cheapest possible insurance against a
  Phase-3+ vocabulary change orphaning stored tier-2 presets. **[DD-1]**
- **Display options live in the domain payload, not the skeleton.** The master
  plan's skeleton sketch lists "display options" as shared, but the actual
  display inputs harvested by the orrery are AU-denominated (axis range,
  dtick) and solar-system-shaped (shells, celestial sphere). Stars will
  declare limits in light-years/magnitudes; Earth system in scenarios. A
  shared `display` block would be an empty abstraction today. The skeleton
  carries only what is genuinely cross-domain: title and the preset hook.
  **[DD-2]** — flagged for Tony; easy to reverse if Phase 3 surfaces real
  shared display fields.
- **`preset_id` is skeleton-level** because tier-2 presets exist in every
  domain's future (encounter flybys, notable-star scenes, Earth scenarios),
  and the master plan makes animation presets the launch-time animation
  channel (§1). Expansion semantics: see Open Question OQ-4.
- **Serializability: settled yes.** Every field is str/float/int/bool/None/
  list/dict. This answers L-089's open decision ("is the spec serializable
  from day one?") in the affirmative — presets, shareable scenes, and golden
  artifacts (L-080) all get it for free.

---

## 2. Deliverable 2 — Solar System Vocabulary

The complete domain payload. Field names are clean/descriptive per the task
constraint (they do not mirror tkinter variable names).

```python
"solar_system": {

    # ---- Object selection -------------------------------------------------
    "objects": ["Earth", "Moon", "Mars", "Parker Solar Probe"],
    #   list[str], required, non-empty. Values are the 'name' keys of
    #   OBJECT_DEFINITIONS in celestial_objects.py (the catalog's unique
    #   human-readable key; 'id'/'id_type' resolution is catalog data the
    #   assembler looks up, not spec content). Exoplanet-domain objects
    #   (object_type in exoplanet / exo_host_star / exo_binary_star /
    #   exo_barycenter) are legal values — their presence is what switches
    #   the assembler into the exoplanet rendering path, exactly as
    #   selection does today (see Mapping notes M-1).

    # ---- Center body ------------------------------------------------------
    "center": "Sun",
    #   str, default "Sun". Must be a catalog object satisfying the
    #   center-capable predicate (can_be_horizons_center @8762: numeric-ID
    #   objects and objects carrying center_id). The assembler resolves
    #   center -> (center_id, id_type) from the catalog, and resolves the
    #   osculating-elements center body (the barycenter special cases at
    #   plot_objects 4367-4386) internally. The center's system_id scopes
    #   which selected objects render (same-system filter, 5016/5484).

    # ---- Dates ------------------------------------------------------------
    "epoch": "2026-07-04T00:00",
    #   ISO datetime, required. The position-marker date (get_date_from_gui).
    #   Encounter presets override this to closest-approach time — in spec
    #   terms, preset expansion WRITES this field (replaces the
    #   _encounter_plot_date[0] one-shot global).
    "window": {
        "start": "2026-07-04T00:00",   # default: equals epoch
        "end":   "2027-07-04T00:00",   # required
    },
    #   The orbit/trajectory data window (get_interval_settings start/end).
    #   days_to_plot is NOT a spec field: the orchestrators recalculate it
    #   from the range ((end-start).total_seconds()/86400, line ~539 of
    #   get_interval_settings) precisely because the entry widget loses
    #   sub-day precision. The derived value is assembler-side. Validation
    #   (end > start; Horizons date floor/ceiling) moves to the assembler's
    #   spec validator; on the web the coverage index enforces the real
    #   bounds anyway.

    # ---- Sampling (display resolution) -------------------------------------
    "sampling": {
        "orbital_points":    50,    # float > 0
        "trajectory_points": 50,    # float > 0
        "satellite_points":  50,    # float > 0
        "satellite_days":    50,    # int > 0
    },
    #   From get_interval_settings. These are DISPLAY settings (points shown
    #   per orbit class), distinct from fetch intervals — the function's own
    #   docstring makes this split, and the vocabulary preserves it: display
    #   sampling is spec; fetch intervals are not (see EXCLUDED rows).

    # ---- Orbit display ----------------------------------------------------
    "orbits": {
        "apsidal_markers": False,
        #   bool. show_apsidal_markers_var. Feeds plot_idealized_orbits and
        #   gates the three capability blocks: CAD perigee + hyperbolic
        #   osculating (non-Sun center, 5865), perihelion osculating orbit
        #   (Sun center, 5879), and their animation twins (7069/7083).
        "closest_approach_markers": False,
        #   bool. show_closest_approach_var. Threads into plot_actual_orbits
        #   (5338/7042) and gates _add_spacecraft_encounter_markers
        #   (5894/7097).
    },
    #   NOTE deliberately absent: "show actual orbits" / "show idealized
    #   orbits" toggles. At this SHA both render unconditionally for
    #   selected objects (plot_actual_orbits always called with
    #   show_lines=True; plot_idealized_orbits always called). The
    #   vocabulary does not invent toggles the GUI does not have. If the
    #   web GUI wants them, that is a vocabulary addition, not a mapping.

    # ---- Shell display ----------------------------------------------------
    "shells": {
        "Sun":   ["photosphere", "corona"],
        "Earth": ["magnetosphere"],
    },
    #   dict[body -> list[shell_key]], default {}. Body names: the 13
    #   shell-bearing bodies = get_planet_shell_vars_map()'s 12 (Mercury,
    #   Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto,
    #   Eris, Planet 9) + Sun. Shell keys: the per-body key sets of
    #   SHELL_CONFIGS / CUSTOM_SHELLS (shell_configs.py) — the same keys
    #   that index sun_shell_vars / <planet>_shell_vars today. An empty or
    #   absent body entry = no shells for that body. This replaces the
    #   13 dicts of IntVars with one serializable structure; the assembler
    #   converts to whatever create_celestial_body_visualization /
    #   add_center_body_shells need (those engines currently take var
    #   dicts and call .get() — the thin adaptation lives in the
    #   assembler, or the engines grow a plain-dict entry point during
    #   Phase 2; either way the SPEC is clean).

    # ---- Celestial sphere (cross-domain feature, §4e) ----------------------
    "celestial_sphere": {
        "stars": False,               # star_background_var
        "star_names": False,          # star_names_var
        "grid": False,                # celestial_grid_var
        "grid_labels": False,         # celestial_grid_labels_var
        "constellation_names": False, # constellation_names_var
    },
    #   Five independent bools, exactly the five kwargs of
    #   add_celestial_sphere_traces (5673-5679 / 7943-7949). The trigger
    #   condition (any of stars/grid/constellation_names true) is assembler
    #   logic, not spec structure.

    # ---- Axis control -----------------------------------------------------
    "axes": {
        "scale_mode": "auto",           # "auto" | "manual"
        "manual_half_range_au": None,   # float > 0; required if manual
        "dtick_au": None,               # float > 0 | None (None = auto dtick)
    },
    #   scale_var ('Auto' vs manual) + custom_scale_entry + custom_dtick_entry.
    #   Auto mode: assembler computes range (calculate_axis_range_from_orbits
    #   for static; get_animation_axis_range logic for animation; exoplanet
    #   scenes via calculate_exoplanet_axis_range; center-shell extent can
    #   enlarge the Auto cube per the Session-C max() rule at 7925-7927 and
    #   the add_center_body_shells return at 5255-5258). Manual mode: range =
    #   [-manual_half_range_au, +manual_half_range_au]. dtick_au follows the
    #   19.3 semantics: None/absent -> auto_dtick; positive -> override.
    #   This is the standing 3D-axis-control convention expressed as spec.

    # ---- Comet tails ------------------------------------------------------
    "comet_tails": True,
    #   bool, default True. In the static pipeline today, tails render
    #   automatically for every selected comet (is_comet predicate at
    #   6042-6047: orbital/trajectory + smallbody/id + symbol diamond +
    #   show_tails) with NO gui toggle. The field makes that implicit
    #   behavior explicit and suppressible. [DD-3 — Tony to confirm]

    # ---- Animation parameters (animation only) ------------------------------
    "animation": None,
    #   None when content_type == "static". When "animation":
    #   {
    #       "step": "day",
    #       #   "minute"|"hour"|"day"|"week"|"month"|"year". Encodes the
    #       #   (step, label) parameter pair of animate_objects — the seven
    #       #   animate_one_* buttons. "month"/"year" are calendar steps
    #       #   (create_animation_dates handles month-end/leap logic), so
    #       #   the enum is names, not a timedelta. The birthday button is
    #       #   step "year" + a preset (it also sets the date fields), not
    #       #   a distinct step value.
    #       "num_frames": 28,          # int > 0 (num_frames_entry)
    #       "camera_track": None,      # None | catalog object name
    #       #   track_camera_var; the GUI's "None (free camera)" sentinel
    #       #   becomes a real None. Tracked mode sizes the window per the
    #       #   element-extent rule (7552-7575) — assembler behavior.
    #       "animate_comet_tails": False,
    #       #   animate_comet_tails_var; per-frame engine-owned tails
    #       #   (MAPS exclusion at 7397 is assembler logic).
    #   }
}
```

**Standing-convention conformance.** The vocabulary can express all four
required conventions: single-info-marker and AU-in-hover are properties of the
traces the computation engines emit (spec-independent — the assembler calls
the same engines); 3D axis dtick+range control is `axes`; the marker symbol
taxonomy is catalog data (`symbol` per object in OBJECT_DEFINITIONS) that the
spec references by object name. No convention requires a field the vocabulary
lacks.

---

## 3. Deliverable 3 — Mapping Table

### 3.0 Counting method (the verification anchor)

A tkinter read is an **empty-paren `.get()`** (`X.get()`); dict data access
always carries a key argument (`d.get('key', ...)`) and is not a GUI input.
Counting empty-paren `.get()` on active (non-comment) code:

- `plot_objects` (lines 4351–6112): **52 reads**
- `animate_objects` (lines 6113–8169): **43 reads**

Reproduce with (Python, on the file at `fdb66ca`):

```python
import re
lines = open('palomas_orrery.py').read().splitlines()
def count(lo, hi):
    n = 0
    for i in range(lo-1, hi-1):
        s = lines[i].lstrip()
        if s.startswith('#'): continue
        n += len(re.findall(r'\.get\(\)', s.split('#')[0]))
    return n
print(count(4351, 6113), count(6113, 8170))   # -> 52 43
```

(The task prompt's "~58 / ~45" counts include commented-out lines; the active
counts at this SHA are 52/43. Same widget population either way.)

The table below accounts for **all 95 reads** plus the indirect widget reads
that reach the orchestrators through in-file helpers (`get_date_from_gui`,
`get_end_date_from_gui`, `get_interval_settings`, `get_animation_axis_range`)
and the two non-widget GUI-session inputs. Row status: **MAPPED** (spec
field), **DERIVED** (assembler computes it; no field), **EXCLUDED** (GUI or
data-layer concern; rationale given).

### 3.1 Direct widget reads

| # | Widget / var | plot_objects reads (lines) | animate_objects reads (lines) | Status → Vocabulary field | Notes |
|---|---|---|---|---|---|
| 1 | `obj['var']` (per-object IntVar, injected by `build_objects_list`) | 13 — 4362, 4492, 4496, 4579, 4864, 5013, 5210, 5331, 5481, 5639, 5848, 5971, 6040 | 14 — 6121, 6238, 6241, 6319, 6428, 6494, 6552, 6883, 7039, 7169, 7240, 7295, 7375, 7757 | MAPPED → `objects` | One selection, read many times for different filters (prefetch, exo detection, orbit loops, tails, axis auto-range). One list field covers all 27 reads. See M-1. |
| 2 | `center_object_var` | 2 — 4363, 4559 | 2 — 6122, 6250 | MAPPED → `center` | Shared. |
| 3 | `special_fetch_var` | 2 — 4410, 4587 | 1 — 6162 | EXCLUDED | Data-acquisition mode (fetch-without-caching to TEMP_CACHE_FILE), not scene description. Assembler never fetches (master plan §1/§3); on desktop this stays a harvester/data-layer control outside the spec. See M-2. |
| 4 | `days_to_plot_entry` | 5 — 4532 (x2), 4737, 4919, 5704 | 2 — 6287 (x2) | DERIVED | The code itself treats the entry as advisory: `get_interval_settings` recomputes days_to_plot from the date range for sub-day precision (its [INFO] mismatch print at 4533/6288 exists because the widget is not trusted). 4737 (`days_ahead` for cache update) is data-layer; 5704 (title text) is derived from `window`; assembler computes `(end-start)` fractional days. |
| 5 | `remember_var` (dialog-local) | 2 — 4700, 4708 | — | EXCLUDED | Mid-plot cache-update dialog ("Remember my choice"). Data-freshness policy, interactive by nature; cannot exist inside a GUI-agnostic assembler. Web: cache is read-only. Desktop: stays in the harvester. See M-3. |
| 6 | `trajectory_interval_entry` | 1 — 4762 | — | EXCLUDED | Special-fetch-mode Horizons fetch interval (e.g. '1d', '6h'). Data acquisition; see #3 / M-2. |
| 7 | `satellite_interval_entry` | 1 — 4765 | — | EXCLUDED | Same. |
| 8 | `default_interval_entry` | 3 — 4771, 4774, 4780 | — | EXCLUDED | Same (orbital / lagrange_point / fallback branches). |
| 9 | `scale_var` | 2 — 5209, 5258 | 1 — 6827 (+ indirect, §3.2) | MAPPED → `axes.scale_mode` | 5258/6827 pass the mode into `add_center_body_shells` (shell auto-scale interplay); one field covers both. |
| 10 | `custom_scale_entry` | 1 — 5221 | 0 direct (indirect via `get_animation_axis_range`, §3.2) | MAPPED → `axes.manual_half_range_au` | |
| 11 | `custom_dtick_entry` | 1 — 5233 | 1 — 7934 | MAPPED → `axes.dtick_au` | Item-19.3 semantics preserved (blank/0 → None → auto). |
| 12 | `planet_shell_vars[p][k]` values | 1 — 5294 (`any(var.get()...)`) + whole dicts passed to engines at 5251-5253, 5282-5312 | 1 — 6850 (`any(v.get()...)`) + dicts passed at 6824-6826, 6350-6361 | MAPPED → `shells` | 12 bodies. The engines receive var dicts and read them downstream; in the assembler the spec's plain dict replaces them (adaptation at the assembler/engine boundary, Phase 2). |
| 13 | `sun_shell_vars` values | 1 — 5316 | 1 — 6843 | MAPPED → `shells["Sun"]` | 13th shell body. |
| 14 | `show_closest_approach_var` | 4 — 5338, 5453, 5894, 5903 | 4 — 7012, 7042, 7097, 7106 | MAPPED → `orbits.closest_approach_markers` | |
| 15 | `star_background_var` | 2 — 5671, 5675 | 2 — 7941, 7945 | MAPPED → `celestial_sphere.stars` | |
| 16 | `star_names_var` | 1 — 5676 | 1 — 7946 | MAPPED → `celestial_sphere.star_names` | |
| 17 | `celestial_grid_var` | 2 — 5671, 5677 | 2 — 7941, 7947 | MAPPED → `celestial_sphere.grid` | |
| 18 | `celestial_grid_labels_var` | 1 — 5678 | 1 — 7948 | MAPPED → `celestial_sphere.grid_labels` | |
| 19 | `constellation_names_var` | 2 — 5672, 5679 | 2 — 7942, 7949 | MAPPED → `celestial_sphere.constellation_names` | |
| 20 | `show_apsidal_markers_var` | 5 — 5858, 5865, 5874, 5879, 5886 | 5 — 7063, 7069, 7078, 7083, 7090 | MAPPED → `orbits.apsidal_markers` | Gates idealized-orbit markers + capabilities B/C/D in both pipelines. |
| 21 | `num_frames_entry` | — | 1 — 6265 | MAPPED → `animation.num_frames` | Animation-only. |
| 22 | `animate_comet_tails_var` | — | 1 — 7396 | MAPPED → `animation.animate_comet_tails` | Animation-only. |
| 23 | `track_camera_var` | — | 1 — 7552 | MAPPED → `animation.camera_track` | Animation-only; 'None (free camera)' sentinel → None. |

**Row-count proof.** plot_objects: 13+2+2+5+2+1+1+3+2+1+1+1+1+4+2+1+2+1+2+5
= **52**. animate_objects: 14+2+1+2+1+1+1+1+4+2+1+2+1+2+5+1+1+1 = **43**.
Every active empty-paren `.get()` in both functions appears in exactly one
row above.

### 3.2 Indirect widget reads (helpers called by the orchestrators)

These do not appear in the in-function grep but are GUI inputs the spec must
carry — omitting them would be the "partial read → confident wrong
vocabulary" failure the prompt warns about.

| Helper (call sites) | Widgets read inside | Status → Field |
|---|---|---|
| `get_date_from_gui` @556 (plot: 4390, 4546, 4784, 5701 + via settings; anim: 6143, 6307 + via settings) | `entry_year`, `entry_month`, `entry_day`, `entry_hour`, `entry_minute` | MAPPED → `epoch` (and `window.start` via settings) |
| `get_end_date_from_gui` @8730 (plot: 4785, 5702 + via settings; anim: via settings) | `end_entry_year/month/day/hour/minute` | MAPPED → `window.end` |
| `get_interval_settings` @482 (plot: 4519; anim: 6275) | `trajectory_points_entry`, `orbital_points_entry`, `satellite_days_entry`, `satellite_points_entry`, `days_to_plot_entry`, + both date helpers | MAPPED → `sampling.*`, `window.*`; `days_to_plot` DERIVED |
| `get_animation_axis_range` @850 (anim: 7907-7917 — receives the widgets as arguments) | `scale_var`, `custom_scale_entry`, `obj['var']` | MAPPED → `axes.scale_mode`, `axes.manual_half_range_au`, `objects` (same fields as direct reads) |

### 3.3 Non-widget GUI-session inputs

| Input | Where read | Status |
|---|---|---|
| `_encounter_plot_date[0]` (one-shot global set by mission/comet presets @9537, 9691, ...) | plot_objects 4550-4553 | MAPPED → `epoch`. Preset expansion writes `epoch` directly; the mutable-global relay disappears in the spec world. |
| `remember_update_choice` / `update_choice_remembered` globals | plot_objects 4723-4725 | EXCLUDED — session cache-update memory, companion to row 5 (M-3). |
| `step`, `label` function parameters of `animate_objects` (from the seven `animate_one_*` handlers @8466-8498) | function signature | MAPPED → `animation.step` (label is derived presentation text). |

### 3.4 GUI-only surfaces confirmed excluded (no spec effect)

`output_label`, `progress_bar`, `root.update_idletasks/after`,
`update_status_display`, `create_monitored_thread` (threading),
`show_figure_safely` (display/save stage), `_last_plotted_fig` /
`_last_plot_name` (social-export handoff — display stage), `STATIC_TODAY`
(filename timestamp), `add_hover_toggle_buttons` (in-figure Plotly buttons,
added unconditionally in both pipelines — assembler behavior, not spec; the
local `hover_data` variable at 4557 is hardcoded and threads into engine
calls unchanged). None of these reads a widget the table misses.

---

## 4. Deliverable 4 — Content-Type Distinction

| Field group | static | animation | Notes |
|---|---|---|---|
| `objects`, `center` | shared | shared | Identical harvesting in both (rows 1-2). |
| `epoch` | position-marker date | animation start date (`current_date` @6307, seeds `create_animation_dates`) | Same widget, same field, role differs by content type. |
| `window` | orbit-path data window | orbit-path context window (orbit lines under the animation; also drives `days_ahead` cache check) | Shared. |
| `sampling.*` | shared | shared | Both call `get_interval_settings`. |
| `orbits.*` | shared | shared | Same gates in both pipelines (rows 14, 20). |
| `shells` | shared | shared | Static renders at epoch positions; animation re-renders per frame for the center body and frame-1 for others — assembler behavior, same spec field. |
| `celestial_sphere.*` | shared | shared | Static backdrop in both (5671-5679 / 7941-7949). |
| `axes.*` | shared | shared | Same three inputs; Auto-range computation differs internally (static: positions-based; animation: orbit-envelope-based via `get_animation_axis_range`; both honor shell extent). Spec is identical. |
| `comet_tails` | applies (epoch-dated tails, automatic today) | applies (frame-1 static tails when `animate_comet_tails` false) | See DD-3. |
| `animation.step` | — | required | The `(step, label)` parameters. |
| `animation.num_frames` | — | required | `num_frames_entry`. |
| `animation.camera_track` | — | optional | `track_camera_var`. Static has no camera input today (constant `get_default_camera()`), see OQ-2. |
| `animation.animate_comet_tails` | — | optional | Per-frame engine-owned tails. |
| Special-fetch mode + intervals | desktop-only (static pipeline only) | absent even on desktop | EXCLUDED from spec entirely; note the asymmetry — animation has no special-fetch branch at this SHA. |
| Orbit-update dialog | desktop static only (interactive) | desktop animation auto-updates without asking (6328-6341) | Both EXCLUDED; the pipelines already disagree here, which is itself evidence this is data-layer policy, not scene content. |

**The consolidation claim holds:** `content_type: "animation"` + a non-None
`animation` block is the entire delta. Everything else is one shared
vocabulary — which is precisely what lets one assembler replace two
orchestrators.

Validation rule: `content_type == "animation"` iff `animation` is a dict;
`content_type == "static"` iff `animation` is None. (Redundant encoding kept
deliberately: the top-level tag lets routers/CI branch without opening the
domain payload.)

---

## 5. Deliverable 5 — Coverage Index Interface (sketch)

The contract between cache and assembler; solar-system-specific per §1. The
assembler NEVER opens cache files — every data need goes through this
interface. The same interface backs the GUI's envelope declaration.

```python
class CoverageIndex(Protocol):
    """Read-only view over the three-tier cache. All methods are pure reads;
    no method fetches, writes, or touches the network."""

    # ---- Envelope declaration (GUI-facing) ---------------------------------
    def list_objects(self) -> list[str]:
        """Catalog names with any coverage at all."""

    def list_centers(self, object_name: str) -> list[str]:
        """Centers for which this object has coverage."""

    def get_coverage(self, object_name: str, center: str
                     ) -> list[CoverageSpan]:
        """Every covered span for the pair.
        CoverageSpan = {start: datetime, end: datetime,
                        step: str,            # e.g. '1d', '6h' — the fetch
                                              # interval the data carries
                        tier: int}            # 1 scheduled | 2 curated | 3 user
        """

    def list_presets(self) -> list[PresetDescriptor]:
        """Tier-2 curated presets (encounters, perihelia, close approaches,
        satellite tours, planetary tours). PresetDescriptor = {preset_id,
        kind, display_name, spec_fragment} where spec_fragment is the
        domain-payload dict the preset expands to. Presets ARE stored spec
        fragments — L-046's 'a saved scene spec IS a preset' realized."""

    # ---- Assembler-facing -----------------------------------------------
    def has_coverage(self, object_name: str, center: str,
                     start: datetime, end: datetime) -> bool:
        """True iff [start, end] lies inside covered spans for the pair.
        The assembler calls this per (object, center) before assembly;
        in a correctly-enveloped GUI it never returns False, but the
        assembler still checks — the index is the authority, not the GUI."""

    def get_positions(self, object_name: str, center: str,
                      start: datetime, end: datetime
                      ) -> TrajectorySeries:
        """The covered position series for the window (dates + x/y/z [AU],
        same shape orbit_paths.json data takes after load). Raises
        CoverageError if not covered — loud, never silent-wrong."""

    def get_position_at(self, object_name: str, center: str,
                        epoch: datetime) -> Position | None:
        """Single-epoch position for the marker (interpolated within a
        covered span per existing practice, or nearest cached point —
        Phase 2 decides the interpolation rule)."""

    def get_osculating_elements(self, object_name: str, center: str,
                                epoch: datetime) -> Elements | None:
        """Cached osculating elements at epoch (replaces the live Horizons
        pre-fetch block at 4410-4490 / 6162-6236 — on the web these come
        from tier-2 cached element sets; None = not cached, and the
        idealized-orbit engine falls back to catalog planetary_params,
        mirroring today's fallback behavior)."""
```

Notes:

- **`step` lives in coverage, not in the spec.** The web user never chooses a
  fetch interval; the data has whatever resolution Tony cached. The spec's
  `sampling.*` (display points) subsamples what coverage provides. This is
  the display-vs-fetch split of `get_interval_settings`' docstring, made
  architectural.
- **Multi-file cache structure (§7 #3) stays open.** This interface is
  deliberately structure-agnostic — per-object, per-pair, or per-(pair+window)
  files all sit behind it. That is the point of index-from-day-one.
- **Other domains do not implement this.** Stars declare
  `{max_distance_ly: 101, max_apparent_magnitude: 9}`; orbital parameters are
  always available; Earth system lists scenarios. Per §1.

---

## 6. Design Decisions (flagged for Tony)

- **[DD-1]** Added `spec_version` to the skeleton (not in the master plan's
  minimum). Insurance for serialized presets/golden artifacts. One string;
  remove if you judge it premature.
- **[DD-2]** Display options placed in the domain payload, not the skeleton
  — the skeleton's "display options" slot would today hold nothing genuinely
  cross-domain (axes are AU-shaped; shells/celestial-sphere are
  solar-system-only). `title` is the one shared display field kept up top.
  Reversible when Phase 3 shows what stars actually share.
- **[DD-3]** `comet_tails: bool = True` makes the static pipeline's implicit
  always-on tails explicit. Rationale: a spec with invisible behavior can't
  be diffed, and the envelope principle says say-what-renders. Alternative:
  omit the field and keep tails unconditional for comets. Your call.
- **[DD-4]** `days_to_plot` demoted to derived. The code already distrusts
  the widget (recomputes from dates for sub-day precision); carrying both a
  window and a duration invites the mismatch the [INFO] print exists to
  catch.
- **[DD-5]** Special-fetch mode, fetch intervals, and the orbit-update dialog
  excluded as data-acquisition/data-freshness policy, not scene description.
  Consequence: the desktop harvester keeps these controls and applies them
  BEFORE spec assembly (they decide what data exists; the spec decides what
  scene to build from it). This is the same layering as the coverage index.
- **[DD-6]** `(step, label)` collapsed to one `animation.step` enum;
  `label` is derived display text. The birthday button is preset + year
  step, not a distinct step value.
- **[DD-7]** Exoplanet scenes get NO dedicated fields. Selection of
  exo-typed objects is the switch today (4492-4496, 6238-6241), and the
  center override for exoplanet systems is orchestration the assembler
  inherits. Phase 4 may add fields; nothing is pre-specified (per the task's
  scope rule: no `.get()` today → no field today).
- **[DD-8]** `objects` uses catalog `name` as the key (not Horizons `id`).
  Names are the catalog's unique key, the GUI's selection currency, and the
  orbit cache's key component (`f"{name}_{center}"`). ID resolution is
  catalog lookup inside the assembler.

## 7. Open Questions for Tony

- **[OQ-1] Sampling defaults location.** Should `sampling.*` be omittable
  (assembler supplies 50s) or always explicit in stored specs? Omittable is
  friendlier for hand-written specs; explicit makes golden artifacts fully
  self-describing. I lean omittable-with-defaults; confirm.
- **[OQ-2] Static camera.** Static plots use constant `get_default_camera()`
  — no GUI input, so per the scope rule I added no field. But Gallery Studio
  refines cameras downstream, and a shareable web scene arguably wants a
  saved viewpoint. Reserve an optional `camera` field now (forward design),
  or defer to Phase 6? I deferred; flag if you want it reserved.
- **[OQ-3] Hover mode initial state.** `add_hover_toggle_buttons` puts
  Full-Info/Names-Only buttons in every figure; the initial mode is
  hardcoded ("Full Object Info", 4557). Should the spec carry an initial
  hover mode, or is in-figure toggling sufficient? I left it out (no widget
  reads it).
- **[OQ-4] Preset expansion semantics.** When `preset_id` is set AND explicit
  fields are present, does the preset win, do explicit fields override the
  preset (preset-as-defaults), or is mixing an error? Preset-as-defaults is
  most useful (tweak an encounter's shells); strictest is error-on-mix.
  Needs a ruling before tier-2 export tooling exists.
- **[OQ-5] Same-system filter.** Objects outside the center's `system_id`
  are silently skipped today (5016/5484). Should the assembler's validator
  reject them loudly instead (envelope honesty), or preserve silent-skip
  (desktop parity)? I lean loud-reject on web, silent-skip flag for desktop
  parity mode — but that's a behavior question for Phase 2, noted here
  because the validator is spec-adjacent.
- **[OQ-6] `orbits.show_actual` / `show_ideal` toggles.** Deliberately not
  invented (unconditional today). If the web GUI's curation wants them,
  add in Phase 2 as a vocabulary addition with defaults True — cheap, but
  it should be a decision, not a drift.

## 8. Issues noted during the session (relay margin)

- **Base SHA delta, benign.** Task prompt base `7b25eb9`; session HEAD
  `fdb66ca` (Tony-stated, round-trip confirmed). `palomas_orrery.py` and
  `celestial_objects.py` are md5-identical across the two SHAs — the delta
  is plan/ledger commits. Analysis validity unaffected. The master plan §2's
  older `d6c8c42` reference (flagged in the prompt's margin note) remains a
  cosmetic update for the plan when convenient.
- **`.get()` census correction.** Active-code widget reads at this SHA:
  52 (plot) / 43 (animate), vs the prompt's ~58/~45 (which count
  commented-out lines). Same widget population; the mapping table proves
  against the 52/43 census with the method in §3.0.
- **`/mnt/project/` contains `uap_ethogram_v3.db` (0 bytes)** — unrelated to
  this project and empty. Likely a stray project-knowledge upload; worth
  removing from the Claude project to keep the snapshot clean.
- **Uploads enumerated:** 3 of 3 read (task prompt, master plan v6, Section W
  draft). No un-read files on disk.

---

*Design session, zero code. Built on main @ `fdb66ca6e959d2cceb90ecd0408f38783b5f1825`;
nothing pushed. Fetched-not-recalled throughout: every field traces to a line
number in the file at this SHA. — Claude Fable 5 with Tony Quintanilla,
July 4, 2026.*
