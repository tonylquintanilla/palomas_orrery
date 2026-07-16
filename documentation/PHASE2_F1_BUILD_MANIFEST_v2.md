# F1 Build Manifest v2 -- Feature-Config Serving Pipeline (build contract)

**Type:** BUILD MANIFEST (executable contract; implementer: Claude Opus)
**Supersedes:** `PHASE2_F1_BUILD_MANIFEST_v1.md` (Claude Fable, Mode 7) and
`gpt_PHASE2_F1_BUILD_MANIFEST_v0.1.md` (GPT), reconciled into this v2 by
Claude Sonnet 5 after an independent comparative review
(`F1_MANIFEST_COMPARATIVE_REVIEW_v1.md`) and Tony's decision on the one
open disagreement (section 0). Fable's manifest is the structural base
(live-verified, and the source of the FLAG-2 bug fix below); GPT's
stop-condition/implementation-report rigor is grafted in (sections 9-10);
the M1 schema (section 4) is rewritten against the actual settled
convention, recovered from the session's own v0.1/v0.2 working files
(unreachable by either AI at build time).
**Built on:** orrery HEAD `58dfa5205d492711d6163560d8c3fa15f6c60b9c`, gallery
HEAD `953c650edc8dbd35ab11ec1720f8283987d63901` -- both re-verified live via
`git ls-remote` during the comparative review, not merely carried from v1.
Re-pin before building; a drifted HEAD means reconcile first.
**Design source:** `documentation/PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md`
(orrery repo, in-tree at the HEAD above; repo copy verified byte-identical to
the session upload, both by Fable and independently by Sonnet 5). Status
CONVERGED. This manifest implements it; it does not reopen it.
**Parent:** L-118 (F1). Companion: PHASE2_ARTIFACT1_AS_BUILT.md,
MASTER_PLAN_INTERACTIVE_GALLERY.md v13.
**Author's verification statement:** every file/line citation and numeric
value below was re-read from live HEAD by at least one of Fable (2026-07-16)
or Sonnet 5 (2026-07-16, independent re-check of the FLAG-2 arithmetic and
the section 4 schema sources), not carried from the handoff's word. Tags:
[verified @HEAD] = re-read live by Fable; [re-verified] = independently
re-checked against live source by Sonnet 5 during reconciliation; [pinned
here] = an implementation semantic this manifest defines; [per handoff] =
design decision carried from v0.4 as settled.

**Two independent units.** M1 (feature-config porting) and M2 (F1a
trust/served_window) are separate, independently buildable, in either
order. They share exactly one file (`tools/gallery_cache_builder.py`) in
disjoint regions; the one merge note is in section 3. Do not combine them
into a single change set for tidiness -- the split is deliberate scoping.

---

## 0. Flags -- resolution status after reconciliation

Six implementation-level semantics were pinned in Fable's original pass.
None reopens a settled design decision; each is a concrete rendering of a
direction the handoff states in prose. Two required a decision before this
manifest could ship; both are now resolved.

- **FLAG-1 (M1) -- RESOLVED, not by confirmation but by recovery.** Fable
  correctly flagged that handoff v0.4 SS4's "unchanged from v0.1" schema
  reference was unreachable -- v0.1-v0.3 are not in either repo or the
  upload set Fable had. Sonnet 5 had v0.1 and v0.2 in this session's own
  working files and recovered the actual settled decision (v0.2 Section 2,
  Tony's direct correction mid-round): field naming **mirrors the orrery's
  own dict shapes exactly** -- `atmosphere`/`upper_atmosphere` (not
  "lower"/"upper"), `inner_belt_distance`/`outer_belt_distance`/
  `belt_thickness` (no invented unit suffix), ring keys copied verbatim
  from each source's own `ring_params` dict (including the dict-of-slugs
  shape itself, e.g. `main_ring`/`halo_ring`/..., not a generic
  `components` list). Section 4.1 below is rewritten against this,
  re-verified directly against `shell_configs.py`, `earth_visualization_
  shells.py`, `jupiter_visualization_shells.py`, and `saturn_visualization_
  shells.py` at HEAD -- not against either draft manifest's guess. Neither
  Fable's nor GPT's proposed schema matched this exactly; see the
  comparative review for specifics if curious. This is settled now; Opus
  builds against section 4.1 as given.
- **FLAG-3 (M2) -- RESOLVED, Tony's direct call: agrees with Fable's
  stance.** If any non-moon, non-spacecraft object fails its trust
  measurement in a build, the global `served_window` is served as
  **null** (unenforced, with a warning), NOT computed from the survivors.
  GPT's alternative (compute the minimum from whichever objects
  succeeded, only fail the build if zero succeed) was considered and
  rejected: `resolver.py` already treats `served_window: null` as a
  supported, gracefully-warned state [re-verified, lines 91-106], while a
  wrong-but-present numeric bound is indistinguishable from a correct one
  to that same consumer -- a survivors-only minimum could silently under-
  or over-state the true bound with no visible sign anything degraded.
  Null-on-any-failure is the conservative, honest default and is now
  settled design, not an open flag. (Rationale in full: a minimum over an
  incomplete set is not conservative -- the missing object could have been
  the binding one.)
- **FLAG-2 (M2) -- CONFIRMED, independently re-verified: mean-motion GM
  correction, the real catch of this whole reconciliation.**
  `propagate_marker` derives mean motion as `n = K_GAUSS / a^1.5`
  (`gallery/assembler/render_orbits.py` line 87 [verified @HEAD]) --
  K_GAUSS is sqrt(GM_sun). For planetocentric elements (the four moons)
  this is wrong by ~3 orders of magnitude. Sonnet 5 re-derived this
  independently against a fresh clone rather than taking the figure on
  faith: `n_wrong = K_GAUSS / (0.00257 AU)^1.5 ~= 132 rad/day`, giving a
  ~68-minute period against the Moon's real 27.3-day sidereal month --
  confirms Fable's claim to within rounding [re-verified]. GPT's manifest
  does not address this anywhere and would have reused the same math
  unmodified for all four moon-category objects; every moon `trust` block
  built from GPT's manifest alone would have been silently wrong. The fix
  (section 5.3) captures Horizons' own mean-motion column into the served
  osculating block (additive field) and uses it in the measurement;
  `render_orbits.py` is NOT modified.
- **FLAG-4 (M2): global window placement.** `served_window` =
  `[as_of_jd - W_min, as_of_jd + W_min]`, symmetric about the build
  epoch, W_min = minimum `window_days` over participants. Two-body drift
  grows in both time directions; the date picker serves past dates too.
  Documented artifact: a comet's window is measured at its Tp anchor
  (possibly decades from tonight), yet its scalar `window_days` still
  participates in the minimum per the pinned SS6.4 rule (Tony's direct
  call: only `category == "moon"` is excluded). A comet can therefore
  clamp today's global window even though its own validity is centered
  elsewhere -- known F1a coarseness, fixed properly by F1b's per-object
  enforcement. Stated here so nobody rediscovers it as a bug.
- **FLAG-5 (M2): cap table.** SS6.6 gives directions ("outer cap for
  planets, not a floor; satellites ~P/8 if anything; comets bound to
  current apparition"); this manifest pins them as: cap = P for
  planet/dwarf_planet/asteroid; P/8 for moon; P/2 for comet (window
  centered on the Tp-anchored epoch never reaches the adjacent
  apparition's aphelion). Caps bound `window_days` from above; the
  measured rate can only shrink the window below the cap, never grow it.
- **FLAG-6 (M2): zero-rate handling.** If the measured error rate is 0
  (or below 1e-12 deg/day), `window_days` = the category cap, with
  `cap_applied` recorded. Physical meaning: no measurable drift within
  Delta, so the cap alone binds. This also makes Layer 1 deterministic:
  the offline suite's `fake_vectors` are Kepler-perfect
  (test_gallery_cache_builder_offline.py lines 47-57 [verified @HEAD]),
  so mocked measurements yield rate ~ 0 and the asserted windows are
  exactly the caps -- and it removes the divide-by-zero.

---

## 1. Scope boundaries (from the manifest prompt; restated as contract)

Out of scope this pass -- Opus must not touch these even if adjacent:

- `gallery/assembler/resolver.py` and `gallery/assembler/cache_reader.py`:
  ZERO edits. The new `trust` blocks and the populated `served_window`
  are additive data / an existing consumed field. F1b (resolver consumes
  per-object trust; deliberate golden-fingerprint reopen) is a separate
  scheduled item.
- `gallery/assembler/render_orbits.py`: ZERO edits (import from it; see
  FLAG-2 and section 5.3).
- Uncertainty-envelope UX (SS6.5): no client-side rendering work. Mode 5;
  Tony confirms against a render later.
- Apophis close-encounter anchoring (SS6.6 sharpened direction): not
  built. Apophis still gets a normal trust measurement as an
  `asteroid`-category participant -- the encounter anchor is about WHERE
  its elements are epoched, which stays as-is this pass.
- L-119 (`event_link`, builder line 727) and L-123 (info card): same
  file, later items. Leave line 727's `None` alone.
- Sun-oriented feature category (magnetosphere envelopes, comae/tails):
  not this pass; ledger item to be logged (section 8).

House rules binding on the build: ASCII-only, LF endings, no Unicode in
source; credit line added to each touched module's docstring ("Module
updated: [date] with Anthropic's Claude Opus 4.8" or current model);
`# Source:` comments only over genuinely fetched/ported values
(source-then-cite, never cite-to-clear); provenance scanner Tier-1 = 0
before push; bottom-up edits if patching by line.

---

## 2. Verified baseline (what the code says at HEAD, re-read this session)

Gallery repo `953c650e`, `tools/gallery_cache_builder.py`:
- Lines 749-750: `feature_configs.json` written as
  `{'schema_version': SCHEMA_VERSION, 'features': {}}` unconditionally.
- Line 739: `'served_window': None` at coverage_index top level.
- Line 727: `'event_link': None` (out of scope, do not touch).
- Line 374: `def resolve_comet_conic(obj, warn)` -- elements epoched at
  solved Tp.
- Line 177: `fetch_vectors_range(...)`; line 204: `fetch_elements(...)`
  returning keys `a,e,i,omega,Omega,TP,MA,TA,epoch_jd` -- note: does NOT
  capture Horizons' mean-motion column today.
- Line 61: `SCHEMA_VERSION = "1.0"`.
- Served coverage_index per-object `osculating` block already carries
  `a_au, e, i_deg, node_deg, peri_deg, M0_deg, epoch_jd, center, source`
  -- i.e. exactly `propagate_marker`'s input dialect. No key-mapping
  adapter is needed; the measurement's input is data already in staging.
  Voyager 1's `osculating` is `null` (spacecraft are structurally outside
  the propagation-trust question).

`data/objects_config.json` [verified @HEAD]:
- `features` today: flat lists. Earth line 17
  `["van_allen_belts", "atmosphere_shell"]`; Jupiter line 24
  `["magnetosphere", "ring_system"]`; Saturn line 31 `["ring_system"]`;
  all others `[]`; **halley/encke have no `features` key at all**.
- Category audit (all 12): earth/jupiter/saturn = planet;
  moon/io/titan/charon = moon; pluto = dwarf_planet; apophis = asteroid;
  halley/encke = comet; voyager_1 = spacecraft. Matches handoff SS1.
- Halley `overrides.comet.anchor: "Tp"` at lines 103-105.

`gallery/assembler/` [verified @HEAD]:
- resolver.py 91-106: served_window consumer -- null -> warning;
  populated -> `OutOfServedWindowError` outside `[start_jd, end_jd]`.
- cache_reader.py 40-41: `served_window()` accessor returns the raw field.
- render_orbits.py 44 `solve_kepler`, 84 `propagate_marker`, 39
  `K_GAUSS` (solar), 87 the solar-GM mean-motion derivation (FLAG-2).

Offline suite `tools/test_gallery_cache_builder_offline.py`
[verified @HEAD]: `ELEMS` mock dict (line 22), `fake_elements` (31),
`fake_vectors` (47, Kepler-perfect), `fake_solution_tp` (63); count
assertion `len(objs) == 12` (line 108); `'served_window' in idx` (110).
No assertion pins `features` to `{}` -- M1 will not break an existing
check, but adds new ones.

Orrery repo `58dfa520` -- SS3 source values, ALL re-read live this
session; see the tables in section 4.2. Source locations:
`shell_configs.py` lines 1423 (Earth `atmosphere`), 1446
(`upper_atmosphere`), 2258 (CUSTOM_SHELLS Earth `magnetosphere` block);
`earth_visualization_shells.py` line 650
(`create_earth_magnetosphere_shell`), params at 670-672, belt loop
779-822 (z-ripple: `z_scale = 0.2 * belt_radius`, `z = z_scale *
sin(2*angle)`, line 818-819); `jupiter_visualization_shells.py` line 704
(`create_jupiter_radiation_belts`, distances `[1.5, 3.0, 6.0]` R_J,
thickness `0.5` R_J), line 882 (`create_jupiter_ring_system`);
`saturn_visualization_shells.py` line 1026 (`create_saturn_ring_system`).

---

## 3. The one shared file -- merge note

Both units edit `tools/gallery_cache_builder.py`, in disjoint regions:

- M1 touches: `derive_served`'s feature assembly (the lines 749-750
  writer) and adds feature-shape validation.
- M2 touches: `derive_served`'s top-level `served_window` (line 739) and
  per-object entry assembly (additive `trust` key), plus new measurement
  functions (new code, placed near the other fetch helpers) and one
  additive column capture in `fetch_elements`.

Build in either order; whichever lands second rebases trivially. If both
are built in one session, still deliver as two separately reviewable
change sets.

---

## 4. UNIT M1 -- Feature-config porting (handoff SS3-SS5)

### 4.1 Target schema for `objects_config.json` `features` [RESOLVED -- FLAG-1, recovered v0.2 convention, re-verified against live source]

`features` changes from a flat list to a dict: feature-key -> feature
config. Unlike v1's generic `kind`/`components` abstraction (which was a
reasonable guess but not what was actually decided), the settled
convention -- Tony's direct correction earlier in this design round,
recovered from the session's own v0.2 working file -- is to **mirror the
orrery's own source dict shapes exactly**, not introduce a new abstraction
layer:

- Where the source itself has sibling config keys (Earth's `atmosphere` /
  `upper_atmosphere` in `SHELL_CONFIGS['Earth']`), the served feature uses
  those same sibling keys, not "lower"/"upper" or a `layers` list.
- Where the source itself names belt-distance fields
  (`inner_belt_distance`, `outer_belt_distance`, `belt_thickness` in
  `create_earth_magnetosphere_shell`'s own `params` dict), those exact
  names are used -- no invented unit suffix (`_re`, `_rp`); units are
  Earth/parent-body radii, stated in prose, not encoded in the field name.
- Where the source itself is a dict-of-ring-slugs (`ring_params` in
  `create_jupiter_ring_system` / `create_saturn_ring_system`), the served
  feature is that same dict-of-slugs (`main_ring`, `halo_ring`, ... /
  `d_ring`, `c_ring`, ...) with the source's own `inner_radius_km`,
  `outer_radius_km`, `thickness_km` field names -- not a generic
  `components` list with a `name` field.
- Jupiter's `radiation_belts` is a genuinely different shape from Earth's
  belts in the SOURCE (a 3-element `belt_distances` list + one shared
  `belt_thickness`, not an inner/outer pair) -- `create_jupiter_radiation_
  belts`'s own local variable names. The served feature mirrors that
  shape rather than forcing parity with Earth's.

No silent unit conversion happens in the builder -- values are served
exactly as the source holds them; the JS layer has each body's radius and
does the scaling.

### 4.2 The three config edits -- exact content

All values below [re-verified against live HEAD during reconciliation,
cross-checked line-by-line against `shell_configs.py`, `earth_
visualization_shells.py`, `jupiter_visualization_shells.py`, and
`saturn_visualization_shells.py`]. Colors are served as CSS
`rgb(r, g, b)` strings exactly as the source holds them.

**Earth** (replaces line 17's list):

```json
"features": {
  "atmosphere_shell": {
    "atmosphere": {
      "name": "Lower Atmosphere", "radius_fraction": 1.05,
      "color": "rgb(150, 200, 255)", "opacity": 0.5, "n_points": 20
    },
    "upper_atmosphere": {
      "name": "Upper Atmosphere", "radius_fraction": 1.25,
      "color": "rgb(100, 150, 255)", "opacity": 0.3, "n_points": 20
    }
  },
  "van_allen_belts": {
    "inner_belt_distance": 1.5,
    "outer_belt_distance": 4.5,
    "belt_thickness": 0.5,
    "n_rings": 5,
    "n_points": 80,
    "colors": ["rgb(255, 100, 100)", "rgb(100, 200, 255)"],
    "names": ["Inner Radiation Belt", "Outer Radiation Belt"]
  }
}
```

(Distances/thickness are in Earth radii, per the source's own comment --
noted here in prose, not encoded as a field-name suffix, per the settled
convention. Belt geometry ripple -- `z = 0.2 * belt_radius * sin(2 *
angle)`, thinner near poles -- is renderer behavior, not a served value;
not part of this schema.)

**Jupiter** (replaces line 24's list; settled feature swap unchanged --
`magnetosphere` dropped, `radiation_belts` replaces it):

```json
"features": {
  "ring_system": {
    "main_ring": { "inner_radius_km": 122500, "outer_radius_km": 129000, "thickness_km": 30 },
    "halo_ring": { "inner_radius_km": 100000, "outer_radius_km": 122500, "thickness_km": 12500 },
    "amalthea_gossamer": { "inner_radius_km": 129000, "outer_radius_km": 182000, "thickness_km": 2000 },
    "thebe_gossamer": { "inner_radius_km": 129000, "outer_radius_km": 226000, "thickness_km": 8600 }
  },
  "radiation_belts": {
    "belt_distances": [1.5, 3.0, 6.0],
    "belt_thickness": 0.5,
    "n_rings": 5,
    "n_points": 80
  }
}
```

(Ring dict keys -- `main_ring`, `halo_ring`, `amalthea_gossamer`,
`thebe_gossamer` -- are `create_jupiter_ring_system`'s own `ring_params`
keys, verbatim [re-verified, lines 898-935]. `radiation_belts` distances/
thickness are in Jupiter radii. Ring and belt colors exist in the source
(`ring_params[...]['color']`, per-belt colors in `create_jupiter_
radiation_belts`) but are NOT part of the settled porting table -- the
handoff's SS3 cites only geometry (distances/thickness/counts) for
Jupiter's rings and belts, unlike Earth's belts where colors ARE cited.
Do not add colors here; that would be an uncited addition beyond what was
actually ported. If color parity with Earth's belts is wanted, that is a
new decision for Tony, not an implementation default.)

**Saturn** (replaces line 31's list):

```json
"features": {
  "ring_system": {
    "d_ring": { "inner_radius_km": 66900,  "outer_radius_km": 74500 },
    "c_ring": { "inner_radius_km": 74658,  "outer_radius_km": 92000 },
    "b_ring": { "inner_radius_km": 92000,  "outer_radius_km": 117500 },
    "a_ring": { "inner_radius_km": 122340, "outer_radius_km": 136800 },
    "f_ring": { "inner_radius_km": 140210, "outer_radius_km": 140420 },
    "g_ring": { "inner_radius_km": 166000, "outer_radius_km": 175000 },
    "e_ring": { "inner_radius_km": 180000, "outer_radius_km": 480000 }
  }
}
```

(Ring dict keys are `create_saturn_ring_system`'s own `ring_params` keys,
verbatim [re-verified, lines 1040+]. The source dict also carries a
`thickness_km` per ring (e.g. D ring: 10 km) and color/opacity/description
fields, none of which are in the handoff's SS3 porting table -- same
not-cited-so-not-ported rule as Jupiter above.)

**Halley and Encke**: add `"features": {}` to each object entry (schema
completeness; no coma/tail params ported -- that is the deferred
sun-oriented category).

**All other objects** (moon, io, titan, pluto, charon, apophis,
voyager_1): flat `[]` becomes `{}`. The migration is total: after M1, no
`features` field anywhere in the config is a list.

### 4.3 `derive_served` feature assembly (replaces the lines 749-750 writer)

- Per object: `feats = obj.get('features', {})`. If a list survives
  (stale config), raise `ValidationAbort` naming the object -- the
  list->dict migration is atomic with this code change; a mixed state is
  a config error, not something to paper over. [Consistent with the
  builder's ABORT-on-structural-invariant stance.]
- Assemble `feature_configs.json` as
  `{"schema_version": SCHEMA_VERSION, "features": {slug: feats for all 12 objects}}`
  -- ALL slugs present, empty dicts included, so "did the port run" is
  visible by inspection and the file's key set matches the catalog.
- Structural validation additions (ABORT disposition, alongside the
  existing invariants): every ring-shaped sub-entry (any dict whose value
  has `inner_radius_km`/`outer_radius_km`) satisfies
  `inner_radius_km < outer_radius_km`; every shell-shaped sub-entry (any
  dict with `radius_fraction`) has `radius_fraction > 1.0`; belt-shaped
  entries (`inner_belt_distance`/`outer_belt_distance`/`belt_thickness` or
  `belt_distances`/`belt_thickness`) have positive values in ascending
  order where a pair exists; colors, where present, match
  `rgb(int, int, int)`. Validate structurally by field presence, not by a
  `kind` tag -- section 4.1's schema has no `kind` field; each feature's
  shape is recognized from which fields it carries. Cheap, and catches a
  mistyped port at build time instead of at render time.
- The per-object coverage_index entries already pass `features` through
  (earth's served entry shows the list today [verified @HEAD]); after
  M1 they carry the dict. That is additive-shape change to a field the
  resolver does not consume [per handoff]; no resolver work.

### 4.4 M1 Layer-1 test updates

- Assert `feature_configs.json` has all 12 slugs; earth/jupiter/saturn
  non-empty; earth's `van_allen_belts.inner_belt_distance == 1.5`; earth's
  `atmosphere_shell` has both `atmosphere` and `upper_atmosphere` keys;
  jupiter has `radiation_belts` and NOT `magnetosphere`, and its
  `ring_system` has all four ring slugs (`main_ring`, `halo_ring`,
  `amalthea_gossamer`, `thebe_gossamer`); saturn's `ring_system` has all
  seven ring slugs; halley/encke present with `{}`.
- The count assertion (line 108, `== 12`) is UNCHANGED -- no new objects.
- Existing check line 110 (`'served_window' in idx`) unaffected by M1.

### 4.5 M1 acceptance gate

1. Layer 1 from a CLEAN checkout (the canary for path assumptions).
2. `--dry-run --object earth`, `--object jupiter`, `--object saturn`
   against real Horizons.
3. A real `--first-build` or `--nightly`; inspect the swapped
   `feature_configs.json`.
4. JS feature-layer smoke against Earth's golden artifact BEFORE
   trusting Jupiter/Saturn's render [per handoff Gap list]. This is
   Tony's Mode 5 gate; the render beats all claims.

---

## 5. UNIT M2 -- F1a trust measurement + served_window (handoff SS6)

### 5.1 What gets built

New builder-side measurement code + `derive_served` additions. Zero
changes to resolver/cache_reader/render_orbits. The golden fingerprint
stays closed: everything M2 serves is either additive (per-object
`trust`) or an already-consumed field getting populated (`served_window`).

### 5.2 The measurement, per non-spacecraft object [per handoff SS6.1-6.3; mechanics pinned here]

Inputs: the object's staged `osculating` block (already fetched and
normalized this build) and its config identity (horizons_id, id_type,
stored/canonical center).

1. **Delta**: `Delta = min(P / 8, 30.0)` days, where P is the orbital
   period from the object's own mean motion (section 5.3):
   `P = 360.0 / n_deg_per_day`. (Earth ~30 d; Moon ~3.4 d; Io ~5.3 h --
   Horizons accepts sub-day epochs; Halley/Encke 30 d.)
2. **Check vectors**: fetch the object's true position at
   `epoch_jd + Delta` and `epoch_jd - Delta`, same Horizons target and
   same center as the raw fetch (reuse the existing fetch layer -- an
   epoch-list call or two single-epoch calls, implementer's choice; it
   MUST route through the same injectable fetch symbols the offline
   suite mocks). Note the anchor: measurement is at the ELEMENT epoch,
   not "tonight" -- for planets/moons those coincide; for Tp-anchored
   comets the measurement brackets perihelion, which is the fast-motion
   worst case and therefore conservative by construction.
3. **Propagate**: two-body position at both epochs from the osculating
   block, via imported `solve_kepler` + the orientation math (section
   5.3's wrapper).
4. **Angular error**: at each epoch, theta = the angle between the
   propagated and fetched position vectors as seen from the object's
   canonical center (`atan2(|r1 x r2|, r1 . r2)`, in degrees). This is
   the render-relevant error for a camera near the center.
5. **Rate**: `error_rate = max(theta_plus, theta_minus) / Delta`
   [deg/day] -- the worse of the two samples [per handoff].
6. **Window**: `window_days = tolerance_deg / (guard_k * error_rate)`
   with `tolerance_deg = 0.5` (adopted estimate, to be visually checked
   once Wave 1 renders -- do not re-derive) and `guard_k = 2.0`
   [per handoff]. If `error_rate < 1e-12`, `window_days = cap`
   (FLAG-6).
7. **Cap** (FLAG-5): `window_days = min(window_days, cap)` where cap =
   P for planet/dwarf_planet/asteroid, P/8 for moon, P/2 for comet.
   Record `cap_applied` when the cap binds, else null.

Failure disposition: any Horizons failure or physics guard trip (e >=
1.0, missing mean motion for a planetocentric object) -> WARN, serve
`trust` with `"window_days": null` and an `"error"` string, and never
abort the build. A check-vector hiccup must not kill the nightly. The
knock-on for the global window is FLAG-3.

### 5.3 Mean motion: the GM correction (FLAG-2) [pinned here]

- `fetch_elements` gains one optional column capture:
  `n_val = get_col(['n', 'N'], required=False)` -- Horizons' osculating
  mean motion (deg/day) -- returned as `'n'` in the dict. Additive,
  backward-compatible.
- `derive_served`'s osculating-block assembly adds `n_deg_per_day` when
  available (additive field; the resolver ignores unknown fields
  [per handoff], and cache_reader reads schema_version permissively
  [verified @HEAD]).
- The measurement's propagation is a small builder-side wrapper:
  `mean_anom = radians(M0_deg + n_deg_per_day * (t - epoch_jd))`, then
  imported `solve_kepler`, then the imported orientation transform from
  render_orbits (its element-to-XYZ function), producing center-relative
  XYZ in AU. `propagate_marker` itself is NOT called for moons and NOT
  modified for anyone -- its solar-GM assumption stays correct for its
  own (heliocentric marker) job.
- Fallback when `n` is absent: heliocentric objects may fall back to the
  K_GAUSS derivation (identical to today's behavior); planetocentric
  objects must NOT (that is the 3-orders-of-magnitude trap) -- they take
  the WARN/null path instead.
- Provenance: the wrapper carries a `# Source:` comment pointing at
  render_orbits.py's `propagate_marker` (the adapted math) per the
  builder's provenance-copy convention.

### 5.4 The served `trust` block [schema pinned here -- this IS the manifest-level definition]

Added per non-spacecraft object in coverage_index (additive key,
sibling of `osculating`):

```json
"trust": {
  "schema_version": 1,
  "method": "two_body_rate_v1",
  "element_epoch_jd": 2461232.5,
  "delta_days": 30.0,
  "samples": [
    { "offset_days":  30.0, "error_deg": 0.0031 },
    { "offset_days": -30.0, "error_deg": 0.0027 }
  ],
  "error_rate_deg_per_day": 0.000103,
  "tolerance_deg": 0.5,
  "guard_k": 2.0,
  "window_days": 2427.2,
  "cap_applied": null,
  "window": { "start_jd": 2458805.3, "end_jd": 2463659.7 }
}
```

(`window` = element_epoch +/- capped window_days -- the per-object truth
F1b will enforce. On measurement failure: `window_days`, `window`,
`error_rate_deg_per_day` null; add `"error": "<reason>"`. Values above
are illustrative shape, not targets.)

Spacecraft (voyager_1): `"trust": { "schema_version": 1, "method":
"fetched_positions", "window": null }` -- explicitly not-applicable
rather than absent, so absence always means "older generation".

### 5.5 Global `served_window` (replaces line 739's None) [per handoff SS6.4; placement pinned, FLAG-3/4]

- Participants: every object with `category not in {"moon", "spacecraft"}`
  -- operationally, moons are excluded by the pinned rule and spacecraft
  produce no propagation window at all. That is: earth, jupiter, saturn,
  pluto, apophis, halley, encke (7 of 12).
- All 7 measured successfully -> `W_min = min(window_days)` over them ->
  `"served_window": { "start_jd": as_of_jd - W_min, "end_jd": as_of_jd + W_min }`
  where `as_of_jd` is the build's generation epoch.
- Any participant null -> `"served_window": null` + warning naming the
  missing objects (FLAG-3).
- Moons still get accurate `trust` blocks served but do not bind the
  global window -- the accepted, known F1a gap, closed by F1b
  [per handoff, Tony's direct call].

### 5.6 M2 Layer-1 test updates

- Route the check-vector fetch through the mocked fetch symbols; the
  existing `fake_vectors` is Kepler-consistent with `ELEMS`, so mocked
  error rates are ~0 and every mocked `window_days` equals its category
  cap deterministically (FLAG-6). Assert exactly that: earth's window ==
  its period cap; moon's == P/8; halley's == P/2 (within float
  tolerance).
- Add a mocked `n` column to `fake_elements`' returned dict consistent
  with each ELEMS entry's `a` (n = K_GAUSS-derived for heliocentric
  mocks is fine -- the mocks are heliocentric-shaped; what matters is the
  code path reads `n_deg_per_day` from the block).
- Assert: every non-spacecraft object serves a `trust` block with
  `method == "two_body_rate_v1"` and finite `window_days`; voyager_1
  serves `method == "fetched_positions"`; top-level `served_window` is
  non-null with `start_jd < as_of_jd < end_jd`; and the existing line
  108 count (12) and line 110 presence checks still pass.
- One failure-path test: force one participant's check-vector mock to
  raise -> assert that object's trust carries `error` and the global
  `served_window` is null with a warning recorded (FLAG-3 exercised, not
  just stated).

### 5.7 M2 acceptance gate

1. Layer 1 from a CLEAN checkout.
2. `--dry-run --object <slug>` for one of each category in scope (earth,
   moon, pluto, apophis, halley) -- eyeball the per-object trust lines
   and the measured rates for physical plausibility (planet rates tiny;
   Moon's rate visibly larger; comet rates largest).
3. Real `--first-build`/`--nightly`; inspect swapped coverage_index:
   `served_window` populated, 11 measured trust blocks + voyager's
   `fetched_positions`.
4. Resolver behavior check via the dev render page date picker
   (PHASE2_ARTIFACT1_AS_BUILT.md SS7): a date inside the window renders;
   a date far outside raises `OutOfServedWindowError` -- exercising the
   EXISTING consumer against the newly populated field, zero resolver
   changes. [Layer-2 manual, Tony's gate.]
5. Fetch-cost note for the nightly: +2 vector fetches x 11 objects = 22
   extra Horizons calls per build. Acceptable; if Horizons throttling
   ever bites, batching both epochs into one epoch-list call per object
   is the sanctioned optimization.

---

## 6. What "done" means (both units)

- Layer 1 green from a clean checkout; Layer 2 dry-runs + a real build
  through the atomic swap; the swap's blast-radius rules untouched
  (nothing new lives inside `data/solar-system/` except served output;
  the config stays the sibling input).
- Guard v2 stance unchanged: trust measurement failures are WARN-class;
  the new structural checks (feature shape) are ABORT-class -- matching
  the existing two-disposition doctrine.
- Provenance scanner Tier-1 = 0; every ported value carries its
  `# Source:` back to the orrery file:line listed in section 2.
- Tony's render gate: Earth golden-artifact feature smoke (M1) and the
  date-picker window check (M2). The render beats all claims.

## 7. Deliverables checklist (Opus)

- [ ] `data/objects_config.json`: 12-object features migration (section
      4.2, schema resolved -- build against it directly).
- [ ] `tools/gallery_cache_builder.py`: derive_served feature assembly +
      shape validation (M1); `fetch_elements` `n` capture, measurement
      functions, trust emission, served_window population (M2).
- [ ] `tools/test_gallery_cache_builder_offline.py`: sections 4.4 + 5.6.
- [ ] Module docstring credit lines on both touched files.
- [ ] Handoff for the build session: built on the SHAs above; pushed-at
      SHA; verified-vs-claimed split; any deviation from this manifest
      flagged, not silently resolved (manifest/handoff disagreement is a
      flag to raise [per ledger skill]).

## 8. Ledger follow-ups (Tony, post-build -- from the handoff's Gap list)

New items to log (next free L-handles; one-line suggested bodies):
- Sun-oriented feature category (magnetosphere envelopes/bow shocks,
  sodium tail, comae/tails) -- needed, deferred, no schema yet.
- F1b: resolver/cache_reader consume per-object `trust`; deliberate
  golden-fingerprint reopen; supersedes the F1a global interim rule.
- Close-encounter anchor mechanism (`overrides.asteroid.anchor` at
  encounter epoch, generalizing `resolve_comet_conic`) -- flagged,
  unscheduled, relevant when Apophis enters scope.
- Post-render: visual sanity check of the 0.5 deg tolerance (Wave 1
  Earth envelope render); per-view tolerance differentiation when there
  is a basis.
- Field-note candidate for the gallery-cache-builder skill after the
  build lands: the n_deg_per_day addition and the planetocentric GM trap
  (FLAG-2) belong in the skill's fetch-facts section.

---

## 9. Stop conditions (grafted from GPT's v0.1 pass -- genuine process
improvement, no conflict with sections 0-8)

Stop rather than improvise when any of these occurs: a pinned SHA cannot
be checked out; a load-bearing source value differs at re-verification
from what section 2 or 4.2 states; the current resolver does not
actually tolerate additive fields (re-check `resolver.py`'s unrecognized-
field warning path before relying on it); reusing `solve_kepler`/the
orientation math from `render_orbits.py` requires a behavior-changing
refactor (it should not -- both are pure functions); the artifact schema
cannot carry additive `trust` without a version bump decision (if it
looks like it needs one, stop and ask rather than bumping unreviewed);
real Horizons data produces a structurally impossible or non-finite
result the failure-disposition rules in section 5.2 don't cover; or the
golden fingerprint changes outside output F1 intentionally modified.

A stop report should identify the smallest blocking question and
preserve all completed, independently valid work (M1 and M2 are
separately committable -- a stop on one does not block delivering the
other). Do not broaden a stop into a request to redesign.

## 10. Required implementation report (grafted from GPT's v0.1 pass)

Deliver a short implementation report beside the code changes, covering:

```text
Pinned SHAs and clean-worktree proof
Files changed per unit (M1, M2)
Any deviation from this manifest, and why (flag, don't silently resolve)
Commands run and results (Layer 1, dry-run, real build)
Generated artifact excerpts (feature_configs.json, coverage_index.json
  trust blocks)
Per-object trust summary table: object key, category, epoch, sample
  offsets, sample errors, measured rate, guarded rate, cap basis, final
  window, whether eligible to control the global window
Global controlling object and final served_window
Network/cache behavior observed (fetch count, any throttling)
Known warnings (measurement failures, null served_window if triggered)
Explicit confirmation of untouched out-of-scope files (resolver.py,
  cache_reader.py, render_orbits.py -- zero edits)
Commit SHAs for the M1 and M2 change sets
```

This report is what lets another model or a human reviewer reproduce and
verify the result without relying on conversation memory -- the same
principle behind every handoff in this project.

---

## Ref

`documentation/PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md` @
orrery 58dfa520 (design source); `FABLE_MANIFEST_PROMPT_F1_v0.2.md`
(the ask); `PHASE2_F1_BUILD_MANIFEST_v1.md` (Fable, structural base of
this v2); `gpt_PHASE2_F1_BUILD_MANIFEST_v0.1.md` (GPT, source of sections
9-10); `F1_MANIFEST_COMPARATIVE_REVIEW_v1.md` (the reconciliation
review); L-118 (parent); PHASE2_ASSEMBLER_BUILD_MANIFEST_v1.md (house
manifest precedent); gallery `953c650e` / orrery `58dfa520` (every
citation re-verified live during reconciliation).

---
v1 written July 2026 with Anthropic's Claude Fable 5 (Mode 7 collegial
relay; independent verification pass against both HEADs). v0.1 (GPT)
written the same round via ChatGPT, requested as a second independent
build contract from the same converged design. v2 (this document)
reconciles both plus Tony's decision on FLAG-3, written with Anthropic's
Claude Sonnet 5 -- structural base from Fable's v1, schema in section 4.1
recovered from this session's own v0.1/v0.2 working files and re-verified
against live source, sections 9-10 grafted from GPT's v0.1.
