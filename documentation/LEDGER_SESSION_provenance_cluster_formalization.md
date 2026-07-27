# Ledger Session -- Provenance Cluster Formalization + Two Closures

Tony Quintanilla, PE | Claude Sonnet 5 | July 27, 2026

**Built on:**
- orrery (palomas_orrery) @ `dd628b155e1bebea70fd9dee84ed6f43991eed75`
  (re-verified 2026-07-27: HEAD had advanced from this document's original
  anchor, `1ef4f82a`, via an unrelated one-item ledger addition; every
  find/replace target below was re-checked byte-exact against the new
  HEAD before this revision -- still a clean match, nothing below needed
  changing because of the move)
- gallery (tonyquintanilla.github.io) @ `0f8e62ebf5fef86a134dfbbfbc2788bee894e51a`
  (unchanged throughout)

**Type:** LEDGER + RECORD HYGIENE (Fable 5's revised sequencing, step 1 --
see `documentation/REVIEW_provenance_refactor_cluster_scoping.md` section
3). Zero code. Targeted edits, not a full-file rewrite -- apply each block
below via find/replace or paste in your editor, in the order given.

**Closes out:** the five confirmations from chat (ring geometry, period-
vs-radius, retire-vs-wrapper, L-114, L-120), all three of Fable's
independently-verified findings that needed a ledger-side fix (L-154's
resume-handoff correction, L-163's stale Gap text, L-114/L-120's stale
status), formalizes the nine floating items (L-154 through L-162) that
have lived only in handoff documents since July 22, **and** the full D3
vulnerability-ladder calibration (Gemini 3.1 Pro + GPT 5.5 + Fable 5 +
Sonnet 5 synthesis, closed 2026-07-27) -- folded into L-156 and L-158
below, which are now updated past what those items looked like when this
session was first drafted.

---

## Part 1 -- Nine new blocks: paste into LEDGER_CONSOLIDATED.md

**Where:** immediately after L-151's `Ref:` line and before the
`### W.Deferred -- captured, not yet actionable` heading (this is the end
of the physical `### W.Active -- current phase` subsection, right after
L-151 in the current file).

**Find** (the exact line currently marking that boundary):
```
### W.Deferred -- captured, not yet actionable
```

**Replace with** (all nine blocks, then the original heading):

```
#### [L-154] Gallery feature-rendering JS layer (shells, rings, radiation belts -- Artifact 2 prerequisite)
<!-- L:154 status:BLOCKED upd:2026-07-27 section:W.Active flag: rice:3/3/70/3 -->
- **What.** The client-side JS that reads `ring_system`, `van_allen_belts`,
  `atmosphere_shell`, and `radiation_belts` out of the served cache and
  actually draws them. `assemble.py` already resolves and reports the
  feature dispatch as data; nothing draws it yet.
- **Blocked on:** the L-155-162 provenance-scoring cluster below (data/
  scoring settled before this gets built, not the other way around).
- **Correction (2026-07-27, Fable 5 review + Sonnet 5 independent
  verification, both against live HEAD):**
  `documentation/HANDOFF_gallery_feature_layer_L154_resume.md` claimed the
  resolver bug (params dropped by `tuple(dict)` in `resolver.py`) was
  "fixed and settled." It is NOT -- `resolver.py` line 133 still reads
  `tuple(rec.get("features") or ())`, and `objects_config.json`'s
  `features` values are genuinely nested dicts (Earth's atmosphere
  fractions, Jupiter's ring radii, all present), so the line still drops
  every parameter to bare category-name keys. The resume handoff is
  corrected in place (Part 3 below) -- this entry is the ledger-side
  record so the claim can't resurface from a stale copy of that handoff.
- **Open design questions once unblocked:** geometry-building approach
  (port the orrery's shell/belt/ring math into JS literally, or design
  fresh JS-native trace builders -- "knowledge transfers, not code");
  legend behavior (shared legendgroup vs. independently-toggleable rows);
  sequencing (validate on Earth's already-closed Mode-5 harness first, or
  build straight into Jupiter/Saturn since that's what's gating Artifact 2).
**Gap:** wait on the cluster below; land the one-line resolver fix in the
first gallery session that resumes this item -- before anything else in
the resume handoff is acted on; then a design session for the three open
questions above; then build (Opus 5) + Mode 5 acceptance.
**Ref:** `assemble.py`, `resolver.py`, `render_objects.py`, `presentation.py`;
`data/solar-system/feature_configs.json`; `data/objects_config.json`;
`documentation/HANDOFF_gallery_feature_layer_L154_resume.md`;
`documentation/REVIEW_provenance_refactor_cluster_scoping.md` (section 5);
L-149/L-150/L-151 (M2 track); L-155-L-162.

---

#### [L-155] Cross-repo constants/geometry pinning checks -- built INTO provenance_scanner.py, not a standalone script
<!-- L:155 status:PENDING-GATE upd:2026-07-27 section:W.Active flag: rice:3/4/75/2 -->
- **What.** Pinning-test logic ("did this specific value drift," binary
  asserts -- the `test_constants_provenance.py` pattern, not the open-ended
  scanner pattern) that reads `objects_config.json`'s `features` values in
  the gallery repo and asserts each equals its named source in the orrery:
  `CENTER_BODY_RADII[x]` for physical radius, the specific dict literal in
  `earth/jupiter/saturn_visualization_shells.py` for ring/belt/atmosphere
  geometry.
- **Design (settled, per `DESIGN_HANDOFF_provenance_scoring_and_pinning.md`
  D6, confirmed on review D6d):** lives inside `provenance_scanner.py`'s own
  run via relative path (`../tonyquintanilla.github.io/...`) -- no separate
  script, no network. Absorbs `test_constants_provenance.py`'s existing
  logic too, one pinning mechanism not two. Fails loud: nonzero exit code
  on any pinning failure (the only hard exit-code gate in the whole
  cluster -- see L-156's D7 for why Tier-1 never gets one).
- **Explicitly out of scope:** `coverage_index.json` / `feature_configs.json`
  (gallery-cache-builder's own test suite's job); anything JS-side.
- **Gated on L-156** (scoring must be correct first) **and effectively on
  L-162** (pinning against 18 named constants is simpler than 3 named + 15
  dict-path lookups -- worth L-162 landing first per its own note, though
  not a hard blocker).
- **Confirmed 2026-07-27 (Sonnet 5, live HEAD):** nothing built yet --
  `provenance_scanner.py` has zero occurrences of `run_pinning_checks` or
  `PINNING_MAP`.
**Gap:** finalize the explicit key-path mapping (gallery config key ->
orrery source location) as a table, not name-matching; design where this
lives inside `provenance_scanner.py` (new function alongside
`find_cross_file_issues`); build (Opus 5, Phase 3 per the amended design)
-- D3 itself is closed (see L-156), so what actually gates this now is
L-156's Phases 1-2 landing in code, not any further calibration round.
**Ref:** `test_constants_provenance.py` (direct precedent, including its
motivating bug: `close_approach_data.py`'s stale `CENTER_BODY_RADII` copy);
`provenance_scanner.py` `main()`; `constants_new.py`; `data/objects_config.json`;
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`;
`DESIGN_REVIEW_provenance_scoring_and_pinning.md`; L-154; L-156; L-157; L-160; L-162.

---

#### [L-156] Provenance scanner scoring model fix -- criticality (category-based) + vulnerability recalibration + comprehensive sweep
<!-- L:156 status:OPEN upd:2026-07-27 section:W.Active flag: rice:5/4/80/3 -->
- **What.** `provenance_scanner.py`'s scoring currently mis-prioritizes
  exactly the data this cluster depends on: `SUN_RADIUS_KM` /
  `EARTH_EQUATORIAL_RADIUS_KM` / `JUPITER_EQUATORIAL_RADIUS_KM` score 6
  (Tier 3, "no action required"); `KM_PER_AU` / `CENTER_BODY_RADII` score
  10 (Tier 2). Root cause: criticality is resolved by direct-import-count
  of the exact symbol name, so a foundational constant consumed
  indirectly (via a derived dict) scores as if barely used.
- **Decided (Tony, design + review, confirmed again in chat 2026-07-27):**
  - **Two criticality categories: MEASURED (C=5) and RELATIONAL (C=4).**
    Not consumer-count-based -- a category judgment, brought in line with
    how display strings already score.
  - **Ring geometry sits in MEASURED, the top tier.** Tony's own reasoning
    (2026-07-27): "in general planetary shells are less certain [but] the
    rings are better defined" -- consistent with the design's own boundary
    (independently-measured vs. derived-from-something-tracked), not a
    blast-radius argument.
  - **Orbital period and radius share the top tier despite different
    failure shapes.** Tony (2026-07-27): "these are fundamental data."
  - **Explicit `undetermined` sentinel** for anything that can't be
    confidently placed in cosmetic/MEASURED/RELATIONAL -- gets its own
    banner, same visibility as the Tier-1 banner. **Naming conformance
    (Fable 5, this review):** use `undetermined`, matching L-163's already-
    decided sentinel name for the same shape of problem, NOT `UNCLASSIFIED`
    as the design review's D2 amendment literally wrote it (that text
    predates L-163's naming decision). Whoever builds Phase 1 implements
    the D2 concept under this name.
  - **Vulnerability ladder (D3): decided,** via a three-AI calibration
    round (Gemini 3.1 Pro, GPT 5.5, Fable 5) plus Sonnet 5 synthesis,
    closed 2026-07-27. Four rungs, same count as today -- no Tier score
    recalibration needed:
    - **V1 FETCHED** -- live pipeline query at runtime. Unchanged.
    - **V2 CROSS-CHECKED** -- never auto-promotable to V1, at any rigor
      level (all three AIs converged on this against my initial draft,
      which had proposed a conditional path to V1; the scanner can't
      observe whether a check was actually rigorous, only a claim that
      it was -- the same cite-to-clear risk as a `# Source:` tag over
      recalled data). Requires a structured, dated annotation: who/what
      checked, against which authority, when, **and whether the check
      was blind (no anchoring)** -- the last field added directly from
      this project's own history (see below), not from the panel.
    - **V3 SOURCED** -- cited but never independently cross-checked,
      *and* anything decayed from V2 over time. **Tony (2026-07-27):
      merged, not split** -- the recency/staleness distinction a split
      would have preserved isn't lost, it lives in the dated field on
      the V2 annotation; it just stops being double-counted as its own
      score tier. Matches Fable's calibration principle (rungs
      distinguished by required action, not by how a value came to be
      wrong) over the split GPT and I had initially favored.
    - **V4 RECALLED** -- no citation at all. Unchanged.
    - **Evidence base (verified against project history, not just the
      two cases the worksheet opened with):** Arrokoth (~1000x radius
      error, sourced not cross-checked) and Parker Solar Probe (surface-
      vs-center convention error, introduced *during* a claimed
      verification) motivated the original ask. Two more, found on a
      follow-up pass, changed the answer: a near-miss where Claude's own
      draft Gemini prompt included its own numbers before Tony caught
      the anchoring risk (`ADDENDUM_v23_design_session_narrative.md`),
      and a session where Gemini's *own* cross-check output was wrong on
      three counts against the primary source
      (`HANDOFF_addendum_phase1_and_uranus_cleanup.md` /
      `HANDOFF_provenance_phase1_v17.md` onward) -- direct evidence that
      cross-checking is itself an interpretation-laden, fallible act,
      not a passive validator. A positive counter-case exists too
      (`MANIFEST_bow_shock_and_dipole_cone_v1.md`, blind pass, 7/8
      agreement) -- the mitigation isn't hypothetical.
    - **Derived values:** not a separate rung (this cluster's original
      framing, and L-158's own title, were wrong on this point) -- an
      *inheritance rule* instead. A value derived at runtime from
      tracked inputs inherits its weakest input's rung, once the
      derivation logic itself has cleared one cross-check. A value
      derived once and then hardcoded as a literal inherits nothing --
      it's a copy, not a derivation, and lands in plain V3 with the
      derivation comment as its citation. See L-158, retitled
      accordingly.
  - **Tier-1 never gets an auto-exit gate, at any threshold** (D7, review
    amendment) -- permanent banner, human judgment, indefinitely. The only
    hard exit-code gate in the cluster is L-155's pinning checks.
- **Full comprehensive-sweep findings folded in** (design section 3): the
  never-fixed inline `'source':` dict-value pattern; the duplicate-
  detector's same-file/dict-kind blind spots; missing magnetosphere unit
  vocabulary; the comet accepted-residual that contradicts the new scheme;
  "Option A" retired.
**Gap:** (1) fix the `CENTER_BODY_RADII` duplication per L-162 (separate
dedicated session); (2) resolve the five comprehensive-sweep items;
(3) build Phases 1-3 (Opus 5) against the decided ladder above -- the D3
gate is clear, nothing further blocks the build.
**Ref:** `provenance_scanner.py` (`find_cross_file_issues`,
`CONCEPT_ALIASES`, `NUMERIC_CLAIM_RE`); `constants_new.py`;
`data/provenance_exceptions.json`; `documentation/provenance_audit_handoff_v1.md`
(Arrokoth/Parker precedent); `ADDENDUM_v23_design_session_narrative.md`
(anchoring near-miss); `HANDOFF_addendum_phase1_and_uranus_cleanup.md`,
`HANDOFF_provenance_phase1_v17.md` (Gemini cross-check itself wrong);
`MANIFEST_bow_shock_and_dipole_cone_v1.md` (blind-pass positive case);
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`;
`DESIGN_REVIEW_provenance_scoring_and_pinning.md`; L-163 (naming precedent);
L-155; L-157; L-158; L-159; L-161; L-162.

---

#### [L-157] Gemini cross-check of shell config ring/belt/atmosphere geometry values
<!-- L:157 status:OPEN upd:2026-07-27 section:W.Active flag: rice:2/3/85/2 -->
- **What.** Run the proven April 2026 methodology (Claude drafts a
  fact-check worksheet, Gemini cross-checks against authoritative sources,
  Tony integrates) against the raw geometry dicts in
  `earth_visualization_shells.py`, `jupiter_visualization_shells.py`,
  `saturn_visualization_shells.py` (`ring_system`, `van_allen_belts`,
  `radiation_belts`, `atmosphere_shell`) -- confirmed these specific
  values have never been through this process.
- **Sequencing (confirmed, review section 5):** runs sequentially through
  the same Mode 7 relay channel as the D3 calibration and L-161's sweep,
  not as a parallel thread -- after Phase 1-2 (L-156) ships, so results can
  be annotated in a form the scanner can actually see.
**Gap:** draft the worksheet (per `worksheet_jupiter_visualization.md`
template, scoped to config values not narrative strings) **blind -- no
Claude-derived figures included**, per the near-miss already caught once
in this project (`ADDENDUM_v23_design_session_narrative.md`: an anchored
draft prompt was rewritten to ask de novo after Tony flagged the
rubber-stamp risk); carry to Gemini; integrate corrections; apply the
cross-checked annotation (with the blind/anchored field, per L-156) once
L-156's build defines its form.
**Ref:** `provenance_audit_handoff_v1.md`; `MODE7_gemini_crosscheck_magnetosphere.md`;
`worksheet_jupiter_visualization.md`; `ADDENDUM_v23_design_session_narrative.md`
(blind-worksheet precedent); L-155; L-156; L-161.

---

#### [L-158] Derived-constant vulnerability inheritance rule (revised from a proposed rung, 2026-07-27)
<!-- L:158 status:OPEN upd:2026-07-27 section:W.Active flag: rice:4/2/70/1 -->
- **What.** Values computed from already-tracked primaries (e.g.
  `SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU`) don't fit the criticality
  question at all -- it's a Vulnerability question.
- **Superseded (D9's original framing, and this item's own original
  title, were wrong):** "derived rung = V1" treated a derived value as
  structurally immune to drift. Both Fable 5 and GPT 5.5's D3 calibration
  passes rejected that premise independently -- the formula, the units, or
  a wrong parent reference are their own error surface (Fable's cited
  precedent: Mars Climate Orbiter, a real mission lost to exactly this
  class of bug), and a value computed once and then hardcoded as a
  literal isn't protected by its original derivation at all.
- **Decided (2026-07-27, folded into L-156's ladder as a rule, not a
  rung):** two cases, not one tier --
  - **Derived at runtime** (formula lives in the code, evaluates from the
    tracked primary every call): inherits its weakest input's V-rung,
    but only once the derivation logic itself -- the formula, the units,
    the parent reference -- has cleared one independent cross-check.
    Until that check happens, treat as unverified regardless of the
    input's own rung.
  - **Derived once, then frozen as a literal** (a hardcoded number with a
    "computed from X" comment): not actually derived any more -- it's a
    copy, and copies drift by exactly the mechanism this item's original
    premise claimed was impossible (the primary updates, the frozen
    literal doesn't). No special handling: plain V3 (sourced-unchecked),
    with the derivation comment serving as its citation.
  - The two-factor structural check (`# Derived:` comment + AST
    confirmation it's actually computed) still stands as the mechanism
    for telling the two cases apart -- it just no longer implies an
    automatic V1 grant on its own.
**Gap:** build -- rides Phase 1 of L-156's scanner build; identify which
existing `# Derived:` comments in `constants_new.py` are runtime formulas
vs. frozen literals before assigning either treatment.
**Ref:** `constants_new.py` derived-constants section; L-156 (holds the
full ladder this rule attaches to).

---

#### [L-159] Disclosed-approximation check (Envelope of the Unknowable, scanner-level)
<!-- L:159 status:OPEN upd:2026-07-27 section:W.Active flag: rice:2/2/60/2 -->
- **What.** Illustrative/stylized values (Mercury's magnetosphere flaring
  parameter, a shared bow-shock eccentricity applied uniformly for
  simplicity) don't fit either criticality tier. Ties to the resident
  protocol's "Show the Envelope of the Unknowable" -- not currently checked
  for anywhere in the scanner. The real question: is the approximation
  disclosed as one, or presented silently as if precise?
- **Decided (D9, review):** annotation convention named -- `# Illustrative:`.
  Planet 9's radius (a model estimate, never directly observed -- see
  L-162) attaches to this item as a case, per the design review.
- **Deliberately deferred:** the ENFORCEMENT check (does the rendered
  hover actually disclose what the comment discloses) is genuinely hard
  and stays open past this cluster closing.
**Gap:** design pass on detection mechanics, once the rest of the cluster
lands.
**Ref:** resident protocol Part 3, "Show the Envelope of the Unknowable";
`MODE7_gemini_crosscheck_magnetosphere.md`; L-156; L-162.

---

#### [L-160] test_constants_provenance.py -- retire once fully absorbed, not before
<!-- L:160 status:OPEN upd:2026-07-27 section:W.Active flag: rice:3/3/90/1 -->
- **What.** Tony confirmed directly: "I never run it, I only run the
  scanner." Correct logic, dashboard-listed, zero code path calling or
  importing it anywhere in the repo. A second, independently-triggered
  entry point that evidence shows doesn't get pulled.
- **Decided (Tony, 2026-07-27):** "if we have fully integrated the
  constants provenance, we can retire the stand-alone file" -- retire is
  confirmed, but **conditional on the integration actually landing first**,
  not a green light to delete it now. This matches the design's own
  sequencing exactly: D10's retirement was always scoped inside Phase 3,
  alongside L-155's pinning engine that replaces what this file checks.
  **Do not delete this file before L-155's pinning checks are built and
  verified to cover the same ground.**
- **On retirement, five reference sites to clear (grepped, not assumed):**
  the file itself; `palomas_orrery_dashboard.py`'s menu entry (~line 227);
  `module_atlas.py`'s ROLE_MAP entry; the scanner's own MODULE_DOMAIN_MAP
  entry and report mention; the comment in
  `comet_visualization_shells.py` line 695 (reword to point at the
  scanner's pinning section instead). The file's docstring institutional
  memory (the motivating bug, the April verification history) migrates
  into the new pinning section's docstring.
**Gap:** **(decide)** none remaining -- retire-vs-wrapper is settled;
**(do)** execute the five-site cleanup as part of L-155's Phase 3 build,
not before.
**Ref:** `test_constants_provenance.py`; `palomas_orrery_dashboard.py`;
`module_atlas.py`; `provenance_scanner.py`; `comet_visualization_shells.py`
line 695; L-155; L-156.

---

#### [L-161] Gemini sweep -- clear the display-string Tier-2 backlog
<!-- L:161 status:OPEN upd:2026-07-27 section:W.Active flag: rice:3/3/70/2 -->
- **What.** ~330 display-string citations, currently C=4/V=2 under
  *today's* meaning of V2 (SOURCED). **Re-read against the closed
  ladder, not the old one** (exactly the D1/D7 re-read L-156's Fable 5
  round flagged as needed): under the new scheme, V2 now means
  CROSS-CHECKED, a stronger bar. Only the subset with a genuine,
  independent, dated (and blind-checked) annotation backfills to the new
  V2; everything else -- including anything merely cited -- lands at the
  new V3 (merged sourced+stale). ~130 were already Gemini-verified by the
  April 2026 worksheets: **check those worksheets against the new blind-
  check bar before backfilling** (per `ADDENDUM_v23`'s anchoring near-
  miss, an anchored pass doesn't qualify even if it happened) -- if they
  don't clear it, they need redoing, not just re-tagging. The remainder
  need a genuinely new sweep regardless.
- **File concentration, confirmed empirically:** 84% of the 330 sit in 15
  files. `celestial_objects.py` alone is 50 findings with zero prior
  worksheet coverage. Neptune, Uranus, Solar, Saturn, Pluto,
  `idealized_orbits.py`, `planet_visualization_utilities.py` also never
  had a Gemini pass.
- **Sequencing (revised on review):** runs AFTER L-156's build ships, not
  parallel with it -- the urgency doesn't exist until the V-ladder change
  actually lands.
- **Practical note:** consider the same Mode 7 relay channel as L-157
  (sequentially, not merged in scope) rather than a second separate
  Gemini engagement.
**Gap:** draft first worksheet (`celestial_objects.py`) **blind**, same
requirement as L-157; confirm the April worksheets' actual coverage
against the new blind-check bar, not just their topic coverage, before
assuming which ~130 are already clear.
**Ref:** L-156; L-157; L-160; `worksheet_*.md` set;
`ADDENDUM_v23_design_session_narrative.md` (blind-worksheet precedent).

---

#### [L-162] CENTER_BODY_RADII full de-duplication -- dedicated Sonnet session
<!-- L:162 status:OPEN upd:2026-07-27 section:W.Active flag: rice:3/3/90/1 -->
- **What.** Promote all 15 remaining `CENTER_BODY_RADII` bodies (Mercury,
  Venus, Moon, Mars, Phobos, Saturn, Uranus, Neptune, Pluto, Bennu, Eris,
  Haumea, Makemake, Arrokoth) to named module-level constants in
  `constants_new.py`, each keeping its existing citation. **Excludes
  Planet 9** (model estimate, never directly observed -- carries to L-159
  instead).
- **Confirmed 2026-07-27 (Sonnet 5, live HEAD): not started.** Only
  Sun/Earth/Jupiter are named; `CENTER_BODY_RADII` still hardcodes all
  three as raw literals (695700, 6378.137, 71492) rather than referencing
  the names -- so even the original 3-body-minimum hasn't landed. Every
  dict entry does carry a good inline citation already; that's not what's
  missing. What's missing is promotion to its own named constant so each
  body scores as its own scanner row instead of one undifferentiated dict.
- **Why now, not "eventually":** simplifies L-155's Phase 3 pinning engine
  -- pins against 18 named constants directly instead of dict-path AST
  extraction for 15 of them. D3 is closed (see L-156), so nothing about
  this item's timing depends on it any more -- it can run whenever a
  dedicated session is free.
**Gap:** dedicated Sonnet session -- fresh SHA pull, safe-file-editing
discipline (bottom-up, ASCII, py_compile clean), credit line, rewrite
`CENTER_BODY_RADII` to reference the new names instead of literals.
**Ref:** `constants_new.py`; `DESIGN_REVIEW_provenance_scoring_and_pinning.md`
section 3a; L-155; L-156; L-159 (Planet 9 case).

---

### W.Deferred -- captured, not yet actionable
```

---

## Part 2 -- Three corrections to existing entries

### 2a. L-163's stale Gap text

**Find:**
```
**Gap:** Phase 4 (do) -- `ledger-and-session-records`'s Codebase
Tooling bullet and `provenance-discipline`'s role-driven-inclusion
bullet both still describe the retired hand-maintained `ROLE_MAP`
and need rewriting to the auto-regenerated-from-docstring-tags
model; `provenance-discipline`'s version/source-SHA line bumps
1.1 -> 1.2. Unblocked now that Phase 3b's classifier is verified
against live HEAD. Same pass runs `skills_index.py`: the live
Skill Manifest table in `PROJECT_INSTRUCTIONS.md` already shows
`ledger-and-session-records` at 1.2 even though the skill file has
been at 1.3 since Phase 1 -- `skills_index.py` wasn't run (or
wasn't committed) after that bump, so this is a pre-existing drift
Phase 4 fixes as a side effect, not something Phase 4 introduces.
```

**Replace with:**
```
**Gap:** None remaining. **Correction (2026-07-27, Fable 5 review,
finding 6):** this paragraph described Phase 4 as pending; it's actually
CLOSED -- `AS_BUILT_L163_phase4.md` documents all four edits applied,
`provenance-discipline` reads v1.2 and `ledger-and-session-records` reads
v1.4 at HEAD, and the Skill Manifest table in `PROJECT_INSTRUCTIONS.md`
matches. This Gap paragraph was simply never rewritten when Phase 4
closed -- a DONE item's own Gap field describing finished work as
outstanding. Left here struck-through rather than deleted, per the
project's own breadcrumb convention.
```

### 2b. L-114 -- flip to DONE

**Find:**
```
<!-- L:114 status:OPEN upd:2026-07-12 section:D.Priority flag: rice:3/3/90/0.5 -->
```

**Replace with:**
```
<!-- L:114 status:DONE upd:2026-07-27 section:D.Priority flag: rice:3/3/90/0.5 -->
```

Then **find:**
```
**Ref:** GALLERY tools/gallery_cache_builder.py (argparse --config default;
load_config; atomic_swap_dir; recover_incomplete_swap; main() call order).
L-098 (parent). Found 2026-07-11 (Sonnet 5); fixed 2026-07-12 (Opus 4.8).  
```

**Replace with:**
```
**Ref:** GALLERY tools/gallery_cache_builder.py (argparse --config default;
load_config; atomic_swap_dir; recover_incomplete_swap; main() call order).
L-098 (parent). Found 2026-07-11 (Sonnet 5); fixed 2026-07-12 (Opus 4.8).
**Closed 2026-07-27:** all four Gap edits confirmed at gallery HEAD
`0f8e62e` (Fable 5 review + Sonnet 5 independent re-run of the offline
suite from a fresh clone -- PASS, 138 checks, 0 failures, matching the
entry's own stated acceptance check). Tony confirmed no local un-pushed
edits remain. `ledger_index.py` will retag this to section C and move it
into the general archive on next run -- expected, not an error.
```

*(Note: `ledger_index.py` infers the correct closed bucket by physical
position when a DONE item isn't already tagged one -- D.Priority has no
dedicated closed bucket, so this correctly lands in the general C
archive. No manual re-filing needed; running the script does it.)*

### 2c. L-120 -- flip to DONE

**Find:**
```
<!-- L:120 status:OPEN upd:2026-07-15 section:W.Active flag: rice:2/2/95/0.5 -->
```

**Replace with:**
```
<!-- L:120 status:DONE upd:2026-07-27 section:W.Active flag: rice:2/2/95/0.5 -->
```

Then **find:**
```
**Ref:** `data/objects_config.json`; `data/solar-system/coverage_index.json`;
gallery-cache-builder skill ("Adding a new object" section); L-098 (parent).
```

**Replace with:**
```
**Ref:** `data/objects_config.json`; `data/solar-system/coverage_index.json`;
gallery-cache-builder skill ("Adding a new object" section); L-098 (parent).
**Closed 2026-07-27:** confirmed at gallery HEAD `0f8e62e` -- `halley` and
`encke` are both in `coverage_index.json`'s 12 served objects, with
`served_window` populated (not null). Tony (2026-07-27): "probably we can
close. we have not done any mode 5 checks yet in the interactive
development, except for earth. all are procedural so far. artifact 4 is
the render" -- the Halley visual/Mode-5 check belongs to Artifact 4's own
build, not to this item, which was only ever about the object being
served. Closing outright, no residual carried forward.
```

*(Same auto-retag note as 2b: `ledger_index.py` will move this into
`W.Done`, the Web Publication track's own closed bucket, since it's
physically inside that track's section.)*

---

## Part 3 -- After pasting

1. **(do)** Run `python ledger_index.py` (VS Code Run button, default
   path). Expect it to report retagging + physically moving L-114 (to
   section C) and L-120 (to W.Done) automatically, and regenerating the
   INDEX. Read its console output once -- it prints exactly what it
   changed.
2. **(do)** Commit + push via GitHub Desktop.
3. **(do)** Paste the new HEAD SHA into this thread so the next session
   builds on ground truth.
4. Separately: apply Part 4 below (the resume-handoff correction) before
   pushing, so it rides the same commit.

---

## Part 4 -- Correct `documentation/HANDOFF_gallery_feature_layer_L154_resume.md`

**Find:**
```
**Do not read this as needing the provenance work explained again.** If
you're picking this up, the provenance work should already be done or in
build. This document only covers L-154 itself.
```

**Replace with:**
```
**Do not read this as needing the provenance work explained again.** If
you're picking this up, the provenance work should already be done or in
build. This document only covers L-154 itself.

**Correction (2026-07-27, Fable 5 review + Sonnet 5 independent
verification):** Section 1 below originally claimed two things as
already-true that were not, as of this date -- see L-154's ledger entry
for the full record. Both are corrected in place below. Re-verify against
HEAD before resuming regardless; this handoff's own history is now the
cautionary example for why.
```

**Find:**
```
- The resolver bug (params silently dropped by `tuple(dict)` in
  `resolver.py`) is fixed and settled -- small, targeted, not an
  architecture question. (This was the loose thread that, while tracing
  where the params actually come from, led into the provenance detour.)
```

**Replace with:**
```
- The resolver bug (params silently dropped by `tuple(dict)` in
  `resolver.py`) is DESIGNED but NOT YET APPLIED -- confirmed still
  present at gallery HEAD `0f8e62e` (2026-07-27): line 133 still reads
  `tuple(rec.get("features") or ())`, and `objects_config.json`'s
  `features` values are genuinely nested dicts, so every parameter is
  still dropped to bare keys. The fix itself is small and settled --
  land it in the first gallery session that resumes this item, before
  anything else here is acted on. (This was the loose thread that, while
  tracing where the params actually come from, led into the provenance
  detour.)
```

**Find:**
```
- Physical radius source: `constants_new.py`'s `CENTER_BODY_RADII`
  (now with all bodies individually named, per L-162) -- ported into
  `objects_config.json` as data, not a separate JS constants table.
```

**Replace with:**
```
- Physical radius source: `constants_new.py`'s `CENTER_BODY_RADII` --
  once L-162 lands (all bodies individually named; NOT yet done as of
  2026-07-27, still dict-only with good inline citations but zero
  promoted constants beyond Sun/Earth/Jupiter) -- ported into
  `objects_config.json` as data, not a separate JS constants table.
```

---

## Tony-action rollup

- **(do)** Paste Part 1's nine blocks; apply Part 2's three edits; apply
  Part 4's resume-handoff correction.
- **(do)** Run `ledger_index.py`; confirm its console output matches what
  Part 3 describes.
- **(do)** Commit + push via GitHub Desktop; paste the new HEAD SHA back
  into this thread.

**Already closed, reflected in L-156/L-158 above:** the D3 calibration
worksheet went to Gemini 3.1 Pro, GPT 5.5, and Fable 5; all three
returned, Sonnet 5 synthesized, and you closed the one remaining fork
(Q2, merge over split) on 2026-07-27. No further panel round needed
before Opus 5 builds Phase 1 against the ladder in L-156.

Nothing here requires an operation outside your known working set -- every
item is a paste/edit, a script run via VS Code's Run button, or a GitHub
Desktop commit/push.

---

*Session written July 2026 with Anthropic's Claude Sonnet 5. Zero code;
all facts checked against fresh clones at the SHAs above before being
written down.*
