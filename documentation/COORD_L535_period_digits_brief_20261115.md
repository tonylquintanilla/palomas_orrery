<!-- Doc-Kind: hand | The brief for one Claude Code session through the python_work door: L-535 (the period's reason), the website's period line saying what set its digits, as the orrery's does. Communication; written once, read by its session. -->
# Brief: the period line says what set its digits (L-535)

Built on orrery d0f90d181235ab160a788bafeda3304ba452fe9a at
https://github.com/tonylquintanilla/palomas_orrery
and gallery f9f81266e328d906a6ebba65375b0604c77f053c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, Tony's pushes of the Mars build, read 2026-11-15,
17:30 Chicago). Nightly bot commits since are expected. This brief is in
the orrery's documentation/ on Tony's computer, not yet pushed.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session on Tony's computer, through the
python_work door, in BOTH folders (orrery first, then the website);
records in the orrery's. Written November 15, 2026 with Anthropic's
Claude Opus 5.5, the coordinating session.

## What this is, in one paragraph

Tony's phone look at Phobos, Nov 15 (run record
`documentation/WHERE_WE_ARE_11-15-26_0837_run_record.md`): "0.31914 days
from JPL, but it does not say if JPL provides this as the precision
too." Then, 17:24: "we should fix this in this session. easily
overlooked." The orrery's own period text ends with one sentence saying
what set the digits (`orbital_period.period_hover_lines`: "Rounded to
how much the period changes in a year.", "Rounded to JPL's stated
uncertainty in the orbit.", and the small-body database variants). The
website prints the same period with no such sentence, for every body: the
export's period block carries `"words": None` for a fetched period, and
the reason (`error_from`, `sbdb_status`) sits only in its `record`, which
`tools/mirror_objects.py` (`period_copy`) deliberately does not copy. A
caveat belongs beside its number (interactive-exhibit, Hover text is
written for the visitor), so the website gains the orrery's sentence.

## The work

Part 1, the orrery:
- One function gives the sentence, used by both the orrery's own hover
  and the export, so the words have one source; the sentence is the
  orrery's existing wording, not new words.
- `export_objects.py` writes it into the period block (a field of the
  session's choosing, named in the report), as plain text: a hard
  `<br>` inside it is a fault on the website (the SOFT_BR rule).
- The orrery's maintenance run, read for its own green line. Report the
  sentence each kind of body now exports (a planet, a moon, an asteroid
  with JPL's uncertainty, one without), and stop.

Part 2, the website:
- Confirm FIRST, before Tony pushes the orrery, that the website's night
  stays green when the orrery's export carries the new field before the
  website knows it (Nov 15: an orrery key ahead of the website's config
  turned two nights red, L-514). If it would not, say so and propose the
  push order before anything else.
- The pull; `periodLine` in `gallery/solar_system_figures.js` prints the
  served sentence after the period, never typed in the page (Typed facts
  check).
- The Hover budget check (the phone's text box under its ceiling) and
  the Display figures fixture, re-recorded: name every hover that
  changed, and confirm the change is that sentence alone.
- The headless walk for one planet and one moon; the gallery run, read
  for its own line.
- Before and after, word for word, for Mars and for Phobos, brought to
  Tony: a reworded hover goes to him before it ships. Then stop.

Part 3, the records: L-535 (the period's reason), L-514 (the Mars room)
where it touches the look, Where We Are by section, the final report as
CLAUDE.md asks, with the token count and the push order.

Out of scope: the rest of Tony's Mars look; the Moons group under a
planet (recorded by the coordinator for L-534's round); any change to how
the digits are worked out.

## Skills this fires

Read each and compare its version line with the manifest:
interactive-exhibit (1.42), provenance-discipline (2.36),
orrery-coding-conventions (1.13), horizons-orbital-mechanics (1.18; the
period), safe-file-editing (1.14),
agentic-pre-test (1.3), and ledger-and-session-records (1.23).

## Start

1. Record the base in both folders (`git rev-parse HEAD`, `git
   ls-remote origin HEAD`, `git status`); stop if they disagree.
2. Read the skills above; name each with its version line.
3. Say Part 1 in one sentence and wait for Tony's go-ahead.

Plain speech, one question per message. Commit and push are Tony's.

Brief written November 15, 2026 with Anthropic's Claude Opus 5.5.
