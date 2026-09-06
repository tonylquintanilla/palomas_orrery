# HANDOFF -- 2026-09-06 (BUILD + MODE 5): the lobby session closes -- lobby and sweep passed, edge labels failed and were rebuilt as the frame HUD

**Built on** orrery `a57e86b82503380e92b4e78cd7d8995a71183f20` at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery `fc8d9fb3ecb2` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main), both confirmed live with `git ls-remote`. Orrery is unchanged
since the last handoff's close; gallery moved twice (`66087696`: the
four away-session patches; `ae28621a`: cleanup; `fc8d9fb3`: the HUD,
back-link and tree-order patches), each confirmed live before the next
build step.

**Type:** BUILD with two Mode 5 rounds. Continues HANDOFF 2026-09-05
(away session). Tony was at his machine for the patch runs and the two
passes, away for the design and the record. This handoff CLOSES the
lobby session; the next session opens Earth.

**Skills loaded and checked against the manifest (all match):**
gallery-pipeline 1.2, safe-file-editing 1.10, ledger-and-session-records
1.9, gallery-assembler 1.2. No skill changed. L-290 proposes a bump of
ledger-and-session-records to 1.10; NOT done, awaiting Tony's ruling.

---

## Mode 5, in Tony's words and what came of each

**Phone, 2026-09-05, at gallery `66087696`.**
- Lobby: renders; doors, a door tap, a Featured card, Home all work.
- Featured order and room order did not match the editor; door-level
  cards sat under an invented "Other" heading. Ruling: the tree is the
  rule. Built as `patch_L286_1_tree_order.py` (live at `fc8d9fb3`).
- Sweep: "this card sweeps correctly" (Paleoclimate Cenozoic). The drag
  handoff L-286 said needed a real phone has had one. Exceptions exist;
  Tony is checking them systematically.
- Safari's back and X landed on the Sun at Outer Corona. Cause was
  ours: the Sun page's "Gallery" button was a plain link. Built as
  `patch_L282_5_back_link.py` (live at `fc8d9fb3`); confirmed working
  on desktop and phone 2026-09-06.
- Edge labels (L-289, first build): FAILED. Scattered, floating,
  vanishing on zoom-out; "may be worse than the plotly labels." Right.
  Labels drawn in the scene behave as scenery. Redesigned in
  conversation (see below) and rebuilt as `patch_L289_3_frame_hud.py`
  (live at `fc8d9fb3`).

**Desktop and phone, 2026-09-06, at `fc8d9fb3`.**
- Triad moves with the grid (desktop); chip works; back link works.
- Four defects: frame note open on arrival and not closable; grid
  colours read as a second key; arrival grid 0.2 AU vs chip 0.1 AU;
  triad did not follow a touch rotation on the phone. All four in
  `patch_L289_4_hud_fixes.py`, delivered NOT run.
- Triad orientation: CONFIRMED by test (markers at +x, +y, +z in the
  scene matched the arrows), not by reasoning.

## Design rulings this session (Tony)

- **L-289 rebuild:** one chip states the uniform grid spacing; a corner
  triad turns with the camera; the First Point of Aries at the x tip
  with a note that the frame is the J2000 ecliptic, not a graph frame;
  aspect ratio read from the layout ("ticks are not always
  isometric"); grid colours tried and then withdrawn ("back to white");
  no dimming. The frame was verified in `feature_renderers.js`
  (poleBasis rotates IAU poles into the J2000 ecliptic) and the note
  sourced to the NAIF frames tutorial. The assembler does not pass the
  provenance scanner, so the citation is hand-carried in the note.
- **Tree order** for the menu and Featured; no new ordering field.
- **Back link** steps back in history when the gallery is behind it.

## Delivered, not yet run

Gallery root:
- `patch_L289_4_hud_fixes.py` `50c36fc2b788fc00c8e95fa269923bed` --
  guards on `interactive.html` at `fc8d9fb3`. Note on hover/tap and
  closable; grid white; arrival dtick from the Home rule; triad reads
  the live gl3d camera per frame (tested with Plotly's events removed:
  23 redraws in a drag, 0 at rest).
- `tools/sweep_report.py` `9b82880a5bf7e4e4b8bd20f29047ab8b` -- new
  devtool; prints every card by sweep class, names first; exits
  non-zero if a figure file cannot be read.

- `patch_L288_1_studio_live_card.py` `1292072c0119273c0283f792fd94c653` --
  guards on `tools/json_converter.py`, `tools/gallery_studio.py` and
  `tools/gallery_editor.py` at `fc8d9fb3`, all-or-nothing. Studio gains
  "New Interactive Card..." (scene picker read from interactive.html,
  title, placard, sources); the card lands in Storage with `live` set
  and no files; the editor places it. `live_scene_urls()` moved to
  json_converter so both tools read one list. Tony's rulings: Studio,
  not the editor; Storage, not a room prompt; no picture. Pre-tested
  per agentic-pre-test: py_compile x3; Studio and editor launched under
  xvfb on throwaway copies; add_live_card on a copy of the real
  metadata (create, Sun-duplicate refused by name, empty title refused,
  id collision suffixed _2, v1 file refused); the dialog driven headless
  (open, reject empty title, create with two sources, close, status
  logged). Not shown: how the dialog sits in Studio's window on
  Windows. NOTE: the ledger patch below was written BEFORE this build
  and does not record it; L-288's build record goes in the next ledger
  patch, after Tony's run.

Orrery root:
- `skills/interactive-exhibit/SKILL.md` (delivered as
  `SKILL_interactive-exhibit.md`; save under that path) -- NEW skill,
  1.0, cut from gallery `fc8d9fb3` and orrery `a57e86b8`. How an
  exhibit is designed, built, verified and carded: the Sun's anatomy as
  a table of shared vs per-body pieces; provenance as a CRITICAL rule
  of the build (value / unit / source / orrery_constant in the served
  entry; Store drift MATCH by name before done; text claims sourced
  inline because the assembler is outside the scanner; bound and
  braid); the L-278, L-289, L-282 field notes; the Mode 5 sequence;
  the eight-step order for adding an exhibit. Every function it names
  was checked to exist in the page. Tony's reminder recorded in it:
  provenance is formal in the assembler as it is built and
  retroactive to the orrery, both under the braid. Install: save,
  Settings > Skills, `skills_index.py` for the manifest row; the Earth
  session verifies its loaded copy reads 1.0 (Stale Skill = Stop).
- `patch_L289_5_ledger_mode5_rounds.py` `2ba56217d47145d96cd37f8785a70376`
  -- guards on the ledger at `a57e86b8`; then `ledger_index.py`.
  Tested through the indexer here: 285 blocks, no problems, L-290 on
  the board.
- `patch_L289_6_master_plan_v25.py` `fa7b024d73b48e25a1da66e74d11675d`
  -- guards on the plan at `a57e86b8`; independent.
- `documentation/L290_relay_anchor_drafts.md` -- the two amendment
  drafts (protocol; ledger-and-session-records 1.10) from the parallel
  Sonnet session, corrected for handle (L-290, not L-288) and delivery
  form (patch, not paste). Proposals until Tony rules.

## How things were tested, and what that does not show

Every patch: LF and CRLF throwaway copies, second run refused,
identical normalized output. `node --check` on the page scripts. The
HUD and its fixes were exercised in a stand-in Plotly scene with the
Sun camera (the Sun page cannot start in the sandbox: Pyodide's CDN is
blocked): note hidden on arrival, hover open / leave close, tap
elsewhere closes, arrival dtick 0.1 = chip 0.1, triad follows a drag
with the event path removed. The tree order ran on the real
`index.html`: 105 cards, Sun first in Featured, zero "Other". The back
link ran on the real page: history length did not grow on the Gallery
tap. Not shown by any of it: how the HUD reads over the real shells on
a phone, and whether the touch-rotation fix holds on iOS Safari.

## Discrepancies and lessons surfaced

- The first L-289 build passed every headless check and failed the
  phone on three counts. The checks measured the mechanism; only the
  phone measured legibility. Recorded in the plan as the round's rule.
- My ledger patch's refusal message on 2026-09-05 said "prediction
  missed" when the truth was "indexer not run yet"; the guard could not
  tell the two apart. Corrected in this session's patches, which name
  the already-applied case separately.
- One test in this session ran on the wrong copy (a `cp` to two
  directories copied to one) and I read the old code's output as the
  new code's for a message. Caught, re-run, recorded.
- The Sonnet document proposed a taken handle and a paste. Both are the
  very failure L-290 describes; noted in the drafts file.

## Tony-actions, rolled up

- **(do)** Gallery: save `sweep_report.py` to `tools/`; run
  `patch_L289_4_hud_fixes.py`; offline maintenance; commit; push; SHA;
  `--live`.
- **(do)** Orrery: `patch_L289_5`, `ledger_index.py`, `patch_L289_6`;
  save the L-290 drafts under `documentation/`; commit; push; SHA.
- **(do)** Mode 5 on the HUD fixes: note hidden on arrival; hover and
  tap; arrival grid equals chip; triad follows a touch rotation.
- **(do)** Run `tools/sweep_report.py`; check one card per class on the
  phone; report the exception classes.
- **(do)** Gallery: run `patch_L288_1_studio_live_card.py` at the repo
  root; open Studio, New Interactive Card..., make a test card, see it
  in the editor's Storage, delete it or keep it; commit the three
  tools; push.
- **(do)** Orrery: save `SKILL_interactive-exhibit.md` as
  `skills/interactive-exhibit/SKILL.md`; install it (Settings >
  Skills); run `skills_index.py`; commit PROJECT_INSTRUCTIONS.md (the
  manifest row) and the skill; push. Ledger records for L-288's build
  and the new skill go in the next ledger patch.
- **(do)** Move spent patch scripts to `documentation/` in both repos.
- **(decide)** L-290: accept, amend or decline the two drafts.
- **(decide, after Mode 5)** L-289 triad size and colours; whether the
  Explorer room gets the HUD; then L-289 DONE.
- **(decide)** Whether the hamburger stays once L-286 lands; museum
  sentence editor field or JSON by hand.
- **(do, separate)** Old-card cleanup in the editor.

## Next session

Open EARTH (master plan step 3) as a design conversation, zero code
first: what Earth's room shows on arrival; what it inherits from the
Sun (drawer, frame zoom, nav cluster, the HUD); what is Earth-specific
(Moon, orbit, seasons, the Earth System door's climate layers); what
the assembler must serve that it does not today. Read Section 5a step
3 and the served Earth entry in `coverage_index.json` before proposing.
L-286 (rooms, drill-down, breadcrumb) remains step 2's open item and
the thing that retires the hamburger and the shim.

Session start: orrery HEAD past `a57e86b8` carrying the ledger and plan
patches and the new skill; gallery HEAD past `fc8d9fb3` carrying the
HUD fixes, `sweep_report.py` and the Studio action; confirm the loaded
interactive-exhibit skill reads 1.0 and the manifest lists it (Stale
Skill = Stop -- if either is missing, STOP and ask Tony to push and
reinstall before Earth); read Tony's Mode 5 on the HUD fixes first; the
first Earth question is the design round in the skill's step 1.

---

*Session written September 6, 2026 with Anthropic's Claude Fable 5.1.
Built on orrery `a57e86b8` and gallery `fc8d9fb3`.*
