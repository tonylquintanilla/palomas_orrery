"""Patch: narrow cross-check credit to attached annotations (L-192).

Run command:

    python patch_L192_attachment.py

Save this file into the SAME folder as provenance_scanner.py, open it in
VS Code, and click Run. Transactional: every edit must find exactly one
anchor or nothing is written at all.

What it changes, in one sentence: a cross-check annotation only grants
credit to the value whose own statement it touches, instead of any value
inside a 30-line window.

Success prints one `ok` line per edit, then `patch applied (N bytes)`.
Failure prints a single ERROR or ANCHOR FAIL line and writes nothing.
"""

import hashlib
import os
import sys

# (files patched are listed in FILES, below)


HELPERS = '''

# ============================================================
# ANNOTATION ATTACHMENT (L-192)
# ============================================================
# A CITATION may be inherited. A section header naming a source
# legitimately covers the declarations beneath it, and the citation
# window plus the block-citation table exist for exactly that.
#
# A cross-check ANNOTATION is a narrower object: it names one checker
# who verified one value on one date and wrote the check down in one
# worksheet. It may not be inherited by proximity. "Gemini checked the
# Moon's radius on 2026-08-02" says nothing about Mercury's radius.
#
# Attachment is adjacency to the unit's own statement -- the unbroken
# run of comment lines ending directly above it, plus the unbroken run
# starting directly below it. A blank line or a line of code ends a run.
#
# Measured when this landed (2026-08-12): 50 of 77 units at the
# cross-checked rung held two attached checkers. The other 27 were
# credited from annotations written for a different value. In the Oort
# cloud case the borrowed annotations pointed at worksheet rows reading
# UNVERIFIED and PARTIAL for the very value being credited, so the
# window was converting a recorded non-verification into a top rung.
#
# Scope: annotation CREDIT only. Citation inheritance is unchanged, and
# the malformation diagnostics keep the wide window -- a broken
# annotation anywhere nearby should still be reported.


def statement_spans(tree):
    """(first_line, last_line, is_module_level) for every statement."""
    spans = []

    def walk(node, top):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.stmt):
                spans.append((
                    child.lineno,
                    getattr(child, 'end_lineno', child.lineno)
                    or child.lineno,
                    top))
                walk(child, False)
            else:
                walk(child, top)

    walk(tree, True)
    return spans


def entry_anchor_map(tree):
    """Map each line of a value expression to the line its entry starts on.

    A display string inside a dict begins one or more lines below the
    key that introduces it, and the comments written for it sit above
    that KEY, not above the literal. Anchoring on the literal's own line
    would find the key line itself -- which is code, not a comment --
    and attach nothing. The innermost (largest) enclosing entry line
    wins for nested structures.
    """
    anchors = {}
    for node in ast.walk(tree):
        pairs = []
        if isinstance(node, ast.Dict):
            for key, val in zip(node.keys, node.values):
                if key is not None:
                    pairs.append((key.lineno, val))
        elif isinstance(node, ast.Assign):
            pairs.append((node.lineno, node.value))
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            pairs.append((node.lineno, node.value))
        for anchor_line, val in pairs:
            lo = val.lineno
            hi = getattr(val, 'end_lineno', lo) or lo
            for ln in range(lo, hi + 1):
                prev = anchors.get(ln)
                if prev is None or anchor_line > prev:
                    anchors[ln] = anchor_line
    return anchors


def comment_run_above(lines, first_line):
    """0-based indices of the comment run ending directly above."""
    out = []
    i = first_line - 2
    while i >= 0 and lines[i].lstrip().startswith('#'):
        out.append(i)
        i -= 1
    return out


def comment_run_below(lines, last_line):
    """0-based indices of the comment run starting directly below."""
    out = []
    j = last_line
    while j < len(lines) and lines[j].lstrip().startswith('#'):
        out.append(j)
        j += 1
    return out


def attached_comment_indices(lines, spans, anchors, line_start):
    """0-based indices of the comment lines attached to this unit.

    A unit declared at module level takes both runs around its whole
    statement -- constants_new.py writes its citations BELOW the
    declaration, the shells modules write them ABOVE, and both are
    correct.

    A string nested inside a dict or a function body takes only the run
    directly above the entry that introduces it. Its enclosing statement
    can span hundreds of lines, and that statement's trailing comments
    belong to the statement, not to one string inside it.
    """
    inner = None
    for first, last, top in spans:
        if first <= line_start <= last:
            if inner is None or (last - first) < (inner[1] - inner[0]):
                inner = (first, last, top)
    if inner is not None and inner[2]:
        return (comment_run_above(lines, inner[0])
                + comment_run_below(lines, inner[1]))
    return comment_run_above(lines, anchors.get(line_start, line_start))


def attached_block(lines, spans, anchors, line_start):
    """(text, 1-based line numbers) of the attached comment lines."""
    idx = sorted(attached_comment_indices(lines, spans, anchors, line_start))
    return ''.join(lines[i] for i in idx), tuple(i + 1 for i in idx)


def collect_orphan_annotations(lines, fname, units):
    """Annotation lines whose comment run touches no code at all.

    The attachment rule refuses window credit. Without this list the
    refused lines would vanish quietly, which is the failure the rule
    exists to prevent -- an annotation that grants nothing and says
    nothing still reads as a completed cross-check to anyone skimming
    the source.

    "Touches no code" is the test, not "attached to a scored unit". A
    run sitting directly above or below a statement was written for that
    statement, whether or not the scanner scores it -- CORE_AU is a
    product of two names, so it never becomes a unit, and its
    annotations are correctly placed all the same. What is genuinely
    unattached is a run fenced off by blank lines on both sides. Two
    live examples at the time of writing are section headers in
    constants_new.py whose annotations were written to cover a group.
    """
    n = len(lines)
    i = 0
    while i < n:
        if not lines[i].lstrip().startswith('#'):
            i += 1
            continue
        j = i
        while j < n and lines[j].lstrip().startswith('#'):
            j += 1
        run = range(i, j)
        code_above = i > 0 and lines[i - 1].strip() != ''
        code_below = j < n and lines[j].strip() != ''
        if not (code_above or code_below):
            for k in run:
                if CROSS_CHECK_LINE_RE.match(lines[k]):
                    ORPHAN_ANNOTATIONS.append(
                        (fname, k + 1, lines[k].strip()))
        i = j

'''


SCANNER_EDITS = [
    # ---- 1. unit slots -------------------------------------------------
    (b"""        'context_text',        # text the unit sees for citation lookup
""",
     b"""        'context_text',        # text the unit sees for citation lookup
        'attached_text',       # comment run(s) touching the unit's statement
        'attached_lines',      # 1-based line numbers of that run
"""),

    # ---- 2. orphan collector ------------------------------------------
    (b"""CROSS_CHECK_ISSUES = []
""",
     b"""CROSS_CHECK_ISSUES = []

# L-192: annotation lines that attach to no unit. Diagnostic only.
ORPHAN_ANNOTATIONS = []
"""),

    # ---- 3. helper block ----------------------------------------------
    (b"""def get_unit_interior(lines, line_start, line_end):
    \"\"\"Return the text inside the unit itself (per-entry comments).\"\"\"
    start = max(0, line_start - 1)
    end = min(len(lines), line_end)
    return ''.join(lines[start:end])
""",
     b"""def get_unit_interior(lines, line_start, line_end):
    \"\"\"Return the text inside the unit itself (per-entry comments).\"\"\"
    start = max(0, line_start - 1)
    end = min(len(lines), line_end)
    return ''.join(lines[start:end])
""" + HELPERS.encode('ascii')),

    # ---- 4. constant units --------------------------------------------
    (b"""        context_text = get_context_block(lines, line_start, line_end,
                                         lookback=30, lookahead=15)

        units.append(ProvenanceUnit(
            kind='constant',""",
     b"""        context_text = get_context_block(lines, line_start, line_end,
                                         lookback=30, lookahead=15)
        att_text, att_lines = attached_block(lines, spans, anchors,
                                             line_start)

        units.append(ProvenanceUnit(
            kind='constant',
            attached_text=att_text,
            attached_lines=att_lines,"""),

    # ---- 5. spans/anchors built once per file --------------------------
    (b"""    fname = os.path.basename(filepath)

    # ---- Top-level assignments: constants and dicts ----""",
     b"""    fname = os.path.basename(filepath)

    # L-192: statement spans and entry anchors, built once per file and
    # threaded through unit construction. Attachment is a property of
    # where a declaration SITS, so it has to be computed while the AST
    # is in hand rather than re-derived later from line numbers.
    spans = statement_spans(tree)
    anchors = entry_anchor_map(tree)

    # ---- Top-level assignments: constants and dicts ----"""),

    # ---- 6. dict unit builder signature + body -------------------------
    (b"""            unit = _make_dict_unit(node, name, lines, module_name,
                                    fname, role)""",
     b"""            unit = _make_dict_unit(node, name, lines, module_name,
                                    fname, role, spans, anchors)"""),

    (b"""def _make_dict_unit(assign_node, name, lines, module_name, fname, role):""",
     b"""def _make_dict_unit(assign_node, name, lines, module_name, fname, role,
                    spans=(), anchors=None):"""),

    (b"""    interior_text = get_unit_interior(lines, line_start, line_end)
""",
     b"""    interior_text = get_unit_interior(lines, line_start, line_end)
    att_text, att_lines = attached_block(lines, spans, anchors or {},
                                         line_start)
"""),

    # ---- 7. string units ----------------------------------------------
    (b"""        units.extend(_extract_string_units(
            tree, lines, module_name, fname, role, block_table))

    return units""",
     b"""        units.extend(_extract_string_units(
            tree, lines, module_name, fname, role, block_table,
            spans, anchors))

    # L-192: anything the attachment rule refused is reported, never
    # dropped. Silence about an unattached annotation is the same
    # failure as silence about an unexamined one.
    collect_orphan_annotations(lines, fname, units)

    return units"""),

    (b"""def _extract_string_units(tree, lines, module_name, fname, role,
                          block_table=None):""",
     b"""def _extract_string_units(tree, lines, module_name, fname, role,
                          block_table=None, spans=(), anchors=None):"""),

    (b"""        units.append(ProvenanceUnit(
            kind='string',""",
     b"""        att_text, att_lines = attached_block(lines, spans, anchors or {},
                                             line_start)

        units.append(ProvenanceUnit(
            kind='string',
            attached_text=att_text,
            attached_lines=att_lines,"""),

    # ---- 8. the scoring change ----------------------------------------
    (b"""    records, cross_check_issues = parse_cross_checks(text)
    sourced = cited or bool(unit.inherited_citation)
    identities = distinct_checker_identities(records)
    distinct_checkers = len(identities) >= 2

    if records or cross_check_issues:
        _record_cross_check_diagnostics(
            unit, records, cross_check_issues, sourced, len(identities))""",
     b"""    #
    # L-192: credit comes from ATTACHED annotations only -- the comment
    # run touching this unit's own statement. The wide window still
    # feeds the diagnostics below, because a malformed annotation
    # anywhere nearby is worth reporting, but it no longer lets one
    # value earn a rung on the evidence of its neighbour.
    records, cross_check_issues = parse_cross_checks(text)
    attached_records, _attached_issues = parse_cross_checks(
        getattr(unit, 'attached_text', None) or '')
    sourced = cited or bool(unit.inherited_citation)
    identities = distinct_checker_identities(attached_records)
    distinct_checkers = len(identities) >= 2

    if records or cross_check_issues:
        _record_cross_check_diagnostics(
            unit, records, cross_check_issues, sourced,
            len(distinct_checker_identities(records)))"""),

    (b"""    elif sourced and records:""",
     b"""    elif sourced and attached_records:"""),

    # ---- 9. scan_project: clear + report -------------------------------
    (b"""    del CROSS_CHECK_ISSUES[:]
""",
     b"""    del CROSS_CHECK_ISSUES[:]
    del ORPHAN_ANNOTATIONS[:]
"""),

    (b"""    if CROSS_CHECK_ISSUES:
        print(f"{len(CROSS_CHECK_ISSUES)} cross-check annotation issue(s) "
              f"-- malformed or unusable annotations, see audit")""",
     b"""    if CROSS_CHECK_ISSUES:
        print(f"{len(CROSS_CHECK_ISSUES)} cross-check annotation issue(s) "
              f"-- malformed or unusable annotations, see audit")

    if ORPHAN_ANNOTATIONS:
        print(f"{len(ORPHAN_ANNOTATIONS)} orphan annotation(s) -- attached "
              f"to no claim, granted no credit, see audit")
        for ofile, oline, _text in ORPHAN_ANNOTATIONS:
            print(f"    {ofile}:{oline}")"""),

    (b"""                    cross_check_issues=list(CROSS_CHECK_ISSUES),""",
     b"""                    cross_check_issues=list(CROSS_CHECK_ISSUES),
                    orphan_annotations=list(ORPHAN_ANNOTATIONS),"""),

    # ---- 10. audit section --------------------------------------------
    (b"""                    cross_check_issues=None, started=None):""",
     b"""                    cross_check_issues=None, started=None,
                    orphan_annotations=None):"""),

    (b"""    # ---- Citation level mismatch (L-174) ----""",
     b"""    # ---- Orphan annotations (L-192) ----
    if orphan_annotations:
        out.append("## ORPHAN ANNOTATIONS -- diagnostic, no scoring effect")
        out.append("")
        out.append("Cross-check annotations that touch no claim's own "
                   "statement. They granted no credit. A citation may be "
                   "inherited from a section header; an annotation may "
                   "not, because it names one checker who verified one "
                   "value.")
        out.append("")
        out.append("Each of these was written for something. Either it "
                   "belongs on a specific value -- move it down and the "
                   "credit follows -- or it was meant to cover a group, "
                   "which this codebase does not express. Nothing here "
                   "is safe to delete without reading the worksheet it "
                   "names.")
        out.append("")
        out.append("| File | Line | Annotation |")
        out.append("|------|-----:|------------|")
        for ofile, oline, otext in sorted(orphan_annotations):
            otext = otext.replace('|', r'\\|')
            out.append(f"| `{ofile}` | {oline} | {otext} |")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Citation level mismatch (L-174) ----"""),
]


# --- test_cross_checked.py --------------------------------------------
# Two tests pinned the retired behaviour. Both went red the moment the
# rule changed, which is exactly what they were written to do.

TEST_EDITS = [
    # The synthetic fixtures build a unit by hand and never set
    # attached_text, so every annotation in them now reads as
    # unattached. These fixtures exist to exercise the parser and the
    # ladder, not attachment; giving them the same text for both keeps
    # them testing what they were written to test.
    (b"""        context_text=context_text,
        raw_value=raw_value or 'fixture claim text',""",
     b"""        context_text=context_text,
        attached_text=context_text,
        attached_lines=(),
        raw_value=raw_value or 'fixture claim text',"""),

    # The bleed test asserted that a neighbour five lines away inherits
    # an annotation it never earned. That was true, was pinned here
    # deliberately, and is now fixed. The assertion inverts.
    (b'''def test_lookback_window_bleed_is_measured():
    """An annotation reaches every claim inside the lookback window.''',
     b'''def test_lookback_window_bleed_is_closed():
    """An annotation reaches ONLY the claim whose statement it touches.'''),

    (b'''    This is a property of the flat 60-line context block, not of the
    annotation parser: the window is the same one that carries `#
    Source:` comments down to the claims below them. A separately
    sourced claim a few lines below an annotated one therefore reads the
    annotation too and receives V2 without anyone having checked it.

    The test pins both halves -- that it happens near, and that it stops
    far away -- so the mechanism is on record rather than inferred. The
    mitigation is a Piece 2 placement question, not a parser change;
    tight placement alone does NOT solve it, because the annotation is
    already tightly placed in this fixture.
    """''',
     b'''    Until L-192 this test asserted the opposite, and was right to.
    The flat context block carried an annotation to every claim inside
    it, so a separately sourced claim a few lines below an annotated
    one read that annotation too and received V2 without anyone having
    checked it. The mechanism was pinned here on purpose rather than
    left to inference.

    Credit now comes from the comment run touching a claim's own
    statement, so the near neighbour holds at V3. Both halves stay
    pinned -- near and far -- because a rule that only works at
    distance is the old behaviour wearing a new name.
    """'''),

    (b"""    test_lookback_window_bleed_is_measured,
""",
     b"""    test_lookback_window_bleed_is_closed,
"""),

    (b'''    assert neighbour_vuln(5) == V_CROSS_CHECKED, (
        "expected the near neighbour to inherit the annotation through "
        "the context window; if this now fails, the window changed and "
        "the Piece 2 placement guidance needs revisiting")''',
     b'''    assert neighbour_vuln(5) == V_SOURCED, (
        "the near neighbour must NOT inherit an annotation written for "
        "another claim; if this fails, credit is flowing through the "
        "context window again (L-192)")'''),
]


FILES = [
    ('provenance_scanner.py', SCANNER_EDITS),
    ('test_cross_checked.py', TEST_EDITS),
]


def stage(path, edits, label):
    """Apply one file's edits in memory. Returns bytes or None on failure."""
    with open(path, 'rb') as f:
        data = f.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    print(f"{label}: fingerprint {fp}  ({len(data)} bytes)")

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print(f"{label}: file uses CRLF; anchors translated")

    staged = data
    for i, (old, new) in enumerate(edits, 1):
        o, n = old, new
        if is_crlf:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = staged.count(o)
        if count != 1:
            head = o.split(b'\n')[0][:70]
            print(f"ANCHOR FAIL {label} edit {i}: expected 1 match, "
                  f"got {count}: {head!r}")
            return None
        staged = staged.replace(o, n, 1)
        print(f"ok  {label} edit {i}")
    return staged


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    for fname, _edits in FILES:
        if not os.path.exists(os.path.join(here, fname)):
            print(f"ERROR: {fname} not found next to this script ({here})")
            return 1

    # Stage everything first. Nothing is written unless every edit in
    # every file found its anchor -- one half-patched file is worse than
    # none, because the next reader cannot tell which half landed.
    staged = {}
    for fname, edits in FILES:
        result = stage(os.path.join(here, fname), edits, fname)
        if result is None:
            print("nothing written")
            return 1
        staged[fname] = result

    for fname, content in staged.items():
        with open(os.path.join(here, fname), 'wb') as f:
            f.write(content)
        print(f"patch applied to {fname} ({len(content)} bytes)")

    print("")
    print("Next: run provenance_scanner.py. Expect the cross-checked rung")
    print("to fall from 77 to 50, and a list of 4 orphan annotations.")
    print("Then run test_cross_checked.py -- expect 17 passed, 0 failed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
