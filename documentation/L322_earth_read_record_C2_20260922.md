# L-322 Earth slice -- the read record, Stage C2

Built on orrery `efd2e2ba2da47fd01505b1ee9f8bfca4758cee74`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `1ae9de50c71089a9f56e607e5eb84732ab519075`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Both HEADs were read live with `git ls-remote` on 2026-09-22 and both
repositories were cloned at those SHAs. The orrery moved once during the
session, from `d4f6d7f0` to `efd2e2ba`, which adds only
`documentation/project_instructions_v3_67.md`; the gallery moved from
`870325c8` to `1ae9de50`, which changes one gallery card's shape and a
timestamp. Neither touches this build.

**Type: READ RECORD.** Session of 2026-09-22, Tony with Anthropic's
Claude Opus 5. Companion to
`documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md`,
sections 4.2 and 17.6.

**What this file is.** A `# Read:` line on a row records that somebody
opened the source and checked it against the number beside it. This file
is the long form for Stage C2: what was opened, where in it, what it
says, and the verdict.

**Who read.** Under provenance-discipline 2.17, The Read Field, the
reader is decided by ACCESS. Three sessions did the reading for these
rows and each row's line names the one that read it.

- **Claude Fable 5.1, 2026-09-11**, from Tony's downloaded PDFs of Shue
  et al. (1998) and Jelinek et al. (2012). Recorded in
  `documentation/L305_gap1_read_record_20260911.md`; fourteen rows take
  their line from there and nothing was re-read here, because neither
  paper can be opened from a sandbox (Wiley refuses automated access,
  which is not a paywall).
- **Claude Opus 5, 2026-09-21**, recorded in
  `documentation/NOTE_L322_C2_rev3_check_opus_20260921.md` and NOT
  repeated in this session: Baker (2018), Meredith (2014), Li, Tu et al.
  (2024), Alken et al. (2021) including its Table 4, and the NOAA
  IGRF-13 coefficient file.
- **Claude Opus 5, 2026-09-22**, this session: the two sources the
  manifest left for the builder, below.

**Section 3, "For Tony to read", is empty.** Every source a row in this
stage needs was opened by a model.

---

## 1. Read this session, by Claude Opus 5, 2026-09-22

### Slavin et al. (1983), the distant magnetotail

Opened: the NASA Technical Reports Server record at
https://ntrs.nasa.gov/citations/19830066648
Title as printed: "Average configuration of the distant (less than
220-earth-radii) magnetotail - Initial ISEE-3 magnetic field results".
Authors as printed: J. A. Slavin, B. T. Tsurutani, E. J. Smith,
D. E. Jones, D. G. Sibeck. Geophysical Research Letters, volume 10,
1 October 1983. The full text is walled; the abstract is open and states
the claim, which is what The Access Standard asks of a partial source.

| Row | Where | What it says | Verdict |
| --- | --- | --- | --- |
| `EARTH_MAGNETOTAIL_OBSERVED_RADII` | abstract | the magnetotail retains much of its near-Earth structure out to X = -220 earth radii; flaring ceases at 100-120 earth radii; the tail diameter settles near 60 earth radii | AGREES with 220. Two figures: the abstract prints 220 and says nothing that makes its zero significant. |

The abstract also prints "Beyond X = -100 to -1200 earth radii", where
-120 is meant. The row's Access line already records that typo and it is
unchanged.

### Li et al. (2025), the outer belt's band

Opened: the open PDF at https://par.nsf.gov/servlets/purl/10575739
Title as printed: "A New Electron and Proton Radiation Belt Identified by
CIRBE/REPTile-2 Measurements After the Magnetic Super Storm of 10 May
2024". Authors as printed: Xinlin Li, Zheng Xiang, Yang Mei, Declan
O'Brien, David Brennan, Hong Zhao, Daniel N. Baker, Michael A. Temerin.
Journal of Geophysical Research: Space Physics 130, e2024JA033504,
doi:10.1029/2024JA033504.

| Row | Where | What it says | Verdict |
| --- | --- | --- | --- |
| `EARTH_VAN_ALLEN_OUTER_BAND_LOW_L` | sec. 1, first paragraph, p. 1 | the inner belt is centred near L = 1.5, and the outer radiation belt "is most intense around L = 4 and 5" | AGREES with 4. One figure: the page prints "4". |
| `EARTH_VAN_ALLEN_OUTER_BAND_HIGH_L` | the same sentence | as above | AGREES with 5. One figure: the page prints "5". |

The same paragraph defines L as the geocentric distance in Earth radii
at the magnetic equator, which is why these two rows carry the
`l_shell` token and the hover says "at the equator".

Two papers that corroborate the band -- Li et al. (2015),
doi:10.1002/2014JA020777, and Kellerman et al. (2014) as reported in
arXiv:1809.00902 -- were carried over from the peak row's old
`# Declared:` prose onto these two rows as `# Source+:` lines. They were
NOT re-read in this session, and the rows say so.

---

## 2. Taken from the two earlier records, not re-read

Fourteen rows take their line from the L-305 record of 2026-09-11, each
naming the table, equation or section that record names, its date and
Claude Fable 5.1: Shue's eight coefficients (Table 1 "After Fit",
p. 17,698), Jelinek's R0 and epsilon (eq. 14, p. 5) and lambda (sec. 4,
after eq. 11, p. 4), the bow shock cut angle (sec. 2 para. 9, p. 2), and
the two crossing-scatter rows (Shue p. 17,697; Jelinek fig. 7).

Eleven rows take their line from the Opus note of 2026-09-21: the five
belt rows, and the six IGRF-13 coefficient rows (the file's 2020.0
column and its 2020-25 secular variation column).

## 3. For Tony to read

Empty. Nothing in this stage needs a source only he can open.

## 4. Rows deliberately given no read line

- **Every expression row**, including the four new kilometre and AU
  rows, Earth's dipole tilt and its rate, and the outer belt's drawn
  peak. A derived row has nothing to read against; checking it means
  checking its inputs, which its Status line names.
- **The three declared solar wind conditions and the two cut angles.**
  A declared drawing choice has no source to read against. The bow shock
  cut angle is the exception that keeps its line: the seven hours it
  converts were read, and the line records that read.
- **`DEG_PER_RAD`**, an exact definition.

---

Written September 2026 with Anthropic's Claude Opus 5.
