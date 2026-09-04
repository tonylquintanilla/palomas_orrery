# HANDOFF -- 2026-09-03 (evening): Stage C shipped; the Sun GUI is complete on desktop

**Built on** orrery `019bf724672bb3d71e803eb80dc00a16d07abd78` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `197fd96340722192f8f58ced7ea5cee62ca074f8` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
**Pushed at** orrery `def557e6fb7d1f4dc9f225b0b54a5aa492a94d48`,
gallery `98cc99bd865feaea3c0e7ad7c3ad9b07db5e5ea8`. Both confirmed
against the live remotes at session close.

**Type:** BUILD. Four gallery pushes and one orrery push, every one
run by Tony, every gallery one Mode 5 tested on the live page.
Supersedes HANDOFF 2026-09-03 (morning: "Four patches waiting, and the
wing designed") as the current state; that handoff stays authoritative
as the record of the wing design conversation (L-280..L-284).

---

## Confirm this first

Both repo HEADs against the pushed anchors above. If either has moved,
read the ledger before proposing work.

Skills this session: `gallery-assembler` 1.2, `safe-file-editing` 1.10,
`ledger-and-session-records` 1.9 loaded and matched the manifest. No
skill was bumped, so nothing carries. Protocol is v3.53 and was not
touched.

---

## What was done (all verified, none claimed)

The morning handoff's four patches had all run before this session
began: orrery at v3.53 with L-276 DONE and L-277, L-280..L-284 present;
gallery serving the 22 curated links with zero placeholders. That was
checked against the served `feature_configs.json`, not the ledger.

**Stage C of the Sun GUI (L-267), three gallery patches, in order:**

| Patch | Gallery SHA | What |
|---|---|---|
| `patch_L267_4_info_panel_links.py` | `0edf4bf4` | The i panel follows the focus: focused shell's swatch, name, one "Read more at NASA/Wikipedia" link, over the exhibit text. `renderShellSet` stamps each shell's link on its traces in Plotly `meta`; `buildSunDrawer` reads it there. No radius, no citation in the panel. |
| `patch_L267_5_wire_sun_info_toggle.py` | `42a906f6` | The i button had NEVER worked on the Sun exhibit. Its listener lived in `initControls()`, which the Sun path skips. Now in `wireInfoToggle()`, called by both paths. |
| `patch_L267_6_panel_drawer_share_height.py` | `6cfaf318` | Tony's option C: panel and drawer share the height. Drawer open, the panel stops at the drawer's measured top edge. Nothing moves sideways. |
| Tony's hand edit | `98cc99bd` | Drawer 40% / panel 60% (`interactive.html` lines 191 and 429). |

**Mode 5 passed**, Tony, on the live page, desktop, all trials: open and
close; Core with its Wikipedia link, opens in a new tab, page still
responds; switches to the Alfven surface and its NASA link while open;
keeps name and link when the focused shell is unticked; **no seize** with
the panel open while hovering markers and rotating. That answers the
mockup's open defect from 2026-08-30.

**Orrery close-out**, `patch_L265_267_stage_c_close.py` at `def557e6`:
L-265 DONE and moved to section C; L-267 amended with the Stage C
record; master plan status v21, Last updated September 3. Ledger index:
279 blocks, 171 live items.

Spent patch scripts are in each repo's root where they ran; archiving
to `documentation/` is Tony's usual sweep.

---

## What was found

- **The i button was decoration on the Sun from Stage A until today.**
  The code was there and compiled; the Sun path never ran it. Verify
  Execution, Not Appearance, on the page's own chrome. Claude's Stage C
  test proved the panel's contents were right and never asked whether
  the panel could open. Found by Tony's trial 1.
- **The hover-seize from the study did not reproduce on the live page**
  with the panel open. Most likely it was the L-278 click re-entry. The
  study's `hovermode: false` workaround was deliberately not ported:
  Stage B found that relayout throws inside Plotly and destroys
  `viewInitial`.
- **"Nothing focused" is unreachable on the live page.** Arrival
  focuses the outermost shell drawn, so the panel's "Focus a shell to
  see its link" text is correct and never seen. Not a defect.
- **Two orrery maintenance checkers fail in the sandbox** (Reset
  completeness, Orbit cache) for want of `tkinter` and `astroquery`.
  Environment, not code; they pass on Tony's machine. Worth knowing so
  the next session does not chase it.

---

## Tony-action list

- **(do)** Portrait pass on a phone: Stages A, B and C are all
  unverified on a small screen, and the 40/60 split was chosen on a
  desktop. Carried from L-260; the one thing between the Sun GUI and
  "complete".
- **(do)** Archive the six spent patch scripts (three gallery, one
  orrery, plus the morning's L265/L276/L277/L280 four already run) to
  `documentation/` when convenient.
- **(decide)** Whether the eighteen `*_info` strings stay in the
  orrery's desktop GUI (carried out of L-265 on closing).
- **(decide)** L-281: Cusdis hosted free tier now, or after the hall
  exists. Carried.
- **(decide)** Confirm or adjust RICE on L-280..L-284. Carried.
- **(decide)** Master plan: the two stale NEXT statements (lines 1219
  and 2343 at `def557e6`) were left as they were on Tony's word; what
  they should now say. L-268's order; L-266's shape;
  `project_instructions_v3_50.md` / `_v3_51.md` reconstruction. All
  carried from 2026-09-02.

---

## What the next session should build

**The hall (L-280), designed in conversation first.** The design is
recorded in L-280 / L-282 / L-283 in enough detail to start from the
ledger alone; do not rebuild it from memory. Iterate the hall screen
with Tony before writing anything: each round simpler. Portrait first;
Mode 5 is his. The gallery-pipeline skill (index.html) and
gallery-assembler skill both fire.

**Not next, but do not lose:** L-284 (retire the social export) sits
inside files that L-254 and the GUI work will open; cluster it there.
L-268's remediation runs by body on the rendering ladder, Earth next.

---

*Session written September 3, 2026 with Anthropic's Claude Fable 5.1.
Built on orrery `019bf724`, gallery `197fd963`; pushed at orrery
`def557e6`, gallery `98cc99bd`; both confirmed at close.*
