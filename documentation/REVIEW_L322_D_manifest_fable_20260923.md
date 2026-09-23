# Review -- the L-322 Stage D build manifest (Earth's pole), before the build

**Built on orrery `751aff3f416b22d534578677191d1492b5b41b31`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `36ef1727ca22fcc51badebad052a1a322b650dd1`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io,
the SHAs the manifest names; both cloned and checked out there.** Both
remotes read live on 2026-09-23 have moved since: orrery `ac25d4f4`
(one commit, a run record added under documentation/) and gallery
`2e0fa8f5` (three commits: L-303 gallery-card work and a nightly cache
build). Of the files Stage D edits, only `coverage_index.json` moved,
and the cache build rewrites that anyway. The build session re-anchors.

**Type: REVIEW.** Written September 23, 2026 by Claude Fable 5.1,
inside Tony's Project. Reviews
`BUILD_MANIFEST_L322_D_earth_pole_20260922.md` by Claude Opus 5.5.
Nothing built, nothing edited.

## The gate, and the rule files I read

The provenance-discipline copy mounted in this session reads 2.15; the
protocol table reads 2.17. That is the Stale Skill = Stop mismatch, and
a reinstall cannot clear it from inside this session. I read 2.17 from
the repo at `751aff3f`, byte-identical to the copy Opus's session
byte-compared: Rules 2, 3, 6 and 7, The ceiling, One Value One Home, A
Drawing Approximation Does Not Promote, When the source gives a range.
Protocol v3.67: Fetched vs Recalled, The Braid. Other skills: version
lines only. Code at `751aff3f`, read and RUN: `test_dimensions.py` and
`test_derived_figures.py` on a throwaway store carrying the manifest's
proposed rows; `constants_tokens.py`; `export_constants.py`'s exact
branch; the gallery's `fmtServed`.

## What I re-measured, and what I accepted

Re-measured, all agree with the manifest: every line number in 2.1,
2.3, 2.4 and 3 (`idealized_orbits.py` 50-60 and 3352,
`feature_renderers.js` 70 and 74, `constants_new.py` 114 and 368,
`test_mirror_constants.py` 373, `objects_config.json` 862); the
obliquity arithmetic (84381.448 / 3600 = 23.439291111); the sidereal
period (23.93447 h at seven figures); the skill's self-contradiction on
opacity and point count (section 9 is right about which section says
which). Accepted as written: the reading of the 2015 IAU report, the
Horizons manual, the pole comparisons in 2.5, and the counts in 2.6.

---

## Findings

### 1. The rotation-period row fails the unit checker as written. -- **blocks the build**

Manifest 4.1. I wrote `2 * math.pi / EARTH_ROTATION_RATE_RAD_S /
3600.0` into a throwaway store with an `hours` token and ran
`test_dimensions.py`. Verdict: MISMATCH, "the arithmetic gives
0.006648 hours; the store holds 23.93447". The `rad_s` token is
defined as 1/s with the radian dropped, so 2 pi over the rate is
seconds; dividing by a bare 3600 leaves it in seconds; the checker
converts seconds to hours itself and finds 0.0066, not 23.93. The
figures checker passes it at seven, which is why a run of that checker
alone would look green.

The fix is the 2.17 pattern, an exact conversion row that carries the
unit: `S_PER_HOUR = 3600.0`, unit `s_per_h`, dimension s/h, exact, a
definition; then `2.0 * math.pi / EARTH_ROTATION_RATE_RAD_S /
S_PER_HOUR`, unit `hours`. Tested: both checkers pass, 23.93447 hours,
seven figures. Two pi stays a bare number on purpose, because the rate
token already treats the radian as dimensionless; giving 2 pi a `rad`
unit fails the check the other way (tested: "declares s; the
arithmetic gives rad s"). Section 4.1 should say all of this, and 4.1's
`hours` token needs `s_per_h` beside it.

### 2. Section 6's question: Rule 7 does not yet answer an exact row, and the answer is method. -- **fix before the build, in the 2.18 bump**

Manifest 6. Measured on the gallery: `fmtServed` prints a row served
as `"exact"` with `value.toFixed(digits)`, a number of places chosen at
each site. Today's exact rows are 2.0, 120, 4.5 and the like, so no one
noticed; for 23.439291111... it is exactly the page choice 2.17's Rule 7
forbids. So Opus is right that the rule does not express this case. It
is not Tony's, because it resolves the same way for any exact row.

The answer, proposed as skill text for 2.18:

- **An exact quantity is stored in the form its definition prints.**
  The obliquity's definition is 84381.448 arcseconds, so the store holds
  `EARTH_OBLIQUITY_J2000_ARCSEC = 84381.448`, unit `arcsec`, declared, a
  frame parameter; and `EARTH_OBLIQUITY_J2000_DEG` is an expression over
  it and an exact conversion row `ARCSEC_PER_DEG = 3600.0` (token
  `arcsec_per_deg`). That is Rule 6's whole-from-parts form, and it
  means the unit checker judges the degree row instead of reading a
  no-input literal, as it does `DEG_PER_RAD` today.
- **An exact row prints its definition's digits.** The export carries,
  for an exact or declared row, a `print` count: Rule 2 applied to the
  defining literal (84381.448 is 8; 2.0 is 2; 120 is 3; 4.5 is 2). A
  derived exact row inherits the print count of its defining input.
  The page prints exact rows by `print` and `toFixed` goes for them.

Under that rule the tilt prints 23.439291 degrees, eight figures, the
digits typed today, now for a reason. The period row, being derived
from a measured rate, is unaffected: seven figures, 23.93447 hours.

This belongs in the same bump section 9 already schedules for the
drawing-number ruling, since one session ships one version of a skill.

### 3. Tony ruled the magnetotail sizes and belt thickness are handled in this build; the build sections do not have them. -- **fix before the build**

Manifest 9 says the magnetotail's 100, 15 and 25 Earth radii and the
belt thickness 0.5 "are handled in this build". Sections 4, 5 and 10
never mention them. As written, the ruling is recorded and not
executed. Add to 4.1: declared rows in the store, with the reason on
each row, under the 2.17 principle that a row feeding a drawn value is
in bound whatever its count; to 5: pointer entries in Earth's config
replacing the typed copies; to 4.3: `earth_visualization_shells.py`
reads the rows; to 10: no number that moves where something is drawn
is typed in both repositories.

### 4. The precession rate: the token, and the obliquity's own drift. -- **fix before the build**

Manifest 4.1, third bullet. "With a token the table knows" would force
the builder to convert the printed rate in its head, because the table
has no token for arcseconds per century or per year. Under Rule 4 and
Rule 6 the row holds the rate in the unit the chapter prints it, with a
token added for that unit, and any degrees-per-year form is derived
from it through an exact conversion row.

Show or cap reaches the obliquity the same way it reaches the pole. The
served tilt is the frame's fixed parameter, but a visitor reads
"tilted 23.439291 degrees" as Earth's tilt today, and the real
obliquity drifts. Two honest forms, and the manifest should pick one
rule for both rows: serve the obliquity's rate from the same chapter
and show it beside the tilt, or have the hover say the tilt printed is
the frame's definition, Earth's mean obliquity at the year 2000, and not
a value for today. Either is method; a manifest that shows the pole's
rate and is silent on the tilt's has applied the rule to one row.

### 5. Smaller points. -- **notes**

- **"IAU 2006".** Opus rightly makes no claim about what that standard
  gives. For the record, and marked as RECALLED, not sourced: my
  training memory has IAU 2006 adopting a mean obliquity a few
  hundredths of an arcsecond below 84381.448. Nothing should be
  written from that; the label goes, so no read is needed. One thing I
  did see today in a search result, a NAIF frame kernel: other
  "ecliptic of J2000" definitions in circulation use 84381.412 (DE405).
  That is the reason the row must name WHOSE frame, Horizons', which
  the manifest already does.
- **The pole rows as exact.** Defensible, and the row's words carry
  the load: the frame was built from Earth's mean pole of 2000, so the
  pole is the frame's axis by construction, up to the offset TN36
  chapter 5 gives. The RA of a pole at declination 90 is arbitrary;
  the row should say so.
- **The moved pole dict.** Dict values are not top-level rows, so no
  store checker will see the other bodies' entries; 4.2 should say
  that in words, so the move is not read as bringing them under check.
  Each closes in its body's slice, as section 7 records.
- **The 2.18 bump.** The contradiction is real, measured: A Drawing
  Approximation Does Not Promote keeps opacity and point count "in the
  store"; One Value One Home says they "stay where they are drawn".
  Tony's ruling settles it for the drawing code. Finding 2's exact-row
  form rides the same bump.

## For the ledger, one row per class

- **A conversion by a bare number inside a store expression** (a 3600,
  a 60, a 1000). The unit checker converts units itself, so a bare
  divisor makes the stored value disagree with the arithmetic. The
  conversion is an exact row with a compound-unit token. Instances
  found today: the period row as drafted; the class also reaches
  `LIGHT_MINUTES_PER_AU` and its neighbours in the NOT YET MIGRATED
  list.
- **Exact rows printed by a page-chosen width.** Every `"exact"` served
  row prints by `toFixed` today; retired by the print count of
  Finding 2.

---

Written September 23, 2026 with Anthropic's Claude Fable 5.1.
