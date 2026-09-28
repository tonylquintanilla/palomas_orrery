"""
constants_rows.py -- read constants_new.py as rows: each top-level
assignment, its right-hand side, and the comment fields beneath it.

WHY THIS EXISTS

    Three tools need the same reading of the store: export_constants.py,
    test_constants_export.py and test_dimensions.py, plus the rewritten
    test_derived_figures.py. Each used to carry its own parser, and two
    parsers can disagree about which comment belongs to which value.
    This is the one reader they share.

    It reads with Python's own parser (ast), not with line regexes, so a
    dict or a parenthesised expression spread over several lines ends
    where Python says it ends, and the comment block is the run of
    comment lines directly below THAT line.

WHAT A ROW CARRIES

    name, line, end_line   where the assignment is
    rhs                    the right-hand side as written
    kind                   "literal"    a number, possibly signed
                           "expression" arithmetic that uses other rows
                           "container"  a dict, list, tuple or set
                           "other"      anything else (a datetime, a string)
    inputs                 the store rows an expression uses, once each
    embedded               numbers typed inside an expression, as written
    unit, unit_error       the token on the "# Unit:" line
    figures, figures_error the count on the "# Figures:" line: an int,
                           "exact", or None when there is no line
    status                 the "# Status:" line joined with "# Status+:"
                           lines, the same join test_status_lines.py makes
    derived_text           the "# Derived:" block, or None
    read_text              the "# Read:" lines, a list, one entry per
                           read with its "# Read+:" lines joined to it
    uncertainty            the stated uncertainty on the "# Figures:" line,
                           as the literal written there ("10", "0.13"),
                           or None. The field form is the word
                           "uncertainty" followed directly by the number,
                           in the row's own unit (provenance-discipline
                           Rule 1); prose around it is never read
    prints                 the print count of an exact row a display
                           prints, an int, or None. Read ONLY in the field
                           form directly after "exact --", as
                           "exact -- prints 3", because measured rows'
                           "# Figures:" lines say "the source prints 1.5"
                           in prose (provenance-discipline 2.20, Rule 7)

    A row is DERIVED when its right-hand side is an expression, or when
    it is on the TRANSITIONAL list below. A row that only carries a
    "# Derived:" note beside a typed number is not derived; it is a
    literal whose arithmetic lives in prose. The checkers name both.

THE TWO SHARED LISTS

    CLOSED_SLICES   slices whose walk is finished. Inside one, a row with
                    no unit, no status or no figure count FAILS; outside,
                    it is named as not yet migrated. ("EARTH",) since
                    L-322 Stage C2, 2026-09-22; empty before. Tony's
                    per-slice gate, 2026-09-14. One home, here, so the
                    three checkers that apply it cannot disagree.

    TRANSITIONAL    EMPTY since L-322 Stage C2 (2026-09-22). It held the
                    two magnetosphere standoffs, which were stored as
                    rounded literals under the ruling of 2026-09-12
                    (L-325) that Tony withdrew on 2026-09-16. Their
                    arithmetic lived only in their "# Derived:" lines
                    until the Earth slice visit made them expressions
                    again. The list and the code that reads it stay, so a
                    later literal awaiting its visit has somewhere to go
                    and the checkers still say what it is.

    A row's slice is its name up to the first underscore: EARTH for
    every Earth row. That rule is enough for the Earth slice. It is not
    enough for the Sun, whose rows are named SUN_, SOLAR_, CORE_,
    RADIATIVE_, CHROMOSPHERE_ and others; the Sun slice will need an
    explicit list here.

Role: utility
Domain: dev_tools

Module created: September 16, 2026 with Anthropic's Claude Opus 5
(L-322, the mechanism: the shared reader the build manifest names).
Module updated: September 22, 2026 with Anthropic's Claude Opus 5
(L-322 Stage C2: Earth is a closed slice, TRANSITIONAL is empty,
figures_of() lets a display format a row by the count the row declares,
and a "# Read:" line's "+" continuations join it, so the export's read
list holds one entry per read.)
Module updated: September 25, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D8: the uncertainty field on a "# Figures:" line
is read here, once, as Row.uncertainty; UNCERTAINTY_FIELD_RE is the one
pattern for it, which test_derived_figures.py now imports instead of
keeping its own; and uncertainty_of() lets a display print a row's
stated uncertainty beside its value, as Earth's magnetotail hover does.)
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D15: an exact row's print count is read here as
Row.prints; print_count_problem() is the one check of it, which the
export runs on every row; prints_of() and exact_text() let an orrery
display print an exact row by its count instead of by a width chosen on
its own line. provenance-discipline 2.20, Rule 7.)
Module updated: September 28, 2026 with Anthropic's Claude Opus 5.5
(L-345, patch L322_D_19: conversions() computes a row's value in every
unit of its dimension from the row's full digits, with the count its
source row alone gives -- provenance-discipline 2.22, Rule 3. A value
in another unit is computed, never stored; the export serves these as
"in", and it is the one implementation of the rule.)
"""

import ast
import hashlib
import math
import os
import re

STORE = "constants_new.py"

CLOSED_SLICES = ("EARTH",)

TRANSITIONAL = ()

TOKEN_RE = re.compile(r"^[a-z][a-z0-9_]*$")
KEY_RE = re.compile(r"^#\s*([A-Z][A-Za-z-]*)(\+?):\s?(.*)$")
NAME_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9_]*\b")
# The field form of a stated uncertainty (provenance-discipline 2.16,
# Rule 1): the word, then the number, in the row's own unit. One pattern
# for every reader: the figures checker, the export and the displays.
UNCERTAINTY_FIELD_RE = re.compile(
    r"\buncertainty\s+([-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?)")
# The print count of an exact row (provenance-discipline 2.20, Rule 7):
# anchored directly after "exact --", so the prose "the source prints
# 1.5" on a measured row's line is never read as one.
PRINTS_FIELD_RE = re.compile(r"^exact\s*--\s*prints\s+(\d+)\b")


class Row(object):
    """One top-level assignment in the store and its comment fields."""

    def __init__(self, name, line, end_line, rhs, node):
        self.name = name
        self.line = line
        self.end_line = end_line
        self.rhs = rhs
        self.node = node
        self.kind = "other"
        self.inputs = []
        self.embedded = []
        self.notes = []
        self.entries = []
        self.unit = None
        self.unit_error = None
        self.figures = None
        self.figures_text = None
        self.figures_error = None
        self.uncertainty = None
        self.prints = None
        self.status = None
        self.derived_text = None
        self.read_text = []

    @property
    def slice(self):
        return slice_of(self.name)

    @property
    def transitional(self):
        return self.name in TRANSITIONAL

    @property
    def is_derived(self):
        return self.kind == "expression" or self.transitional

    def field(self, key, loose=False):
        """The text of a keyed comment, joined with its "+" lines.

        loose=True also joins comment lines that carry no key at all and
        sit under this one, which is how some older rows continue a line
        (an indented "#   ..." under a "# Derived:").
        """
        parts = []
        active = False
        for entry_key, plus, text in self.entries:
            if entry_key == key and not plus and not parts:
                parts.append(text)
                active = True
            elif active and entry_key == key and plus:
                parts.append(text)
            elif active and entry_key is None and loose:
                parts.append(text)
            elif entry_key is not None:
                active = False
        if not parts:
            return None
        return " ".join(p.strip() for p in parts if p.strip())

    def count(self, key):
        return sum(1 for k, plus, _t in self.entries if k == key and not plus)


def slice_of(name):
    return name.split("_", 1)[0]


def in_closed_slice(name, closed=None):
    closed = CLOSED_SLICES if closed is None else closed
    return slice_of(name) in closed


def store_path(project_dir):
    return os.path.join(project_dir, STORE)


def store_sha256(path):
    """sha256 of the store with CRLF normalised to LF.

    A Windows working copy can hold CRLF where the repository holds LF,
    with not one character different. Hashing raw bytes would call that
    a change (safe-file-editing, Compare Content, Not Bytes).
    """
    with open(path, "rb") as handle:
        data = handle.read()
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def read_text(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def _is_number(node):
    if isinstance(node, ast.Constant):
        return (isinstance(node.value, (int, float))
                and not isinstance(node.value, bool))
    if isinstance(node, ast.UnaryOp) and isinstance(
            node.op, (ast.USub, ast.UAdd)):
        return _is_number(node.operand)
    return False


def _parse_entries(notes):
    entries = []
    for line in notes:
        match = KEY_RE.match(line)
        if match:
            entries.append((match.group(1), match.group(2) == "+",
                            match.group(3)))
        else:
            entries.append((None, False, line.lstrip("#").strip()))
    return entries


def _fill_fields(row):
    row.entries = _parse_entries(row.notes)

    if row.count("Unit") > 1:
        row.unit_error = "more than one '# Unit:' line"
    unit_text = row.field("Unit")
    if unit_text is not None:
        token = unit_text.split(" -- ")[0].strip()
        if TOKEN_RE.match(token):
            row.unit = token
        else:
            row.unit_error = ("'# Unit: %s' is not one lowercase token"
                              % unit_text.strip())

    if row.count("Figures") > 1:
        row.figures_error = "more than one '# Figures:' line"
    fig_text = row.field("Figures")
    if fig_text is not None:
        row.figures_text = fig_text.strip()
        head = fig_text.split("--")[0].strip()
        if head == "exact":
            row.figures = "exact"
        elif head.isdigit() and int(head) > 0:
            row.figures = int(head)
        else:
            row.figures_error = ("'# Figures: %s' is neither a positive "
                                 "whole number nor 'exact'" % head)
        match = UNCERTAINTY_FIELD_RE.search(row.figures_text)
        if match:
            row.uncertainty = match.group(1)
        if row.figures == "exact":
            match = PRINTS_FIELD_RE.match(row.figures_text)
            if match:
                row.prints = int(match.group(1))
                if row.prints < 1:
                    row.figures_error = ("'prints %s': a print count is at "
                                         "least 1" % match.group(1))

    row.status = row.field("Status")
    row.derived_text = row.field("Derived", loose=True)
    reads = []
    for key, plus, text in row.entries:
        if key == "Read" and not plus:
            reads.append(text.strip())
        elif key == "Read" and plus and reads:
            reads[-1] = (reads[-1] + " " + text.strip()).strip()
    row.read_text = reads


def parse_store_text(text):
    """Every top-level assignment in `text`, in file order.

    Returns (rows, by_name). Raises SyntaxError if the text is not
    Python, which every caller reports as a failure.
    """
    tree = ast.parse(text)
    lines = text.split("\n")
    rows = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            targets = [node.target]
        else:
            continue
        end = getattr(node, "end_lineno", node.lineno)
        rhs = ast.get_source_segment(text, node.value) or ""
        notes = []
        index = end
        while index < len(lines) and lines[index].startswith("#"):
            notes.append(lines[index])
            index += 1
        for target in targets:
            if isinstance(target, ast.Name):
                row = Row(target.id, node.lineno, end, rhs, node.value)
                row.notes = notes
                rows.append(row)

    names = set(row.name for row in rows)
    for row in rows:
        value = row.node
        if _is_number(value):
            row.kind = "literal"
        elif isinstance(value, (ast.Dict, ast.List, ast.Tuple, ast.Set)):
            row.kind = "container"
        else:
            used = []
            embedded = []
            for sub in ast.walk(value):
                if isinstance(sub, ast.Name) and sub.id in names:
                    if sub.id not in used:
                        used.append(sub.id)
                elif (isinstance(sub, ast.Constant)
                      and isinstance(sub.value, (int, float))
                      and not isinstance(sub.value, bool)):
                    embedded.append(
                        ast.get_source_segment(text, sub) or repr(sub.value))
            if used:
                row.kind = "expression"
                row.inputs = used
                row.embedded = embedded
        _fill_fields(row)

    by_name = dict((row.name, row) for row in rows)
    return rows, by_name


def read_store(project_dir):
    """(text, rows, by_name) for constants_new.py beside `project_dir`."""
    text = read_text(store_path(project_dir))
    rows, by_name = parse_store_text(text)
    return text, rows, by_name


def load_values(project_dir):
    """The store's values, by executing it the way an import would.

    A fresh namespace every call, so a checker never reads a module some
    other code already imported and perhaps changed.
    """
    path = store_path(project_dir)
    namespace = {"__name__": "constants_new_snapshot", "__file__": path}
    exec(compile(read_text(path), path, "exec"), namespace)
    return namespace


_FIGURES_BY_DIR = {}


def figures_of(name, project_dir=None):
    """The figure count row `name` declares: an int, "exact", or None.

    For a display that has only the Python float and must print it at
    the count its row declares (provenance-discipline 2.17, Rule 7). The
    caller formats, with Rule 5's "%.*g" or an f-string's ".{n}g".

    Reads constants_new.py beside this file once per process and keeps
    the table. A name that is not a row raises KeyError, so a display
    that names the wrong row fails where it is built instead of quietly
    printing some other row's count.

    This is the smallest thing L-322 Stage C2's four standoff sites need.
    A general way for every orrery display to format by the declared
    count is the follow-on recorded on L-322, not designed here.
    """
    project_dir = project_dir or os.path.dirname(os.path.abspath(__file__))
    table = _FIGURES_BY_DIR.get(project_dir)
    if table is None:
        _text, _rows, by_name = read_store(project_dir)
        table = dict((row_name, row.figures)
                     for row_name, row in by_name.items())
        _FIGURES_BY_DIR[project_dir] = table
    return table[name]


_UNCERTAINTY_BY_DIR = {}


def uncertainty_of(name, project_dir=None):
    """The uncertainty row `name` states, as (number, literal), or None.

    For a display that prints a value with its stated uncertainty beside
    it, such as "120 Earth radii, plus or minus 10". The literal is what
    the row writes, so the display prints the uncertainty with the digits
    the source gave it. A name that is not a row raises KeyError, as in
    figures_of(). L-322 Stage D, patch D8.
    """
    project_dir = project_dir or os.path.dirname(os.path.abspath(__file__))
    table = _UNCERTAINTY_BY_DIR.get(project_dir)
    if table is None:
        _text, _rows, by_name = read_store(project_dir)
        table = dict((row_name, row.uncertainty)
                     for row_name, row in by_name.items())
        _UNCERTAINTY_BY_DIR[project_dir] = table
    literal = table[name]
    if literal is None:
        return None
    return abs(float(literal)), literal


_PRINTS_BY_DIR = {}


def prints_of(name, project_dir=None):
    """The print count exact row `name` states, an int, or None.

    A name that is not a row raises KeyError, as in figures_of().
    L-322 Stage D, patch D15.
    """
    project_dir = project_dir or os.path.dirname(os.path.abspath(__file__))
    table = _PRINTS_BY_DIR.get(project_dir)
    if table is None:
        _text, _rows, by_name = read_store(project_dir)
        table = dict((row_name, row.prints)
                     for row_name, row in by_name.items())
        _PRINTS_BY_DIR[project_dir] = table
    return table[name]


def _written_digits(text):
    """How many digits a number, as written, has from its first non-zero
    digit to its last digit, trailing zeros included: 200.0 has four,
    2.0 two, 4.5 two, 0.0 none. The ceiling a print count may not pass.
    """
    mantissa = text.strip().lstrip("+-").split("e")[0].split("E")[0]
    digits = mantissa.replace(".", "").lstrip("0")
    return len(digits)


def print_count_problem(row, value):
    """Why `row`'s print count is wrong for `value`, or None.

    Three refusals (provenance-discipline 2.20, Rule 7):
      - a count larger than the digits the number has. For a typed
        number these are the digits of the literal as written; for an
        expression, the digits of the value it computes. So 200.0 allows
        up to four, and a declared construction giving 4.5 up to two;
      - a count too small to write the number out in full, because an
        exact number printed rounded is a different number: 105 at two
        figures would print 100;
      - any count but 1 on a zero, which prints as 0.
    A row with no print count has nothing to check here; whether a
    display reaches it is exact_rows_report.py's question.
    """
    if row.prints is None:
        return None
    if (isinstance(value, bool) or not isinstance(value, (int, float))
            or value != value):
        return ("states 'prints %d', but its value is not one number"
                % row.prints)
    if value == 0:
        if row.prints != 1:
            return ("states 'prints %d', but a zero prints as 0, so its "
                    "print count is 1" % row.prints)
        return None
    if row.kind == "literal":
        written = row.rhs
    else:
        written = repr(float(value))
    ceiling = _written_digits(written)
    if row.prints > ceiling:
        return ("states 'prints %d', but %s has only %d digit(s) to print"
                % (row.prints, written.strip(), ceiling))
    if float("%.*g" % (row.prints, value)) != float(value):
        return ("states 'prints %d', which would print %r as %s: an exact "
                "number prints in full" % (row.prints, value,
                                           format_prints(value, row.prints)))
    return None


def format_prints(value, prints, grouping=False):
    """`value` at `prints` significant figures, in plain digits.

    The same result as the gallery's sigFigures(): 4.5 at two figures is
    "4.5", 2.0 at one is "2", 120.0 at three is "120", 0.0 at one is "0".
    grouping=True adds a thousands separator, "2,000".
    """
    rounded = float("%.*g" % (prints, value))
    if rounded == 0:
        decimals = prints - 1
    else:
        decimals = prints - 1 - int(math.floor(math.log10(abs(rounded))))
    decimals = max(0, min(20, decimals))
    if grouping:
        return "{:,.{d}f}".format(rounded, d=decimals)
    return "{:.{d}f}".format(rounded, d=decimals)


def exact_text(name, grouping=False):
    """Exact row `name` as text, at the print count its row states.

    For an orrery display (provenance-discipline 2.20, Rule 7). The value
    and the count are read by the same name, so they cannot come from
    different rows. A row that states no print count raises ValueError
    where the display is built, instead of a width being chosen for it.
    L-322 Stage D, patch D15.
    """
    import constants_new
    prints = prints_of(name)
    if prints is None:
        raise ValueError("%s states no print count; add 'prints N' after "
                         "'exact --' on its # Figures: line" % name)
    return format_prints(getattr(constants_new, name), prints, grouping)


def names_in(text, known):
    """Store names mentioned in a piece of prose, in order, once each."""
    found = []
    for word in NAME_RE.findall(text or ""):
        if word in known and word not in found:
            found.append(word)
    return found


def wrap_names(names, width=66, indent="      "):
    """A list of names as indented lines no wider than `width`."""
    lines = []
    current = ""
    for name in names:
        piece = name if not current else current + ", " + name
        if len(indent + piece) > width and current:
            lines.append(indent + current + ",")
            current = name
        else:
            current = piece
    if current:
        lines.append(indent + current)
    return lines


# ---------------------------------------------------------------------
# A value in another unit is computed, never stored
# (provenance-discipline 2.22, Rule 3; L-345, Tony's ruling 2026-09-28)
# ---------------------------------------------------------------------

def place_nearest(scaled):
    """The power of ten nearest `scaled` on a log scale, as an exponent,
    a tie going to the coarser: 0.0014 gives -3, 0.0067 gives -2,
    4.26e-6 gives -5. `scaled` is a PLACE UNIT carried through an exact
    factor: a unit in the source's last declared place, or twice a
    stated uncertainty, so that comparing it with powers of ten is the
    Report test's comparison of an uncertainty with half a unit in each
    candidate place.
    """
    return int(math.floor(math.log10(scaled) + 0.5))


def _to_place(value, place):
    """`value` rounded half to even at 10**place (Rule 5), and the count
    of significant figures that leaves. A rounding that carries into a
    new leading digit (9.996 to 10.00) keeps the place and gains the
    figure. Never fewer than one figure: where the place is coarser than
    the value's leading digit -- a one-figure 100 Earth radii is +/- 50,
    as large as 0.002 AU on a value of 0.004 -- the value keeps its one
    leading figure rather than rounding to nothing.
    """
    figures = int(math.floor(math.log10(abs(value)))) - place + 1
    if figures < 1:
        figures = 1
        return float("%.*g" % (1, value)), 1
    rounded = float("%.*g" % (figures, value))
    if int(math.floor(math.log10(abs(rounded)))) - place + 1 != figures:
        figures += 1
        rounded = float("%.*g" % (figures, value))
    return rounded, figures


def conversion_units(unit, tokens):
    """The tokens a row in `unit` converts into, as {token: the name of
    its defining constant, or None for the base}: the dimension's base
    token (km for a length) and every token defined as a multiple of it.
    None when there is nothing to convert to.
    """
    spec = tokens.get(unit)
    if spec is None:
        return None
    dimension = spec.get("dimension")
    # A token belongs to a conversion group when it IS its dimension's
    # base (km for a length) or is defined as a multiple of it (au,
    # r_earth, r_sun). Tokens that merely share a dimension -- the
    # dimensionless fit coefficients, each its own kind of number -- are
    # not conversions of one another.
    group = dict((token, other.get("defining_constant"))
                 for token, other in tokens.items()
                 if other.get("dimension") == dimension
                 and (token == dimension
                      or other.get("defining_constant") is not None))
    if unit not in group or len(group) < 2:
        return None
    return group


def conversions(row, value, values, units_by_name, tokens):
    """Row `row`'s value in every unit of its dimension, computed.

    Returns (entries, problem). `entries` is None when the row has no
    unit to convert into or is not one number; otherwise
    {token: {"value": v, "figures": f, "prints": p}} with the row's own
    unit among them, carrying the row's own value and counts unchanged.

    THE COUNT COMES FROM THE SOURCE ROW ALONE (provenance-discipline
    2.22, Rule 3). The source's uncertainty, scaled by the exact factor,
    sets the place each unit prints to:
      - a stated uncertainty (the \"uncertainty\" field): the Report
        test, the place whose implied half unit is nearest it on a log
        scale;
      - otherwise the source's last declared place, carried through the
        factor to the nearest power of ten -- the same measure;
      - an exact source: its conversions are exact, unrounded, and a
        print count is found by the same place rule from the last place
        of its own print count; with no print count, none.
    The row that defines a token, in that token, is 1 by definition:
    exact, printing 1.
    A row with no figure count converts unrounded, with none.
    The value is always the source's FULL digits times the exact factor,
    rounded once (Rule 4).
    """
    group = conversion_units(row.unit, tokens)
    if group is None:
        return None, None
    if (isinstance(value, bool) or not isinstance(value, (int, float))
            or value != value):
        return None, None
    bases = [token for token, defining in group.items() if defining is None]
    if len(bases) != 1:
        return None, ("dimension of '%s' has %d base token(s), needs "
                      "exactly one to convert through" % (row.unit,
                                                          len(bases)))
    base = bases[0]
    size = {}
    for token, defining in group.items():
        if defining is None:
            size[token] = 1.0
            continue
        if units_by_name.get(defining) != base:
            return None, ("token '%s' is defined by %s, whose unit is %r, "
                          "not the base '%s'" % (token, defining,
                                                 units_by_name.get(defining),
                                                 base))
        size[token] = float(values[defining])
    in_base = float(value) * size[row.unit]

    own_prints = row.prints
    entries = {}
    for token in sorted(group):
        if token == row.unit:
            if isinstance(row.figures, int):
                shown = float("%.*g" % (row.figures, value))
            else:
                shown = float(value)
            entries[token] = {"value": shown, "figures": row.figures,
                              "prints": own_prints}
            continue
        if group[token] == row.name:
            # The row that DEFINES this token, in that token: one, by
            # definition, whatever the row's own precision -- as the
            # crust reads "1 Earth radius" (Tony, 2026-09-27).
            entries[token] = {"value": 1.0, "figures": "exact",
                              "prints": 1}
            continue
        full = in_base / size[token]
        factor = size[row.unit] / size[token]
        if row.figures is None or value == 0:
            entries[token] = {"value": full, "figures": row.figures,
                              "prints": None}
            continue
        if row.figures == "exact":
            prints = None
            if own_prints is not None:
                own_place = (int(math.floor(math.log10(abs(value))))
                             - own_prints + 1)
                place = place_nearest((10.0 ** own_place) * factor)
                prints = max(1, int(math.floor(math.log10(abs(full))))
                             - place + 1)
            entries[token] = {"value": full, "figures": "exact",
                              "prints": prints}
            continue
        if row.uncertainty is not None:
            unit_width = 2.0 * abs(float(row.uncertainty))
        else:
            shown = float("%.*g" % (row.figures, value))
            unit_width = 10.0 ** (int(math.floor(math.log10(abs(shown))))
                                  - row.figures + 1)
        place = place_nearest(unit_width * factor)
        rounded, figures = _to_place(full, place)
        entries[token] = {"value": rounded, "figures": figures,
                          "prints": None}
    return entries, None
