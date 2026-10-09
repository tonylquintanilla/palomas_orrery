<!-- Doc-Kind: hand | Brief for a decisions-only session, October 8, 2026: five open rulings presented to Tony one at a time from his phone, recorded in a records-only patch he runs later. No design, no build. -->
# Handoff: the decisions session, October 8, 2026

Built on orrery b0b3df8264958ec9f4a7270f4e4008825452f08d at
https://github.com/tonylquintanilla/palomas_orrery. Gallery at
ab66aba70a5874b033742a8428070b5889484490 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read
for one line of `daily_run.py` and not touched.

- Type: DOCUMENTATION (zero code). Written by the Fable 5.1
  coordination session of October 8, which read the repo at HEAD and
  wrote no patch.
- Skills this session fires: ledger-and-session-records (manifest
  says 1.17) for every ledger edit and for Tony's page;
  safe-file-editing (manifest says 1.13) for the patch script. Read
  back in your first reply which version line each loaded copy
  carries. The sessions of October 8 found 1.17 installed; a loaded
  copy that reads anything else is a finding to state, not to work
  past.
- The protocol is PROJECT_INSTRUCTIONS.md v3.85.

## How this session runs

- Tony is on his phone. He can read and rule. He cannot run a patch,
  open a file in VS Code, upload a skill ZIP, or push. Do not ask him
  to do any of those in this session.
- One decision per message. Present the options and the
  recommendation, wait for the ruling, then the next. Every ledger
  handle carries its short label in parentheses, in chat and in the
  files.
- The order below goes smallest and most settled first. Tony may
  reorder or skip; a skipped decision stays on his page under
  "Decisions, one at a time".
- What this session produces, as files Tony saves when he is back at
  his machine: a records-only patch (or one per ruled item, the way
  the October 7 sweep did it: patch_L412_1, patch_L001_1,
  patch_L216_1, each tested alone and in both orders); this session's
  handoff for `documentation/`; and Tony's page edited by section.
  The patch's printed steps say: run from the orrery repo root (VS
  Code, Run), then orrery_maintenance_run.py, then move the script
  into documentation/, commit and push.
- Before writing the ledger, read Tony's latest timestamped copy of
  his page, `documentation/WHERE_WE_ARE_10-8-26_1406_run_record.md`
  at HEAD. Quote his verdicts from there, naming the copy.
- Nothing below the page's marker line is edited. Keep the page
  under 130 lines above the marker.

## The decisions, in order

### 1. L-216 (the swap retry): does it close?

- Where it stands: the retry at the builder's folder swap is proven.
  The swap log at gallery 4cfeca27 shows 29 runs, all ok, and two of
  them (20261004T205153Z and 20261006T182032Z) took two attempts at
  `staging_to_live`; both were Tony's hand builds with OneDrive
  paused. The hand run is Tony's standing practice (his ruling of
  October 7). The cause, a lock on the live folder, is outside the
  project and is not being chased.
- Option A, close. Two owed things stay named on L-351 (what each
  skill is owed): the gallery-cache-builder skill's next version (the
  `[SWAP]` line, the run order, the empty "(N)" folders, the two
  proven retries) and the "conflict copies" wording still in four
  places. The one-line fix in `daily_run.py` (it says the OneDrive
  pause lasts 2 hours; Tony pauses 24) rides the next gallery patch
  that opens that file, which is the L-395 (the Horizons check)
  build.
- Option B, keep open as a watch.
- Recommended: A. The Fable sweep and the October 7 patch both
  recommended it. If A, section C gets the block; the RICE question
  about L-216 in decision 2 goes away.

### 2. L-412 (the Sun's slice), question (b): the proposed RICE scores

- Tony's ruling of October 7 is that an item inside an ordered list
  carries no RICE score. Read the proposed scores against that rule
  before presenting them:
  - L-131 (the zodiacal dust shell) and L-128 (the comet ice lines),
    proposed 3/3/70/2: both are items 9 and 10 of L-412's own list.
    Under the rule they carry no score. The proposal is moot.
  - L-228 (the Alfven surface's ranges) and L-241 (the Hills cloud
    hover), "confirmed": items 4 and 6 of the same list. Moot.
  - L-292 (Earth shells the orrery does not draw), "confirmed": a
    member of L-413 (Earth's list). Moot.
  - L-216 (the swap retry), "lowered or DEFERRED": settled by decision
    1 either way.
  - L-252 (an INCOMPLETE verdict is not a confirmation), at 11.4 the
    second-highest score in section A with "Gap: none in the tool":
    the one live question. Read its block and present: re-score it
    (propose a number), or move it to section G, or close it if its
    Gap really is empty.
- So the decision is L-252 alone, plus a housekeeping question:
  whether the existing scores on list members (L-131, L-128, L-228,
  L-241, L-292, and the three gallery checks in decision 3 that carry
  11.4, 10.8 and 11.4) are struck in the patch, so the index stops
  showing numbers the rule says do not apply. Recommended: strike
  them; the index then matches the rule.

### 3. The gallery's checks: a ledger item for road stage 9?

- Where it stands: Tony's page has road stage 9, "the website's
  checks get a short list of their own", and the ledger has no item
  listing its members in order the way L-412 and L-413 do. Tony asked
  on October 4 for the checks list to come before the front-door swap
  (L-363), because L-367 is that no checker boots a new room and the
  swap changes the front door.
- The members, from the sweep of October 7 (L-300 closed, L-379
  narrowed to one fixture): L-235 (three checks that cannot fail),
  L-237 (Artifact 1's stale golden record), L-262 (the framing smoke
  test never run), L-367 (no checker opens a new room; now also the
  lobby code), L-378 (no automated phone check), L-357 (stale
  artifacts no check reads), L-360 (the hover budget cannot see newly
  served lines), L-380 (the export pull runs after the cache build),
  L-388 (the export pull can print success when it could not fetch).
- Option A, open the item now, in L-412's shape. Read the nine blocks
  and propose an order, smallest and most settled first, for Tony to
  confirm. The item's order becomes the plan; its members carry no
  RICE.
- Option B, leave it as a page stage only, and open the item when the
  build is near.
- Recommended: A. The item is a plan, and the plan is what the build
  session will read. It costs one block now and saves a design round
  later.

### 4. L-395 (the Horizons check), the two questions due at the build

- Halley: whether it is keyed and checked too. It is served by the
  gallery, has a list entry, and is the other pinned record. Keying
  it makes the pinned-record check test two pins instead of one, and
  brings Halley's words and link from the list to the website.
  Recommended: yes.
- Encke's description and link, for its new list entry in
  `celestial_objects.py`. Draft them here for Tony to rule on. Two
  constraints from the record: a description with a number in it
  needs a source for each number or the number comes out (L-403,
  numbers in the object list carry no source), and the link is a
  NASA page or a Wikipedia page, chosen the way interactive-exhibit
  says. Offer one version with no numbers and one with sourced
  numbers; Tony picks.
- Both rulings are recorded on L-395 so the build session starts with
  them settled.

### 5. L-418 (splitting provenance-discipline): what rides version 2.27

- The question the split's brief leaves for Tony
  (`documentation/HANDOFF_L418_split_build_brief_20261008.md`,
  section 4): whether L-371 (the Sun room's served numbers) and L-390
  (the conversion marker) ride provenance-discipline 2.27 with the
  split, and L-414 (the scanner's window and declared rows) waits for
  its own session cutting 2.28.
- Recommended, as the brief says: L-371 and L-390 ride; L-414 waits.
  The two are sentence fixes inside sections that stay in the skill;
  L-414 changes the scanner and the push gate's count and deserves
  its own tests. The sweep asks for L-414 before the Sun's list
  reaches L-228 (the Alfven surface's ranges); that order still holds.
- Ruling it now means the split session builds without stopping to
  ask. Record it on L-418.

### 6. The order of the next sessions

- Proposed by the coordination session, for Tony to confirm or
  reorder. Each needs his machine, so none starts from the phone:
  - A: the install probe check, then the split build (L-418), in one
    fresh session from the brief above. Tony uploads
    install-probe.zip in Settings first.
  - B: finishing L-421 (the typed facts): the inner Oort cloud
    redrawn tilted, carrying the `_declared` "1.1 times" fix, then the
    gating check. Its design talk (the hover's words; whether the
    outer edge moves from 20,000 au to 10,000 au) can run from the
    phone first.
  - C: the L-395 (the Horizons check) build, carrying the
    `daily_run.py` 24-hour line.
  - Then the Sun's list from item 3, L-385 (the Sun's opening view),
    and the L-414 session before L-228.
- Why A before B: the Oort cloud build is citation work, and the part
  of provenance-discipline it most needs (the cross-check procedure)
  is the part a plain read never reaches until the split lands. The
  protocol's own rule is skill bumps before builds.
- Record the confirmed order on Tony's page in the READ THIS FIRST
  box, once.

## At the close

- The ledger: each ruling on its own item, dated, in Tony's words
  where he gave them. L-412's "question (b) is still open" line
  becomes its answer.
- Tony's page, by section: the READ THIS FIRST box says what was
  ruled, in sentences; "Decisions, one at a time" loses what was
  ruled; "Settled" gains any standing rule; nothing below the marker.
- The handoff: `documentation/HANDOFF_decisions_20261008.md`, anchored
  on b0b3df82 and on whatever HEAD reads when the session closes.
- Tony's steps, printed by the patch and listed in the handoff, for
  when he is at his machine: run the patch from the orrery repo root,
  run orrery_maintenance_run.py, move the script into documentation/,
  commit and push, and save this brief and the handoff into
  documentation/.

## What this session does not do

- No design talk. The inner Oort cloud's words and outer edge are a
  separate session. If a decision above turns into a design question,
  park it on the page under "At the next design talk" and move on.
- No build, no skill edit, no change to any code file.
- No reinstall and no probe check; those need Tony's machine.

Brief written October 8, 2026, with Anthropic's Claude Fable 5.1.
