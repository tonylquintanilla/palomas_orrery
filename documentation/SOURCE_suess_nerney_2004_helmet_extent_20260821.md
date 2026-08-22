# Source record -- Suess & Nerney (2004), helmet extent

**Retrieved from NASA ADS on 2026-08-21 by Tony Quintanilla.** Record
written the same day with Anthropic's Claude Opus 5, against repo
`6184b3b9` at https://github.com/tonylquintanilla/palomas_orrery.

## The paper

- **Title:** Flow in streamer boundaries, and streamer stability
- **Authors:** Suess, S. T.; Nerney, S.
- **Publication:** Advances in Space Research, Volume 33, Issue 5,
  pages 668-675
- **Year:** 2004
- **DOI:** 10.1016/S0273-1177(03)00237-0
- **Bibcode:** 2004AdSpR..33..668S
- **Refereed:** yes
- **Keywords:** solar wind; solar corona; streamers

The bibcode is the handle to prefer in annotations. It resolves to the
ADS record, which is public. The DOI resolves to ScienceDirect, which
is paywalled.

## Why it was read

`STREAMER_BELT_RADII` in `constants_new.py` has carried 6.0 R_sun as a
declared visualization assumption since 2026-08-20 (L-210), after an
independent source read found its citation stack unsupported. The
shell is being redesigned from a sphere into a band with a pinch at
the helmet cusp, and the cusp radius needed a source rather than a
choice. This paper was already cited in the shell function's docstring
for a 2-4 R_sun helmet extent; this record is the read that confirms
the citation resolves and says what kind of claim it is.

## What we take from it

Two claims, paraphrased. The exact wording is in the abstract at the
bibcode above.

**1. Helmet extent.** Streamers as a whole reach out to many solar
radii, but the CLOSED-field portion -- the helmet -- goes no higher
than 2-4 solar radii. This is the figure the shell docstring already
cited and the basis for placing the band's cusp at 4, the top of the
stated range.

**2. What the visible streamer boundary is.** Because the closed
region stops so low, the brightness boundary that makes a streamer
visible in a coronagraph cannot be the edge between static plasma and
expanding wind. The paper describes it instead as a boundary between
different FLOW REGIMES, and states that it is reasonable to assume
this boundary separates fast coronal-hole wind from slow wind.

A third detail, not load-bearing but relevant to what the cusp means:
the modelled flow can leak out of the cusp in a way the paper likens
to the small mass releases SOHO/LASCO observes.

## Kind -- and this is the part that constrains the drawing

**Claim 1 is stated as established background, not measured here.**
The paper's own result is an essentially analytic MHD stagnation-flow
model of the streamer boundary. So `# Source:` is the correct leg and
the citation is sound, but the annotation should say the figure is
carried as context in a modelling paper. A later reader must not
mistake 2-4 for this paper's measurement.

**Claim 2 is explicitly an assumption.** The paper's own words mark it
as a reasonable thing to assume, not something it demonstrates. That
matters because the band's redesign would render this boundary as a
visible feature, and drawing a claim asserts it harder than writing it
does. It needs either an observational reference or an explicit
in-hover statement that the identification is an interpretation.
OPEN as of 2026-08-21.

## Related figures found while searching, NOT verified

Recorded so a later read does not start cold. Neither has been read at
source and neither may be cited on this basis.

- Endeve, Holzer & Leer 2004, ApJ 603 -- a two-fluid MHD model placing
  the helmet at about 3 R_sun along the equator.
- A 2005 review reports SOHO/UVCS placing the start of the
  heliospheric current sheet above the streamer core beyond about
  2.7 R_sun. Observational, and the closest thing to a measurement
  found so far.

Both sit below 4, which is consistent with 4 being the generous upper
edge of a range rather than a measured value.

## Abstract as retrieved

Deliberately left empty. See the note in
`patch_L210_7_source_record_suess_nerney.py` -- the verbatim abstract
is Elsevier's text and is one click away at bibcode
`2004AdSpR..33..668S`. Paste it here if a local copy is wanted.

## References from this record

- L-210 -- the streamer row, its withdrawn citations and its held value
- L-209 -- the Alfven surface, where the band dissolves
- `constants_new.py::STREAMER_BELT_RADII`
- `solar_visualization_shells.py::create_sun_streamer_belt_shell`
