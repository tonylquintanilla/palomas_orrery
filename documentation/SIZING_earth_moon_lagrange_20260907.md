# Earth-Moon Lagrange Points -- Sizing Note

Built on orrery `d7151aafd8563901e3e1f478be0f4f280da56849`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `92e98ca98e15e0425a48931fca9365f0b52f426f`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | Claude Fable 5.1 | 2026-09-07
Protocol v3.54. Ledger: L-291 (Earth exhibit), step 2 open question 1.
Skills read for this note: interactive-exhibit 1.0, gallery-cache-builder
1.4, gallery-assembler 1.2, ledger-and-session-records 1.10.

This note sizes the work. It decides nothing; the choice is Tony's.

---

## What was read

- `tools/gallery_cache_builder.py` at gallery HEAD: the per-object build
  (lines 745-800), the last-good fallback (910-935), the validator
  (1135-1150), `build_position_file` (685-720).
- `gallery/assembler/assemble.py` (dispatch, lines 50-72),
  `resolver.py` (object resolution, 150-230), `render_spacecraft.py`
  (stub), `render_orbits.py` header.
- `data/solar-system/coverage_index.json` entries for earth, moon,
  voyager_1; `data/objects_config.json` for the same three.
- `interactive.html`: the scene spec's `epoch` (line 1313) and its
  source, `EPOCH_ISO` = today at 00:00 UTC (line ~1712).
- Orrery `celestial_objects.py` lines 301-330: EM-L1..L5 are Horizons
  3011-3015, already fetched by the orrery.

## What the serving path can do today

The builder serves exactly three shapes, and the validator enforces
them:

1. OSCULATING -- every object whose category is not `spacecraft`. The
   builder fetches elements unconditionally (line 753) and the validator
   aborts if they are missing (#3, line 1145).
2. POSITIONS -- category `spacecraft` only. A full arc file, no
   elements. Written by `build_position_file`.
3. FEATURES-ONLY -- an entry with shells and no orbital data (the Sun).

Every object also carries `as_of_today`: one position at the build
epoch, in km, from the same vector fetch that runs for all objects. It
is stored today as a cross-check and never rendered (`render_orbits.py`
line 18; `assemble.py` line 61).

The assembler draws an object ONLY if it has `osculating`
(`assemble.py` line 54). Anything else is silently skipped. The
spacecraft renderer is a stub that raises.

A Lagrange point fits none of the three. Elements for it are
meaningless (a two-body fit would give a wrong period), a spacecraft
arc is the wrong shape, and it has no shells.

## One thing that helps

The exhibit's epoch and the cache's epoch are THE SAME INSTANT. The
scene spec uses today at 00:00 UTC; the builder's `today` is the same.
So an `as_of_today` marker is not stale relative to the scene -- it is
the scene's own epoch, as long as the nightly ran. The Moon moves about
13 degrees a day, so this mattered.

## Option A -- serve as epoch markers (the handoff's assumption)

Builder (gallery repo):
- A fourth serving shape, say `availability: "libration"`, that SKIPS
  the elements fetch at step 3a, KEEPS the vector fetch so
  `as_of_today` is populated, sets `osculating` and `positions` null,
  and records trust method `epoch_marker` with no window.
- A validator branch for it (the validator otherwise aborts the whole
  build on #3 -- this cannot be added to config alone).
- Five config entries: 3011-3015, center `@399`, parent earth, frame
  parent-relative, `features: {}`.
- Offline test file additions for the new shape.
- The last-good fallback (line 910) needs a branch too, or a Horizons
  outage drops the five points with a warning. Acceptable to warn.

Assembler (gallery repo):
- One branch in `assemble.py`: if no `osculating` and category is
  libration, build a marker and label from `as_of_today` (km to AU).
- A docstring stating this is the one case where `as_of_today` IS the
  rendered marker, so the header rule in `render_orbits.py` is amended
  rather than quietly contradicted.

Then: the nightly must run ONCE before anything renders, so the points
cannot appear in the same session that writes the code. Then Mode 5.

Size: one full session of its own, two files in the builder path, one
in the assembler, and a night's wait. Not an afternoon inside the
Earth build.

What it gets right: the positions are Horizons', including the Sun's
perturbation; provenance is the fetch itself, same as every other
object.

## Option B -- compute from the Moon's marker

The Earth-Moon points are geometry relative to the Moon. The assembler
already propagates the Moon's marker at the scene epoch. L4 and L5 are
that vector rotated 60 degrees each way in the Moon's orbit plane; L1,
L2 and L3 sit on the Earth-Moon line at fractions of the Earth-Moon
distance fixed by the mass ratio (about 0.849, 1.168 and 0.993 --
RECALLED, not checked; would be derived in code from the mass ratio,
not typed).

- No builder change. No config entries. No nightly wait.
- About 40 lines in the assembler beside the Moon branch, plus the
  Earth/Moon mass ratio. NEITHER MASS IS IN `constants_new.py` today
  (grep for mass, GM_ finds only the Sun's) -- one sourced constant to
  add, same patch as the rest of step 2.
- Follows the scene epoch by construction, and will keep following it
  if the exhibit ever gets a date control.

Size: fits inside the Earth build.

What it gets wrong, and the hover must say so: this is the circular
restricted three-body approximation. It ignores the Sun and the Moon's
eccentricity. The real points wander from these positions by the size
of those perturbations. Under Show the Envelope this is the
"approximate/stylized, say so" branch. It is also local math in the
assembler -- the same kind the assembler already does (Kepler), but
more of it.

## Option C -- ship Earth without them

Named as legitimate in the handoff. The drawer row waits; L-292's
class row (orrery shell additions) is unaffected; a new ledger row
records the two options above so the decision is not re-derived.

## Not sized here

Sun-Earth L1-L5 (L-294) -- ruled to the heliocentric room. Whichever
option is chosen for Earth-Moon should transfer: A serves them the same
way; B computes them from Earth's marker with the Sun/Earth mass ratio.

---

Written September 2026 with Anthropic's Claude Fable 5.1.
