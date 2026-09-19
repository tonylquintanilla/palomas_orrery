# HANDOFF -- L-322 Earth slice, Stages A and B done; Stage C is next

Built on orrery `3e24909112628f6e39439618d38268191aed7f4d`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `82e786f17634f108a2e0df2ae7c693e5fcf62a60`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Both anchors are the state AFTER everything below was pushed, read live
from both remotes on 2026-09-19. Two orrery pushes ran this session,
each verified in the pushed tree before the next was cut:
`189c2987` (the documents Tony filed), `dfa779bd` (Stage A),
`3e249091` (Stage B). The gallery moved once, from `2ebd001f` to
`82e786f1`, and that was Tony's nightly cache build, not this session.

**Type: BUILD.** Session of 2026-09-19, Tony with Anthropic's Claude
Opus 5.

**Companion, and still the contract:**
`documentation/BUILD_MANIFEST_L322_earth_slice_20260919.md`, written by
Claude Fable 5.1. This handoff does NOT replace it. Its sections 6
through 11 -- Stage C, Stage D, out of scope, rules of delivery, Tony's
decisions -- are unchanged and govern the next session. What this
handoff does is record that Stages A and B are done, correct three
statements in the manifest that turned out to be false, and restate its
section 3 measurements at the current SHA.

**Continues from** `HANDOFF_L334_editor_built_20260919.md`.

---

## READ THIS FIRST, before any provenance or store work

ONE SKILL WAS BUMPED IN THIS SESSION AND REINSTALLED BY TONY AFTER IT.
A reinstall lands in the account and stays invisible to the session that
makes it, so this session could not verify it and did not try.

    provenance-discipline    2.13 -> 2.14

CONFIRM YOUR LOADED COPY READS 2.14 before doing provenance or store
work. If it reads 2.13, that is the stale-skill gate and it stops the
task -- say so and ask Tony to reinstall, rather than working from what
loaded.

The protocol is v3.63 and carries the bump in one entry. Tony has
updated the Project instructions in the interface as well as the repo.

The skill section you are about to use is `### The Read Field`, new at
2.14. Read it before the walk; it is what the walk writes.

---

## What Stages A and B did

**STAGE A, the ledger patch**, `patch_L322_8_ledger_stage_a_20260919.py`,
pushed at `dfa779bd`. Thirteen anchored edits to
`LEDGER_CONSOLIDATED.md`, all verified in the pushed tree.

- **L-337** gained Tony's addition of 2026-09-19 in his own words, plus
  a second quote he gave the same day naming where the orrery already
  draws the thing: each object has a symbol, a circle for the Sun and
  planets, carrying no dimension, drawn whether or not the body has
  shells, and most objects have none. The bullet that said nobody had
  looked at what the marker is was corrected, with its old wording kept
  in place so the change is visible.
- **L-249 is CLOSED** and migrated to section C by the indexer. Its
  built state was measured rather than carried: the four interior
  boundaries are in the store with their own `# Source:` lines,
  `shell_configs.py` takes all four Earth `radius_fraction` values from
  the matching `_RADII` expressions, and the mantle disagreement its
  Note left open is settled by derivation. Its one live residue, the
  cross-check owed on `EARTH_D660_DEPTH_KM`, is re-homed by name to
  L-253 and to L-322's Earth slice.
- **L-322** gained Tony's ruling on what "critical" means, quoted, and a
  new current Gap naming the manifest and its four stages. The
  2026-09-16 Gap is relabelled superseded rather than deleted.
- **L-340** gained the record described under "Three things the manifest
  had wrong" below.

**STAGE B, the skill bump**,
`patch_L322_9_read_field_skill_214_20260919.py`, pushed at `3e249091`.
Ten anchored edits across four files in ONE commit, under the four
binding steps in ledger-and-session-records.

- `skills/provenance-discipline/SKILL.md` goes to 2.14, cut from
  `dfa779bd`. It gains **The Read Field**, beside The Unit Field. The
  Unit Field now points at `constants_tokens.py`, which owns the token
  table, `RETIRED_TOKENS` and the "named number" marker, and names
  `# Read:` among the fields a row's single slice visit writes. Rule 8's
  enumeration names both routes to a derived row. The worksheet schema
  gains the `Read by` column promised on 2026-09-11.
- `PROJECT_INSTRUCTIONS.md` goes to v3.63, header stamp and anchor moved.
- `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` received v3.60.
- `LEDGER_CONSOLIDATED.md` records the bump on L-322.

**TONY APPROVED THE READ FIELD'S WORDING BEFORE IT WAS CUT**, which the
manifest required because it is his ruling being written down. He was
asked four questions and answered each: the quote is complete; the word
is about access rather than importance; the reading list is his whole
share; and a model's read counts. He glossed "need" in the same message
-- a number is in the store and needs a source -- and that sentence is
in the skill.

---

## Three things the manifest had wrong, and what was done

The manifest is a good contract and these are not a reason to distrust
it. They are recorded so the next session does not rediscover them.

**ONE. The handoff it continues from was not in the repo.**
`HANDOFF_L334_editor_built_20260919.md` was neither committed nor
uploaded when the session opened, and Stage A needed Tony's 2026-09-19
addition "quoted whole" from it. The words were recovered from the
transcript of the session that wrote it, confirmed by Tony, and only
then written into L-337. Tony filed the handoff and the manifest at
`189c2987` partway through.

**TWO. L-340 did not hold the record of the one-off config patch.** The
manifest said it did and told the builder to confirm it and add nothing.
It was not there. The reason is mechanical and worth keeping: the orrery
ledger went out at `bb614c7f` at 22:07 on 2026-09-18 and the gallery
patch `patch_L340_1_editor_polish_20260919.py` at `2ebd001f` at 22:22,
and no ledger patch followed. Fable reviewed this, agreed, and named the
cause in his own words: he trusted a handoff's claim over the file
itself. Stage A wrote the record -- the three findings fixed, the direct
write of `data/objects_config.json` named as the exception it is, the
exception owed to interactive-exhibit's next bump, and a
**Tony-action (decide)** on whether it stays narrow, with Fable's view
that it should.

**THREE. L-322 already carried the deployment line.** The manifest asked
Stage A to add a line saying the gallery half is deployed at gallery
`d2ca28b6` with the cache rebuilt at `9ff39cc4`. That note is already in
the block, dated 2026-09-17 and marked `[verified @1b077401]`. It was
not duplicated.

**A fourth finding was added to L-340**, from Fable's review and
reproduced on a throwaway copy of gallery `2ebd001f`.
`documentation/smoke_arrival.js` compares each room's opening against a
fixed `EXPECTED` list of DISPLAY NAMES written into the check. Ticking
another shell to open drawn, or renaming "Crust" or "Photosphere" in the
editor, turns the Arrival check red for a change that is correct. The
fix is for the check to read the config's own arrival block by key.
Recorded, not built; the manifest scopes it out.

---

## Section 3 restated, measured at `3e249091`

The manifest's section 3 was measured at `bb614c7f`, two pushes back.
Nothing in it has moved -- `constants_new.py` was not touched by either
stage, and the orrery run confirms no changes to it since HEAD -- but
the numbers are restated here at the current SHA so the next session is
not stopping on a stale anchor. Measured with `constants_rows.py` on a
clone, not carried.

**The store.** 112 top-level rows. 57 begin with `EARTH_`: 42 typed
numbers and 15 arithmetic expressions. Two of the 42 are the
magnetosphere standoffs on `constants_rows.TRANSITIONAL`, owed back to
arithmetic. `CLOSED_SLICES` is `()`.

**Fields, Earth rows.** Unit 28 of 57, status 28 of 57, figures 0 of 57,
read 0 of 57. Across the whole store, figures and read are 0 of 112. The
`# Read:` field the walk is about to write exists nowhere yet.

**29 Earth rows carry neither a unit nor a status** -- the same 29 the
manifest lists by name in its section 3.

**Five rows still declare the retired token `dimensionless`:**
`EARTH_MAGNETOPAUSE_SHUE_A5`, `_A6`, `_A8`,
`EARTH_BOW_SHOCK_JELINEK_EPS`, `EARTH_BOW_SHOCK_JELINEK_LAMBDA`.

**Three expression rows have no `# Derived:` line:**
`EARTH_LEO_INNER_KM`, `EARTH_LEO_INNER_RADII`, `EARTH_STRATOPAUSE_RADII`.

**Two constants outside the slice feed it.** `KM_PER_AU` and
`GM_SUN_SI`, both through the Hill sphere. Neither carries any field.

**The gallery, at `82e786f1`.** The export serves 23 rows and its stored
`store_sha256` matches the orrery's `constants_new.py`, so the two
repositories are in step. Of the config's 70 links to store rows, 53 are
not served by the export and still go through the older drift check; 24
of those 53 are Earth's. The nightly build between `2ebd001f` and
`82e786f1` touched only cached position data -- not
`data/objects_config.json`, not the export -- so every one of those
counts is unchanged.

One thing that will move in Stage C and is not a fault:
`data/constants_export.sha` in the gallery still names orrery
`bb614c7f`. The export itself is correct, because the store has not
changed; only the recorded commit is older. Stage C's export pull
updates it.

---

## The ledger, at `3e249091`

`ledger_index.py` prints OK on 335 L-blocks, 192 live items, and
rewrites the file with identical bytes on a second run. The orrery
maintenance run is 16 of 16 gating checkers passed.

Open items this session touched, and their state:

    L-322  OPEN. Its current Gap names the manifest and the four
           stages. A and B are done; C and D are the next session's
           material.
    L-337  OPEN, and no longer blocked on knowing what the marker is.
           Still open: where it comes from, and what it says on hover.
    L-340  OPEN. Its three screenshot findings are fixed and recorded;
           what remains is the Mode 5 pass at the window, the fourth
           finding above, and the (decide) on the config-write
           exception.
    L-249  CLOSED, in section C.
    L-253  OPEN, and now the named home for the `EARTH_D660_DEPTH_KM`
           cross-check.
    L-325  OPEN. Its (decide) -- close as superseded, or leave open
           until the standoffs revert -- falls due at the end of C2,
           which is when they revert.

---

## What the next session does

Stage C of the manifest, section 6, unchanged. In short: confirm the
loaded skill reads 2.14; then the walk, in two pushes. C1 is the 29
Earth rows with no fields, plus `KM_PER_AU` and `GM_SUN_SI`. C2 is the
28 magnetosphere rows, where the five `dimensionless` tokens become real
ones and the two standoffs revert to expressions and leave
`TRANSITIONAL`, ending with `CLOSED_SLICES = ("EARTH",)`. After each
orrery push the gallery follows, with OneDrive syncing paused before the
cache build and the config and cache committed together.

The reading goes in ONE file,
`documentation/L322_earth_read_record_<date>.md`, with the rows only
Tony can open in a second section, "For Tony to read", each with the
link, where to look and the number to expect. That list does not go in
chat.

Stage D, Earth's pole moving into the store, is its own push after C.

---

## Tony-action rollup

1. **(do)** File this handoff in the orrery's `documentation/`, commit,
   push. Give the next session this file and the manifest, and both
   SHAs, saying which is which.
2. **(decide)** Whether the one-off config-write exception stays narrow,
   on L-340. Fable's view is that it should.
3. **(decide)** L-325, at the end of C2.
4. **(do)** Pause OneDrive syncing before every cache build.
5. **(look)** Both rooms on the phone after each gallery push, and the
   Mode 5 pass over the editor window when there is time to do it
   properly.

---

Session written September 2026 with Anthropic's Claude Opus 5.
