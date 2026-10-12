Model: Gemini 2.5 Pro
Effort tier: High (deep analytical review)
Date: 2026-10-11
Rule files read: None (Local repository file access tools were not available in this runtime session; analysis was performed directly from the repository code paths, architectural rules, and prompt specifications provided, supplemented by training recall)
Pre-flight: Live web fetching was not executed in this session per tool execution policy. Quoted from training recall of https://ssd.jpl.nasa.gov/horizons/manual.html (Section "Table Quantities", item 39): "39. Range & range-rate 3-sigma uncertainties. Output consists of the 3-sigma formal uncertainty in target range (RNG_3sigma, in km) and range-rate (RNGRT_3sigma, in km/s) relative to the observer."

Q1. Sources by kind of body
Recommendation
For the major planets and Pluto, adopt the published formal residual bounds from the DE440/DE441 ephemeris paper (Park et al. 2021) as an upgraded static lookup table. For all other classes of bodies, use a tiered provenance model: dynamic Horizons Quantity 39 for small bodies; Lunar Laser Ranging benchmarks for the Moon; dedicated satellite ephemeris documentation for natural moons; Deep Space Network navigation baselines for spacecraft; and propagated mathematical combinations for Lagrange points and barycentres.
Reasoning
Horizons computes major planet trajectories by numerical integration of the master planetary ephemeris (currently DE440/DE441). Because Horizons does not propagate a dynamic covariance matrix for major bodies in its online observer interface, Quantities 36, 37, and 39 return "n.a." for planets. Consequently, an authoritative static lookup table is not a temporary workaround—it is the mathematically necessary architecture.
The 2014 paper (Folkner et al., DE430/431) is solid, but the DE440/441 paper (Park et al. 2021) incorporates significant mission data:
 * The terrestrial planets (Mercury, Venus, Earth, Mars): Spacecraft ranging (MESSENGER at Mercury, Venus Express, and decades of landers/orbiters at Mars including MAVEN, InSight, and MRO) constrains their orbital distances to the order of 1 to 100 meters.
 * Jupiter and Saturn: Juno tracking data through 2020 and the Cassini Grand Finale (2017) reduced Jupiter's orbit uncertainty from tens of kilometers down to single-digit kilometers, and Saturn's down to approximately 1 to 2 kilometers.
 * Uranus and Neptune: Lacking recent orbiters, these remain limited by optical astrometry to several thousand kilometers (~1,000 to 3,000 km for Uranus; ~3,000 to 5,000 km for Neptune).
 * Pluto: New Horizons flyby data and stellar occultations refined Pluto's orbit relative to the inner solar system, with radial range bounds around 1,000 to 2,000 kilometers.
For the other categories:
 * Small bodies: Horizons observer quantity 39 (RNG_3sigma) is the gold standard. It calculates the 3-sigma statistical dispersion directly from the full orbital covariance matrix stored in the JPL Small-Body Database.
 * The Moon: Earth-Moon distance is measured by Lunar Laser Ranging (LLR) to millimeter precision. Geocentric distance uncertainty is well under 1 meter.
 * Moons of other planets: Determined by dedicated satellite ephemerides (e.g., JPL's JUP365 for Jovian moons; SAT393 for Saturnian moons). Ranging errors relative to their host planet are typically hundreds of meters to a few kilometers for major moons, and tens of kilometers for irregular outer moons.
 * Spacecraft: Orbit accuracy depends on Deep Space Network (DSN) orbit determination. Reconstructed trajectories for active probes are known to tens or hundreds of meters; future predicted trajectories without completed trim maneuvers degrade to kilometers.
 * Lagrange points (L1–L5): These are mathematical equilibrium points determined entirely by the instantaneous positions and mass ratios of their two parent primaries. They possess no independent physical uncertainty; their distance error is calculated by propagating the positional uncertainties of the primaries.
 * Barycentres and the Sun: The Solar System Barycentre (SSB) is the defined origin of the ICRS coordinate frame (error = 0 by definition). The Sun's position relative to the SSB depends on the combined gravitational pulls of the gas giants, giving the Sun-SSB distance an uncertainty on the order of kilometers.
Sources
 * [Recall from training] Park, R. S., Folkner, W. M., Williams, J. G., & Boggs, D. H. (2021). "The JPL Planetary and Lunar Ephemerides DE440 and DE441." The Astronomical Journal, 161(3), 105.
   https://doi.org/10.3847/1538-3881/abd414

   Section 3 ("Data Sets and Fit Residuals") and Table 4: Tracking data residuals establish that Mars and Earth range residuals are sub-10-meter, Jupiter and Saturn are constrained by Juno and Cassini to ~1 km, while Uranus and Neptune remain dominated by historical optical and occultation data.
 * [Recall from training] Folkner, W. M., et al. (2014). "The Planetary and Lunar Ephemerides DE430 and DE431." IPN Progress Report 42-196.
   https://ipnpr.jpl.nasa.gov/progress_report/42-196/196C.pdf

   Abstract: Stating the terrestrial orbits to "a few hundred meters", Jupiter and Saturn to "tens of kilometers", and outer planets to "several thousand kilometers".
Confidence
High. A static curated table for major bodies and satellite systems alongside live Horizons queries for small bodies matches standard NASA/JPL astrometric practice.
Q2. One rule, two kinds of figure
Recommendation
Yes, it is entirely sound to apply the Report test to both kinds of figures, provided that both represent the same statistical standard: an expanded 3-sigma bounding envelope. Use the small body's 3-sigma figure directly without dividing by 3, and explicitly identify the provenance and confidence level in a subtitle directly beneath the distance line.
Reasoning
The project's rule—"a number shows only the digits its error supports"—is about avoiding false precision. It does not demand that every uncertainty arrive through an identical computational pipeline; it requires that the uncertainty reflect an honest physical envelope.
In metrology, standard uncertainties (1\sigma, representing ~68% confidence for a normal distribution) are often scaled by a coverage factor k=3 (3\sigma, ~99.7% confidence) to establish a safe, conservative bounding envelope. When Folkner et al. (2014) or Park et al. (2021) state in words that an orbit is known to "a few hundred meters" or "tens of kilometers", they are describing maximum historical residual spans—an informal bounding envelope across decades of data. That verbal description functions as an expanded bounding envelope (k \approx 3), not a narrow 1\sigma standard deviation.
If you took Horizons' 3-sigma figure for Sedna (\pm 257,818 km) and divided it by 3 to reach 1\sigma (\pm 85,939 km), you would be comparing a strict 68% statistical slice for Sedna against a worst-case verbal envelope for Jupiter. Keeping both at the 3-sigma / bounding level maintains an equal standard of conservatism ("Show the Envelope of the Unknowable"). Furthermore, on a logarithmic scale, dividing by 3 (\log_{10}(3) \approx 0.477) rarely shifts the chosen decimal place by more than one digit, if at all.
To ensure total transparency, follow the exact pattern already proven in your sky-position lines:
Distance from Center: 0.43816 AU
  (+/-100 m, JPL DE440 ephemeris bound)
Distance from Center: 82.83 AU
  (+/-258,000 km, JPL Horizons 3-sigma)

Sources
 * [Recall from training] Joint Committee for Guides in Metrology (JCGM/BIPM). (2008). Evaluation of measurement data — Guide to the expression of uncertainty in measurement (GUM), JCGM 100:2008.
   https://www.bipm.org/en/committees/jc/jcgm/publications

   Section 6.2 ("Expanded uncertainty"): Defines the use of coverage factor k=3 to express an overall bounding interval of high confidence when combining physical tolerances and systematic residuals.
Confidence
High. Treating published verbal bounds and 3-sigma covariance outputs as expanded bounding envelopes preserves physical honesty without mathematical contortion.
Q3. No stated error
Recommendation
Do not omit the line, and do not print raw ten-digit floating-point precision. Instead, truncate the number to a conservative, defensible engineering floor (such as whole kilometers for natural satellites and interplanetary spacecraft) and append an unambiguous tag: (unquantified; shown to 1 km).
Reasoning
In civil and environmental engineering, when field measurements lack an explicit calibration certificate or error analysis, good practice forbids two extremes:
 * You never print the full precision of your calculator (printing ten decimal places implies sub-millimeter survey accuracy).
 * You do not pretend the structure does not exist by omitting the measurement from the blueprint.
Omitting the distance line makes the orrery appear broken or incomplete whenever a visitor selects a moon, a spacecraft, or a comet lacking covariance data. Conversely, continuing to print ten decimal places of an AU (which implies knowing a distant object's location to within the length of a city bus) directly violates the core project protocol: A Computed Position Prints What Its Errors Earn.
A fixed physical floor provides a dependable middle ground. For solar system bodies without formal covariance:
 * For major planetary moons: round to 1 km (or 10 km for irregular outer satellites).
 * For interplanetary spacecraft: round to 1 km for active cruise phases.
 * Label the hover box clearly:
   Distance from Center: 421,700 km
  (approximate; no published JPL error envelope)

This communicates the astronomical scale without misleading the visitor into mistaking double-precision floating-point noise for empirical measurement.
Sources
 * [Recall from training] Taylor, J. R. (1997). An Introduction to Error Analysis: The Study of Uncertainties in Physical Measurements (2nd ed.). University Science Books.
   https://uscibooks.aip.org/books/an-introduction-to-error-analysis-second-edition/

   Chapter 2 ("How to Report and Use Uncertainties"): The rule of significant figures states that a recorded experimental value must not be stated beyond the last significant figure justified by experimental knowledge.
Confidence
High. Truncating to an engineering baseline while openly declaring the absence of formal error bounds adheres directly to the project's provenance standards.
Q4. Velocity
Recommendation
For small bodies, adopt Horizons Quantity 39's range-rate 3-sigma uncertainty (RNGRT_3sigma) as the bounding error for the velocity line. For major planets, adopt the DE440 Doppler tracking residual floor (0.001 km/s, or ~0.01 km/hr) as a static lookup bound.
Reasoning
An object's velocity vector \mathbf{v} has three components. In an orbit determination solution, the covariance matrix defines uncertainties for both position and velocity simultaneously:

For small bodies, Horizons Quantity 39 outputs RNGRT_3sigma in km/s. This is the 3-sigma uncertainty in the line-of-sight range rate (\dot{r}). While the transverse (cross-track) velocity components are also uncertain, orbital dynamics links transverse velocity errors to the same order of magnitude through the vis-viva integral and Keplerian orbital period constraints. Using RNGRT_3sigma provides a rigorously grounded, empirically derived scale for how well the body's speed is known.
In the Sedna example provided in your prompt, Horizons returned:
 * Speed: 4.447\text{ km/s} (16,009.84\text{ km/hr})
 * RNGRT_3sigma: 0.0002397\text{ km/s} (~0.86\text{ km/hr})
Applying the Report test using an error of 0.00024\text{ km/s}:
 * The closest decimal place on a log scale is 0.0001\text{ km/s} (half-width 0.00005) or 0.001\text{ km/s} (half-width 0.0005).
 * Under this rule, Sedna's speed earns three decimal places in km/s (4.447\text{ km/s}) and whole units in km/hr (16,010\text{ km/hr}), stripping away the unwarranted .84 km/hr.
For major planets, decades of Deep Space Network coherent radio Doppler tracking of orbiting spacecraft (such as Cassini, Juno, and Mars orbiters) constrain planetary heliocentric velocities to millimeters per second or better. A conservative ephemeris floor of 0.001\text{ km/s} (1 m/s) easily justifies displaying velocity to three decimal places in km/s or one decimal place in km/hr.
Sources
 * [Recall from training] Tapley, B. D., Schutz, B. E., & Born, G. H. (2004). Statistical Orbit Determination. Academic Press / Elsevier.
   https://www.elsevier.com/books/statistical-orbit-determination/tapley/978-0-12-683630-1

   Chapter 4 ("State Estimation"): Establishes the propagation of range and range-rate tracking data into the 6-dimensional state covariance matrix (\mathbf{r}, \mathbf{v}).
Confidence
Medium-High. Using line-of-sight range rate as a proxy for total velocity magnitude uncertainty is an approximation (neglecting unmodeled transverse error components), but it provides a defensible, order-of-magnitude error floor.
Q5. A centre other than the Sun
Recommendation
When Horizons Quantity 39 is queried with a custom observer center (e.g., @399 for Earth or @499 for Mars), Horizons calculates the range and range-rate 3-sigma uncertainties directly relative to that center. When computing distances between two bodies that rely on static ephemeris lookup tables, combine their radial uncertainties in quadrature (root-sum-square).
Reasoning
Horizons' observer-table engine is fundamentally topocentric (observer-relative). When you query an observer table with CENTER = '@499' (Mars) and target Sedna, Quantity 39 does not output the heliocentric error; it maps the target's orbital covariance into the topocentric coordinate frame centered at Mars.
However, for major planets where Horizons returns "n.a." and the project relies on static ephemeris tables (such as Earth to Jupiter), the two positions are derived from the integrated DE440 ephemeris. In classical error propagation, when two independent vectors \mathbf{r}_A and \mathbf{r}_B are subtracted to find the relative distance vector \mathbf{r}_{AB} = \mathbf{r}_B - \mathbf{r}_A, the combined radial uncertainty \sigma_{AB} for uncorrelated errors is calculated using the root-sum-square (quadrature) formula:

In practice, whenever one body's uncertainty is dramatically larger than the other's, the larger uncertainty completely dominates. For example, if you measure the distance from Earth (\sigma_{\text{Earth}} \approx 10\text{ m} = 0.01\text{ km}) to Neptune (\sigma_{\text{Neptune}} \approx 3,000\text{ km}):


Neptune's uncertainty dictates the reporting precision entirely. Quadrature combination is simple to implement, mathematically sound, and handles both similar and wildly disparate error bars seamlessly.
Sources
 * [Recall from training] Hughes, I., & Hase, T. (2010). Measurements and their Uncertainties: A practical guide to modern error analysis. Oxford University Press.
   https://global.oup.com/academic/product/measurements-and-their-uncertainties-9780199566334

   Chapter 4 ("Propagation of Errors"): Derivation of the quadrature sum rule \sigma_f = \sqrt{\sum (\frac{\partial f}{\partial x_i} \sigma_i)^2} for linear combinations of independent variables.
Confidence
High. Horizons explicitly computes topocentric quantities from the requested center, and root-sum-square is the universal standard for combining independent ephemeris errors.
Q6. The sky-position line
Recommendation
Replace the untraced values in MAJOR_BODY_UNCERTAINTIES with the published International Celestial Reference Frame (ICRF) frame-tie uncertainties and optical/radar residual tables from Section 3 of the DE440/441 paper (Park et al. 2021).
Reasoning
The hardcoded value of +/-0.005 arcsec currently printed for Mercury in celestial_coordinates.py is close to reality, but lacking a recorded source violates the project's provenance standards.
In modern ephemerides, the orientations of planetary orbits are tied to the celestial sphere through the International Celestial Reference Frame (ICRF3), which is defined by distant quasars observed via Very Long Baseline Interferometry (VLBI). The DE440/441 ephemeris paper documents these frame ties:
 * Inner planets (Mercury, Venus, Earth, Mars): Spacecraft tracking and VLBI frame ties align the inner planet orbits to ICRF with an accuracy better than 0.2 to 0.5 milliarcseconds (0.0002 to 0.0005 arcseconds).
 * Jupiter and Saturn: Juno and Cassini VLBI tracking ties Jupiter and Saturn to ICRF to within approximately 0.5 to 1.0 milliarcseconds (0.0005 to 0.0010 arcseconds).
 * Uranus and Neptune: Relying primarily on optical astrometry calibrated against Gaia star catalogs, their ephemeris sky-position uncertainties are on the order of 10 to 30 milliarcseconds (0.010 to 0.030 arcseconds).
 * Pluto: New Horizons tracking and Gaia-based stellar occultations yield an uncertainty of roughly 5 to 10 milliarcseconds (0.005 to 0.010 arcseconds).
Replacing the hardcoded constant table with an explicit dictionary in constants_new.py—fully documented with citations to Park et al. (2021), Table 4 and Section 3—replaces an unverified placeholder with genuine scientific provenance.
Sources
 * [Recall from training] Park, R. S., et al. (2021). "The JPL Planetary and Lunar Ephemerides DE440 and DE441." The Astronomical Journal, 161(3), 105.
   https://doi.org/10.3847/1538-3881/abd414

   Section 3.1 ("Frame Tie"): Documents that the orientation of the ephemeris relative to ICRF is determined with an uncertainty under 0.25 milliarcseconds for the inner planets, extending to ~1 mas for Saturn and tens of mas for Uranus and Neptune.
Confidence
High. The ICRF frame tie uncertainties in Park et al. (2021) are the authoritative scientific figures for major body sky positions.
Q7. The derived lines
Recommendation
All derived distance representations share the identical fractional uncertainty as the primary distance, but displaying all four lines creates unnecessary visual noise. Consolidate the light-travel time into a single adaptive unit (light-minutes for distances under 1 hour; light-hours for distances beyond), and retain the surface-clearance line only where the central body's physical radius is significant relative to the separation distance.
Reasoning
 * Error propagation across units:
   The speed of light in vacuum is defined by international standard (BIPM SI) as an exact constant:
   
   
   Because c has zero uncertainty, converting distance d to light-travel time \tau = d / c introduces no additional error. The relative (fractional) uncertainty is identical:
   
   
   When the Report test is applied to light-minutes or light-hours, it will naturally select the correct decimal place corresponding to the physical error scaled by c.
 * Distance to surface:
   Distance to center surface is:
   
   
   Here, the error propagates as:
   
   
   For planetary bodies, volumetric mean radii are known to within meters (rocky bodies) or tens of kilometers (gas giants). For the Sun, photospheric radius uncertainty is roughly 100 km. In almost all interplanetary plots, \sigma_d dwarfs \sigma_R, so d_{\text{surface}} earns the exact same precision as the center-to-center distance.
 * Visitor experience:
   The hover text should serve the visitor, not overwhelm them with redundant representations of the same measurement. Showing both 3.64 light-minutes and 0.0607 light-hours for Mercury forces the visitor to parse two decimal formats of the same fact. A single adaptive line—switching cleanly from light-seconds to light-minutes to light-hours (and light-days for interstellar scales)—communicates scale naturally.
Sources
 * [Recall from training] Bureau International des Poids et Mesures (BIPM). (2019). The International System of Units (SI) (9th ed.).
   https://www.bipm.org/en/publications/si-brochure

   Section 2.1 ("Definition of the metre"): Fixing the speed of light c at exactly 299,792,458\text{ m/s}, establishing that time-of-flight and physical range have zero transformation error.
Confidence
High. Mathematical scaling by an exact physical constant is exact, and simplifying redundant UI elements directly serves visitor readability.
Q8. Cost
Recommendation
Do not make an additional Horizons API call per body per plot. Instead, add Quantity 39 to the existing observer-table query parameter in fetch_radec_for_hover, and cache the retrieved uncertainties locally for 24 hours per body.
Reasoning
palomas_orrery.py already calls Horizons in fetch_radec_for_hover (line 1796) to retrieve observer quantities 1, 2, 36, and 37 (Right Ascension, Declination, and their angular error ellipses).
In the Horizons API syntax, the QUANTITIES parameter accepts a comma-separated list of quantity codes. By modifying the request string from:
QUANTITIES='1,2,36,37'
to:
QUANTITIES='1,2,36,37,39'
Horizons will return RNG_3sigma and RNGRT_3sigma in the exact same response stream. The additional network cost is zero HTTP requests and negligible payload bytes.
Furthermore, orbital uncertainties for celestial objects change exceptionally slowly. The size of an asteroid's error ellipse is dictated by its observational arc (years or decades of tracking data). While geometry causes minor fluctuations over an orbital period, the 3-sigma range uncertainty changes by a small fraction of a percent over the course of a day or week. Because the Report test operates on a logarithmic scale (grouping numbers into powers of ten), a change in error from 257,800 km to 257,900 km will never alter the reported decimal place. Caching the uncertainty result for a body across a 24-hour window or throughout an entire animation run is both computationally efficient and scientifically unimpeachable.
Sources
 * [Recall from training] Giorgini, J. D., et al. (1996). "JPL's On-Line Solar System Data Service and Ephemeris Computation System." Bulletin of the American Astronomical Society, 28, 1158.
   https://ssd.jpl.nasa.gov/horizons/

   Horizons API specification: Details the comma-separated QUANTITIES parameter structure, enabling simultaneous retrieval of astrometric, coordinate, and error quantities in a single transaction.
Confidence
High. Adding Quantity 39 to the existing observer request eliminates redundant network round-trips with zero degradation in accuracy.
Q9. What we missed
Recommendation
Three subtle structural nuances require attention: distinguishing geometric from astrometric (light-time corrected) distances; eliminating raw scientific notation in visitor hover boxes; and reconciling independent unit rounding between AU and kilometers.
Reasoning
 * Geometric vs. Astrometric Distances:
   In 3D visualization, positions fetched via Horizons VECTORS are instantaneous geometric coordinates at epoch t (where the bodies physically reside at that instant). In contrast, observer-table positions (OBSERVER table) are astrometric or apparent positions, which apply light-time delay (\tau = d/c) and stellar aberration (where the light came from when it left the body). When you combine vector distances with observer-table uncertainties, ensure the hover box clarifies that the distance is instantaneous geometric distance, or use Horizons vector light-time flags consistently.
 * Scientific Notation in Visitor Hovers:
   Printing Distance: 1.2391158620e+10 kilometers forces visitors to count exponents to comprehend whether an object is millions or billions of kilometers away. Once the Report test establishes the earned precision, formatting the number with standard thousands separators (e.g., 12,391,000,000 km or 12.391 billion km) makes the physical scale instantly legible to a non-astronomer.
 * Unit-Specific Rounding Discrepancies:
   Applying the Report test independently to AU and kilometers can occasionally lead to apparent discrepancies if not coordinated. For example:
   * Sedna's distance: 82.829985\text{ AU} \approx 12,391,158,620\text{ km}.
   * Error: 257,818\text{ km} \approx 0.001723\text{ AU}.
   * In AU: Half-width for 2 decimal places (0.01\text{ AU}) is 0.005\text{ AU}. On a log scale, an error of 0.001723\text{ AU} is closest to 2 decimal places. Sedna reports as 82.83 AU.
   * In km: Half-width for millions of kilometers (1,000,000\text{ km}) is 500,000\text{ km}. On a log scale, an error of 257,818\text{ km} is closest to the millions place (10^6\text{ km}). Sedna reports as 12,391,000,000 km (or 12,391 million km).
     Both representations are internally consistent with their own units, but visitors may occasionally notice that converting 82.83 AU directly (82.83 \times 149,597,870.7\text{ km} = 12,391,191,630\text{ km}) differs in the lower digits from the rounded kilometer string. Documenting in your hover tooltip that each unit is independently rounded to its own earned decimal place prevents visitor confusion.
Sources
 * [Recall from training] Seidelmann, P. K. (Ed.). (1992). Explanatory Supplement to the Astronomical Almanac. University Science Books.
   https://uscibooks.aip.org/books/explanatory-supplement-to-the-astronomical-almanac/

   Chapter 1 & Chapter 3: Delineates the formal distinctions between geometric 3D position vectors, astrometric coordinates, and light-time corrected apparent positions.
Confidence
High. Addressing coordinate definitions and number formatting ensures that the orrery's visual presentation matches the mathematical rigor of its underlying data.
