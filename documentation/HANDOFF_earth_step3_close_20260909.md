# Earth Exhibit -- Step 3 built and on Tony's eyes; L-303 built; L-168 fixed

Built on gallery `e22cde126f49510f98e4ae4112e8ec8137c9d8aa`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
and orrery `f53273c3db98150c169cd9035ccaaf7590ac8c4c`
at https://github.com/tonylquintanilla/palomas_orrery
(orrery moves once more when `patch_L291_14` lands; see the rollup).

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-09
Protocol v3.55. Ledger handles: L-291, L-303, L-168, L-309, L-310.

A partner without this Project reads these first, live at the SHAs
above: `PROJECT_INSTRUCTIONS.md` (orrery root) and, for this task,
`skills/interactive-exhibit/SKILL.md`, `skills/gallery-assembler/SKILL.md`,
`skills/ledger-and-session-records/SKILL.md`. State back which you read.

**Supersedes** `HANDOFF_earth_step3_design_round_20260908.md` and
`HANDOFF_earth_step3_20260908.md` for step 3. Steps 4-6 are done; step
7 (the Studio card) is Tony's; step 8 closes L-291.

---

## STEP 0 -- Gates

- No skill was bumped this session. All seven loaded copies matched the
  v3.55 manifest at session start (assembler 1.3, provenance 2.11,
  interactive-exhibit 1.0, ledger 1.10, orrery-coding-conventions 1.7,
  safe-file-editing 1.10, agentic-pre-test 1.2). Nothing travels.
- `git ls-remote` both repos and reconcile if either moved past the
  anchors above.

## WHAT LANDED (gallery, five pushes)

| Push | Patch | What |
|---|---|---|
| `23054535` | `patch_L303_1_cards_per_orientation` | one card per orientation: converter's sibling stamp, the one viewer rule, sweep_report class, 104 -> 144 cards (40 splits, Keeling collapsed) |
| `97ed2012` | `patch_L291_9_earth_step3` | `?exhibit=earth`: EXHIBITS table, `gallery/earth_geometry.js`, GEO ring, belts in the drawer beyond the frame, source in meta, absence row, Studio picker reads the table, runner row "Earth scene geometry" |
| `bac5a5ee` | `patch_L291_11` | Mode 5 round 1: Sun line from the centre + subsolar dot, terminator marker on the circle, frame axes width 6, spin arcs |
| `da57d095` | `patch_L291_12` | round 2: arc white, ellipse rgba, dates in the arc hover (right changes, wrong cause) |
| `e22cde12` | `patch_L291_13` | round 3: **L-168** -- `propagate_marker` uses the served `n_deg_per_day`; fixture regenerated; arc sweep pinned 60-120 deg |

Runner 6 of 6 offline at every push; `--live` byte-identical, 8 files,
store drift 48 match / 0 DRIFT / 5 could-not-examine (the known class).

Orrery: `patch_L291_10_ledger_step3` landed at `f53273c3` (L-303
PENDING-GATE, L-291 step 3 record, L-309 opened).

## WHAT TONY'S EYES PASSED (2026-09-09, desktop; phone "works the same")

Arrival: eight shells, gold axis with spin arcs, yellow Sun line, grid
chip in AU and km. Drawer: Moon, terminator, GEO, belts, geocorona,
Hill sphere, and the italic magnetosphere row. GEO in the equator's
plane. The Moon's arc a clean quarter-orbit on the faint ellipse with
the marker on it. Terminator marker on the circle. Tony: "looks right."

## THREE THINGS THE PRIOR HANDOFF HAD WRONG (recorded in L-291)

1. Driver spec: `objects ["moon"], center "earth"`. Earth as an object
   is rejected by the resolver (stored relative to the Sun); its shells
   arrive by the centre-features path.
2. The Moon's trust window is served (3.42 days either side today); the
   arc reads it, no number in code.
3. The inner belt drew lit on arrival; belts beyond the frame now go to
   the drawer generically.

## OPEN, IN ORDER

- **L-291 step 7 (Tony, do):** Studio > New Interactive Card > pick
  `?exhibit=earth`, place in the editor, push. Then L-291 closes.
- **L-303 (Tony, do):** Mode 5 on the phone -- one card per figure, the
  portrait file; desktop shows both, tagged 16:9 and 9:16. Retype the
  portrait titles on
  `artemis_ii_20260402-0411_mission_moon_center2_mobile` and
  `maps_disintegration_20260403_07_structures_mobile`.
- **L-305:** the magnetosphere on Jelinek 2012, both repos together,
  its own session; the drawer row says "not yet drawn" until then.
- **L-310:** directional camera steps -- design round first (zero code).
- **L-309:** the sun* chrome rename, deferred with its trigger.
- **L-292:** serve the rotation period so the axis hover can state it.
- **Not in a rule yet:** a Python-side `as_of_today` cross-check for a
  planetocentric body (L-168 records the numbers).

## TONY-ACTION ROLLUP

1. **(do)** `patch_L291_14_ledger_mode5_close_20260909.py` (orrery
   root), then `ledger_index.py` (it moves L-168 to section C), commit,
   push, report the SHA.
2. **(do)** Save this file to the gallery repo's `documentation/`,
   commit, push.
3. **(do)** Step 7, the Studio card.
4. **(do)** L-303's phone check and the two titles.

## WHAT THIS SESSION LEARNED

- **Measure before theorising about the renderer.** Round 2 guessed at
  Plotly's transparent-line path. Round 3 ran one `atan2` sweep on the
  page's own output and read 8,406 degrees. The measurement took one
  command and was available in round 2.
- **Tony's eyes named the cause.** "Points too far apart in time" was
  exactly the diagnosis; the orrery's one-lunar-month rule and the trust
  window are the same idea.
- **A caught bug with an open Gap is a scheduled failure.** L-168 sat
  OPEN for six weeks with its fix designed; the first moon to render
  found it in the one place the fixture could not (the fixture's epoch
  equalled the elements' epoch, so the marker was right by luck).
- **Running the assembler beat reading the handoff, three times:** the
  driver spec, the trust-window number, the lit belt.

Written September 2026 with Anthropic's Claude Opus 5.
