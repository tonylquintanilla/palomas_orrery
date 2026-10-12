Model: GPT-6
Effort tier: High — multi-source research review; no separate user-visible effort setting was exposed
Date: 2026-10-11
Rule files read: PROJECT_INSTRUCTIONS.md (the sections “Fetched vs Recalled Convention” and “Show the Envelope of the Unknowable”); skills/provenance-discipline/SKILL.md (the sections “A Computed Position Prints What Its Errors Earn,” “An Accuracy Stated in Words Is Stored as the Place It Reports To,” and “The Access Standard”); skills/provenance-discipline/references/figures.md (the paragraph “The ceiling” and its Report test); skills/horizons-orbital-mechanics/SKILL.md; skills/orrery-coding-conventions/SKILL.md (the section “Hover Text Is Written for the Visitor”). I opened each file at commit 28a4636717920e86965f2e1777f3bf92386d1bb6 and read the requested sections.
Pre-flight: “Range and range rate (radial velocity) formal 3-standard-deviation uncertainties.” URL: https://ssd.jpl.nasa.gov/horizons/manual.html

Q1. Sources by kind of body

Recommendation — Keep the 2014 DE430/431 report’s worded accuracy categories as a provisional source for the planets and Pluto; the newer DE440/441 paper is important context but does not provide a complete replacement table of per-body, per-date position uncertainties. Use Horizons quantity 39 for small bodies when it is returned, and for every other class use an uncertainty tied to that object’s actual ephemeris or navigation solution; where that cannot be found, say it is unavailable rather than inventing a number.

Reasoning — For Mercury, Venus, Earth and Mars, the 2014 report gives a group-level position accuracy in words. The project’s stored-place method is a defensible way to turn those words into a display policy, provided the hover says this is a published qualitative accuracy category rather than a measured, date-specific “±” value. Jupiter and Saturn have a different accuracy category, as do Uranus, Neptune and Pluto. The newer DE440 paper reports better data and improved orbits for Jupiter, Saturn and Pluto; it also says Uranus and Neptune remain statistically consistent with DE430. But the residuals in that paper are differences between measurements and a fitted model, not a full position-error covariance for every body’s plotted position. I would not turn those residuals into a universal uncertainty table.

For the Moon, the 2014 report says the present-day lunar orbit is known to submeter accuracy, and the 2021 DE440 paper describes the newer lunar-laser-ranging data. This is a useful starting point, but the Moon’s distance from the Sun is a relative position that also depends on the Earth–Sun solution. For the other planets’ moons, seek the uncertainty for the particular satellite ephemeris or orbit solution; there is no single number that honestly covers a well-tracked inner moon, a distant irregular moon, and every epoch alike. For spacecraft, use mission-specific navigation or orbit-determination uncertainties if they are published. A spacecraft ephemeris file gives a position and velocity history, but that fact alone does not state its uncertainty. For Lagrange points, the uncertainty should follow the model that places the point and the uncertainties of the bodies defining it; it should not be treated as though the point were an independently observed small body. For barycentres, use the covariance of the ephemeris states and masses that define the centre, including their relationships to the target. The Sun is included in the DE planetary ephemeris, but the sources I opened do not expose a general, per-date Sun-position uncertainty suitable for every possible centre pairing.

For small bodies, quantity 39 is the strongest directly usable route because its range uncertainty refers to the target as seen from the requested observer. The JPL Small-Body Database (SBDB) also exposes the orbit-fit covariance, where one is available, but converting that covariance into a range uncertainty is additional work; Horizons already performs the relevant projection for this quantity. The main remaining gap is not choosing a better universal number. It is that a common, directly usable, date-specific uncertainty field does not appear to be available for every type of object that the orrery can plot.

Sources — William M. Folkner, James G. Williams, Dale H. Boggs, Ryan S. Park, and Petr Kuchynka, “The Planetary and Lunar Ephemerides DE430 and DE431,” IPN Progress Report 42-196 (2014). Abstract, printed page 1. URL:

https://ipnpr.jpl.nasa.gov/progress_report/42-196/196C.pdf

Quotation: “This orientation is the limiting error source for the orbits of the terrestrial planets, and corresponds to orbit uncertainties of a few hundred meters.”

Ryan S. Park, William M. Folkner, James G. Williams, and Dale H. Boggs, “The JPL Planetary and Lunar Ephemerides DE440 and DE441,” The Astronomical Journal, 161:105 (2021). Abstract, printed page 1. URL:

https://ssd.jpl.nasa.gov/doc/Park.2021.AJ.DE440.pdf

Quotation: “The orbit of Jupiter has improved substantially”.

“Horizons System,” authors not separately identified on the page, JPL Solar System Dynamics; version 4.98e, dated August 25, 2026. Observer-table quantity descriptions for comet/asteroid statistical uncertainties and quantity 39, “Range and range rate (radial velocity) formal 3-standard-deviation uncertainties.” URL:

https://ssd.jpl.nasa.gov/horizons/manual.html

Quotation: “For comets and asteroids, corresponding statistical uncertainties and plane-of-sky error ellipse parameters”.

“SBDB API,” authors not stated in the document, version 1.3 (September 2021). Normal Data Payload and the orbit covariance description. URL:

https://ssd-api.jpl.nasa.gov/doc/sbdb.html

Quotation: “full covariance information on the primary orbit parameters”.

“SPK Required Reading,” B. V. Semenov (last revision shown: August 31, 2021), NASA/JPL Navigation and Ancillary Information Facility. “Segments—The Fundamental SPK Building Blocks.” URL:

https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/spk.html

Quotation: “compute the geometric state (position and velocity) of one solar system body with respect to another”.

constants_new.py, commit 28a4636717920e86965f2e1777f3bf92386d1bb6, comments above the three DE430 position-place constants, lines 3337–3400. Author not separately stated; the file records the project’s source and precision decisions. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/constants_new.py

Quotation: “the place the Report test gives for every value the words can mean”.

If you say no source exists — I did not find a single open JPL source that supplies a comparable, per-date range uncertainty for all eight categories. I checked the opened Horizons manual, the official DE430/431 report, the official DE440/441 paper, the SBDB API documentation, and the SPK reference. That is a statement about those documents and searches, not proof that no specialist satellite or mission paper exists for any individual object.

Confidence — High that Horizons quantity 39 is the best directly usable value for supported small bodies, and high that the DE440 paper is not a universal numeric replacement for the 2014 categories. Medium for the proposed fallback hierarchy for moons, spacecraft, Lagrange points and barycentres; object-specific ephemeris and navigation sources could improve it.

Q2. One rule, two kinds of figure

Recommendation — Use the same Report test as a consistent display-rounding rule, but preserve the meaning of the source’s uncertainty. For a formal 3-sigma range uncertainty, feed the 3-sigma value itself into the test; do not divide it by three unless the project explicitly decides that the displayed digits should instead be based on one standard deviation.

Reasoning — The test answers a narrow question: which displayed place has a rounding half-width closest to the chosen error? It does not make different kinds of evidence statistically equivalent. The small-body figure is a formal, date-dependent 3-sigma result from an orbit-fit covariance. The planetary categories are descriptive statements about the accuracy of a family of ephemerides, not a published per-date standard deviation. The same rounding machinery can serve both if the hover explains the distinction in ordinary words.

I would label a small-body line “formal 3-sigma range uncertainty from JPL Horizons, at [date], from [centre].” For a planet using the 2014 report, I would say “JPL’s published position-accuracy category; not a date-specific uncertainty.” I would not print the half-unit surrogate from the worded category as though JPL had published that numeric ± value. The number of printed digits and the actual stated uncertainty are related, but they are not the same claim. A visitor should be able to tell which claim is being made.

Sources — “The Figure Count (provenance-discipline reference),” in skills/provenance-discipline/references/figures.md; authors not separately stated in the file. “The ceiling,” especially its description of propagating a stated uncertainty and its Report test. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/skills/provenance-discipline/references/figures.md

Quotation: “Where any input carries a stated uncertainty, propagate that instead and let it decide.” The same paragraph specifies a tie “going to the coarser”.

“PROJECT INSTRUCTIONS,” Tony Quintanilla, PE | Claude, v3.91, October 11, 2026. “Fetched vs Recalled Convention.” URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/PROJECT_INSTRUCTIONS.md

Quotation: “A citation is a claim about provenance – it must be TRUE, not just present.”

Confidence — High that the 3-sigma value should be used as given under the project’s stated rule. Medium that the label wording above is the best visitor-facing wording; testing the final hover on a real plot could improve it.

Q3. No stated error

Recommendation — Keep a useful nominal distance, round it only to a clearly declared display floor such as whole kilometres, and put a plain note beside it saying that JPL has not supplied a formal uncertainty for this object. Do not describe the floor itself as an error; if the hover cannot show the caveat clearly, omit the line until the gap is resolved.

Reasoning — There are two different things here: the nominal distance reported by the ephemeris, and how well that distance is known. A nominal distance can be useful even when its uncertainty is unavailable, but ten decimal places make a claim the source has not supported. A whole-kilometre floor is a display convention, not proof of kilometre accuracy. This compromise preserves the visitor’s sense of scale without implying that the last printed digit has been earned by an error estimate. It is also important not to invent a tiny substitute error just to make a rounding helper return something: the absence of an error is real information and should reach the display.

Sources — “PROJECT INSTRUCTIONS,” Tony Quintanilla, PE | Claude, v3.91, October 11, 2026. “Fetched vs Recalled Convention” and “Show the Envelope of the Unknowable.” URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/PROJECT_INSTRUCTIONS.md

Quotation: “A blank with a flag is honest; an unsourced assertion is not.”

orbital_period.py, commit 28a4636717920e86965f2e1777f3bf92386d1bb6, format_by_error(), lines 112–123. Author not separately stated; the module header records the October 11, 2026 update. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/orbital_period.py

Quotation: err = abs(value) * 1e-10 if value else 1e-10. This fallback is a coding convenience, not a source for physical accuracy; I would not copy it into the distance or velocity path.

If you say no source exists — I did not find a general JPL uncertainty field for every plotted body in the opened Horizons manual, DE440/441 paper, SBDB API documentation, or SPK reference. Individual mission or satellite sources could fill a particular gap. Until then, the hover should say what is missing rather than claim that no uncertainty exists in nature.

Confidence — High that a fixed display floor must not be presented as physical accuracy. Medium on keeping the nominal line rather than omitting it; that is a visitor-facing design choice, and the note must be hard to miss.

Q4. Velocity

Recommendation — Do not use the range-rate uncertainty as the uncertainty of the current three-dimensional speed. Where no full velocity uncertainty is available, show speed only as a coarsely rounded nominal value with an explicit note that its uncertainty is not available, or leave the speed line out.

Reasoning — The code forms speed from the three velocity components, taking the square root of the sum of their squares. Range rate is different: it is only the part of the velocity directly toward or away from the observer. A formal uncertainty for that one component does not tell us how uncertain the two sideways components are, so it cannot honestly set the digits for the total speed. The sound route is to obtain a velocity-state covariance (a description of how the velocity components and their errors are related) and propagate it through the calculation of speed. For an object’s orbit fit, position and velocity can also be correlated, so a full state covariance is preferable. If only a radial speed is shown, then a range-rate uncertainty could support that radial-speed line, with its 3-sigma meaning stated.

Sources — “Horizons System,” authors not separately identified on the page, JPL Solar System Dynamics; version 4.98e, August 25, 2026. Observer-table quantity 39, “Uncertainties in plane-of-sky radial direction.” URL:

https://ssd.jpl.nasa.gov/horizons/manual.html

Quotation: “formal 3-standard-deviation uncertainties.”

palomas_orrery.py, commit 28a4636717920e86965f2e1777f3bf92386d1bb6, fetch_position(), the extraction of vx, vy, vz and calculation of velocity, lines 1198–1207. Author not separately stated; the file is the application module. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/palomas_orrery.py

Quotation: velocity = np.sqrt(vx**2 + vy**2 + vz**2).

If you say no source exists — I checked the opened Horizons observer-quantity definitions, the SBDB API’s orbit-element and covariance descriptions, and the DE440 paper’s residual discussion. Those sources offer a formal small-body range-rate uncertainty and orbit-fit covariance data, but I did not find a universal, directly usable accuracy for the full speed of every body type. This does not rule out a full covariance source for a particular mission or object.

Confidence — High that range-rate uncertainty cannot stand in for total-speed uncertainty. Medium on whether the best visitor design is a coarse nominal speed with a caveat or no line; both are more honest than rounding to an unsupported precision.

Q5. A centre other than the Sun

Recommendation — Treat the plotted distance as a relative measurement involving both the target and the chosen centre. For a proper combined error, propagate the uncertainty of their relative position; use root-sum-square only when independence is justified, and do not assume Horizons quantity 39 includes uncertainty in the centre’s own ephemeris.

Reasoning — If the target position is uncertain and the centre position is uncertain, the error in their difference depends on both. When their uncertainties are independent, their contributions can be combined in quadrature (square, add, and take the square root). When they share information or their errors move together, that shortcut can be wrong. The more general method uses the covariance of the difference between the target and centre positions, including any cross-correlation between them, and projects that covariance along the line from centre to target to obtain the uncertainty in the scalar distance.

Quantity 39 is documented as a formal uncertainty derived from a small body’s orbit solution, projected into the range direction as seen from the selected observer. I found no statement in the manual that it also adds the uncertainty of an arbitrary planet, moon, spacecraft or barycentre used as that observer. The safe implementation assumption is therefore that it is not a complete two-body uncertainty unless JPL confirms otherwise. When the centre’s uncertainty is not available, say that the range uncertainty is the small-body formal uncertainty only; do not label it as the combined error of the whole separation.

Sources — Ryan S. Park, William M. Folkner, James G. Williams, and Dale H. Boggs, “The JPL Planetary and Lunar Ephemerides DE440 and DE441,” The Astronomical Journal, 161:105 (2021). Section 1, printed page 1. URL:

https://ssd.jpl.nasa.gov/doc/Park.2021.AJ.DE440.pdf

Quotation: “positions of the Sun, the barycenters … the Moon”.

“SBDB API,” authors not stated, version 1.3 (September 2021). “Orbit Subsection: covariance.” URL:

https://ssd-api.jpl.nasa.gov/doc/sbdb.html

Quotation: “the covariance matrix … for the orbital elements”.

If you say no source exists — The official Horizons manual defines quantity 39 as a formal range and range-rate uncertainty, and the SBDB API describes covariance for the small body’s orbit solution. I did not find wording in either document stating that quantity 39 propagates a separate uncertainty for the observer body’s ephemeris. The recommendation not to assume that it does is based on the documented scope of those fields, not on proof that JPL has no internal treatment of observer uncertainty.

Confidence — Medium-high. The advice follows the fields documented in the opened sources; explicit clarification from JPL on quantity 39’s treatment of observer-state uncertainty would raise confidence.

Q6. The sky-position line

Recommendation — Remove the typed planetary uncertainty values unless each one can be connected to a named, opened source or a documented calculation. Use Horizons’ formal sky-position uncertainties where JPL actually returns them; otherwise show the position without a numeric “±” claim and explain in plain words that a formal sky uncertainty is not available in that line.

Reasoning — The comment above MAJOR_BODY_UNCERTAINTIES says the values are “based on” DE440/441 and mission data, but it does not name a paper, table, page, or calculation that yields the specific arcsecond value for each planet. The 2021 DE440 paper describes the observations used to fit planetary ephemerides and publishes some observation residuals. Those residuals are not themselves uncertainties in the planet’s apparent right ascension or declination as seen from Earth at the hover time. It would be a mistake to use them as though they were.

For a body that returns formal RA/Dec uncertainty from Horizons, use those values and identify them as formal 3-sigma uncertainties. For planets and the Moon, the better future path is an auditable source or calculation that derives the apparent sky uncertainty from the relevant position uncertainties and viewing geometry. Until that exists, omit the numeric uncertainty rather than replace one unsourced number with another. The hover is for visitors, so the note should say “JPL does not provide a formal sky-position uncertainty here,” not just display an unexplained technical label.

Sources — celestial_coordinates.py, commit 28a4636717920e86965f2e1777f3bf92386d1bb6, MAJOR_BODY_UNCERTAINTIES and get_precision_note(), lines 127–143 and 372–439. Author not separately stated; the file records the code but no citation behind those values. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/celestial_coordinates.py

Quotation from the table comment: “Based on DE440/441 planetary ephemeris and mission data”. The comment is not, by itself, a traceable source for any listed number.

“The JPL Planetary and Lunar Ephemerides DE440 and DE441,” Ryan S. Park, William M. Folkner, James G. Williams, and Dale H. Boggs. Section 5.1, “Residuals,” printed pages 12–13. URL:

https://ssd.jpl.nasa.gov/doc/Park.2021.AJ.DE440.pdf

Quotation: “The rms residual … is about 20 cm”. This is a measurement-fit residual, illustrating why a residual should not be relabelled as a general apparent-coordinate uncertainty.

“Hover Text Is Written for the Visitor,” in skills/orrery-coding-conventions/SKILL.md, version 1.10, with Anthropic’s Claude Opus 5.5, October 5, 2026. Section of the same name. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/skills/orrery-coding-conventions/SKILL.md

Quotation: “In general we should avoid compressed language in the hovertext.”

If you say no source exists — I inspected the typed table and its fallback logic, the Horizons manual’s definitions for quantities 36 and 37, and the DE440 paper’s treatment of planetary observations and residuals. I did not find a cited source that supports each of the typed planetary arcsecond values as a formal per-body RA/Dec uncertainty. That is a finding about the opened material, not a claim that no relevant measurement or specialist study exists.

Confidence — High that the current numeric table is not adequately sourced as it stands. Medium on the best eventual replacement for each planet, because the answer depends on whether suitable covariance or source-specific apparent-coordinate uncertainties can be obtained.

Q7. The derived lines

Recommendation — Carry the same underlying range uncertainty through exact unit conversions, recalculating the displayed place in each unit. Keep AU and kilometres as the core distance lines, show either light-minutes or light-hours rather than both, and show distance to the centre’s surface only when a real surface makes that distinction useful.

Reasoning — Kilometres, light-minutes and light-hours are the same distance expressed in different units. Multiplying or dividing by an exact conversion factor does not create a new independent uncertainty; it scales the existing one. The Report test should be run again in each displayed unit because the useful decimal place changes with the unit. If the underlying distance uncertainty is 250,000 km, for example, the AU line, kilometre line and light-time line should all be rounded from that one value and that one uncertainty, not rounded independently from unrelated fixed-width rules.

“Distance to Center Surface” is a different quantity: the distance from the centre minus the centre’s mean radius. It inherits the range uncertainty and also, in principle, the uncertainty of the radius. If the radius error is much smaller and does not change the printed place, the same rounded range error may set the display. If not, include the radius uncertainty in the propagation. Do not print a surface-distance line for a mathematical point, barycentre or Lagrange point that has no physical surface. The current code defaults an unknown centre radius to zero, so without a check that line can become a duplicate distance wearing a misleading label. For a spacecraft or moon near a planet’s surface, the surface distance can be educationally valuable; for a body far from the Sun it usually adds little beyond the main range.

Sources — visualization_utils.py, commit 28a4636717920e86965f2e1777f3bf92386d1bb6, format_detailed_hover_text(), lines 757–786. Author not separately stated; the header records the October 11, 2026 update with Anthropic’s Claude Opus 5.5. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/visualization_utils.py

Quotation: distance_from_origin = np.sqrt(obj_data['x']**2 + obj_data['y']**2 + obj_data['z']**2).

formatting_utils.py, commit 28a4636717920e86965f2e1777f3bf92386d1bb6, format_maybe_float() and format_km_float(), lines 6–20. Author not separately stated. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/formatting_utils.py

Quotation: “If ‘value’ is a numeric type (int or float), return it formatted with 10 decimal places.”

Confidence — High that exact unit conversions should carry a single scaled uncertainty, and high that light-minutes and light-hours are redundant in one short hover. Medium on whether the surface line should be hidden or kept in more plot types; that depends on what visitors use the plot to learn.

Q8. Cost

Recommendation — Do not request quantity 39 afresh for every animation frame. For a static plot, fetch it once and cache it with the target identity, orbit-solution identity when available, centre ID and epoch; a one-day cache window is a reasonable performance compromise only when the hover also records the uncertainty’s epoch and the animation is not pretending that value stays valid across a much longer interval.

Reasoning — A cached uncertainty can save repeated network calls, but its value depends on the fitted orbit, the time, and the observer geometry. “It probably changes slowly” is not a universal rule: a close approach or a poorly constrained orbit can change the uncertainty quickly. For ordinary static plotting, reuse the result for an identical target, centre and epoch. If the application rounds cache times to a UTC day, treat that as an engineering cache policy, not a physical statement that uncertainty is constant for 24 hours. For animations spanning multiple days, years or a close encounter, either refresh at suitable time steps or avoid showing changing-epoch precision as though it were current. The display should say which epoch the uncertainty belongs to.

I would first measure the actual cost before building a more elaborate shortcut. One added query per body is likely a sensible trade for a static plot if results are cached. Reimplementing orbit-covariance propagation from SBDB’s orbital-element covariance may reduce calls, but it adds transformations, correlation handling and more places for a subtle error. That is not obviously cheaper overall than using JPL’s range uncertainty when JPL already supplies it.

Sources — orbital_period.py, commit 28a4636717920e86965f2e1777f3bf92386d1bb6, build_period_record() and its cache-record description, lines 227–243. Author not separately stated; module header records its October 11, 2026 update. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/orbital_period.py

Quotation: “The period record the orbit cache keeps beside an entry’s elements.”

“SBDB API,” authors not stated, version 1.3 (September 2021). Parameters and “Orbit Subsection: covariance.” URL:

https://ssd-api.jpl.nasa.gov/doc/sbdb.html

Quotation: “covariance matrix”. The API’s covariance is useful source material, but does not itself provide the proposed daily cache rule.

If you say no source exists — I did not find an official JPL statement in the opened Horizons manual or SBDB API documentation that quantity 39 can be reused unchanged for a day. I found documentation of time-dependent uncertainty output and of the orbit covariance, not a prescribed cache duration. The one-day idea is therefore an application design decision that should be tested against fast-changing cases.

Confidence — Medium-high. Caching identical requests is sound engineering; the safe duration depends on the objects and epoch range in the animation. Close approaches and long extrapolations should be explicit exceptions.

Q9. What we missed

Recommendation — Before implementing L-401, make two boundaries explicit: the orrery’s plotted vectors are fetched for the requested date, so physical change over a year is not their position error; and a missing uncertainty must never be replaced by a fabricated tiny error just to produce digits. Then apply the same error-based formatter only when a defensible error is actually available.

Reasoning — The period’s one-year comparison estimates how much the fitted period itself changes over that interval; it is used as a conservative numerical stability test for the period. The distance vector in fetch_position() is requested directly from Horizons for the plot date. Its change over a year is real orbital motion, not uncertainty in today’s distance. Reusing the period rule wholesale would therefore confuse motion with error. The appropriate distance limit is the ephemeris or orbit-fit uncertainty at the selected date, plus centre uncertainty where it can be established.

There is also a statistical limit to keep visible: Horizons calls quantity 39 a formal 3-sigma uncertainty. “Formal” matters. A covariance-based estimate is not a guarantee that every true position lies inside that interval, especially after long propagation or strongly nonlinear close encounters. If the hover is intended to teach visitors that a value is well known, show the source and kind of uncertainty in simple words. If it is only a rounding rule, don’t let the number of decimals imply a stronger physical claim than the source makes.

Finally, make absence of an uncertainty a first-class state in the formatting code, distinct from zero error and from an unavailable nominal position. orbital_period.py currently substitutes a tiny relative error when the error is missing; that may preserve output for legacy paths, but it should not be allowed to give L-401 distances or speeds artificial precision. The surface-distance calculation should likewise detect whether the centre has a real physical radius before printing a surface label. These checks matter as much as the chosen rounding function.

Sources — “A Computed Position Prints What Its Errors Earn,” in skills/provenance-discipline/SKILL.md, version 2.28, October 9, 2026, with Anthropic’s Claude Opus 5.5. Section of the same name. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/skills/provenance-discipline/SKILL.md

Quotation: “Its count comes from its errors, and two of them bound it”. The section distinguishes a propagated position’s reproduction drift from the underlying source accuracy; this orrery’s live Horizons vector query is a different path from a position propagated locally from stored orbital elements.

palomas_orrery.py, commit 28a4636717920e86965f2e1777f3bf92386d1bb6, fetch_position(), lines 1181–1207. Author not separately stated. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/palomas_orrery.py

Quotation: vectors = obj.vectors().

orbital_period.py, commit 28a4636717920e86965f2e1777f3bf92386d1bb6, format_by_error(), lines 112–123. URL:

https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/28a4636717920e86965f2e1777f3bf92386d1bb6/orbital_period.py

Quotation: “No error to round by: keep ten figures and let the caller say so.” The following lines create a small fallback error; I would not let a shared distance formatter use that fallback as if it were measured.

If you say no source exists — I did not find a source that supplies all the uncertainties required for all the distance, velocity and centre combinations in the current hover. The search covered the specified project code and rules, the Horizons manual, the DE430/431 report, the DE440/441 paper, the SBDB API, and the SPK reference. This is a bounded search result; particular spacecraft, moon or barycentre solutions may have additional published covariance information.

Confidence — High on the distinction between physical movement and positional uncertainty, and high that missing uncertainty should be represented explicitly. Medium on the final UI choice for unsupported values; Tony’s preference for preserving a useful hover may justify showing a coarse nominal value with a clear warning, while a stricter “only digits earned” mode may hide it until a suitable error source is available.