# Gallery card pass -- run record: every card looked at, what was changed, what was found

Built on gallery `1a12cadedf49fcc959a67ceb52fcb7916741d5c8`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
and orrery `60d3578723c6b60d1f0c779853fd8e0ea2a20e63`
at https://github.com/tonylquintanilla/palomas_orrery (read, not changed).
Both HEADs read live with `git ls-remote` on 2026-09-22 for this copy.
The record was started on gallery `386a44ff` and orrery `dcc36e38`, and
the pass itself began earlier the same day on gallery `1ae9de50` and
orrery `efd2e2ba`.

**Type: RUN RECORD, kept open.** Begun September 22, 2026, Tony with
Anthropic's Claude. It is rewritten as each card is finished, and each
new copy replaces the last. It closes when the last card is done, and the
ledger patch that follows it is written from section 5.

**Rules this work ran under**, each loaded in this session and each
matching the protocol's manifest table at v3.67: safe-file-editing 1.11,
gallery-pipeline 1.2, ledger-and-session-records 1.11.

**Where the earlier part comes from.** Sections 2 and 3 up to the refusal
were done in the previous session ("Gallery editor card cleanup and
layout fixes"). Its running notes lived in that session's sandbox and are
gone; what is written here was read back from that chat and from the
gallery's commits. It is a claim about that session, not a re-measurement,
except where a line says it was checked here.

---

## 1. What the pass is

Tony goes through the gallery card by card and says what looks wrong.
Each finding is either fixed as a patch, changed by Tony in the gallery
editor, or recorded for the ledger. Tony's eyes are the check: none of the
gallery's gating checks reads what the lists show or where buttons sit.

At gallery `386a44ff` the metadata holds 145 cards, and all 145 are
served (none is in Storage). Three are live rooms with no file: Solar
System Explorer, Solar Structures, and Earth and Moon.

## 2. Card 1 -- Solar System Explorer

**Changed in the editor by Tony**, both checked here against the commits:
its shape from 16:9 to 9:16 (gallery `1ae9de50`), and its Featured flag
turned on (gallery `42fd97dd`).

**Patched:** `patch_L285_explorer_buttons_to_bottom_20260922.py`, built on
`1ae9de50`, moved the Explorer's buttons to the bottom of the screen. It
also hid two pieces of room chrome that had been showing on the Explorer
since 2026-08-31, the "In this scene" button and an empty grey pill, and
tightened the legend so ten planets no longer reach the + button on a
phone. Pushed at gallery `83a72d11`. Tony: "both desktop and phone look
right, as expected."

**Recorded, not fixed:**
- Still crowded on a small phone (375 by 553 pixels, where the legend
  meets the + button by about 32 pixels) and on any phone held sideways,
  where the picture is about 160 pixels tall and Plotly's toolbar covers
  the arrow cross. Sideways was crowded before this patch too.
- Two files in the orrery still describe the old layout: the Nav cluster
  row in `skills/interactive-exhibit/SKILL.md`, which says a button
  holder's corner is set only by `.nav-cross-apart`, and L-285's ledger
  note, which says the Explorer's overlap is open.

## 3. Cards 2 and 3 -- Inner Solar System Animation, the 16:9 and 9:16 pair

**What Tony saw.** The 16:9 card is too compressed on the phone and should
not be offered there. The 9:16 card works on the phone but not on the
desktop, because its hover text only appears through the phone's info
card. The editor has no control to take a card off one device.

**Why.** The two cards were converted on 2026-02-17, before the gallery
linked a figure's two shapes, and their file names share no stem, so
nothing ever linked them. Every trace in the 9:16 file has empty hover
text; the words were moved into a hidden data field for the info card,
and the page wires that card only in Mobile mode.

**Tony's ruling, 2026-09-22:** the Desktop tab lists the 16:9 cards and
the Mobile tab the 9:16 cards. A card with no counterpart in the other
shape, and a live room, list in both. This replaces L-287's rule of
2026-09-05, that every card shows in every mode.

**Patched:** `patch_L303_tab_shows_its_own_shape_20260922.py`. It
rewrites one function in `index.html`, `inCurrentMode()`, which the room
lists, the lobby and the welcome count all read, and it links the two
animation cards to each other in `gallery/gallery_metadata.json`.

**The first cut refused**, built on `83a72d11`. It said BASE MOVED
because it fingerprinted the whole metadata file, and Tony's two editor
saves in between (section 2) had changed it. Neither save touched the
lines the patch edits. The second cut, built on `386a44ff`, checks the
metadata only for what the patch needs, keeps the whole-file check on
`index.html`, works out the tab counts when it runs, and says so plainly
if it has already been applied. Tested here on copies of both files, with
LF and with Windows line endings plus a further editor save: it applied,
and the only metadata change was the two new link lines. A second run
refused, saying it had already been applied.

**What the site should show after the push**, computed here from the
metadata at `386a44ff`: 104 exhibits in each tab, where both show 145
today. What leaves Desktop is the 41 portrait twins, and what leaves
Mobile is their 41 landscape partners. 46 landscape-only cards, 14
portrait-only cards and the 3 live rooms stay in both. The Featured strip
shows 5 cards in each tab; the previous session said 4, before Tony
featured the Explorer.

**Done.** Pushed at gallery `2a80a68c`. Checked here at that commit:
`index.html` holds the new `inCurrentMode()`, and the two animation
cards name each other in the metadata. Tony's run of the patch, his
maintenance runs and what he saw are in the Tony section below: 15 of 15
offline checks and 2 of 2 live checks passed, and all four things step 5
asked him to look at were as expected (104 in each tab, 5 Featured cards
in each, the animation once per tab in its own shape, and the 16:9
animation gone from the phone).

**Tony's observation from the same look:** the tab split does not show
on the front page. It appears only once a visitor opens one of the three
doors. Tony adds that this points to a gap in the front page, and that
the guest book is still under construction. Recorded in section 5; no
ruling yet on what the front page should do.

## 3a. Card 4 -- Inner Solar System (the static 9:16 view of 2005-02-04)

**Deleted by Tony in the editor**, at gallery `1a12cade`. Card
`paloma_social_view_2005_02_04`, portrait only, no twin, one of the
cards whose desktop hover box was empty. The metadata now holds 144
cards. Computed here from the metadata at `1a12cade`: 103 exhibits in
each tab, 5 Featured in each.

Its file, `gallery/paloma_social_view_2005_02_04.json`, is still in the
repo. No card points at it, so no list shows it, but it is still on the
site at its own address. Recorded in section 5.

## 3b. Housekeeping done alongside

Tony moved twelve documents out of the gallery's `documentation/` and
into the orrery's (gallery `2a80a68c`, orrery `cb254b01`). Checked here:
all twelve are in the orrery, each identical to the gallery copy apart
from line endings. They are 3d_axis_control_handoff,
AS_BUILT_L173_numbering_fix, HANDOFF_earth_build_order_20260906,
M2_IMPLEMENTATION_REPORT, PREDESIGN_earth_exhibit_20260906,
SIZING_earth_moon_lagrange_20260907, TEST_PROTOCOL_mode5_pre_earth_20260906,
TEST_PROTOCOL_sun_hang_20260902, flyto_mobile_handoff,
gallery_subcategory_handoff, index_transform_audit and
non_destructive_routing_handoff. The spent tab patch was filed in the
orrery's `documentation/` too, where the patch said the gallery's.

## 4. Cards still to look at

The rest of the 145. Each gets a section here as it is done.

## 5. For the ledger, one row per class

Each of these is a kind of problem, not a single instance. None has a
ledger handle yet; the ledger patch at the end of the pass assigns them.

- **Hover text kept only in the hidden data field, so a desktop hover box
  is empty.** The previous session counted 20 served files, 14 portrait
  and 6 landscape, not re-measured here. Twelve of the portrait files had
  no landscape twin: 3D Stars to 20 light years; 3D Stars to Visual
  Magnitude 4.0; Paleoclimage and Extreme Heating Events (in two rooms);
  Earth-Moon System 2026-02-10; Inner Solar System Animation; Inner Solar
  System; Pluto System Barycenter; Voyager 1 and 2 Missions; Jupiter
  System; Near Earth Asteroids; Current Comets 2-10-2026. Since then
  Inner Solar System Animation has its twin and has left the Desktop tab
  (section 3), and Inner Solar System has been deleted (section 3a), so
  ten stay on the desktop with empty hover boxes. The
  six landscape files show an empty box on the desktop: Paleoclimate 540
  Ma; Orbital Transformation of Mercury; HR Diagram Magnitude 4.0;
  Paleoclimate Human Origins; Paleoclimate and Extreme Heating Events (two).
- **The front page does not show the tab split** (Tony, section 3). It
  appears only inside a door. Tony links it to a wider gap in the front
  page; the guest book is L-281, still open.
- **Deleting a card in the editor leaves its file behind.** The file
  is unlisted but still served at its own address (section 3a).
- **The editor cannot link or unlink a card's twin.** Any other pair made
  before the linking existed needs a metadata patch, as this one did.
- **Nothing checks which cards each tab lists, or where the room buttons
  sit.** Both changes in this pass are checked only by Tony looking.
- **A patch that fingerprints a whole file the editor saves refuses on
  any save.** safe-file-editing already has this rule; its examples name
  the ledger's index and the protocol's skill table, not the gallery
  metadata. A candidate field note for that skill.
- **Files quoting a layout or a rule this pass changed** (The Correction
  Does Not Travel): the interactive-exhibit Nav cluster row and L-285's
  note (section 2), and the ledger's L-286 and L-287 text on the mode
  rule, which the tab ruling replaces.

---

Record started September 2026 with Anthropic's Claude Opus 5.5, and
updated the same day after cards 2 to 4.

============================
**Tony**:

Card 1, after the push to 83a72d11: "both desktop and phone look right,
as expected. thanks! head is at 83a72d11523c417027d0a325bb0f2531256bd0b4"

Cards 2 and 3, the tab patch (second cut): your run output and what both
tabs show go here.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L303_tab_shows_its_own_shape_20260922.py
  ok  index.html: header Updated stamp
  ok  index.html: the note above treeRank points at the new rule
  ok  index.html: inCurrentMode() lists the tab's own shape
  ok  index.html: renderNavList's note matches
note: gallery/gallery_metadata.json is CRLF here; compared normalised, written back
      CRLF exactly as found.
  ok  metadata: the 16:9 animation card names its 9:16 twin
  ok  metadata: the 9:16 animation card names its 16:9 twin
  ok  encoding gate: inserted text is ASCII, and neither file
      holds a non-ASCII byte.
  ok  metadata parses, and the two cards name each other
  wrote index.html (162633 bytes)
  wrote gallery/gallery_metadata.json (81063 bytes) [CRLF, as found]

patch applied to 2 file(s)

Stamps updated: the 'Updated' line at the top of index.html.
gallery_metadata.json's 'last_updated' is the editor's to set and
is left alone; no card was added, removed or moved.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into documentation/. It has run. -- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect every gating checker to pass, as before. None of them
     reads the card lists, so a pass does not speak for this
     change; your eyes in step 5 do.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              0.9s  no change to MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.5s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite       9.3s  PASS (201 checks, 0 failures)
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        3.2s  All 245 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 246 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 58 link(s) compared, store
                                    7fb7a1b666d4.
  PASS Pointer join              0.1s  Every link is accounted for: 87
                                    link(s) against orrery dcc36e38,
                                    24 fallback named; read check: 41
                                    of 41 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.1s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 55 hover(s) and 267
                                    number(s) examined; 12 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 sibling(s), none stale,
                                    and nothing in data/ the builder
                                    did not make. The sweep is keeping
                                    up.

======================================================================
  15 of 15 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 sibling(s), none stale, and
  last swap 2026-09-22T23:33:39.924967+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop the change list should show exactly three
     files: index.html, gallery/gallery_metadata.json, and this
     script under documentation/. Commit and push.

gallery moved to 2a80a68c6db57414757d372f424b77162bf4b2db
orrery moved to cb254b0163317509a82a647e5b0bfdc54c171d6c

  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 11 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy

  PASS Served reachability       1.4s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at dcc36e38

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at dcc36e38, byte for byte

  orrery HEAD cb254b01
  examining 29 of 87 links; the other 58 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Earth']            not a top-level constant in the store
                  /objects/1/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  29 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 5 could not be examined.

  PASS Store drift               0.8s  29 pointers against orrery
                                    cb254b01 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 5 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            29 pointers against orrery cb254b01 --
  last swap 2026-09-22T23:33:39.924967+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. Open https://palomasorrery.com/ on the desktop and look at
     both tabs. Desktop should list 104 exhibits and Mobile 104,
     where both said 145 before; the welcome line carries the
     count. (These numbers were worked out just now from your
     metadata, so a card you edit later can change them.)
-- correct. although it is noted that the front page is not yet divided into desktop and mobile. that happens only when opening one of the three doors. 
-- this points to a gap in the front page. the guest book is under construction. 

     The Featured strip should show 5 cards on Desktop and 5 on
     Mobile. -- correct
     
     Inner Solar System Animation should appear once in
     each, the 16:9 view on Desktop and the 9:16 on Mobile. -- correct
     
     On the phone the 16:9 animation card should now be gone --
     that is the other half of this patch -- and nothing else
     there should have changed. -- correct

  6. Tell Claude the new gallery SHA and what you saw: 1a12cadedf49fcc959a67ceb52fcb7916741d5c8
  -- in addition to the checks, i deleted the static inner solar system visualization.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 6 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

====================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L303_phone_setting_and_turn_card_20260922.py
  ok  index.html: header Updated stamp
  ok  index.html: style for the turn-the-phone card
  ok  index.html: the phone leaves out a card set to none
  ok  index.html: turnWanted() beside sweepWanted()
  ok  index.html: the loader holds a 3D landscape figure on an upright phone
  ok  index.html: rotation redraws when the answer changes
  ok  editor: docstring stamp
  ok  editor: the shape values
  ok  editor: a helper that reads whether a card's landscape figure is 3D
  ok  editor: the phone setting in the card form
  ok  editor: saving maps the two 16:9 choices to one value
  ok  converter: docstring stamp
  ok  converter: a re-export keeps shape none
  ok  sweep report: the rule list
  ok  sweep report: docstring stamp
  ok  sweep report: shape none is its own class
  ok  sweep report: the 3D class names what the phone does
  ok  sweep report: the class order
  ok  encoding gate: inserted text is ASCII, and no file holds
      a non-ASCII byte.
  ok  the three Python files compile after the edit
  wrote index.html (167803 bytes)
  wrote tools/gallery_editor.py (55703 bytes)
  wrote tools/json_converter.py (36327 bytes)
  wrote tools/sweep_report.py (7282 bytes)

patch applied to 4 file(s)

Stamps updated: the 'Updated' line at the top of index.html and the
'Module updated' line in each of the three tools.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into documentation/. It has run. -- run and stored 9/23/26
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect every gating checker to pass, as before. None of them
     opens a card on a phone, so a pass does not speak for this
     change; your eyes in step 7 do.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.5s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.3s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      13.9s  PASS (201 checks, 0 failures)
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        4.2s  All 245 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 246 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 58 link(s) compared, store
                                    7fb7a1b666d4.
  PASS Pointer join              0.1s  Every link is accounted for: 87
                                    link(s) against orrery 751aff3f,
                                    24 fallback named; read check: 41
                                    of 41 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         1.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.2s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.3s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.3s  === PASS: 55 hover(s) and 267
                                    number(s) examined; 12 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.3s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 sibling(s), none stale,
                                    and nothing in data/ the builder
                                    did not make. The sweep is keeping
                                    up.

======================================================================
  15 of 15 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 sibling(s), none stale, and
  last swap 2026-09-23T13:09:46.835195+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop the change list should show exactly five
     files: index.html, the three tools, and this script under
     documentation/. Commit and push.
-- gallery moved to 4c20194a69f6cb57ff19a33ffa2f64a320fd8a41
--

  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live
  5. Open the gallery editor (tools/gallery_editor.py, Run) and click
     the Mercury card. 'Shape (phone only)' should show four
     choices, with '16:9 3D' picked and '16:9 2D' greyed out.
  6. Pick 'none', Save All, then commit and push
     gallery/gallery_metadata.json.
  7. On the phone, held upright:
       - Orbital Mechanics should no longer list the Mercury card.
       - Open Trappist1 Exoplanet System. It should show its title
         and 'Turn your phone to landscape to view this card.'
         Turn the phone: the figure is drawn. Turn it back: the
         card returns.
       - A 2D card should sweep sideways as before, and a 9:16 card
         should look as before.
     On the desktop, both tabs should look as before, Mercury
     included.
  8. Tell Claude the new gallery SHA and what you saw.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 8 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 