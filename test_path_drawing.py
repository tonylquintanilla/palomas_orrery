"""
test_path_drawing.py - the orrery's drawing of a path by its plan
(path_drawing.py, L-476), offline, with one live check against JPL and
the website.

WHAT IT CHECKS

    Offline, in the maintenance run:
      1. A planned entry's span is its plan's, the end taken back by the
         69 s every question to JPL adds; an unplanned entry's is its
         typed dates.
      2. A made-up path, a straight line with a bend of 0.005 AU around a
         flyby, drawn by a made-up plan: the backbone is thinned to its
         ends, the flyby's window keeps the bend, and JPL is asked
         nothing outside the span. Planted fault: the window thinned at a
         scale a thousand times coarser, which loses the bend.
      3. Solid to now and dashed after, the two lines meeting at the
         last point before now, one legend entry between them.
      4. A planned entry's checkbox label is its plan's span.
      5. The daily tail around now: on a straight run, where the
         thinning keeps no point near now, the solid part still ends
         within five minutes of now. Planted fault: the tail turned off,
         and the solid part ends at the flyby, two months back.

    Live, by hand (python test_path_drawing.py --galileo): Galileo drawn
    by its plan from JPL now gives the same moments, to the microday, as
    the website's served data/solar-system/positions/galileo.json at
    GALLERY_PIN, apart from the website's last-day pair, which the
    orrery does not draw and which is named. Galileo's path ended in
    2003 and JPL no longer revises it, so the two must agree. With
    --plant the backbone's thinning tolerance is doubled, and the check
    must fail.

RUN COMMAND

    Open this file in VS Code and click Run (the offline checks). The
    live check needs a terminal: python test_path_drawing.py --galileo

Module created: November 3, 2026 with Anthropic's Claude Opus 5.5
(L-476).
Module updated: November 3, 2026, evening, with Anthropic's Claude Opus
5.5 (L-476: check 5, the daily tail, and its planted fault).
"""

import datetime
import json
import os
import subprocess
import sys

import path_drawing as pd

GALLERY = os.path.join(pd.ROOT, "..", "tonyquintanilla.github.io")
GALLERY_PIN = "3a211a8cf10a3002668a85836f31bf973e385f2c"
GALILEO_FILE = "data/solar-system/positions/galileo.json"

RESULTS = []


def check(ok, label):
    RESULTS.append((bool(ok), label))
    return ok


PLAN = {"made": "2026-11-03", "span": {"start": "2025-01-01",
                                       "end": "2025-07-01"},
        "backbone": {"step": "7d", "thin_tol_au": 0.02},
        "events": [{"window": ["2025-03-01 00:00", "2025-03-03 00:00"],
                    "step": "1h", "dist_km": 100000.0}]}
FLYBY = datetime.datetime(2025, 3, 2)
STEPS = {"d": 86400.0, "h": 3600.0, "m": 60.0}


class FakeJPL(object):
    """A straight line along x, 0.01 AU a day, with a bend of 0.005 AU
    in y within a day of FLYBY; answers in fetch_range's shape."""

    def __init__(self):
        self.asked = []

    def __call__(self, ident, id_type, start, stop, step):
        self.asked.append((start, stop, step))
        dt = float(step[:-1]) * STEPS[step[-1]]
        out, t = {}, start
        while t <= stop:
            days = (t - FLYBY).total_seconds() / 86400.0
            y = 0.005 * max(0.0, 1.0 - abs(days))
            out[t.strftime(pd.MINUTE_KEY)] = {
                "jd": 2440587.5 + (t - datetime.datetime(
                    1970, 1, 1)).total_seconds() / 86400.0,
                "x": 0.01 * days, "y": y, "z": 0.0}
            t += datetime.timedelta(seconds=dt)
        return out


def drawn_bend(fraction=None):
    """(highest y drawn, points, fake): PLAN drawn on FakeJPL."""
    saved = pd.WINDOW_THIN_FRACTION
    if fraction is not None:
        pd.WINDOW_THIN_FRACTION = fraction
    try:
        jpl = FakeJPL()
        pts = pd.draw_plan({"key": "craft", "name": "Craft", "id": "-1",
                            "id_type": "id"}, PLAN, fetch=jpl)
    finally:
        pd.WINDOW_THIN_FRACTION = saved
    return max(p["y"] for p in pts), pts, jpl


def offline():
    plans = {"craft": PLAN}
    s, e = pd.entry_span({"key": "craft", "end_date": "typed"}, plans)
    t0, t1 = datetime.datetime(2020, 1, 1), datetime.datetime(2021, 1, 1)
    check(s == datetime.datetime(2025, 1, 1)
          and e == datetime.datetime(2025, 7, 1)
          - datetime.timedelta(seconds=69)
          and pd.entry_span({"start_date": t0, "end_date": t1}, plans)
          == (t0, t1),
          "1. a planned entry's span is its plan's (%s to %s); an "
          "unplanned entry's is its typed dates" % (s, e))

    top, pts, jpl = drawn_bend()
    start, end = pd.plan_span(PLAN)
    inside = all(a >= start and b <= end for a, b, _ in jpl.asked)
    check(top > 0.004 and inside and len(jpl.asked) == 2,
          "2. the flyby's bend is kept (highest y %.4f AU of 0.005, %d "
          "points) and JPL is asked %d times, inside the span"
          % (top, len(pts), len(jpl.asked)))
    top_bad = drawn_bend(fraction=10.0)[0]
    check(top_bad < 0.004,
          "2. planted fault caught: a window thinned a thousand times "
          "coarser loses the bend (highest y %.4f AU)" % top_bad)

    now = datetime.datetime(2025, 3, 2, 0, 30)
    solid, dashed = pd.split_at(pts, now)
    traces = pd.plan_path_traces(pts, "white", "Craft Full Mission",
                                 "Craft Full Mission", "craft", now=now)
    lines = [t for t in traces if t.mode == "lines"]
    check(solid and dashed and solid[-1]["date"] <= now
          and dashed[0] is solid[-1] and dashed[1]["date"] > now
          and len(lines) == 2 and lines[1].line.dash == "dash"
          and [t.showlegend for t in traces] == [True, False, False],
          "3. solid to now and dashed after, meeting at %s, one legend "
          "entry" % (solid[-1]["date"] if solid else None))

    check(pd.span_label("craft", plans) == "(2025-01-01 to 2025-07-01)",
          "4. a planned entry's label is its plan's span (%s)"
          % pd.span_label("craft", plans))

    gap = solid_gap()
    check(gap is not None and gap <= 5.0,
          "5. on a straight run the solid part ends at now: its last "
          "point %s minutes before now" % gap)
    saved = (pd.TAIL_BEHIND_DAYS, pd.TAIL_AHEAD_DAYS, pd.TAIL_LEAD_MINUTES)
    pd.TAIL_BEHIND_DAYS = pd.TAIL_AHEAD_DAYS = pd.TAIL_LEAD_MINUTES = 0
    try:
        bad = solid_gap()
    finally:
        (pd.TAIL_BEHIND_DAYS, pd.TAIL_AHEAD_DAYS,
         pd.TAIL_LEAD_MINUTES) = saved
    check(bad is not None and bad > 1440.0,
          "5. planted fault caught: with the tail turned off the solid "
          "part ends %s minutes before now" % bad)


def solid_gap():
    """Minutes from the solid part's last point to now, for PLAN drawn
    on FakeJPL with now in its straight run, two months after the
    flyby; None when nothing is solid."""
    now = datetime.datetime(2025, 5, 10, 12, 0)
    pts = pd.draw_plan({"key": "craft", "name": "Craft", "id": "-1",
                        "id_type": "id"}, PLAN, fetch=FakeJPL(), now=now)
    solid, dashed = pd.split_at(pts, now)
    if not solid or not dashed or dashed[0] is not solid[-1]:
        return None
    return (now - solid[-1]["date"]).total_seconds() / 60.0


def galileo(plant=False):
    """(ok, why): Galileo by its plan against the website's served file."""
    raw = subprocess.run(["git", "-C", GALLERY, "show", "%s:%s"
                          % (GALLERY_PIN, GALILEO_FILE)],
                         capture_output=True, text=True, check=True).stdout
    web = set(round(t, 6) for t in json.loads(raw)["data"]["t"])
    plan = dict(pd.load_plans()["galileo"])
    if plant:
        plan["backbone"] = dict(plan["backbone"], thin_tol_au=0.04)
    pts = pd.draw_plan({"key": "galileo", "name": "Galileo", "id": "-77",
                        "id_type": "id"}, plan)
    mine = set(round(p["jd"], 6) for p in pts or [])
    last_day = set(t for t in web if t >= 2452903.5)   # 2003-09-21
    extra, missing = sorted(mine - web), sorted(web - mine - last_day)
    ok = bool(mine) and not extra and not missing and len(last_day) == 2
    return ok, ("%d drawn, %d served, the website's last-day pair %s; "
                "drawn and not served %s; served and not drawn %s"
                % (len(mine), len(web), sorted(last_day), extra[:5],
                   missing[:5]))


def main(argv):
    if "--galileo" in argv:
        plant = "--plant" in argv
        ok, why = galileo(plant=plant)
        print("%s  Galileo by its plan against the website's %s at %s%s:"
              "\n      %s" % ("ok  " if ok else "FAIL", GALILEO_FILE,
                              GALLERY_PIN[:8],
                              " (planted: tolerance doubled)" if plant
                              else "", why))
        return 0 if ok else 1
    offline()
    failed = [label for ok, label in RESULTS if not ok]
    for ok, label in RESULTS:
        print("  %s  %s" % ("ok  " if ok else "FAIL", label))
    print()
    if failed:
        print("PATH DRAWING SUITE: %d of %d checks FAILED: %s"
              % (len(failed), len(RESULTS), "; ".join(failed)))
        return 1
    print("PATH DRAWING SUITE: %d of %d checks passed"
          % (len(RESULTS), len(RESULTS)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
