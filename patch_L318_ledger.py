"""patch_L318_ledger.py -- the 2026-09-10 phone look recorded; L-320 ruled
and built; L-318 designed and built. Replaces patch_L316_3_ledger.py and
patch_L320_ledger.py, neither of which needs to run.

ORRERY repo (palomas_orrery). Built on orrery b914c3f0 at
https://github.com/tonylquintanilla/palomas_orrery ; findings read at
gallery 4add58bc at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and at
plotly.js v2.35.2 (the version interactive.html loads).

Run: save this file in the orrery repo root (beside LEDGER_CONSOLIDATED.md),
open it in VS Code, click Run.  Or from a terminal in the repo root:
    python patch_L318_ledger.py

It picks up from whichever state the ledger is in: as pushed at b914c3f0,
after patch_L316_3_ledger.py, or after patch_L320_ledger.py. All three end
at the same text.

What it does, all-or-nothing:
  LEDGER_CONSOLIDATED.md
    - header stamps;
    - L-316 and L-317: pass Mode 5 on the phone; their Gaps narrow;
    - L-318 opened, designed and built: naming a shell in the drawer opens
      its hover text as a label (patch_L318_drawer_label.py);
    - L-319 opened: focusing a smaller shell cuts larger lit shells flat;
    - L-320 opened, ruled and built: every info marker starts 5 degrees off
      the pole (patch_L320_marker_offset.py).

Guard: the ledger's text outside the generated INDEX zone, line endings
normalised, must match one of the three states above. Windows line
endings are kept.

Permanent: the ledger text. Disposable: this script.
Success prints one 'ok' per edit and 'patch applied'. Any failure prints
one ERROR / ANCHOR FAIL line and writes nothing.
Undo is Discard Changes in GitHub Desktop.

Then run ledger_index.py -- expect
"OK: 315 L-blocks parsed, no consistency problems."

Written September 10, 2026 with Anthropic's Claude Opus 5.
"""
import hashlib, os, sys

LEDGER = "LEDGER_CONSOLIDATED.md"
INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"
FP_BASE = "1081d559ca3f3aca6d132ae62a57880b"      # b914c3f0 as pushed
FP_CAPTURED = "9befc96d6cd30e373ec33d3fff5349e9"  # + patch_L316_3_ledger.py
FP_L320 = "566e75e7ea983c400e69c80a80d49c71"      # + patch_L320_ledger.py
FP_FINAL = "d6a7a2899747439c15f09f339d5a68fa"

CAPTURE = [
("header stamp",
b"""(L-316 round 2 on Tony's Mode 5: the title stays and the arrow cross
moves top right; L-317's outlines not yet judged), built on 204d1f5d.
""",
b"""(L-316 round 2 on Tony's Mode 5: the title stays and the arrow cross
moves top right; L-317's outlines not yet judged), built on 204d1f5d.
Module updated: September 10, 2026 with Anthropic's Claude Opus 5
(L-316 and L-317 pass Mode 5 on the phone; L-318, L-319 and L-320
opened from the same look), built on b914c3f0.
"""),
("L-316 round 2 passes; Gap narrows",
b"""**Gap:** Tony's Mode 5, round 2. Portrait phone, both rooms: the title
is back, the cross sits top right clear of it, and the marker at the top
of a zoomed shell is visible; rotate to landscape and back and the cross
follows. Desktop: unchanged -- this also covers L-310's desktop check.
Then, at interactive-exhibit's next bump, its nav cluster row names the
arrows (L-310) and the portrait placement (this item).
""",
b"""- **Round 2 passes on the phone, 2026-09-10** (screenshots of both
  rooms, portrait and landscape). Tony, to each check: the title is back
  and the cross sits top right, clear of it -- "yes"; the marker at the
  top of a zoomed-in shell is visible -- "yes"; rotating to landscape and
  back moves the cross -- "Yes". The landscape screenshot shows the cross
  back under + and -. [render-confirmed Mode 5 @ gallery `4add58bc`] He
  asked which two rooms were meant: the Sun and Earth, and his
  screenshots cover both.
**Gap:** desktop, not yet looked at: title and cross exactly as before --
this also covers L-310's desktop check. Then, at interactive-exhibit's
next bump, its nav cluster row names the arrows (L-310) and the portrait
placement (this item).
"""),
("L-317 outlines pass; Gap narrows",
b"""**Gap:** (1) Tony's Mode 5 on the phone, both rooms: the white outlines
read on the warm shells, and nothing else changed. (2) At
orrery-coding-conventions' next bump: the two-standards rule, and the
example corrected to `create_info_marker`.
""",
b"""- **The outlines pass on the phone, 2026-09-10.** Asked whether the
  marker at the top of a zoomed shell shows, including the outer core's
  white outline, Tony: "yes". [render-confirmed Mode 5 @ gallery
  `4add58bc`] How readily a finger reaches those markers is L-318; where
  they sit against the drawn axis is L-320.
**Gap:** at orrery-coding-conventions' next bump: the two-standards rule,
and the example corrected to `create_info_marker`.
"""),
("L-318, L-319 and L-320 opened",
b"""#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery""",
b"""#### [L-318] Reading a shell's hover text on the phone: taps miss in the mesh, and labels mid-screen lose their pointer
<!-- L:318 status:OPEN upd:2026-09-10 section:A flag: rice:3/2/70/2 -->
- **Tony, 2026-09-10, from the L-316 round-2 phone look (chat, not his
  hand):** "The hovermarker are still frustrating to trigger with a finger
  gesture. Sometimes they work especially if isolated, and sometimes not
  especially if they are in the mesh. Suggestion: activate the hovertext
  when the user selects a shell on the drawer. It would deselect as
  usual. Keep the marker selection method too." And: "the hoverbox for
  the sun shell points at the hovermarker but the earth's does not.
  Pointing helps to associate the shell with the description."
- **Why a label loses its pointer, read from Plotly 2.35.2's source**
  (`src/components/fx/hover.js`, where a label's anchor is chosen): the
  label goes to the right of its point if it fits, else to the left if it
  fits, else it is centred over the point with no pointer and nudged back
  on screen. So it is position, not room. The Sun's outer corona marker
  sat near the right edge, with room to its left; Earth's upper
  atmosphere marker was not near an edge. `gallery/feature_renderers.js`
  wraps hover text at `HOVER_WIDTH` = 70 characters, wider than half a
  portrait phone, so a marker away from the edges loses its pointer.
  [verified @ plotly.js `v2.35.2` and gallery `4add58bc`]
- **What a drawer row tap does today.** It FOCUSES: the camera frames
  that shell and nothing else changes (`sunFocusOn`; Tony's G2 ruling,
  2026-08-30, in the code's words "Focusing moves the camera and NOTHING
  ELSE"). A label on focus adds a second effect to that gesture on Tony's
  word now; the design round records it as an amendment to G2, not a
  quiet exception. [verified @ gallery `4add58bc`]
- **Mechanism, not chosen.** A 3D hover label comes from Plotly's WebGL
  picking: `src/plots/gl3d/scene.js` calls `Fx.loneHover` with screen
  coordinates it computes itself. Showing one on request means computing
  those in the page, or using `layout.scene.annotations`, which the gl3d
  layout accepts; its attributes are to be read before the design round.
  [verified @ plotly.js `v2.35.2`]
- **Questions for the design round:** what shows on focus (the full hover
  text, or less); what clears it (another focus, closing the drawer, a
  tap on the scene); a focused shell that is not drawn (G2's honest empty
  frame suggests no label); and the wrap width on narrow screens, which
  trades a taller label for keeping the pointer.
- **Note:** RICE 3/2/70/2 -> 2.1 proposed, not confirmed.
**Gap:** design round, zero code; then one patch in `interactive.html`
and `gallery/feature_renderers.js`, and Mode 5 on the phone in both
rooms.
**Ref:** L-267 (the drawer and focus), L-316, L-317, L-319, L-320,
`interactive.html` (`sunFocusOn`), `gallery/feature_renderers.js`
(`wrapHover`, `HOVER_WIDTH`), plotly.js v2.35.2
`src/components/fx/hover.js` and `src/plots/gl3d/scene.js`.

#### [L-319] Focusing a smaller shell cuts larger lit shells flat at the frame's box
<!-- L:319 status:OPEN upd:2026-09-10 section:A flag: rice:2/1/70/2 -->
- **Tony, 2026-09-10:** "This lower mantle view is clipped." His portrait
  screenshot: the drawer focused on Earth: Lower Mantle, the grid at
  0.00001 AU (1,496 km), the upper mantle and the atmosphere lit, and
  their dots ending in a straight line along the top of the box.
- **Why, from the code.** Focusing frames the focused shell, with no
  floor (`sunFrameOn`; L-267 Stage B, "THE FRAME FOLLOWS THE FOCUS, AND
  CARRIES NO FLOOR"). Shells lit and larger than the focus reach past that
  box, and the screenshot shows them stopping at its faces. [code
  verified @ gallery `4add58bc`; the cut read off the screenshot]
- **Question:** whether a cut at the box reads as a deliberate cutaway
  worth keeping, or needs another answer. Focus cannot switch the larger
  shells off without breaking G2 (focus changes only the camera).
- **Note:** RICE 2/1/70/2 -> 0.7 proposed, not confirmed.
**Gap:** Tony's call on the question; then design and one patch if it
changes.
**Ref:** L-267 (Stage B), L-318, `interactive.html` (`sunFrameOn`,
`sunGroupRadius`, `sunOutermostShown`).

#### [L-320] Info markers on the drawn axis, and the orrery's per-shell marker angles never served
<!-- L:320 status:OPEN upd:2026-09-10 section:A flag: rice:3/2/80/1 -->
- **Tony, 2026-09-10:** the marker at the top of a zoomed shell is
  visible, "but less when the marker sits on the z axis. An angular
  offset of maybe 5 degrees would help."
- **Two rules for one thing, found before building.** The orrery declares
  a marker angle only where a shell needs one (`info_polar_deg` in
  `shell_configs.py`, applied by `build_sphere_shell`): Earth's crust 10
  degrees, lower atmosphere 20, upper atmosphere 30, each clearing the one
  below, with the cores and mantles on the pole; the Sun's skin stack
  steps 20 in `solar_visualization_shells.py`. None of that is served to
  the gallery. The gallery's `renderShellSet` steps each shell in a group
  20 degrees further than the one before, starting ON the pole, so the
  first shell of each group sits on the axis the Earth room draws -- the
  inner core and the lower atmosphere among them -- and the interior
  angles differ from the orrery's. [verified @ orrery `b914c3f0` and
  gallery `4add58bc`]
- **The same lesson as L-317:** the orrery has a solution and the
  interactive did not carry it. So Tony's ruling comes before any build:
  copy the orrery's angles, and whether 5 degrees applies to markers left
  on the axis in the gallery only or in both; or shift the gallery's own
  steps.
- **Note:** RICE 3/2/80/1 -> 4.8 proposed, not confirmed.
**Gap:** Tony's ruling; then one gallery patch, a smoke check that fails
if a marker lands on the axis, and Mode 5 on the phone.
**Ref:** L-317, L-318, `shell_configs.py` (`info_polar_deg`),
`orrery_rendering.py` (`build_sphere_shell`),
`gallery/feature_renderers.js` (`renderShellSet`),
skills/orrery-coding-conventions/SKILL.md (marker separation).

#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery"""),
]

RULING = [
("header stamp for the L-320 ruling",
b"""(L-316 and L-317 pass Mode 5 on the phone; L-318, L-319 and L-320
opened from the same look), built on b914c3f0.
""",
b"""(L-316 and L-317 pass Mode 5 on the phone; L-318, L-319 and L-320
opened from the same look), built on b914c3f0.
Module updated: September 10, 2026 with Anthropic's Claude Opus 5
(L-320 ruled by Tony and built in the gallery: every info marker starts
5 degrees off the pole), built on b914c3f0.
"""),
("L-320 ruling and build",
b"""- **The same lesson as L-317:** the orrery has a solution and the
  interactive did not carry it. So Tony's ruling comes before any build:
  copy the orrery's angles, and whether 5 degrees applies to markers left
  on the axis in the gallery only or in both; or shift the gallery's own
  steps.
- **Note:** RICE 3/2/80/1 -> 4.8 proposed, not confirmed.
**Gap:** Tony's ruling; then one gallery patch, a smoke check that fails
if a marker lands on the axis, and Mode 5 on the phone.
**Ref:** L-317, L-318, `shell_configs.py` (`info_polar_deg`),
`orrery_rendering.py` (`build_sphere_shell`),
`gallery/feature_renderers.js` (`renderShellSet`),
skills/orrery-coding-conventions/SKILL.md (marker separation).
""",
b"""- **The same lesson as L-317:** the orrery has a solution and the
  interactive did not carry it, so the ruling came before any build.
  Offered: the orrery's angles with 5 degrees off the axis in both; the
  same in the gallery only; or the gallery's own steps shifted 5 degrees.
- **Tony's ruling, 2026-09-10** (his choice of the three; the degree sign
  spelled out): "Keep gallery's steps, shift all 5 degrees." The gallery
  keeps its own 20-degree steps rather than the orrery's per-shell
  angles. The two rules stay different by his choice, and the orrery is
  not touched.
- **Built 2026-09-10** by `patch_L320_marker_offset.py` in the gallery.
  Measured first, nine markers sat exactly on the z axis -- Sun room:
  Core, Termination Shock, Gravitational Influence; Earth room: Inner
  Core, Lower Atmosphere, Exosphere / Geocorona, Low Earth Orbit inner
  edge, Hill Sphere, Terminator. `INFO_MARKER_OFFSET_DEG` = 5 in
  `gallery/feature_renderers.js` (MODE-5 KNOB): `renderShellSet`'s steps
  start there, and `renderAtmosphereShell`, used in neither room, moves
  off the pole by the same amount. `gallery/earth_geometry.js` steps the
  terminator's marker along its own circle to the nearest drawn point, so
  it leaves the axis and stays on the line (Tony's 2026-09-09 ruling that
  it sit ON the line holds). `smoke_sun_shells.js` and
  `smoke_earth_geometry.js` each gain a check that no marker is within 4
  degrees of the axis (now 26 and 32 checks). Both fail with the knob at
  zero, the Earth check fails with the terminator back at its top point,
  and both pass with the knob at 10. After the patch the closest marker
  in each room sits at 5.0 degrees. [verified in the sandbox;
  render-gated]
- **Note:** RICE 3/2/80/1 -> 4.8 proposed, not confirmed.
**Gap:** Mode 5 on the phone, both rooms: a marker at the top of a zoomed
shell reads clear of the axis line.
**Ref:** L-317, L-318, `shell_configs.py` (`info_polar_deg`),
`orrery_rendering.py` (`build_sphere_shell`),
`gallery/feature_renderers.js` (`renderShellSet`,
`INFO_MARKER_OFFSET_DEG`), `gallery/earth_geometry.js` (the terminator),
`documentation/patch_L320_marker_offset.py` (gallery),
skills/orrery-coding-conventions/SKILL.md (marker separation).
"""),
]

L318 = [
("header stamp for L-318",
b"""(L-320 ruled by Tony and built in the gallery: every info marker starts
5 degrees off the pole), built on b914c3f0.
""",
b"""(L-320 ruled by Tony and built in the gallery: every info marker starts
5 degrees off the pole), built on b914c3f0.
Module updated: September 10, 2026 with Anthropic's Claude Opus 5
(L-318 designed in conversation and built in the gallery: naming a shell
in the drawer opens its hover text as a label), built on b914c3f0.
"""),
("L-318 design, ruling and build",
b"""**Gap:** design round, zero code; then one patch in `interactive.html`
and `gallery/feature_renderers.js`, and Mode 5 on the phone in both
rooms.
**Ref:** L-267 (the drawer and focus), L-316, L-317, L-319, L-320,
`interactive.html` (`sunFocusOn`), `gallery/feature_renderers.js`
(`wrapHover`, `HOVER_WIDTH`), plotly.js v2.35.2
`src/components/fx/hover.js` and `src/plots/gl3d/scene.js`.
""",
b"""- **Design settled in conversation, 2026-09-10.** Proposed and accepted:
  a tap on a shell's name frames the shell as before and also opens its
  hover text as a label pinned to its info marker, with an arrow; a tap
  on another name moves it; unticking the shell closes it; a shell that
  is not drawn gets no label; tapping a marker works as before. Tony,
  asked what else closes it: "A tap anywhere in the scene." This amends
  G2 on his word -- the name still never switches a shell on or off.
- **Built 2026-09-10** by `patch_L318_drawer_label.py` in the gallery,
  `interactive.html` only. The label is a Plotly scene annotation at the
  marker's 3D point (`layout.scene.annotations` carries x, y, z, ax, ay,
  the anchors and `showarrow`, read @ plotly.js `v2.35.2`
  `src/components/annotations3d/attributes.js`), with the marker's own
  hover text rewrapped at 34 characters and its border and arrow in the
  shell's colour. The box goes toward the middle of the screen, chosen
  from the marker's place against the live camera, and re-anchors after
  a drag or any relayout. Every label update also sends the live camera:
  Plotly's 3D replot re-applies the layout's stored camera (`scene.js`,
  `setViewport`), which a touch rotation never updates, so without it the
  view would snap back. A tap is one pointer moving 10 px or less within
  500 ms; a drag, a pinch and a cancelled touch are not. Close and
  re-anchor run a tick later, out of Plotly's own handling (the L-278
  lesson). The G2 comment above the row handler is amended in place.
  MODE-5 KNOBS: `SUN_LABEL_WRAP_CHARS`, `SUN_LABEL_OFFSET_PX`,
  `SUN_LABEL_FONT_PX`, `SUN_LABEL_TAP_PX`, `SUN_LABEL_TAP_MS`. Sandbox:
  the page's script parses; 19 checks of the label functions against a
  stub plot pass -- the wrap, the box's side in four positions, open,
  move, a refresh that sends nothing, no label for an undrawn shell,
  close on untick, close on a tap, and a drag, a pinch and a cancelled
  touch that do not close it. One check first failed on its own wrong
  expectation and was corrected. Nothing rendered. [render-gated]
- **Still open here:** a tap on a marker still shows Plotly's own hover
  box, which drops its pointer mid-screen at `HOVER_WIDTH` 70. Narrowing
  it trades a taller box for the pointer; that waits for Tony's look at
  the drawer label.
**Gap:** Tony's Mode 5 on the phone, both rooms: name a shell and its
label points at its marker; turn the view and the label stays with it;
tap the scene and it closes; untick the shell and it closes. Then the
marker-tap pointer question above.
**Ref:** L-267 (the drawer and focus), L-278, L-316, L-317, L-319, L-320,
`interactive.html` (`sunFocusOn`, `sunLabelShow`, `sunLabelInstall`),
`gallery/feature_renderers.js` (`wrapHover`, `HOVER_WIDTH`), plotly.js
v2.35.2 `src/components/fx/hover.js`, `src/plots/gl3d/scene.js` and
`src/components/annotations3d/attributes.js`,
`documentation/patch_L318_drawer_label.py` (gallery).
"""),
]


def body_fp(lf):
    if lf.count(INDEX_START) != 1 or lf.count(INDEX_END) != 1:
        return None
    a = lf.index(INDEX_START)
    b = lf.index(INDEX_END) + len(INDEX_END)
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest() if b > a else None


def apply(lf, edits, steps):
    for name, old, new in edits:
        n = lf.count(old)
        if n != 1:
            raise ValueError("ANCHOR FAIL: %s expected 1 match, got %d" % (name, n))
        lf = lf.replace(old, new)
        steps.append(name)
    return lf


STAGES = [  # (edits, fingerprint after)
    ("CAPTURE", "FP_CAPTURED"),
    ("RULING", "FP_L320"),
    ("L318", "FP_FINAL"),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(root, LEDGER)
    if not os.path.exists(fn):
        print("ERROR: not found: %s (run from the orrery repo root)" % fn); return 1
    with open(fn, "rb") as f:
        raw = f.read()
    was_crlf = b"\r\n" in raw
    lf = raw.replace(b"\r\n", b"\n")
    fp = body_fp(lf)
    tag = " [CRLF: Windows line endings; kept]" if was_crlf else ""
    g = globals()
    states = ["FP_BASE", "FP_CAPTURED", "FP_L320", "FP_FINAL"]
    names = {"FP_BASE": "b914c3f0 as pushed", "FP_CAPTURED": "after patch_L316_3_ledger.py",
             "FP_L320": "after patch_L320_ledger.py", "FP_FINAL": "this patch's result"}
    at = next((s for s in states if g[s] == fp), None)
    if at is None:
        print("ERROR: %s matches none of the expected states (got %s); nothing written" % (LEDGER, fp)); return 1
    if at == "FP_FINAL":
        print("ERROR: this patch has already been applied; nothing written"); return 1
    print("base: ledger text matches %s%s" % (names[at], tag))
    steps = []
    try:
        for i in range(states.index(at), len(STAGES)):
            edits_name, after = STAGES[i]
            lf = apply(lf, g[edits_name], steps)
            if body_fp(lf) != g[after]:
                print("ERROR: stage %s did not reach its tested text; nothing written" % edits_name); return 1
    except ValueError as e:
        print(str(e) + "; nothing written"); return 1
    for s in steps:
        print("ok  %s" % s)
    for h in (b"#### [L-318]", b"#### [L-319]", b"#### [L-320]"):
        if lf.count(h) != 1:
            print("ERROR: %s appears %d times; nothing written" % (h.decode(), lf.count(h))); return 1
    if sum(1 for c in lf if c > 127):
        print("ERROR: non-ASCII in the result; nothing written"); return 1
    print("ok  result matches the tested ledger text (md5 %s, outside the index)" % FP_FINAL)
    data = lf.replace(b"\n", b"\r\n") if was_crlf else lf
    with open(fn, "wb") as f:
        f.write(data)
    print("stamped header: %s" % LEDGER)
    print("patch applied (%d bytes)" % len(data))
    print('next: run ledger_index.py -- expect "OK: 315 L-blocks parsed, no consistency problems."')
    return 0


if __name__ == "__main__":
    sys.exit(main())
