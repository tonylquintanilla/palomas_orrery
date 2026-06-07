# Mode-7 Cross-Check Prompt for Gemini
# Carry to Gemini; bring the response back to Claude. Tony integrates.
# Topic: planetary magnetopause + bow-shock standoff distances and Mercury magnetosphere shape.

You are acting as a space-physics domain reviewer. I am building an educational
3D visualization of planetary magnetospheres and bow shocks. Each boundary is
rendered as a surface of revolution in units of the planet's radius (R_planet),
nose pointed sunward. I need physically accurate SUBSOLAR STANDOFF DISTANCES and
approximate SHAPE dimensions, each with a citation. Please verify or correct the
values below, cite a primary source for each, and explicitly flag anything wrong
or mis-sourced. Disagree where I am wrong -- I want correction, not confirmation.

HARD PHYSICAL INVARIANT I must preserve:
The subsolar bow-shock standoff must be LARGER than the subsolar magnetopause
(or induced-magnetosphere-boundary) standoff -- the shock stands sunward of the
magnetopause. Please confirm this holds for each body with the numbers you
recommend, and flag any pair where it does not.

------------------------------------------------------------------
PART 1 -- Mercury magnetosphere SHAPE (my main question)
------------------------------------------------------------------
I discovered my Mercury magnetosphere was mistakenly drawn at Earth scale (all
dimensions ~10-25 Mercury radii). I am rescaling it to physical Mercury
proportions. My proposed dimensions, in Mercury radii (R_M = 2440 km):

  magnetopause subsolar standoff (nose) : 1.45   [Winslow et al. 2013, MESSENGER]
  magnetotail radius at base            : 2.7    [Winslow 2013: ~2.7 R_M at 3 R_M downstream]
  magnetopause radius at terminator     : 2.5    [my estimate from alpha=0.5 flaring]
  magnetopause polar radius             : 2.2    [my estimate]
  magnetotail radius at far end         : 4.0    [my estimate]
  drawn magnetotail length (downstream) : 15     [visualization choice]

Questions:
  1a. Is the subsolar magnetopause standoff 1.45 R_M correct, and is it measured
      from the planetary DIPOLE or the planet CENTER? Mercury's dipole is offset
      northward (~0.2 R_M, Anderson et al. 2011) -- does that shift where the
      nose should sit relative to a planet-centered sphere in my rendering?
  1b. Given the Shue-type flaring parameter alpha = 0.5 (Winslow 2013), what is
      the physically correct magnetopause radius at the terminator (x=0)? Is my
      2.5 R_M reasonable, or what value do you recommend?
  1c. Magnetotail: Winslow reports ~2.7 R_M radius at 3 R_M downstream. Over what
      downstream distance is the tail well-constrained, and are my base (2.7) /
      far-end (4.0) radii and 15 R_M drawn length physically sensible?
  1d. Mercury's magnetosphere is strongly north-south ASYMMETRIC (northward
      dipole offset, large southern cusp). For an educational symmetric-shell
      rendering, is ignoring that asymmetry acceptable, or should I represent /
      annotate it? What is the single most important shape feature not to get
      wrong?
  1e. The bow shock I render as a conic with eccentricity 1.05 (illustrative,
      same for all planets). Winslow gives Mercury's bow shock e = 1.02. Does the
      per-body eccentricity matter visually/physically, or is a single
      illustrative ~1.05 acceptable for an educational tool?

------------------------------------------------------------------
PART 2 -- Mars bow shock standoff (accuracy question)
------------------------------------------------------------------
I currently render Mars's subsolar bow shock at 1.5 R_M (R_M = 3390 km), sourced
loosely to "Slavin classic, MAVEN-era mean ~1.59." But Vignes et al. 2000 (1.64),
Trotignon et al. 2006 (1.63), and Edberg et al. 2008 (1.58) cluster near ~1.6.
My Mars magnetopause / magnetic-pileup-boundary is set to 1.3 R_M (Vignes 2000,
MPB 1.29).

  2a. What single representative subsolar bow-shock standoff should I use for
      Mars under average solar-wind conditions -- is 1.5 defensible, or should it
      be ~1.6-1.64?
  2b. For internal consistency, is it preferable to take BOTH the Mars bow shock
      and the MPB from the same campaign (e.g., Vignes 2000: shock 1.64, MPB 1.29)?
  2c. Confirm the MPB subsolar value (~1.29-1.3 R_M) and that the nest holds.

------------------------------------------------------------------
PART 3 -- Full nest-table sanity check (flag any errors)
------------------------------------------------------------------
Please sanity-check every row. Units are R_planet (subsolar standoff). Flag any
value that is wrong, mis-sourced, or where the nest (shock > magnetopause) fails.

  Body     Magnetopause (my value / source)        Bow shock (my value / source)
  Mercury  1.45  Winslow 2013                       1.96  Winslow 2013
  Venus    1.05  Zhang 2007 VEX (induced, ~300 km)  1.40  Shan 2015 VEX
  Earth    10    Shue 1997 (standard)               15    textbook (meas. ~11-14)
  Mars     1.3   Vignes 2000 (MPB)                   1.5   (see Part 2)
  Jupiter  50    (code value -- unverified)          82    Joy et al. 2002
  Saturn   22    (code value -- unverified)          27    Went 2011 / Sulaiman 2016
  Uranus   21    (code value -- unverified)          23.7  Ness et al. 1986 V2
  Neptune  26.5  Ness et al. 1989 V2                 34.9  Ness et al. 1989 V2

  3a. I am least sure of the giants' MAGNETOPAUSE values (Jupiter 50, Saturn 22,
      Uranus 21 -- they are old code values I have not sourced). Are they
      physically reasonable subsolar magnetopause standoffs, or should any be
      corrected? (Jupiter's magnetopause is highly variable; what is a sensible
      single representative value?)
  3b. Are the giants highly tilted/offset enough (Uranus ~59 deg, Neptune ~47 deg
      dipole tilt) that a symmetric sunward-nosed shell materially misrepresents
      them? Neptune's rendered magnetosphere envelope currently pokes sunward of
      its bow shock on the tilted flank -- is that physically expected, or an
      artifact I should correct?

------------------------------------------------------------------
RESPONSE FORMAT REQUESTED
------------------------------------------------------------------
For each numbered item: a recommended value (or "confirmed"), one primary-source
citation, and a confidence flag (HIGH / MEDIUM / LOW). For Part 1, a corrected
set of Mercury dimensions if mine are off. Call out explicitly any place my value
is wrong or my source does not actually support the number.
