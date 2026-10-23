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
    6. (L-445) Earth's period moves to the Earth-Moon barycentre. On a list
       of the Sun and Earth, with Earth's entry as L-444's live run wrote
       it (its period asked of 399), and JPL's answers for target 3 in
       documentation/worksheets/period_answers_L445.json:
       - Earth is named missing, "period asked of 399, now 3", before any
         question; re-fetched with plotting's call; its period asked of 3
         alone, around the centre JPL's own answers make steadier, with a
         fresh two-centre test; the record names target 3 and its words,
         and says why the elements fetch's PR, Earth's own, was not
         compared; Earth's elements stay Earth's; the next run asks
         nothing. Planted in period_fetch.py: the target not compared.
         Planted in orbital_period.py: the period asked of the body; the
         elements fetch's PR compared with another body's; the last
         record's centre choice kept across the change of target.
       - The drawn orbit stays Earth's, timed by the record's period; with
         the record around another centre, the barycentre's elements are
         still never drawn as Earth's. Planted: that guard removed.
       - Earth around the Earth-Moon barycentre is still asked of 399.
         Planted: the map applied around any centre.
       - A save that leaves the old target is FAIL; JPL refusing the query
         for 3 is UNREACHABLE and the last period, kept by the fetch, is
         not saved as a new one. Planted: each of those two checks
         removed.

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
Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5 (L-445,
Earth's period: part 6, Earth re-fetched from the Earth-Moon barycentre,
with eight planted faults, five of them in a copy of orbital_period.py;
the recorded records of part 2 carry the three fields L-445 adds.)
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
EARTH_ANSWERS = os.path.join(HERE, "documentation", "worksheets",
                             "period_answers_L445.json")
MODULE = os.path.join(HERE, "period_fetch.py")
OP_MODULE = os.path.join(HERE, "orbital_period.py")
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

# L-445: Earth alone beside the Sun, so its scenarios ask about nothing
# else.
EARTH_ENTRIES = [
    LIST_ENTRIES[0],
    {"name": "Earth", "key": "earth", "id": "399", "id_type": None,
     "horizons_name": "Earth", "object_type": "orbital"},
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

    def __init__(self, answers, cache, refuse=(), entries=None, op=None):
        self.answers = answers["answers"]
        self.tmp = tempfile.mkdtemp(prefix="period_fetch_test_")
        os.makedirs(os.path.join(self.tmp, "data"))
        with open(os.path.join(self.tmp, "celestial_objects.py"), "w",
                  encoding="utf-8", newline="") as handle:
            handle.write(fixture_list(entries or LIST_ENTRIES))
        # L-445: a copy of orbital_period.py with a fault planted in it
        # stands in for the real module while this world is open.
        self.op = op
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
        op = self.op or orbital_period
        self.real_op = sys.modules.get("orbital_period")
        sys.modules["orbital_period"] = op
        self.saved = {
            (ocm, "CACHE_FILE"): ocm.CACHE_FILE,
            (ocm, "BACKUP_FILE"): ocm.BACKUP_FILE,
            (ocm, "BACKUP_OLD"): ocm.BACKUP_OLD,
            (ocm, "TEMP_FILE"): ocm.TEMP_FILE,
            (ocm, "fetch_osculating_elements"): ocm.fetch_osculating_elements,
            (orbit_data_manager, "query_horizons_elements"):
                orbit_data_manager.query_horizons_elements,
            (op, "query_period_pair"): op.query_period_pair,
            (op, "fetch_sbdb_period_sigma"): op.fetch_sbdb_period_sigma,
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
        op.query_period_pair = pair
        op.fetch_sbdb_period_sigma = sbdb
        world.asked_pairs = []
        real_pair = pair

        def pair_logged(horizons_id, id_type, date_str, location):
            world.asked_pairs.append((str(horizons_id), location))
            return real_pair(horizons_id, id_type, date_str, location)
        op.query_period_pair = pair_logged
        return self

    def __exit__(self, *exc):
        for (module, name), value in self.saved.items():
            setattr(module, name, value)
        sys.modules["orbital_period"] = self.real_op
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


def scenario_earth(mod, earth, op=None, save=None, refuse=()):
    """L-445: Earth's entry as L-444's live run wrote it, its period asked
    of 399; the run must re-fetch it asked of 3. Then the same run again,
    which must ask nothing."""
    frozen = earth["inputs"]["cache"]
    with World(earth, copy.deepcopy(frozen), entries=EARTH_ENTRIES,
               op=op, refuse=refuse) as w:
        kw = {"echo": w.echo}
        if save is not None:
            kw["save"] = save
        code, s = mod.run(w.tmp, when_of(earth), **kw)
        first = {"code": code, "s": s, "calls": list(w.calls),
                 "log": list(w.log), "cache": w.cache(),
                 "pairs": list(w.asked_pairs), "op": op or orbital_period}
        w.calls[:] = []
        w.log[:] = []
        code2, s2 = mod.run(w.tmp, when_of(earth), echo=w.echo)
        first["again"] = {"code": code2, "s": s2, "calls": list(w.calls),
                          "log": list(w.log)}
        return first


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


# L-445 writes three fields the recorded entries predate. For a body whose
# period is its own: the target is its own id, with no words, and the
# elements fetch's PR is compared as before.
L445_FIELDS = {"Mercury": "199", "Encke": "90000091"}


def judge_record(r, answers):
    out = []
    frozen = answers["inputs"]["cache"]
    cache = r.get("cache") or {}
    for name in ("Mercury", "Encke"):
        if name not in cache:
            out.append("%s not in the cache" % name)
            continue
        want = copy.deepcopy(frozen[name])
        want["period"].update({"target": L445_FIELDS[name],
                               "target_label": None,
                               "elements_fetch_not_compared": None})
        compare("entry", cache[name], want, out)
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


def _change(pair):
    return abs(pair["p2"] - pair["p1"])


def judge_earth(r, earth):
    """Earth's period re-fetched from the Earth-Moon barycentre: named
    missing for that reason, asked of 3 alone, around the centre the
    two-centre test picks from JPL's own answers, with a fresh test, and
    no comparison with the elements fetch's PR, which is Earth's own."""
    out = []
    pairs = earth["answers"]["period_pairs"]
    date = earth["inputs"]["cache"]["Earth"]["period"]["epoch"]
    sun = pairs["3|None|%s|@sun" % date]["answer"]
    bary = pairs["3|None|%s|@0" % date]["answer"]
    centre, chosen = (("@0", bary) if _change(bary) < _change(sun)
                      else ("@sun", sun))
    head = r["log"][:next((i for i, l in enumerate(r["log"])
                           if l.startswith("FETCH ")), len(r["log"]))]
    if not any(l.strip().startswith("Earth") and
               "period asked of 399, now 3" in l for l in head):
        out.append("Earth not named missing with 'period asked of 399, now "
                   "3' before the first question")
    want = ("PERIOD FETCH: PASS -- fetched 1: Earth; elements refreshed for: "
            "Earth")
    if verdict_line(r) != want or r["code"] != 0:
        out.append("verdict %r exit %s, expected %r"
                   % (verdict_line(r), r["code"], want))
    asked = sorted(set(t for t, _c in r["pairs"]))
    if asked != ["3"]:
        out.append("the period was asked of %s, not 3 alone" % asked)
    rec = ((r.get("cache") or {}).get("Earth") or {}).get("period") or {}
    for field, value in (("target", "3"),
                         ("target_label", "the Earth-Moon center of mass"),
                         ("center", centre),
                         ("agrees_with_elements_fetch", None)):
        if rec.get(field) != value:
            out.append("the record's %s is %r, not %r"
                       % (field, rec.get(field), value))
    if not _close(rec.get("days"), chosen["p1"]):
        out.append("the record's days %r, JPL's PR for 3 around %s is %r"
                   % (rec.get("days"), centre, chosen["p1"]))
    test = rec.get("test") or {}
    if not (_close(test.get("@sun"), _change(sun))
            and _close(test.get("@0"), _change(bary))):
        out.append("the two-centre test %r is not target 3's (around the Sun "
                   "%r, the barycentre %r)" % (test, _change(sun),
                                              _change(bary)))
    why = rec.get("elements_fetch_not_compared") or ""
    if not ("399" in why and "3" in why.replace("399", "")):
        out.append("the record does not say why the elements fetch's PR was "
                   "not compared: %r" % why)
    el = ((r.get("cache") or {}).get("Earth") or {}).get("elements") or {}
    own = earth["answers"]["elements"]["399|None|%s|None" % date]["answer"]
    if not _close(el.get("a"), own["a"]):
        out.append("Earth's elements are not Earth's own (a %r, 399's %r)"
                   % (el.get("a"), own["a"]))
    again = r.get("again") or {}
    if again.get("calls") or not verdict_line(again).startswith(
            "PERIOD FETCH: NOTHING MISSING"):
        out.append("the next run asked again: %r" % verdict_line(again))
    return out


def judge_earth_drawing(r):
    """The drawn orbit stays Earth's own, around the Sun, with the record's
    period; and if the record named another centre, the barycentre's
    elements would still never be drawn as Earth's orbit."""
    out = []
    op = r["op"]
    cache = copy.deepcopy(r.get("cache") or {})
    entry = cache.get("Earth") or {}
    params = copy.deepcopy(entry.get("elements") or {})
    rec = entry.get("period") or {}
    if not params or not rec:
        return ["no Earth entry to draw"]
    got = op.drawing_orbit("Earth", "Sun", params, cache=cache)
    if got["elements"] is not params or tuple(got["offset_au"]) != (0.0, 0.0,
                                                                   0.0):
        out.append("Earth is drawn from other elements than its own")
    if not _close((got["period"] or {}).get("days"), rec.get("days")):
        out.append("Earth's markers are not timed by its record's period")
    moved = copy.deepcopy(cache)
    moved["Earth"]["period"]["center"] = "@0"
    got = op.drawing_orbit("Earth", "Sun", params, cache=moved)
    if got["elements"] is not params:
        out.append("with its period around the barycentre, Earth is drawn from "
                   "the barycentre's elements (a %r)"
                   % (got["elements"] or {}).get("a"))
    elif "Earth-Moon center of mass" not in (got["note"] or ""):
        out.append("the drawing's note does not say whose period it is: %r"
                   % got["note"])
    return out


def judge_map_scope(op):
    """The map applies only around the Sun: Earth's period around the
    Earth-Moon barycentre (a view's 'Earth@3') is still asked of 399."""
    asked = []

    def pair(horizons_id, id_type, date_str, location):
        asked.append((str(horizons_id), location))
        return {"p1": 27.3, "p2": 27.3, "step_days": 365.25, "e": 0.05,
                "targetname": "Earth (399)", "elements": None}
    real = op.query_period_pair
    op.query_period_pair = pair
    try:
        rec = op.build_period_record("399", None, "2026-10-15 10:52", "@3")
    finally:
        op.query_period_pair = real
    out = []
    if asked != [("399", "@3")]:
        out.append("Earth around the Earth-Moon barycentre was asked %r, not "
                   "399 around @3" % asked)
    if rec.get("target") != "399" or rec.get("target_label") is not None:
        out.append("its record names target %r, words %r"
                   % (rec.get("target"), rec.get("target_label")))
    return out


def judge_earth_refused(r):
    """JPL refuses the period query for 3: the fetch keeps the last period,
    asked of 399, which is not a new answer. UNREACHABLE, nothing saved."""
    out = []
    line = verdict_line(r)
    if not line.startswith("PERIOD FETCH: UNREACHABLE -- JPL could not be "
                           "reached for Earth"):
        out.append("verdict %r" % line)
    rec = ((r.get("cache") or {}).get("Earth") or {}).get("period") or {}
    if rec.get("target") is not None or rec.get("epoch") != "2026-10-15 10:52":
        out.append("the cache moved: Earth's period now target %r, epoch %r"
                   % (rec.get("target"), rec.get("epoch")))
    return out


def judge_earth_no_stick(r):
    line = verdict_line(r)
    if (line.startswith("PERIOD FETCH: FAIL -- Earth: saved but its period "
                        "reads back as asked of 399, not 3")
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
     'id_type = fields.get("id_type", "smallbody")\n',
     'id_type = fields.get("id_type")\n', "args"),
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


# L-445: faults planted in a copy of period_fetch.py, judged on Earth.
EARTH_FAULTS = [
    ("Earth's period asked of 399 kept: the target not compared",
     '        if block.get("kind") == "fetched" and block.get("target") != want:\n',
     '        if False:\n', "earth"),
    ("the last period kept on a refused query saved as a new answer",
     '        if complete(got) and fetched_target(\n',
     '        if False and fetched_target(\n', "earth_refused"),
    ("a save asked of the old target read back as fetched",
     '        if block.get("target") != wanted_target(entry, cache_now):\n',
     '        if False:\n', "earth_no_stick"),
]

# L-445: faults planted in a copy of orbital_period.py, with the real
# period_fetch.py, judged on Earth.
OP_FAULTS = [
    ("the period asked of the body, not the map's target",
     "    target = period_target(body, location)\n",
     "    target = body\n", "earth"),
    ("the elements fetch's PR compared with another body's period",
     "    if not own:\n        # L-445: the elements fetch asked the body",
     "    if False:\n        # L-445: the elements fetch asked the body",
     "earth"),
    ("the last record's centre choice kept across the change of target",
     "              % (body, record_target(previous, body), target), "
     "flush=True)\n        previous = None\n",
     "              % (body, record_target(previous, body), target), "
     "flush=True)\n", "earth"),
    ("the map applied around another centre (Earth around the Earth-Moon "
     "barycentre asked of 3)",
     "    if _is_heliocentric(location):\n        return PERIOD_TARGETS.get",
     "    if True:\n        return PERIOD_TARGETS.get", "map_scope"),
    ("the barycentre's elements drawn as Earth's orbit",
     "    if rec.get('target_label'):\n        # L-445: the record's elements",
     "    if False:\n        # L-445: the record's elements", "earth_drawing"),
]


def op_from(source, label):
    mod = types.ModuleType("orbital_period")
    mod.__file__ = OP_MODULE
    exec(compile(source, OP_MODULE + " [" + label + "]", "exec"), mod.__dict__)
    return mod


def plant_op(source, old, new, label):
    n = source.count(old)
    if n != 1:
        raise SystemExit("ANCHOR FAIL for planted fault '%s': %d matches"
                         % (label, n))
    return op_from(source.replace(old, new), label)


def run_earth_judge(which, mod, earth, op=None):
    if which == "earth":
        return judge_earth(scenario_earth(mod, earth, op=op), earth)
    if which == "earth_drawing":
        return judge_earth_drawing(scenario_earth(mod, earth, op=op))
    if which == "earth_no_stick":
        return judge_earth_no_stick(scenario_earth(
            mod, earth, op=op, save=lambda entry, got: None))
    if which == "map_scope":
        return judge_map_scope(op or orbital_period)
    if which == "earth_refused":
        return judge_earth_refused(scenario_earth(mod, earth, op=op,
                                                  refuse={("period", "3")}))
    raise ValueError(which)


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
    with open(EARTH_ANSWERS, "r", encoding="utf-8") as handle:
        earth = json.load(handle)
    with open(OP_MODULE, "r", encoding="utf-8") as handle:
        op_source = handle.read().replace("\r\n", "\n")
    with open(MODULE, "r", encoding="utf-8") as handle:
        source = handle.read().replace("\r\n", "\n")
    with open(ORRERY, "r", encoding="utf-8") as handle:
        orrery_text = handle.read().replace("\r\n", "\n")
    real = module_from(source, "real")
    t = Tally()

    print("=" * 70)
    print("  PERIOD FETCH SUITE (L-444, L-445)")
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
    for label, old, new, which in EARTH_FAULTS:
        mod = plant(source, old, new, label)
        with Quiet():
            found = run_earth_judge(which, mod, earth)
        t.check(bool(found), "%s -- caught: %s"
                % (label, found[0] if found else "NOT CAUGHT"))
    print("Planted faults, each in a copy of orbital_period.py, each caught:")
    for label, old, new, which in OP_FAULTS:
        op = plant_op(op_source, old, new, label)
        with Quiet():
            found = run_earth_judge(which, real, earth, op=op)
        t.check(bool(found), "%s -- caught: %s"
                % (label, found[0] if found else "NOT CAUGHT"))

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
    earth_cases = [
        ("Earth, its period asked of 399: named missing for that reason, "
         "re-fetched asked of 3 around the steadier centre, with a fresh "
         "two-centre test and no comparison with Earth's own PR; the next "
         "run asks nothing", "earth"),
        ("Earth's drawn orbit stays its own; the barycentre's elements are "
         "never drawn as Earth's", "earth_drawing"),
        ("Earth around the Earth-Moon barycentre is still asked of 399",
         "map_scope"),
        ("a save that leaves the old target: FAIL, naming Earth",
         "earth_no_stick"),
        ("the period query for 3 refused: UNREACHABLE, the last period kept "
         "is not saved as a new one", "earth_refused"),
    ]
    for label, which in earth_cases:
        with Quiet() as q:
            found = run_earth_judge(which, real, earth)
        t.check(not found, label + ("" if not found else
                                    " -- " + "; ".join(found)))
        if found:
            print(q.buf.getvalue())

    print("")
    if t.failed:
        print("PERIOD FETCH SUITE: FAIL -- %d of %d: %s"
              % (len(t.failed), t.passed + len(t.failed), "; ".join(t.failed)))
        return 1
    print("PERIOD FETCH SUITE: pass -- %d checks, every planted fault caught "
          "(%d planted, %d of them for Earth's period, L-445)"
          % (t.passed, len(FAULTS) + 2 + len(EARTH_FAULTS) + len(OP_FAULTS),
             len(EARTH_FAULTS) + len(OP_FAULTS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
