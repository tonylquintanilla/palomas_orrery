# Handoff -- L-342: every number in a hover shows the figures its source supports

**Built on gallery `cdfa74c3b12cd50e8955acefb75e36f4bcbbe4ca`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
and orrery `b3faf14f98d84516b1076599f59ac415a9bf5347`
at https://github.com/tonylquintanilla/palomas_orrery.
Both HEADs were read live with `git ls-remote` on 2026-09-20 and both
repositories were cloned there.**

The orrery anchor is one commit ahead of the build manifest's
`2978ceeb`. That commit is Tony filing the manifest itself: 296 lines,
one file, no code. Checked rather than assumed.

Type: AS-BUILT. Prepared September 20, 2026 by Claude Opus 5, builder,
from `documentation/BUILD_MANIFEST_L342_display_figures_20260920.md` by
Claude Fable 5.1. Nothing is pushed; both patches are for Tony to run.

---

## 1. The gates, discharged

All eleven installed skills matched the v3.64 manifest table at load.
That clears three carried obligations: provenance-discipline **2.15**
(v3.64's), interactive-exhibit **1.4** and gallery-cache-builder **1.5**
(v3.62's). No skill was bumped in this session, so none is owed forward.

Rule files read: PROJECT_INSTRUCTIONS v3.64; provenance-discipline 2.15,
Report to the Figures You Have and Rules 1 to 8; interactive-exhibit
1.4; gallery-cache-builder 1.5; safe-file-editing 1.11, Transactional
Patching and Delivery Format; and the manifest rows of
gallery-assembler 1.3, agentic-pre-test 1.2 and
ledger-and-session-records 1.11.

## 2. What was wrong, and what it reads now

Two faults, both live on the site at `cdfa74c3`.

The FIRST was formatting. A shell's radius in Earth radii printed to its
declared figures; the kilometre line beside it went through `fmtKm`,
which always rounded to a whole number. The outer core read "3,480 km"
beside a radius declared to five figures.

The SECOND was arithmetic, and no formatter could have repaired it. The
hover computed the kilometre line and the altitude from the value the
export had already rounded. The upper atmosphere told a visitor
"Altitude: 574 km" -- (1.09 - 1) x 6378.1366, worked from a radius
rounded to three figures -- where its source says 600. No rounding of
574 gives 600.

Every "Today" value in the manifest's section 5 was confirmed by
building the hovers in node from the pushed files, and every "After"
value was confirmed twice: once by a reference script written from the
rules in Python, and once by the check, which computes them
independently of the renderer.

| Hover | Line | Today | After |
| --- | --- | --- | --- |
| Inner Core | radius | 1,222 km | 1,221.5 km (3) |
| Outer Core | radius | 3,480 km | 3,480.0 km (3) |
| Lower Mantle | radius | 5,710 km | 5,710 km (3) |
| Upper Mantle | radius | 6,347 km | 6,346.6 km (3) |
| Crust | radius | 6,378 km | 6,378.1366 km (3) |
| Lower Atmosphere | altitude | 51 km | 50 km (2) |
| Lower Atmosphere | radius | 6,429 km | 6,428 km (3) |
| Upper Atmosphere | altitude | 574 km | 600 km (2) |
| Upper Atmosphere | radius | 6,952 km | 6,980 km (3) |
| LEO inner edge | altitude | 200 km | 200 km (3) |
| LEO inner edge | radius | 6,578 km | 6,578.1366 km (3) |
| LEO outer edge | altitude | 2,000 km | 2,000 km (3) |
| LEO outer edge | radius | 8,378 km | 8,378.1366 km (3) |
| Geostationary | altitude | 35,786 km | 35,786.03 km (3) |
| Geostationary | radius | 42,164 km | 42,164.17 km (3) |
| Geocorona | altitude | 631,436 km | 600,000 km (1) |
| Geocorona | radius | 637,814 km | 600,000 km (1) |
| Hill Sphere | altitude | 1,492,484 km | 1,490,000 km (3) |
| Hill Sphere | radius | 1,498,862 km | 1,500,000 km (3) |

The Crust row is the one the manifest asked the builder to work out. Its
radius is exactly one Earth radius, which is exact for counting, so the
kilometre line keeps the planet radius's eight figures.

## 3. Where the contract was corrected, and by whom

**Amendment one, Fable's, on Opus's finding.** The manifest asked for a
check built the way `smoke_arrival.js` is built, and that check reads
`data/objects_config.json`. The rooms draw their shells from the served
cache, so a check built only on the config could pass while the site
still showed 574 km. That is the 2026-09-17 failure. Section 6 gained
the requirement that the check build Earth's hovers from the served
cache and fail if the cache and the config would build different hovers.

**Amendment two, Fable's, correcting Opus.** The page fetches
`data/solar-system/coverage_index.json`. Nothing in the page or the
assembler opens `feature_configs.json`. The check reads
`coverage_index.json`. Verified here: the page's boot path fetches that
file and the config, and the features block sits inline in it.

**Opus was wrong about the cache builder**, and Fable was right. The
worry was that the builder filters a shell's contents and would drop the
new entries. It does not; it copies the whole features block. The
evidence for the worry was a JSON dump truncated at 900 characters,
above the key it was looking for. The whole Earth features block is
identical in the config and both cache files.

**One small correction to the manifest, for the record.** Section 2 says
`kmAndAu` is called from 16 places and then names 14. Fourteen is right
and the named list is exactly those fourteen. Two of them can never
carry a figure count as the data stands: the ring edges, served as bare
numbers with nowhere to put one, and the `radius_fraction` path, which
no served object uses at all. Both now say so in a comment rather than
staying silent.

## 4. What is delivered

`patch_L342_2_display_figures_20260920.py`, for the GALLERY repo.
Nineteen anchored edits and eight served slots across three files, two
files created. It guards on a content fingerprint of each file it
edits, translates its anchors to CRLF where a working copy holds them,
writes nothing unless every anchor matches exactly once, and refuses a
second run.

`patch_L342_3_ledger_display_figures_20260920.py`, for the ORRERY repo.
Two ledger edits: L-342 records both faults, the fix, the check, the two
amendments above, and closes the geocorona altitude it had left open;
L-340 records the second use of the one-off config-write exception, which
that item asked for. It fingerprints the ledger OUTSIDE the INDEX zone,
so running `ledger_index.py` before or after makes no difference.

## 5. What is permanent, and what is disposable

Both scripts are one-shot and are filed in `documentation/` after they
run. What they install is not: the eight served slots, `shellKmLines`
and the figure arithmetic in the renderer, the new check, its fixture,
and the runner row.

## 6. How it was verified

- The check was demonstrated RED on the unpatched tree: 34 findings,
  naming the outer core and the 574 km among them.
- It was demonstrated red three further ways after the fix -- a count
  ignored at one call site, a served `altitude` removed so the browser
  falls back to subtracting, and a count-less Sun hover changed by one
  character -- and its own self-test makes the rules and the grader go
  red on demand nine ways before it grades anything.
- The delivered patch was run on a clean clone and the result compared
  against the tree these tests were run on: identical, file for file.
- `py_compile` on both patch scripts and the edited runner;
  `node --check` on the renderer and the check.
- The whole gallery maintenance run: **15 of 15 gating checkers pass**,
  up from 14. Cache in step, Config mirror check, Pointer join, Feature
  renderers, Page framing, Sun shells, Earth scene geometry, Hover
  budget, Arrival, Display figures, Artifact 1 assembler, and the four
  suites above them.
- The mirror reports NO CHANGE, which is the manifest's own proof the
  patch wrote the export's numbers. Served links went from 37 to 45,
  every one holding the export's value, unit and count.

The cache rebuild was SIMULATED in the sandbox, by copying the config's
features block into both cache files, because the real builder needs
Horizons and this sandbox cannot reach it. That the two are byte
identical was checked at `cdfa74c3` before the patch. Tony's real cache
builder run is the authority.

## 7. The finding worth keeping

The fixture earned its place on its first run. It caught a fault the
builder had just introduced: the Sun's termination shock is served in
AU, not in body radii, and the first version of `shellKmLines`
multiplied 94 AU by the solar radius. It would have told a visitor
65 million km where the number is 14 billion, in a hover nothing else in
this build was looking at. The lesson is the old one -- a byte-for-byte
hold on everything you did NOT mean to change is what finds the thing
you did not mean to change.

A second, smaller one came from the failure drill. The cache-versus-
config comparison was written for Earth alone, and the drill that
changed a Sun hover in the config produced no failure. It compares every
room now.

## 8. Tony-actions

1. **(do)** Run `patch_L342_2_display_figures_20260920.py` from the
   gallery ROOT, then follow the order the patch prints. The new check
   is RED until the cache is rebuilt, on purpose.
2. **(do)** Run `patch_L342_3_ledger_display_figures_20260920.py` from
   the orrery ROOT, then `python ledger_index.py`.
3. **(look, after the push)** Earth's room on the phone, with section 2's
   table beside you.
4. **(decide, after looking)** Whether any rule-correct number should be
   shown shorter for readability, by name. Two are worth the look: the
   geocorona, whose altitude and radius now both read 600,000 km because
   at one figure they are the same number, and LEO's inner edge at
   6,578.1366 km.

## 9. Owed forward

Nothing is owed to a skill bump from this session; none was made. The
interactive-exhibit line the manifest listed as owed and not cut --
that a hover prints a served primary where the store has one and
computes with Rule P where it does not -- is still owed to that skill's
next bump.

Stage C2 and Stage D are unchanged and follow this build.

---

Written September 20, 2026 with Anthropic's Claude Opus 5.
