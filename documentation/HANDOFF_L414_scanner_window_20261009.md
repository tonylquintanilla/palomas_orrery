<!-- Doc-Kind: hand | Session record for the L-414 build: the provenance scanner reads a row's own comment run, names declared rows, and prints the gate-path figure by name; provenance-discipline 2.28, protocol v3.87. -->
# Handoff: L-414 (the scanner's window), the build

Built on orrery aa46bb102a351984ba800cbfbd0d801853110b9f at
https://github.com/tonylquintanilla/palomas_orrery (branch main,
"L418_5 testing close"). Gallery at 5ec4739b at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, not
touched. Pushed at: Tony's push after his run of the patch; the next
session reads it from `git ls-remote`.

- Type: BUILD. One patch, `patch_L414_1_scanner_window_20261009.py`.
- Companion: `HANDOFF_L414_scanner_window_brief_20261009.md`, the
  brief this session built from (written by the Fable 5.1
  coordination session of October 9). That brief is superseded as a
  plan by this record; it stays the record of what was asked.
- Skills loaded and read back: provenance-discipline 2.27 (all five
  parts of its read plan, and its field-notes reference file),
  safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.18. All four matched the manifest.
  The installed provenance-cross-check 1.0 folder held its reference
  file; it was not loaded, because nothing here fired it.
- Written October 9, 2026 with Anthropic's Claude Opus 5.5. Tony was
  away from his machine; everything below was built and tested on
  throwaway copies of the repo, and nothing has run on his machine yet.

## Read this first

- *A constants_new.py row is now read through its own comment block.
  The three faults on L-414 were one mechanism, and that mechanism is
  what changed.*
- *The push gate's number now exists: Tier-1 on what leaves the
  orrery, named one by one. At aa46bb1 it was 4, all four the
  scanner's own faults. With the patch it is 0.*
- *Discovery found nothing that entered Tier-1 on the gate path, so
  the build went ahead. One row entered off it: L-427.*
- *One method call went beyond the brief and is written into 2.28: a
  declared row's reason may sit on its Status line.*

## 1. What changed, and where

**The rule.** A row in `constants_new.py` owns the comment lines
directly below its assignment, up to the first blank line or line of
code. It also owns a comment block directly above it, but only when a
blank line (or the top of the file) fences that block off from the
code before it. A block between two packed rows belongs to the row
above, because this file writes citations below. Nothing is read across
a blank line.

- `provenance_scanner.py`: `row_comment_indices()` / `row_comment_run()`
  hold the rule. Constant and dict units in `ROW_CONVENTION_FILES`
  (just `constants_new.py`) take their context, their cross-check
  annotations and their declared status from it.
  `constant_has_own_citation()`, the shadow detector's predicate, reads
  the same run. Other modules and all display strings keep their
  window.
- A row whose run says `# Status: declared` (or `declared pending`)
  and gives a reason is `V_DECLARED`: unscored, never a finding, and
  listed under **Declared Rows** in the audit. The reason is a
  `# Declared:` line or the words after `--` on the Status line. A
  bare ledger handle is not a reason; such a row is scored normally
  and listed as reasonless.
- **The gate path**: read from `data/constants_export.json` (its
  rows) and `data/objects_export.json` (its objects, mapped to their
  entries in `celestial_objects.py`). The audit gains a **Gate Path**
  section; the console's last block is now the GATE PATH line, printed
  on every run, naming each failing row, with what was examined. An
  export it cannot read prints UNKNOWN, never 0. An exported typed row
  the scanner did not score is named as a blind spot.
- `provenance_history.py`: each run record gains `gate_tier1`, the
  gate-path findings by name. The delta names what entered and what
  left, compared as a multiset; the Run History table gains a Gate T1
  column. Records from before this patch read as "not comparable",
  never as zero.
- `test_row_run.py` (new): 16 pins, run by the maintenance run as
  "Scanner row run (L-414)". 15 of the 16 fail against the scanner at
  aa46bb1; the one that passes there pins what was deliberately left
  alone (other modules keep their window).
- `orrery_maintenance_run.py`: the new checker row; the scanner's
  verdict hint now reads "GATE PATH:". Its docstring's counts were
  stale and are corrected in passing: eight generators (it said
  seven), twenty gating checkers before this patch (it said eighteen),
  twenty-one with it.
- provenance-discipline 2.28: Scanner Mechanics (four bullets: the
  row run, the window elsewhere, declared rows, the gate-path figure),
  The Goal State (where the path is read from), a note in The Status
  Line on what the scanner now reads, a parenthesis in A Breadcrumb
  Must Not Cite, and the two measurements as a field note. The v2.25
  entry moved to `documentation/SKILL_HISTORIES.md`. The read plan is
  rewritten by `skills_index.py` when the patch runs.
- `PROJECT_INSTRUCTIONS.md` v3.87; v3.84 moved to
  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` PART 1. The manifest
  row comes from `skills_index.py`.

## 2. Discovery, by name

Run on a throwaway clone of aa46bb1, the scanner as it was and then
with the fix.

- **Left Tier-1 (4):** EARTH_MEAN_RADIUS_KM (cited now; its Source sits
  16 lines down); EARTH_SOLAR_WIND_PRESSURE_NPA, EARTH_SOLAR_WIND_BZ_NT,
  EARTH_SOLAR_WIND_SPEED_KM_S (declared pending, L-314).
- **Entered Tier-1 (1), off the gate path:** CENTER_BODY_RADII. Its
  one typed number is Planet 9's 24,000 km, noted "Model estimate
  (Batygin & Brown; 5-10 M_Earth assumption)", with no year and no
  Source line. It had been credited by ARROKOTH_RADIUS_KM's Source
  across a blank line. Not exported. L-427.
- **Lost neighbour credit, Tier 4 (2):** DEFAULT_MARKER_SIZE,
  CENTER_MARKER_SIZE. Rendering settings, which need no source; they
  had been "cited" by the light-year row's Source line. L-372 already
  moves them to the drawing code. (A first draft of this patch filed
  them under L-427 as if they needed sourcing; Tony's question caught
  it before the run.)
- **Now DECLARED (19):** S_PER_HOUR, ARCSEC_PER_DEG, M3_PER_KM3 and
  INNER_CORONA_RADII (reason on the Status line);
  EARTH_POLE_RA_J2000_DEG, EARTH_POLE_DEC_J2000_DEG,
  EARTH_OBLIQUITY_J2000_ARCSEC, GALACTIC_NORTH_POLE_RA_J2000_DEG,
  GALACTIC_NORTH_POLE_DEC_J2000_ARCSEC, EARTH_LEO_LOWER_ALTITUDE_KM,
  the three solar-wind rows, EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG,
  EARTH_BOW_SHOCK_CUT_ANGLE_DEG, OUTER_CORONA_RADII,
  DE430_TERRESTRIAL_POSITION_PLACE_KM,
  DE430_JUPITER_SATURN_POSITION_PLACE_KM,
  DE430_URANUS_NEPTUNE_PLUTO_POSITION_PLACE_KM (a `# Declared:` line).
  Sixteen of them had scored Tier 2 as cited; they leave the findings.
- **The scanner's self-scan:** one new Tier-3 finding,
  `provenance_scanner.py` V_DECLARED, the new constant (the field note
  on the scanner scanning itself).
- **Totals:** findings 1,099 -> 1,081; Tier-1 296 -> 293; Tier-2 675 ->
  659; Tier-3 123 -> 124; Tier-4 5 -> 5.
- **Gate path:** 4 -> 0. Examined 80 of 105 exported rows; the other
  25 are computed from other rows and named in the audit; 11 served
  objects, whose descriptions hold no number-and-unit claim the scanner
  scores.
- **Shadow detector:** cited constants 99 -> 94 (DEFAULT_MARKER_SIZE,
  EARTH_LEO_LOWER_ALTITUDE_KM, EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG,
  M3_PER_KM3, OUTER_CORONA_RADII had been read through a neighbour or
  across a blank line); pinned values 147 -> 145. Shadow constants
  found: 0 before, 0 after. Cross-check issues 0 and 0; orphan
  annotations 4 and 4.

## 3. The planted faults

Each on a copy of `constants_new.py`, scored by the scanner at aa46bb1
and by the fixed one:

| Case | aa46bb1 | fixed |
|------|---------|-------|
| EARTH_THERMOPAUSE_ALTITUDE_KM, Source lines removed (F1) -- expect Tier-1 | FAIL, Tier 2 "Cited" | PASS, Tier 1 |
| EARTH_MEAN_RADIUS_KM, its Source 16 lines down -- expect cited | FAIL, Tier 1 | PASS, Tier 2 "Cited" |
| The three solar-wind rows -- expect DECLARED | FAIL, Tier 1 x3 | PASS, "Declared pending (L-314)" x3 |
| EARTH_STRATOPAUSE_ALTITUDE_KM, own Source and Ref removed, neighbours untouched -- expect Tier-1 | FAIL, Tier 2 "Cited" | PASS, Tier 1 |

The same four shapes are pinned synthetically in `test_row_run.py`, so
the pins survive edits to the rows that motivated them.

## 4. The method calls, and which cases the pins cover

- **A reason on the Status line counts.** The brief named only a
  `# Declared:` line. Read that way, M3_PER_KM3 (exported; "-- an
  exact unit conversion, 1 km^3 = 1e9 m^3") would have been Tier-1 on
  the gate path. The skill's own Status Line example writes the reason
  there, so 2.28 accepts either. A bare handle is not a reason.
- **Section-header citations.** The window's look-back existed "for
  section-header citations". Under the row run a header covers only
  the row it touches, which is The Status Line's per-row rule. No
  recognition pin covered a header over several rows. The 27 pins of
  `test_provenance_1d.py` all hold; its four contiguity pins (below
  counts, above counts, a blank ends the run below, preceding code ends
  the run above) are the row run's rule for single rows. The 20
  citation-inheritance, 19 cross-check, 25 constants-provenance and
  extractor pins also hold, and the status-line checker passes.
- **The gate path is the exports.** It settles L-184's open Task 2b
  (where the path is defined) by The Gate Binds at EXPORT. L-184
  carries a note proposing it closes with L-414.
- **Scope.** Display strings and other modules were left alone; the
  extractor's 60-line window and its pins are untouched.

## 5. Tests run (agentic-pre-test, on throwaway copies)

All on fresh clones of aa46bb1; the deliverable was never edited by a
test.

- py_compile: every changed or new .py file, and the patch script.
- The patch on a clean clone: every edit "ok", "patch applied", 12
  files written, skills_index.py wrote the read plan and the manifest
  row and its --check passed ("OK: 12 skills parsed"). The result was
  byte-identical to the tree the patch was built from.
- A second run refused ("test_row_run.py already exists, so this patch
  has already run. NOTHING was written."); no file changed.
- A CRLF working copy (all ten edited files converted): the same
  result, each file noted as written LF, byte-identical again.
- orrery_maintenance_run.py on the patched clone, with the gallery
  cloned beside it at 5ec4739b, under xvfb: "21 of 21 gating checkers
  passed"; Scanner row run (L-414) "16 of 16 pins hold"; Scanner
  recognition 1d/1e "27 of 27"; Provenance scanner "0 TIER-1 -- the
  push gate holds". (The sandbox first lacked matplotlib and
  customtkinter for Reset completeness; with requirements.txt
  installed it passed. Not related to this patch.)
- F1 planted on that patched copy, scanner run: "GATE PATH: 1 TIER-1
  -- the push gate FAILS on: constants_new.py
  EARTH_THERMOPAUSE_ALTITUDE_KM", and the history line "gate path
  ENTERED Tier-1" naming it.
- data/constants_export.json removed on a copy: "GATE PATH: UNKNOWN",
  with the reason; no number printed.
- test_row_run.py beside the scanner at aa46bb1: 15 of 16 fail, as
  intended.

## 6. Tony-actions, all of them

- Tony-action (do): save `patch_L414_1_scanner_window_20261009.py` in
  the orrery folder and click Run in VS Code.
- Tony-action (do): run `orrery_maintenance_run.py`. Expect "21 of 21
  gating checkers passed" and the scanner's line "GATE PATH: 0 TIER-1
  -- the push gate holds". The run history will say the previous run
  predates L-414; that is expected once.
- Tony-action (do): move the patch script into `documentation/`;
  commit and push.
- Tony-action (do): make a ZIP of `skills/provenance-discipline`
  (right-click, Send to, Compressed (zipped) folder), keep it out of
  the repo folder, and install it in Settings, under Skills, replacing
  the installed one.
- Tony-action (do): replace the Project's instructions with
  `PROJECT_INSTRUCTIONS.md` (now v3.87).
- Tony-action (decide), carried, not new: L-425 (citation location
  checks).

## 7. The obligation that travels

A reinstall during a session may not be visible to it. The next
session confirms its loaded provenance-discipline reads 2.28 before any
provenance work, and that its folder still holds both reference files.
As a data point: this session's own listing showed the installed copy
at 2.27, byte-identical to the repo's skills/ folder at aa46bb1.

## 8. Next session

- The typed facts, L-421 (the inner Oort cloud, then the check), as
  Tony confirmed. Its new sourced rows are now gated by a scanner that
  catches a removed Source line and prints the gate by name.
- Not this session's, and not chased: L-427 (rows a neighbour had been
  crediting); L-425 (citation location checks) and the worksheet
  checker items L-424 and L-426.

Session record written October 9, 2026 with Anthropic's Claude Opus 5.5.
