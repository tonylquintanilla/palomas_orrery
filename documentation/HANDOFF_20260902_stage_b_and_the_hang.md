# HANDOFF -- 2026-09-02: Stage B, and the hang that came with it

**Built on** orrery `2a3755cfe505ec3e665506e324f50f5ac923c75f` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `8e5f0bddcc8378d399f32c8a277d2e85ec1e84de` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote at session end.

**Type:** BUILD. Seven patches ran and were pushed. Nothing is waiting on
Tony's machine. Four ledger items opened, one closed, two amended. One
skill bumped, one protocol version.

---

## Confirm this first

Both repo HEADs against the anchors above.

Then, before work of the matching kind:

- **`gallery-assembler` must read 1.2.** It went to 1.2 at `e71f38ae`;
  the session that bumped it had loaded 1.1. Tony reinstalled it to the
  account, but a running session cannot see a reinstall, so that check
  could not be made from inside. **Confirm the loaded copy reads 1.2
  before any gallery work.** This is the whole of the carried obligation.
- `safe-file-editing` 1.10, `ledger-and-session-records` 1.9 and
  `orrery-coding-conventions` 1.7 all loaded and matched the manifest
  this session. The check is load-triggered, so it does not carry.
- The protocol is **v3.52**, uploaded to the UI. If the resident copy
  says anything else, the UI store is stale.

---

## What ran and was pushed

Seven patches, in order.

**`patch_L254_2_venus_mars_dead_builders.py`** (orrery) -- 13 dead
`create_*_shell` builders annotated in venus and mars, a dispatch note in
each naming the live magnetosphere, module stamps. Pushed at `5639a952`.

**`patch_L276_sites_and_relay_access.py`** (orrery) -- ten line numbers
corrected in `documentation/worksheets/L192_annotated_sites.txt`; L-276
and L-277 opened. Pushed at `7314fa55`.

**`patch_L267_2_sun_stage_b.py`** (gallery) -- Stage B of the Sun GUI,
ten edits, ported from `sun_gui_mockup.html`. Pushed at `e0edd16c`.

**`patch_L267_3_defer_click_focus.py`** (gallery) -- the click hang fix,
two lines. Pushed at `6fd6baaf`.

**`patch_L278_session_ledger_20260902.py`** (orrery) -- L-254 and L-267
amended, L-278 and L-279 opened. Pushed at `5b3fb6b4`.

**`patch_L279_gallery_assembler_diagnostics.py`** (orrery) --
`gallery-assembler` 1.1 -> 1.2, L-278's action redirected, L-279 closed.
Pushed at `e71f38ae`.

**`patch_v352_protocol_version.py`** (orrery) -- protocol to v3.52, v3.49
demoted to the history file, `project_instructions_v3_52.md` archived.
Pushed at `2a3755cf`.

The maintenance runner moved all three of the evening's orrery patch
scripts into `documentation/` on its own.

---

## Ledger state at session end

| Handle | State | What |
|---|---|---|
| L-254 | OPEN | dead builders -- 21 of 76 annotated, 55 left |
| L-265 | OPEN | 22 curated info_url links -- **now the gate on everything** |
| L-267 | OPEN | Sun GUI -- Stage A and B done, Stage C blocked |
| L-276 | OPEN | Mode 7's repo-access sentence, patch not written |
| L-277 | OPEN | L-192 site store anchors by line number |
| L-278 | OPEN | Plotly event-handler re-entrancy -- field note written, item open |
| L-279 | DONE | where the diagnostic discipline lands |

`ledger_index.py` reports 274 blocks, 168 live items.

---

## The decisions Tony made

**L-254 before L-244, on the braid.** Both scored 2.8 and the ledger
could not separate them. The rendering ladder could: L-254's modules are
the ones the ladder opens next, and L-244's conversion factors live in
the star pipeline, which the current artifact does not reach.

**No Fable relay for L-254.** Claude offered to test the new model on it
and recommended against; Tony agreed. The job had nothing left to find --
count closed, pattern proven -- so a relay could only come back right or
wrong on a fully specified task, which decides nothing.

**Stage B before the phone check.** The handoff had gated Stage B on a
Stage A phone pass. Tony reversed it after seeing that the missing
controls were the mockup's accepted design, not a regression.

**Do not repin the extractor.** The failure printed a REPIN block that
silently dropped all ten venus and mars pins. Correcting the line numbers
instead kept every pin live.

**`gallery-assembler`, not a new skill and not the resident protocol.**
Claude proposed an eleventh skill, then extending Mode 5 in the protocol.
Tony pointed at the skill whose own `fires_when` line already said "Mode
5 acceptance." The home existed and had not been used.

**The info icon before the mobile passes.** Tony's sequencing, stated at
the end of the session. It makes L-265 the gate.

---

## What was found, and what each one teaches

**A count does not carry the axis it was counted on, for the third time.**
L-254's "SIX are live" is true of `create_*_shell` and of nothing else --
19 more builders in the same modules are on the live dispatch without
that suffix, so 25 are live. Claude drew a conclusion from the six ("the
other modules are all dead") that was wrong for eight of twelve modules.
The axis is now written into the code, not just a document.

**A line-anchored store breaks on any insertion, and two checkers said
so.** `L192_annotated_sites.txt` holds `module TAB line TAB label` and
nothing regenerates it. Thirty-one inserted lines in each of two modules
moved ten sites into different enclosing scopes. Both failures had one
cause and one fix. Four more L-254 slices will do it again -- L-277.

**THE HANG, and it is the session's real work.** Clicking a cross marker
froze the page with `RangeError: Maximum call stack size exceeded`. Eight
reads to attribute a two-line bug. The relayout was never the problem: it
completed cleanly from the console with a tooltip up, with the tooltip
dismissed, and on a timer over a hovered marker. It was fatal only when
reached from inside `plotly_click`, because Plotly had not finished
dispatching when `layoutReplot` was sent back into it. `setTimeout(fn, 0)`
fixed it. Recorded as L-278 and as a field note in `gallery-assembler`
1.2.

**Three wrong readings, all from inferring test conditions.** The
protocol said what to click and never what state to start in. Trials 1
and 2 were read as exonerating hover and scene weight; both ran on a
light scene and Trial 2 never tapped a marker. Trial R was read as using
the full default set; it used the reduced one. Read 6 was read as "both
hang" when the notes said the relayout completed and the click was what
killed it. Tony carried every correction. That is the load this protocol
exists to spare him -- L-279, now closed into `gallery-assembler` 1.2.

**A diagnostic can destroy the state it is investigating.** The
`hovermode: false` command threw inside Plotly, aborted the relayout
partway, and took `viewInitial` with it, so the reset button stopped
working. Everything observed after that was an artefact of the
diagnostic. Retired in the protocol document with its reason.

**Stack DEPTH is evidence and was missed twice.** `Maximum call stack
size exceeded` on a stack about twenty-five frames deep is not recursion;
it is a large array applied as arguments. That tell was in the first
stack trace, and two hypotheses were chased past it.

**Two dead hypotheses worth keeping.** Hover hit-testing was blamed
first, on a real 2026-08-30 finding whose `Plotly.Fx.unhover` fix never
travelled from the mockup -- tested directly, changed nothing. Trace size
was blamed second, on the ~65,000 argument limit -- the largest trace in
the scene is 4,332 points and the one that hung is 400. Neither was
unreasonable; testing is what killed them.

**The mockup validated the design, not the performance.** Stage B is a
faithful port of a Mode 5-accepted mockup and still hung, because the
mockup's geometry was schematic and the live scene is real.

**The header had been stale since v3.50.** The protocol's version line
read v3.49 while its own history carried v3.50 and v3.51, and the SHA
anchor sat at `ded99fbe` across three versions. Tony found it. The
Correction Does Not Travel, pointed at the version stamp itself.

**Answered, from the prior handoff's action list:** the `hovermode:
false` fix does NOT cure the seize, and the seize was never a hover
problem. That question can come off the list.

---

## Tony-action list

- **(do)** **Replace the 22 placeholder `info_url` links (L-265).** All
  twenty values in the served `feature_configs.json` are
  `https://www.nasa.gov/`. This now gates Stage C, and Stage C gates the
  mobile passes by Tony's own sequencing. It is the top of the list.
- **(do)** Mode 5 portrait pass on phone and tablet, once the i panel
  works. Stage A and B are both live and unverified on a small screen.
- **(decide)** Whether `project_instructions_v3_50.md` and `_v3_51.md`
  get reconstructed from git. Nothing is lost either way -- their content
  is resident and git holds the bytes.
- **(decide)** Whether `MASTER_PLAN_INTERACTIVE_GALLERY.md`'s two stale
  NEXT statements get their own pass. Both describe
  `gallery/feature_renderers.js` as unbuilt; it shipped 2026-08-29.
  Carried from the prior session.
- **(decide)** L-268's order: the braid, or all sixteen with a harness.
  Carried.
- **(decide)** Which shape the dead-link check takes (L-266). Carried.
- **(decide)** L-277: whether each L-254 slice updates the site store, or
  the store stops anchoring by line and anchors by the name it already
  mints.

---

## What the next session should build

**Stage C of the Sun GUI, and it cannot start until L-265 does.** The i
panel carries links, not prose -- Tony's 2026-08-30 ruling, because the
`*_info` strings are Gemini-assisted and the provenance burden is too
high with no export gate in the gallery repo. With every link a
placeholder, the panel has nothing to show. There is no partial version
worth building: showing the source line would duplicate the cross
marker's hover, which the same ruling forbids.

**If L-265 is not ready, the honest alternatives, in order:**

1. **L-276**, the Mode 7 repo-access clause. One clause plus a version
   bump, wording already proposed in the ledger and awaiting Tony's word.
   Smallest thing on the board.
2. **L-277's decision, then its patch.** It is the difference between
   remembering a rule four more times and not needing to.
3. **L-254 solar**, the fourteen in `solar_visualization_shells.py`. The
   only remaining slice the current artifact reaches. Note that solar has
   four LIVE builders that do not match `create_*_shell`
   (`galactic_tide`, `hills_cloud_torus`, `outer_oort_clumpy`,
   `streamer_band`), so its dispatch note is not the venus/mars shape.
   And solar holds L-192 sites, so the site store moves with it.

**Not next, but named so it is not lost:** `interactive.html` without the
`?exhibit=sun` parameter still serves the old premade view. The same GUI
should carry it, starting with the Sun as its only object and taking more
as the braid reaches them. Tony raised it 2026-09-02; no ledger item yet.

---

*Session written September 2, 2026 with Anthropic's Claude Opus 5. Built
on orrery `2a3755cf`, gallery `8e5f0bdd`; both confirmed against the live
remote. Seven patches ran and were pushed; none are waiting.*
