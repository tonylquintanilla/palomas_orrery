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
       every input is exact, or when the row is a DECLARED CONSTRUCTION
       (below). For a TRANSITIONAL row there is no expression, so the
       limit is the fewest figures among the inputs its Status line
       names.
    4. The number the "# Derived:" line states (the last "= number" in
       it) is the row's value rounded to no more figures than declared.
       A comment may state fewer; it may not state more, and it may not
       state different digits.
    5. THE CEILING (provenance-discipline 2.16 and 2.17, Rule 3, The
       ceiling; built at L-322 Stage C2). The row is traced through
       every derived row in its chain to its PRIMARIES. If any measured
       primary states an uncertainty in the field form -- the word
       "uncertainty" followed directly by the number, in the row's own
       unit, on its "# Figures:" line -- the ceiling is set by
       propagation: each primary is moved up and down by its stated
       uncertainty, or by its implied half-unit where it states none,
       the row is re-evaluated through its chain from full digits, the
       half-difference is taken (a central difference), and the changes
       are combined by root-sum-square. Declared and exact inputs move
       nothing. The count that uncertainty supports is the place whose
       implied half-unit is closest on a log scale, a tie going to the
       coarser place. Otherwise counting (check 3) is the ceiling.
       It FAILS a row that declares more than its ceiling; a row that
       declares more than counting alone allows without the uncertainty
       form on its own line; a row whose stated uncertainty, rounded to
       the digits it states, differs from the recomputed one (how a
       one-sided step or a rounded intermediate is caught); and a row
       that writes the uncertainty form when no primary in its chain
       states one. The output prints both ceilings where they differ.
    6. Uncertainties are read ONLY from the field, never from prose. A
       primary whose "# Figures:" line mentions an uncertainty in words
       ("uncertainty", "+/-", "standard deviation") but carries no field
       is named, so the blind spot announces instead of passing.

    A DECLARED CONSTRUCTION is a row whose "# Status:" begins "declared"
    (not "declared pending") and whose expression is a stated rule over
    measured rows, such as the midpoint of a sourced band. It may
    declare "exact" over measured inputs, provided every row its
    "# Figures:" line names is in the expression, and every one is
    listed by name in the output so each use is seen (provenance-
    discipline 2.17, Rule 2). A measured or derived row cannot.

    A typed number carrying a "# Derived:" note gets check 1 only: its
    arithmetic lives in prose and there is nothing to follow.

WHAT FAILS, and what is a named gap

    FAIL   OVER-DECLARED, NAMES A NON-INPUT, NAMES NO INPUT,
           COMMENT DISAGREES, COMMENT OVERSTATES, MALFORMED, CANNOT JUDGE,
           NO UNCERTAINTY FORM, UNCERTAINTY DISAGREES,
           UNCERTAINTY UNSUPPORTED
    gap    NOT YET MIGRATED, INPUT NOT YET MIGRATED, NO DERIVED LINE,
           UNCERTAINTY IN PROSE (named on the primary, not the row)

    NAMES A NON-INPUT means a row named on the "# Figures:" line is not
    in the row's CHAIN -- its expression, or a derived row the expression
    uses, followed down to the primaries.

    A gap FAILS inside a closed slice (constants_rows.CLOSED_SLICES,
    empty until the Earth walk finishes). Outside one it is printed by
    name and the run passes. That is Tony's per-slice gate of
    2026-09-14.

THE FIXTURES RUN FIRST, EVERY TIME

    A small built-in store runs first through the same code and must
    produce every verdict above, including a gap that fails inside a
    closed slice, a row that passes only by the uncertainty route, a
    C1-shaped row that counts within its ceiling, and a declared
    construction. If one comes out wrong, the run fails.

Role: devtool
Domain: dev_tools

Module created: September 2026 with Anthropic's Claude Opus 5.
Module rewritten: September 16, 2026 with Anthropic's Claude Opus 5
(L-322, piece 5 of the build manifest: Rule 8 of provenance-discipline
2.13. The formula table and the Status-word enumeration are gone.)
Module updated: September 22, 2026 with Anthropic's Claude Opus 5
(L-322 Stage C2: checks 5 and 6, the uncertainty ceiling and the field
it is read from; declared constructions accepted as exact and listed;
a named input may be anywhere in the row's chain. Section 4.7 and 17.3
of documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md.)
Module updated: September 25, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D8: the uncertainty field's pattern is imported
from constants_rows.py, its one home, rather than kept here.)
"""

import ast
import math
import os
import re
import sys

import constants_rows

FAILING = ("MALFORMED", "CANNOT JUDGE", "OVER-DECLARED",
           "NAMES A NON-INPUT", "NAMES NO INPUT", "COMMENT DISAGREES",
           "COMMENT OVERSTATES", "NO UNCERTAINTY FORM",
           "UNCERTAINTY DISAGREES", "UNCERTAINTY UNSUPPORTED")
GAPS = ("NOT YET MIGRATED", "INPUT NOT YET MIGRATED", "NO DERIVED LINE",
        "UNCERTAINTY IN PROSE")

# The field form of a stated uncertainty (provenance-discipline 2.16,
# Rule 1): the word, then the number, in the row's own unit. The pattern
# lives in constants_rows.py since L-322 Stage D patch D8, so the export
# and the displays read the field exactly as this checker does.
FIELD_RE = constants_rows.UNCERTAINTY_FIELD_RE
# Words that say a primary states an uncertainty. Read only to NAME a
# primary that has no field; never to take a number.
PROSE_RE = re.compile(r"uncertaint|\+/-|standard deviation", re.IGNORECASE)

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


def stated_uncertainty(row):
    """(number, literal) from the field on the row's figures line, or None."""
    match = FIELD_RE.search(row.figures_text or "")
    if not match:
        return None
    literal = match.group(1)
    return abs(float(literal)), literal


def prose_only(row):
    """True when the figures line speaks of an uncertainty but has no field."""
    text = row.figures_text or ""
    return stated_uncertainty(row) is None and bool(PROSE_RE.search(text))


def literal_place(literal):
    """Decimal exponent of the last digit a written number states.

    A whole number's trailing zeros are taken as placeholders, so "850"
    states the tens place -- the reading that fails least often on an
    uncertainty written to one or two figures.
    """
    body = literal.strip().lstrip("+-").lower()
    mantissa, _sep, exponent = body.partition("e")
    shift = int(exponent) if exponent else 0
    if "." in mantissa:
        return shift - len(mantissa.split(".")[1])
    return shift + len(mantissa) - len(mantissa.rstrip("0"))


def reported_place(sigma):
    """The decimal place whose implied half-unit is closest to `sigma`.

    What the reference page says: choose the single number whose implied
    range is close to the measured one. What this project adds (2.16):
    closeness on a log scale, a tie to the coarser place. The half-unit
    at place p is 0.5 x 10^p, so the place is the nearest whole number to
    log10(2 x sigma), rounding a tie up.
    """
    return int(math.floor(math.log10(2.0 * sigma) + 0.5))


def figures_at_place(value, place):
    return max(1, magnitude(value) - place + 1)


class Chain(object):
    """A derived row followed down to its primaries, and re-evaluated.

    A PRIMARY is a row in the chain that is not an expression. A derived
    row the expression uses is not a primary; its own expression is
    followed, so every number is recomputed from the primaries' full
    digits (Rule 4) and no rounded intermediate enters.
    """

    def __init__(self, by_name, values):
        self.by_name = by_name
        self.values = values

    def reached(self, name, seen=None):
        """Every store row the row's expression reaches, in order."""
        seen = [] if seen is None else seen
        row = self.by_name[name]
        if row.kind != "expression":
            return seen
        for used in row.inputs:
            if used not in seen:
                seen.append(used)
                self.reached(used, seen)
        return seen

    def primaries(self, name):
        return [n for n in self.reached(name)
                if self.by_name[n].kind != "expression"]

    def value(self, name, shift=None, memo=None):
        """The row's value, with one primary moved by `shift`=(name, delta)."""
        memo = {} if memo is None else memo
        if name in memo:
            return memo[name]
        row = self.by_name[name]
        if row.kind != "expression":
            result = float(self.values[name])
            if shift is not None and shift[0] == name:
                result += shift[1]
        else:
            result = self._ev(row.node, shift, memo)
        memo[name] = result
        return result

    def _ev(self, node, shift, memo):
        if isinstance(node, ast.Constant):
            return float(node.value)
        if isinstance(node, ast.Name):
            if node.id in self.by_name:
                return self.value(node.id, shift, memo)
            if node.id in Figures.NUMBERS:
                return Figures.NUMBERS[node.id]
            raise Stop("CANNOT JUDGE", "the name %s" % node.id)
        if isinstance(node, ast.Attribute) and node.attr in Figures.NUMBERS:
            return Figures.NUMBERS[node.attr]
        if isinstance(node, ast.UnaryOp):
            operand = self._ev(node.operand, shift, memo)
            return -operand if isinstance(node.op, ast.USub) else operand
        if isinstance(node, ast.BinOp):
            left = self._ev(node.left, shift, memo)
            right = self._ev(node.right, shift, memo)
            op = node.op
            if isinstance(op, ast.Add):
                return left + right
            if isinstance(op, ast.Sub):
                return left - right
            if isinstance(op, ast.Mult):
                return left * right
            if isinstance(op, ast.Div):
                return left / right
            if isinstance(op, ast.Pow):
                return left ** right
        if isinstance(node, ast.Call):
            func = node.func
            fname = (func.attr if isinstance(func, ast.Attribute) else
                     func.id if isinstance(func, ast.Name) else None)
            if fname in Figures.FUNCS and not node.keywords:
                return Figures.FUNCS[fname](
                    *[self._ev(arg, shift, memo) for arg in node.args])
        raise Stop("CANNOT JUDGE", "the chain evaluator cannot read a %s "
                   "node" % type(node).__name__)

    def contribution(self, name):
        """(step, stated) for a primary, or None when it moves nothing."""
        row = self.by_name[name]
        if row.figures is None or row.figures == "exact":
            return None
        if (row.status or "").startswith("declared"):
            return None
        stated = stated_uncertainty(row)
        if stated is not None:
            return stated[0], True
        value = float(self.values[name])
        if value == 0 or not isinstance(row.figures, int):
            return None
        return 0.5 * 10.0 ** (magnitude(value) - row.figures + 1), False

    def propagate(self, name):
        """(sigma, any primary states one, [(primary, effect)])."""
        effects = []
        stated_any = False
        for primary in self.primaries(name):
            step = self.contribution(primary)
            if step is None:
                continue
            size, stated = step
            stated_any = stated_any or stated
            up = self.value(name, (primary, size))
            down = self.value(name, (primary, -size))
            effects.append((primary, (up - down) / 2.0))
        sigma = math.sqrt(sum(effect * effect for _p, effect in effects))
        return sigma, stated_any, effects


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
    """(findings, info) for one row. Empty findings means OK.

    info carries what the OK line prints: the counting ceiling, the
    uncertainty ceiling and the propagated uncertainty where one was
    computed, and whether the row is a declared construction.
    """
    findings = []
    info = {"counting": None, "ceiling_u": None, "sigma": None,
            "construction": False}
    is_trans = row.name in transitional
    is_expr = row.kind == "expression"

    if row.figures_error:
        return [("MALFORMED", row.figures_error)], info
    if row.figures is None:
        findings.append(("NOT YET MIGRATED", "no # Figures: line"))
    if is_expr and row.derived_text is None:
        findings.append(("NO DERIVED LINE", "an expression with no "
                         "# Derived: line of its own"))
    if row.figures is None or not (is_expr or is_trans):
        return findings, info

    known = set(by_name)
    chain = Chain(by_name, values)
    if is_expr:
        inputs = list(row.inputs)
        reach = chain.reached(row.name)
    else:
        inputs = constants_rows.names_in(
            (row.status or "") + " " + (row.derived_text or ""), known)
        inputs = [n for n in inputs if n != row.name]
        reach = list(inputs)
    stated_here = stated_uncertainty(row) if is_expr else None

    # check 2
    named = [n for n in constants_rows.names_in(row.figures_text, known)
             if n != row.name]
    strays = [n for n in named if n not in reach]
    if strays:
        findings.append(("NAMES A NON-INPUT", "# Figures: names %s, which "
                         "the %s does not reach" % (", ".join(strays),
                                                    "expression" if is_expr
                                                    else "Status line")))
    if isinstance(row.figures, int) and not named and stated_here is None:
        findings.append(("NAMES NO INPUT", "# Figures: declares %d but names "
                         "no input that set it" % row.figures))

    # check 3, counting
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
        return findings, info
    info["counting"] = supported

    if row.figures == "exact":
        if supported is not EXACT:
            status = (row.status or "").strip()
            if (is_expr and status.startswith("declared")
                    and not status.startswith("declared pending")):
                if not named:
                    findings.append(("NAMES NO INPUT", "a declared "
                                     "construction names no row its rule "
                                     "is over"))
                else:
                    info["construction"] = True
            else:
                findings.append(("OVER-DECLARED", "declares exact, but its "
                                 "inputs support %d figures; only a row "
                                 "whose status begins 'declared' may be "
                                 "exact over measured inputs" % supported))
        return findings, info

    # checks 5 and 6: the ceiling
    if is_expr:
        try:
            check = chain.value(row.name)
            if not math.isclose(check, float(value), rel_tol=1e-12,
                                abs_tol=0.0):
                raise Stop("CANNOT JUDGE", "the chain evaluator gives %r "
                           "and the store holds %r" % (check, value))
            sigma, stated_any, _effects = chain.propagate(row.name)
        except (Stop, ValueError, ZeroDivisionError, OverflowError) as exc:
            detail = exc.detail if isinstance(exc, Stop) else str(exc)
            findings.append(("CANNOT JUDGE", detail))
            return findings, info
        info["sigma"] = sigma
        if stated_any and sigma > 0:
            ceiling = figures_at_place(value, reported_place(sigma))
            info["ceiling_u"] = ceiling
            if row.figures > ceiling:
                findings.append(("OVER-DECLARED", "declares %d figures; "
                                 "counting allows %s, and the propagated "
                                 "uncertainty %.3g allows %d"
                                 % (row.figures, supported, sigma,
                                    ceiling)))
            elif (supported is not EXACT and row.figures > supported
                  and stated_here is None):
                findings.append(("NO UNCERTAINTY FORM", "declares %d "
                                 "figures, more than counting's %d, with "
                                 "no 'uncertainty <number>' field on its "
                                 "own line to say why"
                                 % (row.figures, supported)))
            if stated_here is not None:
                number, literal = stated_here
                place = literal_place(literal)
                recomputed = round(sigma, -place)
                if not math.isclose(recomputed, number, rel_tol=1e-9,
                                    abs_tol=0.0):
                    findings.append(("UNCERTAINTY DISAGREES", "states "
                                     "uncertainty %s; recomputed from full "
                                     "digits by central difference it is "
                                     "%.4g, which reads %g at the digits "
                                     "stated" % (literal, sigma,
                                                 recomputed)))
        else:
            if supported is not EXACT and row.figures > supported:
                findings.append(("OVER-DECLARED", "declares %d figures; its "
                                 "inputs support %d" % (row.figures,
                                                        supported)))
            if stated_here is not None:
                findings.append(("UNCERTAINTY UNSUPPORTED", "writes "
                                 "uncertainty %s, but no measured primary "
                                 "in its chain states one, so counting sets "
                                 "its count" % stated_here[1]))
    elif supported is not EXACT and row.figures > supported:
        findings.append(("OVER-DECLARED", "declares %d figures; its inputs "
                         "support %d" % (row.figures, supported)))

    # check 4
    if (is_expr and isinstance(row.figures, int)
            and row.derived_text is not None):
        problem = check_comment(row, value, row.figures)
        if problem:
            findings.append(problem)
    return findings, info


def ok_detail(row, kind, info):
    """The words on an OK line: the count and both ceilings."""
    if info.get("construction"):
        return "exact -- a declared construction over its named rows"
    if row.figures == "exact":
        return "exact"
    if kind == "typed":
        return "%s figures; a typed number, check 1 only" % row.figures
    counting = info.get("counting")
    ceiling_u = info.get("ceiling_u")
    if ceiling_u is None:
        return "%s figures, within what its inputs support" % row.figures
    return ("%s figures; counting allows %s, propagation allows %d "
            "(uncertainty %.3g)" % (row.figures,
                                     "any" if counting is EXACT else counting,
                                     ceiling_u, info["sigma"]))


def judge(rows, by_name, values, closed, transitional):
    """[(verdict, name, detail, fails, kind)] for every row it reads.

    kind is "expression", "transitional" or "typed" for a derived row,
    and "primary" for a primary named by check 6.
    """
    results = []
    reached = []
    for row in rows:
        is_trans = row.name in transitional
        if not (row.kind == "expression" or is_trans
                or row.derived_text is not None):
            continue
        kind = ("transitional" if is_trans else
                "expression" if row.kind == "expression" else "typed")
        findings, info = judge_row(row, by_name, values, transitional)
        if row.kind == "expression":
            for name in Chain(by_name, values).primaries(row.name):
                if name not in reached:
                    reached.append(name)
        if not findings:
            results.append(("OK", row.name, ok_detail(row, kind, info),
                            False, "construction"
                            if info.get("construction") else kind))
            continue
        closed_row = constants_rows.in_closed_slice(row.name, closed)
        for verdict, detail in findings:
            fails = verdict in FAILING or (verdict in GAPS and closed_row)
            results.append((verdict, row.name, detail, fails, kind))
    for name in reached:
        if prose_only(by_name[name]):
            fails = constants_rows.in_closed_slice(name, closed)
            results.append(("UNCERTAINTY IN PROSE", name, "its # Figures: "
                            "line speaks of an uncertainty in words and has "
                            "no 'uncertainty <number>' field, so no ceiling "
                            "can read it", fails, "primary"))
    return results


# ------------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------------

FIXTURE_STORE = '''
import numpy as np
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
FIX_S_A1 = 10.22
# Figures: 4 -- prints 10.22, uncertainty 0.10
FIX_S_A2 = 1.29
# Figures: 3 -- prints 1.29, uncertainty 0.06
FIX_S_A3 = 0.184
# Figures: 3 -- prints 0.184, uncertainty 0.007
FIX_S_A4 = 8.14
# Figures: 3 -- prints 8.14, uncertainty 0.39
FIX_S_A5 = 6.6
# Figures: 2 -- prints 6.6, uncertainty 0.5
FIX_S_P = 2.0
# Status: declared 2026-09-22 -- a drawing condition
# Figures: exact -- a declared condition
FIX_S_BZ = 0.0
# Status: declared 2026-09-22 -- a drawing condition
# Figures: exact -- a declared condition
FIX_S_R = 6378.1366
# Figures: 8 -- uncertainty 0.0001
FIX_S_R0 = 15.02
# Figures: 4 -- prints 15.02
FIX_S_EPS = 6.55
# Figures: 3 -- prints 6.55
FIX_SHUE_OK = (FIX_S_A1 + FIX_S_A2 * np.tanh(FIX_S_A3 * (FIX_S_BZ + FIX_S_A4))) * FIX_S_P ** (-1.0 / FIX_S_A5)
# Figures: 3 -- uncertainty 0.13, root-sum-square of FIX_S_A1 to FIX_S_A5
# Derived: = 10.3
FIX_SHUE_OVER = (FIX_S_A1 + FIX_S_A2 * np.tanh(FIX_S_A3 * (FIX_S_BZ + FIX_S_A4))) * FIX_S_P ** (-1.0 / FIX_S_A5)
# Figures: 4 -- uncertainty 0.13, root-sum-square of FIX_S_A1 to FIX_S_A5
# Derived: = 10.25
FIX_SHUE_ONESIDED = (FIX_S_A1 + FIX_S_A2 * np.tanh(FIX_S_A3 * (FIX_S_BZ + FIX_S_A4))) * FIX_S_P ** (-1.0 / FIX_S_A5)
# Figures: 3 -- uncertainty 0.14, every coefficient moved down only
# Derived: = 10.3
FIX_SHUE_NOFORM = (FIX_S_A1 + FIX_S_A2 * np.tanh(FIX_S_A3 * (FIX_S_BZ + FIX_S_A4))) * FIX_S_P ** (-1.0 / FIX_S_A5)
# Figures: 3 -- set by FIX_S_A1
# Derived: = 10.3
FIX_SHUE_KM = FIX_SHUE_OK * FIX_S_R
# Figures: 2 -- uncertainty 850, carried through FIX_SHUE_OK
# Derived: = 65,000
FIX_SHUE_KM_ROUNDED = FIX_SHUE_OK * FIX_S_R
# Figures: 2 -- uncertainty 840, converted from the rounded 0.132
# Derived: = 65,000
FIX_BS_UNSUPPORTED = FIX_S_R0 * FIX_S_P ** (-1.0 / FIX_S_EPS)
# Figures: 3 -- uncertainty 0.005, set by FIX_S_EPS
# Derived: = 13.5
FIX_LEO_OK = (FIX_S_R + FIX_ALT_KM) / FIX_S_R
# Figures: 8 -- set by FIX_S_R
# Derived: = 1.0313571
FIX_LEO_OVER = (FIX_S_R + FIX_ALT_KM) / FIX_S_R
# Figures: 11 -- set by FIX_S_R
# Derived: = 1.0313571
FIX_LEO_NOFORM = (FIX_S_R + FIX_ALT_KM) / FIX_S_R
# Figures: 9 -- set by FIX_S_R
# Derived: = 1.0313571
FIX_PROSE_R = 6378.1366
# Figures: 8 -- the source gives it to +/- 0.1 m
FIX_PROSE_USE = FIX_PROSE_R * 2
# Figures: 8 -- set by FIX_PROSE_R
# Derived: = 12756.273
FIX_BAND_LO = 4.0
# Figures: 1 -- prints 4
FIX_BAND_HI = 5.0
# Figures: 1 -- prints 5
FIX_MID = (FIX_BAND_LO + FIX_BAND_HI) / 2.0
# Status: declared 2026-09-22 -- the midpoint of the band
# Figures: exact -- declared construction: midpoint of FIX_BAND_LO, FIX_BAND_HI
# Derived: = 4.5
FIX_MID_MEASURED = (FIX_BAND_LO + FIX_BAND_HI) / 2.0
# Status: measured V_SOURCED 2026-09-22
# Figures: exact -- declared construction: midpoint of FIX_BAND_LO, FIX_BAND_HI
# Derived: = 4.5
FIX_MID_PENDING = (FIX_BAND_LO + FIX_BAND_HI) / 2.0
# Status: declared pending 2026-09-22 -- L-1
# Figures: exact -- declared construction: midpoint of FIX_BAND_LO, FIX_BAND_HI
# Derived: = 4.5
FIX_MID_NONAME = (FIX_BAND_LO + FIX_BAND_HI) / 2.0
# Status: declared 2026-09-22 -- the midpoint of the band
# Figures: exact -- a declared construction
# Derived: = 4.5
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
    # L-322 Stage C2: the uncertainty route and the declared construction
    "FIX_SHUE_OK": ["OK"],
    "FIX_SHUE_OVER": ["OVER-DECLARED"],
    "FIX_SHUE_ONESIDED": ["UNCERTAINTY DISAGREES"],
    "FIX_SHUE_NOFORM": ["NO UNCERTAINTY FORM"],
    "FIX_SHUE_KM": ["OK"],
    "FIX_SHUE_KM_ROUNDED": ["UNCERTAINTY DISAGREES"],
    "FIX_BS_UNSUPPORTED": ["UNCERTAINTY UNSUPPORTED"],
    "FIX_LEO_OK": ["OK"],
    "FIX_LEO_OVER": ["OVER-DECLARED"],
    "FIX_LEO_NOFORM": ["NO UNCERTAINTY FORM"],
    "FIX_PROSE_USE": ["OK"],
    "FIX_PROSE_R": ["UNCERTAINTY IN PROSE"],
    "FIX_MID": ["OK"],
    "FIX_MID_MEASURED": ["OVER-DECLARED"],
    "FIX_MID_PENDING": ["OVER-DECLARED"],
    "FIX_MID_NONAME": ["NAMES NO INPUT"],
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
    if any(f for _v, _d, f in got.get("FIX_PROSE_R", [])):
        problems.append("FIX_PROSE_R: unread prose failed outside a closed "
                        "slice")
    if not any(fails for v, name, _d, fails, _k in closed
               if name == "FIX_PROSE_R"):
        problems.append("FIX_PROSE_R: unread prose did not fail inside a "
                        "closed slice")
    constructions = [name for _v, name, _d, _f, kind in results
                     if kind == "construction"]
    if constructions != ["FIX_MID"]:
        problems.append("declared constructions listed as %r, expected "
                        "['FIX_MID']" % constructions)
    for name, words in (("FIX_SHUE_OK", "propagation allows 3"),
                        ("FIX_LEO_OK", "propagation allows 10")):
        details = [d for _v, d, _f in got.get(name, [])]
        if not any(words in d for d in details):
            problems.append("%s: its line does not say %r (%s)"
                            % (name, words, details))
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
              "including a gap failing inside a closed slice, a row passing "
              "only by the uncertainty route and a declared construction."
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
        if kind == "primary":
            continue
        if kind == "construction":
            kind = "expression"
        if name not in names:
            names.append(name)
            kinds[kind] = kinds.get(kind, 0) + 1
    constructions = [name for _v, name, _d, _f, kind in results
                     if kind == "construction"]
    by_route = [name for v, name, d, _f, _k in results
                if v == "OK" and "propagation allows" in d]
    prose = [name for v, name, _d, _f, _k in results
             if v == "UNCERTAINTY IN PROSE"]

    print("Rows read: %d -- %d expression(s), %d transitional, %d typed "
          "number(s) with a # Derived: note."
          % (len(names), kinds.get("expression", 0),
             kinds.get("transitional", 0), kinds.get("typed", 0)))
    print("Ceiling by propagation, because a primary in the chain states an "
          "uncertainty: %d row(s). Every other judged row is ceilinged by "
          "counting." % len(by_route))
    print("Declared constructions, exact by their stated rule (%d):"
          % len(constructions))
    for line in constants_rows.wrap_names(constructions or ["(none)"]):
        print(line)
    print("Primaries whose uncertainty is in words only (%d)%s"
          % (len(prose), ":" if prose else "."))
    for line in constants_rows.wrap_names(prose):
        print(line)
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
