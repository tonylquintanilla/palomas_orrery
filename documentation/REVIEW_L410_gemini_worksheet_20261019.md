<!-- Doc-Kind: hand | Review of Gemini's L-410 source worksheet for the Sun's two fades: what it confirmed, what it found, where it held back, what the re-opening caught, and how it did as a checker. -->
# Review of Gemini's worksheet, L-410 (the Sun's corona and dust cloud)

Built on palomas_orrery 6e0cfacd0b6aa42cb09b0ca765be94e68aab6f70 at
https://github.com/tonylquintanilla/palomas_orrery and
tonyquintanilla.github.io 4fc320fa6d2e0e10d9a50b8b69006cbff96a1364 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Written 2026-10-19 by Anthropic's Claude Opus 5.5. The worksheet is
`documentation/worksheets/worksheet_gemini4_standard_L410_sun_fades_20261019.md`,
saved by Tony. The prompt it answered is
`documentation/prompts/RELAY_L410_gemini_sun_fades_20261019.md`. This
is the second slice relay (provenance-cross-check 1.1, The Slice
Relay).

## In one sentence

A useful leg that read and quoted throughout, found the corona model's
one real limit and the dust's origin, and named the wrong authors for
two of the papers it opened, which only re-opening them caught.

## Which model answered

Its header reads "Gemini 3.1 Pro (serving as the requested Gemini 4
auditor)", effort tier "Standard". The prompt asked for Gemini 4 at its
highest tier. The worksheet's filename says gemini4; its own header
says 3.1 Pro at a standard tier, and the header is the record. Whether
Tony's session was Gemini 4 is his to say.

## What it confirmed (citation rows), with a quote and a locator

- C2, C3, C4: Kelsall et al. (1998), Table 1, every value and
  uncertainty, and the second source it chose (Takimoto et al. 2026)
  writes the same fan model.
- C5: the 5.2 AU cutoff, and the paper's reason, which the prompt
  asked for: it "roughly corresponds to the orbit of Jupiter".
- C6, C8: Lamy et al. (2022), the depletion zone from about 19 to
  about 5 solar radii, and the warped inner plane, node 87.6 degrees.
- C9: Howard et al. (2019), the decrease seen at 0.16 to 0.25 AU.
- C11: Baumbach's formula in Lemaire, eq. 5, 1.05 to 3 solar radii.

## Where it held back

It marked PARTIAL, rather than YES, three rows whose full page it could
not open: C1 (only Boe et al.'s abstract), C7 (the 5 to 50 degree range
inside Lamy et al.'s large PDF) and C10 (aanda.org blocked; it read Mann
et al. through ResearchGate). All three stand on this session's own
reads of the full texts, recorded in the sources record. By the
send-back rule a PARTIAL earns no cross-check leg; none is claimed.

## What it found, and what re-opening it showed

Every figure below was re-opened here before anything is built on it.

- **C10, the corona model's limit (the important find).** The Leblanc
  et al. (1998) model holds only beyond about 1.8 solar radii. Re-opened
  and confirmed: Zic, Vrsnak and Temmer, "Heliospheric Propagation of
  Coronal Mass Ejections: Drag-Based Model Fitting", arXiv 1506.08582,
  state the expression "is valid for radial distances R > 1.8". So
  Leblanc cannot draw the corona from the surface. By the method in the
  sources record (one open model across the drawn range), the corona's
  fade moves to Mann et al. (2023)'s own model, which covers 1 to 250
  solar radii (eq. 11, Table 8); Leblanc stays as a cross-check beyond
  1.8. Gemini named arXiv 1506.08582 as "Reid & Kontar (2015)"; the
  paper's authors as printed are Zic, Vrsnak and Temmer.
- **D2, where the dust comes from.** Re-opened: Nesvorny, Jenniskens,
  Levison, Bottke and Vokrouhlicky, "Cometary Origin of the Zodiacal
  Cloud and Carbonaceous Micrometeorites. Implications for Hot Debris
  Disks", arXiv 0909.4322, abstract: 85-95% of the observed mid-infrared
  emission from particles from the Jupiter-family comets, under 10% from
  long-period comets, asteroidal dust under 10%, and about 85% of the
  mass reaching Earth from Jupiter-family comets. Usable for the words
  list's item 3b. Gemini's author list adds a sixth name, Gounelle, not
  on the arXiv copy.
- **D4, one density model from the surface.** Saito (1970)'s formula
  is confirmed in Grechnev, Uralov, Chertok, Kuzmenko, Afanasyev,
  Meshalkina, Kalashnikov and Kubo, arXiv 1104.3374, eq. 2, which states
  no radial range for it. Gemini named the paper "Afanasyev & Uralov
  (2011)". Without a stated range it cannot be the one model; Mann et
  al. is (above). The Saito, Poland and Munro (1977) two-term fit (Cho
  et al. 2011) was not re-opened; not needed.
- **D1, forward scattering: still unsourced.** Its second source,
  arXiv 2605.12979 (Liu et al., "Forward Modeling of Dust-Induced Stray
  Light in Ground-Based Coronagraphs"), re-opened: it is about dust on
  a telescope's own optics, and never links forward scattering to the
  F-corona or the zodiacal light. Its first (Mann et al. 2006) was read
  through ResearchGate and not re-opened; its third is a commercial
  web page. Lasue, Levasseur-Regourd and Renard (2020), arXiv
  2005.07480, re-opened here as a further try, does not state it
  either. The words keep it out.
- **D3, the inner density exponent.** Helios, 1.3 +/- 0.05 (Leinert et
  al. 1981, as reported in two open papers), 1.3 +/- 0.2 in Kuchner et
  al. (NASA NTRS), Clementine 1.45 +/- 0.05. Not re-opened: they agree
  with Kelsall's 1.34, which the drawing uses, so nothing turns on them.
- **D5, the corona's temperature.** NASA Science, "Our Sun: Facts": up
  to 2 million degrees Celsius; NSO: 1 million kelvin to more than 10
  million. Leads, not re-opened; a temperature comes back only if Tony
  wants one, from the NASA page re-opened at the build.
- **D6, where the dust's light overtakes the electrons'.** Figures from
  2.3 to 6 solar radii across five sources, by latitude and the solar
  cycle; the old text's 2.3 and 3 match Shopov et al. (2004). A spread,
  not one figure; leads, not re-opened, and not in the words.

## How it did, against the rules

- Header: model and tier given, rule files "not imported", said
  plainly. The pre-flight quote was given.
- Quotes and locators on every row; one verdict token per cell, from
  the right column.
- A search log for every discovery row, with the queries run.
- Held back on pages it could not open, as PARTIAL with the reason.
- Three attribution errors, all in second or discovery sources, all
  found only by re-opening: two papers under the wrong authors, one
  source that does not say what its row uses it for. This is the slice
  relay's re-open step doing its job: a discovery find is a lead until
  it is opened again.

Session written October 2026 with Anthropic's Claude Opus 5.5.
