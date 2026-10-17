<!-- Doc-Kind: hand | The words list for Earth's round-1 build (L-330, L-314, L-451, L-452, L-450): every visitor-facing sentence and every citation line the build will change, old beside new, for Tony's approval before patches 2 and 3 are built. -->
# Earth round 1: the words, for your approval -- **Tony: notes** -- 

Built on orrery a73bc24 ("patch earth round 1 close") at
https://github.com/tonylquintanilla/palomas_orrery, and gallery f49b3e6
("daily run 10-17-26") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Written October 17, 2026 with Anthropic's Claude Opus 5.5, from the build
brief `documentation/HANDOFF_earth_round1_build_brief_20261016.md`,
section 4.

Rulings this session, before the list: the belts are drawn curved (A),
both of them, as dots scattered at random (Tony, 2026-10-17: "Yes,
random. And it shows the density better too." and, on the inner belt,
"it reads okay"). The run records: stop and name (Tony, 2026-10-17).

HOW TO READ THIS. Each item shows NOW and NEW. Numbers in [square
brackets] are filled in from the store when the text is printed; they
are shown at today's values so the sentence reads. Nothing here ships
until you approve it. Mark any item you want changed by its number.

---

## 1. The radiation belts

### 1a. The orrery's hover (earth_visualization_shells.py)

The sources lines stay as they are, and one is added for the curve.
Kilometres also get AU beside them, which the orrery's convention asks
for and today's belt hover does not have.

**Inner belt, NEW:** -- approved

> Inner Van Allen Belt: Region of trapped charged particles (mainly protons).
> The belt is one continuous region. Its dots follow Earth's magnetic
> field lines, which curve from the equator down toward the ground, and
> they are thickest near the measured proton flux peak, [1.5] Earth radii
> from Earth's centre, about [3,200] km ([0.000021] AU) above the surface
> at the equator.
> At the equator the belt spans about [1.1] to [2] Earth radii -- roughly
> [640] to [6,000] km above the surface (every kilometre figure here
> converted from Earth radii).
> Drawn by choice: the field lines are those of a magnet at Earth's centre
> lined up with its spin axis, the daily average of the tilted magnetic
> field; the belt stops at the ground; and how the dots thin away from the
> peak shows the shape, it is not measured.
> Source (peak): Baker et al. (2018), Space Sci. Rev. 214:17, doi:10.1007/s11214-017-0452-7.
> Source (extent): Meredith et al. (2014), J. Geophys. Res. Space Physics 119:5328.
> Source (field lines): Koskinen and Kilpua (2022), Physics of Earth's Radiation Belts, sec. 1.2.1.

**Outer belt, NEW:** -- approved

> Outer Van Allen Belt: Region of trapped charged particles (mainly electrons).
> The belt is one continuous region. Its dots follow Earth's magnetic
> field lines, which curve from the equator down toward the ground nearer
> the poles, and they are thickest at L = [4.5], about [22,000] km
> ([0.00015] AU) above the surface at the equator, where L equals
> distance from Earth's centre in Earth radii.
> At the equator the belt spans about [3] to [7] Earth radii and moves
> with geomagnetic activity -- roughly [10,000] to [40,000] km above the
> surface (every kilometre figure here converted from Earth radii).
> Drawn by choice: the same field lines, magnet and spin axis as the inner
> belt; the belt stops at the ground; and how the dots thin away from the
> peak shows the shape, it is not measured.
> Source (peak): Li et al. (2025), doi:10.1029/2024JA033504 -- most intense across
> the L = [4] to [5] band; the drawn [4.5] is our midpoint of it.
> Source (extent): Meredith et al. (2014); Li, Tu et al. (2024), doi:10.1029/2023JA032171.
> Source (field lines): Koskinen and Kilpua (2022), Physics of Earth's Radiation Belts, sec. 1.2.1.

NOW, for comparison, both open: "The belt is one continuous region. The
rings only mark its extent: they are evenly spaced from its inner edge to
its outer edge, and the brighter ring is ..." The rest is unchanged apart
from the AU. -- unclear, we are no longer using a brighter ring, but a continuouis density field.

### 1b. The website's words for the belts (served, so they reach a visitor after the next Daily Run)

**1b-1. Description, inner.** NOW: "A ring of trapped charged particles,
mostly protons, held by Earth's magnetic field close above the
atmosphere." NEW: "A belt of trapped charged particles, mostly protons,
held by Earth's magnetic field close above the atmosphere." -- approved

**1b-2. Description, outer.** NOW: "A broader ring of trapped electrons
farther out, that swells and shrinks with solar storms." NEW: "A broader
belt of trapped electrons farther out, that swells and shrinks with solar
storms." -- approved

**1b-3. About, inner** (the i panel). NOW: "... It follows the magnetic
equator, which is tilted from the geographic one and turns with Earth
once a day; the ring drawn here lies in the daily average of that
plane." NEW: "The inner Van Allen belt is a region of energetic protons
trapped by Earth's magnetic field. The particles are held along the
field lines, so the belt curves down toward the ground on either side of
the equator. The real field is tilted from Earth's axis and turns with
Earth once a day; the belt drawn here follows the field's daily average,
lined up with the spin axis." -- approved

**1b-4. About, outer.** NOW: "... Like the inner belt it follows the
magnetic equator; the ring drawn is the daily average of that tilted
plane." NEW: "The outer Van Allen belt is mostly energetic electrons,
trapped farther out than the inner belt, and it swells and shrinks as the
solar wind changes. Like the inner belt it is held along the field lines,
which meet the ground nearer the poles; it is drawn around the field's
daily average, lined up with the spin axis." -- approved

**1b-5. The shape line** (replaces "hovers_rings", same for both belts).
NOW: "The belt is one continuous region; its evenly spaced rings only mark
its extent, and the brighter ring marks where it is most intense." NEW:
"The belt is one continuous region. Its dots follow Earth's magnetic
field lines, which curve from the equator down toward the ground, and
they are thickest where the belt is most intense. How they thin out is
drawn to show the shape, not measured." -- approved

**1b-6. The outer belt's peak line** ("hovers_band"). NOW: "Drawn at
[4.5] Earth radii: halfway across the band, ..." NEW: "Thickest at [4.5]
Earth radii: halfway across the band, [4] to [5] Earth radii out at the
magnetic equator, where the belt is most intense. The halfway point is
our choice for the picture, not a measured peak." (Only the first two
words change.) -- approved

**1b-7. The inner belt's peak line** (typed in the page, a number's
label). NOW: "Drawn at [1.5] Earth radii from Earth's centre, at the
magnetic equator: near where the measured flux of trapped protons is
greatest." NEW: "Thickest at [1.5] Earth radii ..." (only the first two
words change). -- approved

**1b-8. The plane line** ("hovers_plane", both belts). NOW: "The ring lies
in Earth's equatorial plane, the daily average of the magnetic equator,
which turns with Earth and in 2020 was tilted [9.4105] degrees from it,
shrinking [0.0490] degrees a year (IGRF-13 model)." NEW: "The field lines
are drawn around Earth's spin axis: the daily average of the magnetic
field, which turns with Earth and in 2020 was tilted [9.4105] degrees
from it, shrinking [0.0490] degrees a year (IGRF-13 model). The belt
stops where its field lines meet the ground." -- approved

**1b-9. The i panel's line for the curve** (new). "Field lines: Koskinen,
H. E. J. and Kilpua, E. K. J. (2022), Physics of Earth's Radiation Belts,
Springer, open access, sec. 1.2.1, The Dipole Field." Where this line is
stored is settled in the build; these are its words. == approved

---

## 2. The aberration sentence (L-314), both instruments

One sentence added to each hover. No number in it.

**2-1. Magnetopause** (the orrery's Magnetosphere hover, after "The
Sun-facing surface is the model's own shape ..."; the website's
magnetopause hover, after "Not tilted: the model is symmetric about the
Sun line."):

> It is drawn along the line from the Sun to Earth; the real boundary's
> nose is turned a few degrees toward the direction Earth moves in its
> orbit, by an amount that depends on the solar wind's speed. -- approved

**2-2. Bow shock** (the orrery's Bow Shock hover, after "The XY plane is
the ecliptic."; the website's, after "Not tilted: the fit is symmetric
about the Sun line."):

> It is drawn along the line from the Sun to Earth; the real shock's nose
> is turned a few degrees toward the direction Earth moves in its orbit,
> by an amount that depends on the solar wind's speed. -- approved

Source: the Shue et al. (1998) and Jelinek et al. (2012) rows, whose fits
are made in frames turned this way. On the website both hovers are at the
17-line limit, so other lines in them are refitted rather than the limit
raised; you will see the result at Mode 5. 

---

## 3. The sentences the Typed facts check holds (L-451)

**3-1 to 3-5. Served, words unchanged.** Their text stays exactly as it is
today; only where it lives changes (from the page's code to each
feature's served words, beside the source of its number):
1. "Tilt: [#] deg on [date], measured against the orbit of the Earth-Moon
   barycenter, the gravitational center of the Earth-Moon system, around
   the Sun that day (JPL Horizons)."
2. "Earth turns once every [#] hours measured against the stars."
3. "Spacecraft found the tail stops widening about [#] Earth radii behind
   Earth, plus or minus [#], and is about [#] Earth radii wide beyond
   there, plus or minus [#]."
4. "Spacecraft that cross the real boundary typically find it within [#]
   Earth radii of this model."
5. "Spacecraft that cross the real shock typically find it within [#]
   Earth radii of this model."

**3-7. The Sun room's description, reworded.** NOW: "Nobody has measured
those, and where that is so, the text says so." NEW: "Where that is so,
the text beside it says so." -- approved

**3-8. Earth's description, cut.** "The radiation belts sit in Earth's
equatorial plane, the daily average of the tilted magnetic equator they
follow." is removed. (Sentence 6 stays as it is.) -- approved

---

## 4. The website's 35 notes beside a citation (L-452)

Your rule: wording that bears on the citation moves to the store; a note
stays only if it describes a drawing choice. Three outcomes below: DROP
(the citation already says it, or it moves to the store), KEEP (a drawing
choice, sometimes reworded so it says only that), and what moves where.
The notes are in the order they sit in the config.

**The Sun room**

4-1. Streamer belt, cusp radius. NOW: "extent of the closed-field helmet,
not of the streamer as a whole". DROP: the store's row already says this
(its Note). NEW NOTE, a drawing choice moved out of the citation (see
5-1): "drawn at the top of that range, so the drawn cusp does not
understate the helmet". -- approved

4-2. Streamer belt, fade radius. "the band dissolves across the Alfven
surface". KEEP (how it is drawn). -- approved

4-3. Inner corona. NOW: "the inner solar corona taken as extending to
about 3 R_sun ... A stated convention, not a measurement: the inner
(K-)corona has no sharp edge, and 3 R_sun is the top of the 2-3 R_sun
band ...". The first part repeats the citation and the band is already in
the store; DROP those. KEEP, reworded to the drawing choice with no typed
number: "The inner corona has no sharp edge; the shell is drawn where the
cited work takes it to end." The arXiv number the website once had moves
into the citation (5-3). -- approved. draw as a fuzzy boundary? 

4-4. Alfven surface. NOW: "first Parker Solar Probe crossing, 28 April
2021". DROP: the citation already gives the date; the spacecraft's name
moves into it (5-2). -- approved

4-5. Hills cloud, tilt. Repeats its citation. DROP. -- approved

4-6. Hills cloud, where the disk thins. Repeats its citation. DROP. -- approved.

4-7. Hills cloud, inner radius; and 4-15, the inner Oort limit. NOW: "the
inner edge is thought to lie between 2,000 and 5,000 AU; drawn at the
near end". KEEP the drawing choice only: "drawn at the near end of that
range". -- approved

4-8. Outer cloud, inner radius; and 4-11, galactic tide, inner radius.
NOW: "the outer Oort cloud at r > 10,000 au is roughly spherical; it
begins here, thin, where the inner cloud's disk thins out". KEEP the
drawing choice only: "drawn beginning here, thin, where the inner cloud's
disk thins out". -- approved. draw as a fuzzy boundary?

4-9. Outer cloud, full from; and 4-12, galactic tide, full from. NOW: "the
inner edge of the Oort cloud, about 20,000 AU or less; the far end of the
band, by which the outer cloud is full". KEEP the drawing choice only:
"the far end of the band, by which the drawn outer cloud is full".

4-10, 4-13, 4-14, 4-16. Outer radius (outer cloud, galactic tide,
galactic plane ring, outer Oort). NOW: "the outer edge is thought to lie
between 10,000 and 100,000 AU; drawn at the far end". KEEP the drawing
choice only: "drawn at the far end of that range". -- approved

4-17. The Sun's Hill radius in the Galaxy. Repeats its citation word for
word. DROP. -- approved

**The Earth room**

4-18. Lower mantle. NOW: the Ishii et al. (2019) and Ishii et al. (2018)
attribution. DROP: it moves into the 660 km row's citation, which today
names no work (5-6). -- how do we cite the boundary? clarify.

4-19. Upper mantle. NOW: "Moho". The citation already says Mohorovicic
discontinuity. DROP. -- approved

4-20. Crust. NOW: "volumetric mean radius, 6371.000 km. The Earth radius
used as a unit is the equatorial radius: Prsa et al. (2016) ...". The
first part repeats the citation; the second is a citation for the unit,
and moves to the mean-radius row's notes in the store. DROP. (The crust's
own note and radius note, which describe the drawing, stay: see 6-1.) -- approved.

4-21. Lower atmosphere. NOW: "stratopause at about 50 km". Repeats its
citation. DROP. -- approved

4-22. Low Earth orbit, inner edge. NOW: "Drawing floor: the LEO region
begins at the surface (IADC-02-01 Rev. 3); 200 km marks where orbits stop
decaying within days. Declared, not measured." KEEP, reworded, with the
wrong revision gone and no typed number: "The region begins at the
surface; the inner edge is drawn higher, our choice for the picture, where
orbits stop decaying within days." -- no numeric boundary? unclear. 

4-23. Geostationary ring. NOW: the derivation, which names the wrong table
for the angular velocity (it is Table 1.2), and the NASA Earth Observatory
source for the hover's sentence about keeping pace with Earth. DROP. The
derivation is already the row's; the NASA page moves to the row's notes in
the store. One consequence to know: the i panel will then show the two
IERS citations the number is worked out from, and not the NASA page. The
keeping-pace sentence follows from how the number is worked out (one
orbit per turn of Earth), which those citations carry. -- approved

4-24. Magnetopause. NOW: "eq. 10 evaluated at the declared conditions (Bz
= 0 nT, Dp = 2 nPa). Corroboration: Lugaz et al. (2016) ...". KEEP the
drawing choice, with no typed numbers: "Shue's eq. 10, worked out at the
solar wind chosen for the picture." The corroboration is already in the
store. DROP the rest. -- appro ed

4-25. Magnetopause, a7. Repeats its citation. DROP. -- approved

4-26. Bow shock. NOW: "eq. 14 ... evaluated at the declared pressure of 2
nPa. The paper states no uncertainty ...; Corroboration: Lugaz et al.
...". KEEP the drawing choice: "Jelinek's eq. 14, worked out at the solar
wind pressure chosen for the picture." The rest is already in the store.
DROP. -- approved

4-27. Bow shock, r0. Repeats its citation. DROP. -- approved

4-28. Bow shock, lambda. NOW: repeats the citation, plus why the
magnetopause's lambda is not used. DROP; the reason moves to the store
(5-12). -- approved

4-29. Magnetotail, observed extent. NOW: repeats, plus the abstract's open
address, plus that its flaring and diameter figures are superseded. DROP:
the address moves into the citation, and the superseded figures move out
of it (5-13). -- approved

4-30. Magnetic tilt. NOW: a long note -- what the angle is, how it is
computed, its yearly change, why the dipole turns with Earth, and a
history of the note's own errors. DROP. Each part is already in the store
or moves there (5-14); the history goes. -- approved

4-31. Inner belt, inner edge. NOW: repeats, plus "Open full text at
nora.nerc.ac.uk", plus the layer below. DROP: the address moves into the
citation (5-15); the layer below is already in the store. -- approved

4-32. Outer belt, peak. NOW: "sec. 1, the outer belt is most intense
around L = 4 and 5; the value served is our midpoint of that band.
Kellerman et al. ...". KEEP the drawing choice only: "the value drawn is
our midpoint of that band". The rest repeats the citation. -- approved

4-33. Outer belt, inner edge. NOW: repeats, plus "Open full text at
nora.nerc.ac.uk and par.nsf.gov". DROP: the addresses move into the
citation (5-15). -- approved

4-34. Earth's Hill sphere. The derivation and its sources: already the
row's. DROP. -- approved

4-35. Rotation period. The derivation: already the row's. DROP. -- approved

Not one of the 35: the Solar System room's Pluto row note, "the
Pluto-Charon barycenter", says what the drawn point is. It stays. -- approved

Count: 35 notes. KEEP 17 (4-1 as new words, 4-2, 4-3, 4-7 to 4-16, 4-22,
4-24, 4-26, 4-32 -- most of those cut down to the drawing choice); DROP
18. -- approved

---

## 5. The citation lines in the orrery's store (constants_new.py)

What a visitor reads in the i panel is each row's `# Source:` text, word
for word. These edits take store notes out of it and put citation words
into it. A note taken out goes to the row's other comment lines; nothing
is lost from the store.

**A. The rows L-450 names**

5-1. HELMET_CUSP_RADII. Take out "4.0 is the TOP of that stated range,
chosen so the drawn cusp does not understate the helmet." (The row's
Declared line already says it; the website gets it as 4-1's note.) -- approved

5-6. EARTH_D660_DEPTH_KM. The citation names no work today. NEW: "Ishii,
T., Huang, R., Fei, H. et al. (2018), "Complete agreement of the
post-spinel transition with the 660-km seismic discontinuity", Sci. Rep.
8:6358, doi:10.1038/s41598-018-24832-y -- section "New results of the
post-spinel transition pressure in complete agreement with the
discontinuity depth": the global average depth of the discontinuity is
660 +/- 10 km." The ringwoodite sentence moves to a Note line; the "2 sig
figs" aside goes (the Figures line has it); Ishii et al. (2019) stays on
the Ref line. I re-read the open copy today
(https://pmc.ncbi.nlm.nih.gov/articles/PMC5910398) and confirmed the title,
authors, DOI and sentence. -- approved

5-7. EARTH_EQUATORIAL_RADIUS_KM. Take out "IAU B3 rounds to 6378.1 km"
(the row's Note already explains B3). This also cleans the citation the
low-orbit and lower-atmosphere entries inherit. -- clarify

5-8. EARTH_GM_KM3_S2. Take out "Converted to km^3 s^-2 here." to a Note
line. This also cleans the geostationary ring and Earth's Hill sphere,
which inherit it. -- clarify

5-9. The IADC edition. The rows already cite Revision 2, March 2020, and
that is the document that was read (2026-09-19). They stay. The website's
"Rev. 3" goes with note 4-22. See also 5-17. -- approved

**B. The same kind, found on other served rows** (not named in L-450;
included because they are the same fault and this is the one pass through
the file) -- clarify

5-2. ALFVEN_SURFACE_RADII. Add the spacecraft: "-- Parker Solar Probe's
first crossing, 28 April 2021 09:33 UT; ..." (from note 4-4). -- approved

5-3. INNER_CORONA_RADII. Add "arXiv:2009.04820" after the title (from the
website's old citation; the row's Access line already has it). -- approved

5-4. HILLS_CLOUD_TILT_DEG and INNER_OORT_DISK_OUTER_AU (Nesvorny et al.).
Add the address the website had, https://arxiv.org/pdf/2502.11252v1 (each
row's Access line already has it). -- approved

5-5. HELMET_CUSP_LOW_RADII and HELMET_CUSP_HIGH_RADII. Take out "This row
is the low end." and "This row is the high end." to Note lines. A fault
this fixes: the high row's citation points at the low row's, so a visitor
reads "This row is the low end. This row is the high end." today. -- clarify

5-10. EARTH_POLAR_RADIUS_KM. Take out the worked check against IERS and
"Corrected 2026-09-19: ..." to Note and Corrected lines. -- clarify

5-11. EARTH_INNER_CORE_KM, EARTH_OUTER_CORE_KM, EARTH_UPPER_MANTLE_KM.
Take out "(5 sig figs)" and "(4 sig figs)" (the Figures lines have them).
The upper mantle's "i.e. 24.4 km below the mean radius" moves to a Note
line. -- clarify

5-12. EARTH_BOW_SHOCK_JELINEK_LAMBDA. Take out "(1.54 for the
magnetopause, which this file does not store because the magnetopause is
Shue's)" to a Note line. -- clarify

5-13. EARTH_MAGNETOTAIL_OBSERVED_RADII. Add the abstract's address,
https://ntrs.nasa.gov/citations/19830066648. Move "that flaring ceases at
100-120 R_E, and that the tail diameter settles near 60 R_E" out to the
Note line, which already says those two figures are superseded; a
visitor otherwise reads figures the room does not use. -- approved

5-14. EARTH_DIPOLE_TILT_DEG. Take out "these coefficients reproduce it as
80.6512 N, -72.6797 E (read 2026-09-21 by Claude Opus 5)" to a Note and a
Read line. The citation keeps the paper, the relation and the pole Table
4 prints. -- clarify

5-15. Meredith et al. (2014) on EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE and
EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE: add the open copy,
https://nora.nerc.ac.uk/id/eprint/507469/1/jgra51120.pdf; on the outer
row also Li, Tu et al.'s, https://par.nsf.gov/servlets/purl/10578577 (from
notes 4-31 and 4-33; the Access lines have both). -- clarify

5-16. EARTH_VAN_ALLEN_INNER_RADII. Take out "Geocentric, equatorial, which
is the frame this row is in." to a Note line. -- clarify

5-17. EARTH_LEO_UPPER_ALTITUDE_KM. Take out "as this file does" and the
"Corrected 2026-09-19: ..." history to Note and Corrected lines. The
revision, section and wording stay. -- clarify

5-18. EARTH_ROTATION_RATE_RAD_S. Take out "Corrected 2026-09-19: the old
line said Table 1.1 ..." to a Corrected line. -- approved

5-19. EARTH_VAN_ALLEN_OUTER_BAND_LOW_L and _HIGH_L. Take out "This row is
the lower/upper end of that band." and, on the low row, the two
corroborating papers with "were not re-read here" to an Also line: they
were not re-read, so they should not print as the citation. The high
row's "Corroborated as the row above." goes with them. -- clarify

5-20. EARTH_MAGNETOPAUSE_SHUE_A7_PER_NT. Take out "Eq. 11 prints it as
the subtraction ...; the table carries the sign, so the stored coefficient
is negative and adds." to a Note line. -- clarify

5-21. EARTH_MEAN_RADIUS_KM. Its Note line gains the Prsa et al. (2016)
sentence from note 4-20. (A note, not the citation.) -- clarify

5-22. EARTH_GEOSTATIONARY_RADIUS_KM. Its notes gain the NASA Earth
Observatory page from note 4-23. (A note, not the citation.) -- clarify

---

## 6. Two served notes with project words in them

6-1. The crust's note (L-452 named this one). NOW: "Drawn at the mean
radius, the sphere the interior layers (PREM) are measured against (Tony,
2026-09-28). ..." NEW: the same without "(Tony, 2026-09-28)". -- clarify

6-2. The bow shock's note (found while reading; the same kind). NOW:
"Quiet-time nominal, at the same declared solar wind pressure as the
magnetopause. An earlier note here cited Farris & Russell (1994) for the
model FORM; that was a miscitation ... Removed 2026-09-12 (L-305)." NEW:
"For a quiet solar wind, at the same pressure as the magnetopause." The
history is already in the store, on the bow shock row. -- approved

---

Written October 17, 2026 with Anthropic's Claude Opus 5.5.
