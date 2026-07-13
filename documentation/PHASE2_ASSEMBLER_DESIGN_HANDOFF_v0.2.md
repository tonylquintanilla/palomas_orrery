# Phase 2 — Solar System Assembler: Design Handoff v0.2 (closed pre-design)

**Type:** DESIGN SESSION (zero code)
**Built on:** orrery HEAD `af58f7f87f609f2a632853f50a362ed3ebb30d49`, gallery HEAD
`a08bdd10769f93d7d42601c76fcc14786251ef05` (reconfirmed live at time of writing)
**Companion:** MASTER_PLAN_INTERACTIVE_GALLERY.md v11 (Phase 2 section)
**Parent:** L-079 (shared assembler architecture, keystone)
**Supersedes:** v0.1 (reviewed by Claude Opus 4.8, Mode 7 relay). Every open
design question v0.1 carried into that review has since been resolved or
scoped out — see Section 4. This version is the closed pre-design handoff,
intended to go forward as the basis for a full design manifest.

**Scope note:** housekeeping items (ledger bookkeeping, L-026 CRLF check,
adding Halley to config) and deferred items (Studio preset-authoring refactor,
NEO/spacecraft curated links) are deliberately excluded from this document.
The former are being handled directly outside this handoff; the latter are
tracked in the ledger (L-046, L-104) as their own separate track, unrelated
to the assembler build below.

---

## 1. Where things stand (verified)

- **Phase 1b (L-098) is closed** — verified live at HEAD, not taken on a
  prior handoff's word.
- **L-087 (helpers split) is done** — the four dead tkinter imports in
  `palomas_orrery_helpers.py` were deleted (Tony, directly); independently
  re-verified clean at current HEAD (909 lines, zero tkinter references,
  sole consumer `palomas_orrery.py` unaffected).
- **Scope: the full assembler, not a reduced slice.** A basic scene already
  exercises nearly all the orchestration a solar-system assembler needs
  (object selection, center resolution, shell dispatch, hover composition,
  camera, axes, figure assembly) — there is no meaningful smaller code
  slice to build first.

## 2. What the interactive gallery is — and deliberately is not

Worth stating explicitly, since it scopes everything below: this is not
importing the orrery's functionality wholesale. The assembler reuses the
orrery's computation engines and conventions; almost everything *around*
them is deliberately narrower.

- **Cache-only, never live Horizons** — the single biggest difference. The
  desktop can query any date, any object, live, right now. The interactive
  gallery can only ever show what Phase 1b's served cache already has:
  ~12 configured objects, within a maintained backfill/freeze window. This
  is architectural, not a gap that closes over time.
- **Object catalog breadth** — `celestial_objects.py` has ~179 objects plus
  free-form Horizons ID entry; the gallery config has 12. Every addition
  goes through the deliberate add-object procedure (Section 5), never a
  "just type the ID" path.
- **Static scenes only** — no animation in Phase 2, though the vocabulary
  reserves a content-type distinction for it later. The desktop has full
  animation today.
- **One domain of four** — solar system is Phase 2; stars/hybrid/Earth-system
  are Phase 3-5, not guaranteed parity with what the desktop already covers.
- **Minimal control surface, by design** — object selection, center body,
  date picker. No per-shell toggles, no camera presets, no orbit-cache
  management. Built for Paloma and casual visitors, not for the depth of
  control the desktop offers.
- **Axis control gap** — L-041 (orrery-side dtick/range) is closed; L-040
  (the Studio/web equivalent) is still open. A real, currently-open
  capability gap on the interactive side specifically.
- **One capability flows the other direction:** DP-thinning (DouglasPeucker
  trajectory-point thinning for the served cache) is gallery-side
  infrastructure the desktop doesn't have and doesn't need — the desktop
  could borrow it later if useful. Worth remembering this isn't purely
  "orrery has more" — it's mostly narrower, with at least one place where
  the interactive side built something first.

## 3. Build order — 7 golden artifacts, fully resolved

Ordered by both complexity and commonality/usefulness to actual visitors —
these don't always point the same way, and commonality wins where they
conflict. **None of the seven depend on any open design question** — this
is the key change from v0.1 (see Section 4 for what dissolved and why).

1. **Earth alone** — the floor case: does the assembler place one object
   correctly at all.
2. **Jupiter, Saturn** — adds shells (magnetosphere, ring_system on top of
   Earth's van_allen_belts/atmosphere_shell) — real complexity, but visual,
   not fetch.
3. **Moon, Io, Titan** — parent-relative frames. Same fetch mechanism as
   1-2, just a different `canonical_center` string (see transform-retirement
   note, Section 4) — checked for confirmation, not because they're harder.
4. **Halley, Encke** — comets, grouped, but two different kinds of evidence
   in one step: Halley by Mode-5 desktop comparison (it exists in
   `celestial_objects.py`); Encke by the add-object/pinning path (no desktop
   reference exists for it — that absence is exactly its value as a test).
5. **Voyager 1** — spacecraft trace (glide + event-window-densified arc).
   Hard part already proven end-to-end at the data layer in Phase 1b's live
   gate (2026-07-11) — this artifact is rendering already-solved data, not
   solving anything new. Scope note: this is the *trace only* — flyby
   close-up views are a later enhancement, not part of this artifact (see
   Section 4).
6. **Pluto, Charon** — verified this session to be existing, working,
   already-consistent orrery code (wide heliocentric view + a separate
   barycenter-mode detail view, both pre-built), not new architecture. Port
   the existing pattern; nothing to design.
7. **Halley + event_link marker** — small in scope: place a link marker
   coincident with Halley's existing perihelion marker, prove the link
   resolves to the right static exhibit. Establishes the general pattern for
   every comet at once (automatic, no curation needed — see the L-104 ledger
   note). Does not touch OQ-4 or closeup-shape at all — those questions
   belong to a separate, deferred track (Section 4).

## 4. What dissolved this session, and why (context for whoever builds this)

v0.1 carried three real open design questions into Opus's review — a
"keystone" Pluto/closeup composition question, OQ-4 (preset precedence), and
closeup-view shape. All three turned out not to gate the 7 artifacts above.
Worth understanding why, since it shapes what's actually being asked of a
manifest here: **build against a design that's genuinely settled, not one
where open questions were argued away to hit a deadline.**

- **Transforms are retired except as fallback.** Osculating elements +
  vectors are fetched directly at each object's `canonical_center` for every
  object now — planets and moons alike. This is what makes Moon/Io/Titan
  "same mechanism, different center string" rather than a harder case.
- **Pluto/Charon's "keystone" dissolved entirely.** Initially thought to
  need new dual-fetch composition architecture. Verified directly: the
  orrery already has both a wide heliocentric view (Pluto plotted normally,
  nothing else shown) and a separate barycenter-mode detail view (barycenter
  rendered as its own marker, using the general `object_type: 'barycenter'`
  -> `symbol: 'square-open'` convention already applied consistently across
  the whole catalog — not special-cased for Pluto). Two existing modes, not
  one new composition problem. This also means the hypothesized shared
  mechanism with closeup-view (below) doesn't hold — Pluto's solution is a
  mode *selection*, closeup is a paired overview+zoom *composition*.
  Different shapes.
- **Halley's apparition reasoning, refined by Opus's review:** not "only one
  apparition literally exists" — it's that new apparition solutions get
  added rarely enough (~76-year cadence) that the current record stays
  stable and unambiguous for decades, unlike Encke's ~3.3-year churn. Same
  conclusion (`90000030` is correct, no live search needed), more precise
  mechanism.
- **OQ-4 and closeup-shape turned out to belong to a different, separate
  system than this build.** Two distinct preset mechanisms exist in this
  project: the live scene-spec `preset_id` vocabulary (where OQ-4/closeup
  actually live) versus static Gallery Studio exhibits linked from the
  interactive via an `event_link` marker (L-046/L-104's track). Apophis's
  "close encounter" — the thing that originally seemed to need OQ-4 and
  closeup-shape resolved — turned out to be a Studio-authored static exhibit
  problem, not a live-assembler problem. It was dropped from the 7-artifact
  sequence entirely once that was clear; see the L-104 ledger note for where
  that work now lives.

## 5. Object-cache expansion procedure (for adding beyond the 7 artifacts)

Reuse before inventing — `celestial_objects.py` (~179 objects) already
carries `horizons_id`, `id_type`, and (for comets/spacecraft) start/end
dates for most candidates; `shell_configs.py` carries per-planet shell
definitions mapping to gallery `features`. Verified directly: Voyager 1's
orrery entry (`id='-31'`, `id_type='id'`, `start_date=1977-09-06`) matches
the gallery config's Voyager 1 entry exactly — that's where it came from.

1. Look up the object in `celestial_objects.py` first. Copy `id` ->
   `horizons_id`, `id_type` (translate `None` -> `'majorbody'`), and any
   `start_date`/`end_date` for comets/spacecraft. Check `shell_configs.py`
   for shell `features` if applicable.
2. Author the gallery-specific fields fresh (no orrery counterpart):
   `parent`, `canonical_center`, `center_slug`, `canonical_frame`,
   `trace_policy`. Translate orrery `object_type` -> gallery `category`.
3. Periodic comets or ambiguous short-designation bodies: pin to the
   specific `900000XX` Horizons record (Encke/Halley pattern) —
   horizons-orbital-mechanics skill has the full rule.
4. Spacecraft flyby windows and comet Tp-anchor specifics are not reliably
   pre-existing in `spacecraft_encounters.py` — Voyager 1 there is only a
   commented-out template. These likely need real research even when the
   base object is already known.
5. **Required, not optional:** add a matching mock entry to
   `test_gallery_cache_builder_offline.py`'s `ELEMS` dict, keyed by the
   exact `horizons_id` — a missing key is a hard `KeyError` (the L-117
   failure class).
6. Run the offline suite from a clean checkout, then a `--dry-run --object
   <slug>` against real Horizons (writes only to `.staging`).
7. Run a real build with **`--first-build`, not `--nightly`** — only
   `first-build` mode fetches the full 365-day backfill window and carries
   the N3 floor check against a clipped fetch for non-spacecraft objects.

## 6. Watch item: Horizons date-window staleness

Hardcoded date-arc comments in `celestial_objects.py` (e.g. comet end-dates)
may be stale — Horizons solutions get refit with new observations over time.
No dedicated "give me the valid range" API call exists; the practical check
is a minimal probe query (single epoch) and reading the response for an
error vs. valid data, or the manual "Time Spans" tab in the Horizons web UI.
Treat old date-arc comments as unverified; re-check at the next dry-run that
touches the object.

## 7. L-080 — co-evolves with the build, not a front-loaded phase

A characterization harness needs real output to characterize; there is
currently none (Phase 0's pre-test is mean-element Keplerian math in
Pyodide, not assembler output), and Section 1's "no meaningful smaller
slice" finding means there's no cheap toy output to get first either.
Sequence: build far enough to render golden artifact 1 (Earth alone) ->
Mode-5 confirm -> draft L-080's first concrete criteria against that
confirmed scene, not in the abstract. From there, L-080 co-evolves with the
rest of the 7-artifact build — each confirmed step both advances the
assembler and hands the harness its next golden artifact. The
mainloop-suppression fixture and three existing test files (original L-080
proposal) need no real output and can be prepped in parallel at any time.

## Ref

MASTER_PLAN_INTERACTIVE_GALLERY.md v11 (Phase 2); PHASE1_SCENE_SPEC_VOCABULARY.md
(preset_id/window fields, OQ-2/OQ-4 — now understood as a separate system from
this build, see Section 4); L-079, L-087 (done), L-080, L-098 (closed parent),
L-107, L-111, L-040 (open), L-041 (closed), L-046, L-104 (deferred track, see
ledger); `data/objects_config.json` (gallery HEAD `a08bdd10`);
`celestial_objects.py`, `shell_configs.py`, `spacecraft_encounters.py`,
`close_approach_data.py`, `idealized_orbits.py`, `orbital_elements.py`,
`orbit_data_manager.py` (orrery HEAD `af58f7f`).

---
Session/entry written July 2026 with Anthropic's Claude Sonnet 5. Reviewed by
Claude Opus 4.8 (Mode 7 relay, v0.1). Consolidated into v0.2 following
extensive follow-up design conversation that resolved every question the
Opus review surfaced.
