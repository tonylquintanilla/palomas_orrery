#!/usr/bin/env python3
"""
patch_L456_7_close_20261021.py -- the close of the L-456 address build:
your phone look and this afternoon's findings onto the ledger (L-461,
L-462, L-463, L-464 new), the talks part 2 lines its handoff asked this
session to carry, the handoff's closing section, and Where We Are.

Built on orrery 5102188c51547113c206d12168971c77795ea5f9 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
1dd25994e60fa063a44814a14d196ba705547c70 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 21, 2026 with Anthropic's Claude Opus 5.5. Record:
documentation/HANDOFF_L456_addresses_build_20261021.md, section 0.

RUN COMMAND

    python patch_L456_7_close_20261021.py

    Save this file in the ORRERY folder above, open it in VS Code and
    click Run. It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing

    LEDGER_CONSOLIDATED.md         L-461, L-462, L-463, L-464 new;
                                   lines on L-456, L-412, L-375, L-454,
                                   L-314, L-413, L-458, L-411; the
                                   module's stamp
    documentation/WHERE_WE_ARE.md  edited by section; your run record
                                   below the marker is not touched
    documentation/HANDOFF_L456_addresses_build_20261021.md
                                   a closing section 0, and one line in
                                   section 6

    Each file is checked only at the lines this patch edits, so your
    notes never make it refuse. Nothing is written unless every edit
    fits. Files are written LF. A second run refuses. Once it has run,
    move it into documentation/, before the maintenance run.

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
    "  2. Run the orrery maintenance run (dashboard). Expect 31 of 31",
    "     gating and the gate line 0 TIER-1; it rewrites the ledger's",
    "     index (L-461 to L-464 new).",
    "  3. Commit and push the orrery. Nothing to run on the website.",
]

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

FILES = [
    {'path': 'LEDGER_CONSOLIDATED.md', 'mode': 'edit', 'anchors_only': True, 'zone': ('<!-- INDEX:START', '<!-- INDEX:END -->'), 'edits': [("re-homed to Rappaport et al. (2013), so no GPT prompt; L-412's\nGap), built on 6a8d04c2 and gallery 30db99fb.\nReview and RICE update Tony 6-21-2026\n", "re-homed to Rappaport et al. (2013), so no GPT prompt; L-412's\nGap), built on 6a8d04c2 and gallery 30db99fb.\nModule updated: October 21, 2026, afternoon, with Anthropic's Claude\nOpus 5.5 (the close: L-456 pushed and Tony's phone look; L-461 new,\nthe Daily Run checks the orrery it pulled; L-462 new, a short form of\nthe maintenance run; L-463 and L-464 new, the Sun room's phone\nfindings; talks part 2's lines on L-375, L-454, L-314, L-413, L-412,\nL-458 and L-411), built on 5102188c and gallery 1dd25994.\nReview and RICE update Tony 6-21-2026\n"), ("#### [L-460] Every room's drawer orders its shells by where each begins", '#### [L-464] The Sun room\'s own row: no info link, and the pole\'s citation has nowhere to show (gallery, interactive)\n<!-- L:464 status:OPEN upd:2026-10-21 section:A flag: rice: -->\n- **Tony, 2026-10-21,** at his phone look after L-456\'s addresses were\n  pushed (orrery 5102188c, gallery 1dd25994; run record\n  `documentation/WHERE_WE_ARE_10-21-26_1217_run_record.md`): "also i do not see the sun\'s\n  pole. and the sun drawerer does not have a link, either nasa or\n  wikipedia."\n- **Read the same day on the served site, not yet traced in code:** the\n  Sun\'s own drawer row (the centre body, legend group "center") opens\n  an i panel reading "No link on file for this shell.", though the\n  Sun\'s entry in `data/objects_config.json` carries `info_url`\n  https://science.nasa.gov/sun/. The panel code\'s own comment says\n  every shell in the Sun and Earth rooms has a link; the centre row is\n  the one it missed.\n- The Sun\'s pole is served with its re-homed citation (NASA NAIF\'s\n  pck00011.tpc; gallery `patch_L456_6_sun_pole_website_20261021.py`),\n  but no row or panel was found that shows it to a visitor.\n- Not caused by the address build: between gallery 30db99f and 1dd25994\n  only citation text changed in the served config.\n- **Found and fixed the same day** (gallery\n  `patch_L463_1_sun_room_fixes_20261021.py`): the Sun room never gave\n  the assembler\'s centre marker any words, while the Solar System room\n  gives the same marker the Sun\'s description and link. The Sun room\n  now gives it the Sun\'s description and NASA link from the orrery\'s\n  object list and, as its source, the pole\'s citation, which turns the\n  room\'s drawings but had no row of its own. All three are served\n  words; the Typed facts check passes. In a headless run every one of\n  the Sun room\'s 19 rows now has a link and a source. Earth\'s room has\n  no centre row: its pole has its own row, Rotation Axis and Equator,\n  with a link and a source.\n**Gap:** Tony\'s phone, after the push: the Sun\'s own row shows NASA\'s\nlink and the pole\'s source. Then this item closes.\n**Ref:** gallery `interactive.html`, `data/objects_config.json`,\n`gallery/source_list.js`; interactive-exhibit; L-456; L-412.\n\n#### [L-463] A pink band or sheet across the Sun room on Tony\'s phone (gallery, rendering)\n<!-- L:463 status:OPEN upd:2026-10-21 section:A flag: rice: -->\n- **Tony, 2026-10-21,** the same look: "there are a number of issues,\n  there is a pink band that appears in various views." Three\n  screenshots from his phone, 13:25 to 13:27, sent in chat and not\n  saved: at the 0.1 AU grid, a pale pink sheet across most of the\n  view, edged in purple; at the 50 AU grid with the Heliopause\n  selected, a pink band crossing the view diagonally through the Sun.\n- **Read the same day, not yet reproduced:** a fresh load of the Sun\n  room in a desktop browser drew no band. The room\'s code draws no\n  filled surfaces (no mesh3d, no surfaceaxis in gallery `gallery/` or\n  `interactive.html`). The band\'s purple edge is the colour of the\n  Galactic Plane ring, rgb(175, 135, 235), a line of 181 points: a\n  guess, not a finding, that the phone draws that ring filled.\n- Not caused by the address build: only citation text changed in the\n  served config that day.\n- **Cause confirmed, 2026-10-21, 14:03, Tony\'s test on his phone:** with\n  the Galactic Plane ticked, Go To on the Corona brought the band back\n  (a fifth screenshot, at the 0.02 AU grid). At the 50,000 AU grid the\n  same rows drew cleanly. So the band is the Galactic Plane\'s ring and\n  pole line, at 100,000 AU, drawn by the phone when the view is close\n  in: hundreds to millions of times past the view\'s edge.\n- **Fix built the same day:** gallery\n  `patch_L463_1_sun_room_fixes_20261021.py`. The page cuts any line\n  reaching more than 20 times past the view to the view\'s edge before\n  it is drawn, and again at every frame change (`gallery/far_lines.js`);\n  a desktop sees no change, because gl-plot3d already hid that part.\n  The point count never changes, so per-point hover text stays lined\n  up. Checked: the new gating check "Far lines"\n  (`documentation/smoke_far_lines.js`, its self-test breaking the file\n  three ways first); every other website check passing; a headless\n  walk of the Sun room (the Galactic Plane ticked, then Go To on the\n  Corona: its lines reach 0.102 AU, the view\'s edge, where before they\n  reached 100,000 AU); and every room\'s drawer behaving exactly as\n  before (`tools/headless/compare_rooms.js`, the Sun, Earth and Solar\n  System rooms). Not yet seen on the phone.\n**Gap:** Tony\'s phone, after the push: the Galactic Plane ticked, Go To\non the Corona, no band. Then this item closes.\n**Ref:** gallery `gallery/feature_renderers.js`, `interactive.html`;\nL-412; L-460.\n\n#### [L-462] The orrery maintenance run, a short form for small patches (orrery, maintenance)\n<!-- L:462 status:OPEN upd:2026-10-21 section:A flag: rice: -->\n- **Tony, 2026-10-21,** after `patch_L456_4b_roche_rehome_20261021.py`:\n  "the orrery maintenance runner takes a long time. if only one or two\n  sub-files is needed that would make things quicker." Then: "i don\'t\n  mean now, i\'ve already started it, but going forward."\n- **Proposed in chat the same day, not ruled:** each patch names the\n  steps it needs (for a citation-only patch, the constants export and\n  the provenance gate); a short form of the run does only those and\n  ends by naming every check it skipped, so a skipped check cannot\n  read as a pass (A Check That Cannot Fail Is Not Passing). The full\n  run stays the routine before a session\'s first push and for any\n  patch that touches code.\n**Gap:** a design talk: which steps a patch may name, where the short\nform is started (the dashboard), and whether the push gate accepts it.\n**Ref:** `orrery_maintenance_run.py`, `palomas_orrery_dashboard.py`;\nL-188 (the maintenance run); L-459 (the monthly run).\n\n#### [L-461] The Daily Run confirms the orrery it pulled is the one Tony pushed (gallery, Daily Run)\n<!-- L:461 status:OPEN upd:2026-10-21 section:A flag: rice: -->\n- **What happened, 2026-10-21** (run record\n  `documentation/WHERE_WE_ARE_10-21-26_1217_run_record.md`): the orrery\'s patches\n  ran and passed but were not pushed; the website\'s patch, Daily Run\n  and push went ahead (gallery 53f17b6), and its pull brought the\n  orrery\'s old export (the Pointer join line: "against orrery\n  6a8d04c2"), so the phone showed citations without links. Tony: "i\n  think what happened is that i got impatient and ran the website\n  patch before committing the orrery patch." Put right the same day:\n  orrery 5102188c, gallery 1dd25994.\n- **Tony, 2026-10-21:** "even after pushing, the push can take a bit to\n  complete in github. it is not immediate." So a pull straight after a\n  push can still bring the old export.\n- **Proposed in chat, not ruled:** the Daily Run compares the orrery\n  version its pull brought with the newest commit in Tony\'s orrery\n  folder, and stops with a plain message when they differ: work not\n  pushed, or a push GitHub has not finished serving. Until it is\n  built, the check by eye: the Pointer join line\'s "against orrery"\n  code matches the start of the code GitHub Desktop shows for the\n  orrery push.\n**Gap:** the build (gallery `daily_run.py`, the pull step), with its\nrule in gallery-cache-builder; whether a difference stops the run or\nwaits and tries again.\n**Ref:** gallery `daily_run.py`, `gallery_maintenance_run.py` (the\npulls); gallery-cache-builder; L-446 (the Daily Run pulls before it\nbuilds); L-456.\n\n#### [L-460] Every room\'s drawer orders its shells by where each begins'), ('<!-- L:458 status:OPEN upd:2026-10-20 ', '<!-- L:458 status:OPEN upd:2026-10-21 '), ("**Gap:** the build: the link in the shared i-panel chrome, so every\nroom has it at once (interactive-exhibit); the guest book updater\ntelling a report from a greeting; the message's words as a list for\nTony first.\n", '- **2026-10-21, talks part 2, talk D:** the words approved (Tony,\n  "Approved"), as listed in `documentation/DESIGN_talks2_rulings_20261021.md`\n  talk D; plus an "About this gallery" line under the link opening the\n  front page\'s About card, shared not copied (Tony, "please add the\n  same info button that is in the front page that has my name and\n  email", then "A"); plus "Page: <address>" as the message\'s last\n  line (Tony, "Yes").\n**Gap (2026-10-21):** the build: the link in the shared i-panel\nchrome, so every room has it at once (interactive-exhibit); the guest\nbook updater telling a report from a greeting. The words list is no\nlonger a gap.\n**Gap (superseded above):** the build: the link in the shared i-panel chrome, so every\nroom has it at once (interactive-exhibit); the guest book updater\ntelling a report from a greeting; the message\'s words as a list for\nTony first.\n'), ("**Gap (replaces the one below, 2026-10-21, later):** Tony's three\npapers,", '- **Pushed 2026-10-21** (orrery 5102188c, gallery 1dd25994), after a\n  first website push (53f17b6) that ran before the orrery\'s and served\n  the old citations (L-461). Two follow-up patches:\n  `patch_L456_4b_roche_rehome_20261021.py` (orrery; an earlier copy of\n  patch 4 had run, before the Roche limit\'s re-home) and\n  `patch_L456_6_sun_pole_website_20261021.py` (website; the Sun\'s pole,\n  missing from the earlier copy of patch 5). The live run: "the served\n  export is the orrery\'s at 5102188c, byte for byte". Tony\'s phone\n  look (run record `documentation/WHERE_WE_ARE_10-21-26_1217_run_record.md`): the\n  galactic tide\'s and plane\'s links "perfect", the Earth inner core\'s\n  "correct". Found there and not from the build: L-463 (a pink band)\n  and L-464 (the Sun\'s own row and its pole).\n**Gap (replaces the one below, 2026-10-21, later):** Tony\'s three\npapers,'), ("**Gap (2026-10-21):** the next design talk, which loads\ninteractive-exhibit 1.18, on Earth's list (L-413).\n", '- **2026-10-21, talks part 2, talk B:** option 2, after a draft\n  drawing. Tony: "That looks right and yes separate the two rows so\n  they don\'t clash by default. And please keep option 4 for future\n  consideration." Each model stays sharp, with two faint surfaces at\n  the ends of its own paper\'s fitted range (Shue 0.5 and 8.5 nPa;\n  Jelinek 0.6 and 11 nPa); each pair on its own row; by kind, so the\n  Sun\'s Alfven surface takes 10 and 20 solar radii from its existing\n  rows. Option 1 (a scatter band) and option 3 (words only) declined.\n  Record: `documentation/DESIGN_talks2_rulings_20261021.md`, talk B. The design half\n  is done; the item stays open for the build.\n**Gap (replaces the one below, 2026-10-21, later):** four measured\nrows for the two papers\' ranges, read at the build; the faint\nsurfaces in both instruments; the Sun\'s slice applies it to the\nAlfven surface and the heliosphere\'s edges.\n**Gap (2026-10-21, superseded above):** the next design talk, which loads\ninteractive-exhibit 1.18, on Earth\'s list (L-413).\n'), ("  Tony-action (decide), at the next design talk: is this his ruling,\n  or a line on provenance-discipline's next version?\n", '  Tony-action (decide), at the next design talk: is this his ruling,\n  or a line on provenance-discipline\'s next version?\n- **Ruled 2026-10-21, talks part 2, talk C:** Tony, "The skill\'s and\n  ask in your design to amend the skill not just add to the ledger."\n  So it is method, for provenance-discipline 2.33: the paragraph to add\n  to The Access Standard is written out in\n  `documentation/DESIGN_talks2_rulings_20261021.md` talk C; it rides the next\n  build that bumps provenance-discipline (one session, one bump), with\n  the four-step binding rule. The Tony-action above is answered.\n'), ("**Gap (replaces the one below, 2026-10-21):** L-456's addresses (built\n", "- **2026-10-21, talks part 2:** L-454's device applies to the Alfven\n  surface, two faint surfaces at ALFVEN_SURFACE_RANGE_LOW and _HIGH (10\n  and 20 solar radii), no new talk; check on the phone whether the\n  faint 20 reads apart from the drawn 19.7.\n- **2026-10-21, L-456's addresses pushed** (orrery 5102188c, gallery\n  1dd25994): every Sun and Earth source linked. Tony's phone look the\n  same afternoon found a pink band across the Sun room (L-463), and the\n  Sun's own row without a link and the pole's citation unseen (L-464);\n  neither from the build.\n**Gap (replaces the one below, 2026-10-21, later; the order proposed,\nfor Tony's word):** the Sun room's phone findings, fixed the same day\nand waiting on his phone (L-463, L-464); then the drawer order\nby where each shell begins (L-460) and the Sun's fourteen hover and\ntooltip pairs (L-191); L-454's two faint surfaces on the Alfven\nsurface; the tide and the clumps as stored drawings with the tide's\nphone look (L-434); the streamer belt's and the clumps' eyeballed\nnumbers; L-241; then L-443, with L-128 after it.\n**Gap (2026-10-21, superseded above):** L-456's addresses (built\n"), ("**Gap (2026-10-21):** talk 2's last two questions (L-375's cone,\n", "- **2026-10-21, talks part 2:** L-375's website cone and L-454's device\n  ruled; both are builds on this list now. Talks 3 to 6 are unchanged\n  and still wait behind the Sun's slice.\n**Gap (replaces the one below, 2026-10-21, later):** talks 3 to 6,\nwhich wait behind the Sun's slice (L-412); the builds of L-375's cone\nand L-454's device. Talk 4 (L-314) keeps the solar-wind fetch; its\naberration is built. L-356's build may come on any evening (Tony,\n2026-10-20).\n**Gap (2026-10-21, superseded above):** talk 2's last two questions (L-375's cone,\n"), ("**Gap (2026-10-21):** the offset's row and sentence, with L-356's\n", '- **2026-10-21, talks part 2, talk A:** Tony, "draw Earth\'s dipole\n  cone, as a new drawer row starting unticked". The website has no\n  dipole feature today; the cone is a new served feature with its own\n  row, shell key and served words, its tilt pointing at\n  EARTH_DIPOLE_TILT_DEG. Build notes in\n  `documentation/DESIGN_talks2_rulings_20261021.md` talk A.\n**Gap (replaces the one below, 2026-10-21, later):** read the offset\'s\nsource (unchanged); the offset\'s row and sentence, with L-356\'s\nbuild; build the website\'s cone, on Earth\'s list (L-413).\n**Gap (2026-10-21, superseded above):** the offset\'s row and sentence, with L-356\'s\n'), ('<!-- L:314 status:OPEN upd:2026-10-17 ', '<!-- L:314 status:OPEN upd:2026-10-21 '), ('**Gap:** the whole item, now that L-305 has closed (2026-10-04); the\n', '- **2026-10-21:** kept for future consideration as the moving version\n  of the device for edges that move (L-454 option 4; Tony, "please\n  keep option 4 for future consideration"). Not declined; not moved up.\n**Gap:** the whole item, now that L-305 has closed (2026-10-04); the\n')]},
    {'path': 'documentation/WHERE_WE_ARE.md', 'mode': 'edit', 'anchors_only': True, 'zone': None, 'edits': [("Last updated: October 21, 2026, later: the Sun's and Earth's sources carry links; three papers for you to open.\n- Written at orrery 6a8d04c and gallery 30db99f.\n", "Last updated: October 21, 2026, afternoon: the links are live; the Sun room's phone problems fixed, to check.\n- Written at orrery 5102188 and gallery 1dd2599.\n"), ("> - The Sun's and Earth's sources: 36 of the 39 works re-opened and\n>   linked; in the i panel, the Sun 40 of 40, Earth 73 of 73\n>   (L-456 (what a visitor reads)).\n> - The links go live after the orrery push; the Roche limit cites an open paper.\n> - The design talks of Oct 20 are on the ledger (this morning).\n>\n> **Do next:** *orrery: patch 4b, the maintenance run, commit AND push;\n> then the website: patch 6, the Daily Run, push; then your phone\n> (`HANDOFF_L456_addresses_build_20261021.md`, section 1).*\n", "> - Every Sun and Earth source is linked and live (L-456 (what a visitor reads)).\n> - Your phone's three Sun-room problems: cause found, fixes built\n>   (L-463 (pink band), L-464 (the Sun's own row and pole)).\n> - Talks part 2: Earth's dipole cone and a moving-edge device ruled.\n>\n> **Do next:** *website: patch_L463_1, its run, push, then your phone;\n> orrery: this close patch, the maintenance run, commit, push.*\n"), ("  5.   [next]  Earth's list (L-413): talk 2 partly held (Oct 20); its\n               last two questions, then talks 3 to 6, wait behind the\n               Sun's slice. << moved this session\n", "  5.   [next]  Earth's list (L-413): talk 2 settled (Oct 20-21), the\n               dipole cone and the moving-edge device to build; talks\n               3 to 6 wait behind the Sun's slice. << moved this session\n"), ('               list, addresses (Oct 18-21); now the\n               drawer order (L-460), the 14 hover and tooltip pairs\n', "               list, addresses (Oct 18-21); the phone's three\n               problems fixed (L-463, L-464); now the drawer order\n               (L-460), the 14 hover and tooltip pairs\n"), ("  shell's drawer place is where it begins. (Oct 20)\n", "  shell's drawer place is where it begins. (Oct 20)\n- Earth's dipole cone drawn, unticked. Moving edges: sharp model plus\n  two faint surfaces at its fitted range, own row; live solar wind later.\n  Agency pages read one layer down (skill). Report words approved. (Oct 21)\n"), ('- Last cache build: 20261021T134110Z, ok, every rename on the first try (gallery 30db99f).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md at 6a8d04c).\n', '- Last cache build: 20261021T181821Z, ok; the swap took 3 tries, absorbed (gallery 1dd2599).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md at 5102188).\n'), ("At the next design talk:\n- Whether the website draws Earth's dipole cone: L-375 (the dipole's\n  offset).\n- The device for edges that move: L-454 (edges that move).\n- Mine or the skill's? An agency page that names no source is read one\n  layer down, to the scientific work, before its figure becomes a row\n  (L-411 (the Sun's typed numbers)).\n", 'At the next design talk:\n- A short form of the maintenance run for small patches (L-462 (a\n  shorter run)).\n- The Daily Run checking the orrery it pulled is the one you pushed\n  (L-461 (pull matches push)).\n'), ("- Oct 20's talks: `DESIGN_talks_rulings_20261020.md`, `HANDOFF_design_talks_*`\n", '- Talks: `DESIGN_talks_rulings_20261020.md`, `DESIGN_talks2_rulings_20261021.md`\n')]},
    {'path': 'documentation/HANDOFF_L456_addresses_build_20261021.md', 'mode': 'edit', 'anchors_only': True, 'zone': None, 'edits': [('## 1. Run order (in this order)\n', '## 0. Closed (October 21, 2026, afternoon)\n\nAll of section 1 has run. The orrery is pushed at\n5102188c51547113c206d12168971c77795ea5f9 and the website at\n1dd25994e60fa063a44814a14d196ba705547c70; the live run read "the\nserved export is the orrery\'s at 5102188c, byte for byte". Your phone\nlook (run record\n`documentation/WHERE_WE_ARE_10-21-26_1217_run_record.md`): the\ngalactic tide\'s and plane\'s links work, and so does the Earth inner\ncore\'s.\n\nFound on your phone after the push, none of it from this build (the\nserved config changed only in citation text between gallery 30db99f\nand 1dd25994):\n\n- **A pink band** across the Sun room in several views (L-463). Your\n  test at 14:03 confirmed the cause: the Galactic Plane\'s ring and pole\n  line, at 100,000 AU, drawn by the phone when the view is close in.\n- **The Sun\'s own drawer row had no link** ("No link on file for this\n  shell"), though the Sun has a NASA page on file (L-464).\n- **The Sun\'s pole citation showed nowhere** a visitor can see, though\n  it is served (L-464).\n\nAll three are fixed in the website patch\n`patch_L463_1_sun_room_fixes_20261021.py`, waiting on your run and\nyour phone: tick Galactic Plane, Go To on the Corona, no band; tap the\nSun\'s own row, NASA\'s link and the pole\'s source.\n\nTwo process items from this afternoon, each its own ledger item:\n\n- **L-461:** the website\'s Daily Run ran before the orrery was pushed,\n  so it served the old citations. The Daily Run should compare the\n  orrery it pulled with your orrery folder\'s newest commit. A push also\n  takes a few minutes to show on GitHub (your note). Until it is built,\n  compare the Pointer join line\'s "against orrery" code with the code\n  GitHub Desktop shows for the orrery push.\n- **L-462:** a short form of the orrery maintenance run for small\n  patches, naming every check it skipped. For a design talk.\n\nThis close patch also carries the ledger lines and Where We Are\nchanges from `HANDOFF_talks2_20261021.md` (talks part 2), as that\nhandoff asked of this session.\n\n## 1. Run order (in this order)\n'), ("## 6. For the next session\n\n1. Confirm both repositories' HEADs and read Tony's newest run record.\n", "## 6. For the next session\n\n1. Confirm both repositories' HEADs and read Tony's newest run record.\n   Then, proposed for Tony's word: the Sun room's phone findings first,\n   with his phone in hand (L-463, the pink band; L-464, the Sun's own\n   row and its pole), before the drawer order.\n")]},
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
    if os.path.exists(led) and "#### [L-461]" in read(led):
        return fail("ERROR: the ledger already holds L-461. This patch "
                    "has run before.")
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
