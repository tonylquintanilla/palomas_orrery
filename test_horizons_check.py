"""
test_horizons_check.py -- the Horizons check (L-395, L-431) on JPL's
recorded answers, with no network: every entry agrees, and every planted
fault is caught by name.

WHY THIS EXISTS

    A pass that could not have been a fail proves nothing, so these tests
    plant wrong entries, wrong periods and changed data sheets and require
    each one to be caught, by entry and field, before the agreeing run is
    trusted (A Check That Cannot Fail Is Not Passing).

THE ANSWERS

    documentation/worksheets/horizons_answers_L395.json, keyed by the
    exact query the check makes. The identity answers came with the check
    from the gallery: those of 2026-10-07 are Tony's, fetched in his
    browser; those of 2026-10-10 were fetched through the chat's
    web-fetch tool. The elements and data-sheet answers were CONSTRUCTED
    by L-431's build 3, which could not reach JPL, and the file says so
    for each. A query with no recorded answer is treated as "could not
    reach JPL", so a test can never pass on an answer nobody recorded.

    The same file's "inputs" hold what the check is run on, frozen with
    the answers: the orbit cache's entries for Mercury, Jupiter and Encke
    at orrery db63721d, the thirteen confirmations as the move carried
    them over, and the seeded data sheets. The live records change on
    every plot and every check -- the first live run confirms the three
    periods, and a re-plotted body's period moves to a date no answer was
    recorded for -- and a test that read them would fail on the day the
    check first worked.

WHAT IT CHECKS

    1. The thirteen served entries as the orrery's list held them on
       2026-10-10, and the tested cases MAPS and 3I/ATLAS: each agrees;
       the two pinned comets name their pin the newest.
    2. Planted identity faults, each caught by name: a wrong id; an
       id_type pointing at the other index, both ways; a horizons_name
       off by one character; a stale pin; a pin whose record number JPL
       gave to another comet; a wrong object_type on the barycentre; JPL
       unreachable; an answer that is not JPL's; a comet whose record
       list cannot be fetched. (L-443) A spacecraft, Voyager 1, agrees:
       the small-body index answers its id with JPL's header alone, which
       is no matches; planted: the same header with any other line is
       still JPL not read, never a pass.
    3. The period (L-431): Mercury, Jupiter and Encke agree with JPL's PR
       at their own date and centre. Planted: a PR farther from the
       served period than its error (the check must not pass a period
       JPL disagrees with); an open orbit where a period is served; an
       answer with no elements row; JPL unreachable; a barycentre period
       is asked around the barycentre. (L-445) Earth's period, asked of
       its record's target, the Earth-Moon barycentre (3), agrees with
       JPL's recorded answer for 3; planted: a copy of the check that asks
       the body's own id, 399, against an answer for 399 that would agree,
       caught by the question it asks; a period confirmed when asked of
       399 is due at once; the run records the target in the
       confirmation.
    4. The data sheets (L-401): the Voyagers' figures are read. Planted:
       a moved Revised date with the figure unchanged (noted, not red); a
       changed figure (red, naming the row); a sheet that no longer
       states one (red); a sheet with no Revised date (red: a blind spot
       announces); a spacecraft missing from the record (read and
       recorded).
    5. The run, in a throwaway folder: the carried-over confirmations ask
       JPL nothing for identity, only the never-confirmed periods; a
       second run the same day asks nothing (NOTHING DUE); 26 days on
       every identity is asked again (from day 25) while the offline
       checker still passes, so the website, red at day 30, is never
       left without time for the push and the pull; a period
       re-fetched in the orrery is due at once; an entry changed after
       its confirmation is due at once; JPL unreachable on a due day is
       UNREACHABLE, by name, with nothing recorded; after JPL fails once,
       nothing more is asked.
    6. The offline checker (check_horizons_confirmations.py): it passes on
       a full record, and fails, by name, on a confirmation deleted, one
       overdue, one whose horizons_name changed, a period never
       confirmed, today's run UNREACHABLE, and a sheet a row quotes that
       no longer gives the row's figure.

RUN COMMAND

    python test_horizons_check.py

    Open it in VS Code and click Run. orrery_maintenance_run.py runs it
    among the checkers, and it gates. It writes only to a throwaway
    folder.

Role: devtool
Domain: dev_tools

Module created: October 10, 2026 with Anthropic's Claude Opus 5.5
(L-395, the Horizons check, in the gallery repo).
Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5 (L-431,
build 3, with L-395's move: moved into the orrery with the check; the
period comparison, the data sheets, the run on the orrery's own files and
the orrery's offline checker are tested, each by planted faults.)
Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5 (L-445,
Earth's period: the period is asked of its record's target, shown with a
planted copy of the check asking the body's own id, on JPL's answers for
target 3 in documentation/worksheets/period_answers_L445.json.)
Module updated: October 25, 2026 with Anthropic's Claude Opus 5.5 (L-443,
a spacecraft's identity on JPL's two Lookup answers for -31, fetched that
day through the chat's web-fetch tool and kept in VOYAGER_1_LOOKUP.)
"""

import datetime
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import check_horizons_confirmations as offline  # noqa: E402
import horizons_check as hc  # noqa: E402

ANSWERS = os.path.join(HERE, "documentation", "worksheets",
                       "horizons_answers_L395.json")
EARTH_ANSWERS = os.path.join(HERE, "documentation", "worksheets",
                             "period_answers_L445.json")
MODULE = os.path.join(HERE, "horizons_check.py")
TODAY = datetime.date(2026, 10, 14)

# The thirteen served entries' identity facts as the orrery's list held
# them on 2026-10-10 (orrery patch_L395_5), fixed here so the test does
# not move when the list grows.
SERVED = {
    "sun": ("Sun", "10", None, "Sun", "fixed"),
    "mercury": ("Mercury", "199", None, "Mercury", "orbital"),
    "venus": ("Venus", "299", None, "Venus", "orbital"),
    "earth": ("Earth", "399", None, "Earth", "orbital"),
    "mars": ("Mars", "499", None, "Mars", "orbital"),
    "jupiter": ("Jupiter", "599", None, "Jupiter", "orbital"),
    "saturn": ("Saturn", "699", None, "Saturn", "orbital"),
    "uranus": ("Uranus", "799", None, "Uranus", "orbital"),
    "neptune": ("Neptune", "899", None, "Neptune", "orbital"),
    "pluto_barycenter": ("Pluto-Charon Barycenter", "9", None,
                         "Pluto Barycenter", "barycenter"),
    "apophis": ("Apophis", "2004 MN4", "smallbody", "99942 Apophis",
                "orbital"),
    "halley": ("Halley", "90000030", "smallbody", "1P/Halley", "orbital"),
    "encke": ("Encke", "90000091", "smallbody", "2P/Encke", "orbital"),
}
TESTED = {
    "maps": ("MAPS", "C/2026 A1", "smallbody", "MAPS (C/2026 A1)", "orbital"),
    "atlas_3i": ("3I/ATLAS", "C/2025 N1", "smallbody", "ATLAS (C/2025 N1)",
                 "orbital"),
}
SPACECRAFT = (("Voyager 1", "-31"), ("Voyager 2", "-32"),
              ("Pioneer 10", "-23"))
FETCHED = ("Mercury", "Jupiter", "Encke")

# L-443, 2026-10-25: JPL's Lookup answers for Voyager 1 (-31), fetched
# that day through the chat's web-fetch tool, word for word. The
# small-body index answers a spacecraft's id with its header alone.
VOYAGER_1 = ("Voyager 1", "-31", None, "Voyager 1 (spacecraft)",
             "trajectory")
VOYAGER_1_LOOKUP = {
    hc.lookup_url("-31", "mb"): (
        "API VERSION: 1.1\n"
        "API SOURCE: NASA/JPL Horizons Lookup API\n\n"
        "Object name        = Voyager 1 (spacecraft)\n"
        "Type               = spacecraft\n"
        "Primary SPKID      = -31\n"
        "Primary designation= 1977-084A\n"
        "Aliases            = \n"),
    hc.lookup_url("-31", "sb"): (
        "API VERSION: 1.1\n"
        "API SOURCE: NASA/JPL Horizons Lookup API\n"),
}


def entry(spec):
    _name, hid, id_type, hname, otype = spec
    return {"horizons_id": hid, "id_type": id_type, "horizons_name": hname,
            "object_type": otype}


def recorded_fetch(answers, down=(), extra=None):
    def fetch(url):
        for marker in down:
            if marker in url:
                raise hc.Unreachable("planted: no network")
        if extra and url in extra:
            return extra[url]
        if url not in answers:
            raise hc.Unreachable("no recorded answer for %s" % url)
        return answers[url]
    return fetch


class Tally(object):
    def __init__(self):
        self.passed = 0
        self.failed = []

    def check(self, ok, label):
        if ok:
            self.passed += 1
            print("  ok    %s" % label)
        else:
            self.failed.append(label)
            print("  FAIL  %s" % label)


def fields(result):
    return sorted(d[0] for d in result["disagreements"])


def fixture_list(served):
    lines = ["OBJECT_DEFINITIONS = ["]
    for key, (name, hid, id_type, hname, otype) in served.items():
        lines.append("    {'name': %r, 'key': %r, 'id': %r, 'id_type': %r, "
                     "'horizons_name': %r, 'object_type': %r, "
                     "'mission_info': 'Horizons: %s. A body.', "
                     "'mission_url': None}," % (name, key, hid, id_type,
                                                hname, otype, hid))
    for name, hid in SPACECRAFT:
        lines.append("    {'name': %r, 'id': %r, 'id_type': 'id', "
                     "'object_type': 'trajectory'}," % (name, hid))
    lines.append("]")
    return "\n".join(lines) + "\n"


def build_root(tmp, real_cache, inputs, served=None):
    os.makedirs(os.path.join(tmp, "data"), exist_ok=True)
    with open(os.path.join(tmp, "celestial_objects.py"), "w") as handle:
        handle.write(fixture_list(served or SERVED))
    cache = {name: real_cache[name] for name in FETCHED}
    with open(os.path.join(tmp, "data", "osculating_cache.json"), "w") as h:
        json.dump(cache, h)
    rows = {"VOYAGER_1_POINTING_RA_2030_ARCSEC": 1.701,
            "VOYAGER_1_POINTING_DEC_2030_ARCSEC": 1.535,
            "VOYAGER_2_POINTING_RA_2030_ARCSEC": 4.718,
            "VOYAGER_2_POINTING_DEC_2030_ARCSEC": 3.715}
    with open(os.path.join(tmp, "data", "constants_export.json"), "w") as h:
        json.dump({"rows": {k: {"value": v, "read": [
            "data sheet, the uncertainty paragraph, 2026-10-12, Claude"]}
            for k, v in rows.items()}}, h)
    with open(os.path.join(tmp, hc.CONFIRMATIONS), "w") as h:
        json.dump(inputs["confirmations"], h)
    seed = json.loads(json.dumps(inputs["sheets"]))
    seed["sheets"] = {k: v for k, v in seed["sheets"].items()
                      if k in dict((i, n) for n, i in SPACECRAFT)}
    with open(os.path.join(tmp, hc.SHEETS), "w") as h:
        json.dump(seed, h)
    return cache


def earth_case(earth):
    """(object, period block) for Earth with its period asked of the
    Earth-Moon barycentre (L-445): its entry as L-444's live run wrote it,
    the record moved to target 3 with JPL's recorded PR for 3 around the
    Sun and that period's change in a year as its error."""
    import export_objects as ex
    entry = json.loads(json.dumps(earth["inputs"]["cache"]["Earth"]))
    rec = entry["period"]
    pair = earth["answers"]["period_pairs"][
        "3|None|%s|@sun" % rec["epoch"]]["answer"]
    rec.update({"target": "3",
                "target_label": "the Earth-Moon center of mass",
                "days": pair["p1"],
                "error_days": abs(pair["p2"] - pair["p1"]),
                "year_change_days": abs(pair["p2"] - pair["p1"]),
                "elements": pair["elements"]})
    block, _inputs = ex.period_block("Earth", "orbital", {"Earth": entry}, {})
    obj = {"horizons_id": "399", "id_type": None, "horizons_name": "Earth",
           "object_type": "orbital", "name": "Earth", "period": block}
    return obj, entry


def checker_with(old, new):
    """A copy of horizons_check.py with one fault planted in it."""
    import types
    with open(MODULE, "r", encoding="utf-8") as handle:
        src = handle.read().replace("\r\n", "\n")
    if src.count(old) != 1:
        raise SystemExit("ANCHOR FAIL for a planted fault: %r" % old[:60])
    mod = types.ModuleType("horizons_check_planted")
    mod.__file__ = MODULE
    exec(compile(src.replace(old, new), MODULE + " [planted]", "exec"),
         mod.__dict__)
    return mod


def main():
    with open(ANSWERS, "r", encoding="utf-8") as handle:
        recorded = json.load(handle)
    with open(EARTH_ANSWERS, "r", encoding="utf-8") as handle:
        earth = json.load(handle)
    earth_answers = dict((u, v["answer"])
                         for u, v in earth["check_answers"].items())
    answers = recorded["answers"]
    inputs = recorded["inputs"]
    real_cache = inputs["cache"]
    fetch = recorded_fetch(answers)
    quiet = lambda *a: None  # noqa: E731
    t = Tally()

    print("1. Every served entry, and the tested cases, agree")
    for key, spec in list(SERVED.items()) + list(TESTED.items()):
        r = hc.check_entry(key, entry(spec), fetch)
        t.check(r["status"] == "agrees",
                "%s agrees (JPL: %s)" % (key, r["jpl"].get("name")
                                         or r["error"] or r["disagreements"]))
    for key in ("halley", "encke"):
        r = hc.check_entry(key, entry(SERVED[key]), fetch)
        pin = r["pin"] or {}
        t.check(pin.get("newest") == SERVED[key][1],
                "%s: its pin is the newest of %s records, solution date %s"
                % (key, pin.get("records"), pin.get("solution_date")))

    print("2. Planted identity faults, each caught by entry and field")
    planted = [
        ("a wrong id (Mars as 599)", "mars",
         ("Mars", "599", None, "Mars", "orbital"), ["horizons_name"]),
        ("id_type pointing at the small-body index (Mars)", "mars",
         ("Mars", "499", "smallbody", "Mars", "orbital"), ["id_type"]),
        ("id_type pointing at the major-body index (Apophis)", "apophis",
         ("Apophis", "2004 MN4", None, "99942 Apophis", "orbital"),
         ["id_type"]),
        ("horizons_name off by one character", "apophis",
         ("Apophis", "2004 MN4", "smallbody", "99942 Apophls", "orbital"),
         ["horizons_name"]),
        ("a stale pin (Encke on record 90000090)", "encke",
         ("Encke", "90000090", "smallbody", "2P/Encke", "orbital"), ["pin"]),
        ("a record number JPL gave to another comet (MAPS on 90004956)",
         "maps", ("MAPS", "90004956", "smallbody", "MAPS (C/2026 A1)",
                  "orbital"), ["horizons_name"]),
        ("object_type wrong on the barycentre", "pluto_barycenter",
         ("Pluto-Charon Barycenter", "9", None, "Pluto Barycenter", "fixed"),
         ["object_type"]),
    ]
    for label, key, spec, want in planted:
        r = hc.check_entry(key, entry(spec), fetch)
        t.check(r["status"] == "DISAGREES" and fields(r) == want,
                "%s: %s %s" % (label, r["status"], fields(r)))
    r = hc.check_entry("mars", entry(SERVED["mars"]),
                       recorded_fetch(answers, down=("sstr=499",)))
    t.check(r["status"] == "could not reach JPL",
            "JPL unreachable: %s, never a pass" % r["status"])
    r = hc.check_entry("mars", entry(SERVED["mars"]),
                       lambda url: "<html>Service unavailable</html>")
    t.check(r["status"] == "could not reach JPL",
            "an answer that is not JPL's: %s" % r["status"])
    r = hc.check_entry("halley", entry(SERVED["halley"]),
                       recorded_fetch(answers, down=("DES=",)))
    t.check(r["status"] == "could not reach JPL",
            "a pinned comet whose record list cannot be fetched: %s"
            % r["status"])
    r = hc.check_entry("voyager_1", entry(VOYAGER_1),
                       recorded_fetch({}, extra=VOYAGER_1_LOOKUP))
    t.check(r["status"] == "agrees"
            and r["jpl"].get("name") == "Voyager 1 (spacecraft)",
            "a spacecraft agrees, the small-body index answering its id "
            "with JPL's header alone: %s (JPL: %s)"
            % (r["status"], r["jpl"].get("name") or r["error"]))
    odd = dict(VOYAGER_1_LOOKUP)
    odd[hc.lookup_url("-31", "sb")] += "ERROR: something JPL said\n"
    r = hc.check_entry("voyager_1", entry(VOYAGER_1),
                       recorded_fetch({}, extra=odd))
    t.check(r["status"] == "could not reach JPL",
            "planted: JPL's header with any other line is not read as no "
            "matches: %s" % r["status"])

    tmp = tempfile.mkdtemp(prefix="horizons_check_test_")
    try:
        build_root(tmp, real_cache, inputs)
        objects, _sha, spacecraft = hc.current_entries(tmp)

        print("3. The period, against JPL's PR at its own date and centre")
        for key in ("mercury", "jupiter", "encke"):
            r = hc.check_period(key, objects[key], objects[key]["period"],
                                fetch)
            t.check(r["status"] == "agrees" and "CENTER='@sun'" in r["query"],
                    "%s agrees: JPL's PR %s days, served %s"
                    % (key, r["jpl_days"],
                       objects[key]["period"]["days"]["text"]))
        enc = objects["encke"]
        url = hc.check_period("encke", enc, enc["period"], fetch)["query"]
        err = enc["period"]["record"]["error_days"]
        moved = answers[url].replace(
            "PR= %.15E" % enc["period"]["record"]["days"],
            "PR= %.15E" % (enc["period"]["record"]["days"] + 2 * err))
        r = hc.check_period("encke", enc, enc["period"],
                            recorded_fetch(answers, extra={url: moved}))
        t.check(moved != answers[url] and r["status"] == "DISAGREES"
                and r["disagreement"][0] == "period",
                "a PR %.3g days from the served period, twice its error: %s"
                % (2 * err, r["status"]))
        if r["disagreement"]:
            print("        as printed:  served: %s / JPL: %s"
                  % (r["disagreement"][1], r["disagreement"][2]))
        opened = answers[url].replace(
            "PR= %.15E" % enc["period"]["record"]["days"], "PR= 9.999E+99")
        r = hc.check_period("encke", enc, enc["period"],
                            recorded_fetch(answers, extra={url: opened}))
        t.check(r["status"] == "DISAGREES",
                "an open orbit where a period is served: %s" % r["status"])
        refused = ("API VERSION: 1.2\nAPI SOURCE: NASA/JPL Horizons API\n\n"
                   "Cannot interpret date. Type \"?!\" or try YYYY-MMM-DD\n")
        r = hc.check_period("encke", enc, enc["period"],
                            recorded_fetch(answers, extra={url: refused}))
        t.check(r["status"] == "DISAGREES" and "no elements row"
                in r["disagreement"][2],
                "an answer with no elements row: %s" % r["status"])
        r = hc.check_period("encke", enc, enc["period"],
                            recorded_fetch(answers, down=("ELEMENTS",)))
        t.check(r["status"] == "could not reach JPL",
                "JPL unreachable for a period: %s" % r["status"])
        bary = json.loads(json.dumps(objects["mercury"]))
        bary["period"]["center"] = "@0"
        r = hc.check_period("mercury", bary, bary["period"],
                            recorded_fetch(answers))
        t.check("CENTER='@0'" in (r["query"] or ""),
                "a barycentre period is asked around the barycentre")

        # L-445: Earth's period is the Earth-Moon barycentre's. The fetch
        # holds a recorded JPL answer for 3 and a planted one for 399 that
        # would agree too, so only the question asked tells them apart.
        e_obj, _e_entry = earth_case(earth)
        e_fetch = recorded_fetch(earth_answers)
        r = hc.check_period("earth", e_obj, e_obj["period"], e_fetch)
        t.check(r["status"] == "agrees" and "COMMAND='3'" in (r["query"] or "")
                and r.get("target") == "3",
                "Earth's period, asked of its record's target 3 around the "
                "Sun, agrees: JPL's PR %s days, served %s"
                % (r["jpl_days"], e_obj["period"]["days"]["text"]))
        wrong = checker_with(
            '    target = period.get("target") or obj.get("horizons_id")\n',
            '    target = obj.get("horizons_id")\n')
        r = wrong.check_period("earth", e_obj, e_obj["period"], e_fetch)
        t.check("COMMAND='3'" not in (r["query"] or ""),
                "planted: the check asking the body's own id, 399, while the "
                "record names 3 -- caught: it asked %s"
                % ((r["query"] or "").split("&")[1:2] or ["nothing"])[0])
        held = {"horizons_id": "399", "period": {
            "confirmed": "2026-10-15", "center": "@sun",
            "epoch": e_obj["period"]["record"]["epoch"],
            "days": e_obj["period"]["record"]["days"]}}
        pstate, pdetail = hc.period_state(e_obj["period"], held, TODAY)
        t.check(pstate == "changed" and "target" in pdetail,
                "a period confirmed when asked of 399 is due at once once its "
                "target is 3: %s" % pdetail)
        tmp_e = tempfile.mkdtemp(prefix="horizons_check_earth_")
        try:
            build_root(tmp_e, real_cache, inputs)
            cpath = os.path.join(tmp_e, "data", "osculating_cache.json")
            ecache = hc.load_json(cpath)
            ecache["Earth"] = _e_entry
            with open(cpath, "w") as handle:
                json.dump(ecache, handle)
            both = dict(answers)
            both.update(earth_answers)
            code, out = hc.run(tmp_e, recorded_fetch(both), TODAY, pause=0,
                               echo=quiet)
            conf = hc.load_confirmations(os.path.join(tmp_e, hc.CONFIRMATIONS))
            ep = conf["objects"]["earth"].get("period") or {}
            t.check(code == 0 and ep.get("target") == "3"
                    and "COMMAND='3'" in (ep.get("query") or ""),
                    "the run confirms Earth's period and records its target "
                    "3 and the query (%s)" % out.get("verdict"))
        finally:
            shutil.rmtree(tmp_e, ignore_errors=True)

        print("4. The data sheets")
        for ident in ("-31", "-32"):
            sheet = hc.parse_sheet(answers[hc.sheet_url(ident)])
            t.check(isinstance(sheet["stated"], dict)
                    and sheet["revised"] == "Aug 19, 2022",
                    "%s: Revised %s, %s" % (ident, sheet["revised"],
                                            sheet["stated"]))
        sheet = hc.parse_sheet(answers[hc.sheet_url("-23")])
        t.check(sheet["stated"] is None, "-23: states none, as surveyed")
        rows = hc.row_values(tmp)
        seed = hc.load_sheets(os.path.join(tmp, hc.SHEETS))["sheets"]
        t.check(not hc.sheet_problems(seed["-31"], rows),
                "the seeded record and the rows agree")
        changed = dict(seed["-31"], stated={"RA_arcsec": 1.801,
                                            "DEC_arcsec": 1.535})
        probs = hc.sheet_problems(changed, rows)
        t.check(len(probs) == 1 and "VOYAGER_1_POINTING_RA_2030_ARCSEC"
                in probs[0], "a changed figure is red, naming the row: %s"
                % probs[:1])
        gone = dict(seed["-31"], stated=None, read="2026-11-11")
        probs = hc.sheet_problems(gone, rows)
        t.check(len(probs) == 2, "a sheet that no longer states one is red "
                "for both rows: %d" % len(probs))
        reread = dict(seed["-31"], stated=None, read="2026-10-11")
        t.check(not hc.sheet_problems(reread, rows),
                "...and a row re-read since that sheet read clears it")
        try:
            hc.parse_sheet("API VERSION: 1.2\nAPI SOURCE: NASA/JPL "
                           "Horizons API\n\n Voyager 1   -31\n")
            ok = False
        except ValueError:
            ok = True
        t.check(ok, "a sheet with no Revised date is refused, never passed")

        print("5. The run")
        asked = []
        code, out = hc.run(tmp, lambda u: asked.append(u) or fetch(u), TODAY,
                           pause=0, echo=quiet)
        conf = hc.load_confirmations(os.path.join(tmp, hc.CONFIRMATIONS))
        periods = [k for k, v in conf["objects"].items() if v.get("period")]
        t.check(code == 0 and out["verdict"] == "PASS" and len(asked) == 3
                and all("ELEMENTS" in u for u in asked)
                and sorted(periods) == ["encke", "jupiter", "mercury"],
                "first run: identity carried over, so only the 3 periods "
                "asked (%d queries, %s)" % (len(asked), out.get("verdict")))
        asked = []
        code, out = hc.run(tmp, lambda u: asked.append(u) or fetch(u), TODAY,
                           pause=0, echo=quiet)
        t.check(code == 0 and out["verdict"] == "NOTHING DUE" and not asked,
                "second run the same day: %s, %d queries"
                % (out["verdict"], len(asked)))
        early = datetime.date(2026, 11, 5)
        code, out = hc.run(tmp, fetch, early, pause=0, echo=quiet,
                           write=False)
        due = sorted(set(kind for kind, _k, _r, _w in out["results"]))
        lines = []
        ok_offline = offline.run(tmp, early, echo=lines.append) == 0
        t.check(due == ["identity"] and len(out["results"]) == len(SERVED)
                and ok_offline,
                "26 days on, every identity is asked again while the "
                "offline checker still passes (%d asked, offline %s)"
                % (len(out["results"]), "pass" if ok_offline else "FAIL"))

        cache_path = os.path.join(tmp, "data", "osculating_cache.json")
        cache = hc.load_json(cache_path)
        cache["Jupiter"]["period"]["days"] += 0.001
        with open(cache_path, "w") as handle:
            json.dump(cache, handle)
        code, out = hc.run(tmp, fetch, TODAY, pause=0, echo=quiet,
                           write=False)
        due = [(k, kind) for kind, k, _r, _w in out["results"]]
        t.check(due == [("jupiter", "period")],
                "a period re-fetched in the orrery is due at once: %s" % due)
        cache["Jupiter"]["period"]["days"] -= 0.001
        with open(cache_path, "w") as handle:
            json.dump(cache, handle)
        renamed = dict(SERVED)
        renamed["mars"] = ("Mars", "499", None, "Mars ", "orbital")
        with open(os.path.join(tmp, "celestial_objects.py"), "w") as handle:
            handle.write(fixture_list(renamed))
        code, out = hc.run(tmp, fetch, TODAY, pause=0, echo=quiet,
                           write=False)
        t.check(code == 1 and [(k, kind) for kind, k, _r, _w in
                               out["results"]] == [("mars", "identity")],
                "an entry changed after its confirmation is due at once and "
                "caught: %s" % out["problems"])
        with open(os.path.join(tmp, "celestial_objects.py"), "w") as handle:
            handle.write(fixture_list(SERVED))
        later = datetime.date(2026, 11, 12)
        before = hc.load_confirmations(os.path.join(tmp, hc.CONFIRMATIONS))
        lines = []
        code, out = hc.run(tmp, recorded_fetch(answers, down=("sstr=10&",)),
                           later, pause=0, echo=lines.append)
        after = hc.load_confirmations(os.path.join(tmp, hc.CONFIRMATIONS))
        t.check(code == 1 and out["verdict"] == "UNREACHABLE"
                and after["objects"] == before["objects"]
                and "UNREACHABLE" in lines[-1] and "not checked" in lines[-1],
                "30 days on, JPL unreachable at the first query: %s, nothing "
                "recorded" % lines[-1][:74])
        asked = []

        def down_at_venus(url):
            asked.append(url)
            if "sstr=299" in url:
                raise hc.Unreachable("planted: HTTP 503")
            return fetch(url)
        code, out = hc.run(tmp, down_at_venus, later, pause=0, echo=quiet,
                           write=False)
        not_asked = [k for kind, k, r, _w in out["results"]
                     if r["status"] == "not asked"]
        t.check(code == 1 and out["verdict"] == "UNREACHABLE"
                and not any("sstr=399" in u for u in asked)
                and len(not_asked) >= 10,
                "after JPL fails once, nothing more is asked: %d parts not "
                "asked, %d queries in all" % (len(not_asked), len(asked)))
        code, out = hc.run(tmp, fetch, later, pause=0, echo=quiet)
        sheets = hc.load_sheets(os.path.join(tmp, hc.SHEETS))["sheets"]
        t.check(code == 0 and sheets["-31"]["read"] == later.isoformat()
                and sheets["-31"]["stated"]["RA_arcsec"] == 1.701,
                "30 days on and reachable: every part renewed, the sheets "
                "re-read (%s)" % out["verdict"])
        seed_missing = hc.load_sheets(os.path.join(tmp, hc.SHEETS))
        seed_missing["sheets"].pop("-23")
        with open(os.path.join(tmp, hc.SHEETS), "w") as handle:
            json.dump(seed_missing, handle)
        code, out = hc.run(tmp, fetch, later, pause=0, echo=quiet)
        sheets = hc.load_sheets(os.path.join(tmp, hc.SHEETS))["sheets"]
        t.check(code == 0 and "-23" in sheets
                and "first read" in sheets["-23"]["notes"][-1],
                "a spacecraft missing from the record is read and recorded")
        moved_sheet = answers[hc.sheet_url("-32")].replace(
            "Aug 19, 2022", "Oct 30, 2026")
        lines = []
        code, out = hc.run(tmp, recorded_fetch(
            answers, extra={hc.sheet_url("-32"): moved_sheet}),
            later, pause=0, echo=lines.append, check_all=True)
        sheets = hc.load_sheets(os.path.join(tmp, hc.SHEETS))["sheets"]
        t.check(code == 0 and sheets["-32"]["revised"] == "Oct 30, 2026"
                and "unchanged" in sheets["-32"]["notes"][-1],
                "a moved Revised date with the figure unchanged is noted, "
                "not red: %s" % out["verdict"])

        print("6. The offline checker")
        lines = []
        code = offline.run(tmp, later, echo=lines.append)
        t.check(code == 0, "a full, current record passes: %s" % lines[-1])
        path = os.path.join(tmp, hc.CONFIRMATIONS)
        good = hc.load_confirmations(path)

        def planted_offline(label, change, needle, target=path, base=None):
            data = json.loads(json.dumps(base or good))
            change(data)
            with open(target, "w") as handle:
                json.dump(data, handle)
            out = []
            code = offline.run(tmp, later, echo=out.append)
            t.check(code == 1 and any(needle in s for s in out),
                    "%s: exit %d, %s" % (label, code,
                                         [s for s in out if needle in s][:1]))
            with open(target, "w") as handle:
                json.dump(base or good, handle)

        planted_offline("a confirmation deleted",
                        lambda d: d["objects"].pop("venus"),
                        "venus: never confirmed")
        planted_offline("one overdue",
                        lambda d: d["objects"]["saturn"].update(
                            confirmed=str(later - datetime.timedelta(
                                days=hc.CADENCE_DAYS))),
                        "saturn: confirmed on")
        planted_offline("a period never confirmed",
                        lambda d: d["objects"]["encke"].pop("period"),
                        "encke: period never confirmed")
        last_path = os.path.join(tmp, hc.LAST_RUN)
        last = hc.load_json(last_path)
        planted_offline("today's run UNREACHABLE",
                        lambda d: d.update(verdict="UNREACHABLE",
                                           unasked=["venus's identity"]),
                        "UNREACHABLE", target=last_path, base=last)
        sheets_path = os.path.join(tmp, hc.SHEETS)
        sheet_base = hc.load_sheets(sheets_path)
        planted_offline("a sheet whose figure no longer matches its row",
                        lambda d: d["sheets"]["-32"]["stated"].update(
                            RA_arcsec=4.9),
                        "VOYAGER_2_POINTING_RA_2030_ARCSEC",
                        target=sheets_path, base=sheet_base)
        with open(os.path.join(tmp, "celestial_objects.py"), "w") as handle:
            handle.write(fixture_list(renamed))
        planted_offline("a horizons_name edited after its confirmation",
                        lambda d: None,
                        "mars: changed since its confirmation")
        with open(os.path.join(tmp, "celestial_objects.py"), "w") as handle:
            handle.write(fixture_list(SERVED))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("")
    print("%d checks passed, %d failed." % (t.passed, len(t.failed)))
    if t.failed:
        for label in t.failed:
            print("  - " + label)
        print("HORIZONS CHECK SUITE: FAIL")
        return 1
    print("HORIZONS CHECK SUITE: pass -- %d checks, every planted fault "
          "caught by name" % t.passed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
