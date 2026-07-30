"""
test_citation_inheritance.py - Regression tests for citation-block inheritance.

Pins the Phase 1c mechanism in provenance_scanner.py (ledger L-156 Gap
item 6): a display string inside a dict block that carries its own
citation inherits that citation at V_SOURCED, and -- more importantly --
a string inside an UNCITED block inherits nothing.

Run from the project directory:
    python test_citation_inheritance.py

Exits 0 if all tests pass, non-zero on any failure.

Why these particular tests:
    The load-bearing behavior here is a NEGATIVE. Inheritance that works
    is visible in the audit totals; inheritance that over-reaches is not
    -- it shows up as findings quietly disappearing from Tier 1 while
    the block they came from still has no source. The cross-dict and
    uncited-block tests exist because a name-keyed or outward-searching
    implementation would pass every other check and fail these silently.

Design (matches test_constants_provenance.py):
    - Plain assert functions, no pytest/unittest dependency
    - Synthetic source fixtures for mechanism tests, so the tests do not
      break when shell_configs.py is edited
    - A few live-repo structural tests that assert relationships rather
      than hardcoded line numbers
    - main() runs all tests and prints a pass/fail summary

Module created: July 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""

import ast
import os
import sys
import traceback

from provenance_scanner import (
    CITATION_LOOKBACK_BLOCK,
    SCOPE_DECLARATION_RE,
    SCOPE_DECLARED_BLOCKS,
    V_SOURCED,
    V_RECALLED,
    build_citation_block_table,
    citation_run_above,
    resolve_block_citation,
)


# ============================================================
# HELPERS
# ============================================================

def _table(source):
    """Build a citation block table from a source string."""
    lines = source.splitlines(keepends=True)
    tree = ast.parse(source)
    return build_citation_block_table(tree, lines, 'fixture.py'), lines


def _string_line(source, needle):
    """1-based line number of the first line containing `needle`."""
    for i, line in enumerate(source.splitlines(), start=1):
        if needle in line:
            return i
    raise AssertionError(f"fixture is missing {needle!r}")


# ============================================================
# FIXTURES
# ============================================================

TWO_DICTS = '''\
# Source: Citation ALPHA for the outer table
OUTER_A = {
    # Source: Citation ONE for Jupiter
    'Jupiter': {
        'note': "Jupiter has a radius of 71492 km here.",
    },
    'Pluto': {
        'note': "Pluto has a radius of 1188 km here.",
    },
}

CUSTOM_B = {
    # Source: Citation TWO for Jupiter
    'Jupiter': {
        'note': "Jupiter magnetosphere extends 7000000 km here.",
    },
}
'''

UNCITED_OUTER = '''\
TABLE = {
    'Cited': {
        # Source: Citation for the cited block only
        'note': "This block cites 1000 km of something.",
    },
    'Uncited': {
        'note': "This block cites nothing, 2000 km notwithstanding.",
    },
}
'''

CITED_OUTER_UNCITED_INNER = '''\
# Source: Citation on the OUTER assignment
TABLE = {
    'Uncited': {
        'note': "Inner block has no citation of its own, 3000 km.",
    },
}
'''

MULTILINE_CITATION = '''\
TABLE = {
    # Source: Weber et al. (2011), "Seismic Detection of the Lunar Core";
    #         NASA Moon Fact Sheet; Apollo Seismic Experiment reports;
    #         Draper (1847).
    # Verified: April 2026 provenance audit.
    'Moon': {
        'note': "The Moon core boundary sits at 480 km radius.",
    },
}
'''

SCOPE_LIMITED = '''\
def build():
    # Source: NASA Ring Fact Sheet; Galileo spacecraft data
    # Verified: April 2026 via Gemini fact-check
    # Scope of the above citation: ring geometry only (inner/outer radius,
    # thickness). Colors below are selected by the developer.
    ring_params = {
        'main_ring': {
            'note': "The main ring extends to 129000 km outward.",
        },
    }
    return ring_params
'''

# Same scope declaration, but the claim sits DIRECTLY in the declared
# block rather than in a nested entry. This is the shape that exercises
# the resolver's decline path; the nested shape above is stopped one
# level earlier by the uncited inner block.
SCOPE_LIMITED_FLAT = '''\
def build():
    # Source: NASA Ring Fact Sheet; Galileo spacecraft data
    # Scope of the above citation: ring geometry only (inner/outer radius,
    # thickness). Colors below are selected by the developer.
    ring_params = {
        'note': "The main ring extends to 129000 km outward.",
    }
    return ring_params
'''

FAR_CITATION = '''\
# Source: Citation that sits far above the table
{padding}
TABLE = {{
    'Body': {{
        'note': "A claim of 500 km lives here.",
    }},
}}
'''


# ============================================================
# TESTS -- the load-bearing negatives
# ============================================================

def test_no_cross_dict_inheritance():
    """Same key in two dicts must resolve to two different citations.

    This is the test the predesign explicitly asked for. A name-keyed
    implementation ('Jupiter' -> citation) would merge these and the bug
    would be invisible in the audit totals, because the finding count
    would be identical either way -- only the attributed source changes.
    """
    blocks, _ = _table(TWO_DICTS)

    outer = [b for b in blocks
             if b['dict_name'] == 'OUTER_A' and b['key'] == 'Jupiter'][0]
    custom = [b for b in blocks
              if b['dict_name'] == 'CUSTOM_B' and b['key'] == 'Jupiter'][0]

    assert 'ONE' in outer['citation_text'], \
        f"OUTER_A['Jupiter'] got: {outer['citation_text']!r}"
    assert 'TWO' in custom['citation_text'], \
        f"CUSTOM_B['Jupiter'] got: {custom['citation_text']!r}"
    assert outer['citation_text'] != custom['citation_text'], \
        "cross-dict citation merge -- the two Jupiters share a citation"

    # Spans must be disjoint, which is what makes the merge impossible.
    assert outer['end'] < custom['start'], \
        "the two Jupiter blocks overlap; range keying cannot separate them"


def test_uncited_block_inherits_nothing():
    """A block with no citation must resolve to None, not to a sibling."""
    blocks, _ = _table(UNCITED_OUTER)
    line = _string_line(UNCITED_OUTER, "2000 km")

    citation, declined = resolve_block_citation(blocks, line, line)
    assert citation is None, \
        f"uncited block inherited: {citation!r}"
    assert declined is False


def test_no_outward_fallback_to_cited_parent():
    """An uncited inner block must NOT reach its cited parent's citation.

    This is the invariant the whole mechanism exists to protect. If this
    test fails, the genuinely uncited blocks tracked as L-173 will
    silently clear the moment anyone adds a citation above the outer
    dict, and their real problem -- a missing source -- becomes invisible.
    """
    blocks, _ = _table(CITED_OUTER_UNCITED_INNER)
    line = _string_line(CITED_OUTER_UNCITED_INNER, "3000 km")

    citation, declined = resolve_block_citation(blocks, line, line)
    assert citation is None, \
        (f"outward fallback fired: uncited inner block inherited "
         f"{citation!r} from its cited parent")


def test_scope_declaration_declines():
    """A scope-limited citation must decline rather than inherit.

    Uses the flat shape, where the claim sits directly in the declared
    block, so the resolver actually reaches the scope marker.
    """
    blocks, _ = _table(SCOPE_LIMITED_FLAT)
    line = _string_line(SCOPE_LIMITED_FLAT, "129000 km")

    citation, declined = resolve_block_citation(blocks, line, line)
    assert citation is None, \
        f"inherited past an explicit scope declaration: {citation!r}"
    assert declined is True, \
        "scope declaration was not detected"


def test_scope_declared_block_is_flagged_even_when_unreached():
    """A scope-limited block is recorded whether or not a string reaches it.

    In the live repo the claim sits inside an UNCITED nested entry, so
    strict containment stops one level below the scope declaration and
    the resolver never sees it. The block must still be flagged, or the
    author's explicit limit would vanish from the audit entirely.
    """
    del SCOPE_DECLARED_BLOCKS[:]
    blocks, _ = _table(SCOPE_LIMITED)
    line = _string_line(SCOPE_LIMITED, "129000 km")

    citation, declined = resolve_block_citation(blocks, line, line)
    assert citation is None, \
        f"nested claim under a scope-limited block inherited {citation!r}"
    assert declined is False, \
        "expected the uncited inner block to stop resolution first"

    names = [entry[1] for entry in SCOPE_DECLARED_BLOCKS]
    assert 'ring_params' in names, \
        f"scope-limited block was not flagged; collector holds {names}"
    del SCOPE_DECLARED_BLOCKS[:]


# ============================================================
# TESTS -- capture and containment
# ============================================================

def test_multiline_citation_captured_whole():
    """The full contiguous comment run is captured, not the matched line.

    has_citation() matches per line. For a multi-line citation the first
    match is often a continuation line, so recording only that line drops
    the sources named above and below it.
    """
    blocks, _ = _table(MULTILINE_CITATION)
    moon = [b for b in blocks if b['key'] == 'Moon'][0]

    text = moon['citation_text']
    assert text is not None, "Moon block found no citation"
    assert 'Weber' in text, "citation run truncated at the top"
    assert 'Draper' in text, "citation run truncated in the middle"
    assert 'Verified' in text, "citation run truncated at the bottom"


def test_narrowest_containing_block_wins():
    """Nested blocks resolve to the innermost citation, not the outer one."""
    source = '''\
# Source: OUTER citation
TABLE = {
    # Source: INNER citation
    'Body': {
        'note': "A claim of 900 km sits here.",
    },
}
'''
    blocks, _ = _table(source)
    line = _string_line(source, "900 km")

    citation, _declined = resolve_block_citation(blocks, line, line)
    assert citation is not None, "nested cited block inherited nothing"
    assert 'INNER' in citation, \
        f"resolved to the outer citation instead of the inner: {citation!r}"


def test_function_local_dicts_are_seen():
    """ast.walk must reach dicts nested inside functions.

    jupiter_visualization_shells.py's ring_params is function-local. A
    module-level-only walk misses it entirely, which is why the original
    measurement of this gap undercounted.
    """
    blocks, _ = _table(SCOPE_LIMITED)
    names = {b['dict_name'] for b in blocks}
    assert 'ring_params' in names, \
        f"function-local dict not found; saw {names}"


def test_string_outside_any_block_inherits_nothing():
    """A string with no containing dict block resolves to None."""
    source = '''\
# Source: A module-level citation
NOTE = "A loose claim of 42 km with no containing block."

TABLE = {
    'Body': {
        # Source: block citation
        'note': "Contained claim of 43 km.",
    },
}
'''
    blocks, _ = _table(source)
    line = _string_line(source, "42 km")
    citation, declined = resolve_block_citation(blocks, line, line)
    assert citation is None, \
        f"a string outside every block inherited {citation!r}"
    assert declined is False


# ============================================================
# TESTS -- lookback tuning
# ============================================================

def test_lookback_constant_is_pinned():
    """The lookback is a named constant, not a literal, and is >= 15.

    15 is required to reach ring_params' citation (9 lines above its
    assignment, with the comment run above that). Below 14 the Jupiter
    case is not even detected as scope-limited.
    """
    assert isinstance(CITATION_LOOKBACK_BLOCK, int)
    assert CITATION_LOOKBACK_BLOCK >= 15, \
        f"lookback dropped to {CITATION_LOOKBACK_BLOCK}; the Jupiter case needs 14+"


def test_lookback_does_not_reach_past_its_limit():
    """A citation beyond the lookback window is not picked up."""
    padding = '\n'.join('# filler comment line' for _ in range(60))
    source = FAR_CITATION.format(padding=padding)
    blocks, _ = _table(source)
    body = [b for b in blocks if b['key'] == 'Body'][0]
    outer = [b for b in blocks if b['key'] is None][0]

    assert body['citation_text'] is None, \
        "block picked up a citation far outside the lookback window"
    assert outer['citation_text'] is None, \
        "assignment picked up a citation far outside the lookback window"


def test_citation_run_stops_at_code():
    """Scanning upward stops at the first non-comment, non-blank line."""
    source = '''\
# Source: A citation belonging to something else
PREVIOUS = 1

TABLE = {
    'Body': {
        'note': "A claim of 77 km here.",
    },
}
'''
    lines = source.splitlines(keepends=True)
    decl = _string_line(source, "TABLE = {")
    cite_line, cite_text = citation_run_above(lines, decl)
    assert cite_line is None and cite_text is None, \
        "walked past a code line and stole a previous block's citation"


# ============================================================
# TESTS -- scoring contract
# ============================================================

def test_scope_pattern_matches_the_live_form():
    """The scope marker matches the wording actually used in the repo."""
    live = ("# Scope of the above citation: ring geometry only "
            "(inner/outer radius, thickness).")
    assert SCOPE_DECLARATION_RE.search(live)


def test_inheritance_lands_on_v_sourced_not_lower():
    """Inheriting is not clearing: V_SOURCED, never V_FETCHED/V_CROSS_CHECKED.

    Guards the rung itself. If a later change promotes inherited strings
    to V_CROSS_CHECKED, a citation nobody blind-checked would be scored
    as though somebody had.
    """
    assert V_SOURCED == 3, f"V_SOURCED moved to {V_SOURCED}"
    assert V_RECALLED == 4
    assert V_SOURCED < V_RECALLED, \
        "inheriting must reduce vulnerability, not raise it"


# ============================================================
# TESTS -- live repo structure (relationships, not line numbers)
# ============================================================

def test_live_shell_configs_uncited_blocks_still_uncited():
    """The L-173 blocks must remain uninherited in the live file.

    Asserts the relationship, not a count, so this does not become a
    tripwire the moment those blocks get their real citations. When
    L-173 is resolved these blocks SHOULD become cited -- at which point
    this test is expected to be updated deliberately, not silently.
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'shell_configs.py')
    if not os.path.exists(path):
        print("    (skipped -- shell_configs.py not found)")
        return

    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    with open(path, 'rb') as f:
        tree = ast.parse(f.read())
    blocks = build_citation_block_table(tree, lines, 'shell_configs.py')

    by_key = {}
    for b in blocks:
        if b['kind'] == 'entry':
            by_key[(b['dict_name'], b['key'])] = b

    known_uncited = [('SHELL_CONFIGS', 'Pluto'), ('SHELL_CONFIGS', 'Venus'),
                     ('SHELL_CONFIGS', 'Eris'), ('SHELL_CONFIGS', 'Mars'),
                     ('CUSTOM_SHELLS', 'Mercury')]
    for key in known_uncited:
        block = by_key.get(key)
        if block is None:
            continue
        mid = (block['start'] + block['end']) // 2
        citation, _declined = resolve_block_citation(blocks, mid, mid)
        assert citation is None, \
            (f"{key[0]}['{key[1]}'] now inherits {citation!r} -- if this is "
             f"a real citation, update this test deliberately; if not, the "
             f"resolver is over-reaching")


def test_live_jupiter_and_custom_jupiter_differ():
    """Live cross-dict check against the real shell_configs.py."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'shell_configs.py')
    if not os.path.exists(path):
        print("    (skipped -- shell_configs.py not found)")
        return

    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    with open(path, 'rb') as f:
        tree = ast.parse(f.read())
    blocks = build_citation_block_table(tree, lines, 'shell_configs.py')

    pairs = {}
    for b in blocks:
        if b['kind'] == 'entry' and b['key'] == 'Jupiter':
            pairs[b['dict_name']] = b

    if len(pairs) < 2:
        print("    (skipped -- Jupiter not present in both dicts)")
        return

    texts = [b['citation_text'] for b in pairs.values()]
    assert all(t is not None for t in texts), \
        "a live Jupiter block lost its citation"
    assert texts[0] != texts[1], \
        "live cross-dict merge: both Jupiter blocks share one citation"


# ============================================================
# RUNNER
# ============================================================

TESTS = [
    test_no_cross_dict_inheritance,
    test_uncited_block_inherits_nothing,
    test_no_outward_fallback_to_cited_parent,
    test_scope_declaration_declines,
    test_scope_declared_block_is_flagged_even_when_unreached,
    test_multiline_citation_captured_whole,
    test_narrowest_containing_block_wins,
    test_function_local_dicts_are_seen,
    test_string_outside_any_block_inherits_nothing,
    test_lookback_constant_is_pinned,
    test_lookback_does_not_reach_past_its_limit,
    test_citation_run_stops_at_code,
    test_scope_pattern_matches_the_live_form,
    test_inheritance_lands_on_v_sourced_not_lower,
    test_live_shell_configs_uncited_blocks_still_uncited,
    test_live_jupiter_and_custom_jupiter_differ,
]


def main():
    print("=" * 70)
    print("Citation-block inheritance tests (L-156 Phase 1c)")
    print("=" * 70)

    passed = 0
    failures = []

    for test in TESTS:
        name = test.__name__
        try:
            test()
            passed += 1
            print(f"  PASS  {name}")
        except AssertionError as exc:
            failures.append((name, str(exc)))
            print(f"  FAIL  {name}")
        except Exception as exc:              # noqa: BLE001
            failures.append((name, f"Unexpected {type(exc).__name__}: {exc}"))
            print(f"  ERROR {name}")
            traceback.print_exc()

    print("=" * 70)
    print(f"Results: {passed} passed, {len(failures)} failed, "
          f"{len(TESTS)} total")

    if failures:
        print("\nFailure details:")
        for name, msg in failures:
            print(f"\n  {name}:")
            print(f"    {msg}")
        return 1

    print("\nAll citation-inheritance tests passed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
