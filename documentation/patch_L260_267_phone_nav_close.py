#!/usr/bin/env python3
"""
patch_L260_267_phone_nav_close.py -- LEDGER_CONSOLIDATED.md
The phone pass ran, the navigation cluster shipped: close L-260 and
L-267, open L-285 for what the static gallery still owes.

Built on orrery 9b891970ef32292e7d3c5d444af1c33cc3f8ea43 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery facts at 2509695d (cluster) and 963b7a34 (moved top-left).

WHAT IT DOES, four edits, bottom-up:
  4. L-284's tail: appends a new block, L-285 -- index.html adopts
     gallery/nav_cluster.js and retires the fake-wheel dolly; carries
     the Explorer legend overlap, accepted by Tony.
  3. L-267: status OPEN -> DONE, upd 2026-09-04; the AMENDED banner
     becomes the CLOSED banner; the "portrait pass" Tony-action becomes
     the record of the phone pass, the design rulings, the two patches
     and the Mode 5 result.
  2. L-260: status OPEN -> DONE, upd 2026-09-04; the Gap paragraph
     becomes the close record.
  Both closed items STAY in section A -- "DONE items stay in their
  section until a housekeeping pass moves them to C" is the ledger's
  own rule -- with Gap: none -- move to section C.

AFTER IT RUNS: open tools/ledger_index.py (or wherever it lives in your
tree) in VS Code and press Run, so the INDEX zone is regenerated. This
patch edits DETAIL blocks only and never touches the index zone.

Refuses if the ledger is not at 9b891970; refuses to run twice; writes
nothing on any mismatch. Undo is Discard Changes in GitHub Desktop.

Written September 4, 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
EXPECTED_FP = "f695da486dad7c0b54497c2b6de86ee0"   # md5, LF-normalized, at 9b891970

# ---------------------------------------------------------------- L-260
OLD_260_META = b"<!-- L:260 status:OPEN upd:2026-08-29 section:A flag: rice:3/3/90/1 -->\n"
NEW_260_META = b"<!-- L:260 status:DONE upd:2026-09-04 section:A flag: rice:3/3/90/1 -->\n"

OLD_260_GAP = (
b"**Gap:** portrait. The legend overlays the object it describes,\n"
b"and the axis titles clip. Landscape needs nothing. Deferred by\n"
b"Tony to the next session, 2026-08-29.\n"
)
NEW_260_GAP = (
b"- **The portrait defect was answered by L-267 Stage A** (gallery\n"
b"  `2ed12564`, 2026-08-31): the legend became a drawer, and the\n"
b"  picture is no longer behind anything.\n"
b"- **The phone pass ran, Tony, 2026-09-03, iPhone, live page.** Three\n"
b"  findings, his order: the Plotly modebar is missing so there is no\n"
b"  way to reset the scene (the gallery's own 768 px rule hides it, and\n"
b"  nothing had replaced it); the two-finger zoom does nothing in the\n"
b"  3D scene; landscape works. The first two are the phone half of\n"
b"  this item and were fixed under L-267 (step 7, the navigation\n"
b"  cluster) at gallery `2509695d` and `963b7a34`, Mode 5 passed\n"
b"  2026-09-04.\n"
b"**CLOSED 2026-09-04.** Both halves done: axes at `6c612397`\n"
b"(2026-08-29), phone at `963b7a34` (2026-09-04), each render-confirmed\n"
b"Mode 5 on the live page.\n"
b"**Gap:** none -- move to section C.\n"
)

# ---------------------------------------------------------------- L-267
OLD_267_META = b"<!-- L:267 status:OPEN upd:2026-09-03 section:A flag: rice:4/3/85/3 -->\n"
NEW_267_META = b"<!-- L:267 status:DONE upd:2026-09-04 section:A flag: rice:4/3/85/3 -->\n"

OLD_267_BANNER = b"**AMENDED 2026-09-03 -- Stage C shipped; the phone pass is what remains.**\n"
NEW_267_BANNER = (
b"**CLOSED 2026-09-04 -- the phone pass ran, the navigation cluster\n"
b"shipped, and the Sun GUI is complete on phone and desktop.** Record of\n"
b"the close is below the Stage C record; the design history follows it.\n"
)

OLD_267_TONYACTION = (
b"**Tony-action (do):** the portrait pass on a phone -- Stages A, B and C\n"
b"are all unverified on a small screen, and the 40/60 split was chosen on a\n"
b"desktop. Carried from L-260.\n"
)
NEW_267_TONYACTION = (
b"THE PHONE PASS, Tony, 2026-09-03, iPhone, live page, both orientations.\n"
b"Stages A, B and C hold on a small screen; the 40/60 split is fine.\n"
b"Three findings, in his order: the Plotly modebar is missing, so there\n"
b"is no way to reset the scene -- the gallery's 768 px rule hides it\n"
b"(`interactive.html` 548, 1070, 1497 at `98cc99bd`) and nothing had\n"
b"replaced it; the two-finger zoom gesture does nothing in the 3D\n"
b"scene; landscape works. The static gallery had solved both long ago\n"
b"with `+`/`-`/reset buttons (`index.html` 1572-1625) and Gallery Studio\n"
b"draws the same pair. Tony's ruling: one control set for the whole\n"
b"site.\n"
b"\n"
b"DESIGN, settled in conversation 2026-09-03/04 before anything was\n"
b"built. `+`/`-` step the FRAME (axis ranges), not the camera: the Sun\n"
b"spans six orders of magnitude and a camera dolly cannot travel that --\n"
b"the near shells vanish into the perspective before the far ones arrive\n"
b"and the grid labels never change -- while frame zoom is the mechanism\n"
b"the focus already uses (`sunFrameOn`). Tony: this is also the answer\n"
b"for future features that need to see past the normal range, comet\n"
b"detail for one. Home is the ARRIVAL VIEW (Tony's reading 2): the\n"
b"layout's starting camera, which in perspective resets zoom and\n"
b"orientation together because the eye distance is the zoom, plus the\n"
b"arrival frame, plus focus on the outermost shell shown. Neither\n"
b"button changes the focus or switches a shell -- one job per control,\n"
b"unchanged. The cluster shows on every screen size, desktop included\n"
b"(Tony, 2026-09-04); the modebar stays as it was. Home is a house\n"
b"glyph, deliberately not a circular arrow: on a phone the browser's\n"
b"own reload sits an inch away. Pinch was NOT built -- Tony recalls,\n"
b"and gallery-pipeline 1.2 records, that Plotly does not zoom a 3D scene\n"
b"on pinch; a custom two-finger handler was proposed as a second step\n"
b"and dropped because the buttons cover the need.\n"
b"\n"
b"BUILT. `patch_L267_7_nav_cluster.py` at gallery `2509695d`: new\n"
b"`gallery/nav_cluster.js` (`GalleryNav.mount(container, {zoomIn,\n"
b"zoomOut, home})`, injects its own CSS copied from `index.html`'s\n"
b".zoom-btn, click-only, sibling of the plot so Plotly never sees the\n"
b"taps); `interactive.html` gains `navFrameZoom` (factor 1.6 per tap,\n"
b"each axis about its own centre so the Explorer's 0.3x z-axis keeps its\n"
b"aspect, half-range clamped to 1e-5..5e3 AU, dtick via `sunGridDtick`),\n"
b"`navHome`, `navArrivalR` stored at both rooms' arrival, and one mount\n"
b"after the exhibit branch so both rooms get the same three buttons.\n"
b"Everything is `Plotly.relayout` on public keys; no synthetic events.\n"
b"The cluster hides while the drawer is open. `patch_L267_8` at\n"
b"`963b7a34`: moved from bottom-right to TOP-LEFT after Tony found it\n"
b"under both the drawer and the info panel on the live page -- the\n"
b"drawer owns the bottom, the panel owns the right (desktop) or the\n"
b"bottom (portrait), the title is centred, so top-left is the corner\n"
b"nothing else claims.\n"
b"\n"
b"MODE 5 PASSED, Tony, 2026-09-04, on the live page, iPhone portrait and\n"
b"desktop, conditions stated per gallery-assembler 1.2. Six of seven\n"
b"trials correct: rotate then Home restores angle AND size (camera\n"
b"relayout resets zoom); five taps of `+` close in on the centre with\n"
b"the grid numbers changing and the drawer label unchanged; focused on\n"
b"Core, `-` three and `+` three returns to the start still on Core; no\n"
b"buttons while the drawer is open, back when closed; buttons usable\n"
b"with the i panel open; desktop shows the cluster top-left and Home\n"
b"behaves as on the phone. Trial 6 (the Explorer) was NOT run: the\n"
b"cluster overlaps that room's legend. Tony: not critical, a legacy view\n"
b"L-280 replaces; carried on L-285.\n"
b"\n"
b"CARRIED OUT of this item on closing: the drawer-row indentation\n"
b"question (Tony-action (decide), 2026-08-30, \"could work too\") waits\n"
b"for Earth's shells so it is judged against two bodies, not one --\n"
b"raise it when Earth's drawer rows exist. The static gallery's adoption\n"
b"of the shared cluster is L-285.\n"
b"\n"
b"**Gap:** none -- move to section C.\n"
)

# ---------------------------------------------------------------- L-285
ANCHOR_284_TAIL = (
b"**Ref:** L-269 (the consumer list and its stores), L-270, L-283;\n"
b"social_media_export.py; palomas_orrery.py; star_visualization_gui.py;\n"
b"skills/gallery-pipeline; skills/provenance-discipline.\n"
b"\n"
)
NEW_285 = ANCHOR_284_TAIL + (
b"#### [L-285] index.html adopts the shared navigation cluster; the fake-wheel dolly retires\n"
b"<!-- L:285 status:OPEN upd:2026-09-04 section:A flag: rice:2/2/90/1 -->\n"
b"- **What exists.** `gallery/nav_cluster.js` (L-267 step 7, gallery\n"
b"  `2509695d`) is the site's one control set: `+`, `-`, Home, top-left,\n"
b"  every screen size. `interactive.html` uses it. `index.html` still\n"
b"  draws its own inline cluster (`.zoom-controls`, `.reset-standalone`,\n"
b"  lines 857-1090 and 1571-1625 at `963b7a34`) whose 3D `+`/`-` fake a\n"
b"  mouse wheel at the WebGL canvas (`zoom3D`, line 2551) and whose\n"
b"  reset restores orientation and pan but not zoom level.\n"
b"- **Why it is one row and not a fix today.** Same three buttons, two\n"
b"  mechanisms underneath -- a parallel pipeline by the protocol's\n"
b"  definition, recorded rather than chased (The Braid). The static\n"
b"  gallery's `+`/`-` already do two different things on its own pages\n"
b"  (2D scales axis ranges, 3D dollies the camera), so the visible\n"
b"  inconsistency predates this item. The clean end state is frame zoom\n"
b"  everywhere and the dolly gone.\n"
b"- **Scope when opened.** `index.html` loads `gallery/nav_cluster.js`,\n"
b"  drops its inline cluster markup and CSS, wires `zoomIn`/`zoomOut` to\n"
b"  a range-scaling frame zoom for 3D (the 2D and polar paths already\n"
b"  scale ranges) and Home to the stored original camera and ranges the\n"
b"  fly-to controls already keep (`data-orig-camera`, `data-orig-ranges`).\n"
b"  Its own Mode 5, on a 3D static scene and a 2D one.\n"
b"- **Carried here from L-267:** on the Solar System Explorer room of\n"
b"  `interactive.html` the top-left cluster overlaps Plotly's legend.\n"
b"  Tony, 2026-09-04: not critical, a legacy view L-280 replaces. If the\n"
b"  Explorer outlives expectations, move its legend or hide the cluster\n"
b"  there; do not move the cluster, whose corner the Sun room owns.\n"
b"- **Note:** RICE 2/2/90/1 -> 3.6 proposed, not confirmed.\n"
b"**Gap:** the adoption patch, when `index.html` is next open for other\n"
b"reasons (gallery-pipeline skill fires).\n"
b"**Ref:** L-267 (the cluster and its design); L-260 (the phone findings);\n"
b"gallery/nav_cluster.js; index.html; gallery-pipeline 1.2 (Mobile and\n"
b"Rendering Facts -- the fake-wheel note and the \"3D zoom RESET is not\n"
b"possible\" line, which the Sun room's Home shows is a limit of the\n"
b"dolly, not of Plotly).\n"
b"\n"
)

EDITS = [   # bottom-up
    ("L-285 appended after L-284",       ANCHOR_284_TAIL,     NEW_285),
    ("L-267 close record",               OLD_267_TONYACTION,  NEW_267_TONYACTION),
    ("L-267 banner",                     OLD_267_BANNER,      NEW_267_BANNER),
    ("L-267 status DONE",                OLD_267_META,        NEW_267_META),
    ("L-260 close record",               OLD_260_GAP,         NEW_260_GAP),
    ("L-260 status DONE",                OLD_260_META,        NEW_260_META),
]


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s not found. Run from the palomas_orrery repo root." % TARGET)
    with open(TARGET, "rb") as f:
        data = f.read()
    for _, old, new in EDITS:
        for blob in (old, new):
            if any(b > 127 for b in blob):
                fail("patch payload contains non-ASCII bytes; refusing.")
    fp = hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()
    if fp != EXPECTED_FP:
        if b"#### [L-285]" in data:
            fail("ledger already carries L-285 -- this patch has already run.")
        fail("BASE MOVED: fingerprint %s, expected %s (built at 9b891970). "
             "Compare the ledger against the repo before doing anything." % (fp, EXPECTED_FP))
    is_crlf = data.count(b"\r\n") > 0
    conv = (lambda b: b.replace(b"\n", b"\r\n")) if is_crlf else (lambda b: b)
    checked = []
    for name, old, new in EDITS:
        o = conv(old)
        c = data.count(o)
        if c != 1:
            fail("anchor for '%s' found %d times, expected exactly 1." % (name, c))
        checked.append((name, o, conv(new)))
    print("Fingerprint matched (%s). %d anchors verified, each found once." % (fp, len(checked)))
    for name, o, n in checked:
        data = data.replace(o, n, 1)
        print("  applied: " + name)
    with open(TARGET, "wb") as f:
        f.write(data)
    print("Wrote %s (%d bytes, %s line endings). New fingerprint %s."
          % (TARGET, len(data), "CRLF" if is_crlf else "LF",
             hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()))
    print("")
    print("NEXT, before committing: run ledger_index.py (Run button) so the")
    print("index zone shows L-260 and L-267 DONE and L-285 OPEN.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
