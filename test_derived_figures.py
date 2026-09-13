"""
test_derived_figures.py -- a derived constant carries the figures its
sources support, and still follows from the inputs it names.

WHY THIS EXISTS

    A derived row used to be stored two different ways.
    EARTH_BOW_SHOCK_STANDOFF_RADII held the expression, so Python
    recomputed it on every import and it followed its inputs
    automatically. EARTH_MAGNETOPAUSE_STANDOFF_RADII held a literal,
    because the gallery's store parser cannot evaluate a tanh -- so it
    followed nothing. Its Status line named EARTH_SOLAR_WIND_PRESSURE_NPA
    as an input, that pressure is declared pending under L-314, and when
    it moves the row would have gone quietly stale. No test covered
    either row.

    Tony's ruling of 2026-09-12 (L-325) settled both: a store carries
    the figures its sources support, not the arithmetic result. Sixteen
    digits on a value uncertain in the first decimal is calculator
    output, not precision. Both rows are now literals at their reported
    figures.

    That trades an automatic recomputation for a check that announces,
    and this is the check. It recomputes each derived row from the
    inputs the row itself names, rounds to the figures the row's own
    REPORT declares, and fails when the two stop agreeing. When the
    declared pressure moves, this is what says so.

WHAT WOULD MAKE THIS FAIL

    - an input constant changes and the stored figure no longer follows
      from it
    - the stored literal carries more figures than its REPORT declares
    - a row's REPORT annotation goes missing or stops being readable
    - a derived row is added to the store that this file does not cover

    The last one carries the most weight. A checker that silently skips
    what it does not know about passes while blind, so an uncovered
    derived row FAILS here rather than being quietly ignored.

WHAT THIS DOES NOT DO

    It does not judge how many figures a value should have. That is
    settled on the row, in prose, against the source's own uncertainty,
    under provenance-discipline. This file reads the row's declared
    figure and checks the arithmetic against it.

Role: devtool
Domain: dev_tools

Module created: September 2026 with Anthropic's Claude Opus 5.
"""

import math
import os
import re
import sys

TARGET = "constants_new.py"

REPORT_RE = re.compile(r"REPORT\s+([0-9]+(?:\.[0-9]+)?)")
ASSIGN_RE = re.compile(r"^([A-Z][A-Z0-9_]*)\s*=\s*(.+?)\s*$")


# ------------------------------------------------------------------
# The derivations, one per derived row.
#
# Each names the inputs the row's Status line names and computes the
# value from them. The formula is written out here rather than read
# from the row, because a formula parsed from a comment would be
# checked against itself.
# ------------------------------------------------------------------

def _magnetopause(c):
    """Shue et al. (1998) eq. 10: (a1 + a2 tanh[a3 (Bz + a4)]) Dp^(-1/a5)."""
    return ((c.EARTH_MAGNETOPAUSE_SHUE_A1_RADII
             + c.EARTH_MAGNETOPAUSE_SHUE_A2_RADII
             * math.tanh(c.EARTH_MAGNETOPAUSE_SHUE_A3_PER_NT
                         * (c.EARTH_SOLAR_WIND_BZ_NT
                            + c.EARTH_MAGNETOPAUSE_SHUE_A4_NT)))
            * c.EARTH_SOLAR_WIND_PRESSURE_NPA
            ** (-1.0 / c.EARTH_MAGNETOPAUSE_SHUE_A5))


def _bow_shock(c):
    """Jelinek et al. (2012) eq. 14: R0 Dp^(-1/eps)."""
    return (c.EARTH_BOW_SHOCK_JELINEK_R0_RADII
            * c.EARTH_SOLAR_WIND_PRESSURE_NPA
            ** (-1.0 / c.EARTH_BOW_SHOCK_JELINEK_EPS))


DERIVATIONS = {
    "EARTH_MAGNETOPAUSE_STANDOFF_RADII": {
        "compute": _magnetopause,
        "paper": "Shue et al. (1998) eq. 10",
        "inputs": [
            "EARTH_MAGNETOPAUSE_SHUE_A1_RADII",
            "EARTH_MAGNETOPAUSE_SHUE_A2_RADII",
            "EARTH_MAGNETOPAUSE_SHUE_A3_PER_NT",
            "EARTH_MAGNETOPAUSE_SHUE_A4_NT",
            "EARTH_MAGNETOPAUSE_SHUE_A5",
            "EARTH_SOLAR_WIND_BZ_NT",
            "EARTH_SOLAR_WIND_PRESSURE_NPA",
        ],
    },
    "EARTH_BOW_SHOCK_STANDOFF_RADII": {
        "compute": _bow_shock,
        "paper": "Jelinek et al. (2012) eq. 14",
        "inputs": [
            "EARTH_BOW_SHOCK_JELINEK_R0_RADII",
            "EARTH_BOW_SHOCK_JELINEK_EPS",
            "EARTH_SOLAR_WIND_PRESSURE_NPA",
        ],
    },
}


def significant_figures(literal):
    """How many significant figures a decimal literal states.

    "10.25" is four. Leading zeros do not count, so "0.069" is two.
    """
    digits = literal.strip().lstrip("+-").replace(".", "").lstrip("0")
    return len(digits) if digits else 1


def round_to(value, figures):
    return float("%.*g" % (figures, value))


def read_store(path):
    with open(path, "r") as handle:
        return handle.read()


def blocks(text):
    """Every top-level assignment, with the comment block beneath it.

    Returns {name: (value_text, annotation_lines)}.
    """
    lines = text.split("\n")
    found = {}
    for i, line in enumerate(lines):
        match = ASSIGN_RE.match(line)
        if not match:
            continue
        notes = []
        for j in range(i + 1, len(lines)):
            if lines[j].startswith("#"):
                notes.append(lines[j])
            else:
                break
        found[match.group(1)] = (match.group(2), notes)
    return found


def derived_names(store):
    """Names whose Status line calls the row derived."""
    names = []
    for name, (_value, notes) in store.items():
        for note in notes:
            if note.startswith("# Status:") and "derived" in note:
                names.append(name)
                break
    return sorted(names)


def declared_report(notes):
    """The REPORT figure the row states, as (literal, value, figures)."""
    for note in notes:
        match = REPORT_RE.search(note)
        if match:
            literal = match.group(1)
            return literal, float(literal), significant_figures(literal)
    return None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s is not beside this script." % TARGET)
        return 1

    sys.path.insert(0, here)
    try:
        import constants_new
    except Exception as exc:                      # noqa: BLE001
        print("ERROR: %s would not import: %s" % (TARGET, exc))
        return 1

    store = blocks(read_store(path))
    names = derived_names(store)

    print("=" * 70)
    print("  DERIVED FIGURES -- %s" % TARGET)
    print("=" * 70)
    print("")
    print("A derived row stores the figure its sources support, not the")
    print("arithmetic result. Each row below is recomputed from the inputs")
    print("it names and compared against the figure it declares (L-325).")
    print("")

    failures = []

    # A derived row this file does not know about is a row nothing
    # checks. Announce it and fail, rather than passing while blind.
    uncovered = [n for n in names if n not in DERIVATIONS]
    for name in uncovered:
        failures.append((name, "derived row with no derivation in "
                               "test_derived_figures.py -- add one"))

    retired = [n for n in DERIVATIONS if n not in names]
    for name in retired:
        failures.append((name, "this file derives it, but the store no "
                               "longer marks the row derived"))

    checked = 0
    for name in names:
        if name not in DERIVATIONS:
            continue
        entry = DERIVATIONS[name]
        value_text, notes = store[name]
        report = declared_report(notes)

        if report is None:
            failures.append((name, "no REPORT figure declared on the row"))
            continue
        literal, reported, figures = report

        try:
            stored = float(value_text)
        except ValueError:
            failures.append((name,
                             "value is not a plain literal (%s); a derived "
                             "row stores its reported figure" % value_text))
            continue

        recomputed = entry["compute"](constants_new)
        rounded = round_to(recomputed, figures)
        checked += 1

        print("  %s" % name)
        print("      %s, from %d input(s): %s"
              % (entry["paper"], len(entry["inputs"]),
                 ", ".join(entry["inputs"])))
        print("      recomputed %.12g -> %d figures -> %g"
              % (recomputed, figures, rounded))
        print("      stored %g, declared REPORT %s" % (stored, literal))

        if stored != reported:
            failures.append((name,
                             "stored %g but the row declares REPORT %s"
                             % (stored, literal)))
        elif rounded != reported:
            failures.append((name,
                             "recomputes to %.12g, which is %g at %d "
                             "figures, but the row stores %s -- an input "
                             "moved" % (recomputed, rounded, figures,
                                        literal)))
        elif significant_figures(value_text) > figures:
            failures.append((name,
                             "stored literal %s carries more figures than "
                             "REPORT %s declares" % (value_text, literal)))
        else:
            print("      OK")
        print("")

    if failures:
        print("FAILURES (%d):" % len(failures))
        for name, message in failures:
            print("  %-38s %s" % (name, message))
        print("")
        print("%d of %d derived rows in %s are wrong."
              % (len(failures), len(names), TARGET))
        return 1

    print("All %d derived row(s) in %s recompute to the figures they "
          "declare." % (checked, TARGET))
    return 0


if __name__ == "__main__":
    sys.exit(main())
