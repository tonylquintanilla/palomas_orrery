"""
test_horizons_unserved.py -- the unserved entries' half of the Horizons
check (L-539, horizons_unserved.py) on JPL's recorded answers, with no
network: each planted fault is caught by name.

WHY THIS EXISTS

    A pass that could not have been a fail proves nothing (A Check That
    Cannot Fail Is Not Passing). So each rule the brief and the
    coordinating session's go-ahead of 2026-11-22 set is shown failing on
    a planted case before the agreeing run is trusted.

THE ANSWERS

    documentation/worksheets/horizons_answers_L539.json. Its "answers"
    are JPL's Lookup answers, both indexes, for 501 (Io), 3013 (the L3
    case: no major body, the asteroid 3013 Dobrovoleva), -170 (JWST), 999
    (Pluto), 120136199 (Dysnomia) and 99999999 (nothing), fetched
    2026-11-22 on Tony's machine, word for word. Its "constructed"
    answers are not JPL's, and each says what it stands for: an id two
    major bodies answer, an empty small-body index, and Io's answer with
    its name, then its kind, changed. A query with no answer is "could
    not reach JPL", so no test passes on an answer nobody recorded.

WHAT IT CHECKS, EACH PLANTED FAULT CAUGHT BY NAME

    a. The rule. A fixture list sorts into served, asked, never asked,
       no JPL id and unsorted. Planted: an entry that fits neither side
       (id_type 'barycenter' on a moon), and two entries with one name;
       each fails the run by name.
    b. The code's skips. The check's NOT_ASKED_IDS and NOT_ASKED_TYPES
       equal what palomas_orrery.py and palomas_orrery_helpers.py write
       inline. Planted: the code with one kind dropped from one list, and
       the check with a kind added; each named.
    c. One id. Io, JWST, Pluto and Dysnomia answer, with JPL's name and
       kind. Planted: 3013 as 'majorbody' FALLS THROUGH to 3013
       Dobrovoleva (the L3 case, the go-ahead's point 2); an id two
       objects answer; an id nothing answers.
    d. The run, in a throwaway folder. The first run stores each name and
       kind; Io, Pluto and Dysnomia mark themselves (names equal), JWST
       and a planted near-match ('io', capital dropped) do not. A second
       run the same day asks nothing. JPL's name changed, then its kind
       changed: DIFFERS by name, exit 0, the verdict line saying JPL
       DIFFERS; put back, the difference ends. JPL unreachable:
       UNREACHABLE by name, nothing recorded, no failed identity. A
       failed first answer (3013) is a FAIL, not stored.
    e. The spread. Twelve entries confirmed 21 days ago: ten are asked,
       two wait their turn. At day 30 the offline checker is red, at
       night too.
    f. The mark and the offline checker. By day an entry waiting on
       Tony's look is red, "waiting on your look"; at night it passes,
       named. Marked by mark(), it passes by day. A differing entry
       passes at night and is red by day. Planted: a mark on an entry
       never answered is refused.
    g. The night. The record is on the night's allow-list (the files the
       Horizons check writes, against the files the night declares).
       Planted: the rows with the record left off, caught by name. The
       title flags JPL DIFFERS and NEW JPL NAME are raised from the
       Horizons check's row only. The night's lists name what differs
       and what waits.
    h. The list for Tony: names that differ come first; the served
       entries, the entry with no JPL id and the entries never asked are
       named below.
    j. JPL has no object for this id (the ruling of 2026-11-22). MK2's
       id, which both lists miss and the main service refuses, is stored
       as that answer, never marks itself, and is named waiting; by day
       it is red until marked; marked, it passes while JPL still has
       nothing. Planted: it gains an object (a new name, waiting); a
       named entry, Io, loses its object (DIFFERS); both lists empty and
       the main service answering something else (fails by name).
    i. The real runs check the unserved half by default (hc.run and the
       offline checker's run, unserved=True), and the real list sorts
       with nothing unsorted and no name twice.

RUN COMMAND

    python test_horizons_unserved.py

    Open it in VS Code and click Run. The maintenance run runs it as
    section 8 of test_horizons_check.py (the Horizons check suite row).
    It writes only to a throwaway folder.

Role: devtool
Domain: dev_tools

Module created: November 22, 2026 with Anthropic's Claude Opus 5.5
(L-539, every entry checked). Updated the same day: section j, the
no-object answer, on the coordinating session's ruling after the first
live run; c's id nothing answers is now that answer.
"""

import ast
import datetime
import inspect
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import check_horizons_confirmations as offline  # noqa: E402
import horizons_check as hc  # noqa: E402
import horizons_unserved as hu  # noqa: E402

ANSWERS = os.path.join(HERE, "documentation", "worksheets",
                       "horizons_answers_L539.json")
TODAY = datetime.date(2026, 11, 22)

# name, id, id_type, object_type; None for a field not written
FIXTURE = [
    ("Io", "501", "majorbody", "satellite"),
    ("JamesWebb", "-170", "id", "trajectory"),
    ("Pluto", "999", None, "orbital"),
    ("Dysnomia", "120136199", "majorbody", "satellite"),
    ("io", "501", "majorbody", "satellite"),          # near-match: no self-mark
    ("Planet 9", "planet9_placeholder", None, "hypothetical"),
    ("TRAPPIST-1 b", "trappist1b", "exoplanet", "exoplanet"),
    ("6AC4721", "none", "smallbody", "orbital"),
]
SERVED_FIXTURE = "    {'name': 'Mars', 'key': 'mars', 'id': '499', " \
    "'horizons_name': 'Mars', 'object_type': 'orbital'},"


def fixture_text(rows, served=True):
    lines = ["OBJECT_DEFINITIONS = ["]
    if served:
        lines.append(SERVED_FIXTURE)
    for name, ident, id_type, otype in rows:
        lines.append("    {'name': %r, 'id': %r, 'id_type': %r, "
                     "'object_type': %r}," % (name, ident, id_type, otype))
    lines.append("]")
    return "\n".join(lines) + "\n"


def build_root(tmp, rows, served=False, sheet_day=TODAY):
    os.makedirs(os.path.join(tmp, "data"), exist_ok=True)
    with open(os.path.join(tmp, "celestial_objects.py"), "w",
              newline="") as handle:
        handle.write(fixture_text(rows, served))
    with open(os.path.join(tmp, "data", "osculating_cache.json"), "w") as h:
        json.dump({}, h)
    # JWST's data sheet read today, so the served half asks nothing.
    with open(os.path.join(tmp, hc.SHEETS), "w") as h:
        json.dump({"schema": 1, "sheets": {"-170": {
            "read": sheet_day.isoformat(), "revised": "Nov 20 2026",
            "stated": None, "rows": {}}}}, h)


def recorded(answers, extra=None, down=False, log=None):
    def fetch(url):
        if log is not None:
            log.append(url)
        if down:
            raise hc.Unreachable("planted: no network")
        if extra and url in extra:
            return extra[url]
        if url not in answers:
            raise hc.Unreachable("no recorded answer for %s" % url)
        return answers[url]
    return fetch


def age_all(tmp, when, days=hu.RENEW_FROM_DAYS + 1):
    """Every unserved record confirmed `days` before `when`, so due."""
    entries = hu.load_record(tmp)["entries"]
    for r in entries.values():
        r["confirmed"] = str(when - datetime.timedelta(days=days))
    hu.write_record(tmp, entries)


def entry_of(name, ident, id_type, otype):
    return {"name": name, "id": ident, "id_type": id_type,
            "object_type": otype, "line": 0}


# ------------------------------------------------------------- the code

def says_not_asked(body):
    """True when a block reports its skip as L-512 does:
    tell(report, NOT_ASKED, ...)."""
    for stmt in body:
        call = getattr(stmt, "value", None)
        if (isinstance(stmt, ast.Expr) and isinstance(call, ast.Call)
                and getattr(call.func, "id", None) == "tell"
                and len(call.args) > 1
                and getattr(call.args[1], "id", None) == "NOT_ASKED"):
            return True
    return False


def code_skips(sources):
    """What the fetch code skips, as it writes it inline.

    ids: every string an `if object_id == '...':` compares with, where
    the block reports tell(report, NOT_ASKED, ...) (the position and path
    fetches); id_types: the same for `if id_type == '...':`; kinds: every
    list of strings compared with in / not in that holds 'exoplanet' (the
    plot's and the animation's loops and pre-fetches). sources: {path:
    text}. Returns (ids, id_types, [(path, line, frozenset)])."""
    ids, id_types, kinds = set(), set(), []
    for path, text in sources.items():
        for node in ast.walk(ast.parse(text)):
            if (isinstance(node, ast.If) and says_not_asked(node.body)
                    and isinstance(node.test, ast.Compare)
                    and isinstance(node.test.left, ast.Name)
                    and len(node.test.ops) == 1
                    and isinstance(node.test.ops[0], ast.Eq)
                    and isinstance(node.test.comparators[0], ast.Constant)):
                value = node.test.comparators[0].value
                if node.test.left.id == "object_id":
                    ids.add(value)
                elif node.test.left.id == "id_type":
                    id_types.add(value)
            if not isinstance(node, ast.Compare):
                continue
            for op, right in zip(node.ops, node.comparators):
                if (isinstance(op, (ast.In, ast.NotIn))
                        and isinstance(right, (ast.List, ast.Tuple))):
                    words = [e.value for e in right.elts
                             if isinstance(e, ast.Constant)]
                    if "exoplanet" in words and len(words) > 1:
                        kinds.append((path, node.lineno, frozenset(words)))
    return ids, id_types, kinds


def skip_disagreements(skips, our_ids, our_types):
    ids, id_types, kinds = skips
    out = []
    if ids != set(our_ids):
        out.append("the code skips the ids %s; the check names %s"
                   % (sorted(ids), sorted(our_ids)))
    for word in sorted(id_types - set(our_types)):
        out.append("the code skips the id_type %r, which is not a kind the "
                   "check names" % word)
    for path, line, words in kinds:
        if words != frozenset(our_types):
            out.append("%s line %d skips %s; the check names %s"
                       % (os.path.basename(path), line, sorted(words),
                          sorted(our_types)))
    if not kinds:
        out.append("no inline list of the exoplanet kinds was found in the "
                   "code: the reader no longer sees the skip")
    return out


def read_sources():
    out = {}
    for name in ("palomas_orrery.py", "palomas_orrery_helpers.py"):
        with open(os.path.join(HERE, name), "rb") as handle:
            out[name] = handle.read().decode("utf-8").replace("\r\n", "\n")
    return out


# ------------------------------------------------------------- the night

def written_not_declared(gens):
    """The records the Horizons check writes (git tracks them) that the
    night's allow-list for these rows does not carry."""
    import orrery_maintenance_run as runner
    allowed = runner.night_allow_list(gens)
    writes = [hc.CONFIRMATIONS, hc.SHEETS, hu.RECORD]
    return [w.replace(os.sep, "/") for w in writes
            if w.replace(os.sep, "/") not in allowed]


# ------------------------------------------------------------- the tests

def section(t):
    with open(ANSWERS, "r", encoding="utf-8") as handle:
        recorded_answers = json.load(handle)
    answers = recorded_answers["answers"]
    made = dict((k, v["answer"]) for k, v in
                recorded_answers["constructed"].items())
    fetch = recorded(answers)
    quiet = lambda *a: None  # noqa: E731

    print("  a. the rule")
    sides = hu.sort_entries([dict(entry_of(*r), line=i + 1)
                             for i, r in enumerate(FIXTURE)])
    t.check([e["name"] for e in sides["asked"]]
            == ["Io", "JamesWebb", "Pluto", "Dysnomia", "io"]
            and [e["name"] for e, _w in sides["not_asked"]]
            == ["Planet 9", "TRAPPIST-1 b"]
            and [e["name"] for e, _w in sides["no_id"]] == ["6AC4721"]
            and not sides["unsorted"] and not sides["duplicates"],
            "the fixture sorts: asked %s; never asked %s; no JPL id %s"
            % ([e["name"] for e in sides["asked"]],
               [e["name"] for e, _w in sides["not_asked"]],
               [e["name"] for e, _w in sides["no_id"]]))
    odd = hu.sort_entries([entry_of("Odd moon", "5", "barycenter",
                                    "satellite")])
    t.check([e["name"] for e, _w in odd["unsorted"]] == ["Odd moon"],
            "planted: an entry that fits neither side is unsorted, by name: "
            "%s" % [(e["name"], w) for e, w in odd["unsorted"]])
    twice = hu.sort_entries([dict(entry_of("Io", "501", "majorbody",
                                           "satellite"), line=3),
                             dict(entry_of("Io", "502", "majorbody",
                                           "satellite"), line=9)])
    t.check(twice["duplicates"] == [("Io", [3, 9])],
            "planted: two entries named Io are named, lines %s"
            % twice["duplicates"])
    tmp = tempfile.mkdtemp(prefix="unserved_rule_")
    try:
        build_root(tmp, FIXTURE + [("Odd moon", "5", "barycenter",
                                    "satellite"),
                                   ("Io", "502", "majorbody", "satellite")])
        lines = []
        code, out = hc.run(tmp, fetch, TODAY, pause=0, echo=lines.append,
                           write=False)
        t.check(code == 1 and "Odd moon unsorted" in out["problems"]
                and "Io named twice" in out["problems"]
                and "Odd moon unsorted" in out["line"],
                "planted, in a run: both fail the run by name -- %s"
                % out["line"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("  b. the code's skips, read from the code")
    sources = read_sources()
    skips = code_skips(sources)
    ids, id_types, kinds = skips
    bad = skip_disagreements(skips, hu.NOT_ASKED_IDS, hu.NOT_ASKED_TYPES)
    t.check(not bad and ids == {"planet9_placeholder"}
            and id_types == {"exoplanet"},
            "the check's skips equal the code's: ids %s, id_types %s, %d "
            "inline lists of the exoplanet kinds%s"
            % (sorted(ids), sorted(id_types), len(kinds),
               "" if not bad else " -- " + "; ".join(bad)))
    planted_src = dict(sources)
    old = "['exoplanet', 'exo_host_star', 'exo_binary_star', 'exo_barycenter']"
    planted_src["palomas_orrery.py"] = sources["palomas_orrery.py"].replace(
        old, "['exoplanet', 'exo_host_star', 'exo_binary_star']", 1)
    bad = skip_disagreements(code_skips(planted_src), hu.NOT_ASKED_IDS,
                             hu.NOT_ASKED_TYPES)
    t.check(len(bad) == 1 and "palomas_orrery.py line" in bad[0],
            "planted: the code with a kind dropped from one list is named: %s"
            % bad)
    planted_src = dict(sources)
    planted_src["palomas_orrery.py"] = sources["palomas_orrery.py"].replace(
        "    if object_id == 'planet9_placeholder':",
        "    if object_id == 'planet9_placeholder' or object_id == 'x':", 1)
    planted_src["palomas_orrery_helpers.py"] = sources[
        "palomas_orrery_helpers.py"].replace(
        "    if object_id == 'planet9_placeholder':",
        "    if object_id == 'planet10_placeholder':", 1)
    bad = skip_disagreements(code_skips(planted_src), hu.NOT_ASKED_IDS,
                             hu.NOT_ASKED_TYPES)
    t.check(len(bad) == 1 and "planet10_placeholder" in bad[0],
            "planted: the code skipping another id is named: %s" % bad)
    bad = skip_disagreements(skips, hu.NOT_ASKED_IDS,
                             hu.NOT_ASKED_TYPES + ("satellite",))
    t.check(len(bad) == len(kinds) and bad,
            "planted: the check with a kind added disagrees at each of the "
            "%d lists" % len(bad))

    print("  c. one id at a time")
    for ident, id_type, name, kind in (
            ("501", "majorbody", "Io", "natural satellite"),
            ("-170", "id", "James Webb Space Telescope (spacecraft)",
             "spacecraft"),
            ("999", None, "Pluto", "planet"),
            ("120136199", "majorbody", "Dysnomia",
             "asteroidal system satellite")):
        r = hu.ask(ident, id_type, fetch)
        t.check(r["status"] == "answered" and r["jpl"]["name"] == name
                and r["jpl"]["kind"] == kind,
                "%s answers: %s (%s)" % (ident, (r["jpl"] or {}).get("name"),
                                         (r["jpl"] or {}).get("kind")))
    r = hu.ask("3013", "majorbody", fetch)
    t.check(r["status"] == "FAILS" and "FALLS THROUGH" in r["problem"]
            and "3013 Dobrovoleva" in r["problem"],
            "planted: 3013 as 'majorbody' falls through, by name: %s"
            % r["problem"])
    two = recorded(answers, extra={hc.lookup_url("777", "mb"):
                                   made["two_objects_mb"],
                                   hc.lookup_url("777", "sb"):
                                   made["nothing_sb"]})
    r = hu.ask("777", "majorbody", two)
    t.check(r["status"] == "FAILS" and "2 major bodies" in r["problem"],
            "planted: an id two objects answer: %s" % r["problem"])
    r = hu.ask("99999999", "majorbody", fetch)
    t.check(r["status"] == "absent" and r["jpl"]["name"] is None
            and "out of bounds" in r["jpl"]["answer"]
            and len(r["queries"]) == 3,
            "an id nothing answers, which JPL's main service refuses: %s "
            "(JPL: %s)" % (r["status"], (r["jpl"] or {}).get("answer")))
    blind = recorded(answers, extra={hu.main_url("99999999", "majorbody"):
                                     answers[hu.main_url("501",
                                                         "majorbody")]})
    r = hu.ask("99999999", "majorbody", blind)
    t.check(r["status"] == "FAILS" and "yet its main service answers"
            in r["problem"],
            "planted: both lists empty but the main service answering "
            "something else fails, by name: %s" % r["problem"])
    r = hu.ask("501", "majorbody", recorded(answers, down=True))
    t.check(r["status"] == "could not reach JPL",
            "JPL unreachable is not a failed identity: %s" % r["status"])

    print("  d. the run")
    tmp = tempfile.mkdtemp(prefix="unserved_run_")
    try:
        build_root(tmp, FIXTURE)
        lines = []
        code, out = hc.run(tmp, fetch, TODAY, pause=0, echo=lines.append)
        rec = hu.load_record(tmp)["entries"]
        t.check(code == 0 and sorted(rec) == ["Dysnomia", "Io", "JamesWebb",
                                              "Pluto", "io"]
                and rec["Io"]["jpl_name"] == "Io"
                and rec["Io"]["jpl_kind"] == "natural satellite",
                "the first run stores each name and kind: %s -- %s"
                % (sorted(rec), out["line"]))
        selfs = sorted(n for n, r in rec.items() if r.get("looked"))
        t.check(selfs == ["Dysnomia", "Io", "Pluto"],
                "the names that equal JPL's mark themselves (%s); JamesWebb "
                "and the planted near-match 'io' do not" % selfs)
        t.check("NEW JPL NAME 2 waiting on Tony's look: JamesWebb, io"
                in out["line"],
                "the verdict line names those waiting: %s" % out["line"])
        log = []
        code, out = hc.run(tmp, recorded(answers, log=log), TODAY, pause=0,
                           echo=quiet)
        t.check(code == 0 and not log and out["verdict"] == "NOTHING DUE",
                "a second run the same day asks nothing: %s, %d queries"
                % (out["verdict"], len(log)))
        # The served half's --all would re-read JWST's data sheet, which
        # has no recorded answer; so each run below makes the unserved
        # entries due by their age instead (age_all).
        later = TODAY + datetime.timedelta(days=1)
        renamed = recorded(answers, extra={hc.lookup_url("501", "mb"):
                                           made["io_renamed_mb"]})
        age_all(tmp, later)
        lines = []
        code, out = hc.run(tmp, renamed, later, pause=0, echo=lines.append)
        rec = hu.load_record(tmp)["entries"]
        t.check(code == 0 and rec["Io"]["differs"]
                and "name: Io -> Io (Jupiter I)" in rec["Io"]["differs"][
                    "causes"] and rec["Io"]["jpl_name"] == "Io"
                and "JPL DIFFERS Io since" in out["line"],
                "planted: JPL's name changed is DIFFERS by name, exit %d, the "
                "record kept -- %s" % (code, out["line"]))
        code, out = hc.run(tmp, fetch, later, pause=0, echo=quiet)
        rec = hu.load_record(tmp)["entries"]
        t.check(code == 0 and not rec["Io"]["differs"]
                and "JPL DIFFERS" not in out["line"],
                "put back, the difference ends: %s" % out["line"])
        reclassed = recorded(answers, extra={hc.lookup_url("501", "mb"):
                                             made["io_reclassed_mb"]})
        age_all(tmp, later)
        code, out = hc.run(tmp, reclassed, later, pause=0, echo=quiet)
        rec = hu.load_record(tmp)["entries"]
        t.check(code == 0 and rec["Io"]["differs"]
                and "kind: natural satellite -> planet"
                in rec["Io"]["differs"]["causes"],
                "planted: JPL's kind changed is DIFFERS by name: %s"
                % rec["Io"]["differs"]["causes"])
        hc.run(tmp, fetch, later, pause=0, echo=quiet)
        age_all(tmp, later)
        before = hu.load_record(tmp)
        code, out = hc.run(tmp, recorded(answers, down=True), later, pause=0,
                           echo=quiet)
        t.check(code == 1 and out["verdict"] == "UNREACHABLE"
                and not out["problems"]
                and hu.load_record(tmp) == before,
                "JPL unreachable: %s, nothing recorded, no failed identity"
                % out["verdict"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    tmp = tempfile.mkdtemp(prefix="unserved_l3_")
    try:
        build_root(tmp, [("Earth-Moon L3", "3013", "majorbody",
                          "lagrange_point")])
        lines = []
        code, out = hc.run(tmp, fetch, TODAY, pause=0, echo=lines.append)
        t.check(code == 1 and any(p.startswith("Earth-Moon L3.identity")
                                  and "3013 Dobrovoleva" in p
                                  for p in out["problems"])
                and "Earth-Moon L3" not in hu.load_record(tmp)["entries"],
                "planted, in a run: the L3 case fails by name and is not "
                "stored -- %s" % out["line"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("  e. the spread")
    tmp = tempfile.mkdtemp(prefix="unserved_spread_")
    try:
        many = [("Io %02d" % i, "501", "majorbody", "satellite")
                for i in range(12)]
        build_root(tmp, many)
        old = str(TODAY - datetime.timedelta(days=21))
        hu.write_record(tmp, dict(
            (n, {"id": "501", "id_type": "majorbody",
                 "object_type": "satellite", "first_answered": old,
                 "confirmed": old, "jpl_name": "Io",
                 "jpl_kind": "natural satellite", "looked": {"by": "test"},
                 "differs": None}) for n, _i, _t, _o in many))
        log = []
        code, out = hc.run(tmp, recorded(answers, log=log), TODAY, pause=0,
                           echo=quiet, write=False)
        t.check(len(log) == 2 * hu.PER_RUN
                and out["unserved"]["due"] == hu.PER_RUN,
                "twelve entries 21 days old: %d asked (%d queries), the rest "
                "wait their turn" % (out["unserved"]["due"], len(log)))
        late = TODAY + datetime.timedelta(days=9)
        fails = hu.offline(tmp, late, night=True, echo=quiet)
        t.check(len(fails) == 12 and all("30 days ago" in f for f in fails),
                "at day 30 the offline checker is red, at night too: %d named"
                % len(fails))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("  f. the mark and the offline checker")
    tmp = tempfile.mkdtemp(prefix="unserved_mark_")
    try:
        build_root(tmp, FIXTURE)
        hc.run(tmp, fetch, TODAY, pause=0, echo=quiet)
        day = hu.offline(tmp, TODAY, night=False, echo=quiet)
        night = hu.offline(tmp, TODAY, night=True, echo=quiet)
        t.check(sorted(f.split(":")[0] for f in day) == ["JamesWebb", "io"]
                and all("waiting on your look" in f for f in day)
                and night == [],
                "by day the two waiting are red, by name; at night they pass "
                "(%d by day, %d at night)" % (len(day), len(night)))
        lines = []
        code = offline.run(tmp, TODAY, echo=lines.append, night=False)
        t.check(code == 1 and any("JamesWebb: JPL names it" in s
                                  for s in lines),
                "the offline checker's own run names them: exit %d" % code)
        marked, already, refused = hu.mark(
            tmp, ["JamesWebb", "io", "Io", "Never"], "Tony's look: a test",
            TODAY)
        t.check(marked == ["JamesWebb", "io"] and [a[0] for a in already]
                == ["Io"] and [r[0] for r in refused] == ["Never"],
                "mark(): %s marked, %s already, %s refused"
                % (marked, [a[0] for a in already],
                   [r[0] for r in refused]))
        t.check(hu.offline(tmp, TODAY, night=False, echo=quiet) == [],
                "marked, they pass by day")
        rec = hu.load_record(tmp)
        rec["entries"]["Pluto"]["differs"] = {"since": TODAY.isoformat(),
                                              "causes": ["name: a -> b"]}
        hu.write_record(tmp, rec["entries"])
        day = hu.offline(tmp, TODAY, night=False, echo=quiet)
        night = hu.offline(tmp, TODAY, night=True, echo=quiet)
        t.check(len(day) == 1 and day[0].startswith("Pluto: JPL DIFFERS")
                and night == [],
                "an entry JPL differs on: red by day (%s), passes at night"
                % day)
        differs, waiting = hu.night_lists(tmp)
        t.check([d["name"] for d in differs] == ["Pluto"] and waiting == [],
                "the night's lists name it: differs %s, waiting %s"
                % ([d["name"] for d in differs], waiting))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("  g. the night")
    import orrery_maintenance_run as runner
    gens = runner.night_rows()[0]
    t.check(written_not_declared(gens) == [],
            "every record the Horizons check writes is on the night's "
            "allow-list, %s among them" % hu.RECORD.replace(os.sep, "/"))
    planted = [(r[0], r[1], [p for p in r[2] if "unserved" not in p])
               + tuple(r[3:]) if r[0] == "Horizons check" else r
               for r in gens]
    t.check(written_not_declared(planted)
            == [hu.RECORD.replace(os.sep, "/")],
            "planted: the night's rows with the record left off: %s"
            % written_not_declared(planted))
    tmp = tempfile.mkdtemp(prefix="unserved_night_")
    try:
        os.makedirs(os.path.join(tmp, "data"))
        with open(os.path.join(tmp, runner.NIGHT_RECORD), "w") as handle:
            json.dump({"rows": [
                {"row": "Horizons check", "verdict": "rewrote x -- PASS -- 2 "
                 "checked today, 4 queries; JPL DIFFERS Io since 2026-11-22; "
                 "NEW JPL NAME 1 waiting on Tony's look: io"},
                {"row": "Horizons check suite", "verdict": "pass -- "
                 "JPL DIFFERS and NEW JPL NAME tested"}]}, handle)
        flags = runner.night_title_flags(tmp)
        t.check(flags == "JPL DIFFERS NEW JPL NAME ",
                "the night's title flags, from the Horizons check row only: "
                "%r" % flags)
        with open(os.path.join(tmp, runner.NIGHT_RECORD), "w") as handle:
            json.dump({"rows": [{"row": "Horizons check suite", "verdict":
                                 "JPL DIFFERS NEW JPL NAME"}]}, handle)
        t.check(runner.night_title_flags(tmp) == "",
                "planted: the suite's words raise no flag")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("  h. the list for Tony")
    tmp = tempfile.mkdtemp(prefix="unserved_list_")
    try:
        build_root(tmp, FIXTURE + [("Hal", "501", "majorbody", "satellite")],
                   served=True)
        hu.run(tmp, fetch, TODAY, pause=0, echo=quiet)
        path, counts = hu.write_list(tmp, os.path.join(tmp, "list.md"),
                                     today=TODAY)
        with open(path, "r", encoding="ascii") as handle:
            text = handle.read()
        head = text.split("## Names that match")[0]
        t.check("- Hal -- 501 -- Io -- natural satellite" in head
                and "JamesWebb" not in head and counts["differ"] == 1
                and "The 1 entries the website serves" in text
                and "6AC4721, asked with no JPL id" in text
                and "Never asked of JPL (2): Planet 9, TRAPPIST-1 b" in text,
                "the names that differ come first (%d), the rest below (%d), "
                "and what is not on it is named" % (counts["differ"],
                                                    counts["match"]))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("  j. JPL has no object for this id (the ruling of 2026-11-22)")
    tmp = tempfile.mkdtemp(prefix="unserved_absent_")
    mk2 = [("MK2", "120136472", "majorbody", "satellite"),
           ("Io", "501", "majorbody", "satellite")]
    try:
        build_root(tmp, mk2)
        lines = []
        code, out = hc.run(tmp, fetch, TODAY, pause=0, echo=lines.append)
        rec = hu.load_record(tmp)["entries"]
        t.check(code == 0 and rec["MK2"]["absent"] is True
                and rec["MK2"]["looked"] is None
                and "NEW JPL NAME 1 waiting on Tony's look: MK2"
                in out["line"],
                "the first answer is stored as no object, never marks "
                "itself, and is named waiting: %s" % out["line"])
        day = hu.offline(tmp, TODAY, night=False, echo=quiet)
        t.check(day == ["MK2: %s; not yet looked at -- waiting on your look"
                        % hu.NO_OBJECT]
                and hu.offline(tmp, TODAY, night=True, echo=quiet) == [],
                "planted: an absent id not yet looked at stays red by day "
                "(%s), passes at night" % day)
        hu.mark(tmp, ["MK2"], "Tony's look: a test", TODAY)
        later = TODAY + datetime.timedelta(days=1)
        age_all(tmp, later)
        code, out = hc.run(tmp, fetch, later, pause=0, echo=quiet)
        rec = hu.load_record(tmp)["entries"]
        t.check(code == 0 and rec["MK2"]["confirmed"] == later.isoformat()
                and not rec["MK2"]["differs"]
                and hu.offline(tmp, later, echo=quiet) == [],
                "looked at, it is held: asked again, JPL still has nothing, "
                "it passes -- %s" % out["line"])
        age_all(tmp, later)
        found = recorded(answers, extra={hc.lookup_url("120136472", "mb"):
                                         made["mk2_found_mb"]})
        code, out = hc.run(tmp, found, later, pause=0, echo=quiet)
        rec = hu.load_record(tmp)["entries"]
        t.check(code == 0 and rec["MK2"]["absent"] is False
                and rec["MK2"]["jpl_name"] == "MK2"
                and rec["MK2"]["looked"] is None
                and not rec["MK2"]["differs"]
                and "NEW JPL NAME 1 waiting on Tony's look: MK2"
                in out["line"],
                "planted: an absent id that gains an object is a new name, "
                "waiting on Tony's look -- %s" % out["line"])
        age_all(tmp, later)
        lost = recorded(answers, extra={
            hc.lookup_url("501", "mb"): made["empty_mb"],
            hc.lookup_url("501", "sb"): made["nothing_sb"],
            hu.main_url("501", "majorbody"):
                answers[hu.main_url("120136472", "majorbody")]})
        code, out = hc.run(tmp, lost, later, pause=0, echo=quiet)
        rec = hu.load_record(tmp)["entries"]
        t.check(code == 0 and rec["Io"]["differs"]
                and rec["Io"]["differs"]["causes"]
                == ["name: Io -> %s" % hu.NO_OBJECT]
                and "JPL DIFFERS" in out["line"]
                and "Io since" in out["line"],
                "planted: a named entry that loses its object DIFFERS: %s"
                % (rec["Io"]["differs"] or {}).get("causes"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("  i. the real runs and the real list")
    t.check(inspect.signature(hc.run).parameters["unserved"].default is True
            and inspect.signature(offline.run).parameters[
                "unserved"].default is True,
            "horizons_check.run and the offline checker check the unserved "
            "entries by default")
    real = hu.sort_entries(hu.read_list(HERE))
    t.check(not real["unsorted"] and not real["duplicates"],
            "the real list: %d served, %d asked, %d never asked, %d with no "
            "JPL id, nothing unsorted, no name twice"
            % (len(real["served"]), len(real["asked"]),
               len(real["not_asked"]), len(real["no_id"])))


def main():
    sys.path.insert(0, HERE)
    import test_horizons_check as suite
    t = suite.Tally()
    print("The unserved entries' half of the Horizons check (L-539)")
    section(t)
    print("")
    print("%d checks passed, %d failed." % (t.passed, len(t.failed)))
    if t.failed:
        for label in t.failed:
            print("  - " + label)
        print("UNSERVED CHECK SUITE: FAIL")
        return 1
    print("UNSERVED CHECK SUITE: pass -- %d checks, every planted fault "
          "caught by name" % t.passed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
