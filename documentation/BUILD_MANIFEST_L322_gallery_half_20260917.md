# Build Manifest -- L-322, the gallery half (the export consumed)

**Built on gallery `cb1762a74de14785ca2930526cef2c29051b23da`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io and
orrery `8c2bd1004e634becb3602a5b02b5fc9bcb0480c6`
at https://github.com/tonylquintanilla/palomas_orrery. Both HEADs read
live at the time of writing.**

**Type: BUILD CONTRACT.** Written before the build, zero code.
**Supersedes section 9 of
`documentation/BUILD_MANIFEST_L322_mechanism_20260916.md`** (orrery
repo), which was wrong in two places: it retired Store drift while 48
links had nothing to join to, and it put the join in a file the page
does not read. Sections 1 to 8 and 10 to 14 of that manifest stand; the
orrery half they describe is built at `8c2bd100`.

**Prepared:** September 17, 2026 by Claude Fable 5.1, Tony Quintanilla
integrator. **Continues from**
`documentation/REPLY_L322_order_question_Fable_20260917.md` (order C)
and Tony's ruling of the same day (section 2).

**Skills this build fires:** gallery-cache-builder 1.4 (the config,
the builder, the offline suite), interactive-exhibit 1.3 (every edit to
a room's hover text; Mode 5 on the phone), gallery-assembler 1.3 (the
catalog reads `objects_config.json`), provenance-discipline 2.13 (Rule 7,
display never shows more figures than declared), safe-file-editing 1.11
(every patch), agentic-pre-test 1.2 (every delivered file). The build
session confirms each loaded copy matches the manifest row before
starting.

---

## 1. What is being built, in one paragraph

The gallery stops reading orrery source code and starts reading the
orrery's export file. A generator pulls the export into the gallery at
a recorded orrery SHA. A second generator, the MIRROR, writes each
served number into `data/objects_config.json` from the export by name,
value, unit and figure count, for every link the export can serve, and
leaves the hand-typed value in place, named, for every link it cannot
serve yet. A checker fails whenever a served link's number in the
config differs from the export, so the config's numbers can no longer
be edited by hand without the next run saying so. The existing Store
drift check keeps running over the links the export cannot serve yet,
prints that count, and retires itself when the count reaches zero. The
page changes only where it names a unit and where it formats a served
number, which it now does to the declared figure count.

## 2. The two rulings this build stands on

**Order C (Tony, 2026-09-17, on the reply above).** The gallery half is
built now, without waiting for the store walk. The old check is not
switched off before the new one is on: Store drift narrows to the links
the export cannot serve and retires when that set is empty. This is
Tony's sequencing note of 2026-09-14 applied to the gallery: "Ruling
3's ORDER survives inside a slice; what changes is the denominator it
applies to."

**The join is a tool, not the page (Tony, 2026-09-17).** His words:
"my ruling was intended to insure that constants_new.py remained the
single source of truth. however, a tool reading and writing is not
creating a second store, it is just transmitting. so, i concur with
your option 2." The numbers stay in `objects_config.json` because that
is the file the page reads at boot; they are written there by the
mirror from the export, never by hand, and a hand edit fails the run.
Ruling 8 of 2026-09-11 is read in that light: its target was the hand
copy, and a generated, checked mirror is not one.

## 3. Facts the design rests on, measured at the pins

- The page reads `data/objects_config.json` directly at boot
  (`interactive.html` line 2123). It never reads
  `data/solar-system/feature_configs.json`; that file is a served copy
  the builder writes and the maintenance run probes. So the mirror
  targets `objects_config.json`, and the builder needs no change: its
  copy follows automatically.
- 70 links carry `orrery_constant`. Against the export at `8c2bd100`:
  17 resolve (16 distinct rows), 44 name a row with no unit line yet,
  4 name a row still declaring `dimensionless`, 5 point outside the
  store. The 48 unexported links cover 33 distinct rows, 16 Earth and
  17 beyond.
- The pointer sits in three shapes: beside the value
  (`{value, unit, source, orrery_constant}`, 38 links); on a FEATURE
  whose sub-entry such as `radius` holds `{value, unit}` (30 links);
  and on an orientation entry whose `ra`/`dec` or `pole` hold the
  values (2 links). The five outside-store links are the four
  `planet_poles` entries and the tide default, in the second and third
  shapes. The mirror handles the first two shapes and names any link
  whose row is absent, whatever its shape, as Store drift does today.
- Every one of the 17 served links already matches its export row in
  value, and in unit up to SPELLING: the config writes `R_earth`,
  `nPa`, `nT`, `per_nT` where the export's tokens are `r_earth`,
  `npa`, `nt`, `per_nt` (13 of the 17). The page renderers switch on
  the config spelling with exact case (`feature_renderers.js` lines
  229 to 257, `earth_geometry.js` 200 and 448). So the unit vocabulary
  is a PAGE contract, and this build changes it once, to the token
  spelling, page and config together.
- `check_store_drift` is a per-link loop (`gallery_maintenance_run.py`
  770 to 815); narrowing it is a filter on the list it walks.
- The offline maintenance run at `cb1762a7` is 7 suites; the live run
  is Served reachability and Store drift (report-only).
- Tony runs the cache builder and the maintenance run by hand; there is
  no scheduled job. Every generator here runs when he runs the
  maintenance run.

## 4. Deliverables, in build order

| # | File | Repo | Kind |
|---|---|---|---|
| 0 | `export_constants.py` | orrery | patch: the export gains `closed_slices` and `transitional` from `constants_rows.py`, so the gallery never types them |
| 1 | `tools/mirror_constants.py` | gallery | NEW: the mirror, with a `--report` mode that writes nothing |
| 2 | `tools/test_mirror_constants.py` | gallery | NEW: offline suite for the mirror and the join, on fixture configs |
| 3 | `gallery_maintenance_run.py` | gallery | patch: pull generator, mirror generator, Config mirror check, Pointer join, Export freshness, Store drift narrowed |
| 4 | `data/objects_config.json` | gallery | REWRITTEN BY THE MIRROR, once, in phase 2 (section 7); not edited by hand |
| 5 | `gallery/feature_renderers.js`, `gallery/earth_geometry.js` | gallery | patch: unit tokens `r_earth`, `r_sun`; served numbers formatted to `figures` |
| 6 | `documentation/smoke_hover_budget.js` and the Earth geometry suite | gallery | patch: pinned phrases follow the new formatting where a number's figure count changes what prints |

Piece 0 is one orrery commit and can land first, alone. Pieces 1 to 6
are one gallery session, one commit, after the phase-1 read (section 7).

## 5. Piece 0 -- the export carries the slice lists

`export_constants.py` adds two top-level fields, read from
`constants_rows.py`: `"closed_slices": []` and `"transitional":
["EARTH_MAGNETOPAUSE_STANDOFF_RADII", "EARTH_BOW_SHOCK_STANDOFF_RADII"]`.
`test_constants_export.py` gains one line: the fields equal the tuples
in `constants_rows.py`. The export's `SCHEMA` number moves. Reason: the
gallery's Pointer join must know which slices are closed to know when
a fallback is a FAIL, and the only honest source is the store's own
list. Nothing else in the orrery changes.

## 6. Pieces 1 to 3 -- the mirror, its suite, and the runner

**The pull generator** (`Constants export pull`, in GENERATORS after
Module atlas). Reads orrery HEAD through the commits API as
`check_store_drift` does today; fetches `data/constants_export.json`
at that SHA; writes it to the gallery's `data/constants_export.json`
and the SHA to `data/constants_export.sha`. Prints the SHA and whether
the bytes changed. On a fetch failure it prints N-A and leaves the
previous copy and SHA untouched, so a run with no network still works
against the last pull and says so.

**The mirror** (`tools/mirror_constants.py`; registered as the
generator `Config mirror`, after the pull). For every link in
`objects_config.json`:
- SERVED: the export has the row. The mirror writes `value` (the
  export's, already rounded to the row's figures), `unit` (the export's
  token), and `figures` (the export's count, or null) into the value
  slot the link governs. Any other field on the entry (`source`,
  `note`, `_declared`, presentation) is untouched.
- FALLBACK, not exported: the export names the row in `not_exported`.
  The mirror writes nothing and prints the link with the export's
  reason.
- FALLBACK, absent: the row is not in the store at all (the five). The
  mirror writes nothing and prints the link as NOT IN STORE.
- `--report` prints exactly what the write mode would change, value by
  value, and writes nothing. That is phase 1.

The mirror converts no units. If a served row's token differs from
what the config held, the mirror writes the token and the change
appears in the report; the page must already accept that token (piece
5) or the room breaks, which Mode 5 catches. A conversion table in the
mirror would be a second copy of the token table's factors; the
manifest declines it, and a link that needs a different unit than the
store's is a row to add to the store, not a conversion to hide here.

**The Config mirror check** (offline, gating). Re-reads the config and
the local export and confirms every SERVED link's `value`, `unit` and
`figures` equal the export's. Prints the count compared. FAILS on any
difference, naming the link: that is a hand edit, or a pull without a
mirror run. Also FAILS if `data/constants_export.sha` is missing or
does not name the pull the export came from.

**Pointer join** (offline, gating). Every link classified SERVED,
FALLBACK not-exported, or FALLBACK absent, with counts and names.
FAILS on a FALLBACK inside a closed slice, using the export's
`closed_slices`; outside one, named only. Prints "48 fallbacks" today
and the number the next Earth visit lowers it to. When it prints 0
fallbacks it also prints the line that Store drift may retire.

**Export freshness** (live, gating). Fetches the orrery's export at the
recorded SHA and confirms the gallery's copy is byte-identical,
printing the SHA compared against. Cannot go green without the SHA
resolving.

**Store drift, narrowed** (live, report-only, as today). Same code,
one filter: it examines only FALLBACK links, prints "examining N of 70
links; the other M are served from the export", and when N is 0 prints
"nothing left to examine; retire this check" and returns PASS. It
still parses `constants_new.py` at orrery HEAD for those N, which is
the transitional exception order C accepts, bounded and self-emptying.
The suffix reader, `SCALAR_UNITS`, `store_conversions` and `judge`
stay until that day and go in one patch then; `gallery_maintenance_run.py`
carries a comment naming that patch as owed.

**The suite** (`tools/test_mirror_constants.py`, in OFFLINE_CHECKERS).
Fixture configs and fixture exports, no network: a served link mirrors;
a fallback is left alone and named; an absent link is named; a hand-
edited served value fails the mirror check by name; a fallback inside
a closed slice fails the join; a missing `.sha` fails; the three
pointer shapes all resolve; `--report` writes nothing. Every verdict
asserted, so a green run proves the paths ran.

## 7. Two phases, and what Tony reads between them

**Phase 1, read.** With pieces 0 to 3 built on a throwaway copy, run
the mirror in `--report`. Expected at `cb1762a7` against `8c2bd100`:
0 value changes on the 17 served links (they already match, and no
served row declares `# Figures:` yet, so every export value is
unrounded); 13 unit-spelling changes (`R_earth` to `r_earth`, `nPa` to
`npa`, `nT` to `nt`, `per_nT` to `per_nt`); 17 `figures: null` fields
added; 48 fallbacks named; 5 absent named. Tony reads that list. A value
change appearing here is a finding to record, not a thing to explain
away.

**Phase 2, write.** Pieces 4 and 5 land together in one commit: the
mirror writes the config, and the page's unit switches move to the
token spelling. They cannot land apart, because the page breaks on the
new spelling without piece 5 and the old spelling fails the mirror
check without piece 4. Then piece 6, the offline run (expect 9 suites
green), the live run (Export freshness PASS, Pointer join 17 served /
48 fallback / 5 absent, Store drift examining 53), push, and Mode 5 on
both rooms on the phone: every number the same as before, every hover
that names a unit reading as before.

## 8. Piece 5 -- what the page does with `figures`

Rule 7 of provenance-discipline 2.13: a display may show fewer figures
than the row declares, never more. Where a renderer prints a served
number today with `toFixed(n)` or `toPrecision(n)`, it prints
`toPrecision(figures)` when `figures` is a number and keeps today's
format when it is null. Sites at `cb1762a7`: `feature_renderers.js`
lines 271, 689 to 707, 781; `earth_geometry.js` line 86. Where a hover
budget pin or the Earth geometry suite matches the printed digits, the
pin moves with the format. Today every served `figures` is null, so
phase 2 changes no printed number; the first change comes when the
Earth slice writes `# Figures:` on a served row, and Mode 5 is owed
then.

## 9. What is NOT in this manifest

- The store walk. After this build the Earth slice runs in the orrery
  (57 rows), then the 17 served rows beyond Earth if Tony rules
  served-first at the start of the Sun slice, then the rest. Each visit
  lowers Pointer join's fallback count; the gallery needs no further
  build until the count is 0.
- The two standoffs' reversion to expressions. They are SERVED at this
  build, Store drift stops examining them that day, and they revert in
  the Earth slice like any other Earth row. Both the orrery-half
  handoff and Opus's request said "last"; that is corrected here.
- Moving the five outside-store values into the store (Earth and Sun
  slices). They stay FALLBACK absent until then.
- Retiring Store drift's code. Owed on the day Pointer join prints 0
  fallbacks; one patch, named in the runner.
- L-334, the editor. It reads the config the mirror writes and shows
  SERVED numbers as locked, which this build makes true in fact.

## 10. What makes the whole build fail

Any FAIL from the mirror check, the join inside a closed slice, Export
freshness, or the suite. A phase-1 report showing a value change. A
Mode 5 in which any number or unit reads differently on the phone
after phase 2. A link that resolves in the export but whose page
renderer warns on the new unit spelling (the renderers warn to the
console by name; the build session reads the console).

## 11. Decisions here that are method, not rulings

Named so the build session can change them from the code without
coming back: the pull as a generator rather than a hand copy; the
mirror as a separate tool with `--report`; `figures` added beside
`value` and `unit` rather than in a sub-object; the page adopting the
token spelling rather than the mirror mapping it; Pointer join and the
mirror check as offline checkers; `.sha` as a sidecar file. None of
these change what Tony ruled.

## 12. What the build session records

On L-322: Tony's ruling of 2026-09-17 in his words (section 2), order
C, the two corrections to section 9 of the mechanism manifest, and the
standoffs' revised timing. On the mechanism manifest: a one-line note
at section 9 pointing here. In the orrery-half handoff, if it is still
the current handoff when this lands: a correction line at the top for
"last".
