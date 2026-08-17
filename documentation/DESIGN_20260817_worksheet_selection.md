# Design note -- selecting which rows a request carries

**Built on `98b29f00dbd7e3be235a6f88d615718ccfc397dd` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Confirmed by live `git ls-remote`.

Type: **DESIGN.** Nothing here is built. No ledger handle yet; this note
proposes one.

Lands in `documentation/`.

---

## The problem in one paragraph

`worksheet_request_builder.py` reads the annotated corpus and renders
every row it finds. There is no way to ask it for fewer. At the current
HEAD that is 100 rows over 52 sites in one file, and both August
reviewers said a pilot of roughly fifteen should go first. Producing
fifteen today means editing the generated file by hand -- which breaks
the instruction the request prints in its own header ("do not edit the
Key, Claim or Code value columns"), and produces a slice no second run
could reproduce.

So the pilot needs a way to select rows. The design question is what
that selection is made of.

## The rule this note follows

**A selection is code, not typing.** A pilot chosen by hand is a
one-off no matter how carefully it is chosen, because nothing records
why those rows and nothing can produce them again. A selection defined
in the module is reviewable in a diff, pinned to a SHA like everything
else, and reproducible by anyone who runs the tool.

This is the same distinction that separates a `# Source:` line from a
recalled number: not whether the answer is right, but whether anyone
can check it later.

## What the corpus already knows about its own rows

Measured at HEAD, not recalled. These are the properties a selection
could sort on, and the numbers are why some are useful and some are
not:

| Property | Spread at HEAD |
|---|---|
| File | 7 files: pluto 30, constants_new 23, venus 23, eris 7, mars 7, moon 6, mercury 4 |
| Row origin | 77 from display strings (ordinal keys), 23 from constants |
| Citation was reassembled from a continuation | 82 yes, 18 no |
| Context legs present | 87 rows have none, 6 have two or more |
| Source legs | every row has exactly one; none has zero or several |

Two of those readings matter more than they look.

**82 of 100 rows carry a reassembled citation.** The continuation join
is not an edge case to be sure the pilot includes -- it is the normal
row, and a pilot that happened to draw the other 18 would be testing
the unusual shape.

**Every row has exactly one Source leg.** That is the Shape A work
landing. A selection does not need a branch for "no authority to
verdict," because at this SHA there is no such row.

## The two mechanisms

**Named selections.** A dictionary in the module, each entry a name, a
one-line statement of what it is for, and a predicate over the
properties above. `main()` lists them by number at the prompt and asks
which one, the same way it already asks for a batch name and an anchor
SHA. Blank means the whole corpus, so today's behaviour is the default
and nothing changes for a full run.

**Stratified caps.** For the pilot the useful shape is not "rows where
X" but "a few rows from each kind." So a selection may also declare a
grouping and a cap: group by (file, row origin, joined-or-not), take up
to N from each group. Rows are taken in sorted key order, never at
random, so the same SHA and the same selection give the same rows every
time. A random sample would be a one-off that looks like a mechanism.

## Where selection happens in the run

**After the refusal, never before.** The loud failure added under L-196
blocks a build when a citation continues onto an unmarked line. That
check reads the corpus. If selection ran first, excluding a site would
quietly excuse it -- and a ratchet with a bypass is not a ratchet.

Order: collect the corpus, run the refusal, then select, then number
and render.

## What the request file records about its own selection

The header already carries the batch name, the anchor SHA, and the
extractor version. It gains:

- the selection name, and the count it produced against the corpus
  size -- "12 of 100 rows";
- the group counts, where a stratified cap was used;
- the statement that keys, not row numbers, identify rows.

That last line is not decoration. `row_id` is assigned by position at
render time, so a request covering 12 rows numbers them R1 to R12 while
the same rows in a full run are numbered somewhere inside R1 to R100.
The stable identifier is the key -- `module.py::enclosing::label::cN`.
Anything that outlives the file, including the `# Resolved:` leg,
cites the key. This is the renumbering-across-handoffs problem the
ledger already carries a lesson about, and it arrives here by the same
route.

## The one case where a list of keys is legitimate

Round two. When the checker routes a set of rows back as SEND BACK,
re-dispatching exactly those rows is not hand-picking -- the list is an
OUTPUT of the mechanism, not a preference typed at a prompt. So a
selection may read a key list from a file the checker wrote, and may
not read one a person typed.

The test is whether the list can be regenerated. A checker-written list
can. A remembered one cannot.

## What is deliberately not in this design

- **No filtering by how interesting a constant is.** That is judgment,
  and judgment belongs in the ruling that names a selection, not in the
  selector at run time.
- **No reader count.** One generated file goes to one reader or three;
  the request does not know or care. Per-reader identity is already
  carried on the return side by the `# Cross-checked:` grammar.
- **No new columns.** Selection changes which rows are printed and
  nothing about what a row asks.

## Open, for Tony

1. **A handle.** This wants a ledger item; L-201 is the next free
   number after the `# Resolved:` leg proposed as L-200.
2. **The pilot's selection, by name.** Writing the mechanism does not
   choose the pilot. The named selection the pilot runs is a separate
   ruling, and it is the one that decides what the pilot can prove.
3. **Whether the first named selection ships alone.** The mechanism is
   useful with exactly two entries -- the whole corpus, and the pilot's
   -- and more can be added when a second batch needs one.

---

*Prepared August 17, 2026 with Anthropic's Claude Opus 5. Built on
`98b29f00dbd7e3be235a6f88d615718ccfc397dd` at
https://github.com/tonylquintanilla/palomas_orrery.*
