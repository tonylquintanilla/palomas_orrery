# L-322 Earth slice -- the read record, Stage C1

Built on orrery `4801594104cdb229bc14fa9d77a9ba3ca1e686be`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `82e786f17634f108a2e0df2ae7c693e5fcf62a60`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Both HEADs read live with `git ls-remote` on 2026-09-19, and both
repositories cloned at those SHAs. Every measurement below was taken on
those clones with the project's own reader, `constants_rows.py`.

**Type: READ RECORD.** Session of 2026-09-19, Tony with Anthropic's
Claude Opus 5. Companion to
`documentation/BUILD_MANIFEST_L322_earth_slice_20260919.md`, section 6.

**What this file is.** `# Read:` records that somebody opened a source
and checked it against the number beside it. This file is the long form:
what was opened, where in it, what it says, and the verdict. Section 2 is
Tony's reading list. It had one row on it; Tony read it on 2026-09-19
and section 2 now records that read rather than asking for it.

**Who read.** Under provenance-discipline 2.14, The Read Field, the
reader is decided by ACCESS. Where the builder can open the source it
reads it and names itself; a model's read is a real read and the line
says it was a model's. This session had web search and document fetching,
so it did most of the reading. Nothing below was reconstructed from
training: every row names a document that was actually opened in this
session, and where a source could not be opened, the row says so instead
of claiming a read.

---

## 1. Read this session, by Claude Opus 5, 2026-09-19

### IERS Conventions (2010), IERS Technical Note 36

Opened: the full PDF at https://iers-conventions.obspm.fr/content/tn36.pdf
Title as printed: "IERS Conventions (2010)", Gerard Petit and Brian Luzum
(eds.), IERS Technical Note No. 36.

| Row | Where | What it says | Verdict |
| --- | --- | --- | --- |
| `EARTH_EQUATORIAL_RADIUS_KM` | Table 1.1, p. 18, "Earth constants" | a_E = 6378136.6 m, uncertainty 0.1 m | AGREES with 6378.1366 km. Eight figures, set by the uncertainty. |
| `EARTH_GM_KM3_S2` | Table 1.1, p. 18 | GM(Earth) = 3.986004418e14 m^3 s^-2, uncertainty 8e5 | AGREES with 398600.4418 km^3 s^-2. The uncertainty is ~2 parts in 1e9, so nine figures. |
| `EARTH_ROTATION_RATE_RAD_S` | **Table 1.2**, p. 19, "Parameters of the Geodetic Reference System GRS80" | omega = 7.292115e-5 rad s^-1 | AGREES with the stored value. **The row's citation was wrong about the table.** It said Table 1.1, which contains no angular velocity at all. Corrected on the row. |
| `EARTH_POLAR_RADIUS_KM` | Table 1.1, p. 18 | a_E and 1/f = 298.25642; **no polar radius is tabulated** | The value 6356.752 km is right -- 6378136.6 x (1 - 1/298.25642) = 6356751.86 m -- but it is DERIVED from that table, not printed in it. **The citation implied IERS printed it.** Re-homed to the NASA fact sheet, which does print it, with the IERS derivation kept on the row. |

A third finding from the same table, recorded and acted on: Table 1.1's
own footnote reads "The value for GM(Earth) is TCG-compatible." The row's
note said TCB-compatible. Corrected.

### Dziewonski & Anderson (1981), PREM

Opened: the paper itself, open at Harvard,
https://lweb.cfa.harvard.edu/~lzeng/papers/PREM.pdf
Title as printed: "Preliminary reference Earth model", Adam M. Dziewonski
and Don L. Anderson, Physics of the Earth and Planetary Interiors, 25
(1981) 297-356.

**The skill records this paper as walled with its tabulation open
elsewhere. That is no longer true and the skill can say so at its next
bump:** the 1981 paper is open in full at the address above, and Table I
was read directly rather than through a secondary tabulation.

| Row | Where | What it says | Verdict |
| --- | --- | --- | --- |
| `EARTH_INNER_CORE_KM` | Table I, p. 308 | Inner core: 0 to 1221.5 km | AGREES. Five figures. |
| `EARTH_OUTER_CORE_KM` | Table I, p. 308 | Outer core: 1221.5 to 3480.0 km | AGREES. Four figures -- see the note on padding below. |
| `EARTH_UPPER_MANTLE_KM` | Table I, p. 308 | LID: 6291.0 to 6346.6 km; Crust begins at 6346.6 | AGREES. The row draws the Mohorovicic discontinuity at 6346.6 km. Five figures. |

**A rule this walk had to settle, applied uniformly.** PREM's Table I
pads every boundary radius to one decimal place: 1221.5, 3480.0, 3630.0,
5600.0, 5701.0, 6346.6, 6371.0. A trailing ZERO in that padded place is
the table's format and does not count; a non-zero digit there does. So
3480.0 carries four figures while 1221.5 and 6346.6 carry five. The same
reading governs the NASA fact sheet, which pads to three decimals.

The paper also states its own reference radius, 6371 km, in section 3.

### NASA Planetary Fact Sheet, Earth

Opened: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
Title as printed: "Earth Fact Sheet".

| Row | Where | What it says | Verdict |
| --- | --- | --- | --- |
| `EARTH_MEAN_RADIUS_KM` | Bulk parameters | Volumetric mean radius 6371.000 km | AGREES with 6371.0. Four figures: the table pads to three decimals throughout, so the trailing zeros are formatting. |
| `EARTH_POLAR_RADIUS_KM` | Bulk parameters | Polar radius 6356.752 km | AGREES. Seven figures. This is now the row's source. |

The same sheet lists a core radius of 3485 km, five kilometres from
PREM's 3480. The row's existing note already explains why PREM is
preferred -- the other three boundaries in the same nested stack are
PREM's -- and that reasoning still holds. No change.

### Ishii et al. (2018), Scientific Reports

Opened: https://pmc.ncbi.nlm.nih.gov/articles/PMC5910398/ (open access)
Title as printed: "Complete agreement of the post-spinel transition with
the 660-km seismic discontinuity", Sci. Rep. 8:6358.

| Row | Where | What it says | Verdict |
| --- | --- | --- | --- |
| `EARTH_D660_DEPTH_KM` | Results, the paragraph comparing transition pressure with depth | "the global average depth of the discontinuity is 660 +/- 10 km, a variance in distance that corresponds to a pressure variance of 23.4 +/- 0.4 GPa" | AGREES with 660.0, and **it sources the precision**. +/- 10 km puts the last significant digit in the tens place, which is two figures -- exactly what the row's source line already claimed without a source behind it. |

**This is the row that changed a drawn number.** `EARTH_LOWER_MANTLE_KM`
is computed as 6371.0 - 660. Its `# Derived:` line said the 660 was good
to units and read off 5711 km. It is good to TENS, so the difference is
good to tens and the value is 5710 km. The gallery served 5711.0 for the
lower mantle shell. Tony approved the correction on 2026-09-19 before it
was written.

**A finding for L-253, recorded and not acted on.** L-253 has been
holding two figures for the variation of the 660 boundary as unsourced.
This paper gives +/- 10 km and cites six seismological studies behind it
(Flanagan & Shearer 1998, Houser et al. 2008, Gao & Liu 2014, Zheng et
al. 2015, Houser 2016, Wang & Pavlis 2016). That is a sourced figure for
the variation. It is NOT a second independent cross-check leg -- it is
the same research group as the 2019 paper the row cites -- so the
Review-note's outstanding obligation stands. Whether it discharges is for
L-253 to decide, not this walk.

### NOAA JetStream

Opened: https://www.noaa.gov/jetstream/atmosphere/layers-of-atmosphere
Title as printed: "Layers of the Atmosphere".

| Row | Where | What it says | Verdict |
| --- | --- | --- | --- |
| `EARTH_STRATOPAUSE_ALTITUDE_KM` | Stratosphere section | "The stratosphere extends from 4-12 miles (6-20 km) above the Earth's surface to around 31 miles (50 km)" | AGREES with 50.0. Two figures: 31 miles is 49.9 km, so the km figure is not more precise than that. |
| `EARTH_THERMOPAUSE_ALTITUDE_KM` | Exosphere and thermosphere sections | the exosphere "extends from about 375 miles (600 km)"; "At the bottom of the exosphere is a transition layer called the thermopause" | AGREES with 600.0. Two figures: 375 miles is 603.5 km, rounded to 600 in the km figure. |

The row's note says the thermopause moves over roughly 500 to 1,000 km.
That range is not on this page and is not cited anywhere in the store. It
is left as prose, which is legitimate -- a note is not a citation -- and
is NOT used as the declared range, because nothing sources it.

### Baliukin et al. (2019), JGR Space Physics

Opened: the published abstract, reproduced verbatim at
https://publications.hse.ru/en/view/240296659 and at the HAL record
insu-02021638, where the full text is also open.
Title as printed: "SWAN/SOHO Lyman-alpha Mapping: The Hydrogen Geocorona
Extends Well Beyond the Moon", J. Geophys. Res. Space Physics 124:861-885.

| Row | Where | What it says | Verdict |
| --- | --- | --- | --- |
| `EARTH_GEOCORONA_RADII` | Abstract | "The geocorona was found to extend at least up to 100 Earth radii (RE) ... encompassing the orbit of the Moon (~60 RE)" | AGREES with 100.0. One figure: this is a detection FLOOR, "at least", not a measured edge. The row's note already says so, and the ~60 RE for the Moon's orbit confirms the note's second sentence too. |

### IAU 2012 Resolution B2

Opened: the IAU resolutions text at
https://iauarchive.eso.org/static/resolutions/IAU2012_English.pdf, and
the Observatoire de Paris summary page carrying the same wording.
Title as printed: "RESOLUTION B2 on the re-definition of the astronomical
unit of length".

| Row | Where | What it says | Verdict |
| --- | --- | --- | --- |
| `KM_PER_AU` | the resolution's recommendation | the astronomical unit is "149 597 870 700 m exactly" | AGREES with 149597870.7 km. Exact by definition. |

### Prsa et al. (2016), AJ 152:41

Opened: the arXiv version, https://arxiv.org/pdf/1605.09788
Title as printed: "Nominal values for selected solar and planetary
quantities: IAU 2015 Resolution B3".

| Row | Where | What it says | Verdict |
| --- | --- | --- | --- |
| `GM_SUN_SI` | Table 1 | 1(GM)^N(Sun) = 1.3271244e20 m^3 s^-2, and the resolution states the nominal values are "by definition exact" | AGREES with the stored value. Exact. |

Worth knowing and not acted on: the same table gives a nominal Earth mass
parameter of 3.986004e14 m^3 s^-2, truncated, which is a CONVERSION
CONSTANT rather than a measurement. `EARTH_GM_KM3_S2` correctly uses the
IERS measured value instead. The two are not interchangeable and the
store has the right one.

---

## 2. Read by Tony, 2026-09-19 -- DONE

One row, and it is closed. The link was alive.

### `EARTH_LEO_UPPER_ALTITUDE_KM` = 2000.0 km

**What Tony opened.** The IADC Space Debris Mitigation Guidelines at the
row's own `# Ref:` address,
https://orbitaldebris.jsc.nasa.gov/library/iadc-space-debris-guidelines-revision-2.pdf
He downloaded it, read section 3.3.2 on page 8 of 14, and imaged the
paragraph.

**Where the local copies live.** `documentation/papers/` on Tony's disk,
as `iadc-space-debris-guidelines-revision-2.pdf` and
`EARTH_LEO_UPPER_ALTITUDE_KM_2000_km_tony_read.png`. **Neither is in the
repository, and that is deliberate** -- `documentation/papers/` is
gitignored, so a later reader will not find them by path. The address
above is what travels.

**What it says.** Section 3.3.2 (1): "Region A, Low Earth Orbit (or LEO)
Protected Region -- spherical region that extends from the Earth's
surface up to an altitude (Z) of 2,000 km". AGREES with 2000.0.
Exact -- a defined region boundary, not a measurement.

**Two findings this read turned up, neither visible in the imaged
paragraph.** After Tony confirmed the number, this session opened the
same document at the same address -- it was reachable on a second attempt
-- and read it through.

- **The revision was wrong, and is corrected.** The row's source line
  said "IADC-02-01 Rev. 3 (June 2021)". The document is IADC-02-01
  **Revision 2, March 2020**. Its revision history table lists exactly
  three issues -- 2002-10-15 initial, 2007-09-01 first revision,
  2020-03-01 update to section 5.3.2 -- and stops. There is no Rev. 3.
  The number, the section and the link were all right, which is why
  nothing looked odd.
- **The equatorial-radius claim is right, and is now quoted.** Section
  3.3.1: "the equatorial radius of the Earth is taken as 6,378 km and
  this radius is used as the reference for the Earth's surface from which
  the orbit regions are defined." The row said so already; it now carries
  the figure too.

**Who read, and why the line names Tony.** Tony opened the document and
read the paragraph the row depends on. That is the read the row needed
and the `# Read:` line names him. The corroborating pass is recorded here
rather than on the row, because a read line names a reader and a place,
not an audit trail.

---

## 3. Rows deliberately given NO read line, and why

Not every row needs one. The scope is a MEASURED row whose value is drawn
in a published exhibit, or that feeds one.

- **Every expression row** -- the fifteen `_RADII` and derived `_KM` rows.
  A derived row has nothing to read against; checking it means checking
  its inputs, and its `# Status: derived -- inherits ...` line names them.
- **`EARTH_LEO_LOWER_ALTITUDE_KM`** -- a declared drawing floor. There is
  no source, its absence is not a finding, and the status line says so.
- **`M3_PER_KM3`** -- an exact unit conversion, new in this patch.
- **`EARTH_POLAR_RADIUS_KM`** -- measured, but outside the read scope:
  the gallery links the interior `_KM` rows and this one feeds nothing
  drawn. It was read anyway, above, because the walk had the table open
  and found a citation error in it.

The read scope was re-derived from the gallery config rather than carried
from the manifest: 44 of Earth's 57 rows are drawn or feed something
drawn, and the 13 outside are the same 13 the manifest names.

---

Written September 2026 with Anthropic's Claude Opus 5.
