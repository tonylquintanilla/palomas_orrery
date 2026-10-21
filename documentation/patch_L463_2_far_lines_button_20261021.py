#!/usr/bin/env python3
"""
patch_L463_2_far_lines_button_20261021.py -- the dashboard button the
website's Far lines check was missing, and the ledger after Tony's phone
check: L-463 and L-464 closed, L-465 new. ORRERY folder.

Built on orrery b3c3e2a5d6d1b311c12ce160d6142cfad6fd955f at
https://github.com/tonylquintanilla/palomas_orrery, plus the close patch
(patch_L456_7_close_20261021.py) and its maintenance run, not yet
committed; gallery b334077cd17cd57dff029fd2e3e6bbea445be4aa at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 21, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L463_2_far_lines_button_20261021.py

    Save this file in the ORRERY folder above, open it in VS Code and
    click Run. It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing

    palomas_orrery_dashboard.py    a "Far Lines" button under "Gallery --
                                   checks and data", and its short line,
                                   so the Dashboard parity check passes
    LEDGER_CONSOLIDATED.md         L-463 and L-464 closed (moved to
                                   section C); L-465 new, the Sun's pole
                                   and spin on the website; L-412's Gap;
                                   the module's stamp
    documentation/WHERE_WE_ARE.md  the top box, one road line and one
                                   design-talk line; your run record below
                                   the marker is not touched
    documentation/HANDOFF_L456_addresses_build_20261021.md
                                   one paragraph in section 0

    The dashboard must be exactly the pushed version (line endings
    aside); the ledger, the page and the handoff are checked only at the
    lines this patch edits. It needs the close patch to have run first.
    Nothing is written unless every edit fits. Files are written LF. A
    second run refuses.

WHAT IT PRINTS

    Success: one "ok" line per file, then "patch applied" and what to
    do next. Failure: one ERROR or ANCHOR FAIL line and "NOTHING was
    written."

Undo is Discard Changes in GitHub Desktop.

Role: devtool
Domain: dev_tools
"""

FOLDER_WORD = "the orrery's"
NEXT = [
    "NEXT:",
    "  1. Move this script into documentation/ now, before the",
    "     maintenance run, which would otherwise list it as a module.",
    "  2. Run the orrery maintenance run (dashboard). Expect every",
    "     checker to pass, Dashboard parity included, and the gate line",
    "     0 TIER-1; it rewrites the ledger's index (L-465 new).",
    "  3. Commit and push the orrery. This commit also carries the close",
    "     patch's changes, which were not in the last push (b3c3e2a5).",
]

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

FILES = [
    {'path': 'palomas_orrery_dashboard.py', 'mode': 'edit', 'base_md5': 'de327ffd9c305fc1b2e3d7d84c8541a6', 'new_md5': '5791b50d52ec367b9cbb7ac176325ea8', 'zone': None, 'edits': [('        ("Feature Renderers",\n        os.path.join("documentation", "run_offline_check.py"),', '        ("Far Lines",\n        os.path.join("documentation", "run_offline_check.py"),\n        "A drawn line that reaches far past the view is cut to the view\'s "\n        "edge before a phone draws it (L-463). The Galactic Plane\'s ring "\n        "and pole line, at 100,000 AU, drew as a wide pink band on Tony\'s "\n        "phone whenever the Sun room was zoomed in close. It works six "\n        "cases by hand, builds the Sun room from the served config and "\n        "names the lines it looks after, and checks every drawn point "\n        "lies inside the box. It breaks its own file three ways first, to "\n        "show it can fail. GATES the gallery runner. The check is Node, so "\n        "this button runs it through documentation/run_offline_check.py. "\n        "Runs from the gallery repo ROOT.",\n        GALLERY_REPO_DIR,\n        True,\n        ["Far lines"],\n        True),\n        ("Feature Renderers",\n        os.path.join("documentation", "run_offline_check.py"),'), ('    ("Gallery -- checks and data",\n     "Feature Renderers"):', '    ("Gallery -- checks and data",\n     "Far Lines"):\n        "Checks lines far past the view are cut to its edge.",\n    ("Gallery -- checks and data",\n     "Feature Renderers"):')]},
    {'path': 'LEDGER_CONSOLIDATED.md', 'mode': 'edit', 'anchors_only': True, 'zone': ('<!-- INDEX:START', '<!-- INDEX:END -->'), 'edits': [('L-458 and L-411), built on 5102188c and gallery 1dd25994.\n', "L-458 and L-411), built on 5102188c and gallery 1dd25994.\nModule updated: October 21, 2026, evening, with Anthropic's Claude Opus\n5.5 (L-463 and L-464 closed on Tony's phone; L-465 new, the Sun's pole\nand spin drawn on the website; the Far lines dashboard button), built\non b3c3e2a5 and gallery b334077c.\n"), ('#### [L-464] The Sun room\'s own row: no info link, and the pole\'s citation has nowhere to show (gallery, interactive)\n<!-- L:464 status:OPEN upd:2026-10-21 section:A flag: rice: -->\n- **Tony, 2026-10-21,** at his phone look after L-456\'s addresses were\n  pushed (orrery 5102188c, gallery 1dd25994; run record\n  `documentation/WHERE_WE_ARE_10-21-26_1217_run_record.md`): "also i do not see the sun\'s\n  pole. and the sun drawerer does not have a link, either nasa or\n  wikipedia."\n- **Read the same day on the served site, not yet traced in code:** the\n  Sun\'s own drawer row (the centre body, legend group "center") opens\n  an i panel reading "No link on file for this shell.", though the\n  Sun\'s entry in `data/objects_config.json` carries `info_url`\n  https://science.nasa.gov/sun/. The panel code\'s own comment says\n  every shell in the Sun and Earth rooms has a link; the centre row is\n  the one it missed.\n- The Sun\'s pole is served with its re-homed citation (NASA NAIF\'s\n  pck00011.tpc; gallery `patch_L456_6_sun_pole_website_20261021.py`),\n  but no row or panel was found that shows it to a visitor.\n- Not caused by the address build: between gallery 30db99f and 1dd25994\n  only citation text changed in the served config.\n- **Found and fixed the same day** (gallery\n  `patch_L463_1_sun_room_fixes_20261021.py`): the Sun room never gave\n  the assembler\'s centre marker any words, while the Solar System room\n  gives the same marker the Sun\'s description and link. The Sun room\n  now gives it the Sun\'s description and NASA link from the orrery\'s\n  object list and, as its source, the pole\'s citation, which turns the\n  room\'s drawings but had no row of its own. All three are served\n  words; the Typed facts check passes. In a headless run every one of\n  the Sun room\'s 19 rows now has a link and a source. Earth\'s room has\n  no centre row: its pole has its own row, Rotation Axis and Equator,\n  with a link and a source.\n**Gap:** Tony\'s phone, after the push: the Sun\'s own row shows NASA\'s\nlink and the pole\'s source. Then this item closes.\n**Ref:** gallery `interactive.html`, `data/objects_config.json`,\n`gallery/source_list.js`; interactive-exhibit; L-456; L-412.\n\n#### [L-463] A pink band or sheet across the Sun room on Tony\'s phone (gallery, rendering)\n<!-- L:463 status:OPEN upd:2026-10-21 section:A flag: rice: -->\n- **Tony, 2026-10-21,** the same look: "there are a number of issues,\n  there is a pink band that appears in various views." Three\n  screenshots from his phone, 13:25 to 13:27, sent in chat and not\n  saved: at the 0.1 AU grid, a pale pink sheet across most of the\n  view, edged in purple; at the 50 AU grid with the Heliopause\n  selected, a pink band crossing the view diagonally through the Sun.\n- **Read the same day, not yet reproduced:** a fresh load of the Sun\n  room in a desktop browser drew no band. The room\'s code draws no\n  filled surfaces (no mesh3d, no surfaceaxis in gallery `gallery/` or\n  `interactive.html`). The band\'s purple edge is the colour of the\n  Galactic Plane ring, rgb(175, 135, 235), a line of 181 points: a\n  guess, not a finding, that the phone draws that ring filled.\n- Not caused by the address build: only citation text changed in the\n  served config that day.\n- **Cause confirmed, 2026-10-21, 14:03, Tony\'s test on his phone:** with\n  the Galactic Plane ticked, Go To on the Corona brought the band back\n  (a fifth screenshot, at the 0.02 AU grid). At the 50,000 AU grid the\n  same rows drew cleanly. So the band is the Galactic Plane\'s ring and\n  pole line, at 100,000 AU, drawn by the phone when the view is close\n  in: hundreds to millions of times past the view\'s edge.\n- **Fix built the same day:** gallery\n  `patch_L463_1_sun_room_fixes_20261021.py`. The page cuts any line\n  reaching more than 20 times past the view to the view\'s edge before\n  it is drawn, and again at every frame change (`gallery/far_lines.js`);\n  a desktop sees no change, because gl-plot3d already hid that part.\n  The point count never changes, so per-point hover text stays lined\n  up. Checked: the new gating check "Far lines"\n  (`documentation/smoke_far_lines.js`, its self-test breaking the file\n  three ways first); every other website check passing; a headless\n  walk of the Sun room (the Galactic Plane ticked, then Go To on the\n  Corona: its lines reach 0.102 AU, the view\'s edge, where before they\n  reached 100,000 AU); and every room\'s drawer behaving exactly as\n  before (`tools/headless/compare_rooms.js`, the Sun, Earth and Solar\n  System rooms). Not yet seen on the phone.\n**Gap:** Tony\'s phone, after the push: the Galactic Plane ticked, Go To\non the Corona, no band. Then this item closes.\n**Ref:** gallery `gallery/feature_renderers.js`, `interactive.html`;\nL-412; L-460.\n\n', '#### [L-465] The Sun room draws the Sun\'s pole and its direction of spin, as the orrery does (gallery, the Sun room)\n<!-- L:465 status:OPEN upd:2026-10-21 section:A flag: rice: -->\n- **Tony, 2026-10-21,** in his run record after the Sun\'s own row was\n  fixed (`documentation/WHERE_WE_ARE_10-21-26_1217_run_record.md`): "can we show the\n  pole and the sun\'s rotational direction like the orrery?"\n- **What the orrery draws, read at orrery b3c3e2a5:**\n  `build_rotation_axis_traces` in `planet_visualization_utilities.py`\n  draws a centre body\'s spin-pole line, a curved arrow for the direction\n  of spin and one info marker, from the same pole matrix that turns the\n  streamer belt. Its hover gives the sidereal rotation period, the\n  direction (prograde) and the tilt; for the Sun those are typed strings\n  in that file ("25.38 d sidereal", "7.25 deg to ecliptic"), sourced in\n  its comments, not rows in `constants_new.py`.\n- **What the website has:** the Sun\'s pole is served (`orientation`, NASA\n  NAIF\'s pck00011.tpc) and turns the room\'s drawings, and since L-464\n  its citation shows on the Sun\'s own row; nothing draws the axis. The\n  Earth room\'s axis is its own drawer row, Rotation Axis and Equator,\n  which is the website\'s existing form for this.\n**Gap:** a design talk: the row and what it draws; the numbers its hover\nprints, which need rows in the store with sources before the website may\nprint them (the period and the tilt); the hover\'s words to Tony before\nthey ship. Then the build, in the Sun\'s slice (L-412).\n**Ref:** orrery `planet_visualization_utilities.py`; gallery\n`gallery/earth_geometry.js` (Earth\'s axis row), `interactive.html`;\nL-464; L-412.\n\n'), ('## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)\n\n', '## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)\n\n#### [L-464] The Sun room\'s own row: no info link, and the pole\'s citation has nowhere to show (gallery, interactive, DONE 2026-10-21)\n<!-- L:464 status:DONE upd:2026-10-21 section:C flag: rice: -->\n- **Tony, 2026-10-21,** at his phone look after L-456\'s addresses were\n  pushed (orrery 5102188c, gallery 1dd25994; run record\n  `documentation/WHERE_WE_ARE_10-21-26_1217_run_record.md`): "also i do not see the sun\'s\n  pole. and the sun drawerer does not have a link, either nasa or\n  wikipedia."\n- **Read the same day on the served site, not yet traced in code:** the\n  Sun\'s own drawer row (the centre body, legend group "center") opens\n  an i panel reading "No link on file for this shell.", though the\n  Sun\'s entry in `data/objects_config.json` carries `info_url`\n  https://science.nasa.gov/sun/. The panel code\'s own comment says\n  every shell in the Sun and Earth rooms has a link; the centre row is\n  the one it missed.\n- The Sun\'s pole is served with its re-homed citation (NASA NAIF\'s\n  pck00011.tpc; gallery `patch_L456_6_sun_pole_website_20261021.py`),\n  but no row or panel was found that shows it to a visitor.\n- Not caused by the address build: between gallery 30db99f and 1dd25994\n  only citation text changed in the served config.\n- **Found and fixed the same day** (gallery\n  `patch_L463_1_sun_room_fixes_20261021.py`): the Sun room never gave\n  the assembler\'s centre marker any words, while the Solar System room\n  gives the same marker the Sun\'s description and link. The Sun room\n  now gives it the Sun\'s description and NASA link from the orrery\'s\n  object list and, as its source, the pole\'s citation, which turns the\n  room\'s drawings but had no row of its own. All three are served\n  words; the Typed facts check passes. In a headless run every one of\n  the Sun room\'s 19 rows now has a link and a source. Earth\'s room has\n  no centre row: its pole has its own row, Rotation Axis and Equator,\n  with a link and a source.\n- **Closed 2026-10-21** on Tony\'s phone, after gallery b334077c was\n  pushed and its live run passed: the Sun\'s own row shows NASA\'s link\n  and the pole\'s source, NASA NAIF (run record\n  `documentation/WHERE_WE_ARE_10-21-26_1217_run_record.md`: "correct. thanks."). His\n  next question, the pole and the spin drawn as the orrery draws them,\n  is L-465.\n**Gap:** none.\n**Ref:** gallery `interactive.html`, `data/objects_config.json`,\n`gallery/source_list.js`; interactive-exhibit; L-456; L-412.\n\n#### [L-463] A pink band or sheet across the Sun room on Tony\'s phone (gallery, rendering, DONE 2026-10-21)\n<!-- L:463 status:DONE upd:2026-10-21 section:C flag: rice: -->\n- **Tony, 2026-10-21,** the same look: "there are a number of issues,\n  there is a pink band that appears in various views." Three\n  screenshots from his phone, 13:25 to 13:27, sent in chat and not\n  saved: at the 0.1 AU grid, a pale pink sheet across most of the\n  view, edged in purple; at the 50 AU grid with the Heliopause\n  selected, a pink band crossing the view diagonally through the Sun.\n- **Read the same day, not yet reproduced:** a fresh load of the Sun\n  room in a desktop browser drew no band. The room\'s code draws no\n  filled surfaces (no mesh3d, no surfaceaxis in gallery `gallery/` or\n  `interactive.html`). The band\'s purple edge is the colour of the\n  Galactic Plane ring, rgb(175, 135, 235), a line of 181 points: a\n  guess, not a finding, that the phone draws that ring filled.\n- Not caused by the address build: only citation text changed in the\n  served config that day.\n- **Cause confirmed, 2026-10-21, 14:03, Tony\'s test on his phone:** with\n  the Galactic Plane ticked, Go To on the Corona brought the band back\n  (a fifth screenshot, at the 0.02 AU grid). At the 50,000 AU grid the\n  same rows drew cleanly. So the band is the Galactic Plane\'s ring and\n  pole line, at 100,000 AU, drawn by the phone when the view is close\n  in: hundreds to millions of times past the view\'s edge.\n- **Fix built the same day:** gallery\n  `patch_L463_1_sun_room_fixes_20261021.py`. The page cuts any line\n  reaching more than 20 times past the view to the view\'s edge before\n  it is drawn, and again at every frame change (`gallery/far_lines.js`);\n  a desktop sees no change, because gl-plot3d already hid that part.\n  The point count never changes, so per-point hover text stays lined\n  up. Checked: the new gating check "Far lines"\n  (`documentation/smoke_far_lines.js`, its self-test breaking the file\n  three ways first); every other website check passing; a headless\n  walk of the Sun room (the Galactic Plane ticked, then Go To on the\n  Corona: its lines reach 0.102 AU, the view\'s edge, where before they\n  reached 100,000 AU); and every room\'s drawer behaving exactly as\n  before (`tools/headless/compare_rooms.js`, the Sun, Earth and Solar\n  System rooms). Not yet seen on the phone.\n- **Closed 2026-10-21** on Tony\'s phone, after gallery b334077c was\n  pushed: the Galactic Plane ticked, Go To on the Corona, no band (run\n  record `documentation/WHERE_WE_ARE_10-21-26_1217_run_record.md`: "correct.\n  thanks."). The live run served `gallery/far_lines.js` matching the\n  working copy.\n- **Missed in the build, caught by its check:** the website patch added\n  the "Far lines" step to the gallery run without its dashboard\n  button. The orrery run\'s Dashboard parity check failed on it, by name\n  ("gallery step \\"Far lines\\" ... has no button"), and Tony noted it;\n  `patch_L463_2_far_lines_button_20261021.py` adds the button. The\n  rule is L-416\'s: every run step has a button.\n**Gap:** none.\n**Ref:** gallery `gallery/feature_renderers.js`, `interactive.html`;\nL-412; L-460.\n\n'), ("for Tony's word):** the Sun room's phone findings, fixed the same day\nand waiting on his phone (L-463, L-464); then the drawer order\n", "for Tony's word):** the drawer order\n")]},
    {'path': 'documentation/WHERE_WE_ARE.md', 'mode': 'edit', 'anchors_only': True, 'zone': None, 'edits': [("Last updated: October 21, 2026, afternoon: the links are live; the Sun room's phone problems fixed, to check.\n- Written at orrery 5102188 and gallery 1dd2599.\n", "Last updated: October 21, 2026, evening: the Sun room's three phone problems fixed and checked.\n- Written at orrery b3c3e2a and gallery b334077.\n"), ("> - Your phone's three Sun-room problems: cause found, fixes built\n>   (L-463 (pink band), L-464 (the Sun's own row and pole)).\n", "> - The pink band and the Sun's own row: fixed, checked on your phone.\n"), ('> **Do next:** *website: patch_L463_1, its run, push, then your phone;\n> orrery: this close patch, the maintenance run, commit, push.*\n', "> **Do next:** *orrery: patch_L463_2, the maintenance run, commit AND\n> push (the close patch's changes go with it: not in the last push).*\n"), ("               list, addresses (Oct 18-21); the phone's three\n               problems fixed (L-463, L-464); now the drawer order\n", "               list, addresses, the phone's three problems (Oct\n               18-21); now the drawer order\n"), ('- The Daily Run checking the orrery it pulled is the one you pushed\n  (L-461 (pull matches push)).\n', "- The Daily Run checking the orrery it pulled is the one you pushed\n  (L-461 (pull matches push)).\n- The Sun's pole and spin on the website (L-465 (the Sun's axis)).\n")]},
    {'path': 'documentation/HANDOFF_L456_addresses_build_20261021.md', 'mode': 'edit', 'anchors_only': True, 'zone': None, 'edits': [('This close patch also carries the ledger lines and Where We Are\n', "Closed the same evening on your phone (run record): no band with the\nGalactic Plane ticked and Go To on the Corona; the Sun's own row shows\nNASA's link and the pole's source. L-463 and L-464 are DONE. The\ndashboard button the website patch missed is added by\n`patch_L463_2_far_lines_button_20261021.py`. Your next question, the\nSun's pole and spin drawn as the orrery does, is L-465.\n\nThis close patch also carries the ledger lines and Where We Are\n")]},
]


def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def outside(text, zone):
    if not zone:
        return text
    i = text.index(zone[0])
    j = text.index(zone[1]) + len(zone[1])
    return text[:i] + text[j:]


def fail(message):
    print(message)
    print("NOTHING was written.")
    return 1


def read(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n")


def main():
    planned = []
    removals = []
    led = os.path.join(HERE, "LEDGER_CONSOLIDATED.md")
    if os.path.exists(led) and "#### [L-465]" in read(led):
        return fail("ERROR: the ledger already holds L-465. This patch "
                    "has run before.")
    if os.path.exists(led) and "#### [L-461]" not in read(led):
        return fail("ERROR: run patch_L456_7_close_20261021.py first; "
                    "this one edits the lines it writes.")
    for f in FILES:
        rel = f["path"]
        path = os.path.join(HERE, *rel.split("/"))
        mode = f["mode"]
        if mode == "remove":
            if not os.path.exists(path):
                print("ok  %-50s already gone" % rel)
                continue
            if md5(read(path)) != f["base_md5"]:
                return fail("ERROR: %s differs from what the earlier patch "
                            "4 wrote; it is left alone." % rel)
            removals.append((rel, path))
            print("ok  %-50s to be removed" % rel)
            continue
        if not os.path.exists(path):
            return fail("ERROR: %s is not here. Save this patch in %s "
                        "root folder."
                        % (rel, FOLDER_WORD))
        try:
            text = read(path)
        except UnicodeDecodeError:
            return fail("ERROR: %s is not UTF-8." % rel)
        if mode == "replace":
            have = md5(text)
            if have == f["new_md5"]:
                return fail("ERROR: %s already carries this patch's "
                            "change. It has run before." % rel)
            if have != f["base_md5"]:
                return fail("ERROR: %s is not what the earlier patch 4 "
                            "wrote." % rel)
            planned.append((rel, path, f["content"]))
            print("ok  %-50s replaced" % rel)
            continue
        zone = f.get("zone")
        anchors_only = f.get("anchors_only", False)
        if not anchors_only:
            have = md5(outside(text, zone))
            if have == f["new_md5"]:
                return fail("ERROR: %s already carries this patch's "
                            "change. It has run before." % rel)
            if have != f["base_md5"]:
                return fail("ERROR: %s is not what the earlier patch 4 "
                            "wrote." % rel)
        for n, (old, new) in enumerate(f["edits"], 1):
            count = text.count(old)
            if count != 1:
                first = old.strip().splitlines()[0][:60] if old.strip() else ""
                return fail("ANCHOR FAIL: %s edit %d matched %d times: %r"
                            % (rel, n, count, first))
            text = text.replace(old, new)
        if not anchors_only and md5(outside(text, zone)) != f["new_md5"]:
            return fail("ERROR: %s came out different from the tested "
                        "result." % rel)
        planned.append((rel, path, text))
        print("ok  %-50s %d edit(s)" % (rel, len(f["edits"])))

    for rel, path, text in planned:
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
    for rel, path in removals:
        os.remove(path)
    print("patch applied (%d file(s) written, %d removed)"
          % (len(planned), len(removals)))
    print("")
    for line in NEXT:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
