"""
patch_pinned_values_bleed.py

Unify the two citation-detection rules in provenance_scanner.py, so
build_pinned_values() stops using a window that can bleed.

Built on 6ce6136f64282c9670b265c89228c210f8ffaa73
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT THIS FIXES

    build_pinned_values() decides whether a constant in constants_new.py
    is cited by searching a flat window of 10 lines above and 5 below the
    assignment. In a densely packed file that window reaches past the
    constant it is asking about: an uncited constant sitting near a cited
    one picks up the neighbour's citation and enters the pinned set. From
    there Option A hands display strings V_SOURCED credit on the strength
    of a citation that was never written for that value.

    Since today's 1d build there are TWO functions in this file deciding
    the same question -- "does this constant carry its own citation" --
    by two different rules. build_cited_constant_names() reads only the
    contiguous comment run physically touching the assignment. That is
    the correct rule, and the divergence between them is itself the
    problem: whichever one is read next becomes "how the scanner decides
    citation," and they disagree.

    So this patch does not copy the good rule into the second function.
    It extracts ONE implementation, constant_has_own_citation(), and
    routes both callers through it. One predicate, one place to fix it,
    no way for them to drift apart again.

MEASURED IMPACT AT HEAD: NONE. READ THIS BEFORE RUNNING IT.

    The build prompt expects the pinned set to shrink and some display
    strings to lose V_SOURCED and move toward Tier 1. Measured at HEAD,
    that does not happen, and it is worth knowing why before the absence
    of a delta reads as the patch having failed.

    Every one of the 34 numeric constants in constants_new.py carries its
    own citation. Compared directly:

        build_pinned_values()         -> 58 pinned values
        build_cited_constant_names()  -> 34 names, 58 pinned values
        difference                    -> none, in either direction

    The window has nothing to bleed ONTO, because there is no uncited
    numeric constant in the file for it to reach. The flaw is real as a
    mechanism and latent in the data.

    So this is a defensive fix, not a corrective one. It is still worth
    making: constants_new.py grows, and the first numeric constant added
    without its own citation next to a cited one would enter the pinned
    set silently -- no error, no finding, just slightly wrong scoring
    everywhere Option A fires. The unification is the durable part.

    Expect the scan to be BYTE-IDENTICAL after this patch. That is the
    success condition here, not a warning sign.

HOW TO RUN IT (VS Code)
    1. Save this file into the SAME folder as provenance_scanner.py.
    2. Open it in VS Code.
    3. Click the Run button (the triangle, top right).

    Or from a terminal in that folder:  python patch_pinned_values_bleed.py

WHAT YOU SHOULD SEE
    One "ok" line per edit, then "patch applied". Any failure writes
    nothing to either file.

AFTER IT RUNS
    python test_provenance_1d.py          -> expect 20 passed
    python test_citation_inheritance.py   -> expect 20 passed
    python test_constants_provenance.py   -> expect 73 passed
    python provenance_scanner.py .        -> expect NO CHANGE:
                                             Tier 1 171, Tier 2 646,
                                             Tier 3 62, Tier 4 2

Module updated: July 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGETS = {
    'provenance_scanner.py': '5a00ac3cad8565f7a327265ccb63bd6a',
    'test_provenance_1d.py': 'f79cc1df28a95083ca54749f479cce3d',
}


# ==================================================================
# FILE 1 -- provenance_scanner.py
# ==================================================================
# Bottom-up: build_pinned_values() (line ~1618) before
# build_cited_constant_names() (line ~1482) before the new shared
# helper, which is inserted above both.

# ---- E1: build_pinned_values() uses the shared predicate ----

S1_OLD = b"""        ln = node.lineno
        context = ''.join(lines_c[max(0, ln - 1 - 10):ln + 5])
        if SOURCE_RE.search(context):
            # Store at multiple precisions to match how hover text rounds
            for prec in (0, 1, 2, 3):
                pinned.add(round(num, prec))

    return pinned"""

S1_NEW = b"""        # Was a flat window of 10 lines above and 5 below, which could
        # reach past this constant onto a neighbour's citation. Now the
        # same predicate build_cited_constant_names() uses, so the two
        # cannot disagree about what "cited" means.
        if constant_has_own_citation(lines_c, node.lineno, SOURCE_RE):
            # Store at multiple precisions to match how hover text rounds
            for prec in (0, 1, 2, 3):
                pinned.add(round(num, prec))

    return pinned"""


# ---- E2: build_cited_constant_names() uses the shared predicate ----

S2_OLD = b"""        # Find THIS constant's own citation, in either of the two
        # conventions the file uses.
        #
        # build_pinned_values() uses a flat window of 10 lines above and
        # 5 below, which bleeds: in a densely packed file a constant
        # with no citation of its own picks up a neighbour's, and a copy
        # of it would then be reported as a shadow of something that was
        # never actually cited.
        #
        # constants_new.py mostly writes the citation BELOW the
        # assignment:
        #     KM_PER_AU = 149597870.7
        #     # Source: IAU 2012 Resolution B2
        # while the rest of the codebase writes it above. Both are
        # accepted, but only as a contiguous comment run touching the
        # assignment -- a blank line ends it, which is what stops the
        # bleed.
        cited = False

        idx = node.lineno          # 0-based index of the line BELOW
        while idx < len(lines_c) and lines_c[idx].lstrip().startswith('#'):
            if source_re.search(lines_c[idx]):
                cited = True
                break
            idx += 1

        if not cited:
            idx = node.lineno - 2  # 0-based index of the line ABOVE
            while idx >= 0:
                line = lines_c[idx]
                if source_re.search(line):
                    cited = True
                    break
                if line.strip() and not line.lstrip().startswith('#'):
                    break
                idx -= 1

        if cited:
            named[target.id] = num
    return named"""

S2_NEW = b"""        if constant_has_own_citation(lines_c, node.lineno, source_re):
            named[target.id] = num
    return named"""


# ---- E3: the shared predicate ----

S3_OLD = b"""def build_cited_constant_names(project_dir):"""

S3_NEW = b'''def constant_has_own_citation(lines_c, lineno, source_re):
    """Does the constant assigned at `lineno` carry its OWN citation?

    Single source of truth for this question. Both build_pinned_values()
    and build_cited_constant_names() route through here, because two
    functions in one file answering "is this cited" by different rules
    is how the scanner ends up disagreeing with itself.

    The rule is CONTIGUITY, not distance. A citation counts only if it
    sits in a comment run physically touching the assignment -- a blank
    line ends the run. Distance windows do not work here: a window wide
    enough to catch a real citation is also wide enough to reach the
    NEXT constant's citation, and then an uncited value silently
    inherits provenance it never had.

    Both conventions in this codebase are accepted, because both are in
    use. constants_new.py writes the citation BELOW the assignment:

        KM_PER_AU = 149597870.7
        # Source: IAU 2012 Resolution B2

    while the rest of the repo writes it above. Below is checked first,
    since that is the convention of the file this predicate is applied
    to most often.

    `lines_c` is the file's lines with line endings kept; `lineno` is the
    1-based AST line number; `source_re` is the caller's citation
    pattern.
    """
    # Below: a comment run starting on the very next line. No blank may
    # intervene -- that is what keeps the next constant's citation out.
    idx = lineno
    while idx < len(lines_c) and lines_c[idx].lstrip().startswith('#'):
        if source_re.search(lines_c[idx]):
            return True
        idx += 1

    # Above: walk up through comments and blanks, stopping at the first
    # line of code, which is the previous assignment.
    idx = lineno - 2
    while idx >= 0:
        line = lines_c[idx]
        if source_re.search(line):
            return True
        if line.strip() and not line.lstrip().startswith('#'):
            break
        idx -= 1

    return False


def build_cited_constant_names(project_dir):'''


# ---- E4: credit line ----

S4_OLD = b"""Module updated: July 2026 with Anthropic's Claude Opus 5 (L-156 Phase 1d/1e:"""

S4_NEW = b"""Module updated: July 2026 with Anthropic's Claude Opus 5 (constant_has_own_
citation extracted as the single citation predicate; build_pinned_values no
longer uses a distance window that could inherit a neighbour's citation).

Module updated: July 2026 with Anthropic's Claude Opus 5 (L-156 Phase 1d/1e:"""


S_EDITS = [
    ("S1 build_pinned_values uses shared predicate", S1_OLD, S1_NEW),
    ("S2 build_cited_constant_names uses shared predicate", S2_OLD, S2_NEW),
    ("S3 constant_has_own_citation", S3_OLD, S3_NEW),
    ("S4 module credit line", S4_OLD, S4_NEW),
]


# ==================================================================
# FILE 2 -- test_provenance_1d.py
# ==================================================================

T1_OLD = b"""from provenance_scanner import (
    SHADOW_CONSTANTS,
    SHADOW_DERIVED_MIN_MAGNITUDE,
    build_cited_constant_names,"""

T1_NEW = b"""from provenance_scanner import (
    SHADOW_CONSTANTS,
    SHADOW_DERIVED_MIN_MAGNITUDE,
    build_cited_constant_names,
    build_pinned_values,
    constant_has_own_citation,"""


T2_OLD = b"""# ============================================================
# RUNNER
# ============================================================"""

T2_NEW = b'''# ============================================================
# TESTS -- the shared citation predicate
# ============================================================

import re as _re

_SRC_RE = _re.compile(r'#\\s*[Ss]ource\\s*:', _re.IGNORECASE)


def _lines(text):
    return text.splitlines(keepends=True)


def test_citation_below_assignment_counts():
    """constants_new.py's convention: citation on the following line."""
    src = _lines('X = 1.0\\n# Source: a real reference\\n')
    assert constant_has_own_citation(src, 1, _SRC_RE)


def test_citation_above_assignment_counts():
    """The rest of the codebase's convention: citation above."""
    src = _lines('# Source: a real reference\\nX = 1.0\\n')
    assert constant_has_own_citation(src, 2, _SRC_RE)


def test_blank_line_ends_the_run_below():
    """A blank line stops the search, so the NEXT constant's citation
    is not inherited.

    This is the bleed the predicate exists to prevent. With a distance
    window instead of contiguity, Y below would be scored as cited on
    the strength of Z's citation.
    """
    src = _lines('Y = 2.0\\n'
                 '\\n'
                 '# Source: this belongs to Z, not Y\\n'
                 'Z = 3.0\\n')
    assert not constant_has_own_citation(src, 1, _SRC_RE), \\
        "Y inherited the citation belonging to Z"
    assert constant_has_own_citation(src, 4, _SRC_RE)


def test_preceding_code_ends_the_run_above():
    """Walking up stops at the previous assignment."""
    src = _lines('# Source: belongs to A\\n'
                 'A = 1.0\\n'
                 'B = 2.0\\n')
    assert constant_has_own_citation(src, 2, _SRC_RE)
    assert not constant_has_own_citation(src, 3, _SRC_RE), \\
        "B inherited the citation belonging to A"


def test_both_pinned_builders_agree():
    """The two callers must not diverge again.

    They answer the same question and now share one implementation. If
    this ever fails, one of them has grown its own rule back.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.join(here, 'constants_new.py')):
        print("    (skipped -- constants_new.py not found)")
        return

    pinned = build_pinned_values(here)
    named = build_cited_constant_names(here)
    from_names = set()
    for value in named.values():
        for prec in (0, 1, 2, 3):
            from_names.add(round(value, prec))

    assert pinned == from_names, (
        f"the two citation rules disagree: "
        f"{len(pinned - from_names)} only in build_pinned_values, "
        f"{len(from_names - pinned)} only in build_cited_constant_names")


# ============================================================
# RUNNER
# ============================================================'''


T3_OLD = b"""    test_tier_labels_make_no_blanket_residual_claim,
]"""

T3_NEW = b"""    test_tier_labels_make_no_blanket_residual_claim,
    test_citation_below_assignment_counts,
    test_citation_above_assignment_counts,
    test_blank_line_ends_the_run_below,
    test_preceding_code_ends_the_run_above,
    test_both_pinned_builders_agree,
]"""


T4_OLD = b"""print("Phase 1d/1e recognition tests (L-156)")"""

T4_NEW = b"""print("Phase 1d/1e recognition tests (L-156) + citation predicate")"""


T_EDITS = [
    ("T1 imports", T1_OLD, T1_NEW),
    ("T2 five predicate tests", T2_OLD, T2_NEW),
    ("T3 register in runner", T3_OLD, T3_NEW),
    ("T4 header line", T4_OLD, T4_NEW),
]


ALL_EDITS = [
    ('provenance_scanner.py', S_EDITS),
    ('test_provenance_1d.py', T_EDITS),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))

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
                'provenance_scanner.py': b'constant_has_own_citation',
                'test_provenance_1d.py': b'test_both_pinned_builders_agree',
            }
            if markers[name] in content:
                print("       Likely cause: this patch has ALREADY been "
                      "applied to this file.")
            elif b'\r\n' in content:
                print("       Likely cause: Windows CRLF line endings; "
                      "this patch was built against the LF copy in the "
                      "repo.")
            else:
                print("       Likely cause: the file changed after this "
                      "patch was built. Re-pull and rebuild.")
            sys.exit(1)
        loaded[name] = content

    for name, edits in ALL_EDITS:
        content = loaded[name]
        for label, old, _new in edits:
            count = content.count(old)
            if count != 1:
                print(f"ANCHOR FAIL [{name} :: {label}]: expected exactly "
                      f"1 match, found {count}.")
                print("       Nothing written to ANY file.")
                sys.exit(1)

    patched = {}
    for name, edits in ALL_EDITS:
        content = loaded[name]
        print(f"{name}")
        for label, old, new in edits:
            content = content.replace(old, new, 1)
            print(f"  ok  {label}")
        before = sum(1 for byte in loaded[name] if byte > 127)
        after = sum(1 for byte in content if byte > 127)
        if after > before:
            print(f"ERROR: patch introduces {after - before} non-ASCII "
                  f"byte(s) into {name}. Nothing written to ANY file.")
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
    print("  python test_provenance_1d.py    -> expect 20 passed")
    print("  python provenance_scanner.py .")
    print()
    print("The scan should be UNCHANGED -- Tier 1 171, Tier 2 646.")
    print("Every constant in constants_new.py already carries its own")
    print("citation, so the old window had nothing to bleed onto. That")
    print("is the expected result, not a failed patch.")


if __name__ == '__main__':
    main()
