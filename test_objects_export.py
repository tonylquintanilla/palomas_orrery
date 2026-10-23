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
       the Horizons check compares (L-395); the run prints each one
       beside its key.
    5. (L-431, build 3) Each exported period is the one its inputs give
       today -- the orbit cache's period record, or the typed table --
       field by field, as check 2 compares every field; a fetched period
       names its centre; a period around the barycentre carries the
       Sun-centred elements of the same date, or says why it could not;
       and each object's confirmation matches
       data/horizons_confirmations.json, date for date. The run prints
       each period with its kind, centre and figure counts.
    Before any of that it shows that checks 1, 2, 4 and 5 can fail: it
    feeds a list with a repeated field, an export with one changed word,
    a keyed entry with no horizons_name, a period record with no centre,
    an export whose period differs from its record, a barycentre period
    exported without its Sun-centred set, and an export whose
    confirmation date differs from the record. Each must be refused. If
    any is not, the run fails.

WHAT MAKES IT FAIL
    - a field written twice in any entry
    - the export is missing, is not JSON, or is stale
    - any exported entry differs from what the list, the orbit cache, the
      typed table and the confirmations record give now
    - a keyed entry has no horizons_name
    - a fetched period with no centre, or a barycentre period with no
      Sun-centred set and no reason
    - a fetched period that names no target, the id it was asked of
      (L-445)
    - the self-test did not produce the refusals it must

Role: devtool
Domain: dev_tools

Module created: October 1, 2026 with Anthropic's Claude Opus 5.5
(L-395, the first build).
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-395,
the Horizons check: a keyed entry without a horizons_name fails, shown
failing on a planted entry first).
Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5 (L-431,
build 3, with L-395's move: the export's periods and confirmations are
compared with the orbit cache, the typed table and the confirmations
record; a period with no centre, a barycentre period with no Sun-centred
set and a confirmation date that differs are refused, each shown failing
on a planted fault first.)
Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5 (L-445,
Earth's period: a fetched period must name its target, the id it was
asked of; a record naming none, and an exported block naming none, are
each refused, shown failing on a planted fault first.)
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


SELF_TEST_RECORD = {
    "days": 1206.32, "open_orbit": False, "center": "@sun",
    "epoch": "2026-10-13 08:30", "fetched": "2026-10-13",
    "error_days": 0.15, "error_from": "year_change",
    "sbdb_status": "SBDB sigma",
    "elements": {"a": 2.2, "e": 0.85, "i": 11.3, "omega": 187.3,
                 "Omega": 334.0, "TP": 2461446.7, "MA": 324.2,
                 "TA": 215.4, "epoch": "2026-10-13 08:30 osc."},
}


def period_problems(export):
    """[text] for every exported period that cannot be printed or drawn
    honestly, whatever its inputs say: a fetched period with no centre,
    or a barycentre period with neither its Sun-centred set nor a
    reason (L-431, build 3)."""
    out = []
    for key, obj in (export.get("objects") or {}).items():
        period = obj.get("period")
        if not isinstance(period, dict) or period.get("kind") != "fetched":
            continue
        if not period.get("center"):
            out.append("%s: a fetched period with no centre" % key)
            continue
        if not period.get("target"):
            # L-445: whose period it is (Earth's is the Earth-Moon
            # barycentre's) must be named, or the check cannot ask it.
            out.append("%s: a fetched period that names no target" % key)
            continue
        record = period.get("record") or {}
        if str(period["center"]).lower() not in ("@sun", "@10", "sun", "10"):
            if record.get("paired") is True:
                if not isinstance(record.get("sun_elements"), dict):
                    out.append("%s: a period around %s marked paired, "
                               "with no Sun-centred elements" %
                               (key, period["center"]))
            elif not record.get("not_paired"):
                out.append("%s: a period around %s exported without its "
                           "Sun-centred elements, and no reason" %
                           (key, period["center"]))
    return out


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

    # L-443: an entry with a helio_id is served by it, as a small body.
    helio = good.replace(" 'horizons_name': 'Mars',",
                         " 'horizons_name': 'Mars', 'helio_id': 'A123 BC',")
    served = ex.build_export(helio)["objects"]["mars"]
    if (served["horizons_id"], served["id_type"]) != ("A123 BC", "smallbody"):
        problems.append("an entry with a helio_id was not served by it, as a "
                        "small body: %r" % ((served["horizons_id"],
                                             served["id_type"]),))
    if (export["objects"]["mars"]["horizons_id"] != "499"):
        problems.append("an entry with no helio_id was not served by its id")

    # L-431, build 3: the periods.
    cache = {"Mars": {"period": dict(SELF_TEST_RECORD),
                      "elements": dict(SELF_TEST_RECORD["elements"]),
                      "metadata": {"center_body": "@sun",
                                   "horizons_id": "499"}}}
    confirmations = {"objects": {"mars": {
        "confirmed": "2026-10-10", "horizons_id": "499", "id_type": None,
        "horizons_name": "Mars"}}}
    try:
        with_period = ex.build_export(good, cache, {}, confirmations, b"x")
    except ex.ExportError as exc:
        problems.append("a good period record was refused: %s" % exc)
        return problems
    centreless = json.loads(json.dumps(cache))
    del centreless["Mars"]["period"]["center"]
    try:
        ex.build_export(good, centreless, {}, confirmations, b"x")
        problems.append("a period record with no centre was not refused")
    except ex.ExportError as exc:
        if "names no centre" not in str(exc):
            problems.append("the record with no centre was refused for the "
                            "wrong reason: %s" % exc)
    # L-445: a record with no target, and no horizons_id to say what its
    # period was asked of, is refused; an exported block naming no target
    # is caught.
    if with_period["objects"]["mars"]["period"].get("target") != "499":
        problems.append("a pre-L-445 record's period was not named as "
                        "asked of its elements fetch's id")
    targetless = json.loads(json.dumps(cache))
    del targetless["Mars"]["metadata"]["horizons_id"]
    try:
        ex.build_export(good, targetless, {}, confirmations, b"x")
        problems.append("a period record naming no target was not refused")
    except ex.ExportError as exc:
        if "names no target" not in str(exc):
            problems.append("the record naming no target was refused for "
                            "the wrong reason: %s" % exc)
    untargeted = json.loads(json.dumps(with_period))
    untargeted["objects"]["mars"]["period"].pop("target")
    if not any("names no target" in d for d in period_problems(untargeted)):
        problems.append("an exported period naming no target was not "
                        "refused")
    moved = json.loads(json.dumps(with_period))
    moved["objects"]["mars"]["period"]["record"]["days"] = 1206.33
    if not any("mars.period" in d for d in differences(moved, with_period)):
        problems.append("an exported period that differs from its record "
                        "was not noticed")
    printed = json.loads(json.dumps(with_period))
    printed["objects"]["mars"]["period"]["days"]["figures"] = 9
    if not any("mars.period" in d for d in differences(printed, with_period)):
        problems.append("a period printed to more figures than its record "
                        "earns was not noticed")
    bary = json.loads(json.dumps(with_period))
    bary["objects"]["mars"]["period"]["center"] = "@0"
    bary["objects"]["mars"]["period"]["record"].pop("sun_elements", None)
    bary["objects"]["mars"]["period"]["record"].pop("not_paired", None)
    bary["objects"]["mars"]["period"]["record"]["paired"] = None
    if not period_problems(bary):
        problems.append("a barycentre period exported without its "
                        "Sun-centred set was not refused")
    bare = json.loads(json.dumps(with_period))
    bare["objects"]["mars"]["period"]["center"] = None
    if not period_problems(bare):
        problems.append("an exported period with no centre was not "
                        "refused")
    redated = json.loads(json.dumps(with_period))
    redated["objects"]["mars"]["confirmation"]["identity"]["confirmed"] = (
        "2026-10-11")
    if not any("mars.confirmation" in d
               for d in differences(redated, with_period)):
        problems.append("a confirmation date that differs from the record "
                        "was not noticed")
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
    for field, what in (("period_inputs_sha256",
                         "the orbit cache's period records or the typed "
                         "periods"),
                        ("confirmations_sha256", ex.CONFIRMATIONS),
                        ("cadence_days", "the check's cadence")):
        if held.get(field) != fresh.get(field):
            out.append("made from older %s (run export_objects.py)" % what)
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
            cache, typed, confirmations, conf_raw = ex.load_inputs(root)
            fresh = ex.build_export(text, cache, typed, confirmations,
                                    conf_raw)
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
    if held is not None:
        failures.extend(period_problems(held))

    print("Self-test: a repeated field, a changed word, a keyed entry with "
          "no horizons_name, a period record with no centre, a period record "
          "naming no target, a period that differs from its record, a "
          "period printed to more figures, a barycentre period with no "
          "Sun-centred set, an exported period with no centre, one naming "
          "no target and a changed confirmation date were each refused.")
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
        print("Periods compared with their inputs (L-431):")
        for k in keys:
            print("  " + ex.period_summary(k, fresh["objects"][k]["period"]))
        confirmed = [k for k in keys
                     if fresh["objects"][k]["confirmation"]["identity"]]
        print("Confirmations compared with %s: %d of %d entries carry one."
              % (ex.CONFIRMATIONS.replace(os.sep, "/"), len(confirmed),
                 len(keys)))
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
