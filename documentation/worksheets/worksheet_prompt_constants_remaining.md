# Citation Verification Worksheet — `constants_new.py` Remaining Items

**Built on `225071f6184c5fe150a8cdb258a03dbe10ae2718`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

**Note: the file has been patched locally but not yet pushed. The
values and citations below reflect the post-patch state.**

---

## Context

Two independent checkers (Claude Opus 5 and GPT-5.6 Thinking) completed
a citation verification of `constants_new.py` on August 2, 2026. They
verified 30 of 36 constants. Six remain unverified because their
citations are book chapters that web search cannot open.

You are the third checker, brought in specifically because you have
demonstrated access to book content the other two could not reach
(you confirmed the Carroll & Ostlie photospheric τ = 2/3 definition
earlier in this session).

## The job

For each constant below, verify: **does the cited source contain or
support this value?** If the citation is wrong but the value is
defensible from a different source, say so — we need honest
provenance, not just a correct number.

Use whatever sources you can access — books, papers, authoritative
references. If you cannot verify a citation, say so plainly.

---

## Constants to verify

### 1. Solar core boundary

```python
CORE_AU = 0.2 * SOLAR_RADIUS_AU
# Derived: core extends to ~0.2 solar radii
# Source: Standard solar model (Bahcall et al.)
```

**Questions:**
- Does the standard solar model place the core boundary at 0.2 R_sun?
- GPT noted the conventional range is 0.2–0.25 R_sun. Is 0.2 the
  lower bound, a convention, or a specific model's output?
- "Bahcall et al." is too vague to verify — can you identify the
  specific paper (Bahcall, Basu & Pinsonneault 2001? Bahcall et al.
  2005?) and confirm it states 0.2?
- Is this value discussed in Carroll & Ostlie's solar interior chapters?

### 2. Radiative zone boundary

```python
RADIATIVE_ZONE_AU = 0.7 * SOLAR_RADIUS_AU
# Derived: radiative zone extends to ~0.7 solar radii
# Source: Standard solar model
```

**Questions:**
- GPT noted the tachocline (radiative-convective boundary) is at
  ~0.713 R_sun from helioseismology (Christensen-Dalsgaard et al.).
  Is 0.7 a rounded approximation of this?
- The citation says "Standard solar model" with no author or year.
  Can you identify the specific reference?
- Is this value discussed in Carroll & Ostlie?

### 3. Inner corona boundary

```python
INNER_CORONA_RADII = 3
# Source: Golub & Pasachoff, "The Solar Corona" (2010)
# Note: Visualization boundary for inner (K-)corona; physical extent 2-3 R_sun
```

**Questions:**
- Does Golub & Pasachoff (2010) describe the inner (K-)corona as
  extending to approximately 3 R_sun?
- Is there a conventional distinction between inner and outer corona
  at this radius, or is this a visualization choice?
- We have labeled this a "visualization boundary" — is that fair, or
  does the literature define a sharper transition?

### 4. Streamer belt extent

```python
STREAMER_BELT_RADII = 6.0
# Source: Eclipse observations; helmet streamers extend 4-6 R_sun
# Ref: Golub & Pasachoff (2010); DeForest et al. (2018)
```

**Questions:**
- Does Golub & Pasachoff describe helmet streamers extending to 4-6
  R_sun?
- Does DeForest et al. 2018 confirm this range?
- The code uses 6.0, the upper end of the stated range. Is this
  defensible, or is 5 R_sun more representative?

### 5. Moon radius

```python
MOON_RADIUS_KM = 1737.4
# Source: NASA Fact Sheet (volumetric mean; oblateness ~0.0012)
```

**Questions:**
- Does the NASA NSSDCA Moon Fact Sheet give a volumetric mean radius
  of 1737.4 km?
- Does JPL SSD agree?
- This is a simple web-checkable value, but neither prior checker
  looked it up. Confirm or flag.

### 6. Solar photospheric radius citation (Group D header)

The Group D section header cites Carroll & Ostlie (2017) and the NASA
Sun Fact Sheet. You already confirmed the τ = 2/3 definition from
Chapter 9. The remaining question:

- Does Carroll & Ostlie discuss the chromosphere's physical extent?
  The prior code cited Chapter 11 for a chromosphere boundary of
  1.5 R_sun. We changed the value to 1.1 R_sun (visualization shell)
  because research shows the physical chromosphere extends only
  ~2,000 km above the photosphere (~1.003 R_sun). Does Chapter 11
  say something that could have been read as 1.5 R_sun?

---

## What to produce

A completed row for each item:

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|----------|-------|-------------|-------------------|-------|

Plus any corrections to the citations. If a value is a defensible
approximation, say so — and name the source that defends it.

---

*Worksheet prompt prepared August 2, 2026 by Claude Opus 4.6.
Targeted at Gemini for book-citation access.*
