"""
patch_phase1c_citation_inheritance.py

Phase 1c -- citation-window inheritance for provenance_scanner.py
(ledger L-156 Gap item 6).

Built on cf061d7336cfed20a991218deec8b666e08d31b7
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT THIS DOES
    A display string nested inside a dict block that carries its own
    "# Source:" header currently scores V4 RECALLED, because the string
    extractor walks every string with its own flat 60-line window and is
    blind to the enclosing block's citation. This patch teaches the
    scanner structural containment: build a table of dict blocks and
    their citations, then let a string inherit the citation of the block
    that contains it.

    Inheritance is NOT clearance. An inheriting string lands at
    V3 SOURCED -- "cited, never independently cross-checked" -- the same
    rung L-158 established for derived values. No new rung, no change to
    the 1b ladder.

    The load-bearing invariant: an UNCITED block inherits NOTHING. The
    resolver takes the narrowest block containing the string and stops
    there. It never searches outward to an enclosing dict or to the
    module. Silent outward fallback would falsely clear the genuinely
    uncited blocks tracked as L-173, handing them provenance nobody wrote.

HOW TO RUN IT (VS Code)
    1. Save this file into the SAME folder as provenance_scanner.py
       (your palomas_orrery folder).
    2. Open it in VS Code.
    3. Click the Run button (the triangle, top right).

    Or from a terminal in that folder:  python patch_phase1c_citation_inheritance.py

WHAT YOU SHOULD SEE
    One "ok" line per edit, then "patch applied (N bytes)".

    If instead you see a single "ERROR:" or "ANCHOR FAIL" line, nothing
    was written -- the file on disk is untouched and it is always safe to
    re-check and retry. ANCHOR FAIL means the text this patch expected to
    find had already changed; ERROR means the base file is not the one
    this patch was built against.

    This patch is all-or-nothing. It edits nothing until every anchor has
    matched exactly once.

AFTER IT RUNS
    Run the scanner as usual to see the effect:  python provenance_scanner.py .
    Expected: Tier 1 156 -> 133, Tier 2 563 -> 586, Tier 3 and Tier 4
    unchanged on the real population. See the build notes for the two
    accounting details behind those numbers.

Module updated: July 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = 'provenance_scanner.py'
EXPECTED_MD5 = '94891f347cfe1b46bf14020468571993'


# ------------------------------------------------------------------
# EDIT 1 -- module docstring credit line
# ------------------------------------------------------------------

E1_OLD = b"""Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-162:
CONCEPT_ALIASES entries added for the 14 newly-named CENTER_BODY_RADII
constants).

Role: devtool"""

E1_NEW = b"""Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-162:
CONCEPT_ALIASES entries added for the 14 newly-named CENTER_BODY_RADII
constants).

Module updated: July 2026 with Anthropic's Claude Opus 5 (L-156 Gap item 6,
Phase 1c: citation-block inheritance -- a display string inside a dict block
that carries its own citation now inherits it at V_SOURCED instead of
scoring V_RECALLED. Strictly narrowest-block containment; an uncited block
inherits nothing, which is what keeps the genuinely uncited blocks tracked
as L-173 visible).

Role: devtool"""


# ------------------------------------------------------------------
# EDIT 2 -- constant, scope pattern, block table, resolver
# ------------------------------------------------------------------

E2_OLD = b"""class ProvenanceUnit:"""

E2_NEW = b'''# ============================================================
# CITATION BLOCK INHERITANCE (L-156 Gap item 6, Phase 1c)
# ============================================================
# Citations in this codebase attach at the block level: a comment run
# above a dict entry covers the whole body block below it. The string
# extractor walks each string with its own flat lookback window and
# cannot see that. These helpers close the gap structurally -- by
# containment, not by widening the window.
#
# Distance is deliberately NOT the discriminator here. shell_configs.py
# and idealized_orbits.py have overlapping citation-gap distributions,
# so no threshold separates "inside a cited block" from "happens to have
# a citation somewhere above." Widening the window is not a smaller
# version of this fix; it is a different and wrong one.

# Lookback from a block's opening line up to its citation comment run.
# 8 lines covers every cited block in shell_configs.py. 15 covers
# jupiter_visualization_shells.py's function-local ring_params (citation
# at line 897, assignment opens at 906) with margin, and is applied above
# both the block key and the enclosing assignment.
CITATION_LOOKBACK_BLOCK = 15

# An author may explicitly narrow what a citation covers. Where this
# marker appears in a captured run, the scanner declines to inherit and
# flags the block for review instead. Inheriting past a comment that says
# "colors below are developer-selected" would be the scanner asserting
# provenance the author disclaimed -- the same failure class as a
# "# Source:" over recalled data, pointed the other way.
SCOPE_DECLARATION_RE = re.compile(r'Scope of the above citation:',
                                  re.IGNORECASE)

# Blocks whose citation carries a scope declaration. Collected during
# extraction and reported after the scan so they stay visible rather
# than silently doing nothing.
SCOPE_DECLARED_BLOCKS = []


def citation_run_above(lines, decl_line, lookback=CITATION_LOOKBACK_BLOCK):
    """Find the citation comment run immediately above a declaration.

    Searches up to `lookback` lines above `decl_line` for a line matching
    a citation pattern, then expands to the whole contiguous comment run
    around it. Capturing the run rather than the matched line matters:
    for shell_configs.py's Moon block the pattern matches a CONTINUATION
    line, not the "# Source:" head, and recording only the matched line
    would put a fragment in the report and lose the sources named on the
    other lines.

    Stops at the first line that is neither blank nor a comment, so a
    citation belonging to a previous block is never picked up.

    Returns (citation_line, citation_text), or (None, None).
    """
    i = decl_line - 2
    limit = max(-1, decl_line - 2 - lookback)
    while i > limit:
        text = lines[i]
        if has_citation(text):
            top = i
            while top - 1 >= 0 and lines[top - 1].lstrip().startswith('#'):
                top -= 1
            bottom = i
            while (bottom + 1 < len(lines)
                   and lines[bottom + 1].lstrip().startswith('#')):
                bottom += 1
            return i + 1, ''.join(lines[top:bottom + 1])
        if text.strip() and not text.lstrip().startswith('#'):
            break
        i -= 1
    return None, None


def build_citation_block_table(tree, lines, fname=None):
    """Record every dict block in a file and the citation above it.

    One ast.walk pass over every ast.Assign at ANY nesting depth. Depth
    matters: shell_configs.py's dicts are module-level, but
    jupiter_visualization_shells.py's ring_params is function-local, and
    a module-level-only walk misses it entirely.

    Two block shapes are recorded, because citations attach to both:
      - 'assign': the whole dict assignment, cited above its first line
      - 'entry':  one dict-valued entry, cited above its key line

    Blocks are keyed by LINE RANGE, not by name. That is what makes
    cross-dict inheritance impossible: SHELL_CONFIGS['Jupiter'] and
    CUSTOM_SHELLS['Jupiter'] carry different citations and occupy
    disjoint spans, so neither can reach the other's.
    """
    blocks = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        if not isinstance(node.value, ast.Dict):
            continue

        dict_name = target.id
        assign_start = node.lineno
        assign_end = (getattr(node.value, 'end_lineno', assign_start)
                      or assign_start)
        cite_line, cite_text = citation_run_above(lines, assign_start)
        blocks.append({
            'dict_name': dict_name, 'key': None, 'kind': 'assign',
            'start': assign_start, 'end': assign_end,
            'citation_line': cite_line, 'citation_text': cite_text,
        })

        for key, value in zip(node.value.keys, node.value.values):
            if key is None:
                continue
            if not (isinstance(key, ast.Constant)
                    and isinstance(key.value, str)):
                continue
            if not isinstance(value, ast.Dict):
                continue
            entry_start = key.lineno
            entry_end = (getattr(value, 'end_lineno', entry_start)
                         or entry_start)
            k_line, k_text = citation_run_above(lines, entry_start)
            blocks.append({
                'dict_name': dict_name, 'key': key.value, 'kind': 'entry',
                'start': entry_start, 'end': entry_end,
                'citation_line': k_line, 'citation_text': k_text,
            })

    for block in blocks:
        if block['citation_text'] and SCOPE_DECLARATION_RE.search(
                block['citation_text']):
            SCOPE_DECLARED_BLOCKS.append((
                fname or '<unknown>', block['dict_name'], block['key'],
                block['start'], block['end'], block['citation_line']))

    return blocks


def resolve_block_citation(blocks, line_start, line_end):
    """Return the citation a string at these lines inherits, or None.

    Takes the NARROWEST block containing the string and stops there.
    If that block has no citation of its own, the string inherits
    nothing -- the resolver does NOT continue outward to an enclosing
    dict or to the module.

    That stopping rule is the whole point. Searching outward would let
    SHELL_CONFIGS['Pluto'] (genuinely uncited, 10 findings) pick up a
    citation from SHELL_CONFIGS itself the moment anyone adds one,
    silently clearing findings whose real problem is a missing source.
    Those blocks are tracked as L-173 and need actual sourcing, not a
    scoring change.

    Returns (citation_text, declined), where `declined` is True when the
    resolved citation carries an explicit scope declaration.
    """
    containing = [b for b in blocks
                  if b['start'] <= line_start and line_end <= b['end']]
    if not containing:
        return None, False

    containing.sort(key=lambda b: (b['end'] - b['start'], b['start']))
    block = containing[0]

    if not block['citation_text']:
        return None, False
    if SCOPE_DECLARATION_RE.search(block['citation_text']):
        return None, True
    return block['citation_text'], False


class ProvenanceUnit:'''


# ------------------------------------------------------------------
# EDIT 3 -- ProvenanceUnit slots
# ------------------------------------------------------------------

E3_OLD = b"""        'is_docstring',        # for strings: True if this is a module/class/func docstring
    ]"""

E3_NEW = b"""        'is_docstring',        # for strings: True if this is a module/class/func docstring
        'inherited_citation',  # for strings: citation text of the containing block
        'scope_declined',      # for strings: containing block's citation is scope-limited
    ]"""


# ------------------------------------------------------------------
# EDIT 4 -- build the table and hand it to the string extractor
# ------------------------------------------------------------------

E4_OLD = b"""        units.extend(_extract_string_units(
            tree, lines, module_name, fname, role))"""

E4_NEW = b"""        # Phase 1c: containment table for block-citation inheritance.
        block_table = build_citation_block_table(tree, lines, fname)
        units.extend(_extract_string_units(
            tree, lines, module_name, fname, role, block_table))"""


# ------------------------------------------------------------------
# EDIT 5 -- string extractor signature
# ------------------------------------------------------------------

E5_OLD = b"""def _extract_string_units(tree, lines, module_name, fname, role):"""

E5_NEW = b"""def _extract_string_units(tree, lines, module_name, fname, role,
                          block_table=None):"""


# ------------------------------------------------------------------
# EDIT 6 -- resolve inheritance for each string unit
# ------------------------------------------------------------------

E6_OLD = b"""        context_text = base_context + '\\n' + s

        units.append(ProvenanceUnit("""

E6_NEW = b"""        context_text = base_context + '\\n' + s

        # Phase 1c: does an enclosing cited dict block cover this string?
        inherited_citation = None
        scope_declined = False
        if block_table:
            inherited_citation, scope_declined = resolve_block_citation(
                block_table, line_start, line_end)

        units.append(ProvenanceUnit("""


# ------------------------------------------------------------------
# EDIT 7 -- carry the fields onto the unit
# ------------------------------------------------------------------

E7_OLD = b"""            role=role,
            is_docstring=(line_start in docstring_lines),
        ))"""

E7_NEW = b"""            role=role,
            is_docstring=(line_start in docstring_lines),
            inherited_citation=inherited_citation,
            scope_declined=scope_declined,
        ))"""


# ------------------------------------------------------------------
# EDIT 8 -- score inheriting strings at V_SOURCED
# ------------------------------------------------------------------

E8_OLD = b'''    else:
        unit.vuln = V_RECALLED
        unit.vuln_reason = "No source citation (recalled)"'''

E8_NEW = b'''    elif unit.inherited_citation:
        # Phase 1c: the string sits inside a dict block that carries its
        # own citation. Inheriting is not clearing -- V_SOURCED means
        # "cited, never independently cross-checked," same rung L-158
        # gave derived values.
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Cited via enclosing block citation"
    else:
        unit.vuln = V_RECALLED
        unit.vuln_reason = "No source citation (recalled)"'''


# ------------------------------------------------------------------
# EDIT 9 -- reset the scope collector at the start of a scan
# ------------------------------------------------------------------

E9_OLD = b"""    suppressed_fingerprints, accepted_residuals = load_exceptions(project_dir)"""

E9_NEW = b"""    # Phase 1c: module-level collector, cleared per scan so a second
    # scan_project() call in the same process does not double-report.
    del SCOPE_DECLARED_BLOCKS[:]

    suppressed_fingerprints, accepted_residuals = load_exceptions(project_dir)"""


# ------------------------------------------------------------------
# EDIT 10 -- hand the scope-declared blocks to the report
# ------------------------------------------------------------------

E10_OLD = b"""    generate_report(all_units, consistent_dups, inconsistencies,
                    files_scanned, project_dir, output_path,
                    accepted_residuals=accepted_residuals,
                    coverage_gaps=coverage_gaps)"""

E10_NEW = b"""    if SCOPE_DECLARED_BLOCKS:
        print(f"{len(SCOPE_DECLARED_BLOCKS)} block(s) carry a scope-limited "
              f"citation -- inheritance declined, see audit")

    generate_report(all_units, consistent_dups, inconsistencies,
                    files_scanned, project_dir, output_path,
                    accepted_residuals=accepted_residuals,
                    coverage_gaps=coverage_gaps,
                    scope_declared=list(SCOPE_DECLARED_BLOCKS))"""


# ------------------------------------------------------------------
# EDIT 11 -- report signature
# ------------------------------------------------------------------

E11_OLD = b"""                    accepted_residuals=None, coverage_gaps=None):
    \"\"\"Write PROVENANCE_AUDIT.md.\"\"\""""

E11_NEW = b"""                    accepted_residuals=None, coverage_gaps=None,
                    scope_declared=None):
    \"\"\"Write PROVENANCE_AUDIT.md.\"\"\""""


# ------------------------------------------------------------------
# EDIT 12 -- report section for scope-limited citations
# ------------------------------------------------------------------

E12_OLD = b"""    # ---- Coverage gaps (L-078 check 1b) ----"""

E12_NEW = b"""    # ---- Scope-limited citations (L-156 Phase 1c) ----
    if scope_declared:
        out.append("## SCOPE-LIMITED CITATIONS -- inheritance declined")
        out.append("")
        out.append("These dict blocks carry a citation whose author "
                   "explicitly narrowed what it covers (a `Scope of the "
                   "above citation:` note). Strings inside them do NOT "
                   "inherit the citation -- asserting provenance the "
                   "author disclaimed is the same failure as citing over "
                   "recalled data, pointed the other way. Findings inside "
                   "these blocks stay where they were. Listed here so the "
                   "decision stays visible rather than silently doing "
                   "nothing.")
        out.append("")
        out.append("| File | Block | Lines | Citation at |")
        out.append("|------|-------|-------|------------:|")
        for entry in sorted(scope_declared):
            sfile, dname, dkey, bstart, bend, cline = entry
            label = f"`{dname}['{dkey}']`" if dkey else f"`{dname}`"
            out.append(f"| `{sfile}` | {label} | {bstart}-{bend} | {cline} |")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Coverage gaps (L-078 check 1b) ----"""


EDITS = [
    ("E1  module credit line", E1_OLD, E1_NEW),
    ("E2  constant + block table + resolver", E2_OLD, E2_NEW),
    ("E3  ProvenanceUnit slots", E3_OLD, E3_NEW),
    ("E4  build and pass block table", E4_OLD, E4_NEW),
    ("E5  string extractor signature", E5_OLD, E5_NEW),
    ("E6  resolve inheritance per string", E6_OLD, E6_NEW),
    ("E7  carry fields onto unit", E7_OLD, E7_NEW),
    ("E8  score inheriting strings V_SOURCED", E8_OLD, E8_NEW),
    ("E9  reset scope collector per scan", E9_OLD, E9_NEW),
    ("E10 pass scope blocks to report", E10_OLD, E10_NEW),
    ("E11 report signature", E11_OLD, E11_NEW),
    ("E12 scope-limited report section", E12_OLD, E12_NEW),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print(f"ERROR: {TARGET} not found next to this script.")
        print(f"       Looked in: {here}")
        print("       Move this script into your palomas_orrery folder "
              "and run it again.")
        sys.exit(1)

    with open(path, 'rb') as f:
        content = f.read()

    actual = hashlib.md5(content).hexdigest()
    if actual != EXPECTED_MD5:
        print(f"ERROR: {TARGET} is not the file this patch was built against.")
        print(f"       expected MD5 {EXPECTED_MD5}")
        print(f"       found    MD5 {actual}")
        print("       Nothing written -- the file on disk is untouched.")
        print()
        # Narrow it down rather than leaving a bare hash mismatch.
        if b'CITATION_LOOKBACK_BLOCK' in content:
            print("       Likely cause: this patch has ALREADY been applied.")
            print("       Check with: python test_citation_inheritance.py")
        elif b'\r\n' in content:
            print("       Likely cause: the file has Windows CRLF line "
                  "endings, but the patch was built against the LF copy "
                  "in the repo. The content may be otherwise identical.")
        else:
            print("       Likely cause: the file changed after this patch "
                  "was built. Re-pull and rebuild the patch.")
        sys.exit(1)

    # Verify every anchor before writing anything.
    for label, old, _new in EDITS:
        count = content.count(old)
        if count != 1:
            print(f"ANCHOR FAIL [{label}]: expected exactly 1 match, "
                  f"found {count}. Nothing written.")
            sys.exit(1)

    patched = content
    for label, old, new in EDITS:
        patched = patched.replace(old, new, 1)
        print(f"ok  {label}")

    # ASCII / LF gate on the result.
    try:
        patched.decode('ascii')
    except UnicodeDecodeError as exc:
        print(f"ERROR: patched content is not pure ASCII ({exc}). "
              "Nothing written.")
        sys.exit(1)
    if b'\r\n' in patched:
        print("ERROR: patched content contains CRLF line endings. "
              "Nothing written.")
        sys.exit(1)

    with open(path, 'wb') as f:
        f.write(patched)

    print(f"patch applied ({len(patched)} bytes)")
    print()
    print("Next: run the scanner to see the effect.")
    print("      python provenance_scanner.py .")
    print("Expected: Tier 1 156 -> 133, Tier 2 563 -> 586.")


if __name__ == '__main__':
    main()
