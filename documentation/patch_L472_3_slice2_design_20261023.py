r"""patch_L472_3_slice2_design_20261023.py -- slice 2's design record and
its ledger lines: the seven rulings of Tony's design talk of Oct 23 (the
spacecraft and the comets on open paths), L-476 new (the orrery's plots
by the same path plan), L-443 and Where We Are.

RUN COMMAND
    python patch_L472_3_slice2_design_20261023.py

Save it in the ORRERY repository's root folder
(C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\),
open it in VS Code and click Run. Then move it to documentation/,
commit and push. No maintenance run is needed.

RUN IT AFTER patch_L472_2_records_20261023.py, which it builds on. If
patch 2 has not run, this one says so and writes nothing.

Built on orrery b90d895a4ef1cdc31daec7a20fef8c34369fa24c at
https://github.com/tonylquintanilla/palomas_orrery (branch main) with
patch_L472_2 applied, and gallery
25e4d24228a191622df68b447f519782162977ea at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Final as
delivered: nothing will replace it.

WHAT IT CHANGES (records only; no code)
    documentation/DESIGN_L443_slice2_rulings_20261023.md  NEW: the seven
                                rulings in Tony's words, what was measured
                                to put them, the method left to the build,
                                and the three Settled lines today's patches
                                took off Where We Are
    LEDGER_CONSOLIDATED.md      header stamp; L-476 new; L-443, slice 2
                                designed, and its Gap
    documentation/WHERE_WE_ARE.md  header, box, Settled (slice 2's line in,
                                the Oct 18-19 line out for the length cap).
                                The run-record zone is not touched

The design record is written only to this patch; it was not handed to
you separately, so there is no copy of it to delete first.

SUCCESS prints one "ok" line per file, then "patch applied".
FAILURE prints one FAILURE line, and NOTHING is written; undo is
Discard Changes in GitHub Desktop.

Written October 23, 2026 with Anthropic's Claude Opus 5.5.

Role: devtool
Domain: dev_tools
"""

import os
import sys

TITLE = 'L-443 slice 2 design'
FILES = [
    {"path": 'LEDGER_CONSOLIDATED.md', "edits": [
        (b"count line, built with L-474 and L-475 in gallery patch_L472_1; L-473\nparked; L-443's Gap), built on b90d895 and gallery 25e4d24.\nReview and RICE update Tony 6-21-2026\n\n",
         b"count line, built with L-474 and L-475 in gallery patch_L472_1; L-473\nparked; L-443's Gap), built on b90d895 and gallery 25e4d24.\nModule updated: October 23, 2026, evening, with Anthropic's Claude Opus\n5.5 (slice 2's design talk: its rulings on L-443, the record\nDESIGN_L443_slice2_rulings_20261023.md; L-476 new, the orrery's plots by\nthe same path plan), built on b90d895 and gallery 25e4d24 with patches\nL472_1 and L472_2.\nReview and RICE update Tony 6-21-2026\n\n"),
        (b"\n## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n#### [L-475] The About link at the bottom of every room's i panel (gallery, the rooms' shared chrome)\n",
         b'\n## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n#### [L-476] The orrery\'s whole-path plots draw by the same path plan as the website (orrery, spacecraft and comets)\n<!-- L:476 status:OPEN upd:2026-10-23 section:A flag: rice: -->\n- **Tony, 2026-10-23, at slice 2\'s design talk** (`documentation/DESIGN_L443_slice2_rulings_20261023.md`):\n  "if there are better approaches for the orrery maybe we can implement\n  them there also so the two are as Consistent as possible." And, on\n  drawing the part after today dashed: "But the orrery does not do this\n  today."\n- Today the orrery\'s ordinary plot spreads an even count of points\n  across a spacecraft\'s dates (palomas_orrery.py,\n  `create_dates_list_for_object`); the curvature rule serves only its\n  encounter views (spacecraft_encounters.py,\n  `_calculate_encounter_resolution`).\n- The change: the orrery\'s whole-path plots fetch and draw by the plan\n  slice 2 makes and serves (a backbone thinned where straight, fine\n  steps around each nearest approach or perihelion), solid to today and\n  dashed after. A change to plotting, so the five parallel consumers\n  are mapped first (Check All Parallel Pipelines), and it is judged by\n  Tony\'s eyes on its own.\n**Gap:** after slice 2\'s build: the design of the change in the\norrery\'s plots, then the build.\n**Ref:** L-443; `documentation/DESIGN_L443_slice2_rulings_20261023.md`, rulings 2 and 6;\n`spacecraft_encounters.py`; `palomas_orrery.py`.\n\n#### [L-475] The About link at the bottom of every room\'s i panel (gallery, the rooms\' shared chrome)\n'),
        (b"  About line built in gallery patch_L472_1 (L-472, L-474, L-475);\n  L-473 parked, the drawer already opening groups unticked.\n**Gap (replaces the one below, 2026-10-23, afternoon):** Tony's runs of\npatch_L472_1 and his phone look; then slice 2, the spacecraft and the\nopen-path comets.\n",
         b"  About line built in gallery patch_L472_1 (L-472, L-474, L-475);\n  L-473 parked, the drawer already opening groups unticked.\n- **2026-10-23, evening: slice 2 designed,** from Tony's phone. Seven\n  rulings, in his words in `documentation/DESIGN_L443_slice2_rulings_20261023.md`:\n  one path rule, the orrery's (a backbone thinned where straight, fine\n  steps around each event), its plan made in the orrery and served;\n  the first set the twelve spacecraft still flying among the planets,\n  with the 14 open-path comets; an event placed by the nearest\n  approach found in JPL's positions, a sourced date only extra words;\n  a flyby later in the room of the body flown past, its sharply\n  curving part and nearest approach or approaches; solid to today,\n  dashed after, for spacecraft and comets alike, the future part\n  JPL's own plan or prediction; that part fetched again on the 30-day\n  cycle. The orrery's own plots follow on L-476.\n- **Carried for the build:** gallery `render_orbits.py`'s comment that\n  a 3D line cannot be dashed is wrong (Plotly 2.35.2's schema gives\n  six dash styles); corrected when slice 2 opens the file.\n**Gap (replaces the one below, 2026-10-23, evening):** Tony's runs of\npatch_L472_1 and patch_L472_2 and his phone look; then slice 2's\nbuild, by `documentation/DESIGN_L443_slice2_rulings_20261023.md`.\n**Gap (superseded above):** Tony's runs of\npatch_L472_1 and his phone look; then slice 2, the spacecraft and the\nopen-path comets.\n"),
    ]},
    {"path": 'documentation/WHERE_WE_ARE.md', "edits": [
        (b'# Where We Are\n\nLast updated: October 23, 2026, afternoon: Halley was drawn right; a\ncount line, See more on top, the About line built.\n- Written at orrery b90d895 and gallery 25e4d24, with patches 1 and 2.\n\n> **READ THIS FIRST**\n',
         b'# Where We Are\n\nLast updated: October 23, 2026, evening: Halley was drawn right; the\nview and drawer changes built; slice 2 designed.\n- Written at orrery b90d895 and gallery 25e4d24, with patches 1 to 3.\n\n> **READ THIS FIRST**\n'),
        (b'> - Built with it: L-474 (See more on top), L-475 (the About link in\n>   every i panel). L-473 (groups open unticked) parked: they do.\n>\n> **Do next:** *your phone look of the three changes; then slice 2,\n',
         b'> - Built with it: L-474 (See more on top), L-475 (the About link in\n>   every i panel). L-473 (groups open unticked) parked: they do.\n> - Slice 2 is designed: `DESIGN_L443_slice2_rulings_20261023.md`.\n>\n> **Do next:** *your phone look of the three changes; then slice 2,\n'),
        (b'>\n> **Needs you now:**\n> - *(do) Patch 1 on the website and patch 2 on the orrery, the runs\n>   and pushes; then your phone look.*\n> - Two papers left to try (`READING_L456_tony_20261021.md`).\n\n',
         b'>\n> **Needs you now:**\n> - *(do) Patch 1 on the website; patches 2 and 3 on the orrery, in\n>   order; the runs and pushes; then your phone look.*\n> - Two papers left to try (`READING_L456_tony_20261021.md`).\n\n'),
        (b"\nStanding rulings. A line leaves after a few weeks, once it is habit.\n- Every view, still and animated, opens on the farthest thing drawn,\n  shell or orbit, plus 20%; the center body's axis and cone end just\n  past its farthest shell. Kelvin stays. (Oct 18-19)\n- Drawer order: nearest part as drawn from sourced rows. Drawings end\n  where a row says, Earth too. (Oct 21)\n",
         b'\nStanding rulings. A line leaves after a few weeks, once it is habit.\n- Drawer order: nearest part as drawn from sourced rows. Drawings end\n  where a row says, Earth too. (Oct 21)\n'),
        (b'- Zooming in stays a cutout; one line counts the ticked bodies\n  outside the view, never names them. (Oct 23)\n\n## Deferred\n',
         b'- Zooming in stays a cutout; one line counts the ticked bodies\n  outside the view, never names them. (Oct 23)\n- Paths: one rule, planned in the orrery; nearest approaches place the\n  fine steps; solid to today, dashed after. (Oct 23)\n\n## Deferred\n'),
    ]},
]

NEW_FILES = [('documentation/DESIGN_L443_slice2_rulings_20261023.md',
    b'<!-- Doc-Kind: hand | Design record: Tony\'s rulings for L-443 slice 2, the spacecraft and the comets on open paths, with what was measured to put them to him. -->\n# Slice 2 of the objects: the design talk\'s rulings\n\nTony Quintanilla, PE | Claude Opus 5.5 | October 23, 2026\n\nBuilt on orrery b90d895a4ef1cdc31daec7a20fef8c34369fa24c at\nhttps://github.com/tonylquintanilla/palomas_orrery (branch main) and\ngallery 25e4d24228a191622df68b447f519782162977ea at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io (branch\nmain), both read with git ls-remote on Oct 23.\n\nTony\'s local folders: orrery\nC:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\ngallery\nC:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n\nType: DESIGN SESSION (zero code). Held from Tony\'s phone on the\nafternoon of Oct 23, after the view talk (L-472).\n\nCompanion to: `documentation/DESIGN_L443_objects_rulings_20261022.md`\n(slice 1\'s rulings, which sent the spacecraft and the 14 open-path\ncomets to this slice) and `documentation/HANDOFF_L443_slice1_build_20261022.md`,\nsection 6. Supersedes nothing.\n\nSkills the build fires, by name: horizons-orbital-mechanics (nearest\napproaches, which record serves a body, the 30-day cycle),\ngallery-cache-builder (the builder fetching by the plan),\ninteractive-exhibit (the room drawing the paths, the hover words),\ngallery-assembler (the drawn path), provenance-discipline (any typed\ndate or number), safe-file-editing, agentic-pre-test (orrery code).\n\n## 1. The rulings, in Tony\'s words\n\nEach ruling answers a question put to him in the chat, with the\nmeasurements in section 2.\n\n1. **One path rule, the orrery\'s.** Asked whether every path in slice 2\n   should take a coarse backbone, thinned where it runs straight, with\n   fine steps around each event, the window and the step worked out\n   from that event\'s distance and speed, and the events read from the\n   orrery: "Yes, confirmed. Good solution."\n2. **The orrery and the website alike.** "if there are better\n   approaches for the orrery maybe we can implement them there also so\n   the two are as Consistent as possible." Agreed: the orrery works out\n   each path\'s plan once and serves it, as it places the stored\n   drawings; the website\'s builder fetches by it, and the orrery\'s own\n   plot later draws by it. The orrery\'s side is its own ledger item,\n   L-476, after slice 2.\n3. **The first set is group A.** "I agree, A." The twelve spacecraft\n   still flying among the planets (section 2).\n4. **A flyby belongs in the room of the body flown past.** "the\n   respective spacecraft encounters should be included in that body\'s\n   room, so for voyager 1 Jupiter and Saturn for Example." And what the\n   room shows: "The room should show the flyby so basically the high\n   curvature part and nearest approach or approaches if many orbits are\n   involved." For road stages 12 and 13, not this slice.\n5. **The nearest approach places an event; a sourced date is extra.**\n   "Maybe use the nearest approach which is mechanical instead of a\n   sourced date although a sourced date can be added for the hover or\n   info." The nearest approach is found from JPL\'s own positions and\n   needs no citation. A sourced date, where one is added, carries its\n   own citation.\n6. **Solid to today, dashed after, for both.** For the spacecraft: "Yes\n   planned as dashed would be good. But the orrery does not do this\n   today." For the comets too: "One rule for both." The part after\n   today is JPL\'s own: Horizons\' planned trajectory for a spacecraft,\n   as far as the mission\'s plan runs, and its prediction from the\n   fitted orbit for a comet; never a line the website extends (Tony:\n   "Is the predicted served by JPL not a line projection right?").\n7. **The future part is fetched again on the 30-day cycle.** "Yes and a\n   30-day check for updates sounds right and fits our method."\n\n## 2. What was measured to put them\n\nRead on Oct 23 at the SHAs above, not run unless it says so.\n\n- **The orrery\'s 27 spacecraft** (celestial_objects.py, ids starting\n  with "-"), none with a \'key\', so none is exported to the website.\n  Voyager 1 is on the website from before the export existed.\n- **Group A, twelve, still flying among the planets:** Voyager 1,\n  Voyager 2, New Horizons, Juno, Lucy, JUICE, Psyche, Clipper (Europa\n  Clipper), BepiColombo, SolO (Solar Orbiter), Parker, OSIRISAPE\n  (OSIRIS-APEX).\n- **Group B, near Earth, for the Earth room later:** JamesWebb, Gaia,\n  SOHO, Artemis II.\n- **Group C, ended, for when a date can be chosen:** Pioneer 10,\n  Pioneer 11, Galileo, Cassini, Rosetta, Akatsuki, DART, Hayabusa2,\n  OSIRISREx, MarsRover, Apollo 11 S-IVB.\n- **The 14 comets on open or barely closed paths** (slice 1\'s rulings,\n  section 2): Tsuchinshan, ATLAS (C/2024 G3), West, McNaught, C/2025\n  K1 and fragments B, C, D, PANSTARRS (C/2025 R3), Borisov (C/2025\n  V1), 1I/Oumuamua, 2I/Borisov, 3I/ATLAS, Wierzchos.\n- **Flybys on record** (spacecraft_encounters.py, SPACECRAFT_ENCOUNTERS):\n  three spacecraft. New Horizons (Jupiter Gravity Assist, Pluto Flyby,\n  Arrokoth Flyby), Psyche (Mars Gravitational Assist, Flyby of\n  Phobos), Artemis II (Earth Departure (TLI), Lunar Closest Approach,\n  Reentry & Splashdown), each with dist_km and v_kms.\n- **The orrery\'s curvature rule** (spacecraft_encounters.py,\n  `_calculate_encounter_resolution`): the step is the time to travel\n  half a circle at the flyby distance and speed, over about 30 points,\n  snapped to a Horizons step; the window is one and a half times the\n  time to cross four flyby distances either side. It serves the\n  encounter views only.\n- **The orrery\'s whole-path plot** (palomas_orrery.py,\n  `create_dates_list_for_object`): an even count of points across the\n  object\'s dates, the count set in the GUI.\n- **The orrery\'s close-pass orbit from elements** (idealized_orbits.py,\n  `plot_hyperbolic_osculating_orbit`): points densest at closest\n  approach, spreading toward the open ends.\n- **The website\'s Voyager 1** (gallery data/objects_config.json and\n  tools/gallery_cache_builder.py): a point every 7 days from launch,\n  thinned by Douglas-Peucker at 0.02 AU where the path runs straight;\n  daily points inside two flyby windows typed into the config with no\n  source (1979-02-15 to 03-25 and 1980-10-25 to 11-25); 223 points\n  served; each night appends the last 8 days, one small query.\n- **Dashed lines can be drawn.** Plotly 2.35.2\'s own schema, read from\n  the shipped bundle: scatter3d `line.dash` takes dash, dashdot, dot,\n  longdash, longdashdot and solid. The comment in gallery\n  `gallery/assembler/render_orbits.py`, `build_orbit_traces` ("scatter3d\n  line has no \'dash\' attribute (2D-only)") is wrong; corrected when\n  slice 2 opens that file. How a dashed line looks on the phone is\n  Tony\'s to judge.\n\n## 3. For the build session: method, not rulings\n\nThese are how the work is done, decided by the skills (the protocol\'s\nMethod Belongs to the Skill); a case a rule cannot express comes back to\nTony.\n\n- Each group A spacecraft gets its \'key\' in celestial_objects.py, with\n  its description\'s numbers checked against a page opened that day,\n  as slice 1\'s were.\n- The plan is made in the orrery and served in its export: for each\n  path, its span (launch or the record\'s start, to the end of JPL\'s\n  data), its events, and each event\'s window and step.\n- An event is a nearest approach found in JPL\'s positions, by a coarse\n  pass then a fine one, as `resolve_encounter_time` already does: a\n  spacecraft\'s to each body it passes, every close pass for one in\n  orbit (Juno), a comet\'s perihelion. Voyager 1\'s two typed windows are\n  replaced by events found this way.\n- The future part is fetched again on the Horizons check\'s 30-day cycle.\n  Its words in the hover ("planned" for a spacecraft, "predicted" for a\n  comet) are visitor words and go to Tony before they ship.\n- L-461 (pull matches push) builds with this slice, as recorded.\n- The nightly cost is measured on the first real build, as slice 1\'s\n  was.\n\n## 4. Where this leaves the slice\n\nDesigned. The build follows Tony\'s phone look of the L-472 patch, on a\nbase that includes patch_L472_1 and patch_L472_2.\n\n## 5. The Settled lines today\'s patches took off Where We Are\n\nKept here word for word, to keep the page under its line cap. Each\nruling also lives in the skill that fires on it.\n\n- A citation\'s web address goes on its own Source line. Links checked\n  every 30 days. Problem reports through the guest book\'s form. (Oct 20)\n- Earth\'s dipole cone drawn, unticked. Agency pages read one layer\n  down. Report words approved. (Oct 21)\n- Every view, still and animated, opens on the farthest thing drawn,\n  shell or orbit, plus 20%; the center body\'s axis and cone end just\n  past its farthest shell. Kelvin stays. (Oct 18-19)\n\nSession record written October 2026 with Anthropic\'s Claude Opus 5.5.\n')]

# Patch 2 must have run: its stamp line in the ledger.
REQUIRES = ('LEDGER_CONSOLIDATED.md', b"Module updated: October 23, 2026, afternoon, with Anthropic's Claude Opus")


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    root = os.getcwd()
    req_path, req_text = REQUIRES
    rp = os.path.join(root, req_path)
    if os.path.exists(rp) and req_text not in open(rp, "rb").read().replace(b"\r\n", b"\n"):
        fail("patch_L472_2_records_20261023.py has not run yet. Run it first, "
             "then run this one")
    news = []
    for rel, content in NEW_FILES:
        path = os.path.join(root, rel)
        if os.path.exists(path):
            have = open(path, "rb").read().replace(b"\r\n", b"\n")
            if have == content:
                news.append((rel, path, None))   # already there, identical
                continue
            fail("%s already exists and differs from what this patch writes. "
                 "If it is a copy you saved yourself, delete it and run again"
                 % rel)
        news.append((rel, path, content))
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
    for rel, path, content in news:
        if content is None:
            print("ok  %s (already there, identical)" % rel)
        else:
            open(path, "wb").write(content)
            print("ok  %s (new, %d bytes)" % (rel, len(content)))
    for f, path, out, crlf in plan:
        open(path, "wb").write(out)
        print("ok  %s (%d edits%s)" % (f["path"], len(f["edits"]),
              "; it was CRLF in the working copy, written LF" if crlf else ""))
    print("patch applied: %s (%d files)" % (TITLE, len(plan) + len(news)))


if __name__ == "__main__":
    main()
