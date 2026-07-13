---
name: agentic-pre-test
description: Pre-delivery runtime test protocol for Paloma's Orrery Python deliverables. Use BEFORE delivering any complete file or agentic code in the Paloma's Orrery project, and after ANY data-content sweep (hover strings, legendgroup wiring, marker styling). Trigger words in an orrery coding task include "complete file", "agentic", "sweep", "deliver", "generate the module". Covers py_compile, the xvfb headless GUI run, the SystemButtonFace throwaway-copy rule, and the live-dispatch smoke test. The resident protocol also carries a one-line pointer to this skill; if you are about to hand Tony a complete orrery file and this skill has not loaded, load it.
fires_when: BEFORE delivering complete files/agentic code; after data-content sweeps
---

# Agentic Pre-Test Protocol [CRITICAL]

Skill version: 1.1 | Cut from palomas_orrery @ <ORRERY HEAD after push>   ->   e83fe9ce | 2026-07-12
Source: project_instructions_v3_29.md Part 3 (Agentic Pre-Test Protocol).
Run before delivery. Catches runtime errors Tony would otherwise hit.
Division of labor: Claude covers Syntax + Runtime; Tony covers Visual +
Windows-specific.

## The Standard Test

Setup (once per sandbox): `apt-get install -y python3-tk xvfb`

```bash
python3 -m py_compile palomas_orrery.py
cp palomas_orrery.py _pretest_throwaway.py
sed -i "s/SystemButtonFace/gray90/g" _pretest_throwaway.py
timeout 30 xvfb-run -a python3 _pretest_throwaway.py 2>&1 | head -50
rm _pretest_throwaway.py
```

## [CRITICAL] Swap on a THROWAWAY copy; never restore-in-place

The SystemButtonFace<->gray90 sed round trip is NOT idempotent:
palomas_orrery.py contains 26 SystemButtonFace literals and 0 native
gray90, so the test swap yields gray90 literals indistinguishable from
NATIVE gray90 -- which DOES exist in sibling GUI files
(star_visualization_gui.py has 5, earth_system_visualization_gui.py has 3
at the time of writing). A gray90->SystemButtonFace restore therefore
cannot tell converted from legitimate values; run it on the wrong file, or
after the counts drift, and it silently corrupts the deliverable. Test on a
copy, discard the copy; the deliverable is never edited by the pre-test.
(Caught June 9, 2026; practice every session since.)

Background: SystemButtonFace is a Tk color name that resolves on Windows
but not Linux/macOS. The sed swap is a test workaround, not a fix; the
real fix (out of pre-test scope) is a hex literal ('#F0F0F0'), platform
detection, or ttk styling.

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
