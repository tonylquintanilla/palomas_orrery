# PRELIMINARY DESIGN HANDOFF -- Provenance Refactor Cluster, Part 2

Tony Quintanilla, PE | Claude Opus 5 | July 2026

**Built on** (re-verified live via `git ls-remote --symref` at the start of
this continuation; HEAD had not moved since Part 1):
- orrery (palomas_orrery) @ `8ca3de8f111ee5495edbb6d4fb50f590278ff673`
  at https://github.com/tonylquintanilla/palomas_orrery (branch main)
- gallery (tonyquintanilla.github.io) @ `f4ce24cb68d2aa5834c6abcf98a1d7e0d5a68e8a`
  at https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main)

**Type:** DESIGN SESSION (zero code)

**Companion:** Part 1 of this handoff (same session, L-162 gap resolution and
naming recommendation) -- **never filed as a separate document; content
below is captured in the ledger, not here.** Part 1's naming grounds,
ownership call, and alias-layer hazard live in ledger `[L-162]`'s Note;
the `comet_visualization_shells.py` scanner-visibility question lives in
`[L-158]`'s Note; the Planet 9 pinning exclusion lives in master plan
section 6. Every "Part 1 SX" reference below should be read against those
three locations, not a document that exists.
`OPUS5_PROMPT_provenance_refactor_completion_plan.md` (Sonnet 5, Jul 28)
and the chain it names.

**Covers:** asks 4 (phased build plan), 5 (L-078 lens), 6 (priority cleanup).
Part 1 covered asks 1-3 and held ask 7 pending Tony's decisions.

---

## 1. L-078 -- the answer, and it is not what the ledger says

### 1a. Two of its four Gap items are already closed, by other work

L-078's Gap reads: (a) triage the ~104 Tier-1 findings; (b) resolve the 4
COVERAGE GAP modules; (c) build the near-miss vocabulary detector; (d) F/C
bare-degree fix to `NUMERIC_CLAIM_RE`.

**(b) is DONE, closed as a side effect of L-163.** The live audit at HEAD has
**no role-coverage-gap section at all** -- only the domain one. L-163 Phase 3
tagged every module's docstring and the gate now classifies 114/115 with
`role_source == 'tag'`. Separately, one of the four named modules
(`smoke_rotation_axis.py`) was deleted outright in commit `17913ae`.

More than stale: **(b)'s instruction is now actively wrong.** It says "add to
ROLE_MAP or narrative_files." Since L-163 Phase 3, `ROLE_MAP` is a regenerated
mirror -- hand-adding an entry does nothing, because the next `module_atlas.py`
run overwrites it. A session following that Gap line literally would do work
that silently evaporates. **Tony-action (do):** rewrite L-078's Gap (b).

**(d) belongs in the scanner build, not in L-078's own lane.** It is a
`NUMERIC_CLAIM_RE` edit -- the same regex, same file, same before/after audit
diff discipline as D8's magnetosphere vocabulary addition (`nT`, `Gauss`).
Recommend folding it into Phase 1 rather than leaving it stranded in a parallel
track. **(decide)**

**(c) stays separate and stays open.** The near-miss vocabulary detector needs
corpus tuning and a measured false-positive rate before it goes live -- L-078's
own note says "not a guess-and-ship," and the design converged on the hook point
(`_extract_string_units`) without doing the tuning. That is its own session,
after this cluster.

### 1b. The triage backlog is 145, not 104 -- and the entire delta is one file

Live scan at HEAD, clean clone, real exceptions file loaded: **145 Tier-1 across
28 files.** L-078's last recorded figure was 104 across 26 modules (Jul 16,
Tony-local). Per-file:

| Tier 1 | File |
|-------:|------|
| **41** | `shell_configs.py` |
| 24 | `idealized_orbits.py` |
| 11 | `paleoclimate_wet_bulb_full.py` |
| 9 | `paleoclimate_human_origins_full.py` |
| 7 | `planet_visualization_utilities.py` |
| 7 | `paleoclimate_visualization_full.py` |
| 6 | `sgr_a_grand_tour.py` |
| 4 | `scenarios_western_heatwave_march_2026.py`, `exoplanet_coordinates.py`, `sgr_a_visualization_core.py` |
| 3 | `celestial_coordinates.py`, `sgr_a_visualization_precession.py`, `apsidal_markers.py`, `paleoclimate_visualization.py` |
| 2 | `coordinate_system_guide.py`, `paleoclimate_dual_scale.py` |
| 1 | 12 further files |

**104 + 41 = 145.** Every file other than `shell_configs.py` matches L-078's
July 4 figures within ±1. The growth the prompt attributed to "L-163's Phase 3b
coverage-widening" is real, and it is exactly one newly-in-scope file.

This is good news operationally: the backlog did not diffuse, it concentrated.
`shell_configs.py` is 28% of the entire Tier-1 population in one 2,762-line file.

### 1c. Those 41 findings are display strings, not geometry -- which settles the lane question

Every one of the 41 scores V=4 x C=4 = 16: "No source citation (recalled)" x
"Public-facing display string (hover/INFO)." **None are config geometry values.**

So the prompt's ask -- does L-078's remaining triage ride with L-161's Gemini
sweep or stay separate? -- answers itself from the data:

**Ride with it, merged per-file.** L-078(a) and L-161 are the same work on the
same kind of object through the same relay channel. They differ only in starting
vulnerability: L-078's are uncited (V4); L-161's are cited-but-never-cross-checked
(V2 today, V3 under the new ladder). Both need a blind worksheet carried to
Gemini and mechanically transcribed back. Running them as two separate
engagements over an overlapping file set is duplicated effort in the most
expensive part of the pipeline -- Tony's own relay time.

Recommended shape: **one worksheet per file**, covering that file's uncited and
its re-read claims together. Start with `shell_configs.py` (41 uncited, plus 6
Tier-2 and 43 Tier-3 in the same file) rather than L-161's proposed
`celestial_objects.py` -- it is the larger, denser, and entirely
never-worksheeted target. **(decide)**

### 1d. One contradiction worth knowing before that worksheet is drafted

`shell_configs.py`'s own module docstring says:

> "Source citations are preserved as comments above each body block. The
> provenance audit (April 2026) verified all values - do not modify."

The live scanner reports 41 uncited display strings in that file. The docstring
asserts a verification the scanner cannot see. Either the citations sit outside
the lookback window or in the wrong comment form, or the claim is overstated.
Worth resolving *before* the worksheet, because it changes whether this is
"cite what was never cited" or "repair citations that exist but don't register."
The code is the fact; the docstring is a claim.

---

## 2. The blind-check bar has a consequence nobody has priced

L-156 requires the V2 CROSS-CHECKED annotation to record **whether the check was
blind (no anchoring)**. L-161's Gap already applies this forward: check the April
2026 worksheets against the new bar before backfilling, and if they don't clear
it they need redoing, not re-tagging.

Nobody has applied it backwards, to `constants_new.py` itself. Its own docstring
describes the April 2026 process verbatim:

> "1. Claude sourced constants from IAU resolutions and NASA fact sheets
>  2. Google Gemini reviewed all values against authoritative sources"

That is cross-AI but **anchored by construction** -- Claude's values went in
first, Gemini reviewed them. It is precisely the shape the `ADDENDUM_v23`
near-miss identified and that L-156's blind field was added to prevent.

Consequences if the bar is applied consistently:

- `constants_new.py`'s constants do **not** backfill to V2. They land at V3
  SOURCED. With MEASURED criticality (C=5), that is 3 x 5 = **15 -- Tier 2**,
  not the Tier 3 resting place D5's Phase 2 exit criteria anticipate
  ("verified fundamentals resting in Tier 3").
- L-161's "~130 already Gemini-verified" almost certainly do not clear either.
- D6 stages the pinning engine's `constants_new` rows as active on the grounds
  that they are "already-verified (Gemini-checked April 2026)." That premise is
  the one under question.

I am not recommending an answer. The honest reading of the project's own rule
says the April pass was anchored; the honest counter-reading says it caught two
real Claude-introduced errors (Arrokoth, Parker) and demonstrably worked. The
cost of redoing it is a full blind re-verification of the foundational constants.

**Tony-action (decide):** does the April 2026 constants verification count as
V2 CROSS-CHECKED, or fall to V3 pending a blind redo? This gates Phase 2's
backfill step and D6's "already-verified" premise, so it needs answering before
Phase 2 starts, not during it.

---

## 3. Predicted post-build audit shape -- hand this to the build session

Verified from code: `score = vulnerability x criticality`; tiers are 16-20 /
10-15 / 5-9 / 1-4; `C_PUBLIC = 4`.

A cited display string today is V2 x C4 = 8, Tier 3. Under the merged ladder,
merely-cited becomes V3, so the same string is V3 x C4 = **12, Tier 2**.

L-161 counts ~330 such strings. So Phase 1 landing should move roughly 330
findings from Tier 3 into Tier 2 with **no change in the underlying facts**:

| | Live at HEAD | Predicted after Phase 1 |
|---|---:|---:|
| Tier 1 | 145 | ~145 (unchanged -- V4 and C4 both unchanged) |
| Tier 2 | 158 | ~490 |
| Tier 3 | 442 | ~110 |
| Tier 4 | 19 | ~19 |

**Put this in the build manifest.** The design already warns that "the
recalibration repopulates Tier 2 with genuinely-open items"; the number makes it
a checkable prediction rather than a caveat. A tripling of Tier 2 is the expected
result, not a regression -- and if the actual diff lands far from this, that is
itself the signal worth chasing.

Second-order: constants promoted to MEASURED (C=5) shift too, in the same
direction. Magnitude depends on the §2 decision.

---

## 4. Phased completion plan

Fable 5's Jul 26 six-step order is the right skeleton and I am not replacing it.
Steps 1 (ledger formalization) and 2 (D3 calibration) are both **closed** as of
Jul 27. What follows confirms, corrects, and sharpens the remainder against HEAD.

### Phase 0 -- record hygiene (now; independent; ~1 session, no build)

Cheap, unblocked, and every item is a correction to something a later session
would otherwise trust:

- Rewrite L-078 Gap (b) -- stale and actively misleading (§1a). **(do)**
- **Capture the Tier-1 exit-code flip as a new ledger item.** D7 says the flip
  should be "recorded as its own small ledger item so the flip doesn't float."
  I grepped: **no such item exists.** The instruction to capture it floated.
  Next free handle is **L-170** (highest in use is L-169). **(do)**
- Add `Role:` / `Domain:` docstring tags to
  `patch_ledger_index_retired_handles.py`, or archive it. It landed Jul 28 with
  no tags; `classify_role()` returns `undetermined` for it -- breaking L-163
  Phase 3b's "zero undetermined" close two days after it closed. It is also a
  one-shot patch script, the exact class L-163 Phase 1 archived. **(do)**
- Add `MODULE_DOMAIN_MAP` entries for `orrery_rendering.py` and
  `shell_configs.py` (both currently silent-defaulting to `orrery`). **(do)**
- **L-164** -- `dep_trace.py`'s 1,279 non-ASCII bytes across 8 divider lines.
  Zero dependency, five minutes, no reason to hold it for a phase. Land here.
  **(do)**
- Fix the L-157/L-161 swap in `HANDOFF_gallery_feature_layer_L154_resume.md` §3
  -- it credits the shell-config geometry cross-check to L-161; that is L-157.
  A resumed session would wait on the wrong item. **(do)**
- Carry the 15 -> 14 correction into ledger `[L-162]` and master plan §6. **(do)**
- Reinstall `gallery-assembler` SKILL.md from the repo copy (CRLF drift). **(do)**

### Phase A -- L-162, dedicated session (Sonnet-class)

Per Part 1 §2c, expanded beyond its current ledger scope:

1. 14 new plain-form named constants in `constants_new.py`, each carrying its
   existing citation.
2. `CENTER_BODY_RADII` rewired to reference all 17 names (Sun/Earth/Jupiter
   included -- L-162 owns that fix; see Part 1 §2c).
3. Resolve the `planet_visualization_utilities.py` alias layer -- recommended
   option (a): re-point the 12 existing aliases to import from `constants_new.py`,
   explicitly superseding the unrecorded "v3.20 Option B" decision.
4. Add `CONCEPT_ALIASES` entries for all 14 new names. **Hard requirement** --
   without them the duplicate detector is structurally blind to the new
   cross-file pairs (Part 1 §2b).
5. Pre-flight grep for f-string formatting of `CENTER_BODY_RADII[...]` -- the
   rewrite changes Sun and Jupiter from int to float.
6. `py_compile` + ASCII/LF gate + credit line + as-built anchored to the push SHA.

**Must land before Phase 3.** Independent of Phases 0 and 1.

### Phase 1 -- scanner change-set (Opus 5)

D1+D2 (MEASURED/RELATIONAL, `undetermined` sentinel per L-156's naming
conformance), D3 ladder, D4 recognition regexes, D8 unit vocabulary, D7 banners
and Tier-2 label fix, D9 two-factor structural check. **Plus L-078(d)'s F/C
bare-degree fix** to the same regex (§1a).

One coherent edit. Closes with the full before/after audit diff read line by
line, self-scan delta checked first (`PINNING_MAP` and any new module-level
table will nudge the scanner's own numbers). Check the actual diff against §3's
prediction.

### Phase 2 -- data-side cleanup

D5 has moved to Phase A, so this reduces to: D4's backfill of cross-check
annotations, and D8's exceptions-file deletions (spacecraft_encounters, the
comet entry).

**Blocked on the §2 decision.** You cannot backfill `# Cross-checked:`
annotations until you know whether the April 2026 pass qualifies.

### Phase 3 -- pinning engine (Opus 5)

D6's `run_pinning_checks`; `constants_new` pins active; shell/gallery rows staged
as "pending cross-check (L-157)"; D7's exit-code wiring (pinning live, Tier-1
wired-but-off, flip tracked as L-170); D10's five-site retirement of
`test_constants_provenance.py`.

**Recommend excluding Planet 9 from `PINNING_MAP` entirely** rather than pinning
a model estimate to four significant figures -- it is an L-159 `# Illustrative:`
case. Doing so lets the engine drop dict-path AST extraction completely, which
was §3a's stated goal (Part 1 §2d). **(decide)**

### Phase 4 -- Mode 7 relay, strictly sequential

**L-157 first** (shell-config ring/belt/atmosphere geometry), **then L-161
merged with L-078(a)** (display strings, per §1c). Both worksheets drafted
**blind -- no Claude-derived figures in the draft.** That requirement is not
boilerplate here: this project has already caught one anchored-prompt near-miss
(`ADDENDUM_v23`) and one case where Gemini's own cross-check output was wrong on
three counts. The blind draft is the mitigation for the first; Tony's integration
judgment is the only mitigation for the second.

Claude's role in Phase 4 is worksheet preparation and mechanical transcription
of what comes back -- not verification. Per provenance-discipline: **Claude
cannot be the verifier.**

### Ownership summary

| Phase | Owner |
|-------|-------|
| 0 (record hygiene), A (L-162) | Sonnet-class build session |
| 1, 2, 3 (scanner + pinning) | Opus 5 |
| 4 (L-157, then L-161+L-078a) | Gemini via Tony, sequential |
| L-164 | rides Phase 0 |

Unchanged from the decided position, flagged rather than relitigated: Tier-1
never gets an auto-exit gate; L-155's pinning failure is the cluster's only hard
exit-code gate. Both still look right to me.

---

## 5. Priority cleanup -- what becomes actionable when the cluster lands

RICE from the ledger's generated index at HEAD. Note this list includes **L-119
and L-166, which the prompt's table omitted** -- both sit inside this priority
range.

1. **L-154's resolver one-liner** (gallery, RICE 2.1 but effectively free).
   Verified live at gallery HEAD and reproduced this session:
   `resolver.py` line 133 is still `features = tuple(rec.get("features") or ())`,
   and `tuple()` on a dict yields only keys --
   `{'ring_system': {'main_ring': {'inner_radius_km': 122500}}}` collapses to
   `('ring_system',)`. Third independent confirmation. Land it first in whatever
   gallery session opens next, before anything else in the resume handoff.

2. **L-168 -- pre-flight gate, not an afterthought** (RICE 3.6). Verified live:
   `render_orbits.py` line 42 defines `K_GAUSS` as solar `sqrt(GM_sun)`, line 90
   computes `n = K_GAUSS / (a ** 1.5)` inside `propagate_marker`, with no
   parent-body branch -- and `assemble.py` line ~62 calls it unconditionally for
   every object on the live dispatch path. Dormant today only because Artifact 1
   (Earth) is heliocentric. The error scales as the square root of the Sun-to-parent
   GM ratio, which for any planetocentric moon is large enough to be immediately
   visible in the render. **Fix this before L-154's build reaches its first moon**,
   not after Mode 5 rejects it.

3. **L-119** (RICE 3.6, ties L-168) -- `event_link` hardcoded `None` in the
   builder; gates artifact 7. Absent from the prompt's table; worth re-reading
   before sequencing the artifact order.

4. **L-161 + L-078(a) merged sweep** (RICE 3.1) -- per §1c, starting with
   `shell_configs.py`.

5. **L-166** (RICE 2.4) -- F1b per-object trust enforcement and soft-edge trust
   UX. Also absent from the prompt's table, and adjacent to this cluster's
   subject matter: it is the consumption side of the trust blocks the provenance
   work produces. Worth checking for overlap before either is scheduled.

6. **L-154 design session** -- the three genuinely open questions (geometry-building
   approach, legend behavior, sequencing), taken as a live design conversation,
   not a checklist. The resume handoff's own advice is sound: start at question 1,
   because "port the orrery math literally" and "design fresh JS-native" pull
   question 3 in opposite directions. Then Artifact 2.

7. **L-159 enforcement check** -- stays open past the cluster by design.

**Already closed, contrary to some carried notes:** L-114 (section C) and L-120
(W.Done) are both `status:DONE upd:2026-07-27` at HEAD. Nothing to do.

---

## 6. Tony-action rollup (both parts of this handoff)

### (decide)

1. L-162 naming: **plain** (`MARS_RADIUS_KM`) -- three in-repo grounds (Part 1 §2a).
2. L-162 owns the Sun/Earth/Jupiter literal fix, same edit (Part 1 §2c). If yes,
   L-156's Gap line stands as written.
3. Alias layer: option (a), re-point `planet_visualization_utilities.py` to
   import from `constants_new.py`, explicitly superseding v3.20 Option B.
4. Planet 9: exclude from `PINNING_MAP` as an L-159 case rather than pinning a
   model estimate (Part 1 §2d, Phase 3).
5. **Does the April 2026 constants verification clear the blind-check bar?**
   V2 CROSS-CHECKED, or V3 pending a blind redo (§2). Gates Phase 2.
6. Fold L-078(d)'s F/C bare-degree fix into Phase 1 (§1a).
7. Merge L-078(a) into L-161's relay, one worksheet per file, starting with
   `shell_configs.py` (§1c).

### (do)

8. Rewrite L-078 Gap (b) -- stale and actively misleading.
9. Capture the Tier-1 exit-code flip as **L-170** -- D7 asked for it; it floated.
10. Tag or archive `patch_ledger_index_retired_handles.py` (L-163 regression).
11. `MODULE_DOMAIN_MAP` entries for `orrery_rendering.py`, `shell_configs.py`.
12. Land L-164 (`dep_trace.py`, 1,279 non-ASCII bytes) in Phase 0.
13. Fix the L-157/L-161 swap in `HANDOFF_gallery_feature_layer_L154_resume.md` §3.
14. Carry 15 -> 14 into ledger `[L-162]` and master plan §6.
15. Reinstall `gallery-assembler` SKILL.md from the repo copy (CRLF drift).
16. Correct the master-plan path (`documentation/` prefix) in any reused prompt.
17. Resolve the `shell_configs.py` docstring-vs-scanner contradiction before its
    worksheet is drafted (§1d).
18. Confirm whether `comet_visualization_shells.py` lines 492/602 are
    scanner-visible (Part 1 §4).

---

## 7. Still not read

For honesty about this handoff's own coverage, unchanged from Part 1 except
where noted: `LEDGER_SESSION_provenance_cluster_formalization.md`,
`D3_calibration_worksheet_vulnerability_ladder.md`,
`PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md`,
`ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md`, and `AS_BUILT_L163_phase1-4`.
`REVIEW_provenance_refactor_cluster_scoping.md` and
`HANDOFF_gallery_feature_layer_L154_resume.md` are now read; design handoff
D6-D10 and §3 are now read. Nothing in the unread set is load-bearing for the
plan above, but the D3 calibration worksheet would be worth a builder's eye
before Phase 1.

Ledger `**Note:**` blocks (ask 7) are still held. Decisions 1-5 change their
wording materially; say the word and I will produce them paste-ready in one pass.

---

*Handoff written July 2026 with Anthropic's Claude Opus 5.*
