"""
test_period_fetch.py -- the period fetch (L-444) on recorded answers, with
no network: it asks only for what is missing, with plotting's own call,
writes the record plotting writes, and names a failure; and every planted
fault is caught by name.

WHY THIS EXISTS

    A pass that could not have been a fail proves nothing (A Check That
    Cannot Fail Is Not Passing). So each check here is first run on a
    copy of period_fetch.py with one fault planted in its code, and must
    catch it, before the real module is run and trusted.

THE ANSWERS

    documentation/worksheets/period_fetch_answers_L444.json. Its inputs
    are the orbit cache's entries for Mercury, Jupiter and Encke at orrery
    ffd6c36a, as plotting wrote them from JPL. Its answers are what JPL
    returned for Mercury and Encke, read back from those entries, keyed by
    the exact question the orrery's code asks. One answer per body is
    constructed, the period around the barycentre, and the file says why.
    Only the three functions that talk to the network are replaced:
    orbit_data_manager.query_horizons_elements,
    orbital_period.query_period_pair and
    orbital_period.fetch_sbdb_period_sigma. Everything above them --
    fetch_osculating_elements, build_period_record, save_cache -- is the
    real code. A question with no recorded answer is JPL not reached.

WHAT IT CHECKS, AND THE FAULT PLANTED FOR EACH

    The list used has the Sun, Mercury, Jupiter, the Pluto-Charon
    barycentre and Encke. Encke's entry writes no id_type, so plotting's
    default ('smallbody') is what makes its question match.

    1. Nothing missing: Mercury, Jupiter and Encke all fetched. No query
       is asked and the verdict is NOTHING MISSING; the Sun and the
       barycentre are named, with why.
       Planted: a fetched period treated as missing (asked again).
    2. One refresh, one new object: Mercury's period removed, Encke with
       no cache entry at all, Jupiter fetched.
       - The set names Mercury and Encke, by name, before any question.
         Planted: the set not printed.
       - Encke, with no cache entry, is in the set and fetched as a new
         entry. Planted: the set built only from bodies already cached.
       - Each is fetched by one call of fetch_osculating_elements with
         plotting's arguments: the entry's id, its id_type with
         'smallbody' when it writes none, the run's time, no centre,
         with_period=True. Planted: a record built another way (the
         period alone, beside the old elements: the brief's option B);
         and the id_type read as the export reads it, None when absent.
       - The record saved has the fields a plotted record has, at every
         level, and each field holds what JPL's answer and plotting's
         code put there, compared with Mercury's and Encke's recorded
         entries; only the dates it was written and the two-centre
         test's own date differ. Planted: the option B record above.
       - Jupiter is not asked and its entry is unchanged.
    3. JPL fails: Mercury's period query refused, Jupiter missing too.
       - UNREACHABLE names Mercury; nothing is saved for it; Jupiter is
         named as not asked and is not asked. Planted: the failure not
         recorded (read as a pass); a partial answer, elements without a
         period, treated as whole; the stop after a failure removed.
       - The elements query refused: UNREACHABLE for its elements.
    4. A save that does not stick reads back as not fetched: FAIL naming
       the body. Planted: the read-back removed.
    5. The two lists copied from plotting's pre-fetch filter
       (PLOTTED_TYPES, SKIP_NAMES) equal the ones in palomas_orrery.py, at
       both sites. Planted: a type removed from palomas_orrery.py's copy;
       and a source in which the filter cannot be found.

RUN COMMAND

    python test_period_fetch.py

    Open it in VS Code and click Run. orrery_maintenance_run.py runs it
    among the checkers, as "Period fetch suite", and it gates. It writes
    only to a throwaway folder. Its last line starts
    "PERIOD FETCH SUITE:".

Role: devtool
Domain: dev_tools

Module created: October 15, 2026 with Anthropic's Claude Opus 5.5
(L-444, the missing periods).
"""

import copy
import datetime
import json
import math
import os
import re
import shutil
import sys
import tempfile
import types
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import export_objects                    # noqa: E402
import orbit_data_manager                # noqa: E402
import orbital_period                    # noqa: E402
import osculating_cache_manager as ocm   # noqa: E402

ANSWERS = os.path.join(HERE, "documentation", "worksheets",
                       "period_fetch_answers_L444.json")
MODULE = os.path.join(HERE, "period_fetch.py")
ORRERY = os.path.join(HERE, "palomas_orrery.py")

LIST_ENTRIES = [
    {"name": "Sun", "key": "sun", "id": "10", "id_type": None,
     "horizons_name": "Sun (10)", "object_type": "fixed"},
    {"name": "Mercury", "key": "mercury", "id": "199", "id_type": None,
     "horizons_name": "Mercury (199)", "object_type": "orbital"},
    {"name": "Jupiter", "key": "jupiter", "id": "599", "id_type": None,
     "horizons_name": "Jupiter (599)", "object_type": "orbital"},
    {"name": "Pluto-Charon Barycenter", "key": "pluto_barycenter",
     "id": "9", "horizons_name": "Pluto System Barycenter (9)",
     "object_type": "barycenter"},
    # No id_type written: plotting's default 'smallbody' must be used.
    {"name": "Encke", "key": "encke", "id": "90000091",
     "horizons_name": "2P/Encke", "object_type": "orbital"},
]

# Fields a fresh fetch writes differently from the recorded one, and why.
NOT_COMPARED = {
    ("metadata", "fetched"): "the time it was written",
    ("period", "fetched"): "the day it was written",
    ("period", "test"): "a fresh fetch runs the two-centre test that day; "
                        "the recorded record carries an earlier test",
    ("elements", "solution_TP"): "added later by resolve_tp, not by the "
                                 "fetch (Encke)",
}


# ------------------------------------------------------------- harness

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


def load_answers():
    with open(ANSWERS, "r", encoding="utf-8") as handle:
        return json.load(handle)


def fixture_list(entries):
    lines = ["OBJECT_DEFINITIONS = ["]
    for e in entries:
        body = ", ".join("%r: %r" % (k, v) for k, v in e.items())
        lines.append("    {%s, 'mission_info': 'A body.', "
                     "'mission_url': None}," % body)
    lines.append("]")
    return "\n".join(lines) + "\n"


class World(object):
    """A throwaway folder holding the list and a cache, with the network
    replaced by the recorded answers, and every call of
    fetch_osculating_elements recorded."""

    def __init__(self, answers, cache, refuse=()):
        self.answers = answers["answers"]
        self.tmp = tempfile.mkdtemp(prefix="period_fetch_test_")
        os.makedirs(os.path.join(self.tmp, "data"))
        with open(os.path.join(self.tmp, "celestial_objects.py"), "w",
                  encoding="utf-8", newline="") as handle:
            handle.write(fixture_list(LIST_ENTRIES))
        self.write_cache(cache)
        self.refuse = set(refuse)
        self.calls = []
        self.log = []

    def write_cache(self, cache):
        with open(os.path.join(self.tmp, "data", "osculating_cache.json"),
                  "w", encoding="utf-8", newline="") as handle:
            json.dump(cache, handle, indent=2)

    def cache(self):
        with open(os.path.join(self.tmp, "data", "osculating_cache.json"),
                  "r", encoding="utf-8") as handle:
            return json.load(handle)

    def __enter__(self):
        data = Path(self.tmp) / "data"
        self.saved = {
            (ocm, "CACHE_FILE"): ocm.CACHE_FILE,
            (ocm, "BACKUP_FILE"): ocm.BACKUP_FILE,
            (ocm, "BACKUP_OLD"): ocm.BACKUP_OLD,
            (ocm, "TEMP_FILE"): ocm.TEMP_FILE,
            (ocm, "fetch_osculating_elements"): ocm.fetch_osculating_elements,
            (orbit_data_manager, "query_horizons_elements"):
                orbit_data_manager.query_horizons_elements,
            (orbital_period, "query_period_pair"):
                orbital_period.query_period_pair,
            (orbital_period, "fetch_sbdb_period_sigma"):
                orbital_period.fetch_sbdb_period_sigma,
        }
        ocm.CACHE_FILE = data / "osculating_cache.json"
        ocm.BACKUP_FILE = data / "osculating_cache_backup.json"
        ocm.BACKUP_OLD = data / "osculating_cache_backup_old.json"
        ocm.TEMP_FILE = data / "osculating_cache.tmp"
        real_fetch = self.saved[(ocm, "fetch_osculating_elements")]
        world = self

        def spy(obj_name, horizons_id=None, id_type='smallbody', date=None,
                center_body=None, with_period=False):
            world.calls.append({"name": obj_name, "horizons_id": horizons_id,
                                "id_type": id_type, "date": date,
                                "center_body": center_body,
                                "with_period": with_period})
            world.log.append("FETCH %s" % obj_name)
            return real_fetch(obj_name, horizons_id=horizons_id,
                              id_type=id_type, date=date,
                              center_body=center_body,
                              with_period=with_period)

        def elements(horizons_id, id_type='smallbody', date_str=None,
                     center_body=None):
            key = "%s|%s|%s|%s" % (horizons_id, id_type, date_str,
                                   center_body)
            if ("elements", horizons_id) in world.refuse:
                raise RuntimeError("planted: JPL refused %s" % key)
            if key not in world.answers["elements"]:
                raise RuntimeError("no recorded answer for elements %s" % key)
            return copy.deepcopy(world.answers["elements"][key]["answer"])

        def pair(horizons_id, id_type, date_str, location):
            key = "%s|%s|%s|%s" % (horizons_id, id_type, date_str, location)
            if ("period", horizons_id) in world.refuse:
                raise RuntimeError("planted: JPL refused %s" % key)
            if key not in world.answers["period_pairs"]:
                raise RuntimeError("no recorded answer for period %s" % key)
            return copy.deepcopy(world.answers["period_pairs"][key]["answer"])

        def sbdb(search):
            if search not in world.answers["sbdb"]:
                return None, "SBDB not reached (no recorded answer)", None
            return tuple(world.answers["sbdb"][search]["answer"])

        ocm.fetch_osculating_elements = spy
        orbit_data_manager.query_horizons_elements = elements
        orbital_period.query_period_pair = pair
        orbital_period.fetch_sbdb_period_sigma = sbdb
        return self

    def __exit__(self, *exc):
        for (module, name), value in self.saved.items():
            setattr(module, name, value)
        shutil.rmtree(self.tmp, ignore_errors=True)
        return False

    def echo(self, text):
        self.log.append(text)


def module_from(source, label):
    mod = types.ModuleType("period_fetch_" + label)
    mod.__file__ = MODULE
    exec(compile(source, MODULE + " [" + label + "]", "exec"), mod.__dict__)
    return mod


def plant(source, old, new, label):
    n = source.count(old)
    if n != 1:
        raise SystemExit("ANCHOR FAIL for planted fault '%s': %d matches"
                         % (label, n))
    return module_from(source.replace(old, new), label)


def when_of(answers):
    return datetime.datetime.strptime(answers["when"], "%Y-%m-%dT%H:%M:%S")


def strip_period(entry):
    out = copy.deepcopy(entry)
    out.pop("period", None)
    return out


# ------------------------------------------------------------- scenarios

def scenario_nothing(mod, answers):
    frozen = answers["inputs"]["cache"]
    with World(answers, copy.deepcopy(frozen)) as w:
        code, s = mod.run(w.tmp, when_of(answers), echo=w.echo)
        return {"code": code, "s": s, "calls": list(w.calls),
                "log": list(w.log)}


def scenario_refresh_new(mod, answers):
    frozen = answers["inputs"]["cache"]
    cache = {"Mercury": strip_period(frozen["Mercury"]),
             "Jupiter": copy.deepcopy(frozen["Jupiter"])}
    with World(answers, cache) as w:
        code, s = mod.run(w.tmp, when_of(answers), echo=w.echo)
        return {"code": code, "s": s, "calls": list(w.calls),
                "log": list(w.log), "cache": w.cache()}


def scenario_fail(mod, answers, refuse):
    frozen = answers["inputs"]["cache"]
    cache = {"Mercury": strip_period(frozen["Mercury"]),
             "Jupiter": strip_period(frozen["Jupiter"]),
             "Encke": copy.deepcopy(frozen["Encke"])}
    before = copy.deepcopy(cache)
    with World(answers, cache, refuse=refuse) as w:
        code, s = mod.run(w.tmp, when_of(answers), echo=w.echo)
        return {"code": code, "s": s, "calls": list(w.calls),
                "log": list(w.log), "cache": w.cache(), "before": before}


def scenario_no_stick(mod, answers):
    frozen = answers["inputs"]["cache"]
    cache = {"Mercury": strip_period(frozen["Mercury"]),
             "Jupiter": copy.deepcopy(frozen["Jupiter"]),
             "Encke": copy.deepcopy(frozen["Encke"])}
    with World(answers, cache) as w:
        code, s = mod.run(w.tmp, when_of(answers), echo=w.echo,
                          save=lambda entry, got: None)
        return {"code": code, "s": s, "calls": list(w.calls),
                "log": list(w.log)}


# ------------------------------------------------------------- judges
# Each returns a list of findings; empty means the check passed.

def verdict_line(r):
    return next((l for l in r["log"] if l.startswith("PERIOD FETCH:")), "")


def judge_nothing(r):
    out = []
    if r["calls"]:
        out.append("asked again: %s" % ", ".join(c["name"] for c in r["calls"]))
    if not verdict_line(r).startswith("PERIOD FETCH: NOTHING MISSING"):
        out.append("verdict was %r" % verdict_line(r))
    if r["code"] != 0:
        out.append("exit %s" % r["code"])
    text = "\n".join(r["log"])
    for name in ("Sun", "Pluto-Charon Barycenter"):
        if ("Not fetched here: %s" % name) not in text:
            out.append("%s not named as skipped" % name)
    return out


def judge_set_printed(r):
    out = []
    try:
        first = next(i for i, l in enumerate(r["log"]) if l.startswith("FETCH "))
    except StopIteration:
        return ["nothing was fetched"]
    head = r["log"][:first]
    for name, why in (("Mercury", "typed period, not fetched from JPL"),
                      ("Encke", "no cache entry yet")):
        if not any(l.strip().startswith(name) and why in l for l in head):
            out.append("%s (%s) not printed before the first question"
                       % (name, why))
    return out


def judge_new_object(r):
    out = []
    if "Encke" not in r["s"].get("missing", []):
        out.append("Encke, with no cache entry, is not in the set")
    if "Encke" not in r["s"].get("new", []):
        out.append("Encke not fetched as a new entry")
    if "period" not in (r.get("cache") or {}).get("Encke", {}):
        out.append("Encke has no period in the cache after the run")
    return out


def judge_args(r, answers):
    when = when_of(answers)
    want = [
        {"name": "Mercury", "horizons_id": "199", "id_type": None,
         "date": when, "center_body": None, "with_period": True},
        {"name": "Encke", "horizons_id": "90000091", "id_type": "smallbody",
         "date": when, "center_body": None, "with_period": True},
    ]
    if r["calls"] != want:
        return ["fetch_osculating_elements was called %r, plotting's call is %r"
                % (r["calls"], want)]
    return []


def _close(a, b):
    if isinstance(a, float) or isinstance(b, float):
        try:
            return math.isclose(float(a), float(b), rel_tol=1e-9,
                                abs_tol=1e-12)
        except (TypeError, ValueError):
            return False
    return a == b


def compare(level, got, want, out):
    if not isinstance(got, dict) or not isinstance(want, dict):
        out.append("%s: %r, recorded %r" % (level, type(got).__name__,
                                           type(want).__name__))
        return
    gk = set(k for k in got if (level, k) not in NOT_COMPARED)
    wk = set(k for k in want if (level, k) not in NOT_COMPARED)
    if gk != wk:
        out.append("%s: fields %s missing, %s extra" % (
            level, sorted(wk - gk), sorted(gk - wk)))
    for k in sorted(gk & wk):
        g, v = got[k], want[k]
        if isinstance(g, dict) and isinstance(v, dict):
            compare(k if level == "entry" else "%s.%s" % (level, k), g, v, out)
        elif not _close(g, v):
            out.append("%s.%s: %r, recorded %r" % (level, k, g, v))


def judge_record(r, answers):
    out = []
    frozen = answers["inputs"]["cache"]
    cache = r.get("cache") or {}
    for name in ("Mercury", "Encke"):
        if name not in cache:
            out.append("%s not in the cache" % name)
            continue
        compare("entry", cache[name], frozen[name], out)
    return out


def judge_jupiter_untouched(r, answers):
    frozen = answers["inputs"]["cache"]["Jupiter"]
    out = []
    if any(c["name"] == "Jupiter" for c in r["calls"]):
        out.append("Jupiter, already fetched, was asked")
    if (r.get("cache") or {}).get("Jupiter") != frozen:
        out.append("Jupiter's entry changed")
    return out


def judge_pass(r):
    line = verdict_line(r)
    want = ("PERIOD FETCH: PASS -- fetched 2: Mercury, Encke; elements "
            "refreshed for: Mercury; new cache entries: Encke")
    return [] if (line == want and r["code"] == 0) else [
        "verdict %r exit %s, expected %r exit 0" % (line, r["code"], want)]


def judge_fail(r, part):
    out = []
    line = verdict_line(r)
    if not line.startswith("PERIOD FETCH: UNREACHABLE -- JPL could not be "
                           "reached for Mercury"):
        out.append("verdict was %r" % line)
    if "not asked today: Jupiter" not in line:
        out.append("Jupiter not named as not asked")
    if r["code"] != 1:
        out.append("exit %s" % r["code"])
    if [c["name"] for c in r["calls"]] != ["Mercury"]:
        out.append("asked %s; after Mercury failed nothing more may be asked"
                   % [c["name"] for c in r["calls"]])
    if r["cache"] != r["before"]:
        moved = [k for k in r["before"] if r["cache"].get(k) != r["before"][k]]
        out.append("the cache changed for %s" % ", ".join(moved or ["?"]))
    if ("could not reach JPL for %s" % part) not in "\n".join(r["log"]):
        out.append("the line does not say %s could not be fetched" % part)
    return out


def judge_no_stick(r):
    line = verdict_line(r)
    if (line.startswith("PERIOD FETCH: FAIL -- Mercury: saved but reads back")
            and r["code"] == 1):
        return []
    return ["verdict %r exit %s" % (line, r["code"])]


# ------------------------------------------------------------- filter

FILTER_TYPES = re.compile(
    r"obj\.get\('object_type'\) in (\[[^\]]*'lagrange_point'[^\]]*\])")
FILTER_SKIP = re.compile(r"^\s*SKIP_HORIZONS_PREFETCH = (\[[^\]]*\])", re.M)


def judge_filter(mod, orrery_text):
    import ast as _ast
    out = []
    types_found = FILTER_TYPES.findall(orrery_text)
    skips_found = FILTER_SKIP.findall(orrery_text)
    if len(types_found) != 2:
        out.append("palomas_orrery.py: found the pre-fetch type list %d times, "
                   "expected 2 (the static plot and the animation)"
                   % len(types_found))
    if len(skips_found) != 2:
        out.append("palomas_orrery.py: found SKIP_HORIZONS_PREFETCH %d times, "
                   "expected 2" % len(skips_found))
    for text in types_found:
        if tuple(_ast.literal_eval(text)) != tuple(mod.PLOTTED_TYPES):
            out.append("PLOTTED_TYPES %r, palomas_orrery.py %s"
                       % (mod.PLOTTED_TYPES, text))
    for text in skips_found:
        if tuple(_ast.literal_eval(text)) != tuple(mod.SKIP_NAMES):
            out.append("SKIP_NAMES %r, palomas_orrery.py %s"
                       % (mod.SKIP_NAMES, text))
    return out


# ------------------------------------------------------------- faults

OPTION_B_OLD = (
    '    return ocm.fetch_osculating_elements(\n'
    '        entry["name"],\n'
    '        horizons_id=entry["horizons_id"],\n'
    '        id_type=entry["id_type"],\n'
    '        date=when,\n'
    '        center_body=None,\n'
    '        with_period=True,\n'
    '    )\n')
OPTION_B_NEW = (
    '    from orbital_period import build_period_record\n'
    '    old = ocm.load_cache().get(entry["name"]) or {}\n'
    '    from orbit_data_manager import utc_to_tdb\n'
    '    return {"elements": old.get("elements"),\n'
    '            "metadata": old.get("metadata"),\n'
    '            "period": build_period_record(\n'
    '                entry["horizons_id"], entry["id_type"],\n'
    '                utc_to_tdb(when).strftime("%Y-%m-%d %H:%M"), "@sun")}\n')


FAULTS = [
    # (label, old, new, which judge catches it)
    ("asked again: a fetched period treated as missing",
     '        if block.get("kind") == "fetched":\n'
     '            have.append(entry)\n'
     '            continue\n', '', "nothing"),
    ("the set not printed before asking",
     '    for entry, why in missing:\n'
     '        echo("  %-24s %s" % (entry["name"], why))\n', '', "set"),
    ("a new object missed: the set built only from cached bodies",
     '        block, _inputs = export_objects.period_block(\n'
     '            entry["name"], entry["object_type"], cache, typed)\n',
     '        if entry["name"] not in cache:\n'
     '            continue\n'
     '        block, _inputs = export_objects.period_block(\n'
     '            entry["name"], entry["object_type"], cache, typed)\n',
     "new"),
    ("another path than plotting's: the period alone beside the old "
     "elements (option B)",
     OPTION_B_OLD, OPTION_B_NEW,
     "args+record"),
    ("the same option B record, judged by the field comparison alone",
     OPTION_B_OLD, OPTION_B_NEW, "record"),
    ("the id_type read the export's way (None when absent)",
     '"id_type": fields.get("id_type", "smallbody"),',
     '"id_type": fields.get("id_type"),', "args"),
    ("a failed fetch read as a pass: the failure not recorded",
     '            down = name\n            continue\n',
     '            continue\n', "fail_period"),
    ("a partial answer treated as whole: elements without a period",
     '        if not complete(got):\n',
     '        if got is None:\n', "fail_period"),
    ("the stop after a failure removed: more asked the same day",
     '        if down is not None:\n            continue\n', '', "fail_period"),
    ("the read-back removed: a save that did not stick passes",
     '        if not block or block.get("kind") != "fetched":\n',
     '        if False:\n', "no_stick"),
]


def run_judge(which, mod, answers):
    """Findings for one judge kind on one module."""
    if which == "nothing":
        return judge_nothing(scenario_nothing(mod, answers))
    if which in ("set", "new", "args", "record", "args+record", "pass",
                 "jupiter"):
        r = scenario_refresh_new(mod, answers)
        found = []
        if which == "set":
            found = judge_set_printed(r)
        elif which == "new":
            found = judge_new_object(r)
        elif which == "args":
            found = judge_args(r, answers)
        elif which == "record":
            found = judge_record(r, answers)
        elif which == "args+record":
            found = judge_args(r, answers) + judge_record(r, answers)
        elif which == "pass":
            found = judge_pass(r)
        elif which == "jupiter":
            found = judge_jupiter_untouched(r, answers)
        return found
    if which == "fail_period":
        return judge_fail(scenario_fail(mod, answers,
                                        {("period", "199")}), "its period")
    if which == "fail_elements":
        return judge_fail(scenario_fail(mod, answers,
                                        {("elements", "199")}), "its elements")
    if which == "no_stick":
        return judge_no_stick(scenario_no_stick(mod, answers))
    raise ValueError(which)


class Quiet(object):
    """The fetch code prints its own progress; kept off the test's
    output, and printed only if a check fails."""

    def __enter__(self):
        import io
        self.buf = io.StringIO()
        self.old = sys.stdout
        sys.stdout = self.buf
        return self

    def __exit__(self, *exc):
        sys.stdout = self.old
        return False


def main():
    answers = load_answers()
    with open(MODULE, "r", encoding="utf-8") as handle:
        source = handle.read().replace("\r\n", "\n")
    with open(ORRERY, "r", encoding="utf-8") as handle:
        orrery_text = handle.read().replace("\r\n", "\n")
    real = module_from(source, "real")
    t = Tally()

    print("=" * 70)
    print("  PERIOD FETCH SUITE (L-444)")
    print("=" * 70)
    print("Answers: %s (built on %s)"
          % (os.path.relpath(ANSWERS, HERE).replace(os.sep, "/"),
             answers["built_on"][:8]))
    print("")
    print("Planted faults, each in a copy of period_fetch.py, each caught:")
    for label, old, new, which in FAULTS:
        mod = plant(source, old, new, label)
        found = []
        with Quiet() as q:
            for kind in which.split("+"):
                found.extend(run_judge(kind, mod, answers))
        t.check(bool(found), "%s -- caught: %s"
                % (label, found[0] if found else "NOT CAUGHT"))
    bad_orrery = orrery_text.replace("'orbital', 'satellite', 'trajectory'",
                                     "'orbital', 'trajectory'", 1)
    found = judge_filter(real, bad_orrery)
    t.check(bool(found), "plotting's filter changed, the copy not -- caught: %s"
            % (found[0] if found else "NOT CAUGHT"))
    found = judge_filter(real, "nothing here\n")
    t.check(bool(found), "plotting's filter not found -- caught: %s"
            % (found[0] if found else "NOT CAUGHT"))

    print("")
    print("The real period_fetch.py:")
    cases = [
        ("nothing missing: no query, NOTHING MISSING, Sun and barycentre "
         "named", "nothing"),
        ("the set printed by name before the first question", "set"),
        ("Encke, with no cache entry, in the set and fetched new", "new"),
        ("each body fetched by plotting's call, with plotting's arguments",
         "args"),
        ("the saved records match plotting's recorded ones, field by field",
         "record"),
        ("Jupiter, already fetched, not asked and unchanged", "jupiter"),
        ("the verdict names what was fetched, refreshed and new", "pass"),
        ("period refused: UNREACHABLE, nothing saved, nothing more asked",
         "fail_period"),
        ("elements refused: UNREACHABLE, nothing saved, nothing more asked",
         "fail_elements"),
        ("a save that does not stick: FAIL, naming the body", "no_stick"),
    ]
    for label, which in cases:
        with Quiet() as q:
            found = run_judge(which, real, answers)
        t.check(not found, label + ("" if not found else " -- " + "; ".join(found)))
        if found:
            print(q.buf.getvalue())
    found = judge_filter(real, orrery_text)
    t.check(not found, "PLOTTED_TYPES and SKIP_NAMES equal palomas_orrery.py's "
            "pre-fetch filter at both sites" + ("" if not found else
                                                 " -- " + "; ".join(found)))

    print("")
    if t.failed:
        print("PERIOD FETCH SUITE: FAIL -- %d of %d: %s"
              % (len(t.failed), t.passed + len(t.failed), "; ".join(t.failed)))
        return 1
    print("PERIOD FETCH SUITE: pass -- %d checks, every planted fault caught "
          "(%d planted)" % (t.passed, len(FAULTS) + 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
