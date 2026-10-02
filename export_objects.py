"""
export_objects.py -- write data/objects_export.json from the object list
in celestial_objects.py. The orrery is the one definition of each object;
the gallery reads this file and never reads orrery source.

RUN COMMAND
-----------
Open this file in VS Code and click Run. It takes no arguments.

    python export_objects.py

orrery_maintenance_run.py runs it on every maintenance run, as a
GENERATOR, beside export_constants.py. Running it by hand is the same
thing.

WHICH ENTRIES ARE EXPORTED
--------------------------
Only an entry in OBJECT_DEFINITIONS that carries a 'key' field. The key
is the website's name for the object, spelled exactly as the website's
data/objects_config.json spells its "slug" ('mars', 'pluto_barycenter').
It is never shown to anyone, so renaming a display name cannot break the
link (Tony's ruling, 2026-10-01, L-395). An entry gains a key when the
website starts serving it, and not before.

WHAT IT WRITES
--------------
One JSON file, data/objects_export.json:

    schema          1
    source_sha256   the sha256 of celestial_objects.py, CRLF normalised
                    to LF, so test_objects_export.py can tell whether the
                    list moved after the export was made
    objects         one entry per key, in list order:
                      name         the entry's 'name'
                      horizons_id  the entry's 'id'
                      id_type      the entry's 'id_type', or null where
                                   the entry leaves it blank. A blank is
                                   not a value: the gallery keeps its own
                                   where the list states none
                      description  the entry's 'mission_info', with the
                                   opening "Horizons: ..." sentence
                                   removed when it has one. The website
                                   prints the Horizons id on its own
                                   source line, so the opening is the
                                   orrery's and stays in the orrery
                                   (Tony's ruling, 2026-10-01)
                      info_url     the entry's 'mission_url', or null
    numbers         for each key whose description holds a digit, the
                    numbers it holds, as written. Reported, so that no
                    number reaches the website unseen: a number in a
                    served description is sourced or comes out
                    (provenance-discipline, Fetched vs Recalled)

WHAT MAKES IT FAIL (exit 1, and NOTHING is written)
---------------------------------------------------
    - celestial_objects.py does not parse, or OBJECT_DEFINITIONS is not a
      list of dict literals
    - an entry writes the same field twice (the second silently wins in
      Python, so one of the two is invisible)
    - a key that is not lower-case letters, digits and underscores, or
      two entries with the same key
    - a keyed entry whose name, id, mission_info or mission_url is not a
      plain literal
    - an exported description that still says "Horizons:"

The list is read with Python's own parser (ast), not imported, so the
export never runs the orrery's code and cannot be changed by it.

DETERMINISTIC ON PURPOSE
------------------------
The same list bytes give the same export bytes: no timestamp, no git
SHA (the gallery records the SHA it pulls at, as it does for the
constants export). The file is only written when its content would
change, and always with LF line endings.

Role: devtool
Domain: dev_tools

Module created: October 1, 2026 with Anthropic's Claude Opus 5.5
(L-395, the first build: the Solar System room's eleven bodies take
their names, Horizons ids, descriptions and NASA links from the orrery).
"""

import ast
import hashlib
import json
import os
import re
import sys

SOURCE = "celestial_objects.py"
TARGET = os.path.join("data", "objects_export.json")
SCHEMA = 1
KEY_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
OPENING = re.compile(r"^Horizons:[^.]*\.\s*")
NUMBER = re.compile(r"\d[\d,.]*\d|\d")
FIELDS = ("name", "id", "id_type", "mission_info", "mission_url")


class ExportError(Exception):
    pass


def source_sha256(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def definitions(text):
    """The OBJECT_DEFINITIONS list node. Raises ExportError."""
    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        raise ExportError("%s does not parse: %s" % (SOURCE, exc))
    for node in tree.body:
        if (isinstance(node, ast.Assign)
                and any(getattr(t, "id", None) == "OBJECT_DEFINITIONS"
                        for t in node.targets)):
            if not isinstance(node.value, ast.List):
                raise ExportError("OBJECT_DEFINITIONS is not a list literal")
            return node.value
    raise ExportError("OBJECT_DEFINITIONS was not found in %s" % SOURCE)


def entry_label(entry):
    for k, v in zip(entry.keys, entry.values):
        if isinstance(k, ast.Constant) and k.value == "name":
            if isinstance(v, ast.Constant):
                return str(v.value)
    return "the entry at line %d" % entry.lineno


def repeated_fields(list_node):
    """[(entry label, field, [line numbers])] for every field written twice."""
    found = []
    for entry in list_node.elts:
        if not isinstance(entry, ast.Dict):
            raise ExportError("an item at line %d of OBJECT_DEFINITIONS is "
                              "not a dict literal" % entry.lineno)
        seen = {}
        for k in entry.keys:
            if isinstance(k, ast.Constant) and isinstance(k.value, str):
                seen.setdefault(k.value, []).append(k.lineno)
        for field, lines in seen.items():
            if len(lines) > 1:
                found.append((entry_label(entry), field, lines))
    return found


def literal_fields(entry):
    """{field: value} for the fields the export reads, as literals."""
    out = {}
    for k, v in zip(entry.keys, entry.values):
        if isinstance(k, ast.Constant) and k.value in FIELDS + ("key",):
            try:
                out[k.value] = ast.literal_eval(v)
            except ValueError:
                raise ExportError("%s: '%s' is not a plain literal"
                                  % (entry_label(entry), k.value))
    return out


def description_of(mission_info):
    text = (mission_info or "").strip()
    return OPENING.sub("", text, count=1).strip()


def build_export(text):
    """The export dict for the list's source text. Raises ExportError."""
    list_node = definitions(text)
    repeats = repeated_fields(list_node)
    if repeats:
        raise ExportError("; ".join(
            "%s writes '%s' %d times (lines %s)"
            % (label, field, len(lines), ", ".join(map(str, lines)))
            for label, field, lines in repeats))
    objects = {}
    numbers = {}
    for entry in list_node.elts:
        f = literal_fields(entry)
        if "key" not in f:
            continue
        key = f["key"]
        if not isinstance(key, str) or not KEY_PATTERN.match(key):
            raise ExportError("%s: key %r is not lower-case letters, digits "
                              "and underscores" % (f.get("name"), key))
        if key in objects:
            raise ExportError("key '%s' is on two entries (%s and %s)"
                              % (key, objects[key]["name"], f.get("name")))
        description = description_of(f.get("mission_info"))
        if "Horizons:" in description:
            raise ExportError("%s: its description still says 'Horizons:' "
                              "after the opening is removed" % key)
        objects[key] = {
            "name": f.get("name"),
            "horizons_id": None if f.get("id") is None else str(f["id"]),
            "id_type": f.get("id_type"),
            "description": description or None,
            "info_url": f.get("mission_url"),
        }
        found = NUMBER.findall(description)
        if found:
            numbers[key] = found
    return {
        "schema": SCHEMA,
        "source_sha256": source_sha256(text.encode("utf-8")),
        "objects": objects,
        "numbers": numbers,
    }


def render(export):
    return json.dumps(export, indent=2, ensure_ascii=True,
                      sort_keys=False) + "\n"


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root, SOURCE), "rb") as handle:
        raw = handle.read()
    try:
        export = build_export(raw.decode("utf-8").replace("\r\n", "\n"))
    except ExportError as exc:
        print("FAIL: %s. NOTHING was written." % exc)
        return 1
    target = os.path.join(root, TARGET)
    content = render(export)
    old = None
    if os.path.exists(target):
        with open(target, "r", encoding="utf-8", newline="") as handle:
            old = handle.read()
    keys = list(export["objects"])
    if old == content:
        print("Objects export unchanged: %d keyed entries (%s)."
              % (len(keys), ", ".join(keys)))
    else:
        with open(target, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
        print("Objects export written to %s: %d keyed entries (%s)."
              % (TARGET.replace(os.sep, "/"), len(keys), ", ".join(keys)))
    if export["numbers"]:
        print("Numbers in exported descriptions, each to be sourced or "
              "removed: %s." % "; ".join(
                  "%s: %s" % (k, ", ".join(v))
                  for k, v in export["numbers"].items()))
    else:
        print("Numbers in exported descriptions: none.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
