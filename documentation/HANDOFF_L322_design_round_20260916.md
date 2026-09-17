# L-322's design round is complete, and provenance-discipline is 2.13

Built on orrery `6f124a79d828f99ccb760c4158742f2240024825`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `72a49552aa6ba4b21c2f58e3c5fe53f7d198590c`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

The session opened at orrery `ebdc55cc` and gallery `72a49552`. The
orrery moved once, to `6f124a79` (skill 2.13, protocol v3.61, ledger
L-335), read back with `ls-remote` and the pushed SKILL.md compared
byte-for-byte to the pre-test copy. It moves once more after this
evening's closing patch; that SHA is Tony's to report. The gallery did
not move.

Tony Quintanilla, PE | Claude Fable 5.1 | 2026-09-16, evening
Type: DESIGN + one skill bump. Zero code in the store.
Handles: L-322 (design round complete, (a) through (e) ruled), L-335
(opened and DONE), L-325 (ruling withdrawn; one decide open).
Supersedes `HANDOFF_L331_rooms_described_L334_editor_20260916.md`'s
STILL OPEN item 1 and its rollup item 4; everything else in it stands.

---

## STEP 0 -- before you do anything

1. `git status --porcelain` in both repositories. Expect nothing.
2. `git ls-remote` both. Expect gallery `72a49552` and the orrery at
   the SHA Tony reports after `patch_L322_3_design_round_ledger_20260916.py`.
3. **Version-check provenance-discipline at load. It must read 2.13.**
   This session loaded 2.12, installed 2.13 and cannot verify the
   install. If the loaded copy reads 2.12, STOP before any provenance
   or store work: Tony reinstalls at Settings > Skills and the next
   session checks again.
4. `ledger_index.py` after the closing patch: two runs; the second is
   `OK: 330`, with 192 live items.

---

## WHAT HAPPENED

**The significant-figures procedure is the textbook one, in the skill.**
Tony asked for standard methods and named Wikipedia's Significant
figures page. The measurement that made it urgent: 27 rows carry a
`# Derived:` line, and `test_derived_figures.py` could see 2 of them,
because it enumerated by a word on a `# Status:` line that 25 rows do
not carry. The skill also disagreed with itself, one section saying a
derived row stays an expression and the September 12 section saying it
stores a rounded literal; 21 rows followed the first and 2 the second.
Eight rules landed as The Figure Count Is a Declared Field [QUALITY]
(provenance-discipline 2.13, L-335, protocol v3.61). The design record
is `documentation/DESIGN_L322_d_significant_figures_20260916.md`.

**Tony withdrew his September 12 ruling (L-325)** in the message that
adopted the procedure: a rounded literal at rest is a rounded
intermediate for every row that chains from it. The store holds the
derivation; the EXPORT rounds to the declared count and carries the
count beside the value. The skill keeps a WITHDRAWN stub where the rule
stood.

**The other four questions were ruled in one conversation**, recorded
on L-322 by the closing patch: the dimensional check runs in the orrery
runner, checks derived rows only, and is built with astropy inside the
check, floats staying in the store, reading a token table that carries
each unit's dimension and defining constant (dividing by the defining
constant is a conversion, not a cancellation); the five served values
outside the store move into it, in their bodies' slices, with the smoke
suites run before and after; a bare literal's check is Tony's read,
scoped to drawn rows and their inputs, recorded as a `# Read:` line at
the row's slice visit.

**One round was wasted, and Tony ended it.** Claude turned a passing
remark about a digit once read from a zoomed page image into an
unrecorded verification failure and searched the repo and the past
chats for the row. There was no failed check. "If there's no failed
check what is the problem? We are chasing our tails!"

---

## VERIFIED VS CLAIMED

Verified inside the session:

- Both skill patches and the closing ledger patch on throwaway copies
  of the pushed tree, each refusing a second run; `skills_index.py`
  reporting the manifest row 2.12 -> 2.13; `ledger_index.py` twice,
  OK: 330; the closing patch also run against a CRLF copy of the
  ledger (CRLF preserved, no bare LF).
- The push at `6f124a79`: HEAD read back, and the SKILL.md, protocol
  header, manifest row, L-335 block, v3.58 move and the design file
  all present at that SHA.
- The 27 derived rows, the 2 the checker sees, and the 70 served
  pointers with 5 outside the store: measured at `ebdc55cc` and
  gallery `72a49552`, not recalled.

Claimed and NOT verified here:

- The provenance-discipline reinstall (STEP 0, item 3).
- Tony's maintenance run of 2026-09-16 (14 of 14 gating checkers,
  Derived figures 2 of 2): his output, pasted, not re-run here.

---

## THE LESSON

**A remark is not a defect.** A hunt needs a failing check to chase.
Claude built a founding case out of an anecdote because the rule it
was arguing for wanted one, and spent a round proving a failure that
had not happened. The rule survived on its own merits, smaller: the
`# Read:` line is a field like the other three, and it carries no
urgency.

**A convention that is not in the skill does not travel -- a third
time.** The new section said the figure field works "like `# Unit:`"
and the skill had never defined `# Unit:`; ruling 1 of September 11
lived only in the ledger. The Status Line now carries The Unit Field.

---

## STILL OPEN, in Tony's order (as of 2026-09-16, evening)

1. **L-322, the BUILD.** Mechanism whole, then the Earth slice. The
   mechanism is specified piece by piece in
   `documentation/BUILD_MANIFEST_L322_mechanism_20260916.md`. The
   mechanism: the export generator (`value`, `unit`, `figures` per row,
   plus the bytes-hash of `constants_new.py`), the hash checker in the
   orrery runner, the join check that every pointer resolves BY NAME,
   the dimensional check (astropy inside, token table replacing
   `SCALAR_UNITS`). Then the Earth slice: 53 Earth rows visited once
   each for `# Unit:`, `# Status:`, `# Figures:` and, where read,
   `# Read:`; the 12 Earth derived rows stay expressions;
   `test_derived_figures.py` rewritten to Rule 8; L-325's two literals
   revert when the export lands. Nothing in the item awaits a ruling.
2. **L-334, the editor.** Unchanged from the prior handoff: question 1
   ruled (numbers locked), 2 to 5 settled at the start of the build
   session.
3. **L-331's residue**, **L-333**, and the carried items (L-330, L-231,
   L-273's gallery half, L-061): unchanged from the prior handoff.
4. **Waiting for the next provenance-discipline bump (2.14):** the
   worksheet schema column naming whether a verdict is Tony's or a
   model's (promised 2026-09-11; did not ride 2.13).

---

## TONY-ACTION ROLLUP

1. **(do)** ORRERY: run `patch_L322_3_design_round_ledger_20260916.py`,
   then `python ledger_index.py LEDGER_CONSOLIDATED.md` TWICE (expect
   OK: 330 both times).
2. **(do)** Move the three spent patch scripts from the repo root into
   `documentation/`: `patch_L322_1_figures_skill_protocol_20260916.py`
   and `patch_L322_2_ledger_20260916.py` (pushed at `6f124a79` at the
   root) and `patch_L322_3_design_round_ledger_20260916.py`. A drag in
   GitHub Desktop's file view or File Explorer; git records it as a
   rename.
3. **(do)** File this handoff and
   `BUILD_MANIFEST_L322_mechanism_20260916.md` to `documentation/`. The
   manifest is the build contract for L-322's mechanism; the next
   session builds from it.
4. **(do)** Commit, push, report the SHA.
5. **(decide)** L-325: close it as SUPERSEDED by L-322 now, or leave it
   OPEN until its two literal rows revert to expressions. Neither
   changes the work; the note on L-325 records the choice either way.
6. Next session: STEP 0, then open L-322's build on the mechanism.

---

Session written September 2026 with Anthropic's Claude Fable 5.1.
