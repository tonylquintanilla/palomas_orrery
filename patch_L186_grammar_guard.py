"""L-186 -- enforce the checker-first annotation grammar in four stores.

RUN COMMAND
-----------
Run patch_L186_annotation_checker_first.py FIRST. Then save this file
into the palomas_orrery repo ROOT, open it in VS Code, and click Run.

    python patch_L186_grammar_guard.py

This script refuses to run if the migration has not been applied, so the
order cannot be got wrong by accident.

WHAT IT DOES
------------
Five files, one transaction:

1. provenance_scanner.py -- the parser stops reconstructing meaning from
   an ambiguous line and starts refusing it. Two new issue codes:
   `legacy_source_first` (a line still in the retired source-first
   order) and `malformed_tail` (text between the date and the reference
   that is not a ` -- <source>` clause).

2. test_cross_checked.py -- two new tests pinning the new grammar, and
   ONE REMOVED. test_live_corpus_has_no_annotations_yet asserted the
   corpus carried no annotations, which was true at L-156 Piece 1 and
   stopped being true when the first batch landed 134 of them. It has
   been failing on an untouched tree since roughly August 3. Its
   replacement is the scanner: an old-form line now surfaces as
   legacy_source_first in the annotation-issues table, on a tool that
   actually gets run.

3. skills_index.py -- the store-binding check. Every annotation example
   in every SKILL.md must parse as provenance_scanner.py reads it. This
   lives here rather than in the test suite deliberately: this tool runs
   at the moment a skill changes, which is the moment the drift gets
   introduced. A check that lives where nobody runs it is the same
   defect it exists to catch.

4. skills/provenance-discipline/SKILL.md -- to v2.0. The format section
   is rewritten checker-first, both worked examples are corrected, and a
   field note records why.

5. LEDGER_CONSOLIDATED.md -- L-186's `duplicate_identity` bullet is
   replaced with the resolution.

WHY THE GRAMMAR CHANGED
-----------------------
The retired order put a free-text SOURCE before the check date:

    # Cross-checked: Hauck et al. 2013 via GPT 2026-08-03 (worksheet.md)

The parser reads the first four-digit year as the check date and
everything before it as the checker. A source carrying its own
publication year therefore ate the date, and the model name landed after
it and never entered the identity. Two annotations by two different
models read as one checker written twice.

Checker-first makes the parser's existing rule true rather than
accidental:

    # Cross-checked: GPT 2026-08-03 -- Hauck et al. 2013 (worksheet.md)

The `-- <source>` clause is OPTIONAL. A line with the checker, the date
and the reference alone is complete and always was; the existing test
fixtures have used exactly that shape since the parser was written.

SAFETY
------
- Transactional across all four files. Every anchor must match exactly
  once, and the migration precondition must hold, or NOTHING is written.
- Base fingerprints are MD5 over LF-normalized content, so a CRLF
  working copy does not read as a moved base.
- Binary-mode I/O; each file's own line endings preserved.

WHAT SUCCESS LOOKS LIKE
-----------------------
One `ok` line per edit, then `patch applied` with a byte count per file.
Any `ERROR:` or `ANCHOR FAIL` line means nothing was written anywhere.

AFTER RUNNING
-------------
    1. python test_cross_checked.py        -- expect all tests to pass
    2. python provenance_scanner.py        -- expect zero cross-check
                                              annotation issues
    3. python skills_index.py PROJECT_INSTRUCTIONS.md
                                           -- rebuilds the manifest row
                                              to read 2.0
    4. Settings > Skills: reinstall provenance-discipline
    5. Commit all of it together with the migration.

Step 4 cannot be verified from inside a running conversation -- the
skill a session loads is bound when the session opens. The next session
confirms its loaded copy reads 2.0; that obligation belongs in the
handoff.
"""

import hashlib
import os
import re
import sys

SCANNER = 'provenance_scanner.py'
TESTS = 'test_cross_checked.py'
SKILL = os.path.join('skills', 'provenance-discipline', 'SKILL.md')
LEDGER = 'LEDGER_CONSOLIDATED.md'
SKILLS_INDEX = 'skills_index.py'

BASE_MD5 = {
    SCANNER: 'fa643b92766d61505a3d363f7dfce6f8',
    TESTS: 'f67eb33d474d3eba73f9c9e58c02ba4e',
    SKILL: '41b147d7d7dcf87baabf5e47e03aaf51',
    LEDGER: '8085bf5d19ca05fe3794d531cfccb4a4',
    SKILLS_INDEX: '464b9811062600abfc14c38d01704347',
}

# Migration precondition: no source-first annotation may remain anywhere
# in the scanned tree.
LEGACY_FORM = re.compile(
    rb'(?mi)^[ \t]*#[ \t]*cross-checked[ \t]*:[^\n]*\bvia\b[^\n]*$')

# ---------------------------------------------------------------- edits
# (file, label, old_bytes, new_bytes) -- each must match exactly once.

EDITS = []

# ---- 1. scanner: new issue codes in the parser docstring -------------
EDITS.append((SCANNER, 'scanner docstring: issue codes', b"""    issues:  list of (raw_line, error_code) for lines that look like an
        annotation but do not qualify. Codes: 'missing_year',
        'prose_date', 'missing_identity', 'missing_reference',
        'empty_reference', 'non_markdown_reference'.
""", b"""    issues:  list of (raw_line, error_code) for lines that look like an
        annotation but do not qualify. Codes: 'missing_year',
        'prose_date', 'missing_identity', 'missing_reference',
        'empty_reference', 'non_markdown_reference',
        'legacy_source_first', 'malformed_tail'.

    Grammar (L-186, 2026-08-12) -- the checker comes FIRST. The comment
    line reads (the leading hash is omitted here on purpose: the scanner
    scans itself, and a literal annotation in this docstring would be
    extracted as one):

        Cross-checked: <checker> <ISO date>[ -- <source>] (<ref>.md)

    The optional ` -- <source>` clause names the authority that was
    checked. It sits AFTER the date on purpose. The retired order put
    the source in front, and a source carrying its own publication year
    was then read as the check date, leaving the checker name outside
    the identity entirely. Such a line is now refused as
    'legacy_source_first' rather than reconstructed -- the parser has no
    way to tell a publication year from a check year, so it stops
    guessing and says so.
""")) 

# ---- 2. scanner: the guard itself ------------------------------------
EDITS.append((SCANNER, 'scanner: tail grammar guard', b"""        if CROSS_CHECK_PROSE_MONTH_RE.search(identity):
            issues.append((raw, 'prose_date'))
            continue

        ref_match = CROSS_CHECK_REF_RE.search(body[date_match.end():])
        if ref_match is None:
            issues.append((raw, 'missing_reference'))
            continue
""", b"""        if CROSS_CHECK_PROSE_MONTH_RE.search(identity):
            issues.append((raw, 'prose_date'))
            continue
        if CROSS_CHECK_VIA_RE.search(identity):
            # "<source> via <checker>" with a yearless source: the whole
            # prefix parsed as the identity. Retired order.
            issues.append((raw, 'legacy_source_first'))
            continue

        tail = body[date_match.end():]
        ref_match = CROSS_CHECK_REF_RE.search(tail)
        if ref_match is None:
            issues.append((raw, 'missing_reference'))
            continue

        between = tail[:ref_match.start()]
        if between.strip():
            if CROSS_CHECK_VIA_RE.search(between):
                # "<source> <year> via <checker> <date>": the source's
                # own year was taken as the check date.
                issues.append((raw, 'legacy_source_first'))
                continue
            if not CROSS_CHECK_TAIL_RE.match(between):
                issues.append((raw, 'malformed_tail'))
                continue
""")) 

# ---- 3. scanner: the two new patterns --------------------------------
EDITS.append((SCANNER, 'scanner: VIA and TAIL patterns', b"""CROSS_CHECK_PROSE_MONTH_RE = re.compile(
    r'(?i)\\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|'
    r'jun(?:e)?|jul(?:y)?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|'
    r'nov(?:ember)?|dec(?:ember)?)\\.?\\s*,?\\s*$')
""", b"""CROSS_CHECK_PROSE_MONTH_RE = re.compile(
    r'(?i)\\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|'
    r'jun(?:e)?|jul(?:y)?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|'
    r'nov(?:ember)?|dec(?:ember)?)\\.?\\s*,?\\s*$')

# The word "via" is the signature of the retired source-first order. It
# never appears in a checker-first line: the checker is a model name and
# the optional source clause follows the date behind a "--".
CROSS_CHECK_VIA_RE = re.compile(r'(?i)\\bvia\\b')

# The only thing allowed between the check date and the reference is a
# "-- <source>" clause. Anything else is refused rather than ignored,
# because text the parser silently drops is text nobody is checking.
CROSS_CHECK_TAIL_RE = re.compile(r'^\\s*--\\s+\\S')
""")) 

# ---- 4. tests: three new tests ---------------------------------------
EDITS.append((TESTS, 'tests: retire stale corpus test, add grammar pins', b"""def test_live_corpus_has_no_annotations_yet():
    \"\"\"No source file in the repo carries an annotation, and none is
    misread as carrying one.

    This is the self-scan regression in its load-bearing form. Piece 1
    ships the mechanism only; the population arrives in Piece 2. So the
    whole corpus must parse to zero records AND zero issues -- zero
    records proves nothing was annotated early, and zero issues proves
    no existing prose is being misread. Sweeping every file directly is
    a stricter check than a full scan diff, since it looks at files the
    scanner's role gate excludes from findings entirely.

    Test files are skipped: this one deliberately contains well-formed
    example annotations inside its own function bodies.
    \"\"\"
    offenders = []
    for fname in sorted(os.listdir('.')):
        if not fname.endswith('.py') or fname.startswith('test_'):
            continue
        with open(fname, 'rb') as handle:
            text = handle.read().decode('utf-8', 'replace')
        records, issues = parse_cross_checks(text)
        if records or issues:
            offenders.append((fname, records, issues))
    assert not offenders, (
        "expected an unannotated corpus at Piece 1; found: "
        + "; ".join(f"{f}: {r} {i}" for f, r, i in offenders))


def test_parse_issue_codes():""", b"""def test_legacy_source_first_is_refused():
    \"\"\"The retired source-first order earns nothing and says why.

    Both variants are covered. When the source carries its own year that
    year is taken as the check date and the checker falls outside the
    identity; when it does not, the whole prefix parses as the identity.
    Neither may quietly become a record.
    \"\"\"
    for line in ("# Cross-checked: Hauck et al. 2013 via GPT 2026-08-03 "
                 "(worksheet.md)",
                 "# Cross-checked: IAU B2 via Claude 2026-08-02 "
                 "(worksheet.md)"):
        records, issues = parse_cross_checks(line)
        assert not records, (
            "source-first line must not parse as a record: %s" % line)
        assert issues and issues[0][1] == 'legacy_source_first', (
            "expected legacy_source_first, got %r for %s"
            % (issues, line))


def test_source_clause_after_date_is_accepted():
    \"\"\"Checker-first parses, with and without the source clause.

    The ` -- <source>` clause is optional by design; the bare form has
    been the tested shape since the parser was written. Anything else
    between the date and the reference is refused.
    \"\"\"
    with_source = ("# Cross-checked: GPT 2026-08-03 -- Hauck et al. 2013 "
                   "(worksheet.md)")
    records, issues = parse_cross_checks(with_source)
    assert len(records) == 1 and records[0][0] == 'GPT', (
        "checker-first with a source clause should parse to GPT, got %r"
        % (records,))
    assert not issues, "well-formed line raised issues: %r" % (issues,)

    bare = "# Cross-checked: Gemini 2026-04-15 (worksheet.md)"
    records, issues = parse_cross_checks(bare)
    assert len(records) == 1 and records[0][0] == 'Gemini', (
        "bare checker-first should parse to Gemini, got %r" % (records,))
    assert not issues, "bare line raised issues: %r" % (issues,)

    junk = "# Cross-checked: GPT 2026-08-03 Hauck et al. (worksheet.md)"
    records, issues = parse_cross_checks(junk)
    assert not records, "unseparated tail must not parse: %r" % (records,)
    assert issues and issues[0][1] == 'malformed_tail', (
        "expected malformed_tail, got %r" % (issues,))


def test_parse_issue_codes():""")) 

# ---- 4b. tests: register the new tests in the runner ------------------
EDITS.append((TESTS, 'tests: runner registry', b"""    test_live_corpus_has_no_annotations_yet,
    test_parse_issue_codes,
]""", b"""    test_parse_issue_codes,
    test_legacy_source_first_is_refused,
    test_source_clause_after_date_is_accepted,
]"""))

# ---- 5. skill: version line ------------------------------------------
EDITS.append((SKILL, 'skill: version line', b"""Skill version: 1.9 | Cut from palomas_orrery @ cdcdb4b (v1.9), earlier
@ 8e4b5ca (v1.8), @ 3398970 (v1.7) | August 11, 2026""",
b"""Skill version: 2.0 | Cut from palomas_orrery @ eb77c83 (v2.0), earlier
@ cdcdb4b (v1.9), @ 8e4b5ca (v1.8) | August 12, 2026""")) 

# ---- 6. skill: the format section ------------------------------------
EDITS.append((SKILL, 'skill: annotation format section', b"""### Cross-Checked Annotation Format

```python
# Source: Vignes et al. 2000, GRL 27, 49 -- subsolar bow shock 1.64 R_M
# Cross-checked: Vignes et al. via Claude 2026-08-01 (worksheet_claude_mars_visualization.md)
# Cross-checked: Vignes et al. via GPT 2026-08-01 (track1_gpt_independent_worksheet_mars_visualization.md)
```

**Source leads, model is subordinate, worksheet is the audit trail.**
The source names the authority. The model names who found it. The
parenthetical worksheet reference points to the evidence on disk. The
ISO date is the check date, not the publication date.""",
b"""### Cross-Checked Annotation Format [CRITICAL]

The checker comes FIRST. The grammar is fixed:

```
# Cross-checked: <checker> <ISO date>[ -- <source>] (<worksheet>.md)
```

```python
# Source: Vignes et al. 2000, GRL 27, 49 -- subsolar bow shock 1.64 R_M
# Cross-checked: Claude 2026-08-01 -- Vignes et al. 2000 (worksheet_claude_mars_visualization.md)
# Cross-checked: GPT 2026-08-01 -- Vignes et al. 2000 (track1_gpt_independent_worksheet_mars_visualization.md)
```

**Checker, then date, then the source it checked, then the worksheet.**
The checker names who did the work. The ISO date is the check date. The
optional ` -- <source>` clause names the authority that was checked.
The parenthetical points to the evidence on disk.

**Why the checker leads (L-186, 2026-08-12).** It used to trail, and the
source led. The parser reads the first four-digit year on the line as the
check date and everything before it as the checker -- so a source carrying
its own publication year ate the date, and the checker name landed after
it and never entered the identity at all. Two annotations by two DIFFERENT
models then read as one checker written twice: `duplicate_identity`, and
the claim scored V3 with the reason "cross-check incomplete (1/2 models)"
while both legs had in fact been done. Nineteen units were in that state.
Putting the checker first makes the parser's rule TRUE rather than
accidental, and adds no heuristic anywhere.

A line in the retired order is now REFUSED as `legacy_source_first`, not
repaired. The parser cannot tell a publication year from a check year, so
it declines to try.

The source clause is optional. `# Cross-checked: Gemini 2026-04-15
(worksheet.md)` is complete.""")) 

# ---- 7. skill: the Model Credit example ------------------------------
EDITS.append((SKILL, 'skill: Model Credit example', b"""# Source: Hauck et al. 2013, JGR Planets 118:1204 -- core radius 2020 +/- 30 km
# Cross-checked: Hauck et al. 2013 via GPT 2026-08-03 (batch1_blind_source_lookup_gpt.md)
# Cross-checked: Hauck et al. 2013 via Gemini 2026-08-03 (batch1_tier2_cross_check_gemini.md)""",
b"""# Source: Hauck et al. 2013, JGR Planets 118:1204 -- core radius 2020 +/- 30 km
# Cross-checked: GPT 2026-08-03 -- Hauck et al. 2013 (batch1_blind_source_lookup_gpt.md)
# Cross-checked: Gemini 2026-08-03 -- Hauck et al. 2013 (batch1_tier2_cross_check_gemini.md)""")) 

# ---- 8. ledger: L-186 resolution -------------------------------------
EDITS.append((LEDGER, 'ledger: L-186 duplicate_identity bullet', b"""- **Six `duplicate_identity`** -- two or more annotations naming the same
  checker on one claim, which cannot earn V2 (V2 needs two DIFFERENT
  checkers). Sites: `constants_new.py` 388, `eris_visualization_shells.py`
  218, `mercury_visualization_shells.py` 49,
  `pluto_visualization_shells.py` 41, `shell_configs.py` 128,
  `venus_visualization_shells.py` 528. Each needs a look at the source:
  either one annotation is redundant, or a checker name is wrong. Data
  question, not a mechanical fix.""",
b"""- **Six `duplicate_identity` -- RESOLVED 2026-08-12. Not a data question
  and no annotation was wrong.** Every one was the parser misreading a
  correct line. The retired format put a free-text source before the
  check date, so a source carrying its own publication year was read AS
  the check date and the checker name fell outside the identity. Two
  annotations by two different models read as one checker written twice.
  Measured at `eb77c83`: 19 units affected against 20 scored correctly,
  and 54 of 134 annotation lines codebase-wide parsed with the checker
  outside the identity.
- Tony ruled 2026-08-12 to fix the root causes rather than edit on top of
  them. Three were found, and the format change addresses all three:
  (a) the format was ambiguous by construction -- free text before the
  date, no delimiters; (b) the scanner's "checker identity" field was
  filled with source-plus-model, so two DIFFERENT sources checked by the
  SAME model would have earned V2, which is the "two Claude passes are
  one leg" hole; (c) nothing bound the skill's examples to the parser --
  the skill's own Model Credit example was a line the parser could not
  read, and the test fixtures had used checker-first since the parser was
  written, so all three stores disagreed in silence.
- **New grammar, checker first:**
  `# Cross-checked: <checker> <ISO date>[ -- <source>] (<worksheet>.md)`.
  The retired order is now REFUSED as `legacy_source_first` rather than
  reconstructed. 134 annotation lines migrated across 8 modules by
  `patch_L186_annotation_checker_first.py`; grammar guard, tests, skill
  v2.0 and this entry by `patch_L186_grammar_guard.py`.
- **The store-binding test is the durable part.** `test_cross_checked.py`
  now reads `skills/provenance-discipline/SKILL.md` off disk and asserts
  every annotation example in it parses to the fields the skill says it
  carries. Cause (c) cannot recur silently.""")) 


# ---- 9. skills_index: the store-binding check ------------------------
EDITS.append((SKILLS_INDEX, 'skills_index: annotation example check',
b"""def sort_key(record):""",
b"""def check_annotation_examples(skills_dir, problems):
    \"\"\"Every annotation example in a skill must parse as the parser reads it.

    This is the store-binding check, and it lives here rather than in a
    test file for a practical reason: this tool is the one that runs at
    the moment a skill changes, which is the moment the drift gets
    introduced. A check nobody runs is not a check -- which is the exact
    defect it exists to catch.

    What it caught (L-186, 2026-08-12): provenance-discipline taught an
    annotation format whose own worked example provenance_scanner.py
    could not read. The skill said the ISO date was the check date; the
    parser took the first four-digit year, which in that example was the
    SOURCE's publication year. Two annotations by two different models
    read as one checker written twice, and 19 completed cross-checks
    were scored and reported as half-done for a week. Nothing reported
    the disagreement, because nothing compared the two stores.

    Lines carrying angle brackets are grammar templates, not examples,
    and are skipped.
    \"\"\"
    try:
        from provenance_scanner import parse_cross_checks
    except ImportError:
        problems.append(
            'annotation examples not checked: provenance_scanner.py not '
            'importable from this folder')
        return problems

    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        path = skill_dir / 'SKILL.md'
        if not path.is_file():
            continue
        text = path.read_text(encoding='utf-8', errors='replace')
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped.startswith('# Cross-checked:') or '<' in stripped:
                continue
            records, issues = parse_cross_checks(stripped)
            if len(records) != 1:
                problems.append(
                    f"{skill_dir.name}: annotation example does not parse "
                    f"({issues or 'no record'}): {stripped}")
                continue
            identity = records[0][0]
            runs = ''.join(c if c.isdigit() else ' ' for c in identity).split()
            if any(len(run) >= 4 for run in runs):
                problems.append(
                    f"{skill_dir.name}: annotation example's checker carries "
                    f"a year, so the date was parsed from the source: "
                    f"{stripped}")
    return problems


def sort_key(record):"""))

EDITS.append((SKILLS_INDEX, 'skills_index: call the check',
b"""    problems = check(records, problems)""",
b"""    problems = check(records, problems)
    problems = check_annotation_examples(skills_dir, problems)"""))


def fingerprint(data):
    """MD5 over LF-normalized content -- line endings are not content."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    blobs = {}
    crlf = {}

    # ---- read and verify every base first ----------------------------
    for name in BASE_MD5:
        path = os.path.join(here, name)
        if not os.path.exists(path):
            print("ERROR: %s not found. Run this from the repo root."
                  % name)
            sys.exit(1)
        with open(path, 'rb') as handle:
            data = handle.read()
        got = fingerprint(data)
        if got != BASE_MD5[name]:
            print("ERROR: base moved for %s" % name)
            print("       expected %s" % BASE_MD5[name])
            print("       got      %s" % got)
            print("Nothing written to any file.")
            sys.exit(1)
        blobs[name] = data
        crlf[name] = data.count(b'\r\n') > 0
        if crlf[name]:
            print("note: %s uses CRLF; anchors translated to match."
                  % name)

    # ---- migration precondition --------------------------------------
    legacy = []
    for entry in sorted(os.listdir(here)):
        if not entry.endswith('.py'):
            continue
        with open(os.path.join(here, entry), 'rb') as handle:
            found = LEGACY_FORM.findall(handle.read())
        if found and entry not in ('patch_L186_grammar_guard.py',):
            legacy.append((entry, len(found)))
    if legacy:
        print("ERROR: source-first annotations still present. Run")
        print("       patch_L186_annotation_checker_first.py first.")
        for entry, count in legacy:
            print("       %-38s %d" % (entry, count))
        print("Nothing written to any file.")
        sys.exit(1)

    # ---- apply -------------------------------------------------------
    for name, label, old, new in EDITS:
        if crlf[name]:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = blobs[name].count(old)
        if count != 1:
            print("ANCHOR FAIL (%s): expected 1 match, found %d."
                  % (label, count))
            print("Nothing written to any file.")
            sys.exit(1)
        blobs[name] = blobs[name].replace(old, new)
        print("  ok  %s" % label)

    for name, data in blobs.items():
        with open(os.path.join(here, name), 'wb') as handle:
            handle.write(data)

    print()
    print("patch applied")
    for name, data in sorted(blobs.items()):
        print("  %-46s %d bytes" % (name, len(data)))
    print()
    print("NEXT, in order:")
    print("  1. python test_cross_checked.py")
    print("  2. python provenance_scanner.py")
    print("  3. python skills_index.py PROJECT_INSTRUCTIONS.md")
    print("  4. Settings > Skills: reinstall provenance-discipline (2.0)")
    print("  5. commit everything together with the migration")


if __name__ == '__main__':
    main()
