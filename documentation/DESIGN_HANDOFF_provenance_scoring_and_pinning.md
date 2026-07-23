# Design Handoff -- Provenance Scoring Model Fix and In-Scanner Pinning Checks

Tony Quintanilla, PE | Claude Fable 5 | July 22, 2026

**Built on:**
- orrery (palomas_orrery) @ `9b4571851184e599f72de928cada16d30c9010f6`
- gallery (tonyquintanilla.github.io) @ `79710968241f21c8e6e1836bb1ad35219f1a31f0`

**Type:** DESIGN SESSION (zero code) -- decision document for L-155, L-156,
L-158, L-160, and the section-2 open item from the predesign handoff.

**Companion:** `PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md`
(same SHAs -- both repos verified unchanged since it was written; not even
the expected nightly data commit had landed).

---

## 0. What this session verified before designing

Every load-bearing claim in the predesign's section 2 was re-confirmed
against a fresh clone of both repos at the SHAs above, plus a live run of
the scanner itself (read-only, output to a sandbox file -- no repo touched):

- `CENTER_BODY_RADII` hardcodes 695700 / 6378.137 / 71492 / 60268 as
  literals while `SUN_RADIUS_KM`, `EARTH_EQUATORIAL_RADIUS_KM`,
  `JUPITER_EQUATORIAL_RADIUS_KM` sit 190 lines above in the same file
  whose docstring says "Do not redefine these values locally." Confirmed.
- Live scanner run confirms the exact scores the predesign claimed:
  `SUN_RADIUS_KM` scores V2 x C3 = 6 (Tier 3, "no action required");
  `KM_PER_AU` and `CENTER_BODY_RADII` score V2 x C5 = 10 (Tier 2).
- `find_cross_file_issues` skips same-file duplicates
  (`if len(files) < 2`) and only ever compares `kind == 'constant'` --
  both blind spots confirmed by reading the function, along with the
  "shadow detection (planned separately)" comment.
- `main()`'s only nonzero exit is the invalid-directory argument.
- `test_constants_provenance.py`: exists, correct pattern, and grep
  confirms nothing in the repo calls or imports it -- only listings
  (dashboard menu ~line 227, module_atlas ROLE_MAP, the scanner's own
  MODULE_DOMAIN_MAP and report text, a comment in
  comet_visualization_shells.py line 695).
- The comet accepted-residual entry with the "low user-visible impact"
  reasoning is in `data/provenance_exceptions.json` as described.
- Gallery side: `objects_config.json` carries fully-populated `features`
  dicts for Earth/Jupiter/Saturn; `resolver.py` line 130 does
  `tuple(rec.get("features") or ())`, which iterates the dict and keeps
  keys only -- the settled bug, confirmed, not re-litigated.

**Three facts surfaced this session that the predesign didn't have.** They
shape the design below, so they lead:

1. **`constants_new.py` has no named Saturn primary.** Only Sun, Earth
   (equatorial + polar), and Jupiter (equatorial + polar) exist as named
   constants. Saturn's 60268 -- and Mercury, Venus, Mars, Moon, and every
   small body -- live ONLY inside `CENTER_BODY_RADII`. "Reference the
   primaries" is therefore only possible for three bodies today. The
   de-dup design (D5) is built around this.
2. **HEAD currently carries 105 live Tier-1 findings** (idealized_orbits
   24, paleoclimate files 20, planet_visualization_utilities 7, and so
   on) -- the moving frontier of the L-078 coverage-widening track, which
   keeps pulling new files into scan scope. This changes the answer to
   "should Tier-1 > 0 exit nonzero now" (D7): flipping it on today would
   make every scanner run fail for months, which teaches the operator to
   ignore the failure -- the exact disease being cured.
3. **The Tier-2 label is itself a stale blanket claim.** The report
   hardcodes "ALL ACCEPTED RESIDUALS -- no action required" into the
   Tier-2 tier NAME and a static April 2026 note. Any NEW finding that
   lands in Tier 2 -- including `KM_PER_AU` today, or anything coverage
   widening surfaces tomorrow -- gets auto-narrated as already-reviewed by
   the report template itself. This is the "buried in tiers nobody
   reviews" thesis in its purest form: the tier's own label tells the
   reader not to look. Fixing it is folded into D7.

---

## 1. Recommendations at a glance

| # | Decision | Recommendation |
|---|----------|----------------|
| D1 | Criticality categories | Two categories for constants/dicts: MEASURED (C=5) and RELATIONAL (C=4). Ring geometry -> MEASURED. |
| D2 | How the scanner classifies | Key-name/unit-suffix vocabulary; unknown defaults UP; coverage-gap note; cosmetic gate needs content check, not just name. |
| D3 | Vulnerability ladder | Cross-checked and derived join FETCHED at V=1; merely-sourced moves 2 -> 3; RECALLED stays 4. Carries to Gemini. |
| D4 | Annotation mechanism | `# Cross-checked: <who> <date> (<ref>)` comment, same lookback as `# Source:`. Backfill April-verified sets during the build. |
| D5 | CENTER_BODY_RADII de-dup | Reference the three existing primaries; declare "dict entry IS the primary" for all other bodies. No 19-constant expansion. |
| D6 | Pinning section | `run_pinning_checks()` inside `scan_project()`; AST extraction, no imports; explicit PINNING_MAP table; loud skip if gallery repo absent. |
| D7 | Failing loud | Pinning failure: banner + nonzero exit NOW. Tier-1 > 0: banner now, nonzero exit deferred until the count first reaches 0. Kill the Tier-2 blanket label. |
| D8 | Sweep findings | Recognize inline `'source':` values; retire Option A; add magnetosphere units; un-grandfather the comet residual; defer generalized shadow detection with rationale. |
| D9 | L-158 / L-159 | Derived rung = V1 via two-factor check (`# Derived:` comment + AST confirms it's computed). L-159: define the disclosure keyword now, defer enforcement to its own pass. |
| D10 | L-160 fate | Retire `test_constants_provenance.py` entirely, including its five listing sites. Wrapper option costs more than it returns. |

Five items genuinely need Tony's call before the build -- listed in
section 4. Everything else above is recommended-and-ready.

---

## 2. The design

### D1. Criticality: two categories, and where ring geometry sits

The predesign's edge-case work already found the real boundary, and it is
not "important vs. less important" -- it is **independently measured vs.
defined as a function of something already tracked.** The design takes
that boundary literally and stops there. Two categories:

**MEASURED (C=5).** Any value that is its own catalogued fact about the
world: planet and moon radii, ring radii in km, orbital periods, masses,
`KM_PER_AU`. The test: *if this number is wrong, is the error invisible
until someone checks the source?* One consumer or fifty -- Orcus and
Jupiter are the same kind of fact, per the settled decision.

**RELATIONAL (C=4).** Values defined as a fraction or multiple of an
already-tracked base: `radius_fraction`, `belt_distance` in planetary
radii, atmosphere shells at 1.05 x R_body. These are still facts (the
inner Van Allen belt really is near 1.5 Earth radii), but their failure
mode is contained -- a wrong fraction breaks one feature; a wrong base
breaks the feature AND silently corrupts everything else scaled from it.
The base/derived distinction is structural, not a popularity count, so it
survives the rejection of consumer-count scoring.

**Ring geometry (the predesign's one open item): MEASURED, top tier.**
Jupiter's main-ring inner radius at 122,500 km is a primary catalogued
number, not a function of Jupiter's radius. Under the boundary the
edge-case analysis itself established, it can only sit with the measured
values. The argument for a middle tier is a blast-radius argument -- "a
wrong ring corrupts less than a wrong planet radius" -- and that is the
same reasoning already rejected for Orcus-vs-Jupiter. Consistency picks
the tier. (Marked for Tony's confirmation in section 4, because the
predesign explicitly reserved it as his to reshape.)

Numerically: the existing 1-5 C scale and the tier arithmetic stay
untouched. MEASURED takes the 5 slot, RELATIONAL takes 4 (display strings
keep C_PUBLIC = 4 -- sharing a weight with a different reason string is
already how the scanner works). C_INTERNAL and C_COSMETIC remain for
genuine cases. Import counting stops being the decider for constants and
dicts; the consumer count stays in the report as information (blast
radius is worth *seeing*, just not scoring).

### D2. How the scanner tells MEASURED from RELATIONAL mechanically

No hand-curated list (settled). Classification rides the codebase's own
naming conventions, which are already machine-readable:

- Key/name carries an absolute-unit suffix (`_km`, `_au`, `_kg`,
  `_days`), or the value's associated unit is absolute -> MEASURED.
- Key/name is in the relational vocabulary (`radius_fraction`,
  `*_distance`, `*_radii` when the unit is a body radius,
  `radius_multiplier`, and the small set actually used by the shell
  configs) -> RELATIONAL.
- **Unclassifiable -> defaults UP to MEASURED**, and the report carries a
  "criticality classification gap" note listing what defaulted -- the
  same pattern the scanner already uses for ROLE_MAP and domain coverage
  gaps. Fail-safe in the right direction: uncertainty inflates review
  priority instead of burying it.

**Cosmetic gate (edge case 6, taxonomic-claims-via-color).** Today a dict
is cosmetic if its NAME contains "color" or "label" -- no content
inspection. Tightened: cosmetic requires the name heuristic AND all
values type-check as cosmetic content (rgb/hex strings, label text,
positions). A "colors" dict holding numbers stops being waved through.

Honesty note, so the design doesn't overclaim: no scanner can decide that
a *key-to-color mapping* encodes a taxonomic claim (the Polymele/Leucus
case -- the value really is just an rgb string; the claim lives in which
key it's attached to). That class of error belongs to review passes
(L-157-style worksheets), not static scanning. The design documents this
as a known limitation in the scanner docstring rather than pretending
the gate catches it. What the scanner CAN do -- and will -- is list every
cosmetic-classified dict once in a report appendix, so a mis-filed dict
is at least visible to a human eye annually rather than invisible
forever.

### D3. Vulnerability recalibration (the Gemini lane)

Current ladder: FETCHED 1 / SOURCED 2 / STALE 3 / RECALLED 4. The
Arrokoth 1000x error and the Parker distance error both lived at
"sourced" -- citation present, value wrong. V=2 for merely-sourced is
calibrated too generously (settled). Proposed ladder:

| V | Status | Meaning |
|---|--------|---------|
| 1 | FETCHED | From an authoritative pipeline at runtime |
| 1 | STRUCTURAL | Computed from tracked inputs -- can't independently drift (L-158, see D9) |
| 1 | CROSS-CHECKED | Cited AND independently verified, scanner-visible annotation (D4) |
| 3 | SOURCED | Citation present, never independently checked |
| 3 | STALE | Date-sensitive content, or cross-check aged out |
| 4 | RECALLED | No citation -- training-memory risk |

Two deliberate choices inside this:

**Cross-checked lands at 1, not 2.** The reasoning: the cross-check is
the exact mechanism that caught Arrokoth -- a value that has survived
independent verification against an outside authority has earned the
floor. It also makes the steady-state arithmetic land right without
retuning tier boundaries (which would re-shuffle every existing finding):
cross-checked MEASURED = 1 x 5 = 5, resting quietly in Tier 3;
sourced-only MEASURED = 3 x 5 = 15, sitting in Tier 2 as the honest
"awaiting cross-check" review queue; recalled MEASURED = 4 x 5 = 20,
screaming in Tier 1. That is the ladder working: uncited screams, cited
waits its turn, verified rests. The alternative (cross-checked = 2)
leaves every verified fundamental parked in Tier 2 forever -- a tier that
permanently contains the same resting items stops being read, which is
the current disease with the sign flipped.

**Merely-sourced moves to 3, which moves real findings into Tier 2.**
Cited-but-never-cross-checked strings (C=4) go from score 8 (Tier 3) to
12 (Tier 2). This is intended -- Tier 2 becomes the actual work queue --
but it only reads correctly if two things land WITH it, not after:
the cross-checked annotation backfill for everything the April 2026
worksheets already verified (D4), which absorbs most of the would-be
flood back down to V=1; and the Tier-2 blanket-label removal (D7), so
the queue is labeled as a queue. **D3, D4, and the label fix are one
build unit, not three.**

The whole ladder is a calibration claim about how often "sourced" and
"wrong" coexist -- a factual question, so per the settled lane division
it goes to Gemini via the Mode 7 worksheet before the build, with the
Arrokoth/Parker precedent attached. Tony arbitrates if Gemini pushes
back on the cross-checked = FETCHED equivalence (also flagged in
section 4).

### D4. The cross-checked annotation

Form, designed to ride the existing citation machinery unchanged:

```
# Source: NASA Planetary Fact Sheet
# Cross-checked: Gemini 2026-04-15 (worksheet_earth_visualization.md)
```

- Same comment grammar, same lookback window as `# Source:` -- one new
  regex, no new positional rules to learn.
- The parenthetical reference to the worksheet/handoff is REQUIRED. A
  cross-check claim is a provenance claim like any other; the ref is what
  makes it auditable rather than a magic word that lowers a score. An
  annotation without a ref should score as SOURCED, not CROSS-CHECKED --
  the mechanism must not become a new way to cite-to-clear.
- This is exactly what L-157's Gemini pass writes back when it completes,
  closing the "recorded in scattered handoffs, invisible to the scanner"
  loop.
- **Backfill is in the build's scope.** Stages 1-5 in the scanner's own
  audit-history docstring name what Gemini verified in April 2026 (shell
  files, info_dictionary, star_notes, asteroid_belt, and the
  constants_new fundamentals). Transcribing those confirmations into
  annotations is role 3 of the Review-Repair Protocol -- mechanical
  insertion of already-performed verification, with the worksheet docs as
  the source of truth for what qualifies. Nothing gets annotated that a
  worksheet doesn't cover.

Optional future nit, noted not designed: a "cross-check age" check
(annotation older than N years -> STALE) using the date field. The field
format supports it from day one; nothing builds it now.

### D5. CENTER_BODY_RADII de-duplication

Constrained by fact 1 in section 0: only Sun, Earth, and Jupiter have
named primaries. Three options considered:

1. Add named primaries for all ~19 bodies and reference them all --
   uniform, but adds ~19 constants with citation blocks to fix a
   three-value bug, and most would have exactly one consumer (the dict).
2. **Reference the three primaries that exist; declare the dict entry
   itself the primary for every other body.** RECOMMENDED.
3. Invert -- make the dict canonical and derive the named constants from
   it. Breaks the file's primaries-then-derived architecture and its
   per-constant citation layout. Rejected.

Option 2 fixes the actual bug (same number, twice, one file) everywhere
it exists -- bodies without a named primary have no duplication to fix.
The convention gets stated in the file: *"Entries reference a named
primary where one exists; for all other bodies, the CENTER_BODY_RADII
entry IS the primary source, cited inline."* The build enumerates
mechanically: for each dict entry, does a same-value module-level
constant exist in the file? Reference it; otherwise the literal stays
with its citation comment. (Earth's polar radius and Jupiter's polar
radius are named primaries with no dict entry -- untouched.)

Knock-on effects, all verified against how the code actually works:
- The referenced entries become AST Names instead of literals; the
  scanner's dict-value extraction simply stops seeing a second numeric
  claim there, which is correct -- the claim now lives once, at the cited
  primary.
- The pinning checks (D6) keep asserting the same numeric VALUES for
  those keys, so a pin failure now implicates the primary -- tightened,
  as the predesign anticipated.
- `build_pinned_values` (Option A's support table) is unaffected during
  its remaining lifetime; it reads the primaries, which don't move.

### D6. The pinning section inside the scanner (L-155 + L-160 absorbed)

**Placement and invocation.** One new function,
`run_pinning_checks(project_dir)`, sitting alongside
`find_cross_file_issues`, invoked from `scan_project()` -- so it runs on
every scan, unconditionally, with no flag and no separate entry point.
Results go three places: a new section in `PROVENANCE_AUDIT.md`, the
console summary, and the return path to `main()` for the exit code.

**Reading sources by AST, not import.** The shell modules import Plotly
and friends -- importing them inside the scanner would drag GUI
dependencies into a text tool. `build_pinned_values` already establishes
the in-file precedent: parse the source file's AST and extract the dict
literal or constant value directly. Uniform rule: the pinning section
imports nothing, parses everything. This also means the checks work in
any sandbox or relay session that has the files on disk.

**The mapping is an explicit table, not name-matching (settled).** A
module-level `PINNING_MAP` with one row per pinned value:

- what it is (human label, appears in failure output),
- where it lives in the gallery config (a key path into
  `objects_config.json`, objects addressed by name),
- where its source lives in the orrery (file + constant name, or
  file + dict path),
- the expected value is NOT stored in the table -- it is read from the
  orrery source at scan time and compared against the gallery copy.
  Drift on either side surfaces; there is no third copy to go stale.

The absorbed `constants_new.py` pins are the exception: those ARE
expected-value asserts (name -> verified number + citation ref), because
their whole purpose is catching drift in the source itself -- the
`test_constants_provenance.py` pattern, carried over intact, including
its docstring's motivating-bug history (the close_approach_data stale
copy), which moves into the new section's docstring so the institutional
memory survives the file.

**Gallery path handling.** `../tonyquintanilla.github.io/data/
objects_config.json` relative to the orrery repo root (settled). If the
path is absent -- a sandbox clone under different names, a relay session
with one repo -- the cross-repo rows SKIP, loudly: a clearly-worded
notice in both the console summary and the audit section header
("SKIPPED -- gallery repo not found at expected sibling path"), never a
silent pass. Absence does not affect the exit code; on Tony's machine
the layout is fixed, and a rename would surface as the loud skip on the
very next run, in the console he actually reads. The constants_new pins
run regardless -- they're single-repo.

**Sequencing honesty (the L-155 gate).** The predesign gates cross-repo
pinning on L-157: pinning never-cross-checked numbers and calling them
"verified" would be a false green. The design respects that without
idling the machinery: the build ships the ENGINE plus the
already-verified constants_new pins (Gemini-checked April 2026); the
shell-geometry and gallery rows are added to PINNING_MAP as part of
L-157's integration step -- adding rows to an existing table, trivial
once the engine exists. Until then the audit section lists those rows as
"staged, pending cross-check (L-157)" so the gap is visible rather than
invisible.

### D7. Failing loud -- exit codes, banners, and the Tier-2 label

Three separate things travel under "fail loud," and they get different
answers:

**Pinning failures: nonzero exit AND an unmissable console banner, from
day one.** A pin failure is a regression by definition -- a specific,
previously-verified value drifted. Exit code 2 (distinct from the
existing exit 1 for a bad directory argument -- distinct codes cost
nothing and help any future automation). But the exit code is not what
stops Tony: he runs via the VS Code Run button and reads the console, so
the banner is the actual brake -- a bordered, impossible-to-scroll-past
block naming each failed pin, both values, and "DO NOT PUSH."

**Tier-1 > 0: banner now, nonzero exit deferred.** The predesign asked
whether the pre-existing Tier-1 case should also start exiting nonzero
for consistency. Fact 2 in section 0 changes the answer: HEAD carries
105 live Tier-1 findings on the active coverage-widening frontier.
Flip the exit on today and every run fails for months -- and a red light
that is always red trains the operator to drive through it, which is
normalization of deviance built directly into the tool. Recommended:
the console gets a prominent Tier-1 banner now ("105 Tier-1 findings --
push gate NOT met"), and the nonzero exit is wired but switched on as a
one-line change the first time the count reaches 0 -- recorded as its
own small ledger item so the flip doesn't float. (A baseline-ratchet
file -- fail only if the count EXCEEDS last run -- was considered and
set aside: it adds a state file to maintain for a problem the banner
plus the eventual hard gate already covers. Noted in case Tony prefers
it; section 4.)

**The Tier-2 label lie (fact 3).** Tier names stop asserting per-finding
status. "ALL ACCEPTED RESIDUALS" comes out of the tier label and the
static note; tiers get score-band names only ("Tier 2 (10-15): REVIEW").
Accepted-residual status is per-finding information that already lives
in the exceptions file and the Accepted Residuals block -- the report
marks accepted findings individually instead of blessing whole tiers.
This must land with D3 (the recalibration repopulates Tier 2 with
genuinely-open items; the blanket label would mislabel every one of
them on arrival).

### D8. The five comprehensive-sweep findings, resolved

1. **Inline `'source':` dict values (the scanner's own named,
   never-done fix): DO IT in this build.** Recognize `'source': '...'`
   inside a dict unit's interior as a citation for that unit. Then
   delete the corresponding accepted-residual entries
   (spacecraft_encounters lines 235/266) -- the exceptions file SHRINKS,
   which is the direction it should move.
2. **Duplicate-detector blind spots: resolved by division of labor, and
   honestly bounded.** The same-file blind spot's one known instance is
   fixed structurally by D5. The dict-kind blind spot is covered for
   every value that matters by the explicit PINNING_MAP (which is
   precisely a curated dict-vs-source comparison, done right).
   Generalized shadow detection -- discovering UNKNOWN renamed copies --
   stays unbuilt: DEFERRED to a backlog ledger item with the rationale
   stated (discovery-class tool, lower yield now that the known copies
   are pinned; the April motivating case would today be caught by two
   independent mechanisms). Deferral with a written reason, not silence.
3. **Unit vocabulary: add magnetosphere units** -- `nT`, `Gauss`,
   `Tesla` (spelled forms; bare single letters like `T` and `G` are
   false-positive factories), and the underscore radius notation
   `R_J` / `R_M` / `R_E` / `R_S` as word-bounded tokens, plus
   "Jupiter radii"-style phrases. Discipline from the field notes
   applies: every vocabulary extension has historically surfaced hidden
   findings (star_notes precedent), so the build step includes a
   before/after audit diff, reviewed line by line, not trusted via the
   summary count. Sequenced immediately before L-157 so newly-visible
   magnetosphere claims land straight into the worksheet instead of
   sitting as fresh Tier-1 noise.
4. **Comet accepted residual: un-grandfather it.** Delete the exception
   entry; let `COMET_NUCLEUS_SIZES` / `COMET_FEATURE_THRESHOLDS`
   re-score under D1 (nucleus sizes are measured values -> C=5; they
   will surface in Tier 1 or 2 depending on citations). They join
   L-157's worksheet scope or a small follow-up comet worksheet --
   Tony's sequencing call, low stakes either way.
5. **Option A (pinned-value cross-reference for strings): RETIRE** when
   D4 lands. Its job -- inferring sourcedness by matching raw numbers
   against constants_new values -- is what the explicit annotation now
   does without the coincidental-number fragility its own comments
   admit ("rarely fires... insufficient"). One heuristic removed, one
   scanner easier to reason about. `build_pinned_values` goes with it
   (the pinning section reads sources its own way, per D6).

### D9. L-158 and L-159

**L-158, the derived rung: STRUCTURAL = V1, earned by two factors.** A
value qualifies when (a) a `# Derived:` comment declares the intent --
the form constants_new.py already uses -- AND (b) the AST confirms the
assignment is an expression over Names referencing tracked in-file
constants, not a literal. Either factor alone is insufficient, and the
mismatch case is itself a finding: a `# Derived:` comment sitting over a
hardcoded literal claims a structural safety the value doesn't have --
the same failure class as citing over recalled data, caught for free.
Under this test, constants_new.py's derived section qualifies wholesale
only if every entry passes the AST check -- the build VERIFIES that
rather than assuming it (the section's own header says "Do not hardcode
these values"; the check makes the header enforceable).

**L-159, disclosed approximations: define the convention now, defer
enforcement.** The predesign correctly calls this the least-formed item.
What this design fixes in place: the annotation form --
`# Illustrative:` (or `# Approximate:`) at the value, stating what is
stylized and why -- so new code (and the known cases: Mercury's flaring
parameter, the shared bow-shock eccentricity) starts carrying the marker
immediately, and the Envelope-of-the-Unknowable principle has a
scanner-visible footprint. What stays open, in its own future design
pass: the ENFORCEMENT check (does the rendered hover actually disclose
what the comment discloses) -- that requires tracing comment-to-hover
linkage, which is genuinely hard and shouldn't be rushed into this
build. L-159 stays OPEN, narrowed to the enforcement question.

### D10. test_constants_provenance.py: retire

Recommended over the thin wrapper. The wrapper preserves exactly the
thing being cured -- a second, separately-triggered entry point -- for a
use case ("run just the pins") that the evidence says has occurred zero
times in three months, and which `provenance_scanner.py`'s normal run
now covers anyway. Retirement is complete or it isn't: the file, the
dashboard menu entry (~line 227), the ROLE_MAP entry in module_atlas.py,
the MODULE_DOMAIN_MAP entry and report mention inside the scanner, and
the comment reference in comet_visualization_shells.py line 695 (reworded
to point at the scanner's pinning section). The docstring's
institutional memory -- the motivating bug and the April verification
history -- migrates into the new pinning section's docstring per D6.
Five listing sites, enumerated above from grep, so nothing points at a
dead file.

---

## 3. Build sequencing

Four phases, each independently pushable, ordered so no phase checks
against unverified ground:

**Phase 1 -- the scanner change-set.** D1+D2 (criticality categories +
classification), D3 (V ladder), D4's recognition regexes (Cross-checked,
Derived, inline 'source'), D8's unit vocabulary, D7's banners and
Tier-2 label fix, D9's two-factor structural check. One coherent edit to
provenance_scanner.py. Discipline: scanner changes are shared-CI changes
(field note) -- the phase closes with a full before/after audit diff
reviewed line by line, and the self-scan delta checked first (the
scanner scans itself; new module-level tables like PINNING_MAP will
nudge its own numbers).

**Phase 2 -- data-side cleanup.** D5 (constants_new de-dup), D4's
backfill of April-verified cross-check annotations (worksheets as source
of truth), D8's exceptions-file deletions (spacecraft_encounters, comet
entry). Ends with a fresh scan confirming the expected report shape:
verified fundamentals resting in Tier 3, the honest sourced-awaiting-
cross-check queue in Tier 2.

**Phase 3 -- the pinning engine.** D6's `run_pinning_checks` with the
constants_new pins active and the shell/gallery rows staged-pending-
L-157; D7's exit-code wiring (pinning live, Tier-1 wired-but-off); D10's
retirement of the test file and its five reference sites.

**Phase 4 -- the Gemini pass (L-157).** Worksheet drafted from the
shell-config geometry dicts (now fully visible under the extended
vocabulary), carried to Gemini by Tony, corrections integrated,
`# Cross-checked:` annotations applied, and the staged PINNING_MAP rows
activated. This phase also carries the D3 ladder itself to Gemini as a
calibration question (it can travel with the same worksheet handoff).

The gate order the predesign required is preserved: scoring (1-2) before
Gemini (4); pinning against cross-checked numbers only (3 stages, 4
activates). The settled resolver one-liner is independent of all four
phases -- it is gallery-repo, already decided, and can land whenever a
gallery build session next opens.

Suggested builders per the project's current assignments: Phases 1-3 are
bounded implementation against this document (Sonnet-class build
sessions); Phase 4 is the established Mode 7 worksheet relay.

---

## 4. Decisions for Tony (the genuine calls)

Everything below is presented one at a time, with a recommendation --
nothing else in this document needs a ruling before a build session
starts.

1. **Ring geometry in the MEASURED tier (D1).** Recommended and
   reasoned, but the predesign explicitly reserved this as yours to
   reshape. Confirm, or name the middle tier you want.
2. **Cross-checked = V1, same floor as pipeline-fetched (D3).** The
   strongest claim in the ladder. It also goes to Gemini as a factual
   calibration question, but the equivalence itself is a judgment call:
   does surviving one independent verification earn the same trust as
   live-fetched data? Recommended yes, with the stale machinery as the
   backstop.
3. **Orbital period and radius share the top tier despite different
   failure shapes (predesign edge case 2).** The predesign asked for
   your explicit confirmation that "same criticality" is intended even
   though one fails as a wrong-sized sphere and the other as a
   wrong position compounding over time. Design assumes yes.
4. **Retire vs. thin wrapper for test_constants_provenance.py (D10).**
   Recommended: retire. The wrapper is available if you want a
   run-just-the-pins path badly enough to keep a second entry point
   alive against the evidence.
5. **Tier-1 exit timing (D7).** Recommended: banner now, hard exit
   flipped on when the count first reaches 0 (tracked as its own ledger
   item). Alternative if you want pressure sooner: the baseline-ratchet
   (fail only when the count goes UP), at the cost of a state file.

---

## 5. Proposed ledger updates (for Tony to paste/adjust; indexer run after)

- **L-155:** status PENDING-GATE -> note the design is settled here
  (engine in Phase 3, cross-repo rows activate with L-157). Gap narrows
  to "build per DESIGN_HANDOFF_provenance_scoring_and_pinning.md."
- **L-156:** gap list (a)-(e) resolved per D1-D8; status stays OPEN
  until the build lands, gap narrows to "build Phases 1-2."
- **L-157:** unchanged in substance; gains the D3-ladder calibration
  question and the magnetosphere-vocabulary sequencing note as scope
  additions.
- **L-158:** design settled (D9, two-factor STRUCTURAL rung); gap
  narrows to build.
- **L-159:** stays OPEN, narrowed: annotation convention settled
  (`# Illustrative:`), enforcement check deferred to its own design
  pass.
- **L-160:** recommendation recorded (retire, five reference sites
  enumerated); awaiting Tony's call #4.
- **NEW item:** flip Tier-1 nonzero exit on when count first reaches 0
  (D7) -- small, deliberately captured so it doesn't float.
- **NEW backlog item:** generalized shadow detection, deferred with
  rationale (D8.2).

---

## 6. Decided vs. still open

| Item | State |
|------|-------|
| Ring geometry tier | Recommended MEASURED -- Tony confirms (call 1) |
| Criticality categories + mechanics | Decided (D1, D2) |
| V ladder shape | Decided pending Gemini calibration + call 2 |
| Annotation form + backfill scope | Decided (D4) |
| CENTER_BODY_RADII de-dup approach | Decided (D5) |
| Pinning engine placement, mapping, path handling | Decided (D6) |
| Pinning exit code + banner | Decided (D7) |
| Tier-1 exit timing | Recommended deferred-flip -- Tony confirms (call 5) |
| Tier-2 label fix | Decided (D7) |
| Sweep findings 1-5 | Decided (D8) |
| L-158 semantics | Decided (D9) |
| L-159 | Convention decided; enforcement deliberately open |
| test file fate | Recommended retire -- Tony confirms (call 4) |
| Period-vs-radius same tier | Assumed yes -- Tony confirms (call 3) |

---

*Design session written July 2026 with Anthropic's Claude Fable 5.
Zero code written or proposed as diffs; both repos read-only throughout.*
