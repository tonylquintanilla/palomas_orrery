<!-- Doc-Kind: hand | Design record: Tony's rulings on what "the website and the orrery agree" means (L-484), from the design talk of Nov 3, 2026. -->
# Design record: what "the two agree" means (L-484)

Tony Quintanilla, PE | Claude Fable 5.1 (design session, high effort) | November 3, 2026, 09:27 to 10:13 Chicago

Built on orrery 526a527f0d60288853e799f0e4b9783db84d0ae4 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
3a211a8cf10a3002668a85836f31bf973e385f2c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both read
live on Nov 3 (orrery about 15:07 UTC, gallery about 15:50 UTC). The
coordinating session's edits of this morning to LEDGER_CONSOLIDATED.md
and documentation/WHERE_WE_ARE.md were NOT pushed when this talk ran;
this record was written from the handoff Tony attached
(documentation/HANDOFF_L484_consistency_talk_20261103.md, his local
copy) and from the files on GitHub at the SHAs above.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\,
gallery C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\.

Type: DESIGN SESSION, zero code. Tony ruled from his phone, away from
his computer. This session could not reach his folders (its own
permission system refused the folder request; Tony was shown no prompt),
so it wrote this record in its own workspace and handed it to him as a
file. He places it in documentation/.

What was read before the talk: L-484 (the two agree) in full, from
LEDGER_CONSOLIDATED.md at 526a527f; interactive-exhibit 1.30, the bullet
"The website and the orrery agree on every object both draw, or the
difference is written down" (skills/interactive-exhibit/SKILL.md at
526a527f, the repo copy, not the account's installed copy);
provenance-discipline 2.36, What a Visitor Reads (repo copy at
526a527f); the protocol's The Artifact Bounds the Audit and The Braid
(the Project page, v3.122); L-476 (the orrery plots by the path plan);
celestial_objects.py and data/path_plans.json at 526a527f for section 7.

## 1. Why the talk happened

Tony, Nov 3, 08:59: "Yes let's do L 484. Because that consistency is
also a general check of the website. But I think it warrants a talk
about what we mean by consistency beyond narrow JPL parameters."

The standing rule (Tony, Oct 24; L-484; interactive-exhibit, under
Provenance): for every object both instruments draw, they agree on its
JPL record, its name, its dates and its words, or the difference is a
documented exception. The check that holds this is not built. This
talk said what "agree" means for each kind of thing, so the check can
be designed and then built.

## 2. The rulings, in the order they were made

Each ruling is Tony's; the shape under it is what the ruling means
for the check, as stated in the talk and not objected to.

### Ruling 1. The words have one home (09:27): "The same home."

The question was whether, for the words a visitor reads, "agree" means
THE SAME or NEVER CONTRADICTS. Tony chose a third standard, proposed
in the talk: the same home.

- A sentence a visitor reads on the website is either copied from the
  orrery's export, or it is listed in the exceptions file with its
  reason. Nothing else is allowed.
- A tool can check that: every website string traces to an export
  field or to the exceptions file. "Never contradicts" could not be
  checked by a tool; it would be a human read every build.
- Contradictions are stopped by construction, not caught afterwards.
  The mirrored description already works this way; the hovers,
  tooltips, text boxes and i panel do not yet.
- The cost: the website's shorter phone text is the orrery's text cut
  by a rule (the first sentence, the first few bullets), not rewritten.
  A rewritten sentence is an exception with a reason. So the orrery's
  export carries the words the website shows.
- The cutting rule itself is METHOD (Method Belongs to the Skill): it
  is written into interactive-exhibit when the check is designed, not
  put to Tony.

### Ruling 2. The orrery is the authority on every layer (stated 09:31, not objected to).

Stated in the talk as a consequence of Ruling 1 and of L-395 ("the one
definition of each object"), and left standing: the orrery is the
authority for identity, numbers, dates, words and the MEANING of the
picture. The website holds nothing of its own except its exceptions.

### Ruling 3. Two kinds of exception, kept apart (09:35): "Keep them apart."

- A CHOSEN DIFFERENCE carries a reason and Tony's date, and prints
  quietly every run. It has no end condition. Galileo's gold against
  the orrery's white is one.
- An OPEN DIFFERENCE carries an end condition and its ledger handle,
  and prints as a warning every run until it closes. The main belt's
  kilometres (L-503) was one; it closed when the export served them.
- An UNDOCUMENTED DIFFERENCE fails the run (already ruled, L-484).
- Why apart: if both kinds share one list, the chosen differences
  never close and the list stops meaning "something to fix." That is
  the normalization of deviance Tony names from his operating days.
- Where the exceptions live, the file's name and its fields, are
  METHOD for the check's design (gallery-cache-builder or
  interactive-exhibit, whichever the brief judges). The shape already
  ruled: a file the check reads and prints every run, not ledger prose.

### Ruling 4. The check is bounded by what both draw (09:41): "By what both draw."

- The check examines only objects the orrery defines and the website
  shows. This is The Artifact Bounds the Audit read narrowly, and it
  keeps the denominator closed and countable.
- Tony's reason, in his words: "And Galileo's dates already violate
  this. This was the reason for this review." Both instruments draw
  Galileo; its dates disagree; the check must catch exactly that.
- The alternative put to him, bounding by everything the website
  shows, was declined. Its consequence is recorded so it is not
  re-argued: the five website objects with no orrery key (the Moon,
  Io, Titan, Pluto's body, Charon) are OUTSIDE the check. They stay
  the documented class already on L-484, printed by name every run
  and not a failure, and each enters the check when it gets a key.
  The Braid: record, don't chase.
- What "a general check of the website" means after this ruling: the
  check holds the website to the orrery on the objects both draw. The
  website's other numbers are held by the config mirror and Store
  drift already (handoff section 2); this check does not reach them.

### Ruling 5. The layers of agreement (09:45): "Agree."

Five layers for the check, and one class beside it:

1. The same object: the same JPL record and the same name.
2. The same numbers, on shared objects: every number a visitor reads
   about the object prints from the same sourced row.
3. The same span of time: a path drawn over the same dates.
4. The same words: the orrery's export, or a listed exception
   (Ruling 1).
5. The same picture meaning: solid for flown and dashed for
   predicted; the same symbol for the same kind of thing. Colour is a
   chosen difference (Ruling 3). A tool checks solid-against-dashed
   from the path plan; colour stays Tony's look.

Beside the check, not a layer: THE SAME SET, the class of website
objects with no orrery key (Ruling 4).

The handoff's layer 6 (the same set) became the class; its layer 2
narrowed to shared objects by Ruling 4.

### Ruling 6. The typed dates come out of the object list (10:06, 10:13).

Tony, 10:06: "we should simply by removing the typed end_date and rely
on the JPL mission_end dates. And the same for start dates." Asked
whether the start comes from JPL's first day of positions or from a
sourced launch date, Tony, 10:13: "Yes JPL's first day of positions,
which often start after launch. That is the reason I usually typed
them to start the day after launch but using JPL positions should be
the rule."

- A spacecraft's span is JPL's own first and last day of positions,
  read fresh each time the plan is made. An ended mission stops at
  mission_end, NASA's date, because JPL's positions run past the truth
  at the end (Galileo's run nine days past the impact). Nothing like
  that happens at the start, so there is no launch field: a typed
  launch would be another copy, with a citation.
- A live mission has no end date anywhere; its end is wherever JPL's
  positions stop. That is already how Juno and the others work.
- The typed start_date and end_date are removed from
  celestial_objects.py for spacecraft. What this touches, read at
  526a527f: path_plan.py never reads end_date (it asks to the year
  2100 and JPL clips), but it asks FROM start_date, so the plan must
  ask from a date before any launch and let JPL clip the front as it
  clips the back; its guard that skips an entry with no start_date or
  end_date (path_plan.py line 1132) must change or it skips every
  spacecraft; the orrery's own plot (palomas_orrery.py,
  create_dates_list_for_object) and the 51 typed checkbox labels
  (L-476) read the span from the plan instead. Check All Parallel
  Pipelines before the build: the export and the website's mirror
  carry the plan's span already.
- Scope: spacecraft only. Comets' windows follow the comet-span ruling
  of Oct 24 (documentation/COORD_L443_comet_span_ruling_20261024.md),
  not this.
- This is L-476's design, made sharper: not "the orrery reads the plan
  too" but "the typed copies are gone." It is Ruling 1, the same home,
  applied to dates inside the orrery.

## 3. How the check fails (already ruled before this talk; restated)

An undocumented difference fails the run. A documented one prints with
its reason, every run. A planted fault proves the check can fail (the
protocol's A Check That Cannot Fail Is Not Passing).

## 4. The first findings the check will make

Inside the bound today, from the code at 526a527f:

- Galileo, layer 3. The website draws by the path plan, whose span
  ends 2003-09-21, the impact (data/path_plans.json, made 2026-11-03,
  from mission_end). The orrery's plot draws to the typed end_date,
  2003-09-29 (celestial_objects.py line 942), eight days past it.
- Cassini, layer 3. Plan span ends 2017-09-15 (mission_end); typed
  end_date 2017-09-14 (line 964), a day short.
- Galileo, layer 5. Gold on the website, white in the orrery: a chosen
  difference, to be written into the exceptions file when it exists.

## 5. Why Galileo and Cassini do not conform (Tony's question, 09:45)

Tony's understanding, confirmed from the code: the typed dates in the
object definitions, written by hand long ago, are the cause.

- Every spacecraft in celestial_objects.py carries a start_date and an
  end_date typed by hand. The orrery's ordinary plot spreads its points
  across those two dates (palomas_orrery.py,
  create_dates_list_for_object). L-476 lists seven other spacecraft
  whose typed dates have drifted from JPL's spans.
- Galileo's typed end is where JPL's positions stop, about nine days
  past the impact, on a path leaving Jupiter as if it never hit (found
  Nov 2, L-507; Tony: "Yes stop at impact").
- On Nov 2 both objects gained a mission_end field from NASA's page.
  The path plan stops there and the website draws by the plan. The
  typed end_date was left as it was, and the orrery's plot still reads
  end_date, not mission_end and not the plan. The orrery holds three
  copies of when Galileo ends and its plot reads the oldest.
- The fix is L-476 as written: the orrery's plot takes its span from
  the plan, and the typed dates stop being a second copy. That is
  Ruling 1 applied inside the orrery itself.

## 6. Where each ruling goes next

By the records skill, a design record carries rulings until they are
moved out: decisions to the ledger, method to a skill. This session
could not edit the ledger or Where We Are (their copies on GitHub
predate this morning's unpushed edits; a complete file from that base
would overwrite them). So:

- For L-484 (the two agree), a dated line, to be added by the next
  session at Tony's machine or by a records patch: "2026-11-03, the
  design talk's rulings (DESIGN_L484_consistency_rulings_20261103.md):
  the words have one home, the orrery's export; the orrery is the
  authority on every layer; exceptions are two kinds kept apart,
  chosen (reason, date, no end) and open (end condition, handle);
  the check is bounded by what both draw; five layers (object,
  numbers, span, words, picture meaning) and the unkeyed class
  beside them." Its Gap becomes: the brief for the check's build,
  then the build with a planted fault.
- For L-476 (the orrery plots by the path plan), a dated line: "2026-11-03,
  Tony's ruling (DESIGN_L484_consistency_rulings_20261103.md, Ruling 6):
  the typed start_date and end_date come out of the object list for
  spacecraft; the span is JPL's first and last day of positions, an
  ended mission stopping at mission_end; the plan asks from before any
  launch and lets JPL clip the front; its no-dates guard changes; the
  plot and the checkbox labels read the plan." Its Gap: the brief for
  that build, which is the same build as the orrery plotting by the
  plan. The method (how the plan asks and clips) goes to
  horizons-orbital-mechanics at its next version.
- For interactive-exhibit, at its next version: Rulings 1, 3 and 5
  are method (the same-home test for words, the cutting rule, the two
  kinds of exception and their printing, the five layers). Ruling 4
  joins the Provenance bullet as the check's bound.
- For Where We Are: stage 12c's line reads "talk done Nov 3, rulings
  in DESIGN_L484_consistency_rulings_20261103.md; next, the brief for
  the check." The design-talk list loses this item.
- The brief for the check's build is written when that build is next,
  not now (Token Economy: no speculative documents).

## 7. Housekeeping found during the talk, not for now

- The Project's instructions page on claude.ai reads v3.122. The repo's
  PROJECT_INSTRUCTIONS.md at 526a527f is v3.123, with four skills
  bumped (interactive-exhibit 1.30, orrery-coding-conventions 1.13,
  horizons-orbital-mechanics 1.14, gallery-cache-builder 1.17). Tony
  (09:27): "Not at my machine and will update the ui on my return."
  The next session that loads those skills from the account confirms
  its copy reads the new versions before work that fires them. This
  talk read the two skills it needed from the repo at the SHA, so
  nothing here depended on the installed copies.
- The coordinating session's edits to the ledger, Where We Are and the
  handoff are still to be committed and pushed in GitHub Desktop,
  together with this record.

Token count: this environment prints no count. Read: the handoff (119
lines), L-484 and L-476 in full, two skill sections, the v3.123
protocol entry, four short reads of celestial_objects.py and
data/path_plans.json. Written: this record.

Written November 3, 2026 with Anthropic's Claude Fable 5.1.
