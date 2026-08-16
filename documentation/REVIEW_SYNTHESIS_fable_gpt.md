# Review synthesis -- Fable 5 and GPT 5.6 Sol on the worksheet dispatch loop

**Built on `a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Remote HEAD re-confirmed by live `git ls-remote` before writing this.
Both reviews anchored to the same SHA. No code changed during the
review window.

Lands in `documentation/`.

**Every finding below was re-verified against the pinned source by me
before being recorded here.** Neither review is relayed on its word.
Where a reviewer's claim did not survive that check, it is marked.

---

## The headline

Both reviewers said do not dispatch. They agreed on Findings A and B
and on almost nothing else -- **the two blocker lists are nearly
disjoint.** GPT found four structural defects in the checker that
Fable missed while running Fable's test suite green. Fable found four
defects in the emitted request document that GPT missed while reading
the same builder source.

That disjointness is the most useful result of the exercise. It is
also a warning: if only one review had been commissioned, roughly half
of what follows would have gone undetected either way.

---

## Merged blocker register

Nine, all verified by me at the pinned SHA.

| # | Finding | Found by | Layer |
|---|---|---|---|
| 1 | 45 of 65 rows show a truncated citation | both | builder |
| 2 | Six `# Source:` lines name an event, not an authority | both | annotations |
| 3 | With both verdict columns present, only the value verdict is read | GPT | checker |
| 4 | Display-string claims bypass the key rule entirely | GPT | checker |
| 5 | `shift_check()` is never called by the checker | GPT | checker |
| 6 | A returned request is not in the checker's evidence path | GPT | architecture |
| 7 | Ordinal rows are indistinguishable to the responder | Fable | builder |
| 8 | The request never states the legal verdict tokens | Fable | builder |
| 9 | The builder scripts an answer: "answer NO" | Fable | builder |

### 3 -- the value verdict eats the citation verdict

`read_verdict()` tests for the value-verdict column first and
**returns immediately**. It reaches the citation branch only when no
value-verdict column exists. The old worksheets had one column or the
other, so the precedence was correct then. The new nine-column table
deliberately has both.

So a row reading `Value correct? = yes`, `Citation correct? = no`
processes as a completed positive check and the `no` never becomes a
finding. This is a false clean on the schema the builder was written
to emit, and it defeats Break 5 -- the ruling that created the
separate citation column in the first place.

### 4 -- string claims never touch rule 0

`check_claim()` passes `claim.key()` into `match_row()` for constants.
For a display string it branches to `check_string_claim(claim, tables)`
-- no key argument -- which searches rows by today's numeric value plus
a body-token word filter and then takes `hits[0]`.

26 of the 65 dispatch rows are string ordinals. All of them carry keys
the checker will not read. GPT's phrasing is the accurate one: "builder
mints keys, checker resolves them" is true of the constant path and
false of the string path. The two matching regimes do not merely
coexist in the corpus -- they coexist inside one keyed worksheet.

### 5 -- the ordinal safeguard exists and is not wired

`shift_check()` is defined in `worksheet_keys.py` and appears nowhere
in `worksheet_checker.py`. The test calls the helper directly, which
proves the helper works and not that anything invokes it. Combined
with 4, the honest answer to the ordinal-stability question is: today
the ordinal is not protected.

Fable answered this seed differently -- that two nets already exist and
are good. Fable was reading the design; GPT checked the call graph.
**GPT is right on the facts.** This is the clearest case in the pair of
one reviewer describing intent and the other checking wiring.

### 6 -- the returned file is not evidence

`check_claim()` opens `worksheets.get(claim.worksheet)` -- the filename
written in the source annotation. Nothing searches for a returned file
by key. And `uncited_report()` exempts only filenames containing
"prompt", so a returned `REQUEST_<batch>.md` lands in the uncited set.

**Caveat, and it matters:** this is arguably not a defect. "Dispatch
itself" is already recorded in the handoff as scoped-but-not-built. GPT
found the missing half and classified it as broken. The substance is
still live, because GPT's recommendation is a design proposal for that
unbuilt half -- see the ask below.

### 7 -- ordinal rows the responder cannot answer

Every ordinal row of a string shows the same 90-character excerpt: the
first 90 characters of the whole string. **26 ordinal rows carry only
8 distinct claim excerpts between them.**

For `eris_hill_sphere_info`, four rows all display UI instructions
("SELECT MANUAL SCALE OF AT LEAST 0.1 AU...") against code values
67.8, 0.095, 38 and 37,000.

Worse, three units carry duplicate raw values -- verified exactly as
Fable reported:

- `pluto...haze_layer::description` -- "200" twice
- `pluto...atmosphere::description` -- "200" and "1700" twice each
- `venus...upper_atmosphere::description` -- "100" and "120" twice each

For those pairs the two rows are byte-identical from the responder's
side except for an ordinal naming a position they cannot see. Answers
to them are unverifiable by construction.

Fable's fix is good: excerpt a window *around* each claim's offset,
with the number marked. `physical_claims` already recomputes offsets.

### 8 -- the vocabulary is never stated

The request says "use one token per verdict cell" and never lists the
tokens. I grepped the emitted file: `confirmed`, `partial`, `approx`,
`unverified`, `unsourced` appear zero times. Only `derived` appears,
and only inside `Derived:` legs, not as vocabulary.

The seven-token registry exists because a twenty-token registry was
measured to be words invented at the keyboard. This request reproduces
the conditions of that measurement exactly.

### 9 -- a scripted verdict

For any row with no `# Source:` leg, the builder emits: *Cited source:
none recorded. Answer "Citation correct?" as NO and say so in Notes.*
Exactly one row triggers it -- `CHROMOSPHERE_RADII`, the one value in
the dispatch that is deliberately not physical.

An answer written by the tool that asks the question is a check that
cannot fail, and here it also records a citation defect against a
value that makes no citation claim. Both reviewers reached the same
place on the chromosphere by different routes: it needs a claim
*type*, not a verdict. Neither wants `N/A` added to the vocabulary.

---

## Two live disagreements

### Disagreement 1 -- how to fix the truncation

**Fable: join greedily and announce.** Append unlabeled comment lines
to the most recent leg, stopping at the next label, a blank comment,
or block end. Print how many lines were joined, and report any
unlabeled comment attached to nothing. The argument is an asymmetry:
over-joining is *visible* -- the extra text appears in a human-read
document -- while under-joining, today's behaviour, is silent.

**GPT: do not guess.** An unlabeled indented comment is the same form
used for wrapped notes and free prose, so a join rule replaces one
silent ambiguity with another. Introduce explicit continuation syntax,
normalize the 33 sites to it, and have the builder fail loudly on an
ambiguous continuation.

Both are defensible and they are genuinely opposed. Fable's rests on
the emitted file being read by a human before dispatch. GPT's rests on
not building an inference layer into an anti-inference system.

### Disagreement 2 -- what stops a lazy responder

Both confirmed the attack is real and undetectable today.

**Fable: honest canaries.** Perturb a few pre-filled Code values,
record the true ones in a sealed pin file, and *disclose in the request
that canaries exist without saying which rows*. A confirmed canary
quarantines the worksheet. Requires exempting canary rows from drift
detection.

**GPT: remove the self-certifying field.** Drop `Value correct?` from
the responder's job entirely -- ask for an independently obtained value
plus a specific retrievable source, and let the checker decide
agreement. Ideally do not show the Code value during value lookup at
all. GPT notes that citation checking cannot be blinded this way, which
is an argument for separating the two tasks rather than pretending the
anchoring is absent.

These are not compatible. Fable adds a detector; GPT removes the
affordance.

---

## Where the reviewers were wrong

**GPT's line counts do not hold.** It reported the builder at 288 lines
and the checker at 1,510 at the pinned SHA, and concluded the review
packet had been written against a later working copy. I checked twice
-- `wc -l` on a fresh clone at `a872205`, and a raw fetch of the pinned
blob -- and both give **312 and 1,650**, matching the packet.

GPT's Finding 14 premise is therefore false, and its recommendation
(re-run the review against a newer commit) should be declined. But note
what does survive: the two behaviours GPT said were missing at the
anchor *are* missing at the anchor. It reached a true conclusion from a
false premise, which is worth knowing about that reviewer.

**Fable's "all six" is really five of six.** On Finding A, five of the
six `# Cross-checked:` lines name the Ref-line authority. `ROCHE_LIMIT`
reads "formula verified" -- the checkers verified the formula, which is
what its Source line states. The swap is still right there on
principle, but my table overstated the mechanical evidence by one row.
Fable is correct and the correction is mine to carry.

**Fable answered the ordinal seed from design rather than call graph**
(see blocker 5 above). Its disclosure paragraph anticipated this
failure mode -- same model family as the author -- and it still
happened, on the one seed where the design document and the wiring
disagree.

---

## Where they converged, unprompted

Both, independently:

- Shape A over Shape B for Finding A, and both rejected inferring the
  authority from any leg as reintroducing interpretation. GPT adds
  that Roche's equation and densities belong in `# Calculation:`.
- Keep the seven-token vocabulary. Add definitions, not tokens.
- The chromosphere needs a claim type, not a verdict, and `N/A` should
  not enter the vocabulary.
- 65 is the right *population* -- auditing claims the project already
  trusts beats sourcing the 206 open gaps, because wrong-but-cited
  suppresses suspicion while an honest gap does not.
- But 65 is the wrong *first run*. Both want a small pilot chosen to
  force every structural branch. GPT adds the sharper version: include
  at least one row that should route to SEND BACK and one to
  CONVERSATION, because a run where everything is expected to pass
  does not test routing.
- Cross-family dispatch. Many of the 65 annotations record Claude as
  the August 2 checker, so those rows should go to GPT or Gemini.

Both also independently endorsed the architecture: the non-writing
checker, the no-push-gate constraint, and the SEND BACK / CONVERSATION
split. Neither proposed a redesign when explicitly invited to.

---

## Not blocking, recorded

- **The anchor SHA is typed by hand.** `main()` accepts any non-empty
  string and nothing ties the files on disk to it. Fable's fix: read
  `.git/HEAD` directly (two file opens, no command line), display it,
  ask Tony to confirm rather than transcribe. Fable also reports that
  `PROVENANCE_AUDIT.md`'s run history already carries SHAs that are not
  ancestors of today's HEAD -- unverified by me, worth a look.
- **A mangled Key header silently downgrades the regime.** Rule 0 fires
  only if a header maps to the key role. Retitle the column "Keys" and
  65 keyed rows bind by prose instead. Fable's fix: any worksheet
  carrying the builder's own `Extractor version:` marker must bind by
  key or fail loudly.
- **No end-to-end contract test.** GPT classes this blocking; I would
  call it the thing that makes the other fixes verifiable rather than a
  defect in itself. One test from the builder's emitted table through
  to checker findings would have caught blockers 3, 4 and 6 on the day
  they were written.
- **Announce the filtered numbers.** `physical_claims` drops display
  instructions by design and the builder discards the count. One line
  per string would make that blind spot announce.
- **Wording:** the request says four responder fields; the table has
  five blank columns.

---

*Prepared August 15, 2026 with Anthropic's Claude Opus 5. Built on
`a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery.*
