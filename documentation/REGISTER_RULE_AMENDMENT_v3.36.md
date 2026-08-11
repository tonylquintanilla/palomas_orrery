# Register Rule amendment -- protocol v3.36

Built on `0811ffcc1746d30971d731db7d1893176c2ae6a4` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Target file: `PROJECT_INSTRUCTIONS.md`, Register Rule section at line 193.
Version history entry appends after the v3.35 entry near line 835.

Drafted August 8, 2026 with Claude Opus 5. Not applied.

---

## Edit 1 -- replace the checks block

**Find** (Register Rule section, currently lines 205-215):

```
Two checks before sending, each with a yes-or-no answer:
1. Does this paragraph do one job?
2. Does any sentence point at a label instead of saying the thing?

The test is not "is this correct." It is "can Tony act on this without
a follow-up question."

Backstop: Tony says "opaque" at the point it fails. Claude rewrites that
passage. The miss gets captured as a field note so it accumulates rather
than repeating.
```

**Replace with:**

```
Three checks before sending, in this order:
0. Does this message ask Tony for ONE thing?
1. Does this paragraph do one job?
2. Does any sentence point at a label instead of saying the thing?

Check 0 is the outer scope and fails first. A finding, a recommendation,
an uncertainty, and a new question are four things. Send the one that is
due; the rest wait their turn or go in a file. A message can pass checks
1 and 2 paragraph by paragraph and still be unusable, because the load
is the COUNT of open items, not the density of any one of them.

The test is not "is this correct." It is "can Tony act on this without
a follow-up question."

Two supporting defaults:

ANSWER FIRST, EVIDENCE ON REQUEST. How a number was checked is Claude's
work, not Tony's. State the number and whether to trust it. Show the
method if asked.

CAPTURE GOES IN A FILE, NOT IN THE CONVERSATION. Ledger material,
finding lists, and session records are things Tony opens at his
computer. Putting them in the message makes him absorb what he only
needs to store.

Backstop, corrected: the prior wording relied on Tony saying "opaque"
at the point of failure. Tony has stated he cannot sustain that -- by
the time a message is dense enough to flag, reading it to the end is
already the cost. So the check runs on CLAUDE's side before sending,
and "opaque" is a repair, not the mechanism. Tony may also say "just
the decision," which strips everything except the ruling being asked
for.

(Origin, August 8, 2026: a full mobile session ran without the Register
Rule firing once. Its two checks were paragraph-level and the paragraphs
passed; the failure was four jobs per message. Tony diagnosed it --
"the level of detail and jargon is so dense that I only absorb the
general idea and sometimes not even that." He had already tried the
obvious workarounds: a second model as translator, which added a layer
and introduced errors, and asking for executive summaries, which helped
only partly. The rule's own backstop was the part that had failed.)
```

---

## Edit 2 -- append to Version History

**Insert after the v3.35 entry:**

```
v3.36 (August 8, 2026): Register Rule amended (Part 2). A message-level
check added ahead of the two paragraph-level checks -- does this message
ask Tony for one thing. The prior checks were paragraph-scoped and could
all pass while a message carried four separate jobs, which is the load
that actually fails. Two supporting defaults added: answer first with
evidence only on request, and capture goes in a file rather than in the
conversation. Backstop corrected -- "opaque" is a repair, not the
mechanism, because Tony has stated he cannot sustain flagging density in
real time; the check runs on Claude's side before sending. "Just the
decision" added as a second Tony-side lever. Origin: a full mobile
session in which the rule did not fire once.
```

---

## Notes for whoever applies this

- Section stays in Part 2. Not a skill: skills load per task, and this
  applies to every message in every session.
- Check numbering starts at 0 deliberately, so the existing checks 1 and
  2 keep their numbers and any external reference to them still resolves.
- No skill version bump and no `skills_index.py` run. This is protocol
  only, so the three-store synchronization does not apply.
- ASCII only throughout; no section-sign characters.
