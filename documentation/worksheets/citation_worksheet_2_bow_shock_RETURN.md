# Citation worksheet 2 of 3 -- RETURN
## Earth's bow shock

**Built on** `f1bceefd05eeee0cac38fd519dd207314acb2383` at
https://github.com/tonylquintanilla/palomas_orrery

Vocabulary: v2 (2026-08-13)

**Checker:** Anthropic's Claude Fable 5.1, working in Tony's Claude Project
(protocol and installed skills resident), 2026-09-13. Same session as
the worksheet 1 return.

**Rule files read at that SHA:**

- `PROJECT_INSTRUCTIONS.md`, section "Fetched vs Recalled Convention"
  (lines 739-753 at f1bceefd) -- READ, earlier this session, from a
  shallow clone at the pinned SHA.
- `skills/provenance-discipline/SKILL.md`, sections "The Access
  Standard [CRITICAL]" (line 380) and "Worksheet Types" (line 756) --
  READ, same clone.

**Code value check.** `EARTH_BOW_SHOCK_JELINEK_R0_RADII = 15.02`,
`EARTH_BOW_SHOCK_JELINEK_EPS = 6.55`, `EARTH_BOW_SHOCK_JELINEK_LAMBDA
= 1.17` in `constants_new.py` at f1bceefd. 15.02 x 2^(-1/6.55) =
13.5117, which rounds to the rendered 13.51. At 1 nPa the same
relation gives 15.02; at 3 nPa, 12.70.

**Access note on the Jelinek primary.** Wiley labels
doi:10.1029/2011JA017252 "Free Access", so it passes the Access
Standard; my sandbox is refused by bot detection, as it was for Shue.
The search-result snippets of the Wiley full-text page do show the
paper's own words on coordinates and symmetry, and the model is
restated in two open sources named below. Access to the primary is
therefore SNIPPET-grade in this return, not OPEN.

---

| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |
|---|-----|-------|-----------|-----------|-------------|----------------------------------|----------------|-------------------|-------|
| 1 | CITATION | The bow shock is the boundary where the supersonic solar wind is first slowed by Earth's magnetic field | (no figure) | Right in substance: the bow shock is a collisionless shock that forms sunward of Earth while the solar wind's fast-magnetosonic Mach number exceeds 1; behind it the flow is slower than the fast magnetosonic speed. | n/a | Lugaz et al. (2016), Nat. Commun. 7:13001, full text at https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5063966/ (OPEN). Farris & Russell (1994) abstract, https://ui.adsabs.harvard.edu/abs/1994JGR....9917681F/abstract (ABSTRACT). | APPROX | UNSOURCED | No citation is attached to this definition; the hover's only source line is for the standoff. APPROX on two words. "Supersonic" -- the relevant threshold is the fast-magnetosonic Mach number, not the sound speed alone (Lugaz makes exactly this distinction). "By Earth's magnetic field" -- the obstacle is the magnetosphere as a whole, whose outer surface is the magnetopause; the field is what holds it up. Neither is wrong for a visitor; both can be tightened cheaply: "where the solar wind, moving faster than waves can travel in it, is abruptly slowed and heated by running into Earth's magnetosphere". **On Farris & Russell, as the worksheet asked:** your reading is correct. Its abstract says it develops a semi-empirical Mach-number relation for the standoff DISTANCE and analyses how that distance depends on the size and shape of the obstacle -- specifically arguing the standoff should be compared to the obstacle's radius of curvature. The obstacle's shape is an input; the paper predicts no shock shape. Dropping it as the source for the drawn FORM was right. It would be a legitimate source for one sentence you do not currently print: that the shock's distance depends on the Mach number and on the magnetopause's curvature. |
| 2 | CITATION | It is typically located about 13.51 Earth radii upstream on the Sun-facing side | 13.51 R_E | Arithmetic: 13.5117 R_E. Independent quiet-time figure: 11 to 15 R_E (Lugaz 2016 gives 11-14; Fairfield 1971 via a 2022 ApJ paper gives ~11-15). | R_E from Earth's centre along the aberrated Sun-Earth line (Jelinek); "subsolar distance", frame unstated, R_E = 6,371 km (Lugaz) | Jelinek relation restated: Ghosh et al. (2017), https://arxiv.org/pdf/1709.01407 (OPEN; eq. 10 prints r_bs = 15.02 P_d^(-1/6.55) R_E and attributes it to Jelinek 2012). Jelinek, Nemecek & Safrankova (2010), WDS proceedings, https://physics.mff.cuni.cz/wds/proc/pdf10/WDS10_227_f2_Jelinek.pdf (OPEN; the authors' precursor paper, lambda_BS = 1.17, and the validation refit 14.94 p^(-1/6.62)). Lugaz (2016), PMC, OPEN, as row 1. Zhang et al. (2022), ApJ, https://iopscience.iop.org/article/10.3847/1538-4357/ac4471 (search snippet, SNIPPET: "~11-15 R_E ... (Fairfield 1971)"). | YES | DERIVED | Two questions, answered separately. (1) Does Jelinek at 2 nPa give 13.51? Yes: 15.02 x 2^(-1/6.55) = 13.5117. The coefficients match the open 2017 restatement exactly. (2) Is 13.5 defensible as a quiet-time subsolar bow shock? Yes: it sits inside every independent range I could open (11-14, 11-15) and is the model's own answer at the pressure Shue calls average. **Precision, plainly:** four significant figures overstate what the data carry. Jelinek reports no uncertainty on 15.02 or 6.55, and the crossings scatter about the model by 0.69 R_E (your reading of fig. 7; I could not open the figure, so I am taking that number from `constants_new.py`, not confirming it). The standoff also moves with Bz and Mach number, which this relation omits, and by a full Earth radius between 1 and 3 nPa. "About 13.51" therefore reads as a measurement when it is a model evaluated at a declared input. 13.5 is honest; "about 13 to 14" or "about 14" is more honest still. DERIVED because no source publishes 13.51; the row is complete (inputs named, arithmetic shown, it closes) and inherits the rung of its weakest input, the declared 2 nPa (L-314). |
| 3 | CITATION | Jelinek, Nemecek and Safrankova (2012), J. Geophys. Res. 117:A05208, doi:10.1029/2011JA017252 supports the bow shock standoff | citation row | Yes -- the paper's bow shock model is R_BS = R0 p^(-1/eps) with R0 = 15.02, eps = 6.55, fitted from THEMIS 2007-2009 in aberrated GSE, rotationally symmetric about the aberrated X axis | R_E | Wiley full-text page via search snippets, https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2011JA017252 (SNIPPET; labelled "Free Access"; bibliographic details confirmed: JGR 117, A05208, 2012, corresponding author Nemecek, Charles University; the section-3 text on aberrated GSE and rotational symmetry is visible in the snippet). Ghosh et al. (2017), OPEN, and the 2010 WDS precursor, OPEN, as row 2. A 2025 JGR paper on MMS bow shocks (Wiley, SNIPPET) describes the Jelinek model as a paraboloid with parameters R0, eps, lambda and standoff R_BS = R0 P^(-1/eps). | YES | YES | The citation string is bibliographically correct and the paper is the origin of the standoff relation the orrery evaluates. Three independent later papers attribute the same form and numbers to it. Two cautions carried over from the code's own notes, which I could not check against the figure or the equation numbers directly: the validation refit (12.90 / 14.94, section 5.2) is a different pair from the model (eq. 14), and the precursor 2010 proceedings prints the 14.94 pair as ITS eq. 14, so anyone citing "eq. 14" should say which paper. |
| 4 | CITATION | Lugaz et al. (2016), Nat. Commun. 7:13001, doi:10.1038/ncomms13001 states that under normal solar wind the bow shock forms at a subsolar distance of 11 to 14 Earth radii | corroboration row | Yes, verbatim in the introduction: "Under normal solar wind conditions, a bow shock forms sunward of Earth with a subsolar distance of 11-14 Earth radii (R_E = 6,371 km)". The abstract states the same thing as 60,000-100,000 km. | R_E with R_E = 6,371 km; "subsolar distance", no coordinate frame named | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5063966/ (OPEN, full text); https://www.nature.com/articles/ncomms13001 (OPEN, open-access article page). | YES | YES | Lugaz states it. Frame: not specified; "subsolar" means on the Sun-Earth line, and the sentence attaches no citation of its own in the text I could see, so it is the authors' summary of the field, not a measurement they made. 60,000-100,000 km / 6,371 km = 9.4-15.7 R_E, so the abstract's round figures are looser than the introduction's. **Is the agreement with 13.51 meaningful?** Partly. Both describe the quiet-time subsolar shock, so 13.5 landing inside 11-14 is the kind of agreement one should expect and would be worried not to see. But it is not a check on the Jelinek evaluation, for two reasons: Lugaz gives no pressure, Bz or Mach conditions, so "normal" is undefined, and the Jelinek relation itself leaves that range at 1 nPa (15.02). Read it as "13.5 is a normal number", nothing sharper. Keeping it as a corroborating range, out of visitor text, is the right disposition. |

---

## Two things Tony has to decide

1. Row 2 precision. Print 13.5 (or "about 14") rather than 13.51. The
   data support one decimal at most, and the sentence should say it is
   a model value at a declared pressure.
2. Row 1 wording. Two words are loose ("supersonic", "magnetic field");
   fix or leave. No citation is attached; Lugaz (2016) is an open one.

Nothing else in this worksheet needs a ruling. Rows 3 and 4 clear.
