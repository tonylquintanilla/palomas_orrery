# Send-back: HAUMEA_RADIUS_KM, volumetric mean of which shape model

**Built on `66cf0cbcf298787542ae9b7bf335273d7ffa67d1` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Tony's ruling, 2026-08-15:** send Haumea back for sourcing. Recorded
here so it rides with the L-192 errand when the builder emits it. Lands
in `documentation/` -- a record, not a tool input.

---

## Why this one and not the other three

The convention is already settled and is not in question. Adopted
2026-04-16: equatorial radius for the major planets, **volumetric mean
for small and irregular bodies**, with Haumea named explicitly --
"extremely oblate; volumetric is the only sensible scalar." So the
equatorial figure of 870 km is out of scope, and this errand must not
reopen it.

What is unresolved is narrower. `constants_new.py` reads:

    HAUMEA_RADIUS_KM = 715
    # Source: JPL SSD mean radius (Lockwood et al. 2014)
    #         Highly ellipsoidal: 1050x840x537 km -> geometric mean 779.5 km
    #         JPL SSD publishes 715; equatorial 870

The value and the axes in its own comment do not agree. The geometric
mean of 1050, 840 and 537 is 779.5 km, not 715. Under the standing
convention the constant should be the volumetric mean of the shape
model the project has adopted, so one of those two lines is stale:
either the axes belong to a solution no longer in use, or 715 is not
the volumetric mean of the solution that is.

Both worksheets computed 779.5 in passing. Neither resolved it, because
both were answering whether 816 was right -- and 816 fails against
every candidate, so the question stopped there.

---

## The question to send

> `HAUMEA_RADIUS_KM` is a volumetric mean radius by project convention.
> Which published shape model should it come from, and what volumetric
> mean does that model give?
>
> Report the semi-axes, the derived volumetric mean, and the citation.
> If JPL SSD's 715 km and the semi-axes currently in the code comment
> come from different solutions, say which solution each belongs to.
> Do not recommend the equatorial radius; the project uses volumetric
> mean for small and irregular bodies by a settled convention.

Answer shape: one value, its semi-axes, one citation, and a statement
of which of the two current comment lines is superseded.

---

## What this is not

Not a DRIFTED finding. The 816 to 715 movement is a separate matter
handled by the L2b change of the same date. This errand exists because
715 and the axes printed beneath it cannot both be current, and no
worksheet has ever been asked which.

---

*Prepared August 15, 2026 with Anthropic's Claude Opus 5. Built on
`66cf0cbcf298787542ae9b7bf335273d7ffa67d1` at
https://github.com/tonylquintanilla/palomas_orrery.*
