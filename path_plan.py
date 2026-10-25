"""
path_plan.py -- the orrery's plan for drawing each path the website
serves: a spacecraft's flown and planned trajectory, and a comet on an
open path (L-443, slice 2).

WHY IT EXISTS

    Tony's rulings of 2026-10-23
    (documentation/DESIGN_L443_slice2_rulings_20261023.md):
      1. "One path rule, the orrery's": every path gets a coarse
         backbone, thinned where it runs straight, with fine steps
         around each event, the window and the step worked out from that
         event's distance and speed, and the events read from the
         orrery. "Yes, confirmed. Good solution."
      2. The orrery and the website alike: the orrery works out each
         path's plan once and serves it, as it places the stored
         drawings; the website's builder fetches by it, and the orrery's
         own plot later draws by it (L-476, after slice 2).
      5. "Maybe use the nearest approach which is mechanical instead of
         a sourced date": an event is a nearest approach found in JPL's
         own positions, and needs no citation.
      7. The future part is fetched again on the 30-day cycle.
    Until this module the website's only path, Voyager 1's, carried two
    flyby windows typed into the gallery's config with no source.

WHAT A PLAN IS

    For each served path (an entry in celestial_objects.py with a 'key'
    whose object_type is 'trajectory' and whose id starts with '-', a
    spacecraft), data/path_plans.json holds:
      span      the first and last day JPL has positions for, read from
                JPL itself: the path is asked from the entry's start_date
                (the launch) to the year 2100, and clipped to the limits
                JPL names when it refuses ("No ephemeris for target ...
                after A.D. 2028-SEP-02"). The list's end_date is not
                used: on 2026-10-24 Juno's and Psyche's ran past JPL's
                data and New Horizons' stopped 21 years short of it. The
                part after today is JPL's planned trajectory; nothing is
                extended here.
      backbone  one step and one thinning tolerance for every path, the
                ones Voyager 1's path was built and proven with on
                2026-07-11: a point every 7 days, thinned by
                Douglas-Peucker where the path runs straighter than
                0.02 AU. The website's builder applies them.
      events    each nearest approach that needs finer steps than the
                backbone gives, with the body, the moment, the distance
                and the speed, and the window and step to fetch around it.
      searched  every body whose nearest approaches were looked for.
      made      the day the plan was made.

    Comets on open paths are not planned yet: how much of a comet's path
    to draw is Tony's question of 2026-10-24, and they wait for it.

HOW AN EVENT IS FOUND

    The bodies searched are the Sun, the eight planets, the Moon, Pluto,
    and every small body the website serves (by the record the website
    serves it by, export_objects.served_identity) whose data sheet gives
    a GM. Each body's position
    and each path's are fetched from JPL Horizons once a day across the
    path's span, all around the Sun, and the distance between them is
    worked out here day by day.

    A day nearer than the days either side is a candidate. It is a PASS
    only when it lies inside the body's Hill sphere, the region where the
    body's own gravity outweighs the Sun's pull: its distance from the Sun
    times (GM / (3 GM of the Sun)) ** (1/3), the Moon's reckoned against
    Earth. Every GM is JPL's own, read from the body's Horizons data sheet
    when the plan is made, so no number is typed here. The Sun, the
    drawing's own centre, needs no gate. A body whose sheet gives no GM
    -- most small bodies -- has no Hill sphere to pass inside and is
    named as not searched. (Without this gate the first offline run
    called nearest approaches 85 million km from Mercury and 103 million
    km from the Moon events: the curvature rule alone cannot tell a pass
    from two bodies merely being nearest.)

    A pass becomes an EVENT only when the path bends there faster than
    the backbone could draw: by the orrery's own curvature rule
    (spacecraft_encounters._calculate_encounter_resolution), about 30
    points through a half circle at the passing distance and speed, so
    the ideal step is pi x distance / speed / 30. Kept only when that is
    shorter than the backbone's 7 days. A daily sample can sit up to half
    a day of travel from the true nearest moment, so both tests use the
    distance less half a day's travel; nothing that could pass is
    dropped.

    A candidate is then found exactly in two passes, the orrery's
    resolve_encounter_time numbers: hourly for a day and a half either
    side, then each minute for an hour and a half either side of the
    nearest hour. Around a major body the path is asked of Horizons
    centred on that body; around a small body, which Horizons cannot
    centre on by its designation, both are asked around the Sun and the
    difference taken. The nearest minute gives the distance and the
    speed. The window and the step then follow from them by
    _calculate_encounter_resolution itself, so the website and the
    orrery's encounter views use one rule. Where the ideal step is longer
    than Horizons' six-hour step, the step is in whole days, never more
    than the ideal.

THE 30-DAY CYCLE, AND WHAT IT ASKS

    Only what is due. A plan is made again when it is 30 days old, or at
    once when what it was made from changed (the id, its type, the span,
    or the bodies searched). A plan made again keeps the events it found
    more than 30 days before today, which JPL has already reconstructed,
    and looks again from three days before that onward: the planned
    part is what JPL revises. So most runs ask JPL nothing.

    Any failure to get JPL's answer stops the plan for that path; its
    previous plan, if any, is kept, nothing is written for it, and the
    verdict says UNREACHABLE by name. It never passes.

RUN COMMAND

    Open this file in VS Code and click Run. It takes no arguments.

        python path_plan.py            what is due
        python path_plan.py --all      every path, now
        python path_plan.py --preview  TEMPORARY: slice 2's twelve
                                       spacecraft by name, before they are
                                       keyed, into data/path_plans_preview.
                                       json, which the export never reads
                                       (the dashboard's "Path Plan --
                                       preview of slice 2" button)

    orrery_maintenance_run.py runs it as a GENERATOR, before the objects
    export, which carries each plan to the website.

    The last line is the verdict: "PATH PLAN: ..." naming each path, how
    many events it has, and what was asked.

Role: devtool
Domain: dev_tools

Module created: October 24, 2026 with Anthropic's Claude Opus 5.5
(L-443, slice 2).
"""

import ast
import datetime
import hashlib
import json
import math
import os
import re
import sys
import time
import urllib.parse

import horizons_check as hc
from export_objects import served_identity

ROOT = os.path.dirname(os.path.abspath(__file__))
SOURCE = "celestial_objects.py"
PLANS = os.path.join("data", "path_plans.json")
PREVIEW = os.path.join("data", "path_plans_preview.json")

# TEMPORARY, until the twelve are keyed (L-443 slice 2, the website half):
# group A of documentation/DESIGN_L443_slice2_rulings_20261023.md, by the
# list's own names. A key in the export with no website entry stops the
# website's objects mirror, so the keys land with the website's entries;
# meanwhile --preview plans these by name, into PREVIEW, which the export
# never reads, so the first real flyby list comes from Tony's machine.
# Remove this list, the flag and its dashboard button when they are keyed.
PREVIEW_NAMES = ("Voyager 1", "Voyager 2", "New Horizons", "Juno", "Lucy",
                 "JUICE", "Psyche", "Clipper", "BepiColombo", "SolO",
                 "Parker", "OSIRISAPE")
SCHEMA = 1
CADENCE_DAYS = 30
KEEP_PAST_DAYS = 30        # events older than this are carried, not re-found
OVERLAP_DAYS = 3           # the re-search starts this much before them
PAUSE_SECONDS = 1.0

# The backbone: Voyager 1's proven numbers (gallery config, 2026-07-11),
# now in one place for every path.
BACKBONE_STEP = "7d"
BACKBONE_STEP_SECONDS = 7 * 86400.0
THIN_TOL_AU = 0.02

# Searched around: Horizons' major-body ids (numeric, so Horizons can
# centre on them), then every served small body.
MAJOR_BODIES = [
    ("Sun", "10"), ("Mercury", "199"), ("Venus", "299"), ("Earth", "399"),
    ("Moon", "301"), ("Mars", "499"), ("Jupiter", "599"), ("Saturn", "699"),
    ("Uranus", "799"), ("Neptune", "899"), ("Pluto", "999"),
]

from constants_new import KM_PER_AU as AU_KM   # the store's AU, as
                                                # spacecraft_encounters uses
DAY_S = 86400.0
COARSE_STEP = "1d"
PASS_ONE = (1.5, "1h")     # days either side, step
PASS_TWO = (90, "1m")      # minutes either side, step
LINE = "=" * 70


class Unreachable(Exception):
    """JPL could not be reached, or its answer could not be read."""


class Refused(Exception):
    """JPL answered, and gave no positions for what was asked."""


# ------------------------------------------------------------ the list

def _value(node):
    """A literal, or a datetime(y, m, d[, ...]) call as a datetime."""
    if (isinstance(node, ast.Call) and getattr(node.func, "id", None)
            == "datetime"):
        return datetime.datetime(*[ast.literal_eval(a) for a in node.args])
    return ast.literal_eval(node)


FIELDS = ("name", "key", "id", "id_type", "helio_id", "helio_id_type",
          "object_type", "start_date", "end_date")


def keyed_entries(text, preview=False):
    """[{fields}] for every entry with a 'key', in list order. With
    preview, also each entry named in PREVIEW_NAMES, keyed by its name."""
    tree = ast.parse(text)
    node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(
        getattr(t, "id", None) == "OBJECT_DEFINITIONS" for t in n.targets))
    out = []
    for entry in node.value.elts:
        f = {}
        for k, v in zip(entry.keys, entry.values):
            if isinstance(k, ast.Constant) and k.value in FIELDS:
                f[k.value] = _value(v)
        if f.get("key"):
            out.append(f)
        elif preview and f.get("name") in PREVIEW_NAMES:
            f["key"] = "preview_" + re.sub(r"[^a-z0-9]+", "_",
                                           f["name"].lower()).strip("_")
            out.append(f)
    return out


def is_spacecraft(f):
    return (f.get("object_type") == "trajectory"
            and str(f.get("id", "")).startswith("-"))


# Whose gravity a body's Hill sphere is reckoned against: the Moon's
# against Earth's, every other body's against the Sun's.
PRIMARY = {"301": "399"}


def searched_bodies(entries):
    """[(name, kind, ident, id_type)]: the major bodies, then each served
    small body by the record the website serves it by."""
    out = [(n, "major", i, None) for n, i in MAJOR_BODIES]
    majors = set(i for _, i in MAJOR_BODIES)
    for f in entries:
        if is_spacecraft(f):
            continue
        ident, id_type = served_identity(f)
        if ident is None or ident in majors:
            continue
        if id_type in ("smallbody", "designation", "asteroid_name",
                       "comet_name"):
            out.append((f["name"], "small", ident, id_type))
    return out


# ------------------------------------------------------------- queries

def vectors_url(ident, id_type, center, start, stop, step):
    """Positions and velocities around center, in AU and days, ecliptic,
    as CSV. Times are TDB, Horizons' scale for a vector table."""
    command = hc.command_of(ident, id_type) if id_type else str(ident)
    return ("%s?format=text&COMMAND='%s'&OBJ_DATA=NO&MAKE_EPHEM=YES"
            "&EPHEM_TYPE=VECTORS&CENTER='%s'&START_TIME='%s'"
            "&STOP_TIME='%s'&STEP_SIZE='%s'&OUT_UNITS='AU-D'"
            "&REF_PLANE='ECLIPTIC'&REF_SYSTEM='ICRF'&VEC_TABLE='2'"
            "&CSV_FORMAT='YES'&VEC_LABELS='NO'"
            % (hc.MAIN, urllib.parse.quote(command, safe="="), center,
               urllib.parse.quote(start), urllib.parse.quote(stop), step))


def sheet_url(ident, id_type):
    command = hc.command_of(ident, id_type) if id_type else str(ident)
    return ("%s?format=text&COMMAND='%s'&OBJ_DATA=YES&MAKE_EPHEM=NO"
            % (hc.MAIN, urllib.parse.quote(command, safe="=")))


# JPL prints a major body's GM three ways (read 2026-10-24 from the
# sheets of 399, 599, 301, 10 and 999): "GM, km^3/s^2 = ...",
# "GM (km^3/s^2) = ..." and "GM (planet) km^3/s^2 = ...". A small body's
# sheet writes "GM= <value>" or "GM= n.a." (none). Never the "GM 1-sigma"
# line.
GM = re.compile(r"\bGM(?!\s*1-sigma)(?:,|\s*\(|(?==))[^=\n]{0,24}=\s*"
                r"([0-9]+(?:\.[0-9]*)?(?:[Ee][-+]?[0-9]+)?)")


def parse_gm(text):
    """JPL's GM for a body in km^3/s^2, or None where its sheet gives
    none. Raises Unreachable when the answer is not JPL's."""
    if "API VERSION" not in text:
        raise Unreachable("the answer is not one of JPL's")
    m = GM.search(text)
    return float(m.group(1)) if m else None


def parse_vectors(text):
    """[(jd, x, y, z, vx, vy, vz)] from a CSV vector answer. Raises
    Unreachable when the answer is not JPL's, ValueError when JPL refused."""
    if "API VERSION" not in text:
        raise Unreachable("the answer is not one of JPL's")
    if "$$SOE" not in text or "$$EOE" not in text:
        raise Refused("JPL's answer holds no vectors: %s"
                         % " ".join(text.strip().splitlines()[-2:])[:200])
    rows = []
    block = text[text.index("$$SOE") + 5:text.index("$$EOE")]
    for line in block.strip().splitlines():
        cells = [c.strip() for c in line.split(",")]
        if len(cells) < 8:
            continue
        nums = [float(cells[0])] + [float(c) for c in cells[2:8]]
        rows.append(tuple(nums))
    if not rows:
        raise Refused("JPL's vector table is empty")
    return rows


def ask(fetch, url, pause):
    try:
        text = fetch(url)
    except hc.Unreachable as exc:
        raise Unreachable(str(exc))
    if pause:
        time.sleep(pause)
    try:
        return parse_vectors(text)
    except ValueError as exc:            # a number JPL printed unreadably
        raise Unreachable("JPL's answer could not be read: %s" % exc)


def ymd(d):
    return d.strftime("%Y-%m-%d")


# Asked to this day, so JPL itself names where its positions for a path
# end: the list's end_date goes stale as JPL extends or shortens a plan
# (on 2026-10-24 Juno's ran past JPL's data, New Horizons' stopped 21
# years short of it).
FAR_STOP = datetime.date(2100, 1, 1)
LIMIT = re.compile(r'No ephemeris for target "[^"]*" (prior to|after) A\.D\. '
                   r'(\d{4})-([A-Z]{3})-(\d{2})(?: (\d{2}):(\d{2}))?')
MONTHS = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP",
          "OCT", "NOV", "DEC")


def jpl_limit(text):
    """('prior to' | 'after', date) from JPL's refusal, or None. The limit
    is to the second; a whole day inside it is used, a day earlier for an
    end that falls in the first minutes of a day (JPL states it in UT and
    the table is asked in TDB, about a minute apart)."""
    m = LIMIT.search(text or "")
    if not m:
        return None
    day = datetime.date(int(m.group(2)), MONTHS.index(m.group(3)) + 1,
                        int(m.group(4)))
    if m.group(1) == "prior to":
        return "prior to", day + datetime.timedelta(days=1)
    early = m.group(5) is not None and int(m.group(5)) == 0 and \
        int(m.group(6)) < 5
    return "after", day - datetime.timedelta(days=1) if early else day


def path_rows_and_span(fetch, path, pause):
    """(rows, first day, last day): the path's daily positions around the
    Sun across everything JPL has for it, from the list's start_date (the
    launch) to FAR_STOP, clipped to the limits JPL names when it refuses.
    Raises Unreachable, or Refused with JPL's words when it refuses for
    another reason."""
    first = path["start_date"].date()
    last = FAR_STOP
    for _ in range(4):
        try:
            text = fetch(vectors_url(path["id"], path["id_type"], "500@10",
                                     ymd(first), ymd(last), COARSE_STEP))
        except hc.Unreachable as exc:
            raise Unreachable(str(exc))
        if pause:
            time.sleep(pause)
        try:
            return parse_vectors(text), first, last
        except ValueError as exc:
            raise Unreachable("JPL's answer could not be read: %s" % exc)
        except Refused as exc:
            limit = jpl_limit(text)
            if limit is None:
                raise
            if limit[0] == "after":
                last = limit[1]
            else:
                first = limit[1]
            if first >= last:
                raise Refused("JPL's limits leave no span: %s" % exc)
    raise Refused("JPL kept refusing the span after four tries")


def jd_to_calendar(jd):
    """'YYYY-MM-DD HH:MM' for a Julian date, on the same calendar as
    horizons_check.calendar_jd (which it inverts to the minute)."""
    z = math.floor(jd + 0.5)
    f = jd + 0.5 - z
    a = z
    if z >= 2299161:
        alpha = math.floor((z - 1867216.25) / 36524.25)
        a = z + 1 + alpha - math.floor(alpha / 4)
    b = a + 1524
    c = math.floor((b - 122.1) / 365.25)
    d = math.floor(365.25 * c)
    e = math.floor((b - d) / 30.6001)
    day = b - d - math.floor(30.6001 * e)
    month = e - 1 if e < 14 else e - 13
    year = c - 4716 if month > 2 else c - 4715
    minutes = int(round(f * 1440))
    if minutes == 1440:
        nd = (datetime.date(int(year), int(month), int(day))
              + datetime.timedelta(days=1))
        year, month, day, minutes = nd.year, nd.month, nd.day, 0
    return "%04d-%02d-%02d %02d:%02d" % (year, month, day,
                                         minutes // 60, minutes % 60)


# ------------------------------------------------------------- geometry

def ideal_step_seconds(dist_km, v_kms):
    """The orrery's curvature rule: about 30 points through a half circle
    at the passing distance and speed
    (spacecraft_encounters._calculate_encounter_resolution)."""
    return math.pi * dist_km / v_kms / 30.0


def _rel(a, b):
    """distance km, speed km/s between two rows (jd, x, y, z, vx, vy, vz)."""
    dx, dy, dz = a[1] - b[1], a[2] - b[2], a[3] - b[3]
    dv = (a[4] - b[4], a[5] - b[5], a[6] - b[6])
    return (math.sqrt(dx * dx + dy * dy + dz * dz) * AU_KM,
            math.sqrt(sum(c * c for c in dv)) * AU_KM / DAY_S)


def hill_km(body_row, primary_row, gm, gm_primary):
    """The body's Hill sphere radius in km at a moment: its distance from
    its primary times (GM / (3 GM of the primary)) ** (1/3). None for the
    Sun, the drawing's own centre, which has no Hill sphere here."""
    if gm is None or gm_primary is None or primary_row is None:
        return None
    r, _ = _rel(body_row, primary_row)
    return r * (gm / (3.0 * gm_primary)) ** (1.0 / 3.0)


def candidates(path_rows, body_rows, gate=None):
    """[(jd, dist_km, v_kms)] at each day nearer than the days either side
    that could be a pass needing finer steps than the backbone: inside the
    body's Hill sphere (gate(jd) gives its radius, None for the Sun), and
    bending faster than the backbone draws by the curvature rule. A daily
    sample can sit up to half a day's travel from the true nearest moment,
    so both tests use the distance less half a day's travel."""
    by_jd = dict((round(r[0], 4), r) for r in body_rows)
    series = []
    for r in path_rows:
        b = by_jd.get(round(r[0], 4))
        if b is not None:
            d, v = _rel(r, b)
            series.append((r[0], d, v))
    out = []
    for i in range(1, len(series) - 1):
        jd, d, v = series[i]
        if d < series[i - 1][1] and d <= series[i + 1][1] and v > 0:
            lower = max(d - v * DAY_S / 2.0, 1.0)
            hill = gate(jd) if gate else None
            if hill is not None and lower > hill:
                continue
            if ideal_step_seconds(lower, v) < BACKBONE_STEP_SECONDS:
                out.append((jd, d, v))
    return out


def refine(fetch, path, body, jd, pause):
    """(jd, dist_km, v_kms) at the nearest minute, in the two passes."""
    def rows(start_jd, stop_jd, step):
        start, stop = jd_to_calendar(start_jd), jd_to_calendar(stop_jd)
        if body[1] == "major":
            got = ask(fetch, vectors_url(path["id"], path["id_type"],
                                         "500@" + body[2], start, stop, step),
                      pause)
            zero = (0.0,) * 6
            return [(r[0], _rel(r, (r[0],) + zero)) for r in got]
        a = ask(fetch, vectors_url(path["id"], path["id_type"], "500@10",
                                   start, stop, step), pause)
        b = dict((round(r[0], 6), r) for r in ask(
            fetch, vectors_url(body[2], body[3], "500@10", start, stop, step),
            pause))
        return [(r[0], _rel(r, b[round(r[0], 6)])) for r in a
                if round(r[0], 6) in b]

    days, step = PASS_ONE
    one = rows(jd - days, jd + days, step)
    best = min(one, key=lambda t: t[1][0])
    minutes, step = PASS_TWO
    two = rows(best[0] - minutes / 1440.0, best[0] + minutes / 1440.0, step)
    best = min(two, key=lambda t: t[1][0])
    return best[0], best[1][0], best[1][1]


def window_and_step(jd, dist_km, v_kms):
    """(start, end, step) by spacecraft_encounters' own rule. Its steps
    stop at six hours; where the ideal step is a day or more, the step is
    whole days, never more than the ideal."""
    from spacecraft_encounters import _calculate_encounter_resolution
    enc = {"dist_km": dist_km, "v_kms": v_kms,
           "date": jd_to_calendar(jd)}
    res = _calculate_encounter_resolution(enc)
    if res is None:
        raise ValueError("the encounter rule gave no window")
    ideal = ideal_step_seconds(dist_km, v_kms)
    step = res["fetch_step"]           # the orrery's steps, up to 6h
    if ideal >= DAY_S:
        step = "%dd" % int(ideal // DAY_S)
    return (res["start_dt"].strftime("%Y-%m-%d %H:%M"),
            res["end_dt"].strftime("%Y-%m-%d %H:%M"), step)


# ------------------------------------------------------------- planning

def plan_inputs(path, bodies):
    return {"id": path["id"], "id_type": path.get("id_type"),
            "span": [ymd(path["start_date"]), ymd(path["end_date"])],
            "searched": [b[2] for b in bodies]}


def inputs_sha256(inputs):
    return hashlib.sha256(json.dumps(inputs, sort_keys=True)
                          .encode("ascii")).hexdigest()


def due(previous, inputs, today):
    """(due, why) for one path."""
    if previous is None:
        return True, "never planned"
    if previous.get("inputs_sha256") != inputs_sha256(inputs):
        return True, "what it was made from changed"
    made = datetime.date.fromisoformat(previous["made"])
    if (today - made).days >= CADENCE_DAYS:
        return True, "made %s, %d days ago" % (previous["made"],
                                               (today - made).days)
    return False, "made %s" % previous["made"]


def search_start(path, previous, inputs, today, start=None, end=None):
    """(first day to search, events carried from the previous plan),
    within the span JPL gave (start, end; the previous plan's span when
    none is given yet)."""
    if start is None:
        span = (previous or {}).get("span") or {}
        start = (datetime.date.fromisoformat(span["start"]) if span
                 else path["start_date"].date())
        end = (datetime.date.fromisoformat(span["end"]) if span
               else path["end_date"].date())
    if (previous is None
            or previous.get("inputs_sha256") != inputs_sha256(inputs)):
        return start, []
    cut = today - datetime.timedelta(days=KEEP_PAST_DAYS)
    carried = [e for e in previous.get("events", [])
               if e["closest"][:10] < ymd(cut)]
    begin = max(start, cut - datetime.timedelta(days=OVERLAP_DAYS))
    # A path that ended before the cut has nothing left to look at: its
    # events are all carried and nothing is asked.
    return (min(begin, end), carried)


class BodyRows(object):
    """Each searched body's daily positions around the Sun, fetched once
    across every due path's span and shared. A body JPL gives nothing
    for is named once and left out, and never stops the run."""

    def __init__(self, fetch, first, last, pause):
        self.fetch, self.pause = fetch, pause
        self.first, self.last = ymd(first), ymd(last)
        self.rows, self.refused, self.gms = {}, {}, {}

    def gm(self, body):
        """JPL's GM for the body, read once from its sheet; None (and the
        body named) where the sheet gives none."""
        k = body[2]
        if k not in self.gms:
            try:
                text = self.fetch(sheet_url(body[2], body[3]))
            except hc.Unreachable as exc:
                raise Unreachable(str(exc))
            if self.pause:
                time.sleep(self.pause)
            self.gms[k] = parse_gm(text)
            if self.gms[k] is None and k != "10":
                self.refused[k] = ("%s: its JPL data sheet gives no GM, so "
                                   "it has no Hill sphere to pass inside"
                                   % body[0])
        return self.gms[k]

    def get(self, body):
        k = body[2]
        if k in self.refused:
            return None
        if body[2] != "10":
            self.gm(body)
            if k in self.refused:
                return None
        if k not in self.rows:
            try:
                self.rows[k] = ask(self.fetch, vectors_url(
                    body[2], body[3], "500@10", self.first, self.last,
                    COARSE_STEP), self.pause)
            except Refused as exc:
                self.refused[k] = "%s: %s" % (body[0], exc)
                return None
        return self.rows[k]


def make_plan(fetch, path, bodies, today, rows, previous=None, pause=0.0,
              found=None):
    """One path's plan. found is (rows, start, end) from
    path_rows_and_span, or None for a path with nothing left to search.
    Raises Unreachable."""
    inputs = plan_inputs(path, bodies)
    if found is None:
        span = previous["span"]
        start = datetime.date.fromisoformat(span["start"])
        end = datetime.date.fromisoformat(span["end"])
    else:
        all_rows, start, end = found
    begin, carried = search_start(path, previous, inputs, today, start, end)
    if found is None or begin >= end:
        return {"name": path["name"], "horizons_id": path["id"],
                "id_type": path.get("id_type"), "kind": "spacecraft",
                "made": ymd(today), "inputs_sha256": inputs_sha256(inputs),
                "span": {"start": ymd(start), "end": ymd(end)},
                "backbone": {"step": BACKBONE_STEP,
                             "thin_tol_au": THIN_TOL_AU},
                "events": list(carried), "carried": len(carried),
                "searched_from": ymd(end),
                "searched": list(previous.get("searched", []))}
    begin_jd = hc.calendar_jd(ymd(begin))
    path_rows = [r for r in all_rows if r[0] >= begin_jd - 1e-6]
    events = list(carried)
    searched = []
    sun = ("Sun", "major", "10", None)
    for body in bodies:
        body_rows = rows.get(body)
        if body_rows is None:
            continue
        searched.append(body[0])
        gate = None
        if body[2] != "10":
            prim = next((b for b in bodies
                         if b[2] == PRIMARY.get(body[2], "10")), sun)
            prim_rows = rows.get(prim) if prim[2] != "10" else None
            gm_b, gm_p = rows.gm(body), rows.gm(prim)
            at = dict((round(r[0], 4), r) for r in body_rows)
            pat = (dict((round(r[0], 4), r) for r in prim_rows)
                   if prim_rows else None)

            def gate(jd, at=at, pat=pat, gm_b=gm_b, gm_p=gm_p):
                b = at.get(round(jd, 4))
                p = (pat.get(round(jd, 4)) if pat is not None
                     else (jd,) + (0.0,) * 6)
                if b is None or p is None:
                    return 0.0
                return hill_km(b, p, gm_b, gm_p)
        for jd, _, _ in candidates(path_rows, body_rows, gate):
            try:
                fjd, d, v = refine(fetch, path, body, jd, pause)
            except Refused as exc:
                raise Unreachable("JPL gave no positions around %s near %s "
                                  "(%s)" % (body[0], jd_to_calendar(jd), exc))
            if any(e["body"] == body[0] and abs(e["jd"] - fjd) < 1.0
                   for e in events):
                continue
            ideal = ideal_step_seconds(d, v)
            if ideal >= BACKBONE_STEP_SECONDS:
                continue
            hill = gate(jd) if gate else None
            if hill is not None and d > hill:
                continue
            w0, w1, step = window_and_step(fjd, d, v)
            events.append({"body": body[0], "body_id": body[2],
                           "closest": jd_to_calendar(fjd),
                           "jd": round(fjd, 6), "dist_km": round(d, 1),
                           "v_kms": round(v, 3),
                           "ideal_step_s": round(ideal, 1),
                           "hill_km": None if hill is None else round(hill),
                           "window": [w0, w1], "step": step})
    events.sort(key=lambda e: e["jd"])
    return {"name": path["name"], "horizons_id": path["id"],
            "id_type": path.get("id_type"), "kind": "spacecraft",
            "made": ymd(today), "inputs_sha256": inputs_sha256(inputs),
            "span": {"start": ymd(start), "end": ymd(end)},
            "backbone": {"step": BACKBONE_STEP, "thin_tol_au": THIN_TOL_AU},
            "events": events, "carried": len(carried),
            "searched_from": ymd(begin), "searched": searched}


def render(plans):
    return json.dumps(plans, indent=1, sort_keys=True) + "\n"


def run(root, fetch, today, check_all=False, pause=PAUSE_SECONDS,
        preview=False):
    """(verdict, lines, plans). Writes data/path_plans.json when it changes;
    with preview, data/path_plans_preview.json for PREVIEW_NAMES instead."""
    with open(os.path.join(root, SOURCE), "r", encoding="utf-8") as handle:
        entries = keyed_entries(handle.read(), preview)
    paths = [f for f in entries if is_spacecraft(f)]
    if preview:
        paths = [f for f in paths if f["name"] in PREVIEW_NAMES]
        missing = sorted(set(PREVIEW_NAMES) - set(f["name"] for f in paths))
    bodies = searched_bodies([f for f in entries
                              if not f["key"].startswith("preview_")])
    path_file = os.path.join(root, PREVIEW if preview else PLANS)
    old = {}
    if os.path.exists(path_file):
        with open(path_file, "r", encoding="utf-8") as handle:
            old = json.load(handle)
    plans = dict(old.get("plans") or {})
    lines, asked, unreachable, not_planned = [], [], [], []
    for gone in sorted(set(plans) - set(f["key"] for f in paths)):
        del plans[gone]
        lines.append("  %-22s removed: no longer a served path" % gone)
    todo = []
    for f in paths:
        key = f["key"]
        if not f.get("start_date") or not f.get("end_date"):
            not_planned.append(key)
            lines.append("  %-22s NOT PLANNED: the entry has no start_date "
                         "or end_date" % key)
            continue
        inputs = plan_inputs(f, bodies)
        is_due, why = due(plans.get(key), inputs, today)
        if is_due or check_all:
            todo.append((f, why if is_due else "asked with --all"))
        else:
            lines.append("  %-22s current (%s), %d events"
                         % (key, why, len(plans[key]["events"])))
    found, firsts, lasts = {}, [], []
    for f, why in todo:
        key, prev = f["key"], plans.get(f["key"])
        inputs = plan_inputs(f, bodies)
        if (prev is not None and prev.get("inputs_sha256")
                == inputs_sha256(inputs)
                and search_start(f, prev, inputs, today)[0]
                >= datetime.date.fromisoformat(prev["span"]["end"])):
            found[key] = None              # ended: nothing left to ask
            continue
        if unreachable:
            continue
        try:
            got = path_rows_and_span(fetch, f, pause)
        except Unreachable as exc:
            unreachable.append("%s (%s)" % (key, exc))
            continue
        except Refused as exc:
            not_planned.append(key)
            lines.append("  %-22s NOT PLANNED: JPL refused its positions: "
                         "%s" % (key, exc))
            continue
        found[key] = got
        firsts.append(search_start(f, prev, inputs, today, got[1], got[2])[0])
        lasts.append(got[2])
    rows = BodyRows(fetch, min(firsts), max(lasts), pause) if firsts else None
    for f, why in todo:
        key = f["key"]
        if key in not_planned:
            continue
        if any(u.startswith(key + " (") for u in unreachable):
            lines.append("  %-22s UNREACHABLE; its previous plan is kept"
                         % key)
            continue
        if key not in found or (unreachable and found[key] is not None):
            lines.append("  %-22s not asked: JPL was unreachable earlier "
                         "this run; its previous plan is kept" % key)
            continue
        try:
            plan = make_plan(fetch, f, bodies, today, rows, plans.get(key),
                             pause, found[key])
        except Unreachable as exc:
            unreachable.append("%s (%s)" % (key, exc))
            lines.append("  %-22s UNREACHABLE: %s; its previous plan is "
                         "kept" % (key, exc))
            continue
        plans[key] = plan
        asked.append(key)
        lines.append("  %-22s planned (%s): %d events, %d carried, "
                     "searched from %s" % (key, why, len(plan["events"]),
                                           plan["carried"],
                                           plan["searched_from"]))
        for e in plan["events"]:
            lines.append("      %s TDB  %-14s %13.0f km  %8.3f km/s  "
                         "step %s" % (e["closest"], e["body"], e["dist_km"],
                                      e["v_kms"], e["step"]))
    if rows is not None and rows.refused:
        lines.append("  Not searched: "
                     + "; ".join(sorted(rows.refused.values())))
    out = {"schema": SCHEMA, "cadence_days": CADENCE_DAYS,
           "backbone": {"step": BACKBONE_STEP, "thin_tol_au": THIN_TOL_AU},
           "plans": plans}
    content = render(out)
    os.makedirs(os.path.dirname(path_file), exist_ok=True)
    before = None
    if os.path.exists(path_file):
        with open(path_file, "rb") as handle:
            before = handle.read().replace(b"\r\n", b"\n")
    if before != content.encode("utf-8"):
        with open(path_file, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
    names = ", ".join("%s %d" % (k, len(plans[k]["events"]))
                      for k in sorted(plans)) or "none"
    if preview and missing:
        not_planned = not_planned + ["%s (not in the list)" % m
                                     for m in missing]
    tail = (" Not planned: %s." % ", ".join(not_planned)) if not_planned \
        else ""
    if unreachable:
        verdict = ("PATH PLAN: UNREACHABLE -- %s; kept as they were. "
                   "Paths and events: %s.%s" % ("; ".join(unreachable),
                                                names, tail))
    else:
        verdict = ("PATH PLAN: %d paths, events %s. Asked JPL for: %s.%s"
                   % (len(plans), names, ", ".join(asked) or "nothing",
                      tail))
    return verdict, lines, out


def main(argv):
    check_all = "--all" in argv
    preview = "--preview" in argv
    today = datetime.date.today()
    verdict, lines, _ = run(ROOT, hc.live_fetch, today, check_all,
                            preview=preview)
    print(LINE)
    print("PATH PLAN -- where each served path needs finer steps (L-443)%s"
          % (" -- PREVIEW of slice 2's twelve, into %s" % PREVIEW.replace(
              os.sep, "/") if preview else ""))
    print(LINE)
    for line in lines:
        print(line)
    print()
    print(verdict)
    return 1 if "UNREACHABLE" in verdict else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
