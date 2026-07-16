# F1 — Feature-Config Serving Pipeline: Preliminary Design Handoff v0.4

**Type:** DESIGN SESSION (zero code)
**Built on:** orrery HEAD `f961b4424fd633595286c2764a2ebd19df677236`, gallery HEAD
`953c650edc8dbd35ab11ec1720f8283987d63901` (unchanged since v0.1 — no
repo activity across this whole design round)
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
**Supersedes:** v0.3 (two remaining implementation-blocking gaps closed
this round — both now precise enough to build against)
**Status: CONVERGED — ready for a build manifest.** No open design
questions remain that block starting the build. Everything below is
either fully specified or explicitly, deliberately out of scope with a
reason given.

**v0.4 changes from v0.3:**
1. §6.4's F1a interim-minimum rule pinned exactly: exclude only
   `category == "moon"` (includes Charon) from the conservative global
   `served_window` computation; `planet`, `dwarf_planet`, `asteroid`, and
   `comet` all participate normally. Settled this round — asteroids are
   not satellites, dwarf planets and comets are not satellites, by Tony's
   direct call.
2. §6.6's close-encounter handling sharpened from "needs explicit
   truncation, mechanism unclear" to a concrete direction: **anchor the
   osculating elements at the encounter epoch**, the same pattern already
   proven for comets (`overrides.comet.anchor: "Tp"`, Halley/Encke) rather
   than truncating a propagation window computed from tonight's snapshot.
   Confirmed as a generalization of existing, working code
   (`resolve_comet_conic`), not a new mechanism — still out of scope this
   pass (Apophis isn't in Wave 1/2), captured precisely for whenever it
   is.

---

## 1. Where we stand (verified against live code, not the ledger's word)

Unchanged from v0.1-v0.3:

- `derive_served` (`tools/gallery_cache_builder.py`, lines 749-750) writes
  `feature_configs.json` as `{"schema_version": ..., "features": {}}`
  unconditionally, every build.
- Line 727: `event_link` hardcoded `None` (L-119's scope, not this one).
- Line 739: `served_window: None` at the top level of `coverage_index.json`.
- `objects_config.json`'s `features` field is a flat list per object today.
- `resolver.py` (lines 91-106) / `cache_reader.py` (lines 12-14, 40-41)
  already contain the consumer side of `served_window`.
- `halley` / `encke` have no `features` key at all.
- Every object already gets one real Horizons vector fetched nightly for
  `as_of_today` (line 601). `event_windows` (line 77) is real but
  spacecraft-only today.

New this round, confirming §6.6's sharpened direction: `resolve_comet_conic`
(`tools/gallery_cache_builder.py`, line 374) already fetches osculating
elements epoched *at* a solved anchor time (perihelion, via
`overrides.comet.anchor: "Tp"`) rather than propagating from tonight —
confirmed live in Halley's config entry (`objects_config.json` line 103).
Object categories confirmed across the full 12-object catalog: `earth`/
`jupiter`/`saturn` = `planet`; `moon`/`io`/`titan`/`charon` = `moon`;
`pluto` = `dwarf_planet`; `apophis` = `asteroid`; `halley`/`encke` =
`comet`; `voyager_1` = `spacecraft` (structurally outside this whole
propagation-trust question — spacecraft use fetched positions, not Kepler
propagation).

---

## 2. Decisions reached (v0.1 through v0.4)

All decisions from v0.1-v0.3 stand unchanged. Two additions this round:

- **F1a interim-minimum rule (closed):** the conservative global
  `served_window` populated during F1a is the minimum measured
  `window_days` across every object in scope **except** `category ==
  "moon"`. Planets, dwarf planets, asteroids, and comets all participate
  in that minimum normally — none of them get a special carve-out.
- **Close-encounter handling (sharpened, still deferred):** when this is
  eventually built, the right shape is an `overrides.asteroid.anchor`
  entry (mirroring `overrides.comet.anchor`) that fetches elements epoched
  at the encounter date, not a truncation of a long-range propagation
  window. Logged precisely; not built this pass.

---

## 3. Porting inventory — Wave 1 + Wave 2, cited to source

Unchanged from v0.1-v0.3.

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
| `ring_system` | `create_saturn_ring_system` (line 1026) | simple numeric port, 7 components | D 66,900-74,500 km; C 74,658-92,000 km; B 92,000-117,500 km; A 122,340-136,800 km; F 140,210-140,420 km; G 166,000-175,000 km; E 180,000-480,000 km. |

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

### 6.1-6.3
Unchanged from v0.3: tolerance-first, rate-driven measure (epoch+Δ check
vector, Δ≈P/8 capped ~30 days, worse of two samples, `guard_k=2.0` safety
factor); tolerance adopted at 0.5° global, logged as an estimate to be
visually checked once rendered, not a derivation; per-object `trust`
schema serving rate, not just window.

### 6.4 Build phasing: F1a now, F1b later — interim rule now pinned

F1a (this pass, fingerprint untouched): write per-object `trust` blocks as
additive data; populate the existing global `served_window` conservatively.
**The rule, closed this round:** `start_jd`/`end_jd` derived from the
minimum measured `window_days` across all objects in scope where
`category != "moon"`. Moon-category objects (including Charon) get their
own accurate `trust` block served but are not enforced by the interim
global check — an accepted, known gap for the F1a period, closed properly
when F1b lands.

F1b (a later, deliberate item, unchanged): resolver + cache_reader consume
per-object `trust` directly; fingerprint reopen scheduled on purpose.

### 6.5 UX direction: envelope, not a wall

Unchanged from v0.3.

### 6.6 The one-orbit fallback, and close-encounter handling (sharpened)

Unchanged from v0.3 on the fallback itself (kept only as an outer cap for
planets, not a floor; satellites need ~P/8 if anything; comets bound to
current apparition).

**Close-encounter handling, sharpened this round.** The prior framing
("needs explicit truncation, mechanism unclear") is replaced with a
concrete direction: **anchor the osculating elements at the encounter
epoch**, rather than truncating a window computed by propagating from
tonight's snapshot. This is a generalization of a pattern already proven
in the builder for comets — `resolve_comet_conic`
(`tools/gallery_cache_builder.py` line 374) fetches elements epoched *at*
a solved anchor time (perihelion, `overrides.comet.anchor: "Tp"`,
confirmed live in Halley's config entry) instead of propagating toward it
from a distant epoch. For Apophis, the equivalent would be an
`overrides.asteroid.anchor` entry pinned to the 2029 close-approach date,
with a small parallel builder branch (not yet written) that fetches
elements at that specific epoch the same way `resolve_comet_conic` does
for Tp. **Still explicitly out of scope this pass** — Apophis isn't in
Wave 1/2 — captured precisely so this doesn't need rediscovering later.

---

## Provenance Discipline Notice

Unchanged from v0.3. All §3 values read live from HEAD; the Moon evection
figure independently web-verified; the 0.5° tolerance flagged as an
adopted estimate, not a derivation. New this round: the close-encounter
anchor direction and the object-category table (§1) were both confirmed
against live code/config this session, not assumed from the prior
framing.

---

## Gap / next session

- [ ] Write the `objects_config.json` edits for Earth, Jupiter, Saturn,
      Halley, Encke (Wave 1 + Wave 2 + schema completeness, §3)
- [ ] Rewrite `derive_served` per §5 (feature serving) and §6.4 (F1a:
      emit per-object `trust` blocks; populate global `served_window` via
      the now-pinned moon-exclusion minimum rule)
- [ ] Implement the epoch+Δ check-vector fetch and two-body error-rate
      measurement (§6.2), reusing `gallery/assembler/render_orbits.py`'s
      `solve_kepler`/`propagate_marker` (already validated to machine
      precision) rather than writing new propagation math
- [ ] Layer-1 offline-suite updates for both the new feature-config shape
      and the new `trust` block
- [ ] Offline suite from a clean checkout, `--dry-run`, then a real
      `--first-build`/`--nightly` as acceptance
- [ ] Smoke-test the JS feature layer against Earth's golden artifact
      before trusting Jupiter/Saturn's render
- [ ] Once Wave 1's Earth artifact renders the uncertainty envelope
      (§6.5), visually sanity-check the 0.5° tolerance
- [ ] Revisit per-view tolerance differentiation once there's a basis for
      it
- [ ] Log a new ledger item for the deferred sun-oriented feature category
      — needed, not dropped
- [ ] Log F1b (resolver/cache_reader consume per-object `trust`,
      deliberate fingerprint reopen) as its own scheduled ledger item
- [ ] Log the close-encounter anchor-mechanism direction (§6.6) as a
      flagged, unscheduled item — relevant once Apophis enters scope
- [ ] L-119 (event_link) and L-123 (info card) sequence after this Gap,
      not inside it

---

## Ref

Unchanged from v0.3, plus this document and the confirmed object-category
table (§1): `data/objects_config.json` (full 12-object `category` field
audit), Halley's `overrides.comet.anchor` entry (line 103).

---
Session/entry written July 2026 with Anthropic's Claude Sonnet 5 and Claude
Fable (Mode 7 collegial relay, §6).
