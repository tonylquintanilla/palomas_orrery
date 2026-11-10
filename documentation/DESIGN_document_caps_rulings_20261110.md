<!-- Doc-Kind: hand | Design record of the talk of November 10, 2026: how the working documents are kept from growing (a cap and an overflow home in each one's first lines, pay where you touch, a printed check), and the order of the catch-up. Communication; carries Tony's rulings until the ledger has them. -->
# Design record: document caps, and the catch-up

Built on orrery 3198bc98f58b34573ab924397734a847c82cba30 at
https://github.com/tonylquintanilla/palomas_orrery
and gallery cea21af180b98a6694cb6bfb1083eca38e9b5c5d at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-10, 10:03 Chicago). The review this
talk followed read the orrery at b3ce81f8; the one commit since is the
nightly run's record.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION (zero code). Companion:
documentation/REVIEW_fundamental_documents_20261110.md, which holds the
measurements. This record holds what was decided and what is still
open. No ledger item exists yet: a website build was writing to the
ledger during this talk, so the rulings below wait here until the
ledger is next written, and the item takes the next free handle then.

## What the review found, in three sentences

The governing documents are accurate where they were checked. They
only grow: each has a rule for how a line gets in and none for how a
line leaves, so each carries its own history. Where We Are is the
exception, with a length cap and a rule for when a line leaves, and it
is the one that works.

## Tony's rulings, in his words (Chicago time)

- 09:42, on the Braid: "The reason I described the braid idea is that
  builds were being delayed by what I saw as secondary items. The idea
  is to move along themes."
- 09:48, on how growth is controlled: "I used to have a length cap on
  the project instructions at 800 lines. There really no other method
  to control growth. Generally where I touch works best with periodic
  reassessments like this one. For the master plan generally that's
  when a major build is finished."
- 09:52, asking for a method: "The harness is growing too. The
  complexity is too much for me to figure out well."
- 09:57, to the three rules below: "That makes sense."
- 10:02, to the order below: "This makes sense. I would like this
  session to work as the coordinator and we can split off chunks as we
  decide, on a priority basis between other sessions as you said."

What these settle:
1. Growth is controlled by a length cap on each working document.
2. A session pays where it touches: one that adds to a document at
   its cap moves something out first.
3. A reassessment like this one is held from time to time. The master
   plan is restamped when a major build is finished.
4. Upkeep never stands in front of a build. It goes between builds,
   one piece at a time, by priority.
5. No new skill for this. The rule is written where the records
   skill already speaks of documents, replacing text there.

## The method: three rules

1. EACH WORKING DOCUMENT STATES ITS CAP AND ITS OVERFLOW HOME IN ITS
   FIRST LINES. The cap is a size. The overflow home is the named
   place an old line goes when it leaves: a history file, the ledger,
   or nowhere but git.
2. A SESSION THAT ADDS TO A DOCUMENT AT ITS CAP MOVES SOMETHING OUT
   FIRST, to the home the document names. The session does not choose
   the destination.
3. THE MAINTENANCE RUN PRINTS EVERY DOCUMENT OVER ITS CAP, BY NAME,
   with its size and its cap. Only Tony changes a cap's number.

Which documents: the ones read every session or when their work comes
up. The protocol, the twelve skills, Where We Are (it has its cap
already), the master plan, the two READMEs, the ledger. About
eighteen. A handoff, a brief or a design record is written once and
gets no cap. A generated document is written by its tool and gets
none.

One correction to what was said in the talk. It was said that every
document opens with a one-line tag where the cap can sit. That is
true of the documents doc_index.py reads. A skill opens with a header
block instead, which skills_index.py reads. So the cap sits in the
first-line tag for a document and in the header block for a skill.
It is one rule read by two tools that already exist.

The ledger is the special case. A line count does not suit it. It
needs its closed items in a companion file under the same handles,
and a size limit for one item.

What a cap lets go: the read plans, the contents lists and the
three-entry rule exist because the skills are too long to read in one
go. Under a cap most of that machinery can be retired. Which parts,
and when, is decided as each skill is reduced.

## The order of the catch-up

Stop the growth first. Then reduce one document at a time.

1. THE MECHANISM. One Code session on the orrery. The two tools read
   the caps and the maintenance run prints anything over. Every cap
   starts at the document's size today, so nothing grows from that
   day and nothing is red. The same session renames the two stray
   CLAUDE.md files under documentation/ (the February handoff, and
   the door's canonical copy), which Claude Code loads into a session
   that reads a file beside them.
2. THE EXHIBIT SKILL, SPLIT. One Code session. Rules stay in the
   skill. The description of what the page does moves to a reference
   document, read by section, with no reinstall.
3. THE PROTOCOL. A talk, then one session. Tony's decisions sit here
   (below).
4. THE LEDGER, REDUCED. One Code session. A tool moves closed items
   to the companion file and drops the 777 lines of stamps at the top.
5. THE OPEN ITEMS, TRIAGED. The coordinating session proposes an
   outcome for each of the 242, grouped by theme: on the road,
   deferred with its reason, or closed. Tony rules on the groups and
   corrects the exceptions.
6. THE MASTER PLAN AND BOTH READMES, RESTAMPED when step 2b of the one
   tree (L-515) lands.

After each step that document's cap drops to its new size. A brief is
written for a step when its session is next, not before (the
protocol's Token Economy).

## Not decided

- The protocol's cap: 800 lines again, or higher. Moving out the
  skill table and the version history takes it from 1,480 lines to
  about 1,170. Reaching 800 needs about 370 more; the candidates are
  the gates for the retired store, the origin notes in parentheses,
  and Part 4.
- Whether the skill table leaves the protocol, with the stale-skill
  check becoming "the installed skill equals the repository's copy".
  That is a change to a [CRITICAL] gate, so it is Tony's. Its gain: a
  skill change no longer makes a protocol version, and the protocol is
  pasted into the Project only when one of its rules changes.
- Each skill's target cap.
- The size limit for one ledger item.
- The harness: 57 of the 176 modules are developer tools. Measured,
  not reviewed. Its own look, later.

## Owed to the records

- A ledger item for this work, and these rulings on it.
- One line on Where We Are's road, beside the housekeeping line, when
  the page is next written.
- The four small fixes listed in the review, three of which ride
  step 1 or step 6.

Written November 10, 2026 with Anthropic's Claude Fable 5.2 (the model
this session is configured for), the coordinating session, linked to
Tony's computer.
