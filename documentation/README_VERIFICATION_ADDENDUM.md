# README Rewrite -- Verification Addendum (base 89cd85ba)

**Re-verified against:** orrery HEAD
`89cd85ba93177904a0a61b0072acebac629dcf5e` (SHA round trip confirmed;
full checkout inspected). Companion to
`documentation/README_CHANGE_NOTE.md`, which Tony has already committed
byte-identical to the original deliverable -- this addendum records the
delta, it does not replace that note.

## State of the new base

- Root has NO README.md -- the slot is staged for this deliverable.
- Old README archived at `documentation/README_5_4_26.md` (resolves the
  change note's open question 2: cut beginner/install content is
  preserved there; nothing further to relocate).
- `MODULE_INDEX.md` at root, generated July 17 by `module_atlas.py`;
  old index archived as `documentation/MODULE_INDEX_old.md`.
- `MODULE_ATLAS.md` at root, July 17: **121 modules | 955 functions |
  92,000 lines** -- the README's "121 modules and roughly 92,000
  non-blank lines" now matches the committed atlas exactly.
- **Both CRITICAL flags from the change note are RESOLVED.** The
  MODULE_INDEX.md root link resolves; the atlas counts agree.

## Two edits made to the README for the new base

1. **Orbital mechanics link updated to the current version.** Root's
   `ORBITAL_MECHANICS_README_v3_1.md` is stale (March 4); the current
   edition is `documentation/ORBITAL_MECHANICS_README_v3_3.md`
   (March 16: solution-level TP, non-grav acceleration delta, position
   timestamps). The key-documents table now links v3_3, and the stale
   root file is dropped from the layout diagram.
2. **Layout diagram note** that `documentation/` also holds archived
   prior README versions.

Full link audit re-run at 89cd85ba: all 12 relative links resolve.
ASCII-only, LF-only gates pass.

## Remaining open items (small)

- **Root `ORBITAL_MECHANICS_README_v3_1.md` is now an orphan** -- two
  versions behind its documentation/ successors and no longer linked
  from the README. Suggest removing it from root (or moving it into
  documentation/ with its siblings) so the repo doesn't carry a stale
  copy at top level. Tony's call.
- The committed change note's open question 4 mentioned
  `README_DEPLOYMENT_v2.md` at root -- it has since moved to
  documentation/, so that question is moot.
- Open questions 3, 5, 6, 7 from the committed change note remain as
  written.

-- Claude Fable 5, July 17, 2026.
