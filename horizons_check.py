"""
horizons_check.py -- check each object the website serves against JPL
Horizons: that its entry names exactly one object, that the object's id,
index and name are what the orrery's list says, and that the orbital
period the website prints is the one JPL gives. And re-read each
spacecraft's Horizons data sheet on the same cycle (L-395, L-431).

WHERE IT RUNS AND WHY HERE

    In the orrery's maintenance run, as a generator just before the
    objects export, so the export carries the dates this run writes.
    Tony, 2026-10-12: "shouldn't the horizons check live in the orrery
    repo? the orrery stores and serves the data not the other way
    around," and "can we make the Horizons check part of the exporter
    routine?" Until then it was the second step of the website's Daily
    Run (gallery tools/horizons_check.py, built 2026-10-10, moved here
    by L-431's build 3, 2026-10-14; git keeps its history there).

    It reads the list through export_objects.py's own reader, never the
    export file, so it checks the entries as they are on this run. The
    design, with every ruling, is
    documentation/DESIGN_L395_horizons_check_20261007.md; the move is
    documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md;
    the period comparison is ruling 6 of
    documentation/DESIGN_L431_orbital_periods_rulings_20261011.md.

WHAT IS ASKED, AND WHEN

    Only what is due, so on most runs it asks JPL nothing. Each part of
    an entry is due when it has never been confirmed, when its last
    confirmation is 30 days old or more, or at once when it has changed
    since. An identity or a period is also asked again from day 25: the
    website's own check goes red at day 30 and sees the new date only
    after the push and its pull, so it gets five days' margin. The
    offline checker still passes such a confirmation until day 30.

    IDENTITY (the entries with a 'key', the thirteen the website
    serves): its id, id_type and horizons_name, found as the design
    found them --
      an ordinary entry through JPL's Lookup service: the index its
      id_type points at must hold exactly one object whose primary id
      (major bodies) or primary designation (small bodies) is the id,
      and the other index none; a comet asked by JPL's permanent number
      for it (id_type 'designation', a number) is in the small-body
      index under that primary SPKID;
      a pinned comet record (an id of eight digits starting 9) through
      Horizons' main service: the record must exist under the entry's
      horizons_name and be the newest for its comet, or the pin is
      reported stale for Tony, never re-pinned.
    Compared: id, id_type, horizons_name character for character, and
    object_type only where it means something ("barycenter", and the
    Sun's "fixed").

    PERIOD (L-431, build 3): for a keyed entry whose period was fetched
    from JPL, one elements query at the period's own date and around its
    own centre -- the question the orrery asked when it fetched it --
    and JPL's PR must lie within the period's own error of the period
    the website prints. It is asked of the period's own target, as the
    export names it (L-445): Earth's period is the Earth-Moon
    barycentre's, so the check asks Horizons target 3, not Earth's 399,
    and a change of target makes the period due at once. A typed period, or none, is not compared: the
    website marks it as not from JPL, and this names it.

    DATA SHEETS (L-401, ruled 2026-10-12): every spacecraft in the list
    (an id starting with '-'), its sheet re-read every 30 days. The
    record, data/spacecraft_sheets.json, was seeded from the survey of
    2026-10-12 (documentation/SURVEY_L401_spacecraft_data_sheets_
    20261012.md). Red only where a row of constants_new.py quotes a
    figure from the sheet and the sheet no longer gives that figure
    (Tony's option A, 2026-10-12: "the row claims the figure, not the
    page"). It stays red until a patch changes the row; where the sheet
    has stopped stating a figure at all, a patch that re-reads the sheet
    and moves the row's Read date also clears it. A sheet whose
    "Revised:" date moved but whose figure did not is noted in the
    record, not red. Nothing here edits a row.

    One query at a time, with a pause between. Any error -- no network,
    an HTTP error, an answer that is not JPL's -- is "could not reach
    JPL": it never passes, nothing is recorded for that part, it stays
    due, and the run asks JPL nothing more. The verdict line then says
    UNREACHABLE, by name: the convention for a row that needs the
    network (the gallery's three states, PASS, FAIL and UNREACHABLE).

WHAT IT WRITES

    data/horizons_confirmations.json: for each keyed entry, the date its
    identity was confirmed and what was confirmed, with JPL's name and
    type and the queries asked; under "period" the date its period was
    confirmed, the period, its centre, its target (L-445) and date,
    JPL's PR and the query.
    The thirteen identity confirmations of 2026-10-10 were carried over
    from the website's record by the move, with their dates and queries,
    so the move asked JPL nothing.
    data/spacecraft_sheets.json: each sheet's last read, its "Revised:"
    date and what it states, and a note for each change seen.
    data/horizons_check_last_run.json: this run's date and verdict, each
    problem named. Git ignores it: it changes on every run and is read
    only by the checker that runs next, on the same machine.
    Nothing else. check_horizons_confirmations.py reads all three offline,
    as a checker of the same maintenance run, and goes red on what this
    found; export_objects.py copies the dates into the export, and the
    website's own offline check reads them from there.

WHAT IT PRINTS

    How many entries and sheets were examined, due and queried; one line
    per entry and per sheet asked; each disagreement with the list's
    value, JPL's and the query to paste into a browser; then one verdict
    line: HORIZONS CHECK: PASS, NOTHING DUE, FAIL naming each entry and
    field, or UNREACHABLE naming what was left unasked.

RUN COMMAND

    python horizons_check.py           check what is due
    python horizons_check.py --all     check every entry and sheet

    Open it in VS Code and click Run. The maintenance run runs it with no
    flags. It needs the internet only on a day something is due. Its
    offline tests are test_horizons_check.py, on JPL's recorded answers
    in documentation/worksheets/horizons_answers_L395.json.

Role: devtool
Domain: dev_tools

Module created: October 10, 2026 with Anthropic's Claude Opus 5.5
(L-395, the Horizons check, in the gallery repo).
Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5 (L-431,
build 3, with L-395's move: moved into the orrery's maintenance run
beside the objects export; it compares each fetched period with JPL's PR
and re-reads the spacecraft data sheets on the same 30-day cycle.)
Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5 (L-445,
Earth's period: the period is asked of the target its record names, and
the confirmation records that target.)
Module updated: October 25, 2026 with Anthropic's Claude Opus 5.5 (L-443,
the twelve spacecraft: JPL's answer of its header alone, which is how
the Lookup answers a spacecraft's id in the small-body index, is read as
no matches instead of as JPL unreachable.)
Module updated: October 26, 2026 with Anthropic's Claude Opus 5.5 (L-443,
the comets: an entry asked by JPL's permanent number for a comet, id_type
'designation', is looked for in the small-body index by its primary
SPKID; C/2025 K1, asked as 1004075 since L-470, is the first. A path,
a spacecraft or a comet on an open path, has no period here, as in the
export.)
"""

import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import export_objects

CONFIRMATIONS = os.path.join("data", "horizons_confirmations.json")
SHEETS = os.path.join("data", "spacecraft_sheets.json")
LAST_RUN = os.path.join("data", "horizons_check_last_run.json")
CONSTANTS_EXPORT = os.path.join("data", "constants_export.json")

LOOKUP = "https://ssd.jpl.nasa.gov/api/horizons_lookup.api"
MAIN = "https://ssd.jpl.nasa.gov/api/horizons.api"
CADENCE_DAYS = export_objects.CADENCE_DAYS
# An identity or a period is asked again from day 25, five days before
# the website's own check goes red at day 30 (gallery
# tools/check_horizons_confirmations.py). The website reads the dates
# from the export, which reaches it only after this repo's push and the
# gallery's pull; asking at day 30 exactly would leave it no time, and it
# would go red every cycle however often this run is made. A cold review
# of L-431 build 3 found it. The data sheets, which the website does not
# judge, keep their 30 days.
RENEW_DAYS = CADENCE_DAYS - 5
# What the offline checker passes: a confirmation inside the 30 days,
# including one this run will renew.
PASSING = ("current", "renewing")
PAUSE_SECONDS = 2.0
TIMEOUT_SECONDS = 30
IDENTITY = ("horizons_id", "id_type", "horizons_name")
PINNED = re.compile(r"^9\d{7}$")
INDEX_WORD = {"mb": "major-body index", "sb": "small-body index"}
LINE = "=" * 70
OPEN_ORBIT_FLOOR = 1e90


class Unreachable(Exception):
    """JPL could not be reached, or its answer could not be read."""


# ------------------------------------------------------------- queries

def lookup_url(ident, group):
    return "%s?sstr=%s&group=%s&format=text" % (
        LOOKUP, urllib.parse.quote(str(ident), safe=""), group)


def record_url(record):
    return ("%s?format=text&COMMAND='%s'&OBJ_DATA=YES&MAKE_EPHEM=NO"
            % (MAIN, record))


def record_list_url(designation):
    return ("%s?format=text&COMMAND='DES=%s%%3B'&OBJ_DATA=YES&MAKE_EPHEM=NO"
            % (MAIN, urllib.parse.quote(designation, safe="/")))


def live_fetch(url):
    """JPL's answer as text. Raises Unreachable on any failure."""
    request = urllib.request.Request(
        url.replace("'", "%27"),
        headers={"User-Agent": "palomas-orrery-gallery-horizons-check"})
    try:
        with urllib.request.urlopen(request,
                                    timeout=TIMEOUT_SECONDS) as response:
            code = response.getcode()
            body = response.read()
    except urllib.error.HTTPError as exc:
        raise Unreachable("HTTP %s" % exc.code)
    except Exception as exc:                  # network, DNS, TLS, proxy
        raise Unreachable(str(exc) or exc.__class__.__name__)
    if code != 200:
        raise Unreachable("HTTP %s" % code)
    return body.decode("utf-8", "replace")


# ------------------------------------------------------------- parsing

def _jpl(text):
    if "API VERSION" not in text:
        raise Unreachable("the answer is not one of JPL's (no API VERSION "
                          "line)")


def parse_lookup(text):
    """[{name, type, spkid, designation}] from a Lookup answer.

    "NOTICE: no matches found" gives []. Raises Unreachable when the
    answer is not a Lookup answer at all."""
    _jpl(text)
    found = []
    current = None
    for raw in text.splitlines():
        if "=" not in raw:
            continue
        key, _, value = raw.partition("=")
        key, value = key.strip(), value.strip()
        if key == "Object name":
            current = {"name": value, "type": "", "spkid": "",
                       "designation": ""}
            found.append(current)
        elif current is not None and key == "Type":
            current["type"] = value
        elif current is not None and key == "Primary SPKID":
            current["spkid"] = value
        elif current is not None and key == "Primary designation":
            current["designation"] = value
    if not found and "no matches found" not in text and not bare(text):
        raise Unreachable("the Lookup answer names no object and does not "
                          "say 'no matches found'")
    return found


def bare(text):
    """True when JPL's answer is its two header lines and nothing else.

    L-443, 2026-10-25: JPL's Lookup answers a spacecraft's id (negative,
    -31 for Voyager 1) in the small-body index with its header alone --
    "API VERSION: 1.1" and "API SOURCE: NASA/JPL Horizons Lookup API",
    no object and no "no matches found" notice (fetched that day, -31 and
    -61 in group=sb). That is an empty index, not a failed fetch; until
    then the first spacecraft stopped the whole run as UNREACHABLE. Any
    other line still means the answer was not read, and still fails."""
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return bool(lines) and all(ln.startswith(("API VERSION:", "API SOURCE:"))
                               for ln in lines)


def keep(matches, ident, group):
    """Step 2: the matches whose primary id or designation is the id."""
    field = "spkid" if group == "mb" else "designation"
    return [m for m in matches if m[field] == str(ident)]


HEADER = re.compile(r"^JPL/HORIZONS\s+(.+?)\s{2,}\d{4}-[A-Za-z]{3}-\d{2}")
REC = re.compile(r"Rec #:\s*(\d+)")
SOLN = re.compile(r"Soln\.date:\s*(\S+)")
LIST_ROW = re.compile(r"^\s*(9\d{7})\s+(-?\d+)\s")


def parse_record(text):
    """{name, record, solution_date} for one record, or None when the
    answer holds no record. Raises Unreachable when it is not JPL's."""
    _jpl(text)
    name = record = None
    for raw in text.splitlines():
        m = HEADER.match(raw.strip())
        if m and name is None:
            name = m.group(1).strip()
        r = REC.search(raw)
        if r and record is None:
            record = r.group(1)
            s = SOLN.search(raw)
            solution = s.group(1) if s else ""
    if name is None or record is None:
        return None
    return {"name": name, "record": record, "solution_date": solution}


def parse_record_list(text):
    """[(record, epoch_year)] from a DES=...; answer."""
    _jpl(text)
    rows = []
    for raw in text.splitlines():
        m = LIST_ROW.match(raw)
        if m:
            rows.append((m.group(1), m.group(2)))
    if not rows:
        raise Unreachable("the record list names no record")
    return rows


def designation_of(horizons_name):
    """The designation inside a comet's JPL name: "2P/Encke" -> "2P",
    "MAPS (C/2026 A1)" -> "C/2026 A1". None when there is none."""
    m = re.match(r"^(\d+[PDI])/", horizons_name or "")
    if m:
        return m.group(1)
    m = re.search(r"\(([^()]+)\)\s*$", horizons_name or "")
    if m:
        return m.group(1).strip()
    return None


# ------------------------------------------------------------- one entry

def check_entry(key, obj, fetch, pause=0.0):
    """The verdict for one exported entry.

    Returns {key, status, disagreements, jpl, pin, queries, error}.
    status is "agrees", "DISAGREES" or "could not reach JPL" (and, in
    run(), "not asked" for an entry left after JPL failed); each
    disagreement is (field, the list's value, JPL's value, query)."""
    out = {"key": key, "status": "agrees", "disagreements": [], "jpl": {},
           "pin": None, "queries": [], "error": None}
    ident = obj.get("horizons_id")
    id_type = obj.get("id_type")
    hname = obj.get("horizons_name")
    otype = obj.get("object_type")

    def ask(url):
        if out["queries"] and pause:
            time.sleep(pause)
        out["queries"].append(url)
        return fetch(url)

    def disagree(field, ours, theirs, url):
        out["disagreements"].append((field, ours, theirs, url))

    try:
        if not hname:
            disagree("horizons_name", "(none in the export)",
                     "(nothing to compare)", "")
        elif id_type == "smallbody" and PINNED.match(str(ident or "")):
            url = record_url(ident)
            rec = parse_record(ask(url))
            if rec is None or rec["record"] != str(ident):
                disagree("horizons_id", ident,
                         "no record %s in Horizons" % ident, url)
            else:
                out["jpl"] = {"name": rec["name"], "type": "comet record",
                              "record": rec["record"]}
                designation = designation_of(rec["name"])
                if rec["name"] != hname:
                    # Not our comet's record, so its newest record is
                    # not the question; the name says what is wrong.
                    disagree("horizons_name", hname, rec["name"], url)
                elif designation is None:
                    disagree("pin", "record %s" % ident,
                             "no designation in JPL's name %r, so the "
                             "newest record cannot be found" % rec["name"],
                             url)
                else:
                    lurl = record_list_url(designation)
                    rows = parse_record_list(ask(lurl))
                    newest, year = max(rows, key=lambda r: int(r[0]))
                    out["pin"] = {"record": rec["record"],
                                  "solution_date": rec["solution_date"],
                                  "records": len(rows), "newest": newest,
                                  "newest_epoch_year": year}
                    if newest != str(ident):
                        disagree("pin", "record %s" % ident,
                                 "pin is stale: record %s (epoch-year %s) "
                                 "is newer, of %d for %s"
                                 % (newest, year, len(rows), designation),
                                 lurl)
        else:
            # L-443, slice 2's comets: an entry asked by JPL's permanent
            # number for a comet (id_type 'designation', sent as DES=<n>;,
            # L-470: C/2025 K1, 1004075) is a small body, found in the
            # small-body index by its primary SPKID, as the Lookup answers
            # it (read 2026-10-26: sstr=1004075, group=sb, gives ATLAS
            # (C/2025 K1), Primary SPKID 1004075).
            group = ("sb" if id_type in ("smallbody", "designation")
                     else "mb")
            other = "mb" if group == "sb" else "sb"
            url = lookup_url(ident, group)
            by_spkid = id_type == "designation" and str(ident).isdigit()
            here = keep(parse_lookup(ask(url)), ident,
                        "mb" if by_spkid else group)
            ourl = lookup_url(ident, other)
            there = keep(parse_lookup(ask(ourl)), ident, other)
            if len(here) > 1:
                disagree("horizons_id", ident,
                         "%d objects in the %s: %s" % (
                             len(here), INDEX_WORD[group],
                             "; ".join(m["name"] for m in here)), url)
            elif not here and there:
                disagree("id_type", id_type or "(blank: major body)",
                         "found only in the %s, as %s"
                         % (INDEX_WORD[other], there[0]["name"]), ourl)
            elif not here:
                disagree("horizons_id", ident,
                         "no object in either index whose primary %s is %s"
                         % ("id" if group == "mb" else "designation",
                            ident), url)
            else:
                m = here[0]
                out["jpl"] = {"name": m["name"], "type": m["type"],
                              "spkid": m["spkid"],
                              "designation": m["designation"]}
                if there:
                    disagree("id_type", id_type or "(blank: major body)",
                             "found in both indexes (%s also as %s)"
                             % (INDEX_WORD[other], there[0]["name"]), ourl)
                if m["name"] != hname:
                    disagree("horizons_name", hname, m["name"], url)
                want = {"barycenter": "barycenter", "fixed": "Sun"}.get(otype)
                if want is not None and m["type"] != want:
                    disagree("object_type", otype,
                             "%s (expected %s)" % (m["type"], want), url)
    except Unreachable as exc:
        out["status"] = "could not reach JPL"
        out["error"] = str(exc)
        return out
    if out["disagreements"]:
        out["status"] = "DISAGREES"
    return out


# ------------------------------------------------------------- the period

def calendar_jd(text):
    """The Julian date of "YYYY-MM-DD HH:MM" read as a calendar date, the
    number astropy's Time(text).jd gives and the orrery's period query
    passed as TLIST (orbital_period.query_period_pair), so this asks JPL
    the same question. Raises ValueError on another form."""
    m = re.match(r"^\s*(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{1,2}):(\d{2})"
                 r"(?::(\d{2}(?:\.\d*)?))?)?\s*$", str(text or ""))
    if not m:
        raise ValueError("not a date and time: %r" % text)
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    hh = int(m.group(4) or 0)
    mi = int(m.group(5) or 0)
    ss = float(m.group(6) or 0.0)
    a = (14 - mo) // 12
    yy = y + 4800 - a
    mm = mo + 12 * a - 3
    jdn = (d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100
           + yy // 400 - 32045)
    return jdn + (hh - 12) / 24.0 + mi / 1440.0 + ss / 86400.0


def command_of(horizons_id, id_type):
    """Horizons' COMMAND for an entry, as astroquery 0.4.11 builds it for
    the orrery's period query: a small body's id with a ';' after it (and
    no DES=, which astroquery adds only for 'designation' and 'name'),
    anything else as it is."""
    ident = str(horizons_id)
    if id_type in ("smallbody", "asteroid_name", "comet_name"):
        return ident + ";"
    if id_type == "designation":
        return "DES=" + ident + ";"
    return ident


def period_url(horizons_id, id_type, center, jd):
    """One elements row at jd around center, in AU and days. The ';' a
    small body's COMMAND ends with is sent as %3B, as JPL's own examples
    and record_list_url send it; a bare ';' can end the parameter early.
    (A cold review of L-431 build 3 found it.)"""
    return ("%s?format=text&COMMAND='%s'&OBJ_DATA=NO&MAKE_EPHEM=YES"
            "&EPHEM_TYPE=ELEMENTS&CENTER='%s'&TLIST='%.9f'"
            "&OUT_UNITS='AU-D'&REF_PLANE='ECLIPTIC'&REF_SYSTEM='ICRF'"
            "&TP_TYPE='ABSOLUTE'&CSV_FORMAT='NO'"
            % (MAIN, urllib.parse.quote(command_of(horizons_id, id_type),
                                        safe="="),
               center, jd))


PR = re.compile(r"\bPR\s*=\s*([-+0-9.EeDd]+)")


def parse_period(text):
    """JPL's PR, in days, from an elements answer (OUT_UNITS AU-D), or
    None for an open orbit (PR printed as 9.999E+99). Raises Unreachable
    when the answer is not JPL's, and ValueError when it is JPL's but
    holds no elements row (JPL refused the question)."""
    _jpl(text)
    if "$$SOE" not in text or "$$EOE" not in text:
        raise ValueError("JPL's answer holds no elements row: %s"
                         % " ".join(text.strip().splitlines()[-2:])[:160])
    block = text[text.index("$$SOE"):text.index("$$EOE")]
    m = PR.search(block)
    if not m:
        raise ValueError("JPL's elements row has no PR")
    value = float(m.group(1).replace("D", "E").replace("d", "e"))
    if value >= OPEN_ORBIT_FLOOR:
        return None
    return value


def check_period(key, obj, period, fetch):
    """The verdict for one entry's fetched period.

    Returns {key, status, disagreement, jpl_days, query, error}; status
    is "agrees", "DISAGREES" or "could not reach JPL"."""
    record = period.get("record") or {}
    out = {"key": key, "status": "agrees", "disagreement": None,
           "jpl_days": None, "query": None, "error": None}
    try:
        jd = calendar_jd(record.get("epoch"))
    except ValueError as exc:
        out["status"] = "DISAGREES"
        out["disagreement"] = ("period", record.get("epoch"),
                               "the period's date cannot be read (%s)"
                               % exc, "")
        return out
    # L-445: the period is asked of its record's target (Earth's is the
    # Earth-Moon barycentre, "3"), with no id_type when that is another
    # body; the body's own id only for a block that names none.
    target = period.get("target") or obj.get("horizons_id")
    own = str(target) == str(obj.get("horizons_id"))
    url = period_url(target, obj.get("id_type") if own else None,
                     period.get("center"), jd)
    out["target"] = str(target)
    out["query"] = url
    try:
        answer = fetch(url)
        try:
            jpl = parse_period(answer)
        except ValueError as exc:
            out["status"] = "DISAGREES"
            out["disagreement"] = ("period", _days_text(record),
                                   str(exc), url)
            return out
    except Unreachable as exc:
        out["status"] = "could not reach JPL"
        out["error"] = str(exc)
        return out
    out["jpl_days"] = jpl
    days = record.get("days")
    err = record.get("error_days")
    if days is None or jpl is None:
        if days is None and jpl is None:
            return out
        out["status"] = "DISAGREES"
        out["disagreement"] = ("period", _days_text(record),
                               "open orbit" if jpl is None
                               else "%.10g days" % jpl, url)
        return out
    allowed = err if (err is not None and err > 0) else 1e-9 * abs(days)
    if abs(jpl - days) > allowed:
        out["status"] = "DISAGREES"
        out["disagreement"] = (
            "period", "%s (+/- %.6g days)" % (_days_text(record), allowed),
            "%.10g days at %s around %s, %.6g days away"
            % (jpl, record.get("epoch"), period.get("center"),
               abs(jpl - days)), url)
    return out


def _days_text(record):
    days = record.get("days")
    return "open orbit" if days is None else "%.10g days" % days


# ------------------------------------------------------------- the sheets

REVISED = re.compile(r"Revised:\s*([A-Z][a-z]{2,8}\.?\s+\d{1,2},?\s+\d{4})")
POINTING = re.compile(r"RA\s*\+/-\s*([0-9.]+)\s*arcsec\w*\s*,?\s*"
                      r"DEC\s*\+/-\s*([0-9.]+)\s*arcsec", re.S)
UNCERTAIN = re.compile(r"[^.\n]*uncertaint[^.\n]*\+/-[^.\n]*", re.I)


def sheet_url(horizons_id):
    return ("%s?format=text&COMMAND='%s'&OBJ_DATA=YES&MAKE_EPHEM=NO"
            % (MAIN, horizons_id))


def parse_sheet(text):
    """{revised, stated} from a spacecraft's data sheet. stated is
    {"RA_arcsec", "DEC_arcsec"} where the sheet gives the Voyagers'
    predicted pointing uncertainty, the text of any other sentence
    stating an uncertainty with a +/- figure, or None. Raises
    Unreachable when the answer is not JPL's, and ValueError when the
    sheet's "Revised:" date cannot be read -- a blind spot, which must
    announce, never a pass."""
    _jpl(text)
    m = REVISED.search(text)
    if not m:
        raise ValueError("no \"Revised:\" date could be read from the "
                         "sheet")
    revised = " ".join(m.group(1).replace(".", "").split())
    p = POINTING.search(text)
    if p:
        stated = {"RA_arcsec": float(p.group(1)),
                  "DEC_arcsec": float(p.group(2))}
    else:
        u = UNCERTAIN.search(text)
        stated = " ".join(u.group(0).split()) if u else None
    return {"revised": revised, "stated": stated}


def spacecraft_entries(text):
    """[(id, name)] for every entry of the list with a spacecraft id (one
    starting with '-'), one per id, in list order."""
    import ast
    seen = {}
    for entry in export_objects.definitions(text).elts:
        fields = {}
        for k, v in zip(entry.keys, entry.values):
            if isinstance(k, ast.Constant) and k.value in ("name", "id"):
                try:
                    fields[k.value] = ast.literal_eval(v)
                except ValueError:
                    pass
        ident = str(fields.get("id", ""))
        if ident.startswith("-") and ident not in seen:
            seen[ident] = fields.get("name")
    return list(seen.items())


def row_values(root):
    """{row: (value, latest read date or None)} from the constants export,
    which the maintenance run writes before this runs. {} when it cannot
    be read; the sheets' rows are then reported as unread, never passed."""
    path = os.path.join(root, CONSTANTS_EXPORT)
    try:
        rows = load_json(path).get("rows") or {}
    except (OSError, ValueError):
        return {}
    out = {}
    for name, row in rows.items():
        dates = []
        for line in row.get("read") or []:
            dates.extend(re.findall(r"\d{4}-\d{2}-\d{2}", str(line)))
        out[name] = (row.get("value"), max(dates) if dates else None)
    return out


def sheet_problems(record, rows):
    """[text] for one sheet's record against the rows quoting it: red
    where a row's figure is not the sheet's, or the sheet states none
    and the row was not re-read since (option A, 2026-10-12)."""
    out = []
    stated = record.get("stated")
    for field, row in (record.get("rows") or {}).items():
        if row not in rows:
            out.append("%s quotes the sheet, and the constants export does "
                       "not carry it" % row)
            continue
        value, read = rows[row]
        if not isinstance(stated, dict) or field not in stated:
            if not (read and read >= str(record.get("read"))):
                out.append("%s quotes %s from the sheet, which no longer "
                           "states it (sheet read %s)"
                           % (row, value, record.get("read")))
        elif stated[field] != value:
            out.append("%s is %s; the sheet, read %s, gives %s"
                       % (row, value, record.get("read"), stated[field]))
    return out


# ------------------------------------------------------------- due or not

def parse_day(text):
    try:
        return datetime.date.fromisoformat(str(text))
    except ValueError:
        return None


def _age(day_text, today, renew=False):
    """(state, detail) for a confirmation date alone. With renew, a date
    RENEW_DAYS old or more, and still inside CADENCE_DAYS, is "renewing":
    asked again, and still a pass for the offline checker."""
    day = parse_day(day_text)
    if day is None:
        return "never", "its confirmation has no readable date"
    age = (today - day).days
    if age < 0:
        return "overdue", "confirmed on %s, which is after today" % day
    if age >= CADENCE_DAYS:
        return "overdue", "confirmed on %s, %d days ago (every %d days)" % (
            day, age, CADENCE_DAYS)
    if renew and age >= RENEW_DAYS:
        return "renewing", ("confirmed on %s, %d days ago; asked again from "
                            "day %d, before the website's day %d"
                            % (day, age, RENEW_DAYS, CADENCE_DAYS))
    return "current", "confirmed on %s, %d day%s ago" % (
        day, age, "" if age == 1 else "s")


def confirmation_state(obj, record, today):
    """(state, detail) for an entry's IDENTITY and its confirmation:
    "current", "never", "changed" or "overdue"."""
    if not record or not record.get("confirmed"):
        return "never", "never confirmed"
    moved = [f for f in IDENTITY if record.get(f) != obj.get(f)]
    if moved:
        return "changed", "changed since its confirmation of %s: %s" % (
            record.get("confirmed"), ", ".join(
                "%s %r -> %r" % (f, record.get(f), obj.get(f))
                for f in moved))
    return _age(record.get("confirmed"), today, renew=True)


def period_state(period, record, today):
    """(state, detail) for an entry's PERIOD: "current", "never",
    "changed", "overdue", or "not compared" for a typed period or none."""
    if not isinstance(period, dict) or period.get("kind") != "fetched":
        kind = (period or {}).get("kind", "none") if period else "none"
        return "not compared", ("typed, not fetched from JPL"
                                if kind == "typed"
                                else "no period fetched from JPL")
    held = (record or {}).get("period") if record else None
    if not held or not held.get("confirmed"):
        return "never", "period never confirmed"
    rec = period.get("record") or {}
    # L-445: a confirmation written before the target was recorded was
    # asked of the body's own id, which the identity record keeps.
    held = dict(held)
    held.setdefault("target", (record or {}).get("horizons_id"))
    moved = [f for f, now in (("center", period.get("center")),
                              ("epoch", rec.get("epoch")),
                              ("days", rec.get("days")),
                              ("target", period.get("target")))
             if held.get(f) != now]
    if moved:
        return "changed", "period changed since its confirmation of %s: %s" % (
            held.get("confirmed"), ", ".join(moved))
    state, detail = _age(held.get("confirmed"), today, renew=True)
    return state, "period " + detail


def sheet_state(record, today):
    if not record or not record.get("read"):
        return "never", "not yet read"
    state, detail = _age(record.get("read"), today)
    return state, detail.replace("confirmed", "read")


# ------------------------------------------------------------- the files

def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_confirmations(path):
    if not os.path.exists(path):
        return {"schema": 2, "objects": {}}
    data = load_json(path)
    if not isinstance(data.get("objects"), dict):
        raise ValueError("%s has no objects table" % path)
    return data


def load_sheets(path):
    if not os.path.exists(path):
        return {"schema": 1, "sheets": {}}
    data = load_json(path)
    if not isinstance(data.get("sheets"), dict):
        raise ValueError("%s has no sheets table" % path)
    return data


def render_json(data):
    return json.dumps(data, indent=2, ensure_ascii=True) + "\n"


CONFIRMATIONS_COMMENT = (
    "Written by horizons_check.py (L-395, L-431): the last date each keyed "
    "entry of the orrery's object list was confirmed against JPL Horizons, "
    "and what was confirmed -- its identity, and its period where the "
    "period was fetched -- with this record's last run. Only the check "
    "writes it. check_horizons_confirmations.py reads it offline, and "
    "export_objects.py copies its dates into data/objects_export.json. "
    "The identity confirmations of 2026-10-10 were carried over from the "
    "website's own record by L-431's build 3. Do not edit by hand.")

SHEETS_COMMENT = (
    "Written by horizons_check.py (L-395, L-401): each spacecraft's JPL "
    "Horizons data sheet, as last read -- its Revised: date and what it "
    "states about the trajectory's uncertainty -- with the rows of "
    "constants_new.py that quote it and a note for each change seen. "
    "Seeded from documentation/SURVEY_L401_spacecraft_data_sheets_"
    "20261012.md. Only the check writes it. Do not edit by hand.")


# ------------------------------------------------------------- the run

def show(value):
    return "(blank)" if value in (None, "") else str(value)


def current_entries(root):
    """(objects, list sha, spacecraft) as the list and the orbit cache
    stand now, through export_objects' own reader. Raises ExportError."""
    with open(os.path.join(root, export_objects.SOURCE), "rb") as handle:
        text = handle.read().decode("utf-8").replace("\r\n", "\n")
    objects, _numbers = export_objects.build_objects(text)
    cache, typed, _c, _r = export_objects.load_inputs(root)
    for obj in objects.values():
        obj["period"], _inputs = export_objects.period_block(
            obj["name"], obj["object_type"], cache, typed)
        # L-443, slice 2's comets: as the export serves it, a path (a
        # spacecraft, or a comet on an open path) has no period, so none is
        # compared or confirmed. Until this line the export and this check
        # disagreed for C/2025 K1 and its pieces, whose orbit cache holds a
        # period record.
        if export_objects.is_path(obj):
            obj["period"] = None
    sha = export_objects.source_sha256(text.encode("utf-8"))
    return objects, sha, spacecraft_entries(text)


def run(root, fetch, today, pause=PAUSE_SECONDS, check_all=False,
        write=True, echo=print):
    """The whole check. Returns (exit code, summary dict)."""
    try:
        objects, list_sha, spacecraft = current_entries(root)
    except export_objects.ExportError as exc:
        echo("FAIL: the object list could not be read: %s" % exc)
        echo("HORIZONS CHECK: FAIL -- the list could not be read")
        return 1, {}
    conf_path = os.path.join(root, CONFIRMATIONS)
    sheets_path = os.path.join(root, SHEETS)
    confirmations = load_confirmations(conf_path)
    records = confirmations["objects"]
    sheets = load_sheets(sheets_path)
    sheet_records = sheets["sheets"]
    rows = row_values(root)

    echo(LINE)
    echo("  HORIZONS CHECK -- %s" % today.isoformat())
    echo(LINE)
    echo("Read %s (%s...) through export_objects.py, %s and %s."
         % (export_objects.SOURCE, list_sha[:8],
            CONFIRMATIONS.replace(os.sep, "/"), SHEETS.replace(os.sep, "/")))

    tasks = []          # (kind, key, payload, why)
    quiet = []          # (key, text) for what is not due
    not_compared = []
    for key, obj in objects.items():
        state, detail = confirmation_state(obj, records.get(key), today)
        if state == "current" and not check_all:
            quiet.append((key, "identity not due (%s)" % detail))
        else:
            tasks.append(("identity", key, obj, detail))
        pstate, pdetail = period_state(obj.get("period"), records.get(key),
                                       today)
        if pstate == "not compared":
            if obj.get("period") is not None:
                not_compared.append("%s (%s)" % (key, pdetail))
        elif pstate == "current" and not check_all:
            quiet.append((key, "%s, not due" % pdetail))
        else:
            tasks.append(("period", key, obj, pdetail))
    for ident, name in spacecraft:
        state, detail = sheet_state(sheet_records.get(ident), today)
        if state == "current" and not check_all:
            continue
        tasks.append(("sheet", ident, name, detail))
    sheets_quiet = len(spacecraft) - sum(1 for t in tasks if t[0] == "sheet")

    results = []
    queried = 0
    down = None
    first = True
    for kind, key, payload, why in tasks:
        if down is not None:
            results.append((kind, key, {"status": "not asked",
                                        "error": "JPL could not be reached "
                                        "for %s earlier in this run" % down},
                            why))
            continue
        if not first and pause:
            time.sleep(pause)
        first = False
        if kind == "identity":
            result = check_entry(key, payload, fetch, pause)
            queried += len(result["queries"])
        elif kind == "period":
            result = check_period(key, payload, payload["period"], fetch)
            queried += 1 if result["query"] else 0
        else:
            result = {"status": "agrees", "error": None, "query":
                      sheet_url(key), "sheet": None, "notes": []}
            queried += 1
            try:
                result["sheet"] = parse_sheet(fetch(result["query"]))
            except Unreachable as exc:
                result["status"] = "could not reach JPL"
                result["error"] = str(exc)
            except ValueError as exc:
                result["status"] = "DISAGREES"
                result["error"] = str(exc)
        results.append((kind, key, result, why))
        if result["status"] == "could not reach JPL":
            down = "%s's %s" % (key, kind)

    # The sheets' records: update what was read, and judge every sheet.
    sheet_red = []
    sheet_notes = []
    for kind, key, result, _why in results:
        if kind != "sheet" or result["status"] != "agrees":
            continue
        old = sheet_records.get(key) or {}
        new_sheet = result["sheet"]
        record = dict(old)
        record["name"] = dict(spacecraft).get(key, old.get("name"))
        record.setdefault("rows", {})
        notes = list(old.get("notes") or [])
        if old.get("revised") and old.get("revised") != new_sheet["revised"]:
            note = ("%s: Revised moved from %s to %s"
                    % (today.isoformat(), old["revised"],
                       new_sheet["revised"]))
            if old.get("stated") == new_sheet["stated"]:
                note += "; what it states is unchanged"
            notes.append(note)
            sheet_notes.append("%s (%s)" % (key, note))
        if "stated" in old and old.get("stated") != new_sheet["stated"]:
            note = ("%s: the stated uncertainty changed from %s to %s"
                    % (today.isoformat(), show(old.get("stated")),
                       show(new_sheet["stated"])))
            notes.append(note)
            sheet_notes.append("%s (%s)" % (key, note))
        if not old:
            notes.append("%s: first read" % today.isoformat())
        record.update({"read": today.isoformat(),
                       "revised": new_sheet["revised"],
                       "stated": new_sheet["stated"],
                       "query": result["query"], "notes": notes})
        sheet_records[key] = record
    for ident, _name in spacecraft:
        rec = sheet_records.get(ident)
        if rec:
            for problem in sheet_problems(rec, rows):
                sheet_red.append("%s: %s" % (ident, problem))

    # Identity and period confirmations.
    for kind, key, result, _why in results:
        if result["status"] != "agrees" or kind == "sheet":
            continue
        obj = objects[key]
        record = dict(records.get(key) or {})
        if kind == "identity":
            record["confirmed"] = today.isoformat()
            for f in IDENTITY:
                record[f] = obj.get(f)
            record["object_type"] = obj.get("object_type")
            record["list_sha256"] = list_sha
            record["jpl_name"] = result["jpl"].get("name")
            record["jpl_type"] = result["jpl"].get("type")
            record.pop("pin", None)
            if result["pin"]:
                record["pin"] = result["pin"]
            record["queries"] = result["queries"]
        else:
            rec = obj["period"].get("record") or {}
            record["period"] = {
                "confirmed": today.isoformat(),
                "center": obj["period"].get("center"),
                "target": result.get("target"),
                "epoch": rec.get("epoch"),
                "days": rec.get("days"),
                "error_days": rec.get("error_days"),
                "jpl_days": result["jpl_days"],
                "query": result["query"],
            }
        records[key] = record

    # One line per thing examined.
    n_entries = len(objects)
    echo("Examined %d keyed entries and %d spacecraft sheets: %d due, %d "
         "queries asked of JPL."
         % (n_entries, len(spacecraft), len(tasks), queried))
    echo("")
    for key, text in quiet:
        echo("  %-18s %s" % (key, text))
    if sheets_quiet:
        echo("  %-18s %d of %d not due" % ("sheets", sheets_quiet,
                                           len(spacecraft)))
    for kind, key, result, why in results:
        word = result["status"]
        extra = ""
        if kind == "identity" and word == "agrees":
            extra = " -- JPL: %s" % result["jpl"].get("name")
        elif kind == "period" and word == "agrees":
            extra = " -- JPL's PR %s" % ("open orbit"
                                         if result["jpl_days"] is None
                                         else "%.10g days"
                                         % result["jpl_days"])
            if result.get("target") and result["target"] != str(
                    objects[key].get("horizons_id")):
                extra += " of %s" % result["target"]
        elif kind == "sheet" and word == "agrees":
            extra = " -- Revised %s" % result["sheet"]["revised"]
        elif result.get("error"):
            extra = " -- %s" % result["error"]
        label = ("%s (%s)" % (payload_name(spacecraft, key), key)
                 if kind == "sheet" else key)
        echo("  %-18s %s %s%s  [due: %s]" % (label, kind, word, extra, why))
        pin = result.get("pin") if kind == "identity" else None
        if pin:
            echo("  %-18s   pin: record %s is %s of %d for its comet; "
                 "solution date %s"
                 % ("", pin["record"],
                    "the newest" if pin["newest"] == pin["record"]
                    else "NOT the newest (%s is)" % pin["newest"],
                    pin["records"], pin["solution_date"] or "(none given)"))
    if not_compared:
        echo("")
        echo("Periods not compared, which the website marks as not from JPL: "
             "%s." % "; ".join(not_compared))
    if sheet_notes:
        echo("")
        echo("Sheets that changed, noted for a person (not red): %s."
             % "; ".join(sheet_notes))

    problems = []
    for kind, key, result, _why in results:
        if result["status"] == "not asked":
            continue
        if result["status"] == "could not reach JPL":
            echo("")
            echo("  %s (%s): could not reach JPL (%s)."
                 % (key, kind, result.get("error")))
            q = (result.get("queries") or [None])[-1] if kind == "identity" \
                else result.get("query")
            if q:
                echo("    query:  %s" % q)
            continue
        if result["status"] != "DISAGREES":
            continue
        if kind == "identity":
            for field, ours, theirs, url in result["disagreements"]:
                problems.append("%s.%s" % (key, field))
                echo("")
                echo("  %s.%s DISAGREES" % (key, field))
                echo("    list:   %s" % show(ours))
                echo("    JPL:    %s" % show(theirs))
                if url:
                    echo("    query:  %s" % url)
        elif kind == "period":
            field, ours, theirs, url = result["disagreement"]
            problems.append("%s.period" % key)
            echo("")
            echo("  %s.period DISAGREES" % key)
            echo("    served: %s" % show(ours))
            echo("    JPL:    %s" % show(theirs))
            if url:
                echo("    query:  %s" % url)
        else:
            problems.append("sheet %s (%s)" % (key, result.get("error")))
            echo("")
            echo("  sheet %s: %s" % (key, result.get("error")))
            echo("    query:  %s" % result.get("query"))
    for line in sheet_red:
        problems.append("sheet %s" % line)
        echo("")
        echo("  sheet %s" % line)

    unasked = [("%s's %s" % (k, kind)) for kind, k, r, _w in results
               if r["status"] in ("not asked", "could not reach JPL")]
    if down is not None:
        verdict = "UNREACHABLE"
        line = ("HORIZONS CHECK: UNREACHABLE -- JPL could not be reached "
                "(first at %s); not checked, and still due: %s"
                % (down, ", ".join(unasked)))
        if problems:
            line += "; also FAILED: %s" % "; ".join(problems)
    elif problems:
        verdict = "FAIL"
        line = "HORIZONS CHECK: FAIL -- %s" % "; ".join(problems)
    elif not tasks:
        verdict = "NOTHING DUE"
        line = ("HORIZONS CHECK: NOTHING DUE -- %d entries and %d sheets "
                "current, no query asked" % (n_entries, len(spacecraft)))
    else:
        verdict = "PASS"
        line = ("HORIZONS CHECK: PASS -- %d checked today, %d queries"
                % (len(tasks), queried))

    if write:
        ordered = {k: records[k] for k in objects if k in records}
        ordered.update({k: v for k, v in records.items() if k not in ordered})
        body = {"_comment": CONFIRMATIONS_COMMENT, "schema": 2,
                "cadence_days": CADENCE_DAYS, "objects": ordered}
        _write_if_changed(conf_path, render_json(body))
        sheet_body = {"_comment": SHEETS_COMMENT, "schema": 1,
                      "cadence_days": CADENCE_DAYS,
                      "seeded_from": sheets.get("seeded_from"),
                      "sheets": sheet_records}
        _write_if_changed(sheets_path, render_json(sheet_body))
        # This run's verdict, in its own file, which git ignores: it
        # changes on every run, and it is read only by
        # check_horizons_confirmations.py on the same machine, the same
        # day. Kept out of the confirmations so they move only when JPL
        # confirms something, and the export with them.
        _write_if_changed(os.path.join(root, LAST_RUN), render_json({
            "_comment": "Written by horizons_check.py on every run; read by "
                        "check_horizons_confirmations.py. Not tracked.",
            "date": today.isoformat(), "verdict": verdict,
            "asked": queried, "due": len(tasks),
            "problems": problems, "unasked": unasked}))
    echo("")
    if verdict in ("FAIL", "UNREACHABLE"):
        echo("Nothing in the list or in constants_new.py is edited here. A "
             "simple error is fixed by a session's patch; a choice goes to "
             "Tony.")
    echo(line)
    return (0 if verdict in ("PASS", "NOTHING DUE") else 1), {
        "verdict": verdict, "results": results, "problems": problems,
        "queried": queried, "due": len(tasks)}


def payload_name(spacecraft, ident):
    return dict(spacecraft).get(ident) or ident


def _write_if_changed(path, content):
    old = None
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", newline="") as handle:
            old = handle.read().replace("\r\n", "\n")
    if old != content:
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)


def main(argv):
    root = os.path.dirname(os.path.abspath(__file__))
    code, _ = run(root, live_fetch, datetime.date.today(),
                  check_all="--all" in argv)
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
