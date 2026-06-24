import sys
PATH = sys.argv[1] if len(sys.argv)>1 else "LEDGER_CONSOLIDATED.md"
t = open(PATH, encoding="utf-8").read()
def rep(old,new,n=1):
    global t
    assert t.count(old)==n, f"count {t.count(old)} != {n} for: {old[:55]!r}"
    t = t.replace(old,new)

L068 = """#### [L-068] Static/animation pipeline consolidation -- remaining residuals (umbrella)
<!-- L:068 status:OPEN upd:2026-06-23 section:D.Structural flag: rice:2/2/75/2 -->
- **Umbrella thread for the remaining practical consolidation of the static
  (plot_objects) and animation (animate_objects) pipelines.** The big structural
  unification is DONE -- see section C ("shell-consolidation + animation refactor")
  and the Consolidation Log (F): scene-assembly unified, the three animation
  pipelines merged, explicit blocks deleted in both pipelines, one unified dispatch.
  What remains is distributed across three discrete residuals, tracked here as one
  thread:
    - L-066 -- behavioral parity gap: MAPS tail renders in the static path but not
      the animation path (one-line L2324 gate). The "make the two paths agree" task.
    - L-016 -- cleanup: grep-confirm zero callers across both pipelines, then delete
      the dead duplicate shell-function bodies the unification left behind.
    - L-014 -- the one render path still OUTSIDE the unified dispatch (the four
      asteroid belts via standalone create_main_asteroid_belt()); fold into
      CUSTOM_SHELLS or keep standalone (design call).
  This item is also the HOME for any NEW static/animation parity gap. The standing
  "fix both pipelines or neither" rule is a PRACTICE, not a backlog item, so new
  gaps surface only when caught by eye (the way MAPS/L-066 did) -- when one appears,
  log it here as a sibling of L-066.
**Gap:** none of its own -- this thread closes when L-066, L-016, and L-014 all
close AND no parity gap is outstanding. Tracking/umbrella item.
**Ref:** L-066, L-016, L-014; section C strategic-status block; Consolidation Log (F);
protocol Part 3 "Check All Parallel Pipelines".

"""
# insert L-068 after L-016 block (before L-020), inside D.Structural
rep("#### [L-020 | #26] CUSTOM_SHELLS tooltip verification",
    L068 + "#### [L-020 | #26] CUSTOM_SHELLS tooltip verification")

# back-pointers from the three children
rep("**Ref:** planet_visualization.py L558, L293, L306; neptune_visualization_shells.py.",
    "**Ref:** planet_visualization.py L558, L293, L306; neptune_visualization_shells.py. (umbrella: L-068)")
rep("prereqs ADDENDUM_phase4_decisions.md + HANDOFF_animation_phase4_brief.md.",
    "prereqs ADDENDUM_phase4_decisions.md + HANDOFF_animation_phase4_brief.md. (umbrella: L-068)")
rep("convention. Low urgency; no bug, no user-visible gap.",
    "convention. Low urgency; no bug, no user-visible gap. (umbrella: L-068)")

assert all(ord(c)<128 for c in t), "non-ASCII"
assert t.count("#### [L-068]")==1
assert t.count("(umbrella: L-068)")==3, "back-pointer count"
open(PATH,"w",encoding="utf-8").write(t)
print("OK patch5 applied")
