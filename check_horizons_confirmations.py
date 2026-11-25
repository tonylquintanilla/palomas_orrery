"""
check_horizons_confirmations.py -- every object the website takes from
the orrery's list has been confirmed against JPL Horizons, recently, and
has not changed since; each fetched period too; and every spacecraft
data sheet a row quotes still gives the row's figure (L-395, L-431).

WHY THIS EXISTS

    horizons_check.py asks JPL, in the maintenance run, about whatever is
    due, and records each confirmation. A generator's exit code does not
    count in that run, so the check's own red would not show. This reads
    what it recorded, offline, as a checker of the same run, and fails
    while anything is unconfirmed, overdue, changed, disagreeing or
    unreached. It never touches the network.

    The website keeps its own offline check (gallery
    tools/check_horizons_confirmations.py), which reads the same dates
    from the pulled export, so the website still shows a confirmation
    turning 30 days old when the orrery's run has not been run.

RUN COMMAND

    python check_horizons_confirmations.py
    python check_horizons_confirmations.py --night   (the night run's form)

    Open it in VS Code and click Run. orrery_maintenance_run.py runs it
    among the checkers, after the Horizons check and the objects export,
    and it gates.

WHAT MAKES IT FAIL, NAMED BY ENTRY

    - a keyed entry never confirmed, confirmed 30 or more days ago, or
      whose id, id_type or horizons_name changed since it was confirmed
    - a fetched period never confirmed, overdue, or changed since (a new
      fetch in the orrery makes it due at once)
    - today's Horizons check found a disagreement, or could not reach
      JPL: each is named as the check named it, with UNREACHABLE where
      JPL was not reached
    - a spacecraft sheet never read or 30 or more days old, or one a row
      of constants_new.py quotes whose figure the sheet no longer gives
      (option A, ruled 2026-10-12)
    - a record that cannot be read
    - (L-539) an entry the website does not serve but the orrery asks JPL
      for: never answered, changed since, or 30 days old; an entry that
      fits neither "asked" nor "not asked"; two entries with one name.
      By day also one whose first answer waits on Tony's look, or one JPL
      now differs on; at night those pass, by name.
    - (L-554) a craft still flying whose path the list cuts ('path_cutoff',
      no 'mission_end'; BepiColombo's at JPL's fit date): by day, red when
      JPL's sheet, read today, gives another fit day or path file than the
      entry was cut on (JPL REFIT), when the sheet was not read today, or
      when the entry has no cutoff_file. At night JPL REFIT passes by name,
      the night's commit title saying it, and a sheet not read tonight is
      printed as NOT READ, neither a pass nor red (R4). A pass prints both
      values compared.

    THE NIGHT RUN (L-485, R4: an outside failure is reported, never
    halting). With --night, which orrery_maintenance_run.py --night
    passes, today's UNREACHABLE is printed as REPORTED and is not red:
    what JPL left unasked is renewing, day 25 to 29, and passes. A
    confirmation that has truly lapsed, day 30, still fails by name, so
    only five nights running without JPL turn the night red, and then
    that is the true finding. A disagreement stays red on every run.

    A HELD BODY (L-485, the hold): one whose record carries a hold block,
    written by horizons_check.py when JPL no longer gives its identity
    as the list does. It is printed by name, with the date the hold
    began and its causes, and no lapse clock runs on it however long the
    hold lasts. With --night it passes AS HELD; by day it is red, "waiting
    on your look", as the day's voice is for what waits on a person.
    A value taken today is named (TAKEN) and passes on its new number. A
    period date that cannot be read, or a question JPL refused, is
    REPORTED at night and red by day, as an outage is.

    It uses horizons_check.py's own rules, so the two cannot disagree
    about what is due. It names the periods it does not compare -- typed,
    or not yet fetched, which the website marks as not from JPL -- and
    the served objects the list gives no key yet.

Role: devtool
Domain: dev_tools

Module created: October 10, 2026 with Anthropic's Claude Opus 5.5
(L-395, the Horizons check, in the gallery repo).
Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5 (L-431,
build 3, with L-395's move: the orrery's copy, a checker of its
maintenance run; it reads the periods and the spacecraft sheets too, and
today's check's verdict.)
Module updated: October 29, 2026 with Anthropic's Claude Opus 5.5 (L-504:
today is the UTC day, from utc_clock, as horizons_check.py dates its
confirmations; read from the local clock, an evening run in Chicago saw
tonight's confirmations as dated after today.)
Module updated: October 30, 2026 with Anthropic's Claude Opus 5.5 (L-485,
the nightly run: --night reports an unreached JPL instead of failing on
it, by Tony's ruling R4; a lapsed confirmation still fails.)
Module updated: October 31, 2026 with Anthropic's Claude Opus 5.5 (L-485,
the hold: a held body passes as held at night, by name, with no lapse
clock, and is red by day; today's takes are named; a reported period is
reported at night and red by day.)
Module updated: November 22, 2026 with Anthropic's Claude Opus 5.5 (L-539,
every entry checked: it judges the entries the website does not serve
too, through horizons_unserved.offline; unserved=False judges the served
entries alone, for their tests.)
Module updated: November 25, 2026 with Anthropic's Claude Opus 5.5 (L-554:
a cut path held to JPL's sheet, by horizons_check.cut_state, red by day
on JPL REFIT and on a sheet not read today; at night the first passes by
name and the second is NOT READ, neither pass nor red. cut_lines.)
"""

import datetime
import utc_clock   # L-504: the clock read as UTC
import json
import os
import sys

import export_objects
import horizons_check as hc


def cut_lines(cuts, sheet_records, today, night=False):
    """([failure], [line]) for the cut paths (L-554): each one's state by
    horizons_check.cut_state. By day all but "holds" fail. At night
    "refit" passes by name (the night's title carries JPL REFIT) and "not
    read" is NOT READ, neither a pass nor red; "blind", the list's own
    fault, fails at any hour."""
    failures, lines = [], []
    for cut in cuts:
        state, text = hc.cut_state(cut, sheet_records.get(cut["ident"]),
                                   today)
        if state == "holds":
            lines.append("  %-18s ok   -- %s" % ("path cut", text))
        elif night and state == "refit":
            lines.append("  %-18s JPL REFIT, not red at night (the night's "
                         "title says so) -- %s" % ("path cut", text))
        elif night and state == "not read":
            lines.append("  %-18s NOT READ tonight, neither passed nor red "
                         "(the night run, R4) -- %s" % ("path cut", text))
        else:
            failures.append("path cut %s" % text)
            lines.append("  %-18s FAIL -- %s%s" % (
                "path cut", "JPL REFIT: " if state == "refit" else "", text))
    return failures, lines


def run(root, today, echo=print, night=False, unserved=True):
    """0 when every confirmation passes, else 1. With unserved (the
    default), the entries the website does not serve are judged too, by
    horizons_unserved.offline (L-539); a test of the served entries alone
    passes False."""
    try:
        objects, _sha, spacecraft = hc.current_entries(root)
        confirmations = hc.load_confirmations(os.path.join(root,
                                                           hc.CONFIRMATIONS))
        sheets = hc.load_sheets(os.path.join(root, hc.SHEETS))
        cuts = hc.current_cuts(root)
    except (export_objects.ExportError, ValueError, OSError) as exc:
        echo("FAIL: %s" % exc)
        echo("HORIZONS CONFIRMATIONS: FAIL")
        return 1
    records = confirmations.get("objects") or {}
    sheet_records = sheets.get("sheets") or {}
    rows = hc.row_values(root)
    failures = []
    not_compared = []
    echo("Read %s (%d keyed entries), %s (%d) and %s (%d sheets), %s."
         % (export_objects.SOURCE, len(objects),
            hc.CONFIRMATIONS.replace(os.sep, "/"), len(records),
            hc.SHEETS.replace(os.sep, "/"), len(sheet_records),
            today.isoformat()))
    for key, obj in objects.items():
        hold = (records.get(key) or {}).get("hold")
        if hold:
            # L-485, the hold: a body held for an identity JPL no longer
            # gives as the list does is kept at its last confirmation and
            # waits for Tony. No lapse clock runs on it, however long the
            # hold lasts. At night it passes AS HELD; by day it is red, as
            # the day's voice is for what waits on a person.
            text = "HELD since %s: %s" % (hold.get("since"), "; ".join(
                hold.get("causes") or []))
            echo("  %-18s %s -- %s; kept at its confirmation of %s"
                 % (key, "held" if night else "FAIL", text,
                    (records.get(key) or {}).get("confirmed")))
            if not night:
                failures.append("%s: %s -- waiting on your look" % (key, text))
            continue
        state, detail = hc.confirmation_state(obj, records.get(key), today)
        pstate, pdetail = hc.period_state(obj.get("period"), records.get(key),
                                          today)
        bad = []
        if state not in hc.PASSING:
            bad.append(detail)
        if pstate == "not compared":
            if obj.get("period") is not None:
                not_compared.append("%s (%s)" % (key, pdetail))
        elif pstate not in hc.PASSING:
            bad.append(pdetail)
        if bad:
            failures.extend("%s: %s" % (key, b) for b in bad)
            echo("  %-18s FAIL -- %s" % (key, "; ".join(bad)))
        else:
            echo("  %-18s ok   -- identity %s; %s"
                 % (key, detail,
                    pdetail if pstate != "not compared"
                    else "period " + pdetail + ", not compared"))
    sheet_bad = 0
    for ident, name in spacecraft:
        record = sheet_records.get(ident)
        state, detail = hc.sheet_state(record, today)
        problems = hc.sheet_problems(record, rows) if record else []
        if state != "current" or problems:
            sheet_bad += 1
            text = "; ".join(([] if state == "current" else [detail])
                             + problems)
            failures.append("sheet %s (%s): %s" % (ident, name, text))
            echo("  %-18s FAIL -- %s" % ("%s (%s)" % (name, ident), text))
    echo("  %-18s %d of %d current, each figure a row quotes as the sheet "
         "gives it" % ("sheets", len(spacecraft) - sheet_bad, len(spacecraft)))
    # L-554: each cut path held to what its sheet said today.
    cut_fail, lines = cut_lines(cuts, sheet_records, today, night=night)
    for line in lines:
        echo(line)
    failures.extend(cut_fail)
    # L-539, every entry checked: the entries the website does not serve,
    # each held to the name and kind JPL gave its id. A first answer not
    # yet looked at, or one JPL now differs on, passes at night by name and
    # is red by day, waiting on Tony's look; a lapse is red at any hour.
    if unserved:
        import horizons_unserved
        failures.extend(horizons_unserved.offline(root, today, night=night,
                                                  echo=echo))
    last_path = os.path.join(root, hc.LAST_RUN)
    if os.path.exists(last_path):
        try:
            last = hc.load_json(last_path)
        except ValueError:
            last = {}
        if last.get("date") == today.isoformat():
            echo("Today's Horizons check: %s, %s due, %s queries asked."
                 % (last.get("verdict"), last.get("due"), last.get("asked")))
            if last.get("verdict") == "UNREACHABLE" and night:
                # L-485, R4: on the night run an outage is reported, not
                # red. What it leaves unasked is renewing (day 25 to 29)
                # and still passes; anything that has truly lapsed fails
                # above, by name, as on any other day.
                echo("REPORTED, not red (the night run, R4): JPL could not "
                     "be reached today; still due: %s"
                     % ", ".join(last.get("unasked") or []))
            elif last.get("verdict") == "UNREACHABLE":
                failures.append("UNREACHABLE: JPL could not be reached "
                                "today; still due: %s"
                                % ", ".join(last.get("unasked") or []))
            for problem in last.get("problems") or []:
                line = "today's check: %s" % problem
                if line not in failures:
                    failures.append(line)
            # L-485: a value taken from JPL is confirmed on its new number
            # and passes; it is named so a person can see it moved.
            for item in last.get("taken") or []:
                echo("TAKEN today: %s: %s -> %s"
                     % (item.get("name"), item.get("old"), item.get("new")))
            # A date that cannot be read, or a question JPL refused, is
            # reported at night, as an outage is, and red by day.
            for item in last.get("reported") or []:
                if night:
                    echo("REPORTED, not red (the night run, R4): %s" % item)
                else:
                    failures.append("REPORTED today: %s" % item)
        else:
            echo("Today's Horizons check: not run today (last run %s)."
                 % last.get("date"))
    else:
        echo("Today's Horizons check: no run recorded on this machine.")
    if not_compared:
        echo("Periods not compared, which the website marks as not from JPL: "
             "%s." % "; ".join(not_compared))
    stale = [k for k in records if k not in objects]
    if stale:
        echo("Confirmations for entries no longer keyed (kept, not checked): "
             "%s." % ", ".join(stale))
    if failures:
        echo("FAILURES (%d):" % len(failures))
        for line in failures:
            echo("  - " + line)
        unreachable = any(f.startswith("UNREACHABLE") for f in failures)
        echo("Run the maintenance run on a machine that reaches JPL; a "
             "disagreement is fixed by a session's patch.")
        echo("HORIZONS CONFIRMATIONS: %s -- %s"
             % ("UNREACHABLE" if unreachable else "FAIL",
                "; ".join(f.split(":")[0] for f in failures)))
        return 1
    compared = sum(1 for o in objects.values()
                   if (o.get("period") or {}).get("kind") == "fetched")
    held = [k for k in objects if (records.get(k) or {}).get("hold")]
    echo("HORIZONS CONFIRMATIONS: pass -- %d of %d entries and %d periods "
         "confirmed, %d sheets read, within %d days; %d cut path(s) held to "
         "JPL's sheet%s"
         % (len(objects) - len(held), len(objects), compared,
            len(spacecraft), hc.CADENCE_DAYS, len(cuts),
            "; HELD %s" % ", ".join(
                "%s since %s" % (k, records[k]["hold"].get("since"))
                for k in held) if held else ""))
    return 0


def main(argv=()):
    root = os.path.dirname(os.path.abspath(__file__))
    return run(root, utc_clock.utc_today(), night="--night" in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
