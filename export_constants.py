"""
export_constants.py -- write data/constants_export.json from
constants_new.py. The orrery is the producer of its numbers; the gallery
reads this file and never reads orrery source.

RUN COMMAND
-----------
Open this file in VS Code and click Run. It takes no arguments.

    python export_constants.py

orrery_maintenance_run.py runs it on every maintenance run, as a
GENERATOR, so the export cannot fall behind the store without a checker
saying so (L-322 ruling 7). Running it by hand is the same thing.

WHAT IT WRITES
--------------
One JSON file, data/constants_export.json:

    store_sha256   the sha256 of constants_new.py, CRLF normalised to LF,
                   so test_constants_export.py can tell whether the store
                   moved after the export was made
    tokens         constants_tokens.TOKENS, verbatim: what each unit
                   token means
    closed_slices  the slices whose walk is finished, from
                   constants_rows.CLOSED_SLICES. The gallery's pointer
                   join needs them to know when a row that is not
                   exported is a failure rather than a named gap, and
                   the store's own list is the only honest source
    transitional   the rows stored as rounded literals until the
                   gallery stops parsing the store, from
                   constants_rows.TRANSITIONAL
    rows           one entry per exported row, in store order:
                     value    the number, rounded to its declared figures
                     unit     the token from the row's "# Unit:" line
                     figures  the count from "# Figures:", "exact", or
                              null when the row has no such line yet
                     status   the "# Status:" text, or null
                     derived  true when the row is computed from others
                     read     the row's "# Read:" lines, a list, empty
                              when the row has none (schema 3)
                     inputs   the store rows its expression uses, a list,
                              empty for a typed number (schema 3). The
                              gallery's read check walks these, so a
                              drawn row's measured sources are examined
                              through every derived row between them
                     uncertainty  the stated uncertainty from the
                              "# Figures:" line's field, as the text the
                              row writes ("10", "0.13"), or null when the
                              row states none (schema 4). A display prints
                              it beside the value, as written
    not_exported   every row that is NOT in rows, by name, with the reason

ROUNDING HAPPENS HERE, AND ONLY HERE
------------------------------------
The store holds full precision; the export is the reporting step
(provenance-discipline 2.13, Rule 6). A row declaring "# Figures: 5" is
exported at five significant figures, rounded half to even with
float("%.*g" % (5, x)) (Rule 5). A row declaring "exact" is exported
unrounded. A row with no "# Figures:" line yet is exported unrounded
with "figures": null, so a consumer can tell a declared count from a
missing one. Nothing in constants_new.py is changed.

WHAT IS NOT EXPORTED, AND WHY IT IS NAMED
-----------------------------------------
A row with no "# Unit:" line is not exported: the gallery cannot join to
a row that has not been migrated, and a number with no unit is not
served. It goes in not_exported with its reason. So does a row whose
token is RETIRED (today, "dimensionless"; see constants_tokens.py). The
list shrinks as each body's slice is walked.

WHAT MAKES IT FAIL (exit 1, and NOTHING is written)
---------------------------------------------------
    - a "# Unit:" token that is neither defined nor retired
    - a "# Unit:" or "# Figures:" line that cannot be read
    - a token whose defining_constant is not a row in the store
    - an exported value that is not a number, a list or dict of
      numbers, or null
    - constants_new.py does not parse or does not run

DETERMINISTIC ON PURPOSE
------------------------
The same store bytes give the same export bytes. There is no timestamp
and no git SHA inside the file. A file cannot name the commit that
contains it, and in the normal loop the export is made while the working
copy has uncommitted edits, so a recorded HEAD would name the wrong
commit every time. A timestamp would rewrite the file on every run and
put a diff in every commit. The content anchor is store_sha256; the
commit anchor is recorded by the gallery when it pulls this file at a
SHA it names. (Build manifest correction, recorded: the manifest's
sketch carried "generated" and "orrery_sha" fields.)

The file is only written when its content would change, and always
with LF line endings.

Role: devtool
Domain: dev_tools

Module created: September 16, 2026 with Anthropic's Claude Opus 5
(L-322, the mechanism: piece 2 of the build manifest, the sixth
generator).
Module updated: September 17, 2026 with Anthropic's Claude Opus 5
(L-322, the gallery half: piece 0 of
documentation/BUILD_MANIFEST_L322_gallery_half_20260917.md. The export
carries closed_slices and transitional, so the gallery reads both from
the store rather than keeping its own copy. SCHEMA moves to 2.)
Module updated: September 22, 2026 with Anthropic's Claude Opus 5
(L-322 Stage C2: every exported row also carries "read" and "inputs",
which the gallery's read check needs. SCHEMA moves to 3.)
Module updated: September 25, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D8: every exported row also carries
"uncertainty", so the gallery can print Earth's magnetotail rows with
their stated uncertainties as the orrery does. SCHEMA moves to 4.)
"""

import json
import math
import os
import sys

import constants_rows
from constants_tokens import RETIRED_TOKENS, TOKENS

EXPORT_PATH = os.path.join("data", "constants_export.json")
SCHEMA = 4


def round_to(value, figures):
    """Rule 5: round half to even to `figures` significant figures."""
    return float("%.*g" % (figures, value))


def _export_value(value, figures, where):
    """(exportable value, problem or None)."""
    if value is None:
        return None, None
    if isinstance(value, bool):
        return None, "%s is a boolean, not a number" % where
    if isinstance(value, (int, float)):
        number = float(value)
        if math.isnan(number) or math.isinf(number):
            return None, "%s is not a finite number" % where
        if isinstance(figures, int):
            return round_to(number, figures), None
        return number, None
    if isinstance(value, (list, tuple)):
        out = []
        for index, item in enumerate(value):
            got, problem = _export_value(item, figures,
                                         "%s[%d]" % (where, index))
            if problem:
                return None, problem
            out.append(got)
        return out, None
    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            got, problem = _export_value(item, figures,
                                         "%s[%r]" % (where, key))
            if problem:
                return None, problem
            out[str(key)] = got
        return out, None
    return None, "%s is a %s, not a number" % (where, type(value).__name__)


def build_export(project_dir, tokens=None, retired=None):
    """Build the export in memory.

    Returns (export, failures). `export` is None when there are failures.
    test_constants_export.py calls this too, to re-read the store and
    compare against the file on disk.
    """
    tokens = TOKENS if tokens is None else tokens
    retired = RETIRED_TOKENS if retired is None else retired
    failures = []

    path = constants_rows.store_path(project_dir)
    if not os.path.exists(path):
        return None, [("(store)", "%s not found beside this script"
                       % constants_rows.STORE)]
    try:
        _text, rows, by_name = constants_rows.read_store(project_dir)
    except SyntaxError as exc:
        return None, [("(store)", "%s does not parse: %s"
                       % (constants_rows.STORE, exc))]
    try:
        values = constants_rows.load_values(project_dir)
    except Exception as exc:                          # noqa: BLE001
        return None, [("(store)", "%s does not run: %s"
                       % (constants_rows.STORE, exc))]

    for token, spec in tokens.items():
        defining = spec.get("defining_constant")
        if defining is not None and defining not in by_name:
            failures.append((token, "defining_constant %s is not a row in %s"
                             % (defining, constants_rows.STORE)))

    exported = {}
    not_exported = {}
    for row in rows:
        if row.unit_error:
            failures.append((row.name, row.unit_error))
            continue
        if row.figures_error:
            failures.append((row.name, row.figures_error))
            continue
        if row.unit is None:
            not_exported[row.name] = "no # Unit: line"
            continue
        if row.unit in retired:
            not_exported[row.name] = ("unit token '%s' is retired: %s"
                                      % (row.unit,
                                         retired[row.unit]["reason"]))
            continue
        if row.unit not in tokens:
            failures.append((row.name,
                             "unit token '%s' is not defined in "
                             "constants_tokens.py -- add it there"
                             % row.unit))
            continue
        value, problem = _export_value(values.get(row.name), row.figures,
                                       row.name)
        if problem:
            failures.append((row.name, problem))
            continue
        exported[row.name] = {
            "value": value,
            "unit": row.unit,
            "figures": row.figures,
            "status": row.status,
            "derived": row.is_derived,
            "read": list(row.read_text),
            "inputs": list(row.inputs),
            "uncertainty": row.uncertainty,
        }

    if failures:
        return None, failures

    export = {
        "about": ("Generated by export_constants.py from constants_new.py "
                  "in the palomas_orrery repository. Do not edit by hand; "
                  "the next maintenance run rewrites it."),
        "schema": SCHEMA,
        "store": constants_rows.STORE,
        "store_sha256": constants_rows.store_sha256(path),
        "store_hash_basis": ("sha256 of constants_new.py with CRLF line "
                             "endings normalised to LF"),
        "rounding": ("value is rounded half to even to the row's figures; "
                     "figures 'exact' or null means the value is not "
                     "rounded, and null means the row has not declared a "
                     "count yet"),
        "tokens": tokens,
        "closed_slices": list(constants_rows.CLOSED_SLICES),
        "transitional": list(constants_rows.TRANSITIONAL),
        "rows": exported,
        "not_exported": not_exported,
    }
    return export, []


def render(export):
    """The exact text written to disk."""
    return json.dumps(export, indent=2, ensure_ascii=True,
                      allow_nan=False) + "\n"


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    export, failures = build_export(project_dir)

    print("=" * 70)
    print("  CONSTANTS EXPORT -- %s -> %s"
          % (constants_rows.STORE, EXPORT_PATH.replace(os.sep, "/")))
    print("=" * 70)
    print("")

    if failures:
        print("FAILURES (%d) -- nothing was written:" % len(failures))
        for name, message in failures:
            print("  %-40s %s" % (name, message))
        print("")
        print("Export NOT written: %d problem(s) in %s or "
              "constants_tokens.py." % (len(failures), constants_rows.STORE))
        return 1

    try:
        text = render(export)
    except ValueError as exc:
        print("Export NOT written: a value could not be written as "
              "JSON (%s)." % exc)
        return 1

    target = os.path.join(project_dir, EXPORT_PATH)
    old = None
    if os.path.exists(target):
        with open(target, "rb") as handle:
            old = handle.read().replace(b"\r\n", b"\n").decode("utf-8")
    if old == text:
        action = "unchanged, not written"
    else:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        action = "written" if old is not None else "created"

    rows = export["rows"]
    skipped = export["not_exported"]
    no_unit = [n for n, why in skipped.items() if why == "no # Unit: line"]
    retired = [n for n in skipped if n not in no_unit]
    counted = {}
    for name in rows:
        figures = rows[name]["figures"]
        key = ("no # Figures: line" if figures is None else
               "exact" if figures == "exact" else "rounded to its figures")
        counted[key] = counted.get(key, 0) + 1

    print("Exported %d row(s):" % len(rows))
    for key in ("rounded to its figures", "exact", "no # Figures: line"):
        if counted.get(key):
            print("  %-26s %d" % (key, counted[key]))
    for line in constants_rows.wrap_names(list(rows)):
        print(line)
    print("")
    print("Not exported, %d row(s):" % len(skipped))
    if retired:
        print("  retired unit token (%d) -- replaced at the slice visit:"
              % len(retired))
        for line in constants_rows.wrap_names(retired):
            print(line)
    if no_unit:
        by_slice = {}
        for name in no_unit:
            by_slice.setdefault(constants_rows.slice_of(name), []).append(
                name)
        print("  no # Unit: line (%d), by slice:" % len(no_unit))
        for key in sorted(by_slice):
            print("    %s (%d)" % (key, len(by_slice[key])))
            for line in constants_rows.wrap_names(by_slice[key],
                                                  indent="        "):
                print(line)
    print("")
    print("Store sha256 %s; %d token(s) carried."
          % (export["store_sha256"], len(export["tokens"])))
    print("Export %s: %d of %d rows exported, %d not exported."
          % (action, len(rows), len(rows) + len(skipped), len(skipped)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
