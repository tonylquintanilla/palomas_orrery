import sys
PATH = sys.argv[1] if len(sys.argv)>1 else "LEDGER_CONSOLIDATED.md"
t = open(PATH, encoding="utf-8").read()
def rep(old,new,n=1):
    global t
    assert t.count(old)==n, f"count {t.count(old)} != {n} for: {old[:55]!r}"
    t = t.replace(old,new)

# ---- L-008: spell out abbreviations + set last-update date (2026-06-21, per its Note)
rep("<!-- L:008 status:OPEN upd:- section:D.Movement flag: rice:2/2/50/2 -->",
    "<!-- L:008 status:OPEN upd:2026-06-21 section:D.Movement flag: rice:2/2/50/2 -->")
rep("- **v24 sec5 precision batch** (low-risk): Jupiter compressed/expanded MP\n"
    "  toggle; Earth MP/BS citation upgrade; per-body shock eccentricity.",
    "- **v24 sec5 precision batch** (low-risk): three magnetosphere/bow-shock\n"
    "  precision upgrades -- (1) a Jupiter toggle between its compressed (solar-max)\n"
    "  and expanded (solar-min) magnetopause standoff; (2) upgrade Earth's\n"
    "  magnetopause + bow-shock values to cited sources; (3) per-body bow-shock\n"
    "  eccentricity (body-specific shock shape, not a shared approximation).")

# ---- L-045: accept description + today's date
rep("<!-- L:045 status:OPEN upd:- section:D.Feature-B flag: rice:1/1/90/1 -->",
    "<!-- L:045 status:OPEN upd:2026-06-23 section:D.Feature-B flag: rice:1/1/90/1 -->")
rep("- **N14** ", "- **N14** ", 0) if False else None
rep("#### [L-045 | #N14] Miranda inclination tooltip\n"
    "<!-- L:045 status:OPEN upd:2026-06-23 section:D.Feature-B flag: rice:1/1/90/1 -->\n"
    "`[per chain]`\n"
    "**Tony:** need description. ",
    "#### [L-045 | #N14] Miranda inclination tooltip\n"
    "<!-- L:045 status:OPEN upd:2026-06-23 section:D.Feature-B flag: rice:1/1/90/1 -->\n"
    "- **Add/verify a hover tooltip on Miranda noting its orbital inclination**\n"
    "  (~4.3 deg, the highest among Uranus's major moons), so the visible tilt of its\n"
    "  orbit in the render is explained. Single-info-marker pattern; km + AU where\n"
    "  distances appear. `[per chain]`")

# ---- L-047: retire as undetermined (Tony 2026-06-23)
rep("<!-- L:047 status:OPEN upd:- section:D.Feature-C flag: rice:2/2/50/2 -->",
    "<!-- L:047 status:DONE upd:2026-06-23 section:D.Feature-C flag: rice:2/2/50/2 -->")
rep("**Tony:** this description is unclear. Need to update the rice rating. ",
    "**RETIRED (2026-06-23, Tony):** undetermined -- the N10 'note-composition refactor'\n"
    "scope was never recoverable. Closed as undetermined; if it matters it will resurface.\n"
    "**Gap:** none -- retired. (Move to section C on next housekeeping relocation.)")

# ---- L-048: close core (v4 gate passed); B5 -> L-067
rep("<!-- L:048 status:PENDING-GATE upd:2026-06-11 section:D.Feature-C flag: rice:3/3/50/3 -->",
    "<!-- L:048 status:DONE upd:2026-06-23 section:D.Feature-C flag: rice:3/3/50/3 -->")
rep("**Gap:** the v4 gate (L-004); then the remaining riders listed in-block.\n"
    "**Tony:** L-004 is done. need to discuss and clarify then update rice.  ",
    "**Gap:** none -- v4.1 gate (L-004) PASSED; the 21/51 animation core track is\n"
    "COMPLETE. O14/O15 verdicts closed via L-055. The lone remaining rider, B5\n"
    "(measure_animation_html file-browser dialog), is spun out to L-067. DONE; move to\n"
    "section C on next housekeeping relocation.")

# ---- L-025: plain-language clarification (Tony wants to understand it)
rep("**Tony:** unclear on the technical significance. I don't recall a mode 5 issue. ",
    "**Plain version:** a code-tidiness audit, NOT a render/Mode-5 issue. After the May\n"
    "sweep, simple sphere-shell info-markers all go through one factory; custom-geometry\n"
    "shells (rings, magnetospheres, belts) keep their markers inline because they need\n"
    "special positioning. This item just greps the *_visualization_shells.py files for any\n"
    "OLD inline-marker definitions left OUTSIDE a custom-geometry builder -- stragglers the\n"
    "sweep missed. None found -> close. (Deferred until run.)")

# ---- L-056: extract MAPS wiring to L-066; keep only the two non-visual residuals
rep("#### [L-056] Phase 4 residuals: stale O2/O3 console wording; apsidal_markers em-dashes; MAPS per-frame wiring deferred",
    "#### [L-056] Phase 4 residuals: stale O2/O3 console wording; apsidal_markers em-dashes (MAPS per-frame wiring -> L-066)")
rep("<!-- L:056 status:OPEN upd:2026-06-12 section:G flag: rice:1/2/50/2 -->",
    "<!-- L:056 status:OPEN upd:2026-06-23 section:G flag: rice:1/2/50/2 -->")
rep("  MAPS per-frame wiring DEFERRED per ADDENDUM_phase4 decision 1 (the\n"
    "  two-site exclusion warning and partition design are captured there).",
    "  MAPS per-frame wiring EXTRACTED to its own item L-066 (2026-06-23) -- it is real\n"
    "  scoped work (a one-line gate removal), NOT \"by design\"; see L-066.")
# remove the Scoping block (moves into L-066)
rep("**Scoping (2026-06-18):** MAPS per-frame wiring scoped in handoff v29.\n"
    "  The exclusion is one line (palomas_orrery.py L2324: `if name == 'MAPS':\n"
    "  continue`). The builder (build_comet_tail_traces) is shared with all\n"
    "  comets -- no MAPS-specific code needed. Prerequisite: review ADDENDUM_phase4\n"
    "  decision 1 to understand the two-site exclusion warning before removing\n"
    "  the gate. Main risk: frame-1 tail doubling (known pattern, known guard).\n"
    "  Static path (plot_objects L6062) already handles MAPS. O2/O3 wording and\n"
    "  apsidal em-dashes remain as separate sub-items.  \n", "")
rep("**Tony:** needs update. we worked on this. check mode 5. ",
    "**Note (2026-06-23):** MAPS wiring split out to L-066. L-056 now holds only the two\n"
    "non-visual residuals: O2/O3 console wording (one-line fix on next touch) and\n"
    "apsidal_markers.py em-dashes (-> platform-neutrality, L-027). No Mode-5 needed here.")

# ---- NEW L-066 (MAPS tail wiring): insert at end of section G, before ## H
L066 = """#### [L-066] MAPS per-frame comet-tail animation wiring
<!-- L:066 status:OPEN upd:2026-06-23 section:G flag: rice:2/3/75/1 -->
- **Wire MAPS into the per-frame comet-tail animation.** In ANIMATION mode the MAPS
  tail does NOT render at all (it renders in STATIC mode only) -- Tony, Mode-5,
  2026-06-23. Extracted from L-056. The earlier "non-animation BY DESIGN" notes
  (L-004 / L-011, now in C) recorded the Phase-4 DEFERRAL (ADDENDUM_phase4 decision
  1), NOT a permanent exclusion -- the wiring is wanted and was always scoped as
  deferred, not done. THE FIX (handoff v29 scoping): remove the one-line gate at
  palomas_orrery.py L2324 (`if name == 'MAPS': continue`). build_comet_tail_traces
  is shared with all comets -- NO MAPS-specific code needed. Static path
  (plot_objects L6062) already handles MAPS.
**Gap:** PREREQUISITE -- review ADDENDUM_phase4 decision 1 (two-site exclusion
warning + partition design) before removing the L2324 gate. Risk: frame-1 tail
doubling (known pattern, known guard; Tony reports it currently GONE -- verify it
stays gone). Mode-5 gate: MAPS tail animates per-frame like the other comets
(updates each frame), no frame-1 doubling, exclusion warning still correct.
**Ref:** extracted from L-056 (2026-06-23); ADDENDUM_phase4 decision 1; handoff v29;
palomas_orrery.py L2324 (gate) + L6062 (static path); build_comet_tail_traces;
prereqs ADDENDUM_phase4_decisions.md + HANDOFF_animation_phase4_brief.md.

"""
rep("## H. GALLERY / STUDIO TRACK", L066 + "## H. GALLERY / STUDIO TRACK")

# ---- NEW L-067 (B5): insert before L-049 (right after the closed L-048 block)
L067 = """#### [L-067] measure_animation_html.py file-browser dialog (B5)
<!-- L:067 status:OPEN upd:2026-06-23 section:D.Feature-C flag: rice:1/1/75/1 -->
- **Add a tkinter file-browser dialog to measure_animation_html.py (B5).** Spun out
  of L-048 on close (2026-06-23): the animation core track 21/51 is DONE (v4.1 gate,
  L-004), and B5 was the lone remaining rider -- a convenience dialog
  (filedialog.askopenfilename) to pick the HTML to measure instead of a hardcoded
  path. Small, isolated tooling.
**Gap:** add filedialog.askopenfilename to measure_animation_html.py.
**Ref:** spun out of L-048 (closed 2026-06-23).

"""
rep("#### [L-049 | #N8] Comet info-marker superposition cluster", L067 + "#### [L-049 | #N8] Comet info-marker superposition cluster")

# ---- invariants
assert all(ord(c)<128 for c in t), "non-ASCII introduced"
assert t.count("#### [L-066]")==1 and t.count("#### [L-067]")==1, "new item missing/dup"
assert "## H. GALLERY / STUDIO TRACK" in t
open(PATH,"w",encoding="utf-8").write(t)
print("OK patch3 applied")
