<!-- Doc-Kind: hand | Design record of the talk of November 10, 2026, afternoon, by phone: what leaves the protocol, what stays, and its cap of 800 lines (L-522, step 3). Communication; carries Tony's rulings in his words. -->
# Design record: reducing the protocol (L-522, step 3)

Built on orrery aa4b61841be3c906e32f047e9021076c55aa46bb at
https://github.com/tonylquintanilla/palomas_orrery
and gallery 2dec9fc55164be4db9e6b0b591034d0952f525f6 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-10, 15:10 Chicago). The protocol read
is v3.136, 1,496 lines.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION (zero code). The talk for step 3 of L-522
(document caps), held by phone, one question to a message. The rulings
are on L-522. This record holds Tony's words and what the draft must
do. No draft of the protocol exists yet; it is written when step 3's
session is next.

## The finding the rulings rest on

Tony, 14:57: "Truthfully the only document I track myself is the Where
We Are unless I'm searching for something."

So the protocol's reader is Claude, and any outside model Tony carries
it to. The test for each part is whether it changes what a session
does. It is not written for Tony to read, and it need not be.

## The five rulings, in Tony's words (Chicago time)

1. THE SKILL TABLE LEAVES THE PROTOCOL. Asked whether it should, Tony,
   14:53: "Only for Claude to determine which skills to fire. That's
   the only purpose. Maybe in the maintenance report too, not sure. I
   do not read it." The session read that as yes and said so; Tony went
   on to the next question. Because this rewrites a [CRITICAL] gate,
   the new wording comes to him in the draft before it stands.
2. THE HISTORY LEAVES, ONE LINE STAYS. Tony, 14:57: "I would say one
   line with the pointer to the history file. Make useful to Claude."
   The version history goes too, leaving one line for the current
   version.
3. THE PHILOSOPHY MOVES TO THE ORIGINS DOCUMENT; A SHORT CORE STAYS.
   Tony, 15:01: "I would say move the original to origins. This is
   legacy. Abbreviate it to what is useful to Claude today. We should
   also remember that a lot of this was written for older models and
   it should be useful to Claude 5.x"
4. THE RULES ARE SORTED BY WHAT THEY GUARD AGAINST, AND THE LEDGER
   DECIDES THE THIRD GROUP. Tony, 15:05: "I agree. And I am not a good
   judge because Claude makes few mistakes now. Redirects are mostly
   clarifications or new ideas. But guards and checks are working in
   the background I cannot see."
5. THE CAP IS 800 LINES. Tony, 15:08: "Confirmed".

## What the draft does, ruling by ruling

1. The table. `skills_index.py` writes the table of skills, versions
   and "fires when" into its own generated file under `skills/`, and
   the Code door (`CLAUDE.md`) points to it. In a talk session the
   account already gives each installed skill's name and description,
   which is what makes it fire. The protocol keeps a plain list of the
   skills' names, which does not change when a version does. The gate
   becomes: the installed skill equals the repository's copy, compared
   byte for byte where the session has a shell; a session with no shell
   says it could not compare, and does not build. A skill change then
   makes no protocol version, and the protocol is pasted into the
   Project only when one of its rules changes. Tony still reinstalls a
   skill that changed.
2. The history. Each rule keeps one line: the date, the ledger handle,
   and the file the story is in,
   `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`. The paragraphs move
   there whole. The line is written for a session's use: it says what
   the founding case was in a few words, so the rule can be applied
   with judgment.
3. The philosophy. Part 4 and the quotations move whole and unedited
   into `PROJECT_ORIGIN.md`, marked as legacy with the date they left.
   The protocol keeps what changes a session's conduct: ask when
   unsure; the conversation is the mechanism and not a delay; access is
   not understanding; the orrery and the website's assembler are two
   instruments. The preamble stays.
4. The sort.
   - Truth and checking (a stale base, a citation over recalled data, a
     check that cannot fail, the commit round trip): they do not depend
     on the model. They stay.
   - How a session talks to Tony (plain speech, one ask to a message):
     a stronger model compresses more. They stay.
   - Coaching on basic conduct (the modes, the quick decisions, the
     trigger table, most anti-patterns, agentic against targeted;
     roughly 140 lines): the candidates. For each, the ledger is
     searched for a session on a current model breaking it. One that
     was broken stays, with its case. One that was not shrinks to a
     line or goes. A removed rule that later fails comes back with its
     case, by the protocol's own test for promoting a rule. A model's
     own word that it no longer needs a rule is not evidence.
5. The cap. 800 lines, written on `DOCUMENT_CAPS.md` when the reduced
   protocol lands. If the draft cannot get under 800, the session
   brings Tony what is in the way; it does not ask for a higher number.

Also in the draft, from the review and not asked at this talk: the
gates that guard uploads and the project-file snapshot, a store gone
since v3.30, are replaced by gates for the stores in use (the working
copy on Tony's computer, GitHub at HEAD, a linked session's writes
read back); Session Start names Where We Are; the kinds of session
(L-499) are stated. Each is a change to a gate, so each is Tony's to
rule on the draft.

## The arithmetic, an estimate until the draft exists

From 1,496 lines: the table and its rule, about 225 out; the version
history, about 155 out; the origin notes cut to a line each, about 200
out; the philosophy cut to its core, about 140 out; the coaching, after
the ledger check, perhaps 100 out; the stores in use, the kinds of
session and the caps rule, about 40 in. Near 700 lines.

## Evidence that the first group is still needed

Two faults of the checking kind on November 10, neither seen by Tony
at the time: the build wrote on Where We Are that the page's date and
the ledger's newest stamp agreed when the ledger had no stamp for that
day; and this session's second write of the ledger delivered an older
copy, which the read-back caught (L-522).

And one departure from a gate's letter, on November 9 (the protocol's
v3.135 entry): a session found its loaded skill one version behind,
compared the account's copy on disk with the repository's byte for
byte, found them equal, worked from that copy and said so. The gate
says stop and reinstall. The session did what ruling 1 now makes the
rule. At the talk this was called a third fault; that was too strong,
and it is corrected here.

Written November 10, 2026 with Anthropic's Claude Fable 5.2 (the model
this session is configured for), the coordinating session, linked to
Tony's computer.
