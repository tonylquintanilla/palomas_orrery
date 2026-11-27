<!-- Doc-Kind: hand | Review return, GPT, to documentation/REVIEW_REQUEST_L560_printed_precision_20261127.md (L-560, a digit is earned). Tony's paste, verbatim below the line. Communication; a claim until each figure is checked at its source. -->
# Review return -- GPT 6.2 Astra, Medium -- how many digits may a public page print (L-560)

**Built on** orrery `489e4128056cd08fa46b0c11b90c64fe477ab028` at
https://github.com/tonylquintanilla/palomas_orrery and website
`fafdaeb6ce199b0d5f436dc4c77870f7d1c5c33e` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, the
anchors of the request this answers:
`documentation/REVIEW_REQUEST_L560_printed_precision_20261127.md`.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

- Brought by Tony to the coordinating session on 2026-11-27, 10:11
  Chicago, as the first of two attachments, with the words "Here are
  the responses from GPT and Gemini." The model is named by Tony,
  10:26 the same day: "the first response was GPT 6.2 Astra Medium and
  the second Gemini 4 Neon."
- Saved here at his word ("Please save them to documentation/worksheets
  for reference."), by Claude Fable 5.2, with nothing changed below
  the line: every byte is as pasted, link markers included.
- Its read-back: it says it fetched and read both rule files at the
  orrery commit above.
- NOT VERIFIED. No figure, quotation or source below has been checked
  at its source by a session. Each is a claim until it is.

---- the reply, as pasted ----

Tony, I would adopt four significant figures as a ceiling for the public box, then print fewer whenever the evidence calls for it. The most important change to L-560 is to attach the uncertainty to a particular distance on a particular date. “Titan from Saturn” and “Titan from the Sun” need different evidence. The same is true of “Voyager as seen on the sky” and “Voyager’s distance from Earth.”

I fetched and read both requested rule files at orrery commit 489e4128056cd08fa46b0c11b90c64fe477ab028, including the existing treatment of source accuracy, drift, interpolation between saved positions, and missing uncertainties. PROJECT_INSTRUCTIONS.md⁠￼ · Provenance discipline⁠￼

1. Is the rule standard practice?

Reporting an estimate to a place consistent with its uncertainty is standard scientific practice. I found no common astronomical rule requiring every ephemeris producer to print only those digits. An ephemeris is a prediction of position over time. The international Guide to the Expression of Uncertainty in Measurement, §7.2.6, says it usually suffices to report the uncertainty “to at most two significant digits.” The estimate is then rounded consistently with it. This leaves room for a last digit that is uncertain. The standard does not promise that every displayed digit is correct. 

The producers explain their choices differently. JPL’s Horizons manual, Statement of Ephemeris Limitations, says of its vector output, “This does not mean all digits are physically meaningful.” Extra digits help people carry out further calculations. IMCCE’s Miriade service, Notes to user, likewise says its extra precision is “given to avoid truncation error.” The US Naval Observatory’s history of the printed Astronomical Almanac records an editorial decision to give additional precision to “tabulated true distance of the planets from Earth.” The Minor Planet Center offers a choice of truncated or full sky coordinates and publishes a separate orbit-quality indicator. That indicator describes how uncertainty accumulates along an orbit and does not supply a kilometre uncertainty for distance. 

2. Is there a table by class of body?

I found authoritative tables for particular systems and solutions, but no single table covering planets, major moons and spacecraft that can authorize digits for all dates and centers. JPL’s Planetary Satellite Ephemerides is an index of which orbit solution is used. Its description says it “lists the current JPL planetary satellite ephemeris used for each planetary satellite.” Jacobson’s Saturn paper, by contrast, actually tabulates orbital uncertainties by moon, direction and year. That is the kind of table L-560 needs. 

There is an important correction to “what we have so far.” The planetary values in your request are the project’s rounding places. Folkner and colleagues’ DE430/DE431 abstract gives the underlying descriptions as “a few hundred meters,” “tens of kilometers” and “several thousand kilometers.” Your pinned rule file already recognizes that distinction. Its half-unit is a device for reproducing a formatting decision. It should never reach a visitor as an uncertainty measured by JPL. Also, the later DE440/DE441 paper reports improved orbits for Jupiter, Saturn and Pluto. The older report can document the origin of an editorial choice, but assigning its words to a newer solution requires a separate justification. 

The Moon illustrates the center problem especially well. Folkner’s abstract says the lunar orbit is known to “submeter accuracy through fitting lunar laser ranging data.” This is evidence about the Moon’s motion relative to Earth. A distance from the Sun also depends on where the Earth–Moon system is. The project’s own Moon row correctly says “the Moon’s orbit about Earth.” I would preserve those words wherever the figure is used. The same question applies to Phobos and Deimos relative to Mars. 

3. What can be said for Io, Europa, Ganymede and Callisto under JUP365?

I found a published observational check against JUP365, but no verified JUP365 uncertainty in kilometres for the distance of each of the four moons. Morgado and colleagues’ Milliarcsecond astrometry for the Galilean moons using stellar occultations, Table 4 and §IV, compares observed sky positions with predictions. The table identifies the combination as “ephemeris de440 and jup365.” The authors describe their observations as having “a typical uncertainty below 2 mas (∼6 km at Jupiter distance).” Those observations locate a moon across our line of sight when it passes in front of a star. They do not measure how far away it is along that line. JUP365’s own comment file separately identifies a “Chebyshev interpolation error,” which measures how faithfully the file reproduces the fitted orbit. Neither figure earns a distance digit. 

There is a useful comparison scale if the page or ledger labels it accurately. Fayolle’s Natural Satellites Ephemerides, discussion of Fig. 3.4, compares a different JPL solution, JUP380, with the independent French solution NOE-5-2023. For Io, Europa and Ganymede, the differences were “on average, constrained within 10-15 km.” For Callisto’s position along its orbit, they were “about 40 km on average.” That puts disagreements between these solutions on the scale of tens of kilometres. An average difference between predictions cannot serve as an upper limit on JUP365’s error. I would leave the four JUP365 distance uncertainties open. 

4. What can be said for Titan, Pluto and Charon?

Titan has a direct answer for distance from Saturn. In Jacobson’s The Orbits of the Main Saturnian Satellites, §4.8 defines the radial direction as “along the radius from Saturn.” Table 13, p. 9, gives the following one-standard-deviation estimates. The relevant excerpts are “Titan 250 m 1.3 km 1.2 km” and “261 m 1.8 km 1.2 km.” The second and third columns of uncertainties describe motion along the orbit and perpendicular to its plane. 

SAT441 assessment year	Distance from Saturn	Along the orbit	Perpendicular to the orbit
2018	250 m	1.3 km	1.2 km
2033	261 m	1.8 km	1.2 km

The published scale for Titan from Saturn is therefore a few tenths of a kilometre at one standard deviation at those two assessment dates. The paper also says radial uncertainties have “little or no variation” for most satellites, including Titan. For Titan from the Sun, the direction of interest changes and the uncertainty in Saturn’s own position enters. Table 13 alone cannot settle that box. 

For Pluto and Charon under PLU060, I could not verify a distance uncertainty in kilometres. I read the Brozović–Jacobson abstract and the released file’s comments. I could not retrieve the full journal article. The abstract says, “Our orbit fit yielded the following masses,” and the uncertainties that follow describe masses. There is a genuine earlier position estimate in Brozović and colleagues’ The Orbits and Masses of Satellites of Pluto, abstract, p. 1. It gives “few tens of km or less for Charon, Nix, and Hydra” for the predicted New Horizons encounter. That is an earlier solution at a particular encounter. I would enter neither a modern PLU060 value for Charon from Pluto nor one for Pluto or Charon from the Sun on that evidence. For the latter distances the location of the system’s barycenter, its common center of mass, also matters. 

5. Is there a class-wide spacecraft figure?

I found no defensible class-wide kilometre figure. Use the mission, the trajectory product, the date and the direction being measured. NASA’s Basics of Space Flight, chapter 13, distinguishes “orbit reconstruction,” “orbit determination” and “orbit prediction.” Those are the three cases your boxes need. 

A craft being tracked now. Look first at the Horizons spacecraft data sheet for the trajectory’s source and coverage, then at the navigation team’s orbit-determination report for that period. Check what its quoted error measures. The pinned orrery already identifies a particularly instructive case. The Voyager figures it uses are described there as predicted pointing uncertainties seen from Earth. Converting an angle to kilometres at Voyager gives a displacement across the sky. It supplies no measurement of the error in Voyager’s distance along the line of sight. I would keep that information for a pointing description and remove it as evidence for rounding a range. Pinned Voyager treatment⁠￼ 

An ended mission at last contact. Use the best reconstructed trajectory covering the time of that contact and the uncertainty assessment for that segment. The reception of a last signal dates an event. By itself it says nothing quantitative about the error in position. The places to look are the mission’s final navigation report, its archived trajectory documentation, and the comments accompanying the trajectory file. A predicted path needs the assessment for that forecast and its date of issue, especially if future maneuvers were assumed. NASA’s archive guidance warns that predicted and reconstructed data can be combined in one file, so its date coverage alone is insufficient. 

6. Can a long-unobserved comet have a defensible present distance?

Yes. Ask Horizons for the uncertainty on the displayed date. Time since the last observation alone cannot decide whether to print the distance. I queried Horizons directly for Sun-centered geometric positions on November 27, 2026, at 00:00 TDB, the time scale used in these vector tables. The column legend calls R_s the “Radial direction 1-sigma position uncertainty (km).” Here that direction runs from the Sun to the object, so it answers the distance question directly.

Target returned by Horizons	Approximate formal uncertainty in distance from the Sun	Exact excerpt from the first RTN(1-sigma) row
Comet West, fragment A, JPL solution 2	2.56 million km	2.55619285E+06 Horizons result⁠￼
1I/‘Oumuamua, JPL solution 16	173,000 km	1.72933532E+05 Horizons result⁠￼
3I/ATLAS, JPL solution 55	5,300 km	5.30004559E+03 Horizons result⁠￼

These three path objects can move out of the “no source found” group for that date and those solutions. For West, retain the fragment designation. For a path drawn across many dates, request the corresponding uncertainty along the path. There is no fixed growth rate. The span and quality of the observations, gas escaping from a comet, and encounters with planets can all change the forecast. Horizons specifically warns that its simplified propagation of uncertainty can become optimistic far from the time of the orbit fit. 

I also confirmed n.a. for the Halley solution I selected, both listed Ikeya–Seki fragments, and the Bennu trajectory returned by Horizons, identified as ORX_merged_DE424. The appropriate wording is “Horizons gives no distance uncertainty for this trajectory.” That finding is narrower than saying nobody knows the distance or JPL has never estimated its uncertainty. Where the project requires sourced digits, a drawn path can still be labeled “predicted orbit” while the numerical distance is withheld. Halley result⁠￼ · Ikeya–Seki A⁠￼ · Ikeya–Seki B⁠￼ · Bennu result⁠￼. 

7. Should the page cap the number of significant figures?

Yes. Four is a reasonable editorial choice for this audience. I found no four-figure standard at NASA or in the printed almanac. NASA’s public planet comparison describes Earth’s average distance as “93 million miles (149.7 million kilometers).” The same sentence uses different numbers of significant figures in the two units. It also explicitly says average, an important distinction for an orrery showing a distance now. 

The cap makes the default box readable. Its weakness is that four figures can still overstate a poorly known orbit and can conceal real changes in a well-known one. Also, an uncertainty smaller than one unit of the last place does not guarantee that the last digit is right. If the estimate lies near a rounding boundary, even a small change can move it to the adjacent printed value. Treat the last place as the resolution of the display. Where it matters how far the value could move, show the uncertainty itself. Apply the same physical evidence to both AU and kilometres, so the parenthesis cannot quietly restore digits the first number discarded. 

8. What should the page say about precision, accuracy and uncertainty?

Use “displayed digits” or “rounding place” for what the visitor sees. In the international metrology vocabulary, precision describes agreement among repeated measurements under specified conditions. Accuracy describes closeness to the true value. Uncertainty describes the spread of values reasonably attributable to the quantity, given the information available. A formal orbit uncertainty is the spread estimated by fitting observations under stated assumptions. The actual error is the difference from the true position and is generally unknown. A shared bias in the observations or a missing physical effect can make the formal estimate too optimistic. 

For a single distance with a sourced radial uncertainty, three sigma is a defensible project convention. One sigma means one estimated standard deviation. For a single quantity with an approximately bell-shaped error distribution and a reliable estimate of its spread, NIST says the one-sigma interval covers “approximately 68 %”; Horizons describes its three-sigma interval as “99.7%” under its statistical assumptions. That percentage does not carry over automatically to a three-dimensional position, a historical accuracy described in words, or an unmodeled error. The Horizons observer table’s RNG_3sigma is already three sigma. Its apparent range includes light-travel time, so use care before substituting it for an instantaneous geometric distance. The Sun-centered vector-table R_s used above is one sigma and matches the geometric distance in question. 

I would make one final distinction in the project rule. Taking the largest of source uncertainty, drift and interpolation error can guide rounding. It does not establish a total three-sigma uncertainty for the displayed value. More than one contribution can act in the same direction. Reserve a label such as “JPL’s estimated uncertainty in distance” for JPL’s contribution. Use “rounded to account for the orbit estimate and the page’s approximation” when the page’s own calculation also sets the last place.

My proposed wording for L-560 is: “Show up to four significant figures. Use fewer when the evidence for this body, center and date calls for a coarser distance. Name the source and what its uncertainty describes. When the source gives no uncertainty for that distance, say so.”