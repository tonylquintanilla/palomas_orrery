"""
test_derived_figures.py -- a derived constant declares no more
significant figures than its inputs support, and names every derived
row it cannot judge.

WHY THIS EXISTS

    Python can round a number to N figures but cannot count figures
    through arithmetic, so every value in constants_new.py declares its
    count on a "# Figures:" line, the way it declares its unit
    (provenance-discipline 2.13, The Figure Count Is a Declared Field).
    This file checks those declarations on DERIVED rows, where the count
    is not a matter of reading a source but of following the arithmetic.
    That is Rule 8.

    The store holds each derived row as an EXPRESSION at full precision
    (Rule 6), so Python already recomputes it from its inputs on every
    import. This checker therefore recomputes nothing and keeps no
    formula table. It judges the DECLARATION.

    The previous version of this file (L-325, 2026-09-12) found derived
    rows by the word "derived" on a Status line. Only two rows carried
    it, so it checked 2 of 27 and passed; its promise to fail on a row it
    did not cover could not fire for the other 25. That ruling was
    withdrawn by Tony on 2026-09-16, and this is the rewrite.

RUN COMMAND

    python test_derived_figures.py

    Open it in VS Code and click Run. orrery_maintenance_run.py runs it
    on every maintenance run.

WHICH ROWS IT READS

    Every row whose right-hand side is arithmetic on other rows, every
    row carrying a "# Derived:" line, and the two TRANSITIONAL standoffs
    (constants_rows.TRANSITIONAL). Finding rows both ways matters: at the
    time of writing four expressions have no "# Derived:" line of their
    own, and a checker that looked only for the line would not see them.

WHAT IT CHECKS, per row

    1. The row has a "# Figures:" line. If not: NOT YET MIGRATED.
    2. The line names the input that set the count, and every store row
       it names is an input of the expression. ("exact" needs no name.)
    3. The declared count is no more than the inputs support, worked out
       through the expression by the textbook rules (Rule 3):
         products, quotients, powers and functions keep the fewest
         figures among their measured inputs;
         sums and differences are good to the coarsest decimal place
         among their measured inputs;
         exact inputs, declared conditions and numbers typed into the
         expression never limit the result.
       A lower declared count is always allowed; Rule 3 asks for one
       where a power magnifies uncertainty. "exact" is allowed only when
       every input is exact. For a TRANSITIONAL row there is no
       expression, so the limit is the fewest figures among the inputs
       its Status line names.
    4. The number the "# Derived:" line states (the last "= number" in
       it) is the row's value rounded to no more figures than declared.
       A comment may state fewer (Rule 7); it may not state more, and it
       may not state different digits.

    A typed number carrying a "# Derived:" note gets check 1 only: its
    arithmetic lives in prose and there is nothing to follow.

WHAT FAILS, and what is a named gap

    FAIL   OVER-DECLARED, NAMES A NON-INPUT, NAMES NO INPUT,
           COMMENT DISAGREES, COMMENT OVERSTATES, MALFORMED, CANNOT JUDGE
    gap    NOT YET MIGRATED, INPUT NOT YET MIGRATED, NO DERIVED LINE

    A gap FAILS inside a closed slice (constants_rows.CLOSED_SLICES,
    empty until the Earth walk finishes). Outside one it is printed by
    name and the run passes. That is Tony's per-slice gate of
    2026-09-14.

THE FIXTURES RUN FIRST, EVERY TIME

    No row in the store declares a figure count yet, so every real
    verdict today is a gap. A small built-in store runs first through the
    same code and must produce every verdict above, including a gap that
    fails inside a closed slice. If one comes out wrong, the run fails.

Role: devtool
Domain: dev_tools

Module created: September 2026 with Anthropic's Claude Opus 5.
Module rewritten: September 16, 2026 with Anthropic's Claude Opus 5
(L-322, piece 5 of the build manifest: Rule 8 of provenance-discipline
2.13. The formula table and the Status-word enumeration are gone.)
"""

import ast
import math
import os
import re
import sys

import constants_rows

FAILING = ("MALFORMED", "CANNOT JUDGE", "OVER-DECLARED",
           "NAMES A NON-INPUT", "NAMES NO INPUT", "COMMENT DISAGREES",
           "COMMENT OVERSTATES")
GAPS = ("NOT YET MIGRATED", "INPUT NOT YET MIGRATED", "NO DERIVED LINE")

STATED_RE = re.compile(
    r"=\s*([-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][-+]?\d+)?)"
    r"(\.\.\.)?")

EXACT = None      # the figure count of an exact number: no limit


class Stop(Exception):
    def __init__(self, verdict, detail):
        Exception.__init__(self, detail)
        self.verdict = verdict
        self.detail = detail


def round_to(value, figures):
    """Rule 5: half to even, to `figures` significant figures."""
    return float("%.*g" % (figures, value))


def magnitude(value):
    """The decimal exponent of a non-zero number's leading digit."""
    return int(("%.15e" % abs(value)).split("e")[1])


def literal_figures(text):
    """(fewest, most) significant figures a written number can state.

    They differ only for a whole number ending in zeros, where the
    zeros may or may not count (Rule 2).
    """
    body = text.strip().lstrip("+-").replace(",", "")
    mantissa = re.split(r"[eE]", body)[0]
    digits = mantissa.replace(".", "").lstrip("0")
    if not digits:
        return 1, 1
    if "." in mantissa:
        return len(digits), len(digits)
    return max(1, len(digits.rstrip("0"))), len(digits)


def truncate_to(value, figures):
    scale = 10.0 ** (figures - 1 - magnitude(value))
    return math.copysign(math.floor(abs(value) * scale) / scale, value)


class Figures(object):
    """Walks an expression, carrying each part's value and precision."""

    FUNCS = {"tanh": math.tanh, "sinh": math.sinh, "cosh": math.cosh,
             "exp": math.exp, "log": math.log, "log10": math.log10,
             "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos,
             "tan": math.tan, "atan": math.atan, "arctan": math.atan,
             "radians": math.radians, "degrees": math.degrees,
             "abs": abs, "fabs": abs, "cbrt": lambda x: math.copysign(
                 abs(x) ** (1.0 / 3.0), x)}
    NUMBERS = {"pi": math.pi, "e": math.e}

    def __init__(self, by_name, values):
        self.by_name = by_name
        self.values = values
        self.embedded = []

    def leaf(self, name):
        row = self.by_name[name]
        value = self.values.get(name)
        if row.figures_error:
            raise Stop("MALFORMED", "input %s: %s" % (name, row.figures_error))
        if row.figures is None:
            raise Stop("INPUT NOT YET MIGRATED", "input %s has no "
                       "# Figures: line" % name)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise Stop("CANNOT JUDGE", "input %s is not a number" % name)
        if row.figures == "exact":
            return float(value), EXACT, None
        if value == 0:
            raise Stop("CANNOT JUDGE", "input %s is zero and declares %d "
                       "figures; a zero has no leading digit to count from. "
                       "Declare it exact, or state its uncertainty"
                       % (name, row.figures))
        return (float(value), row.figures,
                magnitude(value) - row.figures + 1)

    def ev(self, node):
        """(value, figures or EXACT, decimal place or None)."""
        if isinstance(node, ast.Constant) and isinstance(
                node.value, (int, float)) and not isinstance(
                node.value, bool):
            return float(node.value), EXACT, None
        if isinstance(node, ast.Name):
            if node.id in self.by_name:
                return self.leaf(node.id)
            if node.id in self.NUMBERS:
                return self.NUMBERS[node.id], EXACT, None
            raise Stop("CANNOT JUDGE", "the name %s" % node.id)
        if isinstance(node, ast.Attribute) and node.attr in self.NUMBERS:
            return self.NUMBERS[node.attr], EXACT, None
        if isinstance(node, ast.UnaryOp) and isinstance(
                node.op, (ast.USub, ast.UAdd)):
            value, figs, place = self.ev(node.operand)
            return (-value if isinstance(node.op, ast.USub) else value,
                    figs, place)
        if isinstance(node, ast.BinOp):
            left = self.ev(node.left)
            right = self.ev(node.right)
            op = node.op
            if isinstance(op, (ast.Add, ast.Sub)):
                value = (left[0] + right[0] if isinstance(op, ast.Add)
                         else left[0] - right[0])
                places = [p for p in (left[2], right[2]) if p is not None]
                if not places:
                    return value, EXACT, None
                place = max(places)
                if value == 0:
                    raise Stop("CANNOT JUDGE", "a sum or difference in the "
                               "expression is exactly zero")
                return value, max(0, magnitude(value) - place + 1), place
            if isinstance(op, ast.Mult):
                value = left[0] * right[0]
            elif isinstance(op, ast.Div):
                value = left[0] / right[0]
            elif isinstance(op, ast.Pow):
                value = left[0] ** right[0]
            else:
                raise Stop("CANNOT JUDGE", "a %s operator"
                           % type(op).__name__)
            return self.limited(value, [left[1], right[1]])
        if isinstance(node, ast.Call):
            func = node.func
            fname = (func.attr if isinstance(func, ast.Attribute) else
                     func.id if isinstance(func, ast.Name) else None)
            if fname not in self.FUNCS or node.keywords:
                raise Stop("CANNOT JUDGE", "the call %s()" % fname)
            parts = [self.ev(arg) for arg in node.args]
            value = self.FUNCS[fname](*[p[0] for p in parts])
            return self.limited(value, [p[1] for p in parts])
        raise Stop("CANNOT JUDGE", "a %s node" % type(node).__name__)

    def limited(self, value, counts):
        """Fewest figures among the non-exact counts."""
        counts = [c for c in counts if c is not EXACT]
        if not counts:
            return value, EXACT, None
        figs = min(counts)
        if value == 0:
            return value, figs, None
        return value, figs, magnitude(value) - figs + 1


def stated_number(text):
    """(literal, has_ellipsis) for the last '= number' in a comment."""
    found = STATED_RE.findall(text or "")
    if not found:
        return None
    literal, dots = found[-1]
    return literal, bool(dots)


def check_comment(row, value, declared):
    """Check 4. Returns (verdict, detail) or None when it passes."""
    stated = stated_number(row.derived_text)
    if stated is None:
        return None
    literal, dots = stated
    number = float(literal.replace(",", ""))
    low, high = literal_figures(literal)
    matching = []
    for figs in range(low, high + 1):
        if math.isclose(round_to(value, figs), number, rel_tol=1e-12):
            matching.append(figs)
        elif dots and math.isclose(truncate_to(value, figs), number,
                                   rel_tol=1e-12):
            matching.append(figs)
    if not matching:
        return ("COMMENT DISAGREES",
                "the # Derived: line states %s; the row's value %r rounds "
                "to %g at %d figures" % (literal, value,
                                         round_to(value, low), low))
    if min(matching) > declared:
        return ("COMMENT OVERSTATES",
                "the # Derived: line states %s, %d figures; the row declares "
                "%d" % (literal, min(matching), declared))
    return None


def judge_row(row, by_name, values, transitional):
    """A list of (verdict, detail) findings; empty means OK."""
    findings = []
    is_trans = row.name in transitional
    is_expr = row.kind == "expression"

    if row.figures_error:
        return [("MALFORMED", row.figures_error)]
    if row.figures is None:
        findings.append(("NOT YET MIGRATED", "no # Figures: line"))
    if is_expr and row.derived_text is None:
        findings.append(("NO DERIVED LINE", "an expression with no "
                         "# Derived: line of its own"))
    if row.figures is None or not (is_expr or is_trans):
        return findings

    known = set(by_name)
    if is_expr:
        inputs = list(row.inputs)
    else:
        inputs = constants_rows.names_in(
            (row.status or "") + " " + (row.derived_text or ""), known)
        inputs = [n for n in inputs if n != row.name]

    # check 2
    named = [n for n in constants_rows.names_in(row.figures_text, known)
             if n != row.name]
    strays = [n for n in named if n not in inputs]
    if strays:
        findings.append(("NAMES A NON-INPUT", "# Figures: names %s, which "
                         "the %s does not use" % (", ".join(strays),
                                                  "expression" if is_expr
                                                  else "Status line")))
    if isinstance(row.figures, int) and not named:
        findings.append(("NAMES NO INPUT", "# Figures: declares %d but names "
                         "no input that set it" % row.figures))

    # check 3
    try:
        if is_expr:
            walker = Figures(by_name, values)
            value, supported, _place = walker.ev(row.node)
        else:
            value = values.get(row.name)
            counts = []
            for name in inputs:
                _v, figs, _p = Figures(by_name, values).leaf(name)
                if figs is not EXACT:
                    counts.append(figs)
            supported = min(counts) if counts else EXACT
    except Stop as stop:
        findings.append((stop.verdict, stop.detail))
        return findings

    if row.figures == "exact":
        if supported is not EXACT:
            findings.append(("OVER-DECLARED", "declares exact, but its "
                             "inputs support %d figures" % supported))
    elif supported is not EXACT and row.figures > supported:
        findings.append(("OVER-DECLARED", "declares %d figures; its inputs "
                         "support %d" % (row.figures, supported)))

    # check 4
    if (is_expr and isinstance(row.figures, int)
            and row.derived_text is not None):
        problem = check_comment(row, value, row.figures)
        if problem:
            findings.append(problem)
    return findings


def judge(rows, by_name, values, closed, transitional):
    """[(verdict, name, detail, fails, kind)] for every row it reads."""
    results = []
    for row in rows:
        is_trans = row.name in transitional
        if not (row.kind == "expression" or is_trans
                or row.derived_text is not None):
            continue
        kind = ("transitional" if is_trans else
                "expression" if row.kind == "expression" else "typed")
        findings = judge_row(row, by_name, values, transitional)
        if not findings:
            if row.figures == "exact":
                detail = "exact"
            elif kind == "typed":
                detail = "%s figures; a typed number, check 1 only" \
                    % row.figures
            else:
                detail = "%s figures, within what its inputs support" \
                    % row.figures
            results.append(("OK", row.name, detail, False, kind))
            continue
        closed_row = constants_rows.in_closed_slice(row.name, closed)
        for verdict, detail in findings:
            fails = verdict in FAILING or (verdict in GAPS and closed_row)
            results.append((verdict, row.name, detail, fails, kind))
    return results


# ------------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------------

FIXTURE_STORE = '''
FIX_R_KM = 6378.1366
# Figures: 8 -- source states it to 0.1 m
FIX_A_KM = 1221.5
# Figures: 5 -- source
FIX_MEAN_KM = 6371.0
# Figures: 5 -- source
FIX_DEPTH_KM = 660.0
# Figures: 2 -- the trailing zero is not significant
FIX_ALT_KM = 200.0
# Figures: exact -- a declared drawing condition
FIX_UNMIGRATED_KM = 42.0
FIX_ZERO = 0.0
# Figures: 2 -- a measured zero
FIX_QUOT = FIX_A_KM / FIX_R_KM
# Figures: 5 -- set by FIX_A_KM (1221.5, 5)
# Derived: 1221.5 / 6378.1366 = 0.19151
FIX_OVER = FIX_A_KM / FIX_R_KM
# Figures: 6 -- set by FIX_A_KM
# Derived: = 0.191514
FIX_DIFF = FIX_MEAN_KM - FIX_DEPTH_KM
# Figures: 4 -- set by FIX_DEPTH_KM
# Derived: 6371.0 - 660 = 5711
FIX_DIFF_OK = FIX_MEAN_KM - FIX_DEPTH_KM
# Figures: 3 -- set by FIX_DEPTH_KM, good to tens
# Derived: 6371.0 - 660 = 5710
FIX_SUM_EXACT = FIX_R_KM + FIX_ALT_KM
# Figures: 8 -- set by FIX_R_KM, the altitude is exact
# Derived: 6378.1366 + 200 = 6578.1366
FIX_WRONG_NAME = FIX_A_KM / FIX_R_KM
# Figures: 5 -- set by FIX_MEAN_KM
# Derived: = 0.19151
FIX_NO_NAME = FIX_A_KM / FIX_R_KM
# Figures: 5 -- from the numerator
# Derived: = 0.19151
FIX_COMMENT = FIX_A_KM / FIX_R_KM
# Figures: 5 -- set by FIX_A_KM
# Derived: 1221.5 / 6378.1366 = 0.19152
FIX_COMMENT_SHORT = FIX_A_KM / FIX_R_KM
# Figures: 5 -- set by FIX_A_KM
# Derived: = 0.1915
FIX_COMMENT_LONG = FIX_A_KM / FIX_R_KM
# Figures: 4 -- set by FIX_A_KM, one dropped by choice
# Derived: = 0.19151
FIX_NOT_MIGRATED = FIX_A_KM / FIX_R_KM
# Derived: = 0.19151
FIX_INPUT_GAP = FIX_UNMIGRATED_KM / FIX_R_KM
# Figures: 2 -- set by FIX_UNMIGRATED_KM
# Derived: = 0.0066
FIX_NO_DERIVED = FIX_A_KM / FIX_R_KM
# Figures: 5 -- set by FIX_A_KM
FIX_EXACT = FIX_ALT_KM * 2
# Figures: exact -- twice a declared condition
# Derived: = 400
FIX_EXACT_WRONG = FIX_A_KM * 2
# Figures: exact -- claimed
# Derived: = 2443
FIX_ZERO_IN = FIX_ZERO + FIX_A_KM
# Figures: 2 -- set by FIX_ZERO
# Derived: = 1200
FIX_POWER = FIX_A_KM ** (1.0 / 3.0)
# Figures: 5 -- set by FIX_A_KM; a cube root does not magnify
# Derived: = 10.690
FIX_TYPED = 3.0
# Derived: typed from prose
FIX_TYPED_DONE = 3.0
# Figures: 2 -- source
# Derived: typed from prose
FIX_BAD_FIG = FIX_A_KM / FIX_R_KM
# Figures: many
# Derived: = 0.19151
FIX_TRANS = 0.19151
# Status: derived -- inherits FIX_A_KM and FIX_R_KM
# Figures: 5 -- set by FIX_A_KM
# Derived: 1221.5 / 6378.1366
FIX_TRANS_OVER = 0.191514
# Status: derived -- inherits FIX_A_KM and FIX_R_KM
# Figures: 6 -- set by FIX_A_KM
# Derived: 1221.5 / 6378.1366
'''

FIXTURE_TRANSITIONAL = ("FIX_TRANS", "FIX_TRANS_OVER")

FIXTURE_EXPECTED = {
    "FIX_QUOT": ["OK"],
    "FIX_OVER": ["OVER-DECLARED"],
    "FIX_DIFF": ["OVER-DECLARED"],
    "FIX_DIFF_OK": ["OK"],
    "FIX_SUM_EXACT": ["OK"],
    "FIX_WRONG_NAME": ["NAMES A NON-INPUT"],
    "FIX_NO_NAME": ["NAMES NO INPUT"],
    "FIX_COMMENT": ["COMMENT DISAGREES"],
    "FIX_COMMENT_SHORT": ["OK"],
    "FIX_COMMENT_LONG": ["COMMENT OVERSTATES"],
    "FIX_NOT_MIGRATED": ["NOT YET MIGRATED"],
    "FIX_INPUT_GAP": ["INPUT NOT YET MIGRATED"],
    "FIX_NO_DERIVED": ["NO DERIVED LINE"],
    "FIX_EXACT": ["OK"],
    "FIX_EXACT_WRONG": ["OVER-DECLARED"],
    "FIX_ZERO_IN": ["CANNOT JUDGE"],
    "FIX_POWER": ["OK"],
    "FIX_TYPED": ["NOT YET MIGRATED"],
    "FIX_TYPED_DONE": ["OK"],
    "FIX_BAD_FIG": ["MALFORMED"],
    "FIX_TRANS": ["OK"],
    "FIX_TRANS_OVER": ["OVER-DECLARED"],
}


def run_fixtures():
    rows, by_name = constants_rows.parse_store_text(FIXTURE_STORE)
    values = {}
    exec(compile(FIXTURE_STORE, "fixture", "exec"), values)
    problems = []
    results = judge(rows, by_name, values, (), FIXTURE_TRANSITIONAL)
    got = {}
    for verdict, name, detail, fails, _kind in results:
        got.setdefault(name, []).append((verdict, detail, fails))
    for name, expected in sorted(FIXTURE_EXPECTED.items()):
        verdicts = [v for v, _d, _f in got.get(name, [])]
        if verdicts != expected:
            problems.append("%s: expected %s, got %s %s"
                            % (name, expected, verdicts,
                               [d for _v, d, _f in got.get(name, [])]))
    for name in got:
        if name not in FIXTURE_EXPECTED:
            problems.append("%s: judged but has no expected verdict" % name)
    if any(f for _v, _d, f in got.get("FIX_NOT_MIGRATED", [])):
        problems.append("FIX_NOT_MIGRATED: a gap failed outside a closed "
                        "slice")
    closed = judge(rows, by_name, values, ("FIX",), FIXTURE_TRANSITIONAL)
    if not any(fails for v, name, _d, fails, _k in closed
               if name == "FIX_NOT_MIGRATED"):
        problems.append("FIX_NOT_MIGRATED: a gap did not fail inside a "
                        "closed slice")
    return problems, len(FIXTURE_EXPECTED)


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))

    print("=" * 70)
    print("  DERIVED FIGURES -- %s (Rule 8)" % constants_rows.STORE)
    print("=" * 70)
    print("")

    fixture_problems, fixture_count = run_fixtures()
    if fixture_problems:
        print("FIXTURES FAILED -- the checker itself is broken:")
        for line in fixture_problems:
            print("  " + line)
    else:
        print("Fixtures: %d built-in rows gave their expected verdicts, "
              "including a gap failing inside a closed slice."
              % fixture_count)
    print("")

    try:
        _text, rows, by_name = constants_rows.read_store(project_dir)
        values = constants_rows.load_values(project_dir)
    except Exception as exc:                          # noqa: BLE001
        print("ERROR: %s could not be read or run: %s"
              % (constants_rows.STORE, exc))
        return 1

    closed = constants_rows.CLOSED_SLICES
    results = judge(rows, by_name, values, closed,
                    constants_rows.TRANSITIONAL)
    names = []
    kinds = {}
    for verdict, name, _d, _f, kind in results:
        if name not in names:
            names.append(name)
            kinds[kind] = kinds.get(kind, 0) + 1

    print("Rows read: %d -- %d expression(s), %d transitional, %d typed "
          "number(s) with a # Derived: note."
          % (len(names), kinds.get("expression", 0),
             kinds.get("transitional", 0), kinds.get("typed", 0)))
    print("")

    order = FAILING + ("OK",) + GAPS
    grouped = {}
    for verdict, name, detail, fails, _kind in results:
        grouped.setdefault(verdict, []).append((name, detail, fails))
    for verdict in order:
        items = grouped.get(verdict)
        if not items:
            continue
        print("%s (%d)" % (verdict, len(items)))
        if verdict in GAPS and not any(f for _n, _d, f in items):
            for line in constants_rows.wrap_names([n for n, _d, _f in items]):
                print(line)
        else:
            for name, detail, fails in items:
                print("  %-38s %s%s" % (name, detail,
                                        "  FAIL" if fails else ""))
        print("")
    print("Closed slices: %s." % (", ".join(closed) if closed else
                                  "none yet, so every gap above is named, "
                                  "not failed"))
    print("")

    failures = [(name, "%s: %s" % (verdict, detail))
                for verdict, name, detail, fails, _k in results if fails]
    failures += [("(fixture)", line) for line in fixture_problems]
    ok = len(grouped.get("OK", []))
    counts = ", ".join("%d %s" % (len(grouped[v]), v) for v in order
                       if grouped.get(v))
    if failures:
        print("FAILURES (%d):" % len(failures))
        for name, message in failures:
            print("  %-38s %s" % (name, message))
        print("")
        print("%d finding(s) fail across %d derived row(s) read (%s)."
              % (len(failures), len(names), counts))
        return 1
    print("No figure count exceeds its inputs: %d derived row(s) read, "
          "%d judged OK -- %s." % (len(names), ok, counts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
