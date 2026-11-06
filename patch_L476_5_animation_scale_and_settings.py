"""
patch_L476_5_animation_scale_and_settings.py -- L-476 (the orrery plots
by the path plan), after Tony's look of Nov 6: the animation's Auto
scale counts a spacecraft, and a settings box that cannot be read is
named instead of a silent stop. With the records: L-476 and Where We Are.

Built on orrery d9db3400113bcaf2dac2c2fd4b3be4018509f4b2 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 6c93d0a at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read live
on Nov 6, 2026. Written by the coordinating session of Nov 6 (Claude
Opus 5.5), on Tony's "yes, please" of 15:23 Chicago.

WHY

    Tony's animation of Pioneer 10, Galileo and Jupiter opened at 6.5 AU
    with Pioneer 10 at 76 to 82 AU outside the view; he set 100 AU by
    hand. The animation sized its view from orbits alone, so a body with
    no orbit never counted; the still plot counts its marker. And his
    first try stopped with "invalid literal for int()" in the status
    line, nothing on the console and the progress bar running, so it
    looked hung.

WHAT IT CHANGES (three files, all or nothing)

    palomas_orrery.py    farthest_frame_positions, new: each body with no
                         orbital elements, its farthest frame position;
                         get_animation_axis_range takes it, and the
                         animation passes it. get_interval_settings names
                         a box it cannot read and what it holds; the
                         animation says so on the console, stops its
                         progress bar, and reads its number of steps the
                         same way; the still plot says so on the console.
                         Stamp.
    LEDGER_CONSOLIDATED.md  L-476: Tony's look, the two fixes, a new Gap.
                         Then it runs ledger_index.py.
    documentation/WHERE_WE_ARE.md  by section; nothing below the
                         run-record marker.

    The permanent part is the new function and the edits that call it
    and name the boxes. The script itself is one-shot.

RUN COMMAND

    Save this file in the orrery's root folder
    (C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\),
    open it in VS Code and click Run.
    (python patch_L476_5_animation_scale_and_settings.py)

    Success: one "ok" line per edit, then the checks' last lines, then
    "patch applied". Failure: one ERROR or ANCHOR FAIL line, and nothing
    is written. Undo is Discard Changes in GitHub Desktop.

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

ORDER = ['palomas_orrery.py']
EXPECT = {'palomas_orrery.py': '856fc20096b931dd670b25136ce6a6da'}
EXPECT_AFTER = {'palomas_orrery.py': 'deb2a2e17c9a08da2dab1fda8ba85e97'}

EDITS = {name: [] for name in ORDER}
EDITS['palomas_orrery.py'].append(('get_interval_settings names the box',
     b'        # Get values from GUI based on object types\n'
     b'        settings = {\n'
     b"            'trajectory_points': float(trajectory_points_entry.get()),\n"
     b"            'orbital_points': float(orbital_points_entry.get()),\n"
     b"            'satellite_days': int(satellite_days_entry.get()),\n"
     b"            'satellite_points': float(satellite_points_entry.get()),\n"
     b"            'start_date': get_date_from_gui(),\n"
     b"            'end_date': get_end_date_from_gui(),\n"
     b"            'days_to_plot': int(days_to_plot_entry.get())\n"
     b'        }\n',

     b'        # Get values from GUI based on object types\n'
     b'        # L-476 (2026-11-06): a box that cannot be read is named, with what\n'
     b'        # it holds, instead of Python\'s "invalid literal for int()".\n'
     b'        def _read(entry, box, kind):\n'
     b'            text = entry.get()\n'
     b'            try:\n'
     b'                return kind(text)\n'
     b'            except ValueError:\n'
     b'                raise ValueError(\'the "%s" box holds "%s", which is not %s\'\n'
     b'                                 % (box, text, "a whole number" if kind is int\n'
     b'                                    else "a number"))\n'
     b'        settings = {\n'
     b'            \'trajectory_points\': _read(trajectory_points_entry, "Trajectory objects", float),\n'
     b'            \'orbital_points\': _read(orbital_points_entry, "Orbital objects", float),\n'
     b'            \'satellite_days\': _read(satellite_days_entry, "Satellite cache span (days)", int),\n'
     b'            \'satellite_points\': _read(satellite_points_entry, "Satellite objects", float),\n'
     b"            'start_date': get_date_from_gui(),\n"
     b"            'end_date': get_end_date_from_gui(),\n"
     b'            \'days_to_plot\': _read(days_to_plot_entry, "Days", int)\n'
     b'        }\n'))
EDITS['palomas_orrery.py'].append(('the still plot says it on the console',
     b'            settings, error_msg = get_interval_settings()\n'
     b'            if error_msg:\n'
     b'                output_label.config(text=error_msg)\n'
     b'            \n',

     b'            settings, error_msg = get_interval_settings()\n'
     b'            if error_msg:\n'
     b'                print(f"[PLOT] {error_msg}", flush=True)   # L-476 (2026-11-06)\n'
     b'                output_label.config(text=error_msg)\n'
     b'            \n'))
EDITS['palomas_orrery.py'].append(('the animation says it, and stops its bar',
     b'            # Get frames number and validate\n'
     b'            N_str = num_frames_entry.get()\n'
     b'            if not N_str.strip():\n'
     b'                output_label.config(text="Please enter a valid number of frames.")\n'
     b'                return\n'
     b'            N = int(N_str)\n',

     b'            # Get frames number and validate\n'
     b'            N_str = num_frames_entry.get()\n'
     b'            if not N_str.strip():\n'
     b'                output_label.config(text="Please enter a valid number of frames.")\n'
     b'                root.after(0, lambda: progress_bar.stop())   # L-476 (2026-11-06)\n'
     b'                return\n'
     b'            # L-476 (2026-11-06): the box is named on the console and in the\n'
     b'            # status line, and the progress bar stops, so a box that cannot\n'
     b'            # be read no longer looks like a hang.\n'
     b'            try:\n'
     b'                N = int(N_str)\n'
     b'            except ValueError:\n'
     b'                _msg = (\'The number of steps to animate holds "%s", which is not \'\n'
     b"                        'a whole number.' % N_str)\n"
     b'                print(f"[ANIMATION] Not started: {_msg}", flush=True)\n'
     b'                output_label.config(text=_msg)\n'
     b'                root.after(0, lambda: progress_bar.stop())\n'
     b'                return\n'))
EDITS['palomas_orrery.py'].append(("the animation's settings stop is said",
     b'            # Get interval settings\n'
     b'            settings, error_msg = get_interval_settings()\n'
     b'            if error_msg:\n'
     b'                output_label.config(text=error_msg)\n'
     b'                return\n',

     b'            # Get interval settings\n'
     b'            settings, error_msg = get_interval_settings()\n'
     b'            if error_msg:\n'
     b'                # L-476 (2026-11-06): it stopped here silently, the progress\n'
     b"                # bar still running; Tony's run of Nov 6 looked hung.\n"
     b'                print(f"[ANIMATION] Not started: {error_msg}", flush=True)\n'
     b'                output_label.config(text=error_msg)\n'
     b'                root.after(0, lambda: progress_bar.stop())\n'
     b'                return\n'))
EDITS['palomas_orrery.py'].append(('get_animation_axis_range takes positions',
     b'def get_animation_axis_range(scale_var, custom_scale_entry, objects, planetary_params, parent_planets, center_object_name,\n'
     b'                             none_if_empty=False):\n'
     b'    """\n'
     b'    Get axis range for animations using the same logic as static plots.\n'
     b'    This ensures consistency between plot_objects() and animate_objects().\n'
     b'    none_if_empty (L-385): passed through; None when nothing orbits.\n'
     b'    """\n'
     b"    if scale_var.get() == 'Auto':\n"
     b'        # Use the same orbital-based scaling as plot_objects()\n'
     b"        selected_objects = [obj for obj in objects if obj['var'].get() == 1]\n"
     b'        \n'
     b'        return calculate_axis_range_from_orbits(\n'
     b'            selected_objects, {}, planetary_params, \n'
     b'            parent_planets, center_object_name,\n'
     b'            none_if_empty=none_if_empty\n'
     b'        )\n',

     b'def farthest_frame_positions(positions_over_time, planetary_params):\n'
     b'    """{name: the frame position farthest from the centre} for each body\n'
     b'    in an animation with no orbital elements in planetary_params -- a\n'
     b'    spacecraft, say, drawn from its positions. calculate_axis_range_from_orbits\n'
     b'    sizes such a body by its position, as the still plot does by its\n'
     b'    marker; a body with elements is sized by its orbit and is left out\n'
     b'    here, so its sizing does not change (L-476, 2026-11-06)."""\n'
     b'    out = {}\n'
     b'    for name, frames in (positions_over_time or {}).items():\n'
     b'        if name in planetary_params:\n'
     b'            continue\n'
     b'        best, best_r = None, -1.0\n'
     b'        for p in frames or []:\n'
     b"            if not p or p.get('x') is None:\n"
     b'                continue\n'
     b"            r = (p['x'] ** 2 + p['y'] ** 2 + p['z'] ** 2) ** 0.5\n"
     b'            if r > best_r:\n'
     b'                best, best_r = p, r\n'
     b'        if best is not None:\n'
     b'            out[name] = best\n'
     b'    return out\n'
     b'        \n'
     b'        \n'
     b'def get_animation_axis_range(scale_var, custom_scale_entry, objects, planetary_params, parent_planets, center_object_name,\n'
     b'                             none_if_empty=False, positions=None):\n'
     b'    """\n'
     b'    Get axis range for animations using the same logic as static plots.\n'
     b'    This ensures consistency between plot_objects() and animate_objects().\n'
     b'    none_if_empty (L-385): passed through; None when nothing orbits.\n'
     b'    positions (L-476, 2026-11-06): farthest_frame_positions, so a body\n'
     b'    with no orbit -- a spacecraft -- counts by the farthest place its\n'
     b'    marker is drawn. Before, {} was passed and a spacecraft never counted:\n'
     b"    Tony's animation of Pioneer 10 with Jupiter opened at 6.5 AU, Pioneer\n"
     b'    10 at 76 to 82 AU outside it.\n'
     b'    """\n'
     b"    if scale_var.get() == 'Auto':\n"
     b'        # Use the same orbital-based scaling as plot_objects()\n'
     b"        selected_objects = [obj for obj in objects if obj['var'].get() == 1]\n"
     b'        \n'
     b'        return calculate_axis_range_from_orbits(\n'
     b'            selected_objects, positions or {}, planetary_params,\n'
     b'            parent_planets, center_object_name,\n'
     b'            none_if_empty=none_if_empty\n'
     b'        )\n'))
EDITS['palomas_orrery.py'].append(('the animation passes its positions',
     b'                else:\n'
     b'                    axis_range = get_animation_axis_range(\n'
     b'            #            scale_var, custom_scale_entry, objects, planetary_params, \n'
     b'                        scale_var, custom_scale_entry, objects, active_planetary_params,\n'
     b'                        parent_planets, center_object_name, none_if_empty=True\n'
     b'                    )\n'
     b'            else:\n'
     b'                axis_range = get_animation_axis_range(\n'
     b'            #        scale_var, custom_scale_entry, objects, planetary_params, \n'
     b'                    scale_var, custom_scale_entry, objects, active_planetary_params,\n'
     b'                    parent_planets, center_object_name, none_if_empty=True\n'
     b'                )\n',

     b'                else:\n'
     b'                    axis_range = get_animation_axis_range(\n'
     b'            #            scale_var, custom_scale_entry, objects, planetary_params, \n'
     b'                        scale_var, custom_scale_entry, objects, active_planetary_params,\n'
     b'                        parent_planets, center_object_name, none_if_empty=True,\n'
     b'                        positions=farthest_frame_positions(positions_over_time,\n'
     b'                                                           active_planetary_params)\n'
     b'                    )\n'
     b'            else:\n'
     b'                axis_range = get_animation_axis_range(\n'
     b'            #        scale_var, custom_scale_entry, objects, planetary_params, \n'
     b'                    scale_var, custom_scale_entry, objects, active_planetary_params,\n'
     b'                    parent_planets, center_object_name, none_if_empty=True,\n'
     b'                    positions=farthest_frame_positions(positions_over_time,\n'
     b'                                                       active_planetary_params)\n'
     b'                )\n'))
EDITS['palomas_orrery.py'].append(('docstring: stamp',
     b"instead of hiding it. Pioneer 10's marker now sits at the end of its line\n"
     b'and Galileo has one.)\n',

     b"instead of hiding it. Pioneer 10's marker now sits at the end of its line\n"
     b'and Galileo has one.)\n'
     b"Module updated: November 6, 2026, afternoon, with Anthropic's Claude Opus\n"
     b"5.5 (L-476, after Tony's look): the animation's Auto scale counts a body\n"
     b'with no orbit -- a spacecraft -- by the farthest place its marker is drawn\n'
     b'(farthest_frame_positions), as the still plot counts its marker; and a\n'
     b'settings box that cannot be read is named, with what it holds, on the\n'
     b"console and in the status line, and the animation's progress bar stops,\n"
     b'where it used to stop silently.\n'))

LEDGER_EDITS = [
    ("L-476: Tony's look, the scale and the boxes, a new Gap",
     b"**Gap (replaces the one below, 2026-11-06):** Tony's look at Pioneer 10\n",

     b"- **2026-11-06, afternoon: Tony's look, and two older gaps it found**\n"
     b"  (the same coordinating session; Tony's run record\n"
     b'  `documentation/WHERE_WE_ARE_11-6-26_1010_run_record.md`; pushed at\n'
     b'  orrery d9db3400 and gallery 6c93d0a).\n'
     b'  - The plot, Pioneer 10 and Galileo centred on the Sun: "yes". The\n'
     b'    `--galileo` check on his machine: "305 drawn, 305 served", the\n'
     b'    last-day pair included, nothing drawn and not served. The animation\n'
     b'    from 2000 by year, 29 frames\n'
     b'    (`Sun_system_animation_20261106_2046_pioneer10_galileo.html`), read\n'
     b'    frame by frame: Pioneer 10 at 76.5, 79.0, 81.6 AU, then 82.1 AU\n'
     b'    dated 2003-01-23 in every later frame; Galileo held at 5.4 AU dated\n'
     b"    2003-09-21. JPL's real positions, which the session could not reach.\n"
     b"  - Older gap 1, the animation's Auto scale: it passed no positions to\n"
     b'    `calculate_axis_range_from_orbits`, so a body with no orbit -- a\n'
     b"    spacecraft -- never counted. Tony's animation with Jupiter opened at\n"
     b'    6.5 AU, Pioneer 10 outside it, and he set 100 AU by hand. The still\n'
     b"    plot counts a spacecraft's marker. Fixed in\n"
     b'    `patch_L476_5_animation_scale_and_settings.py` (Tony, Nov 6: "yes,\n'
     b'    please"): `farthest_frame_positions` gives each body with no orbital\n'
     b'    elements its farthest frame position; a body with elements is left\n'
     b'    out, so its sizing is unchanged.\n'
     b"  - Older gap 2, a settings box that cannot be read: the animation's\n"
     b'    first try of Nov 6 stopped with "invalid literal for int()" in the\n'
     b'    status line, nothing on the console and the progress bar running,\n'
     b'    so it looked hung. `get_interval_settings` read five boxes with\n'
     b'    bare int() and float(), and the animation returned silently on its\n'
     b'    error. Now the box is named with what it holds, on the console and\n'
     b'    in the status line, the progress bar stops, and the number of steps\n'
     b'    to animate is read the same way. The still plot, which carries on\n'
     b'    with defaults, now says it on the console too.\n'
     b'  - Verified in a throwaway copy, with JPL replaced by a stand-in: the\n'
     b'    same animation (Pioneer 10, Galileo, Jupiter, from 2000, 29 years)\n'
     b"    opens at +/-93.8 AU, the stand-in's 78.1 AU plus 20 percent; a Days\n"
     b'    box holding "28.5" stops the animation with \'the "Days" box holds\n'
     b'    "28.5", which is not a whole number\' on the console, and a steps\n'
     b'    box holding "2 9" likewise. Before the patch the same two inputs\n'
     b'    stopped it silently. No permanent check covers the scale or the\n'
     b"    boxes. The orrery's maintenance run on the copy: every checker\n"
     b'    passed but Horizons confirmations, red because the osculating cache\n'
     b"    pushed at d9db340 holds Earth's, Mars's and Jupiter's elements from\n"
     b"    Tony's runs of Nov 6, which JPL must confirm and the session cannot\n"
     b"    reach. The untouched d9db340 is red the same way there; on Tony's\n"
     b'    machine the Horizons check asks JPL first.\n'
     b"**Gap (replaces the one below, 2026-11-06, afternoon):** Tony's look at\n"
     b"the same animation with Auto scale (it opens on Pioneer 10's farthest\n"
     b'point plus 20 percent, about 98 AU); then close. Its loose end at the\n'
     b'close: the horizons-orbital-mechanics sentence carried above, to an open\n'
     b"item for that skill's next version.\n"
     b"**Gap (superseded above, 2026-11-06, afternoon; replaced the one below, 2026-11-06):** Tony's look at Pioneer 10\n"),
]

PAGE_EDITS = [
    ("the page's header",
     b'Last updated: November 6, 2026, afternoon: the coordinating session (Opus), two quick fixes.\n'
     b"- Written at orrery 01b2120 and gallery 8ff3e74, plus this session's two patches.\n",

     b'Last updated: November 6, 2026, late afternoon: the coordinating session (Opus), after your look.\n'
     b"- Written at orrery d9db340 and gallery 6c93d0a, plus this session's third patch.\n"),
    ("the page's box",
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
     b"> - *5. (do) After the push, the website's live run: 32 positions files.*\n",

     b'> - Both fixes are pushed and your look passed: the live check, and\n'
     b">   ended missions' markers on their last day.\n"
     b"> - The animation's Auto scale now counts spacecraft; an unreadable\n"
     b'>   settings box is named instead of a silent stop. Patch, not run.\n'
     b'>\n'
     b'> **Do next:** *steps 1 to 4 below, in order.*\n'
     b'>\n'
     b'> **Needs you now:**\n'
     b'> - *1. (do) Orrery: run `patch_L476_5_animation_scale_and_settings.py`,\n'
     b'>   then the maintenance run from the dashboard: all gating checkers passed.*\n'
     b'> - *2. (do) Look: the same animation on Auto scale: about 98 AU.*\n'
     b"> - *3. (do) Commit and push the orrery, not during the website's night.*\n"
     b'> - *4. Then L-476 (the paths by the plan) closes.*\n'),
    ('the road: stage 13',
     b" 13.   [NOW]   *Quick wins:* the desktop's ended markers (L-476 (the paths\n"
     b"               by the plan)) and the live check's list (L-423 (the\n"
     b"               website's checks)), built, for your look and push. << moved this session\n",

     b" 13.   [NOW]   *Quick wins:* the live check's list, done (L-423 (the\n"
     b"               website's checks)); the ended markers, done, and the\n"
     b"               animation's scale, for your look (L-476 (the paths by the plan)).\n"),
    ('Settled: its mark cleared',
     b'## Settled  **>> UPDATED THIS SESSION**\n',

     b'## Settled\n'),
    ('Signals: the cache build',
     b'- Last cache build: 20261106T155752Z, ok, no retry (gallery swap log at 8ff3e74).\n',

     b'- Last cache build: 20261106T192923Z, ok, no retry (gallery swap log at 6c93d0a).\n'),
    ('Signals: Tier-1',
     b'- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, tested copy, Nov 6).\n',

     b'- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md at d9db340, Nov 6).\n'),
    ('Where the details are: this session',
     b"- This session: the website's `patch_L423_positions_from_config.py`\n"
     b"  and the orrery's `patch_L476_4_ended_markers.py`.\n",

     b'- This session: your run record `WHERE_WE_ARE_11-6-26_1010_run_record.md`;\n'
     b'  the patches `patch_L423_positions_from_config.py` (website),\n'
     b'  `patch_L476_4_ended_markers.py` and `patch_L476_5_...` (orrery).\n'),

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
              "d9db340). Its content differs: pull origin in GitHub "
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
    print("stamps updated: palomas_orrery.py (Module updated line); the "
          "page's header")
    for script, lines in (("ledger_index.py", 4),
                          ("test_path_drawing.py", 1)):
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
    print("  2. Run palomas_orrery.py: Pioneer 10, Galileo and Jupiter, centre")
    print("     on the Sun, start in 2000, 29 steps, the Year animation, on")
    print("     Auto scale. It opens at about 98 AU, Pioneer 10 inside it.")
    print("  3. Move this patch into documentation\\, then commit and push the")
    print("     orrery, not during the website's night.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
