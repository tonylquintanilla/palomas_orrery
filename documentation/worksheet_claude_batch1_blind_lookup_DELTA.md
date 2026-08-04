# Blind Lookup -- Second Claude Pass: Delta Only

**Built on `0739e6bd23f8351241d8a17e3d243f310833755f`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Checker:** Claude Opus 5 (second pass)
**Date:** 2026-08-03
**Companion to:** `worksheet_claude_batch1_blind_lookup.md`, anchored at
`31c2666`, already in the outputs directory.

---

## Why this is a delta and not a worksheet

I researched BL-1 through BL-8 and went to write it up, and the write
failed: **a completed Claude blind-lookup worksheet for this prompt
already exists**, timestamped three minutes before mine and anchored to
a different HEAD (`31c2666` against my `0739e6b`).

I did not overwrite it. This file records only what my pass adds.

**Please do not treat the agreement between the two as confirmation.**
Two Claude passes are one model running twice. We share training,
reasoning habits, and -- since I hit the same abstracts -- most of the
same sources. Where the two agree, that is one leg reported twice, not
two independent legs. The weight on these items still rests on GPT's and
Gemini's worksheets.

I also was not blind. I had read all three follow-up worksheets before
starting, so I knew which values were disputed and which paper each leg
had proposed.

---

## Where the two passes agree

BL-1 (~1400 R_M from Baumgardner 2008, >1000 R_M from Schmidt 2010,
<120 R_M during the MESSENGER flyby window), BL-2 (875 K confirmed with
the model inputs), BL-5 (NOT FOUND in the Williams LLR work), BL-6
(Bierson abstract contains no temperature at all), BL-7 (second-hand
only), and BL-3/BL-4 not attempted.

That the two passes converged independently on the same abstracts is
mildly reassuring about the lookups themselves. It is not a second
opinion.

---

## Four things this pass adds

### 1. BL-2 authorship: Nimmo & Brown, not Szakats

The paper is **Francis Nimmo and Michael E. Brown**, *Sci. Adv.* 9,
eadi9201 (2023). GPT hedged between "Szakats et al." and "Nimmo and
coauthors." Szakats et al. 2023 (*A&A* 669:L3) is a different paper --
the discovery of Eris's tidally locked rotation -- which Nimmo & Brown
cite as input. Getting this right matters, because the citation about to
be written names the authors.

### 2. BL-2 has a fourth input, not three

Both GPT and the earlier pass list three model inputs. The paper's
sentence carries four: the **present-day chondritic heating rate of
4.5e-12 W/kg**, alongside k = 3 W/m/K and Ts = 30 K. If the point of
recording inputs is reproducibility, the heating rate is the one that
actually sets the scale.

### 3. BL-2 gives a better citation for Eris's rocky core than Sicardy

The Nimmo & Brown abstract states that Eris **must have differentiated
into an ice shell and rocky core**, and that its ice shell must be
convecting -- unlike Pluto's conductive shell.

That is a real, citable structural claim. It does not publish a mass
fraction, so ">85% rock" is still unsourced. But for the underlying
"Eris is rock-dominated and differentiated" statement, Nimmo & Brown
2023 is a far better citation than Sicardy 2011, which reports only
density. This bears directly on FU-Er1, which three legs had left
stranded.

### 4. BL-5 by-product: the lunar core *dimensions* are defensible

While failing to find lunar core temperatures, I found the dimensional
constraints the Williams LLR work does publish, plus GRAIL-era
modelling:

- LLR 1-sigma upper limit on core radius: **352 km** (pure Fe) or
  **374 km** (fluid Fe-FeS eutectic), about 20% of the lunar radius
- GRAIL-era models: **fluid outer core radius 200-380 km**, **solid
  inner core radius 0-280 km**, inner core mass fraction 0-1%

The code's **240 km inner core** and **330 km outer core** both fall
inside those published ranges. So the geometry the shells actually
render is sourceable even though the temperatures printed beside it are
not -- worth knowing before anyone deletes the whole block.

---

## BL-8, which neither pass sourced

Both passes marked this NOT ATTEMPTED as a lookup. I offer the physics,
labeled as reasoning:

**The system mass is the physically meaningful choice.** At Pluto's Hill
radius the Pluto-Charon separation is a few tenths of a percent of the
distance involved, so the pair is gravitationally indistinguishable from
a point mass of M_Pluto + M_Charon at the barycentre. Using Pluto alone
describes a body that is not there.

Because r_H scales as mass^(1/3):

| System | Companion fraction | Effect on r_H |
|--------|------------------:|--------------:|
| Pluto-Charon | ~12% | **+3.9%** |
| Eris-Dysnomia | ~8.4% (ratio used in Nimmo & Brown 2023) | **+2.7%** |

For Pluto that is 5.756 Mkm against 5.981 Mkm -- and the code's caption
says 5.99, so the code already uses system mass, whether or not that was
deliberate.

**One trap before anyone applies a correction.** A mass derived from a
satellite's orbit is a **system** mass by construction, since the orbit
responds to the total. So a database value may already include the
companion, and adding it again double-counts. Check whether JPL SSD's
Eris mass of 1.66e22 kg is Eris alone or the Eris-Dysnomia system before
touching the Eris figure. I did not resolve this.

---

## Tony-action rollup

- **(do)** Keep both files. The earlier worksheet is the primary; this
  is an addendum.
- **(do)** When writing the Eris citation, use **Nimmo & Brown 2023**
  and record all four inputs including the 4.5e-12 W/kg heating rate.
- **(decide)** Recite Eris's differentiation claim to Nimmo & Brown 2023
  rather than Sicardy 2011. The ">85%" number remains unsourced either
  way.
- **(decide)** Whether the lunar core dimensions get recited to the LLR
  and GRAIL constraints above, which do support them, while the
  temperatures beside them are removed.
- **(do)** BL-3, BL-4, and BL-8 still need a checker who is not Claude.
  Two Claude passes have now declined all three.
- **(decide)** Whether the routing should record *which model* produced
  each leg, so a repeat pass by the same model cannot be mistaken for
  convergence. This near-miss is the argument for it.

---

*Prepared August 3, 2026 by Claude Opus 5. Not an independent leg -- see
the note at the top.*
