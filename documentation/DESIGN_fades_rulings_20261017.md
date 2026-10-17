<!-- Doc-Kind: hand | Design record: Tony's rule for fuzzy boundaries (a fade only where nature thins out), replacing L-410's range idea, and the design of Earth's hydrogen fade, the exosphere from 3 to 100 Earth radii. Zero code. -->
# Design record: fades where nature thins out, and Earth's hydrogen fade

Built on orrery da78b80fc7cf38c87d9d32d5b491b58023777561 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
f49b3e6974cc1183fe8f64f24878d6e2b6f540f2 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION (zero code), held at the end of the Earth round-1
build session, October 17, 2026. The rulings are recorded on L-410
(fades), L-454 (the moving-edge device) and L-413 (Earth's list). This
record is the reasoning; the ledger is the status.

## 1. The rule (Tony, 2026-10-17)

A boundary is fuzzy in a drawing for one of three reasons, and each is
drawn its own way:

1. **Nature thins out and has no edge** (the inner and outer corona, the
   geocorona, the upper atmosphere into the exosphere, the Oort cloud's
   outer reaches). Drawn as a FADE: dots growing sparser across a band.
2. **A real edge that moves** (the magnetopause, the bow shock, the
   Alfven surface, the heliosphere's edges). Drawn sharp at the model,
   with a SECOND DRAWN DEVICE for the motion, like the dipole cone that
   shows every direction the dipole could point. Its own design talk
   (L-454).
3. **An edge known only as a range** (the Oort cloud's inner edge, 2,000
   to 5,000 AU; the helmet cusp, 2 to 4 solar radii). Drawn as a CHOICE
   with an explanation, as today: the drawing takes one value and the
   words say which end and why. Not a fade.

Edges that are sharp by definition stay sharp (the Hill sphere, low
Earth orbit's 2,000 km, the geostationary ring).

Tony, in his words: "Primarily 1. Because I don't think we should
illustrate uncertainty (3) with a fuzzy boundary rather with a drawn
choice and an explanation, and motion (2) with a second drawn device
like the movement cone we use for the dipole."

"Where meaningful" (his ruling of 2026-10-14) is read as two tests: the
fade is wide enough to see at the scale the room is drawn, and showing
it teaches something a sharp line hides.

**It replaces L-410's range idea.** L-410 (opened 2026-10-04) proposed
that an edge given as a range becomes a band fading between its two
ends. Asked whether today's rule replaces that, Tony: "Yes it replaces
the range idea. Those examples still have fades." So the inner corona
and the Oort cloud still fade, because nature thins there; the range of
an edge is said in words, not drawn as the fade.

The kind-1 list, confirmed ("This sounds right for type 1"): the inner
corona, the outer corona, the geocorona, the upper atmosphere into the
exosphere, and the Oort cloud's outer reaches (partly done: the outer
cloud already starts thin and fills in, L-421).

A fade has a shape: how fast it thins. Where a measured fall-off exists
the fade follows it; where none does, the shape is a drawing choice and
the hover says so, as the belts' hover does.

## 2. The split (Tony: "I agree")

- Designed now: Earth's fade, wholly Earth's and wholly kind 1.
- Later: the moving-edge device (L-454), beside Earth's talk 2 on the
  field (L-356 with L-375), since both are about Earth's magnetic field
  and how it moves.
- The Sun's fades (the inner and outer corona, with the dust cloud,
  L-131) wait for the Sun room's turn, as L-410's order already says.

## 3. Earth's hydrogen fade, as designed

1. **Where it starts: 3 Earth radii** (Tony: "A. As Recommended").
   Measurements begin there. The upper atmosphere's shell at 600 km
   (about 1.1 Earth radii) stays as it is. The hover says the hydrogen
   continues inward but the profile was measured from 3 Earth radii out.
   Declined: carrying the fit inward to 600 km.
2. **Where it stops: 100 Earth radii,** the existing row
   `EARTH_GEOCORONA_RADII`, Baliukin et al. (2019)'s detection floor.
   The geocorona's sharp shell at 100 goes; the dots stop there, and the
   hover says that is where instruments lose the hydrogen, not where it
   ends.
3. **How fast it thins.** From 3 to 15 Earth radii, Zoennchen et al.
   (2022)'s fitted day-side profile. Beyond 15, thinning with the cube of
   distance, the rate they measured above about 8 Earth radii, carried
   out to 100. Baliukin et al. (2019)'s two densities as ESA reports them
   (about 70 atoms per cubic centimetre 60,000 km above the surface,
   about 0.2 at the Moon's distance) fall at that rate or a little
   faster. Only the shape of the thinning is drawn, not a density: the
   two papers differ by about a factor of two at 10 Earth radii and
   agree on the rate. Dots following a density that falls with the cube
   of distance put about the same number in each tenfold step outward,
   so the drawing thins visibly but stays present to 100.
4. **Round.** The profile is the day side's. Asked whether to turn the
   hydrogen like Mercury's sodium tail, Tony asked for the search first
   ("Let's look so B"). Found: three TWINS studies (Zoennchen et al.
   2010, 2015, 2024) measure a day-night difference between about 3 and
   6 to 8 Earth radii -- a night-side excess first, shifted toward dawn
   in 2015, and in 2024 a Sun-side bulge 20 to 50% denser than its
   surroundings with a weaker night-side tail; beyond 6 Earth radii the
   2024 model held its shape fixed. Small against the thousandfold fall
   in density, not one shape, measured over a short stretch. Ruled
   (Tony: "I agree. As recommended"): drawn round; the hover says the
   hydrogen is measured somewhat denser along the Sun-Earth line on both
   the day and night sides, which the drawing does not show, citing the
   2024 study.
5. **Built as a stored drawing** (L-434's rule for scattered dots): the
   orrery places the dots once from rows in `constants_new.py`, the
   website draws them as given, as the belts are built (L-330).

## 4. Sources, as found this session (each to be read in full before its row is written)

- Zoennchen, J. H., Connor, H. K., Jung, J., Nass, U. and Fahr, H. J.
  (2022), "Terrestrial exospheric dayside H-density profile at 3-15 RE
  from UVIS/HDAC and TWINS Lyman-alpha data combined", Ann. Geophys.
  40:271, open, https://angeo.copernicus.org/articles/40/271/2022/ --
  sec. 6, eqs. 7 to 9 as a page summary gave them: the density about 35
  per cubic centimetre at 10 Earth radii, falling about as r^-2.37 below
  8 Earth radii and r^-3 above.
- Baliukin et al. (2019), J. Geophys. Res. Space Physics 124:861-885,
  doi:10.1029/2018JA026136 (already the geocorona row's Source); the two
  densities from ESA's article on it,
  https://www.esa.int/Our_Activities/Space_Science/Earth_s_atmosphere_stretches_out_to_the_Moon_and_beyond
  -- the paper itself was not reachable this session (its HAL copy
  refused the reader).
- Zoennchen et al. (2010), Ann. Geophys. 28:1221; (2015), Ann. Geophys.
  33:413; and Zoennchen, Cucho-Padin, Waldrop and Fahr (2024), Front.
  Astron. Space Sci. 11:1409744 -- the day-night asymmetry.

Read through a page summary only, 2026-10-17, Claude Opus 5.5. Every
number above goes into the store only after a full read, by
provenance-discipline.

Written October 17, 2026 with Anthropic's Claude Opus 5.5.
