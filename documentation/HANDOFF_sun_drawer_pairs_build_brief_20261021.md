<!-- Doc-Kind: hand | Brief for one build session in the Sun's slice: the drawer order by where each shell begins (L-460, interactive-exhibit 1.19, every room, the Sun first with its order listed for Tony before it ships), then the Sun's fourteen hover and tooltip pairs (L-191, orrery only). -->
# Brief: the drawer order (L-460), then the Sun's fourteen pairs (L-191)

Built on orrery 8228622 ("L463 far lines button", 2026-10-21 16:40) at
https://github.com/tonylquintanilla/palomas_orrery and gallery
b334077 ("L463 sun room fixes", 2026-10-21 15:58) at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Run
`git ls-remote` on both at the start; if either has moved, read its
newest handoff and Where We Are first and build on the new HEAD.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD. Written October 21, 2026 by Anthropic's Claude Fable 5.1,
in a coordination session, for a Claude Opus build session. Follows
`HANDOFF_L456_addresses_build_20261021.md` (section 6, items 1 and 3)
and `HANDOFF_talks2_20261021.md`.

## 1. Read this first

- Everything up to 16:46 on October 21 is pushed and checked: every
  Sun and Earth source linked (L-456), the pink band and the Sun's own
  row fixed (L-463, L-464), both days' talks on the ledger. The orrery
  maintenance run passed 31 of 31 at 8228622. Nothing waits on Tony
  before this session.
- Tony's latest run record:
  `documentation/WHERE_WE_ARE_10-21-26_1217_run_record.md` at 8228622
  (pushed separately at c0feb22 a few minutes later; read whichever is
  newer). Read it before the close: it carries his phone looks of the
  day.
- Where We Are's "Do next" box still names `patch_L463_2`, which Tony
  ran; this session's close rewrites the box.
- Skills: confirm the loaded interactive-exhibit reads 1.18 (the
  manifest at 8228622), provenance-discipline 2.32, orrery-coding-
  conventions 1.11, safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.21. interactive-exhibit goes to 1.19 in
  job 1 (one session, one bump; the four-step binding rule; protocol
  v3.107). provenance-discipline is NOT bumped by this session unless
  job 2 needs it; if it is, the "one layer down" paragraph written in
  `DESIGN_talks2_rulings_20261021.md` talk C rides that bump as 2.33,
  and if it is not, that paragraph keeps waiting (the ledger line says
  where).
- Tony is likely at his machine this evening (his run record was
  pushed from it at 16:46). He can run patches, look at the orrery's
  tooltips and hovers, and look at the website on his phone.
- Method, not a question for Tony: where a shell begins is its served
  inner edge; the tie rules below. Bring him only the listed order to
  look at, and the five pairs to choose between.

## 2. Job 1: the drawer order, every room, the Sun first (L-460; gallery; interactive-exhibit 1.19)

Tony's ruling, 2026-10-20: "they should be ordered by lower distance
limit"; in every room, each shell takes its drawer place at the
distance where it begins, "basically when we reach that shell's
distance, that is its place in the order." The Solar System room's
drawer is NOT in scope: it runs outward from the Sun by body, and
L-363's ruling of 2026-10-20 keeps it so.

What his look caught: the corona's row took the streamer belt's old
place at the top of the Sun's drawer when the belt joined it on
2026-10-20.

The build:
1. Trace where each room's drawer order comes from today. At gallery
   b334077 the Sun's features are served in groups in
   `data/objects_config.json` (`sun_structures`, `solar_atmosphere`,
   `solar_wind`, `oort_cloud`, `hill_sphere`), and the drawer lists
   traces in the order the renderers emit them (`gallery/
   feature_renderers.js`; the panel and drawer code in
   `interactive.html`). Confirm this by reading the code, not from this
   sentence: the order may be set in more than one place (Verify
   Execution, Not Appearance), and the Earth room's drawer may be built
   differently from the Sun's. Say in the handoff where it was set.
2. Define "where it begins" from the served rows, one rule for all
   rooms: a shell's inner edge (its `inner` or `r_min` row, or its
   single radius for a sphere drawn as a surface, or the lower end of
   a band); for a shape drawn as stored dots, the drawing's inner
   extent. Ties: a shell that begins at the body's surface sorts after
   the body's interior shells; two shells beginning at the same
   distance keep their present relative order. The centre body's own
   row stays first; frame rows (axis, galactic plane, Sun direction,
   terminator) keep their present places, since they are not shells
   and have no distance. Record these tie rules in the skill with the
   rule itself, so nobody asks again.
3. Read the order from the rows at page load, not from a hand list, so
   a new shell lands in place by itself.
4. List the resulting order for every room (the Sun, Earth; the Solar
   System room untouched) in a short file for Tony, each row with the
   distance it begins at, in the unit the room uses, BEFORE the patch
   is final. His look is the gate. Opus's reading of the Sun's
   atmosphere part, unverified: chromosphere, corona (with the
   streamer belt), Roche limit, zodiacal dust cloud, Alfven surface;
   the full list must include the interior, the solar wind and the
   Oort rows too.
5. The headless room checks (`tools/headless`) assert each room's
   order from the rows; plant a fault (one row's edge moved) and show
   it caught by name.
6. interactive-exhibit 1.19: the rule and its tie rules, one section,
   with the trigger line naming the drawer's order; the three-entry
   rule for its version history (the oldest entry to
   `documentation/SKILL_HISTORIES.md`); `skills_index.py`; the protocol
   entry v3.107 in `PROJECT_INSTRUCTIONS.md`, the oldest resident entry
   to `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`.

Patches: one gallery patch (the order, the checks, the list for Tony)
and the skill bump inside the orrery's close patch (job 3). Tony's run:
the gallery patch, moved into the gallery's `documentation/`, the
Gallery Maintenance Run offline, commit, push, the live run; his phone:
the Sun room's drawer, then Earth's. Then reinstall interactive-exhibit
1.19.

## 3. Job 2: the Sun's fourteen hover and tooltip pairs (L-191, the Sun's share; orrery only)

In `solar_visualization_shells.py` fourteen Sun shells each have two
live strings: an `_info` string the checkbox tooltip shows and an
`_info_hover` string the plot's hover shows. Measured at fcd191e9 and
on the ledger (L-191, 2026-10-18 and 2026-10-20):
- FIVE pairs differ in content: gravitational influence, Roche limit,
  Alfven surface, corona, zodiacal dust. The corona's and the dust
  cloud's differ on purpose: the tooltip adds the panel's words to
  Tony's approved hover words.
- NINE pairs are byte-identical copies: outer Oort, inner Oort, inner
  Oort limit, solar wind, termination shock, chromosphere, photosphere,
  radiative zone, core.
- The Alfven surface's hover leaves out the 10 to 20 solar radii range
  its tooltip prints from L-228's rows.

The build, in Tony's own words from the coordination session of 10-20,
with Opus's correction carried in:
1. Re-measure the fourteen at HEAD first (the strings moved on
   2026-10-20 and 21); say in the handoff whether five and nine still
   hold.
2. For the five, show Tony the two texts side by side with the breaks
   stripped, one shell per message; he picks the survivor, the default
   being the copy that prints from rows. For the corona and the dust
   cloud, the default is the hover (his approved words) with the
   panel's lines kept where the tooltip had them, if he wants them.
3. Then one string per shell, written in newlines, the twin deleted,
   `<br>` derived at the Plotly boundary with `.replace('\n', '<br>')`
   as the gas-giant configs in `shell_configs.py` already do (sixteen
   sites, the template); the Tk backstop in `CreateToolTip` stays.
   Breaks-only where the text does not change, proved byte for byte
   with the breaks stripped, in the patch's own check.
4. The nine: keep one copy, delete the other, checked letter for letter.
5. Every typed number in a surviving string is either printed from its
   row or already on L-411's held list; add none (One Value, One Home).
   The scanner's Tier-1 count may move as string units split or merge
   (L-191's Gap+ of 2026-08-19); the patch predicts the CHANGE, by
   name, not the total.
6. agentic-pre-test: py_compile, the xvfb run on a throwaway copy, the
   live-dispatch smoke test (the Sun's checkboxes built, each tooltip
   and each hover read back, the same words).

Tony's look: each shell's tooltip (hover the checkbox) and its plot
hover, the same words. At the close: L-191's Sun share done, the
fourteen named; the other 39 strings (the gas giants' 36, Planet 9's 2,
the Moon's 1) stay with their rooms.

## 4. Job 3: the close (orrery)

One close patch, built on the pushed HEAD after Tony's job-1 push:
the ledger (L-460 DONE on his look; L-191's Sun share; L-412's list
moved on), Where We Are by section (the box rewritten: changed, do
next, needs you now; stage 7's line; the marks reset), the skill bump
and protocol entry (section 2, step 6), the handoff
`HANDOFF_sun_drawer_pairs_build_<date>.md`. Tony runs it, moves it,
the maintenance run (expect 31 of 31, 0 Tier-1 on the gate path, the
manifest reading interactive-exhibit 1.19), commit, push, reinstall.

## 5. Not this session

- L-434 (the tide and clumps as stored drawings): next on the Sun's
  list after these two.
- Earth's three builds from the talks (L-375's cone, L-454's faint
  surfaces, L-356 with the offset sentence) and L-458 (the report
  link): one Earth session after the Sun's slice.
- L-461, L-462, L-465: rulings first, in a chat or a short talk.
- Tony's reading list: when he has saved a paper into `papers/`, read
  it through the device mount and write its `# Read:` line; if none is
  there, nothing to do.

## 6. At the close

- The handoff: what was built (verified, not claimed), the run order,
  the fourteen named with each survivor, the drawer orders as shipped,
  the skill obligation (interactive-exhibit 1.19: the next session
  confirms its loaded copy).
- "Where this leaves us", two or three lines in Where We Are's words.

Brief written October 21, 2026 with Anthropic's Claude Fable 5.1.
