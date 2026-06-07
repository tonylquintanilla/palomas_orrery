# Fact-Check Worksheet: mercury_visualization_shells.py

## Instructions for Gemini

Mercury shell file, 8 findings. Please verify each claim.

---

## Group A: Outer Core (lines 75, 88)

| # | Claim | Value |
|---|-------|-------|
| A1 | "liquid metallic outer core" | Confirm |
| A2 | "source of Mercury's weak magnetic field" | Confirm |
| A3 | Outer core thickness | "about 1074 km thick" |

Note: 1074 km is suspiciously precise for a value we can't
directly measure. Confirm this is from MESSENGER data/models.

Likely source: NASA MESSENGER mission.

---

## Group B: Crust (lines 177, 193)

| # | Claim | Value |
|---|-------|-------|
| B1 | "solid silicate crust...heavily cratered" | Confirm |
| B2 | Diamond theory: "significant portion...might be made of diamonds, formed by billions of years of meteorite impacts on a graphite-rich surface" | Confirm — is this published? |
| B3 | Crust thickness | "about 35 km thick" |

Note on B2: The diamond crust theory is intriguing. Is this
from a specific paper? Need citation.

Likely source: NASA MESSENGER; Murchie et al. or similar.

---

## Group C: Exosphere (line 333)

| # | Claim | Value |
|---|-------|-------|
| C1 | Composition: "mostly oxygen, sodium, hydrogen, helium, and potassium" | Confirm |
| C2 | Atoms "blasted off the surface by the solar wind and micrometeoroid impacts" | Confirm |

Likely source: NASA MESSENGER.

---

## Group D: Sodium Tail (line 407)

| # | Claim | Value |
|---|-------|-------|
| D1 | Tail extends "up to 10,000 Mercury radii" | Confirm |
| D2 | "approximately 24 million kilometers" | Check: 10,000 * 2,440 km = 24.4 Mkm — math checks out |
| D3 | "or 2.4 million km" | **LIKELY TYPO** — should be 24 million km, not 2.4 million km. The "or" clause is off by 10x |
| D4 | "created when sodium atoms...pushed away by solar radiation pressure" | Confirm |
| D5 | "can be observed from Earth using specialized telescopes" | Confirm |

**Priority flag:** D3 appears to be a decimal error. "24 million
kilometers or 2.4 million km" — those are not the same number.
One of them is wrong.

Likely source: Potter & Morgan (1990s), MESSENGER sodium tail
observations.

---

## Group E: Magnetosphere (line 527)

| # | Claim | Value |
|---|-------|-------|
| E1 | "surprisingly active magnetosphere, given its small size and slow rotation" | Confirm |
| E2 | "significantly weaker and smaller than Earth's" | Confirm |

Likely source: NASA MESSENGER.

---

## Group F: Hill Sphere (line 698)

| # | Claim | Value |
|---|-------|-------|
| F1 | No specific numeric value given — just conceptual | Low priority |
| F2 | "closest planet to the Sun, the Sun's powerful gravity limits the extent" | Confirm |

Note: The info string doesn't give a numeric Hill sphere value.
For reference, Mercury's Hill sphere is approximately 175,000 km
(~72 Mercury radii, ~0.0012 AU). If you want a number added,
please provide.

---

## Summary

Sources likely needed:

1. NASA MESSENGER Mission (interior, exosphere, magnetosphere, sodium tail)
2. Potter & Morgan / MESSENGER sodium tail papers
3. NASA Mercury Fact Sheet

**Priority fix:** D3 decimal error (2.4 vs 24 million km).
