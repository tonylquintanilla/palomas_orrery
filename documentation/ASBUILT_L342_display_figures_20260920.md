# As-Built -- L-342: every number in a hover shows the figures its source supports

**Built on gallery `1061ae4d9ad3b7a9b86b483b09db7f9cbd64eed2`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
and orrery `ee37cc1ff911d96e87fd5d714a456b53f2aef50e`
at https://github.com/tonylquintanilla/palomas_orrery.
Both HEADs were read live with `git ls-remote` on 2026-09-20, after the
pushes this document describes. Both are the SHIPPED state, not the
state the work started from.**

Where it started: gallery `cdfa74c3b12cd50e8955acefb75e36f4bcbbe4ca`,
orrery `b3faf14f98d84516b1076599f59ac415a9bf5347`.

**Rules this work ran under, and which C2 will need.** Fetch from the
orrery at `ee37cc1f`: `PROJECT_INSTRUCTIONS.md` (v3.64) and these
skills under `skills/<name>/SKILL.md` -- provenance-discipline 2.15 (the
section "The Figure Count Is a Declared Field", Rules 1 to 8),
interactive-exhibit 1.4, gallery-cache-builder 1.5, gallery-assembler
1.3, safe-file-editing 1.11, agentic-pre-test 1.2,
ledger-and-session-records 1.11. Inside Tony's Project they load as
installed skills; compare each loaded version line with the protocol's
manifest table and STOP on a mismatch. **In your first reply, name the
rule files you actually read.**

**Type: AS-BUILT.** Written after the build and the install, by Claude
Opus 5, builder. Tony Quintanilla integrator. **For:** Claude Fable 5.1,
writing the Stage C2 build manifest.

It supersedes `HANDOFF_L342_display_figures_built_20260920.md`, which was
written before the install and records the build only. Where the two
differ, this one is right: the handoff's anchors are pre-push.

---

## 1. What shipped

Two faults were live on the site at `cdfa74c3`, and both are gone.

The FIRST was formatting. A shell's radius in Earth radii printed to its
declared figures while the kilometre line beside it went through
`fmtKm`, which always rounded to a whole number.

The SECOND was arithmetic, and no formatter could have repaired it. The
hover computed the kilometre line and the altitude FROM the value the
export had already rounded, so the upper atmosphere told a visitor its
altitude was 574 km where its source says 600.

Every "Today" value in the manifest's section 5 was confirmed by
building the hovers in node from the pushed files. Every "After" value
was confirmed twice -- once by a reference script written from the rules
in Python, once by the check, which computes them independently of the
renderer. Nothing in the manifest's table had to be corrected.

| Hover | Line | Was | Now |
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
radius is exactly one Earth radius, exact for counting, so the kilometre
line keeps the planet radius's eight figures.

Verified end to end after the push: the eight served entries are present
in `data/solar-system/coverage_index.json` at gallery `1061ae4d`, read
from a fresh clone of the remote.

## 2. Where the contract was corrected, and by whom

Fable asked for this to be in the record.

**Amendment one, Fable's, on Opus's finding.** The manifest asked for a
check built the way the Arrival check is built, and that check reads
`data/objects_config.json`. The rooms draw their shells from the served
cache, so a check built only on the config could pass while the site
still showed 574 km -- the 2026-09-17 failure. Section 6 gained the
requirement that the check build Earth's hovers from the served cache
and fail if the cache and the config would build different hovers.

**Amendment two, Fable's, correcting Opus.** The page fetches
`data/solar-system/coverage_index.json`; nothing in the page or the
assembler opens `feature_configs.json`. Confirmed here by reading the
page's boot path. The features block sits inline in `coverage_index.json`
and the check reads that.

**Opus was wrong about the cache builder, and Fable was right.** The
worry was that the builder filters a shell's contents and would drop the
new entries. It does not; it copies the whole features block. The
evidence for the worry was a JSON dump truncated at 900 characters,
above the key it was looking for.

**One correction to the manifest, from the build.** Section 2 says
`kmAndAu` is called from 16 places and then names 14. Fourteen is right
and the named list is exactly those fourteen.

**Both gates fired for real.** The cache-versus-config gate caught the
config sitting ahead of its cache during the build, and again during a
deliberate failure drill. That drill also exposed a gap in the check as
first written -- the comparison covered Earth only, so a Sun hover
changed in the config produced no failure. It compares every room now.

## 3. What C2 needs to know about the mechanism

**Counts travel through arithmetic now.** `gallery/feature_renderers.js`
carries `servedFigureField`, `figProduct`, `figPlace`, `figSum` and
`shellKmLines`. `fmtKm` and `kmAndAu` both take an optional count.
`figProduct` keeps the fewest figures among non-exact inputs;
`figSum` uses the coarsest decimal place and reads the count back from
the result's own size; an `"exact"` input is skipped and a missing count
stops the count travelling. That last property is what holds the Sun's,
Jupiter's and Saturn's hovers byte-identical while their slices are
unvisited, and it is what C2 will switch on.

**Rule S before Rule P.** `shellKmLines` prints `radius_km` or
`altitude` as served where the store holds one, and computes from the
most primary served values where it does not. The precedence is
`radius_km`, then `altitude`, then the product of the radius in body
radii. A shell is still DRAWN from `radius`; only what the hover says
changed.

**Units other than body radii are handled before the body-radius
branch.** The Sun's far shells are served in AU, which converts by an
exact factor. This was a real bug caught by the fixture on its first
run: the first version multiplied 94 AU by the solar radius and would
have shown a visitor 65 million km where the number is 14 billion.

**Twelve of the fourteen call sites can carry a count; two cannot.** A
ring edge is served as a bare number of kilometres with nowhere for a
count to sit, and `radius_fraction` is a typed number that no served
object uses at all. Both say so in a comment rather than staying silent.
If C2 wants ring edges counted, they must first become measured entries.

**The bow shock's power rule is wired ahead of its slice.** Its standoff
is `bsR0 x pressure^(-1/epsilon)`, so Rule 3's fewest-figures default
applies and a figure is dropped where the exponent magnifies the input's
uncertainty. Every input reads null today, so the line prints as it
always has. When the magnetosphere slice gives those rows counts, the
rule fires without anyone having to remember it -- **and the row then
owes a reason in words, which is the slice's to write.**

## 4. What C2 will have to do to the check

This is the part most likely to surprise, so it is stated plainly.

`documentation/smoke_display_figures.js` grades 12 Earth hovers and
holds 43 hovers byte for byte against
`documentation/fixture_hovers_cdfa74c3.json`, recorded at gallery
`cdfa74c3`. **The moment C2 gives the Sun's numbers a count, those Sun
hovers change and the fixture goes red.** That is the fixture working,
not breaking.

The handling is a deliberate act, not a nuisance to be cleared:

- Read every named difference and confirm each is the intended change.
- Then re-record with `node documentation/smoke_display_figures.js
  --record`, which rewrites the fixture from the current tree.
- Say in the ledger which hovers moved and why. A re-record that is not
  explained is a fixture that stopped holding anything.
- Rename the fixture to the SHA it was recorded at, and update the
  check's two references to it, so the filename never lies about which
  state it pins.

The check also carries `ACCEPTANCE`, the manifest's own section 5 table
as literal strings. It is a second, independent grader, so that an error
shared between the check's arithmetic and the renderer's cannot pass. If
a served value legitimately moves, that table fails and names the row;
update it with the reason.

A shell in `ACCEPTANCE` that the run never reaches FAILS. So does any
number in an Earth hover the check cannot account for. Both are
deliberate: an unexamined number is a failure rather than a silence.

## 5. The install, and why it is the bigger finding

The fix itself went in cleanly. Getting it to the site took most of the
day, and none of that was the fix.

**The cache builder's swap failed twice**, at 15:00:19Z and 16:57:47Z,
both `[WinError 5] Access is denied` on the `staging -> live` rename.
That is occurrences four and five of L-216. **OneDrive was paused for
both.** The documented mitigation did not work.

**What the two failures left behind.** The swap is two renames: live
becomes `.prev`, then staging becomes live. The error names the second,
so the first had succeeded -- `data/solar-system` was gone and the
complete new generation was sitting in `data/.staging_solar-system_*`,
validated, with its run manifest already written into it. GitHub Desktop
showed 62 deletions and no additions, which reads like data loss and was
not.

**Recovery was a hand rename, and it worked immediately.** Tony renamed
`.staging_solar-system_20260920T165747Z` to `solar-system` in File
Explorer, minutes after Python's rename of the same directory had been
refused. Then the maintenance run passed 15 of 15 gating checkers,
including `Cache in step` and the new `Display figures`, which is the
verification the builder's own post-swap check would have done.

**A timing detail worth carrying.** The two staging folders are 1h57m
apart, and a OneDrive pause is 2 hours. If the pause was taken shortly
before the first run it expired within a minute of the second run's
rename. Not confirmed -- Tony did not record when he clicked pause --
but close enough to act on.

**New evidence, and it is not from the builder.** `data/` holds
`solar-system (1)`, `solar-system (2)`, `solar-system (3)` and
`1260806133443-solar-system`, dated 2026-09-05, 09-10, 09-18 and 09-06.
Those are OneDrive conflict copies. The builder never writes a name like
that. So OneDrive has been failing to reconcile this exact directory for
over two weeks, and the swap failures are the visible end of something
that has been happening quietly. **`1260806133443-solar-system` is
committed and is on the live site now**, tracked in git; the other three
are local only. None of them is gitignored, so any of them could reach
the site on an inattentive commit.

**What this session recommends for L-216, and what is Tony's to
decide.**

1. **(recommend, method)** Put a bounded retry with a short backoff
   around the `staging -> live` rename in `atomic_swap_dir`. The hand
   rename succeeding minutes later is direct evidence the lock is
   transient. This is small, it is inside the builder, and it would have
   made today invisible.
2. **(recommend, method)** Record the SWAP OUTCOME outside the
   generation. The skill already says this comes before fixing the
   cause, and today is why: the run record is written into the staging
   directory, so a run whose swap fails strands its own record in a
   folder `.gitignore` hides, and the committed history shows no sign a
   run lost its data. Both of today's failures are invisible in the
   repo.
3. **(recommend, method)** Add `data/solar-system (*)/` and the
   `<digits>-solar-system` shape to `.gitignore`, so a conflict copy
   cannot reach the site by accident.
4. **(Tony, decide)** Whether to remove `1260806133443-solar-system`
   from the repository. It is tracked, published, and serves nothing.
5. **(Tony, decide)** Whether to move the repositories off OneDrive.
   This is the lasting fix and his answer on 2026-09-17 was "not at this
   time". It changes his machine outside his usual working set and needs
   its steps and risks written out before he decides. **Do not propose
   it casually**, and do not let five occurrences become the argument
   that decides it for him.

Items 1 to 3 are method and belong in the builder and the skill. Items 4
and 5 are Tony's.

## 6. What is on the two repositories now

**Gallery `1061ae4d`.** Eight served entries in
`data/objects_config.json`; `shellKmLines` and the figure arithmetic in
`gallery/feature_renderers.js`; `documentation/smoke_display_figures.js`
and its fixture; the `Display figures` row in
`gallery_maintenance_run.py`, which now runs **15 gating checkers**, up
from 14. The rebuilt cache went out in the same push as the config.

**Orrery `ee37cc1f`.** L-342 records both faults, the fix, the check,
the two amendments, and closes the geocorona altitude it had left open.
L-340 records the second use of the one-off config-write exception. Both
patch scripts are filed in `documentation/`, with the pre-install
handoff and Tony's install record.

## 7. Still open

- **The read check.** L-342 still carries it: the skill says a missing
  `# Read:` on an in-scope row inside a closed slice FAILS, and no check
  does that yet. It must be demonstrated failing before `CLOSED_SLICES`
  changes.
- **Owed to interactive-exhibit's next bump**, from the manifest and not
  cut: a hover prints a served primary where the store has one, and
  computes with Rule P where it does not. Section 3 above is the
  substance of it.
- **Tony's readability judgment**, after he looks at the phone: whether
  any rule-correct number should be shown shorter, by name. Two are
  worth the look -- the geocorona, whose altitude and radius both read
  600,000 km because at one figure they are the same number, and LEO's
  inner edge at 6,578.1366 km. Rule 7 permits fewer; this is taste, not
  correctness.
- **Stage C2 and Stage D**, unchanged and following this build.

No skill was bumped in this session, so nothing is owed forward on that
account.

---

Written September 20, 2026 with Anthropic's Claude Opus 5.
