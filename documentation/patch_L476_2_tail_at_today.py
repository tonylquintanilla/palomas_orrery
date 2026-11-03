"""
patch_L476_2_tail_at_today.py -- L-476 (the orrery plots by the path
plan), second patch: the solid part of a planned path ends at today.

Built on orrery 329f4ec8fc175f20bf7151a081b5aeb222601efa at
https://github.com/tonylquintanilla/palomas_orrery (branch main), read
live on Nov 3, 2026. Written by the coordinating session (Claude Opus
5.5) from Tony's run record WHERE_WE_ARE_11-3-26_1158_run_record.md.

WHY

    Tony's look, Nov 3: "the spacecraft is within the dashed line"
    (Voyager 1) and "the object is within the dashed line" (3I/ATLAS).
    His saved plot shows why: Voyager 1's solid part ended at 135.8 AU,
    about ten years back, while the spacecraft was at 172.2 AU. The
    brief told the build to leave out the website's daily tail. On a
    straight run the thinning keeps no point near today, so the line
    turned dashed at the last point it kept. Juno passed only because
    its path curves and keeps points near today.

WHAT IT CHANGES (four files, all or nothing)

    path_drawing.py       draw_plan adds the website's daily tail, 7 days
                          behind today and 2 ahead, at a day's step, never
                          thinned; asked from 2 minutes earlier, so its
                          point for today is labelled before now on JPL's
                          clock and ends the solid part. Docstring and
                          stamp.
    test_path_drawing.py  check 5: the solid part ends within 5 minutes
                          of now on a straight run; planted fault, the
                          tail turned off, must fail. Docstring, stamp.
    palomas_orrery_dashboard.py  the suite's button line: 7 of 7, two
                          planted faults. Stamp.
    LEDGER_CONSOLIDATED.md  L-476: Tony's look and this fix; the skill
                          sentence carried; a new Gap.

    The permanent part is the tail in draw_plan and check 5. The script
    itself is one-shot.

    NOT CHANGED, AND NAMED: skills/horizons-orbital-mechanics/SKILL.md
    (1.15), A Plan Draws a Path Only Around the Sun, still says the
    orrery's drawing is the website's "without its daily tail and
    last-day pair". After this patch it keeps the tail. Carried on L-476
    for the skill's next version.

RUN COMMAND

    Save this file in the orrery's root folder
    (C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\),
    open it in VS Code and click Run. (python patch_L476_2_tail_at_today.py)

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line, and nothing is written. Undo is Discard
    Changes in GitHub Desktop.

Written November 3, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

EXPECT = {
    "path_drawing.py": "6c1e81f797cea22677686594c9eccbef",
    "test_path_drawing.py": "f5d18395ae880f789e4ac963d460fe9a",
    "palomas_orrery_dashboard.py": "b5664b0a2472b1dd2180d938fbc08f1b",
    "LEDGER_CONSOLIDATED.md": "8335288127b9af0f6c86ea88145af1d6",
}

ZONE_A = b"<!-- INDEX:START"
ZONE_B = b"<!-- INDEX:END -->"


def fingerprint(name, lf):
    if name == "LEDGER_CONSOLIDATED.md":
        a = lf.index(ZONE_A)
        b = lf.index(ZONE_B) + len(ZONE_B)
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


EDITS = {}

# ---------------------------------------------------------------- path_drawing.py
EDITS["path_drawing.py"] = [
    (b"""backbone's thinning, so a flyby is never thinned away. The website then
adds a daily tail and an ended mission's last-day pair, which are its
room's needs (a marker at the minute the room is opened); the orrery
draws neither. Its twin is fetch_path_by_plan, _plan_span,
fetch_vectors_range and douglas_peucker in the website's
tools/gallery_cache_builder.py (tonyquintanilla.github.io); the two
repositories cannot import each other, so each holds its own copy, and
test_path_drawing.py --galileo compares them against JPL.
""",
     b"""backbone's thinning, so a flyby is never thinned away; then a daily
tail around today, as the website's builder adds one, so the path has a
point of its own at today and the solid part ends where the spacecraft
or comet is. (Fixed 2026-11-03, evening, on Tony's look: built first
without the tail, Voyager 1's solid part ended about ten years back,
at 135.8 AU, with the spacecraft at 172.2 AU; on a straight run the
thinning keeps no point near today.) The website's tail has the same
length and step; its moments are each night's, so only an ended path,
which has no tail, agrees point for point. An ended mission's last-day
pair is the website room's need and is not drawn here. Its twin is
fetch_path_by_plan, fetch_path_tail, _plan_span, fetch_vectors_range
and douglas_peucker in the website's tools/gallery_cache_builder.py
(tonyquintanilla.github.io); the two repositories cannot import each
other, so each holds its own copy, and test_path_drawing.py --galileo
compares them against JPL.
"""),
    (b"""Module created: November 3, 2026 with Anthropic's Claude Opus 5.5
(L-476).
\"\"\"
""",
     b"""Module created: November 3, 2026 with Anthropic's Claude Opus 5.5
(L-476).
Module updated: November 3, 2026, evening, with Anthropic's Claude Opus
5.5 (L-476, Tony's look: the website's daily tail added, so the solid
part ends at today; see the third paragraph).
\"\"\"
"""),
    (b"""WINDOW_THIN_FRACTION = 0.01
""",
     b"""WINDOW_THIN_FRACTION = 0.01

# The daily tail around today, the website's: its builder's
# PATH_TAIL_AHEAD_DAYS (2) ahead, and its config's freeze_after_days (7)
# behind, at a day's step, never thinned (fetch_path_tail). Drawing
# choices mirrored from the website, not measured values.
TAIL_BEHIND_DAYS = 7
TAIL_AHEAD_DAYS = 2
TAIL_STEP = "1d"

# JPL labels each point on its own clock, 69 s ahead of UTC (TDB_OFFSET
# below). The tail is asked from two minutes earlier, so its point for
# today is labelled before now and ends the solid part.
TAIL_LEAD_MINUTES = 2
"""),
    (b"""def draw_plan(obj, plan, fetch=None):
    \"\"\"[{'date', 'jd', 'x', 'y', 'z'}] in time order: the path by its
    plan, the website's whole fetch without its tail and last-day pair.
""",
     b"""def draw_plan(obj, plan, fetch=None, now=None):
    \"\"\"[{'date', 'jd', 'x', 'y', 'z'}] in time order: the path by its
    plan, the website's whole fetch with its daily tail around now (UTC;
    utc_now() when not given), without its last-day pair.
"""),
    (b"""            points.update(got)
    except Exception as exc:
""",
     b"""            points.update(got)
        today = (now or utc_now()).replace(second=0, microsecond=0)
        t0 = max(start, today - datetime.timedelta(
            days=TAIL_BEHIND_DAYS, minutes=TAIL_LEAD_MINUTES))
        t1 = min(end, today + datetime.timedelta(days=TAIL_AHEAD_DAYS))
        if t0 < t1:
            points.update(fetch(ident, id_type, t0, t1, TAIL_STEP))
    except Exception as exc:
"""),
]

# ----------------------------------------------------------- test_path_drawing.py
EDITS["test_path_drawing.py"] = [
    (b"""      4. A planned entry's checkbox label is its plan's span.
""",
     b"""      4. A planned entry's checkbox label is its plan's span.
      5. The daily tail around now: on a straight run, where the
         thinning keeps no point near now, the solid part still ends
         within five minutes of now. Planted fault: the tail turned off,
         and the solid part ends at the flyby, two months back.
"""),
    (b"""Module created: November 3, 2026 with Anthropic's Claude Opus 5.5
(L-476).
\"\"\"
""",
     b"""Module created: November 3, 2026 with Anthropic's Claude Opus 5.5
(L-476).
Module updated: November 3, 2026, evening, with Anthropic's Claude Opus
5.5 (L-476: check 5, the daily tail, and its planted fault).
\"\"\"
"""),
    (b"""          % pd.span_label("craft", plans))


def galileo(plant=False):
""",
     b"""          % pd.span_label("craft", plans))

    gap = solid_gap()
    check(gap is not None and gap <= 5.0,
          "5. on a straight run the solid part ends at now: its last "
          "point %s minutes before now" % gap)
    saved = (pd.TAIL_BEHIND_DAYS, pd.TAIL_AHEAD_DAYS, pd.TAIL_LEAD_MINUTES)
    pd.TAIL_BEHIND_DAYS = pd.TAIL_AHEAD_DAYS = pd.TAIL_LEAD_MINUTES = 0
    try:
        bad = solid_gap()
    finally:
        (pd.TAIL_BEHIND_DAYS, pd.TAIL_AHEAD_DAYS,
         pd.TAIL_LEAD_MINUTES) = saved
    check(bad is not None and bad > 1440.0,
          "5. planted fault caught: with the tail turned off the solid "
          "part ends %s minutes before now" % bad)


def solid_gap():
    \"\"\"Minutes from the solid part's last point to now, for PLAN drawn
    on FakeJPL with now in its straight run, two months after the
    flyby; None when nothing is solid.\"\"\"
    now = datetime.datetime(2025, 5, 10, 12, 0)
    pts = pd.draw_plan({"key": "craft", "name": "Craft", "id": "-1",
                        "id_type": "id"}, PLAN, fetch=FakeJPL(), now=now)
    solid, dashed = pd.split_at(pts, now)
    if not solid or not dashed or dashed[0] is not solid[-1]:
        return None
    return (now - solid[-1]["date"]).total_seconds() / 60.0


def galileo(plant=False):
"""),
]

# --------------------------------------------------- palomas_orrery_dashboard.py
EDITS["palomas_orrery_dashboard.py"] = [
    (b"""         "and the checkbox label from the plan; one planted fault caught. "
         "Ends on \\"PATH DRAWING SUITE: 5 of 5 checks passed\\" (L-476).",
""",
     b"""         "the checkbox label from the plan, and the solid part ending at "
         "today on a straight run; two planted faults caught. "
         "Ends on \\"PATH DRAWING SUITE: 7 of 7 checks passed\\" (L-476).",
"""),
    (b"""the launch-card / status-log UI code.
""",
     b"""the launch-card / status-log UI code.
Module updated: November 3, 2026 with Anthropic's Claude Opus 5.5
(L-476: the Path Drawing Suite's line, 7 checks, two planted faults).
"""),
]

# -------------------------------------------------------- LEDGER_CONSOLIDATED.md
EDITS["LEDGER_CONSOLIDATED.md"] = [
    (b"""**Gap (replaces the one below, 2026-11-03, afternoon):** Tony's Mode 5
look at five Sun-centred plots""",
     b"""- **2026-11-03, afternoon: Tony's look**
  (`documentation/WHERE_WE_ARE_11-3-26_1158_run_record.md`). Juno
  dashed to 2028-09-02, and Galileo solid to Jupiter: "yes". Voyager 1:
  "the spacecraft is within the dashed line"; 3I/ATLAS: "the object is
  within the dashed line". Read from his saved plot
  (solar_system_20261103_1934): Voyager 1's solid part ended at 135.8
  AU and its dashed part ran on from there, with the spacecraft at
  172.2 AU; 3I/ATLAS's solid part ended at 7.4 AU, the comet at 13.0
  AU. The cause is the brief's, which told the build to leave out the
  website's daily tail: on a straight run the thinning keeps no point
  near today, so the line turned dashed at the last point kept. Juno
  passed because its path curves near today.
- **Fixed the same evening** in `patch_L476_2_tail_at_today.py`, by the
  coordinating session (Claude Opus 5.5) on orrery 329f4ec8:
  `draw_plan` adds the website's daily tail, 7 days behind today and 2
  ahead, so the solid part ends within minutes of now;
  `test_path_drawing.py` check 5, with a planted fault (7 of 7).
- **Pioneer 10**, "outline the filled line": it has no plan, and its
  typed end is 2002-03-03, so its line stops at 79.8 AU and its marker
  is at today's 142.2 AU. As before this build; for historical
  missions' next slice (L-507).
- **Juno centred on Jupiter**, "i can't determine": the saved plot
  (solar_system_20261103_1952_juno) shows 51 evenly spaced points, one
  solid line and no dash, which is the drawing before this build.
- **Carried for horizons-orbital-mechanics' next version:** A Plan
  Draws a Path Only Around the Sun says the orrery's drawing is the
  website's "without its daily tail and last-day pair"; it now keeps
  the tail and leaves out only the last-day pair.
**Gap (replaces the one below, 2026-11-03, evening):** Tony's look at
Voyager 1 and 3I/ATLAS after `patch_L476_2`: each marker at the end of
the solid part. Whether `create_dates_list_for_object`, called from
nowhere, goes. Still open for L-484's talk: three planned comets the
orrery draws as ellipses (Tsuchinshan, Wierzchos, ATLAS C/2024 G3),
which the website draws as paths.
**Gap (superseded above, 2026-11-03, evening; replaced the one below, 2026-11-03, afternoon):** Tony's Mode 5
look at five Sun-centred plots"""),
]

ORDER = ["path_drawing.py", "test_path_drawing.py",
         "palomas_orrery_dashboard.py", "LEDGER_CONSOLIDATED.md"]


def main():
    if os.path.basename(ROOT) == "documentation":
        print("ERROR: run this from the orrery's root folder, not "
              "documentation/. NOTHING was written.")
        return 1
    out = {}
    for name in ORDER:
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            print("ERROR: %s not found next to this patch. Save the patch "
                  "in the orrery's root folder. NOTHING was written." % name)
            return 1
        raw = open(path, "rb").read()
        lf = raw.replace(b"\r\n", b"\n")
        got = fingerprint(name, lf)
        if got != EXPECT[name]:
            print("ERROR: %s is not the file this patch was built on "
                  "(orrery 329f4ec8). Its content differs: pull origin "
                  "in GitHub Desktop, or discard local edits to it, and "
                  "run again. NOTHING was written." % name)
            return 1
        for old, new in EDITS[name]:
            n = lf.count(old)
            if n != 1:
                print("ANCHOR FAIL: %s: expected 1 match, found %d: %r. "
                      "NOTHING was written." % (name, n, old[:60]))
                return 1
            lf = lf.replace(old, new)
            print("ok  %s: %s" % (name, old.strip().splitlines()[0][:60]
                                  .decode("ascii")))
        bad = [i for i, c in enumerate(lf) if c > 127]
        if bad:
            print("ERROR: %s would hold %d non-ASCII byte(s) after the "
                  "patch. NOTHING was written." % (name, len(bad)))
            return 1
        out[name] = (path, lf, b"\r\n" in raw)
    total = 0
    for name in ORDER:
        path, lf, was_crlf = out[name]
        with open(path, "wb") as handle:
            handle.write(lf)
        total += len(lf)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("stamps updated: path_drawing.py, test_path_drawing.py and "
          "palomas_orrery_dashboard.py (Module updated lines)")
    print("patch applied (%d bytes, 4 files)" % total)
    print()
    print("Do next, in order:")
    print("  1. Open test_path_drawing.py and click Run. It should end on")
    print("     \"PATH DRAWING SUITE: 7 of 7 checks passed\".")
    print("  2. Run palomas_orrery.py, tick Voyager 1 and 3I/ATLAS, centre")
    print("     on the Sun, and Plot. Each marker should sit where the")
    print("     solid line turns dashed.")
    print("  3. Run the maintenance run from the dashboard and read its")
    print("     last line: all gating checkers passed, Tier-1 0.")
    print("  4. Move this patch into documentation/, then commit and push")
    print("     the orrery in GitHub Desktop.")
    print("Not changed, and named: skills/horizons-orbital-mechanics/"
          "SKILL.md still says the drawing is without the daily tail;")
    print("carried on L-476 for its next version.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
