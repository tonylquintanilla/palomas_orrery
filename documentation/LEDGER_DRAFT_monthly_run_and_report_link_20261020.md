# Ledger drafts: the monthly run and the "report a problem" link (2026-10-20)

Built on fcd191e9 at https://github.com/tonylquintanilla/palomas_orrery
(gallery at e8f6dd5e, https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DOCUMENTATION (drafts for the ledger, nothing filed yet).
Written from a design chat in the Orrery project, 2026-10-20.

## What the ledger already holds

- The link check is NOT new. L-266 (nothing checks that a cited link
  still resolves) has been open since 2026-08-30, RICE 9.0 proposed.
  It already covers dead links, redirects, unreachable sites and the
  nasa.gov placeholder. Its open decision is yours: where the check
  lives (the orrery's scanner, the gallery's maintenance run, or both).
  So it gets a note, not a new item.
- L-425 (a citation's location record is checked only in part)
  proposes the same link check as its third level, "run on Tony's
  machine, report-only".
- Nothing on the ledger offers visitors a way to report a problem.
- Nothing on the ledger runs checks monthly. Two items are waiting for
  a cadence: L-129 (comet structure constants, periodic sweep), whose
  Gap says no cadence is defined, and L-395 (the gallery's objects
  checked against Horizons), which says it re-confirms "on a cadence
  rather than querying every object on every run".
- Next free handles: L-457 and L-458.

## Note to add to L-266 (the link check)

```
- **2026-10-20, the cadence.** Run it monthly, from L-458 (the
  monthly run), not in the Daily Run: sites have short outages, and
  checking about 500 addresses every day is noise and may get the
  checker blocked. A link that fails twice running is reported by
  name; one failure alone is listed as "could not reach".
```

## New item: L-457

```
#### [L-457] A "report a problem" link in the information panel (gallery, interactive)
<!-- L:457 status:OPEN upd:2026-10-20 section:A flag: rice: -->
- **Raised by Tony, 2026-10-20**, in a design chat on verification: the
  live source links in the i panel let a visitor check a claim, and
  "if they see something off, they could report it. You know, that
  could be me, or that could be somebody else."
- The third leg of checking, beside Tony and the outside cross-check
  (provenance-cross-check): the public, through the links L-456 (what
  a visitor reads) puts in the panel.
- Most visitors will not click and fewer will report, so the report
  must be one click from the panel and carry the room and feature
  with it, so the visitor does not have to describe where they were.
- **Tony-action (decide):** where a report lands. A pre-filled GitHub
  issue is simplest to build, but most visitors have no GitHub
  account; an email link or a small form asks nothing of them.
**Gap:** the decision above; then the link in the shared i-panel
chrome (interactive-exhibit), so every room gets it at once.
**Ref:** L-456 (sources as a list with live links); L-265 (the i panel
carries links); L-266 (the link check).
```

## New item: L-458

```
#### [L-458] A monthly run for slow checks, started by the Daily Run (gallery + orrery, maintenance)
<!-- L:458 status:OPEN upd:2026-10-20 section:A flag: rice: -->
- **Raised by Tony, 2026-10-20:** "add a monthly run for monthly
  checks like this in addition to the daily run."
- Some checks are worth doing, but not every day: they are slow, they
  hit outside sites, or what they watch changes slowly.
- **Started by the Daily Run, not remembered** (A Check That Cannot
  Fail Is Not Passing: put the check where it runs). The first Daily
  Run of each month also runs the monthly checks. It knows by the date
  of the last monthly run, recorded in a file, so a missed day or a
  month away still fires on the next run.
- The Daily Run prints the monthly run's date every day, so a monthly
  run that stopped happening shows up as an old date.
- **First job:** L-266 (the link check).
- **Candidates, each to be ruled on when opened:** L-129 (comet
  structure constants), L-395's Horizons re-confirmation, and the
  checks still unbuilt on L-396 (Where We Are's freshness and length)
  and L-230 (a skill bump that misses the protocol's history).
**Gap:** where the monthly list and its date file live; which repo's
Daily Run starts it, or both; how its results reach the run record.
**Ref:** L-446 (the Daily Run's order); L-416 (a dashboard button per
maintenance step); L-236 (the gallery maintenance runner).
```
