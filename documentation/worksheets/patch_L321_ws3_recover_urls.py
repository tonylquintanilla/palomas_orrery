"""
patch_L321_ws3_recover_urls.py

Merges the twenty source URLs recovered from GPT 6 Medium's own exported
markdown into the Claude transcription of worksheet 3, and replaces that
file's transfer-gap banner, which is now false.

HOW TO RUN
    Save this file into documentation/worksheets/ -- the same folder as
    the .md it edits -- open it in VS Code, and click Run.
    Equivalent command line: python patch_L321_ws3_recover_urls.py

WHY
    The transcription was built from a paste in which every URL had
    collapsed to a dead link chip, so each address was marked
    "[url lost]" and the file opens with a banner saying no row may
    clear a citation.

    That banner is now wrong for THIS worksheet. GPT's own exported
    markdown, filed beside it as
    GPT6_medium_worksheet_3_van_allen_belts.md, preserved all twenty
    addresses as live links. Worksheets 1 and 2 exported with none, so
    their banners stay as they are.

    One address is worth noting. GPT gave Koskinen and Kilpua sec. 1.1
    as link.springer.com/chapter/10.1007/978-3-030-82167-8_1. The
    2026-09-13 source-recovery pass reached the identical URL by search,
    without seeing GPT's. Two routes, one address, neither informed by
    the other.

WHAT IT CHANGES
    1. Twenty "[url lost]" markers in the Source column become the real
       addresses, nine distinct sources, counts asserted individually.
    2. The banner heading and its item 1 become a recovery note. Item 2,
       the absent vocabulary line, stays: GPT's own file has no
       vocabulary line either, so that gap is real and unchanged.

    The table's verdicts, values and Notes are untouched. This is a
    transcription being completed, not a worksheet being revised.

PERMANENT HALF
    None. One-shot. The fingerprint below describes a file that stops
    existing the moment this succeeds. Leave the script here once run.

Written September 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "worksheet_gpt-6-medium_L321_van_allen_belts_20260913.md"
FINGERPRINT = "5b9ebe1e3c414eff7c3a139c45f7a8f8"

# (source name as written in the file, its URL, how many times it appears)
SOURCES = [
    ("Baker et al. (2018)",
     "https://link.springer.com/article/10.1007/s11214-017-0452-7", 7),
    ("Li et al. (2015)",
     "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014JA020777", 3),
    ("Li et al. (2025)",
     "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2024JA033504", 4),
    ("Selesnick et al. (2014)",
     "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014JA020188", 1),
    ("Koskinen and Kilpua, sec. 1.1",
     "https://link.springer.com/chapter/10.1007/978-3-030-82167-8_1", 1),
    ("Maiti and Ramachandran (2023), preprint",
     "https://arxiv.org/html/2310.08322v1", 1),
    ("Y. X. Li et al. (2023), full paper",
     "https://www.eppcgs.org/article/pdf/preview/10.26464/epp2023009.pdf", 1),
    ("University of Minnesota, mission announcement (2012)",
     "https://cse.umn.edu/college/news/university-minnesota-led-experiment-fly-nasa-mission-earths-radiation-belts", 1),
    ("Shi et al. (2020)",
     "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019JA027309", 1),
]

OLD_BANNER = b"""## Transfer gap -- read this before citing any row

This return reached the project as pasted plain text rather than as a
file. Two things are missing, and until both are restored no row here
may be used to clear a citation.

**1. Every URL is gone.** The worksheet asked for the URL actually
opened for each source. In the text that arrived, each address had
collapsed to a link chip carrying no address. Those positions are
marked `[url lost]` below. The source NAMES and the access words
survived; the addresses did not. An access word with no URL is an
assertion about a read, not a record of one, which is the shape the
Access Standard exists to refuse.

This matters more on this worksheet than on the other two. Rows 3, 8
and 9 are the DISCOVERY rows, and this checker answered all three by
naming a source that states the figure -- Koskinen and Kilpua for the
inner belt span, Y. X. Li et al. (2023) for the outer belt span, and a
University of Minnesota mission page for the outer altitude pair.
Those three addresses are the most load-bearing in the round.

"""

NEW_BANNER = b"""## Transfer note -- how this file's addresses were recovered

This return first reached the project as pasted plain text, and every
URL died in the paste: each address had collapsed to a link chip
carrying nothing. The twenty addresses in the Source column below were
RECOVERED on 2026-09-13 from the checker's OWN exported markdown, filed
beside this document as `GPT6_medium_worksheet_3_van_allen_belts.md`,
which preserved all of them as live links.

So this worksheet's Source column is complete and its rows may be used
normally. Where this file and the authored file disagree, the authored
file wins: that one is the checker's output, this one is a
transcription of it.

One address is worth recording. GPT gave Koskinen and Kilpua sec. 1.1
as `link.springer.com/chapter/10.1007/978-3-030-82167-8_1`. The
source-recovery pass of the same day reached the identical URL by
search, without having seen GPT's. Two routes, one address, neither
informed by the other.

**Worksheets 1 and 2 are NOT in this condition.** The same checker's
returns for the magnetopause and the bow shock exported with no links
at all. Their transcriptions still carry the original gap banner, and
their access words still have no addresses behind them.

One gap survives here, unchanged.

"""


def fail(msg):
    print("ERROR: " + msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s is not in this folder. Put this script in "
             "documentation/worksheets/, beside the file it edits." % TARGET)

    with open(TARGET, "rb") as f:
        content = f.read()

    actual = hashlib.md5(content).hexdigest()
    if actual != FINGERPRINT:
        fail("%s is not the expected base.\n"
             "       expected md5 %s\n       found    md5 %s\n"
             "       Already patched, or it differs from the copy filed at "
             "orrery d194674d." % (TARGET, FINGERPRINT, actual))

    # 1. the banner
    if content.count(OLD_BANNER) != 1:
        fail("ANCHOR FAIL -- the transfer-gap banner did not match exactly once.")
    content = content.replace(OLD_BANNER, NEW_BANNER)
    print("ok   banner replaced")

    # 2. the addresses
    total = 0
    for name, url, expected in SOURCES:
        old = (name + " [url lost]").encode("ascii")
        new = (name + " " + url).encode("ascii")
        n = content.count(old)
        if n != expected:
            fail("ANCHOR FAIL -- %r: expected %d, found %d" % (name, expected, n))
        content = content.replace(old, new)
        total += n
        print("ok   %-52s x%d" % (name, n))

    if total != 20:
        fail("expected 20 addresses, merged %d" % total)

    left = content.count(b"[url lost]")
    if left:
        fail("%d [url lost] markers remain; the mapping is incomplete." % left)

    try:
        content.decode("ascii")
    except UnicodeDecodeError:
        fail("result is not ASCII.")
    if b"\r" in content:
        fail("result contains CR; line endings must stay LF.")

    with open(TARGET, "wb") as f:
        f.write(content)

    print("patch applied (%d bytes, 20 addresses merged, 0 markers left)" % len(content))
    print("Next: commit and push.")


if __name__ == "__main__":
    main()
