#!/usr/bin/env python3
"""
patch_L363_ledger_solar_system_room_20260926.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
palomas_orrery.py), open it in VS Code and click Run.

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 907436a80ebf1c6d4b0dbcc0fc7da2ceed721ed6
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 8545cbd7d34b98f1de5ff93615c5da5e3e5b75c3
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

It adds five items to LEDGER_CONSOLIDATED.md, section A, above L-362:

  L-363  The Solar System room: Tony's rulings, Half 1 as shipped at
         gallery 8545cbd7, and what Half 2 still has to do.
  L-364  A comet's own trust window can exclude today while the served
         window passes the scene (Halley, Encke).
  L-365  The assembler leaves out a body it cannot draw, without a
         warning (Voyager 1).
  L-366  An orbit's info marker describes an arbitrary point on the
         orbit.
  L-367  No checker opens a new room.

It changes no existing item.

IF IT REFUSES because the ledger moved: the parallel Stage D session
may have filed its own rows first and taken these handles. Tell Claude;
the rows are rebuilt on the new ledger with the next free handles.

RUN THE LEDGER INDEX AFTERWARDS: python ledger_index.py. This patch does
not touch the INDEX zone and does not fingerprint it.

SUCCESS looks like: one "ok" line, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written September 26, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"

# Fingerprinted OUTSIDE the INDEX zone, which ledger_index.py
# regenerates (safe-file-editing, A Guard Must Not Fence What a
# Generator Rewrites).
BASE_OUTSIDE_INDEX = "044339bcffcbf89ef9c542c2ca5fa4b8"

INDEX_START = "<!-- INDEX:START"
INDEX_END = "<!-- INDEX:END -->"

EDITS = [("#### [L-362] The master plan's two summaries are a month behind the plan (documentation)\n", '#### [L-367] No checker opens a new room (checks, gallery)\n<!-- L:367 status:OPEN upd:2026-09-26 section:A flag: rice: -->\n- **Found 2026-09-26** delivering L-363. The gallery maintenance run\n  passed 16 of 16 on the patched copy, and none of its checkers boots a\n  room from the page\'s `EXHIBITS` table. They read recorded payloads\n  (`payload_earth_scene.json`, `payload_earth.json`,\n  `payload_jupiter_saturn.json`) or the served cache, and Arrival says\n  so in its own words: "both rooms". So the 16 said the patch broke\n  nothing else, not that the new room works. The room\'s checks were a\n  headless run in the session and Tony\'s phone.\n- A class, not an instance: Jupiter\'s and Saturn\'s rooms will enter the\n  same blind spot.\n- Related, for Claude sessions: the Solar System Explorer cannot be\n  rendered headless in the sandbox, because it needs Pyodide\'s numpy,\n  which the sandbox cannot fetch. The exhibit rooms need only the\n  standard library and can be.\n**Gap:** A check that lists `EXHIBITS` and fails on a room no checker boots, or one smoke that boots every room.\n**Ref:** gallery `gallery_maintenance_run.py`; gallery `documentation/smoke_*.js`; L-363.\n\n#### [L-366] An orbit\'s info marker describes an arbitrary point on the orbit (gallery, assembler)\n<!-- L:366 status:OPEN upd:2026-09-26 section:A flag: rice: -->\n- **Found 2026-09-26** building L-363, at gallery `a5c35f5f`.\n  `render_orbits.build_orbit_traces` puts each orbit\'s single info\n  marker at the 11th of its sampled points (`idx = min(10, n - 1)`),\n  and its hover gives that point\'s distance and coordinates, labelled\n  only "(osculating orbit)". It is true of that point, and the point\n  means nothing. Every osculating orbit the assembler draws carries one,\n  the golden artifacts included.\n- In the Solar System room the page\'s text box pinned to it, so naming\n  Earth read "r = 0.982514 AU" while Earth was at 1.002730 AU. Fixed in\n  that room only: the room names each body\'s position marker as the\n  box\'s target (`meta.label_target`, read by `sunLabelMarker`). The\n  cross itself is still drawn.\n**Gap:** Decide what the orbit\'s info marker is for -- a named point, such as perihelion, with its name in the hover, or orbit facts only -- then change `render_orbits.py` once.\n**Ref:** gallery `gallery/assembler/render_orbits.py`; gallery `interactive.html::sunLabelMarker`; L-363.\n\n#### [L-365] The assembler leaves out a body it cannot draw, without a warning (gallery, assembler)\n<!-- L:365 status:OPEN upd:2026-09-26 section:A flag: rice: -->\n- **Found 2026-09-26** asking for Voyager 1 in L-363, at gallery\n  `a5c35f5f`. `assemble_scene` draws only objects that carry an\n  osculating block. Anything else -- Voyager 1 is served as positions,\n  frame `arc-natural` -- is skipped with no trace and no warning.\n  `render_spacecraft.py` is a placeholder that raises\n  NotImplementedError until artifact 5.\n- The Solar System room guards itself: its compose counts one position\n  marker per body it asks for and reports a miss in the info panel. The\n  assembler still does not, for any other caller.\n**Gap:** `assemble_scene` warns, or refuses, for every requested object it does not draw; Voyager 1 waits for `render_spacecraft` (artifact 5).\n**Ref:** gallery `gallery/assembler/assemble.py`; `gallery/assembler/render_spacecraft.py`; L-363.\n\n#### [L-364] A comet\'s own trust window can exclude today while the served window passes the scene (gallery, trust)\n<!-- L:364 status:OPEN upd:2026-09-26 section:A flag: rice: -->\n- **Found 2026-09-26** building L-363, at gallery `a5c35f5f`. Each\n  heliocentric object\'s trust record carries its own window, centred on\n  its element epoch. Halley\'s (anchored at its 1986 perihelion, capped\n  at half its period) ends JD 2460350.6, February 2024. Encke\'s ends JD\n  2460843.5, June 2025. Both exclude today.\n- The cache\'s global `served_window` is built in\n  `tools/gallery_cache_builder.py` from the SHORTEST window\'s LENGTH\n  (`window_days`, Apophis\'s today), centred on the build time. It does\n  not look at where each object\'s window falls, and `resolver.py`\n  checks a scene\'s date only against that global window. So a scene of\n  today with a comet in it passes, and draws a position the comet\'s own\n  trust record does not vouch for: a check that passes while blind.\n- Nothing served draws a comet today. L-363 left both out for this\n  reason.\n- Tony, 2026-09-26: the trust window will need changes once the\n  encounter work starts; not today.\n**Gap:** The scene date checked against each drawn object\'s own window, or a served window built from where the windows fall; taken up with the encounter work.\n**Ref:** gallery `tools/gallery_cache_builder.py` (served_window, M2 section 5.5); gallery `gallery/assembler/resolver.py`, step 3; skills/gallery-assembler/SKILL.md; L-363.\n\n#### [L-363] The Solar System room: the bodies as symbols, before their shells (gallery, exhibits)\n<!-- L:363 status:OPEN upd:2026-09-26 section:A flag: rice: -->\n- **What it is.** A third room in `interactive.html`,\n  `?exhibit=solar-system`, titled "The Solar System". It draws the\n  bodies as their symbols on their orbits, from the served cache, on\n  today\'s date, with no shells. Tony, 2026-09-26: symbols first, the\n  way the orrery itself grew, as a quick win while each body\'s shells\n  wait for its own room. It is the top level L-286\'s drill-down needs.\n- **Tony\'s rulings, 2026-09-26:**\n  - Two halves, because L-322 Stage D shares `data/objects_config.json`\n    and the cache rebuild. Half 1 touches only `interactive.html`.\n    Half 2 waits for L-322\'s manifest section 6 to push.\n  - Plan B for the key: `solar-system` is permanent. The Explorer keeps\n    `solar-system-explorer` and stays the default until Half 2 and\n    Tony\'s acceptance; then the default switches, and the Explorer\n    card\'s live link is changed in Studio.\n  - Only bodies the cache stands behind today: the Sun, Earth, Jupiter,\n    Saturn and Apophis. The Moon, Io, Titan and Charon are left out;\n    at this scale each sits on its planet, and they belong in their\n    planets\' rooms.\n  - Today\'s date, the method every room uses (`resolver.py` checks the\n    served window once for the scene). No date control: adding one is\n    a decision for all rooms at once.\n  - The opening view is the rooms\' rule, 1.1 x the largest thing drawn.\n    Claude first cited 25 percent, the static artifacts\' rule, and\n    corrected it before delivery.\n  - Shells are kept out by the room\'s compose using the assembler\'s\n    figure only and building no features. No arrival block.\n- **Half 1 shipped at gallery `8545cbd7`** from\n  `patch_solar_system_room_half1_20260926.py`, built on `a5c35f5f`.\n  The pushed `interactive.html` is byte-identical to the tested file\n  [verified @8545cbd7]. Beyond the plan, naming a body opens its text\n  box at the body, not at its orbit\'s info cross (L-366). Two shared\n  changes that alter nothing in the Sun or Earth rooms, confirmed\n  identical before and after in the headless run: the info panel shows\n  a source when there is no link, and a room can name the marker a\n  text box belongs to. Tony\'s Mode 5 on the phone: "correct for our\n  scope."\n- **Seen in the headless phone run, not ruled:** on an upright phone\n  the in-scene title "Paloma\'s Orrery -- The Solar System" runs under\n  the arrow buttons. For Half 2\'s Mode 5.\n- **Half 2, still to do:**\n  - Mercury, Venus, Mars, Uranus and Neptune in\n    `data/objects_config.json`, and one cache rebuild.\n  - Pluto: a Sun-centred entry for the Pluto system. Pluto is served\n    relative to the Pluto-Charon barycentre, and the assembler refuses,\n    by design, to translate it into a Sun-centred scene.\n  - A link for each body in the config. The panel reads "No link on\n    file for this body" today.\n  - A gallery card for the room, which gives it its L-286 chain.\n  - Tony\'s Mode 5, then **Tony-action (decide):** the default switch.\n  - The comets return with L-364; Voyager 1 with L-365.\n**Gap:** Half 2 (above), after L-322 section 6 pushes; then Tony\'s decision on the default.\n**Ref:** `documentation/HANDOFF_explorer_symbols_half1_20260926.md` (rev 2); gallery `documentation/patch_solar_system_room_half1_20260926.py`; L-286; L-099; L-322; L-364 to L-367.\n\n#### [L-362] The master plan\'s two summaries are a month behind the plan (documentation)\n')]

def split_index(text):
    if INDEX_START in text and INDEX_END in text:
        a = text.index(INDEX_START)
        b = text.index(INDEX_END) + len(INDEX_END)
        return text[:a] + text[b:]
    return text


def fingerprint(data):
    lf = data.replace(b"\r\n", b"\n")
    return hashlib.md5(split_index(lf.decode("utf-8")).encode("utf-8")
                       ).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit(
            "ERROR: run this from the ORRERY repo ROOT, next to "
            "palomas_orrery.py -- not from documentation/. NOTHING was "
            "written.")
    if not os.path.isfile(LEDGER):
        raise SystemExit(
            "ERROR: %s is not here, so this is not the orrery root. "
            "NOTHING was written." % LEDGER)

    with open(LEDGER, "rb") as handle:
        raw = handle.read()
    got = fingerprint(raw)
    if got != BASE_OUTSIDE_INDEX:
        raise SystemExit(
            "ERROR: %s is not the file this patch was built against.\n"
            "       expected %s, found %s.\n"
            "       (The INDEX zone is excluded, so running "
            "ledger_index.py is not the cause.)\n"
            "       NOTHING was written. Undo is Discard Changes in "
            "GitHub Desktop." % (LEDGER, BASE_OUTSIDE_INDEX, got))

    is_crlf = raw.count(b"\r\n") > 0
    text = raw.decode("utf-8")
    applied = []
    for old, new in EDITS:
        o = old.replace("\n", "\r\n") if is_crlf else old
        n = text.count(o)
        if n != 1:
            raise SystemExit(
                "ANCHOR FAIL: expected 1 match in %s, found %d:\n  %r\n"
                "NOTHING was written." % (LEDGER, n, old[:70]))
        text = text.replace(o, new.replace("\n", "\r\n") if is_crlf else new)
        applied.append(old.strip().split("\n")[0][:56])

    with open(LEDGER, "wb") as handle:
        handle.write(text.encode("utf-8"))

    for line in applied:
        print("ok  %-24s %s" % (LEDGER, line))
    print("")
    print("patch applied (%d edits)" % len(EDITS))
    print("")
    print("NEXT:")
    print("  1. python ledger_index.py")
    print("  2. python orrery_maintenance_run.py")
    print("  3. Move this script into documentation/. Replace")
    print("     documentation/HANDOFF_explorer_symbols_half1_20260926.md with")
    print("     rev 2 from this chat. Commit and push.")
    print("  4. Tell Claude the new orrery SHA.")


if __name__ == "__main__":
    main()
