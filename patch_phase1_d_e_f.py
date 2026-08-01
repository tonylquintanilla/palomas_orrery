"""
patch_phase1_d_e_f.py

Phase 1d / 1e / 1f -- the rest of L-156's Phase 1.

Built on e29841f88fcc4b0f4d02681df1e0ec06b13a08c6
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT THIS PATCHES

    provenance_scanner.py       (1d and 1e)
    comet_visualization_shells.py (1f)

    All-or-nothing across BOTH files. If any guard or anchor fails,
    nothing is written to either.

1d -- THREE PIECES OF RECOGNITION WORK

    Piece 1, frozen-copy detection. A module that hand-types a value
    which already exists as a cited constant in constants_new.py has
    made a frozen copy: it will not follow if the source value is ever
    corrected, and it sits outside the citation chain even while the
    number is right. The new detector reports these.

      IMPORTANT DIVERGENCE FROM THE PREDESIGN, flagged for Tony rather
      than resolved here -- see the as-built section 3. The predesign
      asks for this as an amendment to score_unit()'s Option A block.
      Measured at HEAD, that will not reach the problem: Option A only
      inspects display STRINGS, and all three confirmed shadow constants
      are function-local numeric ASSIGNMENTS, which the scanner does not
      extract as units at all. Amending Option A to require an import
      would instead demote 9 unrelated display strings from V_SOURCED to
      V_RECALLED, pushing them UP toward Tier 1. So this patch adds a
      dedicated detector and leaves Option A's scoring untouched.

      The detector matches on NAME AND VALUE together, not value alone.
      Measured repo-wide: name+value yields exactly the 2 confirmed
      direct instances with zero false positives; value alone yields 77
      candidates, mostly coincidental round numbers. The derived case
      (a literal expression built from two pinned values) is caught
      separately, with a magnitude floor that excludes trivial
      small-integer coincidences.

    Piece 2, citation-form recognition. has_citation() did not recognise
    an author-year parenthetical, so genuinely cited values scored V4
    RECALLED -- the scanner calling a cited value uncited, which is
    cite-to-clear pointed the other way. Both live forms are now
    recognised, with and without a year. The pattern requires either a
    multi-author marker (et al. / & Author / and Author) or a
    four-digit year after a capitalised surname, and excludes month
    names so that a date like (May 2026) is not read as a citation.

    Piece 3, temperature units. NUMERIC_CLAIM_RE did not recognise
    Fahrenheit or Celsius. Note this is not purely additive: "35
    degrees C" already matched, as 35 angular DEGREES, because the
    generic degree alternative captured the number and dropped the
    trailing C. The temperature alternatives are therefore placed
    BEFORE the generic ones so the more specific unit wins.

1e -- CONSOLE OUTPUT

    Piece 1, Tier-1 banner. Prominent, bordered, printed whenever Tier-1
    findings exist. Informational ONLY -- the exit code is untouched.
    Design review section 3c is explicit that Tier-1 never gets an
    auto-exit gate at any threshold, ever, and supersedes the
    deferred-flip described in HANDOFF_phase1_1d_to_1f.md at HEAD.

    Piece 2, tier labels. "ALL ACCEPTED RESIDUALS" was asserted in the
    Tier-2 tier NAME, so every new finding landing in that band was
    narrated as already-reviewed by the template itself. Tiers 2, 3 and
    4 now carry neutral score-band names. Accepted-residual status is
    per-finding information and already has its own report block.
    Tier 1 keeps "FIX NOW" -- that is an action directive, not a claim
    about the findings' status. See as-built section 6 if you would
    rather all four were neutral.

1f -- MECHANICAL CODE FIX

    Delete the three shadow constants in comet_visualization_shells.py
    and import the real ones. SOLAR_RADIUS_AU, not SUN_RADIUS_AU --
    the latter name does not exist in constants_new.py.

    Note the locals are function-local, so the local KM_PER_AU at line
    493 was SHADOWING the module-level import at line 42 for the body
    of that function. This is a live scoping issue, not only a
    provenance one.

HOW TO RUN IT (VS Code)
    1. Save this file into the SAME folder as provenance_scanner.py.
    2. Open it in VS Code.
    3. Click the Run button (the triangle, top right).

    Or from a terminal in that folder:  python patch_phase1_d_e_f.py

WHAT YOU SHOULD SEE
    One "ok" line per edit, grouped by file, then "patch applied".
    Any failure writes nothing to either file.

AFTER IT RUNS
    python test_citation_inheritance.py   -> expect 20 passed (unchanged)
    python test_provenance_1d.py          -> expect 15 passed
    python provenance_scanner.py .        -> see the as-built for the
                                             expected tier movement

Module updated: July 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGETS = {
    'provenance_scanner.py':         '004d179fe93c200db4534cf1b0a7f038',
    'comet_visualization_shells.py': '58929e7fc7137f6264d950031a6bf6a7',
}


# ==================================================================
# FILE 1 -- provenance_scanner.py
# ==================================================================

# ---- 1d piece 3: temperature units ----
# Ordered BEFORE the generic degree alternatives. Python's alternation
# is first-match-wins, so without this ordering "35 degrees C" keeps
# matching as 35 angular degrees. \xb0 is the degree sign, written as an
# escape to keep this file pure ASCII.

S1_OLD = b"""    r'(R_sun|AU|km/s|km|m/s|degrees?|deg\\b|arcsec|mas|pc|kpc|Mpc|'"""

S1_NEW = b"""    r'(degrees?\\s*[CF]\\b|deg\\s*[CF]\\b|\\xb0\\s*[CF]\\b|'
    r'degrees?\\s+(?:Celsius|Fahrenheit)\\b|'
    r'R_sun|AU|km/s|km|m/s|degrees?|deg\\b|arcsec|mas|pc|kpc|Mpc|'"""


# ---- 1d piece 2: author-year citation forms ----

S2_OLD = b"""    re.compile(r'https?://\\S+\\.\\S+', re.IGNORECASE),
]"""

S2_NEW = b'''    re.compile(r'https?://\\S+\\.\\S+', re.IGNORECASE),
    # L-156 Gap item 7: bare author-year parentheticals.
    #
    # Two live forms, both real citations that previously scored V4
    # RECALLED -- the scanner calling a cited value uncited:
    #     (Vecellio et al.)          (Sherwood & Huber)
    #     (Vecellio et al., 2022)    (Sherwood & Huber, 2010)
    #
    # Tightness is the whole difficulty here. A pattern that merely
    # looks for a capitalised word and a year inside parentheses
    # matches "(May 2026)" -- a date in a comment -- on the first file
    # in the repo. So a match requires EITHER a multi-author marker
    # (et al. / & Author / and Author), OR a four-digit year following
    # a capitalised surname, and month names are excluded outright.
    re.compile(
        r'\\((?!(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))'
        r'[A-Z][A-Za-z\\'\\-]+'
        r'(?:\\s+et\\s+al\\.?|\\s*&\\s*[A-Z][A-Za-z\\'\\-]+'
        r'|\\s+and\\s+[A-Z][A-Za-z\\'\\-]+)'
        r'(?:,?\\s*(?:19|20)\\d{2}[a-z]?)?\\)'
        r'|'
        r'\\((?!(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))'
        r'[A-Z][A-Za-z\\'\\-]+,?\\s+(?:19|20)\\d{2}[a-z]?\\)'
    ),
]'''


# ---- 1d piece 1: frozen-copy detector ----

S3_OLD = b"""def build_pinned_values(project_dir):"""

S3_NEW = b'''# ============================================================
# SHADOW CONSTANTS (L-156 Gap item 5 / L-158; 1d piece 1)
# ============================================================
# A module that hand-types a value already defined and cited in
# constants_new.py has made a frozen copy. The number may be correct
# today; the problem is that it will not follow if the source is ever
# corrected, and it sits outside the citation chain in the meantime.
# provenance-discipline v1.3 makes this a [CRITICAL] convention: delete
# the local definition and import the real one. Never add a "# Source:"
# comment to a local copy -- that cites-to-clear a structural problem.
#
# Detection matches on NAME AND VALUE TOGETHER. Measured repo-wide at
# the time this was written: name+value returns exactly the two known
# direct instances and nothing else; value alone returns 77 candidates,
# almost all coincidental round numbers (0.5, 2.2, 10.0) that happen to
# equal some pinned constant. Value alone is not a usable signal.
#
# This is a DIAGNOSTIC. It does not change any unit's score. The
# constants involved are function-local assignments, which the scanner
# does not extract as units at all, so there is no score to change --
# see the as-built for why Option A was left alone.

# A derived shadow is an expression built from pinned literals, e.g.
# SUN_RADIUS_AU = 695700.0 / 149597870.7. Requiring at least one
# literal of this magnitude excludes trivial coincidences: without it,
# an expression containing 2 twice matches, because 2.0 is itself a
# pinned value.
SHADOW_DERIVED_MIN_MAGNITUDE = 100.0

SHADOW_CONSTANTS = []


def _numeric_from_node(node):
    """Return the float value of a numeric literal node, or None."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) \\
            and not isinstance(node.value, bool):
        return float(node.value)
    if (isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub)
            and isinstance(node.operand, ast.Constant)
            and isinstance(node.operand.value, (int, float))):
        return -float(node.operand.value)
    return None


def build_cited_constant_names(project_dir):
    """Map NAME -> value for cited numeric constants in constants_new.py.

    build_pinned_values() returns values only, which is enough to ask
    "does this number appear upstream" but not "is this the same
    constant." The name is what separates a frozen copy from a
    coincidence, so it has to be carried.
    """
    path = os.path.join(project_dir, 'constants_new.py')
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'rb') as f:
            content = f.read()
        lines_c = content.decode('utf-8', errors='replace').splitlines(
            keepends=True)
        tree = ast.parse(content)
    except Exception:
        return {}

    source_re = re.compile(r'#\\s*[Ss]ource\\s*:', re.IGNORECASE)
    named = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name) or not target.id.isupper():
            continue
        num = _numeric_from_node(node.value)
        if num is None:
            continue
        # Find THIS constant's own citation, in either of the two
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
    return named


def scan_shadow_constants(project_dir, cited_names, pinned_values):
    """Populate SHADOW_CONSTANTS with local copies of cited constants.

    Walks every assignment at ANY nesting depth, because the known
    instances are function-local -- extract_units_from_file only reads
    top-level assignments, so these are invisible to the normal unit
    pipeline.

    Two shapes:
      'direct'  -- NAME = <literal>, where NAME is a cited constant in
                   constants_new.py and the value agrees.
      'derived' -- NAME = <expression of literals>, where every literal
                   matches a pinned value and at least one is large
                   enough not to be a coincidence.
    """
    for fname in sorted(os.listdir(project_dir)):
        if not fname.endswith('.py') or fname == 'constants_new.py':
            continue
        path = os.path.join(project_dir, fname)
        try:
            with open(path, 'rb') as f:
                tree = ast.parse(f.read())
        except Exception:
            continue

        for node in ast.walk(tree):
            if not isinstance(node, ast.Assign) or len(node.targets) != 1:
                continue
            target = node.targets[0]
            if not isinstance(target, ast.Name):
                continue
            name = target.id

            num = _numeric_from_node(node.value)
            if num is not None:
                upstream = cited_names.get(name)
                if upstream is not None and abs(num - upstream) < 1e-9:
                    SHADOW_CONSTANTS.append(
                        (fname, node.lineno, name, 'direct', num))
                continue

            if isinstance(node.value, ast.BinOp) and name.isupper():
                literals = []
                ok = True
                for sub in ast.walk(node.value):
                    val = None
                    if isinstance(sub, ast.Constant) and isinstance(
                            sub.value, (int, float)) and not isinstance(
                            sub.value, bool):
                        val = float(sub.value)
                    if val is None:
                        continue
                    literals.append(val)
                    if round(val, 3) not in pinned_values:
                        ok = False
                        break
                if (ok and len(literals) >= 2
                        and any(abs(v) >= SHADOW_DERIVED_MIN_MAGNITUDE
                                for v in literals)):
                    SHADOW_CONSTANTS.append(
                        (fname, node.lineno, name, 'derived', None))


def build_pinned_values(project_dir):'''


# ---- scan_project: reset collector ----

S4_OLD = b"""    del SCOPE_DECLARED_BLOCKS[:]
    del SHADOWED_STRINGS[:]
    del DEEP_CITATIONS[:]"""

S4_NEW = b"""    del SCOPE_DECLARED_BLOCKS[:]
    del SHADOWED_STRINGS[:]
    del DEEP_CITATIONS[:]
    del SHADOW_CONSTANTS[:]"""


# ---- scan_project: run the shadow scan ----

S5_OLD = b"""    # Option A: build pinned constant lookup from constants_new.py
    pinned_values = build_pinned_values(project_dir)
    if pinned_values:
        print(f"Loaded {len(pinned_values)} pinned constant values "
              f"for cross-reference scoring")"""

S5_NEW = b"""    # Option A: build pinned constant lookup from constants_new.py
    pinned_values = build_pinned_values(project_dir)
    if pinned_values:
        print(f"Loaded {len(pinned_values)} pinned constant values "
              f"for cross-reference scoring")

    # 1d piece 1: frozen-copy detection. Diagnostic only -- this does
    # not feed scoring.
    cited_names = build_cited_constant_names(project_dir)
    scan_shadow_constants(project_dir, cited_names, pinned_values)"""


# ---- console: shadow line + pass to report ----

S6_OLD = b"""    if DEEP_CITATIONS:
        print(f"WARNING: {len(DEEP_CITATIONS)} citation(s) sit on a dict "
              f"nested deeper than the block table reads -- see audit")"""

S6_NEW = b"""    if DEEP_CITATIONS:
        print(f"WARNING: {len(DEEP_CITATIONS)} citation(s) sit on a dict "
              f"nested deeper than the block table reads -- see audit")
    if SHADOW_CONSTANTS:
        print(f"{len(SHADOW_CONSTANTS)} shadow constant(s) -- local copies "
              f"of cited constants_new.py values, see audit")"""


S7_OLD = b"""                    scope_declared=list(SCOPE_DECLARED_BLOCKS),
                    shadowed=list(SHADOWED_STRINGS),
                    deep_citations=list(DEEP_CITATIONS))"""

S7_NEW = b"""                    scope_declared=list(SCOPE_DECLARED_BLOCKS),
                    shadowed=list(SHADOWED_STRINGS),
                    deep_citations=list(DEEP_CITATIONS),
                    shadow_constants=list(SHADOW_CONSTANTS))"""


S8_OLD = b"""                    scope_declared=None, shadowed=None,
                    deep_citations=None):"""

S8_NEW = b"""                    scope_declared=None, shadowed=None,
                    deep_citations=None, shadow_constants=None):"""


# ---- report section ----

S9_OLD = b"""    # ---- Citation level mismatch (L-174) ----"""

S9_NEW = b'''    # ---- Shadow constants (L-156 Gap item 5, 1d piece 1) ----
    if shadow_constants:
        out.append("## SHADOW CONSTANTS -- [CRITICAL] convention violation")
        out.append("")
        out.append("Local copies of values that are already defined and "
                   "cited in `constants_new.py`. The number may be correct "
                   "today; the problem is that it will not follow if the "
                   "source value is ever corrected, and it sits outside "
                   "the citation chain in the meantime.")
        out.append("")
        out.append("Per provenance-discipline v1.3, No Shadow Constants "
                   "[CRITICAL]: delete the local definition and import the "
                   "real one, through the `planet_visualization_utilities` "
                   "shim or directly. Do NOT add a `# Source:` comment to "
                   "the local copy -- that cites-to-clear a structural "
                   "problem instead of fixing it.")
        out.append("")
        out.append("`direct` means the local name and value both match a "
                   "cited constant. `derived` means the value is computed "
                   "from pinned literals rather than from the imported "
                   "names.")
        out.append("")
        out.append("| File | Line | Name | Kind |")
        out.append("|------|-----:|------|------|")
        for entry in sorted(shadow_constants):
            sfile, line, name, kind, _val = entry
            out.append(f"| `{sfile}` | {line} | `{name}` | {kind} |")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Citation level mismatch (L-174) ----'''


# ---- 1e piece 2: tier labels ----

S10_OLD = b"""    out.append("- 16-20: FIX NOW")
    out.append("- 10-15: ALL ACCEPTED RESIDUALS -- see note below")
    out.append("- 5-9: ALREADY CITED OR LOW RISK")
    out.append("- 1-4: NO ACTION NEEDED")"""

S10_NEW = b"""    out.append("- 16-20: FIX NOW")
    out.append("- 10-15: REVIEW")
    out.append("- 5-9: LOW PRIORITY")
    out.append("- 1-4: LOWEST PRIORITY")"""


S11_OLD = b"""    tier_labels = {
        1: ("16-20", "FIX NOW"),
        2: ("10-15", "ALL ACCEPTED RESIDUALS -- see note below"),
        3: ("5-9", "ALREADY CITED OR LOW RISK -- no action required"),
        4: ("1-4", "NO ACTION NEEDED"),
    }"""

S11_NEW = b"""    # 1e piece 2 (design handoff D7): tier names are score bands, not
    # claims about the findings inside them. The old Tier-2 name asserted
    # "ALL ACCEPTED RESIDUALS", so every new finding landing in that band
    # was narrated as already-reviewed by this template -- including the
    # ones 1b had just moved there. Accepted-residual status is
    # per-finding and has its own report block.
    tier_labels = {
        1: ("16-20", "FIX NOW"),
        2: ("10-15", "REVIEW"),
        3: ("5-9", "LOW PRIORITY"),
        4: ("1-4", "LOWEST PRIORITY"),
    }"""


# ---- 1e piece 1: Tier-1 banner ----

S12_OLD = b"""    print("Priority summary:")
    for tier in [1, 2, 3, 4]:
        score_range, action = tier_labels[tier]
        count = tier_counts.get(tier, 0)
        print(f"  Tier {tier} ({score_range}): {count:5d} findings -- {action}")"""

S12_NEW = b'''    print("Priority summary:")
    for tier in [1, 2, 3, 4]:
        score_range, action = tier_labels[tier]
        count = tier_counts.get(tier, 0)
        print(f"  Tier {tier} ({score_range}): {count:5d} findings -- {action}")

    # 1e piece 1: Tier-1 banner. INFORMATIONAL ONLY.
    #
    # The exit code is deliberately untouched here, and should stay that
    # way. Design review section 3c: Tier-1 never gets an auto-exit gate,
    # at any threshold, ever -- a count is the wrong thing to judge by,
    # since a trivial new finding would fail a good run and a serious
    # finding replacing a trivial one at equal count would pass a bad
    # one. Whether N findings are acceptable to push past is a judgment
    # call every time. The only hard exit-code gate belongs to the
    # pinning checks, which are genuinely binary.
    #
    # (HANDOFF_phase1_1d_to_1f.md at HEAD describes a deferred exit-gate
    # flip. That is the superseded Fable design; do not revive it from
    # that document.)
    tier1 = tier_counts.get(1, 0)
    if tier1:
        bar = "=" * 70
        print()
        print(bar)
        print(f"  {tier1} TIER-1 FINDINGS -- PUSH GATE NOT MET")
        print()
        print("  Informational only. This does not affect the exit code.")
        print("  Review them before pushing; the call is yours.")
        print(bar)'''


# ---- credit line ----

S13_OLD = b"""Module updated: July 2026 with Anthropic's Claude Opus 5 (L-156 Gap item 6,"""

S13_NEW = b"""Module updated: July 2026 with Anthropic's Claude Opus 5 (L-156 Phase 1d/1e:
frozen-copy detection for shadow constants, author-year citation forms,
Fahrenheit/Celsius units, the Tier-1 banner, and neutral tier labels).

Module updated: July 2026 with Anthropic's Claude Opus 5 (L-156 Gap item 6,"""


S_EDITS = [
    ("S1  temperature units in NUMERIC_CLAIM_RE", S1_OLD, S1_NEW),
    ("S2  author-year citation patterns", S2_OLD, S2_NEW),
    ("S3  shadow-constant detector", S3_OLD, S3_NEW),
    ("S4  reset collector per scan", S4_OLD, S4_NEW),
    ("S5  run shadow scan in scan_project", S5_OLD, S5_NEW),
    ("S6  console line for shadow constants", S6_OLD, S6_NEW),
    ("S7  pass shadow constants to report", S7_OLD, S7_NEW),
    ("S8  report signature", S8_OLD, S8_NEW),
    ("S9  shadow-constant report section", S9_OLD, S9_NEW),
    ("S10 neutral tier names in legend", S10_OLD, S10_NEW),
    ("S11 neutral tier_labels", S11_OLD, S11_NEW),
    ("S12 Tier-1 banner", S12_OLD, S12_NEW),
    ("S13 module credit line", S13_OLD, S13_NEW),
]


# ==================================================================
# FILE 2 -- comet_visualization_shells.py  (1f)
# ==================================================================

C1_OLD = b"""from planet_visualization_utilities import KM_PER_AU"""

C1_NEW = b"""from planet_visualization_utilities import (
    KM_PER_AU, SUN_RADIUS_KM, SOLAR_RADIUS_AU)"""


# Delete the two direct shadow constants. The local KM_PER_AU was
# shadowing the module-level import for the body of this function, so
# removing it is a scoping fix as well as a provenance one.
C2_OLD = b"""    import math
    SUN_RADIUS_KM   = 695700.0
    KM_PER_AU       = 149597870.7
"""

C2_NEW = b"""    import math
    # SUN_RADIUS_KM and KM_PER_AU are imported at module scope. Local
    # copies lived here until L-156 1f; the local KM_PER_AU shadowed the
    # import for this whole function. No Shadow Constants [CRITICAL].
"""


# Delete the derived shadow. SOLAR_RADIUS_AU is the real name in
# constants_new.py -- there is no SUN_RADIUS_AU -- and it is defined
# there as SUN_RADIUS_KM / KM_PER_AU, so this substitution is
# value-preserving.
C3_OLD = b"""    SUN_RADIUS_AU = 695700.0 / 149597870.7
"""

C3_NEW = b"""    # SOLAR_RADIUS_AU is imported at module scope. It is defined in
    # constants_new.py as SUN_RADIUS_KM / KM_PER_AU -- the same two
    # values this line used to recompute from literals.
    SUN_RADIUS_AU = SOLAR_RADIUS_AU
"""


C_EDITS = [
    ("C1 import the real constants", C1_OLD, C1_NEW),
    ("C2 delete direct shadow constants", C2_OLD, C2_NEW),
    ("C3 delete derived shadow constant", C3_OLD, C3_NEW),
]


ALL_EDITS = [
    ('provenance_scanner.py', S_EDITS),
    ('comet_visualization_shells.py', C_EDITS),
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
                'provenance_scanner.py': b'SHADOW_CONSTANTS',
                'comet_visualization_shells.py': b'SOLAR_RADIUS_AU',
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
        # ASCII gate. NOTE: this asserts the patch does not INTRODUCE
        # non-ASCII, rather than that the file is pure ASCII.
        # comet_visualization_shells.py already carries 3 em-dashes
        # (9 bytes) in a display string and a comment, in violation of
        # the project's ASCII-only convention. That is a pre-existing
        # problem to fix deliberately, not something this patch should
        # fail on or silently rewrite.
        before = sum(1 for byte in loaded[name] if byte > 127)
        after = sum(1 for byte in content if byte > 127)
        if after > before:
            print(f"ERROR: patch introduces {after - before} non-ASCII "
                  f"byte(s) into {name}. Nothing written to ANY file.")
            sys.exit(1)
        if before:
            print(f"  note: {name} carries {before} pre-existing "
                  f"non-ASCII byte(s); unchanged by this patch")
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
    print("  python test_provenance_1d.py          -> expect 15 passed")
    print("  python test_citation_inheritance.py   -> expect 20 passed")
    print("  python provenance_scanner.py .")
    print()
    print("The shadow-constant section should be EMPTY after this patch --")
    print("1f deletes the only three instances 1d detects. The as-built")
    print("records what the detector reported before they were removed.")


if __name__ == '__main__':
    main()
