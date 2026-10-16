#!/usr/bin/env python3
"""
patch_L401_5_build3_parked_20261015.py -- records that L-401's build 3
(the distance digits: the fly-to buttons, the parameters window, the
animation's uncertainty, the encounters) is parked, not built, and
where each of its four parts opens; corrects the order of Earth's list
(L-413) and stage 5 of the road on Where We Are to match.

Tony's ruling of 2026-10-15, in the coordination session, carried by
this session's close. No code changes.

Built on orrery 45085c4 ("L447 close") at
https://github.com/tonylquintanilla/palomas_orrery; the gallery read at
95713f4 ("daily run again") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and not
touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 15, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L401_5_build3_parked_20261015.py

    Save this file in the ORRERY folder above, open it in VS Code and
    click Run. It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing, in two files

    LEDGER_CONSOLIDATED.md    L-401: the ruling, where each part goes,
                              what the scoping read found, a new Gap;
                              L-413: the order corrected, a new Gap;
                              header stamp
    documentation/WHERE_WE_ARE.md   above the run-record marker only:
                              the date, the box, road stage 5, the
                              marks reset, one Settled line, the
                              signals re-read, three details lines

    Each file is checked only at the lines edited, so Tony's notes
    anywhere else are kept.

WHAT IT PRINTS

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = "LEDGER_CONSOLIDATED.md"
WWA = "documentation/WHERE_WE_ARE.md"
MARKER = "--- Your run record below this line"
WWA_CAP = 130


class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError("missing file: %s (is this the orrery folder?)" % rel)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), (b"\r\n" in raw)


def rep(text, old, new, label, log, rel):
    n = text.count(old)
    if n != 1:
        raise PatchError("ANCHOR FAIL [%s %s]: expected 1 match, got %d: %r"
                         % (rel, label, n, old[:70]))
    log.append("ok  %-34s %s" % (rel, label))
    return text.replace(old, new)


# ---------------------------------------------------------------- ledger

DONE_MARK = "- **2026-10-15, build 3 parked, not built**"

LEDGER_EDITS = [
    ("L-401 date",
     "<!-- L:401 status:OPEN upd:2026-10-13 section:A flag: rice: -->",
     "<!-- L:401 status:OPEN upd:2026-10-15 section:A flag: rice: -->"),

    ("L-401 build 3 parked, and its Gap",
     """**Gap:** Builds 1 and 2 are built and accepted. Left, build 3: the fly-to buttons, the parameters window, the
animation's 2xr; and the encounter slice (`spacecraft_encounters.py`,
`close_approach_data.py`). The two questions above go to the design
talk.
""",
     """- **2026-10-15, build 3 parked, not built** (Tony's ruling of
  2026-10-15, in the coordination session; carried by the build
  session's close, `patch_L401_5_build3_parked_20261015.py`). The
  build session read the code at ffd6c36 and proposed build 3's scope;
  Tony: "no. we got ahead." By the braid, none of its four parts is
  drawn in the Sun or Earth rooms on the website, so each part opens
  with its feature:
  - the fly-to buttons (`visualization_utils.add_fly_to_object_buttons`)
    and the parameters window (`orbital_param_viz.py`): the next time a
    session opens those files;
  - the animation's uncertainty (`palomas_orrery_helpers.fetch_trajectory`
    does not ask for 2xr): with "choosing a date, and animation" (Where
    We Are, waiting on Tony, not urgent);
  - the encounters (`spacecraft_encounters.py`, `close_approach_data.py`):
    with road stage 12, encounters.
  Nothing was built. No code file changed.
- **What the scoping read found, for whichever part opens first**
  (read at ffd6c36; recorded, not chased):
  - Fly-to buttons: the label prints ".0f km", ".3f AU" or ".2f AU",
    and the dropdown sorts by parsing that label back into a number, so
    a change to the label's digits must keep the sort working.
  - Parameters window: the elements print cut to fixed widths (a to
    3 decimals, e to 6, angles to 1); the distances worked from them
    (periapsis, apoapsis, b, c) and the body's position marker print
    ".3f AU". The fallback "estimate" dates (the plot date plus a
    quarter and three quarters of a period) are still there; removing
    them removes something the orrery already does, so it is asked
    first. The two questions above (a model with no stated accuracy;
    numbers that are not distances) reach this window most.
  - The animation: the Voyagers' sheet figure needs their distance from
    Earth on every frame, a second query per frame; the frames' small
    bodies need only 2xr in the query `fetch_trajectory` already makes.
  - Encounters: the hover re-cuts typed mission figures (Juno's
    21.219 km/s prints 21.22; a typed 10.8 prints 10.80); a distance
    the orrery resolves from Horizons has no stated accuracy. The
    close-approach hover prints nine decimals of an AU beside JPL's own
    3-sigma range from the same record. Where the typed mission figures
    came from is a provenance question of its own.
**Gap:** Builds 1 and 2 are built and accepted. Build 3 is parked
(2026-10-15): each of its four parts opens with its feature, as above.
The two questions above go to the design talk.
"""),

    ("L-413 date",
     "<!-- L:413 status:OPEN upd:2026-10-11 section:A flag: rice: -->",
     "<!-- L:413 status:OPEN upd:2026-10-15 section:A flag: rice: -->"),

    ("L-413 order corrected, and its Gap",
     """**Gap:** L-401 first; then L-421's check; then the design talks in the
order above.
""",
     """- **2026-10-15, the order corrected** (Tony's ruling in the
  coordination session of 2026-10-15): L-401's build 3 is parked, each
  part with its feature (L-401 records where), and L-445 (Earth's
  period from the Earth-Moon barycentre) is first on this list.
**Gap:** L-445 (Earth's period) first; then the rest of L-421's checks
(its Gap: parts 2 and 3); then the design talks in the order above.
"""),

    ("header stamp",
     "Review and RICE update Tony 6-21-2026\n",
     """Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5
(L-401 build 3 parked, each part with its feature, Tony's ruling;
L-413's order corrected: L-445 first), built on 45085c4.
Review and RICE update Tony 6-21-2026
"""),
]

# --------------------------------------------------------- where we are

WWA_EDITS = [
    ("header",
     """Last updated: October 15, 2026, night: the front page's words done.
- Written at orrery 464d872 and gallery db63b7d.
""",
     """Last updated: October 15, 2026, late night: L-401 build 3 parked.
- Written at orrery 45085c4 and gallery 95713f4.
"""),

    ("changed since you last read this",
     """> - Done: L-444 (the missing periods): all eight fetched and confirmed.
> - Ruled: L-445 (Earth's period) and L-446 (the daily run's order).
> - Done: the front page says what the site is: L-447 (its words).
""",
     """> - Parked: L-401 build 3 (the distance digits), your ruling of Oct 15:
>   each part waits for its feature. Earth's list now starts at L-445.
"""),

    ("needs you now",
     """> - *Run patch_L447_3_close; one Daily Run clears Cache in step.*
""",
     """> - *Run patch_L401_5, then the maintenance run; commit; push.*
"""),

    ("road stage 5",
     """  5.   [NOW]   L-401 (the distance digits): builds 1 and 2 accepted;
               build 3 later. Then Earth's remaining items.
""",
     """  5.   [NOW]   *Earth's list (L-413): L-445 (Earth's period, stage 8b),
               then the rest of L-421's checks (stage 6), then Earth's
               design talks.*  << moved this session
"""),

    ("road 8b mark reset",
     """               not Earth's centre.*  << new this session
""",
     """               not Earth's centre.*
"""),

    ("road 8c mark reset",
     """               orrery's checked data before it builds.  << new this session
""",
     """               orrery's checked data before it builds.
"""),

    ("road 11 mark reset",
     """               Earth rooms close.  << moved this session
""",
     """               Earth rooms close.
"""),

    ("settled line",
     """Standing rulings. A line leaves after a few weeks, once it is habit.
""",
     """Standing rulings. A line leaves after a few weeks, once it is habit.
- L-401 build 3 parked: fly-to buttons, parameters window when next
  opened; animation with choosing a date; encounters, stage 12. (Oct 15)
"""),

    ("signals re-read",
     """- Last cache build: 20261015T153610Z, ok, no retry (gallery 9f8569e).
- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 9579fcd).
""",
     """- Last cache build: 20261016T021807Z, ok, no retry (gallery 95713f4).
- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 45085c4).
"""),

    ("waiting-on-you mark reset",
     "## Waiting on you  **>> UPDATED THIS SESSION**\n",
     "## Waiting on you\n"),

    ("details: last session's line out",
     """- This session, last: `HANDOFF_L447_front_page_words_20261015.md`
""",
     ""),

    ("details: build 3 on the distance-digits line",
     """  `HANDOFF_L401_distance_build1_20261012.md`
""",
     """  `HANDOFF_L401_distance_build1_20261012.md`; build 3 parked: L-401.
"""),

    ("details: L-421 line, which repeats stage 6",
     """- Every item: `LEDGER_CONSOLIDATED.md`. Open for build: L-421 (the
  typed facts), its check.
""",
     """- Every item: `LEDGER_CONSOLIDATED.md`.
"""),
]


def main():
    log = []
    try:
        led, led_crlf = read(LEDGER)
        if DONE_MARK in led:
            raise PatchError("L-401 already records build 3 parked; this "
                             "patch has run")
        for label, old, new in LEDGER_EDITS:
            led = rep(led, old, new, label, log, LEDGER)

        wwa, wwa_crlf = read(WWA)
        if wwa.count(MARKER) != 1:
            raise PatchError("ANCHOR FAIL [%s run-record marker]" % WWA)
        cut = wwa.index(MARKER)
        top, bottom = wwa[:cut], wwa[cut:]
        for label, old, new in WWA_EDITS:
            top = rep(top, old, new, label, log, WWA)
        above = top.count("\n")
        if above > WWA_CAP:
            raise PatchError("%s would stand %d lines above the marker (cap %d)"
                             % (WWA, above, WWA_CAP))
        log.append("ok  %s: %d lines above the marker (cap %d)"
                   % (WWA, above, WWA_CAP))
        wwa = top + bottom

        out = {LEDGER: (led, led_crlf), WWA: (wwa, wwa_crlf)}
        for rel, (text, _c) in out.items():
            bad = sum(1 for ch in text if ord(ch) > 127)
            if bad:
                raise PatchError("%s: %d non-ASCII character(s)" % (rel, bad))
    except PatchError as exc:
        print("ERROR: %s" % exc)
        print("NOTHING was written.")
        sys.exit(1)

    notes = []
    for rel, (text, crlf) in out.items():
        with open(os.path.join(ROOT, rel), "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf:
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % rel)
    for line in log + notes:
        print(line)
    print("stamps updated: the ledger's header; L-401's and L-413's dates; "
          "Where We Are's date")
    print("patch applied (2 files)")
    print("")
    print("NEXT:")
    print("  1. Move this script into documentation/; then run")
    print("     orrery_maintenance_run.py (it rebuilds the ledger's index);")
    print("     commit and push the orrery.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
