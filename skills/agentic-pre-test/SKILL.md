---
name: agentic-pre-test
description: Pre-delivery runtime test protocol for Paloma's Orrery Python deliverables. Use BEFORE delivering any complete file or agentic code in the Paloma's Orrery project, and after ANY data-content sweep (hover strings, legendgroup wiring, marker styling). Trigger words in an orrery coding task include "complete file", "agentic", "sweep", "deliver", "generate the module". Covers py_compile, the xvfb headless GUI run, the throwaway-copy rule, and the live-dispatch smoke test. The resident protocol also carries a one-line pointer to this skill; if you are about to hand Tony a complete orrery file and this skill has not loaded, load it.
fires_when: BEFORE delivering complete files/agentic code; after data-content sweeps
---

# Agentic Pre-Test Protocol [CRITICAL]

Skill version: 1.3 | 2026-10-06, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 51436054. v1.3 (L-027) drops the colour swap from the
Standard Test. palomas_orrery.py now names its panel colour once,
PANEL_BG = 'gray90', which Tk knows on every system, so the headless
run needs no edit to the copy, and it now fails if a Windows-only
colour name comes back. The throwaway rule stays, with its true
founding case.
Earlier: 1.2 | Cut from palomas_orrery @ 3398970 | 2026-08-05
Source: project_instructions_v3_29.md Part 3 (Agentic Pre-Test Protocol).
Run before delivery. Catches runtime errors Tony would otherwise hit.
Division of labor: Claude covers Syntax + Runtime; Tony covers Visual +
Windows-specific.

## The Standard Test

Setup (once per sandbox): `apt-get install -y python3-tk xvfb`

```bash
python3 -m py_compile palomas_orrery.py
cp palomas_orrery.py _pretest_throwaway.py
timeout 30 xvfb-run -a python3 _pretest_throwaway.py 2>&1 | head -50
rm _pretest_throwaway.py
```

The copy is run as it is, with no edit. The orrery is cross-platform
(Tony, 2026-10-06: "We should not have any windows only
requirements."), so if this run stops with `unknown color name`, or
with any error naming something only one system has, that is a
finding in the deliverable. Fix it there and report it. Never edit
the copy to get past such an error: that turns a check that found the
bug into one that cannot.

## [CRITICAL] The pre-test never edits the deliverable

Anything a test changes in code to make it run headless (a mainloop
patched to a no-op, a network call stubbed) is changed on a throwaway
copy, and the copy is discarded. Never undo a test change in place on
the deliverable: an undo cannot tell the values the test put there
from the ones that were there already.

The founding case, as the file history shows it (corrected
2026-10-06, L-027). Tony's commit dff2d03 of 2026-01-09,
"cross-platform refactor", replaced every SystemButtonFace in
palomas_orrery.py with gray90, and he tested the orrery on Linux and
macOS while it held. The pre-test swapped SystemButtonFace to gray90
on a copy so the file would run headless, and swapping back
afterwards, in place, was the known risk: on 2026-06-09 L-003
recorded the rule against it. On 2026-06-12 commit ec333df, "animation
refactor phase 4", changed all 26 gray90 in the file to
SystemButtonFace: exactly that restore, on the real file. From then on
the damaged file was read as the original. L-027 opened on 2026-06-18
calling SystemButtonFace the starting state, and this skill at 1.1
(L-115, 2026-07-12) rewrote this paragraph to fit the damaged file.
The orrery could not open its window on Linux for four
months.

The swap also hid the bug. Every headless run passed, because the
test removed from the copy the one thing that stopped Linux. A test
workaround that edits the thing under test can leave the test unable
to fail on exactly what it edited -- the resident gate A Check That
Cannot Fail Is Not Passing, from the other side.

Since L-027 the colour is one name, PANEL_BG = 'gray90', defined just
after the root window, so no swap is needed and a future one would
have a single line to change.

## Data-Content Sweeps Need a Live-Dispatch Smoke Test

When a sweep changes output DATA (hover strings, legendgroup wiring,
marker styling) rather than control flow, py_compile is not enough -- an
untouched file compiles as cleanly as a correct one, and a container test
of the wrong path passes falsely.

The standard method: exec the WHOLE module under xvfb with the tk mainloop
monkey-patched to a no-op, so the test runs in the real module namespace
with real tk vars and real builders (network patched), and exercises the
path that actually runs. Then CONSTRUCT the traces and INSPECT the output
on the LIVE dispatch, not the per-body builder functions. A function the
live code never calls then shows up as never-called -- the dead-code trap a
per-function container test misses.

Live-path fact: build_sphere_shell via SHELL_CONFIGS is the live sphere
shell path; the inline marker dicts in *_visualization_shells.py are dead
code for sphere shells (custom geometry routes via CUSTOM_SHELLS and does
use the inline path). See orrery-coding-conventions for the full dispatch
map, and the resident Verify Execution gate for the principle.

## When This Protocol Is Required

- Any Mode 2 (agentic) deliverable: complete files, new modules.
- Any data-content sweep, even delivered as snippets, when the changed
  data can be smoke-tested.
- After bulk/scripted edits (transactional patches), before handoff.

Not required for: single Mode 1 line snippets Tony will apply and render
himself (the render is the gate there), pure documentation, design
sessions.
Gallery-repo builder deliverables have their own layered gate (offline
suite + live dry-run + schedule) -- see the gallery-cache-builder skill and
documentation/TESTING_PROTOCOL.md, not this protocol.

## Deferred Pipelines

When deferring a pipeline patch, smoke-test the DEFERRED pipeline too --
confirm it is in a KNOWN state, not just that it does not error.

## Field Notes

- xvfb-run enables headless GUI testing of tkinter apps in the sandbox.
- Handoffs are claims; runtime output is fact. When a smoke test
  contradicts a handoff, the smoke test wins and the handoff gets
  corrected.
- Testing iterates in dependency order: regression gate, then features,
  then animation. Some bugs are only findable in later rounds (the
  Sun-checkbox-off bug needed Round 3). A three-round fix is fine when
  each round teaches something new.
- ASCII/LF check is part of the delivery gate: run the encoding greps
  from the safe-file-editing skill on every deliverable.
