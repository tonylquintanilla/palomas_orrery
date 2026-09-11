"""patch_L316_ledger_borders.py -- L-310 closed on Tony's Mode 5; L-316 and
L-317 opened from the same pass. Replaces patch_L316_ledger.py, which must
not be run: its L-317 recorded the wrong fix.

ORRERY repo (palomas_orrery). Built on orrery 08cf822d at
https://github.com/tonylquintanilla/palomas_orrery ; records the gallery
build in patch_L316_cross_and_borders.py against gallery 6897c793 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io

Run: save this file in the orrery repo root (beside LEDGER_CONSOLIDATED.md),
open it in VS Code, click Run.  Or from a terminal in the repo root:
    python patch_L316_ledger_borders.py

What it does, all-or-nothing:
  LEDGER_CONSOLIDATED.md
    - header stamp;
    - L-310: DONE on Tony's Mode 5, its loose ends re-homed, and the block
      moved to the end of section C -- the place ledger_index.py would
      move it, so the indexer has nothing to fix afterwards;
    - L-316 opened: on a portrait phone the arrow cross takes the
      in-frame title's place (built in the gallery, Mode 5 pending);
    - L-317 opened: the interactive's info markers lacked the orrery's
      two-standards outline (gallery built, Mode 5 pending).

Guard: the ledger's text outside the generated INDEX zone, line endings
normalised, must match 08cf822d. Windows line endings are kept.

Permanent: the ledger text. Disposable: this script.
Success prints one 'ok' per step and 'patch applied'. Any failure prints
one ERROR / ANCHOR FAIL line and writes nothing.
Undo is Discard Changes in GitHub Desktop.

Then run ledger_index.py -- expect
"OK: 312 L-blocks parsed, no consistency problems."

Written September 10, 2026 with Anthropic's Claude Opus 5.
"""
import hashlib, os, sys

LEDGER = "LEDGER_CONSOLIDATED.md"
INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"
FP_BASE = "cb220402f781dd810ca4ae98f002782d"      # orrery 08cf822d, outside the index
FP_L310_BLOCK = "a51477aafde02710d8c8ec8542342cdf"  # L-310's block as it stands at 08cf822d
FP_FINAL = "194c47ac938e80b49c73a0f74ecf9f5b"    # the tested result, outside the index

STAMP_OLD = b"""(L-305 amended with the Jelinek 2012 read and Tony's Shue/Jelinek
ruling, corrected where it could not land as written; L-314 and L-315
opened; L-310's gallery push recorded), built on 5fea1795.
"""
STAMP_NEW = STAMP_OLD + b"""Module updated: September 10, 2026 with Anthropic's Claude Opus 5
(L-310 closed on Tony's Mode 5, its loose ends re-homed; L-316 and
L-317 opened from the same pass and built in the gallery), built on
08cf822d.
"""

L310_META_OLD = b"""<!-- L:310 status:OPEN upd:2026-09-10 section:A flag: rice:3/3/70/2 -->"""
L310_META_NEW = b"""<!-- L:310 status:DONE upd:2026-09-10 section:C flag: rice:3/3/70/2 -->"""

L310_TAIL_OLD = b"""**Gap:** Tony's Mode 5, phone and desktop, on the Earth room at full
zoom: the step feels right at high magnification, the arrow signs feel
right, and the cross clears the drawer handle and the title on a
portrait phone. Then DONE.
**Ref:** L-267 (nav cluster), L-289 (frame HUD, whose triad shows the
result of any camera move), L-291, `gallery/nav_cluster.js`,
interactive.html (`navHome`, `sunFrameOn`).
"""
L310_TAIL_NEW = b"""- **CLOSED 2026-09-10 on Tony's Mode 5.** Phone, the Earth room at full
  zoom, the three checks as asked: a tap moves a comfortable amount
  zoomed in, left and right turn the expected way, and the cross clears
  the drawer handle and the title. Tony: "all correct" (his screenshot
  of the Earth room's inner core, 2026-09-10). [render-confirmed Mode 5
  @ gallery `6897c793`] Desktop was not separately reported; it rides
  L-316's Mode 5, which checks that desktop is unchanged.
- **Loose ends re-homed before closing** (ledger-and-session-records
  1.11). The two suggestions from the same pass -> L-316 (the cross
  takes the in-frame title's place on a portrait phone) and L-317 (the
  interactive's markers lacked the orrery's two-standards outline).
  interactive.html's missing September 9 header line, found in passing
  by this item's handoff -> fixed by `patch_L316_cross_and_borders.py`
  from the archived L-291
  patches. interactive-exhibit's nav cluster row still names + / - /
  Home only -> L-316's Gap, at that skill's next bump. The step knobs
  (`NAV_STEP_BASE_DEG` 5, `NAV_STEP_SIGN` +1,
  `NAV_STEP_POLE_MARGIN_DEG` 2) stay as built -- struck, the pass needed
  no change [verified @ gallery `6897c793`]. Recentering stays L-313.
**Gap:** none.
**Ref:** L-267 (nav cluster), L-289 (frame HUD, whose triad shows the
result of any camera move), L-291, L-313, L-316, L-317,
`gallery/nav_cluster.js`, interactive.html (`navHome`, `sunFrameOn`),
`documentation/HANDOFF_L310_camera_step_20260910.md` (orrery).
"""

SECTION_C_END = b"""`documentation/patch_L303_1_cards_per_orientation.py` (gallery).
## D. RECONCILED LEDGER -- OPEN"""

NEW_ITEMS = b"""#### [L-316] On a portrait phone the arrow cross takes the in-frame title's place
<!-- L:316 status:OPEN upd:2026-09-10 section:A flag: rice:3/2/80/1 -->
- **Tony, 2026-09-10, from L-310's Mode 5 (chat, not his hand):**
  "replace the title inside the frame and put the arrow cross there. In
  this image the card title 'Earth' is sufficient." Offered the top-right
  corner as the alternative -- the top middle is where a zoomed object's
  top edge lands, and in his screenshot the down arrow would sit near the
  inner core's pole marker -- he chose **top-centre, where the title
  was**.
- **The rule as built.** A portrait phone is `innerHeight > innerWidth`
  with `innerWidth <= 768`, the width at which the page draws no Plotly
  mode bar, so no download button is left saving an image without its
  label. There, in the Sun and Earth rooms, the in-frame title is left
  empty and the cross, Home with it, moves to a top-centre holder; + and
  - stay top-left. Rotating redoes both (`onSunResize`). Desktop,
  landscape, a portrait tablet wider than 768 px and the Explorer are
  unchanged; the Explorer's title carries the scene date. The Sun room
  is included because the rooms share the chrome and its title repeats
  its header the same way.
- **Found building it: Earth's panel pointed at a date that was never
  there.** `EARTH_INFO_HTML` said "This scene is one moment -- the date
  in the title." The Earth title never carried a date; only the
  Explorer's does. The date is in two hovers, the Sun Direction's and
  the terminator's. The sentence now points at the Sun Direction's
  hover. [verified @ gallery `6897c793`] Whether the date should also
  have a visible place in the frame is open. **Tony-action (decide):**
  not urgent.
- **Built 2026-09-10** by `patch_L316_cross_and_borders.py` in the
  gallery, with L-317. `gallery/nav_cluster.js` gains `crossTop(on)`,
  which moves the cross element into a `.nav-cross-top` holder or back
  as the cluster's last child, so the corner layout that passed L-310's
  Mode 5 is unchanged. interactive.html gains `sunCrossOnTop`,
  `sunSceneTitle` and `navPlaceCross`. The same patch adds the missing
  September 9 header line (L-291 step 3; `patch_L291_9` and
  `patch_L291_11` both credit Claude Opus 5) and normalises the page's
  32 non-ASCII bytes. Sandbox: the move, hide/show and a page without
  arrows on a stub DOM; the rule at five screen sizes; the page's
  inline JS parses; all four smoke tests pass. [render-gated]
- **Note:** RICE 3/2/80/1 -> 4.8 proposed, not confirmed.
**Gap:** Tony's Mode 5. Portrait phone, both rooms: no title, the cross
top-centre, Home still works; rotate to landscape and back and both
follow. Desktop: title and cross exactly as before -- this also covers
L-310's desktop check. Then, at interactive-exhibit's next bump, its nav
cluster row names the arrows (L-310) and the portrait placement (this
item).
**Ref:** L-310, L-313 (recentering may add a control to the cluster),
L-267, L-289, L-317, `gallery/nav_cluster.js`, interactive.html
(`sunCrossOnTop`, `navPlaceCross`, `EARTH_INFO_HTML`),
`documentation/patch_L316_cross_and_borders.py` (gallery).

#### [L-317] The interactive's info markers lacked the orrery's two-standards outline
<!-- L:317 status:OPEN upd:2026-09-10 section:A flag: rice:4/2/80/1 -->
- **Tony, 2026-09-10, from L-310's Mode 5 (chat, not his hand):** "make
  the hovertext marker cross more prominent. They get buried in the
  shell dot patterns."
- **A first build went the wrong way and was withdrawn.** It filled every
  gallery marker white at size 14 and recorded the desktop orrery as
  having the same problem. Tony: "on the orrery side we already have
  solutions. It was the interactive that did not have them." Asked about
  the inner core: "There are different borders depending on the
  predominant hue. White for darks and red for brights."
- **The orrery's solution, read at `08cf822d`.** Tony's two-standards
  rule (Mode 5, 2026-05-28/29;
  `documentation/HANDOFF_shell_consolidation_stage_3_v15.md`): the cross
  keeps its shell's colour at size 8, and the outline is red, except
  WHITE on saturated warm fills -- the oranges, the pink-reds, the dense
  reds -- where red is lost. The pale peach and golden ends of that ramp
  revert to red, because white is lost there instead; Earth's inner core,
  rgb(255, 180, 140), is that peach and was reverted in the same round.
  Judged per shell by eye, "NOT an RGB threshold", so it is declared per
  shell: 18 `info_border: 'white'` sites in `shell_configs.py`, and set
  by hand where a builder is not config-driven, Earth's inner radiation
  belt among them (`earth_visualization_shells.py`).
  `orrery_rendering.create_info_marker` takes `border_color`, default
  red. [verified @ `08cf822d`]
- **What the interactive lacked.** Its served rows carry the orrery's
  shell colours exactly, but not the outline flags, and its marker
  builder always drew red. So in the two rooms the Roche limit, the outer
  core, both mantles and the inner belt had red crosses on red and orange
  dots.
- **Built 2026-09-10** by `patch_L316_cross_and_borders.py` in the
  gallery, with L-316. `data/objects_config.json`: `info_border: "white"`
  on the four flagged shells these rooms draw (Sun: Roche Limit; Earth:
  Outer Core, Lower Mantle, Upper Mantle) and `info_borders: ["white",
  "red"]` on Earth's belt pair; the patch refuses to write unless the
  edited config carries exactly that roster. `gallery/feature_renderers.js`:
  `infoMarker()` takes the served outline, red when absent -- the orrery
  factory's shape -- and every renderer that draws from a served row
  passes it. `gallery/earth_geometry.js` is untouched: its axis, Sun,
  terminator and Moon markers are not shells and stay red.
  `documentation/smoke_sun_shells.js` and `smoke_earth_geometry.js` each
  gain one check against the LIVE config (now 25 and 31): exactly the
  flagged markers are white. Both were made to fail -- a flag dropped, a
  flag added, the belt pair swapped, the renderer ignoring the flag. The
  cache builder's suite passes 167 of 167 on the edited config.
  [verified in the sandbox; render-gated]
- **Two things this does not do, named.** The inner core in Tony's
  screenshot keeps its red outline, as in the orrery; correct under the
  rule, and if it still reads as buried on the phone that is a new Mode 5
  call, not this port. And nothing checks that the gallery's roster keeps
  matching `shell_configs.py`: the live store-drift run follows constants,
  not declared drawing choices, and the colours already have that
  exposure. The roster is pinned in the patch and the two smoke checks as
  of orrery `08cf822d`.
- **Why the interactive missed it.** The rule lives in the orrery's code
  comments, `shell_configs.py` and a May handoff. orrery-coding-conventions
  -- the skill a session loads for markers -- never states it, and its
  Single Info Marker Pattern example still shows the style
  `create_info_marker`'s docstring records as retired in May 2026 (size
  6, white border, opacity 0.9). The first build here missed it the same
  way.
- **Note:** RICE 4/2/80/1 -> 6.4 proposed, not confirmed.
**Gap:** (1) Tony's Mode 5 on the phone, both rooms: the white outlines
read on the warm shells, and nothing else changed. (2) At
orrery-coding-conventions' next bump: the two-standards rule, and the
example corrected to `create_info_marker`.
**Ref:** L-310, L-316, `data/objects_config.json` and
`gallery/feature_renderers.js` (gallery), `shell_configs.py`,
`orrery_rendering.py` (`create_info_marker`),
`documentation/HANDOFF_shell_consolidation_stage_3_v15.md` and
`documentation/border_refinement_test_protocol.md` (orrery),
skills/orrery-coding-conventions/SKILL.md.

"""
NEW_ITEMS_ANCHOR = b"""#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery"""


def body_fp(lf):
    if lf.count(INDEX_START) != 1 or lf.count(INDEX_END) != 1:
        return None
    a = lf.index(INDEX_START)
    b = lf.index(INDEX_END) + len(INDEX_END)
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest() if b > a else None


def apply(lf):
    """All edits on LF text. Returns (text, [step names]) or raises."""
    steps = []
    def one(old, new, name):
        nonlocal lf
        n = lf.count(old)
        if n != 1:
            raise ValueError("ANCHOR FAIL: %s expected 1 match, got %d" % (name, n))
        lf = lf.replace(old, new)
        steps.append(name)

    one(STAMP_OLD, STAMP_NEW, "header stamp")

    # L-310: cut the block out of section A, exactly
    head = b"#### [L-310] Finer camera control"
    if lf.count(head) != 1:
        raise ValueError("ANCHOR FAIL: L-310 header expected 1 match, got %d" % lf.count(head))
    i = lf.index(head)
    j = lf.find(b"\n#### [", i + len(head))
    if j < 0:
        raise ValueError("ANCHOR FAIL: no block after L-310")
    j += 1
    block = lf[i:j]
    if hashlib.md5(block).hexdigest() != FP_L310_BLOCK:
        raise ValueError("ERROR: L-310's block is not the one at 08cf822d")
    lf = lf[:i] + lf[j:]
    for old, new, name in ((L310_META_OLD, L310_META_NEW, "L-310 status DONE, section C"),
                           (L310_TAIL_OLD, L310_TAIL_NEW, "L-310 closing record")):
        if block.count(old) != 1:
            raise ValueError("ANCHOR FAIL: %s expected 1 match in L-310's block" % name)
        block = block.replace(old, new)
        steps.append(name)
    block = block.rstrip(b"\n") + b"\n"
    one(SECTION_C_END,
        b"`documentation/patch_L303_1_cards_per_orientation.py` (gallery).\n\n" + block +
        b"## D. RECONCILED LEDGER -- OPEN",
        "L-310 moved to the end of section C")

    one(NEW_ITEMS_ANCHOR, NEW_ITEMS + NEW_ITEMS_ANCHOR, "L-316 and L-317 opened")
    return lf, steps


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
    if fp == FP_FINAL:
        print("ERROR: this patch has already been applied; nothing written"); return 1
    if fp != FP_BASE:
        print("ERROR: %s does not match 08cf822d outside the index (got %s); nothing written" % (LEDGER, fp))
        print("If you have ledger edits since 08cf822d, stop and say so; otherwise Discard Changes and Run again.")
        return 1
    print("base: ledger text matches 08cf822d%s" % (" [CRLF: Windows line endings; kept]" if was_crlf else ""))
    try:
        lf, steps = apply(lf)
    except ValueError as e:
        print(str(e) + "; nothing written"); return 1
    for s in steps:
        print("ok  %s" % s)
    for h in (b"#### [L-310]", b"#### [L-316]", b"#### [L-317]"):
        if lf.count(h) != 1:
            print("ERROR: %s appears %d times; nothing written" % (h.decode(), lf.count(h))); return 1
    bad = sum(1 for c in lf if c > 127)
    if bad:
        print("ERROR: %d non-ASCII byte(s) in the result; nothing written" % bad); return 1
    if body_fp(lf) != FP_FINAL:
        print("ERROR: result does not match the tested result; nothing written"); return 1
    print("ok  result matches the tested ledger text (md5 %s, outside the index)" % FP_FINAL)
    out = lf.replace(b"\n", b"\r\n") if was_crlf else lf
    with open(fn, "wb") as f:
        f.write(out)
    print("stamped header: %s" % LEDGER)
    print("patch applied (%d bytes)" % len(out))
    print('next: run ledger_index.py -- expect "OK: 312 L-blocks parsed, no consistency problems."')
    return 0


if __name__ == "__main__":
    sys.exit(main())
