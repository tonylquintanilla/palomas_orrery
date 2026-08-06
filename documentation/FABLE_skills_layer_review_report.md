# Fable Skills Layer Review — Full Report

**Built on `339897000b63fa768ccb9b556dd432bac4f9d4eb`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Gallery repo verified at `f83a3abc72c5516e6dc2ad264be53ce95b68cf38`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.

**Prepared:** August 5, 2026 by Claude Fable 5 (comprehensive audit leg) · Tony Quintanilla, integrator
**Responds to:** PROMPT_fable_skills_layer_review.md. HEAD matched the prompt's anchor
exactly at session start (`git ls-remote` round trip), so the prompt's line numbers were
trusted as given.

**Method.** All ten skills were read from `skills/<name>/SKILL.md` at HEAD (not from the
installed account copies, which in this session's mount predate the v1.2/v1.6 installs —
see Honest Gaps). Every concrete claim a skill makes about a file, line, function, count,
or ID was checked against live code in whichever repo owns it; both repos were cloned at
their current HEADs. Where a claim could not be checked from this container, it is marked
UNVERIFIED rather than assumed.

---

## Job 1 — Coverage gaps

The module census at HEAD is **117 root `.py` files**. The project's own taxonomy
(`MODULE_DOMAIN_MAP` in provenance_scanner.py) classifies 98 of them; 19 are unmapped and
default to `orrery`, and 2 map entries point at files no longer in the root
(`smoke_dipole_cone`, `smoke_rotation_axis`). That unmapped set is itself evidence for the
gaps below and a small cleanup item for the scanner's own coverage-gap note.

| # | Gap | Modules affected | What a session must currently reconstruct | Recommendation | Severity |
|---|-----|------------------|-------------------------------------------|----------------|----------|
| 1 | **Stars / stellar neighbourhood** (seeded; assessed and enlarged) | The scanner's `stars` domain maps 20 modules (the seeded 18 minus sgr_a/catalog/GUI, plus `simbad_manager`, `vot_cache_manager`-adjacent `visualization_2d/3d/core/utils`); the unmapped set adds `star_visualization_gui`, `catalog_selection`, `vot_cache_manager`, `data_processing`. Realistic scope: **~22–24 modules**, the largest uncovered domain in the project. | The entire acquisition→processing→visualization chain: Gaia/Hipparcos catalog fetch and VOTable caching (`data_acquisition*`, `data_processing`, `vot_cache_manager`), SIMBAD query discipline (`simbad_manager`), the paired dual-mode pattern (`hr_diagram_apparent_magnitude`/`_distance`, `planetarium_*` — one physics, two selection modes), stellar parameter estimation and the patch layer (`stellar_parameters`, `stellar_data_patches` — the existence of a hand-patch module is itself an earned lesson with no written home), Messier handling, the star GUI's cache-vs-fetch flow. The project already recognises the domain twice: provenance-discipline defines a `stars` report domain, and a scanner-hardening episode exposed a Tier-1 in `star_notes.py`. | **NEW SKILL.** The seeded question is answered yes. Two scope decisions ride with it: where `sgr_a_*` (6 modules, currently `orrery`) and the shared `visualization_2d/3d/core/utils` belong — the prompt's seed list and the scanner's map disagree on the edges, and the new skill's frontmatter is where that boundary gets settled. | HIGH |
| 2 | **Paleoclimate / climate-record visualization** | ~9 of the `earth_science` domain's 15: `paleoclimate_*` (5), `fetch_climate_data`, `fetch_paleoclimate_data`, `climate_cache_manager`, `energy_imbalance`. earth-system-pipeline explicitly scopes to the KMZ/scenario/teaser pipeline and does not mention any of these. | Data-source specifics (paleoclimate archives), the dual-scale/wet-bulb visualization patterns, climate cache invalidation semantics. | **SECTION IN earth-system-pipeline** — but cut it *on next touch*, not now. The area shows no active ledger work; writing conventions for a dormant subsystem from cold reads would violate the "record what the project learned" rule. Recommendation is NO ACTION today with a named landing place. | MEDIUM |
| 3 | **Orbit-cache lifecycle tooling** | `export_orbit_cache`, `test_orbit_cache`, `verify_orbit_cache`, `create_ephemeris_database`, `create_cache_backups`, `incremental_cache_manager` (~6). horizons-orbital-mechanics covers *using* the caches (`orbit_data_manager`, `osculating_cache_manager`, the `cache[name]['elements']` nesting) but not the export/verify/backup lifecycle around them. | Which tool is safe to run when, what a verify failure means, backup semantics. | **SECTION IN horizons-orbital-mechanics** (a short "cache lifecycle" block naming the six tools and their one-line jobs). The skill is the layer's shortest at 89 lines and can absorb it without balance damage. | MEDIUM |
| 4 | **Tk GUI wiring contracts** | The GUI half of `palomas_orrery.py`, `star_visualization_gui`, `earth_system_visualization_gui`, `shutdown_handler`, `palomas_orrery_dashboard`. | The load-bearing naming contract `f"{body_prefix}_{suffix}_var"` / `..._info` that `build_shell_checkboxes()` resolves via `globals()` — a mismatch fails **silently** ("No information available"), which is the classic invisible-failure shape this project writes conventions for. Also `CreateToolTip` renders text literally (the `<br>` finding), and the SystemButtonFace platform fact (currently housed in agentic-pre-test as a *test* concern, with no home as a *GUI* concern). | **SECTION IN orrery-coding-conventions** ("GUI wiring contracts": the naming contract, the literal-text tooltip fact, a pointer to agentic-pre-test for the color-name test workaround). Tension acknowledged: that skill is already the second-longest at 343 lines — see Job 2 balance note. A separate skill is not warranted; the material is ~25 lines. | MEDIUM |
| 5 | **Dev tools / diagnostics** | The `dev_tools` domain's 20 modules (`test_*`, `measure_*`, `data_inventory`, `diagnose_*`, one-shot converters). | Little — these are self-describing single-purpose tools with docstrings, indexed by MODULE_ATLAS.md. | **NO ACTION.** A skill here would mirror the atlas, which is already the designed reference for exactly this. The provenance test suite is already named where it matters (provenance-discipline). | LOW |
| 6 | **Shared utilities and report/save widgets** | `utilities` domain (6): `formatting_utils`, `shared_utilities`, `save_utils`, `plot_data_exchange`, `plot_data_report_widget`, `report_manager`. | Little; consumed through call sites with docstrings. | **NO ACTION** standalone. If the Gap-4 GUI section is cut, `report_manager`/`plot_data_report_widget`/`save_utils` get one naming line there. | LOW |
| 7 | **`skills_index.py` has no owning skill** | One module — but it is the tool the whole layer's manifest integrity depends on. ledger-and-session-records' Codebase Tooling section names its four siblings (`module_atlas`, `add_docstrings`, `dep_trace`, `ledger_index`) and omits this one; only the resident protocol names it. | When and how to regenerate the manifest (the exact mechanic behind the three-week drift in Version State (a)). | **SECTION IN ledger-and-session-records** — one bullet in Codebase Tooling plus the binding recommended in Job 3 #8. | LOW (but couples to a MEDIUM mechanics finding) |

---

## Job 2 — Per-skill findings

### orrery-coding-conventions v1.2

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|
| 1 | Hill Sphere Documentation Standard | **GOOD** | The intent-plus-measured-state rewrite is the right pattern, and the prompt's direct question gets a direct answer: **yes, keep it.** It states the intent (perihelion), the measured split at a named SHA, and an explicit "do not correct a body on the strength of this section alone." This is the house pattern any not-yet-uniform convention should use. Preserve under edit pressure. | — | Adopt as the template for partial conventions layer-wide. |
| 2 | Hill table premise | verified | The per-body `radius_fraction` values underlying the measured table are unchanged between the skill's cut SHA and HEAD (no code commits in that window) — the table's premise holds at HEAD. The astronomical classification itself (which distance each rf matches) was not independently recomputed; see Honest Gaps. | — | — |
| 3 | Canonical `\n` / migration status | **GOOD** | Verified against runtime behaviour established in the shell audit: migration split accurate, the `.replace` no-op trap is real and correctly described. The section states measured state with a SHA — same right pattern as #1. | — | Preserve. |
| 4 | Module Docstring Standard | **GOOD** (verified descriptive) | "Every .py module gets a docstring" was checked, not assumed: **117 of 117** root modules carry a leading docstring. This convention is descriptive, not aspirational. Stated so the next review does not re-litigate. | — | — |
| 5 | Hover Text AU Convention | no finding | Phrased as "apply to ALL **new** hover text" — forward-looking, so not an unmarked-aspirational case. One known non-compliant legacy instance (GEO hover, from the shell audit) already tracked; no wording change needed. | — | — |
| 6 | Barycenter Rule | TIER | The only section with no tier tag at all. | LOW | Tag it (reads as [QUALITY]); or state why untagged. |
| 7 | whole skill | BALANCE | 343 lines after 93% growth. The growth is earned (every new section carries its observation), but the skill now spans two audiences: stable visual conventions vs. hot L-156/L-181 migration state. The migration-status content (dead tooltip counts, per-body split) will churn with every batch and force version bumps of an otherwise stable skill. | MEDIUM | No cut now. When L-181 lands, the migration-state passages should collapse to one line + ledger pointer rather than accreting a history. Flag for that future edit, not this one. |

### provenance-discipline v1.6

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|
| 8 | Worksheet Types — "Hill sphere 324.5 should have been 320" | **CONTRADICTION** (cross-skill; also listed Job 3 #1) | Stated as a settled error example. At HEAD, **every** live and dead copy of Mars's Hill sphere reads 324.5 (the consistency patch harmonized the formerly-drifted dead copies *up* to 324.5), and orrery-coding-conventions classifies Mars's 324.5 as the semi-major-axis value with an explicit do-not-correct guard pending the Batch 2 convention decision. A session loading only this skill reads 324.5-at-HEAD as a known-wrong value and "fixes" it to 320 — the exact wrong-action failure Job 2 item 2 warns about, against the other skill's explicit guard. The two 320/324.5 numbers are almost certainly the perihelion-vs-semi-major convention pair, i.e. a *decision pending*, not an error found. | **HIGH** | Reword the example to name the convention question and point at the orrery-coding-conventions Hill section as governing; or swap in an example that is settled (Mars bow shock 1.5→1.64 is right there and is settled). |
| 9 | No Shadow Constants — "Known precedent: comet lines 492-493 ... hardcoded" | STALE | Present-tense description of a fixed state. At HEAD those lines carry the *fix* comment ("Local copies lived here until L-156 1f"); the shadow constants are gone. A reader sent to look for them finds a comment saying they were removed and wonders which document is wrong. | MEDIUM | One-word class of fix: "(fixed in L-156 1f; the in-code comment records it)" — keep the precedent as history, stop describing it as current. |
| 10 | Retired stamp census | verified | "42 remaining — shell_configs 14, earth 13, jupiter 9, comet 6" re-counted at HEAD: exact match, including the from-16-to-14 note. | — | — |
| 11 | Scanner mechanics | verified | `NUMERIC_CLAIM_RE`, `NARRATIVE_ROLES` (exact set), `build_pinned_values`, V2 scoring, exceptions-file behaviour — all present in provenance_scanner.py as described. | — | — |
| 12 | Version-history preamble | BALANCE / REGISTER | The v1.1→v1.6 narrative now runs ~30 lines before the first governing sentence. The ledger is the *declared* change log for skills (per ledger-and-session-records); the in-skill narrative duplicates that job and pushes the two-move rule below the fold. | MEDIUM | Direction only (per ground rules): current-version line stays; history migrates to the ledger appendix it already belongs to. Applies to all skills; this one is the worst case. |
| 13 | Field note — three wrong-paper citations | **GOOD** | Model field note: three distinct failure shapes, each with the concrete observation that earned it. Preserve verbatim under any future trim. | — | — |

### agentic-pre-test v1.1

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|
| 14 | Throwaway-copy rule — "26 SystemButtonFace literals" | STALE | HEAD has **23**. The load-bearing facts survive (0 native gray90 in palomas_orrery.py; 5 and 3 in the named siblings — both re-verified exact), so the rule stands; only the count drifted, and the hedge "at the time of writing" covers the siblings but not the 26. | LOW | Either hedge the count too or drop it; the argument needs "zero native gray90," not the 26. |
| 15 | Layered-gate handoff to gallery-cache-builder | verified GOOD | `documentation/TESTING_PROTOCOL.md` exists; the scope carve-out is accurate and correctly keeps this skill from over-firing on gallery builder work. | — | — |

### safe-file-editing v1.1

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|
| 16 | Delivery Format B — `git apply` from a terminal | CONTRADICTION (vs protocol) | The resident protocol's WHO TONY IS states git is GitHub Desktop-only, "never the git command line," and that operations outside the known working set need plain explanation first. Format B instructs CLI `git apply` and asserts "Tony already has terminal access for this." The skill does state the exact command and both success/failure signals (good), but the working-set assertion contradicts the constitution's account of Tony. Likely a deliberate v1.1 extension the protocol never ratified — but the protocol wins until it does. | MEDIUM | Tony decides which document is right: either the protocol's WHO TONY IS gains a sentence (terminal okay for `git apply` with stated command), or Format B is demoted to "only at Tony's explicit request." Flagged, not resolved, per the skill-vs-protocol rule. |
| 17 | Encoding gate paragraph ("LF line endings. ASCII only...") | REGISTER | The paragraph sits headerless after the Delivery Format section — it reads as a tail of Format B rather than the standalone encoding gate it is (agentic-pre-test points to "the encoding greps from the safe-file-editing skill," which now have no heading to find them under). | LOW | Restore a `## Encoding Gate [QUALITY]` heading. |
| 18 | Field notes | **GOOD** | Both 2026-07-29 notes carry their earned observations (the never-run patch; the combined-grep false confirmation) and neither duplicates another skill. | — | — |

### horizons-orbital-mechanics v1.1

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|
| 19 | Record pinning — Halley `90000030`, Encke `90000091` | verified | Halley confirmed at celestial_objects.py:535; Encke confirmed at the **gallery** repo's data/objects_config.json:126, exactly as the skill locates them. | — | — |
| 20 | Encounter workflow disclaimer (L-046) | **GOOD** | L-046 confirmed OPEN in the ledger. The skill's honest "this is not the encounter build recipe; read code and ledger at HEAD" is the correct way to handle an evolving area — it is why this 89-line skill is *appropriately* short, not under-built. Preserve the pattern. | — | — |
| 21 | whole skill | BALANCE | Shortest skill; absorbs Gap 3 (cache lifecycle) without strain. | LOW | Landing place for Job 1 #3. |

### ledger-and-session-records v1.4

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|
| 22 | Codebase Tooling | omission | Names module_atlas, add_docstrings, dep_trace, ledger_index — omits `skills_index.py`, the fifth member of the same regenerate-a-marker-zone family and the tool this skill's own Protocol-and-Skills-Change-Log section implicitly depends on. | LOW | One bullet; couples to Job 3 #8. |
| 23 | Ledger mechanics claims | verified | INDEX:START/END markers (ledger_index.py:147), `regenerate_role_map()` (module_atlas.py:668), header/metadata format — all match code. | — | — |
| 24 | **Tony:** reservation; L-handle never-renumber | **GOOD** | Both rules carry their earned observations (L-126/L-127 mislabel caught pre-paste; the v23–v27 rebase leak). Model entries. | — | — |

### earth-system-pipeline v1.1

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|
| 25 | Engine/scenario contract | verified | `run_scenario` (line 71), `_heat_scenarios()` (line 798), `MissionControlApp` (controller line 25) all as described; food-insecurity separation accurate. | — | — |
| 26 | Human-Cost Restraint section | **GOOD** | The worked IPC Sudan near-miss (185k/28M/51.7M vs published 135k/19.5M/47.5M) is the strongest observation-earned convention in the layer. Explicitly preserve. | — | — |

### gallery-pipeline v1.1

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|
| 27 | Two-repo layout, tools inventory, index.html-as-viewer | verified | All checked against gallery HEAD; accurate. | — | — |
| 28 | "SHA-pin each repo separately in handoffs" | DUPLICATION | Restates ledger-and-session-records' multi-repo anchor rule without naming the master, unlike this skill's own Shared Conventions section which does the master-pointer pattern correctly three times. | LOW | Add "(master: ledger-and-session-records, Anchor Requirement)". |

### gallery-cache-builder v1.1

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|
| 29 | Field note — mislabeled comment "near line 755" | STALE (line ref only) | The mislabeled "guard/B3 WARN" comment persists but now sits at line **1099**; the substance of the note (B3 aborts; the comment lies; docstring is right) remains correct and the note already tracks cleanup separately. | LOW | Update the line ref, or drop it ("search for the string") since the code beneath it moves. |
| 30 | interactive.html zero-references claim | verified | Re-checked at gallery HEAD: still zero references to data/solar-system/. The "at the time of writing" hedge plus "describe as future work" framing is exactly right for a fact that will one day flip. | — | — |
| 31 | Trust divisors, TRUST_WINDOW_PARTICIPANT_FRAME, onboarding traps | verified GOOD | `_TRUST_CAP_DIVISOR` dict matches to the digit; participant frame = 'heliocentric'; the --first-build-not---nightly trap and the count-assertion trap (Halley 11→12) both carry their observations. | — | — |

### gallery-assembler v1.0

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|
| 32 | Known-stale-doc flag (cache_reader docstring) | verified, extend | The flagged stale docstring ("served_window currently null... F1") is still present at gallery/assembler/cache_reader.py:13-14 while the served cache now carries a real `served_window` (verified in coverage_index.json) — the skill's flag is accurate. **Extension:** resolver.py's docstring (lines 14-16) carries the same stale null/F1 text, which the skill does not mention. | LOW | Add resolver.py to the fix-next-time note. |
| 33 | Encke "confirmed absent from celestial_objects.py" | verified | Still absent at orrery HEAD — the porting-gap-as-live-test framing remains current. | — | — |
| 34 | "as of tonight" (Pluto/Charon, Moon/Io/Titan status) | REGISTER | Time-deictic phrasing in a document read months later; the header date saves it, but barely. | LOW | Replace with the date. |

**Clean list (no findings beyond GOOD/verified):** earth-system-pipeline, gallery-pipeline (one LOW), horizons-orbital-mechanics (one LOW landing note). No skill failed frontmatter, tier definitions, or the protocol-wins rule outright; the one protocol conflict (#16) is flagged for Tony's ratification either way.

**On the prompt's direct question (Job 2 item 2):** the intent-plus-measured-state pattern is right, and after checking the other candidates — module docstrings (verified 117/117 descriptive), AU hover (scoped to "new"), single info marker (compliance history recorded), canonical `\n` (measured split stated) — **no other unmarked aspirational convention was found.** The Mars example (#8) is the inverse problem: a *pending decision* written as a settled error.

---

## Job 3 — Cross-skill coherence and the two-layer boundary

| # | Finding | Skills involved | Type | Severity | Suggested direction |
|---|---------|-----------------|------|----------|--------------------|
| 1 | Mars Hill 320-vs-324.5: provenance-discipline presents a settled correction; orrery-coding-conventions presents a pending convention decision with a do-not-correct guard; the code at HEAD is uniformly 324.5. No statement of which skill governs. | provenance-discipline, orrery-coding-conventions | CONTRADICTION | **HIGH** | Per Job 2 #8. One sentence in each pointing at the other's Hill section as the governing treatment closes it. |
| 2 | Cross-reference graph: **every seeded pointer verified accurate** — each target exists and says what the pointer claims (all nine rows checked, both repos). One delta: the seeded graph predates v1.2's new edge orrery-coding-conventions → provenance-discipline (Geometry Constants), which also verifies. | all | — (GOOD) | — | Add the new edge when the graph is next regenerated. |
| 3 | Nothing points to ledger-and-session-records (seeded asymmetry): **assessed correct, not a gap.** The things other skills need from it session-wide — read the ledger at start, anchor every outbound document — are resident Part-1/Part-3 behaviour by design; the skill fires on its own maintenance triggers. Two pointer-worthy edges exist anyway: gallery-pipeline's SHA-pin line (Job 2 #28) and skills_index.py ownership (#8 below). | ledger-and-session-records | — | — | The two LOW pointers; otherwise leave the asymmetry alone. |
| 4 | Trigger misdirection: orrery-coding-conventions' description names `star_visualization_gui` but the skill contains no star-specific content — a session on star GUI work loads 343 lines and finds nothing for it, while believing it has fired the right skill. | orrery-coding-conventions (+ future stars skill) | TRIGGER_GAP | MEDIUM | When the stars skill lands (Job 1 #1), move the filename into its description; until then the general Plotly/GUI conventions do legitimately apply, so this is misdirection, not error. |
| 5 | Three-gallery-skill disambiguation: each of gallery-pipeline / gallery-cache-builder / gallery-assembler carries explicit "that is X / load Y instead" language in its description, and the divisions were verified against the actual repo layout. This is the layer's best trigger-discrimination work. | the three gallery skills | — (GOOD) | — | Preserve; use as the template if the stars skill needs to split later. |
| 6 | agentic-pre-test / safe-file-editing division (project-specific runtime gate vs portable editing discipline) holds cleanly, with correct mutual pointers, including after v1.1 growth on both sides. | both | — (GOOD) | — | Preserve. |
| 7 | Layer boundary (the v3.30 design premise): **holds.** Everything tier-[CRITICAL] in the skills either has its resident pointer (agentic-pre-test, by design) or sits under a resident principle that covers a session which never loads the skill (No Shadow Constants under Fetched-vs-Recalled; Delivery Format under the anti-pattern table's spirit). Nothing in the resident protocol has grown task-specific enough to move down — v3.33 Part 3 is already lean. One boundary *observation*, not a defect: the new Geometry-Constants-move-in-the-same-patch rule lives only in provenance-discipline; a cross-check session that somehow fired without that skill would miss it. Its `fires_when` ("constants") makes that unlikely. | — | BOUNDARY | LOW | Optional single resident line under Fetched-vs-Recalled if Tony wants belt-and-braces; otherwise no action. |
| 8 | Manifest regeneration depends on memory (Version State (a): three weeks of advertised-1.1-actual-1.2 / advertised-1.4-actual-1.6 drift). The alarm the protocol wires to a version mismatch fires falsely on every load of an affected skill in that window — the learned-to-wave-off state the prompt names. | skills_index.py, ledger-and-session-records, protocol | MECHANICS | **MEDIUM** | Bind the tool run to the *version-bump commit*, not to a checkpoint someone must remember: the ledger skill's Protocol-and-Skills-Change-Log step becomes "bump the SKILL.md version → run `skills_index.py` → commit SKILL.md and both protocol copies **together**." Drift then cannot exist at any pushed SHA, no new ceremony, and the step lives where skill-version recording already fires. (Direction only; Tony and the orchestrator design the wording.) |
| 9 | Staging copies under documentation/ (Version State (b)): `orrery-coding-conventions_SKILL.md` and `provenance-discipline_SKILL.md` are habit-synced, byte-identical today, guaranteed by nothing — the exact multiple-copies failure provenance-discipline's own field notes document for PROVENANCE_AUDIT.md. | provenance-discipline (warning), install path | MECHANICS | MEDIUM | Convention: in-flight revisions live under documentation/ **only while in flight**, and the install commit that lands `skills/<name>/SKILL.md` **deletes** the staging copy in the same commit (the PROMPT_/EDIT_ design docs stay as records). The prompt's own lens closes it: a second copy is safe when a tool owns it; no tool owns these, so they should not outlive the flight. |
| 10 | Version-history-inside-the-skill convention (Job 3 item 5's second question): has crossed from serving to preamble in the two just-revised skills (provenance-discipline's ~30 lines worst). The ledger is already the declared change log — the duplication costs scroll distance exactly where the reader is a fresh session. | all (worst: provenance-discipline) | MECHANICS / BALANCE | MEDIUM | Per Job 2 #12: current-version line in the skill; narrative history in the ledger appendix. |

---

## Closing summary

### 1. Counts

**Job 1:** 7 gaps assessed — 1 NEW SKILL (HIGH), 3 SECTION-IN (2 MEDIUM, 1 LOW), 3 NO ACTION. Plus one repo-evidence note (19 unmapped + 2 stale MODULE_DOMAIN_MAP entries).
**Job 2:** 34 rows — by type: STALE 4 · ASPIRATIONAL 0 (checked; none unmarked) · CONTRADICTION 2 · TIER 1 · REGISTER 2 · BALANCE 3 · DUPLICATION 1 · omission 1 · GOOD/verified 20. By severity: HIGH 1 · MEDIUM 5 · LOW 8 (rest GOOD/verified).
**Job 3:** 10 rows — CONTRADICTION 1 (HIGH) · TRIGGER_GAP 1 · MECHANICS 3 · BOUNDARY 1 · GOOD 4.

### 2. The three changes that would most improve the layer (ranked)

1. **Fix the Mars Hill example and cross-guard the two skills** (Job 2 #8 / Job 3 #1). It is the layer's only HIGH: a live instruction that would cause a wrong edit to correct code, in direct conflict with another skill's explicit guard, on exactly the decision (perihelion convention, L-177's cluster) that is pending for Tony. Cost: two sentences. Everything else in this review can wait a session; this one is armed now.
2. **Bind manifest regeneration to the version-bump commit and delete staging copies on install** (Job 3 #8 + #9). These two mechanics findings are the same disease — a copy kept correct by memory — and the same cure: make the tool run and the deletion travel *inside* the commit that creates the need for them. This converts the layer's integrity from "someone remembered" to "cannot be wrong at any pushed SHA," which is the SHA-round-trip philosophy applied to the layer itself.
3. **Cut the stars skill** (Job 1 #1). Largest coverage hole (~22–24 modules), already recognised by the project's own taxonomy, with earned-lesson evidence sitting homeless (`stellar_data_patches`, the star_notes Tier-1 episode, the dual-mode module-pair pattern). Ranked third only because it is the largest effort; it is the highest-value addition.

### 3. What is working and should not be disturbed

The cross-reference graph is fully accurate — every pointer lands and the target says what the pointer claims, across two repos. The three gallery skills' mutual disambiguation language is the best trigger work in the layer. The intent-plus-measured-state Hill rewrite is the correct template for partial conventions and should be named as such, not just tolerated. The field-note discipline is genuinely earned in the strong cases (three-wrong-citations; IPC Sudan; the never-run patch; Halley 11→12) — under any future trimming, notes with observations outrank prose without them. horizons' honest "this area is evolving, read HEAD" disclaimer is the right way to be short. And the module docstring standard is not aspiration: 117 of 117, verified.

### 4. Honest gaps

- The Hill-sphere astronomical classifications (which orbital distance each coded rf matches) were not independently recomputed — the rf values' constancy since the skills' cut SHA was verified, but the perihelion/semi-major/aphelion assignments are trusted to the skills' own cited measurement session. UNVERIFIED independently; Batch 2's cross-check is the right venue, not this review.
- The installed account-profile copies of the two revised skills could not be compared from this session: the container's mounted skill copies predate the August 5 installs (they read v1.1/v1.5), which is a mount-timing artifact, not evidence about the account. The prompt's pre-work statement that both are installed is taken on its word — the ledger skill's own field note (diff installed vs repo directly) is the check Tony can run that this session cannot.
- Credit-line compliance ("add on any substantive edit") was not audited across 117 modules; PRACTICE-tier, low stakes.
- gallery-pipeline's Studio/viewer behavioural claims (WYSIWYG preview flow, mobile rendering facts) were verified for file layout and named symbols but not exercised at runtime — no browser or Studio session in this container.

*Report prepared August 5, 2026 by Claude Fable 5 · built on orrery `3398970` / gallery `f83a3ab` — pushed-at SHA to be appended by Tony after commit.*
