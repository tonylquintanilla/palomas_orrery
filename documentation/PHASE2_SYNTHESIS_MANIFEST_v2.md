# Phase 2 Solar System Assembler — Synthesis Build Manifest v2

**Type:** BUILD CONTRACT (v2: incorporates both second-pass reviews + the
features-rendering ruling)
**Sources:** Fable's and GPT's original manifests; Fable's and GPT's
second-pass reviews of synthesis v1; `MASTER_PLAN_INTERACTIVE_GALLERY.md`
§3a (three-model convergence, pre-dates this whole Phase 2 thread)
**Design source:** `PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.3.md`
**Pinned orrery base:** `c10a42499771c659e62e6af5c6db04cb3b6d1b3e`
**Pinned gallery base:** `e864fd426a6bcffc478fe5ed9452a4dfc9159766`
**Status:** Ready for Opus to implement. Orchestration and documentation
authority remains Tony + Claude Sonnet 5 throughout.

---

## 0. What changed from v1

One architectural reversal, corrected against v1's own merge error: v1
silently adopted GPT's `render_features.py` (Python generates feature
Plotly traces), which contradicts a real, three-party-reviewed convention
already documented at `MASTER_PLAN_INTERACTIVE_GALLERY.md` §3a — *"Feature
rendering: always JS in interactive layer (both A and B′). Python assembler
handles orbits only."* This isn't a preference call; it's a **three-context
constraint**: static gallery, Interactive A (Phase 0, no Python assembler
at all), and Interactive B′ (this build) all share one JS feature-rendering
layer. Only orbit computation legitimately differs per context. GPT's
proposal wasn't a considered rejection of this — GPT never saw the
three-context table. **Reversed in this version.**

Also incorporated: both second-pass reviews in full (Section 7), and one
correction to how mean elements were framed — they aren't new scope
invented this session, they're completing a decision already in the master
plan's v9 entry (*"Three trace types: actual positions, osculating at
epoch, mean elements"*) that Phase 1b's actual build never implemented.

---

## 1. Governing rule (unchanged)

> The assembler may compose only data already present in the served gallery
> cache. It must never query Horizons, mutate the cache, infer unsupported
> objects, or silently substitute a different frame.

---

## 2. Architecture

**`AssemblyContext`** (ratified from GPT, sharpened per GPT's own
second-pass note): one immutable object per assembly — resolved scene spec,
date, center, object records, cache snapshot id, frame groups, feature
*requests* (not feature traces — see §4), camera policy, axis policy,
warnings. **Explicit invariant, per GPT's second-pass request:** once
frozen, no downstream stage may reinterpret date policy, frame policy, or
object selection. This is the single biggest maintainability property in
the whole design — everything reads from one resolved truth.

**Module layout** (GPT's finer split, ratified — minus features, corrected
this version):

```
gallery/assembler/
  models.py             # SceneSpec, ResolvedObject, AssemblyContext, etc. No Plotly, no I/O.
  catalog.py             # Loads objects_config.json, indexes by slug.
  cache_reader.py         # Reads served cache only. No astroquery, no builder imports.
  resolver.py             # SceneSpec -> AssemblyContext. Frame rejection lives here.
  render_objects.py       # Object markers/labels.
  render_orbits.py        # Osculating conics (Kepler propagation) + mean-elements conics (§5).
  render_spacecraft.py    # Voyager full-arc rendering from served positions.
  render_events.py        # Perihelion + event_link markers.
  presentation.py         # Hover, legend, camera, axes, title, annotations.
  assemble.py             # assemble_scene(scene_spec, repository) -> AssemblyResult
  errors.py               # Stable exception classes.
```

**No `render_features.py`.** Feature *dispatch* (which features apply, with
what parameters) is resolved by `resolver.py` and carried in
`AssemblyContext`/the assembly report as data. Actual feature Plotly traces
are drawn by the shared JS layer, per §3a, not generated in Python.

Boundary rules, unchanged: nothing under `assembler/` imports anything
Pyodide can't supply; nothing touches files or network. Confirmed
independently that this is load-bearing, not optional — `[verified
@8bce8354]`: `palomas_orrery_helpers.py` imports `astroquery` at module
level, `idealized_orbits.py` imports the live-fetch cache manager at module
level. Neither is importable in Pyodide. **Per GPT's second-pass note: this
separation should not get weakened during implementation for convenience.**

`interactive.html` (Phase 0, tier-A) is untouched — zero references to
`data/solar-system`, confirmed `[verified @e864fd42]`.

---

## 3. Scene spec, date resolution, frames

**Scene spec** (Fable's vocabulary-consistent naming + GPT's `view_id`):

```json
{
  "spec_version": "1.0", "domain": "solar_system", "content_type": "static",
  "objects": ["earth"], "center": "sun",
  "epoch": "2026-07-13T00:00:00Z",
  "view_id": null, "preset_id": null
}
```

`preset_id` stays `None` in Phase 2 (OQ-4 is a different system entirely —
handoff §8). `view_id` closed enum: `standard`, `pluto_wide`,
`pluto_barycenter_detail`.

**Vocabulary field dispositions, restored from Fable's second-pass note
(compressed too far in v1):**

| Field | Phase 2 disposition |
|---|---|
| `sampling.orbital_points` | Implemented; default 360; conic polyline density |
| `axes.scale_mode` / `manual_half_range_au` / `dtick_au` | Implemented; closes the assembler-side slice of L-040 |
| `window` | Spacecraft trace clipping only |
| `shells` (spec-level), `celestial_sphere.*`, `animation`, apsidal/closest-approach spec fields, `comet_tails=False` | Known-unimplemented; structured `unsupported_in_phase2` error, never silent drop |
| Anything else unrecognized | Warn (structured), don't abort — forward compatibility |

**Date resolution — Kepler propagation, bounded by real served data, not a
vague "freeze window" (corrected per Fable's second-pass finding):**

Served schema: one osculating snapshot per object (`epoch_jd`, `M0_deg`,
`a_au`, `e`, `i_deg`, `node_deg`, `peri_deg`) plus one `as_of_today`
cross-check point (**named explicitly here per Fable's second-pass note** —
used to validate the propagation engine against a known-good point, never
as the rendered marker source itself, or marker and orbit can visibly
disagree). No dated position range exists for anything except Voyager.

**Resolution:** propagate mean anomaly from `M0_deg` at `epoch_jd` to the
spec's `epoch` via Kepler's equation. **The bound is real served data, not
a phrase:** `coverage_index.json` already has a top-level `served_window`
field — confirmed present in the schema, currently `null` at HEAD. **Small
builder change required:** populate `served_window` with the actual
backfill/freeze range at build time; the assembler reads its bound from
that field and rejects out-of-range requests with a structured error. GPT's
original "nearest-date selection" is retired — confirmed by both
second-pass reviews as correctly superseded, not merely modified.

**Frames** — unchanged, both manifests agreed: reject unsupported mixed
frames with a structured error before building any trace; never revive
general vector transforms. Example (GPT's, kept):

```
Object 'moon' is stored relative to 'earth', but this scene resolves
center 'sun'. Phase 2 does not transform parent-relative data into
heliocentric coordinates. Build a separate Earth-centered Moon scene or
choose a supported view policy.
```

---

## 4. Prerequisite gates

**F1 — gates artifact 2.** `feature_configs.json` written empty
(`{"features": {}}`) every build; atomic swap replaces the served directory
wholesale — a silent data-loss trap. Fix: feature params move into
`objects_config.json` (outside the blast radius); `derive_served` derives
`feature_configs.json` from config instead of writing it empty; Layer-1
updates ride along.

**F2 — gates artifact 7, two-step, corrected.** Builder hardcodes
`event_link: None`. `objects_config.json` carries this field on none of the
12 objects — confirmed directly. Fix: (1) add `event_link` to the schema
(Halley first), (2) wire the builder to pass it through, (3) Layer-1
updates. **Process note, per Fable's own self-correction:** the original
false claim came from testing with `.get('event_link')`, which returns
`None` identically whether the key is missing or present-and-null — a
weaker check than the assertion it was used to support. Worth a ledger
field note: verifying a field's *value* requires first confirming the
field's *presence*; a default-returning accessor can't distinguish the two.

**F3 — gates artifact 4.** Config has 12 objects; live served index has 11,
no `halley` key (index predates the config addition). Needs a
`--first-build` on Tony's hardware. Layer 1 already expects 12.

**F4 — gates shipping anything.** Slim plotly wheel not deployed anywhere
in the gallery repo tree — confirmed via full tree listing. Current dev
bridge is `micropip.install` (live CDN) in `measure_plotly.html`, not
production architecture.

**L-086 (attribution) — ship gate, restored from Fable's original manifest,
dropped in v1 by oversight.** `solar-system.html` (or whatever the new page
is named) needs the same inline "Data: JPL/NASA" credit `interactive.html`
already carries, per the ruled-sufficient L-086 gate. Confirmed real in the
ledger (`PROPOSED`, `rice:2/2/70/1`). Ships alongside F4, not separately.

**F6 — non-blocking.** `data/solar-system.prev_old/` committed to the repo,
looks like a manual-rename artifact. Delete at convenience.

---

## 5. Mean elements — completing v9-scoped work, not new invention

**Correction to how this was framed in v1:** the master plan's own v9
entry already lists *"three trace types: actual positions, osculating at
epoch, mean elements"* as a settled §3a decision, well before this Phase 2
conversation. Phase 1b's actual build (L-098) shipped osculating-primary
only; the mean-elements trace type was scoped but never implemented. This
build completes it, on the same terms already agreed back then.

**Mechanism** (verified in `orbital_elements.py`): unconditional name-keyed
lookup, `ORIGINAL_planetary_params.get(obj_name, {})` — if present, draw
mean orbit alongside osculating; if absent, osculating only. No accuracy
threshold, no computed decision. Port this exactly.

**Scope:** extend served schema with an optional `mean` block (same shape
as `osculating`), for planets and the curated comet list currently live in
`orbital_elements.py` — confirmed: Halley, Ikeya-Seki are real entries;
most other comet candidates are commented-out notes.

**Source discipline, per Fable's second-pass finding (previously
underspecified):** the builder reads mean elements from
`objects_config.json`, same as everything else — **never** a live import
from the orrery's `orbital_elements.py` into the gallery builder. Same
standalone-repo boundary the whole gallery pipeline already respects
(L-107).

**Scoping honesty for artifact 4:** Halley's current epoch (mid-orbit
between 1986 and 2061) won't show the dramatic osculating/mean divergence
this feature exists for. A genuine sungrazer near perihelion would — not
in scope here. Build the mechanism; don't oversell what artifact 4 visibly
demonstrates.

**Satellites/moons excluded — sharper reasoning per Fable's second-pass
physics argument.** Moon/Io/Titan/Charon and the major giant-planet moons
have entries, but inconsistently dated (Moon 2013, Mimas/Iapetus 2022,
Charon 2024, Io/Titan undated) and sourced from an external cited table,
not Horizons' API. **Sharper reason to exclude, not just "old data":**
these entries carry no secular-rate term. A planet's mean elements stay
valid for a long time because planetary perturbations are small and slow.
A moon's orbital elements — the ascending node especially — precess on a
timescale short enough to matter: the Moon's own nodal cycle is ~18.6
years. Without a rate term, a satellite "mean" snapshot is **intrinsically
perishable** in a way a planet's isn't, regardless of how recently it was
dated. Moons stay osculating-only. (Separately, non-blocking: flagged as an
orrery-side cleanup candidate in the handoff, independent of this build.)

---

## 6. The seven golden artifacts

Common acceptance gate, unchanged: L-080 structural checks pass in
CPython; the page renders via Pyodide with no console errors; Mode 5 —
Tony's eyes, which beats all claims; desktop comparison where available.

1. **Earth alone.** Floor case. Osculating conic via Kepler propagation;
   position marker; Earth's shells *dispatched as data* (actual JS
   rendering depends on F1); house title; auto axes; hover km+AU. First
   L-080 fingerprint created here.
2. **Jupiter, Saturn.** Gated on F1. Multi-object heliocentric composition;
   feature *parameters* resolved and reported by Python, actual shell/ring
   traces drawn by the shared JS layer per §3a; one logical feature per
   body regardless of trace count; no legend duplication.
3. **Moon, Io, Titan.** Three separate scenes, each parent-relative;
   combining them into one common view produces the structural
   frame-rejection error, not silently wrong output.
4. **Halley, Encke.** Gated on F3. Two evidence kinds: Halley by Mode-5
   desktop comparison; Encke by the add-object/pinning path. Mean-elements
   mechanism (§5) exercised for Halley, with the scoping caveat noted.
5. **Voyager 1.** Full served arc, chronological, no re-thinning, no
   invented future segment. Flyby close-up composition is explicitly a
   later enhancement (the `center_closeup` fields in
   `spacecraft_encounters.py` are a commented-out template, confirmed).
6. **Pluto, Charon.** Two named views (`pluto_wide`,
   `pluto_barycenter_detail`), ported from the orrery's existing working
   modes. Barycenter marker uses the general
   `object_type: barycenter -> symbol: square-open` convention.
7. **Halley + `event_link`.** Gated on F2 (two-step). One link marker
   coincident with Halley's existing perihelion marker. Automatic for any
   comet with an `event_link` value (riding the perihelion marker every
   comet already gets); never automatic for NEOs/spacecraft (curated only,
   L-104 track, out of scope here).

---

## 7. Hover, invariants, layer order — restored detail from second-pass reviews

**Hover contract**, GPT's specific lines restored (dropped in v1's
compression): comet hover must identify that the displayed curve is
Tp-anchored analytic geometry, not a directly-observed track; Voyager hover
must distinguish the current-position marker from the served historical
arc — they answer different questions and shouldn't blur together.

**Layer order** (GPT's, unchanged): reference/axes helpers -> orbit/conic
traces -> spacecraft arcs -> shells/rings (JS-rendered, per §4 correction)
-> event markers -> object markers -> center marker -> labels. Center and
selected-object markers stay interactable above shells.

**Failure invariants**, unchanged from both manifests: unsupported scene
fails before partial rendering; missing cache payload fails with an
object-specific diagnostic naming the object; a missing optional feature
warns without blocking the base astronomical render.

---

## 8. L-080 harness

Semantic fingerprints, not full Plotly JSON — both manifests agreed, both
second-pass reviews reconfirmed. **Per GPT's second-pass request:**
fingerprints are generated from the frozen `AssemblyContext` *and* the
rendered output — both logical and visual regressions become detectable,
not just one or the other. Fingerprint fields: `artifact_id`,
`scene_spec_hash`, `cache_snapshot_id`, `resolved_date/center/frame`,
`object_slugs`, `trace_roles`/counts, `feature_keys` (the dispatch
decision, not the JS-rendered trace itself), `legend_groups`,
`coordinate_bounds`, numeric position samples against tolerance, warnings.
Co-evolves starting at artifact 1, per handoff §7 — not front-loaded. A
fingerprint update needs an explicit reason in the commit message.

---

## 9. Remaining decisions for Tony

1. **Harness position tolerance** — 0.1% proposed starting point; tune
   against real data.
2. **Perihelion marker default-on for comets** — genuinely a Mode 5 call,
   resolves itself on sight.
3. **Page identity** — new page assumed (keeps `interactive.html` frozen);
   naming is yours.
4. **F1's exact shape** — feature params inside `objects_config.json`
   (recommended, matches existing per-object source-of-truth pattern) vs.
   a sibling file. Low-stakes.

---

## 10. Explicitly out of scope (unchanged)

Live Horizons anything; animation; per-shell user toggles/camera presets;
celestial sphere; OQ-4 preset expansion and closeup-view shape (separate
system per handoff §8); Studio preset-authoring refactor (L-046);
NEO/spacecraft curated links and Apophis close-encounter composition
(L-104, downstream of L-046); catalog growth beyond the current 12; L-040's
Studio-side axis fields (assembler-side slice only lands here); Voyager
flyby close-up composition; mean-elements extension for satellites/moons
(§5, explicit exclusion, sharper reasoning this version).

---

## Ref

`PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.3.md`; `MASTER_PLAN_INTERACTIVE_GALLERY.md`
§3a; synthesis v1; Fable's and GPT's original manifests and second-pass
reviews; `data/objects_config.json`, `data/solar-system/coverage_index.json`,
`data/solar-system/feature_configs.json`, `tools/gallery_cache_builder.py`,
`tools/test_gallery_cache_builder_offline.py`, `interactive.html` [all
verified @e864fd42]; `palomas_orrery_helpers.py`, `celestial_objects.py`,
`idealized_orbits.py`, `orbital_elements.py`, `orbit_data_manager.py`,
`spacecraft_encounters.py`, `close_approach_data.py`, `LEDGER_CONSOLIDATED.md`
(L-086, L-040, L-046, L-104) [all verified @c10a424].

---
Synthesized July 2026 by Claude Sonnet 5, incorporating Claude Fable 5's and
GPT's original manifests and second-pass reviews, for Tony Quintanilla's
Mode 7 relay. Ready for Opus to implement.
