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

*59 live items; 45 need attention (`!`); 53 RICE-scored; 33 closed (section C, listed last). Find an `L-0NN` handle (Ctrl+F in VS Code) to jump to any item; search `| ! |` to list every gap. See "Using and maintaining this ledger" above for details.*

### A. Active Separate Tracks
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-001 | Food Insecurity (Earth System track) | OPEN | 4.3 | 2026-06-30 |
| ! | L-060 | ENSO Standalone Chart (Earth System track) | OPEN | 2.7 | 2026-06-18 |
| ! | L-071 | 2026 European heat dome -- track to resolution (dated scenario series) | OPEN | 2.5 | 2026-06-25 |
| ! | L-077 | 2026 US Midwest/Central heat dome -- migrating-centroid ongoing scenario | OPEN | 2.2 | 2026-06-30 |
| ! | L-078 | Provenance scanner: systematic coverage via module_atlas role classification | OPEN | 2.1 | 2026-07-04 |
| ! | L-063 | Orrery GUI Note text update | OPEN | 2.0 | 2026-06-21 |
| ! | L-062 | README refresh -- fold in handoff + ledger developments | OPEN | 1.5 | 2026-06-21 |
| ! | L-070 | Food Insecurity -- regional multi-country assembly (Sudan crisis shed) | OPEN | 0.9 | 2026-06-24 |

### B. Pending Action (Tony-side)

*(none currently)*

### D.Movement -- Movement track
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-008 | v24 sec5 precision batch (low-risk) | OPEN | 1.0 | 2026-06-21 |
| ! | L-061 | Magnetosphere-dipole frame coupling / seasonal roll | OPEN | 0.2 | 2026-06-21 |

### D.Priority -- Real bugs
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-012 | Osculating pre-fetch false-provenance messages | OPEN [CRIT] | 3.6 | 2026-06-21 |
|  | L-013 | Mercury 2019-epoch anomaly | DEFERRED | 0.1 | 2026-06-15 |

### D.Structural -- Dead code / honest shells
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-026 (#9) | palomas_orrery_helpers.py CRLF -> LF | OPEN | 2.2 | 2026-06-18 |
| ! | L-027 (#61) | Platform Neutrality (SystemButtonFace) | OPEN | 2.2 | 2026-06-18 |
| ! | L-025 (#N7) | Reduced to custom-geometry inline markers only | OPEN | 1.5 | 2026-06-18 |
| ! | L-068 | Static/animation pipeline consolidation -- remaining residuals (umbrella) | OPEN | 1.5 | 2026-06-23 |
| ! | L-028 | ASCII em-dash violation, comet_visualization_shells.py L257/505/519 | OPEN | 1.0 | 2026-06-11 |
| ! | L-015 (#5) | _info import cleanup (~89+87 imports, 2 files) | OPEN | 0.9 | 2026-06-18 |
| ! | L-016 (#6) | Archive dead shell functions | OPEN | 0.9 | 2026-06-18 |

### D.Cosmetic -- Polish
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

### D.Feature-A -- Bucket A (near-term)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-066 | MAPS per-frame comet-tail animation wiring | OPEN | 4.5 | 2026-06-23 |
| ! | L-040 (#19) | Plot-cube control parity + scaling/camera comprehensive review | OPEN | 1.5 | 2026-06-13 |
| ! | L-039 (#23) | Earth ionosphere shell | OPEN | 1.2 | 2026-06-21 |
| ! | L-042 (#20/N5) | Shell-resolution GUI control (20/N5) + Fly-to view scaling (49) | OPEN | 0.5 | 2026-06-11 |
| ! | L-043 | Exoplanet/binary synthetic objects hit Horizons fetch (id_type rejected) | OPEN | 0.4 | 2026-06-16 |

### D.Feature-B -- Bucket B (editorial)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-044 (#22) | Satellite (and minor-body) internal-structure shells | OPEN | 2.7 | 2026-06-21 |
| ! | L-045 (#N14) | Miranda inclination tooltip | OPEN | 0.9 | 2026-06-23 |

### D.Feature-C -- Bucket C (architecture)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-046 (#N6) | Studio encounter-generator -> preset-authoring capability (refactor + Artemis redo; coupled, two repos) | OPEN | 2.2 | 2026-06-21 |
| ! | L-017 (#7) | Tooltip rewiring globals() -> config fields | OPEN | 1.0 | 2026-06-21 |
| ! | L-067 | measure_animation_html.py file-browser dialog (B5) | OPEN | 0.8 | 2026-06-23 |
| ! | L-014 (#2) | Asteroid-belt migration decision | OPEN | 0.4 | 2026-06-20 |

### D.Loose end to reconcile
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-051 | Uranus pole-value prose inconsistency (Dec -15.10 vs stray -15.18) | OPEN | 0.7 | 2026-06-21 |

### E. AU-Convention Compliance
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-052 | AU-convention compliance sweep (GEO altitude hover missing AU; km+AU on all new hover) | OPEN | 0.5 | - |

### G. Open Questions / Tony Calls
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-053 | AU-convention sweep (section E): keep open, revisit | OPEN | 0.8 | 2026-06-07 |
| ! | L-056 | Phase 4 residuals: stale O2/O3 console wording; apsidal_markers em-dashes (MAPS per-frame wiring -> L-066) | OPEN | 0.5 | 2026-06-23 |

### H. Gallery / Studio Track
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-073 | Gallery export-emits-JSON -- fold the manual json_converter run into Export | OPEN | 1.6 | 2026-06-26 |
| ! | L-058 | Open Studio items (May-5 handoff, checked @2f40d9d) | OPEN | 1.5 | 2026-06-08 |
| ! | L-074 | Cull unused raw *_teaser.json in the gallery dir | OPEN | 0.9 | 2026-06-26 |

### W.Prep -- Web Publication prep (before Phase 0)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
|  | L-085 | LICENSE to repo root | PROPOSED | 4.0 | 2026-07-03 |
|  | L-086 | Attribution / credits page | PROPOSED | 2.8 | 2026-07-03 |
|  | L-087 | palomas_orrery_helpers.py computation/GUI split | PROPOSED | 2.0 | 2026-07-03 |

### W.Active -- Web Publication active phase
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
|  | L-088 | Two-sided pilot (Phase 0) | PROPOSED | 2.0 | 2026-07-03 |
|  | L-080 | Characterization harness (scene equivalence gate) | PROPOSED | 1.6 | 2026-07-03 |
| ! | L-079 | Shared assembler architecture (keystone -- redefined) | OPEN | 1.5 | 2026-07-03 |
|  | L-089 | Scene-spec shared skeleton + solar system vocabulary (Phase 1) | PROPOSED | 1.5 | 2026-07-03 |
|  | L-090 | Star cache inventory + wire format decision | PROPOSED | 0.5 | 2026-07-03 |

### W.Deferred -- Web Publication deferred (captured)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
|  | L-091 | Option E: unified front end | DEFERRED | -- | 2026-07-03 |
|  | L-092 | Embeddable scenes for educators | DEFERRED | -- | 2026-07-03 |
|  | L-093 | Educational guided explorations (specs as curriculum) | DEFERRED | -- | 2026-07-03 |
|  | L-094 | Community cache as commons | DEFERRED | -- | 2026-07-03 |
|  | L-095 | PWA / offline capability for classrooms | DEFERRED | -- | 2026-07-03 |
|  | L-096 | Web orrery aesthetic / feel design conversation | DEFERRED | -- | 2026-07-03 |

### C. Reconciled -- Done (closed; for the record)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
|  | L-003 | Protocol amendment candidates (for v3.29) | DONE | 5.4 | 2026-06-22 |
|  | L-065 | European heat wave heat map (Earth System track) | DONE | 4.8 | 2026-06-25 |
|  | L-064 | Provenance-scanner format sweep -- Earth System family | DONE | 4.5 | 2026-06-30 |
|  | L-075 | KMZ info-card "3+5" redesign -- compact header + tappable info balloon (Earth System engine) | DONE | 4.3 | 2026-06-30 |
|  | L-076 | Earth System shared module (earth_system_common) + 3+5 generalized to food | DONE | 4.3 | 2026-06-30 |
|  | L-097 | skills_index.py -- Skill Manifest auto-generation (process/tooling) | DONE | 3.2 | 2026-07-04 |
|  | L-069 | Food Insecurity Phase-2 -- Phase-5 "hidden Catastrophe" reveal (Darfur/Kordofan) | DONE | 2.8 | 2026-06-24 |
|  | L-072 | Gallery Studio WYSIWYG preview -- render through the real index.html viewer | DONE | 2.0 | 2026-06-26 |
|  | L-002 | Protocol -> Skills refactor (process/tooling) | DONE | 1.5 | 2026-07-04 |
|  | L-048 (#21/51) | Animation track 21/51 -- core complete pending the v4 gate | DONE | 1.5 | 2026-06-23 |
|  | L-047 (#N10) | Note-composition structural refactor (behind N6) | DONE | 1.0 | 2026-06-23 |
|  | L-050 (#N9) | white -> red orbit-marker switch (osculating marker intentionally stays white) | DONE | 1.0 | 2026-06-23 |
|  | L-020 (#26) | CUSTOM_SHELLS tooltip verification | DONE | 0.9 | 2026-06-22 |
|  | L-049 (#N8) | Comet info-marker superposition cluster | DONE | 0.5 | 2026-06-23 |
|  | L-004 | Apply C2 fix pass + run ANIMATION_TEST_PROTOCOL_v4_1, push | DONE | -- | 2026-06-17 |
|  | L-005 | Commit protocol v3.28 (or v3.29) to repo root | DONE | -- | 2026-06-17 |
|  | L-006 | Mercury +0.2 R_M northward dipole offset | DONE | -- | 2026-06-20 |
|  | L-007 | Bow-shock hover disclosure remainder | DONE | -- | 2026-06-11 |
|  | L-009 | Dipole cluster: envelope tie / offset direction / remaining cones / half_len_frac | DONE | -- | 2026-06-20 |
|  | L-010 | Keplerian epoch parse fails on 'osc.' suffix | DONE | -- | 2026-06-12 |
|  | L-011 | Pass-C2 v4 blockers (3) + B3-bonus barycenter Sun bug | DONE | -- | 2026-06-11 |
|  | L-018 (#8) | Dead create_sun_direction_indicator imports (verify remainder) | DONE | -- | 2026-06-18 |
|  | L-019 (#13) | Neptune ring info-marker rotation (verify + close) | DONE | -- | 2026-06-18 |
|  | L-021 (#28) | Neptune superimposed info markers (verify + close) | DONE | -- | 2026-06-18 |
|  | L-022 (#40) | Asteroid belt hover -> single info marker | DONE | -- | 2026-06-18 |
|  | L-023 (#N2) | Saturn/Uranus ring marker placement | DONE | -- | 2026-06-18 |
|  | L-024 (#N4) | Planet 9 sphere n=50 -> 20/25 | DONE | -- | 2026-06-18 |
|  | L-029 | v25 D3 dead-code annotations + small-body analytical tail | DONE | -- | 2026-06-18 |
|  | L-036 | O11 greyed-legend display-name verdict: NO item needed | DONE | -- | 2026-06-11 |
|  | L-041 | Item 19.3 axis-control round trip (P1/P2/Phase A/Phase B + toggle follow-on) | DONE | -- | 2026-06-16 |
|  | L-054 | Gate 5(b): full resolution ships, rounded -- render-confirmed | DONE | -- | 2026-06-13 |
|  | L-055 | O14/O15 verdicts arrive with the v4 gate (comet legend churn; sodium particle count) | DONE | -- | 2026-06-17 |
|  | L-057 | Animation auto-scale-vs-shells + Phase 3 tier decision -- CLOSED | DONE | -- | 2026-06-11 |

<!-- INDEX:END -->

---

## DETAIL / RECORD

## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)

#### [L-001] Food Insecurity (Earth System track)
<!-- L:001 status:OPEN upd:2026-06-30 section:A flag: rice:3/3/95/2 -->
- **Phase-1 build COMPLETE, render-confirmed (Mode-5, ge_sudan.jpg, built on
  03630ae).** Module: food_insecurity_generator.py -- new dedicated vector/
  categorical generator (NOT a bend of run_scenario); 189 area polygons, full
  phase1-5 balloon breakdown, transcribed national totals (never summed),
  legend + national ScreenOverlay cards, framing folder, optional Plotly teaser.
  KMZ byte-verified: Beliel balloon shows Phase 5 = 26,411 under mapped P4 (the
  hidden Catastrophe made visible). Provenance scanner Tier-1 = 0 (but see L-064
  -- that clean is currently a false clean for this module).
- **Discrepancy resolved (file wins):** phase5_population>0 is in 10 areas, not
  23 as the manifest prose said; all 10 are mapped P4. Built to the file.
- **Provenance flags carried forward:** phase ramp hex SAMPLED from report p.7
  legend (not IPC published hex); report has NO formal recommended-citation line
  (CITATION assembled from title page); per-area confidence_level/hfa_value shown
  as RAW values (no word-legend in report to map them). All open to retune.
- **Module name CONFIRMED (no longer a proposal): food_insecurity_generator.py**
  -- standalone-runnable via __main__ -> run().
- **KMZ naming convention (Earth System family):**
  data/<SCENARIO_ID>_blockbuster.kmz. Food layer SCENARIO_ID =
  "food_insecurity_sdn" (Sudan) -> data/food_insecurity_sdn_blockbuster.kmz;
  mirrors the heat scenarios (e.g. data/europe_2026_blockbuster.kmz). Generator
  also emits the two ScreenOverlay PNGs and <ID>_teaser.html. Those overlay names
  are now BUILD-STAMPED -- legend_<ID>_<YYYY-MM-DD-HH-MM>.png and
  intel_<ID>_<stamp>.png (one stamp per build, shared by both cards; prior copies
  cleaned) -- so a regenerated KMZ never reuses a filename Google Earth has
  cached; the KMZ filename itself is unchanged so --preload still matches. The
  food_insecurity_<region> prefix is LOAD-BEARING: the controller's
  --preload food_insecurity globs data/food_insecurity_*_blockbuster.kmz (single
  source; the GUI launcher delegates to it -- see L-076), so future regional
  layers (L-070: SS/TD/CF/ET) must follow food_insecurity_<code>_blockbuster.kmz
  to be picked up.
- **GUI registration (DONE).** Earth System Viewer
  (earth_system_visualization_gui.py) at b7650bb -- "Google Earth Food
  Insecurity Layers" section + launcher button -> launch_food_insecurity_layers(),
  which now DELEGATES to the controller (--preload food_insecurity) instead of
  globbing itself (single-source; see L-076); existing heat-wave launcher renamed
  KML -> KMZ. Dashboard (palomas_orrery_dashboard.py): Food Insecurity Generator +
  Controller buttons DONE (Mode-5 confirmed, 1b74bf1). Viewer scroll fix
  (97c21e1): the content area is wrapped in a scrollable canvas so the growing
  food/heat button sections stay reachable at any window size / when maximized
  (the food section had fallen below the fold).
- **KMZ "3+5" parity + tappable i-pin (DONE; c81bb3b; Mode-5 iOS-confirmed,
  IMG_1153/1154).** The food KMZ adopted the heat "3+5" card (L-075) via the
  shared module (L-076): the fixed full-text intel ScreenOverlay shrank to a
  compact header (title + period + "tap the (i) pin"), and the four invisible
  framing placemarks became ONE visible tappable "i" pin whose CDATA balloon
  carries the full briefing (National summary -> hidden Catastrophe -> map-color
  note -> Key drivers -> Middle East line -> "does not assert" -> Source/citation).
  All by reference to the existing transcribed constants -- no synthesis, no new
  numeric literals, provenance unaffected. On iOS the <h4> sections render fine;
  the GE "content controlled by the author" banner is app chrome (full-screen web
  sheet), harmless. run() gained a scenario_id parameter; food __main__ now opens
  the shared picker instead of auto-running Sudan.
- **Stale-card episode (resolved -- deploy path, not code).** The old card
  persisting on the phone through layer/file deletion was a missed
  data/ -> assets/ copy of the regenerated KMZ, NOT a Google Earth cache fault.
  Lesson: confirm the DEPLOY path before theorizing a cache. The build-stamped
  overlay names (above) were kept as cheap cache-bust insurance.
- **Still open under this track:** Deferred sub-layers split out: Phase-5 reveal
  -> L-069; 39 IPC call-out points (HFA-bag/IDP symbols) and the Jun-Sep /
  Oct-Jan projections remain deferred per original scope.
**Ref:** MANIFEST_food_insecurity_sudan_v2.md; HANDOFF_food_insecurity_build_v2.md
(built on 03630ae); cross-ref L-064, L-069.

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

#### [L-070] Food Insecurity -- regional multi-country assembly (Sudan crisis shed)
<!-- L:070 status:OPEN upd:2026-06-24 section:A flag: rice:2/3/45/3 -->
- **Extend the food-insecurity view across the Sudan-war refugee shed:** Sudan
  (have, SD) + South Sudan (SS) + Chad (TD) + CAR (CF) + Ethiopia (ET). Each is a
  SEPARATE IPC analysis / separate manual Mapping Tool fetch (bot-block wall) with
  its own analysis period -- combined view must LABEL per-country periods, never
  blend (cross-border form of "don't compare across periods").
- **Generator already country-agnostic** (reads country/area/phase from the
  GeoJSON); regional = ingest a file set + per-country period labels + per-country
  attribution + multi-country LookAt. Encoding identical per country (choropleth +
  L-069 P5 dots).
**Gap:** DATA-ACQUISITION GATED. Confirm current IPC availability + period per
neighbor at fetch time (Tony, manual). Scope: which neighbors in v1.
**Ref:** L-001 (parent), L-069 (P5 dots reused per country); food_insecurity_generator.py.

#### [L-071] 2026 European heat dome -- track to resolution (dated scenario series)
<!-- L:071 status:OPEN upd:2026-06-25 section:A flag: rice:3/3/70/2.5 -->
- **Follow the ongoing 2026 European heat dome across its lifetime as a dated
  scenario series** -- the Western Heat Dome (Mar 14/17/18) pattern: one new dated
  europe_* scenario per captured day, NOT one scenario auto-advancing its date.
  Same chassis as europe_2026 (wet-bulb spine + C-only air-temp pins,
  fetch_era5_heatwave / Open-Meteo archive). europe_2026 (21 Jun) is entry #1,
  built and closed under L-065.
- **Next:** a new dated scenario for the 27-28 Jun peak, once Open-Meteo's archive
  reaches those dates (a few days' lag). New date = fresh fetch, no cache collision.
- **Carried forward from L-065 (closed):** (a) WWA attribution watch -- update the
  line across the series if a study publishes; (b) Sentinel-3 LST surface snapshot --
  optional separate artifact.
- **Close when:** the dome resolves and the series is complete.
**Ref:** L-065 (build + chassis, closed); scenarios_heatwaves.py; Western
dated-series precedent (scenarios_western_heatwave_march_2026.py).

#### [L-077] 2026 US Midwest/Central heat dome -- migrating-centroid ongoing scenario
<!-- L:077 status:OPEN upd:2026-06-30 section:A flag: rice:3/3/60/2.5 -->
- New L-item (not a sibling of L-071) -- the migrating centroid plus the
  advancing reanalysis/forecast seam is its own design object, not another
  dated snapshot. Track: Gulf Coast bullseye -> St. Louis (~Jul 1) ->
  Chicago (~Jul 4) -> forecast retreat into the High Plains.
- ERA5T lag confirmed ~5 days behind real-time, D-5 typically by 12 UTC
  (Copernicus C3S / ECMWF CDS docs, retrieved 2026-06-30) -- so today there
  is no observed wet-bulb field yet for the June 27-Jul 1 peak.
- Design: ongoing scenario per the L-071 pattern (one dated scenario per
  captured day, chassis shared with europe_2026/scenarios_heatwaves.py),
  but with the forward/migrating segment shown as a forecast ENVELOPE
  (Show-the-Envelope convention) and the already-happened segment as solid
  reanalysis once ERA5T catches up -- the advancing seam is the honest,
  teachable object.
- El Nino backdrop noted as context only (L-060) -- causal restraint, no
  drawn connection.
**Gap:** scaffold the dated-scenario module once ERA5T coverage reaches the
event window (NOAA WPC June 27-29 peak + ~5-day lag -> earliest observed
coverage ~early July). Forecast-vs-reanalysis visual treatment is the open
design detail at build time.
**Ref:** NOAA WPC; Copernicus C3S/ECMWF CDS ERA5T docs (retrieved 2026-06-30);
design conversation this session; cross-ref L-071 (sibling pattern, not
parent), L-060 (El Nino context, no causal claim).

#### [L-078] Provenance scanner: systematic coverage via module_atlas role classification
<!-- L:078 status:OPEN upd:2026-07-04 section:A flag: rice:3/3/70/3 -->
- **Root cause (why files get missed in the first place).** provenance_scanner.py
  gates display-string scanning on a hand-maintained narrative_files allow-list;
  a new file is invisible until someone notices and adds its name. The scanner
  already solved this once, structurally, for one family -- is_shell_file =
  module_name.endswith('_visualization_shells') auto-includes by pattern, no
  list-editing required -- but that fix was never generalized.
- **module_atlas.py already does most of what's needed and is more complete than
  the scanner's own list.** classify_role() tags every module (data / scenario /
  rendering / rendering-shells / cache / computation / gui / pipeline / utility /
  devtool / legacy / other), with 'other' as an honest catch-all rather than a
  silent drop. Its 'data' role already includes 5 catalog/constants files NOT in
  narrative_files (exoplanet_coordinates, star_properties, stellar_data_patches,
  stellar_parameters, messier_catalog); its 'scenario' role already cleanly
  groups the heat/coral/western family the scanner has no equivalent for. The two
  tools have drifted apart from each other despite Tony running them together --
  nothing actually diffs their outputs. (Minor, telling: food_insecurity_generator
  -- the one file properly in narrative_files -- isn't in module_atlas's ROLE_MAP
  either, so it currently shows 'other' there. Both lists are hand-maintained;
  both have independently drifted.)
- **Design, two checks, both surfacing in PROVENANCE_AUDIT.md (Tony's call --
  that's the output actually reviewed every run, not module_atlas's):**
  1. MISSING CATEGORIES (file-level). Replace/extend narrative_files with
     role-driven inclusion: any module classified data / scenario / rendering /
     rendering-shells gets scanned automatically via module_atlas.classify_role.
     Any module landing in 'other' that contains claim-shaped string content
     gets a new "COVERAGE GAPS -- needs role classification" section in the
     audit output. Mechanical, low risk, the more tractable of the two builds.
  2. MISSING FIELDS (vocabulary-level). Found the exact hook point:
     _extract_string_units (provenance_scanner.py ~L711-721) walks every AST
     string Constant, runs extract_numeric_claims(), and on zero claims just
     `continue`s -- the string vanishes with no trace. Fix: a second, looser
     pattern at that exact branch -- number directly followed by 1-4 letters/%/$
     not matched by NUMERIC_CLAIM_RE -- logged as a near-miss instead of dropped,
     in a new "VOCABULARY GAPS -- unrecognized unit candidates" section. Runs
     only on already-covered files (check 1 handles files missing entirely), so
     naturally narrower scope than a whole-file sweep.
  3. The F/C bare-degree gap itself (KNOWN now, not a near-miss) lands directly
     in NUMERIC_CLAIM_RE as its own fix, separate from the near-miss MECHANISM
     being built to catch the next unknown gap.
- **Noise risk on the near-miss check (the harder of the two, flagged not
  solved).** A loose number+token pattern will catch ordinals ("2nd"), version
  strings ("v3.29"), multipliers ("3x") as false near-misses unless explicitly
  excluded. Needs scratch-testing against the real corpus and an eyeballed
  false-positive rate before going live -- not a guess-and-ship.
- **Architecture: scanner imports classify_role from module_atlas.py directly**
  (Tony: no strong preference, deferred to whatever reliably catches gaps every
  run). One-directional, no third shared module. Default unless revisited.
- **Effort framing (Tony's explicit precedent, 2026-06-30): the original scanner
  took ~10 sessions with multiple Gemini cross-checks to harden.** Not treating
  this as a quick patch. Check 1 (categories) is the tractable mechanical build.
  Check 2 (vocabulary near-miss) is the one likely to need the same kind of
  cross-check / corpus-tuning the original scanner got.
- **STATUS (July 4, 2026): step (1) is LIVE -- role-driven inclusion landed.**
  The scanner at HEAD imports classify_role from module_atlas and uses
  NARRATIVE_ROLES = {data, scenario, rendering, rendering/shells, computation}
  additively over the legacy narrative_files allow-list (line 635-639). The
  COVERAGE GAPS section is working (4 modules flagged: shell_configs 91,
  food_insecurity_generator 1, orrery_rendering 1, smoke_rotation_axis 1).
- **First full run under new coverage: Tier-1 = 104** (all score 16: V=4
  recalled x C=4 public-facing display strings) across 26 modules. Largest
  contributors: idealized_orbits.py (23 findings), paleoclimate_wet_bulb_full
  (11), paleoclimate_human_origins_full (9), paleoclimate_visualization_full (7),
  planet_visualization_utilities (7), sgr_a_grand_tour (6),
  scenarios_western_heatwave_march_2026 (4), sgr_a_visualization_core (4),
  exoplanet_coordinates (4). These are real, previously-invisible uncited
  display strings -- the predicted "heavy first run" from the design. The
  previous Tier-1=0 was true only for the smaller file set the legacy
  allow-list covered.
- **Carried forward from L-064 (closed, superseding this item):** F/C vocabulary
  gap; energy_imbalance.py (corroborated independently by L-060's own deferred
  Phase-2 note -- ~47 candidate hits, zero citation markers found in a manual
  proxy check); paleoclimate_wet_bulb_full / paleoclimate_human_origins_full
  (manual proxy shows heavy citation density -- likely another false-clean, same
  shape as scenarios_heatwaves.py) vs paleoclimate_visualization_full (high claim
  volume, thin citation density -- likely the riskier one, same shape as
  scenarios_western_heatwave_march_2026.py); star_notes.py:1257 (still open,
  pre-existing, reconcile in the same pass).
**Gap:** step (1) done. Remaining: (a) triage the 104 Tier-1 findings across
26 modules -- cite, remove-and-note, or add to provenance_exceptions.json per
the three-outcome rule; (b) resolve the 4 COVERAGE GAP modules (add to ROLE_MAP
or narrative_files); (c) step (2) near-miss vocabulary detector (design
converged on hook point, tuning NOT done); (d) step (3) F/C bare-degree fix to
NUMERIC_CLAIM_RE. Triage (a) is the heavy lift; (b-d) are mechanical once (a)
establishes the baseline.
**Ref:** provenance_scanner.py (_extract_string_units ~L711-721, narrative_files
~L623, NARRATIVE_ROLES ~L635, classify_role import ~L216, coverage-gap report
~L1271-1283); module_atlas.py (classify_role, ROLE_MAP); L-064 (closed
predecessor); PROVENANCE_AUDIT.md (July 4, 2026 run: 115 files, 666 findings,
Tier-1 = 104).

## PENDING ACTION (Tony-side)

## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)

### Strategic status -- shell-consolidation + animation refactor (CLOSED, for the record)
(Moved from B. Strategic Status, 2026-06-22; no L-number, historical record. The animation
"final gate pending" noted below PASSED at L-004 / v4.1, June 17.)

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

---

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
**DONE (2026-06-22, verified in code @26e58b2):** all six magnetosphere bodies carry a
SOURCED dipole_cone in CUSTOM_SHELLS (Mercury, Earth, Jupiter, Saturn, Uranus, Neptune);
implementation + provenance gate cleared. The body text above is the June-13 state, now
superseded. Only the rolling-cone coupling remains -- tracked as L-061.
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

#### [L-002] Protocol -> Skills refactor (process/tooling)
<!-- L:002 status:DONE upd:2026-07-04 section:C flag: rice:3/3/50/3 -->
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
- **COMPLETED July 4, 2026.** Designed with Claude Opus 4.6 (two pre-design
  sessions: L002_SKILLS_PREDESIGN.md, L002_SKILLS_PREDESIGN_v2.md). Built with
  Claude Fable 5 via collegial relay. Tony integrated and deployed.
  Eight skills at v1.0, all cut from palomas_orrery @ b29ad3f8 (gallery-pipeline
  also from tonyquintanilla.github.io @ 89c8bf30):
  orrery-coding-conventions, safe-file-editing, agentic-pre-test,
  horizons-orbital-mechanics, provenance-discipline, earth-system-pipeline,
  gallery-pipeline, ledger-and-session-records.
  Protocol v3.30 installed; version history moved to ledger appendix.
  Extraction audit: documentation/MAPPING_TABLE_L002.md (every v3.29 line mapped;
  deliberate duplication registry for future amendments).
  Reviewed by Opus 4.6 against HEAD @ 33f0b148 before deployment.
  Skills 6-8 are first-time capture (~2/3 of skill content): knowledge that
  previously lived only in handoffs and code.
- **Scanner carve-out (design question, decided):** skills contain numeric claims
  (AU conversion, reference distances) with prose attribution rather than
  # Source: comments. Carve-out: "skills cite by prose; masters live in cited .py
  code." The scanner covers the code; the skills describe conventions whose
  authoritative instances are under scanner coverage. No exceptions entries needed
  unless scanner scope widens to .md files.
- **Follow-on:** skills_index.py devtool (L-097) -- same pattern as
  ledger_index.py; kills manifest-table drift.
**Gap:** none -- move to section C.
**Ref:** documentation/MAPPING_TABLE_L002.md, documentation/LEDGER_version_history_block.md, documentation/README_DEPLOYMENT.md, documentation/README_DEPLOYMENT_v2.md, documentation/L002_SKILLS_PREDESIGN.md, documentation/L002_SKILLS_PREDESIGN_v2.md, skills/*.

#### [L-020 | #26] CUSTOM_SHELLS tooltip verification
<!-- L:020 status:DONE upd:2026-06-22 section:C flag: rice:1/2/90/2 -->
Verify that every CUSTOM_SHELLS entry in shell_configs.py has a tooltip
and that the tooltip text is accurate. CUSTOM_SHELLS covers rotation axes,
sodium tail, magnetospheres, bow shocks, radiation belts, rings, and
field-aligned currents across Moon, Pluto, Mercury, Venus, Earth, Mars,
Jupiter, Saturn, Uranus, Neptune.
**Gap:** none -- move to section C.

#### [L-047 | #N10] Note-composition structural refactor (behind N6)
<!-- L:047 status:DONE upd:2026-06-23 section:C flag: rice:2/2/50/2 -->
- **N10** Note-composition structural refactor (behind N6). `[per chain]`
**RETIRED (2026-06-23, Tony):** undetermined -- the N10 'note-composition refactor'
scope was never recoverable. Closed as undetermined; if it matters it will resurface.
**Gap:** none -- move to section C.

#### [L-048 | #21/51] Animation track 21/51 -- core complete pending the v4 gate
<!-- L:048 status:DONE upd:2026-06-23 section:C flag: rice:3/3/50/3 -->
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
**Gap:** none -- move to section C.

#### [L-049 | #N8] Comet info-marker superposition cluster
<!-- L:049 status:DONE upd:2026-06-23 section:C flag: rice:1/2/50/2 -->
`[per chain]`
**Mode-5 confirmed (2026-06-23, Tony):** comet info-markers no longer superimposed. DONE; move to C on next housekeeping.
**Gap:** none -- move to section C.

#### [L-050 | #N9] white -> red orbit-marker switch (osculating marker intentionally stays white)
<!-- L:050 status:DONE upd:2026-06-23 section:C flag: rice:2/1/50/1 -->
`[per chain]`
**RETIRED (2026-06-23, Tony):** undetermined -- no recollection of an orbit-color problem. Closed as undetermined; will resurface if real.
**Gap:** none -- move to section C.

#### [L-065] European heat wave heat map (Earth System track)
<!-- L:065 status:DONE upd:2026-06-25 section:C flag: rice:3/3/80/1.5 -->
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
- CLOSED 2026-06-25 (on 4685906): Mode-5 verified -- teaser (Gosport 36.1C pin,
    source visible, single title, "Click 3D Earth" CTA restored) + KMZ card (peak
    auto-filled, no [TO-FETCH]). Final record correction: UK -> Gosport 36.1C
    (Met Office, 24 Jun); attribution dated to Climate Central CSI (24 Jun 2026);
    Tama upgraded to AEMET primary. Tier-1 = 0. Parked, non-blocking: Sentinel-3
    LST stage-1 snapshot (separate artifact); WWA rapid study to supersede the CSI
    line if it publishes.
**Gap:** none -- move to section C.
**Ref:** existing ERA5/Copernicus heat-map framework; Copernicus CDS (ERA5 2m
temp) + Sentinel-3 LST; EU Copernicus Climate Change Service (C3S); L-001 + L-064
(two-tier on-layer text + scanner-format sweep). Current-event context: 2026
European heatwaves (record June temps; deaths reported across FR/UK/IE/ES/AT/DE/
SI), retrieved 2026-06-22.
**Note:** WATCH: World Weather Attribution rapid study on the June 2026 event. If it
  publishes, it is the strongest citable attribution -- replace the CSI/C3S line

#### [L-069] Food Insecurity Phase-2 -- Phase-5 "hidden Catastrophe" reveal (Darfur/Kordofan)
<!-- L:069 status:DONE upd:2026-06-24 section:C flag: rice:2/3/95/2 -->
- **BUILT + RENDER-CONFIRMED (Mode-5, ge_sudan.jpg 2026-06-24), committed 7923ac2.**
  10 maroon proportional dots in a toggle-able folder "Phase 5 (Catastrophe)
  populations (area level)", one per area carrying a mapped Phase 5 population (all
  mapped P4): Beliel 26,411 ... Kadugli 930. Sized area ~ population (sqrt); placed
  at each area's representative interior point. Renders correctly clustered in North
  Darfur, South Darfur (Nyala) and South Kordofan.
- **Pure IPC passthrough -- zero hardcoded/composed/summed numbers.** Balloon reads
  only area_name / overall_phase / phase5_population / phase5_percentage / population
  at runtime. "Catastrophe" (population term) used throughout; "Famine" (area term,
  none here) appears nowhere on the dots -- verified in KMZ bytes.
- **Dot-size legend key added** (Mode-5 follow-up, approved): legend card shows a
  large + small maroon dot keyed to the data's actual max/min phase5_population
  (read at runtime, not hardcoded), caption "larger = more people". Render-confirmed.
- **Causal-restraint wording tightened:** removed "the reader connects the pattern"
  from C3. C3 now ends "It draws no causal arrow of its own."
- **PRINCIPLE BANKED (generalizes to L-070 and every sensitive layer):** state the
  basis for the visualization; do NOT hand the lay reader a connection we will not
  draw ourselves. "The reader connects the pattern" is buck-passing -- naming the
  basis is honest, outsourcing the inference is not. (Tony, 2026-06-24.)
- **Scanner CATCHES the module (real clean, not false):** L-064 part-1 (allow-list)
  + narrow vocab add (people|persons?|percent|%). Tier-1=0, zero family ripple
  (star_notes:1257's "billion" trigger deliberately deferred to the L-064 sweep).
**Gap:** none -- move to section C.
**Ref:** L-001 (parent); L-064 (scanner); food_insecurity_generator.py; ge_sudan.jpg.
**Tony:** promote the "principle banked" to the protocol at the next update.
*Addressed: earth-system-pipeline skill captures this as the restraint
discipline's core stance (v3.30, L-002).*

#### [L-075] KMZ info-card "3+5" redesign -- compact header + tappable info balloon (Earth System engine)
<!-- L:075 status:DONE upd:2026-06-30 section:C flag: rice:3/3/95/2 -->
- **Problem.** The KMZ intel card was a fixed-size matplotlib PNG ScreenOverlay
  pinned top-left -- it could not reflow and collided with the Google Earth search
  bar on mobile, the long briefing unreadable on a phone.
- **"3+5" redesign (earth_system_generator.py; built on 9007ea3 -> pushed 3ba4e8a).**
  (3) intel card shrunk to a compact always-on header (title + date + "tap the (i)
  pin" hint) + a tappable info "i" Placemark at the grid centroid whose balloon
  carries the full briefing. (5) population-exposure key folded into the balloon;
  risk-scale colorbar moved bottom-right -> right-edge-centered, off the GE nav/3D
  buttons; header dropped below the mobile search bar. New helpers
  create_info_placemark + _briefing_to_html; producer-level change in run_scenario
  / build_spikes_kml.
- **Key fix -- CDATA.** simplekml 1.3.2 entity-escapes description fields by default
  (HTML would render as literal tags); wrapping the balloon in <![CDATA[...]]> makes
  simplekml emit it unescaped (base.py leaves CDATA blocks untouched), so GE renders
  it as HTML -- matching the proven desktop probe.
- **Structural win (parallel-pipeline).** Fix landed in the producer (run_scenario /
  build_spikes_kml), so every heatwave / coral / coastal scenario inherits 3+5 on its
  next regeneration -- not a per-europe_2026 edit.
- **Verified.** py_compile; ASCII/LF; synthetic KML smoke (CDATA balloon, briefing
  reflow, exposure key, repositioned overlays, pop-legend ScreenOverlay removed).
  Mode-5 (Tony, 2026-06-29): europe_2026 regenerated (cached ERA5, offline) and
  confirmed on DESKTOP + iPad + iPhone across Chrome / Bing / Safari -- balloon
  renders everywhere, collision gone, readable. iPhone full-screen sheet is the
  cleanest render; iPad docks the balloon inline. Gallery KMZ pushed d25fd93.
- **iOS banner (app chrome, not the KMZ).** Only the iPhone shows the "content is
  controlled by the author... do not enter passwords" banner: at phone size GE
  presents the balloon as a full-screen web sheet (which carries the standard safety
  banner); the iPad docks it inline (no sheet, no banner). Same file, same HTML;
  harmless (no input field), not switchable from the KML side.
- **Polish (delivered this session; 2 lines, verified; LANDS on the next europe_2026
  regenerate + gallery push).** header screenxy y 0.90 -> 0.84 (iPhone search-bar
  clearance); pin label scenario_id -> title so it matches the balloon heading
  ("Europe Heat Dome (June 2026) - tap for details"). Both Tony-approved. Only
  remaining action on this block; a quick re-confirm on the next regenerate closes it.
- **Dead code surfaced.** create_pop_legend_card is now unused (exposure key folded
  into the balloon); left defined to keep the live push minimal-risk -> remove in the
  L-068 dead-code sweep, not its own push.
- **Generalized to the family (this session -> L-076).** create_info_placemark +
  the briefing-to-HTML helper were extracted to earth_system_common.py and the
  3+5 card + tappable i-pin applied to the FOOD generator too; the picker was
  also generalized (ScenarioPicker). Heat balloon verified byte-identical.
**Linked:** chassis from L-065 (europe_2026 build); series tracked under L-071;
dead-code removal -> L-068. Icon uses remote Google info-i.png (probe parity); bundle
a local icon only if the iOS pin glyph misbehaves.
**Gap:** none -- move to section C.
**Ref:** earth_system_generator.py (run_scenario, build_spikes_kml, build_impact_kml,
create_intel_card, create_info_placemark, _briefing_to_html); simplekml 1.3.2 base.py
CDATA behavior.

#### [L-076] Earth System shared module (earth_system_common) + 3+5 generalized to food
<!-- L:076 status:DONE upd:2026-06-30 section:C flag: rice:3/3/95/2 -->
- **What.** Extracted the engine-agnostic KMZ/UI helpers shared by the heat and
  food generators into a new module, earth_system_common.py, retiring the
  heat<->food duplication before it set in: briefing_to_balloon_html();
  create_info_placemark(kml, title, date, briefing, lat, lon, extra_html="") --
  the tappable "i" pin + CDATA balloon, with the heat population-exposure key now
  passed in via extra_html rather than baked in; and ScenarioPicker(scenarios,
  run_fn, ...), a generic Tkinter menu whose run_fn(scenario, status_callback) is
  injected (heat passes run_scenario, food passes a small adapter over its run()).
  Both generators import from it; both __main__ blocks launch via the shared
  picker.
- **Food 3+5 parity (detail under L-001).** With the shared helpers in place, the
  food KMZ gained the compact header + single tappable i-pin + consolidated
  balloon -- the L-075 pattern applied to categorical/food data instead of the
  scalar heat field. The food generator deliberately still does NOT import the
  scalar heat engine; it shares only the engine-agnostic UI/KMZ helpers.
- **scenarios_food_insecurity.py.** New scenario registry (Sudan now; commented
  stubs for South Sudan / Chad / CAR / Ethiopia) -- the structure L-070 builds on.
- **Controller single-source (--preload).** earth_system_controller.py gained
  preload_layers(prefix) + a --preload <prefix> flag that globs
  data/<prefix>_*_blockbuster.kmz; the food GUI launcher delegates to it, so the
  food_insecurity_* family contract now lives in ONE place. (A symmetric --exclude
  complement was drafted but NOT committed -- left for a later pass if wanted.)
- **Verified.** py_compile; ASCII/LF; the heat balloon proven BYTE-IDENTICAL
  against the pristine create_info_placemark (793 chars, icon + balloonstyle
  match), so the working heat card cannot have drifted; food KMZ render-tested
  end-to-end (189 areas, single i-pin, full balloon). Landed 1b74bf1 -> be183c8
  -> c81bb3b; Mode-5 iOS-confirmed (L-001, IMG_1153/1154). Heat end-to-end render
  remains Tony's Mode-5 (not all heat scenario deps available in-container).
**Gap:** none -- move to section C. 
**Ref:** earth_system_common.py; earth_system_generator.py;
food_insecurity_generator.py; scenarios_food_insecurity.py;
earth_system_controller.py; cross-ref L-075 (heat 3+5 this generalizes), L-001
(food workstream), L-070 (multi-country it enables).

#### [L-072] Gallery Studio WYSIWYG preview -- render through the real index.html viewer
<!-- L:072 status:DONE upd:2026-06-26 section:C flag: rice:2/2/100/2 -->
- **Problem.** Studio Preview opened a bare Plotly figure via file://, so the
  viewer-only chrome (green Google Earth button from `_kmz_handoff`, link-icon
  dropdown from `_link_data`) never appeared -- not WYSIWYG with the live gallery,
  which adds that chrome at view time. The button is viewer chrome, not a figure
  annotation; the Studio preview never ran the viewer.
- **Fix (2 increments; gallery repo 3ee1734 -> pushed 495683e).** Inc 1: a dormant
  `?preview=<file>` branch in index.html `init()` that injects a synthetic lookup
  entry and reuses `loadVisualization` UNCHANGED (no render-path refactor; inert
  for real visitors). Inc 2: `gallery_studio.py` `_preview` rewrite --
  build_gallery_html -> the REAL `json_converter.extract_plotly_json_from_html`
  (same parse that yields the pushed JSON) -> throwaway
  `gallery/_studio_preview.json` -> ephemeral 127.0.0.1 daemon server rooted at the
  repo -> open the GENUINE index.html at `?preview=`. No vendored viewer, no second
  extractor -- WYSIWYG by construction. `.gitignore` covers the preview slot.
- **Verified.** Producer-chain smoke: `_kmz_handoff` + `_studio` survive
  build->extract into the previewed card; py_compile; ASCII/LF. Mode-5 (Tony): GE
  button renders, click-through resolves for PUSHED assets, no button when no KMZ,
  old file:// preview gone, `import json_converter` resolves via dashboard launch.
- **By design (not a gap).** GE button 404s when the KMZ is not yet pushed to
  `gallery/assets/` -- the preview honestly reports push status. Tony pushes the
  KMZ at generation time; only the exported HTML iterates between previews.
  Increment 3 (local-asset fallback) DECLINED for this reason.
**Linked:** sibling to L-058 (open Studio items); preview reuses json_converter as-is.
**Gap:** none -- move to section C.

#### [L-064] Provenance-scanner format sweep -- Earth System family
<!-- L:064 status:DONE upd:2026-06-30 section:C flag: rice:3/3/100/2 -->
- **CONFIRMED for food_insecurity_generator (the per-module question this item
  poses): the scanner does NOT traverse it.** Two compounding gaps, both proven
  empirically (uncited recognized-unit token in a fresh file -> zero findings):
  (1) ALLOW-LIST gap -- _extract_string_units only runs for a hardcoded
  narrative_files set (+ *_visualization_shells); a new module is excluded, so
  its display strings are never extracted/scored. (2) VOCABULARY gap --
  NUMERIC_CLAIM_RE recognizes only physical units (AU/km/deg/masses/K/kg...), no
  people|percent|%|million|thousand|billion, so humanitarian figures aren't seen
  as claims even inside an allow-listed file. The module's Tier-1=0 is a FALSE
  clean.
- **Verified two-part fix (on a SCRATCH copy; repo scanner untouched):** add
  'food_insecurity_generator' to narrative_files; append the humanitarian units
  to NUMERIC_CLAIM_RE. Under it, this module's sourced strings all read "Has
  source citation," Tier-3 -- the construction-site # Source: discipline holds.
- **Family ripple (decision driver):** the vocabulary extension newly surfaces a
  pre-existing REAL Tier-1 -- star_notes.py:1257, "No source citation (recalled)"
  -- invisible before only because of the vocabulary gap. Part (1) is local/safe;
  part (2) is family-wide CI with a ripple to triage.
- **Live-repo check (2026-06-30, @1f5901e): food's half is ALREADY LANDED, not
  just scratch-verified.** narrative_files now contains 'food_insecurity_generator'
  and NUMERIC_CLAIM_RE now carries people|persons?|percent|%. The "scratch copy"
  framing above is historical -- the food-specific fix is live. star_notes.py:1257
  triage status not re-confirmed this pass.
- **Scope expansion (2026-06-30, L-077 scaffold session) found this was bigger
  than one missing file, and that the manual-list mechanism itself was the
  problem, not just its current contents.** 6 of 7 Earth System files were
  missing from narrative_files; a second, separate vocabulary gap (no bare F/C
  degree-suffix pattern -- "117F" / "47.2C" don't match anything) sits underneath
  the humanitarian one; and a manual proxy check found likely real gaps beyond
  the Earth System family entirely (energy_imbalance.py, the paleoclimate_*_full
  family). Full findings preserved below for reference.
- [Full per-file risk breakdown and the manual-proxy methodology from the
  2026-06-30 session retained here verbatim -- see prior revision of this block
  for the complete scenarios_heatwaves.py / scenarios_western_heatwave_march_2026.py
  / scenarios_coral_bleaching.py risk split, all still valid as groundwork.]
**CLOSED BY DECISION (2026-06-30):** the food-insecurity half is genuinely done
and verified live -- that closes this item. The "sweep remaining Earth System
modules" half is NOT more of the same work -- it needs a different MECHANISM
(systematic, role-driven coverage off module_atlas.py, not hand-editing a list
file by file), so it is new tooling work, not a sweep remainder. Promoted to
L-078, the same shape as L-009 spinning off L-061 for new physics rather than
calling it a cone remainder. All empirical findings above (the F/C gap, the
energy_imbalance.py / paleoclimate candidates, the per-file risk split) carry
forward into L-078 as groundwork, not lost.
**Gap:** none -- move to section C.
**Ref:** provenance_scanner.py; PROVENANCE_AUDIT.md; module_atlas.py; originated
from L-001; confirmed via food_insecurity_generator build
(HANDOFF_food_insecurity_build_v2.md); superseded by L-078, 2026-06-30,
repo HEAD 1f5901e.

#### [L-097] skills_index.py -- Skill Manifest auto-generation (process/tooling)
<!-- L:097 status:DONE upd:2026-07-04 section:C flag: rice:2/2/80/1 -->
- **Devtool mirroring ledger_index.py:** walk skills/, read each SKILL.md
  frontmatter (name, description, fires_when) and body version line, regenerate
  the Skill Manifest table in the protocol file between SKILL-MANIFEST markers.
  Kills manifest-table drift the same way ledger_index.py killed hand-pasted
  summary rows. Also runs a consistency check: every skill directory has a
  manifest row and vice versa; folder name matches frontmatter name; version
  line exists.
- **Pattern:** ledger_index.py (402 lines, marker-based zone regeneration,
  --check mode for CI-style dry run). Read ledger_index.py as the recipe;
  mirror the architectural choices (parse -> validate -> regenerate -> report).
- **fires_when frontmatter field** added to all 8 SKILL.md files (editorial
  control of the manifest's "Fires when" column). Claude's skill loader reads
  name/description; this field is read only by skills_index.py. Fallback: first
  sentence of description, truncated, with a warning.
- **COMPLETED July 4, 2026.** Built by Claude Fable 5 via collegial relay
  (spec by Opus 4.6, documentation/FABLE_PROMPT_L097.md). Tony integrated.
  skills_index.py: 262 lines, repo root. Verified: py_compile clean; --check
  mode zero problems (8 skills parsed); manifest regenerated in
  project_instructions_v3_31.md, output matches v3.30 hand-written table.
  Tony ran locally on Windows (Python 3.13) -- clean, manifest regenerated.
- **Skill-layer verification (July 4, 2026, Opus 4.6 session @3429e568).**
  All 8 installed skills confirmed firing: orrery-coding-conventions loaded on
  hover-text trigger, ledger-and-session-records loaded on L-handle trigger.
  The two-layer system (resident protocol + on-demand skills) is operational.
  Protocol v3.31 installed with populated manifest; skills_index.py is the
  ongoing drift check.
**Gap:** none -- move to section C.
**Ref:** L-002 (parent), ledger_index.py (pattern), project_instructions_v3_31.md
Part 3 Skill Manifest, documentation/FABLE_PROMPT_L097.md.
---

## D. RECONCILED LEDGER -- OPEN

### D.Movement -- Movement-track open items

#### [L-008] v24 sec5 precision batch (low-risk)
<!-- L:008 status:OPEN upd:2026-06-21 section:D.Movement flag: rice:2/2/50/2 -->
- **v24 sec5 precision batch** (low-risk): three magnetosphere/bow-shock
  precision upgrades -- (1) a Jupiter toggle between its compressed (solar-max)
  and expanded (solar-min) magnetopause standoff; (2) upgrade Earth's
  magnetopause + bow-shock values to cited sources; (3) per-body bow-shock
  eccentricity (body-specific shock shape, not a shared approximation).
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
**Ref:** planet_visualization.py L558, L293, L306; neptune_visualization_shells.py. (umbrella: L-068)

#### [L-068] Static/animation pipeline consolidation -- remaining residuals (umbrella)
<!-- L:068 status:OPEN upd:2026-06-23 section:D.Structural flag: rice:2/2/75/2 -->
- **Umbrella thread for the remaining practical consolidation of the static
  (plot_objects) and animation (animate_objects) pipelines.** The big structural
  unification is DONE -- see section C ("shell-consolidation + animation refactor")
  and the Consolidation Log (F): scene-assembly unified, the three animation
  pipelines merged, explicit blocks deleted in both pipelines, one unified dispatch.
  What remains is distributed across three discrete residuals, tracked here as one
  thread:
    - L-066 -- behavioral parity gap: MAPS tail renders in the static path but not
      the animation path (one-line L2324 gate). The "make the two paths agree" task.
    - L-016 -- cleanup: grep-confirm zero callers across both pipelines, then delete
      the dead duplicate shell-function bodies the unification left behind.
    - L-014 -- the one render path still OUTSIDE the unified dispatch (the four
      asteroid belts via standalone create_main_asteroid_belt()); fold into
      CUSTOM_SHELLS or keep standalone (design call).
  This item is also the HOME for any NEW static/animation parity gap. The standing
  "fix both pipelines or neither" rule is a PRACTICE, not a backlog item, so new
  gaps surface only when caught by eye (the way MAPS/L-066 did) -- when one appears,
  log it here as a sibling of L-066.
**Gap:** none of its own -- this thread closes when L-066, L-016, and L-014 all
close AND no parity gap is outstanding. Tracking/umbrella item.
**Ref:** L-066, L-016, L-014; section C strategic-status block; Consolidation Log (F);
protocol Part 3 "Check All Parallel Pipelines".

#### [L-025 | #N7] Reduced to custom-geometry inline markers only
<!-- L:025 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:3/2/50/2 -->
The Phase 3 info-marker sweep (141 conversions, 18 files, May 2026) moved
sphere-shell markers to the create_info_marker() factory. Inline marker
dicts should now only remain in CUSTOM_SHELLS builders (rings,
magnetospheres, radiation belts, etc.) which need geometry-specific
positioning.
**Gap:** audit -- grep for inline marker dicts outside CUSTOM_SHELLS
builders. If none found, close. Zero code risk.
**Plain version:** a code-tidiness audit, NOT a render/Mode-5 issue. After the May
sweep, simple sphere-shell info-markers all go through one factory; custom-geometry
shells (rings, magnetospheres, belts) keep their markers inline because they need
special positioning. This item just greps the *_visualization_shells.py files for any
OLD inline-marker definitions left OUTSIDE a custom-geometry builder -- stragglers the
sweep missed. None found -> close. (Deferred until run.)

#### [L-026 | #9] palomas_orrery_helpers.py CRLF -> LF
<!-- L:026 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:3/2/75/2 -->
File confirmed CRLF (verified this session @7964193). Functional no-op
to convert, but the diff touches every line, so best as a standalone
commit with no other changes.
**Gap:** convert CRLF -> LF (binary-mode script or dos2unix). Do as
isolated commit. Low risk but noisy diff.
**Platform neutrality (the larger goal):** part of a general codebase LF-conversion sweep;
keeps the project platform-neutral across Windows / macOS / Linux. Pairs with L-027.

#### [L-027 | #61] Platform Neutrality (SystemButtonFace)
<!-- L:027 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:3/2/75/2 -->
26 occurrences of the Tk color name SystemButtonFace in palomas_orrery.py.
Resolves on Windows; fails on Linux/macOS. The xvfb pre-test sed swap is
a workaround, not a fix. Options: hex literal '#F0F0F0', platform
detection (sys.platform), or ttk styling.
**Gap:** choose replacement strategy, then sweep. Design decision before
build. Moderate scope (26 sites); low functional risk (cosmetic only).
**Platform neutrality:** same goal as L-026 (the LF sweep) -- pair them. This is the Tk
color-name half (SystemButtonFace -> hex literal / sys.platform detection / ttk).

#### [L-028] ASCII em-dash violation, comet_visualization_shells.py L257/505/519
<!-- L:028 status:OPEN upd:2026-06-11 section:D.Structural flag: rice:1/1/100/1 -->
Pre-existing; 3 em-dash lines in MAPS strings `[verified @0ce1e26]`.
**Gap:** fix on next touch (binary-mode).

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

#### [L-066] MAPS per-frame comet-tail animation wiring
<!-- L:066 status:OPEN upd:2026-06-23 section:D.Feature-A flag: rice:2/3/75/1 -->
- **Wire MAPS into the per-frame comet-tail animation.** In ANIMATION mode the MAPS
  tail does NOT render at all (it renders in STATIC mode only) -- Tony, Mode-5,
  2026-06-23. Extracted from L-056. The earlier "non-animation BY DESIGN" notes
  (L-004 / L-011, now in C) recorded the Phase-4 DEFERRAL (ADDENDUM_phase4 decision
  1), NOT a permanent exclusion -- the wiring is wanted and was always scoped as
  deferred, not done. THE FIX (handoff v29 scoping): remove the one-line gate at
  palomas_orrery.py L2324 (`if name == 'MAPS': continue`). build_comet_tail_traces
  is shared with all comets -- NO MAPS-specific code needed. Static path
  (plot_objects L6062) already handles MAPS.
**Gap:** PREREQUISITE -- review ADDENDUM_phase4 decision 1 (two-site exclusion
warning + partition design) before removing the L2324 gate. Risk: frame-1 tail
doubling (known pattern, known guard; Tony reports it currently GONE -- verify it
stays gone). Mode-5 gate: MAPS tail animates per-frame like the other comets
(updates each frame), no frame-1 doubling, exclusion warning still correct.
**Ref:** extracted from L-056 (2026-06-23); ADDENDUM_phase4 decision 1; handoff v29;
palomas_orrery.py L2324 (gate) + L6062 (static path); build_comet_tail_traces;
prereqs ADDENDUM_phase4_decisions.md + HANDOFF_animation_phase4_brief.md. (umbrella: L-068)

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
<!-- L:045 status:OPEN upd:2026-06-23 section:D.Feature-B flag: rice:1/1/90/1 -->
- **Add/verify a hover tooltip on Miranda noting its orbital inclination**
  (~4.3 deg, the highest among Uranus's major moons), so the visible tilt of its
  orbit in the render is explained. Single-info-marker pattern; km + AU where
  distances appear. `[per chain]`

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
convention. Low urgency; no bug, no user-visible gap. (umbrella: L-068)
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

### D.Parked (Tony's explicit call) `[per chain]`

#### [L-067] measure_animation_html.py file-browser dialog (B5)
<!-- L:067 status:OPEN upd:2026-06-23 section:D.Feature-C flag: rice:1/1/75/1 -->
- **Add a tkinter file-browser dialog to measure_animation_html.py (B5).** Spun out
  of L-048 on close (2026-06-23): the animation core track 21/51 is DONE (v4.1 gate,
  L-004), and B5 was the lone remaining rider -- a convenience dialog
  (filedialog.askopenfilename) to pick the HTML to measure instead of a hardcoded
  path. Small, isolated tooling.
**Gap:** add filedialog.askopenfilename to measure_animation_html.py.
**Ref:** spun out of L-048 (closed 2026-06-23).

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

#### [L-056] Phase 4 residuals: stale O2/O3 console wording; apsidal_markers em-dashes (MAPS per-frame wiring -> L-066)
<!-- L:056 status:OPEN upd:2026-06-23 section:G flag: rice:1/2/50/2 -->
- **Phase 4 residuals** (June 12): O2/O3 console notice wording is
  slightly stale when magnetosphere opt-in is ON (the blanket "not yet
  rendered" remains true for sphere shells; engine prints its own
  allocation lines) -- amend on next touch. apsidal_markers.py carries
  4 PRE-EXISTING em-dashes (platform-neutrality flag, not Phase 4's).
  MAPS per-frame wiring EXTRACTED to its own item L-066 (2026-06-23) -- it is real
  scoped work (a one-line gate removal), NOT "by design"; see L-066.
**Note (2026-06-17):** Mercury-centered auto-scale (O16) reads ~1 AU because
  get_animation_axis_range passes positions={} into calculate_axis_range_from_orbits;
  the non-Sun-center distance branch can't fire, so the Sun's heliocentric
  aphelion (~1.017 AU) is used as the fallback, giving a ~1.3 AU cube.
  Pre-existing; not introduced by the animation refactor. Workaround: use
  the orrery-side dtick/range field (item 19.3 Phase B) to override at
  generation time. Reopen as D.Priority only if the fallback causes
  confusion on other planet-centered animations (e.g. Jupiter-centered
  with Sun selected = ~5.5 AU, likely fine).
**Note (2026-06-23):** MAPS wiring split out to L-066. L-056 now holds only the two
non-visual residuals: O2/O3 console wording (one-line fix on next touch) and
apsidal_markers.py em-dashes (-> platform-neutrality, L-027). No Mode-5 needed here.

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
**Linked:** coupled to L-046 (encounter generator -> preset-authoring skill).

#### [L-073] Gallery export-emits-JSON -- fold the manual json_converter run into Export
<!-- L:073 status:OPEN upd:2026-06-26 section:H flag: rice:2/2/80/2 -->
- Export produces only HTML today; Tony runs json_converter by hand before push.
  Wire Export to also emit the JSON via the REAL converter (same transform the
  preview now uses, proven in L-072). One open decision: card-only, or also stamp
  the gallery_metadata.json entry (per-file converter does the latter via
  auto_metadata). Sequence AFTER L-072 so it inherits a proven transform. Curation
  gate stays downstream (which JSON gets posted) -- the converter does not edit.

#### [L-074] Cull unused raw *_teaser.json in the gallery dir
<!-- L:074 status:OPEN upd:2026-06-26 section:H flag: rice:1/1/90/1 -->
- 27 raw `*_teaser.json` are tracked but NOT in gallery_metadata.json (pre-Studio
  intermediates; manifest serves `_gallery`/`_desktop` exports). Candidate
  cull/archive. Confirm none are needed as converter inputs before removing.

---

## W. WEB PUBLICATION TRACK

Governing document: `documentation/MASTER_PLAN_WEB_PUBLICATION.md`.
Architecture, phasing, and rationale live there; this section tracks work items
and status. Cross-references: L-026 (CRLF, companion to L-087), L-046 (presets),
L-068 (pipeline residuals), L-071 (Earth storytelling), L-074 (gallery culling),
L-083 (Plotly 6 / Kaleido -- desktop only, not web).

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
**Ref:** Fable 5 survey (Front 2), master plan S6.

#### [L-086] Attribution / credits page
<!-- L:086 status:PROPOSED upd:2026-07-03 section:W.Prep flag: rice:2/2/70/1 -->
- **What.** One page (site + repo), one entry per data source, four fields each:
  what is used, where it appears in the project, the attribution string in the
  form the provider requires, and the license/redistribution terms with a link.
- **Source list (from repo evidence at HEAD):** JPL Horizons, JPL SBDB/CAD,
  Copernicus CDS / ERA5 / ERA5T, NOAA Coral Reef Watch, IPC and FEWS NET, HDX,
  OCHA FTS, SIMBAD (CDS), Gaia (ESA), Hipparcos, NSIDC, Mauna Loa CO2 (NOAA
  GML/Scripps), HOT program.
- **Provider-required citation strings** (especially Gaia/ESA, CDS/SIMBAD,
  Copernicus) must be fetched at build time, not recalled.
- **Two constraints on hosting/distribution:** Copernicus licence terms and IPC
  terms of use are the most likely to constrain a hosted path. Neither kills any
  option; both need verification before wide release.
**Gap:** fetch each provider's required citation format; draft page; verify
redistribution terms for Copernicus and IPC. Gates any wide release including
the Phase 0 pilot if publicly reachable.
**Ref:** Fable 5 survey (Front 2), master plan S6.

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
- **Natural companion to L-026** (CRLF to LF on the same file, already open).
  Do both in one pass.
**Gap:** decide split strategy (new module vs lazy-import), implement, verify
no callers break. Closes the second seam identified in master plan S2.
**Ref:** Fable 5 review of v2 (finding 3), master plan S2/S6.

### W.Active -- current phase

#### [L-079] Shared assembler architecture (keystone -- redefined)
<!-- L:079 status:OPEN upd:2026-07-03 section:W.Active flag: rice:3/3/50/3 -->
- **Redefined from:** "Headless scene core -- decouple scene construction from
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
  after it validates -- not a single late migration. Delta-log discipline: any
  desktop orchestration change during the build gets a ledger tag
  "assembler-must-inherit."
- **Key decisions (settled):** site never fetches Horizons; three-tier cache all
  offline; GUI declares the envelope; web GUI is a fork not a replacement; one
  assembler per domain; architecture is S3/M3; assemblers read cache through
  index abstraction from day one; Phase 2 gate is scene equivalence not identical
  output; animation presets as curated tier-2 exports.
- **Key decision (open):** server (Dash) vs serverless (Pyodide) -- Phase 0
  two-sided pilot resolves this.
**Gap:** the master plan IS the gap document. Current phase: prep (S6).
**Ref:** MASTER_PLAN_WEB_PUBLICATION.md; Fable 5 survey + L-079 deep dive;
Opus 4.8 convergence handoff + reviews; Opus 4.6 + Tony convergence (July 3).
RICE score 1.5 by arithmetic; strategically this is the keystone -- everything
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
**Ref:** Fable 5 survey (L-080 proposal); master plan S5/S6.

#### [L-088] Two-sided pilot (Phase 0)
<!-- L:088 status:PROPOSED upd:2026-07-03 section:W.Active flag: rice:2/2/50/1 -->
- **What.** Build the orbital parameter eccentricity visualization twice: Dash on
  HF Spaces, Pyodide on a static page. Same visualization, two delivery
  mechanisms. Tests hosting assumptions, cold-start vs first-load download, phone
  experience, ops feel.
- **Why two-sided.** The server-vs-serverless decision (S7 #1 in the master plan)
  is the largest remaining architectural choice. S1's "site never fetches" removed
  the CORS blocker on Pyodide. The orbital parameter viz is pure geometry -- no
  cache, no data files -- making it the cheapest possible test of both paths.
- **Downstream consequence.** If Pyodide wins, the web app is a static site --
  Fable's Option E (gallery viewer as unified front end) arrives nearly for free.
  If Dash wins, the gallery stays a sibling.
- **Attribution gate.** If either pilot is publicly reachable, keep unlisted until
  L-086 lands.
**Gap:** build both versions. Test on phone. Lessons-learned document +
server-vs-serverless decision before proceeding to Phase 1.
**Ref:** Fable 5 review of v4 (finding 10); master plan S5 Phase 0.

#### [L-089] Scene-spec shared skeleton + solar system vocabulary (Phase 1)
<!-- L:089 status:PROPOSED upd:2026-07-03 section:W.Active flag: rice:3/3/50/3 -->
- **What.** Design in conversation, not code.
  (a) The shared spec skeleton -- what every spec has across all domains: domain
  tag, content type, display options.
  (b) The solar system vocabulary: objects, center, dates, display options,
  content type (static/animation).
  (c) The coverage index interface for the solar system domain.
  (d) Scene equivalence criteria -- the concrete definition that shapes L-080's
  golden artifacts.
- **Other domain vocabularies are designed just-in-time** at the head of their
  own phases, informed by lessons learned here.
- **Decide:** is the spec serializable from day one? (Presets, shareable scenes,
  CI hang on this.)
- **Gate check:** confirm no shared-layer seams beyond the two named in S2.
**Gap:** design session(s). Gate: vocabulary document, index interface spec, and
equivalence criteria reviewed and stable before any assembler build.
**Ref:** Fable 5 L-079 deep dive (S2 vocabulary); master plan S5 Phase 1.

#### [L-090] Star cache inventory + wire format decision
<!-- L:090 status:PROPOSED upd:2026-07-03 section:W.Active flag: rice:1/1/50/1 -->
- **What.** The star cache (PKL files under `star_data/`) is gitignored, exceeds
  GitHub size limits, and is distributed via Releases for the desktop. It was
  built carefully from Gaia + Hipparcos with deduplication boundaries, within
  SIMBAD rate limits. Coverage: 101 light-years, apparent magnitude 9. Cannot be
  casually regenerated.
- **Inventory needed:** `du -sh star_data/` on Tony's machine -- total size and
  per-file sizes. This determines where the star cache fits in the headroom
  budget and whether it can ship via Pages.
- **Wire format decision:** pickle is Python-version-coupled (fine for a Dash
  server, brittle for Pyodide, opaque to non-Python consumers). Convert to
  Parquet or JSON at cache-build time is the standard escape. Tied to the
  server-vs-serverless decision (L-088).
**Gap:** Tony runs `du -sh star_data/` and shares the inventory. Wire format
decision follows L-088 (Phase 0).
**Ref:** Fable 5 review of v4 (finding 1); master plan S4b.

### W.Deferred -- captured, not yet actionable

#### [L-091] Option E: unified front end
<!-- L:091 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- The existing gallery viewer (3,345 lines of JS) becomes the single front end
  for all channels: static gallery, scheduled scenes, server-built and
  browser-built scenes. A and B become interchangeable back ends. Every dollar
  of work on the viewer pays into all channels. Arrives nearly for free if the
  serverless (Pyodide) path wins in L-088.
**Ref:** Fable 5 survey (Option E); master plan S8.

#### [L-092] Embeddable scenes for educators
<!-- L:092 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- An iframe embed snippet per scene, so educators can put a working orrery view,
  HR diagram, or orbital visualization in their own pages. Nearly free given the
  viewer; large reach-per-effort.
**Ref:** master plan S8.

#### [L-093] Educational guided explorations (specs as curriculum)
<!-- L:093 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- Scene specs as curriculum -- a notebook (JupyterLite or similar) that walks
  through "build a scene of the inner solar system, now change the center to
  Mars, now add Phobos" or "see how eccentricity transforms an orbit." The spec
  vocabulary becomes the teaching language. Cheap experiment once the assembler
  exists.
**Ref:** master plan S8.

#### [L-094] Community cache as commons
<!-- L:094 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- If tier-3 persistence is turned on, every fulfilled user request enriches the
  shared cache. Over time, the cache becomes a community-curated collection of
  interesting scenes -- driven by curiosity, not just Tony's curation. Tied to
  the tier-3 persistence dial (master plan S7 #5).
**Ref:** master plan S7/S5, S8.

#### [L-095] PWA / offline capability for classrooms
<!-- L:095 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- Progressive Web App wrapper -- installable and usable offline. Relevant for
  classrooms with unreliable connectivity. Modest effort if the architecture is
  static-first. Verify PWA constraints at build time.
**Ref:** master plan S8.

#### [L-096] Web orrery aesthetic / feel design conversation
<!-- L:096 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice: -->
- The desktop is a power tool with 60+ toggles. The web version could be that --
  or something different. A curated explorer. A storytelling medium. An invitation
  to wonder. The envelope-declaring GUI implies curation over completeness. The
  orbital parameter viz is inherently educational. The Earth system carries a duty
  of care. How do these different voices come together in one web experience?
  Design conversation before Phase 6 (web UI).
**Ref:** master plan S8 Q4; Fable 5 review of v4.

### W.Cross-references -- existing items that interact with the web track

- **L-026** -- CRLF to LF on `palomas_orrery_helpers.py`. Companion to L-087.
- **L-046** -- Preset authoring. A saved scene spec IS a preset. Falls out of
  the vocabulary design (L-089).
- **L-068** -- Static/animation pipeline residuals. Desktop cleanup, not web
  blockers, but worth closing.
- **L-071** -- Earth system dated-scenario storytelling. Natural web narrative.
- **L-074** -- Gallery culling. Headroom lever for Pages budget.
- **L-083** -- Plotly 6 / Kaleido migration. Desktop + Instagram concern only;
  Kaleido is not needed for web (Plotly.js renders interactively in browser).

---

## Appendix: Protocol Version History

The protocol's change log lives here as of v3.30; the protocol document
keeps only the most recent entries. Skill-layer changes are logged here
too (or as L-items when they warrant one): skill name, new version, and
the SHA it was cut from.

v1.0-v3.12 (Oct 2025 - Feb 2026): Foundation through Gallery Studio workflow redesign.
  Covers: modes, alignment, discovery pathway, Einstein proof, platform integration,
  Windows encoding, Horizons center patterns, agentic/targeted guidance, xvfb pre-test,
  bottom-up editing, Unicode-safe editing, Mode 7, LF line endings, JPL binary IDs,
  parallel pipeline lesson, iterative design planning, irreducibility argument,
  Gallery Studio session, _studio flag, pan arrows, Hassabis corroboration,
  featured trace labels, gallery badges, studio workflow redesign.

v3.13 (Mar 5, 2026): Studio source vs export distinction. 3D axis dtick+range convention. Hover text AU convention.

v3.14 (Mar 9, 2026): The Epistemic Dialogue. Polycrisis framework. Gemini elevated to dialogue partner.

v3.15 (Mar 14, 2026): Adaptive encounter resolution design. Two-length-scale insight. Double-Helix as safety mechanism.

v3.16 (Mar 25, 2026): Verify base against handoff before building on multi-session files.

v3.17 (Apr 3, 2026): Competitive Mode 7. Activation vs provision. Interpretation gap as signal. Fog of war is the experiment.

v3.18 (Apr 10, 2026): Single info marker pattern. Credit line convention. Ghost tail legendgroup. MAPS elegy.

v3.19 (Apr 13, 2026): Marker symbol convention. Two-tier label system. Renderer refactor. Celestial sphere complete.

v3.20 (Apr 14, 2026): Module Docstring Standard. Module Atlas tooling (99 modules, 785 functions, 86K lines).

v3.21 (May 4, 2026): Project file staleness rule formalized. Object Encyclopedia. Encounter Export design.

v3.22 (May 12, 2026): Collegial Mode 7 pattern. The Weasley Principle. Single info marker codebase-wide refactor: 141 conversions, 18 files, 3 Claude models, 9-13 MB savings per render.

v3.23 (May 16, 2026): Procedural criticality framework -- three-tier taxonomy (CRITICAL / QUALITY / PRACTICE), a Part-2 principle with markers across Part 3. Broad-first methodology validated; procedure-to-judgment ratio scales with experience and shared context. Grounded in Tony's ops-management experience (LOTO, normalization of deviance).

v3.24 (May 29, 2026): Verify Execution, Not Appearance [CRITICAL] -- map the dispatch before editing leaves; compile != used != edited; swallowed exceptions hide render bugs. Agentic Pre-Test refined: data-content sweeps need a runtime smoke against the LIVE dispatch. Platform Neutrality [QUALITY]. Plotly facts (Scatter3d ignores border width, 8-symbol palette); transactional binary-mode patching. From the shell-consolidation dispatch discovery -- an inline-marker sweep editing dead code, an osculating marker silently absent 11 weeks; Tony's eyes caught both.

v3.24 re-issue (May 29, 2026): Enumerate Uploads Before Claiming a Review [CRITICAL] -- ls the uploads dir, read the whole set; the in-context subset is invisible to Tony and not authoritative. Recovered lessons the first pass missed (itself built on 9 of 19 handoffs -- the exact failure it names): floating-items-capture, verify-propagation-with-grep, central-factory-migration-intent, testing-in-dependency-order, smoke-test-deferred-pipelines, handoff-numbering-rebase drift.

v3.25 (May 31, 2026): Provenance Audit named as a Part-3 skill (scanner, Tier-1=0 goal, lookback-window mechanics, exceptions-file over-report gotcha). Fetched-vs-Recalled extended: three outcomes (cite / remove-and-note-the-gap / never cite-to-clear); a citation is a provenance claim that must be TRUE [CRITICAL]. From provenance Phase 1, after nearly papering a # Source over recalled data.

v3.26 (June 2, 2026): Session-Start Repo Pull [CRITICAL] -- the GitHub repo at HEAD is ground truth; pull and SHA-pin, build on repo or fresh upload, /mnt/project + project knowledge demoted to orientation. From the stale-Earth thread: a duplicate upload shadowed the current file and a true ghost was served through a project-knowledge replacement; repo-pull validated byte-for-byte.

v3.27 (June 4, 2026): Project knowledge now auto-syncs from the repo (no manual add/delete), retiring v3.26's stale-snapshot + served-ghost class at source. Session-Start reframed around "The SHA is the round trip" -- a matching remote HEAD confirms commit + push + sync in one unforgeable check. Foundation gains "access is not understanding." Quotable: "Our work is not just right -- it's beautiful."

v3.28 (June 6, 2026): Two additions (Movement-2 dipole-cone session, handoff v27). (1) Live repo vs snapshots -- the repo is live-readable any time (re-pull after a push; reading HEAD is the round-trip check, run live: de12f56 -> c25bdd7); project knowledge does NOT re-sync mid-session; un-pushed edits live only in uploads, which stay tier 1. (2) Show the Envelope of the Unknowable -- companion to Fetched-vs-Recalled: where a value is genuinely unknowable (rotation phase / instantaneous azimuth), show the envelope, not a faked point, and say so in the hover where the shape is approximate; faking an unknowable value is the cite-over-recalled failure class [CRITICAL].

v3.29 (June 22, 2026): Three amendments from the animation-refactor sessions (L-003). (1) Agentic Pre-Test [CRITICAL] corrected -- the SystemButtonFace<->gray90 sed round trip is NOT idempotent (palomas_orrery.py has 26 native gray90 literals), so swap on a THROWAWAY copy and discard it; never restore-in-place on the deliverable. (2) Live-dispatch smoke test folded into the data-sweep gate -- exec the whole module under xvfb with the tk mainloop suppressed, to exercise the real path rather than a lookalike. (3) grep -c in && chains [QUALITY] -- grep -c exits non-zero on a zero count, silently breaking the chain; run verification greps standalone or join with ;. Cleanup: merged the duplicate data-sweep paragraphs, trimmed the redundant Uploads-Before-Project-Files block to a pointer, corrected the stale xvfb archive line, dropped the [NEW v3.23] tag.

v3.30 (July 1, 2026): The skills refactor (L-002). The protocol becomes the
constitution of a two-layer system: Part 3's task-triggered conventions and
procedures extracted into eight repo-authored skills (skills/<name>/SKILL.md,
each versioned and SHA-stamped; installed to the account as a deployment
step), with the resident document keeping the checkpoint CRITICAL gates, the
modes, the principles, the Foundation, and the quotables. Skill set at 1.0:
orrery-coding-conventions, safe-file-editing (portable), agentic-pre-test,
horizons-orbital-mechanics, provenance-discipline, earth-system-pipeline,
gallery-pipeline, ledger-and-session-records -- all cut from palomas_orrery
@ b29ad3f8 (gallery-pipeline also from tonyquintanilla.github.io @ 89c8bf30).
Part-3 technical lessons distributed into skills as field notes; the full
v3.29 Technical lessons list is preserved verbatim below for institutional
memory. Skill Manifest table added to Part 3 as the under-trigger backstop
and version drift check; a Triggers row added ("Relevant skill unfired ->
load it"). Skills 6-8 are first-time capture: Earth System pipeline +
human-cost restraint discipline, gallery pipeline + WYSIWYG authority,
ledger/handoff/manifest conventions -- knowledge that previously lived only
in handoffs and code. Version history moved here; the ledger is now the
change log for protocol and skills. Extraction audit trail:
documentation/MAPPING_TABLE_L002.md. Designed with Claude Opus 4.6; built
with Claude Fable 5 via collegial relay; Tony integrated.

v3.31 (July 4, 2026): Project-knowledge GitHub sync removed; Context Priority
simplified to 7 tiers (the repo, the protocol+skills, and uploads are the
three stores). skills_index.py devtool (L-097) auto-generates the Skill
Manifest table between markers, same pattern as ledger_index.py; fires_when
frontmatter field added to all 8 skills for editorial control of the manifest.
Protocol header still reads v3.30; filename bumped to v3_31. Reviewed and
built with Claude Opus 4.6.

### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)

- Cache: cache[name]['elements'] (nested dict)
- Reference frames can differ for same object; inclination reveals coordinate system
- Osculating elements must match viewing center (Charon@9)
- Horizons centers: Only numeric IDs work. helio_id vs center_id: opposite directions
- JPL binary IDs: 20XXXXXX (barycenter), 920XXXXXX (primary), 120XXXXXX (secondary). Derive primary from secondary via mass ratio
- Plotly camera: Axis ranges control zoom, not camera distance
- xvfb-run enables headless GUI testing; SystemButtonFace -> gray90 for Linux on a THROWAWAY copy -- the swap is NOT idempotent (26 native gray90 literals in palomas_orrery.py), so never restore-in-place on the deliverable
- Python binary mode (rb/wb) preserves line endings and Unicode; sed can corrupt multi-byte UTF-8
- Position data flows through 5 parallel pipelines in palomas_orrery.py -- ALL must be patched
- Plotly customdata survives JSON extraction; _studio flag survives -- downstream consumers can detect curated plots
- Plotly.js native touch works on mobile/tablet without custom code
- D-pad pan arrows: 2D uses Plotly.relayout on axis ranges, 3D uses camera eye/center shifting
- Stacked bugs: fixing one can reveal a second that was invisible before
- JS: JSON.stringify(undefined).substring() crashes; always guard with || ''
- position: fixed escapes CSS containment; position: absolute stays inside parent
- Plotly 3D annotations go on scene.annotations; 2D on layout.annotations
- Gallery Studio source vs export: source has figure-native values; export has _studio_config overlay
- Horizons step format: {number}{unit} (1m, 5m, 1h, 6h, 1d)
- Encounter resolution: cube scale (dist_km * 4) frames view; curvature scale drives fetch step
- Roche limit is not absolute: tensile strength allows survival inside it
- Celestial sphere in ecliptic frame: unit vectors rotated from equatorial via obliquity about X axis
- Sphere shells render via SHELL_CONFIGS -> build_sphere_shell -> create_info_marker (factory). Inline markers in *_visualization_shells.py are dead code for sphere shells; custom geometry (magnetospheres, rings, belts) routes via CUSTOM_SHELLS and uses the live inline path
- Plotly Scatter3d ignores marker border WIDTH (plotly.js #4118) -- the contrast lever is FILL color, not border. 3D symbol palette is only 8: circle, circle-open, cross, diamond, diamond-open, square, square-open, x
- A swallowed exception in try/except hides render bugs; an undefined variable can drop a marker silently for weeks. Check the console for the caught-error print
- grep -c exits non-zero on a zero count, silently breaking an && chain (the next command never runs while output looks complete) -- run verification greps standalone or join with ;
- GitHub is reachable in-environment: git ls-remote gives branch+HEAD SHA with no auth; raw.githubusercontent.com fetches files byte-exact. The HEAD SHA is the unforgeable current-state token AND the round-trip check -- a matching remote HEAD confirms commit + push + sync at once (project knowledge auto-syncs from the repo as of v3.27)
- The two surviving store failures are honest and visible -- no push, or no sync -- both show as a HEAD mismatch. (v3.26's stale-snapshot + served-ghost failures came from the manual step, retired in v3.27)


