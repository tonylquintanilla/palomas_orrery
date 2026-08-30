# HANDOFF -- 2026-08-29 night: the Sun exhibit finished, and the
# gallery gets a runner

**Built on** orrery `bfa9de2fc0b9c2d30c9eb4de27828a8c2b4c8535` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `6c6123974e883a461a92b586b8352c9c535ee8d1` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote at the close of the session.

**Type:** BUILD.

**Companion to** `documentation/HANDOFF_20260829_sun_ships.md`, which
records the ship itself earlier the same day. That document is not
superseded; this one continues from it.

---

## What was done

Everything below was measured, not carried. Where a figure came from a
document rather than a run, it says so.

**The Sun exhibit is finished on its visible surface.** The axes carry
X (AU), Y (AU), Z (AU), using the desktop orrery's own wording from
`build_scene_axes` in `visualization_utils.py`. Tony's Mode 5 read of
the deployed page confirmed both the defect and the fix. The Solar
System Explorer's `buildLayout` has the same blank titles and was left
alone: it is a frozen exhibit on the A path and changing it is a
separate call with its own Mode 5.

**The chromosphere value now matches the store.**
`objects_config.json` held 1.0028748 where `constants_new.py` derives
1.002874802357338. The drift check re-run against the LIVE site reports
26 match, 0 DRIFT, where it read 25 and 1. The corrected radiative-zone
figure is visible in the exhibit's hover with its full citation --
0.713 solar radii, 496,034 km, 0.00332 AU, Christensen-Dalsgaard, Gough
& Thompson (1991). A provenance correction readable by a visitor is new
in this project.

**The gallery has a maintenance runner** (L-236, closed). It departs
from the orrery's in two ways, and both were the design decision rather
than detail. TWO MOMENTS: the plain run is offline and goes before a
commit, and `--live` goes after a push, because the Jekyll failure that
broke the ship existed only on the deployed site and only after a push.
THREE STATES: pass, fail, and unreachable, with unreachable counted
separately and never folded into a passing total.

**Both runners have repo-specific names** (L-264, closed).
`orrery_maintenance_run.py` and `gallery_maintenance_run.py`. Seven live
references swept; the ledger, the handoffs and the spent patch scripts
deliberately left alone as records of what happened under the old name.
Two dashboard rows added for the gallery runner, offline and `--live`.
Nine tracked `.bak` files retired and `*.bak` added to `.gitignore`.

**provenance-discipline 2.10 is recorded in protocol v3.47** (L-258,
closed), together with the significant-figures rule it added, the
RADIATIVE_ZONE_AU correction, the INNER_CORONA_RADII re-homing, and the
two pinned literals restated as ratio bounds.

**The Register Rule makes plain speech the default** (L-261, closed),
on Tony's instruction. The compressed voice keeps its home in the
protocol and the skills; it leaves the chat.

---

## Four defects, and what each one teaches

**One. `smoke_framing.js` has never run** (L-262, OPEN). It slices
`interactive.html` between `function gridDtick(span) {` and
`async function fetchText(url) {`, and neither marker has ever existed
in that file in any commit -- measured across the whole history of both
files. It was added on 2026-08-26 with L-238 and has failed on every
execution since, unnoticed, because it sits in `documentation/` and was
in no routine. Put the check where it runs.

**Two. The reachability check called a correct deploy stale.** It
compared raw bytes; `gallery_cache_builder.py` writes two JSON files in
text mode, so they are CRLF in the working copy and LF in the repo and
on the site. The same line-ending fault had been diagnosed and fixed in
the patch scripts a few hours earlier and was not carried to the runner.
One producer, two consumers, one of them moved.

**Three. The orrery lost its own runner for three commits.** Two
programs were called `maintenance_run.py`, one per repo; the gallery's
was downloaded, the orrery's was displaced, and the deletion travelled
inside a commit that also added a patch script, so it was invisible at
a glance. Recovered byte-identical from `8b762e0`.

**Four. Two handles were cited before their blocks existed.** L-258's
protocol entry and L-264's ledger block were both named in committed
code before anything backed them. Both were found by a person reading,
not by a check. The detection L-230 designs is still unbuilt, and this
is now its third instance.

---

## The skill bump, and the one thing it cannot verify

**safe-file-editing went to 1.9** with Compare Content, Not Bytes
[QUALITY], and protocol v3.48 records it in the same commit that made
it -- which is the whole of the improvement over this morning, when
provenance-discipline 2.10 got its version line, its manifest row and
its commit and not its protocol entry.

**The one step that cannot be discharged from inside the session that
made it:** a skill lives in three stores, and the account install is the
copy Claude actually loads. A reinstall is invisible to the running
conversation, so it is carried in writing instead:

    safe-file-editing went to 1.9 at `bfa9de2f`; the session that
    bumped it had loaded 1.8; the next session confirms its loaded
    copy reads 1.9 before doing patch work.

**Tony-action (do):** reinstall safe-file-editing to the account profile
(Settings > Skills) alongside the commit.

---

## Open decisions for Tony

**L-262, how to fix it.** Re-point the smoke test's markers at the
page's real helpers, or extract those helpers so the page and the test
read one copy. The second is more work and removes the failure class,
since the test broke precisely because it read a copy of logic that
lives inline in the page. It touches `interactive.html`, which is live.

**L-256, which dict joins the status-pass beta.**
`spectral_subclass_temps` (9 entries, and Fable already flagged it as an
uncited physical claim inside the store) or `CENTER_BODY_RADII` (18
well-sourced radii). Open since 2026-08-27 and the single thing blocking
the item.

**L-237, when.** Earth's shells will change artifact 1's feature set
again, so re-cutting the golden record now means re-cutting it twice.
The recommendation is Earth first, re-cut once.

---

## Next-session scoping

The ladder's next rung is **Earth's existing shells**. The data is
already served -- `atmosphere_shell` with two shells plus
`planet_radius`, and `van_allen_belts` with both belts plus thickness --
and `feature_renderers.js` already has live cases for both slugs. No new
hand copy into `objects_config.json` is created by this step, which is
why it was chosen ahead of the transport.

Also open, unchanged by this session: L-257's three enforcement builds,
the rendering ladder still not written into the master plan, and
segment 2, the cross-repo transport, which failed its first real test
this morning and is now evidenced rather than argued.

**The mobile check happened at the close of the session**, on iPhone
Safari, both orientations, and it is the reason L-260 stays open.

The exhibit WORKS on a phone. Pyodide loaded, the assembler ran, the
shells drew, the axis titles are there. That is the premise of the whole
interactive gallery passing its first real test, and it is the headline
rather than what follows.

LANDSCAPE is usable as it stands: the legend takes about a quarter of
the width, scrolls, and the Sun renders clear of it.

PORTRAIT is not. The legend covers roughly 58 percent of the width and
58 percent of the height as an overlay, and the Sun sits BEHIND it, so
the object of the exhibit is the part you cannot see. All 18 entries
render at once instead of scrolling as they do in landscape. The axis
titles also clip -- only fragments of X (AU) and Y (AU) reach the
viewport at the bottom corners.

Both are read from screenshots rather than from the page, and neither is
diagnosed. gallery-pipeline 1.2 carries the 768 px breakpoint and a
bottom-drawer pattern for exactly this case, and the Sun exhibit does
not use it. Whether that is the fix is a design conversation. **This is
the first thing the next session should take up**, ahead of Earth's
shells: the exhibit is public, and portrait is how a phone is held.

---

*Session written August 2026 with Anthropic's Claude Opus 5. Built on
orrery `bfa9de2fc0b9c2d30c9eb4de27828a8c2b4c8535`, gallery
`6c6123974e883a461a92b586b8352c9c535ee8d1`; both confirmed against the
live remote.*
