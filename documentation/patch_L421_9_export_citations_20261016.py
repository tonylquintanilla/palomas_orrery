#!/usr/bin/env python3
"""
patch_L421_9_export_citations_20261016.py -- L-421 part 3, the orrery
half: the constants export carries each row's citation (schema 7), so
the gallery's mirror can write it beside the number and its check can
compare the words as it already compares the numbers.

Built on orrery 0d7211ea38f1cf869525a6d7230db5fff396507b at
https://github.com/tonylquintanilla/palomas_orrery (gallery
09d92918a78a00fea893740b7e2da109d5b11c25 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read, not
touched). From documentation/HANDOFF_L421_checks_brief_20261016.md,
patch 1 of 3; Tony's decision on its section 4: A, the orrery owns the
citation.
Tony's local folder: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
Written October 16, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L421_9_export_citations_20261016.py

    Save this file in the ORRERY folder above, open it in VS Code and
    click Run. It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing, in two files

    export_constants.py        every exported row gains "source" (its
                               "# Source:" text, continuation lines
                               joined), "source_from" (the rows the text
                               was read from) and "source_inherited". A
                               derived row with no "# Source:" of its
                               own takes its inputs' citations; a typed
                               row with none has none. The twelve
                               lines that read "as <ROW>." are followed
                               to that row's citation, so the website
                               never shows a store name. SCHEMA 6 -> 7.
                               The run's output names the rows that
                               follow a pointer, the rows that inherit,
                               and the rows with none.
    test_constants_export.py   check 2 compares the three new fields;
                               new check 7 works every row's citation
                               out again by the same rule, written
                               separately, holds seven worked cases, and
                               tests a small store written in the file
                               for the shapes no row has yet (a derived
                               input with no source, a pointer to a row
                               with no line).

    Both files must be exactly as committed at the SHA above. Nothing
    the orrery draws or prints changes. data/constants_export.json is
    not written by this patch; the maintenance run writes it.

PERMANENT, AND DISPOSABLE

    The two module changes are permanent. This script is one-shot:
    once it has run, a second run refuses and writes nothing.

WHAT IT PRINTS

    Success: one "ok" line per file, then "patch applied" and what to
    do next. Failure: one ERROR or ANCHOR FAIL line and "NOTHING was
    written."

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Each file: how it is checked, and its edits as (old, new), bottom-up.
# "whole": the file must be exactly the base before, and exactly the
# result after. "anchors": checked only at the lines edited, so notes
# elsewhere are kept; the result is still checked whole when the base
# matched. "new": a file this patch adds.
FILES = [
    {
        'path': 'test_constants_export.py',
        'mode': 'whole',
        'base_md5': 'e860691433ece44b07accefa90637e2f',
        'new_md5': '048ccea3f54cf11bdc61f1aed46faf92',
        'edits': [
            ('    print("Export matches the store: sha256 %s on both sides; %d rows "\n          "re-read, %d not exported, %d tokens; %d conversions "\n          "re-computed, %d of %d worked cases hold."\n          % (facts["hash_store"][:12], facts["rows_examined"],\n             facts["not_exported"], facts["tokens"], facts["conversions"],\n             facts["pins"][0], facts["pins"][1]))\n    return 0\n\n',
             '    print("Export matches the store: sha256 %s on both sides; %d rows "\n          "re-read, %d not exported, %d tokens; %d conversions "\n          "re-computed, %d of %d worked cases hold; %d citations worked "\n          "out again, %d of %d worked cases hold."\n          % (facts["hash_store"][:12], facts["rows_examined"],\n             facts["not_exported"], facts["tokens"], facts["conversions"],\n             facts["pins"][0], facts["pins"][1], facts["citations"],\n             facts["citation_pins"][0], facts["citation_pins"][1]))\n    return 0\n\n'),
            ('                  % (facts["conversions"], facts["pins"][0],\n                     facts["pins"][1]))\n        print("")\n\n',
             '                  % (facts["conversions"], facts["pins"][0],\n                     facts["pins"][1]))\n        if "citations" in facts:\n            print("7. citations worked out again by the inheritance rule: "\n                  "%d; worked cases holding: %d of %d; the written store "\n                  "(a chain, a pointer, a pointer to nothing): %s"\n                  % (facts["citations"], facts["citation_pins"][0],\n                     facts["citation_pins"][1],\n                     "holds" if facts.get("chain") else "FAILS"))\n            print("   rows with no citation, own or inherited (%d)%s"\n                  % (len(facts["uncited"]), ":" if facts["uncited"] else ""))\n            for line in constants_rows.wrap_names(facts["uncited"],\n                                                  indent="     "):\n                print(line)\n        print("")\n\n'),
            ('                       by_name, failures, facts)\n\n    # 5. closed slices\n    closed = constants_rows.CLOSED_SLICES if closed is None else closed\n',
             '                       by_name, failures, facts)\n\n    # 7. citations (schema 7, L-421 part 3)\n    _check_citations(on_disk, by_name, failures, facts)\n\n    # 5. closed slices\n    closed = constants_rows.CLOSED_SLICES if closed is None else closed\n'),
            ('            "transitional", "rows", "not_exported")\nROW_FIELDS = ("value", "unit", "figures", "status", "derived", "read",\n              "inputs", "uncertainty", "prints", "in")\n\n# Check 6\'s worked cases of provenance-discipline 2.22, Rule 3: (row,\n',
             '            "transitional", "rows", "not_exported")\nROW_FIELDS = ("value", "unit", "figures", "status", "derived", "read",\n              "inputs", "uncertainty", "prints", "in", "source",\n              "source_from", "source_inherited")\n\n# Check 7\'s worked cases of the inheritance rule (L-421 part 3): (row,\n# the rows its citation is read from, inherited). Written out here, not\n# computed, so a change to the rule fails by name.\nCITATION_PINS = (\n    # A derived row with its own "# Source:" keeps it.\n    ("HELMET_CUSP_RADII", ("HELMET_CUSP_RADII",), False),\n    # A derived row with none inherits both of its inputs\'.\n    ("CHROMOSPHERE_TOP_KM", ("SUN_RADIUS_KM", "CHROMOSPHERE_PHYSICAL_KM"),\n     True),\n    ("EARTH_GEOSTATIONARY_RADIUS_KM",\n     ("EARTH_GM_KM3_S2", "EARTH_ROTATION_RATE_RAD_S"), True),\n    # A declared input (the solar wind\'s pressure and Bz) contributes\n    # nothing: the standoff inherits the five fitted coefficients only.\n    ("EARTH_MAGNETOPAUSE_STANDOFF_RADII",\n     ("EARTH_MAGNETOPAUSE_SHUE_A1_RADII", "EARTH_MAGNETOPAUSE_SHUE_A2_RADII",\n      "EARTH_MAGNETOPAUSE_SHUE_A5", "EARTH_MAGNETOPAUSE_SHUE_A3_PER_NT",\n      "EARTH_MAGNETOPAUSE_SHUE_A4_NT"), True),\n    # A declared typed row has no citation, and none is invented.\n    ("EARTH_SOLAR_WIND_PRESSURE_NPA", (), False),\n    # "as OORT_CLOUD_OUTER_EDGE_LOW_AU." is followed to that row\'s line.\n    ("OORT_CLOUD_OUTER_EDGE_HIGH_AU", ("OORT_CLOUD_OUTER_EDGE_LOW_AU",),\n     False),\n    # A derived row whose input points: the pointer is followed there too.\n    ("OUTER_OORT_CLOUD_AU", ("OORT_CLOUD_OUTER_EDGE_LOW_AU",), True),\n)\n\n\ndef _citation(name, by_name):\n    """Check 7\'s own working of the inheritance rule.\n\n    Deliberately not export_constants.resolve_source(): a second\n    working of the same rule, so a fault in either shows as a\n    disagreement. The text is read through constants_rows, the one\n    reader of the store\'s comments.\n    """\n    def own(row_name):\n        """(text, rows) of the row\'s own line, a pointer followed."""\n        def line(row):\n            text = by_name[row].field("Source", loose=True)\n            return text.strip() if text and text.strip() else None\n\n        def joined(text, tails):\n            return " ".join([text] + [t for t in reversed(tails) if t])\n\n        path = [row_name]\n        tails = []\n        while True:\n            text = line(path[-1])\n            if text is None:\n                if len(path) == 1:\n                    return None, []\n                # The last pointer names a row with no line: the pointing\n                # row\'s line stands as written.\n                tails.pop()\n                return joined(line(path[-2]), tails), [path[-2]]\n            target = None\n            if text.startswith("as ") and "." in text:\n                head, _dot, after = text[3:].partition(".")\n                if head in by_name and head not in path:\n                    target = head\n            if target is None:\n                return joined(text, tails), [path[-1]]\n            tails.append(after.strip())\n            path.append(target)\n\n    text, rows_read = own(name)\n    if text is not None:\n        return text, rows_read, False\n    if not by_name[name].is_derived:\n        return None, [], False\n    order = []\n    visited = {name: True}\n    stack = list(reversed(by_name[name].inputs))\n    while stack:\n        used = stack.pop()\n        if used in visited or used not in by_name:\n            continue\n        visited[used] = True\n        if own(used)[0] is not None:\n            order.append(used)\n        elif by_name[used].is_derived:\n            stack.extend(reversed(by_name[used].inputs))\n    if not order:\n        return None, [], False\n    texts = []\n    rows_from = []\n    for used in order:\n        text, rows_read = own(used)\n        if text not in texts:\n            texts.append(text)\n        for row_name in rows_read:\n            if row_name not in rows_from:\n                rows_from.append(row_name)\n    return "; ".join(texts), rows_from, True\n\n\n# Check 7\'s chain: a store no live row is shaped like yet. CHAIN_C has\n# no source; its input CHAIN_B is derived with none, so its citation is\n# CHAIN_A\'s, reached two steps down; CHAIN_D is declared and gives\n# nothing; CHAIN_A2 repeats CHAIN_A\'s text, which is kept once. CHAIN_P\n# points at CHAIN_A and adds words; CHAIN_Q points at CHAIN_D, which has\n# no line, so CHAIN_Q\'s own line stands as written.\nCHAIN_STORE = \'\'\'\\\nCHAIN_A = 2.0\n# Source: Fixture citation for A,\n#   continued on an untagged line.\nCHAIN_A2 = 3.0\n# Source: Fixture citation for A,\n# Source+: continued on an untagged line.\nCHAIN_D = 5.0\n# Status: declared 2026-10-16 -- a fixture choice\nCHAIN_B = CHAIN_A * 2\nCHAIN_C = CHAIN_B + CHAIN_D + CHAIN_A2\nCHAIN_P = 7.0\n# Source: as CHAIN_A. The high end.\nCHAIN_Q = 11.0\n# Source: as CHAIN_D. Nowhere to go.\n\'\'\'\n# The order is the row\'s "inputs" as the export lists them, which is\n# Python\'s own walk of the expression: CHAIN_A2, then CHAIN_B\'s CHAIN_A.\nCHAIN_WANTED = (\n    ("CHAIN_C", ("Fixture citation for A, continued on an untagged line.",\n                 ["CHAIN_A2", "CHAIN_A"], True)),\n    ("CHAIN_P", ("Fixture citation for A, continued on an untagged line. "\n                 "The high end.", ["CHAIN_A"], False)),\n    ("CHAIN_Q", ("as CHAIN_D. Nowhere to go.", ["CHAIN_Q"], False)),\n)\n\n\ndef _check_chain(failures, facts):\n    """Check 7\'s chain: the export\'s function on a store written here."""\n    _rows, chain = constants_rows.parse_store_text(CHAIN_STORE)\n    ok = True\n    for name, wanted in CHAIN_WANTED:\n        mine = _citation(name, chain)\n        theirs = export_constants.resolve_source(name, chain)\n        theirs = (theirs[0], list(theirs[1]), theirs[2])\n        if not mine == theirs == wanted:\n            ok = False\n            failures.append(("(chain) " + name, "wanted %r; this file "\n                             "works out %r; export_constants gives %r"\n                             % (wanted, mine, theirs)))\n    facts["chain"] = ok\n\n\ndef _check_citations(on_disk, by_name, failures, facts):\n    """Check 7. Every row\'s citation worked out again by the rule."""\n    _check_chain(failures, facts)\n    examined = 0\n    uncited = []\n    for name, served in on_disk["rows"].items():\n        if name not in by_name:\n            continue\n        examined += 1\n        text, cited_from, inherited = _citation(name, by_name)\n        got = (served.get("source"), served.get("source_from"),\n               served.get("source_inherited"))\n        if got != (text, cited_from, inherited):\n            failures.append((name, "citation served as from %r, inherited "\n                             "%r; by the inheritance rule it is from %r, "\n                             "inherited %r%s"\n                             % (got[1], got[2], cited_from, inherited,\n                                "" if got[0] == text else\n                                " (and the text differs)")))\n        if text is None:\n            uncited.append(name)\n    held = 0\n    for name, cited_from, inherited in CITATION_PINS:\n        served = on_disk["rows"].get(name)\n        if served is None:\n            failures.append((name, "PIN: not exported, so its citation "\n                             "cannot be checked"))\n            continue\n        got = (tuple(served.get("source_from") or ()),\n               served.get("source_inherited"))\n        if got != (cited_from, inherited):\n            failures.append((name, "PIN: the citation should come from %r, "\n                             "inherited %r; it comes from %r, inherited %r"\n                             % (cited_from, inherited, got[0], got[1])))\n            continue\n        held += 1\n    facts["citations"] = examined\n    facts["uncited"] = uncited\n    facts["citation_pins"] = (held, len(CITATION_PINS))\n\n# Check 6\'s worked cases of provenance-discipline 2.22, Rule 3: (row,\n'),
            ('slice only when constants_rows.conversion_problem() passes it, and names\neach one it skipped.)\n"""\n\n',
             'slice only when constants_rows.conversion_problem() passes it, and names\neach one it skipped.)\nModule updated: October 16, 2026 with Anthropic\'s Claude Opus 5.5\n(L-421 part 3: check 2 compares "source", "source_from" and\n"source_inherited", new in schema 7, and check 7 works every row\'s\ncitation out again by the inheritance rule and holds five worked cases.)\n"""\n\n'),
            ('       it is served as its source row\'s "in", which check 6 re-computes.\n       Each one skipped is named in the output.\n\nWHAT MAKES IT FAIL\n\n    Any of the five. Also: the export file is missing, is not JSON, lacks\n    a field, or the generator itself reports a problem with the store.\n\n',
             '       it is served as its source row\'s "in", which check 6 re-computes.\n       Each one skipped is named in the output.\n    7. Every row\'s citation (schema 7, L-421 part 3) is worked out again\n       here by the inheritance rule, written in this file rather than by\n       the export\'s own function, and must equal the served "source",\n       "source_from" and "source_inherited". The rule: a row with its own\n       "# Source:" is cited by it, and a line that opens "as <ROW>." is\n       read as that row\'s citation followed by the words after it; a\n       derived row with none takes each\n       input\'s own citation, or, for a derived input with none, that\n       input\'s inputs\', in the order the row\'s "inputs" lists them, each text\n       once, joined with "; "; a typed row with none has none. Seven worked\n       cases are pinned by the rows they cite, so a change to the rule\n       fails here by name: a derived row with its own source keeps it, a\n       derived row inherits two inputs, a declared input contributes\n       nothing, a declared typed row has none, a pointer is followed, and\n       a derived row inherits through its input\'s pointer. No row in the store\n       today reaches a citation through a derived input that has none,\n       so a small store written in this file has one that does, and the\n       export\'s own function must give the answer worked out here for\n       it; without that case the walk down a chain could break and every\n       live row still pass. The rows with no citation, own or inherited,\n       are named in the output.\n\nWHAT MAKES IT FAIL\n\n    Any of the seven. Also: the export file is missing, is not JSON, lacks\n    a field, or the generator itself reports a problem with the store.\n\n'),
        ],
    },
    {
        'path': 'export_constants.py',
        'mode': 'whole',
        'base_md5': 'daadd17d71ca44af687a693ec831a6cd',
        'new_md5': 'f1422d0db3d6c3b46ee16a5c0040f2ef',
        'edits': [
            ('        print(line)\n    print("")\n    print("Not exported, %d row(s):" % len(skipped))\n    if converted_names:\n',
             '        print(line)\n    print("")\n    own = [n for n in rows if rows[n]["source"] is not None\n           and not rows[n]["source_inherited"]]\n    inherited = [n for n in rows if rows[n]["source_inherited"]]\n    uncited = [n for n in rows if rows[n]["source"] is None]\n    pointed = [n for n in own if rows[n]["source_from"] != [n]]\n    print("Citations (schema 7): %d row(s) cite their own source, %d "\n          "inherit their inputs\', %d have none:"\n          % (len(own), len(inherited), len(uncited)))\n    if pointed:\n        print("  own, read through an \\"as <ROW>.\\" pointer (%d):"\n              % len(pointed))\n        for line in constants_rows.wrap_names(pointed):\n            print(line)\n    if inherited:\n        print("  inherited from their inputs (%d):" % len(inherited))\n        for line in constants_rows.wrap_names(inherited):\n            print(line)\n    if uncited:\n        print("  no citation, own or inherited (%d):" % len(uncited))\n        for line in constants_rows.wrap_names(uncited):\n            print(line)\n    print("")\n    print("Not exported, %d row(s):" % len(skipped))\n    if converted_names:\n'),
            ('            "in": converted,\n        }\n\n    if failures:\n',
             '            "in": converted,\n        }\n        # L-421 part 3 (schema 7): the citation travels with the number.\n        cited, cited_from, inherited = resolve_source(row.name, by_name)\n        exported[row.name]["source"] = cited\n        exported[row.name]["source_from"] = cited_from\n        exported[row.name]["source_inherited"] = inherited\n\n    if failures:\n'),
            ('        return out, None\n    return None, "%s is a %s, not a number" % (where, type(value).__name__)\n\n\n',
             '        return out, None\n    return None, "%s is a %s, not a number" % (where, type(value).__name__)\n\n\nPOINTER_RE = re.compile(r"^as ([A-Z][A-Z0-9_]*)\\.\\s*(.*)$", re.DOTALL)\n\n\ndef own_source(name, by_name, _seen=None):\n    """(text, [rows it was read from]) for a row\'s own citation, or\n    (None, []) (L-421, schema 7).\n\n    Its "# Source:" line, with every line that continues it -- a\n    "# Source+:" line or an untagged "#   ..." line, the two forms the\n    store uses -- joined with single spaces, read through constants_rows\'\n    one reader, the same one every other field uses.\n\n    Twelve rows write their line as a pointer, "as <ROW>." -- the same\n    source as that row. A pointer is read as the named row\'s citation,\n    resolved the same way, with any words after the pointer kept after\n    it ("as HELMET_CUSP_LOW_RADII. This row is the high end."). Printed\n    as written, the website would show a visitor a store name.\n    """\n    text = by_name[name].field("Source", loose=True)\n    if text is None or not text.strip():\n        return None, []\n    text = text.strip()\n    match = POINTER_RE.match(text)\n    if match and match.group(1) in by_name:\n        seen = set([name]) if _seen is None else _seen\n        target = match.group(1)\n        if target in seen:\n            return text, [name]\n        seen.add(target)\n        cited, cited_from = own_source(target, by_name, seen)\n        if cited is None:\n            return text, [name]\n        rest = match.group(2).strip()\n        return (cited + (" " + rest if rest else "")), cited_from\n    return text, [name]\n\n\ndef resolve_source(name, by_name, _seen=None):\n    """(text or None, [rows it was read from], inherited) for one row.\n\n    The inheritance rule (provenance-discipline: a derived row "names its\n    inputs and is never cleared on its own; checking it means checking\n    them"). A row with its own "# Source:" is cited by it (own_source,\n    which follows a pointer). A derived row with none takes, for each\n    input in the order its "inputs" lists them, that input\'s own\n    citation, or -- when that input is derived and has none -- its\n    inputs\', and so on down. Each row is visited once, each text kept\n    once, in the order found, joined with "; ". A typed row with no\n    "# Source:" contributes nothing: it is a declared choice or an\n    uncited value, and no citation is invented for it.\n    test_constants_export.py check 7 works the same rule by its own code.\n    """\n    row = by_name[name]\n    text, cited_from = own_source(name, by_name)\n    if text is not None:\n        return text, cited_from, False\n    if not row.is_derived:\n        return None, [], False\n    seen = set([name]) if _seen is None else _seen\n    found = []\n\n    def walk(row_name):\n        for used in by_name[row_name].inputs:\n            if used in seen or used not in by_name:\n                continue\n            seen.add(used)\n            cited, used_from = own_source(used, by_name)\n            if cited is not None:\n                found.append((used_from, cited))\n            elif by_name[used].is_derived:\n                walk(used)\n\n    walk(name)\n    if not found:\n        return None, [], False\n    texts = []\n    rows_from = []\n    for used_from, cited in found:\n        if cited not in texts:\n            texts.append(cited)\n        for used in used_from:\n            if used not in rows_from:\n                rows_from.append(used)\n    return "; ".join(texts), rows_from, True\n\n\n'),
            ('\nEXPORT_PATH = os.path.join("data", "constants_export.json")\nSCHEMA = 6\n\n\n',
             '\nEXPORT_PATH = os.path.join("data", "constants_export.json")\nSCHEMA = 7\n\n\n'),
            ('import math\nimport os\nimport sys\n\n',
             'import math\nimport os\nimport re\nimport sys\n\n'),
            ('constants_rows.conversion_problem() refuses stops the export. The schema\ndoes not change: the file\'s fields are the same.)\n"""\n\n',
             'constants_rows.conversion_problem() refuses stops the export. The schema\ndoes not change: the file\'s fields are the same.)\nModule updated: October 16, 2026 with Anthropic\'s Claude Opus 5.5\n(L-421 part 3: every exported row also carries its citation, "source",\nwith "source_from" and "source_inherited", a derived row with no\n"# Source:" of its own taking its inputs\'. The gallery\'s mirror writes\nit beside the number, Tony\'s option A of 2026-10-16. SCHEMA moves to 7.)\n"""\n\n'),
            ('                              display prints a unit from here and never\n                              converts a served number itself (L-345)\n    not_exported   every row that is NOT in rows, by name, with the reason\n\n',
             '                              display prints a unit from here and never\n                              converts a served number itself (L-345)\n                     source   the row\'s citation, as text, or null\n                              (schema 7, L-421). A row\'s own citation is\n                              its "# Source:" line with the lines that\n                              continue it, "# Source+:" or an untagged\n                              "#   ..." line, joined with spaces. A line\n                              that opens "as <ROW>." points at another\n                              row\'s citation and is read as that row\'s,\n                              followed by any words after the pointer. A\n                              DERIVED row with no "# Source:" of its own\n                              takes its inputs\' citations: each input\'s\n                              own, or, for a derived input with none, that\n                              input\'s inputs\', walked in the order its\n                              "inputs" lists them, each text once,\n                              joined with "; ". A typed row with no\n                              "# Source:" line -- a declared choice --\n                              has none, and none is invented for it.\n                              The gallery\'s mirror writes this beside the\n                              number, so the website prints the orrery\'s\n                              words (Tony\'s ruling of 2026-10-16,\n                              option A: the orrery owns the citation)\n                     source_from  the rows whose "# Source:" lines the\n                              citation was read from, a list: the row\n                              itself when it carries its own, the row its\n                              line points to, its inputs when it\n                              inherited, empty when it has none (schema 7)\n                     source_inherited  true when the citation came from\n                              the row\'s inputs, false otherwise (schema 7)\n    not_exported   every row that is NOT in rows, by name, with the reason\n\n'),
        ],
    },
]


def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def fail(message):
    print(message)
    print("NOTHING was written. Undo is not needed.")
    return 1


def main():
    planned = []
    notes = []
    for f in FILES:
        rel = f["path"]
        path = os.path.join(HERE, *rel.split("/"))
        if f["mode"] == "new":
            if os.path.exists(path):
                with open(path, "rb") as handle:
                    have = handle.read().decode("utf-8").replace("\r\n", "\n")
                if md5(have) == f["new_md5"]:
                    print("ok  %-58s already present, the same" % rel)
                    continue
                return fail("ERROR: %s already exists and differs from what "
                            "this patch adds." % rel)
            planned.append((rel, path, f["content"]))
            print("ok  %-58s new file" % rel)
            continue
        if not os.path.exists(path):
            return fail("ERROR: %s is not here. Save this patch in the "
                        "repository's root folder." % rel)
        with open(path, "rb") as handle:
            raw = handle.read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            return fail("ERROR: %s is not UTF-8." % rel)
        if "\r\n" in text:
            text = text.replace("\r\n", "\n")
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % rel)
        have = md5(text)
        if have == f["new_md5"]:
            return fail("ERROR: %s already carries this patch's change. "
                        "It has run before." % rel)
        exact = have == f["base_md5"]
        if f["mode"] == "whole" and not exact:
            return fail("ERROR: %s is not the version this patch was "
                        "built on (base moved). Compare it with the "
                        "repository in GitHub Desktop." % rel)
        for n, (old, new) in enumerate(f["edits"], 1):
            count = text.count(old)
            if count != 1:
                first = old.strip().splitlines()[0][:60] if old.strip() else ""
                return fail("ANCHOR FAIL: %s edit %d matched %d times: %r"
                            % (rel, n, count, first))
            text = text.replace(old, new)
        if exact and md5(text) != f["new_md5"]:
            return fail("ERROR: %s edited, but the result is not what this "
                        "patch was built to write." % rel)
        if not exact:
            notes.append("note: %s differed from the base outside the edited "
                         "lines; those lines were kept" % rel)
        planned.append((rel, path, text))
        print("ok  %-58s %d edit(s)" % (rel, len(f["edits"])))

    for rel, path, text in planned:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
    for note in notes:
        print(note)
    print("patch applied (%d file(s) written)" % len(planned))
    print("")
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py. Its Constants export row rewrites')
    print('     data/constants_export.json at schema 7: each row now carries its')
    print('     citation (127 rows: 94 cite their own source, 22 inherit their')
    print("     inputs', 11 have none). The Constants export check prints a new")
    print('     line 7. Expect 31 of 31 gating checkers and the gate path at 0.')
    print('     Module atlas rewrites MODULE_ATLAS.md and MODULE_INDEX.md, because')
    print('     two module descriptions changed.')
    print('  2. Move this script into documentation/; commit; push. Then tell')
    print('     Claude the new orrery SHA: the gallery patch is built on it.')
    return 0


if __name__ == "__main__":
    sys.exit(main())
