<!-- Doc-Kind: hand | Sources found for the Sun's two fades (L-410 with L-131): the plasma corona and the zodiacal dust cloud. Each value with what was opened, where in it, and what it says. Read 2026-10-19 by Claude Opus 5.5. -->
# Sources: the Sun's corona and dust cloud (L-410 with L-131)

Built on orrery 6e0cfacd0b6aa42cb09b0ca765be94e68aab6f70 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
4fc320fa6d2e0e10d9a50b8b69006cbff96a1364 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN (zero code). Written October 19, 2026 by Anthropic's
Claude Opus 5.5, during the design talk. Nothing here is in
constants_new.py yet; the fades' build writes the rows, and each
row's wording comes to Tony as a list first.

Every source below was opened in this session, from an open copy.
"Read" means the page was fetched and the figure found at the place
named. Where a figure is worked out from what a source prints, the
line says so.

## Tony's rulings so far (2026-10-19)

- The corona and the dust cloud are two drawings, because they are
  different physics: the corona is plasma whose glow is sunlight
  scattered by free electrons (the K-corona); the F-corona is sunlight
  scattered by dust, the innermost part of the zodiacal light. "Yes."
- In the dust drawing, a dot's place shows the dust's density, and its
  brightness shows the sunlight it receives, which falls with the
  square of distance from the Sun. "Confirmed as recommend."
- The square, not the cube: "Confirmed." (The cube belongs to Earth's
  hydrogen fall-off beyond 15 Earth radii, a dipole's field and tidal
  pull.)
- The inner corona (3 solar radii) and outer corona (50 solar radii)
  spheres become ONE plasma fade, following the measured electron
  density, from the Sun's surface out to the Alfven surface, which
  stays drawn as it is. "Confirmed as recommended."
- The dust cloud's dots stop at 5.2 AU, where Kelsall et al.'s model
  stops its line-of-sight sums; a declared drawing choice, and the
  hover says the cloud has no edge and the drawing stops where that
  model stops. "Confirmed."
- The corona's dots follow the same rule as the dust: place for the
  electron density, brightness for the sunlight each dot receives, since
  the corona's glow is also scattered sunlight. "Yes confirmed."

## Found later the same day (open points closed)

Mann, Warmuth, Vocks and Rouillard, "A heliospheric density and
magnetic field model", A&A 679, A64 (2023), open access (CC BY 4.0).
Read 2026-10-19.
- Eq. 7, the Leblanc et al. (1998) model: N_e(r) = 3.3e5 / R^2 +
  4.1e6 / R^4 + 8.0e7 / R^6 electrons per cubic centimetre, R = r in
  solar radii; for the region between the corona and Earth's orbit in
  the ecliptic plane; 7.14 per cubic centimetre at 1 AU.
- The article's own model, eq. 11 and Table 8, fitted over 1 to 250
  solar radii from Parker's wind equation.
- Open copy: https://www.aanda.org/articles/aa/full_html/2023/11/aa45050-22/aa45050-22.html
- So the corona's fade has an open source covering the whole drawn
  range, surface to the Alfven surface, in one closed form. Baumbach's
  formula (Lemaire, above) holds only to 3 solar radii. Recommended
  for the build, by method (one open model across the drawn range, the
  simplest form): Leblanc et al. as quoted by Mann et al. The original
  1998 paper (Sol. Phys. 183, 165) is not open; Saito et al. (1977)
  was not found open either, so neither is cited at the source.

Howard, Vourlidas, Bothmer, Colaninno, DeForest, Gallagher, Hall,
Hess, Higginson, Korendyke, Kouloumvakos, Lamy, Liewer, Linker,
Linton, Penteado, Plunkett, Poirier, Raouafi, Rich, Rochus, Rouillard,
Socker, Stenborg, Thernisien and Viall, Nature 576, 232-236 (2019).
The author list as printed on its RePEc record, read 2026-10-19:
https://ideas.repec.org/a/nat/nature/v576y2019i7786d10.1038_s41586-019-1807-x.html

The dust's midplane, by method: the drawing follows Kelsall et al.'s
fit throughout (node 77.7 degrees, tilt 2.03), because its shape
parameters were fitted together and mixing in another paper's node
would draw a cloud neither paper measured. Lamy et al.'s warped inner
plane is then said in words in the panel, as a thing the drawing does
not show.

## Gemini's worksheet, the same evening

Reviewed in `REVIEW_L410_gemini_worksheet_20261019.md`. What it
changes here, each re-opened before being written down:
- The Leblanc model holds only beyond about 1.8 solar radii: Zic,
  Vrsnak and Temmer, "Heliospheric Propagation of Coronal Mass
  Ejections: Drag-Based Model Fitting", arXiv 1506.08582, which says
  the expression is valid for R > 1.8. So, by the one-model method
  above, the corona's fade follows Mann et al. (2023)'s own model, which
  covers 1 to 250 solar radii (eq. 11, Table 8); Leblanc is a
  cross-check beyond 1.8. This replaces the recommendation above.
- Where the dust comes from: Nesvorny, Jenniskens, Levison, Bottke and
  Vokrouhlicky, arXiv 0909.4322 (2010), abstract: 85-95% of the
  mid-infrared emission from Jupiter-family comets, under 10% from
  long-period comets, asteroidal dust under 10%, about 85% of the mass
  reaching Earth. Open: https://arxiv.org/pdf/0909.4322
- Kelsall et al. give a reason for 5.2 AU: it roughly corresponds to
  the orbit of Jupiter (sec. 4.2, Gemini's quote; our read of sec. 4.2
  had reached the cutoff and not the reason).
- Forward scattering is still unsourced; the words keep it out.

## Still to settle, at the build (method, not rulings)

- The depletion zone as drawn: the dust thins from about 19 solar
  radii and is gone by about 5 (Lamy et al.), so the corona's fade and
  the dust overlap between them.
- The outer-corona checkbox's new name, and every visitor-facing word,
  come to Tony as a list before they ship.

## 1. What the two lights are

Boe, Habbal, Downs and Druckmuller, "The Color and Brightness of the
F-Corona Inferred from the 2019 July 2 Total Solar Eclipse", arXiv
2103.02113, introduction. Read 2026-10-19.
- The K-corona is Thomson scattering of photospheric light by free
  electrons throughout the corona.
- The F-corona is dust throughout the solar system scattering and/or
  diffracting photospheric light, often called the part of the
  zodiacal light at the smallest elongations from the Sun.
- Open copy: https://arxiv.org/pdf/2103.02113

## 2. The dust cloud's shape and density (the zodiacal cloud)

Kelsall, Weiland, Franz, Reach, Arendt, Dwek, Freudenreich, Hauser,
Moseley, Odegard, Silverberg and Wright, "The COBE Diffuse Infrared
Background Experiment Search for the Cosmic Infrared Background: II.
Model of the Interplanetary Dust Cloud", arXiv astro-ph/9806250
(ApJ 508, 44, 1998). Read 2026-10-19.
- Sec. 4.2.1, eq. 6: the smooth cloud's density is n0 times R^-alpha
  times f(zeta), zeta the height over the cloud's midplane divided by
  distance; eq. 7: f(zeta) = exp(-beta g^gamma), g = zeta^2 / 2 mu below
  mu and zeta - mu/2 above ("widened, modified fan").
- Table 1, "Density and Geometrical Parameters of the IPD Model",
  final values with 68% joint uncertainties:

  | Row | Value | Uncertainty |
  |---|---|---|
  | alpha, radial power-law exponent | 1.34 | 0.022 |
  | beta, vertical shape | 4.14 | 0.067 |
  | gamma, vertical power-law exponent | 0.942 | 0.025 |
  | mu, widening | 0.189 | 0.014 |
  | i, inclination of the midplane | 2.03 deg | 0.017 |
  | Omega, ascending node | 77.7 deg | 0.6 |

  (n0, 1.13e-7 per AU, is a cross-section density at 1 AU, not a
  number of grains; the drawing does not need it.)
- Sec. 4.2: the model's line-of-sight integration stops at an outer
  radial cutoff of 5.2 AU. That is the model's cutoff, not a measured
  edge: the cloud thins with no edge (a kind-1 fade, L-410's ruling of
  2026-10-17).
- Open copy: https://arxiv.org/abs/astro-ph/9806250

## 3. The dust close to the Sun (the F-corona and the dust-free zone)

Lamy, Gilardy and Llebaria, "Observations of the Solar F-corona from
Space", arXiv 2202.11533 (Space Sci. Rev., doi
10.1007/s11214-022-00918-y). Read 2026-10-19.
- Abstract, sec. 4.4: the F-corona's radiance falls as a power law of
  elongation between 5 and 50 degrees, exponent -2.33 near the
  equator and -2.55 over the poles.
- Sec. 4 and 4.1: the dust density is taken as r^-nu, with the
  radiance exponent nu + 1; the Helios value of the radiance exponent
  is about 2.3. Worked out here, not printed: nu is about 1.3,
  agreeing with Kelsall's 1.34.
- Abstract: the outer border of the dust depletion zone is well
  constrained at about 19 solar radii, and the zone extends down to
  about 5 solar radii, the boundary of the dust-free zone.
- Abstract: the inner cloud's symmetry plane is strongly warped; its
  ascending node is constant at 87.6 degrees. (This differs from
  Kelsall's 77.7, which fits the cloud near 1 AU; to settle at the
  build which the drawing follows, or neither.)
- Open copy: https://arxiv.org/pdf/2202.11533

Howard and others, "Near-Sun observations of an F-corona decrease and
K-corona fine structure", Nature 576, 232 (2019), doi
10.1038/s41586-019-1807-x. Abstract read 2026-10-19 (author list not
read on the page; to be read at the build).
- Parker Solar Probe's imaging on its first two perihelia, at 0.16 to
  0.25 AU, shows the F-corona's intensity decreasing at short
  elongations, suggestive of the long-sought dust-free zone.
- Open abstract: https://www.nature.com/articles/s41586-019-1807-x

## 4. The plasma corona's density

Lemaire, "Determination of coronal temperatures from electron density
profiles", arXiv 1112.3850v2 (2012). Read 2026-10-19. A secondary
source: it quotes the two models below, which it did not originate.
- Eq. 5, attributed to Baumbach: n(r) = 1e8 (2.99 r^-16 + 1.55 r^-6 +
  0.036 r^-1.5) electrons per cubic centimetre, r in solar radii,
  stated to be limited in principle to 1.05 to 3 solar radii.
- Eq. 16, the extended Saito model: n(r) = 1e8 [3.09 r^-16 (1 - 0.5
  sin Phi) + 1.58 r^-6 (1 - 0.95 sin Phi) + 0.0251 r^-2.5 (1 - sin^0.5
  Phi)] + n_E (215 / r)^2, Phi the latitude, n_E the density at 1 AU.
  Its last term carries the density out into the solar wind.
- Open copy: https://arxiv.org/pdf/1112.3850
- Still to find: the original papers' open copies (Baumbach 1937,
  Saito 1977), so the rows can cite what was opened at the source
  rather than a quotation of it, and n_E's value if the Saito form is
  used.

Session written October 2026 with Anthropic's Claude Opus 5.5.
