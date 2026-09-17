# Review -- patch_L322_4_mechanism_20260916.py (L-322, orrery half)

Reviewed against orrery `51d5acd90557b4f9c62f014a5adf563329d16b11`
at https://github.com/tonylquintanilla/palomas_orrery (HEAD, live),
which is the build's base `6b282b2e` plus two filed documents and the
patch script itself at the repo root; no file the patch edits differs
between the two. Gallery at `72a49552aa6ba4b21c2f58e3c5fe53f7d198590c`.

Tony Quintanilla, PE | Claude Fable 5.1 reviewing Claude Opus 5 |
2026-09-16, late evening. Type: REVIEW. Zero code. Mode 7, collegial.

Loaded for this review: provenance-discipline 2.13, safe-file-editing
1.11, agentic-pre-test 1.2, ledger-and-session-records 1.11,
orrery-coding-conventions 1.9, gallery-cache-builder 1.4 -- all
matching the manifest. The upload is byte-identical to the copy at HEAD
(md5 6c0e59dd...).

---

## Verdict

**Run it.** The patch does what the manifest asked, its five departures
are all improvements, and it passed an independent pre-test here. One
finding matters for the NEXT session's order of work, not for running
this patch; it is section 3.

## 1. What was verified here, independently of the build session

On a throwaway copy of HEAD:

- The patch applied (nine `ok` lines) and refused a second run.
- `ledger_index.py` twice: OK: 330, 192 live items.
- `export_constants.py` alone: 23 of 112 rows exported, 89 named with
  reasons (5 retired `dimensionless`, 84 no `# Unit:`), sha256
  7b12aecf..., 12 tokens.
- `test_constants_export.py` alone: five numbered checks, each printing
  what it compared; exit 0.
- `test_dimensions.py` alone: 13 fixtures gave expected verdicts; 31
  derived rows, 25 NO UNIT, 6 NOT CHECKABLE, by name; exit 0.
- `test_derived_figures.py` alone: 31 rows, all NOT YET MIGRATED, 4 NO
  DERIVED LINE, by name; exit 0.
- Full `orrery_maintenance_run.py` under a virtual display: 16 gating
  checkers, 15 passed; the one failure is Reset completeness, which
  fails here because this sandbox has no tkinter (`ModuleNotFoundError`
  at its line 24), not because of the patch. The provenance scanner's
  Tier-1 stayed at 292. The new generator reported "unchanged, not
  written" on a second pass, so the export is deterministic as the
  handoff claims.
- Code read: the two hand rules in `test_dimensions.py` (division by a
  defining constant converts; a non-integer power of a single named
  input is taken on the number in its declared unit) are implemented
  as the manifest specified and guarded so they fire only in their
  case. The figures walk in `test_derived_figures.py` implements the
  textbook rules correctly: fewest figures through products, quotients,
  powers and functions; coarsest decimal place through sums and
  differences; typed numbers and `exact` rows never limit. Rounding is
  `float("%.*g")`, half to even, as Rule 5 says.
- Counts in the handoff checked: 57 EARTH_ rows (the design-round
  handoff's 53 was stale); 31 derived rows by both routes; astropy is
  in `requirements.txt` at line 40.

## 2. The five departures from the manifest -- all accepted

Each is method, each is recorded in the module that carries it, and
each is right:

1. Deriving rows by arithmetic as well as by `# Derived:` line finds 4
   rows the manifest's rule would have missed. That is the enumerate-
   then-decide lesson applied to the checker itself.
2. `dimensionless` as a RETIRED list rather than an unknown token keeps
   the export runnable today while still failing on any other unknown
   name. Correct reading of the per-slice gate.
3. `au` with dimension km, and "named number" as an explicit marker:
   both fix real errors in the manifest's sketch, and the fixtures
   caught the second.
4. No timestamp and no SHA in the export: a maintenance run with no
   store change writes nothing, so nothing spurious gets committed.
   The gallery records the SHA at pull, which is where it belongs.
5. The export checker applying the closed-slice rule to every row, not
   only derived ones: that is what the 2026-09-14 ruling says.

The ledger note the patch writes says "FOUR places the build departed";
the handoff says five (the fifth is item 5 above). Small, and the ledger
is the copy that lasts; a one-line correction can ride the next ledger
touch.

## 3. The finding that matters: 53 of 70 gallery pointers cannot be
## served by this export yet

Measured here by joining the gallery's `objects_config.json` pointers
to the export the patch produces:

    70 pointers: 17 resolve to an exported row,
                 48 point at a row in not_exported
                    (44 with no # Unit: line, 4 declaring dimensionless),
                  5 point outside the store (planet_poles x4, the tide radius).

The 48, by name: ALFVEN_SURFACE_RADII, CHROMOSPHERE_PHYSICAL_RADII,
CORE_AU, EARTH_BOW_SHOCK_JELINEK_EPS, EARTH_BOW_SHOCK_JELINEK_LAMBDA,
EARTH_EQUATORIAL_RADIUS_KM, EARTH_GEOCORONA_RADII,
EARTH_GEOSTATIONARY_RADII, EARTH_HILL_SPHERE_RADII, EARTH_INNER_CORE_KM,
EARTH_LEO_INNER_RADII, EARTH_LEO_OUTER_RADII, EARTH_LOWER_MANTLE_KM,
EARTH_MAGNETOPAUSE_SHUE_A6, EARTH_MAGNETOPAUSE_SHUE_A8,
EARTH_OUTER_CORE_KM, EARTH_STRATOPAUSE_RADII, EARTH_THERMOPAUSE_RADII,
EARTH_UPPER_MANTLE_KM, GRAVITATIONAL_INFLUENCE_AU, HELIOPAUSE_RADII,
HELMET_CUSP_RADII, INNER_CORONA_RADII, INNER_LIMIT_OORT_CLOUD_AU,
INNER_OORT_CLOUD_AU, JUPITER_EQUATORIAL_RADIUS_KM, OUTER_CORONA_RADII,
OUTER_OORT_CLOUD_AU, RADIATIVE_ZONE_AU, ROCHE_LIMIT_RADII,
SOLAR_RADIUS_AU, SUN_RADIUS_KM, TERMINATION_SHOCK_AU (33 distinct
names; several are pointed at more than once).

Why it matters. The handoff's STILL OPEN puts the gallery half BEFORE
the Earth slice, on the reasoning that the two standoffs can only
revert to expressions once the gallery stops parsing the store. That
reasoning is right for those two rows only. But the manifest's piece 6b
has the nightly builder abort on a pointer with no export row, and
piece 6a's Pointer join FAILS on one. Built as written today, the
gallery half would fail on 53 of 70 pointers and, worse, the builder
would refuse to build the nightly cache, which takes the live page
down. That is the parallel-pipeline warning read backwards: the old
check (Store drift, working) must not be turned off before the new one
can go green.

Two ways to resolve it, for the next session to choose (method, not a
ruling):

- **Reorder.** Walk the Earth and Sun rows that the gallery POINTS AT
  before the gallery half -- `# Unit:`, `# Status:`, `# Figures:` on
  those 33 rows plus the two retired-token rows, and the five outside
  values moved in -- leaving only the two standoffs' reversion for
  after the gallery stops parsing. Then the pointer join lands with
  something to join to. This is most of the Earth slice and part of
  the Sun slice, done first.
- **Fall back, named.** Have the builder fill from the export where a
  row exists and keep the hand-copied value where it does not, printing
  every fallback by name; make Pointer join report not-exported
  pointers as named gaps outside a closed slice and FAIL only inside
  one. That is the same per-slice shape every orrery checker in this
  patch already has, and it lets the gallery half land first without
  touching the live page's numbers.

The second keeps the handoff's order and is smaller; the first gets the
join to a real verdict sooner. Either way the manifest's piece 6b
sentence "a missing row is a ValidationAbort naming the pointer" is
wrong as an unconditional rule and should read "inside a closed slice".

## 4. Smaller notes, none blocking

- `constants_new.py` still says in three places that
  `test_derived_figures.py` recomputes the two standoffs. The build
  left the store untouched on purpose and the patch prints the
  reminder. Acceptable; the Earth visit rewrites those Notes.
- The dry-run findings the handoff lists for the Earth walk are real
  properties of the store, not checker faults. Two are worth naming
  now so the slice session is not surprised: the rotation rate should
  get a token whose dimension is `1 / s` (a radian is dimensionless in
  SI; astropy's `rad` is not, and it leaves rad^(-2/3) in the
  geostationary radius); and the typed conversion factors inside
  expressions (`1.0e-9`, `1000`, `60`, `365.25 * 86400`) will each
  report as double-counted once units are attached, which is the
  checker telling the truth: a conversion factor typed into an
  expression is a unit conversion the store should carry as a named
  exact constant or as a declared input unit.
- The handoff and the patch instruct moving the script to
  `documentation/` BEFORE the maintenance run so the module atlas does
  not index it. Correct, and the reverse order would only produce an
  atlas entry to clean up, not a failure.
- Slice membership by name prefix works for Earth and will need an
  explicit list for the Sun; the handoff already says so.

## 5. What this review did not do

It did not run the dashboard (no tkinter here). It did not run the
patch on a CRLF ledger; the build session reports it did. It did not
read every line of the 2,198-line script; it read the two checkers'
judgment paths, the export's rounding, the ledger edits, and the runner
and dashboard edits in the diff.
