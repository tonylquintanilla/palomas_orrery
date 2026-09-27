"""
patch_L322_D_15_exact_print_counts_20260927.py -- ORRERY repo.

Built on 0e3d05fd498f1ae8b49ec5dba58503f6bf448576
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery read at 70a77347cf65a14789707bf741cf203d29739c79
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Written 2026-09-27 with Anthropic's Claude Opus 5.5, Tony Quintanilla
integrator. L-322 Stage D, build manifest section 6, the orrery half.
Rules: provenance-discipline 2.20 (Rule 2's trailing-zero paragraph,
Rule 7's exact row), from patch_L322_D_14_prov220_skill.py.

RUN

  Save this file in the ORRERY REPO ROOT (next to palomas_orrery.py),
  open it in VS Code and click Run. It refuses to run from
  documentation/. File it in documentation/ AFTER it has run.

WHAT THIS DOES -- nine files

  constants_new.py
      The seven exact rows a display prints state their print count on
      their "# Figures:" line, directly after "exact --", from what each
      row says it was chosen with: the LEO edge 4 (the IADC's 2,000 km),
      the LEO floor 3 (200 km), the outer belt 2 (the midpoint 4.5),
      the solar wind pressure 1 (Shue's 2 nPa), Bz 1 (a zero prints as
      0), the two cut angles 3 (120 and 105 degrees).
  constants_rows.py
      Reads the print count as Row.prints. print_count_problem() refuses
      a count larger than the digits the number has, a count too small
      to write the number out in full, and any count but 1 on a zero.
      prints_of() and exact_text() let a display print an exact row by
      its count.
  export_constants.py
      Serves "prints" beside each row (SCHEMA 5) and fails, writing
      nothing, when print_count_problem() finds a problem.
  test_constants_export.py
      Compares "prints", and "uncertainty", which it should already
      have compared since schema 4 and did not (fixed in passing).
  earth_visualization_shells.py, shell_configs.py
      The eight lines that printed an exact row by ":g" or ",.0f" print
      it through exact_text(). The text on screen does not change.
  exact_rows_report.py
      Checks that every printed exact row states a count, that every
      orrery line prints it through exact_text(), and that the gallery
      serves the count beside it. Every failure is named; with --check
      it exits 1.
  orrery_maintenance_run.py, palomas_orrery_dashboard.py
      The report runs again among the CHECKERS, with --check, as
      "Exact rows by the count", so a failure fails the run; as a
      generator its exit code did not count. The dashboard gets the
      matching button, and the report's description stops saying it
      never gates. The runner's own count of gating checkers said
      sixteen when it was seventeen; it now says eighteen.

SUCCESS looks like: one "ok" line per edit, one "stamp" line per file,
then "patch applied" naming nine files.

FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written; all nine files are checked before any is written. Undo after
a success is Discard Changes in GitHub Desktop.

AFTERWARD -- do these in order

  1. (do) Run the orrery maintenance run.
     EXPECT ONE FAILED CHECKER: "Exact rows by the count". It names eleven
     gallery prints, on ten lines, as not served a print count yet.
     (One line prints both LEO altitudes.)
     That is correct and it stays red until gallery patch 4 is run: the
     gallery cannot copy the count until this export carries it. Every
     other checker should pass.
  2. (do) Commit and push the orrery.
  3. (do) Run gallery patch 4 when it arrives, then its cache build and
     the gallery maintenance run, commit and push.
  4. (do) Run the orrery maintenance run again. The exact rows report
     now passes. Commit and push the regenerated files.

WHAT IS PERMANENT

  The script is disposable. The print-count field, its checker, the
  export's "prints", exact_text() and the report's check are not.
"""

import hashlib
import os
import sys

FINGERPRINTS = {
    'constants_new.py': 'e630565d31f347fa4658fbdafecb8564',
    'constants_rows.py': '34bce8fe7365f1b3724dff1dc1aa8b30',
    'export_constants.py': '7f3a23f5408d08e097c06f5945631f87',
    'test_constants_export.py': 'd99067d542c3b0731909af524003b4a0',
    'earth_visualization_shells.py': '3d02188a2a11526343359ad6966fa394',
    'shell_configs.py': 'cc8ce3b374a6a0a86eb4d1bbd9307f22',
    'exact_rows_report.py': '193815a020fed3c1393a149c621ae58a',
    'orrery_maintenance_run.py': '92f273b18f199aaa435a194c890db890',
    'palomas_orrery_dashboard.py': '76a3bc1a426e78c757a937751d806fa0',
}

EDITS = {}

# ----------------------------------------------------------------------
# constants_new.py -- seven print counts and the stamp
# ----------------------------------------------------------------------

EDITS['constants_new.py'] = [
    ('stamp: module updated',
     b"""observed reach. They replace five numbers chosen by eye in
earth_visualization_shells.py)
\"\"\"
""",
     b"""observed reach. They replace five numbers chosen by eye in
earth_visualization_shells.py)
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D15: the seven exact rows a display prints state
their print count on their "# Figures:" line, directly after "exact --",
from the digits each was defined or chosen with. The trailing .0 each
is typed with is Python's, not a figure (provenance-discipline 2.20,
Rule 2).)
\"\"\"
""", 1),
    ('EARTH_LEO_UPPER_ALTITUDE_KM prints 4',
     b"""# Figures: exact -- the IADC protected region is DEFINED at an altitude
# Figures+: of 2,000 km. A definition, not a measurement.
""",
     b"""# Figures: exact -- prints 4, the definition's own digits (2,000 km). The
# Figures+: IADC protected region is DEFINED at that altitude. A definition,
# Figures+: not a measurement; the .0 is Python's (Rule 2).
""", 1),
    ('EARTH_LEO_LOWER_ALTITUDE_KM prints 3',
     b"""# Figures: exact -- a drawing choice, so all of its digits are known.
# Declared: the floor the orrery's LEO shell draws from.""",
     b"""# Figures: exact -- prints 3, the digits it was chosen with (200 km). A
# Figures+: drawing choice, so all of its digits are known; the .0 is
# Figures+: Python's (Rule 2).
# Declared: the floor the orrery's LEO shell draws from.""", 1),
    ('EARTH_VAN_ALLEN_OUTER_RADII prints 2',
     b"""# Figures: exact -- declared construction: midpoint of
# Figures+: EARTH_VAN_ALLEN_OUTER_BAND_LOW_L, EARTH_VAN_ALLEN_OUTER_BAND_HIGH_L
""",
     b"""# Figures: exact -- prints 2, the digits of the value its rule gives
# Figures+: (4.5); declared construction: midpoint of
# Figures+: EARTH_VAN_ALLEN_OUTER_BAND_LOW_L, EARTH_VAN_ALLEN_OUTER_BAND_HIGH_L
""", 1),
    ('EARTH_SOLAR_WIND_PRESSURE_NPA prints 1',
     b"""# Figures: exact -- a declared condition, not a measurement (Rule 2).
# Declared: the solar wind dynamic pressure both fits are evaluated at.
""",
     b"""# Figures: exact -- prints 1, the digits it was chosen with: Shue et al.
# Figures+: (1998) use Dp = 2 nPa. A declared condition, not a measurement;
# Figures+: the .0 is Python's (Rule 2).
# Declared: the solar wind dynamic pressure both fits are evaluated at.
""", 1),
    ('EARTH_SOLAR_WIND_BZ_NT prints 1',
     b"""# Figures: exact -- a declared condition, not a measurement (Rule 2).
# Declared: a neutral midpoint chosen here, NOT a figure from the paper.
""",
     b"""# Figures: exact -- prints 1, because a zero prints as 0 (Rule 7). A
# Figures+: declared condition, not a measurement; the .0 is Python's
# Figures+: (Rule 2).
# Declared: a neutral midpoint chosen here, NOT a figure from the paper.
""", 1),
    ('EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG prints 3',
     b"""# Figures: exact -- a declared drawing limit (Rule 2).
# Declared: where the drawn magnetopause stops, measured from the nose.
""",
     b"""# Figures: exact -- prints 3, the digits it was chosen with (120
# Figures+: degrees). A declared drawing limit; the .0 is Python's (Rule 2).
# Declared: where the drawn magnetopause stops, measured from the nose.
""", 1),
    ('EARTH_BOW_SHOCK_CUT_ANGLE_DEG prints 3',
     b"""# Declared+: 100 and stop the drawn shock five degrees short.
# Figures: exact -- a declared drawing limit (Rule 2).
""",
     b"""# Declared+: 100 and stop the drawn shock five degrees short.
# Figures: exact -- prints 3, the digits of the conversion that sets it
# Figures+: (7 h x 15 deg/h = 105 degrees). A declared drawing limit; the
# Figures+: .0 is Python's (Rule 2).
""", 1),
]

# ----------------------------------------------------------------------
# constants_rows.py -- read the count, check it, print by it
# ----------------------------------------------------------------------

EDITS['constants_rows.py'] = [
    ('docstring: what a row carries',
     b"""                           Rule 1); prose around it is never read

""",
     b"""                           Rule 1); prose around it is never read
    prints                 the print count of an exact row a display
                           prints, an int, or None. Read ONLY in the field
                           form directly after "exact --", as
                           "exact -- prints 3", because measured rows'
                           "# Figures:" lines say "the source prints 1.5"
                           in prose (provenance-discipline 2.20, Rule 7)

""", 1),
    ('docstring: stamp',
     b"""stated uncertainty beside its value, as Earth's magnetotail hover does.)
\"\"\"
""",
     b"""stated uncertainty beside its value, as Earth's magnetotail hover does.)
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D15: an exact row's print count is read here as
Row.prints; print_count_problem() is the one check of it, which the
export runs on every row; prints_of() and exact_text() let an orrery
display print an exact row by its count instead of by a width chosen on
its own line. provenance-discipline 2.20, Rule 7.)
\"\"\"
""", 1),
    ('PRINTS_FIELD_RE',
     b"""UNCERTAINTY_FIELD_RE = re.compile(
    r"\\buncertainty\\s+([-+]?(?:\\d+\\.?\\d*|\\.\\d+)(?:[eE][-+]?\\d+)?)")
""",
     b"""UNCERTAINTY_FIELD_RE = re.compile(
    r"\\buncertainty\\s+([-+]?(?:\\d+\\.?\\d*|\\.\\d+)(?:[eE][-+]?\\d+)?)")
# The print count of an exact row (provenance-discipline 2.20, Rule 7):
# anchored directly after "exact --", so the prose "the source prints
# 1.5" on a measured row's line is never read as one.
PRINTS_FIELD_RE = re.compile(r"^exact\\s*--\\s*prints\\s+(\\d+)\\b")
""", 1),
    ('Row.prints',
     b"""        self.uncertainty = None
        self.status = None
""",
     b"""        self.uncertainty = None
        self.prints = None
        self.status = None
""", 1),
    ('_fill_fields: read the count',
     b"""        match = UNCERTAINTY_FIELD_RE.search(row.figures_text)
        if match:
            row.uncertainty = match.group(1)
""",
     b"""        match = UNCERTAINTY_FIELD_RE.search(row.figures_text)
        if match:
            row.uncertainty = match.group(1)
        if row.figures == "exact":
            match = PRINTS_FIELD_RE.match(row.figures_text)
            if match:
                row.prints = int(match.group(1))
                if row.prints < 1:
                    row.figures_error = ("'prints %s': a print count is at "
                                         "least 1" % match.group(1))
""", 1),
    ('prints_of, print_count_problem, format_prints, exact_text',
     b"""def names_in(text, known):
""",
     b"""_PRINTS_BY_DIR = {}


def prints_of(name, project_dir=None):
    \"\"\"The print count exact row `name` states, an int, or None.

    A name that is not a row raises KeyError, as in figures_of().
    L-322 Stage D, patch D15.
    \"\"\"
    project_dir = project_dir or os.path.dirname(os.path.abspath(__file__))
    table = _PRINTS_BY_DIR.get(project_dir)
    if table is None:
        _text, _rows, by_name = read_store(project_dir)
        table = dict((row_name, row.prints)
                     for row_name, row in by_name.items())
        _PRINTS_BY_DIR[project_dir] = table
    return table[name]


def _written_digits(text):
    \"\"\"How many digits a number, as written, has from its first non-zero
    digit to its last digit, trailing zeros included: 200.0 has four,
    2.0 two, 4.5 two, 0.0 none. The ceiling a print count may not pass.
    \"\"\"
    mantissa = text.strip().lstrip("+-").split("e")[0].split("E")[0]
    digits = mantissa.replace(".", "").lstrip("0")
    return len(digits)


def print_count_problem(row, value):
    \"\"\"Why `row`'s print count is wrong for `value`, or None.

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
    \"\"\"
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
    \"\"\"`value` at `prints` significant figures, in plain digits.

    The same result as the gallery's sigFigures(): 4.5 at two figures is
    "4.5", 2.0 at one is "2", 120.0 at three is "120", 0.0 at one is "0".
    grouping=True adds a thousands separator, "2,000".
    \"\"\"
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
    \"\"\"Exact row `name` as text, at the print count its row states.

    For an orrery display (provenance-discipline 2.20, Rule 7). The value
    and the count are read by the same name, so they cannot come from
    different rows. A row that states no print count raises ValueError
    where the display is built, instead of a width being chosen for it.
    L-322 Stage D, patch D15.
    \"\"\"
    import constants_new
    prints = prints_of(name)
    if prints is None:
        raise ValueError("%s states no print count; add 'prints N' after "
                         "'exact --' on its # Figures: line" % name)
    return format_prints(getattr(constants_new, name), prints, grouping)


def names_in(text, known):
""", 1),
    ('import math',
     b"""import ast
import hashlib
import os
import re
""",
     b"""import ast
import hashlib
import math
import os
import re
""", 1),
]

# ----------------------------------------------------------------------
# export_constants.py -- serve the count, refuse a wrong one
# ----------------------------------------------------------------------

EDITS['export_constants.py'] = [
    ('docstring: prints field',
     b"""                              row states none (schema 4). A display prints
                              it beside the value, as written
""",
     b"""                              row states none (schema 4). A display prints
                              it beside the value, as written
                     prints   the print count an exact row states, or
                              null (schema 5). A display prints an exact
                              row to that many significant figures,
                              never by a width of its own
                              (provenance-discipline 2.20, Rule 7)
""", 1),
    ('docstring: what makes it fail',
     b"""    - a \"# Unit:\" or \"# Figures:\" line that cannot be read
""",
     b"""    - a \"# Unit:\" or \"# Figures:\" line that cannot be read
    - a print count constants_rows.print_count_problem() refuses: larger
      than the digits the number has, too small to write it in full, or
      anything but 1 on a zero
""", 1),
    ('docstring: stamp',
     b"""their stated uncertainties as the orrery does. SCHEMA moves to 4.)
\"\"\"
""",
     b"""their stated uncertainties as the orrery does. SCHEMA moves to 4.)
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D15: every exported row also carries \"prints\",
the print count of an exact row a display prints, and a count
constants_rows.print_count_problem() refuses stops the export. SCHEMA
moves to 5.)
\"\"\"
""", 1),
    ('SCHEMA 5',
     b"""SCHEMA = 4
""",
     b"""SCHEMA = 5
""", 1),
    ('refuse a wrong print count',
     b"""        value, problem = _export_value(values.get(row.name), row.figures,
                                       row.name)
        if problem:
            failures.append((row.name, problem))
            continue
""",
     b"""        value, problem = _export_value(values.get(row.name), row.figures,
                                       row.name)
        if problem:
            failures.append((row.name, problem))
            continue
        problem = constants_rows.print_count_problem(
            row, values.get(row.name))
        if problem:
            failures.append((row.name, problem))
            continue
""", 1),
    ('serve prints',
     b"""            \"uncertainty\": row.uncertainty,
        }
""",
     b"""            \"uncertainty\": row.uncertainty,
            \"prints\": row.prints,
        }
""", 1),
]

# ----------------------------------------------------------------------
# test_constants_export.py -- compare the new field, and uncertainty
# ----------------------------------------------------------------------

EDITS['test_constants_export.py'] = [
    ('docstring: check 2 fields',
     b"""    2. Re-reading the store now gives the same rows as the file: value,
       unit, figures, status, derived, read and inputs, for every row.
""",
     b"""    2. Re-reading the store now gives the same rows as the file: value,
       unit, figures, status, derived, read, inputs, uncertainty and
       prints, for every row.
""", 1),
    ('docstring: stamp',
     b"""(L-322 Stage C2: check 2 compares \"read\" and \"inputs\" too.)
\"\"\"
""",
     b"""(L-322 Stage C2: check 2 compares \"read\" and \"inputs\" too.)
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D15: check 2 compares \"prints\", new in schema 5,
and \"uncertainty\", which the export has served since schema 4 and this
check did not compare until now.)
\"\"\"
""", 1),
    ('ROW_FIELDS',
     b"""ROW_FIELDS = (\"value\", \"unit\", \"figures\", \"status\", \"derived\", \"read\",
              \"inputs\")
""",
     b"""ROW_FIELDS = (\"value\", \"unit\", \"figures\", \"status\", \"derived\", \"read\",
              \"inputs\", \"uncertainty\", \"prints\")
""", 1),
]

# ----------------------------------------------------------------------
# earth_visualization_shells.py -- six lines print by the count
# ----------------------------------------------------------------------

EDITS['earth_visualization_shells.py'] = [
    ('import exact_text',
     b"""from constants_rows import figures_of, uncertainty_of
""",
     b"""from constants_rows import figures_of, uncertainty_of, exact_text
""", 1),
    ('pressure, three lines',
     b"""{EARTH_SOLAR_WIND_PRESSURE_NPA:g} nPa""",
     b"""{exact_text('EARTH_SOLAR_WIND_PRESSURE_NPA')} nPa""", 3),
    ('outer belt peak, two lines',
     b"""{EARTH_VAN_ALLEN_OUTER_RADII:g}""",
     b"""{exact_text('EARTH_VAN_ALLEN_OUTER_RADII')}""", 2),
    ('LEO altitude range',
     b"""Altitude range: {EARTH_LEO_LOWER_ALTITUDE_KM:,.0f} km to {EARTH_LEO_UPPER_ALTITUDE_KM:,.0f} km above surface""",
     b"""Altitude range: {exact_text('EARTH_LEO_LOWER_ALTITUDE_KM', grouping=True)} km to {exact_text('EARTH_LEO_UPPER_ALTITUDE_KM', grouping=True)} km above surface""",
     1),
    ('docstring: stamp',
     b"""    rings only mark its extent.
Module updated: September 25, 2026 with Anthropic's Claude Opus 5.5
\"\"\"
""",
     b"""    rings only mark its extent.
September 27, 2026 (L-322 Stage D, patch D15, Opus 5.5): the six hover
    lines that print an exact row -- the solar wind pressure three times,
    the outer belt's drawn peak twice and the LEO altitudes once -- print
    it through constants_rows.exact_text(), at the print count its row
    states, where they used a width chosen on the line (":g", ",.0f").
    The text shown does not change.
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5
\"\"\"
""", 1),
]

# ----------------------------------------------------------------------
# shell_configs.py -- two tooltip lines print by the count
# ----------------------------------------------------------------------

EDITS['shell_configs.py'] = [
    ('import exact_text',
     b"""from constants_rows import figures_of
from constants_new import (
""",
     b"""from constants_rows import figures_of, exact_text
from constants_new import (
""", 1),
    ('outer belt peak',
     b"""f\"{EARTH_VAN_ALLEN_OUTER_RADII:g} Earth radii out (doi:10.1029/2024JA033504).""",
     b"""f\"{exact_text('EARTH_VAN_ALLEN_OUTER_RADII')} Earth radii out (doi:10.1029/2024JA033504).""",
     1),
    ('LEO altitude range',
     b"""roughly {EARTH_LEO_LOWER_ALTITUDE_KM:,.0f} km to {EARTH_LEO_UPPER_ALTITUDE_KM:,.0f} km altitude""",
     b"""roughly {exact_text('EARTH_LEO_LOWER_ALTITUDE_KM', grouping=True)} km to {exact_text('EARTH_LEO_UPPER_ALTITUDE_KM', grouping=True)} km altitude""",
     1),
    ('docstring: stamp',
     b"""    four figures by a fixed format.)
\"\"\"
""",
     b"""    four figures by a fixed format.)
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5 (L-322
    Stage D, patch D15: the magnetosphere tooltip's outer belt peak and
    the LEO tooltip's two altitudes, which are exact rows, print through
    constants_rows.exact_text() at the print count their rows state,
    where they used ":g" and ",.0f". The text does not change.)
\"\"\"
""", 1),
]

# ----------------------------------------------------------------------
# exact_rows_report.py -- the check that makes "finished" able to fail
# ----------------------------------------------------------------------

EDITS['exact_rows_report.py'] = [
    ('docstring: it is a check now',
     b"""It changes nothing and chooses no width. It is a report.
""",
     b"""It changes nothing and chooses no width.

IT IS ALSO A CHECK (patch D15). Rule 7's exact row is built: a printed
exact row states its print count on its \"# Figures:\" line, the export
serves it as \"prints\", orrery displays print through
constants_rows.exact_text(), and the gallery prints by the served
count. Every run prints the check's verdict, a line beginning \"EXACT
ROWS BY THE COUNT:\", and names each failing item. Run with --check,

    python exact_rows_report.py --check

it also exits 1 when the check fails. Without --check it exits 0, which
is how the maintenance run calls it among its GENERATORS, where an exit
code does not count; it calls it again with --check among its
CHECKERS, as \"Exact rows by the count\", where it does. The check
fails when:

    - a printed exact row states no print count;
    - an orrery line prints an exact row any way but exact_text() -- a
      \"{...}\" format, _declared, %, str() or format(): a width chosen
      on the line;
    - a gallery pointer to a printed exact row serves no \"prints\", or
      serves a different count from the row's.

The gallery half checks that the count is SERVED beside the value. That
the page's line prints by it is checked by the gallery's own
documentation/smoke_display_figures.js, which grades the built hovers'
text; this tool reads code, not output, and says so rather than
claiming more.
""", 1),
    ('docstring: orrery half names exact_text',
     b"""form: inside {...} in a formatted string, as the argument of
_declared, _whole_figures or _with_uncertainty, after %, or inside
str(...) or format(...).
""",
     b"""form: inside {...} in a formatted string, as the argument of
exact_text, _declared, _whole_figures or _with_uncertainty, after %,
or inside str(...) or format(...). Only exact_text prints by the count.
""", 1),
    ('docstring: stamp',
     b"""FOLLOWED.)
\"\"\"
""",
     b"""FOLLOWED.)
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D15, manifest section 6: the check above, so the
report says when section 6 is finished and the maintenance run fails
while it is not. The orrery search also finds exact_text().)
\"\"\"
""", 1),
    ('orrery pattern: exact_text',
     b"""        r'\\{\\s*%s\\b[^}]*\\}' % n
        + r'|(?:_declared|_whole_figures|_with_uncertainty)\\(\\s*[\\'\"]%s[\\'\"]' % n
""",
     b"""        r'\\{\\s*%s\\b[^}]*\\}' % n
        + r'|exact_text\\(\\s*[\\'\"]%s[\\'\"]' % n
        + r'|(?:_declared|_whole_figures|_with_uncertainty)\\(\\s*[\\'\"]%s[\\'\"]' % n
""", 1),
    ('by_count helper',
     b"""def read_lines(path):
""",
     b"""def by_count(name, code):
    \"\"\"True when no print of `name` on this line uses a width of its
    own: every printing form but exact_text() is one. A name passed to
    arithmetic on the same line, such as _km_above_surface(NAME, 2), is
    not a print of it.\"\"\"
    n = re.escape(name)
    by_width = re.compile(
        r'\\{\\s*%s\\b[^}]*\\}' % n
        + r'|(?:_declared|_whole_figures|_with_uncertainty)\\(\\s*[\\'\"]%s[\\'\"]' % n
        + r'|%%\\s*\\(?\\s*%s\\b' % n
        + r'|(?:str|format)\\(\\s*%s\\b' % n)
    return not by_width.search(code)


def served_node(config, path):
    \"\"\"The node at a config_pointers() path, or None.\"\"\"
    node = config
    for part in path.strip('/').split('/'):
        if isinstance(node, dict) and part in node:
            node = node[part]
        elif isinstance(node, list) and part.isdigit() \\
                and int(part) < len(node):
            node = node[int(part)]
        else:
            return None
    return node


def read_lines(path):
""", 1),
    ('main: collect the check',
     b"""    printed = [n for n in names if o_sites[n] or g_sites.get(n)]
    unprinted = [n for n in names if n not in printed]
""",
     b"""    printed = [n for n in names if o_sites[n] or g_sites.get(n)]
    unprinted = [n for n in names if n not in printed]

    # The check (patch D15): named items, never a count alone.
    no_count = [n for n in printed if constants_rows.prints_of(n, HERE)
                is None]
    by_width = [(n, f, l, code) for n in printed
                for f, l, code in o_sites[n] if not by_count(n, code)]
    not_served = []
    if gallery_read:
        for n in printed:
            want = constants_rows.prints_of(n, HERE)
            for f, l, code, path in g_sites.get(n, []):
                node = served_node(config, path)
                got = node.get('prints') if isinstance(node, dict) else None
                if got != want:
                    not_served.append((n, f, l, path, got, want))
    failing = bool(no_count or by_width or not_served)
""", 1),
    ('main: report section',
     b"""    add('## Printed')
    add('')
    for n in printed:
""",
     b"""    add('## Printed by the count')
    add('')
    add('Rule 7: each printed exact row states a print count, each orrery '
        'line prints it through `exact_text()`, and the gallery serves '
        'the count beside it. **%s**'
        % ('FAILING -- the items below are named.' if failing
           else 'PASSING: %d rows, every one counted, on %d lines.'
           % (len(printed), len(o_lines) + len(g_lines))))
    add('')
    for n in printed:
        add('- `%s`: prints %s' % (n, constants_rows.prints_of(n, HERE)
                                   if n not in no_count
                                   else 'NO COUNT STATED'))
    if by_width:
        add('')
        add('Orrery lines that print an exact row by a width of their own:')
        add('')
        for n, f, l, code in by_width:
            add('- `%s` at `%s` line %d: `%s`' % (n, f, l, short(code)))
    if not_served:
        add('')
        add('Gallery lines whose served entry does not carry the row\\'s '
            'count (\"prints\" in `data/objects_config.json`):')
        add('')
        for n, f, l, path, got, want in not_served:
            add('- `%s` at `%s` line %d (config `%s`): serves %s, the row '
                'states %s' % (n, f, l, path, got, want))
    if not gallery_read:
        add('')
        add('The gallery half was not read, so this check covers the '
            'orrery only.')
    add('')
    add('## Printed')
    add('')
    for n in printed:
""", 1),
    ('main: summary and exit',
     b"""    else:
        summary += '; the gallery folder was not found'
    print(summary)
    return 0
""",
     b"""    else:
        summary += '; the gallery folder was not found'
    print(summary)
    if failing:
        for n in no_count:
            print('  FAIL %s: printed, but states no print count' % n)
        for n, f, l, _code in by_width:
            print('  FAIL %s: %s line %d prints it by a width of its own'
                  % (n, f, l))
        for n, f, l, path, got, want in not_served:
            print('  FAIL %s: gallery %s line %d, served prints %s, the row '
                  'states %s' % (n, f, l, got, want))
        print('EXACT ROWS BY THE COUNT: FAILING -- %d row(s) with no count, '
              '%d orrery print(s) by a width, %d gallery print(s) not served '
              'the count' % (len(no_count), len(by_width), len(not_served)))
        return 1 if '--check' in sys.argv[1:] else 0
    print('EXACT ROWS BY THE COUNT: PASSING -- %d printed exact rows each '
          'state a count; %d orrery lines print through exact_text(); %s'
          % (len(printed), len(o_lines),
             '%d gallery lines are served the count' % len(g_lines)
             if gallery_read else 'the gallery half was not read'))
    return 0
""", 1),
]


# ----------------------------------------------------------------------
# orrery_maintenance_run.py -- the check counts as a checker
# ----------------------------------------------------------------------

EDITS['orrery_maintenance_run.py'] = [
    ('checker row: Exact rows by the count',
     b"""    ('Constants export check', ['test_constants_export.py'], None),
""",
     b"""    ('Constants export check', ['test_constants_export.py'], None),
    # Rule 7's exact row, built: every printed exact row states a print
    # count, every orrery line prints it through exact_text(), and the
    # gallery serves the count. The same script as the Exact rows report
    # generator, run with --check so its failure fails this run; as a
    # generator its exit code would not count. L-322 Stage D, patch D15.
    ('Exact rows by the count', ['exact_rows_report.py', '--check'],
     'EXACT ROWS BY THE COUNT:'),
""", 1),
    ('docstring: gating count',
     b"""Sixteen checkers are pass/fail: a problem makes them exit non-zero.
""",
     b"""Eighteen checkers are pass/fail: a problem makes them exit non-zero.
""", 1),
    ('docstring: headline count',
     b"""gating sixteen in its headline and quotes the two report-only verdicts
""",
     b"""gating eighteen in its headline and quotes the two report-only verdicts
""", 1),
    ('docstring: stamp',
     b"""shows in the run instead of only in a file nobody opens.)
\"\"\"
""",
     b"""shows in the run instead of only in a file nobody opens.)
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5 (L-322
Stage D, patch D15: CHECKERS gains Exact rows by the count,
exact_rows_report.py --check, so a printed exact row with no print count,
or printed by a width of its own, fails the run; as a generator the same
script's exit code did not count. The gating count above said sixteen,
one behind since patch D3 added Earth pole of date; it is eighteen.)
\"\"\"
""", 1),
]

# ----------------------------------------------------------------------
# palomas_orrery_dashboard.py -- the report's words, and a button
# ----------------------------------------------------------------------

EDITS['palomas_orrery_dashboard.py'] = [
    ('Exact Rows Report description',
     b"""         \"missing. Report-only: writes EXACT_ROWS_PRINTED.md and never \"
         \"gates a push. The maintenance run runs it every time.\",
""",
     b"""         \"missing. Writes EXACT_ROWS_PRINTED.md and prints whether every \"
         \"printed exact row prints by its count; this button never fails. \"
         \"Test Exact Rows By The Count is the same check as a pass/fail.\",
""", 1),
    ('button: Test Exact Rows By The Count',
     b"""         \"Never contacts Horizons; Earth Pole Live Check does.\",
         SCRIPT_DIR,
         True,
         None,
         True),
""",
     b"""         \"Never contacts Horizons; Earth Pole Live Check does.\",
         SCRIPT_DIR,
         True,
         None,
         True),
        (\"Test Exact Rows By The Count\",
         \"exact_rows_report.py\",
         \"Fails when a printed exact row of constants_new.py states no \"
         \"print count, when an orrery line prints one by a width of its \"
         \"own instead of through exact_text(), or when the gallery does not \"
         \"serve the count beside it. Names every failing item. The same \"
         \"script as Exact Rows Report, run with --check.\",
         SCRIPT_DIR,
         True,
         [\"--check\"],
         True),
""", 1),
    ('docstring: stamp',
     b"""orrery root. No other entry touched.
\"\"\"
""",
     b"""orrery root. No other entry touched.
September 27, 2026 with Anthropic's Claude Opus 5.5 (L-322 Stage D, patch
D15): added Test Exact Rows By The Count to the checkers, in alphabetical
place, matching the maintenance runner's new checker; and Exact Rows
Report's description no longer says it is report-only.
\"\"\"
""", 1),
]


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def fail(msg):
    print(msg)
    print('NOTHING was written. Undo is not needed.')
    sys.exit(1)


def convention(data, old, new):
    if data.count(b'\r\n') > 0:
        return old.replace(b'\n', b'\r\n'), new.replace(b'\n', b'\r\n')
    return old, new


def main():
    if os.path.basename(os.getcwd()) == 'documentation':
        fail('ERROR: this is running from documentation/. Run it from the '
             'orrery repo root, then file it in documentation/.')
    results = {}
    for path in FINGERPRINTS:
        if not os.path.exists(path):
            fail('ERROR: %s not found. Run this from the orrery repo root.'
                 % path)
        with open(path, 'rb') as f:
            data = f.read()
        fp = fingerprint(data)
        if fp != FINGERPRINTS[path]:
            fail('ERROR: %s is not the file this patch was built on '
                 '(fingerprint %s, expected %s). Pull or discard local '
                 'changes first.' % (path, fp, FINGERPRINTS[path]))
        for label, old, new, count in EDITS[path]:
            old, new = convention(data, old, new)
            n = data.count(old)
            if n != count:
                fail('ANCHOR FAIL: %s: "%s" -- expected %d match(es), got %d'
                     % (path, label, count, n))
            data = data.replace(old, new)
            print('ok    %s: %s' % (path, label))
        try:
            data.decode('ascii')
        except UnicodeDecodeError as exc:
            fail('ERROR: %s would not be ASCII after the patch (%s).'
                 % (path, exc))
        results[path] = data
    for path, data in results.items():
        with open(path, 'wb') as f:
            f.write(data)
        print('stamp %s: Module updated September 27, 2026 (patch D15)'
              % path)
    print('patch applied: %s' % ', '.join(results))
    print('Next: run the orrery maintenance run. Expect exactly one FAILED '
          'checker, "Exact rows by the count", naming eleven gallery prints, on '
          'ten lines, not served a print count yet; gallery patch 4 clears '
          'it.')


if __name__ == '__main__':
    main()
