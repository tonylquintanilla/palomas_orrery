# As-Built — Batch 1 Cross-Check Patch Scripts

**Built on `ee29e6c691cad2995992396e692fae1d0d5cadc0`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Built:** August 3, 2026 by Claude Opus 5 (build) · Tony Quintanilla, integrator
**Implements:** L-156 Phase 2 Batch 1 cross-check decisions, per
`PATCH_SPEC_batch1_cross_check.md` + Option A scope decision
**Pushed at:** _(fill in after push)_

---

## 1. Anchor reconciliation

The patch spec was anchored to `2ccf6839c4278f01db00fbe2101440ab267a90c2`.
Live HEAD at session start was `ee29e6c691cad2995992396e692fae1d0d5cadc0`.

Traced rather than assumed. Four commits ahead of the spec anchor:

| SHA | Message |
|-----|---------|
| `e902549` | Update LEDGER_CONSOLIDATED.md |
| `31c2666` | batch 1 sourcing |
| `0739e6b` | batch 1 tier 2 |
| `ee29e6c` | batch 1 blind source |

All eighteen changed files are the cross-check evidence itself
(`documentation/batch1_*`, `documentation/worksheet_*`) plus one
`LEDGER_CONSOLIDATED.md` line. **Blob-hash comparison confirmed all five
build targets byte-identical between the two SHAs**, so the spec's line
numbers and anchor text remained valid. Benign-class mismatch; proceeded
with flagging.

---

## 2. Scope decision — Option A

The build was halted before writing any script because of a load-bearing
finding, and resumed on Tony's Option A decision.

**Finding.** For sphere shells, the display text in the five
`*_visualization_shells.py` modules is dead code. `shell_configs.py`
carries its own copy in `hover_text` / `tooltip`, and
`build_sphere_shell(config, ...)` reads hover text from the config dict.

Established by experiment on a throwaway copy, not by reading:

| Mutation | Render follows? |
|---|---|
| `1600-1700 K` in `moon_visualization_shells.py` | **No** |
| `1600-1700 K` in `shell_configs.py` | **Yes** |

Corroborated by grep: `create_moon_inner_core_shell`,
`create_pluto_atmosphere_shell` and `create_eris_hill_sphere_shell` are
imported by `planet_visualization.py` and never called. The module-level
`*_info` strings are imported by `palomas_orrery.py` and
`palomas_orrery_helpers.py` and never used downstream.

**Decision (Tony, this session): Option A.** Widen to six files so values
and render move together. `shell_configs.py` added to the patch set.

**Related structural finding.** Saturn, Uranus and Neptune already use the
reference pattern in `shell_configs.py`:

```python
'hover_text': neptune_hill_sphere_info.replace('\n', '<br>'),
'tooltip': neptune_hill_sphere_info,
```

For those bodies, editing the shell module *does* reach the render. The
codebase is mid-migration; Moon, Eris, Mercury, Venus and Pluto are among
the bodies still carrying duplicated inline copies. Migrating them to the
reference pattern is the structural fix that would retire this whole class
of drift. Not attempted here — it is a design decision, not a patch.

---

## 3. Deliverables

Six standalone transactional patch scripts, 76 edits total.

| Script | Target | Edits |
|--------|--------|------:|
| `patch_moon_cross_check.py` | `moon_visualization_shells.py` | 7 |
| `patch_eris_cross_check.py` | `eris_visualization_shells.py` | 9 |
| `patch_mercury_cross_check.py` | `mercury_visualization_shells.py` | 8 |
| `patch_venus_cross_check.py` | `venus_visualization_shells.py` | 10 |
| `patch_pluto_cross_check.py` | `pluto_visualization_shells.py` | 18 |
| `patch_shell_configs_cross_check.py` | `shell_configs.py` | 24 |

The spec counted 47 edits against five files. The count is 76 here because
several spec items expand to more than one anchored site (a module-level
`# Source:` and its inner twin, an info string and its description copy),
and because Option A added 24 mirror edits in `shell_configs.py`. No spec
item was dropped.

**Run order:** any order. Each script is independent and self-verifying.
Save each into the folder containing its target file, open in VS Code,
click Run. Success prints one `ok` line per edit then
`patch applied (N bytes, was M)`. Failure prints a single `ANCHOR FAIL:`
or `ERROR:` line and writes nothing.

Anchors were extracted programmatically from the pristine repo file by
line range — never hand-transcribed — so trailing whitespace and escaped
quotes are preserved byte-exact.

---

## 4. Verification performed

**Generation-time**
- All 76 anchors verified to occur exactly once in their target. One
  collision was caught and fixed: `'radius_fraction': 4685,` appears in
  both Pluto's and Neptune's `hill_sphere` blocks. The anchor was widened
  to three lines, which disambiguates because Neptune orders its keys
  differently. Without the single-match assertion this would have silently
  corrupted Neptune's Hill sphere.
- Edit ordering confirmed bottom-up within every file.

**Post-patch, on a full pristine copy**
- `py_compile` clean on all six files.
- Non-ASCII scan: clean. CRLF scan: clean (LF only).
- Re-run on an already-patched file fails loud (`ANCHOR FAIL`, exit 1) and
  leaves the file byte-identical. Confirmed by md5.
- Residual scan for every corrected value in both copies: zero survivors
  except two intentional/out-of-scope cases (section 6).
- `xvfb` GUI run of `palomas_orrery.py` on a **throwaway copy** —
  `SystemButtonFace` swap applied to the copy only; the copy was deleted
  and no deliverable was edited by the pre-test. Reached
  `[DASHBOARD] Dashboard ready.` with no errors.

**Live-dispatch smoke test** — traces constructed through
`build_sphere_shell` via `SHELL_CONFIGS`, then inspected. All twelve
sampled shells show the old value removed and the new value present:

Moon inner_core, Moon outer_core, Eris hill_sphere, Eris core, Mercury
outer_core, Mercury crust, Mercury atmosphere, Venus atmosphere, Venus
upper_atmosphere, Pluto core, Pluto crust, Pluto atmosphere — 0 failures.

**Geometry**

| Shell | Result | Expected |
|---|---|---|
| Pluto exobase | 2887.6 km = 2.43 R_Pluto | ~2.43 (was 1.43) |
| Pluto Hill sphere | 5.990 Mkm | ~5.99 (was ~5.57) |
| Mercury sodium tail | 3,408,749 km = 1397 R_M | ~1400 (was 10,000) |
| **Neptune Hill sphere** | **0.775541386098 AU** | **identical before/after** |

Neptune was compared numerically against the pristine tree, not eyeballed.

---

## 5. Independent re-derivation of the Hill sphere values

Recomputed from standard constants rather than transcribed from the spec:

| Body | Spec | Independent recomputation | Verdict |
|---|---|---|---|
| Venus | 166.0 / 167.1 R_V | 166.0 / 167.1 | exact |
| Eris | 8.0 / 14.3 Mkm | 7.995 / 14.265 | confirmed; file's 9.4 wrong |
| Pluto | 5.99 Mkm, rf 5041 | 5.982 Mkm, rf 5033.7 | agrees to 3 s.f. |
| Moon | 58,147–64,901 km | 58,152–64,907 km | 0.01% delta |

GPT's worksheet independently derived Eris at 14.27 Mkm and Gemini at
14.26 Mkm — three-way convergence against 14.265.

**Moon delta noted, not papered over.** The ~5 km difference comes from
perigee/apogee input choice. The spec's figures were used, since they are
the decided cross-check output.

PLUT-2's unit confusion re-derived independently: 1,700 km is an altitude,
so from centre (1188.3 + 1700) / 1188.3 = **2.43**, and the display text's
"0.43 Pluto radii above the surface" should read 1.43. Internally
consistent under the fix.

---

## 6. Flagged — decisions for Tony, not silently actioned

**a. Mercury's mantle still claims a diamond layer.**
MERC-4 drops the diamond claim from the *crust* per spec. The *mantle*
text still says it, and the spec does not list a Mercury mantle edit:
- `mercury_visualization_shells.py` line 55
- `shell_configs.py` lines 144 (hover) and 149 (tooltip)

Left in place deliberately. Dropping it is a one-line follow-up if wanted.

**b. `shell_configs.py` body-level header citations are now stale.**
Each body block carries a header `# Source:` / `# Verified:` pair that
Batch 1 did not touch. Two now contradict the values below them:

- Line 93–94 (Mercury): cites `Margot et al. (2012), Sori (2018)` — but
  MERC-3 replaced Margot's 1074 km with Hauck 2013's 2020 km, and MERC-4
  changed Sori's value from 35 to 26 km.
- Line 236–239 (Moon): cites `Apollo Seismic Experiment reports` — MOON-2
  replaced that with Nakamura 1982/2005.

This is the citation-layer version of the same producer/consumer drift.
Recommend a small follow-up patch or folding into Batch 2. Not done here
because these headers cover claims outside Batch 1's cross-check.

**c. Sixteen `# Verified: April 2026 ...` stamps remain in
`shell_configs.py`** (plus comet 6, earth 13, jupiter 9). Different
wording from the module-level ones and mostly on Batch 2+ bodies. Out of
scope; flagged for a sweep.

**d. Moon inner core keeps `# dark red-orange at 1700K`** as a colour
rationale comment (module line 50). With the temperature claim now removed
from Source and display text, the scanner may flag this as an uncited
1700K. Not in spec; left alone.

**e. MOON-1's range is single-leg.** `58,147`/`64,901` appear only in
`worksheet_claude_batch1_tier2.md`. The annotation says so explicitly and
records that a second independent leg is still owed for V2 scoring. Same
for Pluto's `rf 5041`, though GPT independently supplied the GM inputs, so
that one has two legs of a kind.

**f. Spec corrections found during the build**
- MERC-6 cites lines 524/594; `mercury_visualization_shells.py` is 406
  lines. Those are Venus's numbers (VEN-6 lists 505/524/594). Mercury's
  Winslow sites are 260, 263, 268, 344. Implemented from line 233, which
  is unambiguous; the inline Winslow sites were left as-is.
- `# Verified: April 2026 via Gemini fact-check` count is **9**, not "3 in
  Eris and scattered across the others": Eris 37/210/460 and Mercury
  45/59/68/82/234/399. **Moon, Venus and Pluto have none**, so the spec's
  removal instructions for those three files were no-ops.
- VEN-4 approach (a) was not used. The two Venus blocks are not identical
  — the description carries an extra troposphere paragraph the info block
  lacks — so de-duplication would have been partial regardless. Approach
  (b) was used, with a `# NOTE: duplicated text` comment added. The spec's
  `.replace("\\n", "<br>")` would have matched nothing; the source contains
  real newlines, so the correct call is `.replace("\n", "<br>")`, and
  getting it wrong fails silently into unbroken hover text.

---

## 7. Provenance discipline applied

- No bibliographic detail was added beyond what the spec supplied. Where
  a volume or page number was not in the spec, the existing citation form
  was kept rather than enriched from recall.
- Every `# Cross-checked:` parenthetical was verified to point at a
  worksheet on disk that actually contains the finding, by grepping the
  `documentation/batch1_*` and `worksheet_*` files for each citation and
  each corrected value.
- Unsourceable claims were **removed and the gap noted**, never re-cited:
  Moon inner/outer core temperatures, Pluto core temperature, Pluto N2
  purity, Mercury's diamond layer, Venus thermosphere/ionosphere
  specifics. Each carries a `# Removed:` note stating why.
- Format follows the Mars precedent: source leads, model is subordinate,
  worksheet is the audit trail, ISO date is the check date.

---

## 8. After the patches

1. Run each script in VS Code, one at a time, checking output. **Confirm
   each individually** — a later success does not confirm an earlier one.
2. Mode 5: open the orrery and look at Pluto's atmosphere shell (now ~70%
   larger), Pluto's Hill sphere, and Mercury's sodium tail (now ~7x
   shorter). Tony's eyes are the close gate.
3. Run `provenance_scanner.py` Tony-side, where
   `data/provenance_exceptions.json` lives, and confirm Tier-1 = 0 before
   push.
4. Commit and push; record the new SHA in this document and the ledger.
5. Ledger: close Batch 1, open items for section 6 (a)–(d) and the
   `shell_configs.py` reference-pattern migration.

---

*Built on `ee29e6c691cad2995992396e692fae1d0d5cadc0` at
https://github.com/tonylquintanilla/palomas_orrery*
