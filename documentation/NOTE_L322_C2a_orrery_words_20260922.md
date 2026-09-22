# What the orrery's own words say before and after Stage C2-a

Built on orrery `efd2e2ba2da47fd01505b1ee9f8bfca4758cee74`
at https://github.com/tonylquintanilla/palomas_orrery.

**Type: WORDS FOR TONY.** September 22, 2026, with Anthropic's Claude
Opus 5. A reworded hover is a visitor-facing change and goes to you
before it ships (orrery-coding-conventions 1.9, Hover Text Is Written
for the Visitor). These are the orrery's own hovers. The GALLERY's
wording is a separate list and comes to you before the gallery patch is
cut, as you asked.

Every line below was taken from the traces the real builders produce,
not read out of the source: the magnetosphere builder and the dipole
cone builder were run on a patched copy and their hover strings
compared against the same builders on the unpatched repository. Six
strings change. No other body's hover moves, and no other Earth hover
moves.

## 1. The two standoffs, in four places

The words do not change. The numbers do, because the rows are computed
again and each declares what it may print.

| Where | Before | After |
| --- | --- | --- |
| Magnetosphere hover | ...reaches about **10.25** Earth radii on the Sun-facing side | ...reaches about **10.3** Earth radii on the Sun-facing side |
| Bow shock hover | ...about **13.51** Earth radii upstream | ...about **13.5** Earth radii upstream |
| The magnetosphere information panel | the same two figures, in its own sentences | the same change |
| The shell configuration table's unused tooltip | the same two figures | the same change |

The last of those is text with no consumer. It is kept in step with its
live twin because a later migration would otherwise promote a stale
copy.

## 2. Earth's dipole cone

| | Before | After |
| --- | --- | --- |
| The cone's own line, one decimal for every planet | Dipole tilt: ~**9.6** deg from the spin axis | Dipole tilt: ~**9.4** deg from the spin axis |
| The note under it | Tilt ~9.6 deg for epoch 2020-2025 (IGRF-13); slowly decreasing ~0.05 deg/decade | Tilt **9.4105** deg at epoch **2020.0** (IGRF-13); decreasing about **0.0493** deg a year |

Three things to know about that note.

**The tilt moved because the old figure was in no epoch of the model the
row cites.** IGRF-13 prints no tilt at all. It prints three coefficients
and says the poles are computed from them, so the store computes the
tilt from them: 9.4105 degrees at epoch 2020.0.

**The drift was out by a factor of ten and in the wrong unit.** The old
note said about 0.05 degrees a decade. The source gives that per YEAR,
and computed from the coefficients and their published rates of change
it is 0.0493 degrees a year.

**The first line still rounds to one decimal.** That line is shared by
every planet's cone and prints one decimal whatever the row declares.
Changing it would change Jupiter's, Saturn's, Uranus's and Neptune's
lines too, so it stays as it is and goes on the list of orrery display
sites that format by a fixed width, for the follow-on.

## 3. What did NOT change, and why

- **The outer belt's "Drawn at the flux peak, L = 4.5" line.** The words
  stay. Its band now prints from two store rows instead of being typed,
  and prints the same "L = 4 to 5" it printed before.
- **"where the measured particle flux peaks"** and the words "flux peak"
  beside a value that is a declared midpoint rather than a measurement.
  That wording is yours to settle and is recorded on the ledger, not
  changed here.
- **Every other Earth hover**: the belts' spans and kilometre figures,
  the magnetotail, LEO, the geostationary ring, the Hill sphere, the
  interior layers and the atmosphere. Measured: unchanged, character for
  character.

---

Written September 2026 with Anthropic's Claude Opus 5.
