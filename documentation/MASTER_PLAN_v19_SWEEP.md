# Master plan v19 -- full-document sweep

**Built on `38923c1cc64d492006135ec77779e1fb592582d5` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at `493a0bd7fcba4067c56db318357889e965fba514`. Both confirmed
by live `git ls-remote`. Prepared August 22, 2026 with Anthropic's
Claude Opus 5.**

Scope: every checkable claim in `MASTER_PLAN_INTERACTIVE_GALLERY.md`
(2,010 lines, 118 KB), measured rather than read forward. Sixty-three
file references resolved against both repos; every L-handle the plan
names checked against `LEDGER_CONSOLIDATED.md`; every count and SHA
re-measured.

Twenty-nine items moved. Grouped by what kind of thing they are, not
by section, because the kind determines whether they need a ruling.

---

## A. Mechanical corrections -- measured fact disagrees with stated fact

No judgment involved. Each is a number or a status the document states
and the repo contradicts.

| # | Where | Plan says | Measured at HEAD |
|---|---|---|---|
| A1 | Header | `Status: v18` | -> v19 |
| A2 | Header | `Last updated: August 7, 2026` | -> August 22, 2026 |
| A3 | Header base | orrery `ee0da47c` / gallery `61a78c00` | orrery `38923c1` / gallery `493a0bd` |
| A4 | Header | "L-119/L-120/L-121/L-122 still OPEN, none built yet" | **L-120 DONE 2026-07-27**; L-119, L-121, L-122 still OPEN |
| A5 | Header | "L-150 and L-151 still decided, not yet built" | **L-151 DONE 2026-07-27** (skill exists, v1.1); L-150 still OPEN |
| A6 | S3a | gallery "474 MB with 526 MB headroom" | **439 MB** working tree (S1's 436/588 pair is within a few MB and is the one to keep) |
| A7 | S3a | "Full section-3a rewrite tracked as L-108" | **L-108 DONE 2026-07-12**; the pointer describes an open item that closed |
| A8 | S4a | `palomas_orrery.py` "11,110 lines at HEAD" | **11,092** |
| A9 | S6 | "L-162 ... [ ] Not started, scoped" | **L-162 DONE 2026-07-29** |
| A10 | S11 | "`gallery-pipeline` v1.1" needed | landed; skill is at **1.2** |
| A11 | Closing | Base SHAs | stale, same as A3 |
| A12 | Closing | protocol `v3.37` | **v3.41** |

## B. Structural defects

| # | Where | What |
|---|---|---|
| B1 | line 2010 | **Unmatched code fence.** Five ` ``` ` markers in the file, an odd count. Lines 205/208 pair, 825/840 pair, and 2010 is orphaned -- it opens a block that never closes. |
| B2 | Closing, lines 1991-2001 | **Ten skill versions restated by hand.** Five of ten have drifted: orrery-coding-conventions 1.3 (now 1.4), provenance-discipline 1.8 (now **2.6**), ledger-and-session-records 1.5 (now 1.8), safe-file-editing 1.3 (now 1.7), gallery-cache-builder 1.3 (now 1.4). This is a second store for a value the protocol's generated Skill Manifest already owns, and Stale Skill = Stop compares against that manifest, not this list. See the one open question below. |
| B3 | S10 lineage | `AB_FORK_ANALYSIS.md` is cited with a SHA anchor and **is in neither repo**. No near-match filename exists. It is the only genuine dangling reference of the 63 checked. (`gallery.html` is hypothetical in its sentence; `orbit_paths.json` is documented as gitignored.) |

## C. A stated reason that is false while its conclusion holds

| # | Where | What |
|---|---|---|
| C1 | S2 seam 2, S6, Phase 2 "Requires" | The plan says `palomas_orrery_helpers.py` "imports tkinter directly," calls the split **not started**, and makes it a Phase 2 requirement. At HEAD the file has **zero tkinter references** and **L-087 is DONE (2026-07-15)**. All three functions the assembler needs are present. **But the seam survives in a different shape:** three modules in its transitive import closure still import tkinter -- `osculating_cache_manager`, `save_utils`, `shutdown_handler`. So the requirement is real and the reason given for it is not. Correct the reason; do not re-open the item. |

## D. Open questions the plan asked, now answerable by measurement

The plan tells a future session to resolve these by looking. I looked.

| # | Where | Question | Answer at HEAD |
|---|---|---|---|
| D1 | S7 decision 12 | "the plan says two [constructor calls], measurement finds one ... Resolve by looking, not by patching" | **Two is right.** `constants_new.py` has 48 top-level assignments; 6 arithmetic derivations (unchanged); **two** assignments contain constructor calls -- `HORIZONS_MAX_DATE = datetime(...)` at line 141, and `stellar_class_labels` at line 902, which holds twelve `dict()` calls. The August 11 count missed the second. The argument against `ast` is unaffected, as the plan already noted. |
| D2 | S7 decision 16 | "it says Jupiter has 5 entries, and the August 10 session counted 4. Confirm before the pilot starts" | **Four.** `main_ring`, `halo_ring`, `amalthea_gossamer`, `thebe_gossamer` -- identical in `objects_config.json` and in the served `feature_configs.json`. |

## E. Claims that hold -- verified, not assumed, no edit

Recorded so the next sweep does not re-check them blind.

- S2: the six shared modules are import-clean. `planet_visualization.py`'s two `tk.` mentions are docstring text describing an `IntVar` parameter, not imports.
- S2a: 148 curated cards, exactly as stated. Pyodide **v314.0.2** live in `interactive.html`.
- S3: Encke is still **absent** from `celestial_objects.py`. The deliberate exception stands.
- S5a segment 3: `resolver.py:133` is still `features = tuple(rec.get("features") or ())`; `models.py:91` still types it `Tuple[str, ...]`; **nothing in the gallery repo reads `feature_configs.json`** -- only the builder writes it.
- Header: Artifact 1's golden artifact exists at `gallery/assembler/harness/golden/artifact_1_earth_alone.json`; fingerprint `abbd01094852b57f` corroborated in the ledger and in the gallery-assembler skill.
- S1b row: Saturn 7 rings, Jupiter 4 rings + 4 belt fields, Earth atmosphere + Van Allen -- all served.

## F. The braid -- Section 5a and its consequences

Per the design note Section 1 and Tony's ruling of 2026-08-22.

| # | Where | What changes |
|---|---|---|
| F1 | S5a header | Add an "Amended 2026-08-22" paragraph, matching the existing "Rewritten 2026-08-16" convention. |
| F2 | S5a "One pipeline" | The closing sentence -- "why the provenance refactor precedes the assembler work rather than running beside it" -- is the exact claim the braid overturns. It becomes: the asymmetry governs what an artifact may LOCK, not what may be BUILT. Plus the render-as-check argument: once the assembler draws, a wrong ring radius is something Tony's eyes can catch. |
| F3 | S5a segments | The five segments **do not move**. A new subsection states the execution order: segment 3, then segment 1 sliced to Artifact 2, then 4, then 5. |
| F4 | S5a segment 1 | Its scope for Artifact 2 narrows to the rendered slice. The general audit continues and stops being a gate. |
| F5 | S5a "You are here" | Restamp to 2026-08-22 / `38923c1` / `493a0bd`. Reconciliation figures **110/8/48/20/34/24 -> 105/8/47/19/31/22** (`WORKSHEET_CHECK.md` at HEAD). Tier-1 holds at **292**. |
| F6 | S5 Phase 2 track table | Two-line superseded-by pointer. Track 1's exit condition still reads "Batch 2 gas giants verified," which the braid narrows. The August ruling stays as history. |
| F7 | S10 | A *New in v19* lineage entry. |

**The slice is countable, and this is the number the braid turns on.**
Saturn's 7 rings carry `inner_radius_km` and `outer_radius_km`.
Jupiter's 4 rings add `thickness_km`. The belts carry `belt_distances`
(three values) and `belt_thickness`. **Thirty measured numbers.**
`n_rings` and `n_points` are drawing parameters -- DECLARED under
Section 7 decision 18, and not findings.

Saturn has **no** radiation belts, in the served cache or in
`objects_config.json`. Only Jupiter's. Segment 4's phrase "Jupiter and
Saturn with rings and radiation belts" reads as though both have them.

## G. Surfaced by the sweep, outside this file

Reported, not fixed here.

- **G1. L-225 has no ledger entry.** The highest handle in
  `LEDGER_CONSOLIDATED.md` is L-224. The design note cites L-225 four
  times and the session queue cites it as deferred-with-shape-settled.
  It is a floating item, and the ledger's own lesson is that floating
  items get lost.
- **G2. L-154 is ledger-BLOCKED, and the braid unblocks it.** The
  braid makes the feature-rendering layer the first work. The plan is
  the sequencing authority and the ledger is the status authority, so
  the sequencing change implies a ledger status edit. The plan should
  not silently contradict the ledger.
- **G3.** `MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` line 20 still
  points at the bare `CRITICAL_PATH_SUMMARY.md`. The file is
  `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`. Carried from the prior
  session; belongs with the summary revision that follows 5a.

---

## The one open question

**B2 -- the skill-version list.** Everything else above is either a
mechanical correction or already ruled. This one changes what the
document carries rather than what it says.

The recommendation is to delete the ten hand-written versions and the
protocol version, and point at the protocol's generated Skill Manifest
instead. The reason is the project's own: a hand-maintained second copy
of a value that has a generator is a shadow store, it has drifted five
of ten, and nothing watches it. Fix the producer, not N consumers.

The argument against is that the closing block is a snapshot -- a
record of what the versions were at v18 -- and snapshots are allowed to
be historical. That reading is weaker here, because the block is
written in the present tense as current state, not dated as history.
