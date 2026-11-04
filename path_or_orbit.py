"""
path_or_orbit.py -- the one home of the rule that decides whether a small
body is drawn as a path or as an orbit: by the eccentricity of its orbit
solution in JPL's Small-Body Database, refreshed on the 30-day cycle
(L-510, part 1).

THE RULE

    A small body whose solution e is at or above 1 is drawn as a path, by
    its path plan, as 3I/ATLAS is; below 1, as an orbit. The typed
    'object_type' and the retired 'open_path' no longer decide it.

    Tony's rulings: 2026-11-03, 15:33 to 15:55 Chicago (L-484, L-510):
    "They should be drawn as all the Hyperbolic objects." "This is not a
    special class." "I would say e and JPL should agree. And as far as
    fetching we should update with the 30-day check." "How does JPL
    determine the class? By e." And 2026-11-04, on which e: "Use the e
    that JPL classes by: the orbit solution's eccentricity in JPL's
    small-body database, refreshed on the 30-day cycle. Not today's
    heliocentric osculating e."

    Why not the osculating e: McNaught (C/2006 P1). Its solution's e is
    1.000018816 (SBDB, epoch JD 2454065.5, 2006-11-26, class HYP), the
    e Horizons gives around the Sun at that epoch to the last digit. Its
    e around the Sun on 2026-11-04 is 0.999939767. Around the solar
    system's barycentre its e has held at 0.999916 since 2011 while the
    Sun-centred e swings about it (0.99991, 0.99997, 0.99990, 0.99994 on
    2011, 2016, 2021, 2026 Jan 1 or Nov 4): the swing is the Sun's own
    motion around the barycentre. All asked of JPL on 2026-11-04.

WHAT A SMALL BODY IS HERE

    An entry asked of JPL as a small body around the Sun: one with a
    'helio_id' (the record plotted around the Sun), one whose id_type is
    'smallbody', or a comet asked by JPL's permanent number as a
    'designation' (C/2025 K1 as 1004075). Never a spacecraft (an id
    starting with '-'). Every other entry keeps its typed object_type.

THE STORE

    data/small_body_solutions.json, written only by period_fetch.py in the
    maintenance run (refresh_due / fetch_solution / save_solutions), keyed
    by the entry's name: what SBDB was asked ('search'), the solution's e
    as JPL gave it (text, full precision), its class, epoch and full
    name, and the UTC date it was fetched. A record whose search is not
    the entry's search now is not the entry's: it is due, and the rule
    refuses it.

A NAMED FAILURE, NEVER A QUIET DEFAULT

    A small body with no record, or one asked of another search, raises
    NoSolution naming the body and why. The export, the path plan and the
    period fetch stop on it by name; the orrery's plot prints it by name
    and draws the body by neither its plan nor an ellipse
    (drawn_type_or_none).

    When the database's e and the osculating elements a drawing would use
    disagree about the side of 1, the drawing fails by name
    (side_disagreement): an ellipse is never drawn from elements whose
    solution is hyperbolic, nor a hyperbola from one that is closed.

Functions:
    is_small_body(f)                 -> bool
    search_of(f)                     -> what SBDB is asked for the entry
    load_solutions(root)             -> {name: record}
    solution_e(f, solutions)         -> float; raises NoSolution
    drawn_as_path(f, solutions)      -> bool; raises NoSolution
    drawn_type(f, solutions)         -> 'trajectory', 'orbital' or typed
    drawn_type_or_none(f)            -> as drawn_type; None, printed, on
                                        a NoSolution (the orrery's plot)
    side_disagreement(f, osc_e, s)   -> None, or the named failure
    refresh_due(f, solutions, today) -> None, or why it is asked again
    fetch_solution(search)           -> (record or None, why, reached)
    save_solutions(root, solutions)

Consumed by: palomas_orrery.py (the static plot and the animation),
idealized_orbits.py (the orbit drawing's side check), export_objects.py
(the export's open_path, read by horizons_check.py too), path_plan.py
(which comets are planned), period_fetch.py (the store's only writer).

Role: computation
Domain: orrery

Module created: November 4, 2026 with Anthropic's Claude Opus 5.5
(L-510, part 1: a small body drawn by its eccentricity).
"""

import datetime
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join("data", "small_body_solutions.json")
CYCLE_DAYS = 30
SBDB_API_URL = "https://ssd-api.jpl.nasa.gov/sbdb.api"


class NoSolution(Exception):
    """A small body the rule cannot decide: no solution e on record."""

    def __init__(self, name, why):
        Exception.__init__(self, "%s: %s" % (name, why))
        self.name = name
        self.why = why


def is_small_body(f):
    """True for an entry asked of JPL as a small body around the Sun."""
    ident = str(f.get("id", ""))
    if ident.startswith("-"):
        return False
    if f.get("helio_id") is not None:
        return True
    if f.get("id_type") == "smallbody":
        return True
    return f.get("id_type") == "designation" and ident.isdigit()


def search_of(f):
    """What the Small-Body Database is asked for this entry: its helio_id
    where it has one, else its id; a pinned Horizons record number by the
    name Horizons gives it (orbital_period.sbdb_search_string)."""
    from orbital_period import sbdb_search_string
    ident = f.get("helio_id")
    if ident is None:
        ident = f.get("id", f.get("name"))
    return sbdb_search_string(ident, f.get("horizons_name"))


_LOADED = {}


def load_solutions(root=ROOT):
    """{name: record} from the store; {} when there is none. Read again
    when the file changes on disk."""
    path = os.path.join(root, STORE)
    try:
        stamp = os.path.getmtime(path)
    except OSError:
        return {}
    held = _LOADED.get(path)
    if held and held[0] == stamp:
        return held[1]
    with open(path, "r", encoding="utf-8") as handle:
        solutions = json.load(handle).get("solutions") or {}
    _LOADED[path] = (stamp, solutions)
    return solutions


def _record(f, solutions):
    """The entry's record, or raises NoSolution."""
    name = f.get("name")
    rec = solutions.get(name)
    if rec is None:
        raise NoSolution(name, "no e from JPL's Small-Body Database on "
                               "record (%s); the period fetch asks it"
                         % STORE.replace(os.sep, "/"))
    want = search_of(f)
    if rec.get("search") != want:
        raise NoSolution(name, "its database e was asked of %r, and the "
                               "entry is now asked as %r"
                         % (rec.get("search"), want))
    return rec


def solution_e(f, solutions=None):
    """The solution's e as a float. Raises NoSolution."""
    if solutions is None:
        solutions = load_solutions()
    return float(_record(f, solutions)["e"])


def drawn_as_path(f, solutions=None):
    """True when a small body is drawn as a path: its solution e is at or
    above 1. False for an entry that is not a small body (a spacecraft is
    a path by its own rule, path_plan.is_spacecraft). Raises NoSolution."""
    if not is_small_body(f):
        return False
    return solution_e(f, solutions) >= 1.0


def drawn_type(f, solutions=None):
    """The object_type the orrery draws a body by: for a small body typed
    'orbital' or 'trajectory', 'trajectory' when it is drawn as a path
    and 'orbital' when as an orbit; for anything else its typed
    object_type, which still does that entry's other jobs. Raises
    NoSolution."""
    typed = f.get("object_type")
    if typed not in ("orbital", "trajectory") or not is_small_body(f):
        return typed
    return "trajectory" if drawn_as_path(f, solutions) else "orbital"


def drawn_type_or_none(f, solutions=None):
    """drawn_type for the orrery's plot: on a NoSolution, the failure is
    printed by name and None returned, so the body is drawn by neither its
    plan nor an ellipse, only by the positions JPL gives for the plot's
    dates."""
    try:
        return drawn_type(f, solutions)
    except NoSolution as exc:
        print("[PATH OR ORBIT] FAILED %s; drawn by neither its plan nor "
              "an orbit" % exc, flush=True)
        return None


def side_disagreement(f, osc_e, solutions=None):
    """None when the osculating e a drawing would use sits on the same
    side of 1 as the database's e; otherwise the named failure, as text.
    A small body with no database e is a failure too."""
    if not is_small_body(f):
        return None
    try:
        db_e = solution_e(f, solutions)
    except NoSolution as exc:
        return str(exc)
    try:
        osc = float(osc_e)
    except (TypeError, ValueError):
        return "%s: the elements to draw carry no e" % f.get("name")
    if (db_e >= 1.0) != (osc >= 1.0):
        return ("%s: JPL's Small-Body Database gives e = %s (%s), the "
                "elements to draw give e = %.9f (%s); no orbit is drawn "
                "from elements on the other side of 1"
                % (f.get("name"), _record(f, solutions or load_solutions())
                   ["e"], "open" if db_e >= 1.0 else "closed", osc,
                   "open" if osc >= 1.0 else "closed"))
    return None


def refresh_due(f, solutions, today):
    """None when the entry's record is current; otherwise why it is asked
    again: none on record, asked of another search, or CYCLE_DAYS old."""
    rec = solutions.get(f.get("name"))
    if rec is None:
        return "no database e on record"
    if rec.get("search") != search_of(f):
        return "asked of %r, now %r" % (rec.get("search"), search_of(f))
    try:
        age = (today - datetime.date.fromisoformat(rec["fetched"])).days
    except (KeyError, TypeError, ValueError):
        return "its fetched date cannot be read"
    if age >= CYCLE_DAYS:
        return "database e %d days old" % age
    return None


def fetch_solution(search, today, get=None):
    """(record or None, why, reached). reached is False only when JPL
    could not be reached; an answer with no single orbit is reached and
    has no record, with why naming it."""
    if get is None:
        import requests
        get = lambda params: requests.get(SBDB_API_URL, params=params,
                                          timeout=30).json()
    try:
        data = get({"sstr": search, "full-prec": "1"})
    except Exception as exc:
        return None, "SBDB not reached (%s)" % exc.__class__.__name__, False
    if "list" in data:
        return None, "SBDB found several matches for %r" % search, True
    orbit = data.get("orbit") if isinstance(data, dict) else None
    if not orbit:
        return None, "SBDB has no entry for %r" % search, True
    elements = dict((el.get("name"), el.get("value"))
                    for el in orbit.get("elements") or [])
    try:
        float(elements.get("e"))
    except (TypeError, ValueError):
        return None, "SBDB gives no e for %r" % search, True
    obj = data.get("object") or {}
    return {
        "search": search,
        "e": elements["e"],
        "class": (obj.get("orbit_class") or {}).get("code"),
        "epoch_jd": orbit.get("epoch"),
        "fullname": obj.get("fullname"),
        "fetched": today.isoformat(),
    }, "fetched", True


def save_solutions(root, solutions):
    """Written sorted, LF, ASCII; the file says what it is."""
    path = os.path.join(root, STORE)
    content = json.dumps({
        "note": ("Each small body's orbit-solution eccentricity from JPL's "
                 "Small-Body Database (sbdb.api, full-prec), which decides "
                 "whether the orrery and the website draw it as a path (e "
                 "at or above 1) or an orbit. Written by period_fetch.py on "
                 "the 30-day cycle; read by path_or_orbit.py (L-510)."),
        "solutions": dict(sorted(solutions.items())),
    }, indent=1, ensure_ascii=True) + "\n"
    with open(path + ".tmp", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)
    os.replace(path + ".tmp", path)
    _LOADED.pop(path, None)
