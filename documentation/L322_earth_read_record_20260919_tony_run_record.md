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
Tony's reading list -- the rows this session could not open. There is one
of them.

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

## 2. For Tony to read

One row. This is your whole share of the reading for C1.

### `EARTH_LEO_UPPER_ALTITUDE_KM` = 2000.0 km

**Where to look:** the IADC Space Debris Mitigation Guidelines,
IADC-02-01. The row's own `# Ref:` line points at
https://orbitaldebris.jsc.nasa.gov/library/iadc-space-debris-guidelines-revision-2.pdf

**What to look for:** the definition of the LEO Protected Region, in the
section on protected regions (section 3.3.2 in the revision the row
cites). It is usually labelled "Region A".

**The number you should expect to see:** an altitude of **2,000 km**,
with the region extending from the Earth's surface up to it. The row also
claims the guidelines take the **equatorial radius** as the reference
surface, so that is worth confirming in the same place.

**Why it is on your list and not read above.** This session could not
open the primary document. The definition was confirmed in several
independent reproductions of it, including a reproduction of the IADC
2007 protected-regions figure, and every one of them says 2,000 km from
the surface. But a reproduction is not the document, and The Access
Standard says a read records what was OPENED. So the row carries no
`# Read:` line naming a model; it carries a pointer to this file instead.

**If the link is dead** -- the row's URL says "revision-2" while the
source line says "Rev. 3 (June 2021)", so it may well be -- then the
citation fails The Access Standard and the row should be re-homed to
whatever the current IADC publication is, or to a standards body that
restates it. Tell me which and I will do it in C2.

**When you have read it,** the line to add is:

```
# Read: IADC Space Debris Mitigation Guidelines, LEO Protected Region,
# Read+: <the section number you actually found it in>, <date>, Tony
# Read+: Quintanilla
```

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

=====================

**Tony**: actions

C1 is built and tested. Three files above, and one thing to do.

Run the orrery patch first. 

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L322_10_earth_slice_c1_20260919.py
  ok  TOKENS  four new tokens: km3_s2, m3_s2, rad_s, m3_per_km3
  ok  KM_PER_AU  unit, status, figures, read
  ok  GM_SUN_SI  unit, status, figures, read
  ok  EARTH_EQUATORIAL_RADIUS_KM  four fields
  ok  EARTH_POLAR_RADIUS_KM  source corrected, three fields
  ok  EARTH_MEAN_RADIUS_KM  four fields
  ok  EARTH_INNER_CORE_KM  four fields
  ok  EARTH_INNER_CORE_RADII  unit, figures
  ok  EARTH_OUTER_CORE_KM  four fields
  ok  EARTH_OUTER_CORE_RADII  unit, figures
  ok  EARTH_D660_DEPTH_KM  four fields
  ok  EARTH_LOWER_MANTLE_KM  derived corrected 5711 -> 5710, unit, figures
  ok  EARTH_LOWER_MANTLE_RADII  derived corrected, unit, figures
  ok  EARTH_UPPER_MANTLE_KM  four fields
  ok  EARTH_UPPER_MANTLE_RADII  unit, figures
  ok  EARTH_GM_KM3_S2  four fields
  ok  EARTH_GM_KM3_S2  note corrected TCB -> TCG
  ok  EARTH_ROTATION_RATE_RAD_S  source corrected Table 1.1 -> 1.2
  ok  EARTH_ROTATION_RATE_RAD_S  four fields
  ok  EARTH_GEOSTATIONARY_RADIUS_KM  derived reworded, unit, figures
  ok  EARTH_GEOSTATIONARY_RADII  unit, figures
  ok  EARTH_LEO_UPPER_ALTITUDE_KM  three fields, read deferred to Tony
  ok  EARTH_LEO_LOWER_ALTITUDE_KM  unit, status, figures
  ok  EARTH_LEO_INNER_KM  derived line added, unit, figures
  ok  EARTH_LEO_OUTER_KM  unit, figures
  ok  EARTH_LEO_INNER_RADII  derived line added, unit, figures
  ok  EARTH_LEO_OUTER_RADII  unit, figures
  ok  EARTH_STRATOPAUSE_ALTITUDE_KM  four fields
  ok  EARTH_THERMOPAUSE_ALTITUDE_KM  four fields
  ok  EARTH_STRATOPAUSE_RADII  derived line added, unit, figures
  ok  EARTH_THERMOPAUSE_RADII  derived corrected, unit, figures
  ok  EARTH_GEOCORONA_RADII  four fields
  ok  EARTH_HILL_SPHERE_KM  named conversion M3_PER_KM3, unit, figures
  ok  EARTH_HILL_SPHERE_RADII  unit, figures

      constants_new.py          105955 ->  116443 bytes
      constants_tokens.py         5834 ->    6782 bytes

patch applied (2 files, 34 edits)

NOW, in order:
  1. Run the orrery maintenance run. The three constants
     checkers should report Earth's rows JUDGED rather than
     NO UNIT, and nothing should fail.
  2. Move this script into documentation/.
  3. Commit and push. Report the new SHA.
  4. The gallery half of C1 follows: pull the export, run the
     mirror, rebuild the cache with OneDrive syncing PAUSED,
     run the gallery maintenance run, commit the config and
     the cache TOGETHER, push.

Undo at any point is Discard Changes in GitHub Desktop.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

Save patch_L322_10_...py in the orrery repo root, Run it in VS Code, then run the orrery maintenance run, 

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260919T153516Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 0.8s  unchanged (1 of 1 rewritten, content
                                     identical)
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.9s  rewrote data/constants_export.json
  Module atlas                 6.1s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.3s  rewrote DATA_INVENTORY.md
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.3s  1 derived line(s): 1 changed, 0 added, 0
                                     removed
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.4s  No figure count exceeds its inputs: 31
                                     derived row(s) read, 15 judged OK -- 15 OK,
                                     16 NOT YET MIGRATED, 1 NO DERIVED LINE.
  Constants export check       0.6s  Export matches the store: sha256
                                     b70f2c56756b on both sides; 55 rows re-read,
                                     58 not exported, 16 tokens.
  Dimensions                   1.0s  No unit contradicts its arithmetic: 31
                                     derived row(s) read -- 15 OK, 10 NO UNIT, 6
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 62 status lines in constants_new.py are
                                     well formed; 49 rows carry none.
  Row shape                    0.1s  All 113 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          15.4s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.6s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Worksheet checker            8.3s  76 of 114 routed, 8 clean
  Worksheet checker tests     14.8s  All 136 checks passed
  Worksheet key round trip     0.8s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         23.9s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          11.2s  292 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  16 of 16 gating checkers passed -- 91.9s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          292 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  1887 file(s) examined, 9 written, 1 created, 0 removed, 5 rewritten identically
    written   DATA_INVENTORY.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/constants_export.json
    written   data/provenance_history.json
    written   documentation/L322_earth_read_record_20260919.md
    written   documentation/prompts/citation_review.jsonl
    created   documentation/L322_earth_read_record_20260919_tony_run_record.md
    rewritten with identical bytes, no action needed:
      LEDGER_CONSOLIDATED.md
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

move the script into documentation/, commit and push. The script prints the rest of the sequence when it finishes. 



The gallery patch and the read record are for after that push; the read record is a documentation/ file with nothing to run.

What C1 does. All 57 Earth rows now carry a unit and a status, up from 28. The 29 that had nothing now have figure counts too, and 12 carry a read line naming who read the source. The export goes from 23 rows served to 55, of which 52 are Earth's — so most of those links move off the old drift check onto the new ones. All three constants checkers pass, and I made each one fail on purpose on an Earth row and watched it name the row: the unit checker on a broken _RADII, the figures checker on an over-declared count, the export checker on a value I altered by hand.

Corrections I made as I went, beyond the lower mantle you approved. Three citations in the store said something false. The rotation rate cited IERS Table 1.1, which contains no angular velocity — it is Table 1.2, the GRS80 parameters. The polar radius cited IERS as though that document tabulated one; it does not, the number follows from the equatorial radius and the flattening factor, so I re-homed it to the NASA fact sheet which prints it directly. And the Earth's GM was labelled TCB-compatible where the table's own footnote says TCG. In each case the value was right and only the pointer was wrong, which is the quiet kind of error — a citation that passes inspection while asserting a provenance that does not exist.

One thing turned out better than the skill says. provenance-discipline records the 1981 PREM paper as walled, with its tables open elsewhere. The paper itself is open in full at Harvard, and I read Table I directly rather than through a secondary tabulation. That is worth correcting at the skill's next bump, and the read record says so.

Your reading list has one row on it. EARTH_LEO_UPPER_ALTITUDE_KM, the 2,000 km LEO ceiling. I could not open the primary IADC document, and several faithful reproductions of it are still not the document. The read record's section 2 gives you the link, where to look, and the number to expect. I suspect the link is dead — the URL says revision 2 while the citation says Rev. 3 — in which case tell me and I will re-home it in C2.

Still open for C2, unchanged: the 28 magnetosphere rows, the five retired dimensionless tokens, the two standoffs reverting to expressions, and the read check I told you I would build before Earth closes.
