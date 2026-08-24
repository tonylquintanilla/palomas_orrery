"""
patch_L154_3_ledger_close_and_findings.py -- close L-154 and record the two
findings the build surfaced.

REPO: tonylquintanilla/palomas_orrery (the ORRERY repo).
Built on 2e40a1ebc3f24b02bc3dc57eeb7f652e61e10be2 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Companion gallery SHA: 099a85368ce7f467f88a35a65e0580dd97261b37, which is
where all the code this entry describes actually lives.

THREE EDITS to LEDGER_CONSOLIDATED.md:

1. L-154 OPEN -> DONE. Both halves shipped 2026-08-24 and Mode 5 passed.
   The old 2026-07-29 sequencing note is NOT deleted -- it is annotated as
   superseded by the braid, because the record of a ruling that was later
   changed is worth more than a tidy entry.

2. L-231 opened: the radiation belts are drawn in the ecliptic plane and
   the comment claiming the rotational axis records an UNBUILT intent --
   the magnetic dipole tilt. Tony's clarification of 2026-08-24, which
   corrected Claude's first reading of it as an L-229-class defect.

3. L-232 opened: `data/objects_config.json` now carries MEASURED values
   with source lines, in a store no checker reads, and Earth's radius
   appears in it twice.

Both new entries carry a proposed RICE tagged `**Note:**` so neither reads
as a ruling. Re-run `ledger_index.py` after this patch: the INDEX zone is
generated and this patch deliberately does not touch it.

Written August 2026 with Anthropic's Claude Opus 5 (L-154).
"""

import hashlib
import os

LEDGER = "LEDGER_CONSOLIDATED.md"
EXPECT_MD5 = "d1270a92ca3d613df344afb32be5fe94"


def norm(data):
    return data.replace(b"\r\n", b"\n")


def md5(data):
    return hashlib.md5(norm(data)).hexdigest()


EDITS = [
    # --- 1. L-154 status line -------------------------------------------
    (
        "<!-- L:154 status:OPEN upd:2026-08-23 section:W.Active flag: rice:3/3/70/3 -->",
        "<!-- L:154 status:DONE upd:2026-08-24 section:W.Done flag: rice:3/3/70/3 -->\n"
        "- **DONE 2026-08-24. Both halves shipped and Mode 5 passed.** The\n"
        "  close block is at the end of this entry; everything above it is the\n"
        "  record of the item while it was open, left as written.",
    ),
    # --- 2. L-154 close block, before the Ref line ----------------------
    (
        """**Ref:** `assemble.py`, `resolver.py`, `render_objects.py`, `presentation.py`;
`data/solar-system/feature_configs.json`; `data/objects_config.json`;
`documentation/HANDOFF_gallery_feature_layer_L154_resume.md`;""",
        """**SUPERSEDED, and the supersession is the point.** The 2026-07-29 note
above makes this item wait on the whole provenance cluster. Tony's braid
ruling of 2026-08-22 replaced that: provenance stops being a GATE and
becomes a per-artifact slice, and this item moves to the FRONT of the
order rather than the back. The note is kept because a ruling that was
later changed is part of the record; it is no longer in force.

**CLOSE BLOCK -- 2026-08-24.**
- **First half, gallery `8ec4f261` (2026-08-23).** `resolver.py` kept the
  feature mapping instead of reducing it to a tuple of category names, and
  populated `FeatureRequest.params`. The field had been declared in
  `models.py` and emitted by `assemble.py` since the beginning and had
  never been filled: the pipe was built, wired, and shipping empty dicts.
- **Second half, gallery `099a8536` (2026-08-24)**, via
  `patch_L154_2_feature_render_layer.py`. `gallery/feature_renderers.js`
  (536 lines) draws ring systems, radiation belts and atmosphere shells
  from the report; `gallery/solar_system_earth_test2.html` gained a scene
  selector, a `Frame on` axis control, and the call into the renderers.
- **Two render inputs were missing from the served cache and were added
  to `data/objects_config.json`** under Tony's ruling of 2026-08-24
  (option (a) of three: put the copy in the store the project already
  watches, not in a JavaScript table nothing scans). The IAU pole for
  Jupiter and Saturn as a new `orientation` feature key, and
  `planet_radius` on the three feature nodes whose numbers are expressed
  in multiples of it. See L-232.
- **Earth deliberately gained NO new feature key.** The L-080 fingerprint
  hashes the sorted set of feature keys, so a third key on Earth would
  have broken Artifact 1's lock -- for a rotation the orrery does not
  apply to Earth's belts in the first place (L-231). The patch asserts
  Earth's key list rather than trusting the reasoning.
- **Measured, not asserted.** Ring plane normals fitted from three drawn
  points by cross product, independent of the renderer's own basis
  function: Saturn 28.049 deg from the ecliptic, Jupiter 2.222 deg, both
  matching `idealized_orbits.py`'s pole table and obliquity rotation
  computed separately. A Ring inner/outer radii read back off the drawn
  points at 122,340 and 136,800 km. Jupiter's inner belt at 1.750 R_J.
  Earth's lower atmosphere at 1.0500 R_E.
- **28.05 deg is correct and is not 26.73.** The familiar figure is
  Saturn's tilt against its own ORBIT; these plots are ecliptic-framed.
  Recorded here because a future Mode 5 will otherwise flag a correct
  render as wrong.
- **Mode 5 PASSED 2026-08-24** (Tony), on Earth alone, Jupiter + Saturn
  whole-scene, and framed on each of Jupiter and Saturn. Browser trace
  counts matched the offline harness exactly -- 8 traces from 2 requests
  for Earth, 28 from 5 for Jupiter + Saturn -- and the framing half-spans
  agreed to three figures (Jupiter 0.00358 AU, Saturn 0.00384 AU, Earth
  0.000243 AU).
- **Artifact 1's lock was verified IN THE BROWSER**, not only in Python:
  `abbd01094852b57f` recomputed through Pyodide against the rebuilt cache.
  That is a stronger check than the container test, because it proves the
  browser path produces the same scene spec.
- **One visual oddity, checked and NOT a defect.** Saturn's seven ring
  info markers fall along one ray at increasing radii, because each sits
  at the first point of its own ring. `create_saturn_ring_system` does
  exactly the same thing, and the comment there records that the May 2026
  Neptune 2C fix was specifically to stop them collapsing onto one
  another. Scene-equivalent. Changing it is a change to both instruments.
- **Not done here, and next:** Artifact 2's thirty-number provenance
  slice, then the lock (segment 4), then the page (segment 5). The
  renderers draw from numbers that are not yet sourced, which v19 allows
  explicitly -- drawing is not locking.
- **Patches:** `patch_L154_1_resolver_feature_params.py`,
  `patch_L154_2_feature_render_layer.py`, both archived to
  `documentation/` in the GALLERY repo. Smoke tests
  `smoke_features.js` (23 checks) and `smoke_framing.js` (12 checks)
  archived beside them; they run under Node, which is outside Tony's
  working set, so they are session evidence rather than a routine gate.
  Where a runnable home for them belongs is open.

**Ref:** `assemble.py`, `resolver.py`, `render_objects.py`, `presentation.py`;
`gallery/feature_renderers.js`; `gallery/solar_system_earth_test2.html`;
`data/solar-system/feature_configs.json`; `data/objects_config.json`;
`documentation/HANDOFF_gallery_feature_layer_L154_resume.md`;""",
    ),
    # --- 3. Two new entries at the end of section A ----------------------
    (
        """  Skills Change Log; L-188 (the maintenance runner); L-226, L-227 (the
  two bumps whose absence from the history exposed this).

## PENDING ACTION (Tony-side)""",
        """  Skills Change Log; L-188 (the maintenance runner); L-226, L-227 (the
  two bumps whose absence from the history exposed this).

#### [L-231] Radiation belts are drawn in the ecliptic; the magnetic tilt is an unbuilt intent
<!-- L:231 status:OPEN upd:2026-08-24 section:A flag: rice:2/2/90/2 -->
- **Found while porting the belts to the gallery, 2026-08-24, and the
  first reading of it was WRONG.** Claude reported it as L-229's defect
  class in two more places: `create_earth_radiation_belts` and Jupiter's
  belt builder each construct their points in the ecliptic XY plane with
  a `sin(2*theta)` vertical wobble and never call
  `orient_to_planet_pole`, while each carries a comment saying the belt
  is built around the planet's rotational axis.
- **Tony's correction, same day.** The comment is not a false claim about
  what the code does. It records an intent that was never built -- adding
  the small magnetic axial tilt these planets actually have. So this is
  an unbuilt feature with a breadcrumb, not a frame error.
- **Why the distinction matters and is not pedantry.** L-229 is a
  MISTAKE: the streamer band's own docstring said body frame and the
  caller rotated nothing, so the render contradicted the data. This is a
  PLACEHOLDER: the current drawing is a defensible approximation and the
  comment marks where the refinement goes. Filing the second as the first
  would have put a correct-enough render into a defect queue.
- **The right rotation is not the pole.** Belts follow the MAGNETIC
  dipole, so the eventual transform is the dipole tilt applied on top of
  the spin pole, not the spin pole alone. Approximate magnitudes: Earth
  about 11 deg from the rotation axis, Jupiter about 10 deg, Saturn under
  0.1 deg -- which is why Saturn is the one body where using the pole
  alone (as `saturn_visualization_shells.py` already does) is very nearly
  right. Those figures are orientation for a future design round, NOT
  citable values; sourcing them is part of the build.
- **Scope, when built: BOTH instruments.** The gallery's
  `feature_renderers.js` deliberately matches the orrery here -- scene
  equivalence -- so a change to the orrery's belt orientation must be
  carried to the renderer in the same pass or the two will disagree.
  The renderer already receives `orientation` for Jupiter and consumes it
  only for rings.
- **Note:** RICE 2/2/90/2 -> 1.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, then re-run
  `ledger_index.py`.
- **Ref:** `earth_visualization_shells.py` (belt builder);
  `jupiter_visualization_shells.py` (belt builder);
  `saturn_visualization_shells.py` (belts DO use the pole);
  `idealized_orbits.py::orient_to_planet_pole`; gallery
  `gallery/feature_renderers.js::renderBelts`; L-229 (the genuine frame
  defect this was mistaken for); L-154.

#### [L-232] The gallery's served constants carry sources that nothing checks
<!-- L:232 status:OPEN upd:2026-08-24 section:A flag: rice:3/3/85/2 -->
- **Opened 2026-08-24, as a consequence of Tony's option-(a) ruling.**
  Two render inputs the served cache lacked were added to the gallery's
  `data/objects_config.json`: the IAU pole for Jupiter and Saturn, and
  `planet_radius` for Earth and Jupiter. Both are MEASURED values, both
  carry a `source` field and an `orrery_constant` field naming where they
  were copied from.
- **They are the FIRST `source` fields in that file**, and they sit in a
  store no checker reads. `provenance_scanner.py` scans Python. The
  worksheet checker scans Python. Nothing reads JSON in the gallery repo.
  So a source line there is a claim with no gate behind it -- exactly the
  shape the resident gate warns about, one repo over.
- **The value was still worth adding.** The alternative on the table was
  a JavaScript table, which is a store the transport does not target
  either AND is invisible to the pinning design. Putting the copy where
  segment 2 will land is the version that converges.
- **Earth's radius now appears TWICE in that file**, once in
  `atmosphere_shell` and once in `van_allen_belts`, because a shared
  sibling would have meant a third top-level feature key on Earth and
  L-080's fingerprint hashes that list. The duplication is deliberate and
  is the transport's to collapse, not a hand edit's.
- **Not a blocker for Artifact 2.** The artifact's thirty measured
  numbers are the ring and belt values, which live in the orrery and are
  in the audit already. These five are drawing inputs that arrived with
  their sources attached on the day they were written, which is the
  strongest position a value ever occupies -- the risk is drift later,
  not error now.
- **Two candidate shapes, neither designed:** teach the worksheet
  checker to read `objects_config.json` as a second corpus, or make the
  transport (segment 2) verify each `orrery_constant` pointer resolves
  and matches. The second is better if it lands, because it fixes the
  producer.
- **Note:** RICE 3/3/85/2 -> 3.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, then re-run
  `ledger_index.py`.
- **Ref:** gallery `data/objects_config.json`;
  `provenance_scanner.py`; `worksheet_keys.py`; L-155 (pinning);
  L-181 (single home for feature constants); L-154; master plan
  Section 7 decisions 12 and 18.

## PENDING ACTION (Tony-side)""",
    ),
]


def main():
    if not os.path.exists(LEDGER):
        raise SystemExit(
            "ABORT: %s not found. Run this from the ROOT of the ORRERY repo "
            "(palomas_orrery)." % LEDGER
        )

    with open(__file__, "rb") as fh:
        if any(b > 127 for b in fh.read()):
            raise SystemExit("ABORT: this script carries non-ASCII bytes.")

    with open(LEDGER, "rb") as fh:
        original = fh.read()
    got = md5(original)
    if got != EXPECT_MD5:
        raise SystemExit(
            "ABORT: %s fingerprint mismatch.\n  expected %s\n  got      %s\n"
            "The ledger is not the one this patch was built against."
            % (LEDGER, EXPECT_MD5, got)
        )

    text = original.decode("utf-8")
    before_nonascii = sum(1 for ch in text if ord(ch) > 127)

    for i, (old, new) in enumerate(EDITS, start=1):
        n = text.count(old)
        if n != 1:
            raise SystemExit(
                "ABORT edit %d: anchor matched %d times, expected exactly 1.\n"
                "First 70 chars: %r" % (i, n, old[:70])
            )
        text = text.replace(old, new)

    after_nonascii = sum(1 for ch in text if ord(ch) > 127)
    if after_nonascii > before_nonascii:
        raise SystemExit(
            "ABORT: non-ASCII count rose %d -> %d; inserted text must be ASCII."
            % (before_nonascii, after_nonascii)
        )

    # Content assertions -- each can fail.
    if text.count("<!-- L:231 ") != 1 or text.count("<!-- L:232 ") != 1:
        raise SystemExit("ABORT: the two new status lines did not land once each.")
    if "<!-- L:154 status:OPEN" in text:
        raise SystemExit("ABORT: L-154 still reads OPEN.")
    if text.count("<!-- L:154 status:DONE") != 1:
        raise SystemExit("ABORT: L-154's DONE line did not land exactly once.")
    # The generated INDEX zone must be untouched -- ledger_index.py owns it.
    start = original.decode("utf-8").index("<!-- INDEX:START")
    end = original.decode("utf-8").index("<!-- INDEX:END")
    if original.decode("utf-8")[start:end] not in text:
        raise SystemExit(
            "ABORT: the generated INDEX zone changed. This patch must not "
            "touch it; ledger_index.py regenerates it."
        )

    with open(LEDGER, "wb") as fh:
        fh.write(text.encode("utf-8"))

    with open(LEDGER, "rb") as fh:
        on_disk = fh.read()
    if md5(on_disk) == EXPECT_MD5:
        raise SystemExit("ABORT: the ledger still fingerprints as the pre-edit "
                         "file. The write did not land.")
    disk_text = on_disk.decode("utf-8")
    for probe in ("[L-231]", "[L-232]", "Mode 5 PASSED 2026-08-24",
                  "abbd01094852b57f"):
        if probe not in disk_text:
            raise SystemExit("ABORT: %r missing from the ledger on disk." % probe)

    print("PATCH L-154_3 APPLIED")
    print("  %s: %d edits, %d bytes, %d lines"
          % (LEDGER, len(EDITS), len(on_disk), disk_text.count("\n") + 1))
    print("  non-ASCII %d -> %d" % (before_nonascii, after_nonascii))
    print("  L-154 -> DONE; L-231 and L-232 opened (section A)")
    print("  INDEX zone untouched, as it must be")
    print("")
    print("NEXT:")
    print("  1. python ledger_index.py     (regenerates the INDEX zone)")
    print("     It WILL report one [auto-fix] line for L-154 -- moving the")
    print("     closed block physically into the W.Done heading. Expected.")
    print("  2. Confirm or redirect the two proposed RICE scores, then")
    print("     re-run ledger_index.py again if you change either.")
    print("  3. Archive this script to documentation/.")


if __name__ == "__main__":
    main()
