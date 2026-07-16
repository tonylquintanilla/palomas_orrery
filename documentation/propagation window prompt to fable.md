# Request: creative solutions for the served-position trust-bound problem

**To:** Claude Fable
**From:** Tony Quintanilla, relayed via Claude Sonnet 5 (Mode 7 collegial
relay — physics/math validation + creative architecture input needed)
**Session base:** orrery HEAD `f961b4424fd633595286c2764a2ebd19df677236`,
gallery HEAD `953c650edc8dbd35ab11ec1720f8283987d63901` (both re-confirmed
live via `git ls-remote` at time of writing — re-pin yourself before
relying on any code-level claim below, per this project's standing
discipline)

## What this is

This is one specific, bounded problem inside a larger interactive
solar-system gallery build (Paloma's Orrery project) — not a request to
review the whole architecture. Tony wants genuinely creative options here,
optimized for user experience (the biggest reasonable window, not the most
conservative one), constrained by what's actually feasible in our
execution environment (Pyodide — Python compiled to WebAssembly, running
client-side in the browser). Full latitude to propose something none of us
have thought of yet — that's the point of asking.

## The concrete problem

The gallery's first working artifact (Earth alone) already has a **live
date picker** in its dev test page (`gallery/solar_system_earth_test.html`).
Type in any date, and the assembler re-propagates Earth's position via
Kepler's equation from last night's osculating-element snapshot — moving
the date visibly walks Earth around its orbit, live, in the browser.

**Nothing currently bounds how far from "tonight" that date can be.** A
user (or a bug) can request a date 500 years out, or 500 years back, and
get back a confident-looking position that's quietly wrong. A single
night's osculating-element snapshot (6 numbers + epoch) is a good stand-in
for an object's real position only within some distance of that epoch —
real orbits perturb away from a clean two-body ellipse over time, and how
fast they perturb varies enormously by object.

The consuming code already has a placeholder for this. `gallery/assembler/
resolver.py` (lines 91-106) reads a `served_window` field —
`{"start_jd": ..., "end_jd": ...}` — from the served cache
(`coverage_index.json`) and is supposed to reject (or, today, just warn
about) a requested date outside that bound:

```python
served_window = cache.served_window()
if served_window is None:
    warnings.append(
        "served_window is null in the served cache; propagation bound "
        "is unenforced (populate via the F1 builder change)."
    )
else:
    lo, hi = served_window.get("start_jd"), served_window.get("end_jd")
    if lo is not None and hi is not None and not (lo <= resolved_jd <= hi):
        raise OutOfServedWindowError(...)
```

Today the builder (`tools/gallery_cache_builder.py`, `derive_served`, lines
710-751) always writes `served_window: null` — this is what we're trying
to actually populate. **The field currently exists as ONE global bound for
the whole scene**, not one per object — whether that's even the right
shape is part of the question, below.

## What's already settled, so you don't have to re-derive it

- Osculating elements (6 numbers + epoch) fully determine an orbit's
  **shape** — you can draw the whole ellipse from a single snapshot,
  regardless of period. That's not in question; it's a separate concern
  from this one.
- Elements get **replaced wholesale each night, not accumulated** — the
  builder fetches fresh from Horizons every build (`horizon=0`, no forward
  padding). There's no long history of past snapshots to lean on.
- Spacecraft are the one exception to everything above — they get real
  fetched position vectors over a date range (appended nightly), not
  Kepler-propagated from elements, because they don't follow a clean orbit.
  This bound doesn't apply to them.

## The physically-grounded idea on the table, and its complication

Tony's proposal: bound the trust window by **how far tonight's osculating
elements have diverged from the object's mean (long-term-average) orbital
elements** — divergence from the mean orbit is a real physical signal of
how much perturbation has pulled the instantaneous orbit away from an
idealized ellipse, and it is explicitly **not one-size-fits-all**. Planets
stay close to their mean orbit for a long time; satellites/moons can
diverge substantially from a mean orbit almost immediately, since they're
strongly perturbed by their parent body.

The complication, verified this session: mean elements exist and are
actively maintained for planets and a curated comet list
(`orbital_elements.py`), but **moons were explicitly excluded** from that
work in an earlier design pass — their mean-element source data "lacks
secular-rate terms and is inconsistently dated." Concretely: `orbital_
elements.py`'s Moon entry (line 853) is a single static snapshot dated
`2013-07-31`, with no rate terms to advance it — 13 years stale as of this
writing. So the object Tony flagged as the hardest, most important test
case (satellites) is also the one where the input data for "compare
against the mean" is weakest. Worth knowing before proposing an approach
that assumes clean mean-elements data everywhere.

**Agreed fallback if a clean divergence measure isn't available for a
given object:** use one full orbital period (computable directly from the
served osculating semi-major axis via Kepler's third law — no new data
needed) as a conservative bound. Even a period of a few days is fine as a
floor.

## The actual ask

1. **What measure should drive the trust bound, per object?** Is
   divergence-from-mean the right physical proxy, or is there a more
   standard technique from real ephemeris/orbital-mechanics practice (how
   JPL Horizons or other tools communicate validity windows) that we're
   missing? Is there a cheap way to estimate perturbation growth without
   needing a maintained mean-elements reference at all (e.g., from the
   osculating elements' own rate of change across consecutive nightly
   snapshots, once a few nights of history exist)?
2. **What shape should `served_window` actually take**, given the trust
   bound is inherently per-object (a global scene-wide field seems wrong
   once you accept planets and moons need very different bounds)? Note
   this isn't just a builder change — `resolver.py` and `cache_reader.py`
   already consume the current global shape and are part of Artifact 1's
   closed, golden-fingerprinted build. A shape change touches locked code,
   not just new work — say so plainly if that's where this leads.
3. **UX, not just correctness:** Tony wants the date picker to show the
   meaningful bound as a note/indicator to the user — "here's the range we
   can vouch for" — rather than necessarily hard-blocking. What's the best
   way to surface this so it reads as helpful, not alarming, especially
   near the edges of a short window (a fast-moving moon) versus a long one
   (an outer planet)?
4. **Pyodide feasibility:** whatever's proposed needs to actually run
   client-side, in-browser, on a WASM Python interpreter loaded lazily on
   a button click (see the dev page's consent-gate pattern) — no server
   round-trips, and it needs to feel instant to someone dragging a date
   picker. Flag anything that would need to be precomputed at build time
   (cheap, server-side, once a night) and simply served as a number, versus
   anything that could reasonably be computed live in the browser.
5. Sanity-check the one-orbit-period fallback itself — is it conservative
   enough, or does it understate risk for objects with strong short-period
   perturbations (e.g., a moon perturbed by more than one body)?

Structure your response however makes sense to you — a short set of
options with tradeoffs is more useful here than a single locked
recommendation, since this is still a live design conversation, not a
build request yet.

## Ref

`gallery/assembler/resolver.py` (lines 91-106), `gallery/assembler/
cache_reader.py` (lines 12-14, 40-41), `tools/gallery_cache_builder.py`
(`derive_served` lines 710-751, `process_object` lines 504-590),
`data/objects_config.json` (`defaults` block: `cadence_hours: 24,
guard_k: 2.0, freeze_after_days: 7, backfill_days: 365` — confirmed
spacecraft-fetch-only, not currently tied to any propagation-trust
concept), `data/solar-system/coverage_index.json` (gallery HEAD
`953c650e`); orrery `orbital_elements.py` (Moon entry, line 853, dated
2013-07-31, no secular terms); MASTER_PLAN_INTERACTIVE_GALLERY.md v13
(mean-elements-excludes-moons note, "New in v12" section);
PHASE2_ARTIFACT1_AS_BUILT.md §7 (dev render page, date picker); L-118
(F1, this problem surfaced while scoping it) (orrery HEAD `f961b442`).

---
Prompt written July 2026 with Anthropic's Claude Sonnet 5.