#!/usr/bin/env python3
"""
patch_L331_3_ledger_20260916.py -- ORRERY repo, LEDGER_CONSOLIDATED.md only.

Run: save this file in the ORRERY repo root (next to LEDGER_CONSOLIDATED.md),
open it in VS Code and click Run.  Or:  python patch_L331_3_ledger_20260916.py
Then:  python ledger_index.py LEDGER_CONSOLIDATED.md
       (expect OK: 329 L-blocks parsed, no consistency problems -- no
       item closes here, so one run is enough)

Built on orrery bfc1706b8b0f14ce28cee893381ca3d511fea9ce
at https://github.com/tonylquintanilla/palomas_orrery
(gallery at bbf46429df4cccb4b2e0b7305056684081c67334
at https://github.com/tonylquintanilla/tonyquintanilla.github.io).

WHAT IT DOES:
  - Header stamp for this edit.
  - L-331: records the two gallery builds of the afternoon and evening
    and Tony's Mode 5 of both rooms ("correct"); the Gap narrows to what
    is left -- four hovers the page builds itself in earth_geometry.js,
    the Moon's in render_orbits.py, the Galactic Tide's served source
    string -- and the ceiling.
  - L-334 OPENED: an editor for the interactive exhibits' served store,
    Tony's request of 2026-09-16, with the design questions it has to
    settle before a build.

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = 'LEDGER_CONSOLIDATED.md'
EXPECTED = '530ff458e7cdd754ad7154fbfd8c4660'
ZONE = (b'<!-- INDEX:START', b'<!-- INDEX:END -->')

EDITS = [

(b"""above added), built on d99d8db1.
Review and RICE update Tony 6-21-2026
""",
b"""above added), built on d99d8db1.
Module updated: September 16, 2026 with Anthropic's Claude Opus 5
(L-331: both gallery builds recorded, Mode 5 passed in both rooms, Gap
narrowed to the page-built hovers; L-334 opened -- an editor for the
exhibits' served store), built on bfc1706b.
Review and RICE update Tony 6-21-2026
"""),

(b"""**Gap:** Mode 5 on the phone in the Sun room for the four hovers and the
panel, and in both rooms for the info text; then the plain-language pass
over the remaining hovers, wording to Tony first; the ceiling comes down
with the tallest hover.
  **Tony-action (decide):** the four VISITOR_WORDING sentences, by
  running the patch as written or editing them first.
  **Tony-action (decide):** the reworded hovers, starting with the
  Galactic Tide's.
""",
b"""- **SHIPPED 2026-09-16, gallery `744ad578`:** the mechanical half above,
  run by Tony with the four VISITOR_WORDING sentences as written. The
  live run read all eight files SERVED and byte-identical.
- **TONY'S MODE 5 OF `744ad578` FOUND THE REAL GAP.** "It has data but
  no description of what we are looking at. This is information we
  previously had. We cannot assume the visitor knows what they are
  looking at at a basic level." Checked here and true of every hover the
  gallery built, not four: each said a name, a number and the pointer
  line. The orrery's own `*_info` strings say what each thing IS and had
  never crossed into the gallery. Tony ruled the shape: a served
  `description` (one or two plain sentences, in the hover under the
  name) and a served paragraph (in the i panel, above the link), both
  condensed from the orrery's text, which he had already seen and
  approved -- "just go to the patch directly."
- **SHIPPED 2026-09-16, gallery `bbf46429`:**
  `patch_L331_2_what_you_are_looking_at.py`. `data/objects_config.json`:
  32 features and the two belts gain `description` and `about` (the
  panel field is `about`, not `detail`, because `detail` already carries
  the magnetopause's and bow shock's equations); each entry names the
  orrery string it was condensed from. `feature_renderers.js`: every Sun
  and Earth hover opens with the description through `descLine()`;
  `stampLink` carries `about`; the belt, magnetopause and bow shock
  hovers lose "sourced", "drawing choice", "illustrative" and "A DRAWING
  LIMIT". `interactive.html`: the panel shows `about` first.
  `smoke_hover_budget.js` overlays the store's prose onto the Earth
  fixtures so it measures the hovers the page shows;
  `smoke_earth_geometry.js`'s wording pins follow the plain phrases and
  still pin the content (the served tilt with model and epoch, the
  plane, the measured extent, the width caveat, the drawing cut). The
  magnetopause had reached 18 lines with a description on top; its
  flaring-exponent line left for the panel's equations and it is 16.
  The belts' plane-and-tilt sentence was moved to the panel in a first
  draft and put back on the geometry suite's word: the tilt is quoted
  BECAUSE it is served (L-231), and that is content, not vocabulary.
  Ceiling still 17; the tallest hover is still the rotation axis.
  Nightly run, offline run 7 of 7 with the cache builder suite and the
  Artifact 1 pin, live run 8 of 8 SERVED. **Tony, Mode 5, both rooms:
  "correct."** [verified in the sandbox on a throwaway @ `744ad578`;
  render by Tony]
- **What is left, counted in the built hovers at `bbf46429`:** "served"
  in the rotation axis and the Moon; "trusted" and "osculating" in the
  Moon; "FROZEN" in the terminator. Four are the page's own hovers in
  `gallery/earth_geometry.js`, outside the served store; the Moon's is
  the assembler's, `render_orbits.py`, and is L-321's neighbour. The
  Galactic Tide's served `source` string still reads "DECLARED -- ..."
  and shows in the panel's Source line.
**Gap:** the four `earth_geometry.js` hovers and the Moon's, in plain
words, wording to Tony first; the Galactic Tide's served source string;
the ceiling comes down with the tallest hover (17, the rotation axis --
one of the four).
  **Tony-action (decide):** whether the four page-built hovers get their
  own `description` field served too (L-334 would then reach them), or
  are reworded in the page as they are.
"""),

(b"""#### [L-333] The master plan's two companion summaries have not moved since August (planning documents)""",
b"""#### [L-334] An editor for the interactive exhibits' served store (gallery tooling)
<!-- L:334 status:OPEN upd:2026-09-16 section:A flag: rice:4/4/80/4 -->
- **Tony, 2026-09-16, after Mode 5 of both rooms:** "For the static
  gallery we have a Studio editor that edits the html before json
  conversion. Could we do something similar for the interactive
  exhibits, where I can edit features like the hover text, the info
  panel text, the url link, which shells are displayed upon opening, the
  initial view scale, etc." And, on being told the store is
  hand-maintained: "while you say it is hand maintained, you do all the
  maintenance. What I am thinking of is an editor that can serve the
  correct json and allows me to revise certain parameters and text."
- **Why it is the right next build.** The Sun and Earth rooms are done.
  Every visitor-facing word in them now lives in one file,
  `data/objects_config.json` (name, description, about, note, source,
  link, per shell), and that file is edited only through Claude's patch
  scripts. The protocol's Roles section is explicit that Tony owns the
  workflow and every integration judgment; the words a visitor reads
  are his to change without a session. An editor moves that point of
  maintenance to him. It is also where L-331's last residue lands if
  the page-built hovers are served (see that item's Tony-action).
- **The pipeline it sits on** (gallery README, "objects_config.json ->
  gallery_cache_builder.py -> data/solar-system/"): the store is copied
  verbatim by the nightly into the served `feature_configs.json`, and
  `interactive.html` with `gallery/feature_renderers.js` draws what is
  served. So the editor is a form over the store; nothing downstream
  changes for the text fields.
- **Design questions to settle in conversation before a build (Claude's
  proposals, for Tony to redirect):**
  1. WHAT IT MAY EDIT. Prose and links (name, description, about, note,
     source text, info_url), and the arrival settings once served.
     Numbers -- value, unit, orrery_constant -- shown but LOCKED: they
     are the provenance contract, checked by Store drift against the
     orrery's constant store, and an editor that can change them is a
     new way to drift. A number changes in the orrery, then the
     pipeline.
  2. THE FILE'S SHAPE. The store is hand-formatted with `_comment` and
     `_declared` keys. An editor that saves through `json.dump` rewrites
     the whole file in one canonical layout, once; the comment keys are
     data and survive. Proposal: accept the one-time reformat rather
     than build a formatting-preserving writer; every patch after that
     targets the canonical layout.
  3. ARRIVAL SETTINGS ARE NOT SERVED YET. Which shells draw on arrival
     and the arrival scale live in the page (`SUN_HALF_RANGE_AU`, the
     drawer's rule that a shell larger than the frame starts hidden).
     Proposal: an `arrival` block per object -- `half_range_au` and a
     `drawn` list of shell keys -- read by the page, with the current
     behaviour as the default when the block is absent. A small page
     change, and it is what makes those two items editable at all.
  4. NO PREVIEW, BUT A MEASURE. Studio's preview does not carry: the
     room runs on Pyodide in a browser. What can carry is the hover
     budget's arithmetic -- desktop lines at 70 characters, phone lines
     at 34, the ceiling of 17 -- shown beside the field as it is typed,
     and a Run-the-checks button that runs `gallery_maintenance_run.py`
     offline and shows its verdict. That is the check the patches run
     now, put where Tony edits.
  5. THE SHELL. Studio is Tkinter and Tony runs it from VS Code's Run
     button; same here. Pick a body, pick a shell, edit, save, and the
     usual loop after: nightly, offline run, commit, push, live run.
- **Not this item:** the static gallery's Studio (gallery-pipeline);
  Jupiter's and Saturn's rings, which have no room and no served names
  (L-231 for Jupiter).
- **Note:** RICE 4/4/80/4 -> 3.2 is Claude's proposed score, unratified.
  Reach 4 because it changes who can maintain the rooms, not how many
  visitors see them; Effort 4 for the form, the arrival block, the page
  change and a suite that opens and saves the store round-trip.
**Gap:** the five design questions above, in conversation; then the
build, in this order: the arrival block and its page reader (3), the
editor over prose and links (1, 2, 5), the measure and the checks
button (4).
  **Tony-action (decide):** the five questions, starting with 1 --
  whether numbers are locked.
**Ref:** gallery `data/objects_config.json`, `tools/gallery_cache_builder.py`,
`interactive.html` (`SUN_HALF_RANGE_AU`, `EXHIBITS`, `buildSunDrawer`),
`gallery/feature_renderers.js` (`descLine`, `stampLink`);
`tools/gallery_studio.py` (the shape to copy); L-331 (the served prose
this edits), L-267 (the drawer), L-322 (the unit field the locked
numbers would show), gallery-pipeline skill (Studio), interactive-exhibit
skill 1.3 (the provenance contract an exhibit renders under).

#### [L-333] The master plan's two companion summaries have not moved since August (planning documents)"""),
]


def main():
    path = os.path.join(ROOT, TARGET)
    if not os.path.exists(path):
        print(f'ERROR: {TARGET} not found next to this script. NOTHING was written.')
        return 1
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    content = raw.replace(b'\r\n', b'\n')
    a = content.index(ZONE[0])
    b = content.index(ZONE[1]) + len(ZONE[1])
    actual = hashlib.md5(content[:a] + content[b:]).hexdigest()
    if actual != EXPECTED:
        print(f'ERROR: {TARGET} is not the file this patch was built against')
        print(f'       expected {EXPECTED}, found {actual}{" [CRLF]" if was_crlf else ""}')
        print('       (the INDEX zone is excluded from this comparison)')
        print('       NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
        return 1
    new = content
    for old, repl in EDITS:
        n = new.count(old)
        if n != 1:
            print(f'ANCHOR FAIL: expected 1 match, found {n}: {old[:70]!r}')
            print('NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
            return 1
        new = new.replace(old, repl)
    if any(c > 127 for c in new):
        print('ERROR: the result would hold non-ASCII bytes. NOTHING was written.')
        return 1
    out = new.replace(b'\n', b'\r\n') if was_crlf else new
    with open(path, 'wb') as f:
        f.write(out)
    print(f'ok  {TARGET}  ({len(out)} bytes{", CRLF preserved" if was_crlf else ""})')
    print('stamped: header;  L-331 updated;  L-334 opened')
    print('patch applied. NEXT: python ledger_index.py LEDGER_CONSOLIDATED.md (expect OK: 329 blocks)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
