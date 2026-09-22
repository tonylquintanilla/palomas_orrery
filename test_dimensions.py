"""
test_dimensions.py -- a derived constant's unit follows from its
arithmetic.

WHY THIS EXISTS

    A "# Unit:" line is a claim. For a typed number nothing in the file
    can contradict it. For a row computed from other rows, the claim can
    be CHECKED: work out the unit the arithmetic produces and compare it
    with the unit the row declares. Tony's ruling of 2026-09-11 (L-322,
    ruling 4): dimensional analysis is the real check on a unit, not a
    text match. His ruling of 2026-09-16: astropy does the unit algebra
    INSIDE this check, and the store keeps plain floats.

RUN COMMAND

    python test_dimensions.py

    Open it in VS Code and click Run. orrery_maintenance_run.py runs it
    on every maintenance run.

HOW IT WORKS

    Each token in constants_tokens.py becomes an astropy unit. A token
    with a defining constant is that many of its dimension's unit, the
    factor read from the store by name. A token whose dimension is
    "named number" (l_shell) becomes an irreducible unit that compares
    with nothing else.

    For each derived row, every store name in its expression becomes the
    store's float times its token's unit. The expression is evaluated,
    and the result is compared with the row's own token twice: once for
    DIMENSION (a length is not a pressure), and once for SCALE (the result
    converted into the row's token must equal the number the store
    holds). The second comparison is what catches a row declared in Earth
    radii whose value is really in kilometres, which a dimension check
    alone would pass. It also proves this check evaluated the same
    arithmetic Python did.

RULES NO UNIT ALGEBRA CARRIES (build manifest, section 7; one more at L-322 C2)

    Dividing by a defining constant is a CONVERSION. EARTH_INNER_CORE_KM /
    EARTH_EQUATORIAL_RADIUS_KM is km/km to astropy and Earth radii to the
    store. When an expression divides by a row that defines a token, the
    numerator is converted into that token instead. The defining row must
    itself declare the token's dimension; otherwise the conversion would
    rest on a unit nobody declared.

    Multiplying by a defining constant is the SAME conversion run back.
    EARTH_MAGNETOPAUSE_STANDOFF_RADII * EARTH_EQUATORIAL_RADIUS_KM is
    Earth radii times kilometres -- an area -- to astropy, and kilometres
    to the store. When one factor is a defining constant and the other is
    a quantity in exactly that constant's token, the product is the other
    factor converted out of the token into the token's dimension. A
    factor in any other unit multiplies as usual, so kilometres times
    Earth's radius still reads as an area and fails. (L-322 Stage C2,
    2026-09-22: the manifest's four new kilometre rows are the first rows
    of this shape, and without the rule they are MISMATCH.)

    A non-integer power of a single declared input is taken on the number
    in its declared unit. Shue's Dp^(-1/a5) and Jelinek's p^(-1/eps) are
    empirical fits whose coefficients absorb the unit; astropy would
    return nanopascals to a fractional power. The rule fires only when
    the plain power would leave a fractional unit power AND the base is a
    single store name. A computed base, such as the geostationary radius's
    (GM / w^2)^(1/3), keeps its units, because there the power is
    physics. Every firing is printed on the row's line.

    An exponent must be a pure number. A named pure number (a token like
    l_shell) is used by its value, and the row's line says so. The
    argument of a function such as tanh is reduced to a plain number when
    its units cancel (a per-nanotesla times a nanotesla), because astropy
    only accepts units that cancel by name.

WHAT IT PRINTS, per row, and what FAILS

    OK               the unit follows from the arithmetic
    MISMATCH         it does not, in dimension or in scale            FAIL
    UNKNOWN TOKEN    a token neither defined nor retired              FAIL
    CANNOT EVALUATE  the expression uses something this check cannot
                     evaluate; the row is unjudged, so it fails       FAIL
    NO UNIT          the row has no "# Unit:" line yet                gap
    INPUT NO UNIT    an input has none yet                            gap
    RETIRED TOKEN    the row, or an input, still says "dimensionless" gap
    NOT CHECKABLE    a derived-looking row with no expression to
                     evaluate: the two transitional standoffs, and
                     literals that carry a "# Derived:" note

    A gap FAILS when the row is inside a closed slice
    (constants_rows.CLOSED_SLICES, empty until the Earth walk finishes).
    Every other row in the store is a typed number or a table: nothing in
    the file can contradict its unit, so it is counted, not judged.

THE FIXTURES RUN FIRST, EVERY TIME

    Until the Earth walk writes units on derived rows, every real verdict
    is a gap, and a green run would say nothing about whether this check
    can fail. So a small built-in store runs first, through the same
    code, and every verdict above must come out as expected -- including
    both hand rules, a real mismatch, and a gap that fails inside a
    closed slice. If any fixture verdict is wrong, the run fails: the
    checker itself is broken.

Role: devtool
Domain: dev_tools

Module created: September 16, 2026 with Anthropic's Claude Opus 5
(L-322, the mechanism: piece 4 of the build manifest).
Module updated: September 22, 2026 with Anthropic's Claude Opus 5
(L-322 Stage C2: multiplying by a defining constant converts out of its
token, the division rule run back, with a fixture that passes and one
that fails.)
"""

import ast
import math
import os
import sys

import numpy as np

import constants_rows
from constants_tokens import NAMED_NUMBER, RETIRED_TOKENS, TOKENS

REL_TOL = 1e-9

FAILING = ("MISMATCH", "UNKNOWN TOKEN", "CANNOT EVALUATE")
GAPS = ("NO UNIT", "INPUT NO UNIT", "RETIRED TOKEN")

FUNCTIONS = {
    "tanh": np.tanh, "sinh": np.sinh, "cosh": np.cosh,
    "exp": np.exp, "log": np.log, "log10": np.log10,
    "sqrt": np.sqrt, "cbrt": np.cbrt, "abs": np.abs, "fabs": np.abs,
    "sin": np.sin, "cos": np.cos, "tan": np.tan,
    "arcsin": np.arcsin, "asin": np.arcsin,
    "arccos": np.arccos, "acos": np.arccos,
    "arctan": np.arctan, "atan": np.arctan,
    "radians": np.radians, "degrees": np.degrees,
}
NUMBERS = {"pi": math.pi, "e": math.e}


class Verdict(Exception):
    """Raised mid-evaluation when a row cannot be judged."""

    def __init__(self, verdict, detail):
        Exception.__init__(self, detail)
        self.verdict = verdict
        self.detail = detail


def build_units(tokens, values):
    """({token: astropy unit}, set of irreducible units, problems)."""
    from astropy import units as u
    units = {}
    named = set()
    problems = []
    for token, spec in tokens.items():
        dimension = spec.get("dimension")
        defining = spec.get("defining_constant")
        try:
            if dimension == NAMED_NUMBER:
                unit = u.def_unit(token)
                named.add(unit)
            else:
                base = u.Unit(dimension)
                if defining is None:
                    unit = u.def_unit(token, base)
                else:
                    factor = values.get(defining)
                    if not isinstance(factor, (int, float)) or isinstance(
                            factor, bool):
                        problems.append((token, "defining_constant %s has no "
                                         "numeric value in the store"
                                         % defining))
                        continue
                    unit = u.def_unit(token, factor * base)
        except Exception as exc:                      # noqa: BLE001
            problems.append((token, "dimension %r is not an astropy unit "
                             "(%s)" % (dimension, exc)))
            continue
        units[token] = unit
    return units, named, problems


class Evaluator(object):
    """Evaluate one expression with units attached to its store names."""

    def __init__(self, by_name, values, units, named, tokens, retired):
        self.by_name = by_name
        self.values = values
        self.units = units
        self.named = named
        self.tokens = tokens
        self.retired = retired
        self.defining = dict((spec["defining_constant"], token)
                             for token, spec in tokens.items()
                             if spec.get("defining_constant"))
        self.notes = []

    # -- leaves -------------------------------------------------------

    def quantity(self, name):
        row = self.by_name[name]
        if row.unit is None:
            raise Verdict("INPUT NO UNIT", "input %s has no # Unit: line"
                          % name)
        if row.unit in self.retired:
            raise Verdict("RETIRED TOKEN", "input %s still declares '%s'"
                          % (name, row.unit))
        if row.unit not in self.units:
            raise Verdict("UNKNOWN TOKEN", "input %s declares '%s', which "
                          "constants_tokens.py does not define"
                          % (name, row.unit))
        value = self.values.get(name)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise Verdict("CANNOT EVALUATE", "input %s is not a number"
                          % name)
        return value * self.units[row.unit]

    def plain(self, value, what):
        """A pure number from `value`, for an exponent."""
        from astropy import units as u
        if not isinstance(value, u.Quantity):
            return float(value)
        unit = value.unit.decompose()
        if unit == u.dimensionless_unscaled:
            return float(value.to_value(u.dimensionless_unscaled))
        if unit.bases and all(base in self.named for base in unit.bases):
            self.notes.append("%s used as a number (%s)" % (what, value.unit))
            return float(value.value)
        raise Verdict("CANNOT EVALUATE", "%s carries the unit %s; an "
                      "exponent must be a pure number" % (what, value.unit))

    def dimensionless_to_number(self, value):
        """A plain float for an argument whose units cancel.

        astropy accepts tanh(x) only when x is an angle or is
        dimensionless BY NAME; per_nt times nt cancels only after
        decomposition, so it is reduced here. Anything that does not
        cancel is passed through, and astropy refuses it.
        """
        from astropy import units as u
        if (isinstance(value, u.Quantity)
                and value.unit.decompose() == u.dimensionless_unscaled):
            return float(value.to_value(u.dimensionless_unscaled))
        return value

    # -- nodes --------------------------------------------------------

    def ev(self, node):
        from astropy import units as u
        if isinstance(node, ast.Constant):
            if isinstance(node.value, bool) or not isinstance(
                    node.value, (int, float)):
                raise Verdict("CANNOT EVALUATE", "a %s constant"
                              % type(node.value).__name__)
            return node.value
        if isinstance(node, ast.Name):
            if node.id in self.by_name:
                return self.quantity(node.id)
            if node.id in NUMBERS:
                return NUMBERS[node.id]
            raise Verdict("CANNOT EVALUATE", "the name %s is not a store row"
                          % node.id)
        if isinstance(node, ast.Attribute):
            if node.attr in NUMBERS:
                return NUMBERS[node.attr]
            raise Verdict("CANNOT EVALUATE", "the attribute .%s" % node.attr)
        if isinstance(node, ast.UnaryOp):
            operand = self.ev(node.operand)
            if isinstance(node.op, ast.USub):
                return -operand
            if isinstance(node.op, ast.UAdd):
                return operand
            raise Verdict("CANNOT EVALUATE", "a %s operator"
                          % type(node.op).__name__)
        if isinstance(node, ast.BinOp):
            return self.binop(node)
        if isinstance(node, ast.Call):
            func = node.func
            fname = (func.attr if isinstance(func, ast.Attribute) else
                     func.id if isinstance(func, ast.Name) else None)
            if fname not in FUNCTIONS or node.keywords:
                raise Verdict("CANNOT EVALUATE", "the call %s()" % fname)
            args = [self.dimensionless_to_number(self.ev(arg))
                    for arg in node.args]
            return FUNCTIONS[fname](*args)
        raise Verdict("CANNOT EVALUATE", "a %s node" % type(node).__name__)

    def binop(self, node):
        from astropy import units as u
        op = node.op
        if (isinstance(op, ast.Div) and isinstance(node.right, ast.Name)
                and node.right.id in self.defining):
            token = self.defining[node.right.id]
            left = self.ev(node.left)
            if (isinstance(left, u.Quantity)
                    and left.unit.is_equivalent(self.units[token])):
                right = self.quantity(node.right.id)
                wanted = u.Unit(self.tokens[token]["dimension"])
                if not math.isclose(right.unit.to(wanted), 1.0,
                                    rel_tol=REL_TOL):
                    raise Verdict("MISMATCH", "%s defines '%s' in %s but "
                                  "declares %s" % (node.right.id, token,
                                                   wanted, right.unit))
                self.notes.append("divided by %s: converted into %s"
                                  % (node.right.id, token))
                return left.to(self.units[token])
            right = self.ev(node.right)
            return left / right
        if isinstance(op, ast.Mult):
            left = self.ev(node.left)
            right = self.ev(node.right)
            for const_node, const, other in ((node.right, right, left),
                                             (node.left, left, right)):
                if not (isinstance(const_node, ast.Name)
                        and const_node.id in self.defining
                        and isinstance(other, u.Quantity)):
                    continue
                token = self.defining[const_node.id]
                if other.unit != self.units[token]:
                    continue
                wanted = u.Unit(self.tokens[token]["dimension"])
                if not math.isclose(const.unit.to(wanted), 1.0,
                                    rel_tol=REL_TOL):
                    raise Verdict("MISMATCH", "%s defines '%s' in %s but "
                                  "declares %s" % (const_node.id, token,
                                                   wanted, const.unit))
                self.notes.append("multiplied by %s: converted out of %s "
                                  "into %s" % (const_node.id, token, wanted))
                return other.to(wanted)
            return left * right
        if isinstance(op, ast.Pow):
            base = self.ev(node.left)
            exponent = self.plain(self.ev(node.right), "the exponent")
            if (isinstance(base, u.Quantity)
                    and float(exponent) != int(exponent)):
                trial = base ** exponent
                powers = trial.unit.decompose().powers
                fractional = any(float(p) != int(p) for p in powers)
                if fractional and isinstance(node.left, ast.Name):
                    self.notes.append("power rule: %s taken as a number in "
                                      "%s" % (node.left.id, base.unit))
                    return base.value ** exponent
                return trial
            return base ** exponent
        left = self.ev(node.left)
        right = self.ev(node.right)
        if isinstance(op, ast.Add):
            return left + right
        if isinstance(op, ast.Sub):
            return left - right
        if isinstance(op, ast.Mult):
            return left * right
        if isinstance(op, ast.Div):
            return left / right
        raise Verdict("CANNOT EVALUATE", "a %s operator" % type(op).__name__)


def judge_row(row, ctx):
    """(verdict, detail) for one derived row with an expression."""
    from astropy import units as u
    by_name, values, units, named, tokens, retired = ctx
    if row.unit_error:
        return "CANNOT EVALUATE", row.unit_error
    if row.unit is None:
        return "NO UNIT", "no # Unit: line"
    if row.unit in retired:
        return "RETIRED TOKEN", "declares '%s'" % row.unit
    if row.unit not in units:
        return "UNKNOWN TOKEN", ("declares '%s', which constants_tokens.py "
                                 "does not define" % row.unit)
    evaluator = Evaluator(by_name, values, units, named, tokens, retired)
    try:
        result = evaluator.ev(row.node)
    except Verdict as stop:
        return stop.verdict, stop.detail
    except u.UnitsError as exc:
        return "MISMATCH", "the arithmetic is not dimensionally " \
                           "consistent: %s" % exc
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        return "CANNOT EVALUATE", str(exc)
    notes = ("; " + "; ".join(evaluator.notes)) if evaluator.notes else ""
    if not isinstance(result, u.Quantity):
        result = result * u.dimensionless_unscaled
    declared = units[row.unit]
    if not result.unit.is_equivalent(declared):
        return "MISMATCH", ("declares %s (%s); the arithmetic gives %s%s"
                            % (row.unit, declared.decompose(),
                               result.unit.decompose(), notes))
    converted = float(result.to_value(declared))
    stored = values.get(row.name)
    if not isinstance(stored, (int, float)) or not math.isclose(
            converted, stored, rel_tol=REL_TOL, abs_tol=0.0):
        return "MISMATCH", ("the arithmetic gives %.10g %s; the store holds "
                            "%r%s" % (converted, row.unit, stored, notes))
    return "OK", "%.6g %s%s" % (converted, row.unit, notes)


def judge(rows, by_name, values, tokens, retired, closed):
    """Return (results, others, table_problems).

    results: [(verdict, name, detail, fails)] for every derived-looking
    row. others: the count of every other row.
    """
    units, named, table_problems = build_units(tokens, values)
    ctx = (by_name, values, units, named, tokens, retired)
    results = []
    others = 0
    for row in rows:
        if row.transitional:
            results.append(("NOT CHECKABLE", row.name,
                            "transitional literal; its arithmetic lives in "
                            "its # Derived: line until it reverts", False))
            continue
        if row.kind != "expression":
            if row.derived_text is not None:
                results.append(("NOT CHECKABLE", row.name,
                                "a typed number with a # Derived: note",
                                False))
            else:
                others += 1
            continue
        verdict, detail = judge_row(row, ctx)
        fails = verdict in FAILING or (
            verdict in GAPS and constants_rows.in_closed_slice(row.name,
                                                               closed))
        results.append((verdict, row.name, detail, fails))
    return results, others, table_problems


# ------------------------------------------------------------------
# Fixtures: a built-in store that must produce every verdict.
# ------------------------------------------------------------------

FIXTURE_TOKENS = dict((token, spec) for token, spec in TOKENS.items()
                      if spec.get("defining_constant") is None)
FIXTURE_TOKENS.update({
    "fx_r": {"dimension": "km", "defining_constant": "FIX_R_KM",
             "meaning": "fixture radius"},
    "fx_exponent": {"dimension": NAMED_NUMBER, "defining_constant": None,
                    "meaning": "fixture named pure number"},
    "fx_km3_s2": {"dimension": "km3 / s2", "defining_constant": None,
                  "meaning": "fixture"},
    "fx_per_s": {"dimension": "1 / s", "defining_constant": None,
                 "meaning": "fixture"},
    "fx_m": {"dimension": "m", "defining_constant": None,
             "meaning": "fixture"},
})

FIXTURE_STORE = '''
import numpy as np
FIX_R_KM = 6378.0
# Unit: km
FIX_A_KM = 1275.6
# Unit: km
FIX_A1_R = 10.22
# Unit: fx_r
FIX_A2_R = 1.29
# Unit: fx_r
FIX_A3 = 0.184
# Unit: per_nt
FIX_A4 = 8.14
# Unit: nt
FIX_A5 = 6.6
# Unit: fx_exponent
FIX_P_NPA = 2.0
# Unit: npa
FIX_BZ = 0.0
# Unit: nt
FIX_GM = 398600.4418
# Unit: fx_km3_s2
FIX_W = 7.292115e-5
# Unit: fx_per_s
FIX_BARE = 4.0
FIX_OLD = 3.0
# Unit: dimensionless
FIX_LITERAL = 3.0
# Derived: 1.5 x 2
FIX_CONVERTED = FIX_A_KM / FIX_R_KM
# Unit: fx_r
FIX_UNCONVERTED = FIX_A_KM / FIX_R_KM
# Unit: km
FIX_SUM_KM = FIX_R_KM + FIX_A_KM
# Unit: km
FIX_BAD_SUM = FIX_R_KM + FIX_P_NPA
# Unit: km
FIX_SHUE = (FIX_A1_R + FIX_A2_R * np.tanh(FIX_A3 * (FIX_BZ + FIX_A4))) * FIX_P_NPA ** (-1.0 / FIX_A5)
# Unit: fx_r
FIX_GEO = (FIX_GM / FIX_W ** 2) ** (1.0 / 3.0)
# Unit: km
FIX_EMBEDDED = FIX_A_KM * 1000
# Unit: fx_m
FIX_UNIT_MISSING = FIX_A_KM * 2
FIX_INPUT_MISSING = FIX_BARE * FIX_A_KM
# Unit: km
FIX_INPUT_RETIRED = FIX_OLD * FIX_A_KM
# Unit: km
FIX_UNKNOWN = FIX_A_KM * 2
# Unit: furlong
FIX_CALL = FIX_A_KM * round(FIX_A5)
# Unit: km
FIX_BACK = FIX_CONVERTED * FIX_R_KM
# Unit: km
FIX_BACK_AREA = FIX_A_KM * FIX_R_KM
# Unit: km
'''

FIXTURE_EXPECTED = {
    "FIX_LITERAL": ["NOT CHECKABLE"],
    "FIX_CONVERTED": ["OK"],
    "FIX_UNCONVERTED": ["MISMATCH"],
    "FIX_SUM_KM": ["OK"],
    "FIX_BAD_SUM": ["MISMATCH"],
    "FIX_SHUE": ["OK"],
    "FIX_GEO": ["OK"],
    "FIX_EMBEDDED": ["MISMATCH"],
    "FIX_UNIT_MISSING": ["NO UNIT"],
    "FIX_INPUT_MISSING": ["INPUT NO UNIT"],
    "FIX_INPUT_RETIRED": ["RETIRED TOKEN"],
    "FIX_UNKNOWN": ["UNKNOWN TOKEN"],
    "FIX_CALL": ["CANNOT EVALUATE"],
    "FIX_BACK": ["OK"],
    "FIX_BACK_AREA": ["MISMATCH"],
}


def run_fixtures():
    """Return a list of problems; empty means every verdict fired."""
    problems = []
    rows, by_name = constants_rows.parse_store_text(FIXTURE_STORE)
    values = {}
    exec(compile(FIXTURE_STORE, "fixture", "exec"), values)
    results, _others, table = judge(rows, by_name, values, FIXTURE_TOKENS,
                                    RETIRED_TOKENS, ())
    for token, message in table:
        problems.append("fixture token %s: %s" % (token, message))
    got = dict((name, (verdict, detail, fails))
               for verdict, name, detail, fails in results)
    for name, expected in sorted(FIXTURE_EXPECTED.items()):
        verdict = got.get(name, ("(not judged)", "", False))[0]
        if [verdict] != expected:
            problems.append("%s: expected %s, got %s (%s)"
                            % (name, expected, verdict,
                               got.get(name, ("", "", False))[1]))
    for name in got:
        if name not in FIXTURE_EXPECTED:
            problems.append("%s: judged but has no expected verdict" % name)
    if "power rule" not in got.get("FIX_SHUE", ("", "", 0))[1]:
        problems.append("FIX_SHUE: the power rule did not fire")
    if "power rule" in got.get("FIX_GEO", ("", "", 0))[1]:
        problems.append("FIX_GEO: the power rule fired on a computed base")
    if "converted into fx_r" not in got.get("FIX_CONVERTED", ("", "", 0))[1]:
        problems.append("FIX_CONVERTED: the conversion rule did not fire")
    if "converted out of fx_r" not in got.get("FIX_BACK", ("", "", 0))[1]:
        problems.append("FIX_BACK: the multiplication rule did not fire")
    if got.get("FIX_UNIT_MISSING", ("", "", True))[2]:
        problems.append("FIX_UNIT_MISSING: a gap failed outside a closed "
                        "slice")
    closed_results, _o, _t = judge(rows, by_name, values, FIXTURE_TOKENS,
                                   RETIRED_TOKENS, ("FIX",))
    closed_got = dict((name, fails) for _v, name, _d, fails in closed_results)
    if not closed_got.get("FIX_UNIT_MISSING"):
        problems.append("FIX_UNIT_MISSING: a gap did not fail inside a "
                        "closed slice")
    return problems, len(FIXTURE_EXPECTED)


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))

    print("=" * 70)
    print("  DIMENSIONS -- units of derived rows in %s" % constants_rows.STORE)
    print("=" * 70)
    print("")

    try:
        from astropy import units as _u              # noqa: F401
    except ImportError as exc:
        print("ERROR: astropy is not installed (%s). It is in "
              "requirements.txt." % exc)
        return 1

    fixture_problems, fixture_count = run_fixtures()
    if fixture_problems:
        print("FIXTURES FAILED -- the checker itself is broken:")
        for line in fixture_problems:
            print("  " + line)
        print("")
    else:
        print("Fixtures: %d built-in rows gave their expected verdicts, "
              "including the hand rules and a gap failing inside a "
              "closed slice." % fixture_count)
        print("")

    try:
        _text, rows, by_name = constants_rows.read_store(project_dir)
        values = constants_rows.load_values(project_dir)
    except Exception as exc:                          # noqa: BLE001
        print("ERROR: %s could not be read or run: %s"
              % (constants_rows.STORE, exc))
        return 1

    closed = constants_rows.CLOSED_SLICES
    results, others, table = judge(rows, by_name, values, TOKENS,
                                   RETIRED_TOKENS, closed)

    order = ("MISMATCH", "UNKNOWN TOKEN", "CANNOT EVALUATE", "OK",
             "RETIRED TOKEN", "INPUT NO UNIT", "NO UNIT", "NOT CHECKABLE")
    by_verdict = {}
    for verdict, name, detail, fails in results:
        by_verdict.setdefault(verdict, []).append((name, detail, fails))
    for verdict in order:
        items = by_verdict.get(verdict)
        if not items:
            continue
        print("%s (%d)" % (verdict, len(items)))
        if verdict in ("NO UNIT",):
            for line in constants_rows.wrap_names([n for n, _d, _f in items]):
                print(line)
        else:
            for name, detail, fails in items:
                mark = "  FAIL" if fails else ""
                print("  %-38s %s%s" % (name, detail, mark))
        print("")
    print("Every other row: %d. Typed numbers and tables; nothing in the "
          "file can contradict their units, so they are counted, not "
          "judged." % others)
    print("Closed slices: %s." % (", ".join(closed) if closed else
                                  "none yet, so every gap above is named, "
                                  "not failed"))
    print("")

    failures = [(name, "%s: %s" % (verdict, detail))
                for verdict, name, detail, fails in results if fails]
    failures += [(token, message) for token, message in table]
    failures += [("(fixture)", line) for line in fixture_problems]

    judged = len(results)
    counts = ", ".join("%d %s" % (len(by_verdict[v]), v) for v in order
                       if by_verdict.get(v))
    if failures:
        print("FAILURES (%d):" % len(failures))
        for name, message in failures:
            print("  %-38s %s" % (name, message))
        print("")
        print("%d of %d derived row(s) fail the unit check (%s)."
              % (len([r for r in results if r[3]]), judged, counts))
        return 1
    print("No unit contradicts its arithmetic: %d derived row(s) read -- "
          "%s." % (judged, counts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
