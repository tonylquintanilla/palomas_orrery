"""
test_status_lines.py - enforce the Status Line grammar in constants_new.py.

A status line is one comment line below a constant that declares what
kind of number it is and how well it is known:

    # Status: <kind> <rung> <ISO date> [-- <pointer>]

This checker enforces the grammar on every row that CARRIES one. It does
not require a row to carry one -- coverage is reported, not gated, and
the walk that writes the missing lines is L-322's, paired with the
"# Unit:" walk over the same file.

Why this is a checker and not a change to provenance_scanner.py:
    The scanner SCORES a constant, and it scores by inference -- it
    looks at a 45-line window around the assignment and asks whether
    anything in it resembles a citation. Changing that is L-322's, with
    the one walk. Enforcing the GRAMMAR is a separate, standalone job
    that needs no scanner surgery, and it is what makes a declared row
    a decision somebody made rather than a silence.

What FAILS the run:
    1. A kind that is not measured / declared / declared pending /
       derived.
    2. A measured row with no rung. The rung is what "measured" claims.
    3. A rung on a declared or derived row. Rungs apply to measured
       values only.
    4. V_SOURCED or V_CROSS_CHECKED with no "# Source:" on that row.
       The rung asserts a citation; this is where the citation has to
       be. That is the mirror of rule 5 and it is the one that would
       otherwise let a row declare itself sourced with nothing behind
       it -- cite-to-clear moved up one layer.
    5. V_RECALLED with a "# Source:" on that row. V_RECALLED means no
       citation, so the row is mislabelled one way or the other.
    6. A "declared pending" row with no ledger handle. Pending is
       backlog, and backlog without a handle cannot be counted.
    7. A derived row that names no inputs, or that names one which is
       not a top-level assignment in the file.
    8. A status line that cites -- a URL, a doi, or an author-year. The
       status line must not be citable; a source there becomes a second
       citation beside the first, and the two can disagree.

What is REPORTED but does not fail:
    - A status line with no ISO date. The skill's own examples omit it,
      so this is not settled enough to gate on.
    - Rows carrying no status line at all, counted.
    - The declared, pending and derived rows, NAMED. A count states a
      size; the names say what is there, and four names is a list
      somebody can act on.

A note on what is deliberately NOT checked. A "declared" row MAY carry
a "# Source:", and that is correct rather than contradictory --
INNER_CORONA_RADII is declared at 3 solar radii and cites the paper
that states the convention. The source says where the convention comes
from; it does not claim to measure the value. An earlier draft of this
checker would have failed that row.

Design (matches test_constants_provenance.py):
    - Plain assert functions, no pytest/unittest dependency
    - Text parsing, not import: the grammar lives in comments
    - main() runs all checks and prints a summary naming what it found

Module created: September 2026 with Anthropic's Claude Opus 5.
Module updated: September 12, 2026 with Anthropic's Claude Opus 5
    (L-324: a row-shape guard. A value that is not a container
    literal must fit on the assignment's own line).
Module updated: September 12, 2026 with Anthropic's Claude Opus 5
    (L-324 follow-on: --shape-only runs the guard alone so the
    maintenance dashboard can carry it as its own row, and a shape
    failure is no longer counted as a malformed status line).

Role: devtool
Domain: dev_tools
"""

import ast
import os
import re
import sys

TARGET = "constants_new.py"

KINDS = ("measured", "declared pending", "declared", "derived")
RUNGS = ("V_FETCHED", "V_CROSS_CHECKED", "V_SOURCED", "V_RECALLED")

ASSIGN_RE = re.compile(r"^([A-Z][A-Z0-9_]*)\s*=")
STATUS_RE = re.compile(r"^#\s*Status:\s*(.*)$")
STATUS_CONT_RE = re.compile(r"^#\s*Status\+:\s*(.*)$")
SOURCE_RE = re.compile(r"^#\s*Sources?\+?:\s")
ISO_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
HANDLE_RE = re.compile(r"\bL-\d{2,4}\b")
NAME_RE = re.compile(r"\b[A-Z][A-Z0-9_]{4,}\b")

# A status line that matches any of these is citing, which it must not do.
CITATION_IN_STATUS = (
    re.compile(r"https?://"),
    re.compile(r"\bdoi\s*:", re.I),
    re.compile(r"\([A-Z][A-Za-z.'-]*\s*(?:et\s+al\.?)?,?\s*(?:19|20)\d{2}[a-z]?\)"),
    re.compile(r"\b[A-Z][A-Za-z.'-]+\s+et\s+al\."),
)


class Row(object):
    """One top-level assignment and the comment block attached below it."""

    def __init__(self, name, line_no):
        self.name = name
        self.line_no = line_no
        self.attached = []
        self.status = None
        self.status_line_no = None

    @property
    def attached_text(self):
        return "\n".join(self.attached)

    @property
    def has_source(self):
        return any(SOURCE_RE.match(line) for line in self.attached)


def parse_rows(text):
    """Return every top-level assignment with its attached comment block.

    The block is the run of comment lines immediately below the
    assignment, up to the first line that is neither a comment nor part
    of a parenthesised continuation of the assignment itself.
    """
    lines = text.split("\n")
    rows = []
    i = 0
    while i < len(lines):
        match = ASSIGN_RE.match(lines[i])
        if not match:
            i += 1
            continue
        row = Row(match.group(1), i + 1)
        # Step over a parenthesised multi-line right-hand side.
        depth = lines[i].count("(") - lines[i].count(")")
        j = i + 1
        while depth > 0 and j < len(lines):
            depth += lines[j].count("(") - lines[j].count(")")
            j += 1
        while j < len(lines) and lines[j].startswith("#"):
            row.attached.append(lines[j])
            j += 1
        rows.append(row)
        i = max(j, i + 1)
    for row in rows:
        parts = []
        for offset, line in enumerate(row.attached):
            head = STATUS_RE.match(line)
            if head and not parts:
                parts.append(head.group(1).strip())
                row.status_line_no = row.line_no + offset + 1
                continue
            if parts:
                cont = STATUS_CONT_RE.match(line)
                if cont:
                    parts.append(cont.group(1).strip())
                elif STATUS_RE.match(line):
                    parts.append("DUPLICATE STATUS HEAD")
        if parts:
            row.status = " ".join(parts)
    return rows


def kind_of(status):
    for kind in KINDS:
        if status.lower().startswith(kind):
            return kind
    return None


def rung_of(status):
    for rung in RUNGS:
        if re.search(r"\b%s\b" % rung, status):
            return rung
    return None


def check_rows(rows, known_names):
    """Return (failures, softs). Each is a list of (row_name, message)."""
    failures = []
    softs = []
    for row in rows:
        if row.status is None:
            continue
        status = row.status

        kind = kind_of(status)
        if kind is None:
            failures.append((row.name,
                             "kind is not one of measured / declared / "
                             "declared pending / derived: %r" % status[:60]))
            continue

        rung = rung_of(status)
        if kind == "measured" and rung is None:
            failures.append((row.name,
                             "measured with no rung -- the rung is what "
                             "'measured' claims"))
        if kind != "measured" and rung is not None:
            failures.append((row.name,
                             "%s carries rung %s -- rungs apply to measured "
                             "values only" % (kind, rung)))

        if rung in ("V_SOURCED", "V_CROSS_CHECKED") and not row.has_source:
            failures.append((row.name,
                             "%s but no '# Source:' on the row -- the rung "
                             "asserts a citation that is not here" % rung))
        if rung == "V_RECALLED" and row.has_source:
            failures.append((row.name,
                             "V_RECALLED but the row carries a '# Source:' "
                             "-- mislabelled one way or the other"))

        if kind == "declared pending" and not HANDLE_RE.search(status):
            failures.append((row.name,
                             "declared pending with no ledger handle -- "
                             "backlog that cannot be counted"))

        if kind == "derived":
            named = [n for n in NAME_RE.findall(status) if n not in RUNGS]
            if not named:
                failures.append((row.name,
                                 "derived but names no inputs"))
            for n in named:
                if n not in known_names:
                    failures.append((row.name,
                                     "derived names input %s, which is not a "
                                     "top-level assignment in %s"
                                     % (n, TARGET)))

        for pattern in CITATION_IN_STATUS:
            hit = pattern.search(status)
            if hit:
                failures.append((row.name,
                                 "the status line cites (%r) -- sources live "
                                 "in '# Source:'" % hit.group(0)[:40]))
                break

        if not ISO_DATE_RE.search(status):
            softs.append((row.name, "no ISO date on the status line"))

    return failures, softs


def check_row_shape(text):
    """Return (failures, checked) for the shape of every top-level row.

    A value that is not a container literal must fit on the
    assignment's own line. constants_change_report.py reads values
    line by line off a git diff, so a right-hand side spread over
    several lines leaves the name with nothing readable after the
    equals sign -- which it once reported as a REMOVED constant.

    Container literals are exempt and must be. A dict or list is a
    lookup table that cannot fit on one line, and the change report
    reads its entries separately. Four rows here are exactly that:
    CENTER_BODY_RADII, KNOWN_ORBITAL_PERIODS, stellar_class_labels
    and spectral_subclass_temps. A flat one-assignment-per-line rule
    would be false about all four.

    This runs on the whole file every time rather than on a diff, so
    it also sees rows nobody touched this session. L-324.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        return ([(TARGET, 'could not be parsed (%s)' % exc)], 0)
    failures = []
    checked = 0
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
        else:
            continue
        checked += 1
        if isinstance(node.value,
                      (ast.Dict, ast.List, ast.Tuple, ast.Set)):
            continue
        if getattr(node, 'end_lineno', node.lineno) == node.lineno:
            continue
        for target in targets:
            if isinstance(target, ast.Name):
                failures.append((
                    target.id,
                    'value spans lines %d-%d; a non-container value '
                    'must fit on its own line (L-324)'
                    % (node.lineno, node.end_lineno)))
    return (failures, checked)


def report_shape_only(text):
    """The row-shape guard alone, for the maintenance dashboard.

    The dashboard prints ONE line per checker -- the last meaningful
    line of that tool's output -- so a guard reporting from inside
    another tool's summary never reaches it, even while it gates.
    A failure was visible, because it failed the row. A PASS was
    not, and a pass nobody can see is indistinguishable from a
    check that never ran.

    So this mode ends on its own verdict, and that verdict names
    how many assignments were read. L-324.
    """
    failures, checked = check_row_shape(text)
    print("=" * 70)
    print("  ROW SHAPE -- %s" % TARGET)
    print("=" * 70)
    print("")
    print("A value that is not a container literal must fit on the")
    print("assignment's own line, because constants_change_report.py")
    print("reads values line by line off a git diff. Container")
    print("literals -- a dict or a list -- are exempt: a lookup table")
    print("cannot fit on one line and the report reads its entries")
    print("separately.")
    print("")
    if failures:
        print("FAILURES (%d):" % len(failures))
        for name, message in failures:
            print("  %-44s %s" % (name, message))
        print("")
        print("%d of %d row shapes are wrong in %s."
              % (len(failures), checked, TARGET))
        return 1
    print("All %d row shapes in %s fit the assignment's own line."
          % (checked, TARGET))
    return 0


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s is not beside this script." % TARGET)
        return 1

    with open(path, "r") as handle:
        text = handle.read()

    if "--shape-only" in sys.argv[1:]:
        return report_shape_only(text)

    rows = parse_rows(text)
    known = set(row.name for row in rows)
    grammar_failures, softs = check_rows(rows, known)

    shape_failures, shape_checked = check_row_shape(text)
    failures = grammar_failures + shape_failures

    with_status = [r for r in rows if r.status is not None]
    by_kind = {}
    for row in with_status:
        by_kind.setdefault(kind_of(row.status) or "UNRECOGNISED", []).append(
            row.name)

    print("=" * 70)
    print("  STATUS LINE GRAMMAR -- %s" % TARGET)
    print("=" * 70)
    print("")
    print("Scored from a status line: %d of %d rows."
          % (len(with_status), len(rows)))
    print("  The denominator counts every top-level ALL-CAPS assignment,")
    print("  including dicts and label tables. The unit design record's 88")
    print("  counts numeric constants only; these are different axes.")
    for kind in ("measured", "declared", "declared pending", "derived",
                 "UNRECOGNISED"):
        names = by_kind.get(kind)
        if not names:
            continue
        if kind == "measured":
            print("  measured (%d)" % len(names))
        else:
            print("  %s (%d): %s" % (kind, len(names), ", ".join(sorted(names))))
    print("No status line: %d of %d rows -- unexamined, not passing."
          % (len(rows) - len(with_status), len(rows)))
    print("  These are scored by the scanner's window inference, which the")
    print("  Status Line rule says to delete. That walk is L-322's.")
    print("")
    print("Row shape: %d top-level assignment(s) read, %d failed."
          % (shape_checked, len(shape_failures)))
    print("  A value that is not a container literal must fit on the")
    print("  assignment's own line, because constants_change_report.py")
    print("  reads values line by line (L-324).")
    print("")

    if softs:
        print("REPORTED, does not fail the run (%d):" % len(softs))
        for name, message in softs:
            print("  %-44s %s" % (name, message))
        print("")

    # Two checks, two denominators. Status-line grammar is judged
    # against the rows that CARRY a status line; row shape is judged
    # against every top-level assignment. Merging the counts made a
    # shape failure print as a malformed status line, which names
    # the wrong thing and sends the reader to the wrong place.
    if failures:
        print("FAILURES (%d):" % len(failures))
        for name, message in failures:
            print("  %-44s %s" % (name, message))
        print("")
        print("Results: %d status line(s) checked, %d malformed;"
              " %d row shape(s) read, %d wrong."
              % (len(with_status), len(grammar_failures),
                 shape_checked, len(shape_failures)))
        print("")
        parts = []
        if grammar_failures:
            parts.append("%d of %d status lines are malformed"
                         % (len(grammar_failures), len(with_status)))
        if shape_failures:
            parts.append("%d of %d row shapes are wrong"
                         % (len(shape_failures), shape_checked))
        print("%s in %s." % (" and ".join(parts), TARGET))
        return 1

    print("Results: %d status line(s) checked, 0 malformed;"
          " %d row shape(s) read, 0 wrong."
          % (len(with_status), shape_checked))
    print("")
    print("All %d status lines in %s are well formed; %d rows carry none."
          % (len(with_status), TARGET, len(rows) - len(with_status)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
