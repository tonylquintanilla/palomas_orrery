# Provenance Audit -- Handoff v3

## Paloma's Orrery | Tony + Claude | April 17, 2026

---

## Session Continuity

This handoff continues `provenance_audit_handoff_v2.md` (April 16, 2026).
v2 covered the sgr_a_star_data.py fix, CENTER_BODY_RADII equatorial reversal,
the planet_visualization / planet_visualization_utilities consolidation,
and paused due to a project sync issue that prevented further edits.

v3 covers the April 17 session: fresh conversation restored sync, all four
deferred files plus `close_approach_data.py` completed, and design work
for the `test_constants_provenance.py` tool (deferred to next session).

---

## Sync Check -- First Action of Session

Per v2's resume plan, the five-point sync verification ran at session start:

1. `/mnt/project/constants_new.py` -- 715 lines, v3.20 docstring,
   April 16 hybrid-convention block, Jupiter = 71492. **Pass.**
2. `/mnt/project/planet_visualization.py` -- 1,164 lines (matches the v2
   "1,191 -> 1,164 net -27" note exactly), v3.20 docstring, April 16
   consolidation credit. **Pass.**
3. `/mnt/project/planet_visualization_utilities.py` -- 364 lines, v3.20
   docstring, imports from constants_new. **Pass.**
4. `/mnt/project/info_dictionary.py` -- 2,140 lines, v3.20 docstring,
   split from constants_new with provenance documentation. **Pass.**
5. `/mnt/project/palomas_orrery.py` line 276: `from info_dictionary import
   INFO, note_text` (and line 247's `from constants_new import (...)` no
   longer pulls INFO or note_text). **Pass.**

**All five checks passed.** The "9 files with broken imports" alarm from
late in the v2 session was confirmed to be a sync artifact -- the files
already had their imports updated on Tony's side.

Takeaway: the v2 pause decision was correct. Proceeding with edits against
a stale `/mnt/project/` snapshot would have risked either writing fixes for
non-existent bugs or missing real ones.

---

## What Was Completed This Session

Six files touched. Five were the planned Step 3 queue from v2; a sixth
(`planet_visualization_utilities.py`) got a small addition plus line-ending
normalization as a side effect of the comet file consolidation.

### 1. `apsidal_markers.py` -- 8 hardcoded values replaced

**v2 handoff said 5; actual was 8.** The undercount was three more copies of
the `km -> AU` / `AU -> km` pair appearing in three separate distance-from-
surface functions (lines 139/141, 1208/1210, 1337/1339). Plus one
`km_distance = closest_distance * ...` at line 1445 and one function-local
`AU_TO_KM = 149597870.7` at line 1824.

Changes:
- Docstring upgraded to v3.20 standard (one-line purpose, key functions,
  consumed-by, credit line)
- Import extended: `KM_PER_AU` added to the existing `constants_new` import
- 7 `*/` numeric replacements -> `KM_PER_AU`
- 1 function-local `AU_TO_KM = 149597870.7` -> `AU_TO_KM = KM_PER_AU`
  (preserves local alias pattern matching sgr_a_star_data.py)
- Line endings normalized CRLF -> LF (file had pure CRLF)

Size: 78,960 -> 77,526 bytes (-1,434; mostly CRLF -> LF savings).
Syntax and import chain verified.

### 2. `idealized_orbits.py` -- 45 hardcoded values replaced

All 45 occurrences of `149597870.7` replaced with `KM_PER_AU`. Mechanical
change: the number always means "km per AU" in this module's context.

Import line extended: `KM_PER_AU` added to the `from constants_new` line.

One special case at line 3755 had a self-documenting comment:
`a_km = a * 149597870.7  # 1 AU = 149,597,870.7 km`. Both the number and
the comment were updated: `a_km = a * KM_PER_AU  # convert AU to km`.

Credit line updated to note the April 17 provenance audit.

Size: +18 bytes. Syntax verified. AST confirms 45 `KM_PER_AU` references.

### 3. `gallery_studio.py` -- 2 hardcoded values replaced

Both usages are in the 3D axis override block (dtick annotation
formatting for close-approach plots). Added a function-local
`from constants_new import KM_PER_AU` above the inner `if effective_dtick > 0:`
block so the import runs before any usage regardless of the inner branch.

Note: scope analysis showed that `effective_dtick > 0` is guaranteed once
we pass the outer gate, but placing the import one level up removes the
fragility.

Credit line appended with April 17 provenance audit note.

Size: +243 bytes. Syntax verified.

### 4. `comet_visualization_shells.py` -- three shadow constants deleted

Two function-local shadows existed:
- `create_maps_disintegration_marker` had `SUN_RADIUS_KM = 695700.0` and
  `KM_PER_AU = 149597870.7` at the top of the function body
- `create_maps_ghost_tail_trace` had `SUN_RADIUS_AU = 695700.0 / 149597870.7`

All three replaced with module-level imports via the shim:
```python
from planet_visualization_utilities import KM_PER_AU, SUN_RADIUS_KM, SOLAR_RADIUS_AU
```

The function-local `SUN_RADIUS_AU` was renamed to use the canonical
`SOLAR_RADIUS_AU` name (kept as a local alias for minimal churn at the
two callsites in the ghost tail function).

Also: three em-dashes in strings (lines 235, 480, 490) replaced with
ASCII hyphens per the cross-platform character convention.

Credit line appended. Size: +438 bytes. Syntax and full import chain
verified (constants_new -> planet_visualization_utilities shim ->
comet_visualization_shells).

### 5. `planet_visualization_utilities.py` -- SUN_RADIUS_KM re-exported

Required to support the comet file consolidation above. Previous state
re-exported `SOLAR_RADIUS_AU` but not the underlying `SUN_RADIUS_KM`. The
shim now re-exports both:

```python
from constants_new import (
    KM_PER_AU, SUN_RADIUS_KM, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS,
    CENTER_BODY_RADII,
    # ... (rest unchanged)
)
```

Line endings normalized CRLF -> LF (file had pure CRLF from yesterday's
edits). Docstring already v3.20; added an April 17 credit-line block noting
the SUN_RADIUS_KM re-export and LF normalization.

Size: 13,160 -> 12,991 bytes (-169; CRLF -> LF delta).

### 6. `close_approach_data.py` -- REAL BUG FIX, not just cleanup

The local `CENTER_BODY_RADII_KM` dict at line 55 predated the April 16
Hybrid Radius Convention reversal. It still carried volumetric-mean
values where `constants_new.py` had already switched to equatorial. This
produced silent surface-distance errors on any close approach:

| Body | Stale local | Canonical | Delta |
|---|---|---|---|
| Earth | 6371.0 | 6378.137 | +7.1 km |
| Mars | 3389.5 | 3396.2 | +6.7 km |
| Jupiter | 69911.0 | 71492 | +1,581 km |
| Saturn | 58232.0 | 60268 | +2,036 km |
| Uranus | 25362.0 | 25559 | +197 km |
| Neptune | 24622.0 | 24764 | +142 km |

Apophis's April 13, 2029 Earth flyby at 38,000 km center-to-center was
reporting ~31,622 km surface distance; the corrected value is ~31,615 km.
Not user-visible for Apophis, but a Jovian close-approach plot would have
been visibly off.

Changes:
- Docstring upgraded to v3.20 standard
- Added `from constants_new import KM_PER_AU, CENTER_BODY_RADII`
- `AU_TO_KM = 149597870.7` -> `AU_TO_KM = KM_PER_AU` (preserves local alias)
- Local `CENTER_BODY_RADII_KM` dict deleted
- Two usages at lines 279-280 now reference canonical `CENTER_BODY_RADII`
- Credit line added noting the staleness fix

Size: +301 bytes. Syntax and import chain verified.

**This is the failure mode the whole audit was designed to surface.** The
Hybrid Radius Convention reversal on April 16 only changed the values in
`constants_new.py`. Any file with its own local copy kept the old
values silently. The provenance scanner would have flagged this as an
INCONSISTENCY had it been run since April 16.

---

## Process Note: Documenting Removed Identifiers

During the `close_approach_data.py` edit, a self-referential bug appeared:
the new v3.20 docstring described removing the local dict with the prose
"local AU_TO_KM and CENTER_BODY_RADII_KM replaced with..." -- but that
description itself contained the string `CENTER_BODY_RADII_KM`, which
a grep-based audit would treat as a false positive.

Same pattern bit the `apsidal_markers.py` edit: the credit-line prose
"hardcoded 149597870.7 values replaced with..." contained the very number
it documented removing, causing a post-edit assertion to fail.

**Rule (add to protocol Technical Reference):** *when documenting the
removal of a named value or identifier, describe the change using
generic language that doesn't re-state the removed name verbatim.* For
example: "hardcoded AU-in-km values replaced with KM_PER_AU" rather than
"hardcoded 149597870.7 values..."

Add the rule to v3.21 or the next protocol update.

---

## What's Still Deferred

### `test_constants_provenance.py` (next session, designed this session)

Design discussion with Tony converged on building a regression-test
harness for `constants_new.py`. The tool pins every verified numeric
constant with a test assertion that fails if the value ever drifts.

**Complement to `provenance_scanner.py`, not a replacement.**

The scanner answers "where should I be worried?" -- open-ended discovery,
probabilistic scoring, ranked report of candidates for human attention.

The test harness answers "did this specific value drift?" -- binary,
deterministic, a pass/fail signal for CI-style integration.

Both tools share vocabulary (same concept keys: `SOLAR_RADIUS`, `KM_PER_AU`,
etc.) but have different update cadences, different invocation contexts,
and different failure-mode semantics. Separate files.

**Design decisions made:**

| Question | Decision |
|---|---|
| Framework | Standalone `assert` statements matching `test_orbit_cache.py` style. No pytest dependency. |
| Invocation | `python test_constants_provenance.py` -- exits non-zero on any failure. |
| Scope v1 | All numeric constants in `constants_new.py`: fundamental IAU/NIST values, hybrid-convention body radii, solar/heliosphere constants, spacecraft reference values, derivation invariants (~60-80 tests). |
| Scope v1 excludes | The `INFO` dictionary's embedded numeric claims. Too many, too heterogeneous, and they're already Public-facing Recalled (Score=16) for the scanner to flag. |
| Failure output | Standard assertion failures with descriptive messages. No rolling drift log in v1 (candidate for v2). |
| Location | Repo root, matching `test_orbit_cache.py`, `verify_orbit_cache.py`. |
| Integration with scanner | One-way: scanner could optionally read the test file to identify pinned values and downgrade their vulnerability score. Tests have no dependency on scanner. |

**Proposed structure:**

```python
"""
test_constants_provenance.py - Regression tests for verified numeric constants.

Pins every verified constant in constants_new.py against its cited value.
Fails if any value drifts -- forcing deliberate updates with updated
citation comments rather than silent modification.

Run from the project directory:
    python test_constants_provenance.py

Exits 0 if all tests pass, non-zero on any failure.

Complement to provenance_scanner.py:
    Scanner:  where should I be worried? (open-ended discovery)
    Tests:    did this specific value drift? (binary pinning)

Module created: April 17-18, 2026 with Anthropic's Claude Opus 4.7
"""

# Section 1: Fundamental IAU/NIST constants
def test_km_per_au():
    """IAU 2012 Resolution B2: AU redefined as 149,597,870,700 m exactly."""
    assert KM_PER_AU == 149597870.7

# Section 2: Hybrid-convention body radii (April 16, 2026)
def test_jupiter_equatorial():
    """IAU 2015 nominal equatorial. Hybrid convention: major planets
    use equatorial; volumetric mean = 69911."""
    assert CENTER_BODY_RADII['Jupiter'] == 71492

# Section 3: Derivation invariants
def test_solar_radius_au_derived():
    """SOLAR_RADIUS_AU must equal SUN_RADIUS_KM / KM_PER_AU to full precision."""
    assert abs(SOLAR_RADIUS_AU - SUN_RADIUS_KM / KM_PER_AU) < 1e-15

# ... etc.
```

**Build plan (next session, Mode 2 agentic after Mode 1 design is settled):**

1. Read `test_orbit_cache.py` for style reference (list of asserts + main
   block that reports pass/fail counts)
2. Enumerate every numeric constant and dict value in `constants_new.py`
3. For each, write a test function whose docstring carries the citation
4. Group into sections: Fundamental | Body Radii | Solar | Heliosphere |
   Spacecraft | Orbital Periods | Derivation Invariants
5. Add a `main()` that runs all tests and prints a summary
6. Add to dashboard under Developer Tools

### `INFO` dictionary fact-checking (carried over from v1/v2)

181 entries in `info_dictionary.py`. All scored Public-facing (C=4) and
Recalled (V=4) for Score=16 by `provenance_scanner`. Priority: MAPS
narrative, solar shell descriptions, spacecraft encounter details.
Separate session with its own handoff.

Status: **unchanged from v2 -- still the largest outstanding audit item.**

---

## Dashboard Update (Deferred to Next Session)

The `palomas_orrery_dashboard.py` Developer Tools section currently lists
only two tools (Regenerate Module Atlas, Dependency Trace). Expanding it
to expose all currently-useful developer tools was discussed but
**deferred to next session**, so each addition can be discussed
individually per protocol ("design conversation before coding").

Candidate tools to evaluate for inclusion (in rough priority order):

| Tool | Script | Purpose |
|---|---|---|
| Provenance Scanner | `provenance_scanner.py` | Generates `PROVENANCE_AUDIT.md` |
| Test Constants Provenance | `test_constants_provenance.py` | Pins verified constants (new tool, built first) |
| Verify Orbit Cache | `verify_orbit_cache.py` | Cache integrity check |
| Test Orbit Cache | `test_orbit_cache.py` | Regression tests on cache logic |
| Add Docstrings | `add_docstrings.py` | Docstring standardization (preview by default) |

Questions for next session discussion:
- Which of these belong in the dashboard vs. stay as command-line only?
- Order and grouping within "Developer Tools"?
- Interactive console vs. piped-output for each?
- Descriptions -- what's the one-line purpose each button should carry?
- Does `add_docstrings.py` still earn dashboard real estate now that the
  v3.20 docstring pass is complete, or is it reference-only at this point?

Natural sequencing: build `test_constants_provenance.py` first; then
update the dashboard so both the new tool and its siblings arrive in
the same commit.

---

## Resume Plan (Next Session)

### First: verify sync one more time

The v2 lesson stands: assume `/mnt/project/` is stale at conversation
start. Spot-check two or three of this session's six output files are
present and match the output state before proceeding.

### Second: build `test_constants_provenance.py`

Per the design section above. Estimated scope: ~60-80 test functions,
single file, ~600-800 lines. Mode 1 briefly to confirm scope and style
choices (match `test_orbit_cache.py`?), then Mode 2 agentic build.

### Third: update `palomas_orrery_dashboard.py`

Per the Dashboard Update section above. Discuss each candidate addition
individually, then apply them all in one commit. The new
`test_constants_provenance.py` gets added as part of this pass, not
earlier, so both tool and launcher land together.

### Fourth: re-run `provenance_scanner.py` on the updated codebase

The scanner's INCONSISTENCIES section should now be empty (or much
shorter). Verify the `close_approach_data.py` staleness is no longer
flagged. If anything unexpected appears, triage before the INFO fact-check.

### Fifth: INFO dictionary fact-checking

Open its own handoff. 181 entries, V=4 C=4, Score=16. Priority order:
MAPS narrative -> solar shell descriptions -> spacecraft encounters.

---

## Module Updates (Credit Lines)

Files modified this session, per v3.18 Credit Line Convention:

- `apsidal_markers.py` -- docstring rewritten to v3.20 standard; credit:
  `April 17, 2026 with Anthropic's Claude Opus 4.7 (provenance audit;
  hardcoded AU-in-km values replaced with KM_PER_AU import from
  constants_new.py; line endings normalized to LF)`

- `idealized_orbits.py` -- credit line appended:
  `April 17, 2026 with Anthropic's Claude Opus 4.7 (provenance audit;
  45 hardcoded AU-in-km values replaced with KM_PER_AU import from
  constants_new.py)`

- `gallery_studio.py` -- credit line appended:
  `April 17, 2026 with Anthropic's Claude Opus 4.7 (provenance audit;
  2 hardcoded AU-in-km values replaced with KM_PER_AU)`

- `comet_visualization_shells.py` -- credit line appended:
  `April 17, 2026 with Anthropic's Claude Opus 4.7 (provenance audit;
  function-local KM_PER_AU, SUN_RADIUS_KM, SUN_RADIUS_AU shadows replaced
  with module-level imports from planet_visualization_utilities; em-dashes
  replaced with ASCII hyphens)`

- `planet_visualization_utilities.py` -- credit line appended:
  `April 17, 2026 with Anthropic's Claude Opus 4.7 (provenance audit;
  added SUN_RADIUS_KM re-export for comet_visualization_shells.py;
  line endings normalized to LF)`

- `close_approach_data.py` -- docstring rewritten to v3.20 standard; credit:
  `April 17, 2026 with Anthropic's Claude Opus 4.7 (provenance audit;
  local AU conversion and radii dict replaced with imports from
  constants_new.py. The previous local radii dict had pre-April-16
  volumetric-mean values, so Jupiter surface distances were off by
  ~1,580 km and Saturn by ~2,000 km under the current Hybrid Radius
  Convention. Consolidation fixes that staleness.)`

---

## Quotables from This Session

"we will note the crlf ending issue for a complete review at a later
date. let's clean up the files we touch and move on with replacements."
-- Tony, on the cleanup policy for this session

"should this functionality be part of the existing tool and operate
simultaneously instead of another tool?" -- Tony, on the
scanner-vs-tests question that clarified the separation of concerns

"could you update the handoff. including the new test_constants_provenance
tool. and also, update the palomas_orrery_dashboard with all the
currently available developer tools, if they are still useful."
-- Tony, closing the session

---

## New Principles Established This Session

### Opportunistic Cleanup Rule

When touching a file for a targeted edit, opportunistically clean up
parallel issues the file already has: CRLF normalization, em-dash
replacement, docstring upgrades to v3.20, credit line updates. Do NOT
open a separate cleanup pass for the whole codebase.

Rationale: each file touched is one commit. A combined touch is one
review surface. A separate cleanup pass is N commits with N review
surfaces and requires separate verification for each. Bundling is cheaper
when the file is already under active edit.

Exception: if the cleanup itself has semantic risk (e.g. a line-ending
change that could break a downstream tool), split it into a follow-up
commit for clean attribution.

### Scanner + Tests = Discovery + Pinning

`provenance_scanner.py` and (future) `test_constants_provenance.py` are
complements, not competitors. The scanner is heuristic and open-ended
("where should I be worried?"). The tests are deterministic and
pinning ("did this specific value drift?"). They should share vocabulary
but stay in separate files with different update cadences.

The scanner follows the `module_atlas + provenance_scanner` pattern:
one-way integration, shared infrastructure, separate concerns.

### Documenting Removed Identifiers

When a commit documents the removal of a named value, use generic
language in the documentation ("hardcoded AU-in-km values") rather than
the verbatim identifier ("hardcoded 149597870.7 values"). Otherwise the
documentation itself will false-positive against grep-based audits of
what was removed.

Corollary: when a docstring describes a deleted dict
(`CENTER_BODY_RADII_KM`), reference the category ("radii dict") not the
deleted name. Preserves historical intent without creating audit noise.

---

*Handoff v3: Step 3 complete (6 files touched). `close_approach_data.py`
staleness fixed -- real bug, not just cleanup. `test_constants_provenance.py`
designed and deferred to v4 session, followed by a discussion-first
dashboard update in the same commit.*
