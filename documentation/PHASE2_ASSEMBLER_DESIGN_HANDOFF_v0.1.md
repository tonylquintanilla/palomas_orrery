# Phase 2 — Solar System Assembler: Preliminary Design Handoff v0.1

**Type:** DESIGN SESSION (zero code)
**Built on:** orrery HEAD `5cbbadab99d2a87b65f988c63069c64d95318688`, gallery HEAD
`a08bdd10769f93d7d42601c76fcc14786251ef05` (both reconfirmed live; unchanged
since Phase 1b close, 2026-07-12)
**Companion:** MASTER_PLAN_INTERACTIVE_GALLERY.md v11 (Phase 2 section)
**Parent:** L-079 (shared assembler architecture, keystone)
**Supersedes:** nothing yet — first Phase 2 design pass since L-098 closed

---

## 1. Where we stand (verified, not just claimed)

- **Phase 1b (L-098) is CLOSED**, verified live at orrery HEAD `5cbbadab9`:
  L-098 / L-106 / L-108 / L-117 all show `status:DONE section:C`; the master
  plan Status line matches. This was cross-checked against HEAD directly,
  not taken from the closing handoff's claim alone.
- **L-115 / L-116 are done in substance but still tagged `status:OPEN`.**
  All five Move-1 skill edits and the new gallery-cache-builder skill (Move
  2) are verified live and installed — version-bumped to 1.1 where
  specified, correctly re-pinned to `e83fe9ce`. This is a ledger-lag, not a
  code gap. **Recommend flipping both to DONE at the next ledger touch** —
  pure bookkeeping, low effort, restores signal.
- **L-079's own Gap note is stale.** It still reads "current phase: Phase 1b
  build (L-098)" — needs updating to Phase 2 now that L-098 is closed.

## 2. Decisions reached this session

- **Scope: the full assembler, not a planets-only build.** Reaffirmed the
  standing rationale from the original architecture design: a basic scene
  already exercises nearly all the orchestration (object selection, center
  resolution, shell dispatch, hover composition, camera, axes, figure
  assembly) — there is no meaningful smaller code slice. "Planets only"
  would still require building nearly the whole assembler, so it doesn't
  buy a simpler build.
- **Verification target: the existing gallery test config plus Halley,
  grouped into 7 golden artifacts (see build order below) — not a new set
  of objects, but real thematic grouping by both complexity and
  commonality.** The `data/objects_config.json` set already covers every
  pattern the assembler needs to prove out. **Correction (this session):** transforms
  (deriving a moon's position by differencing) are retired except as a
  fallback — osculating elements + vectors are fetched directly at each
  object's `canonical_center` for every object now, planets and moons
  alike. So the fetch mechanism for Moon/Io/Titan/Pluto/Charon is the same
  as for Earth/Jupiter/Saturn, just a different center string — not a
  harder case. The real complexity drivers are shells, smallbody/comet
  handling, and spacecraft trace policy:
  - Earth, Jupiter, Saturn — heliocentric, plus shells (van_allen_belts,
    magnetosphere, ring_system, atmosphere_shell) — real complexity, but
    visual, not fetch
  - Moon, Io, Titan — same fetch mechanism as the planets, different
    `canonical_center` string; checked for confirmation, not because
    they're harder
  - Pluto, Charon — **more complex than the above, corrected this
    session.** Verified in `idealized_orbits.py`/`orbit_data_manager.py`:
    Pluto's ID (`999`) defaults to `@sun` (real ~39 AU heliocentric orbit),
    while the current gallery config fetches it at `@9` (the barycenter —
    only the tiny ~0.0000142 AU local wobble). The config's existing entry
    captures the local detail only, not the wide-view anchor that would
    place Pluto correctly among the other planets. Likely needs two
    composed fetches (barycenter `9 @ sun` for the wide anchor + `999`/
    `901 @ 9` for local detail), not one — genuinely harder than a plain
    parent-relative moon, and this resolves (rather than leaves open) the
    residual `canonical_frame` question flagged earlier. Earth-Moon avoids
    this because the config anchors Earth directly and treats Moon as
    simple parent-relative, sidestepping the Earth-Moon Barycenter entry
    entirely — Pluto/Charon's mass ratio is what forces the barycenter to
    matter here.
  - Apophis — smallbody `id_type`, heliocentric fetch is simple, but see
    the reframing below: verifying it as a *close encounter* (its actual
    purpose) is not simple
  - Halley — **added this session; the pin is fine, my previous correction
    overcorrected.** Encke has no desktop presence at all (confirmed: no
    entry in `celestial_objects.py`), so it can't be Mode-5 compared
    against anything; Halley is in `celestial_objects.py` (`id='90000030'`)
    so it's Mode-5-comparable. The Encke lesson (each apparition is a
    separate Horizons record, ambiguous without pinning) does NOT transfer
    directly: Encke's ~3.3-year period means a new apparition record
    appears every few years, so picking the current one matters. Halley's
    ~76-year period means only ONE apparition is active right now — the
    orrery's own `mission_info` states it plainly ("returned in 1986 and
    will return in 2061"). There's no competing, more-recent record to
    search for; `90000030` is necessarily still the current one. No live
    disambiguation query needed. Light caveat only: the comment's stated
    end date (`1994-01-11`) describes the observational fit-arc used to
    derive the elements, not a hard propagation cutoff — Halley is a very
    well-characterized orbit, so a 2026 query is a normal extrapolation,
    not a stretch. Still gets the same routine dry-run check any newly
    added object gets — not a special record search.
  - Encke — pinned-record comet, Tp-anchored conic, elliptical/hyperbolic
    orbit-type branch — genuinely more machinery; kept for the add-object
    test, not for Mode-5 comet comparison
  - Voyager 1 — spacecraft, full-arc trace policy + flyby windows (hardest
    case, unaffected by the transform correction)

**Build/verification order — revised this session (commonality, not just
complexity).** Complexity alone isn't the right single axis: how common and
useful an object is to actual visitors matters too, even where it cuts
against technical difficulty. Tony's revised order, 7 golden artifacts
across the 12 objects:

1. Earth alone — the floor case
2. Jupiter, Saturn — shells, grouped
3. Moon, Io, Titan — parent-relative, grouped
4. Halley, Encke — comets, grouped, but carrying two *different* kinds of
   verification in one step: Halley by Mode-5 desktop comparison, Encke by
   the add-object/pinning path (no desktop reference exists for it)
5. Voyager 1 — spacecraft
6. Pluto, Charon (+ the barycenter fetch) — the dual-fetch composition case
7. Apophis — reframed as the *close-encounter* case, not a plain smallbody.
   Its actual purpose is demonstrating a close approach, which depends on
   OQ-4 and the closeup-view shape (Section 3) — both still unresolved.
   Realistically the last one buildable, not because the fetch is hard but
   because the design it depends on isn't settled yet.

Supporting reasoning for Voyager ahead of Pluto/Charon despite Pluto/
Charon's technical complexity finding above: Voyager's hard part (glide +
event-window densify + DP-thinning) was already proven end-to-end at the
data layer during Phase 1b's live gate (2026-07-11) — what's left for the
assembler is rendering already-solved data. Pluto/Charon's dual-fetch
*composition* is a genuinely unsolved architecture question, not yet
attempted anywhere in the codebase — arguably the newer problem of the two.

One open question worth flagging, not resolving here: Pluto/Charon's need
(compose a wide heliocentric anchor + a local offset into one scene
position) and the closeup-view need (a second, differently-scaled scene
re-centered on the encountered body) are both cases of "one visual object
needs more than one fetch/view composed together." Worth checking, when
either gets built, whether they're actually the same underlying mechanism
or genuinely separate — solving one might solve both, might not. Not
asserted either way.
- **Object-cache expansion is explicitly deferred, fully decoupled from
  this track.** `gallery_cache_builder.py` is standalone by design (L-107)
  — adding objects never blocks or depends on assembler progress. Procedure
  captured below for whenever it's next needed.
- **No need for unattended nightly scheduling (L-111) at this stage.** The
  current object set is a manually-run testing group; L-111's
  correctness/operability hardening (gap-aware catch-up, `_health.md`,
  `--add-object`) only matters once runs go unattended. Revisit when
  scaling past manual supervision.

## 3. Open design question: encounter presets and closeup views

Surfaced this session, not resolved — needs a ruling before encounter-preset
tooling is built.

**What's already covered.** The Phase 1 vocabulary document already gives
fixed-date presets a home: `preset_id` expands into `epoch`/`window` at
assembly time ("encounter presets override this to closest-approach time —
preset expansion WRITES this field"). The current Studio-generated fixed
date window carries over as-is; nothing to invent there.

**OQ-4 (blocking, per the vocabulary doc itself).** When `preset_id` is set
and explicit fields are also present, does the preset win, do explicit
fields override it ("preset-as-defaults"), or is mixing disallowed
("strict")? The doc's own text: *"needs a ruling before tier-2 export
tooling exists."* Strict reproduces today's frozen Studio export, just
computed live. Preset-as-defaults additionally lets a visitor nudge the date
around closest approach or toggle a shell — real new capability, not yet
decided.

**Closeup views — a genuine vocabulary gap, not a camera setting.** Tony's
correction this session: a closeup isn't a zoomed camera on the same scene
— it's needed precisely because Plotly's practical zoom range is exceeded
(the encounter geometry can be ~3 orders of magnitude smaller than the
overview's AU-scale range). The fix is a separate scene: different `center`
(re-centered on the encountered body, not the overview's center) and a
different axis range/scale. Verified directly in `spacecraft_encounters.py`:
the Voyager 1 template pairs an overview (`center: 'Sun'`, `plot_scale_au:
8.0`) with a `center_closeup: 'Jupiter'`, `plot_scale_au_closeup: 0.1` —
same time window, different center and scale entirely. Neither a closeup
sub-block nor `select_also` (the curated companion-object list in the same
template) exists in the current vocabulary; the closest related field,
`camera`, was explicitly deferred as OQ-2.

**Dependency, not a fresh problem.** Rendering a closeup correctly needs
real auto-range-to-local-scale + user-settable dtick — this is already
tracked, open, on the Studio/cross-repo side as **L-040** (plot-cube control
parity + scaling/camera review). The orrery desktop side of this
(**L-041**) is already closed. The assembler will need L-040-equivalent
capability; worth building on that existing design rather than solving axis
scale fresh for the web.

**Open shape, not decided:** does a preset expand into one scene spec with
an optional nested `closeup` block (center + axis override), or into a
small ordered pair of scene specs (overview + closeup) the page toggles
between? Tradeoffs unexplored yet — flagging the question, not the answer.

## 4. Object-cache expansion procedure (captured for later, not scheduled now)

Reuse before inventing — `celestial_objects.py` (~179 objects) already
carries `horizons_id`, `id_type`, and (for comets/spacecraft) start/end
dates for most candidates; `shell_configs.py` carries the per-planet shell
definitions that map to gallery `features`. Verified directly: Voyager 1's
orrery entry (`id='-31'`, `id_type='id'`, `start_date=1977-09-06`) matches
the gallery config's Voyager 1 entry exactly — that's where it came from.

1. Look up the object in `celestial_objects.py` first. Copy `id` →
   `horizons_id`, `id_type` (translate `None` → `'majorbody'`), and any
   `start_date`/`end_date` for comets/spacecraft. Check `shell_configs.py`
   for shell `features` if the object is a planet/moon with shells.
2. Author the gallery-specific fields fresh (no orrery counterpart):
   `parent`, `canonical_center`, `center_slug`, `canonical_frame`,
   `trace_policy`. Translate orrery `object_type` → gallery `category`
   (orbital/satellite/trajectory → planet/moon/asteroid/comet/spacecraft).
3. Periodic comets or ambiguous short-designation bodies: pin to the
   specific `900000XX` Horizons record (Encke/Halley pattern) —
   horizons-orbital-mechanics skill has the full rule.
4. Spacecraft flyby windows and comet Tp-anchor specifics are **not**
   reliably pre-existing in `spacecraft_encounters.py` — checked directly,
   Voyager 1 there is only a commented-out template, not active data. These
   likely need real research even when the base object is already known.
5. **Required, not optional:** add a matching mock entry to
   `test_gallery_cache_builder_offline.py`'s `ELEMS` dict, keyed by the
   exact `horizons_id` (plain dict lookup — a missing key is a hard
   `KeyError`, the same failure class L-117 already fixed once for Encke).
6. Run Layer 1 (`python3 tools/test_gallery_cache_builder_offline.py` from
   a clean checkout).
7. Run Layer 2 (`--dry-run --object <slug>` against real Horizons; writes
   only to `.staging`).
8. Run a real build with **`--first-build`, not `--nightly`** — verified in
   code: for non-spacecraft objects, only `first-build` mode fetches the
   full 365-day backfill window and carries the N3 floor check against a
   clipped fetch; `nightly` mode alone would onboard a new object with only
   a few days of data. (Spacecraft are the exception — a genuinely new one
   auto-backfills regardless of mode.) Note `--first-build` re-fetches
   every configured object, not just the new one — no scoped real-build
   option exists yet.

## 5. Watch item: Horizons date-window staleness

Tony's observation: JPL Horizons solutions may have expanded past some of
the hardcoded date-arc comments in `celestial_objects.py` (e.g. Hale-Bopp's
noted end date `2022-07-09` is now roughly four years old — comet data arcs
get extended as new observations are folded into refit solutions). Not
verified live this session (no Horizons access from this environment).
Horizons does expose a "Time Spans" lookup for the current valid range per
object in the web UI — that's the manual check. Programmatically, there's no
single dedicated "give me the valid range" call (the API docs are explicit
that out-of-range requests surface as an error inside a normal ephemeris
response, not as a separate lookup) — but a minimal probe query (single
epoch, few quantities) is a real, scriptable substitute: request the date in
question and check the response for an error vs. valid data. `OBJ_DATA='YES'`
on a normal query also returns solution metadata (solution date, # obs,
fit-arc) for small bodies specifically, which is likely where the old
hardcoded comments originated. Neither tested live from this environment
(no Horizons access here) — Tony's own manual web-UI check remains the
simplest path and is worth doing regardless of what a script could do; it
keeps a human in the loop on exactly the kind of assumption that goes stale
silently. **Action:** treat hardcoded date-arc comments and backfill-window
assumptions as unverified; re-check (manually or via probe query) at the
next dry-run that touches the object rather than trusting the comment. No
urgent action needed now — noted here so it isn't lost.

## 6. L-087 — helpers split (DONE)

- **What it was.** `palomas_orrery_helpers.py` imported tkinter directly
  (`tk`, `ttk`, `messagebox`, `scrolledtext` — lines 19-22), unused.
- **Finding (this session, double-verified):** every one of these imports
  was dead. Grepped the entire 913-line file for `tk.`/`ttk.`/`messagebox.`/
  `scrolledtext.` — zero matches anywhere in any function body; the four
  import lines were the only tkinter references in the file. Also checked
  the sole consumer, `palomas_orrery.py` — its import statement pulls
  exactly the 11 real functions the module defines, none of them tkinter
  names. Safe from both directions.
- **Executed.** Tony deleted the four dead imports directly — independently
  confirmed by VS Code's own unused-import graying before the edit, which
  lines up exactly with the grep finding. L-026 (CRLF→LF, same file) not
  confirmed done in this session — worth a quick check next time the file
  is open, since it was flagged as a natural one-pass companion.

## 7. L-080 — corrected sequencing, not a front-loaded phase

**Correction (this session): L-080 cannot precede the assembler build.**
Previously framed as "design alongside or shortly after L-087, before the
assembler build starts" — that's backwards. A characterization harness
needs real output to characterize; right now the only visualization that
exists is the Phase 0 pre-test (Pyodide + mean-element Keplerian math), which
isn't assembler output and has nothing to do with scene-equivalence criteria.
Combined with the standing design fact from Section 2 (no meaningful smaller
slice of the assembler — a basic scene already exercises nearly all the
orchestration), there's no way to get a toy first output cheaply either:
getting *any* real scene means building most of the assembler.

**Corrected sequence:** L-087 (done) → build the assembler far enough to
render golden artifact 1 (Earth alone, per Section 2's revised order) →
Mode-5 confirm that first real output → draft L-080's first concrete
criteria against that confirmed scene, not in the abstract. From there,
L-080 stops being a separate phase and co-evolves with the rest of the
7-artifact build-up (Jupiter/Saturn → Moon/Io/Titan → Halley/Encke →
Voyager 1 → Pluto/Charon → Apophis) — each confirmed step both advances the
assembler and hands the harness its next golden artifact.

**Still true from before:** the mainloop-suppression fixture and three
existing test files (per the original L-080 proposal) can be folded in
whenever the harness build actually starts — that groundwork doesn't need
real assembler output to prepare.

## Gap / next session

- [ ] Flip L-115 / L-116 to DONE (bookkeeping only)
- [ ] Update L-079's Gap note to point at Phase 2
- [ ] Rule on OQ-4 (preset-as-defaults vs. strict) before encounter-preset tooling
- [ ] Decide closeup-view shape (nested block vs. paired scene specs); connect to L-040
- [ ] Resolve Pluto/Charon's dual-fetch need (barycenter-as-anchor + local detail) before Mode-5 verifying that case
- [ ] Add Halley to `objects_config.json` via the standard add-object procedure (Section 4) — `90000030` is the correct current record (76-year period, only one apparition active), routine dry-run check only, no record search needed
- [x] L-087 executed (Tony deleted the 4 dead tkinter imports directly)
- [ ] Confirm L-026 (CRLF→LF, same file) — not verified done this session
- [ ] Build the assembler far enough for golden artifact 1 (Earth alone); Mode-5 confirm
- [ ] Draft L-080's first concrete criteria against that confirmed scene — not before there's real output to characterize
- [ ] Continue through the 7-artifact order (Jupiter/Saturn → Moon/Io/Titan → Halley/Encke → Voyager 1 → Pluto/Charon → Apophis), each step feeding the harness a new golden artifact
- [ ] Apophis (artifact 7) needs OQ-4 and the closeup-view shape (Section 3) resolved first — it's the close-encounter case, not a plain smallbody
- [ ] Check whether Pluto/Charon's dual-fetch composition and the closeup-view mechanism turn out to be the same underlying solution or genuinely separate — open, not yet explored

## Ref

MASTER_PLAN_INTERACTIVE_GALLERY.md v11 (Phase 2); PHASE1_SCENE_SPEC_VOCABULARY.md
(OQ-2, OQ-4, `preset_id`/`window` fields); L-079, L-087, L-080, L-098
(closed parent), L-107, L-111 (deferred), L-040 (open, Studio axis/scaling
parity), L-041 (closed, orrery-side axis control); `data/objects_config.json`
(gallery HEAD `a08bdd10`); `celestial_objects.py`, `shell_configs.py`,
`spacecraft_encounters.py` (orrery HEAD `5cbbadab9`).

---
Session/entry written July 2026 with Anthropic's Claude Sonnet 5.
