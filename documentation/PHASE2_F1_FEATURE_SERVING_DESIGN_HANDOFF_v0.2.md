# F1 — Feature-Config Serving Pipeline: Preliminary Design Handoff v0.2

**Type:** DESIGN SESSION (zero code)
**Built on:** orrery HEAD `f961b4424fd633595286c2764a2ebd19df677236`, gallery HEAD
`953c650edc8dbd35ab11ec1720f8283987d63901` (re-confirmed live at v0.2 write
time — unchanged since v0.1)
**Companion:** MASTER_PLAN_INTERACTIVE_GALLERY.md v13 (Phase 2 section, "New
in v13"); PHASE2_ARTIFACT1_AS_BUILT.md §7 (dev render page, date picker),
§8 (deviation 2), §9 (open items)
**Parent:** L-118 (F1, gates Artifact 2), L-098 (Phase 1b serving pipeline,
closed)
**Related, explicitly out of scope this pass:** L-119 (F2, event_link —
sequenced after F1), L-123 (info card — sequenced after F1)
**Participants this round:** Tony Quintanilla, Claude Sonnet 5 (design +
verification), Claude Fable (Mode 7 collegial relay — served_window
trust-bound problem, §6)
**Supersedes:** v0.1 (§6 was an open question there; resolved this round)

**v0.2 changes from v0.1:** §6 (`served_window`) fully reworked via a Mode 7
collegial relay to Fable — replaces the divergence-from-mean proposal with
a measured two-body error-rate approach, a per-object `trust` schema, a
phased F1a/F1b build split, an envelope-not-wall UX direction, and a
corrected view of the one-orbit fallback (kept only as an outer cap, not a
floor). Decision 2 (wave sequencing) also revised: config data for Earth,
Jupiter, and Saturn can be authored together in one pass; only the JS
*testing* is sequenced Earth-first, not the build itself. Everything else
carries forward unchanged from v0.1.

---

## 1. Where we stand (verified against live code, not the ledger's word)

Unchanged from v0.1 — re-stated for completeness, not re-verified this
round since nothing in the gallery repo moved between v0.1 and v0.2 (HEAD
confirmed identical, above):

- `derive_served` (`tools/gallery_cache_builder.py`, lines 749-750) writes
  `feature_configs.json` as `{"schema_version": ..., "features": {}}`
  unconditionally, every build.
- Same function, line 727: `event_link` hardcoded `None` (L-119's scope).
- Line 739: `served_window: None` at the top level of `coverage_index.json`.
- `data/objects_config.json`'s `features` field is a flat list per object
  today, not yet the keyed dict this handoff specifies.
- `gallery/assembler/resolver.py` (lines 91-106) and `cache_reader.py`
  (lines 12-14, 40-41) already contain the *consumer* side of
  `served_window` — confirming F1 must produce, at minimum, a
  `{"start_jd": ..., "end_jd": ...}` shaped bound for the existing
  global-scalar reader to keep working (see §6 for why this is now only
  the *interim* shape).
- `halley` and `encke` have no `features` key at all today.

New this round, load-bearing for §6: every object (not only spacecraft)
already gets one real Horizons vector fetched nightly for `as_of_today`
(`tools/gallery_cache_builder.py` line 601, `as_of_today_km`) — confirmed
on Earth's served block, which is osculating-elements-only otherwise. The
`event_windows` field (`data/objects_config.json` line 77, Voyager 1's
flyby dates) is real, but today only densifies *fetched* position vectors
for spacecraft — it is not currently wired to bound a Kepler-propagation
window for an osculating-elements object.

---

## 2. Decisions reached (v0.1 + this round)

- **Config shape (§1 of v0.1, unchanged):** feature params move inline
  into `objects_config.json`, dict keyed by feature name, no sibling file.
- **Wave sequencing (revised this round):** Earth `atmosphere_shell` +
  `van_allen_belts`, Jupiter `ring_system`, and Saturn `ring_system` are
  all authored into config and wired through `derive_served` in the same
  pass — this is not a build-order gate. *Testing* stays sequenced:
  smoke-test the JS feature layer against Earth's closed golden artifact
  first, then Jupiter/Saturn, so a rendering-approach problem is caught
  cheaply before three objects' worth of render is trusted.
- **Jupiter's config swap (unchanged):** `magnetosphere` → `radiation_belts`
  for this pass — the zero-sun-dependency member of Jupiter's magnetosphere
  family, matching Earth's `van_allen_belts` scoping. Full envelope + bow
  shock stays deferred (see next point).
- **Deferred as one flagged category (unchanged, standing):**
  magnetosphere envelopes + bow shocks (Earth, Jupiter, Saturn), Mercury's
  sodium tail, comet comae/tails — all sun-oriented, none proven in the JS
  layer yet. **Needed, not dropped** — Tony's explicit framing, both for
  this category and for comet features specifically. Recommend a new
  ledger item once F1 closes.
- **Comets (unchanged):** Halley/Encke get an empty `"features": {}` this
  pass for schema completeness only; no coma/tail params ported.
- **Config field naming (unchanged):** mirrors the orrery's own dict shapes
  exactly — `atmosphere`/`upper_atmosphere` (not "lower"/"upper"),
  `inner_belt_distance`/`outer_belt_distance`/`belt_thickness` (no invented
  unit suffix), `*_km` ring keys copied near-verbatim from
  `jupiter_visualization_shells.py`'s own `ring_params` dict. The
  units-by-comment convention doesn't survive into JSON; noted in prose
  here rather than invented as a schema field.
- **`served_window` (fully reworked this round — see §6).**

---

## 3. Porting inventory — Wave 1 + Wave 2, cited to source

Unchanged from v0.1. Carried forward without modification:

### Earth
| Feature key | Source | Type | Params |
|---|---|---|---|
| `atmosphere_shell` | `shell_configs.py` `SHELL_CONFIGS['Earth']['atmosphere']` (line 1423) + `['upper_atmosphere']` (line 1446) | simple numeric port | Lower: `radius_fraction 1.05`, `rgb(150,200,255)`, `opacity 0.5`. Upper: `radius_fraction 1.25`, `rgb(100,150,255)`, `opacity 0.3`. `n_points 20` both. |
| `van_allen_belts` | `CUSTOM_SHELLS['Earth']['magnetosphere']` (line 2258) → `earth_visualization_shells.create_earth_magnetosphere_shell` (line 650), belt-only portion (lines 780-822) | custom-geometry algorithm port | `inner_belt_distance 1.5 R_E`, `outer_belt_distance 4.5 R_E`, `belt_thickness 0.5 R_E`, `n_rings 5`, `n_points 80`/ring, `z = 0.2*belt_radius*sin(2*angle)`. Colors `rgb(255,100,100)` / `rgb(100,200,255)`. |

### Jupiter
| Feature key | Source | Type | Params |
|---|---|---|---|
| `ring_system` | `create_jupiter_ring_system` (line 882) | simple numeric port, 4 components | Main 122,500-129,000 km (30 km thick); Halo 100,000-122,500 km (12,500 km); Amalthea Gossamer 129,000-182,000 km (2,000 km); Thebe Gossamer 129,000-226,000 km (8,600 km). April 2026 Gemini fact-check, NASA/Galileo. |
| `radiation_belts` (replaces `magnetosphere`) | `create_jupiter_radiation_belts` (line 704) | custom-geometry algorithm port | `belt_distances [1.5, 3.0, 6.0] R_J`, `belt_thickness 0.5 R_J`, `n_rings 5`, `n_points 80`/ring. No `sun_position` parameter — confirmed zero sun-dependency. |

### Saturn
| Feature key | Source | Type | Params |
|---|---|---|---|
| `ring_system` | `create_saturn_ring_system` (line 1026) | simple numeric port, 7 components | D 66,900-74,500 km; C 74,658-92,000 km; B 92,000-117,500 km; A 122,340-136,800 km; F 140,210-140,420 km; G 166,000-175,000 km; E 180,000-480,000 km. No `sun_position` parameter. |

### Halley / Encke
Add `"features": {}` to each. No coma/tail params ported.

---

## 4. Config schema: before / after

Unchanged from v0.1 — see that document for the full before/after JSON.
Field naming confirmed as-drafted (§2).

---

## 5. `derive_served` changes (F1's feature-serving scope)

Unchanged from v0.1: read `obj.get('features', {})` per object, assemble
`feature_configs.json` from it instead of the empty literal. `event_link`
and the info-card addition stay out of this change, per L-119/L-123's own
Gap notes.

---

## 6. `served_window` — reworked via Mode 7 relay (Claude Fable)

v0.1 left this as an open question with two weak candidates (reusing
spacecraft-fetch defaults, or a vague new "propagation horizon" field). A
prompt was sent to Fable scoped specifically to this problem
(`FABLE_PROMPT_served_window_trust_bound_v0.1.md`); the response was
reviewed, spot-checked, and confirmed by Tony point-by-point. What follows
is the resolved design.

### 6.1 The actual problem

Artifact 1's dev page already has a working date picker that re-propagates
Earth's position via Kepler's equation from last night's osculating
snapshot (`PHASE2_ARTIFACT1_AS_BUILT.md` §7). Nothing today bounds how far
from "tonight" a requested date can be before that propagated position is
physically unreliable — the resolver's `served_window` check exists in
code but is unenforced (`null`).

### 6.2 The measure: tolerance-first, rate-driven (replaces the
divergence-from-mean proposal)

"Valid" means "position error below a tolerance." Window = tolerance ÷
error-growth-rate. The rate is measured directly at build time rather than
inferred from mean-elements comparison:

- In the same nightly Horizons call that already fetches `as_of_today`
  (confirmed existing for every object, §1), request a second check vector
  at epoch + Δ (Δ ≈ P/8, capped ~30 days).
- Propagate the served osculating elements two-body to that same epoch;
  compare against the real fetched vector. `|Δr| / Δt` = a genuine
  along-track error rate in km/day, measured against the actual
  integrated ephemeris, not assumed.
- Sample two Δs (P/8 and P/4) and take the worse rate, to avoid aliasing
  against a periodic perturbation term sampled at a lucky node.
- Apply a safety factor reusing the existing `guard_k` concept
  (`objects_config.json` defaults, currently `2.0`) rather than inventing
  a new tolerance-stacking parameter.

This is **self-calibrating per object** — the Moon's large rate yields a
short window automatically; Neptune's tiny rate yields a long one — with
no curated per-class table to maintain.

**Divergence-from-mean (the original proposal) is demoted to a cross-check
where mean elements exist** (planets + the curated comet list), not the
primary driver. Reasoning, confirmed this round: it measures the
*amplitude* of perturbation, not its *rate* — an orbit can sit far from
its mean elements while drifting slowly, or close while drifting fast.
It's also weakest exactly where the bound matters most: moons were
explicitly excluded from the mean-elements work (master plan v12), and the
Moon's own entry (`orbital_elements.py` line 853) is a static 2013-07-31
snapshot with no secular terms — 13 years stale. Tony's read on this
pivot: "my idea was simplistic" — noted here because it's a real change of
direction, not a footnote.

Nightly-snapshot-to-snapshot drift (a third option Fable considered) is
strictly dominated: wholesale nightly replacement means at most one prior
generation exists, and the measured-rate approach gets the same
information in a single build with no history dependency.

**Tolerance value itself: still open.** Fable's suggestion (~0.5°
along-track true anomaly, roughly where marker placement error becomes
visible at scene zoom) is a reasonable starting point, not a locked
number. Tony's lean, this round: **tolerance should be per-view, not
global** — a scene-scale render tolerates degrees; an Earth-Moon closeup
doesn't. The actual tolerance value(s) per view class are not decided;
carried to the Gap section.

### 6.3 Schema: per-object, not global

A single global `served_window` cannot serve a scene containing both
Neptune and the Moon — confirmed this round as the correct read. Proposed
per-object block, serving the **rate** (not just the resulting window),
so the client can derive uncertainty at any requested date, not only
check a fixed bound:

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

### 6.4 Build phasing: F1a now, F1b later (deliberately)

Making the resolver actually consume per-object bounds touches code that's
already built and locked into Artifact 1's golden fingerprint
(`resolver.py`, `cache_reader.py`). Confirmed this round: F1 stays scoped
to the additive half; the fingerprint reopen is real and gets scheduled on
purpose, not absorbed silently.

- **F1a (this pass, fingerprint untouched):** write the per-object `trust`
  block into `coverage_index.json` as new, additive data — the existing
  resolver ignores fields it doesn't know about (`resolver.py`'s own
  forward-compatibility warning path, line 86-89). Populate the *existing*
  global `served_window` conservatively as an interim stopgap — e.g., the
  minimum window across non-satellite objects in scope for the artifact
  being built. This makes the resolver's current global check start
  enforcing something real immediately, without any schema-consumer
  change.
- **F1b (a later, deliberate item):** `resolver.py` + `cache_reader.py`
  consume per-object `trust` directly; the global field is demoted to an
  outer sanity bound. Version the fingerprint; ship as one small, reviewed
  diff, not folded into F1a.

### 6.5 UX direction: envelope, not a wall

Directly instantiates the resident protocol's own "Show the Envelope of
the Unknowable" principle — not a new idea, a direct application of one
already in the house style. Rather than hard-blocking past the window,
render growing uncertainty: an arc along the orbit, length = rate ×
|t − epoch|, centered on the propagated position. Scrubbing past an
object's window fades its marker while the arc grows; planets stay crisp
for decades, a scrubbed-past Moon visibly degrades. Positive framing on
the date picker itself (a shaded "high-confidence" band), a tooltip on
extrapolated dates ("along-track uncertainty ~1.2°, ±N days beyond
tonight's data"). Hard stop reserved only for an outer sanity cap (~200
years), where the exercise stops meaning anything regardless of object.

**Tony's call, standing:** this is Mode 5 (visual) territory for the
actual treatment — confirm once there's a render to look at, not from
prose. Logged here as the agreed direction, not a locked visual spec.

### 6.6 The one-orbit fallback: kept only as an outer cap, not a floor

Corrected this round, with a verified concrete number. The Moon's evection
term alone is ±1.274° in ecliptic longitude with a ~31.8-day period
(independently confirmed against published lunar theory, not just
relayed) — at 384,400 km that's ~6,700 km, about four lunar radii, well
inside one period and plainly visible at an Earth-centered closeup scale.
A one-orbit-period fallback would have shipped a badly wrong bound for
exactly the object Tony flagged as the hardest case. Tony's own framing:
"my one orbit idea was a first cut... this is much better."

- **Satellites:** one period understates risk. If a fallback is still
  needed anywhere (Option A should make it largely moot), ~P/8 is
  defensible; a full period is not.
- **Long-period comets:** one period *overstates* trust — Halley's would
  be ±76 years from a single pinned apparition, spanning perturbations and
  nongravitational forces a conic doesn't model. Bound to the current
  apparition instead, consistent with the record-pinning discipline
  already in the house pattern (horizons-orbital-mechanics skill).
- **Planets:** fine as an outer cap — it was never the binding constraint
  there anyway.
- **New finding, not previously surfaced by either of us:** two-body
  propagation is invalid through a close encounter regardless of window
  length. Apophis (2029 close approach) sits in the project's own catalog.
  Any object with a known encounter inside its computed window needs the
  window truncated at the encounter. The `event_windows` field is the
  right naming precedent to extend — but confirmed this round that it's
  currently spacecraft-only (densifies fetched vectors for flybys), not
  wired to truncate a Kepler-propagation bound for a smallbody. Flagged,
  not built — Apophis isn't in Wave 1/2 scope.

---

## Provenance Discipline Notice

§3's values carry forward from v0.1 unchanged (all read live from HEAD,
not recalled — see that section). New this round: the Moon evection figure
(±1.274°, ~31.8-day period) cited in §6.6 was independently web-verified
against a lunar-theory source this session, not accepted solely on
Fable's word — consistent with the Fetched-vs-Recalled convention for a
specific numeric claim used to drive a real design decision. The
`event_windows`/`as_of_today` characterizations in §1 and §6.6 were
corrected against the live builder source before being folded in here,
where Fable's phrasing had rounded slightly optimistic.

---

## Gap / next session

- [ ] Decide the tolerance value(s) for §6.2 — Tony leans per-view (scene
      vs. closeup); actual number(s) not yet chosen
- [ ] Confirm the config field-naming convention (§4, carried from v0.1)
      before it's carried into a build manifest
- [ ] Write the `objects_config.json` edits for Earth, Jupiter, Saturn,
      Halley, Encke (Wave 1 + Wave 2 + schema completeness, §3)
- [ ] Rewrite `derive_served` per §5 (feature serving) and §6.4 (F1a: emit
      per-object `trust` blocks, populate conservative global
      `served_window`)
- [ ] Implement the epoch+Δ check-vector fetch and two-body error-rate
      measurement (§6.2) — new builder work, not yet written
- [ ] Layer-1 offline-suite updates for both the new feature-config shape
      and the new `trust` block
- [ ] Offline suite from a clean checkout, `--dry-run`, then a real
      `--first-build`/`--nightly` as acceptance
- [ ] Smoke-test the JS feature layer against Earth's golden artifact
      before trusting Jupiter/Saturn's render (test-order, not build-order
      — §2)
- [ ] Log a new ledger item for the deferred sun-oriented feature category
      (magnetosphere envelopes/bow shocks, Mercury's sodium tail, comet
      tails) — needed, not dropped
- [ ] Log F1b (resolver/cache_reader consume per-object `trust`,
      deliberate fingerprint reopen) as its own scheduled ledger item —
      explicitly not part of this F1 pass
- [ ] Log the close-encounter truncation finding (§6.6) as a flagged,
      unscheduled item — relevant once Apophis enters scope, not before
- [ ] L-119 (event_link) and L-123 (info card) sequence after this Gap,
      not inside it — unchanged

---

## Ref

Everything from v0.1's Ref, plus: `gallery/assembler/resolver.py` (lines
86-106), `tools/gallery_cache_builder.py` (`as_of_today_km` line 483,
`process_object` lines 504-601), `data/objects_config.json` (`event_windows`
example, line 77); `FABLE_PROMPT_served_window_trust_bound_v0.1.md` (this
round's relay prompt); orrery `orbital_elements.py` (Moon entry, line
853). Lunar evection figure independently verified against a published
lunar-theory source (Wikipedia, "Evection"), not carried from Fable's
response alone.

---
Session/entry written July 2026 with Anthropic's Claude Sonnet 5 and Claude
Fable (Mode 7 collegial relay, §6).
