# Predesign Handoff -- Provenance Scoring Fix, Cross-Repo Gallery Scanner, and Gallery Feature-Rendering JS Layer

Tony Quintanilla, PE | Claude Sonnet 5 | July 22, 2026

**Built on:**
- orrery (palomas_orrery) @ `9b4571851184e599f72de928cada16d30c9010f6`
- gallery (tonyquintanilla.github.io) @ `79710968241f21c8e6e1836bb1ad35219f1a31f0`

**Type:** PREDESIGN (zero code) -- decisions and scoping ahead of the design session.

**Companion:** none yet. This is the originating record for L-154 through L-160 below.

---

## 1. Origin

Session started as predesign for the gallery's client-side feature-rendering
JS layer (shells, rings, radiation belts for Artifact 2 -- Jupiter/Saturn).
Tracing where the served feature parameters actually come from surfaced a
chain of deeper issues: a resolver bug that silently drops feature params, a
question of where physical radii should live, a real gap in what the
provenance scanner can see across the repo boundary, and -- once that was
dug into -- a scoring model in `provenance_scanner.py` that mis-prioritizes
exactly the kind of foundational data this work now depends on. Each finding
was verified against live code/live repo state, not recalled. This handoff
gates L-154 (the original JS-layer work) behind L-155/L-156/L-157 below.

---

## 2. What's settled (do not re-litigate in the design session)

1. **Resolver bug, confirmed, small, targeted fix.** `resolver.py`'s
   `features = tuple(rec.get("features") or ())` iterates a dict and keeps
   only its keys -- every param in `coverage_index.json`'s per-object
   `features` block (already fully populated) is silently dropped before
   `FeatureRequest` is built. Fix: iterate `.items()` and populate
   `FeatureRequest.params`. No architecture question here.
2. **Physical radius source of truth: `constants_new.py`'s `CENTER_BODY_RADII`
   dict** (orrery repo) -- already exists, already cited (IAU 2015 Res. B3),
   already has Earth/Jupiter/Saturn. Not a new orrery-side constant. Gets
   ported into `objects_config.json` (gallery repo) as data, not duplicated
   into a JS constants table -- one port surface, not two independently
   drifting copies.
3. **Feature rendering stays JavaScript, always** -- this is already a
   ratified architectural decision in the assembler code itself
   (`assemble.py` docstring, manifest v2 S0/S2), reversed once already from
   a synthesis error. Not open for reconsideration; it constrains L-154 but
   is out of scope for this predesign gate.
4. **The new cross-repo checks are pinning tests ("did this specific value
   drift," binary asserts), not a second open-ended scanner** -- that part
   of the original reasoning stands. But **they run as a new section
   inside `provenance_scanner.py`'s own execution, not as a standalone
   script.** Reason, confirmed directly by Tony: `test_constants_provenance.py`
   already exists, is correct, and has apparently never been run since it
   was built in April 2026 -- Tony runs the scanner, never this. A second,
   separately-triggered tool doesn't get picked up regardless of how well
   it's built; the fix is riding the one trigger point that actually gets
   used, not creating a third one. Scope is `objects_config.json` (the one
   hand-ported gallery artifact) against its named orrery sources. The
   builder's mechanical copy from `objects_config.json` into
   `coverage_index.json` / `feature_configs.json` is NOT in scope here --
   that's gallery-cache-builder's own test suite's job. Given Tony's
   sibling-directory layout, the scanner (run from the orrery repo) reads
   `../tonyquintanilla.github.io/data/objects_config.json` via relative
   path -- no separate script, no network.
4a. **`test_constants_provenance.py`'s existing constants_new.py pinning
    logic gets absorbed into the same new section**, not left standing
    alone alongside it -- otherwise the fix would still leave one
    never-triggered entry point in place. See L-160 for the file's fate.
4b. **Failures fail loud: nonzero exit code, not just a quiet finding
    in a tier.** Confirmed while checking this: the scanner's existing
    `main()` currently only calls `sys.exit(1)` for an invalid directory
    argument -- Tier-1 findings and detected INCONSISTENCIES are printed to
    the console but never fail the run, even though "Tier-1 = 0 before
    push" is a standing CRITICAL discipline. The new pinning-check failures
    must exit non-zero; whether the pre-existing Tier-1-nonzero case should
    now *also* exit non-zero (for consistency -- right now it's the only
    "loud" failure mode missing one) is a design-session decision, not
    assumed here.
5. **No hand-curated override list for "foundational" items.** Rejected in
   favor of fixing the scoring model itself -- a curated list can miss a
   future addition; a structural/categorical fix can't.
6. **Vulnerability (is this actually correct) is a factual question --
   Gemini's lane. Criticality (how much do we care if it's wrong) is a
   project-priority judgment -- Tony's lane, not Gemini's.** Two different
   axes, two different reviewers.
7. **Criticality should NOT be consumer-count-based for constants/dicts.**
   Orcus's radius (one consumer) and Jupiter's (many) are the same *kind*
   of fact and equally bad to get wrong in kind, just not in reach.
   Consumer-count measures blast radius, not importance. Bring
   constants/dicts in line with how display strings are already scored
   (flat categorical `C_PUBLIC`, no popularity weighting).
8. **Draft criticality categories** (first cut, Tony's to reshape):
   - Fundamental / independently-measured base-unit physical constants
     (radius, mass, orbital period, AU<->km) -- top tier, one consumer or fifty.
   - Geometry defined as a fraction/multiple of an already-tracked base unit
     (Van Allen belts, radiation belts, atmosphere shells -- literally
     `radius_fraction x R_body`) -- one tier below; wrong here doesn't
     corrupt another object's scale the way a wrong base radius does, but an
     error in the base value silently propagates into everything built on it.
   - **Open:** where absolute, independently-measured ring geometry
     (Jupiter/Saturn `inner_radius_km`, not derived from planet radius) sits
     -- with the fundamental tier (it's still primary measured data) or its
     own middle tier. Not settled -- design session's first job.
9. **`CENTER_BODY_RADII` duplication is a real, independent bug**, regardless
   of how criticality gets scored. It hardcodes `695700`, `6378.137`,
   `71492`, `60268` etc. as fresh literals instead of referencing
   `SUN_RADIUS_KM`, `EARTH_EQUATORIAL_RADIUS_KM`, `JUPITER_EQUATORIAL_RADIUS_KM`
   -- in the one file whose own docstring says "Do not redefine these values
   locally." This is why criticality undercounts it: the import-graph has no
   edge to trace, since nothing in the dict actually references the primary
   constants.
10. **The Gemini cross-check on shell config ring/belt/atmosphere values has
    never happened.** Searched every worksheet and provenance handoff in
    `documentation/` -- zero hits for `van_allen`, `ring_system`,
    `belt_distance`, `inner_radius_km`. The April 2026 Gemini pass covered
    `constants_new.py`'s fundamental constants and narrative hover text
    (per-file worksheets) -- not the raw geometry dicts in
    `earth/jupiter/saturn_visualization_shells.py`. These carry `# Source:`
    comments but were never independently checked against them.
11. **Scoring-formula fix must land before or alongside the Gemini cleanup
    pass, not after** -- otherwise newly-cross-checked shell values could
    still land in an ignorable tier for the same reason `SUN_RADIUS_KM` does
    today (Tier 3, "no action required").

---

## 3. Comprehensive sweep of `provenance_scanner.py` (since we're touching it)

1. **Self-documented, never-fixed:** the scanner's own "Known limitations"
   section already states inline `'source': '...'` dict values aren't
   recognized as citations, and names the fix ("extend SOURCE_PATTERNS").
   Written April 2026, never done.
2. **Duplicate/inconsistency detector has two structural blind spots,**
   confirmed by reading `find_cross_file_issues` directly:
   - `if len(files) < 2: continue` -- same-file duplication (exactly the
     `CENTER_BODY_RADII` bug) is invisible by construction.
   - Only `kind == 'constant'` units are ever compared; `kind == 'dict'` is
     excluded from the whole mechanism, so a dict could never be checked
     against a named constant even across files.
   - The code comment directly above the function already names this:
     *"deliberately different names (CENTER_BODY_RADII_KM shadow) are NOT
     caught here -- that requires shadow detection (planned separately)."*
     Planned, never built.
3. **`NUMERIC_CLAIM_RE` unit vocabulary has no magnetosphere units.** No
   Tesla/Gauss/nT, no generic `R_planet` notation (`R_M`, `R_J`, `R_E`) --
   only `R_sun` and the literal phrase "Earth radii." The already-completed
   `MODE7_gemini_crosscheck_magnetosphere.md` cross-check uses exactly that
   notation (`1.45 R_M`, `82 R_J`) -- invisible to citation-checking today,
   not just uncited but unrecognized as a numeric claim at all.
4. **An existing accepted-residual entry contradicts the new criticality
   reasoning.** `comet_visualization_shells.py`'s `COMET_NUCLEUS_SIZES` /
   `COMET_FEATURE_THRESHOLDS` are marked accepted with the reason
   "rendering geometry dicts, low user-visible impact" -- the exact
   reasoning just overturned for ring/belt geometry. Needs re-evaluation
   under the new scheme, not grandfathering.
5. **"Option A" (constant cross-reference for display strings) is
   semi-dead code** -- the scanner's own comments call it "rarely fires...
   insufficient." Lower priority: fix the matching fragility or retire it.

---

## 4. Edge cases already run against the draft criticality scheme

1. **`KM_PER_AU`** -- not a fact about a body, it's the ruler itself. Top
   tier confirmed; flagged as the single highest-leverage entry in the file.
2. **Orbital period vs. radius** -- both fundamental, same tier holds, but
   different failure *shape* (wrong-sized sphere vs. wrong position over
   time via Kepler propagation). Worth Tony explicitly confirming "same
   criticality" is intended despite the different failure kind.
3. **Ring geometry** -- resolved the real tier boundary: not
   "important vs. less important" but "independently measured vs. defined
   as a function of something else already tracked." Jupiter's ring radii
   are their own catalogued numbers; Van Allen belts are literally
   `distance x R_planet`. See open item in section 2.8 above.
4. **Derived constants** (e.g. `SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU`)
   -- not a criticality question. A computed value can't independently
   drift; if wrong, an input was wrong, caught there. This is a
   **Vulnerability** question -- logged separately as L-158, not solved here.
5. **Illustrative/stylized approximations** (Mercury's magnetosphere
   flaring parameter, a shared bow-shock eccentricity used uniformly across
   planets) -- doesn't fit either criticality tier. Ties to the resident
   protocol's "Show the Envelope of the Unknowable." Not a criticality
   question at all -- a separate check (disclosed as approximate, or
   presented silently as precise). Logged separately as L-159.
6. **Taxonomic/type claims encoded via color** -- the scanner's cosmetic
   fallback triggers on dict *name* heuristics ("color"/"label" in the
   name -> auto-bottom-tier, no content inspection). The documented
   Polymele/Leucus size-and-type swap Gemini caught is exactly a taxonomic
   claim; if keyed by color, name-based heuristics would misfire and wave
   it through as cosmetic. Criticality should follow what the value
   *claims*, not how it's named/rendered. Real gap, not hypothetical --
   folded into L-156.

---

## 5. New ledger items

#### [L-154] Gallery feature-rendering JS layer (shells, rings, radiation belts -- Artifact 2 prerequisite)
<!-- L:154 status:BLOCKED upd:2026-07-22 section:W.Active flag: rice:3/3/70/3 -->
- **What.** The client-side JS that reads `ring_system`, `van_allen_belts`,
  `atmosphere_shell`, and `radiation_belts` out of the served cache and
  actually draws them. `assemble.py` already resolves and reports the
  feature dispatch as data; nothing draws it yet (confirmed: the dev
  harness fetches `payload.features` and never uses it -- "Feature
  rendering stays JavaScript (none yet -> no shells drawn; that is
  artifact 2 / F1)").
- **Blocked on:** L-155 (new cross-repo scanner) and L-156 (scoring model
  fix), per the predesign decision that data/provenance gets settled before
  this gets built -- not the other way around.
- **Open design questions once unblocked:** geometry-building approach
  (port the orrery's shell/belt/ring math into JS literally, or design
  fresh JS-native trace builders for the same visual result -- "knowledge
  transfers, not code"); legend behavior (shells/rings share the parent
  object's legendgroup silently, or get independently-toggleable legend
  rows); sequencing (validate on Earth's already-closed Mode-5 harness
  first, or build straight into Jupiter/Saturn since that's what's actually
  gating Artifact 2).
**Gap:** wait on L-155/L-156; then a design session for the three open
questions above; then build (Opus 4.8, per model-assignment discussion this
session) + Mode 5 acceptance.
**Ref:** `assemble.py`, `resolver.py`, `render_objects.py`, `presentation.py`;
`gallery/solar_system_earth_test2.html`; `data/solar-system/feature_configs.json`;
`data/objects_config.json`; L-149/L-150/L-151 (M2 track); L-155; L-156.

---

#### [L-155] Cross-repo constants/geometry pinning checks -- built INTO provenance_scanner.py, not a standalone script
<!-- L:155 status:PENDING-GATE upd:2026-07-22 section:W.Active flag: rice:3/4/75/2 -->
- **What.** Pinning-test logic ("did this specific value drift," binary
  asserts -- the `test_constants_provenance.py` pattern, not the open-ended
  scanner pattern) that reads `objects_config.json`'s `features` values in
  the gallery repo and asserts each equals its named source in the orrery:
  `CENTER_BODY_RADII[x]` for physical radius, the specific dict literal in
  `earth/jupiter/saturn_visualization_shells.py` for ring/belt/atmosphere
  geometry.
- **Re-scoped this session (was: standalone script; now: a new section
  inside `provenance_scanner.py`'s own run).** Reason: Tony confirmed he
  never runs `test_constants_provenance.py`, only the scanner -- a second
  entry point, however correct, doesn't get triggered. Given the
  sibling-directory layout (`palomas_orrery_for_github` and
  `tonyquintanilla.github.io` both under `python_work`), the scanner reads
  `../tonyquintanilla.github.io/data/objects_config.json` via relative
  path when run from the orrery repo -- no separate script, no network.
- **Absorbs `test_constants_provenance.py`'s existing logic too** (not just
  the new cross-repo checks) -- one pinning mechanism inside the scanner,
  not two. See L-160 for what happens to the standalone file.
- **Fails loud: nonzero exit code on any pinning failure** (Tony's call).
  Not a quiet finding sitting in a tier -- this is the entire point of
  fixing "never run" for the old tool: whatever runs now needs to actually
  stop you, not wait to be read.
- **Explicitly out of scope:** `coverage_index.json` / `feature_configs.json`
  (builder-derived, mechanical copy -- gallery-cache-builder's own test
  suite's job) and anything JS-side (the JS reads already-served numbers;
  it doesn't carry its own hardcoded copies, so it isn't a dependency here).
- **Gated on L-156.** Pinning against orrery source is only meaningful once
  that source's own scoring correctly reflects what's actually foundational
  and once the shell config values have been through the Gemini cross-check
  (L-157) -- otherwise this checks against never-independently-checked
  numbers and calls that "verified."
**Gap:** finalize the explicit key-path mapping (gallery config key -> orrery
source location) -- not name-matching, an explicit table; design where this
lives inside `provenance_scanner.py` (a new function alongside
`find_cross_file_issues`, invoked from `main()`/`scan_project()`); decide,
alongside L-156, whether the pre-existing Tier-1-nonzero case should also
start exiting non-zero for consistency (currently the scanner's only loud
failure is an invalid directory argument -- Tier-1 findings just print).
**Ref:** `test_constants_provenance.py` (direct precedent, including its
own motivating bug: `close_approach_data.py`'s stale `CENTER_BODY_RADII`
copy); `provenance_scanner.py` `main()` (current exit-code logic, ~line 1749);
`constants_new.py`; `data/objects_config.json`; L-154; L-156; L-157; L-160.

---

#### [L-156] Provenance scanner scoring model fix -- criticality (category-based) + vulnerability recalibration + constants_new.py de-dup + comprehensive sweep
<!-- L:156 status:OPEN upd:2026-07-22 section:W.Active flag: rice:5/4/80/3 -->
- **What.** `provenance_scanner.py`'s scoring currently mis-prioritizes
  exactly the data this session's work depends on. Confirmed live:
  `SUN_RADIUS_KM` / `EARTH_EQUATORIAL_RADIUS_KM` / `JUPITER_EQUATORIAL_RADIUS_KM`
  score 6 (V=2 x C=3), landing in **Tier 3 -- "no action required."**
  `KM_PER_AU` / `CENTER_BODY_RADII` score 10 (Tier 2). The most
  indispensable file in the codebase sits in tiers that don't get reviewed.
- **Root causes, both confirmed in code, not assumed:**
  1. Criticality is resolved by direct-import-count of the exact symbol
     name (`count>=3 -> C_PROPAGATING`); a foundational constant consumed
     indirectly (via a derived dict) scores as if barely used.
  2. `CENTER_BODY_RADII` hardcodes literals instead of referencing the
     named primary constants -- duplication inside the single-source-of-
     truth file itself, which is *why* the import graph can't see true
     reach (no code edge to trace). See section 3 finding #2 above --
     the duplicate detector can't catch this either (same-file + dict-kind
     blind spots), and a code comment already anticipated "shadow
     detection (planned separately)."
- **Decided this session (Tony):** Criticality is a project-priority
  judgment, not a fact -- not Gemini's lane. Not consumer-count-based for
  constants/dicts; bring them in line with how display strings already get
  flat categorical scoring. Vulnerability ("was this actually checked") IS
  a factual question -- still appropriate for Gemini, specifically because
  we have two documented real-world cases (Arrokoth 1000x error, Parker
  Solar Probe distance) where "sourced" and "wrong" coexisted, meaning the
  current V=2 for merely-sourced-but-never-cross-checked is calibrated too
  generously.
- **Draft criticality categories (Tony's first cut, section 2.8 above) --
  not finalized; "where does absolute ring geometry sit" is explicitly open.**
- **Full comprehensive-sweep findings folded in here** (section 3 above):
  the never-fixed inline `'source':` dict-value pattern; the duplicate-
  detector's same-file/dict-kind blind spots; the missing magnetosphere
  unit vocabulary (Tesla/Gauss/nT, `R_planet` notation); the comet accepted-
  residual that contradicts the new scheme; "Option A"'s fix-or-retire call.
- **Full edge-case sanity-check results folded in here** (section 4 above),
  including the taxonomic-claim-via-color gap (Polymele/Leucus precedent).
**Gap:** design session to (a) finalize the criticality category boundaries
and where absolute ring geometry sits, (b) design the vulnerability
recalibration with Gemini (cross-checked vs. merely-sourced, informed by
the Arrokoth/Parker precedent), (c) fix the `CENTER_BODY_RADII` duplication
(reference the primaries; update `test_constants_provenance.py` accordingly
-- tightens the pinning, doesn't weaken it), (d) resolve the five
comprehensive-sweep items, (e) decide the annotation mechanism/keyword for
"cross-checked" status so it's scanner-visible going forward, not just in
scattered handoffs.
**Ref:** `provenance_scanner.py` (`find_cross_file_issues`, `CONCEPT_ALIASES`,
`NUMERIC_CLAIM_RE`, criticality assignment ~line 1112); `constants_new.py`;
`test_constants_provenance.py`; `data/provenance_exceptions.json`;
`documentation/provenance_audit_handoff_v1.md` (Arrokoth/Parker precedent);
`documentation/MODE7_gemini_crosscheck_magnetosphere.md`; L-155; L-157;
L-158; L-159.

---

#### [L-157] Gemini cross-check of shell config ring/belt/atmosphere geometry values
<!-- L:157 status:OPEN upd:2026-07-22 section:W.Active flag: rice:2/3/85/2 -->
- **What.** Run the already-proven April 2026 methodology (Claude drafts a
  fact-check worksheet, Gemini cross-checks against authoritative sources,
  Tony integrates) against the raw geometry dicts in
  `earth_visualization_shells.py`, `jupiter_visualization_shells.py`,
  `saturn_visualization_shells.py` (`ring_system`, `van_allen_belts`,
  `radiation_belts`, `atmosphere_shell`) -- confirmed via full search of
  `documentation/` that these specific values have never been through this
  process. Not a new process; a known-good one applied to a gap that was
  invisible until these numbers needed to leave the repo.
- **Sequencing:** land alongside or after L-156's scoring fix so the
  results are annotated in a way the scanner can actually see going
  forward (see L-156 gap item (e)), not just recorded in another
  scattered handoff.
**Gap:** draft the worksheet (per `documentation/worksheet_jupiter_visualization.md`
template precedent, scoped to config values this time, not narrative
strings); carry to Gemini via Tony; integrate corrections; apply the
cross-checked annotation once L-156 defines its form.
**Ref:** `documentation/provenance_audit_handoff_v1.md`;
`documentation/MODE7_gemini_crosscheck_magnetosphere.md`;
`documentation/worksheet_jupiter_visualization.md`; L-155; L-156.

---

#### [L-158] Derived-constant Vulnerability rung (structurally can't independently drift)
<!-- L:158 status:OPEN upd:2026-07-22 section:W.Active flag: rice:4/2/70/1 -->
- **What.** Values computed from already-tracked primaries (e.g.
  `SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU`) surfaced during the
  edge-case sanity check (section 4, item 4) as not fitting the criticality
  question at all -- it's a Vulnerability question. A derived value can't
  drift on its own; if it's wrong, an input was wrong, and that gets caught
  at the input. Candidate for its own Vulnerability rung, arguably safer
  than "cross-checked," since correctness here is structural rather than
  evidenced by a citation.
**Gap:** design the rung's semantics and where it sits relative to
V_FETCHED/V_SOURCED; decide whether `constants_new.py`'s existing
"Derived (computed, never hardcoded)" section already qualifies wholesale.
**Ref:** `constants_new.py` derived-constants section; L-156.

---

#### [L-159] Disclosed-approximation check (Envelope of the Unknowable, scanner-level)
<!-- L:159 status:OPEN upd:2026-07-22 section:W.Active flag: rice:2/2/60/2 -->
- **What.** Illustrative/stylized values (Mercury's magnetosphere flaring
  parameter, a shared bow-shock eccentricity applied uniformly across
  planets for simplicity) surfaced during the edge-case sanity check
  (section 4, item 5) as not fitting either criticality tier. Ties directly
  to the resident protocol's "Show the Envelope of the Unknowable" -- but
  that principle isn't currently checked for anywhere in the scanner. The
  actual question: is the approximation disclosed as one (fine), or
  presented silently as if precise (a real finding, arguably as serious as
  a bad citation)?
**Gap:** least-formed item in this batch -- needs its own design pass on
detection mechanics (a keyword convention? a review pass like L-157's, but
checking disclosure rather than correctness?) before it's buildable.
**Ref:** resident protocol Part 3, "Show the Envelope of the Unknowable";
`documentation/MODE7_gemini_crosscheck_magnetosphere.md` (illustrative
eccentricity example); L-156.

---

#### [L-160] test_constants_provenance.py has apparently never been run since it was built -- absorb into provenance_scanner.py
<!-- L:160 status:OPEN upd:2026-07-22 section:W.Active flag: rice:3/3/90/1 -->
- **What.** Tony confirmed directly this session: "I never run it, I only
  run the scanner." `test_constants_provenance.py` is correct, dashboard-
  listed, and has no code path calling or importing it anywhere in the
  repo -- confirmed by grep. It's a second, independently-triggered entry
  point, and the evidence is that independent triggers don't get pulled,
  no matter how well-built the tool behind them is. This is "Verify
  Execution, Not Appearance" landing on the project's own tooling: a
  script existing and being listed is not proof it runs.
- **Fix, tied directly to L-155:** absorb its pinning logic into
  `provenance_scanner.py`'s own execution (same new section that handles
  the cross-repo gallery checks), so both the existing constants_new.py
  pins and the new gallery pins ride the one trigger that's actually used.
- **Open:** what happens to the standalone file afterward -- retire it
  entirely (cleanest; avoids a redundant, easy-to-forget second copy of the
  same asserts), or keep it as a thin wrapper importing the scanner's new
  pinning function for the rare case someone wants to run just that check.
  Tony's call, not assumed here.
**Gap:** design session decides retire-vs-wrapper; if retired, remove its
dashboard menu entry too so the menu doesn't point at a dead file.
**Ref:** `test_constants_provenance.py`; `palomas_orrery_dashboard.py`
(menu entry, ~line 227); L-155; L-156.

---

## 6. Prompt for the Designer (optimized for Claude Fable 5)

*(Rewritten per Anthropic's official "Prompting Claude Fable 5" guidance --
Fable 5 follows brief, reason-first instructions better than enumerated
checklists, and over-specifying process can degrade its output. This
version trims behavioral micromanagement and keeps the actual scope/content,
which Fable 5 is well-suited to navigate on its own judgment. Self-contained
-- paste as the opening message; doesn't require this chat's history, only
this document and live repo access.)*

> I'm working on the Paloma's Orrery project with Tony Quintanilla (PE,
> retired civil/environmental engineer, not a professional developer --
> builds this through AI collaboration, holds sole commit authority). His
> provenance scanner's scoring model currently buries the most foundational
> data in the codebase in tiers nobody reviews, and it's about to gate a
> new check protecting values served to a public gallery. He needs that
> scoring model actually fixed, not patched around. With that in mind:
>
> **This is a design session. The deliverable is a decision document, not
> code.** Don't write or edit the scanner, don't touch either repo, don't
> propose a diff. If your design's natural next step is "now implement
> this," stop there and hand it back rather than continuing into a build.
>
> Read `PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md` (this
> document) in full first, then load the `provenance-discipline` and
> `ledger-and-session-records` skills. Everything asserted as settled fact
> in section 2 was checked against live code this session, not recalled --
> pull both repos fresh yourself and re-confirm the SHAs in "Built on"
> still match before building on anything load-bearing (nightly data-only
> commits are expected; code changes aren't, and would mean re-checking
> this handoff's claims). Where you're not certain of something, say so
> rather than asserting it.
>
> Don't re-litigate section 2 ("What's settled") -- that's closed,
> including that the new checks live inside `provenance_scanner.py` itself
> (not a standalone script -- a second entry point already proved it
> doesn't get used) and that failures exit non-zero. Your actual scope is
> section 2's one open item (where absolute ring geometry sits in the
> criticality scheme) and L-156's gap list: the criticality category
> boundaries, the vulnerability recalibration (with Gemini specifically --
> that one's factual, "was this checked against a source"; everything else
> here is Tony's judgment call, not Gemini's), the `CENTER_BODY_RADII`
> de-duplication design, the five comprehensive-sweep findings (section 3)
> and six edge cases (section 4), the cross-checked-vs-cited annotation
> mechanism, where the new pinning section lives in `provenance_scanner.py`
> and how it's invoked, `test_constants_provenance.py`'s fate (retire or
> thin wrapper), and whether the pre-existing Tier-1-nonzero gap should
> also start failing loud now that the scanner is gaining its first
> nonzero-exit checks.
>
> Use your own judgment on how to sequence and structure these -- if a
> cleaner design exists than what the ledger items above imply, say so;
> don't just work through them as a fixed checklist. Pause for Tony only on
> an actual judgment call with no clearly better answer, or something this
> handoff didn't already decide -- not to confirm each step along the way.
>
> When you report back: lead with what you'd actually recommend, not a
> survey of everything considered. Full reasoning and tradeoffs belong in
> the design document itself, not the opening of your response.
>
> Deliverable: a design handoff (zero code), anchored with both repos' SHAs
> the same way this one is, either fully resolving L-156's gap list or
> clearly marking what's decided vs. still open.

---

*Session written July 2026 with Anthropic's Claude Sonnet 5.*
