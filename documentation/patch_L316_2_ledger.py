"""patch_L316_2_ledger.py -- L-316 round 2 recorded; L-317's first phone
look recorded as not judged.

ORRERY repo (palomas_orrery). Built on orrery 204d1f5d at
https://github.com/tonylquintanilla/palomas_orrery ; records
patch_L316_2_cross_right.py against gallery 893261db at
https://github.com/tonylquintanilla/tonyquintanilla.github.io

Run: save this file in the orrery repo root (beside LEDGER_CONSOLIDATED.md),
open it in VS Code, click Run.  Or from a terminal in the repo root:
    python patch_L316_2_ledger.py

What it does, all-or-nothing:
  LEDGER_CONSOLIDATED.md
    - header stamp;
    - L-316: title now says where the cross goes; round 1's phone
      evidence and Tony's round-2 ruling; the round-2 build; new Gap;
    - L-317: round 1 on the phone did not judge the outlines -- the one
      white-outlined marker in view was under the cross.

Guard: the ledger's text outside the generated INDEX zone, line endings
normalised, must match 204d1f5d. Windows line endings are kept.

Permanent: the ledger text. Disposable: this script.
Success prints one 'ok' per edit and 'patch applied'. Any failure prints
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
FP_BASE = "194c47ac938e80b49c73a0f74ecf9f5b"
FP_FINAL = "1081d559ca3f3aca6d132ae62a57880b"

EDITS = [
("header stamp",
b"""(L-310 closed on Tony's Mode 5, its loose ends re-homed; L-316 and
L-317 opened from the same pass and built in the gallery), built on
08cf822d.
""",
b"""(L-310 closed on Tony's Mode 5, its loose ends re-homed; L-316 and
L-317 opened from the same pass and built in the gallery), built on
08cf822d.
Module updated: September 10, 2026 with Anthropic's Claude Opus 5
(L-316 round 2 on Tony's Mode 5: the title stays and the arrow cross
moves top right; L-317's outlines not yet judged), built on 204d1f5d.
"""),
("L-316 title",
b"""#### [L-316] On a portrait phone the arrow cross takes the in-frame title's place""",
b"""#### [L-316] On a portrait phone the arrow cross moves to the top-right corner"""),
("L-316 round 1, round 2, Gap and Ref",
b"""**Gap:** Tony's Mode 5. Portrait phone, both rooms: no title, the cross
top-centre, Home still works; rotate to landscape and back and both
follow. Desktop: title and cross exactly as before -- this also covers
L-310's desktop check. Then, at interactive-exhibit's next bump, its nav
cluster row names the arrows (L-310) and the portrait placement (this
item).
**Ref:** L-310, L-313 (recentering may add a control to the cluster),
L-267, L-289, L-317, `gallery/nav_cluster.js`, interactive.html
(`sunCrossOnTop`, `navPlaceCross`, `EARTH_INFO_HTML`),
`documentation/patch_L316_cross_and_borders.py` (gallery).
""",
b"""- **Round 1 on the phone, 2026-09-10 (screenshot, the Earth room zoomed
  to the inner core).** As built: no title, the cross top-centre, + and
  - top-left, clear of the drawer handle and the grid chip.
  [render-confirmed Mode 5 @ gallery `893261db`] But the outer core's
  info marker -- the one L-317 had just outlined in white -- was nowhere
  in the frame; by where its dots sat, it was under the cross. That is
  the trade-off offered before the ruling, now seen: a shell's marker
  sits at the top of the shell, so whichever shell nearly fills the view
  puts its marker at the top centre. Tony: "could we move the arrow cross
  to the right, restore the title. this would help to see the hovertext
  markers more clearly."
- **Round 2, built 2026-09-10** by `patch_L316_2_cross_right.py` in the
  gallery. The in-frame title is back on every screen, its layout line
  restored exactly. On a portrait phone -- 768 px wide or less, where the
  page's @media rule hides the mode bar that holds the top-right corner
  everywhere else -- the cross moves to a top-right holder, and rotating
  moves it back. `crossTop(on)` is renamed `crossRight(on)`,
  `sunCrossOnTop` is now `sunCrossRight`, and `sunSceneTitle` is gone.
  Desktop, landscape and the Explorer are unchanged. Round 1's date fix
  in `EARTH_INFO_HTML` stays: the title never carried a date. From the
  title's width in the round-1 screenshot (a 440-px-wide phone), the
  cross's up arrow should clear the title by about 40 px there and by
  roughly 7 to 14 px on a 393-px-wide phone, the Sun's title being the
  longer. [estimate; render-gated] Sandbox: the move, hide/show and a
  page without arrows on a stub DOM; the rule at five screen sizes; the
  page's inline JS parses; all four smoke tests pass.
**Gap:** Tony's Mode 5, round 2. Portrait phone, both rooms: the title
is back, the cross sits top right clear of it, and the marker at the top
of a zoomed shell is visible; rotate to landscape and back and the cross
follows. Desktop: unchanged -- this also covers L-310's desktop check.
Then, at interactive-exhibit's next bump, its nav cluster row names the
arrows (L-310) and the portrait placement (this item).
**Ref:** L-310, L-313 (recentering may add a control to the cluster),
L-267, L-289, L-317, `gallery/nav_cluster.js` (`crossRight`),
interactive.html (`sunCrossRight`, `navPlaceCross`, `EARTH_INFO_HTML`),
`documentation/patch_L316_cross_and_borders.py` and
`documentation/patch_L316_2_cross_right.py` (gallery).
"""),
("L-317 round 1 not judged",
b"""**Gap:** (1) Tony's Mode 5 on the phone, both rooms: the white outlines
read on the warm shells, and nothing else changed.""",
b"""- **Round 1 on the phone, 2026-09-10: not judged.** The one
  white-outlined marker in that view, the outer core's, sat under the
  top-centre arrow cross (L-316). L-316's round 2 moves the cross off it.
**Gap:** (1) Tony's Mode 5 on the phone, both rooms: the white outlines
read on the warm shells, and nothing else changed."""),
]


def body_fp(lf):
    if lf.count(INDEX_START) != 1 or lf.count(INDEX_END) != 1:
        return None
    a = lf.index(INDEX_START)
    b = lf.index(INDEX_END) + len(INDEX_END)
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest() if b > a else None


def apply(lf):
    for name, old, new in EDITS:
        n = lf.count(old)
        if n != 1:
            raise ValueError("ANCHOR FAIL: %s expected 1 match, got %d" % (name, n))
        lf = lf.replace(old, new)
    return lf


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
        print("ERROR: %s does not match 204d1f5d outside the index (got %s); nothing written" % (LEDGER, fp))
        return 1
    print("base: ledger text matches 204d1f5d%s" % (" [CRLF: Windows line endings; kept]" if was_crlf else ""))
    try:
        out = apply(lf)
    except ValueError as e:
        print(str(e) + "; nothing written"); return 1
    for name, _, _ in EDITS:
        print("ok  %s" % name)
    if sum(1 for c in out if c > 127):
        print("ERROR: non-ASCII in the result; nothing written"); return 1
    if body_fp(out) != FP_FINAL:
        print("ERROR: result does not match the tested result; nothing written"); return 1
    print("ok  result matches the tested ledger text (md5 %s, outside the index)" % FP_FINAL)
    data = out.replace(b"\n", b"\r\n") if was_crlf else out
    with open(fn, "wb") as f:
        f.write(data)
    print("stamped header: %s" % LEDGER)
    print("patch applied (%d bytes)" % len(data))
    print('next: run ledger_index.py -- expect "OK: 312 L-blocks parsed, no consistency problems."')
    return 0


if __name__ == "__main__":
    sys.exit(main())
