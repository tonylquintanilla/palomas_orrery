---
name: safe-file-editing
description: Safe practices for editing and patching existing source files, in any project. Use whenever editing existing code files (especially .py), delivering line-targeted snippets, applying sed / regex / string-replacement patches, writing multi-edit patch scripts, or checking file encoding and line endings. Covers bottom-up edit ordering, Unicode-safe binary-mode patching, transactional multi-edit scripts, LF/ASCII encoding gates, platform-neutral patterns, and shell verification gotchas (grep -c inside && chains). This is the PORTABLE editing discipline; project-specific pre-delivery testing for Paloma's Orrery lives in the agentic-pre-test skill.
---

# Safe File Editing

Skill version: 1.0 | Cut from palomas_orrery @ b29ad3f8 | July 1, 2026
Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons.
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

The assert is the point: a zero-match replace "succeeds" silently and the
edit never lands. Agentic string matching can silently fail when the target
text was reworded in an earlier session -- variables get added to the
functions that read them but never created where they are defined. Always
verify the new symbol exists at its definition site, not just at its uses.

## File Encoding Gate [QUALITY]

LF line endings. ASCII only in delivered code -- no emoji, arrows, degree
signs, or checkmarks (Windows cp1252 consoles mangle them).

```bash
grep -P '[^\x00-\x7F]' filename.py   # Find non-ASCII (should be empty)
file filename.py                      # Check line endings
```

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
