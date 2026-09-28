# Handoff -- L-322 Stage D: exact rows print by their counts (orrery done); the gallery half and the Sun room are next

**Built on orrery `0e3d05fd498f1ae8b49ec5dba58503f6bf448576` at
https://github.com/tonylquintanilla/palomas_orrery; pushed at
`a7868eee04575abeeae303a6ca6a700890e835f1`. Gallery read at
`2df02f3baead894ff40922bcadef9cb84c49fa07` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; this
session pushed nothing to the gallery.** Both HEADs read live with
`git ls-remote` on 2026-09-28.

**Type: BUILD.** The next session builds one gallery patch and runs no
design round first, unless it finds something below to be wrong.

**Supersedes** `HANDOFF_L322_D_gallery_patch3_done_20260926.md` for what
remains; that handoff stays the record of gallery patch 3 and D13, and
its section 4 ledger rows are still owed (section 5 below). **Companion
record:** `documentation/RUN_RECORD_L322_D13_20260926.md`. Despite its
name it now holds Tony's runs of D14, D15, D16 and D17 as well; the
next session starts its own run record.

**Rules this work ran under:** protocol v3.69 at the start, v3.71 at
the end. provenance-discipline: this session LOADED 2.19 and shipped
2.20 (D14) and then 2.21 (D16, Claude Fable 5.1's recommendation). A
reinstall cannot be verified from inside the session that makes it, so
**the next session confirms its loaded copy reads 2.21 before any
provenance, constants_new.py or print-count work.** 2.21 is the version
the gallery patch below is built to. Other skills unchanged:
interactive-exhibit 1.4, gallery-cache-builder 1.6, gallery-assembler
1.3, safe-file-editing 1.11, agentic-pre-test 1.2,
ledger-and-session-records 1.11. This session shipped two versions of
one skill, which the ledger skill's ONE SESSION, ONE BUMP rule says not
to do; the v3.71 protocol entry says so openly.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds the gallery half.

---

## 1. What was built, and how each piece was verified

All four are orrery patches. Tony ran each from the orrery root,
followed it with the orrery maintenance run, and pushed.

- **D14, provenance-discipline 2.19 -> 2.20.** Rule 2 now says where a
  trailing ".0" comes from: Python, by three routes (a decimal point is
  typed to make a float; division always returns a float; a float
  printed with no format always shows ".0"). None of them is a
  statement about significant figures, so a count is never read from a
  literal, a printed value or the export. Checked by running Python 3
  and Node. Rule 7's exact row was brought into line with D15's code.
- **D15, manifest section 6's orrery half.** The seven exact rows a
  display prints state a print count on their `# Figures:` line,
  directly after `exact --`: the LEO edge 4, the LEO floor 3, the outer
  belt peak 2, the solar wind pressure 1, Bz 1, the two cut angles 3.
  `constants_rows.py` reads the count and refuses one larger than the
  number's digits, one too small to write it in full, and anything but
  1 on a zero. The export serves it as `"prints"` (schema 5). The
  orrery's eight printing lines print through `exact_text()`; their
  text did not change, checked byte for byte through the live builders.
  `exact_rows_report.py --check` is a new pass/fail checker in the
  maintenance run, "Exact rows by the count", with a dashboard button.
  In passing: `test_constants_export.py` now compares `uncertainty`,
  which it had not since schema 4, and the maintenance run's own
  docstring count of gating checkers was corrected.
- **D16, provenance-discipline 2.20 -> 2.21, and protocol v3.71.** A
  sum or difference scaled by an exact row keeps its decimal place,
  carried through the scaling, not its figure count. The case: the top
  of the chromosphere, 695,700 km (exact) + about 2,000 km (one figure)
  is good to thousands; divided by the exact solar radius it is good to
  thousandths, 1.003 solar radii. Counted by fewest figures it would
  have been 1.00, and the export would then have drawn the chromosphere
  on the photosphere. Wikipedia's Significant figures page, the skill's
  reference, names this as its unit-conversion exception (8 inches to
  "20. cm"); checked by fetching the page. Fable's eight edits went in
  unchanged plus one sentence: a single measured value scaled by an
  exact row stays under fewest figures for now.
- **D17, the chromosphere rows and the checker.** `SUN_RADIUS_KM` is
  exact, "prints 4" (the IAU 2015 nominal radius, 6.957 x 10^5 km).
  `CHROMOSPHERE_PHYSICAL_KM` has one figure. `CHROMOSPHERE_TOP_KM` is
  new, 698,000 km at three figures. `CHROMOSPHERE_PHYSICAL_RADII` is
  the sum over the radius and counts to 4 figures, 1.003.
  `test_derived_figures.py` applies the scaling rule and prints the
  place it kept; five new built-in rows test it, two of them refused
  on purpose, and every existing row's verdict was unchanged. The
  orrery's chromosphere hover reads "1.003 solar radii" (was 1.002875)
  and "roughly 0.3%" of the radius (was 0.29%). `exact_rows_report.py`
  lists the gallery's three `SUN_RADIUS_KM` pointers as DRAWN: the Sun
  room uses the row only to turn solar radii into kilometres.

**State after D17, from Tony's run:** 19 of 20 checkers pass. The one
failure is "Exact rows by the count", and it is correct: it names the
Earth room's eleven gallery prints, which the gallery does not yet serve
a count for. It clears when the gallery patch below lands and the orrery
maintenance run is run again.

## 2. Rulings this session (Tony, 2026-09-27 and 2026-09-28)

- Each exact row prints the digits it was defined or chosen with; the
  counts in section 1 follow. Decided as the skill's rule, not case by
  case.
- The trailing ".0" is Python's: checked, and written into the skill.
- The checker also refuses a count too small to write the number in
  full, and a declared construction prints the digits of the value its
  rule gives (4.5 prints two). Approved on the condition that the code,
  the provenance rules and the significant-figure rules agree; they
  were compared line by line before D15 and D16 shipped.
- The crust's hover reads "Radius: 1 Earth radius", not "1.0000 Earth
  radii". One Earth radius is the equatorial radius of IERS Conventions
  (2010), a definition, so the crust's 1 is exact.
- The chromosphere prints 1.003 solar radii (Fable's recommendation,
  2.21). The kilometre line gets its own row, 698,000 km, and the
  Sun's radius is exact and prints 4.

## 3. What remains: ONE gallery patch, rebuilt

Gallery patch 4 was built and tested in this session
(`patch_L322_D_p4_gallery_print_counts_20260927.py`) but **must not be
run as it is.** It was built before D17. Simulated on the gallery at
`2df02f3b` with D17's export: the mirror step writes four Sun links as
well as Earth's (the three `sun_radius` nodes become exact with prints
4, and the chromosphere radius becomes 1.003 with figures 4), so the
patch's "mirror changes nothing" promise is false; and the display
smoke check fails, because the chromosphere's hover changes against the
recorded fixture. So the next session builds **one** gallery patch that
carries patch 4's work and the Sun room's, and records one new fixture.

**Patch 4's work, to carry forward unchanged** (Tony can give the
session the file; everything in it was tested on 2026-09-27):

- `tools/mirror_constants.py` copies `"prints"`; the definition case
  (the crust's 1 by definition) writes `"prints": 1`.
  `tools/test_mirror_constants.py` gains case 19.
- `gallery/feature_renderers.js`: `servedFigures()` returns an exact
  node's `prints`; an exact ROW (a node with its own `orrery_constant`)
  served with no count is printed in full and reported as a warning,
  never given a width. The LEO altitude and the belts print by the
  count. The Earth "Radius:" line is singular at exactly 1.
- `documentation/smoke_display_figures.js`: the LEO rule reads the
  count, the magnetopause and bow shock are graded on their new lines,
  and two self-test ways are added (the page reads a served count; the
  page reports an exact row served without one).
- Visible changes in the Earth room: "Bz 0 nT, dynamic pressure 2 nPa",
  "at dynamic pressure 2 nPa", "Radius: 1 Earth radius". Nothing else.

**The Sun room's work, new:**

- The Sun's "Radius:" line (in `feature_renderers.js`, the `r_sun`
  branch that prints `cfg.radius.value` raw) prints by the served count
  where one is served, and exactly as today where none is. Most Sun
  shells serve no count, and `fmtServed`'s fallback would give them a
  fixed width such as "19.7000"; that must not happen. Singular at
  exactly 1: "1 solar radius".
- The chromosphere's kilometre line prints from `CHROMOSPHERE_TOP_KM`,
  698,000 km, three figures, not from 1.003 x 695,700 (which would
  print "697,800 km" at four figures). This needs a served pointer on
  the chromosphere entry, which only the mirror or `store_writer` may
  write (interactive-exhibit skill); the session decides the node's
  name. Check the AU in brackets: computed from the full digits it is
  0.00466; computed from the rounded served 698,000 it would be
  0.00467. Rule 4 says the first.
- Expected visible changes in the Sun room: the chromosphere reads
  "Radius: 1.003 solar radii" and "= 698,000 km"; the photosphere
  reads "Radius: 1 solar radius". The session lists every changed
  hover, today and after, before building (manifest section 6, step 5),
  and Tony checks them on his phone.

**Order of Tony's runs after the patch:** cache build by hand, the
gallery maintenance run (the mirror step should then change nothing),
commit and push, the phone check, then the orrery maintenance run, where
"Exact rows by the count" should pass.

**Finished means** the orrery's "Exact rows by the count" passes with
the gallery beside it, and the gallery's maintenance run passes 17 of 17
with the new fixture.

## 4. Things noticed, for the ledger (one row per class)

New this session:

- **Sun room radii printed with no count.** The `r_sun` hover branch
  prints served values raw; the chromosphere and the photosphere are
  fixed by the patch above, and the others (such as the Alfven surface,
  19.7) stay raw until their rows carry counts.
- **The orrery's solar hover prints AU at fixed widths** (`:.5f` on
  `SOLAR_RADIUS_AU`, which has no `# Figures:` line yet). Part of L-352's
  class; the chromosphere's AU happens to match its count.
- **2.21 leaves a single measured value scaled by an exact row under
  fewest figures.** If a future row needs the reference page's full
  unit-conversion exception, the rule is widened then, deliberately.
- **ONE SESSION, ONE BUMP was bent**: this session shipped 2.20 and
  landed 2.21. Recorded in the v3.71 entry; noted so it is not repeated
  by habit.

Still owed from the previous handoff, section 4, none of it filed yet
(checked against `LEDGER_CONSOLIDATED.md` at `a7868eee`): the four new
rows (Jupiter's unsourced belt thickness; the recorded Earth scene
overlaid piece by piece; the magnetotail hover at the 17-line ceiling;
no Wikipedia article for the magnetotail), and the closures of L-311
(DONE), L-325 (close, superseded by L-322) and L-342 (close). Its
carried list stands as written there.

The highest handle in the ledger at `a7868eee` is L-367 (the other
chat's L-363 to L-367 were filed), so the next free handle is L-368.
Re-read the ledger index before assigning one.

## 5. For the next session

- Confirm the loaded provenance-discipline reads **2.21**, and the
  other skills match the manifest.
- File the ledger rows of section 4 and of the previous handoff, and
  the three closures, in one ledger patch, before or beside the gallery
  patch. Tony-actions are "do" steps the patch prints, not hand edits.
- Build the one gallery patch of section 3 on the gallery's HEAD at the
  time; its files may have moved.

## 6. Tony-actions

- (do) File this handoff in the orrery's `documentation/`.
- (do) Delete the second copy of
  `patch_L322_D_17_chromosphere_rows_20260928.py` in the orrery root;
  the copy in `documentation/` is the record.
- (do) Keep `patch_L322_D_p4_gallery_print_counts_20260927.py` from this
  chat's downloads, unrun, and give it to the next session as the
  source of patch 4's work. Do not run it.
- (decide) The Sun's Auto view, carried from the previous two handoffs.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.
