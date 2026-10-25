"""
test_path_plan.py -- the path plan, offline, against a made-up solar
system answered in JPL's own vector format (L-443, slice 2).

WHAT IT CHECKS

    A small list with two spacecraft and one served asteroid, and a fake
    Horizons that answers vector questions from simple motions: each
    planet on a circle, the Moon on a circle around Earth, the asteroid
    on a circle at 2.5 AU. Spacecraft A passes Earth at 30,000 km and
    10 km/s on 2025-03-01 12:17 TDB; spacecraft B passes the asteroid at
    500 km and 5 km/s on 2026-02-10 06:43, both off the hour so the
    minute pass is needed. Both relative paths are
    straight lines, so the nearest moment, distance and speed are known
    exactly.

      1. Each flyby is found, at its minute, distance and speed, with the
         window and step the orrery's encounter rule gives.
         Earth's is asked centred on Earth, the asteroid's around the Sun
         and differenced.
      2. A second run the same day asks JPL nothing.
      3. Thirty-one days later the plans are made again: the flybys, now
         more than 30 days old, are carried, not asked again, and none is
         doubled.
      4. A change to what a plan was made from (the list's dates) makes it
         again at once, in full; the span stays JPL's.
      5. JPL unreachable: UNREACHABLE by name, the previous plans kept,
         the file unchanged.
      6. A body JPL gives no positions for is named as not searched, and
         the run goes on.
      9. Each span is JPL's own, read from its refusals: Craft A's list
         end runs past the made-up JPL's data and is clipped, Craft B's
         list start comes before it and moves on.
      8. --preview plans a named, unkeyed spacecraft into its own file,
         names one not in the list, and leaves data/path_plans.json alone.
      7. Two planted faults must fail check 1: the backbone's step set to
         nothing (so no flyby can need finer steps), and the fine passes
         skipped (so the nearest minute is not found).
     10. As it goes: the first line comes before JPL is asked anything and
         names the paths due; then a line for each path's span, each
         body's positions and each flyby found.
     11. Each plan is saved as it is made: when Craft B is first looked
         at closely, Craft A's plan is already on disk. Planted fault:
         the plans written only at the end.
     12. The time limit: when it has passed, the next path is not started
         but named as left for the next run, and a run with no limit then
         plans it and asks nothing about the path already planned.
         Planted fault: the limit never passing.

RUN COMMAND

    Open this file in VS Code and click Run. It takes no arguments, and
    reaches no network.

        python test_path_plan.py

    The last line is "PATH PLAN SUITE: N of N checks passed" or names
    each failure.

Role: devtool
Domain: dev_tools

Module created: October 24, 2026 with Anthropic's Claude Opus 5.5
(L-443, slice 2).
Module updated: October 24, 2026, late night, with Anthropic's Claude
Opus 5.5 (L-443: checks 10 to 12, the lines as it goes, each plan saved
as it is made, the time limit, two of them with a planted fault).
"""

import datetime
import json
import math
import os
import re
import shutil
import sys
import tempfile
import urllib.parse

import horizons_check as hc
import path_plan as pp

AU = pp.AU_KM
DAY = 86400.0

LIST = '''from datetime import datetime
OBJECT_DEFINITIONS = [
    {'name': 'Craft A', 'key': 'craft_a', 'id': '-901', 'id_type': 'id',
     'object_type': 'trajectory', 'start_date': datetime(2025, 1, 1),
     'end_date': datetime(2025, 6, 1)},
    {'name': 'Craft B', 'key': 'craft_b', 'id': '-902', 'id_type': 'id',
     'object_type': 'trajectory', 'start_date': datetime(2025, 11, 1),
     'end_date': datetime(2026, 5, 1)},
    {'name': 'Testroid', 'key': 'testroid', 'id': 'X1', 'id_type': 'smallbody',
     'object_type': 'orbital'},
    {'name': 'Gone', 'key': 'gone_rock', 'id': 'X2', 'id_type': 'smallbody',
     'object_type': 'orbital'},
    {'name': 'Craft C', 'id': '-903', 'id_type': 'id',
     'object_type': 'trajectory', 'start_date': datetime(2025, 1, 1),
     'end_date': datetime(2025, 6, 1)},
]
'''

FLYBY_A = {"jd": hc.calendar_jd("2025-03-01 12:17"), "b_km": 30000.0,
           "v": 10.0, "around": "399"}
FLYBY_B = {"jd": hc.calendar_jd("2026-02-10 06:43"), "b_km": 500.0,
           "v": 5.0, "around": "X1"}

# Where the made-up JPL has positions for each craft, in its own words.
# Craft A's ends before the list's end_date (2025-06-01), as Juno's did
# on 2026-10-24; Craft B's starts after the list's start_date.
LIMITS = {"-901": ("2025-01-01 00:00", "2025-05-20 12:00", "Craft A"),
          "-902": ("2025-11-05 10:00", "2026-05-01 06:00", "Craft B"),
          "-903": ("2025-01-01 00:00", "2025-06-01 00:00", "Craft C")}


def mon(text):
    y, m, d = text[:10].split("-")
    return "%s-%s-%s %s" % (y, pp.MONTHS[int(m) - 1], d, text[11:])

CIRCLES = {"199": 0.387, "299": 0.723, "399": 1.0, "499": 1.524,
           "599": 5.2, "699": 9.58, "799": 19.2, "899": 30.1, "999": 39.5,
           "X1": 2.5, "X2": 3.1}


# Data sheets in JPL's three GM spellings, as read 2026-10-24; the 1-sigma
# line comes first in one of them, which the reader must pass over.
SHEETS = dict((k, "API VERSION: 1.2\n" + v + "\n") for k, v in {
    "10": "GM, km^3/s^2          = 132712440041.93938  Mass, 10^24 kg = ~1988410",
    "199": "  GM, km^3/s^2             = 22031.86855",
    "299": "  GM, km^3/s^2             = 324858.592",
    "399": "  GM 1-sigma, km^3/s^2     =      0.0014\n"
           "  GM, km^3/s^2             = 398600.435436   Inner core rad  = 1215 km",
    "301": "  Radius (IAU), km      = 1737.4           GM, km^3/s^2          = 4902.800066",
    "499": "  GM (km^3/s^2)         = 42828.375214",
    "599": "  GM (km^3/s^2)         = 126686531.900     GM 1-sigma (km^3/s^2) =  +- 1.2732",
    "699": "  GM (km^3/s^2)         = 37931206.234",
    "799": "  GM (km^3/s^2)         = 5793951.256",
    "899": "  GM (km^3/s^2)         = 6835099.97",
    "999": " GM (planet) km^3/s^2  = 869.326         Density (R=1195 km)   = 1.86 g/cm^3",
    "X1": "  GM= 0.001",
}.items())


def circle(r_au, jd, phase=0.0, inc=0.0):
    period = 365.25 * r_au ** 1.5
    w = 2 * math.pi / period
    a = w * (jd - 2451545.0) + phase
    x, y = r_au * math.cos(a), r_au * math.sin(a)
    vx, vy = -r_au * w * math.sin(a), r_au * w * math.cos(a)
    return [x, y * math.cos(inc), y * math.sin(inc),
            vx, vy * math.cos(inc), vy * math.sin(inc)]


def body_state(ident, jd):
    if ident == "10":
        return [0.0] * 6
    if ident == "301":
        e = circle(1.0, jd)
        m = circle(0.00257, jd)        # a small circle, its own period
        mw = 2 * math.pi / 27.32
        a = mw * (jd - 2451545.0)
        m = [0.00257 * math.cos(a), 0.00257 * math.sin(a), 0.0,
             -0.00257 * mw * math.sin(a), 0.00257 * mw * math.cos(a), 0.0]
        return [e[i] + m[i] for i in range(6)]
    return circle(CIRCLES[ident], jd, phase=0.3 * len(ident), inc=0.02)


def craft_state(ident, jd):
    fly = FLYBY_A if ident == "-901" else FLYBY_B
    base = body_state(fly["around"], jd)
    v_au_d = fly["v"] * DAY / AU
    b_au = fly["b_km"] / AU
    t = jd - fly["jd"]
    # straight relative line: offset along z, motion along x
    rel = [v_au_d * t, 0.0, b_au, v_au_d, 0.0, 0.0]
    return [base[i] + rel[i] for i in range(6)]


def parse_step(step):
    m = re.match(r"^(\d+)([dhm])$", step)
    n, u = int(m.group(1)), m.group(2)
    return n * {"d": 1.0, "h": 1 / 24.0, "m": 1 / 1440.0}[u]


class FakeJPL(object):
    def __init__(self, refuse=(), down=False):
        self.calls = []
        self.refuse, self.down = set(refuse), down

    def __call__(self, url):
        self.calls.append(url)
        if self.down:
            raise hc.Unreachable("network unreachable (planted)")
        q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        val = lambda k: urllib.parse.unquote(q[k][0]).strip("'")
        cmd = val("COMMAND").rstrip(";")
        if val("MAKE_EPHEM") == "NO":
            return SHEETS.get(cmd, "API VERSION: 1.2\n  GM= n.a.\n")
        center = val("CENTER").split("@")[1]
        if cmd in self.refuse:
            return ("API VERSION: 1.2\nNo ephemeris for target \"%s\" in "
                    "the span asked.\n" % cmd)
        jd0 = hc.calendar_jd(val("START_TIME"))
        jd1 = hc.calendar_jd(val("STOP_TIME"))
        if cmd in LIMITS:
            lo, hi, label = LIMITS[cmd]
            if jd0 < hc.calendar_jd(lo):
                return ('API VERSION: 1.2\nNo ephemeris for target "%s '
                        '(spacecraft)" prior to A.D. %s:00.0000 UT\n'
                        % (label, mon(lo)))
            if jd1 > hc.calendar_jd(hi):
                return ('API VERSION: 1.2\nNo ephemeris for target "%s '
                        '(spacecraft)" after A.D. %s:00.0000 UT\n'
                        % (label, mon(hi)))
        step = parse_step(val("STEP_SIZE"))
        state = craft_state if cmd.startswith("-") else body_state
        lines = ["API VERSION: 1.2", "$$SOE"]
        n = int(round((jd1 - jd0) / step))
        for i in range(n + 1):
            jd = jd0 + i * step
            s = state(cmd, jd)
            c = body_state(center, jd)
            r = [s[k] - c[k] for k in range(6)]
            lines.append("%.9f, A.D. x, %s," % (
                jd, ", ".join("%.16E" % v for v in r)))
        lines.append("$$EOE")
        return "\n".join(lines) + "\n"


def make_root(source=LIST):
    root = tempfile.mkdtemp(prefix="path_plan_test_")
    with open(os.path.join(root, "celestial_objects.py"), "w") as handle:
        handle.write(source)
    return root


RESULTS = []


def check(ok, label):
    RESULTS.append((bool(ok), label))
    return ok


def flyby_ok(plan, fly, body, centred):
    ev = [e for e in plan["events"] if e["body"] == body]
    if len(ev) != 1:
        return False, "%d %s events" % (len(ev), body)
    e = ev[0]
    want = pp.jd_to_calendar(fly["jd"])
    w0, w1, step = pp.window_and_step(fly["jd"], fly["b_km"], fly["v"])
    probs = []
    if e["closest"] != want:
        probs.append("closest %s, not %s" % (e["closest"], want))
    if abs(e["dist_km"] - fly["b_km"]) > max(1.0, fly["b_km"] * 1e-3):
        probs.append("distance %s km, not %s" % (e["dist_km"], fly["b_km"]))
    if abs(e["v_kms"] - fly["v"]) > 1e-3 * fly["v"]:
        probs.append("speed %s, not %s" % (e["v_kms"], fly["v"]))
    if [w0, w1, step] != e["window"] + [e["step"]]:
        probs.append("window %s step %s, not %s %s" % (
            e["window"], e["step"], [w0, w1], step))
    return not probs, "; ".join(probs) or "ok"


def suite(today=datetime.date(2026, 10, 24), plant=None):
    root = make_root()
    try:
        jpl = FakeJPL(refuse=("X2",))
        if plant:
            saved = plant()
        verdict, lines, out = pp.run(root, jpl, today, pause=0.0)
        if plant:
            saved()
        plans = out["plans"]
        okA, whyA = flyby_ok(plans.get("craft_a", {"events": []}),
                             FLYBY_A, "Earth", True)
        okB, whyB = flyby_ok(plans.get("craft_b", {"events": []}),
                             FLYBY_B, "Testroid", False)
        if plant:
            return okA and okB
        check(okA, "1. Craft A's Earth flyby found exactly (%s)" % whyA)
        sa, sb = plans["craft_a"]["span"], plans["craft_b"]["span"]
        check(sa == {"start": "2025-01-01", "end": "2025-05-20"}
              and sb == {"start": "2025-11-06", "end": "2026-05-01"},
              "9. each span is JPL's own: a list end past JPL's data is "
              "clipped, a start JPL refuses moves on (%s, %s)" % (sa, sb))
        far = [e["body"] for e in plans["craft_a"]["events"]
               if e["body"] not in ("Earth", "Sun")]
        check(not far, "1. no distant body is reported as a pass (%s)"
              % (", ".join(far) or "none"))
        check(okB, "1. Craft B's Testroid flyby found exactly (%s)" % whyB)
        earth_q = [u for u in jpl.calls if "-901" in u and "500%40399" in u
                   or ("-901" in u and "500@399" in u)]
        roid_q = [u for u in jpl.calls if "X1" in u and "1h" in u]
        check(earth_q and roid_q,
              "1. Earth's flyby asked centred on Earth (%d), the "
              "asteroid's around the Sun (%d)" % (len(earth_q), len(roid_q)))
        check("Gone" in "\n".join(lines) and "Not searched" in
              "\n".join(lines), "6. the refused body is named as not "
              "searched")
        check("UNREACHABLE" not in verdict and "craft_a" in verdict,
              "verdict names the paths: " + verdict)
        n_first = len(jpl.calls)
        jpl2 = FakeJPL(refuse=("X2",))
        v2, _, out2 = pp.run(root, jpl2, today, pause=0.0)
        check(not jpl2.calls and out2["plans"] == plans,
              "2. a second run the same day asks nothing (%d calls)"
              % len(jpl2.calls))
        later = today + datetime.timedelta(days=31)
        jpl3 = FakeJPL(refuse=("X2",))
        v3, l3, out3 = pp.run(root, jpl3, later, pause=0.0)
        pa = out3["plans"]["craft_a"]
        check(pa["carried"] == len(plans["craft_a"]["events"])
              and pa["events"] == plans["craft_a"]["events"],
              "3. 31 days later the old events are carried, none doubled "
              "(%d carried, %d events)" % (pa["carried"], len(pa["events"])))
        check(not [u for u in jpl3.calls if "1m" in u],
              "3. ... and no carried flyby is asked again")
        with open(os.path.join(root, "celestial_objects.py"), "w") as h:
            h.write(LIST.replace("datetime(2025, 6, 1)",
                                 "datetime(2025, 7, 1)"))
        jpl4 = FakeJPL(refuse=("X2",))
        v4, l4, out4 = pp.run(root, jpl4, later, pause=0.0)
        p4 = out4["plans"]["craft_a"]
        check(p4["carried"] == 0 and p4["span"]["end"] == "2025-05-20"
              and "changed" in "\n".join(l4),
              "4. a changed list entry makes the plan again in full, and "
              "the span stays JPL's")
        with open(os.path.join(root, pp.PLANS), "rb") as h:
            before = h.read()
        with open(os.path.join(root, "celestial_objects.py"), "w") as h:
            h.write(LIST.replace("datetime(2025, 6, 1)",
                                 "datetime(2025, 8, 1)"))
        jpl5 = FakeJPL(down=True)
        v5, l5, out5 = pp.run(root, jpl5, later, pause=0.0)
        with open(os.path.join(root, pp.PLANS), "rb") as h:
            after = h.read()
        check(v5.startswith("PATH PLAN: UNREACHABLE") and before == after
              and len(jpl5.calls) == 1,
              "5. JPL down: UNREACHABLE by name, plans kept, one question "
              "asked (%d)" % len(jpl5.calls))
        old_names = pp.PREVIEW_NAMES
        pp.PREVIEW_NAMES = ("Craft C", "Nobody")
        try:
            jpl6 = FakeJPL(refuse=("X2",))
            v6, l6, out6 = pp.run(root, jpl6, today, pause=0.0, preview=True)
        finally:
            pp.PREVIEW_NAMES = old_names
        with open(os.path.join(root, pp.PLANS), "rb") as h:
            plans_after = h.read()
        check(list(out6["plans"]) == ["preview_craft_c"]
              and os.path.exists(os.path.join(root, pp.PREVIEW))
              and plans_after == after and "Nobody (not in the list)" in v6,
              "8. --preview plans an unkeyed name into its own file, names "
              "the one not in the list, and leaves the plans untouched")
        print("  first run asked JPL %d questions" % n_first)
        for line in lines:
            print("  " + line)
    finally:
        shutil.rmtree(root, ignore_errors=True)


def as_it_goes():
    """Check 10. One list holds JPL's questions and the lines, in order."""
    root = make_root()
    try:
        seen = []

        class Logged(FakeJPL):
            def __call__(self, url):
                seen.append(("ask", url))
                return FakeJPL.__call__(self, url)

        progress = pp.Progress(out=lambda t: seen.append(("say", t)))
        pp.run(root, Logged(refuse=("X2",)), datetime.date(2026, 10, 24),
               pause=0.0, progress=progress)
        said = [t for k, t in seen if k == "say"]
        first = seen[0] if seen else ("none", "")
        want = ["Craft A: JPL has positions", "Craft B: JPL has positions",
                "Earth: asking JPL for its daily positions",
                "Earth: ", "days received", "flyby of Earth",
                "flyby of Testroid", "Craft A: planned", "saved"]
        missing = [w for w in want if not any(w in t for t in said)]
        ok = (first[0] == "say" and "started" in first[1]
              and "2 due" in first[1] and "Craft A" in first[1]
              and not missing)
        return ok, ("first: %s; missing: %s" % (first[1][:70],
                                                ", ".join(missing) or "none"))
    finally:
        shutil.rmtree(root, ignore_errors=True)


def saved_as_it_goes(plant=False):
    """Check 11. Looks at the file on disk when Craft B is first looked at
    closely (its first hourly question)."""
    root = make_root()
    real = pp.write_plans
    try:
        on_disk = []

        class Watching(FakeJPL):
            def __call__(self, url):
                if "-902" in url and "1h" in url and not on_disk:
                    path = os.path.join(root, pp.PLANS)
                    if os.path.exists(path):
                        with open(path, "r", encoding="utf-8") as h:
                            on_disk.append(sorted(json.load(h)["plans"]))
                    else:
                        on_disk.append([])
                return FakeJPL.__call__(self, url)

        if plant:
            pp.write_plans = lambda path_file, plans: {
                "schema": pp.SCHEMA, "plans": plans}
        pp.run(root, Watching(refuse=("X2",)), datetime.date(2026, 10, 24),
               pause=0.0)
        got = on_disk[0] if on_disk else None
        return got == ["craft_a"], "on disk then: %s" % got
    finally:
        pp.write_plans = real
        shutil.rmtree(root, ignore_errors=True)


def time_limit(plant=False):
    """Check 12. The clock passes the limit the moment Craft A's plan is
    saved; Craft B is then left. A second run with no limit plans it."""
    root = make_root()
    real_write, real_over = pp.write_plans, pp.Progress.over
    try:
        now = [0.0]
        progress = pp.Progress(clock=lambda: now[0], limit=600)

        def write_then_late(path_file, plans):
            out = real_write(path_file, plans)
            if "craft_a" in plans:
                now[0] = 10000.0
            return out

        pp.write_plans = write_then_late
        if plant:
            pp.Progress.over = lambda self: False
        jpl = FakeJPL(refuse=("X2",))
        verdict, lines, out = pp.run(root, jpl, datetime.date(2026, 10, 24),
                                     pause=0.0, progress=progress)
        pp.write_plans, pp.Progress.over = real_write, real_over
        b_asked = [u for u in jpl.calls if "-902" in u and "1h" in u]
        first_ok = (sorted(out["plans"]) == ["craft_a"]
                    and "Left for the next run" in verdict
                    and "craft_b" in verdict.split("Left for the next run")[1]
                    and not b_asked)
        jpl2 = FakeJPL(refuse=("X2",))
        v2, _, out2 = pp.run(root, jpl2, datetime.date(2026, 10, 24),
                             pause=0.0)
        a_asked = [u for u in jpl2.calls if "-901" in u]
        second_ok = (sorted(out2["plans"]) == ["craft_a", "craft_b"]
                     and not a_asked and "Left for" not in v2)
        return (first_ok and second_ok,
                "first run: %s; then: %s" % (verdict[:120], v2[:80]))
    finally:
        pp.write_plans, pp.Progress.over = real_write, real_over
        shutil.rmtree(root, ignore_errors=True)


def plant_no_backbone():
    old = pp.BACKBONE_STEP_SECONDS
    pp.BACKBONE_STEP_SECONDS = 0.0

    def restore():
        pp.BACKBONE_STEP_SECONDS = old
    return restore


def plant_no_fine_pass():
    old = pp.PASS_TWO
    pp.PASS_TWO = (0, "1h")

    def restore():
        pp.PASS_TWO = old
    return restore


def main():
    suite()
    ok, why = as_it_goes()
    check(ok, "10. a first line before JPL is asked, then a line for each "
              "span, each body's positions and each flyby (%s)" % why)
    ok, why = saved_as_it_goes()
    check(ok, "11. each plan saved as it is made (%s)" % why)
    check(not saved_as_it_goes(plant=True)[0],
          "11. planted fault caught: the plans written only at the end")
    ok, why = time_limit()
    check(ok, "12. past the time limit the next path is left for the next "
              "run, which plans it (%s)" % why)
    check(not time_limit(plant=True)[0],
          "12. planted fault caught: the limit never passing")
    for name, plant in (("the backbone's step set to nothing",
                         plant_no_backbone),
                        ("the fine pass skipped", plant_no_fine_pass)):
        caught = not suite(plant=plant)
        check(caught, "7. planted fault caught: %s" % name)
    failed = [label for ok, label in RESULTS if not ok]
    for ok, label in RESULTS:
        print("  %s  %s" % ("ok  " if ok else "FAIL", label))
    print()
    if failed:
        print("PATH PLAN SUITE: %d of %d checks FAILED: %s"
              % (len(failed), len(RESULTS), "; ".join(failed)))
        return 1
    print("PATH PLAN SUITE: %d of %d checks passed" % (len(RESULTS),
                                                       len(RESULTS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
