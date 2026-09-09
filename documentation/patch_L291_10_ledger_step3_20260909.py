"""
patch_L291_10_ledger_step3_20260909.py -- ledger: L-303 built, L-291 step 3 built, L-309 opened

Built on orrery d39cf27c76dc933a3ee3f8d56fd159e877dcd26d
at https://github.com/tonylquintanilla/palomas_orrery (main); gallery at
23054535 for L-303's build and the base of L-291's step-3 patch.

Edits LEDGER_CONSOLIDATED.md only, five hunks: L-303 to PENDING-GATE
with the build named and the migration counted by name; L-291 gains the
step-3 build record, the three handoff corrections, and a Gap that is
the Mode 5 conditions; L-309 opens as DEFERRED (the sun* chrome names,
with the reason and the trigger). Index zone untouched -- run
ledger_index.py after this.

HOW TO RUN: save to the orrery repo root, Run in VS Code, then run
ledger_index.py, commit, push, report the SHA.

GUARDS: md5 (LF) checked against d39cf27c; each hunk matches once;
ASCII-only; refuses to run twice; writes nothing on any failure.

Written September 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "LEDGER_CONSOLIDATED.md"
EXPECT_MD5 = 'ae83aeac3b5b173c4bf5fee4cea74a7b'
EDITS = [('<!-- L:303 status:OPEN upd:2026-09-08 section:A flag: rice:4/4/80/3 -->', '<!-- L:303 status:PENDING-GATE upd:2026-09-09 section:A flag: rice:4/4/80/3 -->'), ("**Gap:** build it -- the converter's inverted pairing and sibling\nstamp; the one viewer rule; the split migration of L-287's 38 pairs\nplus L-301's 3. One known loss to accept: two of L-301's three\nmerges had titles typed differently between L and P and the\nlandscape title survived, so those portrait titles are gone and get\nretyped. Tony-action (do) at that point, not now.\n**Ref:** L-287, L-301, L-286, L-307, L-308, `tools/json_converter.py`,\n`tools/gallery_editor.py`, index.html.\n", '- **Built 2026-09-08, gallery `23054535`** (`patch_L303_1_cards_per_orientation.py`,\n  Tony ran it, runner 5 of 5). The converter keeps L-301\'s pairing\n  detection and inverts the action: a matching file becomes a separate\n  card stamped `"sibling": <the other id>` on both, inserted right\n  after its partner, inheriting its room, description and sources. The\n  viewer rule in Tony\'s wording: on a phone (under 768 px, the sweep\'s\n  own test) hide a landscape card that has a portrait sibling. Three\n  choices not in the ruling, stated for striking: the rule hides only\n  when the sibling is itself SERVED (a portrait in Storage or deleted\n  leaves the landscape showing); the lobby\'s Featured strip shows one\n  of a featured pair; a card with a sibling shows its shape after its\n  size so two same-title cards read apart on the desktop. A deep link\n  to a hidden card on a phone opens its sibling. `sweep_report.py`\n  gains the class "hidden on the phone (portrait sibling)".\n- **The migration, named.** 104 cards became 144: 40 splits, not 41 --\n  `keeling_curve_co2_concentration` listed the SAME file in both slots\n  and collapsed to one landscape card, no sibling. The phone serves 104\n  as before; Featured stays 7 on both. Portrait ids from the portrait\n  filenames; the one clash rule (`_portrait` suffix) did not fire.\n- **Not done, recorded:** `gallery_editor.py` can still put two files on\n  one card, and its Copy carries a `sibling` stamp onto the copy. The\n  viewer tolerates both (a dangling sibling is ignored). A guard in the\n  editor or a sweep_report class when a session has that file open.\n**Gap:** Mode 5 on the phone -- one card per figure, the portrait file;\non the desktop two cards side by side tagged 16:9 and 9:16. Tony-action\n(do): retype the portrait title on\n`artemis_ii_20260402-0411_mission_moon_center2_mobile` and\n`maps_disintegration_20260403_07_structures_mobile` in the editor.\nCloses on Tony\'s eyes.\n**Ref:** L-287, L-301, L-286, L-307, L-308, `tools/json_converter.py`,\n`tools/gallery_editor.py`, `tools/sweep_report.py`, index.html,\n`documentation/patch_L303_1_cards_per_orientation.py` (gallery).\n'), ('<!-- L:291 status:OPEN upd:2026-09-08 section:A flag: rice:4/4/80/3 -->', '<!-- L:291 status:OPEN upd:2026-09-09 section:A flag: rice:4/4/80/3 -->'), ('**Gap:** STEP 3, six items -- the `EXHIBIT === "earth"` branch in\n`interactive.html` (driver spec: objects Earth + Moon, center Earth,\nhalf-range floor 6.155e-5 AU; eight shells lit on arrival; axis,\nequator plane, Sun direction on), the GEO ring renderer, the\nterminator as geometry, the Moon\'s orbit with the trust-window arc,\nthe frozen-epoch hovers, the `sun*` chrome by parameter, i-panel\ncopy with sources. The magnetosphere renderer is NOT in this step;\nsee L-305. Then steps 4-8. Closes on Tony\'s eyes.\n', '- **STEP 3 BUILT 2026-09-09** (`patch_L291_9_earth_step3_20260909.py`,\n  gallery, on `23054535`; not yet run at the time of this entry). All\n  six items. `?exhibit=earth` is a second row in an EXHIBITS table the\n  chrome now reads (title, arrival half-range, Python driver, scene\n  composition); the sun* function names stay, see L-309. New module\n  `gallery/earth_geometry.js`: rotation axis and equator from the\n  served pole; the Sun direction from Earth\'s Horizons elements in the\n  cache, propagated by the assembler; the terminator as a great circle\n  perpendicular to it with a subsolar marker, no lighting model; the\n  Moon\'s trusted arc from the served trust window through the same\n  solver that places the Moon. It composes the room and applies the\n  arrival policy. The GEO ring draws as shape `equatorial_ring` in the\n  shell-set renderer, tilted by the pole. The served source string\n  rides in trace meta and the i-panel shows it under the link. The\n  drawer lists the magnetosphere as "not yet drawn" (its two served\n  member names), a row that is not a button. Studio\'s card picker\n  reads the EXHIBITS table. New gating runner row "Earth scene\n  geometry" (26 checks on the driver\'s real output); 6 of 6 here.\n- **Three things the handoff had wrong, found by RUNNING the assembler\n  here, not by reading:** (1) "objects Earth and Moon, center Earth" is\n  rejected by the resolver -- Earth is stored relative to the Sun; the\n  room is objects `["moon"]`, center `"earth"`, and Earth\'s shells\n  arrive by the centre-features path (L-234). (2) The Moon\'s served\n  trust window is 3.40 days, not the 3.37 the handoff typed; the arc\n  reads the record, so no number is in code. (3) The inner radiation\n  belt at 1.5 R_earth drew LIT on arrival and set the frame: the belt\n  renderer ignored the half-range. Fixed generically (belts beyond the\n  frame go to the drawer, as shells do); Jupiter\'s belts inherit it.\n  Two more found in passing: Earth\'s belts carried a served link and a\n  "flux PEAK, not an edge" note the renderer never read -- now in the\n  hover and the i-panel.\n- **What is NOT served and therefore not stated:** the sidereal\n  rotation period and the obliquity as numbers. The axis hover says\n  the rotation is not shown and names no period. The 23.44 deg tilt it\n  states is DERIVED (served pole through the renderer\'s sourced mean\n  obliquity), and says so. Serving the period is a small orrery\n  constants patch when a session has `constants_new.py` open.\n**Gap:** STEPS 4-8. Tony (do): run the patch, runner (6 of 6), push,\n`--live`, then Mode 5 on the phone at `interactive.html?exhibit=earth`\n-- conditions: arrival shows the eight shells, gold axis and yellow Sun\nline with the grid chip reading in AU and km; the drawer lists the Moon,\nterminator, GEO, belts, geocorona, Hill sphere, and one italic\n"not yet drawn" row; tap GEO and it lies in the equator ring\'s plane;\ntap the Moon and the brighter arc sits on the faint ellipse around the\nmarker; every hover ends in a Source line. Then the Studio card. The\nmagnetosphere is L-305. Closes on Tony\'s eyes.\n'), ('**Gap:** none until the trigger fires. Not a design decision awaiting\nTony; an option with a stated condition.\n**Ref:** L-286, L-303, L-307, index.html (`sweepWanted`, `applySweep`),\nskills/gallery-pipeline/SKILL.md.\n\n', "**Gap:** none until the trigger fires. Not a design decision awaiting\nTony; an option with a stated condition.\n**Ref:** L-286, L-303, L-307, index.html (`sweepWanted`, `applySweep`),\nskills/gallery-pipeline/SKILL.md.\n\n#### [L-309] The exhibit chrome keeps its sun* names after Earth joined it (rename deferred, with its reason)\n<!-- L:309 status:DEFERRED upd:2026-09-09 section:A flag: rice:2/2/90/2 -->\n- **What happened.** L-291 step 3 made Earth the second user of the\n  chrome in `interactive.html` -- drawer, nav cluster, frame zoom,\n  i-panel, HUD, consent gate, back link. The handoff left rename vs\n  parametrize as judgment at the point of edit. The edit PARAMETRIZED:\n  an `EXHIBITS` table carries per room the title, arrival half-range,\n  Python driver and scene composition, and `EX` is the current row.\n  The functions (`sunFocusOn`, `buildSunLayout`, `sunHudInstall`, some\n  sixty others), the CSS classes (`.sun-row`, `body.sun-exhibit`) and\n  the element ids (`sun-drawer-list`) keep their names, and Earth's\n  page carries the `sun-exhibit` body class.\n- **Why not renamed now.** A rename touches roughly a hundred\n  identifiers across a working room for no change a visitor can see,\n  and puts the Sun back under Mode 5 on the same day Earth first needs\n  it. Tony confirmed the sequence 2026-09-09.\n- **When to do it.** With the third room (Jupiter, per the ladder), or\n  in a session that has nothing else open in `interactive.html`. Names\n  to reach for then: `exhibit*` for functions, `.ex-row` /\n  `body.exhibit` for CSS, `exhibit-*` for ids. `live_scene_urls` in\n  `tools/json_converter.py` reads the EXHIBITS table and does not care.\n**Gap:** none until a third room or a free session; a rename, not a\nredesign.\n**Ref:** L-291, L-267 (where the chrome came from), interactive.html\n(`EXHIBITS`, `EX`), `tools/json_converter.py::live_scene_urls`.\n\n")]


def main():
    raw = TARGET.read_bytes().replace(b"\r\n", b"\n")
    got = hashlib.md5(raw).hexdigest()
    if got != EXPECT_MD5:
        print("STOP: LEDGER_CONSOLIDATED.md md5 (LF) is %s, expected %s (at d39cf27c)." % (got, EXPECT_MD5))
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
    print("ok  LEDGER_CONSOLIDATED.md: L-303 PENDING-GATE, L-291 step 3 recorded, L-309 opened (DEFERRED)")
    print("Next: ledger_index.py, commit, push, report the SHA.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
