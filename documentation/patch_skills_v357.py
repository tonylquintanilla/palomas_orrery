"""patch_skills_v357.py -- the skill layer of the 2026-09-10 session:
three skill bumps under the four-step rule, plus the ledger_index.py fix
they name.

ORRERY repo (palomas_orrery). Built on orrery 1fa413d9 at
https://github.com/tonylquintanilla/palomas_orrery ; the gallery state
the exhibit skill is cut from is 9c056d1a at
https://github.com/tonylquintanilla/tonyquintanilla.github.io

Run: save this file in the orrery repo root (beside PROJECT_INSTRUCTIONS.md),
open it in VS Code, click Run.  Or from a terminal in the repo root:
    python patch_skills_v357.py

What it does, all-or-nothing -- seven files or none:

  skills/orrery-coding-conventions/SKILL.md   1.7 -> 1.8 (L-317). Adds Two
      Standards for the Info Marker's Outline -- Tony's Mode 5 ruling of
      May 28-29, 2026, which had lived only in the code and in
      shell_configs.py comments -- and corrects the Single Info Marker
      Pattern example, which still showed the size-6 white-border style
      create_info_marker's docstring records as retired in May 2026.
  skills/interactive-exhibit/SKILL.md         1.1 -> 1.2 (L-316, L-318).
      The nav cluster's four arrows and their portrait placement, the
      drawer label, the Mode 5 sequence, and two Plotly rules read from
      v2.35.2's source: a scene relayout carries the live camera, and a
      hover box keeps its pointer only when it fits to one side.
  skills/safe-file-editing/SKILL.md           1.10 -> 1.11 (L-315). Adds A
      Guard Must Not Fence What a Generator Rewrites.
  ledger_index.py   reads the raw bytes, detects the file's line ending,
      and writes with it instead of the platform default.
  PROJECT_INSTRUCTIONS.md   step 3 of the four-step rule: the v3.57
      entry, the header stamp and the SHA anchor; the v3.54 entry is CUT
      from here (it is moved, not copied -- the same bytes land in the
      archive).
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md   receives the v3.54
      entry at the end of PART 1, with its moved-down note.
  LEDGER_CONSOLIDATED.md   header stamp; L-316 and L-318 record their
      skill rows; L-315 and L-317 close and move to section C.

Guards: each file's text, line endings normalised, must match orrery
1fa413d9 -- the ledger's outside its generated INDEX zone. The three
blocks that MOVE (v3.54, L-315, L-317) are fingerprinted before they are
cut. Windows line endings are kept, per file.

Permanent: the seven files. Disposable: this script.
Success prints one 'ok' per step and 'patch applied'. Any failure prints
one ERROR / ANCHOR FAIL line and writes nothing.
Undo is Discard Changes in GitHub Desktop.

THEN, in this order:
  1. python skills_index.py     -- step 2; rewrites the Skill Manifest in
     PROJECT_INSTRUCTIONS.md to 1.8 / 1.2 / 1.11.
  2. python ledger_index.py     -- expect "OK: 316 L-blocks parsed, no
     consistency problems." This also exercises the line-ending fix.
  3. Settings > Skills: REINSTALL orrery-coding-conventions,
     interactive-exhibit and safe-file-editing from skills/. A reinstall
     is invisible to a running conversation, so the next session is what
     confirms it -- its loaded copies must read 1.8, 1.2 and 1.11.
  4. Commit all of it together (step 4 of the four-step rule) and push.

Written September 11, 2026 with Anthropic's Claude Opus 5.
"""
import hashlib, os, sys

EXPECTED = {
    'skills/orrery-coding-conventions/SKILL.md': '06e7824340785f0b3941ea57cfc3a0a5',
    'skills/interactive-exhibit/SKILL.md': '0702a94e64599ace93c89e612e301889',
    'skills/safe-file-editing/SKILL.md': '62484c3240dba3ff66ed7a894d64928e',
    'PROJECT_INSTRUCTIONS.md': '45e085a70d64362d289c602813754669',
    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': '683843c30e51b63ae1c3ef07358a5870',
    'ledger_index.py': '755319c7996f8e125675503b60b625e9',
    'LEDGER_CONSOLIDATED.md': '1c091651196ff91f5d466ff60e7d0b1f',
}
FP_BLOCKS = {
    'v354': '74ab46c6e74b2e4c839db45611890399',
    'L-315': '402786968c5ec7531d939c5bd033b5cd',
    'L-317': '1d39c28d4d0b44e8c55f7b39579c3f71',
}

SKILL_EDITS = {
 "skills/orrery-coding-conventions/SKILL.md": [
('version header',
b"""Skill version: 1.7 | Cut from palomas_orrery @ 04bba3ca (v1.7),
earlier @ 3faa72a0 (v1.6),
earlier @ 15741822 (v1.5), 86f529a (v1.4), 3398970 (v1.3) | 2026-08-26
""",
b"""Skill version: 1.8 | Cut from palomas_orrery @ 1fa413d9 (v1.8),
earlier @ 04bba3ca (v1.7), 3faa72a0 (v1.6),
earlier @ 15741822 (v1.5), 86f529a (v1.4), 3398970 (v1.3) | 2026-09-11
v1.8 (L-317) adds Two Standards for the Info Marker's Outline -- Tony's
Mode 5 ruling of May 28 and 29, 2026, which had lived only in the code
and in shell_configs.py comments -- and corrects the Single Info Marker
Pattern example, which still showed the size-6 white-border style that
create_info_marker's own docstring records as retired in May 2026.
Earned when the gallery drew every info marker red for two exhibit
rooms, because the rule a marker session loads was not in this skill.
"""),
('the example calls the factory',
b"""```python
go.Scatter3d(
    x=[0], y=[0], z=[r * 1.05],  # shell: north pole 5% above surface
    mode='markers',
    marker=dict(size=6, color=shell_color, symbol='cross',
                opacity=0.9, line=dict(color='white', width=1)),
    name='', showlegend=False,
    text=[info_hover_string],
    hovertemplate='%{text}<extra></extra>'
)
```
""",
b"""```python
create_info_marker(
    x=0, y=0, z=r * 1.05,        # shell: north pole, 5% above the surface
    color=shell_color,           # the cross's FILL is the shell's colour
    text=info_hover_string,
    legendgroup=group,           # toggles with the geometry
    border_color='white',        # only on a saturated warm fill; see below
)
```

`create_info_marker` in `orrery_rendering.py` owns the style -- size 8,
opacity 1.0, cross, border width 2 -- so it changes in one place. New
markers call it. An inline dict, where the factory does not fit, matches
it. (The size-6, white-border, opacity-0.9 pattern this example used to
show is the pre-May-2026 style the factory's docstring records as
retired; it was left standing here until 2026-09-11.)
"""),
("Two Standards for the Info Marker's Outline",
b"""**The trigger is measurable, so measure it.** Two shells within 10% is
the test, not "looks close." A shell whose radius is a derived constant
can move without anyone editing the marker code.

## Hover Text AU Convention [QUALITY]
""",
b"""**The trigger is measurable, so measure it.** Two shells within 10% is
the test, not "looks close." A shell whose radius is a derived constant
can move without anyone editing the marker code.

### Two Standards for the Info Marker's Outline [QUALITY]

The cross's FILL is its shell's colour. That is what ties the marker to
the thing it labels, and it does not change.

The OUTLINE is red by default, and WHITE on saturated warm fills -- the
oranges, the pink-reds, the dense reds -- where a red outline is lost
against the shell's own dot field. The pale peach and golden ends of that
same ramp keep red, because white is lost there instead: Earth's inner
core, `rgb(255, 180, 140)`, was tried in white and reverted.

**Judged per shell by eye, NOT by an RGB threshold.** There is no
lightness cutoff to compute. Tony's Mode 5 of May 28 and 29, 2026 set
each one, and the results are declared, not derived.

Declare it with `'info_border': 'white'` in `SHELL_CONFIGS`;
`build_sphere_shell()` passes it to `create_info_marker(border_color=)`,
whose default is `'red'`. 18 shells carry it at `1fa413d9`, each with a
comment naming the fill it clears. Where a builder is not config-driven,
set `border_color` at the call site with the same comment (Earth's inner
radiation belt, `earth_visualization_shells.py`).

The factory also takes `fill_color`, for the red-on-red exceptions of
May 2026; no shell config uses it today. Its docstring says FILL is the
contrast lever because Plotly ignores marker border WIDTH (field note
below). That is about width, not colour -- a one-pixel white outline
reads clearly against an orange dot field, which is why the declared
rule is a border rule.

**A convention that is not in this skill does not travel.** This rule
lived in the code and in `shell_configs.py` comments for three months
and was never written here. In September 2026 the gallery served the
orrery's shell colours for two exhibit rooms with no outline flags at
all, and every cross drew red -- including the outer core and both
mantles, where it disappears. The session that built those markers
loaded this skill and could not have known. The code is not the store a
fresh session reads. (L-317; the gallery now serves `info_border` per
shell.)

## Hover Text AU Convention [QUALITY]
"""),
 ],
 "skills/interactive-exhibit/SKILL.md": [
('version header',
b"""Skill version: 1.1 | Cut from gallery @ 57fd93c6 (interactive.html,
index.html, tools/json_converter.py, tools/gallery_studio.py,
tools/gallery_editor.py) and orrery @ 1ee1cc61 (LEDGER_CONSOLIDATED.md
L-291, L-303, L-309) | 2026-09-10, with Anthropic's Claude Opus 5
v1.1 (L-291)""",
b"""Skill version: 1.2 | Cut from gallery @ 9c056d1a (interactive.html,
gallery/nav_cluster.js, gallery/feature_renderers.js) and orrery @
1fa413d9 (LEDGER_CONSOLIDATED.md L-310, L-316, L-317, L-318, L-320)
| 2026-09-11, with Anthropic's Claude Opus 5
v1.2 (L-316, L-318) records what the chrome gained after Tony's phone:
the nav cluster's four arrow buttons and their portrait placement, the
drawer label, and two Plotly rules the build found by reading v2.35.2's
source rather than recalling it -- a scene relayout carries the live
camera, and a hover box keeps its pointer only when it fits to one side.
Earlier: v1.1 (L-291)"""),
('drawer row gains the label',
b"""| Drawer replacing the legend: rows from `legendgroup`, `legendonly` hides, All / none, focus row | `buildSunDrawer`, `sunApplyVisibility`, `sunFocusOn` | shared |""",
b"""| Drawer replacing the legend: rows from `legendgroup`, `legendonly` hides, All / none, focus row; naming a DRAWN shell also opens its hover text as a scene annotation pinned to its info marker, closed by a tap in the scene or by unticking (L-318) | `buildSunDrawer`, `sunApplyVisibility`, `sunFocusOn`, `sunLabelShow`, `sunLabelInstall` | shared |"""),
('nav cluster row gains the arrows and the portrait placement',
b"""| Nav cluster: + / - / Home = FRAME zoom (range and dtick change together; the grid re-labels) | gallery/nav_cluster.js, `navFrameZoom`, `navHome` | shared |""",
b"""| Nav cluster: + / - / Home = FRAME zoom (range and dtick change together; the grid re-labels), plus four arrow buttons that turn the camera by a step scaled to the live eye distance, so a tap moves the same slice of screen at any zoom (L-310); on a portrait phone 768 px or narrower the arrow cross moves to the top-right corner, which the hidden mode bar leaves free, and the in-frame title stays (L-316) | gallery/nav_cluster.js (`crossRight`), `navFrameZoom`, `navHome`, `navCameraStep`, `sunCrossRight`, `navPlaceCross` | shared |"""),
('Mode 5 sequence names the arrows and the label',
b"""floats); + / - / Home (grid re-labels, chip follows); drawer (a hidden
shell draws and the view rescales to hold it); a shell tap (focus,
i-panel, link);""",
b"""floats); + / - / Home and the four arrows (grid re-labels, chip follows;
a tap turns the same slice of screen at any zoom); drawer (a hidden
shell draws and the view rescales to hold it); a shell NAME (focus, the
i-panel, and the label pinned to that shell's marker); a shell tap
(focus, i-panel, link);"""),
('two Plotly rules read from v2.35.2',
b"""tap and closes on a tap elsewhere. A `hidden` attribute loses to a more
specific display rule; write the hidden rule at least as specific.
""",
b"""tap and closes on a tap elsewhere. A `hidden` attribute loses to a more
specific display rule; write the hidden rule at least as specific.

**A scene relayout must carry the live camera.** A 3D replot re-applies
the camera stored in the layout (`gl3d/scene.js`, `setViewport`), and a
touch rotation never updates that stored copy. So any `Plotly.relayout`
touching the scene -- opening a label, changing margins -- sends
`scene.camera`, read live, alongside whatever it came to change.
Otherwise the view snaps back to wherever the last mouse event left it.
(L-318, read from plotly.js v2.35.2.)

**A hover box keeps its pointer only when it fits to one side.** Plotly
puts the label to the right of its point if it fits, else to the left if
it fits, else centres it OVER the point with no pointer at all and nudges
it back on screen (`fx/hover.js`). So a wide hover string on a narrow
phone loses the line tying it to its marker, and whether it does depends
on where the marker sits, not on how much room there is. Wrap narrower,
or pin a scene annotation, which always points. (L-318.)
"""),
 ],
 "skills/safe-file-editing/SKILL.md": [
('version header',
b"""Skill version: 1.10 | Cut from palomas_orrery @ ccd1ac96 (v1.10),
earlier @ bfa9de2f (v1.9),
""",
b"""Skill version: 1.11 | Cut from palomas_orrery @ 1fa413d9 (v1.11),
earlier @ ccd1ac96 (v1.10), bfa9de2f (v1.9),
"""),
('v1.11 note',
b"""Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons;
""",
b"""v1.11 (L-315) adds A Guard Must Not Fence What a Generator Rewrites,
earned when three chained ledger patches all refused: each was
fingerprinted against the previous one's raw output, while every one of
them told the operator to run `ledger_index.py` next -- which rewrites
the zone they were hashing.
Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons;
"""),
('the new subsection',
b"""## Delivery Format -- Runnable by Tony, Not Just Reviewable [CRITICAL]
""",
b"""### A Guard Must Not Fence What a Generator Rewrites [QUALITY]

Some files carry a zone a tool regenerates: the ledger's INDEX zone
(`ledger_index.py`), the protocol's Skill Manifest (`skills_index.py`).
A patch that edits the body and ends by telling the operator to run that
tool must not fingerprint the zone. Hash the content OUTSIDE it.

```python
a = lf.index(b"<!-- INDEX:START")
b = lf.index(b"<!-- INDEX:END -->") + len(b"<!-- INDEX:END -->")
fp = hashlib.md5(lf[:a] + lf[b:]).hexdigest()
```

A guard that includes the zone refuses for a reason that is not about
content -- Line Endings Are Not Content, one layer out.

**A chain is worse than a single patch.** Fingerprint patch 2 against
patch 1's raw output and the chain works only while nobody runs the
generator in between. When patch 1's own instructions say to run it, the
chain cannot run at all. In the case that produced this note three
patches were chained that way AND hashed raw bytes, so on a Windows
working copy -- where the generator wrote in text mode and turned the
file CRLF -- every one of them refused in any order. One patch that
accepts EITHER starting state replaced all three.

**A generator does not let the platform pick.** `open(path, 'w',
encoding='utf-8')` writes the platform default, so on Windows an LF file
comes back CRLF: a file-sized diff carrying no change, and a raw-byte
guard downstream that cannot pass. Write with `newline=''`, which keeps
the `'\\n'` the code already holds.

```python
with open(target, 'w', encoding='utf-8', newline='') as f:
    f.write(new)
```

`skills_index.py` had done this since it was written, with the reason in
a comment. `ledger_index.py` had not, and that is half of why the three
patches above refused; it was matched at `1fa413d9`.

**The asymmetry with Line Endings Are Not Content is deliberate.** A
PATCH preserves what the file already uses, because it is there to make
one change and not to restyle 11,000 lines. A GENERATOR that rewrites the
whole file holds the repo's convention, because rewriting the file IS the
job. Do not "fix" either one to match the other.

## Delivery Format -- Runnable by Tony, Not Just Reviewable [CRITICAL]
"""),
 ],
}

PI_EDITS = [
('header stamp',
b"""Tony Quintanilla, PE | Claude | v3.56 | September 10, 2026""",
b"""Tony Quintanilla, PE | Claude | v3.57 | September 11, 2026"""),
('SHA anchor',
b"""Cut from 1ee1cc61 at https://github.com/tonylquintanilla/palomas_orrery""",
b"""Cut from 1fa413d9 at https://github.com/tonylquintanilla/palomas_orrery"""),
('v3.57 entry',
b"""v3.56 (September 10, 2026): No rule changed in this document. TWO skill""",
b"""v3.57 (September 11, 2026): No rule changed in this document. THREE
skill bumps, taken together at the close of the 2026-09-10 evening
session and BEFORE the builds they serve.

orrery-coding-conventions 1.7 -> 1.8 (L-317), interactive-exhibit
1.1 -> 1.2 (L-316, L-318), safe-file-editing 1.10 -> 1.11 (L-315).

TWICE IN ONE EVENING THE INTERACTIVE LACKED A SOLUTION THE ORRERY
ALREADY HAD, and that is what the first bump is for. The gallery drew
every info marker red, against orange and red shells, because Tony's
two-standards outline rule of May 2026 lived in the code and in
shell_configs.py comments and had never been written into the skill a
marker session loads (L-317). Separately, the orrery declares a marker
angle per shell where one is needed, while the gallery stepped from the
pole and left nine markers on the drawn axis (L-320). Only the first
was a skill gap; Tony ruled the second directly, keeping the gallery's
own steps.

The rule the first case earns is this document's own Context Priority
read from the other end: A CONVENTION THAT IS NOT IN THE SKILL DOES NOT
TRAVEL. The code is not the store a fresh session reads. The session
that drew those markers loaded the skill and could not have known.

interactive-exhibit gains the chrome the phone changed -- the arrow
cluster and its portrait placement, the drawer label -- and two Plotly
rules read out of v2.35.2's own source rather than recalled: a scene
relayout must carry the live camera, because a 3D replot re-applies the
layout's stored copy and a touch rotation never updates it; and a hover
box keeps its pointer only when it fits to one side of its point.

safe-file-editing gains A Guard Must Not Fence What a Generator
Rewrites. Three chained ledger patches refused this session: each was
fingerprinted against the previous one's raw output, while every one of
them told Tony to run ledger_index.py next -- which rewrites the zone
they were hashing. ledger_index.py now holds LF on write, as
skills_index.py already did one file away.

THREE BUMPS IN ONE ENTRY IS NOT A VIOLATION OF ONE SESSION, ONE BUMP.
That rule is per SKILL: a session does not ship two versions of one
skill. Three different skills ride one protocol entry, as two did at
v3.55 and v3.56.

These bumps are taken at the session's close rather than before its
builds, which v3.55 recorded as the better order. The builds they
describe had already happened; taking them now is what makes them
available to the NEXT session. So the obligation travels as usual: this
session loaded 1.7, 1.1 and 1.10, and a reinstall cannot be verified
from inside the session that made it. The next session confirms its
loaded copies read 1.8, 1.2 and 1.11 before doing marker, exhibit or
patch work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.54 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

v3.56 (September 10, 2026): No rule changed in this document. TWO skill"""),
]

LI_EDITS = [
('LF enforced on write, matching skills_index.py',
b"""    with open(path, 'w', encoding='utf-8') as f:
        f.write(new)
""",
b"""    # L-315: LF enforced, matching skills_index.py, which has done this
    # since it was written. Plain text mode writes the platform default, so
    # on Windows this rewrote the whole ledger to CRLF -- a file-sized diff
    # carrying no change, and a raw-byte guard in the next patch that could
    # not pass. newline='' preserves the '\\n' the code already holds.
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(new)
"""),
]

LED_STAMP = (b"""hover text joins the provenance braid, Earth first), built on b2c77350.
""",
b"""hover text joins the provenance braid, Earth first), built on b2c77350.
Module updated: September 11, 2026 with Anthropic's Claude Opus 5
(skill layer: orrery-coding-conventions 1.8, interactive-exhibit 1.2 and
safe-file-editing 1.11; L-315 and L-317 closed), built on 1fa413d9.
""")
LED_316 = (b"""**Gap:** desktop, not yet looked at: title and cross exactly as before --
this also covers L-310's desktop check. Then, at interactive-exhibit's
next bump, its nav cluster row names the arrows (L-310) and the portrait
placement (this item).
""",
b"""- **In interactive-exhibit 1.2, 2026-09-11.** Its nav cluster row now
  names the four arrows and the portrait top-right placement, and its
  Mode 5 sequence names the arrows. [verified @ `1fa413d9` + this patch]
**Gap:** desktop, not yet looked at: title and cross exactly as before --
this also covers L-310's desktop check.
""")
LED_318 = (b"""- **Still open here:** a tap on a marker still shows Plotly's own hover
  box, which drops its pointer mid-screen at `HOVER_WIDTH` 70.""",
b"""- **In interactive-exhibit 1.2, 2026-09-11.** The drawer row names the
  label; the touch-path section gains the two Plotly rules this build
  read from v2.35.2 -- a scene relayout carries the live camera, and a
  hover box keeps its pointer only when it fits to one side.
  [verified @ `1fa413d9` + this patch]
- **Still open here:** a tap on a marker still shows Plotly's own hover
  box, which drops its pointer mid-screen at `HOVER_WIDTH` 70.""")
LED_315_META = (b"""<!-- L:315 status:OPEN upd:2026-09-10 section:A flag: rice:2/2/90/1 -->""",
b"""<!-- L:315 status:DONE upd:2026-09-11 section:C flag: rice:2/2/90/1 -->""")
LED_315_GAP = (b"""**Gap:** the field note, under the four-step skill-bump rule;
`ledger_index.py` preserving line endings, in the same session.
""",
b"""- **CLOSED 2026-09-11, both halves.** safe-file-editing 1.11 carries A
  Guard Must Not Fence What a Generator Rewrites: fingerprint the content
  OUTSIDE a generated zone, a chain whose own instructions run the
  generator between its links cannot run at all, and a generator holds
  the repo's line endings rather than the platform's. `ledger_index.py`
  now writes with `newline=''`, which `skills_index.py` has done since it
  was written -- the reason was already in a comment there, one file
  away. Found by testing the fix, not by reading: a first version
  preserved each file's own endings, which would have left the project's
  two generators disagreeing. Sandbox: run on an LF copy and a CRLF copy
  of the ledger at `1fa413d9`, both come back LF with identical content.
  [verified in the sandbox]
**Gap:** none.
""")
LED_317_META = (b"""<!-- L:317 status:OPEN upd:2026-09-10 section:A flag: rice:4/2/80/1 -->""",
b"""<!-- L:317 status:DONE upd:2026-09-11 section:C flag: rice:4/2/80/1 -->""")
LED_317_GAP = (b"""**Gap:** at orrery-coding-conventions' next bump: the two-standards rule,
and the example corrected to `create_info_marker`.
""",
b"""- **CLOSED 2026-09-11.** orrery-coding-conventions 1.8 carries Two
  Standards for the Info Marker's Outline -- fill is the shell's colour,
  outline red by default and white on saturated warm fills, judged per
  shell by eye and declared with `info_border` -- and its Single Info
  Marker Pattern example now calls `create_info_marker` instead of
  showing the size-6 white-border style the factory's docstring records
  as retired in May 2026. The rule closes with the sentence the case
  earns: a convention that is not in the skill does not travel.
  [verified @ `1fa413d9` + this patch] The Mode 5 pass is recorded
  above.
**Gap:** none.
""")

SECTION_C_END = b"""skills/orrery-coding-conventions/SKILL.md (marker separation).
## D. RECONCILED LEDGER -- OPEN"""
ARCHIVE_ANCHOR = b"""made a fourth entry.)


### Preserved verbatim: v3.29 Technical lessons"""


def body_fp(lf):
    a = lf.index(b"<!-- INDEX:START"); b = lf.index(b"<!-- INDEX:END -->") + len(b"<!-- INDEX:END -->")
    return hashlib.md5(lf[:a] + lf[b:]).hexdigest()


def one(lf, pair, label, steps):
    old, new = pair
    n = lf.count(old)
    if n != 1:
        raise ValueError("ANCHOR FAIL: %s expected 1 match, got %d" % (label, n))
    steps.append(label)
    return lf.replace(old, new)


def cut_block(lf, header, want, label):
    """Cut one ledger block out, checking it is the one we built against."""
    if lf.count(header) != 1:
        raise ValueError("ANCHOR FAIL: %s header" % label)
    i = lf.index(header)
    j = lf.find(b"\n#### [", i + len(header)) + 1
    if j <= i:
        raise ValueError("ANCHOR FAIL: %s has no block after it" % label)
    block = lf[i:j]
    if hashlib.md5(block).hexdigest() != want:
        raise ValueError("ERROR: %s is not the block this patch was built against" % label)
    return lf[:i] + lf[j:], block


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    data, crlf = {}, {}
    for rel in EXPECTED:
        p = os.path.join(root, *rel.split("/"))
        if not os.path.exists(p):
            print("ERROR: not found: %s (run from the orrery repo root)" % p); return 1
        with open(p, "rb") as f:
            raw = f.read()
        crlf[rel] = b"\r\n" in raw
        data[rel] = raw.replace(b"\r\n", b"\n")
    for rel, want in EXPECTED.items():
        got = body_fp(data[rel]) if rel == "LEDGER_CONSOLIDATED.md" else hashlib.md5(data[rel]).hexdigest()
        if got != want:
            print("ERROR: %s content %s, expected %s -- not orrery 1fa413d9, or already patched; "
                  "nothing written" % (rel, got, want)); return 1
    steps = []
    try:
        # 1. the three skills
        for rel, edits in SKILL_EDITS.items():
            for label, old, new in edits:
                data[rel] = one(data[rel], (old, new), "%s -- %s" % (rel.split("/")[1], label), steps)
        # 2. ledger_index.py
        for label, old, new in LI_EDITS:
            data["ledger_index.py"] = one(data["ledger_index.py"], (old, new), "ledger_index.py -- " + label, steps)
        # 3. protocol: stamp, anchor, v3.57 entry, then CUT v3.54
        pi = data["PROJECT_INSTRUCTIONS.md"]
        for label, old, new in PI_EDITS:
            pi = one(pi, (old, new), "protocol -- " + label, steps)
        i = pi.index(b"v3.54 (September 6, 2026):")
        j = pi.index(b"\nFunctional for Claude, readable for human")
        v354 = pi[i:j]
        if hashlib.md5(v354).hexdigest() != FP_BLOCKS["v354"]:
            raise ValueError("ERROR: the resident v3.54 entry is not the one this patch was built against")
        data["PROJECT_INSTRUCTIONS.md"] = pi[:i] + pi[j + 1:]
        steps.append("protocol -- v3.54 entry cut (%d bytes)" % len(v354))
        # 4. archive receives it
        data["documentation/PROJECT_INSTRUCTIONS_HISTORY.md"] = one(
            data["documentation/PROJECT_INSTRUCTIONS_HISTORY.md"],
            (ARCHIVE_ANCHOR,
             b"made a fourth entry.)\n\n\n" + v354 +
             b"(Moved down from the resident protocol on 2026-09-11 when v3.57\nmade a fourth entry.)\n\n\n"
             b"### Preserved verbatim: v3.29 Technical lessons"),
            "archive -- v3.54 entry received", steps)
        # 5. the ledger
        led = data["LEDGER_CONSOLIDATED.md"]
        for pair_, label in ((LED_STAMP, "header stamp"), (LED_316, "L-316 records its skill row"),
                             (LED_318, "L-318 records its skill rows")):
            led = one(led, pair_, "ledger -- " + label, steps)
        closed = []
        for handle, meta, gap in ((b"L-315", LED_315_META, LED_315_GAP), (b"L-317", LED_317_META, LED_317_GAP)):
            led, block = cut_block(led, b"#### [" + handle + b"]", FP_BLOCKS[handle.decode()], handle.decode())
            for pair_, what in ((meta, "status DONE, section C"), (gap, "closing record")):
                if block.count(pair_[0]) != 1:
                    raise ValueError("ANCHOR FAIL: %s %s" % (handle.decode(), what))
                block = block.replace(pair_[0], pair_[1])
            closed.append(block.rstrip(b"\n") + b"\n")
            steps.append("ledger -- %s closed" % handle.decode())
        led = one(led, (SECTION_C_END,
                        b"skills/orrery-coding-conventions/SKILL.md (marker separation).\n\n" +
                        b"\n".join(closed) + b"## D. RECONCILED LEDGER -- OPEN"),
                  "ledger -- L-315 and L-317 moved to the end of section C", steps)
        data["LEDGER_CONSOLIDATED.md"] = led
    except ValueError as e:
        print(str(e) + "; nothing written"); return 1
    for rel, d in data.items():
        bad = sum(1 for c in d if c > 127)
        if bad:
            print("ERROR: %s holds %d non-ASCII byte(s); nothing written" % (rel, bad)); return 1
    for h in (b"#### [L-315]", b"#### [L-317]"):
        if data["LEDGER_CONSOLIDATED.md"].count(h) != 1:
            print("ERROR: %s appears %d times; nothing written"
                  % (h.decode(), data["LEDGER_CONSOLIDATED.md"].count(h))); return 1
    if data["PROJECT_INSTRUCTIONS.md"].count(b"v3.54 (September 6, 2026):") != 0 or \
       data["documentation/PROJECT_INSTRUCTIONS_HISTORY.md"].count(b"v3.54 (September 6, 2026):") != 1:
        print("ERROR: the v3.54 entry did not move exactly once; nothing written"); return 1
    for rel in EXPECTED:
        p = os.path.join(root, *rel.split("/"))
        with open(p, "wb") as f:
            f.write(data[rel].replace(b"\n", b"\r\n") if crlf[rel] else data[rel])
    for s in steps:
        print("ok  %s" % s)
    print("patch applied (%d files)" % len(EXPECTED))
    print("next: python skills_index.py, then python ledger_index.py, then reinstall the three skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
