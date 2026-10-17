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
       unit, figures, status, derived, read, inputs, uncertainty and
       prints, for every row.
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
    6. Every conversion the export serves as "in" (schema 6, L-345) is
       re-computed here from the store's full digits, by arithmetic
       written in this file rather than by the export's own function,
       and must equal the served value at its served count. A row whose
       unit has another unit of its dimension must carry "in", and one
       whose unit has none must not. Six worked cases of the count rule
       (provenance-discipline 2.22, Rule 3) are pinned by value and
       count, so a change to the rule fails here by name: the
       chromosphere's top, the bow shock and magnetopause standoffs, the
       LEO floor's print count, one Earth radius in Earth radii, and the
       tops of the lower and upper atmosphere in Earth radii.
    5. The per-slice gate (Tony's ruling of 2026-09-14): a row inside a
       CLOSED slice must be exported and carry a status and a figure
       count. Outside a closed slice a missing field is a named gap, not a
       failure. constants_rows.CLOSED_SLICES is empty until the Earth walk
       finishes, and the output says so. A CONVERSION (L-345, patch D20)
       is the one kind of row the gate skips, and only when
       constants_rows.conversion_problem() finds nothing wrong with it:
       it is served as its source row's "in", which check 6 re-computes.
       Each one skipped is named in the output.
    7. Every row's citation (schema 7, L-421 part 3) is worked out again
       here by the inheritance rule, written in this file rather than by
       the export's own function, and must equal the served "source",
       "source_from" and "source_inherited". The rule: a row with its own
       "# Source:" is cited by it, and a line that opens "as <ROW>." is
       read as that row's citation followed by the words after it; a
       derived row with none takes each
       input's own citation, or, for a derived input with none, that
       input's inputs', in the order the row's "inputs" lists them, each text
       once, joined with "; "; a typed row with none has none. Seven worked
       cases are pinned by the rows they cite, so a change to the rule
       fails here by name: a derived row with its own source keeps it, a
       derived row inherits two inputs, a declared input contributes
       nothing, a declared typed row has none, a pointer is followed, and
       a derived row inherits through its input's pointer. No row in the store
       today reaches a citation through a derived input that has none,
       so a small store written in this file has one that does, and the
       export's own function must give the answer worked out here for
       it; without that case the walk down a chain could break and every
       live row still pass. The rows with no citation, own or inherited,
       are named in the output.

WHAT MAKES IT FAIL

    Any of the seven. Also: the export file is missing, is not JSON, lacks
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
Module updated: September 27, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D15: check 2 compares "prints", new in schema 5,
and "uncertainty", which the export has served since schema 4 and this
check did not compare until now.)
Module updated: September 28, 2026 with Anthropic's Claude Opus 5.5
(L-345, patch L322_D_19: check 2 compares "in", new in schema 6, and
check 6 re-computes every served conversion and holds five worked cases
of the count rule.)
Module updated: September 28, 2026 with Anthropic's Claude Opus 5.5
(L-345, patch L322_D_19a: two more pins, the tops of the lower and
upper atmosphere in Earth radii, 1.0078 at five figures and 1.094 at
four -- the numbers the gallery's two radius lines will print.)
Module updated: September 28, 2026 with Anthropic's Claude Opus 5.5
(L-345, patch L322_D_20: check 5 skips a conversion inside a closed
slice only when constants_rows.conversion_problem() passes it, and names
each one it skipped.)
Module updated: October 16, 2026 with Anthropic's Claude Opus 5.5
(L-421 part 3: check 2 compares "source", "source_from" and
"source_inherited", new in schema 7, and check 7 works every row's
citation out again by the inheritance rule and holds five worked cases.)
Module updated: October 17, 2026 with Anthropic's Claude Opus 5.5
(L-330 round 1 and L-452: the low-orbit altitude's worked case is ESA's
measured 180 km at two figures, where it was an exact 200; the
geostationary ring's citation pin becomes the case of a derived row with
its own pointing Source, and the low-orbit outer edge takes its place as
a derived row inheriting both inputs'.)
"""

import json
import os
import sys

import constants_rows
import export_constants

REQUIRED = ("schema", "store", "store_sha256", "tokens", "closed_slices",
            "transitional", "rows", "not_exported")
ROW_FIELDS = ("value", "unit", "figures", "status", "derived", "read",
              "inputs", "uncertainty", "prints", "in", "source",
              "source_from", "source_inherited")

# Check 7's worked cases of the inheritance rule (L-421 part 3): (row,
# the rows its citation is read from, inherited). Written out here, not
# computed, so a change to the rule fails by name.
CITATION_PINS = (
    # A derived row with its own "# Source:" keeps it.
    ("HELMET_CUSP_RADII", ("HELMET_CUSP_RADII",), False),
    # A derived row with none inherits both of its inputs'.
    ("CHROMOSPHERE_TOP_KM", ("SUN_RADIUS_KM", "CHROMOSPHERE_PHYSICAL_KM"),
     True),
    # (EARTH_GEOSTATIONARY_RADIUS_KM was this pin until 2026-10-17, when
    # it took its own Source to keep the NASA page a visitor reads, L-452.)
    ("EARTH_LEO_OUTER_KM",
     ("EARTH_EQUATORIAL_RADIUS_KM", "EARTH_LEO_UPPER_ALTITUDE_KM"), True),
    # A derived row's own Source may point: it keeps the pointed row's
    # citation and the words after it.
    ("EARTH_GEOSTATIONARY_RADIUS_KM", ("EARTH_GM_KM3_S2",), False),
    # A declared input (the solar wind's pressure and Bz) contributes
    # nothing: the standoff inherits the five fitted coefficients only.
    ("EARTH_MAGNETOPAUSE_STANDOFF_RADII",
     ("EARTH_MAGNETOPAUSE_SHUE_A1_RADII", "EARTH_MAGNETOPAUSE_SHUE_A2_RADII",
      "EARTH_MAGNETOPAUSE_SHUE_A5", "EARTH_MAGNETOPAUSE_SHUE_A3_PER_NT",
      "EARTH_MAGNETOPAUSE_SHUE_A4_NT"), True),
    # A declared typed row has no citation, and none is invented.
    ("EARTH_SOLAR_WIND_PRESSURE_NPA", (), False),
    # "as OORT_CLOUD_OUTER_EDGE_LOW_AU." is followed to that row's line.
    ("OORT_CLOUD_OUTER_EDGE_HIGH_AU", ("OORT_CLOUD_OUTER_EDGE_LOW_AU",),
     False),
    # A derived row whose input points: the pointer is followed there too.
    ("OUTER_OORT_CLOUD_AU", ("OORT_CLOUD_OUTER_EDGE_LOW_AU",), True),
)


def _citation(name, by_name):
    """Check 7's own working of the inheritance rule.

    Deliberately not export_constants.resolve_source(): a second
    working of the same rule, so a fault in either shows as a
    disagreement. The text is read through constants_rows, the one
    reader of the store's comments.
    """
    def own(row_name):
        """(text, rows) of the row's own line, a pointer followed."""
        def line(row):
            text = by_name[row].field("Source", loose=True)
            return text.strip() if text and text.strip() else None

        def joined(text, tails):
            return " ".join([text] + [t for t in reversed(tails) if t])

        path = [row_name]
        tails = []
        while True:
            text = line(path[-1])
            if text is None:
                if len(path) == 1:
                    return None, []
                # The last pointer names a row with no line: the pointing
                # row's line stands as written.
                tails.pop()
                return joined(line(path[-2]), tails), [path[-2]]
            target = None
            if text.startswith("as ") and "." in text:
                head, _dot, after = text[3:].partition(".")
                if head in by_name and head not in path:
                    target = head
            if target is None:
                return joined(text, tails), [path[-1]]
            tails.append(after.strip())
            path.append(target)

    text, rows_read = own(name)
    if text is not None:
        return text, rows_read, False
    if not by_name[name].is_derived:
        return None, [], False
    order = []
    visited = {name: True}
    stack = list(reversed(by_name[name].inputs))
    while stack:
        used = stack.pop()
        if used in visited or used not in by_name:
            continue
        visited[used] = True
        if own(used)[0] is not None:
            order.append(used)
        elif by_name[used].is_derived:
            stack.extend(reversed(by_name[used].inputs))
    if not order:
        return None, [], False
    texts = []
    rows_from = []
    for used in order:
        text, rows_read = own(used)
        if text not in texts:
            texts.append(text)
        for row_name in rows_read:
            if row_name not in rows_from:
                rows_from.append(row_name)
    return "; ".join(texts), rows_from, True


# Check 7's chain: a store no live row is shaped like yet. CHAIN_C has
# no source; its input CHAIN_B is derived with none, so its citation is
# CHAIN_A's, reached two steps down; CHAIN_D is declared and gives
# nothing; CHAIN_A2 repeats CHAIN_A's text, which is kept once. CHAIN_P
# points at CHAIN_A and adds words; CHAIN_Q points at CHAIN_D, which has
# no line, so CHAIN_Q's own line stands as written.
CHAIN_STORE = '''\
CHAIN_A = 2.0
# Source: Fixture citation for A,
#   continued on an untagged line.
CHAIN_A2 = 3.0
# Source: Fixture citation for A,
# Source+: continued on an untagged line.
CHAIN_D = 5.0
# Status: declared 2026-10-16 -- a fixture choice
CHAIN_B = CHAIN_A * 2
CHAIN_C = CHAIN_B + CHAIN_D + CHAIN_A2
CHAIN_P = 7.0
# Source: as CHAIN_A. The high end.
CHAIN_Q = 11.0
# Source: as CHAIN_D. Nowhere to go.
'''
# The order is the row's "inputs" as the export lists them, which is
# Python's own walk of the expression: CHAIN_A2, then CHAIN_B's CHAIN_A.
CHAIN_WANTED = (
    ("CHAIN_C", ("Fixture citation for A, continued on an untagged line.",
                 ["CHAIN_A2", "CHAIN_A"], True)),
    ("CHAIN_P", ("Fixture citation for A, continued on an untagged line. "
                 "The high end.", ["CHAIN_A"], False)),
    ("CHAIN_Q", ("as CHAIN_D. Nowhere to go.", ["CHAIN_Q"], False)),
)


def _check_chain(failures, facts):
    """Check 7's chain: the export's function on a store written here."""
    _rows, chain = constants_rows.parse_store_text(CHAIN_STORE)
    ok = True
    for name, wanted in CHAIN_WANTED:
        mine = _citation(name, chain)
        theirs = export_constants.resolve_source(name, chain)
        theirs = (theirs[0], list(theirs[1]), theirs[2])
        if not mine == theirs == wanted:
            ok = False
            failures.append(("(chain) " + name, "wanted %r; this file "
                             "works out %r; export_constants gives %r"
                             % (wanted, mine, theirs)))
    facts["chain"] = ok


def _check_citations(on_disk, by_name, failures, facts):
    """Check 7. Every row's citation worked out again by the rule."""
    _check_chain(failures, facts)
    examined = 0
    uncited = []
    for name, served in on_disk["rows"].items():
        if name not in by_name:
            continue
        examined += 1
        text, cited_from, inherited = _citation(name, by_name)
        got = (served.get("source"), served.get("source_from"),
               served.get("source_inherited"))
        if got != (text, cited_from, inherited):
            failures.append((name, "citation served as from %r, inherited "
                             "%r; by the inheritance rule it is from %r, "
                             "inherited %r%s"
                             % (got[1], got[2], cited_from, inherited,
                                "" if got[0] == text else
                                " (and the text differs)")))
        if text is None:
            uncited.append(name)
    held = 0
    for name, cited_from, inherited in CITATION_PINS:
        served = on_disk["rows"].get(name)
        if served is None:
            failures.append((name, "PIN: not exported, so its citation "
                             "cannot be checked"))
            continue
        got = (tuple(served.get("source_from") or ()),
               served.get("source_inherited"))
        if got != (cited_from, inherited):
            failures.append((name, "PIN: the citation should come from %r, "
                             "inherited %r; it comes from %r, inherited %r"
                             % (cited_from, inherited, got[0], got[1])))
            continue
        held += 1
    facts["citations"] = examined
    facts["uncited"] = uncited
    facts["citation_pins"] = (held, len(CITATION_PINS))

# Check 6's worked cases of provenance-discipline 2.22, Rule 3: (row,
# unit, value served, figures served, prints served). Written out here,
# not computed, so a change to the rule fails by name.
CONVERSION_PINS = (
    ("CHROMOSPHERE_TOP_KM", "r_sun", 1.003, 4, None),
    ("CHROMOSPHERE_TOP_KM", "au", 0.00466, 3, None),
    ("EARTH_BOW_SHOCK_STANDOFF_RADII", "km", 86000.0, 2, None),
    ("EARTH_BOW_SHOCK_STANDOFF_RADII", "au", 0.00058, 2, None),
    ("EARTH_MAGNETOPAUSE_STANDOFF_RADII", "km", 65000.0, 2, None),
    ("EARTH_MAGNETOPAUSE_STANDOFF_RADII", "au", 0.00044, 2, None),
    # ESA's 180 km since 2026-10-17 (L-330 round 1); it was a declared,
    # exact 200 km floor printing 3.
    ("EARTH_LEO_LOWER_ALTITUDE_KM", "r_earth", 0.028, 2, None),
    ("EARTH_EQUATORIAL_RADIUS_KM", "r_earth", 1.0, "exact", 1),
    # L-345, patch D19a: a sum good to the kilometre, and one good to
    # tens of kilometres, each in Earth radii.
    ("EARTH_STRATOPAUSE_RADIUS_KM", "r_earth", 1.0078, 5, None),
    ("EARTH_THERMOPAUSE_RADIUS_KM", "r_earth", 1.094, 4, None),
)


def _check_conversions(on_disk, values, by_name, failures, facts):
    """Check 6. Every served conversion re-computed from full digits."""
    tokens = on_disk["tokens"]
    size = {}
    for token, spec in tokens.items():
        defining = spec.get("defining_constant")
        size[token] = 1.0 if defining is None else float(values[defining])
    recomputed = 0
    for name, served in on_disk["rows"].items():
        unit = served.get("unit")
        spec = tokens.get(unit, {})
        same = [t for t, s in tokens.items()
                if s.get("dimension") == spec.get("dimension")
                and (t == s.get("dimension")
                     or s.get("defining_constant") is not None)]
        if unit not in same:
            same = []
        entries = served.get("in")
        full = values.get(name)
        one_number = (isinstance(full, (int, float))
                      and not isinstance(full, bool))
        if len(same) < 2 or not one_number:
            if entries is not None:
                failures.append((name, "serves \"in\" but its unit %r has "
                                 "no other unit to convert into" % unit))
            continue
        if not isinstance(entries, dict) or sorted(entries) != sorted(same):
            failures.append((name, "\"in\" should hold %s; it holds %r"
                             % (", ".join(sorted(same)),
                                sorted(entries) if isinstance(entries, dict)
                                else entries)))
            continue
        for token, entry in entries.items():
            recomputed += 1
            if token == unit:
                expect = (served["value"], served["figures"],
                          served["prints"])
                got = (entry.get("value"), entry.get("figures"),
                       entry.get("prints"))
                if got != expect:
                    failures.append((name, "\"in\" %s is %r; the row "
                                     "itself is %r" % (token, got, expect)))
                continue
            if tokens[token].get("defining_constant") == name:
                if (entry.get("value"), entry.get("figures"),
                        entry.get("prints")) != (1.0, "exact", 1):
                    failures.append((name, "defines %s, so in %s it is 1, "
                                     "exact, printing 1; served %r"
                                     % (token, token, entry)))
                continue
            want = float(full) * size[unit] / size[token]
            figures = entry.get("figures")
            if isinstance(figures, int):
                want = float("%.*g" % (figures, want))
                ok = entry.get("value") == want
            else:
                got = entry.get("value")
                ok = (isinstance(got, float) and
                      abs(got - want) <= 1e-12 * max(abs(want), 1e-300))
            if not ok:
                failures.append((name, "\"in\" %s is %r; re-computed from "
                                 "full digits it is %r" % (token,
                                                           entry.get("value"),
                                                           want)))
    held = 0
    for name, token, value, figures, prints in CONVERSION_PINS:
        entry = ((on_disk["rows"].get(name) or {}).get("in") or {}).get(token)
        if entry is None:
            failures.append((name, "PIN: no \"in\" %s served" % token))
            continue
        got = (entry.get("value") if value is not None else None,
               entry.get("figures"), entry.get("prints"))
        if got != (value, figures, prints):
            failures.append((name, "PIN: %s should serve value %r, figures "
                             "%r, prints %r; it serves %r"
                             % (token, value, figures, prints, entry)))
            continue
        held += 1
    facts["conversions"] = recomputed
    facts["pins"] = (held, len(CONVERSION_PINS))


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

    # 6. conversions (schema 6, L-345)
    _check_conversions(on_disk, constants_rows.load_values(project_dir),
                       by_name, failures, facts)

    # 7. citations (schema 7, L-421 part 3)
    _check_citations(on_disk, by_name, failures, facts)

    # 5. closed slices
    closed = constants_rows.CLOSED_SLICES if closed is None else closed
    facts["closed"] = closed
    gated = 0
    skipped = []
    from constants_tokens import TOKENS
    values = constants_rows.load_values(project_dir)
    for row in rows:
        if not constants_rows.in_closed_slice(row.name, closed):
            continue
        if row.conversion_of is not None or row.conversion_error:
            problem = constants_rows.conversion_problem(row, by_name, values,
                                                        TOKENS)
            if problem:
                failures.append((row.name, "GATE: in closed slice %s, "
                                 "marked as a conversion; it %s"
                                 % (row.slice, problem)))
            else:
                skipped.append(row.name)
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
    facts["conversions_skipped"] = skipped
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
            skipped = facts.get("conversions_skipped") or []
            print("   conversions skipped, each checked and served as its "
                  "source row's \"in\" (%d)%s"
                  % (len(skipped), ":" if skipped else ""))
            for line in constants_rows.wrap_names(skipped, indent="     "):
                print(line)
        else:
            print("5. closed slices: none yet, so no row is gated; the "
                  "gaps are named by export_constants.py")
        if "conversions" in facts:
            print("6. conversions re-computed from full digits: %d; worked "
                  "cases of the count rule holding: %d of %d"
                  % (facts["conversions"], facts["pins"][0],
                     facts["pins"][1]))
        if "citations" in facts:
            print("7. citations worked out again by the inheritance rule: "
                  "%d; worked cases holding: %d of %d; the written store "
                  "(a chain, a pointer, a pointer to nothing): %s"
                  % (facts["citations"], facts["citation_pins"][0],
                     facts["citation_pins"][1],
                     "holds" if facts.get("chain") else "FAILS"))
            print("   rows with no citation, own or inherited (%d)%s"
                  % (len(facts["uncited"]), ":" if facts["uncited"] else ""))
            for line in constants_rows.wrap_names(facts["uncited"],
                                                  indent="     "):
                print(line)
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
          "re-read, %d not exported, %d tokens; %d conversions "
          "re-computed, %d of %d worked cases hold; %d citations worked "
          "out again, %d of %d worked cases hold."
          % (facts["hash_store"][:12], facts["rows_examined"],
             facts["not_exported"], facts["tokens"], facts["conversions"],
             facts["pins"][0], facts["pins"][1], facts["citations"],
             facts["citation_pins"][0], facts["citation_pins"][1]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
