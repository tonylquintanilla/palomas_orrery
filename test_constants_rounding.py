"""
test_constants_rounding.py - The rule a conversion is rounded by, held
by values worked out by hand: constants_rows._to_place(), the last step
of every "in" value the constants export serves.

Run from the project directory (VS Code: open this file, click Run):
    python test_constants_rounding.py

Exits 0 if every pin holds and every planted fault is caught, 1
otherwise. The maintenance run executes it as a gating checker,
"Constants rounding", and its last line starts "CONSTANTS ROUNDING:".
It judges a function, not data, so it is not in the night set.

WHY THIS EXISTS
---------------
The Constants export check (test_constants_export.py, check 6)
re-computes each served conversion at the count the export serves, so
it can only say the export used the function. It cannot say the
function follows the rule. On 2026-10-31 the function did not: a
rounding that carried into a new leading digit was re-rounded from the
original value at one more figure, which undid the carry. The belt's
90th-percentile height, 0.667 AU, was served as 99,800,000 km where the
rule gives 100,000,000, and the function's own docstring example, 9.996
at the hundredths, came back 9.996 instead of 10.00. The check 6 pin
had been written against the function's output, so it held the fault
in place (HANDOFF_coordination_20261031.md, section 1).

So these pins are worked BY HAND from the rule, never read from the
function (GPT's criterion (ii), the same handoff, section 4). The rule
is provenance-discipline references/figures.md, Rule 3, "A value in
another unit is computed, never stored": the count is the figures of
the full-digit value down to the place, never fewer than one; Rule 5,
round half to even. Tony, 2026-10-31, 17:10: "do all the computations
with all the numbers and round at the end to significant figures."

WHAT IT CHECKS
--------------
Each pin is (value, place, expected value, expected figures):

  the belt's case     99,781,779.76 at 10**6  -> 100,000,000, 3
  the docstring case  9.996 at 10**-2         -> 10.00, 4
  a carry at units    9.6 at 10**0            -> 10, 2
  no carry            1,234.5 at 10**1        -> 1,230, 3
  the one-figure branch, kept on purpose: the place coarser than the
  leading digit keeps one leading figure, so 637,800 at 10**6 stays
  600,000, one figure, and does not become 1,000,000
                      637,800 at 10**6        -> 600,000, 1
  half to even        2.5 at 10**0            -> 2, 1
                      1.5 at 10**0            -> 2, 1

PLANTED FAULTS
--------------
Before the pins are trusted, two broken roundings are run against them,
each must fail named pins, and the real function is run last:

  F1 the fault of 2026-10-31, the carry undone: must fail the belt's
     case and the docstring case, by name.
  F2 half away from zero, the schoolroom rule: must fail 2.5.

Role: devtool
Domain: dev_tools

Module created: October 31, 2026 with Anthropic's Claude Opus 5.5
(L-484, L-503: the rounding fault's regression test,
COORD_L485_orrery_rounding_hold_pins_brief_20261031.md, section 1).
"""

import decimal
import math
import sys

import constants_rows


# (label, value, place, expected value, expected figures), every one
# worked by hand from the rule, as the docstring above shows.
PINS = (
    ("the belt's case", 99781779.76, 6, 100000000.0, 3),
    ("the docstring case", 9.996, -2, 10.0, 4),
    ("a carry at units", 9.6, 0, 10.0, 2),
    ("no carry", 1234.5, 1, 1230.0, 3),
    ("the one-figure branch", 637800.0, 6, 600000.0, 1),
    ("half to even, 2.5", 2.5, 0, 2.0, 1),
    ("half to even, 1.5", 1.5, 0, 2.0, 1),
)


def _carry_undone(value, place):
    """F1: _to_place() as it stood before 2026-10-31, word for word."""
    figures = int(math.floor(math.log10(abs(value)))) - place + 1
    if figures < 1:
        return float("%.*g" % (1, value)), 1
    rounded = float("%.*g" % (figures, value))
    if int(math.floor(math.log10(abs(rounded)))) - place + 1 != figures:
        figures += 1
        rounded = float("%.*g" % (figures, value))
    return rounded, figures


def _half_away(value, place):
    """F2: rounded half away from zero at the place, counted correctly."""
    quantum = decimal.Decimal(1).scaleb(place)
    rounded = float(decimal.Decimal(repr(value)).quantize(
        quantum, rounding=decimal.ROUND_HALF_UP))
    figures = max(1, int(math.floor(math.log10(abs(rounded)))) - place + 1)
    return rounded, figures


FAULTS = (
    ("F1 the carry undone", _carry_undone,
     ("the belt's case", "the docstring case")),
    ("F2 half away from zero", _half_away, ("half to even, 2.5",)),
)


def failing_pins(function):
    """[(label, got, want)] for every pin `function` does not hold."""
    failed = []
    for label, value, place, want_value, want_figures in PINS:
        got = function(value, place)
        if got != (want_value, want_figures):
            failed.append((label, got, (want_value, want_figures)))
    return failed


def main():
    print("Constants rounding: constants_rows._to_place() against %d "
          "pins worked by hand" % len(PINS))
    print("Planted faults (each must fail the pins named):")
    missed = []
    for name, function, must_fail in FAULTS:
        failed = [label for label, _got, _want in failing_pins(function)]
        caught = all(label in failed for label in must_fail)
        print("  %s  %-26s fails: %s" % ("CAUGHT" if caught else "MISSED",
                                         name, ", ".join(failed) or "none"))
        if not caught:
            missed.append(name)
    print("The real function:")
    failed = failing_pins(constants_rows._to_place)
    for label, value, place, want_value, want_figures in PINS:
        bad = [f for f in failed if f[0] == label]
        if bad:
            print("  FAIL  %-22s %r at 10**%d gave %r, the rule gives %r"
                  % (label, value, place, bad[0][1], bad[0][2]))
        else:
            print("  ok    %-22s %r at 10**%d -> %r, %d figure(s)"
                  % (label, value, place, want_value, want_figures))
    print("=" * 70)
    if missed or failed:
        print("CONSTANTS ROUNDING: FAILED -- %s"
              % ", ".join(missed + [f[0] for f in failed]))
        return 1
    print("CONSTANTS ROUNDING: PASS -- %d of %d pins held; %d of %d planted "
          "faults caught by name." % (len(PINS), len(PINS), len(FAULTS),
                                      len(FAULTS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
