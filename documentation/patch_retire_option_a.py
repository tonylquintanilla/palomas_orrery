"""
patch_retire_option_a.py

Retire Option A (design handoff D8.5), and one more instance of the same
failure class found while auditing for it.

Built on adc9b20d2e6533c25544d565430336f835e87a48
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT THIS REMOVES

    (1) OPTION A -- credit by numeric coincidence.

    score_unit() granted V_SOURCED to an uncited display string whenever
    all of its numeric claims matched values pinned from
    constants_new.py. That is credit without provenance: a match proves
    two numbers are equal, not that anyone consulted a source. The
    scanner exists to make unsourced claims visible, and this made 26 of
    them invisible.

    Suspicious value matches still have a home -- the shadow-constant
    detector reports them as a diagnostic. The difference matters:
    advisory tells you to go look, exculpatory tells you not to bother.

    (2) STALE-MARKER CREDIT -- the same failure, found while auditing
        for others, and arguably worse.

    The same function granted V_SOURCED to a unit with NO citation at
    all whenever its text matched a STALE pattern -- "as of 2024",
    "Planned", "Currently operating". The reason string it wrote was
    literally "No source, contains date-sensitive claims": the scanner
    saying in one breath that a claim has no source and scoring it as
    though it had one. A staleness marker is evidence a claim will go
    out of date, not evidence anyone sourced it. 15 findings were
    credited this way.

    Both were introduced before the V-ladder existed, when V_SOURCED
    still meant something looser than "a citation exists." Under the D3
    ladder that 1b landed, V_SOURCED means "cited, never independently
    cross-checked" -- and neither of these can honestly claim the first
    half of that.

WHAT STAYS

    build_pinned_values() STAYS, and its call site stays. The build
    prompt asks to remove it if Option A was its only consumer. It is
    not: scan_shadow_constants() takes pinned_values and uses it to
    detect DERIVED shadow constants -- expressions like
    695700.0 / 149597870.7 built from pinned literals. Removing it would
    silently break the shadow-constant detector that 1d just added.
    Verified by tracing every reference before touching anything.

    What does change is that pinned_values now feeds ONLY a diagnostic,
    never a score. That is the honest place for it.

    Block-citation inheritance (1c) also stays. It is not the same
    failure class: the string inherits an actual citation written by an
    actual person about the block it sits in. It scores V_SOURCED, which
    is exactly right -- cited, not cross-checked.

MEASURED IMPACT, each removal isolated

    Tier 1  171 -> 210  (+39)
    Tier 2  644 -> 605  (-39)
    Tier 3   62 ->  62  (unchanged)
    Tier 4    2 ->   2  (unchanged)
    Total   879 -> 879  (conserved -- nothing appears or disappears;
                         findings only become correctly scored)

    Measured separately rather than attributing one diff to two causes:

        Option A removed alone      Tier 1 171 -> 194   (+23)
        + stale credit removed      Tier 1 194 -> 210   (+16)

    39 findings enter Tier 1 and none leave. That increase is the
    point, not a side effect: every one was an uncited claim the
    scanner was scoring as sourced.

HOW TO RUN IT (VS Code)
    1. Save this file into the SAME folder as provenance_scanner.py.
    2. Open it in VS Code.
    3. Click the Run button (the triangle, top right).

    Or from a terminal in that folder:  python patch_retire_option_a.py

AFTER IT RUNS
    python test_provenance_1d.py          -> expect 27 passed
    python test_citation_inheritance.py   -> expect 20 passed
    python test_constants_provenance.py   -> expect 73 passed
    python provenance_scanner.py .        -> expect Tier 1 210, Tier 2 605

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGETS = {
    'provenance_scanner.py': 'a2bb551b8535b2e8eba40f916e8c9467',
    'test_provenance_1d.py': '5585323427e0fe2966d984c529d31581',
}


# ==================================================================
# FILE 1 -- provenance_scanner.py   (bottom-up)
# ==================================================================

# ---- E1: the scan_project call site (lowest edit) ----

S1_OLD = b"""    # Option A: build pinned constant lookup from constants_new.py
    pinned_values = build_pinned_values(project_dir)"""

S1_NEW = b"""    # Pinned constant lookup from constants_new.py. Since D8.5 this
    # feeds the shadow-constant detector ONLY -- it no longer reaches
    # scoring. A value match is a reason to go look, not a reason to
    # grant credit.
    pinned_values = build_pinned_values(project_dir)"""


# ---- E2: score_unit signature ----

S2_OLD = b"""def score_unit(unit, imported_names, pinned_values=None):
    \"\"\"Assign vulnerability and criticality to a unit.\"\"\""""

S2_NEW = b'''def score_unit(unit, imported_names):
    """Assign vulnerability and criticality to a unit.

    Vulnerability answers one question: does a citation exist for this
    claim? Nothing else may substitute for it. Two mechanisms that once
    did were retired in D8.5 -- see the note above the ladder below.
    """'''


# ---- E3: Option A block + stale credit ----

S3_OLD = b'''    text = unit.context_text or ''
    is_doc = bool(unit.is_docstring)
    cited = has_citation(text, is_docstring=is_doc)
    stale = has_stale_marker(text)

    # Option A: cross-reference against pinned constants.
    # If ALL numeric claims in a display string match values already
    # pinned and cited in constants_new.py, treat as V_SOURCED.
    # Requires ALL claims to match to avoid false positives.
    if (not cited and pinned_values and unit.kind == 'string'
            and unit.numeric_claims):
        claim_values = set()
        for num_str, unit_str, value in unit.numeric_claims:
            for prec in (0, 1, 2, 3):
                claim_values.add(round(value, prec))
        if claim_values and all(v in pinned_values for v in claim_values):
            cited = True
            unit.vuln_reason = "Cited via pinned constant in constants_new.py"

    # D3 ladder (L-156). STALE is no longer a rung of its own: a cited
    # value that has never been independently cross-checked carries the
    # same vulnerability whether or not it also looks date-sensitive, so
    # both land on V_SOURCED. The distinction is preserved in the REASON,
    # which is where it was always the useful information.
    if cited and stale:
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Cited, not cross-checked; date-sensitive"
    elif cited:
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Cited, not independently cross-checked"
    elif stale:
        unit.vuln = V_SOURCED
        unit.vuln_reason = "No source, contains date-sensitive claims"
    elif unit.inherited_citation:'''

S3_NEW = b'''    text = unit.context_text or ''
    is_doc = bool(unit.is_docstring)
    cited = has_citation(text, is_docstring=is_doc)
    stale = has_stale_marker(text)

    # D8.5 -- two mechanisms removed here, both of the same class.
    #
    # OPTION A granted V_SOURCED to an uncited display string when all
    # its numeric claims matched values pinned from constants_new.py. A
    # value match proves two numbers are equal; it does not prove anyone
    # consulted a source. Suspicious matches are still reported, by the
    # shadow-constant detector, as a DIAGNOSTIC -- which tells you to go
    # look, where a score told you not to bother.
    #
    # STALE-ONLY CREDIT granted V_SOURCED to a unit with no citation at
    # all whenever its text carried a staleness marker ("as of 2024",
    # "Planned"). Its own reason string read "No source, contains
    # date-sensitive claims" -- the scanner stating there was no source
    # and scoring it as though there were. A staleness marker is
    # evidence a claim will EXPIRE, not evidence it was ever sourced;
    # if anything it belongs on the other side of the ladder.
    #
    # Both predate the D3 ladder, when V_SOURCED meant something looser
    # than "a citation exists." Under the ladder 1b landed it means
    # "cited, never independently cross-checked," and neither of these
    # can claim the first half of that.
    #
    # Staleness is still DETECTED and still reported in the reason,
    # which is where it was always the useful information -- it just no
    # longer moves the score on its own.
    if cited and stale:
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Cited, not cross-checked; date-sensitive"
    elif cited:
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Cited, not independently cross-checked"
    elif unit.inherited_citation:'''


# ---- E4: the stale branch's replacement in the else chain ----

S4_OLD = b'''    else:
        unit.vuln = V_RECALLED
        unit.vuln_reason = "No source citation (recalled)"

    # ---- Criticality ----'''

S4_NEW = b'''    elif stale:
        # No citation, and the text says it will go out of date. V4,
        # with the staleness carried in the reason.
        unit.vuln = V_RECALLED
        unit.vuln_reason = "No source citation; date-sensitive (recalled)"
    else:
        unit.vuln = V_RECALLED
        unit.vuln_reason = "No source citation (recalled)"

    # ---- Criticality ----'''


# ---- E5: the score_unit call in scan_project ----

S5_OLD = b"""            score_unit(u, imported_names, pinned_values)"""

S5_NEW = b"""            score_unit(u, imported_names)"""


# ---- E6: docstring, mechanism list entry 8 ----

S6_OLD = b"""    8. Constant cross-reference (Option A):
       An attempt to mark display string claims as V_SOURCED when their
       numeric values match pinned constants in constants_new.py.
       Implemented but rarely fires in practice: the \"all claims must
       match\" requirement breaks on coincidental numbers (200, 1, etc.)
       that appear in hover text but are not pinned constants. The
       correct fix is to add # Source: comments to shell info variables,
       which was done for solar and uranus shells (April 2026).
       Identified as insufficient by Claude Sonnet 4.6 after testing."""

S6_NEW = b"""    8. Constant cross-reference (Option A) -- RETIRED, D8.5, Aug 2026:
       Marked display string claims as V_SOURCED when their numeric
       values matched pinned constants in constants_new.py. Retired
       because a value match is not provenance: it shows two numbers
       are equal, not that anyone consulted a source. It credited 26
       display strings, 23 of which belonged in Tier 1.
       Value matches are still reported by the shadow-constant detector
       as a diagnostic. build_pinned_values() remains, feeding that
       detector only -- it no longer reaches scoring.
       The same audit retired STALE-ONLY credit, which granted
       V_SOURCED to uncited units carrying a staleness marker."""


# ---- E7: docstring, Stage 3 narrative ----

S7_OLD = b"""    Option B (dedup) implemented; Option A (constant cross-reference)
    implemented but rarely fires due to value-matching fragility with
    coincidental numbers like 200, 1, etc."""

S7_NEW = b"""    Option B (dedup) implemented; Option A (constant cross-reference)
    implemented, then retired in August 2026 (D8.5) -- value matching is
    not provenance. See mechanism 8 below."""


# ---- E8: credit line ----

S8_OLD = b"""citation extracted as the single citation predicate; build_pinned_values no"""

S8_NEW = b"""Module updated: August 2026 with Anthropic's Claude Opus 5 (D8.5: Option A
retired -- V_SOURCED is no longer granted for numeric coincidence -- and
stale-only credit retired with it, since a staleness marker is not a source.
build_pinned_values retained; it now feeds the shadow-constant diagnostic only).

Module updated: July 2026 with Anthropic's Claude Opus 5 (constant_has_own_
citation extracted as the single citation predicate; build_pinned_values no"""


S_EDITS = [
    ("S1 call-site comment", S1_OLD, S1_NEW),
    ("S2 score_unit signature", S2_OLD, S2_NEW),
    ("S3 remove Option A + stale credit", S3_OLD, S3_NEW),
    ("S4 stale lands at V_RECALLED", S4_OLD, S4_NEW),
    ("S5 score_unit call", S5_OLD, S5_NEW),
    ("S6 docstring mechanism 8", S6_OLD, S6_NEW),
    ("S7 docstring Stage 3", S7_OLD, S7_NEW),
    ("S8 module credit line", S8_OLD, S8_NEW),
]


# ==================================================================
# FILE 2 -- test_provenance_1d.py
# ==================================================================

T1_OLD = b"""    build_pinned_values,
    constant_has_own_citation,"""

T1_NEW = b"""    build_pinned_values,
    constant_has_own_citation,
    has_stale_marker,
    score_unit,"""


T2_OLD = b"""# ============================================================
# RUNNER
# ============================================================"""

T2_NEW = b'''# ============================================================
# TESTS -- D8.5, no credit without a citation
# ============================================================

class _FakeUnit:
    """Minimal stand-in for a display-string ProvenanceUnit."""

    def __init__(self, context, claims=(), inherited=None):
        self.context_text = context
        self.is_docstring = False
        self.kind = 'string'
        self.name = None
        self.numeric_claims = list(claims)
        self.inherited_citation = inherited
        self.scope_declined = False
        self.raw_value = context
        self.value = context
        self.module = 'fake'
        self.vuln = None
        self.vuln_reason = None
        self.crit = None
        self.crit_reason = None
        self.consumer_count = 0
        self.consumers = ()
        self.score = None

    def compute_score(self):
        self.score = (self.vuln or 0) * (self.crit or 0)


def test_numeric_match_alone_earns_no_credit():
    """Option A is gone: matching a pinned value is not a citation.

    695700.0 is SUN_RADIUS_KM in constants_new.py and is pinned. Before
    D8.5 a display string quoting it with no citation scored V_SOURCED.
    """
    unit = _FakeUnit('The Sun has a radius of 695700 km.',
                     claims=[('695700', 'km', 695700.0)])
    score_unit(unit, {})
    assert unit.vuln == V_RECALLED, \\
        f"numeric coincidence still earns credit: {unit.vuln_reason!r}"


def test_stale_marker_alone_earns_no_credit():
    """A staleness marker is not a source.

    The retired branch wrote the reason 'No source, contains
    date-sensitive claims' while assigning V_SOURCED -- stating there
    was no source and scoring as though there were.
    """
    for text in ['# Voyager 1 distance as of 2024 is 163 AU',
                 '# Planned launch window',
                 '# Still active as of 2025']:
        unit = _FakeUnit(text)
        score_unit(unit, {})
        assert unit.vuln == V_RECALLED, \\
            f"staleness earned credit for {text!r}: {unit.vuln_reason!r}"


def test_staleness_still_detected_and_reported():
    """Retiring the credit must not lose the signal.

    Staleness detection stays; it just no longer moves the score. The
    distinction survives in the reason string, which is where it was
    always the useful information.
    """
    assert has_stale_marker('# current as of 2024'), \\
        "stale detection was removed along with the credit"
    unit = _FakeUnit('# updated 2024, value is 5 AU')
    score_unit(unit, {})
    assert 'date-sensitive' in (unit.vuln_reason or ''), \\
        f"staleness dropped from the reason: {unit.vuln_reason!r}"


def test_real_citation_still_earns_v_sourced():
    """The removals must not break actual sourcing."""
    unit = _FakeUnit('# Source: IAU 2015 Resolution B3\\nradius 695700 km')
    score_unit(unit, {})
    assert unit.vuln == V_SOURCED, \\
        f"a real citation lost its credit: {unit.vuln_reason!r}"


def test_block_inheritance_still_earns_v_sourced():
    """1c inheritance is NOT the same failure class and must survive.

    An inheriting string carries a citation a person actually wrote
    about the block it sits in. That is real provenance, one level up --
    unlike a value match, which is provenance nobody wrote.
    """
    unit = _FakeUnit('radius 695700 km',
                     inherited='# Source: IAU 2015 Resolution B3')
    score_unit(unit, {})
    assert unit.vuln == V_SOURCED, \\
        f"block inheritance was broken: {unit.vuln_reason!r}"


def test_pinned_values_no_longer_reaches_scoring():
    """score_unit() must not accept pinned values at all.

    Signature-level guard. If a future change re-adds the parameter,
    the mechanism can come back quietly; without it, it cannot.
    """
    import inspect
    params = list(inspect.signature(score_unit).parameters)
    assert 'pinned_values' not in params, \\
        f"score_unit still takes pinned values: {params}"


def test_pinned_values_still_feeds_the_shadow_detector():
    """build_pinned_values() must survive -- it has a second consumer.

    scan_shadow_constants() uses it to detect DERIVED shadow constants
    (expressions built from pinned literals). Removing it with Option A
    would have silently broken the detector 1d added.
    """
    import inspect
    params = list(inspect.signature(scan_shadow_constants).parameters)
    assert 'pinned_values' in params, \\
        "the shadow detector lost its pinned-values input"
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(os.path.join(here, 'constants_new.py')):
        assert build_pinned_values(here), \\
            "build_pinned_values returned nothing"


# ============================================================
# RUNNER
# ============================================================'''


T3_OLD = b"""    test_both_pinned_builders_agree,
]"""

T3_NEW = b"""    test_both_pinned_builders_agree,
    test_numeric_match_alone_earns_no_credit,
    test_stale_marker_alone_earns_no_credit,
    test_staleness_still_detected_and_reported,
    test_real_citation_still_earns_v_sourced,
    test_block_inheritance_still_earns_v_sourced,
    test_pinned_values_no_longer_reaches_scoring,
    test_pinned_values_still_feeds_the_shadow_detector,
]"""


T4_OLD = b"""from provenance_scanner import (
    SHADOW_CONSTANTS,"""

T4_NEW = b"""from provenance_scanner import (
    SHADOW_CONSTANTS,
    V_RECALLED,
    V_SOURCED,"""


T5_OLD = b"""    scan_shadow_constants,
)"""

T5_NEW = b"""    scan_shadow_constants,
)  # noqa: F401  -- V_* and scan_shadow_constants used by the D8.5 tests"""


T_EDITS = [
    ("T1 imports: stale + score_unit", T1_OLD, T1_NEW),
    ("T2 seven D8.5 tests", T2_OLD, T2_NEW),
    ("T3 register in runner", T3_OLD, T3_NEW),
    ("T4 imports: V_ constants", T4_OLD, T4_NEW),
    ("T5 import block note", T5_OLD, T5_NEW),
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
                'provenance_scanner.py': b'D8.5 -- two mechanisms removed',
                'test_provenance_1d.py': b'test_numeric_match_alone_earns_no_credit',
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
    print("  python test_provenance_1d.py    -> expect 27 passed")
    print("  python provenance_scanner.py .  -> expect Tier 1 210")
    print()
    print("Tier 1 goes UP by 39. Those findings were always uncited; the")
    print("scanner was crediting them for numeric coincidence. A second")
    print("mechanism of the same class (stale-marker credit, 15 findings)")
    print("was found during the audit and removed with it -- see the")
    print("as-built section 4.")


if __name__ == '__main__':
    main()
