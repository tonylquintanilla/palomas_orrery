"""Patch: capture the L-192 pre-design review in the ledger and handoff.

Run command:

    python patch_capture_L192_review.py

Save this file into the REPO ROOT (the folder holding
LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run. It edits
two files and writes nothing unless every anchor in both is found.

Afterwards run ledger_index.py. L-192 stays OPEN; its date moves to
2026-08-13, so the index row WILL change. That is expected.

Four documents should also be saved by hand before the commit -- the
patch cannot create them because they were produced in other sessions:

  documentation/PREDESIGN_L192_worksheet_checker.md
  documentation/FABLE_REVIEW_L192_worksheet_checker.md
  documentation/ADDENDUM_REQUESTS_worksheet_readability.md
  documentation/worksheets/worksheet_claude_constants_new_addendum.md

Success prints one `ok` line per edit, then a `patch applied` line per
file. Failure prints a single ERROR or ANCHOR FAIL line and writes
nothing.
"""

import hashlib
import os
import sys


LEDGER_EDITS = [
    (b"""<!-- L:192 status:OPEN upd:2026-08-12 section:A flag: rice:3/3/70/3 -->""",
     b"""<!-- L:192 status:OPEN upd:2026-08-13 section:A flag: rice:3/3/70/3 -->"""),

    (b"""- **Method note worth keeping.** Fable's written rule and its own
  measurement script disagreed -- the prose said the entry line, the
  script used the literal's line -- and the independent verification
  leg reproduced the error, because it implemented the same prose and
  read it the same wrong way. The agreement between two implementations
  was reported as confirmation and was not. Caught only by re-reading
  the written rule against the code being produced. Cross-AI
  independence protects against a shared model, not a shared spec.
""",
     b"""- **Method note worth keeping.** Fable's written rule and its own
  measurement script disagreed -- the prose said the entry line, the
  script used the literal's line -- and the independent verification
  leg reproduced the error, because it implemented the same prose and
  read it the same wrong way. The agreement between two implementations
  was reported as confirmation and was not. Caught only by re-reading
  the written rule against the code being produced. Cross-AI
  independence protects against a shared model, not a shared spec.

##### Pre-design reviewed, 2026-08-13: the checker itself

Documents: `documentation/PREDESIGN_L192_worksheet_checker.md` and
`documentation/FABLE_REVIEW_L192_worksheet_checker.md`, both anchored
`00219d9`. Fable's verdict: **sound, with changes.** Not built.

**Purpose, restated.** The checker confirms that an annotation's claim
of evidence is TRUE. It is the only planned check reaching committed
history: `constants_change_report.py` is a pre-commit diff reader by
construction, so a value corrupted and committed three weeks ago has
nothing in the diff to notice. The worksheet is a fixed record and says
what it said.

**Four layers, each with a named failure.** L0 worksheet exists
(currently zero failures across 134 annotations -- passes today, can
still fail on a rename or a migration-mangled filename). L1 the row is
located (failure: UNMATCHED). L2 the value agrees (failure: MISMATCH --
the loudest finding available, because the code and its own evidence
disagree about a number). L3 the verdict is read (failure: an
annotation asserting a completed check over a row recording an
incomplete one -- the Oort case).

**Fable's three additions, all accepted:**

- **Identity consistency.** Nothing checked that the named worksheet
  belongs to the named checker, so two annotations naming different
  models over one model's evidence would pass all four layers and fake
  the rung. Rule: the worksheet filename must contain the checker
  token, case-folded. Verified independently: 134 of 134 pass today,
  and an injected Gemini-over-Claude-worksheet violation is caught.
- **Drift-since-check (L2b).** The tier2 schema records `Code value` --
  what the checker read at the prompt's SHA. Comparing it to the code
  NOW detects a value edited after its check. Verified coverage: the
  column reaches **72 of 134** annotations, not the whole corpus.
- **DERIVED split out of QUALIFIED.** ACCEPTED AS A SPLIT, REJECTED AS
  A DISPOSITION. Fable proposed "closed by derivation, do not queue,"
  citing L-158. **L-158 rules the opposite**: it explicitly retired the
  derived-rung framing, and holds that a runtime-derived value inherits
  its weakest input's rung only once the derivation logic -- formula,
  units, parent reference -- has cleared one independent cross-check,
  and is unverified until then. Fable and GPT both rejected the
  immune-by-derivation premise in July, citing Mars Climate Orbiter.
  The convention wins; a DERIVED row is PENDING, not closed.

**Comparison rule (Fable, accepted).** Exact-or-rounded, never "within
tolerance." A significant-figures tolerance would call Mercury's 2439.7
and JPL's 2439.4 +/- 0.1 a match at three figures and the finding would
vanish. A range cell is never MATCH; it is RANGE, its own class. A
comparison needing a unit conversion is MATCHED-VIA-CONVERSION, its own
class, because the conversion imports the project's own constants into
the comparator.

**Row matching (fork 1, Fable: (a) plus (c)).** Header-role mapping is
the primary matcher; an unrecognised header set makes the whole
worksheet WORKSHEET_UNREADABLE, announced every run. Value-based search
is permitted only against the CODE-VALUE column, never the evidence
column. Future worksheet prompts emit one schema with a key column --
now carried in provenance-discipline v2.1.

**Where it runs (fork 4). RULING CHANGED, 2026-08-13.** The earlier
ruling kept the checker out of `maintenance_run.py` on cost grounds.
Tony's reason was never file size: it was one more block of output to
read on every push. Ruling: **the checker joins the runner**, printing
ONE line on a clean run with its denominator ("134 annotations, N
verified, M unmatched"), findings to the audit. Report-only -- it does
NOT gate pushes; expanding the Tier-1 gate stays a separate decision.
A line carrying a denominator moves when something moves; a line that
always reads the same is wallpaper, and wallpaper is a check that
cannot fail.

**Uncited worksheets (fork 5, accepted).** One line steady-state with
the date the set last changed; the full list prints only when the set
differs from the recorded state.

**Writing (fork 3, Fable recommends, Tony has not ruled).** A
`--propose` mode emitting a patch script, never editing in place, with
each worksheet row quoted verbatim beside each proposed annotation --
so review runs against the evidence rather than the tool's claim about
it. The risk is not forgery; it is a matcher bug writing annotations
against wrong rows and the same matcher later confirming them.

**Still open for Tony (decide):**
1. Does a QUALIFIED verdict (PARTIAL, APPROX) earn a leg? Fable's
   middle: never by token class, only by explicit per-row ruling
   recorded in `provenance_exceptions.json` and visible in the audit.
   Deliberately deferred to a fresh session -- a day spent inside the
   Oort case biases this toward the strict answer.
2. Fork 3, the propose mode.
3. `BENNU_RADIUS_KM` and `ARROKOTH_RADIUS_KM` -- see below.

**Two false attributions, found 2026-08-13 and NOT yet fixed.** Both
annotations credit `worksheet_claude_constants_new.md` for checks it
explicitly did not perform. Row G10 reads UNVERIFIED, "Not checked,"
while the Bennu annotation credits a cross-check against Nolan et al.
Row G14 said the OLD Arrokoth value was wrong; the value was then
corrected against Keane et al. 2022, which the worksheet never opened,
and the annotation rode along unchanged. Both replacement values are
arithmetically self-consistent with their stated inputs, so the numbers
look right and the PROVENANCE claim is what overstates. The checker
will surface both mechanically on its first run. Tony (decide): remove,
reattribute, or annotate. Rule added to provenance-discipline v2.1.
"""),
]


HANDOFF_EDITS = [
    (b"""---

*Handoff prepared August 2026 with Anthropic's Claude Opus 5, built on
`c5218f6202965bc051044e59988e1a040a234fc9` at""",
     b"""---

# PART 2 -- the pre-design, the review, and a rule

Everything above was written at `c5218f6`. The session continued.
Anchor for this part: `00219d9`, plus whatever SHA carries this
amendment.

## The checker was designed, reviewed, and not built

`documentation/PREDESIGN_L192_worksheet_checker.md` went to Fable 5;
`documentation/FABLE_REVIEW_L192_worksheet_checker.md` came back.
Verdict: sound, with changes. Full capture is in the L-192 ledger
block; the three things worth carrying in prose are below.

**Fable cited L-158 wrongly, and the ledger records the divergence.**
It proposed treating a DERIVED verdict as closed-by-derivation, citing
L-158 as having placed derived values on their own rung. L-158
explicitly RETIRED that framing in July: a runtime-derived value
inherits its weakest input's rung only after the derivation logic
itself has cleared one independent cross-check. A DERIVED row is
pending, not closed. The convention wins over external input, and this
is only catchable with both documents open -- a fresh session reads
"the L-158 ruling" and takes it as given.

**One ruling changed.** The checker now JOINS `maintenance_run.py`,
one line with a denominator on a clean run, findings to the audit,
report-only. Tony's original reason for keeping it out was never the
34 files; it was one more block of output to read before every push.
One line with a count answers that, and a count moves when something
moves.

**Two annotations are false and are not yet fixed.**
`BENNU_RADIUS_KM` and `ARROKOTH_RADIUS_KM` both credit
`worksheet_claude_constants_new.md` for checks it explicitly did not
perform. The values are fine; the provenance claim overstates. Tony
(decide) before the checker's first run, or it arrives as a failure.

## The move that changed the design: reopen the session

Tony's ruling, and it is the most reusable thing here: **we do not have
to accept and interpret incomplete or malformed answers.**

One cited worksheet was prose no tool can read; another carried six
PARTIAL and eleven UNVERIFIED rows. The design was drifting toward a
parser clever enough to cope. The better move was to go back to the
conversation that produced them -- "DONE: Phase 2 design and build
Piece 1", August 2-4 -- and ask it to finish the job in a readable
format.

**It works, and the numbers say so.** Of seventeen unresolved rows,
nine closed. Mercury closed because the session finally opened the NASA
fact sheet it had never opened: 2439.7 confirmed, oblateness 0.0009
confirmed, and the 0.3 km disagreement with JPL turns out to be a
separate determination rather than an error. The addendum also found
the two false attributions above, which nobody was looking for.

Old sessions persist and can be continued. They hold the research
context, so asking them to finish costs a fraction of starting over.
This is now a standing move, not a one-off. `documentation/
ADDENDUM_REQUESTS_worksheet_readability.md` holds both prompts as
worked examples.

## Skill: provenance-discipline 2.0 -> 2.1

Two clauses added to Worksheet First, Annotation Second: **the
worksheet has to say the thing** (existence is clause one, not the
whole rule -- a worksheet saying a value is WRONG is not a worksheet
saying the replacement is RIGHT), and **incomplete or malformed
evidence is sent back, not interpreted.** Plus the producer half: the
worksheet table schema and the verdict vocabulary are now stated in the
prompt, because eight layouts exist on disk and no prompt ever
specified one.

Also recorded: the v2.0 changelog entry, which was never written when
v2.0 landed.

**OBLIGATION FOR THE NEXT SESSION.** `provenance-discipline` went to
2.1 at this session's push. The session that bumped it loaded 2.0. A
mid-session reinstall cannot be verified from inside the session --
the loaded copy appears bound at conversation start. **Confirm your
loaded copy reads 2.1 before doing any provenance work.** Your load
performs the check; this note cannot.

## Next session

L-192's build, with fork 2 as the first question rather than the
fifth. Then the backfill of the 27, verdict-gated, starting with the
four orphans and the two false attributions.

The addendum also routed the remaining unresolved rows: D1, D3, D4 to
Gemini for book access; D2, D5, D6, G9, G10 to any journal-access
checker -- those five are the cheapest remaining wins and need no book.

---

*Handoff prepared August 2026 with Anthropic's Claude Opus 5, built on
`c5218f6202965bc051044e59988e1a040a234fc9` at"""),
]


FILES = [
    ('LEDGER_CONSOLIDATED.md', LEDGER_EDITS),
    (os.path.join('documentation',
                  'HANDOFF_20260812b_L192_attachment.md'), HANDOFF_EDITS),
]


def stage(path, edits, label):
    with open(path, 'rb') as f:
        data = f.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    print(f"{label}: fingerprint {fp}  ({len(data)} bytes)")

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print(f"{label}: file uses CRLF; anchors translated")

    staged = data
    for i, (old, new) in enumerate(edits, 1):
        o, n = old, new
        if is_crlf:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = staged.count(o)
        if count != 1:
            head = o.split(b'\n')[0][:70]
            print(f"ANCHOR FAIL {label} edit {i}: expected 1 match, "
                  f"got {count}: {head!r}")
            return None
        staged = staged.replace(o, n, 1)
        print(f"ok  {label} edit {i}")
    return staged


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    for fname, _e in FILES:
        if not os.path.exists(os.path.join(here, fname)):
            print(f"ERROR: {fname} not found under {here}")
            return 1

    staged = {}
    for fname, edits in FILES:
        result = stage(os.path.join(here, fname), edits, fname)
        if result is None:
            print("nothing written")
            return 1
        staged[fname] = result

    for fname, content in staged.items():
        with open(os.path.join(here, fname), 'wb') as f:
            f.write(content)
        print(f"patch applied to {fname} ({len(content)} bytes)")

    print("")
    print("Next: run ledger_index.py. L-192 stays OPEN and its date")
    print("moves to 2026-08-13, so the index row will change.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
