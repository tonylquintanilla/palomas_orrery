# Session Handoff -- August 8-10, 2026

**Built on `826a932f8bb7329e211337085f4d68d26aaa4a51`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery pinned separately at `02d71637e100c4faf6ddaa23cdbc9b6f4a88ddc0`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs verified live at session close.**

**Type: DESIGN SESSION plus small builds.**
**Prepared:** August 10, 2026 by Claude Opus 5, Tony Quintanilla integrator.
**Supersedes** `documentation/HANDOFF_20260808_design_session.md`, which was
written mid-session at `0811ffc` and is now stale on its anchor and its
do-list. Discard that one. It remains valid as a session record only.
**Continues from** `documentation/HANDOFF_20260807_full_session.md`
(anchored `2161b19`).

**Closes:** L-186's mechanical half; one shadow constant.
**Opens:** the L-190 sibling (still needs a handle).
**Retires:** the scheduled nightly build. Tony's ruling, August 10 -- the
builder now runs manually and he commits it himself.

---

## Who you are working for

Tony Quintanilla, PE -- a retired civil and environmental engineer, artist,
and anthropologist. Not a professional programmer, not a formally trained
astronomer. He builds Paloma's Orrery through conversational AI
collaboration and holds sole commit authority and final judgment. The
codebase's structure and discipline are products of that collaboration; do
not read code quality as evidence of his personal programming fluency.

He runs Python by opening a file in VS Code and clicking Run, and works
through GitHub Desktop. Deliver runnable transactional patch scripts.

**Read the Process section at the bottom of this document before your
first substantive reply.** It is not optional context. A protocol
amendment came out of this session because these conversations were
running too dense for Tony to absorb, and the amendment is drafted but
NOT YET APPLIED to `PROJECT_INSTRUCTIONS.md`.

---

## What happened, briefly

Two working days. August 8 was a mobile design session -- zero code, a
set of rulings that unblock Track 0. August 10 was at the machine: the
L-186 patch, a shadow-constant fix, two scanner runs, and a gallery
incident that turned out to be a false alarm with a real lesson in it.

---

## Rulings (Tony, this session)

1. **Fetch-and-import RATIFIED.** Master plan Section 7, decision 12,
   moves from RECOMMENDED to RATIFIED. Two conditions attach: a data-only
   rule plus pre-import gate for `constants_new.py`, because import
   executes top-level code; and builder fallback when GitHub is
   unreachable must be OBSERVED at build time, not inherited from a
   reviewer's claim. It must fall back to the last committed copy, never
   write empty features.

   Verified feasible: `constants_new.py` imports only numpy and datetime,
   nothing orrery-internal, so the fetch really is ONE file with no
   dependency tree.

2. **Registry shape: three zones per entry.** Measured (value + source),
   Declared (style choices, no source expected), Derived display text
   which is NOT stored but built by interpolation.

3. **A measured field carries value, unit, and source** -- not a bare
   number with the unit baked into the key name. Tony's ruling: published
   values vary in units, so conversion is needed for uniform display text
   regardless. Storage stays heterogeneous; conversion at the display
   step. This DELETED an earlier Claude recommendation for a per-feature
   unit convention.

4. **Interpolation locus: builder side** (Section 7, decision 17). Tony's
   reason: so the orrery and assembler cannot diverge. Cost accepted: the
   cache holds finished strings, so rephrasing needs a rebuild.

5. **L-190 is two issues, not one.** The second class -- claims about the
   codebase that no tooling checks -- still needs a handle.

6. **L-188: keep all entries.** Reverses the L-188 block's "must replace,
   not join." Tony's reason: one run may not always be preferred.
   Resolution: keep the individual entries AND add a run-all, with the
   run-all tied to the push so it is not one more optional thing to
   remember. One implementation, two entry points.

7. **Annotation parser: STRIP**, not extend. Done, see below.

8. **Manual-scale instructions stay in the orrery unchanged.** The only
   rule is that the transport never carries them. No sweep, no ledger
   item. Reached after measurement showed 116 sites, not the 3 initially
   visible. Note: the `***` markers mark headline notes generally, not
   scale notes specifically, so `_strip_plotting_suggestions()` in
   `save_utils.py` has a broader scope than its name suggests.

9. **Migration order: structure first.** Prove the structure on Jupiter,
   where served data is complete and correct so the transport has a real
   acceptance test. Then cross-check Artifact 2's remaining values,
   writing into the proven structure. Then complete the migration and
   resolve what surfaces. Artifact 2 stops being blocked and becomes
   step 2.

10. **Not-yet-sourced is ONE state, not two.** Tony's correction: the
    orrery itself is the source, so if the orrery does not offer a value
    there is nothing to render. There is no "field does not apply" case.
    A not-yet-sourced field means a rendered value with no recorded
    provenance. Distinguishable from absent; never an empty field.

11. **"The Artifact Bounds the Audit" goes in the protocol**, with Tony's
    nuance: the bound is closed at any moment and open over time, because
    what the orrery renders is itself an output of these conversations --
    osculating orbits entered as a Claude suggestion, not as a gap being
    filled.

12. **Register Rule amendment approved** for the next protocol pass.
    Drafted, filed at `documentation/REGISTER_RULE_AMENDMENT_v3.36.md`,
    NOT YET APPLIED.

13. **Fix small things in-session; do not ledger them.** Tony's ruling
    when Claude suggested deferring a two-line fix: "either we fix it now
    or it gets forgotten unless recorded in the ledger... we don't need to
    put everything in the ledger, where it gets buried." The ledger is for
    things needing a decision, a design, or a sequence. A two-line import
    fix needs none of those.

---

## What was built and pushed

Three pushes, each round-trip verified.

| SHA | What |
|---|---|
| `308053c` | L-186 patch: 8 annotation repoints, 3 value strips, worksheet filed |
| `826a932` | shadow constant fix, patch scripts moved to `documentation/` |

Gallery: `02d7163` (a revert -- see the incident section).

**L-186 mechanical half is done.** The August 2 Gemini worksheet was
recovered by Tony and filed as
`documentation/worksheet_gemini_constants_remaining.md`. Eight
filename-less annotations in `constants_new.py` now point at it. Three
appended checked-values stripped from eris (x2) and venus (x1).

**Scanner result:** cross-check annotation issues 12 -> 6. All six
remaining are `duplicate_identity`. Zero `non_markdown_reference`.

**Shadow constant closed.** `orbit_data_manager.py` had a local
`KM_TO_AU = 1.0 / 149597870.7` duplicating `KM_PER_AU`. Now imports from
`constants_new` directly. Value bit-identical
(`6.6845871222684464e-09`); the patched module was runtime-import tested
with astroquery and astropy present, not merely compiled.

---

## A provenance failure worth reading before you file anything

Claude took Tony's uploaded Gemini worksheet and REWROTE it before filing
-- converted LaTeX to ASCII, stripped markdown escaping, added a header
block and a provenance note it authored -- then labeled the result as the
Gemini worksheet. Tony caught it: "you have created a parallel unsourced
worksheet not made by gemini... because of a trivial title consistency
issue."

The corpus settled it. Existing worksheets are filed as received; the GPT
one has 115 non-ASCII bytes and the earlier Gemini one has 37. There was
no consistency to fix.

**The rule:** an evidence artifact is filed as received. House style, ASCII
rules, and naming conventions apply to code and to documents we author.
They do not apply to a document whose value is that someone else wrote it.
Tony's original is what is now in the repo, LaTeX intact.

**Second, related.** The August 7 Claude instance was asked whether it had
fabricated the `(Gemini worksheet)` annotation. It gave an accurate
account of its process -- it pattern-matched the adjacent GPT annotation's
shape without checking -- but then concluded the CONTENT was fabricated,
called it cite-to-clear, and offered to strip the annotation. The
recovered worksheet proves all three specifics it believed it invented
were true.

Acting on that self-report would have deleted a real citation. **Keep the
distinction: unverified and true is still unverified.** The method was
wrong; the content was not. An over-confession is as much a calibration
failure as a denial, and it is more persuasive.

---

## The gallery incident: false alarm, real lesson

Gallery commit `6792bf7`, "nightly run," deleted all 48 files under
`data/solar-system/` with zero additions. Reverted at `02d7163`; all
files restored.

**Cause: not the builder.** The builder commits with the hardcoded message
`data: nightly <date>`. "nightly run" was Tony's message, typed in GitHub
Desktop. He opened the gallery tab, saw nothing to commit, went to the
orrery repo, came back, and saw 48 deletions -- the atomic swap window had
opened between his two looks. He reasonably read deletions-with-no-adds as
cleanup of replaced files, and committed.

**The builder behaved correctly throughout.** The swap moves
`data/solar-system` aside while assembling the replacement. During that
window the working tree genuinely shows only deletions.

**Why this matters beyond the incident.** The swap's safety design is
invisible from GitHub Desktop. From inside the tool Tony uses for every
commit, a correctly functioning build looks identical to a catastrophe.
The habit fix ("check the task is Ready first") is weak, because it only
helps if you already suspect a build is running.

### RULING: the scheduled nightly is retired (Tony, August 10)

**The build now runs manually and Tony commits it himself.** The task is
DISABLED, not deleted -- the corrected configuration is worth keeping if
this is ever revisited.

Tony's reasoning, in his words: "It can't run without my machine being on
anyway and it's consistent with me being the only commit authority. And
obviates complicated fail safe procedures that could also fail."

The decisive part is the first clause. The schedule created an appearance
of automation the setup could not deliver -- three nights were missed this
week and the failure was silent. A manual run is honest about what it is.
It also dissolves the surprise that caused the incident: if Tony starts
the build himself, he knows a build is in flight, and the swap window is
no longer something he can walk into.

**Three nightlies were missed** (8/8, 8/9, 8/10) before this ruling. Cause
was Task Scheduler's default "Start the task only if the computer is on AC
power," with Tony on battery. That was corrected before the task was
disabled, along with "Wake the computer" and "Run task as soon as possible
after a scheduled start is missed." Note the last has a precondition -- it
applies only to time-based tasks with an end boundary or infinite repeat
-- so an Expire date far out on the Triggers tab may be needed for it to
work at all.

**What this does NOT dissolve.** The cadence question changes shape rather
than disappearing. "Did the nightly run?" becomes "when did I last run
it?" Something still needs to tell Tony the served data is eleven days
old. See the L-189 design input below.

**One unresolved oddity, now academic:** the task sat in Running for hours
after the work had finished. If the schedule is ever re-enabled, watch for
it.

### NOT BUILT, kept for future reference

A `pre-commit` hook in the gallery repo refusing a deletion-only commit
under `data/solar-system/`. That condition is never legitimate -- the
builder always replaces -- so it catches mid-swap, a crashed build, and
accidental deletion without needing to know which.

This was designed and agreed before the scheduler ruling superseded its
main use case. **Do not build it now.** Record it as a note. It becomes
relevant again if the schedule is ever re-enabled, or if a second person
ever gains commit access to the gallery repo.

If it is built: preferred over a builder-written lock file, which would
require editing a working builder and would leave a stale lock after a
crash. Hooks are untracked, so it needs a tracked `hooks/` folder plus
`core.hooksPath`, set by a small installer Tony runs from VS Code. Test
that it blocks the bad case and permits a normal commit before trusting
it.

---

## Design input for L-189 (next session's work)

Three things this session produced, all evidenced rather than argued.

**Cadence, not just records.** The missed nightlies left NO artifact
anywhere -- no run record, no log, no repo change. A history file that
only accumulates runs cannot report a run that never happened. So the
history must carry a DECLARED expected cadence, and something must compare
now against last-run.

This got MORE important, not less, when the schedule was retired. A
manual build has no expected time at all, so nothing but an explicit
staleness check can tell Tony the served data is eleven days old. The
question changed from "did the nightly run?" to "when did I last run it?"
-- same mechanism, and now the only mechanism.

**The check cannot live inside the thing it watches.** A nightly that never
starts writes nothing. Put the check in the L-188 maintenance runner,
which Tony ruled runs on demand and at the push gate. That makes L-188 the
trigger and L-189 the data.

**Totals hide deltas.** Two scanner runs twenty minutes apart both reported
880 findings. Underneath: shadow constants 1 -> 0, one new file entered the
scan, `orbit_data_manager.py` changed shape. Three real events, invisible
in the summary. Report the delta, not the total. Grade by age in days
rather than pass/fail.

**Precedent already in the tree.** The gallery builder writes
`data/solar-system/raw/runs/<timestamp>.json` per run with
`structural_validation`, `guard_warnings`, `committed`, `pushed_remote`,
and `commit_sha`, and updates the record after the push to record the SHA.
Follow that shape rather than inventing one.

---

## Registry design state (write into the L-181 block)

- Three zones per entry: measured, declared, derived-not-stored.
- Measured fields carry value + unit + source. Conversion at display.
- Derived text is not stored. `CHROMOSPHERE_RADIUS_LINE` is the working
  precedent: two differently stored values (solar radii and km) feeding
  one sentence that emits solar radii, AU, and km.
- **Structural constraint:** everything measured must sit at MODULE SCOPE,
  reachable without executing anything. This is what makes L-181 the
  PRECONDITION for L-190 rather than more work for it -- a value inside a
  draw function cannot be walked by an AST pass, which is exactly why the
  scanner cannot see `belt_distances` today.
- One not-yet-sourced state: a rendered value with no recorded provenance.
- Range-capable measured fields. The Jupiter main ring `description` says
  thickness is about 30 to 300 km while `thickness_km` says 30. The prose
  is more accurate than the data. Whether EVERY measured field becomes
  range-capable is better answered against Jupiter's four entries than in
  the abstract.

**A ring entry today**, for reference:

```
'main_ring': {
    'inner_radius_km': 122500,      # sourced
    'outer_radius_km': 129000,      # sourced
    'thickness_km': 30,             # sourced
    'color': 'rgb(180, 120, 100)',  # developer choice, declared not sourced
    'opacity': 0.7,                 # developer choice
    'name': 'Main Ring',
    'description': "...122,500 km to 129,000 km...about 30-300 km...<br>"
}
```

---

## (do) -- outstanding

### Protocol and skills

1. **Apply the Register Rule amendment.**
   `documentation/REGISTER_RULE_AMENDMENT_v3.36.md` carries both edits
   (the checks block in Part 2, and the version-history entry) plus
   application notes. Protocol only -- no skill bump.
2. **Add "The Artifact Bounds the Audit"** to Part 3, adjacent to Show the
   Envelope of the Unknowable. Text is in the amendment file.
3. **`provenance-discipline` to 1.8.** Two additions. First: if no
   worksheet file exists, the annotation is not written -- save the
   exchange as `.md` first, then annotate. Second, as a field note: an
   evidence artifact is filed as received, never reformatted to house
   style. Three stores move together (repo, account install, manifest via
   `skills_index.py`).

### Provenance

4. **Resolve six `duplicate_identity` sites** against the sources:
   `constants_new.py` 423, eris 218, mercury 49, pluto 41,
   `shell_configs.py` 128, venus 528. Each needs a look at the source to
   decide whether one annotation is redundant or a checker name is wrong.
   Needs Tony's judgment, not a patch.

### Count corrections

5. **Ledger tooltip count: 124, not 126.** The raw grep returns 126 but
   two matches are documentation -- the module docstring at line 12 and a
   comment at line 2062. Real key definitions: 83 in SHELL_CONFIGS + 41 in
   CUSTOM_SHELLS = 124. Two sites carry 126: the L-181 bullet (where it
   contradicts its own "83 sphere + 41 custom" breakdown) and the L-181
   decide-item (d). Also check the historical entry near line 5357.
6. **Master plan decision 12 counts.** It says "7 of 45 top-level
   assignments are derived." Measured at HEAD: 49 assignments, 6 derived.
   The 45-to-49 gap is exactly the four L-179/L-180 additions, so that
   part is stale rather than wrong.

### Ledger

7. **Open a handle for the second L-190 class:** claims about the codebase
   that no tooling checks. Evidence: 772 lines, 37 entries, 126 tooltips,
   45 assignments, 3-vs-8 annotations, and one more from this session --
   Claude reported 248 sites for `CHROMOSPHERE_PHYSICAL_KM` from grepping
   "2000", which matched years and array sizes. Six instances now. None
   changed an outcome; no tool caught any.
8. **Record the scheduled-build retirement.** The nightly task is disabled;
   the builder runs manually and Tony commits it. This is a change to how
   the serving pipeline operates and belongs in the ledger and in the
   `gallery-cache-builder` skill, which currently states that Task
   Scheduler history IS the monitoring channel. That is no longer true --
   there is no scheduler and no monitoring channel. Note the pre-commit
   fail-safe as designed-but-not-built, relevant only if the schedule
   returns.
9. **Note on the L-191 block:** manual-scale instructions are
   orrery-surface-only and must not be collapsed into shared text that
   reaches the transport. 32 of them live in `shell_configs.py` as copies
   of shell-module text.
10. **Note on L-181:** drop the dead numpy import from `constants_new.py`
    when the migration next touches the file. Imported since April 5 2025,
    zero uses across all 46 commits.
11. **Record the eighteen inline literals** duplicating cited constants:
    `KM_PER_AU` 14 sites in 8 files, `MOON_RADIUS_KM` 3 in 2,
    `SUN_RADIUS_KM` 2 in 1. Same violation as the shadow constant, but
    inline in f-strings rather than named assignments, so the scanner sees
    one of nineteen. This is scope-and-sequence work, distinct from
    L-181's migration, and evidence for item 7.

---

## (decide) -- still open

1. **The constructor-call count in decision 12.** It says two assignments
   contain constructor calls. Measured: one, `HORIZONS_MAX_DATE =
   datetime(...)`, with no calls nested inside any of the six derived
   expressions. Staleness does not explain a count going DOWN.
2. **Where the L-188 run-all push-gate binding lands** -- L-188 or L-184.
3. **Migration shape and per-body sequence beyond Jupiter** (L-181). Order
   settled; detail needs Jupiter's four ring entries in view.
4. **Saturn `thickness_km`:** absent from the served cache, but is it
   absent from the ORRERY? If the orrery draws Saturn's rings with a
   thickness, the number exists in code and the gap is transport. One look
   at the file settles it.

---

## Next session

**L-189 first**, per Tony's standing order -- the scanner run history,
built fresh rather than at the end of a long session. History file TRACKED
in git. The console delta is the load-bearing part. The design input above
is new and material. Remember the scanner scans itself, so the first run
after it lands shows a delta that IS the change.

**Before that, a short master plan patch.** Three Section 7 decisions are
stale: 12 still reads "RECOMMENDED, not yet ratified"; 16 (pilot slice)
still reads OPEN; 17 (interpolation locus) still reads OPEN. All three
were ruled this session. Plus the count corrections inside 12, and the
registry three-zone shape, which has no home in the plan at all. Artifact
2's status also changes from blocked to scheduled. Doing this first means
L-189 gets built against a plan that matches what Tony decided.
`MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` needs the same treatment;
it was not read this session.

Then the do-list, then the migration shape conversation, then Track 0
proper.

---

## Process -- read this before your first substantive reply

Tony raised mid-session that these conversations run too dense to absorb:
"the level of detail and jargon is so dense that I only absorb the general
idea and sometimes not even that... I try to be responsive but it is very
hard." He had already tried a second model as translator (added a layer,
introduced errors) and executive summaries (helped partly).

**Diagnosis.** The Register Rule has been in the protocol since v3.33 and
did not fire once across a long session. Its two checks are
PARAGRAPH-level and the paragraphs passed. The failure was four jobs per
message -- finding, recommendation, uncertainty, and new question all at
once. The load is the COUNT of open items, not the density of any one.

**Until the amendment is applied, apply it anyway:**
- One thing per message. A finding and a recommendation are two messages.
- Answer first. How a number was checked is your work, not Tony's.
- Capture goes in a file, not in the conversation.
- Do not rely on Tony saying "opaque." By the time a message is dense
  enough to flag, reading it to the end is already the cost. The check
  runs on your side before sending.

**A second failure mode, distinct from density.** Tony said: "I understand
that if you believe something should be done it must be important because
you have a deep understanding of the code base." That assumption is wrong
and it does damage. You do not have deep understanding of this codebase --
you have what you grepped in the current session. Raising something usually
means you just found it, not that you weighed it against the project and
judged it important.

**So say which it is.** "Found this" versus "this should change what you do
next." Most findings are the first kind. Presenting them identically makes
Tony carry the sorting.

**What the session also demonstrated, and it is worth carrying.** The same
property produced both the overload and the findings. Going through items
one at a time with material in front of Tony is what surfaced the numpy
question, the unit nuance, the L-188 override, the scale-instruction
reconsideration, and the worksheet provenance failure. Tony's own
correction of an earlier framing: it is not luck that he notices things,
it is the layout. "I would not have noticed if your layout of the issues
did not alert me." The layout is Claude's; the noticing is Tony's; neither
half produces the finding alone.

---

*Handoff prepared August 2026 with Anthropic's Claude Opus 5, built on
`826a932f8bb7329e211337085f4d68d26aaa4a51` at
https://github.com/tonylquintanilla/palomas_orrery and
`02d71637e100c4faf6ddaa23cdbc9b6f4a88ddc0` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
