# AS-BUILT -- Retire Option A (D8.5)

Built on `adc9b20d2e6533c25544d565430336f835e87a48`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

**Type:** BUILD. Two deliverables, uncommitted -- awaiting Tony.

**Closes:** D8.5 in `DESIGN_HANDOFF_provenance_scoring_and_pinning.md`.

**Reading order:** section 2 is the number and it is larger than
predicted. Section 4 is a second mechanism found during the audit you
asked for, and it is the more interesting finding.

---

## 1. Anchor

Prompt anchor and live HEAD both `adc9b20d`, matched at session start,
no drift. The bleed fix landed at `d0fe124`, and the patch scripts were
moved out of the repo root at `b813aa6` -- so the self-scan population
dropped from 123 files to 116, which is why the baseline reads 879 rather
than the 881 in the previous session's note. That floating item is
closed.

Base-file guards:

| file | MD5 |
|---|---|
| `provenance_scanner.py` | `a2bb551b8535b2e8eba40f916e8c9467` |
| `test_provenance_1d.py` | `5585323427e0fe2966d984c529d31581` |

---

## 2. Measured outcome

| | before | after | delta |
|---|---:|---:|---:|
| Tier 1 | 171 | **210** | **+39** |
| Tier 2 | 644 | 605 | -39 |
| Tier 3 | 62 | 62 | 0 |
| Tier 4 | 2 | 2 | 0 |
| Total | 879 | 879 | conserved |

39 findings enter Tier 1; none leave. Nothing appears or disappears --
these are the same findings, scored correctly for the first time.

**This is larger than I predicted, and the prediction was mine, so it is
worth saying where it went wrong.** Before building I measured Option A's
population and predicted +23. That was right for Option A alone but
missed how the second mechanism (section 4) interacts: I scored the
stale-credited findings in isolation and read them as staying in Tier 2,
without accounting for those that are also `C_PUBLIC` display strings,
which land at 16 once vulnerability moves to V4. Isolating each removal
afterward gives the clean decomposition:

| | Tier 1 | delta |
|---|---:|---:|
| baseline | 171 | |
| Option A removed alone | **194** | +23 |
| + stale credit removed | **210** | +16 |

+23 matches the pre-build measurement exactly. The +16 is the part I had
not modelled. Recorded rather than smoothed over, because a prediction
that misses by 70 percent is worth knowing about even when the direction
is right.

**The prompt's "18 display strings" is also low: the true figure is 26.**
That number predates 1d -- adding Fahrenheit/Celsius recognition created
new numeric claims in the climate modules, some of which then matched
pinned values and became newly eligible for Option A's credit. Of the 26,
two are suppressed and one stays in Tier 2 (its criticality is not
public), leaving 23 that move.

---

## 3. What was removed, and what was kept

**Removed: Option A.** `score_unit()` granted `V_SOURCED` to an uncited
display string whenever all of its numeric claims matched values pinned
from `constants_new.py`. Removed entirely, along with the
`pinned_values` parameter to `score_unit()`.

**Kept: `build_pinned_values()` and its call site.** The prompt says to
remove it if Option A was its only consumer. **It is not.**
`scan_shadow_constants()` takes `pinned_values` and uses it to detect
*derived* shadow constants -- expressions like `695700.0 / 149597870.7`
built from pinned literals. Removing it would have silently broken the
shadow-constant detector 1d added, and the breakage would not have shown
up in any tier count. I traced every reference before touching anything;
`test_pinned_values_still_feeds_the_shadow_detector` now pins that
dependency so a future session cannot repeat the near-miss.

What did change is that `pinned_values` now feeds a diagnostic only and
never reaches a score. That is the honest place for it, and it is exactly
the advisory-versus-exculpatory distinction the prompt's reasoning draws.

**Kept: block-citation inheritance (1c).** Worth stating explicitly since
it also grants `V_SOURCED` without a citation on the string itself. It is
not the same failure class: an inheriting string carries a citation a
person actually wrote, about the block the string sits in. That is real
provenance one level up, not provenance nobody wrote.
`test_block_inheritance_still_earns_v_sourced` guards it.

---

## 4. The audit found a second instance -- and it is worse

You asked whether Option A was the only place the scanner grants credit
without sourcing. It was not. There is one more, in the same function,
four lines below it:

```
elif stale:
    unit.vuln = V_SOURCED
    unit.vuln_reason = "No source, contains date-sensitive claims"
```

A unit with **no citation at all** was scored `V_SOURCED` whenever its
text matched a staleness pattern -- `as of 2024`, `Planned`, `Expected`,
`Still active`, `Currently operating`.

Read the reason string against the score it assigns. The scanner states
there is no source, and scores the finding as though there were one, in
the same breath.

And the logic runs backwards. A staleness marker is evidence a claim will
**expire** -- that it is *more* vulnerable over time, not less. If it
moved the score at all it should move it the other way.

**15 findings were credited this way**, in `shell_configs.py` (4),
`scenarios_western_heatwave_march_2026.py` (3), `solar_visualization_
shells.py` (3), `info_dictionary.py` (2), and one each in
`comet_visualization_shells.py`, `eris_visualization_shells.py` and
`idealized_orbits.py`.

I removed it in the same patch, since it is the same defect and leaving
it would have meant closing D8.5 with the failure class still live.
Staleness is still **detected** and still reported in the reason string
-- `"No source citation; date-sensitive (recalled)"` -- so no signal is
lost. It simply no longer substitutes for a citation.

**Why both existed.** Both predate the D3 ladder. When they were written,
`V_SOURCED` meant something looser than "a citation exists." After 1b
landed the four-rung ladder, `V_SOURCED` means "cited, never
independently cross-checked" -- and neither mechanism can honestly claim
the first half of that. They were not wrong when written; they were
outlived by a definition change and never revisited.

**The rest of the audit is clean.** I traced every path that can set
`unit.vuln`. Three remain, all requiring a citation a person wrote:
`has_citation()` on the unit's own context; the docstring-prose patterns
(prose citations in docstrings, which is a format allowance, not a
substitute); and 1c block inheritance. Suppression and accepted residuals
were checked separately -- they filter which findings are *reported* and
never touch a score, which is the right separation. No other mechanism
improves a vulnerability score without a real citation being present.

---

## 5. Tests

`test_provenance_1d.py` 20 -> 27. The seven additions are mostly
negatives, because that is where this failure class hides:

- numeric match alone earns no credit (Option A is gone)
- staleness alone earns no credit
- staleness is still detected and still in the reason (signal preserved)
- a real citation still earns `V_SOURCED` (removals did not overreach)
- block inheritance still earns `V_SOURCED` (1c not caught in the sweep)
- `score_unit()` no longer accepts `pinned_values` -- a signature-level
  guard, so the mechanism cannot quietly return
- `build_pinned_values()` still feeds the shadow detector

`test_citation_inheritance.py` 20/20 and `test_constants_provenance.py`
73/73, both unchanged. No existing test asserted Option A behaviour, so
nothing needed updating.

---

## 6. Verification performed

| check | result |
|---|---|
| SHA round trip | anchor == live HEAD, `adc9b20d` |
| Base-file MD5s | both match |
| Consumer trace before removal | `build_pinned_values` has a second consumer; kept |
| `py_compile`, deliverables and targets | pass |
| ASCII gate | no new non-ASCII |
| LF gate | no CRLF |
| Patch apply, clean clone | 13/13 anchors, one match each |
| Idempotency | refuses, nothing written, cause named per file |
| Per-mechanism isolation | Option A +23, stale +16, measured separately |
| `test_provenance_1d.py` | 27/27 |
| `test_citation_inheritance.py` | 20/20 |
| `test_constants_provenance.py` | 73/73 |

Agentic pre-test: devtool, no Tk surface, so the xvfb leg does not apply.
Runtime-equivalent leg was a live scan on the real repo plus all three
suites, on throwaway clones. Deliverables never edited by any test.

---

## 7. Rollup -- Tony-action

- **(do)** Run `patch_retire_option_a.py` via VS Code's Run button.
  Expect 13 `ok` lines across 2 files.
- **(do)** Run `test_provenance_1d.py` (27), `test_citation_inheritance.py`
  (20), `test_constants_provenance.py` (73).
- **(do)** Run `provenance_scanner.py .`. Expect Tier 1 **210**,
  Tier 2 605.
- **(do)** Paste the L-156 note; mark D8.5 CLOSED; run `ledger_index.py`.
- **(decide)** Tier 1 is now 210, up from 132 at the start of Phase 1d.
  Three separate increases now sit on it: piece 3's temperature claims
  (+61), Option A (+23), stale credit (+16). All are real, all were
  previously invisible. Worth deciding whether they get one tracking item
  or several -- the as-built for 1d/1e/1f already proposed L-175 for the
  temperature population.
- **(do)** Still carried over: correct or supersede
  `HANDOFF_phase1_1d_to_1f.md`; stamp the provenance-discipline v1.3 SHA
  placeholder; the three open decisions from the 1d/1e/1f as-built.
- **(do)** Push; record `pushed at <SHA>`.

---

## 8. A note on what Phase 1 has actually done

Tier 1 went 156 -> 132 across 1a-1c, then 132 -> 210 across 1d and this
build. Read as a single trend that looks like regression. It is not.

1a-1c fixed cases where the scanner was **scoring correctly-sourced
claims as unsourced** -- false positives, and the count came down. 1d
onward fixed the opposite: cases where the scanner was **scoring
unsourced claims as sourced**, whether by a blind spot (no temperature
recognition), by numeric coincidence (Option A), or by a marker that
means the opposite of what it was credited for (staleness). Those are
false negatives, and fixing them makes the count go up.

The number got worse because the instrument got honest. That is the
distinction to carry into the ledger, or a future session will read the
trend as Phase 1 having gone backwards.

---

*As-built written August 2026 with Anthropic's Claude Opus 5.*
