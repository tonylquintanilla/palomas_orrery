"""
patch_L291_14_ledger_mode5_close_20260909.py -- ledger: L-291 Mode 5 passed, L-168 DONE, L-310 opened

Built on orrery f53273c3db98150c169cd9035ccaaf7590ac8c4c
at https://github.com/tonylquintanilla/palomas_orrery (main); gallery at
e22cde126f49510f98e4ae4112e8ec8137c9d8aa, where the three Mode 5 rounds
landed.

Edits LEDGER_CONSOLIDATED.md only, five hunks: L-291 to PENDING-GATE
with the three Mode 5 rounds recorded and the Gap reduced to the Studio
card; L-168 to DONE (the propagate_marker fix, cross-checked by name,
Gap: none -- move to section C); L-310 opened (directional camera steps,
Tony's question, a design round). Index zone untouched -- run
ledger_index.py after this.

HOW TO RUN: save to the orrery repo root, Run in VS Code, then run
ledger_index.py, commit, push, report the SHA.

GUARDS: md5 (LF) checked against f53273c3; each hunk matches once;
ASCII-only; refuses to run twice; writes nothing on any failure.

Written September 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "LEDGER_CONSOLIDATED.md"
EXPECT_MD5 = 'e1254be3833dc608cd43673b1b04d9e4'
EDITS = [('<!-- L:291 status:OPEN upd:2026-09-09 section:A flag: rice:4/4/80/3 -->', '<!-- L:291 status:PENDING-GATE upd:2026-09-09 section:A flag: rice:4/4/80/3 -->'), ('**Gap:** STEPS 4-8. Tony (do): run the patch, runner (6 of 6), push,\n`--live`, then Mode 5 on the phone at `interactive.html?exhibit=earth`\n-- conditions: arrival shows the eight shells, gold axis and yellow Sun\nline with the grid chip reading in AU and km; the drawer lists the Moon,\nterminator, GEO, belts, geocorona, Hill sphere, and one italic\n"not yet drawn" row; tap GEO and it lies in the equator ring\'s plane;\ntap the Moon and the brighter arc sits on the faint ellipse around the\nmarker; every hover ends in a Source line. Then the Studio card. The\nmagnetosphere is L-305. Closes on Tony\'s eyes.\n', '- **MODE 5, 2026-09-09, three rounds, all on the served page\n  [render-confirmed Mode 5 @ gallery `e22cde12`].** Step 3 patch ran on\n  `23054535` -> `97ed2012`; `--live` byte-identical, 8 files. Phone\n  matches desktop (Tony). Round 1 (`patch_L291_11`, -> `bac5a5ee`): the\n  terminator\'s marker read as detached -- the Sun line now starts at\n  Earth\'s centre through the circle\'s middle with a subsolar dot on the\n  crust, the terminator\'s marker sits ON the circle; frame axes width 3\n  -> 6 (both rooms); the orrery\'s spin arcs with cone heads at both pole\n  tips, prograde, sense cited (Archinal 2018). Round 2 (`patch_L291_12`,\n  -> `da57d095`): the arc made white and the ellipse faded by rgba --\n  correct changes aimed at the WRONG cause; kept. Round 3\n  (`patch_L291_13`, -> `e22cde12`): Tony read the Moon\'s woven band as\n  "points too far apart in time", which it was -- L-168, fixed at source\n  (see there). GEO confirmed in the equator\'s plane; the Moon\'s arc a\n  clean quarter-orbit with the marker on it. Tony: "looks right."\n- **What the three rounds teach, one sentence each.** Measure the\n  geometry before theorising about the renderer (round 2 guessed at\n  Plotly; one `atan2` sweep in round 3 gave 8,406 degrees). A hover\n  marker belongs on the thing it describes. The frame must read as\n  frame.\n- **Camera control (Tony\'s question, round 1):** Plotly has no drag\n  sensitivity; directional step buttons on the nav cluster are the\n  practical answer. Opened as L-310, shared chrome, a design round of\n  its own.\n**Gap:** STEP 7 -- the Studio card via New Interactive Card (the picker\nreads the EXHIBITS table now; expect `?exhibit=earth`), placed in the\neditor; then L-291 closes. Tony-action (do). L-305 (magnetosphere) and\nL-310 (camera steps) are their own items; L-292 (serving the rotation\nperiod) is the small orrery patch the axis hover is waiting for.\n'), ('<!-- L:168 status:OPEN upd:2026-07-28 section:W.Active flag: rice:3/3/80/2 -->', '<!-- L:168 status:DONE upd:2026-09-09 section:W.Active flag: rice:3/3/80/2 -->'), ('**Gap:** land the `propagate_marker` fix (use served `n`, drop solar-GM\nderivation, guard no-`n`) BEFORE or WITH the L-154 JS feature-rendering\nlayer, so the first Jupiter/Saturn/moon render carries correct marker\npositions; re-run Earth Mode-5 as the no-regression gate.\n', "- **FIXED 2026-09-09, gallery `e22cde12`** (`patch_L291_13_L168_moon_mean_motion`),\n  exactly as designed above: `propagate_marker` reads `n_deg_per_day`\n  from the served block; a block without one raises a plain ValueError\n  naming centre and `a` -- never a quiet solar-GM fallback. `K_GAUSS`\n  stays defined for importers, unused for mean motion. [verified\n  @e22cde12; render-confirmed Mode 5]\n- **The trigger was the one predicted.** The Earth room (L-291) is the\n  first planetocentric render. Its trusted arc -- 121 points across the\n  Moon's 6.84-day served window -- swept 8,406 degrees, 23 orbits, and\n  drew as a lattice of 70-degree chords. Tony read it on sight as points\n  too far apart in time. The Moon's MARKER was wrong too, between 00:00\n  UTC (the page's epoch) and the ~17:40 UTC nightly, when the elements\n  were a day old: 132 rad/day put it anywhere on the orbit; at the\n  fixture's own epoch it happened to be right, which is why no check\n  caught it.\n- **Cross-checked against Horizons' `as_of_today` in the live cache:**\n  Earth 8.8e-12, Moon 2.3e-10, Io 2.6e-9, Titan 2.0e-10 of r. Halley\n  4.96e-3 with the old formula and the new -- unrelated, its elements\n  are pinned at the 1986 perihelion (horizons-orbital-mechanics, comet\n  record pinning). Artifact 1 pin holds: 5 verdicts and T3's feature\n  set unchanged. The Earth smoke pins the arc's sweep at 60-120 degrees;\n  the old arc fails it by a factor of 70.\n- **Not done, recorded:** a Python-side `as_of_today` cross-check for a\n  planetocentric body (the four numbers above, as a test). T1 checks\n  Earth only. Add when `test_artifact1_earth.py` is next open; the pin\n  compares its verdicts by name, so a new verdict is a pin change.\n**Gap:** none -- move to section C.\n"), ('(`EXHIBITS`, `EX`), `tools/json_converter.py::live_scene_urls`.\n\n#### [L-278]', '(`EXHIBITS`, `EX`), `tools/json_converter.py::live_scene_urls`.\n\n#### [L-310] Finer camera control in the exhibit rooms: directional step buttons on the nav cluster\n<!-- L:310 status:OPEN upd:2026-09-09 section:A flag: rice:3/3/70/2 -->\n- **Tony, 2026-09-09, Mode 5 of the Earth room:** "the mouse control is\n  rough for details. can we activate finer control? there is the\n  directional control buttons as an option."\n- **What is true of the mechanism.** Plotly\'s 3D camera drag has no\n  sensitivity setting; a small feature at Earth\'s scale moves out of\n  view in one twitch. The nav cluster (L-267 step 7, `nav_cluster.js`)\n  already steps the FRAME with +/- through `Plotly.relayout`; a camera\n  step is the same move on `scene.camera.eye`, rotated about the up\n  vector (yaw) or the eye\'s horizontal (pitch) by a fixed angle.\n- **Design questions for the round, not settled here:** step size (5\n  degrees? 15?), whether the buttons appear in both rooms and the\n  Explorer (the cluster is shared, L-267), touch layout on a portrait\n  phone beside the drawer handle, and whether a long press repeats.\n  Shared chrome: a design round first, zero code, then one patch.\n**Gap:** design round with Tony; then build. Not blocking L-291.\n**Ref:** L-267 (nav cluster), L-289 (frame HUD, whose triad shows the\nresult of any camera move), L-291, `gallery/nav_cluster.js`,\ninteractive.html (`navHome`, `sunFrameOn`).\n\n#### [L-278]')]


def main():
    raw = TARGET.read_bytes().replace(b"\r\n", b"\n")
    got = hashlib.md5(raw).hexdigest()
    if got != EXPECT_MD5:
        print("STOP: LEDGER_CONSOLIDATED.md md5 (LF) is %s, expected %s (at f53273c3)." % (got, EXPECT_MD5))
        print("      Either this patch already ran or the ledger moved. Nothing written.")
        return 1
    t = raw.decode("utf-8")
    for i, (old, new) in enumerate(EDITS, 1):
        c = t.count(old)
        if c != 1:
            print("STOP: hunk %d matched %d time(s), expected 1. Nothing written." % (i, c))
            return 1
    for old, new in sorted(EDITS, key=lambda e: -t.index(e[0])):
        new.encode("ascii")
        t = t.replace(old, new)
    TARGET.write_bytes(t.encode("utf-8"))
    print("ok  LEDGER_CONSOLIDATED.md: L-291 PENDING-GATE (Mode 5 passed), L-168 DONE, L-310 opened")
    print("Next: ledger_index.py, commit, push, report the SHA.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
