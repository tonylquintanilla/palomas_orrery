"""
horizons_unserved.py -- every entry of the orrery's list that the website
does not serve, but that the orrery asks JPL Horizons for, held to the
name and the kind JPL gives its id (L-539).

WHY THIS EXISTS

    horizons_check.py confirmed only the entries with a 'key', the ones
    the website serves. The others went unchecked, and on 2026-11-19
    L-297 (the Lagrange points) found that the orrery's two L3 entries,
    asked of JPL as 3013 and 33, had drawn the asteroids 3013 Dobrovoleva
    and 33 Polyhymnia under the points' names. Tony's ruling of
    2026-11-19, 15:30: the check covers every entry the orrery asks JPL
    for; a first run writes a one-time list, each entry beside the name
    JPL gives its id, for him to scan once; from then on JPL's name is
    stored and the entry held to it every 30 days, a few per run. The
    coordinating session's go-ahead of 2026-11-22 added: a first answer
    is not yet a confirmed one (the mark, below); the check catches the
    fall-through to the asteroids itself; JPL's kind is held as its name
    is; and "never asked" is read from the code, not typed twice.

WHICH ENTRIES ARE ASKED (a rule read from the list, never a list of names)

    served      an entry with a 'key': horizons_check.py holds it to its
                typed horizons_name. Counted here, not checked twice.
    not asked   an entry the fetch code never sends to JPL: its id is one
                the position and path fetches skip (NOT_ASKED_IDS, Planet
                9's placeholder), or its object_type is one every fetch
                skips (NOT_ASKED_TYPES, the exoplanet systems). Both are
                written inline in palomas_orrery.py and
                palomas_orrery_helpers.py; test_horizons_unserved.py
                fails when a copy here and the code's disagree.
    no JPL id   an entry whose id is the word 'none' (6AC4721). The orrery
                does send it, JPL answers "No matches found", and the
                orrery draws it from its typed elements, as Tony keeps it
                (2026-11-04). Named, never failed.
    asked       any other entry whose id_type is a word the orrery's
                fetches use: 'majorbody', 'id' or blank (astroquery sends
                the bare id; JPL looks among the planets, moons and
                spacecraft first and, finding none, among the asteroids)
                or 'smallbody' and 'designation' (the small bodies only).
    unsorted    anything else. Named, and it fails the run. Two entries
                with the same name fail the run too: the record is named
                by the entry's name, since these entries have no key and
                an id can be shared (-64, OSIRIS-REx and OSIRIS-APEX).

HOW ONE ENTRY IS ASKED

    JPL's Lookup, both indexes, as horizons_check.py asks a served entry.
    A planets-first entry passes when exactly one major body's primary
    SPKID is its id. If none is and the small-body index holds a body of
    that number, the entry FALLS THROUGH to the asteroids: that is the L3
    case, and it fails by name ("3013 ... JPL answers it as 3013
    Dobrovoleva"). A small-body entry passes when exactly one small
    body's primary designation is its id (or, for a 'designation' that
    is a number, its SPKID) and the major-body index finds none. JPL's
    name and its kind ("natural satellite", "spacecraft") are what is
    stored and held.

    JPL HAS NO OBJECT FOR THIS ID (the coordinating session's ruling of
    2026-11-22, on Xiangliu, Hi'iaka, Namaka and MK2): when both lists
    find nothing and JPL's main service, asked as the orrery asks,
    refuses the id ("is out of bounds", "No matches found"), that is an
    answer, stored as a name is. It never marks itself. Once Tony has
    looked, the entry is held to it: each cycle it is asked again and
    passes while JPL still has nothing; when JPL answers with an object,
    that is a new name, waiting on his look; a named entry whose id JPL
    no longer has DIFFERS. Both lists empty and the main service saying
    anything else is a blind spot, and fails by name.

THE MARK: WHO HAS LOOKED (the go-ahead's point 1)

    A first answer is stored, but not yet confirmed: the record carries
    "looked": null until Tony has looked at the pairing of the entry's
    own name and JPL's. A session sets the mark, from the "-- ok" lines
    Tony writes in his run record after scanning the one-time list, by
    running `python horizons_unserved.py --mark <name> ... --by <his run
    record>`. Tony never edits the record. An entry whose own name equals
    JPL's name, character for character, marks itself; one JPL has no
    object for never does. An unmarked entry
    is named on the night's record and in the night's commit title (NEW
    JPL NAME), and by day the offline checker shows it red, waiting on
    his look.

A MISMATCH (agreed as method by the go-ahead)

    Once stored, an entry whose id now answers another name or kind, or
    no object, or two, DIFFERS. Its stored values stay, a "differs" block
    names the causes, the night continues and its commit title starts
    with JPL DIFFERS, and by day it is red, waiting on Tony's look. It is
    asked every run until JPL and the record agree again. To accept a
    name JPL changed, a session adds that name as the entry's
    horizons_name in celestial_objects.py; the check then holds the entry
    to it, and takes JPL's kind with it. An entry whose id or id_type is
    edited is a new first answer, unmarked.

WHEN (agreed as method)

    Due from day RENEW_FROM_DAYS (20), at most PER_RUN (10) a run, oldest
    first; red at day 30 (horizons_check.CADENCE_DAYS). An entry never
    answered, or one that differs, is asked at once and not counted in
    the ten. The whole list is asked with `horizons_check.py --all`.
    JPL unreachable is UNREACHABLE, by name, and never a failed identity.

WHAT IT WRITES

    data/horizons_unserved_confirmations.json, declared to the night on
    the Horizons check's row. The objects export does not read it, so
    nothing the website reads moves. And, run with --list, the one-time
    list for Tony: documentation/CHECK_L539_every_entry_names_20261122.md.

RUN COMMAND

    It runs inside horizons_check.py (the maintenance run's Horizons check
    row). By hand, for a session:
        python horizons_unserved.py --list
        python horizons_unserved.py --mark "Io" "Europa" --by "<run record>"
    Its offline tests are test_horizons_unserved.py, section 8 of
    test_horizons_check.py.

Key functions:
    sort_entries() - each entry of the list as served, asked, not asked,
                     no JPL id or unsorted, with its reason
    ask() - JPL's two Lookup answers for one id, judged
    run() - what is due, asked, compared with the record, and written
    offline() - the offline checker's half, for check_horizons_confirmations
    write_list() - the one-time list for Tony

Consumed by: horizons_check.py, check_horizons_confirmations.py,
orrery_maintenance_run.py (the night's record and title),
test_horizons_unserved.py

Role: devtool
Domain: dev_tools

Module created: November 22, 2026 with Anthropic's Claude Opus 5.5
(L-539, every entry checked). Updated the same day, on the coordinating
session's ruling after the first live run: JPL HAS NO OBJECT FOR THIS ID
is an answer (ask() asks the main service when both lists are empty;
judge() holds it), and write_list() puts those entries first, with what
the orrery draws each from (drawn_from, the session's trace).
"""

import ast
import datetime
import json
import os
import re
import sys
import time

import export_objects
import horizons_check as hc
import utc_clock   # L-504: the clock read as UTC

RECORD = os.path.join("data", "horizons_unserved_confirmations.json")
LIST_DOC = os.path.join("documentation",
                        "CHECK_L539_every_entry_names_20261122.md")
# Agreed as method by the go-ahead of 2026-11-22: due from day 20, at most
# ten a run, red at day 30. The website never reads these, so there is no
# push-and-pull margin to keep, as the served entries' day 25 keeps.
RENEW_FROM_DAYS = 20
PER_RUN = 10

MB_WORDS = (None, "majorbody", "id")
SB_WORDS = ("smallbody", "designation")
# The fetch code's skips, copied so the check can name them; each is
# written inline in the code, so test_horizons_unserved.py reads the code
# and fails when the two disagree (the go-ahead's point 3).
#   palomas_orrery.py fetch_position and palomas_orrery_helpers.py
#   fetch_trajectory: `if object_id == 'planet9_placeholder':`
NOT_ASKED_IDS = {
    "planet9_placeholder": "the position and path fetches skip Planet 9's "
                           "placeholder id and draw it on its theoretical "
                           "orbit",
}
#   palomas_orrery.py, the plot's and the animation's object loops and both
#   pre-fetches: `obj.get('object_type') in [...]` / `not in [...]`
NOT_ASKED_TYPES = ("exoplanet", "exo_host_star", "exo_binary_star",
                   "exo_barycenter")
NOT_ASKED_TYPE_WHY = ("an exoplanet system is drawn from its own elements; "
                      "every fetch skips its kind")
NO_ID = "none"
NO_ID_WHY = ("its id is the word 'none': the orrery sends it, JPL answers "
             "\"No matches found\", and it is drawn from its typed elements "
             "(Tony keeps it so, 2026-11-04)")

READ = ("name", "id", "id_type", "object_type", "key", "horizons_name")

RECORD_COMMENT = (
    "Written by horizons_unserved.py, inside horizons_check.py (L-539): for "
    "each entry of the orrery's list that the website does not serve but "
    "the orrery asks JPL for, the name and kind JPL gives its id, when that "
    "was first answered and last confirmed, whether Tony has looked at the "
    "pairing ('looked'), and any way JPL now differs ('differs'). Named by "
    "the entry's name. The objects export does not read it. A session sets "
    "'looked' with --mark, from Tony's run record. Do not edit by hand.")


class ListError(Exception):
    pass


# ------------------------------------------------------------- the list

def read_list(root):
    """[entry] for every entry of celestial_objects.py, in list order:
    the fields READ, as literals, and its line. Raises ListError."""
    path = os.path.join(root, export_objects.SOURCE)
    try:
        with open(path, "rb") as handle:
            text = handle.read().decode("utf-8").replace("\r\n", "\n")
        node = export_objects.definitions(text)
    except (OSError, export_objects.ExportError) as exc:
        raise ListError(str(exc))
    out = []
    for item in node.elts:
        if not isinstance(item, ast.Dict):
            raise ListError("an item at line %d of OBJECT_DEFINITIONS is "
                            "not a dict literal" % item.lineno)
        fields = {"line": item.lineno}
        for k, v in zip(item.keys, item.values):
            if isinstance(k, ast.Constant) and k.value in READ:
                try:
                    fields[k.value] = ast.literal_eval(v)
                except ValueError:
                    raise ListError("line %d: '%s' is not a plain literal"
                                    % (item.lineno, k.value))
        out.append(fields)
    return out


def sort_entries(entries):
    """{served, asked, not_asked, no_id, unsorted, duplicates}.

    served, asked: [entry]; not_asked, no_id, unsorted: [(entry, why)];
    duplicates: [(name, [lines])]. Every entry lands on exactly one side.
    """
    out = {"served": [], "asked": [], "not_asked": [], "no_id": [],
           "unsorted": [], "duplicates": []}
    lines = {}
    for e in entries:
        lines.setdefault(e.get("name"), []).append(e["line"])
    out["duplicates"] = [(n, ls) for n, ls in lines.items() if len(ls) > 1]
    for e in entries:
        ident = e.get("id")
        id_type = e.get("id_type")
        otype = e.get("object_type")
        if "key" in e:
            out["served"].append(e)
        elif str(ident) in NOT_ASKED_IDS:
            out["not_asked"].append((e, NOT_ASKED_IDS[str(ident)]))
        elif otype in NOT_ASKED_TYPES:
            out["not_asked"].append((e, NOT_ASKED_TYPE_WHY))
        elif str(ident).strip().lower() == NO_ID:
            out["no_id"].append((e, NO_ID_WHY))
        elif not isinstance(e.get("name"), str) or not e["name"].strip():
            out["unsorted"].append((e, "it has no name to be recorded by"))
        elif not isinstance(ident, str) or not ident.strip():
            out["unsorted"].append((e, "its id %r is not an id the orrery "
                                       "can send" % (ident,)))
        elif id_type in MB_WORDS or id_type in SB_WORDS:
            out["asked"].append(e)
        else:
            out["unsorted"].append((e, "its id_type %r is not a word the "
                                       "orrery's fetches use, nor is its "
                                       "kind %r one they skip"
                                       % (id_type, otype)))
    return out


def label(e):
    return "%s (%s)" % (e.get("name"), e.get("id"))


# ------------------------------------------------------------- one entry

NO_OBJECT = "JPL has no object for this id"
# JPL's main service refusing an id, as it answered 120136472 (MK2) and
# 99999999 on 2026-11-22: "DXREAD: requested IOBJ= ******** is out of
# bounds, no action taken." A small-body search answers "No matches found."
REFUSED = re.compile(r"is out of bounds|No matches found", re.I)


def main_url(ident, id_type):
    """JPL's main service asked about one id as the orrery's astroquery
    asks it (horizons_check.command_of), its ';' sent as %3B."""
    command = hc.command_of(ident, id_type).replace(";", "%3B")
    return ("%s?format=text&COMMAND='%s'&OBJ_DATA=YES&MAKE_EPHEM=NO"
            % (hc.MAIN, command))


def refusal_line(text):
    """The first line of JPL's answer after its two header lines."""
    for line in text.splitlines():
        line = line.strip(" *")
        if line and not line.startswith(("API VERSION", "API SOURCE")):
            return line.strip()
    return "(an empty answer)"


def ask(ident, id_type, fetch, pause=0.0):
    """{status, jpl, problem, queries, error} for one id.

    status: "answered", "absent" (neither list finds it and the main
    service refuses it: NO_OBJECT), "FAILS" (problem says how) or "could
    not reach JPL". jpl: {name, kind, spkid, designation} when answered,
    {name None, kind None, absent True, answer} when absent."""
    out = {"status": "answered", "jpl": None, "problem": None,
           "queries": [], "error": None}
    ident = str(ident)
    absent = False

    def q(url):
        if out["queries"] and pause:
            time.sleep(pause)
        out["queries"].append(url)
        return fetch(url)

    try:
        if id_type in SB_WORDS:
            a = hc.parse_lookup(q(hc.lookup_url(ident, "sb")))
            b = hc.parse_lookup(q(hc.lookup_url(ident, "mb")))
            by_spkid = id_type == "designation" and ident.isdigit()
            here = hc.keep(a, ident, "mb" if by_spkid else "sb")
            there = hc.keep(b, ident, "mb")
            if len(here) > 1:
                out["problem"] = ("%d small bodies answer it: %s"
                                  % (len(here), "; ".join(m["name"]
                                                          for m in here)))
            elif not here and there:
                out["problem"] = ("no small body is %s; JPL answers it only "
                                  "among the major bodies, as %s"
                                  % (ident, there[0]["name"]))
            elif not here:
                absent = True
            elif there:
                out["problem"] = ("found in both indexes: the small body %s "
                                  "and the major body %s"
                                  % (here[0]["name"], there[0]["name"]))
            else:
                m = here[0]
        else:
            a = hc.parse_lookup(q(hc.lookup_url(ident, "mb")))
            b = hc.parse_lookup(q(hc.lookup_url(ident, "sb")))
            here = hc.keep(a, ident, "mb")
            if len(here) > 1:
                out["problem"] = ("%d major bodies answer it: %s"
                                  % (len(here), "; ".join(m["name"]
                                                          for m in here)))
            elif not here:
                # The fall-through (the go-ahead's point 2): asked by the
                # bare id, JPL finds no major body and answers with the
                # small body of that number -- the L3 case, 3013 as 3013
                # Dobrovoleva (L-297, 2026-11-18).
                fell = [m for m in b
                        if ident in (m["spkid"], m["designation"],
                                     m["name"].split(" ", 1)[0])]
                if fell:
                    out["problem"] = ("FALLS THROUGH to the asteroids: no "
                                      "major body is %s, so JPL answers it "
                                      "as %s" % (ident, fell[0]["name"]))
                else:
                    absent = True
            else:
                m = here[0]
        if absent:
            # The ruling of 2026-11-22 on Xiangliu, Hi'iaka, Namaka and MK2:
            # "JPL has no object for this id" is an answer, but only when
            # both lists find nothing AND JPL's main service, asked as the
            # orrery asks, refuses the id. Anything else it says is a blind
            # spot, and fails by name.
            url = main_url(ident, id_type)
            text = q(url)
            hc._jpl(text)
            if REFUSED.search(text):
                out["status"] = "absent"
                out["jpl"] = {"name": None, "kind": None, "absent": True,
                              "answer": refusal_line(text)}
                return out
            out["problem"] = ("neither of JPL's lists finds %s, yet its main "
                              "service answers: %s"
                              % (ident, refusal_line(text)))
        if out["problem"] is None:
            if not m["name"].strip():
                out["problem"] = "JPL's Lookup gives no name for %s" % ident
            else:
                out["jpl"] = {"name": m["name"], "kind": m["type"],
                              "spkid": m["spkid"],
                              "designation": m["designation"]}
    except hc.Unreachable as exc:
        out["status"] = "could not reach JPL"
        out["error"] = str(exc)
        return out
    if out["problem"] is not None:
        out["status"] = "FAILS"
    return out


# ------------------------------------------------------------- the record

def load_record(root):
    path = os.path.join(root, RECORD)
    if not os.path.exists(path):
        return {"schema": 1, "entries": {}}
    data = hc.load_json(path)
    if not isinstance(data.get("entries"), dict):
        raise ValueError("%s has no entries table" % RECORD)
    return data


def write_record(root, entries):
    body = {"_comment": RECORD_COMMENT, "schema": 1,
            "cadence_days": hc.CADENCE_DAYS,
            "renew_from_day": RENEW_FROM_DAYS, "per_run": PER_RUN,
            "entries": entries}
    hc._write_if_changed(os.path.join(root, RECORD), hc.render_json(body))


def moved(e, rec):
    """True when the entry's id or id_type is not the one recorded."""
    return (str(rec.get("id")) != str(e.get("id"))
            or rec.get("id_type") != e.get("id_type"))


def age_days(rec, today):
    day = hc.parse_day((rec or {}).get("confirmed"))
    return None if day is None else (today - day).days


def state_of(e, rec, today):
    """(state, detail) for an asked entry and its record:
    "never", "changed", "differs", "overdue", "renewing", "current"."""
    if not rec or not rec.get("first_answered"):
        return "never", "never answered by JPL"
    if moved(e, rec):
        return "changed", ("its id or id_type changed since JPL answered: "
                           "%s %r -> %s %r" % (rec.get("id"),
                                               rec.get("id_type"),
                                               e.get("id"),
                                               e.get("id_type")))
    if rec.get("differs"):
        return "differs", "JPL DIFFERS since %s: %s" % (
            rec["differs"].get("since"),
            "; ".join(rec["differs"].get("causes") or []))
    age = age_days(rec, today)
    if age is None:
        return "never", "its confirmation has no readable date"
    if age < 0:
        return "overdue", "confirmed on %s, which is after today" % (
            rec.get("confirmed"))
    if age >= hc.CADENCE_DAYS:
        return "overdue", "confirmed on %s, %d days ago (every %d days)" % (
            rec.get("confirmed"), age, hc.CADENCE_DAYS)
    if age >= RENEW_FROM_DAYS:
        return "renewing", "confirmed on %s, %d days ago; asked again from " \
            "day %d" % (rec.get("confirmed"), age, RENEW_FROM_DAYS)
    return "current", "confirmed on %s, %d day%s ago" % (
        rec.get("confirmed"), age, "" if age == 1 else "s")


def self_mark(name, jpl_name, today):
    if name == jpl_name:
        return {"date": today.isoformat(),
                "by": "itself: the entry's own name equals JPL's name"}
    return None


def shown(rec):
    """JPL's answer as a reader sees it: its name, or NO_OBJECT."""
    if rec.get("absent"):
        return NO_OBJECT
    return rec.get("jpl_name")


def judge(e, rec, result, today):
    """(new record or None, outcome, text). outcome: "first", "agrees",
    "accepted", "gained", "differs", "fails".

    An absent answer (NO_OBJECT, the ruling of 2026-11-22) is stored as a
    name is, never marks itself, and is held: while JPL still has nothing
    it agrees; when JPL answers with an object, that is a new name,
    waiting on Tony's look ("gained"); a named entry whose id JPL no
    longer has DIFFERS."""
    name = e["name"]
    fresh = not rec or not rec.get("first_answered") or moved(e, rec)
    if result["status"] == "FAILS":
        if fresh:
            return None, "fails", result["problem"]
        causes = [result["problem"]]
        jpl = {"problem": result["problem"]}
    else:
        jpl = result["jpl"]
        absent_now = result["status"] == "absent"
        if fresh:
            new = {"id": str(e.get("id")), "id_type": e.get("id_type"),
                   "object_type": e.get("object_type"),
                   "first_answered": today.isoformat(),
                   "confirmed": today.isoformat(),
                   "jpl_name": jpl["name"], "jpl_kind": jpl["kind"],
                   "jpl_spkid": jpl.get("spkid"),
                   "jpl_designation": jpl.get("designation"),
                   "absent": absent_now,
                   "looked": (None if absent_now
                              else self_mark(name, jpl["name"], today)),
                   "differs": None, "queries": result["queries"]}
            if absent_now:
                new["jpl_answer"] = jpl["answer"]
                return new, "first", "first answer: %s (JPL: %s)" % (
                    NO_OBJECT, jpl["answer"])
            return new, "first", "first answer: JPL names it %s (%s)" % (
                jpl["name"], jpl["kind"])
        was_absent = bool(rec.get("absent"))
        if was_absent and absent_now:
            new = dict(rec)
            new.update({"confirmed": today.isoformat(), "differs": None,
                        "queries": result["queries"],
                        "jpl_answer": jpl["answer"]})
            return new, "agrees", "agrees -- %s, still" % NO_OBJECT
        if was_absent:
            new = dict(rec)
            new.update({"confirmed": today.isoformat(), "differs": None,
                        "queries": result["queries"], "absent": False,
                        "jpl_name": jpl["name"], "jpl_kind": jpl["kind"],
                        "jpl_spkid": jpl["spkid"],
                        "jpl_designation": jpl["designation"],
                        "looked": None,
                        "gained": {"date": today.isoformat(),
                                   "was": NO_OBJECT}})
            new.pop("jpl_answer", None)
            return new, "gained", ("JPL now names it %s (%s), where it had "
                                   "no object: a new name, waiting on "
                                   "Tony's look" % (jpl["name"], jpl["kind"]))
        if absent_now:
            causes = ["name: %s -> %s" % (rec.get("jpl_name"), NO_OBJECT)]
        else:
            listed = e.get("horizons_name")
            accept = (isinstance(listed, str)
                      and listed != rec.get("jpl_name")
                      and jpl["name"] == listed)
            causes = []
            want = listed if isinstance(listed, str) else rec.get("jpl_name")
            if jpl["name"] != want:
                causes.append("name: %s -> %s" % (want, jpl["name"]))
            if not accept and jpl["kind"] != rec.get("jpl_kind"):
                causes.append("kind: %s -> %s" % (rec.get("jpl_kind"),
                                                  jpl["kind"]))
            if not causes:
                new = dict(rec)
                new["confirmed"] = today.isoformat()
                new["queries"] = result["queries"]
                was = new.get("differs")
                new["differs"] = None
                if accept:
                    new.update({"jpl_name": jpl["name"],
                                "jpl_kind": jpl["kind"],
                                "jpl_spkid": jpl["spkid"],
                                "jpl_designation": jpl["designation"],
                                "looked": {"date": today.isoformat(),
                                           "by": "the list's horizons_name, "
                                                 "added after Tony's look"}})
                    return new, "accepted", ("JPL's name %s taken from the "
                                             "list's horizons_name" % listed)
                return new, "agrees", ("agrees -- JPL: %s (%s)%s"
                                       % (jpl["name"], jpl["kind"],
                                          "; it no longer differs" if was
                                          else ""))
    new = dict(rec)
    prior = rec.get("differs") or {}
    new["differs"] = {
        "since": (prior.get("since") if prior.get("causes") == causes
                  else None) or today.isoformat(),
        "causes": causes, "jpl": jpl,
        "query": (result["queries"] or [""])[-1]}
    return new, "differs", "JPL DIFFERS: %s" % "; ".join(causes)


# ------------------------------------------------------------- the run

def due_list(asked, records, today, check_all=False):
    """(tasks, quiet, waiting_turn). tasks: [(entry, why)]. Entries never
    answered, changed or differing are asked at once; renewals at most
    PER_RUN, oldest first; the rest of the renewals wait their turn."""
    tasks, quiet, renew = [], [], []
    for e in asked:
        state, detail = state_of(e, records.get(e["name"]), today)
        if check_all or state in ("never", "changed", "differs"):
            tasks.append((e, detail))
        elif state in ("renewing", "overdue"):
            renew.append((age_days(records[e["name"]], today) or 0, e,
                          detail))
        else:
            quiet.append((e, detail))
    renew.sort(key=lambda r: (-r[0], r[1]["name"]))
    tasks.extend((e, d) for _a, e, d in renew[:PER_RUN])
    waiting_turn = [(e, d) for _a, e, d in renew[PER_RUN:]]
    return tasks, quiet, waiting_turn


def run(root, fetch, today, pause=hc.PAUSE_SECONDS, check_all=False,
        write=True, echo=print, down=None):
    """The unserved entries' half of the Horizons check. down names what
    JPL already failed on this run, so nothing is asked. Returns a summary:
    {queried, due, problems, unasked, down, differs, waiting, counts}."""
    summary = {"queried": 0, "due": 0, "problems": [], "unasked": [],
               "down": down, "differs": [], "waiting": [], "counts": {}}
    try:
        entries = read_list(root)
        record = load_record(root)
    except (ListError, ValueError, OSError) as exc:
        summary["problems"].append("the unserved entries could not be read: "
                                   "%s" % exc)
        echo("  FAIL: the unserved entries could not be read: %s" % exc)
        return summary
    records = record["entries"]
    sides = sort_entries(entries)
    asked = sides["asked"]
    summary["counts"] = dict((k, len(v)) for k, v in sides.items())
    echo("")
    echo("Unserved entries (L-539): %d entries in the list -- %d served, "
         "checked above; %d asked of JPL; %d never asked; %d asked with no "
         "JPL id; %d unsorted."
         % (len(entries), len(sides["served"]), len(asked),
            len(sides["not_asked"]), len(sides["no_id"]),
            len(sides["unsorted"])))
    for e, why in sides["not_asked"]:
        echo("  %-24s never asked: %s" % (label(e), why))
    for e, why in sides["no_id"]:
        echo("  %-24s asked with no JPL id: %s" % (label(e), why))
    for e, why in sides["unsorted"]:
        summary["problems"].append("%s unsorted" % e.get("name"))
        echo("  %-24s UNSORTED, neither asked nor not asked: %s"
             % (label(e), why))
    for n, ls in sides["duplicates"]:
        summary["problems"].append("%s named twice" % n)
        echo("  %-24s NAMED TWICE, at lines %s: the record is named by "
             "name" % (n, ", ".join(map(str, ls))))

    tasks, quiet, waiting_turn = due_list(asked, records, today, check_all)
    summary["due"] = len(tasks)
    echo("  %d asked entries: %d due, %d not due, %d waiting their turn "
         "(at most %d renewals a run)."
         % (len(asked), len(tasks), len(quiet), len(waiting_turn), PER_RUN))
    for e, detail in waiting_turn:
        echo("  %-24s waits its turn: %s" % (label(e), detail))
    first = True
    for e, why in tasks:
        if summary["down"] is not None:
            summary["unasked"].append("%s's identity" % e["name"])
            continue
        if not first and pause:
            time.sleep(pause)
        first = False
        result = ask(e["id"], e.get("id_type"), fetch, pause)
        summary["queried"] += len(result["queries"])
        if result["status"] == "could not reach JPL":
            summary["down"] = "%s's identity" % e["name"]
            summary["unasked"].append("%s's identity" % e["name"])
            echo("  %-24s could not reach JPL (%s)  [due: %s]"
                 % (label(e), result["error"], why))
            if result["queries"]:
                echo("    query:  %s" % result["queries"][-1])
            continue
        new, outcome, text = judge(e, records.get(e["name"]), result, today)
        if new is not None:
            records[e["name"]] = new
        echo("  %-24s %s  [due: %s]" % (label(e), text, why))
        if outcome in ("fails", "differs"):
            echo("    query:  %s" % (result["queries"] or [""])[0])
        if outcome == "fails":
            summary["problems"].append("%s.identity (%s)"
                                       % (e["name"], result["problem"]))
    names = set(e["name"] for e in asked)
    gone = sorted(n for n in records if n not in names)
    if gone:
        echo("  Records for entries no longer asked, kept, not checked: %s."
             % ", ".join(gone))
    for e in asked:
        rec = records.get(e["name"])
        if not rec or moved(e, rec):
            continue
        if rec.get("differs"):
            summary["differs"].append({
                "name": e["name"], "since": rec["differs"].get("since"),
                "cause": "; ".join(rec["differs"].get("causes") or [])})
        if not rec.get("looked"):
            summary["waiting"].append({"name": e["name"], "id": e["id"],
                                       "jpl_name": shown(rec)})
    for d in summary["differs"]:
        echo("  JPL DIFFERS %s -- since %s: %s; kept at its record, waiting "
             "on Tony's look" % (d["name"], d["since"], d["cause"]))
    if summary["waiting"]:
        echo("  NEW JPL NAME, waiting on Tony's look (%d): %s"
             % (len(summary["waiting"]), "; ".join(
                 "%s as %s" % (w["name"], w["jpl_name"])
                 for w in summary["waiting"])))
    if write:
        ordered = dict((e["name"], records[e["name"]]) for e in asked
                       if e["name"] in records)
        ordered.update((n, records[n]) for n in gone)
        write_record(root, ordered)
    return summary


def verdict_words(summary):
    """What the unserved half adds to the check's verdict line: JPL
    DIFFERS and NEW JPL NAME, the words the night's title is raised by."""
    words = ""
    if summary.get("differs"):
        words += "; JPL DIFFERS %s" % ", ".join(
            "%s since %s" % (d["name"], d["since"])
            for d in summary["differs"])
    if summary.get("waiting"):
        words += "; NEW JPL NAME %d waiting on Tony's look: %s" % (
            len(summary["waiting"]),
            ", ".join(w["name"] for w in summary["waiting"]))
    return words


# ------------------------------------------------------------- offline

def offline(root, today, night=False, echo=print):
    """The offline checker's half: [failure] for the unserved entries,
    read from the list and the record, never the network. At night an
    entry waiting on Tony's look, or one JPL differs on, passes by name;
    by day it is red. A lapse is red at any hour."""
    failures = []
    try:
        entries = read_list(root)
        records = load_record(root)["entries"]
    except (ListError, ValueError, OSError) as exc:
        return ["unserved entries: %s" % exc]
    sides = sort_entries(entries)
    for e, why in sides["unsorted"]:
        failures.append("%s: unsorted, %s" % (e.get("name"), why))
    for n, ls in sides["duplicates"]:
        failures.append("%s: named twice (lines %s)"
                        % (n, ", ".join(map(str, ls))))
    ok = 0
    waiting, differs = [], []
    for e in sides["asked"]:
        rec = records.get(e["name"])
        state, detail = state_of(e, rec, today)
        if state in ("never", "changed", "overdue"):
            failures.append("%s: %s" % (e["name"], detail))
            echo("  %-24s FAIL -- %s" % (label(e), detail))
            continue
        if state == "differs":
            differs.append(e["name"])
            echo("  %-24s %s -- %s" % (label(e), "differs" if night
                                       else "FAIL", detail))
            if not night:
                failures.append("%s: %s -- waiting on your look"
                                % (e["name"], detail))
            continue
        if not rec.get("looked"):
            waiting.append(e["name"])
            text = ("JPL names it %s; not yet looked at" % shown(rec)
                    if not rec.get("absent")
                    else "%s; not yet looked at" % NO_OBJECT)
            echo("  %-24s %s -- %s" % (label(e), "waiting" if night
                                       else "FAIL", text))
            if not night:
                failures.append("%s: %s -- waiting on your look"
                                % (e["name"], text))
            continue
        ok += 1
    echo("  %-24s %d of %d asked entries held to JPL's names and kinds; "
         "%d never asked; %d with no JPL id%s%s"
         % ("unserved", ok, len(sides["asked"]), len(sides["not_asked"]),
            len(sides["no_id"]),
            "; JPL DIFFERS %s" % ", ".join(differs) if differs else "",
            "; NEW JPL NAME %d waiting" % len(waiting) if waiting else ""))
    return failures


def night_lists(root):
    """(differs, waiting) for the night's record, read from the record and
    the list as they stand. Each a list of small dicts."""
    try:
        entries = read_list(root)
        records = load_record(root)["entries"]
    except (ListError, ValueError, OSError):
        return [], []
    differs, waiting = [], []
    for e in sort_entries(entries)["asked"]:
        rec = records.get(e["name"])
        if not rec or moved(e, rec):
            continue
        if rec.get("differs"):
            differs.append({"name": e["name"],
                            "since": rec["differs"].get("since"),
                            "cause": "; ".join(rec["differs"].get("causes")
                                               or [])})
        if not rec.get("looked"):
            waiting.append({"name": e["name"], "id": str(e.get("id")),
                            "jpl_name": shown(rec)})
    return differs, waiting


# ------------------------------------------------------------- the mark

def mark(root, names, by, today):
    """Set 'looked' on each named entry, by a session, from Tony's run
    record. Returns (marked, already, refused), with a reason for each
    refusal; an entry not answered, or one JPL differs on, is refused. One
    already marked (itself, or earlier) is left as it is and named."""
    records = load_record(root)["entries"]
    marked, already, refused = [], [], []
    for name in names:
        rec = records.get(name)
        if not rec:
            refused.append((name, "no record: never answered by JPL"))
        elif rec.get("differs"):
            refused.append((name, "JPL differs on it; a session settles that "
                                  "first"))
        elif rec.get("looked"):
            already.append((name, rec["looked"]["by"]))
        else:
            rec["looked"] = {"date": today.isoformat(), "by": by}
            marked.append(name)
    if marked:
        write_record(root, records)
    return marked, already, refused


# ------------------------------------------------------------- the list

def squash(text):
    return re.sub(r"[^a-z0-9]", "", str(text or "").lower())


def write_list(root, path=None, today=None, drawn_from=None):
    """The one-time list for Tony (outcome 2), from the list and the
    record as they stand. drawn_from: {name: what the orrery draws it
    from}, the session's trace, printed beside each entry JPL has no
    object for. Returns (path, counts)."""
    drawn_from = drawn_from or {}
    today = today or utc_clock.utc_today()
    entries = read_list(root)
    records = load_record(root)["entries"]
    sides = sort_entries(entries)
    rows, missing = [], []
    for e in sides["asked"]:
        rec = records.get(e["name"])
        if not rec or moved(e, rec):
            missing.append(e)
            continue
        rows.append((e, rec))
    none = [r for r in rows if r[1].get("absent")]
    hint = [r for r in rows if not r[1].get("absent")
            and squash(r[0]["name"]) not in squash(r[1].get("jpl_name"))]
    rest = [r for r in rows if r not in hint and r not in none]
    out = []
    w = out.append
    w("<!-- Doc-Kind: generated | The one-time list of L-539 (every entry "
      "checked): each entry the orrery asks JPL for, beside the name JPL "
      "gives its id, for Tony to scan once. -->")
    w("# Every entry beside JPL's name for it (L-539)")
    w("")
    w("Written %s by `python horizons_unserved.py --list`, from "
      "`data/horizons_unserved_confirmations.json` and "
      "`celestial_objects.py` as they stood. Built on the orrery's working "
      "copy at Tony's machine, at the base the session recorded. Claude "
      "Opus 5.5 in Claude Code." % today.isoformat())
    w("")
    w("**What to do:** scan it once. In your run record, copy each line at "
      "the top you have looked at and end it \"-- ok\" or \"-- wrong\". A "
      "session then marks the \"-- ok\" ones as looked at. Nothing here "
      "changes an entry.")
    w("")
    w("**The order is a hint, not a verdict.** The first part holds the "
      "entries whose own name, ignoring spaces, capitals and punctuation, "
      "does not appear inside JPL's name. A right entry can be there "
      "(a spacecraft the orrery calls by a short name), and a wrong one "
      "would have been too: Earth-Moon L3, asked as 3013, beside \"3013 "
      "Dobrovoleva\". Since this check, a wrong id like that one fails "
      "before it reaches this list.")
    w("")
    w("Each line: the orrery's name -- the id it asks -- JPL's name for "
      "that id -- JPL's kind.")
    w("")
    w("## %s (%d)" % (NO_OBJECT, len(none)))
    w("")
    w("Neither of JPL's lists finds the id, and JPL's main service, asked "
      "as the orrery asks, refuses it. Each line ends with what the orrery "
      "draws the entry from instead.")
    w("")
    for e, rec in none:
        w("- %s -- %s -- %s -- drawn from: %s"
          % (e["name"], e["id"], NO_OBJECT,
             drawn_from.get(e["name"], "(not traced)")))
    if not none:
        w("- none")
    w("")
    w("## Names that differ (%d)" % len(hint))
    w("")
    for e, rec in hint:
        w("- %s -- %s -- %s -- %s" % (e["name"], e["id"], rec["jpl_name"],
                                      rec["jpl_kind"]))
    if not hint:
        w("- none")
    w("")
    w("## Names that match (%d)" % len(rest))
    w("")
    for e, rec in rest:
        w("- %s -- %s -- %s -- %s%s"
          % (e["name"], e["id"], rec["jpl_name"], rec["jpl_kind"],
             " (marked itself: the names are the same)"
             if (rec.get("looked") or {}).get("by", "").startswith("itself")
             else ""))
    w("")
    if missing:
        w("## Not answered yet (%d)" % len(missing))
        w("")
        for e in missing:
            w("- %s -- %s -- (no answer from JPL recorded)"
              % (e["name"], e["id"]))
        w("")
    w("## Not on this list")
    w("")
    w("- The %d entries the website serves are already held to their typed "
      "names (`horizons_name` in `celestial_objects.py`) by the Horizons "
      "check every 30 days." % len(sides["served"]))
    for e, why in sides["no_id"]:
        w("- %s, asked with no JPL id: %s." % (e["name"], why))
    w("- Never asked of JPL (%d): %s." % (
        len(sides["not_asked"]),
        ", ".join(e["name"] for e, _w in sides["not_asked"])))
    w("")
    text = "\n".join(out) + "\n"
    path = path or os.path.join(root, LIST_DOC)
    with open(path, "w", encoding="ascii", newline="") as handle:
        handle.write(text)
    return path, {"no_object": len(none), "differ": len(hint),
                  "match": len(rest), "missing": len(missing)}


def main(argv):
    root = os.path.dirname(os.path.abspath(__file__))
    today = utc_clock.utc_today()
    if "--list" in argv:
        path, counts = write_list(root, today=today)
        print("Wrote %s: %d with no object at JPL, %d names that differ, "
              "%d that match, %d not answered yet."
              % (os.path.relpath(path, root), counts["no_object"],
                 counts["differ"], counts["match"], counts["missing"]))
        return 0
    if "--mark" in argv:
        i = argv.index("--mark")
        j = argv.index("--by") if "--by" in argv else -1
        if j < i + 2 or j + 1 >= len(argv):
            print("MARK REFUSED: give the names, then whose look it was: "
                  "--mark <name> ... --by \"<run record>\"")
            return 1
        marked, already, refused = mark(
            root, argv[i + 1:j], "Tony's look: %s" % argv[j + 1], today)
        for n in marked:
            print("marked  %s" % n)
        for n, by in already:
            print("already %s (%s)" % (n, by))
        for n, why in refused:
            print("REFUSED %s: %s" % (n, why))
        print("MARK: %d marked, %d already marked, %d refused"
              % (len(marked), len(already), len(refused)))
        return 1 if refused else 0
    print(__doc__.split("RUN COMMAND")[1].split("Key functions")[0])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
