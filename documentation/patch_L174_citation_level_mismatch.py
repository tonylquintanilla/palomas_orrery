"""
patch_L174_citation_level_mismatch.py

L-174 -- citation-level mismatch: the ring_params data fix plus a
scanner-side diagnostic that makes the shape visible everywhere else.

Built on b31200934bc6bfe0e697c4f8cb5f9a1d1ffa1931
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

THE PROBLEM

    Phase 1c gave the scanner structural containment: a display string
    inherits the citation of the narrowest dict block containing it, and
    an uncited block inherits nothing. That rule is deliberately strict
    -- no outward search -- because outward search would silently clear
    the genuinely uncited blocks tracked as L-173.

    The strictness has a cost, and jupiter_visualization_shells.py is
    where it showed up. `ring_params` carries its citation above the
    ASSIGNMENT, but its four per-ring entries are dicts of their own with
    no citation above their keys. The resolver stops at the narrowest
    block -- an uncited ring -- and never sees the citation one level up.
    Four rings shadow a citation meant to cover all of them.

    The generalization, which predicts both the success and the failure:
    a citation must sit at the SAME DEPTH as the narrowest block the
    table records. The table records depth 1 (the assignment) and depth 2
    (its direct dict-valued entries), and nothing deeper.

      - shell_configs.py works: citation at depth 2 (above 'Jupiter'),
        strings at depth 3 (inside ['core']). Narrowest recorded block is
        the cited depth-2 entry. Inherits correctly.
      - ring_params fails: citation at depth 1 (above the assignment),
        strings inside depth-2 blocks. Narrowest recorded block is an
        uncited ring. Inherits nothing.

WHAT THIS PATCH DOES

    Two things, in two files.

    1. jupiter_visualization_shells.py -- a short repeat citation above
       each of the four ring keys, pointing at the full citation above
       ring_params. This moves the citation to the depth the resolver
       reads. Verified: Tier 1 133 -> 132, Tier 2 586 -> 587, exactly one
       finding moves (line 959) and nothing enters.

    2. provenance_scanner.py -- a diagnostic, not a behavior change.
       Scoring is untouched. The scanner now RECORDS two things and
       reports them in a new audit section:

         - shadowed strings: the narrowest containing block is uncited
           while an outer containing block is cited. Three other files
           carry this shape today with no live impact
           (comet_visualization_shells.py, planet_visualization_utilities.py,
           idealized_orbits.py); they are covered by the flat 60-line
           context window, which is why they audit clean. They are one
           edit away from not being.

         - deep citations: a dict nested 3+ levels deep that carries its
           own citation. The table cannot see these, so their strings
           would silently inherit the depth-2 citation instead of the
           nearer one. ZERO exist in the repo today. This is a tripwire
           for the day one appears.

    3. test_citation_inheritance.py -- four tests covering the above.

    Deliberately NOT done: adding repeat citations to the three latent
    files. They have no live mis-scoring, and editing three clean files
    to fix nothing is churn that can itself drift. The diagnostic makes
    the shape visible instead, which covers those three, every future
    instance, and the depth-3 case that no data fix would catch.

HOW TO RUN IT (VS Code)
    1. Save this file into the SAME folder as provenance_scanner.py
       (your palomas_orrery folder).
    2. Open it in VS Code.
    3. Click the Run button (the triangle, top right).

    Or from a terminal in that folder:  python patch_L174_citation_level_mismatch.py

WHAT YOU SHOULD SEE
    One "ok" line per edit, grouped by file, then "patch applied".

    If you see "ERROR:" or "ANCHOR FAIL" instead, NOTHING was written to
    ANY of the three files -- it is all-or-nothing across all of them, so
    it is always safe to re-check and retry.

AFTER IT RUNS
    python test_citation_inheritance.py     -> expect 20 passed, 0 failed
    python provenance_scanner.py .          -> expect Tier 1 132, Tier 2 587

    The audit will carry a new "CITATION LEVEL MISMATCH" section listing
    the shadowed blocks in the three latent files. That section appearing
    is the intended outcome, not a problem to fix.

Module updated: July 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGETS = {
    'jupiter_visualization_shells.py': '5b4404c6a7ae0437386ddc071ef22c2b',
    'provenance_scanner.py':           '421253ef8f75d943494d3955d285f856',
    'test_citation_inheritance.py':    '2a7d1e4d0eef1e5f1d31ac4ff8ec9318',
}


# ==================================================================
# FILE 1 -- jupiter_visualization_shells.py
# ==================================================================
# Bottom-up: thebe_gossamer (951) first, main_ring (907) last.

_REPEAT = (b"        # Source: NASA Jupiter Ring Fact Sheet; Galileo spacecraft"
           b" data (full citation above ring_params)\n")

J_EDITS = [
    ("J1 thebe_gossamer repeat citation",
     b"        'thebe_gossamer': {\n",
     _REPEAT + b"        'thebe_gossamer': {\n"),
    ("J2 amalthea_gossamer repeat citation",
     b"        'amalthea_gossamer': {\n",
     _REPEAT + b"        'amalthea_gossamer': {\n"),
    ("J3 halo_ring repeat citation",
     b"        'halo_ring': {\n",
     _REPEAT + b"        'halo_ring': {\n"),
    ("J4 main_ring repeat citation",
     b"        'main_ring': {\n",
     _REPEAT + b"        'main_ring': {\n"),
]


# ==================================================================
# FILE 2 -- provenance_scanner.py
# ==================================================================

S1_OLD = b"""# Blocks whose citation carries a scope declaration. Collected during
# extraction and reported after the scan so they stay visible rather
# than silently doing nothing.
SCOPE_DECLARED_BLOCKS = []"""

S1_NEW = b'''# Blocks whose citation carries a scope declaration. Collected during
# extraction and reported after the scan so they stay visible rather
# than silently doing nothing.
SCOPE_DECLARED_BLOCKS = []

# L-174 diagnostics. Neither affects scoring; both exist so that a
# citation pitched at the wrong LEVEL is visible instead of silent.
#
# Strict containment means the resolver reads exactly one block: the
# narrowest one containing the string. A citation written one level too
# far out is therefore invisible to it, and -- because the flat 60-line
# context window usually catches the string anyway -- the mismatch does
# not show up as a finding. It shows up as nothing at all, until someone
# moves a few lines and it quietly becomes a real gap.
#
# SHADOWED_STRINGS: narrowest containing block uncited, an outer
#   containing block cited. This is the ring_params shape.
# DEEP_CITATIONS: a dict nested 3+ levels deep carrying its own
#   citation. The block table records only depth 1 (the assignment) and
#   depth 2 (its direct dict-valued entries), so such a citation cannot
#   be reached and its strings would inherit the depth-2 citation
#   instead -- "innermost wins" failing one level down. None exist
#   today; this is a tripwire, not a backlog.
SHADOWED_STRINGS = []
DEEP_CITATIONS = []'''


S2_OLD = b"""    for block in blocks:
        if block['citation_text'] and SCOPE_DECLARATION_RE.search(
                block['citation_text']):
            SCOPE_DECLARED_BLOCKS.append((
                fname or '<unknown>', block['dict_name'], block['key'],
                block['start'], block['end'], block['citation_line']))

    return blocks"""

S2_NEW = b'''    for block in blocks:
        if block['citation_text'] and SCOPE_DECLARATION_RE.search(
                block['citation_text']):
            SCOPE_DECLARED_BLOCKS.append((
                fname or '<unknown>', block['dict_name'], block['key'],
                block['start'], block['end'], block['citation_line']))

    _record_deep_citations(tree, lines, fname)

    return blocks


def _record_deep_citations(tree, lines, fname=None):
    """Flag dicts nested 3+ deep that carry their own citation.

    build_citation_block_table records depth 1 and depth 2 only. A
    citation written above a depth-3 key is therefore unreachable: the
    resolver will hand that string the depth-2 citation instead, which
    is a real misattribution and invisible in the tier counts.

    Nothing in the repo triggers this today. It is recorded rather than
    handled because the honest fix is to extend the table, and doing
    that speculatively for a population of zero would add depth to the
    project's measurement instrument for no measured need.
    """
    def descend(dict_node, depth, name, keypath):
        for key, value in zip(dict_node.keys, dict_node.values):
            if key is None:
                continue
            if not (isinstance(key, ast.Constant)
                    and isinstance(key.value, str)):
                continue
            if not isinstance(value, ast.Dict):
                continue
            path = keypath + [key.value]
            if depth + 1 >= 3:
                cite_line, cite_text = citation_run_above(lines, key.lineno)
                if cite_text:
                    DEEP_CITATIONS.append((
                        fname or '<unknown>', name, list(path),
                        depth + 1, key.lineno, cite_line))
            descend(value, depth + 1, name, path)

    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1:
            continue
        if not isinstance(node.targets[0], ast.Name):
            continue
        if not isinstance(node.value, ast.Dict):
            continue
        descend(node.value, 1, node.targets[0].id, [])


def find_shadowing_block(blocks, line_start, line_end):
    """Return the outer cited block a string is shadowed FROM, or None.

    Shadowed means: the narrowest block containing this string has no
    citation, but some wider containing block does. The resolver
    correctly declines to inherit -- that strictness is what protects
    L-173 -- but the author almost certainly meant the outer citation to
    cover this content, so it is worth reporting.

    Reporting is all this does. Scoring is unchanged.
    """
    containing = [b for b in blocks
                  if b['start'] <= line_start and line_end <= b['end']]
    if len(containing) < 2:
        return None
    containing.sort(key=lambda b: (b['end'] - b['start'], b['start']))
    if containing[0]['citation_text']:
        return None
    for block in containing[1:]:
        if block['citation_text']:
            return block
    return None'''


S3_OLD = b"""        # Phase 1c: does an enclosing cited dict block cover this string?
        inherited_citation = None
        scope_declined = False
        if block_table:
            inherited_citation, scope_declined = resolve_block_citation(
                block_table, line_start, line_end)"""

S3_NEW = b"""        # Phase 1c: does an enclosing cited dict block cover this string?
        inherited_citation = None
        scope_declined = False
        if block_table:
            inherited_citation, scope_declined = resolve_block_citation(
                block_table, line_start, line_end)
            # L-174: diagnostic only, no effect on scoring.
            if inherited_citation is None and not scope_declined:
                shadowing = find_shadowing_block(
                    block_table, line_start, line_end)
                if shadowing is not None:
                    SHADOWED_STRINGS.append((
                        fname, line_start, shadowing['dict_name'],
                        shadowing['key'], shadowing['citation_line']))"""


S4_OLD = b"""    # Phase 1c: module-level collector, cleared per scan so a second
    # scan_project() call in the same process does not double-report.
    del SCOPE_DECLARED_BLOCKS[:]"""

S4_NEW = b"""    # Phase 1c / L-174: module-level collectors, cleared per scan so a
    # second scan_project() call in the same process does not
    # double-report.
    del SCOPE_DECLARED_BLOCKS[:]
    del SHADOWED_STRINGS[:]
    del DEEP_CITATIONS[:]"""


S5_OLD = b"""    if SCOPE_DECLARED_BLOCKS:
        print(f"{len(SCOPE_DECLARED_BLOCKS)} block(s) carry a scope-limited "
              f"citation -- inheritance declined, see audit")

    generate_report(all_units, consistent_dups, inconsistencies,
                    files_scanned, project_dir, output_path,
                    accepted_residuals=accepted_residuals,
                    coverage_gaps=coverage_gaps,
                    scope_declared=list(SCOPE_DECLARED_BLOCKS))"""

S5_NEW = b"""    if SCOPE_DECLARED_BLOCKS:
        print(f"{len(SCOPE_DECLARED_BLOCKS)} block(s) carry a scope-limited "
              f"citation -- inheritance declined, see audit")
    if SHADOWED_STRINGS:
        print(f"{len(SHADOWED_STRINGS)} string(s) sit in an uncited block "
              f"inside a cited one -- citation level mismatch, see audit")
    if DEEP_CITATIONS:
        print(f"WARNING: {len(DEEP_CITATIONS)} citation(s) sit on a dict "
              f"nested deeper than the block table reads -- see audit")

    generate_report(all_units, consistent_dups, inconsistencies,
                    files_scanned, project_dir, output_path,
                    accepted_residuals=accepted_residuals,
                    coverage_gaps=coverage_gaps,
                    scope_declared=list(SCOPE_DECLARED_BLOCKS),
                    shadowed=list(SHADOWED_STRINGS),
                    deep_citations=list(DEEP_CITATIONS))"""


S6_OLD = b"""                    accepted_residuals=None, coverage_gaps=None,
                    scope_declared=None):
    \"\"\"Write PROVENANCE_AUDIT.md.\"\"\""""

S6_NEW = b"""                    accepted_residuals=None, coverage_gaps=None,
                    scope_declared=None, shadowed=None,
                    deep_citations=None):
    \"\"\"Write PROVENANCE_AUDIT.md.\"\"\""""


S7_OLD = b"""    # ---- Scope-limited citations (L-156 Phase 1c) ----"""

S7_NEW = b'''    # ---- Citation level mismatch (L-174) ----
    if shadowed or deep_citations:
        out.append("## CITATION LEVEL MISMATCH -- diagnostic, no scoring effect")
        out.append("")
        out.append("Citations in this codebase attach to a block. The "
                   "resolver reads exactly one block per string: the "
                   "narrowest one containing it. A citation written one "
                   "level further out is invisible to it. Nothing below "
                   "is mis-scored today -- the flat 60-line context "
                   "window catches these independently, which is exactly "
                   "why the mismatch is easy to miss. Move a few lines "
                   "and it becomes a real gap with no warning.")
        out.append("")

    if shadowed:
        from collections import defaultdict as _dd
        grouped = _dd(list)
        for sfile, line, dname, dkey, cline in shadowed:
            grouped[sfile].append((line, dname, dkey, cline))
        out.append("### Shadowed strings")
        out.append("")
        out.append("The string sits in a block with no citation, inside a "
                   "block that has one. Fix by repeating a short citation "
                   "above the inner block's key, as done for "
                   "`ring_params` -- not by loosening the resolver, which "
                   "would clear the L-173 gaps by accident.")
        out.append("")
        out.append("| File | Line | Shadowed from | Its citation at |")
        out.append("|------|-----:|---------------|----------------:|")
        for sfile in sorted(grouped):
            for line, dname, dkey, cline in sorted(grouped[sfile]):
                label = f"`{dname}['{dkey}']`" if dkey else f"`{dname}`"
                out.append(f"| `{sfile}` | {line} | {label} | {cline} |")
        out.append("")

    if deep_citations:
        out.append("### Citations below the table's reach -- ACTION NEEDED")
        out.append("")
        out.append("A dict nested three or more levels deep carries its "
                   "own citation. The block table records only the "
                   "assignment and its direct entries, so this citation "
                   "cannot be reached and strings inside it will inherit "
                   "the shallower one instead -- a real misattribution "
                   "that will not show up in the tier counts. This list "
                   "was empty when the diagnostic was written; if it is "
                   "not empty now, the table needs extending.")
        out.append("")
        out.append("| File | Path | Depth | Key line | Citation at |")
        out.append("|------|------|------:|---------:|------------:|")
        for dfile, dname, path, depth, kline, cline in sorted(deep_citations):
            label = dname + ''.join(f"['{p}']" for p in path)
            out.append(f"| `{dfile}` | `{label}` | {depth} | {kline} "
                       f"| {cline} |")
        out.append("")

    if shadowed or deep_citations:
        out.append("---")
        out.append("")

    # ---- Scope-limited citations (L-156 Phase 1c) ----'''


S_EDITS = [
    ("S1 diagnostic collectors", S1_OLD, S1_NEW),
    ("S2 deep-citation scan + shadow finder", S2_OLD, S2_NEW),
    ("S3 record shadowed strings", S3_OLD, S3_NEW),
    ("S4 reset collectors per scan", S4_OLD, S4_NEW),
    ("S5 console lines + pass to report", S5_OLD, S5_NEW),
    ("S6 report signature", S6_OLD, S6_NEW),
    ("S7 citation-level-mismatch section", S7_OLD, S7_NEW),
]


# ==================================================================
# FILE 3 -- test_citation_inheritance.py
# ==================================================================

T1_OLD = b"""from provenance_scanner import (
    CITATION_LOOKBACK_BLOCK,
    SCOPE_DECLARATION_RE,
    SCOPE_DECLARED_BLOCKS,"""

T1_NEW = b"""from provenance_scanner import (
    CITATION_LOOKBACK_BLOCK,
    DEEP_CITATIONS,
    SCOPE_DECLARATION_RE,
    SCOPE_DECLARED_BLOCKS,
    find_shadowing_block,"""


T2_OLD = b"""# ============================================================
# RUNNER
# ============================================================"""

T2_NEW = b'''# ============================================================
# TESTS -- L-174 citation level mismatch
# ============================================================

def test_shadowing_is_detected():
    """The ring_params shape is reported even though it is not inherited."""
    blocks, _ = _table(CITED_OUTER_UNCITED_INNER)
    line = _string_line(CITED_OUTER_UNCITED_INNER, "3000 km")

    citation, _declined = resolve_block_citation(blocks, line, line)
    assert citation is None, "resolver must still decline to inherit"

    shadowing = find_shadowing_block(blocks, line, line)
    assert shadowing is not None, \\
        "shadowed string was not detected by the diagnostic"
    assert shadowing['citation_text'] is not None


def test_genuinely_uncited_is_not_reported_as_shadowed():
    """An uncited block with no cited ancestor is a real gap, not a mismatch.

    Guards the L-173 population against being reclassified as a level
    mismatch, which would make a missing source look like a formatting
    problem.
    """
    blocks, _ = _table(UNCITED_OUTER)
    line = _string_line(UNCITED_OUTER, "2000 km")
    assert find_shadowing_block(blocks, line, line) is None, \\
        "a genuinely uncited block was misreported as shadowed"


def test_cited_block_is_not_reported_as_shadowed():
    """A string that inherits normally is not flagged.

    Uses MULTILINE_CITATION, where the citation sits ABOVE the block key
    and so is reachable. (UNCITED_OUTER deliberately puts its comment
    INSIDE the block, which the resolver does not read -- that fixture
    tests a different thing.)
    """
    blocks, _ = _table(MULTILINE_CITATION)
    line = _string_line(MULTILINE_CITATION, "480 km")
    citation, _declined = resolve_block_citation(blocks, line, line)
    assert citation is not None, "fixture should inherit here"
    assert find_shadowing_block(blocks, line, line) is None, \
        "a normally-inheriting string was flagged as shadowed"


def test_deep_citation_tripwire():
    """A citation on a depth-3 dict is recorded, since the table cannot read it.

    This population is zero in the repo today. The test uses a fixture so
    it pins the detector rather than the current repo state.
    """
    source = \'\'\'\\
TABLE = {
    \'Body\': {
        # Source: a citation three levels down, below the table\'s reach
        \'layer\': {
            \'note\': "A claim of 55 km sits here.",
        },
    },
}
\'\'\'
    del DEEP_CITATIONS[:]
    _table(source)
    paths = [entry[2] for entry in DEEP_CITATIONS]
    assert any('layer' in p for p in paths), \\
        f"deep citation not recorded; collector holds {DEEP_CITATIONS}"
    del DEEP_CITATIONS[:]


# ============================================================
# RUNNER
# ============================================================'''


T3_OLD = b"""    test_live_jupiter_and_custom_jupiter_differ,
]"""

T3_NEW = b"""    test_live_jupiter_and_custom_jupiter_differ,
    test_shadowing_is_detected,
    test_genuinely_uncited_is_not_reported_as_shadowed,
    test_cited_block_is_not_reported_as_shadowed,
    test_deep_citation_tripwire,
]"""


T_EDITS = [
    ("T1 imports", T1_OLD, T1_NEW),
    ("T2 four L-174 tests", T2_OLD, T2_NEW),
    ("T3 register in runner", T3_OLD, T3_NEW),
]


ALL_EDITS = [
    ('jupiter_visualization_shells.py', J_EDITS),
    ('provenance_scanner.py', S_EDITS),
    ('test_citation_inheritance.py', T_EDITS),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    # ---- Load and guard every file BEFORE touching any of them. ----
    loaded = {}
    for name, expected in TARGETS.items():
        path = os.path.join(here, name)
        if not os.path.exists(path):
            print(f"ERROR: {name} not found next to this script.")
            print(f"       Looked in: {here}")
            print("       Move this script into your palomas_orrery "
                  "folder and run it again. Nothing written.")
            sys.exit(1)
        with open(path, 'rb') as f:
            content = f.read()
        actual = hashlib.md5(content).hexdigest()
        if actual != expected:
            print(f"ERROR: {name} is not the file this patch was built "
                  f"against.")
            print(f"       expected MD5 {expected}")
            print(f"       found    MD5 {actual}")
            print("       Nothing written to ANY file.")
            print()
            markers = {
                'provenance_scanner.py': b'SHADOWED_STRINGS',
                'jupiter_visualization_shells.py': b'full citation above ring_params',
                'test_citation_inheritance.py': b'test_deep_citation_tripwire',
            }
            if markers[name] in content:
                print("       Likely cause: this patch has ALREADY been "
                      "applied to this file.")
                print("       Check with: python "
                      "test_citation_inheritance.py")
            elif b'\r\n' in content:
                print("       Likely cause: Windows CRLF line endings; "
                      "this patch was built against the LF copy in the "
                      "repo.")
            else:
                print("       Likely cause: the file changed after this "
                      "patch was built. Re-pull and rebuild.")
            sys.exit(1)
        loaded[name] = content

    # ---- Verify every anchor in every file before writing anything. ----
    for name, edits in ALL_EDITS:
        content = loaded[name]
        for label, old, _new in edits:
            count = content.count(old)
            if count != 1:
                print(f"ANCHOR FAIL [{name} :: {label}]: expected exactly "
                      f"1 match, found {count}.")
                print("       Nothing written to ANY file.")
                sys.exit(1)

    # ---- Apply. ----
    patched = {}
    for name, edits in ALL_EDITS:
        content = loaded[name]
        print(f"{name}")
        for label, old, new in edits:
            content = content.replace(old, new, 1)
            print(f"  ok  {label}")
        try:
            content.decode('ascii')
        except UnicodeDecodeError as exc:
            print(f"ERROR: patched {name} is not pure ASCII ({exc}). "
                  "Nothing written to ANY file.")
            sys.exit(1)
        if b'\r\n' in content:
            print(f"ERROR: patched {name} contains CRLF. Nothing written "
                  "to ANY file.")
            sys.exit(1)
        patched[name] = content

    for name, content in patched.items():
        with open(os.path.join(here, name), 'wb') as f:
            f.write(content)

    print()
    print(f"patch applied ({len(patched)} files)")
    print()
    print("Next:")
    print("  python test_citation_inheritance.py   -> expect 20 passed")
    print("  python provenance_scanner.py .        -> expect Tier 1 132, "
          "Tier 2 587")
    print()
    print("The audit will gain a CITATION LEVEL MISMATCH section listing")
    print("the three latent files. That section appearing is the point.")


if __name__ == '__main__':
    main()
