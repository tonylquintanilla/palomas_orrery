# PHASE 1B MODEL-CORRECTION HANDOFF

**Base SHA (orrery):** `d4c37cfa019163bebbe239397827ce83a6034509`
**Base SHA (gallery):** `4b086a659b6cf9eaaccfcc3b0d6c15e01dbb6471`
**Pushed at:** NOT PUSHED -- design session, zero code committed.
**Type:** DESIGN SESSION (zero code) -- the reasoning trail for the v4 model
correction.
**Companion:** PHASE1B_BUILD_MANIFEST_v4.md (the build contract this reasoning
produced).
**Supersedes:** the subtraction premise of manifest v3 and design handoff v0.6
Step 3; both remain valid session records for everything else (pre-flight
scaffolding, the epoch and `NEEDS_POSITIONS` catches).

---

## What this session did

Started as "build on Fable 5's manifest v3." It became a design correction
after the ground truth contradicted the manifest's foundation twice. No
export code was written; the pre-flight (Step 0) was delivered and run, and
the product model was corrected against the live code.

### Verified (not claimed)
- **SHA round trip.** Both HEADs confirmed live. Orrery moved `3e21970` ->
  `d4c37cf` since Fable 5's verification; the diff for that range is
  LEDGER + this manifest doc only, zero source files -- v3's code claims
  still held at build start.
- **Pre-flight run on the PRIMARY cache** (not the repo backup, which holds
  only 3 non-tranche objects). Real numbers now in manifest v4 Section
  0-RESULTS: all 10 tranche keys present, daily cadence, AU units;
  osculating 9/9 with `Charon@9`; 8/9 epochs carry HH:MM; per-moon
  points/orbit (Moon 27, Titan 16, Charon 6.4, Io 1.8).
- **`Pluto_Sun` is the body (id 999)**, with `Pluto-Charon Barycenter` a
  separate id-9 system -- confirmed in `celestial_objects.py`.
- **Direct relative-frame pairs exist and are the correct source:**
  `Charon_Pluto-Charon Barycenter` (564 pts), `Moon_Earth-Moon Barycenter`
  (494 pts), the full Pluto system. Confirmed by Tony's cache probe.
- **Satellites are osculating-only in the live renderer** -- verified in
  `idealized_orbits.py @ d4c37cf`: the "osculating-only dual orbit system"
  lists (lines 70-91), center-driven `plot_idealized_orbits`, barycenter
  mode for the Pluto system, and a marked dead old-framing (line 662,
  "0 live callers").

### Discrepancy surfaced (the correction)
Manifest v3 -- and every version before it -- treated served **position
files** as the primary product and **derived** them by subtracting an
interpolated parent trajectory. That subtraction model had already been
**tested and rejected on the desktop** (perturbations; see the two
mechanisms below). The established practice, living in `idealized_orbits.py`
and Tony's judgment, is: **osculating elements are the orbit; direct
relative-frame Horizons vectors are the trajectory layer; no subtraction.**
v4 inverts the product model accordingly and retires Step 3 and invariants
#4/#7.

### Why subtraction fails (for the record)
1. **Catastrophic cancellation** -- differencing two large heliocentric
   vectors (~1 AU Moon/Earth, ~5.1 AU Io/Jupiter) to recover a ~0.003 AU
   residual discards the significant figures that carry the moon's orbit.
2. **Daily-cadence aliasing** -- the moon's fast local motion is aliased at
   daily sampling; two daily-aliased ephemerides cannot be differenced back
   into the true relative path.
Horizons produces the correct perturbed relative motion directly when queried
with the right center; the cache stores those direct pairs for exactly that
reason.

## Decisions made this session (were open, now resolved)
- **Charon: IN, barycenter frame** (barycenter outside Pluto's body).
- **Pluto: barycenter frame** for the test (`Pluto@9` wobble, a~2,127 km);
  heliocentric orbit stays available for the solar-system view, out of scope
  for the 9-object test.
- **Moon: `@399` body frame** (`Moon_Earth` + `Moon@399`); the Earth-Moon
  barycenter trace also exists but is not needed for the test.
- **Titan ships a trace** -- `Titan_Saturn` confirmed (~16 pts/orbit). **Io
  osculating-only** on cadence (~1.8 pts/orbit) even though an Io-Jupiter pair
  exists.
- **Pluto-Charon relative subsystem + the 29-pt barycenter heliocentric
  entry** -- deferred to a fine-cadence follow-on; Phase 2 wide-view
  composition of the Pluto system is gated on that coverage.
- **Routing:** proceed in-session (recommended -- code-grounded
  simplification, not broad re-analysis; Fable is credit-metered for no added
  coverage). Opus 4.8 convergence review is the fit if a second pass on the
  inversion is wanted before the build.

## Next-session scope (Stage 2 build)
Write Steps 1-6 of `export_orbit_cache.py` per manifest v4: osculating blocks
for all tranche objects; direct relative-frame position files where the trace
is adequate; center-match assert per object; the confirmed epoch parser;
provenance Tier-1 = 0 before push. The pre-flight scaffolding's
subtraction-oriented fields (`PARENT_OBJECTS`, `stored_center`,
`trajectory_of`) get revised to the v4 fields (`position_pair_key`,
`viewing_center`, `orbit_source`, `trace_policy`).

---

## Ledger delta (detail block -- run ledger_index.py to regenerate the index)

```
#### [L-098] Phase 1b data serving pipeline (gallery track)
<!-- L:098 status:OPEN upd:2026-07-08 section:A flag: rice: -->
- v4 correction: product model INVERTED. Osculating elements are the
  primary orbit product (matched to viewing center); direct relative-frame
  Horizons position vectors are the secondary where-adequate trajectory
  layer. Subtraction/interpolation path RETIRED (empirically rejected on
  desktop -- catastrophic cancellation + daily-cadence aliasing). Grounded
  against idealized_orbits.py @ d4c37cf (osculating-only satellite systems,
  barycenter mode, dead old-framing at line 662). [verified @d4c37cf]
- Pre-flight (Step 0 of export_orbit_cache.py) delivered and RUN on the
  primary cache 2026-07-08. Results in manifest v4 Section 0-RESULTS.
- Pluto_Sun = body 999 (celestial_objects.py); barycenter is separate id 9.
  pluto.json labeled as body; trajectory_of:pluto_barycenter dropped until
  the Pluto-Charon subsystem is served.
- Diff gate f1ede52..d4c37cf: LEDGER + manifest doc only, zero source.
**Tony:** rulings made this session -- Charon IN (barycenter frame), Pluto
barycenter frame, Moon @399; Titan_Saturn + an Io-Jupiter pair confirmed from
prior work. Io stays osculating-only on cadence.
**Gap:** Stage 2 built and pre-tested (export_orbit_cache.py, 623 lines);
coverage index reconciled to design handoff v0.6 (field shape verified);
full output structure documented in the module docstring. Remaining desktop-
side: run against the primary, Mode 5 render check, provenance Tier-1=0 (+ a
ROLE_MAP entry for the new module), push + record SHA. Confirm exact key
strings (`Moon_Earth`, `Titan_Saturn`) at run (export warns->osculating-only
if any differ). Defer Pluto-Charon relative subsystem + Phase 2 barycenter-
heliocentric coverage (29-pt entry) to fine-cadence follow-on.
**Ref:** PHASE1B_BUILD_MANIFEST_v4.md, PHASE1B_MODEL_CORRECTION_HANDOFF.md,
idealized_orbits.py, celestial_objects.py, osculating_cache.json
```

### Candidate lesson for the archive (Part 5 / ledger institutional memory)
> A well-reviewed manifest can still be founded on a rejected model.
> Phase 1b v3 passed three review passes (Opus 4.8 catches, Fable 5
> verification, this session's early passes) that all checked internal
> consistency while none re-checked the foundational APPROACH -- a
> subtraction model already empirically rejected on the desktop -- against
> the live code. The decision lived in idealized_orbits.py and Tony's
> judgment, not the manifest lineage. Rule: validate a manifest's core
> approach against code at HEAD, not just its internal steps. "The code is
> the fact, the handoff is a claim," applied one level up -- to the design
> premise itself.

---

Session written July 2026 with Anthropic's Claude Opus 4.8.
