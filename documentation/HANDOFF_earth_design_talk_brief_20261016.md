<!-- Doc-Kind: hand | Brief for Earth's first design talk (zero code): the belts' shape (L-330), the eight sentences the Typed facts check holds open (L-451), the rule for the website's notes beside a citation (L-452), and the run records' keep rule (L-449). The talk ends by writing the build brief that follows it, with L-449's check inside. -->
# Brief: Earth's design talk, round 1 (L-330, L-451, L-452, L-449)

Built on orrery 48c84c3 ("Update WHERE_WE_ARE_10-16-26_1708_run_record.md";
the code and the ledger are 25a99ee's, "L421 close") at
https://github.com/tonylquintanilla/palomas_orrery, and gallery
2090a8b ("patch km radius label") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 16, 2026 with Anthropic's Claude Fable 5.1, in the
coordination session of October 15-16.

- Type: DESIGN SESSION, zero code. The conversation is the design
  process: options with their trade-offs, Tony redirects, each round
  simpler than the last. Nothing is built until the design stabilises.
  The session's outputs are a design record and a BUILD BRIEF for the
  session that follows, written at the end from the rulings.
- Ledger: L-413 (Earth's list) names the design talks in order; this
  is the first, L-330 (the belts' shape). L-451, L-452 and L-449 ride
  because each is a ruling Tony can give in the same sitting and the
  same build then carries them. Read all four blocks first, then L-413.
- Order: road stage 5 (Earth's list), after L-421 closed on 2026-10-16.
  After this round: the Sun's list (L-412) resumes at item 3, and the
  rest of Earth's design talks interleave with it rather than block it
  (L-413's own rule).
- ONE SESSION AT A TIME on each repository. This one writes no code,
  so it conflicts with nothing; its small ledger patch at the close is
  the only thing it writes.

## 0. Before the talk

- Pull both repositories at HEAD and pin them; read the four blocks
  at HEAD, not from this brief.
- Skills this session fires, confirmed against the manifest at HEAD:
  interactive-exhibit (1.16; what a room may render and where its
  numbers come from; the served-data provenance contract), ledger-
  and-session-records (1.21; the design record and the close),
  orrery-coding-conventions (1.10; the belts are drawn in the orrery
  too). THE OBLIGATION THAT TRAVELS: this session confirms its loaded
  copy of interactive-exhibit reads 1.16 before exhibit work (bumped
  2026-10-16, protocol v3.101). horizons-orbital-mechanics 1.8 keeps
  travelling; nothing here fires it.
- The Register Rule in full: Tony is ruling from a phone or a chair,
  not a code editor. One question per message. Each option in a plain
  sentence with what it costs. No label without its gloss.

## 1. The agenda, in order, and what each needs from Tony

### 1a. L-330, the belts' shape (the main item)

What is there (L-330, verified at 0d8e6044 and unchanged in kind
since): four edge rows are served for the two radiation belts, inner
1.1 to 2.0 Earth radii and outer 3.0 to 7.0, and neither instrument
draws them. Both draw a ring at the sourced flux peak with a typed
half-width of 0.5 Earth radii, so the outer belt, served 4 radii wide,
is drawn half a radius wide. The plane question (L-231) is ruled and
built: the belts sit in the equatorial plane, the daily average of the
tilted magnetic equator. Before the talk, the session checks at HEAD
whether the hover still prints the typed 0.5 as "Band thickness" above
the served span (L-330 says L-231's pass was to fix it) and reports
what it found.

The options, with what each costs and teaches:

- A. The region between two dipole field-line shells built from the
  served edges (r = L cos^2 latitude, the textbook dipole relation),
  cut at the crust, for both belts; the sourced peak rings kept as
  brighter lines inside. Teaches why trapped particles reach high
  latitudes and why the South Atlantic Anomaly exists. Costs: the
  inner belt's inner shell reaches the surface near 17 degrees
  latitude and may be unreadable against the crust and the low-orbit
  shell; and dipole shells are MAGNETIC geometry drawn about the SPIN
  axis under L-231, so the hover carries a longer sentence than a
  ring's.
- B. A plain torus from the served edges for each belt, peaks as lines.
  Honest to the served width, readable, teaches less: no horns, no
  anomaly.
- C. The hybrid: a torus for the inner belt, shells for the outer belt,
  whose horns are the teaching point. Fable's own fallback in L-330.

Claude's recommendation to bring: C, because it keeps the teaching
where it reads and avoids the one readability risk that is known in
advance. The one thing no option settles from code is how it looks on
the phone, so the talk's ruling is which option(s) go to a THROWAWAY
RENDER in the orrery for Tony's look before either instrument is built
(Mode 5 decides; L-330 says so). Tony may rule one option or two to
compare.

Provenance, for the build brief: the dipole relation needs a source
read before it is drawn (a named textbook or paper, its locator), the
cut at the crust and the "drawn about the spin axis" are declared
drawing choices said in the hover, and no new number is typed: the
edges are the served rows. The build is both instruments in one pass,
orrery first.

Tony's rulings to collect: which option(s) to render; whether the peak
rings stay as lines inside the region.

### 1b. L-451, the eight sentences the Typed facts check holds open

The check prints these eight on every website run without failing,
until each is ruled. Each gets ONE of three answers: SERVE it (the
sentence moves into the feature's served words with its source), ALLOW
it (it is a sentence about the picture, and goes on the check's named
list), or CUT it. Bring them one at a time or in two groups, with a
recommendation each:

1. The tilt sentence, "measured against the orbit of the Earth-Moon
   barycenter ... around the Sun that day (JPL Horizons)": serve, with
   the pole-of-date source already served.
2. "Earth turns once every # hours measured against the stars": serve,
   with the rotation-period row's source.
3. The magnetotail sentence with its four served numbers: serve, with
   the tail rows' source.
4. and 5. "Spacecraft that cross the real boundary/shock typically find
   it within # Earth radii of this model": serve, with the Shue and
   Jelinek rows' sources, since each is a claim from those papers.
6. and 7. The Sun room's two description sentences about what is drawn
   to show a shape and what nobody has measured: allow, as sentences
   about the picture; or move them under the page's own source line.
8. Earth's description sentence, "the radiation belts sit in Earth's
   equatorial plane, the daily average of the tilted magnetic equator
   they follow": serve, with L-231's source, or allow as a sentence
   about the picture. Note that 1a may change the belts' words; rule
   8 with 1a in view.

Tony may rule all eight by class ("serve 1 to 5, allow 6 to 8") in one
answer; the build then does the moving.

### 1c. L-452, the website's notes beside a citation: a RULE, not 35 rulings

Since the citations became the orrery's (L-421), the website's own
note prints after each citation; 14 of the 35 largely repeat it, some
add a locator the citation lacks, and the Crust's served note ends
with a project attribution "(Tony, 2026-09-28)". This is method (Method
Belongs to the Skill): bring Tony the rule, not the 35 cases.
Proposed rule, for his word: a note that repeats its citation is
struck; a note that adds a locator (a section, a table, a page) is
kept and worded as a locator; a note that explains what the number is
for is kept; project attributions and dates never print. The 35 edited
notes come to Tony as a list before they ship, through the store
writer, in the build. L-450 (the orrery's citation texts that carry
store notes, and miss locators) is the orrery side of the same rule
and rides the same build; its rows are named on L-450.

### 1d. L-449, the run records: the keep rule

The builder's run records in `data/solar-system/raw/runs/` were lost
twice (2026-10-16 04:32 and 22:42 UTC) and kept once between (14:05),
cause unknown; the retry theory is ruled out by the second loss. The
builder copies the live `raw/` folder forward whole before it builds
(`gallery_cache_builder.py`, `shutil.copytree(live_raw, staging /
'raw')`), so by design the records survive; on those two builds the
copy did not carry them, and nothing printed what it carried. Two
things, one decision:

- (decide) Keep every record, or a rule for how many the builder keeps
  (for example the last 30). Claude's view, already on L-449: keep
  them while the loss is unexplained; a deletion nobody asked for,
  accepted once, makes the next one look normal.
- The check goes in the build whatever he decides: the builder prints
  how many records it carried forward and from where; the Daily Run
  compares the new cache's `raw/runs/` with the cache it replaced and
  STOPS, naming each record lost, before the maintenance run and before
  anything reaches the change list; and the cause is looked for in the
  copy step itself (what `live_raw` held at that moment, and whether
  the copy reported an error nobody printed). Record what is found;
  do not chase past the records.

### Not this talk

The Sun's items on Where We Are's design-talk list wait for the Sun's
list (L-412): the fuzzy outer corona and the dust cloud, the tide's
cone, the other dot clouds (L-434). The Solar System room's two (the
highlighted row to the top; GO's arrow) wait for a room session. L-401's
two open questions (a model with no stated accuracy; numbers that are
not distances) are orrery-wide and go to their own short talk. Earth's
later talks (L-356 with L-375, L-321, L-314's aberration, L-297 with
L-294, L-374 and L-061) stay in L-413's order; if Tony has energy
after 1a to 1d, L-314's aberration is the smallest: apply the 4.3
degree turn of the nose, or draw un-aberrated and say so in the hover.

## 2. The close

- A design record, `documentation/DESIGN_earth_round1_rulings_<date>.md`,
  in the orrery's documentation/: each ruling in Tony's words, the
  options he declined and why, quoted from the chat or his run record.
- A small ledger patch: the rulings onto L-330, L-451, L-452, L-449
  (and L-450 if it was ruled with 1c); Where We Are's box, stage 5,
  the design-talk list and the marks; the run-record zone read first
  and emptied after. No code.
- THE BUILD BRIEF, written at the end from the rulings:
  `documentation/HANDOFF_earth_round1_build_brief_<date>.md`, anchored
  at the SHAs the session pulled. Its scope, in the order the build
  runs them: the orrery's throwaway render of the belts for Tony's look
  (Mode 5), then the belts in both instruments; the eight sentences
  moved or allowed; the 35 notes and the orrery's citation texts
  through the store writer and the rows (L-452, L-450), the edited
  words to Tony before they ship; L-449's check and keep rule in the
  gallery's builder and Daily Run. One decision left for the build
  session's start, if any, named in the brief. Three patches or fewer,
  one repository at a time, every run green between them.

## 3. Tony's actions, all of them

- (do) Start the design session from this brief, on the phone or at
  the machine; no file to run until the close.
- (decide) 1a: which belt shape(s) go to the throwaway render; the
  peak rings as lines inside, or not.
- (decide) 1b: serve, allow or cut, for the eight sentences, by class
  or one by one.
- (decide) 1c: the rule for the website's notes beside a citation.
- (decide) 1d: keep every run record, or a rule for how many.
- (do) At the close: run the small ledger patch; the maintenance run;
  commit; push. Then start the build session from the brief the talk
  wrote.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
