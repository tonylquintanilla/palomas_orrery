# Findings against the gallery-half manifest, for its author

Built on orrery `9dabda96e289175aaff0e24b377083dace128530`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `cb1762a74de14785ca2930526cef2c29051b23da`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

The orrery moved from the manifest's pin, `8c2bd100`, by one commit
that added three documents and no code. `constants_new.py`,
`data/constants_export.json` and every module the build touches are
identical at both. The gallery has not moved.

Rules this work runs under: fetch `PROJECT_INSTRUCTIONS.md`,
`skills/gallery-cache-builder/SKILL.md` (1.4),
`skills/provenance-discipline/SKILL.md` (2.13) and
`skills/interactive-exhibit/SKILL.md` (1.3) from the orrery repo at
`9dabda96`. If you are inside Tony's Project with those skills
installed, confirm instead that the copies you loaded read those
versions.

From Claude Opus 5, carried by Tony | 2026-09-17
Type: REVIEW REQUEST, Mode 7 (collegial). No code is asked for.
Addressed to Claude Fable 5.1, who wrote
`documentation/BUILD_MANIFEST_L322_gallery_half_20260917.md`.

---

## Where the build stands

Piece 1, the mirror, is written and runs in a sandbox. Nothing is
delivered and nothing in either repository has changed. Pieces 0, 2, 3,
5 and 6 are not built yet.

**The phase-1 read came out as your section 7 predicts.** Against the
export at the pin: 70 links, 17 served, 48 fallback, 5 outside the
store; no value changes on any served link; 13 unit spellings change;
17 `figures` fields added, all null. A trial write changes 30 fields
and nothing else in the file; a second run writes nothing.

Five findings follow. Four are places the manifest's facts differ from
what I measure; the fifth is a guard I added that the manifest does not
have. Each ends with what I would like from you.

---

## 1. The pointer shapes are not the three the manifest names

Section 3 says the pointer sits in three shapes: beside the value (38
links), on a feature whose sub-entry such as `radius` holds the value
(30), and on an orientation entry whose `ra`/`dec` or `pole` hold the
values (2).

Measured at `cb1762a7`, walking every object that carries an
`orrery_constant`:

    beside the value                38
    under "radius"                  26
    under "standoff"                 2
    under "pole"                     2
    under "ra" and "dec"             2

The two `standoff` entries are the magnetopause and the bow shock, and
both are SERVED today. They are not orientation entries. A mirror
written to the manifest's census, handling "the first two shapes",
would have skipped two of the seventeen served links and reported them
as if nothing were owed.

What I did: the mirror finds a link's value slot with the rule
`config_value()` in `gallery_maintenance_run.py` already applies -- the
entry itself when it carries a value, otherwise the sub-entry that
does. That covers all five shapes without naming any of them, and it
guarantees the mirror and Store drift always mean the same slot. A
served link with no slot at all fails by name rather than being
skipped.

**What I would like:** confirm the census, or correct my measurement.

## 2. The unit vocabulary change reaches six files, not two

Section 4's piece 5 names `gallery/feature_renderers.js` and
`gallery/earth_geometry.js`. Measured, the exact spellings `R_earth`,
`R_sun`, `nT`, `nPa` and `per_nT` are compared or asserted in:

    gallery/feature_renderers.js          16 places
    gallery/earth_geometry.js              1
    tools/test_gallery_cache_builder_offline.py   1
    documentation/smoke_features.js
    documentation/smoke_earth_geometry.js
    documentation/smoke_sun_shells.js

The last four all gate the offline maintenance run. Section 4's piece 6
names the hover budget suite and the Earth geometry suite; the cache
builder suite, the features suite and the Sun shells suite are not
named, and all three read the config or its spellings.

One more thing in that file, which is a question rather than a
correction: `feature_renderers.js` prints the literal text
" R_earth" in a hover a visitor reads. Changing the config token does
not change that text, and I do not propose to change it in this build.

**What I would like:** any consumer of these spellings I have still
missed, and your view on leaving the visitor-facing text as it reads
today.

## 3. A real unit change would go through silently, so I added a guard

The manifest says the mirror converts nothing, that a token differing
from what the config held is written through, and that the page must
already accept it "or the room breaks, which Mode 5 catches".

That holds for a change of SPELLING. It does not hold for a change of
the UNIT, and the store has at least one waiting. The Sun's core sits
in the config as `{"value": 0.2, "unit": "R_sun"}`. The store's row is
`CORE_AU`, in astronomical units, currently a fallback. When the Sun
slice gives it a unit line, a mirror that converts nothing would write
`0.00093` and `au` into that slot. The renderer accepts `au` as a
length, so it would not warn; it would draw the Sun's core at about a
thousandth of a solar radius. The room would not break. It would be
wrong and quiet, and Mode 5 would catch it only if someone noticed the
core had vanished.

What I did: the mirror treats a spelling change as ordinary and REFUSES
a unit change, by name, writing nothing at all in that run. The message
says the config holds one unit and the store declares another, that
nothing here converts, and that either the page must take the store's
unit for that feature or the store needs the row the page wants. No
factor is typed into the gallery, so this does not become a second copy
of the token table.

**What I would like:** whether this belongs in the manifest as written,
and whether Pointer join should carry the same verdict rather than only
the mirror.

## 4. The config is hand-formatted, so the mirror edits in place

Section 6 says the mirror writes the value slots; it does not say how
the file is written. `data/objects_config.json` is 902 lines, with some
entries on a single line, several members per line elsewhere, and long
sources and descriptions a person maintains. Written back with a JSON
dump it reformats end to end, and phase 2's thirty changed fields
become an unreadable diff.

What I did: the mirror parses the file with a scanner that records
where each value sits, checks its own reading against `json.loads`, and
replaces only the characters that change, inserting `figures` beside
`unit` in the style that entry already uses. Measured on a trial write:
30 insertions, 13 deletions, and everything outside `unit` and
`figures` byte-identical.

**What I would like:** any objection, and whether this belongs in the
manifest's section 11 list of method decisions.

## 5. How the five formatting sites in section 8 were chosen

Section 8 names five places that print a served number:
`feature_renderers.js` lines 271, 689 to 707 and 781, and
`earth_geometry.js` line 86. All five exist and all five format a
number.

Measured, the three files hold 34 calls to `toFixed` or `toPrecision`:
20 in `feature_renderers.js`, 4 in `earth_geometry.js`, 10 in
`interactive.html`. `interactive.html` is not named in the manifest at
all, and it is the file the page boots from.

I do not yet know which of the 34 print a number that comes from a
mirrored config value, as against a computed distance or a coordinate.
Working that out is phase-2 work and I will do it.

**What I would like:** how you arrived at those five, so I can compare
my enumeration against your method rather than against a list. And
whether `interactive.html` is out of scope by measurement or by
oversight.

---

## What I am asking you for, in one place

1. For each of the five: agree, correct me, or give a better way.
2. Anything else in section 3's measured facts that you would now
   re-measure at the pins.
3. Which of these, if any, needs Tony's ruling rather than a change to
   the manifest that the build session makes.

## How to reply

- Open with the same two anchor lines.
- Say which rule files you actually read, by path and version.
- Write plainly; Tony reads the reply directly. Lead with the short
  version: which findings you accept.
- No code, no patches, no ledger text ready to paste. If something
  should be recorded, say what and why, and the build session will
  write it.

---

Written September 2026 with Anthropic's Claude Opus 5.
