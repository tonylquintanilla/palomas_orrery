"""
test_constants_export.py -- data/constants_export.json says what
constants_new.py holds.

WHY THIS EXISTS

    The round trip from the store to the gallery is two hops. The gallery
    serves what the orrery published, and the orrery published what the
    store holds. This checker is the second hop, the orrery's own (L-322,
    the framing correction from the Fable review of 2026-09-11). The
    maintenance runner regenerates the export before it runs this, but a
    push without a run, or a run whose generator failed, can leave a
    stale export with nothing else saying so.

RUN COMMAND

    python export_constants.py         (writes the export)
    python test_constants_export.py    (checks it)

    Open either in VS Code and click Run. orrery_maintenance_run.py runs
    both, the generator first.

WHAT IT CHECKS, each printing what it compared

    1. The export's store_sha256 equals the sha256 of constants_new.py on
       disk, CRLF normalised to LF. Both hashes are printed.
    2. Re-reading the store now gives the same rows as the file: value,
       unit, figures, status, derived, read and inputs, for every row.
       The count examined is printed and every disagreement is named. An
       export made before schema 3 lacks read and inputs, so it fails
       here by name on every row rather than passing as current.
    3. not_exported names exactly the rows that are not exported, no more
       and no fewer, with the same reasons. Every row in the store is in
       exactly one of the two lists.
    4. Every token's defining_constant is a row in the store. Whether that
       row is itself exported yet is printed beside it. The export's
       closed_slices and transitional lists equal the store's own, so the
       gallery cannot read a stale copy of either.
    5. The per-slice gate (Tony's ruling of 2026-09-14): a row inside a
       CLOSED slice must be exported and carry a status and a figure
       count. Outside a closed slice a missing field is a named gap, not a
       failure. constants_rows.CLOSED_SLICES is empty until the Earth walk
       finishes, and the output says so.

WHAT MAKES IT FAIL

    Any of the five. Also: the export file is missing, is not JSON, lacks
    a field, or the generator itself reports a problem with the store.

WHAT A GREEN RUN PROVES

    Its last line names the hash it compared on both sides and the number
    of rows it re-read. A check that did not run cannot print that line.

Role: devtool
Domain: dev_tools

Module created: September 16, 2026 with Anthropic's Claude Opus 5
(L-322, the mechanism: piece 3 of the build manifest).
Module updated: September 17, 2026 with Anthropic's Claude Opus 5
(L-322, the gallery half: piece 0. Check 4 also compares the export's
closed_slices and transitional against constants_rows.py.)
Module updated: September 22, 2026 with Anthropic's Claude Opus 5
(L-322 Stage C2: check 2 compares "read" and "inputs" too.)
"""

import json
import os
import sys

import constants_rows
import export_constants

REQUIRED = ("schema", "store", "store_sha256", "tokens", "closed_slices",
            "transitional", "rows", "not_exported")
ROW_FIELDS = ("value", "unit", "figures", "status", "derived", "read",
              "inputs")


def check(project_dir, closed=None):
    """Return (failures, facts). Each failure is (name, message)."""
    failures = []
    facts = {}
    target = os.path.join(project_dir, export_constants.EXPORT_PATH)

    if not os.path.exists(target):
        return [("(export)", "%s does not exist -- run export_constants.py"
                 % export_constants.EXPORT_PATH)], facts
    try:
        with open(target, "r", encoding="utf-8") as handle:
            on_disk = json.load(handle)
    except ValueError as exc:
        return [("(export)", "not valid JSON: %s" % exc)], facts
    missing = [key for key in REQUIRED if key not in on_disk]
    if missing:
        return [("(export)", "missing field(s): %s" % ", ".join(missing))], \
            facts

    fresh, problems = export_constants.build_export(project_dir)
    if problems:
        for name, message in problems:
            failures.append((name, "the generator cannot export the store: "
                             + message))
        return failures, facts

    # 1. hash
    facts["hash_disk"] = on_disk["store_sha256"]
    facts["hash_store"] = fresh["store_sha256"]
    if on_disk["store_sha256"] != fresh["store_sha256"]:
        failures.append(("(export)",
                         "stale: exported from store %s, the store on disk "
                         "is %s -- run export_constants.py"
                         % (on_disk["store_sha256"][:12],
                            fresh["store_sha256"][:12])))

    # 2. rows
    disk_rows = on_disk["rows"]
    new_rows = fresh["rows"]
    facts["rows_examined"] = len(set(disk_rows) | set(new_rows))
    for name in new_rows:
        if name not in disk_rows:
            failures.append((name, "exported from the store now, absent "
                             "from the file"))
            continue
        for field in ROW_FIELDS:
            if disk_rows[name].get(field) != new_rows[name][field]:
                failures.append((name, "%s is %r in the file, %r in the "
                                 "store" % (field, disk_rows[name].get(field),
                                            new_rows[name][field])))
    for name in disk_rows:
        if name not in new_rows:
            failures.append((name, "in the file's rows, not exported from "
                             "the store now"))

    # 3. not_exported
    disk_skip = on_disk["not_exported"]
    new_skip = fresh["not_exported"]
    facts["not_exported"] = len(new_skip)
    for name, why in new_skip.items():
        if disk_skip.get(name) != why:
            failures.append((name, "not_exported reason is %r in the file, "
                             "%r in the store" % (disk_skip.get(name), why)))
    for name in disk_skip:
        if name not in new_skip:
            failures.append((name, "listed as not exported in the file, "
                             "but the store exports it or lacks it"))
    _text, rows, by_name = constants_rows.read_store(project_dir)
    facts["store_rows"] = len(rows)
    for row in rows:
        placed = (row.name in disk_rows) + (row.name in disk_skip)
        if placed != 1:
            failures.append((row.name, "appears in %d of the file's two "
                             "lists; it should be in exactly one" % placed))
    for name in list(disk_rows) + list(disk_skip):
        if name not in by_name:
            failures.append((name, "named in the file, not a row in %s"
                             % constants_rows.STORE))

    # 4. defining constants and the two lists the gallery reads
    for field, actual in (("closed_slices", constants_rows.CLOSED_SLICES),
                          ("transitional", constants_rows.TRANSITIONAL)):
        if list(on_disk.get(field, [])) != list(actual):
            failures.append((field, "the export says %r; constants_rows.py "
                             "says %r" % (on_disk.get(field), list(actual))))
    facts["lists"] = (list(constants_rows.CLOSED_SLICES),
                      list(constants_rows.TRANSITIONAL))
    defining = []
    if on_disk["tokens"] != fresh["tokens"]:
        failures.append(("(tokens)", "the file's token table differs from "
                         "constants_tokens.py"))
    for token, spec in sorted(fresh["tokens"].items()):
        name = spec.get("defining_constant")
        if name is None:
            continue
        if name not in by_name:
            failures.append((token, "defining_constant %s is not a row"
                             % name))
            continue
        defining.append((token, name, name in new_rows))
    facts["defining"] = defining

    # 5. closed slices
    closed = constants_rows.CLOSED_SLICES if closed is None else closed
    facts["closed"] = closed
    gated = 0
    for row in rows:
        if not constants_rows.in_closed_slice(row.name, closed):
            continue
        gated += 1
        if row.name not in new_rows:
            failures.append((row.name, "GATE: in closed slice %s and not "
                             "exported (%s)"
                             % (row.slice, new_skip.get(row.name))))
        if row.status is None:
            failures.append((row.name, "GATE: in closed slice %s with no "
                             "# Status: line" % row.slice))
        if row.figures is None:
            failures.append((row.name, "GATE: in closed slice %s with no "
                             "# Figures: line" % row.slice))
    facts["gated"] = gated
    facts["tokens"] = len(fresh["tokens"])
    return failures, facts


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    failures, facts = check(project_dir)

    print("=" * 70)
    print("  CONSTANTS EXPORT CHECK -- %s against %s"
          % (export_constants.EXPORT_PATH.replace(os.sep, "/"),
             constants_rows.STORE))
    print("=" * 70)
    print("")
    if "hash_disk" in facts:
        print("1. store sha256 in the export  %s" % facts["hash_disk"])
        print("   store sha256 on disk now     %s" % facts["hash_store"])
        print("2. rows re-read from the store and compared: %d"
              % facts["rows_examined"])
        print("3. rows not exported: %d; store rows placed: %d"
              % (facts["not_exported"], facts["store_rows"]))
        print("4. closed slices %r; transitional %r"
              % (facts["lists"][0], facts["lists"][1]))
        print("   defining constants:")
        for token, name, exported in facts["defining"]:
            print("     %-8s %-28s %s" % (token, name,
                                         "exported" if exported else
                                         "a row, not exported yet"))
        if facts["closed"]:
            print("5. closed slices: %s; %d row(s) gated"
                  % (", ".join(facts["closed"]), facts["gated"]))
        else:
            print("5. closed slices: none yet, so no row is gated; the "
                  "gaps are named by export_constants.py")
        print("")

    if failures:
        print("FAILURES (%d):" % len(failures))
        for name, message in failures:
            print("  %-40s %s" % (name, message))
        print("")
        gate = [f for f in failures if f[1].startswith("GATE:")]
        other = len(failures) - len(gate)
        parts = []
        if other:
            parts.append("%d where the export does not match %s"
                         % (other, constants_rows.STORE))
        if gate:
            parts.append("%d unfinished field(s) on rows in a closed slice"
                         % len(gate))
        print("%d problem(s): %s." % (len(failures), "; ".join(parts)))
        return 1

    print("Export matches the store: sha256 %s on both sides; %d rows "
          "re-read, %d not exported, %d tokens."
          % (facts["hash_store"][:12], facts["rows_examined"],
             facts["not_exported"], facts["tokens"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
