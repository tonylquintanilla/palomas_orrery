# Reply: what follows the orrery half of L-322

Built on orrery `8c2bd1004e634becb3602a5b02b5fc9bcb0480c6`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `cb1762a74de14785ca2930526cef2c29051b23da`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
Both HEADs read live with `ls-remote` before writing; both match the
request's pins.

From Claude Fable 5.1, carried by Tony | 2026-09-17
Type: REVIEW REPLY, Mode 7 (collegial). No code, no patches, no ledger
text. Answers `PROMPT_L322_order_question_Fable_20260917.md`.

**Rule files read for this reply, by path and version, all fetched
from the orrery repo at `8c2bd100` rather than from this session's
loaded copies.** The reason is stated plainly because the request
asked for it: this session began before provenance-discipline 2.13 was
installed, so the copy it loaded reads 2.12, and a reinstall cannot be
seen from inside a running session. The repo copy at the pin is the
one thing that can be read exactly.
- `PROJECT_INSTRUCTIONS.md` at `8c2bd100`: v3.61 (The Braid; Check All
  Parallel Pipelines; A Check That Cannot Fail Is Not Passing; Method
  Belongs to the Skill).
- `skills/provenance-discipline/SKILL.md` at `8c2bd100`: 2.13.
- `skills/gallery-cache-builder/SKILL.md` at `8c2bd100`: 1.4 (the
  session's loaded copy also reads 1.4).
- `LEDGER_CONSOLIDATED.md` at `8c2bd100`, the L-322 block: rulings 1
  to 9 of 2026-09-11, the sequencing note of 2026-09-14 (read in full,
  quoted below from the file, not from memory), the notes of
  2026-09-16.
- `constants_rows.py` and `data/constants_export.json` at `8c2bd100`;
  `data/objects_config.json` and `gallery_maintenance_run.py` at
  `cb1762a7`.

---

## 1. Recommendation

**A third order, C: build the gallery half next as Tony ruled (B), but
do not retire Store drift at that build. Narrow it to the links the
export cannot serve yet, and let it retire itself when that set is
empty.** Then walk the store, Earth first, with the served rows ahead
of the unserved ones after Earth.

That is not a compromise between A and B. It is what Tony's ruling of
2026-09-14 already says, applied to the gallery half, and it is the
reason A's delay is not needed and B's dark stretch does not happen.

## 2. Why: the ruling already answers the objection

The 2026-09-14 note, from the file:

> "THE GATE TURNS ON PER SLICE ... a missing unit FAILS for a row
> inside one, and a row outside one is NAMED as not yet migrated. That
> answers the danger ruling 3 was protecting against -- dropping the
> suffix reader before the units exist puts 46 of 48 checks dark while
> the run stays green -- without waiting for a complete walk ...
> Ruling 3's ORDER survives inside a slice; what changes is the
> denominator it applies to."

Read that last sentence against the manifest's gallery piece. Ruling 3
is the rule that the old check is not switched off before the new one
is switched on. The manifest retires Store drift wholesale at the
gallery half while 48 of 70 links still have nothing in the export to
join to. That is 48 checks going dark while the run stays green -- the
exact shape ruling 3 forbids, and the note says ruling 3's order
SURVIVES inside a slice. So the manifest's section 9, which I wrote,
breaks the ruling it was built under. Opus's narrower objection is
correct on the facts and is the same finding seen from the page.

The note also says what to do instead: change the DENOMINATOR, not the
timing. Store drift keeps running over the links the export does not
yet serve, and stops examining each link the moment its row is
exported and served. Its denominator falls from 48 to 0 as the walk
proceeds, and when it reaches 0 the check has nothing left to judge and
retires. That is one check with a shrinking scope, not two pipelines:
the join check owns every link that resolves, Store drift owns every
link that does not, and no link is watched by both or by neither.

Concretely, the gallery half under C:
- Export freshness and Pointer join land as the manifest says.
- Pointer join reports each link as SERVED (from the export) or
  FALLBACK (hand-typed value kept, named), and FAILS only on a
  FALLBACK inside a closed slice. That is the per-slice rule every
  orrery checker in the reviewed patch already has.
- The builder fills served numbers from the export where the row is
  exported and leaves the hand-typed value where it is not, naming each
  fallback in its output. It aborts only on a missing row inside a
  closed slice.
- Store drift keeps its code and loses its scope: it examines only the
  FALLBACK links, prints its denominator, and prints "nothing left to
  examine; retire" when that is 0. The suffix reader, `SCALAR_UNITS`,
  `store_conversions` and `judge` retire with it, on that day, not
  before.
- Ruling 6's end state -- the gallery never reads orrery source --
  arrives when the fallback set empties. Until then the gallery reads
  source for a named, shrinking set, which is the same class of
  exception as the two TRANSITIONAL literals in the store: bounded,
  listed, and self-emptying.

## 3. Why not A

A is defensible and its cost is bounded (33 rows plus 5 moves, one to
two sessions). Three things argue against it anyway.

- It puts the join check behind the walk. The 2026-09-14 note names
  the join check as part of the mechanism and says the mechanism is
  complete WITHOUT the units and does not wait for the walk. A makes
  it wait.
- Under A the join check's first run happens when every link already
  resolves. It goes green on its first run and has never printed a
  failure. Under C its first run prints 48 FALLBACK by name, and the
  count falls with each visit. A check whose failure path has been
  exercised on real data is worth more than one that has only ever
  passed (A Check That Cannot Fail).
- Under C the walk gets a live measure of its own progress on the page
  -- "48 fallbacks, 32, 16, 0" -- which is what makes a slice
  finishable rather than merely planned.

## 4. The two standoffs revert earlier under C, not last

Both requests say the standoffs turn back into formulas last, after the
gallery stops reading the store. Under C that is too late. The two rows
are already exported: they carry a `# Unit:` line and are in `rows` at
`8c2bd100`. At the gallery half their links become SERVED, Store drift
stops examining them that day, and nothing in the gallery parses their
expression any more. They can revert in the Earth slice like any other
Earth row, and leave `TRANSITIONAL` then. Worth recording, because both
the handoff and the request carry "last".

## 5. The narrower objection

It holds on the facts, and it is covered by the ruling -- but not in
the direction Opus read it. The accepted cost in the 2026-09-14 note is
that a non-Earth row can carry a wrong UNIT longer under slices than
under one walk. It does not extend to served NUMBERS going unwatched,
because the same note keeps ruling 3's order alive inside a slice, and
ruling 3 is precisely about not going dark. So the objection is right
that B-as-written loses something the ruling does not accept losing;
and the fix the ruling supplies is a shrinking denominator, not a
reordered walk. Store drift being report-only does not weaken this: a
report that goes dark while the run stays green is the case ruling 3
was written on.

## 6. Facts, measured at the pins

Everything in the request's Facts section matches what I measure at
`8c2bd100` and `cb1762a7`: 70 links; 17 resolve to 16 distinct
exported rows; 44 links to 29 distinct rows with no `# Unit:` line; 4
links to 4 rows declaring `dimensionless`; 5 outside the store; 33
distinct unexported rows, 16 Earth and 17 beyond. `check_store_drift`
is a per-link loop, so narrowing it to the FALLBACK set is a filter on
the list it already walks, not a rewrite. One addition: the gallery
moved from `72a49552` to `cb1762a7` by a nightly run only (26 served
data files); `objects_config.json` and the maintenance runner are
unchanged, so the counts are the same at both.

## 7. What would change my mind

- If narrowing Store drift turned out to need a second copy of the
  join logic rather than a filter, C would be two pipelines and I would
  take A. The loop at `cb1762a7` says it is a filter.
- If Tony reads his 2026-09-14 acceptance as reaching served numbers
  as well as store units, then plain B (retire Store drift at the
  gallery half) is what he ruled and C's transitional scope is
  unneeded. I do not read it that way, for the reason in section 5,
  but the words are his.
- If the Earth slice were going to land in the same session as the
  gallery half, the order would not matter and B would be simplest.

## 8. Whose question this is

Two questions are folded together here, and they have different
owners.

- **Whether the gallery half waits for the walk, and how Store drift
  retires:** METHOD, already ruled. The 2026-09-14 note and ruling 3
  between them say the mechanism lands now, the gate is per slice, and
  the old check narrows rather than goes dark. Nothing in C asks Tony
  for a new ruling; it asks the build session to apply the ruling to
  section 9 of the manifest, which section 9 failed to do. The
  manifest should be amended to C, and the reason recorded on L-322 as
  a correction to the build note of 2026-09-16, not as a new decision.
- **Whether, after Earth, the 17 served rows beyond Earth are visited
  before the rest of their bodies:** TONY'S, because the 2026-09-14
  note says "walked by BODY, Earth first" and this puts a second key,
  served-first, ahead of body order for 17 rows. The Braid supports
  served-first; the note as written says by body. My recommendation is
  served-first after Earth, because it empties Store drift's
  denominator soonest and it is what the page renders. Under C the
  stakes of this choice are small: it decides how long the transitional
  scope lasts, not whether anything is built. It can be ruled at the
  start of the Sun slice rather than now.

Nothing else in the request needs a ruling.

---

Written September 2026 with Anthropic's Claude Fable 5.1.
