---
name: safe-file-editing
description: Safe practices for editing and patching existing source files, in any project. Use whenever editing existing code files (especially .py), delivering line-targeted snippets, applying sed / regex / string-replacement patches, writing multi-edit patch scripts, or checking file encoding and line endings. Covers bottom-up edit ordering, Unicode-safe binary-mode patching, transactional multi-edit scripts, LF/ASCII encoding gates, platform-neutral patterns, and shell verification gotchas (grep -c inside && chains). This is the PORTABLE editing discipline; project-specific pre-delivery testing for Paloma's Orrery lives in the agentic-pre-test skill.
fires_when: Editing existing files, patch scripts, sed/regex edits, encoding checks (portable)
---

# Safe File Editing

Skill version: 1.5 | Cut from palomas_orrery @ 50438c6 (v1.5), earlier @
a872205 (v1.4), 1ba20c3 (v1.3), 3398970 (v1.2), bdaaa0c (v1.1)
| August 20, 2026, with Anthropic's Claude Opus 5
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
anchors, dates and module descriptions.
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


## Encoding Gate [QUALITY]

LF line endings. ASCII only in delivered code -- no emoji, arrows, degree
signs, or checkmarks (Windows cp1252 consoles mangle them).

```bash
grep -P '[^\x00-\x7F]' filename.py   # Find non-ASCII (should be empty)
file filename.py                      # Check line endings
```

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
in the SAME transaction as the body. Whichever of these the file
carries: the version line, the anchor SHA, the history or changelog
paragraph, the date, and -- where the change alters what the file DOES
-- the module description at the top.

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
