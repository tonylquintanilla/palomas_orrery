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

-- orrery moved to 903f9013ac81e58c2050d2aade61763d2c5ff64a

The gallery patch and the read record are for after that push; the read record is a documentation/ file with nothing to run.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L322_11_lower_mantle_citation_20260919.py
  ok  1 change written

      was: Ishii, Kumagai, Sugiura & Tsuchiya (2019), Nature Geoscience 12:869 -- the 660-km discontinuity
      now: Ishii, Huang, Myhill et al. (2019), Nature Geoscience 12:869-872 -- the sharp 660-km discontinuity; the global average depth of 660 +/- 10 km is from the same group's open companion, Ishii et al. (2018), Scientific Reports 8:6358

NOW, in order -- this is the rest of the gallery half of C1:
  1. Pull the orrery's export: python tools/pull_constants_export.py
  2. Run the mirror: python tools/mirror_constants.py --write
     It writes the NUMBERS. Expect the lower mantle shell to
     move from 5711.0 to 5710.0 km, and expect many Earth
     links to start being served by the export rather than
     going through the older drift check.
  3. PAUSE OneDrive syncing, then rebuild the served cache.
  4. Run the gallery maintenance run. Expect 'Cache in step'.
  5. Move this script into documentation/.
  6. Commit the config AND the cache TOGETHER, and push. A
     config change is not deployed until the cache is rebuilt.
  7. Look at both rooms on the phone.

Undo at any point is Discard Changes in GitHub Desktop.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.1s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.6s  rewrote
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  rewrote data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite       7.7s  PASS (167 checks, 0 failures)
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        3.1s  All 245 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 246 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 37 link(s) compared, store
                                    b70f2c56756b.
  PASS Pointer join              0.1s  Every link is accounted for: 70
                                    link(s) against orrery 903f9013,
                                    28 fallback named.
  FAIL Cache in step             0.1s  18 difference(s): the served cache
                                    is NOT what the config says. The
                                    live rooms draw from the cache.
                                    Run the cache builder and commit
                                    its output with the config.
  PASS Feature renderers         0.8s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 sibling(s), none stale.
                                    The sweep is keeping up.

======================================================================
  1 of 14 gating checkers FAILED
  Cache in step
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 sibling(s), none stale. The
======================================================================

----------------------------------------------------------------------
Cache in step -- 18 difference(s): the served cache is NOT what the config says. The live rooms draw from the cache. Run the cache builder and commit its output with the config.
----------------------------------------------------------------------
======================================================================
  CACHE IN STEP -- the served cache against data/objects_config.json
======================================================================

Compared 4 object(s) serving features (sun, earth, jupiter, saturn), 34 named shell(s),
against data/solar-system/coverage_index.json and data/solar-system/feature_configs.json.

FAILURES (18):
  data/solar-system/coverage_index.json        earth/earth_interior/inner_core/radius/figures: config present, cache absent
  data/solar-system/coverage_index.json        earth/earth_interior/outer_core/radius/figures: config present, cache absent
  data/solar-system/coverage_index.json        earth/earth_interior/lower_mantle/radius/value: config 5710.0, cache 5711.0
  data/solar-system/coverage_index.json        earth/earth_interior/lower_mantle/radius/figures: config present, cache absent
  data/solar-system/coverage_index.json        earth/earth_interior/lower_mantle/source: config "Ishii, Huang, Myhill et al. (2019), Nature G..., cache "Ishii, Kumagai, Sugiura & Tsuchiya (2019), N...
  data/solar-system/coverage_index.json        earth/earth_interior/upper_mantle/radius/figures: config present, cache absent
  data/solar-system/coverage_index.json        earth/earth_interior/crust/radius/figures: config present, cache absent
  data/solar-system/coverage_index.json        earth/earth_interior/planet_radius/figures: config present, cache absent
  data/solar-system/coverage_index.json        earth: and 20 more difference(s)
  data/solar-system/feature_configs.json       earth/earth_interior/inner_core/radius/figures: config present, cache absent
  data/solar-system/feature_configs.json       earth/earth_interior/outer_core/radius/figures: config present, cache absent
  data/solar-system/feature_configs.json       earth/earth_interior/lower_mantle/radius/value: config 5710.0, cache 5711.0
  data/solar-system/feature_configs.json       earth/earth_interior/lower_mantle/radius/figures: config present, cache absent
  data/solar-system/feature_configs.json       earth/earth_interior/lower_mantle/source: config "Ishii, Huang, Myhill et al. (2019), Nature G..., cache "Ishii, Kumagai, Sugiura & Tsuchiya (2019), N...
  data/solar-system/feature_configs.json       earth/earth_interior/upper_mantle/radius/figures: config present, cache absent
  data/solar-system/feature_configs.json       earth/earth_interior/crust/radius/figures: config present, cache absent
  data/solar-system/feature_configs.json       earth/earth_interior/planet_radius/figures: config present, cache absent
  data/solar-system/feature_configs.json       earth: and 20 more difference(s)

18 difference(s): the served cache is NOT what the config says. The live rooms draw from the cache. Run the cache builder and commit its output with the config.

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

gallery moved to b1c11cc7300c8fa943e1c9358d0ce699b94cf19b

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 11 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy

  PASS Served reachability       1.5s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at 903f9013

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 903f9013, byte for byte

  orrery HEAD 903f9013
  examining 33 of 70 links; the other 37 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NO UNIT       EARTH_MAGNETOPAUSE_SHUE_A6       the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/magnetopause/surface/a6
    NO UNIT       EARTH_MAGNETOPAUSE_SHUE_A8       the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/magnetopause/surface/a8
    NO UNIT       EARTH_BOW_SHOCK_JELINEK_EPS      the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/bow_shock/surface/epsilon
    NO UNIT       EARTH_BOW_SHOCK_JELINEK_LAMBDA   the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/bow_shock/surface/lambda
    NOT IN STORE  planet_poles['Earth']            not a top-level constant in the store
                  /objects/1/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  33 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 9 could not be examined.

  PASS Store drift               0.6s  33 pointers against orrery
                                    903f9013 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 9 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            33 pointers against orrery 903f9013 --
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

What C1 does. All 57 Earth rows now carry a unit and a status, up from 28. The 29 that had nothing now have figure counts too, and 12 carry a read line naming who read the source. The export goes from 23 rows served to 55, of which 52 are Earth's — so most of those links move off the old drift check onto the new ones. All three constants checkers pass, and I made each one fail on purpose on an Earth row and watched it name the row: the unit checker on a broken _RADII, the figures checker on an over-declared count, the export checker on a value I altered by hand.

Corrections I made as I went, beyond the lower mantle you approved. Three citations in the store said something false. The rotation rate cited IERS Table 1.1, which contains no angular velocity — it is Table 1.2, the GRS80 parameters. The polar radius cited IERS as though that document tabulated one; it does not, the number follows from the equatorial radius and the flattening factor, so I re-homed it to the NASA fact sheet which prints it directly. And the Earth's GM was labelled TCB-compatible where the table's own footnote says TCG. In each case the value was right and only the pointer was wrong, which is the quiet kind of error — a citation that passes inspection while asserting a provenance that does not exist.

One thing turned out better than the skill says. provenance-discipline records the 1981 PREM paper as walled, with its tables open elsewhere. The paper itself is open in full at Harvard, and I read Table I directly rather than through a secondary tabulation. That is worth correcting at the skill's next bump, and the read record says so.

Your reading list has one row on it. EARTH_LEO_UPPER_ALTITUDE_KM, the 2,000 km LEO ceiling. I could not open the primary IADC document, and several faithful reproductions of it are still not the document. The read record's section 2 gives you the link, where to look, and the number to expect. I suspect the link is dead — the URL says revision 2 while the citation says Rev. 3 — in which case tell me and I will re-home it in C2.

**Tony**: correct. I read the paper downloaded to orrery documentation/papers as iadc-space-debris-guidelines-revision-2.pdf in the link provided https://orbitaldebris.jsc.nasa.gov/library/iadc-space-debris-guidelines-revision-2.pdf and I imaged the specific paragraph referenced and saved it in the same directory as EARTH_LEO_UPPER_ALTITUDE_KM_2000_km_tony_read.png 

Still open for C2, unchanged: the 28 magnetosphere rows, the five retired dimensionless tokens, the two standoffs reverting to expressions, and the read check I told you I would build before Earth closes.

==============================

Opus: 
Reading the run record from disk — only the image landed in my context.Reading both remotes live before anything else — the offline run in your record ended on a red Cache in step.The cache is the live-site problem. Confirmed: the deployed rooms serve the old value. Now checking the orrery side and the row Tony read.Trying the IADC document myself now that you've given the link — it should settle two smaller things on that row.That search result is the document itself, and its revision table settles one thing already. Fetching it to check the other.The document settles both. Section 3.3.1 says exactly what the row claims — but the revision is wrong. Building the patch.**The live site is still serving the old numbers.** That is the one thing to fix, and it is the failure gallery-cache-builder 1.5 was bumped to prevent. I cloned the gallery at `b1c11cc7` and ran Cache in step against it: 18 differences, the same 18 your offline run reported. The config went out and the cache did not. Right now the Earth room draws the lower mantle at 5711 km with the wrong author list, because the rooms read the cache.

The live run passed because it only checks that the served files match your working copy. Both are stale in the same way, so it cannot see this — another check that cannot fail for this particular thing, which is worth a line on L-336 when you next touch it.

**What to do, in this order.** Run the orrery patch above first: it changes comments only, no value moves, and the export comes out byte-identical apart from the store hash. Push it. 

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L322_12_iadc_read_20260919.py
  ok  STORE  EARTH_LEO_UPPER_ALTITUDE_KM  the read line, Tony's read
  ok  STORE  EARTH_LEO_UPPER_ALTITUDE_KM  revision corrected Rev. 3 -> Revision 2
  ok  RECORD  section 2 becomes the record of the read
  ok  RECORD  the header stops promising a list that no longer exists

      constants_new.py                                      116443 ->  117113 bytes
      documentation/L322_earth_read_record_20260919.md       13260 ->   13797 bytes

patch applied (2 files, 4 edits)

NOW, in order:
  1. Run the orrery maintenance run. Nothing should change
     except the two files above: this patch touches no value,
     so the export and every checker should be unmoved.
  2. Move this script into documentation/.
  3. Commit and push. Report the new SHA.

Undo at any point is Discard Changes in GitHub Desktop.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

Then do the gallery in one pass — pull the export, run the mirror, 

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L322_11_lower_mantle_citation_20260919.py
ERROR: that entry does not hold the text this patch was cut against.
  expected 'Ishii, Kumagai, Sugiura & Tsuchiya (2019), Nature Geoscience 12:869 -- the 660-km discontinuity'
  found    "Ishii, Huang, Myhill et al. (2019), Nature Geoscience 12:869-872 -- the sharp 660-km discontinuity; the global average depth of 660 +/- 10 km is from the same group's open companion, Ishii et al. (2018), Scientific Reports 8:6358"
If the patch already ran, this is what a second run looks like: it refuses.
NOTHING was written. Undo is Discard Changes in GitHub Desktop.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

pause OneDrive, -- paused for 2 hours

rebuild the cache, 

[RECOVER] removed retained data\solar-system.prev (cleared read-only on 6 entries)
[sweep] kept 1 recent sibling(s) as autopsies: .staging_solar-system_20260917T234936Z
[warn] sun: features-only entry; no Horizons fetch
[done] run 20260919T210317Z (nightly): 13 objects

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

run the offline maintenance run until Cache in step is green, 

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              0.7s  no change to MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.8s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite       6.7s  PASS (167 checks, 0 failures)
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        2.8s  All 245 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 246 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 37 link(s) compared, store
                                    b70f2c56756b.
  PASS Pointer join              0.1s  Every link is accounted for: 70
                                    link(s) against orrery 6071df8e,
                                    28 fallback named.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.7s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.1s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.1s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 sibling(s), none stale.
                                    The sweep is keeping up.

======================================================================
  14 of 14 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 sibling(s), none stale. The
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

and commit the config and the cache together. Doing the orrery first means the gallery only needs one cycle.

orrery moved to 4417217b9d3ee2fe4b275e62b99ed789f86a464b
gallery moved to ddda2893c0ed3bd552fefacca745cbfcfd6aa9d7

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 11 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy

  PASS Served reachability       1.5s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at 6071df8e

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 6071df8e, byte for byte

  orrery HEAD 4417217b
  examining 33 of 70 links; the other 37 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NO UNIT       EARTH_MAGNETOPAUSE_SHUE_A6       the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/magnetopause/surface/a6
    NO UNIT       EARTH_MAGNETOPAUSE_SHUE_A8       the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/magnetopause/surface/a8
    NO UNIT       EARTH_BOW_SHOCK_JELINEK_EPS      the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/bow_shock/surface/epsilon
    NO UNIT       EARTH_BOW_SHOCK_JELINEK_LAMBDA   the constant's name declares no unit
                  /objects/1/features/earth_magnetosphere/bow_shock/surface/lambda
    NOT IN STORE  planet_poles['Earth']            not a top-level constant in the store
                  /objects/1/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  33 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 9 could not be examined.

  PASS Store drift               0.8s  33 pointers against orrery
                                    4417217b -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 9 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            33 pointers against orrery 4417217b --
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

**Your read is recorded, and it found two more things.** The number is confirmed and the row now carries a real read line naming you, with the section and its words. After you confirmed it I tried the same link again and it worked this time, so I read the document through — which turned up what your paragraph could not show.

The revision was wrong. The row cited "IADC-02-01 Rev. 3 (June 2021)". The document is **Revision 2, March 2020**, and its revision history table lists three issues and stops at 2020. There is no Rev. 3. The number, the section and the link were all correct, which is exactly why nobody looked twice at the revision.

The other claim on that row turned out right, and I had flagged it as unverified. Section 3.3.1 says the equatorial radius "is taken as 6,378 km and this radius is used as the reference for the Earth's surface from which the orbit regions are defined." The row said so already; it now carries the figure too.

**On where the paper lives.** `documentation/papers/` is gitignored, so your PDF and image stay on your disk and never reach the repository. That is the right arrangement and I have not tried to change it — but it means a later reader cannot follow a path to them, so the read record now says the address is what travels, not the filename.

C2 is unchanged: the 28 magnetosphere rows, the five retired `dimensionless` tokens (your live run already names four of them as NO UNIT), the two standoffs reverting to expressions, and the read check before Earth closes. -- confirmed

=====================================================

Opus: 
Let me re-measure before explaining, and look at what was actually in your last commit.Two answers, and the second one is my mistake, not yours.

**Where the heading is.** In the orrery, at `documentation/L322_earth_read_record_20260919.md`. It is the heading of section 2, roughly two thirds of the way down. That file is the read record. The other one, with `_tony_run_record` on the end, is the transcript you filed beside it. -- confirmed

**Why the export is stale: I told you it would not move, and it did.** You followed the outline exactly. The outline was wrong.

Step 1 of that patch printed this: *"Run the orrery maintenance run. Nothing should change except the two files above: this patch touches no value, so the export and every checker should be unmoved."* If you ran the run, it would have reported that it rewrote `data/constants_export.json` — and my sentence had just told you that file should not have moved. Leaving it out of the commit is the sensible thing to do after reading what I wrote. -- i ran the maintenance runner without removing anything from the commit. the record above should confirm that. 

The commit confirms it. `4417217` carries four files: `constants_new.py`, the read record, the run record, and the patch script. `data/constants_export.json` is not among them.

**Why I was wrong, specifically.** The export file stamps itself with a hash of `constants_new.py`. That hash covers the whole file, comment lines included, not only the values. My patch changed comment lines, so the hash changed, so the export needed regenerating even though not one number moved. I had already measured exactly this earlier in the session — I watched the hash go from `b70f2c56` to `179dbd58` on my own test copy — and then wrote an instruction saying the opposite. Having the evidence and writing the contrary is the part I got wrong, not the reasoning about values.

**The fix is one file in each repository.**

In the orrery: run the maintenance run as usual. It will report that it rewrote `data/constants_export.json`. **Commit that file this time** and push. -- again, i commited everything last time. i did not exclude anything. 

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260919T195956Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 0.7s  unchanged (1 of 1 rewritten, content
                                     identical)
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.3s  rewrote data/constants_export.json
  Module atlas                 5.3s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               3.9s  rewrote DATA_INVENTORY.md
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.4s  No figure count exceeds its inputs: 31
                                     derived row(s) read, 15 judged OK -- 15 OK,
                                     16 NOT YET MIGRATED, 1 NO DERIVED LINE.
  Constants export check       0.6s  Export matches the store: sha256
                                     179dbd5877b8 on both sides; 55 rows re-read,
                                     58 not exported, 16 tokens.
  Dimensions                   0.7s  No unit contradicts its arithmetic: 31
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
  Reset completeness          10.5s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.4s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Worksheet checker            7.1s  76 of 114 routed, 8 clean
  Worksheet checker tests     12.5s  All 136 checks passed
  Worksheet key round trip     0.7s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         16.4s  All 76 checks passed
  Extractor pins               0.3s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           8.1s  292 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  16 of 16 gating checkers passed -- 70.1s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          292 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  1890 file(s) examined, 8 written, 0 created, 0 removed, 5 rewritten identically
    written   DATA_INVENTORY.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/constants_export.json
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      LEDGER_CONSOLIDATED.md
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

Then in the gallery: run `tools/pull_constants_export.py`, commit `data/constants_export.json` and `data/constants_export.sha`, and push.

Nothing else changes. No cache rebuild, and no need to pause OneDrive — I tested that on clones before saying it: with the new export in place the gallery still passes all 14 of its offline checkers, Cache in step included, because no exported row value moves.