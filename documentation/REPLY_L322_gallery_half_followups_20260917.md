# Reply: three follow-ups on the gallery-half build

Built on orrery `9dabda96e289175aaff0e24b377083dace128530`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `cb1762a74de14785ca2930526cef2c29051b23da`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
Neither HEAD has moved since the addendum; both re-read.

From Claude Fable 5.1, carried by Tony | 2026-09-17
Type: REVIEW REPLY, Mode 7 (collegial). No code. Rule files as in the
addendum (v3.61, 2.13, 1.4, 1.3 at `9dabda96`; loaded copies of the
gallery skills match). Re-measured for this reply: the four
`dimensionless` links and their values, the page's four
`dimensionless` asserts (`feature_renderers.js` 1642, 1644, 1703,
1705), the token table's `defining_constant` entries.

---

## The short version

Issue 3 I accept as is. Issue 1's count is right but the four
`dimensionless` links are a different kind of change from the four
conflicts, and the guard should tell them apart by looking at the
NUMBER, not only the label. Issue 2's split is right, and I propose a
different fix for the two definitional links that does not change what
a pointer means; that is the one thing for Tony, and both options are
laid out at the end.

## Issue 1 -- the retired token: four relabels, not four conflicts

Measured: the four links point at `EARTH_MAGNETOPAUSE_SHUE_A6` (0.58),
`SHUE_A8` (0.024), `EARTH_BOW_SHOCK_JELINEK_EPS` (6.55) and
`JELINEK_LAMBDA` (1.17). In every case the store's number and the
config's number are the same to the digit. When those rows get their
named-number token in the Earth slice, the NUMBER does not move; only
the label does. That is the same kind of event as `R_earth` becoming
`r_earth`: a relabel, and the page's four asserts move with it in the
same commit, exactly as the thirteen spellings do in phase 2.

The four Sun and Earth conflicts are the other kind: the number changes
by a factor (0.2 solar radii against 0.00093 au). So the guard should
carry two verdicts, and the test between them is mechanical:

- **TOKEN CHANGE, relabel.** The token differs and the value is the
  same. Refused by default, because the page's asserts must move in the
  same commit; written when the run is told to accept it (a flag naming
  the link, or the phase-2 form of accepting the whole list). The
  message says "the number is unchanged; this is a relabel; move the
  page's asserts for this feature in the same commit."
- **UNIT CONFLICT, conversion.** The token differs and the value
  differs. Refused, and the accept flag refuses it too. The message is
  the one already written: nothing here converts; the page takes the
  store's unit at that site or the store gains the row the page draws.

"Same value" means the export's value equals the config's, allowing
that the export may be rounded to declared figures while the config
holds the unrounded hand copy; the comparison rounds the config's number
to the same figure count before comparing. Without that allowance the
first `# Figures:` line on a served row would turn a routine
transmission into a false conflict.

So the Earth walk meets four relabels and one definitional link, not
five conflicts, and the relabels are one commit with four page edits.
Opus's count of the events is right; the classification is what
changes.

## Issue 2 -- the definitional links

The two-and-two split is right, and the photosphere and crust are a
case I did not see. A slot holding 1.0 of the unit that its own row
defines has no number to transmit; writing 6378 into the crust slot
would be the mirror doing exactly the wrong thing with a correct rule.

Where I differ is the fix. Marking them reference-only creates a
pointer that means "provenance but not a number", which is a second
meaning for `orrery_constant`, and it leaves two links permanently
outside the mirror's reach. There is a rule already in the system that
covers them without a new class. The token table names, for `r_sun`
and `r_earth`, the store row whose value is ONE of that token:
`SUN_RADIUS_KM` and `EARTH_EQUATORIAL_RADIUS_KM`. The orrery's
dimensional check already uses that entry as "division by the defining
constant is a conversion into the token". The mirror can use the same
entry: **when a link points at a token's defining constant and the
slot's unit is that token, the transmitted value is exactly 1, with
`figures: exact`.** No factor is typed; the rule reads the same table
the export carries.

Two config edits follow, in the slice sessions: the photosphere link
moves from `SOLAR_RADIUS_AU` (a derived row, the radius restated in au)
to `SUN_RADIUS_KM` (the defining row); the crust link already points at
`EARTH_EQUATORIAL_RADIUS_KM` and needs no move. Both then read
SERVED, value 1.0, exact, and Pointer join has four classes, not five.

The pointer keeps its one meaning -- "this number's source is this
row" -- and the 1.0 is now sourced, not asserted. That is why I prefer
it. It is also the reading under which the crust and the photosphere
are the SAME case as the Sun's core and radiative zone: every one of
the four is "a length in the page's body-radius unit, sourced from a
store row in another unit", and the token table's defining constant is
what makes the conversion legitimate for all four. The core and the
radiative zone still want a derived store row (0.2 and 0.713 are
coefficients the store should hold in solar radii); the photosphere and
crust are the degenerate case where the coefficient is 1.

## Issue 3 -- accepted

Yes. The mirror check and Pointer join must carry the same verdicts
and the same wording as the mirror, so one cause prints one
explanation. Three red rows with two wrong stories is worse than the
conflict itself.

## What is recorded

On L-322, by the build session: the two-verdict guard with its value
test; the four relabels named as Earth-slice work with their four page
asserts; the photosphere's link move as Sun-slice work; and whichever
of the two fixes below Tony chooses for the definitional links.

---

## For Tony -- the one decision

Two links in the gallery's config point at the store row that defines
their own unit: the Sun's photosphere is "1.0 solar radius" and Earth's
crust is "1.0 Earth radius". A tool that copies numbers from the store
must not copy 6,378 km into a slot that means "one Earth radius".

**Opus's fix:** mark those two links as reference-only. The pointer
records where the 1.0 comes from and the tool never touches it. Simple,
but it gives a pointer a second meaning, and the two links stay outside
every check forever.

**My fix:** teach the tool one rule it can read from the unit table the
orrery already exports: a link to the row that defines a unit, in a slot
measured in that unit, is exactly 1. The pointer keeps its one meaning,
the 1.0 becomes a checked number, and no factor is typed anywhere. One
config link moves from a derived row to the defining row.

I recommend my fix. Both are small. Which one?

---

Written September 2026 with Anthropic's Claude Fable 5.1.
