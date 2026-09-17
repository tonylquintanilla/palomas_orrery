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
    read_text              the "# Read:" lines, a list

    A row is DERIVED when its right-hand side is an expression, or when
    it is on the TRANSITIONAL list below. A row that only carries a
    "# Derived:" note beside a typed number is not derived; it is a
    literal whose arithmetic lives in prose. The checkers name both.

THE TWO SHARED LISTS

    CLOSED_SLICES   slices whose walk is finished. Inside one, a row with
                    no unit, no status or no figure count FAILS; outside,
                    it is named as not yet migrated. Empty until the
                    Earth walk finishes, then ("EARTH",). Tony's
                    per-slice gate, 2026-09-14. One home, here, so the
                    three checkers that apply it cannot disagree.

    TRANSITIONAL    the two magnetosphere standoffs. They were stored as
                    rounded literals under the ruling of 2026-09-12
                    (L-325), which Tony withdrew on 2026-09-16. They stay
                    literals until the gallery stops parsing this store
                    (the gallery session of this build), then revert to
                    expressions at their Earth-slice visit, and this list
                    empties. Their arithmetic lives only in their
                    "# Derived:" lines until then.

    A row's slice is its name up to the first underscore: EARTH for
    every Earth row. That rule is enough for the Earth slice. It is not
    enough for the Sun, whose rows are named SUN_, SOLAR_, CORE_,
    RADIATIVE_, CHROMOSPHERE_ and others; the Sun slice will need an
    explicit list here.

Role: utility
Domain: dev_tools

Module created: September 16, 2026 with Anthropic's Claude Opus 5
(L-322, the mechanism: the shared reader the build manifest names).
"""

import ast
import hashlib
import os
import re

STORE = "constants_new.py"

CLOSED_SLICES = ()

TRANSITIONAL = (
    "EARTH_MAGNETOPAUSE_STANDOFF_RADII",
    "EARTH_BOW_SHOCK_STANDOFF_RADII",
)

TOKEN_RE = re.compile(r"^[a-z][a-z0-9_]*$")
KEY_RE = re.compile(r"^#\s*([A-Z][A-Za-z-]*)(\+?):\s?(.*)$")
NAME_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9_]*\b")


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

    row.status = row.field("Status")
    row.derived_text = row.field("Derived", loose=True)
    row.read_text = [t for k, plus, t in row.entries if k == "Read"]


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
