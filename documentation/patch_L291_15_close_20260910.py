"""
patch_L291_15_close_20260910.py -- close the Earth exhibit and the card model

Built on orrery 1ee1cc617979477e7fd00d607828004f4fe957d2
at https://github.com/tonylquintanilla/palomas_orrery (main)
and gallery 57fd93c62606cb91ed56050885dd7ce6f3852859
at https://github.com/tonylquintanilla/tonyquintanilla.github.io (main).
Both confirmed against the live remotes before this was written.

HOW TO RUN
Save this file in the ORRERY repo root (beside LEDGER_CONSOLIDATED.md).
Open it in VS Code and click Run. Equivalent command:
    python patch_L291_15_close_20260910.py
Success prints one line per file and the next steps. Failure prints STOP
and writes nothing; undo is never needed, but if in doubt, Discard Changes
in GitHub Desktop.

WHY
Tony confirmed the Earth exhibit's Mode 5 on the lobby, desktop and phone,
2026-09-10, at gallery 57fd93c6 -- eight featured cards on each, the
interactive Earth and Moon among them, and on the phone the static Earth
and Moon and Sudan pairs each once. That closes L-291 (the Earth exhibit)
and L-303 (one card per orientation). Tony confirmed the contents of this
patch in chat the same day.

Three-store check performed before writing: interactive-exhibit reads 1.0
and ledger-and-session-records 1.10 in the repo at 1ee1cc61, in the
installed copies this session loaded (byte-identical), and in the
manifest. No stale-skill stop.

WHAT THIS DOES (six files edited, one created, in the ORRERY repo;
applied only if every guard passes)

LEDGER_CONSOLIDATED.md
  L-291 DONE and L-303 DONE, each with its close record. Their loose ends
  re-homed: the rotation period to NEW L-311 (L-291's Gap pointed it at
  L-292, which never mentioned it); the editor's copy defect, two files on
  one card and the two portrait titles to NEW L-312; the planetocentric
  test from L-168 to L-237; the Studio button and the editor's unchecked
  save to L-288. L-310 gains Tony's note on Studio's arrows and what they
  do. L-168's title stops saying its fix is open. Header stamp added.

documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md       v28 -> v29
  Status says Earth is live and complete; the rolling stamp gains v29 and
  drops v26; Section 5a gains the 2026-09-09/10 subsection; two entries
  that placed a handoff in the gallery repo are corrected, visibly.

skills/interactive-exhibit/SKILL.md                     1.0 -> 1.1
  Four places still described one EXHIBIT branch per room; step 3 gains
  the driver rule found by running the resolver; step 7 gains the check
  for an existing card and the order Studio forces; a field note.

skills/ledger-and-session-records/SKILL.md              1.10 -> 1.11
  A Closing Item Re-homes Its Loose Ends [QUALITY].

PROJECT_INSTRUCTIONS.md                                 v3.55 -> v3.56
  The v3.56 entry (binding rule step 3). Header stamp and SHA anchor move.
  v3.53 moves down. The manifest zone is NOT touched: skills_index.py owns
  it.

documentation/PROJECT_INSTRUCTIONS_HISTORY.md
  Receives the v3.53 entry verbatim, with the moved-down note.

documentation/HANDOFF_earth_close_20260910.md           NEW
  This session's handoff. Refuses to overwrite an existing file.

WHAT IS PERMANENT
  The two skill rules, the two new ledger items, the plan's v29 record,
  and the handoff. This script is disposable: once it has run its
  fingerprints describe a tree that no longer exists, and a second run
  stops without writing. Move it into documentation/ after it runs.

Written September 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

FILES = {
    "LEDGER_CONSOLIDATED.md": "34f83fef681e56fc6f2f3205155ea301",
    "documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md": "eeaa4241441e3ef1ff706219b5f01917",
    "skills/interactive-exhibit/SKILL.md": "364b3a21d31fb6aed919719c4daaf4aa",
    "skills/ledger-and-session-records/SKILL.md": "5d021fd7853c1ff33a3f9682a471209c",
    "PROJECT_INSTRUCTIONS.md": "2720685849325b0d0f8740c84840bd63",
    "documentation/PROJECT_INSTRUCTIONS_HISTORY.md": "833116027a41ba63f9d357234acb45ea",
}
NEW_FILE = "documentation/HANDOFF_earth_close_20260910.md"


# =====================================================================
# LEDGER
# =====================================================================

LEDGER_EDITS = [
    # ---- header stamp
    (
        "fixed again; L-290 opened), built on a57e86b8.\n"
        "Review and RICE update Tony 6-21-2026\n",
        "fixed again; L-290 opened), built on a57e86b8.\n"
        "Module updated: September 10, 2026 with Anthropic's Claude Opus 5\n"
        "(L-291 and L-303 closed on Tony's Mode 5; their loose ends re-homed\n"
        "to L-311 and L-312, opened here, and to L-237 and L-288; L-310 gains\n"
        "Studio's prior art; L-168's title), built on 1ee1cc61.\n"
        "Review and RICE update Tony 6-21-2026\n",
    ),
    # ---- L-291
    (
        "<!-- L:291 status:PENDING-GATE upd:2026-09-09 section:A flag: rice:4/4/80/3 -->",
        "<!-- L:291 status:DONE upd:2026-09-10 section:C flag: rice:4/4/80/3 -->",
    ),
    (
        "**Gap:** STEP 7 -- the Studio card via New Interactive Card (the picker\n"
        "reads the EXHIBITS table now; expect `?exhibit=earth`), placed in the\n"
        "editor; then L-291 closes. Tony-action (do). L-305 (magnetosphere) and\n"
        "L-310 (camera steps) are their own items; L-292 (serving the rotation\n"
        "period) is the small orrery patch the axis hover is waiting for.\n",
        "- **STEP 7, 2026-09-09/10 -- the card was made twice.** The first\n"
        "  Earth card (gallery `97ed2012`, 2026-09-09 12:54) was made in the\n"
        "  editor with Copy Card to Room from the static Earth-and-Moon\n"
        "  portrait card, plus a live URL: Tony had not found New Interactive\n"
        "  Card in Studio. The copy kept the portrait's `sibling` stamp, file\n"
        "  and size, so index.html's Featured rule (a 9:16 card yields to a\n"
        "  featured sibling) dropped it from the DESKTOP lobby while the phone\n"
        "  showed it beside the static card. The 2026-09-09 close handoff said\n"
        "  step 7 had not started, because its session never read the\n"
        "  metadata. The 2026-09-10 review\n"
        "  (`documentation/REVIEW_earth_close_20260910.md`) found the card and\n"
        "  replayed the viewer's rule against it. Tony deleted the copy, made\n"
        "  the card in Studio (`earth_and_moon`: no files, no sibling, 9:16,\n"
        "  featured, room `solar_system/earth`) and placed it in the editor.\n"
        "  [verified @ gallery `57fd93c6`]\n"
        "- **CLOSED 2026-09-10 on Tony's Mode 5**, the lobby's Featured strip\n"
        "  on desktop and phone: eight cards on each, the interactive Earth\n"
        "  and Moon among them. [render-confirmed Mode 5 @ gallery `57fd93c6`]\n"
        "- **Loose ends re-homed before closing** (ledger-and-session-records\n"
        "  1.11). Serving the rotation period and obliquity -> L-311; this Gap\n"
        "  had pointed it at L-292, which never mentioned it. The Studio button\n"
        "  that was not found and the editor's unchecked save -> L-288. The\n"
        "  editor's copy defect -> L-312. Camera steps stay L-310, the\n"
        "  magnetosphere L-305, the chrome rename L-309.\n"
        "**Gap:** none.\n",
    ),
    (
        "**Ref:** `documentation/PREDESIGN_earth_exhibit_20260906.md` (gallery),\n"
        "L-292 (shells the orrery does not draw), L-293 (lunar standstill),\n",
        "**Ref:** `documentation/PREDESIGN_earth_exhibit_20260906.md` (gallery),\n"
        "`documentation/REVIEW_earth_close_20260910.md` and\n"
        "`documentation/HANDOFF_earth_close_20260910.md` (orrery), L-311\n"
        "(rotation period), L-312 (editor follow-ons),\n"
        "L-292 (shells the orrery does not draw), L-293 (lunar standstill),\n",
    ),
    # ---- L-303
    (
        "<!-- L:303 status:PENDING-GATE upd:2026-09-09 section:A flag: rice:4/4/80/3 -->",
        "<!-- L:303 status:DONE upd:2026-09-10 section:C flag: rice:4/4/80/3 -->",
    ),
    (
        "**Gap:** Mode 5 on the phone -- one card per figure, the portrait file;\n"
        "on the desktop two cards side by side tagged 16:9 and 9:16. Tony-action\n"
        "(do): retype the portrait title on\n"
        "`artemis_ii_20260402-0411_mission_moon_center2_mobile` and\n"
        "`maps_disintegration_20260403_07_structures_mobile` in the editor.\n"
        "Closes on Tony's eyes.\n",
        "- **CLOSED 2026-09-10 on Tony's Mode 5.** Desktop: the Earth room lists\n"
        "  the static pair side by side, tagged 16:9 and 9:16 (Tony's\n"
        "  screenshot, gallery `de191147`). Phone: in the lobby's Featured\n"
        "  strip the static Earth and Moon and the Sudan cards each appear\n"
        "  once. [render-confirmed Mode 5 @ gallery `57fd93c6`]\n"
        "- **The editor defect recorded above fired before anyone went\n"
        "  looking.** Copy Card to Room put a portrait card's `sibling` stamp\n"
        "  on the first Earth exhibit card and hid it from the desktop lobby\n"
        "  (L-291, step 7). Re-homed to L-312 with the two-files-on-one-card\n"
        "  case.\n"
        "- **The two portrait titles are deferred** -- Tony, 2026-09-10, on the\n"
        "  review: \"deferred to the braid. not critical.\" Re-homed to L-312,\n"
        "  with the titles recovered from git history.\n"
        "**Gap:** none.\n",
    ),
    # ---- L-168
    (
        "#### [L-168] propagate_marker uses solar K_GAUSS mean-motion -- wrong for planetocentric moon markers (FLAG-2; caught in F1 design, avoided in serving, source fix still open)\n"
        "<!-- L:168 status:DONE upd:2026-09-09 section:W.Done flag: rice:3/3/80/2 -->",
        "#### [L-168] propagate_marker uses solar K_GAUSS mean-motion -- wrong for planetocentric moon markers (FLAG-2; caught in F1 design, avoided in serving, fixed at source 2026-09-09)\n"
        "<!-- L:168 status:DONE upd:2026-09-10 section:W.Done flag: rice:3/3/80/2 -->",
    ),
    (
        "  Earth only. Add when `test_artifact1_earth.py` is next open; the pin\n"
        "  compares its verdicts by name, so a new verdict is a pin change.\n",
        "  Earth only. Add when `test_artifact1_earth.py` is next open; the pin\n"
        "  compares its verdicts by name, so a new verdict is a pin change.\n"
        "  **Re-homed 2026-09-10 to L-237**, which opens that file. (Title\n"
        "  corrected the same day: it said the source fix was still open.)\n",
    ),
    # ---- L-237
    (
        "<!-- L:237 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/90/1 -->",
        "<!-- L:237 status:OPEN upd:2026-09-10 section:A flag: rice:3/4/90/1 -->",
    ),
    (
        "**Gap:** re-cut it. Pair with the L-235 T5 fix -- re-cutting a record\n"
        "that nothing compares against buys very little.\n",
        "- **Carries a test from L-168, re-homed 2026-09-10.** When\n"
        "  `gallery/assembler/tests/test_artifact1_earth.py` is open for the\n"
        "  re-cut: a Python-side `as_of_today` check for a PLANETOCENTRIC body.\n"
        "  T1 checks Earth only, and the moon marker bug L-168 fixed was right\n"
        "  at the fixture's epoch by luck. L-168 records the numbers to pin,\n"
        "  as fractions of r against Horizons in the live cache: Earth 8.8e-12,\n"
        "  Moon 2.3e-10, Io 2.6e-9, Titan 2.0e-10. The pin compares verdicts by\n"
        "  name, so the new verdict is a pin change.\n"
        "**Gap:** re-cut it, with the planetocentric test above. Pair with the\n"
        "L-235 T5 fix -- re-cutting a record that nothing compares against buys\n"
        "very little.\n",
    ),
    # ---- L-288
    (
        "<!-- L:288 status:OPEN upd:2026-09-08 section:A flag: rice:3/3/70/2 -->",
        "<!-- L:288 status:OPEN upd:2026-09-10 section:A flag: rice:3/3/70/2 -->",
    ),
    (
        "**Gap:** the live-card converter path above; the Earth-and-Moon\n"
        "portrait re-export; then DONE.\n",
        "- **From the Earth card, 2026-09-09/10 (L-291, step 7): two controls\n"
        "  that were needed existed, and neither was found.** (1) Tony did not\n"
        "  see New Interactive Card in Studio on his first look and made the\n"
        "  card by copying instead, which is how L-312's pairing-tag defect\n"
        "  reached a live card. Measured at gallery `57fd93c6`: the button is\n"
        "  fourth of four in the action row (Preview, Export HTML..., Export\n"
        "  Encounter..., New Interactive Card...; widths 12, 14, 18 and 20\n"
        "  characters) in a 960x720 window with an 800x500 minimum. The row is\n"
        "  not wide enough to clip sideways, so the cause is NOT established.\n"
        "  Its tooltip still reads \"the Sun today; Earth when its exhibit\n"
        "  exists.\" (2) Tony asked for a refresh button after the editor did\n"
        "  not show the card Studio had just written. The editor has one: File\n"
        "  > Reload from disk (`_reload`). It is not on the toolbar.\n"
        "- **The hazard behind (2) is not the missing button.** Save All writes\n"
        "  the editor's in-memory copy of both files with no check that the\n"
        "  disk changed since it loaded them, so an editor left open while\n"
        "  Studio writes a card would save over that card. Two forms, recorded\n"
        "  and not ruled: Reload on the toolbar, which works when remembered;\n"
        "  or a check at save that the files on disk are still the ones loaded,\n"
        "  which fires unprompted.\n"
        "- **Studio refused a second card for `?exhibit=earth` while the copy\n"
        "  existed** -- correct. The working order is in interactive-exhibit\n"
        "  1.1, step 7.\n"
        "**Gap:** the live-card converter path above; the Earth-and-Moon\n"
        "portrait re-export; the 2026-09-10 findings (the Studio button's\n"
        "cause and tooltip, the editor's save check); then DONE.\n",
    ),
    # ---- L-310
    (
        "<!-- L:310 status:OPEN upd:2026-09-09 section:A flag: rice:3/3/70/2 -->",
        "<!-- L:310 status:OPEN upd:2026-09-10 section:A flag: rice:3/3/70/2 -->",
    ),
    (
        "**Gap:** design round with Tony; then build. Not blocking L-291.\n",
        "- **Tony, 2026-09-10 (from chat, not his hand), confirming this as the\n"
        "  next track:** \"note that the studio already has directional button\n"
        "  option: navigation controls/pan zoom arrows.\"\n"
        "- **What that option does, read at gallery `57fd93c6`.** Studio's\n"
        "  Navigation Controls section, \"Show pan/zoom arrows\"\n"
        "  (`show_nav_arrows`), embeds buttons in the HTML that Studio\n"
        "  EXPORTS. A 2D chart gets a full D-pad whose arrows shift the axis\n"
        "  ranges, plus zoom and reset. On a polar chart, left and right rotate\n"
        "  the angular axis 15 degrees a press. A 3D scene gets reset and zoom\n"
        "  ONLY, and Studio's own comment and tooltip give the reason: the\n"
        "  directional arrows had no detectable effect in 3D, and the D-pad\n"
        "  blocked the animation slider. So the prior art is real, and its 3D\n"
        "  half was tried and withdrawn. A 3D step has to move\n"
        "  `scene.camera.eye` (the bullet above), not the ranges; the polar\n"
        "  rotation is the nearer model.\n"
        "- **Three control sets exist, one per kind of page.** HTML exported by\n"
        "  Studio carries Studio's; the gallery viewer, `index.html`, draws its\n"
        "  own inline cluster; the exhibit rooms use `gallery/nav_cluster.js`.\n"
        "  A camera step designed here lands in the cluster. L-285 already\n"
        "  records moving `index.html` onto the cluster.\n"
        "**Gap:** design round with Tony; then build. Not blocking L-291.\n",
    ),
    # ---- insert L-311 and L-312 after L-310
    (
        "#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery\n",
        "#### [L-311] Earth's rotation period and obliquity are not served, so the axis hover names neither\n"
        "<!-- L:311 status:OPEN upd:2026-09-10 section:A flag: rice:2/2/90/1 -->\n"
        "- **Opened 2026-09-10, re-homed from L-291 as it closed.** The Earth\n"
        "  room's axis hover says the rotation is not shown and names no\n"
        "  period, and the 23.44 degree tilt it states is DERIVED -- the served\n"
        "  pole through the renderer's sourced mean obliquity -- and says so\n"
        "  (L-291, step 3 record). Neither number is in Earth's served entry.\n"
        "- **Why it has its own row.** L-291's Gap and the 2026-09-09 close\n"
        "  handoff both sent this to L-292, which is \"Earth shells the orrery\n"
        "  does not draw\" and never mentioned it. Found by the 2026-09-10\n"
        "  review.\n"
        "- **What the store already holds, read at orrery `1ee1cc61`.**\n"
        "  `EARTH_ROTATION_RATE_RAD_S = 7.292115e-5`, sourced to IERS\n"
        "  Conventions (2010), TN36 Table 1.1, nominal mean angular velocity.\n"
        "  A sidereal period follows from it as a DERIVED constant; nothing new\n"
        "  needs sourcing for the period. No obliquity constant was found by\n"
        "  name; the renderer's sourced value is the place to start.\n"
        "- **Scope when opened.** Period (derived) and obliquity (sourced) in\n"
        "  `constants_new.py`; served rows in Earth's entry with value / unit /\n"
        "  source / orrery_constant; store drift reads MATCH by name; the axis\n"
        "  hover states both with their sources. Orrery and gallery move\n"
        "  together.\n"
        "- **Note:** RICE 2/2/90/1 -> 3.6 proposed, not confirmed.\n"
        "**Gap:** the serving patch above, when a session has `constants_new.py`\n"
        "open.\n"
        "**Ref:** L-291 (step 3 record), L-292 (not this), provenance-discipline\n"
        "(the store), interactive-exhibit (the served-data contract).\n"
        "\n"
        "#### [L-312] The gallery editor's copy and file slots make cards the viewer misreads; two portrait titles to retype\n"
        "<!-- L:312 status:OPEN upd:2026-09-10 section:A flag: rice:2/2/85/1 -->\n"
        "- **Opened 2026-09-10, re-homed from L-303 as it closed.** One row for\n"
        "  the class: editor-side follow-ons of the card-per-orientation change,\n"
        "  cleared the next time a session has `tools/gallery_editor.py` open\n"
        "  (The Braid).\n"
        "- **(1) Copy Card to Room carries the source card's `sibling`, `files`\n"
        "  and `size_kb`.** `_copy_to_room` deep-copies the card and resets only\n"
        "  id, room and featured. L-303 recorded it as unguarded. It fired on\n"
        "  the first Earth exhibit card, 2026-09-09: a copy of the static\n"
        "  Earth-and-Moon portrait with a live URL added kept the portrait's\n"
        "  sibling stamp, and index.html's Featured rule (a 9:16 card yields to\n"
        "  a featured sibling) dropped it from the desktop lobby (L-291, step\n"
        "  7). The toolbar tooltip for Copy to Room reads \"Put a second card\n"
        "  for this exhibit in another room\", which invites exactly that use.\n"
        "  Fix shape, not ruled: the copy drops `sibling`; a copy that gains a\n"
        "  live URL drops its files too.\n"
        "- **(2) The editor can still put two files on one card** (Set Landscape\n"
        "  File and Set Portrait File on the same card), which L-303 retired.\n"
        "  The viewer tolerates it. A guard in the editor, or a\n"
        "  `sweep_report.py` class.\n"
        "- **(3) Two portrait titles lost in the L-301 merge, deferred.** Tony,\n"
        "  2026-09-10: \"deferred to the braid. not critical.\" The titles\n"
        "  before the merge, from gallery metadata before `b5622a8`:\n"
        "  - `artemis_ii_20260402-0411_mission_moon_center2_mobile`: Artemis II\n"
        "    - Earth to Moon Flyby April 6, 2026\n"
        "  - `maps_disintegration_20260403_07_structures_mobile`: MAPS -\n"
        "    Disintegration April 4, 2026\n"
        "  Tony-action (do), when the editor is next open: retype both.\n"
        "- **Note:** RICE 2/2/85/1 -> 3.4 proposed, not confirmed.\n"
        "**Gap:** (1) and (2) in the next editor session; (3) at the same time.\n"
        "**Ref:** L-303, L-291 (step 7), L-288 (the Studio half),\n"
        "`tools/gallery_editor.py` (`_copy_to_room`, `_build_toolbar`),\n"
        "index.html (the Featured rule), `tools/sweep_report.py`.\n"
        "\n"
        "#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery\n",
    ),
]


# =====================================================================
# MASTER PLAN v29
# =====================================================================

MP_EDITS = [
    (
        "**Status:** v28 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n",
        "**Status:** v29 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n",
    ),
    (
        "5). **The second exhibit, EARTH, has its DATA SERVED and its CODE NOT\n"
        "YET WRITTEN** (L-291): steps 0-2 of the interactive-exhibit skill are\n"
        "done on both repos as of 2026-09-08 -- 21 sourced constants in the\n"
        "orrery store, every Earth shell reading them, and a nine-group served\n"
        "entry whose 24 pointers read MATCH on the live run. Step 3, the\n"
        "`EXHIBIT === \"earth\"` branch, is next AND IS SPLIT: it proceeds on\n"
        "the eleven sourced features, and the magnetosphere is deferred to\n"
        "L-305 for a rebuild on a cited model, absent and named in the\n"
        "meantime rather than approximate.\n",
        "5). **The second exhibit, EARTH, is LIVE AND COMPLETE** (L-291, closed\n"
        "2026-09-10 on Tony's Mode 5): `interactive.html?exhibit=earth`,\n"
        "shells plus the Moon, arriving at low Earth orbit -- eleven sourced\n"
        "features, the axis, the Sun line and terminator, and the Moon on its\n"
        "trusted arc -- with its card featured in the lobby (gallery\n"
        "`57fd93c6`). The magnetosphere is absent and named until its rebuild\n"
        "on a cited model (L-305). Earth made the rooms a TABLE, `EXHIBITS` in\n"
        "`interactive.html`, one row per room, and it found L-168, the\n"
        "planetocentric mean-motion bug, on the first moon it drew.\n",
    ),
    (
        "parameter -- is next and is unblocked. Handoff:\n"
        "`documentation/HANDOFF_earth_step3_20260908.md` in the gallery repo.\n",
        "parameter -- is next and is unblocked. Handoff:\n"
        "`documentation/HANDOFF_earth_step3_20260908.md` in the orrery repo\n"
        "[this read \"gallery repo\" until v29; the file was only ever in the\n"
        "orrery].\n",
    ),
    (
        "is unblocked on six of its seven items. Handoff:\n"
        "`documentation/HANDOFF_earth_step3_20260908.md` in the gallery repo,\n"
        "superseded in part by this round.\n",
        "is unblocked on six of its seven items. Handoff:\n"
        "`documentation/HANDOFF_earth_step3_20260908.md` in the orrery repo\n"
        "[\"gallery repo\" until v29], superseded in part by this round.\n",
    ),
    (
        "### What this section deliberately does not carry\n",
        "### 2026-09-09/10 -- Earth ships, and its card finds a gap in the handoff\n"
        "\n"
        "Measured at orrery `1ee1cc61` and gallery `57fd93c6`, both confirmed\n"
        "against the live remotes. Appended, not merged.\n"
        "\n"
        "**Step 3 built, then three Mode 5 rounds** (L-291). `?exhibit=earth`\n"
        "became the second row of an `EXHIBITS` table the shared chrome reads,\n"
        "and `gallery/earth_geometry.js` composes the room: the served shells,\n"
        "the axis and equator from the served pole, the Sun line and terminator\n"
        "as geometry rather than lighting, the GEO ring, and the Moon on its\n"
        "trusted arc. Running the assembler corrected the step-3 handoff three\n"
        "times: Earth is the CENTER and not an object, the Moon's trust window\n"
        "is read from the record, and a belt beyond the frame goes to the\n"
        "drawer. Tony read the Moon's woven arc as points too far apart in\n"
        "time. That was L-168 -- solar mean motion applied to a planetocentric\n"
        "orbit, caught in July, designed, and left open until the first moon\n"
        "rendered. Fixed at source.\n"
        "\n"
        "**The card was made twice.** The first Earth card was a copy of the\n"
        "static Earth-and-Moon portrait with a live URL added, because the\n"
        "Studio button was not found. The copy kept the portrait's pairing\n"
        "tag, so the lobby's Featured rule hid it on the desktop while the\n"
        "phone showed it. The handoff written that night said the card step\n"
        "had not started; its session never read the metadata. A review the\n"
        "next morning did, replayed the viewer's rule against it, and Tony\n"
        "rebuilt the card in Studio. Mode 5 on the lobby, desktop and phone,\n"
        "closed L-291 and L-303 (one card per orientation).\n"
        "\n"
        "**Loose ends became a rule.** Three unfinished tasks were riding\n"
        "inside items that had closed or were about to, one of them behind a\n"
        "pointer to an item that never mentioned it. They went to L-311 (the\n"
        "rotation period), L-312 (the editor's copy defect and two titles),\n"
        "L-237 (a planetocentric test) and L-288 (the Studio button and the\n"
        "editor's unchecked save). ledger-and-session-records 1.11 makes\n"
        "re-homing part of closing; interactive-exhibit 1.1 corrects the\n"
        "places that still described one branch per room. Protocol v3.56.\n"
        "\n"
        "**What this does to the order.** Step 3 of the 2026-09-03 order,\n"
        "Earth into the assembler, bundled three items. The room is done.\n"
        "L-237, Artifact 1's golden record, is still open and now also carries\n"
        "the planetocentric test. L-268 does not record whether Earth's slice\n"
        "was discharged by step 2's rebuild of the served entry; that is for\n"
        "L-268's next session to settle. Step 4, the transport, was not built\n"
        "alongside Earth and still stands before step 5, Jupiter and Saturn.\n"
        "Tony's next track is the L-310 camera-step design round -- shared\n"
        "chrome, zero code -- taken beside the order, not as a step in it.\n"
        "Handoff: `documentation/HANDOFF_earth_close_20260910.md` in the\n"
        "orrery repo.\n"
        "\n"
        "### What this section deliberately does not carry\n",
    ),
]

MP_LU_START = "**Last updated:** September 8, 2026 (v28, evening: a DESIGN BUILD,\n"
MP_V26_MARK = " v26,\nSeptember 6, 2026: the EARTH exhibit designed in\n"
MP_LU_END = "\n**Participants:**"
MP_LU_NEW_HEAD = (
    "**Last updated:** September 10, 2026 (v29: the Earth BUILD closes.\n"
    "Step 3 built and through three Mode 5 rounds; L-168 fixed at source\n"
    "on the first moon it could affect; the card made in Studio after a\n"
    "copied card hid from the desktop lobby; L-291 and L-303 closed on\n"
    "Tony's Mode 5; loose ends re-homed to L-311, L-312, L-237 and L-288;\n"
    "next track the L-310 camera-step design round; two handoff locations\n"
    "corrected; Section 5a gains the 2026-09-09/10 subsection; with\n"
    "Anthropic's Claude Opus 5. v28, September 8, 2026, evening: a DESIGN BUILD,\n"
)


# =====================================================================
# interactive-exhibit 1.0 -> 1.1
# =====================================================================

IE_EDITS = [
    (
        "Skill version: 1.0 | Cut from gallery @ fc8d9fb3 (interactive.html,\n"
        "feature_renderers.js, data/objects_config.json, gallery_maintenance_run.py,\n"
        "tools/gallery_studio.py) and orrery @ a57e86b8 (LEDGER_CONSOLIDATED.md\n"
        "L-260, L-267, L-278, L-282, L-288, L-289) | 2026-09-06\n",
        "Skill version: 1.1 | Cut from gallery @ 57fd93c6 (interactive.html,\n"
        "index.html, tools/json_converter.py, tools/gallery_studio.py,\n"
        "tools/gallery_editor.py) and orrery @ 1ee1cc61 (LEDGER_CONSOLIDATED.md\n"
        "L-291, L-303, L-309) | 2026-09-10, with Anthropic's Claude Opus 5\n"
        "v1.1 (L-291) corrects what Earth step 3 made untrue and adds what its\n"
        "close taught about carding. The page picks a room from an `EXHIBITS`\n"
        "table now, not an `EXHIBIT === \"<key>\"` branch, and four places still\n"
        "said branch: the anatomy's switch and class rows, step 3, and step\n"
        "7's picker. Step 3 gains the driver rule the build found by running\n"
        "the resolver; step 7 gains the check for an existing card and the\n"
        "order Studio forces; the rename paragraph points at L-309, which\n"
        "deferred it; one field note.\n"
        "Earlier: v1.0 cut from gallery @ fc8d9fb3 (interactive.html,\n"
        "feature_renderers.js, data/objects_config.json, gallery_maintenance_run.py,\n"
        "tools/gallery_studio.py) and orrery @ a57e86b8 (LEDGER_CONSOLIDATED.md\n"
        "L-260, L-267, L-278, L-282, L-288, L-289) | 2026-09-06\n",
    ),
    (
        "## The anatomy of an exhibit (the Sun, read at fc8d9fb3)\n",
        "## The anatomy of an exhibit (the Sun, read at fc8d9fb3; two rows corrected at 1.1)\n",
    ),
    (
        "| `EXHIBIT` switch: `?exhibit=` lower-cased, default `solar-system-explorer` | interactive.html, SUN EXHIBIT block | shared; a new room adds one `EXHIBIT === \"<key>\"` branch |\n",
        "| `EXHIBIT` switch: `?exhibit=` lower-cased, default `solar-system-explorer`; `EX = EXHIBITS[EXHIBIT]` is the room | interactive.html, `const EXHIBITS` | shared; a new room adds one ROW to `EXHIBITS` -- title, sceneTitle, pngName, halfRangeAu, driver, infoHtml, compose (since Earth step 3, L-291; at fc8d9fb3 it was one `EXHIBIT === \"<key>\"` branch per room) |\n",
    ),
    (
        "| `body.<key>-exhibit` class and `.<key>-chrome` show/hide rule | `applySunChrome()`, CSS | per-body class, shared mechanism |\n",
        "| `body.sun-exhibit` class and `.sun-chrome` show/hide rule, added for EVERY room | `applySunChrome()`, CSS | shared; the name stays `sun` until the rename (L-309) -- at fc8d9fb3 this row read per-body `body.<key>-exhibit` |\n",
    ),
    (
        "The naming carries a debt: most shared pieces are called `sun*` because\n"
        "the Sun was first. The second exhibit is the moment to rename or\n"
        "parametrize them, not to copy them under `earth*`. One drawer, one nav\n"
        "cluster, one HUD, one i-panel; the body is a parameter.\n",
        "The naming carries a debt: most shared pieces are called `sun*` because\n"
        "the Sun was first. The rule is to rename or parametrize them, never to\n"
        "copy them under `earth*`. One drawer, one nav cluster, one HUD, one\n"
        "i-panel; the body is a parameter. Earth, the second room, PARAMETRIZED\n"
        "through the `EXHIBITS` table and kept the names: a rename touches about\n"
        "a hundred identifiers in a working room for no change a visitor sees,\n"
        "and would put the Sun back under Mode 5. It is deferred to the third\n"
        "room or a free session, with the names to reach for (L-309).\n",
    ),
    (
        "3. Code: one `EXHIBIT === \"<key>\"` branch; a driver spec with the body\n"
        "   as `objects` and `center`; the body's half-range floor; the layout\n"
        "   builder's per-body values; i-panel copy with sources inline. Reuse\n"
        "   the shared chrome by parameter, renaming `sun*` where the second\n"
        "   user makes the name wrong.\n",
        "3. Code: one row in `EXHIBITS`; a driver spec whose `center` is the\n"
        "   body; the body's half-range floor; the layout builder's per-body\n"
        "   values; i-panel copy with sources inline. What goes in `objects` is\n"
        "   whatever the resolver accepts against that centre -- RUN it, do not\n"
        "   infer it. The Sun room passes `[\"sun\"]`. Earth as an object is\n"
        "   rejected, because the cache stores it relative to the Sun, so the\n"
        "   Earth room passes `[\"moon\"]` and Earth's own shells arrive by the\n"
        "   centre-features path (L-291). Reuse the shared chrome by parameter\n"
        "   (L-309 on names).\n",
    ),
    (
        "7. Card: Studio -> New Interactive Card (L-288) -> pick the scene (the\n"
        "   picker reads `EXHIBIT === \"<key>\"` literally from the page source, so\n"
        "   the key must appear in that form) -> title, placard, sources -> lands\n"
        "   in Storage -> the editor places it; featured if it belongs on the\n"
        "   lobby.\n",
        "7. Card. FIRST read `gallery/gallery_metadata.json` for a card whose\n"
        "   `live` already opens `interactive.html?exhibit=<key>`: Studio\n"
        "   refuses a second one, and a card made some other way may already\n"
        "   exist. Then Studio -> New Interactive Card (L-288) -> pick the scene\n"
        "   (`live_scene_urls()` in `tools/json_converter.py` reads the keys of\n"
        "   the page's `EXHIBITS` table, and the older branch form too) ->\n"
        "   title, placard, sources -> it lands in Storage -> in the editor,\n"
        "   File > Reload from disk (an open editor does not see Studio's\n"
        "   write, and its Save All would write over it) -> place it; featured\n"
        "   if it belongs on the lobby. Never make an exhibit card with the\n"
        "   editor's Copy Card to Room: the copy keeps the source card's\n"
        "   pairing tag (field note 2026-09-10).\n",
    ),
    (
        "- 2026-09-06, L-288: Studio authors the exhibit's card; the card is a\n"
        "  placard with an Interactive tag and needs no picture (the lobby\n"
        "  settled that on the phone).\n",
        "- 2026-09-06, L-288: Studio authors the exhibit's card; the card is a\n"
        "  placard with an Interactive tag and needs no picture (the lobby\n"
        "  settled that on the phone).\n"
        "- 2026-09-10, L-291 step 7: the first Earth card was a COPY -- Copy\n"
        "  Card to Room on the static Earth-and-Moon portrait, then a live URL\n"
        "  -- made because the Studio button was not found. It kept the\n"
        "  portrait's `sibling` stamp, file and size, and index.html's Featured\n"
        "  rule (a 9:16 card yields to a featured sibling) dropped it from the\n"
        "  DESKTOP lobby while the phone showed it. The handoff written the\n"
        "  night before said step 7 had not started: its session never read the\n"
        "  metadata. A replay of the viewer's rule against the served metadata\n"
        "  predicted both screens before Tony looked, and was right. Fixed by\n"
        "  delete, then Studio, then the editor, in that order. The editor's\n"
        "  Reload from disk existed and was not found either (L-288, L-312).\n",
    ),
    (
        "Author here: `skills/interactive-exhibit/SKILL.md` in the orrery repo.\n"
        "Install to the account (Settings > Skills). Run `skills_index.py` so the\n"
        "manifest in PROJECT_INSTRUCTIONS.md gains the row. Per Stale Skill =\n"
        "Stop, the session that installs it cannot verify the install; the Earth\n"
        "session confirms its loaded copy reads 1.0 before building.\n",
        "Author here: `skills/interactive-exhibit/SKILL.md` in the orrery repo.\n"
        "Install to the account (Settings > Skills). Run `skills_index.py` so the\n"
        "manifest in PROJECT_INSTRUCTIONS.md carries the version. Per Stale Skill\n"
        "= Stop, the session that installs a version cannot verify the install.\n"
        "1.0 was confirmed by the Earth sessions; the first session after 1.1's\n"
        "push confirms its loaded copy reads 1.1 before exhibit work.\n",
    ),
]


# =====================================================================
# ledger-and-session-records 1.10 -> 1.11
# =====================================================================

LS_EDITS = [
    (
        "Skill version: 1.10 | Cut from palomas_orrery @ 50cbd2df (v1.10),\n"
        "earlier @ 41c0b279 (v1.9), @ 3586970d (v1.8), @ 434a712b (v1.7),\n"
        "@ 305b269 (v1.6), @ 3398970 (v1.5) | September 6, 2026, with\n"
        "Anthropic's Claude Opus 5\n",
        "Skill version: 1.11 | Cut from palomas_orrery @ 1ee1cc61 (v1.11),\n"
        "earlier @ 50cbd2df (v1.10), @ 41c0b279 (v1.9), @ 3586970d (v1.8),\n"
        "@ 434a712b (v1.7), @ 305b269 (v1.6), @ 3398970 (v1.5) | September 10,\n"
        "2026, with Anthropic's Claude Opus 5\n",
    ),
    (
        "junctures\", which was not countable and so kept returning the judgment\n"
        "to Tony.\n",
        "junctures\", which was not countable and so kept returning the judgment\n"
        "to Tony. v1.11 (L-291) adds A Closing Item Re-homes Its Loose Ends:\n"
        "before an item goes DONE, each thing its body records as not done gets\n"
        "a home in an open item, or is struck with a reason. Three were found\n"
        "riding inside closing items on 2026-09-10, one of them behind a pointer\n"
        "to an item that never mentioned it.\n",
    ),
    (
        "### Cluster the Tail by Topic, Not by Age [QUALITY]\n",
        "### A Closing Item Re-homes Its Loose Ends [QUALITY]\n"
        "\n"
        "Before an item's status goes to DONE, read its body for work it\n"
        "records as NOT done -- \"not done, recorded\", \"add when X is next\n"
        "open\", a Gap saying another item carries something. Each one gets one\n"
        "of two outcomes in the closing patch:\n"
        "\n"
        "- a line in an OPEN item whose files that work will open (by files\n"
        "  touched, as in the section below), naming the closing item; or\n"
        "- struck in the closing item, with the reason.\n"
        "\n"
        "The closing item's own record then says where each one went, by\n"
        "handle.\n"
        "\n"
        "The reason is where readers look. A closed item moves to section C,\n"
        "and section C is institutional memory, not a backlog: no session\n"
        "opens it to find the next job. A not-done line inside it is a floating\n"
        "item that happens to have a handle -- Capture on First Mention\n"
        "satisfied in form and defeated in effect.\n"
        "\n"
        "Check a pointer as well as a line. A Gap saying \"L-NNN carries it\" is\n"
        "a claim about another block; open that block and find the work in it.\n"
        "\n"
        "(Origin, 2026-09-10, closing L-291 and L-303; Tony confirmed it as\n"
        "method rather than a ruling. Three loose ends: Earth's rotation\n"
        "period, recorded in L-291's body and pointed by its Gap and its\n"
        "handoff at L-292, which never mentioned it; a planetocentric\n"
        "`as_of_today` test inside L-168, closed the day before; and the\n"
        "gallery editor's Copy carrying a card's pairing tag, inside L-303 --\n"
        "which had already fired on the first Earth card, hiding it from the\n"
        "desktop lobby, before anyone looked. L-311, L-237 and L-312 received\n"
        "them.)\n"
        "\n"
        "### Cluster the Tail by Topic, Not by Age [QUALITY]\n",
    ),
]


# =====================================================================
# PROTOCOL v3.56 and HISTORY
# =====================================================================

PI_HEADER_OLD = "Tony Quintanilla, PE | Claude | v3.55 | September 8, 2026\n"
PI_HEADER_NEW = "Tony Quintanilla, PE | Claude | v3.56 | September 10, 2026\n"
PI_ANCHOR_OLD = "Cut from 159c5a2c at https://github.com/tonylquintanilla/palomas_orrery\n"
PI_ANCHOR_NEW = "Cut from 1ee1cc61 at https://github.com/tonylquintanilla/palomas_orrery\n"
PI_ENTRY_ANCHOR = "An entry lives in exactly one place, never both.\n\n"
PI_ENTRY = """v3.56 (September 10, 2026): No rule changed in this document. TWO skill
bumps, both from closing the Earth exhibit (L-291).

interactive-exhibit 1.0 -> 1.1. Earth step 3 moved the page from one
`EXHIBIT === "<key>"` branch per room to an `EXHIBITS` table, and the
skill still described the branch in four places: the anatomy's switch
and class rows, step 3, and step 7's scene picker. Step 3 also gains
the driver rule the build found by running the resolver -- the body is
the CENTER, and `objects` is whatever the resolver accepts against it --
and step 7 gains a check for an existing card before Studio is opened,
with the order Studio forces. The rename paragraph now points at L-309,
which deferred the rename with its trigger.

ledger-and-session-records 1.10 -> 1.11. A Closing Item Re-homes Its
Loose Ends [QUALITY]: before an item goes DONE, each thing its body
records as not done gets a home in an open item, or is struck with a
reason. Three were riding inside closing items, one behind a pointer to
an item that never mentioned it, and one had already fired -- the
gallery editor's copy defect, recorded inside L-303, hid the first Earth
card from the desktop lobby.

THE CARD IS THE LESSON, and it is Verify Execution, Not Appearance one
layer out. The 2026-09-09 handoff said step 7, the card, had not
started. A card for the exhibit had been in the gallery since that
afternoon, made by copying a static card, and the session never read
the metadata that showed it. A review read it the next morning,
replayed the viewer's Featured rule against it, and predicted what each
screen would show; Tony's eyes then agreed. A handoff's claim about a
step is checked against the artifact that step produces.

Both skills read the same in all three stores before the bump. This
session loaded 1.0 and 1.10, so the obligation travels as usual:
interactive-exhibit went to 1.1 and ledger-and-session-records to 1.11
in patch_L291_15; the next session confirms its loaded copies read 1.1
and 1.11 before exhibit or ledger work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.53 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""
V53_START = "v3.53 (September 3, 2026): One clause corrected, one note added. No\n"
V53_END = "\nFunctional for Claude, readable for human, signal preserved."
HI_INSERT_BEFORE = "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n"
HI_MOVED_NOTE = ("\n\n(Moved down from the resident protocol on 2026-09-10 when v3.56\n"
                 "made a fourth entry.)\n\n\n")


# =====================================================================
# HANDOFF (new file)
# =====================================================================

HANDOFF = """# Earth exhibit closed; L-291 and L-303 DONE; two skill bumps

Built on orrery `1ee1cc617979477e7fd00d607828004f4fe957d2`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `57fd93c62606cb91ed56050885dd7ce6f3852859`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
Pushed at: orrery -- the commit carrying `patch_L291_15_close_20260910.py`
(the next session reads it from `git log`). Gallery did not move.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-10
Type: DOCUMENTATION (review and closing patch; no code).
Protocol v3.56. Handles: L-291, L-303, L-168, L-237, L-288, L-310,
L-311, L-312.

**Supersedes** the OPEN list of `HANDOFF_earth_step3_close_20260909.md`.
**Companions:** `documentation/REVIEW_earth_close_20260910.md` (the
review, with Tony's annotations); `patch_L291_15_close_20260910.py`.

---

## STEP 0 -- Gates for the next session

- **Skill obligation.** interactive-exhibit went 1.0 -> 1.1 and
  ledger-and-session-records 1.10 -> 1.11 in `patch_L291_15`. This
  session loaded 1.0 and 1.10, which matched the repo, the install and
  the manifest before the bump. The next session confirms its loaded
  copies read 1.1 and 1.11 before exhibit or ledger work. L-310's design
  round fires interactive-exhibit, so its load is the check.
- `git ls-remote` both repos. Orrery should be one commit past
  `1ee1cc61`, or two if the spent patch was moved separately; gallery
  should still be `57fd93c6` unless a nightly ran.

## WHAT HAPPENED

- **The review found the card step already done, badly.** A card
  opening `?exhibit=earth` had been in the gallery since 2026-09-09
  12:54, made in the editor by copying the static Earth-and-Moon portrait
  card. It kept the portrait's pairing tag, so the lobby's Featured rule
  hid it on the desktop. The prior handoff said the step had not
  started.
- **Tony rebuilt the card** -- deleted the copy, New Interactive Card in
  Studio, placed and featured in the editor -- and pushed gallery
  `57fd93c6`. The first SHA he reported, `77165da`, was the orrery
  commit saving his annotated review; the round trip showed the gallery
  had not moved yet, and his screenshot at 9:52 matched the old copy.
- **Mode 5, desktop and phone, on the lobby**: eight featured cards on
  each, the interactive Earth and Moon among them; on the phone the
  static pairs appear once. L-291 and L-303 closed.
- **Two controls existed and were not found**: Studio's New Interactive
  Card button (cause not established) and the editor's File > Reload
  from disk. Both recorded in L-288.
- **L-310's prior art, from Tony**: Studio's pan/zoom arrows. Read at
  `57fd93c6`, they are a full D-pad for 2D, a 15-degree rotation for
  polar, and reset-and-zoom only for 3D, withdrawn because the arrows
  had no detectable effect there. Recorded in L-310.

## WHAT `patch_L291_15` CHANGED

| File | Change |
|---|---|
| `LEDGER_CONSOLIDATED.md` | L-291, L-303 DONE; L-311, L-312 opened; L-237, L-288, L-310, L-168 amended; header stamp |
| `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` | v29; Section 5a 2026-09-09/10; two handoff locations corrected |
| `skills/interactive-exhibit/SKILL.md` | 1.1 |
| `skills/ledger-and-session-records/SKILL.md` | 1.11 |
| `PROJECT_INSTRUCTIONS.md` | v3.56; v3.53 moved down |
| `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` | receives v3.53 |
| `documentation/HANDOFF_earth_close_20260910.md` | this file |

## OPEN, IN ORDER

1. **L-310, the camera-step design round** -- Tony's pick, zero code,
   works from the phone. Start from its 2026-09-10 bullets: a 3D step
   moves the camera eye, not the ranges; three control sets exist
   (L-285).
2. **L-311** -- serve Earth's rotation period (derived from the store's
   IERS rate) and obliquity; the axis hover states them. Both repos.
3. **L-305** -- the magnetosphere on Jelinek et al. 2012; its own design
   session first.
4. **The plan's order**: L-237 (re-cut Artifact 1's record, now with the
   planetocentric test), step 4 the transport, step 5 Jupiter and
   Saturn. Whether Earth's slice of L-268 is done is unrecorded.
5. **When Studio or the editor is next open**: L-288's findings and
   L-312 (the copy defect, two files on one card, two titles).

## TONY-ACTION ROLLUP

1. **(do)** Run `patch_L291_15_close_20260910.py` (orrery root, Run).
2. **(do)** Run `skills_index.py` (Run). It rewrites the manifest rows
   to 1.1 and 1.11.
3. **(do)** Copy `PROJECT_INSTRUCTIONS.md` to
   `documentation/project_instructions_v3_56.md` (File Explorer: copy,
   paste, rename). Do this after step 2 so the archive holds the new
   manifest.
4. **(do)** Run `ledger_index.py` (Run). It moves L-291 and L-303 to
   section C and adds L-311 and L-312 to the board.
5. **(do)** Move the spent patch into `documentation/`.
6. **(do)** GitHub Desktop: commit, push; report the orrery SHA.
7. **(do)** Reinstall interactive-exhibit and ledger-and-session-records
   (Settings > Skills).
8. **(do)** If this Project's instructions carry the protocol text,
   replace them with v3.56.
9. **(do, later)** Retype the two portrait titles when the editor is
   next open (L-312 carries them).

## WHAT THIS SESSION LEARNED

- **Check a step against what it produces.** "Step 7 not started" was
  a claim; `gallery_metadata.json` was the fact, one read away.
- **"We need a button" can mean "the button could not be found."** Both
  controls Tony asked about or missed already existed.
- **A replay on served data predicts; it does not accept.** It named
  both screens correctly, and still waited for Tony's eyes -- which
  first saw the site serving the old file, because the push had not
  landed.

Written September 2026 with Anthropic's Claude Opus 5.
"""


# =====================================================================
# harness
# =====================================================================

def fail(msg):
    print("STOP: " + msg)
    print("      Nothing was written.")
    return 1


def main():
    texts = {}
    crlf = {}
    for name, md5 in FILES.items():
        path = ROOT / name
        if not path.exists():
            return fail("%s not found. Is this script in the orrery repo root?" % name)
        raw = path.read_bytes()
        crlf[name] = b"\r\n" in raw
        lf = raw.replace(b"\r\n", b"\n")
        got = hashlib.md5(lf).hexdigest()
        if got != md5:
            return fail("%s md5 (LF) is %s, expected %s (at 1ee1cc61). "
                        "Either this patch already ran or the file moved." % (name, got, md5))
        texts[name] = lf.decode("utf-8")
    if (ROOT / NEW_FILE).exists():
        return fail("%s already exists; this patch will not overwrite it." % NEW_FILE)

    led = texts["LEDGER_CONSOLIDATED.md"]
    mp = texts["documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md"]
    ie = texts["skills/interactive-exhibit/SKILL.md"]
    ls = texts["skills/ledger-and-session-records/SKILL.md"]
    pi = texts["PROJECT_INSTRUCTIONS.md"]
    hi = texts["documentation/PROJECT_INSTRUCTIONS_HISTORY.md"]

    groups = [("ledger", led, LEDGER_EDITS), ("master plan", mp, MP_EDITS),
              ("interactive-exhibit", ie, IE_EDITS), ("ledger skill", ls, LS_EDITS)]
    for label, blob, edits in groups:
        for i, (old, new) in enumerate(edits, 1):
            n = blob.count(old)
            if n != 1:
                return fail("%s edit %d matched %d time(s), expected 1: %r"
                            % (label, i, n, old[:70]))

    singles = [("protocol header", pi, PI_HEADER_OLD), ("protocol SHA anchor", pi, PI_ANCHOR_OLD),
               ("protocol entry anchor", pi, PI_ENTRY_ANCHOR), ("v3.53 start", pi, V53_START),
               ("protocol end marker", pi, V53_END), ("history insert anchor", hi, HI_INSERT_BEFORE),
               ("plan last-updated start", mp, MP_LU_START), ("plan v26 mark", mp, MP_V26_MARK),
               ("plan participants", mp, MP_LU_END)]
    for label, blob, needle in singles:
        if blob.count(needle) != 1:
            return fail("%s matched %d time(s), expected 1." % (label, blob.count(needle)))
    for handle in ("#### [L-311]", "#### [L-312]"):
        if handle in led:
            return fail("%s already exists in the ledger; handles have moved." % handle)

    # ---- slice v3.53 out of the protocol
    s = pi.find(V53_START)
    e = pi.find(V53_END)
    if not (0 <= s < e):
        return fail("could not bound the v3.53 block.")
    v53 = pi[s:e]
    if not (1500 <= len(v53) <= 4000):
        return fail("v3.53 block is %d chars, outside the expected 1500-4000." % len(v53))

    # ---- master plan rolling stamp: keep v28 and v27, drop v26
    a = mp.find(MP_LU_START)
    b = mp.find(MP_V26_MARK)
    c = mp.find(MP_LU_END)
    if not (0 <= a < b < c):
        return fail("plan's last-updated block is not in the expected order.")
    kept = mp[a + len(MP_LU_START):b]
    if not kept.rstrip().endswith("with Anthropic's Claude Fable 5.1."):
        return fail("the kept v28/v27 text does not end at v27's credit line.")
    dropped = mp[b:c]

    # ---- apply
    for old, new in LEDGER_EDITS:
        led = led.replace(old, new, 1)
    # The stamp is cut FIRST, while a and c still index this exact text.
    # (A test run that cut it after the status edit above it left a stray
    # fragment of the old stamp behind; the check below now catches that.)
    mp = mp[:a] + MP_LU_NEW_HEAD + kept + ")" + mp[c:]
    for old, new in MP_EDITS:
        if mp.count(old) != 1:
            return fail("master plan edit no longer unique after the stamp cut: %r" % old[:70])
        mp = mp.replace(old, new, 1)
    for old, new in IE_EDITS:
        ie = ie.replace(old, new, 1)
    for old, new in LS_EDITS:
        ls = ls.replace(old, new, 1)

    pi = pi[:s] + pi[e:]
    pi = pi.replace(PI_HEADER_OLD, PI_HEADER_NEW, 1)
    pi = pi.replace(PI_ANCHOR_OLD, PI_ANCHOR_NEW, 1)
    pi = pi.replace(PI_ENTRY_ANCHOR, PI_ENTRY_ANCHOR + PI_ENTRY, 1)
    hi = hi.replace(HI_INSERT_BEFORE, v53.rstrip("\n") + HI_MOVED_NOTE + HI_INSERT_BEFORE, 1)

    out = {
        "LEDGER_CONSOLIDATED.md": led,
        "documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md": mp,
        "skills/interactive-exhibit/SKILL.md": ie,
        "skills/ledger-and-session-records/SKILL.md": ls,
        "PROJECT_INSTRUCTIONS.md": pi,
        "documentation/PROJECT_INSTRUCTIONS_HISTORY.md": hi,
        NEW_FILE: HANDOFF,
    }
    for name, blob in out.items():
        try:
            blob.encode("ascii")
        except UnicodeEncodeError as exc:
            return fail("%s would contain non-ASCII at %d." % (name, exc.start))

    # ---- verify the result before writing anything (each can fail)
    landed = 0
    for label, blob, edits in [("ledger", led, LEDGER_EDITS), ("master plan", mp, MP_EDITS),
                               ("interactive-exhibit", ie, IE_EDITS), ("ledger skill", ls, LS_EDITS)]:
        for i, (old, new) in enumerate(edits, 1):
            if new not in blob:
                return fail("%s edit %d did not land." % (label, i))
            landed += 1
    ua = mp.find("**Last updated:**")
    uc = mp.find("\n**Participants:**")
    stamp = mp[ua:uc]
    if not stamp.endswith("with Anthropic's Claude Fable 5.1.)"):
        return fail("the plan's new stamp does not end at v27's credit line: %r" % stamp[-60:])
    if stamp.count("(") != stamp.count(")") or "v26" in stamp:
        return fail("the plan's new stamp is malformed (parentheses %d/%d, v26 present: %s)."
                    % (stamp.count("("), stamp.count(")"), "v26" in stamp))
    resident = [ln[:5] for ln in pi.split("\n") if ln[:4] == "v3.5" and ln[5:8] == " (S"]
    if resident != ["v3.56", "v3.55", "v3.54"]:
        return fail("protocol resident entries are %s, expected v3.56, v3.55, v3.54." % resident)
    if hi.count(V53_START) != 1 or pi.count(V53_START) != 0:
        return fail("v3.53 is not in exactly one place.")

    for name, blob in out.items():
        data = blob.encode("utf-8")
        if crlf.get(name):
            data = data.replace(b"\n", b"\r\n")
        (ROOT / name).write_bytes(data)
        tag = " [CRLF kept]" if crlf.get(name) else ""
        print("Patched %-50s md5(LF) %s%s" % (name, hashlib.md5(blob.encode()).hexdigest(), tag))

    print()
    print("LEDGER        L-291 DONE, L-303 DONE; opened L-311 (rotation period),")
    print("              L-312 (editor follow-ons); amended L-237, L-288, L-310, L-168;")
    print("              header stamp added")
    print("MASTER PLAN   v28 -> v29; kept v28 and v27, dropped v26 (%d chars);" % len(dropped))
    print("              Section 5a 2026-09-09/10; two handoff locations corrected")
    print("SKILLS        interactive-exhibit 1.0 -> 1.1")
    print("              ledger-and-session-records 1.10 -> 1.11")
    print("PROTOCOL      v3.55 -> v3.56; header and SHA anchor moved;")
    print("              v3.53 (%d chars) moved down to the history file" % len(v53))
    print("HANDOFF       %s written" % NEW_FILE)
    print()
    print("Stamps updated: both skill version lines, the plan's Status and Last")
    print("updated lines, the protocol header and anchor, the ledger header.")
    print()
    print("Checked before writing: %d of %d edits landed; plan stamp ends at v27"
          % (landed, len(LEDGER_EDITS) + len(MP_EDITS) + len(IE_EDITS) + len(LS_EDITS)))
    print("with balanced parentheses and no v26; protocol keeps %s;" % ", ".join(resident))
    print("v3.53 now lives only in the history file.")
    print()
    print("Next, in order:")
    print("  1. skills_index.py  (Run) -- it owns the manifest zone")
    print("  2. Copy PROJECT_INSTRUCTIONS.md to documentation/project_instructions_v3_56.md")
    print("     (after step 1, so the archive carries the new manifest)")
    print("  3. ledger_index.py  (Run) -- moves L-291 and L-303 to section C")
    print("  4. Move this script into documentation/")
    print("  5. GitHub Desktop: commit and push; report the SHA")
    print("  6. REINSTALL interactive-exhibit and ledger-and-session-records")
    print("     (Settings > Skills). The next session verifies the install.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
