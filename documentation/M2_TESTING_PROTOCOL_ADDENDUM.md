# Gallery Cache Builder -- Testing Protocol Addendum: M2 (F1a Trust + served_window)

Tony Quintanilla, PE | Claude Sonnet 5 | July 2026
Applies to: tools/gallery_cache_builder.py (Phase 2, L-118, F1 manifest v2 sec 5)
Appends to: documentation/TESTING_PROTOCOL.md (M1's Layer 1/2/3 above cover the
original 11-object tranche; this section is M2-specific, same three-layer
structure, same rule -- "runs without errors" is not the gate).

Anchor: gallery @af3a2c8611293bc865b62c23f61334a2c2941e45 (post-nightly) --
orrery (this doc's home repo) @e2c4f238add2b19390235abd5f6189ff30ff424f

**Status as of 2026-07-22: all three Layers PASS -- full M2 testing protocol
closed.** Layers 1 and 2 (five steps) closed L-149 and L-118's testing gaps
2026-07-21. Layer 3 (nightly Task Scheduler, unattended, real git push, no
manual intervention) closed 2026-07-22 -- verified across two real test
runs, including surviving an accidental double-fire cleanly.

Revision note: this replaces an earlier version of this file that had a raw,
unformatted chat transcript pasted into the middle of Step 2, an unfilled
`[paste ... here]` template surviving in Step 3 alongside the real Step 3
result written elsewhere, and a stale pre-fix Step 2 checklist sitting next
to the corrected one. Content is unchanged in substance; this pass
de-duplicates, fills in the evidence that was missing, and corrects a couple
of counts that were true when first written and are no longer current.

---

## Layer 1 -- Offline suite

Run: `python3 tools/test_gallery_cache_builder_offline.py`

**Original state (before the L-149 fix): 134 checks, 0 failures** (87
pre-existing + 4 M1 shape-validator + 43 M2), from a clean checkout.

**Current state (after the L-149 fix landed): 138 checks, 0 failures.**
Four new checks were added alongside the canonical_frame fix
(tools/test_gallery_cache_builder_offline.py, ~lines 315-379):
- served_window's half-width equals the minimum `window_days` among
  heliocentric-frame participants only
- pluto's own (barycentric) `window_days` is smaller than the controlling
  half-width -- proving the exclusion isn't vacuous, i.e. it's actually
  doing something rather than just never mattering
- a forced pluto check-vector failure leaves pluto's own trust block
  carrying an `error`
- that same forced failure does NOT null the global `served_window` --
  since pluto no longer participates, its failure can't take the whole
  site down anymore (this is the direct fix for the bug Step 1 found)

**Claude:** [verified @32671a19, sandbox re-run] Ran the suite fresh myself
against gallery HEAD after confirming the L-149 fix was present in that
commit: `PASS (138 checks, 0 failures)`. Also confirmed `gallery_cache_builder.py`
and `test_gallery_cache_builder_offline.py` were byte-identical between that
commit and the later `--first-build`/`--nightly` pushes (c5c9ea09, af3a2c86)
-- those were data-only commits, so this 138/138 result still holds at
current HEAD without needing a re-run.

**tony**: (original 134-check run, pre-fix, from a clean checkout)
```
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\tools> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/tools/test_gallery_cache_builder_offline.py
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 12 objects
  ok  first-build structural validation passes (pass)
  ok  clean fakes -> no guard warnings
  ok  12 objects served (12)
  ok  attribution present
  ok  served_window field present
  ok  earth has parity/addition field 'name'
  ok  earth has parity/addition field 'horizons_id'
  ok  earth has parity/addition field 'category'
  ok  earth has parity/addition field 'availability'
  ok  earth has parity/addition field 'parent'
  ok  earth has parity/addition field 'stored_center'
  ok  earth has parity/addition field 'canonical_frame'
  ok  earth has parity/addition field 'trajectory_of'
  ok  earth has parity/addition field 'osculating'
  ok  earth has parity/addition field 'positions'
  ok  earth has parity/addition field 'presets'
  ok  earth has parity/addition field 'features'
  ok  earth has parity/addition field 'orbit_type'
  ok  earth has parity/addition field 'as_of_today'
  ok  earth has parity/addition field 'event_link'
  ok  earth.osculating has 'center'
  ok  earth.osculating has 'epoch_jd'
  ok  earth.osculating has 'a_au'
  ok  earth.osculating has 'e'
  ok  earth.osculating has 'i_deg'
  ok  earth.osculating has 'node_deg'
  ok  earth.osculating has 'peri_deg'
  ok  earth.osculating has 'M0_deg'
  ok  earth.osculating has 'source'
  ok  voyager_1: osculating null, positions present
  ok  voyager_1 position file on disk
  ok  position file unit km
  ok  B-3: serving_base + scene_features restored for v0.6 parity
  ok  B-3: positions block carries step_hours
  ok  earth as_of_today is km-scale (|r|=1.5e+08)
  ok  encke serves Tp_jd + solution_Tp_jd
  ok  encke orbit_type elliptical (e<1)
  ok  halley serves Tp_jd + solution_Tp_jd
  ok  halley orbit_type elliptical (e<1)
  ok  pluto/charon centered on pluto_barycenter
  ok  raw vectors written
  ok  elements JSONL history written
  ok  run manifest written
  ok  M1: feature_configs schema_version present
  ok  M1: feature_configs has all 12 object slugs
  ok  M1: every served feature entry is a dict (no lists survive)
  ok  M1: earth has van_allen_belts + atmosphere_shell
  ok  M1: earth van_allen_belts.inner_belt_distance == 1.5
  ok  M1: earth atmosphere_shell has atmosphere + upper_atmosphere
  ok  M1: jupiter has radiation_belts and NOT magnetosphere
  ok  M1: jupiter ring_system has all four ring slugs
  ok  M1: saturn ring_system has all seven ring slugs
  ok  M1: encke/halley present with empty {}
  ok  M1: inverted ring (inner >= outer) ABORTS
  ok  M1: malformed color string ABORTS
  ok  M1: malformed colors-list entry ABORTS
  ok  M1: a surviving features list (post-migration) ABORTS in derive_served
  ok  M2: earth serves a trust block
  ok  M2: earth trust method == two_body_rate_v1
  ok  M2: earth has a finite positive window_days
  ok  M2: jupiter serves a trust block
  ok  M2: jupiter trust method == two_body_rate_v1
  ok  M2: jupiter has a finite positive window_days
  ok  M2: saturn serves a trust block
  ok  M2: saturn trust method == two_body_rate_v1
  ok  M2: saturn has a finite positive window_days
  ok  M2: moon serves a trust block
  ok  M2: moon trust method == two_body_rate_v1
  ok  M2: moon has a finite positive window_days
  ok  M2: io serves a trust block
  ok  M2: io trust method == two_body_rate_v1
  ok  M2: io has a finite positive window_days
  ok  M2: titan serves a trust block
  ok  M2: titan trust method == two_body_rate_v1
  ok  M2: titan has a finite positive window_days
  ok  M2: pluto serves a trust block
  ok  M2: pluto trust method == two_body_rate_v1
  ok  M2: pluto has a finite positive window_days
  ok  M2: charon serves a trust block
  ok  M2: charon trust method == two_body_rate_v1
  ok  M2: charon has a finite positive window_days
  ok  M2: apophis serves a trust block
  ok  M2: apophis trust method == two_body_rate_v1
  ok  M2: apophis has a finite positive window_days
  ok  M2: voyager_1 serves a trust block
  ok  M2: voyager_1 trust method == fetched_positions
  ok  M2: voyager_1 trust window is null
  ok  M2: encke serves a trust block
  ok  M2: encke trust method == two_body_rate_v1
  ok  M2: encke has a finite positive window_days
  ok  M2: halley serves a trust block
  ok  M2: halley trust method == two_body_rate_v1
  ok  M2: halley has a finite positive window_days
  ok  M2: top-level served_window is non-null
  ok  M2: served_window brackets as_of (start < as_of < end)
  ok  M2: earth's window == its period cap (planet, cap=P)
  ok  M2: moon's window == P/8 (moon cap)
  ok  M2: halley's window == P/2 (comet cap)
[warn] jupiter: trust measurement failed (simulated check-vector outage); served null window
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[warn] served_window: null -- trust measurement missing/failed for ['jupiter'] (FLAG-3: null-on-any-failure is the conservative default)
[done] run 20260709T000000Z (first-build): 12 objects
  ok  M2: forced check-vector failure -> jupiter trust carries 'error'
  ok  M2: forced check-vector failure -> served_window null (FLAG-3, exercised)
[done] run 20260709T000000Z (nightly): 12 objects
  ok  nightly structural validation passes
  ok  nightly did not shrink earth
  ok  frozen past point unchanged byte-for-byte
  ok  guard: clean charon point -> no warning
  ok  guard: 35.7 AU point -> exactly one warning
  ok  guard: outer-bound trip tagged likely-contamination
  ok  guard KEPT the point (monitor, not reject)
  ok  guard: spacecraft |r|>200 AU -> sanity warning
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 12 objects
[RECOVER] restoring C:\Users\tonyq\AppData\Local\Temp\tmpog_iz718\data\solar-system from C:\Users\tonyq\AppData\Local\Temp\tmpog_iz718\data\solar-system.prev (crash mid-swap)
[done] run 20260709T000000Z (nightly): 12 objects
  ok  A-1/N1: nightly recovered the whole generation from .prev after a crash
  ok  A-1: archive not thinned by recovery (4106 >= 4106)
  ok  A-1: recovered nightly validates
[ABORT] fail: nightly run but no live raw archive (possible unrecovered crash) -- refusing to build a thin cache
  ok  A-1: nightly with no generation ABORTS instead of committing thin
  ok  A-2: main() exits nonzero on structural abort
  ok  A-2: main() exits 0 on pass
  ok  A-4: majorbody/id -> None
  ok  A-4: smallbody/None pass through unchanged
  ok  DP: straight line -> 2 endpoints
  ok  DP: keeps the bend
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 12 objects
[warn] titan: FETCH FAILED (simulated Horizons outage); served last-good orbit, as_of_today nulled
[done] run 20260709T000000Z (nightly): 12 objects
  ok  A-3: failed Titan still SERVED (not vanished)
  ok  A-3: Titan conic served from last-good
  ok  A-3: Titan as_of_today NULLED (no stale marker)
  ok  A-3: run validates with a stale object
  ok  N4/#B3: correct km conversion passes
  ok  N4/#B3: un-converted (AU-valued) served point ABORTS
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 12 objects
[ABORT] fail: N3 object(s) dropped from a served set: ['titan']
  ok  N3: dropping a served object (titan) ABORTS the publication
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 12 objects
[warn] encke: FETCH FAILED (solution-TP request_failed for encke); served last-good orbit, as_of_today nulled
[warn] halley: FETCH FAILED (solution-TP request_failed for halley); served last-good orbit, as_of_today nulled
[warn] served_window: null -- trust measurement missing/failed for ['encke', 'halley'] (FLAG-3: null-on-any-failure is the conservative default)
[done] run 20260709T000000Z (nightly): 12 objects
  ok  N5: solution-TP request failure serves last-good (not silent today-anchor)
[master (root-commit) 003988a] data: nightly 2026-07-10
 1 file changed, 1 insertion(+)
 create mode 100644 data/f.txt
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>

[commit] PUSH FAILED (Command '['git', '-C', 'C:\\Users\\tonyq\\AppData\\Local\\Temp\\tmpzv36lf3y', 'push']' returned non-zero exit status 128.) -- committed locally only; remote is STALE
  ok  N2: local commit succeeds but no-remote push is NOT reported as pushed
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 12 objects
[dry-run] validated; wrote nothing outside C:\Users\tonyq\AppData\Local\Temp\tmpjel8tggo\data\.staging_solar-system_20260709T000000Z
  ok  P2-2: --dry-run --object clears N3 + no-raw against an existing generation
[dry-run] validated; wrote nothing outside C:\Users\tonyq\AppData\Local\Temp\tmpghprojr2\data\.staging_solar-system_20260709T000000Z
  ok  P2-2: --dry-run --object works on a clean machine (no raw archive)
[warn] voyager_1: DP thin glide 2548 -> 2 points (tol=0.02 AU)
[done] run 20260703T000000Z (first-build): 12 objects
  ok  P2-1: spacecraft first-build passes #T (arc ends today, not a stale stride point)
  ok  P2-1: spacecraft as_of_today is fresh regardless of stride phase
  ok  #B3: correct per-component conversion passes
  ok  #B3: swapped axes (magnitude-preserving) ABORTS component-wise
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 12 objects
[warn] encke: FETCH FAILED (solution-TP request_failed for encke); served last-good orbit, as_of_today nulled
[warn] halley: FETCH FAILED (solution-TP request_failed for halley); served last-good orbit, as_of_today nulled
[warn] served_window: null -- trust measurement missing/failed for ['encke', 'halley'] (FLAG-3: null-on-any-failure is the conservative default)
[done] run 20260709T000000Z (nightly): 12 objects
  ok  P2-9: stale comet carries its comet block forward (not nulled)

PASS (134 checks, 0 failures)
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\tools>
```

**Claude:** Confirmed -- Layer 1 passes exactly as expected. `PASS (134
checks, 0 failures)` -- matches precisely: 87 pre-existing + 4 M1
shape-validator + 43 M2 checks, all green.

A few things worth pointing out so the noise doesn't cause second-guessing:

- The repeated `[warn] voyager_1: DP thin glide 2549 -> 2 points` is
  expected -- normal spacecraft thinning behavior on synthetic mock data,
  fires each time the suite builds, not a problem.
- `[warn] jupiter: trust measurement failed (simulated check-vector
  outage)` and the `served_window: null` warning right after it are the
  **intentional** forced-failure test (FLAG-3) -- that's supposed to
  happen, and the two `ok` lines right after confirm it worked correctly.
- The `[RECOVER]`, `[ABORT]`, and `PUSH FAILED` lines are all
  deliberately-simulated failure scenarios (crash mid-swap,
  no-remote-configured, dropped object) that other pre-existing tests are
  checking the *handling* of -- not real problems with the machine or git
  setup.
- All 12 M2 trust-block checks passed, plus the three FLAG-6 determinism
  checks (earth/moon/halley window == cap).

**Notes -- what Layer 1 proves for M2 (logic, statically reasoned):**
- `fetch_elements` captures Horizons' `n`; `n_deg_per_day` flows through
  `build_osculating_block` (including the A-3 history/fallback path, so a
  stale object's served conic still carries it) and, for a freshly-measured
  object, into `measure_trust`.
- The FLAG-2 wrapper (own `n`, not solar `K_GAUSS`) is wired correctly for
  every category -- directly confirmed deterministic (`window_days == cap`)
  for earth, moon, and halley (one per cap-divisor category); the other 8
  objects only get a "finite positive `window_days`" check, so their
  `== cap` holding too is a reasonable inference from shared construction
  (error rate is 0.0 for all 11 under the same mock), not something
  independently asserted per object.
- FLAG-3 (served_window null on any participant failure) fires through the
  real dispatch, not just in the abstract -- forced one object's
  check-vector fetch to fail and confirmed both the per-object `error` and
  the global null.
- FLAG-5/6 cap table and zero-rate handling.

**What Layer 1 cannot prove (Layer 2's job) -- all three settled by Step 1,
see "Known Layer-1-only assumptions" at the bottom of this doc:**
- Whether Horizons' mean-motion column is really named `n`/`N` for these
  object types, and whether it's present for every category in scope.
- Whether the `epochs=[jd1, jd2]` list-form query works for `.vectors()`
  the way it already does for `.elements()`.
- Whether the measured error rates are *physically* the shape the design
  expects.

---

## Layer 2 -- Live dry-run sequence (Tony's hardware)

Per manifest v2 sec 5.7. Five objects, one per category in scope (sec 5.7
names earth, moon, pluto, apophis, halley -- covering planet, moon,
dwarf_planet, asteroid, comet; jupiter/saturn/io/titan/charon/encke follow
the same pattern as their category-mate and are lower priority for the
first pass).

### Step 1 -- dry-run per representative object; eyeball physical plausibility

A dry-run validates and writes nothing outside `.staging` -- same pattern
as M1's Layer 2 step 1. After each, the staged `coverage_index.json`'s
`trust` block for that object is what to inspect.

**What "looks right" means here** -- this is physical, not just structural,
so eyeballing matters (per manifest sec 5.7 point 2, quoted directly:
*"planet rates tiny; Moon's rate visibly larger; comet rates largest"*):

- **earth**: two-body Kepler is an excellent approximation of Earth's real
  orbit over a 30-day bracket -- expect `error_rate_deg_per_day` very
  small, `cap_applied` likely equal to `window_days` (the ~365-day period
  cap binds, not the measured rate).
- **moon**: the Sun's perturbation on the Earth-Moon two-body ellipse is
  large -- expect a materially larger `error_rate_deg_per_day` than
  earth's, and plausibly `cap_applied: null` with `window_days` well under
  the P/8 cap.
- **pluto**: still a planet-cap object; expect small rate, similar
  character to earth (dwarf_planet uses the same P-divisor as planet).
- **apophis**: today-anchored, ordinary asteroid two-body behavior --
  expect planet-like smallness, not comet-like largeness.
- **halley**: measured at its Tp-anchor epoch (near perihelion) -- expect
  the largest rate of the five, plausibly `cap_applied: null` here too.

If any of these come back inverted (e.g. earth's rate larger than
halley's) that's a real bug to chase before going further, not a rounding
concern.

**`python tools/gallery_cache_builder.py --dry-run --object earth`**

Clean pass, and it answers both open questions from Layer 1. `n_deg_per_day:
0.9851...` is present -- Horizons' mean-motion column really is named `n`
for a real planet query. Two real samples came back (`offset_days: -30` and
`+30`), each with a real `error_deg` -- the `epochs=[jd1, jd2]` list-form
query works for `.vectors()` against the live API. The physics matched
prediction exactly: `error_rate_deg_per_day` tiny (0.000277), `cap_applied`
(365.43) equals `window_days` (365.43) -- the ~365-day period cap binds,
not the measured rate (the rate alone would've earned Earth a ~904-day
window). The -30/+30 errors aren't symmetric (0.0020 deg vs 0.0083 deg) --
normal, real Horizons includes actual planetary perturbations a pure
two-body propagation won't drift identically for. The top-level
`served_window` in this file is Earth's window alone (single-object dry
run); the real multi-object answer comes in Step 2.

**`python tools/gallery_cache_builder.py --dry-run --object moon`**

Moon's numbers landed where the physics says they should, though not quite
in the way predicted -- a good illustration of the cap logic doing its job.
`error_rate_deg_per_day: 0.0331` vs Earth's 0.000277 -- about 120x larger,
matching the prediction that the Sun's perturbation on the Earth-Moon
two-body ellipse dominates. `n_deg_per_day: 13.39` implies a period of
360/13.39 ~= 26.9 days -- close to the real 27.3-day sidereal month (the
gap is just today's instantaneous osculating fit). But the cap bound, not
the rate -- opposite of the prediction. The tolerance math alone would
allow a ~7.55-day window before Moon's real trajectory drifts 0.5 deg from
the two-body prediction; but moon's structural cap (P/8 ~= 3.36 days) is
tighter, so the cap wins. `window_days`, `cap_applied`, and `delta_days`
all show the same number (3.3607...) because `delta_days` and moon's cap
divisor both happen to be period/8 for this category -- two independent
formulas sharing a divisor, not a glitch. `served_window: null` at the top
is also expected: moon is one of the two categories (`moon`, `spacecraft`)
excluded from the global `served_window` entirely, and this single-object
run had zero eligible participants.

**`python tools/gallery_cache_builder.py --dry-run --object pluto`**

Pluto's numbers are internally correct, but they weren't measuring what
was assumed, and this is where the real bug surfaced. `a_au: 1.424e-05` is
not Pluto's real ~39.5 AU distance from the Sun -- that's ~2,130 km,
Pluto's wobble radius around the Pluto-Charon barycenter. `"center":
"pluto_barycenter"`, `"canonical_frame": "barycenter-relative"` confirm it
-- an already-settled serving choice from the Pluto/Charon design work, not
new to M2, but it meant the trust check measured the mutual Pluto-Charon
orbit, not Pluto's solar orbit. The number checks out as real physics: 360
/ 56.39 deg/day = 6.384 days -- essentially the textbook Pluto-Charon
mutual period (~6.39 days). The problem is one level up: `dwarf_planet`
wasn't in the excluded-participant set (`{'moon', 'spacecraft'}`) -- only
category label was checked, not serving frame. Charon does the identical
motion and was excluded, but only because its category label happens to be
`moon`. Since `resolver.py`'s `resolve()` gates the entire scene against
one global `served_window` before even looking at which objects are in
scene, Pluto's ~6.4-day window controlling the site-wide minimum would mean
a request for something as ordinary as "Jupiter, 10 days from now" gets
wrongly rejected.

Three options were raised: (1) reframe the exclusion rule around serving
frame (`canonical_frame`) rather than category label -- generalizes and
matches the pattern already used for Charon; (2) leave it as-is, accept a
~week-wide site-wide date range; (3) change how the resolver consumes
`served_window` (per-object bound instead of one global minimum) -- bigger
change, outside M2's declared scope.

**Tony:** Yes, #1.

**`python tools/gallery_cache_builder.py --dry-run --object apophis`**

Clean, no surprises -- exactly the "boring in a good way" result expected.
`n_deg_per_day: 1.1127` -> period ~323.5 days, matching Apophis's actual
~323.6-day orbital period. `error_rate_deg_per_day: 3.7e-06` -- even
cleaner than Earth's, since this is Apophis on an ordinary day, far from
any close encounter. Cap binds at the full period (`window_days ==
cap_applied == 323.5`), same shape as Earth. One thing checked rather than
shrugged off: the top-level `served_window` start doesn't exactly match
Apophis's own `trust.window` start (~0.624-day gap, vs ~0.058 days on
Earth's run -- different size each time). Traced to the code: the
per-object window anchors to `element_epoch_jd` (midnight UTC, fixed for
the day), but the global `served_window` centers on `as_of_jd` = actual
wall-clock time when the build runs. Checks out numerically both times
(Apophis ran at 14:59:08 UTC, ~0.624 of a day past midnight; Earth ran at
01:24:06 UTC, ~0.058 of a day past midnight) -- two different reference
points doing two different jobs correctly, not a bug.

**`python tools/gallery_cache_builder.py --dry-run --object halley`**

Completes the five, but the number didn't match the prediction, worth
owning rather than talking around. `error_rate_deg_per_day: 6.4e-06` --
smaller than Earth's, far smaller than Moon's or Pluto's, barely bigger
than Apophis's. The prediction ("near perihelion = fast = should diverge
fastest") was wrong, or at least incomplete. `delta_days` is capped at a
flat 30 days that doesn't scale with period: for Moon and Pluto,
period/8 is well under 30, so the check window scales down with the
object; for Earth, Apophis, and Halley, period/8 exceeds 30, so all three
get clamped to the same flat 30-day window. For Halley (period ~27,761
days, ~76 years -- matches the real value closely), 30 days is ~0.1% of
the orbit -- a genuinely tiny slice even centered at the fastest point.
Perturbation away from the tangent two-body ellipse builds up with elapsed
time from the anchor epoch, so a tiny window just hasn't had much chance to
show it yet -- a real property of a flat time cap on a wildly different
timescale, not a bug. And it turns out not to matter anyway: same as Earth
and Apophis, the category structural cap wins (comet P/2 = 13,880.67,
clamping a rate-implied ~39,000-day window). What mattered more, and landed
clean: this is the first real, live-Horizons confirmation that the
Tp-anchor fix works end to end -- `epoch_jd: 2446469.97` (1986, not today),
samples at `offset_days: -30.0 / +30.0` from that epoch, not from "now."

**Step 1 outcome:** five for five. Mean-motion column resolves correctly on
live queries, list-form epoch vectors work, the comet Tp-anchor fix holds
against real data, every rate/cap relationship matched known physics except
the Halley delta_days surprise (explained, not a bug) -- and Pluto's run
surfaced a real bug (L-149), now fixed per Tony's decision.

### Step 2 -- real --first-build; inspect the swapped coverage_index

**Confirm (corrected -- see note below):**
- `served_window` is populated (non-null) -- or, if null, that the warning
  names exactly the objects whose measurement failed, not a silent
  swallow.
- 11 measured `trust` blocks (`method: "two_body_rate_v1"`) + voyager_1's
  `method: "fetched_positions"`. Unchanged, every object still gets
  measured individually.
- **Global `served_window` controller must be one of exactly 6:** earth,
  jupiter, saturn, apophis, halley, encke (the heliocentric-frame
  objects). Moon/Io/Titan (parent-relative) and Pluto/Charon
  (barycenter-relative) must show a `trust` block but take no part in the
  global minimum. If Pluto or Charon shows up as controller, that's a real
  regression, not a "worth a second look."

Note: this checklist originally named Pluto as a plausible controller,
written before the L-149 fix. That version is stale and has been replaced
above -- once the fix landed, Pluto is structurally excluded from voting
and cannot be the controller.

**tony:**
```
python tools/gallery_cache_builder.py --first-build
```
Terminal tail:
```
[RECOVER] could not remove retained data\solar-system.prev ([WinError 5] Access is denied: 'data\\solar-system.prev\\raw\\elements'); swap will quarantine it
[SWAP] stale data\solar-system.prev (suspected file lock) -> quarantining as data\solar-system.quarantine_20260721T200207Z
[warn] voyager_1: DP thin glide 2551 -> 29 points (tol=0.02 AU)
[done] run 20260721T200207Z (first-build): 12 objects

gallery head is at c5c9ea093233f1a8fe37483301c0d427460e95ac
orrery head is at 3417753c1d0b23635b96dc9de37b1d6f0b1e2ee4
```
Plus the run manifest, `feature_configs.json`, `coverage_index.json`,
`voyager_1.json`, and `pluto.jsonl` from that run, uploaded for review.

**Claude:** PASS. Full evidence below.

**Run manifest (`20260721T200207Z.json`):**
```json
{
  "run_id": "20260721T200207Z",
  "started": "2026-07-21T20:02:07.902467+00:00",
  "mode": "first-build",
  "objects": {
    "earth": "backfilled(366)", "jupiter": "backfilled(366)",
    "saturn": "backfilled(366)", "moon": "backfilled(366)",
    "io": "backfilled(366)", "titan": "backfilled(366)",
    "pluto": "backfilled(366)", "charon": "backfilled(366)",
    "apophis": "backfilled(366)", "voyager_1": "backfilled(105)",
    "encke": "backfilled(366)", "halley": "backfilled(366)"
  },
  "guard_warnings": [],
  "structural_validation": "pass",
  "committed": false,
  "finished": "2026-07-21T20:02:31.352115+00:00"
}
```

**`served_window`:** `{start_jd: 2460919.788243763, end_jd: 2461566.8819219014}`
-- half-width = 323.5468390692 days, matching Apophis's `window_days`
(323.54683906902784) to 10 decimal places. **Controller = Apophis, not
Pluto.** Pluto (~6.38d) and Charon (~0.80d) both got fully measured but
took no part in the global bound -- the fix working exactly as designed on
live data, not just the mock.

**All 12 trust blocks, spot-checked against real orbital physics
(period = 360 / n_deg_per_day):**

| object    | frame               | method              | window_days     | period check |
|-----------|---------------------|----------------------|------------------|---------------|
| earth     | heliocentric        | two_body_rate_v1    | 365.33 (=cap)    | 365.33d, matches ~365.25d real |
| jupiter   | heliocentric        | two_body_rate_v1    | 4331.38 (=cap)   | 11.86 yr, matches real |
| saturn    | heliocentric        | two_body_rate_v1    | 10764.60 (=cap)  | 29.47 yr, matches real |
| moon      | parent-relative     | two_body_rate_v1    | 3.35 (=cap, P/8) | 26.83d, close to real 27.3d sidereal |
| io        | parent-relative     | two_body_rate_v1    | 0.221 (=cap, P/8)| 1.77d, matches real |
| titan     | parent-relative     | two_body_rate_v1    | 1.99 (=cap, P/8) | 15.95d, matches real |
| pluto     | barycenter-relative | two_body_rate_v1    | 6.38 (=cap)      | 6.38d mutual period, matches real |
| charon    | barycenter-relative | two_body_rate_v1    | 0.798 (=cap, P/8)| same mutual period, moon-category cap |
| **apophis** | **heliocentric**  | two_body_rate_v1    | **323.55 (=cap, CONTROLLER)** | 323.55d, matches real |
| voyager_1 | arc-natural         | fetched_positions    | null             | n/a |
| encke     | heliocentric        | two_body_rate_v1    | 603.52 (=cap, P/2, Tp-anchored) | 1207.04d full period |
| halley    | heliocentric        | two_body_rate_v1    | 13880.67 (=cap, P/2, Tp-anchored) | 76.03 yr, matches real |

Nothing inverted, nothing physically implausible.

**`feature_configs.json`** is no longer the empty stub -- earth
(`atmosphere_shell` + `van_allen_belts`), jupiter (`ring_system` + 4-ring
`radiation_belts`), saturn (7-ring `ring_system`) are all populated with
real ported values; the other 9 objects correctly serve `{}`. This is
L-118's problem, not L-149's, but it's resolved in the same push -- worth
knowing next time that item comes up.

**Two things that look odd but are expected:**

- `"committed": false` in the run manifest is not a problem.
  `--first-build` alone doesn't auto-push -- the script only commits+pushes
  with `--commit`, which wasn't passed. The swap happened locally; Tony
  pushed manually via GitHub Desktop about 4 minutes later (commit
  "interactive first build," author Tony Quintanilla, 20:06:44 UTC --
  confirmed via the GitHub API). Fetching the pushed `coverage_index.json`
  from the new HEAD matched the upload byte-for-byte on `served_window`
  and `generated`, confirming this build's data is genuinely live, not
  just staged.
- The `[RECOVER]`/quarantine warning is expected and self-healing.
  Something (likely OneDrive, since the whole project tree lives under
  OneDrive Desktop) held a lock on the old `data\solar-system.prev`
  folder, so the builder quarantined it instead of failing the run. The
  quarantined folder is auto-swept after a few days; nothing to do.

**Voyager point-count discrepancy, resolved:** the run manifest says
`backfilled(105)`, the served positions file says `n_points: 113`. Traced
in the code (`run_build`, ~lines 760-815): `backfilled(N)` only counts
points fetched *this run* (thinned glide + flyby dense windows + fresh
daily tail = the `new` dict). The final served file is `points.update(new)`
against whatever was already archived -- the extra 8 are older archived
points this run didn't need to re-touch. Both numbers are correct; they're
measuring different things, not disagreeing.

### Step 3 -- one real --nightly

**tony:**
```
python tools/gallery_cache_builder.py --nightly
```
Terminal output:
```
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --nightly
[RECOVER] could not remove retained data\solar-system.prev ([WinError 5] Access is denied: 'data\\solar-system.prev\\raw\\elements'); swap will quarantine it
[SWAP] stale data\solar-system.prev (suspected file lock) -> quarantining as data\solar-system.quarantine_20260721T211338Z
[done] run 20260721T211338Z (nightly): 12 objects

gallery head at af3a2c8611293bc865b62c23f61334a2c2941e45
```

**Claude:** Clean pass, no regressions. `served_window` refreshed
correctly to `{start_jd: 2460919.837711381, end_jd: 2461566.931389519}`
(generated 2026-07-21T21:13:45 UTC) -- re-centered on the new build time
(start/end both shifted ~71 minutes forward, matching the real gap between
the 20:02 and 21:13 UTC runs), while the half-width stayed pinned to
Apophis's `window_days` (323.5468d), unchanged from Step 2. Every other
object's `window_days` also matched Step 2 bit-for-bit -- expected, not
stale: element epochs are anchored to midnight UTC of the calendar day, and
this nightly ran within the same UTC day as the first-build, so Horizons
legitimately returns identical elements for both queries. Apophis still
controls; Pluto/Charon still correctly excluded. All 12 objects present, no
`[ABORT]`, no fetch-failure warnings.

Same `[RECOVER]`/quarantine pattern as Step 2, second time in a row -- same
benign, self-healing story, most likely OneDrive holding a brief lock on
`.prev` right after the previous run touched it (the two runs were only
~71 minutes apart). Not blocking anything; safe to leave the quarantine
folders for the automatic sweep, or delete by hand if desired -- `.prev`
itself should be left alone (it's the intentional one-generation rollback).

**This is the nightly-refresh proof both L-118 and L-149 were waiting on.
Both are closed as of this run** (ledger updated separately).

### Step 4 -- resolver behavior via the dev render page date picker

Per manifest sec 5.7 point 4 (PHASE2_ARTIFACT1_AS_BUILT.md SS7): a date
inside `served_window` renders; a date far outside raises
`OutOfServedWindowError`. This exercises the EXISTING resolver/cache_reader
consumer against the newly populated field -- zero resolver code changes,
so this step is really confirming M2 wired the field resolver already
knows how to read, not testing new resolver logic. It also happens to
reuse the same Earth dev harness that closed Artifact 1 -- that's fine and
expected, not a re-litigation of Earth's Mode 5 acceptance.

**How to run it:**
1. In VS Code (with the tonyquintanilla.github.io folder open), open a
   terminal: Terminal > New Terminal (or Ctrl+`). Starts already in the
   repo root.
2. Type `python -m http.server 8000` and press Enter. Serves the repo's
   own files to a browser at localhost:8000; modifies nothing. Leave it
   running; Ctrl+C or closing the terminal stops it.
3. In a browser, go to
   `http://localhost:8000/gallery/solar_system_earth_test2.html` -- note
   the "2". The page's own header comment still says to open
   `solar_system_earth_test.html` (no "2"); that's a leftover from before
   the date picker was added and should be fixed (see Housekeeping below).
   Only `test2.html` has the date box wired to the resolver.
4. Set the date box to a date inside `served_window` (roughly Sep 2025 --
   Jun 2027 as of this build; it shifts slightly every run) and click
   "Render Earth." Expect a normal plot and a green "Rendered. This is the
   Mode 5 gate..." log line.
5. Set the date box to something clearly outside that range (e.g.
   2020-01-01 or 2030-01-01) and click "Render Earth" again. Expect a red
   "ERROR: OutOfServedWindowError..." log line instead of a plot -- that
   red error IS the pass condition.

**tony:** page log
```
Loading Pyodide runtime (from CDN)...
Pyodide ready.
Fetching assembler package (14 files)...
Assembler written to Pyodide FS.
Fetching served cache (../data/) ...
Served cache loaded.
Running assemble_scene(earth, 2026-07-13T00:00:00Z) in the browser...
Assembly complete: 5 traces.
Rendered. This is the Mode 5 gate - your eyes decide.
Running assemble_scene(earth, 2020-07-13T00:00:00Z) in the browser...
ERROR: Traceback (most recent call last):
  File "/lib/python314.zip/_pyodide/_base.py", line 597, in eval_code_async
    await CodeRunner(
    ...<9 lines>...
    .run_async(globals, locals)
  File "/lib/python314.zip/_pyodide/_base.py", line 411, in run_async
    coroutine = eval(self.code, globals, locals)
  File "<exec>", line 18, in <module>
  File "/home/pyodide/assembler/assemble.py", line 37, in assemble_scene
    ctx = resolve(scene_spec, catalog, cache)
  File "/home/pyodide/assembler/resolver.py", line 103, in resolve
    raise OutOfServedWindowError(
    ...<2 lines>...
    )
assembler.errors.OutOfServedWindowError: Requested epoch (JD 2459043.5000) is outside the served_window [2460919.8377, 2461566.9314].
If this is a fetch/CORS error, serve over http (python -m http.server) rather than opening the file directly.
```
Local server terminal (excerpt):
```
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
::1 - - [21/Jul/2026 22:29:39] "GET / HTTP/1.1" 200 -
::1 - - [21/Jul/2026 22:29:54] "GET /gallery/solar_system_earth_test2.html HTTP/1.1" 304 -
::1 - - [21/Jul/2026 22:31:13] "GET /gallery/assembler/__init__.py HTTP/1.1" 304 -
  [... 13 more assembler files, all 200/304 ...]
::1 - - [21/Jul/2026 22:31:13] "GET /data/solar-system/coverage_index.json HTTP/1.1" 200 -
::1 - - [21/Jul/2026 22:31:13] "GET /data/objects_config.json HTTP/1.1" 200 -
```

**Claude:** PASS on both halves.
- Inside the window (2026-07-13): rendered normally, 5 traces, green
  "Mode 5 gate" message.
- Outside the window (2020-07-13): correctly refused --
  `OutOfServedWindowError: Requested epoch (JD 2459043.5000) is outside
  the served_window [2460919.8377, 2461566.9314]`.

The trailing "If this is a fetch/CORS error..." line always prints after
*any* caught error in the page's `catch` block, generic boilerplate, not a
sign of an actual CORS problem -- the successful first render already
proved fetch/CORS was fine. The `served_window` bounds in the error --
`[2460919.8377, 2461566.9314]` -- match exactly what was pulled from the
pushed `coverage_index.json` after the nightly run, confirming the dev page
is reading the real, current served cache. The server log shows only
200s/304s, no errors, and the assembler files + served cache were fetched
once (22:31:13) and reused across both date clicks -- the page caches the
Pyodide runtime after the first click, no re-fetch needed on rerender.

### Step 5 -- fetch-cost / throttling note

Each non-spacecraft object costs one additional `fetch_vectors_range` call
per build (both check epochs via the new `epoch_jds` list mode, one call)
-- projected +11 Horizons calls per nightly run.

**Observed:** `--first-build` ~23 seconds for all 12 objects (includes
Voyager's larger historical backfill); `--nightly` ~7 seconds. No throttle
warnings in either console output.

**Tony:** No delays observed.

**Claude:** Logged as the Step 5 note. Two data points isn't enough to
claim Horizons "never" slows down -- that's better confirmed by watching a
few real nightlies over the coming days than by manufacturing a test for
it now. If it ever does bite, the manifest already names the sanctioned
optimization (batch further -- unlikely needed at 11 objects).

---

## Layer 3 -- Schedule

**CLOSED, 2026-07-22.** Task Scheduler job "Paloma's Orrery Nightly Build"
created (account `tonyq`, daily trigger 12:00 PM, action = python.exe +
`tools/gallery_cache_builder.py --nightly --commit`, start-in = repo root).
"Run whether user is logged on or not" selected; real Windows account
password entered and accepted ("log on as batch job" granted -- the 4-digit
PIN cannot be used for this option, confirmed separately).

Two real tests, not just a saved config:

1. **Manual `--commit` test** (before the scheduled task existed) -- proved
   the script's own git add/commit/push sequence works on this machine with
   no separate PAT or credential setup: GitHub Desktop's credential helper
   is already shared with plain command-line git. Commit `ae8ab13`, verified
   live.
2. **Task Scheduler manual "Run"** -- fired twice by accident (a manual
   trigger gives no visible feedback, which is normal, not a failure sign --
   that's what caused the second click). Verified this was two genuinely
   separate, complete script executions 5 seconds apart (`d59e2b6`,
   `7971096`), not one confused run. Checked precisely: Run 1 finished (own
   commit landed) about 3 seconds before Run 2 started -- no real overlap,
   though this was fortunate timing, not a guarantee. Confirmed both runs'
   data independently: no corruption, served_window still correctly
   controlled by Apophis, all 12 objects consistent, Voyager's position
   count grew by exactly one day as expected. Concurrency policy ("Do not
   start a new instance") confirmed set, protecting future accidental
   double-clicks from a real overlap going forward.

A stale "Running" status lingered in the Task Scheduler list after both test
runs had long finished -- confirmed benign (gallery HEAD unchanged for 20+
minutes, consistent with nothing actually executing) and resolved by
Refresh (F5), a known display quirk in the Task Scheduler snap-in, not a
real hang.

Minor, non-blocking finding along the way: the run manifest committed to git
history reads `"committed": false` even on runs that pushed successfully --
a write-order quirk (the manifest is corrected to the true status only
*after* `git commit` already captured the old value, so the fix never makes
it into that same commit). Doesn't affect anything real; worth a small
future patch, not urgent.

**Claude:**
Totally normal answer for someone who's never needed to know — let's just test it directly rather than guess. Let me check the exact success/failure messages to watch for first.Let's just test it directly — one real run tells us more than any amount of guessing about Windows Credential Manager. Low-risk either way: the data swap happens *before* the git step, so even total git failure won't lose or corrupt anything — worst case you just push manually via GitHub Desktop like every other time tonight.

**Run this:**
```
python tools/gallery_cache_builder.py --nightly --commit
```

**What to expect:**

- **Success looks like silence** on the git front, which is a little counterintuitive — the code only prints something when the commit/push *fails*. If you just see the normal `[done] run ... (nightly): 12 objects` line and nothing starting with `[commit]`, that's actually the good outcome.
- **If git itself isn't findable**, you might see a raw Python error (`FileNotFoundError` or similar) instead of a clean message — that's fine, just means `git.exe` isn't on your system PATH (very possible if GitHub Desktop is the only git you've ever installed). Not scary, just informative.
- **If git is found but push fails**, you'll see a line starting with `[commit] PUSH FAILED (...)`.

Paste whatever you get back to me either way — I'll check the actual gallery repo directly afterward. If it worked, I'll see a new commit titled "data: nightly [today's date]" authored without any GitHub Desktop involvement, which is the real proof the unattended path works. If it didn't, we'll know exactly what needs fixing before Task Scheduler is worth setting up.


C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>python tools/gallery_cache_builder.py --nightly --commit
[RECOVER] could not remove retained data\solar-system.prev ([WinError 5] Access is denied: 'data\\solar-system.prev\\raw\\elements'); swap will quarantine it
[SWAP] stale data\solar-system.prev (suspected file lock) -> quarantining as data\solar-system.quarantine_20260722T045938Z
warning: in the working copy of 'data/solar-system/coverage_index.json', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/feature_configs.json', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/apophis.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/charon.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/earth.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/encke.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/halley.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/io.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/jupiter.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/moon.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/pluto.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/saturn.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/elements/titan.jsonl', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/runs/20260711T214714Z.json', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/runs/20260711T232647Z.json', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/runs/20260721T200207Z.json', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/runs/20260721T211338Z.json', CRLF will be replaced by LF the next time Git touches it
warning: in the working copy of 'data/solar-system/raw/runs/20260722T045938Z.json', CRLF will be replaced by LF the next time Git touches it
[main ae8ab13] data: nightly 2026-07-22
 26 files changed, 279 insertions(+), 245 deletions(-)
 create mode 100644 data/solar-system/raw/runs/20260722T045938Z.json
Enumerating objects: 67, done.
Counting objects: 100% (67/67), done.
Delta compression using up to 12 threads
Compressing objects: 100% (34/34), done.
Writing objects: 100% (35/35), 12.26 KiB | 1.02 MiB/s, done.
Total 35 (delta 27), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (27/27), completed with 27 local objects.
To https://github.com/tonylquintanilla/tonyquintanilla.github.io.git
   af3a2c8..ae8ab13  main -> main
[done] run 20260722T045938Z (nightly): 12 objects

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

That's a full, clean pass — confirmed live, `ae8ab133de0e8c4132bdc118aa106851251dbf46` matches your terminal exactly.

**It just works.** `git.exe` is on PATH, and whatever credential helper GitHub Desktop set up is shared with plain command-line git — no PAT setup needed, no separate configuration. The commit message ("data: nightly 2026-07-22") and the push both came straight from the script, unattended, in under 10 seconds. This closes the one real unknown standing between here and Task Scheduler.

Two small, genuinely non-blocking notes from that output:
- The CRLF warnings are just git noting it'll normalize line endings on these files going forward — harmless, standard on Windows repos, not something this run caused or something to fix.
- Same `[RECOVER]`/quarantine pattern as the last two runs, third time now — still the same benign, self-healing story (likely OneDrive), still nothing to do.

## Now the actual Task Scheduler setup

1
Open Task Scheduler
Click the Windows Start button, type 'Task Scheduler', and open it. It's a built-in Windows tool, no install needed.
2
Create a new task
In the right-hand panel, click 'Create Task...' (not 'Create Basic Task' -- the full version gives you the 'start in' folder option you need). Give it a name like 'Paloma's Orrery Nightly Build'.
3
Set the trigger (when it runs)
Go to the 'Triggers' tab, click 'New...', set it to 'Daily', pick a time (late night/early morning works well, when you're not actively working in that folder -- avoids the OneDrive file-lock issue showing up mid-edit). Click OK.
4
Set the action (what it runs)
Go to the 'Actions' tab, click 'New...'. For 'Program/script', enter the full path to your python.exe (the same one from your terminal prompts: C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe). For 'Add arguments', enter: tools/gallery_cache_builder.py --nightly --commit. For 'Start in', enter the repo root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io -- this 'start in' field is exactly the working-directory requirement the testing protocol calls for. Click OK.
5
Check the General tab settings
Back on the 'General' tab: consider checking 'Run whether user is logged on or not' if you want it to fire even when you're not signed in -- but that may prompt for your Windows password to save the task, and needs you to be signed in at least once after each reboot for saved credentials to work. 'Run only when user is logged on' is simpler and more reliable if your machine is usually on and you're usually logged in overnight.
6
Save and do one test run
Click OK to save (enter your Windows password if prompted). Then right-click the new task in the list and choose 'Run' to fire it immediately as a test, rather than waiting for tonight. Check the 'Last Run Result' column -- 0x0 means success. You can also just check the gallery repo on GitHub afterward for a fresh 'data: nightly' commit.
7
Watch the first few unattended runs
This is the testing protocol's own instruction, not optional: watch the first few nights play out before trusting it fully. A nonzero exit code shows up right in Task Scheduler's history for that task, so a bad night is visible without you needing to go looking through logs.


Once you've got this saved and done a test run, that's Layer 3 closed — the full M2 testing protocol done end to end, from the offline suite tonight all the way to genuinely unattended nightly builds.

---

## Known Layer-1-only assumptions -- all settled by Step 1

1. `Horizons(..., epochs=[jd1, jd2])` for `.vectors()` -- **SETTLED.**
   Confirmed working against the live API on every Step 1 dry-run (real
   `-30`/`+30` day samples came back for earth, moon, pluto, apophis, and
   halley alike).
2. Mean-motion column name (`n` vs `N`) and presence, per object category
   -- **SETTLED.** `n` resolved correctly on every live query across all
   five Step 1 objects and all 12 objects in Step 2/3.
3. Pluto's real semi-major axis producing a very different window than the
   Layer-1 mock's placeholder -- **SETTLED, and more consequential than
   expected.** The real number wasn't just "different as expected" -- it
   revealed that Pluto's served orbit is barycenter-relative, which is
   what surfaced the L-149 participant-exclusion bug in the first place.
   Fixed per Tony's decision in Step 1; proven on live data in Steps 2-3.

---

## Housekeeping (not blocking, not forgotten)

- `gallery/solar_system_earth_test2.html`'s header comment still points to
  `solar_system_earth_test.html` (no "2") as the URL to open. Cosmetic --
  worth a one-line fix to the comment so a future session isn't sent to
  the wrong file.
**Tony:** Done.

- This addendum's Layer 1 evidence block above is Tony's original 134-check
  run, kept verbatim as the historical record; the current 138-check state
  is Claude's sandbox verification, clearly labeled as such above it. If a
  fresh Tony-run of the offline suite happens on Windows at some point,
  worth pasting that in to replace the sandbox-verification note with a
  first-party one.
