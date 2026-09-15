# For Fable: the radiation belt plane decision (Paloma's Orrery, L-231)

You are being asked for an adversarial review and a recommendation on one
open design decision. Please read the whole brief before answering.

**Write in plain language.** Tony reads these directly and has asked for
ordinary sentences rather than compressed or aphoristic phrasing. Say the
thing rather than naming it. If you use a term of art, gloss it in the same
sentence. File paths, commit hashes and ledger handles like L-231 are fine,
because they can be looked up.

---

## The project, briefly

Paloma's Orrery is a solar system visualization with two faces: a desktop
Python application that renders with Plotly, and a web gallery at
palomasorrery.com with an interactive Earth exhibit. It is a layperson's
learning tool, not a research tool, and that framing has settled several
earlier arguments.

The governing rules that bear on this question:

- The constants store carries value, unit and source. Prose interpolates
  from it; geometry derives from it. No recalled numbers anywhere.
- A value that is a drawing choice rather than a measurement is marked
  "declared" with its reason written out, and the hover text on the page
  has to say which it is.
- Scene equivalence: the desktop and the web page are meant to draw the
  same scene, so a change to one has to land in the other in the same pass.
- Mode 5 is authoritative: what Tony sees on his own screen beats any
  claim or code assertion.
- A drawing approximation does not get promoted to a stored fact.

## The decision

Earth's two Van Allen radiation belts are drawn as rings. Which plane are
those rings in?

Three documents in the project currently give three different answers, and
two of the three already know they disagree.

1. **The served data** (`data/objects_config.json`, the belts block's
   `_frame` note) says the belt edge rows are geocentric distances in the
   **geomagnetic equatorial plane**, which is the frame their sources state.
   Tony's ruling, 2026-09-14.
2. **The web renderer** (`gallery/feature_renderers.js`, the comment at the
   head of `renderBelts`) says the belts are drawn in the **ecliptic plane**
   on purpose, for both Earth and Jupiter, and names scene equivalence with
   the desktop as the reason.
3. **The desktop orrery** (`create_earth_radiation_belts`) builds its points
   in the ecliptic XY plane with a vertical wobble, while its own comment
   claims the belt is built around the planet's **rotational axis**.

So what is drawn is the ecliptic plane in both instruments. What the two
comments claim is two other things, and what the data says is a third.

## What is already settled, and is not up for review

- **The magnetopause and bow shock are NOT tilted.** Both are fitted in
  coordinates aligned to the solar wind, from crossings taken at every
  dipole tilt, so the tilt is already averaged into the published
  coefficients; one study notes it does not move the equatorial
  magnetopause at all. Ruled and built. Do not reopen this. It matters here
  only because it means the same number has opposite answers for two
  different elements of the same scene.
- **The tilt figures are already sourced.** Ledger item L-009, closed
  2026-06-22 and verified in code: all six bodies with a magnetosphere
  carry a sourced dipole cone. Earth's is **9.6 degrees**, Jupiter's 10.3.
  Mercury and Saturn have their dipole within a degree of the spin axis, so
  their cone is degenerate and renders as a plain line rather than as a cone
  claiming a precision it has not got.
- **A separate, uncited 11 degrees exists** in the desktop code, typed at
  the call that rotates the magnetosphere shape. It is already ruled for
  removal. External authorities give 9.41 degrees from the WMM2020 field
  model coefficients and 9.21 from WMM2025 (NOAA), and about 10 (British
  Geological Survey), so 9.6 is in the right neighbourhood and 11 is a stale
  textbook round number.
- **L-231 is the ledger item** that owns this. Tony's recorded correction
  from 2026-08-24: the code comments claiming the rotational axis are not
  false claims about what the code does, they record an intent that was
  never built. So this is a placeholder with a breadcrumb, not a defect.

## The complication that makes this interesting

**The cone precedent.** The reason the orrery draws a cone for each body's
dipole rather than a tilted axis is that *no single orientation is correct
in general* — the magnetic axis turns with the planet, so any one direction
is a picture of one instant. The cone shows the swept envelope instead of
choosing a moment.

**The Earth exhibit is a frozen scene.** It states on the page that it shows
no rotation, and it carries no lighting model; its terminator hover says the
day-night line is frozen. There is no "now" in it to tilt toward.

**L-061, still open.** The dipole cone is locked to the body (spin-pole
frame, Sun-independent). The magnetosphere is locked to the Sun (its axis
follows the planet-to-Sun line). As the planet orbits, the Sun line sweeps
through 360 degrees once per year, so the dipole appears to roll relative to
the magnetosphere once per orbit. Whatever is decided for the belts sits in
the same coupling.

**The belts are served in two different kinds of unit.** The outer belt's
centre is served as an L-shell value of 4.5, and L labels a whole magnetic
shell — it equals a geocentric distance in planet radii only where that
shell crosses the magnetic equator. The hover already says this: the ring is
drawn at that radius because that is the one plane where the two numbers
agree. The belt edges are served in Earth radii, in the geomagnetic
equatorial frame.

## The options as they look from here

Please treat this list as a starting point, not a menu. If there is a fifth
option, say so.

- **A. Leave the rings in the ecliptic plane** and make both comments and
  the served frame note agree with what is drawn, with the hover saying the
  real plane is tilted and turns.
- **B. Draw them in Earth's equatorial plane** (the spin pole), which is
  what the desktop comment claims, and say in the hover that the true
  magnetic plane is a further nine degrees off this.
- **C. Tilt them into the geomagnetic equatorial plane** at the sourced 9.6
  degrees. This needs a direction as well as an angle, and the direction
  turns once a day, so it needs a declared epoch or a declared convention,
  and the hover has to say which.
- **D. Draw a swept band** thick enough to contain the sweep, following the
  cone precedent.

## What I am asking you for

1. **Which document should be made to agree with the other two, and why.**
   That is the actual decision. The rest follows from it.
2. **Does the cone precedent transfer?** A cone is the swept envelope of an
   axis — a line. A belt is a torus. Be concrete about what the swept
   envelope of a tilted torus over one rotation actually looks like, and
   whether drawing it would teach a layperson something true or leave them
   thinking the belt is thicker than it is.
3. **Is any static choice coherent given L-061?** If the dipole rolls
   relative to the Sun-locked magnetosphere once per orbit, does a frozen
   scene have an honest answer at all, or is the honest answer a sentence
   rather than a shape?
4. **What each option's hover text must say** to be honest. One or two
   sentences per option is enough.
5. **Does scene equivalence force the same choice in both instruments?**
   The desktop can animate and the web exhibit is frozen. Is that a reason
   for them to differ, or is differing worse than either choice?
6. **Your recommendation, and what would change your mind.** Name the
   observation or source that would move you off it.

## Please also push back on the framing

If any part of this brief is wrong, loaded, or missing something that would
change the answer, say so first and before anything else. In particular:

- Is "which plane" even the right question, or is the belt's real shape
  poorly served by a ring in any plane?
- Is 9.6 degrees the right figure to be using, given that the underlying
  quantity drifts and the published values disagree at the first decimal?
- Is there a reason the ecliptic plane was chosen originally that this brief
  has not captured, and that would survive scrutiny?

## What I have not given you

I have not sent the papers behind the belt edge rows, the full text of
L-231, L-009 or L-061, or the drawing code itself. If you need any of them
to answer, say which and why rather than guessing. If you can fetch, the
repositories are public:

- orrery: `https://github.com/tonylquintanilla/palomas_orrery` at
  `695f1f04a98a925737df929430567957ad62ccaf`
- gallery: `https://github.com/tonylquintanilla/tonyquintanilla.github.io` at
  `0d8e6044f5a998a2c61b4a515ef5a4fa86cfea7a`

Relevant files: `earth_visualization_shells.py`, `constants_new.py` and
`LEDGER_CONSOLIDATED.md` in the orrery; `gallery/feature_renderers.js` and
`data/objects_config.json` in the gallery.

## One caution

Everything above that is attributed to a ledger item or a code comment was
read from the files. Everything attributed to Tony is his ruling as
recorded. The external tilt figures came from NOAA and the British
Geological Survey. If you find any of it does not match the repositories,
report that as a finding — a brief that misstates its own record is worse
than an unanswered question.
