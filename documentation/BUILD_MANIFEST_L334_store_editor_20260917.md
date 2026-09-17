# Build Manifest -- L-334, an editor for the rooms' served store

**Built on orrery `9dabda96e289175aaff0e24b377083dace128530`
at https://github.com/tonylquintanilla/palomas_orrery and gallery
`cb1762a74de14785ca2930526cef2c29051b23da`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io. Both
HEADs read live with `ls-remote` on 2026-09-17.**

**Neither HEAD contains the gallery half of L-322 yet.** Two patches
exist, tested, and are not pushed: `patch_L322_5_export_slice_lists_20260917.py`
(orrery) and `patch_L322_6_gallery_half_20260917.py` (gallery). This
plan was written with both patch texts in hand. The build does NOT
start until both are pushed and the gallery's maintenance run has
rewritten `data/objects_config.json` (section 2).

**Type: BUILD CONTRACT.** Written before the build, zero code.
**Prepared:** September 17, 2026 by Claude Fable 5.1, Tony Quintanilla
integrator, in one short design conversation on Tony's phone.
**Continues from** `HANDOFF_L331_rooms_described_L334_editor_20260916.md`
and the L-334 ledger item, whose five design questions this settles.

**Skills this build fires:** interactive-exhibit 1.3 (the page change,
the hover budget, Mode 5 on the phone), gallery-cache-builder 1.4 (the
config and the offline suite), safe-file-editing 1.11 (every patch, and
the editor's own writer), agentic-pre-test 1.2 (every delivered file;
the editor is a Tkinter window, so the headless run applies),
orrery-coding-conventions 1.9 (module docstrings), ledger-and-session-records
1.11 (this document, the ledger note). The build session confirms each
loaded copy matches the protocol's manifest row before starting. This
session loaded ledger-and-session-records 1.11 and interactive-exhibit
1.3, and both matched.

Who this is written for: Tony is a retired professional engineer who
builds this project by conversation with AI partners. He is not a
programmer, runs scripts from VS Code's Run button, and commits and
pushes through GitHub Desktop. The quality of the code in these
repositories is the product of that collaboration, not evidence of a
programmer at the keyboard. Write to him in plain sentences.

---

## 1. What is being built, in one paragraph

A window Tony opens from VS Code's Run button, in the gallery
repository. He picks a room (Sun, Earth), picks a shell, and edits the
words a visitor reads: the name, the hover description, the panel
paragraph, the note, the source text, the link. He also ticks which
shells are drawn when the room opens. Numbers are shown and cannot be
changed. Saving changes only the characters he edited and leaves the
rest of the file byte for byte as it was. A button runs the gallery's
offline checks and shows the verdict. After that the usual loop
applies: commit, push, live run, phone check.

## 2. What must be true before the build starts

1. `patch_L322_5` is run in the orrery, the orrery maintenance run is
   green (16 of 16), and the result is pushed. Tony reports the SHA.
2. `patch_L322_6` is run in the gallery, then
   `python gallery_maintenance_run.py`. That run's Config mirror
   rewrites `data/objects_config.json` (13 unit spellings, 17 figure
   fields). 10 of 10 gating checkers. Pushed. Tony reports the SHA.
3. The build session pulls both repositories at those SHAs and builds
   on them. Every fact in section 4 marked "at `cb1762a7`" is
   re-measured first, because the mirror has touched the file since.

## 3. The rulings this build stands on

**Numbers are locked (Tony, 2026-09-16).** Value, unit, figure count and
the `orrery_constant` link are displayed and not editable. A number
changes in the orrery and arrives through the export and the mirror.

**The file is edited in place (Tony, 2026-09-17, given for the mirror;
applied here as method).** The ledger's question 2 proposed saving with
a plain JSON dump and accepting a one-time reformat of all 900 lines.
L-322's gallery half decided the opposite for the same file, for a
reason that applies equally here: a reformat buries the real change in
a diff nobody can read. So the editor saves the way
`tools/mirror_constants.py` does. It reads the file with the mirror's
own scanner, which records where each value sits, and replaces only
those characters. One reader, shared, so the two tools cannot disagree
about the layout.

**The room opens on the body itself (Tony, 2026-09-17).** His words: "I
am thinking of the arrival scene showing the surface shell plus frame
elements like sun direction, axes, terminator." And on the Moon:
"Exclude the moon with its box not selected." So on arrival:
- the surface shell is drawn (Earth's crust; the Sun's photosphere);
- the frame elements the page builds are drawn (axes and pole in both
  rooms; Sun direction and terminator in Earth's);
- every other shell, and the Moon with its orbit, starts with its
  drawer box unticked, one tap away;
- the opening view fits what is drawn.

**This supersedes Tony's ruling of 2026-08-29** that the Sun's room
opens at a half-width of 0.25 AU with the core through the outer corona
in frame. That ruling is recorded in a comment above
`SUN_HALF_RANGE_AU` in `interactive.html`; the build rewrites the
comment to say what replaced it and when.

**Shell and no preview (method).** Tkinter, opened from the Run button,
the shape of `tools/gallery_studio.py`. No live preview, because the
room only runs in a browser under Pyodide.

## 4. Facts the design rests on, measured at gallery `cb1762a7`

- The page reads `data/objects_config.json` directly at boot. The file
  is 902 lines. Sun and Earth carry features; Jupiter and Saturn carry
  ring and belt blocks with no room yet.
- A shell's editable fields, read from Earth's crust: `name`,
  `description`, `about`, `note`, `source`, `info_url`. Its locked
  fields: `radius` (value, unit, and after the mirror, figures) and
  `orrery_constant`. Drawing choices (`color`, `opacity`, `n_points`,
  `marker_size`) are out of scope for this build; see section 8.
- The page already sizes the opening view to fit whatever is visible,
  times 1.1 (`interactive.html`, the `arrivalR` loop near line 2149).
  It then applies a floor: `Math.max(arrivalR * 1.1, EX.halfRangeAu)`.
  The floors are `SUN_HALF_RANGE_AU = 0.25` and
  `EARTH_HALF_RANGE_AU = 6.155e-5`. At 0.25 AU the Sun alone is about
  one fiftieth of the view's width, so the floor has to go or shrink
  for Tony's arrival scene to work.
- Which shells start hidden is decided today by size, not by a list:
  `feature_renderers.js` (near line 1784) reads `sceneHalfRangeAu` and
  sends any shell larger than that frame to the legend. The hidden
  state is the string `"legendonly"` (`SUN_HIDDEN`), never `false`.
- The hover budget lives in `documentation/smoke_hover_budget.js`:
  desktop lines wrap at 70 characters, the phone's label wraps again at
  34, and the ceiling is 17 lines. The suite measures the BUILT hover,
  which the renderer assembles from the label, the description, the
  radius lines and more. A count of the description field alone is not
  the hover's count.

## 5. The pieces, in build order

**Piece 1 -- the arrival block and its page reader.** Each room's
object in `objects_config.json` gains:

    "arrival": {
      "_declared": "Drawing choices for the opening view, not measurements.",
      "drawn": ["crust"]
    }

`drawn` names shell keys. The page draws those and the frame elements,
and sets everything else, the Moon included, to `"legendonly"`. The
size rule in `feature_renderers.js` stops deciding arrival visibility
when a `drawn` list is present. With no `arrival` block the page
behaves exactly as it does today; that is the fallback and it is
tested. The floor becomes a small per-room minimum or is removed;
decide at the build by trying both on the phone. The block carries no
`orrery_constant`, so the mirror and its two checks ignore it; the
build confirms that by running them. This piece changes what a visitor
sees, so it ships alone and goes to Tony for a phone check of both
rooms before piece 2 starts. It is written into the file by a patch
script, the last hand patch to that file's words.

**Piece 2 -- the shared in-place writer.** A small module that imports
the scanner from `tools/mirror_constants.py` and offers two operations:
replace one string value, and replace one list of strings. It renders
with `json.dumps(..., ensure_ascii=True)`, the way the mirror does,
re-parses the result before writing, and writes nothing if the result
does not parse. It refuses any path that ends in `value`, `unit`,
`figures` or `orrery_constant`. No Tkinter in this module, so its suite
runs headless.

**Piece 3 -- the editor window**, `tools/exhibit_store_editor.py`.
Room list, shell list, a form. Editable fields as text boxes; locked
fields as grey read-only text with the link's store name beside them.
An arrival panel per room: one tick box per shell and one for the
Moon. Save writes through piece 2 and then re-reads the file to show
what is now on disk. Unsaved changes are flagged before switching
shell or closing.

**Piece 4 -- the measure and the checks button.** Beside each hover
field, a live count of that field's own lines at 70 and at 34
characters, labelled as the field's count, not the hover's. The Run
checks button runs `python gallery_maintenance_run.py` offline and
shows the verdict lines, the Hover budget's among them; that is the
real measure, because it builds the hover the visitor sees.

**Piece 5 -- the suite**, wired into the maintenance run as an offline
checker. Section 6.

**Piece 6 -- records.** Module docstrings with run instructions for the
Run button; the gallery README's pipeline section gains the editor;
the interactive-exhibit skill gains a short section on the arrival
block and on who may write the config (the mirror for numbers, the
editor for words, nobody by hand), which is a skill bump with its
protocol entry; the ledger note in section 9.

## 6. What tells us it is working

Each check below names what would make it fail.

- **Open and save with no edit leaves the file identical, byte for
  byte.** Fails if the writer touches anything it was not asked to.
- **Editing one description changes only that string's characters.**
  Checked by diffing before and after. Fails on any other changed byte.
- **A locked field refuses.** The writer is asked to change a `value`,
  a `unit`, a `figures` and an `orrery_constant`; all four must refuse
  and write nothing. Fails if any write lands.
- **After an editor save, the Config mirror check and the Pointer join
  still pass, and they print how many links they compared.** Fails if
  the editor disturbed a number.
- **Awkward text survives a round trip:** a double quote, a backslash,
  an accented character, a very long line. Fails if what is read back
  differs from what was typed, or the file stops being ASCII.
- **The arrival fallback:** with the `arrival` block removed from a
  fixture, the page-side logic gives today's visibility. Fails if the
  old behaviour changed.
- **Built-in fixtures run first, every run,** as in the L-322 checkers,
  so a pass means each refusal path actually ran.
- **Mode 5 on the phone, Tony's eyes,** for piece 1, and once more at
  the end after Tony edits one real hover through the window.

## 7. What is out of scope, and where it goes

- The four page-built hovers and the Moon's (L-331's residue). They are
  built in `earth_geometry.js` and `render_orbits.py`, not served, so
  the editor cannot reach them. Whether they get a served
  `description` is still Tony's to decide, on L-331.
- Jupiter's and Saturn's blocks. No room, no served names (L-231).
- The static gallery's Studio.

## 8. Open, to settle at the build

1. **The floor:** removed, or a small per-room minimum. Tried on the
   phone in piece 1. Tony's eyes decide.
2. **Whether colours and opacity are editable.** They are drawing
   choices, not provenance, and Tony is an artist; they were not in his
   list on 2026-09-16. Not built unless he asks.
3. **Whether the frame elements get tick boxes too.** Tony described
   them as part of the arrival scene, so this plan draws them always.

## 9. Ledger text for the build session to apply

No ledger patch was cut this session, because the unpushed
`patch_L322_5` fingerprints the ledger and a second patch against the
same HEAD would make one of the two refuse. The build session adds
this to L-334, above its Gap line, and rewrites the Gap:

> **Questions 2 to 5 SETTLED, Tony, 2026-09-17.** (2) The file is
> edited in place with the mirror's scanner, not dumped; L-322's
> decision for the same file, applied as method. (3) The arrival block
> holds a `drawn` list only. Tony: the room opens on "the surface shell
> plus frame elements like sun direction, axes, terminator", and
> "exclude the moon with its box not selected." The view fits what is
> drawn; the 0.25 AU ruling of 2026-08-29 is superseded. (4) A
> per-field line count, and a button that runs the offline checks,
> whose Hover budget is the real measure. (5) Tkinter from the Run
> button. Contract:
> `documentation/BUILD_MANIFEST_L334_store_editor_20260917.md`.
>
> **Gap:** push L-322's two patches; then pieces 1 to 6 of the
> manifest, piece 1 to Tony's phone before piece 2 starts.

## 10. Tony-action rollup

1. **(do)** Save this file to the orrery's `documentation/`.
2. **(do)** Run and push `patch_L322_5` (orrery), then `patch_L322_6`
   and the maintenance run (gallery). Report both SHAs.
3. **(decide, at the build)** the three items in section 8.

---

Written September 17, 2026 with Anthropic's Claude Fable 5.1.
