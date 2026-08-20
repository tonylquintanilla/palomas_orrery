# L-214 measurement -- what the request builder drops, with its text

**Built on `97c520177b18d69e6b5d3943557fdea47f56e8bf` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Produced with the project's own `worksheet_checker.collect_claims`,
`worksheet_keys.LEG_RE`, `OTHER_LABEL_RE` and `continues_a_leg` -- not
a grep. Two checks confirm the method before any of it is read:

- It reproduces the ledger's published L-214 count exactly: **12 lines
  at 12 of 55 claim sites**, 128 files read.
- It reproduces the corpus's known-good current state: **0 unmarked
  continuations today**, which is why the pilot dispatched at all.

Blind spot, announced rather than dropped: `collect_claims` reports **22
unreached `# Cross-checked:` lines** that attach to no unit. All are
record legs, so none can enter the count below, but the number is here
rather than absent.

---

## Part 1 -- the 12 dropped lines, with the text that follows them

The label line is what the count found. The indented lines under it are
continuation text that is dropped along with it today, because the drop
closes the run.

### `KM_PER_AU`  -- constants_new.py:54  (label `Note`)

```
# Note: 1 AU = 149,597,870,700 m exactly. We use km (divide by 1000).
```

### `SUN_RADIUS_KM`  -- constants_new.py:62  (label `Note`)

```
# Note: This is the IAU nominal value (conversion constant), not a
# measurement. The measured photospheric radius is ~696,340 km
# (Haberreiter et al. 2008). Use nominal for all calculations.
```

### `EARTH_EQUATORIAL_RADIUS_KM`  -- constants_new.py:72  (label `Note`)

```
# Note: B3 rounds to 6378.1 km; full precision from IERS Conventions
```

### `CHROMOSPHERE_PHYSICAL_KM`  -- constants_new.py:175  (label `Note`)

```
# Note: the PHYSICAL extent, and since 2026-08-16 the drawn one too.
#       CHROMOSPHERE_PHYSICAL_RADII below converts it to solar radii and
#       is what the shell draws at. The 1.1 stylization is retired.
```

### `INNER_CORONA_RADII`  -- constants_new.py:186  (label `Note`)

```
# Note: Visualization boundary for inner (K-)corona; physical extent 2-3 R_sun
```

### `STREAMER_BELT_RADII`  -- constants_new.py:197  (label `Note`)

```
# Note: Visualization cutoff at upper end of 4-6 R_sun observed range;
#   streamer-belt structure remains observable beyond 6 R_sun.
```

### `ROCHE_LIMIT_RADII`  -- constants_new.py:205  (label `Note`)

```
# Note: Roche limit is NOT absolute; tensile strength allows survival
# inside it. Ikeya-Seki survived at 1.66 R_sun.
```

### `HELIOPAUSE_RADII`  -- constants_new.py:252  (label `Note`)

```
# Note: This is in solar radii, not AU. 121.6 AU * 149597870.7 / 695700 = 26148 R_sun
```

### `PARKER_CLOSEST_RADII`  -- constants_new.py:294  (label `HELIOCENTRIC`)

```
# HELIOCENTRIC: 9.86 from Sun center. NASA press reports ~3.83 Mkm above
#   the surface = 8.86 R_sun altitude. Same orbit, different reference.
```

### `mercury_sodium_tail_info`  -- mercury_visualization_shells.py:97  (label `Note`)

```
# Note: Potter & Morgan 1985 is the exosphere sodium DISCOVERY paper; it does not
#       establish tail extent. The former "10,000 R_M" was unsupported by either
#       source and has been replaced with the observed range.
```

### `moon_hill_sphere_info`  -- moon_visualization_shells.py:586  (label `Note`)

```
# Note: SINGLE-LEG. Only the Claude tier-2 worksheet carries the 58,147-64,901 km
#       range. GPT and Gemini converged on method and inputs but did not publish
#       this range. A second independent leg is still owed for V2 scoring.
```

### `venus_atmosphere_info`  -- venus_visualization_shells.py:339  (label `NOTE`)

```
# NOTE: duplicated text -- the description entry in create_venus_atmosphere_shell
#       below carries a <br> copy of this block. Edit both copies together.
```

---

## Part 2 -- what adding `Note` to CONTEXT_LEGS does on its own

Simulated by rebuilding `LEG_RE` with `Note` added and re-running
`legs_of` over the same 55 claim sites.

| | unmarked continuation lines | sites | builder |
|---|---|---|---|
| today | 0 | 0 | writes |
| with `Note` added | 10 | 6 | **REFUSES** |

The 10 lines are the continuation text in Part 1. They carry no
`# Note+:` marker, so once `Note` is a recognised leg they become
unmarked continuations and the L-195 ratchet stops the run. Marking them
is the same patch; the result is that the whole note travels rather than
its first line.

---

## Part 3 -- the one line that is not like the others

`moon_hill_sphere_info`, `moon_visualization_shells.py:586`:

```
# Note: SINGLE-LEG. Only the Claude tier-2 worksheet carries the 58,147-64,901 km
#       range. GPT and Gemini converged on method and inputs but did not publish
#       this range. A second independent leg is still owed for V2 scoring.
```

This names which model produced the range, says the other two did not,
and states that a second independent leg is still owed. That is what
`worksheet_checker.py:1607` excludes `Resolved` from `CONTEXT_LEGS` to
prevent: a row dispatched a second time must not be shown what the last
one concluded. Shipping `Note` text wholesale ships this too.

`venus_atmosphere_info` is a milder case in the other direction --
a code-maintenance note about duplicated text, of no use to a responder,
but harmless if it travels.

