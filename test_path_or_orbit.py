"""
test_path_or_orbit.py -- the rule that draws a small body as a path or an
orbit by its orbit solution's e in JPL's Small-Body Database
(path_or_orbit.py, L-510), on made-up records, with no network; and the
guard that the retired 'open_path' does not come back to the object list.
Each check is first run against a planted fault and must catch it.

WHAT IT CHECKS, AND THE FAULT PLANTED FOR EACH

    1. The rule, on one body each side of 1, one at exactly 1, one with no
       record and one whose record was asked of another search: e
       1.00005 and 1.0 are paths, 0.99999 an orbit; the last two raise
       NoSolution naming the body. Planted: the comparison turned the
       wrong way (< 1 for a path); and 'above 1' in place of 'at or
       above' (> for >=).
    2. The drawn type: a small body typed 'orbital' with e at or above 1
       is drawn as 'trajectory', one typed 'trajectory' below 1 as
       'orbital'; a spacecraft and a moon keep their typed object_type.
       Planted: the typed field let decide again.
    3. The side check: McNaught's database e (1.000018815882278) against
       its Sun-centred elements of 2026-11-04 (e 0.999939778) is a named
       failure; elements on the same side are none. Planted: the side
       check that never fails.
    4. The 30-day cycle: no record, a record 30 days old and one asked of
       another search are due; one 29 days old is not.
    5. Reading JPL's answer: an orbit gives the record; several matches is
       a reached answer with no record; an exception is not reached.
    6. The guard (the shape of test_path_plan.py check 19): no entry of
       the real celestial_objects.py carries 'open_path'. The entries
       examined are counted, and any that carries it is named. Planted:
       'open_path' put back on West.
    7. The store: every keyed small body in the real list has a database
       e in data/small_body_solutions.json, asked as the list asks it
       now, so the export can decide each one. The bodies are counted and
       any without one is named.
    8. The plot's second link (L-512, part 1): a body with no record is
       decided by the e of its typed elements (0.99994 an orbit), and the
       console names it and orbital_elements.py; a body with a record is
       decided by the store even when its typed e disagrees, and prints
       nothing; a record asked of another search still fails by name; with
       no typed e either, the plot's call returns None and prints FAILED;
       the export's call (no fallback) still refuses. Planted: the typed e
       put on the wrong side of 1 (1.00006) must change the answer; the
       lookup turned off must fail by name; the typed e read before the
       store must be caught.
    9. The real plot list: every small body the plot sends through the
       rule is decided by one link or the other, and those the second
       link decides are named (6AC4721 on 2026-11-04).

RUN COMMAND

    python test_path_or_orbit.py

    Open it in VS Code and click Run. orrery_maintenance_run.py runs it
    among the checkers, as "Path or orbit suite", and it gates. It writes
    nothing. Its last line starts "PATH OR ORBIT SUITE:".

Role: devtool
Domain: dev_tools

Module created: November 4, 2026 with Anthropic's Claude Opus 5.5
(L-510, part 1: a small body drawn by its eccentricity).
Module updated: November 4, 2026, afternoon, with Anthropic's Claude Opus
5.5 (L-512, part 1: checks 8 and 9, the plot's second link, the typed
elements' e, with its planted faults.)
"""

import ast
import contextlib
import datetime
import io
import os
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import path_or_orbit   # noqa: E402

MODULE = os.path.join(HERE, "path_or_orbit.py")
LIST = os.path.join(HERE, "celestial_objects.py")
TODAY = datetime.date(2026, 11, 4)


def rec(search, e, fetched="2026-11-04"):
    return {"search": search, "e": e, "class": None, "epoch_jd": None,
            "fullname": None, "fetched": fetched}


ENTRIES = {
    "open": {"name": "Open", "id": "C/2099 A1", "id_type": "smallbody",
             "object_type": "orbital"},
    "edge": {"name": "Edge", "id": "C/2099 A2", "id_type": "smallbody",
             "object_type": "orbital"},
    "closed": {"name": "Closed", "id": "C/2099 A3", "id_type": "smallbody",
               "object_type": "trajectory"},
    "none": {"name": "Nameless", "id": "C/2099 A4", "id_type": "smallbody",
             "object_type": "orbital"},
    "moved": {"name": "Moved", "id": "C/2099 A5", "id_type": "smallbody",
              "object_type": "orbital"},
    "craft": {"name": "Craft", "id": "-61", "id_type": "id",
              "object_type": "trajectory"},
    "moon": {"name": "Moonlet", "id": "X9", "id_type": "smallbody",
             "object_type": "satellite"},
    "mcnaught": {"name": "McNaught", "id": "C/2006 P1",
                 "id_type": "smallbody", "object_type": "trajectory"},
}
SOLUTIONS = {
    "Open": rec("C/2099 A1", "1.00005"),
    "Edge": rec("C/2099 A2", "1.0"),
    "Closed": rec("C/2099 A3", ".99999"),
    "Moved": rec("C/2099 A0", "1.2"),
    "Moonlet": rec("X9", "0.01"),
    # JPL's Small-Body Database, read 2026-11-04 (sbdb.api, full-prec)
    "McNaught": rec("C/2006 P1", "1.000018815882278"),
}


def module_from(source, label):
    mod = types.ModuleType("path_or_orbit_" + label)
    mod.__file__ = MODULE
    exec(compile(source, MODULE + " [" + label + "]", "exec"), mod.__dict__)
    return mod


def plant(old, new, label):
    with open(MODULE, "r", encoding="utf-8") as handle:
        source = handle.read()
    n = source.count(old)
    if n != 1:
        raise SystemExit("ANCHOR FAIL for planted fault '%s': %d matches"
                         % (label, n))
    return module_from(source.replace(old, new), label)


# ------------------------------------------------------------- checks

def check_rule(m):
    probs = []
    for key, want in (("open", True), ("edge", True), ("closed", False)):
        got = m.drawn_as_path(ENTRIES[key], SOLUTIONS)
        if got is not want:
            probs.append("%s (e %s) drawn as %s" % (
                ENTRIES[key]["name"], SOLUTIONS[ENTRIES[key]["name"]]["e"],
                "a path" if got else "an orbit"))
    for key in ("none", "moved"):
        try:
            m.drawn_as_path(ENTRIES[key], SOLUTIONS)
            probs.append("%s decided with no record of its own"
                         % ENTRIES[key]["name"])
        except m.NoSolution as exc:
            if exc.name != ENTRIES[key]["name"]:
                probs.append("the failure named %r, not %r"
                             % (exc.name, ENTRIES[key]["name"]))
    return (not probs, "; ".join(probs) or
            "Open 1.00005 and Edge 1.0 paths, Closed 0.99999 an orbit, "
            "Nameless and Moved refused by name")


def check_drawn_type(m):
    want = {"open": "trajectory", "closed": "orbital",
            "craft": "trajectory", "moon": "satellite"}
    probs = ["%s drawn as %r, not %r" % (ENTRIES[k]["name"],
                                         m.drawn_type(ENTRIES[k], SOLUTIONS),
                                         w)
             for k, w in sorted(want.items())
             if m.drawn_type(ENTRIES[k], SOLUTIONS) != w]
    return not probs, "; ".join(probs) or "typed field overruled both ways"


def check_sides(m):
    probs = []
    why = m.side_disagreement(ENTRIES["mcnaught"], 0.999939778, SOLUTIONS)
    if not why or not why.startswith("McNaught:"):
        probs.append("McNaught's two sides of 1 not refused by name (%r)"
                     % why)
    if m.side_disagreement(ENTRIES["mcnaught"], 1.00001, SOLUTIONS):
        probs.append("elements on the database's side refused")
    if m.side_disagreement(ENTRIES["craft"], 0.5, SOLUTIONS):
        probs.append("a spacecraft held to a database e")
    return not probs, "; ".join(probs) or "McNaught refused by name"


def check_cycle():
    f = ENTRIES["open"]
    probs = []
    cases = (({}, True, "no record"),
             ({"Open": rec("C/2099 A1", "1.1", "2026-10-05")}, True,
              "30 days old"),
             ({"Open": rec("C/2099 A1", "1.1", "2026-10-06")}, False,
              "29 days old"),
             ({"Open": rec("C/2099 B1", "1.1")}, True, "another search"))
    for sols, due, label in cases:
        if bool(path_or_orbit.refresh_due(f, sols, TODAY)) is not due:
            probs.append("%s: %s" % (label, "not due" if due else "due"))
    return not probs, "; ".join(probs) or "4 cases"


def check_answers():
    probs = []
    good = {"object": {"fullname": "C/2099 A1 (Test)",
                       "orbit_class": {"code": "HYP"}},
            "orbit": {"epoch": "2461000.5",
                      "elements": [{"name": "e", "value": "1.00005"}]}}
    r, _w, reached = path_or_orbit.fetch_solution("C/2099 A1", TODAY,
                                                  lambda p: good)
    if not (reached and r and r["e"] == "1.00005" and r["class"] == "HYP"
            and r["fetched"] == "2026-11-04"):
        probs.append("an orbit not read: %r" % (r,))
    r, w, reached = path_or_orbit.fetch_solution(
        "C/2099", TODAY, lambda p: {"list": []})
    if not reached or r is not None or "several" not in w:
        probs.append("several matches not named")

    def down(_p):
        raise IOError("planted: no network")
    r, _w, reached = path_or_orbit.fetch_solution("C/2099 A1", TODAY, down)
    if reached or r is not None:
        probs.append("no network read as reached")
    return not probs, "; ".join(probs) or "3 answers"


def entries_carrying(text, field):
    tree = ast.parse(text)
    node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(
        getattr(t, "id", None) == "OBJECT_DEFINITIONS" for t in n.targets))
    names, bad = 0, []
    for entry in node.value.elts:
        names += 1
        keys = [k.value for k in entry.keys if isinstance(k, ast.Constant)]
        if field in keys:
            name = next((ast.literal_eval(v) for k, v in
                         zip(entry.keys, entry.values)
                         if isinstance(k, ast.Constant) and k.value == "name"),
                        "?")
            bad.append(name)
    return names, bad


def check_guard(plant_it=False):
    with open(LIST, "r", encoding="utf-8") as handle:
        text = handle.read()
    if plant_it:
        text = text.replace("'key': 'west',", "'key': 'west', "
                            "'open_path': True,", 1)
    n, bad = entries_carrying(text, "open_path")
    return (n > 0 and not bad,
            "%d entries examined; carrying open_path: %s"
            % (n, ", ".join(bad) or "none"))


def check_store():
    with open(LIST, "r", encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(
        getattr(t, "id", None) == "OBJECT_DEFINITIONS" for t in n.targets))
    solutions = path_or_orbit.load_solutions(HERE)
    small, missing = 0, []
    for entry in node.value.elts:
        f = {}
        for k, v in zip(entry.keys, entry.values):
            if isinstance(k, ast.Constant):
                try:
                    f[k.value] = ast.literal_eval(v)
                except ValueError:
                    pass
        if "key" not in f or not path_or_orbit.is_small_body(f):
            continue
        small += 1
        try:
            path_or_orbit.solution_e(f, solutions)
        except path_or_orbit.NoSolution as exc:
            missing.append(str(exc))
    return (small > 0 and not missing,
            "%d keyed small bodies; without a database e: %s"
            % (small, "; ".join(missing) or "none"))


# The second link's made-up typed elements (L-512). 0.99994 is 6AC4721's
# typed e (MPEC 2026-A49); 1.00006 the same distance on the other side.
TYPED = {"Nameless": {"e": 0.99994}, "Closed": {"e": 1.5},
         "Moved": {"e": 0.5}}
TYPED_WRONG_SIDE = {"Nameless": {"e": 1.00006}, "Closed": {"e": 1.5},
                    "Moved": {"e": 0.5}}


def quietly(call):
    """(result or the NoSolution raised, what was printed)."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        try:
            got = call()
        except path_or_orbit.NoSolution as exc:
            got = exc
        except Exception as exc:   # a planted module's own NoSolution
            if exc.__class__.__name__ != "NoSolution":
                raise
            got = exc
    return got, out.getvalue()


def check_second_link(m, typed=TYPED):
    probs = []
    none, closed, moved = ENTRIES["none"], ENTRIES["closed"], ENTRIES["moved"]
    got, said = quietly(lambda: m.drawn_type(none, SOLUTIONS, True, typed))
    if got != "orbital":
        probs.append("Nameless (no record, typed e 0.99994) drawn as %r"
                     % (got,))
    elif "Nameless" not in said or "orbital_elements.py" not in said:
        probs.append("the console did not name Nameless and "
                     "orbital_elements.py (%r)" % said.strip())
    got, said = quietly(lambda: m.drawn_type(closed, SOLUTIONS, True, typed))
    if got != "orbital":
        probs.append("Closed (record 0.99999, typed 1.5) drawn as %r: the "
                     "typed e read before the store" % (got,))
    elif said:
        probs.append("a body decided by the store printed %r" % said.strip())
    got, _said = quietly(lambda: m.drawn_type(moved, SOLUTIONS, True, typed))
    if getattr(got, "name", None) != "Moved":
        probs.append("Moved (asked of another search) not refused by name "
                     "(%r)" % (got,))
    got, said = quietly(lambda: m.drawn_type_or_none(none, SOLUTIONS, {}))
    if got is not None or "FAILED Nameless" not in said:
        probs.append("with neither link the plot's call gave %r, printed %r"
                     % (got, said.strip()))
    got, _said = quietly(lambda: m.drawn_type(none, SOLUTIONS))
    if getattr(got, "name", None) != "Nameless":
        probs.append("the export's call (no fallback) decided Nameless: %r"
                     % (got,))
    got, _said = quietly(lambda: m.side_disagreement(
        none, 0.99994, SOLUTIONS, True, typed))
    if got is not None:
        probs.append("the orbit drawing's side check refused Nameless: %r"
                     % (got,))
    return (not probs, "; ".join(probs) or
            "Nameless an orbit by its typed e, said by name; Closed by the "
            "store; Moved refused; neither link FAILED; the export strict")


def lookup_off_fails_by_name(m):
    got, _said = quietly(lambda: m.drawn_type(ENTRIES["none"], SOLUTIONS,
                                              True, TYPED))
    return getattr(got, "name", None) == "Nameless"


def check_plot_list():
    """Every small body the plot sends through the rule, from the real
    list, decided by one link; the second link's bodies named."""
    from orbital_elements import planetary_params
    with open(LIST, "r", encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(
        getattr(t, "id", None) == "OBJECT_DEFINITIONS" for t in n.targets))
    solutions = path_or_orbit.load_solutions(HERE)
    small, typed, failed = 0, [], []
    for entry in node.value.elts:
        f = {}
        for k, v in zip(entry.keys, entry.values):
            if isinstance(k, ast.Constant):
                try:
                    f[k.value] = ast.literal_eval(v)
                except ValueError:
                    pass
        if (f.get("object_type") not in ("orbital", "trajectory")
                or not path_or_orbit.is_small_body(f)):
            continue
        small += 1
        got, _said = quietly(lambda: path_or_orbit.decided_e(
            f, solutions, planetary_params))
        if isinstance(got, Exception):
            failed.append(str(got))
        elif got[1] == "typed":
            typed.append("%s (e %r, %s)" % (f["name"], got[0],
                                            "a path" if got[0] >= 1.0
                                            else "an orbit"))
    return (small > 0 and not failed,
            "%d small bodies in the plot's list; decided by their typed "
            "elements: %s; decided by neither: %s"
            % (small, ", ".join(typed) or "none",
               "; ".join(failed) or "none"))


def main():
    results = []

    def check(ok, label):
        results.append((ok, label))
        print("  %s  %s" % ("ok  " if ok else "FAIL", label))

    real = path_or_orbit
    ok, why = check_rule(real)
    check(ok, "1. the rule: at or above 1 a path, below an orbit, no record "
              "refused by name (%s)" % why)
    for label, old, new in (
            ("the comparison turned the wrong way",
             "    return solution_e(f, solutions) >= 1.0\n",
             "    return solution_e(f, solutions) < 1.0\n"),
            ("'above 1' in place of 'at or above'",
             "    return solution_e(f, solutions) >= 1.0\n",
             "    return solution_e(f, solutions) > 1.0\n")):
        check(not check_rule(plant(old, new, label))[0],
              "1. planted fault caught: %s" % label)
    ok, why = check_drawn_type(real)
    check(ok, "2. the drawn type (%s)" % why)
    check(not check_drawn_type(plant(
        '    return ("trajectory" if drawn_as_path(f, solutions, fallback, '
        'params)\n            else "orbital")\n', "    return typed\n",
        "typed"))[0],
        "2. planted fault caught: the typed field let decide again")
    ok, why = check_sides(real)
    check(ok, "3. two sides of 1 refused by name (%s)" % why)
    check(not check_sides(plant(
        "    if (db_e >= 1.0) != (osc >= 1.0):\n",
        "    if False:\n", "never"))[0],
        "3. planted fault caught: the side check that never fails")
    ok, why = check_cycle()
    check(ok, "4. the 30-day cycle (%s)" % why)
    ok, why = check_answers()
    check(ok, "5. JPL's answer read (%s)" % why)
    ok, why = check_guard()
    check(ok, "6. no entry of celestial_objects.py carries open_path (%s)"
          % why)
    planted = check_guard(plant_it=True)
    check(not planted[0] and "West" in planted[1],
          "6. planted fault caught, naming West: open_path put back")
    ok, why = check_store()
    check(ok, "7. every keyed small body has its database e (%s)" % why)
    ok, why = check_second_link(real)
    check(ok, "8. the plot's second link, the typed elements' e (%s)" % why)
    check(not check_second_link(real, TYPED_WRONG_SIDE)[0],
          "8. planted fault caught: the typed e put on the wrong side of 1 "
          "changes the answer")
    off = plant("    e = typed_e(f, params)\n", "    e = None\n", "lookup off")
    check(not check_second_link(off)[0] and lookup_off_fails_by_name(off)
          and not lookup_off_fails_by_name(real),
          "8. planted fault caught: the lookup turned off fails by name "
          "(Nameless)")
    check(not check_second_link(plant(
        "    if solutions.get(name) is not None:\n", "    if False:\n",
        "typed first"))[0],
        "8. planted fault caught: the typed e read before the store")
    ok, why = check_plot_list()
    check(ok, "9. every small body in the plot's list is decided (%s)" % why)

    failed = [label for ok, label in results if not ok]
    print()
    if failed:
        print("PATH OR ORBIT SUITE: %d of %d checks FAILED: %s"
              % (len(failed), len(results), "; ".join(failed)))
        return 1
    print("PATH OR ORBIT SUITE: %d of %d checks passed, every planted "
          "fault caught" % (len(results), len(results)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
