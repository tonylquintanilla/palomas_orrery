# Handoff -- 2026-08-15 (second session) -- the builder built, and five claims that did not survive checking

**Built on `253bcdd4b2cfc38b95f6d049c6a3e94232bf5287`; pushed at
`87176e9ecc79f73dbc202db024175c0ed5a22625`, then
`a872205d17ee5298d1bdc86c614b43506e82b22c`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Both SHAs confirmed by live `git ls-remote`, and every pushed file
compared byte-for-byte against the tree its tests ran on. Gallery repo
untouched this session.

Lands in `documentation/`.

**Skill gate: clear, and nothing to carry forward.**
`ledger-and-session-records` 1.6, `safe-file-editing` 1.3,
`provenance-discipline` 2.3, `agentic-pre-test` 1.2,
`orrery-coding-conventions` 1.3 -- each loaded version checked against
its manifest row at HEAD, all matching. No skill was bumped
mid-session.

---

## What this session was

It opened as five blocking decides and ended with the request builder
built and the schema closed. Two of the five dissolved rather than
being ruled: item 3 collapsed once the population was measured, and
item 4 turned out to be a programming problem rather than a policy
question.

The through-line, and it is the reason the process record below is
long: five claims Claude made this session did not survive being
checked. Three were caught by a check, two by Tony. The prior session's
record read "every one was found by a person reading or by accident;
none was found by the system." That ratio moved.

---

## Tony's rulings, in order

1. **Master plan: fix the version and count, not the L-192 status.**
   Two documents advertised `provenance-discipline v2.1` against an
   actual 2.3 and "eight checkers" against an actual twelve. Corrected
   in both the plan and the summary. The L-192 status rewrite and the
   L-193 entry wait, because the plan is the slow document and the
   ledger is where in-flight state belongs.
2. **Break 2 (Fable item 3): field 2's object stays a NUMBER.** "If the
   checker cannot verify a claim it should not be asked to do so." A
   rendered qualitative sentence is a real class, recorded as L-194,
   deferred to a future refactor, and blocking nothing.
3. **Break 5 (Fable item 5): field 3 verdicts the `# Source:` line
   only.** `# Ref:` and `# Also:` are shown to the responder as
   read-only context and never verdicted. The blocks where the
   authority is not in the Source line are a malformation, not a schema
   case -- opened as L-195.
4. **Item 4 (over-precision) handed to Claude as a programming
   problem.** See the Claude-side ruling below.
5. **The `maintenance_run.py` runtime figure is not worth a patch.**
   Both documents still say "about 40 seconds"; measured runs this
   session were 55.4s and 69.6s.
6. **One build, not two.** The request builder and the checker's key
   rule ship together.

## The one ruling Claude made, on Tony's instruction

**No new verdict token from `compare()`.** Three of its seven call
sites are row-matching probes that gate on
`if verdict not in ('MATCH', 'CONVERSION'): continue`; a new token
would change which row a claim binds to, which is upstream of every
verdict printed. Instead: a separate precision report, called only at
the three final-verdict sites, saying that code and source state the
same value at different precision and which side is finer. It reports;
field 2 settles it. NOT BUILT -- scoped only.

---

## What landed in the repo

| At | What |
|---|---|
| `87176e9` | Master plan + summary: skill version and checker count corrected in both. L-194 (text-only assertions, DEFERRED). L-195 (citation legs, OPEN). L-192 gains the Break 2 and Break 5 rulings. |
| `a872205` | `worksheet_request_builder.py` (new). Rule 0 in `worksheet_checker.py`. Tests 61 -> 69. L-192 as-built. |

**The builder emits 65 rows over 65 distinct keys, zero collisions** --
the 53 -> 65 figure reproduced from the corpus rather than carried from
the ruling.

**The round trip is closed at the format layer, not assumed.** The
emitted request file was parsed back through the checker's
`parse_tables()`: one row table, 65 rows, zero unregistered headers,
all eight column roles resolved, rule 0 binding a row by key.

**Why one build.** `worksheet_keys.py` had zero consumers -- the
checker did not import it and `resolve()` was never called on the
checking path. Shipping the builder alone would have put keys into
outgoing worksheets that the returning checker could not read.

**`match_row()` is not deleted.** Rule 0 sits ahead of the four fuzzy
rules rather than replacing them, because 104 annotations still bind
through them. That is the first half of the transition the sequencing
decide is about.

Full detail is in L-192's as-built block; it is not repeated here.

---

## Open items

**Tony-action (decide)** -- none of these gate the builder

1. **Cross-worksheet disagreement.** Two responders, same (key,
   ordinal), opposite tri-states. Reporting both and routing to
   conversation is safe; choosing between them is not.
2. **What UNKNOWN does.** A state, not a route. Whether it blocks,
   passes or parks is a policy ruling; the checker's default becomes
   policy by silence otherwise.
3. **The pluto 614/638 merge**, open since 2026-08-14.
4. **Transition sequencing**, still open in L-192: whether both
   annotation formats stay readable through the re-cut or the re-cut is
   atomic.

**Claude-side, scoped but not built**

- The precision report (ruling above). Three call sites, `compare()`
  untouched.
- Dispatch itself. **L-195 should land first:** a block whose authority
  is not in its `# Source:` line would be verdicted CITATION RIGHT
  under Break 5 while the real authority went unchecked.
- **The builder's prompt says "batch" and the builder does not
  batch.** It asks for a batch name, uses it as the filename and the
  title, and emits all 65 rows regardless. The word was borrowed from
  `batch1_tier2` and L-156's "Batch 2 gas giants", where a batch is a
  real subset; here it labels nothing. Recorded rather than fixed at
  session end, because the fix is one line either way and the real
  question is not the wording. If batching should be REAL, the natural
  split is by module -- `constants_new.py` 24 rows,
  `pluto_visualization_shells.py` 18, `venus_visualization_shells.py`
  14, the rest 2 to 4 each -- but that decision waits on the first
  dispatch showing how Tony actually wants to hand the work out.
  Deciding it beforehand would lock a shape in before anything has
  been learned. (Tony's call, 2026-08-15: premature, next session.)

**Discharged this session**

- Master-plan decision 16 asked to confirm Jupiter's ring count before
  the Track 0 pilot starts, since the pilot is scoped by it.
  **Confirmed at `253bcdd`: 4.** Jupiter 4, Saturn 7, Uranus 11,
  Neptune 11, total 33 -- matching L-181's AST enumeration. The 5 in
  the decision text comes from counting `inner_radius_km` including the
  line that reads the key.

---

## Measured, for whoever needs the numbers

**Constant migration state at `253bcdd`.** `constants_new.py` holds 49
top-level assignments; 22 modules import from it. Outside it: 68
`radius_fraction` literals in `shell_configs.py` (117 across the shell
layer), 33 ring entries, ~22 belt and torus values. Artifact 2's
middle step -- Saturn's 7 ring entries plus both bodies' belt and torus
values, roughly 23 values -- is where the registry first has to hold a
list-plus-scalar shape.

**Citation legs at `253bcdd`.** 337 citation blocks in the repo; 20
carry more than one leg, 17 of those in `constants_new.py`, at least 9
in the dispatch corpus. Shapes: Source+Ref (4), Source+Ref+Also (3),
Source+Also (2). The scan breaks a block on an unlabeled continuation
comment, so 20 is a floor.

**Text-only assertions at `253bcdd`.** Display prose strings over 120
characters, as total / carrying a number+unit / carrying none:
`shell_configs.py` 143 / 92 / 51; `saturn_visualization_shells.py`
32 / 10 / 22; `mars_visualization_shells.py` 19 / 6 / 13;
`jupiter_visualization_shells.py` 25 / 19 / 6;
`earth_visualization_shells.py` 28 / 27 / 1. The 120-character cut is
Claude's, not the scanner's.

---

## Process record: five claims that did not survive checking

Recorded in the same spirit as the prior session's seven. The
difference worth noting is the ratio: three of these were caught by a
check that ran, two by Tony reading.

1. **"The probe path is a latent bug, caught by luck."** It is not.
   `claim_rows()` matches on a value test AND a body-token word filter,
   and its docstring says which does what: "The word filter is what
   stops a coincidental numeric equality in another body's row from
   being taken as this string's evidence." Pluto's core density
   probe-matched Eris's density and Mercury's magnetotail radius
   because integer rounding maps all three to 3; the token filter
   rejected both, as designed. Claude had instrumented `compare()`
   without checking whether its calls were load-bearing, then reported
   probe output as live findings -- the same gate quoted at Tony
   earlier the same day. **Caught by Tony.**
2. **Fable's Break 2 cites the wrong file.** The Mars stratosphere
   claim is not in `mars_visualization_shells.py:518`; the word appears
   nowhere in that module. It is in `shell_configs.py`, twice: line
   1256 under `hover_text` (live, read by `orrery_rendering.py`) and
   1268 under `tooltip` (still zero consumers at HEAD). Fable's
   conclusion survives its citation being wrong. **Caught by grep
   before the recommendation was made.**
3. **Master plan decision 16 compressed from three steps to two.**
   Claude reported the sequence as Jupiter pilot then general
   migration, dropping the middle step Tony's ruling inserted
   deliberately -- cross-check Artifact 2's remaining values into the
   proven structure. **Caught by Tony.**
4. **Doubled escapes in a patch script's line-ending normalizer** --
   `b'\\\\r\\\\n'` where `b'\\r\\n'` was meant. Identical to defect 5 in the
   prior session's record, in a script written to record that class of
   defect. **Caught by the ASCII/LF delivery gate**, not by reading the
   code.
5. **The stale-key check was circular.** It resolved the CLAIM's key,
   which is minted from today's source moments earlier and therefore
   always resolves -- a check that cannot fail. Corrected to resolve
   the keys the WORKSHEET carries, which is what a rename looks like
   from this side. **Caught by the test written for it**, which failed
   on the first run.

**And one guard that proved itself.** All six new rule-0 checks are
synthetic on purpose: no worksheet in the corpus carries a Key column,
so the live run cannot reach rule 0 and a green run proves nothing
about it. The load-bearing check -- a stale-key row whose prose WOULD
match -- was mutation-tested by breaking the rule deliberately to
confirm it goes red. It does.

**A scanner finding from the pre-test.** The new module first
classified as role `undetermined`, which scored its display-width
constant as an uncited physical claim and moved Tier-1 206 -> 207. A
`Role: devtool` line in the docstring returned it to 206. A new dev
tool without a role line is scored as though it made claims about the
world.

---

*Prepared August 15, 2026 with Anthropic's Claude Opus 5. Built on
`a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery.*
