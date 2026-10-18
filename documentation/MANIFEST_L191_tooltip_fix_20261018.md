<!-- Doc-Kind: hand | Manifest: the GUI tooltip fix for L-191, what was measured, what changed, how it was tested. -->
# MANIFEST: the GUI's checkbox tooltips show line breaks (L-191)

Built on orrery f80a3ad at https://github.com/tonylquintanilla/palomas_orrery
and gallery 0be187e at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\
Type: BUILD (one line of code, plus records). Companion patch:
`documentation/patch_L191_2_tooltip_br_20261018.py`.
(A first copy named `_1` was saved anchored at f58f69f and could not be
replaced under its name; `_2` is the one that ran. L-351's read-back
rule caught it.)
Written October 18, 2026 with Anthropic's Claude Fable 5.1.

## 1. What Tony saw, and what it was

- Tony, 2026-10-18, hovering the Sun's shell checkboxes in the orrery's
  window: the tooltips show the characters `<br>` instead of line
  breaks. He recalled it as fixed one to two months ago.
- It was diagnosed then and never built. L-191 (display-text
  duplication across the shell modules) recorded the cause on August 7
  and measured 58 affected strings on August 21 and 24. Its first job
  was "confirm by render" and nothing after it moved.
- The cause, read from the code: the tooltip strings (`core_info`,
  `alfven_surface_info` and the rest) are written with Plotly's `<br>`,
  and `CreateToolTip` in `palomas_orrery.py` hands its text to a Tk
  label as given. A Tk label prints what it is given.
- It is not a regression. Every commit of `solar_visualization_shells.py`
  since 2026-08-22 carries `<br>` in those strings. The `<br>` went in
  on 2026-05-25 (commit 97bbfe3).

## 2. Measured at f58f69f (the code is the same at f80a3ad): which tooltips are affected

Every string a GUI tooltip shows, by both paths: the direct
`CreateToolTip(widget, name)` calls in `palomas_orrery.py`, and the
names `build_shell_checkboxes` (celestial_objects.py) builds at run
time from `SHELL_DEFINITIONS`. Each name resolved to its definition in
the source and read as a raw slice, not evaluated (the August lesson:
an evaluator skips f-strings silently).

122 tooltip strings examined. 58 carry `<br>`, and no other tag:

| Body | Strings | Path |
|---|---|---|
| Sun | 19 | direct calls, `solar_visualization_shells.py` |
| Jupiter | 10 | run time |
| Saturn | 10 | run time |
| Uranus | 8 | run time |
| Neptune | 8 | run time |
| Planet 9 | 2 | run time |
| Moon | 1 | run time |

Clean: Earth (its 11 are written with newlines), the asteroid belt,
the object checkboxes (their text comes from `INFO` in
info_dictionary.py, whose five `<br>` entries are star classes no
checkbox shows), and the two tooltips in `orbital_param_viz.py`, which
has its own copy of the class. The August count of 58 reproduces
exactly.

## 3. What changed

One line in `CreateToolTip.showtip` (`palomas_orrery.py`): the label's
text is `self.text.replace('<br>', '\n')`. A string written with `<br>`
now reads as lines in the GUI; a string written with newlines is
unchanged. All 58 at once; no string touched; the plots cannot change,
because the plots never read this class.

This is the reverse of the canonical direction (orrery-coding-
conventions, Canonical Text Format: write in newlines, derive `<br>`
for Plotly). It is a backstop at the Tk boundary, not a licence to
write in `<br>`. The structural fix stays owed per slice (section 5).

## 4. How it was checked

- The patched `palomas_orrery.py` compiles (py_compile, Python 3.13).
- The tooltip class was exercised under a real Tk display (xvfb,
  Python 3.12): a widget given a three-line `<br>` string shows a label
  whose text holds two newlines and no `<br>`; a newline-authored
  string comes through unchanged. The class source was taken from the
  PATCHED throwaway copy, not retyped.
- The full headless run of the orrery (agentic-pre-test's standard
  test) could not be run here: the sandbox's Tk-bearing Python has none
  of the orrery's dependencies. Tony's own run and look are the gate:
  open the orrery, hover a Sun shell checkbox and a Jupiter one.
- The patch applied on a throwaway copy of the repository at f80a3ad, and
  on Tony's own working copies, which carry the un-pushed L-411 follow-up
  of 2026-10-18 in the ledger:
  every anchor matched once; the ledger index rebuilt with no problems;
  Where We Are stays under its 130-line cap; a second run refused.

## 5. What stays owed (L-191's gap, rewritten)

- (1b) The structural fix, per slice: the Sun's 19 strings in the Sun's
  slice (L-412), written in newlines, their 14 `_info_hover` twins
  deleted, `<br>` derived at the Plotly boundary the way the gas-giant
  configs already do. The gas giants' 36, Planet 9's 2 and the Moon's 1
  when their rooms open.
- (2) Earth, when its talks come: no visible bug, the same duplication,
  and the surface-specific-text case that decides the shape of the fix.
- orrery-coding-conventions' sentence "a tk.Label renders text
  literally, so `<br>` shows up on screen" is out of date after this
  patch; carried on L-351 for the skill's next bump, since a session
  following it would do nothing wrong.

## 6. Tony's steps

1. (do) Run this patch from VS Code (orrery folder).
2. (do) Run the orrery maintenance run from the dashboard: the ledger
   index picks up the dates; expect 31 of 31 gating and the gate at
   0 TIER-1 (the patch types no number).
3. (decide) Open the orrery, hover a Sun shell checkbox and a Jupiter
   one: lines, not `<br>`. Your look is the gate.
4. (do) Move this patch into documentation/; commit; push.

## 7. Skill versions

This session confirmed its loaded copies read ledger-and-session-records
1.21, safe-file-editing 1.13, agentic-pre-test 1.3 and
orrery-coding-conventions 1.10, as the manifest expects. v3.103's
obligation, provenance-discipline 2.31, still travels: no provenance
work fired here.
