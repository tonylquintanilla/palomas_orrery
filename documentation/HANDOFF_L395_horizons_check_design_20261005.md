<!-- Doc-Kind: hand | Handoff for a fresh session: design, then the first discovery run, of the check of the orrery's object list against JPL Horizons (L-395). -->
# Handoff: checking the object list against JPL Horizons (L-395)

Built on orrery 72e3b55805c29f1f08a583864bd815a47e7434c6 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
624aa94557e16956b2fe022a467936ae2ccf3406 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Pushed
at: Tony's push of this session's closing patch, which carries this
file. The receiving session pulls both repos at HEAD and reads L-395
in LEDGER_CONSOLIDATED.md before anything else here.

Type: DESIGN, then DISCOVERY. Audience: a session inside this Project,
which has the protocol and the installed skills. Skills to load:
horizons-orbital-mechanics, provenance-discipline (2.26 if reinstalled),
ledger-and-session-records (1.15 if reinstalled). Written October 5,
2026, with Anthropic's Claude Opus 5.5.

## Why this, and why now

- Tony, 2026-10-05: it matters "because like our other accuracy
  disciplines this is about verification of information we are
  serving."
- The website serves eleven bodies whose identity facts are copies of
  the orrery's object list (`OBJECT_DEFINITIONS` in
  `celestial_objects.py`): the Sun, the eight planets, Pluto and
  Apophis. The copy is checked against the list (L-395's first build,
  2026-10-01). The list itself is checked against nothing.
- So the check is in scope under The Braid: it is bounded to what the
  website serves today, and it terminates.

## What is settled (Tony's rulings, on L-395)

- The orrery's object list is the one definition of each object; the
  website keeps copies written by `tools/mirror_objects.py` from
  `data/objects_export.json`, and a check fails on any difference.
- Horizons is the outside authority. The list can go stale -- legacy
  entries, the orrery's own evolution, errors -- so the check compares
  the list with Horizons, not only the website with the list (Tony,
  2026-09-29).
- Simple errors a check finds are fixed and reported; anything with a
  choice in it comes to Tony (provenance-discipline, A Simple Error a
  Check Finds Is Fixed and Reported).
- Discovery before remediation: the first run lists every disagreement
  and fixes nothing except simple errors, reported.

## What is open: the design round, in this order

1. What Horizons can confirm for an entry: that its id resolves to
   exactly one object; that object's name and designation; its kind.
   And what it cannot: the project's modelling choices, such as
   drawing Pluto about the Pluto-Charon barycentre.
2. Which fields are compared, and what counts as agreement. Apophis is
   the worked case: `2004 MN4` and `99942` name one Horizons record.
3. Where the check runs, and its cadence. It needs the network, so
   when it cannot reach Horizons it says so and never passes. It
   records the date each object was last confirmed, the way a
   constants row records who read its source, and re-confirms on a
   cadence rather than querying every object on every run.
4. Pinned records (Halley `90000030`, Encke `90000091`): flagged when
   JPL has a newer solution, for Tony to decide. Not among the eleven,
   so this may wait for stage 9; the design should say.
5. What the first run prints: every disagreement by name, the object
   and the field, with Horizons' answer beside the list's.

## One practical fact, found 2026-10-05

- This chat's sandbox cannot reach JPL: a Horizons API query was
  refused with `x-deny-reason: host_not_allowed`. So either the check
  runs on Tony's machine, like the cache builder, or Tony adds
  `ssd.jpl.nasa.gov` to the chat's allowed domains so a session can
  run the discovery pass itself. That is a (decide) for the design
  round, not before it.

## Not in scope

- The other 171 entries of the list (road stage 9), except as the
  design says the check will reach them later.
- Fields the list lacks (a moon's parent, a clean kind for comets):
  recorded on L-395, its own round.
- The numbers inside descriptions: L-403.

## Running beside the website session (Tony, 2026-10-05)

Tony asked that this design round and Earth's website patch run as two
sessions at once. The website session's handoff,
`documentation/HANDOFF_L413_earth_orrery_patch_20261005.md`, carries the
same three rules.

- DO NOT REWRITE WHERE WE ARE. The website session owns the page this
  round. Put this session's updates for the page in this session's
  handoff, under a heading saying so; the next rewrite picks them up.
- THE OPENING CHECKS ARE THE WEBSITE SESSION'S. This session reads the
  version of each skill it loads and compares it with the protocol's
  manifest, as always, but leaves closing L-369, L-418 and L-419 to the
  website session. In the ledger it edits only L-395, and any item it
  opens.
- PULL AGAIN BEFORE ANY PATCH. Both sessions start from orrery
  be67ca39. Before building a patch, re-read HEAD, build on whatever the
  website session has pushed, and name that commit. Ledger edits match
  only the lines they change (L-419), so the two sessions' ledger
  patches apply in either order.
- A design round is conversation first. Tony carries two threads; one
  question at a time.

## Tony-actions

(decide)
- At the design round: the five questions above, one at a time.
- Where the check runs: Tony's machine, or this chat with JPL allowed.
