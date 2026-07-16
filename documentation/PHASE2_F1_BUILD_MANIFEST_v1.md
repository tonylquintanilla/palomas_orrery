# F1 Build Manifest v1 -- Feature-Config Serving Pipeline (build contract)

**Type:** BUILD MANIFEST (executable contract; implementer: Claude Opus)
**Built on:** orrery HEAD `58dfa5205d492711d6163560d8c3fa15f6c60b9c`, gallery
HEAD `953c650edc8dbd35ab11ec1720f8283987d63901` -- both re-pinned live this
session via `git ls-remote`. Re-pin before building; a drifted HEAD means
reconcile first.
**Design source:** `documentation/PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md`
(orrery repo, in-tree at the HEAD above; repo copy verified byte-identical to
the session upload). Status CONVERGED. This manifest implements it; it does
not reopen it.
**Parent:** L-118 (F1). Companion: PHASE2_ARTIFACT1_AS_BUILT.md,
MASTER_PLAN_INTERACTIVE_GALLERY.md v13.
**Author's verification statement:** every file/line citation and every
numeric value in this manifest was re-read from live HEAD this session
(Fable, 2026-07-16), not carried from the handoff's word. Tags:
[verified @HEAD] = re-read this session; [pinned here] = an implementation
semantic this manifest defines (flagged in section 0); [per handoff] =
design decision carried from v0.4 as settled.

**Two independent units.** M1 (feature-config porting) and M2 (F1a
trust/served_window) are separate, independently buildable, in either
order. They share exactly one file (`tools/gallery_cache_builder.py`) in
disjoint regions; the one merge note is in section 3. Do not combine them
into a single change set for tidiness -- the split is deliberate scoping.

---

## 0. Flags for Tony -- read before relaying to Opus

Six implementation-level semantics were pinned while writing this contract.
None reopens a settled design decision; each is a concrete rendering of a
direction the handoff states in prose. They are flagged because the
protocol says pin-and-flag beats silently deciding. Confirm or redirect;
everything else in this manifest is transcription of settled design plus
verified code fact.

- **FLAG-1 (M1, blocking for M1 only): the feature-config JSON schema is
  proposed here, not transcribed.** Handoff v0.4 SS4 says "unchanged from
  v0.1" without reproducing it, and v0.1-v0.3 are not in either repo or
  the upload set -- the settled shape is unreachable from this session.
  Section 4.1's schema is constructed strictly from SS3's tables, SS5's
  `obj.get('features', {})` contract, and the config's existing idiom
  (the `overrides.comet` block). **Check it against v0.1 SS4 (or your
  memory of it) before Opus builds M1.** If it matches, strike this flag.
  If it differs, the v0.1 shape wins -- edit section 4.1, not the design.
- **FLAG-2 (M2): mean-motion GM correction, discovered this pass.**
  `propagate_marker` derives mean motion as `n = K_GAUSS / a^1.5`
  (`gallery/assembler/render_orbits.py` line 87 [verified @HEAD]) --
  K_GAUSS is sqrt(GM_sun). For planetocentric elements (the four moons)
  this is wrong by ~3 orders of magnitude (Moon: ~68-minute period
  instead of 27.3 days). The fix (section 5.3) captures Horizons' own
  mean-motion column into the served osculating block (additive field)
  and uses it in the measurement; `render_orbits.py` is NOT modified.
  This is a missing-consideration catch of exactly the kind the relay
  exists for -- without it, every moon's measured "error rate" would be
  garbage and the moon trust blocks (served, per SS6.4) would be wrong.
- **FLAG-3 (M2): missing-participant semantics.** If any non-moon,
  non-spacecraft object fails its trust measurement in a build, the
  global `served_window` is served as **null** (unenforced, with a
  warning), not computed from the survivors. Rationale: a minimum over
  an incomplete set is not conservative -- the missing object could be
  the binding one. The resolver already handles null gracefully with its
  own warning (resolver.py lines 94-98 [verified @HEAD]).
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

### 4.1 Target schema for `objects_config.json` `features` [pinned here -- FLAG-1]

`features` changes from a flat list to a dict: feature-key -> feature
config. Every feature config has:

- `kind`: one of `"sphere_shells"`, `"belt_rings"`, `"flat_rings"` --
  tells the JS layer which renderer to use.
- `components`: ordered list; each component is one drawable element.
- `params` (optional): shared parameters across the feature's components.

Units are explicit in field names, never implied: `radius_fraction`
(dimensionless, x body radius), `*_km` (kilometers), `*_rp` (planet
radii of the parent body). The JS layer already has each body's radius;
it does the scaling. No silent unit conversion happens in the builder --
values are served exactly as ported.

### 4.2 The three config edits -- exact content

All values below [verified @HEAD] against the orrery sources cited in
section 2. Colors are served as CSS `rgb(r, g, b)` strings exactly as the
source holds them.

**Earth** (replaces line 17's list):

```json
"features": {
  "atmosphere_shell": {
    "kind": "sphere_shells",
    "components": [
      { "name": "Lower Atmosphere", "radius_fraction": 1.05,
        "color": "rgb(150, 200, 255)", "opacity": 0.5, "n_points": 20 },
      { "name": "Upper Atmosphere", "radius_fraction": 1.25,
        "color": "rgb(100, 150, 255)", "opacity": 0.3, "n_points": 20 }
    ]
  },
  "van_allen_belts": {
    "kind": "belt_rings",
    "components": [
      { "name": "Inner Radiation Belt", "distance_rp": 1.5,
        "color": "rgb(255, 100, 100)" },
      { "name": "Outer Radiation Belt", "distance_rp": 4.5,
        "color": "rgb(100, 200, 255)" }
    ],
    "params": {
      "thickness_rp": 0.5, "n_rings": 5, "n_points": 80,
      "z_ripple": { "scale": 0.2, "harmonic": 2 }
    }
  }
}
```

(`z_ripple`: the source's `z = 0.2 * belt_radius * sin(2 * angle)` --
scale is the 0.2 multiplier on belt radius, harmonic the 2 inside the
sine. Belts are rendered around the parent's rotational axis; thinner
near poles, per the source comment.)

**Jupiter** (replaces line 24's list; note the settled feature swap --
`magnetosphere` is dropped, `radiation_belts` replaces it):

```json
"features": {
  "ring_system": {
    "kind": "flat_rings",
    "components": [
      { "name": "Main Ring", "inner_radius_km": 122500,
        "outer_radius_km": 129000, "thickness_km": 30 },
      { "name": "Halo Ring", "inner_radius_km": 100000,
        "outer_radius_km": 122500, "thickness_km": 12500 },
      { "name": "Amalthea Gossamer Ring", "inner_radius_km": 129000,
        "outer_radius_km": 182000, "thickness_km": 2000 },
      { "name": "Thebe Gossamer Ring", "inner_radius_km": 129000,
        "outer_radius_km": 226000, "thickness_km": 8600 }
    ]
  },
  "radiation_belts": {
    "kind": "belt_rings",
    "components": [
      { "name": "Inner Belt", "distance_rp": 1.5 },
      { "name": "Middle Belt", "distance_rp": 3.0 },
      { "name": "Outer Belt", "distance_rp": 6.0 }
    ],
    "params": { "thickness_rp": 0.5, "n_rings": 5, "n_points": 80 }
  }
}
```

(Jupiter belt colors: the source function assigns per-belt colors
internally; if v0.1's schema carried explicit colors for them, add them
from `create_jupiter_radiation_belts`'s color list during the build --
one more reason FLAG-1's confirmation matters. If v0.1 is silent, port
the source's per-belt colors into `components[i].color` for parity with
Earth's belts.)

**Saturn** (replaces line 31's list):

```json
"features": {
  "ring_system": {
    "kind": "flat_rings",
    "components": [
      { "name": "D Ring", "inner_radius_km": 66900,  "outer_radius_km": 74500 },
      { "name": "C Ring", "inner_radius_km": 74658,  "outer_radius_km": 92000 },
      { "name": "B Ring", "inner_radius_km": 92000,  "outer_radius_km": 117500 },
      { "name": "A Ring", "inner_radius_km": 122340, "outer_radius_km": 136800 },
      { "name": "F Ring", "inner_radius_km": 140210, "outer_radius_km": 140420 },
      { "name": "G Ring", "inner_radius_km": 166000, "outer_radius_km": 175000 },
      { "name": "E Ring", "inner_radius_km": 180000, "outer_radius_km": 480000 }
    ]
  }
}
```

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
  existing invariants): every feature has `kind` in the allowed set and
  a non-empty `components` list; every `flat_rings` component has
  `inner_radius_km < outer_radius_km`; every `sphere_shells` component
  has `radius_fraction > 1.0`; colors, where present, match
  `rgb(int, int, int)`. Cheap, and catches a mistyped port at build
  time instead of at render time.
- The per-object coverage_index entries already pass `features` through
  (earth's served entry shows the list today [verified @HEAD]); after
  M1 they carry the dict. That is additive-shape change to a field the
  resolver does not consume [per handoff]; no resolver work.

### 4.4 M1 Layer-1 test updates

- Assert `feature_configs.json` has all 12 slugs; earth/jupiter/saturn
  non-empty; earth's `van_allen_belts.components[0].distance_rp == 1.5`;
  jupiter has `radiation_belts` and NOT `magnetosphere`; saturn's
  `ring_system.components` length 7; halley/encke present with `{}`.
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
      4.2) -- after FLAG-1 is confirmed.
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

## Ref

`documentation/PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md` @
orrery 58dfa520 (design source); `FABLE_MANIFEST_PROMPT_F1_v0.2.md`
(the ask); L-118 (parent); PHASE2_ASSEMBLER_BUILD_MANIFEST_v1.md
(house manifest precedent); gallery `953c650e` / orrery `58dfa520`
(every citation re-verified live this session).

---
Manifest written July 2026 with Anthropic's Claude Fable 5 (Mode 7
collegial relay; independent verification pass against both HEADs).
