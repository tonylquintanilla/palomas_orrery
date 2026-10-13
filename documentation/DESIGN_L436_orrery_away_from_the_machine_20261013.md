<!-- Doc-Kind: hand | Design note, an idea and not a plan: using the orrery while Tony is away from his machine. What drives it, what the linked-computer session can and cannot do today, why a Pyodide port of the orrery is the wrong road, and the two routes that fit. Tony, 2026-10-13: "it's just an idea." -->
# Note: the orrery away from the machine (L-436)

Built on orrery 87a5470 at
https://github.com/tonylquintanilla/palomas_orrery (v3.93); gallery read
at f9453ddbc8b29ed15550a4e980bf3688eed79c82 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Neither
is touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 13, 2026 with Anthropic's Claude Fable 5.1, in the
coordination session of October 12 and 13.

- Type: DESIGN note (zero code). An idea recorded on first mention so
  it is not lost; nothing here is scheduled.
- Ledger: L-436, opened by `patch_L436_1_idea_20261013.py` in section
  D.Feature-C (architecture; design before code), unscored.

## 1. What drives it, in Tony's words

"I am often away from my machine." (2026-10-13)

The question came in three steps across two days. Could the dashboard
be operated from the phone through the linked session? Could a patch
and the maintenance run be run that way, stopping at the push? Could
the orrery itself be run from the phone, picking the Sun, Mercury,
Venus, Sedna and Voyager 1 at 0 hours and reading the hovers? And
then: could the orrery's window be converted to Pyodide (Python
running inside a browser) to run it remotely?

## 2. What the linked session can do today, measured in this session

The desktop app links a chat to Tony's computer. The link is to the
computer, not to the device he is holding, so it works from the phone
while the computer is awake and the app is open.

- It can read and write files in the connected repository folder.
  This session did both: patches and briefs were saved straight into
  `palomas_orrery_for_github\` on 2026-10-12 and 13.
- It can run a command on the computer. Not yet tried in this session;
  the first try should be the maintenance run alone, to see the shell
  and the approval prompt work.
- It cannot click. The orrery, Gallery Studio, the exhibit store editor
  and the guest book updater are windows or y/n prompts; they need a
  person at the screen.
- It cannot see a render. The look that accepts a visual change (Mode
  5) stays at the machine.
- The push stays at the machine, in GitHub Desktop, by Tony's choice:
  the patch-and-push routine is the one way a change reaches the
  repository, and the protocol rests on it.

So from the phone: "run the patch and the maintenance run, stop at the
push" works for the two mechanical steps and gets the output read back
with a red row explained; the look and the push wait for the machine.
For a records-only patch (no render), everything but the push.

## 3. Why not Pyodide

Pyodide runs Python inside a browser page with no install. Four
things stand in the orrery's way, in order of weight:

- **The window.** The orrery's controls are tkinter, a desktop toolkit
  that does not exist in a browser. Every control would be rebuilt as
  a web page: a second orrery, not a port.
- **The network.** The orrery's method is "ask Horizons live". A browser
  page may only call sites that permit it, and JPL's Horizons does not
  send that permission, so the page could not reach it directly;
  someone would host a relay in between.
- **The libraries.** plotly and numpy run in Pyodide; astroquery and
  astropy are the fetch layer, which the network problem already stops.
- **The data.** The orbit cache, the star catalogues and the climate
  files are hundreds of megabytes read from disk; a page would download
  what it needs each time.

The protocol's own words (The Orrery and the Assembler): "The assembler
exists because the orrery's Python requirement is a wall between the
work and everyone who isn't Tony." The website IS the orrery running
remotely. It solves the network by having the orrery fetch once and
serve the recipe, and it solves the window by being a page from the
start. Stage 15 of the road is the goal line: the website does what the
desktop orrery does, with a date to choose. A Pyodide port would be a
second attempt at that goal with the hard parts left in.

## 4. The two routes that fit, if the idea is taken up

- **A headless hover script in the orrery.** A small tool that takes a
  list of body names and a date, fetches their positions through the
  same functions the plot uses (`format_detailed_hover_text` and its
  dispatch), prints each hover, and saves the HTML the plot would save.
  Then "plot these five at 0 hours and read me the output" is a command
  the linked session can run from the phone, with the real JPL answers.
  It gives the words and the digits; not the render. A tool, not a
  patch: it gets a dashboard button and the checker treats it as a
  reader of the hover, not a second way of building one. It fits L-401
  build 3's session, which opens the fly-to and parameters paths.
- **The website's rooms**, which already open on the phone. Build 3 of
  L-431 brings the periods there; stage 11 brings the rest of the
  objects. This is where the effort already goes.

## 5. Tony's actions

- (decide, recorded, not urgent) Whether the headless hover script is
  added to L-401 build 3's scope, or waits. Default: waits; it is a
  convenience, not a slice.
- (do, when convenient) The first test of running a command from the
  phone: the maintenance run alone, output read back.

Note written October 2026 with Anthropic's Claude Fable 5.1.
