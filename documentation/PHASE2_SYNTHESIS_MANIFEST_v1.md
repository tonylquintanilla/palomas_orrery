# Phase 2 Solar System Assembler — Synthesis Build Manifest v1

**Type:** BUILD CONTRACT (synthesis of two independent manifests + new findings)
**Sources:** Claude Fable 5's manifest, GPT's independent manifest (competitive
Mode 7 pattern), both built from `PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.2.md`
**Design source:** `PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.3.md` (see its Sections
8-9 for the full convergence/divergence/resolution record this synthesizes)
**Pinned orrery base:** `8bce8354b6c9ae37b1e941f536cfc6f0a0a435c8`
**Pinned gallery base:** `e864fd426a6bcffc478fe5ed9452a4dfc9159766`
**Status:** Ready for a second-pass review by Fable and GPT, then implementation by Opus.
**Orchestration:** Tony Quintanilla + Claude Sonnet 5 remain the orchestrators
and documentation authority across this whole relay; this manifest is not a
final, unreviewable artifact — it goes back out for one more pass before build.

---

## 0. Purpose and governing rule

This is not a third independent manifest. It is a synthesis: every place
Fable and GPT converged is carried forward as-is; every place they diverged
has been resolved (see Section 1); four real implementation-blocking facts
Fable found and GPT's manifest didn't know about are folded in as hard gates
(Section 4); and one substantive design gap neither manifest addressed —
mean-vs-osculating elements — is resolved as new scope (Section 5).

Governing rule, unchanged from both source manifests:

> The assembler may compose only data already present in the served gallery
> cache. It must never query Horizons, mutate the cache, infer unsupported
> objects, or silently substitute a different frame.

The gallery repository is the implementation home. The desktop orrery is a
computation and visual-convention reference, never a runtime dependency.

All claims are tagged `[verified @<sha>]` or `[carried]`, consistent with
both source manifests' own discipline.

---

## 1. What converged, and what was resolved (full record: handoff v0.3 §8-9)

**Converged (both manifests agreed, nothing to resolve):** cache-only
architecture; no network/file I/O inside the assembler; the same 7 golden
artifacts in the same order; hard rejection of unsupported mixed-frame
scenes, never silent transformation; Pluto/Charon as two named views, not
one composed scene; L-080 as semantic fingerprints, not full Plotly JSON;
the full deferred-work list; decisions routed back to Tony rather than
decided silently.

**Resolved divergences, now settled for this build:**

| Question | Fable said | GPT said | Resolution |
|---|---|---|---|
| Central resolved-state object | (no equivalent) | `AssemblyContext`, immutable, frozen post-resolution | **Adopt GPT's `AssemblyContext`** |
| Pluto view naming | "two specs" (loose) | `view_id` closed enum | **Adopt GPT's `view_id`** |
| Scene-spec field names | Vocabulary-consistent (`epoch`, `preset_id`) | Redesigned (`date`, `event_links`) | **Fable's naming + GPT's `view_id` addition** |
| Module layout | 3 files | ~11 files, finer separation | **Adopt GPT's layout** |
| Date resolution | Propagate via Kepler's eq. from `M0_deg`/`epoch_jd` | "Nearest-date selection, never extrapolate" | **Fable's model — verified correct, see §3** |
| Verification depth | Read builder code + live served cache | Read `objects_config.json` only | **Fable's findings adopted as gates, §4** |

---

## 2. Architecture: `AssemblyContext` and module layout

**`AssemblyContext`** (GPT's proposal, ratified): a single immutable object
produced once per assembly, containing at minimum: resolved scene spec,
resolved date, resolved center slug/record, resolved object records,
cache snapshot id, frame groups, feature requests, camera policy, axis
policy, warnings. No renderer recomputes center resolution, date policy,
or frame interpretation independently — everything downstream reads from
the frozen context. This is also what gives L-080 one deterministic thing
to fingerprint per artifact.

**Module layout** (GPT's proposal, ratified):

```
gallery/assembler/
  models.py            # SceneSpec, ResolvedObject, AssemblyContext, etc. No Plotly, no I/O.
  catalog.py            # Loads objects_config.json, indexes by slug, read-only lookups.
  cache_reader.py        # Reads served cache only. No astroquery, no builder imports.
  resolver.py            # SceneSpec -> AssemblyContext. Frame rejection lives here.
  render_objects.py      # Object markers/labels.
  render_orbits.py       # Analytic orbit / comet-conic traces (osculating + mean, see §5).
  render_spacecraft.py   # Voyager full-arc rendering from served positions.
  render_features.py     # Shell/belt dispatch (see §4, F1).
  render_events.py       # Perihelion + event_link markers (see §4, F2).
  presentation.py        # Hover, legend, camera, axes, title, annotations.
  assemble.py            # assemble_scene(scene_spec, repository) -> AssemblyResult
  errors.py               # Stable exception classes.
tests/assembler/          # Unit, contract, integration, golden-artifact tests.
```

Two boundary rules [QUALITY], both from GPT's manifest, unchanged:
nothing under `assembler/` imports anything Pyodide can't supply (stdlib,
numpy, plotly in `render_orbits`/`assemble` only); nothing under
`assembler/` touches files or network — data arrives as parsed dicts. This
is what makes the CPython/Pyodide dual-runtime property true by
construction, per Fable's verified finding that the desktop modules
(`palomas_orrery_helpers.py` imports `astroquery` at module level,
`idealized_orbits.py` imports the live-fetch cache manager at module level)
are not importable in Pyodide — confirmed independently at
`[verified @8bce8354]`.

The Phase 0 page (`interactive.html`) is not modified — confirmed zero
references to `data/solar-system` `[verified @e864fd42]`. It stays the
frozen tier-A exhibit; the new page is a separate artifact (naming is
Tony's call, per Section 8).

---

## 3. Scene spec, date resolution, and frame handling

**Scene spec** — Fable's vocabulary-consistent field names, plus GPT's
`view_id`:

```json
{
  "spec_version": "1.0",
  "domain": "solar_system",
  "content_type": "static",
  "objects": ["earth"],
  "center": "sun",
  "epoch": "2026-07-13T00:00:00Z",
  "view_id": null,
  "preset_id": null
}
```

`preset_id` must be `None` in Phase 2 (OQ-4 stays out of scope — it belongs
to a different system entirely, per handoff §8). `view_id` is a closed
enum for Phase 2: `standard`, `pluto_wide`, `pluto_barycenter_detail`.
Unknown fields warn (structured), don't abort — forward compatibility for
later phases. Known-unimplemented vocabulary fields (`shells` at spec
level, `celestial_sphere.*`, `animation`, apsidal/closest-approach markers
as spec fields, `comet_tails=False`) produce a structured
`unsupported_in_phase2` error, never a silent drop.

**Date resolution — corrected from both source manifests, resolved by
checking the actual served schema (handoff v0.3 §9):**

The served schema gives one osculating-elements snapshot per object
(`epoch_jd`, `M0_deg`, `a_au`, `e`, `i_deg`, `node_deg`, `peri_deg`) plus
one `as_of_today` cross-check point — never a range of dated positions,
except for Voyager (which uses a genuinely different path, §3 continued
below). **Resolution: propagate mean anomaly from `M0_deg` at `epoch_jd` to
the spec's `epoch` via Kepler's equation, bounded to the object's served
validity/freeze window; reject if the requested epoch is genuinely out of
range.** This is not "extrapolate at will" — it's bounded, and it's the
only resolution that actually uses what the schema provides. GPT's
"nearest-date selection" is explicitly retired: there is nothing to select
from except the one snapshot, for anything except Voyager.

**Voyager is the one object that doesn't use this path at all** — full
served position arc, chronological, no propagation, no re-thinning
(already Douglas-Peucker-thinned at the data layer, proven live 2026-07-11
`[carried]`).

**Frame handling** — both manifests agreed and it stands: a scene may
contain multiple objects only if already in a common served frame (all
heliocentric; parent-relative siblings sharing a center; Pluto+Charon in
`pluto_barycenter`), or under an explicit `view_id`. Arbitrary
heliocentric + parent-relative mixtures are rejected with a structured,
human-readable error before any Plotly trace is built — general vector
transforms are never revived as a normal path. Example failure text (GPT's,
kept verbatim, it's good):

```
Object 'moon' is stored relative to 'earth', but this scene resolves
center 'sun'. Phase 2 does not transform parent-relative data into
heliocentric coordinates. Build a separate Earth-centered Moon scene or
choose a supported view policy.
```

---

## 4. Prerequisite gates — Fable's builder-layer findings, corrected where needed

These are new facts neither the handoff nor GPT's manifest knew about when
first written. All four independently re-verified this session, all at
`[verified @e864fd42]` unless noted.

- **F1 — gates artifact 2 (Jupiter/Saturn shells).** The builder writes
  `data/solar-system/feature_configs.json` empty
  (`{"schema_version": "1.0", "features": {}}`) on every run, and the
  atomic swap replaces the served directory wholesale — confirmed by
  direct read of the live file. Any hand-authored feature params placed
  directly in the served output get silently destroyed by the next
  nightly build. **Fix required before artifact 2:** feature parameters
  move into `objects_config.json` (outside the swap blast radius, already
  the per-object source of truth — Fable's own recommendation, obviously
  right); `derive_served` derives `feature_configs.json` from config
  instead of writing it empty; Layer-1 offline-test updates ride along.
- **F2 — gates artifact 7 (Halley + event_link), corrected.** The builder
  hardcodes `event_link: None` in `derive_served` — confirmed at the exact
  line. **Correction to Fable's original claim:** `objects_config.json`
  does NOT carry an `event_link` field on any of the 12 objects — checked
  every entry, including Halley, directly. So this is a **two-step fix**,
  not Fable's one-line "pass the config value through": (1) add
  `event_link` to the schema (Halley's entry at minimum), (2) wire the
  builder to read and pass it through, (3) Layer-1 updates.
- **F3 — gates artifact 4 (Halley/Encke).** Config has 12 objects; the
  live served `coverage_index.json` (generated 2026-07-11, before Halley
  was added) has 11, no `halley` key — confirmed directly. Layer 1's
  offline suite already expects 12 and has Halley-specific checks. What's
  missing is the Layer-2 `--first-build` run on Tony's hardware. Gates
  artifact 4 only.
- **F4 — gates shipping anything.** The slim self-hosted plotly wheel is
  not deployed anywhere in the gallery repo — confirmed via a full repo
  tree listing, not just a guessed path. `measure_plotly.html` currently
  bridges via `micropip.install` (live CDN) — a real dev fallback, not the
  production architecture. This is the ship gate for every artifact, not
  just the ones that use shells or events.
- **F6 — non-blocking housekeeping.** `data/solar-system.prev_old/` is
  committed to the repo — confirmed present in the tree. Looks like a
  manual-rename artifact predating the current `.prev` sweep logic.
  Delete at Tony's convenience; costs repo weight, not correctness.

(F5 — moons served osculating-only, `positions: null` — confirmed, and is
fully explained by the date-resolution model in Section 3; not a gate, a
design confirmation.)

---

## 5. Mean elements — new scope, resolved this session (handoff v0.3 §9)

Neither source manifest addressed this; it surfaced during the
Kepler-propagation design conversation and is real, scoped work.

**What:** near perihelion, a highly eccentric comet's osculating orbit can
look dramatically different from its long-term mean orbit — visually
near-hyperbolic, tangent to the mean ellipse at that point. The comparison
is only meaningful with both shown together. The orrery already has a
working mechanism for this: an unconditional name-keyed lookup
(`ORIGINAL_planetary_params.get(obj_name, {})`) — if present, draw the mean
orbit alongside the osculating one; if absent, osculating only. No accuracy
threshold, no computed decision — a curated list, checked and reused, not
invented.

**Scope for this build:** extend the served schema with an optional `mean`
elements block (same shape as `osculating`: `a_au`, `e`, `i_deg`, `node_deg`,
`peri_deg`, `M0_deg`/`epoch`, source), populated for planets and the
curated comet list currently live in `orbital_elements.py` (confirmed:
Halley, Ikeya-Seki are real entries; most other comet candidates are
commented-out notes, not live data). `render_orbits.py` gets the same
lookup-and-draw logic the orrery already uses — port it, don't redesign it.

**Scoping honesty for artifact 4:** Halley's current epoch (mid-orbit
between its 1986 and 2061 returns) won't show the dramatic divergence this
feature exists for. A genuine near-perihelion sungrazer (Ikeya-Seki is the
orrery's own example) would demonstrate it properly, but isn't in the
7-artifact scope. Build the mechanism now; don't claim artifact 4 fully
demonstrates it visually.

**Explicitly excluded: satellites/moons.** Moon, Io, Titan, Charon, and the
major Jovian/Saturnian/Uranian moons all have entries in
`orbital_elements.py`, but they're inconsistently sourced and dated (Moon:
2013; Mimas/Iapetus: 2022; Charon: 2024 post-New Horizons; Io/Titan:
undated) — confirmed directly. Root cause: Horizons doesn't serve
satellite mean elements via its API the way it does osculating elements;
these come from an external, separately-cited reference table, hand-
transcribed at different times for different systems — not a maintained
standard the way planetary J2000 values are. Reliable at best for
Jupiter's and Saturn's major, heavily-studied moons; inconsistent
elsewhere; several minor-moon entries are incomplete, commented-out
attempts. **Moons stay osculating-only in the served schema — no
mean-elements extension for them.** (Separately, non-blocking: the
satellite `orbital_elements.py` entries are a candidate for orrery-side
cleanup, independent of this build — noted in the handoff, not gating
anything here.)

---

## 6. The seven golden artifacts

Common acceptance gate, unchanged from both source manifests: (a) L-080
structural checks pass in CPython; (b) the page renders it via Pyodide
with no console errors; (c) Mode 5 — Tony's eyes on the render, which
beats all claims; desktop comparison where the desktop can produce the
same scene.

1. **Earth alone.** `objects: [earth], center: sun, view_id: standard`.
   Floor case: adapter -> resolver -> render -> figure path; osculating
   conic via Kepler propagation at the requested epoch; position marker;
   Earth's two shells (once F1 lands, otherwise deferred within this
   artifact); house title; auto axes; hover with km + AU. L-080's first
   fingerprint schema gets created here.
2. **Jupiter, Saturn.** Gated on F1. Multi-object heliocentric composition;
   Jupiter magnetosphere + rings, Saturn rings, data-driven from
   `objects_config.json`; one logical feature per body regardless of
   internal trace count; legend entries don't multiply per feature trace.
3. **Moon, Io, Titan.** Three separately assembled scenes (Moon@earth,
   Io@jupiter, Titan@saturn), not one mixed-frame scene. Each context
   resolves `parent-relative`; attempting to combine them into one common
   view produces the structural frame-rejection error, not three
   unrelated origin-centered traces.
4. **Halley, Encke.** Gated on F3 (Halley's `--first-build`). Two
   evidence kinds: Halley by Mode-5 desktop comparison; Encke by the
   add-object/pinning path (no desktop reference exists for it). Both
   conics Tp-anchored, identified as such in the assembly report. Mean-
   elements mechanism (§5) exercised for Halley, with the scoping caveat
   above about its epoch not showing dramatic divergence.
5. **Voyager 1.** Full served arc only — flyby close-up composition is
   explicitly a later enhancement, not part of this artifact (the
   `center_closeup` fields in `spacecraft_encounters.py`'s Voyager entry
   are a commented-out template, not live data — confirmed). Chronological
   ordering, endpoint at the final served sample, no future segment
   invented, `trace_policy: full-arc` in the report.
6. **Pluto, Charon.** Two named views (`pluto_wide`, `pluto_barycenter_detail`)
   ported directly from the orrery's existing, already-working modes — not
   new composition architecture. Barycenter marker uses the general
   `object_type: barycenter` -> `symbol: square-open` convention, not a
   Pluto-only conditional.
7. **Halley + `event_link`.** Gated on F2 (two-step fix). One link marker
   coincident with Halley's existing perihelion marker; hover names the
   linked static exhibit; selecting it is understood to leave the live
   scene. Establishes the general comet -> static-exhibit pattern for any
   comet that gets an `event_link` value in the future — automatic for
   comets (riding the perihelion marker every comet already gets), never
   automatic for NEOs/spacecraft (curated only, per the L-104 ledger note
   — out of scope for this build).

---

## 7. L-080 harness

Both manifests agreed: semantic fingerprints, not full Plotly JSON;
co-evolves starting at artifact 1, not front-loaded (per handoff §7's
already-resolved sequencing). Fingerprint contents (merging both
proposals): `artifact_id`, `scene_spec_hash`, `cache_snapshot_id`,
`resolved_date`, `resolved_center`, `resolved_frame`, `object_slugs`,
`trace_roles`/`trace_count_by_role`, `feature_keys`, `legend_groups`,
`coordinate_bounds`, numeric position samples against tolerance, warnings.
Layer structure (GPT's, adopted): unit tests (schema/catalog/date/frame/
feature-dispatch/route validation) -> structural figure tests (trace
roles, order, legend groups, origin, hover fields, no NaN/inf) -> semantic
golden fingerprints -> Mode 5 screenshot evidence (advisory, not blocking)
-> mainloop-suppression/import tests (no Tkinter, no network, no file
writes on import). A fingerprint update requires an explicit reason
recorded in the commit message — accidental baseline rewrites should be
hard to do by accident.

---

## 8. Remaining decisions for Tony (shorter than either source manifest's list — most got resolved above)

1. **Harness position tolerance.** Both manifests proposed defaults (GPT:
   unspecified numeric target; Fable: 0.1% of orbit scale). Reasonable
   starting point; tune once the harness runs against real data.
2. **Perihelion marker default-on for comets** (artifacts 4/7). Genuinely a
   Mode 5 call — resolves itself when you look at the render, not before.
3. **Page identity** — new page vs. extending `interactive.html`. This
   manifest assumes a new page (keeps the frozen tier-A demo frozen);
   naming is yours whenever it comes up.
4. **F1's exact shape** — feature params inside `objects_config.json`
   (this manifest's recommendation, matching Fable's) vs. a sibling file.
   Low-stakes either way.

---

## 9. Explicitly out of scope (unchanged from the handoff)

Live Horizons anything; animation; per-shell user toggles and camera
presets; celestial sphere; OQ-4 preset expansion and closeup-view shape
(a separate system, per handoff §8 — not this build's concern at all);
Studio preset-authoring refactor (L-046); NEO/spacecraft curated links and
Apophis close-encounter composition (L-104, downstream of L-046); catalog
growth beyond the current 12 (the object-cache-expansion procedure in the
handoff governs, unchanged); L-040's Studio-side axis fields (only the
assembler-side slice lands here); Voyager flyby close-up composition;
mean-elements extension for satellites/moons (§5, explicit exclusion).

---

## 10. Second-pass ask for Fable and GPT

This synthesis is not asking either of you to rebuild from scratch. Read
it for: (a) whether the resolution of your own divergence (Section 1's
table) is fair to what you actually argued; (b) whether F1-F4 and the
mean-elements scope (Sections 4-5) are correctly understood and correctly
gated; (c) anything either of you would still push back on. Flag
disagreement plainly rather than silently accepting a resolution you don't
actually think is right — that's the entire point of a second pass.

---

## Ref

`PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.3.md` (full record); Fable's manifest;
GPT's manifest; `data/objects_config.json`,
`data/solar-system/coverage_index.json`,
`data/solar-system/feature_configs.json`, `tools/gallery_cache_builder.py`,
`tools/test_gallery_cache_builder_offline.py`, `interactive.html`
[all verified @e864fd42]; `palomas_orrery_helpers.py`, `celestial_objects.py`,
`idealized_orbits.py`, `orbital_elements.py`, `orbit_data_manager.py`,
`spacecraft_encounters.py`, `close_approach_data.py`
[all verified @8bce8354].

---
Synthesized July 2026 by Claude Sonnet 5 from Claude Fable 5's and GPT's
independent manifests, for Tony Quintanilla's Mode 7 relay. Tony and Sonnet
remain the orchestration and documentation authority across this relay.
