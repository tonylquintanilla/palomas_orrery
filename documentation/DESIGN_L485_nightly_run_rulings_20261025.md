<!-- Doc-Kind: hand | Design record of the Oct 25 talk on L-485 (a nightly unattended run): Tony's purpose and rulings, Claude's proposals awaiting his word, and what the build session verifies first. Zero code. -->
# Design record: the nightly run that keeps the website current without Tony

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session, talk only) | October 25, 2026

Built on orrery 0c27f47ad631efbfc611a80404095649025687d6 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b1a4ce6c7fc72b17571a13e18ab11df98b86485b at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
Both read live with git ls-remote on the morning of Oct 25. No code was
changed in this session.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION record (zero code). Carries the rulings for L-485
(a nightly unattended run) until a records patch moves them to the
ledger; the method it names goes to gallery-cache-builder at its next
version. Companion to L-461 (pull matches push; ruled "stop" on Oct 25,
`COORD_L461_stop_ruling_20261025.md`) and L-462 (a shorter run). It
also opens a legacy item (section 6), to get the next free handle.

## 1. The purpose, in Tony's words

Tony, Oct 25, 13:11: "There are really only two reasons for automation:
keeping a cadence of midnight runs and fully automated in the event I
cannot work the website. So I would want to move the 30 day checks to
the automated run not just the maintenance run. This website is a
legacy gift for Paloma."

Earlier the same talk, on a run that would still need his push each
morning: "Well if I'm pushing anyway there's really no gain." That
ruled out a nightly run that only saves waiting time. The run exists
to keep the site current with no hand on it.

## 2. Rulings, Oct 25

**R1. The checkers are the gate for the nightly push.** Tony: "I think
we have enough safeguards." The gate in three parts, put to him and
confirmed by his going on to the next question:
- The push happens only on a clean run: every gating checker passes
  and the cache swap succeeded. One red line and nothing is committed;
  the previous cache stays live.
- The nightly commit touches only what the tools write: the served
  cache under `data/solar-system/`, the run records, the swap log, the
  pulled export and its mirror, the guest book file; in the orrery, the
  data files its 30-day tools write (section 3). Never code, never a
  page, never a word a visitor reads. A run that would change anything
  else fails instead of committing.
- A failed night is visible: a dated log and the dashboard's last-run
  line say which checker went red. Silence is never "fine."

**R2. The 30-day checks move inside the automation.** Not only the
website's Daily Run but the orrery's 30-day work: the Horizons check,
the period fetch, the path plan's re-check, the link check. Tony's
reason is the purpose above: anything that depends on him monthly is a
thirty-day fuse. (The website's own gate, Horizons confirmations
within 30 days, would otherwise stop every push a month after his last
orrery run.)

**R3. It runs on GitHub's computers, not Tony's.** Tony: "Yes on
running on GitHub." A schedule on his machine dies with the machine.
GitHub Actions runs it from a setup file in the repository, keeps
every run's log, and needs nothing in his house to be on. The
machine-sleep-and-wake plan he first asked about is therefore not
built.

**R4. Outside failure points are reported, never halting.** Tony: "the
other failure points are beyond our control and should be reported but
not halt the rest of the run or future runs." The guest book's Google
sign-in expiring, JPL changing its interface or being down, a source
address no longer answering, an outside library's address failing: each
is logged and the rest of the run continues; no such failure stops the
next night's run.

**R5. The guest book step reports and continues.** From Tony's note of
Oct 24 ("unless the autorun just reports any new messages and
continues"): the nightly run reads the form's new messages and lists
them in the log; approving, replying and pinning stay his.

## 3. Proposed by Claude, consistent with the rulings, awaiting Tony's word

**P1. When a 30-day check disagrees, that body keeps its last
confirmed values.** Today a Horizons DISAGREES, a comet with a newer
record, or a period JPL now gives differently goes to Tony. The
automation never decides those: it stops refreshing that one body,
keeps serving the values last confirmed, whose fetched date the hover
and the i panel already print, and logs the disagreement where a
future reader finds it. The site degrades to "last confirmed on this
date," which is true, not to a guess. (Same principle as removing an
unsourceable number rather than citing it wrong.) Tony's R4 covers the
failure-point half of this; the keep-last-confirmed half is his to
confirm at the build's design.

**P2. Which orrery tools run at night.** The ones that write data the
website pulls and that have planted-fault suites: period_fetch.py,
horizons_check.py, path_plan.py, export_objects.py, export_constants.py,
export_drawings.py, and the link check. NOT the parts of the maintenance
run that judge code (the provenance scanner as a gate, the constants
change report, the reset-completeness test that opens the Tk window):
they matter when code changes, and at night no code changes.

**P3. Two workflows, one per repository, sequenced by the clock.** The
orrery's runs first and commits its data files to the orrery repo; the
website's runs about an hour later, pulls what was pushed, builds, checks
and commits to the website repo. Each pushes only to its own repository
with GitHub's built-in token, so no cross-repository credential has to
be created, stored or renewed, which is itself a legacy risk avoided.
GitHub runs scheduled jobs late when many start on the hour, so each is
scheduled off the hour (for example 23:17 and 00:47 UTC). Tony asked
for midnight UTC; the website's run lands just after it.

**P4. The first week is read daily.** Push on from night one; Tony reads
the log each morning for a week before he stops reading it daily.

## 4. What the build session verifies before trusting the design

- GitHub pauses scheduled workflows in a repository with no commits for
  sixty days. Confirm from GitHub's own documentation whether the
  workflow's nightly commits count as activity. If they do not, the
  design needs a keep-alive, and that is a legacy fact to record.
- The runners' tools: Python with the orrery's libraries (no Tk
  needed for P2's set), node and a headless Chromium for the website's
  smoke suites, and the time each job takes against GitHub's limits.
  The path plan's full re-check ran 28 minutes on Tony's machine on
  Oct 24; the job's time limit must hold it.
- Permissions: the built-in token must be allowed to push to the
  repository (a repository setting), and GitHub Pages must redeploy on
  the workflow's commit as it does on Tony's.
- The orrery's tools, run on Linux, write LF and ASCII as the project
  requires; nothing in them assumes Windows paths.
- The guest book updater's Google sign-in: how it is stored for a
  runner, and that its expiry fails soft (R4).

## 5. What L-485's records patch carries

- R1 to R5 as Tony's rulings, in his words above; P1 to P4 as
  proposals, P1 marked awaiting his word.
- L-462 (a shorter run): reconsidered in this light; a shorter manual
  run matters less once the nightly run exists. Tony's call whether it
  stays.
- Where We Are: L-485 leaves the Deferred list and takes a place on the
  road, after slice 2, as the step that makes stage 15's website stand
  on its own.

## 6. A legacy item of its own (next free handle)

Tony, Oct 25: "This website is a legacy gift for Paloma." Beyond the
nightly run, the things the site leans on that are not in these two
repositories, each to be named, its failure mode written down, and its
failure made visible rather than silent (R4): who besides Tony can hold
the GitHub account and the Google sign-in; JPL Horizons' interface; the
Plotly library served from an outside address; GitHub Pages itself; the
sixty-day rule above. Discovery first, one list; remediation later, in
slices (The Braid). This is Tony's to shape at a talk of its own.

## 7. Tony-action rollup

- **(do)** Commit this record with your next push.
- **(decide)** P1, keep-last-confirmed, at the build's design talk.
- **(decide)** Whether L-462 (a shorter run) stays.
- **(decide)** When the legacy talk (section 6) happens; it does not
  block L-485.

Written October 25, 2026 with Anthropic's Claude Fable 5.1.
