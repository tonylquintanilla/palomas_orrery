<!-- Doc-Kind: hand | Field manual, one page: which instrument, which model and how much thinking each kind of task in Paloma's Orrery gets. Companion to the protocol's Token Economy (v3.121, L-506). Opened from the dashboard's documents list. -->
# Method, model, effort: which instrument for which task

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | November 2, 2026

Written at orrery fd3551cc and gallery b7ddf775. One page, for quick
inspection from the dashboard. The rule it serves is the protocol's
Token Economy (Part 2, v3.121): spend tokens where they buy
verification or a decision, nowhere else. Tony, Nov 2, 2026: "What
would help would be recommendations regarding model and effort as
well as method meaning snippet, patch or Code for our various actions
and tasks."

## The table

Method first, since it decides the most; then model; then effort
(thinking on or off).

| Task | Method | Model | Effort |
|---|---|---|---|
| Design talk: an open question, rulings, options with tradeoffs | Chat, zero code; a design record at the end | Fable | High (thinking on) |
| Review of a build that came back wrong, or a judgment the files do not settle | Chat, short, from the handoff | Fable | High |
| Coordination: read a report against its brief, write a brief, update Where We Are and the handoff | Chat with the computer linked; records placed as files, sizes read back | Opus | Standard |
| A change with known anchors in one or two files (a symbol, a constant, a workflow line, a sentence) | Patch, tested on a copy, run by Tony | Opus | Standard |
| Records only: ledger items, a protocol or skill bump with no build | Patch (patch_L506_token_economy.py is the shape) | Opus | Standard |
| A build that needs the terminal loop: tests, the maintenance run, the headless walk, a look in the browser, or more than two or three files | Code session, from a brief | Opus | Standard; High for orbital mechanics or provenance |
| A page misbehaving, cause unknown | Code session with the built-in browser | Opus | High |
| A number's independent check, physics or data validation | Mode 7 relay to Gemini or GPT, only for domain uncertainty | Gemini / GPT | n/a |
| Running the daily run, the maintenance run, a patch | Tony's Run button; no model | none | none |

## Three notes that go with it

- A SNIPPET IS FOR UNDERSTANDING (Mode 1), or for a one-line fix Tony
  types himself. Any edit to a versioned file is delivered as a patch,
  by safe-file-editing's own rule (A Paste Is An Unverified Transfer):
  a paste cannot report whether it landed. So the ladder is patch,
  then Code, with "snippet" meaning the explanation beside the patch.
- SONNET AND HAIKU ARE NOT IN THE TABLE on purpose. This project's
  work runs on dense rules, and a cheaper model that misreads them
  costs a correction session, which is dearer than the saving.
- SESSION SHAPE COUNTS AS MUCH AS MODEL. One job per session, closed
  when its handoff or patch is placed. A long session re-reads itself
  at every turn, whatever the model. A skill is read in full when its
  rules govern the work, and in the parts its read plan names when it
  is loaded for its version line or one section.

## What prompted it

Nov 2, 2026: 75 percent of the week's Fable allowance spent in four
days (Tony, 09:37), the morning after a coordinating session on Fable
had written a 176-line brief for a Code session to change one marker
symbol, then dropped it when a patch was asked for. The table is the
answer to the question that followed. It is hand-written reference,
part of the field manual with the protocol and the skills; it changes
when Tony rules a row changed, and the protocol's Token Economy
section points at it.

Written November 2, 2026 with Anthropic's Claude Fable 5.1.
