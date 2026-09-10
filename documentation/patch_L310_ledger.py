"""patch_L310_ledger.py -- L-310 design ruled and built; L-313 (recenter) opened.

ORRERY repo (palomas_orrery). Built on orrery 5fea1795; the gallery
build it records is patch_L310_camera_step.py against gallery 57fd93c6.

Run: save this file in the orrery repo root (beside LEDGER_CONSOLIDATED.md),
open it in VS Code, click Run.  Or from a terminal in the repo root:
    python patch_L310_ledger.py

What it does, all-or-nothing:
  LEDGER_CONSOLIDATED.md  -- L-310 gains the 2026-09-10 design ruling, what
                             was settled with it, the split-off of recentering,
                             the build record and a Mode 5 Gap; L-313 opened
                             (recenter the camera on a chosen feature); header
                             stamp. Then run ledger_index.py to rebuild the
                             index zone -- this script does not touch it.
  documentation/HANDOFF_L310_camera_step_20260910.md  -- written new.

Permanent: the ledger text and the handoff. Disposable: this script.
Success prints one 'ok' per edit and 'patch applied'. Any failure prints one
ERROR / ANCHOR FAIL line and writes nothing.

Written September 10, 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib, os, sys

LEDGER = "LEDGER_CONSOLIDATED.md"
LEDGER_MD5 = "94a40a25a85898d13556b5db461408ef"
HANDOFF = os.path.join("documentation", "HANDOFF_L310_camera_step_20260910.md")

LEDGER_EDITS = [
# 1. header stamp (inserted above the Sept 10 Opus 5 stamp)
(b"""Module updated: September 10, 2026 with Anthropic's Claude Opus 5""",
b"""Module updated: September 10, 2026 with Anthropic's Claude Fable 5.1
(L-310 design ruled and built; L-313 opened), built on 5fea1795.
Module updated: September 10, 2026 with Anthropic's Claude Opus 5"""),
# 2. L-310 body and Gap
(b"""**Gap:** design round with Tony; then build. Not blocking L-291.
""",
b"""- **Design round, 2026-09-10, on the phone, and the ruling.** Tony:
  coarse sweep and rotation are not the need; the hand and the mouse
  give those. "In full zoom both sweep and rotate are hard to control
  precisely. It's like moving a telescope on full magnification by
  hand." So: no hold-to-repeat, and no fixed angle. The step SCALES
  WITH MAGNIFICATION. A tap turns the camera by a base angle (5
  degrees, a Mode 5 knob) times the ratio of the live eye distance to
  the arrival eye distance, so a wheel-dollied view gets a
  proportionally smaller step and a tap always moves about the same
  slice of the screen -- the slow-motion knob. Frame zoom (+/-) does
  not change the eye distance, and a fixed angle already sweeps a
  fixed slice there, so the two zooms compose.
- **Settled with it.** Left/right yaw about the up vector; up/down
  pitch about the eye's horizontal, refused within 2 degrees of the
  poles. Arrows draw only where the page passes step handlers, so a
  2D page later gets the three buttons unchanged (the L-285 lesson:
  one button, one meaning). Layout is a cross with Home at the centre,
  under + and -. The step reads the live camera through
  `sunLiveCamera` (L-289), so it is right after a touch rotation. The
  sign convention and the base angle are Mode 5 knobs
  (`NAV_STEP_SIGN`, `NAV_STEP_BASE_DEG`).
- **Recentering was raised and split off.** Rotation orbits the scene
  centre, so an off-centre feature swings out of view however fine
  the step; the orrery already has a recenter for its comet-detail
  views. Tony: capture it as its own item. L-313.
- **Built 2026-09-10** by `patch_L310_camera_step.py` in the gallery
  repo (`gallery/nav_cluster.js`, `interactive.html`) against gallery
  `57fd93c6`; syntax-checked and the cluster's two layouts exercised on
  a stub DOM in the sandbox. [render-gated]
**Gap:** Tony's Mode 5, phone and desktop, on the Earth room at full
zoom: the step feels right at high magnification, the arrow signs feel
right, and the cross clears the drawer handle and the title on a
portrait phone. Then DONE.
"""),
# 3. L-313 opened, above L-311
(b"""#### [L-311] Earth's rotation period and obliquity are not served, so the axis hover names neither""",
b"""#### [L-313] Recenter the camera on a chosen feature in the exhibit rooms
<!-- L:313 status:OPEN upd:2026-09-10 section:A flag: rice:3/3/60/3 -->
- **Opened 2026-09-10, split from L-310's design round.** A camera
  step, however fine, orbits the scene centre; a feature off that
  centre (the Moon in the Earth room) swings across the screen and
  out on any rotation. A telescope mount has the same limit, which is
  why the object is centred in the finder before high power. The fix
  is to move `scene.camera.center` onto the feature so the arrows and
  the mouse both turn about it.
- **Prior art, from Tony:** the orrery already recenters for
  high-zoom views such as comet details. Read that mechanism first
  (which module, and how it picks the point) before designing the
  room's version; the module is not yet named here.
- **Questions for the design round:** how the point is chosen (a tap
  on a plotted point through Plotly's click event; what a tap on empty
  space does); where the control lives (a cluster button, or a gesture
  with no button); how the frame HUD shows that the pivot moved
  (L-289's triad follows the camera eye, not the centre); and that
  Home restores the arrival centre as it restores the eye.
- **Note:** RICE 3/3/60/3 -> 1.8 proposed, not confirmed.
**Gap:** design round, zero code, after L-310 passes Mode 5. Then one
patch, shared chrome.
**Ref:** L-310 (the arrows), L-267 (the cluster), L-289 (the HUD),
`gallery/nav_cluster.js`, interactive.html (`navCameraStep`,
`navHome`), the orrery's recenter.

#### [L-311] Earth's rotation period and obliquity are not served, so the axis hover names neither"""),
]

HANDOFF_TEXT = """# L-310 camera steps built; L-313 (recenter) opened

Built on orrery `5fea17955d5f2d57f8426da8446d7d1b76f7274f`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `57fd93c62606cb91ed56050885dd7ce6f3852859`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
Pushed at: orrery -- the commit carrying `patch_L310_ledger.py`;
gallery -- the commit carrying `patch_L310_camera_step.py` (the next
session reads both from `git log`).

Tony Quintanilla, PE | Claude Fable 5.1 | 2026-09-10
Type: DESIGN + BUILD (one design round from the phone; one gallery
patch; ledger). Protocol v3.56. Handles: L-310, L-313.

**Supersedes** item 1 of the OPEN list in `HANDOFF_earth_close_20260910.md`.

## STEP 0 -- Gates for the next session

- The skill obligation from the Earth close handoff was discharged this
  session: interactive-exhibit loaded 1.1, ledger-and-session-records
  1.11, both matching the manifest. Nothing travels from this session;
  no skill was bumped.
- `git ls-remote` both repos. Orrery one commit past `5fea1795`;
  gallery one commit past `57fd93c6`, or two if the spent patch was
  moved separately.

## WHAT HAPPENED

- **The design round reframed the item.** Tony: coarse sweep is not
  the need; fine control at full magnification is, like a telescope
  by hand at high power. So the step scales with the eye distance
  instead of sitting at a fixed angle, and there is no hold-to-repeat.
- **Recentering surfaced and was split off** as L-313. Rotation
  orbits the scene centre, so a fine step still swings an off-centre
  feature away. The orrery has a recenter for comet detail views;
  that is the prior art.
- **Built** `navCameraStep` in interactive.html and optional arrow
  buttons in `gallery/nav_cluster.js` (a cross with Home at the
  centre, drawn only when a page passes step handlers). Sandbox:
  patch applied on a throwaway copy, re-run aborted on the
  fingerprint, `node --check` on both files, stub-DOM mount gave 7
  buttons with steps and 3 without, rotation math checked by hand.
  Not rendered: Mode 5 is the gate.

## FOUND IN PASSING, NOT FIXED

- interactive.html's header stamp stopped at September 6. The Earth
  step 3 edits of 2026-09-09 (the `EXHIBITS` table, L-291) carry no
  Updated line. This patch adds its own line; the missing one needs
  the wording from the session that made the change.

## OPEN, IN ORDER

1. **L-310 Mode 5** on the Earth room at full zoom, phone and desktop.
   Three knobs in interactive.html if it is off: `NAV_STEP_BASE_DEG`
   (5), `NAV_STEP_SIGN` (+1), `NAV_STEP_POLE_MARGIN_DEG` (2). If the
   cross collides with the drawer handle on a portrait phone, that is
   a layout change in `nav_cluster.js`, not a knob.
2. **L-311**, **L-305**, then the plan's order, as in the Earth close
   handoff.
3. **L-313** design round after L-310 closes; read the orrery's
   recenter first.

## TONY-ACTION ROLLUP

1. **(do)** Gallery repo root: run `patch_L310_camera_step.py` (Run).
2. **(do)** Orrery repo root: run `patch_L310_ledger.py` (Run), then
   `ledger_index.py` (Run).
3. **(do)** Move both spent patches into each repo's `documentation/`.
4. **(do)** GitHub Desktop: commit and push both repos; report both
   SHAs.
5. **(decide)** Mode 5 on the phone and desktop; say what the arrows
   feel like at full zoom. L-310 closes on your word.

Written September 2026 with Anthropic's Claude Fable 5.1.
"""


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(root, LEDGER)
    if not os.path.exists(fn):
        print("ERROR: not found: %s (run from the orrery repo root)" % fn); return 1
    hf = os.path.join(root, HANDOFF)
    if os.path.exists(hf):
        print("ERROR: %s already exists -- already patched; nothing written" % HANDOFF); return 1
    with open(fn, "rb") as f:
        content = f.read()
    got = hashlib.md5(content).hexdigest()
    if got != LEDGER_MD5:
        print("ERROR: %s fingerprint %s, expected %s -- wrong base or already patched; nothing written"
              % (LEDGER, got, LEDGER_MD5)); return 1
    for i, (old, new) in enumerate(LEDGER_EDITS, 1):
        n = content.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s edit %d expected 1 match, got %d: %r" % (LEDGER, i, n, old[:60]))
            return 1
        content = content.replace(old, new)
        print("ok  %s edit %d" % (LEDGER, i))
    with open(fn, "wb") as f:
        f.write(content)
    print("stamped header: %s" % LEDGER)
    with open(hf, "wb") as f:
        f.write(HANDOFF_TEXT.replace("\r\n", "\n").encode("ascii"))
    print("ok  wrote %s" % HANDOFF)
    print("patch applied (%d bytes ledger; handoff %d bytes)" % (len(content), len(HANDOFF_TEXT)))
    print("next: run ledger_index.py to rebuild the index zone")
    return 0


if __name__ == "__main__":
    sys.exit(main())
