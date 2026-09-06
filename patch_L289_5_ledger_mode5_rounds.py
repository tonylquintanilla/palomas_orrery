"""
patch_L289_5_ledger_mode5_rounds.py -- LEDGER_CONSOLIDATED.md: the two
Mode 5 rounds of 2026-09-05/06 and what they produced. L-282: lobby
passed, back link fixed, Featured follows the tree. L-286: the sweep
CONFIRMED on the phone; the menu follows the tree; a sweep report tool.
L-289: the first build FAILED on the phone and was rebuilt as the frame
HUD (triad, Aries note, grid chip), then fixed once more from the
desktop and phone pass. L-290 opened from a parallel Sonnet session:
relay anchors must name the protocol and skills, not the code SHA
alone. Header stamped. No status changes: L-289's second rebuild and
the HUD fixes are render-gated.

RUN: save at the ORRERY repo root next to LEDGER_CONSOLIDATED.md, open
in VS Code, Run. Then ledger_index.py, commit, push, report the SHA.
Independent of the gallery patches.

Guards on the LF-normalized md5 of the ledger at orrery a57e86b8; a CRLF
working copy passes and is written back as CRLF. Refuses a second run.
All inserted text is ASCII. No .bak.

Written September 6, 2026 with Anthropic's Claude Fable 5.1. Built on
orrery a57e86b82503380e92b4e78cd7d8995a71183f20 at
https://github.com/tonylquintanilla/palomas_orrery (main); gallery state
described is fc8d9fb3ecb2 (patches L289_3, L282_5, L286_1 live) plus
patch_L289_4 delivered, not run. Archive to documentation/ once run.
"""
import hashlib, os, sys

EXPECT = "76e3c34c0b74f05f94d55073239dbc07"
P = "LEDGER_CONSOLIDATED.md"

EDITS = [
    # header stamp
    (b"L-289 designed and built, L-287 note; all render-gated), built on\n"
     b"9652a43d plus patch_L287_6.\n",
     b"L-289 designed and built, L-287 note; all render-gated), built on\n"
     b"9652a43d plus patch_L287_6.\n"
     b"Module updated: September 6, 2026 with Anthropic's Claude Fable 5.1\n"
     b"(Mode 5 rounds of 2026-09-05/06: L-282 lobby passed, back link fixed,\n"
     b"tree order; L-286 sweep confirmed on the phone, sweep_report tool;\n"
     b"L-289 first build failed on the phone, rebuilt as the frame HUD and\n"
     b"fixed again; L-290 opened), built on a57e86b8.\n", 1),
    # L-282
    (b"<!-- L:282 status:OPEN upd:2026-09-05 section:A flag: rice:5/4/75/4 -->\n",
     b"<!-- L:282 status:OPEN upd:2026-09-06 section:A flag: rice:5/4/75/4 -->\n", 1),
    (b"- **Tony-action (decide), after Mode 5:** whether the hamburger stays\n"
     b"  once L-286 lands, and whether the museum sentence gets an editor\n"
     b"  field or is set in the JSON by hand.\n",
     b"- **Tony-action (decide), after Mode 5:** whether the hamburger stays\n"
     b"  once L-286 lands, and whether the museum sentence gets an editor\n"
     b"  field or is set in the JSON by hand.\n"
     b"- **Mode 5, 2026-09-05, phone, live at gallery `66087696`:** the lobby\n"
     b"  renders; doors, a door tap, a Featured card and Home all work. Three\n"
     b"  findings, one cause (the shim grouped by first appearance in the\n"
     b"  metadata file, not by the tree): Featured put the Sun sixth where\n"
     b"  the editor shows it first; rooms behind a door were out of order;\n"
     b"  cards directly under a door sat under an invented \"Other\" heading.\n"
     b"  Tony's ruling: the TREE is the rule -- built under L-286\n"
     b"  (`patch_L286_1_tree_order.py`, live at `fc8d9fb3`); Featured follows\n"
     b"  the same walk, so the editor's tree and in-room order ARE the lobby's\n"
     b"  order and no new field was added.\n"
     b"- **Back paths, 2026-09-05/06:** Safari's own back control landed on\n"
     b"  the Sun at Outer Corona from the lobby, whatever page Tony started\n"
     b"  on. Cause was ours: the Sun page's \"Gallery\" button was a plain link,\n"
     b"  so every visit left lobby -> Sun -> lobby in the history and the\n"
     b"  browser's back walked into the Sun. `patch_L282_5_back_link.py`\n"
     b"  (live at `fc8d9fb3`): when the page behind is our own gallery the\n"
     b"  button calls history.back(); opened from a shared link it stays a\n"
     b"  link. Tony, desktop and phone 2026-09-06: works.\n"
     b"- **Tony-action (do):** the old-card cleanup in the editor (remove or\n"
     b"  fix), separate from this item.\n", 1),
    # L-286
    (b"<!-- L:286 status:OPEN upd:2026-09-04 section:A flag: rice:5/4/70/4 -->\n",
     b"<!-- L:286 status:OPEN upd:2026-09-06 section:A flag: rice:5/4/70/4 -->\n", 1),
    (b"**Gap:** the room-path reader in `index.html` (filter a grid to a room);\n",
     b"- **Sweep CONFIRMED on the phone, 2026-09-05** (Tony, Paleoclimate\n"
     b"  Cenozoic in portrait: \"sweeps correctly\"). The drag handoff this\n"
     b"  entry said needed a real phone has had one. Exceptions exist; Tony\n"
     b"  is checking them systematically. `tools/sweep_report.py` (built\n"
     b"  2026-09-06, not yet committed) applies sweepWanted()'s own rule to\n"
     b"  every card and prints them BY CLASS, names first: sweeps at the\n"
     b"  file's aspect; sweeps at 16:9 (no stored size); sweeps a little\n"
     b"  (stored taller than wide, e.g. Warming Stripes 1200x1400 -> 689 px);\n"
     b"  Mapbox (map has its own drag); fits without scrolling; 3D; portrait\n"
     b"  file; shape 9:16. A card whose file cannot be read exits non-zero.\n"
     b"  One card per class on the phone should find the exceptions.\n"
     b"- **Tree order BUILT 2026-09-05, live at `fc8d9fb3`**\n"
     b"  (`patch_L286_1_tree_order.py`): ROOM_ORDER from a pre-order walk of\n"
     b"  `gallery_config.json`; the menu and Featured sort by it; a door\n"
     b"  precedes its rooms so loose cards list at the door with no heading.\n"
     b"  Verified headless: 105 cards, Sun first in Featured, zero \"Other\".\n"
     b"  Tony's Mode 5 on this is pending.\n"
     b"- **Tony-action (do):** save `tools/sweep_report.py`, run it, and\n"
     b"  check one card per class on the phone; report the exception classes.\n"
     b"**Gap:** the room-path reader in `index.html` (filter a grid to a room);\n", 1),
    # L-289
    (b"<!-- L:289 status:OPEN upd:2026-09-05 section:A flag: rice:3/2/80/1 -->\n",
     b"<!-- L:289 status:OPEN upd:2026-09-06 section:A flag: rice:3/2/80/1 -->\n", 1),
    (b"**Gap:** Mode 5 on the phone; Tony's density and size rulings; then\n"
     b"DONE.\n"
     b"**Ref:** L-267 (Sun exhibit GUI), interactive.html, HANDOFF 2026-09-05.\n"
     b"\n"
     b"#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery\n",
     b"- **Mode 5, 2026-09-05, phone, live at `66087696`: the twelve-edge\n"
     b"  build FAILED.** Tony, with screenshots: the labels were scattered\n"
     b"  and the every-second pattern hard to read; labels on edges beside\n"
     b"  the camera floated on nothing; on zoom-out the labels vanished;\n"
     b"  \"this may be worse than the plotly labels.\" Cause, one choice: the\n"
     b"  labels were points IN the scene, so they behaved as scenery --\n"
     b"  shrank with distance, were clipped at the box boundary, projected\n"
     b"  from behind the camera. Not fixable by thinning or size.\n"
     b"- **Redesign 2026-09-05 (Tony, by conversation):** the tick numbers\n"
     b"  repeat one value sixty times, so ONE chip states the uniform\n"
     b"  spacing (\"grid 0.2 AU\"); direction is a TRIAD in the corner that\n"
     b"  turns with the camera (Tony: \"can the triad rotate in alignment?\"\n"
     b"  -- yes, it is computed from the camera); the First Point of Aries\n"
     b"  glyph at the x tip with a note that this is the J2000 ECLIPTIC\n"
     b"  frame, not a graph frame; grid lines coloured per axis to match.\n"
     b"  Aspect ratio read from the layout, not assumed 1:1:1 (Tony: \"ticks\n"
     b"  are not always isometric\"). Frame VERIFIED before the note was\n"
     b"  written: `feature_renderers.js` rotates IAU poles into the J2000\n"
     b"  ecliptic by the mean obliquity; belts are drawn in the ecliptic;\n"
     b"  the served index stores the Sun as frame-origin. Source for the\n"
     b"  note: NASA/JPL NAIF frames tutorial (J2000 x axis = vernal equinox).\n"
     b"  The assembler does not pass through the provenance scanner (Tony),\n"
     b"  so the citation is hand-carried in the note itself.\n"
     b"- **Built 2026-09-05, live at gallery `fc8d9fb3`:**\n"
     b"  `patch_L289_3_frame_hud.py` -- edge labels OUT; sunHud* (triad SVG,\n"
     b"  chip, note) IN as page chrome that only reads the camera and never\n"
     b"  calls Plotly (the L-278 hazard does not apply); Plotly tick numbers\n"
     b"  back on; titles stay blank. Triad orientation CONFIRMED by test:\n"
     b"  markers at +x, +y, +z in the scene matched the arrows.\n"
     b"- **Mode 5, 2026-09-06, desktop and phone, at `fc8d9fb3`:** triad\n"
     b"  moves with the grid (desktop); chip works; back link works. Four\n"
     b"  defects: (1) the frame note was open on arrival and its X did not\n"
     b"  close it -- `hidden` lost a CSS specificity contest to the rule that\n"
     b"  shows Sun chrome; (2) grid colours read as a second key against the\n"
     b"  triad -- back to white; (3) arrival grid 0.2 AU vs chip 0.1 AU --\n"
     b"  the arrival layout set no dtick, Plotly and the page chose\n"
     b"  differently; +/- and Home agree (Home sets dtick); mouse wheel is\n"
     b"  camera zoom by design; (4) on the phone the triad did not follow a\n"
     b"  touch rotation -- Plotly fires no camera events during touch.\n"
     b"- **Built 2026-09-06, delivered NOT run:** `patch_L289_4_hud_fixes.py`\n"
     b"  (guards on `fc8d9fb3`). Note behaves like every other hover: mouse\n"
     b"  opens on rest over the glyph or the note, closes on leave; touch\n"
     b"  taps to toggle, tap elsewhere closes; X removed. Grid white.\n"
     b"  Arrival dtick set from the same rule Home uses. Triad reads the\n"
     b"  gl3d scene's live camera (getCamera()) once per animation frame and\n"
     b"  redraws only on change -- tested with Plotly's events removed: 23\n"
     b"  redraws in a drag, 0 at rest.\n"
     b"- **Tony-action (do):** run `patch_L289_4_hud_fixes.py`, push; Mode 5\n"
     b"  on desktop and phone: note hidden on arrival, hover/tap, arrival\n"
     b"  grid = chip, triad follows a touch rotation.\n"
     b"- **Tony-action (decide), after Mode 5:** triad size and colours;\n"
     b"  whether the Explorer room gets the same HUD.\n"
     b"**Gap:** Mode 5 on `patch_L289_4`; Tony's rulings above; then DONE.\n"
     b"**Ref:** L-267 (Sun exhibit GUI), L-278 (why the HUD never calls\n"
     b"Plotly), interactive.html, feature_renderers.js (poleBasis),\n"
     b"HANDOFF 2026-09-05 (away session), HANDOFF 2026-09-06.\n"
     b"\n"
     b"#### [L-290] Relay anchors must name the protocol and skills, not the code SHA alone\n"
     b"<!-- L:290 status:OPEN upd:2026-09-06 section:A flag: rice:4/3/90/1 -->\n"
     b"- **Opened 2026-09-06** from a parallel Claude Sonnet session Tony ran\n"
     b"  against orrery `a57e86b8` (it proposed the handle L-288, already\n"
     b"  taken; placed here). The Anchor Requirement pins the CODE repo's\n"
     b"  SHA and URL on every outbound document and says nothing about the\n"
     b"  protocol or the skills that govern HOW the work is done. A partner\n"
     b"  without resident access -- GPT, Gemini, or a Claude session outside\n"
     b"  this account and Project -- reads the code with none of that\n"
     b"  context unless the document names PROJECT_INSTRUCTIONS.md and the\n"
     b"  task-relevant SKILL.md files as fetch targets too. L-191's Fable\n"
     b"  relay had to fetch source itself despite being a Claude model:\n"
     b"  resident loading is tied to the account and Project, not the model.\n"
     b"- **Method Belongs to the Skill:** the answer is the same next month\n"
     b"  for a different task. Requirement goes resident (Mode 7, \"Documents\n"
     b"  as handoffs\"); the wording template goes in\n"
     b"  ledger-and-session-records (Anchor Requirement section), with two\n"
     b"  forms: fetch-capable partners are told which files to fetch at the\n"
     b"  pinned SHA; Gemini (snapshot-only, L-276) gets the relevant excerpt\n"
     b"  pasted inline with the limitation stated.\n"
     b"- **Drafts** of both amendments, as the Sonnet session wrote them, are\n"
     b"  in `documentation/L290_relay_anchor_drafts.md` (delivered\n"
     b"  2026-09-06). They are proposals until Tony rules. A skill bump\n"
     b"  (ledger-and-session-records 1.9 -> 1.10) follows the four-step\n"
     b"  binding rule and is verified by the NEXT session's load, per Stale\n"
     b"  Skill = Stop.\n"
     b"- **Tony-action (decide):** accept, amend or decline the two drafts.\n"
     b"**Gap:** Tony's ruling; then the protocol edit, the skill bump, the\n"
     b"reinstall, and the manifest regeneration, in one push.\n"
     b"**Ref:** L-276 (relay partners can read the repo; the Gemini snapshot\n"
     b"note), L-191 (the Fable relay), Mode 7 Key Principles,\n"
     b"skills/ledger-and-session-records/SKILL.md.\n"
     b"\n"
     b"#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery\n", 1),
]


def die(m):
    print("ERROR: " + m)
    print("NOTHING was written.")
    sys.exit(1)


os.chdir(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(P):
    die("%s not found next to this script; save at the orrery repo root" % P)
raw = open(P, "rb").read()
crlf = b"\r\n" in raw
s = raw.replace(b"\r\n", b"\n") if crlf else raw
got = hashlib.md5(s).hexdigest()
if got != EXPECT:
    if b"#### [L-290] Relay anchors" in s:
        die("this patch has already been applied to %s" % P)
    die("%s does not match orrery a57e86b8 (md5 %s, expected %s)" % (P, got, EXPECT))
print("ok  %s matches a57e86b8%s" % (P, " (working copy is CRLF)" if crlf else ""))

for old, new, n in EDITS:
    c = s.count(old)
    if c != n:
        die("anchor expected %d time(s), found %d: %r" % (n, c, old[:70]))
    s = s.replace(old, new)
    print("ok  edit: %r" % old[:60])

if any(any(ch > 127 for ch in new) for _, new, _ in EDITS):
    die("non-ASCII byte in inserted text")

out = s.replace(b"\n", b"\r\n") if crlf else s
open(P, "wb").write(out)
print("LEDGER_CONSOLIDATED.md: %d edits -- header stamp; L-282 Mode 5 + back link + tree ruling;"
      " L-286 sweep confirmed + tree order built + sweep_report; L-289 failure, redesign, two builds,"
      " Mode 5 round 2; L-290 opened." % len(EDITS))
print("No status changed. Next: ledger_index.py, commit, push, report the orrery SHA.")
print("Undo is Discard Changes in GitHub Desktop.")
