#!/usr/bin/env python3
"""
patch_L280_5a_critical_path.py -- MASTER_PLAN_INTERACTIVE_GALLERY.md
v21 -> v22: re-measure Section 5a's critical path and retire two stale
NEXT statements.

Built on orrery def557e6fb7d1f4dc9f225b0b54a5aa492a94d48 at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery facts measured at 98cc99bd865feaea3c0e7ad7c3ad9b07db5e5ea8 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

What it does, in one file, four edits, bottom-up:
  4. Section 11 (line ~2347): the NEXT paragraph still names the
     feature-rendering JS layer as the gate. That shipped 2026-08-29.
     Replaced with a pointer to Section 5a's 2026-09-03 order.
  3. Section 5a: appends "2026-09-03 -- the Sun GUI is complete on
     desktop, the phone pass names three defects, and the order to
     Jupiter" before "What this section deliberately does not carry".
  2. Header "Next:" paragraph (line ~44): same stale claim as edit 4.
     Replaced with a pointer to 5a. The L-166 and Layer 3 sentences
     that follow it are kept.
  1. Header status line: v21 -> v22.

How to run: open this file in VS Code, in the palomas_orrery repo root,
and press Run. It edits documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md
in place. It refuses to run against any file whose content does not
match the fingerprint it was built against, refuses to run twice, and
writes nothing at all if any single anchor is missing.

Undo is Discard Changes in GitHub Desktop. No .bak is written
(safe-file-editing 1.10, Git Is the Backup).

Written September 3, 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib
import os
import sys

TARGET = os.path.join("documentation", "MASTER_PLAN_INTERACTIVE_GALLERY.md")
EXPECTED_FP = "6dd779bf1599c9e2b0661997fc2221d2"   # md5 of LF-normalized bytes at def557e6

# ----------------------------------------------------------------------
# Edit 1 -- header status line
# ----------------------------------------------------------------------
OLD_STATUS = b"**Status:** v21 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n"
NEW_STATUS = b"**Status:** v22 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n"

# ----------------------------------------------------------------------
# Edit 2 -- header "Next:" paragraph (stale since 2026-08-29)
# ----------------------------------------------------------------------
OLD_HEADER_NEXT = (
b"**Next: F1's data layer is done, but nothing renders it yet.** A repo-wide\n"
b"search (Python and JS/HTML) for anything consuming `ring_system`,\n"
b"`van_allen_belts`, `atmosphere_shell`, or `radiation_belts` found nothing.\n"
b"Artifact 1 (Earth)'s own acceptance test confirms this by design: features\n"
b"dispatch as data only, with \"JavaScript rendering them\" as the intended\n"
b"next step -- and that JS was never written. Writing that feature-rendering\n"
b"layer is the real next gate before Artifact 2 (Jupiter/Saturn) can attempt\n"
b"Mode 5. Alongside it, the trust system's consumption side is now tracked as L-166\n"
)
NEW_HEADER_NEXT = (
b"**Next: the order is in Section 5a, dated 2026-09-03, and it is five\n"
b"steps: the Sun room's phone controls, the hall (L-280), Earth into the\n"
b"assembler, the transport (segment 2) built alongside Earth, then\n"
b"Jupiter and Saturn.** The paragraph that stood here until v22 said the\n"
b"feature-rendering JS layer was \"never written\" and was the gate before\n"
b"Artifact 2. That layer is `feature_renderers.js`; it shipped with the\n"
b"Sun exhibit on 2026-08-29 and has drawn 18 shells on the live page\n"
b"since. The sentence outlived the fact by five days and two plan\n"
b"versions -- The Correction Does Not Travel, on this document's own\n"
b"front page. Alongside the order, the trust system's consumption side is tracked as L-166\n"
)

# ----------------------------------------------------------------------
# Edit 3 -- Section 5a append
# ----------------------------------------------------------------------
ANCHOR_5A_TAIL = b"### What this section deliberately does not carry\n"
APPEND_5A = (
b"### 2026-09-03 -- the Sun GUI is complete on desktop, the phone pass\n"
b"names three defects, and the order to Jupiter\n"
b"\n"
b"Measured at orrery `def557e6` and gallery `98cc99bd`, both confirmed\n"
b"against the live remotes. Appended, not merged, in the shape of the\n"
b"August 25 and 29 subsections above.\n"
b"\n"
b"**What shipped between August 29 and today.** The Sun room's GUI\n"
b"(L-267) in three stages: A, the drawer replacing the legend and the\n"
b"portrait defect fixed (gallery `2ed12564`); B, the mockup ported --\n"
b"row split with a GO, focus label on the drawer handle, cross-marker\n"
b"navigation (`e0edd16c`), and the click-hang it exposed fixed by\n"
b"deferring the focus call one tick (`6fd6baaf`, recorded portably as\n"
b"L-278 and as a field note in gallery-assembler 1.2); C, the i panel\n"
b"following the focus with the shell's swatch, name and one link out\n"
b"(`0edf4bf4`), the i button wired for the Sun path at all -- it had\n"
b"been decoration since Stage A (`42a906f6`) -- and panel and drawer\n"
b"sharing the height, 40/60 (`6cfaf318`, `98cc99bd`). The 22 curated\n"
b"links (L-265) are served with zero placeholders. Mode 5 passed on\n"
b"desktop for every trial, including the hover-seize from the\n"
b"2026-08-30 study, which did not reproduce on the live page. The wing\n"
b"is designed and recorded in L-280 (door, hall, two rooms, What's New),\n"
b"L-281 (guest book), L-282 (lobby), L-283 (theme) and L-284 (retire the\n"
b"social export). Nothing of the wing is built.\n"
b"\n"
b"**The phone pass ran today, and it is not a pass.** Tony, on a phone,\n"
b"2026-09-03, Mode 5. Three findings, in his order:\n"
b"\n"
b"- The Plotly modebar is missing, so there is no way to reset the\n"
b"  scene. This is the gallery's own rule, not a Sun defect:\n"
b"  `interactive.html` hides the modebar below 768 px (CSS at line 548\n"
b"  and `displayModeBar: window.innerWidth > 768` at lines 1070 and\n"
b"  1497, measured at `98cc99bd`). On the desktop the modebar was the\n"
b"  reset; on the phone nothing replaced it.\n"
b"- The two-finger zoom gesture does not work in the 3D scene.\n"
b"- Landscape works.\n"
b"\n"
b"The static gallery already solved both. `index.html` at the same SHA\n"
b"carries `zoomIn`, `zoomOut`, `panReset` and `resetStandalone` buttons\n"
b"(lines 1572 to 1625) with `touchstart` handlers, and Gallery Studio\n"
b"draws the same `+` / `-` pair (`tools/gallery_studio.py` lines 2447\n"
b"and 2473). Tony's ruling: land on ONE control set that works for both\n"
b"the static gallery and the interactive wing. The Sun room is the\n"
b"first room, so whatever it gets, the hall's chrome inherits; that is\n"
b"why this is step 1 and not a finishing item.\n"
b"\n"
b"These findings are Mode 5 results and belong in the ledger, which\n"
b"carries status authority (L-221). L-260 still reads \"mobile is\n"
b"untested\" and L-267 still reads \"the phone pass is what remains\"; both\n"
b"are now wrong in the same direction and are owed an amendment. This\n"
b"section records that and does not assert around it.\n"
b"\n"
b"**The order, confirmed by Tony 2026-09-03.** Braided so each step\n"
b"feeds the next; the general audit and the constants work continue\n"
b"beside it and gate nothing here.\n"
b"\n"
b"1. **Sun room: phone controls.** Reset and zoom on a phone, one\n"
b"   control set shared with the static gallery. Then the phone pass\n"
b"   again. This is what stands between the first room and complete.\n"
b"2. **The hall (L-280), designed in conversation first, portrait\n"
b"   first.** The door card on the main page, the placard, the two\n"
b"   rooms, the What's New JSON and the rule that shipping patches\n"
b"   append to it. Until this exists the Sun room is a URL nobody can\n"
b"   find. The chrome from step 1 is what the hall copies.\n"
b"3. **Earth into the assembler.** The next body. Three items travel\n"
b"   together: Earth's shells and belts drawn through\n"
b"   `feature_renderers.js`, which also exercises the belt path Jupiter\n"
b"   will need; the Earth slice of L-268's collapsed-feature\n"
b"   remediation; and L-237, Artifact 1's stale golden record, which\n"
b"   reopens anyway the moment Earth grows features.\n"
b"4. **Segment 2, the transport, built alongside Earth.** Earth would\n"
b"   be the second body whose constants reach the gallery by hand-editing\n"
b"   `objects_config.json`. The August 29 subsection said the transport\n"
b"   should land before hand-copying becomes routine. Two bodies is\n"
b"   where it becomes routine.\n"
b"5. **Jupiter and Saturn.** Segment 1 sliced to the thirty measured\n"
b"   numbers, then segment 4 locks Artifact 2, and the premade Solar\n"
b"   System Explorer room starts being replaced by interactive planets\n"
b"   as L-280 rules.\n"
b"\n"
b"Off the path and clustered: L-284 (retire the social export) with\n"
b"L-254 (dead sphere-shell builders), both orrery-side, worked the next\n"
b"time the orrery side is open for other reasons. Tony's ruling,\n"
b"2026-09-03.\n"
b"\n"
b"**One thing this plan never carried and now does.** The body order for\n"
b"the assembler -- Sun, Earth, Jupiter and Saturn -- had lived in\n"
b"conversation and in memory. The five segments sequence propagation\n"
b"shapes and provenance slices; the August 25 subsection named the\n"
b"drawn-feature axis and said nothing sequences it. The list above is\n"
b"the first place the order is written down. Bodies after Saturn are\n"
b"not ordered here; that is a ruling for when Saturn is on screen.\n"
b"\n"
b"**Rows in the 2026-08-23 table that are now stale, by name.**\n"
b"\"Segment 3, assembler draw: NOT STARTED\" -- done for the Sun, and\n"
b"its GUI is complete on desktop. \"Artifact 1, Earth: LOCKED\" --\n"
b"reopened, and now step 3. \"Segment 4, Artifact 2: gated on segment\n"
b"3\" -- segment 3 is no longer the gate; steps 1 to 4 above are. Left\n"
b"standing for the same reason the August 25 append gave: the table is\n"
b"re-stated only by a pass that reads the repo.\n"
b"\n"
)

# ----------------------------------------------------------------------
# Edit 4 -- Section 11 NEXT paragraph (stale since 2026-08-29)
# ----------------------------------------------------------------------
OLD_S11_NEXT = (
b"NEXT, and no longer waiting on the scanner work (the braid,\n"
b"2026-08-22): write the feature-rendering JS layer (ring/shell/belt\n"
b"consumers). It is what stands between here and attempting Artifact 2\n"
b"(Jupiter/Saturn) Mode 5, it depends on nothing, and the data it needs\n"
b"is already served. Layer 3 (nightly Task\n"
)
NEW_S11_NEXT = (
b"NEXT is not restated here; it drifted the same way the skill versions\n"
b"did. Until v22 this line said the feature-rendering JS layer was still\n"
b"to be written, five days after it shipped with the Sun exhibit. The\n"
b"order lives in Section 5a, dated 2026-09-03, and only there (the\n"
b"same fix-the-producer ruling as the paragraph above). Layer 3 (nightly Task\n"
)

EDITS = [
    # bottom-up: later in the file first
    ("Section 11 NEXT paragraph",  OLD_S11_NEXT,   NEW_S11_NEXT),
    ("Section 5a append",          ANCHOR_5A_TAIL, APPEND_5A + ANCHOR_5A_TAIL),
    ("header Next paragraph",      OLD_HEADER_NEXT, NEW_HEADER_NEXT),
    ("header status v21 -> v22",   OLD_STATUS,     NEW_STATUS),
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

    # ASCII gate on the payload (safe-file-editing, Encoding Gate)
    for _, old, new in EDITS:
        for blob in (old, new):
            if any(b > 127 for b in blob):
                fail("patch payload contains non-ASCII bytes; refusing.")

    fp = hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()
    if fp != EXPECTED_FP:
        if NEW_STATUS.replace(b"\n", b"\r\n") in data or NEW_STATUS in data:
            fail("file already reads v22 -- this patch has already run.")
        fail("BASE MOVED: fingerprint %s, expected %s (built at def557e6). "
             "Compare the file against the repo before doing anything." % (fp, EXPECTED_FP))

    is_crlf = data.count(b"\r\n") > 0
    conv = (lambda b: b.replace(b"\n", b"\r\n")) if is_crlf else (lambda b: b)

    # verify every anchor before writing anything
    checked = []
    for name, old, new in EDITS:
        o = conv(old)
        n = old != new and conv(new)
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

    new_fp = hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()
    print("Wrote %s (%d bytes, %s line endings). New fingerprint %s."
          % (TARGET, len(data), "CRLF" if is_crlf else "LF", new_fp))
    print("Check: header reads v22, Section 5a ends with the 2026-09-03 append,")
    print("       Section 11's NEXT line points at 5a. Then commit and push in GitHub Desktop.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
