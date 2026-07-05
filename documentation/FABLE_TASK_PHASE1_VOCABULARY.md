# Fable 5 Task: Phase 1 — Scene-Spec Vocabulary Design

**Type:** DESIGN SESSION (zero code)
**From:** Claude Opus 4.6 via Tony (collegial relay)
**Date:** July 4, 2026
**Base:** main @ `7b25eb9`

---

## What this is

Tony Quintanilla is building a web publication of Paloma's Orrery, a Python/
Plotly solar system and climate visualization suite. The architecture calls for
**shared assemblers** — one per domain — that both the desktop tkinter GUI and
the new web GUI feed through. The assembler takes a **scene spec** (a plain
data document) and produces a Plotly figure. No tkinter, no network calls, no
knowledge of which GUI produced the spec.

Your task is to design the **scene-spec vocabulary** for the solar system
domain by reading the two orchestration functions in `palomas_orrery.py` —
`plot_objects` (static scenes) and `animate_objects` (animations) — and
distilling every parameter they consume into a GUI-agnostic vocabulary.

The master plan (`MASTER_PLAN_WEB_PUBLICATION.md`, uploaded alongside this
prompt) has the full architectural context. §3 defines the assembler pattern.
§4a describes the solar system domain. §5 Phase 1 defines this task's scope.

---

## What to upload alongside this prompt

Tony should provide Fable with:

1. **This prompt** (paste or upload)
2. **`palomas_orrery.py`** — the full 11,110-line file at HEAD (`7b25eb9`).
   This is the primary input. Focus on `plot_objects` and `animate_objects`.
3. **`MASTER_PLAN_WEB_PUBLICATION.md`** — v6 (the updated master plan)
4. **`celestial_objects.py`** — contains `OBJECT_DEFINITIONS`, the data
   dictionary of all plottable objects. The vocabulary references objects by
   the keys and structure defined here.

---

## What to read and how

### In `palomas_orrery.py`:

**`plot_objects`** — the static scene orchestrator. This function:
- Reads ~58 `.get()` calls on tkinter widget variables (StringVar, IntVar,
  BooleanVar) to harvest the user's GUI selections
- Calls computation modules (`idealized_orbits`, `planet_visualization`,
  `orbit_data_manager`, `visualization_utils`, `shell_configs`, etc.) to
  build Plotly traces
- Produces a `plotly.graph_objects.Figure`

**`animate_objects`** — the animation orchestrator. Same pattern, ~45 `.get()`
calls. Produces animation frames.

**Your job:** Map every `.get()` call in both functions. Each one is a GUI
input that the vocabulary must capture. Group them by semantic role (object
selection, center body, date range, display toggles, visual options, animation
parameters, special features). Note which inputs are shared between the two
functions and which are unique to one.

Also map the **output side**: what trace types does each function produce?
What computation modules does it call, and with what parameters? The
vocabulary must carry enough information for the assembler to reproduce
these calls.

### In `celestial_objects.py`:

Read `OBJECT_DEFINITIONS` to understand the object catalog structure. The
vocabulary's object-selection fields reference this catalog.

### In the master plan:

Read §1 (architectural constraints), §3 (assembler architecture), §4a (solar
system domain), §5 Phase 1 (this task), and §5a (execution map). These are
settled decisions that constrain the vocabulary.

---

## What to produce

### Deliverable 1: Shared Spec Skeleton

The fields every scene spec has regardless of domain. Per the master plan §5
Phase 1: "domain tag, content type, display options."

```python
# Example shape (illustrative, not prescriptive):
{
    "domain": "solar_system",      # or "stars", "orbital_params", "earth_system"
    "content_type": "static",      # or "animation"
    "display": { ... },            # common display options
    ...
}
```

### Deliverable 2: Solar System Vocabulary

The complete set of fields specific to the solar system domain. Every `.get()`
call in `plot_objects` and `animate_objects` should map to a field here (or be
explicitly excluded with rationale — e.g., "this is a GUI-only concern with no
effect on the assembled figure").

Organize by semantic group:
- **Object selection** — which objects to plot, which are active
- **Center body** — what the scene is centered on
- **Date range** — start, end, step; epoch for static
- **Orbit display** — orbit paths, apsidal markers, orbit segments
- **Shell display** — which shells, which configs
- **Label/annotation** — object labels, hover text options
- **Axis control** — range, dtick, visibility
- **Camera** — initial camera position/orientation
- **Animation parameters** — frame count, speed, trail length (animation only)
- **Special features** — encounters, close approaches, exoplanet overlays,
  celestial sphere, Planet 9 hypothetical
- **Content preset** — if using a curated tier-2 preset (encounter, comet
  perihelion, etc.), the preset ID; the assembler expands this into the
  specific object/date/center selections

(These groups are suggested, not mandatory. Let the actual `.get()` calls
drive the structure.)

### Deliverable 3: Mapping Table

A table tracing each vocabulary field back to its source `.get()` call(s) in
the orrery. Format:

| Vocabulary field | plot_objects `.get()` | animate_objects `.get()` | Notes |
|---|---|---|---|
| `objects.planets` | `planet_vars[name].get()` | `planet_vars[name].get()` | Shared |
| ... | ... | ... | ... |

This table is the verification artifact — it proves the vocabulary is complete
relative to what the GUI currently offers.

### Deliverable 4: Content-Type Distinction

How the vocabulary differs between `content_type: "static"` and
`content_type: "animation"`. Which fields are static-only, animation-only,
or shared? The master plan says "animation/static consolidation is inherent —
the assembler handles both via a content-type tag." Show how.

### Deliverable 5: Coverage Index Interface (sketch)

The master plan §1 says: "Assemblers read cache through the coverage-index
abstraction from day one." The coverage index tells the assembler (and the
GUI's envelope) what data is available: which object/center pairs, for what
date ranges, at what step sizes.

Sketch the interface the assembler calls to query coverage. This is the
contract between cache and assembler. Example shape:

```python
# Does data exist for this request?
index.has_coverage(object_id, center_id, start, end, step) -> bool

# What's available for this object?
index.get_coverage(object_id) -> list of (center_id, date_range, step)

# What objects are available?
index.list_objects() -> list of object_ids
```

The coverage index is a **solar system concept** — other domains declare
their bounds more simply (stars: distance + magnitude limits; orbital
parameters: always available; Earth system: list of scenarios).

---

## Constraints

- **No tkinter anywhere in the vocabulary.** The spec is a plain Python data
  structure (dict, dataclass, or similar). Both GUIs produce specs; neither
  GUI's implementation leaks into the spec.
- **No network calls in the assembler.** All data comes through the coverage
  index, which reads pre-cached files. The vocabulary must not assume live
  Horizons access.
- **The assembler is new code.** It is written against this vocabulary, using
  `plot_objects`/`animate_objects` as recipe reference. The vocabulary does not
  need to mirror the orrery's internal variable names — it should use clean,
  descriptive names that make sense to someone who has never seen the tkinter
  code.
- **Standing visual conventions apply.** These are requirements the vocabulary
  must be able to express:
  - Single info marker pattern (one hover-carrying marker per trace, not N)
  - AU in all distance hover text alongside km
  - 3D axis dtick + range control
  - Marker symbol taxonomy (cross for positions, diamond for perihelion, etc.)

---

## Output format

Tony is the interpreter between us. Please organize your output with:

1. **A summary section at the top** — the vocabulary at a glance, before the
   detailed analysis. Tony reads this first to orient.
2. **Clear section headers** matching the five deliverables above.
3. **The mapping table** as a distinct, scannable artifact.
4. **Design decisions called out explicitly** — where you made a judgment call
   (e.g., "I grouped X with Y because..."), flag it so Tony can confirm or
   redirect.
5. **Open questions for Tony** collected at the end — anything the orrery code
   left ambiguous or where multiple vocabulary designs seem equally valid.

---

## What NOT to do

- Do not write assembler code. This is a vocabulary design, not an
  implementation.
- Do not redesign the computation modules. `idealized_orbits.py`,
  `planet_visualization.py`, etc. are shared engines that stay as-is. The
  vocabulary feeds parameters to them through the assembler.
- Do not design vocabularies for other domains (stars, orbital parameters,
  Earth system). Those are just-in-time, per the master plan.
- Do not propose GUI layouts or frameworks. The Dash-vs-Pyodide decision is
  Phase 0's job, running in parallel.

---

*Prompt written July 4, 2026 by Claude Opus 4.6 for collegial relay to
Claude Fable 5. Tony carries context and holds commit authority.*
