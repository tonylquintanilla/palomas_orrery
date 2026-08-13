"""Patch: master plan v17 -> v18 and summary current through Aug 13.

Run command:

    python patch_masterplan_v18.py

Save this file into the REPO ROOT (the folder holding
LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run. It edits
two files in documentation/ and writes nothing unless every anchor in
both is found.

No generator to run afterwards -- neither file is generated. Commit
and push.

RUN THIS AFTER patch_capture_L192_review.py, not before. Both are
anchored independently so the order does not actually matter, but the
summary's text refers to the ledger capture as done.

Success prints one `ok` line per edit, then a `patch applied` line per
file. Failure prints a single ERROR or ANCHOR FAIL line and writes
nothing.
"""

import hashlib
import os
import sys


PLAN = os.path.join('documentation', 'MASTER_PLAN_INTERACTIVE_GALLERY.md')
SUMMARY = os.path.join('documentation',
                       'MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md')


PLAN_EDITS = [
    (b"""**Status:** v17 -- Phase 2 (solar system assembler) BUILD UNDERWAY. Design""",
     b"""**Status:** v18 -- Phase 2 (solar system assembler) BUILD UNDERWAY. Design"""),

    (b"""---

## Section 11 -- Protocol & Skills Review (from Phase 0)""",
     b"""*New in v18 (August 13, 2026):*
- **Track 1 tooling advanced on three fronts; no rendering code touched
  and no Track 0 or Track 2 work moved.** L-186 closed, L-188 closed,
  L-189 closed, L-192's scanner half built. The plan's phase structure
  is unchanged; this entry records what the provenance layer now does
  that it did not do on August 7.
- **L-186 closed, and it was never a data question.** The six
  `duplicate_identity` findings carried through three handoffs as
  "each needs a look at the source" were all the parser misreading
  correct annotations. The retired annotation grammar put a free-text
  source before the check date, so a source carrying its own
  publication year ate the date and the model name landed outside the
  checker identity -- two annotations by two DIFFERENT models read as
  one checker written twice. Measured: 54 of 134 annotation lines
  codebase-wide were affected. The fix was the grammar, not the six
  sites: checker first, optional source clause, retired order REFUSED
  rather than reconstructed. All 134 lines migrated.
- **L-188 closed. `maintenance_run.py` runs four generators and eight
  checkers in about 40 seconds.** Its first pass confirmed its own
  premise by finding two red test files nobody had executed -- one
  asserting an unannotated corpus since roughly August 3, the other
  failing 6 of 73 against values deliberately corrected on August 2.
  Neither was detectable before, because neither file was in any
  routine.
- **55 pinned constant literals retired; `constants_change_report.py`
  replaces them and stores no numbers.** It asks git what changed in
  `constants_new.py` since the last commit and reads both values out of
  the diff -- so it covers constants that do not exist yet. 18
  structural tests kept (derivations, orderings, cross-consistency,
  completeness); none holds a copy of a measured value.
- **Protocol v3.39: "A Check That Cannot Fail Is Not Passing"
  [CRITICAL].** Companion to Verify Execution, Not Appearance, one
  layer out: that gate asks whether the code you edited is the code
  that runs; this one asks whether the CHECK you are trusting can
  produce a failure at all. Three instances in one session, each in a
  different layer and each indistinguishable from a pass. The three
  moves: make success carry evidence, make the blind spot announce, put
  the check where it runs.
- **L-192's scanner half built (August 12-13): cross-check credit now
  requires ATTACHMENT.** The scanner counted any annotation inside a
  30-line window. That window is correct for a citation -- a section
  header naming IAU Resolution B3 legitimately covers the constants
  beneath it -- and wrong for an annotation, which names one checker
  who verified one value on one date. The deciding case:
  `INNER_LIMIT_OORT_CLOUD_AU` wore the cross-checked rung on
  annotations belonging to the heliopause constant three lines above,
  while the worksheets those annotations name read UNVERIFIED and
  PARTIAL for the Oort value. The window was converting a recorded
  non-verification into a top rung.
- **Audit movement: the cross-checked rung fell from 77 to 50.**
  Nothing got worse; 50 was always the true number. Four orphan
  annotations are reported -- two section headers in `constants_new.py`
  written to cover a group, which the codebase has no grammar to
  express.
- **Ruled: per-value annotations, not block-scope grammar.** A parser
  cannot distinguish group intent from proximity, because in bytes they
  are identical. The reason to prefer per-value is the Oort case: a
  block annotation reading "everything below checked" would have
  papered over two UNVERIFIED worksheet rows inside its own scope.
- **A number was wrong twice before it was caught, and the method note
  matters more than the number.** Fable's written attachment rule and
  its own measurement script disagreed; the independent verification
  leg reproduced the error, because it implemented the same prose and
  read it the same wrong way, and the agreement was reported as
  confirmation. Cross-AI independence protects against a shared model,
  not a shared specification. Correct split: 50 keep, 27 drop.
- **L-192's checker itself is designed and reviewed, not built.**
  Pre-design and Fable's review both anchored `00219d9`; verdict sound
  with changes. Four layers, each with a named failure: worksheet
  exists, row located, value agrees, verdict read. Three additions
  accepted -- an identity-consistency check (the worksheet filename
  must carry the checker token; 134 of 134 pass today), a
  drift-since-check against the tier2 schema's `Code value` column
  (reaches 72 of 134), and DERIVED split out of QUALIFIED. Fable
  proposed treating DERIVED as closed-by-derivation, citing L-158;
  L-158 rules the opposite and the convention wins.
- **Ruling changed: the checker joins `maintenance_run.py`.** The
  earlier ruling kept it out on cost grounds. The cost was never the 34
  markdown files -- it was one more block of output to read before
  every push. One line carrying a denominator answers that, findings to
  the audit, report-only. It does not gate pushes.
- **A standing move, new: reopen the session that produced the
  evidence.** Tony's ruling -- we do not have to accept and interpret
  incomplete or malformed answers. Two cited worksheets were unusable,
  one prose a tool cannot read and one carrying seventeen unresolved
  rows, and the design was drifting toward a parser clever enough to
  cope. Going back to the originating conversation closed nine of
  seventeen rows, settled the Mercury radius that had been open eleven
  days, and surfaced two annotations crediting a worksheet for checks
  it explicitly did not perform. Now carried in
  provenance-discipline v2.1.

---

## Section 11 -- Protocol & Skills Review (from Phase 0)"""),
]


SUMMARY_EDITS = [
    (b"""Where we are 8/11/2026

Updated 2026-08-11 after the August 8-10 session. Built on
4509c08 at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at 02d71637e100c4faf6ddaa23cdbc9b6f4a88ddc0 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Companion to MASTER_PLAN_INTERACTIVE_GALLERY.md v17. The plan is the
reference document; this is the readable snapshot.""",
     b"""Where we are 8/13/2026

Updated 2026-08-13 after the August 12-13 sessions. Built on
00219d9 at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at cd4874467254c89e88dc2a8fa0645e99bf5c986e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Companion to MASTER_PLAN_INTERACTIVE_GALLERY.md v18. The plan is the
reference document; this is the readable snapshot."""),

    # L-188 is closed, so this decision is settled by default.
    (b"""  (decide) Where the L-188 run-all push-gate binding lands -- L-188 or
           L-184.

""",
     b""""""),

    (b"""  Track 1     L-186  Cross-check annotation issues -- mechanical half
                     done, six duplicate_identity sites remain
              L-177  Mercury Hill sphere convention
              L-184  Interactive build-path push gate""",
     b"""  Track 1     L-186  Cross-check annotation issues  DONE
              L-192  Worksheet checker -- scanner half built,
                     checker designed and reviewed, NOT built
              L-177  Mercury Hill sphere convention
              L-184  Interactive build-path push gate"""),

    (b"""  Tooling     L-188  Maintenance runner -- one command, the whole suite
              L-189  Provenance scanner: run history and run-to-run
                     delta  -- NEXT SESSION'S BUILD""",
     b"""  Tooling     L-188  Maintenance runner -- one command, the whole
                     suite  DONE
              L-189  Provenance scanner: run history and run-to-run
                     delta  DONE"""),

    (b"""Protocol at v3.35. The v3.36 Register Rule amendment is drafted at
documentation/REGISTER_RULE_AMENDMENT_v3.36.md and NOT YET APPLIED. \"The
Artifact Bounds the Audit\" is ruled for Part 3 but has no drafted text
anywhere in the repo -- it needs writing, not applying.""",
     b"""Protocol at v3.39. The v3.36 Register Rule amendment is applied, and
so is \"The Artifact Bounds the Audit\" (v3.37). v3.38 records the two
limits on Stale Skill = Stop. v3.39 adds \"A Check That Cannot Fail Is
Not Passing\" as a CRITICAL gate. provenance-discipline is at v2.1."""),

    (b"""Entry written August 2026 with Anthropic's Claude Opus 5.""",
     b"""AUGUST 12-13: THE PROVENANCE LAYER GREW TEETH

Two sessions, no rendering code touched, and Track 0 did not move. What
changed is what the tooling can now catch.

L-186 closed, and it turned out not to be a data question at all. Six
findings had been carried through three handoffs as \"each needs a look
at the source.\" All six were the parser misreading correct
annotations, because the old annotation format let a source's own
publication year eat the check date. The fix was the format. All 134
annotations were migrated.

L-188 and L-189 closed. `maintenance_run.py` now runs four generators
and eight checkers in one command, about 40 seconds. Its very first
pass found two test files that had been red for days and that nobody
ran, which is the argument for the runner in one sentence.

Fifty-five pinned constant values were retired from the test suite.
They were pinning pre-correction numbers and nobody had updated them.
`constants_change_report.py` replaces them and stores no numbers at all
-- it asks git what moved and reads both values out of the diff, which
means it covers constants that do not exist yet.

L-192 is the one worth reading twice. The scanner had been granting
its top trust rung -- cross-checked -- to values on the strength of
annotations written for a DIFFERENT value a few lines away. The
deciding case was the inner Oort cloud limit, which wore the top badge
while the two worksheets it was credited with read UNVERIFIED and
PARTIAL for that exact number. A recorded non-verification was
rendering as a completed check.

Credit now requires the annotation to touch the value's own
declaration. The cross-checked count fell from 77 to 50. Nothing got
worse; 50 was always the real number.

Two things from those sessions are worth carrying beyond them.

The first is a correction. A measurement went to Tony wrong twice
before it was caught -- Fable's written rule and its own script
disagreed, and the independent check reproduced the error because it
read the same prose the same wrong way. Two implementations agreeing
is only as good as the specification they share. The right split is 50
and 27.

The second is a move that is now standing procedure: reopen the
session that produced the evidence. Two cited worksheets were
unusable, and the design was drifting toward building a parser clever
enough to interpret them. Tony's ruling was that we do not have to
accept and interpret incomplete or malformed answers. Going back to
the August 2-4 conversation and asking it to finish closed nine of
seventeen open rows, settled Mercury's radius after eleven days, and
turned up two annotations crediting a worksheet for checks it had
explicitly declined to make. Old sessions persist, they hold the
research context, and asking them to finish costs a fraction of
starting over.

The worksheet checker itself is designed and reviewed and NOT built.
That is the next build, and one question goes first: whether a
half-confirmed verdict can count as a completed check.


Entry written August 2026 with Anthropic's Claude Opus 5."""),
]


FILES = [(PLAN, PLAN_EDITS), (SUMMARY, SUMMARY_EDITS)]


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
    print("No generator to run. Commit and push.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
