# L-214 -- reconciling the two Mode 7 review legs

**Built on `97c520177b18d69e6b5d3943557fdea47f56e8bf` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Legs: Claude Fable 5 (`REVIEW_RETURN_L214_FABLE_20260819.md`) and GPT
(`Mode_7_Review___L-214...md`). Both reviewed the same two documents.
Both read in full from disk.

---

## 1. Where the two legs agree, and both disagree with the proposal

**The root cause is one layer below where the proposal was working.**
The leg regex is BUILT FROM the policy sets, so "not in our vocabulary"
and "does not exist" are the same condition. Both legs say: detect any
`# Label:` line generically FIRST, then classify it. GPT: treat the
comments as a small typed document format -- detect, classify, validate
continuation, apply transport policy, apply grammar. Fable reaches the
same place by asking how many OUTPUTS the builder has rather than which
set each label belongs to.

The invariant both propose, in GPT's words: every syntactically labelled
line attached to a claim must finish the builder in ONE NAMED
DISPOSITION. There is no fifth disposition called "fell through the
regex."

This subsumes proposal item 2. Naming `RECORD_LEGS` is right but
insufficient -- it fixes one hole while leaving the mechanism that made
the hole.

**Unclassified text must not travel to the outside reviewer.** Both legs
dispute this, and both frame it as disputing the IMPLEMENTATION's reading
of Tony's ruling rather than the ruling. Both read "report so we can deal
with it by reading" as locating the reader on the PROJECT side.

Fable's asymmetry argument: withhold-by-default fails visibly and
recoverably -- a responder lacks context, the report says exactly what
was missed, the next dispatch carries it once a human classifies it.
Ship-by-default fails invisibly and unrecoverably -- a contaminated leg
does not error, it CONVERGES, and convergence is this system's success
signal.

GPT's version: the builder still does not interpret the prose; it simply
declines to infer that "unknown" means "safe context."

**One home for the vocabulary.** Both legs, unprompted beyond B4, say the
verdicted label, the context set, the record set, and every regex derived
from them belong in one module that the request builder, the
Resolved-walking tool, and the linkage checker all import. Fable adds the
sharp version: the hazard is not naming the set twice in prose, it is
COMPILING it twice from two literals. If the walking tool carries its own
pattern today, item 2's implementation IS that tool's migration -- 
otherwise item 2 recreates the disease it treats.

**Item 6 is wrong and both say why.** The moon line is a record wearing a
context label. Forcing it under `Resolved` is structurally wrong because
`Resolved` has a strict linkage grammar and the moon line is prose.

---

## 2. Where the two legs differ

**Fourth state, or a second axis?**

Fable: add a fourth state -- withheld, free-form, no grammar. Candidate
names `# History:` or `# Held:`.

GPT: do NOT add a fourth state; that preserves the conceptual mistake.
RECORD is a TRANSPORT role and can carry more than one GRAMMAR.
`Resolved` is RECORD + strict linkage grammar; a new `# Review-note:` is
RECORD + free-form. If another structured record form appears later you
add a label, not a state.

**These are the same structure under two names.** Fable's own A4 states
the two-by-two explicitly -- travels-or-withheld crossed with
validated-or-free -- and calls the empty cell a fourth state. GPT names
the axes and refuses to call the cell a state. GPT's framing scales
better and is the one recommended here; Fable's naming candidates remain
useful.

---

## 3. What the legs found that the proposal had wrong, factually

**Item 5 undercounts. Verified.** Fable's B1 point 4: after item 4
relabels the odd spellings to `# Note:`, THEIR continuation lines join
the unmarked set too. Re-run with the project's own tooling:

| | unmarked lines | sites | builder |
|---|---|---|---|
| today | 0 | 0 | writes |
| item 1 only | 10 | 6 | refuses |
| item 1 + item 4 | **12** | **8** | refuses |

The two additional lines are the continuation under
`PARKER_CLOSEST_RADII` and the one under `venus_atmosphere_info`. Fable
said "at least twelve, not ten." Confirmed exactly.

Fable's reading of what that means: a migration whose own manifest
undercounts its own steps is evidence the six items were derived
separately rather than integrated as one change. That is correct.

**The six items need an ORDER constraint, not just a list.** Fable's B1
point 3: as sequenced, items 1 and 5 are landable while item 6 is
known-defective. In that window the moon note carries valid `Note+:`
markers and travels cleanly on the next moon-row dispatch. The ratchet
protects only until the marker sweep completes; after that nothing
refuses. Constraint: the moon line leaves `Note` before or in the same
transaction as the marker sweep.

---

## 4. Two process findings, both Fable's, both outside the design

**This leg was partially contaminated and disclosed it.** Fable ran
INSIDE the Paloma's Orrery project, so it carried resident memory of the
protocol and the general state of the provenance work. It did not carry
the L-214 design conversation. It is not the fresh-chat-outside-any-
project leg the dispatch rule prescribes.

**The Part A / Part B ordering is a check that cannot fail.** Fable's
disclosure: the prompt arrived as one document in one context, so there
is no way to write Part A without Part B already read, and NOTHING IN ANY
ANSWER DISTINGUISHES A REVIEWER WHO COMPLIED FROM ONE WHO COULD NOT.

The corroboration is in the other leg. GPT's A3 opens "my prediction
before consulting the measured result is..." and then states the measured
result to the digit. That is the tell, and it is not GPT's fault -- the
instruction asked for something the format made impossible.

Fable's remedy: if the split matters, it needs two physical dispatches --
Part A sent alone, answer collected, then Part B sent.

This is a defect in the dispatch design, authored in this session, and it
is an instance of the protocol's own CRITICAL gate.

---

## 5. Open items neither leg could judge

- Which document "worksheet" denotes in the ruling -- the outbound
  request or the return. Fable's most consequential critique pivots on
  it. This is the question now in front of Tony.
- Whether the reconciliation queue or ledger already carries "second leg
  owed" for the moon row. If it does, the moon comment is a redundant
  mirror to delete rather than prose to rehome. Fable: the first occupant
  of a new state should be prose that has no other home.
- The 22 unreached `# Cross-checked:` lines. Fable: "It reads like a
  finding living in a footnote; it deserves its own handle and a look."
- Whether `Cross-checked`, `Removed` and `Corrected` have grammars, which
  decides whether the registry associates validators with all four record
  labels or only `Resolved`.
