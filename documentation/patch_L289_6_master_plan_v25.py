"""
patch_L289_6_master_plan_v25.py -- MASTER_PLAN_INTERACTIVE_GALLERY.md ->
v25: Section 5a gains the 2026-09-06 subsection. The lobby and the
sweep passed the phone; the twelve-edge labels did not and were rebuilt
as the frame HUD; step 2 is still two of three; step 3 (Earth) opens as
a design conversation next session.

Appended, not merged, in the shape of the earlier subsections. The plan
carries SEQUENCING; status stays in the ledger (L-221).

RUN: save at the ORRERY repo root next to
MASTER_PLAN_INTERACTIVE_GALLERY.md, open in VS Code, Run. Independent of
the ledger patch (different file). Then commit, push, report the SHA.

Guards on the LF-normalized md5 of the plan at orrery a57e86b8; a CRLF
working copy passes and is written back as CRLF. Refuses a second run.
All inserted text is ASCII. No .bak.

Written September 6, 2026 with Anthropic's Claude Fable 5.1. Built on
orrery a57e86b82503380e92b4e78cd7d8995a71183f20 at
https://github.com/tonylquintanilla/palomas_orrery (main); gallery state
described is fc8d9fb3ecb2 plus patch_L289_4 delivered, not run. Archive
to documentation/ once run.
"""
import hashlib, os, sys

EXPECT = "27a89bde691a4ea2ada875b3fe9c84ad"
P = "MASTER_PLAN_INTERACTIVE_GALLERY.md"

SECTION = b"""### 2026-09-06 -- the phone passed the lobby and the sweep, failed the
edge labels, and the labels were rebuilt as chrome

Measured at orrery `a57e86b8` and gallery `fc8d9fb3`, both confirmed
against the live remotes. Two Mode 5 rounds since the 2026-09-05
subsection: the phone on 2026-09-05, the desktop and the phone on
2026-09-06. Appended, not merged.

**What passed.** The lobby (L-282): doors, a door tap, a Featured card,
Home. The sweep (L-286): a landscape-only 2D card in portrait sweeps
and swipes; the drag handoff this plan and the ledger both said needed
a real thumb has had one. The back link: fixed the same day (the
Sun's "Gallery" button had been a plain link, so Safari's own back
walked into the Sun) and confirmed on both devices.

**What failed, and why the failure is the useful part.** The
twelve-edge axis labels (L-289) were drawn as text INSIDE the scene.
On the phone they shrank with distance, vanished on zoom-out, were
sliced at the box boundary, and floated on nothing for edges beside
the camera. Tony: "this may be worse than the plotly labels." He was
right, and the lesson is not about labels. Anything drawn in the scene
behaves as scenery; anything that must stay legible at every zoom and
angle belongs in the page. The rebuild followed that line: one chip
naming the uniform grid spacing, a corner triad that turns with the
camera, the First Point of Aries at the x tip with a note that the
frame is the J2000 ecliptic (verified in the renderer before it was
written, sourced to NAIF). A second pass found four defects in the
rebuild -- the note would not close, the coloured grid read as a
second key, arrival spacing disagreed with the chip, the triad did not
follow a touch rotation -- and a fix for all four is delivered and
waiting for the phone.

**What this does to the order.** Nothing moves. Step 2 is still two of
three items built (editor, lobby) and one designed-not-started
(L-286's rooms page, drill-down and breadcrumb, which also retires the
hamburger and the shim). L-289 is Sun-room chrome and rides beside
step 1. Step 3, Earth into the assembler, is next after step 2 and
opens as a DESIGN conversation in the next session -- what Earth's
room shows on arrival, what it inherits from the Sun (the drawer, the
frame zoom, the HUD are all reusable now), what is Earth-specific, and
what the assembler must serve that it does not serve today.

**Two rules this round confirmed, in the plan's own words.** The tree
is the order: the lobby's menu and Featured grid now follow the room
tree in `gallery_config.json`, so the editor's order IS the visitor's
order and no new field was added. And the phone is the gate: three of
the five things built since 2026-09-05 changed after Tony's eyes saw
them, and none of the changes could have come from the headless
renders that preceded them.

**Recorded, not planned.** Tony is checking the sweep's exceptions
systematically with `tools/sweep_report.py`, which names every card by
class. The old-card cleanup is his, in the editor, separate from any
step here. L-290 (relay anchors must name the protocol and skills) is
a process item from a parallel Sonnet session and waits on his ruling.

"""

EDITS = [
    (b"**Status:** v24 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n",
     b"**Status:** v25 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n", 1),
    (b"**Last updated:** September 5, 2026 (v24: Section 5a gains the\n"
     b"2026-09-05 subsection -- L-287 live; the lobby, the 2D sweep and the\n"
     b"twelve-edge labels built and render-gated; the order unchanged; with\n"
     b"Anthropic's Claude Fable 5.1. v23, September 4, 2026: step 2 realigned\n"
     b"from the hall to the lobby, rooms and editor -- L-280 retired, L-282\n"
     b"rewritten, L-286 and L-287 opened.)\n",
     b"**Last updated:** September 6, 2026 (v25: Section 5a gains the\n"
     b"2026-09-06 subsection -- the phone passed the lobby and the sweep and\n"
     b"failed the edge labels, rebuilt as the frame HUD; the order unchanged;\n"
     b"Earth opens as a design conversation next; with Anthropic's Claude\n"
     b"Fable 5.1. v24, September 5, 2026: the 2026-09-05 subsection -- L-287\n"
     b"live; lobby, 2D sweep and twelve-edge labels built and render-gated.\n"
     b"v23, September 4, 2026: step 2 realigned from the hall to the lobby,\n"
     b"rooms and editor -- L-280 retired, L-282 rewritten, L-286 and L-287\n"
     b"opened.)\n", 1),
    (b"### What this section deliberately does not carry\n",
     SECTION + b"### What this section deliberately does not carry\n", 1),
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
    if b"### 2026-09-06 -- the phone passed the lobby" in s:
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
print("MASTER_PLAN_INTERACTIVE_GALLERY.md: %d edits -- v25 status, last-updated block, Section 5a 2026-09-06 subsection." % len(EDITS))
print("Next: commit, push, report the orrery SHA.")
print("Undo is Discard Changes in GitHub Desktop.")
