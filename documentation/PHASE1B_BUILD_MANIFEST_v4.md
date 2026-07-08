# PHASE 1B BUILD MANIFEST -- export_orbit_cache.py (v4)

**Type:** BUILD MANIFEST (Mode 2 -- agentic, new module)
**Design source:** PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.6 + the model
correction recorded in PHASE1B_MODEL_CORRECTION_HANDOFF.md (this session).
The handoff carries the reasoning; this manifest is the build contract.
**Base:** orrery -- resolve live HEAD at build session start (do NOT hardcode).
This manifest's code claims verified at HEAD `d4c37cf` (July 8, 2026).
**Pre-build gates:**
(1) diff `f1ede52..<live HEAD>` for source files -- **RUN AND PASSED through
    `d4c37cf`** (July 7-8, 2026): the only changes since `3e21970` are
    LEDGER_CONSOLIDATED.md + this manifest doc; zero source files touched.
    If HEAD moves past `d4c37cf`, re-run `d4c37cf..<live HEAD>`.
(2) pre-flight verification (Step 0) -- **RUN on the primary cache**
    (July 8, 2026); results recorded in Section 0-RESULTS below.
**Post-build gate:** provenance scan Tier-1 = 0 on new module before push.

---

## THE v4 CORRECTION (read first)

**v3 and every prior version inverted the product model.** They treated
served **position files** as the primary product and *derived* them by
subtracting an interpolated parent trajectory from a moon's heliocentric
trajectory. That subtraction approach was **already tested and rejected on
the desktop** -- it does not produce correct moon orbits. v4 corrects the
foundation:

> **Osculating elements are the primary orbit product; direct relative-frame
> position vectors are a secondary, where-adequate trajectory layer; the
> subtraction/interpolation path is retired entirely.**

Consequences, itemized:
- **Step 3 is rewritten** from "subtract + interpolate" to "select the direct
  Horizons product." Gone with it: the containment assert, the `np.interp`
  clamp hazard, the interpolation error budget, the Earth-Moon scallop
  check, and the subtraction-based composition contract. None of that
  apparatus was ever needed -- it existed only to make a rejected model work.
- **Invariants #4 (containment) and #7 (interp/nesting budget) are retired**
  and replaced by a center-match invariant (served position center MUST equal
  osculating center, per object -- the Charon@9 lesson).
- **The moon-cadence gate (Step 0-STOP) is reframed.** Because the orbit is
  drawn from osculating elements, *every moon ships its orbit regardless of
  cadence*. The gate is now "does the direct position trace get added,"
  not "does the moon ship."
- The v3 epoch catch stands and is folded into Step 4 (8/9 tranche epochs
  carry HH:MM; parse the whole time, not just the date).

See Section "Why the model inverted" for the reasoning, kept for the record.

## v0.6 schema reconciliation (Stage 2 build)

The emitted `coverage_index.json` and position files are reconciled to the
schema in PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.6 (field names verified
against the handoff's glossary): per-object `name / horizons_id / category /
availability / parent / stored_center / canonical_frame / trajectory_of /
osculating / positions / presets / features`; the positions block
`{file, start, end, step_hours, n_points, size_kb}`; per-object `presets`
arrays; top-level `scene_features`; and `schema_version` "1.0" (the schema
format version the v0.6 example carries -- distinct from the handoff's own
v0.6). Where v0.6 encoded the subtraction model, v4 carries the correction in
the values, documented at the construction site:
- `availability`: `cache-required` is RETIRED. Every non-spacecraft is
  `analytic` (the orbit renders from osculating); a served trace is expressed
  by `positions != null`, independent of availability.
- Invariants: v0.6 #1 (cache-required -> positions), #4 (parent-relative
  parent dependency), #7 (moon/parent grid nesting) are RETIRED -- all three
  were subtraction/composition artifacts. Kept: #2, #3, #5, #6, #8, plus the
  v4 center-match (#C: osculating.center == stored_center).
- `canonical_frame`: adds `barycenter-relative` (the one enum extension) for
  Pluto and Charon, per Tony's ruling that both orbit the barycenter.
- Pluto departs from v0.6's heliocentric-substitution entry: v4 serves Pluto's
  own barycenter-relative wobble (`Pluto@9` + `Pluto_Pluto-Charon Barycenter`),
  so `trajectory_of` is null and `stored_center` is `pluto_barycenter`.
The full output structure is documented in the module docstring (Tony's ask).

---

## Why the model inverted (reasoning for the record)

**The empirical finding (Tony, this session):** the subtraction model was
implemented, tested, and rejected because it did not produce correct orbits
-- "too many perturbations." Two mechanisms explain it:
1. **Catastrophic cancellation.** A moon and its parent both sit at large
   heliocentric radius (Moon/Earth ~1 AU; Io/Jupiter ~5.1 AU). Differencing
   two ~1-5 AU vectors to recover a ~0.003 AU residual (the moon's local
   orbit) discards 2-3 significant figures -- the residual is numerical noise
   at the scale that matters.
2. **Daily-cadence aliasing.** The position cache is sampled daily. A moon's
   sub-daily-to-few-day motion is aliased at that cadence; differencing two
   daily-aliased heliocentric ephemerides cannot reconstruct the true
   relative path.

Horizons serves the correct, fully perturbed relative motion **directly**
when queried with the right center -- which is exactly why the cache holds
direct relative pairs (`Charon_Pluto-Charon Barycenter`,
`Moon_Earth-Moon Barycenter`, and the rest of the Pluto/Haumea/Orcus/Eris
systems). The desktop does not derive them; it fetches them.

**Code confirmation (idealized_orbits.py @ `d4c37cf`):**
- Satellite orbits are an "osculating-only dual orbit system" (lines 70-91):
  Jupiter, Saturn, Uranus, Neptune, Pluto moons, and the TNO systems.
- `plot_idealized_orbits(..., center_id='Sun', ...)` is center-driven --
  "For non-Sun centers, only plots moons of that center body."
- Barycenter mode is implemented: "When 'Pluto-Charon Barycenter' is center,
  Charon and Pluto both orbit the barycenter"; `PLUTO_BARYCENTER_ORBITERS`
  lists both. This realizes the Charon@9 center-match requirement in code.
- The old framing is dead and marked: line 662, a Uranus-moon function with
  "0 live callers (verified 2026-06-01, Opus 4.8). Retained for reference."

**The meta-lesson (for the ledger archive):** manifest v3 was reviewed three
times -- Opus 4.8's manifest catches, Fable 5's verification, and this
session's early passes -- and every pass checked the manifest's **internal
consistency** (field bugs, key conventions, interpolation error math) while
none re-checked its **foundational approach** against the established project
decision. That decision lived in `idealized_orbits.py` and in Tony's
judgment, not in the manifest's lineage. A well-reviewed manifest can still
be founded on a rejected model. The rule this yields: validate a manifest's
core APPROACH against live code at HEAD, not just its internal steps --
the same "the code is the fact, the handoff is a claim" discipline, applied
one level up, to the design premise itself.

---

## 0-RESULTS: pre-flight, run on the primary cache (July 8, 2026)

Facts the build proceeds on (from `--preflight-only` on Tony's
`palomas_orrery_for_github/data/`):
- **All 10 tranche pair keys present; daily cadence (1.000 d/step); AU units.**
  Spans: Earth 2023-2047, Jupiter/Saturn/Io/Titan to 2054, Pluto to 2064,
  Moon/Charon/Voyager/Apophis to 2027.
- **`Pluto_Sun` is the Pluto BODY (id 999)**; `Pluto-Charon Barycenter` is a
  separate id-9 system (`celestial_objects.py`). Per Tony's ruling the test
  serves Pluto in the **barycenter frame**, not the body-heliocentric one
  (the plain heliocentric frame is already exercised by Earth/Jupiter/Saturn).
  `Pluto`'s heliocentric orbit (`Pluto` @sun, a=39.5, full coverage) remains
  available for the solar-system view but is out of the 9-object test.
- **Direct relative-frame pairs exist** (the correct source, no subtraction):
  `Pluto_Pluto-Charon Barycenter` (564 pts, 2025-11-24..2027-06-10),
  `Charon_Pluto-Charon Barycenter` (564 pts), `Moon_Earth-Moon Barycenter`
  (494 pts) and the `@399` Earth-body pair, plus the full Pluto system
  (Styx/Nix/Kerberos/Hydra barycenter-relative). The barycenter's own
  heliocentric path `Pluto-Charon Barycenter_Sun` is only 29 pts / one month
  -- the deferred Phase 2 coverage limit for placing the system in a wide view.
- **Osculating cache healthy, both frames present where needed:** 115 entries;
  9/9 tranche present; **8/9 epochs carry HH:MM**; 0/9 `MA=None`. Center-match
  verified against the cache, not assumed -- `Pluto@9` (a=1.42e-5 AU ~ 2,127 km,
  Pluto's barycenter wobble), `Charon@9` (a ~ 17,460 km), and `Moon@399`
  (center `@399`) all exist and match their served traces' centers.
- **Per-moon position-trace usability at daily cadence:** Moon ~27 pts/orbit
  (adequate), Titan ~16 (adequate), Charon ~6.4 (marginal, Mode 5 call),
  Io ~1.8 (no usable trace -- orbit ships osculating-only).

---

## 1. What We're Building

One desktop developer tool (`export_orbit_cache.py`) that reads the local
caches read-only and writes web-servable files for the interactive gallery.
It lives in the orrery repo root beside `gallery_studio.py`, does not run in
the browser, and never modifies the desktop caches. Plus a small
`feature_configs.json` authored from `SHELL_CONFIGS` (Phase 2 prep).

The pre-flight (Step 0) already ships and has been run (Section 0-RESULTS).
This manifest specifies the remaining export stage (Steps 1-6).

---

## 2. Inputs (all desktop-local, read-only)

| File | Role in v4 | Read via |
|------|-----------|----------|
| `data/osculating_cache.json` | **PRIMARY.** Osculating elements per object, matched to viewing center. The orbit product. | Direct JSON load |
| `data/orbit_paths.json` | **SECONDARY.** Direct relative-frame position vectors (date-keyed, AU). The trajectory layer, served where cadence is adequate. NO subtraction. | Direct JSON load |
| `celestial_objects.py` | `OBJECT_DEFINITIONS` -- Horizons IDs, categories, system membership | Import (clean at HEAD: `datetime` only) |
| `constants_new.py` | `KM_PER_AU` = 149597870.7 | Import |
| `shell_configs.py` | `SHELL_CONFIGS` -- feature params (Phase 2) | Import (pulls plotly transitively -- expected on desktop; no tkinter) |
| `close_approach_data.py` | Apophis / close-approach preset metadata | Import (stdlib + constants) |

---

## 3. Outputs (to target directory)

```
<output_dir>/
  coverage_index.json      # per-object: osculating (primary) + positions
                           #   (null or a served file) + features + metadata
  feature_configs.json     # renderer params from SHELL_CONFIGS (Phase 2 prep)
  positions/
    earth.json             # heliocentric, km        (full coverage)
    jupiter.json           # heliocentric, km        (full coverage)
    saturn.json            # heliocentric, km        (full coverage)
    pluto.json             # center = pluto_barycenter; Pluto_Pluto-Charon
                           #   Barycenter trace + Pluto@9 osculating (~6.4
                           #   pts/orbit -- the barycenter wobble). NOT the
                           #   body-heliocentric frame (that is covered by the
                           #   planets and lives in the solar-system view).
    charon.json            # center = pluto_barycenter; Charon_Pluto-Charon
                           #   Barycenter trace + Charon@9 osculating. IN.
    voyager_1.json         # arc-natural, km
    moon.json              # center = earth (@399); Moon_Earth trace +
                           #   Moon@399 osculating; ~27 pts/orbit
    titan.json             # center = saturn (@699); Titan_Saturn trace +
                           #   Titan osculating; ~16 pts/orbit (pair confirmed)
    (io.json  NOT written) # ~1.8 pts/orbit -- no usable trace; osculating only
  presets/
    (apophis_2029_...json) # only if 2029 position data exists (it does not;
                           #   cache ends 2027 -> preset null, as predicted)
```

**Every tranche object still ships an ORBIT** -- its osculating block in the
coverage index. Position files are the additive trajectory layer, written
only where a direct relative pair exists at adequate cadence. Io's absence
from `positions/` is not a dropped object; its orbit renders from osculating.

---

## 4. Processing Steps

### Step 0: pre-flight (SHIPPED, RUN -- Section 0-RESULTS)
Read-only diagnostics + the (reframed) Step 0-STOP. Retained as
`--preflight-only`. Step 0-STOP now reports, per moon, whether the direct
position trace is added; the orbit always ships.

### Step 1: load and validate inputs
Load `osculating_cache.json` (primary) and `orbit_paths.json` (secondary);
import `OBJECT_DEFINITIONS`, `KM_PER_AU`, `SHELL_CONFIGS`.

### Step 2: define test tranche
Per-object fields carry: `slug`, `osc_key` (the osculating cache key,
matched to center), `position_pair_key` (the DIRECT relative pair, or None),
`viewing_center` (the osculating center -> schema slug), `category`,
`orbit_source` (always `"osculating"` for served orbits), and
`trace_policy` (`"serve"` / `"marginal"` / `"none"` from the cadence check).
`position_pair_key` per the resolved rulings (Section 8), each verified to
have a center-matched osculating entry:
- Pluto  -> `Pluto_Pluto-Charon Barycenter`  (osc `Pluto@9`,  center `@9`)
- Charon -> `Charon_Pluto-Charon Barycenter` (osc `Charon@9`, center `@9`)
- Moon   -> `Moon_Earth`  (osc `Moon@399`, center `@399`) -- the `@399` body
  trace; the Earth-Moon-barycenter trace also exists but is out of the test.
  Confirm the exact key string (`Moon_Earth`) at build.
- Titan  -> `Titan_Saturn`  (osc `Titan`, center `@699`) -- pair confirmed
  present (Tony, prior work); Io -> None (orbit osculating-only regardless of
  cadence).
CENTER_SLUG_MAP extended to the barycenter center names actually present as
pair-key centers (`Pluto-Charon Barycenter` -> `pluto_barycenter`, etc.).

### Step 3 (REWRITTEN): select the direct Horizons product -- NO subtraction
For each object:
1. **Orbit (primary):** emit its osculating block, elements matched to the
   viewing center (Step 4 builds it).
2. **Trajectory (secondary):** if `position_pair_key` is set and
   `trace_policy != "none"`, read that DIRECT relative pair from
   `orbit_paths.json`, sort by date, convert AU->km (`KM_PER_AU`), parse
   dates to JD, and write the position file AS-IS. No parent lookup, no
   interpolation, no containment check, no clamp hazard -- the frame is
   already correct because Horizons produced it in that frame.
3. **Center-match assert (the Charon@9 lesson):** the served position
   `center` MUST equal the object's osculating `center`. Fail loud on
   mismatch -- a position trace in a different frame from its own orbit
   ellipse renders wrong.
4. Heliocentric objects (planets, Pluto-body, Voyager, Apophis) use their
   `<name>_Sun` pair directly; same as-is path, center = sun / arc-natural.

### Step 4: build osculating entries for the coverage index
For each object with `osc_key`:
- Map fields (verified at HEAD): `a->a_au`, `e->e`, `i->i_deg`,
  `omega->peri_deg`, `Omega->node_deg`, `MA->M0_deg`.
- **Epoch parser (v3 catch, confirmed 8/9 on the primary):** strip the
  trailing `" osc."` and parse the remainder with astropy.time. It may be
  `"YYYY-MM-DD HH:MM"` (8/9) or `"YYYY-MM-DD"` (Apophis). Do NOT split-and-
  take-date-only -- that drops the time-of-day (up to ~1d epoch error on M0).
- `MA=None` defensive branch retained (0/9 in the tranche, but keep it):
  try TA->M0 via `e`, else emit without `M0_deg` + loud warning; never
  serialize None as 0.0.
- Resolve center via `resolve_center_slug`; assert Charon -> `pluto_barycenter`.
- Build the structured `source` object from metadata (`horizons_id`,
  `center_body`, `epoch`, `fetched`).

### Step 5: assemble coverage index + assert invariants (rewritten)
- `#1` every tranche object has `osculating != null` (the primary orbit).
- `#2` spacecraft -> `osculating == null`, `positions != null` (Voyager arc).
- `#3` **center-match:** for every object with both, served `positions.center`
  == `osculating.center`. (Replaces the retired containment invariant.)
- `#4` any served moon position is a DIRECT Horizons relative pair, never a
  derived/subtracted one. (Replaces the retired interp/nesting invariant.)
- `#5` `osculating.center` populated AND a valid slug.
- `#6` every `presets[].positions.file` exists (Apophis preset null -> skip).
- `#7` every `positions.file` referenced exists on disk.
- Add `schema_version`, `generated`, generator version, `serving_base`,
  `feature_configs` path, `scene_features`.
- **Phase 2 note (not a Phase 1b contract):** wide-view heliocentric placement
  composes a moon's center-relative orbit onto its center's heliocentric
  position using the DIRECT heliocentric entry for that center. For the Pluto
  system that entry (`Pluto-Charon Barycenter_Sun`) is only 29 pts today --
  recorded as an open Phase 2 coverage question, NOT a subtraction contract.

### Step 6: feature configs (Phase 2 prep)
Read `SHELL_CONFIGS`; write `feature_configs.json` best-effort. Unchanged.

---

## 5. Position file format (unchanged from v3 shape)

Column-oriented `{object, center, frame, unit:"km", epoch_type:"JD", source,
data:{t,x,y,z}}`. Voyager carries `frame:"arc-natural"`. Moons carry
`frame:"relative"` with `center` = the osculating center slug.

---

## 6. Script interface
```
python export_orbit_cache.py [--output-dir <path>] [--full-catalog] [--preflight-only]
```
`--preflight-only` ships and has been run. Export (default mode) is Stage 2.

---

## 7. What to verify after build
1. Provenance scan Tier-1 = 0 on `export_orbit_cache.py` before push.
2. Spot-check a served moon file (Moon or Titan): km scale, JD timestamps,
   `center` = the osculating center slug, point count = cache cadence
   (no decimation -- there is no interpolation step to decimate).
3. Charon (if shipped): `positions/charon.json` center `pluto_barycenter`
   AND coverage_index `osculating.center` also `pluto_barycenter`.
4. Center-match invariant printed pass/fail per object.
5. Coverage index: every object has an osculating orbit; Io present with
   `positions:null`; Apophis preset null.
6. Round trip: copy to gallery repo, a test page fetches `coverage_index.json`
   + one position file + one osculating-only object (Io) and renders both an
   ellipse (Io) and an ellipse+trace (Titan).

---

## 8. Resolved decisions (Tony, this session)
- **Charon: IN, barycenter frame.** The barycenter lies outside Pluto's body,
  so it is the correct center. `Charon_Pluto-Charon Barycenter` trace +
  `Charon@9` osculating. ~6.4 pts/orbit hexagon accepted.
- **Pluto: barycenter frame** (not body-heliocentric) for the test, same
  rationale. `Pluto_Pluto-Charon Barycenter` trace + `Pluto@9` osculating.
  Pluto's heliocentric orbit stays available for the solar-system view but is
  out of the 9-object test (the plain heliocentric frame is covered by the
  planets).
- **Moon: `@399` body frame** for the test. Both `@399` and Earth-Moon-
  barycenter traces exist; only `@399` is required here. `Moon_Earth` trace +
  `Moon@399` osculating.
- **Pluto-Charon relative subsystem** (Styx/Nix/Kerberos/Hydra + fine cadence
  + the 29-pt barycenter heliocentric entry for wide-view placement) --
  DEFERRED to the fine-cadence follow-on; tracked (L-098), not built here.
- **Planet-moon pairs confirmed** (Tony, prior work): `Titan_Saturn` exists
  -> Titan ships a trace (~16 pts/orbit). An Io-Jupiter pair exists too, but
  Io stays osculating-only on cadence (~1.8 pts/orbit), so no Io trace ships
  here. When Io gets a trace in the fine-cadence follow-on, confirm the served
  key is `Io_Jupiter` (Io relative to Jupiter `@599`, to match Io's osculating)
  rather than the inverse `Jupiter_Io` (Jupiter seen from Io). Still confirm
  the exact `Moon_Earth` string and the `@599`/`@699` CENTER_SLUG_MAP additions
  at build.

---

## 9. Lineage
- Design handoff: PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.6
- Model correction + reasoning: PHASE1B_MODEL_CORRECTION_HANDOFF.md (this session)
- Code grounded at orrery HEAD `d4c37cf`: idealized_orbits.py (osculating-only
  satellite systems, barycenter mode, dead-framing marker), celestial_objects.py
  (Pluto 999 vs barycenter 9), osculating_cache_manager.py (keys, fields)
- Pre-flight run on the primary cache July 8, 2026 (Section 0-RESULTS)
- Ledger: L-098 (data serving pipeline)

---

Build manifest v4 written July 2026 with Anthropic's Claude Opus 4.8
(model correction: product model inverted, subtraction path retired,
grounded against idealized_orbits.py at HEAD; Tony's Section-8 rulings
folded in -- Pluto/Charon barycenter frame, Moon @399 -- with the @9/@399
osculating center-match verified against the cache).
Supersedes v3's Step 3 and invariants #4/#7; v3 remains the session record
for the pre-flight scaffolding and the epoch/`NEEDS_POSITIONS` catches.
