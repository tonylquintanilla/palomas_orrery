# Section W Ledger Updates — July 6, 2026
# Apply these detail blocks to LEDGER_CONSOLIDATED.md, then run ledger_index.py.
# Four items: L-088 (DONE), L-079 (body update), L-098 (NEW), L-099 (NEW).
# Verify L-098 and L-099 numbers don't collide with existing entries.

---

## L-088 — STATUS: OPEN → DONE

#### [L-088] Gallery integration test (Phase 0)
<!-- L:088 status:DONE upd:2026-07-06 section:W.Done flag: rice:2/2/100/1 -->
- **What.** One-sided Pyodide test in the gallery. Proves the stack: Python
  computation in the browser on a static GitHub Pages site.
- **Done.** `interactive.html` deployed to `palomasorrery.com/interactive.html`
  (created `300ac30c`, updated `a85a4fa`, July 6, 2026). Pyodide v314.0.2 +
  NumPy computing Keplerian orbits from mean orbital elements, rendered by
  Plotly.js. Tested on desktop Chrome and iPhone Safari. Consent gate for
  first-time visitors (localStorage persistence). ~4-10 second load time,
  cached after first visit. Server/serverless resolved: Pyodide.
- **A/B fork resolved: B′.** `measure_plotly.html` timed full plotly-in-Pyodide
  cold-start on iPhone Safari WiFi: **2.1-3.3 s** (acceptance ≤15 s — passed at
  one-seventh). `import plotly.graph_objects` = 57-59 ms. Fable's convention-
  duplication analysis confirmed A's parallel-pipeline cost exceeds B′'s cold-
  start cost for a solo developer. B′ uses slim self-hosted wheel (~3.9 MB).
  Two-tier model: frozen A exhibits (instant) + data-backed B′ exhibits
  (shared engines, one codebase). Phase 0 closed.
- **Supersedes:** Two-sided pilot (Dash vs Pyodide), matplotlib question — both
  dissolved by the v8 architectural pivot.
- **Attribution gate (L-086):** Publicly reachable with inline "Data: JPL/NASA"
  credit. Ruled sufficient pending L-086.
**Ref:** Master plan v9 §5 Phase 0; gallery @ `4b086a6`.

---

## L-079 — body update (status stays OPEN)

#### [L-079] Shared assembler architecture (keystone — redefined)
<!-- L:079 status:OPEN upd:2026-07-06 section:W.Active flag: rice:3/3/50/3 -->
- **Redefined from:** "Headless scene core — decouple scene construction from
  Tkinter" (Fable 5 survey, July 2 2026).
- **Redefined to:** Build a shared assembler per domain. Both GUIs (tkinter
  desktop, web) are thin harvesters feeding the assembler. The assembler is new
  code written with the desktop orchestration as recipe reference. Original code
  archived for reference or reconstruction.
- **Four domains:** solar system (main build), stars, orbital parameters
  (educational showcase), Earth system (mixed KMZ + Plotly).
- **Phasing (governed by master plan v9):**
  Phase 0: gallery integration test ✓ DONE (L-088, July 6, 2026).
  Phase 1a: shared spec skeleton + solar system vocabulary ✓ DONE (L-089).
  Phase 1b: data serving pipeline (L-098). Phase 2: solar system assembler +
  desktop migration tail (requires A/B architecture decision). Phase 3: star
  assembler + cache. Phase 4: hybrid (exoplanets + Sgr A*). Phase 5: Earth
  system.
- **Per-domain migration tails:** desktop migrates onto each assembler right
  after it validates — not a single late migration. Delta-log discipline: any
  desktop orchestration change during the build gets a ledger tag
  "assembler-must-inherit."
- **Key decisions (settled):** site never fetches Horizons; three-tier cache all
  offline; GUI declares the envelope; web GUI is a fork not a replacement; one
  assembler per domain; architecture is S3/M3; assemblers read cache through
  index abstraction from day one; Phase 2 gate is scene equivalence not identical
  output; animation presets as curated tier-2 exports; scene spec is JSON-
  serializable from day one; animation/static consolidation verified (one
  assembler replaces both orchestrators).
- **Key decision (settled):** server (Dash) vs serverless (Pyodide) -- Phase 0
  resolved this: Pyodide, proven July 6, 2026 (L-088).
- **Key decision (settled):** architecture A (numpy + JS figure builder) vs B′
  (shared engines via plotly in Pyodide, slim self-hosted wheel). B′ measured
  at 2.1-3.3 s on iPhone WiFi (July 6, 2026). Two-tier model: frozen A
  exhibits + data-backed B′ exhibits.
- **Progress:** Phase 1a vocabulary delivered (L-089, Fable 5, July 4, 2026).
  Phase 0 closed (L-088, July 6, 2026). A/B fork resolved: B′. Phase 1b
  (data serving pipeline) is the next design track. Master plan at v9.
**Gap:** the master plan IS the gap document. Current phase: Phase 1b (L-098).
**Ref:** MASTER_PLAN_INTERACTIVE_GALLERY.md v9; PHASE1_SCENE_SPEC_VOCABULARY.md;
DATA_SERVING_BROAD_ANALYSIS.md; Fable 5 survey + L-079 deep dive; Opus 4.8
convergence handoff + reviews; Opus 4.6 + Tony convergence (July 3, July 6);
Fable 5 vocabulary session (July 4).

---

## NEW: L-098 — Data serving pipeline (Phase 1b)

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
  to serve (osculating elements + position vectors). Two classes for rolling
  cache (analytic-available, cache-required) plus spacecraft write-once.
- **Gitignore:** `orbit_paths.json` and `orbit_cache/` added to `.gitignore`
  @ `6368c87` (July 6, 2026). Old pair-based cache preserved locally for
  desktop use.
- **Independent of A/B fork:** the data pipeline is the same regardless of
  whether the consumer is a Python assembler (B) or a JS figure builder (A).
**Gap:** Export script, coverage index, serving home, OQ resolutions.
**Ref:** DATA_SERVING_BROAD_ANALYSIS.md; master plan v9 §3a, §5 Phase 1b.

---

## NEW: L-099 — Solar System Explorer (interactive exhibit)

#### [L-099] Solar System Explorer interactive exhibit
<!-- L:099 status:DONE upd:2026-07-06 section:W.Done flag: rice:2/2/80/1 -->
- **What.** First interactive exhibit in the gallery. Pyodide + NumPy computes
  Keplerian orbits from mean orbital elements; Plotly.js renders 3D figure.
  Planet toggles, date picker, info panel, consent gate.
- **Done.** `interactive.html` deployed to `palomasorrery.com/interactive.html`
  (created `300ac30c`, updated `a85a4fa`, July 6, 2026). Tested on desktop
  Chrome and iPhone Safari. Consent gate explains Pyodide with explicit opt-in
  (localStorage persistence). Gallery dark-space aesthetic, Cormorant Garamond
  + DM Sans fonts, mobile-responsive.
- **Architecture.** Architecture A (lightweight): Python/NumPy computes orbit
  geometry, JavaScript builds Plotly traces, `Plotly.newPlot()` renders.
  No plotly Python package in Pyodide. Frozen as an "instant tier" exhibit
  under the two-tier model (A/B fork resolved: B′ for Phase 2+ data-backed
  exhibits, A retained for frozen pedagogical demos). Option C viewer
  (master plan §2a): `index.html` serves curated cards; `interactive.html`
  serves interactive exhibits via `?exhibit=` parameter (hardcoded in v1).
- **Next iteration:** Plot refinements (Mercury color contrast, scale presets,
  outer planet zoom, additional controls). Feed observations into the A/B
  architecture decision at Phase 2 start.
**Ref:** Master plan v9 §2a, §5 Phase 0; gallery @ `a85a4fa`.
