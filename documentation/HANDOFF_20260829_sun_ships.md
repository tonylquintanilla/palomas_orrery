# HANDOFF 2026-08-29 -- the Sun ships, and what shipping it found

**Built on orrery `688561ef63706cefcac981e381d794c324033432` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `ac9a5c7baf108b4c90a32ed5c80235e4a1c8625a` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both confirmed against the live remote 2026-08-29.**

Session base was orrery `071a0a65` / gallery `833daa9a`. Six patches
landed and pushed. One is delivered and unrun.

---

## READ THIS FIRST -- three carried obligations

**1. `provenance-discipline` went 2.9 -> 2.10 in this session, which
cannot clear its own reinstall.** The session that wrote 2.10 loaded 2.9
and stayed on 2.9; a reinstall lands in the account and is invisible to
a running conversation.

**The next session confirms its loaded copy reads 2.10 before doing any
provenance work.** If it reads 2.9 or lower, stop and reconcile -- do
not proceed and mention it afterwards.

**2. One patch is delivered and NOT run.**
`patch_master_plan_v20_sun_ships.py` -- the two plan documents. Guarded
against orrery `688561ef`. If anything else has edited either document
since, its guard will refuse and it must be re-cut.

**3. Three ledger edits are owed and none was patched**, because the
ledger's fingerprint depends on whether `ledger_index.py` has run since,
and guessing would make a patch refuse for the wrong reason. They are
listed under "What is owed" below.

---

## THE HEADLINE

**The Sun is live on the public gallery**, at

    palomasorrery.com/interactive.html?exhibit=sun

Unlinked from the landing page, carrying inline credit, Mode 5 accepted
by Tony 2026-08-29. Eighteen shells from the core to the Sun's
gravitational influence at 150,000 AU, each carrying its source in its
hover text.

What is new is not the picture. It is that the shared Python assembler
ran **in a visitor's browser**, against the served cache, and handed its
feature report to JavaScript to draw. That is architecture B' and
Section 3a's Python-assembles / JavaScript-draws split, working end to
end outside Tony's machine for the first time.

It is a SECOND exhibit on the page that has been public since July,
reached by the `?exhibit=` parameter Section 2a designed for exactly
this. The Solar System Explorer is untouched and is still what loads
with no parameter. Nothing was promoted from a dev page.

---

## What landed and is pushed

| Item | Repo | State |
|---|---|---|
| `.nojekyll` at the repo root | gallery | RUN, pushed `833daa9a` |
| `patch_sun_exhibit_interactive_html.py` | gallery | RUN. 6 edits |
| `patch_sun_exhibit_rescale.py` | gallery | RUN. 2 files, 5 edits |
| `patch_L258_significant_figures_at_rest.py` | orrery | RUN. 2 files, 4 edits |
| `skills_index.py` | orrery | RUN. Caught 2.9 -> 2.10 and said so |
| `patch_objects_config_L258_carry.py` | gallery | RUN. 2 edits |
| `patch_sun_modebar_and_credit.py` | gallery | RUN. 2 edits |
| `patch_master_plan_v20_sun_ships.py` | orrery | **DELIVERED, NOT RUN** |

**Verified in the published bytes**, not from the patches' own reports:
`interactive.html` at gallery `ac9a5c7b` carries `toImageButtonOptions`,
`displaylogo: true` and the new credit line; the served
`coverage_index.json` carries `radiative.radius.value = 0.713` and the
Lamy citation; both `.py` files under `gallery/assembler/` return
content rather than a 404 page.

---

## The four defects, and three of them nothing could have caught

**GitHub Pages was serving no `.py` file in the repository at all.**
Pages runs Jekyll by default; there was no `.nojekyll`; the entire
`gallery/assembler/` directory returned 404. It worked perfectly over
`python -m http.server`, which is where every previous test had run, so
the failure was invisible to the whole existing test surface. One empty
file fixed it.

The prediction that found it was narrower than the truth -- Jekyll drops
underscore-prefixed names, so `__init__.py` was expected to 404 and
`resolver.py` was not. Both did. The wider fix was right for a reason
the prediction had not identified, which is worth remembering: the
diagnosis was partly wrong and the remedy was still correct.

**The scene axes were pinned**, so nothing the legend did could move the
frame. A visitor turning on the heliopause at 121 AU inside a
quarter-AU box saw the page do nothing. Caught by Tony's render, against
a code reading that said otherwise, which is the resident gate working.

**Nine info markers were being drawn with no shells around them.** Each
shell is two traces -- geometry carrying `hoverinfo: "skip"`, and one
info marker carrying the hover. `feature_renderers.js` sent the geometry
to the legend when a shell exceeded the frame and left its marker
behind, so markers sat at 94 AU through 150,000 AU, hoverable, alone.
Invisible only because the pinned axes fell inside them. **This defect
predates the Sun exhibit and is in the shared renderer**, so Earth's
shells would have hit it too. Fixed in the producer.

It was surfaced by fixing the second defect: making the frame follow the
data made the strays visible by blowing the frame out to 173,250 AU.
Fixing an invisible thing surfaces its neighbours.

**And segment 2 failed in its first real test.** See below; it is the
one with consequences beyond this session.

---

## Segment 2 is no longer theoretical

`RADIATIVE_ZONE_AU` was corrected in the orrery, committed, pushed, and
the gallery cache builder re-run. **The site went on serving 0.7.**

The builder passes feature constants THROUGH from
`data/objects_config.json`, a hand copy living in the gallery repo. It
has never read `constants_new.py`. Fetch-and-import -- the transport
that would have it resolve the orrery HEAD SHA and read the store
directly -- was RATIFIED 2026-08-08 (master plan Section 7, decision 12)
and never built.

The instruction "re-run the builder and it will pick up the new value"
was WRONG, and the builder ran clean while doing exactly what it was
built to do. The value reached the site by a hand patch to
`objects_config.json`. That is not a workaround; it is the current
architecture.

The 2026-08-28 handoff predicted this in the abstract -- "it is not a
defence against later drift, it IS the gate's missing enforcement
point." It failed the following day, in its first real exercise.

**It does not gate the next exhibit.** It should be built before the
ladder gets long enough that hand-copying many bodies becomes routine,
because every body added multiplies the surface.

---

## The Mode 5 claim, narrowed

Section 5a and the critical path both justify the braid's ordering with
a sentence saying a wrong radius "becomes something Tony's EYES can
catch." Fable's review of 2026-08-27 contradicted it. This session
produced the case.

`RADIATIVE_ZONE_AU` moved 0.7 -> 0.713: **1.9 percent of a drawn
radius, invisible at any zoom.** It was caught on the live page -- by
READING THE HOVER TEXT, not by seeing the shell.

So the argument survives and the mechanism was misnamed. The geometry
catches gross errors: a wrong frame, a factor of two, a body in the
wrong place. The HOVER catches everything else, because it carries the
value, the units and the source. Drawing a feature is what puts its
provenance in front of a reader for the first time. That is the half
worth designing for.

Corrected in both documents by the unrun patch.

---

## What is owed

**Three ledger edits.** None was patched, deliberately.

1. **L-258 has no entry.** It covers the significant-figures rule
   (provenance-discipline 2.10), `RADIATIVE_ZONE_AU` 0.7 -> 0.713 with
   its citation restated, `INNER_CORONA_RADII` re-homed from Golub &
   Pasachoff to Lamy et al. with the value unchanged, and three
   `# Cross-checked:` legs retired. All four are already annotated in
   `constants_new.py`; the handle needs its block.
2. **The Sun exhibit has no handle at all.** It was captured on first
   mention in the 2026-08-28 handoff and never minted.
3. **L-256's block still lacks its 2.9 line**, owed since 2026-08-28,
   and now also a 2.10 line.

**Two RICE scores still await confirmation or redirect** -- L-256
(3/3/70/2) and L-257 (2/3/60/2), both Claude's proposals, open since
2026-08-27.

**Seventeen of the Sun's nineteen values have no `# Status:` line.**
Two got one during this session because they were being edited anyway.
The status-pass beta is otherwise where the 2026-08-28 handoff left it,
and it is still blocked on one ruling: **which dict joins the beta**,
`spectral_subclass_temps` (9 entries) or `CENTER_BODY_RADII` (18).

**The rendering ladder is still unwritten into the master plan.** The
draft is at `documentation/DRAFT_rendering_ladder_section.md`. Four
amendments are owed from the Mode 7 reviews: a definition of
*published*, a per-step slice denominator stated before the step
starts, a whole-published-set revalidation sweep on every build, and the
transport hole -- which is now sharper than the reviews had it, per the
section above.

Its step 1 is also superseded. It reads "render the Sun as is, and
look," a local render explicitly not a publication. Tony declined that
intermediate step on 2026-08-28 and the Sun went straight to the live
page, so step 1 becomes the shipped exhibit and the local-look framing
goes.

**The golden-artifact mechanism is unrepaired**, unchanged from the
2026-08-28 handoff: the harness compares today's assembly to itself,
three of fourteen fields change on every nightly build by design, and
the position tolerance is `0.001` RELATIVE -- about 150,000 km at
Earth's distance.

**L-257's three enforcement builds are unstarted.** The worksheet schema
does not require `quote` and `locator`; nothing parses `# Status:`; the
scanner still infers.

---

## Two measurements corrected

**The Sun has 18 drawable shells, not 19.** Measured through the real
renderer at gallery `ac9a5c7b`: 18 named traces plus 18 info-marker
companions. The master plan's 2026-08-25 append says 19. Corrected by
the unrun patch. Every count of "the Sun's nineteen values" elsewhere
refers to `constants_new.py` entries, which is a different denominator
and is not affected.

**The modebar is full on this exhibit and absent on mobile.** Nothing is
removed -- image capture and the Plotly credit are both on, and
`toImageButtonOptions` names the file and doubles the pixel dimensions.
The 768 px breakpoint is untouched, so the bar does not appear on a
phone. That is the gallery's existing convention, not a judgement about
the menu; `displayModeBar: true` changes it if wanted.

---

## Process notes, recorded not smoothed

**A wrong instruction, and the guard that did not exist.** "Re-run the
cache builder and it will pick up the new value" was asserted from a
mental model of the pipeline rather than from reading it. The builder
had no way to do that and never had. Nothing in the routine would have
caught the claim; Tony caught it by looking at the hover.

**An overreach, withdrawn.** Golub & Pasachoff was carried from the
`HELMET_CUSP_RADII` finding to `INNER_CORONA_RADII` as though the
earlier removal transferred. It does not: the store's own note says that
read "was decisive about what to REMOVE and silent about what to KEEP,"
and it was about helmet-streamer extent, a different claim. The
citation still moved, on the narrower and correct ground that the work
is unreachable under the access standard.

**A ruling recalled correctly against a document that said otherwise.**
Tony's "I thought we had already decided on those three" was right about
`GRAVITATIONAL_INFLUENCE_AU`, which the store records as confirmed
2026-08-07 under L-179. The handoff's characterisation had been read
forward instead of the store being read -- one message after invoking
the status line as the fix for exactly that.

**A test harness artifact worth not misreading.** Piping a patch's
output to `head` killed it on SIGPIPE mid-print, before it wrote. It
looked like a silent failure and was not one. The patches write after
all verification, but they interleave writes with prints, so a signal
between two files could split a transaction. It cannot happen under the
VS Code Run button.

---

## Where the next session starts

**Housekeeping, short.**

1. Confirm the loaded `provenance-discipline` reads **2.10**. If lower,
   stop and reconcile.
2. SHA round trip on both repos. Orrery `688561ef`, gallery `ac9a5c7b`
   at the close of this session.
3. Run `patch_master_plan_v20_sun_ships.py`, then `ledger_index.py`,
   then `maintenance_run.py`.
4. Write the three ledger edits: L-258's block, a handle for the Sun
   exhibit, and L-256's 2.9 and 2.10 lines.

**Then one of three, and the choice is Tony's.**

**(a) The next ladder step -- Earth's existing shells.** The renderer
already handles `atmosphere_shell` and `van_allen_belts`, and both are
served. This is the cheapest visible increment and it exercises the
orphan-marker fix on a second body.

**(b) The transport, segment 2.** Now evidenced rather than argued. It
is the only place the export gate could ever fire, and every body added
to the ladder widens the hand-copy surface.

**(c) The status-pass beta.** Blocked on one ruling: which dict joins
it. The Sun's own values are partly closed already, so the remaining
job is the dict and the format proof.

**A note on reading order.** This document states final positions. Where
it does not cover something, `constants_new.py` settles it -- the store
is the authority and the narrative documents are backup. Do not
reconstruct any of this from the source conversation: it contains at
least four superseded states of its own, each stated before its
correction.

*Prepared 2026-08-29 with Anthropic's Claude Opus 5.*
