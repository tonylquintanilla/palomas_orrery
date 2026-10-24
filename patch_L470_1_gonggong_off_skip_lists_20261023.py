r"""patch_L470_1_gonggong_off_skip_lists_20261023.py -- Gonggong comes off
the orrery's Horizons skip lists, by Tony's ruling of Oct 23 ("Yes, or
just take it off the skip list and see if it fails"), so the maintenance
run is the test (L-470).

RUN COMMAND
    python patch_L470_1_gonggong_off_skip_lists_20261023.py

Save it in the ORRERY repository's root folder
(C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\),
open it in VS Code and click Run.

RUN IT AFTER patch_L472_2 and patch_L472_3, which it builds on; if patch
3 has not run, this one says so and writes nothing.

THEN, BEFORE COMMITTING:
  1. The orrery maintenance run. Look at two lines:
     - Period fetch: it should say it fetched Gonggong.
     - Horizons check: it should PASS, with Gonggong's period confirmed.
     If either names Gonggong as failing, do not commit: Discard Changes
     in GitHub Desktop and bring the line to Claude. The skip then goes
     back with the comment it lacked (which record, which centre, the
     date).
  2. One look in the orrery with Gonggong as the centre body, which the
     maintenance run does not ask. If it draws, every centre answered.
  3. Commit and push. The website's next Daily Run pulls the fetched
     period, and the typed 550.34 years is replaced by JPL's.
Then move this file to documentation/.

Built on orrery b90d895a4ef1cdc31daec7a20fef8c34369fa24c at
https://github.com/tonylquintanilla/palomas_orrery (branch main) with
patch_L472_2 and patch_L472_3 applied. The coordination note is
documentation/COORD_L470_gonggong_ruling_20261023.md. Final as
delivered: nothing will replace it.

WHAT IT CHANGES
    palomas_orrery.py    Gonggong off all six lists: SKIP_HORIZONS_PREFETCH
                         (static plot and animation), SKIP_HORIZONS_TRAJECTORY,
                         ANALYTICAL_POSITION_FALLBACK (two sites) and
                         ANALYTICAL_ANIMATION_FALLBACK, each with a dated
                         comment; the module's update stamp
    period_fetch.py      Gonggong off SKIP_NAMES, with a comment; the stamp
    LEDGER_CONSOLIDATED.md  header stamp; L-470, the ruling, the build and
                         its Gap
    documentation/WHERE_WE_ARE.md  the box's do line; Gonggong off the
                         design-talk list; a Settled line. The run-record
                         zone is not touched

PERMANENT: the four list changes. This script is disposable.

SUCCESS prints one "ok" line per file, then "patch applied".
FAILURE prints one FAILURE line, and NOTHING is written; undo is
Discard Changes in GitHub Desktop.

Written October 23, 2026 with Anthropic's Claude Opus 5.5.

Role: devtool
Domain: dev_tools
"""

import os
import sys

TITLE = 'L-470 Gonggong off the skip lists'
FILES = [
    {"path": 'palomas_orrery.py', "edits": [
        (b'did, so a body\'s orbit and marker come from one record, the one the\nwebsite serves.)\n\n"""\n',
         b'did, so a body\'s orbit and marker come from one record, the one the\nwebsite serves.)\nModule updated: October 23, 2026 with Anthropic\'s Claude Opus 5.5 (L-470:\nGonggong comes off all six Horizons skip lists, the two pre-fetch lists,\nthe static trajectory list and the three analytical fallbacks. No failure\nwas on record; it went on in commit c60572d, 2026-02-04, with Weywot\'s\ncomment beside it. Tony\'s ruling of this day: "just take it off the skip\nlist and see if it fails", so the maintenance run is the test.)\n\n"""\n'),
        (b"\n            #    ANALYTICAL_POSITION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', 'Weywot', '6AC4721']\n                ANALYTICAL_POSITION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', 'Gonggong', '6AC4721']  # Weywot removed - JPL data works at Quaoar\n                if planet in ANALYTICAL_POSITION_FALLBACK:\n                    from orbital_elements import planetary_params\n",
         b"\n            #    ANALYTICAL_POSITION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', 'Weywot', '6AC4721']\n                ANALYTICAL_POSITION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', '6AC4721']  # Weywot removed - JPL data works at Quaoar; Gonggong removed 2026-10-23 (L-470): no failure on record; the maintenance run is the test\n                if planet in ANALYTICAL_POSITION_FALLBACK:\n                    from orbital_elements import planetary_params\n"),
        (b"    # These TNO moons have no usable JPL parent-centered ephemeris\n#    SKIP_HORIZONS_PREFETCH = ['MK2', 'Xiangliu', 'Vanth', 'Weywot']\n    SKIP_HORIZONS_PREFETCH = ['MK2', 'Xiangliu', 'Vanth', 'Gonggong']  # Weywot removed - JPL data works at Quaoar\n\n    # Filter objects that need osculating elements\n",
         b"    # These TNO moons have no usable JPL parent-centered ephemeris\n#    SKIP_HORIZONS_PREFETCH = ['MK2', 'Xiangliu', 'Vanth', 'Weywot']\n    SKIP_HORIZONS_PREFETCH = ['MK2', 'Xiangliu', 'Vanth']  # Weywot removed - JPL data works at Quaoar; Gonggong removed 2026-10-23 (L-470): no failure on record; the maintenance run is the test\n\n    # Filter objects that need osculating elements\n"),
        (b"                # These TNO moons have no usable JPL parent-centered ephemeris\n        #        SKIP_HORIZONS_TRAJECTORY = ['MK2', 'Xiangliu', 'Vanth', 'Weywot']\n                SKIP_HORIZONS_TRAJECTORY = ['MK2', 'Xiangliu', 'Vanth', 'Gonggong']  # Weywot removed - JPL data works at Quaoar\n                \n                for obj in selected_objects:\n",
         b"                # These TNO moons have no usable JPL parent-centered ephemeris\n        #        SKIP_HORIZONS_TRAJECTORY = ['MK2', 'Xiangliu', 'Vanth', 'Weywot']\n                SKIP_HORIZONS_TRAJECTORY = ['MK2', 'Xiangliu', 'Vanth']  # Weywot removed - JPL data works at Quaoar; Gonggong removed 2026-10-23 (L-470): no failure on record; the maintenance run is the test\n                \n                for obj in selected_objects:\n"),
        (b"                # Fallback for objects without JPL ephemeris (e.g., MK2, 6AC4721)\n            #    ANALYTICAL_POSITION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', 'Weywot', '6AC4721']\n                ANALYTICAL_POSITION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', 'Gonggong', '6AC4721']  # Weywot removed - JPL data works at Quaoar\n                if obj_data is None and obj['name'] in ANALYTICAL_POSITION_FALLBACK:\n                    from orbital_elements import planetary_params\n",
         b"                # Fallback for objects without JPL ephemeris (e.g., MK2, 6AC4721)\n            #    ANALYTICAL_POSITION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', 'Weywot', '6AC4721']\n                ANALYTICAL_POSITION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', '6AC4721']  # Weywot removed - JPL data works at Quaoar; Gonggong removed 2026-10-23 (L-470): no failure on record; the maintenance run is the test\n                if obj_data is None and obj['name'] in ANALYTICAL_POSITION_FALLBACK:\n                    from orbital_elements import planetary_params\n"),
        (b"    # These TNO moons have no usable JPL parent-centered ephemeris\n#    SKIP_HORIZONS_PREFETCH = ['MK2', 'Xiangliu', 'Vanth', 'Weywot']\n    SKIP_HORIZONS_PREFETCH = ['MK2', 'Xiangliu', 'Vanth', 'Gonggong']  \n\n    pre_fetch_objects = [\n",
         b"    # These TNO moons have no usable JPL parent-centered ephemeris\n#    SKIP_HORIZONS_PREFETCH = ['MK2', 'Xiangliu', 'Vanth', 'Weywot']\n    SKIP_HORIZONS_PREFETCH = ['MK2', 'Xiangliu', 'Vanth']  # Gonggong removed 2026-10-23 (L-470): no failure on record; the maintenance run is the test\n\n    pre_fetch_objects = [\n"),
        (b"\n                #        ANALYTICAL_ANIMATION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', 'Weywot', '6AC4721']  # Objects without usable JPL ephemeris\n                        ANALYTICAL_ANIMATION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', 'Gonggong', '6AC4721']  # Weywot removed - JPL data works at Quaoar\n\n                        if obj['name'] in ANALYTICAL_ANIMATION_FALLBACK:\n",
         b"\n                #        ANALYTICAL_ANIMATION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', 'Weywot', '6AC4721']  # Objects without usable JPL ephemeris\n                        ANALYTICAL_ANIMATION_FALLBACK = ['MK2', 'Xiangliu', 'Vanth', '6AC4721']  # Weywot removed - JPL data works at Quaoar; Gonggong removed 2026-10-23 (L-470): no failure on record; the maintenance run is the test\n\n                        if obj['name'] in ANALYTICAL_ANIMATION_FALLBACK:\n"),
    ]},
    {"path": 'period_fetch.py', "edits": [
        (b'an entry with a helio_id is fetched by it, as a small body, as plotting\'s\npre-fetch now does around the Sun and as the export serves it.)\n"""\n\n',
         b'an entry with a helio_id is fetched by it, as a small body, as plotting\'s\npre-fetch now does around the Sun and as the export serves it.)\nModule updated: October 23, 2026 with Anthropic\'s Claude Opus 5.5 (L-470:\nGonggong comes off SKIP_NAMES with palomas_orrery.py\'s two pre-fetch\nlists, so its period is fetched, around the Sun by its helio_id, 2007\nOR10, and the Horizons check confirms it.)\n"""\n\n'),
        (b'# never asks. Copied, and held to the source by test_period_fetch.py.\nPLOTTED_TYPES = ("orbital", "satellite", "trajectory", "lagrange_point")\nSKIP_NAMES = ("MK2", "Xiangliu", "Vanth", "Gonggong")\n\nREAD_FIELDS = ("name", "key", "id", "id_type", "object_type", "is_mission",\n',
         b'# never asks. Copied, and held to the source by test_period_fetch.py.\nPLOTTED_TYPES = ("orbital", "satellite", "trajectory", "lagrange_point")\n# Gonggong came off both copies on 2026-10-23 (L-470): no failure was on\n# record, and the maintenance run is the test (Tony: "just take it off the\n# skip list and see if it fails").\nSKIP_NAMES = ("MK2", "Xiangliu", "Vanth")\n\nREAD_FIELDS = ("name", "key", "id", "id_type", "object_type", "is_mission",\n'),
    ]},
    {"path": 'LEDGER_CONSOLIDATED.md', "edits": [
        (b'the same path plan), built on b90d895 and gallery 25e4d24 with patches\nL472_1 and L472_2.\nReview and RICE update Tony 6-21-2026\n\n',
         b"the same path plan), built on b90d895 and gallery 25e4d24 with patches\nL472_1 and L472_2.\nModule updated: October 23, 2026, evening, with Anthropic's Claude Opus\n5.5 (L-470: Gonggong off the six skip lists and SKIP_NAMES, the\nmaintenance run the test, by Tony's ruling in the coordination note),\nbuilt on b90d895 with patches L472_2 and L472_3.\nReview and RICE update Tony 6-21-2026\n\n"),
        (b"  (`documentation/HANDOFF_L443_view_and_drawer_brief_20261023.md`,\n  sec. 3, item 5).\n**Gap (replaces the one below, 2026-10-22, evening):** the Gonggong test,\nby the skill's method, in a session and on Tony's orrery.\n**Gap (superseded above):** a plot of Gonggong around\n",
         b'  (`documentation/HANDOFF_L443_view_and_drawer_brief_20261023.md`,\n  sec. 3, item 5).\n- **2026-10-23, evening: discussed and ruled.** In the coordination\n  session (`documentation/COORD_L470_gonggong_ruling_20261023.md`), Tony: "I\'m not\n  aware of any problem." and "Yes, or just take it off the skip list\n  and see if it fails." The skip came in with commit c60572d,\n  2026-02-04, beside Weywot\'s comment; nothing records a failure. The\n  test runs through the checks that already exist.\n- **Built 2026-10-23,** `patch_L470_1_gonggong_off_skip_lists_20261023.py`:\n  Gonggong off all six lists in palomas_orrery.py (the two pre-fetch\n  lists, the static trajectory list, the three analytical fallbacks)\n  and off SKIP_NAMES in period_fetch.py, each with a dated comment.\n  Checked in the sandbox, which cannot reach JPL: the period fetch\'s\n  suite passes 36 of 36 and goes red, naming both lists, with only one\n  side changed; the period fetch on a throwaway copy lists Gonggong as\n  the one body missing a fetched period and asks 2007 OR10 around the\n  Sun, saving nothing (UNREACHABLE); the orrery starts headlessly.\n**Gap (replaces the one below, 2026-10-23, evening):** Tony\'s maintenance\nrun: Period fetch and Horizons check answer for Gonggong, or name the\nfailure (then Discard Changes, and the skip goes back with its comment:\nrecord, centre, date); one look in the orrery with Gonggong as the\ncentre; then the website\'s Daily Run pulls the fetched period, and\nL-470\'s Gonggong instance closes.\n**Gap (superseded above):** the Gonggong test,\nby the skill\'s method, in a session and on Tony\'s orrery.\n**Gap (superseded above):** a plot of Gonggong around\n'),
    ]},
    {"path": 'documentation/WHERE_WE_ARE.md', "edits": [
        (b'>\n> **Needs you now:**\n> - *(do) Patch 1 on the website; patches 2 and 3 on the orrery, in\n>   order; the runs and pushes; then your phone look.*\n> - Two papers left to try (`READING_L456_tony_20261021.md`).\n\n',
         b'>\n> **Needs you now:**\n> - *(do) Patch 1 on the website; patches 2, 3 and L470_1 on the\n>   orrery, in order; the runs and pushes; then your phone look.*\n> - Two papers left to try (`READING_L456_tony_20261021.md`).\n\n'),
        (b'- Paths: one rule, planned in the orrery; nearest approaches place the\n  fine steps; solid to today, dashed after. (Oct 23)\n\n## Deferred\n',
         b'- Paths: one rule, planned in the orrery; nearest approaches place the\n  fine steps; solid to today, dashed after. (Oct 23)\n- Gonggong off the skip lists; the maintenance run is its test. (Oct 23)\n\n## Deferred\n'),
        (b'\nAt the next design talk:\n- "Gonggong skipped but needs discussion" (your run record, Oct 22;\n  L-470 (entries the website cannot serve)).\n- The Daily Run checking the orrery it pulled is the one you pushed\n  (L-461 (pull matches push)): not built with slice 1; with slice 2.\n',
         b'\nAt the next design talk:\n- The Daily Run checking the orrery it pulled is the one you pushed\n  (L-461 (pull matches push)): not built with slice 1; with slice 2.\n'),
    ]},
]

# Patch 3 must have run: its stamp line in the ledger.
REQUIRES = ('LEDGER_CONSOLIDATED.md', b"5.5 (slice 2's design talk: its rulings on L-443, the record")


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    root = os.getcwd()
    req_path, req_text = REQUIRES
    rp = os.path.join(root, req_path)
    if os.path.exists(rp) and req_text not in open(rp, "rb").read().replace(b"\r\n", b"\n"):
        fail("patch_L472_3_slice2_design_20261023.py has not run yet. Run "
             "patch_L472_2 and patch_L472_3 first, then this one")
    plan = []
    for f in FILES:
        path = os.path.join(root, f["path"])
        if not os.path.exists(path):
            fail("%s not found. Run this from the repository's root folder"
                 % f["path"])
        raw = open(path, "rb").read()
        crlf = b"\r\n" in raw
        lf = raw.replace(b"\r\n", b"\n")
        if all(lf.count(old) == 0 and lf.count(new) >= 1
               for old, new in f["edits"]):
            fail("%s already carries this patch's edits; it has run before"
                 % f["path"])
        spots = []
        for k, (old, new) in enumerate(f["edits"]):
            n = lf.count(old)
            if n != 1:
                fail("ANCHOR FAIL in %s, edit %d: expected 1 match, found %d: %r"
                     % (f["path"], k + 1, n, old[:70]))
            spots.append((lf.index(old), old, new))
        spots.sort()
        out, last = b"", 0
        for i, old, new in spots:
            if i < last:
                fail("%s: two edits overlap" % f["path"])
            out += lf[last:i] + new
            last = i + len(old)
        out += lf[last:]
        plan.append((f, path, out, crlf))
    for f, path, out, crlf in plan:
        open(path, "wb").write(out)
        print("ok  %s (%d edits%s)" % (f["path"], len(f["edits"]),
              "; it was CRLF in the working copy, written LF" if crlf else ""))
    print("patch applied: %s (%d files)" % (TITLE, len(plan)))


if __name__ == "__main__":
    main()
