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
"""

import datetime
import utc_clock   # L-504: the clock read as UTC
import json
import os
import sys

import export_objects
import horizons_check as hc


def run(root, today, echo=print):
    try:
        objects, _sha, spacecraft = hc.current_entries(root)
        confirmations = hc.load_confirmations(os.path.join(root,
                                                           hc.CONFIRMATIONS))
        sheets = hc.load_sheets(os.path.join(root, hc.SHEETS))
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
    last_path = os.path.join(root, hc.LAST_RUN)
    if os.path.exists(last_path):
        try:
            last = hc.load_json(last_path)
        except ValueError:
            last = {}
        if last.get("date") == today.isoformat():
            echo("Today's Horizons check: %s, %s due, %s queries asked."
                 % (last.get("verdict"), last.get("due"), last.get("asked")))
            if last.get("verdict") == "UNREACHABLE":
                failures.append("UNREACHABLE: JPL could not be reached "
                                "today; still due: %s"
                                % ", ".join(last.get("unasked") or []))
            for problem in last.get("problems") or []:
                line = "today's check: %s" % problem
                if line not in failures:
                    failures.append(line)
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
    echo("HORIZONS CONFIRMATIONS: pass -- %d of %d entries and %d periods "
         "confirmed, %d sheets read, within %d days"
         % (len(objects), len(objects), compared, len(spacecraft),
            hc.CADENCE_DAYS))
    return 0


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    return run(root, utc_clock.utc_today())


if __name__ == "__main__":
    sys.exit(main())
