# Shell Consolidation -- Phase D2 Handoff

**Session:** May 20-21, 2026 (D2 implementation + Round 1/2/3 testing)
**Executed by:** Anthropic's Claude Opus 4.6 (implementation) from manifest reviewed by Claude Opus 4.7 (Mode 7 audit)
**Tested by:** Tony Quintanilla (Mode 5 visual verification)
**Gap analysis:** Anthropic's Claude Opus 4.7
**Integrator:** Tony Quintanilla

---

## Summary

Phase D2 threaded `sun_position` through the unified dispatch into
`rotate_to_sunward()` and `create_sun_direction_indicator()`, activated
Earth (11 deg) and Jupiter (10 deg) magnetic tilts, replaced Neptune's
4-trace magnetic axis + pole markers with a single offset-center diamond
marker (Option C), and removed the duplicate sun direction indicator at
non-center planet paths.

Items 4, 10, 11, 12 are functionally complete in their intended scope:
Sun-centered and static-frame body-centered views. Mode 5 testing
confirmed correct behavior across all eight magnetosphere bodies in
those views.

D2 also caught and resolved two bugs during testing iteration:
- **Line 6194 NameError** (caught by Opus 4.7 Mode 7 review before
  Tony tested). Animation path referenced `_sun_pos_tuple` before
  it was defined in scope. Reverted to default `sun_position=(0,0,0)`
  for animation. Animation rotation deferred to D3.
- **Sun-checkbox-off fallback to (0,0,0)** (caught Round 1 testing).
  When the Sun toggle was off, `positions` dict did not contain a Sun
  entry, so `_sun_pos_tuple` fell back to origin and the indicator
  and rotation lost the Sun. Fixed by independent Sun fetch at
  lines 4500-4506 in `palomas_orrery.py`.

Round 3 testing surfaced one CRITICAL regression and four QUALITY-tier
gaps inside D2's promise, plus several pre-existing items that the
testing exposed. These are catalogued below with proposed fixes.

---

## Files Delivered

| File | Change type | Status |
|------|-------------|--------|
| `shared_utilities.py` | Complete file | Applied |
| `planet_visualization.py` | Snippets 2a-2f | Applied |
| `shell_configs.py` | 8 x `needs_sun_position: True` | Applied |
| `earth_visualization_shells.py` | Snippet 3c (largest) | Applied |
| `mercury_visualization_shells.py` | Snippet 3a | Applied |
| `venus_visualization_shells.py` | Snippet 3b | Applied |
| `mars_visualization_shells.py` | Snippet 3d | Applied |
| `jupiter_visualization_shells.py` | Snippet 3e | Applied |
| `saturn_visualization_shells.py` | Snippet 3f | Applied |
| `neptune_visualization_shells.py` | Snippet 3g | Applied |
| `uranus_visualization_shells.py` | Signature only (already had it) | Applied |
| `orrery_rendering.py` | `rotate_to_sunward` signature | Applied |
| `palomas_orrery.py` | Snippets 4a, 4c-4g + 2 hotfixes + 6194 revert + Sun fetch fix | Applied (Mode 1 by Tony) |

13 files modified. All compile (Pre-flight 0.0 passed).

---

## Items Resolved by D2

| Item | Status | Notes |
|-----:|--------|-------|
| 4    | **DONE (static)** | `sun_position` threaded through all 3 layers for static rendering. Animation deferred to D3. |
| 10   | **DONE** | Double sun direction indicator removed (snippet 4d) |
| 11   | **DONE** | Earth 11 deg, Jupiter 10 deg magnetic tilt activated |
| 12   | **DONE (Option C)** | Neptune single diamond marker; axis line and pole markers removed |

---

## Verification Results -- Round 3 (Tony's Mode 5)

### Sun-centered regression (Section 1.1): mostly PASS

All eight magnetosphere bodies render correctly in Sun-centered and
body-centered static views, with the following pre-existing issues
exposed (none caused by D2):

| Body | Issue | Class |
|------|-------|-------|
| Earth | Outer corona clipped at fly-to-Sun (0.15 AU too small) | D2 quality gap (B) |
| Mercury | Sodium tail oriented to -X, not anti-Sun | D2 quality gap (C) |
| Mars | Induced magnetosphere has no hover/info marker | Pre-existing (item 25) |
| Jupiter | No bow shock shell (not implemented) | Pre-existing (item 24) |
| Saturn | No bow shock shell (not implemented) | Pre-existing (item 24) |
| Uranus | Magnetosphere hovertext truncated (`\n` not `<br>`) | Pre-existing (item 27 class) |
| Uranus | No bow shock shell rendering | **Possibly D2-caused** (D) |
| Neptune | Magnetosphere hovertext truncated | Pre-existing (item 27 class) |
| Neptune | Radiation/FAC hover not legend-grouped | Pre-existing |
| Neptune | Arc markers superimposed | Pre-existing (item 28) |
| Neptune | Lassell + Arago ring markers superimposed | Pre-existing |

### Animation smoke (Section 1.2): FAIL

This is the regression. Pre-D2 expected behavior was "shells render,
rotation not applied." Tony observed:

- Sun-centered + animated: planet shells do NOT render for any planet
  (Mercury, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Eris, Pluto)
- Earth-centered + animated: Moon shells render when moon is enabled,
  but Earth shells do not render in moon-centered animations
- Pluto-centered + animated: Pluto shells render, but not when barycentered
- **Venus + Sun-centered + animated: plot CRASHES** (no plot generated)
- Sun shells DO render when animated alongside planets, regardless of center

This was not predicted by the manifest. Gap A below.

### Sun direction indicator (Section 2): PASS with two quality gaps

- 2.1, 2.2, 2.4: correct
- 2.3: Earth indicator and Moon indicator both render and both point
  toward Sun, but they toggle together (single legendgroup) and both
  carry the same legend label `"Sun Direction"`. Gaps D and E.

### Magnetosphere sunward rotation (Section 3): PASS

- Earth (Sun off and Sun on), Jupiter, Mars, off-center Earth from
  Sun-center: all correct.
- Saturn: rotation is moot -- no bow shock and no observable
  asymmetry (item 24 class, deferred).
- Uranus (Section 4.3): no bow shock rendering. Gap (D).

### Magnetic tilt (Section 4): PASS but visually subtle

- Earth 11 deg, Jupiter 10 deg: tilt is geometrically active but visually
  hard to discern. Tony confirmed it is implemented; the visual subtlety
  is intrinsic to small-angle tilt on a large envelope.
- Uranus 60 deg: unchanged, still renders correctly.

### Neptune diamond marker (Section 5): UNANNOTATED

Tony's test results contain no annotations for 5.1, 5.2, or 5.3. By his
convention (annotate only when something is off), this likely means
PASS, but it is not confirmed. **Recommend explicit re-check** before
closing item 12.

### Animation paths (Section 6): see Section 1.2 -- the broader issue
covers what this section was testing.

---

## Gaps and Proposed Solutions

Tagged with the v3.23 criticality framework. The gap label letters
(A-E) correspond to the verification results above.

### Gap A: Animation regression -- non-center planet shells absent [CRITICAL]

**Symptom.** When the center body is Sun (or any body with offset planets),
planet shells render in the static plot but disappear during animation.
Venus crashes outright. Sun shells continue to render during animation.

**What we know:**
- D2 reverted line 6194 to avoid NameError. Animation path uses default
  `sun_position=(0,0,0)`. Confirmed in pre-flight 0.2.
- Adding `sun_position=(0,0,0)` to the signature of
  `create_planet_visualization` (snippet 2d) defaults all existing calls.
  This should not, on its own, cause shells to stop rendering.
- Static path with the same dispatch works correctly. So the dispatch
  itself is healthy.
- This is exactly the parallel-pipelines lesson: position data flows
  through 5 parallel pipelines in `palomas_orrery.py`. Fixing one does
  not propagate.

**What we do not yet know:**
- Whether animation rendering of non-center planet shells worked
  *before* D2 changes landed.
- Whether snippet 4g (`create_planet_visualization(fig, center_object_name,
  shell_vars, sun_position=_sun_pos_tuple)`) at line ~4535 has an analog
  in the animation path that was either (a) not present, (b) present but
  broken, or (c) present but bypassed by D2.
- The Venus crash mechanism specifically (NameError? KeyError? Builder
  exception?).

**Recommended action.** Diagnose before fixing. Two-step:

1. **CRITICAL diagnostic.** Reproduce the Venus crash with console
   logging on. The crash message tells us which pipeline. Run:
   ```
   timeout 60 xvfb-run -a python3 palomas_orrery_dashboard.py 2>&1 | tee venus_crash.log
   ```
   then trigger Sun-center + Venus shells + Animate. Tony does this
   on Windows directly (no xvfb needed).

2. **Investigate animation path.** Map all `create_planet_visualization`
   and `create_celestial_body_visualization` calls in
   `palomas_orrery.py`. The static path has three (line 4535
   center-body, line ~4641 non-center planet, line ~4668 off-center
   Sun). The animation path (around line 6100-6300) likely has at
   least one analog. Compare structure.

3. **Mode 7 candidate.** If the diagnostic is unclear, this is a
   strong Mode 7 case -- Gemini can scan the full animation code
   path without needing the testing context.

**Why CRITICAL.** Animation is a primary user surface. Sun-centered
animation with planet shells is the main use case the orrery
visualizes. A silent regression here is more destructive than a
visible bug.

---

### Gap B: Earth fly-to-Sun distance too small [QUALITY]

**Symptom.** When viewing Earth-centered and clicking the "fly to Sun"
auto-zoom, the camera distance is set to 0.15 AU. The outer corona
extends beyond this. The corona is clipped from view.

**Where.** Fly-to camera logic in `palomas_orrery.py`. Distance is
hardcoded.

**Proposed fix.** Compute the fly-to distance from the outermost Sun
shell radius. Sun outermost-corona shell is roughly 5 solar radii ~=
0.023 AU; if the fly-to should frame the full corona at the position,
use ~0.2 AU or `max(0.15, sun_outer_radius_au * 1.5)`.

This is a targeted snippet, ~5 lines. Easy to fold into D3 or a
D2.1 micro-session. Not blocking.

---

### Gap C: Mercury sodium tail does not respect sun_position [QUALITY]

**Symptom.** Mercury-centered static view shows the sodium tail
oriented along -X (the default builder orientation), not anti-Sun.
All other Mercury shells rotate correctly.

**Diagnosis.** The sodium tail builder is likely a custom shell
that was not updated to receive `sun_position`. Check:

```
grep -n "sodium" mercury_visualization_shells.py
grep -n "sodium" shell_configs.py
```

If the sodium tail is a `CUSTOM_SHELLS` entry, it needs:
1. `'needs_sun_position': True,` in its config (the dispatch flag).
2. Its builder signature updated to accept `sun_position=(0,0,0)`.
3. Its `rotate_to_sunward()` call updated to pass `sun_position`.

This is the same pattern as snippet 3a for the Mercury magnetosphere;
D2 simply did not cover the sodium tail because the manifest scoped
itself to magnetospheres + bow shocks. The sodium tail is an
anti-solar feature (driven by radiation pressure) and physically
should rotate with the Sun direction.

**Decision needed from Tony.** Is the sodium tail in scope for D2.1,
or absorb into D3? Argument for D2.1: it is the same contract as
item 4 and the fix pattern is identical. Argument for D3: D2 is
already complete by manifest scope.

---

### Gap D: Uranus bow shock not rendering [INVESTIGATE]

**Symptom.** Section 3.5 (Saturn) is expected to be missing bow shock
because gas giants haven't had bow shocks built (item 24). But Section
4.3 (Uranus) reports "no bow shock is rendering or in legend." Uranus
*should* have a bow shock since it was on the original sun_position
list (Uranus magnetosphere builder is in the 8 listed in snippet 2.5).

**Hypothesis.** Either:
- Uranus bow shock was never implemented (in which case this is item
  24 territory and not D2), or
- It was implemented but the dispatch wiring is wrong (in which case
  D2 broke or omitted something).

**Verify by reading `uranus_visualization_shells.py`.** Look for a
`create_uranus_bow_shock_*` function. If absent, confirm with Tony
that this is item 24 scope and move on. If present, trace the
dispatch path.

The manifest said "Uranus -- no change. Already has `sun_position`
in signature." This suggests Uranus magnetosphere shell was already
wired pre-D2. The bow shock may or may not be present in the source.

---

### Gap E: Sun direction indicator -- toggle linkage and legend labels [QUALITY]

**Symptom.** When both Earth and Moon shells are enabled and Earth-centered:
- Both indicators render correctly and point toward the (same) Sun.
- Toggling the legend entry for one toggles both off together.
- Both legend entries are labeled identically as `"Sun Direction"`.

**Root cause (proposed).** In `shared_utilities.py:create_sun_direction_indicator()`,
the legendgroup and `name` fields likely don't include the body identifier.
Two indicators with the same `name` and same `legendgroup` toggle together.

**Proposed fix.** In `create_sun_direction_indicator`, parameterize the
legend metadata by `object_type` (already passed in):
- Legend name: `f"{object_type}: Sun Direction"` (or just `"Sun Direction"`
  when `object_type` is None / suppressed body)
- legendgroup: `f"sun_direction_{object_type}"` -- one group per body

This is a `shared_utilities.py` snippet, ~3-5 lines. Verify the
suppression-when-at-Sun logic still holds (it should -- name change
doesn't affect suppression).

**Decision needed from Tony.** Legend name format. Options:
- `"Earth: Sun Direction"` and `"Moon: Sun Direction"` (matches
  "Body: Shell" convention used elsewhere)
- `"Sun Direction (Earth)"` and `"Sun Direction (Moon)"` (groups
  the function name first)
- `"Sun Direction from Earth"` (most readable)

Recommend the first -- it matches the existing convention and groups
indicator entries near the body in the legend.

---

## Gaps Pushed to D3

These items surfaced during D2 testing but are pre-existing or out
of D2 scope:

| Item | Description | Class |
|-----:|-------------|-------|
| 42 | Mars induced magnetosphere missing hover/info marker | New (item 25 deferred from E) |
| 43 | Uranus magnetosphere hovertext truncated (`\n` vs `<br>`) | New (item 27 class) |
| 44 | Neptune magnetosphere hovertext truncated | New (item 27 class) |
| 45 | Neptune radiation hovertext not legend-grouped to magnetosphere | New |
| 46 | Neptune field-aligned current hovertext not legend-grouped | New |
| 47 | Neptune Lassell + Arago ring info markers superimposed | New (item 28 class) |
| 48 | Mercury sodium tail does not rotate with sun_position | New (D2 scope gap C) |
| 49 | Earth fly-to-Sun distance hardcoded at 0.15 AU (clips outer corona) | New (D2 scope gap B) |
| 50 | Sun direction indicators (Earth + Moon) share legendgroup and label | New (D2 scope gap E) |
| 51 | Animation path: non-center planet shells absent; Venus crashes | New (CRITICAL gap A) |
| 52 | Uranus bow shock not rendering (verify if implemented at all) | New (gap D) |

Items 24 and 25 from D1 remain open in their existing classification.

---

## Recommended Path Forward

### Option 1: D2.1 micro-session (recommended for gap A)

Address only Gap A (animation regression) in a focused diagnostic
session. This is CRITICAL and not in D2's original scope; it likely
predates D2 but was exposed by Tony's thorough testing. Diagnose first,
then patch the animation path with the analog of snippet 4c/4g.

Mode 1 (targeted snippets) with Tony applying. Probably 1-3 snippets
in `palomas_orrery.py` once the cause is known.

### Option 2: D3 absorption (for gaps B, C, D, E)

Fold the four QUALITY-tier gaps into the D3 cleanup sweep. They are
all small, targeted fixes that map well to the D3 "polish" character.

| Gap | Files touched | Approx. snippets |
|-----|---------------|------------------|
| B (Earth fly-to) | `palomas_orrery.py` | 1 |
| C (sodium tail) | `mercury_visualization_shells.py`, `shell_configs.py` | 2 |
| D (Uranus bow shock) | `uranus_visualization_shells.py` (if exists) or note as item 24 | 0-3 |
| E (indicator legend) | `shared_utilities.py` | 1 |

Total D3 burden increase: ~4-7 snippets across 4 files. Within D3's
existing scope envelope.

### Option 3: Diagnose only, then re-stage

If gap A turns out to be a deeper architectural issue (e.g., animation
shell-rendering pipeline missing entirely for non-center bodies, not
just sun_position threading), it may merit its own phase (D2.5) or
push D3. Decision after diagnosis.

**Recommended sequence:**
1. Tony reproduces Venus crash with console capture.
2. Claude reads animation path code to map the pipelines.
3. Decide between Option 1 and Option 3 based on findings.
4. Gaps B-E go to D3 regardless.

---

## Bugs Found and Fixed During D2 (already resolved)

| Bug | Round | Root cause | Fix |
|-----|-------|-----------|-----|
| Line 6194 NameError | Pre-test (Opus 4.7 review) | Animation referenced `_sun_pos_tuple` before definition in animation scope | Reverted; animation deferred to D3 |
| Sun-checkbox-off: no rotation/indicator | Round 1 | `positions` dict only has toggled-on objects; `_sun_pos_tuple` fell back to (0,0,0) | Independent Sun fetch at lines 4500-4506 |

---

## Updated Deferred Items Table (post-D2)

The D1 handoff documented items 1-41. D2 closes items 4, 10, 11, 12
and surfaces items 42-52.

| Item | Stage | Description | Status |
|-----:|:-----:|-------------|--------|
| 4 | -- | sun_position wiring (static) | **DONE (D2)** |
| 10 | -- | Double sun direction indicator | **DONE (D2)** |
| 11 | -- | Earth/Jupiter magnetic_tilt_deg | **DONE (D2)** |
| 12 | -- | Neptune magnetic poles -> diamond marker | **DONE (D2 Option C)** -- verify section 5 |
| 24 | E | Gas giant bow shocks | Open (Jupiter/Saturn/Uranus) |
| 25 | E | Mars magnetosphere info marker | Open (now also item 42) |
| 42 | D3 | Mars induced magnetosphere hover/info marker | NEW |
| 43 | D3 | Uranus magnetosphere hovertext truncation | NEW |
| 44 | D3 | Neptune magnetosphere hovertext truncation | NEW |
| 45 | D3 | Neptune radiation hovertext legend-group | NEW |
| 46 | D3 | Neptune FAC hovertext legend-group | NEW |
| 47 | D3 | Neptune Lassell + Arago ring marker superposition | NEW |
| 48 | D3 or D2.1 | Mercury sodium tail sun_position wiring | NEW |
| 49 | D3 | Earth fly-to-Sun distance | NEW |
| 50 | D3 | Sun direction indicator legend differentiation | NEW |
| 51 | **D2.1** | Animation: non-center planet shells absent + Venus crash | NEW -- CRITICAL |
| 52 | Verify | Uranus bow shock rendering (or confirm item 24) | NEW |

Total deferred: D1 closed 14, D2 closes 4, D2 surfaces 11. Net open
items after D2: 27 - 4 + 11 = 34.

---

## Phase D Staging (updated)

### D1: Sun config extraction + switchover -- COMPLETE
(Unchanged from D1 handoff.)

### D2: sun_position threading -- COMPLETE (static), DEFERRED (animation)

Items 4, 10, 11, 12 complete in static scope. Animation deferred
to D3 by manifest design, but Round 3 testing revealed the animation
issue is broader than rotation -- shell rendering itself is absent
for non-center bodies, and Venus crashes. Item 51 elevates the
animation work from a deferred polish to a CRITICAL diagnostic.

### D2.1: Animation diagnostic + critical fix -- PROPOSED

Single-scope micro-session: diagnose item 51, patch animation
pipeline, restore non-center body shell rendering, eliminate Venus
crash. Mode 1 snippets. Estimated 1-3 snippets in `palomas_orrery.py`
once diagnosed.

### D3: Cleanup sweep -- EXPANDED

Original D3 scope plus gaps B, C, D, E (items 48-50, 52) and items
42-47 from Round 3 testing. Asteroid belt migration (item 2),
Neptune sub-items (items 13, 28, 47), and provenance Tier-1
remediation (items 36-39) all carry forward.

---

## Procedural Lessons from D2

Tagged with v3.23 criticality framework.

**[CRITICAL] -- The Round 1 -> Round 2 -> Round 3 cadence matters.**
The Sun-checkbox-off bug was invisible to compile checks, static
analysis, and Mode 7 manifest review. Only Tony toggling the Sun
checkbox off found it. The animation regression was invisible to
Round 1 and Round 2 because Tony hadn't gotten to animation
testing yet. Testing iterates. The protocol's structure -- regression
gate, then features, then animation -- exposed issues in dependency
order. Round 3 found bugs that Round 1 and Round 2 could not have.

**[QUALITY] -- The parallel-pipelines lesson resurfaced.** D2 patched
the static pipelines (5 call sites) but did not patch the animation
pipeline. The manifest acknowledged this explicitly and deferred
rotation to D3. Tony's testing revealed that the animation pipeline
has a separate issue (no shell rendering at all for non-center
bodies) that is not the same as the "no rotation" deferral. Lesson:
when deferring a pipeline patch, smoke-test the deferred pipeline
to confirm it is in a known state, not just to confirm it does not
error.

**[PRACTICE] -- Mode 7 catches manifest bugs before they ship.** Opus
4.7's pre-test review caught the line 6194 NameError. Without that,
Tony's first animation click would have errored out and we would have
had to iterate on the NameError before discovering the shell-rendering
issue. Mode 7 saved a testing round.

**[PRACTICE] -- Annotation conventions matter.** Tony's "no annotation =
pass" convention is efficient but introduces ambiguity at handoff time
(see Neptune section 5 -- unconfirmed status). Future testing protocols
could include an explicit "PASS" marker for sections without issues,
or a final "all unmarked passed" assertion. Low priority, but a
candidate for testing protocol template improvement.

---

## Architecture Notes

The D2 dispatch threading completes the static-frame story. The
contract is:

```
palomas_orrery.py (call site)
    -> sun_position computed once from positions['Sun']
    -> create_planet_visualization(..., sun_position=_sun_pos_tuple)
        -> create_celestial_body_visualization(..., sun_position=sun_position)
            -> dispatcher checks needs_sun_position flag
                -> magnetosphere builder(center_position, sun_position=sun_position)
                    -> rotate_to_sunward(x, y, z, center_position, sun_position)
            -> create_sun_direction_indicator(center_position, sun_position, ...)
```

Three layers, one parameter. Default `(0, 0, 0)` preserves
Sun-centered behavior. Independent Sun fetch handles the
Sun-toggle-off case.

The animation pipeline is parallel and was not threaded in D2.
Whether it has the dispatch contract at all is the diagnostic
question for item 51.

The Neptune diamond marker pattern (Option C) is worth noting as
a design precedent. The original four-trace pattern (magnetic axis
line + 2 pole markers + magnetosphere envelope) consumed legend
space and conveyed physical information that was largely lost in
practice. The single diamond at the offset center carries the same
information (0.55-radius offset, 47-degree tilt, Voyager 2 1989)
in hover text on one marker. This is a generalization of the
single info marker pattern from C1-C4. When a 4-trace assembly
exists to communicate one geometric fact, consolidate.

---

## Credit

```
Module updated: May 2026 with Anthropic's Claude Opus 4.6 (implementation)
                         and Anthropic's Claude Opus 4.7 (manifest review
                         and gap analysis)
```

Opus 4.7 credited for D2 manifest review (catching line 6194 NameError
pre-test) and this handoff gap analysis. Opus 4.6 for D2 implementation,
Round 1 Sun-fetch fix, and the 13-file change set. Tony credited for
Round 1/2/3 testing thoroughness -- specifically for finding both the
Sun-checkbox-off bug and the animation regression, neither of which
was visible from manifest review alone.

---

*Paloma's Orrery | palomasorrery.com*
*"A bad snippet is localized. A complete file from a stale base is destructive." -- May 2026*
*"Testing iterates. Round 3 finds bugs that Round 1 cannot." -- D2 lesson, May 2026*
