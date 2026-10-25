"""
export_objects.py -- write data/objects_export.json from the object list
in celestial_objects.py. The orrery is the one definition of each object;
the gallery reads this file and never reads orrery source.

RUN COMMAND
-----------
Open this file in VS Code and click Run. It takes no arguments.

    python export_objects.py

orrery_maintenance_run.py runs it on every maintenance run, as a
GENERATOR, beside export_constants.py. Running it by hand is the same
thing.

WHICH ENTRIES ARE EXPORTED
--------------------------
Only an entry in OBJECT_DEFINITIONS that carries a 'key' field. The key
is the website's name for the object, spelled exactly as the website's
data/objects_config.json spells its "slug" ('mars', 'pluto_barycenter').
It is never shown to anyone, so renaming a display name cannot break the
link (Tony's ruling, 2026-10-01, L-395). An entry gains a key when the
website starts serving it, and not before.

WHAT IT WRITES
--------------
One JSON file, data/objects_export.json:

    schema          3 (2 from L-431's build 3, 2026-10-14, which added
                    each object's period and confirmation; 3 from L-443's
                    slice 2, 2026-10-24, which added each path's plan)
    source_sha256   the sha256 of celestial_objects.py, CRLF normalised
                    to LF, so test_objects_export.py can tell whether the
                    list moved after the export was made
    period_inputs_sha256
                    the sha256 of what the periods were read from: each
                    keyed entry's slice of the orbit cache (its period
                    record and its elements) and the typed values used.
                    The cache is an input since build 3; the fingerprint
                    names exactly what of it was read, so an unrelated
                    entry Tony fetches does not make the export stale
    confirmations_sha256
                    the sha256 of data/horizons_confirmations.json, CRLF
                    normalised, which horizons_check.py writes just
                    before this runs in the maintenance run
    paths_sha256    the sha256 of data/path_plans.json, CRLF normalised,
                    which path_plan.py writes just before this runs
    cadence_days    30: how often JPL re-confirms each entry. The
                    website's offline check reads it from here, so the
                    two repositories cannot disagree about the cycle
    objects         one entry per key, in list order:
                      name         the entry's 'name'
                      horizons_id  the entry's 'id', or its 'helio_id'
                                   where it has one: the record the
                                   orrery plots a body by when the Sun
                                   is the centre, which the Sun-centred
                                   rooms serve (L-443)
                      horizons_name the entry's 'horizons_name', JPL's
                                   exact name for the object. The
                                   Horizons check compares it (L-395)
                      object_type  the entry's 'object_type'. The check
                                   compares it for "barycenter" and the
                                   Sun's "fixed" only
                      id_type      the entry's 'id_type' ('helio_id_type',
                                   else 'smallbody', for a helio_id), or
                                   null where
                                   the entry leaves it blank. A blank is
                                   not a value: the gallery keeps its own
                                   where the list states none
                      description  the entry's 'mission_info', with the
                                   opening "Horizons: ..." sentence
                                   removed when it has one. The website
                                   prints the Horizons id on its own
                                   source line, so the opening is the
                                   orrery's and stays in the orrery
                                   (Tony's ruling, 2026-10-01)
                      info_url     the entry's 'mission_url', or null
                      period       the body's orbital period, by the
                                   orrery's fallback order (L-431, Tony's
                                   ruling 5): see PERIOD below. null for
                                   the Sun, which orbits nothing here,
                                   and for a spacecraft, which has no
                                   orbital period (L-443 build B)
                      path         a spacecraft's only (a trajectory whose
                                   id starts with '-'): its plan from
                                   data/path_plans.json -- made, span,
                                   backbone, events, searched -- or null
                                   until path_plan.py has made one
                                   (L-443 slice 2)
                      confirmation when JPL last confirmed the entry and
                                   what it confirmed, copied from
                                   data/horizons_confirmations.json:
                                   "identity" (the id, id_type and
                                   horizons_name) and "period" (the
                                   period, its centre and date), each
                                   null until JPL has confirmed it
    numbers         for each key whose description holds a digit, the
                    numbers it holds, as written. Reported, so that no
                    number reaches the website unseen: a number in a
                    served description is sourced or comes out
                    (provenance-discipline, Fetched vs Recalled)

PERIOD (L-431, build 3)
-----------------------
The period the orrery's own hover shows for the body seen from the Sun,
read from the period record the orbit cache keeps beside the entry's
elements (data/osculating_cache.json, under the entry's name; the record
is written by orbital_period.build_period_record when Tony accepts an
elements update, or by period_fetch.py in the maintenance run, just
before this, for a served body that has none fetched, L-444). Its parts:

    kind         "fetched" (from JPL Horizons), "typed" (the orrery's
                 typed table KNOWN_ORBITAL_PERIODS, used only when
                 nothing was fetched), or "none" (neither)
    typed        true for a typed value, so no reader mistakes it for
                 JPL's
    center       the Horizons centre the period is taken around, "@sun"
                 or "@0" (the solar system's barycentre); null unless
                 fetched
    center_label the hover's words for that centre, from
                 orbital_period.centre_label, so the website's sentence
                 and the orrery's name the centre alike
    target       (fetched only, L-445) the Horizons id the period was
                 asked of: the record's 'target', or, for a record saved
                 before L-445, the id its elements fetch asked. Earth's
                 is "3", the Earth-Moon barycentre; every other body's is
                 its own id
    target_label (fetched only, L-445) the words for whose period it is
                 when that is not the body itself ("the Earth-Moon
                 center of mass"), else null. The orrery's hover and the
                 website's sentence both print "for <it>," before the
                 centre when it is not null
    years, days  each {"value", "figures", "text"}: the period printed to
                 the place its own error earns (orbital_period.
                 format_by_error, the orrery's digits rule), the value
                 that print shows, and its figure count. The website
                 prints the value at that count and never recounts it;
                 years and days are each placed by their own error
                 (ruling 3). A typed value prints as typed, its years
                 to the same count (orbital_period._typed_strings), as
                 the orrery's hover does, and each count is the figures
                 that print shows
    open_orbit   true when JPL gives no period (an open orbit)
    fetched      the date JPL was asked, or null
    words        the sentence a typed or missing period carries in the
                 orrery: "Typed value, not fetched from JPL." The website
                 prints the same words, so the two agree
    record       for a fetched period only, what the check and the test
                 need and the website does not show: the full days, its
                 error and what governs it (the year's change or SBDB's
                 sigma), SBDB's status words, the date the period is
                 taken at (epoch), the elements Horizons gave around the
                 period's centre at that date and, when that centre is
                 not the Sun, the Sun-centred elements of the same date
                 ("sun_elements") with "paired": true. A barycentre
                 ellipse is placed in a Sun-centred scene by pairing the
                 two at one date (horizons-orbital-mechanics, The Drawn
                 Orbit Follows the Period's Centre); when the cache's
                 Sun-centred elements are from another date they are not
                 paired, "paired" is false and "not_paired" says why, as
                 the orrery then draws the body from its Sun-centred
                 elements. A period asked of another body (a target_label)
                 is never paired: its elements are that body's (L-445). Tony, 2026-10-13, asked whether the
                 heliocentric data should also be fetched; it already
                 is, and it travels with the barycentre set: "confirmed."

WHAT MAKES IT FAIL (exit 1, and NOTHING is written)
---------------------------------------------------
    - celestial_objects.py does not parse, or OBJECT_DEFINITIONS is not a
      list of dict literals
    - an entry writes the same field twice (the second silently wins in
      Python, so one of the two is invisible)
    - a key that is not lower-case letters, digits and underscores, or
      two entries with the same key
    - a keyed entry whose name, id, mission_info or mission_url is not a
      plain literal
    - a keyed entry with no 'horizons_name', or one that is not a
      non-empty string: the Horizons check has nothing to compare JPL's
      name with (L-395)
    - an exported description that still says "Horizons:"
    - the orbit cache or the confirmations record cannot be read
    - a keyed entry's period record names no centre, or holds no days
      (a period with no centre cannot be printed or drawn honestly)
    - a keyed entry's period record names no target and its metadata no
      horizons_id, so nobody can say whose period it is (L-445)

The list is read with Python's own parser (ast), not imported, so the
export never runs the list's code and cannot be changed by it. The
digits rule and the centre's words are orbital_period.py's, imported:
one home for the rule the orrery's hover prints by.

DETERMINISTIC ON PURPOSE
------------------------
The same inputs give the same export bytes: no timestamp, no git SHA
(the gallery records the SHA it pulls at, as it does for the constants
export). Its inputs are celestial_objects.py, the keyed entries' slice
of data/osculating_cache.json, the typed periods in constants_new.py and
data/horizons_confirmations.json, each fingerprinted above. The file is
only written when its content would change, and always with LF line
endings.

Role: devtool
Domain: dev_tools

Module created: October 1, 2026 with Anthropic's Claude Opus 5.5
(L-395, the first build: the Solar System room's eleven bodies take
their names, Horizons ids, descriptions and NASA links from the orrery).
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-395,
the Horizons check: each object carries horizons_name and object_type,
and a keyed entry without a horizons_name is refused).
Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5 (L-431,
build 3, with L-395's move: schema 2. Each object carries its period, by
the orrery's fallback order and digits rule, with the elements around
its centre and, for a barycentre period, the Sun-centred set of the same
date; and its confirmation, copied from data/horizons_confirmations.json,
which horizons_check.py writes in the maintenance run just before this
runs. The orbit cache and the confirmations are inputs now, and both are
fingerprinted.)
Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5 (L-444:
the PERIOD section names period_fetch.py as the other writer of the
period record. Nothing this module does changed.)
Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5 (L-445,
Earth's period: a fetched period's block names its target, the id the
period was asked of, and its target_label when that is not the body;
a period asked of another body is never paired with this body's
elements; a record with no target and no horizons_id is refused.)
Module updated: October 24, 2026 with Anthropic's Claude Opus 5.5 (L-443,
slice 2: schema 3. Each served spacecraft carries its path's plan, which
path_plan.py writes in the maintenance run just before this runs; the
plans file is an input now, and fingerprinted.)
Module updated: October 25, 2026 with Anthropic's Claude Opus 5.5 (L-443,
build B: a spacecraft serves no period, null as the Sun's is, where the
period block would have said "Not yet fetched from JPL".)
Module updated: October 22, 2026 with Anthropic's Claude Opus 5.5 (L-443,
slice 1: a keyed entry with a 'helio_id' is served by it, as a small
body, through served_identity, so the Sun-centred rooms take the record
the orrery plots a body by around the Sun. No keyed entry had one
before.)
"""

import ast
import hashlib
import json
import os
import re
import sys

SOURCE = "celestial_objects.py"
TARGET = os.path.join("data", "objects_export.json")
CACHE = os.path.join("data", "osculating_cache.json")
CONFIRMATIONS = os.path.join("data", "horizons_confirmations.json")
PATHS = os.path.join("data", "path_plans.json")
SCHEMA = 3
CADENCE_DAYS = 30
KEY_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
OPENING = re.compile(r"^Horizons:[^.]*\.\s*")
NUMBER = re.compile(r"\d[\d,.]*\d|\d")
FIELDS = ("name", "id", "id_type", "mission_info", "mission_url",
          "horizons_name", "object_type", "helio_id", "helio_id_type")


def served_identity(f):
    """(horizons_id, id_type) the website serves for an entry's fields:
    its 'helio_id' where it has one, as a small-body designation
    ('helio_id_type', else 'smallbody', the type plotting gives a
    helio_id), else its 'id' and 'id_type'. The rooms are Sun-centred,
    and a helio_id is the record the orrery itself plots a body by when
    the Sun is the centre (L-443, Tony's ruling of 2026-10-22: a small
    body is served by its helio_id). period_fetch.py asks the period of
    the same record, so the period and the identity describe one body."""
    helio = f.get("helio_id")
    if helio is not None:
        return str(helio), f.get("helio_id_type") or "smallbody"
    hid = f.get("id")
    return (None if hid is None else str(hid)), f.get("id_type")


class ExportError(Exception):
    pass


def source_sha256(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def definitions(text):
    """The OBJECT_DEFINITIONS list node. Raises ExportError."""
    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        raise ExportError("%s does not parse: %s" % (SOURCE, exc))
    for node in tree.body:
        if (isinstance(node, ast.Assign)
                and any(getattr(t, "id", None) == "OBJECT_DEFINITIONS"
                        for t in node.targets)):
            if not isinstance(node.value, ast.List):
                raise ExportError("OBJECT_DEFINITIONS is not a list literal")
            return node.value
    raise ExportError("OBJECT_DEFINITIONS was not found in %s" % SOURCE)


def entry_label(entry):
    for k, v in zip(entry.keys, entry.values):
        if isinstance(k, ast.Constant) and k.value == "name":
            if isinstance(v, ast.Constant):
                return str(v.value)
    return "the entry at line %d" % entry.lineno


def repeated_fields(list_node):
    """[(entry label, field, [line numbers])] for every field written twice."""
    found = []
    for entry in list_node.elts:
        if not isinstance(entry, ast.Dict):
            raise ExportError("an item at line %d of OBJECT_DEFINITIONS is "
                              "not a dict literal" % entry.lineno)
        seen = {}
        for k in entry.keys:
            if isinstance(k, ast.Constant) and isinstance(k.value, str):
                seen.setdefault(k.value, []).append(k.lineno)
        for field, lines in seen.items():
            if len(lines) > 1:
                found.append((entry_label(entry), field, lines))
    return found


def literal_fields(entry):
    """{field: value} for the fields the export reads, as literals."""
    out = {}
    for k, v in zip(entry.keys, entry.values):
        if isinstance(k, ast.Constant) and k.value in FIELDS + ("key",):
            try:
                out[k.value] = ast.literal_eval(v)
            except ValueError:
                raise ExportError("%s: '%s' is not a plain literal"
                                  % (entry_label(entry), k.value))
    return out


def description_of(mission_info):
    text = (mission_info or "").strip()
    return OPENING.sub("", text, count=1).strip()


def build_objects(text):
    """(objects, numbers) for the list's source text: each keyed entry's
    identity, words and link, the fields schema 1 carried. The Horizons
    check reads the list through this, so it and the export see the same
    entries. Raises ExportError."""
    list_node = definitions(text)
    repeats = repeated_fields(list_node)
    if repeats:
        raise ExportError("; ".join(
            "%s writes '%s' %d times (lines %s)"
            % (label, field, len(lines), ", ".join(map(str, lines)))
            for label, field, lines in repeats))
    objects = {}
    numbers = {}
    for entry in list_node.elts:
        f = literal_fields(entry)
        if "key" not in f:
            continue
        key = f["key"]
        if not isinstance(key, str) or not KEY_PATTERN.match(key):
            raise ExportError("%s: key %r is not lower-case letters, digits "
                              "and underscores" % (f.get("name"), key))
        if key in objects:
            raise ExportError("key '%s' is on two entries (%s and %s)"
                              % (key, objects[key]["name"], f.get("name")))
        horizons_name = f.get("horizons_name")
        if not isinstance(horizons_name, str) or not horizons_name.strip():
            raise ExportError("%s: key '%s' has no horizons_name (JPL's "
                              "exact name, which the gallery's Horizons "
                              "check compares)" % (f.get("name"), key))
        description = description_of(f.get("mission_info"))
        if "Horizons:" in description:
            raise ExportError("%s: its description still says 'Horizons:' "
                              "after the opening is removed" % key)
        served_id, served_type = served_identity(f)
        objects[key] = {
            "name": f.get("name"),
            "horizons_id": served_id,
            "horizons_name": horizons_name,
            "id_type": served_type,
            "object_type": f.get("object_type"),
            "description": description or None,
            "info_url": f.get("mission_url"),
        }
        found = NUMBER.findall(description)
        if found:
            numbers[key] = found
    return objects, numbers


# ------------------------------------------------------------- periods

def _canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _printed(value, err):
    """{value, figures, text} for value printed by the orrery's rule."""
    import orbital_period as op
    text = op.format_by_error(value, err)
    return {"value": float(text.replace(",", "")),
            "figures": op.figures_by_error(value, err),
            "text": text}


def _typed_printed(days):
    """{years, days}, each {value, figures, text}, for a typed value: the
    days as typed, the years to the same figure count (the orrery's
    _typed_strings)."""
    import orbital_period as op
    years_s, days_s = op._typed_strings(days)
    return ({"value": float(years_s), "figures": _text_figures(years_s),
             "text": years_s},
            {"value": float(days_s), "figures": _text_figures(days_s),
             "text": days_s})


def _text_figures(text):
    """The significant figures a printed number shows: its digits less any
    leading zeros. For a typed print, which carries no separators and
    whose trailing zeros '%g' has already dropped ('0.886', not
    '0.8860'), so the count is what the orrery's hover shows."""
    return len(re.sub(r"[^0-9]", "", text).lstrip("0")) or 1


def _strip_osc(epoch):
    return str(epoch or "").replace(" osc.", "").strip()


def period_block(name, object_type, cache, typed_table):
    """(period, inputs) for one keyed entry: the export's period block
    and the slice of the inputs it was read from, for the fingerprint.
    Raises ExportError on a record that cannot be exported honestly."""
    import orbital_period as op
    if object_type == "fixed":
        return None, None
    entry = cache.get(name) if isinstance(cache, dict) else None
    entry = entry if isinstance(entry, dict) else {}
    rec = entry.get("period") if isinstance(entry.get("period"), dict) else None
    if rec is not None:
        if not rec.get("center"):
            raise ExportError("%s: its period record names no centre"
                              % name)
        if "days" not in rec:
            raise ExportError("%s: its period record holds no days" % name)
        # L-445: the id the period was asked of. A record saved before
        # L-445 has no 'target'; its period was asked of the id its
        # elements fetch asked, which the metadata keeps.
        target = op.record_target(rec, (entry.get("metadata") or {}).get(
            "horizons_id"))
        if not target:
            raise ExportError("%s: its period record names no target"
                              % name)
        inputs = {"period": rec, "elements": entry.get("elements"),
                  "center_body": (entry.get("metadata") or {}).get(
                      "center_body"),
                  "horizons_id": (entry.get("metadata") or {}).get(
                      "horizons_id")}
        days = rec.get("days")
        err = rec.get("error_days")
        block = {
            "kind": "fetched", "typed": False,
            "center": rec["center"],
            "center_label": op.centre_label(rec["center"]),
            "target": target,
            "target_label": rec.get("target_label"),
            "open_orbit": days is None,
            "fetched": rec.get("fetched"),
            "words": None,
        }
        if days is None:
            block["years"] = block["days"] = None
        else:
            block["years"] = _printed(days / op.D_PER_JULIAN_YEAR,
                                      err / op.D_PER_JULIAN_YEAR
                                      if err else None)
            block["days"] = _printed(days, err)
        record = {
            "days": days,
            "error_days": err,
            "error_from": rec.get("error_from"),
            "sbdb_status": rec.get("sbdb_status"),
            "epoch": rec.get("epoch"),
            "elements": rec.get("elements"),
        }
        if not op._is_heliocentric(rec["center"]):
            sun = entry.get("elements")
            sun_centre = (entry.get("metadata") or {}).get("center_body",
                                                            "@sun")
            el = rec.get("elements")
            if rec.get("target_label"):
                record["paired"] = False
                record["not_paired"] = ("the period is %s's; its elements "
                                        "are not this body's"
                                        % rec["target_label"])
            elif not isinstance(el, dict):
                record["paired"] = False
                record["not_paired"] = ("the period record holds no "
                                        "elements around its centre")
            elif not (isinstance(sun, dict)
                      and op._is_heliocentric(sun_centre)):
                record["paired"] = False
                record["not_paired"] = ("the cache holds no Sun-centred "
                                        "elements for this body")
            elif _strip_osc(sun.get("epoch")) != _strip_osc(el.get("epoch")):
                record["paired"] = False
                record["not_paired"] = (
                    "the Sun-centred elements are from %s and the "
                    "period's from %s" % (_strip_osc(sun.get("epoch")),
                                          _strip_osc(el.get("epoch"))))
            else:
                record["paired"] = True
                record["sun_elements"] = sun
        block["record"] = record
        return block, inputs
    typed = typed_table.get(name, "missing") if typed_table else "missing"
    if typed != "missing":
        inputs = {"typed": typed}
        block = {"kind": "typed", "typed": True, "center": None,
                 "center_label": None, "open_orbit": typed is None,
                 "fetched": None,
                 "words": "Typed value, not fetched from JPL."}
        if typed is None:
            block["years"] = block["days"] = None
        else:
            block["years"], block["days"] = _typed_printed(float(typed))
        return block, inputs
    return ({"kind": "none", "typed": False, "center": None,
             "center_label": None, "open_orbit": False, "fetched": None,
             "years": None, "days": None,
             "words": "Not yet fetched from JPL."}, {"none": True})


def confirmation_of(record):
    """The export's copy of one entry's confirmation record: what JPL
    confirmed and when, without the queries (the record keeps those)."""
    record = record if isinstance(record, dict) else {}
    identity = None
    if record.get("confirmed"):
        identity = {"confirmed": record.get("confirmed"),
                    "horizons_id": record.get("horizons_id"),
                    "id_type": record.get("id_type"),
                    "horizons_name": record.get("horizons_name")}
    period = record.get("period")
    if isinstance(period, dict) and period.get("confirmed"):
        period = {k: period.get(k) for k in
                  ("confirmed", "center", "epoch", "days", "jpl_days",
                   "error_days")}
    else:
        period = None
    return {"identity": identity, "period": period}


def load_inputs(root):
    """(cache, typed_table, confirmations, confirmations_raw). Raises
    ExportError when a file cannot be read."""
    path = os.path.join(root, CACHE)
    try:
        with open(path, "r", encoding="utf-8") as handle:
            cache = json.load(handle)
    except (OSError, ValueError) as exc:
        raise ExportError("%s could not be read: %s"
                          % (CACHE.replace(os.sep, "/"), exc))
    try:
        from constants_new import KNOWN_ORBITAL_PERIODS as typed
    except Exception as exc:
        raise ExportError("constants_new.KNOWN_ORBITAL_PERIODS could not be "
                          "read: %s" % exc)
    path = os.path.join(root, CONFIRMATIONS)
    raw = b""
    confirmations = {"objects": {}}
    if os.path.exists(path):
        try:
            with open(path, "rb") as handle:
                raw = handle.read()
            confirmations = json.loads(raw.decode("utf-8"))
        except (OSError, ValueError) as exc:
            raise ExportError("%s could not be read: %s"
                              % (CONFIRMATIONS.replace(os.sep, "/"), exc))
    return cache, dict(typed), confirmations, raw


def load_paths(root):
    """(plans, raw) from data/path_plans.json, which path_plan.py writes
    just before this runs; ({}, b"") when it does not exist yet. Raises
    ExportError when it cannot be read."""
    path = os.path.join(root, PATHS)
    if not os.path.exists(path):
        return {}, b""
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
        return (json.loads(raw.decode("utf-8")).get("plans") or {}), raw
    except (OSError, ValueError) as exc:
        raise ExportError("%s could not be read: %s"
                          % (PATHS.replace(os.sep, "/"), exc))


# What of a plan the website reads; the rest is path_plan.py's own
# bookkeeping (what it was made from, what it carried, where it looked).
PATH_FIELDS = ("made", "span", "backbone", "events", "searched")


def is_path(obj):
    """A spacecraft: a trajectory whose Horizons id starts with '-'."""
    return (obj.get("object_type") == "trajectory"
            and str(obj.get("horizons_id") or "").startswith("-"))


def path_of(plan):
    if not plan:
        return None
    return dict((f, plan.get(f)) for f in PATH_FIELDS)


def build_export(text, cache=None, typed_table=None, confirmations=None,
                 confirmations_raw=b"", paths=None, paths_raw=b""):
    """The export dict for the list's source text, the period inputs and
    the path plans. Raises ExportError."""
    objects, numbers = build_objects(text)
    paths = paths or {}
    cache = cache or {}
    typed_table = typed_table or {}
    records = (confirmations or {}).get("objects") or {}
    period_inputs = {}
    for key, obj in objects.items():
        if is_path(obj):
            # L-443 build B: a spacecraft has no orbital period to serve.
            # plotting never asks elements for a mission (is_mission), so
            # the period block would read "Not yet fetched from JPL", which
            # is not true of a spacecraft; it serves none, as the Sun does,
            # and the website prints no period line for it.
            period, inputs = None, None
        else:
            period, inputs = period_block(obj["name"], obj["object_type"],
                                          cache, typed_table)
        obj["period"] = period
        obj["confirmation"] = confirmation_of(records.get(key))
        period_inputs[key] = inputs
        if is_path(obj):
            obj["path"] = path_of(paths.get(key))
    return {
        "schema": SCHEMA,
        "source_sha256": source_sha256(text.encode("utf-8")),
        "period_inputs_sha256": hashlib.sha256(
            _canonical(period_inputs).encode("ascii")).hexdigest(),
        "confirmations_sha256": source_sha256(confirmations_raw),
        "paths_sha256": source_sha256(paths_raw),
        "cadence_days": CADENCE_DAYS,
        "objects": objects,
        "numbers": numbers,
    }


def period_summary(key, period):
    """One line naming an exported period, for the run's output."""
    if period is None:
        return "%s: no period (the centre, or a spacecraft)" % key
    if period["kind"] == "none":
        return "%s: none (not yet fetched)" % key
    if period["open_orbit"]:
        shown = "open orbit"
    else:
        shown = "%s years (%s days), %d and %d figures" % (
            period["years"]["text"], period["days"]["text"],
            period["years"]["figures"], period["days"]["figures"])
    if period["kind"] == "typed":
        return "%s: %s, TYPED" % (key, shown)
    extra = ""
    record = period.get("record") or {}
    if "paired" in record:
        extra = (", paired with the Sun-centred elements" if record["paired"]
                 else ", NOT paired: %s" % record.get("not_paired"))
    whose = ("for %s, " % period["target_label"]
             if period.get("target_label") else "")
    return "%s: %s, %saround %s, fetched %s%s" % (
        key, shown, whose, period["center_label"], period["fetched"], extra)


def render(export):
    return json.dumps(export, indent=2, ensure_ascii=True,
                      sort_keys=False) + "\n"


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root, SOURCE), "rb") as handle:
        raw = handle.read()
    try:
        cache, typed, confirmations, conf_raw = load_inputs(root)
        paths, paths_raw = load_paths(root)
        export = build_export(raw.decode("utf-8").replace("\r\n", "\n"),
                              cache, typed, confirmations, conf_raw,
                              paths, paths_raw)
    except ExportError as exc:
        print("FAIL: %s. NOTHING was written." % exc)
        return 1
    target = os.path.join(root, TARGET)
    content = render(export)
    old = None
    if os.path.exists(target):
        with open(target, "r", encoding="utf-8", newline="") as handle:
            old = handle.read()
    keys = list(export["objects"])
    if old == content:
        print("Objects export unchanged: %d keyed entries (%s)."
              % (len(keys), ", ".join(keys)))
    else:
        with open(target, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
        print("Objects export written to %s: %d keyed entries (%s)."
              % (TARGET.replace(os.sep, "/"), len(keys), ", ".join(keys)))
    if export["numbers"]:
        print("Numbers in exported descriptions, each to be sourced or "
              "removed: %s." % "; ".join(
                  "%s: %s" % (k, ", ".join(v))
                  for k, v in export["numbers"].items()))
    else:
        print("Numbers in exported descriptions: none.")
    served_paths = [(k, o) for k, o in export["objects"].items()
                    if "path" in o]
    if served_paths:
        print("Paths exported (L-443): %s." % "; ".join(
            "%s %s" % (k, ("%d events, made %s" % (len(o["path"]["events"]),
                                                   o["path"]["made"]))
                       if o["path"] else "NO PLAN YET (run path_plan.py)")
            for k, o in served_paths))
    print("Periods exported (L-431):")
    for key, obj in export["objects"].items():
        print("  " + period_summary(key, obj["period"]))
    typed = [k for k, o in export["objects"].items()
             if (o["period"] or {}).get("kind") in ("typed", "none")]
    if typed:
        print("Not fetched from JPL yet, so the website marks them: %s. "
              "Plot each in the orrery and answer yes to Update Orbital "
              "Elements, then run this again." % ", ".join(typed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
