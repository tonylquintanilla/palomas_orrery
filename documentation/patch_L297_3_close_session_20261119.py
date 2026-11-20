"""
patch_L297_3_close_session_20261119.py -- closes the coordinating session
of Nov 18 and 19 (L-297, the Lagrange points): the round live and looked
at, and Tony's four rulings of Nov 19 on the cleanup it found.

Built on orrery 1c0688ca6660b991c3de917826304892b9e7fa9f at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 0c832de1caf357efd34c6b5c36770ee394d0bbec at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read
Nov 19, 2026, 21:10 Chicago. Written by the coordinating session (Claude
Opus 5.5) under safe-file-editing 1.14 and ledger-and-session-records 1.23.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\,
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.

WHAT IT CHANGES (two files)

    LEDGER_CONSOLIDATED.md
      L-297 (the Lagrange points): live and looked at; L4 and L5 beside
        the drawn orbit, measured; its loose ends re-homed; DONE.
      L-512 (the orrery's fallbacks): a point's elements and close
        approaches asked of JPL, received from L-297.
      L-533 (ESCAPADE): the box's last day ruled, "Yes".
      L-536 (a moon's yearly change): Tony's rule for a period's digits
        and its sentence.
      L-538 (the orbiters' printed error): no stopgap; the real fix.
      L-432 (the default goldenrod): the colour table moved; the 24 still
        in goldenrod, named.
      L-539 (every entry checked against JPL), new.
      Then it runs ledger_index.py.
    documentation/WHERE_WE_ARE.md, by section, above the run-record
      marker only: the header; the box; road stage 15 and line b;
      Settled; Deferred; Signals; Waiting on you; Where the details are.
      It stays within 130 lines.

    Each edit is checked at the text it replaces; your notes elsewhere
    are left alone. Nothing is written unless every edit finds its text.

RUN COMMAND

    Save in the orrery's root folder, open in VS Code, click Run.
    (python patch_L297_3_close_session_20261119.py)

    Success: "ok" lines, then "patch applied". Failure: one ERROR or
    ANCHOR FAIL line, and nothing is written.

Written November 19, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
PAGE = os.path.join("documentation", "WHERE_WE_ARE.md")
MARKER = b"--- Your run record below this line"


def b(s):
    return s.encode("ascii")


# ---- the ledger ----------------------------------------------------------

L297_OLD_GAP = """**Gap:** the push and the Daily Run (Tony's run order of Nov 19); Tony's
phone look; the skill bumps above are written, with L-537
(patch_L297_2_skills_and_protocol.py, Nov 19): Tony reinstalls the
three and pastes v3.143.
"""
L297_NEW_GAP = """**Note:** (2026-11-19, evening, LIVE AND LOOKED AT; the coordinating
session, Claude Opus 5.5) pushed at orrery a70d98c5 and gallery 56bc3fab
after the Daily Run of 11:55 (50 of 50 gating checks, the swap "ok");
the skills and v3.143 at orrery 1c0688ca, reinstalled and pasted.
- TONY'S PHONE LOOK, 20:36 to 20:48 Chicago, in his run record
  `WHERE_WE_ARE_11-18-26_2200_run_record.md`: every line "yes" but one.
  On L4 and L5 sitting on the Moon's orbit: "nearly on the drawn orbit.
  i assume that is because of the perturbations." Measured from the
  served files that evening: on all 90 days, JPL's Earth-Moon L4 and L5
  sit at exactly the Moon's distance from Earth and exactly 60 degrees
  from it, a triangle on the Moon as it is now. The drawn orbit is an
  ellipse, the Moon's distance 364,445 to 405,584 km over those days,
  so 60 degrees from the Moon it lies a little nearer or farther.
  Geometry, not perturbation; nothing to fix.
- RE-HOMED before closing (A Closing Item Re-homes Its Loose Ends): the
  orrery's pre-fetch asking JPL for a point's elements ("Required
  masses not defined") and the close-approach cache asking by a point's
  number, to L-512 (the orrery's fallbacks), whose skip lists are where
  a point belongs; the box's last day, to L-533, ruled Nov 19; the
  orbiters' printed error, L-538; a check of every entry asked of JPL,
  L-539, new.
**Gap:** none.
"""

L297_META_OLD = "<!-- L:297 status:OPEN upd:2026-11-19 section:A flag: rice:2/3/70/3 -->\n"
L297_META_NEW = "<!-- L:297 status:DONE upd:2026-11-19 section:A flag: rice:2/3/70/3 -->\n"

L512_META_OLD = "<!-- L:512 status:OPEN upd:2026-11-04 section:A flag: rice: -->\n"
L512_META_NEW = "<!-- L:512 status:OPEN upd:2026-11-19 section:A flag: rice: -->\n"
L512_GAP_OLD = "**Gap:** Tony's look at A2, wifi off and on; then slices b and c.\n"
L512_GAP_NEW = """- **Received 2026-11-19 from L-297 (the Lagrange points):** a ticked
  Lagrange point still enters the osculating pre-fetch (its object_type
  is on that list), and JPL answers "Required masses not defined,
  osculating elements not available", printed with a traceback and
  passed over; and the close-approach cache asks JPL's small-body
  service by the point's number (3011 ...), which answers with no
  approaches. The plot is drawn. A point has no elements and no close
  approaches to ask for: it belongs on the skip lists, with a comment
  naming what failed (horizons-orbital-mechanics, A Skip Names What
  Failed). Found by L-297's Session 1, Nov 18.
**Gap:** Tony's look at A2, wifi off and on; then slices b and c; and
the Lagrange points kept out of the pre-fetch and the close approaches.
"""

L533_META_OLD = "<!-- L:533 status:OPEN upd:2026-11-18 section:A flag: rice: -->\n"
L533_META_NEW = "<!-- L:533 status:OPEN upd:2026-11-19 section:A flag: rice: -->\n"
L533_GAP_OLD = """**Gap:** the row under Mars, by L-534's rule once it is designed. The
box's last day waits for Tony's ruling (the note of Nov 19). The loops near L2, with
"""
L533_GAP_NEW = """**Note:** (2026-11-19, 21:03, the coordinating session, Claude Opus 5.5)
THE BOX'S LAST DAY, RULED. Tony: "Yes" -- the website asks JPL for each
span's last moment too, as `fetch_path_last_day` does for an ended
mission, so the 27 paths that stop short run to their span's end and
each box names that day. A gallery build of its own.
**Gap:** the row under Mars, by L-534's rule once it is designed. The
box's last day: its build, as ruled Nov 19. The loops near L2, with
"""

L536_META_OLD = "<!-- L:536 status:OPEN upd:2026-11-15 section:A flag: rice: -->\n"
L536_META_NEW = "<!-- L:536 status:OPEN upd:2026-11-19 section:A flag: rice: -->\n"
L536_GAP_OLD = """**Gap:** its own session: measure the swing (JPL's PR at many dates
across a year), choose how the digits are set from it, and the period
fetch's and the digits test's checks; Tony's word on the rule.
"""
L536_GAP_NEW = """**Note:** (2026-11-19, 16:48 to 16:52, the coordinating session, Claude
Opus 5.5) TONY'S RULE. The instance first: the Moon's period on the
website reads 26.9 days since the push of Nov 19 (it read 27); its two
dates fell on like points of its swing (JPL's figure 27.43 days on Nov
6 and 26.88 on Nov 19, per L-297's Session 2). Ruled: a period prints
TODAY'S figure, the osculating period at the date shown as now, with
only the digits its swing allows, and its sentence gives the swing's
range, measured -- for example "27 days. JPL's figure for the Moon
swings between 26.9 and 27.4 days through its month, because the Sun
pulls on it, so it is given to the whole day." The range is read from
JPL's figures across a year, about weekly, never typed; one rule for
every body, the orrery and the website printing one sentence (L-535).
Tony: "Can we also give the uncertainty because many people will
question the imprecision" -- the range is that. The year's average was
offered and not taken. The sampling is method, for
horizons-orbital-mechanics when it is built.
**Gap:** its own session, in the orrery (the period fetch, the export,
the digits test) and the website's sentence; the Moon first.
"""

L538_GAP_OLD = """**Gap:** the design, in an orrery session with the path plan; until then
those boxes print up to about one place finer than earned.
"""
L538_GAP_NEW = """**Note:** (2026-11-19, 16:45, the coordinating session, Claude Opus 5.5)
TONY'S RULING: no stopgap. A coarser figure in those boxes until the fix
was offered and not taken; "Yes" to the real fix, soon. The likely cure
reuses what L-297 built: points an hour apart from yesterday to the day
after tomorrow for a craft inside a capture, as for the Lagrange
points, so the box places it on its loop on the dates visitors mostly
see. Tony asked first, "I thought that the path already varies in
frequency by its curve?" It does, at events; the orbiter rule keeps a
capture's loops out of the events (Tony, 2026-10-24), so between an
arrival and a departure the points stay a week apart.
**Gap:** the build, soon (Tony, Nov 19): finer points near today for a
craft inside a capture; until then those boxes print up to about one
place finer than earned.
"""

L432_META_OLD = "<!-- L:432 status:OPEN upd:2026-11-18 section:A flag: rice: -->\n"
L432_META_NEW = "<!-- L:432 status:OPEN upd:2026-11-19 section:A flag: rice: -->\n"
L432_GAP_OLD = """**Gap:** trace which of the 27 actually draw goldenrod; then Tony picks
colours, Encke first, beside Halley and the other comets.
**Ref:** `constants_new.py` (`color_map`); `celestial_objects.py`;
L-395.
"""
L432_GAP_NEW = """**Note:** (2026-11-19, the coordinating session, Claude Opus 5.5) THE
CLASS IS FIXED: the colour table moved out of `constants_new.py` into
`orrery_colors.py`, a drawing module, re-exported by one import
(patch_L432_1_colors_to_drawing_code.py, pushed at orrery 1c0688ca;
Tony's ruling of 2026-09-22). The eight Lagrange points keep their
colours under the names shown; the two L3 lines and the name map are
gone. The Constants change check names a colour line leaving the store
and passes, and fails on one added there, with a self-test of the
shape every run. Tony's look in the orrery: "okay". Of the patch's
closing line, provenance-discipline's note names DEFAULT_MARKER_SIZE
and CENTER_MARKER_SIZE, not the colour table, so it stands as written.
- WHICH DRAW GOLDENROD, traced Nov 19 at 1c0688ca by each entry's
  colour key: 24. Planet 9, Mani, 2026 ED138, Encke, West, Tsuchinshan,
  Parker, Vanth; TRAPPIST-1 and its b to h; TOI-1338 A/B, its A and B
  and its b and c; Proxima Centauri and its b and d. For Planet 9, Mani
  and Vanth the colour key ('orbital', 'MS4', 'Van') names no line
  though a line exists under the name shown.
**Gap:** Planet 9, Mani and Vanth: their colour keys; then Tony picks
colours for the rest on his eye at the desk (Mode 5), Encke first, one
line each in orrery_colors.py.
**Ref:** `orrery_colors.py` (`color_map`, moved from `constants_new.py`
Nov 19); `celestial_objects.py`; L-395.
"""

L539_ANCHOR = "#### [L-529] Guided encounters: the guide's way of telling"
L539_BLOCK = """#### [L-539] Every entry the orrery asks JPL for is checked against JPL, not only the website's (orrery, the Horizons check)
<!-- L:539 status:OPEN upd:2026-11-19 section:A flag: rice: -->
- **Found 2026-11-19** in L-297 (the Lagrange points): the orrery's
  Earth-Moon L3 and L3, asked as 3013 and 33, had drawn the asteroids
  3013 Dobrovoleva and 33 Polyhymnia under those names. Nothing caught
  it: `horizons_check.py` confirms only the entries the objects export
  carries, those with a 'key'.
- **The class, counted at orrery 1c0688ca** (`celestial_objects.py`):
  of 184 entries, 74 have no key, and 57 of those are asked of JPL --
  43 moons (Jupiter's Metis to Callisto, Saturn's Pan to Phoebe,
  Uranus's Ariel to Mab, Neptune's Triton, Despina and Galatea, Pluto's
  Charon, Styx, Nix, Kerberos and Hydra, and Dysnomia, Xiangliu, Vanth,
  Weywot, Hi'iaka, Namaka and MK2); 8 spacecraft (Apollo 11 S-IVB,
  SOHO, Gaia, Hayabusa2, OSIRISREx, MarsRover, JamesWebb, Artemis II);
  3 barycentres (Earth-Moon, Orcus-Vanth, Patroclus-Menoetius); and
  Menoetius, Pluto and 6AC4721. The other 17 are not asked of JPL:
  Planet 9, and the exoplanets and their stars.
- **Tony's ruling, 2026-11-19, 15:30:** "Yes" -- the check covers every
  entry the orrery asks JPL for. Its first run writes a one-time list,
  each entry beside the name JPL gives its id, for Tony to scan once,
  as the two L3 entries would have shown; from then on it stores JPL's
  name and holds the entry to it every 30 days, a few per run, under
  the maintenance run's 15 minutes.
**Gap:** a Code session in the orrery (horizons_check.py and its suite).
**Ref:** L-297 (the Lagrange points); L-395 (the Horizons check);
horizons-orbital-mechanics, Checking an Entry Against JPL.

"""

LEDGER_EDITS = [
    ("L-297: DONE", L297_META_OLD, L297_META_NEW),
    ("L-297: the note, Gap none", L297_OLD_GAP, L297_NEW_GAP),
    ("L-512: date stamp", L512_META_OLD, L512_META_NEW),
    ("L-512: received from L-297", L512_GAP_OLD, L512_GAP_NEW),
    ("L-533: date stamp", L533_META_OLD, L533_META_NEW),
    ("L-533: the last day ruled", L533_GAP_OLD, L533_GAP_NEW),
    ("L-536: date stamp", L536_META_OLD, L536_META_NEW),
    ("L-536: Tony's rule", L536_GAP_OLD, L536_GAP_NEW),
    ("L-538: no stopgap", L538_GAP_OLD, L538_GAP_NEW),
    ("L-432: date stamp", L432_META_OLD, L432_META_NEW),
    ("L-432: the table moved, the 24 named", L432_GAP_OLD, L432_GAP_NEW),
    ("L-539: new item", L539_ANCHOR, L539_BLOCK + L539_ANCHOR),
]

# ---- Where We Are ---------------------------------------------------------

PAGE_EDITS = [
    ("header",
     "Last updated: November 19, 2026, morning: the Lagrange points built on the website too, not pushed (Opus, Claude Code).\n"
     "- Written at orrery 53bf2469 and gallery 133dbd21, with both Lagrange sessions' edits on your disk.\n",
     "Last updated: November 19, 2026, night: the Lagrange points live and looked at; this round's cleanup ruled (Opus, coordinating session).\n"
     "- Written at orrery 1c0688ca and gallery 0c832de1, with this patch's edits on your disk.\n"),
    ("box: changed",
     "> - The website now serves and draws the eight Lagrange points: the Earth-Moon four in Earth's fold, the Earth-Sun four in a group after Earth, each a square in the orrery's colour, with NASA's words and its distance from its own centre, served an hour apart near today (L-297 (the Lagrange points)).\n"
     "> - The twins' names sit on opposite sides, and Earth-Moon L1's name is on the left. The points' and the open-path comets' boxes print the curve's error, held by a new daily check; craft orbiting a planet print a digit too many inside your dates, logged as L-538 (the orbiters' printed error). Nothing pushed yet.\n",
     "> - The eight Lagrange points are live on the website and in the orrery, and your phone look passed every line. L4 and L5 sit just off the Moon's drawn orbit by geometry: JPL puts them at the Moon's distance now, 60 degrees either side, and the orbit is an ellipse (L-297 (the Lagrange points), closed).\n"
     "> - The orrery's colours live in their own drawing file now, `orrery_colors.py`; three skills updated, the protocol at v3.143, the skills page at Plugins (L-432 (the default goldenrod), L-537 (the skills page), closed).\n"),
    ("box: do next",
     "> **Do next:** *Push both by the run order, before 16:00 UTC; the Daily Run; your phone look; then the round's skill bumps (L-297 (the Lagrange points)); then the design talk on destinations and encounters.*\n",
     "> **Do next:** *The design talk on destinations and encounters (L-534 (missions by destination), L-529 (guided encounters)); beside it, this round's cleanup (the road, line b).*\n"),
    ("box: needs you now",
     "> - *(do) Push the orrery, then the website after the Daily Run, before 16:00 UTC (GitHub runs the nights hours late).*\n",
     ""),
    ("road: stage 15",
     "               live Nov 18; the Lagrange points (L-297): both\n"
     "               halves built Nov 18 and 19, the push next; then the\n",
     "               live Nov 18; the Lagrange points (L-297) live\n"
     "               Nov 19, on your phone look; next, the\n"),
    ("road: line b",
     "  b.   [beside] Housekeeping: L-424, L-425, L-426 (the checkers' three);\n",
     "  b.   [beside] This round's cleanup, each ruled Nov 19 (the order is yours): every path to its last day, L-533 (ESCAPADE); the orbiters' hourly points, L-538 (the orbiters' printed error); every entry checked against JPL, L-539 (every entry checked); the period's swing in its sentence, L-536 (a moon's yearly change); the 24 in goldenrod, L-432 (the default goldenrod), at your desk. << new this session\n"
     "  h.   [beside] Housekeeping: L-424, L-425, L-426 (the checkers' three);\n"),
    ("Settled: four rulings in",
     "Standing rulings; a line leaves once it is habit, or a skill carries it.\n",
     "Standing rulings; a line leaves once it is habit, or a skill carries it.\n"
     "- Every path runs to its span's last day: the website asks JPL for it too (Nov 19; L-533 (ESCAPADE)).\n"
     "- A period prints today's figure with only the digits its swing allows, and its sentence gives the swing's measured range (Nov 19; L-536 (a moon's yearly change)).\n"
     "- A craft orbiting a planet gets the real fix, hourly points near today, and no stopgap (Nov 19; L-538 (the orbiters' printed error)).\n"
     "- Every entry the orrery asks JPL for is checked against JPL, starting from a one-time list you scan (Nov 19; L-539 (every entry checked)).\n"),
    ("Settled: the drawer line out",
     "- The drawer opens at the row its handle names, scrolled into view and highlighted; the opening names Earth (\"Keep Earth\") (Nov 16; L-535 (the period's reason)).\n",
     ""),
    ("Settled: El Nino's design line out",
     "- El Nino is a page like Sudan's, its chart the June design; one source of record, NOAA's Climate Prediction Center, its forecast NOAA's own chances on RONI; WMO and Australia's index left out (Nov 16; L-060 (El Nino)).\n",
     ""),
    ("Settled: the frame line out",
     "- Every frame fits across the picture's narrow side, the farthest point of what it frames plus 10 percent; a picture wider than tall is unchanged. The Solar System view, its Home and Reset frame where bodies are now (your ruling of Oct 2), so an orbit line may run past the side there: the dots stay inside, and Go To shows a whole orbit (Nov 15; L-514 (the Mars room)).\n",
     ""),
    ("Deferred: L-536 out, on the road",
     "- A moon's change in a year, read from two dates, catches the moon's own short wobble (Phobos's jumped 20 times in a day); the digits should come from many dates: its own session (Nov 15; L-536 (a moon's yearly change)).\n",
     ""),
    ("Deferred: L-538 out, on the road",
     "- A craft orbiting a planet: its points cut corners, and inside your dates Juno and BepiColombo print a digit too many (Nov 19; L-538 (the orbiters' printed error), with L-507 (historical missions)).\n",
     ""),
    ("Signals: the cache build",
     "- Last cache build: 20261118T230303Z, ok, no retry on the swap (the website's swap log at 133dbd21, read Nov 18).\n",
     "- Last cache build: 20261119T204434Z, ok, no retry on the swap (the website's swap log at 0c832de1, read Nov 19).\n"),
    ("Signals: Tier-1",
     "- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, generated by this session's maintenance run, Nov 18, read Nov 18).\n",
     "- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md at orrery 1c0688ca, generated Nov 19, read Nov 19).\n"),
    ("Waiting on you: the decision answered",
     "- 27 of 34 flying paths stop 1 to 7 days short of their span, the twins among them: ask JPL for each span's last day too? (L-533 (ESCAPADE)).\n",
     "- None open. The last day was ruled Nov 19: yes, each path asks for its span's last day (L-533 (ESCAPADE)).\n"),
    ("Waiting on you: the labels to the design talk",
     "- Planet 9: how to show a body that may not exist.\n",
     "- Planet 9: how to show a body that may not exist.\n"
     "- A tidier Solar System view: where several names share a few pixels, only the largest body's name until you zoom in (Nov 19; L-297 (the Lagrange points)).\n"),
    ("Where the details are: this round",
     "- This round: L-297 (the Lagrange points), its brief `COORD_L297_lagrange_points_brief_20261118.md`, the words `WORDS_L297_lagrange_points_20261118.md`; the website's `INTERACTIVE_AS_BUILT.md`, The Lagrange points; L-538 (the orbiters' printed error).\n",
     "- This round: L-297 (the Lagrange points), its brief `COORD_L297_lagrange_points_brief_20261118.md`, the words `WORDS_L297_lagrange_points_20261118.md`; the website's `INTERACTIVE_AS_BUILT.md`, The Lagrange points; the close `patch_L297_3_close_session_20261119.py`; your run record `WHERE_WE_ARE_11-18-26_2200_run_record.md`.\n"),
]


def plan(path, edits, top_only=False):
    if not os.path.exists(path):
        print("ERROR: %s not found. Run this from the orrery's root folder "
              "(palomas_orrery_for_github). Nothing was written." % path)
        return False, None
    raw = open(path, "rb").read()
    text = raw.replace(b"\r\n", b"\n")
    if top_only:
        if text.count(MARKER) != 1:
            print("ERROR: the run-record marker is not on %s once. Nothing "
                  "was written." % path)
            return False, None
        top, marker, bottom = text.partition(MARKER)
    else:
        top, marker, bottom = text, b"", b""
    for label, old, new in edits:
        n = top.count(b(old))
        if n != 1:
            print("ANCHOR FAIL: %s in %s -- expected its text once, found "
                  "%d. If this patch already ran, there is nothing to do. "
                  "Nothing was written." % (label, path, n))
            return False, None
        top = top.replace(b(old), b(new))
        print("ok %s" % label)
    if top_only and top.count(b"\n") > 130:
        print("ERROR: %s would stand over 130 lines above its marker (%d). "
              "Nothing was written." % (path, top.count(b"\n")))
        return False, None
    if b"\r\n" in raw:
        print("note: %s was CRLF in the working copy; written LF" % path)
    return True, top + marker + bottom


def main():
    if os.path.basename(os.getcwd()).lower() == "documentation":
        print("ERROR: run this from the orrery's root folder, not from "
              "documentation\\. Nothing was written.")
        return 1
    for _, _, new in LEDGER_EDITS + PAGE_EDITS:
        b(new)  # raises on a non-ASCII character before anything is written
    ok, led = plan(LEDGER, LEDGER_EDITS)
    if not ok:
        return 1
    ok, page = plan(PAGE, PAGE_EDITS, top_only=True)
    if not ok:
        return 1
    with open(LEDGER, "wb") as f:
        f.write(led)
    print("ok %s written" % LEDGER)
    with open(PAGE, "wb") as f:
        f.write(page)
    print("ok %s written (%d lines above the marker)"
          % (PAGE, page.partition(MARKER)[0].count(b"\n")))
    print("Running ledger_index.py ...")
    r = subprocess.run([sys.executable, "ledger_index.py"],
                       capture_output=True, text=True)
    for line in (r.stdout + r.stderr).strip().splitlines()[-4:]:
        print("  " + line)
    if r.returncode != 0:
        print("ERROR: ledger_index.py exited %d. The edits above are "
              "written; Discard Changes in GitHub Desktop undoes them. "
              "Paste these lines to the session." % r.returncode)
        return 1
    print("ok ledger_index.py")
    print("patch applied")
    print("")
    print("Do next:")
    print("  1. (do) Move this file into documentation\\.")
    print("  2. (do) In GitHub Desktop (orrery): commit and push the ledger,")
    print("     Where We Are, this file and the next coordinator's prompt")
    print("     (documentation\\PROMPT_coordinator_start_20261120.md).")
    print("     Not while a night is running.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
