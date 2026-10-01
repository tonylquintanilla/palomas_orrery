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
  4. Tell Claude the new orrery SHA. -- 5db8bbe0ba1098992329083fda6e3a325fab2da9 and gallery at 0f513fd5d8ad2ce1e3ba5f19ea2f44388484690e
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

=================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L396_where_we_are_and_skill_1_13_20260930.py
ok  LEDGER_CONSOLIDATED.md                         header stamp
ok  LEDGER_CONSOLIDATED.md                         L-396 added
ok  PROJECT_INSTRUCTIONS.md                        header v3.74, cut from 5db8bbe0
ok  PROJECT_INSTRUCTIONS.md                        version history: v3.74 entry
ok  PROJECT_INSTRUCTIONS.md                        version history: v3.71 moved down
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md  PART 1: v3.71 received
ok  skills/ledger-and-session-records/SKILL.md     description and fires_when name WHERE_WE_ARE.md
ok  skills/ledger-and-session-records/SKILL.md     version line 1.12 -> 1.13
ok  skills/ledger-and-session-records/SKILL.md     v1.13 paragraph in the header
ok  skills/ledger-and-session-records/SKILL.md     The Document Stack: Where We Are added
ok  documentation/project_instructions_v3_74.md    created
ok  documentation/WHERE_WE_ARE.md                  replaced your earlier draft

Stamps updated: the skill's version line (1.13), the protocol's
header (v3.74, cut from 5db8bbe0), the ledger's Module updated.

patch applied (10 edits in 4 files, 2 new files)

NEXT:
  1. python orrery_maintenance_run.py

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260930T150604Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 0.8s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             1.1s  unchanged (1 checked, not written)
  Module atlas                 5.7s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.3s  rewrote DATA_INVENTORY.md
  Exact rows report            1.2s  unchanged (1 checked, not written) -- 8 of
                                     21 exact rows printed at 19 lines (9 orrery,
                                     10 gallery); 5 drawn only, 0 not followed, 0
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.6s  No figure count exceeds its inputs: 29
                                     derived row(s) read, 17 judged OK -- 17 OK,
                                     12 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 15 conversion(s)
                                     checked.
  Constants export check       0.9s  Export matches the store: sha256
                                     b6d8bfdb21f6 on both sides; 76 rows re-read,
                                     66 not exported, 26 tokens; 160 conversions
                                     re-computed, 10 of 10 worked cases hold.
  Exact rows by the count      1.0s  PASSING -- 8 printed exact rows each state a
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
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          16.4s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.6s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            7.8s  76 of 114 routed, 8 clean
  Worksheet checker tests     12.8s  All 136 checks passed
  Worksheet key round trip     0.8s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         17.1s  All 76 checks passed
  Extractor pins               0.3s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           8.3s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  18 of 18 gating checkers passed -- 83.1s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2014 file(s) examined, 8 written, 0 created, 0 removed, 4 rewritten identically
    written   DATA_INVENTORY.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROJECT_INSTRUCTIONS.md
    written   PROVENANCE_AUDIT.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      WORKSHEET_CHECK.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/. Commit and push. -- 10012821cf6289095912c0a5f2a0ae86d26ce1e1
  3. Reinstall ledger-and-session-records from skills/ to
     Settings > Skills. -- done
  4. Replace the Project's instructions in claude.ai with the new
     PROJECT_INSTRUCTIONS.md. -- v3.74 done
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

=================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L363_7_half2_config_20260930.py
ok  data\objects_config.json                      the rooms section, after the list of objects
ok  data\objects_config.json                      the Pluto-Charon Barycenter, before pluto
ok  data\objects_config.json                      Mercury, Venus, Mars, Uranus, Neptune, after saturn
ok  data\objects_config.json                      the file's description names the rooms section
ok  tools\test_gallery_cache_builder_offline.py   the served-window check reads its participants from the config
ok  tools\test_gallery_cache_builder_offline.py   mock orbit sizes for the six new Horizons ids
ok  tools\test_gallery_cache_builder_offline.py   stamp: Module updated

Stamps updated: the config's own description (its top _comment);
the offline test's Module updated line.

patch applied (4 edits in data\objects_config.json, 3 in tools\test_gallery_cache_builder_offline.py)
objects_config.json now serves 19 objects; the room's drawer rows:
  sun, mercury, venus, earth, apophis, mars, jupiter, saturn, uranus, neptune, pluto_barycenter

Undo, if needed: Discard Changes in GitHub Desktop on both files.

----------------------------------------------------------------------
1. Run the offline builder test now? No network. [y/n] y

>>> python tools\test_gallery_cache_builder_offline.py
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
  ok  first-build structural validation passes (pass)
  ok  clean fakes -> no guard warnings
  ok  every configured object served (19 of 19)
  ok  attribution present
  ok  served_window field present
  ok  earth has parity/addition field 'name'
  ok  earth has parity/addition field 'horizons_id'
  ok  earth has parity/addition field 'category'
  ok  earth has parity/addition field 'availability'
  ok  earth has parity/addition field 'parent'
  ok  earth has parity/addition field 'stored_center'
  ok  earth has parity/addition field 'canonical_frame'
  ok  earth has parity/addition field 'trajectory_of'
  ok  earth has parity/addition field 'osculating'
  ok  earth has parity/addition field 'positions'
  ok  earth has parity/addition field 'presets'
  ok  earth has parity/addition field 'features'
  ok  earth has parity/addition field 'orbit_type'
  ok  earth has parity/addition field 'as_of_today'
  ok  earth has parity/addition field 'event_link'
  ok  earth.osculating has 'center'
  ok  earth.osculating has 'epoch_jd'
  ok  earth.osculating has 'a_au'
  ok  earth.osculating has 'e'
  ok  earth.osculating has 'i_deg'
  ok  earth.osculating has 'node_deg'
  ok  earth.osculating has 'peri_deg'
  ok  earth.osculating has 'M0_deg'
  ok  earth.osculating has 'source'
  ok  voyager_1: osculating null, positions present
  ok  voyager_1 position file on disk
  ok  position file unit km
  ok  B-3: serving_base + scene_features restored for v0.6 parity
  ok  B-3: positions block carries step_hours
  ok  earth.pole_of_date served for the build's date (2026-07-09)
  ok  earth.pole_of_date passes the #P checker (no problems)
  ok  earth tilt of date is the geometry's on the served inputs (23.438152565955857 deg)
  ok  frame_constants serves KM_PER_AU and EARTH_OBLIQUITY_J2000_DEG from the export (EARTH_OBLIQUITY_J2000_DEG, KM_PER_AU)
  ok  no other object carries pole_of_date (none)
  ok  #P aborts a build whose served tilt is not its inputs' (#P earth: tilt 23.438153565955858 is not what its inputs giv)
  ok  earth as_of_today is km-scale (|r|=1.5e+08)
  ok  encke serves Tp_jd + solution_Tp_jd
  ok  encke orbit_type elliptical (e<1)
  ok  halley serves Tp_jd + solution_Tp_jd
  ok  halley orbit_type elliptical (e<1)
  ok  pluto/charon centered on pluto_barycenter
  ok  raw vectors written
  ok  elements JSONL history written
  ok  run manifest written
  ok  M1: feature_configs schema_version present
  ok  M1: feature_configs has all 12 object slugs
  ok  M1: every served feature entry is a dict (no lists survive)
  ok  M1: earth serves group 'earth_interior'
  ok  M1: earth serves group 'earth_atmosphere'
  ok  M1: earth serves group 'earth_exosphere'
  ok  M1: earth serves group 'earth_orbital_zones'
  ok  M1: earth serves group 'earth_geostationary'
  ok  M1: earth serves group 'earth_magnetosphere'
  ok  M1: earth serves group 'van_allen_belts'
  ok  M1: earth serves group 'hill_sphere'
  ok  M1: earth serves group 'orientation'
  ok  M1: earth inner_belt_distance is a measured entry in R_earth with source and pointer
  ok  M1: earth earth_atmosphere has lower_atmosphere + upper_atmosphere
  ok  M1: the pre-L-291 atmosphere_shell group is gone (no second home)
  ok  M1: jupiter has radiation_belts and NOT magnetosphere
  ok  M1: jupiter ring_system has all four ring slugs
  ok  M1: saturn ring_system has all seven ring slugs
  ok  M1: encke/halley present with empty {}
  ok  M1: inverted ring (inner >= outer) ABORTS
  ok  M1: malformed color string ABORTS
  ok  M1: malformed colors-list entry ABORTS
  ok  M1/L-238: interior shell (radius_fraction 0.19) PASSES
  ok  M1/L-238: radius_fraction 0.0 and -0.5 both ABORT
  ok  M1: a surviving features list (post-migration) ABORTS in derive_served
  ok  M2: sun serves a trust block
  ok  M2/L-256: sun (frame origin) trust method == not_applicable
  ok  M2/L-256: sun (frame origin) serves no trust window
  ok  M2: earth serves a trust block
  ok  M2: earth trust method == two_body_rate_v1
  ok  M2: earth has a finite positive window_days
  ok  M2: jupiter serves a trust block
  ok  M2: jupiter trust method == two_body_rate_v1
  ok  M2: jupiter has a finite positive window_days
  ok  M2: saturn serves a trust block
  ok  M2: saturn trust method == two_body_rate_v1
  ok  M2: saturn has a finite positive window_days
  ok  M2: mercury serves a trust block
  ok  M2: mercury trust method == two_body_rate_v1
  ok  M2: mercury has a finite positive window_days
  ok  M2: venus serves a trust block
  ok  M2: venus trust method == two_body_rate_v1
  ok  M2: venus has a finite positive window_days
  ok  M2: mars serves a trust block
  ok  M2: mars trust method == two_body_rate_v1
  ok  M2: mars has a finite positive window_days
  ok  M2: uranus serves a trust block
  ok  M2: uranus trust method == two_body_rate_v1
  ok  M2: uranus has a finite positive window_days
  ok  M2: neptune serves a trust block
  ok  M2: neptune trust method == two_body_rate_v1
  ok  M2: neptune has a finite positive window_days
  ok  M2: moon serves a trust block
  ok  M2: moon trust method == two_body_rate_v1
  ok  M2: moon has a finite positive window_days
  ok  M2: io serves a trust block
  ok  M2: io trust method == two_body_rate_v1
  ok  M2: io has a finite positive window_days
  ok  M2: titan serves a trust block
  ok  M2: titan trust method == two_body_rate_v1
  ok  M2: titan has a finite positive window_days
  ok  M2: pluto_barycenter serves a trust block
  ok  M2: pluto_barycenter trust method == two_body_rate_v1
  ok  M2: pluto_barycenter has a finite positive window_days
  ok  M2: pluto serves a trust block
  ok  M2: pluto trust method == two_body_rate_v1
  ok  M2: pluto has a finite positive window_days
  ok  M2: charon serves a trust block
  ok  M2: charon trust method == two_body_rate_v1
  ok  M2: charon has a finite positive window_days
  ok  M2: apophis serves a trust block
  ok  M2: apophis trust method == two_body_rate_v1
  ok  M2: apophis has a finite positive window_days
  ok  M2: voyager_1 serves a trust block
  ok  M2: voyager_1 trust method == fetched_positions
  ok  M2: voyager_1 trust window is null
  ok  M2: encke serves a trust block
  ok  M2: encke trust method == two_body_rate_v1
  ok  M2: encke has a finite positive window_days
  ok  M2: halley serves a trust block
  ok  M2: halley trust method == two_body_rate_v1
  ok  M2: halley has a finite positive window_days
  ok  M2: top-level served_window is non-null
  ok  M2: served_window brackets as_of (start < as_of < end)
  ok  M2: earth's window == its period cap (planet, cap=P)
  ok  M2: moon's window == P/8 (moon cap)
  ok  M2: halley's window == P/2 (comet cap)
  ok  L-363: the heliocentric participants are read from the config (12: earth, jupiter, saturn, mercury, venus, mars, uranus, neptune, pluto_barycenter, apophis, encke, halley)
  ok  L-149: served_window half-width == min of heliocentric participants
  ok  L-149: pluto's own window is smaller than the controlling one (sanity -- proves the exclusion is doing real work, not vacuously true)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] jupiter: trust measurement failed (simulated check-vector outage); served null window
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[warn] served_window: null -- trust measurement missing/failed for ['jupiter'] (FLAG-3: null-on-any-failure is the conservative default)
[done] run 20260709T000000Z (first-build): 19 objects
  ok  M2: forced check-vector failure -> jupiter trust carries 'error'
  ok  M2: forced check-vector failure -> served_window null (FLAG-3, exercised)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] pluto: trust measurement failed (simulated check-vector outage); served null window
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
  ok  L-149: forced pluto check-vector failure -> pluto trust carries 'error'
  ok  L-149: forced pluto check-vector failure -> served_window STAYS non-null (pluto excluded from participation, so its failure can't gate the site)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg

----------------------------------------------------------------------
THE CACHE SWAP COULD NOT FINISH, AND THERE WAS NO PREVIOUS
CACHE TO PUT BACK.

The new data was built and it passed every check. The step that
renames the new folder into place was refused 0 time(s) by
Windows. data/solar-system does not exist right now because it
did not exist before this run either.

WHAT TO DO: run the builder again. Nothing was committed or
pushed.

The new data is kept at
  C:\Users\tonyq\AppData\Local\Temp\tmp2xz7__i_\data\.staging_solar-system_20260709T000000Z
This run was recorded in data/cache_swap_log.jsonl
----------------------------------------------------------------------

[ABORT] fail: swap raised: simulated: file lock during promotion (e.g. OneDrive) -- no commit; there was no previous cache to put back
  ok  L-173: swap raising is caught, not propagated as an uncaught exception
  ok  L-173: swap failure -> commit never attempted (committed stays False)
  ok  L-173: swap failure leaves out_dir exactly as atomic_swap_dir left it -- missing, not half-written -- so next run's recover_incomplete_swap() restores cleanly from .prev, not from a hand-patched state
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[ABORT] fail: post-swap verification: promoted generated='2000-01-01T00:00:00+00:00' does not match this run's '2026-07-09T00:00:00+00:00' -- stale data landed instead of this run's build -- no commit
  ok  L-173: post-swap content mismatch caught even though the swap call itself did not raise
  ok  L-173: post-swap mismatch -> commit never attempted
  ok  L-173: unlike the raised-exception case, the (bad) promoted data is left in place here, not deleted -- verify_promoted_data only refuses to commit it
  ok  L-216: a rename refused twice then allowed -> the run still passes
  ok  L-216: the NEW generation is live after the retry
  ok  L-216: the run left exactly ONE line in the tracked swap log (found 1)
  ok  L-216: the swap log says ok
  ok  L-216: the swap log says 3 attempts -- a line with more than one attempt and outcome ok is a failure this build absorbed (3)
  ok  L-216: the builder SAYS a refusal was absorbed, and on which rename, on the screen the build ran from
  ok  L-216: the maintenance run reads the same thing back from the log ('last swap 2026-07-09T00:00:00+00:00: succeeded after a refused rename -- staging_to_live took 3 attempts -- a refusal this build absorbed')
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] staging_to_live refused on attempt 1 of 6 ([Errno 13] simulated: Access is denied); waiting 0s
[SWAP] staging_to_live refused on attempt 2 of 6 ([Errno 13] simulated: Access is denied); waiting 0s
[SWAP] staging_to_live refused on attempt 3 of 6 ([Errno 13] simulated: Access is denied); waiting 0s
[SWAP] staging_to_live refused on attempt 4 of 6 ([Errno 13] simulated: Access is denied); waiting 0s
[SWAP] staging_to_live refused on attempt 5 of 6 ([Errno 13] simulated: Access is denied); waiting 0s
[SWAP] staging_to_live refused on attempt 6 of 6 ([Errno 13] simulated: Access is denied); giving up

----------------------------------------------------------------------
THE CACHE SWAP COULD NOT FINISH. THE OLD CACHE IS BACK IN PLACE.

The new data was built and it passed every check. The step that
renames the new folder into place was refused 6 time(s) by
Windows. This is the file lock recorded as L-216.

NOTHING WAS LOST. data/solar-system holds the generation that
was there before this run, so GitHub Desktop will NOT show a
pile of deletions. Nothing was committed and nothing was
pushed, so the live site is unaffected.

WHAT TO DO: run the builder again. The lock is usually brief.

The new data is kept at
  C:\Users\tonyq\AppData\Local\Temp\tmp6nsrla8k\data\.staging_solar-system_20260709T000000Z
This run was recorded in data/cache_swap_log.jsonl
----------------------------------------------------------------------

[ABORT] fail: swap raised: staging_to_live refused on all 6 attempts ([Errno 13] simulated: Access is denied) -- no commit; the previous cache was put back
  ok  L-216: the swap fails -> the OLD generation is live again, byte for byte
  ok  L-216: the roll-back consumed .prev rather than leaving a second copy behind
  ok  L-216: the new generation is KEPT at its staging path
  ok  L-216: a rolled-back run never commits
  ok  L-216: the swap log says rolled_back ('rolled_back')
  ok  L-216: the log records every attempt that was made
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
  ok  L-216: both refused -> the live directory is missing
  ok  L-216: the previous generation is still on disk in .prev
  ok  L-216: the plain-words block is printed, and it says not to commit the deletions
  ok  L-216: it names BOTH hand recoveries -- discard and re-run, or rename the staging folder
  ok  L-216: it never says 'will self-heal' without saying what Tony does
  ok  L-216: the swap log says failed ('failed')
  ok  L-216: a failed swap never commits
  ok  L-216: a clean swap says so too -- success carries evidence instead of silence
  ok  L-216: and the maintenance run agrees, reading the log
  ok  L-216: the first build wrote a swap log line to compare the dry run against (found 1)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[dry-run] validated; wrote nothing outside C:\Users\tonyq\AppData\Local\Temp\tmpzqegr1lx\data\.staging_solar-system_earth_20260709T000000Z
  ok  L-216: a dry run leaves the swap log untouched
  ok  L-216: a refusal absorbed on an EARLIER rename is reported, not read as 'succeeded first time' ('last swap t: succeeded after a refused rename -- live_to_prev took 3 attempts -- a refusal this build absorbed')
  ok  L-216: the sibling report NAMES the folders the builder did not make (['123-solar-system', 'solar-system (1)'])
  ok  L-216: a builder-made sibling is still classed as the builder's
  ok  L-216: the live cache and .prev are not reported as strays
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[done] run 20260709T000000Z (nightly): 19 objects
  ok  nightly structural validation passes
  ok  nightly did not shrink earth
  ok  frozen past point unchanged byte-for-byte
  ok  guard: clean charon point -> no warning
  ok  guard: 35.7 AU point -> exactly one warning
  ok  guard: outer-bound trip tagged likely-contamination
  ok  guard KEPT the point (monitor, not reject)
  ok  guard: spacecraft |r|>200 AU -> sanity warning
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[RECOVER] restoring C:\Users\tonyq\AppData\Local\Temp\tmp3tsrh6xd\data\solar-system from C:\Users\tonyq\AppData\Local\Temp\tmp3tsrh6xd\data\solar-system.prev (crash mid-swap)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[done] run 20260709T000000Z (nightly): 19 objects
  ok  A-1/N1: nightly recovered the whole generation from .prev after a crash
  ok  A-1: archive not thinned by recovery (6302 >= 6302)
  ok  A-1: recovered nightly validates
[sweep] no sibling directories present
[ABORT] fail: nightly run but no live raw archive (possible unrecovered crash) -- refusing to build a thin cache
  ok  A-1: nightly with no generation ABORTS instead of committing thin

----------------------------------------------------------------------
WHAT TO DO NEXT, before you commit anything:

  1. Run the gallery maintenance run, from this same folder:
         python gallery_maintenance_run.py
     Every gating checker should pass. Its LAST line reads the
     swap log back and should agree with the [SWAP] line above.
  2. In GitHub Desktop, look at the change list. A good build
     shows changed and added files and NO pile of deletions.
  3. Commit and push.
  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

TONY-ACTION ROLLUP for this run:
  (do)     steps 1 to 4 above, in that order.
----------------------------------------------------------------------
  ok  A-2: main() exits nonzero on structural abort
  ok  A-2: main() exits 0 on pass
  ok  L-216: a good hand run ends by printing its next steps
  ok  L-216: the maintenance run comes BEFORE the commit in those steps (maintenance at 188, commit at 477)
  ok  L-216: the live check comes AFTER the push
  ok  L-216: a failed run does NOT print the next steps -- a failure prints its own advice
  ok  L-216: a dry run does NOT print them -- it changed nothing
  ok  L-216: a --commit run does NOT print them -- it has already committed, so 'before you commit' would be wrong
  ok  A-4: majorbody/id -> None
  ok  A-4: smallbody/None pass through unchanged
  ok  DP: straight line -> 2 endpoints
  ok  DP: keeps the bend
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] titan: FETCH FAILED (simulated Horizons outage); served last-good orbit, as_of_today nulled
[done] run 20260709T000000Z (nightly): 19 objects
  ok  A-3: failed Titan still SERVED (not vanished)
  ok  A-3: Titan conic served from last-good
  ok  A-3: Titan as_of_today NULLED (no stale marker)
  ok  A-3: run validates with a stale object
[sweep] no sibling directories present
[POLE] earth: pole of date NOT served (simulated Horizons outage) -- the page draws the frame's year-2000 axis and says so
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[warn] earth: pole of date NOT served (simulated Horizons outage) -- the page draws the frame's year-2000 axis and says so
[done] run 20260709T000000Z (first-build): 19 objects
  ok  pole fetch fails: the build still validates (pass)
  ok  pole fetch fails: Earth served, orbit kept, pole_of_date null
  ok  pole fetch fails: the run manifest says so (not served (fetch failed))
  ok  N4/#B3: correct km conversion passes
  ok  N4/#B3: un-converted (AU-valued) served point ABORTS
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[ABORT] fail: N3 object(s) dropped from a served set: ['titan']
  ok  N3: dropping a served object (titan) ABORTS the publication
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] encke: FETCH FAILED (solution-TP request_failed for encke); served last-good orbit, as_of_today nulled
[warn] halley: FETCH FAILED (solution-TP request_failed for halley); served last-good orbit, as_of_today nulled
[warn] served_window: null -- trust measurement missing/failed for ['encke', 'halley'] (FLAG-3: null-on-any-failure is the conservative default)
[done] run 20260709T000000Z (nightly): 19 objects
  ok  N5: solution-TP request failure serves last-good (not silent today-anchor)
[master (root-commit) 47e5b2b] data: nightly 2026-07-10
 1 file changed, 1 insertion(+)
 create mode 100644 data/f.txt
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>

[commit] PUSH FAILED (Command '['git', '-C', 'C:\\Users\\tonyq\\AppData\\Local\\Temp\\tmpgy12wydq', 'push']' returned non-zero exit status 128.) -- committed locally only; remote is STALE
  ok  N2: local commit succeeds but no-remote push is NOT reported as pushed
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[dry-run] validated; wrote nothing outside C:\Users\tonyq\AppData\Local\Temp\tmpunvu2779\data\.staging_solar-system_earth_20260709T000000Z
  ok  P2-2: --dry-run --object clears N3 + no-raw against an existing generation
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[dry-run] validated; wrote nothing outside C:\Users\tonyq\AppData\Local\Temp\tmp45zi_0m5\data\.staging_solar-system_earth_20260709T000000Z
  ok  P2-2: --dry-run --object works on a clean machine (no raw archive)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-03 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2548 -> 2 points (tol=0.02 AU)
[done] run 20260703T000000Z (first-build): 19 objects
  ok  P2-1: spacecraft first-build passes #T (arc ends today, not a stale stride point)
  ok  P2-1: spacecraft as_of_today is fresh regardless of stride phase
  ok  #B3: correct per-component conversion passes
  ok  #B3: swapped axes (magnitude-preserving) ABORTS component-wise
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] encke: FETCH FAILED (solution-TP request_failed for encke); served last-good orbit, as_of_today nulled
[warn] halley: FETCH FAILED (solution-TP request_failed for halley); served last-good orbit, as_of_today nulled
[warn] served_window: null -- trust measurement missing/failed for ['encke', 'halley'] (FLAG-3: null-on-any-failure is the conservative default)
[done] run 20260709T000000Z (nightly): 19 objects
  ok  P2-9: stale comet carries its comet block forward (not nulled)
  ok  L-274: run id with Z parses from the name (name)
  ok  L-274: run id WITHOUT Z parses -- the run_id=None fallback shape
  ok  L-274: an interposed object slug does not defeat the parser (L-148)
  ok  L-274: an unparseable name returns None so the caller falls back
  ok  L-274: a well-shaped but impossible date is refused, not accepted
[sweep] reaped 2 sibling(s) older than 3 day(s):
           .staging_solar-system_20260810T120000Z
           solar-system.quarantine_20260820T120000Z
[sweep] kept 1 recent sibling(s) as autopsies: solar-system.quarantine_20260901T120000Z
  ok  L-274: a 12-day-old quarantine is reaped even though mtime is now
  ok  L-274: a stale .staging sibling is reaped on the same rule
  ok  L-274: a same-day quarantine is KEPT as an autopsy (A-11)
  ok  L-274: the live served directory is never a sweep target

PASS (229 checks, 0 failures)

----------------------------------------------------------------------
2. Dry-run the six new objects against JPL Horizons? Writes nothing to the served cache. [y/n] y

>>> python tools\gallery_cache_builder.py --dry-run --object mercury
[RECOVER] removed retained data\solar-system.prev (cleared read-only on 6 entries)
[sweep] no sibling directories present
[dry-run] validated; wrote nothing outside data\.staging_solar-system_mercury_20260930T222405Z

>>> python tools\gallery_cache_builder.py --dry-run --object venus
[sweep] kept 1 recent sibling(s) as autopsies: .staging_solar-system_mercury_20260930T222405Z
[dry-run] validated; wrote nothing outside data\.staging_solar-system_venus_20260930T222409Z

>>> python tools\gallery_cache_builder.py --dry-run --object mars
[sweep] kept 2 recent sibling(s) as autopsies: .staging_solar-system_mercury_20260930T222405Z, .staging_solar-system_venus_20260930T222409Z
[dry-run] validated; wrote nothing outside data\.staging_solar-system_mars_20260930T222412Z

>>> python tools\gallery_cache_builder.py --dry-run --object uranus
[sweep] kept 3 recent sibling(s) as autopsies: .staging_solar-system_mars_20260930T222412Z, .staging_solar-system_mercury_20260930T222405Z, .staging_solar-system_venus_20260930T222409Z
[dry-run] validated; wrote nothing outside data\.staging_solar-system_uranus_20260930T222415Z

>>> python tools\gallery_cache_builder.py --dry-run --object neptune
[sweep] kept 4 recent sibling(s) as autopsies: .staging_solar-system_mars_20260930T222412Z, .staging_solar-system_mercury_20260930T222405Z, .staging_solar-system_uranus_20260930T222415Z, .staging_solar-system_venus_20260930T222409Z
[dry-run] validated; wrote nothing outside data\.staging_solar-system_neptune_20260930T222418Z

>>> python tools\gallery_cache_builder.py --dry-run --object pluto_barycenter
[sweep] kept 5 recent sibling(s) as autopsies: .staging_solar-system_mars_20260930T222412Z, .staging_solar-system_mercury_20260930T222405Z, .staging_solar-system_neptune_20260930T222418Z, .staging_solar-system_uranus_20260930T222415Z, .staging_solar-system_venus_20260930T222409Z
[dry-run] validated; wrote nothing outside data\.staging_solar-system_pluto_barycenter_20260930T222422Z

All six dry runs passed: mercury, venus, mars, uranus, neptune, pluto_barycenter.

----------------------------------------------------------------------
3. The first build. Pause OneDrive first (L-216) and note the time.
   Press Enter when OneDrive is paused, or type s to skip: 

>>> python tools\gallery_cache_builder.py --first-build
[sweep] kept 6 recent sibling(s) as autopsies: .staging_solar-system_mars_20260930T222412Z, .staging_solar-system_mercury_20260930T222405Z, .staging_solar-system_neptune_20260930T222418Z, .staging_solar-system_pluto_barycenter_20260930T222422Z, .staging_solar-system_uranus_20260930T222415Z, .staging_solar-system_venus_20260930T222409Z
[POLE] earth: pole of 2026-09-30 served (RA 0.70472, Dec 89.85019 deg); tilt 23.4381 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2561 -> 29 points (tol=0.02 AU)
[done] run 20260930T222437Z (first-build): 19 objects

----------------------------------------------------------------------
WHAT TO DO NEXT, before you commit anything:

  1. Run the gallery maintenance run, from this same folder:
         python gallery_maintenance_run.py
     Every gating checker should pass. Its LAST line reads the
     swap log back and should agree with the [SWAP] line above.
  2. In GitHub Desktop, look at the change list. A good build
     shows changed and added files and NO pile of deletions.
  3. Commit and push.
  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

TONY-ACTION ROLLUP for this run:
  (do)     steps 1 to 4 above, in that order.
----------------------------------------------------------------------

----------------------------------------------------------------------
CHECK: the six new objects in the served cache
  ok       mercury           window +/- 88 days, covers today
  ok       venus             window +/- 225 days, covers today
  ok       mars              window +/- 687 days, covers today
  ok       uranus            window +/- 30879 days, covers today
  ok       neptune           window +/- 60229 days, covers today
  ok       pluto_barycenter  window +/- 90143 days, covers today
  whole cache trusted +/- 88 days either side of this build
  All six are served, each trusted for today.

======================================================================
NEXT:
  - python gallery_maintenance_run.py

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.4s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.9s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      13.5s  PASS (229 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 64 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served, print count
                                    written as served, "in" written as
                                    served and a slot served in
                                    another unit from it.
  PASS Store writer suite        4.7s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 65 link(s) compared, store
                                    b6d8bfdb21f6.
  PASS Pointer join              0.1s  Every link is accounted for: 89
                                    link(s) against orrery 10012821,
                                    20 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.8s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 296
                                    number(s) examined; 13 graded, 7
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Guest book                0.1s  === GUEST BOOK: all 8 checks
                                    passed
  PASS Guest book updater        0.3s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 directory in data/ the
                                    builder did not make: solar-system
                                    (1). Check whether they belong
                                    there; the newer .gitignore rules
                                    keep the known conflict-copy
                                    shapes out of git but do not
                                    remove anything.

======================================================================
  19 of 19 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 directory in data/ the builder
  last swap 2026-09-30T22:24:55.787467+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  - In GitHub Desktop, commit the config, the cache and the test
    TOGETHER, and push. Resume OneDrive. -- 1530bb6db6a3133f8f1dc8d5b163c8f7559dac1b
  - python gallery_maintenance_run.py --live

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 13 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy
    SERVED   gallery/guestbook.js                           matches the working copy
    SERVED   data/guestbook.json                            matches the working copy

  PASS Served reachability       2.0s  all 13 files served and
                                    byte-identical to the working copy

  orrery export pinned at 10012821

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 10012821, byte for byte

  orrery HEAD 10012821
  examining 24 of 89 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  24 pointers: 20 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               0.9s  24 pointers against orrery
                                    10012821 -- 20 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            24 pointers against orrery 10012821 --
  last swap 2026-09-30T22:24:55.787467+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  - Move this script into documentation/, and tell Claude the new
    gallery SHA.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

===============================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L397_cache_in_step_all_objects_20260930.py
ok  tools\check_cache_in_step.py  the last line counts every object
ok  tools\check_cache_in_step.py  the report names every object compared
ok  tools\check_cache_in_step.py  compare_objects, self_test, and check() calling both
ok  tools\check_cache_in_step.py  IDENTITY: the fields compared
ok  tools\check_cache_in_step.py  import copy
ok  tools\check_cache_in_step.py  stamp: Module updated
ok  tools\check_cache_in_step.py  WHAT MAKES IT FAIL: the new failures
ok  tools\check_cache_in_step.py  WHAT IT CHECKS: part 1, every object
ok  tools\check_cache_in_step.py  title line: objects and shells

Stamps updated: the module's description and its Module updated line.
patch applied (9 edits in tools\check_cache_in_step.py)
Undo, if needed: Discard Changes in GitHub Desktop.

>>> python tools\check_cache_in_step.py
======================================================================
  CACHE IN STEP -- the served cache against data/objects_config.json
======================================================================

Compared all 19 object(s) by presence and identity (sun, earth, jupiter, saturn, mercury, venus, mars, uranus, neptune, moon, io, titan, pluto_barycenter, pluto, charon, apophis, voyager_1, encke, halley),
after showing that comparison able to fail;
and 4 object(s) serving features (sun, earth, jupiter, saturn), 35 named shell(s),
against data/solar-system/coverage_index.json and data/solar-system/feature_configs.json.

The served cache holds the config's 19 object(s) and their features exactly: 4 object(s) with 35 named shell(s), in both cache files.

======================================================================
NEXT:
  1. python gallery_maintenance_run.py

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              0.8s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.7s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      12.2s  PASS (229 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 64 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served, print count
                                    written as served, "in" written as
                                    served and a slot served in
                                    another unit from it.
  PASS Store writer suite        4.1s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 65 link(s) compared, store
                                    b6d8bfdb21f6.
  PASS Pointer join              0.1s  Every link is accounted for: 89
                                    link(s) against orrery 10012821,
                                    20 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    35 named shell(s), in both cache
                                    files.
  PASS Feature renderers         0.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.1s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 296
                                    number(s) examined; 13 graded, 7
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Guest book                0.1s  === GUEST BOOK: all 8 checks
                                    passed
  PASS Guest book updater        0.2s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.1s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 directory in data/ the
                                    builder did not make: solar-system
                                    (1). Check whether they belong
                                    there; the newer .gitignore rules
                                    keep the known conflict-copy
                                    shapes out of git but do not
                                    remove anything.

======================================================================
  19 of 19 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 directory in data/ the builder
  last swap 2026-09-30T22:24:55.787467+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. Move this script into documentation/. -- done
  3. Commit and push, then tell Claude the new gallery SHA. -- f6d1ca95d5e6e95b886b6998a3fdf8ea1a5efeb1

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 13 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy
    SERVED   gallery/guestbook.js                           matches the working copy
    SERVED   data/guestbook.json                            matches the working copy

  PASS Served reachability       1.8s  all 13 files served and
                                    byte-identical to the working copy

  orrery export pinned at 10012821

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 10012821, byte for byte

  orrery HEAD 10012821
  examining 24 of 89 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  24 pointers: 20 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               0.9s  24 pointers against orrery
                                    10012821 -- 20 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            24 pointers against orrery 10012821 --
  last swap 2026-09-30T22:24:55.787467+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L363_8_room_step3a_20260930.py
ok  interactive.html                     13 edit(s)
ok  gallery/assembler/presentation.py    2 edit(s)
ok  data/objects_config.json             2 edit(s)

Stamps updated: interactive.html's Updated list; presentation.py's
Module updated line; the drawer description in objects_config.json.
patch applied (3 files)
Undo, if needed: Discard Changes in GitHub Desktop on the three files.

======================================================================
NEXT:
  1. python gallery_maintenance_run.py

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.2s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.0s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      15.9s  PASS (229 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 64 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served, print count
                                    written as served, "in" written as
                                    served and a slot served in
                                    another unit from it.
  PASS Store writer suite        5.1s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 65 link(s) compared, store
                                    b6d8bfdb21f6.
  PASS Pointer join              0.1s  Every link is accounted for: 89
                                    link(s) against orrery 10012821,
                                    20 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    35 named shell(s), in both cache
                                    files.
  PASS Feature renderers         0.9s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 296
                                    number(s) examined; 13 graded, 7
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Guest book                0.1s  === GUEST BOOK: all 8 checks
                                    passed
  PASS Guest book updater        0.3s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 directory in data/ the
                                    builder did not make: solar-system
                                    (1). Check whether they belong
                                    there; the newer .gitignore rules
                                    keep the known conflict-copy
                                    shapes out of git but do not
                                    remove anything.

======================================================================
  19 of 19 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 directory in data/ the builder
  last swap 2026-09-30T22:24:55.787467+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. Commit and push. Move this script into documentation/. -- 432435a84aaeaaa7226bb1bbdb431390547f0d18
  3. python gallery_maintenance_run.py --live

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 13 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy
    SERVED   gallery/guestbook.js                           matches the working copy
    SERVED   data/guestbook.json                            matches the working copy

  PASS Served reachability       2.1s  all 13 files served and
                                    byte-identical to the working copy

  orrery export pinned at 10012821

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 10012821, byte for byte

  orrery HEAD 10012821
  examining 24 of 89 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  24 pointers: 20 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               1.0s  24 pointers against orrery
                                    10012821 -- 20 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            24 pointers against orrery 10012821 --
  last swap 2026-09-30T22:24:55.787467+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  4. Open palomasorrery.com/interactive.html?exhibit=solar-system
     on your phone and desktop. Look at: the opening view, ticking
     each planet, the colours, a text box (try Earth and Pluto),
     and the source line in the panel. Tell Claude what you see,
     and the new gallery SHA.

-- **Tony**: 1) does Horizons serve the distance to pluto with 9 significant digits as shown? Neptune shows 8 sig figs, some have 7 and earth has 6. are we using the same number of sig figs for AU as km? Which number is in the store? It seems that AU has one less sig fig than km. 
2) the "i" info panel has "no link on file" for this object. use the general description and the same NASA or Wikipedia link as in to other rooms. This should become standard and in the skill, and come from the objects dictionary. 
3) are we using the objects dictionary served to the config for object information?  

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 




