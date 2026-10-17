<!-- Doc-Kind: hand | The sources for Earth's hydrogen fade (L-410), read in full where reachable, with the quotations and locators each store row will carry, and the rows proposed for Tony's approval before the fade is built. -->
# Earth's hydrogen fade: the sources, read, and the rows proposed

Built on orrery da78b80fc7cf38c87d9d32d5b491b58023777561 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
f49b3e6974cc1183fe8f64f24878d6e2b6f540f2 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN (zero code), companion to
`documentation/DESIGN_fades_rulings_20261017.md`. Read 2026-10-17 by
Claude Opus 5.5, through a reader that quotes the published text; each
quotation below is the reader's verbatim return, with its locator.

## 1. Zoennchen et al. (2022) -- the profile, read in full

Zoennchen, J. H., Connor, H. K., Jung, J., Nass, U. and Fahr, H. J.
(2022), "Terrestrial exospheric dayside H-density profile at 3-15 RE
from UVIS/HDAC and TWINS Lyman-alpha data combined", Ann. Geophys.
40:271-279, open access,
https://angeo.copernicus.org/articles/40/271/2022/angeo-40-271-2022.pdf

- Abstract, p. 271: "which constrained the neutral H density there at
  10 RE to a value of 35 cm-3"; "a faster radial H-density decrease was
  found at distances above 8 RE (~ r-3)"; "compared to the lower
  distances of 3-7 RE (~ r-2.37)".
- Sec. 6, p. 275, eq. 7: nH(r) = 370 520 (r + 2.47)^-3.67 cm-3, r
  geocentric in RE; "the UVIS/HDAC observations can be calculated very
  precisely over the entire radial range 3-15 RE within +/-2 % error."
- Sec. 6, p. 276, eq. 8: nH(r) = 10 198 r^-2.375 cm-3, "fitted in the
  distance range 3-7 RE".
- Sec. 6, p. 276, eq. 9: nH(r) = 35.17 (10 RE / r)^3.02 cm-3, "The fit
  of the H-density profile between 9-15 RE delivers a r-3 fall".
- Sec. 6, p. 276: "there is an expected total error in the H density
  of about 25 %"; "found value of 35 cm-3 at 10 RE is more likely to be
  a lower limit."
- Where it applies: "Terrestrial ecliptic dayside observations" (p.
  271), "near the Earth-Sun line up to 15 RE geocentric distance" (p.
  272), a scan "within the ecliptic plane during ~ 1.5 h" (p. 272);
  18 August 1999 (p. 273), as solar activity rose from minimum, F10.7
  of 130 (p. 273); "quiet geomagnetic conditions" (p. 274). No local
  time is stated.

Checked here by arithmetic, not a claim of the paper: eq. 7 gives 35.2
at 10 RE (the abstract's 35) and 10.2 at 15 RE, where eq. 9 gives 10.3,
so the two agree at the join; eq. 7's own slope at 15 RE is -3.15,
close to eq. 9's -3.02.

## 2. Beyond 15 Earth radii -- Baliukin et al. (2019), through ESA

The paper (J. Geophys. Res. Space Physics 124:861-885,
doi:10.1029/2018JA026136; already `EARTH_GEOCORONA_RADII`'s Source)
could not be opened this session: the publisher refused the reader and
the open copy (HAL) refused it too. Its two densities are read from ESA's
article on it, a secondary source:
https://www.esa.int/Our_Activities/Space_Science/Earth_s_atmosphere_stretches_out_to_the_Moon_and_beyond
-- "with just 70 atoms per cubic centimeter at 60 000 kilometers above
Earth's surface" and "about 0.2 atoms at the Moon's distance" (the day
side).

Checked here by arithmetic: 60,000 km above the surface is 10.4 Earth
radii from the centre and the Moon about 60.3; between them the density
falls as r^-3.3. Carrying eq. 9's r^-3.02 out from 15 Earth radii gives
0.15 at the Moon against ESA's 0.2, and eq. 7 gives 31 at 10.4 Earth
radii against ESA's 70 -- the factor of about two between the papers,
which Zoennchen's "lower limit" allows. The rate agrees; the level does
not, and only the rate is drawn.

## 3. The day-night difference, for the hover -- Zoennchen et al. (2024)

Zoennchen, J. H., Cucho-Padin, G., Waldrop, L. and Fahr, H. J. (2024),
"Comparison of terrestrial exospheric hydrogen 3D distributions at solar
minimum and maximum using TWINS Lyman-alpha observations", Front.
Astron. Space Sci. 11:1409744, doi:10.3389/fspas.2024.1409744, open.
- Abstract: "a nose/geotail structure consistent with theoretical
  effects from the solar radiation pressure".
- Sec. 3.2: the nose "provides an H-density peak value that is 20%-50%
  larger than the H densities of the surrounding"; "A second region of
  enhanced H densities is present on the nightside near midnight."
- Its range: "at the lower and upper boundary of 3.75 and 6.0 Re"; "the
  angular shape of our model at r > 6 Re is fixed to its shape at 6 Re".
(Section labels as the reader gave them; to be checked against the
page when the row is written.)

## 4. The rows proposed (for Tony's approval; nothing is built)

In `constants_new.py`, beside `EARTH_GEOCORONA_RADII`, each carrying the
quotation and locator above as its `# Source:`:

| Row | Value | Unit | What it is |
|---|---|---|---|
| EARTH_EXOSPHERE_H_FIT_INNER_RADII | 3 | r_earth | where the measured profile starts (eq. 7's range); the fade starts here |
| EARTH_EXOSPHERE_H_FIT_OUTER_RADII | 15 | r_earth | where it ends |
| EARTH_EXOSPHERE_H_FIT_COEFF_CM3 | 370520 | per cm^3 | eq. 7's coefficient |
| EARTH_EXOSPHERE_H_FIT_OFFSET_RADII | 2.47 | r_earth | eq. 7's offset |
| EARTH_EXOSPHERE_H_FIT_EXPONENT | 3.67 | dimensionless | eq. 7's exponent |
| EARTH_EXOSPHERE_H_OUTER_EXPONENT | 3.02 | dimensionless | eq. 9's fall, carried from 15 Earth radii to the 100 of `EARTH_GEOCORONA_RADII`; ESA's figures for Baliukin et al. (2019) on its Also line |
| EARTH_EXOSPHERE_H_AT_10_RADII_CM3 | 35 | per cm^3 | the abstract's density at 10 Earth radii, a lower limit; for the hover only |

Declared, not measured, and said in the hover: carrying eq. 9's fall
past 15 Earth radii; the round shape; the dots' count and seed.

Written October 17, 2026 with Anthropic's Claude Opus 5.5.
