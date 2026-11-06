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
      6. An ended mission's marker (marker_moment): chosen after the
         path's last day, it is asked for that day at 00:01; chosen
         before, nothing changes; a mission still flying never changes;
         a plan that stops before mission_end (Akatsuki's cutoff) gives
         the plan's day. Planted fault: the last day lost, and the
         marker is asked for the date chosen.
      7. The animation (hold_last_day): frames after the last day hold
         the last day's position, labelled with that moment, JPL asked
         once; frames before it and a mission still flying are as they
         came. Planted fault: the last day lost, and those frames stay
         empty, which hides the marker.
      8. An ended path's line ends at its marker: drawn after its
         span, its last point is the last-day pair's 00:01, the
         moment marker_moment asks the marker for. Planted fault: JPL
         asked nothing for the pair, and the line stops short.

    Live, by hand (python test_path_drawing.py --galileo): Galileo drawn
    by its plan from JPL now gives the same moments, to the microday, as
    the website's served data/solar-system/positions/galileo.json at
    GALLERY_PIN, its last-day pair included (the orrery draws it since
    2026-11-06, L-476; before, it was left out). Galileo's path ended in
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
Module updated: November 6, 2026 with Anthropic's Claude Opus 5.5
(L-476: checks 6 and 7, an ended mission's marker on its last day in the
static plot and the animation, and check 8, its line ending at that
marker by the last-day pair, each with a planted fault; check 2 counts
the pair; the --galileo check now expects the pair drawn).
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
    pair = [a for a in jpl.asked if a[2] == "1m"]
    rest = [a for a in jpl.asked if a[2] != "1m"]
    inside = all(a >= start and b <= end for a, b, _ in rest)
    check(top > 0.004 and inside and len(rest) == 2 and len(pair) == 1,
          "2. the flyby's bend is kept (highest y %.4f AU of 0.005, %d "
          "points) and JPL is asked %d times inside the span, and %d for "
          "the last-day pair" % (top, len(pts), len(rest), len(pair)))
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

    ok, why = ended_marker()
    check(ok, "6. an ended mission's marker is asked for its last day "
          "when the date chosen is after it: %s" % why)
    ok, why = ended_frames()
    check(ok, "7. the animation holds an ended mission's marker on its "
          "last day: %s" % why)
    saved = pd.last_day
    pd.last_day = lambda obj, plans=None: None
    try:
        bad6 = ended_marker()[0]
        bad7 = ended_frames()[0]
    finally:
        pd.last_day = saved
    check(not bad6, "6. planted fault caught: with the last day lost, the "
          "marker is asked for the date chosen")
    check(not bad7, "7. planted fault caught: with the last day lost, the "
          "frames after it stay empty")

    last, marker = ended_line()
    check(last == marker, "8. an ended path's line ends at its marker: its "
          "last point %s, the marker %s" % (last, marker))

    def no_pair(ident, id_type, start, stop, step):
        return {} if step == "1m" else FakeJPL()(ident, id_type, start,
                                                 stop, step)
    last, marker = ended_line(fetch=no_pair)
    check(last != marker, "8. planted fault caught: with no last-day pair "
          "the line stops at %s, short of the marker %s" % (last, marker))


# An ended mission's made-up plan, and one cut before its mission_end.
ENDED = {"craft_ended": {"span": {"start": "1972-03-04", "end": "2003-01-23"}},
         "craft_cut": {"span": {"start": "2010-05-22", "end": "2024-04-26"}}}


def ended_marker():
    """(ok, why) for marker_moment on made-up entries."""
    ended = {"key": "craft_ended", "mission_end": datetime.datetime(2003, 1, 23)}
    cut = {"key": "craft_cut", "mission_end": datetime.datetime(2025, 9, 18),
           "path_cutoff": datetime.datetime(2024, 4, 26)}
    flying = {"key": "craft_ended"}
    unplanned = {"name": "Unplanned", "mission_end": datetime.datetime(2003, 9, 21)}
    today = datetime.datetime(2026, 11, 6, 12, 0)
    before = datetime.datetime(2000, 6, 1)
    got = {
        "ended, after": pd.marker_moment(ended, today, ENDED),
        "ended, before": pd.marker_moment(ended, before, ENDED),
        "flying": pd.marker_moment(flying, today, ENDED),
        "cut": pd.marker_moment(cut, today, ENDED),
        "unplanned": pd.marker_moment(unplanned, today, ENDED),
    }
    want = {
        "ended, after": (datetime.datetime(2003, 1, 23, 0, 1), True),
        "ended, before": (before, False),
        "flying": (today, False),
        "cut": (datetime.datetime(2024, 4, 26, 0, 1), True),
        "unplanned": (datetime.datetime(2003, 9, 21, 0, 1), True),
    }
    wrong = ["%s gave %s, wanted %s" % (k, got[k], want[k])
             for k in want if got[k] != want[k]]
    return not wrong, ("; ".join(wrong) if wrong else
                       "after the last day 2003-01-23 00:01, before it the "
                       "date chosen, a cut plan 2024-04-26 00:01, a mission "
                       "still flying unchanged")


def ended_frames():
    """(ok, why) for hold_last_day on a made-up animation of six yearly
    frames, 2001 to 2006, the path ending on 2003-01-23."""
    ended = {"key": "craft_ended", "name": "Craft",
             "mission_end": datetime.datetime(2003, 1, 23)}
    dates = [datetime.datetime(y, 6, 1) for y in range(2001, 2007)]
    padded = [{"x": 1.0}, {"x": 2.0}, None, None, None, None]
    asked = []

    def fetch_at(moment):
        asked.append(moment)
        return {"x": 82.1, "y": 0.0, "z": 0.0}

    held = pd.hold_last_day(ended, dates, padded, fetch_at, ENDED)
    flying = pd.hold_last_day({"key": "craft_ended", "name": "Flying"},
                              dates, padded, fetch_at, ENDED)
    moment = datetime.datetime(2003, 1, 23, 0, 1)
    ok = (held[:2] == padded[:2]
          and all(p and p["x"] == 82.1 and p["position_date"] == moment
                  for p in held[2:])
          and asked == [moment] and flying == padded)
    return ok, ("frames %s; JPL asked %s"
                % ([None if p is None else p["x"] for p in held],
                   [m.strftime("%Y-%m-%d %H:%M") for m in asked]))


def ended_line(fetch=None):
    """(the line's last moment, the marker's moment) for PLAN drawn as an
    ended mission's path, on a day after its span."""
    entry = {"key": "craft", "name": "Craft", "id": "-1", "id_type": "id",
             "mission_end": datetime.datetime(2025, 7, 1)}
    now = datetime.datetime(2026, 11, 6, 12, 0)
    pts = pd.draw_plan(entry, PLAN, fetch=fetch or FakeJPL(), now=now)
    marker = pd.marker_moment(entry, now, {"craft": PLAN})[0]
    return (pts[-1]["date"] if pts else None), marker


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
    # Since 2026-11-06 the orrery draws the last-day pair too (L-476).
    extra, missing = sorted(mine - web), sorted(web - mine)
    ok = (bool(mine) and not extra and not missing and len(last_day) == 2
          and last_day <= mine)
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
