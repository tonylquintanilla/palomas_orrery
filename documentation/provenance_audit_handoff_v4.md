# Provenance Audit -- Handoff v4

## Paloma's Orrery | Tony + Claude | April 17, 2026

---

## Session Continuity

This handoff continues `provenance_audit_handoff_v3.md` (April 17, 2026,
earlier session). v3 completed Step 3 of the audit (6 files cleaned up,
`close_approach_data.py` staleness bug fixed), designed
`test_constants_provenance.py`, and deferred building it to v4.

v4 covers the April 17 evening session. Built four things:

  1. `test_constants_provenance.py` (new, 669 lines, 73 tests)
  2. `module_atlas.py` role reorganization (no OTHER category remains)
  3. `palomas_orrery_dashboard.py` Developer Tools expansion (2 -> 4 buttons
      with workflow descriptions and a path reminder)
  4. `provenance_scanner.py` full rewrite (869 lines -> 1011 lines, around
      a "unit of provenance" abstraction)

All four passed working syntax and end-to-end verification.

---

## Sync Check

Per v3's instruction to verify sync at session start, spot-checked four
of the six files from v3's output state. The project files were stale;
Tony re-uploaded the five audit files (`apsidal_markers.py`,
`idealized_orbits.py`, `close_approach_data.py`,
`planet_visualization_utilities.py`, plus `celestial_objects.py`) and
verification confirmed post-April-17 state: zero remaining hardcoded
`149597870.7` values, `April 17, 2026` credit lines present,
`KM_PER_AU` imports from `constants_new` present.

`gallery_studio.py` and `comet_visualization_shells.py` were not
uploaded; neither needed for this session's work.

`constants_new.py` confirmed at post-audit state (715 lines,
Jupiter = 71492 equatorial).

---

## What Was Completed This Session

### 1. `test_constants_provenance.py` (NEW)

Plain-assert regression harness pinning every verified numeric constant
in `constants_new.py` against its cited value. 73 tests across 9 sections:

  - Fundamental constants (7): IAU/NIST exact definitions
  - Derived constants (4): identity and sanity checks
  - Solar structure (8 + shell-ordering invariant)
  - Heliosphere and Oort (6 + ordering invariant)
  - Spacecraft reference (1): Parker's corrected 9.86 R_sun
  - `CENTER_BODY_RADII` (17 per-body + completeness): the Hybrid
    Radius Convention dict. Several tests include messages like "if
    this is 69911, the pre-April-16 volumetric convention returned"
    so a regression is immediately recognizable.
  - `KNOWN_ORBITAL_PERIODS` (20): planets + major moons + Halley + Sedna
  - Hyperbolic-objects-are-None (12 objects in one consolidated test)
  - Cross-module invariants (5): e.g. `EARTH_EQUATORIAL_RADIUS_KM` must
    equal `CENTER_BODY_RADII['Earth']`

Style choice: plain `assert` functions with a pass/fail counter in
`main()`, no `unittest`/`pytest` dependency. Test functions are
auto-collected by `_collect_tests()` using `inspect.getmembers`. The
harness exits non-zero on any failure.

Verified against the current `constants_new.py`: **73 passed, 0 failed**.

Also verified drift detection works: injected `'Jupiter': 69911` (the
April 16 staleness bug) and confirmed both `test_center_body_radii_jupiter`
and `test_jupiter_equatorial_matches_center_body` fire with messages
pointing at the exact problem.

Design decision: exclude the `INFO` dictionary from v1. Too many
heterogeneous narrative entries; better handled by prose fact-check
(next session).

### 2. `module_atlas.py` Role Reorganization

Two targeted edits to `ROLE_MAP`:

  a. Removed `create_ephemeris_database`, `verify_orbit_cache`,
     `create_cache_backups` from the Cache block. These are one-shot
     scripts and diagnostic tools, not cache managers. Cache block now
     contains only `climate_cache_manager`, `incremental_cache_manager`,
     `orbit_data_manager`, `osculating_cache_manager`, `vot_cache_manager`.

  b. Expanded Developer Tools block from 1 entry (`dep_trace`) to 12:
     added `module_atlas` itself (resolving the pre-existing TODO
     comment), plus `provenance_scanner`, `test_constants_provenance`,
     `test_orbit_cache`, `verify_orbit_cache`, `add_docstrings`,
     `create_cache_backups`, `create_ephemeris_database`,
     `convert_hot_ph_to_json`, `diagnose_bcodmo`, `examine_hot_csv`.

  c. Also promoted `messier_object_data_handler` and
     `sgr_a_visualization_core_arcs` to `pipeline` (Tony's call: they are
     part of plotting pipelines). Added `info_dictionary` to `data` and
     `gallery_json_fixer` to `pipeline`.

  d. Removed a duplicate key in `ROLE_MAP` for `convert_hot_ph_to_json`
     (was in both pipeline and devtool blocks; kept devtool).

  e. Broadened the `pipeline` role description from "Transforms data
     between stages (export, conversion)" to "Transforms data between
     stages (export, conversion, plotting pipelines)" per Tony's
     observation about the two rendering-adjacent modules.

Atlas regenerated. Results: 105 modules, 812 functions, 87K lines.
**The OTHER category no longer exists** -- every module now has an
intentional role assignment.

### 3. `palomas_orrery_dashboard.py` Developer Tools Expansion

Developer Tools section grew from 2 buttons to 4:

  1. Regenerate Module Atlas -- existing
  2. Provenance Scanner -- new
  3. Test Constants Provenance -- new
  4. Dependency Trace -- existing

All four launch interactive (`cmd /k`, console stays open after exit).
Descriptions were expanded to include use-case guidance so future
sessions know when to reach for each tool without re-deriving the
context.

Also added a dim-colored path reminder next to the section header:
*"Run from C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github"*.
This was prompted by a real sync bug: the first `provenance_scanner.py`
run hit the sandbox directory instead of the clean repo and would have
produced misleading results. The reminder is scoped to Developer Tools
only (other sections don't need it).

One small cleanup: the old Atlas button description said "Window closes
when done" -- which was a lie (`cmd /k` keeps it open). Trimmed.

### 4. `provenance_scanner.py` Full Rewrite

This was the largest change and the one that shifted the session.

**Why rewrite, not patch**: the first scan from the clean repo
produced 4660 findings, 2110 Tier-1. On inspection these were almost
entirely false positives -- 142 Tier-1 findings in `constants_new.py`
alone (the most-cited file in the codebase) revealed that the scanner
had a fundamental resolution mismatch: it walked the AST but scored
line-by-line, and this codebase attaches citations at declaration
level (above or below), not line-by-line. A targeted patch would have
fixed the immediate symptoms but left the architecture wrong for this
codebase's conventions.

**The reframe**: "unit of provenance." The unit is the smallest thing
that has a coherent source citation:
  - A dict with one `# Source:` comment is ONE unit, not N entries.
  - A hover string with three co-referring numbers is ONE unit, not
    three separate claims.
  - Each unit is scored once. The report still breaks down dict
    entries for display, but scoring happens at unit granularity.

Three bugs emerged during development that only showed up against real
data:

  (a) **Context block was lookback-only.** The first draft looked
      only ABOVE a declaration for citations. But `constants_new.py`'s
      dominant convention is `KM_PER_AU = 149597870.7` followed by
      `# Source: IAU 2012 Resolution B2` below. Fixed to look both
      directions (lookback=30, lookahead=15).

  (b) **Concept matching was substring-based.** "SPEED_OF_LIGHT"
      matched "SPEED_OF_LIGHT_KM_S" by substring, producing a
      false-positive INCONSISTENCY when the m/s and km/s values
      differed by exactly 1000x (which is correct -- they're the
      same constant in different units). Fixed to exact-name matching.

  (c) **Docstrings are self-describing prose.** The `constants_new.py`
      module docstring talks about provenance using words like
      "Verified", "authoritative", "Source of truth" -- but without
      the structured `# Source:` prefix. The scanner flagged the
      docstring as uncited. Added a separate `DOCSTRING_CITATION_PATTERNS`
      set applied only to docstring-origin strings.

Also added per-name import resolution (`build_name_import_map`): the
criticality score now depends on whether the specific NAME is imported,
not whether the containing module is imported. `KM_PER_AU` scores C=5
because 5 files import it by name. `color_map` in the same module
would score lower because it's not imported anywhere by name.

**Final results** (new scanner vs old on same codebase):

| Metric | Old scanner | New scanner | Change |
|---|---|---|---|
| Total findings | 4,660 | 549 | -88% |
| Tier 1 (FIX NOW) | 2,110 | 280 | -87% |
| `constants_new.py` Tier 1 | 142 | 0 | -100% |
| Inconsistencies | 0 | 0 | clean |
| Consistent duplicates | 4 | 2 | signal sharpened |

The remaining 280 Tier-1 findings are legitimate: 278 are public-facing
narrative strings (mostly in `info_dictionary.py` and shell files) with
numeric claims that lack citation. **This IS the INFO dictionary
fact-check work queue.**

Output file format unchanged. Tony's existing workflow for reading
`PROVENANCE_AUDIT.md` carries over.

---

## Session Reorientation Partway Through

A framing shift happened in the middle of this session that's worth
preserving. Initially I proposed "defer scanner fix, move to INFO
dictionary." Tony pushed back: the INFO dictionary surfaces through
normal visual inspection of plots; scanner-class errors are invisible
during normal use. Fixing the scanner is load-bearing because it's
the only mechanism that finds the silent drift pattern that produced
the April 16 staleness bug.

That reframe is correct and worth preserving. Paraphrasing the
exchange:

> "INFO dictionary errors leak into user experience slowly but don't
> hide. Scanner-class errors accumulate invisibly until some
> downstream plot quietly lies."

The partnership principle here: I was treating "the scanner" as an
auxiliary audit utility. Tony was treating it as load-bearing
infrastructure. The second framing is correct; 87% of my original
plan was built on the first, and it was wrong.

---

## What's Still Deferred

### INFO dictionary fact-check (next session, newly unblocked)

181 entries in `info_dictionary.py`. The provenance scanner now flags
54 Tier-1 findings in that file. These are prioritized by criticality
-- start with the highest-consumer-count entries (`object_type_mapping`,
`class_mapping`) and work down.

Estimated scope: own session, own handoff. Methodology will be prose
fact-check against authoritative sources (SIMBAD references for object
types, NASA fact sheets for planetary descriptions, published papers
for specific claims like "Artemis II closest approach 9,600 km"). Not
a code-editing task so much as a research task with occasional edits.

### Shadow detection for `provenance_scanner.py`

Would have caught the April 16 `CENTER_BODY_RADII` vs
`CENTER_BODY_RADII_KM` bug automatically. The scanner currently only
catches SAME-name-DIFFERENT-value duplicates. Shadow detection catches
DIFFERENT-name-OVERLAPPING-keys-DIFFERENT-values.

Design questions to resolve (flagged for Mode 7 / Gemini consultation
next time):
  - How much key overlap counts as shadowing? 50%? 75%? All keys?
  - Should the comparison be value-sensitive (shadowing only matters
    if values differ) or name-sensitive (any dict with the same keys
    is a shadow candidate)?
  - Legitimate shadowing patterns (e.g. test fixtures copying a subset
    of production data) need to be excluded.

Not blocking the INFO dictionary work. Separate session.

### Known scanner debt / future enhancements

  (a) The 2 remaining "consistent duplicates" findings both involve
      `SPEED_OF_LIGHT_KM_S` and `KM_PER_AU` being defined in both
      `constants_new.py` and `sgr_a_star_data.py`. `sgr_a_star_data.py`
      could import these from `constants_new.py` to eliminate the
      duplication. Low priority -- values agree.

  (b) The `DOCSTRING_CITATION_PATTERNS` set is currently 9 regexes.
      May need more as we encounter docstring styles in other modules.

  (c) Numeric claim regex could be extended to recognize ranges like
      "120-123 AU" as one claim, not two.

---

## Resume Plan (Next Session)

### First: verify sync

Per protocol. Spot-check that the four output files from this session
are present in `/mnt/project/`:
  - `test_constants_provenance.py` -- 669 lines
  - `module_atlas.py` -- has 11 devtool entries, no OTHER category
  - `palomas_orrery_dashboard.py` -- Developer Tools has 4 buttons
  - `provenance_scanner.py` -- 1011 lines, imports
    `build_name_import_map` (new function in this version)

### Second: open the INFO dictionary fact-check session

Own handoff. Recommend starting with highest-propagation entries
(`object_type_mapping` imported by 6 modules, `class_mapping` imported
by 5). These are SIMBAD/terminology mappings that affect every star
visualization.

Spend time understanding the format first before editing. The file
is 2,140 lines, and reading it end-to-end is probably worth an hour
of the next session before proposing any changes.

### Third (optional): scanner shadow detection

Design session with Mode 7 Gemini input. Not blocking.

---

## Review-Repair Protocol for Tier 1 Findings

This section covers HOW to work through the 280 Tier 1 findings the
new scanner produces. It was added after v4 wrap-up when Tony asked
the right question: "does the handoff give me a review-repair protocol?"
The original v4 document covered the tool-building work but not the
operating procedure for using the tools.

### The core rule: Claude cannot be the verifier

The scanner flags "this number has no citation." The fix requires
finding an authoritative source for the number. Claude cannot do that
step reliably:

  - Claude has no reliable web access for primary sources
  - Claude's training data has known errors that look confident
    (example: in April, the codebase had Parker perihelion at 8.86
    R_sun, which matched training-era descriptions; Gemini caught
    that this was surface altitude, not distance from center, and
    the correct value was 9.86)
  - An invented but plausible-looking citation is worse than no
    citation, because it makes the finding disappear from the
    scanner without the value actually being verified

Therefore: **Claude must not add citations agentically.** Claude can
add citations Tony provides, can do the mechanical insertion with
proper formatting, can prepare worksheets of findings-by-file, but
cannot be the one who decides "this is the authoritative source."

### The three-role split (Mode 7, cooperative pattern)

For each file being repaired:

  1. **Claude prep**: Extract the file's Tier 1 findings into a
     worksheet. For each finding, note the line number, the claimed
     value, and the surrounding context. Group findings that share
     a likely source (e.g., all of a shell file's radii probably
     cite the same IAU fact sheet).

  2. **Tony or Gemini research**: Locate the authoritative source
     for each value. Verify the value matches. Cross-check when
     possible. This is the irreducible judgment step.

  3. **Claude mechanical edit**: Take the verified citations and
     insert them into the code with correct formatting and consistent
     comment conventions.

Most files will collapse substantially at step 1. A shell file with
41 findings may only need 5-6 distinct citations once grouped by source.

### Per-file workflow

For each file in the Tier 1 queue:

  1. Open the file and the PROVENANCE_AUDIT.md Tier 1 section side
     by side.

  2. Read the flagged strings together. Identify the small number of
     primary sources they reference (usually: IAU 2015, NASA fact sheet,
     JPL Horizons, one or two specific papers).

  3. Verify each source. Use Gemini as a research partner for any
     claim that is not obviously cited elsewhere in the codebase.
     Claude can help cross-check against constants_new.py (which IS
     cited) and flag discrepancies.

  4. Add block-level `# Source:` comments above the hover-text
     blocks. One block comment often covers 5-10 findings in the
     same section. Do not add inline per-line citations unless the
     source genuinely differs per line.

  5. Re-run the provenance scanner from the dashboard. The file's
     Tier 1 count should drop to zero or near-zero. Any remaining
     findings either (a) need more specific citations or (b) are
     consciously accepted as common knowledge.

  6. Commit that one file. Do not batch multiple files in one
     commit -- keeps the blast radius contained if any citation
     turns out to be wrong later.

### What "done" looks like for a file

After a repair pass, the file is done when one of these is true:

  - Re-scan shows zero Tier 1 findings for this file, OR
  - Re-scan shows remaining Tier 1 findings that Tony has
    consciously classified as common knowledge (document that
    decision in the commit message)

A file is NOT done just because Claude added comments -- the test
is whether the scanner now accepts the citations AND whether Tony
trusts each citation to point at something real.

### Work sequencing recommendation

The 280 Tier 1 findings are concentrated in 19 files. Suggested
order of attack (highest leverage first):

  Stage 1 -- Shell files with shared sources (expected: ~150 findings):
    solar (41), neptune (26), earth (25), uranus (23),
    jupiter (18), comet (18), pluto (11), saturn (9), mercury (8),
    asteroid_belt (8), venus (6), moon (5), mars (5),
    planet9 (4), eris (4)

    These cluster around IAU 2015 fact sheets and NASA planetary
    fact sheets. Each file probably collapses to 4-8 citations.
    Estimated: 6-10 focused sessions, 1-2 files per session.

  Stage 2 -- INFO dictionary (54 findings):
    Own dedicated session. Prose fact-check. Highest user-visibility
    impact because INFO content shows up in hover text and gallery.

  Stage 3 -- Long tail (23 findings across star_notes, spacecraft_
             encounters, sgr_a_star_data):
    Touch when editing those files for other reasons. Low urgency.

### What Claude CAN do agentically in this workflow

To be clear about the non-verification parts Claude can handle alone:

  - Generate a per-file worksheet of findings with context
  - Consolidate duplicate definitions (e.g., the 2 flagged duplicates
    where sgr_a_star_data.py could import from constants_new.py)
  - Mechanical insertion of Tony-or-Gemini-verified citations
  - Re-run the scanner and report before/after deltas
  - Add standard v3.18 credit lines to modified files

What Claude CANNOT do agentically: add a citation Claude cannot
independently verify. If Claude reaches for a citation from training
data, the error-correction loop is broken and the scanner's whole
purpose is defeated.

### Anti-pattern to avoid

Do not ask Claude to "clear the Tier 1 findings in file X" as an
agentic task. That phrasing invites Claude to invent plausible-looking
citations. Instead phrase as:

  - "Prepare a worksheet of Tier 1 findings in file X grouped by
    likely source" (prep)
  - "Here are the verified citations, insert them at the appropriate
    locations in file X" (mechanical)

The distinction matters. Same model, same session; different
failure modes.

---

## Module Updates (Credit Lines)

Files modified this session, per v3.18 Credit Line Convention:

- `test_constants_provenance.py` -- NEW. Credit:
  `Module created: April 17, 2026 with Anthropic's Claude Opus 4.7`

- `module_atlas.py` -- credit line appended:
  `April 17, 2026 with Anthropic's Claude Opus 4.7 (role map
  reorganization; removed OTHER category; broadened pipeline
  description; promoted one-shot scripts and diagnostic tools to
  devtool; promoted plotting-pipeline modules to pipeline)`

- `MODULE_ATLAS.md` -- regenerated with the updated role map

- `palomas_orrery_dashboard.py` -- credit not added (small UI change
  with no semantic impact on the scan logic; could add on next edit)

- `provenance_scanner.py` -- REWRITTEN. Docstring credit:
  `Module rewritten: April 17, 2026 with Anthropic's Claude Opus 4.7
  (replaces earlier line-granular scanner. The previous version
  produced ~2000 false-positive Tier-1 findings because block-level
  citations were invisible at its resolution.)`

---

## Quotables from This Session

"the info dictionary is important but at the end of the day, these
are text lines that we can read with any plot and catch errors by
inspection. the scanner is intended to find errors that are basically
invisible in the code. this is where the issue lies."
-- Tony, reorienting the session away from "defer scanner, do INFO"
toward "fix scanner first"

"you are now the frontier model. the original script was created by
the previous model. if you have a better approach, i am all ears."
-- Tony, on the scanner rewrite authorization

"i prefer the conversation over questionnaires" -- Tony, early in
the session when I reached for `ask_user_input_v0` out of habit

"i am not a software professional and the jargon is hard to follow.
can you put this in plain english please." -- Tony, on jargon

"the modules are part of the plotting pipelines and should be
categorized as such." -- Tony, on the two rendering-adjacent modules

"could you add to the header for developer tools: 'Run from
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github'"
-- Tony, the sync-directory reminder prompted by a near-miss

---

## New Principles Established This Session

### Scanner-class vs INFO-class errors

Two different failure modes, two different tools required:

  - **INFO-class errors**: wrong text in a display string, wrong
    Messier object description, wrong spacecraft encounter date.
    These surface during normal visual inspection. Slow feedback
    loop but reliable. Prose fact-check is the right tool.

  - **Scanner-class errors**: a local dict shadowing a canonical one
    with different values; a constant redefined with the wrong units;
    a computation pipeline using a stale source. These produce
    quantitatively wrong plots that may look visually plausible.
    Silent until some downstream calculation goes noticeably wrong.
    A tool is the only mechanism that finds them.

Both tools exist now. They are complementary, not competitive.

### Unit of provenance

The unit is the smallest thing with a coherent source citation.
Citation patterns in this codebase attach at declaration level (above
or below) or at section headers, not line-by-line. A scanner that
scores line-by-line will produce noise proportional to the size of
the declaration. A scanner that scores at unit granularity produces
one finding per declaration.

This reframe is load-bearing for the scanner's utility but also
applies more broadly: any static analysis that treats "each line as
an independent proposition" will miss structure that the code author
encoded at block level.

### The frontier-model license

When Tony says "you are now the frontier model, if you have a better
approach I am all ears," that's permission to push back on my own
plan if the plan is wrong. Not a rubber stamp -- genuine openness to
a reframe. The scanner rewrite was the right call because the unit
reframe changed enough of the core that a patch-based approach
produced uglier code than starting from the right abstraction. But
this should not become a habit; legacy modules (palomas_orrery.py)
still deserve targeted edits, and this license is specific to
infrastructure rewrites where the reframe is load-bearing.

---

*Handoff v4: three new tools delivered (test_constants_provenance,
rewritten provenance_scanner, dashboard expansion) plus atlas
reorganization. INFO dictionary fact-check unblocked and queued for
v5. Shadow detection deferred to a design session.*
