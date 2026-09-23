# Test protocol -- the Sun exhibit hang, 2026-09-02

**Built on** gallery `e0edd16c5e6f406a7b8b66323ff2e4f75db62726` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main),
with Stage B (`patch_L267_2`) applied and pushed.

Page under test: https://palomasorrery.com/interactive.html?exhibit=sun

---

## What this is for

The hang has to be attributed before anything is changed. There are four
live candidates and they call for four different fixes. Guessing wrong
costs a Mode 5 round each time.

This protocol does not confirm the hang. It separates the candidates.
Every trial below states what each outcome RULES OUT, so a trial that
cannot rule anything out has no business being in the list.

---

## The four candidates

**H1 -- hover hit-testing.** Plotly's 3D hover reads pixels back off the
GPU on every mouse move. On a heavy scene the browser reports this as
"GPU stall due to ReadPixels" and the page goes unresponsive while the
last tooltip stays parked on screen.

*Evidence for:* this is not a new bug. It was found on 2026-08-30 in the
mockup, named there as "the page feels seized rather than merely stale,"
and the fix written was to clear the tooltip and set `hovermode: false`.
**That fix never left the mockup.** The word `hovermode` does not appear
anywhere in `interactive.html` or `gallery/feature_renderers.js` at
`e0edd16c`. The symptom you describe -- unresponsive, then the hovertext
jumping to the top-left corner -- is the same shape.

*What would rule it out:* Trial 3. If turning hover off does not change
the tap count before the hang, H1 is not the cause.

**H2 -- scene weight.** Stage B does not hide anything when it focuses,
so all nineteen groups stay drawn while the frame shrinks to one small
object. Every vertex of the Oort cloud, the heliopause and the galactic
tide is still transformed and clipped on every frame.

*What would rule it out:* Trial 4. If a two-shell scene hangs at the same
count, weight is not the cause.

**H3 -- the framing relayout.** `sunFrameOn` is new in Stage B. It calls
`Plotly.relayout` with a range and a dtick on all three axes, which makes
gl3d rebuild the scene. Nothing waits for the previous rebuild to finish
before the next tap starts one.

*What would rule it out:* Trial 5. If calling `sunFrameOn` repeatedly on
its own never hangs, H3 is not the cause.

**H4 -- one specific object.** The Alfven surface is where it stopped. It
may be the only group whose geometry or radius does something the others
do not.

*What would rule it out:* Trial 2. If the hang tracks the tap COUNT
rather than which object was tapped, H4 is dead.

There is a fifth possibility worth naming so it is not assumed away: the
mockup passed Mode 5 on 2026-08-30 with schematic geometry, and the live
page has real traces including point clouds. **The mockup validated the
interaction design, not the performance.** A Stage B port can be a
faithful port and still be too heavy.

---

## Setup, once

1. Open the page. Press **F12** to open Chrome DevTools. Dock it to the
   right so it does not resize the plot between trials. -- done
2. Click the **Console** tab. Leave it open for every trial. -- done
3. Each trial should start with a clean console. Chrome already clears it
   on reload by default, so there is nothing to set. If you want to be
   sure, click the **circle with a slash through it** at the top left of
   the Console toolbar -- that is Clear console -- before each trial.

   (An earlier draft of this file sent you to Settings > Preferences for
   a "Preserve log" checkbox. It is not there. That control lives in the
   Console tab's own settings gear, and it is off by default, which is
   what this step wanted anyway.)

For every trial: reload with **Ctrl+Shift+R** first. A plain reload can
reuse the WebGL context.

Record for each trial: the tap number where it hung (or "no hang"), and
anything red or yellow in the console.

---

## Trial 1 -- control: is Stage B involved at all?

Reload. Touch nothing in the drawer and tap no markers. Rotate the scene
with the mouse continuously for 60 seconds, -- no problems

then hover slowly across the shells for another 30. -- no problems

- **If it hangs:** Stage B is not the cause. Stop here and report it --
  H1 or H2, and the rest of the protocol changes.
- **If it does not hang:** focusing is implicated. Continue.

This trial is first because it is the only one that can exonerate the
patch, and everything below assumes the patch is involved.

---

## Trial 2 -- does the hang track the count or the object?

Reload. Tap cross markers in this order, one every three seconds, and say
the number out loud as you go:

Core, Radiative Zone, Convective Zone, Photosphere, Chromosphere,
Inner Corona, Outer Corona, Alfven Surface, Termination Shock,
Heliopause, Inner Oort Cloud, Outer Oort Cloud.

Record the tap number where it hangs. -- no problems

Reload. Run the **same list backwards**. Record the number again. -- no problems

- **Same COUNT both times, different object:** accumulation. H4 is dead.
- **Same OBJECT both times, different count:** it is that object. H4
  stands and Trials 3 to 5 can wait.
- **No hang on the second pass:** timing-dependent. Note how fast you
  were tapping; three seconds may already be enough to let it settle. -- no problems at 3 seconds

---

## Trial 3 -- RETIRED, 2026-09-02. Do not run this again.

**The command in this trial breaks the page.** Setting `hovermode: false`
by relayout on this gl3d scene threw
`RangeError: Maximum call stack size exceeded` inside plotly-2.35.2,
which aborted the relayout partway and destroyed the scene's saved state.
Everything after that failed for the same reason -- the cascade ends with
`Cannot read properties of undefined (reading 'viewInitial')`, which is
the stored initial camera the modebar reset button reads. That is why GO
stopped working and why reset did nothing.

So the hang Tony saw in Trial 3 is NOT the hang being investigated. It is
a second, different failure that this trial introduced. **H1 remains
untested.** Recovery is a reload; nothing is damaged on disk.

Worth noting for later: the same `hovermode: false` call works in
`sun_gui_mockup.html`. Same call, same Plotly version, different scene.
That is a real difference between the mockup and the live page and it is
not yet explained.

~~Reload. Before tapping anything, paste this into the Console:~~
~~`Plotly.relayout(document.getElementById('plotly-container'), {hovermode:false})`~~

---

## What Trials 1 and 2 actually established -- REVISED 2026-09-02

Less than the first reading of them claimed, because this protocol left
the drawn set uncontrolled and both trials were run with a light scene.

How they were actually run, in Tony's words:

- Trial 1: only the default shells through the outer corona. Not all
  nineteen.
- Trial 2: no cross markers were tapped at all. The drawer was emptied
  first, then one shell was switched on, hovered for three seconds,
  switched off, and the next switched on -- so exactly ONE shell was
  drawn at any moment, and the path exercised was the checkbox
  (`sunApplyVisibility`), not the marker (`sunFocusOn`). Tony did this
  because the cross markers are hard to see and hit in a populated
  scene, which is a fair reason and a GUI finding in its own right.

So the corrected reading:

**H1 is NOT weakened.** Trial 1 hovered over a partial scene. The
hover-hit-test cost scales with what is drawn, and the heavy traces were
absent.

**H2 is NOT weakened. It is untouched, and that matters most.** The
original hang had the default set drawn and the camera framing down onto
one small object. Trial 2 never once had more than a single shell in the
scene, so the condition H2 describes -- a tight frame with large traces
still drawn -- was never created.

**H3 is not supported either.** The three-second gap was there, but so
was a nearly empty scene, so the clean result has two explanations and
cannot choose between them.

**And the marker path was never exercised.** The original failure was a
marker tap on the Alfven surface. Nothing run so far has tapped a marker.

The defect is this protocol's, not the testing. Trials that start from a
clean state cannot separate causes that only appear in a loaded one. The
trials below start from the FAILING condition and remove one thing at a
time.

---

## Trial R -- reproduce first. Nothing below means anything without this.

Reload with Ctrl+Shift+R and change nothing in the drawer -- the default
arrival set stays exactly as it loads.

Tap cross markers the way you did yesterday. Natural speed, no counting,
no three-second discipline. Include the Alfven surface.

- **It hangs:** good. That is the baseline, and every trial below is a
  subtraction from it.
- **It does not hang after 20 or so taps:** the failure needs something
  neither of us has identified yet. Stop and say so. Guessing further
  from here would be inventing a cause.

Record roughly how many taps, and which object was focused when it went.

---

## Trial R RESULT, 2026-09-02 -- this changes the whole investigation

**It hung on the first hover, over the outer corona. No marker was
tapped. No focus operation ran.** One error in the console:

```
Uncaught RangeError: Maximum call stack size exceeded   plotly-2.35.2.min.js:8
```

plus the standing `Canvas2D: Multiple readback operations using
getImageData` warning, which is the hover hit-test reading pixels back
off the GPU.

**Stage B is very likely not the cause, and this is an argument from the
code rather than a hunch.** On arrival, the only Stage B code that runs
is `sunFocusIdx = sunOutermostShown(); renderSunDrawer();`. Both touch
the DOM. Neither calls Plotly. The plot state at the moment of the hang
is byte-for-byte what Stage A produced -- same `newPlot`, same arrival
layout, same floor. Tony changed nothing in the drawer before hovering.

**And the Trial 3 RangeError was misattributed.** I blamed the
`hovermode: false` command for causing it. The same error now appears
with no command run at all, so the command did not cause it -- it hit the
same path. What the command DID do is take the scene down with it, which
is why reset stopped working there.

**H1 is now the leading candidate, in a sharper form.** Not "hover is
slow" but "hover blows the JavaScript call stack." That is a specific,
findable bug, and it is the kind of thing that happens in Plotly when a
routine applies a very large array as function arguments -- the argument
limit is around 65,000.

**The drawn set was the SAME in both, so that is not the variable.** An
earlier version of this section said Trial R used the full default set.
It did not -- Tony ran it with the same shells out through the outer
corona that Trial 1 used. Identical scenes. One hovered fine for thirty
seconds; the other died on the first hover.

That leaves the difference somewhere else, and the most promising place
is WHERE the pointer was. Trial 1 hovered "slowly across the shells."
Trial R died on the outer corona specifically -- the dense teal point
cloud in the render. So the candidate becomes narrower and more testable:

**H5 -- one trace is large enough to overflow the stack when hovered.**
Trial 1 may simply never have landed on it. This would explain the
30-second clean run and the instant death equally well, and nothing else
so far explains both.

---

## Next: two read-only reads. Neither changes anything.

Reload with Ctrl+Shift+R. Do not touch the drawer. Do not hover yet.

**Read 1 -- how big are the traces?** Paste and press Enter:

```
document.getElementById('plotly-container').data.map(t=>[t.name,(t.x||[]).length]).sort((a,b)=>b[1]-a[1]).slice(0,8)
```

console.table(document.getElementById('plotly-container').data.map(t=>({points:(t.x||[]).length, name:t.name||t.legendgroup||"?"})).sort((a,b)=>b.points-a.points))

[
    {
        "points": 4332,
        "name": "Sun: Streamer Belt (helmet and stalk)"
    },
    {
        "points": 3600,
        "name": "Sun: Hills Cloud (torus)"
    },
    {
        "points": 2000,
        "name": "Sun: Galactic Tide (thinned at the plane)"
    },
    {
        "points": 1782,
        "name": "Sun: Outer Oort Cloud (clumps)"
    },
    {
        "points": 625,
        "name": "Sun: Core"
    },
    {
        "points": 625,
        "name": "Sun: Radiative Zone"
    },
    {
        "points": 625,
        "name": "Sun: Photosphere"
    },
    {
        "points": 625,
        "name": "Sun: Chromosphere (2,000 km skin)"
    },
    {
        "points": 400,
        "name": "Sun: Inner Corona"
    },
    {
        "points": 400,
        "name": "Sun: Roche Limit (Comets)"
    },
    {
        "points": 400,
        "name": "Sun: Alfven Surface"
    },
    {
        "points": 400,
        "name": "Sun: Outer Corona"
    },
    {
        "points": 400,
        "name": "Sun: Termination Shock"
    },
    {
        "points": 400,
        "name": "Sun: Heliopause"
    },
    {
        "points": 400,
        "name": "Sun: Inner Limit of Oort Cloud"
    },
    {
        "points": 400,
        "name": "Sun: Inner Oort Cloud"
    },
    {
        "points": 400,
        "name": "Sun: Outer Oort Cloud"
    },
    {
        "points": 400,
        "name": "Sun: Gravitational Influence"
    },
    {
        "points": 1,
        "name": "Sun"
    },
    {
        "points": 1,
        "name": "Sun: Core"
    },
    {
        "points": 1,
        "name": "Sun: Radiative Zone"
    },
    {
        "points": 1,
        "name": "Sun: Photosphere"
    },
    {
        "points": 1,
        "name": "Sun: Streamer Belt (helmet and stalk)"
    },
    {
        "points": 1,
        "name": "Sun: Chromosphere (2,000 km skin)"
    },
    {
        "points": 1,
        "name": "Sun: Inner Corona"
    },
    {
        "points": 1,
        "name": "Sun: Roche Limit (Comets)"
    },
    {
        "points": 1,
        "name": "Sun: Alfven Surface"
    },
    {
        "points": 1,
        "name": "Sun: Outer Corona"
    },
    {
        "points": 1,
        "name": "Sun: Termination Shock"
    },
    {
        "points": 1,
        "name": "Sun: Heliopause"
    },
    {
        "points": 1,
        "name": "Sun: Hills Cloud (torus)"
    },
    {
        "points": 1,
        "name": "Sun: Outer Oort Cloud (clumps)"
    },
    {
        "points": 1,
        "name": "Sun: Galactic Tide (thinned at the plane)"
    },
    {
        "points": 1,
        "name": "Sun: Inner Limit of Oort Cloud"
    },
    {
        "points": 1,
        "name": "Sun: Inner Oort Cloud"
    },
    {
        "points": 1,
        "name": "Sun: Outer Oort Cloud"
    },
    {
        "points": 1,
        "name": "Sun: Gravitational Influence"
    }
]

Click the little triangle on the result to expand it, and send the eight
rows. Any trace with more than about 65,000 points is the prime suspect
on its own.

**Read 2 -- where does the stack overflow happen?** Now hover until it
hangs. -- same behavior as before. hung on outer corona. hovertext hung for about 30 seconds. 

In the Console, click the **triangle to the left of** `Uncaught
RangeError: Maximum call stack size exceeded` to expand it. That reveals
the call stack. Send the top eight or so lines, even though the names are
minified -- a repeating frame name is the recursive function, and that is
the whole answer.

plotly-2.35.2.min.js:8 Canvas2D: Multiple readback operations using getImageData are faster with the willReadFrequently attribute set to true. See: https://html.spec.whatwg.org/multipage/canvas.html#concept-canvas-will-read-frequently
(anonymous) @ plotly-2.35.2.min.js:8
t.exports @ plotly-2.35.2.min.js:8
t.exports @ plotly-2.35.2.min.js:8
u.<computed>.triangles @ plotly-2.35.2.min.js:8
s @ plotly-2.35.2.min.js:8
h.update @ plotly-2.35.2.min.js:8
t.exports @ plotly-2.35.2.min.js:8
d.update @ plotly-2.35.2.min.js:8
t.exports @ plotly-2.35.2.min.js:8
createScene @ plotly-2.35.2.min.js:8
k.tryCreatePlot @ plotly-2.35.2.min.js:8
k.initializeGLPlot @ plotly-2.35.2.min.js:8
T @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.newPlot @ plotly-2.35.2.min.js:8
initSunExhibit @ interactive.html?exhibit=sun:1425
await in initSunExhibit
pyodideScript.onload @ interactive.html?exhibit=sun:1698
script
loadPyodideRuntime @ interactive.html?exhibit=sun:1695
(anonymous) @ interactive.html?exhibit=sun:1716
console.table(document.getElementById('plotly-container').data.map(t=>({points:(t.x||[]).length, name:t.name||t.legendgroup||"?"})).sort((a,b)=>b.points-a.points))
VM681:1 (index)pointsname(index)pointsname04332'Sun: Streamer Belt (helmet and stalk)'13600'Sun: Hills Cloud (torus)'22000'Sun: Galactic Tide (thinned at the plane)'31782'Sun: Outer Oort Cloud (clumps)'4625'Sun: Core'5625'Sun: Radiative Zone'6625'Sun: Photosphere'7625'Sun: Chromosphere (2,000 km skin)'8400'Sun: Inner Corona'9400'Sun: Roche Limit (Comets)'10400'Sun: Alfven Surface'11400'Sun: Outer Corona'12400'Sun: Termination Shock'13400'Sun: Heliopause'14400'Sun: Inner Limit of Oort Cloud'15400'Sun: Inner Oort Cloud'16400'Sun: Outer Oort Cloud'17400'Sun: Gravitational Influence'181'Sun'191'Sun: Core'201'Sun: Radiative Zone'211'Sun: Photosphere'221'Sun: Streamer Belt (helmet and stalk)'231'Sun: Chromosphere (2,000 km skin)'241'Sun: Inner Corona'251'Sun: Roche Limit (Comets)'261'Sun: Alfven Surface'271'Sun: Outer Corona'281'Sun: Termination Shock'291'Sun: Heliopause'301'Sun: Hills Cloud (torus)'311'Sun: Outer Oort Cloud (clumps)'321'Sun: Galactic Tide (thinned at the plane)'331'Sun: Inner Limit of Oort Cloud'341'Sun: Inner Oort Cloud'351'Sun: Outer Oort Cloud'361'Sun: Gravitational Influence'Array(37)
undefined
plotly-2.35.2.min.js:8 Uncaught RangeError: Maximum call stack size exceeded
V @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
R @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
mt @ plotly-2.35.2.min.js:8
J.each @ plotly-2.35.2.min.js:8
D @ plotly-2.35.2.min.js:8
e.loneHover @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
e.layoutReplot @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
a.emit @ plotly-2.35.2.min.js:8
t.emit @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
e.layoutReplot @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
a.emit @ plotly-2.35.2.min.js:8
t.emit @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
e.layoutReplot @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
a.emit @ plotly-2.35.2.min.js:8
t.emit @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
e.layoutReplot @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
a.emit @ plotly-2.35.2.min.js:8
t.emit @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
e.layoutReplot @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
a.emit @ plotly-2.35.2.min.js:8
t.emit @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
e.layoutReplot @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
a.emit @ plotly-2.35.2.min.js:8
t.emit @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
e.layoutReplot @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
a.emit @ plotly-2.35.2.min.js:8
t.emit @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
e.layoutReplot @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
a.emit @ plotly-2.35.2.min.js:8
t.emit @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
e.layoutReplot @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
a.emit @ plotly-2.35.2.min.js:8
t.emit @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
e.layoutReplot @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
a.emit @ plotly-2.35.2.min.js:8
t.emit @ plotly-2.35.2.min.js:8
k.render @ plotly-2.35.2.min.js:8
t.glplot.onrender @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
F.redraw @ plotly-2.35.2.min.js:8
k.plot @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.call @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
createScene @ plotly-2.35.2.min.js:8
k.tryCreatePlot @ plotly-2.35.2.min.js:8
k.initializeGLPlot @ plotly-2.35.2.min.js:8
T @ plotly-2.35.2.min.js:8
e.plot @ plotly-2.35.2.min.js:8
e.drawData @ plotly-2.35.2.min.js:8
h.syncOrAsync @ plotly-2.35.2.min.js:8
e._doPlot @ plotly-2.35.2.min.js:8
e.newPlot @ plotly-2.35.2.min.js:8
initSunExhibit @ interactive.html?exhibit=sun:1425
await in initSunExhibit
pyodideScript.onload @ interactive.html?exhibit=sun:1698
script
loadPyodideRuntime @ interactive.html?exhibit=sun:1695
(anonymous) @ interactive.html?exhibit=sun:1716


If the page is too hung to expand the error, reload, hover to trigger it
again, and expand it before touching anything else.

**Read 3 -- is it one trace?** Reload. Hover the inner shells only: the
core, then the radiative zone, then the photosphere. Stay off the outer
corona. Give each a few seconds.

- **No hang, then hover the outer corona and it dies:** H5 confirmed. One
  trace, and Read 1 will say why.
- **It dies on an inner shell too:** H5 is dead and the trigger is not a
  particular trace.

Neither read draws, relayouts, or changes state. They only look.

---

## READ 1 RESULT, 2026-09-02 -- size is not the cause

The whole scene is tiny. Largest trace 4,332 points (Streamer Belt), then
Hills Cloud 3,600, Galactic Tide 2,000, Outer Oort clumps 1,782. Every
sphere shell is 400 or 625 points. **Outer Corona, the one that hangs, is
400 points.** The info cross markers are 1 point each, as the single info
marker pattern intends.

Nothing is within two orders of magnitude of the ~65,000 argument limit.
**H5 is dead.** A 400-point trace cannot overflow the call stack by array
size, and hit-testing 400 points is not slow.

So the overflow is RECURSION, not volume. Something in Plotly's hover
path is calling itself without terminating. That is usually caused by the
CONTENT of a particular trace rather than its size, which fits what we
see: hover works on some shells and dies on this one.

The likeliest content to do it is the hover text. Plotly renders hover
labels through a routine that parses the string for `<br>` and other tags
and builds nested SVG text spans. Malformed, unbalanced or deeply nested
tags are a known way to send it into recursion. The Sun's shell text
comes from the `*_info` strings, which carry newlines in the orrery and
are converted to `<br>` at the Plotly boundary -- a conversion with a
real chance of emitting something the parser cannot close.

Hypothesis, not a finding. Read 4 tests it.

---

## Read 4 -- what is in the outer corona's hover text?

Reload. Before hovering anything, paste this one line:

```
copy(JSON.stringify(document.getElementById('plotly-container').data.filter(t=>/Outer Corona|Sun: Core/.test(t.name||t.legendgroup||"")).map(t=>({name:t.name,lg:t.legendgroup,hoverinfo:t.hoverinfo,hovertemplate:t.hovertemplate,text:t.text,hovertext:t.hovertext})),null,1))
```

`copy(...)` puts the result on the clipboard instead of printing it, so
nothing is truncated. Paste it into a file or straight into the chat.

[
 {
  "name": "Sun: Core",
  "lg": "Sun: Core",
  "hoverinfo": "skip"
 },
 {
  "name": "",
  "lg": "Sun: Core",
  "hovertemplate": "%{text}<extra></extra>",
  "text": [
   "Sun: Core<br><br>Radius: 0.2 solar radii<br>= 139,140 km (0.000930 AU)<br><br>Source: Bahcall, Pinsonneault & Basu (2001), ApJ 555:990 (radial<br>profiles); drawn at the low end of the conventional 0.2-0.25 R_sun<br>core range"
  ]
 },
 {
  "name": "Sun: Outer Corona",
  "lg": "Sun: Outer Corona",
  "hoverinfo": "skip"
 },
 {
  "name": "",
  "lg": "Sun: Outer Corona",
  "hovertemplate": "%{text}<extra></extra>",
  "text": [
   "Sun: Outer Corona<br><br>Radius: 50 solar radii<br>= 34,785,000 km (0.233 AU)<br><br>Source: Mann et al. (2004), A&A 414:1127; F-corona envelope, not a<br>sharp physical edge"
  ]
 }
]

It returns the traces for the Outer Corona, which hangs, and the Core,
which does not. Comparing the two is the point: whatever differs in those
strings is the candidate. -- note that the scene did not hang by hovering. i was able to hover over each visible marker and the hover text displays. it hung when i "clicked" on the cross marker. note that as i am typing in VS, the "Backspace" key causes a delay before i am able to proceed between a second to about 5 to 10 seconds inconsistently.

## READ 4 RESULT, 2026-09-02 -- it is the CLICK, not the hover

Tony's note: "the scene did not hang by hovering. I was able to hover
over each visible marker and the hover text displays. It hung when I
CLICKED on the cross marker."

That is the first clean attribution in this whole investigation, and it
reverses two things.

**H1 is dead. Hover is exonerated.** Every marker hovers fine and its
text displays. And the two strings came back well formed -- short,
balanced `<br>`, a closed `<extra></extra>`, no nesting. The hover-text
recursion idea is dead with it.

**Stage B is back in, and narrowly.** A click on a cross marker reaches
`plotly_click` -> `sunFocusOn` -> `sunFrameOn` -> `Plotly.relayout`.
That whole chain is new in Stage B. Nothing else runs on a click.

So the question is now small enough to answer in three commands: is the
relayout itself the problem, or is the problem calling it from INSIDE
Plotly's own click handler? Those are different bugs with different
fixes, and Read 5 separates them.

Worth knowing which, because the second is a one-line fix. Mutating a
plot synchronously inside a Plotly event handler re-enters Plotly's
update machinery while it is still dispatching; deferring the call by a
single tick lets the dispatch finish first.

**Before running anything: close the hung tab.** A page in a runaway loop
pegs a CPU core, which is the likeliest explanation for the one-to-ten
second Backspace lag in VS Code.

---

## Read 5 -- same function, three contexts

Three steps. Reload with Ctrl+Shift+R before each. Leave the drawer
alone.

**Step 1 -- the relayout alone, no click, no chrome.**

```
sunFrameOn(sunGroups.findIndex(g=>/Outer Corona/.test(g.name)))
```

- **Hangs:** the relayout is the bug. Read 6 would then be the dtick and
  range values it is being handed. -- hung. see uploaded image. 

plotly-2.35.2.min.js:8 Canvas2D: Multiple readback operations using getImageData are faster with the willReadFrequently attribute set to true. See: https://html.spec.whatwg.org/multipage/canvas.html#concept-canvas-will-read-frequently
(anonymous) @ plotly-2.35.2.min.js:8
sunFrameOn(sunGroups.findIndex(g=>/Outer Corona/.test(g.name)))
Promise {<fulfilled>: div#plotly-container.js-plotly-plot}
plotly-2.35.2.min.js:8 Uncaught RangeError: Maximum call stack size exceeded
V @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
R @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
mt @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
D @ plotly-2.35.2.min.js:8
t.38103.e.loneHover @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
t.71817.e.layoutReplot @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
t.71817.e.layoutReplot @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
t.71817.e.layoutReplot @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
t.71817.e.layoutReplot @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
t.71817.e.layoutReplot @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
t.71817.e.layoutReplot @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
t.71817.e.layoutReplot @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
t.71817.e.layoutReplot @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
t.71817.e.layoutReplot @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
t.71817.e.layoutReplot @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
q @ plotly-2.35.2.min.js:8
sunFrameOn @ interactive.html?exhibit=sun:1267
sunFocusOn @ interactive.html?exhibit=sun:1295
(anonymous) @ interactive.html?exhibit=sun:1461
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
H @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
(anonymous) @ plotly-2.35.2.min.js:8
t.33626.e.call @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8
requestAnimationFrame
t @ plotly-2.35.2.min.js:8


- **Fine:** the relayout is innocent in isolation. Go to Step 2.

**Step 2 -- the whole focus call, still no click.**

```
sunFocusOn(sunGroups.findIndex(g=>/Outer Corona/.test(g.name)))
```

This adds closing the drawer and redrawing the rows. Same code a click
runs, just not called from inside the click event.

- **Hangs:** the cause is in the DOM work around the relayout.
- **Fine:** go to Step 3.

**Step 3 -- now click the outer corona's cross marker.**

- **Hangs:** confirmed. The code is fine and the CONTEXT is the bug --
  relayout re-entering Plotly from inside its own click dispatch. The fix
  is to defer `sunFocusOn` by one tick out of the handler, and it is two
  lines.
- **Fine:** the failure is not reproducing today, which is its own
  finding. Say so rather than hunting.

Steps 1 and 2 change the camera, so the view will move. Nothing else is
altered and a reload restores everything.

---

## READ 5 RESULT, 2026-09-02 -- the stack trace names it

The expanded stack, innermost first:

```
V  <-  (anon)  <-  R  <-  (anon)  <-  (anon)  <-  mt  <-  (anon)  <-  D
   <-  t.38103.e.loneHover
   <-  (anon) x2  <-  H  <-  (anon) x6
   <-  t.33626.e.call  <-  t.71817.e.layoutReplot  <-  (anon)  <-  q
   <-  sunFrameOn        interactive.html:1267
   <-  sunFocusOn        interactive.html:1295
   <-  (anon)            interactive.html:1461   <- the plotly_click handler
   <-  plotly-2.35.2.min.js
```

**`loneHover` is Plotly's hover-label renderer.** Its presence inside a
`layoutReplot` stack means a hover label was ACTIVE when the relayout
ran, and the replot went to re-render it. That is where the recursion
lives.

The mechanism fits every result on record:

- **The click hangs** because you must hover a cross marker to click it.
  The tooltip is up at the instant the relayout fires.
- **Hovering alone is fine** because nothing relayouts.
- **Trial 2 was fine** because the pointer was over the DRAWER when the
  checkbox relayout ran. No hover label was active.
- **Trial 1 was fine** for the same reason -- no relayout at all.
- **Trial 3 died** because a console relayout ran while the page still
  had a live hover state, which is the same collision by another route.

**The fix already exists and has already passed Mode 5.** The mockup
calls `Plotly.Fx.unhover(gd)` before its relayouts. That line never
travelled to `interactive.html`. It was written on 2026-08-30 for what
looked like a different symptom, and it is the right fix for this one.

Not yet confirmed. Read 6 confirms it before anything is patched.

---

## Read 6 -- confirm the fix before writing it

Two timed runs. The delay lets the relayout fire while your pointer is
still resting on a marker, which is the condition a click creates.

Reload with Ctrl+Shift+R before each.

**Run 1 -- reproduce, deliberately.** Paste, press Enter, then move the
pointer onto any cross marker and HOLD STILL until the tooltip shows and
the five seconds elapse.

```
setTimeout(()=>sunFrameOn(sunGroups.findIndex(g=>/Outer Corona/.test(g.name))), 5000)
```

Expected: it hangs. If it does NOT hang, an active hover label is not the
trigger and this whole reading is wrong. -- hung in the same manner upon click. simple hold still does not do it.  the backspace sis hanging up. even aftr many seconds the hold still do did not hang up... not able to backspace. note that upon hoveritin hovering and holding still, then after about 5-10 sgrid appeared, but not initially. i mean the secondary tics appeared . 

**Run 2 -- the same thing, with the tooltip dismissed first.** Same
gesture: paste, hover a marker, hold still.

```
setTimeout(()=>{Plotly.Fx.unhover(document.getElementById('plotly-container')); sunFrameOn(sunGroups.findIndex(g=>/Outer Corona/.test(g.name)));}, 5000)
```

Expected: the camera moves and nothing hangs. -- hte backspace is still hanging. not able to backspace. i closed th e browser and reopened. ni have not done anything with the scene s except F12. secondary tei tics appear after about 5 seconds. rotation works and nothing hangs hovertext appears okay. upon clicking on the hover marker the scene hangs

**Run 1 hangs and Run 2 does not:** confirmed, and the patch is one line
in `sunFocusOn` plus one in `sunApplyVisibility`.

**Both hang:** unhover is not enough, and the fix is larger. -- his i this is the case. what is interesting is that hte backpa bacs backspace hangs before i do na anything with the scene. 

**Neither hangs:** the trigger is something else about the click, and the
next step is another read rather than a patch.

---

## READ 6 RESULT, 2026-09-02 -- neither timed run hung. The CLICK does.

Tony's summary said both hung, but his own detail says otherwise, and the
detail is what counts:

- Run 1: "simple hold still does not do it... upon hovering and holding
  still, then after about 5-10 s the secondary ticks appeared."
- Run 2: "secondary ticks appear after about 5 seconds. Rotation works
  and nothing hangs, hovertext appears okay. Upon clicking on the hover
  marker the scene hangs."

**Secondary ticks appearing IS the relayout completing.** `dtick` is set
only by `sunFrameOn`, and nothing else in the page sets it. So in both
runs the timed relayout ran to completion, with a hover label active, and
the page stayed alive. Rotation and hover kept working afterwards.

Then a click killed it. Both times.

So the outcome is the third branch of Read 5, and it is now supported by
three independent observations:

**The relayout is innocent.** It has now completed cleanly from the
console with a tooltip up (Run 1), with the tooltip dismissed (Run 2),
and in Read 5 Step 1 where it returned a fulfilled Promise.

**Unhover is not the fix.** Run 2 tested it directly. H1 stays dead.

**The bug is the CONTEXT.** The same relayout is fatal only when reached
from inside `plotly_click`. The Read 5 stack says exactly that:
`(anon) interactive.html:1461` is the click handler, and everything above
it is Plotly re-entering its own update machinery -- `layoutReplot`
running while the click dispatch that triggered it has not returned.

A detail that supports this and that an earlier reading missed: the
visible stack is about twenty-five frames. **A stack overflow with a
shallow stack is not runaway recursion.** It is what you get when a
routine applies a very large array as function arguments partway down --
which is what a half-finished replot re-entering itself produces.

**The fix is to let the dispatch finish before touching the plot.**
Deferring `sunFocusOn` by a single tick out of the handler is two lines,
and it is testable right now without a patch.

---

## Read 7 -- confirm the deferred handler, no patch needed

Reload with Ctrl+Shift+R. Paste this one line and press Enter. It
replaces the click handler with a deferred version, live, in the page:

```
(()=>{const gd=document.getElementById('plotly-container');gd.removeAllListeners('plotly_click');gd.on('plotly_click',ev=>{if(!ev||!ev.points||!ev.points.length)return;const k=sunTraceGroup[ev.points[0].curveNumber];if(typeof k==='number')setTimeout(()=>sunFocusOn(k),0);});console.log('deferred click handler installed');})()
```

You should see `deferred click handler installed`. the return )(Enter) na and backspace do not work in vs. typed the above. confirmed as you said. backspace does not work. 

Now click cross markers the way you did in Trial R. Ten or so, at natural
speed, including the outer corona and the Alfven surface.

- **No hang:** confirmed. The patch is two lines and I write it. -- confirmed. double ck clicking on the hover marker selects that shell. rotates okay. click on marker does not hang. the b vs hang does still happen. reset works. the drwa drw drawer works. 







- **Still hangs:** deferring is not enough. The next step is to stop
  reframing on click entirely and keep the rest of Stage B, which is the
  fallback already named at the end of this file.

Nothing is written to disk. A reload restores the original handler. 

---

## Not our bug: the VS Code backspace lag

Tony: "backspace in VS hanging before I do anything with the scene.
Backspace in this chat works fine."

Before the scene is touched, and not in the browser, so the runaway tab
is not causing it. It is a VS Code or machine problem, not this one, and
it should not be folded into this investigation. Worth its own look
later -- a repo folder inside OneDrive is a common cause of editor
stalls -- but not now. -- this has never happened before now==. it still happens when Chrome is shut down. 

---

## Trial S -- is it the RATE? (tests H3)

Three runs. Reload before each and **leave the drawer alone**, so the
default set is drawn throughout. Paste each line into the Console, press
Enter, watch 30 seconds.

`sunFocusOn` is what a marker tap calls, minus the click handling, so
this exercises the real path without having to hit a small target.

**Run A -- slow, the control.**

```
for (let i=0;i<12;i++) setTimeout(()=>sunFocusOn(i%12), i*2000)
```

**Run B -- fast.** Same code, same objects, same order. Only the interval
changes.

```
for (let i=0;i<12;i++) setTimeout(()=>sunFocusOn(i%12), i*250)
```

**Run C -- fast, but serialised.** `sunFocusOn` returns the relayout's
promise. This awaits each one, so the next focus cannot begin until the
last has finished.

```
(async()=>{ for (let i=0;i<12;i++) { await sunFocusOn(i%12); } })()
```

Reading it:

- **A fine, B hangs, C fine:** H3 confirmed and C is the fix. Serialising
  is a small change and needs no design decision.
- **A fine, B hangs, C hangs too:** rate matters but awaiting is not
  enough. The fix is larger and probably means not reframing per focus.
- **B fine:** H3 is dead. Rate is not the variable.

Run C is the one that earns its place: it tests the fix before I write
it.

---

## Trials 4, 5 and 6 -- superseded

Trial 4 became Trial W and Trial 5 became Trial S, both rewritten to
start from the loaded scene rather than a clean one. Trial 6, the numeric
check on radii and dtick, is still worth two minutes if R, W and S all
come back inconclusive:

```
sunGroups.map((g,i)=>[g.name, sunGroupRadius(i), sunGridDtick(2*sunGroupRadius(i)*1.1)])
```

Every radius should be positive and finite, every dtick positive and
roughly a sixth of twice the radius. A dtick of 0, NaN or Infinity would
be the hang on its own.

---

## What to send back

```
Trial R  hangs after ~__ taps on ______ / no hang after 20
Trial W  hangs after ~__ taps / no hang
Trial S  A: ______  B: ______  C: ______
```

Plus any red console error, and any yellow warning mentioning GPU,
ReadPixels or WebGL context.

**Stop at the first trial that answers cleanly.** If R will not reproduce
the failure, stop there and say so -- everything after it assumes a
baseline that does not exist.

---

## What I will not do with the result

I will not ship a fix on a verdict the data does not support. The
2026-09-01 session produced a diagnostic that printed READONLY IS THE
CAUSE while its own rows showed every case identical, and a fix on that
verdict would have looked like a diagnosis and been a guess. If these
trials come back mixed, the honest answer is that the cause is not yet
known, and the next step is another trial rather than a patch.

If it becomes clear the port is sound but the live scene is simply too
heavy for per-focus reframing, reverting Stage B's framing while keeping
its row split is a real option and is not a failure. The row split, the
focus label and the marker navigation are all independently useful and
none of them relayouts anything.

---

*Written September 2, 2026 with Anthropic's Claude Opus 5. Built on
gallery `e0edd16c`.*
