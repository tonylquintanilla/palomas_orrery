# Handoff -- L-363 integrated: the Solar System room's Half 2, now the gallery's front door

**Built on orrery `e5c3f92a2ad1dd47ad8cb35d17c159e07f1a9cf9` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`f46cf299c2b6e93e5f3ba405c4ad62032e7666ae` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
HEADs read live with `git ls-remote` on 2026-09-29 and shallow-cloned.
This session wrote nothing to either repository.

**Type: DOCUMENTATION (zero code).** It reconciles three documents
against the repositories and the ledger, and merges them into one brief
for the session that builds Half 2.

**Supersedes, for what remains:**
- `HANDOFF_L363_half1_done_half2_after_stage_d_20260928.md` (Half 1's
  record; its sections 5 and 6 are replaced by section 4 below).
- `DESIGN_solar_system_room_front_door_20260929.md` (the design stays
  the record of the rulings and the reasoning; its sections 6 and 8 are
  merged into sections 4 and 5 below).

**Companion, not superseded:** `HANDOFF_L345_D20_done_20260928.md` (the
record of D20, already filed). `HANDOFF_L345_gallery_done_D20_next_20260928.md`
is fully superseded by it and is only a record now.

**Rules this session loaded:** ledger-and-session-records 1.12,
interactive-exhibit 1.6, provenance-discipline 2.22, each matching the
protocol v3.73 manifest. That discharges the obligation D20's handoff
carried (confirm 1.12 and 1.6). No skill changed.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds next.

---

## 1. What has landed since the three documents were written

Each document was written before the pushes below, so each describes an
earlier state. Checked against the repositories this session:

- **Patch 6 landed.** The gallery is at `f46cf299` ("L363_6"). The
  script is in the gallery's `documentation/`. Tony's run: patch applied,
  offline maintenance run 19 of 19, live run 2 of 2 with every served
  file byte-identical, and his phone and desktop check "correct" (the
  view stays turned after + and -, after naming a body, after turning
  the phone; the palomasorrery.com link sits under the grid chip and is
  in the camera's picture). This answers the design document's
  Tony-action "confirm whether patch 6 landed".
- **Patch 5's script moved** into the gallery's `documentation/`, as
  the Half 1 handoff asked.
- **D20 landed.** The orrery is at `e5c3f92a` ("L345 D20"). Tony's
  orrery maintenance run: 18 of 18 gating checkers, the derived-figures
  and export checks reading exactly as the patch predicted. His Mode 5
  on Earth's interior: "correct". Skills reinstalled.
- **In the ledger:** L-345 is DONE. L-322 is still OPEN, with Stage D's
  finishing condition recorded as met and the Sun's slice as its next
  Gap. So the start condition the Half 1 handoff set for Half 2 --
  "Half 2 continues after Stage D completes" -- is met.
- **A cache swap succeeded** on 2026-09-29 at 20:55 UTC, first time.
  The cache holds the config's features for four objects (Sun, Earth,
  Jupiter, Saturn) and 35 named shells.

## 2. Where the three documents disagree, and which is right

Under ledger-and-session-records, the ledger wins on what is done and
the master plan wins on order. Five disagreements:

1. **The ledger's L-363 is three days behind.** It was last updated
   2026-09-26. It does not carry patches 2 to 6, the room's card, the
   lost-card episode and the editor's save check, or any of the
   2026-09-27 to 29 rulings. It still says Half 2 waits for "L-322
   section 6", which Tony superseded on 2026-09-28 ("after Stage D
   completes"), and it still lists "a gallery card for the room" as Half
   2 work; the card was made at gallery `3f7f50ab`. The update the Half
   1 handoff owed was never filed. Section 6 below files it once, merged
   with the design's.
2. **The master plan (v34) orders Half 2 third.** Its "What comes next"
   reads: the Sun's slice, then Jupiter and Saturn (Artifact 2), then
   "the Solar System room's second half (L-363), beside those". v34 was
   written before the front-door design, which changes what the room is
   for. Whether that moves it up the order is Tony's decision, and it is
   the one question this handoff carries to chat (section 5).
3. **The design names the wrong skill version to confirm.** Its section
   8 says confirm interactive-exhibit 1.5; D20 moved it to 1.6. This
   session confirmed 1.6. Nothing else in the design depends on it.
4. **Two Half 1 questions are answered by the design, one is replaced,
   one stands.** See section 4.1.
5. **Apophis falls out of the design's first list.** The room draws
   Apophis today. The design's drawer opens on ten rows (the Sun, eight
   planets, Pluto) and puts Apophis under "near-Earth asteroids", a group
   whose design round has not happened. Section 4.1, item 7.

## 3. What the room is, after the design (settled)

These are Tony's rulings of 2026-09-26 to 29, gathered from the three
documents. Each is stated in full in its source; this is the merged
list, in sentences.

- The Solar System room (`interactive.html?exhibit=solar-system`)
  becomes the gallery's front door: a second way in beside the card
  taxonomy, which stays the complete index. It draws only what JPL
  Horizons can place, and the shells and groups of such things.
- The scene stays a clean orrery: symbols on orbits, today's hover text,
  nothing else. Everything about where to go next lives in the drawer.
- The room draws now, the minute it is opened, in UTC, and the line
  under the title says so. That line is, in Tony's words, "the reason
  for the exhibit at all."
- It opens with only the Sun and Earth drawn, the drawer closed, and
  Earth's row highlighted so the closed drawer's handle reads "Earth".
  The view fits 1.1 times Earth's distance.
- The drawer opens on ten rows: the Sun, the eight planets and Pluto.
  "See more" adds the groups in place along the spine. A ticked row is
  never hidden by collapsing the list.
- Tapping a body in the scene opens its hover and highlights its row;
  nothing is drawn or removed. Tapping a highlighted row expands it
  ("Enter the ... room", then card titles, or "No room or cards yet").
  Ticking a row draws it and reframes the view to 1.1 times where the
  largest ticked thing is today. Everything ticks except the Sun.
- Home returns to the unzoomed default view of the last ticked object
  still ticked; if nothing is ticked, it ticks Earth and shows the
  opening view.
- Each thing has one address: a row links to the same room or card the
  taxonomy does, and what a body holds is read from the exhibits and the
  card metadata, never kept in a second list.
- The swap: the new room becomes the default once the nine bodies are
  in, without waiting for a date picker. In one commit, the Explorer's
  card link becomes `interactive.html?exhibit=solar-system-explorer`, the
  page's fallback key becomes `solar-system`, and the README's bare link
  is checked. The Explorer stays a card, reachable from the gallery but
  not from inside the room.
- Groups, comets, missions and encounters are later design rounds, each
  its own. The Trojans are the settled pattern for a group: a cloud
  served once, drawn like a shell, with its notables only in the group's
  own room.

## 4. Half 2: the merged brief

### 4.1 Questions before building

Before bringing any of these to Tony, check whether a skill settles it.

1. **The opening view.** Settled by the design: Sun and Earth, 1.1
   times Earth. What remains is method: where that choice is served,
   since the room has no entry in `data/objects_config.json` and the
   arrival block is the only served model for an opening. Read
   interactive-exhibit 1.6's arrival section first. (Skill)
2. **The default room.** Settled by the design's swap (section 3).
   Applied last, after Tony's Mode 5.
3. **Pluto.** Still open. The served `pluto` is stored relative to the
   Pluto-Charon barycentre, and the assembler refuses by design to
   translate it into a Sun-centred scene. What the row draws is method:
   orrery-coding-conventions (the barycenter rule) and
   horizons-orbital-mechanics. It is the one body with a known blocker,
   so it goes last and does not hold up the other five. (Skill)
4. **A link for each body.** Replaced. The Half 1 handoff asked where a
   per-body link lives in the config. The design answers differently: a
   row's links are the rooms and cards that already exist, read from the
   exhibits table and the card metadata. So the question becomes how a
   card says which body it belongs to (design question 15), which is
   gallery-pipeline method. Whether the availability icons are in Half
   2 at all is open: the design's "buildable soon" list names the drawer
   and ticks but not the icons. (Skill, then scope)
5. **Where the list lives.** The ten rows and the spine should be served
   data, not page code, so a new group does not mean editing
   `interactive.html` (design question 3). Half 2 needs at least the ten
   rows; the shape should be chosen so the spine fits later. (Design,
   then skill)
6. **Ticking also opens the row?** Assumed in the design, not ruled.
   (Tony)
7. **Apophis.** Today it is drawn; under the design it belongs to a
   group not yet designed. Keep it as a single row under "See more"
   until that round, or leave it out of Half 2. Neither choice
   forecloses the group. (Tony, but small)
8. **Tick order for Home.** Home's fallback needs the room to remember
   the order things were ticked; nothing does today. (Method)

### 4.2 The build, in order

1. **Mercury, Venus, Mars, Uranus and Neptune into
   `data/objects_config.json`.** Check each Horizons target and centre
   against horizons-orbital-mechanics before writing it. Then one cache
   rebuild (gallery-cache-builder; Tony pauses OneDrive first). None of
   the five is in the config today: it holds the Sun, Earth, Jupiter,
   Saturn, the Moon, Io, Titan, Pluto, Charon, Apophis, Voyager 1,
   Encke and Halley.
2. **Check each new body's own trust window covers today,** not only
   the cache's overall window (L-364: Halley's and Encke's did not).
3. **The room.** Extend `SOLAR_SYSTEM_BODIES` (today
   `["earth", "jupiter", "saturn", "apophis"]`, at `interactive.html`
   line 1865 at `f46cf299`); the ten-row drawer with ticks; the
   highlight and the handle; the opening on Sun and Earth; the Home
   rule; the two info paragraphs rewritten. Every relayout carries the
   live camera (`sunKeepCamera()`, patch 6).
4. **Hovers under the current skills.** A body's hover prints its
   distance in AU to six decimals, then in km, computed by the
   assembler. interactive-exhibit 1.6 says a hover never converts a
   served number to print it; positions are computed, not served, so
   the rule may not reach them. Decide from the skills; bring Tony only
   a case they do not settle.
5. **Pluto,** once question 3 is settled.
6. **Tony's Mode 5** on his phone, upright and sideways, and on the
   desktop, with every visitor-facing word listed before the build.
7. **The swap,** in one commit (section 3).

The build writes `data/objects_config.json` and rebuilds the cache. The
Sun's slice (L-322's next Gap) writes the Sun room's links in the same
file through the mirror. The two must not be in flight at once,
whichever goes first.

### 4.3 Not Half 2

Groups (main belt, Trojans, near-Earth asteroids, trans-Neptunian
objects), comets, missions, encounters and the date reach are each a
later design round. The design makes comets (L-364) and Voyager 1
(L-365) part of the room's future; their ledger rows should say so. The
orbit info cross (L-366) is unchanged.

## 5. The open decision for Tony

**The order.** Does the front door move ahead of the Sun's slice and
Artifact 2, or stay third as v34 has it? The plan's own rule is that
bundling to complete a planned step outranks the RICE score, so this is
a sequencing call, which is the plan's authority and Tony's.

The other items in 4.1 marked "Tony" wait until the Half 2 session
opens.

## 6. For the ledger (one combined update, no new class beyond the design's)

- **L-363** gains: patches 2 to 6, each in a line (the quoted room key
  in Studio; the date line and the editor's save check; the line in
  every room; short scene titles; the live camera on every relayout and
  the site credit), with their gallery SHAs; the card, "Solar System",
  9:16, in the `solar_system` door, at `3f7f50ab`; the lost card and the
  save check; the Half 1 rulings (Half 1 handoff section 2); the front
  door rulings (section 3 above); the start condition met. Its **Gap**
  becomes section 4 of this handoff. Its **Ref** adds this handoff, the
  Half 1 handoff and the design.
- **L-364 and L-365** each gain a line: part of the Solar System room's
  future per the front-door design (comets by apparition; missions by
  launch date).
- **L-367** gains: the headless recipe (Half 1 handoff section 7) is how
  the rooms were checked meanwhile.
- **L-378** gains: the sandbox cannot load Google Fonts, so a
  text-width layout decision is settled only on the phone.
- **Four new rows, one per class, from the design's section 9:** cloud
  shapes for the main belt, near-Earth asteroids and trans-Neptunian
  objects; the served-list layout (unless Half 2 takes it, question 5);
  encounter data (dates, spacecraft records, target centring); a card
  naming the body it belongs to (unless Half 2 takes it, question 4).
- **For interactive-exhibit's next bump** (not now): the headless
  recipe as a field note, and a line in the touch-path section naming
  every caller that must carry the live camera (patch 6 found one that
  did not). Neither is in 1.6.

## 7. Tony-actions

- (do) File `DESIGN_solar_system_room_front_door_20260929.md` in the
  orrery's `documentation/`; it is not there at `e5c3f92a`.
- (do) File this handoff in the orrery's `documentation/`.
- (do) Replace the filed copies of the two 2026-09-28 handoffs with the
  uploaded ones if you want your run records kept with them: the filed
  L-363 handoff lacks the patch 6 run, and the filed L-345 gallery
  handoff lacks the D20 push SHA.
- (do) File the unrun `patch_L322_D_p4_gallery_print_counts_20260927.py`
  in the gallery's `documentation/` as a record; it is not there at
  `f46cf299`.
- (decide) Section 5: the order.
- (decide, still open, unrelated to L-363) L-389 (atmosphere tops on
  the equatorial or the mean radius) and L-385 (the Sun's Auto view).

## 8. For the next session

- Confirm the loaded skills match the manifest.
- Re-anchor both repositories; line numbers will have moved.
- File the ledger update in section 6 before building.
- If Tony has put Half 2 next: start with section 4.1, one question at
  a time, skills first.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.
