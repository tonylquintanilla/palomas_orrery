# Earth's magnetosphere reaches the web page, and the belts find their plane

Orrery at `04e385f3`, gallery at `97867f3e`, both read back with `ls-remote`
at the close.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-15
Type: BUILD. Eleven patches applied, one withdrawn unrun.
Handles: L-231, L-305 items 5 and 6b, L-330 (new).
Reviewed at the start by Claude Fable 5.1; its findings are recorded in
L-231.

---

## STEP 0 — before you do anything

1. `git status --porcelain` in BOTH repositories. Expect nothing. This
   session opened with an Earth scene checker failing on a working copy
   that did not match its commit, and two sessions had waved that failure
   off as known-old. It was not.
2. `git ls-remote` both. Expect the two commits above.
3. **Read STILL OPEN below before picking anything up.** Three interface
   changes are decided and unbuilt, and they are the first task.
4. Version-check every skill at load, as usual.

---

## WHAT HAPPENED

The web page could not draw Earth's magnetosphere. It had been served one
number for each boundary — the distance to the nose — which is a single
point on a surface. The shape existed nowhere: not in the served data, and
not in the desktop orrery either, which drew a typed half-ellipsoid that
the provenance rules had already refused to promote.

It turned out the research was done. Every coefficient of Shue's
magnetopause and Jelinek's bow shock had been sourced and stored on the
tenth and eleventh of September, with uncertainties, conditions and a cut
angle. Nobody had served them or written the code that turns them into a
shape. So this was a build, not a study.

Both surfaces are now drawn from the store, through eleven served rows,
with no number typed into the renderer. Alongside that, the radiation
belts moved out of the ecliptic and into Earth's equatorial plane, which
was a separate question that Fable's review settled.

---

## WHAT TONY RULED

- **The belts are drawn about the spin axis, in Earth's equatorial plane.**
  The deciding argument is the geostationary ring: it is drawn in that
  plane at 6.6 Earth radii, inside an outer belt served as spanning 3 to 7,
  and the ecliptic put those two 23.4 degrees apart in one picture. The
  magnetic equator would be better but needs a direction as well as an
  angle, and that direction turns once a day while this scene is frozen.
  The spin equator is its daily average. (L-231, full reasoning there.)
- **The magnetopause stops at 120 degrees from the nose.** Shue's surface
  has no end. 120 is the furthest the authors plot their own model, so
  past it we would be drawing something the paper never showed. Declared,
  not measured.
- **If we quote it, it goes in the store.** Earth's dipole tilt was sourced
  to IGRF-13 but lived as a literal in a visualization module. It is now a
  store row, the dipole table reads that row, and the belt hover quotes
  9.6 degrees with its epoch.
- **The hover is the glance; the i panel is the record.** Every citation,
  every model equation and every served caveat left the hover. Each hover
  now ends with one line pointing at the `i` button. Uniform on all of
  them, because that button also carries the link out and people should
  learn where it is.
- **Do not keep cutting.** "We should not remove so much information that
  it is less useful." The hover budget checker's header says so in those
  words, so it is not read later as an instruction to trim.
- **The drawer row becomes one target.** See STILL OPEN item 1.

---

## VERIFIED VS CLAIMED

Verified inside the session:

- The live store-drift run: 70 pointers, 56 match, 0 DRIFT, 1 UNIT
  MISMATCH, 13 could not be examined — the figure written into a patch
  docstring before the run and matched exactly, twice.
- The belt rotation, measured rather than asserted: a flat unit ring
  through `orient_to_planet_pole` comes out 23.439 degrees from the
  ecliptic pole, which is Earth's obliquity, and stays a perfect circle.
- Both surfaces: the nose of each lands on the served standoff to within
  a fifth of a percent, each is drawn to its served cut angle to within
  half a degree, and each is a true surface of revolution about the Sun
  line to about one part in a thousand million. That last leg is the one
  that fails if anyone reintroduces a tilt.
- Every served note reaches the i panel, all four, character for character.
- All seven gating checkers in the gallery runner.
- `ledger_index.py`: 325 blocks, no consistency problems.
- The provenance scanner: Tier-1 never rose.

Claimed and NOT verified from inside the session:

- Every render. The sandbox has no tkinter and no Horizons connection, so
  the desktop orrery was never run here; Tony ran it and reported.
- The i panel showing the citation, the equations and the caveat together.
  The code paths were checked; the panel was not opened by me.

---

## THE LESSON

**A checker exists for the failure you already had, not the one you are
about to have.**

Three times tonight a check passed while the thing it was meant to protect
was broken, and each time the reason was the same shape.

The hover line-WIDTH rule passed on every line of a 32-line hover box that
ran off the bottom of a phone. Narrow and unreadable are different
failures.

The Earth scene checker passed while the fixture it composes from was a
month behind the config — including all four of the served outline colours,
which is why a white-outline finding confused two sessions.

And one leg asserted that every hover carried a "Source:" line, which was
true only because the fixture had no sources in it.

The new hover budget suite is the width rule's missing twin. It failed on
its first run and named two renderers that had been missed, then failed
again because the assembler's traces had been excluded by a name list that
named one of two. It now excludes them by where they came from.

A second lesson, smaller: the run sequence written for Tony had fourteen
steps and did not include rebuilding the served cache. The page reads a
built copy of the config, not the config. Everything was pushed and nothing
appeared, and the live run passed because it compares the served files to
the working copy and both were equally stale.

---

## STILL OPEN

### 1. Three interface changes, decided and unbuilt — START HERE

All three are ruled. None is built. They were confirmed at the end of the
session when there was no room left to build them properly, and a rushed
interface change at the end of a long session is the thing this session
spent its night correcting.

**(a) Move the navigation cluster to the bottom left, above the drawer.**
It lives in `gallery/nav_cluster.js`, NOT in `interactive.html` — the page
only has one rule about it, `body.sun-drawer-open .nav-cluster`. On the
phone it currently sits top right and is drawn ON TOP of the hover box,
blanking words in the middle of five consecutive lines of the magnetopause
hover. Shortening the hover did not fix it and cannot: the box still opens
underneath those buttons.

Two cautions. The comment beside the frame HUD in `interactive.html`
already claims the cluster is on the left and the drawer button in the
centre; either it is stale or something else is going on, and one of the
two is wrong. And the drawer button is already centred but can grow to 92%
of the width, so on a short screen the cluster on the left and the HUD on
the right will face each other across it — check with the longest group
name, which is the Hill sphere row. If it collides, reduce the 92%, not
the cluster's position.

**(b) The drawer row becomes one target.** Today a row has three: a box
that toggles the group, a title that focuses it and makes its text
available, and GO, which moves the camera. A tap that lands on the title
instead of the box does half a job and reads as a failed tap.

Remove the selection box — the colour swatch already carries the state,
dimmed when off. Fold GO's behaviour into the tap rather than dropping it:
GO is the ONLY route to anything outside the arrival frame, and the
magnetopause at 23 Earth radii, the bow shock at 29 and the Hill sphere
are all invisible without it.

**Tony's ruling on the framing:** move the camera only when the thing is
outside the current view. Tapping the crust, already filling the screen,
should not move anything.

**(c) The exhibit's own info text is now false.** `interactive.html` around
line 1515 still tells the visitor the magnetosphere is not drawn yet and
describes what the desktop orrery draws instead.

### 2. The ledger and the master plan were NOT updated

`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` and
`LEDGER_CONSOLIDATED.md` both need this session's work reflected. The
ledger carries L-231's ruling and L-330 already, from a patch applied
mid-session; what is missing is everything after that — the surfaces
shipping, the hover-to-panel move, the hover budget suite, and the three
changes above.

This was not attempted rather than attempted badly: the master plan was
never opened in this session, and writing into a document you have not
read is how stale erratum gets made.

### 3. Lower the hover budget ceiling

It sits at 17, which is the worst hover as things stand (the rotation axis
and equator). It is a ratchet: lower it when the worst comes down, never
raise it. The suite says so every run.

### 4. Carried from before, unchanged

- **L-330**, the belt's shape: thin rings at the sourced peaks versus the
  region between the served edges, which is what the sources actually give.
  Needs Mode 5 on the plane fix first.
- **L-322**, teaching the maintenance checker to read a constant's unit
  from the store's own `# Unit:` line instead of from its name. That
  clears five of the thirteen unexamined pointers and the one unit
  mismatch, and it is also what would let the scanner stop calling two
  declared drawing limits "measured".
- **L-061**, the dipole cone and the magnetosphere in the same rolling
  frame.
- **L-305 item 6b** remainder, and the handoff edits from the review at
  the start of this session, which were agreed and never made.

---

## TONY-ACTION ROLLUP

1. **(do)** Archive the spent patch scripts to `documentation/` in both
   repositories.
2. **(do)** File this handoff to `documentation/`.
3. **(decide)** Nothing outstanding. Every question raised tonight was
   ruled.

---

## ONE THING WORTH KEEPING

Twice tonight a patch stated the result of a run in its own docstring
before the run happened, and both times the run matched exactly. That is
cheap to do and it is the difference between a check and a reassurance.

Written September 2026 with Anthropic's Claude Opus 5.
