<!-- Doc-Kind: hand | Relay note from the decisions session of 2026-10-08 to the split session (L-418) running in parallel. One approved paragraph to carry. -->
# Note for the split session (L-418): the section 4 ruling, and one approved paragraph

Built on orrery b0b3df8264958ec9f4a7270f4e4008825452f08d at
https://github.com/tonylquintanilla/palomas_orrery (HEAD at 18:0x CDT,
2026-10-08, unchanged since both sessions started).

From the decisions session of 2026-10-08 (Claude Opus 5.5, Tony on
his phone).

## 1. Your brief's section 4 decision is ruled: as recommended

Tony, 2026-10-08 18:08, on the question in
`documentation/HANDOFF_L418_split_build_brief_20261008.md` section 4:
"As recommended? -- yes". So:

- L-371 (the Sun room's served numbers) and L-390 (the conversion
  marker) ride provenance-discipline 2.27 with the split, as phase-2
  sentence fixes.
- L-414 (the scanner's window and declared rows) waits for its own
  session, which cuts 2.28. That session still comes before the Sun's
  list reaches L-228 (the Alfven surface's ranges), as the Fable sweep
  asked.

No need to ask Tony this again.

## 2. One approved paragraph also rides the split

Tony closed L-252 (an INCOMPLETE verdict is not a
confirmation) and ruled that one paragraph goes into the provenance
skill WITH THE SPLIT, word for word, not as a later bump. Tony: "Concur
with B." and, on the wording, "Approved".

Where it goes: immediately after the send-back rule ("PARTIAL and
APPROX return to the originator for completion", and its "Ask for a
NEW file" paragraph), before "A Complete Row That Disagrees Is a
Finding [CRITICAL]". In 2.26 that is under Review-Repair Protocol for
Cross-Checked Annotations. If the split moves that section into
provenance-cross-check 1.0, the paragraph goes there, beside the
send-back rule. It is a NEW paragraph, so it belongs in the patch's
phase 2, printed as an insertion; the phase-1 byte-identical check runs
before it.

If the split patch is already built and tested without it: do not
rebuild. Say so in the handoff, and it rides the L-414 session's 2.28
instead.

The paragraph, verbatim:

**What the checker reports is a different list** (L-252, Tony,
2026-10-08). `worksheet_checker.py` compares the code against a
worksheet and reports one of four outcomes. They are the checker's
words, not worksheet tokens, and never belong in a verdict cell.

- DRIFTED -- the worksheet confirmed a value and the code left it, or
  called it APPROX or PARTIAL and the code moved somewhere the
  worksheet never named. The only defect of the four; routed to
  conversation.
- CORRECTED -- the worksheet rejected the value and the code moved.
  Recorded, not routed.
- COMPLETED -- the worksheet called it APPROX or PARTIAL and supplied a
  value, and the code now reads exactly that value. Recorded, not
  routed.
- UNCHECKED_MOVE -- the code moved and the worksheet carries no value
  verdict. Routed, because nobody has established anything.

COMPLETED says only that the code took the value the worksheet
supplied. It is not a confirmation. The row is still APPROX or
PARTIAL, it earns no leg toward the cross-checked rung, and the
send-back rule above is unchanged.

(The four definitions match worksheet_checker.py lines ~1381-1393 at
b0b3df82.)

Also for the ledger: the decisions session's records patch closes
L-252 and writes this paragraph onto L-418. The two patches both edit
LEDGER_CONSOLIDATED.md; each anchors only on the lines it edits, so
either may run first.

Written 2026-10-08 with Anthropic's Claude Opus 5.5.
