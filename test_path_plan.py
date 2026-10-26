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
      8. An unkeyed spacecraft is not planned (until 2026-10-25 a
         --preview flag planned some by name; it went when slice 2's
         twelve were keyed).
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
     13. The orbiter rule, on two made-up orbiters around Mars: Craft D
         loops five times and leaves, and has exactly an arrival at its
         first nearest approach and a departure at its last, each to the
         minute; Craft E is still looping when its data ends, and has
         one arrival, marked as staying, and no departure. Planted
         fault: every nearest approach inside the Hill sphere kept, as
         rule 1 did.
     14. Every event names its kind (a flyby says "flyby"), and a plan
         made by the older rule is made again.
     15. Two made-up comets on open paths, each a straight line past the
         Sun: each has one event, its perihelion, found in JPL's
         positions to the minute (Comet One's data sheet writes TP 1.3
         days early, as a calendar day; Comet Two's as a Julian date),
         with the encounter rule's window and step; Comet One's span runs
         a year before its perihelion to a year after today, Comet Two's
         is clipped at both ends to JPL's data. A comet not marked
         open_path is not planned, and no spacecraft searches a comet.
     16. The same day asks nothing; 31 days later each comet is planned
         again, Comet One's end moved 31 days, Comet Two's still JPL's.
     17. Two planted faults must fail check 15: the perihelion taken from
         the data sheet's TP, and JPL's limits ignored.

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
Module updated: October 25, 2026 with Anthropic's Claude Opus 5.5
(L-443, build B: checks 13 and 14, the orbiter rule with a planted
fault, and each event's kind; check 8 now holds that an unkeyed entry is
not planned, the --preview flag it checked having gone).
Module updated: October 26, 2026 with Anthropic's Claude Opus 5.5
(L-443, build B part 2: checks 15 to 17, comets on open paths, with two
planted faults).
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
LIMITS = {"-904": ("2025-01-01 00:00", "2025-09-01 00:00", "Craft D"),
          "-905": ("2025-01-01 00:00", "2025-06-01 00:00", "Craft E"),
          "-901": ("2025-01-01 00:00", "2025-05-20 12:00", "Craft A"),
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


# Two orbiters around Mars (check 13). Each comes in along a straight
# line, loops N times between PERI and PERI + LOOP km every PERIOD days,
# nearest at T0 + k x PERIOD (off the hour, so the minute pass is
# needed), then leaves along a straight line -- or, for Craft E, is
# still looping when its data ends. Mars's Hill sphere at 1.524 AU is
# about 1.08 million km, so every loop lies inside it. By rule 1 each
# loop's nearest approach was an event: D had 5, E 7.
ORBITERS = {
    "-904": {"t0": hc.calendar_jd("2025-03-10 05:23"), "period": 9.7,
             "loops": 5, "peri": 20000.0, "loop": 600000.0, "vt": 3.0,
             "out": 1.0e6},
    "-905": {"t0": hc.calendar_jd("2025-03-10 05:23"), "period": 9.7,
             "loops": 99, "peri": 20000.0, "loop": 600000.0, "vt": 3.0,
             "out": 1.0e6},
}

LIST_ORBIT = '''from datetime import datetime
OBJECT_DEFINITIONS = [
    {'name': 'Craft D', 'key': 'craft_d', 'id': '-904', 'id_type': 'id',
     'object_type': 'trajectory', 'start_date': datetime(2025, 1, 1),
     'end_date': datetime(2025, 9, 1)},
    {'name': 'Craft E', 'key': 'craft_e', 'id': '-905', 'id_type': 'id',
     'object_type': 'trajectory', 'start_date': datetime(2025, 1, 1),
     'end_date': datetime(2025, 6, 1)},
]
'''


def orbiter_rel(o, jd):
    """[r, dr/dt in km/day] of an orbiter around Mars."""
    t_in = o["t0"] - o["period"] / 2.0
    t_out = o["t0"] + (o["loops"] - 1) * o["period"] + o["period"] / 2.0
    top = o["peri"] + o["loop"]
    if jd < t_in:
        return top + o["out"] * (t_in - jd), -o["out"]
    if jd > t_out:
        return top + o["out"] * (jd - t_out), o["out"]
    ph = 2 * math.pi * (jd - o["t0"]) / o["period"]
    return (o["peri"] + o["loop"] * (1 - math.cos(ph)) / 2.0,
            o["loop"] * math.pi / o["period"] * math.sin(ph))


def craft_state(ident, jd):
    if ident in ORBITERS:
        o = ORBITERS[ident]
        base = body_state("499", jd)
        r, dr = orbiter_rel(o, jd)
        rel = [r / AU, 0.0, 0.0, dr / AU, o["vt"] * DAY / AU, 0.0]
        return [base[i] + rel[i] for i in range(6)]
    fly = FLYBY_A if ident == "-901" else FLYBY_B
    base = body_state(fly["around"], jd)
    v_au_d = fly["v"] * DAY / AU
    b_au = fly["b_km"] / AU
    t = jd - fly["jd"]
    # straight relative line: offset along z, motion along x
    rel = [v_au_d * t, 0.0, b_au, v_au_d, 0.0, 0.0]
    return [base[i] + rel[i] for i in range(6)]


# Two made-up comets on open paths (checks 15 to 17). Each moves along a
# straight line past the Sun, so its perihelion -- the nearest moment, its
# distance and speed -- is known exactly. Comet One's perihelion falls off
# the hour; its data sheet writes TP as a calendar day 1.3 days early (an
# osculating TP is not the nearest moment), so the plan must find the
# perihelion in the positions, not take the TP. Comet Two's sheet writes TP
# as a Julian date, and JPL's data for it begins after a year before its
# perihelion and ends before a year after today, so both ends are clipped.
COMETS = {
    "C/2025 Z9": {"t0": hc.calendar_jd("2026-01-15 03:41"), "q": 0.4,
                  "v": 50.0, "tp": "TP= 2026-Jan-13.95"},
    "C/2024 Z8": {"t0": hc.calendar_jd("2024-06-02 17:09"), "q": 1.2,
                  "v": 30.0, "tp": "TP= 2460464.2"},
}
LIMITS["C/2024 Z8"] = ("2023-09-01 00:00", "2027-03-01 00:00", "Comet Two")

LIST_COMET = """from datetime import datetime
OBJECT_DEFINITIONS = [
    {'name': 'Craft A', 'key': 'craft_a', 'id': '-901', 'id_type': 'id',
     'object_type': 'trajectory', 'start_date': datetime(2025, 1, 1),
     'end_date': datetime(2025, 6, 1)},
    {'name': 'Comet One', 'key': 'comet_one', 'id': 'C/2025 Z9',
     'id_type': 'smallbody', 'object_type': 'trajectory', 'open_path': True},
    {'name': 'Comet Two', 'key': 'comet_two', 'id': 'C/2024 Z8',
     'id_type': 'smallbody', 'object_type': 'orbital', 'open_path': True},
    {'name': 'Comet Closed', 'key': 'comet_closed', 'id': 'C/2020 Z7',
     'id_type': 'smallbody', 'object_type': 'orbital'},
]
"""


def comet_state(ident, jd):
    c = COMETS[ident]
    v_au_d = c["v"] * DAY / AU
    t = jd - c["t0"]
    return [v_au_d * t, c["q"], 0.0, v_au_d, 0.0, 0.0]


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
            if cmd in COMETS:
                return ("API VERSION: 1.2\n   %s\n   GM= n.a.\n"
                        % COMETS[cmd]["tp"])
            return SHEETS.get(cmd, "API VERSION: 1.2\n  GM= n.a.\n")
        center = val("CENTER").split("@")[1]
        if cmd in self.refuse:
            return ("API VERSION: 1.2\nNo ephemeris for target \"%s\" in "
                    "the span asked.\n" % cmd)
        jd0 = hc.calendar_jd(val("START_TIME"))
        jd1 = hc.calendar_jd(val("STOP_TIME"))
        if cmd in LIMITS:
            lo, hi, label = LIMITS[cmd]
            what = "spacecraft" if cmd.startswith("-") else cmd
            scale = "UT" if cmd.startswith("-") else "TDB"
            if jd0 < hc.calendar_jd(lo):
                return ('API VERSION: 1.2\nNo ephemeris for target "%s '
                        '(%s)" prior to A.D. %s:00.0000 %s\n'
                        % (label, what, mon(lo), scale))
            if jd1 > hc.calendar_jd(hi):
                return ('API VERSION: 1.2\nNo ephemeris for target "%s '
                        '(%s)" after A.D. %s:00.0000 %s\n'
                        % (label, what, mon(hi), scale))
        step = parse_step(val("STEP_SIZE"))
        state = (craft_state if cmd.startswith("-") else
                 comet_state if cmd in COMETS else body_state)
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
        check("craft_c" not in out5["plans"]
              and "preview_craft_c" not in out5["plans"],
              "8. an entry with no key is not planned: Craft C, unkeyed, "
              "has no plan")
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


def orbiters(plant=False):
    """Check 13. Craft D loops 5 times around Mars and leaves; Craft E is
    still looping when its data ends. Planted fault: the orbiter rule
    off, every nearest approach inside the Hill sphere kept (rule 1)."""
    root = make_root(LIST_ORBIT)
    real = pp.orbiter_rule
    try:
        if plant:
            pp.orbiter_rule = lambda series, gate: [
                (i, "flyby", False) for i, k, st in real(series, None)]
        verdict, lines, out = pp.run(root, FakeJPL(), datetime.date(
            2026, 10, 24), pause=0.0)
        plans = out["plans"]
        probs = []
        for key, ident, kinds in (("craft_d", "-904",
                                   [("arrival", False), ("departure",
                                                         False)]),
                                  ("craft_e", "-905", [("arrival", True)])):
            o = ORBITERS[ident]
            ev = [e for e in plans.get(key, {"events": []})["events"]
                  if e["body"] == "Mars"]
            got = [(e.get("kind"), e.get("stays")) for e in ev]
            if got != kinds:
                probs.append("%s: %s" % (key, got))
                continue
            want = [pp.jd_to_calendar(o["t0"])]
            if len(kinds) == 2:
                want.append(pp.jd_to_calendar(
                    o["t0"] + (o["loops"] - 1) * o["period"]))
            if [e["closest"] for e in ev] != want:
                probs.append("%s at %s, not %s" % (
                    key, [e["closest"] for e in ev], want))
            if any(abs(e["dist_km"] - o["peri"]) > 1.0
                   or abs(e["v_kms"] - o["vt"]) > 1e-3 for e in ev):
                probs.append("%s: distance or speed" % key)
        stray = [e["body"] for k in plans for e in plans[k]["events"]
                 if e["body"] not in ("Mars", "Sun")]
        if stray:
            probs.append("stray events: %s" % stray)
        return not probs, "; ".join(probs) or (
            "craft_d %s; craft_e %s" % (
                [(e["kind"], e["closest"]) for e in plans["craft_d"]
                 ["events"] if e["body"] == "Mars"],
                [(e["kind"], e["stays"]) for e in plans["craft_e"]
                 ["events"] if e["body"] == "Mars"]))
    finally:
        pp.orbiter_rule = real
        shutil.rmtree(root, ignore_errors=True)


def kinds_named():
    """Check 14. A flyby says it is one, and a plan made by the old rule is
    made again."""
    root = make_root()
    try:
        _, _, out = pp.run(root, FakeJPL(refuse=("X2",)),
                           datetime.date(2026, 10, 24), pause=0.0)
        kinds = sorted(set(e.get("kind") for k in out["plans"]
                           for e in out["plans"][k]["events"]))
        path = os.path.join(root, pp.PLANS)
        with open(path, "r", encoding="utf-8") as h:
            data = json.load(h)
        bodies = pp.searched_bodies(pp.keyed_entries(LIST))
        ent = [f for f in pp.keyed_entries(LIST) if f["key"] == "craft_a"][0]
        old = pp.plan_inputs(ent, bodies)
        old["rule"] = 1
        data["plans"]["craft_a"]["inputs_sha256"] = pp.inputs_sha256(old)
        with open(path, "w", encoding="utf-8") as h:
            json.dump(data, h)
        _, lines, _ = pp.run(root, FakeJPL(refuse=("X2",)),
                             datetime.date(2026, 10, 25), pause=0.0)
        remade = any("craft_a" in l and "changed" in l for l in lines)
        return ("flyby" in kinds and None not in kinds and remade,
                "kinds %s; rule-1 plan made again: %s" % (kinds, remade))
    finally:
        shutil.rmtree(root, ignore_errors=True)


def comets(plant=None, today=datetime.date(2026, 10, 24)):
    """Checks 15 to 17: two comets on open paths. Returns (ok, why,
    plans, lines, calls)."""
    root = make_root(LIST_COMET)
    saved = plant() if plant else None
    try:
        jpl = FakeJPL()
        verdict, lines, out = pp.run(root, jpl, today, pause=0.0)
        plans = out["plans"]
        probs = []
        for key, ident, span in (
                ("comet_one", "C/2025 Z9",
                 {"start": "2025-01-15", "end": "2027-10-24"}),
                ("comet_two", "C/2024 Z8",
                 {"start": "2023-09-02", "end": "2027-02-28"})):
            c = COMETS[ident]
            plan = plans.get(key)
            if not plan:
                probs.append("%s not planned" % key)
                continue
            ev = plan["events"]
            if len(ev) != 1 or ev[0]["kind"] != "perihelion" \
                    or ev[0]["body"] != "Sun":
                probs.append("%s events %s" % (key, [(e["body"], e["kind"])
                                                   for e in ev]))
                continue
            e = ev[0]
            want = pp.jd_to_calendar(c["t0"])
            d_km = c["q"] * AU
            w0, w1, step = pp.window_and_step(c["t0"], d_km, c["v"])
            if e["closest"] != want:
                probs.append("%s perihelion %s, not %s" % (key, e["closest"],
                                                           want))
            if abs(e["dist_km"] - d_km) > d_km * 1e-6 \
                    or abs(e["v_kms"] - c["v"]) > 1e-3:
                probs.append("%s distance or speed" % key)
            if [w0, w1, step] != e["window"] + [e["step"]]:
                probs.append("%s window %s %s, not %s %s" % (
                    key, e["window"], e["step"], [w0, w1], step))
            if plan["span"] != span:
                probs.append("%s span %s, not %s" % (key, plan["span"], span))
            if plan["kind"] != "comet":
                probs.append("%s kind %s" % (key, plan["kind"]))
        if "comet_closed" in plans:
            probs.append("a comet not marked open_path was planned")
        sa = plans.get("craft_a", {}).get("searched", [])
        if any(n.startswith("Comet") for n in sa):
            probs.append("Craft A searched a comet: %s" % sa)
        return (not probs, "; ".join(probs) or "both perihelia to the minute, "
                "spans %s and %s" % (plans["comet_one"]["span"],
                                     plans["comet_two"]["span"]),
                plans, lines, jpl.calls, root)
    finally:
        if saved:
            saved()


def comet_cycle():
    """Check 16. The same day asks nothing; 31 days later each comet is
    planned again and its span's end has moved 31 days."""
    ok, why, plans, lines, calls, root = comets()
    try:
        jpl2 = FakeJPL()
        _, _, out2 = pp.run(root, jpl2, datetime.date(2026, 10, 24),
                            pause=0.0)
        same = not jpl2.calls and out2["plans"] == plans
        jpl3 = FakeJPL()
        _, l3, out3 = pp.run(root, jpl3, datetime.date(2026, 11, 24),
                             pause=0.0)
        one = out3["plans"]["comet_one"]
        moved = (one["span"]["end"] == "2027-11-24"
                 and one["events"][0]["closest"]
                 == plans["comet_one"]["events"][0]["closest"])
        two = out3["plans"]["comet_two"]["span"]["end"] == "2027-02-28"
        return (ok and same and moved and two,
                "same day %d calls; 31 days later comet_one ends %s, "
                "comet_two %s" % (len(jpl2.calls), one["span"]["end"],
                                  out3["plans"]["comet_two"]["span"]["end"]))
    finally:
        shutil.rmtree(root, ignore_errors=True)


def plant_tp_taken():
    """The perihelion taken from the data sheet's TP, not found in JPL's
    positions."""
    real = pp.make_comet_plan

    def fake(fetch, path, today, found, pause=0.0, progress=None):
        plan = real(fetch, path, today, found, pause, progress)
        tp = found[3]
        plan["events"][0]["closest"] = pp.jd_to_calendar(tp)
        return plan
    pp.make_comet_plan = fake

    def restore():
        pp.make_comet_plan = real
    return restore


def plant_no_clip():
    """JPL's limits ignored, so a span JPL refuses is not moved."""
    real = pp.jpl_limit
    pp.jpl_limit = lambda text: None

    def restore():
        pp.jpl_limit = real
    return restore


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
    ok, why = orbiters()
    check(ok, "13. the orbiter rule: an orbiter that leaves has one "
              "arrival and one departure, one that stays has one arrival "
              "and no departure, each at its minute (%s)" % why)
    check(not orbiters(plant=True)[0],
          "13. planted fault caught: every nearest approach inside the "
          "Hill sphere kept (rule 1)")
    ok, why = kinds_named()
    check(ok, "14. every event names its kind, and a plan made by the "
              "older rule is made again (%s)" % why)
    ok, why, _, lines, _, root = comets()
    shutil.rmtree(root, ignore_errors=True)
    check(ok, "15. each comet on an open path has its perihelion found in "
              "JPL's positions to the minute, as its one event, and its "
              "span from a year before it to a year after today, clipped "
              "to JPL's data; a comet not marked is not planned, and no "
              "spacecraft searches a comet (%s)" % why)
    for line in lines:
        if "comet" in line:
            print("  " + line)
    ok, why = comet_cycle()
    check(ok, "16. a comet's plan is not asked again the same day, and 31 "
              "days later is made again with its end moved (%s)" % why)
    for name, plant in (("the perihelion taken from the data sheet's TP",
                         plant_tp_taken),
                        ("JPL's limits ignored", plant_no_clip)):
        got = comets(plant=plant)
        shutil.rmtree(got[5], ignore_errors=True)
        check(not got[0], "17. planted fault caught: %s" % name)
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
