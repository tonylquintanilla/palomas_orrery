# The Sun's 19 store values -- what each one's status would say

Built on orrery `7f4a2f9f046bc00ad9e418367b42beffaff89e7b` at
https://github.com/tonylquintanilla/palomas_orrery (branch main), gallery
`1a67b00d73813a1387ff1de7b77f8175c39c0f1e`. Both confirmed against the
live remote, 2026-08-27.

Read from `constants_new.py` at that SHA. Every line below is the file's
own text, not a recollection. Grouped by what needs doing, not by
position in the file.

---

## A. Three that need your ruling

### 1. RADIATIVE_ZONE_AU = 0.7

Its own comment: rounds the helioseismic tachocline at about 0.713.

A single measured value exists and the code holds a rounding of it.
Under "measured is the goal" this becomes **0.713**. First value change
the pass produces.

Source is Christensen-Dalsgaard, Gough & Thompson (1991), ApJ 378:413 --
pre-arXiv, so ADS is the access route.

### 2. INNER_CORONA_RADII = 3

Two problems on one row.

Its source is Golub & Pasachoff, "The Solar Corona" (2010) -- the same
work the nine-source read of 2026-08-20 removed from the helmet row for
returning no figure, no uncertainty and no findable position. It is
still cited here.

And 3 is the top of a 2-3 physical range, so even with a good source
there is no single number to promote to.

### 3. GRAVITATIONAL_INFLUENCE_RANGE_AU = (100000, 200000)

Its source line reads "spread of published Sun-in-Galaxy Hill sphere
estimates." No work is named. There is nothing to fetch, so it cannot
pass the access standard as written.

The value is almost certainly fine. The citation is not a citation.

---

## B. Four range-picks -- the pattern question

Each holds a defensible number chosen from a published range. None can
be promoted to "measured" by finding a better source, because the source
gives a range on purpose.

- **CORE_AU = 0.2** -- conventional core range 0.2-0.25 R_sun
- **INNER_CORONA_RADII = 3** -- physical extent 2-3 R_sun (also in A)
- **HELMET_CUSP_RADII = 4.0** -- source states helmets reach no higher
  than 2-4 R_sun; 4.0 is the top, and the row says why
- **INNER_LIMIT_OORT_CLOUD_AU = 2000** -- literature range 2000-5000 AU

`GRAVITATIONAL_INFLUENCE_AU = 150000` already shows the answer: the
range is stored as its own constant and the drawn value is the midpoint,
with the reason written down. The other four could follow it.

---

## C. Seven access checks -- fetchable, not yet fetched

Nothing wrong with these rows. Their sources have simply never been
opened under the new standard.

Likely open, quick:
- **SUN_RADIUS_KM** -- IAU 2015 B3, plus arXiv:1605.09788 and an NSSDCA
  link already in the row
- **PARKER_CLOSEST_RADII** -- JHUAPL mission page, URL in the row
- **OUTER_CORONA_RADII** -- Mann et al. (2004), A&A (open access)
- **CORE_AU** -- Bahcall, Pinsonneault & Basu (2001), ApJ (arXiv exists)

Paywalled journal, needs an arXiv or ADS route:
- **ALFVEN_SURFACE_RADII** -- Kasper et al. (2021), Phys. Rev. Lett.
- **TERMINATION_SHOCK_AU** -- Stone et al. (2005), Science
- **HELIOPAUSE_RADII** -- Gurnett et al. (2013), Science

Textbook, needs Google Scholar or Books:
- **CHROMOSPHERE_PHYSICAL_KM** -- Carroll & Ostlie, Ch. 11
- **ROCHE_LIMIT_RADII** -- Murray & Dermott, Sec. 4.6 (cited for a
  formula, not a measurement -- low risk)

---

## D. Three Oort values with no cross-check at all

- **INNER_LIMIT_OORT_CLOUD_AU = 2000** -- Hills (1981); Oort (1950)
- **INNER_OORT_CLOUD_AU = 20000** -- Hills (1981)
- **OUTER_OORT_CLOUD_AU = 100000** -- Oort (1950); Weissman (1996)

Both Hills 1981 and Oort 1950 have free full text on ADS, so these are
cheap to check. This is the group L-192 found wearing a cross-check rung
that belonged to the constant three lines above it.

---

## E. Five that look clean as they stand

- **SUN_RADIUS_KM** -- IAU nominal, and the row distinguishes the
  nominal value from the measured photospheric radius
- **HELMET_CUSP_RADII** -- carries a verbatim quotation from its source
  inline; abstract confirmed open 2026-08-27
- **TERMINATION_SHOCK_AU**, **HELIOPAUSE_RADII** -- both cross-checked,
  and the heliopause check caught a real error (26449 to 26148)
- **PARKER_CLOSEST_RADII** -- the altitude-versus-centre correction is
  recorded on the row

---

## F. Two derived -- never cleared on their own

- **SOLAR_RADIUS_AU** = SUN_RADIUS_KM / KM_PER_AU
- **CHROMOSPHERE_PHYSICAL_RADII** = 1 + CHROMOSPHERE_PHYSICAL_KM /
  SUN_RADIUS_KM

Status reads "derived, inherits" and names its inputs. Checking one of
these means checking its inputs.

---

## What the pass would produce

Nineteen `# Status:` lines. Three rows flagged for a ruling (section A),
four flagged as range-picks (section B), nine access checks queued
(sections C and D). No value changes in the pass itself.

*Prepared 2026-08-27 with Anthropic's Claude Opus 5.*
