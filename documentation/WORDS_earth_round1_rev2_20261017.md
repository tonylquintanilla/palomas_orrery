<!-- Doc-Kind: hand | Revision 2 of Earth round 1's words list: answers to Tony's "clarify" marks, each shown as what a visitor reads today and after; items he approved are listed by number. Read with WORDS_earth_round1_20261017.md. -->
# Earth round 1: the words, revision 2 -- answers to your marks

Built on orrery a73bc24 ("patch earth round 1 close") at
https://github.com/tonylquintanilla/palomas_orrery, and gallery f49b3e6
("daily run 10-17-26") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Written October 17, 2026 with Anthropic's Claude Opus 5.5, answering
Tony's marks on `documentation/WORDS_earth_round1_20261017.md`
(revision 1). Item numbers are revision 1's.

APPROVED AS WRITTEN (your marks, 2026-10-17): 1a inner and outer, 1b-1
to 1b-9, 2-1, 2-2, 3-7, 3-8, 4-1 to 4-8, 4-10 to 4-17, 4-19 to 4-21,
4-23 to 4-35, the Pluto row, the count, 5-1, 5-2, 5-3, 5-4, 5-6, 5-9,
5-13, 5-18, 6-2. Sentences 3-1 to 3-5 keep today's words; nothing to
approve there.

Below: first, how a citation reaches a visitor, which is what most of
your marks asked. Then each marked item, shown as what a visitor reads
today and after.

---

## 0. How a citation reaches a visitor

Every number the website shows has a Source line in its i panel (the
panel that opens beside the picture).

1. That Source line is copied, word for word, from ONE comment line on
   the number's row in the orrery's `constants_new.py`: the line that
   starts `# Source:`.
2. All the OTHER comment lines on that row -- `# Note:`, `# Read:`,
   `# Corrected:`, `# Figures:`, `# Access:`, `# Also:` -- stay in the
   orrery. A visitor never sees them. They are our working record.
3. When a number is worked out from other rows, its Source line is
   those rows' Source lines, one after another, joined by semicolons.
   The geostationary ring, for example, shows the citation for Earth's
   GM and then the one for Earth's spin rate.
4. After the Source line the website may print a short note of its own,
   after a dash. That is `source_note`. Under your rule, from now on it
   only says what we chose for the drawing.

So the work in sections 4 and 5 is sorting: words a visitor should read
belong in `# Source:` (or the drawing note); words that are our own
bookkeeping belong in the other lines, where nothing is lost and a
visitor is not confused by them. "Bookkeeping" means things like "this
row", "this file", "here", how many figures we counted, and the history
of our corrections.

---

## 1. Your marks, answered

### 1a, "unclear" (the NOW text)

The quoted "NOW" text is TODAY's wording, about rings. It is what the
new text replaces. The new hovers you approved say nothing about rings
or a brighter ring; they describe the dots. No change needed.

### 4-3 and 4-8, "draw as a fuzzy boundary?"

That is a new design question: changing how the inner corona's edge and
the outer Oort cloud's start are drawn. It is outside this build. I will
record it in the ledger at the close for a later design talk, unless you
want it now. The words you approved fit either drawing.

### 4-9, no mark

"the far end of the band, by which the drawn outer cloud is full". It is
the same kind as 4-8 and 4-10. Please include it in your approval below.

### 4-18, "how do we cite the boundary?"

The lower mantle's top is drawn at Earth's mean radius minus the depth
of the 660 km boundary. Two numbers make it, so the i panel cites both:
the NASA fact sheet for the mean radius, then the paper for the depth.
Today the depth's citation names no paper; the paper is only in the
website's note.

Visitor reads TODAY:
> Source: NASA Planetary Fact Sheet, Earth -- volumetric mean radius; the
> 660-km seismic discontinuity, ringwoodite dissociating to bridgmanite
> plus ferropericlase; global average depth 660 km (2 sig figs -- the
> trailing zero is not significant). -- Ishii, Huang, Myhill et al.
> (2019), Nature Geoscience 12:869-872 -- the sharp 660-km discontinuity;
> the global average depth of 660 +/- 10 km is from the same group's open
> companion, Ishii et al. (2018), Scientific Reports 8:6358

Visitor reads AFTER:
> Source: NASA Planetary Fact Sheet, Earth -- volumetric mean radius;
> Ishii, T., Huang, R., Fei, H. et al. (2018), "Complete agreement of the
> post-spinel transition with the 660-km seismic discontinuity", Sci. Rep.
> 8:6358, doi:10.1038/s41598-018-24832-y -- section "New results of the
> post-spinel transition pressure in complete agreement with the
> discontinuity depth": the global average depth of the discontinuity is
> 660 +/- 10 km.

Kept in the orrery only: the mineral sentence (ringwoodite ...), as a
Note; Ishii et al. (2019), on its Ref line.

### 4-22, "no numeric boundary? unclear"

The number IS shown: the shell's name reads "Low Earth Orbit, inner edge
(200 km)", and the 200 km is served from its own row beside it. The
note does not type it again, because a typed copy is a second store of
the number.

But your mark made me read the note's reason again. "Where orbits stop
decaying within days" is a claim about nature, and nothing in the store
sources it. So I now propose dropping that reason:

NEW (replaces revision 1's wording): "The region begins at the surface;
the inner edge is drawn higher, at a height chosen for the picture."

### 5-7, Earth's equatorial radius

Shown in the i panel of the low-orbit edges and the lower atmosphere, as
well as the radius itself.

TODAY: "IERS Conventions (2010), Petit & Luzum (eds.), IERS Technical
Note No. 36, Table 1.1; IAU B3 rounds to 6378.1 km"
AFTER: "IERS Conventions (2010), Petit & Luzum (eds.), IERS Technical
Note No. 36, Table 1.1"

Why: "IAU B3 rounds to 6378.1 km" is our remark that another body rounds
the number differently. It is not part of what IERS says. The row's Note
already explains it.

### 5-8, Earth's GM

Shown in the i panel of the geostationary ring and Earth's Hill sphere.

TODAY: "... geocentric gravitational constant GM_E = 3.986004418e14 m^3
s^-2 (uncertainty 8e5 m^3 s^-2). Converted to km^3 s^-2 here."
AFTER: the same, ending at "(uncertainty 8e5 m^3 s^-2)."

Why: "here" means our file, which stores the number in km^3 s^-2. To a
visitor "here" points nowhere. It becomes a Note: "The table gives m^3
s^-2; this row stores km^3 s^-2."

### Section B, "clarify": why more rows than L-450 named

L-450 named three rows as examples of one kind of fault: our own
bookkeeping printed inside a citation a visitor reads. I read every
citation the website prints. About twenty more rows need the same
kind of work: some carry the same fault, and some should take back a
locator or an address the website's note had. They are B's items. Fixing them now costs little, because the
build is already going through `constants_new.py` row by row. Leaving
them means a second pass later.

### 5-5, the helmet cusp range (Sun room, streamer belt)

TODAY, the range's low end: "Suess & Nerney (2004), Adv. Space Res.
33:668-675, bibcode 2004AdSpR..33..668S -- the closed field regions, or
helmets, reach no higher than 2-4 solar radii. This row is the low end."
TODAY, its high end: the same, then "This row is the low end. This row is
the high end."
AFTER, both: "Suess & Nerney (2004), Adv. Space Res. 33:668-675, bibcode
2004AdSpR..33..668S -- the closed field regions, or helmets, reach no
higher than 2-4 solar radii."

Why: a visitor has no "row". And the high end contradicts itself today,
because it copies the low end's line and then adds its own.

### 5-10, Earth's polar radius

No room shows this number today; it is exported but not used. The fix is
for when one does.

TODAY: "NASA Planetary Fact Sheet, Earth -- polar radius, 6356.752 km.
IERS Technical Note 36 does NOT tabulate a polar radius; it follows from
that table's equatorial radius and flattening factor ... Corrected
2026-09-19: the old line named IERS as though it printed this number."
AFTER: "NASA Planetary Fact Sheet, Earth -- polar radius, 6356.752 km."

Kept in the orrery only: our check against IERS (Note) and the history
(Corrected).

### 5-11, the inner core, outer core and upper mantle

TODAY, inner core: "... inner core boundary (ICB) at r = 1221.5 km (5 sig
figs)." AFTER: "... inner core boundary (ICB) at r = 1221.5 km."
TODAY, outer core: "... (CMB) at r = 3480 km (4 sig figs)." AFTER: "...
(CMB) at r = 3480 km."
TODAY, upper mantle: "... base of the crust (Mohorovicic discontinuity)
in the reference model, r = 6346.6 km (5 sig figs), i.e. 24.4 km below
the mean radius." AFTER: "... in the reference model, r = 6346.6 km."

Why: "(5 sig figs)" is our count of the number's digits, already on the
row's Figures line. "24.4 km below the mean radius" is our arithmetic,
not the paper's words; it moves to a Note.

### 5-12, the bow shock's shape factor

TODAY: "Jelinek et al. (2012), doi:10.1029/2011JA017252 -- sec. 4, in the
text after eq. 11: lambda = 1.17 for the bow shock (1.54 for the
magnetopause, which this file does not store because the magnetopause is
Shue's)."
AFTER: the same, ending at "for the bow shock."

Why: the parenthesis explains a choice in our file, not the paper. It
moves to a Note.

### 5-14, the magnetic tilt (shown with the belts)

TODAY: "Alken et al. (2021), ... -- for the RELATION: the geomagnetic
poles are computed from the three degree-1 Gauss coefficients, which is
what this row does. The paper prints no tilt of its own. Its Table 4
gives the 2020.0 north geomagnetic pole at 80.65 N, -72.68 E; these
coefficients reproduce it as 80.6512 N, -72.6797 E (read 2026-09-21 by
Claude Opus 5)."
AFTER: "Alken et al. (2021), ... -- the geomagnetic poles, and so the
dipole's tilt, are computed from the three degree-1 Gauss coefficients;
the paper prints no tilt of its own. Its Table 4 gives the 2020.0 north
geomagnetic pole at 80.65 N, -72.68 E."

Kept in the orrery only: our check that the coefficients reproduce the
pole (Note), and who read it and when (Read).

### 5-15, Meredith et al. (2014), the belts' edges

The website's notes (4-31, 4-33) were the only place a visitor learned
where to read the papers free. Those notes are dropped, so the addresses
move into the citations.

TODAY, inner belt's inner edge: "Meredith, N. P., ... doi:10.1002/
2014JA020064 -- introduction, first paragraph: ..." then the note "...
Open full text at nora.nerc.ac.uk ..."
AFTER: "Meredith, N. P., ... doi:10.1002/2014JA020064, open full text at
https://nora.nerc.ac.uk/id/eprint/507469/1/jgra51120.pdf -- introduction,
first paragraph: ..."
The outer belt's inner edge gets the same, plus Li, Tu et al.'s open
copy, https://par.nsf.gov/servlets/purl/10578577.

### 5-16, the inner belt's peak

TODAY: "Baker, D. N. et al. (2018), ... -- sec. 2: inner-zone proton
fluxes peak near geocentric r ~ 1.5 R_E. Geocentric, equatorial, which
is the frame this row is in."
AFTER: the same, ending at "r ~ 1.5 R_E."

Why: "this row". The paper's own words already say geocentric.

### 5-17, the low-orbit outer edge (2,000 km)

TODAY: "... IADC Space Debris Mitigation Guidelines, IADC-02-01 REVISION
2, March 2020, section 3.3.2 (1) -- the LEO Protected Region extends from
the Earth's surface to an altitude of 2,000 km. Section 3.3.1 takes the
equatorial radius as the reference surface, as this file does, and gives
it as 6,378 km. Corrected 2026-09-19: the old line said "Rev. 3 (June
2021)". The document at the Ref link below, which is the one that was
read, is Revision 2 of March 2020, and its revision history table ends
there. No Rev. 3 was involved."
AFTER: the same, without "as this file does" and without the
"Corrected ..." sentences, which move to a Corrected line. The revision,
section and quotation stay.

### 5-19, the outer belt's peak band

TODAY, the outer belt's peak i panel (the two band ends, joined):
"Li, X., ... doi:10.1029/2024JA033504 -- sec. 1: the outer radiation belt
is most intense around L = 4 and 5. This row is the lower end of that
band. Li et al. (2015), ... -- greatest intensity between 4 and 5
equatorial R_E ... Kellerman et al. (2014), as reported in ... These two
corroborate; they were carried on the peak row's "# Declared:" line until
2026-09-22 and were not re-read here.; Li et al. (2025), doi:... -- sec.
1: ... This row is the upper end of that band. Corroborated as the row
above."
AFTER: "Li, X., Xiang, Z., Mei, Y., ... (2025), "A New Electron and Proton
Radiation Belt Identified by CIRBE/REPTile-2 Measurements After the
Magnetic Super Storm of 10 May 2024", J. Geophys. Res. Space Physics 130,
e2024JA033504, doi:10.1029/2024JA033504 -- sec. 1: the outer radiation
belt is most intense around L = 4 and 5.; Li et al. (2025),
doi:10.1029/2024JA033504 -- sec. 1: the outer radiation belt is most
intense around L = 4 and 5."
(The second, short citation is the same paper for the band's other end,
as today.)

Why: a citation a visitor reads should name only papers that were opened
and read for this number. The two corroborating papers were not re-read,
so they move to an Also line, kept in the orrery.

### 5-20, the magnetopause's a7 coefficient

TODAY: "Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
row a7, p. 17,698: -0.007 +/- 0.0005 per nT. Eq. 11 prints it as the
subtraction (0.58 - 0.007 Bz); the table carries the sign, so the stored
coefficient is negative and adds."
AFTER: the same, ending at "per nT."

Why: the rest explains how our file stores the sign. It moves to a Note.

### 5-21 and 5-22, notes in the orrery only

Neither changes anything a visitor reads. They keep the citations from
the two dropped website notes (4-20 and 4-23) in the orrery, so they are
not lost: Prsa et al. (2016) on the mean radius row, and the NASA Earth
Observatory page on the geostationary row.

One thing to know about 4-20: the crust's radius note, which a visitor
reads, says "as the International Astronomical Union recommends". After
the note is dropped, the i panel no longer shows Prsa et al. (2016) as
the source for that. The words stay true; the citation is kept in the
orrery.

### 6-1, the crust's note

TODAY, in the crust's i panel: "Drawn at the mean radius, the sphere the
interior layers (PREM) are measured against (Tony, 2026-09-28). Crust
thickness (5-10 km oceanic, 30-50 km continental) is below the drawn
resolution."
AFTER: "Drawn at the mean radius, the sphere the interior layers (PREM)
are measured against. Crust thickness (5-10 km oceanic, 30-50 km
continental) is below the drawn resolution."

Why: a visitor does not know who Tony is or what the date means. Your
ruling of that day stays in the ledger.

Found while answering, not part of this build: the crust thicknesses in
that note (5-10 km and 30-50 km) are typed numbers with no source
anywhere. I will record them in the ledger as a class, not chase them
here.

---

Written October 17, 2026 with Anthropic's Claude Opus 5.5.
