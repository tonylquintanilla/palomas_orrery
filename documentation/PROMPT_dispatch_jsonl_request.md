# PROMPT -- what to paste with a JSONL cross-check request

**Built on `eae95f5a119906968634d57a9fab8964e815466e` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Lands in `documentation/worksheets/`, where the other prompt files
live. The checker scans that directory and recognises a `PROMPT_`
name, so it is categorised as a prompt file rather than counted as an
uncited worksheet.

Reusable. Paste the block below into a fresh chat, attach the
`REQUEST_*.jsonl` file, send nothing else. It carries no batch name,
no row count and no model name, so the same text serves every
responder and every batch.

---

## What is deliberately NOT in it

**It does not say what to do when you cannot determine an answer.**
That silence is load-bearing, not an oversight. UNKNOWN was designed
and held on 2026-08-18 pending evidence, and the pre-registered
trigger counts returned rows where a responder reached for
`unverified` beside a note describing a search they actually
performed, or hedged with a token outside the vocabulary. A prompt
that told them what to do in that case would manufacture exactly the
evidence the trigger looks for, and the count would prove nothing.
See `documentation/DESIGN_20260818_unknown_verdict.md`.

**It does not restate the verdict vocabulary.** The header record
carries it, generated from the checker's own registry. A prompt that
retyped the words would be a second store free to drift from the
first.

**It does not name the expected dispositions or the trap rows.** For
obvious reasons.

---

## The prompt

```
You are performing an independent verification of scientific constants
used in an astronomy visualization project. Attached is a JSON Lines
file: one JSON object per line.

The FIRST line is a header. Read it before anything else -- it carries
the instructions, the answer fields, the verdict vocabulary, and how
rows are identified. Every line after it is a row to answer.

WHAT TO DO

Fill the answer fields named in the header, in place, on every row.
Return all rows, in the order they arrived, including any you could
not complete.

Do not edit the key, claim, code value, hash or id on any row. Those
identify the row and the checker verifies them; a row whose hash no
longer matches its content is returned unread.

Use only the verdict words the header lists, one word per verdict
field. A word carrying a qualification -- "yes, but rounded" -- is
read as unclassified, which wastes the row. Put the qualification in
the notes field, where it is read by a person.

HOW TO ANSWER

Give the value the source states, and cite the source specifically
enough that someone else could find the same number: the document, the
edition or year, and the table or section. "IAU" is not a citation.
"IAU 2015 Resolution B3, Table 1" is.

Answer from the authority itself, not from the codebase and not from
this project's repository. The code's own citation is shown to you so
you can judge it, not so you can adopt it.

If your answer rests on your own recollection rather than a document
you actually consulted, say so plainly in the notes. That is useful
information and it is not held against you.

Disagreeing with the code is a normal outcome and often the point. A
value that differs, a citation that names the wrong authority, a
number more precise than its source supports -- these are findings,
and reporting them is the job. Confirming a row you did not actually
check is the one outcome that damages the work, because it is
indistinguishable from a real confirmation and it removes the row from
anyone else's attention.

HOW TO RETURN IT

One fenced code block, containing only the JSON Lines file and nothing
else -- no commentary inside the fence, no markdown around the
records. Keep the header line at the top so the returned file still
says what it was built from. Anything you want to tell me that does
not fit a notes field goes outside the fence, after the block.
```

---

## After the return lands

Save the block verbatim as `documentation/worksheets/<name>.jsonl`,
where `<name>` is what the annotation will cite. Then run
`worksheet_checker.py` before reading the content: an unparseable
return, a modified hash or a missing row is worth knowing before any
time goes into judging answers.

Record the date the model ran, not the date you filed it. Nothing in
the loop carries that date -- it exists only in the `# Cross-checked:`
annotation, because a person typed it there.

---

Written August 18, 2026 with Anthropic's Claude Opus 5.
