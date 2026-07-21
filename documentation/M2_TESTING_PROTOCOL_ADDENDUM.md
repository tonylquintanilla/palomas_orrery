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

**Claude**:
**Confirmed — Layer 1 passes exactly as expected.**

`PASS (134 checks, 0 failures)` — matches precisely: 87 pre-existing + 4 M1 shape-validator + 43 M2 checks, all green.

A few things worth pointing out so you're not second-guessing any of the noise in there:

- The repeated `[warn] voyager_1: DP thin glide 2549 -> 2 points` is expected — normal spacecraft thinning behavior, fires each time the suite builds, not a problem.
- `[warn] jupiter: trust measurement failed (simulated check-vector outage)` and the `served_window: null` warning right after it are the **intentional** forced-failure test (FLAG-3) — that's supposed to happen, and the two `ok` lines right after confirm it worked correctly.
- The `[RECOVER]`, `[ABORT]`, and `PUSH FAILED` lines are all deliberately-simulated failure scenarios (crash mid-swap, no-remote-configured, dropped object) that other pre-existing tests are checking the *handling* of — not real problems with your machine or git setup.
- All 12 M2 trust-block checks passed, plus the three FLAG-6 determinism checks (earth/moon/halley window == cap).

This is a clean, complete match to what I verified independently in my own sandbox all session. Nothing here needs a second look.

**Ready for step 2** whenever — the five dry-runs (earth, moon, pluto, apophis, halley). Same as before: run them, paste me the `trust` block from each staged `coverage_index.json`, and I'll check the shape.

**Notes:**
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

**Claude:**
 Two issues, one real and one just a precision nit. Went back through the actual code behavior and the test output to check each claim rather than taking the addendum's own wording at face value.

**Real issue — bullet 1 overclaims the A-3 path:**

> "`n_deg_per_day` flows through `build_osculating_block`, the A-3 history/fallback path, and into `measure_trust`."

This isn't quite what the code does. For a stale object (A-3, `serve_last_good`), `measure_trust` is never called at all — it gets a hardcoded null trust block instead (`"error": "stale generation (last-good elements served; trust not re-measured this run)"`). That was a deliberate call in the M2 build: re-attempting a check-vector fetch during an outage that already triggered A-3 seemed unlikely to succeed, so it doesn't try.

What *is* true: `n_deg_per_day` does flow through the A-3 path as far as the served `osc_block` (via `last_good_elements`/`build_osculating_block` — that's real and needed for a stale object's conic to render at all). It just stops there — it never reaches `measure_trust` for a stale object. The wording bundles those into one chain when they're actually two separate, disconnected facts. Should read something like:

> "`n_deg_per_day` flows through `build_osculating_block` (including the A-3 history/fallback path, so a stale object's served conic still carries it) and, for a freshly-measured object, into `measure_trust`."

**Minor — bullet 2 slightly overstates directness:**

> "confirmed deterministic (`window_days == cap`) for all 11 non-spacecraft objects"

Checking the actual test output: only 3 of the 11 get a direct equality assertion — earth (planet/dwarf_planet/asteroid divisor), moon (moon divisor), halley (comet divisor), one per cap category. The other 8 (jupiter, saturn, pluto, charon, io, titan, apophis, encke) only get the generic "finite positive `window_days`" check — not a direct `== cap` assertion each. Since error rate is 0.0 by construction for all 11 under the same mock, `window_days == cap` almost certainly holds for all of them too — but that's an inference from shared construction, not something independently tested per object. Small thing, but worth not blurring "confirmed" and "reasonably inferred."

Everything else — the FLAG-3 bullet, and the whole "what Layer 1 cannot prove" section — checks out exactly as written, no changes needed there. 

## Layer 2 -- Live dry-run sequence (Tony's hardware)

Per manifest v2 sec 5.7. Five objects, one per category in scope (sec 5.7
names earth, moon, pluto, apophis, halley -- covering planet, moon,
dwarf_planet, asteroid, comet; jupiter/saturn/io/titan/charon/encke follow
the same pattern as their category-mate and are lower priority for the
first pass).

### Step 1 -- dry-run per representative object; eyeball physical plausibility

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

```
python tools/gallery_cache_builder.py --dry-run --object earth

**Claude:**:
This is a clean pass — and it actually answers both of the open questions Layer 1 flagged as unknowable until real Horizons was involved.
What it confirms:

n_deg_per_day: 0.9851... is present and populated — Horizons' mean-motion column really is named n (or your fallback list found it), for a real planet query. Open question #1, settled.
Two real samples came back (offset_days: -30 and +30), each with a real error_deg — the epochs=[jd1, jd2] list-form query works for .vectors() against the live API, same as it already did for .elements(). Open question #2, settled.
The physics is exactly what the addendum predicted: error_rate_deg_per_day is tiny (0.000277 — two-body is a near-perfect stand-in for Earth's real orbit at this timescale), and cap_applied (365.43) equals window_days (365.43) — the ~365-day period cap is what's binding here, not the measured rate. If you work the math backward, the measured rate alone would've earned Earth a ~904-day window — the cap pulled it down to the period. That's the exact "cap binds, not the rate" case the addendum called out as the expected earth behavior.

Two small things worth understanding, not worrying about:

The -30/+30 errors aren't symmetric (0.0020° vs 0.0083°) — that's normal. Real Horizons includes actual perturbations from the other planets; a pure two-body propagation won't drift identically in both time directions. The code takes the worse of the two on purpose, which is what happened.
The top-level served_window in this file (the one at the very top of the JSON) is Earth's window alone, since this run only touched one object — it's not the real multi-object answer. That comes in Step 2, and it'll almost certainly be tighter than this, set by whichever comet or fast-mover has the smallest window, not by Earth.

python tools/gallery_cache_builder.py --dry-run --object moon

**Claude:**
Moon's numbers came back exactly where the physics says they should, though not quite in the specific way the addendum guessed — worth walking through, since it's a good illustration of the cap logic actually doing its job.
The rate itself: right direction, right rough size. error_rate_deg_per_day: 0.0331 vs Earth's 0.000277 — about 120x larger, matching the prediction that the Sun's perturbation on the Earth-Moon two-body ellipse would dominate the way other-planet perturbations don't for Earth. And as a sanity check: n_deg_per_day: 13.39 implies a period of 360/13.39 ≈ 26.9 days — close to the real 27.3-day sidereal month (the gap is just today's instantaneous osculating fit, not an error).
But the cap bound, not the rate — opposite of what the addendum guessed, and that's fine. The addendum expected cap_applied: null (rate binds). What actually happened: the tolerance math alone would allow a ~7.55-day window before Moon's real trajectory drifts 0.5° from the two-body prediction — genuinely decent for a two-body approximation. But moon's structural cap (P/8 ≈ 3.36 days) is tighter than that, so the cap wins anyway. window_days, cap_applied, and delta_days are all showing the same number (3.3607...) for a reason, not a glitch: delta_days and moon's cap divisor both happen to be period/8 in this code, so for moon specifically all three collapse to one value. Nothing stuck or duplicated — just two independent formulas sharing a divisor for this one category. The takeaway: moon's rate is actually decent; the P/8 structural ceiling is just deliberately tighter than what the rate alone would justify. Correct behavior, wrong guess about which branch would fire — not a bug.
served_window: null at the top is expected here too, not a failure. Moon is one of the two categories (moon, spacecraft) excluded from the global served_window entirely — this run only had one object, and it's the excluded one, so there were zero eligible participants. That's a different, silent code path from the "measurement failed" warning case — no warning printed because nothing failed. Real served_window shows up in Step 2 once all 11 non-excluded objects are in the same build.
[RECOVER] fired again, same file, same non-blocking story as before — nothing new there.

python tools/gallery_cache_builder.py --dry-run --object pluto

**Claude:**
Now the bigger thing — Pluto's numbers are internally correct, but they're not measuring what the addendum assumed, and it matters.
Look at a_au: 1.424e-05. That's not Pluto's real ~39.5 AU distance from the Sun — that's ~2,130 km, which is Pluto's wobble radius around the Pluto-Charon barycenter. The osculating block confirms it: "center": "pluto_barycenter", "canonical_frame": "barycenter-relative". That's a deliberate, already-settled serving choice from the Pluto/Charon design work, not new to M2 — but it means the trust check just measured the mutual Pluto-Charon orbit, not Pluto's solar orbit.
And the number checks out as real physics, not an error: 360 / 56.39 deg/day = 6.384 days — that's essentially exactly the textbook Pluto-Charon mutual orbital period (~6.39 days). So there's no bug in the arithmetic. The problem is one level up:

dwarf_planet isn't in the excluded-participant set ({'moon', 'spacecraft'}) — only moon and spacecraft are excluded from the global served_window.
Charon does the exact same motion (same barycenter, same ~6.4-day period) and is excluded — but only because its category label happens to be moon, not because anything actually checks whether an object is barycenter-anchored.
Pluto is doing the identical kind of fast local orbit, but keeps its dwarf_planet label, so it isn't caught.

I checked how this actually gets used before flagging it — resolver.py's resolve() checks the requested date against served_window as one single gate for the entire scene, before it even looks at which objects are in that scene:
pythonserved_window = cache.served_window()
...
if not (lo <= resolved_jd <= hi):
    raise OutOfServedWindowError(...)
So if Pluto's ~6.4-day window ends up controlling the global minimum in Step 2 (and it will — every other participant we've measured so far is in the hundreds of days, comets will be in the thousands), a request for something as ordinary as "Jupiter, 10 days from now" gets rejected — even though Jupiter's own window is ~4,336 days and Pluto isn't even in that scene.
This is exactly the "if it still is [the tightest window], that's worth a second look" checkpoint the addendum already built in for Step 2 — it's just showing up now, for a real and legitimate reason instead of the mock's placeholder.
Three ways to handle it, your call:

Reframe the exclusion rule around the serving frame, not the category label — anything barycenter/parent-relative gets excluded, which would catch Pluto the same way it already (accidentally) catches Charon, and generalizes to any future object served the same way.
Leave it as-is — accept that the whole site's date range is genuinely bounded to about a week until this is revisited.
Change how the resolver consumes served_window (per-object bound instead of one global minimum) — bigger change, and outside M2's declared scope (the implementation report confirmed resolver.py has zero edits).

(1) fits the pattern the codebase already uses for Charon, for what that's worth, but I don't want to assume it for you.

**Tony:** Yes, #1. 

python tools/gallery_cache_builder.py --dry-run --object apophis

**Claude:**
Apophis checks out cleanly, no surprises, exactly the "boring in a good way" result the addendum expected.

Period matches the real thing. n_deg_per_day: 1.1127 → period 360/1.1127 ≈ 323.5 days — that's Apophis's actual, well-known ~323.6-day orbital period. Second object in a row where the raw mean-motion number lines up with the textbook value.

Even cleaner than Earth. error_rate_deg_per_day: 3.7e-06 — smaller than Earth's 2.8e-04, which makes sense: this is Apophis measured on an ordinary day, far from any close encounter, so two-body is about as good a fit as it gets. And like Earth (and unlike Moon/Pluto), the cap binds at the full period (window_days == cap_applied == 323.5) rather than the measured rate — the rate alone would allow a window in the tens of thousands of days, but the P/1 structural ceiling for asteroid category catches it first. Exactly the "planet-like, not comet-like" shape predicted, no inversions.

One thing worth actually checking rather than shrugging off: the top-level served_window (start 2460918.577...) doesn't exactly match Apophis's own trust.window (start 2460917.953...) — a ~0.624-day gap. Same kind of small gap showed up on Earth's run too (~0.058 days), a different size each time. I went back to the code rather than assume it's noise: the per-object window is anchored to element_epoch_jd (midnight UTC, fixed for the day), but the global served_window is deliberately centered on as_of_jd = right now — actual wall-clock time when the build runs, line 1029/1046. And it checks out numerically both times: Apophis ran at 14:59:08 UTC (≈0.624 of a day past midnight — matches its gap exactly), Earth ran at 01:24:06 UTC (≈0.058 of a day past midnight — matches its gap exactly). So this is two different reference points doing two different jobs correctly, not a bug — per-object math anchors to when the elements were fetched, the site-wide bound anchors to the actual present moment. Good one to have caught and confirmed rather than waved off.

python tools/gallery_cache_builder.py --dry-run --object halley

**Claude:**
Good — that completes the five, but the number doesn't match what I predicted, and I want to own that rather than talk around it.

error_rate_deg_per_day: 6.4e-06 — that's smaller than Earth's (2.8e-04), far smaller than Moon's or Pluto's, and barely bigger than Apophis's (3.7e-06). I predicted Halley would show the largest rate of the five, reasoning "near perihelion = fast = should diverge fastest." That reasoning was wrong, or at least incomplete — here's what's actually going on, traced through the numbers rather than guessed at:

delta_days is capped at a flat 30 days, and that cap doesn't scale with period. delta_days = min(period/8, 30). For Moon (period ≈ 27d) and Pluto (mutual period ≈ 6.4d), period/8 is well under 30, so the check window scales down with the object — Pluto got delta_days ≈ 0.8 days, a fair slice of its own tiny orbit. But Earth, Apophis, and Halley all have period/8 > 30, so all three get clamped to the same flat 30-day window regardless of how much longer their real period is. For Earth (365d) and Apophis (323d), 30 days is still a meaningful ~8-9% bite out of the orbit. For Halley (period ≈ 27,761 days, ~76 years — matches the real value almost exactly), 30 days is about 0.1% of the orbit — a genuinely tiny slice, even though it's centered at the fastest point. Perturbation away from the tangent two-body ellipse builds up with elapsed time from the anchor epoch, so an absolutely-tiny window, even at perihelion, just hasn't had much chance to show it yet. That's a real property of a flat time cap on a wildly different timescale, not a bug.

And it turns out not to matter anyway — same as Earth and Apophis, the category structural cap wins here, not the measured rate. The rate alone would justify a window around 39,000 days; the comet P/2 cap clamps it to 13,880.67 regardless (cap_applied == window_days, confirmed). So the unusually clean rate is close to moot for what actually gets served.

The part of the prediction that mattered more, and did land clean: this is the first real, live-Horizons confirmation that the Tp-anchor fix actually works end to end. epoch_jd: 2446469.97 — 1986, not today — and the two samples are at offset_days: -30.0 / +30.0 from that epoch, not from "now." That's exactly the mechanism the mock bug used to get wrong. It's correct against the real API.

Five for five, Step 1 done. Quick recap of what it proved: mean-motion column resolves correctly on live queries, list-form epoch vectors work, the comet Tp-anchor fix holds against real data, and every rate/cap relationship lined up with known real physics except this one surprise, which explained itself once traced through the code rather than assumed.

```

### Step 2 -- real --first-build; inspect the swapped coverage_index

**Claude:**
## What's still needed — summary

**For L-149 to close**, its own Gap says exactly two things remain, both live (not mock):
1. **Step 2** — real `--first-build`
2. **Step 3** — real `--nightly`

Once those two run clean, L-149 goes from OPEN to DONE. Everything else about it (the code fix, the offline tests proving it) is already done and verified.

**For the overall M2 addendum**, Steps 4 and 5 are also still open, but they're not part of L-149's own gap — they're general M2 acceptance, not tied to this specific bug:
- **Step 4** — resolver date-picker check (dev render page)
- **Step 5** — fetch-cost/throttling note

**Not blocking any of this:**
- **L-150** (Pluto/Charon two-view design) — decided, not built, rides with a future golden artifact
- **L-151** (gallery-assembler skill) — looks done in the repo, ledger status just hasn't been flipped

## One thing to flag before you run Step 2

The addendum's own "Confirm" checklist for Step 2 was written *before* the L-149 fix, so one line in it is now stale:

> "the controller should be one of earth/jupiter/saturn/**pluto**/apophis/halley/encke... if Pluto is still the tightest, that's worth a second look"

That's outdated — Pluto is now structurally excluded from voting (barycenter-relative, not heliocentric), so it can't be the controller at all anymore. The updated version of that check is:

- **Trust blocks:** still 11 measured (`two_body_rate_v1`) + Voyager 1 (`fetched_positions`) — unchanged, every object still gets measured individually.
- **Global `served_window` controller:** must be one of exactly 6 — **earth, jupiter, saturn, apophis, halley, encke.** Moon/Io/Titan (parent-relative) and Pluto/Charon (barycenter-relative) should show a `trust` block but take no part in the global minimum.
- If Pluto or Charon *does* still show up as the controller, that's now a real regression, not a "worth a second look" — the fix isn't working.

Step 4, when you get to it, is actually the cleanest real-world proof of the fix: try a scene like "Jupiter, 10 days out" on the dev render page. Before the fix that would've wrongly hit `OutOfServedWindowError` because of Pluto's ~6.4-day window; now it shouldn't.

Want me to update the addendum doc itself with this corrected Step 2 checklist before you run it, or just run it as-is and we'll reconcile after you paste the output?

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

**Tony**:
Pass. 

**Claude**:
Both new SHAs check out live. Now confirming the pushed data actually matches what you uploaded, and checking why the run manifest says `"committed": false`.Let me double check one detail — the run manifest and the served positions file show different Voyager 1 point counts (105 vs 113), worth verifying before I call this clean.Both new SHAs check out live — gallery `c5c9ea09`, orrery `3417753c`. And I pulled the actual pushed `coverage_index.json` from the new gallery HEAD: it matches your upload byte-for-byte on `served_window` and the `generated` timestamp, so this build's data is genuinely live now, not just staged locally.

## Two things that look odd but are expected

**`"committed": false` in the run manifest** — not a problem. `--first-build` alone doesn't auto-push; the script only commits+pushes if you also pass `--commit`. You didn't, so the swap happened locally and the manifest correctly reports it wasn't pushed by the script. You then pushed it yourself via GitHub Desktop about 4 minutes later — I checked: the actual commit on GitHub is titled "interactive first build," authored by you, timestamped 20:06:44 UTC. Exactly your normal loop (script swaps → you review → you commit+push).

**The `[RECOVER]`/quarantine warning** — also expected, and self-healing. Something (likely OneDrive, since your whole project tree lives under OneDrive Desktop) had a lock on the old `data\solar-system.prev` folder, so the builder quarantined it instead of failing the run. The quarantined folder gets swept away automatically after a few days — nothing for you to do.

(Also checked the Voyager 1 count mismatch you might notice — manifest says `backfilled(105)`, served file says `113` points. Traced it in the code: `backfilled(N)` only counts points fetched *this run* [glide + flyby windows + fresh tail]; the extra 8 come from older archived points this run didn't need to re-touch. Both numbers are correct, just measuring different things.)

Two things that look odd but are expected

"committed": false in the run manifest — not a problem. --first-build alone doesn't auto-push; the script only commits+pushes if you also pass --commit. You didn't, so the swap happened locally and the manifest correctly reports it wasn't pushed by the script. You then pushed it yourself via GitHub Desktop about 4 minutes later — I checked: the actual commit on GitHub is titled "interactive first build," authored by you, timestamped 20:06:44 UTC. Exactly your normal loop (script swaps → you review → you commit+push).

The [RECOVER]/quarantine warning — also expected, and self-healing. Something (likely OneDrive, since your whole project tree lives under OneDrive Desktop) had a lock on the old data\solar-system.prev folder, so the builder quarantined it instead of failing the run. The quarantined folder gets swept away automatically after a few days — nothing for you to do.

(Also checked the Voyager 1 count mismatch you might notice — manifest says backfilled(105), served file says 113 points. Traced it in the code: backfilled(N) only counts points fetched this run [glide + flyby windows + fresh tail]; the extra 8 come from older archived points this run didn't need to re-touch. Both numbers are correct, just measuring different things.)

Step 2 — PASS, and this is the real-data proof for L-149
served_window is populated: half-width = 323.5468 days
Controller = Apophis (window_days: 323.54683906902784 — matches the half-width to 10 decimal places). Not Pluto.
Pluto (window ~6.38d) and Charon (~0.80d) still get fully measured — their trust blocks are real and correct — but neither touches the global bound at all. That's the exclusion working exactly as designed, on live Horizons data, not just the mock.
All 11 non-spacecraft objects show two_body_rate_v1; Voyager 1 shows fetched_positions with window: null — 12/12 as expected.
Spot-checked the physics on every object (period from n_deg_per_day vs. real values): Jupiter ~11.86 yr, Saturn ~29.5 yr, Io ~1.77 d, Titan ~15.9 d, Halley ~76 yr — all correct, nothing inverted.

Small bonus: feature_configs.json is no longer the empty stub — Earth/Jupiter/Saturn are serving real shell and ring data now. That's L-118's problem, not L-149's, but worth knowing it looks resolved too next time that item comes up.

For L-149 specifically: its Gap needed Step 2 and Step 3. Step 2 just passed cleanly — Step 3 (--nightly) is the last thing standing between it and DONE. Ready whenever you want to run it; same deal, paste the output and I'll check the trust blocks refresh without the shrink gate or any M1 structural check regressing.

Short answer: yes, but with one caveat

L-118's own Gap has 5 items. Between what you just ran and what I verified, 4 of them are now confirmed done — but the 5th (nightly acceptance) hasn't happened yet, and it's the exact same run that closes L-149's own remaining gap.

Confirmed done (live, not assumed):

Feature params ported into objects_config.json and derive_served builds feature_configs.json from it — your uploaded file shows real content: Earth (atmosphere_shell + van_allen_belts), Jupiter (ring_system + radiation_belts), Saturn (7-ring system), everything else correctly {}
served_window is populated — confirmed non-null in the same build
Layer-1's shape-validator checks for this (schema_version, all 12 slugs, dict-not-list shape, malformed-input ABORTs) all still pass — 138/138, and I confirmed the code didn't change between the HEAD I tested and your new push, so that result still holds

One worth flagging while we're in there: L-118's text says served_window "rides along in the same change" as the feature_configs fix. In practice it turned out to be its own separate, bigger effort — the M2 trust-measurement system (L-149/L-150/L-151), not something derive_served's feature-porting code does directly. Worth correcting that cross-reference so a future reader doesn't go looking for served_window logic in the wrong place.

Still open: the nightly leg. L-118's Gap wants --first-build/--nightly acceptance; you've done first-build, not nightly yet. Same run you're about to do for L-149's Step 3 — one nightly run closes both.

Not part of closing these two

M2's Layers 1-3 (what we've been doing) are the builder's data gate — is the right data being served correctly. Mode 5 is a separate, later render gate — does the golden artifact actually look right. The gallery-assembler skill draws this line explicitly: passing the data gate is a prerequisite for attempting an artifact's Mode 5 acceptance, not the same milestone as passing it.

Step 4 (already on your list — the resolver date-picker check) is a small visual check, but it's testing that served_window correctly gates dates on the render page — not a Mode 5 aesthetic pass on a golden artifact.

Looking ahead — I checked, and it's not ready yet either

The natural next Mode-5 candidate would be Artifact 2 (Jupiter/Saturn), next in your declared order. Since today's fix means Jupiter's rings/radiation belts and Saturn's 7-ring system are now being served correctly, I checked whether anything actually draws them yet.

It doesn't. I searched the whole repo — Python and JS/HTML both — for anything consuming ring_system, van_allen_belts, atmosphere_shell, or radiation_belts. Nothing does. Even Earth's own closed Artifact 1 confirms this by design: its acceptance test explicitly checks that features dispatch as data only, with "JavaScript rendering them" as the intended next step — and that JS doesn't exist anywhere in the repo yet.

So Jupiter/Saturn isn't blocked on data anymore (once nightly confirms), but it is blocked on writing that rendering layer — real, separate work, not a Mode 5 visual check you could do today.

(Pluto/Charon two-view, if that crossed your mind since it's the artifact most tied to today's fix — that's Artifact 6, and it's additionally blocked on L-150's multi-orbit trust model, which is still just a design decision, not built.)

So, for right now

Just Step 3 (--nightly) closes L-118 and L-149. Mode 5 comes later, once the feature-rendering layer for Jupiter/Saturn exists to look at.

## Step 2 — PASS, and this is the real-data proof for L-149

- `served_window` is populated: half-width = 323.5468 days
- **Controller = Apophis** (`window_days: 323.54683906902784` — matches the half-width to 10 decimal places). Not Pluto.
- Pluto (window ~6.38d) and Charon (~0.80d) still get fully measured — their trust blocks are real and correct — but neither touches the global bound at all. That's the exclusion working exactly as designed, on live Horizons data, not just the mock.
- All 11 non-spacecraft objects show `two_body_rate_v1`; Voyager 1 shows `fetched_positions` with `window: null` — 12/12 as expected.
- Spot-checked the physics on every object (period from `n_deg_per_day` vs. real values): Jupiter ~11.86 yr, Saturn ~29.5 yr, Io ~1.77 d, Titan ~15.9 d, Halley ~76 yr — all correct, nothing inverted.

Small bonus: `feature_configs.json` is no longer the empty stub — Earth/Jupiter/Saturn are serving real shell and ring data now. That's L-118's problem, not L-149's, but worth knowing it looks resolved too next time that item comes up.

**For L-149 specifically:** its Gap needed Step 2 *and* Step 3. Step 2 just passed cleanly — Step 3 (`--nightly`) is the last thing standing between it and DONE. Ready whenever you want to run it; same deal, paste the output and I'll check the trust blocks refresh without the shrink gate or any M1 structural check regressing.

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
