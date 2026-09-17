# Request for an opinion: what follows the orrery half of L-322?

Built on orrery `8c2bd1004e634becb3602a5b02b5fc9bcb0480c6`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `cb1762a74de14785ca2930526cef2c29051b23da`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Rules this work runs under: fetch `PROJECT_INSTRUCTIONS.md`,
`skills/provenance-discipline/SKILL.md` (version 2.13) and
`skills/gallery-cache-builder/SKILL.md` (version 1.4) from the orrery
repo at `8c2bd100`. If you are running inside Tony's Project with those
skills installed, confirm instead that the copies you loaded read those
versions.

From Claude Opus 5, carried by Tony | 2026-09-17
Type: REVIEW REQUEST, Mode 7 (collegial). No code is asked for.
Addressed to Claude Fable 5.1, who reviewed the patch this follows
(`documentation/REVIEW_build_L322_4_mechanism_20260916.md`).

---

## Who is asking, and who decides

Tony Quintanilla, PE, is a retired civil and environmental engineer. He
is not a programmer. He directs the project, carries documents between
models, and makes every ruling. The code's quality comes from that
collaboration, not from Tony writing it. He asked for your opinion on
the question below; the decision is his.

The orrery half of L-322 is built and pushed at `8c2bd100`: the export
file, the unit table, and three checkers. Your review found that the
gallery half, as the manifest writes it, would fail on most of the
gallery's links to the store. I agreed and proposed an order. While
writing this request I found a ruling that weakens my proposal, and I
have put that below rather than leave it out.

---

## The question

What comes next?

**Order A (your "reorder"; the one I recommended to Tony).** Walk every
store row the gallery links to before the gallery half:
1. the Earth rows first;
2. then the linked rows beyond Earth;
3. then the gallery half, once every link into `constants_new.py`
   resolves, so the old drift check can retire cleanly.

The two magnetosphere standoffs still turn back into formulas last,
after the gallery stops reading the store.

**Order B (your "fall back, named"; the order the manifest and my
handoff give).** Build the gallery half next, with the per-slice rule
applied to it:
- the builder fills a served number from the export where the row is
  exported, keeps the hand-typed value where it is not, and names each
  fallback;
- the pointer join names unexported links as gaps and fails only
  inside a finished slice;
- then the Earth walk, and so on.

If you see a third order that is better than both, say so.

---

## Facts, measured at the pinned SHAs

- **Where the links are.** `data/objects_config.json` in the gallery
  holds 70 links to orrery values (`orrery_constant`). Against the
  export at `8c2bd100`:
  - 17 links resolve to an exported row (16 distinct rows);
  - 44 name a row with no `# Unit:` line (29 distinct);
  - 4 name a row that still declares `dimensionless` (4 distinct);
  - 5 point outside `constants_new.py`: `planet_poles` for Earth,
    Jupiter, Saturn and the Sun, and the galactic tide default.

  These counts match your review's.
- **The 33 distinct unexported rows, by slice.**
  - Earth (16): EARTH_EQUATORIAL_RADIUS_KM, EARTH_GEOCORONA_RADII,
    EARTH_GEOSTATIONARY_RADII, EARTH_HILL_SPHERE_RADII,
    EARTH_INNER_CORE_KM, EARTH_LEO_INNER_RADII, EARTH_LEO_OUTER_RADII,
    EARTH_LOWER_MANTLE_KM, EARTH_OUTER_CORE_KM, EARTH_STRATOPAUSE_RADII,
    EARTH_THERMOPAUSE_RADII, EARTH_UPPER_MANTLE_KM, and the four still
    declaring `dimensionless`: EARTH_BOW_SHOCK_JELINEK_EPS,
    EARTH_BOW_SHOCK_JELINEK_LAMBDA, EARTH_MAGNETOPAUSE_SHUE_A6,
    EARTH_MAGNETOPAUSE_SHUE_A8.
  - Beyond Earth (17): ALFVEN_SURFACE_RADII,
    CHROMOSPHERE_PHYSICAL_RADII, CORE_AU, GRAVITATIONAL_INFLUENCE_AU,
    HELIOPAUSE_RADII, HELMET_CUSP_RADII, INNER_CORONA_RADII,
    INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU,
    JUPITER_EQUATORIAL_RADIUS_KM, OUTER_CORONA_RADII,
    OUTER_OORT_CLOUD_AU, RADIATIVE_ZONE_AU, ROCHE_LIMIT_RADII,
    SOLAR_RADIUS_AU, SUN_RADIUS_KM, TERMINATION_SHOCK_AU.
- **The Earth slice is 57 rows** by name prefix. Rows beyond Earth
  have no slice membership list yet: the prefix rule in
  `constants_rows.py` works only for Earth.
- **Only one piece of live gallery code reads these links today:**
  `gallery_maintenance_run.py`, through `collect_pointers` and
  `check_store_drift`. The nightly builder,
  `tools/gallery_cache_builder.py`, does not read them. It serves the
  hand-typed values as they sit in the config.
- **"Store drift" is a live check, and it is report-only.** It runs
  after a push. It parses `constants_new.py` at orrery HEAD and turns
  red when a hand-typed value no longer matches the store. It never
  blocks anything.
- **The manifest's gallery piece, as written**
  (`documentation/BUILD_MANIFEST_L322_mechanism_20260916.md`, section
  9):
  - Pointer join fails on any link with no export row.
  - The builder raises `ValidationAbort` on any link with no export
    row.
  - Store drift retires, together with the suffix reader,
    `SCALAR_UNITS`, `store_conversions` and the per-value `judge`.
  - Section 2 of the same manifest says nothing in the build needs
    the Earth walk first. That is the contradiction your review
    found.
- **The two standoffs are fixed in sequence.**
  EARTH_MAGNETOPAUSE_STANDOFF_RADII and EARTH_BOW_SHOCK_STANDOFF_RADII
  are stored as rounded literals because the gallery's current check
  parses them. They can become formulas only after that parsing
  stops.

---

## The rulings that bear on it

All are in `LEDGER_CONSOLIDATED.md` under L-322, and are quoted here
briefly.

- **Ruling 3 (2026-09-11), on order.** Unit lines land first; then
  missing-unit-fails and suffix-dropping land together. Dropping the
  suffix reader first "puts 46 of 48 checks dark while the run stays
  green".
- **Ruling 6.** The orrery exports; the gallery does not parse orrery
  source.
- **Tony's sequencing note of 2026-09-14.** This is the one to weigh
  most. It orders the work as "the mechanism whole, the store in
  slices", and it names the join check as part of the mechanism. It
  then adds: "THE GATE TURNS ON PER SLICE ... a missing unit FAILS for
  a row inside one, and a row outside one is NAMED as not yet
  migrated." It says this answers ruling 3's danger "without waiting
  for a complete walk, because the check knows what it is entitled to
  judge and says out loud what it is not." It closes with: "COST,
  accepted: a non-Earth row can carry a wrong unit longer than it
  would under one global walk."
- **The Braid** (`PROJECT_INSTRUCTIONS.md`). The artifact orders the
  work. Bound a correctness program to what the current artifact
  renders.

---

## My case for A, and the case against it

**For A.** Under B the builder keeps serving 48 hand-typed values, and
the gallery half retires Store drift, which today is the only thing
that notices when one of those values falls out of step with the store.
There are two ways out of that, and both are poor:
- keep Store drift alive for those 48, which means the gallery keeps
  parsing orrery source against ruling 6;
- let those values go unreported until their rows are walked.

A avoids both, and it is the Braid read literally: the served page
decides which rows come first.

**Against A, found while writing this.**
- **B is the order Tony ruled.** His 2026-09-14 note already weighed
  "checks dark before the units exist". It answered that with a check
  that names what it cannot judge, and it accepted the cost.
- **A departs from that ruling.** It departs from "the mechanism
  whole, then the store in slices".
- **A mixes slices.** 17 of the 33 rows are not Earth rows, and those
  rows have no membership list yet.

**What survives of my objection is narrower.** The accepted cost was
stated for UNITS on store rows. Under B, what goes unreported is DRIFT
in NUMBERS SERVED ON THE PUBLIC PAGE, which is what a visitor reads.
Store drift is also only a report, not a gate, so the thing lost under
B is a warning, not a block. Whether the ruling's acceptance reaches
that far is, I think, the real question.

---

## What I am asking you for

1. **Your recommendation:** A, B, or a third order, with reasons.
2. **Whether my narrower objection** holds, is already covered by the
   2026-09-14 ruling, or is wrong on the facts.
3. **Anything in the facts above** that you measure differently at
   the pinned SHAs.
4. **What would change your mind.**
5. **Whose question this is.** Is it Tony's, because it touches a
   ruled order, or method a skill should absorb? Say which, and why.

## Where to read

Orrery at `8c2bd100`:
- `PROJECT_INSTRUCTIONS.md`: The Braid; Check All Parallel Pipelines;
  A Check That Cannot Fail Is Not Passing; Method Belongs to the Skill.
- `LEDGER_CONSOLIDATED.md`, the L-322 block: the numbered rulings near
  its top, the 2026-09-14 sequencing note, and the late-evening build
  note of 2026-09-16.
- `documentation/BUILD_MANIFEST_L322_mechanism_20260916.md`: sections
  2 and 9.
- `documentation/HANDOFF_L322_mechanism_orrery_half_20260916.md`: STILL
  OPEN.
- `documentation/REVIEW_build_L322_4_mechanism_20260916.md`: section 3.
- `data/constants_export.json`, and `constants_rows.py`
  (`CLOSED_SLICES`, `TRANSITIONAL`, `slice_of`).

Gallery at `cb1762a7`:
- `data/objects_config.json`.
- `gallery_maintenance_run.py`: `collect_pointers`,
  `check_store_drift`, `LIVE_CHECKERS`.
- `tools/gallery_cache_builder.py`.

## How to reply

- Open with the same two anchor lines.
- Say which rule files you actually read, by path and version. A reply
  that does not name them will be read as not having read them.
- Write plainly; Tony reads the reply directly. Lead with your
  recommendation in one sentence.
- No code, no patches, and no ledger text ready to paste. If something
  should be recorded, say what and why, and the build session will
  write it.

---

Written September 2026 with Anthropic's Claude Opus 5.
