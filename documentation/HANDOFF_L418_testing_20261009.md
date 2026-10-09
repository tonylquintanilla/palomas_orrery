<!-- Doc-Kind: hand | Session record: the provenance skills tested after the split (L-418 closed), the planted-fault run for citation location checks (L-425), and the quote idea measured, 2026-10-08 to 2026-10-09. -->
# Handoff: the provenance skills tested, and the citation checks measured

Tests run on orrery 1e309533118120df942a484aafa8c7c66902aaf3, and the
records patch built on orrery 08f037590a9f0b90ebebf504c6975c8a82519790
(Tony's "cleanup" commit, records only), at
https://github.com/tonylquintanilla/palomas_orrery (branch main). Gallery
b50f8bd675064714222ce996fef8194301fe7bc7 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read only
(`data/objects_config.json` for the rooms' rows,
`data/cache_swap_log.jsonl` for the page's signal); not changed.

- Type: TESTING, records-only at the close. Every run was on a
  throwaway clone in the sandbox; no deliverable file was edited.
- Companion to `documentation/HANDOFF_L418_testing_session_brief_20261008.md`
  (the brief this session followed),
  `documentation/TESTING_PROTOCOL_provenance_skills_20261008.md` (the
  protocol) and `documentation/HANDOFF_L418_split_build_20261008.md`.
- Skills loaded, each read back against the manifest and the repo
  byte for byte: provenance-discipline 2.27, provenance-cross-check
  1.0, ledger-and-session-records 1.18, safe-file-editing 1.13,
  agentic-pre-test 1.3. Both new skill folders were listed:
  provenance-discipline has `references/figures.md` and
  `references/field-notes.md`; provenance-cross-check has
  `references/worksheets.md`. Tests A1 and A2, repeated in a fresh
  session: pass.
- October 8 to 9, 2026, with Anthropic's Claude Opus 5.5.

## Read this first

- *The four skill tests passed. L-418 (splitting provenance-discipline)
  closes.*
- *The planted-fault run: the four silent faults were silent, as the
  protocol's table said. The three it said were caught were caught
  differently, and one new path was found.*
- *A defect in the worksheet checker was found by the run: it compares
  very small numbers as equal. L-426 (the checker's small-number
  comparison).*
- *L-425 (citation location checks) is now Tony's decision, on these
  results.*

## Part 1 -- the skill tests A3 to A6

| Test | Result | Evidence |
|---|---|---|
| A6, the read plan | PASS | `skills/provenance-discipline/SKILL.md` read from the throwaway with the file reader. The plan named five parts, lines 1-303, 304-601, 602-904, 905-1201, 1202-1255; all five were read, in that order, none cut. |
| A5, the cross-check skill stays quiet | PASS | Every measured row already has a `# Source:` line, so the nearest ordinary citation edit was used: an `# Access:` line on SUN_RADIUS_KM, after opening the arXiv full text of Prsa et al. (2016), Table 1 (6.957 x 10^8 m). provenance-discipline governed it; provenance-cross-check was not opened. |
| A3, the figures pointer | PASS | `references/figures.md` was read whole (its own three-part plan) before any line was written, and it changed the answer: SOLAR_RADIUS_AU is a conversion of SUN_RADIUS_KM, so it takes `# Conversion: of SUN_RADIUS_KM`, not a `# Figures:` line (Rule 1, Rule 3). On the throwaway, test_derived_figures.py's one UNMARKED CONVERSION (that row) cleared, 19 conversions checked, none wrong. |
| A4, the cross-check skill fires | PASS | Asked for a GPT prompt on three Sun rows (TERMINATION_SHOCK_AU, HELIOPAUSE_AU, HELMET_CUSP_LOW_RADII), provenance-cross-check 1.0 loaded and `references/worksheets.md` was opened first. The prompt carried the anchor, the skills to read back, the table schema, the verdict words, bare addresses in a code block, a pre-flight fetch, a model-and-tier header and the quote-and-locator rule. A test artifact; not dispatched, not kept. |

The limit on these passes: the session knew the expected answers from
the brief. The tests show the files load and point to the right
places; they cannot show what an unprimed session would do. A3 is the
strongest, because opening the reference file changed the line.

## Part 2 -- the planted-fault run

Baseline: orrery_maintenance_run.py on an unplanted clone, then each
checker alone. It matched Tony's run of 2026-10-08 on every shared line
(296 Tier-1, 74 of 110 routed, 105 status lines well formed). Three
sandbox-only differences, the same in every run: Reset completeness and
Earth pole of date fail (no tkinter here), and the exact-rows check
reads the orrery half only (no gallery repo). Faults planted on served
rows, each on its own row; the full run and each checker alone, then
each fault alone where attribution needed it.

| # | Row | Fault | Predicted | Observed | Checker line, verbatim | Gates? |
|---|---|---|---|---|---|---|
| F1 | EARTH_THERMOPAUSE_ALTITUDE_KM | `# Source:` removed, row V_SOURCED | scanner and test_status_lines rule 4 | test_status_lines only | `EARTH_THERMOPAUSE_ALTITUDE_KM  V_SOURCED but no '# Source:' on the row -- the rung asserts a citation that is not here` | yes |
| F2 | TERMINATION_SHOCK_AU | `# Access:` removed | nothing | nothing | silent | -- |
| F3 | HELMET_CUSP_LOW_RADII | `# Read:` record file renamed to a missing one | nothing | nothing; the broken path is copied into constants_export.json | silent | -- |
| F4 | EARTH_POLAR_RADIUS_KM | `# Cross-checked:` worksheet renamed to a missing one | worksheet_checker L0, report-only | named in WORKSHEET_CHECK.md only; the run's summary line is unchanged | `MISSING_WORKSHEET -- no such file in documentation/worksheets`; summary `74 of 110 routed, 8 clean` | no |
| F5 | EARTH_VAN_ALLEN_OUTER_BAND_LOW_L | `# Access:` address to a missing page | nothing | nothing | silent | -- |
| F6 | EARTH_MAGNETOPAUSE_SHUE_A1_RADII | `# Read:` Table 1 to Table 7 | nothing | nothing; the wrong locator is copied into constants_export.json | silent | -- |
| F7a | SUN_RADIUS_KM (served) | value 695700.0 to 696340.0 | worksheet_checker DRIFTED | constants_change_report, test_constants_provenance, test_constants_export; worksheet_checker UNCHECKED_MOVE twice | `VALUE MOVED ALONE -- no provenance change in this block`; `CENTER_BODY_RADII['Sun'] drifted to 696340.0`; `the generator cannot export the store: states 'prints 4', which would print 696340.0 as 696300`; `UNCHECKED_MOVE -- code now 696340.0, checker read 695700.0; this worksheet carries no value verdict` | first three yes; the worksheet line no |
| F7b | GRAVITATIONAL_CONSTANT_SI (not served; its worksheets say value YES) | value 6.67430e-11 to 6.67400e-11 | worksheet_checker DRIFTED | constants_change_report only | `VALUE MOVED ALONE -- no provenance change in this block` | yes |

Where observed differs from predicted:

- **F1.** The scanner does not catch a removed `# Source:` in
  constants_new.py: the row above's citation sits inside its 30-line
  look-back and is credited to this row. Shown: removing the
  stratopause row's Source and Ref lines too made both rows Tier-1
  (296 to 298). Only test_status_lines rule 4 guards, and only on rows
  whose status line declares a sourced rung. Recorded on L-414 (the
  scanner's window).
- **F4.** Report-only as predicted, but nothing a person reads in the
  run changes: that leg was already routed SEND BACK for another cause,
  so no count moves. Shown with F4 alone.
- **F7.** The table missed constants_change_report.py, which gates but
  compares against the last commit, so it guards only until the change
  is committed. DRIFTED was reached on neither row:
  - F7a: every served cross-checked row points at a worksheet that
    records only a citation verdict, so a drift prints UNCHECKED_MOVE,
    the "no value verdict" case of L-424 (the checker's one word for
    two cases), and the checker's own line says so. The summary moved
    74 to 76 and named nothing.
  - F7b: `compare()` in worksheet_checker.py rounds both numbers to
    decimal places, and at five places every number near 1e-11 is 0.
    Probe: 1e-11, 9.9e-11, 6.674e-11 and 2e-7 each "MATCH" 6.67430e-11.
    Numbers near 1e-5 still compare (7.0e-5 against 7.292115e-5 is a
    MISMATCH). Opened as L-426 (the checker's small-number comparison).
- **New, not in the table.** `# Read:` text is exported. F3's missing
  record path and F6's wrong table reach constants_export.json, and the
  export check passes, because it checks that the export matches
  constants_new.py, not that constants_new.py is right. Access lines are
  not exported, so F2 and F5 stay in the orrery.

What each proposed level of L-425 would have done with these: level 1
(every named file exists) catches F3 and F4, failing the run; level 2
(every sourced row carries an access record) catches F2; level 3 (the
link check) catches F5. Nothing proposed catches F6.

The planted copies were reset and deleted; nothing from them is
delivered.

## Part 3 -- the quote idea, measured, not built

Bound: the rows the gallery's `data/objects_config.json` points at for
the Sun room (25 constants rows) and the Earth room (50): 75 rows.

- 40 are measured. 38 carry a `# Read:` line; RADIATIVE_ZONE_AU and
  SUN_RADIUS_KM do not.
- Of the 38: 23 name a sentence, paragraph, section, page or abstract
  (quotable as text); 11 name a table, figure or equation, where the
  "quote" would be a table row, a caption or an equation
  (EARTH_BOW_SHOCK_JELINEK_EPS, EARTH_BOW_SHOCK_JELINEK_R0_RADII,
  EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII, EARTH_EQUATORIAL_RADIUS_KM,
  EARTH_INNER_CORE_KM, EARTH_OUTER_CORE_KM, EARTH_UPPER_MANTLE_KM,
  EARTH_MAGNETOPAUSE_SHUE_A6, EARTH_MAGNETOPAUSE_SHUE_A7_PER_NT,
  EARTH_MAGNETOPAUSE_SHUE_A8, EARTH_MEAN_RADIUS_KM); and 4 say "as"
  another row and would share its quote (HELMET_CUSP_HIGH_RADII,
  OORT_CLOUD_INNER_EDGE_HIGH_AU, OORT_CLOUD_OUTER_EDGE_LOW_AU,
  OORT_CLOUD_OUTER_EDGE_HIGH_AU).
- Of the 23 quotable rows, 19 carry an `# Access:` address the online
  check could open. The other four (EARTH_GEOCORONA_RADII,
  EARTH_LEO_UPPER_ALTITUDE_KM, EARTH_STRATOPAUSE_ALTITUDE_KM,
  EARTH_THERMOPAUSE_ALTITUDE_KM) carry addresses on `# Ref:` lines
  instead.
- No conversion case among the tries: each row is stored in its
  source's unit (L-386's rule), so the quote's number and the row's
  number are in the same unit.

The tries. Every quote below came through the fetch tool, which passes
the page through a small model and caps a quote at 125 characters, so
each is that model's transcription, not the page's bytes. Tony granted
the four addresses on 2026-10-09.

| Row | Address | Result | Quote, as returned |
|---|---|---|---|
| INNER_OORT_CLOUD_AU (20000 au) | arXiv 2105.12816v2, sec. 2.2 | quote found | "and the inner edge of the Oort cloud ( \lesssim 20\,000 au )" -- the paper writes the number with a typeset thin space |
| GRAVITATIONAL_INFLUENCE_PC (0.65 pc) | same paper | quote found, in the captions only | Fig. 2: "The red dotted curve indicates the Hill radius of the Sun in orbit around the Galactic center, here at about 0.65 pc." The tool found 0.65 nowhere else, including sec. 5, which the row's `# Read:` also names: a lead to check, not proof |
| OORT_CLOUD_INNER_EDGE_LOW_AU (2000 au) | science.nasa.gov, Oort Cloud Facts | quote found | "The inner edge of the Oort Cloud, however, is thought to be located between 2,000 and 5,000 AU from the Sun," |
| EARTH_VAN_ALLEN_OUTER_BAND_LOW_L (4) | par.nsf.gov copy of Li et al. (2025), sec. 1 | quote found | "the outer radiation belt which is most intense around L = 4 and 5" |
| EARTH_MAGNETOTAIL_OBSERVED_RADII (220 R_E) | NTRS 19830066648, abstract | quote found | "the magnetotail retains much of its near earth structure out to X = -220 earth radii" -- the source gives a signed coordinate |
| TERMINATION_SHOCK_AU (94.01 au) | NASA ADS abstract | site unreachable from here | ADS refuses automated fetches (robots rule). A limit of the sandbox, recorded, not worked around |

What the tries show for an offline "the quote contains the number"
check: the number's printed form varies (20\,000, 2,000), a small
number appears by accident (the 4 in "L = 4 and 5"), and a sign can
differ from the row (-220). A containment test needs the source-form
number and would still pass an invented quote that contains it.

**The design question for Tony, on L-425, not answered here:** should a
`# Quote:` line become a fourth level of citation checking; if so, does
it live beside `# Read:` in constants_new.py or in the record file a
`# Read:` line names; and is it required of new rows only, or
backfilled for the served slice? The numbers beside it: 38 served
measured rows have a locator; 23 are quotable as text, 19 of those
with an address; 11 point at a table, figure or equation. The limits
beside it: a quote can be invented as easily as a citation; only the
online check on Tony's machine, reading the page's own text, can tell
a real one; a quote written in a Claude session is a model's
transcription until that check confirms it; and stored but never
checked, a quote is a check that cannot fail. Tony reads links, not
quotes (2026-08-27); a quote would be for the tool.

## Departures from the brief

- A5 used an `# Access:` line, because no measured row lacks a
  `# Source:` line, so "add the Source line" had no real target.
- F7 was planted twice. Every served cross-checked row's worksheet is
  citation-only, so DRIFTED cannot be reached on a served row; F7b on
  GRAVITATIONAL_CONSTANT_SI, which is not served, is the one place it
  could be. Eight rows were planted instead of seven.
- F7a moved from CHROMOSPHERE_PHYSICAL_KM to SUN_RADIUS_KM, because the
  chromosphere row's only leg already matches no worksheet row.
- Part 3 tried six rows, not five: both arXiv rows were reachable
  before the other four were granted.
- The records patch was built on 08f0375, not 1e30953, because Tony's
  overnight commit moved HEAD; it changed only records, all read here.

## Also recorded

- **L-386 (the Sun's conversion rows):** A3 showed SOLAR_RADIUS_AU's
  fix on a throwaway: `# Unit: au` and `# Conversion: of SUN_RADIUS_KM`
  in place of its two `# Derived:` lines clear the UNMARKED CONVERSION
  the maintenance run prints. Not applied; this session edits no
  deliverable.
- **L-425 (citation location checks):** its earlier bullet said the
  scanner gates a missing Source line; measured, it does not in
  constants_new.py (F1). Corrected there.
- **Where We Are's length.** The page stood at 137 lines above the
  marker before this close, over the 130 cap (L-396's check, which
  would catch it, is not built). This close drops three pointers to
  closed work from Where the details are -- the galactic plane and
  the panel colour (L-420, L-027), the Fable sweep's record and the
  sweep's report -- which the ledger keeps, and ends at 128.
- **L-351 (owed to the skills' next versions):** Tony's note of
  2026-10-08 on who empties the run-record zone, quoted beside the owed
  contradiction. This patch writes nothing below the marker.

## Tony-actions (rollup)

- **(do)** Run `patch_L418_5_testing_close_20261009.py` from the orrery
  folder (VS Code, Run), then orrery_maintenance_run.py; move the patch
  into documentation/; commit and push.
- **(decide)** L-425 (citation location checks): which levels to build,
  on the results above; and the quote question, with the count.
- **(decide)** L-424 (the checker's one word for two cases): whether the
  checker prints two words. F7a is the first observation of the case
  on a served row.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
