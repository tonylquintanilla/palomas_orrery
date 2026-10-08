<!-- Doc-Kind: hand | Session record: L-421 (the typed facts), October 6 to 8, 2026 -- what was built, what Tony ruled, and what is left for the next session. -->
# Handoff: L-421 (the typed facts), October 6 to 8, 2026

Built on orrery 36176d5075fc8e896e2176c39bc053237a37ddbe at
https://github.com/tonylquintanilla/palomas_orrery and gallery
ab66aba70a5874b033742a8428070b5889484490 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
The session started at orrery fbd223ee and gallery 8487b0f8, from
`documentation/MANIFEST_L421_typed_facts_20261006.md`.

- Type: BUILD, gallery. Three patches, run and pushed by Tony.
- Skills: interactive-exhibit loaded at 1.12, matching the manifest,
  which discharged the obligation carried from v3.84. The ledger skill
  was read at 1.17 from the repo at HEAD for this close.

## What was built

All three in the gallery repo. No word a visitor reads changed in any
of them; each was applied to a fresh clone of the base it names,
matched the working copy byte for byte, refused a second run, and
passed 24 of 24 gating checks.

- **patch_L421_1** (pushed at 6fae15e0). The geostationary ring, the
  magnetopause, the bow shock and the magnetotail each print a served
  `hover` word from `data/objects_config.json`. Earth's belts print three
  parallel lists, `hovers_band`, `hovers_rings`, `hovers_plane`. A
  `{name}` blank is filled from a served row. `store_writer.py` and the
  editor know the new fields. Items E5 to E10.
- **patch_L421_2** (pushed at 4cfeca27). The rotation axis, the Sun
  line, the terminator and the Moon's arc print served words from
  Earth's `orientation.words`, each entry with its source. The pole of
  date's source line prints from the cache builder's served record (it
  matched the typed copy when that was deleted). The Sun's clumpy outer
  cloud and galactic tide print served words. The panel's words, its
  footer and the frame note's source line move from a 2.6:1 grey to the
  6.3:1 paragraph grey. Items E1 to E4, E11 to E13, S2, S3.
- **patch_L421_3** (pushed at ab66aba7). The four guides get Read more
  links, each a Wikipedia article returned live by a search that day.
  The cause of the missing link was in `interactive.html`: the panel took
  a group's link and source only from its first and legend traces, and
  the guides keep theirs on the info marker. It now fills an empty value
  from any trace and never overwrites one. Measured headless in all
  three rooms: only those eight Earth values changed.

## Sources read

Round 1 is recorded in `documentation/L421_round1_sources_20261006.md`.
The sense of rotation cites Archinal et al. (2019), the correction
(Fig. 1), from the PDF Tony supplied, with the USNO glossary's diurnal
and direct motion. The 2018 report was not re-read and is no longer
cited.

## Tony's rulings and verdicts

Quoted from `documentation/WHERE_WE_ARE_10-7-26_0832_run_record.md`
(his latest copy, 2,125 lines) and from chat.
- Patch 1, the six hovers on the phone: "correct".
- Patch 2: "All type is correct."
- Patch 3, each of the four links: "correct".
- The inner Oort cloud: "remember this is part of the sun slice not
  deferred."
- On the header: he meant the Sun Direction's missing link, not header
  icons.

## What is left, for the next session

1. **The inner Oort cloud, redrawn.** Nesvorny et al. (2025, ApJ 983):
   a slightly warped disk about 15,000 au across, tilted about 30
   degrees to the ecliptic, its ends twisted toward the galactic poles,
   the tilt a range that can be drawn as an envelope. First trace what
   uses the cloud's outer edge: the paper puts the disk at 1,000 to
   10,000 au, the served cloud runs 2,000 to 20,000. Then the one
   question to Tony, the new words to Tony, the build, his look.
2. **The check.** The survey that found the 17 becomes a gating check in
   the gallery run, shown failing on a planted typed sentence first.
3. Still unchecked: whether each served number's citation in
   `data/objects_config.json` agrees with its row's in
   `constants_new.py`.
4. Owed elsewhere: the served-hover method is on L-351 (what each
   skill is owed) for interactive-exhibit's next bump; L-363's
   `_declared` "1.1 times" did not ride these patches.

## Lesson

A link that was served still did not show, because the panel read
only two of a group's traces. Every check passed; Tony's look found it.
The headless page harness then measured the fix across all three rooms.

Session written October 2026 with Anthropic's Claude Opus 5.5.
