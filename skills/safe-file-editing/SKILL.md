---
name: safe-file-editing
description: Safe practices for editing and patching existing source files, in any project. Use whenever editing existing code files (especially .py), delivering line-targeted snippets, applying sed / regex / string-replacement patches, writing multi-edit patch scripts, or checking file encoding and line endings. Covers bottom-up edit ordering, Unicode-safe binary-mode patching, transactional multi-edit scripts, LF/ASCII encoding gates, platform-neutral patterns, and shell verification gotchas (grep -c inside && chains). This is the PORTABLE editing discipline; project-specific pre-delivery testing for Paloma's Orrery lives in the agentic-pre-test skill.
fires_when: Editing existing files, patch scripts, sed/regex edits, encoding checks (portable)
---

# Safe File Editing

Skill version: 1.10 | Cut from palomas_orrery @ ccd1ac96 (v1.10),
earlier @ bfa9de2f (v1.9),
earlier @ 6d12ecac (v1.8), d424c459 (v1.7), ef3bd13 (v1.6),
50438c6 (v1.5), a872205 (v1.4), 1ba20c3 (v1.3), 3398970 (v1.2),
bdaaa0c (v1.1) | August 29, 2026, with Anthropic's Claude Opus 5
Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons;
v1.1 adds the delivery-format convention from a same-day incident (a
transactional patch silently never run; see Field Notes). v1.3 adds
Line Endings Are Not Content, earned when a patch aborted twice on a
CRLF working copy whose bytes were identical to the repo's. v1.4 adds
Fix In Passing, Report It, after a patch blocked itself on two Unicode
arrows that predated it by months, and Naming and Archiving a Patch
Script, an unstated convention 96 scripts deep that Tony had been
following alone. v1.5 adds Stamp What You Change (L-220), after Tony
observed that this project updates bodies more reliably than it updates
anchors, dates and module descriptions. v1.6 generalises that section to
every file type, because 1.5's only concrete example was a Python module
docstring and the rule's founding case was stale Markdown headers -- it
would not have fired on the files it was written for. v1.7 adds A Paste
Is An Unverified Transfer (L-223), which extends the delivery rule to
prose, markdown and ledger files -- every example in 1.6 was code, and
this project had been hand-editing a 579 KB ledger on that silence.
v1.8 (L-226) does two things, both from Tony's rulings of 2026-08-23.
It rescopes the Encoding Gate to say PROSE explicitly, because a
session read "delivered code" as excluding markdown and left 23
non-ASCII characters in a file it was already patching. And it adds
The Correction Does Not Travel, one scope out from Stamp What You
Change: that section governs the file the patch is editing, this one
governs the other files quoting the value it just changed.
Portable: applies to any project, not only Paloma's Orrery.

## Bottom-Up Editing [QUALITY]

Edit from bottom to top (highest line numbers first). Each edit can change
line numbers for everything below it; bottom-up keeps every remaining
target's line number valid.

## Unicode-Safe Editing (binary mode) [QUALITY]

Use Python binary mode for files containing Unicode OR requiring specific
line endings. sed can corrupt multi-byte UTF-8 and normalize line endings
silently.

```python
with open(filename, 'rb') as f: content = f.read()
content = content.replace(b'old_text', b'new_text')
with open(filename, 'wb') as f: f.write(content)
```

| Scenario                   | Method                          |
|----------------------------|---------------------------------|
| File has Unicode           | Python binary mode              |
| File needs CRLF preserved  | Python binary mode              |
| Simple ASCII-only files    | sed okay                        |
| Uncertain                  | Python binary mode (always safe)|

## Transactional Patching for Clustered Edits

For a batch of related edits: one script, anchored byte-level replaces,
each asserting EXACTLY ONE match -- all-or-nothing, fails loud on drift.

```python
edits = [(b'anchor_old_1', b'new_1'), (b'anchor_old_2', b'new_2')]
with open(fn, 'rb') as f: content = f.read()
for old, new in edits:
    n = content.count(old)
    assert n == 1, f'expected 1 match, got {n}: {old[:60]!r}'
    content = content.replace(old, new)
with open(fn, 'wb') as f: f.write(content)
```

### Git Is the Backup [QUALITY]

A patch script does NOT write a `.bak`. It prints how to undo instead.

The reason is structural rather than tidy-minded. A patch guards on a
content fingerprint before it writes, and refuses when the working copy
does not match. So at the moment it writes, the file on disk IS the
committed version -- git holds it, and one button restores it. The
`.bak` cannot ever be the only copy. The single case where it would
earn its place, uncommitted work, is precisely the case the fingerprint
gate refuses to run in.

So say this, in the words of the tool the person actually uses:

```
FAILURE: ... NOTHING was written.
Undo is Discard Changes in GitHub Desktop.
```

Not writing them is worth more than deleting them later, because a
stale copy is an ACTIVE HAZARD and not just clutter. A session grepping
for a value can hit one and read it as current; when the nine tracked
backups were swept from the orrery on 2026-08-29, two of them were a
superseded master plan and a superseded skill.

The rate is days. All eight backups swept from the gallery on
2026-08-31 were created in the preceding two days.

**And `*.bak` does not mean what it looks like.** The glob matches a
name ENDING in `.bak`, so `page.html.bak` is silently ignored and sits
on disk unseen, while `page.html.bak2` and `page.html.bak_L271` are NOT
matched and get committed. Any ignore rule for this needs all three
shapes:

```
*.bak
*.bak[0-9]
*.bak_*
```

**A rotating runtime backup is a different thing and is fine.**
`close_approach_data.py` keeps two generations of its cache, bounded at
two, rebuilt by the program that owns it. That is a program managing its
own data, not a patch hedging against itself. Keep it out of the
repository all the same: git already holds the previous cache.

(Tony's question, 2026-08-31: "why do we create them at all?" He also
believed the maintenance runner cleaned them up. It does not -- the word
does not appear in it. What existed was one manual sweep, which is how
a habit gets mistaken for a mechanism. L-271.)

### Line Endings Are Not Content [QUALITY]

A patch harness has to answer two questions, and they are different:
"is this the file I built against" and "does this anchor still exist."
Line endings can change the first answer while leaving the second true.

**Fingerprint the content, not the raw bytes.** Normalize before hashing:

```python
fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
```

A Windows working copy can hold CRLF where the repo holds LF. With
`.gitattributes` set to `* text=auto eol=lf`, git normalizes on commit
and reports NO change -- correctly, because there is none. A raw-byte
fingerprint calls that "BASE MOVED" and sends everyone hunting for an
edit that was never made. The delta is exactly one byte per line, which
is the tell: compare sizes before assuming content drift.

**Translate anchors to the file's own convention.** Anchors are written
LF; a CRLF file matches none of them and the patch aborts on a file it
could have edited safely. Detect per file and convert both sides:

```python
is_crlf = data.count(b'\r\n') > 0
if is_crlf:
    old = old.replace(b'\n', b'\r\n')
    new = new.replace(b'\n', b'\r\n')
```

Preserve what the file already uses rather than converting it. The patch
is there to make one change, not to also silently restyle 11,000 lines.

**Files in one repo can disagree.** Do not detect once and apply the
answer everywhere. In the case that produced this note, four files were
LF and one was CRLF in the same working directory -- something had
rewritten that one file in text mode, which is precisely what the
binary-mode rule above exists to prevent.

The assert is the point: a zero-match replace "succeeds" silently and the
edit never lands. Agentic string matching can silently fail when the target
text was reworded in an earlier session -- variables get added to the
functions that read them but never created where they are defined. Always
verify the new symbol exists at its definition site, not just at its uses.

## Delivery Format -- Runnable by Tony, Not Just Reviewable [CRITICAL]

A patch that only Claude knows how to run is not delivered, it's described.
Every patch-style deliverable states its own exact run command, in the
deliverable itself, every time -- never assume a prior session's
explanation still applies.

**Format A -- transactional Python script (default; prefer this).**
Matches "Transactional Patching for Clustered Edits" above. Tony's steps:
save the file into the same folder as the file(s) it edits, open in VS
Code, click Run. The module docstring MUST state the run command
explicitly (`python <scriptname>.py`) so the file is self-contained even
outside this conversation.
- Success: one `ok` line per edit, then `patch applied (N bytes)`.
- Failure: a single `ERROR:` (bad base) or `ANCHOR FAIL` (a specific edit's
  text wasn't found) line -- nothing is written either way, always safe to
  re-check and retry.

**Format B -- raw unified diff (`.patch` file).** Use only when Format A
doesn't fit (e.g. matching an external AI's own diff output). Tony's exact
command, stated every time a `.patch` file is delivered:
```
git apply <path-to-file>.patch
```
run from a terminal with the working directory set to the repo root the
patch targets (or the correct subfolder, e.g. `tools\`, if the diff's
paths are relative to one).

### Naming and Archiving a Patch Script [QUALITY]

A patch script is disposable and its record is permanent. Both facts
are carried by where it ends up, not by anyone remembering.

**Name it `patch_<handle>_<what>.py`**, leading with the ledger handle
that authorized it -- `patch_L189_run_history.py`,
`patch_F1_active_path_gate.py`. A name describing only what the script
does ("normalize_continuations_stage1.py") reads fine on the day and
is unattributable a year later.

**Number a sequence.** Where several patches must run in order, the
order lives nowhere but their fingerprints -- each is built against the
tree the last one produced, so running them out of order aborts safely
but tells nobody what the right order was. Put it in the filename:
`patch_L196_1_continuations`, `_2_chromosphere`, `_3_key_retirement`.
Sort order is then run order.

**Archive to `documentation/` once it has run**, never the repo root.
It is one-shot by construction -- the fingerprint it guards on describes
a tree that stopped existing the moment it succeeded, so a second run
aborts and writes nothing. Keeping it is for the record, not for reuse.

**Say which parts are permanent.** A disposable script routinely
installs lasting capability -- a new function, a new file grammar, a new
data record. The script is thrown away; those are not. State the split
when delivering, or the permanent half gets archived mentally along
with the script.

(Tony's ruling, 2026-08-16. The convention was already 96 scripts deep
in `documentation/` and written down nowhere, so a session that read
the delivery format above still produced three unprefixed scripts and
had to be told.)

**Standing: the VS Code Run button is the preferred path where practical;
a terminal step is a fallback, not forbidden** (Tony, 2026-08-05,
resolving the conflict Fable flagged between this section and the resident
protocol's WHO TONY IS). So prefer a runnable .py patch script over a
.patch file when both would work. When a terminal step genuinely is the
better tool, give the exact command and say what success and failure look
like -- which is what the two bullets below do.
- Success: **silence** -- `git apply` prints nothing when it works. This is
  the opposite signal from Format A; say so explicitly when handing over a
  `.patch` file, since silent success reads as "did nothing" otherwise.
- Failure: an explicit `error:` line (e.g. "patch does not apply") --
  nothing is written.

**Multiple patches touching the same target file, delivered together:**
confirm each one individually -- request or read the actual run output for
EVERY file, not just the last one. A later, unrelated success (a passing
test suite, a clean compile) does not confirm an earlier patch actually
executed; each deliverable needs its own confirmed evidence.


### A Paste Is An Unverified Transfer [QUALITY]

The delivery rule above covers PROSE too -- markdown, documentation,
the ledger. An edit to any version-controlled file is delivered as a
patch script, not as text for Tony to paste into an editor.

The reason is not that any editor is buggy. It is what a paste is.

Text on a clipboard passes through several participants -- the source
application, the OS clipboard, the editor's own paste handling, the
buffer, the save. Not one of them owns reporting the outcome. Nothing
anywhere compares what arrived against what was sent. So a paste that
silently dropped and a paste that landed perfectly produce the same
evidence, which is none. That is true on a good day; a slow or failed
paste only makes the property briefly visible.

A patch script has the opposite shape. The text is already inside the
file when it reaches the machine, having travelled as a file rather
than through the clipboard. The script opens the target, writes bytes
through one synchronous call that either returns or raises, and then
prints what it changed. Success carries evidence.

So: **a document edit is a patch, the same as a code edit.** Anchor on
structure rather than on exact line wrapping when the target is prose
that may have been reflowed -- find the heading, find the next
heading, work between them -- and require every anchor to match
exactly once.

WHEN A HAND EDIT IS UNAVOIDABLE, the human check is to watch until the
text actually appears before clicking or typing anything else, and to
NOT retry on silence. Retrying is the natural response to a paste that
seems not to have happened, and it is how one pending transfer becomes
two. Name this for what it is: a person looking, standing in for a
check the tooling does not perform. It works, and it holds right up
until the session where someone is tired or moving fast. That is the
argument for the patch being the default rather than the fallback.

(Origin: L-223, 2026-08-21. A paste into LEDGER_CONSOLIDATED.md
appeared to do nothing several times, then completed about a minute
later. Tony caught it only because he was comparing the paste against
the copy -- which is this project's own confirming question, asked of
a text editor.)

## Encoding Gate [QUALITY]

LF line endings. ASCII only -- no emoji, arrows, degree signs, or
checkmarks (Windows cp1252 consoles mangle them).

**This covers PROSE, not only code.** Markdown, documentation, plans,
handoffs and the ledger are all in scope, on the same terms as a .py
file. Earlier wordings said "delivered code", and that phrasing was
read as putting markdown outside the gate.

```bash
grep -P '[^\x00-\x7F]' filename.py   # Find non-ASCII (should be empty)
file filename.py                      # Check line endings
```

(Tony's ruling, 2026-08-23. A patch revising a master plan found 22
PRIME characters and one DOUBLE PRIME in an architecture name,
reported them, and declined to sweep them -- reasoning that the gate
was scoped to code and that prose typography needed a ruling rather
than a sweep. All three Fix In Passing conditions held, and the patch
was holding the fingerprint and the all-or-nothing harness at that
exact moment. Tony: when touching a file, incidental non-ASCII gets
fixed. Note that Stamp What You Change already said markdown is not an
exception -- so the skill's two halves disagreed, and the reader
followed the narrower one.)

### Fix In Passing, Report It [QUALITY]

When a patch is already fingerprinting a file and finds a violation of
an ALREADY-RULED convention in it -- non-ASCII bytes, CRLF where the
repo is LF -- fix it in the same patch and say so in the output. Do not
note it and move on.

The reasoning is about what actually gets scheduled. A dedicated sweep
for two characters is costly and low priority, so "recorded for later"
means never. Meanwhile the patch already holds the two things that make
the fix safe: a fingerprint proving the file is the expected one, and an
all-or-nothing harness. Those conditions will not recur more cheaply
than right now.

This is NOT a licence for scope creep. It applies only where all three
hold:
- the convention is already ruled, not a judgment call being made on
  the spot;
- the file is already being edited by this patch, not opened for the
  purpose;
- the fix is mechanical, with no reading of intent.

A design change, a refactor, or anything needing a decision stays out
of scope and goes to the person. "Fix only what asked" governs DESIGN.
It was never meant to preserve a ruled violation in a file you are
already holding open.

**Scope the gate to what the patch INTRODUCES, then sweep what it can
reach.** A gate that fails the whole run because the file already held a
violation blocks a correct patch over somebody else's bug. A gate that
stays silent about it is how a convention quietly stops being true. So:
hard-fail on non-ASCII in inserted lines, fix pre-existing violations
where the three conditions hold, and print which of the two happened.

Report both outcomes explicitly, because they are different facts:

```
note: <file> had N non-ASCII byte(s); normalized to ASCII in passing
note: <file> still holds N non-ASCII byte(s) this patch did not reach
```

The second line is the one that matters. A patch that fixes some and
not all must say which, or the next session reads a clean run as a
clean file.

**The patch script's own bytes are also in scope.** A script that
repairs a Unicode character has to CARRY that character to match on it.
Write it escaped (a `\uXXXX` literal) so the deliverable stays ASCII and
does not fail the gate it exists to enforce.

### Stamp What You Change [QUALITY]

A patch that edits a file also updates that file's own currency block,
in the SAME transaction as the body. THIS APPLIES TO EVERY FILE TYPE.
Markdown is not an exception -- it is where the rule was earned.

The currency block is whatever the file carries to say what it is and
when it was last true:

| File | Currency block |
|---|---|
| `.py` module | docstring: the `Module updated: <date> with <model>` line, and the description of what the module does |
| `SKILL.md` | the `Skill version:` line, its cut-from SHA list, the date, and the `vN.M adds...` paragraph |
| plan, handoff, review prompt, manifest | the `Built on <SHA> at <URL>` line and the status or "last updated" line |
| the protocol | its header anchor and version |
| ledger, atlas, any generated file | the header stamp, where one exists and is hand-maintained |

Where the change alters what the file DOES, the description at the top
moves with it -- a module docstring and a master plan's status line do
the same job and go stale the same way.

**Why this is worth the bump it costs** (Tony, 2026-08-20): the
documentation is what keeps the conversation targeted, clear and
trackable. Every session starts cold and reads these headers to work out
what it is looking at. A stale one does not merely misinform -- it costs
the next session the orientation the document exists to give, and the
error compounds because the next session writes its own documents on top
of that misreading.

The stamp names the model that made the change, e.g. "with Anthropic's
Claude Opus 5". Attribution is a partnership value here, and it is also
provenance: a reader can tell whether a human or a model last touched
the header, which matters most when the header is the thing being
trusted.

The patch PRINTS which stamps it updated, so the operator sees it
happened rather than trusting that it did.

**Why it belongs in the patch and nowhere else.** Nobody schedules a
separate pass to re-stamp headers, so a body-only edit leaves the file
describing a state that no longer exists, permanently. The patch is
already fingerprinting the file and already knows the anchor it was
built on. That is the only moment where the stamp is free and correct.
Same reasoning as Fix In Passing, Report It, one field over: the file is
open, the obligation is adjacent, and a separate sweep for it would
never be scheduled.

**The module description is the highest-stakes half.** A stale date
makes a file look older than it is, which is recoverable. A stale
DESCRIPTION misdirects a reader about what the file does -- and in this
project it propagates: `module_atlas.py` builds MODULE_ATLAS.md and
MODULE_INDEX.md from each module's own docstring, and the atlas says so
in its own header ("the source of truth is each module's own docstring
... do not hand-edit it"). So a description left stale after a
behaviour change is not one wrong line; it is a wrong line reproduced
into a generated document that presents itself as current.

(Origin: Tony's rule, 2026-08-20, from the observation that this project
"tends to update the body more than the anchors" -- master plan headers,
module histories and dates drift while their bodies stay current. The
alternative considered and rejected was a generated currency stamp
rebuilt by the maintenance run. It was rejected because it needs its own
generator to maintain, while a stamp written by the patch that caused
the staleness cannot drift: there is no second step to forget.)

### The Correction Does Not Travel [QUALITY]

One scope out from Stamp What You Change. That section governs the
file the patch is editing. This one governs the OTHER files that
quote the value the patch just changed.

**When you correct a value, a name, or a status in code, the prose
describing it does not follow. Nobody is assigned to carry it.**

The asymmetry is what makes this dangerous rather than merely untidy.
A wrong value in code tends to surface -- something renders oddly, a
test pins it, a checker reads it. A wrong value in a document that
DESCRIBES the code surfaces only when a human reads that sentence and
happens to know better. So the document version outlives the code
version, and it is the one a future session reads first.

So when a patch changes any of the following, ask what QUOTES it:
- a numeric value with a source (the documents citing that source)
- a constant's NAME (anything that told a reader to grep for it)
- an item's STATUS (plans and summaries describing it as open)
- a file's location or name (every pointer to it)

Three moves, in the order they are usually available:
- **Fix it in the same patch** where the quoting file is already a
  target. Cheapest, and the only version with no second step.
- **Name the quoting file in the patch's own output** where it is
  not. "constants_new.py now reads 15; MASTER_PLAN_CRITICAL_PATH_
  SUMMARY.md still says 17" is a line somebody can act on. Silence
  is not.
- **Record the correction VISIBLY when you do fix it**, rather than
  swapping the digit. A document that silently rewrites its own past
  stops being evidence of anything, and the next reader has nothing
  to check it against.

The confirming question is the project's own, pointed sideways:
WHAT ELSE SAYS THIS? If the answer is "nothing" without having
looked, that is not an answer.

(Origin, 2026-08-23. `constants_new.py` had read 15 R_sun since
2026-08-22, when L-209 corrected DeForest, Howard and McComas (2014)
at source -- the paper's arXiv abstract page disagrees with the
accepted manuscript arXiv itself serves, and two earlier reads had
both quoted the listing page. `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`
still said 17 the next day, INSIDE the paragraph that file had
written to correct an earlier wrong claim about the same row, in a
document whose own text argues that a wrong claim in a summary
outlives the conversation it came from. The same file named
`STREAMER_BELT_RADII`, which L-224 had renamed the day before, and
called L-214 "designed and unbuilt, and the next scheduled work"
two days after L-214 went DONE. Three instances, one file, one
cause. The provenance machinery watches the code; nothing watched
whether the documents describing the code kept up.)

## Compare Content, Not Bytes [QUALITY]

A guard, a diff or a reachability check that compares RAW BYTES
across a Windows working copy will refuse or cry wolf on files
nobody has changed. Compare the LF-normalised content instead, and
write each file back in the line-ending style you found it in.

```python
raw = open(path, "rb").read()
was_crlf = b"\r\n" in raw
content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
actual = hashlib.md5(content).hexdigest()      # guard on THIS
...
final = out.replace(b"\n", b"\r\n") if was_crlf else out
```

**Why the two copies legitimately differ.** Any tool that writes in
TEXT mode on Windows -- `open(path, 'w')` -- turns every \n into
\r\n. Git normalises it back on commit, especially under a
`* text=auto eol=lf` .gitattributes. So the repository holds LF, a
static host serves LF, and the working copy holds CRLF, with not
one character different between them. Nobody did anything wrong and
the byte comparison is simply asking the wrong question.

**Say when normalisation was what saved it.** Print `[CRLF]` beside
a guard that matched only after normalising, and say "matches (the
working copy is CRLF)" on a row rather than a bare match. Silently
swallowing the difference trades a false alarm for a blind spot,
which is the worse of the two.

**Preserve the style on write.** Flipping a 700 KB file's line
endings shows in a git GUI as every line changed, which buries the
eight edits that actually matter. This half is not cosmetic: a diff
nobody can read is a diff nobody reviews.

**[QUALITY] rather than [CRITICAL], deliberately.** Both failure
directions are LOUD -- a guard refuses, or a check reports stale --
so nothing is silently corrupted and nothing passes that should
not. What it costs is trust in the check, which is why it is worth
a section at all. The critical tier stays short.

(Two instances, one day, August 29 2026. A four-file patch refused
to run because `ledger_index.py` had left LEDGER_CONSOLIDATED.md
CRLF in the working copy; the md5 was reproduced exactly by
converting the repo copy, proving not one character differed. Then
the gallery maintenance runner reported two served files stale on
every live run, because `gallery_cache_builder.py` writes
coverage_index.json and feature_configs.json in text mode. The
second is the lesson: the first had already been diagnosed and
fixed in the patch scripts hours earlier, and was not carried to
the runner that had already been written. One producer, two
consumers, one of them moved -- Check All Parallel Pipelines, and
L-182's shape. L-236.)

## grep -c in && Chains [QUALITY]

grep -c exits NON-ZERO when the count is 0 (its "found nothing" signal),
which silently BREAKS an && chain: the downstream command never runs while
the terminal output still looks complete. Never put grep -c mid-chain with
&&. Run verification greps standalone, or join with ; instead.
(Caught June 10, 2026 -- a residual check did not execute until re-run
standalone.)

## Platform Neutrality [QUALITY]

Goal: code runs equally on Windows, macOS, and Linux. When touching a file,
watch for platform-specific patterns and FLAG them (fix if in scope, note
in the handoff if not):
- OS-specific system color names or GUI defaults (Tk system colors).
- Hardcoded path separators -- use pathlib or os.path.join.
- Unicode in print() (cp1252 consoles).
- open() without explicit encoding='utf-8'.
- OS-specific shell-outs.

(The known Paloma's Orrery headliner -- SystemButtonFace in
palomas_orrery.py -- and its test workaround live in the agentic-pre-test
skill.)

## Field Notes

- Python binary mode (rb/wb) preserves line endings and Unicode; sed can
  corrupt multi-byte UTF-8.
- Duplicate code blocks accumulate in iterative sessions: when editing a
  large file across multiple sessions, grep for existing blocks before
  adding new ones (two near-identical mobile override blocks with 95 vs
  100 margins once coexisted in one file).
- Unicode in generated files breaks on Windows -- generate ASCII.
- A bad snippet is a localized error; a complete file from a stale base is
  destructive. When unsure of the base, deliver a snippet.
- Confirm each delivered patch individually, not by batch. One session
  delivered a transactional script alongside several unrelated `.patch`
  files in the same reply; the script was never actually run, but a later
  test suite passing (confirming only the *other* files) was mistakenly
  read as covering it too. A scanner re-run caught the gap. Get the actual
  execution output for every file delivered, not just the last one.
  (2026-07-29)
- `grep -c 'a\|b\|c'` confirms something matched, not which pattern did.
  Verifying three distinct claims in one combined call read as confirming
  all three when only one had actually landed. Check each anchor
  separately when verifying multiple distinct claims. (2026-07-29)
- **A fingerprint mismatch is evidence of difference, not evidence of
  editing.** A patch aborted with BASE MOVED and the diagnosis offered
  was "your working copy has unpushed edits" -- stated as fact, inferred
  from comparing the working copy against repo bytes without checking
  what kind of difference it was. It was CRLF versus LF, content
  identical, nothing edited. The check was right to fire and the reading
  of it was wrong. When a fingerprint fails, establish WHAT differs
  before saying WHY. (2026-08-07)
- **A pre-existing violation found mid-patch gets fixed, not noted.** A
  patch touching eight files hit its own ASCII gate on two Unicode
  arrows in a comment that predated the work by months. The first
  instinct was to report and leave it, citing "fix only what asked."
  Tony's ruling: the convention was already ruled, the file was already
  fingerprinted, and a separate sweep for two characters would never be
  scheduled -- so fix it in passing and report it. The anti-pattern
  "fix only what asked" guards against is unreviewed DESIGN change, not
  mechanical compliance with a standing rule. (2026-08-16)
- **Build patch anchors from the file, not from memory of the file.** An
  anchor included trailing context typed from recall; the actual next
  line was a different `# Source:` comment entirely, so the anchor
  matched zero times and the harness refused. This is the harness
  working, but it costs a round trip. Read the exact bytes at the edit
  site first, and prefer a short unique anchor over a long guessed one.
  Where a block genuinely appears twice and both copies get the same
  replacement, one edit with an explicit expected count of 2 is safer
  than two long anchors distinguished only by distant context.
  (2026-08-07)
