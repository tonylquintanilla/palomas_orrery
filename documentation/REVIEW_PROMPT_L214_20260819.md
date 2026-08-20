# Mode 7 review request -- L-214, the leg vocabulary of a citation
# request builder

**Built on `97c520177b18d69e6b5d3943557fdea47f56e8bf` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Companion file, required reading:
`L214_MEASUREMENT_20260819.md`, attached with this prompt. Cut from the
same commit.

You have no access to this repository. Everything you need to judge the
question is in this document and the attached measurement. If something
essential is missing, say so plainly rather than inferring it -- a gap in
this prompt is a defect in the prompt, not a puzzle for you to solve.

---

## 0. Who you are writing for

This is Paloma's Orrery, a Python solar-system and stellar visualization
suite. It is built by Tony Quintanilla, PE -- a retired civil and
environmental engineer, an artist, and an anthropologist. He is not a
professional software developer and not a formally trained astronomer.
He builds the project through conversation with AI partners rather than
by writing code unassisted, and he holds sole commit authority and final
judgment.

The code you will see quoted below is disciplined, and a reviewer
reading it cold will reasonably infer that a skilled programmer wrote
it. That inference is wrong and it matters here. The structure and the
docstrings are the product of iterative collaboration, not of Tony's
personal programming background. What Tony owns and drives is the
workflow: the design conversation, the project protocol, the ledger, the
multi-model review you are now part of, and every integration judgment.

The practical consequence for your answer: **Tony's explicit request in
this session is for STRUCTURAL recommendations rather than line-level
technical judgments.** He has said, in these words, that parsing and
judging technical language is not his expertise -- that is what the
review worksheets are for. Write your review so that the load it puts on
him is a decision about shape, not an exercise in reading code. Address
the mechanism to the implementing model; address the choice to Tony.

One more convention worth knowing: this project treats agreement between
two AI models as a sanity check and never as proof. Two models agreeing
usually confirms a shared misreading. You are one of two independent
legs and you are not being asked to converge with the other one.

---

## 1. What the system does

The project keeps its numeric constants in a module, `constants_new.py`,
with the authority for each value written directly above it as a Python
comment. Other modules import the constant rather than retyping the
number. A separate tool reads those comments and builds a REQUEST: a
worksheet dispatched to an outside model asking, for one constant at a
time, whether the cited authority actually supports the value. The
returns come back as worksheets, are checked mechanically for format,
and are then read by Tony.

The comments use a small labelled grammar. A label, a colon, and text:

    # Source: IAU 2015 Resolution B3, Table 1
    # Ref: IERS Conventions (2010), Chapter 1
    EARTH_EQUATORIAL_RADIUS_KM = 6378.1366

The vocabulary splits into three jobs, though only two of them are
currently named in code.

**VERDICTED.** One label, `Source`. This is the authority the outside
model is asked to rule on.

**CONTEXT.** Five labels: `Ref`, `Also`, `See`, `Derived`,
`Calculation`. Shown to the outside model, never verdicted.

**RECORD.** `Cross-checked`, `Removed`, `Corrected`, `Resolved`. These
carry what PREVIOUS reviews concluded. They are deliberately withheld
from the request, because a row dispatched a second time must not be
shown what the last reviewer decided. That would contaminate the second
leg and this project's whole method rests on legs being independent.

Here is the relevant code, quoted exactly.

```python
VERDICTED_LEG = 'Source'
CONTEXT_LEGS = ('Ref', 'Also', 'See', 'Derived', 'Calculation')

LEG_RE = re.compile(
    r'^\s*#\s*(%s)(\+)?:\s*(.*)$'
    % '|'.join((VERDICTED_LEG,) + CONTEXT_LEGS))
```

A long citation that wraps onto a second line must carry a
leg-specific continuation marker, `# Source+:` under `# Source:`. The
marker is leg-specific on purpose, so that a continuation attached to
the wrong authority can be named rather than silently joined.

The gathering loop, quoted exactly:

```python
    for line in (attached_text or '').splitlines():
        match = LEG_RE.match(line)
        if not match:
            # A line that continues the leg above it but carries no
            # marker is the failure this refuses on. Anything else
            # closes the run, so a marker separated from its leg by
            # unrelated prose cannot join across the gap.
            if open_label is not None and continues_a_leg(line):
                unmarked.append(line.strip())
                continue
            open_label = None
            open_leg = None
            continue
```

It returns five things: the verdicted leg, the context legs, `problems`
(continuation markers that could not be joined -- reported into the
worksheet), `unmarked` (continuation text with no marker -- the builder
REFUSES to write while any exists), and a count of lines joined.

---

## 2. The defect

Notice what the code above does with a line whose label is real but
unrecognised, for example `# Note: B3 rounds to 6378.1 km; full
precision from IERS Conventions`.

`LEG_RE` does not match it, because `Note` is in neither named set. It
is not an unmarked continuation either, because it has a label. So it
takes the last branch: `open_label = None; continue`. The line is not
joined, not reported, not refused. It is dropped, and nothing anywhere
says it was dropped.

The RECORD legs -- `Cross-checked` and the rest -- are dropped by
**exactly the same branch**. Their invisibility is correct behaviour;
the decision is documented in a docstring elsewhere in the codebase. But
it is enforced by falling through an unmatched branch rather than by any
named rule. Correct behaviour and a silent defect share one code path
and are indistinguishable from inside it.

This surfaced in a real failure. A constant naming the Alfven surface
was stored as an ALTITUDE above the Sun's surface while the renderer
drew it as a distance from Sun CENTRE, so the shell rendered one solar
radius too small. A previous session had found that exact distinction
and written it into the file -- on comment lines labelled `# Note:` and
`# HELIOCENTRIC:`. Neither label was readable. Three outside models were
then dispatched to check that row and none of them was shown the two
lines that stated the answer.

The attached measurement quantifies it, using the project's own tooling
rather than a text search: **12 dropped lines at 12 of 55 claim sites.**
Three of the five constants still unresolved on the current
reconciliation queue are on that list. In each case the dropped line is
what the outside models spent their dispatch rediscovering.

---

## 3. What has already been ruled, and is not open

These are Tony's decisions from this session. Treat them as given. If
you believe one of them is load-bearing wrong, say so in a clearly
marked CHALLENGE section rather than by quietly designing around it.

1. **`Note` becomes a recognised context label.** Its text travels with
   the row.
2. **Unrecognised labels are REPORTED, not refused.** Tony's words:
   "report so we can deal with it by reading not refusing."
3. **Reports carry the text**, not merely the label name, so that a
   reader knows what to do with the finding.
4. **Four odd labels get fixed in the source rather than aliased in the
   parser** -- two `# NOTE:` and two `# HELIOCENTRIC:` become `# Note:`.
   Rationale: an alias map grows forever and leaves the silent-drop path
   exactly as silent.

Two standing project conventions also bound the answer.

**The tool carries; the reader judges.** The builder transports material
to a human or model reader because citation comparison is a language
judgment rather than a numerical one. The builder must not interpret
prose, score it, or decide what a note means.

**The visibility convention.** A failure that prints where the responder
reads it gets an ANNOTATION. A failure that appears nowhere gets a
REFUSAL. Visibility decides, not severity.

---

## 4. What we want from you

**Please answer Part A before reading Part B.** Part B contains the
implementing model's own recommendation. Reading it first will anchor
you, and an anchored second leg is worth very little to this project.
Write Part A, then scroll on.

### PART A -- your own structure, derived independently

Given sections 1 through 3, and the attached measurement:

**A1.** How should the leg vocabulary be structured so that "withheld on
purpose" and "nobody has classified this" are distinguishable? Propose
the shape you would build. Name the states and say what each one does to
a line.

**A2.** The measurement shows one dropped line that is different in kind
from the others. Find it and say what you think it implies. (It is in
Part 3 of the attached file. Form your own view of why it matters before
you read ours.)

**A3.** Adding `Note` to the recognised set has a consequence the
attached file measures. Predict it before you look, then check yourself
against Part 2 of the file. Say whether you predicted it, including if
you did not. What does that consequence tell you about the design of the
continuation-marker rule?

**A4.** Is there a structurally different framing of this whole problem
that sections 1 to 3 have not considered? We are asking because the
implementing model and the project have been inside this design for a
day and may be solving the problem as posed rather than the problem as
it is.

### PART B -- critique of our proposal

Only after Part A is written.

The implementing model recommended this six-part structure:

1. `CONTEXT_LEGS` gains `Note`. Travels with the row.
2. `RECORD_LEGS` becomes a NAMED set -- `Cross-checked`, `Removed`,
   `Corrected`, `Resolved` -- withheld by name rather than by falling
   through an unmatched branch.
3. Anything in neither set is reported into the worksheet with its text.
   Does not refuse, does not vanish.
4. The four odd labels are fixed in the source.
5. Ten continuation lines get `# Note+:` markers -- a mechanical
   consequence of item 1, without which the builder refuses to write.
6. One `# Note:` on a constant called `moon_hill_sphere_info` moves
   under `# Resolved:`, because it states what previous review legs
   concluded.

**Item 6 is known to be defective and we are telling you so.** After
recommending it, the implementing model read the code and found that
`# Resolved:` carries a strict grammar -- `Resolved: <worksheet> <key>
-- <what changed> (L-nnn)` -- validated by a linkage checker. A
free-form status note placed there fails validation. So the proposal
moves a line into a slot it does not fit.

That failure suggests the three-state model may be incomplete. The line
in question must not travel, and it is free-form prose, and RECORD is
the only non-travelling state available but demands a strict grammar.
There may need to be a fourth state: withheld, free-form, no grammar.
Or the taxonomy may be wrong in a way we have not seen.

**B1.** Where does your Part A structure differ from the six items, and
which difference matters most?

**B2.** Is a fourth state the right answer to the item 6 problem, or is
that a symptom of a worse structural error?

**B3.** Item 3 ships unclassified free-form text to outside reviewers
automatically. Does that create a contamination path we have not named?
The moon line is one instance we found by reading. Is there a
STRUCTURAL reason to expect others, and if so what stops them?

**B4.** Item 2 names the record legs in the request builder. A separate
tool already walks the raw file text independently to find `Resolved`
legs. Naming the same set in two places is a pattern this project has
been burned by before -- two code paths knowing the same fact, one of
them updated. Is that a real risk here, and what is the right single
home for that knowledge?

**B5.** What would make this design fail six months from now, in a way
that would not announce itself?

---

## 5. How to answer

Please use these headings, in this order: **Part A** (A1-A4), **Part B**
(B1-B5), **CHALLENGE** (only if you are disputing something from section
3), **WHAT I COULD NOT JUDGE** (anything this prompt did not give you
enough to assess -- this section is expected to be non-empty and an
empty one will be read as a failure to look).

Two things this project asks of every review:

**Do not agree in order to be agreeable.** A review that endorses the
proposal adds nothing that the proposal did not already contain. If you
think it is broadly right, say what is right in one paragraph and spend
the rest on where it is thin.

**Say when you are inferring.** If you are reasoning from a convention
you have seen in other codebases rather than from what this prompt
states, mark it. We would rather have a flagged guess than a confident
one.

Length: as long as it needs to be. Structure matters more than volume.

---

*Prepared August 19, 2026 with Anthropic's Claude Opus 5. Built on
`97c520177b18d69e6b5d3943557fdea47f56e8bf`.*
