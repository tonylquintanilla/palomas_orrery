# Relay response: L-191 display-text survey

**Built on `e1c64dc955ba3323312d9b23ed53547985fe32cb` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 21, 2026 with Anthropic's Claude Fable 5, in response to
RELAY_REQUEST_L191_survey_fable_20260820.md.**

At survey time `git ls-remote` reported remote HEAD equal to the pinned
SHA, so this survey describes the repository's current state, not just a
historical snapshot. All file:line references below are at that SHA.
Method: static analysis of the parsed code (Python's `ast` module), no
repo code executed, no files edited. Two machine-readable evidence files
accompany this document: `l191_inventory.json` (every tooltip binding,
resolved) and `l191_cfgmap.json` (every `hover_text` entry mapped to its
module twin).

To preserve independence of the count, the code measurement was
completed **before** reading the L-191 ledger item. The ledger was
opened only afterward, for the comparison in section (b).

---

## Executive summary

**58 strings reach a Tkinter tooltip and carry `<br>` — not 20.** The
ledger's figure of "20, all in `solar_visualization_shells.py`" misses
39 strings that reach tooltips through a constructed-name loop in
`celestial_objects.py`, where the string's name never appears next to
`CreateToolTip` in source. The ledger's companion claim — "gas giant
shells have NO tooltips at all" — is false at this SHA and was already
false on the ledger's own measurement date: the loop path has been in
the tree since January 2026 and the checkbox variables since April
2025. Jupiter, Saturn, Uranus, Neptune, Planet 9, and one Moon string
are broken exactly the way solar is; solar is merely where it was seen.

The deeper finding matches the ledger's: the format bug is the small
problem. 41 of the 52 inline `hover_text` copies in `shell_configs.py`
differ from their module `_info` twin, with nothing on screen or in the
code keeping any pair aligned.

---

## (a) Inventory: every string reaching a Tkinter tooltip

### The surfaces

Three Tkinter tooltip mechanisms exist; a fourth candidate has none.

| Mechanism | Defined at | Live bindings |
|---|---|---|
| `CreateToolTip` (main GUI) | `palomas_orrery.py:3533` | 94 direct call sites + 78 via loop |
| `CreateToolTip` (param viz, own copy) | `orbital_param_viz.py:35` | 2 |
| `Tooltip` (dashboard) | `palomas_orrery_dashboard.py:506` | 1 (`:926`) |
| `star_visualization_gui.py` | — | none (verified: no tooltip class or call) |

Grep finds 102 `CreateToolTip(` call lines in `palomas_orrery.py`; the
AST finds 94 live calls. The 8 extra grep hits (lines 8992, 10284,
10765, 10796, 10806, 10817, 10873, 10889) are all commented out — dead,
excluded.

**The loop path** (the one the relay flagged):
`build_shell_checkboxes()` at `celestial_objects.py:1457-1495` builds
the tooltip name at runtime as `f"{body_prefix}_{shell['var_suffix']}_info"`,
fetches it from `globals()` passed in from `palomas_orrery.py`, and
binds it at `celestial_objects.py:1493`. It is called for 11 bodies at
`palomas_orrery.py:9125, 9128, 9216, 9263, 9294, 9306, 9328, 9340,
9347, 9388, 9400` (Mercury, Venus, Moon, Mars, Jupiter, Saturn, Uranus,
Neptune, Pluto, Eris, Planet 9). `SHELL_DEFINITIONS`
(`celestial_objects.py:1332`) yields 78 constructed names. All 78
resolve to module-level string literals, and all 78 companion
`*_var` checkbox variables exist in `palomas_orrery.py` (verified name
by name — a missing variable would silently skip the checkbox, and
none is missing). All 78 bindings are live.

### The 58 affected strings (reach Tkinter AND carry `<br>`)

**Via the loop — 39 strings.** Formats verified on the evaluated
literal value; every one is pure `<br>` (no literal `\n` mixed in).

| Body | Count | Names (defining module and line) |
|---|---|---|
| Jupiter | 10 | `jupiter_core_info` :76, `jupiter_metallic_hydrogen_info` :147, `jupiter_molecular_hydrogen_info` :217, `jupiter_cloud_layer_info` :289, `jupiter_upper_atmosphere_info` :446, `jupiter_io_plasma_torus_info` :624, `jupiter_radiation_belts_info` :701, `jupiter_hill_sphere_info` :791, `jupiter_ring_system_info` :868, `jupiter_magnetosphere_info` :1030 — all in `jupiter_visualization_shells.py` |
| Saturn | 10 | `saturn_core_info` :38, `saturn_metallic_hydrogen_info` :124, `saturn_molecular_hydrogen_info` :201, `saturn_cloud_layer_info` :277, `saturn_upper_atmosphere_info` :484, `saturn_enceladus_plasma_torus_info` :707, `saturn_radiation_belts_info` :810, `saturn_hill_sphere_info` :931, `saturn_ring_system_info` :1012, `saturn_magnetosphere_info` :1230 — all in `saturn_visualization_shells.py` |
| Uranus | 8 | `uranus_core_info` :38, `uranus_mantle_info` :106, `uranus_cloud_layer_info` :183, `uranus_upper_atmosphere_info` :360, `uranus_magnetosphere_info` :448, `uranus_radiation_belts_info` :616, `uranus_ring_system_info` :770, `uranus_hill_sphere_info` :1145 — all in `uranus_visualization_shells.py` |
| Neptune | 8 | `neptune_core_info` :39, `neptune_mantle_info` :112, `neptune_cloud_layer_info` :196, `neptune_upper_atmosphere_info` :369, `neptune_magnetosphere_info` :461, `neptune_radiation_belts_info` :824, `neptune_ring_system_info` :1170, `neptune_hill_sphere_info` :1682 — all in `neptune_visualization_shells.py` |
| Planet 9 | 2 | `planet9_surface_info` :37, `planet9_hill_sphere_info` :214 — `planet9_visualization_shells.py` |
| Moon | 1 | `moon_hill_sphere_info` — `moon_visualization_shells.py:585` (the other 5 Moon strings are clean `\n`) |

**Via direct calls — 19 strings, all defined in
`solar_visualization_shells.py`.** Call sites in `palomas_orrery.py`.

| Name | Defined at | Call site | Form |
|---|---|---|---|
| `hover_text_sun_and_corona_tooltip` | :970 | :8993 | f-string, `<br>` |
| `core_info` | :445 | :9006 | literal |
| `radiative_zone_info` | :416 | :9010 | literal |
| `photosphere_info` | :383 | :9014 | literal |
| `chromosphere_info` | :354 | :9023 | concat + constant, `<br>` |
| `inner_corona_info` | :317 | :9027 | literal |
| `roche_limit_info` | :686 | :9032 | literal |
| `streamer_belt_info` | :625 | :9037 | literal |
| `alfven_surface_info` | :743 | :9042 | f-string, `<br>` |
| `outer_corona_info` | :296 | :9046 | f-string, `<br>` |
| `termination_shock_info` | :282 | :9080 | literal |
| `solar_wind_info` (Heliopause checkbox) | :249 | :9084 | literal |
| `inner_limit_oort_info` | :155 | :9092 | literal |
| `hills_cloud_torus_info` | :170 | :9096 | literal |
| `inner_oort_info` | :140 | :9100 | literal |
| `outer_oort_clumpy_info` | :195 | :9104 | literal |
| `galactic_tide_info` | :224 | :9108 | literal |
| `outer_oort_info` | :122 | :9112 | literal |
| `gravitational_influence_info` | :96 | :9120 | concat + constant, `<br>` |

The five non-literal forms (f-strings and concatenations interpolating
module constants) were classified by source inspection after the
automatic resolver flagged them; all five visibly carry `<br>`
throughout.

Consumer check: each of the 58 has exactly **one live consumer — the
tooltip**. The imports of these names in `palomas_orrery_helpers.py`
and `planet_visualization.py` are dead (zero load-uses in either file,
verified by AST), and none is used inside its own module's Plotly
builders.

### The clean strings (reach Tkinter, no `<br>`)

- **Loop, 39 strings, `\n`:** Mercury 8, Venus 7, Moon 5 of 6, Mars 8,
  Pluto 6, Eris 5. The loop splits exactly 39/39, and exactly along
  module lines — every giant-planet string broken, every
  terrestrial/dwarf string clean except Moon's Hill sphere.
- **Earth, 11 strings, `\n`:** direct calls at `palomas_orrery.py:9142-9213`,
  defined `earth_visualization_shells.py:55, 127, 199, 269, 339, 492,
  564, 637, 870, 986, 1097`.
- **Asteroid belt, 4 strings, `\n`:** `main_belt_info`,
  `hilda_group_info`, `jupiter_trojans_greeks_info`,
  `jupiter_trojans_trojans_info` in
  `asteroid_belt_visualization_shells.py`; call sites
  `palomas_orrery.py:9052-9072`.
- **Object checkboxes via `INFO`** (`info_dictionary.py:265`, imported
  at `palomas_orrery.py:283`): 183 entries — 114 with `\n`, 68 with no
  breaks, 1 f-string (`MAPS`, `\n`), **0 with `<br>`**. Reached at
  `palomas_orrery.py:8915, 8925, 10097, 10103` and inside f-string
  composites (perihelion presets at :9418/:9877/:9887/:9941/:9995/:10005,
  comet fragments at :10043) which append `\n`-formatted suffixes —
  clean.
- **GUI-control tooltips** (buttons, entry fields, scale controls):
  45 strings defined in `palomas_orrery.py` itself (24 with `\n`, 21
  with no breaks) plus spacecraft-encounter f-strings (`\n`) — clean.
- **`orbital_param_viz.py`:** 2 self-contained strings, `\n`.
- **Dashboard:** 1 dynamic string (`:925`), no breaks.

The relay's scope exclusion is honored: the 124 dead `tooltip` dict
keys in `shell_configs.py` were not surveyed beyond confirming they
were not counted anywhere above.

---

## (b) The count, derived independently

**Definition used:** count distinct string definitions (one defining
assignment = one string) that (1) are live-bound to a Tkinter tooltip
at this SHA — through a direct `CreateToolTip`/`Tooltip` call or
through the constructed-name loop with the checkbox variable confirmed
present — and (2) contain `<br>` in their evaluated value.

**How it was counted:** enumerate all tooltip classes and all call
sites by AST (not grep — grep over-counts by 8 commented-out calls);
resolve argument 2 of every call through the import graph to its
defining assignment; expand the loop's 78 names from
`SHELL_DEFINITIONS` and verify each name and its `*_var` exist in
`palomas_orrery.py`'s globals; evaluate each resolved value and test
for the substring `<br`. Five values that would not fold automatically
were classified by reading their source. Only `<br>` exists — no
`<br/>` or `<br />` anywhere in the shell modules — so the
classification has no variant ambiguity, and no affected string mixes
literal `\n` with `<br>`.

**Result: 58** = 39 (loop) + 19 (direct, all solar-defined).

**Against the ledger (read after the count was fixed):** L-191 records
**20, all in `solar_visualization_shells.py`**, and separately asserts
zero `CreateToolTip` bindings for any gas-giant shell. The disagreement
locates precisely:

1. **The loop is invisible to call-site name resolution.** No
   gas-giant string name ever appears next to `CreateToolTip` in
   source; the name is assembled at runtime and fetched from
   `globals()`. A survey that "resolved every name bound to
   `CreateToolTip` back to its definition" — the ledger's stated
   method — resolves the loop's binding to the local `tooltip_text`
   and stops, never expanding `SHELL_DEFINITIONS`. That is a third
   instance of the failure L-191 itself records twice: the proxy
   (names visibly bound at call sites) stood in for the thing
   (strings that reach the surface).
2. **The surface existed when the ledger measured.** This is not tree
   movement. `build_shell_checkboxes` and `SHELL_DEFINITIONS` with the
   gas giants entered at `1bfa6c1` (2026-01-27); the gas-giant
   checkbox variables date to `6b3757b` (2025-04-18). Both predate the
   2026-08-07 measurement.
3. **Solar: 19 here vs 20 there — unresolved, small.** My 19 is 18
   `_info`-named strings plus `hover_text_sun_and_corona_tooltip`,
   which matches the ledger's own Gap arithmetic ("author the 18
   `_info` strings") more closely than its headline 20. The ledger
   does not pin the SHA its count was taken at, and solar has been
   patched since (L-209 among others), so the one-string delta could
   be tree movement or a counting-unit difference. Locating it needs
   the August 7 base SHA.

**Cheapest confirmation, and it is the render's to give:** hover any
Jupiter shell checkbox (e.g. "-- Core"). If literal `<br>` shows, the
wider scope is confirmed on screen, where it counts, and not only in
the AST. Per the protocol, my static claim does not outrank the render.

---

## (c) Pattern map

Live sources per family at this SHA. "Tooltip" is the Tkinter surface;
"plot" is the Plotly hover. Sphere shells render via
`SHELL_CONFIGS -> build_sphere_shell()` (`orrery_rendering.py`,
dispatched at `planet_visualization.py:425`); custom shells render via
`CUSTOM_SHELLS` and lazy-imported builder functions whose inline text
is live.

| Family | Tooltip source | Plot source | Copies | State |
|---|---|---|---|---|
| Solar (19 checkboxes) | module `_info`, direct calls | 15 `_info_hover` strings referenced by name at `shell_configs.py:1891-2048`; remainder inline in builders | two authored copies per shell | **format bug visible**; pair agreement measured in (d) |
| Saturn, Uranus, Neptune sphere shells (16) | module `_info`, loop | same `_info` via `'hover_text': X.replace('\n','<br>')` — the reference pattern, `shell_configs.py` | **one** text source | **format bug visible**; the `.replace` is a no-op today because the source carries `<br>` (the trap the conventions skill names) — plot correct by accident |
| Jupiter (10), Planet 9 (2), Moon Hill (1) | module `_info`, loop | independent inline literals in `shell_configs.py` | two copies | **format bug visible** on tooltip; plot correct; copies diverged (see (d)) |
| Mercury, Venus, Moon (5), Mars, Pluto, Eris sphere shells | module `_info`, loop | independent inline literals in `shell_configs.py` | two copies | tooltip clean; **silently diverged** — the L-182 shape |
| Earth sphere shells (8) | module `_info`, direct calls | independent inline literals in `shell_configs.py` | two live copies **plus a dead third** (module builder dicts — `create_earth_*` functions are imported but never called anywhere) | tooltip clean; 6 pairs verbatim, crust deliberately different, Hill sphere diverged |
| Earth custom (magnetosphere, LEO, GEO belt) + all custom shells | module `_info` (Earth direct; others loop) | live inline text inside builder functions | two copies | tooltip side measured; builder-side agreement **not measured** (open item 2) |
| Asteroid belt (4) | module `_info`, direct calls | inline in builders | two copies | tooltip clean |
| Object checkboxes | `INFO` dict, single string per object | n/a (tooltip-only) | one | clean |
| GUI controls | inline/local strings | n/a | one | clean |

One correction to the ledger's four-pattern table follows from the
above: the "gas giants: tooltip source none" row is wrong, and with it
the "why only solar broke" explanation. Solar is not the only module
whose `_info` goes to Tkinter unconverted — all eleven loop bodies'
strings do. The giants broke identically and were not seen; the
terrestrials/dwarfs are clean today, so the same edit shows nothing
there.

---

## (d) Duplication risk, measured

**Same-module pairs (`_info` / `_info_hover`) — solar only, 15 pairs
plus one composite.** No other module defines `_info_hover` names, and
no `_info_hover` exists without its `_info` partner.

- **9 pairs verbatim identical** after `<br>`↔`\n` normalization:
  `core`, `radiative_zone`, `photosphere`, `chromosphere`,
  `inner_oort`, `outer_oort`, `inner_limit_oort`, `solar_wind`,
  `termination_shock`. Two hand-authored copies of the same text, no
  linking mechanism — pure redundancy awaiting drift.
- **1 pair differs by surface-specific text only:**
  `gravitational_influence` — the `_info` copy prepends "SELECT A
  MANUAL SCALE OF AT LEAST 160,000 AU TO VISUALIZE." and is otherwise
  identical to the hover. Note the direction: this is a
  **tooltip-only** addition, the mirror image of Earth's hover-only
  legend note. Surface-specific text runs both ways.
- **4 pairs deliberately divergent in content:** `inner_corona`
  (similarity 0.20), `outer_corona` (0.35), `alfven_surface` (0.35),
  `roche_limit` (0.49), `streamer_belt` (0.51) — condensed or
  restructured hover variants. (That is five items; `roche_limit` and
  `streamer_belt` sit between "condensed" and "enriched.") Evidence of
  one-sided maintenance inside this set: `inner_corona_info_hover`
  carries MAPS C/2026 A1 and Kreutz-sungrazer content the tooltip copy
  lacks entirely — the hover was updated in 2026, the tooltip was not.
  Measured: the contents differ. Inferred: which differences are
  design and which are drift.
- **The composite pair:** `hover_text_sun_and_corona` (:943) vs
  `hover_text_sun_and_corona_tooltip` (:970) differ **only** by
  removal of `<b>`/`</b>` tags — the `<br>` tags were left in when the
  tooltip variant was made. And the plot-side variant is now **dead**:
  its only call site is the commented line `palomas_orrery.py:8992`.

**Cross-file pairs (module `_info` vs `shell_configs.py` inline
`hover_text`) — the sphere-shell duplication.** 83 `hover_text` entries
total: 31 reference-form (16 `.replace` + 15 `_info_hover` names) and
52 independent inline literals. Of the 52, matched to their module
twin by constructed name (all 52 matched):

- **11 agree verbatim** after normalization (Earth 6, Venus 3, Mercury
  and Moon partial) — agreement with no mechanism, the pair class the
  relay says matters most.
- **41 differ.** Full list with similarity ratios in
  `l191_cfgmap.json`. Six sit at 0.93-0.97 (Jupiter core 0.963, Jupiter
  molecular H 0.936, Jupiter upper atmosphere 0.965, Moon Hill 0.946,
  Pluto Hill 0.971, Eris mantle 0.973) — near-identical, classic
  unmechanized drift. The rest range 0.03-0.90; in every sampled case
  the `shell_configs.py` copy is the richer one (title lines, scale
  instructions, citations and range conventions from the Batch 1
  provenance work), and the module `_info` copy fell behind. Measured:
  they differ, and how much. Inferred: the direction of maintenance.
- **Earth specifically** (the design case): 8 sphere pairs — 6
  verbatim; crust differs by exactly the deliberate hover-only
  additions (title line + "(Note: toggle off the crust layer in the
  legend to better see the interior structure.)" — verified
  byte-for-byte against the constraint in the relay's section 4); Hill
  sphere genuinely diverged (0.164 — the tooltip copy is a 126-char
  stub, the config copy is the full text). The 3 custom Earth shells
  (magnetosphere, LEO, GEO belt) have no config pair; their plot text
  lives in the builders.

**No-partner strings:** 4 asteroid-belt, 183 `INFO`, and all
GUI-control strings are single-copy — tooltip-only, no drift exposure.

**Dead copies, for completeness (not scope):** the 124 `tooltip` dict
keys (excluded per the relay), the Earth/other module builder layer
dicts (dead for sphere shells), and `hover_text_sun_and_corona`
(plot variant, only consumer commented out). Any naive promotion or
"restoration" of these resurrects stale text.

**One structural hazard found in passing:** the loop's lookup is
`tooltips_dict.get(tooltip_name, "No information available")`
(`celestial_objects.py:1488`). A renamed or deleted `_info` string
fails silently into that fallback — a check that cannot fail. Any
design that renames strings must account for it.

---

## (e) Design, against Earth's constraint

The mechanism, concretely. Three rules and one escape hatch:

**1. One authored body per shell, in `\n`, keeping the existing
`<thing>_info` name.** The name is load-bearing: the loop constructs
it, and the April 2025 convention already means "tooltip format." The
body is the shared text both surfaces show.

**2. Surface-specific text is a named, `\n`-authored module constant,
composed at the consuming boundary — never merged into the body.**

```python
# earth_visualization_shells.py -- authored once, tooltip-ready:
earth_crust_info = ("Earth's crust is the thin, solid outer layer ...")

EARTH_CRUST_HOVER_PREFIX = (
    "Earth Crust\n"
    "(Note: toggle off the crust layer in the legend to better see "
    "the interior structure.)\n\n")
```

**3. `<br>` exists in exactly one place: the Plotly boundary
conversion**, which is the reference pattern the tree already uses,
extended to carry the additions:

```python
# shell_configs.py -- the Plotly boundary:
'hover_text': (EARTH_CRUST_HOVER_PREFIX + earth_crust_info)
                  .replace('\n', '<br>'),
```

The tooltip consumes `earth_crust_info` directly, as it does today.
The hover gets prefix + body, converted. Tooltip-only additions (the
gravitational-influence scale instruction) are the same move mirrored:
`CreateToolTip(cb, GRAV_SCALE_NOTE + gravitational_influence_info)`
with the hover taking the bare body. Both directions the codebase
actually contains are covered, and every addition is a named constant
a grep can find.

**The escape hatch:** genuinely divergent texts — solar's condensed
hover variants — stay separately authored. But the pair must then be
*marked* as deliberately divergent (a comment at both definitions, or a
rename that breaks the implied twin-ship), because today an unmarked
`_info`/`_info_hover` pair is indistinguishable from a drifted one,
and that ambiguity is how the inner-corona tooltip silently missed the
2026 MAPS update its hover received. Whether each of the five divergent
solar pairs stays divergent or reconciles into body-plus-additions is a
content ruling, Tony's, per pair.

**What it costs:**

- **Content reconciliation is the real cost, and it is not
  mechanical.** For the 41 differing config pairs, someone must rule
  which copy is authoritative before the copies can collapse — and the
  richer config copies carry Batch 1 citation work, so this
  reconciliation overlaps L-181's constant-layer migration and the
  provenance discipline. Rulings can be batched per family, but they
  are rulings, not replaces.
- **A byte-compare gate on the Plotly side.** For the 16
  reference-pattern entries, converting the module string to `\n`
  makes the no-op `.replace` go live; the converted output must
  byte-equal today's hover text or the render changes silently. Cheap
  to check in the patch script, mandatory to check.
- **Two conventions to keep:** inserted text ASCII-only, and the
  `_info` suffix contract with the loop (rule 1 preserves it; any
  deviation hits the silent `"No information available"` fallback).
- **What it buys:** for every unified pair, agreement stops being a
  fact to verify and becomes a property of the structure — the drift
  class this item exists to kill is closed by construction, not by
  vigilance.

---

## (f) Order of work, with what goes wrong at each step

**0. Confirm scope on screen, then correct the ledger.**
Tony-action (do): hover one Jupiter shell checkbox. Tony-action
(decide): L-191's scope figure and pattern table, corrected per this
survey (or per the reconciliation if the render disagrees with me).
Risk of skipping: the sweep gets planned against 20 strings and
delivers a third of the fix, which is this item's twice-recorded
failure mode.

**1. Rule the authoritative-copy policy for divergent pairs.**
Tony-action (decide), per family, feedable in batches; the per-pair
diffs are in `l191_cfgmap.json`. Risk: skipping this turns step 5 into
silent content selection by whoever writes the patch.

**2. Pilot Earth — the constraint case.** Collapse the 6 verbatim
config pairs to derivation, express crust via `HOVER_PREFIX`, take the
Hill-sphere content ruling from step 1. Mode 5 on both surfaces:
tooltip unchanged to the eye, hover byte-identical for the 6, crust
hover identical, Hill per ruling. Risk: mesh3d shells are Earth's
rendering path — verify the hover actually displays from `hover_text`
for mesh geometry during the render check, since this survey verified
wiring statically only.

**3. Solar — the visible bug.** Convert the 19 strings to `\n`
(the five constant-interpolating forms need edits that preserve their
interpolations — patch scripts, fingerprinted, bottom-up per
safe-file-editing). Derive the 9 verbatim `_info_hover` twins from the
body and delete the authored duplicates; express gravitational
influence as tooltip-prefix + body; derive
`hover_text_sun_and_corona_tooltip` from its plot twin (strip bold,
convert breaks) or retire the dead plot twin — Tony's call; mark or
reconcile the 5 divergent pairs per step 1. Risk: the 15 `_info_hover`
names are referenced from `shell_configs.py:1891-2048` — deleting a
name without repointing its config reference is an immediate
`NameError` at import, which at least fails loudly.

**4. The loop bodies — mechanical sweep, 39 strings.** Exact inverse
conversion `<br>` → `\n` in the module literals; nothing else changes.
The 16 Saturn/Uranus/Neptune reference entries go live — run the
byte-compare gate. Jupiter, Planet 9, and Moon-Hill plot text is
untouched (independent inline copies remain until step 5). Risk is low
and measured: only `<br>` exists (no variants), and no affected string
mixes formats, so the conversion is unambiguous; the gate catches the
one thing that could still surprise.

**5. Migrate the remaining inline config entries to the reference
pattern** — L-181's lane — landing the step 1 content rulings family
by family, Mode 5 each. Risk: this is where a wrong authoritative-copy
choice becomes the rendered text; it is also where the near-identical
drift sextet (0.93-0.97) silently picks a winner if nobody diffs them
first. Diff first.

**6. Make the invariant enforce itself.** A check, wired into the
routine that already runs (the scanner pass or pre-push), asserting no
string live-bound to a Tkinter tooltip contains `<br` — resolving
bindings the way this survey did, printing how many strings it
resolved, and failing both on any unresolvable name and on the loop
fallback ever firing. Success carries evidence; the blind spot
announces; the check lives where it runs.

---

## Measured vs inferred, and open items

**Measured:** every count, name, line, format classification, pair
comparison, similarity ratio, dead-code determination, and date in
this document; the Earth crust constraint byte-for-byte; the
regression commit's existence and shape (`97bbfe3`, 2026-05-25,
touching the shell modules with `\n`→`<br>` line changes).

**Inferred:** that the loop bindings *render* (asserted from
module-level statements plus verified variable existence — no GUI was
executed; step 0's single hover settles it); the deliberate-vs-drift
classification of divergent pairs (except where dated content proves
one-sided update); the maintenance direction of the config copies.

**Open items — things this survey could not determine:**

1. **The ledger's 20th solar string.** 19 measured here; locating the
   delta needs the August 7 measurement's base SHA, which L-191 does
   not pin for that count.
2. **Custom-builder hover text vs `_info` agreement is unmeasured.**
   The live plot text for all `CUSTOM_SHELLS` (including Earth's
   magnetosphere/LEO/GEO and the 17 loop-body custom shells in the
   affected set) is function-local and multi-fragment; the tooltip
   side is measured, the builder side is not. This gap fails the
   completeness of part (d) for custom shells, and I am reporting it
   rather than estimating it.
3. **No runtime execution.** Static analysis only, per the
   survey-not-sweep ruling; liveness claims are AST-plus-existence
   claims until a render confirms.
4. **The per-module regression/restoration history is untraced.**
   `97bbfe3` touched modules that are clean today (Earth, Eris, the
   asteroid belt); whether those were converted and later restored, or
   their `_info` strings were never converted, was not established.
   It does not change the current-state scope the sweep plans against.

**Where I disagree with section 4 of the request:** nowhere on the
requirements, one place on the history it transmits — "the fix already
exists" (16 sites: confirmed exactly), the Earth constraint (confirmed
byte-for-byte), and the April 2025 design intent stand; but the L-191
material behind section 3's framing understates the symptom's spread,
and the item's "why only solar broke" explanation is contradicted by
measurement. Solar is where the bug was seen, not where it lives.
