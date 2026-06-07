# Shell Consolidation -- Phase D2 Handoff (v2)

**Session:** May 20-22, 2026 (D2 implementation + Round 1/2/3 testing + review)
**Executed by:** Anthropic's Claude Opus 4.6 (implementation) from manifest reviewed by Claude Opus 4.7 (Mode 7 audit)
**Tested by:** Tony Quintanilla (Mode 5 visual verification, Rounds 1-3)
**Gap analysis:** Anthropic's Claude Opus 4.7 (v1), reviewed and corrected by Anthropic's Claude Opus 4.6 (v2)
**Integrator:** Tony Quintanilla

**Status:** D2 DEPLOYED. D3 sequenced and ready to start.

**Next session entry point:** D3.1 -- inventory hovertext labels and
legendgroup assignments across all `*_visualization_shells.py` files,
then plan the sweep. See Phase D Staging for full D3 sequence.

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

D2 deployed to GitHub May 22, 2026. Provenance scanner: 0 Tier-1
on all touched files.

Round 3 testing surfaced pre-existing animation limitations and
QUALITY-tier gaps. These are catalogued below with proposed fixes.

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
| 12   | **DONE (Option C)** | Neptune single diamond marker confirmed (Section 5 PASS). Marker convention correction deferred -- see item 53. |

---

## Verification Results -- Round 3 (Tony's Mode 5)

### Sun-centered regression (Section 1.1): PASS

All eight magnetosphere bodies render correctly in Sun-centered and
body-centered static views. The following pre-existing issues were
exposed during testing (none caused by D2):

| Body | Issue | Item |
|------|-------|------|
| Earth | Outer corona clipped at fly-to-Sun (0.15 AU too small) | 49 |
| Mercury | Sodium tail oriented to -X, not anti-Sun | 48 |
| Mars | Induced magnetosphere has no hover/info marker | 42 (= item 25) |
| Jupiter | No bow shock shell (not implemented) | 24 |
| Saturn | No bow shock shell (not implemented) | 24 |
| Uranus | Magnetosphere hovertext truncated (`\n` not `<br>`) | 43 |
| Uranus | No bow shock shell (not implemented, item 24 confirmed) | 52 -> 24 |
| Neptune | Magnetosphere hovertext truncated | 44 |
| Neptune | Radiation hovertext not labelled to match legend entry + toggles with other traces | 45 |
| Neptune | FAC hovertext not labelled to match legend entry + toggles with other traces | 46 |
| Neptune | Arc markers (Adams, Le Verrier, Galle) superimposed | 47a |
| Neptune | Lassell + Arago ring markers superimposed | 47b |

### Animation smoke (Section 1.2): known limitation accepted

Tony observed that shells render only for the center body during
animation, never for non-center bodies regardless of what the center
is. Specific cases:

- Sun-centered + animated: planet shells do NOT render (any planet)
- Body-centered + animated: that body's shells render; others do not
- Moon-centered + animated: Moon shells render; Earth shells do not
- Pluto barycentered + animated: Pluto shells do not render
- Venus + Sun-centered + animated: no shells render (no crash; earlier
  report of crash was not reproducible on re-test)
- Sun shells DO render during animation regardless of center

This is accepted as a pre-existing limitation, not a D2 regression.
Animation shell rendering for non-center bodies is deferred as its
own comprehensive item (item 51).

### Sun direction indicator (Section 2): PASS

- 2.1: Correct. ONE yellow dashed arrow, hover shows AU + km.
- 2.2: Correct. One arrow on Earth, Sun shells at offset, no arrow
  on Sun body.
- 2.3: Earth and Moon indicators both render and both point toward
  Sun. Directions are not parallel (correct -- different positions,
  same target, so vectors converge). Test protocol language "matches
  Earth arrow direction" should read "both directed toward the same
  Sun position." Indicators share legendgroup and legend label --
  item 50.
- 2.4: Jupiter and Mars correct.

### Magnetosphere sunward rotation (Section 3): PASS

- Earth (Sun off and Sun on), Jupiter, Mars, off-center Earth from
  Sun-center: all correct.
- Saturn: no bow shock rendered (item 24, pre-existing).
- Uranus: no bow shock rendered. Confirmed not implemented (item 24).

### Magnetic tilt (Section 4): PASS

- Earth 11 deg: geometrically active but visually difficult to
  discern at this scale. Intrinsic to small-angle tilt on large
  envelope. Confirmed implemented.
- Jupiter 10 deg: same -- active but not visually discernible.
- Uranus 60 deg: tilt character confirmed unchanged from pre-D2.
  Visual inspection (screenshot reviewed by Opus 4.6) shows
  magnetosphere envelope clearly canted at large angle relative
  to ring plane and orbital plane, consistent with 60-degree tilt.

### Neptune diamond marker (Section 5): PASS

- 5.1: Diamond marker present, labeled "Neptune: Magnetic Field Center."
- 5.2: Old magnetic axis line and pole markers removed. Legend
  shows 1 entry, not 4.
- 5.3: Hover text and legendgroup linkage confirmed.
- Convention note: marker should be open square (`square-open`),
  not filled diamond, per the marker symbol convention (the magnetic
  field center is a position in space, not a physical object).
  Deferred as item 53.

### Animation paths (Section 6): see Section 1.2

Covered by the animation limitation above. Center-body shells render
during animation; non-center do not. No NameError (line 6194 revert
confirmed working).

---

## Decisions Made During Review

| Decision | Outcome |
|----------|---------|
| Gap A (animation shells) | Accept current state. Defer as comprehensive item 51. Not a D2 regression. |
| Venus "crash" | Not reproducible. Behaves like other planets (no shells, no crash). |
| Neptune Section 5 | Confirmed PASS. Item 12 closed. |
| Neptune marker symbol | Should be `square-open` (position in space, not object). Item 53. |
| Sun direction legend labels | Use `"Earth: Sun Direction"` / `"Moon: Sun Direction"` format (matches `"Body: Shell"` convention). Item 50. |
| Indicator legend toggle | Earth and Moon indicators toggling together is confirmation they share legendgroup. Fix in item 50 (separate legendgroups). |
| Section 2.3 protocol language | "matches Earth arrow direction" should read "both directed toward the same Sun position" (convergent, not parallel). |
| Uranus bow shock | Confirmed not implemented. Reclassify item 52 as part of item 24 (gas giant bow shocks). |
| Uranus 60-deg tilt | Confirmed unchanged from pre-D2 via screenshot review. |
| Hovertext-legend consistency | Two issues across all shells: (1) hovertext should lead with legend label so user can identify which entry it belongs to, and (2) each shell should toggle independently via its own legendgroup. Cleanup item 54. |
| Neptune superposition | Arc markers and Lassell/Arago are two separate superposition problems, not one. Split item 47 into 47a and 47b. |

---

## Gaps and Proposed Solutions

Tagged with the v3.23 criticality framework.

### Gap B: Earth fly-to-Sun distance too small [QUALITY]

**Symptom.** Earth-centered fly-to-Sun camera distance is 0.15 AU.
Outer corona extends beyond this and is clipped.

**Fix.** Compute fly-to distance from outermost Sun shell radius,
or use ~0.2 AU. Targeted snippet, ~5 lines in `palomas_orrery.py`.

### Gap C: Mercury sodium tail does not respect sun_position [QUALITY]

**Symptom.** Mercury-centered: sodium tail oriented along -X (default
builder orientation), not anti-Sun. All other Mercury shells rotate
correctly.

**Fix.** Same pattern as snippet 3a: add `needs_sun_position: True`
to sodium tail config in `shell_configs.py`, update builder signature
in `mercury_visualization_shells.py`, thread `sun_position` into
`rotate_to_sunward()` call. 2-3 snippets.

### Gap E: Sun direction indicator legend differentiation [QUALITY]

**Symptom.** Earth + Moon indicators share same legendgroup and same
label "Sun Direction." They toggle together and cannot be
distinguished in the legend.

**Fix (decided).** In `shared_utilities.py:create_sun_direction_indicator()`:
- Legend name: `f"{object_type}: Sun Direction"`
- legendgroup: `f"sun_direction_{object_type}"` (one group per body)
1 snippet in `shared_utilities.py`.

---

## Bugs Found and Fixed During D2 (already resolved)

| Bug | Round | Root cause | Fix |
|-----|-------|-----------|-----|
| Line 6194 NameError | Pre-test (Opus 4.7 review) | Animation referenced `_sun_pos_tuple` before definition in animation scope | Reverted; animation deferred to D3 |
| Sun-checkbox-off: no rotation/indicator | Round 1 | `positions` dict only has toggled-on objects; `_sun_pos_tuple` fell back to (0,0,0) | Independent Sun fetch at lines 4500-4506 |

---

## Updated Deferred Items Table (post-D2)

D1 handoff documented items 1-41. D2 closes items 4, 10, 11, 12
and surfaces items 42-54.

| Item | Stage | Description | Status |
|-----:|:-----:|-------------|--------|
| 4 | -- | sun_position wiring (static) | **DONE (D2)** |
| 10 | -- | Double sun direction indicator | **DONE (D2)** |
| 11 | -- | Earth/Jupiter magnetic_tilt_deg | **DONE (D2)** |
| 12 | -- | Neptune magnetic poles -> diamond marker | **DONE (D2 Option C)** |
| 24 | E+ | Gas giant bow shocks (Jupiter, Saturn, Uranus) | Open -- deferred beyond D3 |
| 25 | E+ | Mars magnetosphere info marker | Open (= item 42) |
| 42 | D3.4 | Mars induced magnetosphere hover/info marker | NEW |
| 43 | D3.4 | Uranus magnetosphere hovertext truncation (`\n` -> `<br>`) | NEW |
| 44 | D3.2 | Neptune magnetosphere hovertext truncation | NEW |
| 45 | D3.2 | Neptune radiation: hovertext not labelled to match legend entry + traces toggle together (should be independent) | NEW |
| 46 | D3.2 | Neptune FAC: hovertext not labelled to match legend entry + traces toggle together (should be independent) | NEW |
| 47a | D3.2 | Neptune arc markers (Adams/Le Verrier/Galle) superimposed | NEW |
| 47b | D3.2 | Neptune Lassell + Arago ring markers superimposed | NEW |
| 48 | D3.3 | Mercury sodium tail sun_position wiring (Gap C) | NEW |
| 49 | D3.3 | Earth fly-to-Sun distance hardcoded at 0.15 AU (Gap B) | NEW |
| 50 | D3.3 | Sun direction indicator: per-body legendgroup + label (Gap E) | NEW -- decided: `"Body: Sun Direction"` format |
| 51 | E+ | Animation: non-center body shells do not render | NEW -- deferred beyond D3 |
| 52 | -- | Uranus bow shock | Reclassified as item 24 |
| 53 | D3.2 | Neptune magnetic center marker: `square-open` not `diamond` (convention) | NEW |
| 54 | D3.1 | All shells: hovertext should lead with legend label + each shell should toggle independently (own legendgroup) | NEW -- sweep, goes first |

Total deferred: D1 closed 14, D2 closes 4, D2 surfaces 13. Net open
items after D2: 27 - 4 + 13 = 36.

---

## Phase D Staging (updated)

### D1: Sun config extraction + switchover -- COMPLETE
(Unchanged from D1 handoff.)

### D2: sun_position threading -- COMPLETE, DEPLOYED
Items 4, 10, 11, 12 complete in static scope. Animation deferred.
Deployed to GitHub May 22, 2026. Provenance scanner: 0 Tier-1.

### D3: Cleanup sweep -- EXPANDED, SEQUENCED

Sequencing decision (May 22, 2026): item 54 goes first because
proper hovertext labels and independent legendgroup toggles are
the infrastructure that makes all other shell work reviewable.
Without them, you can't tell which trace you're looking at during
testing.

**D3.1: Hovertext/legendgroup sweep (item 54)**
Systematic pass across all `*_visualization_shells.py` files.
Two dimensions: (1) hovertext leads with legend label, (2) each
shell gets its own legendgroup for independent toggle. Start with
inventory of current state, then sweep.

**D3.2: Neptune cluster (items 44, 45, 46, 47a, 47b, 53)**
Benefits from D3.1 foundation. All in `neptune_visualization_shells.py`.
Includes magnetosphere hovertext truncation, radiation/FAC label +
legendgroup fixes, two superposition problems, marker convention.

**D3.3: Quick targeted fixes (items 48, 49, 50)**
Mercury sodium tail sun_position wiring, Earth fly-to distance,
Sun direction indicator legend differentiation. High return, low risk.

**D3.4: Remaining items**
Items 42 (Mars info marker), 43 (Uranus hovertext truncation),
and D1 carryovers (asteroid belt migration item 2, provenance
Tier-1 items 36-39).

**Deferred beyond D3:**
Item 24 (gas giant bow shocks) and item 51 (animation shell
rendering for non-center bodies) -- new feature work, larger scope.

---

## Procedural Lessons from D2

Tagged with v3.23 criticality framework.

**[CRITICAL] -- The Round 1 -> Round 2 -> Round 3 cadence matters.**
The Sun-checkbox-off bug was invisible to compile checks, static
analysis, and Mode 7 manifest review. Only Tony toggling the Sun
checkbox off found it. The animation limitation was invisible to
Round 1 and Round 2 because Tony hadn't gotten to animation
testing yet. Testing iterates. The protocol's structure -- regression
gate, then features, then animation -- exposed issues in dependency
order. Round 3 found bugs that Round 1 and Round 2 could not have.

**[QUALITY] -- The parallel-pipelines lesson resurfaced.** D2 patched
the static pipelines (5 call sites) but did not patch the animation
pipeline. The manifest acknowledged this explicitly and deferred
rotation to D3. Tony's testing revealed that the animation pipeline
has a separate limitation (no shell rendering at all for non-center
bodies) that is not the same as the "no rotation" deferral. Lesson:
when deferring a pipeline patch, smoke-test the deferred pipeline
to confirm it is in a known state, not just to confirm it does not
error.

**[QUALITY] -- Mode 7 gap analysis requires review.** Opus 4.7's gap
analysis was thorough but under-specified several items: lumped two
distinct Neptune superposition problems into one item, identified
the hovertext-legend mismatch as only a labeling problem when it was
both labeling and legendgroup independence, and left Neptune Section 5
as unconfirmed. The v2 review caught these. Lesson: Mode 7 output is
a strong first pass but benefits from a second pair of eyes, especially
when the reviewer did not perform the testing.

**[PRACTICE] -- Mode 7 catches manifest bugs before they ship.** Opus
4.7's pre-test review caught the line 6194 NameError. Without that,
Tony's first animation click would have errored out and we would have
had to iterate on the NameError before discovering the shell-rendering
limitation. Mode 7 saved a testing round.

**[PRACTICE] -- Test protocol language precision.** Section 2.3
expected Moon arrow to "match Earth arrow direction" -- but both
arrows point toward the same Sun position from different locations,
so they converge rather than run parallel. Tony's observation was
more precise than the test expectation. Protocol language should
describe the physics ("both directed toward the same Sun position")
not the visual expectation ("matches direction").

---

## Architecture Notes

The D2 dispatch threading completes the static-frame story. The
contract is:

```
palomas_orrery.py (call site)
    -> sun_position computed once from positions['Sun'] or independent fetch
    -> create_planet_visualization(..., sun_position=_sun_pos_tuple)
        -> create_celestial_body_visualization(..., sun_position=sun_position)
            -> dispatcher checks needs_sun_position flag
                -> magnetosphere builder(center_position, sun_position=sun_position)
                    -> rotate_to_sunward(x, y, z, center_position, sun_position)
            -> create_sun_direction_indicator(center_position, sun_position, ...)
```

Three layers, one parameter. Default `(0, 0, 0)` preserves
Sun-centered behavior. Independent Sun fetch (lines 4500-4506)
handles the Sun-toggle-off case.

The animation pipeline is parallel and was not threaded in D2.
Non-center body shells do not render during animation at all
(item 51), which is a prerequisite for animation sun_position
wiring -- shells must render before rotation matters.

The Neptune diamond marker pattern (Option C) is a design precedent:
when a multi-trace assembly exists to communicate one geometric fact,
consolidate to a single marker with hover text. Convention correction
pending (item 53: should be `square-open` per marker symbol convention,
since the magnetic field center is a position in space, not a physical
object).

---

## Credit

```
Module updated: May 2026 with Anthropic's Claude Opus 4.6 (implementation
                         and v2 handoff review)
                         and Anthropic's Claude Opus 4.7 (manifest review
                         and v1 gap analysis)
```

Opus 4.7 credited for D2 manifest review (catching line 6194 NameError
pre-test) and v1 handoff gap analysis. Opus 4.6 for D2 implementation,
Round 1 Sun-fetch fix, 13-file change set, and v2 handoff review
(correcting gap analysis under-specifications). Tony credited for
Round 1/2/3 testing thoroughness -- specifically for finding both the
Sun-checkbox-off bug and the animation limitation, neither of which
was visible from manifest review alone.

---

*Paloma's Orrery | palomasorrery.com*
*"A bad snippet is localized. A complete file from a stale base is destructive." -- May 2026*
*"Testing iterates. Round 3 finds bugs that Round 1 cannot." -- D2 lesson, May 2026*
