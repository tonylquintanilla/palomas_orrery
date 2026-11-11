<!-- Doc-Kind: hand | The brief for one Claude Code session through the python_work door: L-522 (document caps), step 2, the exhibit skill split into its rules and a reference. Communication; written once, read by its session. -->
# Brief: document caps, step 2, the exhibit skill's split

Built on orrery f74ab006e6804fd71b16cf96b4712f4198940b1b at
https://github.com/tonylquintanilla/palomas_orrery
and gallery e21b6746fc4ee71fb7af710c3b4a1a10885fcd2b at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-10, 23:35 Chicago). Nightly bot commits
since are expected. This brief is in Tony's next orrery push; the
session reads it in the folder in front of it.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session through the python_work door, in
BOTH repositories: the skill and the records in the orrery, the new
reference and one small check in the gallery. No code of the website's
page or the orrery is changed. Written November 10, 2026 with
Anthropic's Claude Fable 5.2, the coordinating session.

Tony's word. In his run record of that night, read at 23:24, choosing
the order: "let's do the split first. i
will handoff the website work to a new Opus coordinator that can pick
up the updated skills." 23:34, to the plan this brief follows, which
Claude proposed: "i read the plan and it sounds reasonable. please
proceed."

## What step 2 is, in one paragraph

`skills/interactive-exhibit/SKILL.md` is 2,440 lines and sits at its
cap. About twenty of its rules are short, five to ten lines each. Six
sections are long, 1,619 lines between them: they describe what the
page does today, with about 440 code names and snippets in backticks. Every website
build has added to them, and each addition has cost a skill version, a
protocol version, a reinstall and a paste. This session parts the
two. The rules stay in the skill. What the page does, and where, moves
whole into a reference in the website's own repository, where a build
changes it in the same commit as the code. History moves to the
skills' history file. Nothing is rewritten that can be moved.

## Start

1. The orrery's CLAUDE.md from its first step, then the gallery's. Both
   bases recorded; edits waiting in either folder: say so and stop.
2. L-522 (document caps) in the ledger: the six steps, and step 1's
   close. `DOCUMENT_CAPS.md`.
3. Skills: interactive-exhibit (1.40), in full, once, with its line
   numbers kept; ledger-and-session-records (1.23), the parts on a
   skill's version entries and the binding rule; safe-file-editing
   (1.14).
4. Ask Tony ONE thing before building: this session rewrites a skill's
   file and adds a file and a check to the website. May it edit
   `skills/interactive-exhibit/SKILL.md`, run `skills_index.py`, add
   one protocol version entry, and write in the gallery folder the two
   files this brief names?

## The three destinations

Each line of the old skill goes to exactly one of them.

1. THE SKILL keeps what is a RULE: it tells a session how to work, and
   it would still be true if the page's code were rewritten. "Never
   mutate a plot from inside a Plotly event handler" is the model: a
   few lines, the reason, the handle.
2. THE REFERENCE takes what DESCRIBES: what the page does today, which
   function or file does it, in what order, with Tony's rulings on what
   the room must do. It is a new file in the gallery, at its root
   beside `interactive.html`; the name is method, say it. It opens with
   a Doc-Kind line and three sentences: it says what the page does NOW;
   a build that changes the page changes it in the same commit; changed
   text is replaced, never appended to, and git keeps the old.
3. `documentation/SKILL_HISTORIES.md` takes HISTORY that stands alone:
   the skill's version entries past the three the three-entry rule
   keeps, and any paragraph that only tells how a thing used to be.

The six long sections, at the base, by their line numbers:
- Provenance is part of the build (183 to 510)
- What a room opens on is SERVED, not coded (511 to 677)
- One drawer for every centre (678 to 824)
- One picture: the folds and the view's middle (825 to 964)
- The Solar System room's drawer: bodies, not shells (965 to 1689)
- A room's drawer lists its shells where each begins (1690 to 1801)

## The job, in three parts, with a stop and a report after each

**Part 1: the plan, before any edit.**
A table of every section of the old skill: its lines, its destination,
and for a section that is split, how many lines go where. With it, the
text of each NEW rule the six long sections leave behind in the skill:
one short rule each, in the style of the short ones, its tier kept,
with the old line numbers each sentence rests on. Nothing is written to
a file in this part. The coordinating session reads this report before
Tony's go-ahead.

**Part 2: the moves.**
- The six sections' text moves into the reference WHOLE, under its own
  headings, in its own words. A remark inside a sentence on how a thing
  used to be ("until v1.33") moves with its sentence; it is not cut out
  here. A later build that changes a paragraph drops such remarks then.
- In the skill each of the six is replaced by its rule from Part 1 and
  one line naming the reference's section.
- The rest of the skill is judged the same way, section by section; say
  in the report what else moved and why. The target for the skill is
  500 lines, the size `skills_index.py` already warns above. If it
  cannot be reached without rewriting rules, stop at what moving alone
  gives and say what is in the way. The rules come first in the file.
- The skill's `fires_when` is about 4,000 characters and lists features
  one by one. Cut it to the few phrases that make the skill fire: a
  room or an exhibit in `interactive.html`, its drawer and chrome, the
  served words and numbers and where they come from, testing a room.
- THE ACCOUNT, by script, printed in the report: every non-blank line
  of the skill at the base is found, word for word, in exactly one of
  the new skill, the reference, or the history file. A line found in
  none is on a list that is printed whole, each with its reason. A line
  found in two is a fault. And every line of the new skill that was not
  in the old is printed: those are the new rules and pointers, and
  nothing else.

**Part 3: the check, and the doors.**
- One small check in the gallery's maintenance run: every code name
  the reference gives in backticks (a function, a file, an object's
  member) is found in the code it belongs to, the gallery's or the
  orrery's. It prints how many names it examined, how many backticked
  things it set aside as not names and of what kinds, and each name it
  did not find. A name not found is red. Show it going red on a planted
  name, on a throwaway copy.
- Its first run is a finding. Names the old skill gave that the code no
  longer has are listed for Tony by name. Correct the reference where
  the right name is plain from the code; where it is not, leave the
  sentence, mark it, and list it.
- The gallery's `CLAUDE.md`, under "The skills": the reference's name;
  a session reads the section for the part it changes, and changes the
  reference in the commit that changes the page. The exhibit skill
  itself carries the same pointer once.

## Out of scope

- No rule is added, dropped or changed in meaning. A rule that looks
  wrong or stale is listed for Tony, not fixed.
- No other skill. No code of the page, the assembler or the orrery.
- The reference is not tidied, reordered or shortened beyond the name
  corrections of Part 3.
- The reference gets no row on `DOCUMENT_CAPS.md`: the nightly run on
  GitHub checks out the orrery alone. Say so on L-522.

## Checks

- Part 2's account, clean.
- `skills_index.py --check`, and the orrery maintenance run whole: no
  row red that was green at the base.
- The gallery maintenance run, offline, whole, with the new row.
- `doc_index.py --caps` after the caps are lowered.

## Close

- The skill's version entry and the bump, the protocol's version entry
  and the manifest, by the binding rule. The manifest's table shrinks
  with `fires_when`; the protocol ends shorter.
- `DOCUMENT_CAPS.md`: the exhibit skill's cap and the protocol's cap
  are LOWERED to their new sizes. The page's own text allows that to a
  step that shortens a document. No cap is raised.
- L-522: step 2 done, the sizes before and after by name, the names not
  found, and what is owed. Where We Are by section, within its 130
  lines; the build track's lines are left as they are.
- The final report in the form the doors set, with "Where this leaves
  us" and, if there is one, "One final thought".
- For the website's new coordinating session, one plain paragraph in
  the report: what the skill now holds, what the reference holds, and
  where each is read.
- Commit and push are Tony's: the website, then the orrery. Then he
  reinstalls interactive-exhibit and pastes the protocol.
