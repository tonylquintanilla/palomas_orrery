## DRAFT — Section W entries for LEDGER_CONSOLIDATED.md
## Tony: patch into the ledger with any edits. RICE scores are proposals.
## New L-numbers start at L-085 (L-084 is the highest from Fable's survey).

---

## W. Web Publication Track

Governing document: `MASTER_PLAN_WEB_PUBLICATION.md` (repo root, when committed).
Architecture, phasing, and rationale live there; this section tracks work items
and status. Cross-references: L-026 (CRLF, companion to L-087), L-046 (presets),
L-068 (pipeline residuals), L-071 (Earth storytelling), L-074 (gallery culling),
L-083 (Plotly 6 / Kaleido — desktop only, not web).

### W.Index
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-079 | Shared assembler architecture (keystone) | OPEN | 1.5 | 2026-07-03 |
| ! | L-080 | Characterization harness (scene equivalence gate) | PROPOSED | 1.6 | 2026-07-03 |
| ! | L-085 | LICENSE to repo root | PROPOSED | 4.0 | 2026-07-03 |
| ! | L-086 | Attribution / credits page | PROPOSED | 2.8 | 2026-07-03 |
| ! | L-087 | palomas_orrery_helpers.py computation/GUI split | PROPOSED | 1.5 | 2026-07-03 |
| ! | L-088 | Two-sided pilot (Phase 0) | PROPOSED | 2.0 | 2026-07-03 |
| ! | L-089 | Scene-spec shared skeleton + solar system vocabulary (Phase 1) | PROPOSED | 1.5 | 2026-07-03 |
| ! | L-090 | Star cache inventory + wire format decision | PROPOSED | 1.0 | 2026-07-03 |
| ! | L-091 | Option E: unified front end (gallery viewer as single renderer) | DEFERRED | -- | 2026-07-03 |
| ! | L-092 | Embeddable scenes for educators | DEFERRED | -- | 2026-07-03 |
| ! | L-093 | Educational guided explorations (specs as curriculum) | DEFERRED | -- | 2026-07-03 |
| ! | L-094 | Community cache as commons (tier-3 shared asset) | DEFERRED | -- | 2026-07-03 |
| ! | L-095 | PWA / offline capability for classrooms | DEFERRED | -- | 2026-07-03 |
| ! | L-096 | Web orrery aesthetic / feel design conversation | DEFERRED | -- | 2026-07-03 |

### W.Prep -- before Phase 0

#### [L-085] LICENSE to repo root
<!-- L:085 status:PROPOSED upd:2026-07-03 section:W.Prep flag: rice:2/2/100/1 -->
- **What.** The MIT license file lives at `documentation/LICENSE.md` where GitHub
  cannot find it. The repo page shows no license badge; tooling reads the project
  as unlicensed. Move or copy to repo root.
- **Copyright year conflict.** The file says Copyright (c) 2024; README says
  (c) 2025-2026. Harmonize when moving.
- **Why now.** Cheapest half of the wide-release gate. The license choice already
  exists; this makes the existing claim true in form.
**Gap:** move file, harmonize year, verify badge appears. One commit.
**Ref:** Fable 5 survey (Front 2), master plan §6.

#### [L-086] Attribution / credits page
<!-- L:086 status:PROPOSED upd:2026-07-03 section:W.Prep flag: rice:2/2/70/1 -->
- **What.** One page (site + repo), one entry per data source, four fields each:
  what is used, where it appears in the project, the attribution string in the
  form the provider requires, and the license/redistribution terms with a link.
- **Source list (from repo evidence at HEAD):** JPL Horizons, JPL SBDB/CAD,
  Copernicus CDS / ERA5 / ERA5T, NOAA Coral Reef Watch, IPC and FEWS NET, HDX,
  OCHA FTS, SIMBAD (CDS), Gaia (ESA), Hipparcos, NSIDC, Mauna Loa CO₂ (NOAA
  GML/Scripps), HOT program.
- **Provider-required citation strings** (especially Gaia/ESA, CDS/SIMBAD,
  Copernicus) must be fetched at build time, not recalled.
- **Two constraints on hosting/distribution:** Copernicus licence terms and IPC
  terms of use are the most likely to constrain a hosted path. Neither kills any
  option; both need verification before wide release.
**Gap:** fetch each provider's required citation format; draft page; verify
redistribution terms for Copernicus and IPC. Gates any wide release including
the Phase 0 pilot if publicly reachable.
**Ref:** Fable 5 survey (Front 2), master plan §6.

#### [L-087] palomas_orrery_helpers.py computation/GUI split
<!-- L:087 status:PROPOSED upd:2026-07-03 section:W.Prep flag: rice:2/2/75/1.5 -->
- **What.** `palomas_orrery_helpers.py` imports tkinter directly (tk, ttk,
  messagebox, scrolledtext, lines 19-22) and carries three computation functions
  the assembler will need: `calculate_planet9_position_on_orbit` (@217),
  `rotate_points2` (@265), `calculate_axis_range` (@313). The computation
  functions themselves do not use tkinter.
- **Fix:** split computation functions into an import-clean module; leave GUI
  helpers in place. Or lazy-import tkinter so the module can be imported without
  a live Tk root.
- **Natural companion to L-026** (CRLF → LF on the same file, already open).
  Do both in one pass.
**Gap:** decide split strategy (new module vs lazy-import), implement, verify
no callers break. Closes the second seam identified in master plan §2.
**Ref:** Fable 5 review of v2 (finding 3), master plan §2/§6.

### W.Active -- current phase

#### [L-079] Shared assembler architecture (keystone — redefined)
<!-- L:079 status:OPEN upd:2026-07-03 section:W.Active flag: rice:3/3/50/3 -->
- **Redefined from:** "Headless scene core — decouple scene construction from
  Tkinter" (Fable 5 survey, July 2 2026).
- **Redefined to:** Build a shared assembler per domain. Both GUIs (tkinter
  desktop, web) are thin harvesters feeding the assembler. The assembler is new
  code written with the desktop orchestration as recipe reference. Original code
  archived for reference or reconstruction.
- **Four domains:** solar system (main build), stars, orbital parameters
  (educational showcase), Earth system (mixed KMZ + Plotly).
- **Phasing (governed by master plan):**
  Phase 0: two-sided pilot (L-088). Phase 1: shared spec skeleton + solar system
  vocabulary (L-089). Phase 2: solar system assembler + desktop migration tail.
  Phase 3: star assembler + cache. Phase 4: hybrid (exoplanets + Sgr A*).
  Phase 5: Earth system. Phase 6: web UI.
- **Per-domain migration tails:** desktop migrates onto each assembler right
  after it validates — not a single late migration. Delta-log discipline: any
  desktop orchestration change during the build gets a ledger tag
  "assembler-must-inherit."
- **Key decisions (settled):** site never fetches Horizons; three-tier cache all
  offline; GUI declares the envelope; web GUI is a fork not a replacement; one
  assembler per domain; architecture is S3/M3; assemblers read cache through
  index abstraction from day one; Phase 2 gate is scene equivalence not identical
  output; animation presets as curated tier-2 exports.
- **Key decision (open):** server (Dash) vs serverless (Pyodide) — Phase 0
  two-sided pilot resolves this.
**Gap:** the master plan IS the gap document. Current phase: prep (§6).
**Ref:** MASTER_PLAN_WEB_PUBLICATION.md; Fable 5 survey + L-079 deep dive;
Opus 4.8 convergence handoff + reviews; Opus 4.6 + Tony convergence (July 3).
RICE score 1.5 by arithmetic; strategically this is the keystone — everything
reprices after it. Tony's call on whether enabling value overrides the score.

#### [L-080] Characterization harness (scene equivalence gate)
<!-- L:080 status:PROPOSED upd:2026-07-03 section:W.Active flag: rice:1/2/80/1 -->
- **What.** A tests/ directory with golden-artifact capture for a fixed set of
  scenes. The harness gates every phase of the web publication initiative: "scene
  equivalence confirmed, render agrees" before each step.
- **Scene equivalence** (not identical output): same object set, positions match,
  display conventions honored (single-info-marker, AU in hover, marker symbols),
  plus Mode 5 (Tony's visual judgment). Trace ordering, naming, and layout
  details may legitimately differ. Concrete criteria are a Phase 1 deliverable
  (L-089).
- **Includes:** mainloop-suppression fixture (existing practice, extracted once),
  the three existing test files folded in, golden-artifact capture and comparison.
**Gap:** spec the harness for scene equivalence (criteria from L-089). Build.
Additive; no production modules edited.
**Ref:** Fable 5 survey (L-080 proposal); master plan §5/§6.

#### [L-088] Two-sided pilot (Phase 0)
<!-- L:088 status:PROPOSED upd:2026-07-03 section:W.Active flag: rice:2/2/50/1 -->
- **What.** Build the orbital parameter eccentricity visualization twice: Dash on
  HF Spaces, Pyodide on a static page. Same visualization, two delivery
  mechanisms. Tests hosting assumptions, cold-start vs first-load download, phone
  experience, ops feel.
- **Why two-sided.** The server-vs-serverless decision (§7 #1 in the master plan)
  is the largest remaining architectural choice. §1's "site never fetches" removed
  the CORS blocker on Pyodide. The orbital parameter viz is pure geometry — no
  cache, no data files — making it the cheapest possible test of both paths.
- **Downstream consequence.** If Pyodide wins, the web app is a static site —
  Fable's Option E (gallery viewer as unified front end) arrives nearly for free.
  If Dash wins, the gallery stays a sibling.
- **Attribution gate.** If either pilot is publicly reachable, keep unlisted until
  L-086 lands.
**Gap:** build both versions. Test on phone. Lessons-learned document +
server-vs-serverless decision before proceeding to Phase 1.
**Ref:** Fable 5 review of v4 (finding 10); master plan §5 Phase 0.

#### [L-089] Scene-spec shared skeleton + solar system vocabulary (Phase 1)
<!-- L:089 status:PROPOSED upd:2026-07-03 section:W.Active flag: rice:3/3/50/3 -->
- **What.** Design in conversation, not code.
  (a) The shared spec skeleton — what every spec has across all domains: domain
  tag, content type, display options.
  (b) The solar system vocabulary: objects, center, dates, display options,
  content type (static/animation).
  (c) The coverage index interface for the solar system domain.
  (d) Scene equivalence criteria — the concrete definition that shapes L-080's
  golden artifacts.
- **Other domain vocabularies are designed just-in-time** at the head of their
  own phases, informed by lessons learned here.
- **Decide:** is the spec serializable from day one? (Presets, shareable scenes,
  CI hang on this.)
- **Gate check:** confirm no shared-layer seams beyond the two named in §2.
**Gap:** design session(s). Gate: vocabulary document, index interface spec, and
equivalence criteria reviewed and stable before any assembler build.
**Ref:** Fable 5 L-079 deep dive (S2 vocabulary); master plan §5 Phase 1.

#### [L-090] Star cache inventory + wire format decision
<!-- L:090 status:PROPOSED upd:2026-07-03 section:W.Active flag: rice:1/1/50/1 -->
- **What.** The star cache (PKL files under `star_data/`) is gitignored, exceeds
  GitHub size limits, and is distributed via Releases for the desktop. It was
  built carefully from Gaia + Hipparcos with deduplication boundaries, within
  SIMBAD rate limits. Coverage: 101 light-years, apparent magnitude 9. Cannot be
  casually regenerated.
- **Inventory needed:** `du -sh star_data/` on Tony's machine — total size and
  per-file sizes. This determines where the star cache fits in the headroom
  budget and whether it can ship via Pages.
- **Wire format decision:** pickle is Python-version-coupled (fine for a Dash
  server, brittle for Pyodide, opaque to non-Python consumers). Convert to
  Parquet or JSON at cache-build time is the standard escape. Tied to the
  server-vs-serverless decision (L-088).
**Gap:** Tony runs `du -sh star_data/` and shares the inventory. Wire format
decision follows L-088 (Phase 0).
**Ref:** Fable 5 review of v4 (finding 1); master plan §4b.

### W.Deferred -- captured, not yet actionable

#### [L-091] Option E: unified front end
<!-- L:091 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- The existing gallery viewer (3,345 lines of JS) becomes the single front end
  for all channels: static gallery, scheduled scenes, server-built and
  browser-built scenes. A and B become interchangeable back ends. Every dollar
  of work on the viewer pays into all channels. Arrives nearly for free if the
  serverless (Pyodide) path wins in L-088.
**Ref:** Fable 5 survey (Option E); master plan §8.

#### [L-092] Embeddable scenes for educators
<!-- L:092 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- An iframe embed snippet per scene, so educators can put a working orrery view,
  HR diagram, or orbital visualization in their own pages. Nearly free given the
  viewer; large reach-per-effort.
**Ref:** master plan §8.

#### [L-093] Educational guided explorations (specs as curriculum)
<!-- L:093 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- Scene specs as curriculum — a notebook (JupyterLite or similar) that walks
  through "build a scene of the inner solar system, now change the center to
  Mars, now add Phobos" or "see how eccentricity transforms an orbit." The spec
  vocabulary becomes the teaching language. Cheap experiment once the assembler
  exists.
**Ref:** master plan §8.

#### [L-094] Community cache as commons
<!-- L:094 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- If tier-3 persistence is turned on, every fulfilled user request enriches the
  shared cache. Over time, the cache becomes a community-curated collection of
  interesting scenes — driven by curiosity, not just Tony's curation. Tied to
  the tier-3 persistence dial (master plan §7 #5).
**Ref:** master plan §7/#5, §8.

#### [L-095] PWA / offline capability for classrooms
<!-- L:095 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- Progressive Web App wrapper — installable and usable offline. Relevant for
  classrooms with unreliable connectivity. Modest effort if the architecture is
  static-first. Verify PWA constraints at build time.
**Ref:** master plan §8.

#### [L-096] Web orrery aesthetic / feel design conversation
<!-- L:096 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- The desktop is a power tool with 60+ toggles. The web version could be that —
  or something different. A curated explorer. A storytelling medium. An invitation
  to wonder. The envelope-declaring GUI implies curation over completeness. The
  orbital parameter viz is inherently educational. The Earth system carries a duty
  of care. How do these different voices come together in one web experience?
  Design conversation before Phase 6 (web UI).
**Ref:** master plan §8 Q4; Fable 5 review of v4.

### W.Cross-references -- existing items that interact with the web track

- **L-026** — CRLF → LF on `palomas_orrery_helpers.py`. Companion to L-087.
- **L-046** — Preset authoring. A saved scene spec IS a preset. Falls out of
  the vocabulary design (L-089).
- **L-068** — Static/animation pipeline residuals. Desktop cleanup, not web
  blockers, but worth closing.
- **L-071** — Earth system dated-scenario storytelling. Natural web narrative.
- **L-074** — Gallery culling. Headroom lever for Pages budget.
- **L-083** — Plotly 6 / Kaleido migration. Desktop + Instagram concern only;
  Kaleido is not needed for web (Plotly.js renders interactively in browser).
