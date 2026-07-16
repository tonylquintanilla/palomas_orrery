# F1 — Feature-Config Serving Pipeline: Preliminary Design Handoff v0.3

**Type:** DESIGN SESSION (zero code)
**Built on:** orrery HEAD `f961b4424fd633595286c2764a2ebd19df677236`, gallery HEAD
`953c650edc8dbd35ab11ec1720f8283987d63901` (re-confirmed live at v0.2 write
time; unchanged since — no repo activity between v0.2 and v0.3)
**Companion:** MASTER_PLAN_INTERACTIVE_GALLERY.md v13 (Phase 2 section, "New
in v13"); PHASE2_ARTIFACT1_AS_BUILT.md §7 (dev render page, date picker),
§8 (deviation 2), §9 (open items)
**Parent:** L-118 (F1, gates Artifact 2), L-098 (Phase 1b serving pipeline,
closed)
**Related, explicitly out of scope this pass:** L-119 (F2, event_link —
sequenced after F1), L-123 (info card — sequenced after F1)
**Participants:** Tony Quintanilla, Claude Sonnet 5 (design + verification),
Claude Fable (Mode 7 collegial relay — served_window trust-bound problem,
§6)
**Supersedes:** v0.2 (§6.2's tolerance value was the one item still open;
resolved this round)

**v0.3 changes from v0.2:** Tolerance adopted at **0.5° along-track true
anomaly, applied globally** — Tony's own words: "I have no basis for
tolerance other than what Fable suggested." This is logged as an adopted
working default, not a derived result — see §6.2 for the honest framing
and what would revise it. The per-view differentiation Tony leaned toward
earlier is not abandoned, just deferred until there's an actual basis for
different values (see Gap). Nothing else changed from v0.2.

---

## 1. Where we stand (verified against live code, not the ledger's word)

Unchanged from v0.1/v0.2:

- `derive_served` (`tools/gallery_cache_builder.py`, lines 749-750) writes
  `feature_configs.json` as `{"schema_version": ..., "features": {}}`
  unconditionally, every build.
- Same function, line 727: `event_link` hardcoded `None` (L-119's scope).
- Line 739: `served_window: None` at the top level of `coverage_index.json`.
- `data/objects_config.json`'s `features` field is a flat list per object
  today, not yet the keyed dict this handoff specifies.
- `gallery/assembler/resolver.py` (lines 91-106) and `cache_reader.py`
  (lines 12-14, 40-41) already contain the *consumer* side of
  `served_window`.
- `halley` and `encke` have no `features` key at all today.
- Every object (not only spacecraft) already gets one real Horizons vector
  fetched nightly for `as_of_today` (`tools/gallery_cache_builder.py` line
  601). The `event_windows` field (`data/objects_config.json` line 77) is
  real but currently spacecraft-only.

---

## 2. Decisions reached (v0.1 through v0.3)

- **Config shape:** feature params move inline into `objects_config.json`,
  dict keyed by feature name, no sibling file.
- **Wave sequencing:** Earth `atmosphere_shell` + `van_allen_belts`,
  Jupiter `ring_system`, and Saturn `ring_system` are all authored into
  config and wired through `derive_served` in the same pass — not a
  build-order gate. *Testing* stays sequenced: Earth's JS render against
  the closed golden artifact first, then Jupiter/Saturn.
- **Jupiter's config swap:** `magnetosphere` → `radiation_belts` for this
  pass. Full envelope + bow shock stays deferred.
- **Deferred as one flagged category, needed not dropped:** magnetosphere
  envelopes + bow shocks (Earth, Jupiter, Saturn), Mercury's sodium tail,
  comet comae/tails. Recommend a new ledger item once F1 closes.
- **Comets:** Halley/Encke get an empty `"features": {}` this pass, schema
  completeness only.
- **Config field naming:** mirrors the orrery's own dict shapes exactly —
  no invented unit suffixes; units-by-comment convention noted in prose
  since JSON can't carry it inline.
- **`served_window`:** reworked via Fable relay — see §6. Measured
  two-body error rate (not divergence-from-mean) drives a per-object
  `trust` block; F1a (additive, fingerprint untouched) ships now, F1b
  (resolver enforces per-object bounds, deliberate fingerprint reopen)
  is a separate, later, scheduled item. Envelope-not-wall UX direction
  agreed, confirmed once rendered. One-orbit fallback kept only as an
  outer cap, not a floor; close-encounter truncation (Apophis) flagged,
  unscheduled.
- **Tolerance value (new in v0.3):** adopted at 0.5°, global — see §6.2.

---

## 3. Porting inventory — Wave 1 + Wave 2, cited to source

Unchanged from v0.1/v0.2.

### Earth
| Feature key | Source | Type | Params |
|---|---|---|---|
| `atmosphere_shell` | `SHELL_CONFIGS['Earth']['atmosphere']` (line 1423) + `['upper_atmosphere']` (line 1446) | simple numeric port | Lower: `radius_fraction 1.05`, `rgb(150,200,255)`, `opacity 0.5`. Upper: `radius_fraction 1.25`, `rgb(100,150,255)`, `opacity 0.3`. `n_points 20` both. |
| `van_allen_belts` | `CUSTOM_SHELLS['Earth']['magnetosphere']` (line 2258) → `create_earth_magnetosphere_shell` (line 650), belt-only (lines 780-822) | custom-geometry port | `inner_belt_distance 1.5 R_E`, `outer_belt_distance 4.5 R_E`, `belt_thickness 0.5 R_E`, `n_rings 5`, `n_points 80`/ring, `z = 0.2*belt_radius*sin(2*angle)`. Colors `rgb(255,100,100)` / `rgb(100,200,255)`. |

### Jupiter
| Feature key | Source | Type | Params |
|---|---|---|---|
| `ring_system` | `create_jupiter_ring_system` (line 882) | simple numeric port, 4 components | Main 122,500-129,000 km (30 km); Halo 100,000-122,500 km (12,500 km); Amalthea Gossamer 129,000-182,000 km (2,000 km); Thebe Gossamer 129,000-226,000 km (8,600 km). |
| `radiation_belts` (replaces `magnetosphere`) | `create_jupiter_radiation_belts` (line 704) | custom-geometry port | `belt_distances [1.5, 3.0, 6.0] R_J`, `belt_thickness 0.5 R_J`, `n_rings 5`, `n_points 80`/ring. No sun-dependency. |

### Saturn
| Feature key | Source | Type | Params |
|---|---|---|---|
| `ring_system` | `create_saturn_ring_system` (line 1026) | simple numeric port, 7 components | D 66,900-74,500 km; C 74,658-92,000 km; B 92,000-117,500 km; A 122,340-136,800 km; F 140,210-140,420 km; G 166,000-175,000 km; E 180,000-480,000 km. No sun-dependency. |

### Halley / Encke
Add `"features": {}` to each. No coma/tail params ported.

---

## 4. Config schema: before / after

Unchanged from v0.1.

---

## 5. `derive_served` changes (F1's feature-serving scope)

Unchanged from v0.1: read `obj.get('features', {})` per object, assemble
`feature_configs.json` from it instead of the empty literal. `event_link`
and the info-card addition stay out of this change.

---

## 6. `served_window` — reworked via Mode 7 relay (Claude Fable)

### 6.1 The actual problem

Artifact 1's dev page has a working date picker that re-propagates Earth's
position via Kepler's equation from last night's osculating snapshot.
Nothing today bounds how far from "tonight" a requested date can be before
that's unreliable — the resolver's check exists in code but is unenforced
(`null`).

### 6.2 The measure: tolerance-first, rate-driven

"Valid" means "position error below a tolerance." Window = tolerance ÷
error-growth-rate, where the rate is measured directly at build time: a
second Horizons check vector at epoch + Δ (Δ ≈ P/8, capped ~30 days,
worse of two samples to avoid aliasing), compared against two-body
propagation from the served elements. Self-calibrating per object — the
Moon's large rate yields a short window automatically, Neptune's tiny rate
a long one.

**Tolerance: adopted at 0.5° along-track true anomaly, applied globally.**
Fable's original suggestion, framed as "roughly where marker placement
error becomes visible at scene zoom" — an engineering estimate, not a
derived figure. Tony's basis for adopting it, stated plainly: no
independent basis exists to pick a different number, so there's no reason
to withhold a reasonable one. This is logged honestly as an **adopted
working default**, not a validated result. Per-view differentiation (which
Tony leaned toward earlier — a scene-scale render can tolerate more than
an Earth-Moon closeup) is not abandoned; it's deferred until there's an
actual basis for setting different values per view, which is more likely
to come from *looking at* a rendered closeup than from deriving it in
advance. This is the project's own Visual Verification principle applying
here as much as anywhere: the render is the ground truth, and 0.5° is
checkable once Wave 1's Earth artifact actually shows the uncertainty
envelope on screen (§6.5) — if it looks too generous or too tight at that
point, that's the moment to revise it, not now.

Divergence-from-mean stays demoted to a cross-check where mean elements
exist (planets + curated comets), not the primary driver — unchanged from
v0.2, for the reasons given there (amplitude vs. rate; weakest exactly
where satellites need it most).

### 6.3 Schema: per-object, not global

```json
"trust": {
  "method": "measured",
  "epoch_jd": 2461236.5,
  "error_km_per_day": 142.0,
  "window_days": 38.5,
  "tolerance_deg": 0.5,
  "safety_k": 2.0
}
```

`tolerance_deg` is carried per-object in this schema even though the
*value* is global for now (0.5° everywhere) — this costs nothing and means
per-view differentiation later is a value change, not a schema change.

### 6.4 Build phasing: F1a now, F1b later

Unchanged from v0.2. F1a: additive `trust` blocks, conservative global
`served_window` stopgap, fingerprint untouched. F1b: resolver/cache_reader
consume per-object `trust` directly, deliberate fingerprint reopen,
scheduled as its own later item.

### 6.5 UX direction: envelope, not a wall

Unchanged from v0.2. Growing uncertainty arc along the orbit, fading
marker, shaded high-confidence band, tooltip on extrapolated dates, hard
stop only at an outer sanity cap (~200 years). Mode 5 territory for the
actual visual treatment — and now also the natural place to sanity-check
the 0.5° tolerance itself once there's something to look at.

### 6.6 The one-orbit fallback: kept only as an outer cap, not a floor

Unchanged from v0.2. Moon evection (±1.274°, ~31.8-day period,
independently verified) shows a one-period fallback would badly understate
risk for satellites. Comets need apparition-bounding, not period-bounding.
Planets: fine as an outer cap. New finding carried forward: close
encounters (Apophis 2029) invalidate two-body propagation regardless of
window length — `event_windows` is the right naming precedent to extend,
confirmed spacecraft-only today, not wired for this yet. Flagged, not
built.

---

## Provenance Discipline Notice

Unchanged from v0.2. §3's values read live from HEAD, not recalled. The
Moon evection figure independently web-verified, not accepted solely on
Fable's word. The 0.5° tolerance adopted in §6.2 is explicitly flagged as
an unvalidated engineering estimate, not a sourced or derived value —
consistent with "show the envelope of the unknowable" rather than dressing
up a placeholder as a settled number.

---

## Gap / next session

- [ ] Write the `objects_config.json` edits for Earth, Jupiter, Saturn,
      Halley, Encke (Wave 1 + Wave 2 + schema completeness, §3)
- [ ] Rewrite `derive_served` per §5 (feature serving) and §6.4 (F1a:
      emit per-object `trust` blocks, populate conservative global
      `served_window`)
- [ ] Implement the epoch+Δ check-vector fetch and two-body error-rate
      measurement (§6.2) — new builder work, not yet written
- [ ] Layer-1 offline-suite updates for both the new feature-config shape
      and the new `trust` block
- [ ] Offline suite from a clean checkout, `--dry-run`, then a real
      `--first-build`/`--nightly` as acceptance
- [ ] Smoke-test the JS feature layer against Earth's golden artifact
      before trusting Jupiter/Saturn's render
- [ ] **Once Wave 1's Earth artifact renders the uncertainty envelope
      (§6.5), visually sanity-check the 0.5° tolerance** — revise if it
      reads too generous or too tight; this is the intended validation
      path, not a derivation done in advance
- [ ] Revisit per-view tolerance differentiation once there's a basis for
      it (likely from that same visual check, closeup vs. scene-scale)
- [ ] Log a new ledger item for the deferred sun-oriented feature category
      — needed, not dropped
- [ ] Log F1b (resolver/cache_reader consume per-object `trust`,
      deliberate fingerprint reopen) as its own scheduled ledger item
- [ ] Log the close-encounter truncation finding (§6.6) as a flagged,
      unscheduled item — relevant once Apophis enters scope
- [ ] L-119 (event_link) and L-123 (info card) sequence after this Gap,
      not inside it — unchanged

---

## Ref

Unchanged from v0.2, plus this document. `FABLE_PROMPT_served_window_
trust_bound_v0.1.md` (relay prompt); `orbital_elements.py` (Moon entry,
line 853); lunar evection figure independently verified against a
published lunar-theory source (Wikipedia, "Evection").

---
Session/entry written July 2026 with Anthropic's Claude Sonnet 5 and Claude
Fable (Mode 7 collegial relay, §6).
