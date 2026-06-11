# HANDOFF -- Animation Refactor 21/51, Phase 3 Session A (June 10, 2026)

Built on: orrery repo HEAD 8438a858d73511593019a64385c82a7a5edb9620 (verified
via git ls-remote; matches the SHA Tony supplied).
Deliverables: palomas_orrery.py + planet_visualization.py (3a patch),
measure_perframe_elements.py (new repo tool), ANIMATION_ENGINE_DESIGN_v1.md
(the Session-A design doc), two diff files vs HEAD.

Session A scope per the GO block: design doc + 3a warm-up patch + measurement
harness + rebuild-as-universal exploration. All four delivered. The design
answer to Tony's directive: **YES -- rebuild-per-frame works as the universal
strategy**, one contract, no translate machinery; details and the trace-count
stability invariant in ANIMATION_ENGINE_DESIGN_v1.md.

## A correction first (own the record)

My Phase-2 handoff and the June-10 ledger claimed the wrapper retirement was
"a ONE-SITE change." **That was wrong.** A repo-wide grep this session found
THREE live call sites: the consolidated dispatch helper (L2022) plus TWO in
the static planets_with_shells loop (center-fallback L4698 and non-center
L4712) that were outside Phase 2's scope and outside my Phase-2 re-grep.
"Verify universal-propagation claims with grep" applies to my own handoffs.
The ledger correction is below; all three sites are retired in this patch.

## What changed (8 hunks in palomas_orrery.py, 1 in planet_visualization.py)

WRAPPER RETIREMENT (Phase 2.5 / D.Structural 3), all three sites swapped to
create_celestial_body_visualization directly:
- Helper planet branch (~L2022): center body, center_object == body by
  construction -- live-tested IDENTICAL (T1/T2 below).
- Static center-fallback (~L4704): is_center implies equality -- identical.
- Static non-center (~L4723): now passes the TRUE
  center_object=center_object_name (the Phase-D correction the wrapper's own
  comment promised; the old hardcode claimed the body was the plot center).
  Live characterization (T3): for the representative non-center case the
  trace sets are IDENTICAL (16 == 16, no name diffs) -- center_object only
  bites in indicator-suppression edge geometry. [render-gated, risk ~nil]
- Dead import removed from palomas_orrery.py's import block.
- planet_visualization.py: wrapper docstring now opens with a RETIRED notice
  (zero pipeline callers; helpers' dead import noted; deletion rides the
  D.Structural 6 archive sweep per dead-code discipline). DO NOT add callers.

O2/O3 HONEST NO-OP NOTICES (3a), in animate after the dispatch (~L6260):
- Sun shells checked, planet-centered animation -> one console NOTE naming
  the gap and where they DO render.
- Non-center bodies with shells checked -> one console NOTE listing them.
Both say "Phase 3 scope" -- silence replaced with statement.

## Verification done (Claude-side)

- py_compile clean (3 files); ASCII-only; LF; hunks confined; sed swap on a
  throwaway copy only.
- LIVE tests in the real module namespace under xvfb (full GUI exec):
  T1 center-site swap: retired wrapper vs direct unified -- trace-for-trace
     IDENTICAL (names + coordinates).
  T2 helper planet branch post-swap == direct unified call -- identical.
  T3 non-center characterization: old hardcode vs Phase-D correction --
     identical sets for Earth-at-(0.7,0.7,0), Sun-centered (16 == 16,
     no only-in-old / only-in-new names).
  T4 O2/O3 notice conditions fire correctly (Mars center, Sun + Earth
     shells checked -> both notices, Earth listed).
- VERIFICATION LESSON (protocol candidate): `grep -c` exits 1 when the count
  is 0, which silently BREAKS an `&&` chain -- a downstream verification
  command can simply never run while the output looks complete. One residual
  check this session did not execute until re-run standalone. Rule: never
  put `grep -c` mid-chain with `&&`; run verification greps standalone or
  with `;`.

## The budget table (Decision 5a data; harness in repo, rerunnable)

First-cut primitives (committed per-frame):
  rotation axis 10.7 KB/f; dipole cone 19.5 KB/f; sun indicator 0.8 KB/f
  -> axis+cone per decorated body ~30 KB/f, ~0.9 MB @29f. Trivial.
Sun-direction customs: Mercury sodium tail 48.5 KB/f (500 particles;
  ~24.9 KB/f at 250) -> 1.4 MB @29f as-is. Affordable; particle knob exists.
Measured follow-on: Earth magnetosphere FULL 146.4 KB/f (4.25 MB @29f --
  too rich). REDUCED composite (belts 40x3, bow shock 15x15, envelope
  un-reduced): **62.4 KB/f -> 1.81 MB @29f. GATE 5(a) PASSES**, envelope
  reduction still in hand (~1.4 MB after the one remaining producer
  promotion). Gate 5(b) = Tony's Mode-5 quality judgment at the follow-on.

Session-A findings that SHRANK the resolution-sweep estimate: the bow-shock
conic producer is ALREADY parameterized (n_phi/n_theta); the magnetosphere
envelope comes from one shared producer (create_magnetosphere_shape) whose
single promotion propagates to every body. Per-body work reduces to local
density literals (belts, particle counts) + one dispatch flag.

## Mode-5 checklist (Session A render gate -- light)

Static:
  [ ] Shells-on center plot (e.g. Earth center + magnetosphere): unchanged
      (T1/T2 say identical; confirm by eye).
  [ ] NON-CENTER shells static plot (e.g. Sun-centered, Earth magnetosphere
      checked): renders as before -- shells at Earth's position, sun-direction
      indicator behavior unchanged (T3 says identical; this is the one
      formally render-gated swap).
Animate:
  [ ] Earth-centered animation with SUN shells checked: console NOTE appears;
      render otherwise unchanged.
  [ ] Sun-centered animation with Earth magnetosphere checked: console NOTE
      lists Earth; render otherwise unchanged.
  [ ] One P3-style regression run: center marker + shells + payload as in
      Phase 2 (nothing here touched frames).

## Ledger-ready updates

- D.Structural 3 (retire create_planet_visualization): RETIRED at all THREE
  call sites this session `[render-gated on the checklist]`; wrapper
  annotated dead; deletion joins D.Structural 6. CORRECT the June-10 entry:
  the "exactly ONE live pipeline call site" claim was wrong (three sites;
  grep-confirmed this session). The helpers dead import joins D.Structural
  5/6 (file is also the CRLF item 9).
- 21/51 Phase 3: Session A DONE (design doc + 3a + harness + budget table).
  Rebuild-as-universal ADOPTED as engine strategy. Gate 5(a) PASSED at the
  measured reduction; 5(b) pending at the follow-on. O2/O3 no-ops now
  noticed, not silent.
- Section G: the animation auto-scale question moves from standalone
  decision to Session C consolidation scope (per Decision 3) -- the engine
  computes axis_range from orbital + shell + element extents under Auto.
- NEW protocol candidates (section A list): the grep -c chain-break rule.
- NEXT: Session B (engine + first customers: axis, cone, sun indicator),
  per ANIMATION_ENGINE_DESIGN_v1.md section 10; protocol v3 issues with it.

Module updated: June 2026 with Anthropic's Claude Fable 5
