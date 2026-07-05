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

**Scope boundary:** This is the vocabulary + coverage-index slice of Phase 1.
The shared-layer seam gate-check (confirming no tkinter seams beyond the two
named in §2) and the scene-equivalence criteria (largely Mode 5 / Tony's
visual judgment) are handled separately — out of scope here.

The master plan (`MASTER_PLAN_WEB_PUBLICATION.md`, uploaded alongside this
prompt) has the full architectural context. §3 defines the assembler pattern.
§4a describes the solar system domain. §4e describes cross-domain integration
(celestial sphere, exoplanet orbits, Sgr A*) — features the solar system
assembler calls or hosts. §5 Phase 1 defines this task's scope.

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
system domain), §4e (cross-domain integration — celestial sphere, exoplanets,
Sgr A*), §5 Phase 1 (this task), and §5a (execution map). These are settled
decisions that constrain the vocabulary.

**Scope rule for special features:** Some features listed in §4e (exoplanet
overlays, Sgr A* Grand Tour) are Phase 4 hybrid items, not solar-system-native.
The clean resolution: if `plot_objects` or `animate_objects` reads a `.get()`
for a feature today, it is in scope and must be mapped. If they don't, it is
forward-design — note it in Open Questions but don't fully specify the
vocabulary fields. Let the actual `.get()` calls drive what's in vs. out.

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
  (Note: `calculate_planet9_position_on_orbit` and `calculate_axis_range`
  live in `palomas_orrery_helpers.py`, not the main file — the vocabulary
  references these as assembler-called computations but doesn't need their
  internals. Don't upload helpers; this note is sufficient.)
- **Content preset** — if using a curated tier-2 preset (encounter, comet
  perihelion, etc.), the preset ID; the assembler expands this into the
  specific object/date/center selections

(These groups are suggested, not mandatory. Let the actual `.get()` calls
drive the structure.)

### Deliverable 3: Mapping Table

A table tracing each vocabulary field back to its source `.get()` call(s) in
the orrery. **The row set must equal the full `.get()` set** — every `.get()`
in both functions appears as either a mapped field or an explicit
"EXCLUDED — [rationale]" row. This is how the table proves completeness;
excluded inputs that silently vanish leave a hole in the proof. Format:

| Vocabulary field | plot_objects `.get()` | animate_objects `.get()` | Notes |
|---|---|---|---|
| `objects.planets` | `planet_vars[name].get()` | `planet_vars[name].get()` | Shared |
| EXCLUDED | `some_gui_only_var.get()` | — | GUI layout only, no effect on figure |
| ... | ... | ... | ... |

This table is the verification artifact — it proves the vocabulary is complete
relative to what the GUI currently offers. The total row count should be
verifiable against a grep of `.get()` calls in both functions.

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

- **Fetched-not-recalled (house rule).** Every vocabulary field and every
  `.get()` mapping must come from the actual uploaded file, never from what
  a solar-system visualization "probably" exposes. You are reasoning over
  11,110 lines — the dominant failure mode is designing a plausible vocabulary
  from partial reading plus training recall rather than from the actual code.
  The mapping table (Deliverable 3) is the guard; treat it as the primary
  artifact, not a secondary summary.
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

Tony is the interpreter between us. **This is likely a single Fable session —
the access window closes July 7, and this sits on the critical path.** Be
complete and self-contained; anything genuinely unresolved goes to Open
Questions for Tony to carry to another instance. Do not leave silent gaps
expecting a follow-up Fable round.

Please organize your output with:

1. **A summary section at the top** — the vocabulary as a compact field list
   (field name, type, allowed values) that Tony can hold in his head. Not a
   narrative paragraph — a scannable table or structured outline.
2. **Clear section headers** matching the five deliverables above.
3. **The vocabulary itself as structured tables and concrete dict/dataclass
   shapes** — field names, Python types, allowed values, defaults. Reserve
   prose for rationale only.
4. **The mapping table** as a distinct, scannable artifact with every `.get()`
   accounted for (see Deliverable 3 completeness requirement).
5. **Design decisions called out explicitly** — where you made a judgment call
   (e.g., "I grouped X with Y because..."), flag it so Tony can confirm or
   redirect.
6. **Open questions for Tony** collected at the end — anything the orrery code
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
Claude Fable 5. Reviewed by Claude Opus 4.8 (9 points, all accepted).
Tony carries context and holds commit authority.*

*Margin note for Tony (not for Fable): §2 line 65 of the master plan says the
shared layer was "verified at HEAD (`d6c8c42`)" — the original verification
SHA, not the current HEAD (`7b25eb9`). The prompt is clean (uses `7b25eb9`
throughout), but if Fable reads §2 closely it may flag the mismatch as an Open
Question. The shared-layer boundary hasn't changed — only the LICENSE move and
Section W entries landed between those SHAs — but worth updating §2 in the
plan when convenient.*
