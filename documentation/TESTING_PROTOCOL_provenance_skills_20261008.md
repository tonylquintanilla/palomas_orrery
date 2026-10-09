<!-- Doc-Kind: hand | How to test the split provenance skills, and what checks a citation's location record today, measured 2026-10-08 (L-418). -->
# Testing protocol: the provenance skills after the split (L-418)

Built on orrery c921ef84bc3569b1d70e6a66ccee7b98e94c9958 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), with
patch_L418_3 run on Tony's machine and not yet pushed. Written
2026-10-08 with Anthropic's Claude Opus 5.5. Every count below was
measured on that date, not recalled.

## Read this first

- *Part A tests that the two skills load and fire. Part B is your
  question: what checks that a citation's location record is there,
  correct and not broken.*
- *Short answer to B: the scanner does not check it. It checks that a
  citation is near a number, not where the citation points.*
- *One check runs today, and it is report-only: the worksheet checker
  confirms that a worksheet named in a cross-check annotation exists.*
- *Nothing checks that a link still opens, or that the page it opens
  says the number. Section B4 proposes what could.*

## Part A -- the skills load and fire

Run each in a fresh session. Each step says what passing looks like.

A1. **The loaded versions.** Ask the session to read the version line
of each loaded skill. Pass: provenance-discipline 2.27,
provenance-cross-check 1.0, ledger-and-session-records 1.18.
*Status: passed on 2026-10-08, in the build session itself, after the
install. All three files and the three reference files were listed.*

A2. **The reference files arrived.** Ask the session to list both skill
folders. Pass: provenance-discipline has `references/figures.md` and
`references/field-notes.md`; provenance-cross-check has
`references/worksheets.md`. *Status: passed on 2026-10-08.*

A3. **The figures pointer fires.** Give the session a figures task, for
example: "Add a derived row to constants_new.py for X, with its
`# Figures:` line." Pass: before writing the line, it says it opened
`references/figures.md`, and its line follows Rule 1's forms. Fail: it
writes the line without opening the file. This is the only test of
whether the pointer works, so ask it plainly afterwards.

A4. **The cross-check skill fires on its own.** Ask for a worksheet
prompt for another model, for example: "Prepare a citation-check prompt
for GPT on three Sun rows." Pass: provenance-cross-check loads; the
prompt states the table schema, the verdict words, bare URLs in a code
block, a pre-flight fetch and a model-and-tier header; and the session
says it opened `references/worksheets.md`. Fail: only
provenance-discipline loads.

A5. **The cross-check skill stays quiet when it should.** Ask for an
ordinary citation edit with no relay, for example: "Add the Source line
for X." Pass: provenance-discipline loads and provenance-cross-check
does not. A skill that loads every time costs the reading the split
was meant to save.

A6. **The read plan is followed.** Ask the session to read
provenance-discipline whole. Pass: it reads the parts the plan at the
top names, in order, and says so. Fail: it reads once and works from
part of the file.

A7. **The maintenance run gates it.** Run orrery_maintenance_run.py.
Pass: "Skill headers" reports 12 skills and no problems. That run
checks the read plans, the reference files, the contents lists and the
annotation examples, now including those in reference files.

## Part B -- the citation's location record

### B1. What a location record is, in this project

A measured row in `constants_new.py` carries up to five lines that
together say where its number came from:

- `# Source:` -- the paper or page, with its authors and title.
- `# Access:` -- how it was reached: the URL, the access word (open
  full text, abstract), and the date.
- `# Read:` -- where in the document the number is (page, table), the
  date, and who read it.
- `# Cross-checked:` -- a model's check, naming the worksheet file that
  holds it.
- A record file in `documentation/`, named on a `# Read:` line, where
  a long read is written up.

"Broken or missing" can mean four different things, and each needs a
different check:

1. The line is missing.
2. The line names a file in the repo that is not there.
3. The line names a web address that no longer opens.
4. The address opens, but the page does not say the number.

### B2. What checks each of the four today

| Failure | Checked by | Gates the push? |
|---|---|---|
| 1. `# Source:` missing near a number | provenance_scanner.py (Tier-1) | Yes, on the active build path |
| 1. `# Source:` missing on a row marked V_SOURCED | test_status_lines.py, rule 4 | Yes |
| 1. `# Access:` missing | nothing | -- |
| 1. `# Read:` missing on a drawn row | written in the skill; not yet built as a check | -- |
| 2. Worksheet named in `# Cross-checked:` missing | worksheet_checker.py, layer L0 | No, report-only |
| 2. Record file named in `# Read:` missing | nothing | -- |
| 3. A web address no longer opens | nothing | -- |
| 4. The page does not say the number | nothing automatic; only a person or a model reading it | -- |

### B3. Measured today (orrery c921ef84)

- 61 rows in `constants_new.py` are marked measured V_SOURCED or
  V_CROSS_CHECKED.
- 20 of them carry no `# Access:` line. Among them: KM_PER_AU,
  PARSEC_TO_AU, SUN_RADIUS_KM, EARTH_EQUATORIAL_RADIUS_KM,
  EARTH_POLAR_RADIUS_KM, EARTH_MEAN_RADIUS_KM, EARTH_INNER_CORE_KM,
  EARTH_OUTER_CORE_KM. Several are defined constants (the IAU's AU and
  nominal solar radius), where a page to open may matter less. No rule
  yet says every sourced row must carry one.
- 4 of them carry no `# Read:` line.
- 17 record files are named in the comments; all 17 exist.
- 130 `# Cross-checked:` lines name 21 worksheets; all 21 exist.
- 40 different web addresses appear in `constants_new.py`. None has
  been tested for whether it still opens.
- This covers `constants_new.py` only. The gallery's served `source`
  and `info_url` fields, in `data/objects_config.json`, are in the other
  repository and were not measured.

### B4. What could be built (for your decision, not built)

Three levels, cheapest first. Each fits Extend a Boundary Before Adding
a Path: the first two are new rules in a checker the maintenance run
already has (test_status_lines.py), not a new tool.

1. **Every named file exists** -- a record file on a `# Read:` line, a
   worksheet in a `# Cross-checked:` line. Fails the run, names the
   row and the file. Runs anywhere, no internet. Today it would pass.
2. **Every sourced row carries an access record** -- a V_SOURCED or
   V_CROSS_CHECKED row with no `# Access:` line, or one with no URL or
   DOI and no date. First it reports the 20 by name without failing;
   it fails only after you rule which rows must carry one (for example,
   whether a defined constant is excused).
3. **Every web address still opens** -- a link check that visits each
   address and reports the ones that fail or have moved. It needs the
   internet, so it runs on your machine, not in the maintenance run
   and not in a Claude sandbox, where most sites are blocked. Report
   only, run now and then, because a site being down for an hour is
   not a broken citation.

None of the three can catch failure 4. That stays with the `# Read:`
line and the exhibit rule (a quotation and a locator, in
provenance-cross-check): someone opens the page and finds the number.
A tool can only tell you which reads are missing or stale.

## Tony-actions

- **(decide)** Which of B4's three to build, if any. Recommended: 1
  and 2 together in one session (2 report-only at first); 3 later, as
  its own small tool.
- **(do)** Part A in the next fresh session: A3 to A6. A1, A2 and A7
  are already shown, or run with the maintenance run.

Written October 2026 with Anthropic's Claude Opus 5.5.
