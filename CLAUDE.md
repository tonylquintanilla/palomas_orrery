<!-- Doc-Kind: hand | The door into the protocol for a Claude Code session: it points at PROJECT_INSTRUCTIONS.md and the skills, and states what a Code session writes. -->
# Paloma's Orrery: how a Claude Code session works here

This file is the door into the project's rules for a session that runs
in Claude Code. It points; it does not repeat. The rules themselves are
in PROJECT_INSTRUCTIONS.md (the protocol) and in skills/ (the skills).
Added October 26, 2026, by Tony's ruling of that night, on the first
Code session. One store for every rule: if a sentence here disagrees
with the protocol or a skill, the protocol or the skill wins, and this
file gets corrected.

@PROJECT_INSTRUCTIONS.md

## Who you are working for

Tony is in the protocol's Roles section. Read it. He is not a
programmer. He runs Python with VS Code's Run button and uses GitHub
Desktop's buttons for commit and push. Explain any step outside that
in plain words before asking him to do it.

## The skills

They live in this folder at skills/<name>/SKILL.md. The Skill Manifest
in PROJECT_INSTRUCTIONS.md says which skill fires on which work. Read
each one the job fires, in full, before the work, and open your first
report by naming the skills you read and the version line each one
carries. Compare that version with the manifest's row. If they
disagree, stop and say so (the protocol's Stale Skill = Stop gate).

## At the start of a session

1. Read documentation/WHERE_WE_ARE.md. Its "Do next" line names the
   job, and a brief it names (documentation/COORD_*.md) carries the
   details.
2. Record the base: run `git rev-parse HEAD` and `git ls-remote origin
   HEAD`. Both are read-only. If they differ, or `git status` shows
   edits already waiting, say so and stop; Tony's loop is commit and
   push after every session, so the folder should match the remote.
3. Say what you are about to do, in one sentence, and wait for his
   go-ahead.

## What a Code session writes, and what it does not

- You edit the files in this folder directly. There is no patch file
  in a Code session (Tony's ruling, Oct 26, 2026). The change list in
  GitHub Desktop is his review; the records below are his summary.
- Commit and push are Tony's, always. Never run git commit, git push,
  git add, or anything that discards work (reset, checkout, restore,
  clean, stash). The settings file beside this one forbids the
  important ones; this sentence covers the rest.
- Run the tests yourself and read the result. For orrery work that is
  orrery_maintenance_run.py, from this folder; it takes several
  minutes. "All green" is a line you read from its output, never a
  prediction. If a checker fails, fix it or report it; do not close
  the session with it red.
- The gallery repository is the sibling folder
  ..\tonyquintanilla.github.io. An orrery session reads it (the
  maintenance run does) and does not edit it unless the job says so.
- ASCII only, LF line endings: the safe-file-editing skill.

## At the end of a session

- Records per the ledger-and-session-records skill: the ledger item,
  and documentation/WHERE_WE_ARE.md edited section by section. The
  page's "Changed since you last read this" box carries a plain-word
  summary of what changed and why, for Tony, since he does not read
  diffs (his ruling, Oct 26, 2026). Nothing below the page's run-record
  marker is touched.
- The run-record zone below that marker is empty by design. Tony's
  record is his timestamped copy of the page
  (`WHERE_WE_ARE_<m-d-yy>_<hhmm>_run_record.md`), one session per
  copy, and he writes only there (his ruling of Oct 28, 2026). An
  empty zone is not a missing record: read his latest copy instead.
- Your final report lists every file changed with the number of edits,
  the way a patch prints "ok <file> (n edits)", so Tony can paste it
  into his run record; then his run order (what to look at, what to
  commit), then the Tony-action rollup.

## How to report to Tony

Tony reads your reports on his phone, between other things. He
is not a programmer and cannot follow compressed language (the
protocol's Register Rule, Part 2). So every report to him:
- Leads with the claim in one plain sentence; detail after.
- Says the thing, not the name of the thing: a ledger handle
  always carries its short label in parentheses, "L-412 (the
  Sun's slice)", and a file is named with what it is for.
- Puts one question to him per report. A finding, a
  recommendation, an uncertainty and a question are four things;
  send the one that is due and put the rest in the records.
- Ends with the file list for his run record, his run order, and
  the Tony-action rollup, in that order.
Tony, Oct 27, 2026: "Code is difficult to follow and technical."
This section is the answer.
