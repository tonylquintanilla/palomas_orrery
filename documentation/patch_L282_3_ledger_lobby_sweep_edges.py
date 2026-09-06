"""
patch_L282_3_ledger_lobby_sweep_edges.py -- LEDGER_CONSOLIDATED.md: the
2026-09-05 away-session record. L-282 rulings (Featured, Interactive,
Under construction) and the lobby build; L-286's sweep built for 2D;
L-289 designed and built (twelve-edge labels); a note on L-287 that the
mode filter was a leftover. Header stamped. No status changes: every
build here is render-gated until Tony's phone pass.

RUN ORDER MATTERS. This runs AFTER patch_L287_6_ledger_close.py AND
after ledger_index.py has been run once on its result. Save at the
ORRERY repo root next to LEDGER_CONSOLIDATED.md, open in VS Code, Run.
Then run ledger_index.py again, commit both, push, report the orrery SHA.

Guards on the LF-normalized md5 of the ledger as patch_L287_6 plus one
indexer run leave it, predicted by re-running both here on the ledger at
orrery 9652a43d (the indexer is deterministic). If Tony's copy differs
the guard refuses and writes nothing; the next session rebuilds this
patch against the real file. A CRLF working copy passes and is written
back as CRLF. Refuses a second run. All inserted text is ASCII. No .bak;
undo is Discard Changes in GitHub Desktop.

Written September 5, 2026 with Anthropic's Claude Fable 5.1. Built on
orrery 9652a43db8361a9d904002e6a4271a34281be8a1 at
https://github.com/tonylquintanilla/palomas_orrery (main) plus the
delivered patch_L287_6; gallery state described is
503fa387068a176fa7e12d2ab8df3752c8ffe429 plus four delivered gallery
patches, NOT yet run. Archive to documentation/ once run.
"""
import hashlib, os, sys

EXPECT = "446d0b1f867bf6ce534ffc4f7b20fd14"
P = "LEDGER_CONSOLIDATED.md"

EDITS = [
    # header stamp, after the L-287 close stamp
    (b"and its door count corrected), built on 9652a43d.\nReview and RICE update Tony 6-21-2026\n",
     b"and its door count corrected), built on 9652a43d.\n"
     b"Module updated: September 5, 2026 with Anthropic's Claude Fable 5.1\n"
     b"(away-session: L-282 rulings and lobby build, L-286 sweep for 2D,\n"
     b"L-289 designed and built, L-287 note; all render-gated), built on\n"
     b"9652a43d plus patch_L287_6.\n"
     b"Review and RICE update Tony 6-21-2026\n", 1),
    # L-282 date
    (b"<!-- L:282 status:OPEN upd:2026-09-04 section:A flag: rice:5/4/75/4 -->\n",
     b"<!-- L:282 status:OPEN upd:2026-09-05 section:A flag: rice:5/4/75/4 -->\n", 1),
    # L-282: the open decision becomes the ruling; build record; Tony-actions
    (b"**Tony-action (decide), carried here from L-287 on 2026-09-05:** What's\n"
     b"New is driven by the `featured` flag (7 cards carry it at `503fa387`),\n"
     b"by the dated JSON feed from L-280, or by both.\n",
     b"- **Rulings 2026-09-05 (Tony, away from the machine, by phone):**\n"
     b"  What's New is retired as a name; the lobby section is FEATURED,\n"
     b"  driven by the existing `featured` flag alone, no dated feed (a feed\n"
     b"  would add a step every shipping patch has to remember). Live-scene\n"
     b"  cards are labelled INTERACTIVE wherever a visitor sees them. Empty\n"
     b"  rooms show as UNDER CONSTRUCTION. Arrangement approved from a\n"
     b"  portrait mockup: title, museum sentence, three door rows, Featured\n"
     b"  grid, guest book row, footer; doors above Featured. Door sentences\n"
     b"  are Tony's, entered through the editor into the room tree.\n"
     b"- **Built 2026-09-05, NOT yet run or pushed** [render-gated]:\n"
     b"  `patch_L282_1_lobby.py` (gallery, guards on `index.html` at\n"
     b"  `503fa387`). The first screen becomes the lobby: renderLobby() is\n"
     b"  the ONE writer of the home view (the initial markup, goHome() and\n"
     b"  the error path had each written it). Door rows read label, colour\n"
     b"  and sentence from `gallery_config.json` doors; the second line\n"
     b"  counts exhibits, interactive scenes and rooms under construction\n"
     b"  (rooms with no card anywhere in their subtree). A door tap opens the\n"
     b"  existing menu with that door expanded -- the interim until L-286\n"
     b"  gives each door its rooms page; the hamburger stays as the second\n"
     b"  path for the same reason. Featured is a two-column grid (three on\n"
     b"  desktop) of `featured` cards; an Interactive tag on live cards;\n"
     b"  \"Live scene\" -> \"Interactive\" in the menu. Guest book row reads\n"
     b"  Under construction until L-281. The museum sentence reads a\n"
     b"  top-level `sentence` in `gallery_config.json` if present, else\n"
     b"  today's text; the editor has no field for it yet. Tested in\n"
     b"  headless Chromium at 390x844 and 1280x800 with Plotly served\n"
     b"  locally: lobby rendered, door tap opened the menu at Stars, a\n"
     b"  Featured card drew its plot, Home returned to the lobby, the lobby's\n"
     b"  i button opened About; no script errors. Fonts and the dove wall\n"
     b"  could not load in the sandbox.\n"
     b"- **Consumers touched:** `index.html` only. `interactive.html` is\n"
     b"  unchanged by this item (L-289 edits it separately).\n"
     b"- **Tony-action (do):** run `patch_L282_1_lobby.py` then\n"
     b"  `patch_L282_2_sweep.py` (L-286) at the gallery root, commit, push,\n"
     b"  report the SHA; Mode 5 on the phone: the lobby, a door tap, a\n"
     b"  Featured card, Home.\n"
     b"- **Tony-action (decide), after Mode 5:** whether the hamburger stays\n"
     b"  once L-286 lands, and whether the museum sentence gets an editor\n"
     b"  field or is set in the JSON by hand.\n", 1),
    # L-286: the sweep half of the room-shape rule is built for 2D
    (b"  L-287 (cards must carry a room path before rooms can be drawn).\n"
     b"**Gap:** the room-path reader in `index.html` (filter a grid to a room);\n",
     b"  L-287 (cards must carry a room path before rooms can be drawn).\n"
     b"- **Room-shape rule BUILT for 2D, 2026-09-05, NOT yet run or pushed**\n"
     b"  [render-gated]: `patch_L282_2_sweep.py` (gallery; guards on the\n"
     b"  file `patch_L282_1` leaves). Tony's ruling by phone: \"no squeezed\n"
     b"  landscape\" -- landscape on the phone stays as it is; portrait must\n"
     b"  sweep, not compress. On a phone (<768 px) in portrait, a 2D plot\n"
     b"  served from a landscape file with no portrait slot and shape not\n"
     b"  9:16 is drawn at its own width (the file's width/height where it\n"
     b"  carries them, else 16:9) at full room height, and `.viz-container`\n"
     b"  scrolls sideways; Plotly `dragmode` is set false while swept so the\n"
     b"  horizontal drag goes to the sweep, and restored on rotation to\n"
     b"  landscape; zoom buttons still work; 3D scenes scale to fit as\n"
     b"  before; Home clears the room. Also lifts the MODE FILTER (see L-287\n"
     b"  note): every card shows on the phone, 105 not 56. Tested headless:\n"
     b"  a 66 Ma paleoclimate card drew 1429 px wide in a 390 px room, a\n"
     b"  touch swipe scrolled it 288 px, rotation cleared and restored the\n"
     b"  sweep, a 3D card and a two-slot card did not sweep, desktop\n"
     b"  unchanged. Warming Stripes is stored 1200x1400 so it sweeps only to\n"
     b"  689 px -- a Studio export question if it should be wider. The drag\n"
     b"  handoff is the piece this entry already said needs a real phone.\n"
     b"**Gap:** the room-path reader in `index.html` (filter a grid to a room);\n", 1),
    # L-289: design and build
    (b"**Gap:** reproduce on the phone; try the label placement; Tony judges.\n",
     b"- **Design settled 2026-09-05 (Tony, by phone), replacing the\n"
     b"  top/back-view idea above.** Two observations first: on desktop the\n"
     b"  camera zoom shrinks grid and all, so the numbers never change; on\n"
     b"  the phone the frame zoom re-labels the grid as you go in, which is\n"
     b"  real information about scale (Tony: better). And the arrival frame\n"
     b"  is full on purpose, so the box edges Plotly labels sit off-screen.\n"
     b"  Ruling: labels on ALL TWELVE edges of the box, internal and open,\n"
     b"  so one is in view at any rotation; tick values as well as the axis\n"
     b"  name, thinned to every second or third grid line; the page OWNS the\n"
     b"  ticks (Plotly's one-edge set off on the Sun so no edge carries\n"
     b"  two); NO label at a vertex; the axis name on the UNLABELED grid\n"
     b"  line nearest the centre of each edge so no value is lost to it;\n"
     b"  NO dimming with distance. Clutter is a Mode 5 call.\n"
     b"- **Built 2026-09-05, NOT yet run or pushed** [render-gated]:\n"
     b"  `patch_L289_1_edge_labels.py` (gallery; guards on `interactive.html`\n"
     b"  at `503fa387`) and `patch_L289_2_name_on_skipped_tick.py` (guards\n"
     b"  on patch 1's output). One scatter3d text trace, hover off, no\n"
     b"  legend group (the drawer never sees it), added after newPlot and\n"
     b"  after buildSunDrawer so extents and sunTraceGroup never counted it;\n"
     b"  rebuilt by sunEdgeLabelsUpdate() after sunFrameOn, navFrameZoom and\n"
     b"  navHome from the same range and dtick the grid uses; ticks are\n"
     b"  multiples of dtick clear of both vertices by half a step;\n"
     b"  `?ticks=N` (1..6, default 2) is the Mode 5 switch. Sun exhibit only;\n"
     b"  the Explorer's axes are untouched. Tested in a stand-in page (the\n"
     b"  Sun page cannot run in the sandbox: Pyodide's CDN is blocked) with\n"
     b"  Plotly, the Sun camera and arrival ranges: 36 labels installed;\n"
     b"  values re-scaled with the grid (0.2 at arrival, 0.02/0.06 three taps\n"
     b"  in, 0.5 out); with lines every 0.2 on a -0.7..0.7 range, ticks=2\n"
     b"  reads -0.4, 0, 0.4 with the name on the -0.2 line, ticks=3 reads\n"
     b"  -0.4, 0.2 with the name on 0, ticks=1 puts the name between lines\n"
     b"  at 0.1. No script errors. How it reads over the real shells is\n"
     b"  unknown until the phone.\n"
     b"- **Tony-action (do):** run the two L-289 patches at the gallery root\n"
     b"  (either side of the L-282 patches; different file), commit, push;\n"
     b"  Mode 5 on the phone: rotate, +, -, Home; try `&ticks=3`.\n"
     b"- **Tony-action (decide), after Mode 5:** tick density (1, 2 or 3),\n"
     b"  label size (one constant, 9 px today), and whether the Explorer\n"
     b"  room should get the same edges.\n"
     b"**Gap:** Mode 5 on the phone; Tony's density and size rulings; then\n"
     b"DONE.\n", 1),
    # L-287 note in the archive: the filter was a leftover, lifted under L-286
    (b"**Gap:** none. Closed on the remodel at gallery `503fa387`.\n",
     b"- **Note 2026-09-05 (after close):** the reader shim kept the page's\n"
     b"  mode FILTER, so a landscape-only card was still invisible on a\n"
     b"  phone -- 56 shown of 105 -- against the rule above that a one-file\n"
     b"  card shows in both orientations. Surfaced by the lobby's counts.\n"
     b"  Lifted by `patch_L282_2_sweep.py` under L-286, together with the\n"
     b"  sweep that makes showing them acceptable (Tony: no squeezed\n"
     b"  landscape). Recorded here so the closed record does not claim the\n"
     b"  rule was in force before it was.\n"
     b"**Gap:** none. Closed on the remodel at gallery `503fa387`.\n", 1),
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
    if got == "64e10bda8093abb6eef0bcb8eb957f4a":
        die("ledger is still at 9652a43d -- run patch_L287_6_ledger_close.py and ledger_index.py first")
    if b"L-289 designed and built, L-287 note; all render-gated), built on" in s:
        die("this patch has already been applied to %s" % P)
    die("%s does not match the predicted post-L287_6 ledger (md5 %s, expected %s). "
        "Not an error in your files: the prediction missed. Next session rebuilds this patch." % (P, got, EXPECT))
print("ok  %s matches the post-L287_6 ledger%s" % (P, " (working copy is CRLF)" if crlf else ""))

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
print("LEDGER_CONSOLIDATED.md: %d edits -- header stamp; L-282 rulings + lobby build + Tony-actions;"
      " L-286 sweep built for 2D; L-289 design + build + Tony-actions; L-287 archive note." % len(EDITS))
print("No status changed: every build is render-gated until the phone pass.")
print("Next: run ledger_index.py, commit, push, report the orrery SHA.")
print("Undo is Discard Changes in GitHub Desktop.")
