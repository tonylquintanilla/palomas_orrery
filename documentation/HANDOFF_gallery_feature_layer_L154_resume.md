# Handoff -- Resume L-154 (Gallery Feature-Rendering JS Layer) After the Provenance Detour

Tony Quintanilla, PE | Claude Sonnet 5 | July 23, 2026

**Built on:**
- gallery (tonyquintanilla.github.io) @ `79710968241f21c8e6e1836bb1ad35219f1a31f0`
- orrery (palomas_orrery) @ `9b4571851184e599f72de928cada16d30c9010f6`

**Type:** DESIGN SESSION (zero code) -- picks up exactly where the original
predesign conversation was, before it opened into the provenance/scoring
work. That whole detour is tracked separately (L-155 through L-162); this
handoff exists so the *original* thread doesn't get lost underneath it.

**Do not read this as needing the provenance work explained again.** If
you're picking this up, the provenance work should already be done or in
build. This document only covers L-154 itself.

---

## 1. What L-154 actually is

The client-side JavaScript that reads `ring_system`, `van_allen_belts`,
`atmosphere_shell`, and `radiation_belts` out of the served gallery cache
and draws them -- the one piece standing between here and attempting
Artifact 2 (Jupiter/Saturn) in the interactive gallery assembler.

**Already confirmed, not open:**
- Feature rendering is JavaScript, always -- a ratified architectural
  decision already in `assemble.py`'s own docstring (reversed once already
  from a synthesis error). Python resolves and reports which features
  apply and to which object; it never builds shell/ring trace geometry.
- The resolver bug (params silently dropped by `tuple(dict)` in
  `resolver.py`) is fixed and settled -- small, targeted, not an
  architecture question. (This was the loose thread that, while tracing
  where the params actually come from, led into the provenance detour.)
- Physical radius source: `constants_new.py`'s `CENTER_BODY_RADII`
  (now with all bodies individually named, per L-162) -- ported into
  `objects_config.json` as data, not a separate JS constants table.

---

## 2. The three open design questions -- exactly as left

**1. Geometry-building approach.** Port the orrery's existing shell/belt/
ring drawing math (the `SHELL_CONFIGS` / `*_visualization_shells.py`
pattern -- concentric-sphere loops for belts, parametric surfaces for
atmosphere shells) into JS fairly literally, or design fresh JS-native
trace builders that hit the same visual result without mirroring the
Python line-by-line. The project's own stated principle applies directly
here: "knowledge transfers, not code" (see resident protocol, Foundation,
"The Orrery and the Assembler").

**2. Legend/toggle behavior.** Should a planet's shells/rings/belts share
its `legendgroup` silently (toggle together with the planet, no separate
legend rows), or get their own independently-toggleable legend entries?
The Python-side per-object traces already use `legendgroup = obj.slug`
(`assemble.py`) -- the open question is only whether JS-added feature
traces follow that same grouping, and whether they're visible as their
own rows or folded silently under the parent.

**3. Sequencing.** Validate the JS feature layer against Earth's already-
Mode-5-closed harness first (lower risk -- Earth already has real
`atmosphere_shell` + `van_allen_belts` data, adds shells to a known-good
baseline), or build straight into Jupiter/Saturn's rings since that's
what's actually gating Artifact 2 either way. Building on Earth first
means proving the JS mechanism once, cheaply, before also taking on new
geometry (rings are a new shape -- an equatorial disk, not a shell) at the
same time.

No recommendation was converged on for any of the three -- this is
presented as three genuine, still-open branches with real tradeoffs, per
this project's own "propose options, let judgment drive convergence"
convention. Whoever resumes this should treat it as a live design
conversation, not a checklist to close mechanically.

---

## 3. What changed underneath L-154 while it was blocked

Nothing that reopens the three questions above. Worth knowing, briefly:

- `objects_config.json`'s `features` block is unchanged in shape; the
  params flow correctly once the resolver fix lands (L-154's own settled
  item, unaffected by the provenance work).
- The physical-radius values L-154 will read are now individually
  Gemini-verifiable per body (L-162's promotion), not bundled in one
  dict-level citation -- doesn't change how the JS reads them, just
  strengthens what's behind the numbers.
- If L-161's Gemini sweep of shell config values (ring/belt/atmosphere
  geometry) is done or underway by the time this resumes, the numbers
  L-154's JS will draw have more confidence behind them than they did
  when this thread paused -- not a design change, just better-grounded
  data underneath the same design questions.

---

## 4. Suggested next step when this resumes

Pick up at question 1 (geometry-building approach) first -- it's the one
most likely to affect the answer to question 3 (sequencing), since a
"port the orrery math literally" approach is lower-risk to prove on
Earth's small, closed harness, while a "design fresh JS-native" approach
might reasonably want to prove itself against the more complex Jupiter/
Saturn geometry directly, where the payoff is bigger. That dependency
wasn't explicitly worked out before the detour opened -- worth surfacing
early in the resumed conversation rather than assuming an order.

---

*Handoff written July 2026 with Anthropic's Claude Sonnet 5.*
