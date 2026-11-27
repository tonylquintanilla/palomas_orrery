<!-- Doc-Kind: hand | Review request, the second on L-560 (a digit is earned), for an outside model (GPT or Gemini), carried by Tony: the style in which a distance is shown to a lay visitor, in au and in kilometres; whether any standard exists to lean on, with a search of the Adler and Hayden planetariums; and one source for spacecraft. Communication. -->
# Review request: in what style should a public page show a distance?

For Tony: paste everything below the line into GPT and into Gemini, and
bring both replies back to a session.

---- paste below this line ----

Built on orrery 8678143278ab5c3872776f236d69cfb468e2eee2
at https://github.com/tonylquintanilla/palomas_orrery (branch main)
and website 95bdd6a04c8a68c8968a30824710eb6d70138a77
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(branch main), both read 2026-11-27, 12:34 Chicago. This is the second
request on the same subject. The first, and both replies to it, are in
the orrery repository at that commit:
`documentation/REVIEW_REQUEST_L560_printed_precision_20261127.md` and
the two files in `documentation/worksheets/` whose names end
`_L560_printed_precision_review_RETURN_20261127.md`. Everything you
need is in this request; those are there if you can fetch them.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Rules this work runs under. If you can fetch from GitHub, read
`PROJECT_INSTRUCTIONS.md` and `skills/provenance-discipline/SKILL.md`
in the orrery repository at the commit above, and say in your reply
which of the two you actually read. If you cannot fetch, say so; the
two rules that matter here are these:
- A number or a practice is either found at a source or it is not
  asserted. A plausible answer from memory is not acceptable. If you
  cannot quote a source, say "recalled, not verified", or say you do
  not know. "I do not know" and "none found" are good answers.
- A citation must be true, not just present. For every claim about
  what an institution does, give the page, its link, and a short exact
  quotation, or say plainly what you looked at and did not find.

Who you are writing for. Tony Quintanilla is a retired civil and
environmental engineer, an artist and an anthropologist. He is not an
astronomer and not a programmer. He makes every decision on this
project. Write in plain language and explain a technical term the
first time you use it. Do not propose code.

## The situation

Paloma's Orrery (palomasorrery.com) is a public website that draws the
solar system from NASA JPL's Horizons positions. When a visitor taps a
body, a box prints its distance. Today it reads like this:

    0.32001664 AU from the Sun (47,873,807 km)

After the first review Tony approved a rule, in five statements:

1. At most four significant figures, in both units alike. This is an
   editorial choice for the reader, said once on the page as such, and
   not a claim about accuracy.
2. Fewer when the evidence is coarser. Where a sourced uncertainty is
   larger than the fourth figure, the distance is rounded to the place
   that uncertainty supports, at three sigma where the source gives a
   sigma.
3. The evidence must fit the distance printed: this body, from this
   centre, on this date.
4. No source, no number. The marker and path stay, with the position's
   source named. No figure ever stands beside a disclaimer.
5. Say what each thing is. A rounding place we chose is never called
   JPL's uncertainty.

The rule says how many figures. It does not yet say how they are
written. Tony's concerns, in his words:

- "we use au and km as standard units. The same 4 digits will read
  differently and maybe even as zero. If we used scientific notation
  different again."
- "Is there a standard that we can pick? Maybe a national level
  planetarium that we can lean on for a standard?"
- "I don't think it makes sense for the spacecraft to go blank. JPL
  knows where they are."

## The style we are weighing, not yet approved

- The astronomical unit as a plain decimal with four significant
  figures: 0.3200, 172.5, and for the Moon from Earth 0.002570.
- Kilometres from the same four figures, with the scale as a word
  once the number is large: 384,400 km; 47.87 million km; 25.80
  billion km.
- No scientific notation.
- Open: whether to print "AU", as now, or "au".

## What we found, to be checked by you

We read these through a search tool's results, not the pages
themselves. Please check each.

- NASA prints distances for the public in at least three ways. Its
  Voyager status page, in a copy saved in October 2025, gave the
  distance from Earth as "15,709,189,949 mi" and "168.99637871 AU"
  (https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/).
  Its Planetary Fact Sheet gives the planets' distances from the Sun
  in millions of kilometres, "57.9", "108.2", "149.6", and the Moon's
  from Earth as "0.384"
  (https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html). Its
  prose writes "about 122 AU, or about 11 billion miles (18 billion
  kilometers)" (https://www.jpl.nasa.gov/interstellarvoyager/).
- The International Astronomical Union, in its 2012 Resolution B2,
  fixed the astronomical unit at exactly 149 597 870 700 m and asked
  that the symbol "au" be used.
- We found no standard from a planetarium. We did not search any
  planetarium ourselves; question 2 is that search.

## The questions

1. Is there a published standard or style guide for how a distance in
   the solar system is written for the public: how many figures, which
   units, how large numbers are written? Please look at least at NASA's
   own style guidance, the IAU's style manual, the style guides of the
   astronomy journals, the Astronomical Almanac, NIST's guide to the SI
   (Special Publication 811), and the planetarium and science-museum
   associations. Name what exists, with its place and a link. If
   nothing governs this, say so.

2. A search of two planetariums: the Adler Planetarium in Chicago and
   the Hayden Planetarium at the American Museum of Natural History in
   New York. For each: on its public web pages, and in any software or
   data it publishes for the public, how is a body's distance written?
   Which units, how many figures, what format for large numbers? Does
   either publish a guideline for this? Give the page, its link and a
   short quotation for each thing you report. If you find nothing for
   one of them, say what you looked at.

3. NASA's practice. Check our three examples above. Is any of the
   three closer to an official NASA style than the others? Does NASA's
   Eyes on the Solar System show a body's distance, and in what form?

4. The style we are weighing. What is wrong with it, or could mislead
   a lay reader? In particular:
   a. Kilometres as "47.87 million km" against "47,870,000 km" against
      scientific notation. Do trailing zeros read as exact? Which do
      reputable public sources use?
   b. Small values in astronomical units. The Moon from Earth is
      0.002570. Do reputable sources switch unit by scale, kilometres
      alone for a moon from its planet and astronomical units beyond?
      Is switching better for the reader than one pair of units
      everywhere?
   c. When the same four figures are converted between the two units,
      can the two printed numbers disagree with each other, and how do
      careful sources avoid that?
   d. "AU" or "au" for a public page, given the IAU's resolution and
      NASA's habit.
   e. Thousands separators, and "billion", for readers outside the
      United States.
   f. Miles. The site prints none. For a lay audience that is mostly
      in the United States, is that a real loss?

5. Spacecraft. With a ceiling of four significant figures, the page
   needs only to show that a tracked craft's distance is known better
   than about one part in ten thousand. Is there one citable source
   that supports this for interplanetary spacecraft as a class, for
   the part of a trajectory that is fitted to tracking data? An
   earlier reply named Thornton and Border, "Radiometric Tracking
   Techniques for Deep-Space Navigation" (JPL's DESCANSO series); we
   have not read it. Give the quotation and its place. Please keep
   apart: a trajectory fitted to tracking data; an ended mission at
   its last contact; and a predicted path.

6. Anything in the rule and the style together that a professional
   would call wrong, or that would mislead a lay reader.

## What to send back

- An answer to each question by its number, the plain answer first.
- For every claim about a source or an institution: the page, its
  place, a link, and a short exact quotation; or the words "recalled,
  not verified"; or "none found", with what you looked at.
- Which of the project's rule files you read, or that you could not
  fetch them.
- Your model's name and version, as you know it.

Written November 2026 with Anthropic's Claude Fable 5.2.
