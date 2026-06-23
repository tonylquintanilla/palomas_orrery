# LEDGER_CONSOLIDATED.md -- Paloma's Orrery Backlog

Tony Quintanilla, PE | Claude | Palomas Orrery Project
Consolidated: June 7, 2026 from handoff v28; supersedes all prior in-handoff
ledgers. Current HEAD: see git log (repo is the source of truth).
Module updated: June 2026 with Anthropic's Claude Sonnet 4.6, Opus 4.8 + Claude Fable 5
Review and RICE update Tony 6-21-2026

---

## Purpose and use

This is the single authoritative backlog for the Paloma's Orrery codebase
(~86k lines, ~100 modules) -- a Python/Plotly/Tkinter 3D solar system
visualization suite with a companion Gallery Studio pipeline and web gallery.
It tracks every open item, deferred decision, known bug, design question, and
new idea across the orrery refactor / Movement track and all active work streams.

**What this ledger is for.**

- *Session start:* Claude searches this file first -- open items, Tony's
  `**Tony:**` comments, and any `**Gap:**` notes -- before proposing work.
  It is the shared memory that survives session boundaries.
- *During a session:* blocks are updated in place as work lands. Status,
  gap, and ref fields change; new items are appended with the next L-handle.
  Nothing is renumbered; nothing is re-embedded from a handoff.
- *Between sessions:* Tony adds `**Tony:**` comments to any block as an
  async message to the next session -- questions, observations, things to
  verify visually. Claude reads them at session start and addresses them
  before building. See "Using and maintaining" below.
- *For the record:* closed items move to section C and stay there. The
  archive is not cleaned; it is the project's institutional memory. A future
  session (or Paloma) can reconstruct what was tried, what failed, and why.

**What this ledger is not.**

It is not a session log (that lives in handoffs and the git history). It is
not a design document (design emerges in conversation and lands in code and
comments). It is not a specification (the render is the spec -- Tony's eyes
are the gate). It is a backlog and a shared context artifact: the thing that
keeps the work from drifting between sessions.

**The round trip: protocol -> ledger -> handoff -> manifest -> code -> repo -> ledger.**

The ledger sits within a larger document stack. From the top down:

- *Protocol (the constitution):* the project instructions document the
  practical philosophy and operating conventions of the Tony-Claude
  partnership -- modes, criticality tiers, anti-patterns, technical
  standards, and the principles behind them. It is the load-bearing
  structure that everything else rests on. It evolves slowly and
  deliberately; amendments are proposed in conversation, ratified by Tony,
  and committed to the repo. Every session starts from it.
- *Ledger -> conversation:* an open item, a Tony comment, or a gap note
  becomes the seed for a design conversation. The conversation produces
  clarity -- options narrow, architecture simplifies, decisions land.
- *Conversation -> handoff:* what was done and what remains gets written
  into a handoff document. Most handoffs are session records: decisions
  made, code delivered, scope of what is still open. A handoff is a claim,
  not a verification -- the render and the repo are the facts. But some
  handoffs have a longer life: orbital mechanics, Gallery/Studio design, and
  similar foundational topics are maintained as durable design documents,
  updated in place as the domain evolves. These are reference artifacts, not
  session logs.
- *Handoff -> manifest (sometimes):* for complex multi-file builds, a
  handoff is distilled into a manifest -- specific, ordered instructions
  for code modifications, file by file, function by function. Not every
  handoff becomes a manifest; small or targeted work goes straight from
  handoff to code without one.
- *Code -> repo:* every change -- code and documentation alike -- is
  committed and pushed to the GitHub repo before the next session begins.
  The repo at HEAD is the source of truth for every turn. The SHA is the
  unforgeable confirmation that commit, push, and sync all landed; a
  matching remote HEAD is the round-trip check. Nothing builds on unverified
  ground.
- *Repo -> ledger:* once work is pushed and render-confirmed, the relevant
  ledger block is updated in place -- status, gap, ref, and any note worth
  keeping. New bugs, new ideas, and deferred observations get their own
  blocks. The ledger absorbs what the session produced and becomes the
  springboard for the next conversation.

The manifests and session-record handoffs are working documents -- they live
their life in a session and then become history. The durable handoffs, the
protocol, and the ledger are the persistent artifacts: they carry forward
what the project still needs to know, each at its own level of abstraction.

**Structure.** DETAIL blocks are the single source of truth. The INDEX below
is generated from them by `ledger_index.py` -- edit a block, re-run the tool.
Handles are append-only (L-###, next is L-062); a closed item keeps its handle
and moves to section C. Section layout:

- **A** -- cross-cutting / strategic items
- **PENDING** -- action items waiting on a specific gate (test, push, decision)
- **D.*** -- open work, organized by type (Movement, Priority, Structural, etc.)
- **E** -- AU-convention compliance cluster (standing convention sweep)
- **G** -- open questions / Tony's calls
- **H** -- Gallery / Studio track
- **C** -- reconciled done items (archive; do not re-do)

This file lives at the repository root alongside `MODULE_ATLAS.md` and
`PROVENANCE_AUDIT.md` as an authoritative generated-index artifact. The git
log carries the SHA history; this file carries the backlog.

## Verification convention (honesty about this ledger's own claims)

A handoff is a claim; the code is closer to fact. Each status carries a tag:

- `[verified @SHA]` -- checked against the live repo code in the named session.
- `[per chain; not re-verified]` -- carried from a handoff's prose; status is
  as the handoff stated, NOT re-confirmed against HEAD this session.
- `[render-gated]` -- correctness is a Mode-5 judgment, not settleable here.
- `[render-confirmed Mode 5]` -- Tony's eyes passed it on live data.

Items with no tag are administrative (tracks, actions) rather than code claims.

---

## ID + status convention

Live-backlog items carry an append-only handle **L-###** (assigned once, never
reused or reordered) so each is greppable for life. A pre-existing number is kept
inline as an alias: `[L-027 | #61]`, `[L-040 | #19]`. Section-C archive items keep
legacy numbers (no retroactive L-###). When an L-### item closes it keeps its
handle and moves to C.

The **DETAIL blocks are the single source of truth.** The INDEX zone is GENERATED
from them by `ledger_index.py` -- edit one block, regenerate; index and detail
cannot desync (module_atlas pattern).

- DISPOSITION (one per item): `DONE | PENDING-GATE | OPEN | BLOCKED | DEFERRED | PARKED | OBSERVED`
- EVIDENCE (separate axis, in the detail): `[verified @SHA] | [render-confirmed Mode 5] | [render-gated] | [per chain]`
- `**Gap:**` states the blocker/next-action on anything not DONE; `**Ref:**` points at the authority (handoff / SHA / code).
- `render-confirmed Mode 5` is EVIDENCE, not a disposition. It means Tony's
  eyes passed the output on live data -- a DONE item can carry it, and an
  OPEN item can carry it on a partial fix. It does not close an item.
- DONE items stay in their section until a housekeeping pass moves them to C.
  The trigger is `**Gap:** none -- move to section C`. Items in C are closed
  for the record; do not re-do them.

## Using and maintaining this ledger

**Author / update protocol.** Claude is the primary author of the ledger's
content: during a session it drafts and updates detail blocks (new items,
status changes, gap/ref notes), normally at the handoff that closes a session
and only when asked. Tony is the integrator and the only writer to the repo --
Claude has read-only GitHub access, so every change is reviewed and committed
by Tony. Updates are made IN PLACE: edit the relevant detail block; do not
re-embed a fresh copy. Handles are append-only -- the next new item is L-062;
a closed item keeps its L-### and moves to section C.

**ledger_index.py -- what it does, when to run it.** The DETAIL blocks are the
single source of truth; the INDEX tables below are GENERATED from them. After
any edit to a block -- a new item, a status change, an edited title or date --
regenerate the index so the board matches the detail:

    python ledger_index.py LEDGER_CONSOLIDATED.md

Run it from the repo root, where both files live (on Windows it is `python`,
not `python3`). It rewrites only the zone between the INDEX:START / INDEX:END
markers, so it is safe to re-run and never touches your prose. To validate
without rewriting -- catches duplicate handles or a malformed metadata line --
add `--check`:

    python ledger_index.py LEDGER_CONSOLIDATED.md --check

**Finding an item (Windows / VS Code).** Every item is keyed by its L-handle,
so you never scroll. In VS Code, Ctrl+F opens Find in this file -- type an
L-handle (e.g. `L-012`) to land on both its index row AND its detail block;
type a legacy alias (`#61`, `19.3`) to find it by its old number. To LIST
matches rather than jump to them -- e.g. every open item -- use the Search
panel (Ctrl+Shift+F) and search `| ! |` (the gap marker); it shows all hits at
once. PowerShell equivalent, if you prefer the command line:
`Select-String -Path LEDGER_CONSOLIDATED.md -Pattern 'L-012'`.

**Default path (Run button / bare invocation).** `ledger_index.py` now falls
back to `LEDGER_CONSOLIDATED.md` in its own folder when called with no
argument -- so pressing the Run button in VS Code, or typing bare
`python ledger_index.py`, just works. Pass an explicit path to override;
`--check` still works with or without an explicit path.

**Tony's comment convention -- async notes between sessions.** Any DETAIL
block may carry a `**Tony:**` paragraph between the narrative and the
`**Gap:**` line. These are free-form: questions, second-thoughts, design
observations, things to verify visually. The metadata parser ignores them,
so they cannot break the index. At the start of a review session Claude
searches for every `**Tony:**` block and addresses them before building.
Date-stamp is optional but useful: `**Tony (2026-06-17):**`. A `**Note:**`
tag (no date required) works the same way for factual addenda from either
side. For a free-floating thought with no obvious home, either attach it to
the nearest relevant item or open a new `D.LooseEnd` item for it -- floating
notes get lost; capturing on first mention is the rule.

**RICE scoring -- prioritization for planning.** Each DETAIL block's
metadata line can carry an optional `rice:R/I/C/E` field at the end:

    <!-- L:999 status:OPEN upd:2026-06-18 section:D.Movement flag: rice:3/3/100/2 -->

The four dimensions, adapted for this project:

    R (Reach/Value)    Educational or visual value
                       3 = core experience  2 = gallery quality  1 = internal hygiene
    I (Impact)         Magnitude of improvement
                       3 = new capability  2 = meaningful  1 = polish  0.5 = marginal
    C (Confidence %)   Scope clarity
                       100 = ready to build  80 = mostly scoped  50 = needs design  25 = speculative
    E (Effort)         Sessions to complete
                       0.5 = quick fix  1 = one session  2 = two sessions  3 = three+

    Score = R x I x (C / 100) / E

Separator is `/` (not `.`) so decimal values like `0.5` work. Omit the
field entirely or use `rice:-` for unscored items -- both display as `--`
in the INDEX. `ledger_index.py` parses the field, computes the score, and
sorts scored items to the top of their section (descending); unscored
items follow by L-number. Completed items carry their score into section C
as an archive of the prioritization thinking -- no cleanup on close.

<!-- INDEX:START (generated by ledger_index.py -- do not edit this zone by hand) -->

## INDEX (generated -- status board; edit DETAIL blocks, then re-run ledger_index.py)

*44 live items; 40 need attention (`!`); 44 RICE-scored. Find an `L-0NN` handle (Ctrl+F in VS Code) to jump to any item; search `| ! |` to list every gap. See "Using and maintaining this ledger" above for details.*

### A
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-065 | European heat wave heat map (Earth System track) | OPEN | 4.8 | 2026-06-22 |
| ! | L-001 | Food Insecurity (Earth System track) | OPEN | 4.0 | 2026-06-22 |
| ! | L-060 | ENSO Standalone Chart (Earth System track) | OPEN | 2.7 | 2026-06-18 |
| ! | L-063 | Orrery GUI Note text update | OPEN | 2.0 | 2026-06-21 |
| ! | L-002 | Protocol -> Skills refactor (process/tooling) | OPEN | 1.5 | 2026-06-22 |
| ! | L-062 | README refresh -- fold in handoff + ledger developments | OPEN | 1.5 | 2026-06-21 |

### D.Movement
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-008 | v24 sec5 precision batch (low-risk) | OPEN | 1.0 | - |
| ! | L-061 | Magnetosphere-dipole frame coupling / seasonal roll | OPEN | 0.2 | 2026-06-21 |

### D.Priority
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-012 | Osculating pre-fetch false-provenance messages | OPEN [CRIT] | 3.6 | 2026-06-21 |
|  | L-013 | Mercury 2019-epoch anomaly | DEFERRED | 0.1 | 2026-06-15 |

### D.Structural
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-064 | Provenance-scanner format sweep -- Earth System family | OPEN | 3.0 | 2026-06-22 |
| ! | L-026 (#9) | palomas_orrery_helpers.py CRLF -> LF | OPEN | 2.2 | 2026-06-18 |
| ! | L-027 (#61) | Platform Neutrality (SystemButtonFace) | OPEN | 2.2 | 2026-06-18 |
| ! | L-025 (#N7) | Reduced to custom-geometry inline markers only | OPEN | 1.5 | 2026-06-18 |
| ! | L-028 | ASCII em-dash violation, comet_visualization_shells.py L257/505/519 | OPEN | 1.0 | 2026-06-11 |
| ! | L-015 (#5) | _info import cleanup (~89+87 imports, 2 files) | OPEN | 0.9 | 2026-06-18 |
| ! | L-016 (#6) | Archive dead shell functions | OPEN | 0.9 | 2026-06-18 |
|  | L-020 (#26) | CUSTOM_SHELLS tooltip verification | DONE | 0.9 | 2026-06-22 |

### D.Cosmetic
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-035 | Solar shell hovertext <br> vs 
 context mismatch (C6b) | OPEN | 4.0 | 2026-06-11 |
| ! | L-032 (#41) | Sun legend ordering (ordered dispatch iteration; no manual fix) | OPEN | 1.5 | - |
| ! | L-033 | Comet plotted-period trace visibility (line weight/color; O6b) | OPEN | 1.5 | 2026-06-10 |
| ! | L-034 | Center-body hover "Distance to Center Surface" negative-radius formatting | OPEN | 1.5 | 2026-06-21 |
| ! | L-030 (#17) | GEO info-marker position | OPEN | 1.0 | - |
| ! | L-031 (#18) | Uranus gossamer ring visibility | OPEN | 0.9 | - |
| ! | L-037 | WARNING: Unknown object type 'satellite' (spurious; handled downstream) | OPEN | 0.9 | 2026-06-15 |
| ! | L-038 | Psyche encounter hardcoded fallback distances lack # Source | OPEN | 0.5 | - |

### D.Feature-A
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-040 (#19) | Plot-cube control parity + scaling/camera comprehensive review | OPEN | 1.5 | 2026-06-13 |
| ! | L-039 (#23) | Earth ionosphere shell | OPEN | 1.2 | 2026-06-21 |
| ! | L-042 (#20/N5) | Shell-resolution GUI control (20/N5) + Fly-to view scaling (49) | OPEN | 0.5 | 2026-06-11 |
| ! | L-043 | Exoplanet/binary synthetic objects hit Horizons fetch (id_type rejected) | OPEN | 0.4 | 2026-06-16 |

### D.Feature-B
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-044 (#22) | Satellite (and minor-body) internal-structure shells | OPEN | 2.7 | 2026-06-21 |
| ! | L-045 (#N14) | Miranda inclination tooltip | OPEN | 0.9 | - |

### D.Feature-C
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-046 (#N6) | Studio encounter-generator -> preset-authoring capability (refactor + Artemis redo; coupled, two repos) | OPEN | 2.2 | 2026-06-21 |
| ! | L-048 (#21/51) | Animation track 21/51 -- core complete pending the v4 gate | PENDING-GATE | 1.5 | 2026-06-11 |
| ! | L-017 (#7) | Tooltip rewiring globals() -> config fields | OPEN | 1.0 | 2026-06-21 |
| ! | L-047 (#N10) | Note-composition structural refactor (behind N6) | OPEN | 1.0 | - |
| ! | L-014 (#2) | Asteroid-belt migration decision | OPEN | 0.4 | 2026-06-20 |

### D.Parked
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
|  | L-050 (#N9) | white -> red orbit-marker switch (osculating marker intentionally stays white) | PARKED | 1.0 | - |
|  | L-049 (#N8) | Comet info-marker superposition cluster | PARKED | 0.5 | - |

### D.LooseEnd
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-051 | Uranus pole-value prose inconsistency (Dec -15.10 vs stray -15.18) | OPEN | 0.7 | 2026-06-21 |

### E
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-052 | AU-convention compliance sweep (GEO altitude hover missing AU; km+AU on all new hover) | OPEN | 0.5 | - |

### G
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-053 | AU-convention sweep (section E): keep open, revisit | OPEN | 0.8 | 2026-06-07 |
| ! | L-056 | Phase 4 residuals: stale O2/O3 console wording; apsidal_markers em-dashes; MAPS per-frame wiring deferred | OPEN | 0.5 | 2026-06-12 |

### H
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-058 | Open Studio items (May-5 handoff, checked @2f40d9d) | OPEN | 1.5 | 2026-06-08 |

<!-- INDEX:END -->

---

## DETAIL / RECORD

## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)

#### [L-001] Food Insecurity (Earth System track)
<!-- L:001 status:OPEN upd:2026-06-22 section:A flag: rice:3/3/90/2 -->
- **Food Insecurity -- Sudan, Current period; design re-converged 2026-06-22.**
  Earth System track. Phase-1 design now locked tighter AND simpler than the
  original manifest. Old work (period7_food_insecurity.html + pre-rethink
  handoffs) is REFERENCE ONLY, not a building block -- starting fresh.
- **Source (SUPERSEDES the 2026-06-21 HDX-mirror call):** IPC Mapping Tool
  no-key GeoJSON (ipcinfo.org/ipc-country-analysis/ipc-mapping-tool/). IPC-native
  geometry + full per-area phase attributes in one file, NO key -- the IPC key is
  no longer needed at all. Fetched + inspected 2026-06-22
  (IPC_SD_A_87143417_2026-06-22.geojson): 228 features (189 area polygons, 39
  call-out points), one polygon per analysis area carrying mapped phase, full
  phase1-5 population/pct, evidence level (confidence_level), assistance level
  (hfa_value), risk_of_famine flag, period window. Provenance UPGRADES to "IPC,
  IPC Mapping Tool" (not "IPC via HDX", not FEWS NET -- FEWS is IPC-compatible
  but NOT IPC consensus, by its own statement). HDX dataset demoted to scriptable
  backup (ipc_sdn.geojson + CSVs, stable resource IDs) and the route to the
  deferred historical arc (area_long CSV spans 2019-2027). SANDBOX WALL: ipcinfo
  + data.humdata.org bot-block automated fetch -- Tony fetches manually (the
  coral arrangement, confirmed working this session).
- **Scope: Phase 1 = CURRENT PERIOD ONLY (Feb-May 2026).** Full national coverage
  (195 localities). Projections (Jun-Sep 2026 lean, Oct 2026-Jan 2027 harvest;
  PARTIAL, 56/195 localities; IPC's own "do not compare across periods" caveat)
  DEFERRED to a deliberate second layer. Current-only is both the honest data
  scope (no comparability hazard; not-analysed collapses to one null feature,
  Abyei PCA) and the right Reel length.
- **Popup shows the FULL phase breakdown, not just mapped phase.** Each balloon
  carries phase1-5 population/pct INCLUDING phase5_population (Catastrophe). This
  is the structural fix for the mapped-vs-population error: the map color is the
  highest severity affecting AT LEAST 20% of an area's population, so sub-20%
  Phase-5 populations hide behind a P4 color (23 areas carry Catastrophe pops,
  all mapped P4). Legend STATES the 20% rule so the glance is honest.
- **Drivers = single NATIONAL card, IPC voice:** conflict; displacement/
  immobility; high food prices; health/WASH collapse; limited humanitarian
  access. Includes IPC's OWN naming of the Middle East -> fuel/food/fertilizer
  channel -- the Iran-war test case resolved per the handoff rule (transcribe
  IPC's framing, never author the linkage; reader makes the Hormuz connection).
  No per-area driver prose invented.
- **Totals TRANSCRIBED from the IPC report, NEVER summed from polygons.** Naive
  GeoJSON sum overcounts (28M vs IPC's 19.5M P3+; 185k vs 135k P5) because
  IDP-settlement units overlap host localities. Headline figures (19.5M in P3+,
  ~135k in Catastrophe) come from IPC's text; polygons are for per-area color +
  popups only.
- **Corrected section-10 framing (replaces the stale Sept-2025 spot-check):** NO
  area mapped Phase 5; ~135k in Phase 5 (Catastrophe) [N/S Darfur, S Kordofan];
  El Fasher/Kadugli "not directly comparable" this round (data did not allow
  town-level disaggregation -- a data gap, NOT an improvement; concerns remain
  high); 14 areas at risk of Famine in the Jun-Sep worst-case projection.
  Verification = "phases render where the CURRENT release puts them," no
  hardcoded area-to-phase claim.
- **Two-tier on-layer text (NEW principle):** on-layer text splits by how words
  get authority. TRANSCRIBED tier (IPC's verbatim words -- drivers, citation,
  period, analysis date) is safe by construction. COMPOSED tier (sentences we
  write because no single IPC line says them -- e.g. "no area mapped Phase 5 but
  ~135k in Catastrophe") is high-stakes: hardcode it as a framing-layer text
  element, BUILD it in the generator with each numeric token carrying a
  `# Source:` within scanner lookback (not pasted as a finished string), and it
  MUST trip provenance scanner Tier-1 before push -- cite-or-remove, never
  cite-to-clear. (See L-064 for the family-wide sweep.)
- **Venue: one KMZ, two showings.** Live in the gallery (palomasorrery.com) and
  as a narrated Reel (60-90s) on instagram (palomas_orrery). The Reel ROUTE
  (national figure -> the P4 orange -> the hidden Catastrophe -> national drivers
  -> close) is a first-class design input; narration reads FROM the on-layer
  framing text, closing the ad-lib gap (words said == words on the layer ==
  sourced).
**Gap:** design not yet fully written down. NEXT: (1) [done this session] ledger
revised; (2) write design handoff v2 as the design-session plan; (3) then
manifest v2 (executable spec) -- decide now-vs-next-session; (4) then code from
the manifest. Still to SOURCE before build: exact IPC recommended-citation string
(lift verbatim from the report); IPC official phase hex ramp (color guidance --
GeoJSON carries no colors, do not recall); confirm provenance_scanner.py
traverses the food-insecurity generator's framing-layer display path at HEAD.
Read the live Earth System KMZ pattern from the repo at HEAD before writing
integration (do not prescribe from the manifest).
**Ref:** design base 2026-06-22 (HEAD f1834dc); IPC Mapping Tool GeoJSON
(IPC_SD_A_87143417_2026-06-22.geojson, analysis "SD February 2026"); IPC Sudan
Special Report Feb2026-Jan2027 (published 2026-06-03, data to 2026-04-10, Natl
IPC Technical Working Group); supersedes HANDOFF_food_insecurity_design_v1.md +
MANIFEST_food_insecurity_sudan_first_cut.md (de12f56, now reference). Pending:
design handoff v2, manifest v2.

#### [L-002] Protocol -> Skills refactor (process/tooling)
<!-- L:002 status:OPEN upd:2026-06-22 section:A flag: rice:3/3/50/3 -->
- **Protocol -> Skills refactor (process/tooling, not orrery code).** Lift the
  task-triggered PROCEDURE/CONVENTION layer of Part 3 into Anthropic SKILL.md
  files (load on demand); keep the JUDGMENT layer (modes, criticality,
  anti-patterns, Foundation, double-helix) resident. Sketch-first /
  design-before-build -- the framing below is the leg-up from the v3.29 cleanup,
  NOT the design itself.
- **Sorting principle (the design lever):** a skill only helps if its trigger
  fires at the moment of need. So the cut is NOT QUALITY-vs-CRITICAL and NOT
  procedure-vs-judgment -- it is "does the moment-of-need announce itself in the
  task?" Task-coupled guidance (writing hover text -> AU convention) extracts
  cleanly; checkpoint guidance that must fire UNPROMPTED (session start, every
  delivery) can't be a skill -- nothing in the request triggers it -- so it stays
  resident by standing instruction.
- **Three buckets (v3.29 Part-3 inventory; illustrative, not the final set):**
  (A) EXTRACT -- task-triggered conventions/procedures: docstring standard,
      single-info-marker, marker-symbol, hover-AU, 3D-axis, Horizons centers,
      provenance-scanner mechanics, a safe-editing bundle (bottom-up + binary-mode
      + file-encoding), platform-neutrality, credit-line, barycenter.
  (B) RESIDENT POINTER + skill body -- CRITICAL but task-coupled: Agentic Pre-Test
      (a resident one-liner fires it; the commands + live-dispatch smoke test live
      in the skill).
  (C) STAY RESIDENT -- checkpoint CRITICAL gates, never extract: SHA round trip,
      uploads-before-project, enumerate-uploads, verify-base, verify-execution,
      check-parallel-pipelines, fetched-vs-recalled, show-the-envelope; + Parts 1/2/4.
- **Fable-5 caveat (packaging, not content):** skill content is model-invariant; a
  larger-scope model only changes the ECONOMICS of carrying Part 3 resident. Design
  the boundary now (cheap, reversible); defer the extraction build until the
  platform is known -- a bigger context may pull some (A)/(B) items back to (C).
  Build risks rework; design does not.
- **Where the deferred design work actually is:** writing each skill's TRIGGER
  DESCRIPTION (the SKILL.md description is what fires it) + the bundling decisions
  (how many skills, what groups). That is the sketch-first session.
**Gap:** deferred design session (possibly post-Fable): finalize the (A)/(B)/(C) sort, write each skill's trigger description, decide bundling. Hard constraint: bucket (C) gates stay resident. RICE holds at 3/3/50/3 until the design lands.

#### [L-060] ENSO Standalone Chart (Earth System track)
<!-- L:060 status:OPEN upd:2026-06-18 section:A flag: rice:3/3/75/2.5 -->
- **ENSO standalone gallery chart (design locked, build next session).** Earth
  System track, not the orrery refactor. Single-unit (deg C) chart leading with
  RONI so El Nino / La Nina state reads honestly in a warming climate; ONI as a
  thin overlaid line (keeps the RONI-ONI divergence visible, anchors the
  forecast). RONI drawn as a FILLED-to-zero seesaw -- red El Nino above, blue
  La Nina below (recognizable, gallery-striking; the Economist / Climate Brink
  use the same idiom and also lead with RONI -- external validation of the
  RONI-first call). 2026 forecast as a CALIBRATED envelope: plume mean +
  skill-scaled Gaussian (official IRI product; widens at the spring barrier;
  upper edge is where the "strongest ever" tail lives, shown as possibility not
  promise) -- NOT a single median line (the Economist chart's grey median spike
  is exactly what we reject). Plume is ONI / Nino-3.4 basis, hung off the ONI
  line, basis STATED IN HOVER (the Economist chart leaves forecast basis
  unstated -- our fix). Fallback if IRI skill-calibration params are not cleanly
  fetchable: labeled model-spread band ("model spread, not a calibrated
  probability"). 2026 event shown NOW, PROVISIONAL with preliminary/developing
  flagging (Western Heatwave convention) -- already front-page news. Phase
  shading COMPUTED from RONI (+/-0.5, 5 overlapping seasons); strength from RONI
  magnitude, never a recalled label. ENSO<->energy-imbalance told as MECHANISM:
  a PLOTLY-DRAWN charge/discharge schematic (no time axis) + cited physics in
  the "i" card -- NOT a data overlay, NOT a computed covariance. EEI stays drawn
  once on the energy-imbalance chart (no parallel pipeline); cards cross-link.
  No traces beyond RONI + ONI + thresholds + phases + today + plume (Tony: let
  it land). Data: RONI.ascii.txt CONFIRMED fetchable; ONI URL + IRI plume parse
  TBV at build. Mobile + desktop variants from the start. Design base SHA 799d7da.
  Phase 2 (DEFERRED, coupled, do NOT lose): targeted Mode-1 pass on
  energy_imbalance.py -- narrative correction (El Nino imbalance dip led by
  OUTGOING LONGWAVE, NOT primarily "reflects more sunlight"; fold in RONI
  rationale) + add 2026 band provisional-with-flagging. Split to own L-handle if
  it risks leaking when L-060 closes.
**Gap:** build next session. One genuine open call left (build, not design): confirm ONI file URL + IRI plume parse / skill-calibration params at HEAD before hardcoding (cached-CSV fallback if scrape unstable; model-spread band fallback if calibration params unavailable). Provenance-scan new module (Tier-1=0) before push. Resolved: plume=calibrated Gaussian envelope; schematic=Plotly; 2026 band=provisional-now; no extra traces.
**Ref:** ENSO_chart_spec.md v2 (design spec, this session); cross-ref L-001 (Food Insecurity, same Earth System track); energy_imbalance.py (Phase 2 target).

#### [L-062] README refresh -- fold in handoff + ledger developments
<!-- L:062 status:OPEN upd:2026-06-21 section:A flag: rice:2/1/75/1 -->
- **README review/refresh.** Review the repo README against its last update and
  fold in developments captured since in the handoffs and this ledger (Movement
  track complete, animation engine, item-19.3 axis control, shell-consolidation
  refactor complete, Gallery/Studio round trip, Earth System track). Goal: a
  current public-facing description matching what the code actually does. Paired
  with L-063 (in-GUI Note) -- both are user-facing text that has drifted from
  project state.
**Gap:** read current README at HEAD; draft a refresh from the handoff/ledger record; Tony reviews + commits. Scope-light, mostly assembly not design.

#### [L-063] Orrery GUI Note text update
<!-- L:063 status:OPEN upd:2026-06-21 section:A flag: rice:2/1/50/0.5 -->
- **Update the Note in the orrery GUI.** The in-app Note text (palomas_orrery.py)
  has drifted from current project state; refresh it to reflect current scope.
  Paired with L-062 as the user-facing text refresh. Small Mode-1 edit once the
  new wording is decided.
**Gap:** decide the new Note wording (light design -- what should it say now?), then a Mode-1 snippet into palomas_orrery.py (grep the current Note string first). Could alternatively live in D.Cosmetic; kept in A, paired with L-062.

#### [L-065] European heat wave heat map (Earth System track)
<!-- L:065 status:OPEN upd:2026-06-22 section:A flag: rice:3/3/80/1.5 -->
- **European heat wave 2026 -- new heat map, reuses the existing ERA5 framework.**
  Earth System / stressors family (the "heat" member named in the food-insecurity
  handoff). A dated temperature heat map of the ongoing 2026 European heat wave,
  built on the existing ERA5/Copernicus heat-map chassis -- new region + date
  config, NOT a new pipeline. TIMELY: a second, hotter wave began 22 Jun 2026
  (Western + Central Europe), deaths reported and June records falling; gallery +
  Reel value is time-sensitive while it is in the news.
- **Data = Fetched, trusted:** ERA5 2m temperature via Copernicus CDS (the live
  pipeline). Note the ~5-day near-real-time lag -- "now" honestly means up to ~5
  days back, so the layer is dated / pinned / deliberately re-pulled (no live
  auto-update), same as the family. Confirm exact dates, extent, and peak values
  at fetch time; do NOT recall breaking-news numbers (they go stale fast).
  Copernicus Sentinel-3 LST is the near-real-time surface-temperature alternative
  if a snapshot is wanted alongside the air-temp reanalysis.
- **Human-impact text = composed/transcribed tier (two-tier on-layer text; see
  L-001 / L-064).** If the layer carries any casualty / health-alert / attribution
  text, it is transcribed from an authority (national met services, EU Copernicus
  C3S, WMO, health agencies, WWA-style attribution), per-number `# Source:` within
  scanner lookback, Tier-1 visible, cite-or-remove. Climate-change attribution
  belongs to the cited authority in its voice -- we never author it; the reader
  connects it to the family thesis. Breaking-news tolls are volatile and
  contested -- transcribe a dated, sourced figure at build or omit.
**Gap:** scope at build: pick region window + date(s) (current wave from 22 Jun
2026, or the May + June arc), reuse the ERA5 heat-map generator (read the live
pattern at HEAD first), decide whether any impact text appears and if so wire it
through the composed-tier discipline. Confirm provenance scanner coverage of the
heat-map generator's display path (the L-064 question, asked locally).
**Ref:** existing ERA5/Copernicus heat-map framework; Copernicus CDS (ERA5 2m
temp) + Sentinel-3 LST; EU Copernicus Climate Change Service (C3S); L-001 + L-064
(two-tier on-layer text + scanner-format sweep). Current-event context: 2026
European heatwaves (record June temps; deaths reported across FR/UK/IE/ES/AT/DE/
SI), retrieved 2026-06-22.

## PENDING ACTION (Tony-side)

## B. STRATEGIC STATUS

**The shell-consolidation refactor is COMPLETE** (per v23 headline; all 13 bodies
route through SHELL_CONFIGS / CUSTOM_SHELLS -> create_celestial_body_visualization
-> build_sphere_shell -> create_info_marker). The project is in
cleanup-and-close, not mid-refactor. (June 11: the create_planet_visualization
wrapper is now RETIRED -- zero pipeline callers; see section C.)

**Animation refactor (21/51): CORE TRACK DELIVERED, final gate pending.**
- Phase 1 (frame fence + sun threading + first-frame sync) -- DONE
  `[render-confirmed Mode 5 @7977a11, June 10]`. 88-94% file reductions.
- Phase 2 (scene-assembly consolidation 2a-2d) -- DONE
  `[render-confirmed Mode 5, June 10-11]`. Closed N3 + O5 + O6(a); two fixes
  shipped during testing (incl. osculating labeling, idealized_orbits)
  `[per chain]`.
- Phase 2.5 (wrapper retirement, 3 sites) -- DONE
  `[render-confirmed Mode 5 via Session A gate, June 10]`.
- Phase 3 Session A (design doc + 3a + budget harness) -- DONE
  `[render-confirmed Mode 5, June 10]`. Rebuild-as-universal adopted;
  gate 5(a) bytes PASSED at measured reduction.
- Phase 3 Session B (per-frame engine + axis/cone/indicator + greyed-legend
  disclosure) -- CONDITIONALLY render-confirmed June 11: engine allocates,
  rebuilds, budget-reports correctly; riding behavior visually confirmed at
  planet-centered scale; solar-system-scale visual confirmation blocked by a
  TOOLING gap (camera tracking; item 19), not an engine defect.
- Phase 3 Session C (barycenter Sun fix, console-spam fix, opt-in per-frame
  comet tails, sodium tail, U+N bow-shock disclosure, one-line auto-scale) --
  DELIVERED and PUSHED @7b71c29, `[render-gated on protocol v4]`.

**Movement 1 (bow shocks + magnetosphere nest) COMPLETE** (v24). `[per chain]`

**Movement 2 (pole-frame consumers) COMPLETE pending one gate:** rotation-axis
primitive (11 bodies, v26) and dipole cones (Uranus/Neptune, v27) done; the
v27 "animation gap" resolved -- center bodies confirmed O4 (June 10), and
NON-center bodies now animate via the Phase-3 engine (Session B). The
bow-shock hover disclosure remainder was delivered in Session C
`[render-gated C5]`.

**N15 ring-plane migration COMPLETE** (v25). `[per chain]`
**Analytical moon-orbit retirement DONE** (v25). `[per chain]`
**Provenance Tier-1 = 0** -- RE-CONFIRMED June 11 post-campaign
`[verified @d9460e2: PROVENANCE_AUDIT.md, 109 files scanned, 497 findings,
Tier-1 FIX NOW = 0]`. The clean mark held through the entire animation
refactor.

**Tony:** This item does not have an L-number or header and should be closed and moved to C.

---

## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)

From v23 DONE table (closed by D1/D2/D3.1/C1; `[per chain]`):
1 Sun config extraction; 4 sun_position wiring (static); 10 double sun direction
indicator; 11 Earth/Jupiter magnetic_tilt_deg; 12 Neptune poles -> square-open;
14 Neptune debug print; 15 Neptune function-local imports; 16 Venus hover text;
25/42 Mars magnetosphere info marker; 27 hover \n -> <br>; 29 Sun call-site
switchover; 31 sun/corona Tkinter format; 32 Sun marker borders; 33 photosphere
mesh3d; 34 photosphere hover truncation; 35 corona_from_distance retired; 43/44
Uranus/Neptune magnetosphere hover truncation; 45 Neptune radiation labelling;
46 Neptune FAC labelling; 47a/47b Neptune arc / Lassell+Arago superimposed;
48 Mercury sodium-tail sun_position; 50 sun-direction per-body legendgroup;
54 hovertext/legendgroup sweep; 55 solar shell naming; 56 crust/cloud
legendgroup; 57 Neptune double-leader; 58 MAPS placeholder legendgroups;
59 create_neptune_magnetic_poles orphan; 60 Moon Hill Sphere prefix;
N1 osculating-marker "color not defined"; 36/39 Neptune/Uranus provenance Tier-1
display strings; 53 Neptune magnetic-center marker -> square-open;
N2-orphan Uranus dipole SIGN closed by convention.

Closed SINCE v23 (Movement chain + verified):
- **24 Bow shocks (all 8)** -- DONE (v24). **Magnetosphere nest sizing** -- DONE
  (v24). **U3 Uranus 105-deg fudge** -- RETIRED `[verified @76c330e]`.
  **N15 ring-plane migration** -- DONE (v25). **Analytical moon-orbit
  retirement** -- DONE (v25). **Rotation-axis primitive** (11 bodies) -- DONE
  (v26). **N13 dipole sweep-cone** -- DONE (v27). **N12 pole markers** -- DONE
  (June 7). `[all per chain unless tagged]`
- **Double 'Sun' in the center dropdown** -- DONE `[verified @730b2bf, L9296]`.
- **Duplicate 'Sun' key in CUSTOM_SHELLS** -- DONE `[verified @730b2bf via AST]`.
  (Full root-cause narratives for both retained in the June-8 entry of the
  prior ledger edition; reachable in git history.)
- **21/51 PHASE 1** (frame fence + sun threading + first-frame sync) -- DONE
  `[render-confirmed Mode 5 @7977a11, June 10]`. P1 4818->271 KB (94.4%),
  P2 5133->593 KB (88.4%); Sun Direction indicator un-suppressed in
  animations; magnetotail oriented at frame 1. Companion artifacts in repo:
  measure_animation_html.py, ANIMATION_TEST_PROTOCOL (v4 current).
- **21/51 PHASE 2 (2a-2d)** -- DONE `[render-confirmed Mode 5, June 10-11]`.
  One canonical center-body marker (add_celestial_object via
  add_center_body_marker); explicit blocks deleted in BOTH pipelines; one
  sun-position producer (resolve_shell_sun_position); one center-shell
  dispatch (add_center_body_shells); one shell-vars map
  (get_planet_shell_vars_map, replaced three copies); osculating params
  threaded through marker hover. Net -36 lines. P2-7 correction recorded:
  barycenters render as open squares with full hover + legend, correct
  as-is (the transparency-suppression expectation in the checklist was
  wrong, not the code).
- **N3 center-marker double** + **O5 animate bare hover** + **O6(a) animate
  no-marker-with-shells** -- CLOSED by Phase 2a (one disease: two marker
  mechanisms in static, one in animate, no canon). `[render-confirmed]`
- **D.Structural 3: create_planet_visualization RETIRED** -- DONE
  `[render-confirmed via Session A gate, June 10]`. THREE call sites swapped
  to the unified dispatch (NOT one -- the prior "one-site" ledger claim was
  wrong; corrected by repo-wide grep June 10); non-center sites now pass the
  TRUE center_object (the wrapper's own promised Phase-D correction;
  live-characterized identical). Wrapper annotated dead; deletion rides
  D.Structural 6. helpers' dead import joins D.Structural 5/6.
- **21/51 Phase 3 SESSION A** (3a notices + retirement + design doc +
  measurement harness) -- DONE `[render-confirmed Mode 5, June 10]`.
  Rebuild-as-universal adopted (ANIMATION_ENGINE_DESIGN_v1.md); gate 5(a)
  bytes PASSED: reduced magnetosphere composite 62.4 KB/f -> 1.81 MB @29f
  (envelope un-reduced; ~1.4 MB after the create_magnetosphere_shape
  producer promotion). measure_perframe_elements.py in repo.
- **21/51 Phase 3 SESSION B** (per-frame engine; axis + dipole cone +
  sun-direction indicator riding non-center bodies; greyed-legend
  disclosure) -- CONDITIONALLY render-confirmed June 11 @e5fd86d. Engine
  architecturally sound (allocation, rebuild, budget guardrail, stability
  assert all confirmed); riding visually confirmed at planet-centered scale
  (B3: Sun's axis rides the Sun marker); solar-system-scale visual gap is a
  TOOLING item (camera tracking -> item 19), not an engine defect.
  Greyed-legend (`visible='legendonly'` + legendrank + italic note)
  ACCEPTED (B4); click wart acceptable. 14 per_frame registry tags.
- **RESET BUTTON + center-dropdown trace-storm guard** -- DONE
  `[render-confirmed Mode 5, Tony, June 15 @6c5c3b]`. Top-bar Reset (date_frame
  row 0 col 11, next to Vernal Eq) behind a confirm dialog returns the GUI to
  STARTUP state. Two Mode-1 snippets into palomas_orrery.py (handler
  reset_all_selections ~8212; button ~8605) + new file test_reset_completeness.py.
  Option A; shells cleared by a COMPLEMENT-SET SWEEP (the SHELL_CONFIGS/
  CUSTOM_SHELLS registry covers only 78 of 113 -- Sun 19/Earth 12/belts 4 are
  hand-coded). Runtime-proven total: 310 IntVar names -> 309 distinct objects
  (frag_var aliases comet_2025k1d_var); the sweep targets exactly 117 vars, ALL
  declared-default 0; the only default-ON vars (show_apsidal_markers_var,
  show_closest_approach_var = 1) are handled in the named set, never swept.
  Completeness lives in the TEST (dirty-all -> live handler -> assert all 309
  IntVars + 3 StringVars + 10 entries restored), not in an over-built registry.
  GUARD: the objects loop fired update_center_dropdown's per-object 'write' trace
  ~182x/click (the `[CENTER MENU] Dynamic centers: Sun + ['Sun']` flood); a module
  flag `_reset_in_progress` + early-return guard (palomas_orrery.py ~10280/10287)
  + one explicit end-of-handler rebuild after center->Sun cut it to 1 rebuild AND
  clears a lingering pre-reset center. Storm absence render-confirmed by Tony.
  MAP CORRECTION: the 4 "stragglers" (arrokoth_new_horizons_var, dw_var, kbo_var,
  voyager1h_var) are DEAD/unwired; the live "2024 DW" var is asteroid_dw_var
  (already in the 182 objects); the sweep re-zeros the dead 4 harmlessly (D-sweep
  candidates).


#### [L-004] Apply C2 fix pass + run ANIMATION_TEST_PROTOCOL_v4_1, push
<!-- L:004 status:DONE upd:2026-06-17 section:C flag: -->
- **Apply the C2 fix pass (2 files) and run ANIMATION_TEST_PROTOCOL_v4_1**
  (the focused retest of C2/C6d + regression), append results to the 3C
  handoff, push. On pass: the Phase 3 CORE TRACK (Sessions A/B/C + fix
  pass) is COMPLETE -- move the marked render-gated items below into
  section C and update 21/51. (v4 first run, June 11: C1/C3/C5/C7 PASS,
  C4 pass-with-caveat, C2/C6 blocked by the three bugs below -- all
  three root-caused and fixed in pass C2.)
**Note (2026-06-17):** v4.1 gate COMPLETE. C2 PASS (Halley: no doubling,
  comet details correct, Sun tracking works). C6d PASS (Mercury-centered
  29-frame animation: Sun tracks correctly). O16 PASS WITH NOTE (auto-scale
  ~1 AU; root cause logged on L-056 -- positions={} fallback, pre-existing,
  workaround via 19.3 Phase B). MAPS tail non-animation BY DESIGN.
  Phase 3 CORE TRACK COMPLETE. L-007 (bow-shock disclosure) moves to C
  this pass. DONE.
**Gap:** none -- move to section C.

#### [L-005] Commit protocol v3.28 (or v3.29) to repo root
<!-- L:005 status:DONE upd:2026-06-17 section:C flag: -->
- **Commit protocol v3.28 (or v3.29 with the candidates above) to the repo
  root.** `[per chain; not re-verified June 11]`

- (CLEARED June 11) Phase 2, Session A, Session B, and Session C are all AT
  HEAD (chain above); no code push outstanding.

**Note (2026-06-17):** v3.28 confirmed committed @8e0f228. DONE -- move to C.
**Gap:** none -- move to section C.

---

#### [L-010] Keplerian epoch parse fails on 'osc.' suffix
<!-- L:010 status:DONE upd:2026-06-12 section:C flag: -->
- **`[KEPLERIAN POS] Could not parse epoch date` with 'osc.' suffix**
  -- FIXED in Phase 4 (June 12) `[render-gated]`. The apsidal_markers
  chain gained the missing '%Y-%m-%d %H:%M' form (the suffix WAS being
  stripped; the HH:MM format was not in the chain). The fix uncovered
  the worse half: FOUR sites in palomas_orrery.py used the same broken
  chain with a SILENT J2000 fallback -- a wrong-position failure, not
  console noise. All four now route through _parse_osc_epoch (one
  producer, three formats) with a loud [EPOCH] note before any J2000
  fallback. Smoke-tested (all three Horizons forms + garbage -> None).
**Note (2026-06-17):** DONE items stay in their section until a housekeeping
  pass moves them to C -- they provide a readable trail without jumping to
  the archive. When Gap says "none -- move to section C" that is the
  housekeeping trigger. render-confirmed Mode 5 is EVIDENCE of correctness,
  not a disposition -- a DONE item can be render-confirmed; an OPEN item
  can also be render-confirmed on a partial fix. Moving to C this pass.
**Gap:** none -- move to section C.

#### [L-011] Pass-C2 v4 blockers (3) + B3-bonus barycenter Sun bug
<!-- L:011 status:DONE upd:2026-06-11 section:C flag: -->
- FIXED in pass C2 (June 11, `[render-gated v4.1]`), three v4 blockers:
  * **C2a frame-1 comet doubling** -- the pre-existing frame-1 tail
    block AND the engine both added the comet's traces (incl. the
    builder's own Sun Direction). Fix: frame-1 block skips
    engine-owned comets (opt-in on, non-MAPS); the engine's
    allocation IS frame-1 content.
  * **C2b/C2c vanishing tail/indicator** -- STICKY-VISIBLE MERGE:
    Plotly applies frame traces as a MERGE; builders omit 'visible',
    so a slot once dummied to visible=False never reappeared. Tails
    filled previously-dummied slots exactly at perihelion; the
    indicator reshuffled into a dead slot when variable counts grew.
    Fix: EXPLICIT visible on every slot write (normalizer); the
    missing-position branch now writes explicit dummies + a console
    note (was a silent blanking). LESSON: frame updates are merges --
    any property a builder omits inherits the slot's history; padding
    slots with invisible dummies REQUIRES explicit visibility on
    every later write.
  * **C6d Mercury-centered Sun tracking** -- the engine excluded the
    center body entirely, but a centered body's SUN-DIRECTION
    elements must track the Sun moving around it; frame-1 freeze
    there is a physics lie. Fix: get_center_engine_elements() is the
    single source of truth -- the dispatch SKIPS that set
    (skip_elements threading, static unaffected, regression-tested
    identical) and the engine adds matching center_fixed specs
    (origin position, per-frame Sun). Inertial elements (axis, cone)
    correctly stay frozen. The B3-bonus barycenter Sun-Direction bug (indicator
  pointed at (0,0,0)/the barycenter when the Sun checkbox was off) was FIXED
  in Session C `[render-gated C1]`: the engine resolves a REAL Sun trajectory
  (fetching it when unchecked) and SUPPRESSES sun-direction elements when
  unresolvable -- it never points at a placeholder. Root cause for the
  archive: a fallback value is a CONTRACT -- (0,0,0) was a rotation-skip
  sentinel to shell-orientation code and literal position data to the
  indicator; reusing a fallback without checking each consumer's semantics
  is how a sentinel becomes a physics bug. Suppression beats fabrication.
**Note (2026-06-17):** v4.1 gate PASS -- C2 confirmed on Halley animation
  (no doubling, comet details correct, Sun tracking works). C6d confirmed
  on Mercury-centered 29-frame animation (Sun tracks correctly).
  MAPS tail non-animation is BY DESIGN (excluded per ADDENDUM_phase4
  decision 1). Moving to C this pass.
**Gap:** none -- move to section C.

#### [L-055] O14/O15 verdicts arrive with the v4 gate (comet legend churn; sodium particle count)
<!-- L:055 status:DONE upd:2026-06-17 section:C flag: -->
- O14/O15 verdicts arrive with the v4 gate (comet legend churn; sodium
  particle count) -- record here if either becomes an item. O15 may be
  settled by rounding (500 particles now ~31 KB/f).
**Note (2026-06-17):** v4.1 gate run: O14/O15 not observed as blocking issues
  during Halley animation test. No new items opened. DONE -- move to C.
**Gap:** none -- move to section C.

#### [L-018 | #8] Dead create_sun_direction_indicator imports (verify remainder)
<!-- L:018 status:DONE upd:2026-06-18 section:C flag: -->
Sole dead import was in palomas_orrery_helpers.py (line 52); removed.
Remainder verified: planet_visualization.py (L512 caller) and
palomas_orrery.py (L2298/L2363 callables) are live. No dead imports remain.
**Gap:** none -- move to section C.
**Ref:** grep confirmation + patch_dead_imports.py [verified @feab717].

#### [L-022 | #40] Asteroid belt hover -> single info marker
<!-- L:022 status:DONE upd:2026-06-18 section:C flag: -->
All four belt geometries (main, Hilda, Trojan L4, Trojan L5) use
create_info_marker() factory with hoverinfo='skip' on geometry traces.
Completed during Stage 3 sweep + Phase 1 re-pipe (May 27-29, 2026).
Documented in module docstring.
**Gap:** none -- move to section C.
**Ref:** asteroid_belt_visualization_shells.py docstring [verified @7964193].

#### [L-019 | #13] Neptune ring info-marker rotation (verify + close)
<!-- L:019 status:DONE upd:2026-06-18 section:C flag: -->
Original concern: ring info markers might not be rotated correctly to
match ring geometry. Code now uses x_final[0], y_final[0], z_final[0]
from the rotated ring points -- same transform as the ring geometry itself.
Fix documented in neptune_visualization_shells.py docstring (Stage 3
sweep, May 27-28 2026).
**Note:** visual verification (Mode 5 render) to confirm markers sit on
their rings, then close. Zero code risk.
`**Gap:** none -- move to section C`

#### [L-021 | #28] Neptune superimposed info markers (verify + close)
<!-- L:021 status:DONE upd:2026-06-18 section:C flag: -->
Original concern: multiple Neptune info markers (magnetosphere, bow shock,
radiation belts, ring system) might overlap visually. The Stage 3 sweep
(May 27-28 2026) fixed the degenerate X-axis-rotation bug where all ring
markers collapsed to one position.
**Note:** visual verification (Mode 5 render) -- confirm markers at
distinct positions. Zero code risk.
`**Gap:** none -- move to section C`

#### [L-023 | #N2] Saturn/Uranus ring marker placement
<!-- L:023 status:DONE upd:2026-06-18 section:C flag: -->
Original concern: ring info markers at wrong positions. Both modules
document a fix for the "Neptune 2C pattern -- previously all rings shared
one degenerate X-axis-rotated marker" (Stage 3 sweep, May 27 2026).
Markers now use first point of rotated ring geometry.
**Note:** visual verification (Mode 5 render) -- confirm ring markers sit
on their respective rings. Zero code risk. Likely DONE.
`**Gap:** none -- move to section C`

#### [L-024 | #N4] Planet 9 sphere n=50 -> 20/25
<!-- L:024 status:DONE upd:2026-06-18 section:C flag: -->
Planet 9 surface now uses mesh_resolution=24 (mesh3d geometry). Hill sphere
uses n_points=20. If the original concern was n=50 being too dense, the
current values (20-24) appear to address it.
**Note:** verify that no Planet 9 shell still carries n=50. If all are at
20-24, close. Zero code risk.
`**Gap:** none -- move to section C`

#### [L-029] v25 D3 dead-code annotations + small-body analytical tail
<!-- L:029 status:DONE upd:2026-06-18 section:C flag: -->
Zero DEAD/UNUSED/ORPHAN/RETIRED annotations found in palomas_orrery.py.
3 RETIRED annotations in planet_visualization.py (covered by L-016).
No "analytical tail" references found in codebase. This item may be
stale -- the original v25 dead-code work may have been completed or
absorbed by the Phase 3 sweep.
**Note:** verify whether any actionable content remains. If not, close
as absorbed. If the "small-body analytical tail" refers to a specific
feature, needs clarification from Tony.
`**Gap:** none -- move to section C`

#### [L-006] Mercury +0.2 R_M northward dipole offset
<!-- L:006 status:DONE upd:2026-06-20 section:C flag: rice: -->
- **Mercury +0.2 R_M northward dipole offset** -- DONE. (Anderson 2011;
  v24 Movement-2 item.) `[verified absent @76c330e]`
  **Tony:** let's prioritize the dipole implementation for Mercury, Earth and Jupiter and clean these up. 
  **Done (2026-06-20, built @5b294c8 -> pushed @08f9831, Mode-5 confirmed):**
  offset_fraction 0.19 R_M northward implemented in PLANET_DIPOLE +
  build_dipole_cone_traces (axial; Anderson et al. 2011, MESSENGER). Mercury
  renders as the degenerate axis-line (tilt 0, option a). This IS the +0.2 item
  -- Anderson reports 0.19 +/- 0.01 R_M.
  **Gap:** none -- move to section C

#### [L-009] Dipole cluster: envelope tie / offset direction / remaining cones / half_len_frac
<!-- L:009 status:DONE upd:2026-06-20 section:C flag: rice: -->
- **Envelope -> dipole tie / season-derived roll** (Mode-7, conditional);
  **dipole offset DIRECTION** (Mode-7; apex stays centered until sourced);
  **REMAINING DIPOLE CONES** (verified set, June 13 @33aac56): the cone
  exists on Uranus + Neptune (done -- the dramatically tilted/offset
  dipoles, where the swept envelope matters most). Of the eight bodies
  with a magnetosphere, the candidates still WITHOUT a dipole_cone, on
  physics, are Earth, Jupiter, Mercury (genuine tilted/offset global
  dipoles -- Tony's named set) plus Saturn (MARGINAL: dipole aligned to
  <1 deg of the spin axis, so the swept cone is near-degenerate; earns the
  element only weakly). EXCLUDED on physics: Mars (crustal fields, no
  global dipole) and Venus (induced magnetosphere, no internal dynamo).
  PROVENANCE GATE unchanged: all dipole tilts are currently RECALLED and
  MUST be sourced before any PLANET_DIPOLE entry (Fetched-vs-Recalled) --
  show the envelope, but the tilt that SETS it must be cited, not
  remembered. **per-body half_len_frac tuning** (Mode-5 knobs).
  `[verified set @33aac56]`
**Tony:** as mentioned above, let's prioritize cleaning up the remaining dipoles and cones.
**Done (2026-06-20, built @5b294c8 -> pushed @08f9831, Mode-5 confirmed):**
  REMAINING DIPOLE CONES sub-part CLOSED -- Mercury, Earth, Jupiter, Saturn
  dipole_cones built + rendered (handoff v30). Offset MAGNITUDE sourced and
  applied AXIALLY (northward along spin pole): Mercury 0.19, Earth 0.085,
  Jupiter 0.12, Saturn 0.045 R_p (peer-reviewed; Gemini de-novo June 18).
  Mercury + Saturn render as the degenerate axis-line (tilt ~0, option a);
  Earth + Jupiter as full swept cones (9.6 / 10.3 deg). half_len_frac: existing
  values Mode-5-confirmed acceptable, no dedicated tuning needed. L-006 closed
  in parallel. Smoke PASS @08f9831; provenance Tier-1 = 0.
**Closed by decision (2026-06-20):** the swept cone (the FAST sweep of the
  dipole axis about the spin axis) + the axial offset are the honest, legible
  object, and they are DONE. No remainders are kept on this item -- the slower
  frame-coupling motions are promoted to L-061 (magnetosphere-dipole frame
  coupling / seasonal roll), because they are new physics, not unfinished cone
  work, and a closed number should not smuggle separate work as a footnote.
  ("No element needs to exist; it earns its place by what it teaches"; access
  is not understanding.)

  THREE MOTIONS, THREE TIMESCALES (kept for the record; only #1 is this item):
  1. DIPOLE AXIS about the spin axis -- FAST, one rotation (hours-days). DONE:
     this IS the cone; instantaneous azimuth unknowable -> draw the whole sweep.
  2. OFFSET lateral direction -- MIXED (longitude-locked fast; Earth secular,
     over decades). Axial magnitude shipped; lateral part small vs cone scale.
     -> L-061.
  3. ENVELOPE -> dipole SEASONAL ROLL -- SLOW, one orbit; invisible in a static
     plot. -> the core of L-061.
**Gap:** none -- move to section C

#### [L-036] O11 greyed-legend display-name verdict: NO item needed
<!-- L:036 status:DONE upd:2026-06-11 section:C flag: rice: -->
- O11 verdict June 11: greyed-legend display names derive correctly from
  checkbox keys -- NO item needed; recorded so it is not re-raised.
**Gap:** none -- move to section C

#### [L-041] Item 19.3 axis-control round trip (P1/P2/Phase A/Phase B + toggle follow-on)
<!-- L:041 status:DONE upd:2026-06-16 section:C flag: rice: -->
- (June 14 DESIGN, no code) Orrery-side axis control (item 19.3) scoped +
    handed off: HANDOFF_item19_axis_control_orrery_v1.md, built on 1288b51 /
    gallery 2f40d9d. DECISION (a2): scene-dict extraction only (axes +
    aspectmode + camera + domain, verified byte-identical across the 5704/7940
    twins); layout envelope (title/annotation/legend/margin/footer) NOT merged
    -> divergence-audit seed (4 catalogued divergences in the handoff). Full
    function-body merge stays off the list. FINDING: _track_axis (7652) is
    already the complete, correct spec (range + autorange=False + dtick +
    styling); the two MAIN paths (5704/7940) under-specify (no dtick /
    autorange) -- THAT is the close-approach unreadability. Feature =
    generalize the track spec to the under-specified sites via
    build_scene_axes/build_scene, dtick from the SHARED
    visualization_utils._calculate_grid_dtick (provable Studio parity). Q2:
    auto-only first cut (auto dtick + non-Sun-center range autofit IF the
    existing range logic doesn't already fit extent); user GUI fields = fast
    follow. Q3 matrix: range never overrides S3(exoplanet)/S4(track); dtick
    lands on S1/S2 first; S4 already correct. Two-phase: P1 byte-identical
    extraction (Mode-5 zero-change gate), P2 turn on dtick+range (Apophis
    render gate). Confirm-at-impl: read get_improved_axis_range /
    get_animation_axis_range (range-autofit scope), _track_dtick source
    (parity routing), Studio round-trip (no double-apply).      
- (June 15) Item 19.3 Phase 2 COMPLETE. auto_dtick + autorange=False landed on
  S1/S2 via build_scene. Base 7aecc3b -> bd768ee (builder) -> aa1a4cd (call sites).
  build_scene gains auto_dtick (derives dtick from the range span via the SHARED
  visualization_utils._calculate_grid_dtick -> provable Studio parity) + an
  axis_range=None guard (emit neither dtick nor autorange when no range exists).
  Headline fix verified: close-approach cubes now readable -- e.g. 0.0008 AU span
  -> 0.0001 AU dtick (~15,000 km gridlines) instead of effective dtick=1. Default
  build_scene call stays byte-identical, so Phase 1 untouched. Render gate (Tony,
  Mode 5, aa1a4cd): static close-approach readable; everyday full-system plots fine
  with explicit ~6-gridline dtick (intended, visible change: auto_dtick applies to
  ALL S1/S2 plots).
  FINDING: the load-bearing non-tracking animation-hold test PASSED -- autorange=False
  on the up-front once-set scene SUPPRESSES Plotly per-frame autorange (grid/range
  held across frames). This validates the "real fix (autorange suppression)" named
  in the palomas_orrery.py June-13 note (~7847) FOR THE NON-TRACKING PATH. BOUNDARY:
  does NOT resolve the camera-tracking (S4) per-frame autorange residual (separate
  dedicated-session item; _track_axis untouched). Two distinct problems; only the
  non-tracking one is closed.
  Also folded in: removed the duplicate _calculate_grid_dtick() docstring line
  (Phase-1 insertion artifact). Cosmetic residuals: trailing whitespace on
  palomas_orrery.py 5711/7927; MODULE_ATLAS.md lags (auto_dtick absent) -- regen
  when convenient.
  19.3 Phase 1 (extraction) + Phase 2 (dtick/autorange) done. Fast-follow remains:
  user-settable range/dtick GUI fields (orrery + Studio round trip); S3 exoplanet
  opt-in.   
- (June 16) Item 19.3 Phase A COMPLETE -- user-settable dtick GUI field
  (orrery generation side). Base 30840b1 -> 1c08a8a (one transactional patch,
  7 edit groups, all palomas_orrery.py, Mode 1). Blank field = Phase 2
  auto_dtick; >0 overrides, threaded to all three live build_scene sites
  (S1 ~5720, S2 ~7955, S3 ~5998, AST-confirmed 3/3). Orrery already had a
  user-settable RANGE (custom_scale_entry); this fills the missing DTICK.
  Studio half of the round trip was ALREADY DONE @2f40d9d (March) -- this
  added the orrery half, not Studio.
  S3 PARALLEL-PIPELINE FIX: exoplanet STATIC scene (bare inline scene=dict,
  AU-coarse grid) migrated to build_scene, matching exoplanet ANIMATION
  (already on S2 build_scene). update_layout merges -> camera/domain/theme
  preserved; build_scene_axes emits same X/Y/Z (AU) titles. Verified static
  AND animated (Proxima ~+/-0.0583 AU).
  CORRECTION (Observation Override): the design-stage "manual dtick is a no-op
  under Auto scale" caveat was WRONG. calculate_axis_range_from_orbits /
  get_animation_axis_range never return None (concrete fit, or [-1,1]
  fallback), so axis_range is always a concrete cube -> dtick applies under
  Auto AND Manual, matching Tony's Studio experience. No logic changed; only
  tooltip + 4 comment blocks corrected. build_scene None-guard (481-483) is
  defensive only.
  S4 (camera-track) deliberately EXCLUDED -- computes its own _track_dtick;
  the Phase-2 per-frame-autorange boundary holds.
  Render gate (Tony, Mode 5, 1c08a8a): ALL 6 PASS -- regression, Auto+finer
  dtick, Manual close-approach, S3 exoplanet (static+animated), animation
  hold, Reset clears.
  Fast-follow REMAINING -> Phase B: Studio read-on-load (populate
  scene_axis_range/scene_dtick fields from the loaded figure's baked grid so
  the round trip is VISIBLE). Open decision: km-suffix on axis titles
  (annotate vs match orrery). Handoff: HANDOFF_item19_3_phaseA_dtick_gui.md.
  Pre-existing observation (NOT Phase A): exoplanet-animation
  "id_type (host_star) not allowed" ValueError on host-star trajectory fetch
  -- confirm if tracked.
 (June 16, item 19.3 Phase B SHIPPED) Studio read-on-load round trip,
gallery tools/gallery_studio.py, built on 2f40d9d / orrery c28eec0.
New shared reader _read_scene_grid_from_figure; both _do_load branches
populate scene_axis_range/scene_dtick from the figure (D3 precedence:
explicit studio override wins, else figure); _extract_encounter_data
routed through the same reader (+ figure dtick now surfaced in the
read-only panel). D1 RECONCILED to the live bytes: the handoff's
half-extent gate did not match the live dtick-keyed suffix; OPTION B
chosen (KM_SUFFIX_MAX_AU = 0.01 emit gate on half-extent, dtick tiers
kept inside, range-auto fallback). Closes the item-19.3 round trip
(orrery bakes -> Studio reads + refines). Render-gate items in handoff
sec 5. Optional later: orrery also emitting the suffix under the same
cutoff (full title parity) -- NOT this item.
(June 16, item 19.3 Phase B follow-on, from the render-gate observation)
DEFAULT_CONFIG show_axes / show_grid / show_modebar flipped False -> True
(gallery tools/gallery_studio.py, landscape editorial baseline), pushed at
812c05f. Tony's call: the boxes should reflect what the orrery HTML
produces on load AND these defaults should display across the other modes
("I always turn them on"), so the global default was flipped rather than a
surgical raw-branch-only set. Blast radius = every path that seeds from
DEFAULT_CONFIG (app startup, Reset Defaults, landscape preset, orrery-mode
entry, raw-orrery load) now starts with axes/grid/modebar on. Studio
exports UNAFFECTED -- they carry their own saved toggle states in
_studio_config, which override the default on load. show_modebar=True is
safe vs non-Plotly input: Studio only ingests Plotly figures (others bounce
at load), and show_modebar is only the exported HTML's Plotly
displayModeBar flag -- never touches a tkinter window. 
**Ref:** HANDOFF_item19_3_phaseB_studio_readonload.md; SHA chain 7aecc3b -> ... -> gallery 812c05f
**Gap:** none -- move to section C

#### [L-054] Gate 5(b): full resolution ships, rounded -- render-confirmed
<!-- L:054 status:DONE upd:2026-06-13 section:C flag: rice: -->
- **Gate 5(b)** RECAST (June 12); RENDER-CONFIRMED (June 13) `[render-
  confirmed Mode 5]`: full resolution ships, rounded. Tony's June-13 pass
  on live Mercury data confirmed (1) animated magnetosphere correct (tail
  anti-sunward across frames, no seam/flicker at d7 rounding); (2) camera
  tracking frames the active elements (element-extent window: tail opens
  it, magnetosphere tightens it); (3) tracked playback centers steadily on
  the body (cube-size wobble noted acceptable, see camera-tracking RESIDUAL);
  (4) indicator clamp renders sensibly; (5) inertial-note hover wording.
  Mercury-centered AND Sun-centered-track-Mercury both confirmed; saved-file
  round trip confirmed identical to live render.
**Gap:** none -- move to section C

#### [L-057] Animation auto-scale-vs-shells + Phase 3 tier decision -- CLOSED
<!-- L:057 status:DONE upd:2026-06-11 section:C flag: rice: -->
(CLOSED June 10-11: animation Auto-scale-vs-shells -- implemented as
max(orbital, shell) in Session C, render-gated C6. Phase 3 tier decision --
tier 2 adopted at the June-10 GO; tier 1 dropped; tier 3 = the resolution
follow-on behind gate 5(b).)
**Gap:** none -- move to section C

#### [L-007] Bow-shock hover disclosure remainder
<!-- L:007 status:DONE upd:2026-06-11 section:C flag: rice: -->
- **Bow-shock hover disclosure remainder** -- DELIVERED Session C
  `[render-gated C5]`: U+N bow-shock hovers now carry the conic-model
  sourced-vs-schematic note + the animation-freeze line (this also closes
  the Phase-1 orientation-freeze disclosure rider and the frame-1-freeze
  rider -- one sweep, three siblings, as designed). MOVE TO C on the v4
  gate pass.
**Gap:** MOVE TO section C on the v4 gate pass (L-004).
**Tony:** L-004 is done. 
**Gap:** none -- move to section C

#### [L-003] Protocol amendment candidates (for v3.29)
<!-- L:003 status:DONE upd:2026-06-22 section:C flag: rice:3/3/90/1.5 -->
- **Protocol amendment candidates (for v3.29; from the animation refactor):**
  - The xvfb SystemButtonFace<->gray90 sed round trip is NOT idempotent on files
    that natively contain gray90 (palomas_orrery.py has 26 native gray90
    literals). Rule: run the swap on a THROWAWAY copy only; never
    restore-in-place on the deliverable. (Caught June 9; applied as practice
    in every session since.)
  - Full-module exec under xvfb with tk mainloop suppressed enables LIVE-dispatch
    tests inside the real module namespace (real tk vars, real builders, network
    calls patched). Used as the standard verification gate for Sessions
    Phase 2 through 3C; candidate for the Agentic Pre-Test section.
  - `grep -c` exits 1 when the count is 0, silently BREAKING an `&&` chain --
    a downstream verification command can simply never run while the output
    looks complete. Rule: never put `grep -c` mid-chain with `&&`; run
    verification greps standalone or with `;`. (Caught June 10 -- one residual
    check did not execute until re-run standalone.)
**Gap:** none -- move to section C
---

## D. RECONCILED LEDGER -- OPEN

### D.Movement -- Movement-track open items

#### [L-008] v24 sec5 precision batch (low-risk)
<!-- L:008 status:OPEN upd:- section:D.Movement flag: rice:2/2/50/2 -->
- **v24 sec5 precision batch** (low-risk): Jupiter compressed/expanded MP
  toggle; Earth MP/BS citation upgrade; per-body shock eccentricity.
  `[per chain]` (The inner-four bow-shock hover km/AU sub-item `[verified
  @76c330e]` is de-duped to L-052 / section E -- the AU-convention home -- so it
  is not double-counted; the precision batch keeps the three physics sub-items.)
**Note (2026-06-21):** distinct from L-007. L-007 was the bow-shock hover
  DISCLOSURE (sourced-vs-schematic + animation-freeze note), now DONE / in C.
  L-008 is the precision-VALUES batch -- different content, real remaining work.
**Tony:** Clarify description. Update RICE.   

#### [L-061] Magnetosphere-dipole frame coupling / seasonal roll
<!-- L:061 status:OPEN upd:2026-06-21 section:D.Movement flag: rice:1/1/50/3 -->
- **Magnetosphere-dipole frame coupling / seasonal roll** -- OPEN, deferred.
  Promoted from L-009 (2026-06-20). Two frames the render currently keeps separate
  are physically COUPLED:
    * the dipole cone is BODY-locked (spin-pole frame, Sun-independent);
    * the magnetosphere is SUN-locked (bow-shock-to-tail axis follows the
      planet->Sun line).
  As the planet orbits, the Sun-line sweeps ~360 deg once per orbital YEAR, so the
  magnetosphere reorients in inertial space while the spin/dipole axis stays fixed
  -- the dipole orientation appears to ROLL relative to the magnetosphere, once per
  orbit. (Tony confirms, 2026-06-20: the dipole does not travel WITH the
  magnetosphere, but has a dynamic relationship with it -- it rolls with respect to
  the magnetosphere as the planet orbits the Sun.)
  AMPLITUDE = OBLIQUITY: the spin-axis-to-Sun-line angle swings over the orbit with
  amplitude equal to the axial tilt (magnetospheric "seasons") -- near-nil for
  Mercury (~0) and Jupiter (~3 deg); meaningful for Earth (23), Saturn (27),
  Neptune (28); extreme for Uranus (~98 deg, pole swings sunward at solstice over
  its 84-yr orbit).
  WHY ITS OWN ITEM (new physics, not a cone remainder): the real magnetosphere's
  SHAPE responds to the dipole tilt and the interplanetary field, not just the
  Sun-line. Modeling the coupling is a Mode-7 question (envelope-orientation
  physics -> Gemini, not asserted from memory). Folds in the L-009 offset-direction
  remainder (mode 2).
**Gap:** scope DELIBERATELY UNREFINED (Tony: capture broad, do not refine yet -- seasonal-roll-only vs full coupling is a judgment call for whoever picks it up). Visible/teachable only under envelope animation across enough of an orbit for the obliquity-driven angle to shift, dramatic only for high-tilt bodies -- the natural build/re-open trigger. RICE is a placeholder pending deliberate scoring.

### D.Priority -- real bugs

#### [L-012] Osculating pre-fetch false-provenance messages
<!-- L:012 status:OPEN upd:2026-06-21 section:D.Priority flag:CRIT rice:2/2/90/1 -->
- **What it is (plain version).** When you choose "use existing elements" (the
  cached path), the program correctly loads osculating elements FROM CACHE -- but
  the console then prints messages claiming a FRESH FETCH that did not happen:
  "[SUCCESS] Mercury fetched fresh data" and "[PRE-FETCH] OK: <obj>: Updated".
  The log says "fresh" over cached data. (The variable is even named
  fresh_elements but holds cache on that path.)
- **Why CRIT (not cosmetic).** Cite-over-recalled failure class: a SUCCESS /
  "fresh" stamp printed over cached elements can hide a STALE element -- you would
  trust an old position because the log told you it was freshly fetched. A false
  provenance line is exactly what the protocol treats as load-bearing. The render
  looks fine; the trust signal is the lie.
- **Two defects found alongside the main one:**
  1. The "[SUCCESS] ... fetched fresh" line is HARDCODED to Mercury
     (`if obj_name == 'Mercury':`, palomas_orrery.py:4464) -- leftover debug.
     Every other object gets only the false "Updated".
  2. The age channel is DEAD: calculate_age_days (:285) swallows its error in a
     bare except and returns None, so the cached element's real solution date
     can't be shown -- it reports "unknown age".
- **Honest fix.** Print the ACTUAL path (fetched vs cached); on a cache hit say
  so and show the element's real solution date instead of "fetched fresh" /
  "unknown age". Drop the Mercury-only hardcode so the message is correct for all
  objects.
- **LATENT sub-bug (separate, lower-priority).** Fresh-save writes a CENTER-AWARE
  key cache[cache_key] (:804) but the fallback reads the BARE key cache[obj_name]
  (:832). They coincide for heliocentric (key == name) but DIVERGE for
  barycentric / body-centered cases like 'Charon@9' -- one producer, two key
  conventions, so a non-heliocentric center can miss or read the wrong cached
  element. Split to its own L-handle if it grows.
**Gap:** the logging fix (report fetched-vs-cached + real solution date; drop the Mercury hardcode) is the CRIT part, ~0.5 session. The cache-key divergence is a separate, smaller follow-on.
**Ref:** osculating_cache_manager.py:813-815/832/285/804; palomas_orrery.py:4464/4471/4473 

#### [L-013] Mercury 2019-epoch anomaly
<!-- L:013 status:DEFERRED upd:2026-06-15 section:D.Priority flag: rice:1/1/10/2 -->
- **Mercury 2019-epoch anomaly** (June 15, UNRESOLVED, deferred to recurrence).
  doc-1 rendered Mercury's Keplerian with epoch 2019-01-01 osc. / 2018 perihelion
  while Venus/Earth were current. NOT stale cache (project is 18 months old) and
  NOT the static fallback (planetary_params['Mercury'] epoch = 2025-11-19).
  Grounded: doc-1 params had MA/TA keys -> OSCULATING source (the static dict has
  neither); the 2019 element was a runtime set, since overwritten by Tony's update
  (current Mercury correct: epoch 2026-06-15 17:50, marker 0.433395 == hover
  0.4333945989). Origin not determinable from disk; recollection insufficient.
  ACTION: if it recurs, capture osculating_cache_backup.json at that instant
  and/or add a one-line element-source+epoch print at fetch time before
  theorizing. LESSON re-affirmed: Claude's "7-year stale cache" was a recalled
  inference dressed as fact; Tony's domain knowledge overrode it (Observation
  Override).
  **Tony:** this was a one-time observation. i do not know what caused it. pending better definition. 

### D.Structural -- dead-code / honest shell files (Phase 3)

`[per v23/v25 chain unless tagged]`
**Tony:** dead code items are good canditates for a cleanup pass. 

#### [L-015 | #5] _info import cleanup (~89+87 imports, 2 files)
<!-- L:015 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:2.5/1/75/2 -->
Named dead imports removed (hover_text_sun, create_planet_visualization)
from helpers.py [verified @feab717, patched this session].
**Gap:** ~78 remaining dead _info string imports in helpers.py (89 imported,
~11 used). Broader sweep deferred; low-risk, moderate volume.
**Ref:** grep confirmation this session; patch_dead_imports.py.

#### [L-016 | #6] Archive dead shell functions
<!-- L:016 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:1/1/90/1 -->
create_planet_visualization() at planet_visualization.py L558 is annotated
RETIRED (June 2026, Phase 2.5). Zero callers confirmed -- all references
are in comments/docstrings. Two retired Sun functions in the same file
(L293, L306) are similarly dead. Also: create_neptune_magnetic_poles() in
neptune_visualization_shells.py is marked DEPRECATED (D2 Option C, May 2026).
**Gap:** grep-confirm zero callers across both pipelines (plot_objects +
animate_objects), then delete bodies. Low risk; cleanup only.
**Ref:** planet_visualization.py L558, L293, L306; neptune_visualization_shells.py.

#### [L-020 | #26] CUSTOM_SHELLS tooltip verification
<!-- L:020 status:DONE upd:2026-06-22 section:D.Structural flag: rice:1/2/90/2 -->
Verify that every CUSTOM_SHELLS entry in shell_configs.py has a tooltip
and that the tooltip text is accurate. CUSTOM_SHELLS covers rotation axes,
sodium tail, magnetospheres, bow shocks, radiation belts, rings, and
field-aligned currents across Moon, Pluto, Mercury, Venus, Earth, Mars,
Jupiter, Saturn, Uranus, Neptune.
**Gap:** none -- VERIFIED 2026-06-22 (AST walk of CUSTOM_SHELLS @666244f):
11 bodies, 41 leaf shell-configs, all 41 carry a tooltip, zero missing. DONE;
move to section C on next housekeeping relocation.

#### [L-025 | #N7] Reduced to custom-geometry inline markers only
<!-- L:025 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:3/2/50/2 -->
The Phase 3 info-marker sweep (141 conversions, 18 files, May 2026) moved
sphere-shell markers to the create_info_marker() factory. Inline marker
dicts should now only remain in CUSTOM_SHELLS builders (rings,
magnetospheres, radiation belts, etc.) which need geometry-specific
positioning.
**Gap:** audit -- grep for inline marker dicts outside CUSTOM_SHELLS
builders. If none found, close. Zero code risk.
**Tony:** unclear on the technical significance. I don't recall a mode 5 issue. 

#### [L-026 | #9] palomas_orrery_helpers.py CRLF -> LF
<!-- L:026 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:3/2/75/2 -->
File confirmed CRLF (verified this session @7964193). Functional no-op
to convert, but the diff touches every line, so best as a standalone
commit with no other changes.
**Gap:** convert CRLF -> LF (binary-mode script or dos2unix). Do as
isolated commit. Low risk but noisy diff.
**Tony:** this should be part of a general sweep of the code base for LF conversion. 
this is a maintenance item to keep the codebase platform neutral, which is the larger goal
and should be stated clearly. 

#### [L-027 | #61] Platform Neutrality (SystemButtonFace)
<!-- L:027 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:3/2/75/2 -->
26 occurrences of the Tk color name SystemButtonFace in palomas_orrery.py.
Resolves on Windows; fails on Linux/macOS. The xvfb pre-test sed swap is
a workaround, not a fix. Options: hex literal '#F0F0F0', platform
detection (sys.platform), or ttk styling.
**Gap:** choose replacement strategy, then sweep. Design decision before
build. Moderate scope (26 sites); low functional risk (cosmetic only).
**Tony:** this has the same purpose as L-026. 

#### [L-028] ASCII em-dash violation, comet_visualization_shells.py L257/505/519
<!-- L:028 status:OPEN upd:2026-06-11 section:D.Structural flag: rice:1/1/100/1 -->
Pre-existing; 3 em-dash lines in MAPS strings `[verified @0ce1e26]`.
**Gap:** fix on next touch (binary-mode).

#### [L-064] Provenance-scanner format sweep -- Earth System family
<!-- L:064 status:OPEN upd:2026-06-22 section:D.Structural flag: rice:3/2/50/1 -->
- **Sweep the Earth System visualizations so on-layer / display-string text is in
  a format the provenance scanner catches at Tier-1.** Emerged from L-001's
  two-tier-text decision: the composed-tier discipline (numeric claims built in
  the generator with `# Source:` within lookback; framing-layer / annotation text
  traversed by the scanner, not just per-feature popups) should hold across the
  whole family -- ERA5 heat maps, energy imbalance, ENSO (L-060), ocean
  acidification / pH, food insecurity (L-001) -- so composed sensitive statements
  everywhere are scanner-visible, not "trust me."
- **Design-needed:** confirm, per module, whether provenance_scanner.py actually
  traverses each generator's display-string path (esp. framing-layer/annotation
  text vs per-feature popups); where it does not, the fix (move numeric
  construction to a scanner-visible site / make the path traversable) is the task.
  Couples with the provenance audit (PROVENANCE_AUDIT.md, Tier-1=0 goal).
**Gap:** deferred. Confirm scanner coverage of each Earth System generator at
HEAD, define the on-layer-text format contract, then sweep. Section placement
(D.Structural) adjustable.
**Ref:** provenance_scanner.py; PROVENANCE_AUDIT.md; originated from L-001
(two-tier on-layer text).

### D.Cosmetic -- polish (bundle when convenient)

**Tony:** the `[per chain]` notes require development. probably a mode 5 pass and rice updates. 

#### [L-030 | #17] GEO info-marker position
<!-- L:030 status:OPEN upd:- section:D.Cosmetic flag: rice:1/1/100/1 -->
`[per chain]`

#### [L-031 | #18] Uranus gossamer ring visibility
<!-- L:031 status:OPEN upd:- section:D.Cosmetic flag: rice:1/2/90/2 -->
`[per chain]`

#### [L-032 | #41] Sun legend ordering (ordered dispatch iteration; no manual fix)
<!-- L:032 status:OPEN upd:- section:D.Cosmetic flag: rice:2/2/75/2 -->
`[per chain]`

#### [L-033] Comet plotted-period trace visibility (line weight/color; O6b)
<!-- L:033 status:OPEN upd:2026-06-10 section:D.Cosmetic flag: rice:2/1.5/100/2 -->
- Comet plotted-period trace visibility (line weight/color; O6b June 10).

#### [L-034] Center-body hover "Distance to Center Surface" negative-radius formatting
<!-- L:034 status:OPEN upd:2026-06-21 section:D.Cosmetic flag: rice:1/1/75/0.5 -->
- **What it is.** The detailed hover already shows two distances correctly: a
  distance to the center body's CENTER (r=0) and a distance to its SURFACE. The
  bug is only on the CENTER BODY'S OWN hover: because the formatter treats the
  center as an object at the origin, its surface line renders as a NEGATIVE radius
  -- "Distance to Center Surface: -<radius> km (below mean datum)". The
  magnitudes are right; only the sign/label on the center body's own surface line
  reads wrong.
- **Fix.** In format_detailed_hover_text, special-case the center body so its own
  surface line reads sensibly (drop the misleading minus, or relabel). Mode-5 to
  confirm the exact wording you want.
**Gap:** decide display wording (Mode-5), then a targeted edit to format_detailed_hover_text. Cosmetic; zero functional risk.

#### [L-035] Solar shell hovertext <br> vs \n context mismatch (C6b)
<!-- L:035 status:OPEN upd:2026-06-11 section:D.Cosmetic flag: rice:2/2/100/1 -->
- Solar shell hovertext uses '<br>' where '\n' renders (or vice versa;
  context-specific -- C6b finding, June 11). Fix in the affected
  formatter on next touch.

#### [L-037] WARNING: Unknown object type 'satellite' (spurious; handled downstream)
<!-- L:037 status:OPEN upd:2026-06-15 section:D.Cosmetic flag: rice:1/1/90/1 -->
- `WARNING: Unknown object type 'satellite'` fires once per satellite (Triton/
  Despina/Galatea in the June-15 gate). Handled correctly downstream (orbits
  plotted, Keplerian properly skipped as Satellites) -- spurious; a type-dispatch
  that does not list 'satellite'. Silence on next touch of that dispatch.

#### [L-038] Psyche encounter hardcoded fallback distances lack # Source
<!-- L:038 status:OPEN upd:- section:D.Cosmetic flag: rice:1/1/75/1.5 -->
- Psyche encounter HARDCODED FALLBACK distances (8,009 km Mars GA / 1,151 km
  Phobos), used when Horizons has no ephemeris past 2029-06-11 (expected,
  graceful), lack a `# Source:` -- add one (provenance discipline) on next touch.
  **Tony:** unclear why the provenance scanner has not flagged this item. 

### D.Feature -- Bucket A (near-term)

#### [L-039 | #23] Earth ionosphere shell
<!-- L:039 status:OPEN upd:2026-06-21 section:D.Feature-A flag: rice:2/2/60/2 -->
- **Add an ionosphere shell to Earth's visualization** -- a new atmospheric shell
  alongside Earth's existing shells. The ionosphere is the ionized upper-atmosphere
  region (~60-1000 km altitude, D/E/F layers). Pattern is the established one: a
  SHELL_CONFIGS / CUSTOM_SHELLS entry with sourced altitude bounds, a checkbox
  toggle, the single-info-marker pattern, and hover carrying km + AU per convention.
**Gap:** SOURCE the layer boundaries before any literal (Fetched-vs-Recalled -- cite, do not recall); pick the representation (single band vs D/E/F sub-layers); then build on the Earth shell pattern. Light design, then standard shell build.

#### [L-040 | #19] Plot-cube control parity + scaling/camera comprehensive review
<!-- L:040 status:OPEN upd:2026-06-13 section:D.Feature-A flag: rice:3/3/50/3 -->
- **19 Plot-cube control parity + SCALING/CAMERA COMPREHENSIVE REVIEW** --
  JOINED / cross-repo. The original parity scope (scene_axis_range,
  scene_dtick, aspectmode, camera orientation, axes/grid toggles; Studio
  side `[verified @2f40d9d]`; design authority 3d_axis_control_handoff.md)
  PLUS, per Tony's June-11 framing call, the accumulated scaling/camera
  FIXTURE LIST (all scaling work lives here; no separate session track):
    * Photosphere auto-scale collapse (static Auto = shell extent alone,
      hiding orbits; Session-A Finding 1 concrete case).
    * Sun-Direction indicator clipped by cube range (Finding 1 / O12)
      -- FIXED in Phase 4 (June 12) `[render-gated]`: geometric clamp in
      create_sun_direction_indicator (ray-cube exit along the sun
      direction, 0.95 margin, min_scale floor wins); axis_range threaded
      through the unified dispatch (Manual scales only -- Auto widens to
      2x shell extent AFTER the dispatch, so the incoming range would
      over-clamp) and into both engine indicator specs via a
      collect-time range hint (the animate pipeline's orbital-derived
      Auto range CAN undercut the shell-scaled length -- the O12 case).
      No-range path byte-identical (smoke-tested).
    * Sun orbit around a planet center lacks cube buffer (O12).
    * Fly To zoom limit ignores shell extent (computed from orbital
      distance/marker size; planets stop too far out to see magnetosphere
      or belts; comets okay). (O13b, June 11.) RESOLVED (Phase 4 render-
      gate, June 13) `[render-confirmed Mode 5]`: window sizing replaced
      the body-radius multiple with the LARGEST ACTIVE element's MEASURED
      extent -- traces_extent_from_center() (shared_utilities) is the one
      producer; the static dispatch records fig._body_element_extent_au per
      body and the per-frame allocator records _perframe_body_extent, and
      BOTH the camera-tracking window and add_fly_to_object_buttons
      (new target_extents param) consume it. Sodium tail on -> window
      opens to ~0.20 AU to hold the whole 10,003-radii tail; tail off ->
      collapses to ~0.002 AU on the magnetosphere (Tony's call: largest
      active element sets the size). The empty-box Fly To is gone.
    * CAMERA TRACKING across animation frames -- IMPLEMENTED in Phase 4
      (June 12) and RENDER-CONFIRMED in the Phase 4 render-gate session
      (June 13) `[render-confirmed Mode 5]`. The view window translates
      with the body while the camera stays FREE (the user can orbit during
      playback). UI: 'Camera: track body across frames' combobox in the
      Per-frame elements group; requires redraw=True (already set).
      MECHANISM CHANGE (June 13 live fix): per-frame go.Frame(layout=...)
      scene ranges are UNRELIABLE for a 3D scene when the window is tiny
      relative to the body's offset from origin -- Plotly silently drops
      the per-frame range and autoranges the whole Sun-body span (the
      sodium-tail-off case: a 0.0045 AU cube 0.42 AU from origin swung to
      ~0.4 AU and went non-uniform; the body also rendered off-center and
      effectively invisible). FIX: save_utils._inject_camera_tracking
      injects a post_script that applies the body-centered window via
      Plotly.relayout on load (centers the body) and on every
      plotly_animatingframe (holds the window) -- the documented-reliable
      path for driving a 3D scene during animation; data stashed as
      fig._track_relayout_data keyed by frame date. Routes through
      _write_html so it reaches BOTH the browser-opened and the saved
      offline file (saved round trip render-confirmed). The frame.layout
      path is kept as a no-JS fallback; the relayout runs after the frame
      and wins. This IS the JS event-based follow-on the prior RESIDUAL
      parked (ADDENDUM_phase4 amendment C) -- now built.
      RESIDUAL (OPEN -- item 1 attempted June 13, RENDER-FALSIFIED, then
      REVERTED): dropping the scene from frame.layout (frames data-only, JS
      as sole per-frame window owner -- item 1) did NOT make the cube
      uniform. The render still showed the cube differing BY AXIS and
      swinging ~0.15-0.65 AU -- essentially unchanged. So the frame.layout/
      JS conflict was NOT the cause; the render caught the wrong diagnosis.
      Item 1 was pushed (373298d) then REVERTED (frame.layout restored),
      because it bought nothing and cost the large-window partial-hold plus
      the no-JS fallback -- the reverted 33aac56-equivalent behavior is the
      better baseline. REFINED DIAGNOSIS (next-session seed, NOT verified):
      Plotly re-autoranges the 3D scene per frame when frames carry data
      without an explicit range, overriding the JS relayout -- the cube
      differs by axis (autorange fits the asymmetric sodium tail per axis)
      and swings as the tail rotates. SUPPORTING EVIDENCE (console): track
      half-width 0.19612 AU (relayout target ~0.39 cube), but the swing's
      upper bound (~0.65) matches the static auto-scale "+/-0.606714 AU"
      full-orbit autorange -- the scene drifts toward the data-extent
      autorange. CENTERING still holds (relayout midpoint right); only
      SIZE/uniformity is uncontrolled. COSMETIC: Tony judged the wobble
      "not a visual problem"; load-bearing behavior (centering, shell-track,
      saved round trip, reticle) all render-confirmed. DEFERRED to a
      dedicated session with a repro that ACTUALLY RUNS in Tony's browser
      (prior two did not). Won't-fix (accept the wobble) is a legitimate
      close if autorange can't be cleanly suppressed during 3D frame
      animation.
      RETICLE (June 13) `[render-confirmed Mode 5]`: the center '<>' marker
      (a hand-aligned screen-space paper-coord annotation borrowed from the
      star viz, never pixel-exact) is suppressed under camera tracking via
      add_look_at_object_buttons(show_target_marker=_track_body is None) --
      at shell scale with one body there is nothing to disambiguate, and
      the eyeball error shows. Kept in all non-tracking and static views.
    * Directional arrow camera controls for Plotly 3D (Studio has 2D
      D-pad pan; no 3D equivalent) -- precise cameras without the
      mouse; aids shell-scale visual verification. (Promoted June 11.)
    * O16: auto-scale max() Sun-centered case PASSED (C6a, June 11);
      Mercury-centered case retests in v4.1 after the C6d fix.
**Tony:** Question: when we say render-confirmed Mode 5 does that mean the item is completed? Does it still belong in the open items? 
**Gap:** remaining for item 19: scene_aspectmode + scene_camera parity / read-on-load (next-session scope); camera-tracking per-frame autorange RESIDUAL (dedicated session); 3D arrow camera controls.

#### [L-042 | #20/N5] Shell-resolution GUI control (20/N5) + Fly-to view scaling (49)
<!-- L:042 status:OPEN upd:2026-06-11 section:D.Feature-A flag: rice:2/1/50/2 -->
  20/N5 shell-resolution GUI control (enabler; its backend partially exists
  since Session A -- bow-shock conic already parameterized, sphere-shell
  n_points per-config; remaining: create_magnetosphere_shape promotion +
  per-body density literals). 49 Fly-to view scaling (folds into the
  fixture list above). View-window design (49 + 19 + Studio parity).
  `[per chain unless tagged]`

#### [L-043] Exoplanet/binary synthetic objects hit Horizons fetch (id_type rejected)
<!-- L:043 status:OPEN upd:2026-06-16 section:D.Feature-A flag: rice:1/1/75/2 -->
- (June 16) OBSERVATION logged (pre-existing, NOT item 19.3 / Phase A).
  Exoplanet + binary system plots (static AND animated) route synthetic
  objects through the Horizons fetch path, which rejects their identifiers.
  Reproducible across TRAPPIST-1, TOI-1338 (binary), Proxima Centauri --
  every run, both modes. Console-only symptoms:
    - fetch_trajectory (palomas_orrery_helpers.py ~388) raises
      "id_type (X) not allowed" tracebacks: host_star, binary_star_a/b.
    - "Error fetching data ... id_type (exoplanet|barycenter) not allowed"
      for exoplanets and the system barycenter.
    - "Error fetching data for object 10" (Sun) dumps the full Sun
      properties block: location='@TOI1338_BARYCENTER ' (trailing space)
      is unresolvable -- Sun-relative-to-exo-center goes to Horizons too.
  ROOT: synthetic exo/binary objects carry internal TYPE tags
  (exo_host_star, exo_binary_star, exoplanet, barycenter) forwarded to
  Horizons as id_type; these are positioned by the exo synthetic generator
  and should never hit Horizons. Fetch fails -> caught -> synthetic
  positioning renders correctly (Tony Mode-5 clean; axis ranges right).
  IMPACT: cosmetic to the render; cost is tracebacks (can mask a real
  error) + spurious failed Horizons calls + a Sun-properties dump per
  exo-system plot.
  FIX DIRECTION (deferred): gate the Horizons fetch/data path to SKIP
  synthetic object types (exo_host_star, exo_binary_star, exoplanet,
  exo-system barycenter, Sun-relative-to-exo-center) instead of calling
  Horizons and catching the rejection. Bonus: helpers.py is CRLF
  (standard is LF) -- fold a line-ending normalize into that session.
  Tier: D.Priority-noise. Thread: helpers.py ~388 + id_type assignment in
  exoplanet_systems.py / celestial_objects.py.
**Gap:** gate the Horizons fetch/data path to SKIP synthetic types (exo_host_star/exo_binary_star/exoplanet/exo-barycenter/Sun-relative-to-exo-center); + helpers.py CRLF->LF.

### D.Feature -- Bucket B (editorial; open-ended) `[per chain]`

#### [L-044 | #22] Satellite (and minor-body) internal-structure shells
<!-- L:044 status:OPEN upd:2026-06-21 section:D.Feature-B flag: rice:3/3/90/3 -->
- **Extend internal-structure shells to satellites and minor bodies.** Today the
  layered internal-structure treatment (core / mantle / crust, named layers with
  sourced radii) lives on the planets and the Sun. This carries it to important
  MOONS first (e.g. the Galilean moons, Titan, Triton, Earth's Moon), then outward
  to ASTEROIDS and MINOR PLANETS. Each body gets sourced layer radii, a toggle,
  single-info-marker hover (km + AU), per the existing shell pattern. 20/N5
  (shell-resolution GUI control, L-042) is the on-ramp.
**Gap:** SIGNIFICANT design session first (Tony): which bodies first, which layers per body, sourcing per body (Fetched-vs-Recalled on every radius). Editorial / open-ended -- build only after the design stabilizes. Bucket B.

#### [L-045 | #N14] Miranda inclination tooltip
<!-- L:045 status:OPEN upd:- section:D.Feature-B flag: rice:1/1/90/1 -->
`[per chain]`
**Tony:** need description. 

### D.Feature -- Bucket C (architecture; design-before-code)

#### [L-014 | #2] Asteroid-belt migration decision
<!-- L:014 status:OPEN upd:2026-06-20 section:D.Feature-C flag: rice:1/1/75/2 -->
The asteroid belt renders via standalone create_main_asteroid_belt() in
asteroid_belt_visualization_shells.py, called directly (main L2021). It is
not in SHELL_CONFIGS (not a sphere) or CUSTOM_SHELLS (no checkbox-gated
toggle per shell -- the four belts have their own tk.IntVars at main L2883).
Decision: should the four belt geometries move into CUSTOM_SHELLS (like
rings and magnetospheres), or stay standalone?
**Gap:** design decision. Benefits: unified dispatch, factory hover standard,
one fewer standalone call path. Costs: belt geometry is scattered-point
clouds, not sphere or ring -- CUSTOM_SHELLS builders may need a new
convention. Low urgency; no bug, no user-visible gap.
[D.Feature-C: tag applied 2026-06-20 -- design-before-code]

#### [L-017 | #7] Tooltip rewiring globals() -> config fields
<!-- L:017 status:OPEN upd:2026-06-21 section:D.Feature-C flag: rice:2/3/50/3 -->
13 call sites in palomas_orrery.py (L9101-L9376) pass globals() to
build_shell_checkboxes() so it can look up tk.IntVar shell variables by NAME
(string). It works, but it is fragile: rename a variable and the lookup silently
misses, dropping a checkbox with no error -- invisible until someone notices the
missing toggle in the GUI. Recommended direction: build ONE explicit dict
{var_name: tk_var} (or a small registry/dataclass) at startup and pass it instead
of globals(), so a rename surfaces as a missing key, not a silent drop.
**Gap:** design decision first (dict vs dataclass vs registry), then thread the chosen object through all 13 call sites. Touches live UI wiring -- Mode-5 the GUI after. Design-before-code.
[D.Feature-C: tag applied 2026-06-20 -- design-before-code]

#### [L-046 | #N6] Studio encounter-generator -> preset-authoring capability (refactor + Artemis redo; coupled, two repos)
<!-- L:046 status:OPEN upd:2026-06-21 section:D.Feature-C flag: rice:3/3/75/3 -->
- **N6, reframed (Tony, 2026-06-21): the encounter generator is a NEW SKILL.**
  Beyond the original scope (refactor the Studio encounter-generator + redo the
  Artemis preset, coupled across the TWO repos), the larger intent is to
  generalize it into a PRESET-AUTHORING capability -- a reusable tool for producing
  many standard and special visualizations (flybys, close approaches, mission
  encounters, special framings) as gallery presets, not a one-off Artemis fix. N11
  rides. Design authority: ENCOUNTER_EXPORT_HANDOFF_v3.md (orrery repo); full
  verified specifics in git history / prior edition.
  `[per chain + @2f40d9d/@730b2bf verifications]`
**Gap:** design conversation first -- separate (1) the immediate refactor + Artemis redo from (2) the generalized preset-authoring vision; decide how much of (2) to scope now. Coupled across two repos. Design-before-code, Bucket C.

#### [L-047 | #N10] Note-composition structural refactor (behind N6)
<!-- L:047 status:OPEN upd:- section:D.Feature-C flag: rice:2/2/50/2 -->
- **N10** Note-composition structural refactor (behind N6). `[per chain]`
**Tony:** this description is unclear. Need to update the rice rating. 

#### [L-048 | #21/51] Animation track 21/51 -- core complete pending the v4 gate
<!-- L:048 status:PENDING-GATE upd:2026-06-11 section:D.Feature-C flag: rice:3/3/50/3 -->
- **21/51 Animation track -- CORE COMPLETE pending the v4 gate. Status
  June 11:**
  - Phases 1, 2, 2.5, 3A DONE; 3B conditionally confirmed (section C).
  - **PHASE 3 SESSION C -- DELIVERED + PUSHED @7b71c29,
    `[render-gated on ANIMATION_TEST_PROTOCOL_v4]`:** barycenter Sun fix
    (engine Sun contract: real trajectory / engine fetch / suppression --
    never a placeholder position); console-spam fix (O13a; quiet rebuilds,
    builder messages print once at allocation, zero builder edits); comet
    tails per frame as OPT-IN (Animation Settings checkbox, default off
    per O1; build_comet_tail_traces capture shim, the 240-line builder
    unchanged; VARIABLE-COUNT handling: per-frame max-probe + pad-to-max
    with invisible dummies -- live counts are non-monotonic, 9/7/5/6
    measured; MAPS excluded, disclosed); Mercury sodium tail as engine
    customer (checkbox-gated; its greyed placeholder skipped when live);
    U+N bow-shock hover disclosure (D.Movement remainder); one-line
    auto-scale (Auto cube = MAX of orbital and center-shell extents, never
    shell alone -- the Finding-1 inverse).
  - **ENGINE ARCHITECTURE (for the record):** rebuild-as-universal --
    builder(**frame_context) through the same dispatch convention as
    static; registry = 14 per_frame tags in CUSTOM_SHELLS + the indicator
    builtin; trace-count stability asserted loud, variable-count elements
    pad-to-max; engine Sun contract with suppression-over-fabrication;
    quiet rebuilds; live byte-budget guardrail (warn >150 KB/frame).
    Design authority: ANIMATION_ENGINE_DESIGN_v1.md (sec 8 footnote
    superseded by the greyed legend -- amend on next touch).
  - **REMAINING RIDERS after the v4 gate:**
    * Resolution-sweep follow-on: RESOLVED BY MEASUREMENT (Phase 4,
      June 12, ADDENDUM decision 3). The 7-decimal coordinate-rounding
      lever (PERFRAME_COORD_DECIMALS, applied at the build_perframe_traces
      chokepoint -- every engine element inherits it) roughly HALVES
      per-frame bytes: Earth magnetosphere FULL 133->68 KB/f, Jupiter
      FULL 79->43, sodium tail 46->31 (live-measured; decimal places are
      scale-safe at any heliocentric distance, unlike significant
      digits). Full-resolution geometry + rounding fits the per-body
      budget, so NO density reduction ships: gate 5(b) is moot in its
      original form (nothing reduced to judge), and the per-body density
      literal sweep is CLOSED AS NOT NEEDED (reopen only if multi-
      magnetosphere or 60-frame budgets bite in practice; all eight
      simultaneously measure 411 KB/f rounded -- the >150 guardrail
      warns correctly). create_magnetosphere_shape n-parameter promotion
      DONE (defaults byte-identical; doubles as 20/N5's backend).
    * measure_animation_html.py: add tkinter file-browser dialog (B5).
    * Camera tracking -> item 19 fixture list (above): IMPLEMENTED.
    * O14/O15 incoming from the v4 gate: comet-tail legend churn verdict;
      sodium particle count in per-frame mode (knob exists, 500 -> 250
      measured ~24.9 KB/f -- note rounding now takes 500 to ~31 KB/f,
      which may settle O15 without the knob).
  - Standing instruction kept: when deferring, smoke-test the animate
    pipeline to a KNOWN state.
**Gap:** the v4 gate (L-004); then the remaining riders listed in-block.
**Tony:** L-004 is done. need to discuss and clarify then update rice.  

### D.Parked (Tony's explicit call) `[per chain]`

#### [L-049 | #N8] Comet info-marker superposition cluster
<!-- L:049 status:PARKED upd:- section:D.Parked flag: rice:1/2/50/2 -->
`[per chain]`
**Tony:** need to verify mode 5. 

#### [L-050 | #N9] white -> red orbit-marker switch (osculating marker intentionally stays white)
<!-- L:050 status:PARKED upd:- section:D.Parked flag: rice:2/1/50/1 -->
`[per chain]`
**Tony:** need to verify mode 5. 

### D.Loose end to reconcile `[per chain; not re-verified]`

#### [L-051] Uranus pole-value prose inconsistency (Dec -15.10 vs stray -15.18)
<!-- L:051 status:OPEN upd:2026-06-21 section:D.LooseEnd flag: rice:1/2/50/1.5 -->
- **What it is.** Two different Uranus pole Declination values appear in prose:
  -15.10 (the load-bearing value actually used) and a stray -15.18 elsewhere.
  Reconcile to one (fix the stray) when next in that file.
- **Why the provenance scanner does NOT catch it (Tony's question).** The scanner
  flags a numeric token that LACKS a citation within its lookback window -- it
  checks for PRESENCE of a # Source, not AGREEMENT between two cited values. Both
  -15.10 and -15.18 likely sit within lookback of a citation, so each individually
  passes the "has a source" test; the scanner has no cross-value consistency check,
  so a contradiction between two separately-cited numbers slips through. A scanner
  BLIND SPOT, not a missed flag.
**Gap:** find both occurrences, confirm -15.10 is correct, fix the stray -15.18. Optional: log the scanner's no-consistency-check limitation as an enhancement candidate (fold into L-002/L-003, not its own item).

## E. AU-CONVENTION COMPLIANCE CLUSTER (standing convention; one sweep)

#### [L-052] AU-convention compliance sweep (GEO altitude hover missing AU; km+AU on all new hover)
<!-- L:052 status:OPEN upd:- section:E flag: rice:1/1/50/1 -->
- Inner-four bow-shock hover ("radii" only) `[verified @76c330e]`; GEO
  altitude hover missing AU `[per standing convention]`; confirm km+AU on
  any new hover at add time. (Session C's U+N bow-shock disclosure lines
  added no new numbers; existing km/AU values untouched.)

## F. CONSOLIDATION LOG (what each pass repaired)


- (June 7, v28 consolidation) RESTORED 2 leaked Movement-2 items + the v24
  sec5 batch; corrected the stale U3 "open"; UNIFIED the three animation
  records into 21/51; closed N13, N12; recorded Q2; moved Food Insecurity
  to a separate track; HEAD verifications. (Full detail: prior edition /
  git history.)
- (June 8) Recovered the N6 generator-refactor leak; recorded the two-repo
  coupling; Gallery section H stood up.
- (June 10) ANIMATION PASS 1: Phase 1 render-confirmed; Phase 2 delivered;
  PENDING June-8 items verified at HEAD and cleared; center-marker
  divergence root-caused (N3 + O5 + O6a = one disease); v27 axis/cone gap
  refined to non-center-only (O4); animate shell auto-scale found dead and
  annotated; new items from the O-log.
- (June 10, later) Phase 2 render-confirmed; Phase 3 GO (rebuild-universal
  directive); Session A delivered: the "one-site" wrapper claim CORRECTED
  by repo-wide grep (three sites); budget harness + gate 5(a) passed;
  grep -c chain-break lesson.
- (June 11, fix pass C2) v4 first run found 3 blockers; all root-caused
  with reproduction, not patched on guesses: the perihelion repro
  EXONERATED the engine math and convicted Plotly's frame-merge
  semantics (sticky visible); the doubling was two producers of one
  element (frame-1 block + engine); Mercury-centered was a coverage
  gap, not a trajectory bug (Tony's barycenter-class instinct pointed
  the way; the trigger differed). skip_elements threaded through the
  dispatch with a None-default regression test (HEAD-identical).
  Promoted: epoch-parser 'osc.' gap (D.Priority), <br> hovertext
  (D.Cosmetic), 3D arrow cameras (item 19).
- (June 11) Sessions B + C: engine delivered and conditionally confirmed
  (solar-system-scale visual gap identified as TOOLING -> item 19 with the
  go.Frame camera mechanism note); greyed-legend disclosure verified and
  accepted (supersedes the footnote; console notices demoted to dev
  diagnostics); B3-bonus barycenter bug root-caused (sentinel conflation:
  a fallback value is a CONTRACT) and fixed with
  suppression-over-fabrication; comet trace counts measured non-monotonic
  -> pad-to-max; capture-shim pattern adopted for the comet core (faithful
  by construction, hairy builder untouched); O13a spam fixed engine-side;
  scaling consolidated into item 19 per Tony's framing call (no separate
  track); section-G auto-scale and tier-decision questions CLOSED;
  provenance re-scan at d9460e2: Tier-1 = 0 held through the campaign.
- (June 14) Item 19.3 design session: SHA round trip verified (orrery 1288b51,
  gallery 2f40d9d); map-confirmed 4 scene sites (2 twins / 2 variants, prior
  3-site grep was stale); seam decision (a2) + Q2/Q3 settled; handoff drafted.
  No code. Divergence-audit seeded.

## G. OPEN QUESTIONS / TONY CALLS

#### [L-053] AU-convention sweep (section E): keep open, revisit
<!-- L:053 status:OPEN upd:2026-06-07 section:G flag: rice:3/1/50/2 -->
- AU-convention sweep (section E): KEEP OPEN, revisit (Tony, June 7).

#### [L-056] Phase 4 residuals: stale O2/O3 console wording; apsidal_markers em-dashes; MAPS per-frame wiring deferred
<!-- L:056 status:OPEN upd:2026-06-12 section:G flag: rice:1/2/50/2 -->
- **Phase 4 residuals** (June 12): O2/O3 console notice wording is
  slightly stale when magnetosphere opt-in is ON (the blanket "not yet
  rendered" remains true for sphere shells; engine prints its own
  allocation lines) -- amend on next touch. apsidal_markers.py carries
  4 PRE-EXISTING em-dashes (platform-neutrality flag, not Phase 4's).
  MAPS per-frame wiring DEFERRED per ADDENDUM_phase4 decision 1 (the
  two-site exclusion warning and partition design are captured there).
**Note (2026-06-17):** Mercury-centered auto-scale (O16) reads ~1 AU because
  get_animation_axis_range passes positions={} into calculate_axis_range_from_orbits;
  the non-Sun-center distance branch can't fire, so the Sun's heliocentric
  aphelion (~1.017 AU) is used as the fallback, giving a ~1.3 AU cube.
  Pre-existing; not introduced by the animation refactor. Workaround: use
  the orrery-side dtick/range field (item 19.3 Phase B) to override at
  generation time. Reopen as D.Priority only if the fallback causes
  confusion on other planet-centered animations (e.g. Jupiter-centered
  with Sun selected = ~5.5 AU, likely fine).
**Scoping (2026-06-18):** MAPS per-frame wiring scoped in handoff v29.
  The exclusion is one line (palomas_orrery.py L2324: `if name == 'MAPS':
  continue`). The builder (build_comet_tail_traces) is shared with all
  comets -- no MAPS-specific code needed. Prerequisite: review ADDENDUM_phase4
  decision 1 to understand the two-site exclusion warning before removing
  the gate. Main risk: frame-1 tail doubling (known pattern, known guard).
  Static path (plot_objects L6062) already handles MAPS. O2/O3 wording and
  apsidal em-dashes remain as separate sub-items.  
**Tony:** needs update. we worked on this. check mode 5. 

## H. GALLERY / STUDIO TRACK (website repo; low-activity)

(Unchanged this pass; carried verbatim from the June-10 edition.)

- **Repo source.** https://github.com/tonylquintanilla/tonyquintanilla.github.io
  -- owner WITH the 'l', repo name WITHOUT; branch main; public; HEAD
  verified June 8 == `2f40d9d`; custom domain palomasorrery.com; Studio file
  tools/gallery_studio.py (NOT root). Uploaded Studio byte-identical
  @2f40d9d.
- **Docs split:** WEBSITE repo documentation/ holds web_gallery_handoff.md +
  3d_axis_control_handoff.md `[verified @2f40d9d]`; ORRERY repo
  documentation/ holds the encounter-export design set incl.
  ENCOUNTER_EXPORT_HANDOFF_v3.md `[verified @730b2bf]`.
- **No Studio running ledger** by design (stand one up only if Studio work
  resumes in volume).
- **Joined items:** N6 (Bucket C) and item 19 (Bucket A) -- tracked in their
  orrery homes, cross-referenced here.
**Tony:** needs L-number, header, and update. 

#### [L-058] Open Studio items (May-5 handoff, checked @2f40d9d)
<!-- L:058 status:OPEN upd:2026-06-08 section:H flag: rice:3/3/50/3 -->
- **Open Studio items** (May-5 handoff; checked @2f40d9d where
  file-verifiable): encounter-export mission-type testing `[per handoff]`;
  camera capture NOT extracted `[verified]`; link-icon end-to-end test
  `[per handoff]`; content re-population through the Studio `[per handoff]`;
  gallery-card thumbnails ABSENT; About/Downloads/Contact pages ABSENT;
  og:image meta present (per-card previews unconfirmed).
- **Recently closed:** _enter_orrery_mode() DEFAULT_CONFIG reset
  `[verified @2f40d9d ~L4775]`; 'ongoing' status comment
  (spacecraft_encounters.py L60, verified).
**Tony:** this connects to another item on the studio preset generator refactor. 

---


