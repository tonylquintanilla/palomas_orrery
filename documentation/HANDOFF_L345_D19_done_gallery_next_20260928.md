# Handoff -- L-345: conversions are computed (orrery D19 done); the gallery patch, then D20, are next

**Built on orrery `a7868eee04575abeeae303a6ca6a700890e835f1` at
https://github.com/tonylquintanilla/palomas_orrery; pushed at
`807e9dd535211b2bdb91263b49988e1494c308a8`. Gallery read at
`2df02f3baead894ff40922bcadef9cb84c49fa07` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; this
session pushed nothing to the gallery.** Both HEADs read live with
`git ls-remote` on 2026-09-28. The pushed D19 files were compared byte
for byte with the tree this session tested, and they are identical.

**Type: BUILD.** The next session builds one gallery patch, then orrery
patch D20. No design round is needed unless something below is found
to be wrong.

**Supersedes** `HANDOFF_L322_D_print_counts_orrery_done_20260928.md` for
what remains. That file stays the record of D14 to D17, and Tony's runs
of D18 and D19 are appended to it. **Companion records**, both in
`documentation/`: `DESIGN_L345_conversions_computed_20260928.md` and
`RULING_L345_conversion_count_rule_20260928.md`. The ruling replaces
the design's section 4 and withdraws its section 7 third bullet.

**Rules this work ran under:** protocol v3.71 at the start, v3.72 at
the end. This session LOADED provenance-discipline 2.21 and
interactive-exhibit 1.4, and shipped 2.22 and 1.5 at `807e9dd5`. Tony
reinstalled both. A reinstall cannot be verified from inside the
session that makes it, so **the next session confirms its loaded copies
read provenance-discipline 2.22 and interactive-exhibit 1.5 before any
provenance, constants_new.py or exhibit work.** That is also why this
session stopped here: the rest is exhibit and store work, and this
session's loaded rules are the old ones. Other skills unchanged:
gallery-cache-builder 1.6, gallery-assembler 1.3, safe-file-editing
1.11, agentic-pre-test 1.2, ledger-and-session-records 1.11.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds next.

---

## 1. What was built, and how each piece was verified

- **D18, the ledger catch-up (orrery `714293a9`).** Five Stage D
  handoffs and the Stage D manifest had each listed items "for the
  ledger" and none had been filed. D18 filed them: new items L-368 to
  L-385, a line added to L-243, L-345, L-350, L-351, L-352 and L-360,
  a Stage D note on L-322, and L-311, L-325 and L-342 closed. Tested on
  a copy; `ledger_index.py` then reported no consistency problems.
- **D19, the mechanism (orrery `807e9dd5`).**
  - `constants_rows.conversions()` works out a row's value in every
    unit of its dimension -- for a length, km, AU, Earth radii and
    solar radii -- from the row's full digits, rounded once, each count
    from the source row alone.
  - `export_constants.py` serves that as `"in"` on each exported row,
    schema 6. 53 of 89 exported rows carry it.
  - `test_constants_export.py` compares `"in"` like every other field.
    Its new check 6 re-computes all 212 served conversions with its own
    arithmetic and holds eight worked cases by value. It was shown
    failing three ways before it was trusted: the rule changed, a
    served value changed, and `"in"` removed from a row.
  - provenance-discipline 2.22, interactive-exhibit 1.5 and protocol
    v3.72 landed in the same commit. The ledger records L-345's ruling;
    L-384 closed; L-351's interactive-exhibit line is marked partly
    landed; new items L-386 and L-387.
  - Tony's maintenance run: 19 of 20 checkers pass. "Constants export
    check" ends "212 conversions re-computed, 8 of 8 worked cases
    hold." The one failure is "Exact rows by the count", naming the
    Earth room's eleven lines, as expected until the gallery patch.
- **The first D19 run wrote nothing.** Its script refused when the two
  L-345 documents were already filed in `documentation/`, and a refused
  patch writes nothing. The revised script accepts an already-filed
  document when it is identical and still refuses one that differs.
  The commit `3e9e9d13` holds only the documents; `807e9dd5` holds the
  patch.

## 2. Rulings and decisions this session

- **Tony, 2026-09-28, on L-345:** "follow the single source of truth
  principle. use the single best source for the store with provenance.
  compute all conversions instead of duplicating. we should build this
  architecture now. add to the skill if clarification is needed."
- **Tony, on the count rule, after Claude Fable 5.1's review:**
  "confirmed as recommended", as the skill's method.
- **Three places Claude departed from Fable's text**, each recorded
  where it lives:
  - The rule's wording: "the power of ten nearest that scaled
    uncertainty" was replaced by the Report test's comparison with half
    a unit in each place, which is what Fable's table computes. Read
    literally, the bow shock's AU would have printed 0.000576. Recorded
    in the skill and in v3.72.
  - Fable's LEO finding was not taken. The equatorial radius row states
    8 figures and an uncertainty of 0.0001 km; Tony's ruling of
    2026-09-27 made the UNIT exact, not the kilometre value. Recorded
    on L-345.
  - A converted value never shows fewer than one figure. Without it the
    geocorona, 100 Earth radii at one figure, would round to nothing in
    AU; with it, 0.004 AU. Recorded in the skill.
- **Tony, 2026-09-28, on the master plan's two companions (L-333,
  L-362):** "i think we should integrate these reports. the summary as
  an executive summary. the body should keep its critical path
  section." So the plan becomes ONE document: an executive summary at
  the top, taking the place of `MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md`,
  and the critical path kept in the body as section 5a, taking the
  place of `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`. Built at D20 (section
  4b).

## 3. Read-back, as the ruling asks

- **Where the rule lives:** provenance-discipline 2.22, Rule 3, the
  paragraph beginning "A value in another unit is computed, never
  stored, and its count comes from its source row alone". It follows
  2.21's place paragraph and replaces that paragraph's last two
  sentences. Rule 8's paragraph "The checker also applies Rule 3's
  scaling paragraph" is widened to match.
- **Hovers that print a bow shock kilometre or AU line:** one, the
  gallery Earth room's Bow Shock hover, "That is about 86,200 km
  (0.000576 AU)". It becomes "86,000 km (0.00058 AU)". The orrery's bow
  shock hovers print Earth radii only (`shell_configs.py` line 2319,
  `earth_visualization_shells.py` lines 969 and 1236), so they do not
  move.

## 4. What remains, in this order

**The gallery patch goes first, then D20.** The design put D20 first.
The order is reversed because D20 stops exporting the 13 conversion
rows, and 11 gallery pointers still name them: until the gallery moves
those pointers, its maintenance run would fail on rows the export no
longer serves. The gallery patch needs only D19, which is pushed.

### 4a. The gallery patch

- **Patch 4's work, unchanged.** The source is
  `patch_L322_D_p4_gallery_print_counts_20260927.py` (Tony has it; do
  not run it). Its five target files were byte-identical at gallery
  `2df02f3b`, checked this session. Its fixture must be re-recorded.
- **The mirror copies `"in"`** (`tools/mirror_constants.py`), as it
  copies `"prints"`, with a case in `tools/test_mirror_constants.py`.
  The config is hand-formatted and read as a diff, so decide the
  layout of `"in"` on the node before writing it.
- **The 11 pointers move** from conversion names to the rows they come
  from. Measured at gallery `2df02f3b`: `EARTH_GEOSTATIONARY_RADII`,
  `EARTH_LEO_INNER_RADII`, `EARTH_LEO_OUTER_RADII`,
  `EARTH_STRATOPAUSE_RADII`, `EARTH_THERMOPAUSE_RADII`,
  `EARTH_HILL_SPHERE_RADII`, `EARTH_MAGNETOPAUSE_STANDOFF_KM`,
  `EARTH_MAGNETOPAUSE_STANDOFF_AU`, `EARTH_BOW_SHOCK_STANDOFF_KM`,
  `EARTH_BOW_SHOCK_STANDOFF_AU`, and `CHROMOSPHERE_PHYSICAL_RADII`.
  The stratopause and thermopause have no kilometre radius row yet
  (see 4b): decide whether their pointers wait for D20 or D20 comes
  first for those two. Neither the mirror nor `store_writer` writes
  pointers, so the move is the patch's own edit.
- **The page prints units from `"in"`** (interactive-exhibit 1.5):
  `kmAndAu()` and `shellKmLines()`, and the two standoff hovers, which
  read the served `standoff_km` and `standoff_au` nodes today.
- **The Sun's "Radius:" line** prints by the served count where one is
  served and exactly as today where none is, singular at exactly 1.
  Most Sun shells serve no count; `fmtServed`'s fallback would give
  them a fixed width such as "19.7000", which must not happen.
- **Expected visible changes**, to be listed today-and-after before
  building and checked on Tony's phone:
  - Earth, magnetopause: "Bz 0 nT, dynamic pressure 2 nPa".
  - Earth, bow shock: "at dynamic pressure 2 nPa"; "86,000 km
    (0.00058 AU)".
  - Earth, crust: "Radius: 1 Earth radius".
  - Sun, chromosphere: "Radius: 1.003 solar radii" and "= 698,000 km
    (0.00466 AU)".
  - Sun, photosphere: "Radius: 1 solar radius".
  - Anything else that moves is a finding, not a change, until
    explained.
- **Tony's runs after it:** cache build by hand, the gallery maintenance
  run, commit and push, the phone check, then the orrery maintenance
  run, where "Exact rows by the count" should pass.

### 4b. Orrery patch D20: the rows

- The 13 conversion rows stop being rows: each keeps its name and its
  `# Unit:` line (so the dimension checker still reads its arithmetic),
  loses its `# Figures:` and `# Status:` lines, and gains a marker the
  reader recognizes, naming the row it comes from. The export lists it
  under not_exported with that reason, and the closed-slice gate skips
  it. The 13: the four interior `_RADII` rows,
  `EARTH_GEOSTATIONARY_RADII`, `EARTH_LEO_INNER_RADII`,
  `EARTH_LEO_OUTER_RADII`, `EARTH_HILL_SPHERE_RADII`, the two standoffs'
  `_KM` and `_AU`, and `CHROMOSPHERE_PHYSICAL_RADII`, re-written as
  `CHROMOSPHERE_TOP_KM / SUN_RADIUS_KM`.
- The stratopause and thermopause each gain a kilometre radius row,
  Earth's radius plus the altitude, and their `_RADII` names become
  conversions of it.
- `test_derived_figures.py` gains the Rule 8 widening, and with it the
  check that can fail: a row that is one row scaled only by exact rows,
  and is not marked as a conversion, fails, by name. Show it failing
  before trusting it.
- **One orrery display prints a conversion name by its count:**
  `CHROMOSPHERE_PHYSICAL_RADII`, at 1.003, in the Sun's chromosphere
  hover. It needs a count after the row loses its `# Figures:` line;
  the computed count is 4, the same. No other conversion name is
  printed through `figures_of()` or `_declared()` (measured at
  `807e9dd5`). Hold every orrery hover byte for byte, with the
  pre-delivery test (agentic-pre-test), because this is display code.
- **The master plan restamps to v34 in this patch.** The ledger skill's
  rule is once per design build, and L-345 is one; D20 is where it
  ends and Stage D closes, so v34 records both. Per Tony's ruling in
  section 2:
  - the plan gains an executive summary at the top, written from the
    current state, not copied from the August companion;
  - section 5a stays the critical path, brought current;
  - both companion files get a short retirement line saying the plan
    now carries them, and are otherwise left as dated records (git
    holds their history either way);
  - L-333 and L-362, which record the same problem, both close, each
    pointing at v34;
  - ledger-and-session-records gains the change to The Document Stack:
    the plan is one document at two zooms -- the executive summary and
    the body, with the critical path inside the body -- and the summary
    is rewritten with every restamp. That is a skill bump, 1.11 ->
    1.12, with its protocol version-history entry, in the same commit
    (the binding rule). Check first that no other session has bumped
    it since `807e9dd5`.

## 5. For the ledger, one row per class

Nothing new beyond what D19 filed (L-386, L-387). When D20 lands, L-345
closes if the gallery patch has landed; otherwise it waits for it.
L-333 and L-362 close at D20 with the plan's v34 (section 4b).

## 6. For the next session

- Confirm the loaded provenance-discipline reads **2.22** and
  interactive-exhibit **1.5**, and the other skills match the manifest.
- Re-anchor both repositories; gallery files may have moved.
- Build section 4a, then 4b.

## 7. Tony-actions

- (do) File this handoff in the orrery's `documentation/`.
- (do) Give the next session
  `patch_L322_D_p4_gallery_print_counts_20260927.py` again, unrun, as
  the source of patch 4's work.
- (decide) The Sun's Auto view, now on the ledger as L-385.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.
