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
                     prints   the print count an exact row states, or
                              null (schema 5). A display prints an exact
                              row to that many significant figures,
                              never by a width of its own
                              (provenance-discipline 2.20, Rule 7)
                     in       the row's value in every unit of its
                              dimension -- for a length, km, au,
                              r_earth and r_sun -- each as {value,
                              figures, prints}, or null when the row's
                              unit has no other unit to convert into
                              (schema 6). Computed by
                              constants_rows.conversions() from the
                              row's FULL digits and rounded once, each
                              count from the source row alone
                              (provenance-discipline 2.22, Rule 3). A
                              display prints a unit from here and never
                              converts a served number itself (L-345).
                              A table of numbers (a dict keyed by name,
                              the main belt's distance and height
                              percentiles) carries one such "in" per
                              entry, keyed as its value is, each worked
                              out the same way from that entry's full
                              digits (L-503, L-484, 2026-10-29)
                     source   the row's citation, as text, or null
                              (schema 7, L-421). A row's own citation is
                              its "# Source:" line with the lines that
                              continue it, "# Source+:" or an untagged
                              "#   ..." line, joined with spaces. A line
                              that opens "as <ROW>." points at another
                              row's citation and is read as that row's,
                              followed by any words after the pointer. A
                              DERIVED row with no "# Source:" of its own
                              takes its inputs' citations: each input's
                              own, or, for a derived input with none, that
                              input's inputs', walked in the order its
                              "inputs" lists them, each text once,
                              joined with "; ". A typed row with no
                              "# Source:" line -- a declared choice --
                              has none, and none is invented for it.
                              The gallery's mirror writes this beside the
                              number, so the website prints the orrery's
                              words (Tony's ruling of 2026-10-16,
                              option A: the orrery owns the citation)
                     source_from  the rows whose "# Source:" lines the
                              citation was read from, a list: the row
                              itself when it carries its own, the row its
                              line points to, its inputs when it
                              inherited, empty when it has none (schema 7)
                     source_inherited  true when the citation came from
                              the row's inputs, false otherwise (schema 7)
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

A CONVERSION is not exported either (L-345, patch D20). It is a name the
orrery's drawing code keeps for a row's value in another unit, marked
"# Conversion: of <ROW>" in constants_new.py; its value is served as
that row's "in", so its not_exported reason names the row.

WHAT MAKES IT FAIL (exit 1, and NOTHING is written)
---------------------------------------------------
    - a "# Unit:" token that is neither defined nor retired
    - a "# Unit:" or "# Figures:" line that cannot be read
    - a print count constants_rows.print_count_problem() refuses: larger
      than the digits the number has, too small to write it in full, or
      anything but 1 on a zero
    - a token whose defining_constant is not a row in the store
    - a row marked "# Conversion:" that constants_rows.conversion_problem()
      refuses: it names no row, is not that row scaled only by rows that
      define units, carries a field of its own, or has the wrong value
    - a conversion constants_rows.conversions() cannot make: a dimension
      without exactly one base token, a defining row whose unit is not
      the base, or a value smaller than its own uncertainty in a unit
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
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D15: every exported row also carries "prints",
the print count of an exact row a display prints, and a count
constants_rows.print_count_problem() refuses stops the export. SCHEMA
moves to 5.)
Module updated: September 28, 2026 with Anthropic's Claude Opus 5.5
(L-345, patch L322_D_19: every exported row also carries "in", its
value in every unit of its dimension, computed from full digits by
constants_rows.conversions(). Tony's ruling of 2026-09-28: a value in
another unit is computed, never stored. SCHEMA moves to 6.)
Module updated: September 28, 2026 with Anthropic's Claude Opus 5.5
(L-345, patch L322_D_20: a row marked "# Conversion: of <ROW>" is not
exported; not_exported names the row it is served through, and a marker
constants_rows.conversion_problem() refuses stops the export. The schema
does not change: the file's fields are the same.)
Module updated: October 16, 2026 with Anthropic's Claude Opus 5.5
(L-421 part 3: every exported row also carries its citation, "source",
with "source_from" and "source_inherited", a derived row with no
"# Source:" of its own taking its inputs'. The gallery's mirror writes
it beside the number, Tony's option A of 2026-10-16. SCHEMA moves to 7.)
Module updated: October 29, 2026 with Anthropic's Claude Opus 5.5
(L-503, L-484: a row whose value is a table of numbers carries "in" for
each entry, so the website can print the main belt's distances in
kilometres beside AU, as the orrery does. The schema does not change: a
table's "in" was null and is now filled; the fields are the same.)
"""

import json
import math
import os
import re
import sys

import constants_rows
from constants_tokens import RETIRED_TOKENS, TOKENS

EXPORT_PATH = os.path.join("data", "constants_export.json")
SCHEMA = 7


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


def table_conversions(row, value, values, units_by_name, tokens):
    """(entries, problem) for a row whose value is a table of numbers, a
    dict keyed by name: {key: that entry in every unit of its dimension},
    each made by constants_rows.conversions() exactly as a one-number row's
    "in" is, from the entry's full digits in the store. (None, None) for a
    value that is not such a table, or a unit with nothing to convert into.
    """
    if not isinstance(value, dict) or not value:
        return None, None
    if not all(isinstance(v, (int, float)) and not isinstance(v, bool)
               for v in value.values()):
        return None, None
    out = {}
    for key, entry in value.items():
        converted, problem = constants_rows.conversions(
            row, entry, values, units_by_name, tokens)
        if problem:
            return None, "entry %r: %s" % (key, problem)
        if converted is None:
            return None, None
        out[str(key)] = converted
    return out, None


POINTER_RE = re.compile(r"^as ([A-Z][A-Z0-9_]*)\.\s*(.*)$", re.DOTALL)


def own_source(name, by_name, _seen=None):
    """(text, [rows it was read from]) for a row's own citation, or
    (None, []) (L-421, schema 7).

    Its "# Source:" line, with every line that continues it -- a
    "# Source+:" line or an untagged "#   ..." line, the two forms the
    store uses -- joined with single spaces, read through constants_rows'
    one reader, the same one every other field uses.

    Twelve rows write their line as a pointer, "as <ROW>." -- the same
    source as that row. A pointer is read as the named row's citation,
    resolved the same way, with any words after the pointer kept after
    it ("as HELMET_CUSP_LOW_RADII. This row is the high end."). Printed
    as written, the website would show a visitor a store name.
    """
    text = by_name[name].field("Source", loose=True)
    if text is None or not text.strip():
        return None, []
    text = text.strip()
    match = POINTER_RE.match(text)
    if match and match.group(1) in by_name:
        seen = set([name]) if _seen is None else _seen
        target = match.group(1)
        if target in seen:
            return text, [name]
        seen.add(target)
        cited, cited_from = own_source(target, by_name, seen)
        if cited is None:
            return text, [name]
        rest = match.group(2).strip()
        return (cited + (" " + rest if rest else "")), cited_from
    return text, [name]


def resolve_source(name, by_name, _seen=None):
    """(text or None, [rows it was read from], inherited) for one row.

    The inheritance rule (provenance-discipline: a derived row "names its
    inputs and is never cleared on its own; checking it means checking
    them"). A row with its own "# Source:" is cited by it (own_source,
    which follows a pointer). A derived row with none takes, for each
    input in the order its "inputs" lists them, that input's own
    citation, or -- when that input is derived and has none -- its
    inputs', and so on down. Each row is visited once, each text kept
    once, in the order found, joined with "; ". A typed row with no
    "# Source:" contributes nothing: it is a declared choice or an
    uncited value, and no citation is invented for it.
    test_constants_export.py check 7 works the same rule by its own code.
    """
    row = by_name[name]
    text, cited_from = own_source(name, by_name)
    if text is not None:
        return text, cited_from, False
    if not row.is_derived:
        return None, [], False
    seen = set([name]) if _seen is None else _seen
    found = []

    def walk(row_name):
        for used in by_name[row_name].inputs:
            if used in seen or used not in by_name:
                continue
            seen.add(used)
            cited, used_from = own_source(used, by_name)
            if cited is not None:
                found.append((used_from, cited))
            elif by_name[used].is_derived:
                walk(used)

    walk(name)
    if not found:
        return None, [], False
    texts = []
    rows_from = []
    for used_from, cited in found:
        if cited not in texts:
            texts.append(cited)
        for used in used_from:
            if used not in rows_from:
                rows_from.append(used)
    return "; ".join(texts), rows_from, True


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

    units_by_name = dict((name, row.unit) for name, row in by_name.items())
    exported = {}
    not_exported = {}
    for row in rows:
        if row.unit_error:
            failures.append((row.name, row.unit_error))
            continue
        if row.conversion_of is not None or row.conversion_error:
            # L-345, patch D20: a conversion is served as its source
            # row's "in", never as a row of its own.
            problem = constants_rows.conversion_problem(row, by_name, values,
                                                        tokens)
            if problem:
                failures.append((row.name, "marked as a conversion; it "
                                 + problem))
            else:
                not_exported[row.name] = (
                    "a conversion of %s, served as that row's \"in\""
                    % row.conversion_of)
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
        problem = constants_rows.print_count_problem(
            row, values.get(row.name))
        if problem:
            failures.append((row.name, problem))
            continue
        # L-345: the row in every unit of its dimension, computed here
        # from full digits, never stored as a second row.
        converted, problem = constants_rows.conversions(
            row, values.get(row.name), values, units_by_name, tokens)
        if not problem and converted is None:
            # L-503, L-484: a table (the main belt's distance and height
            # percentiles) carries "in" for each entry, keyed as its value
            # is, each entry converted from the store's full digits as a
            # one-number row is.
            converted, problem = table_conversions(
                row, values.get(row.name), values, units_by_name, tokens)
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
            "prints": row.prints,
            "in": converted,
        }
        # L-421 part 3 (schema 7): the citation travels with the number.
        cited, cited_from, inherited = resolve_source(row.name, by_name)
        exported[row.name]["source"] = cited
        exported[row.name]["source_from"] = cited_from
        exported[row.name]["source_inherited"] = inherited

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
    converted_names = [n for n, why in skipped.items()
                       if why.startswith("a conversion of ")]
    retired = [n for n in skipped
               if n not in no_unit and n not in converted_names]
    counted = {}
    for name in rows:
        figures = rows[name]["figures"]
        key = ("no # Figures: line" if figures is None else
               "exact" if figures == "exact" else "rounded to its figures")
        counted[key] = counted.get(key, 0) + 1

    converted = sum(1 for name in rows if rows[name].get("in"))
    print("Exported %d row(s), %d with their value in every unit of their "
          "dimension (\"in\"):" % (len(rows), converted))
    for key in ("rounded to its figures", "exact", "no # Figures: line"):
        if counted.get(key):
            print("  %-26s %d" % (key, counted[key]))
    for line in constants_rows.wrap_names(list(rows)):
        print(line)
    print("")
    own = [n for n in rows if rows[n]["source"] is not None
           and not rows[n]["source_inherited"]]
    inherited = [n for n in rows if rows[n]["source_inherited"]]
    uncited = [n for n in rows if rows[n]["source"] is None]
    pointed = [n for n in own if rows[n]["source_from"] != [n]]
    print("Citations (schema 7): %d row(s) cite their own source, %d "
          "inherit their inputs', %d have none:"
          % (len(own), len(inherited), len(uncited)))
    if pointed:
        print("  own, read through an \"as <ROW>.\" pointer (%d):"
              % len(pointed))
        for line in constants_rows.wrap_names(pointed):
            print(line)
    if inherited:
        print("  inherited from their inputs (%d):" % len(inherited))
        for line in constants_rows.wrap_names(inherited):
            print(line)
    if uncited:
        print("  no citation, own or inherited (%d):" % len(uncited))
        for line in constants_rows.wrap_names(uncited):
            print(line)
    print("")
    print("Not exported, %d row(s):" % len(skipped))
    if converted_names:
        print("  conversions (%d) -- each served as its source row's \"in\":"
              % len(converted_names))
        for line in constants_rows.wrap_names(converted_names):
            print(line)
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
