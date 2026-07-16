# F1 Build Manifest -- Comparative Review (Fable v1 vs GPT v0.1)

**Type:** REVIEW (Claude Sonnet 5, independent verification pass against
live HEAD -- not a design session, not a manifest)
**Reviewed:** `PHASE2_F1_BUILD_MANIFEST_v1.md` (Fable) and
`gpt_PHASE2_F1_BUILD_MANIFEST_v0.1.md` (GPT), both against orrery HEAD
`58dfa5205d492711d6163560d8c3fa15f6c60b9c` and gallery HEAD
`953c650edc8dbd35ab11ec1720f8283987d63901` -- both re-verified live via
`git ls-remote` before this review, not assumed from either manifest's
own header.
**Bottom line:** Fable's manifest catches a real, verified, high-impact
bug that GPT's manifest would have shipped silently. GPT's manifest is
closer on one settled-but-unreachable schema detail and stronger on
explicit stop-conditions. Neither should go to Opus as-is; see
Recommendation.

---

## 1. The headline finding: FLAG-2 is real, verified, and GPT's manifest misses it entirely

Fable's manifest flags that `propagate_marker` (`gallery/assembler/
render_orbits.py` line 87) derives mean motion as `n = K_GAUSS / a**1.5`,
where `K_GAUSS = sqrt(GM_sun)`. That is correct for heliocentric bodies
but wrong by ~3 orders of magnitude for planetocentric elements (the four
moon-category objects: moon, io, titan, charon).

**I checked this directly against live source, not Fable's word.** Cloned
the gallery repo fresh (`953c650e`), read `render_orbits.py` lines 39 and
81-90:

```python
K_GAUSS = 0.01720209895  # sqrt(GM_sun) in AU**1.5 / day
...
n = K_GAUSS / (a ** 1.5)                       # rad/day
```

Ran the arithmetic myself for the Moon (a ~ 0.00257 AU):
`n_wrong = 0.01720209895 / (0.00257)**1.5 ~= 132 rad/day` ->
`period_wrong = 2*pi / n_wrong ~= 0.0476 days ~= 68.5 minutes`.

That matches Fable's claimed figure (~68 min vs. the real 27.3-day
sidereal month) almost exactly. **This is a real, verified bug.** If
Opus builds the trust measurement by reusing `propagate_marker` (or its
underlying math) directly for the moon-category objects, every moon's
measured error rate would be computed against a wrong ellipse and the
served `trust` blocks for moon/io/titan/charon would be garbage --
silently, because nothing in the pipeline would raise an error.

**GPT's manifest does not mention this anywhere.** Section B1 says
"Import from it [`render_orbits.py`] if dependency direction and import
safety are acceptable" -- i.e., it expects direct reuse of the existing
propagation math with no caveat about planetocentric bodies. Section B2's
functional decomposition (`propagate_two_body(elements, delta_days) ->
predicted position`) has no parameter or note distinguishing heliocentric
from planetocentric mean-motion sources. If Opus had built from GPT's
manifest alone, the four moon trust blocks would ship wrong, and nothing
in GPT's own test list (B9) would catch it, since the tests are written
against the same (uncorrected) assumption.

This is the single most important reason not to hand Opus GPT's manifest
as-is, and the single strongest argument for Fable's manifest as the
technical base. Fable's own framing of this as "the real catch of this
pass" is not overstatement -- I'd call it the entire value of having run
a second, independent pass.

---

## 2. FLAG-1 (schema naming): resolvable now -- I have what neither AI could reach

Fable flagged that the "unchanged from v0.1" schema reference in the
handoff's SS4 is unreachable, since v0.1-v0.3 aren't in either repo or
the upload set, and proposed its own schema from first principles. GPT
didn't flag this as uncertain at all -- it just asserted a schema.

**I have v0.1 and v0.2 in this session's working files (written before
the handoff was consolidated to v0.4).** The actual settled decision,
from v0.2 Section 2 (Tony's direct correction, mid-session, after v0.1's
first-draft naming was rejected):

> **Config field naming (unchanged):** mirrors the orrery's own dict
> shapes exactly -- `atmosphere`/`upper_atmosphere` (not "lower"/
> "upper"), `inner_belt_distance`/`outer_belt_distance`/`belt_thickness`
> (no invented unit suffix), `*_km` ring keys copied near-verbatim from
> `jupiter_visualization_shells.py`'s own `ring_params` dict. The
> units-by-comment convention doesn't survive into JSON; noted in prose
> here rather than invented as a schema field.

I also re-checked `jupiter_visualization_shells.py` lines 898-935 (the
actual `ring_params` dict) to confirm the ring key names directly:
`inner_radius_km`, `outer_radius_km`, `thickness_km`, `color`, `opacity`,
`name`, `description`, nested under snake_case ring slugs
(`main_ring`, `halo_ring`, `amalthea_gossamer`, ...).

**How the two manifests measure up against the actual settled
convention:**

| Field | Settled (v0.2, confirmed) | Fable's guess | GPT's guess |
|---|---|---|---|
| Belt distances | `inner_belt_distance`, `outer_belt_distance`, `belt_thickness` -- no suffix | `distance_rp` (invented suffix, inside a generic `components` list) | `inner_belt_distance`, `outer_belt_distance`, `belt_thickness` -- exact match |
| Atmosphere | `atmosphere`/`upper_atmosphere` as the shape, not "lower"/"upper" | `components: [{"name": "Lower Atmosphere"}, {"name": "Upper Atmosphere"}]` | `layers: [{"name": "lower_atmosphere"}, {"name": "upper_atmosphere"}]` -- closer, still not the literal settled shape |
| Ring keys | `*_km`, copied near-verbatim from `ring_params` | `inner_radius_km`/`outer_radius_km`/`thickness_km` -- matches | `inner_radius_km`/`outer_radius_km`/`thickness_km` -- matches |

**Neither manifest exactly reproduces the settled schema** (both
introduce a generic `kind`/`type` + list-of-components/layers
abstraction that the settled decision's "mirrors the orrery's own dict
shapes exactly" language doesn't really support), **but GPT's field-name
choices for the belt distances are an exact match to what was actually
decided, and Fable's `_rp` suffix is precisely the kind of invented unit
suffix Tony rejected earlier in this same design round.** This is a
concrete, checkable deviation in Fable's manifest, not a style
preference.

**Recommendation:** Section 4.1 in whichever manifest goes to Opus needs
to be rewritten to actually use `atmosphere`/`upper_atmosphere`,
`inner_belt_distance`/`outer_belt_distance`/`belt_thickness` with no
suffix, ring keys verbatim from `ring_params`. Ring naming is already
correct in both manifests and can stay as-is.

---

## 3. A new disagreement this review surfaced: partial-measurement-failure semantics

Fable's FLAG-3: if **any** non-moon, non-spacecraft participant's trust
measurement fails during a build, the global `served_window` is served
as `null` (unenforced, with a warning) rather than computed from
whichever objects succeeded -- "a minimum over an incomplete set is not
conservative; the missing object could be the binding one."

GPT's B7: computes the minimum over whichever participants have a
**successful** measurement, and only fails the entire build if **zero**
qualifying objects succeed. A single participant's failure (say Saturn's
check-vector fetch flakes one night) does not null the window -- it's
silently excluded from the minimum, and the window is computed from the
remaining six.

**These are genuinely different behaviors on a load-bearing question,
not a wording difference.** I checked `resolver.py` (lines 91-106)
directly: `served_window: null` is an explicitly supported, graceful
state already built into the consumer -- it warns and treats the bound
as unenforced, which is exactly the same disposition the project already
uses elsewhere for "we don't have this yet." A wrong-but-present numeric
bound, by contrast, is indistinguishable from a correct one to the
resolver -- it will enforce whatever it's given. Given the project's own
running principle (conservative honesty over silent optimism -- the same
instinct behind "Show the Envelope of the Unknowable" and the
Fetched-vs-Recalled discipline), Fable's "any failure -> null" reads as
the safer default: a null night is visibly degraded; a survivors-only
minimum that happens to be wrong is invisible.

That said, this is a genuine judgment call neither the original design
handoff nor SS6.4 settled (SS6.4 only says which *categories* are
excluded from the minimum, not what happens on a *measurement failure*
for a participating object) -- both AIs made an implementation-latitude
decision here, and they made different ones. Worth your explicit call
rather than me picking silently.

---

## 4. Other comparative notes

**Verification grounding.** Fable did the re-pin and code verification
live this session (`git ls-remote`, direct reads) and tagged every claim
`[verified @HEAD]`. GPT was explicit that its execution environment's
GitHub network access failed, and rather than fabricate verification, it
restructured the manifest so the implementer (Opus) performs the pin/
verify/relocate-symbols step as a mandatory first gate (Section 1). This
is honest, correct behavior on GPT's part -- no cite-to-clear violation --
but it does mean GPT's manifest is a step further from "ready," since
none of its own numeric claims have actually been re-checked by anyone
yet (its "trust" JSON examples are explicitly `0.0` placeholders, not
illustrative real numbers the way Fable's are).

**Stop-condition and reporting rigor.** GPT's manifest is more exhaustive
here: Section 5's stop-condition list and Section 4's required
implementation-report structure are more explicit and complete than
Fable's equivalent (Fable has strong per-flag callouts but no single
consolidated stop-condition list or report template). This is a real
strength worth carrying into whatever goes to Opus regardless of which
manifest wins on the technical merits.

**Scope discipline.** Both correctly leave `resolver.py`/`cache_reader.py`
untouched, both correctly keep Apophis to a normal (non-anchored) trust
measurement this pass, both correctly exclude the UX/envelope work,
`event_link`, info-card, and sun-oriented features. No scope leakage in
either.

**Structural style.** Fable's manifest reads as narrative-plus-code
(prose explaining the "why," pinned semantics called out as flags against
the handoff). GPT's reads as a stricter, more legalistic contract
(numbered musts, explicit "do not X" per section, a functional
decomposition sketch for M2). Both are usable shapes; the difference is
tone/rigor, not correctness, except where noted above.

---

## Recommendation

Don't hand Opus either manifest as-is. The needed reconciliation is
small and concrete:

1. Take Fable's manifest as the base (it's live-verified, it caught
   FLAG-2, and its `trust` schema and measurement design are more
   fully worked out).
2. Fix FLAG-2 in -- already done, it's the strongest part of Fable's
   pass.
3. Rewrite section 4.1 (M1 schema) using the actual settled field names
   above -- neither AI's guess as given.
4. Get your explicit call on section 3's partial-failure question
   (null-on-any-failure vs. compute-from-survivors) -- I'd lean toward
   Fable's null-on-any-failure, for the reasons in section 3 above, but
   it's a real decision, not a formality.
5. Graft GPT's stop-condition list and implementation-report template
   into the reconciled manifest -- genuine process improvement, no
   conflict with Fable's content.

I can produce that reconciled v2 manifest directly if you want it --
it's mechanical at this point, not a new design question. Let me know
whether you want me to build it, or want to run the partial-failure
question past Fable/GPT again first.

---
Review written July 2026 with Anthropic's Claude Sonnet 5.
