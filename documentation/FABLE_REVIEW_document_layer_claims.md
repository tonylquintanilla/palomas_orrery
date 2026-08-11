# Review Request: Document-Layer Claim Audit

**Built on `df7ca50f1730a40717c9f0fc22138465a5c4cef1`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery repo pinned separately at `d5437f08f94feccd70b697729b52cdc44df8b51d`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs verified live at the time of writing.**

**Prepared:** August 11, 2026, by Claude Opus 5, for Tony Quintanilla,
integrator. This is a review request, not a build. It asks for findings,
not patches.

---

## Who you are writing for

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist, and an anthropologist. He is not a professional software developer
and not a formally trained astronomer. He builds Paloma's Orrery through
conversation with AI partners rather than by writing code unassisted, and
he holds sole commit authority and final judgment.

The codebase you will be reading is disciplined, documented, and
structured. Do not read that as evidence of his personal programming
fluency -- it is the product of two years of iterative collaboration. What
Tony owns and drives personally is the workflow: the protocol, the master
plan, the ledger, the design decisions, and the judgment calls that resolve
conflicts between models. He is the integrator, not a passenger.

He runs Python by opening a file in VS Code and clicking Run. He works
through GitHub Desktop, not the git command line. If a finding implies an
operation outside that set, explain plainly what it does and what could go
wrong rather than assuming command-line fluency.

**Write your output for him to read directly.** Lead each finding with the
verdict in one plain sentence. One idea per sentence. Gloss any technical
term on first use. No aphorisms -- say what you found, not the shorthand
for it.

---

## What the project is, in two paragraphs

Paloma's Orrery is an interactive solar system visualization suite in
Python (Plotly, Tkinter) -- roughly 121 modules and 92,000 lines -- plus a
web gallery front end in a second repository. The orrery queries JPL
Horizons live for ephemerides; the gallery caches a recipe and
reconstructs scenes client-side without a live connection.

Underneath the code is a **record layer**: a resident protocol document
(`PROJECT_INSTRUCTIONS.md`, currently v3.37, 849 lines), a consolidated
ledger (`LEDGER_CONSOLIDATED.md`), a master plan, and ten versioned skill
files. These documents are not commentary. They are the mechanism by
which a multi-session, multi-model project stays consistent with itself,
because every session starts cold and no model remembers the last one.
That is what makes their accuracy load-bearing, and it is what this audit
is about.

---

## The failure class you are being asked to audit

Documents in the record layer make **claims about the project** -- counts,
locations, and statuses. Some of those claims were true when written and
drifted. Some were never true. Nothing in the toolchain checks any of
them. Every instance found so far was caught by a person happening to
look at the right file.

Nine instances are on record across recent session handoffs:

1. A stated line count of 772 that did not match the file.
2. A stated 37 entries that did not match.
3. A stated 126 tooltip definitions where the real figure is 124 -- and
   one of the two places recording 126 contradicts its own "83 + 41"
   breakdown in the same bullet.
4. A stated 45 assignments that did not match.
5. A 3-versus-8 annotation discrepancy.
6. A "248 sites" figure that turned out to be an artifact of how a search
   was run rather than a real count.
7. An "unresolved oddity" carried forward in planning documents that had
   in fact been answered three weeks earlier in
   `documentation/M2_TESTING_PROTOCOL_ADDENDUM.md`, line 749.
8. The protocol's own claim that a lessons archive was preserved verbatim
   in the ledger's version-history appendix. It never had been. That claim
   stood unchallenged from July 1 to August 11.
9. Found August 11, still live at the anchor SHA above: the protocol's
   Version History section states that the full history, v1.0 through
   current, lives in the ledger's Protocol Version History appendix. That
   appendix stops at v3.34. Versions v3.35, v3.36, and v3.37 are not in
   it.

Note the shape of numbers 8 and 9. They are not miscounts. They are
documented backups that do not exist. That is the more dangerous subtype,
because a wrong count is embarrassing while a phantom backup is a plan
built on something that is not there.

None of the nine changed a rendered output. All nine were caught by eye.

---

## The job

**Check the record layer's factual claims against the artifacts they
describe, and report which ones are false.**

That is the entire job. You are not asked to fix anything, propose
architecture, or evaluate the code's quality.

### What counts as a claim in scope

- **Countable.** "There are N of X." Line counts, file counts, entry
  counts, occurrence counts, item counts.
- **Locational or existential.** "X lives in Y." "X is documented in Z."
  "The archive is preserved in the appendix." "This is recorded as
  L-nnn."
- **Status.** "This is done." "This is retired." "Skill X is at version
  N." "This decision is ratified." "Tier-1 findings are at zero."
- **Cross-reference.** A pointer to a file, section, line, ledger handle,
  or skill that must actually resolve to the thing named.

### What is NOT in scope

Judgments, design rationale, philosophy, quotations, aspirational
statements, and anything whose truth is a matter of opinion rather than
measurement. If checking a sentence would require deciding whether Tony's
reasoning was correct, it is out of scope.

---

## Scope: which documents

The bounding rule here is one of Tony's own, and it matters more than the
file list: **the artifact bounds the audit.** The audit covers claims that
live documents make about the current state of the project. It does not
cover everything that could be said about the project. An audit whose
denominator grows whenever someone thinks of something can never close,
and an audit that can never close stops being read.

**In scope -- live documents describing current state:**

- `PROJECT_INSTRUCTIONS.md` (the protocol, v3.37)
- `LEDGER_CONSOLIDATED.md`
- `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- `documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md`
- All ten `skills/*/SKILL.md` files
- `MODULE_ATLAS.md`, `MODULE_INDEX.md`, `DATA_INVENTORY.md`,
  `PROVENANCE_AUDIT.md`, `README.md`

**Out of scope:**

- **Session handoffs** (`documentation/HANDOFF_*.md`). A handoff's claims
  are historical -- they describe the state a past session was built on,
  and correcting them would make the document assert something untrue
  about when it was written. This is a standing ruling. The exception:
  if a handoff claim was carried forward into a live document above, the
  copy in the live document is in scope.
- **Superseded and versioned copies** in `documentation/`
  (`project_instructions_v3_*.md`, `*_old.md`, prior master plan
  updates). These are archived states, not current claims.
- **Code comments and docstrings.** A separate audit tool
  (`provenance_scanner.py`) already covers data provenance in code.
- **Whether the code is correct.** Not this job.

The `documentation/` directory holds roughly 700 files. Only the four
named above are in scope. If you find yourself reading a fifth, check it
against the bounding rule first.

---

## How to check

The repository is public. Fetch files at the pinned SHA so there is no
ambiguity about which state you reviewed:

```
https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/df7ca50f1730a40717c9f0fc22138465a5c4cef1/PROJECT_INSTRUCTIONS.md
```

Substitute the path for other files. The SHA in that URL pins the exact
bytes; a URL with `main` instead would drift.

**If you cannot fetch, say so and ask Tony to paste the files.** Do not
audit from recollection of what these documents usually say. The failure
class you are auditing is precisely the one that recalled specifics
produce.

---

## Deliverable

A findings list. One row per claim checked and found wrong. For each:

| Field | Content |
|---|---|
| Verdict | FALSE / STALE / UNVERIFIABLE |
| Location | File and line number |
| The claim | Quoted, short |
| The check | What you did to test it |
| The reality | What you measured instead |
| Weight | Does this change what Tony does, or is it a correction? |

Verdict meanings:
- **FALSE** -- the claim is not true and appears never to have been.
- **STALE** -- true when written, no longer true.
- **UNVERIFIABLE** -- you could not check it with what you have. Say what
  would settle it. Do not guess. In this project, a flagged gap is
  honest and a plausible-but-unchecked answer is not.

**Report only failures and unverifiables.** A list of everything that
checked out is not useful to him and buries the part that is.

**Do not produce patches.** Tony decides what changes and in what order,
and several of these will turn out to be decisions rather than
corrections. A patch presented alongside a finding pressures the finding
into looking settled.

---

## Second output, briefly

After the findings, answer one question in a short paragraph:

**Which of these claim types could a tool check automatically, and which
genuinely require a person?**

Context for why this is being asked: Tony is about to open a ledger item
for this whole failure class, and the natural next question is whether it
becomes a checker or stays a discipline. A line count is trivially
checkable. "This decision was ratified" may not be. Your read on where
that boundary falls is the useful part, not a specification.

---

## Three constraints on your own output

1. **Your counts are claims too.** If you report "the appendix stops at
   v3.34," state how you determined it. This audit is recursive by
   nature and the discipline applies to the auditor.

2. **Do not expand the scope.** If you notice something outside the file
   list that seems important, note it in one line at the end under
   "outside scope, noticed anyway." Do not pursue it. Scope creep in an
   audit report is how the report stops being finishable.

3. **Distinguish "I found this" from "this should change what Tony does
   next."** Most findings are the first kind. Presenting both in the same
   register makes him do the sorting, and sorting is the expensive part.

---

## What this review is not for

Do not review or comment on: the design of L-189 (a scanner run-history
feature currently being built), the six open `duplicate_identity`
provenance sites, the orrery's rendering code, or the master plan's
technical decisions on their merits. Those are either in active work or
require judgment against sources that you do not have.

---

*Review request prepared August 11, 2026 with Anthropic's Claude Opus 5,
built on `df7ca50f1730a40717c9f0fc22138465a5c4cef1` at
https://github.com/tonylquintanilla/palomas_orrery and
`d5437f08f94feccd70b697729b52cdc44df8b51d` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
