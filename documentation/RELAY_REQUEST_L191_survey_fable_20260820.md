# Relay request: L-191 display-text survey

**Built on `e1c64dc955ba3323312d9b23ed53547985fe32cb` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 20, 2026 with Anthropic's Claude Opus 5, for Claude
Fable 5.**

Files are readable at
`https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/e1c64dc955ba3323312d9b23ed53547985fe32cb/<path>`.
Pin that SHA. The repository moves, and a survey of a moving target
cannot be checked later.

You are being asked for a SURVEY, not a fix. Please read to the end
before starting; the last section says what not to do, and it is the
part most likely to be skipped.

---

## 1. Who you are writing for

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist and an anthropologist. He is **not a professional software
developer and not a formally trained astronomer.** He builds this
project through conversation with AI partners rather than by writing
code unassisted, and he holds sole commit authority and final judgment
on every decision.

The codebase you are about to read is NOT evidence of his personal
programming skill. Its structure and discipline are the product of two
years of iterative collaboration. Reading it cold, you will reasonably
infer that a skilled programmer wrote it. Don't let that inference set
your register: unpack technical terms on first use, and describe
operations rather than assuming command-line fluency.

What Tony does own personally is the method: the protocol, the ledger,
the master plan, the multi-model relay you are part of, and every
integration judgment. He directs; he does not rubber-stamp. If your
survey disagrees with what is written below, say so plainly. That is
the reason for asking you rather than continuing alone.

He works in VS Code using its Run button, and in GitHub Desktop for
commits. He does not use the git command line.

## 2. What the project is

Paloma's Orrery is a Python and Plotly visualization suite: a 3D solar
system model, a stellar neighbourhood viewer, and an Earth-system
climate hub. Roughly 86,000 lines across about 100 modules. It is named
after Tony's daughter, and its working motto is "Data Preservation is
Climate Action."

Two details matter for this job:

- The desktop application has a **Tkinter** GUI -- Python's standard
  windowing toolkit. Its tooltips are plain text labels. They have no
  HTML parser.
- The plots are **Plotly** figures rendered in a browser. Their hover
  text IS HTML, so a line break there is written `<br>`.

The same descriptive prose is shown on both surfaces.

## 3. The symptom

On August 20, 2026, Tony hovered a checkbox in the desktop GUI and read
literal `<br>` tags in the tooltip text, where line breaks should have
been. The browser hover for the same content rendered correctly.

Read it in `LEDGER_CONSOLIDATED.md` at the repository root: search for
the heading `#### [L-191]` and read the whole item, about eighty lines.
It is your starting brief, not your conclusion -- see section 6.

## 4. What is already established, and is not yours to re-derive

These are requirements and history. Take them as given.

**The intended design, from April 2025.** A string named `<thing>_info`
carries `\n` and feeds the Tkinter tooltip. A string named
`<thing>_info_hover` carries `<br>` and feeds the Plotly hover. Two
names, two formats, one meaning. The naming convention still says so.

**The regression.** A commit in May 2026 converted `\n` to `<br>` in
the tooltip variants as well, collapsing the distinction while the
names went on implying it held.

**The fix already exists elsewhere in the tree.** `shell_configs.py`
carries about sixteen sites of the form
`'hover_text': saturn_core_info.replace('\n', '<br>')` -- one string
authored in `\n`, converted to HTML at the Plotly boundary. That is the
target pattern. This job is not "invent a system"; it is "bring the
other modules into the pattern the codebase already uses," with a
working reference implementation to copy.

**A constraint that decides the design, and it is not in the module
with the visible bug.** The Earth shell text has the same duplication
with no visible symptom. Its crust description ends with a note telling
the reader to toggle the crust off in the legend to see the interior.
That note is deliberately ABSENT from the tooltip, because a legend
instruction is meaningless on a checkbox. So collapsing to one string
either loses that sentence or puts it where it does not belong. **Any
design must carry surface-specific text alongside the shared body.**
Design against Earth's harder case, not the solar module's easier one.

**Tony's standing ruling on this item:** survey before sweep. That is
why you are being asked to measure and design rather than to edit.

## 5. What we are asking you to produce

**(a) An inventory.** For every string in the codebase that reaches a
Tkinter tooltip, name it, give its defining module and line, and state
whether it currently contains `<br>`, `\n`, both, or neither. Resolve
each name from the `CreateToolTip` call site back to its definition;
several are passed through intermediate variables and one path runs
through `celestial_objects.py`.

**(b) A count, derived independently.** How many strings are actually
affected -- that is, reach a Tkinter surface AND carry `<br>`? Show how
you counted. See section 6 before you answer this.

**(c) A pattern map.** For each family of shells (solar, Earth,
gas giants, asteroid belt, and anything else you find), record: where
the tooltip text comes from, where the plot text comes from, whether
they are one string or two, and whether the two agree today.

**(d) The duplication risk, measured.** Where a family keeps two
copies, how many pairs are verbatim identical, how many differ
deliberately, and how many have no partner? A pair that agrees today
but has no mechanism keeping it in agreement is the failure we care
about most, because nothing on screen would reveal the drift.

**(e) A design, against Earth's constraint.** How should one string
serve both surfaces while still allowing surface-specific additions?
Give the mechanism, not just the principle, and say what it costs.

**(f) The order of work,** and what could go wrong at each step.

## 6. What has been deliberately withheld, and why

**The ledger records a count. We are not telling you what it is.**

We want yours derived from the code, so the two can be compared. If we
gave you ours, your answer could only agree with it, and we would learn
nothing.

There is a specific reason to want a second count here. Earlier today
the assisting model estimated the scope by counting `<br>` occurrences
in one file and reported a figure in the hundreds. That was wrong: the
count swept in the `_info_hover` strings, where `<br>` is correct and
required. The ledger records an earlier estimate that failed the same
way, for the same reason, and the model repeated it anyway. **A raw
`<br>` count is a proxy for the thing, not the thing.** Count what
reaches a Tkinter surface.

If your figure and the ledger's disagree, that is a useful result
either way, so please state your method precisely enough that the
disagreement can be located.

## 7. How to answer

- Ground every claim in a file and line at the pinned SHA. "About" and
  "several" are not usable here.
- Say what you could not determine. A path you could not resolve, a
  dynamic binding you could not follow, a file you could not read --
  report it as an open item and let it fail your own survey. Silence
  about something unexamined is the failure mode; an incomplete survey
  that says where it is incomplete is worth more than a confident one.
- Where you disagree with section 4, say so and show why.
- Separate what you MEASURED from what you INFERRED. Both are welcome;
  conflating them is not.

## 8. What not to do

- **Do not write patches, and do not edit files.** Survey first is
  Tony's ruling, and it is what produced everything useful in L-191.
  A sweep proposed before the surfaces are mapped will get the scope
  wrong, which is the mistake this item has already recorded twice.
- **Do not "fix" this at the tooltip** by normalizing `<br>` to a
  newline where the label is built. It was proposed today and rejected:
  it hides the symptom on one surface and leaves two copies of the text
  free to drift apart, which is the deeper problem. If you think that
  judgment is wrong, argue it -- but argue it, do not quietly assume
  it.
- **Do not touch the `_info_hover` strings' `<br>` tags.** They are
  correct.
- **Do not expand scope to the dead `tooltip` dictionary keys** in
  `shell_configs.py`. There are 124 of them, they are read by nothing,
  and their disposition is a separate open question for Tony.
