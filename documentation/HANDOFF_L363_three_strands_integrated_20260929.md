# Handoff -- L-363: three strands integrated; Half 2 of the Solar System room is next, under the front-door design

**Built on orrery `e5c3f92a2ad1dd47ad8cb35d17c159e07f1a9cf9` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`f46cf299c2b6e93e5f3ba405c4ad62032e7666ae` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
HEADs read live with `git ls-remote` on 2026-09-29, and every file this
document cites was fetched at those two SHAs. This session wrote nothing
to either repository.

**Type: DOCUMENTATION (zero code).** A review of three documents
against the repositories as they stand, folded into one plan.

**How this document was made.** Two sessions did the same review in
parallel on 2026-09-29: Claude Fable 5.1 and Claude Opus 5.5. This is
Fable's document, amended by the Opus session at Tony's request with
three corrections from the Opus draft (marked *Amended* where they
land): the Sun's slice also writes `data/objects_config.json`, so the
two builds cannot be in progress at once (section 2, item 4); Apophis
is Tony's decision, not a default (section 4, step 3); and the
sequencing question has a third option (section 6). The Opus session
re-verified Fable's two new findings at HEAD: the fallback key does
appear twice in `interactive.html`, and the unrun p4 script is filed in
the orrery's `documentation/`. The Opus draft is discarded; this is the
one document to file.

**Integrates, and supersedes for what remains:**
- `documentation/HANDOFF_L345_gallery_done_D20_next_20260928.md` (the
  store: conversions computed, D20 next). Its work is DONE; see 1.
- `documentation/HANDOFF_L363_half1_done_half2_after_stage_d_20260928.md`
  (the room: Half 1 done, Half 2 waits). Its Half 2 sections 5 and 6 are
  replaced by section 4 below; its record of Half 1 stands.
- `DESIGN_solar_system_room_front_door_20260929.md` (the room as the
  gallery's front door; not yet filed in the repo). Its rulings stand
  unchanged; its start conditions and its patch-6 question are settled
  below.
All three stay authoritative as session records. Their embedded
ledger notes are folded into section 5 here.

**Rules this work ran under:** protocol v3.73. Loaded at session start
and compared, in both sessions: ledger-and-session-records **1.12**,
interactive-exhibit **1.6**, provenance-discipline **2.22**, each
matching the manifest. **The obligation v3.73 carried ("the next
session confirms its loaded copies read 1.12 and 1.6") is
discharged.** The design document's "check interactive-exhibit 1.5"
now means 1.6.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds Half 2.

---

## 1. The three strands, and where each stands today

**Strand A -- the store (L-345 and L-322 Stage D).** Every number a
room prints comes from one row in `constants_new.py`, in the unit its
source gives; any other unit is computed, never stored twice. The
L-345 handoff said D20 was next. **D20 has landed.** Orrery HEAD is
`e5c3f92a`, the SHA in Tony's run record appended to that handoff.
Verified at HEAD: L-345 reads "DONE 2026-09-28" with "Gap: none";
L-322 carries the note "Stage D's finishing condition was met at
orrery 2a7d26b9 and gallery 52da593c" and its Gap is now point (3),
the Sun's slice; the master plan is at v34 with the executive summary;
`documentation/HANDOFF_L345_D20_done_20260928.md` exists. Tony
reinstalled both bumped skills, and this session's loaded copies
confirm it. **The gate that held Half 2 is open.**

**Strand B -- the room, Half 1 (L-363).** The room
`interactive.html?exhibit=solar-system` draws the Sun, Earth, Jupiter,
Saturn and Apophis as symbols on their orbits, at the minute it is
opened. The handoff listed six gallery patches and said patch 6 (the
camera kept through zoom and turning; the palomasorrery.com credit in
the scene) was not yet run. **Patch 6 has landed.** Gallery HEAD is
`f46cf299`, the SHA in Tony's run record appended to that handoff;
the live check there showed all 13 served files byte-identical to the
working copy, and Tony's phone check reads "correct". Verified at
HEAD: `documentation/patch_L363_6_site_credit_and_camera_20260928.py`
is filed, and patch 5's script has moved from the gallery root into
`documentation/` (a Tony-action from that handoff, done).
`SOLAR_SYSTEM_BODIES` still reads `["earth", "jupiter", "saturn",
"apophis"]`; the page's fallback key is still `solar-system-explorer`;
the Explorer card's live link is still the bare `interactive.html`.
Nothing of Half 2 has started, which is as it should be.

**Strand C -- the design (the room as the front door).** A design
session on 2026-09-29, zero code. It settles what the room is for: a
second way into the gallery, where a visitor sees the Sun and Earth,
opens a drawer, ticks a planet and reaches that body's room and cards.
Its rulings are recorded in its sections 3 to 5 and 7 and are not
repeated here; they stand as written. **It changes what Half 2 is**
(its section 8): not "the other six planets" but the nine symbols, a
ten-row drawer with tick boxes, the highlight-and-handle behaviour,
the Home rule, the opening on the Sun and Earth, and the default swap.
Groups, comets, missions and encounters are later rounds.

**Where they converge.** Strand A has finished and freed Strand B's
second half. Strand C has redefined that second half. So the next
build is Half 2 of L-363 as the design describes it, and everything it
needs to start is in place at the two SHAs above.

## 2. What the three documents could not know, verified this session

Each is a fact at HEAD that at least one of the documents left open or
stated in a now-superseded form.

1. **D20 landed at orrery `e5c3f92a`; patch 6 landed at gallery
   `f46cf299`.** The design document said it did not check patch 6; the
   L-363 handoff said to confirm D20. Both are confirmed by the run
   records Tony appended and by the SHAs read live today.
2. **The design's anchors are behind.** It read the orrery at
   `d4fdf78d` (master plan at v33) and the gallery at `63e657f7`
   (before patch 6). Nothing it read about the room's code has changed
   since -- `SOLAR_SYSTEM_BODIES`, the fallback key, the Explorer
   card's link and `navHome` are as it describes -- but the master
   plan it read is one version old (item 4).
3. **The L-363 ledger row has not received Half 1's record.** At HEAD
   it reads `upd:2026-09-26`. Its Gap still says Half 2 waits for
   "L-322 section 6", and its plan-B text still says "the Explorer
   card's live link is changed in Studio". It also still lists "a
   gallery card for the room" as Half 2 work; the card was made at
   gallery `3f7f50ab`. All three are superseded: the gate is open, the
   card exists, and the swap is now two changes in one commit (the
   design's section 7). The handoff's owed update (patches 2 to 6, the
   card, the rulings, the lost card) and the design's owed update fold
   into ONE ledger patch; see section 5.
4. **The master plan v34 orders Half 2 third.** Its executive summary
   lists what comes next as (1) the Sun's slice, (2) Jupiter and
   Saturn's Artifact 2, (3) "the Solar System room's second half,
   beside those". The design makes the room the gallery's default once
   the nine planets are in. How that changes the order is Tony's
   (section 6).
   *Amended.* **The two builds write the same file.** Half 2 adds
   object entries to `data/objects_config.json` and edits
   `interactive.html`. The Sun's slice edits `constants_new.py` and
   the export -- and then, because closing the slice exports the 14
   Sun-room values that are hand-typed in the gallery today (L-371,
   L-386), the gallery's mirror rewrites those values into
   `data/objects_config.json` too. Different entries, same file, and
   both end in the gallery maintenance run and a cache rebuild. That
   shared file and shared rebuild are exactly what Stage D's gate
   protected. **The two must not be in progress at the same time:**
   whichever goes first is pushed and live-checked before the other
   starts.
5. **The fallback key appears TWICE in `interactive.html`** (at
   `f46cf299`, lines 1091 and 1589, both reading
   `"solar-system-explorer"`). The design's swap says "the page's
   fallback key changes", singular. The swap patch changes both, and
   its self-check counts two.
6. **The design document is not filed** in the orrery's
   `documentation/` (Tony-action, still open). Both handoffs are filed,
   but the repo copy of the L-363 handoff (267 lines) lacks the run
   record Tony appended locally (upload is 470 lines), and the repo
   copy of the L-345 gallery handoff lacks the D20 push SHA Tony
   appended. Both local copies reach the repo at his next orrery push.
7. **The unrun `patch_L322_D_p4_gallery_print_counts_20260927.py`** was
   filed in the ORRERY's `documentation/`, not the gallery's as the
   L-345 handoff asked. It is a record either way; Tony decides whether
   it moves. Low weight.
8. **Skill versions moved under the design.** It names interactive-
   exhibit 1.5 and provenance-discipline 2.22 as the copies to confirm.
   The copies to confirm are now interactive-exhibit 1.6,
   ledger-and-session-records 1.12 and provenance-discipline 2.22, and
   this session has confirmed them.

## 3. Where the documents disagree, and which one wins

| Question | L-363 handoff said | Design said | Stands |
|---|---|---|---|
| What Half 2 is | Five planets and Pluto into the config; extend the body list; links; hovers; Mode 5; the default decision (sec. 6) | The nine symbols, the ten-row drawer with ticks, highlight and handle, Home, opening on Sun and Earth, the swap (sec. 8) | Design. The handoff's steps survive INSIDE the design's list (section 4 below). |
| The opening view (handoff Q1) | Open on everything at 54 AU, or frame something smaller? Likely Tony's, Mode 5 | Ruled: Sun and Earth only, drawer closed, Earth's row highlighted, view fits 1.1 x Earth's distance | Design. Q1 is settled. What remains is method: where a room with no object entry gets its opening setting served (design Q1, section 6A). |
| The default room (handoff Q4) | Tony decides at Half 2; "update the Explorer card's live link" may no longer be right | Ruled 2026-09-29: the new room becomes the default once nine planets are in, without waiting for a date picker; the Explorer stays a card, its live link becomes `?exhibit=solar-system-explorer`; the page's fallback becomes `solar-system` | Design. Q4 is settled. The L-363 ledger row's plan-B wording is superseded. |
| Pluto (handoff Q2, design Q8) | Method: barycenter rule, horizons-orbital-mechanics | Same; "Pluto goes last, the others in one batch and one rebuild" (Q16) | Agree. Settle from the skills before Tony; build the eight others first. |
| A link for each body (handoff Q3) | Where a body's link lives in the config, and who may write it: interactive-exhibit | Widened: each row shows "has a room" and "has cards" icons read from the exhibits and card metadata, and each thing has one address (sec. 3, items 6 and 7); a card needs a field naming its body (Q15) | Design widens it. The "has cards" half needs a card-to-body field the gallery metadata does not have; that is gallery-pipeline's, and can land as its own slice (section 4, step 6). |
| Apophis | Drawn today, one of the bodies the cache stands behind | Not in the ten-row drawer; belongs to "near-Earth asteroids", a later round | *Amended.* Tony's (section 4, step 3). Either choice leaves the near-Earth round open. |
| Start conditions | Wait for D20 and Stage D closed; confirm skills 1.5 and 2.22 | Same | Met at `e5c3f92a` / `f46cf299`; skills confirmed at 1.6, 1.12, 2.22. |
| Comets, Voyager 1, the orbit info cross | Not Half 2 (L-364, L-365, L-366) | Still not Half 2, but comets and Voyager 1 are now part of the room's future and their rows should say so | Agree. One added line each on L-364 and L-365 (section 5). |

## 4. Half 2, integrated: the order of work

Before asking Tony any question below, check whether a skill already
answers it (the protocol's "Method Belongs to the Skill"). The design
marked each open question with its likely owner; that marking is kept.

**Step 0 -- the ledger patch that is owed** (section 5). It lands
first, so that the L-363 row says what the room is before the room
changes again. **Built 2026-09-29, in the Opus session:**
`patch_L363_ledger_and_plan_v35_20260929.py` (orrery), which also
restamps the master plan to v35 with the new order. Tested on a
throwaway copy of orrery `e5c3f92a`, both LF and CRLF: every anchor
matched once, a second run refuses, `ledger_index.py` parses 390
blocks with no consistency problems, and the maintenance run's results
were the same before and after the patch. It lands with Tony's filing
push.

**Step 1 -- the design round, one question at a time.** These decide
the shape of the build and none needs code first.
- (Skill first) Where the room's opening choice -- Sun and Earth, Earth
  highlighted, 1.1 x Earth -- is served. The room has no entry in
  `data/objects_config.json`; the arrival block is the model. Read
  interactive-exhibit 1.6's arrival section and "who may write
  `data/objects_config.json`". (Design 6A.1.)
- (Skill first) The drawer's list: spine order, groups, "See more".
  Served data, not page code, or every new group edits
  `interactive.html`. What shape. (Design 6A.3.)
- (Skill first) Pluto: what the row draws. Orrery-coding-conventions'
  barycenter rule and horizons-orbital-mechanics. (Design 6C.8.)
- (Method) How the room remembers tick order, for Home's fallback.
  (Design 6D.14.)
- (Skill first) The hovers under the bumped skills: a body's hover
  prints AU to six decimals then km, computed by the assembler.
  interactive-exhibit 1.6 says a hover prints a unit it is served and
  never converts a served number; positions are computed, not served,
  so decide from the skills whether the rule reaches them.
  (Handoff 6.4.)
- (Tony) Whether ticking a row also opens it. (Design 6D.13.)
- (Tony) Apophis: keep it as one row under "See more" until the
  near-Earth round, or leave it out of Half 2. (*Amended*; see step 3.)
- (Decided 2026-09-29) The master plan's restamp: Tony directed it
  with ruling C; v35 carries the new order (step 0).

**Step 2 -- the config and the cache** (from the handoff's step 1,
unchanged in substance).
- Mercury, Venus, Mars, Uranus and Neptune into `data/objects_config.json`
  as object entries with no features. Check each Horizons target and
  centre against horizons-orbital-mechanics before writing it.
- Pluto as step 1 settles it, in the same batch if settled, else in its
  own later batch (design Q16).
- The room's opening setting and the served list, as step 1 settles
  them.
- One cache rebuild (gallery-cache-builder; Tony pauses OneDrive
  first).
- **Check each new body's OWN trust window covers today**, not only the
  cache's overall window (L-364: Halley's and Encke's did not).

**Step 3 -- the room** (the design's "buildable soon" list).
- `SOLAR_SYSTEM_BODIES` grows to the nine bodies. *Amended:* **Apophis
  is Tony's call, not a default.** It is drawn today, so removing it
  changes what a visitor sees. The two choices: keep it as a single row
  under "See more" until the near-Earth asteroids round, or leave it
  out of Half 2 and bring it back with that round. Neither forecloses
  the group.
- The ten-row drawer: Sun, Mercury, Venus, Earth, Mars, Jupiter,
  Saturn, Uranus, Neptune, Pluto, each with a tick box except the Sun.
  Ticking draws and reframes to 1.1 x the largest extent among the
  ticked rows. "See more" is present but its groups are empty until
  their rounds (Apophis aside, per the ruling above); how it reads when
  empty is a Mode 5 word.
- Selecting and ticking as two acts: tapping a body in the scene
  highlights its row without drawing anything; the closed handle shows
  the highlighted name; tapping a highlighted row expands it to an
  "Enter the ... room" button (Sun, Earth today; the rest "No room or
  cards yet").
- Home: the last ticked object still ticked, default angle, drawer
  closed, its row highlighted; fall back through tick order; if nothing
  is ticked, tick Earth and show the opening view.
- The two info paragraphs rewritten: the bodies drawn; what is still
  missing.
- Every relayout carries the live camera (`sunKeepCamera()`, patch 6);
  a new drawer or Home path that relayouts must call it.
- Every visitor-facing word listed for Tony BEFORE the build (handoff
  6.5).

**Step 4 -- Tony's Mode 5** on his phone, upright and sideways, and on
the desktop. The handoff's headless recipe (its section 7) checks
layout and behaviour meanwhile, with its two limits: no numpy, so the
Explorer cannot render there; no Google Fonts, so whether text fits is
settled only on the phone (L-378).

**Step 5 -- the swap, in one commit** (design sec. 7), once Tony has
accepted step 4 AND the Sun's slice has closed (Tony's ruling C,
section 6):
- Both occurrences of the fallback key `"solar-system-explorer"` in
  `interactive.html` become `"solar-system"` (section 2, item 5).
- The Explorer card's `live` becomes
  `interactive.html?exhibit=solar-system-explorer` (Studio or the
  editor, not by hand).
- The README's bare `interactive.html` link (line 52 at `f46cf299`) is
  checked and, if it should now mean the Explorer, changed.
- The room's own card already links `interactive.html?exhibit=solar-system`
  and does not change.
- Then the gallery maintenance run, push, live run, and Tony opens the
  bare address on his phone: it should be the new room.

**Step 6 -- availability icons and cards linked to a body.** "Has a
room" can be read from `EXHIBITS` today. "Has cards" needs a field on
each card naming its body (design Q15); that is gallery-pipeline's and
touches Studio and `gallery_metadata.json`. It can ship inside Half 2
if the field is small, or as the first later round. Not a gate on the
swap.

**Later rounds, each its own design round:** the groups as rooms with
clouds (the Trojans first, as the pattern; sources for the camp
assignment and the lobes' extent before anything is served); comets
by apparition (L-364); space missions and encounters (L-365, Voyager 1
first; the cache's date reach and how it holds spacecraft, not yet
read); the orbit info cross (L-366); the date picker and animation.

## 5. For the ledger, one patch, one row per class

**L-363 gains** (the two owed updates, folded):
- Half 1's record from the handoff: patches 2 to 6 and what each did,
  including patch 6's snap-back fix (a rule interactive-exhibit already
  had, missed by the zoom caller -- worth a line in the skill's
  touch-path section naming every caller at its next bump); the card
  "Solar System" in the `solar_system` door at gallery `3f7f50ab`; the
  rulings in the handoff's section 2; the lost card and the editor's
  save check (its section 3).
- The design: the front-door idea; the rulings in its sections 3 to 5
  and the swap in section 7, by reference to the filed design document
  rather than restated; Tony's ruling of 2026-09-29 on the order (C:
  Half 2 through Mode 5, then the Sun's slice, then the swap); the
  Tony-decisions still open (ticking opens the row; Apophis). The
  restamp was decided with the order (v35).
- **Gap becomes:** section 4 of this document.
- The plan-B sentence is rewritten to the swap as ruled, and the "a
  gallery card for the room" line is marked done at `3f7f50ab`.

**L-364 and L-365 gain** one line each: part of the room's future
under the design (comets by apparition; missions and encounters).

**L-367 gains:** the headless recipe (handoff section 7) is how the
rooms were checked meanwhile.

**L-378 gains:** the sandbox cannot load Google Fonts, so a text-width
layout decision is settled only on the phone.

**New rows, one per class, for the design's open questions that are
not L-363's** (the design's section 9, kept as it named them):
1. Cloud shapes for the three remaining groups: the main belt,
   near-Earth asteroids, trans-Neptunian objects (shape, extents,
   sources; the Trojans set the pattern).
2. The served list: spine order, groups and "See more" as data, not
   page code.
3. Encounter data: dates, spacecraft records centred on their targets,
   the cache's date reach.
4. Cards linked to a body: a field in the gallery metadata, and Studio
   writing it.

Handles: the highest at `e5c3f92a` is L-390, so these are L-391 (group
clouds, with the Patroclus decision), L-392 (the served list), L-393
(encounter data) and L-394 (cards linked to a body); and L-395, the
direction after the Sun (the objects exported from the orrery's
dictionary and checked against Horizons). The patch's
fingerprint refuses if another session filed first.

**The skill line the handoff asked for:** interactive-exhibit's next
bump gets the headless recipe as a field note and the touch-path
callers named. Not this session; recorded here so it is not lost.

## 6. The one decision this document brings to Tony

**Where does Half 2 of the room go in the order?** The master plan v34
says the Sun's slice, then Jupiter and Saturn, then Half 2 "beside
those". The design of 2026-09-29 makes the room the gallery's default
once the nine planets are in. Whatever the order, the two builds are
not in progress at once (section 2, item 4). *Amended:* three options.

- **A. Half 2 next, swap included.** Build Half 2 through step 5; the
  Sun's slice follows. The front door opens soonest. The cost: the
  new default sends visitors into the Sun room while 14 of its values
  are still hand-typed in the gallery rather than served from the
  export.
- **B. Beside, as v34 has it.** The Sun's slice goes first; Half 2
  follows and alternates with Artifact 2 as Tony directs. The front
  door waits longest.
- **C. Half 2 next, swap held.** *(Ruled.)* Build Half 2 through step 4 (the room
  finished and accepted on the phone, reachable by its own card and
  link), then the Sun's slice, then the swap (step 5) as a small patch
  of its own. The front door is built now and becomes the default only
  once every room it leads into prints numbers served from the export.
  The Opus session's recommendation.

**Tony's ruling, 2026-09-29: C, "confirmed as recommended."** The
order is now: the ledger patch (section 4, step 0); Half 2 through step
4; the Sun's slice (L-322's Gap, L-371, L-386); then the swap (step 5).
The master plan restamps to v35 for this order, at Tony's direction, in
the step 0 patch.

**After the Sun, in outline (Tony, 2026-09-29; L-395).** "In the
original orrery the shells came late." The gallery grows the way the
orrery did: symbols with positions from Horizons and osculating orbits
first, moons with them; then encounters; then shells and slices, where
Jupiter and Saturn's Artifact 2 now falls. The objects come from the
orrery's own dictionary, `OBJECT_DEFINITIONS` in `celestial_objects.py`,
exported the way the constants are, and the check reaches past the
dictionary to JPL Horizons, because the dictionary itself can go
stale. That round opens with its own design session after the swap.

## 7. Tony-actions, consolidated from all three documents

Done, verified at HEAD (no action): D20 run and pushed; skills
reinstalled; patch 6 run and pushed; patch 5's script moved to the
gallery's `documentation/`; both handoffs filed.

Still open:
- (do) File `DESIGN_solar_system_room_front_door_20260929.md` and this
  document in the orrery's `documentation/`, and push. The push also
  carries the run records appended to the L-363 and L-345 handoffs
  (section 2, item 6). The Opus draft
  (`HANDOFF_L363_integrated_half2_front_door_20260929.md`) is not
  filed.
- (decided 2026-09-29) Section 6: C.
- (decide, at Half 2) Whether ticking a row also opens it (design
  Q13).
- (decide, at Half 2) Apophis: one row under "See more", or out until
  the near-Earth round.
- (decided 2026-09-29) The master plan's restamp: v35, in the step 0
  patch.
- (do) Before the filing commit: save
  `patch_L363_ledger_and_plan_v35_20260929.py` in the orrery root, click
  Run, then run `orrery_maintenance_run.py`, then move the patch into
  `documentation/`. All of it goes in the same push.
- (decide, still open) The Sun's Auto view in the orrery, L-385; and
  L-389, whether Earth's atmosphere shells sit on the equatorial or
  the mean radius.
- (decide, later) Patroclus and Menoetius, one row or two (design Q6)
  -- belongs to the Trojans round, not Half 2.
- (do, optional) Move `patch_L322_D_p4_gallery_print_counts_20260927.py`
  from the orrery's `documentation/` to the gallery's, if Tony wants
  the record where the handoff placed it.
- (later) Mode 5 on the phone for the drawer, upright and sideways,
  with every visitor-facing word listed first.

## 8. For the next session

- Re-anchor both repositories live; expect orrery `e5c3f92a` plus
  Tony's filing push (which carries the step 0 patch), and gallery
  `f46cf299`.
- Confirm the loaded skills match the manifest (interactive-exhibit
  1.6, ledger-and-session-records 1.12, provenance-discipline 2.22,
  gallery-assembler 1.3, gallery-cache-builder 1.6, gallery-pipeline
  1.2, horizons-orbital-mechanics 1.1, orrery-coding-conventions 1.9,
  safe-file-editing 1.11, agentic-pre-test 1.2).
- Read L-363 in the ledger and the room's code in `interactive.html`
  from line 1840 (`f46cf299`); line numbers move.
- Confirm step 0 landed: L-363 in the ledger reads `upd:2026-09-29`,
  L-391 to L-394 exist, and the master plan's summary reads v35.
- Start at section 4, step 1.

---

Session written September 2026 with Anthropic's Claude Fable 5.1;
amended the same day with Anthropic's Claude Opus 5.5.

===============================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L363_ledger_and_plan_v35_20260929.py
ok  LEDGER_CONSOLIDATED.md                           header stamp
ok  LEDGER_CONSOLIDATED.md                           L-391 to L-395 added
ok  LEDGER_CONSOLIDATED.md                           L-378 date
ok  LEDGER_CONSOLIDATED.md                           L-378 line
ok  LEDGER_CONSOLIDATED.md                           L-371 date
ok  LEDGER_CONSOLIDATED.md                           L-371 note
ok  LEDGER_CONSOLIDATED.md                           L-367 date
ok  LEDGER_CONSOLIDATED.md                           L-367 line
ok  LEDGER_CONSOLIDATED.md                           L-365 date
ok  LEDGER_CONSOLIDATED.md                           L-365 line
ok  LEDGER_CONSOLIDATED.md                           L-364 date
ok  LEDGER_CONSOLIDATED.md                           L-364 line
ok  LEDGER_CONSOLIDATED.md                           L-363 rewritten
ok  LEDGER_CONSOLIDATED.md                           L-322 date
ok  LEDGER_CONSOLIDATED.md                           L-322 note
ok  documentation\MASTER_PLAN_INTERACTIVE_GALLERY.md executive summary rewritten (v35)
ok  documentation\MASTER_PLAN_INTERACTIVE_GALLERY.md status stamp
ok  documentation\MASTER_PLAN_INTERACTIVE_GALLERY.md status block's pointer
ok  documentation\MASTER_PLAN_INTERACTIVE_GALLERY.md Last updated: v35 added
ok  documentation\MASTER_PLAN_INTERACTIVE_GALLERY.md Last updated: v32 entry dropped (three kept)
ok  documentation\MASTER_PLAN_INTERACTIVE_GALLERY.md participants
ok  documentation\MASTER_PLAN_INTERACTIVE_GALLERY.md Section 5a: 2026-09-29 added

Stamps updated: the ledger's header (Module updated, September 29, 2026);
the master plan's executive summary, Status and Last updated (v35).

patch applied (15 edits in LEDGER_CONSOLIDATED.md, 7 in documentation\MASTER_PLAN_INTERACTIVE_GALLERY.md)

NEXT:
  1. python orrery_maintenance_run.py

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260929T214213Z, 1 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.0s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.7s  unchanged (1 checked, not written)
  Module atlas                 6.5s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.4s  rewrote DATA_INVENTORY.md
  Exact rows report            1.3s  unchanged (1 checked, not written) -- 8 of
                                     21 exact rows printed at 19 lines (9 orrery,
                                     10 gallery); 5 drawn only, 0 not followed, 0
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.7s  No figure count exceeds its inputs: 29
                                     derived row(s) read, 17 judged OK -- 17 OK,
                                     12 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 15 conversion(s)
                                     checked.
  Constants export check       1.1s  Export matches the store: sha256
                                     b6d8bfdb21f6 on both sides; 76 rows re-read,
                                     66 not exported, 26 tokens; 160 conversions
                                     re-computed, 10 of 10 worked cases hold.
  Exact rows by the count      1.3s  PASSING -- 8 printed exact rows each state a
                                     count; 9 orrery lines print through
                                     exact_text(); 10 gallery lines are served
                                     the count
  Dimensions                   1.0s  No unit contradicts its arithmetic: 44
                                     derived row(s) read -- 32 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 78 status lines in constants_new.py are
                                     well formed; 61 rows carry none.
  Row shape                    0.1s  All 142 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          19.2s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.9s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.0s  76 of 114 routed, 8 clean
  Worksheet checker tests     15.6s  All 136 checks passed
  Worksheet key round trip     1.1s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         24.2s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          11.6s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  18 of 18 gating checkers passed -- 102.5s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2012 file(s) examined, 7 written, 0 created, 0 removed, 5 rewritten identically
    written   DATA_INVENTORY.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      PROJECT_INSTRUCTIONS.md
      WORKSHEET_CHECK.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/. -- done
  3. Put DESIGN_solar_system_room_front_door_20260929.md and
     HANDOFF_L363_three_strands_integrated_20260929.md in
     documentation/, with your local copies of the two
     2026-09-28 handoffs. Commit and push.
  4. Tell Claude the new orrery SHA. -- 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 
