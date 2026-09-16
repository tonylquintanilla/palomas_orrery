#!/usr/bin/env python3
"""
patch_L332_1_skills_protocol_generators_20260916.py -- ORRERY repo.

Run: save this file in the ORRERY repo root (next to PROJECT_INSTRUCTIONS.md),
open it in VS Code and click Run.  Or:  python patch_L332_1_skills_protocol_generators_20260916.py

Built on orrery d99d8db1d3bac407e1d3891b9c6b016d839898c7
at https://github.com/tonylquintanilla/palomas_orrery
(gallery facts read at b375cfe1dd9901a133d7a811f6ccba0d48167975
at https://github.com/tonylquintanilla/tonyquintanilla.github.io).

WHAT IT DOES (nine files, all-or-nothing):

  L-332  skills/interactive-exhibit/SKILL.md          1.2 -> 1.3
         Carries the phone chrome of 2026-09-15/16: the arrow cross's
         corner is set by crossApart / .nav-cross-apart; the drawer row's
         finger-sized target and GO ticking an unticked shell; soft line
         breaks; the phone's text box without an arrow, mid-view; the
         phone tap that reaches a marker; the hover budget suite; and
         Tony's standing rule that a hover is written for the visitor.
  L-331  skills/orrery-coding-conventions/SKILL.md    1.8 -> 1.9
         One new section, Hover Text Is Written for the Visitor: Tony's
         rule of 2026-09-16 ("In general we should avoid compressed
         language in the hovertext"), which reaches the orrery's own
         hovers next (L-321).
  v3.60  PROJECT_INSTRUCTIONS.md gains the version-history entry naming
         both bumps and why; header stamp and SHA anchor move with it;
         the v3.57 entry moves down into
         documentation/PROJECT_INSTRUCTIONS_HISTORY.md to keep three
         resident.
  L-273  module_atlas.py, provenance_scanner.py, data_inventory.py,
         worksheet_checker.py each emit a Doc-Kind: generated tag as the
         first line of the file they write, so doc_index.py stops listing
         MODULE_ATLAS.md, MODULE_INDEX.md, PROVENANCE_AUDIT.md,
         DATA_INVENTORY.md and WORKSHEET_CHECK.md as untagged. Their
         module docstrings are stamped. provenance_scanner.py's docstring
         also has its L-214 stamp moved out of the middle of the Task 2a
         sentence it had been inserted into (fixed in passing; a ruled
         convention, the file already open, mechanical).

WHAT IS PERMANENT: everything above. The script itself is one-shot.

THEN (Tony):
  1. python skills_index.py          (expect: manifest rows read 1.3 and
                                      1.9; it prints what they read before)
  2. the orrery maintenance run, so the five generated files pick up
     their tag and README.md's document table stops saying untagged.
  3. Reinstall interactive-exhibit and orrery-coding-conventions at
     Settings > Skills. The session that installs cannot verify it; the
     next session confirms 1.3 and 1.9 loaded before exhibit or hover
     work.
  4. Commit SKILL.md x2, PROJECT_INSTRUCTIONS.md, the history file, the
     four generators and the regenerated outputs TOGETHER (the four-step
     rule: a bump is one commit).

The guard on PROJECT_INSTRUCTIONS.md hashes the content OUTSIDE the
SKILL-MANIFEST zone, because skills_index.py rewrites that zone.

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# (path, md5 of LF-normalised content with generated zones removed, [zone markers])
FILES = {
    'skills/interactive-exhibit/SKILL.md': ('397e12a82e4ea66283f1f632f274de21', None),
    'skills/orrery-coding-conventions/SKILL.md': ('992c575b486c6e10e83e57018210b3f4', None),
    'PROJECT_INSTRUCTIONS.md': ('742f0e45f468bff750b6803ff24d63d3', (b'<!-- SKILL-MANIFEST:START', b'<!-- SKILL-MANIFEST:END -->')),
    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': ('dbb4773af1198140670f5e86ecd76176', None),
    'module_atlas.py': ('2b5b371b04ce3f3d8fd25c4a81865592', None),
    'provenance_scanner.py': ('692d7a5267e75a1e47bb8f8f0109909a', None),
    'data_inventory.py': ('44a4b60085732088a42f4001a784644e', None),
    'worksheet_checker.py': ('9021f1ac59389b7325c7b7a6377edd15', None),
}

EDITS = {}

# ----------------------------------------------------------------------
# skills/interactive-exhibit/SKILL.md  1.2 -> 1.3
# ----------------------------------------------------------------------
EDITS['skills/interactive-exhibit/SKILL.md'] = [
(b"""Skill version: 1.2 | Cut from gallery @ 9c056d1a (interactive.html,
gallery/nav_cluster.js, gallery/feature_renderers.js) and orrery @
1fa413d9 (LEDGER_CONSOLIDATED.md L-310, L-316, L-317, L-318, L-320)
| 2026-09-11, with Anthropic's Claude Opus 5
v1.2 (L-316, L-318) records what the chrome gained after Tony's phone:
""",
b"""Skill version: 1.3 | Cut from gallery @ b375cfe1 (interactive.html,
gallery/nav_cluster.js, gallery/feature_renderers.js,
documentation/smoke_hover_budget.js) and orrery @ d99d8db1
(LEDGER_CONSOLIDATED.md L-316, L-318, L-331, L-332) | 2026-09-16, with
Anthropic's Claude Opus 5
v1.3 (L-332) carries the phone chrome as six rounds on Tony's phone left
it on 2026-09-15/16 (L-316 rounds 3 and 4, L-318 rounds 3 to 6). The
arrow cross's corner is set by one CSS rule and the method that moves it
says nothing about the corner; a drawer row has a finger-sized selection
target and GO on an unticked shell ticks it, amending L-267's G2 in that
one case; a line break inside a sentence is soft and the phone rejoins
it; on a portrait phone the text box has no arrow and sits mid-view; and
a phone tap reaches a shell's marker rather than its dots, through a
second Plotly rule read from v2.35.2. Step 4 gains the hover budget
suite. One new rule: hover text is written for the visitor -- Tony's
standing rule of 2026-09-16, the Register Rule pointed at what a visitor
reads (L-331). Version 1.2 described the chrome as rounds 1 and 2 left
it, which was five rounds stale when this was cut.
Earlier: v1.2 (L-316, L-318) records what the chrome gained after Tony's phone:
"""),

(b"""| Drawer replacing the legend: rows from `legendgroup`, `legendonly` hides, All / none, focus row; naming a DRAWN shell also opens its hover text as a scene annotation pinned to its info marker, closed by a tap in the scene or by unticking (L-318) | `buildSunDrawer`, `sunApplyVisibility`, `sunFocusOn`, `sunLabelShow`, `sunLabelInstall` | shared |
""",
b"""| Drawer replacing the legend: rows from `legendgroup`, `legendonly` hides, All / none, focus row. A row's whole left end -- edge, box and colour dot, the full row height, about 65 px -- ticks and unticks; rows are at least 44 px tall; the name or GO on an UNTICKED shell ticks it and then frames it (L-318 round 3, amending L-267's G2 in that one case; GO still never hides anything). Naming a DRAWN shell also opens its hover text as a text box: on the desktop and a landscape phone a scene annotation pinned to its info marker with an arrow; on a portrait phone (`sunPhonePortrait()`) a page annotation centred in the view with no arrow, same text and width (L-318 round 5). A tap in the scene, on the box, or on the backdrop closes it; the backdrop also closes the drawer; unticking closes it too (L-318) | `buildSunDrawer`, `sunApplyVisibility`, `sunFocusOn`, `sunLabelShow`, `sunLabelInstall`, `sunPhonePortrait`; knobs `SUN_LABEL_WRAP_CHARS` (34), `SUN_LABEL_PHONE_X` / `_Y` (0.5), `SUN_LABEL_FONT_PX` (12) | shared |
"""),

(b"""on a portrait phone 768 px or narrower the arrow cross moves to the top-right corner, which the hidden mode bar leaves free, and the in-frame title stays (L-316) | gallery/nav_cluster.js (`crossRight`), `navFrameZoom`, `navHome`, `navCameraStep`, `sunCrossRight`, `navPlaceCross` | shared |
""",
b"""on a portrait phone 768 px or narrower the arrow cross, Home with it, moves apart from + and - into its own holder, and the in-frame title stays (L-316). WHICH corner is set only by the `.nav-cross-apart` CSS rule in `nav_cluster.js` -- top right since round 4, after a round at the bottom left -- and the method that moves it, `crossApart(on)`, says nothing about the corner, so the next move is one CSS edit. The open drawer hides the cluster and the holder both. The page decides WHEN: `navPlaceCross()` asks `sunPhonePortrait()`, the same test the text box uses | gallery/nav_cluster.js (`crossApart`, `.nav-cross-apart`), `navFrameZoom`, `navHome`, `navCameraStep`, `navPlaceCross`, `sunPhonePortrait` | shared |
"""),

(b"""a tap turns the same slice of screen at any zoom); drawer (a hidden
shell draws and the view rescales to hold it); a shell NAME (focus, the
i-panel, and the label pinned to that shell's marker); a shell tap
(focus, i-panel, link); the HUD note (hover on desktop, tap on phone); Gallery
button then browser back; then landscape; then desktop. Report each
""",
b"""a tap turns the same slice of screen at any zoom); drawer (the row's
left end ticks on the first try; a hidden shell draws and the view
rescales to hold it; GO on an unticked shell ticks and frames it); a
shell NAME (focus, the i-panel, and its text box -- mid-view with no
arrow on a portrait phone, pinned to the marker elsewhere; the whole box
on screen; sentences unbroken); a MARKER tap (opens on the first tap; a
tap on empty space closes the box); the HUD note (hover on desktop, tap
on phone); Gallery button then browser back; then landscape; then
desktop, where the text box and the tap are as they were. Report each
"""),

(b"""phone loses the line tying it to its marker, and whether it does depends
on where the marker sits, not on how much room there is. Wrap narrower,
or pin a scene annotation, which always points. (L-318.)
""",
b"""phone loses the line tying it to its marker, and whether it does depends
on where the marker sits, not on how much room there is. Wrap narrower,
or pin a scene annotation, which always points. (L-318.) Since round 5
the portrait phone's text box is a page annotation with no arrow at all,
on Tony's word ("very useful but not indispensable"); the desktop keeps
the pinned label. Plotly's OWN hover box on a marker tap still follows
this rule and Tony saw no problem with it once taps landed.

**A line break inside a sentence is soft.** Hover text is wrapped twice
-- at `HOVER_WIDTH` (70) for the desktop box and again at
`SUN_LABEL_WRAP_CHARS` (34) for the phone's text box -- so a hard `<br>`
that only keeps a desktop line short leaves an orphan word on the phone.
Write it as `GalleryFeatures.SOFT_BR` (`<br soft>`): Plotly draws it as
a break, because its text splitter reads a tag's name only up to the
first space (`src/lib/svg_text_utils.js`), and the phone's wrapper turns
it back into a space. A hard `<br>` stays for paragraph and list breaks.
`documentation/smoke_hover_budget.js` fails on a hard break inside a
sentence. (L-318 round 4.)

**A 3D tap takes the nearest drawn point from EVERY trace.** gl-plot3d
picks the point nearest the finger within `pickRadius` (10 px, set in
`src/plots/gl3d/scene.js`) across all traces, and only afterwards does
scene.js drop a pick whose trace has hoverinfo `skip` -- so a shell's
text-less dots win over its one info marker. On a portrait phone only,
`sunTapPicking(gd)` makes text-less traces draw nothing into the pick
buffer and widens the search to `SUN_PICK_RADIUS_PX` (22). It reaches
into `gd._fullLayout.scene._scene` (`glplot.pickRadius`, `glplot.update`,
each object's `drawPick`), is re-applied after every plot, and does
nothing if those are not where 2.35.2 keeps them. The desktop is
untouched: "the mouse pointer is fine enough to pick out the marker"
(Tony). (L-318 round 6; Tony: "always opens on first tap.")

### Hover text is written for the visitor [QUALITY]
Tony's standing rule, 2026-09-16: "In general we should avoid compressed
language in the hovertext." It is the protocol's Register Rule -- which
governs how Claude writes to Tony -- applied to what a visitor reads.
A hover names the thing and says it plainly. Project vocabulary
("served", "sourced", "drawing choice", "trusted arc", "L shell") and
capitalised labels ("DECLARED", "A DRAWING LIMIT", "FROZEN") are
compression: a visitor has not been through the conversation that gave
them meaning. The rule changes the WORDS, not the facts or the caveats.
A caveat stays beside its number, in words a visitor can use -- "It is
not a measured distance" rather than "DECLARED -- ... Not a measurement."
Citations, equations and served caveats live in the i panel, with one
pointer line under each hover (L-231); the hover is the glance. Reworded
hovers go to Tony before they ship. (L-331; the orrery's own hovers
follow under orrery-coding-conventions 1.9 and L-321.)
"""),

(b"""4. Pre-test here: `node --check` on the page script; a stand-in scene
   for chrome that can run without Pyodide (the CDN is blocked in the
   sandbox, so the exhibit itself cannot start here -- say so in the
   handoff).
""",
b"""4. Pre-test here: `node --check` on the page script; a stand-in scene
   for chrome that can run without Pyodide (the CDN is blocked in the
   sandbox, so the exhibit itself cannot start here -- say so in the
   handoff); and `documentation/smoke_hover_budget.js`, given
   `interactive.html` as well as the renderers, which counts each
   hover's lines (soft breaks count; hard breaks inside sentences fail),
   holds every hover under `CEILING` (17, a ratchet that only comes
   down), measures the phone's text boxes with the page's own wrapper,
   and checks that each hover points at the i panel. It builds the Earth
   scene, Jupiter and Saturn; at b375cfe1 it does NOT build the Sun
   room, and four Sun hovers missed the move to the panel because of it
   (L-331). A checker passes on what it does not look at: when adding a
   room, add it to this suite before trusting its green.
"""),

(b"""1.0 was confirmed by the Earth sessions; the first session after 1.1's
push confirms its loaded copy reads 1.1 before exhibit work.
""",
b"""1.0 was confirmed by the Earth sessions; 1.1 and 1.2 by the sessions
that followed their pushes. The first session after 1.3's push confirms
its loaded copy reads 1.3 before exhibit work.
"""),

(b"""  DESKTOP lobby while the phone showed it. The handoff written the
  night before said step 7 had not started: its session never read the
  metadata. A replay of the viewer's rule against the served metadata
  predicted both screens before Tony looked, and was right. Fixed by
  delete, then Studio, then the editor, in that order. The editor's
  Reload from disk existed and was not found either (L-288, L-312).
""",
b"""  DESKTOP lobby while the phone showed it. The handoff written the
  night before said step 7 had not started: its session never read the
  metadata. A replay of the viewer's rule against the served metadata
  predicted both screens before Tony looked, and was right. Fixed by
  delete, then Studio, then the editor, in that order. The editor's
  Reload from disk existed and was not found either (L-288, L-312).
- 2026-09-15, L-318 round 3: a drawer row had two targets, an 18 px box
  and a name that did what GO did, and Tony's finger kept landing on
  the name of an unticked shell -- the camera moved and nothing drew, a
  tap that read as doing nothing. Measured in the page before any
  design: every pixel around the box belonged to the name. A one-target
  row with no box was proposed and withdrawn once Tony described his
  use (tick several, then go to one). Measure before you describe.
- 2026-09-15, L-318 round 4: Tony read the orphan words as unnecessary
  line breaks. Right about the words; measuring showed they cost one or
  two lines per box, and the box's WIDTH was the real height. Line
  counts written into the patch's notes before the run disagreed with
  the run on every row and were corrected before delivery.
- 2026-09-15/16, L-318 rounds 5 and 6: Plotly sometimes drew no arrow
  to a mid-screen box, and why was not pinned down; the arrow was
  removed on the phone instead. The tap fix went the other way -- the
  cause was read from Plotly's source first and worked on the first
  phone test. Three of five rounds changed something after Tony's eyes;
  the sandbox has no WebGL and no phone, and cannot see any of it.
"""),
]

# ----------------------------------------------------------------------
# skills/orrery-coding-conventions/SKILL.md  1.8 -> 1.9
# ----------------------------------------------------------------------
EDITS['skills/orrery-coding-conventions/SKILL.md'] = [
(b"""Skill version: 1.8 | Cut from palomas_orrery @ 1fa413d9 (v1.8),
earlier @ 04bba3ca (v1.7), 3faa72a0 (v1.6),
earlier @ 15741822 (v1.5), 86f529a (v1.4), 3398970 (v1.3) | 2026-09-11
v1.8 (L-317) adds Two Standards for the Info Marker's Outline -- Tony's
""",
b"""Skill version: 1.9 | Cut from palomas_orrery @ d99d8db1 (v1.9),
earlier @ 1fa413d9 (v1.8), 04bba3ca (v1.7), 3faa72a0 (v1.6),
earlier @ 15741822 (v1.5), 86f529a (v1.4), 3398970 (v1.3) | 2026-09-16
v1.9 (L-331) adds Hover Text Is Written for the Visitor -- Tony's
standing rule of 2026-09-16, "In general we should avoid compressed
language in the hovertext." It was ruled over the gallery's hovers and
reaches the orrery's own next (L-321); a convention that is not in the
skill does not travel, and this is the skill a hover session loads.
v1.8 (L-317) adds Two Standards for the Info Marker's Outline -- Tony's
"""),

(b"""## Layer Chain Gap Handling [PRACTICE]
""",
b"""## Hover Text Is Written for the Visitor [QUALITY]

The two sections above govern a hover's BREAKS. This one governs its
WORDS.

**Tony's standing rule, 2026-09-16: "In general we should avoid
compressed language in the hovertext."** It is the resident protocol's
Register Rule -- which governs how Claude writes to Tony -- applied to
the person reading the plot. A visitor has not been through the
conversation that gave a project word its meaning, so to them it is a
label pointing at nothing.

Compression, in a hover, is any of these:
- project vocabulary: "served", "sourced", "trusted arc", "drawing
  choice", "illustrative", "osculating" without a gloss, "L shell"
  without saying what it measures;
- a capitalised label standing in for a sentence: "DECLARED --",
  "A DRAWING LIMIT", "FROZEN", "STYLIZED";
- a caveat that names its kind instead of saying what is true: "Not a
  measurement." says less than "It is not a measured distance; the
  ring is drawn here so the picture reads."

**The rule changes the words, not the facts or the caveats.** Every
number keeps its value, unit and AU; every caveat stays beside its
number, in plain words. Show the Envelope of the Unknowable still
applies -- silence about an approximation reads as precision -- so the
plain sentence says that the thing is drawn, chosen or approximate, and
why, in words a visitor can use.

Two things follow. A hover is the glance; the citation, the equation
and the served or sourced detail belong in the i panel (gallery) or the
`_info` text (orrery), with a pointer under the hover -- the L-231 move.
And a reworded hover is a visitor-facing change: it goes to Tony before
it ships, with the old and the new side by side.

(Origin, 2026-09-16, L-331. Tony, on the Sun room's Galactic Tide hover,
which opened "DECLARED --" and closed "Not a measurement.": "declared
not measured means little to a visitor." Counted in the gallery's hovers
the same day: "served" in 14, "sourced", "drawing choice" and
"illustrative" in 5 each, capitalised labels in 4. The orrery's hovers
were not counted; they are where the rule reaches next.)

## Layer Chain Gap Handling [PRACTICE]
"""),
]

# ----------------------------------------------------------------------
# PROJECT_INSTRUCTIONS.md  v3.59 -> v3.60
# ----------------------------------------------------------------------
V360_ENTRY = b"""v3.60 (September 16, 2026): No rule changed in this document. TWO
skill bumps, taken as the session's first action, ahead of the build
they serve.

interactive-exhibit 1.2 -> 1.3 (L-332) and orrery-coding-conventions
1.8 -> 1.9 (L-331).

THE EXHIBIT SKILL WAS FIVE ROUNDS STALE. Version 1.2 was cut on
2026-09-11 and described the rooms' chrome as L-316 round 2 and L-318
rounds 1 and 2 left it. Six more rounds ran on Tony's phone on
2026-09-15/16, each checked before the next was built, and the skill
that fires on any edit to that chrome did not know any of them: the
arrow cross's corner is now one CSS rule; a drawer row has a finger-
sized target and GO ticks an unticked shell; a break inside a sentence
is soft; the portrait phone's text box has no arrow and sits mid-view;
and a phone tap reaches a marker through a second Plotly rule read from
v2.35.2's pick pass. The skill also gains the hover budget suite in its
pre-test step, with the note that the suite does not build the Sun
room -- which is how four Sun hovers missed the move to the i panel
(L-331). A checker passes on what it does not look at.

THE ONE NEW RULE IS TONY'S, and it rides both skills. On 2026-09-16,
reading the Sun room's Galactic Tide hover -- "DECLARED --" at the top,
"Not a measurement." at the bottom -- he said that declared-not-
measured means little to a visitor, and then made it general: "In
general we should avoid compressed language in the hovertext." That is
this document's Register Rule pointed the other way: the Register Rule
governs what Claude writes to Tony; this governs what the plot says to
a visitor, who has been through none of the conversation. It is written
into interactive-exhibit for the gallery's hovers and into
orrery-coding-conventions for the orrery's, because the orrery's hovers
are where it reaches next (L-321), and a convention that is not in the
skill a hover session loads does not travel. The rule changes the
words, not the facts or the caveats; reworded hovers go to Tony first.

THE ORDERING IS v3.55's: the bumps precede L-331's build, so the next
exhibit session's stale-skill gate fires on a matching manifest. The
obligation still travels: this session loaded 1.2 and 1.8, and a
reinstall cannot be verified from inside the session that makes it. The
next session confirms its loaded copies read 1.3 and 1.9 before exhibit
or hover work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.57 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

V357_START = b"""v3.57 (September 11, 2026): No rule changed in this document. THREE
skill bumps, taken together at the close of the 2026-09-10 evening
session and BEFORE the builds they serve.
"""
V357_END = b"""Version history: v3.54 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

Functional for Claude, readable for human, signal preserved.
"""

EDITS['PROJECT_INSTRUCTIONS.md'] = [
(b"""Tony Quintanilla, PE | Claude | v3.59 | September 14, 2026

Cut from 773e5c2d at https://github.com/tonylquintanilla/palomas_orrery
""",
b"""Tony Quintanilla, PE | Claude | v3.60 | September 16, 2026

Cut from d99d8db1 at https://github.com/tonylquintanilla/palomas_orrery
"""),
(b"""v3.59 (September 14, 2026): ONE RULE REWRITTEN, the Register Rule, on
""",
V360_ENTRY + b"""v3.59 (September 14, 2026): ONE RULE REWRITTEN, the Register Rule, on
"""),
# the v3.57 entry is removed as a SPAN (start anchor .. end anchor) below
]

EDITS['documentation/PROJECT_INSTRUCTIONS_HISTORY.md'] = [
(b"""Version history: v3.53 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37
""",
b"""Version history: v3.53 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

@@V357@@

(Moved down from the resident protocol on 2026-09-16 when v3.60
made a fourth entry.)

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37
"""),
]

# ----------------------------------------------------------------------
# L-273: the four generators emit a Doc-Kind tag
# ----------------------------------------------------------------------
STAMP = (b"Module updated: September 16, 2026 with Anthropic's Claude Opus 5 "
         b"(L-273: the output opens with a Doc-Kind: generated tag, read by\n"
         b"doc_index.py; hand-editing the output is an error the tag now names).\n")

EDITS['module_atlas.py'] = [
(b"""    lines.append("# Paloma's Orrery -- Module Atlas")
    lines.append("")
    lines.append(f"Generated: {now}")
""",
b"""    lines.append("<!-- Doc-Kind: generated | The module atlas: every "
                 "module's role, functions and dependencies, rebuilt by "
                 "module_atlas.py from the docstrings. Do not hand-edit. -->")
    lines.append("# Paloma's Orrery -- Module Atlas")
    lines.append("")
    lines.append(f"Generated: {now}")
"""),
(b"""    lines.append("# Paloma's Orrery - Module Index")
    lines.append("")
    lines.append(f"**Generated:** {now} by `module_atlas.py`  ")
""",
b"""    lines.append("<!-- Doc-Kind: generated | The human-browsable module "
                 "index, rebuilt by module_atlas.py alongside the atlas. "
                 "Do not hand-edit. -->")
    lines.append("# Paloma's Orrery - Module Index")
    lines.append("")
    lines.append(f"**Generated:** {now} by `module_atlas.py`  ")
"""),
(b"""with the action named, instead of landing in `undetermined` -- which
had been carrying two unrelated meanings at once.
""",
b"""with the action named, instead of landing in `undetermined` -- which
had been carrying two unrelated meanings at once.

""" + STAMP),
]

EDITS['provenance_scanner.py'] = [
(b"""    out.append("# Paloma's Orrery -- Provenance Audit")
    out.append("")
    out.append(f"Generated: {now}")
""",
b"""    out.append("<!-- Doc-Kind: generated | The provenance audit: every "
               "numeric claim scored against its citation, rebuilt by "
               "provenance_scanner.py on each run. Do not hand-edit. -->")
    out.append("# Paloma's Orrery -- Provenance Audit")
    out.append("")
    out.append(f"Generated: {now}")
"""),
# Fix in passing: the L-214 stamp had been inserted into the middle of the
# Task 2a stamp's sentence. Move it after that paragraph.
(b"""Module updated: August 2026 with Anthropic's Claude Opus 5 (Task 2a:
Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-214).
per-domain split printed under each console tier line;
MODULE_DOMAIN_MAP entries added for orrery_rendering and shell_configs,
and two entries removed for smoke_* files no longer in the repo.
""",
b"""Module updated: August 2026 with Anthropic's Claude Opus 5 (Task 2a:
per-domain split printed under each console tier line;
MODULE_DOMAIN_MAP entries added for orrery_rendering and shell_configs,
and two entries removed for smoke_* files no longer in the repo.
Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-214).
""" + STAMP),
]

EDITS['data_inventory.py'] = [
(b"""        out.write("# Data Inventory (local, gitignored -- CURRENT state)\\n\\n")
""",
b"""        out.write("<!-- Doc-Kind: generated | The data inventory: the "
                  "state of the local, gitignored data stores, rebuilt "
                  "by data_inventory.py. Do not hand-edit. -->\\n")
        out.write("# Data Inventory (local, gitignored -- CURRENT state)\\n\\n")
"""),
(b"""Module updated: July 2026 with Anthropic's Claude Opus 4.6
\"\"\"
""",
b"""Module updated: July 2026 with Anthropic's Claude Opus 4.6
""" + STAMP + b"""\"\"\"
"""),
]

EDITS['worksheet_checker.py'] = [
(b"""    add('# Worksheet Check (L-192)')
    add('')
""",
b"""    add('<!-- Doc-Kind: generated | The worksheet check: every '
        'annotated claim scored against its worksheet evidence, rebuilt '
        'by worksheet_checker.py. Do not hand-edit. -->')
    add('# Worksheet Check (L-192)')
    add('')
"""),
(b"""Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1 (L-277: label regexes now come from worksheet_keys).
\"\"\"
""",
b"""Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1 (L-277: label regexes now come from worksheet_keys).
""" + STAMP + b"""\"\"\"
"""),
]


def lf(data):
    return data.replace(b'\r\n', b'\n')


def fingerprint(content, zone):
    if zone:
        a = content.index(zone[0])
        b = content.index(zone[1]) + len(zone[1])
        content = content[:a] + content[b:]
    return hashlib.md5(content).hexdigest()


def main():
    originals = {}
    results = {}
    # 1. read + guard every file before writing any
    for rel, (fp_expected, zone) in FILES.items():
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print(f'ERROR: {rel} not found next to this script. NOTHING was written.')
            return 1
        raw = open(path, 'rb').read()
        was_crlf = b'\r\n' in raw
        content = lf(raw)
        actual = fingerprint(content, zone)
        if fp_expected != 'PLACEHOLDER' and actual != fp_expected:
            print(f'ERROR: {rel} is not the file this patch was built against')
            print(f'       expected {fp_expected}, found {actual}{" [CRLF]" if was_crlf else ""}')
            print('       NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
            return 1
        originals[rel] = (content, was_crlf, actual)

    # 2. apply edits in memory
    for rel, edits in EDITS.items():
        content, was_crlf, _ = originals[rel]
        for old, new in edits:
            n = content.count(old)
            if n != 1:
                print(f'ANCHOR FAIL: {rel}: expected 1 match, found {n}: {old[:70]!r}')
                print('NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
                return 1
            content = content.replace(old, new)
        results[rel] = content

    # 3. move the v3.57 entry from the protocol into the history file
    proto = results['PROJECT_INSTRUCTIONS.md']
    a = proto.count(V357_START)
    b = proto.count(V357_END)
    if a != 1 or b != 1:
        print(f'ANCHOR FAIL: PROJECT_INSTRUCTIONS.md v3.57 span: start x{a}, end x{b}')
        print('NOTHING was written.')
        return 1
    i = proto.index(V357_START)
    j = proto.index(V357_END) + len(V357_END)
    span = proto[i:j]
    tail = b'\nFunctional for Claude, readable for human, signal preserved.\n'
    assert span.endswith(tail)
    v357 = span[:-len(tail)].rstrip(b'\n') + b'\n'
    results['PROJECT_INSTRUCTIONS.md'] = (proto[:i]
        + b'Functional for Claude, readable for human, signal preserved.\n'
        + proto[j:])
    hist = results['documentation/PROJECT_INSTRUCTIONS_HISTORY.md']
    assert hist.count(b'@@V357@@') == 1
    results['documentation/PROJECT_INSTRUCTIONS_HISTORY.md'] = hist.replace(
        b'@@V357@@\n', v357)

    # 4. encoding gate on what this patch introduces
    for rel, content in results.items():
        bad = [c for c in content if c > 127]
        if bad:
            print(f'ERROR: {rel} would hold {len(bad)} non-ASCII byte(s) after the patch. NOTHING was written.')
            return 1
        if results[rel] == originals[rel][0]:
            print(f'ERROR: {rel} unchanged after edits -- anchors matched but produced no change.')
            return 1

    # 5. write, preserving each file's own line-ending style
    for rel, content in results.items():
        _, was_crlf, _ = originals[rel]
        out = content.replace(b'\n', b'\r\n') if was_crlf else content
        with open(os.path.join(ROOT, rel), 'wb') as f:
            f.write(out)
        print(f'ok  {rel}  ({len(out)} bytes{", CRLF preserved" if was_crlf else ""})')
    print('stamped: skills/interactive-exhibit/SKILL.md (1.3), '
          'skills/orrery-coding-conventions/SKILL.md (1.9), '
          'PROJECT_INSTRUCTIONS.md (v3.60, d99d8db1), '
          'module_atlas.py, provenance_scanner.py, data_inventory.py, '
          'worksheet_checker.py (docstrings)')
    print('note: provenance_scanner.py: the L-214 docstring stamp was moved out '
          'of the middle of the Task 2a sentence, in passing')
    print('patch applied. NEXT: python skills_index.py; then the maintenance run; '
          'then reinstall both skills; commit everything together.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
