# Cross-Check Worksheet Prompt — Batch 1 Tier 1 Sourcing

**Built on `2ccf6839c4278f01db00fbe2101440ab267a90c2`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Your role

You are an independent fact-checker for Paloma's Orrery, a Python/Plotly
solar system visualization project. Tony Quintanilla is the integrator.

## The job

**Value verification + source discovery.** The claims below appear in
display strings visible to users but have NO `# Source:` citation. They
are recalled values — written from AI training memory without
verification against a primary source. Your task for each claim is:

1. Independently research the correct value from authoritative primary
   sources (NASA fact sheets, ESA, JPL, mission papers, USGS, IAU).
2. Report what the authoritative source says.
3. Note whether the value in the code matches.
4. Provide the full citation so a `# Source:` comment can be written.

**Research against live authoritative sources. Use web search, reference
databases, and any primary source material you can access (including
textbooks and monographs). Do NOT answer from training memory — that is
the failure class this entire mechanism exists to prevent.** These claims
are uncited precisely because they were originally written from training
memory. Confirming them from training memory would be circular.

**Routing:** Tony sends this same prompt to Claude, GPT, and Gemini
independently. All three research the same claims without seeing each
other's answers. Tony compares all three worksheets for convergence.

## Worksheet format

Fill in one row per claim:

| # | Claim in code | Code value | Your value | Your source | Match? | Notes |

"Match?" means: does the code's value match what the authoritative
source says? YES / NO / APPROX (within rounding) / OUTDATED (was
correct at time of writing but has since been updated)

---

## File 1: eris_visualization_shells.py

### Finding: Atmosphere description (line 386)

This display string has no `# Source:` citation. The scanner flagged it
as Tier 1 (no source citation; date-sensitive recalled). The description
appears in the `create_eris_atmosphere_shell()` function's layer_info
dict.

**Claims to verify:**

| # | Claim in code | Code value |
|---|---------------|------------|
| E1 | Upper limit on Eris surface atmospheric pressure | ~1 nanobar |
| E2 | Comparison: Eris atmosphere vs Pluto atmosphere | ~10,000 times thinner |
| E3 | Temperature at aphelion | around -240 degC |

**Source code context:**

```python
# (No # Source: citation exists for this block)
'description': (
    "Atmosphere: Eris has a very tenuous atmosphere that is dynamic. ..."
    "* The current understanding of Eris's atmosphere is that it is
      extremely tenuous, with an upper limit on surface pressure of
      about 1 nanobar. This is about 10,000 times thinner than Pluto's
      current atmosphere. ..."
    "* Collapse at Aphelion: Eris is currently near its aphelion
      (farthest point from the Sun). At these extremely cold
      temperatures (around -240 degC), the primary atmospheric
      constituents, nitrogen and methane, would freeze and deposit
      as frost on the surface. ..."
)
```

---

## File 2: venus_visualization_shells.py

### Finding: Atmosphere description (lines 328 and 345)

These display strings have no `# Source:` citation. The scanner flagged
both as Tier 1 (no source citation, recalled). The same text appears
twice — once in `venus_atmosphere_info` (line 328, used in the module
header) and once in the `create_venus_atmosphere_shell()` description
dict (line 345). They are duplicates; verify the claims once.

**Claims to verify:**

| # | Claim in code | Code value |
|---|---------------|------------|
| V1 | Venus surface atmospheric pressure vs Earth | ~90 times Earth's |
| V2 | Venus atmosphere CO2 composition | ~96.5% |
| V3 | Venus atmosphere N2 composition | ~3.5% |
| V4 | Venus surface temperature | ~464 degC |
| V5 | Venus troposphere height | ~60 km |

**Source code context:**

```python
# (No # Source: citation exists for this block)
venus_atmosphere_info = (
    "Venus boasts an extremely dense atmosphere, about 90 times the
     pressure of Earth's atmosphere at the surface. It is composed
     primarily of carbon dioxide (about 96.5%) and nitrogen (about
     3.5%), with trace amounts of other gases, including sulfuric acid
     clouds that completely enshroud the planet. This thick, CO2-rich
     atmosphere creates a runaway greenhouse effect, making Venus the
     hottest planet in our solar system with surface temperatures
     around 464 degC. ..."
)

# Same text repeated in create_venus_atmosphere_shell() description:
# "... The 'lower atmosphere' of Venus is generally considered to be
#  the troposphere, which extends from the surface up to an altitude
#  of approximately 60 kilometers."
```

---

## What to produce

A completed worksheet with one row per claim (E1-E3, V1-V5), answering:
what does the authoritative source say, and does it match the code?

For each claim, provide the specific source you checked (URL, paper
reference, or fact sheet name) — not just "NASA" but "NASA Venus Fact
Sheet" or "Sicardy et al. 2011, Nature" with enough specificity to
write a `# Source:` comment from it.

---

*Worksheet prompt prepared August 2, 2026 by Claude Opus 4.6
(orchestration). Batch 1 Tier 1 — uncited claims needing sourcing.*
