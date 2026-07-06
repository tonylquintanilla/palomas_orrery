# MASTER PLAN v9 + LEDGER UPDATES — Draft for Review
## July 6, 2026 | Tony + Opus 4.6

This document contains the proposed updates for Tony's sign-off.
Apply to MASTER_PLAN_INTERACTIVE_GALLERY.md and LEDGER_CONSOLIDATED.md
after review, then run ledger_index.py.

---

# MASTER PLAN CHANGES: v8 → v9

## Change 1: Header

Replace:
```
**Status:** Draft v8 — architectural pivot; ready for review.
**Base:** main @ `fdb66ca`, gallery @ `89c8bf30`
**Date begun:** July 3, 2026
**Last updated:** July 5, 2026
**Participants:** Tony Quintanilla, Claude Opus 4.6, Claude Opus 4.8, Claude Fable 5
```

With:
```
**Status:** Draft v9 — Phase 0 proven; data serving framed.
**Base:** main @ `a6bfcfb`, gallery @ `a6420bc`
**Date begun:** July 3, 2026
**Last updated:** July 6, 2026
**Participants:** Tony Quintanilla, Claude Opus 4.6, Claude Opus 4.8, Claude Fable 5
```

---

## Change 2: §2a — add one line after the Option C description

After the existing §2a content (after the paragraph about `gallery_metadata.json`
bridging both), add:

```
**First artifact deployed:** `interactive.html` at gallery repo root alongside
`index.html`, serving the Solar System Explorer exhibit. Pyodide v314.0.2.
Deployed July 6, 2026.
```

---

## Change 3: §3a — Full rewrite

Replace the entire section from `## §3a` through the `---` before `## §4` with:

```
## §3a — Data Serving Architecture (framed — Phase 1b)

**What Phase 0 proved.** The Solar System Explorer prototype computes
Keplerian orbits from mean orbital elements embedded in `orbital_elements.py`,
with no served data at all. This proves the Keplerian trace needs zero cache.
But the elements embedded in the codebase are manually maintained and some are
old (Saturn: epoch 2003, Pluto: epoch 1989). The desktop has better data —
fresh osculating elements in `osculating_cache_manager.py` and position
vectors in `orbit_paths.json` — accumulated over months of plotting.

**The data serving architecture is the pipeline that bridges Tony's desktop
caches to the browser.**

**Three trace types (from the desktop codebase, verified in gallery JSON):**

- **Actual positions** — Horizons ephemeris, x/y/z at dated time steps. Covers
  only the selected date range. Critical for precision at encounters, perihelia,
  close approaches, and date-range sweeps. This is the rolling cache data.
- **Osculating orbit at epoch** — complete Keplerian conic from instantaneous
  elements (6 numbers + epoch per object). Critical for moons, where it's the
  only way to see the full orbit shape. The divergence from the mean orbit IS
  the perturbation lesson.
- **Mean elements** — long-term average from `orbital_elements.py`. Ships with
  the codebase; no serving needed. Toggled off by default. Accurate for planet
  shapes; poor for close-approach detail.

**Two data types to serve (mean elements ship free):**

1. **Osculating elements per object** — tiny (a handful of numbers each). Could
   ride in the coverage index or a small sidecar file. The assembler computes
   the complete Keplerian conic from these.
2. **Position vectors over date ranges** — the rolling cache, the real volume.
   Per-object canonical files (F2 storage: ~190 objects, not 1,501 pairs).
   ~36 MB for the full catalog (Fable estimate).

**What works analytically vs what requires cache:**

- **Planets, asteroids, comets** — analytical orbits sufficient at solar-system
  scale. Presets override with cached data for close approaches and perihelia
  (Tier-2 curated data, write-once).
- **Moons** — cache required. Constant perturbations and non-heliocentric
  mechanics make analytical orbits insufficient. The rolling batch is primarily
  moons.
- **Spacecraft** — actual position arcs only, write-once (completed missions
  never change). Elements not typically applicable.

**Barycenters:** Pluto-Charon and Orcus-Vanth have barycenters outside the
primary body. The coverage index needs a `stored_center` field per object.

**F2 canonical storage (settled).** Per-object files, not per-pair. The old
pair-based `orbit_paths.json` (133 MB, 1,501 entries) is archived locally,
gitignored, and still used by the desktop code. The web cache is a derived
projection: an export script reads the desktop cache, extracts one canonical
trajectory per object (heliocentric for planets/asteroids/comets, parent-
relative for moons, arc-natural for spacecraft), and writes web-format files.
The precision rule: store moons parent-relative to preserve significance in
float64.

**Serving home is a configuration value.** The file layout and index schema
is the real architectural decision. Fable's H1 (dedicated `palomas-orrery-data`
repo, orphan-branch publish, zero history growth) is the leading candidate.
CORS verification needed before locking: does a project site under the custom
domain (`palomasorrery.com/<repo>/`) share the gallery's origin?

**Star cache:** 31 MB pickle → `.npz` for v1 (NumPy stable in Pyodide; Parquet
held as optimization). Deferred to Phase 3.

**Open questions (carry to Phase 1b/Phase 2 transition):**

- OQ-A: Web catalog scope — all 157 positional objects or a curated first tranche?
- OQ-B: Window policy — sliding, accumulating, or split (accumulate heliocentric,
  slide moons)?
- OQ-C: Update cadence — monthly batch + 90-day forward padding as starting point.
- OQ-D: Moon step size — 6h gives ~7 points per Io orbit (hexagonal). Inner moons
  may want 2h. Per-object `step_hours` in the index.
- OQ-E: Serving home — dedicated repo (H1) vs gallery subfolder (H2) vs R2 (H3).
  CORS check first.
- OQ-F: Canonical frame for each class — settled in principle (helio/parent-
  relative/arc-natural); implementation details at build time.
- OQ-G: Wire format — JSON for v1 (debuggability during assembler development).

**Source:** Fable 5 broad analysis (`DATA_SERVING_BROAD_ANALYSIS.md`, July 5,
2026, built on `993dfd5` / `a6420bc`). Reviewed and refined by Opus 4.6 + Tony
(July 6, 2026).
```

---

## Change 4: §5 — Phasing updates

### Phase 0 — replace entirely:

```
### Phase 0 — Gallery Integration Test

**✓ DONE** (July 6, 2026). `interactive.html` deployed to
`palomasorrery.com/interactive.html`. Pyodide v314.0.2 + NumPy computing
Keplerian orbits from mean elements, rendered by Plotly.js. Tested on desktop
Chrome and iPhone Safari. Zero server, zero data files — pure computation from
embedded orbital elements.

**Stack proven:** Python computation runs in the browser on a static GitHub
Pages site. Server/serverless decision resolved: Pyodide.

**Consent gate:** First-time visitors see an explicit opt-in explaining Pyodide
("a Python computation engine that runs entirely in your browser via
WebAssembly. No data leaves your device"). Choice persisted in localStorage;
returning visitors go straight to loading. Resolves the user-trust concern
about unnamed downloads.

**Lessons:** Pyodide v314.0.2 loads in ~4-10 seconds depending on connection
(cached after first visit). The lightweight approach (Python computes math,
JavaScript builds Plotly figure) avoids loading the full `plotly` Python
package — dramatically faster than loading plotly in Pyodide. The full
assembler approach (plotly in Python) deferred to Phase 2.
```

### Insert Phase 1b after Phase 1:

After the Phase 1 section (currently "✓ COMPLETE"), insert:

```
### Phase 1b — Data Serving Pipeline

**Build the bridge from Tony's desktop caches to the browser.** The desktop
has accumulated months of osculating elements and position vectors from
Horizons. Phase 1b makes this data available to the interactive gallery.

Deliverables:
1. **Export script** — reads desktop caches (osculating elements from
   `osculating_cache_manager.py` + position vectors from `orbit_paths.json`),
   writes per-object canonical files in web-servable format.
2. **Coverage index** — JSON manifest listing available objects, their
   availability class, date coverage, step size, stored center, and osculating
   elements. The assembler reads this to know what it can offer.
3. **Serving home** — resolve OQ-E (CORS check first), set up the serving
   destination, deploy the first web cache (planets as proof of pipeline).
4. **Resolve OQ-A through OQ-G** — scope, window policy, cadence, moon step
   size, format.

Requires: Fable analysis (delivered), gitignore updates (done).
Gate: export script runs, web cache deployed, assembler can read it.
```

### Phase 2 — update first line:

Change:
```
Requires: helpers split (L-087), Phase 0 lessons.
```
To:
```
Requires: helpers split (L-087), Phase 0 lessons, Phase 1b data pipeline.
```

---

## Change 5: §5a — Update dependency chain

Replace the dependency chain diagram with:

```
PREP (independent, can start now)
  ✓ LICENSE moved to root
  ✓ Section W ledger entries
  ○ Attribution page ─────────── 4.8 ──→ needed before public pages
  ○ Helpers split ────────────── 4.6 ──→ needed before Phase 2

PHASE 0 ✓ DONE ──── PHASE 1a ✓ COMPLETE ──── PHASE 1b
Stack proven         Vocabulary delivered       Data serving pipeline
(Jul 6)              (Fable, Jul 4)             Export script + coverage
                                                index + serving home
                          │
                     PHASE 2 ◄── Phase 1b + helpers split
                     Solar system assembler
                     + enhanced interactive page
                          │
                     PHASE 3
                     Star assembler + star cache format
                          │
                     PHASE 4
                     Hybrid domains
                          │
                     PHASE 5 ◄── 4.8 restraint discipline
                     Earth system
```

---

## Change 6: §7 — Open Decisions

Update items #1, #3-6, #10:

Item #1 — change from "Resolved in principle" to:
```
1. ~~**Server vs serverless.**~~ **Resolved: Pyodide.** Phase 0 proved the
   stack (July 6, 2026): Pyodide v314.0.2 loads in ~4 seconds on WiFi,
   computes Keplerian orbits via NumPy, renders via Plotly.js. Works on
   desktop Chrome and iPhone Safari. Consent gate addresses user-trust
   concern about unnamed downloads.
```

Items #3-6 — replace with:
```
3. **Data serving file layout and index schema.** Per-object canonical files
   (F2 settled). Coverage index format, availability classes, `stored_center`
   field. Resolved in Phase 1b.
4. **Tier-1 rolling cache scope and window.** OQ-A (which objects), OQ-B
   (window policy), OQ-C (cadence), OQ-D (moon step size). Resolved in
   Phase 1b.
5. **Tier-3 persistence:** on or off. A dial.
6. **Serving home.** CORS check determines whether a dedicated repo (H1)
   shares origin with the gallery under the custom domain. Five-minute
   check, do before locking. Resolved in Phase 1b.
```

Item #10 — change from the current Pyodide weight text to:
```
10. ~~**Pyodide package weight + cold-start.**~~ **Resolved.** Pyodide v314.0.2
    loads in ~4-10 seconds. Consent gate explains what's loading and gives
    users an explicit choice. Returning visitors skip consent (localStorage).
    The lightweight approach (Python for math, JS for figure) avoids loading
    the full `plotly` Python package in Pyodide. The full assembler approach
    (plotly in Python) deferred to Phase 2; may add to cold-start time.
```

---

## Change 7: §10 — Lineage additions

Add after the last bullet in the lineage list (after the "Opus 4.6 + Tony
data serving exploration" entry):

```
- **Fable 5 data serving analysis** (July 5, 2026): Broad-first analysis of
  data serving architecture. Five reframing findings: F2 canonical per-object
  storage collapses 1,501 pairs to ~190 objects; restructured cache ~36 MB
  (not 130 MB). Three-class split (analytic-capable / elements-degrading /
  trajectory-is-the-data). Three hybrid approaches (H1-H3). Serving home
  identified as configuration value, not architecture. Seven open questions
  (OQ-A through OQ-G). Six verification items for Phase 0.
  (`DATA_SERVING_BROAD_ANALYSIS.md`, built on `993dfd5` / `a6420bc`.)
- **Opus 4.6 + Tony convergence and build** (July 6, 2026): Reviewed Fable
  analysis; adopted F2, three trace types, two-class model (analytic vs
  cache-required, refined from Fable's three-class). Built Solar System
  Explorer as Phase 0 deliverable — `interactive.html` deployed to
  `palomasorrery.com/interactive.html`. Pyodide v314.0.2, mean element
  Keplerian computation, consent gate. Tested on desktop Chrome and iPhone
  Safari. Phase 0 proven. Phase 1b (data serving pipeline) identified as
  the gap between vocabulary (Phase 1a) and assembler (Phase 2). Gitignore
  updated for orbit cache files.
```

Add to "New in v8 → v9" decisions list:
```
*New in v9:*
- Phase 0 proven: Pyodide + NumPy + Plotly.js on static GitHub Pages (§5)
- Server/serverless resolved in practice: Pyodide (§7 #1)
- F2 canonical per-object storage adopted (§3a)
- Three trace types identified: actual positions, osculating at epoch, mean elements (§3a)
- Two data types to serve: osculating elements (tiny) + position vectors (rolling cache) (§3a)
- Analytical orbits sufficient for planets/asteroids/comets; moons require cache (§3a)
- Phase 1b inserted: data serving pipeline (§5)
- Consent gate for Pyodide loading (§5, §7 #10)
- Pyodide cold-start acceptable: ~4-10s, cached after first visit (§7 #10)
- interactive.html deployed as first exhibit (§2a)
- orbit_paths.json and orbit_cache/ added to .gitignore
```

Replace closing line:
```
Base: main @ `a6bfcfb` / gallery @ `a6420bc`. Phase 0 proven. Phase 1a
vocabulary delivered. Phase 1b (data serving pipeline) is the next design
track. Solar System Explorer live at palomasorrery.com/interactive.html.
```

---

# LEDGER UPDATES

## L-088 — STATUS: OPEN → DONE

```
#### [L-088] Gallery integration test (Phase 0)
<!-- L:088 status:DONE upd:2026-07-06 section:W.Done flag: rice:2/2/100/1 -->
- **What.** One-sided Pyodide test in the gallery. Proves the stack: Python
  computation in the browser on a static GitHub Pages site.
- **Done.** `interactive.html` deployed to `palomasorrery.com/interactive.html`
  (July 6, 2026). Pyodide v314.0.2 + NumPy computing Keplerian orbits from
  mean orbital elements, rendered by Plotly.js. Tested on desktop Chrome and
  iPhone Safari. Consent gate for first-time visitors (localStorage persistence).
  ~4-10 second load time, cached after first visit. Server/serverless resolved:
  Pyodide.
- **Supersedes:** Two-sided pilot (Dash vs Pyodide), matplotlib question — both
  dissolved by the v8 architectural pivot.
**Ref:** Master plan v9 §5 Phase 0; interactive.html @ `a6420bc`.
```

## L-079 — body update (status stays OPEN)

Replace the phasing block with:
```
- **Phasing (governed by master plan v9):**
  Phase 0: gallery integration test ✓ DONE (L-088, July 6, 2026).
  Phase 1a: shared spec skeleton + solar system vocabulary ✓ DONE (L-089).
  Phase 1b: data serving pipeline (L-0XX). Phase 2: solar system assembler +
  desktop migration tail. Phase 3: star assembler + cache. Phase 4: hybrid
  (exoplanets + Sgr A*). Phase 5: Earth system.
```

Replace the progress block with:
```
- **Progress:** Phase 1a vocabulary delivered (L-089, Fable 5, July 4, 2026).
  Phase 0 proven (L-088, July 6, 2026). Phase 1b (data serving pipeline) is
  the next design track. Master plan at v9.
```

Replace the key decision (open) with:
```
- **Key decision (settled):** server (Dash) vs serverless (Pyodide) -- Phase 0
  resolved this: Pyodide, proven July 6, 2026 (L-088).
```

## NEW: L-098 — Data serving pipeline (Phase 1b)

```
#### [L-098] Data serving pipeline (Phase 1b)
<!-- L:098 status:OPEN upd:2026-07-06 section:W.Active flag: rice:3/3/50/3 -->
- **What.** Build the bridge from Tony's desktop caches to the browser. The
  desktop has accumulated months of osculating elements and position vectors
  from Horizons. This pipeline makes that data available to the interactive
  gallery as web-servable files.
- **Deliverables:** (a) Export script: reads desktop caches, writes per-object
  canonical files (F2 storage). (b) Coverage index: JSON manifest of available
  objects, availability class, date coverage, step size, stored center, and
  osculating elements. (c) Serving home: resolve OQ-E (CORS check first),
  deploy first web cache. (d) Resolve OQ-A through OQ-G.
- **Design source:** Fable 5 broad analysis (DATA_SERVING_BROAD_ANALYSIS.md,
  July 5, 2026). Reviewed and refined by Opus 4.6 + Tony (July 6, 2026).
  F2 canonical storage adopted. Three trace types understood. Two data types
  to serve (osculating elements + position vectors). Analytical orbits
  sufficient for planets/asteroids/comets; moons require cache.
- **Gitignore:** `orbit_paths.json` and `orbit_cache/` added to .gitignore
  (July 6, 2026). Old pair-based cache preserved locally for desktop use.
**Gap:** Export script, coverage index, serving home, OQ resolutions.
**Ref:** DATA_SERVING_BROAD_ANALYSIS.md; master plan v9 §3a, §5 Phase 1b.
```

## NEW: L-099 — Solar System Explorer (interactive exhibit)

```
#### [L-099] Solar System Explorer interactive exhibit
<!-- L:099 status:DONE upd:2026-07-06 section:W.Done flag: rice:2/2/80/1 -->
- **What.** First interactive exhibit in the gallery. Pyodide + NumPy computes
  Keplerian orbits from mean orbital elements; Plotly.js renders 3D figure.
  Planet toggles, date picker, info panel, consent gate.
- **Done.** `interactive.html` deployed to `palomasorrery.com/interactive.html`
  (July 6, 2026). Tested on desktop Chrome and iPhone Safari. Consent gate
  explains Pyodide with explicit opt-in (localStorage persistence). Gallery
  dark-space aesthetic, Cormorant Garamond + DM Sans fonts, mobile-responsive.
- **Architecture:** Option C viewer (master plan §2a). `index.html` serves
  curated cards; `interactive.html` serves interactive exhibits. URL parameter
  (`?exhibit=`) ready for future exhibits.
- **Next iteration:** Plot refinements (Mercury color contrast, scale presets,
  outer planet zoom, additional controls). Feed back into the assembler design
  for Phase 2.
**Ref:** Master plan v9 §2a, §5 Phase 0; gallery @ `a6420bc`.
```

---

## END OF DRAFT — awaiting Tony's review before commit.
