"""
test_objects_export.py -- data/objects_export.json says what the object
list in celestial_objects.py holds, and no entry in the list writes a
field twice.

WHY THIS EXISTS
    The gallery takes each served object's name, Horizons id,
    description and NASA link from data/objects_export.json (L-395). If
    the list moves and the export does not, the website serves the old
    words under a green run. And a Python dict literal that writes a
    field twice keeps only the second, silently: Tony found and removed
    such repeats by hand in September 2026, and nothing stopped the next
    one.

RUN COMMAND
    python test_objects_export.py

    Open it in VS Code and click Run. orrery_maintenance_run.py runs it
    among the checkers.

WHAT IT CHECKS
    1. Every entry in OBJECT_DEFINITIONS, all of them and not only the
       keyed ones, writes each field once.
    2. The export exists, was made from the list as it is now (its
       source_sha256), and equals what export_objects.py would write
       today, entry by entry.
    3. Each exported description is free of the "Horizons:" opening.
    It prints how many entries it scanned, the keys it compared, and
    every number in an exported description by key, so a pass names
    what it looked at.

    4. Every keyed entry carries a horizons_name, JPL's exact name, which
       the gallery's Horizons check compares (L-395); the run prints
       each one beside its key.
    Before any of that it shows that checks 1, 2 and 4 can fail: it
    feeds a list with a repeated field, an export with one changed word,
    and a keyed entry with no horizons_name, and each must be refused.
    If any is not, the run fails.

WHAT MAKES IT FAIL
    - a field written twice in any entry
    - the export is missing, is not JSON, or is stale
    - any exported entry differs from what the list gives now
    - a keyed entry has no horizons_name
    - the self-test did not produce the refusals it must

Role: devtool
Domain: dev_tools

Module created: October 1, 2026 with Anthropic's Claude Opus 5.5
(L-395, the first build).
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-395,
the Horizons check: a keyed entry without a horizons_name fails, shown
failing on a planted entry first).
"""

import json
import os
import sys

import export_objects as ex


SELF_TEST_LIST = (
    "OBJECT_DEFINITIONS = [\n"
    "    {'name': 'Mars', 'key': 'mars', 'id': '499', 'horizons_name': 'Mars',\n"
    "     'mission_info': 'Horizons: 499. Red.', 'id': '4'},\n"
    "]\n")


def self_test():
    """[problems] -- each refusal this check depends on, shown to happen."""
    problems = []
    try:
        ex.build_export(SELF_TEST_LIST)
        problems.append("a list writing 'id' twice was not refused")
    except ex.ExportError as exc:
        if "'id' 2 times" not in str(exc):
            problems.append("the repeated field was refused for the wrong "
                            "reason: %s" % exc)
    good = SELF_TEST_LIST.replace(", 'id': '4'}", "}")
    export = ex.build_export(good)
    if export["objects"]["mars"]["description"] != "Red.":
        problems.append("the 'Horizons:' opening was not removed")
    altered = json.loads(json.dumps(export))
    altered["objects"]["mars"]["description"] = "Blue."
    if not differences(altered, export):
        problems.append("a changed description was not noticed")
    nameless = good.replace(" 'horizons_name': 'Mars',", "")
    try:
        ex.build_export(nameless)
        problems.append("a keyed entry with no horizons_name was not "
                        "refused")
    except ex.ExportError as exc:
        if "no horizons_name" not in str(exc):
            problems.append("the entry with no horizons_name was refused "
                            "for the wrong reason: %s" % exc)
    return problems


def differences(held, fresh):
    """[text] naming every way the held export differs from a fresh one."""
    out = []
    if held.get("schema") != fresh["schema"]:
        out.append("schema %r, expected %r" % (held.get("schema"),
                                                fresh["schema"]))
    if held.get("source_sha256") != fresh["source_sha256"]:
        out.append("made from an older %s (run export_objects.py)"
                   % ex.SOURCE)
    held_objects = held.get("objects") or {}
    for key in fresh["objects"]:
        if key not in held_objects:
            out.append("%s: missing from the export" % key)
            continue
        for field, value in fresh["objects"][key].items():
            if held_objects[key].get(field) != value:
                out.append("%s.%s: export has %r, the list gives %r"
                           % (key, field, held_objects[key].get(field),
                              value))
    for key in held_objects:
        if key not in fresh["objects"]:
            out.append("%s: in the export but no entry has that key" % key)
    if held.get("numbers") != fresh["numbers"]:
        out.append("the numbers list differs from the descriptions")
    return out


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    failures = self_test()
    if failures:
        print("SELF-TEST FAILED -- the checks below could not fail, so a "
              "pass would mean nothing:")
        for f in failures:
            print("  - " + f)
        return 1

    with open(os.path.join(root, ex.SOURCE), "rb") as handle:
        text = handle.read().decode("utf-8").replace("\r\n", "\n")
    list_node = ex.definitions(text)
    scanned = len(list_node.elts)
    repeats = ex.repeated_fields(list_node)
    for label, field, lines in repeats:
        failures.append("%s writes '%s' %d times (lines %s)"
                        % (label, field, len(lines),
                           ", ".join(map(str, lines))))
    fresh = None
    if not repeats:
        try:
            fresh = ex.build_export(text)
        except ex.ExportError as exc:
            failures.append(str(exc))

    target = os.path.join(root, ex.TARGET)
    held = None
    if not os.path.exists(target):
        failures.append("%s is missing (run export_objects.py)"
                        % ex.TARGET.replace(os.sep, "/"))
    else:
        try:
            with open(target, "r", encoding="utf-8") as handle:
                held = json.load(handle)
        except ValueError as exc:
            failures.append("%s is not JSON: %s" % (ex.TARGET, exc))
    if held is not None and fresh is not None:
        failures.extend(differences(held, fresh))

    print("Self-test: a repeated field, a changed word and a keyed entry "
          "with no horizons_name were each refused.")
    print("Scanned %d entries in OBJECT_DEFINITIONS for repeated fields: "
          "%d found." % (scanned, len(repeats)))
    if fresh is not None:
        keys = list(fresh["objects"])
        print("Compared %d keyed entries with the export: %s."
              % (len(keys), ", ".join(keys)))
        print("JPL names (horizons_name): %s." % "; ".join(
            "%s = %s" % (k, fresh["objects"][k]["horizons_name"])
            for k in keys))
        if fresh["numbers"]:
            print("Numbers in exported descriptions: %s." % "; ".join(
                "%s: %s" % (k, ", ".join(v))
                for k, v in fresh["numbers"].items()))
        else:
            print("Numbers in exported descriptions: none.")
    if failures:
        print("FAILURES (%d):" % len(failures))
        for f in failures:
            print("  - " + f)
        print("OBJECTS EXPORT: FAIL")
        return 1
    print("OBJECTS EXPORT: pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
