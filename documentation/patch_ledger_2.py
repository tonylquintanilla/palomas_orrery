import sys, re
PATH = sys.argv[1] if len(sys.argv)>1 else "LEDGER_CONSOLIDATED.md"
t = open(PATH, encoding="utf-8").read()
def rep(old, new, n=1):
    assert t.count(old)==n, f"count {t.count(old)} != {n} for: {old[:60]!r}"
    return t.replace(old, new)

# A) clear L-006 dipole directive note (resolved: implementation done, code-verified)
t = rep("  **Tony:** let's prioritize the dipole implementation for Mercury, Earth and Jupiter and clean these up. \n", "")

# B) L-009 note -> DONE stamp (the body text above is the stale June-13 state)
t = rep("**Tony:** as mentioned above, let's prioritize cleaning up the remaining dipoles and cones.",
        "**DONE (2026-06-22, verified in code @26e58b2):** all six magnetosphere bodies carry a\n"
        "SOURCED dipole_cone in CUSTOM_SHELLS (Mercury, Earth, Jupiter, Saturn, Uranus, Neptune);\n"
        "implementation + provenance gate cleared. The body text above is the June-13 state, now\n"
        "superseded. Only the rolling-cone coupling remains -- tracked as L-061.")

# C) L-026 note (3 lines) -> platform-neutrality framing
t = rep("**Tony:** this should be part of a general sweep of the code base for LF conversion. \n"
        "this is a maintenance item to keep the codebase platform neutral, which is the larger goal\n"
        "and should be stated clearly. ",
        "**Platform neutrality (the larger goal):** part of a general codebase LF-conversion sweep;\n"
        "keeps the project platform-neutral across Windows / macOS / Linux. Pairs with L-027.")

# D) L-027 note -> cross-link to L-026
t = rep("**Tony:** this has the same purpose as L-026. ",
        "**Platform neutrality:** same goal as L-026 (the LF sweep) -- pair them. This is the Tk\n"
        "color-name half (SystemButtonFace -> hex literal / sys.platform detection / ttk).")

# E) L-058 note -> link to L-046
m = re.search(r"\*\*Tony:\*\* this connects to another item on the studio preset generator refactor. ", t)
assert m, "L-058 studio-preset note not found"
t = t.replace(m.group(0), "**Linked:** coupled to L-046 (encounter generator -> preset-authoring skill).")

# F) move B. STRATEGIC STATUS into section C as a closed record; drop the orphan note
lines = t.split("\n")
b = lines.index("## B. STRATEGIC STATUS")
chdr = "## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)"
c = lines.index(chdr)
note = "**Tony:** This item does not have an L-number or header and should be closed and moved to C."
bsec = lines[b:c]
assert note in bsec
moved = [l for l in bsec if l not in ("## B. STRATEGIC STATUS", note, "---")]
while moved and moved[0]=="": moved.pop(0)
while moved and moved[-1]=="": moved.pop()
lines = lines[:b] + lines[c:]
ci = lines.index(chdr) + 1
if ci < len(lines) and lines[ci]=="": ci += 1
header = [
  "### Strategic status -- shell-consolidation + animation refactor (CLOSED, for the record)",
  "(Moved from B. Strategic Status, 2026-06-22; no L-number, historical record. The animation",
  '"final gate pending" noted below PASSED at L-004 / v4.1, June 17.)',
  "",
]
lines = lines[:ci] + header + moved + ["", "---", ""] + lines[ci:]
t = "\n".join(lines)

assert all(ord(ch)<128 for ch in t), "non-ASCII introduced"
assert t.count("## B. STRATEGIC STATUS")==0, "B header still present"
assert t.count("### Strategic status -- shell-consolidation")==1, "moved block missing/dup"
open(PATH,"w",encoding="utf-8").write(t)
print("OK: dipole notes cleared + L-009 stamped; L-026/L-027 platform-neutrality; L-058->L-046; Strategic Status moved to C")
