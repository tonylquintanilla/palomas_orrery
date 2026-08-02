# Citation Verification -- `constants_new.py` Remaining Items

**Built on `225071f6184c5fe150a8cdb258a03dbe10ae2718`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
HEAD verified fresh; it matches the stated anchor exactly.**

**Checker:** Claude Opus 5
**Date:** 2026-08-02

---

## Read this first: the prompt's premise about the checker is wrong

The prompt says this: *"You are the third checker, brought in
specifically because you have demonstrated access to book content the
other two could not reach (you confirmed the Carroll & Ostlie
photospheric tau = 2/3 definition earlier in this session)."*

I did not confirm that, and I cannot. I have no access to Carroll &
Ostlie, to Golub & Pasachoff, or to any book text. In the constants
worksheet I produced earlier today I marked all six Group D book
citations **UNVERIFIED** for exactly this reason, and said so plainly.

The prompt is addressed to Gemini -- its own footer says so. It reached
me instead. Two things follow, and the second one matters more than the
first.

**First:** I cannot do the job this prompt was written for. Four of the
six items need book access I do not have.

**Second, and this is the real finding:** somewhere between the two
worksheets, a confirmation that never happened got recorded as though it
had. If that belief had gone one step further -- into a `# Source:`
comment reading "Carroll & Ostlie, Ch. 9, confirmed" -- the file would
carry a citation to a verification no checker performed.

That is the precise failure the vulnerability ladder exists to catch,
occurring in the machinery built to catch it. A cross-check is only
worth what the checker actually did. Please trace where the tau = 2/3
attribution came from before any of it lands in a citation.

I have done the items I genuinely can do below, and marked the rest as
still open for a checker with book access.

---

## Two other things I cannot verify

**The patched file.** The prompt says `constants_new.py` was patched
locally but not pushed, and that the values below reflect the post-patch
state. It is not in the repo at HEAD and it was not uploaded. So I
cannot confirm the post-patch values at all -- including the
chromosphere change from 1.5 to 1.1 that item 6 asks about. Everything
below is verified against sources, not against your working copy.

**The count.** The prompt says two checkers "verified 30 of 36
constants." I reported 24 of 35, and 35 is what I counted in the file at
HEAD. GPT may have covered more, and the 36th may be a post-patch
addition. Worth reconciling, since the count is the thing that tells you
when the group is done.

---

## Worksheet

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|----------|-------|--------------|-------------------|-------|
| 1 | `CORE_AU` | 0.2 R_sun | Standard solar model (Bahcall et al.) | **NO -- category error** | Paper identified but figure not confirmed. See below. |
| 2 | `RADIATIVE_ZONE_AU` | 0.7 R_sun | Standard solar model | **UNVERIFIED** | Could not confirm the 0.713 tachocline figure from a primary source this session. See below. |
| 3 | `INNER_CORONA_RADII` | 3 | Golub & Pasachoff (2010) | **UNVERIFIED -- no book access** | Unchanged from my earlier worksheet. |
| 4 | `STREAMER_BELT_RADII` | 6.0 | Golub & Pasachoff (2010); DeForest et al. (2018) | **UNVERIFIED -- no book access** | The DeForest half is a paper and is checkable; I did not reach it this session. |
| 5 | `MOON_RADIUS_KM` | 1737.4 | NASA Fact Sheet (volumetric mean; oblateness ~0.0012) | **YES -- fully confirmed** | See below. |
| 6 | Group D header / chromosphere | 1.1 (post-patch) | Carroll & Ostlie (2017) | **UNVERIFIED -- no book access** | And the post-patch value itself is unverifiable to me; see above. |

---

## Item 5 -- Moon radius: confirmed, and the comment is exactly right

This is the one item I could close cleanly, and it closes completely.

The NASA NSSDCA Moon Fact Sheet gives:

- Volumetric mean radius **1737.4 km**
- Equatorial radius 1738.1 km, polar radius 1736.0 km
- **Ellipticity (flattening) 0.0012**

Both halves of the code comment check out -- the value and the
parenthetical oblateness. The citation says NASA Fact Sheet, and the
NASA Fact Sheet says 1737.4. Nothing to fix.

Two corroborating details worth recording, because they explain any
disagreement someone might hit later:

- 1737.4 km is also the IAU/LRO **lunar reference radius**, adopted by
  the Lunar Reconnaissance Orbiter Lunar Geodesy and Cartography
  Working Group (2008) and Archinal et al. (2011). USGS lunar map
  products use it as the map-scale radius. So the value is not just a
  fact-sheet number; it is the standard datum.
- JPL Horizons carries a slightly different figure: volumetric mean
  radius **1737.53 +/- 0.03 km**, while using 1737.400 km as the
  equatorial radius in its own ephemeris output. The 0.13 km spread
  between NSSDCA and Horizons is real but far below anything the orrery
  renders.

**Verdict: YES.** Keep the value and the citation as they stand.

---

## Item 1 -- `CORE_AU`: the citation is the wrong shape for the claim

I can answer two of the four questions, and the answer to the third
changes what the fix should be.

**Which paper.** The intended reference is almost certainly **Bahcall,
Pinsonneault & Basu 2001, ApJ 555, 990** -- described by Bahcall's own
solar-model data archive as the latest in the series of successively
refined standard solar models that began in 1962. It does publish
detailed tables of physical variables as a function of solar radius,
which is the right kind of source. Bahcall, Serenelli & Basu 2005 (ApJ
621, L85) and 2006 (ApJSS 165, 400) are the later revisions.

**Whether it states 0.2.** I could not confirm that it does, and I want
to be careful about why, because this is not the usual "I couldn't get
the paper" situation.

**A standard solar model does not have a core boundary.** It produces a
continuous run of temperature, density, and energy generation from
center to surface. There is no radius in the model where something
changes state. "The core extends to 0.2 R_sun" is a description
astronomers wrap around that continuous profile -- roughly, where
essentially all fusion happens -- not a quantity the model outputs.

So the citation is not merely vague. It points at a source that cannot
contain the claim in the form the claim is written, which is a different
defect from a wrong page number. GPT's observation that the conventional
range is 0.2-0.25 R_sun is the tell: a measured boundary would not have
a conventional range.

**Recommended fix.** Either cite a specific table or figure in BPB 2001
together with the criterion being applied -- for example the radius
enclosing some stated fraction of energy generation -- or relabel the
constant the way you have already relabeled the chromosphere: a
visualization boundary at the low end of the conventional 0.2-0.25
range, disclosed as such. The second option is honest and cheap. The
first is better but requires someone to open the paper's tables.

I could not check Carroll & Ostlie's solar interior chapters.

---

## Item 2 -- `RADIATIVE_ZONE_AU`: the physics question is real, the source is still open

I could not confirm the 0.713 R_sun tachocline figure against a primary
helioseismology source this session, so I am not going to assert it.
What I can say is narrower and still useful:

The tachocline is a genuinely measured feature, unlike the core
boundary. It is inferred from helioseismic inversions of the solar
rotation profile, and it is a real transition -- differential rotation
above, near-solid-body rotation below. So if 0.7 is a rounding of a
measured 0.713, the underlying claim is sound in a way item 1's is not.

But the citation as written ("Standard solar model", no author, no year)
still does not point anywhere. The tachocline is a helioseismology
result, not a standard-solar-model output, so even the *field* named in
the citation is wrong.

**Recommended fix:** cite the helioseismic determination directly.
Christensen-Dalsgaard is the right author family and Basu & Antia's
review work covers it; a checker with journal access should pin the
specific paper and the value with its uncertainty. Then say plainly in
the comment that 0.7 is a rounding of it.

---

## Items 3, 4, 6 -- still open, unchanged

`INNER_CORONA_RADII`, `STREAMER_BELT_RADII`, and the chromosphere
citation rest on Golub & Pasachoff (2010) and Carroll & Ostlie (2017).
I have no access to either and my verdict is the same as this morning:
**UNVERIFIED**.

One of the four is partly reachable without books. **DeForest et al.
2018** is a paper, and it is the second reference on the streamer belt
constant. A checker could confirm or refute the 4-6 R_sun helmet
streamer range from that alone, which would make the Golub & Pasachoff
half redundant rather than load-bearing.

On the framing question in item 3 -- whether "visualization boundary" is
fair for the inner corona at 3 R_sun -- I will not answer from memory.
But the question itself points somewhere useful: if the literature
turns out not to define a sharp inner/outer corona transition, then
labeling it a visualization boundary is not a retreat, it is the correct
description, and the same disclosure pattern you applied to the
chromosphere applies here.

---

## Tony-action rollup

- **(do)** Trace where the "Claude confirmed Carroll & Ostlie tau = 2/3"
  attribution originated. Nothing in my earlier worksheet supports it.
  Before anything derived from it reaches a citation.
- **(do)** Send items 3, 4, and 6 to Gemini as originally intended. They
  need book access and no amount of web search substitutes.
- **(do)** Push or upload the patched `constants_new.py` before the next
  round, so a checker can verify the post-patch state rather than the
  described one.
- **(decide)** Reconcile 35 vs 36 constants so the group has a
  definition of done.
- **(decide)** Item 1: relabel `CORE_AU` as a disclosed visualization
  boundary in the 0.2-0.25 range, or cite a specific BPB 2001 table
  with the criterion used. The current citation names a source that
  cannot contain the claim as written.
- **(decide)** Item 2: replace "Standard solar model" with a
  helioseismic determination of the tachocline. Wrong field, not just
  vague.
- **(decide)** Item 5 is closed. `MOON_RADIUS_KM` and its citation are
  both correct; no change.

---

*Prepared August 2, 2026 by Claude Opus 5. Sources consulted live: NASA
NSSDCA Moon Fact Sheet; USGS lunar map products (SIM 3316) for the
IAU/LRO reference radius; JPL Horizons lunar geophysical data; Bahcall
solar-model archive and the BPB 2001 (ApJ 555:990) listing. No book
sources were accessible.*
