# Mode 5 test protocol -- Sun exhibit GUI study

**Built on** orrery `70f12a7b5c260288c0fc1a135f45e547651c5d9f` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `80759493dd03f7005eb9c4baae6448756893f884` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote at session start.

**Subject:** `sun_gui_mockup.html` (throwaway study, not a deliverable).
**Type:** Mode 5 acceptance. Tony runs it; it cannot be delegated.
**Written** August 30, 2026 with Anthropic's Claude Opus 5.

---

## What this protocol is for

Two different jobs, and they are kept apart on purpose.

Sections A through F are PASS/FAIL. Each one names the thing that would
make it fail, not just what a pass looks like -- a check whose only
outcome is "nothing looked wrong" cannot fail, and a check that cannot
fail is not passing.

Section G is JUDGMENT. No right answer, no box to tick. These are the
design questions the study exists to settle, and they are yours.

---

## What it does not cover

Say these out loud rather than let a clean run imply more than it earned.

- The streamer belt, the Hills torus, the clumpy outer Oort cloud and the
  galactic tide are drawn as plain spheres at their outer limit. Their
  real shapes are not under test.
- No Pyodide, no assembler, no served cache. The study reads a data table
  generated from `objects_config.json` and draws it directly.
- No provenance checking. The radii and sources were copied out of the
  config by script, not verified against their papers in this session.
- Nothing here tests `interactive.html`. This is a study of a proposed
  shape, not a change to the live page.

---

## Setup

**Desktop.** Open `sun_gui_mockup.html` in a browser. It needs the
internet for Plotly and the fonts.

**Phone.** A local file will not open usefully on the phone, so the file
has to be served. The simplest path in your workflow: drop it at the root
of the gallery repo, commit and push in GitHub Desktop, then open
`tonyquintanilla.github.io/sun_gui_mockup.html`.

That URL is PUBLIC the moment it is pushed, though nothing links to it.
Your call whether that is acceptable for a study file. If it is not,
Section F can run on the desktop browser dragged narrow, which covers
the layout but not touch.

---

## A. Arrival

| # | Do | Passes if | Fails if |
|---|---|---|---|
| A1 | Open the page | The Sun draws; the label at the bottom reads **Outer Corona**; the drawer count reads **9 of 18** | Blank scene, a different count, or the label reads anything else | -- zoom works correctly. hovertext works correctly. clicking the label opens the drawer correctly. the "i" icon opens the hovertext correctly. deselecting the outer corona leaves the alfven surface at the top and the label reselects correctly. snapping back to the gravitational influence snaps correctly to 150,000 au. the "reset camera" button just resets to the standard isometric grid. 
| A2 | Look at all three axis titles | **X (AU)**, **Y (AU)**, **Z (AU)** are each fully readable | Any one is cut off at an edge or missing | -- correct
| A3 | Read the tick numbers | Roughly 4 to 8 gridlines per axis, numbers legible | One or two lonely ticks, or so many they overlap | -- 0.02 au tics are okay but the font size could be one size larger for easier readibility. 
| A4 | Drag to rotate | The Sun stays spherical from every angle | It flattens into an ellipsoid at some rotation | -- the plot stays spherically correct from all perspectives never an ellipsoid

---

## B. The four defects from 2026-08-30

These are regression checks. Each one failed before this pass.

| # | Do | Passes if | Fails if |
|---|---|---|---|
| B1 | Click any cross marker | The frame jumps to that shell and the label changes to its name | Nothing happens |
| B2 | Open the drawer, switch one shell off | The picture updates **immediately** | Nothing changes until you press reset camera on the modebar |
| B3 | Switch off everything above the core | The frame tightens hard onto the core; tick numbers go to thousandths of an AU | The frame stays at about 0.25 AU and the core is a speck |
| B4 | Add back the radiative zone, then the photosphere, then the chromosphere, one at a time | The label changes on **every** one | The label stays on Core |

---

## C. The split: what is drawn vs. where the camera is

This is the design under test. If any of these fails, the two ideas are
not actually separate and the shape is wrong.

| # | Do | Passes if | Fails if |
|---|---|---|---|
| C1 | Tap a cross marker | Label and frame move; the **drawer count does not change** | The drawer count changes |
| C2 | Open the drawer, hover a row, click its small **go** | That shell is focused; **nothing is switched on or off** | The row toggles as well | -- the go button works correctly and moves the camera to that view, but the "go" button should be larger font and move visible, maybe red. 
| C3 | Toggle a row that is not the focused one | The label moves to the outermost thing now drawn | The label sits still |
| C4 | Switch off the shell the label is naming | The label falls back to the outermost thing still drawn | The label empties, keeps a dead name, or the frame jumps somewhere unrelated |
| C5 | Press **All / none** twice | Everything off: label reads *Nothing drawn*, no error, frame stays sane. Everything on: label reads *Gravitational Influence* | An error, a blank page, or a frame that will not come back | -- correct

---

## D. The extremes

The shells span eight orders of magnitude. This is where a framing rule
breaks if it is going to.

| # | Do | Passes if | Fails if |
|---|---|---|---|
| D1 | Focus **Gravitational Influence** | Frame at about 165,000 AU; ticks at 50,000 AU; the Sun is a single point | Ticks unreadable, scene blank, or the modebar reset does nothing | -- reads correctly with tics at 50,000 au each
| D2 | Focus **Core** alone | Frame at about 0.001 AU; the core sphere fills a good part of the view | The yellow centre marker swamps the core, or the frame will not go that tight |
| D3 | Toggle six or seven rows quickly in a row | The picture ends up matching the drawer | The picture ends up on a different frame than the label says |
| D4 | Go straight from Core to Gravitational Influence and back | Both directions land correctly | One direction sticks |

---

## E. The info panel

| # | Do | Passes if | Fails if |
|---|---|---|---|
| E1 | Press **i** | The panel names the same object the label names | It names something else, or the exhibit generally | == correct
| E2 | Leave it open, tap a different marker | The panel follows the new focus | It keeps the old object |
| E3 | Focus the galactic tide, read the panel | It says plainly that the shape is approximated here | It presents the sphere as the real shape |
| E4 | Read the source line on three different shells | Each carries a real citation, and the radius shows km **and** AU | A missing source, or km with no AU |

---

## F. Portrait and the phone

| # | Do | Passes if | Fails if |
|---|---|---|---|
| F1 | Drag the desktop window narrower than it is tall | Axis titles stay fully readable | Any title clips at a corner |
| F2 | Same, look at the Sun | The label pill sits below the Sun, not over it | It covers the object |
| F3 | Open the drawer in portrait | It covers about 60% and scrolls; closing it returns the whole picture | It covers everything, or will not scroll to the eighteenth row |
| F4 | Phone, **landscape** | Usable: Sun clear, label readable, drawer scrolls | Any of those fails |
| F5 | Phone, **portrait** | Same | Same |
| F6 | Phone: tap a cross marker with a finger | It responds to a fingertip | You have to hit it exactly |

---

## G. Judgment -- these are yours, not pass/fail

1. **Does the label earn its place?** It is on screen permanently to say
   one thing. The marker hover and the i panel both also name objects.
   If it does not earn it, the drawer can open from the top bar instead. -- the label works. it clearly identifies the selection. to add to its impact we could highlight the row in the drawer for the selected shell. and when "go"-ing to a new shell, changing the highlight along with the label. 

2. **Does "go" earn its place?** It is a second gesture on every row, and
   two gestures on one row needs explaining. The alternative is that
   tapping a row draws it *and* goes to it, with no second affordance. -- yes it does. it is an action button. just clicking on the row deselects the row; i would remove that automated action. let the row selection just identify the object being targeted, with the box selecting the object and the "go" moving the camera separately. 

3. **Tapping a marker on a hidden shell currently draws it.** I changed
   that without being asked. Should it only go, and leave drawing to the
   drawer? -- unclear

4. **Is the drawer the right height in portrait?** Sixty percent was a
   guess. -- it's fine. its a temporary card. 

5. **Does the eighteen-row list want grouping?** The config already
   groups these -- structures, atmosphere, wind, Oort, hill sphere. The
   study ignores that and shows one flat list. -- it's okay. it follows the orrery pattern. indentation could work too. 

6. **Does the frame want to be gentler?** It cuts straight to the new
   range. An eased move would show the visitor how much bigger the next
   shell is, which is arguably the whole lesson of the exhibit. -- it works. 

---

## Recording the run

For each failure, note the check number, what you saw, and the browser
or phone. A failure with no note is a failure that has to be found twice.

If a check cannot be run at all -- the phone path was not set up, say --
record it as **not run**, never as a pass. An unrun check counted as
passing is the failure mode this protocol is shaped to avoid.
