<!-- Doc-Kind: hand | Handoff for a design talk (zero code): what consistency between the orrery and the website means, beyond JPL's parameters, for L-484 (the two agree). Carries the review of what is checked today, the six layers proposed, and the first question. -->
# Handoff: what "the two agree" means (L-484), for a design talk

Tony Quintanilla, PE | Claude Opus 5.5 (coordinating session) | November 3, 2026, 09:05 Chicago

Built on orrery 526a527f0d60288853e799f0e4b9783db84d0ae4 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
3a211a8cf10a3002668a85836f31bf973e385f2c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both read
live on Nov 3, about 15:00 UTC; plus this session's edits to
`LEDGER_CONSOLIDATED.md` and `documentation/WHERE_WE_ARE.md`, which Tony
pushes before the talk. Read L-484 at the pushed SHA, not this summary,
if the two differ.

Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`,
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.

Type: DESIGN SESSION (zero code). Fable, high effort, by
`METHOD_MODEL_EFFORT.md`. A design record at the end, not a brief: the
brief is written when the build is next.

Read first: L-484 (the two agree) in full; interactive-exhibit 1.30,
its bullet "The website and the orrery agree on every object both draw"
(under Provenance); provenance-discipline 2.36, What a Visitor Reads;
the protocol's The Artifact Bounds the Audit and The Braid. A session
outside this Project also fetches `PROJECT_INSTRUCTIONS.md` and those
two skills at the orrery SHA above, and says which it read.

## 1. Why this talk

Tony, Nov 3, 08:59: "Yes let's do L 484. Because that consistency is
also a general check of the website. But I think it warrants a talk
about what we mean by consistency beyond narrow JPL parameters." It is
stage 12c on Where We Are, next after the current work.

The rule already stands (Tony, Oct 24): for every object both
instruments draw, they agree on its JPL record, its name, its dates and
its words, or the difference is a documented exception. The check is
not built; until it is, each build compares the two by hand.

## 2. What is checked today (read from the code at the SHAs above)

In the website's maintenance run:
- Objects mirror and its check: for the 92 objects the orrery keys, a
  tool copies name, JPL id, kind, description, NASA link, period and
  path plan from the orrery's export; a hand edit fails the run.
- Export freshness: the website's export is the orrery's, byte for byte.
- Config mirror and Store drift: served numbers pulled from the
  orrery's constants export; Store drift examines 3 pointers, 2 of them
  not examinable (Jupiter's and Saturn's poles).
- Horizons confirmations, on both sides, every 30 days.

## 3. What nothing checks

- Five website objects with no orrery key: the Moon, Io, Titan, Pluto's
  body, Charon. No mirror, no period, no Horizons check.
- Dates. The first finding: the website draws Galileo by its path plan,
  ending at the impact, 2003-09-21; the orrery's plot draws to its
  typed end_date, 2003-09-29, eight days past it. Cassini's typed end is
  a day short of its plan's. Recorded on L-476 (the orrery plots by the
  path plan), which is the fix.
- Words beyond the mirrored description: the orrery's hovers and
  tooltips against the website's text boxes and i panel.
- The exceptions themselves: the documented differences (the belt's
  kilometres, Galileo's gold for the orrery's white) live in ledger
  prose that no tool reads.

## 4. The six layers proposed (for Tony to cut, add or reorder)

1. The same object: same JPL record, same name. Mostly held now.
2. The same numbers: every number a visitor reads, on either site,
   prints from the same sourced row. The layer that makes this a
   general check of the website: it reaches every number the website
   shows, not only shared objects.
3. The same span of time: a path drawn over the same dates. Galileo
   fails today.
4. The same claims in words: what the website's shorter text says, the
   orrery says too, from the same source.
5. The same picture language: symbols, solid for flown and dashed for
   predicted, colours, except differences chosen on purpose.
6. The same set: every object the website shows is one the orrery
   defines. The five above fail today.

## 5. The first question (one at a time)

For the words and the picture (layers 4 and 5), does "agree" mean THE
SAME, or NEVER CONTRADICTS?
- The same: a tool can check it, but the website's phone-length text
  would have to match the desktop's longer hovers.
- Never contradicts: fits two instruments built for different screens,
  but a tool can check only the numbers and dates inside the words; the
  rest is a human read, recorded as a pass or an exception.

## 6. Questions that follow, in the order they depend on each other

Not to be asked together; each waits for the one before.
- Which side is the authority for each layer. Default from the rulings:
  the orrery for identity, numbers and dates ("the one definition of
  each object", L-395); the colours and the words are open.
- Where an exception lives: a file the check reads and prints every
  run, with its reason and an end condition (the belt's line on L-484
  is the shape), instead of ledger prose.
- The bound: only what both draw (The Artifact Bounds the Audit), or,
  for layer 2, every number the website shows.
- Whether the five unkeyed objects get keys, or are a documented class.
- How the check fails: an undocumented difference fails the run; a
  documented one prints with its reason (already ruled). A planted
  fault proves it, per the protocol.

## 7. At the end of the talk

A design record, `documentation/DESIGN_L484_consistency_rulings_<date>.md`,
with each ruling in Tony's words; rulings moved to L-484 (decisions)
and, where they are method, carried for interactive-exhibit's next
version. Where We Are: 12c's line and the design-talk list. Then a brief,
when the build is next.

Written November 3, 2026 with Anthropic's Claude Opus 5.5.
