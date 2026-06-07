# HANDOFF: Shell Consolidation Stage 3 -- Dispatch Discovery (v14)

**Date:** May 27, 2026
**Session model:** Claude Opus 4.7
**Supersedes:** v13 (which was written before the dispatch discovery
and is partly wrong -- see "Correction to v13" below)
**Predecessor of record:** v12

---

## READ THIS FIRST: the headline finding

**Info marker styling for sphere shells comes from ONE centralized
factory -- `create_info_marker()` in `orrery_rendering.py` -- not from
the inline markers in the `*_visualization_shells.py` files.**

For every body whose interior/atmosphere/hill-sphere shells are
defined in `SHELL_CONFIGS` (which is all 13: Mercury, Venus, Earth,
Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Eris, Planet 9,
Sun), the sphere shells render through:

```
SHELL_CONFIGS (shell_configs.py)
  -> build_sphere_shell(config, ...)  (orrery_rendering.py, dispatch line 387)
    -> create_info_marker(...)        (orrery_rendering.py -- THE control point)
```

`create_info_marker()` is hardcoded:
```python
marker=dict(size=8, color=color, opacity=1.0,
            symbol='cross', line=dict(color='red', width=2))
```

**The inline `marker=dict(...)` blocks inside the `create_*_shell`
functions in the shell files are DEAD CODE for these sphere shells.**
The legacy path that would call them (`create_planet_shell_traces`,
the `globals()` lookup at planet_visualization.py:671) is imported
but **never invoked anywhere** in the live codebase (verified by
grep across all files -- only docstring mentions, zero calls).

**Implication:** most of this session's Stage 3 inline-marker sweep
edited dead code. It compiled, imported, and passed container tests
because the functions are still *callable* -- they are just never
*called*. The plots looked "converted" because the factory already
produces red-bordered crosses; that was true before the sweep and
after.

---

## How the discovery happened

Tony plotted Moon (center view) repeatedly while we tried to fix the
info-marker contrast on the dense red outer_core shell. Three
successive edits to `create_moon_outer_core_shell` in
`moon_visualization_shells.py` -- a width bump, a double marker, a
white-fill double marker -- produced NO visible change each time.

The Moon plot output log showed Moon rendering as a SHELL_CONFIGS
body. Tracing the dispatch revealed Moon's sphere shells go through
`build_sphere_shell()` -> `create_info_marker()`, never touching
`create_moon_outer_core_shell`. The edits were to dead code.

This is the third time this session that an incorrect mental model
of the dispatch led to wrong action (after the Earth "minimal fix"
and the marker-width assumption). The pattern is clear enough to be
its own lesson (Lesson 6 below).

---

## The verified dispatch map (the deliverable that matters)

Two live paths. Everything routes through one of them; the legacy
inline path is dead.

### Path 1 -- Sphere shells (SHELL_CONFIGS)

```
SHELL_CONFIGS[body][shell] = {name, color, opacity, n_points,
                              marker_size, radius_fraction|radius_au,
                              hover_text, tooltip}
  -> build_sphere_shell(config, body, center_position)
    -> geometry trace (Scatter3d or Mesh3d, from config)
    -> create_info_marker(...)  [HARDCODED red cross, factory]
```

Covers the sphere shells (cores, mantles, crusts, atmospheres, hill
spheres) of all 13 bodies. **Marker styling = factory only.** The
config controls fill color, size, opacity, n_points, hover text --
but NOT the info-marker border/symbol. That is the factory's job.

### Path 2 -- Custom geometry (CUSTOM_SHELLS)

```
CUSTOM_SHELLS[body][shell] = {'builder': 'module.function', 'tooltip'}
  -> lazy import the named function from the shell file
    -> the function runs its OWN code, including its OWN inline markers
```

Covers magnetospheres, ring systems, radiation belts, plasma tori,
sodium tails, LEO/GEO belts, Oort structures. **These call the real
shell-file functions, so their inline markers ARE live.**

CUSTOM_SHELLS builders (verified live):
- Mercury: sodium_tail, magnetosphere
- Venus: magnetosphere
- Mars: magnetosphere
- Earth: magnetosphere, leo, geostationary_belt
- Jupiter: magnetosphere, io_plasma_torus, radiation_belts, ring_system
- Saturn: magnetosphere, enceladus_plasma_torus, radiation_belts, ring_system
- Uranus: magnetosphere, radiation_belts, ring_system
- Neptune: magnetosphere, radiation_belts, ring_system
- Sun: hills_cloud_torus, outer_oort_clumpy (and more)

---

## Correction to v13: what was real vs. fiction

v13 reported "73 conversions, 8 preserves" as delivered work. With
the dispatch map, that sorts cleanly:

| v13 claimed work | Path | Verdict |
|------------------|------|---------|
| 73 inline marker conversions (sphere shells) | Path 1 | **FICTION** -- dead code; factory controls these |
| 8 red-on-red preserves (sphere shells) | Path 1 | **FICTION** -- dead code |
| Planet 9 n_points 50->25 | Path 1 (SHELL_CONFIGS already had n_points=20) | **FICTION** -- live value was already 20 |
| Saturn ring marker geometry fix | Path 2 (CUSTOM_SHELLS ring_system) | **REAL** |
| Uranus ring marker geometry fix | Path 2 (CUSTOM_SHELLS ring_system) | **REAL** |
| Earth magnetosphere recovery (rotation) | Path 2 (CUSTOM_SHELLS magnetosphere) | **REAL** |
| Earth magnetosphere TypeError context | Path 2 | superseded by recovery; the GitHub baseline was already correct |
| Sun direction dormant-call deletions (20) | dispatch post-loop indicator | **REAL** -- verified one-indicator-per-body empirically |
| Dead import removals (10) | n/a (true cleanup) | **REAL** -- the imports were genuinely unused |
| orrery_rendering.py migration-intent docstring | n/a (documentation) | **REAL** but now needs updating to reflect this discovery |

**Net real deliverables from this session:**
1. Saturn + Uranus ring marker geometry fixes (CUSTOM_SHELLS, live)
2. Earth magnetosphere regression recovery (CUSTOM_SHELLS, live)
3. Sun direction duplicate-call cleanup (20 deletions, dispatch-verified)
4. Dead import removals (10)

**Net fiction (dead-code edits, harmless but inert):**
1. 73 sphere-shell inline marker conversions
2. 8 sphere-shell red-on-red preserves
3. Planet 9 n_points change

The fiction edits are harmless -- they compile and don't break
anything; they just don't render. But they should NOT be relied upon
as having changed anything visual, and the credit lines claiming
them as marker work are misleading and should be corrected.

---

## Decision for next session (Tony's plan)

**Continue testing with the Moon file until satisfied, THEN
propagate to the other files.** But with the dispatch map in hand,
"the Moon file" now means the right control point:

The Moon outer_core contrast experiment must be done where it
actually renders -- which for the sphere-shell path is
`create_info_marker()` in `orrery_rendering.py` and/or a per-config
override in `SHELL_CONFIGS`. Editing `create_moon_outer_core_shell`
will continue to do nothing for the static Moon plot.

**The Moon file is currently left AS-IS** (Tony's instruction): it
carries the unresolved white-fill double-marker experiment plus
Tony's manual changes. It is NOT reverted. It is a parked
experiment. Note: that experiment is in dead code, so it has no
visual effect -- it is preserved as a record of the intended marker
design, to be ported to the real control point next session.

---

## Recommended approach for the contrast fix (next session)

The contrast problem (white/red markers invisible on dense red dot
fields) is now a SINGLE-POINT fix, not a per-file sweep. Options,
in order of cleanliness:

### Option A -- Factory parameter + per-config override (recommended)

1. Add `border_color='red'` parameter to `create_info_marker()`.
2. Add `fill_color=None` parameter (defaults to shell color; allows
   white/yellow override).
3. Have `build_sphere_shell()` read optional config keys
   (e.g. `info_border`, `info_fill`) and pass them through.
4. Add those keys ONLY to the SHELL_CONFIGS entries that need them
   (the dense red shells: Moon outer_core, Pluto core/mantle,
   Eris core/mantle).

Result: the fix lives in the config + factory, exactly where the
live render reads from. No shell-file edits. Self-documenting (the
config says `info_fill: 'white'`).

### Option B -- Auto-detection in the factory

`create_info_marker()` inspects fill color, picks border/fill by a
redness threshold. Less config noise, more "magic," harder for Mode
5 to override per-site. The threshold sits between R=180 (warm tones
that read fine with red border, e.g. rgb(255,180,140)) and R=187
with low G/B (Eris core rgb(187,63,63), which does not). Tight but
defensible.

### What the experiment proved (port this knowledge)

- Border WIDTH is ignored in Plotly Scatter3d (plotly.js #4118).
  Only fill color, size, symbol, and border COLOR render.
- Therefore the contrast lever is FILL color (and optionally symbol
  shape), not border. A white-filled or yellow-filled cross reads
  on dense red; a shell-colored cross with any border does not.
- 3D symbol palette is only 8: circle, circle-open, cross, diamond,
  diamond-open, square, square-open, x. Free for info-marker
  variants: filled `square` and `x` (both unused in convention).
- The double-marker (open square ring + cross) is a candidate but
  unproven -- it was tested only in dead code. Re-test at the real
  control point.

### Propagation plan (after Moon satisfies Mode 5)

Once the fix works for Moon outer_core at the real control point,
the dense-red sites needing it are: Moon outer_core, Pluto core,
Pluto mantle, Eris core, Eris mantle. With Option A, that is 5
config entries gaining `info_fill: 'white'` (or whatever wins). The
warm-tone sites (Earth/Mars/Venus inner_core, etc.) tested fine with
the factory's default red border and need nothing.

---

## State of the deliverables

The 14 files generated this session are in outputs. Recommended
disposition:

- **Deploy the REAL work:** Saturn, Uranus (ring fixes), Earth
  (magnetosphere recovery + dead import), and the sun-direction
  cleanup across asteroid_belt, jupiter, mars, venus, eris, planet9,
  pluto (dormant-call deletions + dead imports). These are genuine.
- **The sphere-shell inline marker conversions are inert.** They do
  no harm deployed (dead code), but they also do nothing. Decision
  for Tony: deploy them anyway (consistency, and they become live IF
  a future refactor ever re-activates the inline path -- unlikely),
  or strip them to keep the shell files honest. Recommend deploying
  as-is to avoid yet another edit round, with the credit lines
  corrected to not over-claim.
- **Correct the credit lines** on the sphere-shell files: they
  currently claim "info markers brought to red-border standard,"
  which is misleading since the factory controls that. Suggested
  correction: "inline markers updated for consistency; note these
  are not the live render path -- see handoff v14."
- **Moon file: leave as-is** (parked experiment, per Tony).

If a clean deploy is wanted, the minimal honest set is just the REAL
work (Saturn, Uranus, Earth, + the 7 sun-direction-cleanup files).
The sphere-shell marker conversions can be dropped entirely without
visual consequence.

---

## Lessons for the Archive

(Lessons 1-5 from v13 stand -- uploaded-files-over-project,
visual-verification, minimal-fix anti-pattern, verify-rendering-
empirically, know-when-to-stop. Added:)

### Lesson 6 [CRITICAL]: Map the dispatch before editing the leaves

Three times this session, acting on an assumed dispatch structure
produced wrong work: the Earth "minimal fix," the marker-width
assumption, and the dead-code sweep. The shell files LOOK like the
place to change shell appearance -- they have the marker dicts right
there. But the live render path for sphere shells goes through
SHELL_CONFIGS -> build_sphere_shell -> create_info_marker, and the
inline markers are vestigial. **Before editing any leaf function,
trace from the GUI call through the dispatch to confirm the leaf is
actually on the live path.** A grep for "where is this function
CALLED (not imported)" would have caught this on day one.

The tool that should exist: a dispatch map in MODULE_ATLAS.md
showing, for each render path, which functions are live and which
are dead. This session is the evidence that the map is worth
building.

### Lesson 7 [QUALITY]: "It compiled and the tests passed" can coexist with "it does nothing"

Every dead-code edit this session compiled, imported, and passed the
functional container test (the function returns a valid trace list).
None of that detects that the function is never called. Container
tests verify a function WORKS; they do not verify it is USED. For
refactors, "is this code path reached" is a separate question from
"does this code path work," and only the former tells you whether an
edit matters.

---

## Next-session opener (concrete)

1. Build the dispatch map: for each of the 13 bodies, list which
   shells go via SHELL_CONFIGS (factory markers) vs CUSTOM_SHELLS
   (own markers). Put it in MODULE_ATLAS.md. (Most of this is in
   this handoff's "verified dispatch map" section -- formalize it.)
2. Implement Option A (factory border_color/fill_color params +
   per-config override) OR Option B (auto-detect). Recommend A.
3. Test on Moon outer_core at the REAL control point until Mode 5
   satisfied.
4. Propagate the chosen fix to the 5 dense-red config entries.
5. Decide disposition of the inert sphere-shell inline edits.
6. Re-issue the test protocol to test at the factory/config level.

---

*"Tony's eyes win." -- and this session they caught a regression,*
*an invisible marker, a 7-year-old Plotly bug, AND that an entire*
*sweep was editing dead code. The plots are the ground truth; the*
*code's apparent structure is not.*

*Handoff written: May 27, 2026 with Anthropic's Claude Opus 4.7*
