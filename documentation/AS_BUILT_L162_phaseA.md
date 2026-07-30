# AS-BUILT: Phase A -- L-162 CENTER_BODY_RADII Named Constants

Tony Quintanilla, PE | Claude Sonnet 5 | July 29, 2026

**Built on:** orrery (palomas_orrery) @ `90d022e4e4b39c19698e6d4ce64087d66ae35ac1`
at https://github.com/tonylquintanilla/palomas_orrery (branch main)

**Type:** BUILD SESSION. Three files touched, all existing code -- targeted
snippets below, not complete files, per this project's own editing
discipline. Folded into this thread per your request to close the
parallel track; this replaces that track's own build of the same item.

**Scope, exactly as both tracks converged on it:**
1. 14 new plain-form named constants in `constants_new.py`
2. `CENTER_BODY_RADII` rewired to reference all 17 names (Sun/Earth/
   Jupiter included)
3. Re-point the 9 relevant aliases in `planet_visualization_utilities.py`
4. `CONCEPT_ALIASES` entries for all 14 new names
5. Pre-flight check for the Sun/Jupiter int-to-float change
6. Compile + ASCII/LF gate + credit lines + this as-built

No open decisions going in -- naming (plain), ownership (this item owns
Sun/Earth/Jupiter's fix too), and the alias-layer call (re-point,
superseding v3.20 Option B) were all settled before this session started.

---

## Pre-flight: the int-to-float question, resolved before writing

`Sun` and `Jupiter` change from raw int literals (`695700`, `71492`) to
referencing their own float constants (`695700.0`, `71492.0`). Checked
every consumer of `CENTER_BODY_RADII` in the repo (`palomas_orrery.py`,
`idealized_orbits.py`, `close_approach_data.py`, `apsidal_markers.py`,
`orrery_rendering.py`, `planet_visualization.py`, plus the two files
edited here) for `:d`/`%d`-style integer-only formatting: zero hits. All
consumers do arithmetic or generic dict lookups, both indifferent to
int vs. float. No risk found; proceeded.

## Files changed

### 1. `constants_new.py` -- 14 new named constants + `CENTER_BODY_RADII` rewire

New subsection inserted immediately above `CENTER_BODY_RADII` (after the
existing hybrid-convention commentary, which stays as introductory
context for the whole dict):

```python
# ------------------------------------------------------------
# Named constants (L-162, 2026-07-29): the 14 remaining bodies,
# promoted from CENTER_BODY_RADII dict entries to their own named
# constant, same pattern as SUN_RADIUS_KM / EARTH_EQUATORIAL_RADIUS_KM /
# JUPITER_EQUATORIAL_RADIUS_KM above. Value and citation carried forward
# unchanged from the dict entry each replaces -- no new sourcing done
# in this pass. Planet 9 excluded (model estimate; L-159).
# ------------------------------------------------------------

MERCURY_RADIUS_KM = 2439.7
# Source: NASA Fact Sheet (volumetric mean; oblateness ~0.0009)

VENUS_RADIUS_KM = 6051.8
# Source: NASA Fact Sheet (volumetric mean; oblateness ~0)

MOON_RADIUS_KM = 1737.4
# Source: NASA Fact Sheet (volumetric mean; oblateness ~0.0012)

MARS_RADIUS_KM = 3396.2
# Source: IAU 2015 nominal equatorial (volumetric = 3389.5)

PHOBOS_RADIUS_KM = 11.1
# Source: NASA/JPL Solar System Dynamics group

SATURN_RADIUS_KM = 60268
# Source: IAU 2015 nominal equatorial (volumetric = 58232)

URANUS_RADIUS_KM = 25559
# Source: IAU 2015 nominal equatorial (volumetric = 25362)

NEPTUNE_RADIUS_KM = 24764
# Source: IAU 2015 nominal equatorial (volumetric = 24622)

PLUTO_RADIUS_KM = 1188.3
# Source: New Horizons occultation (Nimmo et al. 2017)

BENNU_RADIUS_KM = 0.262
# Source: Volumetric mean (top-shape asteroid, OSIRIS-REx)

ERIS_RADIUS_KM = 1163
# Source: Volumetric mean (Sicardy et al. 2011 occultation)

HAUMEA_RADIUS_KM = 816
# Source: Volumetric mean (highly ellipsoidal: 1050x840x537 km)

MAKEMAKE_RADIUS_KM = 715
# Source: Volumetric mean (Brown et al.)

ARROKOTH_RADIUS_KM = 9.95
# Source: Volumetric mean (~35x20x14 km bilobed shape)
# Corrected 2026-04-15 per Gemini review (was 0.0088 = 8.8 meters!)
```

`CENTER_BODY_RADII` itself, search for the old dict (18 raw-literal
entries) and replace the whole literal with:

```python
CENTER_BODY_RADII = {       # km (equatorial for major bodies, volumetric for small)
    # L-162 (2026-07-29): all 17 named bodies now reference their own
    # named constant below instead of a raw literal -- Sun/Earth/Jupiter
    # were already named; Mercury through Arrokoth are newly promoted in
    # this pass. Planet 9 stays a raw literal -- model estimate, excluded
    # from promotion and from pinning per L-159.
    'Sun':      SUN_RADIUS_KM,
    'Mercury':  MERCURY_RADIUS_KM,
    'Venus':    VENUS_RADIUS_KM,
    'Earth':    EARTH_EQUATORIAL_RADIUS_KM,
    'Moon':     MOON_RADIUS_KM,
    'Mars':     MARS_RADIUS_KM,
    'Phobos':   PHOBOS_RADIUS_KM,
    'Jupiter':  JUPITER_EQUATORIAL_RADIUS_KM,
    'Saturn':   SATURN_RADIUS_KM,
    'Uranus':   URANUS_RADIUS_KM,
    'Neptune':  NEPTUNE_RADIUS_KM,
    'Pluto':    PLUTO_RADIUS_KM,
    'Bennu':    BENNU_RADIUS_KM,
    'Eris':     ERIS_RADIUS_KM,
    'Haumea':   HAUMEA_RADIUS_KM,
    'Makemake': MAKEMAKE_RADIUS_KM,
    'Arrokoth': ARROKOTH_RADIUS_KM,
    'Planet 9': 24000       # Model estimate (Batygin & Brown; 5-10 M_Earth assumption)
}
```

Plus a credit line in the module docstring, same place as the existing
April 2026 one:

```python
Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-162: 14
remaining CENTER_BODY_RADII bodies promoted to named constants; value
and citation carried forward unchanged from each dict entry)
```

### 2. `planet_visualization_utilities.py` -- 9 aliases re-pointed

Import list gains 9 names:

```python
from constants_new import (
    KM_PER_AU, SUN_RADIUS_KM, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS,
    CENTER_BODY_RADII,
    # L-162 (2026-07-29): named directly in constants_new.py now; these
    # nine no longer derive from a CENTER_BODY_RADII lookup below.
    MERCURY_RADIUS_KM, VENUS_RADIUS_KM, MOON_RADIUS_KM, MARS_RADIUS_KM,
    SATURN_RADIUS_KM, URANUS_RADIUS_KM, NEPTUNE_RADIUS_KM, PLUTO_RADIUS_KM,
    ERIS_RADIUS_KM,
    ...
```

The 9 alias-derivation lines (`MERCURY_RADIUS_KM = CENTER_BODY_RADII['Mercury']`
and so on) are deleted; each body's `_AU` conversion line stays exactly as
it was, now reading the imported name instead of the locally-derived one.
Earth, Jupiter, Planet 9 are unchanged -- outside L-162's 14-body scope,
no name collision with `constants_new.py` either way. Full before/after
in the attached patch file.

### 3. `provenance_scanner.py` -- 14 `CONCEPT_ALIASES` entries

Appended to the existing dict:

```python
    # L-162 (2026-07-29): the 14 bodies newly promoted from
    # CENTER_BODY_RADII dict entries to named constants. No known
    # alternate name exists elsewhere in the repo for any of these today
    # (checked); each is registered under its own canonical name so a
    # future differently-named duplicate has an anchor to be caught
    # against, per the design's hard requirement.
    'MERCURY_RADIUS_KM':  ('MERCURY_RADIUS_KM',),
    'VENUS_RADIUS_KM':    ('VENUS_RADIUS_KM',),
    'MOON_RADIUS_KM':     ('MOON_RADIUS_KM',),
    'MARS_RADIUS_KM':     ('MARS_RADIUS_KM',),
    'PHOBOS_RADIUS_KM':   ('PHOBOS_RADIUS_KM',),
    'SATURN_RADIUS_KM':   ('SATURN_RADIUS_KM',),
    'URANUS_RADIUS_KM':   ('URANUS_RADIUS_KM',),
    'NEPTUNE_RADIUS_KM':  ('NEPTUNE_RADIUS_KM',),
    'PLUTO_RADIUS_KM':    ('PLUTO_RADIUS_KM',),
    'BENNU_RADIUS_KM':    ('BENNU_RADIUS_KM',),
    'ERIS_RADIUS_KM':     ('ERIS_RADIUS_KM',),
    'HAUMEA_RADIUS_KM':   ('HAUMEA_RADIUS_KM',),
    'MAKEMAKE_RADIUS_KM': ('MAKEMAKE_RADIUS_KM',),
    'ARROKOTH_RADIUS_KM': ('ARROKOTH_RADIUS_KM',),
```

Full patch files (unified diff, exact) for all three are attached
alongside this document.

---

## Verification actually run, not just claimed

- `py_compile` clean on all three files.
- ASCII/LF gate clean on all three (zero non-ASCII bytes, no CRLF).
- **`test_constants_provenance.py` run in full: 73 passed, 0 failed** --
  every existing per-body assertion (including the ones checking
  `CENTER_BODY_RADII['Saturn'] == 60268` etc. against the raw literal)
  still passes, because the referenced named constant carries the
  identical value.
- `planet_visualization_utilities.py` imported live and every alias
  checked against its pre-edit value: all 12 match exactly (9 re-pointed,
  3 unchanged).
- Scanner re-run against the edited tree: **764 -> 778 findings (+14,
  exactly the 14 new constants -- no more, no less)**. Tier 1 unchanged
  at 145 (nothing string-level touched). Tier 3 +14 (the new constants,
  scored under the pre-Phase-1 model -- expected, will re-score once
  Phase 1 lands). Zero new INCONSISTENCIES, zero new duplicate flags,
  domain-coverage-gap section unchanged (still just `orrery_rendering.py`
  and `shell_configs.py`, untouched by this work).

## Ledger

`[L-162]` flips from `OPEN` to `DONE`. Paste-ready ledger note in the
companion file.

---

*Built July 2026 with Anthropic's Claude Sonnet 5.*
