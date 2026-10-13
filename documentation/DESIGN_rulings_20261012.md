<!-- Doc-Kind: hand | Design-session record: seven rulings Tony made on 2026-10-12 in a coordination session, away from his machine, clearing the design-talk list on Where We Are. Zero code. The next ledger patch carries each one to its item. -->
# Design record: Tony's rulings of October 12, 2026

Built on orrery c5dff25076294d1402498db424cb3761a245af21 at
https://github.com/tonylquintanilla/palomas_orrery; gallery read at
f9453ddbc8b29ed15550a4e980bf3688eed79c82 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Neither
is touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 12, 2026 with Anthropic's Claude Fable 5.1.

- Type: DESIGN SESSION record (zero code).
- Why it exists: Tony, 2026-10-12: "I am trying to clear out the
  scaffolding backlog so that once the earth and sun slices are
  completed we can proceed smoothly." The rulings below were made in
  chat, one at a time, from the design-talk list on
  `documentation/WHERE_WE_ARE.md`.
- Each ruling names the item it belongs to. The next session's ledger
  patch writes it there, quoting this record, and takes the item off
  the page's design-talk list.

## 1. L-424 (the checker's one word for two cases): already ruled; the checker follows the skill

Tony: "I thought we decided this already?" He had, on 2026-10-08: the
provenance-cross-check skill defines the two cases separately
("approved as recommended"). What the ledger left open, whether
`worksheet_checker.py` prints two words to match, is method the skill
already answers, not a new decision, and should not have been put to
him again.

Ruled, by that: the checker prints two words. UNCHECKED_MOVE where the
worksheet carries no value verdict; UNVERIFIED_MOVE where it carries
one and it was UNVERIFIED. A test for each. Built with L-426 (the
checker's small-number comparison), which opens the same function
(`compare()`); a change to a checker gets its own session (ruling of
2026-10-08), so that pair is one session, after L-425's.

## 2. L-425 (citation location checks): all three levels, now; no Quote line until level 3 has run

Tony: "All now." Then, on the `# Quote:` question, "Confirmed as long
as level 3 does run."

Ruled:
- Level 1, every file a citation names must exist, fails the run.
- Level 2, every sourced row carries an address with a date, reported
  by name first and failing after Tony rules the excused classes.
- Level 3, a link check that visits each address, runs on Tony's
  machine, report-only -- and it must actually run, as a row of the
  orrery maintenance run, not a tool that waits to be remembered.
- No `# Quote:` line now. Once level 3 runs and shows what it can
  read of each page, the quote idea is brought back to Tony with that
  evidence. Until then a stored quote is a check that cannot fail.
- Added to the same session, on Tony's word "Add it to a brief
  session. Your decision": the audit's Tier-1 total prints with its
  domain split beside it everywhere it prints (at c5dff25: orrery 125,
  Earth System 149, stars 12, utilities 2), and the scanner reads each
  module's docstring `Domain:` tag instead of keeping its own list.
  Report-only; the brief's section 3d.
Brief: `documentation/HANDOFF_L425_citation_locations_brief_20261012.md`.

## 3. L-433 (the road after the Sun and Earth rooms): confirmed, with one meaning made explicit

Tony: "Confirmed." And: "when I said sun and earth rooms I included
the solar system features."

Ruled, for Where We Are's road and the master plan's Section 5a at
their next restamp:
- Stages 5 to 7, "the Sun and Earth rooms", include the Solar System
  room's features. The fuzzy boundaries (L-410) and the scattered disk
  (L-136, below) sit inside that template stage, not after it.
- Stage 13 becomes: the inner planets get their rooms, Mercury, Venus
  and Mars, built from the Sun and Earth template. Jupiter and Saturn
  follow.
- Stage 14, the Earth System layers, moves up beside 13 rather than
  after it.
- Encounters (12) and the golden artifacts stay as paths, not fixed
  next steps: Tony's "then we can decide on priorities".
- One line added: the scaffolding checks (L-424, L-425, L-426, the
  dashboard's labels) are cleared beside the Sun and Earth slices, not
  after them, so nothing is in front when the rooms close.

## 4. L-136 (the scattered disk): yes, scoped

Tony: "Yes."

Ruled: the scattered disk is drawn as a region in the Solar System
room beside the Kuiper belt (not the Sun's slice, his ruling of
2026-10-04). Its edges are ranges, so it is drawn under L-410's
fuzzy-boundary rule and comes after L-410 is built. Its numbers are
sourced then; nothing is typed now. It is built when the Kuiper belt's
region is next opened, one patch for both. Inside the template stage,
by ruling 3.

## 5. The dashboard's checker labels: "Test" comes off

Tony: "Confirmed", on the recommendation in
`documentation/HANDOFF_dashboard_labels_brief_20261012.md`, section 5.

Ruled: the 20 checker labels that begin with "Test" lose it; the
CHECKERS heading carries the meaning. The maintenance run's row names
and the dashboard's labels then agree with less renaming. That brief's
section 5 is updated to say so.

## 6. The Horizons check: a changed data sheet is cleared by the row, option A

Tony: "A. Confirmed", on the first (decide) item of
`documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md`,
section 5 (that brief is not edited; it arrives with patch_L401_4 and
this record is read beside it).

Ruled: red means the figure a row quotes is no longer the figure on
the spacecraft's Horizons data sheet. It stays red until a patch
changes the row, or re-reads it and moves its Read date. No accept
button; nothing clears without a person reading the sheet. A sheet
whose "Revised:" date moved but whose figure is unchanged is noted in
the check's own record and is not red: the row claims the figure, not
the page (The Artifact Bounds the Audit). The second (decide) item on
that brief, whether the identity check widens past the thirteen, was
not raised; its default, no, stands until it is.

## 7. The orrery's Tier-1 findings: the path, not a sweep; four ride L-431 build 2

Tony asked what citations `idealized_orbits.py` (29 Tier-1 findings,
the orrery's second-largest file) is missing, then: "So your
recommended approach is to continue the path not a sweep?" Yes, and
he confirmed it, with one exception confirmed separately.

Ruled:
- No sweep of the 288. The orrery's findings clear by the road: L-431
  fetching the periods and barycentre separations from Horizons
  retires the typed `BINARY_PARAMS` dictionaries in
  `idealized_orbits.py` (Pluto-Charon, Orcus-Vanth, Earth-Moon, one
  more) and the hovers that read them; each body's remaining hover
  sentences are rebuilt with sourced rows when its slice opens. The
  Earth System's 149 wait for stage 14.
- Four findings in `idealized_orbits.py` are mechanical and ride L-431
  build 2 in passing, because that build opens the file: the two
  "theta = 0 deg" and "theta = 180 deg" lines go to
  `data/provenance_exceptions.json` as geometry, not claims; the two
  console prints of transform angles (Mars 25.19 deg, Triton 3 deg)
  are rendering settings and are excused the same way, with the
  reason. Fixed and named in that patch's output.
- The planets' orbit-description dictionary in the same file (ten or
  so textbook claims: Mercury's +43 arcsec/century, Venus e ~ 0.007,
  Earth's 25,772-year axial precession, Mars's eccentricity range,
  the 900-year Great Inequality and the 5:2, Uranus 98 deg, Pluto's e
  and i) is ONE ledger row by class, opened when the inner planets'
  rooms open (ruling 3): each number becomes a sourced row the
  sentence interpolates, or the sentence loses the number. Not in
  passing. (A first reading in chat called it one claim copied four
  times; it is not, and this record is the correction.)

## Tony's actions, all of them

- (do) Commit this record with the next push; the briefs beside it
  name it.
- (decide) Nothing further today; each ruling above is settled.

Session record written October 2026 with Anthropic's Claude Fable 5.1.
