"""
path_drawing.py - the orrery draws a planned path by its path plan
(L-476): a spacecraft's flown and planned trajectory, or a comet on an
open path, around the Sun.

Tony's rulings of 2026-10-23
(documentation/DESIGN_L443_slice2_rulings_20261023.md): the orrery
works out each path's plan once (path_plan.py, data/path_plans.json),
the website fetches by it, and the orrery's own plot draws by it
(ruling 2); solid to today and dashed after, the part after today being
JPL's own planned trajectory or prediction, never extended (ruling 6).
And on Oct 24, 17:26: "the orrery's object list for served windows
should be updated to match the website" -- so a planned entry's dates
are read from its plan here, never typed a second time.

The drawing is the website's, point for point: the backbone across the
plan's span at its step, thinned by Douglas-Peucker where it runs
straight; each event's window at its own step, thinned at its own scale
(WINDOW_THIN_FRACTION of the passing distance) and merged after the
backbone's thinning, so a flyby is never thinned away. The website then
adds a daily tail and an ended mission's last-day pair, which are its
room's needs (a marker at the minute the room is opened); the orrery
draws neither. Its twin is fetch_path_by_plan, _plan_span,
fetch_vectors_range and douglas_peucker in the website's
tools/gallery_cache_builder.py (tonyquintanilla.github.io); the two
repositories cannot import each other, so each holds its own copy, and
test_path_drawing.py --galileo compares them against JPL.

Only around the Sun (Tony, 2026-11-03, 12:06 Chicago: "yes and the
orrery and the website should both follow this"). A plan's backbone and
thinning are worked in distances around the Sun; centred on Jupiter, a
7-day step thinned at 0.02 AU would erase Juno's orbits. So a planned
path centred on any other body is drawn as before, its span read from
the plan.

Key functions:
    entry_span() - a planned entry's first and last moment, from its
                   plan; an unplanned entry's typed dates
    draw_plan()  - the dates and positions of a planned path, asked of
                   JPL by the website's method
    plan_path_traces() - the path solid to today and dashed after, one
                   colour, one legend entry, one info marker
    span_label() - a planned entry's "(start to end)" checkbox label

Consumed by: palomas_orrery.py (plot_actual_orbits, plot_objects'
worker, animate_objects' worker), orbit_data_manager.py,
spacecraft_encounters.py; test_path_drawing.py.

Module created: November 3, 2026 with Anthropic's Claude Opus 5.5
(L-476).
"""

import datetime
import json
import os

from constants_new import KM_PER_AU
from utc_clock import utc_now, HORIZONS_CACHE  # L-504: the clock read as UTC; JPL asked fresh

ROOT = os.path.dirname(os.path.abspath(__file__))
PLANS = os.path.join("data", "path_plans.json")

# A window's points are thinned at its own event's scale: a point is
# kept where the path bends away from the chord by more than this
# fraction of the passing distance. The website's WINDOW_THIN_FRACTION,
# the same number (gallery-cache-builder, A Spacecraft Is Fetched by Its
# Plan).
WINDOW_THIN_FRACTION = 0.01

# Points are keyed to the minute, as the website keys them: a window's
# step can be a minute, and a window point lands on a backbone point of
# the same minute and replaces it.
MINUTE_KEY = "%Y-%m-%d %H:%M"

# TDB runs 69 s ahead of UTC (orbit_data_manager.utc_to_tdb, the
# website's own copy of it).
TDB_OFFSET = datetime.timedelta(seconds=69)

_DRAWN = {}     # (key, made, span) -> points, for this run of the orrery


def load_plans(root=ROOT):
    """{key: plan} from data/path_plans.json; {} when there is none."""
    path = os.path.join(root, PLANS)
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle).get("plans") or {}


def plan_for(obj, plans=None):
    """The entry's plan, or None: an entry is planned when its 'key' has
    a plan in data/path_plans.json."""
    key = obj.get("key")
    if not key:
        return None
    if plans is None:
        plans = load_plans()
    return plans.get(key)


def plan_span(plan):
    """(start, end) of a plan's span as plain UTC datetimes. The span's
    days are JPL's (TDB); the end is taken back by the 69 s that every
    question to JPL adds, so the last moment asked is the span's end on
    JPL's clock and never past it (the website's _plan_span)."""
    span = plan["span"]
    start = datetime.datetime.strptime(span["start"], "%Y-%m-%d")
    end = datetime.datetime.strptime(span["end"], "%Y-%m-%d")
    return start, end - TDB_OFFSET


def entry_span(obj, plans=None):
    """(start, end) of an entry's path: a planned entry's from its plan;
    any other entry's typed start_date and end_date (None where there is
    none). Every reader that means the span of the path asks here."""
    plan = plan_for(obj, plans)
    if plan:
        return plan_span(plan)
    return obj.get("start_date"), obj.get("end_date")


def span_label(key, plans=None):
    """"(YYYY-MM-DD to YYYY-MM-DD)" for a planned entry's checkbox, read
    from its plan when the window is built. A key with no plan prints so
    and labels nothing, which shows on the window."""
    plan = (load_plans() if plans is None else plans).get(key)
    if not plan:
        print("[PATH PLAN] %s: no plan in %s, so no dates on its label"
              % (key, PLANS), flush=True)
        return ""
    return "(%s to %s)" % (plan["span"]["start"], plan["span"]["end"])


def _norm_id_type(id_type):
    """astroquery deprecates 'id' and 'majorbody'; None is the value that
    finds spacecraft and major bodies (the website's _norm_id_type)."""
    return None if id_type in ("majorbody", "id") else id_type


def fetch_range(ident, id_type, start, stop, step):
    """{minute key: {'jd', 'x', 'y', 'z'}} around the Sun, in AU, on the
    ecliptic: JPL's positions from start to stop (plain UTC datetimes) at
    step, asked as the website asks them (fetch_vectors_range)."""
    from astroquery.jplhorizons import Horizons
    from astropy.time import Time
    epochs = {"start": (start + TDB_OFFSET).strftime("%Y-%m-%d %H:%M"),
              "stop": (stop + TDB_OFFSET).strftime("%Y-%m-%d %H:%M"),
              "step": step}
    query = Horizons(id=ident, id_type=_norm_id_type(id_type),
                     location="@sun", epochs=epochs)
    rows = query.vectors(refplane="ecliptic", cache=HORIZONS_CACHE)
    out = {}
    for row in rows:
        jd = float(row["datetime_jd"])
        when = Time(jd, format="jd").datetime
        out[when.strftime(MINUTE_KEY)] = {
            "jd": jd, "x": float(row["x"]), "y": float(row["y"]),
            "z": float(row["z"])}
    return out


def douglas_peucker(points, tol_au):
    """Iterative 3D Ramer-Douglas-Peucker on {key: {jd, x, y, z}}: keep
    the ends and any point further than tol_au from its local chord. The
    website's douglas_peucker, unchanged."""
    items = sorted(points.items(), key=lambda kv: kv[1]["jd"])
    n = len(items)
    if n < 3:
        return points
    P = [(kv[1]["x"], kv[1]["y"], kv[1]["z"]) for kv in items]
    keep = [False] * n
    keep[0] = keep[n - 1] = True
    stack = [(0, n - 1)]
    while stack:
        lo, hi = stack.pop()
        ax, ay, az = P[lo]
        bx, by, bz = P[hi]
        ux, uy, uz = bx - ax, by - ay, bz - az
        u2 = ux * ux + uy * uy + uz * uz
        dmax, idx = -1.0, -1
        for i in range(lo + 1, hi):
            px, py, pz = P[i]
            if u2 == 0.0:
                d = ((px - ax) ** 2 + (py - ay) ** 2 + (pz - az) ** 2) ** 0.5
            else:
                t = ((px - ax) * ux + (py - ay) * uy + (pz - az) * uz) / u2
                cx, cy, cz = ax + t * ux, ay + t * uy, az + t * uz
                d = ((px - cx) ** 2 + (py - cy) ** 2 + (pz - cz) ** 2) ** 0.5
            if d > dmax:
                dmax, idx = d, i
        if dmax > tol_au and idx != -1:
            keep[idx] = True
            stack.append((lo, idx))
            stack.append((idx, hi))
    return {items[i][0]: items[i][1] for i in range(n) if keep[i]}


def draw_plan(obj, plan, fetch=None):
    """[{'date', 'jd', 'x', 'y', 'z'}] in time order: the path by its
    plan, the website's whole fetch without its tail and last-day pair.
    'date' is the minute key read back as a plain datetime. Asked of JPL
    once per plan in a run of the orrery. None, with the reason printed,
    when JPL gives nothing."""
    fetch = fetch or fetch_range
    start, end = plan_span(plan)
    memo = (obj.get("key"), plan.get("made"), start, end)
    if fetch is fetch_range and memo in _DRAWN:
        return _DRAWN[memo]
    ident, id_type = obj["id"], obj.get("id_type")
    backbone = plan.get("backbone") or {}
    try:
        glide = fetch(ident, id_type, start, end,
                      backbone.get("step", "7d"))
        tol = backbone.get("thin_tol_au")
        if tol:
            glide = douglas_peucker(glide, float(tol))
        points = dict(glide)
        for ev in plan.get("events") or []:
            w0 = datetime.datetime.strptime(ev["window"][0], MINUTE_KEY)
            w1 = datetime.datetime.strptime(ev["window"][1], MINUTE_KEY)
            w0, w1 = max(w0, start), min(w1, end)
            if w0 >= w1:
                continue
            got = fetch(ident, id_type, w0, w1, ev["step"])
            if ev.get("dist_km"):
                got = douglas_peucker(
                    got, float(ev["dist_km"]) * WINDOW_THIN_FRACTION
                    / KM_PER_AU)
            points.update(got)
    except Exception as exc:
        print("[PATH PLAN] %s: not drawn by its plan; JPL gave no path "
              "(%s)" % (obj.get("name"), exc), flush=True)
        return None
    out = [dict(p, date=datetime.datetime.strptime(k, MINUTE_KEY))
           for k, p in sorted(points.items(), key=lambda kv: kv[1]["jd"])]
    print("[PATH PLAN] %s: %d points by its plan made %s, %s to %s"
          % (obj.get("name"), len(out), plan.get("made"),
             plan["span"]["start"], plan["span"]["end"]), flush=True)
    if fetch is fetch_range:
        _DRAWN[memo] = out
    return out


def split_at(points, now):
    """(solid, dashed): the points up to now, and from the last of them
    on, so the two lines meet. Either can be empty."""
    solid = [p for p in points if p["date"] <= now]
    later = [p for p in points if p["date"] > now]
    dashed = (solid[-1:] + later) if later else []
    return solid, dashed


def plan_path_traces(points, color, name, hover_text, legendgroup,
                     now=None):
    """The traces of a path drawn by its plan: solid to now (UTC), dashed
    after, one colour and one legend entry, and one info marker at the
    middle point carrying the hover (orrery-coding-conventions, Single
    Info Marker Pattern)."""
    import plotly.graph_objs as go
    solid, dashed = split_at(points, now or utc_now())
    traces = []
    for part, dash in ((solid, None), (dashed, "dash")):
        if len(part) < 2:
            continue
        line = dict(color=color, width=2)
        if dash:
            line["dash"] = dash
        traces.append(go.Scatter3d(
            x=[p["x"] for p in part], y=[p["y"] for p in part],
            z=[p["z"] for p in part], mode="lines", line=line,
            name=name, hoverinfo="skip", legendgroup=legendgroup,
            showlegend=not traces))
    mid = points[len(points) // 2]
    traces.append(go.Scatter3d(
        x=[mid["x"]], y=[mid["y"]], z=[mid["z"]], mode="markers",
        marker=dict(size=8, color=color, symbol="cross", opacity=1.0,
                    line=dict(color="white", width=2)),
        name="", text=[hover_text], customdata=[hover_text],
        hovertemplate="%{text}<extra></extra>", legendgroup=legendgroup,
        showlegend=False))
    return traces
