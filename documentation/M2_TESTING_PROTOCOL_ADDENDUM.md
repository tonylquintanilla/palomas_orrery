# Gallery Cache Builder -- Testing Protocol Addendum: M2 (F1a Trust + served_window)

Tony Quintanilla, PE | Claude Sonnet 5 | July 2026
Applies to: tools/gallery_cache_builder.py (Phase 2, L-118, F1 manifest v2 sec 5)
Appends to: documentation/TESTING_PROTOCOL.md (M1's Layer 1/2/3 above cover the
original 11-object tranche; this section is M2-specific, same three-layer
structure, same rule -- "runs without errors" is not the gate).

## Layer 1 -- Offline suite (done, reproduced)

Run: `python3 tools/test_gallery_cache_builder_offline.py`
State: **134 checks, 0 failures** (87 pre-existing + 4 M1 shape-validator + 43
M2), from a clean checkout. Independently reproduced in the build sandbox;
paste your own Windows run below to triple-confirm, same as M1's pattern.

**tony**:
```
[paste your python (not python3) run here]
```

**Claude**:
[fill in after Tony's run]

What Layer 1 proves for M2 (logic, statically reasoned):
- `fetch_elements` captures Horizons' `n`; `n_deg_per_day` flows through
  `build_osculating_block`, the A-3 history/fallback path, and into
  `measure_trust`.
- The FLAG-2 wrapper (own `n`, not solar `K_GAUSS`) is wired correctly for
  every category -- confirmed deterministic (`window_days == cap`) for all
  11 non-spacecraft objects under a mocked-but-genuinely-Kepler-consistent
  check vector.
- FLAG-3 (served_window null on any participant failure) fires through the
  real dispatch, not just in the abstract -- forced one object's
  check-vector fetch to fail and confirmed both the per-object `error` and
  the global null.
- FLAG-5/6 cap table and zero-rate handling.

What Layer 1 **cannot** prove (Layer 2's job):
- Whether Horizons' mean-motion column is really named `n`/`N` for these
  object types, and whether it's present for every category in scope.
- Whether the `epochs=[jd1, jd2]` list-form query works for `.vectors()`
  the way it already does for `.elements()` -- untested against the live
  API from this sandbox (no network access to ssd.jpl.nasa.gov).
- Whether the measured error rates are *physically* the shape the design
  expects (see step 1 below) -- Layer 1's mock proves the wiring, not the
  physics.

## Layer 2 -- Live dry-run sequence (Tony's hardware)

Per manifest v2 sec 5.7. Five objects, one per category in scope (sec 5.7
names earth, moon, pluto, apophis, halley -- covering planet, moon,
dwarf_planet, asteroid, comet; jupiter/saturn/io/titan/charon/encke follow
the same pattern as their category-mate and are lower priority for the
first pass).

### Step 1 -- dry-run per representative object; eyeball physical plausibility

```
python tools/gallery_cache_builder.py --dry-run --object earth
python tools/gallery_cache_builder.py --dry-run --object moon
python tools/gallery_cache_builder.py --dry-run --object pluto
python tools/gallery_cache_builder.py --dry-run --object apophis
python tools/gallery_cache_builder.py --dry-run --object halley
```

A dry-run validates and writes nothing outside `.staging` -- same pattern
as M1's Layer 2 step 1. After each, the staged `coverage_index.json`'s
`trust` block for that object is what to inspect (`tools\inspect_staging.py
<staging-dir>` if that tool has a view for it, otherwise read the JSON
directly).

**What "looks right" means here** -- this is physical, not just structural,
so eyeballing matters (per manifest sec 5.7 point 2, quoted directly:
*"planet rates tiny; Moon's rate visibly larger; comet rates largest"*):

- **earth**: two-body Kepler is an excellent approximation of Earth's real
  orbit over a 30-day bracket (other-planet perturbations are a tiny
  effect at this timescale) -- expect `error_rate_deg_per_day` very small,
  `cap_applied` likely equal to `window_days` (the ~365-day period cap
  binds, not the measured rate).
- **moon**: the Sun's perturbation on the Earth-Moon two-body ellipse is
  large relative to Earth's solar perturbations -- expect a materially
  larger `error_rate_deg_per_day` than earth's, and plausibly
  `cap_applied: null` with `window_days` well under the P/8 cap (the
  measured rate binds instead of the cap -- this is the interesting case
  to check, since Layer 1's mock can only ever show `cap_applied` bound).
- **pluto**: still a planet-cap object; expect small rate, similar
  character to earth (dwarf_planet uses the same P-divisor as planet).
- **apophis**: today-anchored (see the answer above this protocol) --
  ordinary asteroid two-body behavior at "today", not flyby geometry;
  expect planet-like smallness, not comet-like largeness.
- **halley**: measured at its Tp-anchor epoch (near perihelion, the fast
  part of a very eccentric orbit) -- expect the largest rate of the five,
  plausibly `cap_applied: null` here too.

If any of these come back inverted (e.g. earth's rate larger than
halley's) that's a real bug to chase before going further, not a rounding
concern.

**tony**:
```
[paste dry-run output + trust block excerpts here]
```

**Claude**:
[fill in after Tony's run]

### Step 2 -- real --first-build; inspect the swapped coverage_index

```
python tools/gallery_cache_builder.py --first-build
```

Confirm:
- `served_window` is populated (non-null) -- or, if null, that the warning
  names exactly the objects whose measurement failed, not a silent
  swallow.
- 11 measured `trust` blocks (`method: "two_body_rate_v1"`) + voyager_1's
  `method: "fetched_positions"`.
- The controlling object (the one whose `window_days` sets the global
  minimum) is physically plausible given step 1's rates -- likely one of
  the comets or the Moon-class bodies... except moons don't participate
  (FLAG-3/5.5 excludes `moon`/`spacecraft` from the global window by
  design), so the controller should be one of earth/jupiter/saturn/pluto/
  apophis/halley/encke. If Pluto's real `a` behaves like a normal ~39.5 AU
  semi-major axis (unlike the Layer-1 mock's placeholder value -- see the
  implementation report), Pluto should NOT be the tightest window on real
  data; if it still is, that's worth a second look.

**tony**:
```
[paste --first-build output here]
```

**Claude**:
[fill in after Tony's run]

### Step 3 -- one real --nightly

```
python tools/gallery_cache_builder.py --nightly
```

Confirm trust blocks refresh (new `element_epoch_jd`/samples) without the
shrink gate or any M1 structural check regressing.

**tony**:
```
[paste --nightly output here]
```

**Claude**:
[fill in after Tony's run]

### Step 4 -- resolver behavior via the dev render page date picker

Per manifest sec 5.7 point 4 (PHASE2_ARTIFACT1_AS_BUILT.md SS7): a date
inside `served_window` renders; a date far outside raises
`OutOfServedWindowError`. This exercises the EXISTING resolver/cache_reader
consumer against the newly populated field -- zero resolver code changes,
so this step is really confirming M2 wired the field resolver already
knows how to read, not testing new resolver logic.

**tony**:
```
[paste render-page check notes/screenshots here]
```

**Claude**:
[fill in after Tony's check]

### Step 5 -- fetch-cost / throttling note

Each non-spacecraft object now costs one additional `fetch_vectors_range`
call per build (both check epochs via the new `epoch_jds` list mode, one
call) -- projected +11 Horizons calls per nightly run. Confirm against the
real `--first-build`/`--nightly` timing/log above; note if Horizons
throttles or slows noticeably. If it ever bites, the manifest names the
sanctioned optimization: batch further (unlikely needed at 11 objects).

**tony**:
```
[paste timing/throttling observations here]
```

**Claude**:
[fill in after Tony's observations]

## Layer 3 -- Schedule

Unchanged from M1: only after Layers 1-2 pass, enable the nightly Task
Scheduler job. M2 adds no new Layer-3 concerns (no new scheduling modes,
no new CLI flags beyond what --first-build/--nightly already cover).

## Known Layer-1-only assumptions Layer 2 must settle

Carried forward from the M2 implementation report, repeated here since
this is the document that tracks the live-verification gate specifically:

1. `Horizons(..., epochs=[jd1, jd2])` for `.vectors()` -- assumed to behave
   like the already-proven `.elements()` list-epoch pattern; unverified
   live.
2. Mean-motion column name (`n` vs `N`) and presence, per object category.
3. Pluto's real semi-major axis will produce a very different (much
   larger, much more plausible) window than the Layer-1 mock's placeholder
   `a` -- expected, not a regression if the real number looks completely
   different from the mocked `1.89e-05` days.
