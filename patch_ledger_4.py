import sys
PATH = sys.argv[1] if len(sys.argv)>1 else "LEDGER_CONSOLIDATED.md"
lines = open(PATH, encoding="utf-8").read().split("\n")
nL0 = sum(1 for l in lines if l.startswith("#### [L-"))

def edit_block(hdr, meta_old, meta_new, note_old, note_new):
    i = lines.index(hdr)
    assert lines[i+1]==meta_old, f"meta drift at {hdr[:30]}"
    lines[i+1]=meta_new
    for j in range(i, i+10):
        if lines[j]==note_old:
            lines[j]=note_new
            return
    raise AssertionError(f"note not found for {hdr[:30]}")

# L-049 close (Mode-5 confirmed: markers no longer superimposed)
edit_block("#### [L-049 | #N8] Comet info-marker superposition cluster",
    "<!-- L:049 status:PARKED upd:- section:D.Parked flag: rice:1/2/50/2 -->",
    "<!-- L:049 status:DONE upd:2026-06-23 section:D.Parked flag: rice:1/2/50/2 -->",
    "**Tony:** need to verify mode 5. ",
    "**Mode-5 confirmed (2026-06-23, Tony):** comet info-markers no longer superimposed. DONE; move to C on next housekeeping.")

# L-050 retire (undetermined)
edit_block("#### [L-050 | #N9] white -> red orbit-marker switch (osculating marker intentionally stays white)",
    "<!-- L:050 status:PARKED upd:- section:D.Parked flag: rice:2/1/50/1 -->",
    "<!-- L:050 status:DONE upd:2026-06-23 section:D.Parked flag: rice:2/1/50/1 -->",
    "**Tony:** need to verify mode 5. ",
    "**RETIRED (2026-06-23, Tony):** undetermined -- no recollection of an orbit-color problem. Closed as undetermined; will resurface if real.")

# Move L-066 from section G (OPEN QUESTIONS) into D.Feature-A (near-term open work)
s = lines.index("#### [L-066] MAPS per-frame comet-tail animation wiring")
h = lines.index("## H. GALLERY / STUDIO TRACK (website repo; low-activity)")
block = lines[s:h]
while block and block[-1]=="": block.pop()        # drop trailing blanks
block = [l.replace("section:G", "section:D.Feature-A") if l.startswith("<!-- L:066 ") else l for l in block]
del lines[s:h]                                     # remove block + trailing blanks (## H now at s)
assert lines.count("### D.Feature -- Bucket A (near-term)")==1, "D.Feature-A header not unique"
fa = lines.index("### D.Feature -- Bucket A (near-term)")
ins = fa+1
if ins < len(lines) and lines[ins]=="": ins += 1   # past the blank under the header
lines[ins:ins] = block + [""]

t = "\n".join(lines)
assert all(ord(c)<128 for c in t), "non-ASCII"
assert sum(1 for l in lines if l.startswith("#### [L-")) == nL0, "L-block count changed"
assert t.count("section:G\b")==0
open(PATH,"w",encoding="utf-8").write(t)
print("OK patch4 applied")
