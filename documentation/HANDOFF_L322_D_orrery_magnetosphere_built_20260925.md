# Handoff -- L-322 Stage D: the orrery magnetosphere built; gallery patch 3 next

**Built on orrery `4bab8c043bfecd713158e24867c6cef41813d5f3` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`a21680abf2f6daefb2f639fde28100252eb16b03` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
HEADs read live with `git ls-remote` on 2026-09-25, after Tony's last
push.

**Type: BUILD.** The next session builds gallery patch 3.

**Opens from** `documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md`,
rev 3, section 5 (the gallery half), with the tail and the belts specified
by what the orrery now draws: `RUN_RECORD_L322_D8_20260925.md` and
`RUN_RECORD_L322_D9_20260925.md`. **Companion records:** those two, and
`RUN_RECORD_L322_D10_20260925.md`, each with Tony's run appended.
**Supersedes** `HANDOFF_L322_D_gallery_pole_live_20260925.md` for what
remains; that handoff stays the record of D6, D7 and the tap-lag fix.

**Rules this work ran under:** protocol v3.68; provenance-discipline
2.18, orrery-coding-conventions 1.9, safe-file-editing 1.11,
agentic-pre-test 1.2, horizons-orbital-mechanics 1.1,
ledger-and-session-records 1.11. Every loaded copy was byte-identical to
`skills/` at orrery `62e93856`, checked at session start. Patch 3 will
fire gallery-cache-builder 1.6, gallery-assembler 1.3 and
interactive-exhibit 1.4 as well.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds gallery patch 3.

---

## 1. What was built, and how each piece was verified

All three are orrery patches, each run by Tony, each followed by the
orrery maintenance run (17 of 17 gating checkers passed every time), and
each confirmed on his screen.

- **D8, orrery `a909e283`: Earth's magnetosphere from `constants_new.py`.**
  - Four new rows. `EARTH_MAGNETOTAIL_FLARE_END_RADII` is 120 Earth
    radii, uncertainty 10, and `EARTH_MAGNETOTAIL_DIAMETER_RADII` is 60,
    uncertainty 5; both are measured, from Slavin et al. (1985).
    `EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII` is half the diameter, and
    `EARTH_MAGNETOTAIL_DRAWN_END_RADII` equals the observed 220; both are
    declared, and between them they carry the drawing's three rules.
  - The magnetopause is Shue's own surface, stopped at the cut angle.
    The tail starts where the surface stops, widens in a straight line
    to 120 Earth radii behind Earth, is 60 wide from there, is round, and
    ends at 220. Five numbers chosen by eye are gone.
  - `constants_rows.py` reads the uncertainty written on a row's
    `# Figures:` line, once, for every reader (`Row.uncertainty`,
    `uncertainty_of()`, one pattern `UNCERTAINTY_FIELD_RE`), and
    `export_constants.py` serves it as `"uncertainty"` beside each row.
    `constants_export.json` moved from schema 3 to 4.
  - Verified: Tony's plot at 0.01 AU showed the tail and the surface
    inside the bow shock; the hover read "good".
- **D9, orrery `7133636d`: the belts' rings, evenly spaced.** Tony's note
  on D8 was that the gaps between rings were uneven, which reads as a
  physical feature, and that the brighter ring was barely brighter.
  Each belt's rings are now evenly spaced on the largest step that lands
  on both edge rows and on the peak row: 10 rings every 0.1 Earth radii
  for the inner belt, the peak fifth from the inside; 9 every 0.5 for the
  outer, the peak fourth. The peak ring is fully opaque and drawn with
  points twice the size. Both hovers say the belt is one continuous
  region and the rings only mark its extent. Verified: Tony, "very nice".
- **D10, orrery `4bab8c04`: a grid label on every orrery plot.** A small
  box in the lower left, such as "grid 0.0002 AU (29,920 km)", added by
  `save_utils._inject_grid_label` to every page whose 3D scene is drawn
  in AU. It reads the spacing Plotly actually drew, so it follows Auto
  scale, the Fly To buttons and camera tracking. Verified: Tony's manual,
  Fly To and Auto plots, "correct".

## 2. Rulings this session

- **The tail is drawn round** (Tony, 2026-09-25). The width was measured
  near the plane of Earth's orbit; the real tail is often flattened in a
  direction set by the solar wind's field (Sibeck and Lin 2014); under
  average conditions it is about as tall as wide (Maezawa et al. 1997).
  The rule and its reason are on `EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII`.
- **The uncertainty is read in `constants_rows.py` and served by the
  export** (Tony, 2026-09-25).
- **The belts: evenly spaced rings on a step that lands on the peak**
  (Tony, 2026-09-25, option 2 of two), with the hover sentence.
- **The orrery grid label is a label only**, not the gallery's turning
  triad (Tony, 2026-09-25).

## 3. What remains of Stage D, in order

1. **Gallery patch 3 (manifest section 5, the rest).**
   - **Pull the new export first.** The gallery's copy of
     `constants_export.json` is still the one from orrery `62e93856`,
     schema 3. The next gallery maintenance run pulls orrery `4bab8c04`,
     schema 4; `pull_constants_export.py` accepts "schema 3 or later".
     Add `"uncertainty"` to `FIELDS` in `tools/mirror_constants.py`, so
     served links carry it.
   - **The tail.** Add pointer entries in `data/objects_config.json` for
     the four new tail rows, and draw the tail in the Earth room from the
     served rows exactly as D8's run record section 6 describes: Shue's
     surface to the cut, a straight line from where it stops to the flare
     end, the drawn radius from there to the drawn end, round. The tail's
     starting radius and distance are computed from the served Shue rows
     at the cut, not served. Delete the unused `length_radii`,
     `base_radii`, `end_radii`, `color` and `opacity` from the
     `magnetotail` entry and rewrite its `_declared` sentence. Re-home the
     entry's `source` string: it cites the 1983 abstract for "the tail
     diameter settles near 60", which is now the 1985 row's job.
   - **The belts.** Delete both `belt_thickness` entries and the
     renderer's 0.5 fallback, and draw the rings as D9's run record
     section 5 describes: evenly spaced from the served inner edge to
     the served outer edge on the step that lands on the served peak,
     the peak ring brighter and larger, and the same hover sentence.
     The step is the greatest common divisor of the two distances, edge
     to peak and peak to edge, taken on the served decimal values; the
     orrery's `_even_belt_rings()` in `earth_visualization_shells.py`
     is the reference, including its cap of 25 rings.
   - **The hovers.** The tail's wording in D8's run record section 4 is
     the orrery's; the room keeps its own i-panel conventions and hover
     budget. The tail's two measured sizes print with their served
     uncertainties, "plus or minus".
   - **Carried unchanged from the previous handoff:** the axis hover's
     sidereal period from the row, with a pointer entry for it, the
     re-homed sources, and the "none is served" sentence replaced;
     Earth's orientation source string names Horizons; the magnetic-tilt
     source sentence's factor-of-ten rate corrected;
     `tools/test_mirror_constants.py` line 373 expects SERVED; D5's cone
     cleanup if the gallery draws a cone.
   - **The cache is rebuilt**, because the config changes.
   - **Phone checks** on Tony's phone, both rooms, as for D7.
2. **How exact rows print (manifest section 6).** Unchanged.

## 4. For the ledger, one row per class

New this session:
- **The orrery's magnetosphere hover gives Earth radii without
  kilometres or AU**, in its old lines and its new. Each would need a
  row in `constants_new.py` with a declared figure count, as the
  standoffs got at C2.
- **The drawn tail's growth and the 1983 "about 30 percent".** From 20
  to 120 Earth radii behind Earth the straight line grows about 44
  percent at the central width and 32 percent at its low end; the 1983
  figure is inside the 1985 envelope, so the construction stands. The
  note is on the flare-end row.
- **The uncertainty field's pattern reads a sentence's full stop as a
  decimal point.** Written "uncertainty 10. The ..." it served "10.".
  Every row today follows the number with a unit, a comma or the line's
  end; nothing checks that the next one will.
- **Earth's magnetosphere costs about 42 percent more per animation
  frame** (147 to 209 KB) since D8; D9 held it level. A rendering
  matter, for Tony's eye in animation.
- **`shell_configs.py`'s magnetosphere tooltip** (dead data, kept in
  step with its live twin) says nothing about the tail and still says
  the belts are drawn at the flux peak.
- **A scanner comparison by set could pass blind.** Comparing the
  scanner's findings as a set of names cannot see a second finding that
  looks like one already there. D8's result stands because the
  scanner's own count agreed; D9 and D10 compared counted lists. Worth a
  line in the provenance skill's scanner mechanics if it recurs.

Carried from the previous handoff, unchanged:
- The phone tap lag, fixed at gallery `ce09f789`: DONE. The next free
  handle at orrery `62e93856` was L-363; re-read the ledger index before
  assigning one.
- Phone behaviour of the rooms has no automated check.
- The hover budget check's weak floor ("at least one hover").
- `documentation/payload_earth_scene.json` is aging (tilt 9.6 against the
  served 9.4105).
- The cache builder types its own `KM_PER_AU` beside the served row.
- The gallery maintenance routine pulls the export after the build.
- L-311 is DONE when gallery patch 3 lands; L-325 and L-342 close per
  manifest section 8.
- Earth's eccentric dipole offset, other bodies' cone hovers, the
  scanner's proximity rule, and provenance-discipline 2.18's stale worked
  example (23.439291).

## 5. Tony-actions

- (do) File this handoff in the orrery's `documentation/`.
- (do) File the ledger rows in section 4.
- (decide) The Sun's Auto view, carried from the previous handoff.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.
