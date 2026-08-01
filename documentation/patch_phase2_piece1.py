"""
patch_phase2_piece1.py -- L-156 Phase 2 Piece 1: cross-check annotation
recognition in provenance_scanner.py.

Built on 523ea0247f6908f1c29d35468908e324542206bd
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME folder as provenance_scanner.py
    (the palomas_orrery repo root), open it in VS Code, and click Run.
    Equivalent command line: python patch_phase2_piece1.py

WHAT YOU SHOULD SEE
    Success: one "ok" line per edit, then "patch applied (N bytes)".
    Failure: a single "ERROR:" line (wrong base file) or "ANCHOR FAIL"
    line (one edit's anchor text was not found). Nothing is written in
    either failure case, so it is always safe to re-check and re-run.

WHAT IT CHANGES
    Five anchored edits to provenance_scanner.py:
      1. parse_cross_checks() + its regexes, after has_citation()
      2. CROSS_CHECK_ISSUES module-level collector
      3. scoring branch in score_unit() + diagnostics recorder
      4. V_CROSS_CHECKED constant comment (removes "NOTHING SETS THIS")
      5. scan_project / generate_report diagnostics plumbing

Module created: August 2026 with Anthropic's Claude Opus 5.
"""

import os
import sys

TARGET = 'provenance_scanner.py'


# ---- Edit 1: parse_cross_checks(), placed after has_citation() ----

ANCHOR_1 = b'''def has_stale_marker(text):
    """Does the given text contain a staleness indicator?"""'''

NEW_1 = b'''# ============================================================
# CROSS-CHECK ANNOTATIONS (L-156 Phase 2 / D4)
# ============================================================
# An annotation line records that ONE checker independently verified a
# claim against primary sources: who checked, an ISO date, and the
# worksheet the check is written down in. Two annotations with distinct
# checker identities, on a claim that already carries source evidence,
# are what the V_CROSS_CHECKED rung means.
#
# The colon after the keyword is load-bearing. Prose comments in this
# codebase already use the bare phrase -- planet_visualization_utilities
# carries "Giants cross-checked to Voyager 2 (Uranus: Desch..." -- and
# without the required colon that line is a live false positive.
#
# There is deliberately NO worked example anywhere in this module. The
# scanner scans itself, and a complete annotation written inside a
# comment here would sit in the citation lookback window of this
# module's own units and grant them V2 on themselves. The annotation
# form is documented in the provenance-discipline skill instead.

CROSS_CHECK_LINE_RE = re.compile(
    r'(?mi)^[ \\t]*#[ \\t]*cross-checked[ \\t]*:(?P<body>[^\\n]*)$')

# ISO only: a four-digit year, optionally -MM, optionally -DD. Prose
# dates are rejected on purpose -- "April 2026" leaves no deterministic
# boundary between the checker identity and the date.
CROSS_CHECK_DATE_RE = re.compile(
    r'\\b((?:19|20)\\d{2}(?:-\\d{2}(?:-\\d{2})?)?)\\b')

# The reference parenthetical, searched in the text AFTER the date so a
# parenthetical inside the identity cannot be mistaken for it.
CROSS_CHECK_REF_RE = re.compile(r'\\(([^()]*)\\)')

# A prose date carries a four-digit year, so the ISO test alone does not
# reject "Gemini April 2026" -- it silently splits into identity
# "Gemini April" and date "2026". That is not a cosmetic mis-parse: two
# annotations from ONE checker in different months would then read as
# two distinct checker identities and earn V2 by themselves, which is
# precisely the hole the two-model rule exists to close. So a month name
# immediately before the year disqualifies the line.
CROSS_CHECK_PROSE_MONTH_RE = re.compile(
    r'(?i)\\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|'
    r'jun(?:e)?|jul(?:y)?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|'
    r'nov(?:ember)?|dec(?:ember)?)\\.?\\s*,?\\s*$')


def parse_cross_checks(text):
    """Parse cross-check annotation lines out of a context block.

    Returns (records, issues).

    records: list of (identity, date, reference) tuples -- one per line
        carrying all three parts. Tuple order is fixed and callers index
        positionally; identity is index 0.
    issues:  list of (raw_line, error_code) for lines that look like an
        annotation but do not qualify. Codes: 'missing_year',
        'prose_date', 'missing_identity', 'missing_reference',
        'empty_reference', 'non_markdown_reference'.

    A line qualifies only with an ISO date and, after that date, a
    parenthetical reference ending in `.md`. Anything less earns
    nothing. This is the anti-gaming rule: the annotation is not a
    citation form, is deliberately absent from SOURCE_PATTERNS, and
    never grants source credit on its own. A malformed annotation on an
    uncited claim leaves it at V_RECALLED, exactly as if the line were
    not there -- but it is reported as a diagnostic rather than dropped
    in silence.

    The reference is checked for shape, not existence. Whether the named
    worksheet is actually in the repo is a separate integrity question,
    not the parser's job.
    """
    if not text or 'cross-check' not in text.lower():
        return [], []

    records = []
    issues = []

    for match in CROSS_CHECK_LINE_RE.finditer(text):
        raw = match.group(0).strip()
        body = match.group('body')

        date_match = CROSS_CHECK_DATE_RE.search(body)
        if date_match is None:
            issues.append((raw, 'missing_year'))
            continue

        identity = ' '.join(body[:date_match.start()].split())
        if not identity:
            issues.append((raw, 'missing_identity'))
            continue
        if CROSS_CHECK_PROSE_MONTH_RE.search(identity):
            issues.append((raw, 'prose_date'))
            continue

        ref_match = CROSS_CHECK_REF_RE.search(body[date_match.end():])
        if ref_match is None:
            issues.append((raw, 'missing_reference'))
            continue

        reference = ref_match.group(1).strip()
        if not reference:
            issues.append((raw, 'empty_reference'))
            continue
        if not reference.lower().endswith('.md'):
            issues.append((raw, 'non_markdown_reference'))
            continue

        records.append((identity, date_match.group(1), reference))

    return records, issues


def distinct_checker_identities(records):
    """Distinct checker identities from parse_cross_checks() records.

    Returns them in first-seen order, keeping original capitalization
    for the report while comparing case-folded and whitespace-normalized.

    Known limitation, by decision: this is string identity, not model
    family. "Gemini" and "Gemini Pro" count as two checkers. The
    competitive pattern is human-mediated -- the integrator confirms the
    two legs were genuinely independent; the scanner only observes that
    two different checker strings are present with valid references.
    """
    seen = set()
    ordered = []
    for record in records:
        key = ' '.join(record[0].split()).lower()
        if key not in seen:
            seen.add(key)
            ordered.append(record[0])
    return ordered


def has_stale_marker(text):
    """Does the given text contain a staleness indicator?"""'''


# ---- Edit 2: module-level collector, beside the other diagnostics ----

ANCHOR_2 = b'''SHADOWED_STRINGS = []
DEEP_CITATIONS = []
'''

NEW_2 = b'''SHADOWED_STRINGS = []
DEEP_CITATIONS = []

# L-156 Phase 2 diagnostic. Cross-check annotations that were rejected
# by the parser, or accepted but unusable (present on an unsourced
# claim, or repeating one checker identity). None of these move a
# score; they exist so a malformed annotation is visible rather than
# silently doing nothing. Entries: (file, line, code, detail).
CROSS_CHECK_ISSUES = []
'''


# ---- Edit 3: scoring branch in score_unit() ----

ANCHOR_3 = b'''    if cited and stale:
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Cited, not cross-checked; date-sensitive"
    elif cited:'''

NEW_3 = b'''    # L-156 Phase 2 / D4. V_CROSS_CHECKED requires BOTH halves:
    # source evidence AND a completed competitive cross-check.
    #
    # Source evidence first, because a cross-check verifies a sourced
    # claim -- it does not substitute for sourcing. Without that
    # prerequisite an uncited claim carrying annotations would jump
    # V4 to V2, which is a stronger move than cite-to-clear.
    #
    # Inherited citations count. A string inside a cited dict block is
    # sourced by the same reasoning the elif below already uses; not
    # accepting it here would strand legitimately cross-checked claims
    # at V3 for a reason unrelated to the check.
    #
    # Two DISTINCT checkers, because the rung is defined by a two-model
    # process. One annotation is half of it, and says so in the reason.
    records, cross_check_issues = parse_cross_checks(text)
    sourced = cited or bool(unit.inherited_citation)
    identities = distinct_checker_identities(records)
    distinct_checkers = len(identities) >= 2

    if records or cross_check_issues:
        _record_cross_check_diagnostics(
            unit, records, cross_check_issues, sourced, len(identities))

    if sourced and distinct_checkers:
        unit.vuln = V_CROSS_CHECKED
        who = ', '.join(identities)
        unit.vuln_reason = (
            "Cross-checked by %d models (%s)%s"
            % (len(identities), who,
               "; date-sensitive" if stale else ""))
    elif sourced and records:
        # One leg of the competitive pattern done. Still V3, but the
        # reason says which state it is in, so the audit shows work in
        # progress instead of looking identical to an unchecked claim.
        unit.vuln = V_SOURCED
        unit.vuln_reason = (
            "Cited; cross-check incomplete (%d/2 models)"
            % len(identities))
    elif cited and stale:
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Cited, not cross-checked; date-sensitive"
    elif cited:'''


# ---- Edit 3b: the diagnostics recorder, above score_unit() ----

ANCHOR_3B = b'''def score_unit(unit, imported_names):
    """Assign vulnerability and criticality to a unit.'''

NEW_3B = b'''def _record_cross_check_diagnostics(unit, records, issues, sourced,
                                    distinct_count):
    """Collect cross-check annotation problems for the audit report.

    Diagnostic only -- nothing here changes a score. Three shapes are
    worth seeing: the parser's own rejections, an annotation sitting on
    a claim with no citation to verify, and two annotations that name
    the same checker (which is one leg written twice, not two legs).

    Deduplicated by (file, code, detail). Every unit whose context
    window reaches an annotation reports that annotation's problems, so
    a single malformed line would otherwise fill the table with one row
    per nearby claim. The recorded line is the FIRST unit that saw it,
    which is why the report column reads "Near line" -- the annotation
    itself sits somewhere in the lookback above that line, not on it.
    """
    def _add(code, detail):
        for entry in CROSS_CHECK_ISSUES:
            if entry[0] == unit.file and entry[2] == code \\
                    and entry[3] == detail:
                return
        CROSS_CHECK_ISSUES.append((unit.file, unit.line_start, code, detail))

    for raw, code in issues:
        _add(code, raw)

    if records and not sourced:
        _add('unsourced_annotation',
             "annotation present, but the claim carries no citation")

    if len(records) >= 2 and distinct_count < 2:
        _add('duplicate_identity',
             "two or more annotations name the same checker")


def score_unit(unit, imported_names):
    """Assign vulnerability and criticality to a unit.'''


# ---- Edit 4: V_CROSS_CHECKED constant comment ----

ANCHOR_4 = b'''V_CROSS_CHECKED = 2   # Independently cross-checked against dated evidence,
                      # blind (the checker was not shown our value). NEVER
                      # auto-promotable to V_FETCHED at any rigor level --
                      # the scanner can observe that a check is claimed, not
                      # that it was rigorous.
                      # NOTHING SETS THIS YET. Population arrives with the
                      # `# Cross-checked:` annotation recognition in D4;
                      # until then this rung is intentionally empty rather
                      # than dead code.'''

NEW_4 = b'''V_CROSS_CHECKED = 2   # Independently verified via competitive pattern:
                      # same worksheet to multiple models, independent
                      # research, integrator compares. Requires source
                      # evidence AND two distinct checker annotations.
                      # NEVER auto-promotable to V_FETCHED at any rigor
                      # level -- the scanner can observe that a check is
                      # claimed, not that it was rigorous.
                      # See provenance-discipline skill v1.4 for the
                      # annotation form and competitive-pattern definition.'''


# ---- Edit 5a: clear the collector at scan start ----

ANCHOR_5A = b'''    del SCOPE_DECLARED_BLOCKS[:]
    del SHADOWED_STRINGS[:]
    del DEEP_CITATIONS[:]
    del SHADOW_CONSTANTS[:]'''

NEW_5A = b'''    del SCOPE_DECLARED_BLOCKS[:]
    del SHADOWED_STRINGS[:]
    del DEEP_CITATIONS[:]
    del SHADOW_CONSTANTS[:]
    del CROSS_CHECK_ISSUES[:]'''


# ---- Edit 5b: console notice + report handoff ----

ANCHOR_5B = b'''    generate_report(all_units, consistent_dups, inconsistencies,
                    files_scanned, project_dir, output_path,
                    accepted_residuals=accepted_residuals,
                    coverage_gaps=coverage_gaps,
                    scope_declared=list(SCOPE_DECLARED_BLOCKS),
                    shadowed=list(SHADOWED_STRINGS),
                    deep_citations=list(DEEP_CITATIONS),
                    shadow_constants=list(SHADOW_CONSTANTS))'''

NEW_5B = b'''    if CROSS_CHECK_ISSUES:
        print(f"{len(CROSS_CHECK_ISSUES)} cross-check annotation issue(s) "
              f"-- malformed or unusable annotations, see audit")

    generate_report(all_units, consistent_dups, inconsistencies,
                    files_scanned, project_dir, output_path,
                    accepted_residuals=accepted_residuals,
                    coverage_gaps=coverage_gaps,
                    scope_declared=list(SCOPE_DECLARED_BLOCKS),
                    shadowed=list(SHADOWED_STRINGS),
                    deep_citations=list(DEEP_CITATIONS),
                    shadow_constants=list(SHADOW_CONSTANTS),
                    cross_check_issues=list(CROSS_CHECK_ISSUES))'''


# ---- Edit 5c: generate_report signature ----

ANCHOR_5C = b'''                    scope_declared=None, shadowed=None,
                    deep_citations=None, shadow_constants=None):
    """Write PROVENANCE_AUDIT.md."""'''

NEW_5C = b'''                    scope_declared=None, shadowed=None,
                    deep_citations=None, shadow_constants=None,
                    cross_check_issues=None):
    """Write PROVENANCE_AUDIT.md."""'''


# ---- Edit 5d: render the diagnostic subsection ----

ANCHOR_5D = b'''    # ---- Citation level mismatch (L-174) ----
    if shadowed or deep_citations:'''

NEW_5D = b'''    # ---- Cross-check annotation issues (L-156 Phase 2) ----
    if cross_check_issues:
        out.append("## CROSS-CHECK ANNOTATION ISSUES -- diagnostic, "
                   "no scoring effect")
        out.append("")
        out.append("Annotation lines the scanner saw but could not use. "
                   "None of these changed a score. They are listed "
                   "because an annotation that quietly does nothing is "
                   "worse than one that is visibly wrong -- it reads as "
                   "a completed cross-check to anyone skimming the "
                   "source.")
        out.append("")
        out.append("A qualifying annotation needs an ISO date and, "
                   "after it, a parenthetical worksheet reference "
                   "ending in `.md`. Two of them, naming different "
                   "checkers, on a claim that already has a citation, "
                   "are what earns V2.")
        out.append("")
        out.append("`Near line` is the first claim that saw the "
                   "annotation, not the annotation's own line. The "
                   "annotation sits within the citation lookback above "
                   "it.")
        out.append("")
        out.append("| File | Near line | Issue | Detail |")
        out.append("|------|----------:|-------|--------|")
        for entry in sorted(cross_check_issues):
            cfile, cline, code, detail = entry
            detail = detail.replace('|', r'\\|')
            out.append(f"| `{cfile}` | {cline} | `{code}` | {detail} |")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Citation level mismatch (L-174) ----
    if shadowed or deep_citations:'''


EDITS = [
    (ANCHOR_1, NEW_1, 'parse_cross_checks() after has_citation()'),
    (ANCHOR_2, NEW_2, 'CROSS_CHECK_ISSUES collector'),
    (ANCHOR_3B, NEW_3B, '_record_cross_check_diagnostics()'),
    (ANCHOR_3, NEW_3, 'score_unit() cross-check branch'),
    (ANCHOR_4, NEW_4, 'V_CROSS_CHECKED comment'),
    (ANCHOR_5A, NEW_5A, 'clear collector at scan start'),
    (ANCHOR_5B, NEW_5B, 'console notice + report handoff'),
    (ANCHOR_5C, NEW_5C, 'generate_report signature'),
    (ANCHOR_5D, NEW_5D, 'report diagnostic subsection'),
]


def main():
    if not os.path.exists(TARGET):
        print("ERROR: %s not found. Put this script in the same folder "
              "as provenance_scanner.py and run it from there." % TARGET)
        return 1

    with open(TARGET, 'rb') as handle:
        content = handle.read()

    original_len = len(content)

    if b'def parse_cross_checks(' in content:
        print("ERROR: provenance_scanner.py already has "
              "parse_cross_checks(). Nothing written -- this patch has "
              "already been applied.")
        return 1

    for anchor, replacement, label in EDITS:
        found = content.count(anchor)
        if found != 1:
            print("ANCHOR FAIL (%s): expected 1 match, found %d. "
                  "Nothing written." % (label, found))
            return 1
        content = content.replace(anchor, replacement)
        print("ok  %s" % label)

    with open(TARGET, 'wb') as handle:
        handle.write(content)

    print("patch applied (%d bytes, was %d)" % (len(content), original_len))
    return 0


if __name__ == '__main__':
    sys.exit(main())
