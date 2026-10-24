<!-- Doc-Kind: hand | Design record: Tony's rulings of Oct 24 on the five findings of his Oct 23 phone look (the drawer's controls, the count line, a far orbit's frame, the About card's return); zero code. -->
# Design record: the drawer's controls, the count line, and a far orbit's frame

Tony Quintanilla, PE | Claude Opus 5.5 | October 24, 2026

Built on orrery 991425bc89b3be21a794b6d748857e7c36b974c7 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b0f50ce52181154b43dcc384d85bcf0461798fde at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
Both read live with git ls-remote at the session's start.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION (zero code). One records patch for the orrery,
`patch_L477_1_drawer_view_records_20261024.py`, which writes this file.

Companion to: the brief Claude Fable 5.1 wrote that morning in a
coordinating session, "Brief: the drawer's controls, the count line,
and a far orbit's frame" (attached to this session; its file name not
given); Tony's run record `documentation/WHERE_WE_ARE_10-23-26_1402_run_record.md`,
his answers to the Oct 23 phone checklist (lines 538-546), the primary
record of the five findings. Supersedes nothing.

Skills this session loaded, each at the version the protocol's manifest
expects: interactive-exhibit 1.21 (discharging v3.109's obligation),
ledger-and-session-records 1.22, safe-file-editing 1.13.

Ledger: L-477 (the drawer's controls), L-478 (the count line's place),
L-479 (a far orbit's frame, and each orbit's near and far distance),
L-480 (the About card's return). Closed by the patch: L-472 (the view
fix), L-473 (groups open unticked), L-474 (See more on top), L-475 (the
About link).

Tony's words are quoted as he typed them, with curly quotes made
straight.

## 1. The drawer's controls (findings 1 and 2) -> L-477

**What was measured to put it.** At gallery b0f50ce, a group row in the
Solar System room's drawer is ONE button with two zones: a tap inside
its `.pick` span runs `ssGroupTick`, which ticks every body in the
group; anywhere else runs `ssFold`, which only folds it
(`interactive.html`, `ssBuildRows`). The `.pick` span is the row's
whole left end, about 65 px, made wide on purpose for body rows
(L-318 round 3). On a group row it is exactly where a thumb reaching
for the group's name lands. That explains why the comets opened
unticked on the afternoon of Oct 23 and ticked that night.

**The mock-up.** At Tony's request ("Yes please do a mock up"), four
working phone drawers on one Design canvas in his artifacts, "Drawer
controls mock-up": today's drawer, A-prime (one job per row, See more
and None in the top bar), B (a small group box at the row's right end),
and option 1 (added later, below). Built from the page's own colours,
type, row heights and the room's real body list in its served order;
not the real page.

**Tony's finding, which set the rule.** "What's confusing is the the
referent is different. See more/fewer rows all/none celestial objects."
See more acts on the LIST (which rows show); All / none acts on the
PICTURE (what is drawn); a group row mixes the two. Claude put it as a
rule: each control acts on one thing, and sits beside that thing or
says it in its words. Option 1 followed: no See more, the groups always
listed and folded, the top bar's one control acting on the picture.
Added to the mock-up at Tony's word (by voice, "Yes, please"; then
"Please Do the mockup").

**The rulings.**
- "I think so. No "see more" Let that be permanent. And change
  all/none to "Reset" that resets the view to the starting view when
  the visitor wants a fresh start. Simple."
- "Actually I think we should use the same logic for the groups. The
  starting view is unticked. The visitor tries some objects. A Reset
  button can bring back the original unticked list. "All" is very
  confusing with too many orbits all at once. It is better for the
  visitor to develop the view."

So:
- See more / See fewer is removed for good. All six groups are always
  listed, folded shut.
- A group row only folds open or shut. It never ticks anything. Its
  box goes; where the box was, the fold arrow (the mock-up's form).
- The top bar's All / none becomes Reset: the room as a visitor first
  finds it -- the served opening's ticks (Mercury, Venus, Earth, Mars),
  its highlighted row (Earth), every group folded shut, and the
  opening view.
- Each open group's "All / none in <group>" becomes "Reset <group>",
  which unticks that group's bodies (Claude's reading, shown in the
  mock-up's option 1, for Tony's phone look to confirm).
- No control anywhere ticks many bodies at once. The visitor builds the
  view one body at a time.

**What the build decides by method.**
- Reset and Home stay distinct, and the build says so in code and in
  the skill: Home moves the camera and keeps the ticks (with nothing
  ticked it already puts back the served opening); Reset puts back the
  ticks, the folds and the view.
- A group's Reset shows only while at least one of its bodies is ticked
  (nothing to reset otherwise), and leaves the group open.
- Where Reset sits in the top bar, and its touch target (at least
  44 px tall, the drawer's rule).
- The served rows lose `see_more` (data/objects_config.json, the
  rooms section, through the store writer's rules or a patch); the
  page's See more code (`ssAddSeeMore`, `seeMoreLabel`, `visible`'s
  seeMore branch) and its checks go, and `toggleAll` and
  `groupToggle` are replaced by the two resets.
- The drawer check (`smoke_solar_system_drawer.js`) and the headless
  walk (`walk_solar_system_drawer.js`) change with it, each new check
  shown red on a broken copy first.
- interactive-exhibit's next version describes the new drawer. Its
  present text names See more, the group's box and All / none in six
  places in The Solar System room's drawer section; a session following
  them would build the wrong drawer, so the bump rides the build
  (ledger-and-session-records, A Wrong Sentence in a Skill).

## 2. Where the count line sits (finding 3) -> L-478

**Tony's suggestion,** twice in the run record: "would this line fit
above the object label on the left?" and "the aries symbol is partially
covered, that is why i am thinking we could move the ticked body count
to the left side above the object label."

**Ruling.** Claude proposed taking it as it stands, the placement being
method; Tony: "Yes".

**What the build decides by method.** The line moves from above the
grid chip (`#ss-outside` in the right-hand HUD) to the left side, above
the object label, in the same type. The build checks on the phone that
it does not collide with the object label at its longest or with an
open text box.

## 3. Framing a far closed orbit (finding 4) -> L-479

**What was measured to put it.** The room frames on where each ticked
body is NOW, plus 20% (Tony's ruling of Oct 2). Sedna is 82.8 AU out
(coverage_index.json, the Oct 22 run, as the brief gives it; the
elements at the Oct 24 epoch give 82.9 by Kepler's equation), so the
view reaches about 99 AU from the Sun. Its served orbit (a = 539.58 AU,
e = 0.8588, coverage_index.json at gallery b0f50ce, JPL Oct 24) runs
from 76 AU to about 1,000 AU from the Sun. A view holding all of it
reaches about 1,200 AU, some twelve times wider (the brief said "about
ten"). The count line does not help here: Sedna itself is in view;
only its orbit is cut.

Go To at b0f50ce (`ssGo`) frames the body and then opens its hover as
a text box (`sunLabelShow`): Tony's ruling of Oct 10, "Go To, takes
them the orbit and hovertext."

**Options put.** A, keep the Oct 2 rule; B, Go To fits the body's whole
orbit, ticking unchanged; C, ticking a single body fits its whole
orbit. Claude leaned B.

**Tony:** "B may work but now it activates the hover". Claude put B1
(keep the text box; one tap on the picture closes it; every Go To
alike) and B2 (Go To only moves the view, for every body). Tony:
"Let's try B1".

**Ruling, as a trial.** Go To fits the body's whole orbit and opens its
text box, the same for every body. Ticking still frames on where the
bodies are now (the Oct 2 rule stands for ticking). Tony's phone look
after the build decides whether it stays.

**The orbit's near and far distance in every body's hover.** Put to
Tony: "Its orbit runs from 76 to 1,000 AU from the Sun." Tony: "It
would be informative but may be too long. It would also give an
intuitive sense of the eccentricity." Claude offered one short line,
"Orbit: 76 to 1,000 AU from the Sun.", noting Earth's would read close
to "0.98 to 1.02 AU", nearly the same number twice. Tony: "Yes".

**What the build decides by method.**
- Go To's frame: the farthest point of the drawn orbit from the Sun,
  times the room's frame margin (1.2), so the frame rule is the same
  rule applied to the orbit.
- An open path (slice 2's comets and spacecraft) has no whole orbit;
  slice 2's design decides what its Go To fits.
- The two distances are worked out from the served elements (q = a(1
  - e), Q = a(1 + e)), never typed, for closed orbits only.
  provenance-discipline fires: the figures each prints, and its
  citation, follow its rules for a computed number. A body drawn around
  the barycentre (`drawn_orbit`) needs the build to say which elements
  the line reads; the line says "from the Sun".
- The hover-length check (`smoke_hover_budget.js`, CEILING 17) holds
  every body's hover; if the line pushes any over, it comes back to
  Tony.

The two instruments still frame differently on purpose: the orrery
opens on the farthest thing drawn, shell or orbit, plus 20% (Settled,
Oct 18-19). Nothing here changes the orrery.

## 4. The About card's return (finding 5) -> L-480

Method, Claude's pick, put to Tony with "you can overrule" and not
overruled: closing the About card steps back to the page the visitor
came from, through the browser's history, as the Gallery button
already does ("Gallery steps back in history when the gallery is
behind it", interactive-exhibit's anatomy table). A visitor who opened
About from a room lands back in that room. Arriving at the lobby
directly, the close stays in the lobby as now.

## 5. The build order

The build session that follows builds L-477, L-478, L-479 and L-480
together in the gallery, then Tony's phone look; then slice 2 of L-443,
by `DESIGN_L443_slice2_rulings_20261023.md`.

## 6. Settled lines removed from Where We Are

The page sits at its 130-line cap, so two Settled lines came off for
the two that went on. Both rules now live in skills (interactive-exhibit
1.19, provenance-discipline 2.34). Kept here word for word:

    - Drawer order: nearest part as drawn from sourced rows. Drawings end
      where a row says, Earth too. (Oct 21)
    - An edge nobody can place: a cloud across its range. An edge that
      moves: sharp, with two dashed circles at its range's ends. The hover
      says which. The Oort spheres removed. (Oct 22)

## 7. Tony-action rollup

- **(do)** Save `patch_L477_1_drawer_view_records_20261024.py` in the
  orrery folder, run it from VS Code, move it to documentation/, then
  run `ledger_index.py`, commit and push. Push the Oct 23 close note
  `HANDOFF_L472_session_close_20261023.md` with the same commit.
- **(do)** The Daily Run, which covers the live check owed since the
  website push at b0f50ce, if it has not run since.
- **(do)** After the build session: the phone look of the four rulings,
  before slice 2.

Written October 24, 2026 with Anthropic's Claude Opus 5.5.
