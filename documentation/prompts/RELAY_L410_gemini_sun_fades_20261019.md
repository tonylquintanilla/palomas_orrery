<!-- Doc-Kind: hand | Relay prompt for Gemini 4: check the sources behind the Sun's two fades (L-410 with L-131) and search for the ones still missing. Copy everything below the line into Gemini. -->
# Relay prompt for Gemini 4 -- the Sun's corona and dust cloud (L-410)

Written 2026-10-19 by Anthropic's Claude Opus 5.5 for Tony to carry to
Gemini 4. Copy everything below the line. Ask for the highest effort
tier Gemini offers: six of the rows are DISCOVERY rows, which are only
as good as how long the checker keeps looking.

---

Built on palomas_orrery 6e0cfacd0b6aa42cb09b0ca765be94e68aab6f70 at
https://github.com/tonylquintanilla/palomas_orrery and
tonyquintanilla.github.io 4fc320fa6d2e0e10d9a50b8b69006cbff96a1364 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. The rows
below are NOT in either repository yet, so every value you need is
written out here.
Vocabulary: v2 (2026-08-13)

## Who you are working for

Tony Quintanilla, PE, a retired civil and environmental engineer, builds
Paloma's Orrery, a 3D astronomy visualization (a desktop program and the
website palomasorrery.com), through conversation with AI partners. He is
not a professional programmer or astronomer. Every number a visitor
reads must come from a source anyone can open. Please write plainly.

## What is being drawn

Two new drawings of the Sun's surroundings, both as clouds of dots:

- The CORONA, the Sun's outer atmosphere of hot plasma, as one cloud
  thinning outward from the Sun's surface to the Alfven surface (about
  19.7 solar radii), where it becomes the solar wind. The dots are
  placed by a model of the electron density.
- The ZODIACAL DUST CLOUD, as a separate cloud: dust flattened toward
  the planets' plane, thinning with distance, thinning out again close
  to the Sun (the dust-free zone), and drawn out to 5.2 AU. Near the Sun
  its scattered sunlight is the F-corona.

In both, a dot's place shows density and its brightness shows the
sunlight it receives, which falls with the square of distance.

## The rules this job follows

If you have imported the palomas_orrery repository, read these two
files and name them at the top of your answer:

- skills/provenance-discipline/SKILL.md -- sections The Access Standard
  and What a Visitor Reads
- skills/provenance-cross-check/references/worksheets.md -- section
  Worksheet Types

If you have not imported it, say so; the rules you need are restated
here:

1. **Open sources only.** A source counts only if its text can be read
   without a paywall: open full text, a free abstract that states the
   claim, an agency page or document, an arXiv preprint. A source
   behind a paywall does not count, whatever its authority.
2. **Name what you opened.** Give the title and authors as printed in
   the document you actually opened, not a paper it cites.
3. **Quote it.** Every row needs a short verbatim quote from the source
   containing the figure or statement, and a locator (section,
   equation, table, page, or the exact URL). A row without both is
   recorded as UNVERIFIED whatever its verdict says. If you are
   recalling rather than reading, say so and leave the row UNVERIFIED.
   Silence is better than a guess.
4. **Temperatures are stored in kelvin.** If a source gives degrees
   Celsius, report the figure exactly as the source prints it; the
   conversion is ours.
5. **Prefer an agency or a peer-reviewed paper** (NASA, ESA, an open
   journal article or arXiv preprint) over an educational or news page.
   Say which kind each source is.

## Before any row: a pre-flight

Open this page and quote one sentence from it, so we know your fetching
works:

```
https://arxiv.org/abs/2202.11533
```

## Your answer's header

Start with one line naming your MODEL and your EFFORT TIER, then the
list of rule files you read (or "not imported").

## The two kinds of row

[CITATION] -- the row names a source. Open it and confirm it states the
figure or statement, at the figure's precision. Then, separately, check
the value against one other open source of your own choosing,
preferably an agency or a paper.

[DISCOVERY] -- the claim may have no source at all. Do not assume one
exists, and do not reconcile it with any other row. Find whether an
open source states it. UNSOURCED is a valid and useful answer, but a
negative must show its search: list the queries you actually ran and
the places you looked, in a SEARCH LOG under the table. A negative with
no search log is recorded as UNVERIFIED.

## The table

One row per numbered item below, in this exact layout:

| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Read by | Quote | Locator | Notes |

- **Read by**: who opened the source -- your model name.
- **Access word**: one of open full text, abstract, agency page, open
  document, educational page, news page.
- Each verdict cell holds EXACTLY ONE token, and the tokens belong to
  their column:

```
Value correct?     YES  NO  APPROX  UNVERIFIED
Citation correct?  YES  NO  PARTIAL  DERIVED  UNSOURCED  UNVERIFIED
```

  APPROX qualifies a value (right to a stated tolerance; say the
  tolerance in Notes). PARTIAL qualifies a citation (the source supports
  part of the claim). UNSOURCED means the named source does not publish
  the figure at all; NO means it publishes a different one. For a
  DISCOVERY row, "Citation correct?" answers whether the source you
  found states the claim.

- Put every URL as a bare address inside a code block, after the table,
  numbered by row. Links pasted as chips lose their address.
- Please deliver the whole answer as a downloadable Markdown file named
  worksheet_gemini4_<effort tier>_L410_sun_fades_20261019.md, as well
  as in the chat.

## The rows

### Citation rows (a source is named)

C1. The K-corona is sunlight scattered by free electrons in the corona;
the F-corona is sunlight scattered or diffracted by dust, and is the
part of the zodiacal light closest to the Sun. Source named: Boe,
Habbal, Downs and Druckmuller, "The Color and Brightness of the
F-Corona Inferred from the 2019 July 2 Total Solar Eclipse", arXiv
2103.02113, introduction. https://arxiv.org/pdf/2103.02113

C2. In the COBE zodiacal cloud model, the smooth cloud's density falls
with distance from the Sun as R to the power -alpha, alpha = 1.34
(+/- 0.022). Source named: Kelsall et al. (1998), "The COBE Diffuse
Infrared Background Experiment Search for the Cosmic Infrared
Background: II. Model of the Interplanetary Dust Cloud", ApJ 508, 44,
arXiv astro-ph/9806250, eq. 6 and Table 1.
https://arxiv.org/abs/astro-ph/9806250

C3. The same model's vertical shape, eq. 7 (the "widened, modified
fan"): beta = 4.14 (+/- 0.067), gamma = 0.942 (+/- 0.025), mu = 0.189
(+/- 0.014). Source named: as C2, Table 1.

C4. The same model's midplane: inclination 2.03 degrees (+/- 0.017) to
the ecliptic, ascending node 77.7 degrees (+/- 0.6). Source named: as
C2, Table 1.

C5. The same model integrates along each line of sight out to an outer
radial cutoff of 5.2 AU from the Sun. Source named: as C2, sec. 4.2.
Please also say whether the paper gives a reason for 5.2 AU.

C6. The outer border of the dust depletion zone is at about 19 solar
radii, and the zone extends down to about 5 solar radii, the boundary
of the dust-free zone. Source named: Lamy, Gilardy and Llebaria,
"Observations of the Solar F-corona from Space", Space Sci. Rev.
(2022), doi 10.1007/s11214-022-00918-y, arXiv 2202.11533, abstract.
https://arxiv.org/pdf/2202.11533

C7. The F-corona's radiance falls as a power law of elongation between
5 and 50 degrees, exponent -2.33 near the equator and -2.55 over the
poles. Source named: as C6, abstract and sec. 4.4.

C8. The inner zodiacal cloud's symmetry plane is strongly warped, and
its ascending node is constant at 87.6 degrees. Source named: as C6,
abstract.

C9. Parker Solar Probe's imaging on its first two perihelion passes, at
0.16 to 0.25 AU, showed the F-corona's intensity decreasing at short
elongations, suggestive of the dust-free zone. Source named: Howard et
al., "Near-Sun observations of an F-corona decrease and K-corona fine
structure", Nature 576, 232-236 (2019), doi 10.1038/s41586-019-1807-x,
abstract.
https://www.nature.com/articles/s41586-019-1807-x

C10. The Leblanc et al. (1998) electron density model: N_e(r) =
3.3e5 / R^2 + 4.1e6 / R^4 + 8.0e7 / R^6 electrons per cubic
centimetre, R in solar radii, for the region between the corona and
Earth's orbit in the ecliptic plane, giving 7.14 per cubic centimetre
at 1 AU. Source named: Mann, Warmuth, Vocks and Rouillard, "A
heliospheric density and magnetic field model", A&A 679, A64 (2023),
eq. 7, open access. Please also say from what height above the Sun the
model is stated to apply, if Mann et al. or any open source says.
https://www.aanda.org/articles/aa/full_html/2023/11/aa45050-22/aa45050-22.html

C11. Baumbach's electron density formula: n(r) = 1e8 (2.99 r^-16 +
1.55 r^-6 + 0.036 r^-1.5) per cubic centimetre, limited in principle to
1.05 to 3 solar radii. Source named: Lemaire, "Determination of coronal
temperatures from electron density profiles", arXiv 1112.3850v2, eq. 5.
https://arxiv.org/pdf/1112.3850

### Discovery rows (no source yet, or a better one wanted)

D1. Forward scattering. Find an open source that states, in words,
that interplanetary dust scatters sunlight mostly forward (a strong
forward peak in its scattering phase function), and that this is why
the F-corona or zodiacal light is brightest close to the Sun. Quote
the sentence.

D2. Where the zodiacal dust comes from. Find an open source (an agency
page or a paper) that states the dust's origin: comets, asteroid
collisions, or both, with the shares if it gives them. Report every
figure you find with its source; do not average them.

D3. The dust's density exponent near the Sun. Lamy et al. (C6) give the
radiance exponent as about 2.3 and the relation radiance exponent =
density exponent + 1, from which we worked out a density exponent of
about 1.3; it is not printed there. Find an open source that states the
inner cloud's density exponent directly (for example from the Helios
probes), with its value and uncertainty.

D4. One electron density model from the Sun's surface out. Find an open
source that prints, with numbers, a coronal electron density model
valid from about 1 solar radius out to at least 20 solar radii, in one
form. The Saito, Poland and Munro (1977) model is one candidate; report
its formula only if an open source prints it.

D5. The corona's temperature. Find an agency page or open paper that
states the corona's typical temperature (the project's old text said
one to three million kelvin). Report every figure with its source; do
not average them.

D6. Where the F-corona becomes brighter than the K-corona. Find an
open source that states the distance from the Sun (in solar radii) at
which the dust's light overtakes the electrons' light. The project's old
text said the K-corona dominates within about 2.3 solar radii and the
F-corona beyond about 3.

## What not to do

- Do not propose wording for the website.
- Do not combine rows, or reconcile one row's figure with another's.
- Do not fill a cell from memory. If you could not open a source, the
  cell is UNVERIFIED and Notes says what stopped you.
