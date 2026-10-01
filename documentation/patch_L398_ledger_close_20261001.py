#!/usr/bin/env python3
"""
patch_L398_ledger_close_20261001.py -- ORRERY repo. Closes the session
of 2026-10-01 (L-398).

Run: save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
open it in VS Code and click Run. Run the gallery's
patch_L398_3_dashboard_wrapper_20261001.py first: the button this patch
adds runs the file that one creates.

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery c12994d27e6205371cd463b1b535afd0a2f4dd17
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 58dd8f25ad7f3c01a2e4b03497abaa5091081f98
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

WHAT IT DOES.

  LEDGER_CONSOLIDATED.md
      - header stamp;
      - L-398 done: what was built and pushed, your phone check, your
        notes on the delivery, and where its loose ends went;
      - L-402 added: choosing a date, or animating, within the range
        the drawn bodies are trusted for (your idea, recorded);
      - L-401 added: the orrery's own distance hovers print by fixed
        widths (one row for the class, recorded, not chased);
      - L-363: a line saying L-398 landed and the NASA link is next.
  palomas_orrery_dashboard.py
      A "Solar System Figures" button under Gallery -- checks and data,
      and the offline runner's description names the new check.
  documentation/WHERE_WE_ARE.md
      rewritten for this session.
  documentation/HANDOFF_L398_distance_figures_20261001.md
      this session's record (new).

No skill changes. Everything is written or nothing is.

SUCCESS looks like: one "ok" line per edit and per file, then "patch
applied". FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and
NOTHING is written. Undo is Discard Changes in GitHub Desktop.

Written October 1, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
LEDGER_FP = "e0c3faa1a31a3f943a165c4b160a7dc3"
DASH = "palomas_orrery_dashboard.py"
DASH_FP = "f0006c2c3815fd47c53f55cdb81faa1a"
PAGE = "documentation/WHERE_WE_ARE.md"
PAGE_FP = "11984970ec86cb373b48a66df6c9411c"
HANDOFF = "documentation/HANDOFF_L398_distance_figures_20261001.md"
INDEX = ("<!-- INDEX:START", "<!-- INDEX:END -->")

LEDGER_EDITS = [('header stamp', 'Review and RICE update Tony 6-21-2026\n', "Module updated: October 1, 2026 with Anthropic's Claude Opus 5.5\n(L-398 done; L-401 and L-402 opened; L-363 note; a dashboard button for\nthe Solar System figures check), built on c12994d2.\nReview and RICE update Tony 6-21-2026\n"), ('L-401 and L-402 added', '## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n#### [L-399]', '## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n#### [L-402] Choose a date, or animate, within the range the drawn bodies are trusted for (gallery, exhibits)\n<!-- L:402 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n- **Tony\'s idea, 2026-10-01**, prompted by the distance fix (L-398): "we\n  could implement animation and date picking within the propagation\n  range of the cache adjusting the precision with time from the fetched\n  date." Then: "Could we determine the date range based on the selected\n  row instead of all the objects in the room? For example without\n  Mercury or without the Moon to get more range?"\n- **What already exists** [read at gallery 58dd8f25]. Each body\'s own\n  trust window is in the served cache, as half-widths in days: Mercury\n  88, Venus 225, Earth 365, Apophis 324, Mars 687, Jupiter 4,332, Saturn\n  10,754, Uranus 30,879, Neptune 60,248, the Pluto-Charon barycentre\n  90,143; the Moon 3.4. Each is capped at one orbital period. And a\n  distance already prints fewer figures the further the date is from the\n  elements\' date (L-398), so precision follows the date with no new rule.\n- **What stands in the way.** gallery/assembler/resolver.py checks ONE\n  served_window for every scene -- today 88 days either side, Mercury\'s\n  -- whatever the scene draws. Tony\'s second sentence answers the\n  question L-150 left open: the range follows the bodies drawn.\n- **For its design talk:** what happens when a ticked body\'s window does\n  not cover the chosen date (grey its row, refuse the tick, or move the\n  date); what animation costs per frame on a phone, with the orrery\'s\n  animate_objects as the model; and Tony\'s ruling of 2026-09-26 that a\n  date control comes to all rooms at once (the Sun room has no date, and\n  Earth\'s room would be held to the Moon\'s days only when the Moon is\n  drawn).\n- **When.** Recorded, not scheduled. Claude suggested a design talk once\n  the drawer (L-363 step 3b) is built; not ruled.\n**Gap:** the design talk.\n**Ref:** gallery/assembler/resolver.py (the served_window check);\ntools/gallery_cache_builder.py (trust); L-149; L-150; L-363; L-398.\n\n#### [L-401] The orrery\'s own distance hovers print by fixed widths, not by the errors the position earns (orrery, provenance)\n<!-- L:401 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n- **Recorded 2026-10-01, closing L-398**, as one row for the class under\n  The Braid: recorded, not chased. provenance-discipline 2.23 says every\n  computed position a display prints goes to the place the larger of\n  its drift and its source\'s accuracy earns. The orrery\'s hovers print\n  distances by widths chosen where they are printed [read at orrery\n  c12994d2]: format_detailed_hover_text in visualization_utils.py gives\n  the distance through formatting_utils.format_maybe_float, ten decimal\n  places of an AU, and format_km_float; add_fly_to_object_buttons labels\n  its buttons at ".0f km", ".3f AU" or ".2f AU". These are Rule 7\'s\n  fixed-width sites, which are listed and assigned when the rule reaches\n  them.\n- Where the orrery\'s position comes straight from Horizons for the plot\n  date there is no drift, and JPL\'s accuracy is what applies, through\n  the three DE430 rows in constants_new.py.\n**Gap:** discovery first -- list every orrery site that prints a computed\ndistance, by function -- then fix in slices when the work reaches the\norrery\'s hovers.\n**Ref:** visualization_utils.py; formatting_utils.py; constants_new.py\n(DE430 rows); provenance-discipline 2.23; L-398.\n\n#### [L-399]'), ('L-398 done', '<!-- L:398 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n', '<!-- L:398 status:DONE upd:2026-10-01 section:A flag: rice: -->\n'), ('L-398 close block', '**Gap:** the build above, and both skill bumps.\n**Ref:** interactive.html solarSystemDistanceLine (gallery); L-363; L-399; L-345.\n', '- **Method, 2026-10-01** (Tony: "Confirmed as recommended"). An\n  accuracy stated only in words is stored as the place the Report test\n  gives for every value the words can mean, the coarser where they could\n  mean two: 1 km, 100 km and 10,000 km. The last is one place coarser\n  than the Build bullet above planned ("the place the source names").\n- **Built and pushed 2026-10-01.**\n  - Orrery, patch_L398_1_accuracy_rows_and_skills_20261001.py, pushed at\n    c12994d2 with Tony\'s notes patch: the three DE430 rows,\n    provenance-discipline 2.23, interactive-exhibit 1.7, protocol v3.75,\n    and exact_rows_report.py\'s DRAWN entry for the new links. Tony\'s\n    maintenance run: 18 of 18 gating checks.\n  - Gallery, patch_L398_2_distance_figures_20261001.py, pushed at\n    58dd8f25: nine position_accuracy links, the figures logic in\n    gallery/solar_system_figures.js, Apophis\'s sentence, and a gating\n    check, "Solar System figures". Tony\'s runs: 20 of 20 offline; live,\n    14 of 14 files served byte-identical and the export at c12994d2.\n- **Tony\'s phone check, 2026-10-01.** Pluto 35.6108 AU (5,327,300,000\n  km), Neptune 4,469,690,000 km, Uranus 2,908,350,000 km, Saturn\n  1,411,367,900 km, Jupiter 793,946,800 km (5.307207 AU), Apophis with\n  the sentence. Every place is as designed. The digits differ from the\n  patch\'s examples, which were worked at the cache\'s own minute\n  (00:01 UTC): the room draws the minute it is opened, and from the\n  served elements Pluto moves outward about 4,300 km an hour, Jupiter\n  outward 2,000, Saturn inward 1,900 and Uranus inward 1,100 -- all four\n  match a look about 18.5 hours later. The inner planets were not looked\n  at.\n- **Tony\'s notes on the delivery, 2026-10-01.** "Nine bodies get a link"\n  meant a pointer in objects_config.json to the orrery\'s row, which a\n  visitor never sees; the info panel\'s NASA link is L-395, next. The new\n  check goes on the dashboard: patch_L398_3_dashboard_wrapper_20261001.py\n  (gallery) and patch_L398_ledger_close_20261001.py (orrery).\n- **Loose ends.** Small bodies\' own uncertainty: L-399, already open. The\n  orrery\'s own distance hovers, which the new rule reaches: L-401, opened\n  by this close. The skill obligation: the next session confirms its\n  loaded copies read provenance-discipline 2.23 and interactive-exhibit\n  1.7; Tony reinstalled both on 2026-10-01, which this session cannot see.\n**Ref:** gallery/solar_system_figures.js,\ndocumentation/smoke_solar_system_figures.js and\ndocumentation/run_solar_system_figures.py (gallery); constants_new.py\nDE430 rows; L-363; L-399; L-401; L-345.\n'), ('L-363 note', '<!-- L:363 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n', "<!-- L:363 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n- **2026-10-01, L-398 landed** (gallery 58dd8f25). A body's distance now\n  prints to the place the larger of the drift and JPL's own accuracy\n  earns; Uranus, Neptune and Pluto to ten thousand km, Apophis with\n  Tony's sentence. Tony noticed the info panel still has no NASA link for\n  a body: that is L-395, the next step. Order unchanged: L-395, then step\n  3b, then the phone check.\n")]
DASH_EDITS = [("offline runner's list names the new check", '        "hover budget, arrival, display figures, and the guest book. "\n', '        "hover budget, arrival, display figures, Solar System figures, "\n        "and the guest book. "\n'), ('button: Solar System Figures', '        ("Store Editor Suite",\n', '        ("Solar System Figures",\n        os.path.join("documentation", "run_solar_system_figures.py"),\n        "Checks the distances the Solar System room prints (L-398). Each "\n        "prints to the place the larger of two errors earns: how far the "\n        "page\'s arithmetic may have drifted from JPL Horizons, and how "\n        "well JPL knows where the body is at all, from its 2014 ephemeris "\n        "report. Works six distances by hand, matches every body in the "\n        "room\'s drawer to its group\'s row, and prints each body\'s "\n        "distance from the served cache with what set its figures. Fails "\n        "unless Uranus, Neptune and Pluto print to JPL\'s ten-thousands "\n        "place, and if the page stops using gallery/solar_system_figures.js. "\n        "It breaks that file three ways first, so a pass has shown it can "\n        "fail. The check is Node; this is the Python wrapper the dashboard "\n        "needs. GATES the gallery runner. Runs from the gallery repo ROOT.",\n        GALLERY_REPO_DIR,\n        True,\n        None,\n        True),\n        ("Store Editor Suite",\n')]
PAGE_TEXT = '<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->\n# Where We Are\n\nLast updated: October 1, 2026, evening\n- Written at orrery c12994d2 plus this session\'s closing patch, and\n  gallery 58dd8f25 plus its small patch.\n\n> **READ THIS FIRST**\n>\n> **Changed this session:**\n> - Distances in the Solar System room now show only the figures JPL\'s\n>   own accuracy allows.\n> - Pluto, Uranus and Neptune end at ten thousand km. Jupiter and Saturn\n>   end at hundreds of km.\n> - Apophis keeps its distance and says JPL\'s own uncertainty is not yet\n>   included.\n> - A new check guards this in the website\'s maintenance run, and it\n>   gets its own dashboard button.\n> - Your idea is recorded: choose a date, or play time forward, over\n>   the range the ticked bodies are trusted for.\n>\n> **Do next:**\n> - *Each body gets its NASA description and link, taken from the\n>   orrery\'s own object list.*\n>\n> **Needs you now:**\n> - *Run the small website patch, then this closing patch in the orrery\n>   folder, then commit and push both.*\n\nHow to read the marks:\n- *Italic* lines are the must-reads.\n- **>> UPDATED THIS SESSION** beside a heading means that section\n  changed in the latest session.\n- Sections without a mark are as they were.\n- The marks are cleared and reset at every session\'s update, so they\n  always mean "new since you last read this."\n\n## The goal\n\n- Paloma\'s Orrery on the web.\n- The website does what the desktop orrery does, in the browser, from\n  data fetched from JPL each night, so a visitor never waits on JPL.\n- Anyone can open it, with nothing to install.\n- Built from the same code and the same checked numbers as the desktop\n  orrery.\n- The one real limit: the browser can show only the dates the saved\n  data covers.\n\n## The road\n\n  1. [done]   The Sun\'s room is live on the website.\n  2. [done]   Earth\'s room is live, with every number traced to its source.\n  3. [done]   The numbers come from one place: the orrery feeds the\n              website, and nothing is typed twice.\n  4. [NOW]    *The Solar System room becomes a second way in: all the\n              planets, a drawer to pick them, and a way into each\n              body\'s own room.*\n  5. [next]   The Sun\'s numbers get the same checking Earth\'s got.\n  6. [next]   The Solar System room\'s card becomes the top featured\n              card in the lobby. The lobby stays the front page.\n  7. [later]  The rest of the orrery\'s objects come to the website --\n              dwarf planets, asteroids, moons -- from the orrery\'s own\n              object list, checked against JPL Horizons.\n  8. [later]  Encounters: comets and spacecraft shown at the dates\n              that matter.\n  9. [later]  The planets get their details -- layers, rings, magnetic\n              fields -- Jupiter and Saturn first.\n 10. [goal]   The website does what the desktop orrery does, from data\n              fetched from JPL each night.\n\n## Right now  **>> UPDATED THIS SESSION**\n\n- The Solar System room shows the Sun, all eight planets, Pluto and\n  the asteroid Apophis, where they are when you open it.\n- Each text box gives the body\'s distance in AU and in km, with only\n  the figures JPL\'s accuracy and the page\'s arithmetic allow.\n- The digits change from one visit to the next, because the planets\n  move: Pluto moves about 4,300 km further out every hour.\n- The info panel has no NASA link for a body yet. That is the next step.\n- The drawer\'s new behaviours have not been built yet.\n\n## The next three steps  **>> UPDATED THIS SESSION**\n\n1. *Each body gets its NASA description and link, taken from the\n   orrery\'s own object list.*\n   - It starts with a short design talk about that list.\n   - Pluto\'s row links to NASA\'s Pluto page.\n2. The drawer\'s new behaviours are built.\n   - "See more", "Enter the Sun room", tapping a body to find its row,\n     and Home remembering what you ticked.\n3. You check the room on your phone and desktop.\n\n## Waiting on you  **>> UPDATED THIS SESSION**\n\nNow:\n- *Run patch_L398_3 in the website folder, then commit and push.*\n- *Run the closing patch in the orrery folder, then the maintenance\n  run, then commit and push.*\n\nAt the next design talk:\n- What the orrery\'s object list should hold for each body, and what\n  belongs only to the website.\n\nNot urgent:\n- Choosing a date, and animation, your idea of today.\n  - The range would follow only the bodies you tick, so leaving out\n    Mercury or the Moon gives more time.\n  - Talked through once the drawer is built.\n- Whether a bare interactive.html link should open the Solar System\n  room instead of the Explorer.\n  - You said "to be determined".\n  - It comes up again after the Sun\'s numbers are done.\n\n## Where the details are\n\n- Every item, done and open: `LEDGER_CONSOLIDATED.md`\n  - This session: L-363, L-389, L-396, L-398, L-399, L-400, L-401, L-402.\n- The reasoning behind the order:\n  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n- The latest session record:\n  `documentation/HANDOFF_L398_distance_figures_20261001.md`\n'
HANDOFF_TEXT = '<!-- Doc-Kind: hand | Session record for L-398, the Solar System room\'s distance figures, and Tony\'s notes of 2026-10-01. -->\n# HANDOFF -- L-398: distances print what JPL\'s accuracy earns\n\nBuilt on orrery 7a47269c09acd4d2f875f6c8d49070659c4c2ee9 at\nhttps://github.com/tonylquintanilla/palomas_orrery, and gallery\nc48f9a92e6d6094a8d25ae9413a94c17503ee50c at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io.\nOrrery pushed at c12994d2 (the notes patch and patch_L398_1). Gallery\npushed at 58dd8f25 (patch_L398_2). This record lands with the closing\npatch patch_L398_ledger_close_20261001.py, after the gallery\'s\npatch_L398_3_dashboard_wrapper_20261001.py.\n\nType: BUILD.\nSupersedes: nothing. Follows HANDOFF_L363_half2_step3a_20260930.md,\nwhose section 6 items 1 and 2 this session carried out.\n\nSession written October 2026 with Anthropic\'s Claude Opus 5.5.\n\n## 1. Skills at session start\n\nAll loaded copies matched the manifest: ledger-and-session-records 1.13,\nsafe-file-editing 1.11, provenance-discipline 2.22, interactive-exhibit\n1.6, gallery-cache-builder 1.6, gallery-assembler 1.3, agentic-pre-test\n1.2. This session bumped provenance-discipline to 2.23 and\ninteractive-exhibit to 1.7 (protocol v3.75). Tony reinstalled both;\nthis session cannot see that. THE NEXT SESSION CONFIRMS its loaded\ncopies read 2.23 and 1.7 before any provenance, constants_new.py or\nexhibit work.\n\n## 2. Rulings\n\n- Tony\'s notes on Where We Are, recorded by\n  patch_L363_ledger_tony_notes_20261001.py: the lobby stays the front\n  page and the Solar System room\'s card becomes the top featured card;\n  whether a bare interactive.html link switches is "to be determined";\n  the goal line reworded ("confirmed as recommended"); Earth\'s\n  atmosphere is the provenance skill\'s to decide; the orbit markers\n  keep their words; the stray folder deleted.\n- The distance figures: an accuracy stated only in words is stored as\n  the place the Report test gives for every value the words can mean,\n  the coarser where they could mean two. Uranus, Neptune and Pluto at\n  ten-thousands, one place coarser than the plan\'s wording. Tony:\n  "Confirmed as recommended".\n- Tony asked for the new check on the dashboard.\n- Tony\'s idea, recorded as L-402: choose a date, or animate, within the\n  range the cache is trusted for, with the range following only the\n  bodies drawn ("without Mercury or without the Moon to get more\n  range"). Not scheduled; Claude suggested a design talk after the\n  drawer.\n\n## 3. What was built, verified\n\n| Patch | Repo | Pushed | Verified |\n|---|---|---|---|\n| patch_L363_ledger_tony_notes_20261001.py | orrery | c12994d2 | Tony\'s run, every edit ok. |\n| patch_L398_1_accuracy_rows_and_skills_20261001.py | orrery | c12994d2 | Tony\'s maintenance run: 18 of 18 gating. In the sandbox: LF and CRLF copies, refuses a rerun and the wrong folder; store checks pass; scanner Tier 1 unchanged at 296, the new rows at Tier 2. |\n| patch_L398_2_distance_figures_20261001.py | gallery | 58dd8f25 | Tony\'s runs: 20 of 20 offline, live 14 of 14 files byte-identical, export at c12994d2. In the sandbox: the room\'s real driver run in CPython on the real cache, its compose run in Node; the new check fails on the unpatched gallery with 18 named problems. Tony\'s phone: places as designed (ledger L-398). |\n| patch_L398_3_dashboard_wrapper_20261001.py | gallery | -- | Sandbox: the wrapper passes from the root and refuses from documentation/. |\n| patch_L398_ledger_close_20261001.py | orrery | -- | This patch: ledger, dashboard button, Where We Are, this record. |\n\n## 4. Found this session\n\n- The orrery\'s own distance hovers print by fixed widths -- ten decimal\n  places of an AU in the detailed hover. Recorded as L-401, one class\n  row, not chased.\n- My first message said the front-door ruling replaced a plan to make\n  the room the website\'s opening page. The plan only ever meant a bare\n  interactive.html link. Corrected in L-363.\n- My delivery message said "nine bodies get a link", which read as a\n  visitor link. It meant a pointer in objects_config.json.\n\n## 5. Discrepancies\n\n- None between handoff and base.\n\n## 6. Next session\n\n1. Confirm the loaded skills read provenance-discipline 2.23 and\n   interactive-exhibit 1.7.\n2. L-395: a short design talk on the orrery\'s object list, then the\n   export of descriptions and NASA links, with the duplicate-field\n   check.\n3. L-363 step 3b, the drawer, then Tony\'s phone check.\n\n## 7. Tony-actions, rolled up\n\n- (do) Run patch_L398_3_dashboard_wrapper_20261001.py in the gallery\n  root; move it to documentation/; commit and push.\n- (do) Run patch_L398_ledger_close_20261001.py in the orrery root; then\n  orrery_maintenance_run.py; move the patch to documentation/; commit\n  and push.\n'


def norm(raw):
    return raw.replace(b"\r\n", b"\n").decode("utf-8")


def ledger_fp(text):
    start, end = INDEX
    if start in text and end in text:
        a = text.index(start)
        b = text.index(end) + len(end)
        text = text[:a] + text[b:]
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def plain_fp(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def edited(path, want_fp, fp_fn, edits):
    with open(path, "rb") as f:
        raw = f.read()
    crlf = b"\r\n" in raw
    text = norm(raw)
    got = fp_fn(text)
    if got != want_fp:
        raise SystemExit("ERROR: %s is not the file this patch was built "
                         "against (fingerprint %s, expected %s). It has "
                         "changed since c12994d2, or this patch has already "
                         "run. NOTHING was written." % (path, got, want_fp))
    for label, old, new in edits:
        n = text.count(old)
        if n != 1:
            raise SystemExit("ANCHOR FAIL: %s -- %s: expected 1 match, found "
                             "%d. NOTHING was written." % (path, label, n))
        text = text.replace(old, new)
    if any(ord(ch) > 127 for ch in text):
        raise SystemExit("ERROR: %s would hold non-ASCII text. NOTHING was "
                         "written." % path)
    return text, crlf


def write(path, text, crlf):
    data = text.replace("\n", "\r\n") if crlf else text
    with open(path, "wb") as f:
        f.write(data.encode("utf-8"))


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")

    ledger, ledger_crlf = edited(LEDGER, LEDGER_FP, ledger_fp, LEDGER_EDITS)
    dash, dash_crlf = edited(DASH, DASH_FP, plain_fp, DASH_EDITS)
    with open(PAGE, "rb") as f:
        praw = f.read()
    if plain_fp(norm(praw)) != PAGE_FP:
        raise SystemExit("ERROR: %s holds content this patch does not know. "
                         "NOTHING was written." % PAGE)
    if os.path.exists(HANDOFF):
        raise SystemExit("ERROR: %s already exists, so this patch has "
                         "probably run. NOTHING was written." % HANDOFF)

    write(LEDGER, ledger, ledger_crlf)
    for label, _o, _n in LEDGER_EDITS:
        print("ok  %s  %s" % (LEDGER, label))
    write(DASH, dash, dash_crlf)
    for label, _o, _n in DASH_EDITS:
        print("ok  %s  %s" % (DASH, label))
    write(PAGE, PAGE_TEXT, b"\r\n" in praw)
    print("ok  %s  rewritten" % PAGE)
    write(HANDOFF, HANDOFF_TEXT, False)
    print("ok  %s  new" % HANDOFF)
    print("")
    print("Stamps updated: the ledger's header line; Where We Are's date.")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. python orrery_maintenance_run.py  (rebuilds the ledger index")
    print("     and moves L-398 into the closed section)")
    print("  2. Move this script into documentation/. Commit and push.")
    print("  3. Optional: open the dashboard and press Solar System Figures")
    print("     under Gallery -- checks and data. It should end \"=== PASS\".")
    return 0


if __name__ == "__main__":
    sys.exit(main())
