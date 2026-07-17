# M2 Implementation Report -- F1a Trust Measurement + served_window

Built by Claude Sonnet 5. Manifest: `documentation/PHASE2_F1_BUILD_MANIFEST_v2_2.md`
(orrery repo, fetched and read in full at build time -- not carried from a
prior session's paraphrase).

## Pinned SHAs and clean-worktree proof

- **Gallery** built on `8a65699c022effb8131bae1939793209ab1c436f` (main) --
  this already includes the M1 shape-validator regression-test follow-up
  (confirmed byte-identical to the delivered patch before building M2 on
  top of it).
- **Orrery** `9644b1f9cc7943a509d92c973ee6d3b756b4dffc` (unchanged; M2 makes
  zero orrery-repo edits -- all M2 logic and its render_orbits.py import are
  gallery-repo-internal).
- Both re-confirmed live via `git ls-remote` immediately before writing this
  report.
- Layer 1 proof run from a **truly clean clone** (fresh `git clone`, edited
  files copied in, working tree otherwise pristine at the SHA above): PASS.

## Files changed (M2)

- `tools/gallery_cache_builder.py`: import bootstrap for
  `solve_kepler`/`_elements_to_xyz_au`; `_jd_to_dt`; `fetch_vectors_range`
  additive `epoch_jds` mode; `fetch_elements` `n` capture;
  `append_elements_history` / `last_good_elements` carry `n` through history
  and the A-3 fallback; `build_osculating_block` adds `n_deg_per_day`; new
  trust-measurement block (`_two_body_position`, `_angle_between_deg`,
  `_fetch_check_vectors`, `measure_trust`); `run_build` wires
  `measure_trust` into the per-object loop; `serve_last_good` adds a
  `trust` key to both its stale returns; `derive_served` attaches `trust`
  per object and computes the global `served_window` (FLAG-3/4/5).
- `tools/test_gallery_cache_builder_offline.py`: `fake_elements` gains a
  mocked `n`; `fake_vectors` gains an additive, separate `epoch_jds` branch
  (Option B); 43 new M2 checks (per-object trust presence/shape, FLAG-6
  determinism for earth/moon/halley, served_window bracketing, and one
  forced-failure test exercising FLAG-3 through the real dispatch).
- `render_orbits.py`, `resolver.py`, `cache_reader.py`: **zero edits**,
  confirmed by diff-stat against the pinned gallery SHA (only the two files
  above appear in the diff).

Diffs and full files are attached alongside this report.

## Deviations from the manifest -- flagged, not silently resolved

1. **The literal "leave fake_vectors untouched" reading of Option B is not
   achievable, and I built something that honors its intent instead.**
   Manifest sec 5.2 point 2 requires the check-vector fetch to "route
   through the same injectable fetch symbols the offline suite mocks" --
   i.e., through `fetch_vectors_range` itself, not a new production
   function. Since `measure_trust` is wired into `run_build`'s per-object
   loop unconditionally (every build measures trust for every non-spacecraft
   object -- confirmed by the manifest's own sec 5.6 test design, which
   expects the *existing* first-build test call to also produce trust
   blocks), `fetch_vectors_range` is the ONE shared injection point for both
   the arc fetch and the check-vector fetch, for the entire test run, not
   just an isolated M2 test block. A wholly separate mock *function* bound
   to a *different* symbol was therefore not compatible with the "same
   injectable symbol" requirement. Resolution: `fetch_vectors_range` (and
   `fake_vectors`) gained a new, **additive** `epoch_jds` calling
   convention -- a separate `if` branch, not a modification of the existing
   lines -- that is genuinely Kepler-consistent. The existing date-range
   branch, used by the arc fetch and all 91 pre-existing checks, is
   byte-for-byte unchanged. This satisfies the manifest's routing
   requirement and Tony's Option-B regression-safety intent (zero risk to
   the other 91 checks) without literally being "the same untouched
   function for everything."
2. **FLAG-6's own stated rationale (sec 0) and sec 5.6's text both assert
   the existing `fake_vectors` is already Kepler-consistent with `ELEMS`.**
   Independently re-verified false (twice: once flagged before this build,
   once reconfirmed while building) -- it returns a static `(a, 0, 0)` for
   every epoch. The corrected implementation achieves FLAG-6's *outcome*
   (deterministic `window_days == cap` for every category) via the new
   `epoch_jds` branch described above, not via the literal mechanism the
   manifest text describes.
3. **`fetch_vectors_range`'s new `epoch_jds` mode returns an index-keyed
   dict** (`{0: {...}, 1: {...}}`), not the date-string-keyed shape the
   existing mode uses. Two check epochs can land in the same calendar date
   for a fast-moving object (Io-class Delta is hours, not days), so
   date-string keys would silently collide. This is a new, additive return
   shape used only by this new calling convention.
4. **`append_elements_history` and `last_good_elements` now carry `n`
   through the JSONL history and the A-3 stale-fallback path.** Not
   explicit in the manifest text (which only names `fetch_elements` and
   `build_osculating_block`), but without it a moon whose *fresh* element
   fetch fails on a given night would always lose its trust measurement
   even though its last-known `n` is sitting in history -- an unnecessary
   loss given the additive-field philosophy already in play.
5. **`serve_last_good`'s non-spacecraft stale path serves `trust` as
   WARN/null rather than re-attempting a fresh check-vector fetch.** Not
   addressed in the manifest. Reasoned, not assumed: a fresh check-vector
   fetch during the same outage that already triggered the A-3 fallback
   would very likely also fail, so re-measuring was judged not worth the
   extra network call. Flagging in case Tony wants different behavior here.
6. **A bug in my own test mock, caught and fixed before delivery, not a
   manifest deviation but worth recording:** the first version of the
   Kepler-consistent `epoch_jds` mock branch hardcoded the measurement
   epoch as `FIXED_NOW`. This is wrong for Tp-anchored comets (Halley/Encke
   measure at their `resolve_comet_conic` solution-TP epoch, which can be
   decades from "today") and produced a large, spurious `error_rate` for
   Halley (~0.40 deg/day instead of 0) in an early test run. Fixed by
   deriving the epoch as the midpoint of the two requested check epochs,
   which is correct by construction for any object regardless of which
   epoch its elements were actually fetched at. Caught by sanity-checking
   real numbers before writing the formal assertions, not assumed correct.

## Commands run and results

```
python3 -m py_compile tools/gallery_cache_builder.py tools/test_gallery_cache_builder_offline.py
  -> clean

ASCII / LF encoding gate on both files -> clean

python3 tools/test_gallery_cache_builder_offline.py   (from a clean clone)
  -> PASS (134 checks, 0 failures)
  [87 pre-existing + 4 M1 shape-validator (already at base) + 43 M2]

Independent sanity script (ad hoc, not part of the committed suite):
constructed a first-build run and inspected every non-spacecraft object's
trust block directly -- used to design and verify the formal assertions
above, and to catch the Halley epoch bug in (6) before it became a
false-passing test.
```

Layer 2 (real Horizons dry-run) was **not** run -- this sandbox has no
network access to JPL Horizons (only pypi/github/npm domains are
allowlisted). This is Tony's gate per manifest sec 5.7 and is the single
most important remaining check, in particular:

- Whether `Horizons(..., epochs=[jd1, jd2])` for `.vectors()` behaves the
  way it already does for `.elements()` in `fetch_elements` (same
  astroquery class, same `epochs` parameter, list form) -- I could not
  confirm this against the live API.
- Whether Horizons' mean-motion column is reliably named `n` or `N` for
  the object types in scope (the `get_col` fallback list mirrors the
  existing defensive pattern used for every other column, but hasn't been
  checked against a real response).

## Generated artifact excerpts (from the sanity run, mocked data)

```json
"earth": { "trust": {
  "schema_version": 1, "method": "two_body_rate_v1",
  "element_epoch_jd": 2461230.5, "delta_days": 30.0,
  "error_rate_deg_per_day": 0.0, "tolerance_deg": 0.5, "guard_k": 2.0,
  "window_days": 365.2568983263281, "cap_applied": 365.2568983263281,
  "window": {"start_jd": 2460865.24, "end_jd": 2461595.76}
}}
"voyager_1": { "trust": {
  "schema_version": 1, "method": "fetched_positions", "window": null
}}
```

Top-level `served_window` (mocked build): `{"start_jd": 2461230.49998,
"end_jd": 2461230.50002}` -- correctly brackets `as_of_jd = 2461230.5`.

## Per-object trust summary (mocked first-build)

| Object | Category | Epoch (JD) | Delta (d) | Rate (deg/d) | Cap basis | Window (d) | Participant? |
|---|---|---|---|---|---|---|---|
| earth | planet | 2461230.5 | 30 | 0.0 | P | 365.3 | YES |
| jupiter | planet | 2461230.5 | 30 | 0.0 | P | 4336 | YES |
| saturn | planet | 2461230.5 | 30 | 0.0 | P | 10835 | YES |
| moon | moon | 2461230.5 | 0.005949 | 0.0 | P/8 | 0.005949 | no (excluded category) |
| io | moon | 2461230.5 | 0.006834 | 0.0 | P/8 | 0.006834 | no (excluded category) |
| titan | moon | 2461230.5 | 0.03372 | 0.0 | P/8 | 0.03372 | no (excluded category) |
| pluto | dwarf_planet | 2461230.5 | 2.4e-06 | 0.0 | P | 1.89e-05 | YES |
| charon | moon | 2461230.5 | 5.8e-05 | 0.0 | P/8 | 5.8e-05 | no (excluded category) |
| apophis | asteroid | 2461230.5 | 30 | 0.0 | P | 323.4 | YES |
| halley | comet | 2446470.5 | 30 | 0.0 | P/2 | 13715 | YES |
| encke | comet | 2460239.5 | 30 | 0.0 | P/2 | 602 | YES |
| voyager_1 | spacecraft | -- | -- | n/a | n/a | null | no (excluded category) |

Mocked error rates are all exactly 0.0 by construction (FLAG-6, Option B's
dedicated Kepler-consistent branch) -- this proves the *wiring*, not real
accuracy; real error rates come from Layer 2 against actual Horizons data.

## Global controlling object and final served_window (mocked build)

7 participants: earth, jupiter, saturn, pluto, apophis, halley, encke --
exactly the 7-of-12 the manifest names in sec 5.5. **Pluto's mocked window
controls** (it has by far the smallest window, `1.89e-05` days) because its
pre-existing mock `a` value (`1.39e-5` AU, in the test file's `ELEMS` table
since before this build) is a placeholder that was only ever load-bearing
for the guard-band check, not for period/window math -- now that trust
measurement uses `a` for a real period calculation, Pluto's mock produces an
absurdly tight window. This is not a bug in the M2 code (the minimum is
computed correctly); it's a pre-existing test-data placeholder now exercised
in a new way. Flagging for awareness; not changed, since touching `ELEMS`
could perturb the guard-band tests it was tuned for.

## Network/cache behavior (projected, not measured -- no live Horizons access)

Each non-spacecraft object now costs one additional `fetch_vectors_range`
call per build (the two check-vector epochs in a single `epoch_jds` call),
i.e. +11 Horizons calls per nightly run (was +22 in the manifest's estimate,
which assumed two separate single-epoch calls; the list-form single call
here halves that). Confirm against real Horizons at Layer 2.

## Known warnings (from the mocked runs)

- `served_window: null -- trust measurement missing/failed for [...]` fires
  correctly whenever any participant's measurement fails (observed for
  `['encke', 'halley']` in the pre-existing N5 simulated-outage test, and
  for `['jupiter']` in the new forced-failure M2 test) -- FLAG-3 exercised
  through the real dispatch, not just asserted.
- `<slug>: trust measurement failed (no n_deg_per_day ...)` fires correctly
  before `fake_elements` carried a mocked `n` (confirmed during build,
  before the mock update) -- the WARN-not-ABORT disposition held even
  across every one of the 11 non-spacecraft objects simultaneously.

## Out-of-scope files -- explicit confirmation of zero edits

`gallery/assembler/resolver.py`, `gallery/assembler/cache_reader.py`,
`gallery/assembler/render_orbits.py`: confirmed zero edits by diff-stat
against the pinned gallery SHA (only `tools/gallery_cache_builder.py` and
`tools/test_gallery_cache_builder_offline.py` appear).

## Commit SHAs

Not yet committed -- Tony holds sole commit authority. Built on gallery
`8a65699c`; ready for Tony to review the attached diffs and push.
