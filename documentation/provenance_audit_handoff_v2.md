# Provenance Audit — Handoff v2

## Paloma's Orrery | Tony + Claude + Gemini | April 16, 2026

-----

## Session Continuity

This handoff continues `provenance_audit_handoff_v1.md` (April 15, 2026).
v1 covered the creation of `provenance_scanner.py`, the `info_dictionary.py`
split, and the first `constants_new.py` restructure with Gemini cross-review.

v2 covers the April 16 session: sgr_a_star_data.py fix, CENTER_BODY_RADII
equatorial-vs-volumetric decision reversal, planet_visualization /
planet_visualization_utilities consolidation, and a persistent project
sync issue that paused remaining work.

-----

## What Was Completed This Session

### Step 1: `sgr_a_star_data.py` — AU conversion fix

Wrong values corrected. The module had `AU_TO_KM = 1.496e8` and
`AU_TO_METERS = 1.496e11`, which are off from the IAU 2012 exact value
(149,597,870.7 km) by ~2,129 km per AU.

**Changes:**
- Added `from constants_new import KM_PER_AU`
- `AU_TO_KM = KM_PER_AU` (preserves the local alias name for zero-churn
  at the two internal callsites)
- `AU_TO_METERS = KM_PER_AU * 1000`
- Full citation block inline: `# Source:`, `# Ref:`, `# Verified:`
- Docstring upgraded to v3.20 standard with proper one-line purpose,
  key functions section, consumed-by list, credit line

**Scope containment verified:** no external modules import `AU_TO_KM` or
`AU_TO_METERS` from `sgr_a_star_data.py`, so the rename-to-import was
fully internal. The two internal callsites (lines for Schwarzschild
radius conversion and orbital velocity GR correction) now use the
correct precision.

Status: **Integrated by Tony and compile-verified.**

### Step 2: `constants_new.py` — CENTER_BODY_RADII convention reversal

**The April 15 restructure switched CENTER_BODY_RADII to volumetric mean
for all bodies. This was reversed in the April 16 session to a hybrid
convention: equatorial for major planets, volumetric for small bodies.**

This was a real decision point flagged in handoff v1:

> "Mars and Jupiter in CENTER_BODY_RADII changed from equatorial to
> volumetric mean radii. If shell rendering uses these to draw sphere
> surfaces, equatorial may be more visually correct."

April 16 downstream flow analysis (Claude) showed that shell modules
treat these radii as a *unit of scale*, not just as sphere-drawing
inputs. Literature-cited positions like "Io torus at 5.9 R_J" assume
the equatorial radius (IAU convention). Using volumetric mean silently
introduced ~2.3% position errors (~9,500 km for Io torus).

Tony sent the flow analysis to Gemini for second-pass review. Gemini
agreed with the reversal, citing:
1. Literature alignment (5.9 R_J = 5.9 × equatorial = 71,492 km)
2. Visual truth for oblate bodies (Jupiter/Saturn's equatorial edge is
   where moons and rings orbit)
3. The hybrid approach is most principled (equatorial where oblateness
   is significant, volumetric where "equatorial" is ill-defined)

Both AIs converged. Reversal applied.

**Value changes (seven):**

| Body | Was (volumetric) | Now (equatorial) |
|---|---|---|
| Earth | 6371.0 | 6378.137 |
| Mars | 3389.5 | 3396.2 |
| Jupiter | 69911 | 71492 |
| Saturn | 58232 | 60268 |
| Uranus | 25362 | 25559 |
| Neptune | 24622 | 24764 |
| Pluto | 1188 | 1188.3 |

**Unchanged (kept volumetric, deliberately):**
- Mercury, Venus, Moon — difference sub-0.1%, no functional gain from
  switching
- Bennu, Eris, Haumea, Makemake, Arrokoth, Planet 9 — small/irregular
  bodies where "equatorial" isn't meaningful

**Documentation changes:**
- Dict-level comment rewritten to describe the hybrid convention
- Module docstring extended with a "Revised 2026-04-16" block logging
  the decision reversal and Gemini agreement
- Every major-body entry now shows both values (e.g.
  `'Mars': 3396.2, # IAU 2015 nominal equatorial (volumetric = 3389.5)`)

Status: **Integrated by Tony and compile-verified.** Io torus sanity
check: `5.9 * CENTER_BODY_RADII['Jupiter']` = 421,802.8 km, matches
literature ~421,800 km.

### Step 3a: `planet_visualization_utilities.py` — solar constants consolidation

This file is the "shim" layer per protocol v3.20 Option B: it owns the
body-radius aliases (MERCURY_RADIUS_AU, JUPITER_RADIUS_KM, etc.) that
shell modules consume dozens of times each, but sources its data from
`constants_new.py`.

**Changes:**
- Docstring upgraded to v3.20 standard (one-line purpose, key functions,
  consumed-by, credit line)
- Solar/heliosphere constants (SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU,
  CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,
  STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,
  TERMINATION_SHOCK_AU, HELIOPAUSE_RADII, INNER_LIMIT_OORT_CLOUD_AU,
  INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU, GRAVITATIONAL_INFLUENCE_AU)
  now imported from `constants_new` instead of redefined locally
- Body-radius aliases unchanged in function, still derived from
  `CENTER_BODY_RADII[...] / KM_PER_AU`
- Re-exported via Python's default behavior so shell modules that
  already import from this file keep working unchanged

Status: **Integrated by Tony and compile-verified.** Full import chain
tested with all 14 shell modules loading cleanly.

### Step 3b: `planet_visualization.py` — duplicate elimination

This file had **two layers of duplicates**: a complete local
redefinition of all 15 solar/heliosphere constants, plus a local
shadow redefinition of `KM_PER_AU` on line 278 that shadowed the
import from line 12.

**Changes:**
- Docstring upgraded to v3.20 standard
- Utility import extended to pull solar/system constants and all 24
  body-radius aliases from `planet_visualization_utilities.py`
- Removed all 15 solar/heliosphere local redefinitions
- Removed the shadow `KM_PER_AU = 149597870.7`
- Removed all 12 body-radius local derivations (MERCURY_RADIUS_KM/AU,
  VENUS_RADIUS_KM/AU, EARTH_RADIUS_KM/AU, etc.)
- Replaced the deleted block with a 4-line pointer comment directing
  future readers to the utility import

**Size:** 1,191 → 1,164 lines (net -27). No behavior change — the 32
internal consumers of these constants now resolve them through the
import chain.

**Dead-code verification:** no external modules import body-radius
constants from `planet_visualization.py`. The local redefinitions were
used only within this file's functions, so deletion was safe.

Status: **Integrated by Tony and compile-verified.** Full import test
with all 14 shell modules in place: Jupiter=71492, Mars=3396.2,
Earth=6378.137 confirmed post-switch.

-----

## Four Files Deferred

Step 3 was planned to continue with four more files, each containing
hardcoded `149597870.7` values that should import `KM_PER_AU` from
`constants_new`. These were scoped but not executed due to the sync
issue described below.

| File | Occurrences | Nature |
|---|---|---|
| `apsidal_markers.py` | 5 | Direct multiplications in hover text and diagnostics |
| `idealized_orbits.py` | 45 | Mostly print/hover format strings; one secular-change calc |
| `gallery_studio.py` | 2 | dtick annotation formatting |
| `comet_visualization_shells.py` | 2 | Function-local shadow redefinitions (`SUN_RADIUS_KM`, `KM_PER_AU` in `create_maps_disintegration_marker`; also `SUN_RADIUS_AU` derivation on line 524) |

**`close_approach_data.py`** also has its own `CENTER_BODY_RADII_KM` dict
with a "duplicated here to keep" comment. Tony confirmed this is
historical, not structural. Consolidation was deferred.

All five files should be a single Mode 1 batch when the sync issue is
resolved. Rough plan per file:
1. Verify or add `from constants_new import KM_PER_AU` (and
   `SUN_RADIUS_KM` for comet_visualization_shells)
2. Replace hardcoded numeric literals with the imported name
3. Delete shadow redefinitions inside functions
4. Upgrade docstring to v3.20 if needed
5. Compile-test

-----

## The Sync Issue (Why We Paused)

**Symptom:** The project file tree visible to Claude (`/mnt/project/`) is
not updating when Tony refreshes the project in the UI. Files show
their original timestamps from the start of the conversation and their
original content, even after Tony confirms a refresh.

**Evidence accumulated during session:**

1. **`constants_new.py` state divergence.** Handoff v1 described a
   restructured 690-line file with `info_dictionary.py` split out.
   `/mnt/project/constants_new.py` showed the pre-restructure 2,648-line
   file with no `info_dictionary.py` present. Even after Tony's refresh,
   the project file remained stale. Tony uploaded both files directly
   as attachments, which put them in `/mnt/user-data/uploads/` where
   Claude could read them.

2. **`planet_visualization.py` and `planet_visualization_utilities.py`
   updates.** After Tony integrated Claude's proposed changes to these
   files and uploaded them back to the project, `/mnt/project/` still
   shows the pre-update versions (same original timestamp, same line
   counts, same old "Celestial Body Visualization Module" docstrings).
   The attachments in `/mnt/user-data/uploads/` are correct; the
   project-file copies are frozen.

3. **Inferred: broken-import false alarm.** Late in the session, Claude
   flagged that 9 files (`palomas_orrery.py`, `palomas_orrery_helpers.py`,
   `gallery_studio.py`, `object_type_analyzer.py`, `star_visualization_gui.py`,
   `visualization_2d.py`, `visualization_3d.py`, `visualization_core.py`,
   `exoplanet_stellar_properties.py`) still import `INFO`, `note_text`,
   `object_type_mapping`, or `class_mapping` from `constants_new` —
   names that no longer exist there after the restructure. If true, the
   entire project would currently ImportError at startup.

   **This is almost certainly a sync artifact.** Handoff v1 explicitly
   lists all 9 files as having had their imports updated to point to
   `info_dictionary`. Tony's local project must have the updated
   imports; what Claude sees in `/mnt/project/` is the pre-restructure
   state, frozen.

**Working theory:** `/mnt/project/` appears to be snapshotted at
conversation start and not refreshed by in-conversation project updates
on the Claude side. The two known workarounds are:
- Upload files as direct attachments (goes to `/mnt/user-data/uploads/`,
  which is live)
- Start a fresh conversation (gets a fresh snapshot)

**Why this matters for the audit:** proceeding with consolidation edits
against the `/mnt/project/` view risks either:
- Writing fixes for "bugs" that only exist in the stale copy (wasted work,
  no impact on Tony's real codebase), or
- Missing real bugs because the stale copy shows code that doesn't
  match the current state

Tony's call (quoted): *"otherwise we are chasing a moving target and
prone to mistakes."*

-----

## Resume Plan (Next Session)

### First: verify sync works

1. Start fresh conversation (new snapshot of `/mnt/project/`)
2. Read `/mnt/project/constants_new.py` — confirm it shows the v3.20
   restructured 716-line file with the April 16 hybrid-convention
   CENTER_BODY_RADII block
3. Read `/mnt/project/planet_visualization.py` — confirm it shows the
   v3.20 docstring and the consolidated import block
4. Confirm `/mnt/project/info_dictionary.py` exists and is visible
5. Sample one of the "broken import" files (e.g. `palomas_orrery.py`
   line ~247) — confirm it imports `INFO, note_text` from
   `info_dictionary`, not from `constants_new`

If all five checks pass, sync is working and we proceed. If any fail,
fall back to upload-as-attachment workflow for the affected files.

### Second: execute deferred Step 3

1. `apsidal_markers.py` — 5 replacements, plus check the `AU_TO_KM =
   149597870.7` on line 1824 (function-local, should also import)
2. `idealized_orbits.py` — 45 replacements, all mechanical
3. `gallery_studio.py` — 2 replacements (and confirm `INFO` import is
   correctly pointing to `info_dictionary`, not `constants_new`)
4. `comet_visualization_shells.py` — function-local shadows to delete,
   add `SUN_RADIUS_KM` to the existing `KM_PER_AU` import
5. `close_approach_data.py` — investigate whether the `CENTER_BODY_RADII_KM`
   local dict can be deleted in favor of importing `CENTER_BODY_RADII`

### Third: testing protocol (the "Next session" item from v1)

v1's "testing protocol" task remains deferred. With consolidation
complete, the next natural step is a small test harness that imports
`constants_new` and verifies the published values match the cited
sources (a regression test for the whole provenance audit). This
doesn't exist yet.

### Fourth: INFO dictionary fact-checking (the v1 "Ongoing" item)

181 entries in `info_dictionary.py`, all Public-facing (Criticality=4)
and Recalled (Vulnerability=4). Score=16 each. Priority: MAPS narrative,
solar shell descriptions, spacecraft encounter details. This is a
separate session with its own handoff document.

-----

## Values Currently Verified in `constants_new.py`

As of end of this session (pending sync resolution):

### Fundamental (IAU-defined, exact)
- `KM_PER_AU = 149597870.7` — IAU 2012 exact
- `SUN_RADIUS_KM = 695700.0` — IAU 2015 nominal
- `EARTH_EQUATORIAL_RADIUS_KM = 6378.137` — IAU 2015 nominal
- `JUPITER_EQUATORIAL_RADIUS_KM = 71492.0` — IAU 2015 nominal
- `SPEED_OF_LIGHT_KM_S = 299792.458` — NIST/SI exact

### Derived (computed, never hardcoded)
- `SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU` — 0.00465047...
- `LIGHT_MINUTES_PER_AU = KM_PER_AU / SPEED_OF_LIGHT_KM_S / 60.0` — 8.31675...

### Spacecraft reference
- `PARKER_CLOSEST_RADII = 9.86` — Perihelion 22, Dec 24 2024 (Gemini
  catch v1)

### Hybrid-convention body radii
- Sun, major planets, Pluto: equatorial (IAU 2015 nominal + Nimmo 2017)
- Mercury, Venus, Moon: volumetric mean (oblateness sub-0.1%)
- Small bodies: volumetric mean (equatorial ill-defined)

-----

## New Principles Established This Session

### The Hybrid Radius Convention

Planetary body radii serve two distinct purposes in code: they draw
sphere surfaces (where "the physical planet" is the question), and
they provide a unit of scale for positions cited in literature (where
"what did the paper mean by R_J" is the question). The second use is
what dominates in shell modules, and the second use is strictly
equatorial by planetary-science convention.

Rule: if a body's oblateness is >0.1% AND the code scales positions by
the radius (as in `5.9 * JUPITER_RADIUS_AU`), use equatorial. For small
bodies where "equatorial" is ill-defined (irregular, extremely
ellipsoidal, or model-estimate), use volumetric mean. For bodies with
sub-0.1% oblateness (Mercury, Venus, Moon), either works; volumetric is
the conventional fact-sheet value.

### Mode 7 Reversal Is Legitimate

The April 15 Mode 7 session (Claude + Gemini) converged on volumetric
mean. The April 16 session (Claude alone initially, then Gemini asked
with downstream-flow context) converged on equatorial. Both were
good-faith analyses; the April 16 call was better because it had
information the April 15 session did not (how the values flow into
literature-scaled shell positions).

Lesson: Mode 7 doesn't produce a final answer, it produces a
well-reasoned answer at a moment in time. New information can
legitimately reverse a prior Mode 7 conclusion. Document the reversal
with the new context and the original reasoning preserved, so future
readers see why.

### The Sync Issue Is A First-Class Operational Hazard

The project sync issue isn't just an inconvenience — it creates exactly
the "confident confabulation about the wrong version of reality"
failure mode that started this whole audit. When Claude's view of the
codebase disagrees with Tony's, edits cannot be trusted. The correct
response is to pause and confirm state, not to proceed and hope.

This generalizes: any time Claude's internal model of the codebase
state is stale (long conversation, multi-session context drift,
refreshed uploads that may or may not have propagated), the right move
is to verify against a known-current source before continuing.

-----

## Module Updates (Credit Lines)

Files modified in this session, per v3.18 Credit Line Convention:

- `sgr_a_star_data.py` — docstring updated: `April 15, 2026 with
  Anthropic's Claude Opus 4.6 (provenance audit)`
- `constants_new.py` — docstring updated: `Revised 2026-04-16 by
  Anthropic's Claude Opus 4.6 and Google Gemini` (equatorial reversal)
- `planet_visualization_utilities.py` — docstring updated: `April 16,
  2026 with Anthropic's Claude Opus 4.6 (provenance audit; solar/system
  constants now imported from constants_new.py rather than redefined
  locally)`
- `planet_visualization.py` — docstring updated: `April 16, 2026 with
  Anthropic's Claude Opus 4.6 (provenance audit; body-radius aliases
  and solar/system constants now imported from
  planet_visualization_utilities.py rather than redefined locally.
  Removed shadow redefinition of KM_PER_AU.)`

-----

## Quotables from This Session

"we should follow our 4/16 decision."

"l can't unravel how this evolved, but let's go with 4/16 equatorial.
this is the standard from your information."

"we should use the actual distance. maybe scaling by radii is not
reliable?" — Tony, surfacing the real architecture question

"B is right. keep constants_new simple. aliases live locally and going
forward will be avoided or cleaned out." — Tony, on the shim-layer
decision

"otherwise we are chasing a moving target and prone to mistakes." —
Tony, calling the pause

"I suggest we override the April 15 decision and switch the primary
planets back to equatorial." — Gemini, on the reversal

"The Conflict Analysis: NASA Fact Sheet = Volumetric Mean, Paloma's
Orrery Flow = Equatorial." — Gemini, naming the two usage regimes

-----

*Handoff v2: Three files consolidated. Four files deferred. Sync issue
paused work. Resume when fresh conversation restores sync.*
