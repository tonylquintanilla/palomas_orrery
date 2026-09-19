#!/usr/bin/env python3
"""
patch_L322_9_read_field_skill_214_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
PROJECT_INSTRUCTIONS.md), open it in VS Code and click Run.  Or:
python patch_L322_9_read_field_skill_214_20260919.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. Filed first and run second, it stops with one line,
writes nothing, and the push goes out without it. This script refuses to
run from documentation/.

Built on orrery dfa779bd9377065f2dc9511f2ef630499bedbb38
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 82e786f17634f108a2e0df2ae7c693e5fcf62a60
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

STAGE B of documentation/BUILD_MANIFEST_L322_earth_slice_20260919.md:
the skill learns the read line BEFORE the walk, because a convention
that is not in the skill does not travel. Tony approved the wording of
The Read Field on 2026-09-19, answering four questions about it, and
glossed "need" in the same message.

This is ONE skill bump under the four binding steps in
ledger-and-session-records: the version line, skills_index.py, a
protocol version-history entry, and all of it in ONE commit.

WHAT IT DOES (four files, 10 anchored edits):

  skills/provenance-discipline/SKILL.md
      version line 2.13 -> 2.14, cut from dfa779bd, with the v2.14
      paragraph; THE READ FIELD as a new section beside The Unit Field;
      The Unit Field pointed at constants_tokens.py and naming
      "# Read:" among the fields a slice visit writes; Rule 8's
      enumeration naming both routes to a derived row; the worksheet
      schema gaining the "Read by" column promised on 2026-09-11.

  PROJECT_INSTRUCTIONS.md
      header stamp and SHA anchor move to v3.63 / dfa779bd; the v3.63
      entry is added; v3.60 is REMOVED, because a fourth entry pushes
      the oldest down and an entry lives in exactly one place.

  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
      v3.60 lands at the end of PART 1 with its moved-down note.

  LEDGER_CONSOLIDATED.md
      a dated line on L-322 recording the bump, the approval, and the
      obligation the next session discharges.

TWO GENERATED ZONES ARE EXCLUDED FROM THE FINGERPRINTS: the skill
manifest in PROJECT_INSTRUCTIONS.md (skills_index.py) and the INDEX
zone in LEDGER_CONSOLIDATED.md (ledger_index.py). This patch's own
steps tell Tony to run both tools, so guarding those zones would refuse
for a reason that is not about content.

WHAT IS PERMANENT AND WHAT IS NOT. This script is disposable. The skill
section, the protocol entry and the ledger line are permanent. The
reinstall is Tony's and cannot be verified from inside this session.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written to ANY of the four files. Undo is Discard Changes in GitHub
Desktop.
"""

import hashlib
import os
import sys

SKILL = "skills/provenance-discipline/SKILL.md"
PROTOCOL = "PROJECT_INSTRUCTIONS.md"
HISTORY = "documentation/PROJECT_INSTRUCTIONS_HISTORY.md"
LEDGER = "LEDGER_CONSOLIDATED.md"

# Content fingerprints, CRLF normalized, generated zones excluded.
BASE = {
    SKILL:    "14f6e863f9261d4bb2642797024a7593",
    PROTOCOL: "7eb189235857e1da7b6a80c23d28a975",
    HISTORY:  "7e0d4b7c601c05a89404834b1307412b",
    LEDGER:   "a24ad391eb0474a734894d8c5f94466e",
}

# (file, start marker, end marker) for zones a generator rewrites.
ZONES = {
    PROTOCOL: (b"<!-- SKILL-MANIFEST:START", b"<!-- SKILL-MANIFEST:END -->"),
    LEDGER:   (b"<!-- INDEX:START", b"<!-- INDEX:END -->"),
}


def fail(msg):
    print(msg)
    print("NOTHING was written to any file. Undo is Discard Changes in "
          "GitHub Desktop.")
    sys.exit(1)


def fingerprint(path, raw):
    lf = raw.replace(b"\r\n", b"\n")
    if path in ZONES:
        start, end = ZONES[path]
        try:
            a = lf.index(start)
            b = lf.index(end) + len(end)
        except ValueError:
            fail("ERROR: the generated-zone markers are missing from "
                 + path + ".")
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


# ---------------------------------------------------------------- edits
# (file, label, old_bytes, new_bytes). Every old must match EXACTLY ONCE.

EDITS = []

# == skills/provenance-discipline/SKILL.md =============================

EDITS.append((SKILL, "SKILL  version line 2.13 -> 2.14 and the v2.14 paragraph",
    b"""Skill version: 2.13 | Cut from palomas_orrery @ ebdc55cc (v2.13),
earlier @ bfc0505e (v2.12), @ 159c5a2c (v2.11), @ 071a0a65 (v2.10),
earlier @ a263f73d (v2.9), @ 7f4a2f9f (v2.8), @ 3faa72a0 (v2.7),
@ f603be3 (v2.6), @ 731066f (v2.5), @ 6b99ace (v2.2),
@ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9)
| September 16, 2026
""",
    b"""Skill version: 2.14 | Cut from palomas_orrery @ dfa779bd (v2.14),
earlier @ ebdc55cc (v2.13), @ bfc0505e (v2.12), @ 159c5a2c (v2.11),
earlier @ 071a0a65 (v2.10), @ a263f73d (v2.9), @ 7f4a2f9f (v2.8),
@ 3faa72a0 (v2.7), @ f603be3 (v2.6), @ 731066f (v2.5),
@ 6b99ace (v2.2), @ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9)
| September 19, 2026
v2.14 writes down L-322 ruling (b), the read. It has been a ruling
since 2026-09-11 and lived only in the ledger, and a convention that is
not in the skill does not travel -- the protocol has recorded that
lesson three times. The Status Line gains The Read Field: a
"# Read: <page or table>, <date>, <reader>" line on a measured row
whose value is DRAWN in a published exhibit, or that feeds one. WHO
DOES THE READING IS DECIDED BY ACCESS, on Tony's ruling of 2026-09-19,
so the builder reads what it can open and names itself, a row only Tony
can open goes to him in a FILE and never as a list in chat, and a
source neither can open fails The Access Standard. A model's read
counts and the line says so; a read reconstructed from training is
worse than no read, because it stops the next reader from looking. The
Unit Field now points at constants_tokens.py, which owns the token
table, the RETIRED_TOKENS list and the "named number" marker, and names
"# Read:" among the fields a row's single slice visit writes. Rule 8's
enumeration names BOTH routes to a derived row -- its arithmetic and
its "# Derived:" line -- because a typed number carrying a
"# Derived:" note is a literal whose arithmetic lives in prose, and the
checker must still name it. The worksheet schema gains the "Read by"
column promised on 2026-09-11 and missed by 2.13. Handle L-322.
"""))

EDITS.append((SKILL, "SKILL  The Unit Field points at constants_tokens.py and names # Read:",
    b"""quantity and retires as a token. The migration is walked by body,
Earth first, and each row is visited once: `# Unit:`, `# Status:` and
`# Figures:` (below) are written at that single visit.
""",
    b"""quantity and retires as a token.

**`constants_tokens.py` owns the token table.** One entry per token,
carrying its dimension -- an astropy unit string, or the words `named
number` for a quantity with no physical dimension that is still a named
thing, which is what `l_shell` is -- and, for a unit defined by a value
in the store, the row that defines it. A retired token is not simply
absent: `RETIRED_TOKENS` holds it with the reason, so a checker meeting
`dimensionless` on a row says what is wrong with it instead of saying
the token is unknown. A token in neither table is a failure. That file
replaces two pieces of the gallery that did this job by inference,
`SCALAR_UNITS` and the suffix reader.

The migration is walked by body, Earth first, and each row is visited
ONCE: `# Unit:`, `# Status:`, `# Figures:` (below) and, where the row is
in scope, `# Read:` (below) are all written at that single visit.
"""))

EDITS.append((SKILL, "SKILL  The Read Field, a new section beside The Unit Field",
    b"""### Geometry Constants Are First-Class Claims
""",
    b"""### The Read Field

**A typed-in number can be checked by a person or a model reading the
source against it, and `# Read:` records that this happened.** One line
beside the value, in the same comment block as `# Unit:`, `# Status:`
and `# Figures:`:

```
# Read: <page or table>, <date>, <reader>
```

```python
EARTH_MAGNETOPAUSE_SHUE_A1_RADII = 10.22
# Read: Table 1 "After Fit", p. 17,698, 2026-09-11, Claude Fable 5.1
```

**Scope: a measured row whose value is DRAWN in a published exhibit,
and any row that feeds one.** Not every row in the store. A declared
drawing choice has nothing to read against, and a measured row nobody
draws is outside the bound, by The Artifact Bounds the Audit.

**Who does the reading is decided by ACCESS, not by importance.** The
scope of 2026-09-11 said the check applies "where critical" and never
defined the word. Tony's ruling, 2026-09-19:

> what I meant by critical is where your own search tools cannot read a
> needed source but I can.

He glossed "need" in the same message: a number is in the store and
needs a source. So the question is never how important the number is.
An unimportant number behind a wall only Tony can open still goes to
him, and a load-bearing number the builder can open never does.

Three branches, and a row takes whichever applies:

- **The builder can open the source.** The builder reads it against the
  row and writes the line, naming ITSELF as the reader. A model's read
  is a real read, recorded as a model's.
- **The builder cannot open it and Tony can.** The row goes on a
  reading list for him: one file, one row per constant, with the link,
  where to look in it, and the number he should expect to see. That
  list is Tony's WHOLE share of the reading -- nothing else in a slice
  walk asks him to read a source -- and it is a file he opens at his
  machine, never a list in chat. His line carries his name and the date
  he read.
- **Neither can open it.** The citation fails The Access Standard.
  Re-home it to an open authority carrying the same value, or remove
  the claim and note the gap.

**A read counts only if the source was actually OPENED.** The line
records what was opened, with the title as printed and the table or
page, under The Access Standard's rule that a source names what was
opened rather than what it cites. A read reconstructed from training is
worse than no read, because the line stops the next reader from looking
while recording nothing that was checked. This is a `# Source:` over
recalled data, one layer out.

**No line at all means the row has not been read**, the way a missing
`# Status:` means the pass has not reached the value. Inside a closed
slice a missing line on an in-scope row FAILS; outside one it is named
as not yet migrated.

(Tony's rulings, 2026-09-11 and 2026-09-19, on L-322 ruling (b),
confirmed point by point on 2026-09-19 before this section was written.
The fourteen magnetosphere rows already carry a dated per-row record in
`documentation/L305_gap1_read_record_20260911.md`, a model's read of
Tony's PDFs; their lines name the model.)

### Geometry Constants Are First-Class Claims
"""))

EDITS.append((SKILL, "SKILL  Rule 8's enumeration names both routes to a derived row",
    b"""gap outside one. Enumeration is by the `# Derived:` line, not by a
`# Status:` word: at 2.12 the checker found derived rows by Status and
saw 2 of 27.
""",
    b"""gap outside one. ENUMERATION NAMES BOTH ROUTES TO A DERIVED ROW, never
a `# Status:` word: a row whose right-hand side is ARITHMETIC over other
store rows, and a row carrying a `# Derived:` line. They are not the
same set. `constants_rows.py` treats a typed number with a `# Derived:`
note as a LITERAL whose arithmetic lives in prose rather than in the
expression, so it is invisible to a walk that looks only at right-hand
sides -- and the two `TRANSITIONAL` standoffs are exactly that shape
until they revert. The checker names rows found by either route, and an
expression with no `# Derived:` line is itself a named gap. (At 2.12
enumeration went by Status and saw 2 of 27.)
"""))

EDITS.append((SKILL, "SKILL  the worksheet schema gains the Read by column",
    b"""| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |
""",
    b"""| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Read by | Notes |

**`Read by` names WHO opened the source**, a model by name or Tony, and
it is not optional. A verdict is only as good as the reading behind it,
and the two readings are reached differently: a model reads what its
search tools can open, and Tony reads what only he can (The Read Field,
above). A worksheet that does not say which happened cannot be turned
into a `# Read:` line without guessing, and guessing there is the
failure that rule exists to prevent. (Promised on 2026-09-11; it did
not ride 2.13.)
"""))

# == PROJECT_INSTRUCTIONS.md ===========================================

EDITS.append((PROTOCOL, "PROTOCOL  header stamp and SHA anchor move to v3.63",
    b"""Tony Quintanilla, PE | Claude | v3.62 | September 19, 2026

Cut from e1a79f67 at https://github.com/tonylquintanilla/palomas_orrery
""",
    b"""Tony Quintanilla, PE | Claude | v3.63 | September 19, 2026

Cut from dfa779bd at https://github.com/tonylquintanilla/palomas_orrery
"""))

EDITS.append((PROTOCOL, "PROTOCOL  the v3.63 entry is added above v3.62",
    b"""v3.62 (September 19, 2026): No rule changed in this document. TWO skill
""",
    b"""v3.63 (September 19, 2026): No rule changed in this document. ONE
skill bump, taken ahead of the walk it serves, which is v3.55's
ordering.

provenance-discipline 2.13 -> 2.14 (L-322). The READ is written down.

IT HAD BEEN A RULING SINCE 2026-09-11 AND LIVED ONLY IN THE LEDGER.
L-322 ruling (b) said a bare literal's check is a human reading the
source against it, "where critical", and the skill that fires on every
constants session did not carry any of it. This is the same lesson as
v3.57 and v3.61: a convention that is not in the skill does not travel,
and the field the walk is about to write has to be defined before the
walk writes it.

WHAT "CRITICAL" MEANS IS TONY'S, AND IT IS ABOUT ACCESS. Asked on
2026-09-19 what the word meant, he said it is "where your own search
tools cannot read a needed source but I can", and glossed "need" in the
same message: a number is in the store and needs a source. So the split
is not by importance. An unimportant number behind a wall only Tony can
open still goes to him; a load-bearing number Claude can open never
does. Three branches follow -- the builder reads what it can open and
names itself on the row, a row only Tony can open goes to him in a FILE
with the link, where to look and the number to expect, and a source
neither can open fails The Access Standard and is re-homed or removed.
His reading list is his WHOLE share: nothing else in a slice walk asks
him to read a source.

A MODEL'S READ COUNTS, AND THE LINE SAYS SO. Tony confirmed this
directly rather than leaving it to be inferred: the model may read a
source. The fourteen magnetosphere rows already work that way. What
does NOT count is a read reconstructed from training, because the line
then stops the next reader from looking while recording nothing that
was checked -- a `# Source:` over recalled data, one layer out.

THE WORDING WAS APPROVED BEFORE IT WAS CUT. It is his ruling being
written down, so the section was brought to him in full and he answered
four questions about it point by point. Three smaller things ride the
same bump: The Unit Field now points at `constants_tokens.py`, which
owns the token table, the retired list and the "named number" marker;
Rule 8's enumeration names both routes to a derived row, its arithmetic
and its `# Derived:` line, which are not the same set; and the
worksheet schema gains the "Read by" column promised on 2026-09-11 and
missed by 2.13.

THE OBLIGATION TRAVELS, as it always does. This session loaded 2.13,
and a reinstall cannot be verified from inside the session that makes
it. The next session confirms its loaded copy reads 2.14 before any
provenance or store work, and that session is Stage C, the walk itself.

The header stamp and the SHA anchor move with this entry.

Version history: v3.60 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

v3.62 (September 19, 2026): No rule changed in this document. TWO skill
"""))

EDITS.append((PROTOCOL, "PROTOCOL  v3.60 is REMOVED from the resident three",
    b"""v3.60 (September 16, 2026): No rule changed in this document. TWO
skill bumps, taken as the session's first action, ahead of the build
they serve.

interactive-exhibit 1.2 -> 1.3 (L-332) and orrery-coding-conventions
1.8 -> 1.9 (L-331).

THE EXHIBIT SKILL WAS FIVE ROUNDS STALE. Version 1.2 was cut on
2026-09-11 and described the rooms' chrome as L-316 round 2 and L-318
rounds 1 and 2 left it. Six more rounds ran on Tony's phone on
2026-09-15/16, each checked before the next was built, and the skill
that fires on any edit to that chrome did not know any of them: the
arrow cross's corner is now one CSS rule; a drawer row has a finger-
sized target and GO ticks an unticked shell; a break inside a sentence
is soft; the portrait phone's text box has no arrow and sits mid-view;
and a phone tap reaches a marker through a second Plotly rule read from
v2.35.2's pick pass. The skill also gains the hover budget suite in its
pre-test step, with the note that the suite does not build the Sun
room -- which is how four Sun hovers missed the move to the i panel
(L-331). A checker passes on what it does not look at.

THE ONE NEW RULE IS TONY'S, and it rides both skills. On 2026-09-16,
reading the Sun room's Galactic Tide hover -- "DECLARED --" at the top,
"Not a measurement." at the bottom -- he said that declared-not-
measured means little to a visitor, and then made it general: "In
general we should avoid compressed language in the hovertext." That is
this document's Register Rule pointed the other way: the Register Rule
governs what Claude writes to Tony; this governs what the plot says to
a visitor, who has been through none of the conversation. It is written
into interactive-exhibit for the gallery's hovers and into
orrery-coding-conventions for the orrery's, because the orrery's hovers
are where it reaches next (L-321), and a convention that is not in the
skill a hover session loads does not travel. The rule changes the
words, not the facts or the caveats; reworded hovers go to Tony first.

THE ORDERING IS v3.55's: the bumps precede L-331's build, so the next
exhibit session's stale-skill gate fires on a matching manifest. The
obligation still travels: this session loaded 1.2 and 1.8, and a
reinstall cannot be verified from inside the session that makes it. The
next session confirms its loaded copies read 1.3 and 1.9 before exhibit
or hover work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.57 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.


Functional for Claude, readable for human, signal preserved.
""",
    b"""Functional for Claude, readable for human, signal preserved.
"""))

# == documentation/PROJECT_INSTRUCTIONS_HISTORY.md =====================

EDITS.append((HISTORY, "HISTORY  v3.60 lands at the end of PART 1",
    b"""(Moved down from the resident protocol on 2026-09-19 when v3.62
made a fourth entry.)

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37
""",
    b"""(Moved down from the resident protocol on 2026-09-19 when v3.62
made a fourth entry.)

v3.60 (September 16, 2026): No rule changed in this document. TWO
skill bumps, taken as the session's first action, ahead of the build
they serve.

interactive-exhibit 1.2 -> 1.3 (L-332) and orrery-coding-conventions
1.8 -> 1.9 (L-331).

THE EXHIBIT SKILL WAS FIVE ROUNDS STALE. Version 1.2 was cut on
2026-09-11 and described the rooms' chrome as L-316 round 2 and L-318
rounds 1 and 2 left it. Six more rounds ran on Tony's phone on
2026-09-15/16, each checked before the next was built, and the skill
that fires on any edit to that chrome did not know any of them: the
arrow cross's corner is now one CSS rule; a drawer row has a finger-
sized target and GO ticks an unticked shell; a break inside a sentence
is soft; the portrait phone's text box has no arrow and sits mid-view;
and a phone tap reaches a marker through a second Plotly rule read from
v2.35.2's pick pass. The skill also gains the hover budget suite in its
pre-test step, with the note that the suite does not build the Sun
room -- which is how four Sun hovers missed the move to the i panel
(L-331). A checker passes on what it does not look at.

THE ONE NEW RULE IS TONY'S, and it rides both skills. On 2026-09-16,
reading the Sun room's Galactic Tide hover -- "DECLARED --" at the top,
"Not a measurement." at the bottom -- he said that declared-not-
measured means little to a visitor, and then made it general: "In
general we should avoid compressed language in the hovertext." That is
this document's Register Rule pointed the other way: the Register Rule
governs what Claude writes to Tony; this governs what the plot says to
a visitor, who has been through none of the conversation. It is written
into interactive-exhibit for the gallery's hovers and into
orrery-coding-conventions for the orrery's, because the orrery's hovers
are where it reaches next (L-321), and a convention that is not in the
skill a hover session loads does not travel. The rule changes the
words, not the facts or the caveats; reworded hovers go to Tony first.

THE ORDERING IS v3.55's: the bumps precede L-331's build, so the next
exhibit session's stale-skill gate fires on a matching manifest. The
obligation still travels: this session loaded 1.2 and 1.8, and a
reinstall cannot be verified from inside the session that makes it. The
next session confirms its loaded copies read 1.3 and 1.9 before exhibit
or hover work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.57 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-19 when v3.63
made a fourth entry.)

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37
"""))

# == LEDGER_CONSOLIDATED.md ============================================

EDITS.append((LEDGER, "LEDGER  a dated line on L-322 recording the bump",
    b"""**Tony's ruling, 2026-09-19 -- what "critical" means in ruling (b).**""",
    b"""**Note (2026-09-19) -- the ruling below is now IN THE SKILL, which is
where it fires.** provenance-discipline 2.13 -> 2.14, cut from orrery
`dfa779bd`, under protocol entry v3.63 and the four binding steps in
ledger-and-session-records. The Status Line gains The Read Field: the
form, the scope, Tony's ruling in his words, the three access branches,
and that a model's read counts and names the model. Tony approved the
wording before it was cut, answering four questions about it point by
point, and glossed "need" as a number that is in the store and needs a
source. Three smaller things ride the same bump: The Unit Field points
at `constants_tokens.py` and its retired list and "named number"
marker; Rule 8's enumeration names both routes to a derived row, its
arithmetic and its `# Derived:` line; and the worksheet schema gains
the "Read by" column promised on 2026-09-11 and missed by 2.13.
**Tony-action (do):** reinstall provenance-discipline 2.14 from
Settings > Skills after the push, then START A NEW SESSION for Stage C.
A mid-session reinstall cannot be verified from inside the session that
makes it, so THE NEXT SESSION confirms its loaded copy reads 2.14
before any provenance or store work.
**Tony's ruling, 2026-09-19 -- what "critical" means in ruling (b).**"""))


def main():
    here = os.path.basename(os.path.abspath(os.getcwd()))
    if here == "documentation":
        fail("ERROR: this patch is being run from documentation/. Run it "
             "from the ORRERY repo ROOT (next to " + PROTOCOL + "), then "
             "move it into documentation/ afterwards.")

    for path in BASE:
        if not os.path.exists(path):
            fail("ERROR: " + path + " is not here. Run this patch from the "
                 "ORRERY repo ROOT.")

    raws = {}
    for path, want in BASE.items():
        with open(path, "rb") as handle:
            raws[path] = handle.read()
        got = fingerprint(path, raws[path])
        if got != want:
            fail("ERROR: " + path + " is not the file this patch was built "
                 "against.\n"
                 "  expected content fingerprint " + want + "\n"
                 "  found                        " + got + "\n"
                 "  (Line endings are excluded, and so is any generated "
                 "zone.)\n"
                 "  If this patch already ran, that is the expected "
                 "result: it is one-shot.")

    # All four bases are good. Apply every edit in memory; write nothing
    # until all of them have matched, so a late failure cannot leave two
    # files edited and two not.
    out = dict(raws)
    for path, label, old, new in EDITS:
        is_crlf = raws[path].count(b"\r\n") > 0
        if is_crlf:
            old = old.replace(b"\n", b"\r\n")
            new = new.replace(b"\n", b"\r\n")
        n = out[path].count(old)
        if n != 1:
            fail("ANCHOR FAIL: expected exactly 1 match, found %d -- %s\n"
                 "  anchor began: %r" % (n, label, old[:70]))
        out[path] = out[path].replace(old, new)

    for path, data in out.items():
        try:
            data.decode("ascii")
        except UnicodeDecodeError as exc:
            fail("ERROR: the result for " + path + " is not ASCII (%s)."
                 % exc)

    for path, data in out.items():
        with open(path, "wb") as handle:
            handle.write(data)

    for path, label, _old, _new in EDITS:
        print("  ok  " + label)
    print("")
    for path in sorted(out):
        print("      %-46s %7d -> %7d bytes"
              % (path, len(raws[path]), len(out[path])))
    print("")
    print("patch applied (4 files, %d edits)" % len(EDITS))
    print("")
    print("NOW, in order:")
    print("  1. Run skills_index.py from this folder. It rebuilds the")
    print("     Skill Manifest table in PROJECT_INSTRUCTIONS.md. Expect")
    print("     it to report that the manifest was advertising")
    print("     provenance-discipline 2.13 before it overwrites it with")
    print("     2.14. That report is the tool working.")
    print("  2. Run ledger_index.py from this folder. Expect OK, 335")
    print("     L-blocks, 192 live items -- no block changed status, so")
    print("     nothing migrates this time.")
    print("  3. Move this script into documentation/.")
    print("  4. Run the orrery maintenance run.")
    print("  5. Commit ALL of it together -- the skill, the protocol, the")
    print("     history file and the ledger -- and push. The four travel")
    print("     in ONE commit; that is the binding rule.")
    print("  6. REINSTALL provenance-discipline 2.14 from Settings >")
    print("     Skills. This session cannot verify that, so Stage C is a")
    print("     NEW session and its first act is confirming its loaded")
    print("     copy reads 2.14.")
    print("  7. Tell Claude the new orrery SHA.")
    print("")
    print("Undo at any point is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
