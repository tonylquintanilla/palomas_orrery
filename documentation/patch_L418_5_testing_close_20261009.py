#!/usr/bin/env python3
"""
patch_L418_5_testing_close_20261009.py -- the close of the testing
session after the provenance split (L-418).

HOW TO RUN: save this file in the orrery folder (the one holding
LEDGER_CONSOLIDATED.md), open it in VS Code and click Run. From a
terminal: python patch_L418_5_testing_close_20261009.py. It asks nothing.

WHAT IT DOES. Records-only. Closes L-418 (splitting
provenance-discipline) on tests A3 to A6; writes the planted-fault run
and the quote count into L-425 (citation location checks), with the one
design question; adds the run's observation to L-424 (the checker's one
word for two cases), L-414 (the scanner's window) and L-386 (the Sun's
conversion rows); opens one item for the worksheet checker's
small-number comparison; quotes Tony's run-record note on L-351; stamps
the ledger; edits Where We Are by section; and writes the session's
handoff, documentation/HANDOFF_L418_testing_20261009.md -- or leaves it
as it is if the same copy is already there, and stops if a different
one is. No code and no constants change. Nothing below the run-record
marker is touched.

Every edit is anchored on lines that must match exactly once; if any
was changed first by someone else the patch stops with ANCHOR FAIL and
writes nothing. A second run refuses (it finds its own stamp in the
ledger). Undo is Discard Changes in GitHub Desktop.

SUCCESS: one "ok" line per edit, then "patch applied".

Built on orrery 08f037590a9f0b90ebebf504c6975c8a82519790 at
https://github.com/tonylquintanilla/palomas_orrery (branch main); the
tests it records ran on 1e309533118120df942a484aafa8c7c66902aaf3.
Written October 9, 2026 with Anthropic's Claude Opus 5.5.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
BASE = '08f0375'
TODAY = '2026-10-09'
LEDGER = 'LEDGER_CONSOLIDATED.md'
WWA = 'documentation/WHERE_WE_ARE.md'
HANDOFF = 'documentation/HANDOFF_L418_testing_20261009.md'
REC = '`documentation/HANDOFF_L418_testing_20261009.md`'
MARKER = '--- Your run record below this line.'
CAP = 130
DONE_STAMP = "(L-418 closed on tests A1 to A6; L-425 gains the planted-fault run\n"


class Refuse(Exception):
    pass


def read_lf(rel):
    path = ROOT / rel
    if not path.is_file():
        raise Refuse(f"ERROR: {rel} not found. Run this from the orrery folder.")
    text = path.read_bytes().decode('utf-8')
    if '\r\n' in text:
        print(f"note: {rel} was CRLF in the working copy; it is written LF")
    return text.replace('\r\n', '\n')


def edit(text, old, new, rel, label):
    n = text.count(old)
    if n != 1:
        raise Refuse(f"ANCHOR FAIL: {rel}: {label}: expected 1 match, found "
                     f"{n}.\n  anchor starts: {old[:90]!r}")
    print(f"ok  {rel:30s} {label}")
    return text.replace(old, new)


def block_span(ledger, n):
    m = re.search(r'^#### \[L-%d\][^\n]*\n' % n, ledger, re.M)
    if not m:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: item L-{n} not found.")
    nxt = re.compile(r'^(#### \[L-|## )', re.M).search(ledger, m.end())
    return m.start(), (nxt.start() if nxt else len(ledger))


def block_edit(ledger, n, old, new, label):
    a, b = block_span(ledger, n)
    blk = ledger[a:b]
    if blk.count(old) != 1:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: L-{n}: {label}: expected 1 "
                     f"match inside the item, found {blk.count(old)}.\n"
                     f"  anchor starts: {old[:90]!r}")
    print(f"ok  {LEDGER:30s} L-{n}: {label}")
    return ledger[:a] + blk.replace(old, new) + ledger[b:]


def set_meta(ledger, n, status=None, section=None):
    a, b = block_span(ledger, n)
    blk = ledger[a:b]
    pat = r'<!-- L:%d status:(\S+) upd:(\S+) section:(\S+) ' % n
    m = re.search(pat, blk)
    if not m:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: L-{n}: metadata line not found.")
    new = '<!-- L:%d status:%s upd:%s section:%s ' % (
        n, status or m.group(1), TODAY, section or m.group(3))
    blk = blk[:m.start()] + new + blk[m.end():]
    what = 'date' if not status else f'{status}, section {section}, date'
    print(f"ok  {LEDGER:30s} L-{n}: metadata -> {what}")
    return ledger[:a] + blk + ledger[b:]


# ------------------------------------------------------------------
# THE LEDGER
# ------------------------------------------------------------------

L418_GAP = """\
**Gap:** the next fresh session runs tests A3 to A6 of the testing
protocol and says what it found; then this item closes.
"""

L418_CLOSE = """\
- **2026-10-09, tests A1 to A6 pass in a fresh session** (record:
  %(rec)s, Part 1; tests on orrery 1e30953). The loaded copies read
  provenance-discipline 2.27, provenance-cross-check 1.0 and
  ledger-and-session-records 1.18, matching the manifest and the repo
  byte for byte, and both skill folders hold their reference files
  (A1, A2). A6: the read plan named five parts and all five were read
  in order with the file reader. A5: an ordinary citation edit (an
  Access line on SUN_RADIUS_KM) was governed by provenance-discipline
  alone. A3: `references/figures.md` was opened before the line was
  written, and it changed the answer -- SOLAR_RADIUS_AU takes a
  Conversion line, not a Figures line (carried to L-386). A4: a relay
  prompt for GPT loaded provenance-cross-check and opened
  `references/worksheets.md` first, and carried the schema, the
  verdict words, bare addresses, a pre-flight fetch and a model-and-tier
  header. The limit, stated in the record: the session knew the
  expected answers from the brief.
- **Loose ends, re-homed at the close.** Moving the two long procedures
  into reference files: done by this item's split at 2.27, struck. The
  four other long skills' read plans: L-351 carries them, and
  skills_index.py names them on PLAN_NOT_YET every run. The two skill
  ZIPs: deleted by Tony ("-- done", his run record), absent at 08f0375.
  L-414's 2.28: on L-414.
**Gap:** none. Closed 2026-10-09.
"""

L425_CHECKED = "  (worksheet_checker.py layer L0, report-only).\n"

L425_CORRECTED = """\
  (worksheet_checker.py layer L0, report-only).
- **Corrected 2026-10-09, by the planted-fault run below:** in
  constants_new.py the scanner does NOT catch a removed Source line
  when the row above is cited within its 30-line look-back (F1), and
  the L0 finding is named only in WORKSHEET_CHECK.md, never in the
  maintenance run's summary line (F4).
"""

L425_DECIDE = """\
  **Tony-action (decide):** which to build. Recommended: (1) and (2)
  together in one session; (3) later, as its own small tool.
**Gap:** Tony's decision above.
"""

L425_RESULTS = """\
- **2026-10-09, the planted-fault run** (record: %(rec)s, Part 2, with
  every checker's line word for word). Throwaway clone of orrery
  1e30953; a baseline run first; each fault on its own served row.
  - F1, `# Source:` removed from EARTH_THERMOPAUSE_ALTITUDE_KM
    (V_SOURCED): caught by test_status_lines.py alone, which gates. The
    scanner was silent: the stratopause row's citation, within its
    look-back, was credited to it (removing that too gave 296 to 298).
    On L-414.
  - F2, `# Access:` removed from TERMINATION_SHOCK_AU: silent.
  - F3, HELMET_CUSP_LOW_RADII's record file renamed to a missing one:
    silent, and the broken path is copied into constants_export.json.
  - F4, EARTH_POLAR_RADIUS_KM's worksheet renamed to a missing one:
    MISSING_WORKSHEET in WORKSHEET_CHECK.md, report-only; the summary
    line stayed "74 of 110 routed, 8 clean".
  - F5, EARTH_VAN_ALLEN_OUTER_BAND_LOW_L's address changed to a missing
    page: silent.
  - F6, EARTH_MAGNETOPAUSE_SHUE_A1_RADII's Read moved from Table 1 to
    Table 7: silent, and copied into constants_export.json.
  - F7a, SUN_RADIUS_KM's value moved alone: constants_change_report.py
    ("VALUE MOVED ALONE"), test_constants_provenance.py and
    test_constants_export.py fail, all gating; the worksheet checker
    printed UNCHECKED_MOVE, not DRIFTED (on L-424).
  - F7b, GRAVITATIONAL_CONSTANT_SI's value moved alone (not served; its
    worksheets say value YES): constants_change_report.py only; the
    worksheet checker saw no drift (L-%(n)d).
  - constants_change_report.py compares against the last commit, so it
    guards a moved value only until the commit.
  - Against the three levels above: (1) would have caught F3 and F4,
    failing the run; (2) F2; (3) F5. Nothing proposed catches F6.
- **2026-10-09, the quote idea measured** (record, Part 3). Bound: the
  rows the gallery's objects_config.json points at, Sun 25 and Earth
  50. 40 are measured; 38 carry a Read line (not RADIATIVE_ZONE_AU,
  SUN_RADIUS_KM). Of the 38: 23 name text (a sentence, section, page or
  abstract), 19 of them with an Access address; 11 name a table, figure
  or equation; 4 say "as" another row. Six tries, through the fetch
  tool, which passes a page through a small model and caps a quote at
  125 characters: INNER_OORT_CLOUD_AU, GRAVITATIONAL_INFLUENCE_PC,
  OORT_CLOUD_INNER_EDGE_LOW_AU, EARTH_VAN_ALLEN_OUTER_BAND_LOW_L and
  EARTH_MAGNETOTAIL_OBSERVED_RADII found; TERMINATION_SHOCK_AU
  unreachable (NASA ADS refuses automated fetches). The tries show the
  number's printed form varies (20\\,000; 2,000), a small number turns
  up by accident (L = 4 and 5) and a sign can differ (-220). For
  GRAVITATIONAL_INFLUENCE_PC the tool found 0.65 in the Fig. 2 and 3
  captions and not in sec. 5, which the Read line also names: a lead,
  not proof.
- **The quote question, for Tony, not answered here:** should a
  `# Quote:` line become a fourth level; does it live beside `# Read:`
  in constants_new.py or in the record file the Read line names; and
  is it required of new rows only, or backfilled for the served slice
  (38 rows, 23 quotable as text)? Its limits: a quote can be invented
  as easily as a citation; only the online check on Tony's machine,
  reading the page itself, can tell; a quote written in a Claude
  session is a model's transcription until then; stored and never
  checked, it is a check that cannot fail.
  **Tony-action (decide):** which of the levels to build, on the
  measured results; and the quote question, with the count. The
  recommendation above, (1) and (2) together and (3) later, stands.
**Gap:** Tony's decision above.
"""

L425_REF_OLD = "`provenance_scanner.py`; `test_status_lines.py`; `worksheet_checker.py`;\nL-418.\n"
L425_REF_NEW = ("`provenance_scanner.py`; `test_status_lines.py`; `worksheet_checker.py`;\n"
                "L-418; L-414; L-424; L-%(n)d; %(rec)s.\n")

L424_GAP = """\
**Gap:** Tony's decision above; if yes, a session builds it with a test
for each case and updates the skill's bullet to match.
"""

L424_NEW = """\
- **2026-10-09, seen on a served row** (planted-fault run, F7a; record
  %(rec)s). SUN_RADIUS_KM's value moved alone, and both its legs
  printed "UNCHECKED_MOVE -- code now 696340.0, checker read 695700.0;
  this worksheet carries no value verdict": the no-value-verdict case,
  named in the line. Every served row's cross-check worksheet records
  only a citation verdict, so this is the case a drift on a served row
  reaches. The summary moved from 74 to 76 routed and named nothing.
- The session that builds this item opens `compare()`, the same
  function as L-%(n)d (the checker's small-number comparison); carry
  both.
**Gap:** Tony's decision above; if yes, a session builds it with a test
for each case and updates the skill's bullet to match.
"""

L414_GAP = "**Gap:** the fix, by provenance-discipline's method;"
L414_NEW = """\
- **2026-10-09, the window's other face** (planted-fault run, F1;
  record %(rec)s). With EARTH_THERMOPAUSE_ALTITUDE_KM's own Source
  lines removed, the scanner still scored it "Cited, not independently
  cross-checked": the stratopause row's Source and Ref lines, a few
  lines above, fell inside its 30-line look-back. Removing those as
  well made both rows Tier-1 (296 to 298). So the window both misses a
  row's own late Source line (above) and credits a neighbour's; in
  constants_new.py, where rows sit close, a removed Source line is
  caught only by test_status_lines.py rule 4, on rows that declare a
  sourced rung.
**Gap:** the fix, by provenance-discipline's method;"""

L386_GAP = """\
**Gap:** the core, the radiative zone and the photosphere's AU row
(CORE_AU, RADIATIVE_ZONE_AU, SOLAR_RADIUS_AU), still unexported: the
"""

L386_NEW = """\
- **2026-10-09, SOLAR_RADIUS_AU's marker shown working** (test A3;
  record %(rec)s). On a throwaway, replacing its two `# Derived:` lines
  with `# Unit: au` and `# Conversion: of SUN_RADIUS_KM -- computed from
  that row, which carries the source and the count.` cleared the one
  UNMARKED CONVERSION test_derived_figures.py prints; 19 conversions
  checked, none wrong. Not applied: that session edited no deliverable.
**Gap:** the core, the radiative zone and the photosphere's AU row
(CORE_AU, RADIATIVE_ZONE_AU, SOLAR_RADIUS_AU), still unexported: the
"""

L351_OLD = """\
    the run-record zone. The skill says both "no patch edits below
    the marker" and "once read, the close empties the live zone".
"""

L351_NEW = """\
    the run-record zone. The skill says both "no patch edits below
    the marker" and "once read, the close empties the live zone".
    Tony, beside that note in his run record of 2026-10-08: "the run
    record is documented only in this timestamped copy not in the
    original WHERE WE ARE".
"""


def new_item(n):
    return """\
#### [L-%(n)d] The worksheet checker compares very small numbers as equal (worksheet checker)
<!-- L:%(n)d status:OPEN upd:%(t)s section:A flag: rice: -->
- **Found 2026-10-09** by the planted-fault run (F7b; record %(rec)s).
  `compare()` in `worksheet_checker.py` rounds the code's value and the
  worksheet's to the coarser of their DECIMAL PLACES. For numbers near
  1e-11 both round to 0, so any two of them match. Probe at 1e30953:
  1e-11, 9.9e-11, 6.674e-11 and 2e-7 each "MATCH" 6.67430e-11, while
  7.0e-5 against 7.292115e-5 is still a MISMATCH. Both drift (L2b) and
  agreement (L2a) use `compare()`, so a moved value on such a row is
  invisible. The one row it reaches today is GRAVITATIONAL_CONSTANT_SI,
  the only constants row this session found whose worksheets give a
  value verdict of YES.
- The rounding is on purpose -- 243 in the code must match 243.0226 in a
  worksheet -- so the fix is to round to significant figures rather than
  to decimal places, not to drop the rounding. Method, not Tony's: he
  asked on 2026-10-09 whether to compare at full digits, and this was
  the answer.
- A change to a checker gets its own session (Where We Are, Settled,
  2026-10-08). L-424's session opens the same function; carry both,
  with a test that fails on the probe values first.
**Gap:** the fix and its test; then the probe values report MISMATCH
and 6.67430e-11 still matches 6.6743e-11.
**Ref:** `worksheet_checker.py` (`compare`, `displayed_precision`,
`float_precision`); `test_worksheet_checker.py`; L-424; L-425.

""" % {'n': n, 't': TODAY, 'rec': REC}


def build_ledger(ledger):
    n = max(int(x) for x in re.findall(r'^#### \[L-(\d+)\]', ledger, re.M)) + 1
    v = {'n': n, 'rec': REC}
    ledger = block_edit(ledger, 418, L418_GAP, L418_CLOSE % v,
                        'A1 to A6 recorded; loose ends re-homed; Gap none')
    ledger = set_meta(ledger, 418, 'DONE', 'C')
    ledger = block_edit(ledger, 425, L425_CHECKED, L425_CORRECTED,
                        'the scanner bullet corrected by measurement')
    ledger = block_edit(ledger, 425, L425_DECIDE, L425_RESULTS % v,
                        'planted-fault results, quote count, the question')
    ledger = block_edit(ledger, 425, L425_REF_OLD, L425_REF_NEW % v, 'Ref')
    ledger = set_meta(ledger, 425)
    a, b = block_span(ledger, 425)
    ledger = ledger[:b] + new_item(n) + ledger[b:]
    print(f"ok  {LEDGER:30s} L-{n}: opened, the checker's small-number comparison")
    ledger = block_edit(ledger, 424, L424_GAP, L424_NEW % v,
                        'F7a seen on a served row; carry L-%d' % n)
    ledger = set_meta(ledger, 424)
    ledger = block_edit(ledger, 414, L414_GAP, L414_NEW % v,
                        "the window credits a neighbour's citation")
    ledger = set_meta(ledger, 414)
    ledger = block_edit(ledger, 386, L386_GAP, L386_NEW % v,
                        "SOLAR_RADIUS_AU's marker shown working")
    ledger = set_meta(ledger, 386)
    ledger = block_edit(ledger, 351, L351_OLD, L351_NEW,
                        "Tony's note on the run-record zone")
    ledger = set_meta(ledger, 351)
    ledger = edit(
        ledger, "Review and RICE update Tony 6-21-2026\n",
        "Module updated: October 9, 2026 with Anthropic's Claude Opus 5.5\n"
        "(L-418 closed on tests A1 to A6; L-425 gains the planted-fault run\n"
        "and the quote count; L-%d opened, the checker's small-number\n"
        "comparison; L-424, L-414, L-386 and L-351 updated), built on\n"
        "%s.\n"
        "Review and RICE update Tony 6-21-2026\n" % (n, BASE),
        LEDGER, 'header stamp')
    return ledger, n


# ------------------------------------------------------------------
# WHERE WE ARE: by section, nothing below the marker
# ------------------------------------------------------------------

def build_wwa(wwa, n):
    if wwa.count(MARKER) != 1:
        raise Refuse(f"ANCHOR FAIL: {WWA}: the run-record marker was not found once.")
    cut = wwa.index(MARKER)
    top, tail = wwa[:cut], wwa[cut:]
    top = edit(top,
               "Last updated: October 8, 2026, at the provenance split's close.\n"
               "- Written at orrery e5cc4bb2 and gallery ab66aba7, before your run of\n"
               "  patch_L418_4.\n",
               "Last updated: October 9, 2026, at the provenance tests' close.\n"
               "- Written at orrery %s and gallery b50f8bd, before your run of\n"
               "  patch_L418_5.\n" % BASE, WWA, 'header')
    a = top.find("> **Changed since you last read this:**\n")
    b = top.find("> **Do next:**", a)
    if a < 0 or b < 0:
        raise Refuse(f"ANCHOR FAIL: {WWA}: the box's two headings were not found.")
    if "The provenance split ran, all 20 checks pass" not in top[a:b]:
        raise Refuse(f"ANCHOR FAIL: {WWA}: 'Changed since' was edited since.")
    top = (top[:a] +
           "> **Changed since you last read this:**\n"
           "> - The four tests of the new provenance skills passed; L-418\n"
           ">   (splitting provenance-discipline) is closed.\n"
           "> - A planted-fault run: four of seven citation faults went\n"
           ">   unnoticed, as expected; three were caught, more weakly than thought.\n"
           "> - L-%d (the checker's small-number comparison): the worksheet\n"
           ">   checker treats very small numbers as equal.\n"
           "> - Your quote question, measured: 38 of the 40 measured numbers\n"
           ">   the Sun and Earth rooms serve say where they were read.\n"
           ">\n" % n + top[b:])
    print(f"ok  {WWA:30s} box: changed since you last read this")
    top = edit(top,
               "> **Do next:** *a fresh session runs the split's four tests\n"
               "> (A3 to A6 in the testing protocol). Then, as you confirmed:",
               "> **Do next:** *as you confirmed:",
               WWA, 'box: do next')
    a = top.find("> **Needs you now:**\n")
    b = top.find("\n*Italic* lines are the must-reads.", a)
    if a < 0 or b < 0:
        raise Refuse(f"ANCHOR FAIL: {WWA}: 'Needs you now' was not found.")
    if "Run patch_L418_4" not in top[a:b]:
        raise Refuse(f"ANCHOR FAIL: {WWA}: 'Needs you now' was edited since.")
    top = (top[:a] +
           "> **Needs you now:**\n"
           "> - *Run patch_L418_5, then orrery_maintenance_run.py, and push.*\n"
           "> - *Decide L-425 (citation location checks): which checks to build,\n"
           ">   on the run's results (on L-425 and in the handoff).*\n"
           + top[b:])
    print(f"ok  {WWA:30s} box: needs you now")
    top = edit(top, "## The road  **>> UPDATED THIS SESSION**\n",
               "## The road\n", WWA, 'marks: the road cleared')
    top = edit(top, "               and Halley checked too. << new this session\n",
               "               and Halley checked too.\n", WWA, 'marks: stage 8 cleared')
    top = edit(top, "               L-423 (the website's checks). << new this session\n",
               "               L-423 (the website's checks).\n", WWA,
               'marks: stage 9 cleared')
    top = edit(top, "## Settled  **>> UPDATED THIS SESSION**\n",
               "## Settled\n", WWA, 'marks: settled cleared')
    top = edit(top, "## Waiting on you  **>> UPDATED THIS SESSION**\n",
               "## Waiting on you\n", WWA, 'marks: waiting cleared')
    top = edit(top,
               "## Signals\n",
               "## Signals  **>> UPDATED THIS SESSION**\n", WWA, 'marks: signals')
    top = edit(top,
               "- Last cache build: 20261008T013323Z, ok, one attempt. Last retry: the\n"
               "  Oct 6 18:20 hand build, two attempts, ok.\n",
               "- Last cache build: 20261008T180043Z, ok. Its last rename took two\n"
               "  attempts, and the retry absorbed it.\n",
               WWA, 'signals: the cache build, from the swap log')
    top = edit(top,
               "- This page's date and the ledger's newest stamp: both Oct 8. Agree.\n",
               "- This page's date and the ledger's newest stamp: both Oct 9. Agree.\n",
               WWA, 'signals: the dates')
    top = edit(top,
               "  designed). Open for build: L-421 (the typed facts), L-418 (splitting\n"
               "  provenance-discipline).\n",
               "  designed). Open for build: L-421 (the typed facts).\n",
               WWA, 'details: L-418 no longer open')
    top = edit(top,
               "- The provenance split: L-418 (splitting provenance-discipline),\n"
               "  run and pushed; record\n"
               "  `documentation/HANDOFF_L418_split_build_20261008.md`; tests\n"
               "  `documentation/TESTING_PROTOCOL_provenance_skills_20261008.md`\n",
               "- The split's tests and the citation checks: L-418 (splitting\n"
               "  provenance-discipline, closed), L-425 (citation location checks),\n"
               "  L-%d (the checker's small-number comparison); record\n"
               "  `documentation/HANDOFF_L418_testing_20261009.md`\n" % n,
               WWA, 'details: the tests')
    top = edit(top,
               "- Today's decisions: `documentation/HANDOFF_decisions_20261008.md`.\n",
               "- The Oct 8 decisions: `documentation/HANDOFF_decisions_20261008.md`.\n",
               WWA, 'details: the decisions line dated')
    top = edit(top,
               "- The Fable sweep's record:\n"
               "  `documentation/HANDOFF_L422_fable_sweep_close_20261007.md`\n"
               "- The galactic plane and the panel colour, both closed: L-420 (the\n"
               "  galactic plane), L-027 (the panel colour);\n"
               "  `documentation/HANDOFF_L420_galactic_plane_20261006.md`\n"
               "- The sweep's report: `documentation/LEDGER_SWEEP_review_20261007.md`\n",
               "",
               WWA, 'details: three closed items out, for the cap (the ledger keeps them)')
    lines = top.count('\n')
    if lines > CAP:
        raise Refuse(f"ERROR: {WWA} would have {lines} lines above the marker; "
                     f"the cap is {CAP}.")
    print(f"ok  {WWA:30s} {lines} lines above the run-record marker (cap {CAP})")
    return top + tail


# ------------------------------------------------------------------
# THE HANDOFF (new file)
# ------------------------------------------------------------------

HANDOFF_TEXT = r'''<!-- Doc-Kind: hand | Session record: the provenance skills tested after the split (L-418 closed), the planted-fault run for citation location checks (L-425), and the quote idea measured, 2026-10-08 to 2026-10-09. -->
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
'''


def main():
    print(f"patch_L418_5 -- built on orrery {BASE}\n")
    try:
        ledger = read_lf(LEDGER)
        if DONE_STAMP in ledger:
            raise Refuse("ERROR: the ledger already carries this patch's header "
                         "stamp; it has already run.")
        wwa = read_lf(WWA)
        ledger, n = build_ledger(ledger)
        wwa = build_wwa(wwa, n)
        h = HANDOFF_TEXT.replace('L-426', 'L-%d' % n) if n != 426 else HANDOFF_TEXT
        out = {LEDGER: ledger, WWA: wwa}
        # FIXED 2026-10-09: the handoff's presence used to mean "already run",
        # but Tony may have saved the delivered copy there himself. Identical:
        # left as it is. Different (his notes, say): refuse, never overwrite.
        if (ROOT / HANDOFF).exists():
            have = read_lf(HANDOFF)
            if have != h:
                raise Refuse(f"ERROR: {HANDOFF} is already in documentation/ and "
                             f"differs from the copy this patch carries (notes "
                             f"added?). It is not overwritten. Move it out of "
                             f"documentation/ and run again; then compare the two.")
            print(f"ok  {HANDOFF:30s} already in place, identical; left as it is")
        else:
            out[HANDOFF] = h
            print(f"ok  {HANDOFF:30s} the session's handoff (new)")
        for rel, text in out.items():
            if any(ord(c) > 127 for c in text):
                raise Refuse(f"ERROR: {rel} would hold non-ASCII characters.")
    except Refuse as exc:
        print(f"\n{exc}\nNOTHING was written.")
        sys.exit(1)
    for rel, text in out.items():
        with open(ROOT / rel, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
    print("\npatch applied: %d files written (%s)" % (len(out), ', '.join(out)))
    print("New item: L-%d (the checker's small-number comparison)." % n)
    print("\nNEXT:\n  1. Run orrery_maintenance_run.py -- it rebuilds the ledger's index\n"
          "     and moves L-418 into the closed section.\n"
          "  2. Move this script into documentation/; commit and push.")


if __name__ == '__main__':
    main()
