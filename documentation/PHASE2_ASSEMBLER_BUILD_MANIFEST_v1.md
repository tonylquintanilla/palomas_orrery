# Phase 2 Build Manifest v1 -- Solar System Assembler (B-prime)

**Type:** BUILD CONTRACT (design manifest, zero code delivered here)
**Author:** Claude Fable 5, Mode 7 collegial relay, July 13, 2026
**Built on:** orrery HEAD `8bce8354b6c9ae37b1e941f536cfc6f0a0a435c8`, gallery
HEAD `e864fd426a6bcffc478fe5ed9452a4dfc9159766` -- both independently
re-pinned via `git ls-remote` this session, matching Tony's report exactly.
**Parent:** L-079 (shared assembler architecture). Companion: L-080 (harness),
L-098 (closed), MASTER_PLAN_INTERACTIVE_GALLERY.md v11 Phase 2,
PHASE2_ASSEMBLER_DESIGN_HANDOFF v0.2, PHASE1_SCENE_SPEC_VOCABULARY.md.
**Audience:** the implementer (Opus, per the master plan's model assignments),
with Tony as integrator. Decisions routed back to Tony are collected in
Section 9 -- nothing there is decided silently on his behalf.

---

## 0. Verification record

Every claim below was fetched at the pinned HEADs this session, not carried.

Confirmations of the handoff's load-bearing claims:

- **L-087 done.** `palomas_orrery_helpers.py` is 909 lines, zero tkinter
  references. [verified @8bce8354]
- **Barycenter convention exists catalog-wide.** `object_type: 'barycenter'`
  -> `symbol: 'square-open'` for Earth-Moon (`id='3'`), Patroclus-Menoetius,
  Pluto-Charon (`id='9'`). Not Pluto-special-cased, exactly as the handoff
  says. [verified @8bce8354]
- **Halley pinned to `90000030`** in `celestial_objects.py` with the record-
  number comment. [verified @8bce8354]
- **Gallery config has all 12 objects** including `halley | 90000030 |
  smallbody`, Pluto/Charon at `@9`, Voyager 1 `-31 | id | full-arc`.
  [verified @e864fd42]
- **Voyager 1 served positions** are real and healthy: `positions/
  voyager_1.json`, column-oriented `{t,x,y,z}`, km, JD epochs, 105 points,
  glide + densified windows visible in the data. [verified @e864fd42]
- **Comet blocks carry the Tp anchor.** Encke's served block has
  `comet: {Tp_jd, solution_Tp_jd, max_distance_au}`. Artifact 7's perihelion
  marker has its data. [verified @e864fd42]

New findings -- things the handoff could not see because they live at the
builder/serving layer, below its altitude. Each is numbered F1-F6 and wired
into the build items and prerequisites below.

- **F1 [gates artifact 2]: `feature_configs.json` is a blast-radius trap.**
  The builder writes it EMPTY (`{'features': {}}`) into staging on every run
  (`derive_served`, builder line ~750), and `data/solar-system/` is replaced
  wholesale by the atomic swap. Any hand-authored feature renderer params
  placed in the served file are silently destroyed by the next nightly.
  The three-context table says features render in JS from this file -- so
  before artifact 2 (Jupiter/Saturn shells) can exist, feature params need a
  source of truth OUTSIDE the swap blast radius, with the builder deriving
  the served file from it. Same lesson as L-114's config move, one file over.
  [verified @e864fd42]
- **F2 [gates artifact 7]: `event_link` is hardcoded `None` in the builder**
  (`derive_served`, line ~727), even though `objects_config.json` already
  carries an `event_link: null` field per object. Artifact 7 needs a small
  builder change: pass `obj.get('event_link')` through, plus the Layer-1
  offline-test updates that go with any builder change. [verified @e864fd42]
- **F3 [gates artifact 4]: Halley is configured but not yet served.** Config
  has 12 objects; the live `coverage_index.json` (generated 2026-07-11) has
  11 -- no build has run since Halley was added. The offline suite already
  asserts 12 and has Halley-specific checks, so Layer 1 is consistent with
  config; what is missing is the Layer-2 `--first-build` run on Tony's
  hardware. Prerequisite for any Halley render. [verified @e864fd42]
- **F4 [gates everything]: the slim plotly wheel is not deployed.** `data/`
  contains only `objects_config.json` and the solar-system directories -- no
  ~3.9 MB wheel. B-prime's no-PyPI-at-runtime stance depends on it. Dev
  sessions can bridge via micropip/CDN, but the ship gate requires the wheel
  in the serving home. [verified @e864fd42]
- **F5 [confirms a design simplification]: moons are served osculating-only.**
  Moon/Io/Titan have `positions: null`, `availability: analytic`,
  parent-relative frames in the served index. Consistent with the v0.4
  osculating-primary model: artifact 3 renders each moon's own conic in its
  parent frame -- no cached position files are involved for moons at all.
  The assembler's moon path is exactly the planet path with a different
  center. [verified @e864fd42]
- **F6 [housekeeping, non-blocking]: `data/solar-system.prev_old/` is
  committed to the repo.** The builder's `.prev` semantics are local
  one-generation rollback; a committed `prev_old` looks like a manual rename
  artifact predating the current sweep logic. Flag for deletion at Tony's
  convenience -- it costs repo weight and could confuse a future reader.
  [verified @e864fd42]

One architectural verification that shapes the whole build:

- **The desktop engines are not importable in Pyodide.**
  `palomas_orrery_helpers.py` imports `astroquery` at module level;
  `idealized_orbits.py` imports `osculating_cache_manager` (the live-fetch
  layer) at module level. [verified @8bce8354] This settles "reuse vs
  rewrite" by fact, not preference: the assembler is NEW code with
  recipe-reference provenance comments (`# Source: <module>.<function>`),
  the same pattern `gallery_cache_builder.py` already uses for its fetch
  specifics. The master plan's "the assembler is new code; the original
  desktop code is the recipe reference" is not just policy -- it is the only
  path that runs.

---

## 1. What is being built -- one paragraph

A pure-Python scene assembler for the solar system domain: it takes a
JSON-serializable scene spec (the Phase 1a vocabulary, subset per Section 3),
plus the served coverage index and any needed position files as already-parsed
dicts, and returns a Plotly figure as a JSON-ready dict. It has no network, no
tkinter, no file I/O of its own -- data acquisition happens in JavaScript
(fetch) and is handed in. Because it is pure functions over dicts, the same
module runs identically in CPython (where the L-080 harness lives) and in
Pyodide (where the gallery page calls it). The first consumer is a new
interactive gallery page with a minimal control surface: object selection,
center body, date picker.

---

## 2. Where the code lives

All new assembler code goes in the GALLERY repo (`tonyquintanilla.github.io`),
because Pyodide must fetch it from the serving origin and because its data
contract is the gallery's served cache. Proposed layout:

```
assembler/
  conic_engine.py            # B1 -- Kepler math, no plotly dependency
  coverage_adapter.py        # B2 -- served-schema reader, loud errors
  solar_system_assembler.py  # B3 -- spec -> figure JSON
tests/
  test_conic_engine.py       # B7 -- CPython, no browser
  test_assembler_golden.py   # B7 -- golden artifacts, CPython
  golden/                    # B7 -- spec + expected-check pairs
solar-system.html            # B4 -- the new interactive page (name: Tony's call)
js/solar-system/             # B4 -- harvest, bootstrap, feature renderers
```

Two boundary rules, both [QUALITY]:

- Nothing under `assembler/` imports anything the Pyodide runtime cannot
  supply. Allowed: stdlib, numpy, plotly (B3 only). `conic_engine.py` stays
  numpy-only so the harness can test it without plotly installed.
- Nothing under `assembler/` reads files or touches the network. Data
  arrives as parsed dicts. This is what makes the CPython/Pyodide dual-runtime
  property true by construction rather than by discipline.

The Phase 0 page (`interactive.html`) is NOT modified. It is the frozen
tier-A exhibit per the two-tier model; the new page is a separate B-prime
artifact. [verified @e864fd42: interactive.html has zero references to
data/solar-system -- it is still the self-contained mean-elements demo.]

---

## 3. The spec contract for Phase 2 -- subset, normalization, honesty

The vocabulary (PHASE1_SCENE_SPEC_VOCABULARY.md) is the schema; Phase 2
implements a subset and is HONEST about the rest. Three disposition classes,
enforced by the validator:

**IMPLEMENTED (assembler acts on these):**

| Field | Phase 2 behavior |
|---|---|
| `spec_version` | must be "1.0" |
| `domain` / `content_type` | must be "solar_system" / "static" |
| `preset_id` | must be None (see OQ-4 ruling below) |
| `title` | None -> house format "Paloma's Orrery for {date} UTC" |
| `objects` | catalog slugs from the coverage index (DD-8 honored: names/slugs, not Horizons IDs) |
| `center` | slug; must match each object's served frame (see OQ-5 ruling) |
| `epoch` | ISO datetime; drives position markers and the title |
| `window` | spacecraft trace clipping only in Phase 2 |
| `sampling.orbital_points` | conic polyline density; default 360 |
| `axes.scale_mode` / `manual_half_range_au` / `dtick_au` | implemented in layout -- this closes the assembler-side slice of L-040 (note in the ledger entry when it lands) |

**KNOWN-UNIMPLEMENTED (structured error if present and non-default):**
`shells` (spec-level; features come from the served index in Phase 2, see
Section 5), `celestial_sphere.*`, `animation`, `orbits.apsidal_markers`,
`orbits.closest_approach_markers`, `comet_tails=False`. The error is a
machine-readable dict (`{"error": "unsupported_in_phase2", "field": ...}`)
so the JS layer can show a friendly message. Envelope honesty: the assembler
never silently drops a requested behavior.

**UNKNOWN fields:** warn (structured), do not abort -- forward compatibility
for Phase 3+ vocabulary growth.

**Vocabulary open-question rulings this manifest makes** (confirm or veto,
Tony -- Section 9):

- **OQ-1 (sampling defaults): omittable-with-defaults, and the assembler
  returns its NORMALIZED spec alongside the figure.** Hand-written specs stay
  friendly; golden artifacts store the normalized form and are fully
  self-describing. Both halves of the question, no trade-off.
- **OQ-5 (same-system filter): loud-reject on the web.** A spec asking for
  Io centered on Saturn gets a structured error naming the mismatch, never a
  silent skip. The coverage index is the authority; desktop parity mode is a
  desktop concern.
- **OQ-4 (preset expansion): stays out of scope, per the handoff's Section 4.**
  Concretely: `preset_id` must be None in Phase 2. The master plan's Phase 2
  line "presets for encounters, comet perihelion, close approaches" is
  satisfied at the UI level -- a page preset is a stored spec JSON that
  PREFILLS the controls, which then harvest normally. No expansion semantics,
  no precedence question, nothing OQ-4 needs to rule on. When tier-2 preset
  tooling arrives (L-046/L-104 track), OQ-4 gets its ruling then.
- **OQ-2 (camera), OQ-3 (hover mode), OQ-6 (show_actual/ideal): deferred**,
  unchanged from the vocabulary's own leanings. No fields reserved.

---

## 4. The data contract -- adapter over the SERVED schema, not the sketch

The vocabulary's Deliverable 5 (`CoverageIndex` Protocol) was written before
Phase 1b existed; it imagines tiered coverage spans and cached element SETS.
The served reality (schema 1.0) is simpler and better: osculating-primary,
one conic per object, spacecraft position arcs, `as_of_today` markers.
[verified @e864fd42] The adapter (B2) honors the Protocol's SPIRIT -- the
assembler never opens cache files, every data need goes through the
interface, errors are loud -- while matching the schema that actually ships:

```python
class CoverageAdapter:
    """Read-only view over parsed served data. No I/O, no network."""
    def __init__(self, index: dict, positions: dict[str, dict] = None): ...
    def list_objects(self) -> list[str]                    # served slugs
    def get_object(self, slug) -> dict                     # full block, KeyError -> CoverageError
    def orbit_elements(self, slug) -> dict | None          # osculating block (AU)
    def positions(self, slug) -> dict | None               # {t,x,y,z} km (spacecraft)
    def as_of_today(self, slug) -> dict | None             # km, JD
    def comet_anchor(self, slug) -> dict | None            # {Tp_jd, solution_Tp_jd, ...}
    def frame_of(self, slug) -> tuple[str, str]            # (stored_center, canonical_frame)
```

Rules the adapter enforces, all loud (`CoverageError` with a structured
payload):

- Requested object not in the index.
- Center mismatch: object's `stored_center` does not match the scene's
  center slug (the OQ-5 loud-reject lives here).
- Spacecraft window outside the served arc (`window` clipped to data with a
  structured warning if partially covered; error if zero overlap).
- Units are read from the data, never assumed (`unit` field on positions,
  `_au`/`_deg` suffixes on elements) -- the schema's own "unit is data" rule.

**Epoch semantics [route to Tony if it surprises]:** the served conic has one
epoch; the assembler propagates M from `M0_deg` at `epoch_jd` to the spec's
epoch via the period derived from `a_au`. For the ~12-object catalog within
the freeze window this is the intended use of osculating-primary. The
`as_of_today` point is used as a cross-check in the harness (Section 7), not
as the rendered marker source -- the rendered marker must come from the same
engine that draws the orbit, or marker and orbit can disagree visibly.

---

## 5. Feature rendering (JS) and the F1 fix

Per the settled three-context table, the Python assembler handles ORBITS
ONLY; features (shells, belts) render in JavaScript in the interactive layer.
Phase 2 needs four object features (`van_allen_belts`, `atmosphere_shell`,
`magnetosphere`, `ring_system`) and can defer the three `scene_features`
(asteroid_belt, kuiper_belt, heliosphere) unless artifact 2's Mode 5 wants
context.

**The F1 fix (builder + config, before artifact 2):**

1. Feature parameters live in `objects_config.json` -- already outside the
   blast radius, already the per-object source of truth, already has the
   `features` slug lists. Extend each slug to a param object or add a
   sibling `feature_params` block (implementer's choice; keep it one file).
2. `derive_served` emits `feature_configs.json` FROM config instead of
   writing `{}`. One producer, derived consumer -- the drift class this
   project already knows how to kill.
3. Layer-1 offline-test updates ride along (the count-assertion lesson from
   the Halley add applies to any new served content).

Feature geometry recipes come from the orrery's shell modules
(`SHELL_CONFIGS` for spheres; `CUSTOM_SHELLS` path for magnetosphere/rings --
note the live-dispatch warning in orrery-coding-conventions before reading
any shell leaf as a recipe). Parameters worth serving per feature: radii in
planet-radii or km, color, opacity, and the info-marker hover string. The JS
renderers follow the house conventions translated to JS: geometry traces
`hoverinfo: 'skip'`, ONE cross info marker at the north pole `r * 1.05`
carrying the full hover text, same legendgroup as the geometry, all distance
hover text km + AU.

---

## 6. The seven golden artifacts -- build contract per artifact

Common acceptance gate for every artifact: (a) harness structural checks pass
in CPython; (b) the page renders it via Pyodide without console errors;
(c) Mode 5 -- Tony's eyes on the render, which beats all claims. Desktop
comparison plots are the Mode 5 reference where the desktop can produce the
same scene.

**A1 -- Earth alone.** Spec: `objects: ["earth"], center: "sun", epoch:
<today>`. Proves: adapter -> engine -> assembler -> figure path; conic
polyline from served elements; position marker at epoch; house title; auto
axes; marker symbol (filled circle); hover with km + AU. The floor case --
everything after this is variation.
Harness bootstrap happens HERE (Section 7): A1's confirmed render becomes
golden artifact #1, per the handoff's L-080 co-evolution sequence.

**A2 -- Jupiter, Saturn.** Adds: multiple objects in one scene; the JS
feature layer (magnetosphere, ring_system + Earth's two if Earth is in the
scene). Prerequisite: F1 fix deployed and a build run so `feature_configs
.json` is populated. Proves: Python-orbits/JS-features composition; single
info marker pattern in JS; legendgroup toggling.

**A3 -- Moon, Io, Titan.** Same engine path, `center` = parent slug,
positions in the parent-relative frame (F5: osculating-only, no position
files). Proves: the transform-retirement claim end-to-end -- a moon is a
planet with a different center string. Axes: manual range will matter here
(Moon orbit at ~0.0026 AU is invisible at AU scale) -- first real exercise
of `axes.manual_half_range_au` + `dtick_au`.

**A4 -- Halley, Encke.** Prerequisite: F3 (Halley `--first-build` on Tony's
hardware; Layer 1 already expects 12). Two evidence kinds by design: Halley
gets a Mode-5 desktop comparison (exists in `celestial_objects.py` at
`90000030`); Encke has no desktop reference -- its acceptance is the harness
checks plus Tp cross-check (perihelion distance from the conic `a(1-e)` vs
the served `Tp_jd` position). Proves: comet category, high-e conics, the
add-object path's output is renderable.

**A5 -- Voyager 1.** Spec: `objects: ["voyager_1"], center: "sun",
trace_policy full-arc, window` = served arc (or a sub-window to prove
clipping). Data is already proven at the serving layer (2026-07-11 live
gate); this artifact renders `positions/voyager_1.json` as a polyline:
glide + densified flyby windows, drawn in km -> AU. Conventions: open
diamond marker at arc end (or `as_of_today`), single info marker at a
representative uncluttered index on the arc, hover km + AU. No conic for
spacecraft (`orbit_type: null` served -- adapter must not ask).

**A6 -- Pluto, Charon.** Port the existing desktop pattern, nothing new:
wide heliocentric view (Pluto's trajectory is the barycenter's --
`trajectory_of` substitution honored when the field is non-null) and the
barycenter-mode detail view (`center: "pluto_barycenter"` -- NOTE: the
served `stored_center` is `pluto_barycenter` [verified @e864fd42]; the
center slug vocabulary must include it, and the barycenter renders as its
own `square-open` marker per the catalog-wide convention). Two scenes, two
specs, mode selection not new composition -- exactly as the handoff resolved
it.

**A7 -- Halley + event_link marker.** Prerequisite: F2 (builder pass-through
+ config value + Layer-1 updates + a build). Config gets `halley.event_link:
{url or exhibit slug, label}`; the assembler places ONE link marker
coincident with Halley's perihelion point (from the comet Tp anchor /
conic), hover carries the label, and the JS layer wires the click to the
static exhibit. Proves: the general comet -> static-exhibit breadcrumb
pattern, automatically, for every comet that ever gets an `event_link`
value. Does not touch OQ-4 or closeup-shape.

Perihelion marker note (A4/A7): the cleanest read of the conventions is a
small marker at true-anomaly zero for comets, on by default for the comet
category, using the desktop's apsidal marker style as the recipe
(`apsidal_markers.py`). Default-on-for-comets is a Mode 5 / Tony call --
routed back (Section 9).

---

## 7. L-080 harness -- co-evolving, and cheaper than planned

The dual-runtime property (Section 2) changes L-080's economics: the harness
runs in CPython with zero browser machinery. `pytest tests/` on Tony's
machine (or the sandbox) exercises the identical code Pyodide runs. Pyodide
itself needs only a thin integration smoke (the page loads, one assemble
round-trips), not per-artifact browser automation.

Structure, seeded at A1 per the handoff's sequence:

- `tests/golden/<artifact>/spec.json` -- the normalized spec (OQ-1 ruling
  makes these self-describing).
- `tests/golden/<artifact>/checks.json` -- structural expectations, NOT
  pixel output: object set and trace count; marker symbols per category
  (taxonomy table); every distance hover contains both "km" and "AU";
  geometry traces hoverinfo-skip with exactly one info marker per feature;
  position-at-epoch within tolerance of an independent check value.
- Check values come from two independent anchors: the served `as_of_today`
  point (same-day epochs) and, where the desktop can produce the scene, a
  desktop-exported position. Tolerance: proposed 0.1% of the orbit's scale
  (routed back -- Tony may want tighter).
- Scene equivalence remains structural-plus-Mode-5, per the ledger entry:
  trace ordering, naming, layout details may legitimately differ from the
  desktop. The harness gates structure; Tony's eyes gate truth.

Each confirmed artifact adds its golden pair before the next artifact
starts. The harness is additive; no production modules are edited by it.

---

## 8. Build order, sessions, and prerequisites

**Stage 0 -- prerequisites (can run before or alongside Stage 1):**
- P1: deploy the slim plotly wheel to the serving home (F4). Dev can bridge
  via CDN micropip; the SHIP gate for any artifact requires the wheel.
- P2: Halley `--first-build` on Tony's hardware (F3). Gates A4/A7 only.
- P3: F6 housekeeping (`prev_old` deletion) -- anytime, non-blocking.

**Stage 1 (one or two sessions):** B1 conic engine + B2 adapter + B3
assembler skeleton + A1 -> Mode 5 -> harness bootstrap (B7 seed). Then A3
(moons -- pure engine variation, exercises manual axes). A2 waits for F1.

**Stage 2 (one session):** F1 builder/config change + Layer 1 + a build ->
A2 (features/JS layer, B4 grows its renderers). A5 (Voyager -- independent
of features, can swap earlier if F1 stalls).

**Stage 3 (one session):** A6 (Pluto/Charon, two specs) + F2 builder change
+ A7 (event_link). Ship gate: wheel deployed (P1), attribution requirement
satisfied for the new public page (the L-086 gate applies to
`solar-system.html` exactly as it did to `interactive.html` -- inline
"Data: JPL/NASA" credit minimum).

Builder changes (F1, F2) follow the full Layer discipline from the
gallery-cache-builder skill: offline suite from a clean checkout (count
assertions included), `--dry-run`, then a real build. Assembler changes
follow the harness. The page follows Mode 5.

**Testing layers for this build (mirrors TESTING_PROTOCOL's shape):**
- Layer 0: `pytest tests/` in CPython -- engine units + golden artifacts.
- Layer 1: builder offline suite (only when F1/F2 touch the builder).
- Layer 2: Pyodide integration smoke on the page (one assemble round-trip,
  console clean).
- Layer 3: Mode 5 -- the authoritative close gate, per artifact.

---

## 9. Routed back to Tony (decisions this manifest does NOT make)

1. **Page identity:** new `solar-system.html` vs extending `interactive.html`.
   This manifest assumes a new page (keeps the frozen tier-A demo frozen);
   naming and navigation are yours.
2. **OQ-1 / OQ-5 rulings** (Section 3): confirm omittable-with-defaults +
   normalized-spec-returned, and loud-reject. Both are one-line reversals if
   you disagree.
3. **Perihelion marker default-on for comets** (A4/A7): Mode 5 call.
4. **F1 shape:** feature params inside `objects_config.json` vs a sibling
   source file. This manifest recommends inside (one file, already outside
   the blast radius); either satisfies the invariant.
5. **Harness position tolerance** (Section 7): 0.1% proposed.
6. **F6:** delete `data/solar-system.prev_old/` when convenient.
7. **Epoch propagation semantics** (Section 4): flagged in case propagating
   the served conic to arbitrary in-window epochs surprises you; it is the
   intended osculating-primary use, but say so if you want epoch clamped to
   the freeze window.

## 10. Explicitly out of scope (unchanged from the handoff)

Live Horizons anything; animation; per-shell spec toggles and camera
presets; celestial sphere; OQ-4 preset expansion and closeup-view shape
(L-046/L-104 track); Studio preset-authoring refactor; NEO/spacecraft
curated links; catalog growth beyond the 12 (the Section 5 add-object
procedure in the handoff governs, unchanged); L-040's Studio-side fields
(only the assembler-side axes slice lands here).

---

## Ref

PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.2.md; PHASE1_SCENE_SPEC_VOCABULARY.md
@8bce8354; MASTER_PLAN_INTERACTIVE_GALLERY.md v11; gallery-cache-builder,
horizons-orbital-mechanics, orrery-coding-conventions skills;
`data/objects_config.json`, `data/solar-system/coverage_index.json`,
`data/solar-system/positions/voyager_1.json`, `tools/gallery_cache_builder.py`,
`tools/test_gallery_cache_builder_offline.py`, `interactive.html`
[all verified @e864fd42]; `palomas_orrery_helpers.py`, `celestial_objects.py`,
`idealized_orbits.py`, `LEDGER_CONSOLIDATED.md` (L-080, L-040, L-102, L-104)
[all verified @8bce8354].

---
Manifest written July 13, 2026 by Anthropic's Claude Fable 5, Mode 7
collegial relay for Tony Quintanilla. Built on orrery @8bce8354 / gallery
@e864fd42; every code-level claim fetched at those SHAs this session.
