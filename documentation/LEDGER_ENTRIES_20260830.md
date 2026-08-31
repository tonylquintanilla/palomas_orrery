# Ledger entries -- 2026-08-30 session

**Built on** orrery `70f12a7b5c260288c0fc1a135f45e547651c5d9f` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `80759493dd03f7005eb9c4baae6448756893f884` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote at session start.

Four new handles: L-265, L-266, L-267, L-268. Highest in use before this
was L-264, checked against `LEDGER_CONSOLIDATED.md` at the SHA above.

RICE numbers below are PROPOSED, not confirmed. Each carries its
reach/impact/confidence/effort split so you can see what I assumed.
Adjust before running `ledger_index.py`; the index rebuilds from the
`<!-- L:... -->` comments, so fix them there and the status board
follows.

---

## INDEX ROWS

Add to `### A. Active Separate Tracks` (or wherever you place the
gallery-track rows -- L-260 and L-262 sit in A today):

```
| ! | L-266 | Nothing checks that a cited link still resolves | OPEN | 12.0 | 2026-08-30 |
| ! | L-265 | The i panel carries links, not curated prose | OPEN | 10.8 | 2026-08-30 |
| ! | L-267 | The Sun exhibit GUI shape: drawer, focus label, marker navigation | OPEN | 9.6 | 2026-08-30 |
| ! | L-268 | Sweep: features collapsed out of their own identity [16 found] | OPEN | 10.8 | 2026-08-30 |
```

---

## DETAIL BLOCKS

Place in the `## A. ACTIVE SEPARATE TRACKS` detail section, after
L-264's block.

---

#### [L-265] The i panel carries links, not curated prose
<!-- L:265 status:OPEN upd:2026-08-30 section:A flag: rice:4/3/90/2 -->
- **The panel needed content and the obvious content was already
  written.** `solar_visualization_shells.py` holds eighteen `*_info`
  strings, one per Sun shell, several thousand words in total. They
  were extracted this session and shown working in the GUI study.
- **They cannot ship as they are.** A fresh scanner run over
  `solar_visualization_shells.py` returns 6 Tier-1 and 29 Tier-2, 35
  findings. The eighteen info strings are the Tier-2 rows -- each
  carries a `# Source:` comment, so they score 12, "cited, not
  independently cross-checked." The `# Source:` line covers the
  shell's RADIUS. It does not cover the temperatures, densities,
  dates and distances in the paragraph beneath it.
- **Tony's account of their origin, 2026-08-30:** "I originally wrote
  these strings largely using Gemini information." That is the
  recalled-data case exactly, which means the Tier-2 score is
  generous rather than harsh.
- **The gate is the second problem, and it is the harder one.**
  Provenance binds at EXPORT from the orrery (provenance-discipline
  2.9) because no checker exists in the gallery repo. Eighteen
  paragraphs of unverified prose is a far larger export than
  `objects_config.json`'s eighteen radii and their citations, and
  once across the boundary nothing scores them again.
- **Tony's ruling, 2026-08-30: replace the prose with links.**
  Initially links alone; clarifying text may be added later. The
  reasoning is the same as not embedding a lookup table from memory
  -- the liability moves to NASA or Wikipedia, who maintain it.
- **The scanner needs no change to accept this, which was checked
  rather than assumed.** Running the scanner's own
  `extract_numeric_claims` over four candidate strings: the current
  termination-shock paragraph yields 2 claims (94 AU, 84 AU), a
  link-only string yields 0, a link plus prose with no figures yields
  0, and a link with one number left in yields 1. A link-only string
  does not become an ACCEPTED claim; it stops being a claim. The rule
  that makes this work is therefore strict -- **a link-only string
  carries no figures**, and any later clarifying sentence that
  includes a number puts the liability straight back.
- **The objects come free; the structures do not.**
  `celestial_objects.py` holds 193 objects, 184 of them with a
  `mission_url`, mostly NASA and Wikipedia, already keyed per object
  and consumed by the orrery's own info tooltips
  (`palomas_orrery.py` line 9415). The eighteen shells have no
  equivalent -- `data/objects_config.json` contained the string
  "http" zero times before this session.
- **Field added 2026-08-30** by `patch_L265_info_url_placeholder.py`
  (gallery repo): `info_url` on each of the 20 named features, plus
  an `info_urls` array on the one grouped block, seeded with
  `https://www.nasa.gov/`. 22 links, all identical on purpose -- a
  curated link is never exactly the front page, so counting the
  unreplaced ones is one search. A plausible per-shell placeholder
  would have been indistinguishable from a real choice, which is
  cite-to-clear wearing a URL.
- **Tony-action (do):** replace all 22 placeholders with curated
  links. This is the curatorial step and it is his: "That's my
  curatorial part, selecting the link. I have no expertise for
  creating new astronomical text."
- **Tony-action (decide):** whether the eighteen `*_info` strings
  stay in the orrery's own GUI after the gallery stops using them.
  They are Tier-2 there today and nothing in this ruling removes
  them from the desktop tooltips.
- **Gap: not every feature can hold a link.** Tony's ruling of
  2026-08-30 is that each distinct feature gets its own link even
  where features are currently grouped. The patch satisfies that for
  Earth's two belts with a parallel `info_urls` array. Sixteen other
  sub-features across Jupiter and Saturn cannot take one at all,
  because their identity is not in the config. Carried as **L-268**
  rather than as a gap on this row -- it is a data-shape change to a
  live renderer, not part of dropping in placeholders.
- **Gap: two of the eighteen carry live constants.** `outer_corona_info`
  and `alfven_surface_info` interpolate `ALFVEN_SURFACE_RADII` and
  friends from `constants_new.py` at render time. The study's hand
  copy froze those to the literal text "(computed)" -- a shadow
  constant forming in real time, and the clearest single argument for
  the cross-repo transport. Moot if the prose is replaced outright;
  live if any of it is kept.
- **Note:** RICE 4/3/90/2 -> 5.4 proposed, not confirmed.
- **Ref:** L-266 (the check this creates the need for); L-267 (the
  panel that consumes it); provenance-discipline 2.9 (the export
  gate); the cross-repo transport, segment 2 of
  `MASTER_PLAN_INTERACTIVE_GALLERY.md`.

---

#### [L-266] Nothing checks that a cited link still resolves
<!-- L:266 status:OPEN upd:2026-08-30 section:A flag: rice:5/4/90/2 -->
- **Raised by Tony, 2026-08-30**, on being told that link rot would be
  invisible: "That would be a helpful check from the scanner: is named
  link dead."
- **The gap is real and it predates L-265.** The orrery already carries
  roughly 470 URLs across its Python modules -- 184 in
  `celestial_objects.py` alone, plus `constants_new.py`,
  `exoplanet_systems.py` and the Earth System family. Every one is a
  provenance claim. `provenance_scanner.py` reads text and scores
  numeric claims against citations; it has no notion of whether a URL
  it can see still answers.
- **L-265 makes it load-bearing rather than merely useful.** Once the
  i panel's content IS a link, a dead link is not a broken reference
  in a comment -- it is the visitor's entire path to the source,
  failing silently on a public page. That is the failure shape the
  protocol is most set against.
- **It cannot live where the scanner lives, and that is the design
  problem.** The links to check will sit in `objects_config.json` in
  the GALLERY repo. `provenance_scanner.py` exists only in the orrery
  repo. Same boundary that moved the provenance gate from serving to
  export (provenance-discipline 2.9). Three shapes, none chosen:
  (a) extend the scanner and have it read across the boundary, which
  is the cross-repo reach that L-236 deliberately avoided;
  (b) a check in `gallery_maintenance_run.py`, which already has a
  `--live` mode built for exactly this kind of after-push question;
  (c) both, each checking its own repo's links.
- **Three states, not two.** Resolves, does not resolve, and could not
  be reached -- network failures must be counted separately and never
  folded into a pass, the same rule `gallery_maintenance_run.py`
  already applies to reachability (L-236).
- **A fourth state, specific to L-265: STILL THE PLACEHOLDER.** Every
  unreplaced `info_url` is byte-identical to `https://www.nasa.gov/`,
  which resolves perfectly well. A checker that only asks "is it
  dead" will pass all 22 placeholders. The placeholder count is a
  distinct row and it must not read as green.
- **A redirect is not a pass either.** NASA reorganises; a 301 to a
  hub page is a link that resolves and no longer supports the claim.
  Report the final URL, not just the status code.
- **Tony-action (decide):** which of the three shapes above, before
  any of it is built.
- **Note:** RICE 5/4/90/2 -> 9.0 proposed, not confirmed. Reach is
  high because it covers every URL in both repos, not only the 22.
- **Ref:** L-265 (what makes it urgent); L-236 (the gallery runner and
  its three-state convention); L-235 (checks that cannot fail,
  gallery side); provenance-discipline 2.8, The Access Standard --
  reachability is already a stated precondition of a citation, with
  nothing enforcing it.

---

#### [L-267] The Sun exhibit GUI shape: drawer, focus label, marker navigation
<!-- L:267 status:OPEN upd:2026-08-30 section:A flag: rice:4/3/85/3 -->
- **Origin: L-260's portrait defect, which turned out to be a design
  question rather than a layout fix.** The legend covers the picture
  in both orientations and badly in portrait. Moving it was the
  obvious repair; what to move it INTO was not.
- **A boundary ladder was proposed and withdrawn.** Because the Sun's
  eighteen features genuinely nest, "how far out am I looking" fully
  determines "what am I looking at", and a single ordered control
  looked elegant. Tony found the flaw: "we are replacing the object
  list from the orrery that was a completely selectable list with a
  set determined by a boundary." The collapse is a property of THIS
  exhibit, not a general truth. Orbits pull the two apart -- "Earth
  and Jupiter and nothing else" is a sensible request a boundary
  cannot express.
- **Tony's ruling, 2026-08-30, on what the gallery is:** "The gallery
  is meant to produce the orrery to allow the user to assemble their
  own scene. The question is the gui shape." Free object selection is
  therefore permanent, and any control that takes it away is wrong
  however well it suits one exhibit.
- **The agreed shape, four parts, no two doing the same job.**
  (1) Cross markers -- one per shell at its own radius, already built,
  carrying name, radius in km and AU, and citation. Tapping one moves
  the camera. (2) The i panel -- descriptive material and the link
  out, NOT a second copy of the marker's hover. (3) The drawer -- what
  is in the scene, a free multi-select list, the orrery's object list
  moved out of the picture. (4) The focus label -- one thing, where
  the camera is, a readout rather than a chooser, and the handle that
  opens the drawer.
- **One job per control, and it settled two open questions at once.**
  Tony, 2026-08-30: "let the row selection just identify the object
  being targeted, with the box selecting the object and the go moving
  the camera separately." Applied consistently, this also ruled that
  focusing no longer draws a hidden shell -- the same conflation, one
  gesture doing two jobs. Sending the camera to something not drawn
  gives an empty frame at that scale, which is an honest answer; the
  label says "(not drawn)" and dims its swatch.
- **A framing rule was found wrong in the process, and it matters
  beyond the study.** Framing carried a floor of `SUN_HALF_RANGE_AU`
  (0.25 AU), inherited from `interactive.html`. Fifteen of the
  eighteen shells are smaller than that, so framing on the core, the
  radiative zone or the chromosphere produced the identical 0.25 AU
  cube and adding any of them changed nothing on screen. The floor is
  correct on the live page, where the frame only ever widens from a
  fixed arrival view. It is wrong the moment the frame follows a
  chosen object -- and it would have followed us into the real build.
- **Evidence: `sun_gui_mockup.html`**, a throwaway study running real
  Plotly with radii, colours, opacities, point counts and sources
  generated from `objects_config.json` rather than retyped, reusing
  the live page's sphere geometry, hover format and framing rules.
  Tony ran a written Mode 5 protocol against it over two rounds; all
  pass/fail checks passed on the second.
- **Not tested, and recorded as not tested:** the four non-spherical
  structures are drawn as spheres at their outer limit; no Pyodide,
  assembler or served cache; nothing here touched `interactive.html`.
- **Open defect, undiagnosed.** Tony, 2026-08-30: hover text latches
  and the display seizes when a cross marker and then the i button are
  used in sequence. A headless browser confirmed Plotly's gl3d hover
  hit-tests by reading pixels back off the GPU on every mouse move
  ("GPU stall due to ReadPixels" in the console) across 8,119 points,
  and that is on the live page's code path too. The exact sequence
  could NOT be reproduced -- synthetic mouse events do not reach
  Plotly's 3D hover machinery. The applied fix (clear the tooltip and
  set `hovermode: false` while the panel is open, restore on close) is
  reasoned from mechanism, not witnessed. **Tony-action (do):**
  confirm whether it cures the seize. If not, the next move is taking
  the panel off the canvas rather than overlaying it.
- **Tony-action (decide):** whether the drawer's eighteen rows want
  indentation by the config's five groups. Tony 2026-08-30: "it's
  okay. it follows the orrery pattern. indentation could work too" --
  a maybe, left for judging against Earth's shells rather than one
  body.
- **Note:** RICE 4/3/85/3 -> 3.4 proposed, not confirmed.
- **Ref:** L-260 (the portrait defect this answers); L-262 (the
  framing helpers, and see the correction below); L-265 (what the i
  panel will carry); L-237.

---

#### [L-268] Sweep: features collapsed out of their own identity
<!-- L:268 status:OPEN upd:2026-08-30 section:A flag: rice:4/4/85/3 -->
- **Found while adding `info_url` under L-265**, 2026-08-30, and
  carried out of that row on Tony's instruction.
- **Tony's framing, 2026-08-30, and it is the reason this is a sweep
  rather than a bug:** "These are distinct features collapsed for
  convenience at the time." The instances are not related by body or
  by feature type. They are related by a decision that got made
  repeatedly, and there was no reason to think three was all of them.
- **DISCOVERY IS DONE AND IT TERMINATED.** `sweep_collapsed_features.py`
  (gallery repo) enumerates against the stated pattern below and was
  run at gallery `80759493`: **20 stored as themselves, 16 collapsed,
  0 unclassified.** Sixteen is the whole set in the config as it
  stands, not an estimate. Re-runnable; the count moves when a body
  is added.
- **The sweep reports three lists, and the third is the load-bearing
  one.** OK, COLLAPSED, and UNCLASSIFIED. Anything it cannot place
  makes the run non-clean and exits 2. Its first run had 4
  unclassified -- the `orientation` groups, which carry pole
  direction and draw nothing. They are now named in
  `NOT_A_FEATURE_GROUP` and printed under NOT EXAMINED, BY NAME, so
  they are visibly excluded rather than quietly absorbed, and a NEW
  group still lands in UNCLASSIFIED.
- **Remediation is separate and is NOT part of this discovery.** The
  sweep fixes nothing and prints a list. Fixing happens in slices,
  by body, on the rendering ladder.
- **The eighteen Sun shells hold everything about themselves in one
  place.** Name, colour, radius, source and now link sit inside one
  dict per feature. Nothing can come apart, because each feature IS
  one object.
- **THE PATTERN, stated so the sweep can terminate.** A feature is
  COLLAPSED when it is drawn as a distinct thing but is not stored as
  one. Two forms, failing differently -- BY INDEX (several things in
  one block, paired across parallel arrays by position) and BY
  RENDERER (the config holds radii only; name and colour live in a
  style table in `feature_renderers.js`).
- **The sixteen, as measured:**
  - **Rings (11):** Saturn's seven and Jupiter's four carry only
    `inner_radius_km` / `outer_radius_km` in the config. Their
    display names and colours live in `RING_STYLE`, a hardcoded dict
    in `feature_renderers.js` (line 55). The pairing is by KEY --
    `RING_STYLE.saturn.d_ring` -- so it is safe. But the config has
    nowhere to put a link, because the config does not know a ring
    has a name.
  - **Belts (5):** Earth's two -- Inner and Outer Radiation Belt --
    and Jupiter's three -- Inner, Middle and Outer Radiation Belt,
    which are named ONLY in the renderer and not in the config at
    all. Paired by
    INDEX, not by key, and the arrays are split across two files.
    Jupiter is the worst case: `belt_distances: [1.5, 3.0, 6.0]` in
    the config, `names` and `colors` in `BELT_STYLE.jupiter` in the
    JavaScript (line 80). `renderBelts` assembles belt `i` at draw
    time from `distances[i]`, `names[i]`, `colors[i]`.
- **Why index pairing is the part that bites.** There is no inner
  belt anywhere in the data. There is a first entry in three lists,
  and the only thing joining them is that they are all first. List
  the belts outer-first in one array and not the others and every
  list is still the right length, every slot still full, the page
  still draws two belts with correct names and correct colours -- and
  each link now points at the other belt. Nothing errors. The only
  way to find it is to click both links and read what comes up.
- **The existing guard does not cover it.** `renderBelts` line 467
  warns when `names[i]` or `colors[i]` is missing, which catches a
  list that is too SHORT. A list of the right length in the wrong
  order is indistinguishable from a correct one from the inside. The
  length assertion in `patch_L265_info_url_placeholder.py` has the
  same limit: it proves there are two links for two belts and proves
  nothing about which belt each belongs to.
- **The fix is to store a belt as a belt** -- one dict per belt and
  per ring, holding its own name, colour, distance and link, the way
  all eighteen Sun shells already do. Then there is no ordering to
  get wrong because there is no ordering at all, and the JavaScript
  stops being a second home for presentation identity.
- **What it touches:** `renderBelts` and `renderRings` in
  `feature_renderers.js`, `RING_STYLE` and `BELT_STYLE`, and the
  `van_allen_belts` / `radiation_belts` / `ring_system` blocks in
  `objects_config.json`. A live renderer on a public page, so a
  build with a Mode 5.
- **Why it was not done in the L-265 patch.** Changing how a live
  renderer reads its data, inside a patch whose stated job is
  dropping in placeholder links, is the scope creep that turns one
  Mode 5 into a hunt. The placeholder patch is additive and breaks
  nothing; this is a data-shape change and deserves its own pass.
- **Timing argument.** Earth's shells are the next rung on the
  rendering ladder, and Earth's belts are half of the belt problem.
  Doing this as part of that rung costs one Mode 5 rather than two.
  Jupiter and Saturn are not on the ladder yet, so their eleven
  rings and three belts could follow later -- but the shape should
  be decided once, for all of them, not twice.
- **Tony-action (decide):** all sixteen in one pass, or Earth's two
  now with Jupiter and Saturn deferred to their own rungs. The
  SHAPE should be settled once for all of them either way; only the
  order of the edits is in question.
- **Tony-action (do):** add `sweep_collapsed_features.py` to
  `gallery_maintenance_run.py` so it runs in the routine rather than
  sitting in a folder. A sweep nobody executes is L-262's failure
  wearing different clothes.
- **THE BACKLOG IS A LIST OF NAMES, NOT A COUNT.** Tony's ruling,
  2026-08-30: "if the backlog is a names list not just a count this
  works because we know what needs to be built. A count is
  ignorable."
- **The reason, in his words, and it is NOT the one first recorded
  here.** The initial write-up had this as an attention problem -- a
  number being easy to skip past. Tony corrected it: "I can't read
  everything either. That's why I want a list not a count. I can't go
  grep the code for all the instances that built a count. A list is
  manageable and it gives me a sense of the gap."
  So a count is not a weak signal. It is a signal that only works for
  a reader who can go and find out WHAT, and neither reader reliably
  is one. Claude cannot, because it resets and will not think to open
  the file. Tony cannot, because he cannot read everything and does
  not grep. **A report has to be complete enough to act on where it
  lands.**
- **And the names carry the SHAPE of the work, which the number
  cannot.** "16" states a size. "D Ring, C Ring, B Ring, A Ring, F
  Ring, G Ring, E Ring" says it is the whole of one body's ring
  system, one kind of thing, mechanical rather than seven separate
  judgments. That is what gives a sense of the gap.
- The sweep therefore prints every collapsed feature by name, grouped
  by body and feature block, and every stored feature still missing
  an `info_url` the same way.
- **The rule caught the sweep itself on its first pass.** Jupiter's
  three belts came out as `radiation_belts[0..2]` -- precisely the
  ignorable form the ruling is against. Their names exist, in
  `BELT_STYLE` in the renderer; the sweep's table-finder matched
  `name:` and missed `names:`, so it never read that table. It
  reported them as UNNAMED ANYWHERE rather than labelling them by
  index quietly, which is the blind spot announcing, and that is how
  the gap was visible at all. Now fixed: it reads both keyed and
  array style tables and reports "Inner / Middle / Outer Radiation
  Belt (named only in the renderer)".
- **Where this rule should live is an open question, carried to the
  handoff.** There is no skill for the maintenance runner -- checked
  across all ten on 2026-08-30, the word appears once in passing.
  Five rulings on runner reporting are closed in the ledger and
  written nowhere that loads: L-188, L-197, L-205, L-212, L-236.
  Three of them were wanted this session and not available, which is
  why the sweep printed a count in the first place.
- **Gap: the orrery has not been swept.** The same collapsing may
  exist in `shell_configs.py` and the `*_visualization_shells.py`
  family, which have their own parallel structures. This sweep reads
  the gallery's config and renderer only. Unexamined, which is not
  the same as clean.
- **Note:** RICE 4/4/85/3 -> 4.5 proposed, not confirmed.
- **Ref:** L-265 (which surfaced it); L-266 (a mispaired link
  resolves perfectly well, so the dead-link check cannot catch this
  either); L-235 (checks that cannot fail, gallery side).

---

## AMENDMENT TO AN EXISTING ENTRY

#### [L-262] -- the diagnosis in the record is wrong

The 2026-08-29 night handoff states that `smoke_framing.js` slices
`interactive.html` between two markers that "have never existed in that
file in any commit." The measurement is right and the conclusion drawn
from it is wrong.

The test was never about `interactive.html`. It takes the page path as
`process.argv[2]`, and its markers -- `gridDtick`, `frameLayout`,
`rebuildFrameOptions` -- live in `gallery/solar_system_earth_test2.html`.
`gallery_maintenance_run.py` line 146 points it at the wrong page.

Run against the page that actually holds its helpers, it passes all
twelve checks. Verified this session.

Two one-line fixes, neither touching the live page:
1. `gallery_maintenance_run.py` line 146 -- point at
   `gallery/solar_system_earth_test2.html`.
2. `documentation/smoke_framing.js` -- it reads
   `payload_jupiter_saturn.json` from the working directory; the file
   is in `documentation/`.

**This voids the bundling argument in the 2026-08-29 handoff.** L-262
was to be folded into the portrait pass to save one Mode 5. It needs no
Mode 5 at all.

**A residual gap the fix does not close, and it should be recorded
rather than left implied.** Once pointed correctly, the test guards
`solar_system_earth_test2.html` -- a test page. The live exhibit's own
framing (`sunRefitFrame` in `interactive.html`) still has no test, and
L-267's work adds more framing logic to exactly that file. "Put the
check where it runs" is only half satisfied.
