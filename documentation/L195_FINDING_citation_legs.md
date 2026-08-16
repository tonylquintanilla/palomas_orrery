# L-195 finding -- where the authority is not in the `# Source:` line

**Built on `a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**
HEAD confirmed by live `git ls-remote` at the start of this session.
Gallery repo at `30b6968`, untouched.

Lands in `documentation/`.

---

## The population, measured

| Scope | Count |
|---|---|
| Comment blocks in the repo containing a `# Source:` line | 333 |
| Blocks also carrying a `# Ref:` / `# Also:` leg | 19 |
| ...in `constants_new.py` | 17 |
| ...in `sgr_a_star_data.py` | 1 |
| ...in `orbital_elements.py` | 1 |
| Rows in the 65-row dispatch whose block carries a non-Source leg | 13 |
| **Of those 13, blocks where the authority is NOT in the Source line** | **6** |

The handoff's figures were 337 blocks and 20 multi-leg, described there
as a floor. The difference is block definition: that scan broke a run
on an unlabeled continuation comment, this one keeps a contiguous
comment run together. Neither is wrong; 19 and 333 are what a
whole-run definition gives at `a872205`.

The dispatch corpus is 65 rows over 7 files: `constants_new.py` 24,
`pluto_visualization_shells.py` 18, `venus_visualization_shells.py` 14,
`eris_visualization_shells.py` 4, `mars_` 2, `mercury_` 2, `moon_` 1.
All 13 multi-leg rows are in `constants_new.py`. No shell module has a
multi-leg block.

---

## The six

Every one of them is in the outgoing dispatch.

| Constant | Value | `# Source:` line says | Real authority, currently in `# Ref:` |
|---|---|---|---|
| `STREAMER_BELT_RADII` | 6.0 | Eclipse observations; helmet streamers extend 4-6 R_sun | Golub & Pasachoff (2010); DeForest, Howard & McComas (2014), ApJ 787:124 |
| `ROCHE_LIMIT_RADII` | 3.45 | Fluid Roche limit formula: d = 2.44 * R * (rho_sun/rho_comet)^(1/3) | Murray & Dermott, *Solar System Dynamics* (1999), Sec. 4.6 |
| `ALFVEN_SURFACE_RADII` | 18.8 | Parker Solar Probe first crossing, April 28, 2021 | Kasper et al. (2021), Phys. Rev. Lett. 127:255101 |
| `TERMINATION_SHOCK_AU` | 94 | Voyager 1 crossed at 94 AU (Dec 2004) | Stone et al. (2005), Science 309:2017 |
| `HELIOPAUSE_RADII` | 26148 | Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012) | Gurnett et al. (2013), Science 341:1489 |
| `PARKER_CLOSEST_RADII` | 9.86 | Parker Solar Probe perihelion 22, Dec 24, 2024 | https://parkersolarprobe.jhuapl.edu/The-Mission/index.php |

Three shapes of wrongness, all the same failure: an **event**
(a spacecraft crossing), a **method** (eclipse observation), or a
**formula** standing where a retrievable authority should be.

### The evidence is in the code, not in my reading

Each of these blocks carries `# Cross-checked:` lines naming what the
2026-08-02 checkers actually verified against. For all six, the named
authority is the **Ref** line, not the Source line:

- `STREAMER_BELT_RADII` -> Gemini recorded *Golub & Pasachoff*, GPT recorded *DeForest et al.*
- `ALFVEN_SURFACE_RADII` -> both recorded *Kasper et al.*
- `TERMINATION_SHOCK_AU` -> both recorded *Stone et al.*
- `HELIOPAUSE_RADII` -> both recorded *Gurnett et al.*
- `PARKER_CLOSEST_RADII` -> Claude recorded *JHUAPL/Riley et al.*, GPT recorded *NASA PSP mission data*
- `ROCHE_LIMIT_RADII` -> both recorded *formula verified* (no source named at all)

For the seven clean rows the same test passes the other way: the
Cross-checked clause names exactly what the Source line says
(*IAU B2*, *IAU B3*, *IAU B3 / IERS*, *NIST/SI*). Twelve of thirteen
agree with their Source line or with their Ref line, never ambiguously.
The one that names neither is `ROCHE_LIMIT_RADII`.

### Two of the six are circular

`TERMINATION_SHOCK_AU` and `HELIOPAUSE_RADII` have Source lines that
restate the claim being checked. Asking a responder "is this citation
correct?" against *"Voyager 1 crossed at 94 AU (Dec 2004)"* for the
value 94 is asking whether the claim supports the claim. It cannot
return CITATION WRONG for any reason a responder could discover. That
is the v3.39 gate -- a check that cannot fail is not passing -- and it
would go out in the first dispatch.

---

## The seven that are fine, and why

`KM_PER_AU`, `SUN_RADIUS_KM`, `EARTH_EQUATORIAL_RADIUS_KM`,
`EARTH_POLAR_RADIUS_KM`, `JUPITER_EQUATORIAL_RADIUS_KM`,
`JUPITER_POLAR_RADIUS_KM`, `SPEED_OF_LIGHT_KM_S`.

In each, the Source line names a standards body and its instrument
(IAU Resolution B2, IAU Resolution B3, IERS Conventions, NIST/SI) and
the Ref line is a locator for that same authority -- the resolution
PDF, the Prsa et al. 2016 paper that publishes the B3 nominal values,
the CODATA page. Authority in the Source, retrieval aid in the Ref.
That is the shape the schema was written for. **Leave them alone.**

---

## Two repair shapes

### Shape A -- swap, narrative demoted to a context leg

```python
TERMINATION_SHOCK_AU = 94
# Source: Stone et al. (2005), Science 309:2017
# See: Voyager 1 crossed the termination shock at 94 AU, December 2004
# Also: Voyager 2 crossed at 84 AU (Aug 2007) -- asymmetric
```

`See` is already in the builder's `CONTEXT_LEGS`
(`Ref`, `Also`, `See`, `Derived`, `Calculation`), so the event
narrative still prints above the table as read-only context. Nothing
is lost from the responder's view. `# Note:` would NOT work here --
it is not a recognised leg and the responder would never see it.

### Shape B -- merge onto the verdicted line

```python
TERMINATION_SHOCK_AU = 94
# Source: Stone et al. (2005), Science 309:2017 -- Voyager 1 termination shock crossing, 94 AU, December 2004
# Also: Voyager 2 crossed at 84 AU (Aug 2007) -- asymmetric
```

### The tradeoff

Shape A leaves the verdicted line as a bare authority, so the question
the responder answers is well-formed: does Stone et al. 2005 support
94 AU. Shape B keeps the paper and what it is cited for on one line,
which reads better to a human -- but it rebuilds the compound line that
made these six ambiguous in the first place, and a responder can
verdict the narrative half of it.

---

## Two things noted, not asked

**`ROCHE_LIMIT_RADII` is not like the other five.** Its value is
computed, not measured, and the block already carries `# Calculation:`
and the two density inputs (rho_sun = 1408, rho_comet ~ 500). Under
either shape the Source becomes Murray & Dermott for the *formula*.
The two densities remain uncited inside the block. Whether that is a
gap or correctly out of scope is a separate question; it does not
block the dispatch.

**A seventh case sits outside the dispatch.** `constants_new.py:190`
reads `# Source: Various; F-corona envelope extends to ~50 R_sun` with
`# Ref: Mann et al. (2004), A&A 414:1127`. "Various" is not an
authority. It has no `# Cross-checked:` line, so it is not in the 65
and not urgent -- but it is the same malformation and should ride
along with whichever shape is chosen.

---

*Prepared August 15, 2026 with Anthropic's Claude Opus 5. Built on
`a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery.*
