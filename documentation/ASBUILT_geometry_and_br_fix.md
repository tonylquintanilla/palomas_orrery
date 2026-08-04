# As-Built — Geometry Corrections + `<br>` Fix

**Built on `06a16df768a010205b7078630ac31bf0cd17f846`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Built:** August 4, 2026 by Claude Opus 5 · Tony Quintanilla, integrator
**Implements:** L-156 Batch 1 geometry follow-up + Mars retroactive fix
**Input:** `PROMPT_opus5_geometry_and_br_fix.md`, `FABLE_shell_consistency_audit_report.md`
**Pushed at:** _(fill in after push)_

---

## 1. Anchor reconciliation

Three SHAs were in play at session start:

| SHA | What it actually is |
|-----|---------------------|
| `80c8580` | Real — the commit creating the prompt file; unpushed when first checked |
| `f83a3ab` | HEAD of **`tonyquintanilla.github.io`** (gallery repo), not the orrery |
| `06a16df` | Orrery HEAD after Tony's push — the build base |

The `80c8580` "does not exist" reading was correct at the moment of the check
and resolved on push. That is the SHA round trip working as designed: the one
failure mode is honest and visible.

**All ten source files are byte-identical between `80c8580` and `06a16df`**
(blob-hash comparison), so the prompt's line numbers and current values are
valid at the build base. The only delta is the prompt document itself.

---

## 2. Verification of the input claims

Fable's audit and the prompt were treated as claims and checked against HEAD.
Every `radius_fraction` and text value was read from the live runtime dicts.

**Confirmed exactly as reported:** Mercury outer_core 0.85 → 2,073.7 km;
Mercury mantle encoded thickness 317.2 km vs text 331 km; Mercury crust
encoded 48.8 km vs text 26 km; Moon inner_core 0.1485 → 258.0 km; Moon
outer_core 0.2083 → 361.9 km; Venus core 0.5 → 3,025.9 km; Venus crust
encoded 121.0 km; Eris mantle 0.60→0.66 = 69.8 km vs text "around 100
kilometers"; Mars live config 324.5 vs dead copies 320; `<br>` census
(moon 26, eris 28, pluto 36, mars 28; mercury/venus already clean).

**Three corrections to the inputs:**

1. **Finding #43 (Moon `:*` artifact) is not a Batch 1 artifact and is not
   confined to dead code.** It is present at `ee29e6c` — *before* Batch 1 —
   so it predates the patches. And it exists in the **live** config copy
   (`shell_configs.py:275`) as well as the module copy (`moon:139`), so it
   actually renders in the Plotly hover. Both sites are fixed here; Fable
   located only the module copy.

2. **Mars has a fourth dead-copy site the prompt missed.** Beyond
   `mars:844`, `mars:859` and `mars:884`, there is
   `'radius_fraction': 320,` at **`mars:854`** in a dead legacy dict. All
   four are corrected.

3. **No cross-checked value exists for the Mercury Hill scale note.** The
   worksheets addressed the Hill sphere `radius_fraction`, not the display
   scale hint. Per the prompt's fallback, the value was computed: rf 94.4
   → 230,308 km = 0.00154 AU radius, **0.00308 AU diameter**. The module's
   "0.003 AU" would clip the shell; the config's "0.005 AU" shows it with
   margin. Harmonized to **0.005 AU**. Gap flagged below.

---

## 3. Deliverables

Seven transactional patch scripts, 47 edits.

| Script | Target | Edits |
|--------|--------|------:|
| `patch_shell_configs_geometry.py` | `shell_configs.py` | 14 |
| `patch_mercury_geometry_text.py` | `mercury_visualization_shells.py` | 4 |
| `patch_mars_dead_copies.py` | `mars_visualization_shells.py` | 11 |
| `patch_moon_br_fix.py` | `moon_visualization_shells.py` | 6 |
| `patch_eris_br_fix.py` | `eris_visualization_shells.py` | 5 |
| `patch_pluto_br_fix.py` | `pluto_visualization_shells.py` | 6 |
| `patch_orrery_comment.py` | `palomas_orrery.py` | 1 |

Run in any order; each is independent and self-verifying. Save each into the
folder holding its target file, open in VS Code, click Run.

### Corrected geometry — every value derived, not transcribed

| Body | Shell | Old rf | New rf | Encodes | Basis |
|---|---|---|---|---|---|
| Mercury | outer_core | 0.85 | **0.828** | 2,020.1 km | Hauck 2013, 2020 ± 30 km |
| Mercury | mantle | 0.98 | **0.9636** | 2,350.9 km | 2,020 + 331 km |
| Moon | inner_core | 0.1485 | **0.1381** | 239.9 km | Weber 2011, 240 km |
| Moon | outer_core | 0.2083 | **0.1899** | 329.9 km | 330 km |
| Venus | core | 0.5 | **0.5288** | 3,200.2 km | NASA Fact Sheet, 3,200 km |
| Eris | mantle | 0.66 | **0.686** | 797.8 km | core 697.8 + 100 km ice |
| Mars | hill (×4 dead) | 320 | **324.5** | — | matches live config |

Each derived as `km ÷ body radius` using `constants_new.py` values read at
runtime (Mercury 2,439.7 · Moon 1,737.4 · Venus 6,051.8 · Eris 1,163 ·
Mars 3,396.2).

---

## 4. Verification performed

- All 47 anchors verified to occur exactly once. **Seven collisions were
  caught and fixed** during generation: bare `'radius_fraction': 1.0,` and
  `0.98,` lines repeat across bodies. Mercury's and Venus's mantle blocks
  are byte-identical through `marker_size`, so the Mercury mantle rf edit
  was merged with its hover-text edit into one atomic anchor keyed on the
  unique hover string. Without the single-match assertion these would have
  silently written to the wrong body — the same class as Batch 1's Neptune
  `4685` collision.
- `py_compile` clean on all seven targets; all seven scripts compile.
- ASCII clean, LF only, on every patched file.
- Re-run on an already-patched file fails loud and leaves it byte-identical
  (md5 confirmed).
- **Live-dispatch smoke test:** shells built through `build_sphere_shell` via
  `SHELL_CONFIGS` render at 2020.1 / 239.9 / 329.9 / 3200.2 / 797.8 km — all
  within 2 km of target.
- **Unchanged guard:** Mars hill 324.5, Pluto hill 5041, Pluto atmosphere
  2.43, **Neptune hill 4685**, Mercury crust 1.0, Venus crust 1.0 — all
  verified unmoved.
- `<br>` residual in module `_info` strings: **0** across all six bodies.
  118 conversions total, matching the pre-count exactly.
- Diamond claim absent from Mercury mantle hover; `<br>:` artifact absent.
- `xvfb` GUI run of `palomas_orrery.py` on a **throwaway copy** reached
  `[DASHBOARD] Dashboard ready.` The throwaway was deleted; no deliverable
  was edited by the pre-test.

---

## 5. Flagged, not resolved (per prompt instruction)

**Layer-chain gaps — comments added in the code, values left alone.**

- **Mercury:** 2,020 + 331 + 26 = 2,377 km against R = 2,439.7 km — a
  **62.7 km** shortfall. Crust stays at rf 1.0, so its drawn thickness is
  **~88.8 km**, not 26 km. Note this **grew from ~48.8 km** when the mantle
  moved to 0.9636 — correcting the mantle made the crust *more* stylized.
  Mode 5 decision.
- **Venus:** crust drawn at ~121 km against text 10–30 km. Closing it
  numerically would make the crust shell essentially invisible. Mode 5.

**New finding — an error I introduced in Batch 1. Needs your decision.**

Mercury's Hill sphere `radius_fraction` is 94.4, encoding 230,308 km. My
independent computation gives:

| Convention | Hill radius | In R_M |
|---|---|---|
| perihelion 0.30750 AU | 175,297 km | 71.85 |
| semi-major 0.38710 AU | 220,675 km | 90.45 |
| aphelion 0.46670 AU | 266,052 km | 109.05 |
| **code rf 94.4** | **230,308 km** | **94.40** |

The Batch 1 citation I wrote at `mercury:414-416` asserts **"Perihelion
convention"** — which would be 71.85 R_M, not 94.4. The geometry matches no
standard convention, and 230,308 km sits **above** the 175,000–225,000 km
range Gemini's tier-2 worksheet supplied. Fable did not catch this because
Mercury's Hill display text is qualitative — there is no number in the text
for the constant to contradict.

This is wrong-but-cited, the failure mode the discipline names as worse than
uncited. I did not patch it: the fix depends on which convention you choose
(move the citation, move the constant, or send it to Batch 2 cross-check).
Say the word and it is a one-line change either way.

**Other flagged items (not patched, for ledger):** Moon crust three-way text
disagreement · Moon `# dark red-orange at 1700K` comment · Eris layer
structure inversion (Fable #10) · Earth shadow constants · solar
gravitational 150k vs 126k · Saturn Hill three-way · solar chromosphere
three extents · 44 remaining "Verified: April 2026" stamps (two removed here,
in the Mercury and Moon headers) · Jupiter/Saturn false "not yet rendered"
claims · 124 dead `tooltip` fields.

**Consequence of a decision already made:** dropping "SET MANUAL SCALE" from
Mercury's crust and exosphere `_info` removes that guidance from the GUI
checkbox tooltip. The alternative — propagating the line into the config
instead — remains available if the guidance turns out to be wanted.

---

## 6. After the patches

1. Run each script in VS Code, one at a time, confirming each individually.
2. **Mode 5 is the close gate**, and this round changes what you will see:
   Mercury's outer core shrinks slightly and its mantle noticeably; Moon's
   two cores shrink ~7% and ~9%; Venus's core grows ~6%; Eris's mantle
   thickens. Mercury's crust band will look thicker than before.
3. **Also Mode 5 the GUI tooltips** — the `<br>` fix is code-path-proven but
   render-unverified. Tick any Moon, Eris, Pluto or Mars shell checkbox and
   confirm the tooltip shows real line breaks instead of literal `<br>`.
4. Run `provenance_scanner.py` on your side; confirm Tier-1 = 0 before push.
5. Commit, push, record the new SHA here and in the ledger.

---

*Built on `06a16df768a010205b7078630ac31bf0cd17f846` at
https://github.com/tonylquintanilla/palomas_orrery*
