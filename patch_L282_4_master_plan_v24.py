"""
patch_L282_4_master_plan_v24.py -- MASTER_PLAN_INTERACTIVE_GALLERY.md ->
v24: Section 5a gains the 2026-09-05 subsection (L-287 live; the lobby,
the sweep and the twelve-edge labels built and render-gated; the step-2
build order half done), and the header moves with it.

Appended, not merged, in the shape of the August 25, 29 and September 3
subsections. The plan carries SEQUENCING; status stays in the ledger
(L-221), so nothing here asserts a status the ledger does not.

RUN: save at the ORRERY repo root next to
MASTER_PLAN_INTERACTIVE_GALLERY.md, open in VS Code, Run. Independent of
the ledger patches (different file). Then commit, push, report the SHA.

Guards on the LF-normalized md5 of the plan at orrery 9652a43d; a CRLF
working copy passes and is written back as CRLF. Refuses a second run.
All inserted text is ASCII. No .bak; undo is Discard Changes in GitHub
Desktop.

Written September 5, 2026 with Anthropic's Claude Fable 5.1. Built on
orrery 9652a43db8361a9d904002e6a4271a34281be8a1 at
https://github.com/tonylquintanilla/palomas_orrery (main); gallery state
described is 503fa387068a176fa7e12d2ab8df3752c8ffe429 plus four
delivered, unrun gallery patches. Archive to documentation/ once run.
"""
import hashlib, os, sys

EXPECT = "8e89b90e149883909b81ba604e9c1564"
P = "MASTER_PLAN_INTERACTIVE_GALLERY.md"

SECTION = b"""### 2026-09-05 -- L-287 is live, and the lobby, the sweep and the
twelve-edge labels are built and waiting for the phone

Measured at orrery `9652a43d` and gallery `503fa387`, both confirmed
against the live remotes at session start; neither moved during the
session, because Tony was away from his machine. Appended, not merged.

**What shipped on 2026-09-04/05 (the machine session).** Step 2's
first item, the editor and room tree (L-287), is DONE and live at
gallery `503fa387`: `gallery_config.json` and `gallery_metadata.json`
are schema version 2 (a room tree; one card per exhibit with two file
slots, shape, live, featured, sources); 105 cards, none in storage;
`tools/gallery_editor.py` rewritten; `index.html` carries a reader
SHIM that maps rooms onto the old category menu so the schema could
ship before the lobby. Two corrections to the design record travelled
with it: 38 landscape/portrait pairs, not 33; seven consumers of the
metadata, not five (`gallery_cleanup.py`, which deletes orphans, and
`gallery_json_fixer.py`).

**What was built on 2026-09-05 (the away session), none of it run.**
Four gallery patches and two orrery patches wait at the repo roots;
every one guards on the bytes it was built against and refuses
otherwise. The record of each is in the ledger; the plan's interest
is what they do to the order.

- **Step 2's second item, the lobby (L-282), is built.** Rulings by
  phone: the section is FEATURED, from the existing flag, no dated
  feed; live cards read INTERACTIVE; empty rooms read UNDER
  CONSTRUCTION; doors above Featured. A door tap opens the existing
  menu at that door until step 2's third item, the rooms and
  breadcrumb (L-286), replaces it. So the hamburger and the shim
  survive one more step, and L-286 retires both.
- **The room-shape rule (L-286) is built for 2D plots ahead of the
  rooms it was written for.** The lobby's counts surfaced that the
  shim still filtered cards by mode, hiding every landscape-only card
  on a phone, against L-287's own rule. Tony: "no squeezed
  landscape" -- landscape on the phone stays; portrait sweeps. The
  filter is lifted and the sweep built in one patch, because showing
  the cards without the sweep would have shown them compressed.
- **L-289 (the Sun's axis labels on the phone) is designed and
  built.** Tony's design, replacing the top-view/back-view idea:
  labels on all twelve edges of the box, tick values and axis names,
  thinned by count, no label at a vertex, the name on an unlabeled
  line, no dimming. The page owns the ticks. This is chrome the
  future rooms inherit, which is why it belongs beside step 1's nav
  cluster rather than in a finishing list.

**What this does to the order.** Nothing moves. Step 2 is two of
three items built and one designed-not-started (L-286's drill-down and
breadcrumb). Step 3, Earth into the assembler, is unchanged and still
next after step 2. The guest book (L-281) and the theme (L-283) stay
where the September 3 list left them.

**The gate on all of it is one phone pass.** The lobby, the sweep and
the edge labels were each exercised in a headless browser here --
lobby and sweep on the real page with Plotly served locally, the edge
labels in a stand-in scene because the Sun page's Pyodide cannot load
in the sandbox -- with no script errors. What a headless run cannot
say is how any of it reads in a hand. The sweep intercepts the plot's
own drag layer, which L-286 already said needs a real phone before the
rule is trusted. Until Tony's pass, every one of these is a claim.

**One measurement worth keeping.** The mode filter hid 49 of 105
exhibits from phone visitors: Solar System showed 31 of 39, Earth
System 22 of 57, Stars 3 of 9. It had been in force since the
Desktop/Mobile toggle was added and nobody had counted, because the
menu counted only what it showed. The lobby counts what exists, and
that is how it surfaced.

"""

EDITS = [
    (b"**Status:** v23 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n",
     b"**Status:** v24 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n", 1),
    (b"**Last updated:** September 4, 2026 (v23: Section 5a step 2 realigned\n"
     b"from the hall to the lobby, rooms and editor -- L-280 retired, L-282\n"
     b"rewritten, L-286 and L-287 opened; with Anthropic's Claude Fable 5.1)\n",
     b"**Last updated:** September 5, 2026 (v24: Section 5a gains the\n"
     b"2026-09-05 subsection -- L-287 live; the lobby, the 2D sweep and the\n"
     b"twelve-edge labels built and render-gated; the order unchanged; with\n"
     b"Anthropic's Claude Fable 5.1. v23, September 4, 2026: step 2 realigned\n"
     b"from the hall to the lobby, rooms and editor -- L-280 retired, L-282\n"
     b"rewritten, L-286 and L-287 opened.)\n", 1),
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
    if b"### 2026-09-05 -- L-287 is live" in s:
        die("this patch has already been applied to %s" % P)
    die("%s does not match orrery 9652a43d (md5 %s, expected %s)" % (P, got, EXPECT))
print("ok  %s matches 9652a43d%s" % (P, " (working copy is CRLF)" if crlf else ""))

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
print("MASTER_PLAN_INTERACTIVE_GALLERY.md: %d edits -- v24 status, last-updated block, Section 5a 2026-09-05 subsection." % len(EDITS))
print("Next: commit, push, report the orrery SHA.")
print("Undo is Discard Changes in GitHub Desktop.")
