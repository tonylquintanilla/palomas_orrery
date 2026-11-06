"""
patch_L476_4_ended_markers.py -- L-476 (the orrery plots by the path
plan): an ended mission's marker on its last day in the desktop's static
plot and animation, and its line ending there. With the records for this
session: L-476, L-423 (the website's checks) and Where We Are.

Built on orrery 01b212006a47d657d7b58f4a6d5431476d3520de at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 8ff3e7401052fa42a3976d2182d0e088d95bd3fe at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read live
on Nov 6, 2026. Written by the coordinating session of Nov 6 (Claude
Opus 5.5), on Tony's job of that morning, item b, his go-ahead of 12:20
Chicago, and his "Yes, add them" on the last-day pair.

WHY

    The desktop orrery asked JPL for every marker at the date chosen.
    So Pioneer 10's line stopped in 2003 at 82.1 AU while its marker sat
    at today's predicted 142.2 AU, and Galileo, whose JPL positions stop
    in 2003, had no marker at all. In the animation an ended mission's
    marker vanished after its last day. The website already puts the
    marker on the mission's last day.

WHAT IT CHANGES (six files, all or nothing)

    path_drawing.py      last_day, marker_moment and hold_last_day: an
                         ended mission (an entry with 'mission_end')
                         chosen after its path's last day is asked for
                         that day at 00:01 UTC, the website's moment; and
                         draw_plan adds the website's last-day pair to a
                         path that has ended, so its line ends at the
                         marker. Docstring and stamp.
    palomas_orrery.py    the static worker's two marker loops ask for
                         marker_moment, and the hover's sky position and
                         distance from Earth are asked for the same day;
                         the animation's frames after the last day hold
                         the marker there. Stamp.
    test_path_drawing.py checks 6, 7 and 8, each with a planted fault;
                         check 2 counts the pair; the --galileo check now
                         expects the pair drawn. Docstring and stamp.
    palomas_orrery_dashboard.py  the Path Drawing Suite's line (13 of
                         13); a Served List button and line for the
                         website's new check, which the dashboard parity
                         check requires. Stamp.
    LEDGER_CONSOLIDATED.md  L-476 and L-423: dated notes, new Gaps, date
                         stamps. Then it runs ledger_index.py.
    documentation/WHERE_WE_ARE.md  by section; nothing below the
                         run-record marker.

    The permanent part is the three functions, the edits that call them,
    the pair in draw_plan, the checks and the button. The script itself
    is one-shot.

    NOT CHANGED, AND NAMED: skills/horizons-orbital-mechanics/SKILL.md
    (1.18), A Plan Draws a Path Only Around the Sun, still says the
    orrery's drawing leaves out the last-day pair. Carried on L-476 for
    its next version.

RUN COMMAND

    Run the WEBSITE's patch_L423_positions_from_config.py first: this
    one refuses until the website has tools/test_served_list.py, since
    its dashboard button names that check.

    Then save this file in the orrery's root folder
    (C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\),
    open it in VS Code and click Run. (python patch_L476_4_ended_markers.py)

    Success: one "ok" line per edit, then the three checks' last lines,
    then "patch applied". Failure: one ERROR or ANCHOR FAIL line, and
    nothing is written. Undo is Discard Changes in GitHub Desktop.

    The ledger and Where We Are are checked only at the text each edit
    replaces, so your notes elsewhere never stop it.

Written November 6, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
WEBSITE = os.path.join(ROOT, "..", "tonyquintanilla.github.io")
LEDGER = "LEDGER_CONSOLIDATED.md"
PAGE = os.path.join("documentation", "WHERE_WE_ARE.md")
MARKER = b"--- Your run record below this line"

ORDER = ['path_drawing.py', 'test_path_drawing.py', 'palomas_orrery.py', 'palomas_orrery_dashboard.py']
EXPECT = {'path_drawing.py': '4d68a9647c059dd98242d260334ac892', 'test_path_drawing.py': 'e296f39f75cc0534b35110f393675761', 'palomas_orrery.py': 'a42adba7fd6c149762118097edf99f5b', 'palomas_orrery_dashboard.py': '1b36d3d935250c12bfc0b1287888708d'}
EXPECT_AFTER = {'path_drawing.py': '59989502dabe0fc83edab9507cb15bdd', 'test_path_drawing.py': '8a709bcef5e0c19918b1c0941f8a0d6f', 'palomas_orrery.py': '856fc20096b931dd670b25136ce6a6da', 'palomas_orrery_dashboard.py': '24259229b4bcf32e42f3801546a6c25e'}

EDITS = {name: [] for name in ORDER}
EDITS['path_drawing.py'].append(('docstring: key functions',
     b'    span_label() - a planned entry\'s "(start to end)" checkbox label\n',

     b'    span_label() - a planned entry\'s "(start to end)" checkbox label\n'
     b'    marker_moment() - the moment a marker is asked for: an ended\n'
     b"                   mission's last day, when the date chosen is after it\n"
     b"    hold_last_day() - an animation's frames after an ended mission's\n"
     b'                   last day hold its marker there\n'))
EDITS['path_drawing.py'].append(('docstring: stamp',
     b"Module updated: November 3, 2026, evening, with Anthropic's Claude Opus\n"
     b"5.5 (L-476, Tony's look: the website's daily tail added, so the solid\n"
     b'part ends at today; see the third paragraph).\n'
     b'"""\n',

     b"Module updated: November 3, 2026, evening, with Anthropic's Claude Opus\n"
     b"5.5 (L-476, Tony's look: the website's daily tail added, so the solid\n"
     b'part ends at today; see the third paragraph).\n'
     b"Module updated: November 6, 2026 with Anthropic's Claude Opus 5.5\n"
     b"(L-476, the ended missions' markers: last_day, marker_moment and\n"
     b"hold_last_day, so an ended mission's marker sits on its path's last day\n"
     b'in the static plot and the animation, as the website puts it; and\n'
     b"draw_plan adds the website's last-day pair to a path that has ended, so\n"
     b'its line ends at that marker).\n'
     b'"""\n'))
EDITS['path_drawing.py'].append(('last_day, marker_moment, hold_last_day',
     b'    if plan:\n'
     b'        return plan_span(plan)\n'
     b'    return obj.get("start_date"), obj.get("end_date")\n',

     b'    if plan:\n'
     b'        return plan_span(plan)\n'
     b'    return obj.get("start_date"), obj.get("end_date")\n'
     b'\n'
     b'\n'
     b"# The minute of an ended mission's last day its marker is asked for: the\n"
     b"# website's last served point, 00:01 UTC (fetch_path_last_day in its\n"
     b'# tools/gallery_cache_builder.py asks 00:00 and 00:01 of that day, and\n'
     b'# the room puts the marker on the later). A drawing choice mirrored from\n'
     b'# the website, not a measured value.\n'
     b'# Source: tools/gallery_cache_builder.py, fetch_path_last_day, read at\n'
     b'# gallery 8ff3e74 (tonyquintanilla.github.io): it asks last_day and\n'
     b'# last_day + 1 minute, at a 1m step.\n'
     b'LAST_DAY_MINUTE = 1\n'
     b'\n'
     b'\n'
     b'def last_day(obj, plans=None):\n'
     b'    """The day an ended mission\'s path ends, as a plain UTC datetime at\n'
     b"    00:00; None for an entry with no 'mission_end' (a mission still\n"
     b"    flying, or no mission at all). A planned entry's is its plan's last\n"
     b'    day, which already stops at the earlier of mission_end and\n'
     b"    path_cutoff and inside JPL's data (path_plan.path_stop): Akatsuki's\n"
     b'    is 2024-04-26, not its mission_end. An entry with no plan takes the\n'
     b'    earlier of those two days from the entry itself."""\n'
     b'    if not obj.get("mission_end"):\n'
     b'        return None\n'
     b'    plan = plan_for(obj, plans)\n'
     b'    if plan:\n'
     b'        return datetime.datetime.strptime(plan["span"]["end"], "%Y-%m-%d")\n'
     b'    end = min(d for d in (obj.get("mission_end"), obj.get("path_cutoff"))\n'
     b'              if d)\n'
     b'    return datetime.datetime(end.year, end.month, end.day)\n'
     b'\n'
     b'\n'
     b'def marker_moment(obj, when, plans=None):\n'
     b'    """(moment, ended): the moment an entry\'s marker is asked of JPL for.\n'
     b'    The moment chosen, except for an ended mission chosen after its\n'
     b"    path's last day: then that day at LAST_DAY_MINUTE, so the marker sits\n"
     b'    at the end of its drawn path, where the website puts it (L-476; Tony,\n'
     b'    2026-11-05: "an ended mission\'s marker on its last day, static plot\n'
     b'    and animation, Galileo too"). Before that day nothing changes, and\n'
     b'    neither does any entry with no \'mission_end\'."""\n'
     b'    day = last_day(obj, plans)\n'
     b'    if day is None:\n'
     b'        return when, False\n'
     b'    moment = day + datetime.timedelta(minutes=LAST_DAY_MINUTE)\n'
     b'    if when > moment:\n'
     b'        return moment, True\n'
     b'    return when, False\n'
     b'\n'
     b'\n'
     b'def hold_last_day(obj, dates, positions, fetch_at, plans=None):\n'
     b'    """An animation\'s positions for an ended mission, with every frame\n'
     b"    after its path's last day holding the marker on that day instead of\n"
     b"    hiding it. fetch_at(moment) is asked once, for the day's position;\n"
     b"    each such frame holds a copy of it with 'position_date' set to that\n"
     b'    moment, so the hover says which day it shows. Frames up to the last\n'
     b"    day, and any entry with no 'mission_end', are returned as they came.\n"
     b'    When JPL gives nothing for the day the frames stay as they came and\n'
     b'    the console says so."""\n'
     b'    day = last_day(obj, plans)\n'
     b'    if day is None:\n'
     b'        return positions\n'
     b'    moment = day + datetime.timedelta(minutes=LAST_DAY_MINUTE)\n'
     b'    after = [i for i, d in enumerate(dates)\n'
     b'             if d > moment and i < len(positions)]\n'
     b'    if not after:\n'
     b'        return positions\n'
     b'    point = fetch_at(moment)\n'
     b'    if not point or "x" not in point:\n'
     b'        print("[ENDED MISSION] %s: JPL gave no position for its last day, "\n'
     b'              "%s, so its marker is hidden after it"\n'
     b'              % (obj.get("name"), moment.strftime("%Y-%m-%d")), flush=True)\n'
     b'        return positions\n'
     b'    out = list(positions)\n'
     b'    for i in after:\n'
     b'        held = dict(point)\n'
     b'        held["position_date"] = moment\n'
     b'        out[i] = held\n'
     b'    print("[ENDED MISSION] %s: marker held on its last day, %s, for %d "\n'
     b'          "frame(s) after it" % (obj.get("name"), moment.strftime("%Y-%m-%d"),\n'
     b'                                 len(after)), flush=True)\n'
     b'    return out\n'))
EDITS['palomas_orrery.py'].append(("the static plot's first marker loop",
     b'                        pos_report = {}   # L-512 A2: what JPL answered\n'
     b'                        obj_data = fetch_position(fetch_id, date_obj, center_id=center_id, id_type=fetch_id_type,\n'
     b'                                                  report=pos_report)\n'
     b'                        \n'
     b'                        # Thread position timestamp for hover text\n'
     b'                        if obj_data is not None:\n'
     b"                            obj_data['position_date'] = date_obj\n",

     b"                        # L-476 (2026-11-06): an ended mission's marker on its path's\n"
     b'                        # last day, where the website puts it, when the date chosen\n'
     b'                        # is after that day (path_drawing.marker_moment).\n'
     b'                        marker_date, ended = path_drawing.marker_moment(obj, date_obj)\n'
     b'                        if ended:\n'
     b'                            print(f"[ENDED MISSION] {obj[\'name\']}: marker on its last day, "\n'
     b'                                  f"{marker_date:%Y-%m-%d}", flush=True)\n'
     b'                        pos_report = {}   # L-512 A2: what JPL answered\n'
     b'                        obj_data = fetch_position(fetch_id, marker_date, center_id=center_id, id_type=fetch_id_type,\n'
     b'                                                  report=pos_report)\n'
     b'                        \n'
     b'                        # Thread position timestamp for hover text\n'
     b'                        if obj_data is not None:\n'
     b"                            obj_data['position_date'] = marker_date\n"))
EDITS['palomas_orrery.py'].append(("the static plot's second marker loop",
     b'                    pos_report = {}   # L-512 A2: what JPL answered\n'
     b'                    obj_data = fetch_position(fetch_id, date_obj, center_id=center_id, id_type=fetch_id_type,\n'
     b'                                              report=pos_report)\n'
     b'\n'
     b'                    # Thread position timestamp for hover text\n'
     b'                    if obj_data is not None:\n'
     b"                        obj_data['position_date'] = date_obj\n",

     b"                    # L-476 (2026-11-06): an ended mission's marker on its path's\n"
     b'                    # last day, as in the loop above.\n'
     b'                    marker_date, ended = path_drawing.marker_moment(obj, date_obj)\n'
     b'                    if ended:\n'
     b'                        print(f"[ENDED MISSION] {obj[\'name\']}: marker on its last day, "\n'
     b'                              f"{marker_date:%Y-%m-%d}", flush=True)\n'
     b'                    pos_report = {}   # L-512 A2: what JPL answered\n'
     b'                    obj_data = fetch_position(fetch_id, marker_date, center_id=center_id, id_type=fetch_id_type,\n'
     b'                                              report=pos_report)\n'
     b'\n'
     b'                    # Thread position timestamp for hover text\n'
     b'                    if obj_data is not None:\n'
     b"                        obj_data['position_date'] = marker_date\n"))
EDITS['palomas_orrery.py'].append(("the animation's frames after the last day",
     b"                        positions_over_time[obj['name']] = pad_trajectory(\n"
     b'                            dates_list, \n'
     b'                            obj_start,\n'
     b'                            obj_end,\n'
     b'                            fetch_id, \n'
     b'                            center_id, \n'
     b'                            fetch_id_type\n'
     b'                        )\n',

     b"                        positions_over_time[obj['name']] = pad_trajectory(\n"
     b'                            dates_list, \n'
     b'                            obj_start,\n'
     b'                            obj_end,\n'
     b'                            fetch_id, \n'
     b'                            center_id, \n'
     b'                            fetch_id_type\n'
     b'                        )\n'
     b"                        # L-476 (2026-11-06): the frames after an ended mission's\n"
     b'                        # last day hold its marker there, instead of hiding it.\n'
     b"                        positions_over_time[obj['name']] = path_drawing.hold_last_day(\n"
     b"                            obj, dates_list, positions_over_time[obj['name']],\n"
     b'                            lambda moment: fetch_position(fetch_id, moment, center_id=center_id,\n'
     b'                                                          id_type=fetch_id_type))\n'))
EDITS['palomas_orrery.py'].append(('docstring: stamp',
     b"(plot_actual_orbits, the static worker's two, the animation worker's):\n"
     b'jpl_outcome.holds_fallback says so on the console.)\n'
     b'\n'
     b'"""\n',

     b"(plot_actual_orbits, the static worker's two, the animation worker's):\n"
     b'jpl_outcome.holds_fallback says so on the console.)\n'
     b"Module updated: November 6, 2026 with Anthropic's Claude Opus 5.5 (L-476,\n"
     b"the ended missions' markers): when the date chosen is after an ended\n"
     b"mission's last day, the static worker's two marker loops ask JPL for that\n"
     b'day (path_drawing.marker_moment), and its hover gives that day, its sky\n'
     b"position and its distance from Earth on that day; the animation's\n"
     b'frames after that day hold the marker there (path_drawing.hold_last_day)\n'
     b"instead of hiding it. Pioneer 10's marker now sits at the end of its line\n"
     b'and Galileo has one.)\n'
     b'\n'
     b'"""\n'))
EDITS['test_path_drawing.py'].append(('docstring: checks 6 and 7',
     b'      5. The daily tail around now: on a straight run, where the\n'
     b'         thinning keeps no point near now, the solid part still ends\n'
     b'         within five minutes of now. Planted fault: the tail turned off,\n'
     b'         and the solid part ends at the flyby, two months back.\n',

     b'      5. The daily tail around now: on a straight run, where the\n'
     b'         thinning keeps no point near now, the solid part still ends\n'
     b'         within five minutes of now. Planted fault: the tail turned off,\n'
     b'         and the solid part ends at the flyby, two months back.\n'
     b"      6. An ended mission's marker (marker_moment): chosen after the\n"
     b"         path's last day, it is asked for that day at 00:01; chosen\n"
     b'         before, nothing changes; a mission still flying never changes;\n'
     b"         a plan that stops before mission_end (Akatsuki's cutoff) gives\n"
     b"         the plan's day. Planted fault: the last day lost, and the\n"
     b'         marker is asked for the date chosen.\n'
     b'      7. The animation (hold_last_day): frames after the last day hold\n'
     b"         the last day's position, labelled with that moment, JPL asked\n"
     b'         once; frames before it and a mission still flying are as they\n'
     b'         came. Planted fault: the last day lost, and those frames stay\n'
     b'         empty, which hides the marker.\n'
     b"      8. An ended path's line ends at its marker: drawn after its\n"
     b"         span, its last point is the last-day pair's 00:01, the\n"
     b'         moment marker_moment asks the marker for. Planted fault: JPL\n'
     b'         asked nothing for the pair, and the line stops short.\n'))
EDITS['test_path_drawing.py'].append(('docstring: stamp',
     b"Module updated: November 3, 2026, evening, with Anthropic's Claude Opus\n"
     b'5.5 (L-476: check 5, the daily tail, and its planted fault).\n'
     b'"""\n',

     b"Module updated: November 3, 2026, evening, with Anthropic's Claude Opus\n"
     b'5.5 (L-476: check 5, the daily tail, and its planted fault).\n'
     b"Module updated: November 6, 2026 with Anthropic's Claude Opus 5.5\n"
     b"(L-476: checks 6 and 7, an ended mission's marker on its last day in the\n"
     b'static plot and the animation, and check 8, its line ending at that\n'
     b'marker by the last-day pair, each with a planted fault; check 2 counts\n'
     b'the pair; the --galileo check now expects the pair drawn).\n'
     b'"""\n'))
EDITS['test_path_drawing.py'].append(('checks 6 and 7',
     b'    check(bad is not None and bad > 1440.0,\n'
     b'          "5. planted fault caught: with the tail turned off the solid "\n'
     b'          "part ends %s minutes before now" % bad)\n',

     b'    check(bad is not None and bad > 1440.0,\n'
     b'          "5. planted fault caught: with the tail turned off the solid "\n'
     b'          "part ends %s minutes before now" % bad)\n'
     b'\n'
     b'    ok, why = ended_marker()\n'
     b'    check(ok, "6. an ended mission\'s marker is asked for its last day "\n'
     b'          "when the date chosen is after it: %s" % why)\n'
     b'    ok, why = ended_frames()\n'
     b'    check(ok, "7. the animation holds an ended mission\'s marker on its "\n'
     b'          "last day: %s" % why)\n'
     b'    saved = pd.last_day\n'
     b'    pd.last_day = lambda obj, plans=None: None\n'
     b'    try:\n'
     b'        bad6 = ended_marker()[0]\n'
     b'        bad7 = ended_frames()[0]\n'
     b'    finally:\n'
     b'        pd.last_day = saved\n'
     b'    check(not bad6, "6. planted fault caught: with the last day lost, the "\n'
     b'          "marker is asked for the date chosen")\n'
     b'    check(not bad7, "7. planted fault caught: with the last day lost, the "\n'
     b'          "frames after it stay empty")\n'
     b'\n'
     b'    last, marker = ended_line()\n'
     b'    check(last == marker, "8. an ended path\'s line ends at its marker: its "\n'
     b'          "last point %s, the marker %s" % (last, marker))\n'
     b'\n'
     b'    def no_pair(ident, id_type, start, stop, step):\n'
     b'        return {} if step == "1m" else FakeJPL()(ident, id_type, start,\n'
     b'                                                 stop, step)\n'
     b'    last, marker = ended_line(fetch=no_pair)\n'
     b'    check(last != marker, "8. planted fault caught: with no last-day pair "\n'
     b'          "the line stops at %s, short of the marker %s" % (last, marker))\n'
     b'\n'
     b'\n'
     b"# An ended mission's made-up plan, and one cut before its mission_end.\n"
     b'ENDED = {"craft_ended": {"span": {"start": "1972-03-04", "end": "2003-01-23"}},\n'
     b'         "craft_cut": {"span": {"start": "2010-05-22", "end": "2024-04-26"}}}\n'
     b'\n'
     b'\n'
     b'def ended_marker():\n'
     b'    """(ok, why) for marker_moment on made-up entries."""\n'
     b'    ended = {"key": "craft_ended", "mission_end": datetime.datetime(2003, 1, 23)}\n'
     b'    cut = {"key": "craft_cut", "mission_end": datetime.datetime(2025, 9, 18),\n'
     b'           "path_cutoff": datetime.datetime(2024, 4, 26)}\n'
     b'    flying = {"key": "craft_ended"}\n'
     b'    unplanned = {"name": "Unplanned", "mission_end": datetime.datetime(2003, 9, 21)}\n'
     b'    today = datetime.datetime(2026, 11, 6, 12, 0)\n'
     b'    before = datetime.datetime(2000, 6, 1)\n'
     b'    got = {\n'
     b'        "ended, after": pd.marker_moment(ended, today, ENDED),\n'
     b'        "ended, before": pd.marker_moment(ended, before, ENDED),\n'
     b'        "flying": pd.marker_moment(flying, today, ENDED),\n'
     b'        "cut": pd.marker_moment(cut, today, ENDED),\n'
     b'        "unplanned": pd.marker_moment(unplanned, today, ENDED),\n'
     b'    }\n'
     b'    want = {\n'
     b'        "ended, after": (datetime.datetime(2003, 1, 23, 0, 1), True),\n'
     b'        "ended, before": (before, False),\n'
     b'        "flying": (today, False),\n'
     b'        "cut": (datetime.datetime(2024, 4, 26, 0, 1), True),\n'
     b'        "unplanned": (datetime.datetime(2003, 9, 21, 0, 1), True),\n'
     b'    }\n'
     b'    wrong = ["%s gave %s, wanted %s" % (k, got[k], want[k])\n'
     b'             for k in want if got[k] != want[k]]\n'
     b'    return not wrong, ("; ".join(wrong) if wrong else\n'
     b'                       "after the last day 2003-01-23 00:01, before it the "\n'
     b'                       "date chosen, a cut plan 2024-04-26 00:01, a mission "\n'
     b'                       "still flying unchanged")\n'
     b'\n'
     b'\n'
     b'def ended_frames():\n'
     b'    """(ok, why) for hold_last_day on a made-up animation of six yearly\n'
     b'    frames, 2001 to 2006, the path ending on 2003-01-23."""\n'
     b'    ended = {"key": "craft_ended", "name": "Craft",\n'
     b'             "mission_end": datetime.datetime(2003, 1, 23)}\n'
     b'    dates = [datetime.datetime(y, 6, 1) for y in range(2001, 2007)]\n'
     b'    padded = [{"x": 1.0}, {"x": 2.0}, None, None, None, None]\n'
     b'    asked = []\n'
     b'\n'
     b'    def fetch_at(moment):\n'
     b'        asked.append(moment)\n'
     b'        return {"x": 82.1, "y": 0.0, "z": 0.0}\n'
     b'\n'
     b'    held = pd.hold_last_day(ended, dates, padded, fetch_at, ENDED)\n'
     b'    flying = pd.hold_last_day({"key": "craft_ended", "name": "Flying"},\n'
     b'                              dates, padded, fetch_at, ENDED)\n'
     b'    moment = datetime.datetime(2003, 1, 23, 0, 1)\n'
     b'    ok = (held[:2] == padded[:2]\n'
     b'          and all(p and p["x"] == 82.1 and p["position_date"] == moment\n'
     b'                  for p in held[2:])\n'
     b'          and asked == [moment] and flying == padded)\n'
     b'    return ok, ("frames %s; JPL asked %s"\n'
     b'                % ([None if p is None else p["x"] for p in held],\n'
     b'                   [m.strftime("%Y-%m-%d %H:%M") for m in asked]))\n'))
EDITS['palomas_orrery_dashboard.py'].append(("the Path Drawing Suite's line",
     b'         "the checkbox label from the plan, and the solid part ending at "\n'
     b'         "today on a straight run; two planted faults caught. "\n'
     b'         "Ends on \\"PATH DRAWING SUITE: 7 of 7 checks passed\\" (L-476).",\n',

     b'         "the checkbox label from the plan, the solid part ending at "\n'
     b'         "today on a straight run, and an ended mission\'s marker on its "\n'
     b'         "last day in the plot and the animation, its line ending there; "\n'
     b'         "five planted faults caught. "\n'
     b'         "Ends on \\"PATH DRAWING SUITE: 13 of 13 checks passed\\" (L-476).",\n'))
EDITS['palomas_orrery_dashboard.py'].append(('docstring: stamp',
     b"(L-510: the Objects Mirror Check's and Suite's descriptions say the\n"
     b"website's objects mirror follows a body across e = 1 by itself).\n",

     b"(L-510: the Objects Mirror Check's and Suite's descriptions say the\n"
     b"website's objects mirror follows a body across e = 1 by itself).\n"
     b"Module updated: November 6, 2026 with Anthropic's Claude Opus 5.5\n"
     b"(L-476: the Path Drawing Suite's line, 13 checks, five planted faults.\n"
     b"L-423: the website's Served List button and line, and the offline\n"
     b"run's card names it.)\n"))
EDITS['path_drawing.py'].append(('docstring: the last-day pair',
     b"length and step; its moments are each night's, so only an ended path,\n"
     b"which has no tail, agrees point for point. An ended mission's last-day\n"
     b"pair is the website room's need and is not drawn here. Its twin is\n",

     b"length and step; its moments are each night's, so only an ended path,\n"
     b'which has no tail, agrees point for point. An ended path also gets the\n'
     b"website's last-day pair, 00:00 and 00:01 UTC of its span's last day,\n"
     b"since an ended mission's marker sits on that day (marker_moment): its\n"
     b'line ends at its marker (added 2026-11-06, L-476; Tony: "Yes, add\n'
     b'them"; before, the line could stop up to six days short, 0.12 AU for\n'
     b'Akatsuki near Venus). Its twin is\n'))
EDITS['path_drawing.py'].append(('draw_plan: its docstring',
     b"    plan, the website's whole fetch with its daily tail around now (UTC;\n"
     b'    utc_now() when not given), without its last-day pair.\n',

     b"    plan, the website's whole fetch with its daily tail around now (UTC;\n"
     b'    utc_now() when not given), and for a path whose span ended before\n'
     b"    now its last-day pair, as the website's fetch_path_last_day adds it.\n"))
EDITS['path_drawing.py'].append(('draw_plan: the last-day pair',
     b'        if t0 < t1:\n'
     b'            points.update(fetch(ident, id_type, t0, t1, TAIL_STEP))\n',

     b'        if t0 < t1:\n'
     b'            points.update(fetch(ident, id_type, t0, t1, TAIL_STEP))\n'
     b'        # The last-day pair (L-476, 2026-11-06): a path whose span ended\n'
     b'        # before today gets 00:00 and 00:01 UTC of its last day, as the\n'
     b"        # website's fetch_path_last_day asks them, so an ended mission's\n"
     b'        # line ends where its marker sits (marker_moment, 00:01).\n'
     b'        day = datetime.datetime.strptime(plan["span"]["end"], "%Y-%m-%d")\n'
     b'        if day + datetime.timedelta(days=1) <= today:\n'
     b'            points.update(fetch(ident, id_type, day, day + datetime.timedelta(\n'
     b'                minutes=LAST_DAY_MINUTE), "1m"))\n'))
EDITS['test_path_drawing.py'].append(('ended_line',
     b'def solid_gap():\n',

     b'def ended_line(fetch=None):\n'
     b'    """(the line\'s last moment, the marker\'s moment) for PLAN drawn as an\n'
     b'    ended mission\'s path, on a day after its span."""\n'
     b'    entry = {"key": "craft", "name": "Craft", "id": "-1", "id_type": "id",\n'
     b'             "mission_end": datetime.datetime(2025, 7, 1)}\n'
     b'    now = datetime.datetime(2026, 11, 6, 12, 0)\n'
     b'    pts = pd.draw_plan(entry, PLAN, fetch=fetch or FakeJPL(), now=now)\n'
     b'    marker = pd.marker_moment(entry, now, {"craft": PLAN})[0]\n'
     b'    return (pts[-1]["date"] if pts else None), marker\n'
     b'\n'
     b'\n'
     b'def solid_gap():\n'))
EDITS['test_path_drawing.py'].append(('check 2 counts the pair',
     b'    inside = all(a >= start and b <= end for a, b, _ in jpl.asked)\n'
     b'    check(top > 0.004 and inside and len(jpl.asked) == 2,\n'
     b'          "2. the flyby\'s bend is kept (highest y %.4f AU of 0.005, %d "\n'
     b'          "points) and JPL is asked %d times, inside the span"\n'
     b'          % (top, len(pts), len(jpl.asked)))\n',

     b'    pair = [a for a in jpl.asked if a[2] == "1m"]\n'
     b'    rest = [a for a in jpl.asked if a[2] != "1m"]\n'
     b'    inside = all(a >= start and b <= end for a, b, _ in rest)\n'
     b'    check(top > 0.004 and inside and len(rest) == 2 and len(pair) == 1,\n'
     b'          "2. the flyby\'s bend is kept (highest y %.4f AU of 0.005, %d "\n'
     b'          "points) and JPL is asked %d times inside the span, and %d for "\n'
     b'          "the last-day pair" % (top, len(pts), len(rest), len(pair)))\n'))
EDITS['test_path_drawing.py'].append(('docstring: the --galileo check',
     b"    GALLERY_PIN, apart from the website's last-day pair, which the\n"
     b"    orrery does not draw and which is named. Galileo's path ended in\n",

     b'    GALLERY_PIN, its last-day pair included (the orrery draws it since\n'
     b"    2026-11-06, L-476; before, it was left out). Galileo's path ended in\n"))
EDITS['test_path_drawing.py'].append(('the --galileo check expects the pair',
     b'    extra, missing = sorted(mine - web), sorted(web - mine - last_day)\n'
     b'    ok = bool(mine) and not extra and not missing and len(last_day) == 2\n',

     b'    # Since 2026-11-06 the orrery draws the last-day pair too (L-476).\n'
     b'    extra, missing = sorted(mine - web), sorted(web - mine)\n'
     b'    ok = (bool(mine) and not extra and not missing and len(last_day) == 2\n'
     b'          and last_day <= mine)\n'))
EDITS['palomas_orrery.py'].append(("the hover's RA/Dec on the marker's day",
     b'            # Fetch RA/Dec and uncertainties - NOW RECEIVING 4 VALUES\n'
     b'            ra_deg, dec_deg, ra_3sigma, dec_3sigma, earth_distance_au = fetch_radec_for_hover(\n'
     b"                obj_info['id'], \n"
     b'                get_date_from_gui(), \n'
     b"                obj_info.get('id_type')\n"
     b'            )\n',

     b'            # Fetch RA/Dec and uncertainties - NOW RECEIVING 4 VALUES\n'
     b'            # L-476 (2026-11-06): asked for the day the marker shows, so an\n'
     b"            # ended mission's sky position and distance from Earth are its\n"
     b"            # last day's, as its marker is (path_drawing.marker_moment).\n"
     b'            ra_deg, dec_deg, ra_3sigma, dec_3sigma, earth_distance_au = fetch_radec_for_hover(\n'
     b"                obj_info['id'], \n"
     b'                path_drawing.marker_moment(obj_info, get_date_from_gui())[0], \n'
     b"                obj_info.get('id_type')\n"
     b'            )\n'))
EDITS['palomas_orrery_dashboard.py'].append(('the Served List button',
     b'        "Planted faults, among them an orbit drawn around the Sun, are each "\n'
     b'        "caught. GATES the gallery runner.",\n'
     b'        GALLERY_REPO_DIR,\n'
     b'        True,\n'
     b'        None,\n'
     b'        True),\n'
     b'        "FROM THE ORRERY -- its numbers, drawings and pole",\n',

     b'        "Planted faults, among them an orbit drawn around the Sun, are each "\n'
     b'        "caught. GATES the gallery runner.",\n'
     b'        GALLERY_REPO_DIR,\n'
     b'        True,\n'
     b'        None,\n'
     b'        True),\n'
     b'        ("Served List",\n'
     b'        os.path.join("tools", "test_served_list.py"),\n'
     b'        "The live check\'s positions files (L-423): read from "\n'
     b'        "data/objects_config.json -- every spacecraft and every comet on "\n'
     b'        "an open path, by the cache builder\'s own rule -- instead of "\n'
     b'        "typed, so a body that crosses e = 1 changes the list by itself. "\n'
     b'        "Checks each file the config names is in the served cache and "\n'
     b'        "none is typed, then plants five faults, each caught: a comet "\n'
     b'        "joining, one leaving, two configs that cannot give a list, and a "\n'
     b'        "404 on Pioneer 10\'s file. Fetches nothing. GATES the gallery "\n'
     b'        "runner.",\n'
     b'        GALLERY_REPO_DIR,\n'
     b'        True,\n'
     b'        None,\n'
     b'        True),\n'
     b'        "FROM THE ORRERY -- its numbers, drawings and pole",\n'))
EDITS['palomas_orrery_dashboard.py'].append(("the Served List button's line",
     b'     "Drawn Orbit"):\n'
     b'        "Checks a barycentre orbit is served and drawn around the barycentre.",\n',

     b'     "Drawn Orbit"):\n'
     b'        "Checks a barycentre orbit is served and drawn around the barycentre.",\n'
     b'    ("Gallery -- checks and data",\n'
     b'     "Served List"):\n'
     b'        "Checks the live check reads its positions files from the config.",\n'))
EDITS['palomas_orrery_dashboard.py'].append(("the offline run's card names it",
     b'        "guest book updater, the Daily Run\'s steps, the artifact-1 "\n',

     b'        "guest book updater, the Daily Run\'s steps, the served list, the "\n'
     b'        "artifact-1 "\n'))

LEDGER_EDITS = [
    ('L-476: the Nov 6 build and a new Gap',
     b'**Gap (replaces the one below, 2026-11-05, evening):** the next small\n',

     b"- **2026-11-06: built, an ended mission's marker on its last day in\n"
     b'  the desktop** (the coordinating session of Nov 6, Claude Opus 5.5,\n'
     b'  through the python_work door, built on orrery 01b2120 and gallery\n'
     b"  8ff3e74; `patch_L476_4_ended_markers.py`). Tony's go-ahead of Nov 6,\n"
     b'  12:20 Chicago ("proceed"), on the instrument proposed: a patch to\n'
     b'  `palomas_orrery.py` with a helper in `path_drawing.py`.\n'
     b"  - The static plot: both of the worker's marker loops ask JPL for\n"
     b'    `path_drawing.marker_moment`: the date chosen, or, for an entry\n'
     b"    with `mission_end` chosen after its path's last day, that day at\n"
     b"    00:01 UTC, the website's last served point. The hover's sky\n"
     b'    position and distance from Earth are asked for the same moment\n'
     b"    (`add_celestial_object`); they had been asked for the GUI's date.\n"
     b'  - The animation: `path_drawing.hold_last_day` gives the frames after\n'
     b"    the last day that day's position, asked once, its `position_date`\n"
     b'    that moment. Before, `pad_trajectory` left them empty and the\n'
     b"    marker vanished after the mission's end.\n"
     b'  - Found while building, and added on Tony\'s word (Nov 6: "Yes, add\n'
     b'    them"): the drawn line stopped up to six days short of its marker.\n'
     b"    Measured on the website's served files: Akatsuki 0.12 AU near\n"
     b'    Venus, DART 0.07 AU, Pioneer 10 0.035 AU. `draw_plan` now adds the\n'
     b"    website's last-day pair (00:00 and 00:01 UTC of the span's last\n"
     b'    day) to a path that has ended, so the line ends at the marker.\n'
     b'  - Verified in a throwaway copy: the path drawing suite "13 of 13\n'
     b'    checks passed" (checks 6 to 8 new, each with a planted fault;\n'
     b'    check 2 counts the pair). The real plot and animation run headless\n'
     b"    with JPL replaced by a stand-in. Before the patch, Pioneer 10's\n"
     b"    marker was asked for today and drawn at the stand-in's 138.3 AU\n"
     b'    while its line ended at 78.1 AU, and its frames after 2003 were\n'
     b'    hidden. After it, the marker sits at 78.148 AU on 2003-01-23 00:01\n'
     b'    UTC, the line ends at the same point, and the frames hold it;\n'
     b'    Galileo likewise on 2003-09-21. The orrery\'s maintenance run: "35\n'
     b'    of 35 gating checkers passed", "0 TIER-1 -- the push gate holds".\n'
     b'  - Not run here: `python test_path_drawing.py --galileo`, which needs\n'
     b'    JPL. It now expects the last-day pair drawn.\n'
     b"  - Carried for horizons-orbital-mechanics' next version: A Plan Draws\n"
     b"    a Path Only Around the Sun says the orrery's drawing leaves out\n"
     b"    the website's last-day pair; since this patch it draws it for a\n"
     b"    path that has ended. And v3.127's obligation is still open: this\n"
     b"    session read the skills as the repository's files, not as the\n"
     b"    account's installed copies.\n"
     b"**Gap (replaces the one below, 2026-11-06):** Tony's look at Pioneer 10\n"
     b'and Galileo, Sun-centred, in a plot and an animation: each marker at\n'
     b'the end of its line, the hover giving the last day. Then\n'
     b'`python test_path_drawing.py --galileo` on his machine, and close.\n'
     b'**Gap (superseded above, 2026-11-06; replaced the one below, 2026-11-05, evening):** the next small\n'),
    ('L-476: date stamp',
     b'<!-- L:476 status:OPEN upd:2026-11-05 section:A flag: rice: -->',

     b'<!-- L:476 status:OPEN upd:2026-11-06 section:A flag: rice: -->'),
    ("L-423: the live check's list, read from the config",
     b'**Gap:** items 1 and 2 done; next, item 3, L-357 (stale leftovers).\n',

     b"- **2026-11-06: the live check's positions files come from the\n"
     b'  config** (the coordinating session of Nov 6, Claude Opus 5.5, built\n'
     b"  on gallery 8ff3e74; the website's\n"
     b'  `patch_L423_positions_from_config.py`). Not one of the seven items\n'
     b"  above; Tony's job of Nov 6, item a.\n"
     b'  - Why: the live check (`gallery_maintenance_run.py --live`, its row\n'
     b'    "Served reachability") typed its positions files. It still named\n'
     b"    piece C of C/2025 K1's, unserved since piece C became an orbit on\n"
     b'    Nov 4, so Nov 5\'s live run reported a false "not served". And it\n'
     b"    left out all seven ended missions' files.\n"
     b'  - Now `positions_files()` reads them from `data/objects_config.json`\n'
     b"    by the cache builder's own `is_path_body()`: every spacecraft and\n"
     b'    every comet on an open path. Today that is 32 files, 19 spacecraft\n'
     b'    and 13 comets, and the page asks the same question before it draws\n'
     b'    (`solarSystemPositionFiles`). A config that cannot give the list\n'
     b'    turns the check red, saying why, and nothing is fetched.\n'
     b'  - The new gating row "Served list" (`tools/test_served_list.py`):\n'
     b'    the real list, each file in the served cache; no positions file\n'
     b'    typed; five planted faults, each caught (Halley marked open_path\n'
     b'    joins, 3I/ATLAS without it leaves, a config with no path body and\n'
     b"    one that is not JSON turn the check red, a 404 on Pioneer 10's file\n"
     b'    fails naming it). Shown failing when the runner was broken two\n'
     b"    ways on a copy. The orrery's dashboard gains its button and line\n"
     b"    (in the orrery's patch), which the dashboard parity check requires.\n"
     b'  - Verified in a throwaway copy: the website\'s offline run "37 of 37\n'
     b'    gating checkers passed". Its five pulls could not reach GitHub\n'
     b"    from the session's workspace, and the live site could not be\n"
     b"    reached either, so the live run is Tony's after the push.\n"
     b"  - Carried for interactive-exhibit's next version: One check reads\n"
     b'    the file the browser fetches says a new file the page fetches by\n'
     b'    name joins `SERVED_FILES` in the same push. For a positions file\n'
     b'    that is no longer so; and its count, "eleven files as of\n'
     b'    d9d7a48f", is stale.\n'
     b'**Gap:** items 1 and 2 done; next, item 3, L-357 (stale leftovers). The\n'
     b'live check\'s list: Tony\'s live run after the push, its "Served\n'
     b'reachability" line naming 32 positions files read from the config.\n'),
    ('L-423: date stamp',
     b'<!-- L:423 status:OPEN upd:2026-10-29 section:A flag: rice: -->',

     b'<!-- L:423 status:OPEN upd:2026-11-06 section:A flag: rice: -->'),
]

PAGE_EDITS = [
    ("the page's header",
     b'Last updated: November 5, 2026, evening: the Code session (Opus) for the ended missions.\n'
     b"- Written at orrery fb0a8dce and gallery 3660993, plus this session's edits (not pushed).\n",

     b'Last updated: November 6, 2026, afternoon: the coordinating session (Opus), two quick fixes.\n'
     b"- Written at orrery 01b2120 and gallery 8ff3e74, plus this session's two patches.\n"),
    ("the page's box",
     b'> **Changed since you last read this:**\n'
     b'> - Five more ended missions are built: Pioneer 10 and 11, Rosetta,\n'
     b'>   DART, and Akatsuki cut on 26 April 2024, as you ruled. Not pushed.\n'
     b"> - An orbiter's loops around a planet are no longer passes of the Sun.\n"
     b'>\n'
     b'> **Do next:** *steps 2 to 5 below; steps 2 to 4 in one sitting,\n'
     b"> before 08:17 UTC, or the website's night stops at its mirror.*\n"
     b'>\n'
     b'> **Needs you now:**\n'
     b'> - *1. Done: you approved the words file (Nov 5, evening).*\n'
     b"> - *2. (do) Commit and push the orrery, not during the website's night.*\n"
     b"> - *3. (do) The website's Daily Run, from the dashboard: last lines all\n"
     b'>   green, the swap log\'s last build "ok". Red: stop, paste me the lines.*\n'
     b"> - *4. (do) Only then commit and push the website's whole change list.*\n"
     b'> - *5. (do) Phone look: the five ticked from Historical missions.*\n',

     b'> **Changed since you last read this:**\n'
     b"> - The website's live check reads its 32 positions files from the config.\n"
     b"> - The desktop puts an ended mission's marker on its last day, and\n"
     b'>   its line now ends there (your ruling). Both are patches, not run.\n'
     b'>\n'
     b'> **Do next:** *steps 1 to 5 below, in order.*\n'
     b'>\n'
     b'> **Needs you now:**\n'
     b'> - *1. (do) Website: run `patch_L423_positions_from_config.py`, then\n'
     b'>   tools/test_served_list.py: "SERVED LIST: all 7 checks passed".*\n'
     b'> - *2. (do) Orrery: run `patch_L476_4_ended_markers.py`, then the\n'
     b'>   maintenance run from the dashboard: all gating checkers passed.*\n'
     b'> - *3. (do) Look: Pioneer 10 and Galileo, Sun-centred, plot and animation.*\n'
     b"> - *4. (do) Commit and push both, not during the website's night.*\n"
     b"> - *5. (do) After the push, the website's live run: 32 positions files.*\n"),
    ('the road: stage 13',
     b' 13.   [NOW]   *Quick wins:* the e rule, done (L-510 (the typed fields));\n'
     b'               five ended missions, built, waiting for your words and push\n'
     b"               (L-507 (historical missions)); then the desktop's ended\n"
     b'               markers (L-476 (the paths by the plan)). << moved this session\n',

     b" 13.   [NOW]   *Quick wins:* the desktop's ended markers (L-476 (the paths\n"
     b"               by the plan)) and the live check's list (L-423 (the\n"
     b"               website's checks)), built, for your look and push. << moved this session\n"),
    ("Settled: the last-day pair, Tony's ruling of today",
     b'## Settled  **>> UPDATED THIS SESSION**\n'
     b'\n'
     b'Standing rulings; a line leaves once it is habit, or a skill carries it.\n',

     b'## Settled  **>> UPDATED THIS SESSION**\n'
     b'\n'
     b'Standing rulings; a line leaves once it is habit, or a skill carries it.\n'
     b"- An ended mission's line ends at its marker on its last day, desktop as website (Nov 6).\n"),
    ('Deferred: its mark cleared',
     b'## Deferred  **>> UPDATED THIS SESSION**\n',

     b'## Deferred\n'),
    ('Signals: the cache build',
     b'- Last cache build: 20261105T200309Z, ok, no retry (gallery swap log, Nov 5).\n',

     b'- Last cache build: 20261106T155752Z, ok, no retry (gallery swap log at 8ff3e74).\n'),
    ('Signals: Tier-1',
     b'- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, generated Nov 5).\n',

     b'- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, tested copy, Nov 6).\n'),
    ('Signals: the dates',
     b"- This page's date and the ledger's newest stamp: both Nov 5. Agree.\n",

     b"- This page's date and the ledger's newest stamp: both Nov 6. Agree.\n"),
    ('Where the details are: this session',
     b'- This session: `WORDS_L507_more_voyages_20261105.md` and the brief\n'
     b'  `COORD_L507_historical_missions_more_voyages_brief_20261105.md`.\n',

     b"- This session: the website's `patch_L423_positions_from_config.py`\n"
     b"  and the orrery's `patch_L476_4_ended_markers.py`.\n"),

]


def plan_code(name):
    """(ok, bytes or None): the code file with its edits, None if already
    applied."""
    path = os.path.join(ROOT, name)
    if not os.path.isfile(path):
        print("ERROR: %s not found next to this patch. Save the patch in "
              "the orrery's root folder. NOTHING was written." % name)
        return False, None
    raw = open(path, "rb").read()
    text = raw.replace(b"\r\n", b"\n")
    got = hashlib.md5(text).hexdigest()
    if got == EXPECT_AFTER[name]:
        print("already there, identical: %s" % name)
        return True, None
    if got != EXPECT[name]:
        print("ERROR: %s is not the file this patch was built on (orrery "
              "01b2120). Its content differs: pull origin in GitHub "
              "Desktop, or discard local edits to it, and run again. "
              "NOTHING was written." % name)
        return False, None
    for label, old, new in EDITS[name]:
        n = text.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s, %s: expected 1 match, found %d. "
                  "NOTHING was written." % (name, label, n))
            return False, None
        text = text.replace(old, new)
        print("ok  %s: %s" % (name, label))
    if b"\r\n" in raw:
        print("note: %s was CRLF in the working copy; written LF" % name)
    return True, text


def plan_record(path, edits, top_only=False):
    """(ok, bytes or None): a record with its edits, checked only at the
    text each edit replaces; None if every edit is already there."""
    if not os.path.isfile(os.path.join(ROOT, path)):
        print("ERROR: %s not found. NOTHING was written." % path)
        return False, None
    raw = open(os.path.join(ROOT, path), "rb").read()
    text = raw.replace(b"\r\n", b"\n")
    if top_only:
        if text.count(MARKER) != 1:
            print("ERROR: the run-record marker is not on %s once. NOTHING "
                  "was written." % path)
            return False, None
        top, marker, bottom = text.partition(MARKER)
    else:
        top, marker, bottom = text, b"", b""
    if all(top.count(new) == 1 for _, _, new in edits):
        print("already there, identical: %s" % path)
        return True, None
    for label, old, new in edits:
        n = top.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s, %s: expected its text once, found %d. "
                  "NOTHING was written." % (path, label, n))
            return False, None
        top = top.replace(old, new)
        print("ok  %s: %s" % (path, label))
    if top_only and top.count(b"\n") > 130:
        print("ERROR: %s would stand over 130 lines above its marker. "
              "NOTHING was written." % path)
        return False, None
    return True, top + marker + bottom


def main():
    if os.path.basename(ROOT).lower() == "documentation":
        print("ERROR: run this from the orrery's root folder, not "
              "documentation\\. NOTHING was written.")
        return 1
    if not os.path.isfile(os.path.join(WEBSITE, "tools",
                                       "test_served_list.py")):
        print("ERROR: the website's folder has no tools\\test_served_list.py "
              "yet. Run the website's patch_L423_positions_from_config.py "
              "first: this patch's dashboard button names that check. "
              "NOTHING was written.")
        return 1
    planned = []
    for name in ORDER:
        ok, data = plan_code(name)
        if not ok:
            return 1
        planned.append((name, data, len(EDITS[name])))
    for path, edits, top_only in ((LEDGER, LEDGER_EDITS, False),
                                  (PAGE, PAGE_EDITS, True)):
        ok, data = plan_record(path, edits, top_only)
        if not ok:
            return 1
        planned.append((path, data, len(edits)))
    for name, data, _ in planned:
        if data is not None and any(c > 127 for c in data):
            print("ERROR: %s would hold a non-ASCII byte. NOTHING was "
                  "written." % name)
            return 1
    wrote = False
    for name, data, n in planned:
        if data is None:
            continue
        with open(os.path.join(ROOT, name), "wb") as handle:
            handle.write(data)
        wrote = True
        print("ok %s (%d edits)" % (name, n))
    print("stamps updated: path_drawing.py, test_path_drawing.py, "
          "palomas_orrery.py and palomas_orrery_dashboard.py (Module "
          "updated lines); the ledger's two date stamps; the page's header")
    for script, lines in (("ledger_index.py", 4),
                          ("test_path_drawing.py", 1),
                          ("test_dashboard_parity.py", 1)):
        print("Running %s ..." % script)
        r = subprocess.run([sys.executable, script], cwd=ROOT,
                           capture_output=True, text=True)
        for line in (r.stdout + r.stderr).strip().splitlines()[-lines:]:
            print("  " + line)
        if r.returncode != 0:
            print("ERROR: %s exited %d. The edits above are written; "
                  "Discard Changes in GitHub Desktop undoes them. Paste "
                  "these lines to the session." % (script, r.returncode))
            return 1
    print("patch applied" if wrote else "Nothing to do: already applied.")
    print("")
    print("Do next, in order:")
    print("  1. Run the maintenance run from the dashboard and read its last")
    print("     lines: all gating checkers passed, 0 TIER-1 on the gate path.")
    print("  2. Run palomas_orrery.py, tick Pioneer 10 and Galileo, centre")
    print("     on the Sun, today's date, and Plot. Each marker sits at the")
    print("     end of its line, and its hover says 'Position at:' its last")
    print("     day (2003-01-23 and 2003-09-21). Then an animation across")
    print("     2003 by year: after its last day each marker stays put.")
    print("  3. Move this patch into documentation\\, then commit and push")
    print("     the orrery and the website, not during the website's night.")
    print("Not changed, and named: skills/horizons-orbital-mechanics/"
          "SKILL.md still says the drawing leaves out the last-day pair;")
    print("carried on L-476 for its next version.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
