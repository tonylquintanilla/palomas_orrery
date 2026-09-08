"""
patch_L291_7_ledger_masterplan_20260908.py -- session close: ledger + master plan v27

Built on orrery af4c604ed48540876b3165bc772411cd0dc7d0c9
at https://github.com/tonylquintanilla/palomas_orrery (main)
and gallery 700b426d4cecc1f80fd6f9ca5758e5058ea497a6
at https://github.com/tonylquintanilla/tonyquintanilla.github.io (main).

WHAT THIS DOES (two files in the ORRERY repo, applied only if both guards pass)

LEDGER_CONSOLIDATED.md
  Updates: L-291 (step 2 complete both halves; live store drift 24 MATCH
                  by name; step 3 next), L-292 (the gallery serves the
                  exosphere as the geocorona row; the orrery shell waits),
                  L-286 (a regression the sweep caused and its fix),
                  L-288 (the converter path and the grey box, fixed; the
                  served Earth-and-Moon portrait file still carries the
                  box until re-exported).
  Adds:    L-301 Landscape+portrait pairing lost at L-287, restored
           L-302 The info card closed itself on the tap that opened it
           L-303 One card two files, or one card per orientation? (Tony: decide)
           L-304 Plotly relayout field notes for gallery-assembler (bump pending)
  Then Tony runs ledger_index.py.

documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md -> v27
  The status header said Earth was DESIGNED AND NOT BUILT; step 2 is done
  on both sides, so that line was the stale kind The Correction Does Not
  Travel names. Header and stamp move; Section 5a gains the 2026-09-08
  subsection. Restamp reason: the status paragraph was wrong, not "a
  key juncture".

Handles: highest at af4c604e is L-300; the four new ones are the next
four. Re-checked before writing.

Written September 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = {
    "LEDGER_CONSOLIDATED.md": "9c3097b4c2459f4a91c85740a572337f",
    "documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md": "93d50355f252a132ddc953ee1f3c6764",
}
EXPECTED_MAX_HANDLE = 300

LEDGER_EDITS = [
    # ---- L-291 ----
    (
        "<!-- L:291 status:OPEN upd:2026-09-07 section:A flag: rice:4/4/80/3 -->",
        "<!-- L:291 status:OPEN upd:2026-09-08 section:A flag: rice:4/4/80/3 -->",
    ),
    (
        "**Gap:** the GALLERY half of step 2 -- `data/objects_config.json`\n"
        "Earth entry: value/unit/source/orrery_constant on every feature,\n"
        "the new rows (magnetosphere as four served rows, LEO, geostationary,\n"
        "Hill sphere, geocorona), the `orientation` block, the exosphere shell\n"
        "(L-292) -- then store drift MATCH by name on the live run. Then steps\n"
        "3-8. Closes on Tony's eyes.\n",
        "- **Claude, 2026-09-08 -- STEP 2 COMPLETE, both halves.**\n"
        "  `patch_L291_6_earth_served_entry.py` (gallery `12241c0` -> served\n"
        "  live by the 2026-09-08 nightly): Earth's entry rebuilt in the measured\n"
        "  shape, nine groups -- earth_interior, earth_atmosphere,\n"
        "  earth_exosphere, earth_orbital_zones, earth_geostationary,\n"
        "  earth_magnetosphere, van_allen_belts, hill_sphere, orientation. The\n"
        "  magnetosphere's one orrery call is four served rows. Seven files\n"
        "  moved with it, each found by a check rather than by reading: the\n"
        "  drift checker learned Earth radii (`_RADII` on an `EARTH_` name,\n"
        "  factor from the store); the shell-set renderer learned `R_earth`,\n"
        "  `km` and `planet_radius`, so the Earth groups draw in the Explorer\n"
        "  room today with their sources in the hover; the belt renderer reads\n"
        "  measured distances; the builder's shape validator reads them too\n"
        "  (the Cache builder suite caught that); two test files re-pinned to\n"
        "  the served shape; the smoke fixture regenerated from the entry.\n"
        "- **Live run, Tony, 2026-09-08:** 53 pointers, 48 MATCH, 0 DRIFT.\n"
        "  All 24 Earth constant pointers MATCH by name. The five that could\n"
        "  not be examined are the known class (pole pointers into\n"
        "  `idealized_orbits.py`, the galactic-tide default) -- none new.\n"
        "- **Not drawn yet, and the dispatch says so by name:**\n"
        "  earth_geostationary (an equatorial ring) and earth_magnetosphere\n"
        "  (the two standoff shapes). Their renderers are step 3.\n"
        "**Gap:** STEP 3 -- the `EXHIBIT === \"earth\"` branch in\n"
        "`interactive.html` (driver spec: objects Earth + Moon, center Earth,\n"
        "half-range floor 6.155e-5 AU; eight shells lit on arrival; axis,\n"
        "equator plane, Sun direction on), the GEO ring and magnetosphere\n"
        "renderers, the terminator as geometry, the Moon's orbit with the\n"
        "trust-window arc, the frozen-epoch hovers, the `sun*` chrome by\n"
        "parameter, i-panel copy with sources. Then steps 4-8. Closes on\n"
        "Tony's eyes.\n",
    ),
    # ---- L-292 ----
    (
        "<!-- L:292 status:OPEN upd:2026-09-06 section:A flag: rice:3/3/75/2 -->",
        "<!-- L:292 status:OPEN upd:2026-09-08 section:A flag: rice:3/3/75/2 -->",
    ),
    (
        "**Gap:** the exosphere shell, with its constant in `constants_new.py`;\n"
        "the other two when a build already has the file open.\n",
        "- **Claude, 2026-09-08:** the constant exists -- `EARTH_GEOCORONA_RADII`\n"
        "  (100 R_E, Baliukin et al. 2019) since `c51761a0` -- and the GALLERY\n"
        "  serves the exosphere as the `earth_exosphere/geocorona` row, named\n"
        "  as a detected extent rather than an edge. The ORRERY still folds the\n"
        "  exosphere into the upper-atmosphere hover and draws no shell of its\n"
        "  own; that is the remaining half.\n"
        "**Gap:** the orrery's exosphere/geocorona shell in\n"
        "`SHELL_CONFIGS['Earth']` at `EARTH_GEOCORONA_RADII`; the other two\n"
        "when a build already has the file open.\n",
    ),
    # ---- L-286: the sweep's regression ----
    (
        "<!-- L:286 status:OPEN upd:2026-09-06 section:A flag: rice:5/4/70/4 -->",
        "<!-- L:286 status:OPEN upd:2026-09-08 section:A flag: rice:5/4/70/4 -->",
    ),
    (
        "**Gap:** the room-path reader in `index.html` (filter a grid to a room);\n"
        "the breadcrumb component shared by both pages; the special-exhibit\n"
        "placement; the room-shape field; Mode 5 on phone at all four levels.\n",
        "- **Regression found by Tony 2026-09-07, fixed at gallery `1eb1e084`\n"
        "  (`patch_L286_1_viewer_3d_rotation.py`).** Served 3D cards did not\n"
        "  rotate on load; the orbit or reset button revived them on the\n"
        "  desktop, and the phone has neither. The sweep's `applySweep()` ran\n"
        "  after every newPlot and, for a 3D figure with no dragmode, compared\n"
        "  \"restore null\" against the layout's undefined and relayouted\n"
        "  `dragmode: null`. In Plotly 2.35.2 that relayout makes gl3d's\n"
        "  updateFx copy the LAYOUT dragmode (default \"zoom\") into every scene,\n"
        "  and turntable rotation is gone. Read out of the shipped bundle, not\n"
        "  inferred. Fix: a 3D figure never has its dragmode touched by the\n"
        "  sweep; for 2D an absent dragmode reads as null. Tony's Mode 5:\n"
        "  correct. Field note filed under L-304.\n"
        "**Gap:** the room-path reader in `index.html` (filter a grid to a room);\n"
        "the breadcrumb component shared by both pages; the special-exhibit\n"
        "placement; the room-shape field; Mode 5 on phone at all four levels.\n",
    ),
    # ---- L-288: converter path + grey box ----
    (
        "<!-- L:288 status:OPEN upd:2026-09-05 section:A flag: rice:3/3/70/2 -->",
        "<!-- L:288 status:OPEN upd:2026-09-08 section:A flag: rice:3/3/70/2 -->",
    ),
    (
        "**Gap:** the converter path above; then DONE.\n",
        "- **Two Studio-chain defects found by Tony 2026-09-07, fixed at gallery\n"
        "  `e6c39a00` (`patch_L288_1_converter_path_and_routed_hover.py`).**\n"
        "  (1) `json_converter.py` resolved its output folder against the\n"
        "  working directory; run from `tools/` it made `tools/gallery/` and a\n"
        "  shadow schema-1 metadata there, so the editor never saw the card.\n"
        "  Now resolved against the repo root from the script's own location.\n"
        "  (2) Portrait's routed hover suppressed the tooltip by transparency,\n"
        "  and Plotly replaces a zero-opacity label background with `#444`\n"
        "  grey while the orrery's per-trace `hoverlabel.font.size: 11` beat\n"
        "  the size-1 suppression: a large grey box, no text. Fix: strip the\n"
        "  per-trace hoverlabel when routing; opacity 0.01, not 0. The prior\n"
        "  field note that `hoverinfo='none'` kills 3D events was respected.\n"
        "- **Still visible on the site:** the served Earth-and-Moon PORTRAIT\n"
        "  file was exported 2026-09-07 17:50, before the fix; it carries the\n"
        "  grey box until the scene is re-exported through Studio and\n"
        "  re-converted (Tony-action, do).\n"
        "**Gap:** the live-card converter path above; the Earth-and-Moon\n"
        "portrait re-export; then DONE.\n",
    ),
]

NEW_BLOCKS = """#### [L-301] Landscape+portrait pairing lost at L-287, restored in the converter
<!-- L:301 status:DONE upd:2026-09-08 section:C flag: rice:4/4/90/1 -->
- **Found by Tony 2026-09-08:** the Earth-and-Moon card showed its
  landscape file on the phone. He converts a landscape export and a
  portrait export SEPARATELY, as always -- Studio handles each by its
  own preset, so they are separate scenes -- and that used to give one
  card serving the right file to each device.
- **What broke.** Until L-287 (2026-09-04) a card carried a `mode` tag
  and the viewer FILTERED the grid by device. L-287 made one card carry
  two `files` slots and its migration paired existing cards BY TITLE
  (38 pairs). The converter that shipped with it has no pairing rule:
  `_v2_entry` joins a new file to a card only on a matching filename,
  and Studio's `<base>_gallery` / `<base>_mobile` never match. Every
  pair converted since landed as two one-file cards, and the viewer,
  which now shows every card everywhere, served the landscape one to
  the phone. Three pairs: Earth and Moon, MAPS disintegration
  structures, Artemis II moon-centered -- the last two also with
  titles typed differently between L and P, which a title rule alone
  would miss.
- **Fix, gallery `1eb1e084` (`patch_L287_2_converter_pairs_orientations.py`):**
  a new file joins an existing card by, in order, filename/id; shared
  STEM (trailing `_gallery|_mobile|_portrait|_landscape` removed) with
  that orientation empty; exactly one title match with that slot
  empty. The three stranded pairs merged by the same rule (landscape
  card survives; two differing titles printed for the editor). 107 ->
  104 cards. Tested both orders and the title-only case.
- **Tony's Mode 5, 2026-09-08:** the phone serves the portrait file.
**Gap:** none. See L-303 for the design question this raised.
**Ref:** L-287, `tools/json_converter.py`, `gallery_metadata.json`,
`gallery/patch_L287_1_migrate_schema_v2.py` (the migration's title
rule, which this generalises).

#### [L-302] The info card closed itself on the tap that opened it
<!-- L:302 status:DONE upd:2026-09-08 section:C flag: rice:4/4/90/1 -->
- **Found by Tony 2026-09-08, three symptoms, one cause.** Phone: tapping
  a marker showed only the hover box; the card came up only after a
  small upward swipe. Desktop in mobile mode: a left click flashed the
  card; only a right click kept it. Desktop mode: correct.
- `index.html` opens the card from `plotly_click`; the same tap or click
  then bubbles as a DOM `click` to the document listener whose rule is
  "a click outside the card dismisses it" -- and it dismissed the card
  it had just opened. A right click fires plotly_click but no DOM click;
  a tiny drag on release is still a Plotly click and no DOM click. Those
  were the two accidental workarounds.
- **Fix, gallery `700b426d` (`patch_viewer_infocard_tap_20260908.py`):**
  `showInfoCard` stamps its open time; the dismiss listener ignores a
  click within 400 ms of it. Same patch re-pinned
  `documentation/pin_artifact1_known_failure.py` to the 13 feature keys
  served since L-291 (the pin had caught that move, correctly, once the
  nightly rebuilt the cache).
- **Tony's Mode 5, 2026-09-08:** correct on mobile.
**Gap:** none.
**Ref:** L-288 (the grey box that still shows behind it until the
portrait re-export), index.html, gallery-pipeline SKILL.md (mobile).

#### [L-303] One card with two files, or one card per orientation? (Tony to decide)
<!-- L:303 status:OPEN upd:2026-09-08 section:A flag: rice:3/3/60/2 -->
- **Tony, 2026-09-08 (paraphrased from chat, not his hand):** he would
  prefer a separate card for each orientation. The single L+P card does
  not show the details of each file; it shows only 16:9, never 9:16 for
  the portrait; and replacing or deleting one file should not touch the
  other. Separate scenes are necessary because Studio handles each by
  its own preset.
- **Claude's account of the current model.** L-287's rule is one card,
  two slots; on a phone the viewer serves the portrait slot, on the
  desktop the landscape, so the mobile scene stays unique in content.
  The editor already offers Preview / Replace / Clear per slot and a
  size per file. The 16:9 / 9:16 radio governs the ONE-file case only.
- **The fact that bears on the ruling:** the viewer no longer filters
  the grid by device. Two separate cards would both appear on every
  device unless device filtering returns (a `shape`- or slot-based
  filter), which is what the L-286 sweep replaced. So "separate cards"
  is really "separate cards AND filter by device", and both halves need
  the ruling.
- Options: (a) keep one card, improve the editor's display of the two
  files (show both shapes, per-file dates); (b) one card per
  orientation, restore device filtering in the viewer, and undo the
  three merges of L-301; (c) something else.
**Gap:** Tony-action (decide). No build until ruled.
**Ref:** L-287, L-301, L-286, `tools/gallery_editor.py`, index.html.

#### [L-304] Plotly relayout field notes for gallery-assembler (bump pending)
<!-- L:304 status:OPEN upd:2026-09-08 section:A flag: rice:3/2/90/1 -->
- Three Plotly 2.35.2 behaviours were read out of the shipped bundle
  this session and each cost a real defect. They belong beside L-278 in
  the gallery-assembler field notes, one bump, next session that opens
  that skill (one session, one bump):
  1. A layout-level `dragmode` relayout -- even to null -- makes gl3d's
     `updateFx` copy the LAYOUT dragmode (default "zoom") into every
     scene; turntable rotation is lost until a modebar button restores
     it (L-286 regression).
  2. `hoverlabel.bgcolor` with ZERO opacity is replaced by
     `defaultLine` (#444): "transparent" renders as opaque grey. Use a
     small non-zero opacity (L-288).
  3. A per-trace `hoverlabel` overrides the layout's; the orrery writes
     `{font: {size: 11}}` on many traces, so layout-level suppression
     never applies to them (L-288).
  And one viewer lesson, not Plotly's: a `plotly_click` bubbles as a DOM
  click; a document-level dismiss listener sees the click that opened
  the thing it dismisses (L-302).
**Gap:** Tony-action (do): gallery-assembler 1.2 -> 1.3 with these four
notes, when a session next has that skill open.
**Ref:** L-278, L-279, L-286, L-288, L-302, skills/gallery-assembler/SKILL.md.

"""
INSERT_BEFORE = "#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery\n"

# ---- master plan ----
MP_EDITS = [
    (
        "**Status:** v26 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n",
        "**Status:** v27 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n",
    ),
    (
        "5). **The second exhibit, EARTH, is DESIGNED AND NOT BUILT** (L-291):\n"
        "shells plus the Moon, arriving at low Earth orbit, blocked only on the\n"
        "`interactive-exhibit` skill install.\n",
        "5). **The second exhibit, EARTH, has its DATA SERVED and its CODE NOT\n"
        "YET WRITTEN** (L-291): steps 0-2 of the interactive-exhibit skill are\n"
        "done on both repos as of 2026-09-08 -- 21 sourced constants in the\n"
        "orrery store, every Earth shell reading them, and a nine-group served\n"
        "entry whose 24 pointers read MATCH on the live run; step 3, the\n"
        "`EXHIBIT === \"earth\"` branch, is next.\n",
    ),
    (
        "**Last updated:** September 6, 2026 (v26: the EARTH exhibit designed in\n",
        "**Last updated:** September 8, 2026 (v27: Earth's step 2 complete on\n"
        "both sides -- the store, the shells, the served entry, the live drift\n"
        "run; four gallery-pipeline defects found by Tony on the served\n"
        "Earth-and-Moon card and fixed the same day; Section 5a gains the\n"
        "2026-09-08 subsection; with Anthropic's Claude Fable 5.1. v26,\n"
        "September 6, 2026: the EARTH exhibit designed in\n",
    ),
    (
        "**What this does to the order.** Nothing moves. Step 3, Earth into the\n"
        "assembler, has had its design conversation and is now blocked on ONE\n"
        "Tony-action: installing the `interactive-exhibit` skill to the account,\n"
        "since a session can read the repo copy but cannot load it. Step 2's\n"
        "remaining item (L-286's rooms page) is unchanged.\n"
        "\n"
        "### What this section deliberately does not carry\n",
        "**What this does to the order.** Nothing moves. Step 3, Earth into the\n"
        "assembler, has had its design conversation and is now blocked on ONE\n"
        "Tony-action: installing the `interactive-exhibit` skill to the account,\n"
        "since a session can read the repo copy but cannot load it. Step 2's\n"
        "remaining item (L-286's rooms page) is unchanged.\n"
        "\n"
        "### 2026-09-07/08 -- Earth's data lands on both sides, and the served\n"
        "card found four defects in the pipeline that serves it\n"
        "\n"
        "Measured at orrery `af4c604e` and gallery `700b426d`, both confirmed\n"
        "against the live remotes at close. Appended, not merged.\n"
        "\n"
        "**The gate fired.** The session loaded `ledger-and-session-records`\n"
        "1.10 and `interactive-exhibit` 1.0, matching the manifest -- the check\n"
        "the 2026-09-06 session could not perform from inside itself. L-290\n"
        "and L-296 closed on it.\n"
        "\n"
        "**Step 2, orrery side, in four patches, each Mode-5'd.** Twenty-one\n"
        "constants entered `constants_new.py` with fetched sources (IERS 2010\n"
        "TN36; IADC-02-01 Rev. 3; Baker et al. 2018; JGR 2025; Shue et al.\n"
        "1998; Lugaz et al. 2016; Baliukin et al. 2019). Every Earth shell\n"
        "literal that now had a store name was migrated onto it -- Tony's\n"
        "ruling: one store, one source of truth, the orrery side not deferred.\n"
        "Two values moved when sourced: the bow shock 15 -> 12.5 R_E (a\n"
        "citation saying 11-14 cannot sit under a 15) and LEO's edges by 7 km\n"
        "(the old figures were mean-radius sums). The atmosphere shells stopped\n"
        "drawing at visibility fractions and drew their sourced boundaries,\n"
        "as the chromosphere already did (L-295 closed). Every live Earth hover\n"
        "now ends in a Source line scoped to what it sources -- Tony's ruling,\n"
        "and the rule waits for orrery-coding-conventions 1.8 (L-299).\n"
        "\n"
        "**Step 2, gallery side, in one patch of seven files.** Earth's served\n"
        "entry in the measured shape, nine groups, 24 pointers MATCH by name on\n"
        "the live run. The six files beside the config were each found by a\n"
        "check: the drift checker did not know Earth radii; the renderers did\n"
        "not know `R_earth`, `km` or `planet_radius`; the builder's validator\n"
        "threw on measured belts; two test files pinned the old shape. The\n"
        "Earth groups draw in the Explorer room today, sources in the hover,\n"
        "which answers Tony's question of whether the assembler carries the\n"
        "sourcing the orrery now shows: it does, when the served row is\n"
        "measured and the renderer reads it.\n"
        "\n"
        "**Lagrange points sized and deferred (L-297).** Serving them from\n"
        "Horizons is a fourth serving shape in the builder plus an assembler\n"
        "branch plus one nightly -- a session of its own. Computing them from\n"
        "the Moon's marker was rejected: an approximation of a value that can\n"
        "be fetched. Tony ruled defer now, Horizons later.\n"
        "\n"
        "**Four defects the served card surfaced, all Tony's finds, all fixed\n"
        "the same day.** The converter wrote to `tools/gallery/` when run from\n"
        "`tools/` (L-288). Portrait's routed hover drew an opaque grey box\n"
        "because Plotly replaces a zero-opacity label background with grey\n"
        "(L-288). Served 3D cards did not rotate until a modebar button was\n"
        "pressed, because the sweep relayouted `dragmode` after every render\n"
        "(L-286). The landscape+portrait pairing Tony's workflow relies on\n"
        "had been lost at L-287 and three pairs were stranded as one-file\n"
        "cards (L-301). And the info card closed itself on the tap that\n"
        "opened it (L-302). Each Plotly behaviour was read out of the shipped\n"
        "bundle; the field notes wait for gallery-assembler 1.3 (L-304).\n"
        "\n"
        "**One design question raised, not ruled (L-303).** Tony prefers a\n"
        "card per orientation; the current model is one card with two slots,\n"
        "and the viewer no longer filters by device, so the two halves have to\n"
        "be ruled together.\n"
        "\n"
        "**What this does to the order.** Nothing moves. Step 3 -- the Earth\n"
        "branch in `interactive.html`, the GEO ring and magnetosphere\n"
        "renderers, the terminator, the Moon's trust-window arc, the chrome by\n"
        "parameter -- is next and is unblocked. Handoff:\n"
        "`documentation/HANDOFF_earth_step3_20260908.md` in the gallery repo.\n"
        "\n"
        "### What this section deliberately does not carry\n",
    ),
]


def main():
    texts = {}
    for name, md5 in FILES.items():
        lf = (ROOT / name).read_bytes().replace(b"\r\n", b"\n")
        got = hashlib.md5(lf).hexdigest()
        if got != md5:
            print("STOP: %s md5 (LF) is %s, expected %s (at af4c604e)." % (name, got, md5))
            print("      Either this patch already ran or the file moved. Nothing written.")
            return 1
        texts[name] = lf.decode("utf-8")
    led = texts["LEDGER_CONSOLIDATED.md"]
    mx = max(int(h) for h in re.findall(r"^#### \[L-(\d+)\]", led, re.M))
    if mx != EXPECTED_MAX_HANDLE:
        print("STOP: highest handle is L-%d, expected L-%d. Nothing written." % (mx, EXPECTED_MAX_HANDLE))
        return 1
    for i, (old, new) in enumerate(LEDGER_EDITS, 1):
        if led.count(old) != 1:
            print("STOP: ledger edit %d matched %d time(s), expected 1. Nothing written." % (i, led.count(old)))
            return 1
    if led.count(INSERT_BEFORE) != 1:
        print("STOP: ledger insertion anchor not unique. Nothing written.")
        return 1
    mp = texts["documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md"]
    for i, (old, new) in enumerate(MP_EDITS, 1):
        if mp.count(old) != 1:
            print("STOP: master plan edit %d matched %d time(s), expected 1. Nothing written." % (i, mp.count(old)))
            return 1
    for old, new in LEDGER_EDITS:
        led = led.replace(old, new, 1)
    led = led.replace(INSERT_BEFORE, NEW_BLOCKS + INSERT_BEFORE, 1)
    for old, new in MP_EDITS:
        mp = mp.replace(old, new, 1)
    for t in (led, mp, NEW_BLOCKS):
        t.encode("ascii")
    (ROOT / "LEDGER_CONSOLIDATED.md").write_bytes(led.encode("utf-8"))
    (ROOT / "documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md").write_bytes(mp.encode("utf-8"))
    print("Patched LEDGER_CONSOLIDATED.md                      md5 %s" % hashlib.md5(led.encode()).hexdigest())
    print("Patched documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md  md5 %s (v27)" % hashlib.md5(mp.encode()).hexdigest())
    print("Updated: L-291 (step 2 complete; Gap = step 3), L-292, L-286, L-288")
    print("Added:   L-301 pairing restored (DONE)   L-302 info card tap (DONE)")
    print("         L-303 card model -- Tony decides  L-304 Plotly field notes -> assembler 1.3")
    print("Next: ledger_index.py (Run button), commit, push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
