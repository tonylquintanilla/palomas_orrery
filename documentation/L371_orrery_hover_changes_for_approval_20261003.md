<!-- Doc-Kind: hand | Every orrery hover line patch_L371_1 changes, old beside new, for Tony's approval before it runs. -->
# The orrery's Sun hovers: what patch_L371_1 changes

Built on orrery 17ef66607cbe63ac5ed7bdbff15397fbe546ae42 at
https://github.com/tonylquintanilla/palomas_orrery. Written October 3,
2026 with Anthropic's Claude Opus 5.5.

Every line below is a line a visitor sees in the orrery. Each number in
a new line is printed from its row in constants_new.py, at the number
of figures its source supports, so none of them is typed any more.

Most hovers also have a matching checkbox tooltip with the same words.
Where that is so, the change is listed once and says "(and its
tooltip)". Lines not listed here do not change.

Please answer with "approved", or name the lines you want changed.

---

## 1. Gravitational Influence (and its tooltip)

The biggest change. The old text gave a range with no source and drew
its midpoint. The new text is your approved note.

Old:
> The Sun's gravitational influence extends to roughly 2.4 light-years (~150,000 AU).
> Published estimates range 100,000-200,000 AU (1.6-3.2 light-years); this visualization draws the midpoint.

New:
> The Sun's Hill radius in the galaxy, calculated where the galaxy's
> tidal pull overtakes the Sun's gravity: about 0.65 parsecs
> (134,000 AU, about 2.1 light-years). Calculated, not measured.

Same hover, first paragraph:

Old: `The Heliopause (120-123 AU):`
New: `The Heliopause (121 AU):`

The shell itself is drawn smaller: at 134,072 AU instead of 150,000.

## 2. Heliopause (and its tooltip)

Old: `Voyager 1 encountered the Heliopause at ~123 AU.`
New: `Voyager 1 encountered the Heliopause at 121 AU.`

This one was wrong, not just rounded: Gurnett et al. (2013) give 121 AU.

Old:
> * The heliosheath extends from ~120 to 150 AU at the Heliopause.

New:
> * The heliosheath lies between the termination shock (94.01 AU) and the heliopause
>   (121 AU), on Voyager 1's path.

The old line was wrong: the heliosheath lies inside the heliopause, not
beyond it. The shell is drawn at 121 AU instead of 121.6.

## 3. Termination Shock (and its tooltip)

Old: `Voyager 1 encountered the Termination Shock at 94 AU, while Voyager 2 at 84 AU.`
New: `Voyager 1 encountered the Termination Shock at 94.01 AU, while Voyager 2 at 84 AU.`

Voyager 2's 84 AU stays typed; it has no row yet.

## 4. Inner Limit of Oort Cloud (and its tooltip)

A new line under the title, your approved note:

> Thought to lie between 2,000 and 5,000 AU; drawn at 2,000.

## 5. Outer Oort Cloud (and its tooltip)

Old:
> Oort Cloud's Outer Edge: At 100,000 AU, it's about 1.58 light-years from the Sun, placing it just
> beyond the nearest star systems and marking the boundary between the Solar System and interstellar space.

New:
> Oort Cloud's Outer Edge:
> Thought to lie between 10,000 and 100,000 AU; drawn at 100,000.
> At 100,000 AU it is about 2 light-years from the Sun, marking the boundary
> between the Solar System and interstellar space.

Two corrections ride along. 100,000 AU is known to one figure, so it is
"about 2 light-years", not 1.58. And "just beyond the nearest star
systems" was wrong: the nearest star is more than twice as far, so that
phrase is dropped.

## 6. Outer Corona (and its tooltip)

Old: `Extended outer solar corona at ~50 solar radii (~0.23 AU).`
New:
> Extended outer solar corona at 50 solar radii (0.23 AU).
> A boundary chosen for the drawing; the faint outer corona has no sharp edge.

The second line is your approved note. Further down the same hover:

Old:
> * Visible streamer belt: drawn at 6.0 R_sun, an approximation
>   (see Streamer Belt shell)

New:
> * Streamer belt: the helmets pinch at 4 R_sun, and the stalk fades out
>   across the Alfven surface (see Streamer Belt shell)

The old line described the streamer belt as it was drawn before August.

## 7. Inner Corona (and its tooltip)

Old: `* Solar Inner Corona (extends to 2-3 solar radii, ~0.014 AU)`
New: `* Solar Inner Corona (extends to 2-3 solar radii; drawn at 3, about 0.01 AU)`

Old: `* The fluid Roche limit for comets (~3.45 R_sun) lies just outside this shell.`
New: `* The fluid Roche limit for comets (about 3 R_sun) lies just outside this shell.`

## 8. Roche Limit (and its tooltip)

The Roche limit is worked out from a comet density known only as
"about 500", one figure. So the answer is good to one figure too. The
shell is still drawn at the full 3.45.

Old: `Result: ~3.45 R_sun (~0.016 AU) from Sun center`
New:
> Result: about 3 R_sun (0.02 AU) from Sun center;
> the comet density is known to one figure, so the result is too.

In the tooltip, the old "~2,400,165 km from Sun center = ~1,704,465 km
from photosphere (~0.0114 AU)" becomes "about 2,000,000 km from the
Sun's center (0.02 AU)", and the MAPS line's "(3.45 R_sun, 0.016 AU)"
becomes "(about 3 R_sun, 0.02 AU)".

## 9. The Sun's own marker (and its tooltip)

Old:
> * Roche Limit: 3.45 R_sun -- tidal disruption threshold for comets
> * Streamer Belt (Visible Corona): drawn at 6.0 R_sun, approximate
> * Extended Corona (F-corona): ~50 R_sun -- faint dust-scattered envelope

New:
> * Roche Limit: about 3 R_sun -- tidal disruption threshold for comets
> * Streamer Belt (Visible Corona): helmets pinch at 4 R_sun, the stalk fades beyond
> * Extended Corona (F-corona): 50 R_sun, a boundary chosen for the drawing

## 10. Streamer Belt band

Old:
> higher than 2-4 R_sun, and the band pinches at 4.0 R_sun
> (2,782,800 km, 0.018602 AU) where they open.

New:
> higher than 2-4 R_sun, and the band pinches at 4 R_sun
> (3,000,000 km, 0.02 AU) where they open.

Old: `past the Alfven surface at 19.7 R_sun` / `(13,705,290 km, 0.091614 AU)`
New: `past the Alfven surface at 19.7 R_sun` / `(13,700,000 km, 0.092 AU)`

The checkbox tooltip's "pinching at the cusp at 4.0 R_sun" becomes
"4 R_sun".

## 11. MAPS comet hovers

The helmet cusp prints as "~4 R_sun, ~0.02 AU" (was "~4.0 R_sun,
~0.019 AU"). The typed "Roche limit (~3.45 R_sun, ~0.016 AU)" becomes
"(~3 R_sun, ~0.02 AU)". The typed "Inner K-corona (~3.0 R_sun, ~0.014
AU)" becomes "(~3 R_sun, ~0.01 AU)". Same in the ghost tail's hover.

## 12. The manual-scale tooltip in the main window

Old: `* Heliopause (edge of the Sun's influence): 126 AU`
New: `* Heliopause (edge of the Sun's influence): 121 AU`

Old: `* Solar Wind Termination Shock: 94 AU`
New: `* Solar Wind Termination Shock: 94.01 AU`

Old: `* Extent of Solar Gravitational Influence (Hill Sphere): 150,000 AU`
New: `* Extent of Solar Gravitational Influence (Hill Sphere): 134,000 AU`

The two Oort cloud lines read as before, 2,000 and 100,000 AU, now
printed from their rows.

---

## Not changed, recorded for later

These hovers type other numbers that have no row yet: Voyager 2's 84 AU,
Sedna's 936 AU, "75 to 100 AU" for the termination shock, the Alfven
surface's "12-15" and "17-19 R_sun", the 15 R_sun field of view, and
several temperatures. The heliopause hover also says both Voyagers are
still in the heliosheath, which stopped being true in 2018. These are
one ledger entry, for a later pass.
