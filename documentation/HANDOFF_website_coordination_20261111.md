<!-- Doc-Kind: hand | Handoff: the website track's coordination, from the session of Nov 9 to 11 to a new coordinating session that takes Mars. Communication; written once, read by its receiver. -->
# Handoff: the website track's coordination, to the Mars coordinator

Built on orrery b63df416de703f763e90732c3cfe04ac2a01bd86 at
https://github.com/tonylquintanilla/palomas_orrery
and gallery bd65f036d16b553953f7c8b2e76edc6b10c6b5f4 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-11, 22:10 Chicago). Nightly bot commits
since are expected.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: HANDOFF, coordination (zero code). From the coordinating session of
Nov 9, 22:13 to Nov 11, 22:10 (Claude Opus 5.5, through the python_work
door), to a new Opus coordinating session for the website track, starting
with Mars. Tony, Nov 11, 00:19: "after this fix I think we can hand off
this coordination to a new session for Mars."
Companion: `documentation/WHERE_WE_ARE.md` (the road, the open items) and
the ledger, which wins on status. This file restates neither; it says
where to start and what this session learned.

## Start here

1. Record both bases; say whether either moved past the anchor above.
2. Read Where We Are and Tony's latest run record (the newest
   `WHERE_WE_ARE_*_run_record.md`). Record any verdict of his not yet in
   the ledger.
3. Load the skills the work fires and compare each version line with the
   manifest. Three bumps were cut in sessions that loaded the older copy,
   so each is an obligation for the first session that loads it from the
   account: interactive-exhibit reads 1.41 (v3.138), gallery-cache-builder
   reads 1.19 (v3.139). ledger-and-session-records 1.23 was confirmed on
   Nov 10 (the account's copy byte for byte the repo's at d65309a8).
4. Read L-514 (the Mars room) in full, then L-515 (one nested tree)
   rulings 13 to 20, then L-523 (taps sent as hovers) and L-525 (hold the
   bad data).

## Three ledger passes waiting, each small

- L-523 (taps sent as hovers): Tony's phone look passed ("-- correct",
  in `WHERE_WE_ARE_11-10-26_1813_Fable_run_record.md`); the session that
  read it left the closing to a ledger pass. Close it, re-homing any
  loose end first (the records skill).
- L-524 (the Kepler solver's start): Tony's phone look at the frozen date
  line, `?freeze=1`, upright and sideways, is on Where We Are; his finding
  of Nov 11 ("this line pushes the date line below the directional
  arrows") is what it checks.
- L-525 (hold the bad data): read the first nights with the hold switched
  on, for a "HELD" commit title (none expected).

## Mars, as it stands

- The design is L-514's rulings 1 to 4 and its note received from L-515
  on Nov 9: Mars is a fold of the one tree, not a room; its fold lists its
  shells, Phobos and Deimos together by distance; "Centre on Mars" moves
  the view and opens on the symbol alone; the axis lines cross at Mars.
- Phobos and Deimos are served as JPL's positions for at least 48 hours
  (L-515 ruling 11, ruling 18), built in this step. A moon's checked span
  from nightly elements is capped at an eighth of its period
  (gallery-assembler, the trust system). Io's is already about 5 hours
  either side (the served cache, Nov 9), and Phobos's period is much
  shorter than Io's, which is why. That is builder
  work: gallery-cache-builder and horizons-orbital-mechanics.
- Taps beside a planet: since L-523 a finger's tap reaches 22 px in
  either orientation. L-514 ruling 4's risk stands, measured in the
  build: a wider reach near Mars may pick Mars instead of Phobos.
- interactive-exhibit is at its cap (738 lines, `DOCUMENT_CAPS.md`). The
  Mars session moves old lines out to `documentation/SKILL_HISTORIES.md`
  before adding any; what the page does goes to the gallery's
  `INTERACTIVE_AS_BUILT.md`, not the skill (L-522 step 2).
- The moons Io, Titan, Pluto and Charon have no words or i-panel link
  until the orrery keys them (L-515 leftover 1). Mars's moons must be
  keyed in the orrery's `celestial_objects.py` first, in the same round as
  their website entries, as every new object is.
- Order from here, by the road: Mars, then Uranus and Neptune.

## What this session decided with Tony, by handle

- L-515 rulings 13 to 20 (Nov 9, night): one picture and one drawer; a
  moon folded under its planet; "Centre on" moves the view (picture A),
  the orrery's view measured from a centre waits for the date span;
  a centre opens on its own opening, the Sun included; the axis lines
  cross at the centre; fast moons drawn from their elements with a
  sentence past the checked span; "Pluto system"; the trail line a path
  down the tree. Built Nov 10 (step 2b), passed his phone look Nov 10.
- The Sun direction line stays out of Earth's fold (Nov 10, L-515).
- L-485 (a nightly run): the two red nights of Nov 10 were JPL's, for one
  afternoon; nothing pinned.

## What this session learned (method, for the next coordinator)

- A HEAD MOVES BETWEEN A PROMPT'S WRITING AND ITS SENDING. Tony asked for
  a re-check before sending the tap fix's prompt, and the exhibit skill
  had been split in between, making three of its lines wrong. Re-read
  both heads before any prompt leaves the session.
- TWO COORDINATORS RAN IN PARALLEL (Fable on the documents, Opus on the
  website). Each kept to its own files; neither wrote the ledger while a
  Code session was open on it. Keep that.
- READ THE LIBRARY, DON'T INFER IT. The tap fault was found by reading
  Plotly 2.35.2's shipped `scene.js` (click only under 5 px) and
  gl-select-static (the distance in pixels), fetched from npm; JPL itself
  is not reachable from the workspace (the proxy refuses it).
- ONE TEST THAT TELLS TWO CAUSES APART. The red nights: Tony's own Daily
  Run against the runner's, then the runner by hand at the same hour, so
  JPL changing in between was ruled out.
- PICTURES FOR A DESIGN QUESTION. Inline sketches, one question to a
  message, a lean with its reason: Tony ruled eight questions in an hour.
  Label a sketch a sketch; source any number drawn in it.
- TWO MISTAKES OF THIS SESSION, said to Tony at the time: it claimed the
  bot does not write to the orrery (it does: data/nightly_run_record.json);
  it loaded a whole folder listing to read two sizes (slice instead).

Session written November 2026 with Anthropic's Claude Opus 5.5.
