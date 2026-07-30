# Ledger + Master Plan Update -- 1a Landed, Ready for a Fresh Session

Tony Quintanilla, PE | Claude Sonnet 5 | July 29, 2026

**Built on:** orrery @ `2374e4c29a82ae65f8d6f12999d28c6859b8ba60`

**Why this exists:** you asked whether we have enough documentation to
review Opus's next response in a new session. Honest answer at the time:
not quite -- L-156 was a full day stale (still described Phase 1 as pure
future work) and the master plan had no record of 1a landing at all. This
closes that gap. After this paste, a fresh session reading only the
ledger and master plan will know: 1a is done, what it found, what got
ratified, and what's next.

---

## Section 1 -- Ledger (`LEDGER_CONSOLIDATED.md`)

Search for the `[L-156]` block's status line:

```
<!-- L:156 status:OPEN upd:2026-07-28 section:W.Active flag: rice:5/4/80/3 -->
```

Replace with (date only changes):

```
<!-- L:156 status:OPEN upd:2026-07-29 section:W.Active flag: rice:5/4/80/3 -->
```

Search for this exact Gap paragraph:

```
**Gap:** (1) fix the `CENTER_BODY_RADII` duplication per L-162 (separate
dedicated session); (2) resolve the five comprehensive-sweep items;
(3) build Phases 1-3 (Opus 5) against the decided ladder above -- the D3
gate is clear, nothing further blocks the build; (4) Phase 3 also retires
```

Replace just that opening (through "against the decided ladder above")
with:

```
**Gap:** (1) fix the `CENTER_BODY_RADII` duplication per L-162 (separate
dedicated session) -- **DONE, L-162 closed 2026-07-29;** (2) resolve the
five comprehensive-sweep items; (3) build Phases 1-3 (Opus 5) against the
decided ladder above, sub-stepped 1a-1f for clean attribution --
**1a DONE (2026-07-29, see Note below); 1b next.** 1c-1f remain: 1c
citation-window inheritance (Gap item 6), 1d citation-recognition regexes
+ D8 vocab + L-078(d) (Gap item 5, now also carrying the citation-form
gap, item 7 below), 1e banners/labels/Tier-2 sub-band, 1f the D9
structural check (see L-158); (4) Phase 3 also retires
```

Search for this exact sentence (end of Gap item 6):

```
genuinely distant citations, not the same phenomenon; they stay Tier-1 and
need the worksheet like any other genuinely uncited claim.
**Updated Tier prediction**
```

Insert a new Gap item 7 between them:

```
genuinely distant citations, not the same phenomenon; they stay Tier-1 and
need the worksheet like any other genuinely uncited claim.
(7) **Citation-form recognition gap (found 2026-07-29, during 1a).**
`has_citation`/`SOURCE_PATTERNS` doesn't recognize a bare author-year
parenthetical as a citation -- only `# Source:`/`# Verified:` keywords or
a URL. Real, verified instances exist (`TW_SURVIVABILITY_BIOLOGICAL`,
`TW_SURVIVABILITY_THEORETICAL`); measured at ~54 of 156 Tier-1 findings
but not independently confirmed at that precision -- re-measure when 1d
actually lands. Belongs in 1d alongside item (5)'s D4 regex work.
**Updated Tier prediction**
```

Finally, search for the end of the prediction table:

```
| Tier 4 | 19 | ~19 |
```

Append this whole block immediately after it:

```
**1a built and verified (2026-07-29).** Landed against HEAD `459fecd1`
(pre-Phase-A baseline), independently re-verified by me against the
actual pushed state at `bdaaa0c` after a first attempt silently failed to
execute (caught by a scanner re-run; see `safe-file-editing` skill v1.1
Field Notes for the process lesson). Result on the combined
Phase-A-plus-1a state: 781 findings, **Tier 1 = 156** (up from 145 -- see
below), Tier 2 = 181, Tier 3 = 430, Tier 4 = 14. `undetermined` count:
**5**, not the 62 (D2-as-written) or 40 (widened vocabulary alone) the
design discussion estimated -- role as a classification input (per
Tony's approval) closed the rest: `comet_visualization_info`,
`TW_SURVIVABILITY_BIOLOGICAL`, `TW_SURVIVABILITY_THEORETICAL`,
`ROTATION_AXIS_OMITTED`, `REFERENCE_YEAR`.

**Tier 1 growing is correct, not a regression.** The cluster's own
earlier prediction (Tier 1 stays flat through 1a, since all current
Tier-1 findings are strings) was wrong -- raising a constant's
criticality from low to MEASURED can promote a previously-buried,
uncited physical fact *into* Tier 1 for the first time. Verified
directly: `COMET_NUCLEUS_SIZES`, `planet_tilts`,
`BASELINE_ABSOLUTE_TEMP`, `B_STAR_TEMPERATURES` and others were sitting
in Tier 2/3 specifically because volume-based scoring undercounted them
-- D1 working as designed. The "Updated Tier prediction" table above is
superseded by this; a corrected end-of-Phase-1 prediction should wait
until 1d lands (see below), since 1d now looks like a bigger mover than
1b/1c.

**Role-veto amendment -- ratified (2026-07-29).** Breaks the earlier
approval that role would only fill in where a name match was absent,
never override one. Necessary: without it, `HUB_THRESHOLD` (devtool,
matches `threshold`), `MAX_DATA_AGE_DAYS` (cache, matches `_days`), and
`PERFRAME_INDICATOR_RADIUS_FACTOR` (gui, matches `radius`) all scored
MEASURED and landed uncited tool config in Tier 1 -- the exact failure
D1 exists to prevent, reintroduced through a generic stem. Verified
directly, both directions: all three now correctly score
"Internal (role ...)", while `BASELINE_ABSOLUTE_TEMP` and
`B_STAR_TEMPERATURES` (genuine physical facts, different roles) still
correctly score MEASURED. Costs nothing legitimate.

**A third recognition gap, found during 1a (2026-07-29) -- reshapes 1d
and Phase 4.** Distinct from the two already in Gap item (6): this one
is citation *form*, not distance or nesting. `has_citation`/
`SOURCE_PATTERNS` only recognizes `# Source:`/`# Verified:` keywords or
a URL -- a bare author-year parenthetical (`# empirical limit (Vecellio
et al.)`) matches nothing. Verified directly:
`TW_SURVIVABILITY_BIOLOGICAL` and `TW_SURVIVABILITY_THEORETICAL` are
genuinely, correctly cited (Vecellio et al. 2022; Sherwood & Huber 2010
-- real, well-known thresholds) and still score V4 RECALLED, "no source
citation." The scanner accusing a cited value of being uncited is
cite-to-clear's mirror image -- same integrity failure, opposite
direction. Measured at 54 of 156 Tier-1 findings (14/9/8 in
`shell_configs.py`/`paleoclimate_wet_bulb_full.py`/`idealized_orbits.py`)
-- **I could not independently reproduce this exact count** with a quick
approximation (got 19 with a looser pattern, different per-file split);
the underlying mechanism is solidly confirmed, the precise number isn't,
pending 1d's actual pattern-matching. This means 1d (where D4's
recognition regexes live) is likely Phase 1's single largest Tier-1
reducer, not a minor step, and undercuts the plan to start the Gemini
worksheet with the paleoclimate family -- several of those already name
their sources correctly.

**Sequencing decided: 1b next, not 1d pulled forward (2026-07-29).**
These are independent scoring passes recomputed fresh each run, not a
stateful migration -- final end-of-Phase-1 state is identical regardless
of 1b/1d order. Reordering would only invalidate the predictions above
for no gain, since Phase 4 doesn't start until after all of 1a-1f
regardless of their internal order.
```

Then run `ledger_index.py LEDGER_CONSOLIDATED.md` (normal run, not
`--check`) and confirm `--check` comes back clean afterward.

---

## Section 2 -- Master plan (`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`)

Search for this sentence, in the section 6 addendum:

```
now starts with the paleoclimate and sgr_a families instead of
`shell_configs.py`. Full detail: L-156 Gap item 6, L-078's note.
```

Append immediately after it:

```

**Build progress, 2026-07-29: 1a landed.** Phase 1 is sub-stepped 1a-1f
for clean attribution (each step gets its own audit diff before the next
starts). 1a (D1/D2 criticality classification) is built and verified
against live HEAD `bdaaa0c`: Tier 1 rose to 156 (up from 145) -- correct,
not a regression; raising criticality can promote a previously-buried
uncited fact into Tier 1 for the first time. Two things surfaced during
the build: a role-veto amendment (ratified -- prevents devtool/gui/cache
config from misfiring as physical facts) and a third recognition gap,
distinct from the citation-window issue above -- the scanner doesn't
recognize a bare author-year citation as a citation at all, only
`# Source:`-style keywords. This makes 1d (not yet built) look like
Phase 1's largest single Tier-1 reducer, and undercuts starting the
Gemini worksheet with paleoclimate -- several of those findings are
already correctly cited. 1b is next (not 1d pulled forward -- reordering
doesn't change the final Phase 1 outcome, only invalidates predictions
already on record for no gain). Full detail: L-156's Note, this same
date.
```

---

*Compiled July 2026 with Anthropic's Claude Sonnet 5.*
